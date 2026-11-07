lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T12:13Z

# p20-gate: referee of b109.md Lemma P20 (depth-uniform quadratic-radius tower estimate (110))

Provenance: Claude Opus 5.5 (claude-opus-5-5), max effort, Mac mini worker, branch claude/ym4d-hard-route at 285da4077. One line-by-line reading by one model. Not an audit, not human review.

**First failing step: none.**

| Statement | Verdict |
|---|---|
| P19, real-point Taylor inequality (109) | ADVANCE |
| P20, quadratic-radius tower estimate (110), under (104) | ADVANCE, as an implication from a1-balaban (8.2), (9.1)-(9.2) and F0 (flat-port), all checked earlier (rows 81, 95), with one line added to the order of constants (finding F1) |
| P15 (72), (74)-(77), the bootstrap P20 reads through section 11.2 | ADVANCE (elementary; re-derived) |
| P1-P14, P16 (apart from the insertion convention of (86)), P17-P18 | not read by P20; not checked here |

No numeric job was run. P19 is elementary, and a run could not test P20's uniformity in depth and volume. No step rests on a computation.

## 1. Scope and what P20 reads

Refereed: `library/b109.md` P19 (lines 3312-3338) and P20 (lines 3340-3456), with premises (104)-(105) (lines 3200-3215) and the ceilings at lines 3342, 3440-3443, 3646-3649.

P20's proof reads these inputs. Of P1-P18 it reads only P15's bootstrap (72), (74)-(77), through section 11.2, and the insertion convention of P16's (86).

- P19 (109), the real-point Taylor inequality.
- (86), P16's Hessian expansion (line 2676), cited for the insertion convention of (111).
- (107), the one-step relative-angle inequality of section 11.2 (a1-balaban section 3.5, actual-mean form section 7.6), for the raw datum increment.
- `a1-balaban.md` (8.2), the real critical-orbit theorem, linear in the datum radius, conditional on F0.
- `a1-balaban.md` (9.1)-(9.2), the uniform datum ball and the holomorphic axial representative, with the second-order (Euler-equation) estimate.
- `a1-balaban.md` (3.6) and section 7, the plaquette-averaging recursion, for the datum radius of a real field.
- `flat-port.md` sections 4-9, which supply F0.
- CA-I 34178-34189 and CA-I (4.8:eq-tower-rules-b), the collar bound, for the interior.

The outline treats the same statement. SA Theorem 5(a), lines 9746-9753, states (110) with K^sharp(alpha_0' + alpha_1'^2). SA mechanism 8, lines 9899-9911, sketches the proof: the P19 inequality without its constant, the plaquette formula (111) as a display, and "Theorem 1 is linear in the datum". So P20 is a proof of a step the outline sketches. It is not a correction of their text.

Source pins: SA `YM4_sketch_500.tex` and CA-I `theorem_0_complete_account_raw_I.tex` at 31a47c543775, fetched to a scratch folder; CMP 109 OCR at `~/ym4d-papers/cmp109.txt`, pp. 262-263.

## 2. P19 (109): ADVANCE

Checked line by line.

- Cauchy on the complex line z -> z w/t, |z| < r: the line lies in the ball, so the degree-m vector coefficient has norm at most H/r^m. For t <= r/2, ||R(w)|| <= H (t/r)^2 / (1 - t/r) <= 2 H t^2/r^2. Correct.
- The same bound holds at u and v, because ||u||, ||v|| <= t when the projections have norm at most one. Correct.
- The identity F(w) = F(u) + i F(v) - i F(0) + R(w) - R(u) - i R(v) follows from F(x) = F(0) + DF(0)x + R(x) at x = u, v, w and complex linearity DF(0)w = DF(0)u + i DF(0)v. I expanded it; it is exact. Correct.
- The triangle inequality then gives (109) with 6 = 3 x 2. Correct.

In P20 the domain space is the complexified bond fields w, with ||w|| = max(sup|w|, sup|nabla_{U_r} w|). Here w_R = (w + w^*)/2 and w_I = (w - w^*)/(2i). In operator norm |w_R|, |w_I| <= |w|. Because U_r is unitary, Ad(U_r) commutes with the adjoint, so nabla_{U_r} commutes with both projections. So both projections have norm at most one in this norm, as P19 requires.

