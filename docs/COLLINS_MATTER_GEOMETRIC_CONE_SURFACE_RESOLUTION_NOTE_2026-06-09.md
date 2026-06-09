# Collins Matter-Cone vs Geometric-Cone: Surface-Resolution of the Marginal Velocity Anisotropy

**Date:** 2026-06-09
**Claim type:** bounded_theorem + structural no-go (two genuine advances + a synthesis)
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome. The labels are source-side claim-boundary
declarations, not audit verdicts.
**Primary runner:**
[`scripts/frontier_collins_matter_geometric_cone_surface_resolution_2026_06_09.py`](../scripts/frontier_collins_matter_geometric_cone_surface_resolution_2026_06_09.py)
**Cached runner output:**
[`logs/runner-cache/frontier_collins_matter_geometric_cone_surface_resolution_2026_06_09.txt`](../logs/runner-cache/frontier_collins_matter_geometric_cone_surface_resolution_2026_06_09.txt)
(SCORECARD: PASS=18, FAIL=0)

---

## Role

The Collins–Perez–Sudarsky–Urrutia–Vucetich (*PRL* **93** (2004) 191301)
naturalness problem is the radiative regeneration of the **marginal**
(dimension-4) velocity anisotropy `c_t ≠ c_s`. In framework-native terms (the
2026-06-08 session framing) it is the statement that the **matter cone** — the
renormalized, species-dependent group/Lieb-Robinson velocity `v_LR` of an
interacting field — drifts away from the **geometric cone** — the species-blind
front velocity `v_front = 1` fixed by one-tick-one-edge graph reachability
([`LATTICE_NN_LIGHT_CONE_NOTE.md`](LATTICE_NN_LIGHT_CONE_NOTE.md)). The
quantified-obstruction note
([`LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06.md`](LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06.md))
makes this quantitative: `δv ~ α/4π`, and the asymptotically-free gauge
anomalous dimension `γ ~ 0.15–0.34` is `~10–15` orders too weak to suppress it
below the experimental Lorentz-violation bounds.

This note **localizes the obstruction to a surface choice** and resolves the
problem on the framework's own canonical surface. The pivotal observation: the
`δv ~ α/4π` obstruction is computed on the **anisotropic continuous-time**
surface (spatial `Z^3` + continuum time, the spacetime-anisotropy ratio
`ξ = a_τ/a_s → 0`), whereas the framework's **own retained matter realization**
— the canonical isotropic staggered action with `η_0 = 1`, the surface of the
retained free-2-point SO(4)/RP/dispersion results
([`LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md`](LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md))
— is the **symmetric `Z^4`** surface (`ξ = 1`), where the 4D hypercubic group
`B_4` forbids the marginal anisotropy.

The runner computes the one-loop (gauged, rainbow) velocity self-energy
coefficient on a one-parameter family of surfaces `ξ = a_τ/a_s` and establishes:

1. **(Advance 1 — interacting `B_4` closure.)** On the symmetric `Z^4` surface
   the **interacting one-loop** velocity coefficients satisfy `z_t = z_s` to
   machine precision (`|δv| < 6×10⁻¹⁸`), **representation-blind** (no species
   split). This closes the **Collins-relevant** part of the retained
   free-2-point SO(4) note's named-open *interacting* item — the marginal
   (dimension-4) velocity anisotropy — at one loop, all-orders by the
   exact-symmetry mechanism (`B_4` axis relabeling of a hypercubic-symmetric
   measure). The broader interacting-SO(4) questions (taste-symmetry
   restoration, full n-point covariance) are **not** addressed and are not
   needed here: the Collins operator is the marginal one, and `B_4` forbids it
   in *any* hypercubic-symmetric regularization, the gauged Wilson action
   included.

2. **(Localization.)** On the continuous-time surface (`ξ → 0`) the same
   coefficient regenerates a **robust nonzero** anisotropy `|δv| ≈ 0.08 g²`
   (stable to ~1% across loop cutoff, resolution, IR boson mass, and lattice
   size) that **scales with the gauge Casimir → species split**. This is the
   Collins obstruction, reproduced and pinned entirely to the surface.

