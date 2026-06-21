# Goal

Unblock safe runner-cache cleanup by preserving cache files that are still
referenced elsewhere in the repository.

Block130 made cleanup header-aware for nested runner paths. Block131 handles
the next safety boundary: a cache can be runner-orphaned but still be cited by
a live note as frozen evidence. Deleting it would create a broken link.

The observed live example is:

- `docs/CHSH_STRUCTURAL_BOUND_NARROW_THEOREM_NOTE_2026-05-17.md`
- `logs/runner-cache/chsh_structural_bound_narrow_2026_05_17.txt`
