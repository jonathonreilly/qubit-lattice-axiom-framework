# Broad Gravity Bundle: Per-Signature Bounded IF-Chains

**Date:** 2026-04-13. Admitted-input scope repair: 2026-05-28.
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.

---

## Binding Claim

This note is a bounded conditional chain for the broad weak-field GR-signature
bundle. It does **not** derive the GR signatures from the Cl(3)-on-`Z^3`
baseline alone, and it does not claim a zero-free-parameter physical-gravity
closure. In particular it does **not** derive `L^{-1} = G_0` from the baseline:
that closure identity is an **admitted input**, stipulated, not derived (see
"Admitted Inputs" below).

The binding claim is the implication:

> If the framework supplies the named inputs
>
> 1. the weak-field action/response is read through `S = L(1 - phi)`;
> 2. the gravitational source density is the Born/mass-density readout
>    `rho = |psi|^2`;
> 3. the field operator and propagator Green function are related by the
>    stipulated weak-field closure `L^{-1} = G_0`;
>
> then, on top of the retained weak-field Poisson/Newton core, the weak
> equivalence principle and gravitational time dilation follow as corollaries
> of the action `S = kL(1 - phi)`, and the conformal metric, geodesic equation,
> and GR light-bending factor of 2 follow conditionally on the additional
> standard lattice-to-continuum identification.

The conclusion is therefore **bounded support conditional on the named
inputs**, not an unconditional derivation of those inputs. This mirrors the
bounded IF-chain framing of
[`GRAVITY_CLEAN_DERIVATION_NOTE.md`](GRAVITY_CLEAN_DERIVATION_NOTE.md), whose
conclusion is likewise an implication over the same named inputs.

---

## Admitted Inputs

The following are **stipulated inputs**, made explicit here. They are
**NOT derived** in this note, and they are **NOT** supplied by the one-hop
retained-bounded dependencies cited below. The audit verdict on this row was
that the note had promoted `L^{-1} = G_0` as if derived from the
Cl(3)-on-`Z^3` baseline, while
[`GRAVITY_FULL_SELF_CONSISTENCY_NOTE.md`](GRAVITY_FULL_SELF_CONSISTENCY_NOTE.md)
treats it as stipulated, and the one-hop retained-bounded dependencies do not
supply the promoted premise. This subsection records the inputs honestly.

| Admitted input | Role | Status in this note |
|----------------|------|---------------------|
| `L^{-1} = G_0` | weak-field self-consistency closure (propagator sources the field it propagates in) | **stipulated input, not derived** here or from the Cl(3)-on-`Z^3` baseline |
| `rho = \|psi\|^2` | gravitational mass-source readout (Born density) | **stipulated input**, not derived here as a physical source law |
| `S = L(1 - phi)` | weak-field test-mass action/response | **stipulated input**, not derived here as a full test-mass action theorem |

The Cl(3)-on-`Z^3` baseline and the lattice Green-function asymptotic
`G(r) ~ 1/(4 pi r)` are external/baseline mathematical background, used in
parallel with the framework calculation, not new framework axioms.

---

## What The Step-by-Step Chain Establishes (Conditional On The Admitted Inputs)

The chain below records what follows **given** the admitted inputs. The status
tags name what is an algebraic identity, what is a definition, and what is
admitted. They do **not** assert that the admitted inputs are derived from the
baseline.

### Step 1: H = -Delta (KS construction)

**Status:** algebraic identity (baseline).

Cl(3) on `Z^3` gives the staggered Hamiltonian whose square is the negative
graph Laplacian. This is established in
[`GRAVITY_CLEAN_DERIVATION_NOTE.md`](GRAVITY_CLEAN_DERIVATION_NOTE.md) Step 1
and verified to machine precision.

### Step 2: G_0 = H^{-1} (definition of propagator)

**Status:** definition.

The propagator's Green's function is the inverse of the Hamiltonian. Not a
physical claim; it is what "propagator" means on this graph.

