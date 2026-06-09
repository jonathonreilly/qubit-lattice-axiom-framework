# Free-Sector Emergent Poincaré Covariance, Assembled from the Kinetic-Isotropy Primitive (OS0)

**Date:** 2026-06-09
**Claim type:** bounded_theorem (assembly/synthesis; free Gaussian matter sector)
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Primary runner:**
[`scripts/frontier_emergent_poincare_free_sector_from_os0_2026_06_09.py`](../scripts/frontier_emergent_poincare_free_sector_from_os0_2026_06_09.py)
**Cached runner output:**
[`logs/runner-cache/frontier_emergent_poincare_free_sector_from_os0_2026_06_09.txt`](../logs/runner-cache/frontier_emergent_poincare_free_sector_from_os0_2026_06_09.txt)
(SCORECARD: PASS=19, FAIL=0)

---

## Role: the missing generator the primitive supplies

The single-clock theorem
([`AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`](AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md),
corollary C4) already delivers the Wightman structure **W1–W5**: a Hilbert
space, a one-parameter unitary time group `U(t)=e^{-iHt}`, the spectrum condition
`H≥0`, microcausality, cluster decomposition, and a codimension-1 Cauchy slice.
That is the Wightman/Haag–Kastler framework **minus the Lorentz boost and
rotation generators** — the one structural piece that mixes time with space.

