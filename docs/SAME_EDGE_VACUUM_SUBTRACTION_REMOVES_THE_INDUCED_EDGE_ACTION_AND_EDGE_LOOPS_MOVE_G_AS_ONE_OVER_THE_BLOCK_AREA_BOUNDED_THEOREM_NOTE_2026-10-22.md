---
claim_id: same_edge_vacuum_subtraction_removes_the_induced_edge_action_and_edge_loops_move_g_as_one_over_the_block_area_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the response law's vacuum standard (edges respond only to departures from the vacuum of the same edges): subtracting, at each joint configuration, the site shares of the vacuum odds on the same edges leaves zero matter phase for vacuum odds at every edge configuration, so the sea's induced edge action is removed whole (exact Fock toy: 2 x 5 torus, 5 fermions, 252 configurations, staggered mass 0.5; raw d2E0/dh2 = -8.947, a fixed flat reference leaves -1.780, the same-edge reference 0). With an added particle the response is the departure's own (2D staggered toy, N = 8 to 24). For time-dependent edges the sea's response depends on q^2 - omega^2 (1D Wilson-Dirac sea, coefficient ratio extrapolating to 0.9991), so an instantaneous reference leaves the omega^2 (kinetic) half, a non-covariant term, while an adiabatic reference carried along the same edge history removes every order below pair threshold (remainders 5.8e-3, 1.5e-4, 5.4e-6, 2.2e-7 after orders 0 to 6). The edges' own zero-point loops are not subtracted: the one-loop term (1/2) ln det is independent of the overall stiffness while the bare hinge sum scales as b_e^2, so dG/G = C W4/b_e^2 with the 4D lattice tadpole W4 = 0.154933. Estimates use a supplied envelope |C| <= 10 and an induced fraction f = 0.232 taken from a companion computation. Supplied model, finite diagnostic: toy seas, a scalar vertex, the heat-kernel normalisation, the envelope for C and the block sizes."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/same_edge_vacuum_subtraction_removes_the_induced_edge_action_and_edge_loops_move_g_as_one_over_the_block_area_2026_10_22.py
---

# Same-edge vacuum subtraction removes the induced edge action, and edge loops move G as one over the block area

