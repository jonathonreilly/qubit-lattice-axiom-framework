#!/usr/bin/env python3
"""Serialize citation-graph builds across local clones and worktrees.

This process-only launcher deliberately leaves the governed graph builder
byte-identical.  The lock is inherited across ``exec`` so it remains held by
the builder itself and is released automatically on normal exit or a signal.
"""
from __future__ import annotations

import fcntl
import hashlib
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
BUILDER_PATH = Path(__file__).with_name("build_citation_graph.py")

# GitHub redirects the former repository slug to the current one, but local
# checkout configuration retains whichever spelling was cloned.  Locking on
# the literal URL therefore split one repository into two serialization
# domains.  Keep this alias explicit and offline: lock acquisition must not
# depend on GitHub availability or credentials.
_GITHUB_REPOSITORY_ALIASES = {
    "jonathonreilly/cl3-lattice-framework": (
        "jonathonreilly/qubit-lattice-axiom-framework"
    ),
}
_GITHUB_REMOTE_PATTERNS = (
    re.compile(
        r"^(?:https?|git)://github\.com/([^/]+)/([^/]+?)(?:\.git)?/?$",
        re.IGNORECASE,
    ),
    re.compile(
        r"^(?:ssh://)?git@github\.com[:/]([^/]+)/([^/]+?)(?:\.git)?/?$",
        re.IGNORECASE,
    ),
)


def _canonical_remote_identity(remote: str) -> str:
    """Normalize equivalent GitHub transports and the known repo rename."""
    stripped = remote.strip().rstrip("/")
    for pattern in _GITHUB_REMOTE_PATTERNS:
        match = pattern.fullmatch(stripped)
        if match is None:
            continue
        slug = f"{match.group(1)}/{match.group(2)}".casefold()
        slug = _GITHUB_REPOSITORY_ALIASES.get(slug, slug)
        return f"github:{slug}"
    return f"origin:{stripped}"


def _repository_identity() -> str:
    """Return one local identity for independent clones of this repository."""
    origin = subprocess.run(
        ["git", "remote", "get-url", "origin"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    remote = (origin.stdout or "").strip()
    if origin.returncode == 0 and remote:
        return _canonical_remote_identity(remote)

    common_dir = subprocess.run(
        ["git", "rev-parse", "--git-common-dir"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    common = (common_dir.stdout or "").strip()
    if common_dir.returncode == 0 and common:
        path = Path(common)
        if not path.is_absolute():
            path = REPO_ROOT / path
        return f"common-dir:{path.resolve()}"
    return f"checkout:{REPO_ROOT.resolve()}"


def citation_graph_lock_path() -> Path:
    key = hashlib.sha256(_repository_identity().encode("utf-8")).hexdigest()[:20]
    return Path(tempfile.gettempdir()) / f"citation-graph-build-{key}.lock"


def main() -> int:
    lock_path = citation_graph_lock_path()
    with lock_path.open("a+", encoding="utf-8") as handle:
        try:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            print(
                f"Waiting for serialized citation-graph build lock {lock_path}",
                file=sys.stderr,
                flush=True,
            )
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX)

        # PEP 446 makes Python-created descriptors non-inheritable by default.
        # Preserve this one deliberately so the governed builder owns the
        # lock after exec; no launcher process remains to mishandle signals.
        os.set_inheritable(handle.fileno(), True)
        os.execv(
            sys.executable,
            [sys.executable, str(BUILDER_PATH), *sys.argv[1:]],
        )
    return 1  # pragma: no cover - os.execv either replaces us or raises


if __name__ == "__main__":
    raise SystemExit(main())
