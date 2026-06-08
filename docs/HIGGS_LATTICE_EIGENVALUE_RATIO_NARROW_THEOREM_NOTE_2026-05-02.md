# Higgs Lattice Eigenvalue Ratio (Mean-Field) — Narrow Theorem

**Date:** 2026-05-02 (2026-05-28: Clifford identity derived and mean-link
`u_0` wired to a retained authority; 2026-06-08: framework-native `d=4/Z^4`
APBC carrier made an explicit unresolved bounded hypothesis).
**Type:** bounded_theorem (proposed; audit-lane to ratify)
**Status authority:** independent audit lane only.
**Primary runner:** `scripts/frontier_higgs_lattice_eigenvalue_ratio_narrow.py`

## 2026-06-08 safe-narrow repair

The current audit blocker asks for a retained one-hop authority deriving
`d_t = 1`, total `d = 4`, and the `Z^4` APBC carrier for this lattice block,
or else a narrow row that makes `d=4/Z^4 APBC` an explicit unresolved bounded
hypothesis.

This source note takes the second route. The exact curvature identity remains
valid inside the supplied `d=4/Z^4` APBC taste-block packet, but this row no
longer claims that the framework-native carrier theorem has been derived.
The open science is the retained derivation of that carrier from the baseline
framework; the algebra below is the bounded packet to be reused once that
carrier is closed.

## 2026-05-28 Audit Repair (derive + wire retained inside the supplied packet, then formal-lemma the rest)

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
   spacetime dimension `d = 4` (framework `3+1`) are grounded in
   `clifford_chirality_dimension_narrow_theorem_note_2026-05-10`, which is
   audited clean but still `retained_pending_chain`; this row therefore remains
   audit-ready rather than self-promoted.
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
4. **`N_taste = 16` — DERIVED inside the supplied APBC packet.** Given the
   `d=4/Z^4` APBC taste-block packet, it is the spin⊗taste hypercube
   dimension `2^d = 2^4 = 16` (equivalently 4 spin × 4 taste components on
   the unit hypercube), verified in Part 2. This row does not derive the
   framework-native `d=4/Z^4` carrier itself.

Net: the packet has no new axiom and no registered admission. The Clifford
identity and `N_taste` are derived after the `d=4/Z^4` APBC carrier is
supplied, `u_0` is supplied by a retained one-hop authority, and the
mean-field factorization is the explicit hypothesis of the formal lemma. The
framework-native carrier remains an unresolved bounded hypothesis for this
row, not a retained conclusion.

## Claim scope (proposed)