## 3. P20 (110): ADVANCE, step by step

**Input curl (111)-(112). Correct.** I redid the finite product. With W(b) = e^{i eta a(b)} U_r(b),

  dW = e^{X_1} e^{X_2} e^{X_3} e^{X_4} dU_r,  X_1 = i eta a_1, X_2 = i eta Ad(U_1) a_2, X_3 = -i eta Ad(U_1 U_2 U_3^{-1}) a_3, X_4 = -i eta Ad(dU_r) a_4.

The transports are unitary, so |X_r| <= eta |a|. Terms with two or more insertions total at most C eta^2 |a|^2. The transports of a_3 and a_4 differ from those of the ordinary covariant curl by Ad(dU_r). Since |Ad(P)X - X| <= 2|P - I||X| for unitary P, this costs C eta |a| |dU_r - I| <= C eta^3 eps_0 eps_1. This is (111). Then |dW (dU_r)^{-1} - I| = |dW - dU_r| < 2 eps_0 eta^2, because dU_r is unitary. That gives (112). The step uses only |a| < eps_1, the value bound, which matches SA's "without any bound on nabla A'". The real and imaginary parts of d_{U_r}a are d_{U_r}a_R and d_{U_r}a_I, and both have norm at most |d_{U_r}a|. Apply (111) to a_R and to a_I. Then e^{i eta a_R} U_r and e^{i eta a_I} U_r are unitary fields with plaquette defects at most C(eps_0 + eps_1^2) eta^2. Correct.

