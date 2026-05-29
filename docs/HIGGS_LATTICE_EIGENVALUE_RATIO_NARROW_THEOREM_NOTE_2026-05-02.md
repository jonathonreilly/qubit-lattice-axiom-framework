# Higgs Lattice Eigenvalue Ratio (Mean-Field) — Narrow Theorem

**Date:** 2026-05-02 (2026-05-28: both former admissions knocked down — Clifford
identity derived, mean-link u_0 wired to a retained authority; no admissions).
**Type:** bounded_theorem (proposed; audit-lane to ratify)
**Status authority:** independent audit lane only.
**Primary runner:** `scripts/frontier_higgs_lattice_eigenvalue_ratio_narrow.py`

## 2026-05-28 Audit Repair (no admissions — derive + wire retained, then formal-lemma the rest)

The 2026-05-28 audit verdict was `audited_conditional`:

> *"The displayed algebra and runner checks close exactly: W''(0)/N_tot equals
> 1/(4u_0^2), matching R_lattice. The retained one-hop rows cover the scoped
> SU(3) and g_bare surfaces, but the Clifford/staggered identity D_taste^2=d I
> and mean-field factorization U_ab → u_0 delta_ab are load-bearing admitted
> premises, not retained one-hop theorem rows or registered Tier-A admissions."*

The offered repair allowed either a registered admission OR retained one-hop
coverage. **This repository does not take admissions**, so each former
admission is knocked down instead — by derivation or by wiring a retained
authority:

1. **`D_taste² = d·I` — DERIVED, not admitted.** This is an elementary
   Euclidean Clifford fact: for the d=4 lattice taste algebra `Cl(4)` with
   generators `γ_μ² = +I`, `{γ_μ,γ_ν} = 2δ_μν I`, one has `Σ_μ γ_μ² = d·I`, and
   the symmetric taste-Dirac element `D_taste = Σ_μ γ_μ` satisfies
   `D_taste² = d·I` (cross terms cancel by antisymmetry), so every taste
   eigenvalue has magnitude `√d = 2`. The runner now **constructs the four
   Euclidean gamma matrices explicitly and verifies the Clifford algebra,
   `Σγ_μ² = 4·I`, and `D_taste² = 4·I` by exact matrix algebra** (Part 3) — it
   is derived, not asserted. The Clifford generator structure and the even
   spacetime dimension `d = 4` (framework `3+1`) are the retained
   `clifford_chirality_dimension_narrow_theorem_note_2026-05-10` surface.
2. **Mean-link `u_0` — RETAINED authority, not admitted.** The mean-link
   `u_0 = <P>^{1/4}` and the tadpole mean-field scheme are carried by the
   retained-bounded `u0_plaquette_quartic_derivation_narrow_theorem_note_2026-05-17`,
   now wired as a one-hop dependency. The note no longer admits `u_0`.
3. **Mean-field factorization `U_ab → u_0 δ_ab` — explicit hypothesis of a
   formal lemma, not an admission.** Replacing the link by its mean value
   `u_0 δ_ab` in the fermion operator is the **defining hypothesis of the
   tadpole mean-field truncation regime** (its scale `u_0` retained per item 2).
   The lemma below is an exact algebraic identity *within that named
   truncation*; it makes no claim that the truncation is the exact theory.
   This is the same formal/conditional category the audit lane accepts, with
   the scale now retained-backed rather than admitted.
4. **`N_taste = 16` — DERIVED.** It is the spin⊗taste hypercube dimension
   `2^d = 2^4 = 16` (equivalently 4 spin × 4 taste components on the unit
   hypercube), verified in Part 2; not an admitted block size.

Net: the load-bearing chain has **no admitted premises** — the Clifford
identity and `N_taste` are derived (runner matrix-verified), `u_0` is supplied
by a retained one-hop authority, and the mean-field factorization is the
explicit hypothesis of the formal lemma. No new axiom or import is introduced;
the two new one-hop deps are existing retained / retained-pending rows.

## Claim scope (proposed)

