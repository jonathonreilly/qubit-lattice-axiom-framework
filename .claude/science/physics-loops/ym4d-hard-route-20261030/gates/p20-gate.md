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
| P1-P14, P16-P18 | not read by P20; not checked here |

No numeric job was run. P19 is elementary, and a run could not test P20's uniformity in depth and volume. No step rests on a computation.

## 1. Scope and what P20 reads

Refereed: `library/b109.md` P19 (lines 3312-3338) and P20 (lines 3340-3456), with premises (104)-(105) (lines 3200-3215) and the ceilings at lines 3342, 3440-3443, 3646-3649.

P20's proof reads these inputs. None of P1-P18 is read by P20.

- P19 (109), the real-point Taylor inequality.
- (86), the perturbed-plaquette expansion of P16 (line 2676), for (111).
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

**Raw datum increment. Correct, with the right citation.** The plain one-step average has a linear part whose sup-norm can be about (d+1)L, because of the endpoint contour pieces. So a recursion on plain angles with coefficient L would be false. P20 does not use one. Section 11.2 bounds the *straightened* angles by (107), and the endpoint (node) factors by a summable first-power bound. The same two steps appear in P15 (74)-(77) at a flat reference and in a1-balaban (7.14) at a curved real reference. In tower units (top length 1, t_q <= 1) they give ||a_q|| <= 2|w| t_q and |v_q - 1| <= C|w|, with no factor depending on depth. Hence the plain raw increment B(w), defined by M(e^{i eta_n w} U_r) = e^{iB(w)} M(U_r), is holomorphic and obeys ||B(w)||_inf <= C|w|_inf on a fixed ball. The curved reference needs only *value* smallness in a local gauge, (7.10)-(7.13); (7.11)-(7.14) never read nabla A_0. A coordinate-tree gauge gives that smallness from the curvature of U_r alone (the real case of P21's (114)). So the input is available for every reference U_r in (104).

**Holomorphic ball and crude bound H. Correct.** Take r <= r_B/(2C), where r_B is the uniform raw-datum radius of a1-balaban section 9.1 (gate row 81: ADVANCE, with D3). Then w -> Phi_{V_0}(B(w)), with V_0 = M(U_r), is holomorphic on {||w|| < r}. This is a composition of holomorphic maps in finitely many variables. a1-balaban (9.2) gives r(Phi) <= C(eps_adm + ||B||_inf). In level-n units, top-layer plaquettes and bonds have scale 1. So eta_n^{-2}|dPhi(p) - 1| <= r(Phi) and |J(Phi)(b)| <= r(Phi). This gives the fixed H. The current in a1-balaban is the imaginary part of eta^{-2} D_U^* dU, which is CMP 109 (1.8) with L^{-n} in place of xi, in level-n units, as CA-I 32903-32912 prescribes. The complex conjugators to the axial representative have norm and inverse norm at most exp(C||B||/(1 - L^{-1})). So H is uniform in p, n, Z and volume.

**Real points (113). Correct.** a1-balaban's datum norm is the maximal raw error of the test loops, with a seam factor L^2. Its (8.2) gives |dU(p) - 1| <= B eps eta^2 L(p)^{-2} and |J| <= B eps L(b)^{-3} for every datum radius eps up to the admissible one. So it is linear in the datum radius, with B fixed before depth and volume. The curvature recursion (3.6), with its actual-mean form in a1-balaban section 7.1, uses only plaquette defects of a unitary field. In level-n units it gives: a real field with fine defects delta eta^2 = delta s^2 eta_n^2 has level-q test errors at most 2 delta s^2 t_q^2 (times L^2 at seams). So the datum radius of U_r is at most C eps_0 s^2. For e^{i eta a_R} U_r and e^{i eta a_I} U_r it is at most C(eps_0 + eps_1^2) s^2. At real w the increment B(w) is real and lies in the r_B ball. Orbit uniqueness and the unique axial gauge (a1-balaban section 9.1, last paragraph) identify Phi_{V_0}(B(w)) with the real critical representative at that datum. Curvature and current norms are invariant under unitary gauges. This proves (113) with C = C(L) B.

**Application of P19. Correct.** In tower units, ||sa|| = max(s|a|, s^2 |nabla_{U_r} a|) <= s eps_1. With eps_1 <= r/2, P19 gives |F(sa)| <= 3C s^2 (eps_0 + eps_1^2) + 6H s^2 eps_1^2 / r^2. This is the current bound of (110) with K = 3C + 6H/r^2. Multiplying the plaquette version by eta_n^2, with eta_n s = eta, gives the curvature bound. K is made of a1-balaban's B, C(L), r_B and the dimension constants of (111). It does not depend on eps_1/eps_0, p, n, Z, the torus, M, kappa or gamma.

**Interior. Correct.** By the definition of collar(r) (CA-I after 4.8:eq-tower-rules-a), a point of Z farther than collar(r) L^n steps from Z^c lies in Omega_n. A point of Z^{wr p} lies at least 2 M L^{p-1} steps from Z^c (two layers of pi_{p-1} cubes, CA-I 4.8:eq-cube-lattices-b). With collar <= R_1 M_1 and M >= 2 L R_1 M_1, the margin at the worst case n = p is at least 3 R_1 M_1 L^n steps. So Z^{wr p}, with the bond-and-six-plaquette current stencils, lies in the top layer. This matches CA-I 34178-34189.

**The U_r clause.** Set a = 0. Then |F(0)| <= C eps_0 s^2, which is the real (1.17) with constant C(L)B. Correct.
