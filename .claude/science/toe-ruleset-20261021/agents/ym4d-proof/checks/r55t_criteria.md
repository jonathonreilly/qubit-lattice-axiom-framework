# r55t criteria (REVIEW55_TENT, batch C7) — written BEFORE any r55t script exists

Author: Opus 5.5 reviewer (claude-opus-5-5). Exact arithmetic only: python3 -I, fractions.Fraction and
ints; no numpy, no BLAS, no floats in any verdict. Logarithms only via rigorous rational intervals
(atanh series with an explicit remainder bound). Every constant below is QUOTED from the file whose
claim is under test (file named); none is derived in this review. A FAIL is reported as a FAIL; no
criterion is edited after a script exists; any re-run gets a new id; anything run after seeing a
result is labelled post-hoc.

Conventions (from the sources, not from the reviewed workers' scripts, which are NOT read or run):
d* of 1-forms and 2-forms as BFT_A l.1872; (d lambda)(z,mu) = lambda(z+e_mu) - lambda(z); Q_str as
BFT_A l.599; slice functional h as LINEAR_PACKAGE §1.2 (ORDER-AVERAGED over the 4! orders and
y in B(Y); paths stay in the block); a fixed-order variant h^(0123) is computed ONLY for the
collision test T6; level-l roots centred, off(l) = (L^l - 1)/2, level-(i+1) block of Y = L*Y + [0,L)^d
in level-i coordinates, its root = L*Y + (L-1)/2; ev = restriction to roots; Phi_k as BFT_A §38.3 /
YSUP §1.0: Phi_k(v)(X) = sum_{i<k} h_i(Q_str^{(0->i)} v)(root of X as a level-(i+1) site).
Quintic tent as BFT_B l.2024. Infinite lattice Z^d with finite supports (everything is local).

## Part A — funnel, d = 4, L = 3 (claims of TENTQ §2.8(iii), YSUP §2.3(ii), FACEB §4.2/§5.5)
Witness u := (1/8) d*delta_p, p the (0,1)-plaquette with base corner c_X + (1,0,0,0).
- A1 PASS iff, with ORDER-AVERAGED h at k = 2: phi_1 = -1/432, phi_2 = -17/104976 and
  Phi_2(u)(X) = -65/26244 exactly (quoted: REVIEW_BFT_A_S8 l.45, YSUP l.229-233). Else FAIL.
- A2 PASS iff at k = 3 and k = 4 the same phi_1, phi_2 and phi_i = 0 for i >= 3, so that
  Phi_3(u) = Phi_4(u) = -65/26244 exactly (YSUP "terminates"; Codex FACEB R2). Else FAIL.
- A3 PASS iff Phi_k(d delta_{c_X})(X) = 3^{-4k} - 1 exactly at k = 1, 2, 3 (Codex FACEB R4; YSUP
  ys1 A5 quoted -80/81, -6560/6561). Else FAIL.
- A4 (measurement for T6, pre-registered reading). Compute the h_0 kernel on one block for both
  operators: max|c| and sum|c|. Quoted values: COFUN §3 max = 1/3, sum = 8/3 (fixed order);
  YSUP §2.1(b) "(10/81)" and Codex FACEB "W(0,mu) = 10/81" (order-averaged). Reading fixed in
  advance: if max_avg != max_fixed, T6 is a REAL collision and COFUN's "sharp 1/3" is sharp only for
  the fixed-order operator. A4 PASS iff sum|c| = 8/3 for BOTH operators (both files agree on 8/3).
- A5 (measurement for T6). phi_1, phi_2, Phi_2(u) with the FIXED-ORDER h. Reading fixed in advance:
  if they differ from A1's, the exact witness constants are operator-dependent.
- A6 DESIGNED-FAIL CONTROLS. (a) roots at block corners (off(l) := 0): A1's equality must FAIL.
  (b) witness without the 1/8: A1's equality must FAIL (phi_1 then -1/54 if A1 passes).
  A6 "fires" iff both corrupted runs fail A1. A non-firing control is reported as such.
- A7 PASS iff h_0(d lambda)(Y) = mean_{B(Y)} lambda - lambda(root) exactly, for 5 pseudo-random
  integer lambda, for BOTH operators, and Q_str(d lambda) = d(A lambda) one step (block average A)
  exactly on the same lambda. (Independent check of the implementation, not of a reviewed claim.)

## Part B — TENTQ Proposition QFALSE (§2.3, §2.2(a)); d = 4 at k = 1, 2 and d = 2 at k = 1, 2, 3
j_0 := sign(d chi^5_{X0}) (sign 0 := 0), D := d* j_0, D_perp := D off the level-k roots.
- B1 PASS iff ||d chi^5_{X0}||_1 = 2d n^{d-1} exactly (TENTQ §2.2(a); BFT_B §25.1(f)).
- B2 PASS iff Q_{X0} := sum_z chi^5_{X0}(z) D(z) (box sum, a different code path from B1) equals
  2d n^{d-1} exactly.
- B3 PASS iff max|D| = 2d exactly (tq1b's "= 2d"; TENTQ §2.3 needs only "<= 2d").
- B4 PASS iff R := |<chi^5_{X0}, D_perp>| / (n ||D_perp||_inf) >= n^2 - 1 (TENTQ §2.3's claim);
  R is reported exactly. (Restricting max_X to X0 gives a lower bound on the max.)
- B5 PASS iff sum_X chi^5_X = 1 at every site of a window containing the support (sanity).
- B6 DESIGNED-FAIL CONTROL: tent scale n-1 instead of n. B1 must FAIL; fires iff it fails.

## Part C — the bootstrap algebra (FACEB FB-BOOT; GESIGN GS-WINDOW; Codex FACEB R1)
y = a + z + G y, row sums of |G| <= eps < 1; A = ||a||_inf, B = ||z||_inf, M = ||y||_inf.
- C1 PASS iff a = (1,1), z = 0, G = [[0,-1/2],[0,1/2]] gives y = (0,2) exactly (Codex R1's
  pointwise example; also the degenerate point of GS-WINDOW).
- C2 PASS iff for 200 pseudo-random exact instances (size 4, eps in {1/2, 1/4, 1/10}) every
  instance satisfies M >= (A - B)/(1 + eps) AND M <= (A + B)/(1 - eps). (A theorem; the check
  guards the reviewer's algebra.) Any violation is a FAIL.
- C3 PASS iff scalar G = -1/2, z = 0 gives y = (2/3) a exactly (sharpness of 2/3).

## Part D — arithmetic on quoted constants
- D1 PASS (for Codex's "rounded the wrong way") iff 0.0024768 > 65/26244 exactly; report the
  difference exactly (Codex quoted 89/2050312500).
- D2 PASS iff (1/54)/(130/6561) = 243/260 and (1/54)/(65/26244) = 486/65 and
  (1/432)/(65/26244) = 243/260 exactly.
- D3 PASS iff (1/3)*sum_{i=0}^{k-1} 3^{3(k-i)} = (9/26)(n^3 - 1) for k = 1..6, and 0.3462 > 9/26;
  report 0.3462 - 9/26 exactly (Codex quoted 3/65000).
- D4 PASS iff 8*65/26244 = 130/6561.
- D5 With rigorous rational intervals for log10(3) and log10(307/125) (DX' = (307/125)e-152,
  C_Omega = 1, C_SR omitted, as FACEB §6.3 freezes them): D = 152 - log10(307/125);
  k* = (3 + D/log10 3)/2; k*_double = (3 + D/(2 log10 3))/2. D5 PASS iff the k* interval lies in
  [160.37, 160.39] and the k*_double interval lies in [80.93, 80.95]. FACEB's 81.7 is REFUTED iff
  the k*_double interval is disjoint from [81.65, 81.75].

## Part E — top-level root charges (target T7), d = 2, L = 3, k = 1, ORDER-AVERAGED root map
Q := Q_str - d o h (LINEAR_PACKAGE §1.2), one step level 0 -> level 1.
- E1 PASS iff Q(d lambda) = d(ev lambda) exactly for 5 pseudo-random integer lambda on all level-1
  links whose stencil lies in the window (validates the implementation of Q).
- E2 (the claim under test is GESIGN GS-BASE's reading "Xi^T N_B = 0 identically ... (CC-0) holds
  exactly", with N_B = kappa Q^T B_k). For B a single level-1 link (not co-closed), S := Q^T B,
  D(S) := d*S. GS-BASE's reading PASSES iff D(S) == 0 at every level-0 site. It FAILS iff D(S) != 0
  somewhere. Also report whether D(S) = ev^T d*B exactly (transposed root covariance) and whether
  D(S) vanishes off the level-1 roots (i.e. the source is (cc)).
- E3 CONTROL: B := the boundary of one level-1 plaquette (co-closed at level 1). Expected D(S) == 0;
  E3 PASS iff D(S) == 0 everywhere (shows E2's root charges are exactly d*B, not an artefact).

## What these checks cannot decide (stated in advance)
No response field Y^p is computed; nothing here is evidence about Phi_k(Y^p_{*,0}) or about the
actual (TENT-osc). Part E is abelian and linear: it tests the cited linear identities' scope, not
the nonabelian remainder. k <= 4 throughout: nothing here measures a level count.
