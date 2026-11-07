lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-03T02:50Z

# floor-screen: the outline's floor screening (SA L18334-18415)

Queue row 83. Anthropic claude-opus-5-5, effort max, Mac mini worker, started
2026-11-02T14:50Z, folder pinned at branch commit `98cf31942`. Same-model reading
and proof; not a gate, not an audit, no status.

Sources and credit. Ethan Sussman and Levent Alpoge (with Claude and Codex as
authors of their text), `YM4_sketch_500.tex` at `31a47c543775` (sha256
`d7f77d4d...4d6f`, read from a local clone; "L" numbers are lines of that file):
floor screening L18334-18415, Lemma 2.5 (4) L17709-17715, drop-out evaluations
L18130-18205, the stages of R L17575-17630, (1b) Theorems 1, 2, 6 L9660-9686,
L9776. T. Balaban, CMP 102 (1985) 277-309 (Theorem 1 p. 279, Section F and
Proposition 8 pp. 300-305, Proposition 9 pp. 305-309) and CMP 99 (1985) 389-434
(Theorems 3.1-3.3), read from `~/ym4d-papers/` (outside git, not copied). Our
`library/a3-response.md`, `gates/a3-gate-b2c312b2e.md`, `library/route-decisions.md`.
No numerics: the question turned out to be structural (memory was 56 percent free;
no job was started).

## 0. Result

**Moves:** `library/route-decisions.md` position H (Package C, rank 1) and its first
reversal test (4.3, first bullet).

1. **"Arbitrary data in the floor": false, and not the outline's hypothesis.**
   With an arbitrary floor datum the localized background need not exist
   (Example 1: one bare plaquette at -1 in a layer-0 part of the floor; no
   configuration is regular at any radius below 2, so by totality every test that
   reads the background fails, also far outside the floor, with zero energy
   outside it). The outline never asks for this: Lemma 2.5 (4) (L17709) and the
   drop-out fibre (L18149-18151, L17831 "Second") take the old-core datum regular
   at C R_l^2 eps_l, and it is so on the supports (Lemma S, checked here for the
   regions the label makes).
2. **No heavy wall can act on the background.** For a fixed term, the stage
   background reads only the datum on its determining set and the shape of its
   sequence (Lemma O). Everything large in the floor (the bare field, the averages
   of the next level that failed their tests, the stored fluctuation fields, the
   complement of Omega_0) is off the determining set and has exactly zero
   influence. What is on it is regular (Lemma S). So the reversal test as worded
   in route-decisions 4.3 cannot fire. Its honest residue is uniformity of the
   background estimates in the shape of the floor's regions, which is a clause of
   A3 (the outline claims it at L9658).
3. **The screening estimate is an implication, proved here (Theorem R):** it
   follows from the outline's (1b) Theorem 1 (A1: one regular critical orbit) and
   (1b) Theorem 2, first half (A3 in profile form) on the stage sequences of R,
   with Theorem 6 (a) (those sequences are separated) and the energy of averages,
   plus elementary steps written in full here (geometry of the collar, Lemma G;
   thresholds of deep floor layers, Lemma T, which are controlled by asymptotic
   freedom alone; the comparison of the two terms). Rate delta_0 = L delta_P,
   where delta_P is the profile rate of (1b) Theorem 2.
4. **Defects in the outline's text, none breaking:** the display L18355-18361 is
   stated "outside the floor"; it is proved, and available in general, only at
   weighted distance at least L M R_{m_b} - 4 from the floor, that is where the
   operation acts (the form L17715 states); in the waiting collar next to the floor
   no argument gives it, and no renewed test reads it there. Two provisos are
   unstated (the width of "a margin of Y", L17317; the flow bounds of g-bar,
   L6031). Section 6.
5. **Balaban.** CMP 102 Theorem 1 is A1 with global bounds and no locality;
   Proposition 8 is a global halving, which alone gives only the floor's size
   C R^2 eps in the window. But its proof (Section F, (160)-(167)) is already local
   in the datum: the datum enters on the cube around the point, and the rest enters
   through a tail with an explicit factor e^(-delta_0 R_1 M_1 / 2). Only its
   quadratic term and its iteration are global. Section 5 gives the port-ready
   one-step statement (OS-loc) and the elementary iteration (Lemma I) that turn
   that proof into what Theorem R reads; for the screening the quadratic term may
   stay global. Proposition 9 (190), the derivative decay, rests on (189), which
   Balaban did not carry out (p. 308). CMP 99 Theorems 3.1-3.3 supply the linear
   propagator decay at regular backgrounds.
