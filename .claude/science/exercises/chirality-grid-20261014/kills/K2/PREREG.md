# K2 kill-round pre-registrations (written 2026-10-14 15:07Z by `date -u`, BEFORE any K2 script is written or run)

Agent: Claude Opus 5.5 (same family as the X3 author and supervisor; NOT an independent referee).
Targets: X3-A, X3-B, X3-C, L3g (X3-E), the set-B package; parent F2-H.
Rule: readings below are fixed now. Never edited afterwards; later changes go in dated follow-ups.
All scripts: numpy/scipy, OMP_NUM_THREADS=2, < 0.3 GB, one at a time, own code (X3 scripts only read, never imported).

---
## K2-T1: independent rebuild of the free OS transfer spectrum of the overlap (X3-A, X3-B)

**Object.** Free Neuberger overlap on Z^4, D = 1 + X (X^dag X)^{-1/2}, X = sum_mu i g_mu sin p_mu + sum_mu (1 - cos p_mu) - M,
built numerically from explicit 4x4 Euclidean gammas (own basis), NOT from X3's closed forms.
C(t; p) = int dp4/2pi e^{i p4 t} D^{-1}(p4, p) by FFT over N4 = 8192 points, t = 1..2n.
Transfer content extracted model-independently: block-Hankel H0_ij = Gam C(i+j-1), H1_ij = Gam C(i+j) (i,j = 1..n, n = 6),
generalized eigenproblem H1 v = lam H0 v on the numerical range of H0 (Prony/GEVP). Gam calibrated on the free Wilson r=1, m=+0.5
control (must make H0 PSD; otherwise BROKEN). Second, independent of the Hankel route: E1(p) = the branch point of D^{-1}(z) found
numerically as the zero of det(X^dag X)(z) inside the unit disc (root finding on the 4x4 matrix, not the X3 formula), minimized
over the Brillouin zone by dense grid + Nelder-Mead from 200 random starts, for M in {0.5, 2-sqrt2, 1.0, 1.5, 1.9}.
Spatial momenta: the 8 spatial corners, 40 random p, 10 points near p = 0.

**Readings (fixed now).**
- **X3-A SURVIVES** if, for M in {0.5, 1.0}: (i) an isolated top GEVP eigenvalue lam_1 with |lam_1 - e^{-arcsinh S}| < 1e-6 exists exactly
  at the sampled p with beta(p) < sqrt(1+S^2) and at none of the 7 nonzero spatial corners; (ii) every other GEVP eigenvalue lies in
  (0, e^{-E1(p)} + 1e-6]; (iii) H0 and H1 PSD (min/max > -1e-9); (iv) min_p E1 >= 0.3 (and = ln 2 within 1e-3 at M = 1);
  and for M in {1.5, 1.9}: negative GEVP eigenvalues occur only at p with beta(p) < 0, with H0 PSD and H1 indefinite.
- **X3-A WOUNDED** if (i)-(iv) hold but a stated number is wrong (e.g. the global threshold minimum is not at an S = 0 point, or the
  "best value 0.881 at M = 2 - sqrt2" is off by > 1e-2).
- **X3-A DEAD** if any of: a light (lam > e^{-0.3}) isolated GEVP eigenvalue at a doubler corner; an isolated negative eigenvalue
  (pole) at M <= 1; H0 indefinite at M <= 1; min_p E1 < 0.3 at M = 1.
