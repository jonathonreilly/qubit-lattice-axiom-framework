# Induced Composite-Link Trajectory: Local Covariance, Exact Increment Law, and a Non-Autonomy Exhibit

**Date:** 2026-06-08
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Scope:** conditional existence, covariance, and exact increment law for the
matter-induced composite-link trajectory, containing an exact non-autonomy
counterexample and a complementary minimal-occupancy rigidity identity.
**Script:** `scripts/frontier_induced_composite_link_trajectory_non_autonomy_2026_06_08.py`
**Cache:** `logs/runner-cache/frontier_induced_composite_link_trajectory_non_autonomy_2026_06_08.txt`
**Status:** source proposal. All statements are finite-dimensional exact algebra
checked by the runner (`PASS=36 FAIL=0`). Authority role: source proposal; the
audit lane sets status.

## The named residual this addresses

The interacting-gauge convergence note
[`ST1_ST2_SAME_WALL_GAUGE_DYNAMICS_RESIDUAL_CONVERGENCE_NARROW_THEOREM_NOTE_2026-06-08.md`](ST1_ST2_SAME_WALL_GAUGE_DYNAMICS_RESIDUAL_CONVERGENCE_NARROW_THEOREM_NOTE_2026-06-08.md)
reduces the foundation's undelivered input to one item: a continuous-time
gauge-link / color-einselection dynamics, in particular a gauge-link
**generator** with arrow and rate. Record alone cannot supply that generator;
see
[`RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06.md`](RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06.md)
and
[`RECORD_MARKOV_GENERATOR_EMBEDDABILITY_BOUNDARY_2026-06-06.md`](RECORD_MARKOV_GENERATOR_EMBEDDABILITY_BOUNDARY_2026-06-06.md).

The composite-link construction
([`COLOR_LINK_INDEX_ROUTING_VIA_CROSS_SITE_MATTER_BILINEAR_UNITARIZATION_BOUNDED_THEOREM_NOTE_2026-06-08`](COLOR_LINK_INDEX_ROUTING_VIA_CROSS_SITE_MATTER_BILINEAR_UNITARIZATION_BOUNDED_THEOREM_NOTE_2026-06-08.md))
gives the link a matter-native carrier: `U_eff = polar(M(x,y))` with
`M(x,y)_ij = Σ_α ψ_α(x)_i ψ_α(y)_j*` over occupied matter modes. The sharpest
unexplored question on that route: **does the matter dynamics INDUCE the
gauge-link dynamics through this construction** — is the undelivered link
generator already determined by the matter evolution? This note answers the
question exactly, in a small exact model, with mixed outcome: the induced
trajectory exists and is locally gauge-covariant with a closed-form increment,
but it is **not autonomous in the link variable** — exhibited exactly.

## Setting and conditionality (load-bearing, named)

Every statement below is conditional on all three of:

1. **The supplied `C³` color carrier** (`MR_color` residual;
   [`COLOR_SU3_MATTER_REALIZATION_RESIDUAL_MAP_2026-06-05`](COLOR_SU3_MATTER_REALIZATION_RESIDUAL_MAP_2026-06-05.md),
   registry/audit status external to this note). Nothing here derives color
   from the axioms.
2. **THIS matter Hamiltonian.** The model evolves the one-body density under
   uniform quadratic nearest-neighbor hopping on a 4-site cycle (and a 2-site
   edge for the exhibit): (i) `H_free = κ A ⊗ I₃` (color-diagonal), (ii)
   `H_cov` with a frozen generic `SU(3)` link background `V_xy` on each edge,
   (iii) a staggered-sign variant of (ii). The "connection" reading of the
   covariant hopping is the subject of
   `matter_gauge_minimal_coupling_fiber_frame_forces_connection_narrow_theorem_note_2026-06-08`,
   [`MATTER_GAUGE_MINIMAL_COUPLING_FIBER_FRAME_FORCES_CONNECTION_NARROW_THEOREM_NOTE_2026-06-08.md`](MATTER_GAUGE_MINIMAL_COUPLING_FIBER_FRAME_FORCES_CONNECTION_NARROW_THEOREM_NOTE_2026-06-08.md).
   Here the covariant hopping is simply a named model Hamiltonian, and no
   connection reading is consumed. This note does **not** claim the induced
   evolution is the framework's realized dynamics; it is induced by the named
   Hamiltonian in each case.
