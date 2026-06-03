# Koide Value Bit: Octahedral O_h Equivariance Over-Constrains, It Does Not Derive r = 1/2

**Date:** 2026-06-02
**Claim type:** no_go (bounded over-constraint)
**Status authority:** independent audit lane only; effective status is
pipeline-derived after audit. This note approves no new import, sets no audit
verdict, and does not promote charged-lepton Koide to a derived theorem.
**Primary runner:** `scripts/frontier_koide_octahedral_overconstrains_value_bit.py`
(28/28 PASS), cache
`logs/runner-cache/frontier_koide_octahedral_overconstrains_value_bit.txt`.

## Purpose

The charged-lepton Koide value bit reduces to a single free amplitude ratio:
`Q = 2/3` iff `r = |b|^2/a^2 = 1/2` iff equal C_3 isotype-block energy
(`koide_q23_block_weight_frontier_bounded_note_2026-05-29`, **unaudited**;
`koide_circulant_q_two_thirds_algebraic_narrow_theorem_note_2026-05-10`,
**retained**). The retained Frobenius no-go
(`koide_frobenius_isotype_split_uniqueness_note_2026-04-21`, **retained_no_go**)
proves positive-definiteness + Ad-invariance + scalar/traceless orthogonality
do not force the weight ratio: the invariant inner products on `Herm(3)` form the
two-parameter family `B = alpha Tr(XY) + beta tr(X) tr(Y)`, and the bit is the
free scalar/traceless (equivalently trivial/doublet) ratio.

That freedom is a **C_3 / Ad-invariance** result. The grade-1 generation
carrier sits inside the qubit `Cl(3,0)` and the spatial lattice carries the full
octahedral point group `O_h` (48 signed permutations of the three generation
axes), strictly richer than `C_3`. The open next path of the generation-id
bridge (`koide_generation_id_cl3_grade1_bridge_narrow_theorem_note_2026-06-02`,
**unaudited**) asks whether `O_h`-equivariance, being richer than `C_3`, pins
the bit. This note answers that question.

Non-circular: `Q = 2/3` and `r = 1/2` enter only as check targets; no step
assumes them.

## Result

**O_h equivariance OVER-CONSTRAINS the value bit. It neither derives `r = 1/2`
nor leaves it free: it removes the carrier on which the bit is defined.**

Precisely, four exact statements (all over the generation `R^3` = the three
grade-1 axes, `O_h` acting by signed permutation `H -> g H g^T`):

1. **The C_3 weight freedom does collapse under O_h — on `R^3`.** The space of
   `C_3`-invariant symmetric bilinear forms on `R^3` is 2-dimensional
   (`span{I, J - I}`, the free bit); the space of `O_h`-invariant symmetric
   forms is exactly **1-dimensional**, and the unique invariant form is the
   round metric `lambda I`. So the scope hypothesis "O_h is strictly stronger
   than C_3 here" is literally true.

2. **But a round metric does not select `Q`.** `Q = 1/3 + (1/3) D^2/A^2`, where
   `A` is the C_3-trivial (democratic) component and `D` the C_3-doublet length,
   is a ratio of the **spectrum vector** invariant under any round (scalar)
   re-metricization (`Q(lambda s) = Q(s)`). The three canonical rows —
   democratic `A^2:D^2 = 1:0 -> Q=1/3`, equal-block `1:1 -> Q=2/3`,
   per-dimension `1:2 -> Q=1` — are distinguished by the `A^2:D^2` split, a
   property of the operator's eigendata, not of the metric. Collapsing the
   metric to round therefore does not pin the split.

3. **O_h erases the very block split the bit lives on.** Under `O_h`, `R^3` is
   the irreducible standard rep `T_1u`: the democratic direction `(1,1,1)` is
   `C_3`-invariant but **not** `O_h`-invariant (36 of 48 elements move
   `+-(1,1,1)`), and the `O_h`-average of the democratic projector is the
   isotropic `(1/3) I`. So `O_h` admits no invariant trivial/doublet
   decomposition; it does not refine the `C_3` block structure, it destroys it.

4. **An O_h-equivariant generation mass operator is forced scalar.** The
   `O_h`-commutant on `R^3` is 1-dimensional (Schur on `T_1u`): the only
   `O_h`-equivariant operator is `lambda I`, a fully **degenerate** spectrum
   (`m_1 = m_2 = m_3`) — no generation hierarchy and no Koide structure at all.
   The `C_3`-commutant is 3-dimensional (circulant), which is why `C_3` hosts a
   nondegenerate, Koide-structured spectrum. Likewise, the only
   `O_h`-equivariant operator anticommuting with the chiral grading
   `Gamma_chi = (2/3) J - I` is `0`, so `O_h`-equivariance also kills the chiral
   (anticommuting) mass operator. A non-circulant anticommuting witness does
   exist (`H = |v><w| + |w><v|`, `w perp v`; `{H, Gamma_chi} = 0`, `[H, R] != 0`)
   but is not `O_h`-invariant — confirming the bit is non-vacuous and is removed
   by over-constraint, not by selection.

## Why this is the structural reason the retained chart fails O_h covariance