- **X3-B** (F3-A does not reach the free Euclidean route) is read off the same run: survives iff X3-A survives or is only wounded,
  AND no isolated (pole-type) lam < 0 exists for any M in (0,2) (a gapped negative continuum alone does not revive F3-A's copy).

## K2-T2: geometry diagnosis of X3's gauge-invariant tests (T-X3d/e/f/f', D1)

**Object.** X3's geometry rebuilt in own code: 2D Wilson kernel H_W = g5 (D_W - M), M = 1, Lx = 4 PERIODIC in x, open time t in {-3..4},
FREE field (all links 1). Also Lx = 4 ANTIPERIODIC in x, and the torus (antiperiodic t, Lt = 8).
**Readings.** If min|eig H_W| < 1e-6 in the free periodic-x open-time geometry, X3's open-geometry tests used an overlap whose
H_W has exact (Chern edge) zero modes independent of the gauge field; X3's diagnosis "bulk plaquettes up to 0.74" is then wrong, and
T-X3d/e/f/f' and D1 are unreadable as L3g evidence (method wound on X3-E). If min|H_W| >= 0.5 there, X3's diagnosis stands.

## K2-T3: the decisive L3g test (X3's named "next decisive test", made clean)

**Question.** Is the gauge-INVARIANT reflection-positivity kernel of the gauged (vector-like, Dirac) overlap fermion measure PSD at
gauge coupling beta_g = 0, with every plaquette admissible?

**Object.** 2D U(1). Link reflection theta: t -> 1 - t. Lambda+ = {t >= 1}. Observables F = f(U+) (gauge-invariant functions of the
Lambda+ links; finite sets u_1..u_k of Lambda+ configurations stand for f's concentrated on gauge orbits).
Kernel Zt_ab = int dU_c 1_adm(U_c) det D_m[u_a on Lambda+, U_c on crossing links, theta^{-1} u_b on Lambda-],
with theta^{-1}u_b: U_x(x, 1-t) = u_b,x(x, t), U_t(x, -t) = conj(u_b,t(x, t)).
D_m = (1 - m/2) D_ov + m, D_ov = 1 + g5 sgn(g5 (D_W - M)), M = 1, m = 0.05, Wilson r = 1. Control: Wilson D_W + m with the same indicator.
Admissibility: every plaquette (bulk of both halves and crossing) has |arg U_p| < delta. Bulk: by rejection sampling of u's
(links N(0, s^2)); crossing: by the integration domain. The crossing integral is reduced EXACTLY to the gauge-invariant variables
(the crossing-plaquette angles and, on the torus, the temporal Polyakov phase; the pure-gauge zero mode is dropped with constant
Jacobian) and done by rules that converge exponentially for a smooth integrand on the exact domain:
- **G1** open time t in {-3..4}, Lx = 2, x ANTIPERIODIC for fermions: 1D interval, Gauss-Legendre n = 16 and 32.
- **G1'** as G1 with Lt = 12 (t in {-5..6}).
- **G2** open time t in {-3..4}, Lx = 4, x antiperiodic: 3D convex polytope {|d_i| < delta, |Phi - d0 - d1 - d2| < delta}, triangulated
  (scipy Delaunay of its exact vertices), Duffy-collapsed Gauss-Legendre per tetrahedron, n = 5 and 7 (and 9 if needed).
- **G3** torus, antiperiodic t (Lt = 8), Lx = 2 periodic x: two crossing planes; variables = one plaquette per plane (interval, GL)
  and the Polyakov phase (full circle, trapezoid); n = (10, 10, 16) and (16, 16, 32).
Sets: delta = 0.3 with s = 0.12; delta = 0.6 with s = 0.25. k = 8 configurations per set; 3 sets per (geometry, delta).
Measured per set: overlap and Wilson normalized kernels Zt_ab / sqrt(Zt_aa Zt_bb); min eig / max eig; symmetry defect;
q = max |Zt(n_hi) - Zt(n_lo)| (normalized); min |eig H_W| over every evaluated point.

**Readings (fixed now).**
- A set is **clean** iff q < 1e-5 AND min|H_W| > 0.1 at every evaluated point.
- **CONTROL-FAIL** (no reading for that geometry): the Wilson + indicator kernel has min/max < -10 q - 1e-10 in any clean set.
- **FAIL (L3g dead in this formulation):** some clean set with overlap min eig / max < -1e-6 AND |min| > 10 q, with the Wilson control
  PSD (> -10q - 1e-10) in the same set.
- **PASS (necessary condition holds in the tested class):** every set of every geometry is clean and has overlap min/max > -10 q - 1e-10.
- **OPEN:** anything else (unclean sets, or values between the thresholds).
Scope fixed now: PASS covers only vector-like Dirac overlap, gauge-only (vacuum-sector) observables, beta_g = 0, 2D U(1), the
finite configuration sets drawn. It does not test the chiral (Weyl) measure, fermionic observables, non-abelian fields or 4D.

**Diagnostic D-GF (no reading):** on the same configurations, the gauge-FIXED kernel (crossing links = 1, no integral), as X3's
T-X3c/D1, min eig/max reported for overlap and Wilson.

Expectation stated before running: I do not predict the overlap result. I expect K2-T2 to show exact edge zero modes (reason:
H_W is the Qi-Wu-Zhang Chern insulator for 0 < M < 2; at M = 1 its open-boundary edge band crosses zero at k_x = 0, which a
periodic Lx = 4 lattice contains).

---
### Amendment A1 to K2-T3 (2026-10-14, written before any K2-T3 code exists; nothing run)
Reason found while designing (derivation, mine): with fermions present, the hard crossing indicator is NOT a fair control.
Gauge-fix the crossing links to 1 by a slice-1 gauge transformation g (exact for a gauge-invariant integrand); then
Zt(a,b) = int dg W(a^g, b) Det(a^g, b). Wilson's Det is a PSD kernel (Osterwalder-Seiler), but the indicator's Fourier
coefficients c_n = sin(n delta)/(n pi) change sign, and once fermion hops carry charge across the plane the Gauss-law projection
allows unequal n_x, so products of c_n's of mixed sign enter. Wilson + hard indicator is therefore not guaranteed PSD
(X3's character-expansion argument covers only the pure-gauge part).
**Change (primary weight):** each crossing plaquette gets the Fejer triangle weight w(theta) = max(0, 1 - |theta|/delta):
same support (exactly the admissible set |arg U_p| < delta), Fourier coefficients (delta/2pi) sinc^2(n delta/2) >= 0, so the
Wilson control is RP by the standard proof and any failure is the overlap's. Quadrature: domains are split at the kinks of w
(d_x = 0) so every piece carries a smooth integrand (G1/G1'/G3 intervals split; G2 polytope cut into up to 16 convex cells,
each triangulated). The hard indicator is kept as a SECONDARY run on G1 and G3 with the same readings, except that a
Wilson failure there is attributed to the indicator (recorded, not a CONTROL-FAIL of the primary test).
All readings (clean, CONTROL-FAIL, FAIL, PASS, OPEN) and thresholds are unchanged and apply to the primary (triangle) runs.

---
### Follow-up V1 (registered 2026-10-14 15:14Z, AFTER seeing K2-T3 G1p delta=0.6 sets 1-2 negative; readings of K2-T3 unchanged)
Result seen: G1p (Lx=2, Lt=12, open t, antiperiodic x) delta = 0.6, set 1: overlap min/max -7.4e-6 (q 4.8e-15, min|H_W| 0.861,
Wilson +1.1e-5): this meets the pre-registered FAIL line. Before any interpretation, a bug hunt on the SAME configurations:
(V1a) full kernel without symmetry filling (all 64 entries computed), symmetry defect reported;
(V1b) brute-force recomputation by independent code: different site indexing, links assembled explicitly, every plaquette
computed from links (not from the offset formulas), weight = product of Fejer weights of the wrapped crossing plaquettes,
overlap built as X (X^dag X)^{-1/2} with X = D_W - M (not via sgn(H_W)), crossing phase phi_1 on a uniform trapezoid grid
over the full circle (N = 20000 and 40000);
Reading: the FAIL stands as a code-level fact if V1a symmetry defect < 1e-10 and V1b reproduces the negative eigenvalue
(relative) within 10% with the Wilson kernel PSD; otherwise the K2-T3 result is a code artefact and K2-T3 is OPEN.

V1 result (15:18Z): V1a symmetry defect 4.2e-15 (set 1), full-matrix min/max -7.4055e-6; V1b independent code -7.3872e-6
(N = 20000), -7.4005e-6 (N = 40000), converging O(h^2) to V1a; Wilson +1.08e-5. The pre-registered V1 condition holds:
the K2-T3 FAIL line is a code-level fact (same-family check; not an independent referee).

---
### Follow-up V2 (registered 2026-10-14 15:19Z, before writing or running it; K2-T3 readings unchanged)
Robustness of the G1p delta = 0.6 negative eigenvalue (same 3 configuration sets, seed 262), descriptive except where stated:
(V2a) gauge coupling: crossing weight w_beta(d) = tri(d) exp(beta cos d) (positive-type: product of positive-type functions),
beta in {0, 1, 4, 10}. Reading: "weight-robust" if some set keeps overlap min/max < -1e-6 (> 10 q, Wilson PSD) at beta = 1 AND 4;
"weight-dependent" if every set is PSD at beta = 4.
(V2b) operator parameters on set 1: (M, m) in {(1.0, 0.05), (1.0, 0.3), (0.6, 0.05), (1.4, 0.05)}; descriptive.
(V2c) negative control on the Theta convention: Lambda- temporal links NOT conjugated (wrong Theta); Wilson gauge-fixed kernel
(crossing links = 1) min/max reported over 4 sets of 8 rough configurations. If it stays PSD (> -1e-10), the Wilson control has
no power to detect a wrong Theta and the FAIL reading is downgraded to "conditional on the Theta convention".

---
### Follow-up V3 (registered 2026-10-14 15:31Z, after seeing G3 (torus, Lt = 8) delta = 0.6 all PSD and G1 (open, Lt = 8) PSD,
while G1p (open, Lt = 12) failed; K2-T3 readings unchanged)
Question: is the G1p violation tied to the open time ends, or to the larger half-lattice (Lt = 12)?
Object: torus, antiperiodic t, Lt = 12 (t in -5..6), Lx = 2 periodic x (G3p); delta = 0.6, s = 0.25, k = 8, 3 sets, Fejer weight,
n = (6, 8), nw = (10, 16); same clean criteria.
Reading: "not an open-boundary artefact" if some clean G3p set has overlap min/max < -1e-6 and |min| > 10 q with Wilson PSD;
"open-boundary-associated" if all 3 G3p sets are PSD (then the FAIL stands as registered for the open-time formulation only,
and the torus question is OPEN at this sample size).

V2 result (15:30Z, k2v2_robustness.out): (V2a) set 1 stays negative at beta = 0, 1, 4, 10 (-7.4e-6, -7.8e-6, -8.4e-6, -8.5e-6;
q <= 9e-15; Wilson +1.07e-5..+1.19e-5); set 2 likewise (-5.1e-7..-5.7e-7): "weight-robust" reading holds. (V2b) set 1: (M,m) =
(1,0.05) -7.4e-6; (1,0.3) -4.7e-6; (0.6,0.05) -2.0e-5; (1.4,0.05) +6.2e-6. (V2c) wrong Theta: Wilson gauge-fixed kernel
non-Hermitian (1.2e-1) with min/max -3.4e-4; correct Theta -2.9e-15 (PSD to roundoff): the control discriminates.

---
### Follow-up V4 to K2-T1 (registered 2026-10-14 15:33Z, after seeing K2-T1's first blocks; K2-T1 readings unchanged)
Seen: K2-T1 reports worst H0 min/max -1.5e-4..-2.8e-4 at M = 0.5/1.0 and GEVP top-eigenvalue mismatches of 3e-5..3e-3 at
momenta inside Omega. Suspected causes (stated before checking): (1) the p = (1e-3, 0, 0) point has a pole at E ~ 1e-3, so the
N4 = 8192 FFT carries aliasing ~ e^{-E N4} ~ 3e-4; (2) an n = 6 Hankel GEVP cannot resolve a pole lying just above a continuum.
V4: same code, near-zero point moved to p = (0.02, 0, 0) (aliasing ~ e^{-160}); per momentum report H0/H1 min/max; the light pole
located DIRECTLY as the zero of the smallest singular value of D(p4 = iE) on the principal branch (E scanned in (0, E1), refined),
and compared with arcsinh S; GEVP top eigenvalue error reported as a diagnostic only.
Readings: X3-A free claims SURVIVE if, for M in {0.5, 1.0}: H0 and H1 PSD (> -1e-9) at every momentum; a direct pole exists iff
beta < sqrt(1+S^2), with |E_pole - arcsinh S| < 1e-8, and at none of the 7 nonzero corners; no GEVP eigenvalue above
max(e^{-E1}, e^{-E_pole}) + 1e-6; and for M in {1.5, 1.9} negative GEVP eigenvalues only where beta < 0, H0 PSD, H1 indefinite.
If H0 is still indefinite beyond -1e-9 at M <= 1 with the aliasing removed, X3-A's positivity claim is DEAD in my code (then a
convention check against K-U is owed before any conclusion).

V4 result (15:43Z): M = 0.5/1.0 H0, H1 PSD (+6e-15, -5e-17); direct poles agree with Omega at 58/58 momenta, max |E_pole - arcsinh S|
3.6e-9, no corner poles, nothing above the ceiling; M = 1.5/1.9 negative lambda only at beta < 0, H0 PSD, H1 indefinite.
Reading: X3-A SURVIVES (the K2-T1 as-registered H0 negativity was the p = 1e-3 aliasing point, as suspected before checking).

---
### Follow-up V5 (registered 2026-10-14 15:47Z, after seeing G3 and G3p set 0 PSD with LARGE margins (min/max 1e-3..2.5e-2),
whereas open-time kernels were nearly rank-1 (min/max 1e-6..1e-4); K2-T3 readings unchanged)
Reason: a random torus set has a PSD margin ~1e-2, far above the ~1e-5 size of the open-time violation, so it has little power.
Design: CLUSTERED sets, k = 8 configurations = one admissible base (s = 0.25, delta = 0.6) plus independent N(0, 0.05^2) link
perturbations (rejected unless all bulk plaquettes stay < delta). Geometries: G3p (torus, Lt = 12, Lx = 2; n = (6,8), nw = (10,16))
3 sets; and G1p (open, Lt = 12) 3 sets for comparison. Same clean criteria.
Reading: "torus violation" if a clean G3p set has overlap min/max < -1e-6, |min| > 10 q, Wilson PSD (then the FAIL is not an
open-end artefact); "torus PSD at this power" otherwise (the torus question stays OPEN; the FAIL stands for open time ends).
G2 (Lx = 4) is cut to 1 set if time allows (reported as such).

