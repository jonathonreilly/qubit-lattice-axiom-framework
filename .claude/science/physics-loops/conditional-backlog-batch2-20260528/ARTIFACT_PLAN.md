# Artifact Plan

## Source Notes

Patch the six target source notes with a `2026-05-28 Science-Fix Re-Audit
Scope` section that states the narrow live claim and the unresolved bridge.

## Runner Support

Update `scripts/frontier_audit_backlog_campaign_synthesis.py` so its assertions
match the narrowed campaign-index title and require the re-audit scope marker.
Refresh the SHA-pinned runner cache.

## Generated Audit Data

Run `bash docs/audit/scripts/run_pipeline.sh` after source edits. The expected
artifact is a generated reset of the six changed rows to `unaudited`, with no
manual verdict edits.

## Review Package

Commit the notes, runner/cache update, generated audit projection, and this
loop pack. Open a draft `[physics-loop]` PR for reviewer extraction.
