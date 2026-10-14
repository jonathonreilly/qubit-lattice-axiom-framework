# F5-T1 pre-registration (written 2026-10-14 13:33Z, before any run)

Route F5-A (dissipative Wilson walker). Agent: Claude Opus 5.5 (route agent F5), same family as supervisor.

## Class searched (bounded; not a no-go beyond it)
Quasi-free (quadratic), translation-invariant, Markovian (Lindblad, CPTP) dynamics of the
two-component walker h(k) = sum_j sin k_j sigma_j on Z^3 (periodic grid), with
- (S) the scalar "dissipative Wilson" family: loss-only or loss+gain with damping
  Gamma(k) = kappa f(k)^p * 1, f = sum_j (1 - cos k_j), p = 1, 2, 4;
- (R) random jump families: 3 loss + 2 gain operators whose Bloch symbols are random
  complex trigonometric-polynomial 2-vectors of range <= 2, each multiplied by f(k)^m
  (m = 1, 2) so the damping vanishes only at k = 0; 6 random seeds per m.
Single-particle equation: d rho1/dt = -i[h, rho1] - (1/2){M + N, rho1} + N,
M = sum loss symbols v v^dag, N = sum gain symbols g g^dag; h_eff = h - (i/2)(M + N).

## Measured
1. W3[h_eff - E_ref], E_ref = -i*eta just below the real axis (point-gap winding; T2 of
   LATTICE_HANDEDNESS proves W3 = 0 for every finite-range UNITARY tick).
2. min over k != 0 of the smallest damping rate of h_eff (doublers damped?).
3. Steady state rho_ss(k) (per-k Lyapunov solve): mixedness sum lambda(1 - lambda),
   averaged over the zone; and the steady-state jump rate per site
   r = <Tr(M rho)> + <Tr(N (1 - rho))> (record-writing events per site per unit time if
   each jump writes a record).
4. Direction-averaged deviation from the Dirac sea near the light node,
   e_sea(q) = <n_+(qhat) + 1 - n_-(qhat)>_{S^2} at |q| = 1e-3, 1e-2, 1e-1.

## Readings (fixed now, not to be changed after the result)
- PASS (the lens survives this test): some member has W3 != 0 (one undamped light node,
  doublers damped) AND r = 0 to numerical precision (a jump-free steady state, compatible
  with one permanent record per site) AND e_sea -> 0 as q -> 0.
- FAIL: every member with W3 != 0 has r bounded away from 0, and e_sea -> 1 (or stays O(1))
  as q -> 0. This is a bounded result for the searched class; the general statement rests on
  the lemmas in ROUTE_REPORT.md (Lemma B, Lemma C), not on the search.
- Controls that must behave: Hermitian limit (Gamma = 0) gives W3 = 0; a gapped trivial
  insulator with on-site spin-up loss and spin-down gain gives r = 0 and a pure state.

## Prediction (registered so it can be wrong)
W3 = +-1 for every member whose damping vanishes only at k = 0; r > 0 for all; e_sea -> 1.

---

# F5-T2 pre-registration (written 2026-10-14 13:37Z, after T1's result, before T2 is run)

Route F5-B mechanism test, 2+1D -> 1+1D analogue only (does NOT count as closure; WALL.md says
1+1D alone is not closure). Question: can an absorbing (lossy) far boundary remove the mirror
chiral mode of an inflow slab, or does strong loss just push the mirror one row inward
(quantum Zeno), as the SPIN10 frozen-boundary projection pushed doublers inward?

Model: Qi-Wu-Zhang strip, h = sin kx sx + sin ky sy + (m + cos kx + cos ky) sz, m = -1,
open in y with Ly = 12, 20, 30 rows; Markov loss Gamma on both orbitals of the last row only;
h_eff = h_strip - (i/2) Gamma P_last. Scan Gamma in {0.1, 0.3, 1, 3, 10, 30, 100}.
Measure, over kx, the decay rates (-2 Im E) of in-gap eigenstates (|Re E| < 0.4).

- PASS (lossy far wall works in the analogue): for some Gamma, the in-gap content is exactly
  one branch with decay < 1e-6 (the near-edge chiral mode, Ly = 20) and every other in-gap
  state has decay >= 0.05 at every kx.