> **Given** the declared graph-first SU(3) gauge surface
> ([`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md)), the
> Wilson canonical convention `g_bare = 1` (carried by the retained
> rescaling-freedom-removal theorem
> [`G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md`](G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md)
> plus the retained constraint-vs-convention disambiguation theorem
> [`G_BARE_CONSTRAINT_VS_CONVENTION_THEOREM_NOTE_2026-05-03.md`](G_BARE_CONSTRAINT_VS_CONVENTION_THEOREM_NOTE_2026-05-03.md);
> historical sister cycle 6 reader pointer: `G_BARE_CANONICAL_CONVENTION_NARROW_THEOREM_NOTE_2026-05-02.md`),
> the supplied unresolved `d=4/Z^4` APBC taste-block carrier hypothesis,
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
| supplied `d=4/Z^4` APBC taste-block carrier | unresolved bounded hypothesis | supplies the finite carrier on which `N_taste = 2^4 = 16` is derived; native carrier theorem remains open |
| [`CLIFFORD_CHIRALITY_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md`](CLIFFORD_CHIRALITY_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md) | retained_pending_chain | framework Clifford generator structure used inside the supplied carrier packet |
| Clifford identity `D_taste² = d · I` | **DERIVED** (runner Part 3, exact matrix algebra) | Euclidean `Cl(4)`: `Σ_μ γ_μ² = d·I` and `D_taste² = d·I` ⇒ `|λ_k| = √d = 2` per taste |
| Mean-field factorization `U_{ab} → u_0 δ_{ab}` | **explicit lemma hypothesis** (tadpole mean-field truncation; scale `u_0` retained above) | scales eigenvalues by `u_0` |

The Clifford identity is derived by explicit matrix construction once the
finite carrier packet is supplied; the mean-link `u_0` is supplied by a
retained one-hop authority; the mean-field factorization is the explicit
hypothesis of the formal lemma. The result is an exact algebraic identity
within those named bounded hypotheses.

## 2026-06-06 Bridge Packet Inlining Repair

The 2026-06-05/2026-06-07 audit blocker asks for a retained one-hop bridge
deriving the `d=4/Z^4` taste count `N_taste = 16` and the mean-field
determinant `W(J)` form used in the curvature calculation. The source side now
exposes the bridge packet explicitly and the parent runner checks it inline.

Bridge packet:

- Broad taste-count and `W(J)` bridge note:
  [`docs/HIGGS_LATTICE_TASTE_COUNT_AND_WJ_FORM_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`](HIGGS_LATTICE_TASTE_COUNT_AND_WJ_FORM_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)
- Broad bridge runner:
  [`scripts/audit_companion_higgs_lattice_taste_count_wj_form_2026_06_05.py`](../scripts/audit_companion_higgs_lattice_taste_count_wj_form_2026_06_05.py)
- Broad bridge cache:
  [`logs/runner-cache/audit_companion_higgs_lattice_taste_count_wj_form_2026_06_05.txt`](../logs/runner-cache/audit_companion_higgs_lattice_taste_count_wj_form_2026_06_05.txt)
- Determinant/APBC bridge note:
  [`docs/HIGGS_MEAN_FIELD_DETERMINANT_APBC_TASTE_BRIDGE_NOTE_2026-06-06.md`](HIGGS_MEAN_FIELD_DETERMINANT_APBC_TASTE_BRIDGE_NOTE_2026-06-06.md)
- Determinant/APBC bridge runner:
  [`scripts/audit_companion_higgs_mean_field_determinant_apbc_taste_bridge_2026_06_06.py`](../scripts/audit_companion_higgs_mean_field_determinant_apbc_taste_bridge_2026_06_06.py)
- Determinant/APBC bridge cache:
  [`logs/runner-cache/audit_companion_higgs_mean_field_determinant_apbc_taste_bridge_2026_06_06.txt`](../logs/runner-cache/audit_companion_higgs_mean_field_determinant_apbc_taste_bridge_2026_06_06.txt)

The parent runner now verifies that those paths are linked here, that the
bridge notes/runners contain the load-bearing `N_taste = 16`, `W(J) = log det(D
+ J)`, `D_mf^dag D_mf = 4 u_0^2 I_48`, and `W''(0)/48 = 1/(4 u_0^2)`
statements, and that both bridge caches are SHA-fresh and clean-exit:

```text
TOTAL: 50 PASS / 0 FAIL
TOTAL: 15 PASS / 0 FAIL
```

After the parent algebra checks, the primary runner reports:

```text
TOTAL: PASS=90, FAIL=0
```

This is a bridge-packet repair only. It does not identify `R_lattice` with
`(m_H/v)^2`, does not claim a Higgs mass prediction, does not derive a numerical
`u_0`, and does not set an audit verdict.

## Load-bearing step (class A)

```text
Cl(3)/Z^4 APBC minimal block (L = 2):
  N_sites = 2^4 = 16  =  N_taste                                (derived inside supplied d=4/Z^4 APBC packet)
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
tadpole mean-field truncation and supplied `d=4/Z^4` APBC carrier as the
named bounded hypotheses.
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
  Pure lattice-side algebraic identity at mean-field on supplied Cl(3)/Z^4 APBC:
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
- The framework-native derivation of the `d=4/Z^4` APBC taste-block carrier
  from baseline primitives.

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
