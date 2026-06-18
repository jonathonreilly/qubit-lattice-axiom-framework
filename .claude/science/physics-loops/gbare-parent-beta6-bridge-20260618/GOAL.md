# Goal

Repair the new critical conditional on `g_bare_derivation_note` without
editing audit-owned files or refreshing existing PRs.

The target blocker is the parent proof's implicit `beta = 6` surface. The
science goal is to make the parent source cite and verify a non-circular
composition:

```text
finite-link canonical scalar slot g_bare^2 = 1
Wilson coefficient identity beta g_bare^2 = 2 N_c
N_c = 3
=> beta = 6
```
