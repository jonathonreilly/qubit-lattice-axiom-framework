# The One-Loop Velocity Anisotropy is Computed as One Coefficient δv(ξ): the Naturalness Gap is the Continuous-Time Horn, B₄ Protects ξ=1, and the Lever is Sharpened (Not Closed) to the Record-Tick Bridge

**Date:** 2026-06-08
**Claim type:** no_go (computed coefficient + a sharpened, still-open lever)
**Type:** no_go
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome. The label is a source-side claim-boundary
declaration, not an audit verdict.
**Primary runner:**
[`scripts/frontier_lorentz_velocity_rg_coefficient_computed_2026_06_08.py`](../scripts/frontier_lorentz_velocity_rg_coefficient_computed_2026_06_08.py)
**Cached runner output:**
[`logs/runner-cache/frontier_lorentz_velocity_rg_coefficient_computed_2026_06_08.txt`](../logs/runner-cache/frontier_lorentz_velocity_rg_coefficient_computed_2026_06_08.txt)

---

## Role

This note supplies the **named open input** of the two landed emergent-Lorentz
conditionals —
[`EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md`](EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md)
(#3121) and
[`LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06.md`](LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06.md)
(#3123) — the one-loop velocity-RG coefficient, the spatial-only power-divergent
mixing, and the fixed-point anomalous dimension/suppression sufficiency.

It **computes** the one-loop velocity anisotropy `δv` and shows it is **one
coefficient `δv(ξ)`** of the spacetime anisotropy `ξ = a_s/a_τ` (spatial spacing /
temporal spacing). The decisive structure:

1. the gauge-invariant **on-shell** anisotropy is computed `δv ≈ (g²C₂/16π²)·c_v`
   with a **computed** `c_v ≈ 2` (O(1)) — `δv|_UV(fund) ≈ 1.7×10⁻² ≈ 0.2 α_s`, a
   **finite** `~α_s/4π` Collins regeneration, **nonzero** for every action tried
   (Wilson and staggered);
2. it is **not internally protected**: taste, the remnant `U(1)` chiral symmetry, and
   the per-site `Cl(3,0)` structure are **internal** symmetries that cannot relate a
   temporal to a spatial coefficient (machine-precision representation check); only a
   **spacetime** (`t↔s`-crossing) symmetry can;
3. as a function of `ξ`: `δv = 0` at `ξ = 1` by the **B₄ hypercubic** point group
   (exact, rep-blind, all-orders), and it grows monotonically to the obstruction value
   as `ξ → ∞` (continuous time). **#3121/#3123/#3277 are this one coefficient read at
   the `ξ → ∞` horn**, where the asymptotically-free `γ = (4/3 + N_f/2)α_s ≈ 0.15–0.34`
   is far too small to suppress the residual species `δv(1 GeV) ≈ 10⁻⁸…10⁻⁴` — a robust
   **12–21 order** gap to the tight SME bounds.

**Verdict (lever sharpened, still OPEN — not closed).** The naturalness gap is the
**continuous-time horn** (`ξ → ∞`). The **other horn `ξ = 1` is B₄-protected**
(`δv = 0`, residual LV only the Planck-suppressed dim-6 `(E/M_Pl)²` operator). The
framework **exhibits** a one-tick-one-edge causal structure that **would** sit at
`ξ = 1` **if** the record tick is the physical time coordinate — which the live ledger
classifies `audited_renaming` (a naming bridge, **not** a retained derivation) against a
retained clock-rate no-go. The would-be second condition, form-equality, is **not** a
separate gate: it is supplied by the framework's canonical isotropic staggered action
(modulo a symmetric-staggered realization rider), so the conditions **fold into that one
bridge**. So `ξ = 1` is a **conditional candidate** horn, **not** a custodial mechanism.
**Net:** this upgrades #3121/#3123 from order-of-magnitude to **computed**, **closes the
internal (taste) escape**, **hardens the `v < 1` sign and `O(1)` `c_v`** (the spatial
tadpole reinforces the rainbow; a `c_v → 0` cancellation is strongly disfavored), and
**sharpens the open problem to a single named bridge** — it does not close it. Runner:
**32 PASS / 0 FAIL**.

## The computation

### (0) The dim-6 lattice LV source
On the cubic `Z³` lattice the free dispersion is `E² = k² − (a²/3)Σ_i k_i⁴ + O(a⁴)`
(fermion; boson `a²/12`) — a CPT-even, parity-even **dimension-6** operator
([`EMERGENT_LORENTZ_INVARIANCE_NOTE.md`](EMERGENT_LORENTZ_INVARIANCE_NOTE.md)), the
operator the Collins mechanism feeds into the marginal `δv`.

### (A) The bare off-shell `δv` is artifact-dominated (reproduced)
Naive fermions: temporal `A` log-divergent, spatial `B ≡ 0` by parity → "`0.31`"
spurious; Wilson off-shell `B − A` varies `~5×` over `r ∈ [0.3, 2.0]` — a
discretization artifact (runner Part A).

### (B) The gauge-invariant on-shell pole velocity — computed
At the Minkowski mass shell (`w_ext = i m₀, k → 0`) the gauge-dependent part of the
self-energy (`∝ S⁻¹`) vanishes by the **Nielsen identity**, so the pole velocity is
gauge-invariant. The on-shell `δv = Σ_s − Σ_t`: the `r`-variation collapses from `~5×`
to `<1×` (B1); `|δv| ≈ 0.011–0.016` per `g²C₂` `= O(0.1–0.2)α_s`, `c_v ≈ 2`,
loop- but **not** Planck-suppressed (B2); sign `v < 1` in this Euclidean extraction
(B3) — **not** triangulated (an independent real-time cross-check confirms the
magnitude, nonzero-ness, and no-protection but cannot certify the sign); IR-finite
(B5); gauge (`ξ`) spread `~15%` and an exact-O(1) residual needing the full lattice
vertex + tadpole (B4). The **seagull/tadpole** (B7) is **spatial-only** — continuous
time has no temporal seagull (the covariant derivative is linear in `A₀`), while the
compact spatial links `U_j = exp(ig a A_j)` carry an `A_j²` seagull — so it is a
**definite-sign** `O(g²C₂)` contribution (`δv_tad ≈ −0.014` per `g²C₂`, the standard
anisotropic `u_s < u_t = 1`) that **reinforces** the rainbow (`rainbow ⊕ tadpole ≈
−0.027`, both `v < 1`). It **strongly disfavors** (does not formally rule out — the full
cos-vertex + compact-measure terms are uncomputed) a `c_v → 0` cancellation, and
**corroborates** the `v < 1` sign from a second diagram (Euclidean/mean-field, not a
real-time certification).

### (C) No internal protection — only a spacetime symmetry can
On a **4D-symmetric** Euclidean lattice the temporal and spatial self-energy
coefficients are **equal** to `~10⁻¹⁵` (runner C1) — `δv = 0` by the B₄ hypercubic
symmetry. The kinetic form on `ℝ × Z³` has a **2-dimensional** invariant space
(`c_t ≠ c_s` allowed; the retained
[`SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md`](SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md)),
collapsing to **1-dimensional** (`c_t = c_s` forced) only under a `t↔s`-crossing
**spacetime** element. Taste and the remnant `U(1)` chiral symmetry are **internal**
(they commute with, or are Lorentz-scalars under, the spacetime `γ`-index) and impose
**no** relation between `Σ_t` and `Σ_s` (C2). So **no internal symmetry protects the
velocity** — consistent with the runner's nonzero staggered `δv` and with the
literature (staggered taste protects the *mass*, not the speed of light).

### (D) The anomalous dimension `γ = (4/3 + N_f/2)α_s`
The velocity-RG difference mode of #3121 obeys
`d(v_F − v_b)/dl = −(C_F + C_B N_f)α(v_F − v_b)`; this eigenvalue **is** the
speed-difference operator's anomalous dimension. For SU(3): `C_F = 4/3`, `C_B = T_F =
1/2`; the adjoint `C_A = 3` drops out of the difference channel. So
`c_γ = 4/3 + N_f/2`, `γ ≈ 0.15–0.34`. Asymptotic freedom makes `γ` **weak exactly at**
`M_Pl` (runner Part D).

### (E) RG run + species residual (at the continuous-time horn)
`δv|_IR ≈ δv|_UV·(μ/M_Pl)^γ` with `μ/M_Pl ≈ 8×10⁻²⁰`. With `γ ≈ 0.15–0.34 < γ_crit ≈
0.54` (weakest), the residual species `δv(1 GeV) ≈ 10⁻⁸…10⁻⁴` exceeds the tight
bounds (`10⁻²⁰…10⁻²⁷`) by **12–21 orders** in every factor-2 corner of `(c_v, γ)`;
the weakest (colored, `10⁻¹²`) bound is at the **edge**. The "all species share one
`v*`" steelman fails — the species difference is the observable (runner Part E).

### (F) δv is one coefficient `δv(ξ)`; B₄ protects `ξ = 1`; the lever, sharpened
Interpolating the spacetime anisotropy `ξ = a_s/a_τ`: `|δv|` is **minimal at `ξ = 1`**
and grows **monotonically ~6.6×** toward the continuous-time obstruction value as
`ξ → 5` (runner F1). At `ξ = 1` the marginal `δv = 0` by the **B₄ hypercubic
symmetry** — **exact** (the `t↔s` swap is a finite relabeling of a B₄-invariant
measure, machine zero at every resolution, runner C1/F2), **rep-blind** (the loop is
gauge-rep-independent, so the species difference `(C₂ᵢ − C₂ⱼ)·0 = 0` too), and an
**all-orders** selection rule (the marginal dim-4 anisotropy is not B₄-invariant; power
counting forbids regenerating it from the dim-6 residual). The residual LV at `ξ = 1`
is then only the **B₄-allowed dim-6 4D-cubic operator** `Σ_μ p_μ⁴` — Planck-suppressed
`~(E/M_Pl)²`, harmless.

**Form-equality is not a separate gate — it folds into the bridge (F3/F3b/F5).** B₄
requires the full **isotropic action** (equal kinetic form), not just equal spacing; but
form-equality is **supplied by the framework's canonical isotropic staggered action**, not
a separate free assumption. It is a **finite B₄ group-theory fact** (exact, rep-blind,
all-orders): **any** hypercubic-symmetric action gives `Σ_t = Σ_s` to machine zero —
naive (`r = 0`): `2×10⁻¹⁸`, Wilson `r_t = r_s = 1`: `4×10⁻¹⁹`, `r_t = r_s = 0.5`:
`4×10⁻¹⁸` — and only a **deliberate** `r_t ≠ r_s` breaks it (`3×10⁻⁴`, `~10¹⁵×` larger).
The framework's canonical free-staggered action (the SO(4) note: `Z³ × Z_τ`, isotropic
`η_μ`, `c₄ = −1/3` in all four directions) **is** isotropic, so form-equality holds on it
automatically. **Genuine rider:** this holds for the canonical **symmetric-staggered**
(central-difference) tick, **not** for a generic forward/Wilson transfer step `e^{−Ha_τ}`
(which reintroduces `r_t ≠ r_s`); the symmetric realization is the framework's standing
choice but is **not** forced by Stone-discretization alone. So the two `ξ = 1` conditions
**collapse into one bridge** (plus this realization rider):

- **The record-tick bridge (F4–F5) — the single primary gate.** `ξ = 1` follows from the
  framework's
  one-tick-one-edge causal structure (one record tick = one nearest-neighbor edge, by
  the **no-diagonal clause** of the LATTICE axiom + the retained
  [`LATTICE_NN_LIGHT_CONE_NOTE.md`](LATTICE_NN_LIGHT_CONE_NOTE.md)) only via the
  identification **"record tick = physical time coordinate."** In the live ledger
  [`MIN_TIME_STEP_TIED_TO_THE_LATTICE_EDGE...NOTE_2026-06-08.md`](MIN_TIME_STEP_TIED_TO_THE_LATTICE_EDGE_BY_CAUSAL_LOCALITY_RATIO_DERIVED_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-08.md)
  carries `effective_status = audited_renaming` (a naming/definition bridge, **not** a
  retained derivation; its Planck-time companion is `unaudited`), and there is a
  **retained** clock-rate no-go
  [`POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md`](POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md)
  (`retained_no_go`): records fix the tick/edge **count**, not the **rate**. Also
  `a_τ = a_s/c` is a **definitional unit choice** (`c := v_front`), not a derived
  isotropy; the kinematic front speed `v_front = 1` is **not** the renormalized group
  velocity `v_LR ≈ 0.935` that `δv` measures.
- **The stated native surface.** `MINIMAL_AXIOMS` + #3121 take **continuous** Stone
  time (`ξ → ∞`), the obstruction horn; the Lattice axiom itself disclaims a "causal
  cone." So the framework's mainline arguably points at `ξ → ∞`, not `ξ = 1`.

## Verdict

**Computed coefficient; lever sharpened to one named bridge; not closed.** The one-loop
velocity anisotropy is one computed coefficient `δv(ξ)`: **nonzero and not internally
(taste) protected for `ξ > 1`**, **zero by B₄ for `ξ = 1`**, and growing to the
**Collins-type obstruction** (computed `δv|_UV ≈ 0.2 α_s`, `γ ≈ 0.15–0.34 ≪ γ_crit`,
12–21 orders over the tight SME bounds) as `ξ → ∞`. This **locates** the #3123/#3277
obstruction as the continuous-time horn and exhibits a B₄-protected horn at `ξ = 1`.
**The continuous-time (`ξ → ∞`) horn is the framework's *derived* surface:** the
single-clock codimension-1 theorem reconstructs continuous Stone time `U(t)=exp(−itH)`
on the spatial `Z³` slice (its Step-1 physical output), and the retained
`SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY` leaves `a_τ` removable — so this obstruction
surface is *not* a mere `a_τ→0` artifact, it is the derived-time output; the
complementary `ξ = 1` reading (`δv = 0`) rests on a separate non-retained finite-`a_τ`
symmetric-tick realization premise (see the companion boundary note). Both horns of the
one coefficient `δv(ξ)` remain live.
The framework's one-tick-one-edge causal structure **would** sit at `ξ = 1` — a **live,
attractive candidate** — but reaching it requires the record-tick = physical-time
bridge (currently `audited_renaming`, against a retained clock-rate no-go). Form-equality
is **not** a second independent gate: it is supplied by the framework's canonical isotropic
staggered action (modulo the symmetric-staggered realization rider), so the conditions fold
into that one bridge. `ξ = 1` is therefore a **conditional candidate horn, not a custodial
mechanism, and not a closure.** Net: #3121/#3123 are upgraded to **computed**, the
**internal (taste) escape is closed**, the `v < 1` sign and `O(1)` `c_v` are hardened by
the tadpole, and the open problem is **sharpened to a single, named, currently-non-retained
bridge**.

## Honest scope (the named residuals)

- **Which horn is physical — the dominant residual.** `ξ = 1` (protected) vs `ξ → ∞`
  (obstruction) is genuinely unsettled and reduces to the record-tick = physical-time
  bridge, which the audit lane classifies as `audited_renaming` and which must clear a
  retained clock-rate no-go. The framework's stated native surface (continuous time)
  is the obstruction horn. This is a framework-definition/audit question, not a
  calculation; it is **open**.
- **Form-equality (folds into the bridge, not a separate gate).** B₄ needs the full
  isotropic action, but this is **supplied by the framework's canonical isotropic
  staggered action** (a finite group-theory fact: any hypercubic-symmetric action gives
  `Σ_t = Σ_s` to machine zero, only deliberate `r_t ≠ r_s` breaks it, F3/F3b). The
  genuine rider: it holds for the canonical symmetric-staggered (central-difference) tick,
  not a generic forward/Wilson transfer step — the framework's standing choice, not forced
  by Stone alone.
- **`v_front` vs `v_LR`.** `δv` lives on the renormalized group velocity (`~0.935`),
  not the kinematic causal front (`=1`); `a_τ = a_s/c` is a unit choice, not a derived
  isotropy. "All species share `c`" is the emergent-Lorentz attractor question (#3121),
  not delivered by the front speed.
- **Exact O(1) coefficient `c_v` (~factor-2).** Rainbow + the spatial tadpole are
  definite-sign and reinforce (B7), so a `c_v → 0` cancellation is **strongly disfavored**
  — but the full Wilson/clover cos-vertex, the compact-measure term, and continuum
  matching are uncomputed, so it is **not formally ruled out**. Does not move the
  order-of-magnitude obstruction at `ξ → ∞`.
- **Sign (`v < 1`).** Corroborated by **two diagrams** (the Euclidean rainbow and the
  mean-field tadpole, B7), but neither is a real-time certification — so not fully
  triangulated. The verdict does not depend on it.
- **Species accounting.** SU(3)-only; color-singlet leptons (`C₂ = 0`) get `δv = 0`
  from gluons; the EM/weak sectors carry separate couplings/runnings — an O(1)
  cross-gauge-group simplification.

## What this note does NOT claim

- It does **not** claim a closure, a solution, or a custodial mechanism; it does
  **not** say the framework "protects Lorentz invariance," "lands on," or "selects"
  `ξ = 1`. `ξ = 1` is a **conditional candidate** horn (conditional on the
  `audited_renaming` record-tick bridge **and** form-equality).
- It does **not** claim the framework is inconsistent — only that the velocity
  naturalness reduces to the named binary.
- It does **not** independently certify the `v < 1` sign, nor a 3-sig-fig `δv`.
- It does **not** contradict #3121 (the attractive log flow is real; #3121's residual
  D — the power-divergent `δc_s` — is exactly the computed `δv` at `ξ → ∞`) or #3277
  (this is the same coefficient read across `ξ`).
- **No** new axiom, primitive, repo vocabulary, or class tag; **no** PDG-fit / `g_bare`
  derivation input (`β = 6 → g² = 1` is the framework's own convention; LV bounds are
  comparators).
- It does **not** set or change any audit status.

## Reprove-and-cite ledger

- **Reproven here** (runner, from Haar/lattice primitives): the dim-6 dispersion
  `a²/3`, `a²/12`; the naive/Wilson off-shell artifacts; the gauge-invariant on-shell
  `δv = Σ_s − Σ_t` (r-stability, magnitude, gauge spread, IR-finiteness, staggered
  non-protection); the spatial **seagull/tadpole** (`δv_tad ≈ −0.014` per `g²C₂`,
  definite-sign, no temporal seagull); the 4D-symmetric B₄ control (`δv = 0` to `10⁻¹⁵`),
  its rep-blindness, and the **form-equality** test (any isotropic action → `Σ_t = Σ_s`
  to machine zero; only deliberate `r_t ≠ r_s` reintroduces `δv ~ 10⁻⁴`); `C_F = 4/3`,
  `T_F = 1/2`, `γ = (4/3 + N_f/2)α_s`; the `γ_crit` table and species gap; the
  `δv(ξ)` interpolation (minimal at `ξ = 1`, monotone to `ξ → ∞`).
- **Cited** (comparator/scope only, never a derivation input):
  Collins–Perez–Sudarsky–Urrutia–Vucetich *PRL* **93** (2004) 191301;
  Capitani *Phys. Rept.* **382** (2003) 113 (hep-lat/0211036); Groote–Shigemitsu
  *PRD* **62** (2000) 014508 (hep-lat/0001021, anisotropic speed-of-light renorm at the
  same on-shell point); Giuliani–Mastropietro–Porta *Ann. Phys.* **327** (2012) 461
  (attractive emergent-Lorentz flow restored only with a protecting Ward identity);
  Bednik–Pujolàs–Sibiryakov *JHEP* **1311** (2013) 064; Nielsen (gauge-parameter
  independence of the pole); Reisz (lattice power-counting, *CMP* 1988); Lepage–Mackenzie
  *PRD* **48** (1993) 2250 and Karsch / Klassen (anisotropic-lattice tadpole improvement,
  `u_s < u_t = 1`, comparators for B7); Kostelecký–Russell SME data tables (LV
  comparator bounds).

## Audit dependency repair links

This section records explicit dependency links for the audit citation graph. It does
not promote this note or change any audited claim scope. The cited ledger statuses are
recorded verbatim as of 2026-06-08 (the audit lane is the only status authority).

- [LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06.md](LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06.md)
- [EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md](EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md)
- [SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md](SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md)
- [EMERGENT_LORENTZ_INVARIANCE_NOTE.md](EMERGENT_LORENTZ_INVARIANCE_NOTE.md)
- [LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md](LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md)
- [MIN_TIME_STEP_TIED_TO_THE_LATTICE_EDGE_BY_CAUSAL_LOCALITY_RATIO_DERIVED_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-08.md](MIN_TIME_STEP_TIED_TO_THE_LATTICE_EDGE_BY_CAUSAL_LOCALITY_RATIO_DERIVED_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-08.md) (`audited_renaming`)
- [POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md](POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md) (`retained_no_go`)
- [LATTICE_NN_LIGHT_CONE_NOTE.md](LATTICE_NN_LIGHT_CONE_NOTE.md)
- [DIRAC_LORENTZ_DIAGNOSTIC_BOUNDARIES_FROM_REJECTED_REPAIRS_NOTE_2026-06-07.md](DIRAC_LORENTZ_DIAGNOSTIC_BOUNDARIES_FROM_REJECTED_REPAIRS_NOTE_2026-06-07.md)
- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)

### Source-note boundary

**Hypothesis set:** (1) the three axioms + the approved scale primitive `a⁻¹ = M_Pl`;
(2) the spacetime anisotropy `ξ = a_s/a_τ` as the control parameter, with the
continuous-time (`ξ → ∞`) and the symmetric (`ξ = 1`) surfaces both named; (3) the
`β = 6` SU(3) bare coupling (`g² = 1`); (4) standard one-loop lattice perturbation
theory (rainbow self-energy, Wilson/staggered doubler control, the Nielsen on-shell
pole prescription, the coupled velocity RG of #3121); (5) SME/UHECR/GRB/clock bounds
as comparators. The result is a one-loop, rainbow-level computation; the named
residuals are the record-tick bridge (`audited_renaming`), form-equality, the exact
O(1) coefficient, and the sign.

**Forbidden-imports check:** no new axiom, primitive, repo vocabulary, or class tag;
only standard terms (self-energy, pole velocity, Nielsen identity, Wilson/staggered
fermion, taste/hypercubic symmetry, anomalous dimension, RG flow, Reisz power-counting,
spacetime anisotropy). No fitted/PDG/lattice-MC value consumed as a derivation input.

**No-promotion statement:** this note does **not** promote, demote, or set the audit
status of #3121, #3123, the emergent-Lorentz notes, the free-staggered SO(4) note, the
minimum-time-step / clock-rate notes, the diagnostic note, or any upstream row. The
independent audit lane is the only status authority.
