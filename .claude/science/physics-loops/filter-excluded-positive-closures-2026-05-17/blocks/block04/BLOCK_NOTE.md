# Block 04 Note — L3b Overall Scalar Invariance

**Date:** 2026-05-17
**Branch:** `physics-loop/g-bare-l3b-overall-scalar-block04-2026-05-17`
**Lane:** g_bare (continuation of block 03)
**Status:** positive closure — L3b orbit shown inert for g_bare

## Summary

The L3b continuous overall-scalar admission `N_F ∈ R_{>0}` in
`Tr_{V_3}(T_a T_b) = N_F · δ_{ab}` is physically inert for the bare
gauge coupling `g_bare`. Every positive-real choice of N_F yields the
same g_bare = 1 at the canonical-matching Wilson coefficient
`β_canonical(N_F) = N_c / N_F`.

This is the continuous-orbit generalization of:
- Block 03 (L3a binary V_3 vs V; 2-point discrete subset)
- 2026-05-03 rescaling-freedom-removal theorem (discrete T_a → c T_a
  on canonical N_F = 1/2)

The novel content: explicit packaging of L3b as a 1-parameter
continuous convention orbit with g_bare as an orbit invariant. The
orbit identity is `β · N_F · g_bare² = N_c` (standard convention).

## Deliverables

1. **Source theorem:**
   `docs/G_BARE_L3B_OVERALL_SCALAR_INVARIANCE_NARROW_THEOREM_NOTE_2026-05-17.md`
2. **Runner:**
   `scripts/audit_companion_g_bare_l3b_overall_scalar_invariance_2026_05_17.py`
3. **Cache:**
   `logs/runner-cache/audit_companion_g_bare_l3b_overall_scalar_invariance_2026_05_17.cache.txt`
4. **Scorecard:** PASS = 65, FAIL = 0, TOTAL = 65
5. **Block artifacts:** this note + VALUE_GATE.md

## V1-V5 Disposition

All five value-gate criteria passed (see VALUE_GATE.md).

V5 in particular: this is NOT a one-step variant of block 03. The
block 03 identity is a 2-point structural specialization of the L3b
orbit (with the inflation factor 2 = dim(V_fiber) forced by Cl(3) +
Z^3); block 04 covers the full continuous 1-parameter orbit on the
fixed V_3 trace surface.

## Status (honest)

The L3b admission remains an admitted convention. The note proves
g_bare is invariant along the L3b orbit, NOT that the canonical
N_F = 1/2 is structurally selected. The framework's L4 g_bare = 1
conclusion is robust against the entire L3b 1-parameter residual.

The deeper open question — whether the canonical Gell-Mann
normalization is uniquely forced by Cl(3) algebraic structure alone —
remains open and is the single remaining convention layer in the
g_bare chain per the 2026-05-07 four-layer stratification.

## Next-block recommendation

The three named admissions (L3a, L3b, C-iso `a_τ = a_s`) and the
W1.exact engineering frontier remain from the bridge-gap fragmentation
memory. Block 03 closed L3a; block 04 closes L3b. The natural next
target is **C-iso `a_τ = a_s`** (the time-vs-space lattice spacing
identification admission), or the **W1.exact engineering frontier**.

The C-iso admission is conceptually parallel to L3b (a continuous-orbit
invariance question — does the choice of `a_τ/a_s` ratio leave physical
observables invariant?). The W1.exact frontier is a different lane
(staggered-Dirac realization gate).

**Recommendation:** block 05 target `C-iso a_τ = a_s` admission with
the same orbit-invariance pattern. Mirror block 03/block 04 structure:
identify the convention orbit, show physical observables are invariant
along it, or no-go if not.
