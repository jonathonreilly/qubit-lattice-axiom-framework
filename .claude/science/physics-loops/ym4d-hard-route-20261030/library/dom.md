# DOM: real support and earlier covariance classes
Provenance: Codex (GPT-6; exact serving variant not exposed), max effort requested; checkout `04c4e88731038f056dde44b19822e62512a7c8bc`; Sussman–Alpoge `31a47c543775`. Research text, not an audit; no status granted.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the covariance classes and Lemma 2.2(a) mechanism in `YM4_sketch_500.tex`. The pinned outline was fetched once to `/tmp/sa_ym4.tex`. T. Bałaban supplies the background methods rebuilt in the cited A1/A3 notes; Claude supplies the pivot lemma checked below. All arguments are by hand.

## 1. Check of `ti-2.md` (Claude)

This section checks the adopted rules, their readers, Lemmas 1, 3, 4, Theorem TI, and Corollary R14. Source line numbers refer to the pinned checkout.

**Checked line by line by Codex. ADVANCE as conditional implications; first failing step none in the statements below.** This does not supply (DOM), (ID), or an independent proof of their inherited analytic inputs.

- **(N), lines 43–52.** Rounding a face outward after adding \(m_i\) moves it by \([m_i,2m_i)\). Both faces belong to \(F_{i-1}\), so the increment is a multiple of \(m_{i-1}\). The smallest containing box is unique. Isometries carrying the grids therefore carry that box. Inductively, \(D_i\subset H_i+[-2m_i,2m_i]^4\subset A_i\). Thus `geo-3.md` §2 keeps its junction and exterior clearances. `geo-2.md` §6 keeps its geometric sum with \(K=2\). `geo-5.md` (3.1) reads the lower bound, not equality. Its filling and splice arguments still apply. `geo-4.md` reads the containment and shell bounds. `geo5c-count.md` reads only the lower gap. These also preserve the cited GEO/EXT-out inputs of the meet estimates; they do not remove those estimates' other premises.
- **The remaining geometric readers.** `cond-c.md` Rule W uses \((a+1)M\xi_{p-1}<m_p\), or the old base-point cell margin. Neither uses the rounding rule. `inn-213.md` (7.1) bounds \(|c_--z_c|_1\) by the nest diameter. Its (7.2), and `inn-fix.md` Lemmas H, C and Theorem I\(^R\), use the same shell counts. All remain valid with \(K=2\).
- **(T), line 54.** Under \(x\mapsto Ox+t\), frame coordinates gain the constant vector \((\langle t,Ore_i\rangle)_i\). This preserves lexicographic order. Nearest sites and frame-ordered combs are carried. Every cited bound holds for any root in the core. Nonwrapping lifts differing by a period give the same rule.
- **(F), lines 56–57.** Each minimal containing union obeys Steps 2–4 of `carrier-adopt.md` Lemma P. In its rooted estimate, the sum of the filing weights over unions containing the root is at most one. Thus (P) is unchanged. Summing over all unions gives weight one, preserving the total. Each union contains the carrier, preserving locality.
- **(INS) and Lemma 4, lines 59–63, 140–146.** Reindexing the finite group proves invariance. Since \(d_j(gX)=d_j(X)\), the triangle inequality gives \(\|\mathcal RH\|\le\|H\|\), \(\|H-\mathcal RH\|\le2\|H\|\). Translation covariance and Lemma 3 reduce the average to the signed permutations. These preserve the partitions and commute with common lifts, giving the companion. The underlying polymer class and its rooted count stay the same. The identity \(H=\mathcal RH+D_H\) must be retained: only an invariant total permits dropping \(D_H\). B4's defect allowance remains a premise. Its WF10 reader uses the extra norm through \(\rho_j^2d_j\), with no counterterm.
- **Lemma 1, lines 117–124.** A1 uniqueness and the invariant contour slice give exact covariance. The fibre with prescribed \(\mathcal M^iU\) lies inside the fibre with prescribed \(\mathcal M^{j-1}U\). Criticality restricts to it. (DOM) supplies the neighbourhood where uniqueness identifies its orbit; the slice then identifies the representative. The transformed third test has the same centre. Bond reversal conjugates its logarithm by a unitary and changes its sign, preserving its norm. This also proves the substitution in Lemma 2.
- **Lemma 3, lines 132–138.** The running minimum drops by at most \(B_\sharp\). The stated floor bounds the logarithmic ratio by \((1+1/r)^r\le e<L\). Rounding to powers of \(L\) commutes with multiplication by \(L\). Iteration gives \(\check R_iL^{i-j}\le\check R_j\). At insertion, every listed grid side divides \(L^{m+1-j}\); signed permutations preserve centred grids.
- **Theorem TI, lines 150–169.** (DOM) and Lemma 1 identify each earlier read with \(U_i(W')\), \(W'\in\mathcal K_i\). (ID) turns its total into \(\mathcal E^{(i)}(W')+c_i\). The group inclusion permits induction. Lemma 4 handles inserted totals. Substitution in the positive real integral preserves its logarithm and both subtractions. The empty list starts the induction. Holomorphic continuation is in the datum coordinates \(B\): successive one-variable identity theorems extend equality from a real open ball. It does not assert equality on arbitrary independent-current pairs.
- **Corollary R14, lines 175–179.** Lemma R's average preserves the total on precisely those backgrounds. It preserves the norm and locality, and introduces at most \(M^4\) grid offsets. Theorem P then gives the common coefficient and (20). The separate assumptions (ER7), (BX), (UR), (YA) remain for (19).

Section 5 of `ti-2.md` labels its domain argument a sketch. The next sections test that argument without using Lemma 1(b) before its domain hypotheses.

## 2. Radii and the real inputs

Write \(k=j-1\), \(e_i=\min(\varepsilon_{i-1},\varepsilon_i)\), and \(a_i=\min(\alpha_{0,i-1},\alpha_{0,i})\). At level zero use the single available radius. Put \(d=q-\mathfrak p_0>0\). SA (R19), (RF4) give
\[
 \varepsilon_i=A_0\theta_i^{-1/2}(\log\theta_i)^{\mathfrak p_0},\quad
 \delta_i=(A_1/A_0)\varepsilon_i,\quad
 \alpha_{0,i}=C_0\theta_i^{-1/2}(\log\theta_i)^q.
 \tag{1}
\]
Let \(D=\max(\bar B,c_5)\). Then \(|\theta_{i+1}-\theta_i|\le D\). Above a fixed floor \(\Theta\), both functions \(y^{-1/2}(\log y)^s\), \(s=\mathfrak p_0,q\), decrease and have logarithmic derivative of magnitude at most \(1/(2y)\). Choose \(\Theta\ge D\). Integration between neighbours gives ratios between \(1/2\) and \(2\). Consequently
\[
 \varepsilon_s\le2^{s-i}\varepsilon_i,\qquad
 e_i\ge\varepsilon_i/2,\qquad
 a_i\ge\frac{C_0}{2A_0}(\log\Theta)^d\varepsilon_i\quad(i\le s).
 \tag{2}
\]

The following are the precise library inputs used. They retain their stated hypotheses and torus floors.

1. A1, `a1-balaban.md` (8.2), its curvature-of-averages converse, and its fixed uniqueness neighbourhood. The checks are `gates/a1-balaban-gate.md` §§1, 5–6 and `gates/flat-port-gate.md`. For a uniform level-\(s\) background, curvature radius \(f\) makes its datum \(C_Af\)-regular. A1 then bounds its current by \(C_Rf\), in level-\(s\) units. The local real gauges have \(|A|,|\nabla A|\le C_GMf\), by `a3-close.md` §1 and its check, §A of `gates/a3-close-meet-gate.md`.
2. Real-critical A3: `a3-derivative.md` (31), §6.1 and §7, with `gates/a3-derivative-gate.md`'s repairs. The linear inputs are the repaired `p82-curved.md` theorem and `gates/a3-balaban-reads-gate.md`. On one fixed datum ball \(\|B\|_\infty<r_B\), the background response has \(\|h(B)\|_1\le C_H\|B\|_\infty\). Constants are uniform in depth and volume. All fields used below are real. No complex-reference or independent-current extension from `a3-clauses.md` is used.

Fix the geometric lengths, these constants and \(r_B\) first. Fix \(0<c\le1\), the radius factor in (R15). Choose \(A_1/A_0\) after them. Increase \(\Theta\) last. Every further condition below has this order. The inherited choice \(L\ge27\) suffices; no requirement makes \(L\) larger than a constant depending on \(L\).

## 3. The whole real support, including pivots

Put \(U_*=U_j(W)\), \(R=\mathcal M^kU_*\). The class gives
\[
 F_j(U_*):=L^{2j}\max_p|\partial U_*(p)-1|<ce_j.
 \tag{3}
\]
The converse in input 1 and A1 give \(\|J_j(U_*)\|\le C_Rce_j\). In level-\(k\) units the curvature and current gain \(L^{-2}\), \(L^{-3}\). Thus \(U_*\) lies in A1's level-\(k\) uniqueness neighbourhood once the floor is large. The datum \(R\) is regular. Its fibre is contained in the fibre over \(W\); hence \(U_*\) is critical there. A1 and the contour slice now give \(U_k(R)=U_*\). This uses no earlier covariance class.

On the support, nonpivot bonds satisfy \(d(V(b),R(b))\le\delta_k\). **The pivot estimate is essential.** `s210-fix.md` Lemma G(i)–(iii), checked here by hand, gives
\[
 \sup_b\left|\tfrac1i\log(V(b)R(b)^{-1})\right|
       \le C_P\delta_k .                                      \tag{4}
\]
Here \(C_P=C(L)\), and the floor must ensure
\(9L(C_8L\varpi+\delta_k)\le c_1L^{-6}\), where
\(\varpi=\sup_{p\subset D_c}|\partial R(p)-1|\le C_Ace_jL^{-2}\).

For completeness, this estimate covers every solution of the delta constraint. In a double block, write its straight transport as \(T=PV(b_0)Q\). Only the \(L\) axial paths use the pivot. The remaining logarithms have total weight \(1-L^{-3}\). After a comb gauge, their transports lie within \(\sigma=9L(C_8L\varpi+\delta_k)\) of 1. For \(T=e^{iZ}\), \(|Z|\le\pi/2\), the logarithm bound gives
\(|m(T)+(1-L^{-3})Z|\le2\sigma\). The constraint therefore forces \(|Z|\le5L^3\sigma\). If \(|Z|>\pi/2\), the crude logarithm rule gives instead
\(L^{-3}|Z|\le\pi L^3\sigma+3\sigma\le4L^3\sigma\), contradicting \(\sigma\le L^{-6}/8\). The last crude rule, \(\mathcal M=T\), cannot solve the small target either. On \(|Z|\le8L^3\sigma\), the map \(T\mapsto e^{-im(T)}\mathcal M(R)(c)\) maps the ball into itself and contracts by at most \(1-3L^{-3}/4\). Changing the nonpivot links by \(\delta_k\) changes this map by at most \(CL\delta_k\). Dividing by its contraction gap gives \(CL^4\delta_k\), proving (4). The logarithm estimates use \(\sin t\ge t-t^3/6\); no numerical test is involved.

Set \(B=\frac1i\log(VR^{-1})\). Choose the floor so that \(C_P\delta_k<r_B/2\). All real \(tB\), \(0\le t\le1\), then lie in A3's datum ball, before any conclusion about \(\mathcal K_k\). In A3's real gauge,
\(U_k(V)\sim e^{i\eta_kh(B)}U_*\), \(\|h(B)\|_1\le C_HC_P\delta_k\). Here the derivative in \(\|h\|_1\) is covariant with the reference. Real gauge changes preserve curvature and current norms, this response norm, and existence of the local gauges used below.

Expanding the four transported link factors of a plaquette gives a linear covariant curl and a quadratic remainder. Their bounds are \(C\eta_k^2\|h\|_1\) and \(C\eta_k^2\|h\|_1^2\); the reference-curvature term is at most \(C\eta_k^2ce_j\|h\|_1\). Enlarge a fixed \(C_F\) to absorb these terms and (4). Therefore
\[
 F_k(U_k(V))\le cL^{-2}e_j+C_F\delta_k.
 \tag{5}
\]
By (2), \(e_j/e_k\le4\). Choose
\(A_1/A_0\le c/(8C_F)\). Then (5) is strictly less than \(ce_k/2\), since \(4/L^2<1/4\). This proves the required one-step curvature bound with room. It also proves real existence on the entire support through A3, not merely near its centre. Boundary points of the sharp box obey the same strict conclusion.

## 4. Earlier classes and every real core

Let \(U=U_s(W_s)\) be a uniform background with \(F_s(U)<ce_s\). This covers \(U_j(W)\) and, by (5), \(U_k(V)\). Input 1 gives
\(\|J_s(U)\|\le C_R\varepsilon_s\) and local real gauges bounded by \(C_GM\varepsilon_s\). Fix \(i\le s\) and put \(n=s-i\). Changing units gives
\[
 F_i(U)=L^{-2n}F_s(U),\qquad J_i(U)=L^{-3n}J_s(U).
 \tag{6}
\]
A cube of side \(O(LM)\) at level \(i\) fits in such a cube at level \(s\). Restrict its gauge. The potential gains \(L^{-n}\); its derivative gains \(L^{-2n}\). Thus its local gauge bound is at most \(C_GM\varepsilon_sL^{-n}\). These arguments work for every translated cube.

The averages \(W_i=\mathcal M^iU\) have datum radius at most \(C_A\varepsilon_sL^{-2n}\). Equation (6) places \(U\) in the fixed \(\mathcal N_i\), after increasing the floor. Nested fibres make it critical over \(W_i\). A1 gives existence there; uniqueness and the common contour slice give
\[
                         U_i(W_i)=U.                         \tag{7}
\]
For \(n\ge1\), (2) gives
\[
 \frac{F_i(U)}{ce_i}
 <2(2/L^2)^n\le4/L^2<1.
 \tag{8}
\]
For \(n=0\) this is the assumed bound. Thus (R15) holds at every earlier level.

Here is the hereditary part, with its full loss retained. Fix any read domain \(X\) at level \(i\), any \(Z\subset X\) of level \(p\le i\), either tower rule, and truncation depth \(0\le v\le p\). The real tower datum consists of actual averages of \(U\). The curvature converse bounds all its tests by
\(C_A\varepsilon_sL^{-2(s-v)}\). This is below A1's datum ceiling at the chosen floor, so the tower background exists. On the prescribed eroded interior, A1 gives
\[
 |\partial U_v(Z;U)-1|\le C_T\varepsilon_sL^{-2s},\qquad
 |J_v(U_v(Z;U))|\le C_T\varepsilon_sL^{-2(s-v)},\quad C_T=BC_A.
 \tag{9}
\]
Indeed that interior lies in the tower's last member. The erosion is at most \(\max(\rho,3M_1')\) in level-\(p\) units; the removed layers have width \(2M/L>\max(\rho,3M_1')+2\). The existing geometric floors imply this inequality. All current stencils therefore remain inside \(Z\). At \(v=0\), the datum is the field itself and its current is a sum of six plaquette contributions; enlarge \(C_T\) to include it. This is the real part of `a3-close.md` Lemma T, with no analytic substitution.

The two tower bounds required by the level-\(i\) core are respectively
\(a_iL^{-i-p}\) and \(a_iL^{2v-i-p}\). Dividing (9) by them gives the same upper bound:
\[
 \frac{C_T\varepsilon_s}{a_i}L^{-2(s-i)}L^{p-i}
 \le\frac{2C_TA_0}{C_0}(\log\Theta)^{-d}(2/L^2)^n.
 \tag{10}
\]
This includes every truncation and every tower; no sum over them is taken. The physical pair is represented by \((U,0,J_i(U))\). Its simple curvature, current and real-gauge bounds, divided by their core bounds, are at most
\[
 \frac{2C_*A_0}{C_0}(\log\Theta)^{-d}(2/L)^n,                \tag{11}
\]
where \(C_*\) includes \(C_T,C_R,C_G\) and the fixed gauge normalization. The complex-potential clauses vanish. The tower with the real factor and the tower with the product coincide.

Choose \(\Theta\) so that \(2C_*A_0C_0^{-1}(\log\Theta)^{-d}<1/4\). Then (10)–(11) put every restriction in the half core, uniformly in \(i,s,X,Z,p,v\) and grid offsets. The supplied current on a restriction is the ambient current; (9) separately checks the tower current. Absolute core radii are handled by making \(\varepsilon(\Theta)\) smaller than their fixed minimum. All remaining ceilings also hold at one floor: \(y^{-1/2}(\log y)^b\to0\), as follows from \(e^{t/4}\ge(t/4)^N/N!\) with an integer \(N>b\). No constant depends on depth or volume.

We can now verify each clause of (DOM). Clause (a) follows from (4) and A3's real datum ball. Equations (6)–(11) prove (b) and (c), including the required uniqueness neighbourhoods. Clause (d) follows from the declared intersection of translates; the estimates also admit each translated core directly. For (e), apply (10)–(11) at the origin level of each inserted family. They hold on every translate of its core, so they hold on the invariant intersection used by (INS). Lemma 3 ensures that its insertion group preserves its grid class. This proves (DOM) for the whole-lattice kernel (K), with the declared cores and torus floors.

## Result

`ti-2.md`: checked line by line by Codex; the adopted rules and listed implications pass with their premises retained.

**(DOM) is proved as an implication from the stated real A1/A3 package and the adopted block map and cores.** The support requires the pivot bound (4). The choice of \(A_1/A_0\) gives (R15); the later coupling floor pays for every hereditary core clause. This new proof has not been checked by the other model.

**First remaining unsupplied input to Theorem TI: (ID), B4's identity.** No input fails inside the domain implication above. With (ID), Theorem TI and Corollary R14 give (20). The separate premises of (19), including the unresolved (BX) repair, remain. This result does not prove the full large-field version of SA Lemma 2.2(a), run an audit, or grant status.