6. **What stays open:** (1b) Theorem 1 on stage sequences, uniform in depth (row
   81, pending); (1b) Theorem 2 first half, or (OS-loc), on the same sequences
   (row 82 and `a3-response.md` Section 8 item 3, pending); (1b) Theorem 6 (a) for
   the stage sequences; the energy of averages (L18206-18336, argued there,
   unchecked here); the support regularity inside regions changed by earlier R
   operations (the outline's claim, not checked here). No new obligation: Package
   C's two top items (floor screening, 2.8) both reduce to the outline's Theorem 2
   with Theorem 1, which our seam chain also needs.

## 1. The statement

Setting (outline (2a)-(2c), my notation where it has none). The operation R acts at
level m on a class component X of Z_m with preparation bottom m_b = m - N_m,
N_m = R_m (L17575). Write R_j for the outline's check-R_j, the smallest power of L
not below (log min_{i<=j} x_i)^r, r >= 2 (L17334), and l_j = log x_j (L18016 with
the frame theta = x). Thresholds: eps_j = g_j p_0(g_j), p_0(g) = A_0 (log g^-2)^p0
(L6029-6031, L17257); varsigma = C g_m l_m^(p1-4r) (L18349). Cells of level j are
M R_j-cubes of T^(j) (L17459); Omega_j and every large-field region are unions of
cells of their level (Proposition 2.3).

- O = Omega_{m_b}^c intersected with X, the old core (L17709).
- F, the floor: the level-m_b cells of O that do not touch Omega_{m_b}.
- W_c = O minus F, the waiting collar (one cell wide).
- S: a stage or prepared sequence of R, localized in X (L17612, Theorem 6 (a));
  B_S its determining set, V its datum, d_S its weighted distance (L9602),
  U-hat = U_S(V) its background ("stage background").
- A test loop tau of V (L9616) has a level l(tau) and a bare support (the union of
  the blocks under its bonds). T_F: the test loops whose bare support meets F;
  T_far: all others.

**(FS), as the outline states it (L18353-18366).** If the unspent Wilson, gauge and
stored Gaussian energy in the new window is below c l_m^(2p1-8r), then for every
stage background, "outside the floor",

    |dU-hat(p) - 1| <= C (varsigma + R_m^2 eps_m e^(-delta_0 M R_m)) L^(-2 j(p)),

using "a collar of fixed positive width in its own local units and the
weighted-distance background estimate. It does not require a small field inside
the floor." L17715 states the same bound "where the operation acts", that is on
X intersected with Omega_{m_b}.

**(FS*), the form proved in Section 4.** Same conclusion for every bare plaquette p
all of whose corners lie in Omega_{m_b} (in local units, |dU-hat(p) - 1| is
compared with eta^2 L(p)^-2, which is L^(-2 j(p)) in bare units), under the data
hypotheses

- (D-far) |dV(tau) - 1| <= varsigma for tau in T_far;
- (D-F) |dV(tau) - 1| <= C_F R_{l(tau)}^2 eps_{l(tau)} for tau in T_F.

(D-far) is what the energy of averages gives from the small unspent energy
(input (EA), Section 3); (D-F) is the regularity of the old-core datum (Lemma S,
and by definition in the drop-out evaluation fibres, L17831 "Second", L18149).

## 2. Arbitrary floor data: false; and why no heavy wall acts

**Example 1 (the strong reading fails).** Let a level-0 part of the stage sequence
lie in F (allowed: Omega_0 = Omega_1-tilde has a layer-0 margin, L17317, and no
condition restricts the shape of members, L9599). In layer 0 every bare bond is a
determining bond and M^0 U = U, so a test loop all of whose bonds lie in Gamma_0 is
a bare plaquette p of every compatible U: dU(p) = dV(p). Put V(b) = -1 on one such
bond (and 1 elsewhere); then dV(p) = -1 for the plaquettes containing b, and every
compatible U has |dU(p) - 1| = 2. Regularity at radius a in layer 0 asks
|dU(p) - 1| < a eta^2 L(p)^-2 = a. So for every a < 2 the regular critical orbit is
empty, the localized background does not exist, and by totality (L17346) every
test that reads it equals 0, including bond tests far outside the floor, while
U = 1 off the floor has zero energy there. Decay "for arbitrary data in the floor"
is therefore false already at existence. This datum is on no support (Lemma S).

**Lemma O (what the stage background reads).** For a fixed term (fixed history,
hence fixed regions and fixed sequence S), U-hat depends on the field variables only
through the datum V on B_S.

*Proof.* By definition (L9607-9616) U-hat is the regular critical orbit of
A_{Omega_0} = sum of a_p over plaquettes in Omega_0^S on
C(B_S, V) = {U on Omega_0^S : M_{B_S}(U) = V}; localization in X replaces the data
on the collar bonds of X by the lift of V (Theorem 6 (c), L9776), again a function
of V. Neither the constraint set nor the action reads any other variable. QED.

So the bare field in the floor, the averages V_{l+1} = M(V_l) that failed their
level-(l+1) tests (they lie in Omega_{l+1}^c, which no bond of Gamma_{l+1} reaches,
L9607), the stored fluctuation fields A' (level l-1 variables under the level-l
datum on the strip) and anything outside Omega_0^S have zero influence on U-hat.
The heavy wall of the reversal test can act only through the datum, which is
regular (Lemma S), or through the shape of S, against which A3 must be uniform.

