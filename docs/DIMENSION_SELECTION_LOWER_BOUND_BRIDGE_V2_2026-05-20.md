# Dimension-Selection Lower-Bound Bridge V2 (Runner-Faithful)

**Date:** 2026-05-20
**Type:** bounded_theorem
**Status authority:** independent audit lane only.
**Primary runner:** [`scripts/frontier_dimension_selection.py`](../scripts/frontier_dimension_selection.py)
**Retained finite-k sign bridge:** [`DIMENSION_SELECTION_FINITE_K_CENTROID_SIGN_BRIDGE_NOTE_2026-05-25.md`](DIMENSION_SELECTION_FINITE_K_CENTROID_SIGN_BRIDGE_NOTE_2026-05-25.md)
**Finite-k bridge runner:** `scripts/frontier_dimension_selection_finite_k_centroid_sign_bridge.py`
**Radial-profile proof runner:** `scripts/dimension_selection_poisson_profile_native_proof_2026_06_09.py`
**Scope:** bounded finite-k / analytic sign bridge for the existing runner; not a
promotion of `DIMENSION_SELECTION_NOTE.md` or of the wider D=3 chain.
**Closes (proposed):** the named gap on `DIMENSION_SELECTION_NOTE.md`
flagged by the review-loop disposition in
`D3_RETENTION_CLOSURE_PLAN_2026-05-20.md`:
*"the analytic sign argument treats the two-dimensional Green function
and the force-sign convention inconsistently with the existing
DIMENSION_SELECTION_NOTE runner."* This V2 supplies the runner-faithful
analytic bridge.