**Raw datum increment. Correct, with the right citation.** The plain one-step average has a linear part whose row norm can exceed L by terms of order dL, from the endpoint contour sums (P15: "the derivatives of the two u-factors cancel those terms"). So a recursion on plain angles with coefficient L does not hold in general. P20 does not use one. Section 11.2 bounds the *straightened* angles by (107), and the endpoint (node) factors by a summable first-power bound. The same two steps appear in P15 (74)-(77) at a flat reference and in a1-balaban (7.14) at a curved real reference. In tower units (top length 1, t_q <= 1) they give ||a_q|| <= 2|w| t_q and |v_q - 1| <= C|w|, with no factor depending on depth. Hence the plain raw increment B(w), defined by M(e^{i eta_n w} U_r) = e^{iB(w)} M(U_r), is holomorphic and obeys ||B(w)||_inf <= C|w|_inf on a fixed ball. The curved reference needs only *value* smallness in a local gauge, (7.10)-(7.13); (7.11)-(7.14) never read nabla A_0. A coordinate-tree gauge gives that smallness from the curvature of U_r alone (the real case of P21's (114)). So the input is available for every reference U_r in (104).

**Holomorphic ball and crude bound H. Correct.** Take r <= r_B/(2C), where r_B is the uniform raw-datum radius of a1-balaban section 9.1 (gate row 81: ADVANCE, with D3). Then w -> Phi_{V_0}(B(w)), with V_0 = M(U_r), is holomorphic on {||w|| < r}. This is a composition of holomorphic maps in finitely many variables. a1-balaban (9.2) gives r(Phi) <= C(eps_adm + ||B||_inf). In level-n units, top-layer plaquettes and bonds have scale 1. So eta_n^{-2}|dPhi(p) - 1| <= r(Phi) and |J(Phi)(b)| <= r(Phi). This gives the fixed H. The current in a1-balaban is the imaginary part of eta^{-2} D_U^* dU, which is CMP 109 (1.8) with L^{-n} in place of xi, in level-n units, as CA-I 32903-32912 prescribes. The complex conjugators to the axial representative have norm and inverse norm at most exp(C||B||/(1 - L^{-1})). So H is uniform in p, n, Z and volume.

**Real points (113). Correct.** a1-balaban's datum norm is the maximal raw error of its test loops; seam loops use the finer average. Its (8.2) gives |dU(p) - 1| <= B eps eta^2 L(p)^{-2} and |J| <= B eps L(b)^{-3} for every datum radius eps up to the admissible one. So it is linear in the datum radius, with B fixed before depth and volume. The curvature recursion (3.6), with its actual-mean form in a1-balaban section 7.1, uses only plaquette defects of a unitary field. In level-n units it gives: a real field with fine defects delta eta^2 = delta s^2 eta_n^2 has level-q test errors at most 2 delta s^2 t_q^2 (times L^2 at seams). So the datum radius of U_r is at most C eps_0 s^2. For e^{i eta a_R} U_r and e^{i eta a_I} U_r it is at most C(eps_0 + eps_1^2) s^2. At real w the increment B(w) is real and lies in the r_B ball. Orbit uniqueness and the unique axial gauge (a1-balaban section 9.1, last paragraph) identify Phi_{V_0}(B(w)) with the real critical representative at that datum. Curvature and current norms are invariant under unitary gauges. This proves (113) with C = C(L) B.

**Application of P19. Correct.** In tower units, ||sa|| = max(s|a|, s^2 |nabla_{U_r} a|) <= s eps_1. With eps_1 <= r/2, P19 gives |F(sa)| <= 3C s^2 (eps_0 + eps_1^2) + 6H s^2 eps_1^2 / r^2. This is the current bound of (110) with K = 3C + 6H/r^2. Multiplying the plaquette version by eta_n^2, with eta_n s = eta, gives the curvature bound. K is made of a1-balaban's B, C(L), r_B and the dimension constants of (111). It does not depend on eps_1/eps_0, p, n, Z, the torus, M, kappa or gamma.

**Interior. Correct.** By the definition of collar(r) (CA-I after 4.8:eq-tower-rules-a), a point of Z farther than collar(r) L^n steps from Z^c lies in Omega_n. A point of Z^{wr p} lies at least 2 M L^{p-1} steps from Z^c (two layers of pi_{p-1} cubes, CA-I 4.8:eq-cube-lattices-b). With collar <= R_1 M_1 and M >= 2 L R_1 M_1, the margin at the worst case n = p is at least 3 R_1 M_1 L^n steps. So Z^{wr p}, with the bond-and-six-plaquette current stencils, lies in the top layer. This matches CA-I 34178-34189.

**The U_r clause.** Set a = 0. Then |F(0)| <= C eps_0 s^2, which is the real (1.17) with constant C(L)B. Correct.

## 4. Ceilings and order of constants (lines 3342, 3440-3443, 3646-3649)

P20 says only "sufficiently small individual radii". The ceilings it actually uses are two, and both are fixed by early constants. Notation: r_B is the raw-datum radius of a1-balaban 9.1. eps_adm is the admissible datum radius of a1-balaban 8 (written eps_1 there). (C_B, r_*) are the constant and radius of ||B(w)|| <= C_B |w|, from a1-balaban (7.14) and P15 (75)-(77). alpha_* is the curvature ceiling of the averaging recursion, (3.6) and (7.12)-(7.13). C_1 = C(L) is the constant of (111)-(112) times the seam factor L^2.

- Fix r := min{r_*, r_B/(2 C_B)}.
- (i) eps_1 <= r/2. This serves P19 (t = s eps_1 <= r/2). It also gives eta eps_1 <= 1 for the series in (111), and keeps the real increments inside the r_B ball.
- (ii) C_1 (eps_0 + eps_1^2) <= min{alpha_*, eps_adm/2}. This puts U_r's datum strictly inside the admissible radius, and the data of e^{i eta a_R} U_r and e^{i eta a_I} U_r in the range of (8.2).

Neither ceiling depends on eps_1/eps_0, p, n, Z, the torus, M, B^(109), kappa or gamma. The term eps_1^2 enters (ii) only as a ceiling on eps_1. No relation between eps_0 and eps_1 is imposed. Lines 3440-3443 and 3646-3649 are therefore correct, and conservative: the ceilings may be fixed before M and B^(109), not only after them.

Order: L; the block letter 𝔐; F0 constants (flat-port); a1-balaban's B, r_B, eps_adm, localization length and gap; R_1 (finding F1); M_1 = R_*' 𝔐; then K = 3C + 6H/r^2 and the two ceilings; then M >= 2 L R_1 M_1 and B^(109); then the account's radii; gamma last. This agrees with the order in `gates/l17c-gate.md` (its section "Constant order"). No step closes a cycle.

## 5. Findings (none breaks P20)

**F1. Order of constants: one premise to add (repairable, no new proof).** P20 claims uniformity "in both tower rules" through a1-balaban sections 8-9. That theorem holds on separated sequences whose gap is fixed *after* the localization length R_1M_1 of a1-balaban (6.3)-(6.5) (its M_1 is Balaban's block letter, CA-I's 𝔐). Its gate, D2, says the gap must exceed four lengths, about 6L times that localization length. CA-I's rule r_1 has gap exactly R_1 𝔐 L^q (CA-I 32877). Rule r_2 has gap R_*' 𝔐 L^q >= R_1 𝔐 L^q. So P20 needs CA-I's gap number R_1 to be at least a1-balaban's gap, in units of 𝔐. CA-I fixes R_1 only by one-sided floors ("sufficiently large", R_1 >= L, R_*' >= R_1), and M_1 and M come after it. So the repair is one line: choose CA-I's R_1 after a1-balaban's localization length, at least its D2 gap. The letter R_1 denotes two different constants here: a1-balaban's localization factor and CA-I's gap number. If they are read as one constant, the D2 condition cannot hold for r_1.

**F2. Premise (105) is not used.** No step of P20 reads the real cube-gauge clause. The averaging bootstrap needs only value smallness of U_r in a local gauge, which a coordinate-tree gauge gives from curvature (section 3 above). a1-balaban's datum class is defined by test loops alone. So P20 holds under (104) alone, with the floor M >= 2 L R_1 M_1 that the interior step uses. Dropping (105) makes the statement stronger and breaks nothing.

**F3. Convention scope (remark).** P20 is proved for the default determining set, with inward bonds free. This is the setting of SA Theorem 5 (SA 9625), and the only one a1-balaban covers (its section 10). b109 section 11.1 fixes it ("the actual default determining sets, including their outward rows"). CA-I 32901-32902 defers the tower's data sets to Balaban's Lambda_q. SA 9625 notes that CMP 96 and 119 keep the level-0 inward bonds. A consumer of (110) must read the tower in the default convention. This bears equally on L17 and on every consumer of (1.17).

**F4. Which object T_n is (remark).** b109 defines T_n as the axial representative of the regular critical orbit, and for complex data its analytic branch. a1-balaban proves existence and uniqueness of that orbit, not minimality. CA-I 32896 calls U_n^r "the axial-gauge minimiser" of CMP 102 Theorem 1. The two coincide when the minimal orbit is regular. That clause of CMP 102 Theorem 1 is cited, not rebuilt; this is outside P20.

**F5. Citations (cosmetic).** P20 cites (86), the Hessian expansion, for the insertion convention. The finite product expansion (111) is proved in place and does not need (86). "The argument in (107)" means section 11.2's straightened recursion together with the node-factor bound. A recursion on plain angles with coefficient L would be false (section 3).

## 6. What this changes

- L17C's corrected L17 (`gates/l17c-gate.md`: ADVANCE given P20) now rests on a checked P20. The corrected L17 holds as an implication from a1-balaban sections 8-9 (row 81) and F0 (`flat-port.md`, row 95), both checked line by line by Claude on Codex text. It also needs F1 here and finding 1 of the l17c gate. Q119 of `library/b119.md` is the same statement as L17, so it inherits the same resolution.
- Kind (How we work, item 9): a check of our proof of a step the outline sketches. SA Theorem 5(a) is stated at SA 9746-9753 and sketched in SA mechanism 8 (9899-9911). This is not a correction of their text. P20 writes out mechanism 8 with its constant 6, the plaquette expansion, and the inputs "Theorem 1 is linear in the datum" (a1-balaban (8.2)) and the uniform holomorphic ball (a1-balaban (9.1)-(9.2)).
- Still open: the eps_0-only L17, CMP 109 (1.17) at complex pairs as CA-I 34067-34072 and 34153-34163 use it. P20 neither proves nor refutes it. The example in b109 section 11.4 shows that the hypotheses do not force eps_1^2 <= C eps_0. Also still open: F0's own provenance (CMP 89, 95, 96, as rows 81 and 95 record) and a1-balaban's (10.2).

Credit: Tadeusz Balaban for the minimizer, averaging, gauge and continuation arguments (CMP 98, 99, 102, 109). Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for Theorem 5(a) and the real-point argument of mechanism 8 that P19-P20 write out.

Checked line by line by Claude (Mini worker).