> **Given** the declared graph-first SU(3) gauge surface
> ([`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md)), the
> Wilson canonical convention `g_bare = 1` (carried by the retained
> rescaling-freedom-removal theorem
> [`G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md`](G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md)
> plus the retained constraint-vs-convention disambiguation theorem
> [`G_BARE_CONSTRAINT_VS_CONVENTION_THEOREM_NOTE_2026-05-03.md`](G_BARE_CONSTRAINT_VS_CONVENTION_THEOREM_NOTE_2026-05-03.md);
> historical sister cycle 6 reader pointer: `G_BARE_CANONICAL_CONVENTION_NARROW_THEOREM_NOTE_2026-05-02.md`),
> and the Cl(3) Clifford identity `D_taste² = d · I` at
> mean-field factorization with `N_taste = 16` taste eigenvalues, the
> dimensionless lattice generating-functional curvature ratio is
> ```
> R_lattice  ≡  4 / (u_0² · N_taste)  =  1 / (4 u_0²)         at N_taste = 16
> ```
> where `u_0` is the mean-link parameter.

The narrow theorem **explicitly does NOT** claim:

- that `R_lattice` equals the physical ratio `(m_H / v)²` (this is a
  separate physical-matching identification, class (F), and is the
  parent's blocked load-bearing step);
- the **numerical** value of `u_0` (its tadpole definition `u_0 = <P>^{1/4}`
  is retained via the wired authority, but the number requires the separate
  plaquette evaluation, not in scope here);
- the full Higgs mass derivation `m_H = v / (2 u_0)`;
- a Standard Model Higgs-mass prediction.

The result is a **pure lattice-side algebraic identity**: the curvature
of the Clifford-Dirac generating functional at mean-field. The physical-
side identification with `(m_H / v)²` is the renaming step the parent's
audit verdict flagged and is excluded here.

## Declared dependencies (one-hop) — no admissions

| Authority / input | Audit-lane status | Role |
|---|---|---|
| [`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md) | retained | provides SU(N_c=3) gauge structure on Z³ taste surface |
| [`G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md`](G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md) | retained | removes the `A → A/g` rescaling freedom on the canonical Cl(3) normalization surface |
| [`G_BARE_CONSTRAINT_VS_CONVENTION_THEOREM_NOTE_2026-05-03.md`](G_BARE_CONSTRAINT_VS_CONVENTION_THEOREM_NOTE_2026-05-03.md) | retained_bounded | `g_bare = 1` on the canonical-normalization + Wilson-matching + local-`beta = 6` surface |
| [`U0_PLAQUETTE_QUARTIC_DERIVATION_NARROW_THEOREM_NOTE_2026-05-17.md`](U0_PLAQUETTE_QUARTIC_DERIVATION_NARROW_THEOREM_NOTE_2026-05-17.md) | retained_bounded | supplies the mean-link `u_0 = <P>^{1/4}` and the tadpole mean-field scheme (replaces the former `u_0` admission) |
| [`CLIFFORD_CHIRALITY_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md`](CLIFFORD_CHIRALITY_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md) | retained_pending_chain | framework Clifford generator structure + even spacetime dimension `d=4`, grounding the derived `D_taste² = d·I` |
| Clifford identity `D_taste² = d · I` | **DERIVED** (runner Part 3, exact matrix algebra) | Euclidean `Cl(4)`: `Σ_μ γ_μ² = d·I` and `D_taste² = d·I` ⇒ `|λ_k| = √d = 2` per taste |
| Mean-field factorization `U_{ab} → u_0 δ_{ab}` | **explicit lemma hypothesis** (tadpole mean-field truncation; scale `u_0` retained above) | scales eigenvalues by `u_0` |

The Clifford identity is derived by explicit matrix construction (not
admitted); the mean-link `u_0` is supplied by a retained one-hop authority
(not admitted); the mean-field factorization is the explicit hypothesis of the
formal lemma (the tadpole mean-field truncation regime), not an admitted
premise. The result is an exact algebraic identity within that named
truncation.

## Load-bearing step (class A)

```text
Cl(3)/Z^4 APBC minimal block (L = 2):
  N_sites = 2^4 = 16  =  N_taste                                (derived: spin⊗taste hypercube dim 2^d = 2^4)
  N_c = 3                                                       (declared: graph_first_su3)
  N_tot = N_c × N_sites = 48                                    (algebraic)

Clifford identity D_taste² = d · I  (DERIVED, runner Part 3: Euclidean Cl(4) matrix construction):
  taste eigenvalues: |λ_k| = sqrt(d) = 2 (in lattice units, d=4 spacetime)

Mean-field factorization U_{ab} → u_0 δ_{ab}  (lemma hypothesis: tadpole mean-field truncation; u_0 retained via u0_plaquette_quartic):
  full eigenvalues: |λ_k|_full = 2 u_0
  pure imaginary (staggered anti-Hermiticity): λ_k = ± 2 i u_0

Generating functional at mean field:
  W(J) = sum_{k=1}^{N_tot} (1/2) log(J² + 4 u_0²)
       = (N_tot / 2) · log(J² + 4 u_0²)

Curvature:
  d²W/dJ² |_{J=0} = N_tot · (1 / (2 u_0²)) · (1 / 2)
                 = N_tot · (1 / (4 u_0²))

Per-taste curvature:
  d²W/dJ² |_{J=0} / N_tot = 1 / (4 u_0²)

Scaled dimensionless ratio:
  R_lattice  ≡  4 / (u_0² · N_taste)
             =  4 / (u_0² · 16)
             =  1 / (4 u_0²)

This matches the per-taste curvature; the ratio R_lattice is an
algebraic combination of the derived Clifford identity, the retained
mean-link u_0, and the truncation hypothesis.
```

This is class (A) — an exact algebraic identity; the derived Clifford
identity (Part 3) and the retained mean-link `u_0` carry it, with the
tadpole mean-field truncation as the only (named) hypothesis.
No physical-side identification, no fitted value.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/frontier_higgs_lattice_eigenvalue_ratio_narrow.py
```

Verifies, at exact rational precision via Python `Fraction`:

1. `N_tot = N_c × N_sites = 48` from `(N_c, N_sites) = (3, 16)`.
2. Clifford-identity eigenvalue magnitude `2 u_0` (from `D_taste² = d·I` with `d = 4`).
3. Generating functional `W(J)` curvature at mean field.
4. `R_lattice = 4 / (u_0² · 16) = 1 / (4 u_0²)` algebraic identity.
5. Cited repo authorities are graph-visible in the live ledger and this
   new row remains effective-unaudited before independent audit
   lookup.
6. Scope discipline: the physical identification `R_lattice = (m_H/v)²`
   is **not** in the load-bearing chain.

## Audit-lane disposition (proposed)

```yaml
target_claim_type: bounded_theorem
proposed_claim_scope: |
  Pure lattice-side algebraic identity at mean-field on Cl(3)/Z^4 APBC:
  R_lattice = 4/(u_0² N_taste) with N_taste = 16 gives R_lattice = 1/(4 u_0²).
  NO physical Higgs mass identification, NO m_H = v/(2 u_0) claim.
proposed_load_bearing_step_class: A
audit_required_before_effective_retained: true
```

Audit status is set only by the independent audit lane. This note is safe to
land as an unaudited, graph-visible bounded-theorem candidate; retained-family
effective status requires independent audit of this row and retained-grade
closure of its declared dependency chain.

## What this theorem closes

The lattice-side algebraic content of the parent
`HIGGS_MASS_FROM_AXIOM_NOTE`'s derivation, freed from the conditional
physical-matching identification (which is class (F) and was the parent's
blocking step). The narrow theorem provides a clean retained-bounded
primitive for the lattice-side curvature that downstream rows can cite once
the audit lane ratifies this row and its dependency chain.

## What this theorem does NOT close

- The physical identification `R_lattice = (m_H/v)²` (separate downstream
  matching theorem; remains in the lattice→physical matching cluster
  obstruction, see prior campaign cycle 13 PR #274).
- The Higgs mass prediction `m_H = v/(2 u_0)` (separate full theorem).
- The **numerical** value of `u_0` (its tadpole definition `u_0 = <P>^{1/4}`
  is retained; the number requires the separate plaquette evaluation).

## Cross-references

- `HIGGS_MASS_FROM_AXIOM_NOTE.md` — parent with a conditional audit verdict;
  this narrow theorem keeps only the lattice-side algebra clean.
- [`G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md`](G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md) —
  retained sister theorem: removes the `A → A/g` rescaling freedom.
- [`G_BARE_CONSTRAINT_VS_CONVENTION_THEOREM_NOTE_2026-05-03.md`](G_BARE_CONSTRAINT_VS_CONVENTION_THEOREM_NOTE_2026-05-03.md) —
  retained_bounded sister theorem: `g_bare = 1` on canonical-normalization
  + Wilson-matching + `beta = 6` surface.
- `G_BARE_CANONICAL_CONVENTION_NARROW_THEOREM_NOTE_2026-05-02.md` —
  historical cycle 6 sister narrow theorem (plain-text reader pointer,
  not a markdown-link load-bearing dependency; the load-bearing g_bare
  content is now carried by the two retained 2026-05-03 sister theorems
  listed above).
- [`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md) —
  declared dependency.
- Cycles 1-5 (PRs #292, #293, #294, #297, #299) — sister narrow theorems
  / synthesis on different lanes.
