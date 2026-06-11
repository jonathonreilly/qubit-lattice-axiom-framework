# Adjacency Rank Is Bounded By The Qubit's Anticommuting Capacity: The Two Threes Share A Structure

**Date:** 2026-06-10
**Claim type:** bounded_theorem (exact algebra: the Dirac-square carrier bound
`d <= 3` from the Quantum axiom, with `Z^3` the saturating case; the
saturation reading is a named residual)
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set, predict, promote, or demote any audit outcome.
**Primary runner:**
[`scripts/adjacency_rank_qubit_clifford_bound_2026_06_10.py`](../scripts/adjacency_rank_qubit_clifford_bound_2026_06_10.py)
(SCORECARD: PASS=18, FAIL=0; cached:
[`logs/runner-cache/adjacency_rank_qubit_clifford_bound_2026_06_10.txt`](../logs/runner-cache/adjacency_rank_qubit_clifford_bound_2026_06_10.txt))

---

## The coincidence this addresses

The axiom set states the number 3 twice:

- the **Lattice** axiom posits `Z^3`;
- the **Quantum** axiom's one qubit per site carries `M_2(C) ~= Cl(3,0)`,
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

**(T2) Cross-term forcing.** A translation-covariant nearest-neighbor
first-order hopping operator `D = sum_mu gamma_mu (x) nabla_mu` on `Z^d`
satisfies the Dirac-square condition

```text
    D^2 = I (x) Laplacian        (no spin-lattice cross terms)
```

iff the per-site coefficients `gamma_mu` are mutually anticommuting
self-adjoint unitaries. The hostile witness `gamma_2' = (sigma_1 +
sigma_2)/sqrt(2)` — itself a self-adjoint unitary — grows cross terms
(runner Part C).

**(T3) The bound.** Hence on the one-qubit-per-site lattice, a Dirac-square
NN carrier exists iff `d <= 3`. `Z^3` is the **saturating** case, and the
saturating family is the Pauli frame up to the retained uniqueness
([`CL3_PAULI_IRREP_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md`](CL3_PAULI_IRREP_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md)).

**(T4) Realization tie.** The `d = 3` matrix carrier is unitarily equivalent,
by the Kawamoto-Smit site-dependent frame `T(x) = sigma_1^{x1} sigma_2^{x2}
sigma_3^{x3}`, to **two identical copies of the framework's eta-phase
staggered operator**:

```text
    W^dag D W = I_2 (x) D_staggered(eta),
    eta_1 = 1,  eta_2 = (-1)^{x1},  eta_3 = (-1)^{x1+x2},   EXACTLY
```

(runner Part E, `Z_4^3`, every site and direction). The theorem's carrier
class is the framework's realized carrier — the landed staggered surface —
not an analogy.

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
  after:   d <= 3 FORCED    (by the Quantum axiom, within the Dirac-square
                             carrier class: T1 + T2)
           d  = 3 = saturation of the qubit's anticommuting capacity (T3),
                    realized by exactly the landed staggered carrier (T4)
  residual: the SATURATION READING -- why the realized lattice uses the full
            capacity -- and the carrier-class reading (below).
```

The two threes are no longer independent premises that happen to agree: one
bounds the other, and equality is saturation. What remains unforced is
narrower than what was unforced before.

## Named residuals (each graded honestly)

- **Saturation reading** — sub-saturating dimensions exist: the `d = 1, 2`
  Dirac-square carriers are exhibited by the runner (Part F). Nothing here
  selects `d = 3` over `d < 3`; the theorem converts "why 3?" into "why
  saturate?", which is a strictly narrower question but an open one.
- **Carrier-class reading** — the bound binds the Dirac-square NN carrier
  class. That the framework's realized kinetic carrier is in this class is
  the landed staggered realization surface
  ([`STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md`](STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md),
  [`STAGGERED_SCHEME_FORCED_BY_ONE_QUBIT_PER_SITE_LOCALITY_NARROW_THEOREM_NOTE_2026-06-06.md`](STAGGERED_SCHEME_FORCED_BY_ONE_QUBIT_PER_SITE_LOCALITY_NARROW_THEOREM_NOTE_2026-06-06.md));
  landed-but-unaudited conditionality is inherited through T4.
- **No axiom change** — this note changes no axiom memo. If the owner later
  chooses to cite this theorem in a consolidation rewording of the Lattice
  axiom, that is a separate owner-approved, audit-decided step (the
  minimality policy's path), explicitly not taken here.

## Relation to adjacent landed results

- [`AXIOM_STACK_MINIMALITY_CL4C_NO_GO_THEOREM_NOTE_2026-04-29.md`](AXIOM_STACK_MINIMALITY_CL4C_NO_GO_THEOREM_NOTE_2026-04-29.md)
  records the adjacent cell-space no-four-generators claim on `P_A H_cell`.
  T1 is the per-site statement on `M_2(C)` itself — a different, smaller
  space with a two-line obstruction; the two surfaces are complementary rungs
  of the same wall.
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
  T1; the runner's nullspace computation would show rank < 12).
- A non-anticommuting coefficient family satisfying the Dirac-square
  condition (would refute T2).
- A failure of the Kawamoto-Smit conjugation identity at any site/direction
  (would refute T4 and cut the realization tie).
- A retained derivation that the realized kinetic carrier is outside the
  Dirac-square class (would empty the carrier-class reading and limit the
  bound's reach).

## Dependencies

- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md) — the Lattice
  and Quantum axioms whose two 3s this note links.
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
  — the complementary cell-space no-go.

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency. It changes no axiom memo and registers no
primitive. The independent audit lane is the only status authority.

## Audit metadata

```yaml
claim_type_author_hint: bounded_theorem
claim_scope: "Within the translation-covariant nearest-neighbor Dirac-square carrier class over one qubit per site, M_2(C)'s anticommuting self-adjoint-unitary capacity forces d <= 3; Z^3 is the saturating case, and the saturating matrix carrier is Kawamoto-Smit conjugate to the eta-phase staggered carrier. The saturation reading and carrier-class reading remain named residuals; no axiom, primitive, or audit status is changed."
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
