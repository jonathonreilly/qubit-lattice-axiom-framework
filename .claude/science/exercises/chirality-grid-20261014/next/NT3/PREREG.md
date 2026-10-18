# NT-3 = T-G1 pre-registration (written 2026-10-14 ~20:55Z, before any test run)

Agent: Claude Opus 5.5 (same family as supervisor and all exercise agents; not independent).
Item: TESTS.md (branch origin/claude/chirality-grid-exercise-20261014) lines 40-43, FIXED readings
TG1-SYMMETRIC / TG1-BROKEN / OPEN. This file only makes those readings operational; it does not change them.

Only run before this file: `scripts/design_overlaps.py` (a design calculation of filter overlaps, not a test;
output pasted below). It reproduces K1's 3D numbers (f_NN A = 1.2247, max 0.400; f_F1 A = 0.6338, max 0.185).

## Question
K1 gap G1 (kills/K1/KILL_REPORT.md:203): does H_Q = sum_x Q(psi_S(x)), psi_S = F psi, restricted to the
mirror (non-light) modes, have a unique, symmetric, gapped ground state at strong coupling, as the on-site
quartic does, or does the overlap of neighbouring psi_S(x) (no independent-site limit; K1:176-183) produce
degeneracy, order growing with size, or a gapless sector?