3. **(Interpolation.)** `|δv|(ξ)` is machine-zero at `ξ = 1` and jumps to
   `O(10⁻²)` for every `ξ < 1`, rising through the resolved regime. The
   anisotropy is minimal **exactly** at the symmetric point.

4. **(Advance 2 — structural no-go.)** On the continuous-time surface **no**
   internal/flavor ("taste") symmetry can restore `z_t = z_s`: such a symmetry
   is an overall index factor common to the temporal and spatial coefficients,
   so it cannot touch their difference (verified: any nonzero rescaling of a
   nonzero `δv` stays nonzero). The **only** operation that zeroes `δv` is the
   `B_4` temporal↔spatial axis relabel, which is a symmetry of the
   integrand-plus-measure **iff** `ξ = 1`. Therefore the obstruction lives in
   the loop **measure** (an uncut temporal integral vs a cut spatial
   Brillouin zone), **not in the algebra**, and a temporal UV cutoff — i.e.
   **discrete time** — is the *unique* protection route.

## The argument

### (A) The problem is one number, and that number is the surface ratio `ξ`

Spatial isotropy is automatic: the regenerated spatial self-energy is an
`O_h`-invariant tensor, whose invariant space is one-dimensional, so the three
spatial speeds stay equal (a single scalar `c_s`; see the interacting-attractor
note Part B). The entire marginal anisotropy is therefore the *single*
temporal-vs-spatial ratio `c_t / c_s`. The runner's Part 0 reproduces the
group-theory mechanism: `O_h × time-parity` leaves **two** diagonal quadratic
kinetic coefficients (`c_t ≠ c_s` allowed), while `B_4` leaves **one**
(`c_t = c_s` forced). The whole Collins problem in this framework is the binary
"is the kinetic measure `B_4`-symmetric?", i.e. "is `ξ = 1`?".

### (B) On the framework's canonical surface the interacting answer is `δv = 0`, exactly, rep-blind

The framework's canonical free staggered action (`η_0 = 1`,
`η_μ(n) = (-1)^{Σ_{ν<μ} n_ν}`) discretizes **all four** directions — including
Euclidean time — on the same nearest-neighbor footing. The retained free-2-point
result is *unconditionally* SO(4)-covariant there. The runner extends this to the
**gauged one loop**: the rainbow velocity self-energy coefficient is identical in
the temporal and spatial directions to machine precision (Part 1), because the
`B_4`-symmetric loop measure maps the temporal coefficient integral onto the
spatial one by axis relabeling. The gauge representation enters only as an overall
`g² C_2(R)` factor multiplying a vanishing spacetime difference, so **species
differences vanish too** — the protection is representation-blind and, being an
exact symmetry of the regulated action, holds to all orders. The leading residual
Lorentz violation is the dimension-6 `ℓ = 4` cubic harmonic (`c_4 = -1/3`), which
with `a⁻¹ = M_Pl` is `~(1/3)(E/M_Pl)² ≈ 2×10⁻³⁹` at `1 GeV` (Part 5).

### (C) The obstruction is the anisotropic-regulator artifact, and on it nothing can help

On the continuous-time surface the temporal loop momentum is integrated over the
whole line (no temporal cutoff) while the spatial momenta are cut at the
Brillouin-zone edge `1/a_s`. This measure asymmetry **is** `δv`: the runner finds
a robust `|δv| ≈ 0.08 g²` that splits species (Part 2), growing monotonically from
machine-zero as `ξ` decreases from 1 (Part 3). Because the asymmetry is in the
measure, not the vertex algebra, the standard custodial candidates are powerless
**by construction**: CPT (the split is CPT-even), `O_h` (spatial only), the gauge
Ward identity (does not tie `c_t` to `c_s`), and internal/taste symmetry (commutes
with the spacetime index, hence an overall factor common to `c_t` and `c_s`) all
leave `c_t - c_s` untouched. The runner verifies the elimination (Part 4): only
the `B_4` axis relabel zeroes `δv`, and it is available **iff** `ξ = 1`. This is
the **structural no-go**: on strictly continuous time, *no symmetry can protect
emergent Lorentz invariance*; discretizing time is the only route. (This is the
honest direction — it makes the continuous-time horn worse, and tells us exactly
where the resolution must live.)

