# Check of row 1439 (`library/gap-mech-candidate3-astra62.md`)

Checker: Claude Opus 5.5 (laptop subagent, row 1441). Started 2026-11-23T19:02Z (date -u).
Note checked was written by gpt-6.2-astra max (row 1439).

## Plan

Read the note in full, then check items 1 to 9 of the row 1441 brief in order,
by hand and with small exact-rational computations in /tmp (outside the repo).
Read supporting sources only where a step relies on them. Read the Lean
statements from the generator source; do not run Lean. Append each finding as
it is made.

## Findings

Line numbers refer to `library/gap-mech-candidate3-astra62.md` as read at 19:02Z (188 lines).
Scratch computations: `/tmp/chk1441/num.py`, `/tmp/chk1441/env.py` (floating point, used only as sanity
checks of hand-verified inequalities; none is a proof step).

### Item 1. Lemma 1 (line 54-58). HOLDS.
- On spin j, dimension d=2j+1, the unit-S^3 Laplacian has eigenvalue -(d^2-1). So (1-Delta)^{-1} has
  multiplier 1/d^2, the Frobenius commutator multiplier. K_p has 1-p+p/d^2 = (1+(1-p)(d^2-1))/d^2, which is
  (1-(1-p)Delta)/(1-Delta). Checked.
- K_p^{-1} = (1-Delta)Q_{1-p} = [I - p Q_{1-p}]/(1-p), since (1-Delta) = [(1-(1-p)Delta) - p]/(1-p).
  So the residual is (F - pQ_{1-p}F)/(1-p). Q_u = int_0^inf e^{-t} e^{utDelta} dt is a probability
  convolution, so the formula is continuous and mass preserving. Uniqueness: all multipliers of K_p are
  nonzero. With F and Q F continuous, residual >= 0 iff (1) pointwise. Checked.

### Item 2. Lemma 2 (lines 60-73). HOLDS.
- J = sum_{k>=1} p^k (I-N)^k, ||I-N||_TV <= 2, so ||J|| <= 2p/(1-2p) <= 4p for p <= 1/4. Checked.
- Degree: a link lies in 6 plaquettes, each with 3 other links: D <= 18. Checked.
- Changing links in A moves at most 6|A| plaquette factors, each with log oscillation 2 beta: 12 beta|A|.
  So |v_A| <= (4p e^{12beta})^{|A|} = q^{|A|}, q <= 4/(16*19^2) = 1/1444 = 1/[4(D+1)^2]. Exact. Checked.
- Factorization: no plaquette meets two components, so the weight ratio is a product over components, and
  the product signed measure integrates it factorwise. Checked.