- FAIL (Zeno relocation): for every Gamma some second in-gap branch has decay < 0.01 over
  a kx interval crossing Re E = 0.
- Also record: near-edge decay vs Ly (expect ~exp(-2 Ly / xi)) and the large-Gamma scaling
  of the far-edge decay (Zeno prediction ~ 1/Gamma).

## F5-T2b (dated follow-up, registered 2026-10-14 13:38Z AFTER seeing T2)
T2 used m = -1, where the QWZ edge mode is exactly one row thick near kx = 0, so the
near-edge decay sat at machine floor and the Ly scaling could not be seen. T2b repeats T2
unchanged (same PASS/FAIL readings) at generic masses m = -1.5 and m = -0.5, Ly = 8, 12, 16,
to check robustness and to see the near-edge leak ~ exp(-2 Ly / xi).

## F5-T3a (registered 2026-10-14 13:42Z, after T2/T2b, before running)
Question: does a Markov lossy far wall also drain the filled bulk (valence) sea of the inflow
slab, through the bulk states' amplitude on the last row? (If yes, the near-wall sea ends where
it merges into an emptied bulk: Lemma B's compensating flux lands on a zero-cost filled/empty
interface, the precursor of the Ohmic-vacuum argument, Lemma V.)
Model: T2's strip, m = -1.5, Ly = 12, 20, 30, Gamma = 0.3, 1, 3. Decay rates of all valence
states (Re E < -0.4).
- PASS (route F5-B survives the drain): a nonzero fraction (>= 10%) of valence states have
  decay < 1e-6 at Ly = 20 (protected bulk sea).
- FAIL: every valence state has decay >= 1e-4 at Ly = 20 (the whole bulk sea drains within
  ~1e4 lattice times); report the median decay and its Ly scaling (expect ~ Gamma / Ly).

## F5-T3 (as written in ROUTE_REPORT draft at ~13:45Z): WITHDRAWN BEFORE RUNNING (13:47Z)
Reason (reasoning, no result seen): with a Markov loss-only far wall, T3a already shows the bulk
drains, so the system empties and R(E) -> 0 trivially; the test could not separate the Ohmic
branch of Lemma V. Replaced by F5-T3' below.

## F5-T3' (registered 2026-10-14 13:47Z, before running): the energy-selective horn
Dilemma under test: a Markov (band-blind) sink drains or heats the seas (Lemma P, T1, T3a); an
energy-selective zero-temperature sink (retarded self-energy -i Gamma(k)/2, occupations theta(-w),
mu = 0) keeps the seas but broadens the damped mirrors. Lemma V (suggested) says a broadened
charged node at mu = 0 conducts: sigma(0) ~ e^2 Gamma.
Model: the scalar dissipative Wilson walker, Gamma = kappa f^p, kappa = 1, p = 1, 2, 4, on N^3 grids
(N = 32, 48, 64; shifted grid). Kubo-Bastin Fermi-surface term at T = 0, w = 0:
  sigma_xx = (1/pi) * mean_k Tr[v_x ImG v_x ImG],  G = (0 - h + i Gamma/2)^-1,  in e^2/(hbar a).
Control: Gamma = eta * 1 (Hermitian walker, eta -> 0): sigma_xx -> 0 linearly in eta.
- PASS (energy-selective sink harmless): sigma_xx < 1e-60 e^2/(hbar a) (photon absorption slower than
  the age of the universe) for some p.
- FAIL: sigma_xx >= 1e-6 e^2/(hbar a) for every p; report the light-node vs doubler split.

## F5-T4 (registered 2026-10-14 13:49Z, not run): energy-selective far wall on the strip
QWZ m = -1.5, Ly = 20; far row attached to a T = 0 wide-band lead (self-energy -i Gamma/2 on the last
row, mu = 0), Gamma in {0.1, 1, 10}. Kubo-Bastin DC sigma_xx, with the near-edge Drude part removed
by adding a uniform eta in {1e-2, 1e-3} and subtracting the eta-scaling piece.
- PASS: the far-wall remainder is < 1e-6 e^2/h for some Gamma.  FAIL: it is >= 1e-3 e^2/h for all Gamma.
