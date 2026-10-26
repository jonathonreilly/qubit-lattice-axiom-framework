# Adjacency Rank Is Bounded By The Qubit's Anticommuting Capacity: The Two Threes Share A Structure

**Date:** 2026-06-10
**Claim type:** bounded_theorem (exact algebra: the Dirac-square carrier bound
`d <= 3` within a supplied Hermitian central-difference carrier on M_2(C);
physical carrier realization and saturation remain open)
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set, predict, promote, or demote any audit outcome.
**Primary runner:**
[`scripts/adjacency_rank_qubit_clifford_bound_2026_06_10.py`](../scripts/adjacency_rank_qubit_clifford_bound_2026_06_10.py)
(SCORECARD: PASS=19, FAIL=0; cached:
[`logs/runner-cache/adjacency_rank_qubit_clifford_bound_2026_06_10.txt`](../logs/runner-cache/adjacency_rank_qubit_clifford_bound_2026_06_10.txt))

---

## Current-premise boundary

The algebra below concerns a supplied Hermitian central-difference carrier.
Current Lattice/Qubit premises provide the lattice and one-site algebra;
Admissibility does not select this kinetic operator. The formal model space
is C^2 tensor ell^2(Z^d); the actual Lattice axiom already supplies Z^3, so
no physical dimension is derived here. Physical realization
and saturation remain conditional/open. The June carrier comparisons below
are not upgraded to current physical derivations by this correction.

## The coincidence this addresses

The axiom set states the number 3 twice:

- the **Lattice** axiom posits `Z^3`;
- the **Qubit** axiom's one-site algebra carries `M_2(C) ~= Cl(3,0)`,
  whose maximal mutually anticommuting self-adjoint-unitary family has
  exactly three members (the Pauli frame).

[`AXIOM_REDUCTION_NOTE.md`](AXIOM_REDUCTION_NOTE.md) lists `d = 3` as the one
unforced discrete choice (C1), and the qubit/dimension link has so far been
recorded only as matched-pair consistency. Under the no-coincidence
discipline, the same number in two independent premises is structure to be
exhibited. This note exhibits half of it, exactly: **the qubit bounds the
Dirac-square adjacency rank at 3, and `Z^3` is the saturating case.** The
other half — why the realized lattice *saturates* the bound — is a named
residual, stated below, not claimed.

## The theorem (exact)

**(T1) Maximality.** In `M_2(C)`, any family of mutually anticommuting
self-adjoint unitaries has at most 3 members. Anticommutation with an
invertible partner forces tracelessness; traceless self-adjoint unitaries are
unit Bloch vectors `n.sigma`; pairwise anticommutation is pairwise
orthogonality of the `n` in `R^3` (`{n.sigma, m.sigma} = 2(n.m) I`); and the
extension system `{X, sigma_a} = 0, a = 1,2,3` has nullspace exactly zero —
there is no 4th anticommuting element of `M_2(C)`, even non-unitary
(runner Parts A, B, D).

**(T2) Cross-term forcing within the supplied Hermitian class.** Let
`nabla_mu=(S_mu-S_mu^-1)/2` be the central differences on the infinite
lattice `Z^d`, and let each constant `gamma_mu` be Hermitian. For
`D = sum_mu gamma_mu (x) nabla_mu`, define `Laplacian=sum_mu nabla_mu^2`
(the central-difference square, not the one-step graph Laplacian). Then D
satisfies the Dirac-square condition

```text
    D^2 = I (x) Laplacian        (no spin-lattice cross terms)
```

iff the supplied Hermitian coefficients square to identity and pairwise
anticommute. Independence of the Fourier monomials `sin(p_mu)^2` and
`sin(p_mu)sin(p_nu)` gives these coefficient equations. Hermiticity is a
hypothesis, not a consequence of D squared: simultaneous similarity by
`diag(2,1)` preserves Pauli squares and anticommutators but produces
non-Hermitian coefficients. The hostile witness `gamma_2' = (sigma_1 +
sigma_2)/sqrt(2)` — itself a self-adjoint unitary — grows cross terms
(runner Part C).

**(T3) The bound.** Within the supplied Hermitian central-difference model,
a Dirac-square carrier exists iff `d <= 3`. `Z^3` is the **saturating** case, and the
saturating family is the Pauli frame up to the fixed-sign uniqueness
([`CL3_PAULI_IRREP_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md`](CL3_PAULI_IRREP_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md)).

**(T4) Realization tie.** The `d = 3` matrix carrier is unitarily equivalent,
by the Kawamoto-Smit site-dependent frame `T(x) = sigma_1^{x1} sigma_2^{x2}
sigma_3^{x3}`, to **two identical copies of the framework's eta-phase
staggered operator**:

