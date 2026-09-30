# T15 pre-registration (written before any script was run)

Author: Claude Sonnet 5.5 (same vendor family as the supervisor; same-family check).

Wall: the Euclidean hypercubic tick (primitive c_t = c_s on Z^3 x Z_tau) protects the
cone, but the real-time step is a different object; and the exponent 16 is "Euclidean-only"
(native continuous-time count is 8).

Hypothesis H*: the two halves of the wall are misframed in one specific way.
 (i) The temporal doubler (the 8 -> 16 factor, the k_4 = pi corner) is NOT removed by
     going to real time. The Hilbert space obtained by OS reconstruction from the free
     staggered block (positive two-step transfer matrix) already carries the doubled mode
     content, so "continuous emergent time has no second corner" is a non sequitur when the
     Hamiltonian is the OS Hamiltonian. The 8 vs 16 split is then a split between two
     REGULATORS (Kogut-Susskind Hamiltonian versus Z^4 staggered), not Euclid versus real time.
 (ii) The Euclidean tick cannot be a real-time step at c_t = c_s in d >= 2 (CFL): the
     real-time symmetric-difference (leapfrog) continuation of the same kernel has complex
     frequency wherever r > 1, and r_max = sqrt(d) > 1. The framework does not need it to be:
     OS defines real time as the continuous flow of H_OS = -(1/2a) log T^2.

## Test A (exact, free field): does the reconstructed Hilbert space carry the doubling?
Object: free staggered Grassmann action, N^d spatial torus x L time slices (antiperiodic in
time), mass m, d = 1, 2, 3; N = 4 (d = 3: 64 sites, L up to 12), N = 6 (d = 1, 2).
Prediction under H*: |det D(L)| = 2^{-nL} * Z_KS(beta = L; levels +-asinh(r_j))^2, n = N^d,
Z_KS = prod over the n single-particle levels (1 + e^{-beta eps}) e^{beta eps/2}.
Rival (native/KS count, no doubling): |det D(L)| = 2^{-nL/2} * Z_KS(beta = L)^1  (one factor).
PASS (for the route "doubling survives OS"): max relative error of ln|det D| against the
squared form < 1e-9 for every (d, N, m, L), and the single-power form fails by > 1e-2.
FAIL (route dead): the single-power form fits and the squared form does not. Then the
reconstructed space has the KS count 8, and the fork note's "native gives 8" reading of the
real-time content stands.
Also record: number of negative and positive decaying roots of the recurrence (expected
equal, n/2 each per particle/antiparticle sector).

## Test B (exact, algebra + grid): can the tick be a real-time step at c_t = c_s?
Object: leapfrog continuation psi_{t+1} = psi_{t-1} - 2 i tau H psi_t, H = KS spatial
operator + m P, eigenvalues +-r, r^2 = m^2 + sum sin^2 k_i.
Prediction: unitary (|z| = 1) iff tau*r <= 1; at tau = a (= c_t = c_s) the fraction of the
Brillouin zone with r > 1 is 0 for d = 1 and positive for d = 2, 3.
PASS (for "tick is not a real-time step in d >= 2"): fraction > 0 for d = 2 and 3 at m = 0
and fraction = 0 (up to grid) for d = 1. FAIL: fraction 0 for d = 2 or 3.
Also verify by direct eigenvalue computation of the 2-step matrix that |z| != 1 on the r > 1
set, and that the doubler branch omega = pi - asin(tau r) exists for r <= 1.

## Test C (exact): inheritance of the cone.
The OS Hamiltonian E = asinh(r) has small-k speed 1 = c_s and maximal group velocity <= 1
on the whole zone; E_OS^2 and omega_RT^2 differ from r^2 at O(r^4) only.
PASS: max_k dE/dk = 1 (attained at k -> 0), E/r -> 1. FAIL: any group velocity > 1 or
small-k speed != 1.

## Test D (table): temporal corners of one-step unitary ticks.
For U = exp(-i tau H) and the Cayley tick (1 - i tau H/2)/(1 + i tau H/2) count nodes
(quasi-energy 0 or pi, massless) per spatial corner; for the leapfrog the same.
Prediction: 0 extra nodes at pi for the first two, 1 extra for leapfrog (only for tau*r <= 1).

## What each outcome would do
- A PASS and B PASS: the "not the real-time step" half is a non-requirement (OS flow), the 16 is a
  regulator choice = a named premise; wall priced, half of it misframed. It does NOT pass the wall:
  the interacting OS and the existence of an RP action stay open (sibling T02, T03).
- A FAIL: the exponent split is real: real time has 8. Wall stands harder.
- B FAIL: the identification of tick and step is not excluded by CFL; the tick-as-step route reopens.

## Addendum A2 (written after run 2, before run 3; run 2 passed Test A on free field)
Test E (static gauge background). Same D but random U(1) phases on every SPATIAL link, temporal
links = 1 and time-independent. Derivation: B = P(A+m) is still Hermitian with symmetric spectrum
(P A P = -A holds for any nearest-neighbour bipartite A; odd moments of B vanish), so the same
Matsubara product applies with r^2 = m^2 + spec(A^dagger A). Prediction: |det D| = 2^{-nL} Z_KS^2
with levels +-asinh(|mu_j|) to 1e-12 for random static spatial phases. PASS = identity holds; FAIL =
the doubling was a free-field accident. Test F (convention): time-first staggered phases
(eta_t = 1, eta_i = (-1)^{t + sum_{j<i} x_j}) give the same |det D|: PASS if equal to 1e-12.
Test G (discriminating power): random time-DEPENDENT temporal U(1) phases (strength 0.5) should
break the identity (error >> 1e-6), i.e. the identity is not trivially true for every D.

## Run log (honest)
- run1: Test A failed by a constant offset n*ln4 independent of L, a bug in my lnZ_KS (an extra ln 2 per level).
  Kept as run1_BUGGY_extra_ln2_in_lnZ_KS.txt. Bug fixed, criteria unchanged, rerun = run2.txt. The direct
  determinants were untouched by the bug.
- run2: A, B, C, D as pre-registered: all pass. run3: E, F pass; G (discriminating power) breaks the identity as expected
  (temporal phases change the Polyakov loops, so this is only a sanity check that the identity is not vacuous, not a taste-breaking result).
- Not tested: interacting temporal links, non-abelian links, dynamical gauge fields, rooting.
