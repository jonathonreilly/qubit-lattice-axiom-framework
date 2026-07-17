# Flavor Z=det Fermionic-Statistics Locator

**Date:** 2026-06-04
**Type:** open_gate
**Claim type:** open_gate
**Status authority:** independent audit lane only. This source note sets source
claim metadata only; it does not set, predict, or edit any audit outcome.
**Current source boundary:** bounded support inside the abstract
two-candidate determinant-side scope; physical spin-statistics selection
remains open.
**Trace class:** direct_blocker_closure
**Reachability to target:** partially closes the missing determinant-side
bridge inside the abstract two-candidate Grassmann-vs-bosonic finite algebra
scope, and prunes the route "finite local dimension, ordinary tensor-product
ladders, or Jordan-Wigner realizability by themselves select physical
cross-site CAR/Grassmann statistics".
**Bare retained allowed:** false
**Audit required before effective status change:** true
**Primary runner:** [`scripts/flavor_zdet_fermionic_statistics_admission_2026_06_04.py`](../scripts/flavor_zdet_fermionic_statistics_admission_2026_06_04.py)
**Runner cache:** [`logs/runner-cache/flavor_zdet_fermionic_statistics_admission_2026_06_04.txt`](../logs/runner-cache/flavor_zdet_fermionic_statistics_admission_2026_06_04.txt)
**No-promotion statement:** This source note creates no promotion, no registry
edit, no audit verdict, and no downstream status change; status remains owned
by the independent audit lane.

## Closed Packet

This note isolates the determinant-amplitude input:

```text
Z = det(D + J)
```

The finite packet verifies three sides of the gate:

1. If Grassmann/CAR matter variables are supplied, the finite Berezin Gaussian
   gives the determinant.
2. In the 2026-06-07 repair, the determinant side is no longer merely
   a free import in the **abstract two-candidate** scope: it consumes the
   formal finite occupation-parity `Z_2` grading theorem and the separately
   cited abstract Grassmann forcing bridge, which compares the
   Grassmann and bosonic one-pair-per-site candidates and supplies the
   finite Berezin determinant compatibility.
3. The tested finite hard-core/tensor-product carrier data do not by themselves
   select cross-site CAR/Grassmann statistics.

The packet does not derive the physical-lattice choice of Grassmann/CAR
variables from baseline axioms. It does not introduce a new axiom or
admission.

## 2026-06-07 Bridge Repair

The audit blocker for this row was that the determinant-amplitude input was
treated as a supplied Grassmann/CAR premise. This repair scopes the
determinant side only at the abstract finite-algebra level by citing and
checking two one-hop dependencies without pinning their live
pipeline-derived grades:

- [`FERMION_PARITY_Z2_GRADING_THEOREM_NOTE_2026-05-02.md`](FERMION_PARITY_Z2_GRADING_THEOREM_NOTE_2026-05-02.md)
  supplies an exact algebraic `Z_2` grading on a **supplied ordered occupation
  space**. It does not select that carrier, identify it with the physical
  lattice matter space, or prove a fermion-statistics or superselection rule.
- [`STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md`](STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md)
  supplies the abstract Grassmann forcing bridge at its pipeline-derived
  grade: within the
  explicitly named two-candidate comparison, the Grassmann candidate matches
  the per-site dimension-two readout and gives `det(M)`, while the bosonic
  candidate has the wrong per-site Fock dimension and the wrong scalar
  partition structure.

Composed with the existing finite checks here, those dependencies close the
following narrow statement:

> In the abstract two-candidate matter-generator scope, the
> determinant-amplitude side has one-hop formal/algebraic support: the Grassmann
> candidate carries the finite `det(M)` readout, while the ordinary
> hard-core/tensor and bosonic comparator routes do not supply that same
> readout.

This is **bounded support**, not a physical spin-statistics theorem. The
physical spin-statistics selector remains open: this packet still does not
identify the framework's physical per-site Hilbert space on `Z^3` with the
abstract `Cl(3)` faithful complex irrep, and it still does not derive the
cross-site CAR/Grassmann relations from a deeper baseline axiom.