**Supersedes (in part):** the rejected
`DIMENSION_SELECTION_LOWER_BOUND_BRIDGE_NOTE_2026-05-20.md`
(submitted in PR #1603, not landed) which argued from `F = ∇φ`
classical force, inconsistent with the runner's action-based
propagator observable.

## 2026-05-29 Audit Repair (finite-k bridge now load-bearing)

The 2026-05-28 audit verdict was `audited_conditional`:

> *"The derivative sign calculation closes algebraically once the eikonal bending rule is admitted. The restricted packet does not derive or independently certify the needed bridge from the finite-k discrete propagator and normalized centroid o"*

with repair: *"missing_bridge_theorem: provide a discrete-to-eikonal bridge theorem, or an independent finite-k sign proof, showing the runner's normalized centroid shift has the claimed sign for the stated potential family."*.

That repair now exists as
[`DIMENSION_SELECTION_FINITE_K_CENTROID_SIGN_BRIDGE_NOTE_2026-05-25.md`](DIMENSION_SELECTION_FINITE_K_CENTROID_SIGN_BRIDGE_NOTE_2026-05-25.md),
which the audit ledger marks `retained_bounded`. It differentiates the actual
finite-k, finite-lattice, layer-normalized runner update at the runner
constants (`k = 6.0`, `L_x = 40`, `L_y = 60`, source at `y_mid`, mass offset
`+7`) and replays the parent finite probe at `M = 0.005`.

- **Load-bearing (in scope):** The retained finite-k bridge computes the
  exact first derivative of the runner's normalized detector centroid at
  `M = 0` and directly verifies the parent finite probe. Its sign table is
  negative for `d = 1, 2` and positive for `d = 3, 4, 5`.
- **Consistency check (in scope, but not the finite-k closure):** Elementary
  calculus on the runner's stated profile `f_d(r)` explains why the sign
  transition is aligned with `df_d/dr`: `f_1` and `f_2` increase with `r`,
  while `f_d(r) = r^{-(d-2)}` decreases for `d ≥ 3`.
- **Removed as load-bearing:** The standard WKB/eikonal
  discrete-to-ray bridge is no longer admitted or required for this packet's
  finite-runner sign claim. Any eikonal language below is interpretive
  context only.

No new axiom is introduced. This revision only connects an already retained
bounded finite-k bridge to the older lower-bound packet and corrects the
source-drift prose identified by audit. It is a re-audit candidate, not a
ledger retag.

## Claim

For `scripts/frontier_dimension_selection.py`, which computes
attractiveness via the centroid shift of a 2D wave-mechanical
propagator with action `S = L · (1 − φ)` through a d-dimensional
analytic potential `φ`, the runner's finite-k normalized
centroid-shift observable

```text
raw_delta = c_y(with mass) − c_y(no mass)
```

is **positive (attractive)** for `d = 3, 4, 5` and **negative
(repulsive)** for `d = 1, 2`, for the runner's fixed finite-k
geometry and analytic potential family. The transition is certified
by the retained finite-k tangent recursion and parent finite-probe
replay; the derivative-sign calculus on `f_d(r)` is explanatory
support, not an admitted WKB bridge.

This is the bounded finite-runner sign bridge that the lower-bound runner was
missing. The runner's numerical observation at `d ∈ {1, 2, 3, 4, 5}`
is now backed by an audited retained finite-runner sign bridge for
the exact normalized centroid observable. The derivation admits the
choice to use the runner's analytic potential family as the finite
test surface, but the profile identities themselves are proved below
on that surface rather than imported from a textbook. It does not
derive the whole dimension-selection theorem.

## Setup

The runner uses a 2D wave-mechanical propagator that steps a wave
packet `ψ(x, y)` from `x = 0` to `x = L_x - 1` through a
d-dependent potential `φ(x, y)` constructed by

```text
φ(r) = −M · f_d(r),   r = √((x − x_mass)² + (y − y_mass)²)               (1)
```

with the analytic d-dependent profile

```text
f_d(r) = r                  for d = 1                                    (2a)
f_d(r) = log(r)             for d = 2                                    (2b)
f_d(r) = 1 / r^(d−2)        for d ≥ 3                                   (2c)
```

(from `scripts/frontier_dimension_selection.py` line 367–372). Note
that the absolute sign of `φ` is not load-bearing here. In particular,
for `d = 2`, `φ = −M log(r)` is positive when `0 < r < 1` and negative
when `r > 1`; the runner's regularization permits `r = 0.5`. What
matters for the sign discussion is the spatial *shape* of `f_d`:
`f_d` **grows** with `r` for `d = 1, 2` and **decays** with `r` for
`d ≥ 3`.

## Step 0 — Runner-native radial Green-profile proof

The runner's profile family is not taken as a load-bearing textbook
import. The companion certificate
[`scripts/dimension_selection_poisson_profile_native_proof_2026_06_09.py`](../scripts/dimension_selection_poisson_profile_native_proof_2026_06_09.py)
proves the exact identities used by this finite-runner packet.

For a radial profile `f(r)` in dimension `d`, the away-from-source
radial operator is

```text
Delta_d f = f''(r) + ((d - 1)/r) f'(r),  r > 0.
```

The profile family used by the runner satisfies:

```text
d = 1:  f_1(r) = r,          Delta_1 f_1 = 0,  r^(d-1) f_1'(r) = 1
d = 2:  f_2(r) = log(r),     Delta_2 f_2 = 0,  r^(d-1) f_2'(r) = 1
d >= 3: f_d(r) = r^(2-d),    Delta_d f_d = 0,  r^(d-1) f_d'(r) = 2-d
```

Thus each profile is harmonic away from the source and has
radius-independent shell flux on the runner's radial coordinate. The
derivative sign is also exact:

```text
f_1'(r) > 0,  f_2'(r) > 0,  f_d'(r) < 0 for d >= 3.
```

That sign is the profile-orientation input used in Step 2, while the
retained finite-k bridge remains the load-bearing certificate for the
actual normalized centroid sign. Maradudin or standard mechanics texts
may be cited as parallel provenance for the same radial Poisson
profiles, but the textbook references are parallel provenance, not
load-bearing inputs for this packet.

The propagator step (line 386–397) accumulates a phase

```text
phase = k · S = k · L · (1 − φ_avg)                                      (3)
```

per step of length `L` (with `L = √(1 + dy²)` for the local
lattice-step direction `dy ∈ {−1, 0, +1}`). `φ_avg` is the average
of `φ` at the two endpoints of the step.

The centroid `c_y` of the post-propagation `|ψ(x = L_x − 1, y)|²`
is then measured, and `raw_delta = c_y(mass present) − c_y(no mass)`
is the observable. Mass is placed at `y = y_mid + 7` (positive
offset above the propagation axis). Thus `raw_delta > 0` means
the centroid is deflected **toward** the mass position — attractive.

## Step 1 — Retained finite-k sign authority

The retained finite-k bridge differentiates the actual runner update:

```text
A_x(M)[y+dy, y]
  = exp(i k L_dy [1 + M f_avg]) / L_dy,
psi_{x+1}(M) = A_x(M) psi_x(M) / ||A_x(M) psi_x(M)||.
```

At `M = 0`, it computes the exact normalized tangent recursion for
`d psi_x / dM` and then evaluates

```text
dC/dM |_{M=0}
  = sum_y y * 2 Re(conj(psi_{L_x-1}(0,y)) dot psi_{L_x-1}(y)).
```

The audited retained bridge reports:

| d | `dC/dM at M=0` | finite-probe `raw_delta` at `M=0.005` | sign |
|---|---:|---:|---|
| 1 | `-6178.064177806486` | `-3.8672175352803855` | away |
| 2 | `-693.5367985302938` | `-2.151826031186392` | away |
| 3 | `+137.43355955069325` | `+0.7271976977843124` | toward |
| 4 | `+119.62276629484603` | `+0.6596476488010232` | toward |
| 5 | `+145.12754503252833` | `+0.8307846758016488` | toward |

This closes the auditor's named alternative repair route for the
finite runner: an independent finite-k sign proof showing the
runner's normalized centroid shift has the claimed sign for
`d ∈ {1, 2, 3, 4, 5}`.

## Step 2 — Why the sign transition matches `df_d/dr`

The mass is at `y_mass = y_mid + 7`. The source-emitted packet
centered at `y_mid` propagates in `+x`. Along the propagation, the
packet encounters regions of varying `f_d(r)` depending on its
transverse position `y`.

**Case `d ≥ 3`:** `f_d(r) = 1 / r^(d−2)` is a *decreasing* function
of `r`. Larger `f_d` occurs at *smaller* `r`, i.e., closer to the
mass at `(x_mid, y_mid + 7)`. This is the profile orientation
corresponding to a centroid shift in the `+y` direction, toward
`y_mass = y_mid + 7`. **The finite-k bridge verifies
`raw_delta > 0`: attractive.**

**Case `d = 2`:** `f_d(r) = log(r)` is a *strictly increasing*
function of `r` (for `r > 0`). Larger `f_d` occurs at *larger* `r`,
i.e., farther from the mass. This is the profile orientation
corresponding to a centroid shift in the `−y` direction, away from
`y_mass = y_mid + 7`. **The finite-k bridge verifies
`raw_delta < 0`: repulsive.**

**Case `d = 1`:** `f_d(r) = r` is also strictly increasing in `r`.
Same profile orientation as `d = 2`, away from mass. **The finite-k
bridge verifies `raw_delta < 0`: repulsive.**

The runner's finite-k sign result is therefore consistent with the
following profile criterion:

```text
attractive (raw_delta > 0)  iff  d f_d / d r < 0  for r > 0              (5)
```

By inspection of (2a–c):

```text
d f_1 / d r = 1            > 0           (d = 1: repulsive)              (6a)
d f_2 / d r = 1 / r        > 0  for r > 0  (d = 2: repulsive)           (6b)
d f_d / d r = −(d−2)/r^(d−1)  < 0  for d ≥ 3  (d ≥ 3: attractive)       (6c)
```

For the finite runner dimensions under audit, **`raw_delta > 0` iff
`d ≥ 3`** — exactly the runner's observation.

## Step 3 — Runner-faithful sign convention

The previous (rejected) bridge note argued from `F = − ∇φ` classical
force. That is the **mechanical-particle force**, not the
runner's wave-packet observable. The repaired V2 packet no longer
uses a classical force law or an admitted eikonal bridge as the
load-bearing argument. It uses the finite-k normalized centroid
derivative from the retained bridge and keeps the `df_d/dr` calculus
only as a transparent explanation of the sign transition.

## Step 4 — Comparison to runner output

The runner observes (per `DIMENSION_SELECTION_NOTE.md`):

| d | Attractive? | β (mass exp.) | α (distance exp.) | I_3 |
|---|---|---|---|---|
| 1 | **NO** | 0.18 | 0.42 | < 1e-10 |
| 2 | **NO** | 0.27 | -0.17 | < 1e-10 |
| 3 | YES | 1.01 | 1.32 | < 1e-10 |
| 4 | YES | 1.05 | 3.30 | < 1e-10 |
| 5 | YES | 1.03 | 5.01 | < 1e-10 |

The sign-transition between `d = 2` and `d = 3` matches both the
retained finite-k bridge and the analytic profile criterion in Step 2.
The `d = 2` logarithmic case is sign-consistent because
`f_2 = log(r)` is increasing in `r`, even though `φ = −M log(r)`
changes absolute sign at `r = 1`.

The distance exponents `α` and mass exponents `β` in this table are
included only to identify the parent runner surface. They are not
derived by this bridge, and the displayed `α` values should not be
read as precision matches to the ideal Green-function falloff.

## What this closes

- The named gap on `DIMENSION_SELECTION_NOTE.md` flagged in the
  review-loop disposition: *"the analytic sign argument treats
  the two-dimensional Green function and the force-sign convention
  inconsistently with the existing runner."* This V2 now uses the
  retained finite-k centroid-sign bridge for the exact runner
  observable; both the `d = 2` log case and the `d = 1` linear case
  are handled without importing WKB/eikonal sign preservation.
- The audit's later missing-bridge repair request on this row:
  *"provide a discrete-to-eikonal bridge theorem, or an independent
  finite-k sign proof."* The retained finite-k bridge supplies the
  second option for the stated finite runner geometry.

## What this does not close

- **The upper-bound dependency** on `DIMENSION_SELECTION_NOTE.md` is
  not addressed here. That is
  separately supported by the two upper-bound notes already landed
  (`BERTRAND_STABLE_ORBIT_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md`
  and `COULOMB_STABILITY_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md`).
- **The mass-exponent `β` and distance-exponent `α` predictions** of
  the runner are consistent with but not derived by this bridge.
  Those would require additional bridges from the d-dim Green's
  function to the runner's regularized observable.
- **The wider D=3 chain** (anomaly-forces-time, Lorentz, single-clock route,
  single-clock uniqueness). All remain conditional per
  `D3_RETENTION_CLOSURE_PLAN_2026-05-20.md`.

## Admitted inputs

1. **Runner's exact action form `S = L · (1 − φ)`** and propagator
   step `psi_new += exp(i k S) / L · psi_old` — from
   `scripts/frontier_dimension_selection.py` lines 386–397; admitted
   as the runner's specification.
2. **Runner's d-dependent potential form (2a–c)** — from
   `scripts/frontier_dimension_selection.py` lines 367–372;
   admitted only as the finite runner's chosen analytic test surface.
   The radial profile identities for (2a–c) are proved in this packet
   by the runner-native radial Green-profile certificate above; textbook
   references are parallel provenance, not load-bearing inputs.
3. **Retained finite-k centroid-sign bridge** —
   [`DIMENSION_SELECTION_FINITE_K_CENTROID_SIGN_BRIDGE_NOTE_2026-05-25.md`](DIMENSION_SELECTION_FINITE_K_CENTROID_SIGN_BRIDGE_NOTE_2026-05-25.md),
   audited as `retained_bounded`, supplies the exact normalized
   tangent recursion and parent finite-probe replay.
4. **Sign of `df_d/dr`** — elementary calculus on (2a–c). No
   admission.

## Risk classification

This is a `bounded_theorem` re-audit candidate. The narrow
contribution is that the older runner-faithful lower-bound packet now
depends on a retained finite-k derivative bridge instead of an
admitted WKB/eikonal bridge. The result remains bounded to the
current runner geometry, constants, potential family, and finite
dimensions `d ∈ {1, 2, 3, 4, 5}`. It does not promote full spatial
dimension selection.

## Citation-graph note

**Upstream framework dependencies** (load-bearing markdown links):

- [`DIMENSION_SELECTION_FINITE_K_CENTROID_SIGN_BRIDGE_NOTE_2026-05-25.md`](DIMENSION_SELECTION_FINITE_K_CENTROID_SIGN_BRIDGE_NOTE_2026-05-25.md) (retained_bounded) — supplies the finite-k normalized centroid-sign bridge for the exact runner geometry and parent finite probe.
- [`DIMENSIONAL_GRAVITY_TABLE.md`](DIMENSIONAL_GRAVITY_TABLE.md) (retained_bounded) — supplies companion d-dim potential context for the `d ≥ 3` case.
- [`scripts/dimension_selection_poisson_profile_native_proof_2026_06_09.py`](../scripts/dimension_selection_poisson_profile_native_proof_2026_06_09.py) — proves the runner-native radial profile identities for `d = 1, 2, 3, 4, 5` directly on the analytic family used here.

**Runner/context references** (plain text, not load-bearing graph deps):

- `scripts/frontier_dimension_selection.py` — supplies the finite runner specification and the observed force-sign / β / α data this bridge connects to the finite-k sign authority.
- `scripts/frontier_dimension_selection_finite_k_centroid_sign_bridge.py` — support runner for the retained finite-k derivative certificate.
- `DIMENSION_SELECTION_NOTE.md` — existing note using the runner; this bridge does not promote that note.
- `D3_RETENTION_CLOSURE_PLAN_2026-05-20.md` — tracking note that identified this gap.

**Parallel references only** (not load-bearing graph deps):

- Standard d-dimensional Poisson Green's function discussions
  (Maradudin et al. 1971 for lattice `d = 3`, standard mechanics texts
  for the continuum radial profiles).

**Plain-text pointer references** (NOT load-bearing deps):

- `DIMENSION_SELECTION_LOWER_BOUND_BRIDGE_NOTE_2026-05-20.md` (rejected V1) — superseded by this V2 with the runner-faithful finite-k sign authority
- `BERTRAND_STABLE_ORBIT_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md`, `COULOMB_STABILITY_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md` — provide the upper-bound half; not load-bearing for this lower-bound bridge

## What this file is not

- Not a derivation that this analytic potential family is the unique
  possible dimension-selection test surface; it remains the parent
  runner's chosen finite test family.
- Not a derivation of the eikonal limit itself; WKB/eikonal reasoning is no longer load-bearing for this packet.
- Not a derivation of the runner's β / α exponents (separate bridges; out of scope).
- Not a numerical-prediction change.
- Not a unilateral retagging. The bounded-theorem candidacy depends on independent audit acceptance that the retained finite-k bridge closes this row's previous missing-bridge blocker.
