# Block 03 Claim Status Certificate

**Date:** 2026-05-17
**Target:** `g_bare_derivation_note` (audited_conditional, parent open_gate)
**Block class:** Deep (~90 min)
**Branch:** `physics-loop/g-bare-derivation-block03-2026-05-17`

## Outcome

**POSITIVE CLOSURE on the L3a residual's `g_bare`-physical-inertia question.**

The L3a binary admission `N_F ∈ {1/2, 1}` (between V_3 trace and V trace, the
single residual after the 2026-05-07 W2 trilogy) is **NOT** structurally
closed by this block — that remains the staggered-Dirac realization gate's
matter-rep route per the 2026-05-07 10-vector consolidation. However, this
block establishes a strictly NEW positive identity: **the residual binary
admission is physically inert for `g_bare`**. Both trace surfaces yield
`g_bare = 1` at the Wilson canonical matching surface, with only the
conventional `β` value differing (`β = 6` for V_3, `β = 8` for V).

## Source theorem note

`docs/G_BARE_L3A_TRACE_SURFACE_INVARIANCE_NARROW_THEOREM_NOTE_2026-05-17.md`

**Type:** positive_theorem (proposed; audit-lane to ratify)
**Load-bearing step class:** A (algebraic substitution into three cited
identities: N_F binary reduction Z2, L3a S1 uniform inflation sharpening,
CL3 color automorphism V-embedding).

## Theorem statement (T1-T5 summary)

Under the symmetric Wilson lattice action `S_W^{(W)} = β^{(W)} · Σ_p F^{(W)}(U_p^{(W)})`
with `F^{(W)}(U) := (dim(W) - Re Tr_W(U))/dim(W)`, and the convention-independent
continuum kinetic `(1/(4 g²)) Σ_a F^a_μν F^{a μν}`:

- **(T1)** `Tr_V(F²) = 2 · Tr_{V_3}(F²)` (trace inflation by `dim(V_fiber) = 2`).
- **(T2)** Lattice-side `a^4` ratio `F^{(V)} / F^{(V_3)} = 3/4` (structural).
- **(T3)** Continuum-side `(1/(2g²)) (1/N_F^{(W)}) Tr_W(F²)` reduces to
  convention-independent `(1/(4g²)) Σ_a F^a_μν F^{a μν}` for both `W`.
- **(T4)** Wilson matching: `β^{(W)} = dim(W) / (N_F^{(W)} · g_bare²)`.
  At `g_bare = 1`: `β^{(V_3)} = 6 = 2 N_c`; `β^{(V)} = 8 = dim(V)`.
- **(T5)** L3a binary swap routes entirely into `β`, leaving `g_bare`
  invariant. Both `(V_3, β=6)` and `(V, β=8)` recover `g_bare = 1`.

## Runner

`scripts/audit_companion_g_bare_l3a_trace_surface_invariance_2026_05_17.py`
**Result:** PASS = 33, FAIL = 0
**Cache:** `logs/runner-cache/audit_companion_g_bare_l3a_trace_surface_invariance_2026_05_17.txt`

## Class-A breakdown (load-bearing only)

| Section | Identity verified | Method | PASS count |
|---------|------------------|--------|------------|
| A | (T1) trace inflation | numpy on random F + sympy on Gell-Mann basis | 8 |
| B | (T2) lattice a^4 ratio 3/4 | numpy least-squares fit + sympy ratio | 4 |
| C | (T3) continuum invariance | sympy symbolic simplify | 4 |
| D | (T4) Wilson matching identity | sympy exact rational | 6 |
| E | (T5) g_bare invariance | sympy with multiple counterfactuals | 9 |
| F | Parent-row consistency | sympy alignment with frontier_g_bare_derivation.py | 2 |

## Honest scope

This theorem **does not** close the L3a admission (i.e., does not derive
`N_F = 1/2` from A1+A2 alone). It establishes the **strictly weaker
positive identity** that the L3a residual is `g_bare`-inert: regardless
of which side of the binary admission the audit lane retains, the parent
`g_bare_derivation_note`'s L4 conclusion `g_bare = 1` is unchanged.

The trace-surface routing is algebraically parallel to the 2026-05-03
generator-rescaling routing (`T_a → c T_a` routes `β → c² β` with
`g_bare` unchanged). The present theorem is the corresponding routing
identity for the trace-surface degree of freedom rather than the
generator-rescaling degree of freedom.

## Dep chain (one hop)

- `n_f_bounded_z2_reduction_theorem_note_2026-05-07_w2` (unaudited;
  carries the binary admission and uniform inflation ratio).
- `l3a_v3_trace_surface_bounded_obstruction_note_2026-05-07_l3a` (unaudited;
  carries the S1 uniform inflation sharpening).
- `cl3_color_automorphism_theorem` (`retained_bounded`; carries the
  canonical V_3 ⊂ V embedding).

## Impact on parent g_bare_derivation_note

The parent's L4 conclusion `g_bare = 1` is now **demonstrably L3a-binary-
inert**. The parent re-audit, if it occurs, can cite this candidate as
supporting evidence that the L4 `g_bare = 1` value does not depend on
which side of the binary L3a admission is retained. The four-layer
stratification's L3 → L4 inference is sharpened to "L4 g_bare = 1
invariant under L3a binary swap".

This does NOT lift the parent's `audited_conditional` status (which
requires retained-grade closure of the rescaling-removal and constraint-
vs-convention deps); but it adds an independent positive arrow making
the L4 conclusion structurally more robust.

## V1-V5 outcome

PASS. See `VALUE_GATE.md` for the gate's full text. The block's
non-trivial marginal content is the explicit invariance arrow from L3a
binary admission to Wilson-extracted `g_bare`, not present in any prior
note in the cluster. The arrow is algebraically parallel to (but
structurally distinct from) the 2026-05-03 generator-rescaling routing
theorem.

## Block status

**COMPLETE.** Source note + runner + cache landed. Block artifacts
populated. PR opened.

The L3a residual remains 1 (no admission count reduction); but the
parent g_bare_derivation_note has a new independent positive arrow
demonstrating L3a-binary-inertness of the L4 conclusion.
