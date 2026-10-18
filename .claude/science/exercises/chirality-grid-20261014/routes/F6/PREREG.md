# F6 pre-registrations (written 2026-10-14 13:31Z, before any script was run)

Route agent F6 (misframing brief). Claude Opus 5.5, same family as the supervisor; not an independent referee.

## T-A  Operator versus net chirality (route F6-1)

A1. Two-component walker on the site qubit, H = sum_a sigma_a sin(p_a), periodic L = 4 (128 x 128 dense).
Body-diagonal shift T_d = T_x T_y T_z (identity on the qubit). Staggered sign eps = (-1)^(x+y+z).
- PASS: ||[H, T_d]|| <= 1e-10; ||T_d eps T_d^-1 + eps|| <= 1e-10; spectrum of H + m eps has min |E| = m (to 1e-10);
  and at all 8 corners k in {0,pi}^3 the T_d eigenvalue exp(i(kx+ky+kz)) times the Berry-monopole
  charge of the lower band (computed independently, discrete Stokes on a small cube around the corner) is the same sign.
- FAIL: any of these violated.
- Reading if PASS: one qubit per site already carries an exact lattice chirality operator in continuous time
  (commutes with the kinetic term, anticommutes with the only bookkeeping mass); what it lacks is net chirality.

A2. 20 random finite-range (range-1 cube, 26 neighbours) Hermitian carriers with N = 2 and 20 with N = 4 bands per site,
no symmetry imposed (no parity, no time reversal, no rotation). Monopole census at the N/2 | N/2+1 gap by discrete
Stokes (Fukui-Hatsugai-Suzuki link variables) on a 20^3 grid.
- PASS (for the misframing): every sample has net monopole charge 0, and at least half the N = 4 samples show nodes of both hands.
- FAIL: any nonzero net (would signal a bug; the net is zero by theorem).
- Note: net = 0 is a theorem (Stokes on T^3). The runner illustrates; the proof is the evidence.

## T-B  What observation allows for mirror masses (route F6-2)

B1. Index lemma (proof in report); runner: 200 random U(1)-invariant symmetric (Majorana) mass matrices on random
vector-like charge lists; PASS: the massless charge multiset is symmetric under q -> -q in every sample.

B2. Mirror families whose masses come from electroweak breaking (degenerate doublets, Peskin-Takeuchi heavy limit):
S per mirror family = (N_c + 1)/(6 pi). gg -> h rate with one extra chiral heavy quark doublet (exact one-loop A_1/2).
- PASS (G-breaking mirror masses are observationally excluded): S for three mirror families exceeds the PDG fit
  central value by > 3 sigma, AND mu_ggF >= 5 for every mirror-quark mass in 0.4-3 TeV.
- FAIL: either quantity within 2 sigma of data.

## T-C  The cheaper question's first test: anomaly gate on the framework's own mirror halves (route F6-3)

Content: 16 lattice fields carrying the left-handed-basis SM charges (Q, u^c, d^c, L, e^c, nu^c), and the 15 without nu^c.
Splits: (W) walker, light = hw=1 corners (three, one hand), mirror = hw 0, 2, 3; (K) Kogut-Susskind / K2a,
light = T_d-even half (2 x 16), mirror = T_d-odd half (2 x 16bar).
Coefficients of the mirror half: SU(3)^3, U(1)_Y^3, U(1)_Y-grav^2, SU(3)^2 U(1)_Y, SU(2)^2 U(1)_Y (exact);
Witten SU(2) (doublets mod 2); Z16 for Spin-Z4^X with X = 5(B-L) - 4Y; Ibanez-Ross-type mixed Z2 x G^2 (mod 2)
for every Z2 subgroup of the corner translation group (walker: 7 subgroups; K: Z2^d only).
- PASS: with nu^c every coefficient of the mirror half vanishes, for both splits.
- FAIL: any nonzero coefficient; the symmetry carrying it is then the exact price for symmetric gapping.
- Expectation before running: PASS with nu^c; without nu^c only Z16 fails (walker mirror -45 = 3 mod 16; K mirror -30 = 2 mod 16).
- Count check (same script): walker split with 16 fields gives 48 light Weyl of one hand = 3 x 16.

## T-D  Follow-up added 2026-10-14 13:41Z, before running (construction supporting route F6-3)

Walker plus one local staggered bilinear M_f = i eps F, where F is the scalar hopping operator with symbol
f(k) = s(s^2 - 1), s = cos kx + cos ky + cos kz (range 3, cubic-rotation invariant, G-invariant).
On L = 4 (corners on the grid) and L = 8:
- PASS: M_f Hermitian; {H, M_f} = 0; zero-mode count of H + M_f = 12 (6 nodes x 2: hw 1 and hw 2 only);
  T_d = -1 on all hw=1 zero modes and +1 on all hw=2 zero modes; nonzero spectrum gapped by >= 1e-6 at L = 8
  except at the six nodes (min |E| over non-node momenta reported).
- FAIL: any of these violated.
- Reading if PASS: per field, the walker reduces by a local covariant bilinear to 3 left (hw1) + 3 right (hw2),
  graded by T_d on the nodes; the mirror list SMG must gap is exactly 3 x 16bar with no vector pair.