**Lemma S (support regularity of the old-core datum; checked for label regions).**
On the support of a term, every test loop tau of the label's datum V_l on Gamma_l
(l < m_b) satisfies |dV(tau) - 1| <= C L^2 eps_l, C absolute.

*Proof.* tau has a bond of Gamma_l, hence an endpoint in Omega_l (L9607), so tau
lies within one level-l spacing of Omega_l. By L17320,
Omega_l^c = Q_l'^~2 u P_l'^~4 u Yhat^~8 (layers in level-l cells), so every cube on
which the level-l plaquette test failed is at least four level-l cells from
Omega_l, and Omega_l is at least eight cells from the old live region Y, outside a
margin of which that test is made. Reading "a margin" as at most four cells (the
outline gives no width; this is my reading), the plaquette test was made and
passed on the cubes that contain tau. A passed test gives a regular localized
background on the cube whose averages are V_l there (L17317), and the
converse at the end of (1b) Theorem 1 (L9667; Balaban CMP 98 Proposition 2, cited
at CMP 102 p. 278, unchecked here) bounds the test loops of the averages by
2 eps_l inside a layer and C L^2 eps_l across a seam. QED.

Inside regions changed by earlier R operations (healed boxes, drop-outs) the
outline asserts the envelope C R_l^2 eps_l (L17709, L17828, L18197-18199); healed
boxes carry the cut-off |log V'| < M_0 eps_k (L17604), so their test loops are
small too. I did not check those cases line by line; the drop-out masses impose
the envelope by definition of the evaluation fibre.

## 3. The inputs Theorem R reads

- **(A1-S)** [(1b) Theorem 1, L9660, on the sequences of Theorem 6 (a)]. There are
  eps-bar > 0 and C_1 (depending on L) such that for every stage or prepared
  sequence S of R localized in X and every real datum V on B_S whose test loops all
  lie within eps_1 <= eps-bar of 1, the critical configurations of C(B_S, V) that
  are regular at a fixed small radius form exactly one non-empty orbit, regular at
  radius C_1 eps_1. *Status:* fixed-geometry A1 proved (row 79,
  `library/a1-orbit.md`); uniformity in depth pending (row 81); Balaban CMP 102
  Theorem 1 for his torus sequences, with global bounds (Section 7).
- **(A3-P)** [(1b) Theorem 2, first half, L9678]. There are a_P > 0, C_P and
  delta_P > 0 (depending on L) such that for every S as above and every critical
  U in C(B_S, V) regular at radius a_P, at each bare plaquette p with corner x,
  eta^-2 L(p)^2 |dU(p) - 1| <= C_P max_tau e^(-delta_P d_S(x, tau)) |dV(tau) - 1|.
  *Status:* unproved; not in Balaban (row 80; Section 7 here); the common next
  target named in `library/a3-response.md` Section 8 item 3; pending row 82.
  Section 5 gives a one-step form (OS-loc) that suffices.