### Step 3: Self-consistency L^{-1} = G_0 gives L = H = -Delta

**Status:** ADMITTED INPUT (closure identity), not derived from the baseline.

`L^{-1} = G_0` is the weak-field closure identity. **Given** this input, the
unique solution is `L = G_0^{-1} = H`, which gives the Poisson equation
(consistent with the retained Poisson/Newton core). The closure is stipulated:
[`GRAVITY_FULL_SELF_CONSISTENCY_NOTE.md`](GRAVITY_FULL_SELF_CONSISTENCY_NOTE.md)
records `L^{-1} = G_0` as a stipulated closure identity, not a theorem of the
Cl(3)-on-`Z^3` baseline. Deriving it is queued as an open follow-on (see "Open
Follow-Ons").

### Step 4: phi = GM/r (Green's function of L)

**Status:** lattice potential-theory theorem (external mathematics).

The Green's function of `-Delta` on `Z^3` converges to `1/(4 pi r)` at large
distances. This is a theorem of pure mathematics. Established in
[`GRAVITY_CLEAN_DERIVATION_NOTE.md`](GRAVITY_CLEAN_DERIVATION_NOTE.md) Step 5.

### Step 5: The propagator action S = kL(1 - phi)

**Status:** follows from Steps 1-4 **given the admitted weak-field response
input** `S = L(1 - phi)`, plus the eikonal/WKB limit.

The propagator on `Z^3` accumulates phase along paths. In the free theory, the
phase along a path of length `L` is `S = kL`. **Given** the weak-field response
input, when a background field `phi` is present the propagator's hopping
amplitude at site `x` is modified:

    amplitude per step at x = exp(ik(1 - phi(x)))

The supporting derivation chain (conditional on the admitted input and the
eikonal limit) is:

1. The field `phi` modifies the effective potential at each site.
2. The Hamiltonian becomes `H(phi) = H + phi` (the field is a potential).
3. The propagator in the modified Hamiltonian has Green's function
   `G(phi) = (H + phi)^{-1}`.
4. In the eikonal (WKB) limit, `G(phi)` is approximated by the path sum with
   phase `exp(ikL(1 - phi))` along each path.

The detailed first-order chain is:
- `H psi = E psi` is the eigenvalue problem.
- `H + phi` perturbs the eigenvalues to `E(1 - phi)` at leading order
  (first-order perturbation theory on a slowly varying field).
- The Green's function phase is `exp(ikL)` with `k` related to `E`.
- The perturbation shifts `k_eff = k(1 - phi)` per step.
- The total phase along a path of length `L` is
  `S = k * sum(1 - phi(x_i)) = kL(1 - phi_avg)`.
- For a smooth field, `phi_avg -> phi` at the path location, giving
  `S = kL(1 - phi)`.

**Limits consumed:** the eikonal/WKB limit (wavelength << field scale) and
first-order perturbation theory (`phi << 1`, weak field). These are standard
semiclassical limits, not imported GR. The weak-field response form
`S = L(1 - phi)` is an **admitted input** (see "Admitted Inputs"), not derived
here.

---

## Status Of S = kL(1 - phi)

The action form `S = kL(1 - phi)` follows under the chain:

```
Cl(3) on Z^3                              [BASELINE]
    |
    v
H = -Delta                                [algebraic identity, KS]
    |
    v
G_0 = H^{-1}                              [DEFINITION]
    |
    v
L^{-1} = G_0 => L = -Delta => Poisson     [ADMITTED INPUT closure]
    |
    v
phi = GM/r                                [external lattice theorem]
    |
    v
H(phi) = H + phi                          [potential coupling]
    |
    v
S = kL(1 - phi)                           [given admitted S=L(1-phi) input + eikonal limit]
```

The chain consumes one **admitted closure input** (Step 3), one **admitted
weak-field response input** (Step 5 form), and one semiclassical limit. The
admitted inputs are NOT derived from the baseline. The GR content that follows
from `S = L(1 - phi)` inherits the **conditional** status of `S = L(1 - phi)`:
it is bounded support **given the admitted inputs**, not an unconditional
derivation.

This is the honest correction to the earlier framing that called the chain
"derived" and "promoted" WEP and time dilation: those signatures are
corollaries **conditional on the admitted inputs**, not unconditional
derivations from the Cl(3)-on-`Z^3` baseline.

---

## Per-Signature Bounded IF-Chains

### Signature 1: Weak Equivalence Principle (WEP)

**Conditional chain:**

`S = kL(1 - phi)` holds given the admitted inputs (Steps 1-5). The deflection
of a test particle is determined by the stationary-phase condition:

    delta S / delta(path) = 0

The deflection angle `theta` depends on the impact parameter `b`:

    theta = dS/db = d/db [kL(1 - phi(b))]

Since `S = k * F(path, phi)`, the stationary-phase trajectory is where
`delta F = 0` (`k` cancels). Therefore the trajectory -- and hence the
deflection -- is independent of `k`. All particles, regardless of wavenumber,
follow the same trajectory. This IS the weak equivalence principle.

**Why the k-independence is non-trivial (given the inputs):** it would fail if
the action had a k-dependent potential coupling, if `phi` depended on `k`, or
if the Hamiltonian perturbation were nonlinear in `phi`. None occur given the
admitted inputs: the field `phi` is the universal Poisson field, the potential
coupling `H + phi` is linear, and the eikonal phase is `k *` (geometric
factor).

**Inputs consumed:** the admitted inputs (`S = L(1-phi)`, `rho = |psi|^2`,
`L^{-1} = G_0`); the eikonal limit (consumed in Step 5).

**Status:** **bounded support conditional on the admitted inputs.** This is a
corollary of the conditional action chain, not an unconditional derivation from
the baseline.

---

### Signature 2: Gravitational Time Dilation

**Conditional chain:**

A "clock" is any oscillatory mode with frequency `omega`. On the lattice, a
mode with wavenumber `k` at site `x` has local phase accumulation rate:

    d(phase)/dt = k * (1 - phi(x))

The ratio of clock rates between two sites:

    tau_1/tau_2 = (1 - phi(x_1)) / (1 - phi(x_2))

For the Poisson field `phi = GM/(4 pi r)`:

    tau(r)/tau(infinity) = 1 - GM/(4 pi r)

which matches `g_00^{1/2} = (1 - 2GM/rc^2)^{1/2}` to first order with
`phi = GM/(4 pi r)` in lattice units.

**Derived vs admitted:** GIVEN any action `S = L(1-f)`, the time-dilation
ratio is an algebraic identity. The non-trivial part is that the field `f` is
the Poisson field `phi = GM/(4 pi r)` from the retained core, so the `1/r`
profile is a prediction, not an input. But the action form `S = L(1-f)` itself
is an **admitted input** here, not derived. The phase identity is tautological;
the `r`-profile is supplied by the retained Poisson/Newton chain.

**Distinguishing test:** running the same time-dilation test with (a) the
Poisson field, (b) a random field, (c) a `1/r^2` field all give ratio `= 1.0`
for the phase identity, but only the Poisson field gives the correct
`r`-dependence.

**Inputs consumed:** the admitted inputs; the eikonal limit; identification of
phase rate with clock rate.

**Status:** **bounded support conditional on the admitted inputs.** The
tautological phase identity holds unconditionally; the matching `1/r` profile
is supplied by the retained Poisson/Newton chain; the action form is admitted.

---

### Signature 3: Geodesic Equation

**Conditional chain:**

In the eikonal limit, the path sum is dominated by the stationary-phase path:

    delta integral (1 - phi(x)) ds = 0

This is the geodesic equation for the conformal metric
`g_ij = (1 - phi)^2 delta_ij`, with Christoffel symbols

    Gamma^i_jk = -(delta^i_j partial_k phi + delta^i_k partial_j phi
                   - delta_jk partial^i phi) / (1 - phi)

In the Newtonian limit the geodesic equation reduces to
`d^2 x^i / dt^2 = -partial_i phi`, which is Newton's equation.

**Additional condition:** the continuum limit (coarse-graining the lattice path
cost to a smooth Riemannian metric) is an additional step beyond the bare
lattice, on top of the admitted inputs.

**Numerical support:** Christoffel match to `O(10^{-7})` on `N=31`; Newtonian
limit matches `-grad(phi)`; `1/b` deflection scaling confirmed
(`beta = 1.05`, `R^2 = 0.998`).

**Status:** **bounded support conditional on the admitted inputs and the
standard continuum limit.**

---

### Signature 4: Light Bending (Factor of 2)

**Conditional chain:**

The temporal contribution gives the Newtonian deflection
`theta_1 = 2GM/(4 pi b)`. The spatial metric contribution
`g_ij = (1 - phi)^2 delta_ij`, if it holds, gives total deflection
`theta_total = 2 theta_1 = 4GM/(4 pi b)`.

The conformal spatial metric follows from the isotropy of the action (the
scalar `phi` couples the same in all directions), the effective distance per
step `d_eff = a(1 - phi(x))`, and the continuum limit.

**Additional conditions:** the continuum limit (as in Signature 3) plus the
null-geodesic identification (mapping high-k lattice modes to null rays).

**Numerical support:** deflection ratio (full propagator / Newtonian)
`= 1.985 +/- 0.012` at large impact parameters, consistent with factor 2.

**Status:** **bounded support conditional on the admitted inputs, the continuum
limit, and the null-geodesic identification.**

---

### Signature 5: Conformal Metric g_ij = (1 - phi)^2 delta_ij

**Conditional chain:**

The action `S = kL(1 - phi)` modifies effective distances by `(1 - phi)`,
isotropically; in the continuum limit this defines the Riemannian metric
`g_ij = (1 - phi)^2 delta_ij`, with temporal `g_00 = -(1 - phi)^2`, giving the
conformal Minkowski form
`ds^2 = -(1 - phi)^2 dt^2 + (1 - phi)^2 dx^2`.

**Additional condition:** the continuum limit (lattice path cost -> smooth
Riemannian metric).

**Numerical support:** anisotropy `< 0.4%`; matches weak-field Schwarzschild in
isotropic coordinates.

**Status:** **bounded support conditional on the admitted inputs and the
standard continuum limit.**

---

## Summary Table

| Signature | Conditional chain | Conditions beyond admitted inputs | Status |
|-----------|-------------------|-----------------------------------|--------|
| WEP | `S = kL(1-phi)` given admitted inputs; `k` cancels in `delta S = 0` | eikonal (already in chain) | bounded support conditional on admitted inputs |
| Time dilation | phase rate `= k(1-phi)`; `phi = GM/4 pi r` from retained core | eikonal; clock = oscillatory mode | bounded support conditional on admitted inputs |
| Geodesic equation | stationary phase gives conformal geodesics | + continuum limit | bounded support conditional on admitted inputs + continuum limit |
| Light bending (x2) | spatial metric from isotropy; null-ray integration | + continuum limit + null-geodesic identification | bounded support conditional on admitted inputs + those conditions |
| Conformal metric | action isotropy + scalar coupling -> conformal | + continuum limit | bounded support conditional on admitted inputs + continuum limit |

---

## What Is Actually Established (Conditional)

**Given the admitted inputs**, two signatures follow as corollaries of the
conditional action chain:

1. **WEP:** the deflection of any test particle is independent of its
   wavenumber `k`. The k-independence requires the specific structure that the
   admitted inputs supply (universal Poisson field, linear potential coupling,
   no k-dependent terms). It is bounded support conditional on the admitted
   inputs, not an unconditional derivation from the baseline.

2. **Time dilation:** the phase accumulation rate in a gravitational well is
   `k(1 - phi(r))` with `phi(r) = GM/(4 pi r)` from the retained Poisson/Newton
   chain. The phase identity is tautological; the `1/r` profile is supplied by
   the retained core; the action form is admitted.

**Conditional on the admitted inputs plus the standard continuum limit
(and null-geodesic identification for light bending):** geodesic equation,
light bending (factor 2), conformal metric.

---

## Assumptions

### Baseline
- Cl(3) on `Z^3`.

### Admitted inputs (stipulated, NOT derived here; see "Admitted Inputs")
- `L^{-1} = G_0` (weak-field self-consistency closure).
- `rho = |psi|^2` (gravitational mass-source readout).
- `S = L(1 - phi)` (weak-field test-mass response).

### Limits consumed in the conditional action chain
- Eikonal / WKB limit (wavelength << gravitational field scale).
- First-order perturbation theory (`phi << 1`, weak field).

### Additional conditions for the conditional signatures
- Continuum limit (lattice path cost -> smooth Riemannian metric).
- Null-geodesic identification (light bending only).

---

## Open Follow-Ons

To promote beyond the bounded conditional chain, future work would need
retained bridge theorems for the admitted inputs and conditions:

1. **Derive `L^{-1} = G_0` from the Cl(3)-on-`Z^3` baseline** rather than
   stipulating it as a weak-field closure identity. This is the load-bearing
   admitted input flagged by the audit and is the primary open follow-on.
2. Derive the physical gravitational source map `rho = |psi|^2`.
3. Derive the weak-field test-mass response `S = L(1 - phi)`.
4. Discharge the continuum-limit and null-geodesic identifications with
   explicit lattice-to-continuum bridge theorems.

### Other open items (strong field / dynamics)

1. **Strong-field regime:** `phi ~ 1` breaks the weak-field expansion. Horizons,
   frame dragging, post-Newtonian corrections not covered.
2. **Full propagator WEP:** the eikonal WEP is exact; whether dispersive
   `O(k^2 a^2)` corrections break WEP for finite-wavelength particles on the
   lattice is open (numerics inconclusive at `N=31`).
3. **Post-Newtonian corrections:** `O(phi^2)` terms in the action would give 1PN
   corrections; not yet computed from the lattice path sum.
4. **Dynamic sector:** gravitational waves require promoting Poisson to
   d'Alembertian (Lorentz-covariant wave equation); a separate derivation lane.

---

## Commands Run

```bash
python3 scripts/frontier_broad_gravity.py
```

## Citations

This note's bounded IF-chain consumes the named one-hop authorities. The audit
verdict was that these one-hop retained-bounded dependencies do **not** supply
the promoted premise `L^{-1} = G_0`; that premise is recorded as an admitted
input above.

- [gravity_clean_derivation_note](GRAVITY_CLEAN_DERIVATION_NOTE.md) —
  this note's Step 1 ("Cl(3) on `Z^3` uniquely gives the staggered Hamiltonian
  whose square is the negative graph Laplacian") and Step 5 ("the propagator
  action `S = kL(1 - phi)`") consume gravity_clean's Steps 1 and 5 directly.
  gravity_clean is the upstream chain composer; this note is downstream.
  Direction in citation graph: broad_gravity -> gravity_clean
  (consumer -> producer). The reverse edge in gravity_clean's Citations section
  was removed in 2026-05-05 as a misattribution that created a length-2 cycle.
- [gravity_full_self_consistency_note](GRAVITY_FULL_SELF_CONSISTENCY_NOTE.md)
  — supplies the broader self-consistency surface and records `L^{-1} = G_0` as
  a stipulated closure identity, not a theorem derived from the
  Cl(3)-on-`Z^3` baseline. Correct upstream.