### (D) The framework's own structure selects the protected surface

Three retained/standing features all point at `ξ = 1`, and the obstruction horn
contradicts each:

- **Canonical matter realization.** The framework's staggered action is the
  symmetric `Z^4` action (`η_0 = 1`); the retained free-SO(4) result lives there.
  The continuous-time surface is *not* the framework's matter realization — it is
  the Hamiltonian/Kogut–Susskind anisotropic regulator (`ξ → 0`).
- **One-tick-one-edge.** The retained finite-graph reachability structure
  advances the causal front by exactly one edge per tick — the combinatorial
  content of `ξ = 1`. The obstruction needs `ξ → 0` (infinitely many ticks per
  edge), which contradicts one-tick-one-edge.
- **No retained consumer of continuum time.** Every retained consumer of the
  single-clock evolution uses integer transfer steps `T^n`; continuous Stone time
  `U(t) = e^{-iHt}` is the `a_τ → 0` IR reconstruction (the unaudited Step-1
  interpolation), not the UV regulator where the loop is computed.

Two standing objections are answered head-on. *"`a_τ` is removable"* (the transfer
fixes only `a_τ·H`): true for the **absolute** scale, but `δv` is dimensionless
and depends only on the **ratio** `ξ`, which one-tick-one-edge fixes combinatorially
— the removable absolute scale is irrelevant. *"Derived time outputs continuous
Stone time, so `ξ → 0`"*: the derived object is the **IR continuum evolution**; the
UV **regulator** in which loops are computed is the discrete transfer on `Z^4`, and
the continuum is taken as the symmetric `a → 0` limit afterward — the standard,
Lorentz-preserving order of operations, and the one the framework's own free-SO(4)
construction uses.

## Verdict

**Collins is reduced to a single, mild, well-motivated admission, and on the
framework's own canonical surface it is solved.** On the symmetric `Z^4` surface
— the surface of the framework's retained free-SO(4)/RP/dispersion constructions
— the interacting one-loop (and, by exact `B_4`, all-orders) marginal velocity
anisotropy is **identically zero, representation-blind**; emergent Lorentz is
radiatively stable, with only the Planck-suppressed dimension-6 residual. The
`δv ~ α/4π` obstruction is an artifact of regulating on the non-canonical
anisotropic continuous-time surface, on which — by the structural no-go — **no
custodial symmetry could ever help**. The single remaining admission is the
metric identification `ξ = a_τ/a_s = 1` (the fundamental tick-length equals the
fundamental edge-length), which is the framework's own units choice (`η_0 = 1`)
and the unique value consistent with one-tick-one-edge.

This is a sharper position than the field-wide statement that Collins requires a
custodial symmetry the framework lacks: here the protecting symmetry (`B_4`) is
*present on the framework's canonical surface*, the obstruction is a
*regulator-selection* artifact rather than a prediction, and the entire residual
is one structural-geometry premise rather than an open dynamical naturalness gap.
That premise (`ξ = 1`) is classified below: it is **not** a coupling and **not** a
scale primitive, but a structural lattice-geometry premise broadly of the Lattice
axiom's cubic-adjacency *type* — though **strictly stronger** than the spatial-isotropy
case, because it adds a temporal generator the axioms disclaim rather than respecting
the axiom-resident `O_h` (see the sharpened comparison below) — owner-approvable at
**retained (non-bounding)** grade, under which `δv = 0` is retained, not bounded. The
cost of solving Collins in this framework is therefore a single minimal
lattice-geometry primitive, strictly cheaper than the custodial symmetry the field
requires, though **not** a mere relabel of the cubic adjacency.

## What this note establishes vs leaves open

