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
from urllib.parse import unquote, urlsplit


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
_GITHUB_SCP_REMOTE = re.compile(
    r"^(?:[^/@:]+@)?github\.com:(?P<path>[^?#]+)$",
    re.IGNORECASE,
)
_GITHUB_DEFAULT_PORTS = {
    "http": 80,
    "https": 443,
    "git": 9418,
    "ssh": 22,
}


def _checkout_identity(repo_root: Path) -> str:
    """Return a worktree-stable discriminator without consulting a remote."""
    common_dir = subprocess.run(
        ["git", "rev-parse", "--git-common-dir"],
        cwd=repo_root,
        capture_output=True,
        text=True,
    )
    common = (common_dir.stdout or "").strip()
    if common_dir.returncode == 0 and common:
        path = Path(common)
        if not path.is_absolute():
            path = repo_root / path
        return f"common-dir:{path.resolve()}"
    return f"checkout:{repo_root.resolve()}"


def _github_slug(remote: str) -> str | None:
    """Return a normalized GitHub slug for supported transports and ports."""
    stripped = remote.strip().rstrip("/")
    scp_match = _GITHUB_SCP_REMOTE.fullmatch(stripped)
    if scp_match is not None:
        path = scp_match.group("path").rstrip("/")
    else:
        parsed = urlsplit(stripped)
        scheme = parsed.scheme.casefold()
        if scheme not in _GITHUB_DEFAULT_PORTS:
            return None
        try:
            hostname = (parsed.hostname or "").casefold()
            port = parsed.port
        except ValueError:
            return None
        if hostname != "github.com":
            return None
        if port not in (None, _GITHUB_DEFAULT_PORTS[scheme]):
            return None
        if parsed.query or parsed.fragment:
            return None
        path = parsed.path.strip("/")

    parts = path.split("/")
    if len(parts) != 2 or not all(parts):
        return None
    owner, repository = (part.casefold() for part in parts)
    if repository.endswith(".git"):
        repository = repository[:-4]
    if not repository:
        return None
    slug = f"{owner}/{repository}"
    return _GITHUB_REPOSITORY_ALIASES.get(slug, slug)


def _local_remote_target(remote: str, repo_root: Path) -> Path | None:
    """Resolve a local Git origin with the same cwd-relative rule Git uses."""
    parsed = urlsplit(remote)
    if parsed.scheme.casefold() == "file":
        if parsed.query or parsed.fragment:
            return None
        if parsed.netloc not in ("", "localhost"):
            path = Path(f"//{parsed.netloc}{unquote(parsed.path)}")
        else:
            path = Path(unquote(parsed.path))
    elif parsed.scheme:
        return None
    elif re.match(r"^(?:[^/@:]+@)?[^/:]+:", remote):
        return None
    else:
        path = Path(remote).expanduser()

    if not path.is_absolute():
        path = repo_root / path
    return path.resolve()


def _opaque_remote_without_credentials(remote: str) -> str:
    """Remove URL userinfo before an opaque remote contributes to a lock key."""
    parsed = urlsplit(remote)
    if parsed.scheme and parsed.hostname:
        try:
            port = parsed.port
        except ValueError:
            port = None
        authority = parsed.hostname.casefold()
        if port is not None:
            authority = f"{authority}:{port}"
        return f"{parsed.scheme.casefold()}://{authority}{parsed.path}"

    scp_match = re.fullmatch(r"(?:[^/@:]+@)?([^/:]+):(.+)", remote)
    if scp_match is not None:
        return f"{scp_match.group(1).casefold()}:{scp_match.group(2)}"
    return remote


def _canonical_remote_identity(
    remote: str,
    *,
    repo_root: Path | None = None,
) -> str:
    """Normalize the known rename without aliasing unrelated repositories."""
    root = repo_root or REPO_ROOT
    stripped = remote.strip().rstrip("/")
    slug = _github_slug(stripped)
    if slug is not None:
        return f"github:{slug}"

    local_target = _local_remote_target(stripped, root)
    if local_target is not None:
        return f"local-origin:{local_target}"

    opaque = _opaque_remote_without_credentials(stripped)
    return f"opaque-origin:{opaque}|{_checkout_identity(root)}"


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
        return _canonical_remote_identity(remote, repo_root=REPO_ROOT)

    return _checkout_identity(REPO_ROOT)


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