## Direct Checks

1. **Supplied Grassmann variables realize `det`.** The signed permutation sum
   matches `det(M)` for the tested finite matrix.

2. **Ordinary cross-site qubit ladders commute.** The ordinary two-site tensor
   product does not satisfy CAR across sites.

3. **Jordan-Wigner is a realization, not a selector.** A dressed generator set
   realizes cross-site CAR, but the dressing is an additional representation
   choice inside this packet.

4. **Local dimension two is not enough.** Fermions and hard-core bosons share
   nilpotent two-state local carriers; the difference is cross-site statistics.

5. **Formal parity grading supplies the algebraic comparison.** After this
   packet supplies the ordered two-mode carrier, the occupation-parity row
   supplies `F=(-1)^{Q_total}` and the finite `Z_2` odd/even grading. In the
   runner, the dressed generators are `Z_2`-odd, anticommute across the two
   tested sites, and their bilinear is `Z_2`-even. The physical carrier
   identification remains open.

6. **The Grassmann forcing row supplies the abstract determinant
   bridge at its live pipeline grade.** The cited bridge supplies the
   two-candidate Grassmann-vs-bosonic comparison and the finite Berezin
   determinant compatibility in the abstract scope.

7. **Determinant and permanent differ.** Signed determinant statistics and
   unsigned hard-core/permanent-style statistics are distinct finite choices.

8. **Koide internal chirality is separate.** `Gamma_chi` acts on the internal
   generation factor and commutes with the tested `C3`-equivariant mass
   operator. Spatial CAR selection does not settle that internal residual.

## Scope

This is not a physical spin-statistics theorem and not a baseline derivation
of FS. It says:

- the abstract two-candidate determinant side has bounded one-hop support via
  the formal parity theorem and the separately graded Grassmann bridge;
- the tested finite routes do not force a physical-lattice FS selector; and
- downstream log-det consumers still need their own dependency/audit review
  before any effective status changes.

## Downstream boundary (non-load-bearing here)

The determinant side repaired here is separate from the Koide
occupancy/slot-degree selector. The downstream occupancy-independence theorem
[`KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md`](KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md)
now records a repaired conditional algebraic fork and does not adopt the
per-outcome-cell condition that yields its alternative endpoint. Thus this
row can support the abstract determinant-amplitude side without pretending
that determinant statistics selects a Koide counting or occupancy input.
That downstream row owns its arithmetic evidence; this runner does not replay
or extend it. This note does not adopt an occupancy condition, derive physical
spin-statistics, or edit audit status.

## Dependencies

- [`FERMION_PARITY_Z2_GRADING_THEOREM_NOTE_2026-05-02.md`](FERMION_PARITY_Z2_GRADING_THEOREM_NOTE_2026-05-02.md)
  (formal finite `Z_2` grading on a supplied ordered occupation space; neither
  a physical carrier nor a physical selector by itself).
- [`STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md`](STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md)
  (abstract two-candidate Grassmann forcing bridge; live grade is
  pipeline-derived).
- [`KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md`](KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md)
  (downstream occupancy/slot-degree boundary; bounded-theorem source, not an
  audit verdict).

## No-Go Discipline Gate

The no-go applies only to the finite routes represented in the runner:

| Route | Status in this packet |
| --- | --- |
| On-site Clifford/local dimension | Does not force cross-site CAR. |
| Ordinary tensor-product ladders | Commute across sites. |
| Jordan-Wigner | Realizes CAR after a generator/string choice; not a selector. |
| Abstract determinant-character mathematics | Works in the separately graded two-candidate Grassmann scope. |
| Koide chirality transport | Separate internal-generation residual. |
| Continuum spin-statistics | Not tested here and left open. |

## Provenance

- The runner checks determinant/permanent arithmetic, ordinary ladder
  commutation, Jordan-Wigner CAR realization, local nilpotency, the cited
  bridge's source boundary, parity-graded composition, dependency boundary
  language, and internal `Gamma_chi` separation.
- No `docs/audit/**` status is updated by this packet.
- No new axiom is introduced.