3. **The ≥3-occupied-mode / full-rank precondition** inherited from the
   composite-link construction: `U_eff(x,y)` is defined only where `M(x,y)`
   has rank 3.

The matter states are one-body densities `0 ≤ ρ ≤ 1` (the fermionic-Gaussian
reading of the construction note: `M(x,y)` is the cross-site one-body density
block `⟨a†_{y,j} a_{x,i}⟩`, with mode occupations folded into the c-number
amplitudes). Evolution is exact: `ρ(t) = e^{-iHt} ρ(0) e^{iHt}` by `eigh`.

## Verdict (four exact findings)

### 1. The induced trajectory exists; degeneracy is exactly characterized

Along exact trajectories of a generic 4-occupied-mode state on the 4-cycle
(`t ∈ [0,8]`, all 4 edges, both `H_free` and `H_cov`), `M(x,y;t)` stays rank 3
(min `σ₃ = 3.7×10⁻³` free, `8.1×10⁻⁴` cov over the sampled grid) and `U_eff(t)`
stays exactly unitary. The degeneracy locus is exactly characterized by
`rank M(x,y) ≤ min(rank G(x), rank G(y))` with `G(x)` the 3×K site amplitude
block (`M = G(x)G(y)†`): the link variable fails exactly where some endpoint's
occupied color support drops below 3. An engineered state with 2-dimensional
color support at one site has `σ₃(M) = 0` at `t = 0`, and the hopping evolution
restores rank 3 by `t = 0.7` — rank-deficiency is a real but non-invariant
boundary, not a persistent obstruction along generic trajectories.

### 2. Covariance: exact, with teeth

- `H_free`: the **entire induced trajectory** is globally `SU(3)`-equivariant,
  `U_eff^g(t) = g U_eff(t) g†`, to machine precision (`10⁻¹⁴`).
- `H_cov` with **frozen** background and a global rotation of the state only:
  equivariance **fails** at order 1 (violation `1.64` — teeth; the background
  breaks the global symmetry, as it must).
- `H_cov` under the **joint** local transformation (state by `⊕_x g_x`,
  background by `V_xy → g_x V_xy g_y†`): the induced trajectory is exactly
  locally covariant, `U_eff(x,y;t) → g_x U_eff(x,y;t) g_y†`, to `10⁻¹⁴`,
  including the staggered-sign variant. The induced link evolution is a
  gauge-covariant map (state, background) → link trajectory.

### 3. The exact increment law — closed form, but with non-link inputs

Writing `Ṁ ≡ dM(x,y)/dt`, the induced increments are exactly:

```
  Ṁ(x,y) = −i[ V_xy M(y,y) − M(x,x) V_xy ]                (local-density term)
           −i[ Σ_{z~x, z≠y} V_xz M(z,y) − Σ_{z~y, z≠x} M(x,z) V_zy ]   (chord term)

  U̇_eff = U_eff Ω,   Ω the unique solution of the Sylvester equation
  Ω Q + Q Ω = U_eff† Ṁ − Ṁ† U_eff,   Q = (M†M)^{1/2}
```

