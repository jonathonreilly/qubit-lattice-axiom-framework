# Assumptions And Imports

## Premise Set

- The audit packet builder consumes `helper_runner_paths` from
  `docs/audit/data/citation_graph.json`.
- `_frontier_loader.load_frontier(module_name, filename)` is the repo-local
  dynamic helper loader for many frontier runners.
- Dynamic helper files named by string literal filenames are source files that
  should travel with restricted audit packets when they exist under `scripts/`.

## Forbidden Imports

- No audit verdicts are imported or authored.
- No retained-grade status is inferred from this tooling repair.
- No source claim is treated as cleaner because helper paths are now visible.

## Remaining Risk

The parser intentionally handles literal filenames only. Non-literal dynamic
loads remain outside this block's scope and should be surfaced by the packet
diagnostic if they become queue blockers.