- **Establishes** (verified by the registered runner):
  (1) interacting one-loop `B_4` protection of the **marginal** velocity
  anisotropy on the symmetric `Z^4` surface, rep-blind, to machine precision —
  closing the Collins-relevant (marginal) part of the free-SO(4) note's
  named-open *interacting* item at one loop (all-orders by the exact-symmetry
  mechanism; the broader taste/n-point interacting-SO(4) questions are out of
  scope);
  (2) the structural no-go — on continuous time the obstruction is a loop-measure
  asymmetry and no internal/spacetime symmetry can remove it; only a temporal UV
  cutoff (`ξ = 1`) can;
  (3) the localization/interpolation — `|δv|(ξ)` is machine-zero at `ξ = 1`,
  robustly nonzero and species-splitting for `ξ < 1`.
- **The single residual premise `ξ = 1`** — classified and resolvable (next
  section). It is **not** derivable from the *current* retained results, but it
  is a structural lattice-geometry premise of the same type as the Lattice
  axiom's cubic adjacency, owner-approvable at retained (non-bounding) grade.

## Status of the residual premise: three distinct freedoms, and the one that is the genuine admission

A precise accounting matters here (the framework is 3 space + emergent time, **not**
4 space). The Euclidean object on which loops are computed is the regulator block
`Λ = Z^3 × Z_τ` — the *same* block the single-clock evolution theorem
([`AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`](AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md))
and the free-2-point SO(4) note already use, with finite Euclidean-time spacing
`a_τ`. "`B_4`/hypercubic" is a symmetry of *that block's action*; after Wick
rotation the `τ`-axis is Lorentzian time. Nothing here makes time a fourth
*spatial* dimension.

Three logically independent quantities live in the time direction (the
`/exercise` "three freedoms", `XI_KINETIC_ISOTROPY_INDEPENDENCE_ADMISSION_NOTE`,
PR #3360):

1. **The absolute scale `a_τ`** — *removable*. The transfer fixes only `a_τ·H`
   ([`SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md`](SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md)),
   and the one approved dimensionful ruler (`a⁻¹ = M_Pl`) sets it.
2. **The spacing ratio `a_τ/a_s`** — *derived*. One record tick reaches exactly
   one nearest-neighbor edge, pinned by the Lattice axiom's **no-diagonal** clause
   (6-NN, not 26-NN; with diagonals a tick would span `√3` and decouple) plus the
   retained reachability theorem
   ([`MIN_TIME_STEP_TIED_TO_THE_LATTICE_EDGE_BY_CAUSAL_LOCALITY_RATIO_DERIVED_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-08.md`](MIN_TIME_STEP_TIED_TO_THE_LATTICE_EDGE_BY_CAUSAL_LOCALITY_RATIO_DERIVED_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-08.md),
   currently `audited_renaming`). This is the **geometric cone** `v_front`.
3. **The kinetic-form ratio `c_t/c_s`** — *the genuine admission*. This is the
   **matter cone** — the Euclidean kinetic normalization (OS0) of the action — and
   PR #3360 **proves it independent** of `Σ = {Lattice, Quantum, Record}` +
   emergent-time + RP (a Robinson/Vaught independence theorem: two models, one with
   `c_t = c_s` and one with `c_t/c_s = 2.5`, both satisfy `Σ`, differing only on the
   Lorentz output). Collins is *exactly* this third freedom.

So my earlier "`ξ = a_τ/a_s`" framing conflated (2) and (3): the spacing ratio is
derived; the **kinetic-form isotropy `c_t = c_s` is the load-bearing, independent
admission**. The runner's `a_τ`-family breaks both at once (a naive action ties form
to spacing); the discrete-tick runner's `r_t ≠ r_s` deformation isolates the form
break at equal spacing — that broken-form case is exactly freedom (3).

