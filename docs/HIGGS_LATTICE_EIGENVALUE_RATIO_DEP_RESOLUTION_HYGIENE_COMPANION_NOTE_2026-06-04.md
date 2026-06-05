---
claim_id: higgs_lattice_eigenvalue_ratio_dep_resolution_hygiene_companion_note_2026-06-04
claim_type_author_hint: meta
---

# Higgs Lattice Eigenvalue Ratio Dep-Resolution Hygiene Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / dependency-surface hygiene evidence)
**Status:** companion-only. This records two review-compatible facts about the
parent
[`HIGGS_LATTICE_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02.md`](HIGGS_LATTICE_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02.md):
the historical deprecated `g_bare` dependency is absent from the current
parent dependency set, and the parent's runner rechecks the lattice-side
ratio algebra without using dependency-grade fields in its algebraic blocks.
It is not a theorem claim, not a direct status change, and not independent
audit work.
**Companion target:** `higgs_lattice_eigenvalue_ratio_narrow_theorem_note_2026-05-02`
**Primary runner:**
[`scripts/audit_companion_higgs_lattice_eigenvalue_ratio_dep_resolution_2026_06_04.py`](../scripts/audit_companion_higgs_lattice_eigenvalue_ratio_dep_resolution_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_higgs_lattice_eigenvalue_ratio_dep_resolution_2026_06_04.txt`](../logs/runner-cache/audit_companion_higgs_lattice_eigenvalue_ratio_dep_resolution_2026_06_04.txt)

## Claim Boundary

The parent is a bounded lattice-side algebra statement:

```text
R_lattice = 4 / (u_0^2 N_taste) = 1 / (4 u_0^2)
```

at `N_taste = 16`, with the Clifford taste identity checked by explicit
finite matrix algebra. This companion does not decide the parent's final
audit disposition. It only records that:

1. the deprecated 2026-05-02 `g_bare` convention parent named in older
   dependency-weakening history is not in the current parent dependency set;
2. the current parent runner's algebraic blocks derive the `D_taste^2 = d I`
   identity, structural counts, and `R_lattice` formula directly;
3. the current parent runner's dependency-ledger block is graph-visibility
   bookkeeping and is not used to compute the lattice-side ratio;
4. one current dependency remains pending-chain in the ledger, so this
   companion does not claim dependency closure or parent promotion.

## Evidence

The companion runner checks:

- the parent runner exits with `PASS=40 FAIL=0`;
- the parent runner transcript contains the Clifford identity, structural
  count, and `R_lattice` checks;
- the parent runner source keeps dependency-grade field reads out of its
  algebraic blocks before the final graph-visibility section;
- the current ledger dependency set has the deprecated dependency absent and
  the five repaired dependencies present;
- exactly one current dependency is pending-chain, and that status is treated
  as a blocker for dependency closure rather than as closed support;
- direct symbolic arithmetic reproduces `4 / (u_0^2 * 16) = 1 / (4 u_0^2)`.

## What This Does Not Claim

- It does not claim a new theorem.
- It does not promote the parent or this companion.
- It does not edit the parent or any dependency note.
- It does not classify pending-chain dependencies as closed support.
- It does not claim a physical Higgs-mass prediction, Standard Model matching,
  or an `m_H / v` identification.
- It does not close the parent's dependency chain; independent audit handling
  remains required.

The safe downstream use is only this meta evidence: the deprecated dep is no
longer declared, and the parent runner's lattice-side algebra is substance
checked independently of dependency-grade fields.