```text
    W^dag D W = I_2 (x) D_staggered(eta),
    eta_1 = 1,  eta_2 = (-1)^{x1},  eta_3 = (-1)^{x1+x2},   EXACTLY
```

(runner Part E, `Z_4^3`, every site and direction). This is an identity between supplied operators. Their identification
with a physically realized kinetic carrier remains an additional bridge;
the current axioms do not supply it.

**(T5) Chirality coherence.** The on-site extension to a 4th anticommuting
element is exactly zero (T1), while on a doubled space `C^2 (x) C^2` the
4-family `Gamma_mu = sigma_mu (x) tau_1, Gamma_4 = I (x) tau_2` exists with
grading `gamma_5 = I (x) tau_3` (up to phase) anticommuting with all four
(runner Part G). Saturation alone therefore reproduces the retained
separate-factor chirality boundary: chirality **cannot** live inside the
per-site qubit and **can** live on a separate factor — the same structure the
chirality program reached independently
([`CHIRALITY_SEPARATE_FACTOR_DIRAC_MASS_ALGEBRA_SUPPORT_BOUNDED_NOTE_2026-06-08.md`](CHIRALITY_SEPARATE_FACTOR_DIRAC_MASS_ALGEBRA_SUPPORT_BOUNDED_NOTE_2026-06-08.md)).
Two independent routes agreeing on one structure is the no-coincidence
discipline's positive case.

## What the consolidation does to C1

[`AXIOM_REDUCTION_NOTE.md`](AXIOM_REDUCTION_NOTE.md)'s C1 records `d = 3` as
a bare choice. After this note the status of the dimension statement is
sharper:

```text
  before:  d = 3            (choice; qubit link = matched-pair consistency)
  after:   d <= 3          (conditional on the M_2(C) Hermitian Dirac-square
                             carrier class: T1 + T2)
           d  = 3 = saturation of the qubit's anticommuting capacity (T3),
                    equivalent to two supplied staggered copies (T4)
  residual: the SATURATION READING -- why the realized lattice uses the full
            capacity -- and the carrier-class reading (below).
```

The model exhibits algebraic compatibility between the supplied one-site
algebra and the separately supplied cubic lattice. It neither removes a
primitive nor derives physical saturation or a kinetic branch.

## Named residuals (each graded honestly)

- **Saturation reading** — sub-saturating dimensions exist: the `d = 1, 2`
  Dirac-square carriers are exhibited by the runner (Part F). Nothing here
  selects `d = 3` over `d < 3` in that model. The physical lattice axiom
  already supplies Z^3; the calculation does not derive that choice.
- **Carrier-class reading** — the bound binds the Dirac-square NN carrier
  class. Physical identification with a realized kinetic carrier remains
  open; the older realization proposals are separate conditional context
  ([`STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md`](STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md),
  [`STAGGERED_SCHEME_FORCED_BY_ONE_QUBIT_PER_SITE_LOCALITY_NARROW_THEOREM_NOTE_2026-06-06.md`](STAGGERED_SCHEME_FORCED_BY_ONE_QUBIT_PER_SITE_LOCALITY_NARROW_THEOREM_NOTE_2026-06-06.md));
  T4 supplies only operator equivalence and does not discharge the
  physical identification obligations of these proposals.