The retained affine Hermitian chart is only `{+-I}`-covariant under `O_h`
(`koide_q23_oh_covariance_nogo_note_2026-04-22`, **retained_no_go**). This note
supplies the underlying reason: any nondegenerate generation spectrum **cannot**
be `O_h`-equivariant (statement 4), so no chart carrying a real
charged-lepton spectrum can be `O_h`-covariant beyond parity. The prior no-go
attacked a particular chart's covariance group; this note attacks the
isotype-weight freedom directly and shows the obstruction is intrinsic to having
a generation hierarchy, not an artifact of the chart's specific coefficients.

## The preserve-XOR-pin dichotomy

Scanning every intermediate group `C_3 <= H <= O_h`: the largest `O_h`-subgroup
fixing the democratic direction `(1,1,1)` is `C_3v` (order 6), whose `R^3`
invariant-form space is **still 2-dimensional** (bit free) and whose commutant is
2-dimensional (still admits nondegenerate operators). Every enlargement that
would add a constraint pinning the ratio simultaneously adds the sign flips that
destroy the democratic direction. Hence:

> A symmetry group either **preserves** the trivial/doublet split — in which
> case the value bit is defined but **free** — or it enlarges to include the
> sign flips that **erase** the split. No intermediate group simultaneously
> defines the bit and pins its value.

This is a clean separation: the value bit cannot be discharged by enlarging the
generation symmetry from `C_3` toward `O_h`.

## Boundary

This note does NOT claim:

- a derivation of `Q = 2/3`, `r = 1/2`, or the charged-lepton Koide relation;
- that `O_h` is the physical generation symmetry (it shows it cannot be, for the
  mass sector);
- any new axiom, import, or audit verdict.

On `Herm(3)` (as opposed to the generation `R^3`), `O_h` does **not** collapse
the Frobenius family: both `Tr(XY)` and `tr(X) tr(Y)` are `O_h`-invariant, so the
scalar/traceless ratio remains free there. The `R^3` collapse in statement 1 is
specific to the generation-axis metric and is over-constraining precisely
because it forces a degenerate operator (statement 4).

## Verified tiers (origin/main audit ledger)

| claim_id | effective status |
|---|---|
| `koide_frobenius_isotype_split_uniqueness_note_2026-04-21` | retained_no_go |
| `koide_q23_oh_covariance_nogo_note_2026-04-22` | retained_no_go |
| `koide_z3_equivariant_anticommuting_no_go_note_2026-05-16` | retained_bounded |
| `koide_circulant_q_two_thirds_algebraic_narrow_theorem_note_2026-05-10` | retained |
| `koide_q23_block_weight_frontier_bounded_note_2026-05-29` | unaudited |
| `koide_generation_id_cl3_grade1_bridge_narrow_theorem_note_2026-06-02` | unaudited |

## No-Go Discipline Gate

- **N1 alternative routes:** the metric reading (statement 1), the spectrum-ratio
  reading (statement 2), the block-erasure reading (statement 3), the
  equivariant-operator reading (statement 4), and the intermediate-group scan are
  distinguished.
- **N2 wall independence:** the over-constraint is established independently at
  the metric, spectrum, representation, and operator levels.
- **N3 hidden walls:** the note does not assume `O_h` is the generation symmetry;
  it tests the hypothesis and reports over-constraint.
- **N4 residual matching:** the prior chart no-go (`{+-I}` covariance) is
  recovered as a corollary of statement 4 (no nondegenerate `O_h`-equivariant
  spectrum).
- **N5 rhetoric audit:** "over-constrains" / "removes the carrier" is used; no
  "only/last/closes" or finite-enumeration framing.
- **N6 partial-closure scan:** the `Herm(3)` (Reading B) non-collapse and the
  `C_3v` split-preserving subgroup are preserved as the relevant open structure;
  the `C_3` r = 1/2 amplitude pin remains the live frontier.
- **N7 steelman:** a reviewer may object that the bit could be carried on
  `Herm(3)` rather than `R^3`; statement 4 and Section 7 address both —
  `Herm(3)` leaves the ratio free, `R^3` over-constrains.
- **N8 cross-cycle echo:** prior chirality no-go refinements separated the
  carrier algebra from the physical operator; this note follows that separation
  by distinguishing metric, spectrum, and operator levels.

## Next paths this opens

- The value bit stays located at the `C_3`-level `r = 1/2` amplitude pin. Since
  `O_h` enlargement over-constrains, a positive derivation must come from a
  **C_3-internal selection principle** (an extremal/positivity/records functional
  on the circulant surface), not from enlarging the spatial point group.
- The `C_3v` order-6 split-preserving subgroup leaves the bit free but adds the
  three body-diagonal reflections to `C_3`; whether any of those reflections,
  combined with a positivity or reality condition, narrows the 2-parameter form
  is an untested sub-question.
- Statement 4 sharpens the generation-chirality gate: an `O_h`-equivariant chiral
  operator is forced to `0`, so the chiral grading must break `O_h` down at least
  to a split-preserving subgroup — consistent with the `C_3`-orbit-splitting
  requirement of `koide_z3_equivariant_anticommuting_no_go`.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/frontier_koide_octahedral_overconstrains_value_bit.py
```