V3 result (15:50Z): G3p (torus, Lt = 12) delta = 0.6: overlap min/max +2.3e-2, +5.8e-3, +1.1e-2 (q <= 3e-15, min|H_W| >= 0.716),
Wilson +2.1e-2, +2.7e-3, +1.0e-2: "open-boundary-associated" reading at this sample size (torus OPEN). Peak RSS 329 MB: OVER the
0.3 GB rule (cause: a 3-operand einsum with a p*N^3 intermediate in lat2d.logdet_batch; fixed at 15:50Z, before V5-G3p and G2).
V5 G1p result (15:50Z): clustered open sets: overlap min/max -1.1e-7, +2.1e-8, -1.7e-7 (q <= 8e-15), Wilson +2.7e-7, +2.6e-7,
+2.0e-7 (descriptive: negatives recur, below the -1e-6 magnitude line).
Note: numpy 2.4 slogdet emits spurious divide/overflow/invalid RuntimeWarnings on these matrices; checked against the sum of
log eigenvalues (agreement 1e-14, min|eig D_m| = 1.39), so values are unaffected.

---
### Follow-up V6 (registered 2026-10-14 15:58Z, after V3/V5 torus PSD; K2-T3 readings unchanged)
Question: does the open-time violation fade or persist as the open ends recede from the plane (toward infinite time)?
Object: open time, Lx = 2 antiperiodic x, Lt in {12, 16, 20} (t in -T+1..T, T = 6, 8, 10), delta = 0.6, s = 0.25, k = 8, 6 random
sets per Lt (new seed 9000 + T), Fejer weight, GL n = (16, 32). Same clean criteria and FAIL line as K2-T3.
Reading: "persists as the ends recede" if a clean FAIL-line set (min/max < -1e-6, > 10 q, Wilson PSD) occurs at Lt = 16 or 20;
"fades" if no set at Lt = 16 and 20 has min/max < -1e-8. Anything else: descriptive.

V5 G3p result (15:59Z): clustered torus sets: overlap min/max +3.5e-5, +2.1e-5, (set 2 +4.8e-5 order; see k2v5_G3p.out), Wilson PSD,
q <= 7e-15, min|H_W| >= 0.776: "torus PSD at this power"; torus question OPEN. Peak RSS 323 MB (over 0.3 GB decimal).
V6 result (16:00Z): open Lx = 2: Lt = 12: 3/6 FAIL-line sets (most negative -2.8e-6); Lt = 16: 0/6 (all > +3e-6);
Lt = 20: 2/6 FAIL-line sets (most negative -3.3e-5, Wilson +3.6e-5 in that set); all clean (q <= 2e-14, min|H_W| >= 0.83).
Reading: "persists as the ends recede" (a clean FAIL-line set at Lt = 20). Peak RSS 313 MB (over 0.3 GB decimal; 299 MiB).

G2 result (16:14Z; time-cut to 1 set): Lx = 4, Lt = 8, open, delta = 0.6: overlap min/max +1.3e-4 (q 7.6e-10, min|H_W| 0.507),
Wilson +1.2e-4: clean, PSD (consistent with G1 at Lt = 8). G2 delta = 0.3 and G3 delta = 0.3 NOT run (time).