- **(S1)** [structure of the stage sequences: my reading of L17585-17612 and of
  Theorem 6 (a), L9776; unchecked]. (a) S is separated in the sense of L9599, so
  (A1-S) and (A3-P) apply to it. This is consistent with Proposition 2.3 (L17398):
  stage and prepared sequences are unions of M-cubes with gaps of at least one
  M-cube of the later level, that is M L xi_j, which exceeds the gap
  rho xi_j = R_1 M-frak xi_j once M > R_1 M-frak / L; the order of choice allows
  this, since M is fixed after M-frak and R_1 (L9599). (b) The core C_{m_b} = X n Z_{m_b} is never
  unfolded (L17598), so on O the sequence S is the label's sequence: every point
  of O lies in an S-layer j <= m_b - 1 or outside Omega_1^S; and Omega_0^S lies in
  X-tilde (X with one layer of level-m M-cubes), where X-tilde minus X lies in
  Lambda_m, inside Omega_{m_b} (other components of Z_m are a level-m cell away,
  and an M-cube is smaller than an M R_m-cell).
- **(EA)** [energy of averages, L18206-18336 with Lemma 2.5 (i), L17690; argued in
  full there from one stated one-step inequality, `library/sa-map.md` Section 3
  item 6; unchecked here]. If the unspent Wilson, gauge and stored Gaussian energy
  in the new window is below c l_m^(2p1-8r), every test loop of the stage datum
  whose bare support carries no floor plaquette has |dV(tau) - 1| <= varsigma.
  The plaquettes spent before the wait lie in F (L18338-18341; checked against the
  margins of L17320: old live regions are 8 level-m_b cells inside Omega_{m_b}^c,
  failed plaquette and approximate tests 4 and 2 cells, and a share reaches one
  cell), so these supports use only unspent plaquettes. This gives (D-far).
- **(SUP)**: Lemma S, with the outline's envelope for regions changed by earlier R
  operations. This gives (D-F) with C_F = max(C L^2, the outline's C).

## 4. Theorem R (the screening, given the inputs)

**Lemma T (deep levels have smaller thresholds).** Assume the frame's flow bounds
x_q >= x_q' - C_fl for q <= q' (the hypothesis -C <= x_q - x_q' <= C (q' - q) of
Theorem 5 (c), L9767, which (2e) imposes on admitted frames, L7470), and
eps_j = A_0 g_j (log x_j)^p0 with g_j = x_j^(-1/2) (L6031 writes g-bar_j; I assume
g-bar obeys the same flow bounds). There is x_* = x_*(C_fl, r, p0) such that
x_m >= x_* implies, for every l <= m,

    R_l^2 eps_l <= 4 L^2 R_m^2 eps_m.

*Proof.* Put s = 2r + p0 and phi(x) = x^(-1/2) (log x)^s; phi is decreasing on
[e^(2s), infinity), since phi'/phi = (s / log x - 1/2) / x. As min_{i<=l} x_i <= x_l,
R_l <= L (log x_l)^r, so R_l^2 eps_l <= L^2 A_0 phi(x_l). The flow bound gives
x_l >= x_m - C_fl >= e^(2s), so phi(x_l) <= phi(x_m - C_fl) <= 2 phi(x_m) once x_m
is large. Also min_{i<=m} x_i >= x_m - C_fl, so
R_m^2 eps_m >= A_0 x_m^(-1/2) (log(x_m - C_fl))^(2r) (log x_m)^p0 >= (1/2) A_0 phi(x_m)
once x_m is large. QED.

So the deep layers of the floor cost nothing: asymptotic freedom makes their
thresholds smaller. The allowance (1 + a)^(1/2) of L17624 and L17831 concerns the
opposite comparison and is not needed here.

**Lemma G (the collar in the weighted distance).** Assume (S1). If x lies in
Omega_{m_b} and tau is in T_F, then l(tau) <= m_b - 1 and
d_S(x, tau) >= L M R_{m_b} - 4.

