"""
Reusable Composio session helper for the Reddit connection.

Nothing here hardcodes a subreddit, sort order, time filter, or tool slug.
Callers discover the right tool at runtime via search() and invoke it via
run() — this keeps the tool general-purpose instead of locked to one
use case (e.g. "top posts from r/wallstreetbets").

Authentication is never performed here: if Reddit isn't connected for a
user, connection_status() returns a Connect Link for a human to open and
approve themselves.
"""

import os
import re
import time
from pathlib import Path

from dotenv import load_dotenv
from composio import Composio

_ENV_PATH = Path(__file__).resolve().parent.parent / ".env"
_DEFAULT_USER_ID = os.environ.get("REDDIT_TOOL_USER_ID", "zeela_default")

_client = None
_sessions = {}


def _get_client():
    global _client
    if _client is None:
        load_dotenv(_ENV_PATH)
        if not os.environ.get("COMPOSIO_API_KEY"):
            raise RuntimeError(f"COMPOSIO_API_KEY not found. Expected it in {_ENV_PATH}.")
        _client = Composio()
    return _client


def get_session(user_id: str = None):
    """Return a cached Composio session scoped to the Reddit toolkit for this user."""
    user_id = user_id or _DEFAULT_USER_ID
    if user_id not in _sessions:
        _sessions[user_id] = _get_client().sessions.create(user_id=user_id, toolkits=["reddit"])
    return _sessions[user_id]


def connection_status(user_id: str = None) -> dict:
    """Check whether Reddit is connected for this user.

    Returns {"is_active": True} when ready to fetch, or
    {"is_active": False, "connect_url": "..."} when a human needs to
    authorize first. Never completes the OAuth flow itself.
    """
    session = get_session(user_id)
    status = session.toolkits(toolkits=["reddit"])
    item = status.items[0]
    is_active = bool(item.connection and item.connection.is_active)
    result = {"is_active": is_active}
    if not is_active:
        result["connect_url"] = session.authorize("reddit").redirect_url
    return result


def search(query: str, user_id: str = None):
    """Discover the right Reddit tool(s) for a task.

    Always call this before run() for a new kind of request — never guess
    a tool slug. Read primary_tool_slugs / recommended_plan_steps /
    known_pitfalls from the result before executing.
    """
    return get_session(user_id).search(query=query)


def is_rate_limited(error) -> bool:
    """Reddit/Composio report rate limits as 'HTTP 429' or 'rate limit exceeded'."""
    return bool(re.search(r"429|rate[\s_-]?limit", str(error), re.IGNORECASE))


def run(tool_slug: str, arguments: dict = None, user_id: str = None, max_retries: int = 3) -> dict:
    """Execute one Reddit tool call, retrying with backoff on rate limits."""
    session = get_session(user_id)
    delay = 2.0
    last = None
    for attempt in range(max_retries):
        resp = session.execute(tool_slug, arguments=arguments or {})
        data = resp.model_dump() if hasattr(resp, "model_dump") else resp
        last = data
        error = (data or {}).get("error")
        if error and is_rate_limited(error):
            if attempt < max_retries - 1:
                time.sleep(delay)
                delay *= 2
                continue
        return data
    return last