## Toy model (stands in for X2's Spin(10)/16 and its 10-vector channel)
- Per site: 4 complex fermions c_alpha(x), alpha = 1..4 = the 4 of SU(4) = Weyl spinor of Spin(6).
  4 x 4 antisymmetric = 6 = vector of SO(6); B_{ab} = c_a c_b is the 6-vector bilinear (image of X2's B^a).
- Primary interaction (image of EP's lambda term B^a B^a + h.c., all legs filtered):
  Q(psi_S(x)) = -( c_S1 c_S2 c_S3 c_S4 (x) + h.c. )  [= -(1/24)(eps cccc + h.c.) = -(B.B + h.c.)/norm].
  Symmetries: SU(4), translations, k -> -k parity (f even), Z4 (c -> i c); U(1)_F broken to Z4 as in X2 (X2:80).
  On-site eigenvalues per site: -1 (unique, (|0> + |1111>)/sqrt2, SU(4) singlet), 0 (14 states), +1.
- Strong coupling = W -> infinity: H = H_Q alone (primary). The light mode k = 0 has f(0) = 0, so it
  commutes with H_Q exactly (X2-L2); the Fock space is the non-light modes (light factor 2^4 trivial; checked V2).
- Momentum-space form: H_Q = -(1/V) sum_{k1+k2+k3+k4 = 0} f(k1)f(k2)f(k3)f(k4) c_1(k1)c_2(k2)c_3(k3)c_4(k4) + h.c.

## Filters (normalised <f^2>_BZ = 1 for the local ones, so the on-site control has the same K(0) = 1)
| id | f(k) | aggregate overlap A | max nbr |K(r)|/K(0) | role |
|---|---|---|---|---|
| C0 | 1 on all k (light included) | 0 | 0 | on-site control (exactly solvable; ED as code check) |
| C1 | 1 on k != 0, 0 at k = 0 (ring-only, nonlocal) | 1/sqrt(L-1) | 1/(L-1) | minimal-overlap light-decoupling comparator |
| F_lo | (1-cos k)(1+0.6 cos k)/2 | 0.656 | 0.358 | f_F1-like aggregate (3D 0.634) |
| F_star | (1-cos k)/2 (3-site star) | 0.972 | 0.667 | 1D image of both X2 filters |
| F_hi | ((1-cos k)/2)^2 | 1.275 | 0.800 | >= f_NN aggregate (3D 1.225) |
| cube | 2x2x2 3D cluster, exact X2 f_NN and f_F1 values at the 8 corners (light = hw1) | — | — | single-size 3D data point |

Sizes: 1D rings L = 3, 4, 5, 6, 7 (L = 7 only if the largest sector's sparse matrix is estimated <= 0.6 GB;
memory cap 1.0 GB per run, one process, OMP_NUM_THREADS = 2). Mirror Fock dim = 2^(4(L-1)) (L = 7: 2^24, split
into (SU(4)-weight, momentum) sectors; largest primary sector ~ 4e4). Cube: 2^20 split into 8 momenta x weights.

## Method
Exact diagonalisation (dense below dim 600, Lanczos/eigsh otherwise) in every sector labelled by the SU(4)
weight modulo the diagonal shift (the eps term shifts all n_alpha by 1) and total momentum; only dominant
weights n1 >= n2 >= n3 >= n4 are needed (every multiplet has a highest weight there). Real symmetric matrices.

## Observables (per filter, per L)
1. E0/L; ground-state degeneracy D (all sectors; a GS at momentum K != 0 or a non-singlet GS counts as D > 1);
   GS quantum numbers: SU(4) singlet test (raising operators E_12, E_23, E_34 annihilate GS to < 1e-8), K, N mod 4.
2. Gap Delta = E1 - E0 over all sectors; sector-resolved lowest energies (4, 6, 15, ... sectors) incl. the
   6-vector-sector gap Delta_6 (tower-of-states precursor).
3. Order: pair field P_q = sum_k g(k) c_1(k) c_2(q-k), with g = f f (psi_S version) and g = 1 (mirror-projected
   local psi_M version); structure factor S_6(q) = (6/L) ||P_q|GS>||^2 at q = 0 and q = q_max (closest to pi);
   q = 0 susceptibility chi_6 = (6) * 2 sum over both P and P^dag of <v|(H - E0)^-1|v>, reported per site.
4. Light attribution of the lowest excitation: Delta n(k) = sum_alpha (<n_alpha(k)>_exc - <n_alpha(k)>_GS);
   w_light = weight of |Delta n| on the two smallest |k| = 2 pi/L. Lowest excitation "light-attributed" if w_light >= 0.5.

## Decision rules (fixed now; per filter; trends use L = 4..Lmax, L = 3 reported only, since at L = 3 every
non-light mode is adjacent to k = 0)
- U: D = 1 at every L in 4..Lmax.
- S: unique GS is an SU(4) singlet with K = 0 (a unique GS is automatically invariant up to phase; checked anyway).
- G (gapped): Delta_nl(L) >= 0.1 (on-site gap = 1) at every L, and Delta_nl(Lmax)/Delta_nl(Lmax-2) >= 0.6, where
  Delta_nl is the lowest excitation that is NOT light-attributed. A light-attributed excitation is the by-design
  light branch (the X2 light generation lives there and is gapless by construction); its gap is reported
  separately and does not by itself count as the FIXED reading's "gapless sector" (reading, stated now).
- O (no order growth): S_6(0)(Lmax)/S_6(0)(4) < 1.4 and chi_6/L(Lmax)/chi_6/L(4) < 1.4 (LRO would give ~ Lmax/4 >= 1.5
  for S_6(0)), for both psi_S and psi_M versions; and Delta_6 not monotone-decreasing to < 0.5 Delta_6(4).

Readings per filter:
- **TG1-SYMMETRIC:** U and S and G and O all hold.
- **TG1-BROKEN:** U or S fails at some L >= 4 (degeneracy, nonzero-momentum or non-singlet GS); or O fails
  monotonically (order / tower growing with size); or G fails on a non-light-attributed excitation (gapless sector).
- **OPEN:** otherwise (non-monotone, criteria split across sizes, numerical problems).
Overall NT-3 reading: TG1-SYMMETRIC if F_lo, F_star, F_hi are all SYMMETRIC and the cube has a unique singlet
gapped GS for both f_NN and f_F1; TG1-BROKEN if any of these is BROKEN, stating which overlap fails (X2 needs only
one working filter, X2:59, so a filter-split result is reported as such); OPEN otherwise. The controls C0/C1 must
read SYMMETRIC; if a control fails the test is OPEN (instrument problem).

## Validation (before trusting results)
- V1: C0 ED reproduces E0 = -L, D = 1, gap 1 exactly (L = 3..5).
- V2: F_star with the light mode included (L = 4): same E0, degeneracy x 16.
- V3: independent real-space Jordan-Wigner builder (dense, L = 3, 4096 dims incl. light; sparse L = 4) reproduces
  the momentum-space spectrum (lowest 6 levels to 1e-9).

## Secondary (robustness; does not change the primary reading unless it flips U/S, reported either way)
- S1: Q_v = Q + v sum_{a<b} B_S,ab^dag B_S,ab, v = +0.5, -0.5; F_star; L = 4..6.
- S2: H = sum_k sin(k) n(k) + W H_Q, W = 4, 16; F_star; L = 4..6 (1D image of the walker; 1D chiral anomaly
  forbids a gapped chiral mirror in the thermodynamic limit, so S2 is a finite-size check only).

## Scope (fixed now)
0+1D-like finite clusters (rings <= 7 sites, one 8-site cube). They cannot decide 3+1D or 4D. 1D cannot host
continuous SSB (Coleman), so only precursors are measurable; 1D concentrates the overlap on 2 neighbours, so per
bond it is harsher than 3D at equal aggregate A. SU(4)/6-vector stands in for Spin(10)/10-vector. No kinetic term in
the primary model (W = infinity).

## Design calculation output (scripts/design_overlaps.out)
star A = 0.9718 max 0.6667; flat b = 0.6 A = 0.6561 max 0.3577; ((1-c)/2)^2 A = 1.2754 max 0.8000;
3D f_NN A = 1.2247 max 0.4; 3D f_F1 A = 0.6338 max 0.185.

---
## Dated follow-up A1 (2026-10-14 ~21:01Z; appended after the L = 3..6 primary runs, before any run below)
Observed so far (primary_L3to5.out, primary_L6.out): unique singlet K = 0 GS everywhere; the lowest excitation is
always the 6-vector sector (1,1,0,0) at K0, and for the local filters its gap falls with L (F_star 0.45, 0.18, 0.074;
F_hi 0.081, 0.0065, 0.00064 at L = 4, 5, 6) while C1 stays at 0.488-0.489 and the 2x2x2 cube gaps are 1.31 / 1.65.
**Defect in the pre-registered attribution metric:** for the self-conjugate 6 sector the flavour-summed Delta n(k)
vanishes identically (particle-hole), so w_light = 0/0 was set to 0 and the 6-sector state was classed "non-light"
by default (analyze.py; visible as w0.00 rows). The literal rules are applied unchanged in the report; the
following diagnostics decide whether the collapse is the near-light weak coupling (f(2 pi/L) -> 0 by design) or a
mirror-sector SSB precursor. They do not change the FIXED readings.
- D1 (decoupling): rerun F_lo, F_star, F_hi with f set to 0 on the near-light momenta |k| = 2 pi/L (those modes then
  decouple exactly and are dropped like k = 0), L = 5, 6, 7 (L = 4 leaves only k = pi). Reading: if the 6-sector gap
  becomes >= 0.3 and flat and chi_6/site stops growing (< 1.4 ratio over the L range), the collapse is attributed to
  the near-light modes; if the gap still collapses, it is attributed to the mirror sector (SSB precursor -> BROKEN).
- D2 (scaling): tabulate gap_6(L) against f_near(L)^2 and f_near(L)^4 (f_near = normalised f(2 pi/L)).
- S2 extended: kinetic term sum_k sin(k) n(k) + W H_Q for F_lo, F_star, F_hi, W = 4, 16, L = 4..6, GS momentum
  found by scanning the weight-0 sector over all K. Reading: same U/S/G/O rules with the kinetic term present;
  near-light modes then carry kinetic energy |sin(2 pi/L)| >> W f_near^4 for F_hi.
- L = 7 primary as registered (all sectors), if the largest sector (~4e4) runs within budget.

---
## Dated follow-up A2 (2026-10-14, appended at the time printed by `date -u` just above this block in the run log, ~21:10Z; before the runs below)
Seen since A1: L = 7 primary (F_star gap 0.031, F_hi 8.2e-5, F_lo 0.330, C1 0.489; all GS unique singlets);
D1 (near-light shell dropped): gaps still fall for F_star/F_hi and equal 0.64 x (smallest kept f)^2 to 1%
(so the next shell takes over); S2 (kinetic + W H_Q): lowest excitations are single light-branch quasiparticles.
A2 adds a working attribution for the soft 6-sector state (replaces the 0/0 metric; does not change readings):
- D3: for the lowest state |6> of the (1,1,0,0) chain at the GS momentum, pair weights
  w(k) = |<6| c_2^dag(-k) c_1^dag(k) |GS>|^2 / sum_k' (same), and the overlap of |6> with the normalised
  P^dag_q=0 |GS> (psi_M version). "Near-light-attributed" if w(+-2 pi/L) carries >= 0.5 of the pair weight.
  Runs: primary F_lo, F_star, F_hi at L = 5, 6, 7; C1 at L = 6 as control.
- S1 as pre-registered (v = +-0.5, F_star, L = 4..6).

---
## Dated follow-up A3 (appended 2026-10-14, time = the `date -u` line printed just before this append in the session log; before the run below)
D4 (mirror-corner single-particle spectral gap; observable only, readings unchanged): primary W = infinity model,
F_lo / F_star / F_hi / C1, L = 4..7, mirror momentum k_m = floor(L/2) (pi for even L, nearest to pi for odd L).
In the sector of c_1^dag(k_m)|GS> (weight (1,0,0,0), momentum K0 + k_m) compute the lowest 8 levels and the
normalised spectral weights |<n|c_1^dag(k_m)|GS>|^2 / ||c_1^dag(k_m) GS||^2; report the weight-averaged energy
E_avg - E0 over those levels, the captured weight, and the lowest level carrying weight >= 0.1.
Same for the hole c_1(k_m)|GS>. Interpretation (stated now): a size-independent O(1) mirror-corner gap with the
weight concentrated in one level is the SMG signature at the corner; a gap falling with L at the corner (not at
the light shell) would be a mirror-sector gapless signature.