*Proof.* Let s = M R_{m_b} xi_{m_b}, the side of a level-m_b cell; xi_{m_b - 1} =
xi_{m_b} / L.
(i) dist_inf(F, Omega_{m_b}) >= s: both are unions of closed cells of one grid of
side s (Proposition 2.3, L17398; cells, L17409), and no cell of F touches one of Omega_{m_b}; two
closed grid cubes that do not touch differ by at least 2 in some index, hence are
at l_inf-distance at least s.
(ii) Level. By (S1b), O misses Omega_{m_b}^S, and Omega_{m_b}^S lies in X-tilde
minus O, which is inside Omega_{m_b}. A test loop of level j has its bonds in
Gamma_j^S or, at a seam, reads averages of level-(j-1) blocks next to
Omega_j^S (L9607, L9616); since members are unions of cubes aligned with their
blocks (L9599), its bare support lies within l_inf-distance xi_{j-1} of
Omega_j^S. For j >= m_b + 1 that neighbourhood lies in Omega_{j-1}^S (the gap
exceeds rho xi_{j-1}), hence in Omega_{m_b}; for j = m_b it lies within
xi_{m_b - 1} < s of Omega_{m_b}. Either way it misses F by (i). So tau in T_F has
level l <= m_b - 1.
(iii) Distance. Every point of tau is within 3 xi_l <= 3 xi_{m_b - 1} of its
support, which meets F; so dist_inf(tau, Omega_{m_b}) >= s - 3 xi_{m_b - 1}. Let
Gamma be a lattice path from x to tau and Gamma' its part after its last point in
Omega_{m_b}. Gamma' lies in Omega_{m_b}^c and has length at least
s - 4 xi_{m_b - 1}. A point of Omega_{m_b}^c either lies in O, hence in an S-layer
j <= m_b - 1 or outside Omega_1^S (S1b), or lies outside X-tilde, hence outside
Omega_0^S; in each case its weight in d_S (L9602) is at least 1 / xi_{m_b - 1}.
So the weighted length of Gamma is at least L M R_{m_b} - 4. QED.

**Theorem R.** Assume (A1-S), (A3-P), (S1), and (D-far), (D-F) for the stage datum
V. There is g_* > 0, depending on L, C_F, M, A_0, p0, p1, r, C_fl, C_P, delta_P and
the constant C_v of varsigma = C_v g_m l_m^(p1-4r), such that if g_m <= g_*:

(a) the stage background U-hat exists (exactly one regular critical orbit);
(b) for every bare plaquette p with all corners in Omega_{m_b},
    eta^-2 L(p)^2 |dU-hat(p) - 1|
      <= C_P max{varsigma, 4 L^2 C_F e^(4 delta_P) R_m^2 eps_m e^(-L delta_P M R_m)};
(c) the second entry is at most varsigma.

So (FS) holds where the operation acts, with delta_0 := L delta_P and
C := C_P (1 + 4 L^2 C_F e^(4 delta_P)).

*Proof.* Step 1 (the datum is regular). By (D-far), (D-F) and Lemma T every test
loop of V lies within eps_1 := max{varsigma, 4 L^2 C_F R_m^2 eps_m} of 1. Both
entries tend to 0 with g_m (R_m <= L l_m^r and eps_m = A_0 g_m l_m^p0, with
g_m = e^(-l_m / 2)). Choose g_* with eps_1 <= eps-bar and C_1 eps_1 <= a_P.

Step 2 (existence). (A1-S) gives one regular critical orbit, regular at radius
C_1 eps_1 <= a_P; this is (a), and (A3-P) applies to it.

Step 3 (profile). Fix p and a corner x of p. By (A3-P),
eta^-2 L(p)^2 |dU-hat(p) - 1| <= C_P max_tau e^(-delta_P d_S(x, tau)) |dV(tau) - 1|.
For tau in T_far the term is at most varsigma (D-far). For tau in T_F, by (D-F),
Lemma T and Lemma G, it is at most
C_F R_l^2 eps_l e^(-delta_P (L M R_{m_b} - 4)) <= 4 L^2 C_F e^(4 delta_P) R_m^2 eps_m e^(-L delta_P M R_m),
using R_{m_b} >= R_m (R is non-increasing in the level, L17334). This is (b).

Step 4 (the second entry is below varsigma). The flow bound gives
(l_m / 2)^r <= R_m <= L l_m^r for small g_m. The ratio of the second entry to
varsigma is therefore at most
(4 L^4 C_F e^(4 delta_P) A_0 / C_v) l_m^(6r + p0 - p1) exp(-L delta_P M 2^(-r) l_m^r),
which tends to 0 as l_m tends to infinity since r > 0. Lower g_* until it is at
most 1. QED.