- **No axiom change** — this note changes no axiom memo. If the owner later
  chooses to cite this theorem in a consolidation rewording of the Lattice
  axiom, that is a separate owner-approved, audit-decided step (the
  minimality policy's path), explicitly not taken here.

## Relation to adjacent landed results

- [`AXIOM_STACK_MINIMALITY_CL4C_NO_GO_THEOREM_NOTE_2026-04-29.md`](AXIOM_STACK_MINIMALITY_CL4C_NO_GO_THEOREM_NOTE_2026-04-29.md)
  withdraws its broad cell-space impossibility claim: supplied bilinears
  can generate `M_4(C)` on `P_A H_cell`. T1 concerns the different, smaller
  per-site algebra `M_2(C)` and does not use that withdrawn claim.
- [`CL3_FRAME_FREE_AMBIENT_CHIRAL_GRADING_NO_GO_NOTE_2026-06-02.md`](CL3_FRAME_FREE_AMBIENT_CHIRAL_GRADING_NO_GO_NOTE_2026-06-02.md)
  concerns the grade-1 generation 3-space; T5 concerns the spinor carrier.
  Distinct surfaces; the separate-factor conclusion is shared.
- [`QUBIT_AXIOM_HARDENING_NOTE_2026-05-20.md`](QUBIT_AXIOM_HARDENING_NOTE_2026-05-20.md)
  certifies the `M_2(C) ~= Cl(3,0)` equivalence this note's T1 lives on.

## Hostile witnesses (wall-independence)

| dropped hypothesis | witness | outcome |
|---|---|---|
| anticommutation | `gamma_2' = (sigma_1+sigma_2)/sqrt(2)` (s.a. unitary) | cross terms appear; Dirac-square fails (C3) |
| the bound's tightness | extension system `{X, sigma_a} = 0` | nullspace exactly 0; no 4th element of any kind (D1, D2) |
| saturation-as-forced | `d = 1, 2` carriers | exist exactly; the bound does not select (F) |
| on-site chirality | doubled-space 4-family | exists on the separate factor only (G) |

## Falsifiers

- A 4th element of `M_2(C)` anticommuting with the Pauli frame (would refute
  T1; the runner's 12-by-4 complex constraint matrix would have rank < 4).
- A non-anticommuting constant Hermitian coefficient family satisfying the specified Dirac-square
  condition (would refute T2).
- A failure of the Kawamoto-Smit conjugation identity at any site/direction
  (would refute T4 and cut the realization tie).
- A retained derivation that the realized kinetic carrier is outside the
  Dirac-square class (would empty the carrier-class reading and limit the
  bound's reach).

## Dependencies

- [MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md) — current
  Lattice and Qubit premises supply Z^3 and M_2(C), respectively. They do
  not supply the Hermitian Dirac-square kinetic ansatz or a realized
  staggered dynamics. `docs/MINIMAL_AXIOMS_2026-06-05.md` is historical
  provenance for this note's original Lattice/Quantum terminology only.
- [AXIOM_REDUCTION_NOTE.md](AXIOM_REDUCTION_NOTE.md) — the C1 status this
  note sharpens; meta surface, cited for the C1 record only.
- [CL3_PAULI_IRREP_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md](CL3_PAULI_IRREP_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md)
  — uniqueness of the saturating frame.
- [QUBIT_AXIOM_HARDENING_NOTE_2026-05-20.md](QUBIT_AXIOM_HARDENING_NOTE_2026-05-20.md)
  — the recorded `M_2(C) ~= Cl(3,0)` reading.
- [STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md](STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md)
  — the KS surface T4 realizes; landed but unaudited, so conditionality is
  inherited for the realization tie.
- [STAGGERED_SCHEME_FORCED_BY_ONE_QUBIT_PER_SITE_LOCALITY_NARROW_THEOREM_NOTE_2026-06-06.md](STAGGERED_SCHEME_FORCED_BY_ONE_QUBIT_PER_SITE_LOCALITY_NARROW_THEOREM_NOTE_2026-06-06.md)
  — the one-component-per-site carrier density; landed but unaudited, so
  conditionality is inherited.
- [CHIRALITY_SEPARATE_FACTOR_DIRAC_MASS_ALGEBRA_SUPPORT_BOUNDED_NOTE_2026-06-08.md](CHIRALITY_SEPARATE_FACTOR_DIRAC_MASS_ALGEBRA_SUPPORT_BOUNDED_NOTE_2026-06-08.md)
  — the independently-reached separate-factor chirality structure T5
  reproduces.
- [AXIOM_STACK_MINIMALITY_CL4C_NO_GO_THEOREM_NOTE_2026-04-29.md](AXIOM_STACK_MINIMALITY_CL4C_NO_GO_THEOREM_NOTE_2026-04-29.md)
  — historical cell-space claim, now corrected; not a premise of T1.

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency. It changes no axiom memo and registers no
primitive. The independent audit lane is the only status authority.

## Audit metadata

```yaml
claim_type_author_hint: bounded_theorem
claim_scope: "Within the supplied translation-covariant Hermitian central-difference Dirac-square carrier class on C^2 tensor ell^2(Z^d), M_2(C)'s anticommuting self-adjoint-unitary capacity forces d <= 3; Z^3 is the saturating case, and the saturating matrix carrier is Kawamoto-Smit conjugate to the eta-phase staggered carrier. The saturation reading and carrier-class reading remain named residuals; no axiom, primitive, or audit status is changed."
upstream_dependencies:
  - minimal_axioms
  - axiom_reduction_note
  - cl3_pauli_irrep_uniqueness_narrow_theorem_note_2026-05-10
  - qubit_axiom_hardening_note_2026-05-20
  - staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07
  - staggered_scheme_forced_by_one_qubit_per_site_locality_narrow_theorem_note_2026-06-06
  - chirality_separate_factor_dirac_mass_algebra_support_bounded_note_2026-06-08
admitted_context_inputs: []
source_sets_audit_outcome: false
```
