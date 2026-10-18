# C1 WORKLOG

## 2026-10-18 18:56 UTC — setup, model fixed from repo, criteria declared (before any production data)

**Model (supplied premise, read from repo).**
- `docs/THE_PURE_SPIN_HALF_LINK_MODEL_ON_THE_CUBIC_TORUS_IS_GAPLESS_..._2026-09-04.md` (Definitions):
  `E_e = Z_e/2`, `U_e = sigma^+_e`, `G_v = (div E)_v - rho_v`, and **`rho_v = 0` on every
  torus (z_v = 6 even)**; the staggered background `2rho = +-(-1)^i` is declared only on the
  2D *ladder* geometry, not on the cubic torus.
- `docs/RING_MODEL_BETWEEN_THE_ROKHSAR_KIVELSON_AND_PURE_RING_POINTS_..._2026-09-24.md` and its
  runner: `H = V D - g A` on the ice (3-in/3-out) configurations, A = plaquette-flip adjacency,
  D = number of flippable plaquettes. RK point V = g.
- `docs/RING_MODEL_THE_ZERO_WINDING_GAUSS_SECTOR_HAS_FROZEN_FLIP_COMPONENTS_..._2026-10-01.md`:
  sector = flip component of the canonical zero-winding state; frozen states exist on every even L.
- Exact L=2 anchors (from those notes, to be recomputed here): 9600 Gauss states, 937 flip
  components, largest 864 (zero winding); at V=0, g=1: E0 = -9.0267209135, internal gap 2.2257853859.

**Discrepancy with the task text.** The task says "the repo's staggered background charge
convention". On the cubic torus the repo convention is rho_v = 0 (no background). I use rho = 0
and report this. (Staggered background appears only for the 2D ladder.)

**Method decision (justified in NOTE).** A periodic (finite-T trace) worldline with local
plaquette-flip pair updates conserves, for every plaquette, the net signed number of flips over the
period; these integers form a class label (cube boundaries + three global plane classes) that local
updates cannot change, so a local finite-T code samples a class-restricted ensemble, not Tr e^{-bH}.
I therefore use an **open-path, guide-free (uniform trial state) continuous-time path-integral
projector (PIGS-type)**: the ends are free, so single-flip end moves change every class, and the
middle of the path samples |psi0|^2 exactly as T -> infinity with no importance function.
Projection time T plays the role of beta; scaled T = a L (z=1) and T = b L^2 (z=2).
A periodic-mode run at L=2 vs exact thermal ED is kept as a negative/ergodicity control.

**Prior exposure disclosed.** I have read titles/summaries of the repo RING_MODEL notes (guide-
biased projector results: e.g. reptation S at k_min 0.62(2) on 4^3, 0.50(2) on 6^3 with guide
exp(0.2 N_flip); 09-04 note title "quadratic transverse mode not a Maxwell photon", unverified).
Literature recalled (no numbers relied upon): pyrochlore quantum ice Coulomb phase at V=0
(Hermele-Fisher-Balents 2004; Banerjee et al 2008; Shannon et al 2012); cubic QDM (Sikora et al
2009/2011): Coulomb phase only in a window below RK, ordered at smaller V (I do not recall the
window edges reliably).

### Pre-declared comparison criteria (fixed now, before production)

Observables (per site, N_v = L^3), measured at the path middle:
- S_T(k) = sum_a <|E_a(k)|^2>/N_v (S_L = 0 exactly by Gauss), at k_min = 2pi/L (avg over axes).
  Exponent p(L1,L2) = ln[S_T(k1)/S_T(k2)] / ln[K1/K2], K = 2 sin(k/2).
  Expectation: quantum Coulomb p = 1; classical/RK-like p = 0; gapped/confined p = 2.
- Flippability Bragg weights: S_n(Q) = <|sum_v (n_{v,o} - <n>) e^{-iQ.v}|^2>/N_v summed over the
  3 orientations o (and per orientation), for all Q in {0,pi}^3 \ 0 (and (pi/2,..)-type when L%4==0);
  E-field S_aa(Q) at the same Q. Bragg ratio R_Q = [S(Q,L_max)/S(Q,L=4)] / [N_v(L_max)/N_v(4)].
- Photon gap: omega_eff(k_min) from the imaginary-time transverse-E correlator at the middle.

Verdict rules (each V separately; L_max = largest L reached with converged projection):
1. **Ordered** if some Q has R_Q >= 0.5 with its 2-sigma lower bound >= 0.4 (Bragg weight
   not decaying like 1/N), OR p(two largest L) >= 1.6 at 2 sigma (lower bound).
2. **Coulomb (consistent)** if all R_Q <= 0.25 at 2-sigma upper bound, AND p from the two largest
   L lies in [0.6, 1.4] (2-sigma interval overlapping and central value inside), AND omega_eff*L
   at the two largest L agree within 25% (z=1) better than omega_eff*L^2 does.
3. **RK-like/classical** if p <= 0.4 and no Bragg.
4. Otherwise **inconclusive at accessible L**.
Projection convergence: a point is used only if the z=1 and z=2 (or two different T) values of
S_T(k_min) and E/N_p agree within 2 combined sigma; otherwise flagged.
Errors: binning with bin-size scan; quoted error = plateau (largest of the last bins) of binned SE.
Validation pass criteria vs exact L=2 (open path, finite T): |QMC - exact| <= 3 sigma for every
checked observable; additionally all relative errors < 1% for E.
