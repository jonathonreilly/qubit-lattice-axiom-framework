#!/usr/bin/env python3
"""Sharded audit-ledger IO.

The git-tracked source of truth for the audit ledger is
``docs/audit/data/ledger/<claim_id[:2]>/<claim_id>.json`` (exactly one row
per file, one file per row) plus ``docs/audit/data/ledger_meta.json`` (every top-level
ledger key except ``rows``: schema_version, stats, last_invalidations).

The monolithic ``docs/audit/data/audit_ledger.json`` is an UNTRACKED
materialized cache kept byte-identical to the canonical pre-sharding
serialization, so every existing reader (``json.load`` sites, external
tooling) keeps working after ``ensure_cache()`` or a pipeline run. Writers
MUST go through ``save_ledger()``: a direct write to the cache is detected
via the manifest and refused at the next materialization instead of being
silently discarded.

Rationale (2026-07-13, owner-directed): git stores a full blob per commit
for every changed file; the ~61 MB monolith rewritten by every verdict was
~1.5 GB of packed history and grew ~170 KB packed per verdict. One-row
shards reduce a verdict commit to a few KB.

CLI:
  python3 ledger_io.py --materialize   # shards -> cache (pipeline step 0)
  python3 ledger_io.py --migrate       # one-shot: tracked monolith -> shards
  python3 ledger_io.py --verify        # shards <-> cache coherence check
"""
from __future__ import annotations

import argparse
import contextlib
import fcntl
import hashlib
import json
import os
import re
import sys
import tempfile
from pathlib import Path
from typing import Any

DATA = Path(__file__).resolve().parents[1] / "data"
MANIFEST_SCHEMA = "ledger_cache_manifest_v1"
_KNOWN_CACHE_SHA: str | None = None


def _shards() -> Path:
    return DATA / "ledger"


def _meta() -> Path:
    return DATA / "ledger_meta.json"


def _cache() -> Path:
    return DATA / "audit_ledger.json"


def _manifest() -> Path:
    return DATA / "ledger_cache_manifest.json"

FOREIGN_WRITE_ERROR = (
    "docs/audit/data/audit_ledger.json differs from the sharded ledger and "
    "was not written by ledger_io: the monolith is a generated cache, and a "
    "direct write to it would be silently lost. Re-apply the change through "
    "ledger_io.save_ledger() (or discard the cache file) and retry."
)
STALE_WRITE_ERROR = (
    "the sharded audit ledger changed after this writer materialized its "
    "input; refusing to overwrite a concurrent update. Reload the ledger "
    "and retry the operation."
)
UNPRIMED_WRITE_ERROR = (
    "save_ledger() requires ensure_cache() before loading a sharded ledger; "
    "refusing an unversioned full-ledger write that could overwrite a "
    "concurrent update."
)


def _dump(value: Any) -> str:
    return json.dumps(value, indent=2, sort_keys=True) + "\n"


def _sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _read_text(path: Path) -> str:
    """Read UTF-8 without universal-newline normalization."""
    with path.open("r", encoding="utf-8", newline="") as handle:
        return handle.read()


@contextlib.contextmanager
def _ledger_lock():
    """Serialize materialization and saves that share the same DATA root."""
    key = hashlib.sha256(str(DATA.resolve()).encode("utf-8")).hexdigest()[:20]
    lock_path = Path(tempfile.gettempdir()) / f"audit-ledger-{key}.lock"
    with lock_path.open("a+") as handle:
        fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)