*What is used and what is not.* No uniqueness beyond (A1-S), no holomorphy, no
second half of Theorem 2; (A3-P) is used only at weighted distance at least
L M R_{m_b} - 4 from the floor, and only to damp the floor's datum. The collar
enters only through Lemma G. The statement is about real fields, as the tests are.
The remaining links of the renewed-test argument (L18367-18397: the shell-loop
holonomy bound, and |log V'(b)| <= C M^2 R_m^2 varsigma < delta'_m; the last holds at
small coupling, since C M^2 R_m^2 varsigma <= C' M^2 L^2 g_m l_m^(p1-2r) while
delta'_m = A_1 g_m p_1(g_m) is of order g_m l_m^p1, L17585) are as in the outline
and were not rechecked line by line.

## 5. A port-ready one-step form, from Balaban CMP 102 Section F

Theorem R reads the whole profile bound (A3-P). The screening needs less, and the
shape of what it needs is already in Balaban's proof of his Proposition 8.

*Notation.* For a top y of S-layer j let Delta(y) = B^j(y) and let box(y) be
Balaban's big cube around it: side 2 R_1 M_1 xi_i, contained in the two adjacent
S-layers i and i + 1, with i = j or j - 1 (CMP 102 pp. 278-279 and p. 302). Its
d_S-diameter is at most 8 R_1 M_1, since weights in layer i + 1 are smaller. For a critical U regular at radius eps_0, let r_U(y) be the least
r >= 0 with |dU(p) - 1| <= r eta^2 xi_j^-2 and |D* dU(b)| <= r eta^2 xi_j^-3 on
Delta(y) (his space (2)). Let a(y) = max |dV(tau) - 1| over the test loops in
box(y). For kappa > 0 and f >= 0 on tops, (T f)(y) = sup_y' e^(-kappa d_S(y, y')) f(y').

**(OS-loc), proposed, unproved.** There are kappa > 0, B_3, C_Q, a_5 > 0 (depending
on L) such that for every S as in (A1-S), every critical U in C(B_S, V) regular at
radius eps_0 <= a_5, and every f with r_U <= f <= eps_0,

    r_U(y) <= max{B_3 a(y), (1/2) (T f)(y)} + C_Q eps_0^2   for every top y.

*What Balaban proves.* CMP 102 (158)-(169), pp. 302-305: r_U(y) <= max{B_3 eps_1,
(1/2) eps_0}, with operators at U = 1 (p. 302: "all the operators in this section
are taken without any external gauge field configuration", from CMP 95, 96). In
his (160)-(161) the datum enters only on box(y) (he uses (7) only there), and
everything outside box(y) enters through a tail
sum_{y2 outside box} e^(-delta_0 d(y1, y2) / 2) (d(y1, y2) + 1) ... eps_0, whose
prefactor (162)-(163), B_3 e^(-delta_0 R_1 M_1 / 2) <= 1/2, produces the 1/2. His
quadratic term (165), B_0 (C_4 + 4 C_2)(36 d L^2 B_1 eps_0)^2, is our C_Q eps_0^2;
he absorbs it as eps_0 / 8 using (166). So (OS-loc) is his step with two changes:
the global datum bound becomes a(y) (no change in the argument), and the tail's
eps_0 becomes T f (the real change).

*The one real point of the port.* Balaban bounds the far datum in a generalized
axial gauge centred at y, by eps_0 times the length of a comb path. To put T f in
its place one needs, for z on the comb path from y to y2, d_S(y, z) <= d_S(y, y2) +
const. With several local scales this fails in general: a comb path can cross a
finer layer that a d_S-geodesic goes around. So the port must work in local gauges
on cubes, patched (our gated Lemma U, `library/lattice-uhlenbeck.md`; Lemma P of
`library/a3-response.md` with the gate's repair), which is what the outline's 1b.5
says it does (L9795: "uses only operators at 1"). The quadratic term may stay
global, as the next lemma shows.

**Lemma I (weighted halving; proved).** Assume (OS-loc) for U, and
B_3 sup a + C_Q eps_0^2 <= eps_0 and 2 C_Q eps_0 <= 1. Then
r_U <= B_3 T a + 2 C_Q eps_0^2.

*Proof.* Put Q = C_Q eps_0^2, f_0 = eps_0, f_(n+1) = max{B_3 a, (1/2) T f_n} + Q.
(i) r_U <= f_n <= eps_0 for all n: true at n = 0 since U is regular at eps_0; if
true at n, (OS-loc) with f = f_n gives r_U <= f_(n+1), and
f_(n+1) <= max{B_3 sup a, eps_0 / 2} + Q <= eps_0 by the two provisos.
(ii) T is monotone, commutes with max, satisfies T(u + c) <= T u + c for constants
c >= 0, u <= T u (as d_S(y, y) = 0) and T T u <= T u (triangle inequality for d_S).
With A = B_3 a + 2Q, induction gives f_n <= max{T A, 2^(-n) eps_0 + 2Q}:
f_(n+1) <= max{B_3 a + Q, (1/2) max{T T A, 2^(-n) eps_0 + 2Q} + Q}
        <= max{A, (1/2) T A + Q, 2^(-n-1) eps_0 + 2Q} <= max{T A, 2^(-n-1) eps_0 + 2Q},
because A <= T A and 2Q <= A <= T A. Letting n tend to infinity in (i),
r_U <= max{T A, 2Q} = T A <= B_3 T a + 2Q. QED.

**Corollary R'.** Theorem R holds with (OS-loc) in place of (A3-P): for g_m small and
every top y in Omega_{m_b},
r_U-hat(y) <= B_3 max{varsigma, e^(kappa (4 + 8 R_1 M_1)) 4 L^2 C_F R_m^2 eps_m e^(-L kappa M R_m)}
              + 2 C_Q eps_0^2 <= (2 B_3 + 1) varsigma,
so (FS) holds where the operation acts with delta_0 = L kappa.

*Proof.* Take eps_0 = (C_1 + 2 B_3) eps_1 with eps_1 as in Step 1 of Theorem R;
U-hat is regular at C_1 eps_1 <= eps_0, and the provisos of Lemma I hold for small
g_m since sup a <= eps_1. Apply Lemma I at y. For y' whose box contains a loop of
T_F, a(y') <= 4 L^2 C_F R_m^2 eps_m (Lemma T, (D-F)) and
d_S(y, y') >= L M R_{m_b} - 4 - 8 R_1 M_1 (Lemma G, the triangle inequality and
the diameter of box(y')); for the other y', a(y') <= varsigma. The quadratic term: eps_0 <= C R_m^2 eps_m, so
2 C_Q eps_0^2 / varsigma <= C g_m l_m^(8r + 2 p0 - p1) -> 0. Step 4 of Theorem R
handles the second entry. QED.

So the screening needs exactly: (A1-S), (OS-loc) (Balaban's Section F step with a
weighted tail, in local gauges), (S1), (EA), (SUP). It does not need the quadratic
term localized, nor the second half of Theorem 2, nor Theorems 3-5.

## 6. Defects (ranked by what they break)

1. **`library/route-decisions.md` 3.3 ("Against") and 4.3 (first bullet) read the
   floor's data as arbitrary** (evidence for that file's owner). The outline's
   hypothesis is regularity at C R_l^2 eps_l of the old-core datum (L17709; the
   drop-out fibre, L17831 and L18149). The arbitrary version is false (Example 1)
   and unused; the heavy wall cannot be built on a support (Lemmas O, S). Breaks:
   the first reversal test as worded can never fire. Repair (for the lead): restate
   it as "(1b) Theorem 2, first half, or (OS-loc), fails on a stage sequence of R
   with datum regular at C R^2 eps", which is the third bullet of 4.3.
2. **Display L18355-18361, "outside the floor".** Proved here, and in general only
   available, at points of Omega_{m_b} (L17715 states it there); in W_c next to F
   the profile gives only C_P C_F R^2 eps. Breaks nothing, provided each renewed
   test reads the stage background only on Omega_{m_b}. As far as I read them they
   do: the stage tests are on shells outside the core (L17585 (1)); the main-step
   field B lives on the shells (L17598); the extension test reads the exterior field
   (L17585 (2)); the last-shell test uses another background, U_{k_b,box}((1, V_{k_b})),
   whose datum lies outside the core (L17598-17604).
3. **Lemma S proviso.** The width of "a margin of Y" outside which the step's
   plaquette test is made (L17317) is not given; Lemma S needs it at most seven
   level-l cells (Omega_l is eight cells from Y). Repair: state the width.
4. **Lemma T proviso.** The thresholds are written with g-bar_j (L6031); Lemma T
   needs g-bar to obey the frame's two flow bounds. If it is another running
   coupling, rerun Lemma T with its own bounds.
5. **Rate naming.** The display's delta_0 is the (1c) propagator rate elsewhere in
   the text; here it is L delta_P (Theorem R) or L kappa (Corollary R'). Constants
   only.

No defect found in the structure of the argument: the floor/collar margins
(L17320 against the shares of L17702) keep the spent action inside F, and
the second term of the display is below varsigma at small coupling (Step 4).

## 7. What Balaban supplies, exactly

- **CMP 102 Theorem 1 (p. 279).** For a datum V with all test loops within
  eps_1 < a_1 of 1 on the whole determining set ((7), p. 278), a minimal orbit in
  the space (8), unique critical orbit in (6) if B_3 eps_1 <= eps_0 <= a_0, with
  local bounds (9)-(10) of size B_3 M eps_1 on cubes. Geometry: Omega_j unions of
  big blocks of side M_1 L^j eta, gaps (L^j eta)^-1 dist > R M_1, torus. Every
  bound is in the global eps_1: this is (A1-S) for his sequences, with no
  locality. Applied to the stage background it gives curvature C eps_1 =
  C R_m^2 eps_m in the window, which is too large for the tests by the factor
  R_m^2 eps_m / varsigma, a positive power of l_m.
- **CMP 102 Proposition 8 (p. 304) and its proof, Section F (pp. 300-305; the
  step itself is (154)-(169), pp. 302-305).** Global
  halving eps_0 -> max{B_3 eps_1, eps_0 / 2}. As shown in Section 5, the proof is
  local in the datum ((160) uses (7) on the cube only), weighted in the tail
  ((161), (163)), global only in the quadratic term (165) and in the iteration.
  This is the source to port for (OS-loc).
- **CMP 102 Proposition 9 (p. 309) and (190) (p. 308).** The derivative of the
  background (Landau gauge) in the datum decays like e^(-delta_0 d(y, y') / 2). Its
  input (189) is introduced with "We do not perform these calculations here"
  (p. 308). Using (190) for the screening would also need a path of regular data
  from a floor-free datum to the actual one with small increments; with deep fine
  layers in the floor a regular datum has large holonomies on large loops, so a
  straight path in one gauge leaves the polydisc of Proposition 9 (my reading; not
  pursued).
- **CMP 99 (389-434) Theorems 3.1-3.3 (pp. 397-399).** The operators G'(U), G(U)
  and their derivatives at a configuration regular in the sense (3.35) obey local
  bounds with exponential decay in the weighted distance (2.36) of CMP 96, uniform
  in the sequence; proofs by random-walk expansions over a cover of the torus.
  These are the linear inputs at curved backgrounds. The outline needs them for an
  arbitrary first member Omega_0 and proposes a separate parametrix argument
  (L9795 onward).

## 8. Open, and what the lead may change

**Open, hardest first.**
1. (OS-loc), or (A3-P), on the stage sequences of R: the halving in local form
   with a weighted tail, in local gauges (Section 5). Row 82, and
   `library/a3-response.md` Section 8 item 3. The quadratic term may stay global
   for this use.
2. (A1-S) uniform in depth on those sequences: row 81 (port of CMP 102 Theorem 1).
3. (S1): Theorem 6 (a) for the stage and prepared sequences, and the reading that
   the core is never unfolded. Geometry; cheap; no queue row yet.
4. (EA), the energy of averages (outline L18206-18336): argued there, unchecked here.
5. (SUP) inside regions changed by earlier R operations, and the two provisos of
   Section 6 items 3-4.

**What moved.** Position H of `library/route-decisions.md`: (i) its rank-1 open
step (3.2 item 1) is an implication from (1b) Theorems 1, 2 (or (OS-loc)) and 6 (a)
with (EA), proved here with every other step written; it adds no analytic
obligation, so Package C's two top items (floor screening and 2.8, whose stop is
(L)) both rest on the outline's Theorem 2 with Theorem 1, the same statement our
own seam chain needs. (ii) Its first reversal test cannot fire as worded (Section 6
item 1). (iii) The "Against" worry of 3.3 about arbitrary floor data is settled.
Row 82 gets a precise, smaller target, (OS-loc), with its source in Balaban.

**For the lead to forward (I edit no other file).** In `route-decisions.md`: 3.2
item 1 relabelled "implication from A1, A3 profile (or OS-loc), Theorem 6 (a), EA:
`library/floor-screen.md`"; 3.3 "Against", the sentence on arbitrary floor data,
replaced by Section 2 here; 4.3 first bullet restated as in Section 6 item 1.
Ledger rows "1b Theorem 2 / 1b.5" and "New-mark payment, L18334" of
`library/sa-ledger.md` can point here.