- Recursion: for A containing e, the component C of e and A' = A - C with A' disjoint from N[C]; this is a
  bijection, and v_A = v_C v_{A'}. Checked.
- Induction: Lambda - N[C] is reached from Lambda - e by at most (D+1)|C| single deletions inside sets
  strictly smaller than Lambda; each ratio <= (1-eps)^{-1}. (1-1/(2n))^n >= 1/2 by Bernoulli gives 2^{|C|}.
  Checked.
- Count: a closed walk of length 2(k-1) along a DFS of a spanning tree, each step to one of <= D
  neighbours, recovers the vertex set: <= D^{2(k-1)}. Sum = 2q/(1-2D^2 q) = 1/398 <= 4q = 1/361 <= eps = 1/38
  (exact fractions). Checked.
- Z_E F = (prod K_e^{-1})F, positive, mass one. Centre signs and positive mixtures: oscillation unchanged and
  the residual is linear in F. Checked.

### Item 3. Straight products (line 75). HOLDS, one wording note.
- g_1U_1 g_2U_2 ... = g_1 (U_1 g_2 U_1^{-1}) ... (U_1..U_b). Given the residual links the conjugates are
  independent, each with law K because K is central. The coarse factor is K^{*b}, independent of the
  residual. Checked.
- R_j = (⊗K)*D_{2^j}R: D_2 R_j = (⊗K^{*2})*D_{2^{j+1}}R = (⊗K)*R_{j+1}. Checked. Wording note: for
  j >= 1, R_j is not the blocked Wilson law; the blocked law is (⊗K^{*(2^j-1)})*R_j. The claim "one fresh
  copy per doubling with a positive residual" is true for the chain R_j as defined. Not a defect.

### Item 4. Theorem 3, (4)-(7a) (lines 79-125). HOLDS.
- (4) ordinary: matches gap-solve4 (23) (line 310-312 there: C_t <= C, trace Hoelder, min-max). Neutral
  extension: normalized single-bond multipliers are I_{h+1}/I_1-type and nonnegative (GL3), constant one, so
  Haar projection <= convolution; tensor, compression and the same sandwich preserve order; layers commute
  with centre flips; P_0 restricts to an invariant subspace; |Tr prod T_s| <= prod ||T_s||_{N_t} <= Tr T^{N_t}.
  Deleted plaquettes are temporal and off the seam. Checked.
- z(beta) >= 8 e^{-1/2}/(3 pi^3) beta^{-3/2}: Haar density (2/pi) sin^2, sin t >= 2t/pi for t <= 1. Checked
  (numerically z(1)=0.416 vs bound 0.052).
- A_m(r): bi-invariant triangle inequality on peeled boundary words; pair averaging valid because every pair
  sum is <= r <= pi, where cos u + cos v <= 2cos((u+v)/2). Checked.
- Six faces of a temporal coarse edge are temporal, have distinct fine plaquettes (periods >= 3b). (5):
  Markov with (4); G^c contained in the union of {angle_i > eps/2}. Checked.
- (6): sign averaging gives cosh >= 1, so word density >= Haar-commutator law/(c_A c_B) >= e^{-l}/2, using
  w(theta) = s/(2 sin s) >= 1/2, s = pi-theta. U within eps of -S_1 on G forces all angles >= pi-2eps since
  d(-g,h) = pi - d(g,h). G is a function of the other coarse links, same law before and after the decision.
  Limits: log z/beta -> 0. (3) follows. Dominated branch: p <= Pr(G^c) + 2e^l Pr(E)/v_eps, exponentially small,
  exponent not (3). Checked.
- (7): b=1 gives -6*2 = -12; (2) gives the matching lower bound; neutral via centre-sign mixture. b=2:
  6*4*(1-cos(pi/4)) = 24-12sqrt2 = 7.03; with l=2beta, 5.03 > 0. Checked.
- (7a): conditional density >= p/2 (the e-marginal is unchanged by the e-convolution). At the identity
  background the six incident plaquettes give e^{6beta x}/c(6beta); continuity and full support make the
  pointwise statement valid; the neutral mixture has the same conditional there. Cap x >= 1/2 has mass
  1/3 - sqrt3/(4pi) = 0.1955 > 1/8; p <= 16e^{-9beta} <= 16e^{-18} < 16^{-5} = 2^{-20} (e^3 > 16.375 > 16).
  Checked.
- Informal sentence, line 119: "with only polynomial sensitivity of the proposed coupling gain" is not
  defined or proved; it is a remark, not part of the theorem. The 2p matrix-coefficient bound is correct.

### Item 5. Proposition 4 (lines 129-143). HOLDS.
- Word mean in the fundamental: I/4; thinned: (1-3p/4)I; [A,B]^{-1} has the same law, so orientation of the
  boundary links does not matter. Conditioning on the residual bounds |E x(U_C)| by the product. Checked.
- c(beta) = 2I_1/beta, r = c'/c = I_2/I_1 (via I_0 = I_2 + 2I_1/beta). Multiplier of C_w at degree h is
  c I_{h+1}/I_1; that of C_{xw} - rC_w is c d/dbeta[I_{h+1}/I_1]. Each I_{j+1}/I_j is the mean of t under the
  tilt of (1-t^2)^{j-1/2}, derivative = variance. Checked. One-plaquette step: Tr(T^{k-1}(T'-rT)) >= 0.
- Rectangle inequality from 1434 (lines 79-85 there; check 1436 item 3): W(2,2) >= W(1,2)^2 >= W(1,1)^4,
  second step monotone because W(1,2) >= W(1,1)^2 >= 0. Checked.
- Neutral fundamental reorientation (line 139). I re-derived it. With time = original i, the 0i stack is the
  only electric one; the 0j, 0k stacks are constant in new time and become static magnetic sectors (transfer
  stays positive). The 0i seam bit inserts the projection for flipping the original-time links at t_0 in the
  new slice; this flip preserves all new-spatial plaquettes (each 0j/0k plaquette carries two such links). Moving
  the stack flips only 0-links, which the (i,j) loop does not use. The transporter along j uses no 0-links, so
  J intertwines the projection for m = 1. Sector weights are partition masses independent of r; Jensen on the
  joint index. Both reorientations use original spatial directions. Checked. This is new relative to check
  1436 item 4, which needed even m because the temporal-loop case can flip loop links.
- r(2) >= 3/7: I_1/I_2 = 4/beta + I_3/I_2, and I_{n+1}/I_n <= beta/(2n+2) termwise from the positive series
  (I verified this directly; the GL4 index row does not display the bound). r is increasing. Numerically
  r(2) = 0.4331. 1-3p/4 >= 3/7 gives p <= 16/21. Checked; the bound holds for all beta >= 2, not only the band.
- Even character: chi_h chi_2 contains chi_h once for h >= 1; degree-0 ratio I_3/I_1;
  I_1/I_3 = 1 + (4/beta)(6/beta + I_4/I_3) <= 3/2 + 24/beta^2 <= 15/2 (numerically 7.477 at beta=2).
  (2/15)^4 = 3.2e-4 > (1/9)^4 = 1.5e-4. Checked.

### Item 6. Proposition 5 and the Lean statements (lines 147-167). HOLDS.
- Geometry: the prism [i,2i] x [0,j] x [0,2] has 10 faces; minus the outer strip: 2 pushed + 2 + 2 temporal
  over the other three edges + 2 spatial caps = 8. Four signed j per i. Checked by hand and by the Lean
  statements below.
- M(pi): with u = pi-2x, A_2(u) = 2(1-sin x), A_2(2x) = 2(1-cos x), 4A_8(2x) = 32(1-cos(x/4)) >= 2(1-cos x)
  by |sin 4y| <= 4|sin y|. Total >= 6 - 2sin x - 4cos x >= 6-2sqrt5. Numerical minimum 1.5313 >= 1.5279.
  Truncation at u is valid (A_m increasing, all arguments <= pi). Checked.
- Chessboard: site-plane RP with conditional independence given plane links; (Ef)^2 <= E(f theta f); doubling
  allowed while width <= P/2, final P/2^s < 2H per direction, so V/k <= (2H)^4; strict containment is
  inherited, copies disjoint; numerator <= 1 with a >= 0; small-ball Z_per >= (c_1 beta^{-3/2})^{4V} e^{-48V}.
  Polynomial in beta, uniform in periods. Periods >= 16 make H = 8 <= P/2. Checked.
- Neutral factor 8: L_{1-s} = L_s^* from M_{2-t} = M_t, C_{1-t} = C_t, so the circle product is B^*B;
  Tr(P_0 B^*B) <= Tr(B^*B); denominator Tr(P_0 T^N) = (1/8) sum of 8 positive twisted partitions >= Z/8.
  Checked. Margin: 36-12sqrt5 = 9.17 > 8. Checked.
- Lean statements (generator read in full; SHA-256 of generator 5900b68a...0370 matches; I regenerated
  Star.lean in /tmp/chk1441/gen with python3 -I, SHA 56d86edf...df2a matches; 24 detour theorems, 30
  #print axioms, no sorry or native_decide; Lean not run, per brief).
  - `patches i` = inner strip + outer strip + four detours; `allKeys` over six rays; length 216 = 6 x 36.
  - `key` = lower corner + sorted axes identifies the unoriented plaquette; `maskSound` derives Nodup of keys
    from distinct bit positions, which is sound whatever faceCode does off range.
  - `detour_*`: length 8; `sameBoundary` = equality of boundary 1-chains; `wordTest` = the glued boundary
    words agree up to cyclic rotation. `splice` replaces an edge e of the word by the three edges following
    e-bar in the new face, i.e. multiplies the holonomy by a conjugate of the face holonomy; free reduction
    and end cancellation preserve the conjugacy class. So the angle of the outer-strip loop is at most the
    sum of the detour face angles. This is exactly what M(r) uses, with the trivial planar step
    hol(face) = hol(inner) x conj(hol(outer)).
  - Coordinates span width <= 4 in each axis, so periods >= 16 give no identification. Hand step, correct.
  The Lean statements say what the proof uses.

### Item 7. Equation (9) (lines 171-179). HOLDS.
- Chart: 4 int x(U_p)^2 = 1; cross terms vanish because each unit plaquette and the 2x2 loop have an
  unpaired edge (inner cross links or one shared edge). Constants have zero coefficient. So every fine plaquette
  coefficient is beta. Checked.
- Lemma 2 with the 8-link loop as an extra factor: degree <= 25, oscillation 12beta + 2eta,
  p = e^{-12beta-2eta}/(16*26^2) gives q = 1/(4*26^2). Checked.
- x(V_C) is a coarse function, so it pulls out of D_2; the coarse links are product Haar; difference is
  4 eta * 1/4 = +-eta. eta = 1/4 > (log 2)/4 = 0.173. Checked. Scope: comparison inputs with a non-plaquette
  term; the statement is correctly limited to "no sign from these data".

### Item 8. Two-phase separation and five tests (lines 181-183). HOLDS as scoped.
- Lemma 2 holds at any beta, so a common p for both labelled components gives a label-independent factor and
  positive residuals; the finite-size Perron statement is taken from check 1387 (not re-derived here). The
  conclusion is limited to that comparison class. Correct.
- (t1), (t3): U(1) commutator trivial; SU(2) adjoint 1/9; SU(d) irrep d^{-2}. Checked.
- (t2) five-dimensional claim (8 faces, four alternatives each, cost >= 8(6-2sqrt5)): plausible by the same
  plane argument; disjointness in 5D is not Lean-checked and I did not check it in detail. Not load-bearing.

### Item 9. Judgement.
- The note does not move (M-neutral). It closes a class: independent thinned Haar-commutator multipliers
  (and Wilson-tilted words with bounded concentrations) on straight-product links. Precisely: bare
  p_* = e^{-12beta+o(beta)} (both directions proved); b = 2 word branch with concentrations <= 4beta each is
  O(e^{-c beta}); band beta >= 2: bare p <= 2^{-20}, doubled spatial square common p <= 16/21; (9): thinning plus
  fine plaquette coefficients fix no coarse sign; two-phase: a common factor at every doubling does not imply
  (M-neutral), (N-phys) or (W) in that comparison class. The class is stated precisely in Theorem 3 and
  Propositions 4-5; the only imprecise sentence is the line-119 remark on "polynomial sensitivity".
- Note on relevance: on the target trajectory beta grows like log n, so the large-beta exponents apply; the
  bare factor is e^{-12beta}, negligible there. (3) weakens like 3pi^2/b^2 for large b, which the note does
  not claim otherwise.
- Next row 2 (line 188): well posed after fixing that "full plaquette cost" means all plaquettes with all
  four vertices in X and that the six faces are those of the coarse temporal edge at the origin. Upper
  bound 72-12sqrt26 = 10.81 re-derived (spatial links 1; 12 centre-neighbour and 60 neighbour-outside temporal
  plaquettes). Feasibility: the J <= 10 side is cheap to certify if such a field exists. The J > 10 side needs
  a global lower bound for a nonconvex SU(2) problem. The simplest certificate (angle subadditivity plus the
  convex envelope of 1-cos, tangent point 0.810) evaluates to 9.79 at the known abelian field and 9.71 over its
  one-parameter family, both below 10, so that relaxation cannot decide it. A decisive J > 10 needs
  nonconvex branch-and-bound or a sharper relaxation; feasibility is uncertain. Either outcome only refines the
  closed class (4beta to 5beta); it does not move (M-neutral).

## Verdict

HOLDS. No failing line. Verified by hand: Lemmas 1-2, straight products, Theorem 3 with (4)-(7a), Proposition 4
including the fundamental neutral reorientation, Proposition 5 including the chessboard and neutral factor 8,
(9), and the Lean statements (by reading; hashes reproduced). Not verified: the finite-size two-phase estimate of
check 1387 (taken as cited), the five-dimensional remark in (t2), the Lean run itself (not run, per brief), and
row 1434's one-plaquette and rectangle proofs beyond what check 1436 records. Wording notes only: R_j (line 75)
is an auxiliary chain, not the blocked law; line 119's "polynomial sensitivity" sentence is informal.
