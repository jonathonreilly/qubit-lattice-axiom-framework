# Conserved Stress-Vertex Operator Ward Telescoping in the Cubic GR Channel

**Date:** 2026-06-08
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set, predict, or estimate any audit verdict. Effective status is
pipeline-derived after independent audit and dependency closure.
**Primary runner:**
[`scripts/frontier_universal_gr_cubic_diffeo_ward_operator_telescope.py`](../scripts/frontier_universal_gr_cubic_diffeo_ward_operator_telescope.py)
**Cached log:**
[`logs/runner-cache/frontier_universal_gr_cubic_diffeo_ward_operator_telescope.txt`](../logs/runner-cache/frontier_universal_gr_cubic_diffeo_ward_operator_telescope.txt)

## Statement

For the finite operator models used in the runner, the conserved
velocity-times-momentum stress vertex satisfies exact lattice operator
Ward identities. In both the two-component `Cl(3)` Dirac model and the
staggered Kähler-Dirac model, the longitudinal contraction of the stress vertex
splits into:

```text
propagator-difference term + contact term.
```

The propagator-difference term telescopes inside the tested cubic triangle into
a difference of two-point bubbles. The contact term is `O(k)` and is not
subleading; in the tested staggered kinematics it carries the same leading
power as the telescoped term and contributes one half of the contracted
amplitude.

This is a bounded support theorem for the operator backbone of the cubic GR
Ward channel. It does not prove the full cubic diffeomorphism Ward identity,
does not construct the conserved cubic seagull, and does not establish an
Einstein-Hilbert cubic vertex.

## Runner-Verified Claims

- **T1. Elliptic pin.** The native two-component `iD` determinant is positive
  on the tested Brillouin-zone grid, while the bare Hermitian control is
  sign-indefinite.
- **T2. Two-component gauge Ward identity.**
  `sum_i 2 sin(k_i/2) u_i = D(q+k)-D(q)` holds to roundoff.
- **T3. Two-component stress Ward identity.**
  `sum_i 2 sin(k_i/2) V_ij = 1/2 sbar_j [D(q+k)-D(q)] + 1/2 S_sc u_j`
  holds to roundoff.
- **T4. Staggered gauge Ward identity.** The midpoint staggered velocity
  satisfies the corresponding finite operator identity, and `D D^dagger` has
  the scalar spectrum form checked by the runner.
- **T5. Staggered stress Ward identity.** The staggered stress vertex satisfies
  the same propagator-difference plus contact decomposition.
- **T6. Telescoping diagnostic.** In the tested non-collinear staggered cubic
  triangle, the contracted triangle equals the telescoped two-point
  bubble-difference plus the contact term to roundoff; the bubble-difference is
  nonzero.
- **T7. Contact scaling.** The contact channel is `O(k)`.
- **T8. Non-subleading contact.** The contact and telescoped terms scale with
  the same measured power in the tested sweep; the contact is numerically half
  the contracted amplitude in that setup.

The runner reports `TOTAL: PASS=12 FAIL=0`.

## Boundary

This note establishes only the finite operator identities and the telescoping
diagnostic above. The following remain open:

- the explicit conserved cubic seagull/contact vertex;
- the full quantitative cubic Ward `LHS=RHS` match;
- the continuum `O(a^2)` versus same-order-obstruction question;
- the quartic and higher nonlinear completion;
- an Einstein-Hilbert vertex normalization or `G_Newton` magnitude; and
- any claim of exact finite-lattice diffeomorphism invariance.

The contact term is the important guardrail: because it is not subleading, the
runner does not license dropping it or calling the cubic Ward closed. It shows
where a seagull completion must enter.

## Load-Bearing Inputs And Context

Load-bearing finite operator context:

- [`CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md`](CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md)
  for the native elliptic `iD` carrier context.
- [`LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md`](LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md)
  for the staggered Kähler-Dirac matter-sector context.
- [`UNIVERSAL_GR_STRESS_WARD_TRANSVERSE_SEAGULL_BOUNDED_THEOREM_NOTE_2026-06-08.md`](UNIVERSAL_GR_STRESS_WARD_TRANSVERSE_SEAGULL_BOUNDED_THEOREM_NOTE_2026-06-08.md)
  for the two-point stress-Ward/seagull context that this note does not
  promote.
- [`UNIVERSAL_GR_INDUCED_GRAVITON_W_NATIVE_FINITE_K_BOUNDED_THEOREM_NOTE_2026-06-08.md`](UNIVERSAL_GR_INDUCED_GRAVITON_W_NATIVE_FINITE_K_BOUNDED_THEOREM_NOTE_2026-06-08.md)
  for the finite-momentum induced-graviton context.

Context only:

- [`UNIVERSAL_GR_CUBIC_GRAVITON_SEAGULL_VERTEX_BOUNDED_THEOREM_NOTE_2026-06-08.md`](UNIVERSAL_GR_CUBIC_GRAVITON_SEAGULL_VERTEX_BOUNDED_THEOREM_NOTE_2026-06-08.md)
- [`UNIVERSAL_GR_STAGGERED_TT_PROJECTED_STRESS_TRIANGLE_SUPPORT_BOUNDED_NOTE_2026-06-08.md`](UNIVERSAL_GR_STAGGERED_TT_PROJECTED_STRESS_TRIANGLE_SUPPORT_BOUNDED_NOTE_2026-06-08.md)

## Forbidden-Imports Check

No observed gravitational coupling, fitted value, Einstein-Hilbert
normalization, or external continuum GR vertex is used as a derived input. The
runner performs finite matrix identities and finite Brillouin-zone sums only.

## Validation

Run:

```bash
python3 scripts/frontier_universal_gr_cubic_diffeo_ward_operator_telescope.py
```

Expected: `TOTAL: PASS=12 FAIL=0`.