Claim type: bounded_theorem.
Primary runner: `scripts/same_edge_vacuum_subtraction_removes_the_induced_edge_action_and_edge_loops_move_g_as_one_over_the_block_area_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its response law (CL-3 in the three-law numbering) is the vacuum-standard principle: edges and links respond only to departures from the vacuum of the same edges, in the vacuum's own units. A matter sea on curved edges induces an edge action (Sakharov's induced gravity), which could move 1/G away from the hinge-sum value. This note asks how much of the induced term the vacuum standard removes, which reference vacuum is needed to keep the result covariant, and how large the edges' own unsubtracted loops are. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here.

## Statement

A. The sea under the vacuum standard.

1. If at each joint configuration the vacuum standard subtracts the site shares of the vacuum odds on the same edges, then for vacuum odds the total matter phase is zero at every configuration and for every edge configuration. The sea's induced edge action (cosmological, Einstein-Hilbert, R^2 and nonlocal parts alike) is removed whole, not only its constant. Subtracting a fixed (flat) vacuum instead leaves minus the sea's static susceptibility. This is a structural statement; the runner's same-edge comparison is identical by construction, and the computed content is the raw and flat-reference curvatures.
2. With one added particle the response is the departure's own: the second derivative of E1 - E0 in the edge modulation stays O(1) while the vacuum's raw second derivative grows as the area N^2. No species-count x volume x curvature term survives, only the matter's own stress.
3. For time-dependent edges the sea's response is a function of q^2 - omega^2 (the ratio of the omega^2 and -q^2 coefficients tends to 1 in the continuum limit). Subtracting only the instantaneous vacuum removes the static half and leaves the omega^2 half: a non-covariant induced kinetic term as large as the removed gradient term.
4. An adiabatic reference (the vacuum carried along the same edge history, expanded in omega/gap) removes every order: the remainder after order 2n falls geometrically, by a factor at most (omega/2m)^2 per order. Real pair creation above threshold is not removed; it is a physical departure.

B. The edges' own zero-point loops (not subtracted).

5. The 4D lattice tadpole is W4 = int_BZ d^4k/(2 pi)^4 / k_hat^2 = int_0^inf (e^{-2t} I0(2t))^4 dt = 0.154933; a field on blocks of b cells has G(0) = W4/(b L)^2.
6. The one-loop term (1/2) ln det of the edges' quadratic form does not depend on its overall stiffness, while the bare hinge sum scales as the stiffness, b_e^2 for block edges of b_e cells with the same G. The edges' own loop correction to 1/G is therefore O(1) per block against b_e^2: dG/G = C W4/b_e^2, with C a lattice sum not computed here.

## Derivation

Item 1 diagonalises the exact fixed-number Hamiltonian (bond hops -1/length, staggered on-site mass) on the 252 configurations at random edge lengths 1 + 0.3 u and at a cosine length modulation h, and takes second differences in h (step 1e-3) of the raw ground energy and of the ground energy minus the flat vacuum's expectation. Item 2 does the same for single-particle levels of a 2D staggered torus. Item 3 computes the scalar (sigma_z) vertex polarisation of the half-filled 1D Wilson-Dirac sea (60000 momenta) and the ratio of its d/d omega^2 and -d/d q^2 coefficients at four masses, with a linear extrapolation in m. Item 4 subtracts the omega^2 expansion of the same polarisation at omega = m/2 order by order. Item 5 integrates the Bessel form with scipy. Item 6 takes the second variation of (1/2) ln det of K times a weighted 10 x 10 lattice Laplacian plus mass at K = 1 and K = 100.

## Finite checks

Exact or closed-form checks (the runner asserts each):
- Same-edge share difference 0 (by construction); raw d2E0/dh2 = -8.947; flat-reference -1.780.
- Adiabatic remainders after orders 0, 2, 4, 6: 5.8e-03, 1.5e-04, 5.4e-06, 2.2e-07 (each step below 0.3 of the last; overall below 1e-3).
- W4 = 0.154933 (asserted to 2e-5).
- d2/dh2 of (1/2) ln det: -18.889054 at K = 1 and -18.889053 at K = 100.

Finite diagnostics (supplied model, finite diagnostic):
- Added particle (2D staggered torus): N = 8, 12, 16, 24 give raw/N^2 = -0.8416, -0.8183, -0.8099, -0.8038 and departure -0.0000, +0.0000, -0.0000, +0.0000.
- Covariance ratio (omega^2 against -q^2 coefficient): 0.8265, 0.9070, 0.9518, 0.9755 at m = 0.1, 0.05, 0.025, 0.0125; linear extrapolation 0.9991 (asserted within 0.02 of 1).

## Estimates against measurement

Estimates with supplied inputs (the heat-kernel normalisation delta(1/16 pi G) = (1/2)(1/6 - xi) G(0) per real component with 1/(16 pi G) = 1/(2 L^2); the envelope |C| <= 10; f = 24 x 0.00483/0.5 = 0.232, the induced tensor fraction for 24 Dirac copies from the companion note THE_CUBE_TICK_SEA_INDUCES_NEITHER_A_LORENTZ_INVARIANT_MAXWELL_TERM_NOR_A_NEWTONIAN_SECTOR_BOUNDED_THEOREM_NOTE_2026-10-21; block sizes b_e from earlier block computations; l_P = 1.616255e-35 m):

| b_e | one minimally coupled component, W4/(6 b_e^2) | envelope 10 W4/b_e^2 |
|---|---|---|
| 1 | 2.6e-02 | 1.5e+00 |
| 10 | 2.6e-04 | 1.5e-02 |
| 27 | 3.5e-05 | 2.1e-03 |
| 76 | 4.5e-06 | 2.7e-04 |

- At one-cell edges (b_e = 1) the correction is O(1) and uncontrolled; at the block sizes the rules use it is small.
- Reference choice: with no subtraction the sea adds f = 0.232 to the tensor term and nothing to the Newtonian one (G_T/G_N 0.81, from the companion note). With an instantaneous reference it adds f to the tensor kinetic term only, giving |c_g - 1| = 0.099 against the GW170817 bound of about 3e-15; with the adiabatic reference it adds nothing.
- Sea modes slower than the edges' zero-point motion (below about 1/(b_e L)) are not adiabatic, but carry at most the fraction 1/b_e^2 of the induced term: f/b_e^2 = 2.3e-03, 3.2e-04, 4.0e-05 at b_e = 10, 27, 76.
- Unit map L/l_P = sqrt(8 pi)(1 + dG/(2G)): sqrt(8 pi) = 5.0133; at b_e = 10 the range is 4.969 to 5.058; L = 8.103e-35 m. L moves by under 1%, not by an O(1) factor.

## Boundary

Not claimed: the value of the lattice sum C (only an envelope is supplied); the edge field's curvature couplings and ghost content; the induced term for the full matter content on the update law's cube tick (toy seas only); real pair creation above threshold; a derivation that the register's dressed-weight clause names the adiabatic rather than the instantaneous vacuum.

## Supplied vs forced

Supplied: the toy seas (2D staggered Fock torus, 2D single-particle torus, 1D Wilson-Dirac), the scalar vertex, the edge modulations, the heat-kernel normalisation, the envelope |C| <= 10, f = 0.232 from the companion note, the block sizes. Forced, given those: zero induced edge action under the same-edge reference; the flat-reference remainder; the q^2 - omega^2 structure and the resulting non-covariance of an instantaneous reference; order-by-order removal by an adiabatic reference; W4; the stiffness independence of the one-loop term and so the 1/b_e^2 scaling of dG/G.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records. They fix none of the supplied inputs above.
- [Candidate-law register](CANDIDATE_LAWS.md): the response law's vacuum standard, the coefficient-one hinge sum, block edges of b_e cells. Zero premise weight; results using it are conditional on it.

## How to run

```
python3 scripts/same_edge_vacuum_subtraction_removes_the_induced_edge_action_and_edge_loops_move_g_as_one_over_the_block_area_2026_10_22.py
```

Needs numpy and scipy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 120`, runs in about 1 s with about 110 MB resident, prints about 4.2 kB and ends with `TOTAL: PASS=10 FAIL=0`. Its random draws are seeded; two repeated runs gave identical output apart from the elapsed-time line.