Those missing generators are exactly the content of **Euclidean SO(4) invariance
of the regulator** (the Osterwalder–Schrader axiom OS0): under OS reconstruction,
Euclidean SO(4) becomes Lorentz SO(3,1) on the reconstructed Hilbert space, i.e.
it supplies the boosts `K_i` and rotations `J_i`. As of 2026-06-09 that invariance
is an **approved framework primitive**, `kinetic_isotropy_primitive`
([`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)),
`c_t=c_s` on the hypercubic-symmetric Euclidean `Z^4` surface. Crucially the
primitive also **de-circularizes** OS0: previously SO(4)/Lorentz covariance was
the *output* of the emergent-Lorentz program, so citing it as an *input* to a
reconstruction was circular; as an approved primitive it is a clean input.

This note assembles the on-main pieces with that primitive into a **continuum
Poincaré-covariant Wightman QFT for the free Gaussian matter sector**, and is
explicit about the residual bridges that keep it bounded.

## The assembly (verified by the runner)

1. **OS0/OS1 — Euclidean SO(4), including the boost plane.** The free continuum
   Euclidean Dirac 2-point `G_E(p)=(m-iγ·p)/(p²+m²)` is SO(4)-bispinor covariant
   to machine precision, verified not only in a spatial (`x-y`) plane but in the
   **`τ-x` plane** — the mixed time–space rotation that becomes a Lorentz boost.
   The vector rotation is derived from the spinor rotation by the trace identity
   `R_{ab}=¼ tr(γ_a S γ_b S^{-1})` and confirmed to be a genuine SO(4) element.
   (Realization/check of rung A,
   [`LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md`](LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md);
   the *premise* OS0 is now the approved primitive.)
2. **Wick step — SO(4) → SO(3,1).** A `τ-x` Euclidean rotation analytically
   continues to a Minkowski boost (rapidity `η`); the continued boost preserves
   the Minkowski metric (`LᵀgL=g`) and the on-shell invariant `p²=m²`. The
   Euclidean rotational invariant continues to the Lorentz invariant.
3. **The Poincaré algebra closes.** With the boost generators `K_i=M^{0i}` (the
   newly-supplied piece) adjoined to the rotations `J_i=M^{jk}` and the
   single-clock translations `P^μ` (with `H=P^0`), every commutator of
   `{M^{μν}, P^μ}` lies in the span of the generators — verified across all 100
   commutators by least-squares span-membership (convention-independent), with
   `[P^μ,P^ν]=0`.
4. **Positive-energy representation.** The forward mass shell
   `p^0=+\sqrt{p²+m²}≥0` maps into the forward cone under every boost, so the
   spectrum condition `H≥0` (W2) is boost-invariant: the assembled
   representation is a **positive-energy** Poincaré representation, not merely a
   covariant one.
5. **OS-axiom checklist.** OS0 (approved primitive, new); OS1 (SO(4) of the free
   2-point, rung A, `retained_bounded`, de-circularized); OS2 (reflection
   positivity of the free Dirac Gaussian, *derived* in the reconstruction note,
   RP `retained_bounded`); OS3 (cluster with mass gap `m`, `retained_bounded`);
   W1–W5 (single-clock, lattice `positive_theorem`). The boost/rotation
   generators follow from OS0 + the standard OS reconstruction theorem on the
   now-approved hypercubic-symmetric surface.

## What this establishes

For the **free Gaussian matter sector** in the continuum limit, the framework now
assembles a **Poincaré-covariant, positive-energy Wightman QFT**: the boost and
rotation generators that W1–W5 lacked are supplied by the approved OS0 primitive
(via SO(4)→SO(3,1)), the algebra closes, and the spectrum condition is
boost-invariant. The conceptual hardest part — that a discrete spatial lattice
with emergent time can carry exact Lorentz boosts at all without species-dependent
Lorentz violation — is the part the primitive settles.

## What this leaves open (honest residual — why it is bounded, not retained)

- **G1: the lattice→continuum measure bridge.** OS2/OS1 are established for the
  *continuum* free Dirac Gaussian; that the framework's *lattice* fermion measure
  converges to it is shown only at the 2-point level. The full
  measure-convergence (and the `1+1d → 4D` arena bridge) is **not** supplied here.
  This is moderately hard, not textbook.
- **Interacting continuum existence.** Everything here is the **free** (`U=1`)
  Gaussian sector. The interacting `SU(3)×U(1)` continuum measure is the
  constructive-QFT/mass-gap-class problem and is **untouched**.
- **RP is not newly ratified here.** OS2 is cited (`retained_bounded`/derived),
  not re-proven; statistics selection (CAR vs Bose) remains gated on the
  reconstruction `R` and its rungs.
- **The primitive supplies no dynamical content.** No mass ratio, coupling, or
  mixing angle is touched; the irreducible dimension-6 spatial-cubic lattice
  Lorentz violation (from the Lattice axiom's cubic adjacency, Planck-suppressed)
  and its Planck-pin readout are separate and unchanged.

## What this note does NOT claim

- **Not** interacting emergent Lorentz invariance, and **not** a Poincaré
  upgrade of the *interacting* W1–W5 — free Gaussian sector only.
- **Not** a new derivation of SO(4) (rung A already derives it in the continuum
  limit); the contribution is the *assembly* plus the approved-primitive premise
  that de-circularizes it.
- **Not** an audit verdict; the independent audit lane sets effective status. The
  approved `kinetic_isotropy_primitive` chain-satisfies without bounding, but the
  G1 measure bridge keeps this assembly a bounded_theorem until that bridge is
  retained.
- **No** new axiom, primitive, repo vocabulary, or class tag; **no** PDG/fitted
  input.

## Dependencies

- [KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
  — OS0 (Euclidean SO(4) invariance), the boost/rotation ingredient; approved primitive.
- [AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md](AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md)
  — W1–W5 (the structure missing only the boosts).
- [LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md](LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md)
  — rung A, the free-fermion SO(4) realization (de-circularized by OS0).
- [FREE_FIELD_OS_WIGHTMAN_RECONSTRUCTION_CONDITIONAL_THEOREM_NOTE_2026-05-30.md](FREE_FIELD_OS_WIGHTMAN_RECONSTRUCTION_CONDITIONAL_THEOREM_NOTE_2026-05-30.md)
  — OS2 (RP of the free Dirac Gaussian) derived; gates G1/G2 referenced here.
- [LORENTZ_BOOST_COVARIANCE_3PLUS1D_THEOREM_NOTE.md](LORENTZ_BOOST_COVARIANCE_3PLUS1D_THEOREM_NOTE.md)
  — the free-scalar SO(4)→SO(3,1) companion.
- [SCALE_REFERENCE_PRIMITIVE_NOTE.md](SCALE_REFERENCE_PRIMITIVE_NOTE.md)
  — the dimensionful anchor (units only).

**No-promotion statement:** this note does not promote, demote, or set the audit
status of any dependency. The independent audit lane is the only status authority.
