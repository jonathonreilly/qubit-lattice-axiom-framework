# The Yang–Mills Mass Gap on a Fixed Planck Lattice: a Fundamental Length Dissolves the Continuum Obstruction

**Date:** 2026-06-09
**Claim type:** bounded_theorem (fixed-`a` existence + strong-coupling gap) + an explicit reframing of an open problem
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Primary runner:**
[`scripts/frontier_yang_mills_gap_fixed_planck_lattice_2026_06_09.py`](../scripts/frontier_yang_mills_gap_fixed_planck_lattice_2026_06_09.py)
**Cached runner output:**
[`logs/runner-cache/frontier_yang_mills_gap_fixed_planck_lattice_2026_06_09.txt`](../logs/runner-cache/frontier_yang_mills_gap_fixed_planck_lattice_2026_06_09.txt)
(SCORECARD: PASS=13, FAIL=0)

> **This note does NOT solve the Clay Yang–Mills problem.** It makes a precise,
> creative claim about why the framework's *specific* commitments make its version
> of the problem narrower than Clay's, and establishes the pieces that genuinely
> follow — while naming, in full, the pieces that remain open.

---

## The idea

The Clay Millennium Yang–Mills problem asks for a **continuum** (`a → 0`) 4D
non-abelian gauge quantum field theory with a mass gap. The `a → 0` limit is the
hard part: it is where the uniform bounds and the constructive-QFT machinery are
missing.

The framework makes an unusual commitment that changes the question: the lattice
spacing `a` is the **Planck length**, a *fundamental minimal length*, **not a
regulator to be removed**. The framework never takes `a → 0`. Its physics is the
infrared effective theory (`p ≪ 1/a = M_Pl`) of a **fixed-spacing** lattice QFT.
Under that commitment the mass-gap question reorganizes into three pieces — two
that are rigorous (or rigorous in a controlled regime) and one that is the honest
residual.

## (A) Existence is rigorous at fixed `a`

At fixed `a` the framework's `SU(3) × U(1)` Wilson + staggered theory is a
rigorously-defined QFT — there is no continuum obstruction to face:

1. **The path integral converges.** The Wilson action is a bounded function on the
   compact group manifold, so the finite-volume partition function is a finite,
   positive integral (runner Part A: `Z` finite and positive for `SU(2)` and
   `U(1)` at `β = 6`). The fermions integrate to a determinant `det D[U]`, positive
   for the relevant staggered setup, leaving a well-defined positive measure.
2. **Reflection positivity → a positive transfer matrix** `T`, with
   `H = -(1/a) log T ≥ 0` (Osterwalder–Seiler 1978). The runner verifies the
   spectrum-condition structure (transfer eigenvalues in `(0,1]` after vacuum
   normalization).
3. **Perron–Frobenius → a unique ground state with a finite-volume gap.** The
   transfer matrix is *positivity-improving* (strictly positive kernel), so its
   top eigenvalue is non-degenerate: a unique vacuum and a spectral gap
   `-\log(λ_1/λ_0) > 0` at every finite volume (runner Part A).

So the word that made the wall sound impassable — *existence* — is, for the
framework's fixed-`a` setting, a **cited theorem**, not an open problem.

## (B) The mass gap is rigorous at strong coupling

For the non-abelian sector the convergent character / strong-coupling expansion
gives a Wilson-loop **area law** with string tension `σ > 0` — confinement, hence
exponential clustering, hence a **mass gap** (Osterwalder–Seiler; Münster). The
runner computes `σ(β) = -\log⟨\text{plaquette factor}⟩ > 0` for `SU(2)` and `U(1)`
at strong coupling, and verifies the loop obeys an **area** law
`\ln⟨W⟩ = -σ\,(R\,T)` (linear in area, not perimeter — the signature of
confinement, not a trivial perimeter/self-energy law).

## (C) The gap is gauge-resolved — and it matches reality

This is the creative payoff. The gap is **not** a single yes/no; it depends on the
gauge group, and the framework's `U(1) × SU(3)` content gives exactly the observed
spectrum:

- **`U(1)` (hypercharge/EM)** has a weak-coupling **Coulomb phase** in 4D — rigorous
  (Guth 1980; Fröhlich–Spencer 1982). That phase is **gapless**: it is the
  **massless photon**. The framework's `U(1)` sits here.
- **`SU(3)` (color)** is **confining/gapped** — area law at strong coupling, believed
  at all couplings. Massive glueballs and a linear quark potential; **no massless
  gluon**.

So the framework predicts precisely what we see: a massless photon and a confined,
gapped gluon sector. The "mass gap" is real where nature has one (color) and
absent where nature has none (electromagnetism), with both following from the same
fixed-`a` lattice structure.

## (D) What is NOT solved — the honest residual

- **The Clay problem itself (continuum `a → 0` gap) is not solved** — and the
  framework does not need it. A fundamental length means there is no continuum
  limit to construct.
- **The `SU(3)` gap at the framework's actual coupling `β = 6` is not rigorously
  proven.** `β = 6` lies in the scaling/crossover region where the strong-coupling
  expansion no longer converges; the gap there is supported by lattice Monte Carlo
  and the strong-to-scaling continuity, not by a convergent expansion. This is the
  genuine open quantitative piece.
- **The IR scale `Λ_QCD ≪ M_Pl`** is generated by RG flow from `β = 6` by
  dimensional transmutation; the flow is standard but its rigorous control at
  `β = 6` is part of the same open piece.

## Net

For the framework's fixed-Planck-lattice setting: **existence is rigorous, the
mass gap is rigorous at strong coupling, and the gauge-resolved gap matches the
observed spectrum (massless photon + gapped color sector).** The famous
continuum obstruction is dissolved by the fundamental length rather than solved;
the one genuinely-open quantitative residual is the `SU(3)` gap at `β = 6` (the
scaling region), which is exactly the place a future convergent-expansion or
constructive bound would have to reach. The contribution is the **reframing plus
the rigorous fixed-`a` pieces**, not a Clay-problem solution.

## What this note does NOT claim

- **Not** a solution to the Clay Yang–Mills existence-and-mass-gap problem.
- **Not** a rigorous `SU(3)` gap at `β = 6` (named open residual).
- **Not** a new dynamical observable; the gauge content, `β = 6`, and the staggered
  realization are the framework's existing inputs/gates, used not re-derived.
- **No** new axiom, primitive, vocabulary, or class tag; **no** PDG/fitted input.
  Standard results (Osterwalder–Seiler 1978; Guth 1980; Fröhlich–Spencer 1982;
  Münster) are cited as method/comparator. Sets no audit status.

## Dependencies

- [SCALE_REFERENCE_PRIMITIVE_NOTE.md](SCALE_REFERENCE_PRIMITIVE_NOTE.md) — the
  fundamental length `a⁻¹ = M_Pl` whose *fixedness* is the load-bearing reframing.
- [KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
  — the hypercubic-symmetric surface on which RP/Osterwalder–Seiler apply.
- `EMERGENT_POINCARE_FREE_SECTOR_FROM_KINETIC_ISOTROPY_PRIMITIVE_BOUNDED_THEOREM_NOTE_2026-06-09.md`
  (context, plain-text reference; in review as PR #3380, not yet on main) — the
  free-sector relativistic structure this gauges.
- [STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)
  — the matter realization (Tier-A admission) whose determinant enters the measure.

**No-promotion statement:** this note does not promote, demote, or set the audit
status of any dependency. The independent audit lane is the only status authority.