both verified exactly (decomposition to `10⁻¹⁶`; the polar increment against
4th-order finite differences of the exact trajectory to `10⁻¹⁰`, both `H`'s).
`Ω` is anti-Hermitian; its `su(3)` projection is identical on all three `Z₃`
det-branches (`10⁻¹⁴`), so the `SU(3)`-direction increment is center-ambiguity-free.

Structure read off the law (exact statements, not asymptotics):

- The bilinear's drift is **linear in the other matter bilinears** — the local
  color densities `M(x,x), M(y,y)` and the **chord** bilinears `M(z,y), M(x,z)`
  (site pairs that are not edges) — with frozen-link-valued coefficients. It has
  staple **geometry** (paths through neighbors) but it is matter-bilinear-linear,
  **not** a function of the link variables: the closed linear object is the full
  one-body matrix `ρ(t)`, not the edge set.
- The polar increment additionally consumes `Q` — the positive part that the
  unitarization discards.
- A Wilson-staple-force direction diagnostic (cos-angle between the `su(3)`
  increment and the frozen-background staple force along the trajectory) shows
  no stable alignment (mean `−0.07`, range `[−0.48, +0.27]`); reported as a
  diagnostic only, no claim either way.

### 4. Non-autonomy: an exact counterexample (the obstruction), plus a rigidity

**Exhibit.** On a single edge, two one-body densities `ρ_A ≠ ρ_B` (both
physical: eigenvalues in `(0,1]`; both carrying rank-3 bilinears) constructed
with `M_A = U₀ Q_A`, `M_B = U₀ Q_B`, `Q_B = Q_A + Δ`, `Δ ⪰ 0`, sharing **all**
of:

- the same composite link `U_eff(0) = U₀` (dev `10⁻¹³`),
- the same local color densities `M(x,x)`, `M(y,y)` (exact),
- the same bilinear velocity `Ṁ(0)` (exact — the single-edge `Ṁ` depends only
  on the matched local densities),

yet `dU_eff/dt` differs at order 1: `‖Ω_A − Ω_B‖_F = 3.99` (`H_cov`) and
`3.34` (`H_free`), with `‖Q_A − Q_B‖_F = 0.021`, both increments confirmed
against finite differences of the two exact evolutions (`10⁻¹⁰`), and the two
induced trajectories separate to `‖U_A − U_B‖_F = 1.49` by `t = 0.25`. The
increment difference is not perturbatively small in `ΔQ`: the Sylvester
solution has sensitivity `1/(q_i + q_j)`, so small occupied directions amplify
the hidden-data dependence. Non-autonomy holds for the **free color-diagonal**
hopping as well — it is intrinsic to the polar compression, not an artifact of
the background.

So: `U̇_eff` is **not** a function of `U_eff` (the link is not a closed
subsystem under the induced route); it is not even a function of
`(U_eff, M(x,x), M(y,y), Ṁ)` — the discarded positive part `Q` is load-bearing
in the increment. Equivalently, the two compression layers fail separately:
(L1) the `M`-level drift couples to chord bilinears and local densities beyond
the edge set; (L2) the `U`-level increment needs `Q` even when `Ṁ` is supplied.

**Complementary rigidity (where the hidden-`Q` channel closes).** At minimal
occupancy — exactly 3 occupied modes with invertible 3×3 endpoint amplitude
blocks — the Schur identity `M M(y,y)^{-1} M† = M(x,x)` holds exactly, which
forces `Q = (U₀† M(x,x) U₀) # M(y,y)` (the matrix geometric mean; verified to
`10⁻¹³`): the positive part is **determined** by `(U_eff, local densities)`,
and the L2 freedom is absent. With ≥4 occupied modes the Schur identity breaks
generically (`min dev = 0.76` over draws) and the hidden-`Q` freedom opens. The
hidden-`Q` non-autonomy channel therefore lives **strictly above minimal
occupancy**; at minimal occupancy the residual obstruction is L1
(chord/local-density dependence) alone.

## What the runner verifies (`PASS=36 FAIL=0`)

Part 1 (9, incl. 2 setup checks): Hermiticity/physicality setup; rank-3 along
trajectories (both `H`'s); exact unitarity of `U_eff`; the rank bound on 20
random draws; the engineered degeneracy and its evolution-restoration.
Part 2 (4): global equivariance exact for `H_free`; frozen-background global
violation (teeth); joint local covariance exact for `H_cov` and the
staggered-sign variant.
Part 3 (8): exact local+chord decomposition; `Ṁ` vs finite differences; the
Sylvester polar increment vs finite differences (both `H`'s); a known-answer
test of the Sylvester machinery (explicit family with `U̇(0) = X U₀` known a
priori — independent of finite differences); anti-Hermiticity;
`Z₃`-branch-freeness of the `su(3)` increment.
Part 4 (15): exhibit physicality/rank/preconditions; exact `U_eff(0)`,
local-density, and `Ṁ(0)` agreement; order-1 increment difference (both `H`'s)
with finite-difference confirmation; trajectory separation; the K=3 Schur
identity and geometric-mean rigidity; the K=4 break.
Plus 3 INFO diagnostics (restored rank value, local/chord magnitudes,
staple-overlap statistics).

## Honest boundaries — what this does NOT establish

- **No discharge of any gate.** The local color-frame redundancy residual, the
  continuous link-generator residual, the mixing-regime residual, and the
  blocking-isometry selection are all untouched. This note neither supplies the
  framework's link dynamics nor
  shows one cannot exist — it shows the **matter-induced candidate on this
  route is not autonomous in the link variable**.
- **Not the framework's realized dynamics.** Everything is conditional on the
  supplied `C³` carrier and the named model Hamiltonians (uniform quadratic
  hopping; free, frozen-`SU(3)`-background, staggered-sign variants). No claim
  is made that these are the framework's realized matter dynamics; the
  staggered-Dirac realization lane is a separate gate with its own tiers.
- **No Markovianity / long-time statements.** Trajectory statements are exact
  identities at the checked configurations and sampled times of a small exact
  model; nothing is claimed about mixing, stationarity, step statistics, or any
  CLT input; the mixing-regime question is shaped, not advanced.
- **Scope of the non-autonomy.** The exhibit defeats autonomy of `U_eff` under
  the polar compression **for this construction and this Hamiltonian class**
  (quadratic hopping; one-body closure). Named routes that this exhibit does
  NOT foreclose: enlarging the compression to carry `(U_eff, Q)` (equivalently
  `M`) or occupancy data alongside the link; the exact minimal-occupancy sector
  (where the rigidity removes the hidden-`Q` freedom and the residual question
  is L1 only); coarse-grained or averaged regimes where the hidden data could
  become slaved (not attempted here); non-quadratic or record-coupled matter
  dynamics.
- **Quantitative values** (`3.99`, `1.64`, overlap statistics, …) are
  seed-specific magnitudes of a generic-draw model; the exact-zero and
  machine-precision identities are the load-bearing content.

## Relation to the wall

The same-wall convergence note named one undelivered input: the continuous-time
gauge-link dynamics. This note asks whether the derived matter sector already
induces it through the composite link. The answer sharpens the link-generator
residual rather than delivering it:

- **Positive (conditional):** the induced link trajectory exists generically,
  is exactly locally gauge-covariant, and obeys a closed-form increment law
  (Sylvester/polar) — the matter dynamics does induce *a* link evolution with
  identifiable structure.
- **Obstruction (exact):** that evolution is not a dynamics **of the link**:
  its generator requires matter data the link compression discards (chord
  bilinears, local densities, and — above minimal occupancy — the positive
  part `Q`). Any closed link-level generator on this route must therefore
  either carry extra slow variables alongside `U_eff`, restrict to the
  minimal-occupancy sector, or arise at a different compression level
  (averaging/blocking), where the mixing-regime question lives. This converts
  the missing-generator residual into a named structural requirement with exact
  teeth at this model's level.

## Negative-Boundary Discipline

The non-autonomy exhibit is a bounded route constraint, not a no-go against all
gauge dynamics.

- Alternative routes left open: carry `(U_eff,Q)` or `M` rather than `U_eff`
  alone; restrict to the minimal-occupancy sector; seek coarse-grained slaving
  of hidden data; use non-quadratic or record-coupled matter dynamics; use a
  different compression or connection-level variable.
- Wall independence: the chord/local-density dependence and the hidden-`Q`
  dependence are distinct. The K=3 rigidity closes the hidden-`Q` channel only;
  it does not close the chord/local-density channel.
- Hidden-wall scan: the supplied `C³` carrier, named Hamiltonian class, and
  full-rank precondition are explicit assumptions, not derived inputs.
- Residual matching: the result targets only the link-generator residual named
  by the same-wall convergence note. It does not target local color-frame
  redundancy, mixing/ergodicity, blocking-isometry selection, or the connection
  reading of the covariant hopping model.
- Rhetoric resolution: the tested negative is finite-dimensional, edge-level,
  one-body, and polar-compression-specific. No lattice-wide, long-time, or
  universal dynamics obstruction is claimed.
- Partial-closure scan: no new axiom or primitive is required by this result;
  the live import-retirement path is to enlarge or change the compression data
  and then prove a retained generator theorem.
- Steelman: a hostile reviewer can reasonably argue that a different slow
  variable, a minimal-occupancy sector, or a coarse-grained regime may slave the
  hidden data and produce an autonomous effective link law. This note leaves
  those routes open.
- Cross-cycle echo: prior overbroad wall claims in this repo have been repaired
  by convention stripping or reframe. This note avoids that pattern by naming
  the open convention/reframe routes instead of declaring structural closure.

## Cross-references

- The composite-link construction (consumed):
  [`COLOR_LINK_INDEX_ROUTING_VIA_CROSS_SITE_MATTER_BILINEAR_UNITARIZATION_BOUNDED_THEOREM_NOTE_2026-06-08`](COLOR_LINK_INDEX_ROUTING_VIA_CROSS_SITE_MATTER_BILINEAR_UNITARIZATION_BOUNDED_THEOREM_NOTE_2026-06-08.md)
- The supplied color carrier (conditionality inherited):
  [`COLOR_SU3_MATTER_REALIZATION_RESIDUAL_MAP_2026-06-05`](COLOR_SU3_MATTER_REALIZATION_RESIDUAL_MAP_2026-06-05.md)
- The dynamics wall (the residual being shaped):
  [`ST1_ST2_SAME_WALL_GAUGE_DYNAMICS_RESIDUAL_CONVERGENCE_NARROW_THEOREM_NOTE_2026-06-08.md`](ST1_ST2_SAME_WALL_GAUGE_DYNAMICS_RESIDUAL_CONVERGENCE_NARROW_THEOREM_NOTE_2026-06-08.md)
- Record-side boundaries (respected):
  [`RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06.md`](RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06.md),
  [`RECORD_MARKOV_GENERATOR_EMBEDDABILITY_BOUNDARY_2026-06-06.md`](RECORD_MARKOV_GENERATOR_EMBEDDABILITY_BOUNDARY_2026-06-06.md)
- The covariant-hopping connection reading (NOT consumed; named for scope):
  [`MATTER_GAUGE_MINIMAL_COUPLING_FIBER_FRAME_FORCES_CONNECTION_NARROW_THEOREM_NOTE_2026-06-08.md`](MATTER_GAUGE_MINIMAL_COUPLING_FIBER_FRAME_FORCES_CONNECTION_NARROW_THEOREM_NOTE_2026-06-08.md)
- Color algebra dependency: [`GRAPH_FIRST_SU3_INTEGRATION_NOTE`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md)

Consult the audit ledger for current dependency status. This source note does
not set or update any dependency status.

- Standard math cited for method only: polar decomposition and its derivative
  (Sylvester equation), matrix geometric mean / Riccati uniqueness, Schur
  complement positivity.