**Why it is not derivable — sharply.** RP, the single-clock theorem, the
scale primitive, and causal order are all **`ξ`-blind**: RP yields a positive
transfer with `H ≥ 0` for *every* `c_t/c_s` (PR #3360 leg A), so it cannot force
`c_t = c_s` — and since `c_t = c_s` *is* the OS0/Lorentz output, deriving it from
RP would be circular. The scale primitive is barred (it carries zero dimensionless
content; `c_t/c_s` is dimensionless). The velocity RG leaves the common-speed
direction marginal. Independence is proven, not merely unestablished.

**`c_t = c_s` is a structural admission of the same broad *type* as spatial isotropy
— but strictly stronger, and the comparison must be stated tightly.** Both are
dimensionless covariance premises on the regulator (not couplings/mass-ratios, which
the scale-purity rule rightly blocks; and **not** a dynamical custodial symmetry, the
expensive field-wide fix, which here is *impossible* by the structural no-go). A
ground-up re-examination
([`XI_KINETIC_ISOTROPY_INDEPENDENCE_ADMISSION_NOTE_2026-06-09.md`](XI_KINETIC_ISOTROPY_INDEPENDENCE_ADMISSION_NOTE_2026-06-09.md),
PR #3360, runner Parts E–F) sharpens the comparison and corrects an earlier
over-reading. Spatial isotropy `z_x = z_y = z_z` is itself **not** a bare-axiom
theorem: the witness **M3** (a spatially anisotropic `K_x ≠ K_y` action on the same
`Z³`/Quantum/Record) is axiom-faithful and breaks `O_h`. What makes spatial isotropy
cheap is that its symmetry **`O_h` is a genuine automorphism of the `Z³` 6-NN graph
the Lattice axiom asserts** (all 48 signed permutations preserve `{±e_i}`; a shear
does not) — so it follows from "respect the cubic symmetry you already asserted." The
`z_t = z_s` relabel is **not** the same move: the space↔time generator is **not** an
automorphism of any axiom object — under axiom-resident `O_h × time-parity` the four
axes split into **two** orbits `{t}` and `{x, y, z}`, and **no 4th anticommuting
Clifford generator exists** in `M₂(ℂ) = Cl(3,0)` (`{T, σ_i} = 0 ⟹ T = 0`; the
pseudoscalar `σ_x σ_y σ_z = i·I` is central). So `ξ = 1` **adds** a generator the
axioms disclaim rather than **respecting** one they assert: it is regulator geometry
the substrate does not host, **strictly stronger** than spatial isotropy and rooted in
the same `Cl(3)` / `d = 3` structure. It remains far cheaper than a dynamical
custodial symmetry — but **cubic → hypercubic is not a relabel**.

**Resolution.** Record the matter-sector OS0 isotropy `c_t = c_s` (equivalently,
"the matter realization is the `B_4`-symmetric staggered action `η_0 = 1`") as an
**owner-approved structural primitive** — companion to the Lattice axiom's cubic
adjacency, registered in `axiom_premise_nodes.json` by the same explicit-approval
mechanism that recorded the Record axiom and the scale-reference primitive. PR
#3360's independence result is precisely what makes this *clean*: an independent
premise is consistent and non-redundant to add. Under it, the Collins marginal
anisotropy is **identically zero to all orders, representation-blind** (Parts 1, 4)
— emergent Lorentz radiatively stable at **retained** (non-bounding) grade, residual
only the Planck-suppressed dimension-6 cubic harmonic. Honest caveat: this is
owner-approval of a minimal structural premise (the framework deliberately keeps
time emergent), not a derivation — but it is the minimal, canonical,
retained-consistent choice, and strictly cheaper than the custodial symmetry the
field requires. The spacing freedom (2) is already derived; only the form
freedom (3) is approved.

## Honest scope

- The rainbow self-energy uses a Feynman-gauge-like massless lattice boson
  `1/k̂²` and a naive (exactly-`B_4`) fermion. The **load-bearing** output is
  structural — `0` on the symmetric surface (exact `B_4` relabeling, all orders,
  rep-blind) vs robust nonzero-and-rep-split on the anisotropic surface, and the
  *origin* of the difference. The precise `O(1)` anisotropic coefficient (full
  Wilson/clover vertex, Ward tadpole/seagull, on-shell gauge prescription) is the
  known open input and is **not** claimed here; it does not affect the
  zero-vs-nonzero dichotomy or the no-go.
- The continuous-time `|δv| ≈ 0.08 g²` is verified IR-insensitive and converged;
  its sign and exact magnitude are scheme/vertex-dependent and not load-bearing.
- `B_4` gives Euclidean `t↔s` symmetry; the velocity ratio `δv` is a ratio of
  kinetic coefficients invariant under the Euclidean→Minkowski continuation, so
  the `δv = 0` conclusion carries over. The separate finite-`a` fact `v_LR ≈ 0.93
  < v_front = 1` (matter cone inside geometric cone) is Lorentz-*invariant* as
  long as it is species-common, which `B_4` guarantees; it is not the Collins
  defect.
- **No** new axiom, primitive, repo vocabulary, or class tag; **no** PDG / fitted
  / `g_bare` input. The LV bounds and the cited literature are comparators/scope
  only. This note does **not** set or change any audit status.

## Reprove-and-cite ledger

- **Reproven here** (runner): the `O_h`-vs-`B_4` diagonal-quadratic invariant
  counts (2 vs 1); the interacting one-loop `z_t = z_s` on `Z^4` to machine
  precision and its rep-blindness; the robust nonzero rep-splitting `δv` on
  continuous time; the `ξ`-interpolation; the structural no-go (internal symmetry
  is an overall factor; `B_4` relabel needs `ξ = 1`); the dimension-6 `c_4 = -1/3`
  residual and its `a⁻¹ = M_Pl` size.
- **Cited** (comparator/scope only, never a derivation input):
  Collins–Perez–Sudarsky–Urrutia–Vucetich *PRL* 93 (2004) 191301;
  Reisz (lattice power-counting, *CMP* 1988);
  Kostelecký–Russell SME data tables (LV bound comparators).

## Dependencies

- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md) — axiom boundary
  (Lattice/Quantum/Record; no time metric or dynamics supplied by the axioms).
- [SCALE_REFERENCE_PRIMITIVE_NOTE.md](SCALE_REFERENCE_PRIMITIVE_NOTE.md) — the
  single dimensionful primitive; its purity rule (zero dimensionless content) is
  why `ξ = 1` cannot ride on it, and the dimension-6 size estimate uses it.
- [audit/AXIOM_MINIMALITY_POLICY.md](audit/AXIOM_MINIMALITY_POLICY.md) §6 — the
  approval mechanism and the axiom/primitive (non-bounding) vs Tier-A (bounding)
  distinction under which `ξ = 1` is classified as an approvable structural primitive.
- [LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md](LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md)
  — the canonical symmetric-`Z^4` staggered surface; this note closes its
  named-open *interacting* item at one loop.
- [EMERGENT_LORENTZ_RADIATIVE_STABILITY_DISCRETE_TICK_B4_BOUNDED_THEOREM_NOTE_2026-06-08.md](EMERGENT_LORENTZ_RADIATIVE_STABILITY_DISCRETE_TICK_B4_BOUNDED_THEOREM_NOTE_2026-06-08.md)
  — the supplied-`Z^4` `B_4` boundary; this note supplies the cross-surface
  comparison, the structural no-go, and the surface-selection argument it defers.
- [LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06.md](LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06.md)
  — the `δv ~ α/4π` obstruction, here localized to the `ξ → 0` surface.
- [SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md](SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md)
  — the complementary spatial-cubic boundary (`O_h` alone allows `c_t ≠ c_s`).
- [LATTICE_NN_LIGHT_CONE_NOTE.md](LATTICE_NN_LIGHT_CONE_NOTE.md) — one-tick-one-edge
  reachability (retained as finite-graph reachability; the `ξ = 1` combinatorial
  content).
- [EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md](EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md)
  — the `O_h` single-scalar reduction and the attractive difference-mode flow.

**No-promotion statement:** this note does **not** promote, demote, or set the
audit status of the obstruction note, the discrete-tick `B_4` note, the free-SO(4)
note, or any upstream row. The independent audit lane is the only status authority.
