#!/usr/bin/env python3
"""Sharded audit-ledger IO.

The git-tracked source of truth for the audit ledger is
``docs/audit/data/ledger/<claim_id>.json`` (exactly one row per file, one
file per row) plus ``docs/audit/data/ledger_meta.json`` (every top-level
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
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

DATA = Path(__file__).resolve().parents[1] / "data"
MANIFEST_SCHEMA = "ledger_cache_manifest_v1"


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


def _dump(value: Any) -> str:
    return json.dumps(value, indent=2, sort_keys=True) + "\n"


def _sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


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
    if "/" in claim_id or claim_id in {"", ".", ".."}:
        raise ValueError(f"claim id is not shard-safe: {claim_id!r}")
    return _shards() / claim_id[:2] / f"{claim_id}.json"


def load_ledger() -> dict:
    """Load the full ledger dict from shards (or the legacy monolith)."""
    if not sharded():
        return json.loads(_cache().read_text(encoding="utf-8"))
    rows: dict[str, dict] = {}
    for path in sorted(_shards().glob("*/*.json")):
        rows[path.stem] = json.loads(path.read_text(encoding="utf-8"))
    meta = (
        json.loads(_meta().read_text(encoding="utf-8"))
        if _meta().exists()
        else {}
    )
    if "rows" in meta:
        raise ValueError("ledger_meta.json must not contain a rows key")
    return {**meta, "rows": rows}


def save_ledger(ledger: dict) -> dict:
    """Persist the ledger: changed shards + meta + refreshed cache.

    Returns a change summary {"changed": [...], "removed": [...],
    "meta_changed": bool} so callers can log commit-relevant deltas.
    """
    rows = ledger.get("rows")
    if not isinstance(rows, dict):
        raise ValueError("ledger must carry a rows dict")
    _shards().mkdir(parents=True, exist_ok=True)
    changed: list[str] = []
    removed: list[str] = []
    existing = {path.stem: path for path in _shards().glob("*/*.json")}
    for claim_id, row in rows.items():
        blob = _dump(row)
        path = shard_path(claim_id)
        if claim_id not in existing or existing[claim_id].read_text(
            encoding="utf-8"
        ) != blob:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(blob, encoding="utf-8")
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
        or _meta().read_text(encoding="utf-8") != meta_blob
    )
    if meta_changed:
        _meta().write_text(meta_blob, encoding="utf-8")
    _write_cache(ledger)
    return {"changed": sorted(changed), "removed": sorted(removed),
            "meta_changed": meta_changed}


def _write_cache(ledger: dict) -> None:
    blob = _dump(ledger)
    _cache().write_text(blob, encoding="utf-8")
    _manifest().write_text(
        _dump({"schema": MANIFEST_SCHEMA, "cache_sha256": _sha(blob)}),
        encoding="utf-8",
    )


def _manifest_sha() -> str | None:
    if not _manifest().exists():
        return None
    try:
        manifest = json.loads(_manifest().read_text(encoding="utf-8"))
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
    if not sharded():
        return False
    ledger = load_ledger()
    blob = _dump(ledger)
    if _cache().exists():
        current = _cache().read_text(encoding="utf-8")
        if current == blob:
            if _manifest_sha() != _sha(blob):
                _manifest().write_text(
                    _dump({"schema": MANIFEST_SCHEMA, "cache_sha256": _sha(blob)}),
                    encoding="utf-8",
                )
            return False
        recorded = _manifest_sha()
        if recorded is not None and recorded != _sha(current):
            raise SystemExit(FOREIGN_WRITE_ERROR)
        # Cache is ours (or manifest missing on a fresh checkout) but shards
        # moved (git pull, direct shard edit): refresh.
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
    current = _cache().read_text(encoding="utf-8")
    if current == blob:
        return None
    recorded = _manifest_sha()
    if recorded is not None and recorded != _sha(current):
        return FOREIGN_WRITE_ERROR
    return "cache is stale relative to shards; run ledger_io.py --materialize"


def migrate() -> dict:
    """One-shot: split the tracked monolith into shards + meta + cache."""
    if sharded() and any(_shards().glob("*/*.json")):
        raise SystemExit("ledger/ already contains shards; refusing to re-migrate")
    ledger = json.loads(_cache().read_text(encoding="utf-8"))
    summary = save_ledger(ledger)
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
