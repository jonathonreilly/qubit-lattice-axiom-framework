---
claim_id: koide_anticommuting_eigenvector_vs_eigenvalue_readout_reconciliation_note_2026-06-01
claim_type_author_hint: positive_theorem
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# The anticommuting (eigenvector) and circulant (eigenvalue) routes to Koide Q=2/3 are consistent — a readout-class reconciliation

**Date:** 2026-06-01
**Claim type:** reconciliation + positive spectral theorem. Adds no axiom and no
import; changes no other note's status or claim.
**Status authority:** independent audit lane only.
**Primary runner:**
`scripts/frontier_koide_anticommuting_eigenvector_vs_eigenvalue_readout_reconciliation.py`
with cache
`logs/runner-cache/frontier_koide_anticommuting_eigenvector_vs_eigenvalue_readout_reconciliation.txt`
(14/14 checks).

## The apparent conflict

Two retained theorems reach Koide `Q = 2/3` on the `C_3` generation space:

- **(chiral / eigenvector)**
  [`KOIDE_ANTICOMMUTING_OPERATOR_DERIVATION_THEOREM_NOTE_2026-05-10.md`](KOIDE_ANTICOMMUTING_OPERATOR_DERIVATION_THEOREM_NOTE_2026-05-10.md)
  (retained): for any 3-dim Hermitian `H` with `{H, Γ_χ} = 0`
  (`Γ_χ = (2/3)J − I`), every **eigenvector** `v` with eigenvalue `≠ 0` satisfies
  the lightcone condition `⟨v|Γ_χ|v⟩ = 0`, i.e.
  `Q(v) = (Σ_g v_g²)/(Σ_g v_g)² = 2/3`. Here `√m_g = v_g` (the eigenvector
  **components**).
- **(non-chiral / eigenvalue)**
  [`KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md`](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md)
  (retained): the circulant `H = aI + bC + b̄C²` (which **commutes** with `Γ_χ`)
  has **eigenvalues** `λ_k`; the signed eigenvalue readout `√m_k = λ_k` gives
  `Q = (Σ λ_k²)/(Σ λ_k)² = 2/3` at `r = |b|²/a² = 1/2`.

A chirality fan-out flagged a **tension**: applying the eigenvalue readout to the
*anticommuting* `H` gives `Q = ∞`, seemingly contradicting the chiral theorem's
`Q = 2/3`.

## The resolution: different √m readouts of the same operator

There is **no contradiction**. The `∞` and the `2/3` are the Koide ratio of two
**different objects** of the same anticommuting `H` — its *spectrum* versus its
*eigenvector* — and the chiral theorem uses the eigenvector, never the spectrum.

### Why the anticommuting spectrum forces Q_eigenvalue = ∞ (a positive fact)

`Γ_χ² = I` and `{H, Γ_χ} = 0` give `Γ_χ H Γ_χ = −H`, so `H` is conjugate to `−H`
and its spectrum is symmetric under `λ → −λ`. On the **odd** 3-dim space one
eigenvalue is its own negative, hence `0`, so the spectrum is `{−λ, 0, +λ}` and
`Σ_k λ_k = 0` (runner §B). Therefore the **eigenvalue** readout
`(Σ λ_k²)/(Σ λ_k)² = ∞` for **any** anticommuting `H` — this is a forced spectral
fact, not a defect (runner §D).

### What the chiral theorem actually computes

The anticommuting theorem reads `√m` off the **eigenvector** `v` (its components),
not the spectrum: `Q(v) = 2/3` via `⟨v|Γ_χ|v⟩ = 0` (runner §C, reproduced for both
nonzero-eigenvalue eigenvectors). The circulant theorem reads `√m` off the
**eigenvalues**: `Q = 2/3` at `r = 1/2` while `[H, Γ_χ] = 0` (runner §E). Both are
correct; they identify `√m` with different objects.

## What this means

- The fan-out's `Q = ∞` was a **readout category error** — the eigenvalue readout
  of an eigenvector-readout theorem. The earlier "the anticommuting operator is
  unphysical / Q = ∞" framing is **withdrawn**: the chiral route gives `Q = 2/3`
  under its own (eigenvector) readout.
- The surviving, correct part of that analysis is **non-necessity**: a *non-chiral*
  operator (the circulant, `[H, Γ_χ] = 0`) also reaches `Q = 2/3` (eigenvalue
  readout at `r = 1/2`). So `Γ_χ`-anticommutation is **sufficient (eigenvector
  route), not necessary** for `Q = 2/3` — not "unphysical."
- The genuine fork is therefore the **√m readout class**: eigenvector components
  (chiral / anticommuting route) versus eigenvalues (non-chiral / circulant
  route). Both give `2/3`; *which identification of `√m` is physical* is the open
  readout-class question (the native operator is the real anti-Hermitian
  [`CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md`](CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md),
  retained_bounded; its Hermitian lift `H = iD` is the circulant, whose
  eigenvalue readout is the comparator-compatible one). This note locates the
  fork; it does not select a readout.

## Non-circularity and scope

`Q = 2/3` is the **output** of both routes (the chiral eigenvector LCC and the
circulant eigenvalue readout); neither the chirality nor `r = 1/2` is assumed
(runner §F). This note **reconciles** two retained theorems and corrects the
category error; it does **not** change either note's status, does not assert a new
`Q`-value mechanism, and does not select the physical readout class.

## Cited dependencies

`koide_anticommuting_operator_derivation` (retained, the eigenvector route),
`koide_circulant_q_two_thirds_algebraic` (retained, the eigenvalue route),
`cpt_exact_real_anti_hermitian_d` (retained_bounded, the native real operator).
No PDG value, no fitted selector, no convention is load-bearing.