def _atomic_write_text(path: Path, text: str) -> None:
    """Replace *path* atomically with a fully flushed UTF-8 text file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, raw_tmp = tempfile.mkstemp(
        dir=path.parent,
        prefix=f".{path.name}.",
        suffix=".tmp",
    )
    tmp = Path(raw_tmp)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp, path)
    except BaseException:
        tmp.unlink(missing_ok=True)
        raise


def sharded() -> bool:
    return _shards().is_dir()


def shard_path(claim_id: str) -> Path:
    """Fanout by the claim id's first two characters.

    A flat directory of ~3,750 shards makes the ledger/ tree object itself
    ~330 KB and git re-stores a changed directory's tree per commit; the
    two-character fanout keeps every tree small so a one-row change costs
    a few KB. The prefix is taken from the claim id (not a hash) so humans
    can predict a shard's path.
    """
    if not isinstance(claim_id, str) or not re.fullmatch(
        r"[A-Za-z0-9_-][A-Za-z0-9_.-]*", claim_id
    ):
        raise ValueError(f"claim id is not shard-safe: {claim_id!r}")
    return _shards() / claim_id[:2] / f"{claim_id}.json"


def load_ledger() -> dict:
    """Load the full ledger dict from shards (or the legacy monolith)."""
    if not sharded():
        return json.loads(_read_text(_cache()))
    rows: dict[str, dict] = {}
    for path in sorted(_shards().glob("*/*.json")):
        claim_id = path.stem
        expected = shard_path(claim_id)
        if path != expected:
            raise ValueError(
                f"ledger shard is in the wrong fanout directory: {path}; "
                f"expected {expected}"
            )
        if claim_id in rows:
            raise ValueError(f"duplicate ledger shard for {claim_id!r}")
        row = json.loads(_read_text(path))
        if not isinstance(row, dict) or row.get("claim_id") != claim_id:
            raise ValueError(f"ledger shard identity mismatch: {path}")
        rows[claim_id] = row
    meta = (
        json.loads(_read_text(_meta()))
        if _meta().exists()
        else {}
    )
    if "rows" in meta:
        raise ValueError("ledger_meta.json must not contain a rows key")
    return {**meta, "rows": rows}


def save_ledger(ledger: dict, *, _validate_cache: bool = True) -> dict:
    """Persist the ledger: changed shards + meta + refreshed cache.

    Returns a change summary {"changed": [...], "removed": [...],
    "meta_changed": bool} so callers can log commit-relevant deltas.
    """
    with _ledger_lock():
        return _save_ledger_locked(ledger, validate_cache=_validate_cache)


def _save_ledger_locked(ledger: dict, *, validate_cache: bool) -> dict:
    rows = ledger.get("rows")
    if not isinstance(rows, dict):
        raise ValueError("ledger must carry a rows dict")
    expected_sha = _KNOWN_CACHE_SHA
    if validate_cache and sharded():
        # Refuse a missed direct-cache writer before its in-memory result can
        # be laundered into authoritative shards by an otherwise ported writer.
        _ensure_cache_locked()
        if expected_sha is None:
            raise SystemExit(UNPRIMED_WRITE_ERROR)
        if _KNOWN_CACHE_SHA != expected_sha:
            raise SystemExit(STALE_WRITE_ERROR)
    folded: dict[str, str] = {}
    for claim_id, row in rows.items():
        shard_path(claim_id)
        prior = folded.setdefault(claim_id.casefold(), claim_id)
        if prior != claim_id:
            raise ValueError(
                "claim ids collide on a case-insensitive filesystem: "
                f"{prior!r}, {claim_id!r}"
            )
        if not isinstance(row, dict) or row.get("claim_id") != claim_id:
            raise ValueError(f"ledger row identity mismatch: {claim_id!r}")
    _shards().mkdir(parents=True, exist_ok=True)
    changed: list[str] = []
    removed: list[str] = []
    existing = {path.stem: path for path in _shards().glob("*/*.json")}
    for claim_id, row in rows.items():
        blob = _dump(row)
        path = shard_path(claim_id)
        if claim_id not in existing or _read_text(existing[claim_id]) != blob:
            _atomic_write_text(path, blob)
            changed.append(claim_id)
    for claim_id, path in existing.items():
        if claim_id not in rows:
            path.unlink()
            if not any(path.parent.iterdir()):
                path.parent.rmdir()
            removed.append(claim_id)
    meta = {key: value for key, value in ledger.items() if key != "rows"}
    meta_blob = _dump(meta)
    meta_changed = (
        not _meta().exists()
        or _read_text(_meta()) != meta_blob
    )
    if meta_changed:
        _atomic_write_text(_meta(), meta_blob)
    _write_cache(ledger)
    return {"changed": sorted(changed), "removed": sorted(removed),
            "meta_changed": meta_changed}


def _write_cache(ledger: dict) -> None:
    global _KNOWN_CACHE_SHA
    blob = _dump(ledger)
    _atomic_write_text(_cache(), blob)
    _atomic_write_text(
        _manifest(),
        _dump({"schema": MANIFEST_SCHEMA, "cache_sha256": _sha(blob)}),
    )
    _KNOWN_CACHE_SHA = _sha(blob)


def _manifest_sha() -> str | None:
    if not _manifest().exists():
        return None
    try:
        manifest = json.loads(_read_text(_manifest()))
    except json.JSONDecodeError:
        return None
    if manifest.get("schema") != MANIFEST_SCHEMA:
        return None
    value = manifest.get("cache_sha256")
    return value if isinstance(value, str) else None


def ensure_cache() -> bool:
    """Materialize the cache from shards; refuse foreign cache writes.

    Returns True when the cache was (re)written. No-op on pre-sharding
    checkouts (the tracked monolith IS the ledger there).
    """
    with _ledger_lock():
        return _ensure_cache_locked()


def _ensure_cache_locked() -> bool:
    global _KNOWN_CACHE_SHA
    if not sharded():
        return False
    ledger = load_ledger()
    blob = _dump(ledger)
    if _cache().exists():
        current = _read_text(_cache())
        if current == blob:
            if _manifest_sha() != _sha(blob):
                _atomic_write_text(
                    _manifest(),
                    _dump({"schema": MANIFEST_SCHEMA, "cache_sha256": _sha(blob)}),
                )
            _KNOWN_CACHE_SHA = _sha(blob)
            return False
        recorded = _manifest_sha()
        if recorded is None or recorded != _sha(current):
            raise SystemExit(FOREIGN_WRITE_ERROR)
        # Cache is ours but shards moved (git pull, direct shard edit): refresh.
    _write_cache(ledger)
    return True


def verify() -> str | None:
    """Return an error string when shards and cache disagree."""
    if not sharded():
        return None
    ledger = load_ledger()
    blob = _dump(ledger)
    if not _cache().exists():
        return "cache missing; run ledger_io.py --materialize"
    current = _read_text(_cache())
    if current == blob:
        return None
    recorded = _manifest_sha()
    if recorded is None or recorded != _sha(current):
        return FOREIGN_WRITE_ERROR
    return "cache is stale relative to shards; run ledger_io.py --materialize"


def migrate() -> dict:
    """One-shot: split the tracked monolith into shards + meta + cache."""
    if sharded() and any(_shards().glob("*/*.json")):
        raise SystemExit("ledger/ already contains shards; refusing to re-migrate")
    ledger = json.loads(_read_text(_cache()))
    summary = save_ledger(ledger, _validate_cache=False)
    round_trip = load_ledger()
    if _dump(round_trip) != _dump(ledger):
        raise SystemExit("migration round-trip mismatch; aborting")
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--materialize", action="store_true")
    group.add_argument("--migrate", action="store_true")
    group.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if args.migrate:
        summary = migrate()
        print(
            f"migrated {len(summary['changed'])} rows into "
            f"{_shards().relative_to(DATA.parents[1])}/ (round-trip verified)"
        )
        return 0
    if args.verify:
        error = verify()
        if error:
            print(error)
            return 1
        print("shards and cache are coherent")
        return 0
    wrote = ensure_cache()
    print("cache rematerialized" if wrote else "cache already current")
    return 0


if __name__ == "__main__":
    sys.exit(main())
