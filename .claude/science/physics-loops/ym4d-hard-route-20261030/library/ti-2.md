lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-04T12:02Z

# ti-2: check of ti-cov.md, the covariant rules, and (TI)

Queue row 208, `ti-2`. Pinned at commit 52e541e2d on branch `claude/ym4d-hard-route`.
Written by Claude (Opus 5.5, max effort) on the Mac mini worker, 2026-11-04. Research-stage working state; no status.

**Moves:** (TI), hence (R14), (20) for every old regular member, B4's (19) and WF7's retained premise.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the step functional (RF16), the list action (R17), (R14), the class (R15), the frame sum, the insertion age and the defect allowance; `YM4_sketch_500.tex` at `31a47c543775`, fetched to a scratch folder. Their YM3_I (lines 38578-38609) gives the same symmetry argument for isometries that preserve the partitions. Codex: `ti-cov.md` (formula (2), (3), (5), (6), (7), the tie rule and the averaged filing). T. Balaban: the backgrounds (CMP 102 Theorem 1, rebuilt as A1 in `a1-balaban.md`) and the contour gauge (CMP 109 (0.14)-(0.16)). Every step below is by hand. No numerics were run.

## 1. Check of `ti-cov.md` Sections 2-5 (Codex)

Provenance: Claude Opus 5.5, max effort, commit 52e541e2d. One line-by-line reading by one other model; not an audit.

**Verdict: Sections 2-5 ADVANCE, each as an implication from its named inputs. Checked line by line by Claude, first failing step none.** Three precisions follow. None breaks a statement.

What I redid:

- **(1).** \((e^{iA}V)^{-1}=V^{-1}e^{-iA}=e^{-i\operatorname{Ad}(V^{-1})A}V^{-1}\). \(\operatorname{Ad}(V^{-1})\) is orthogonal on su(2). So bond balls and Lebesgue measure are kept.
- **\(\mathcal M(gV)=g\mathcal M(V)\).** In (R3) (SA 5631-5641), reindex the start block of the reversed bond \(\bar c\) by \(x'=x+(c_+-c_-)\). The loop becomes \(W'_{x'}=U[c]^{-1}W_x^{-1}U[c]\). So \(\log W'_{x'}=-\operatorname{Ad}(U[c]^{-1})\log W_x\), and \(\mathcal M(U)(\bar c)=U[c]^{-1}e^{-\bar a}=\mathcal M(U)(c)^{-1}\), with \(\bar a\) the block mean of \(\log W_x\). This is also `prefactor-loc.md` Lemma D (c). Blocks are centred (L odd), and \(\mathcal G(y,x)\) contains every coordinate order (SA 7065). So g maps blocks, contour families and contour means to their images. On the support every coarse bond lies in Dom(c); SA 7065-7072 states that the two cruder rules are covariant.
- **(2).** Haar measure is invariant under bond permutations and under inversion. \(\delta\) is a class function with \(\delta(h^{-1})=\delta(h)\), so \(\delta(\mathcal M(V)(b)^{-1}W(b))=\delta(\mathcal M(V)(b)W(b)^{-1})\). \(\mathfrak G_{j-1}\) runs over all blocks, and \((gV)(gy,gx)=V(y,x)\). The pivot \(b_0(c)=(y+he_\mu,y+(h+1)e_\mu)\), \(h=(L-1)/2\), is the middle bond of \([c_-,c_+]\) (SA 8167). So g maps pivots to pivots and non-pivots to non-pivots.
- **(3).** Put \(F=\exp[-xA(U_{j-1})+S(U_{j-1})]\) in (2) and use \(U_l(gV)=gU_l(V)\). Then \(T(F)(gW)=T(F)(W)>0\). The two subtractions are invariant. Logarithms of equal positive numbers agree. Continuation needs one connected domain, as stated.
- **Section 3.** Items 1-6 hold as stated. Item 1: (A7) of `assign-adopt.md`, and the distance formula (5.1) of `geo-prop23.md`. Items 3-4: Rule W and box first are estimation devices for (19) and enter no total. Definition D and [RED] are natural with their data carried. In the regular step they enter only through uncut sums, so they change no regular total; in the large-field kept form they do enter, which is why their naturality matters in Section 4. Item 5: Steps 2-4 of `carrier-adopt.md` Lemma P bound *every* minimal containing union, not only the selected one. Equal weights sum to one. So (P) is unchanged, and so is the total \(-\frac12\sum\langle A',\mu A'\rangle\). Item 6: for \(x\mapsto Ox+t\) and frame \(r\mapsto Or\), \(\langle Ox+t,Ore_i\rangle=\langle x,re_i\rangle+\langle t,Ore_i\rangle\). So the frame-ordered lexicographic order is carried, and with it the first nearest site.
- **Section 4, (4).** \(R/L^2\) is odd, so \(h=13Rm/(2L)\in Lm(\mathbb Z+\frac12)=F_{i+1}\). The lower-face-first rule gives \(\alpha_i=-h-m\) and \(\beta_i=\min\{u\in F_{i+1}:u\ge h+m\}=h+Lm\). Since \(h+Lm<Rm/2+Lm<17Rm/2\), \(D_i\subset E_i^{[8]}\). Reflection in coordinate 1 fixes C and the centred grids. It sends \(D_i\) to \([-h-Lm,h+m]\times[-h-m,h+Lm]^3\), while the rule applied to C gives \(D_i\) again. The WRONG verdict on the formation-rule implication stands. The rule is translation covariant; only reflections fail.
- **(5).** The smallest box with faces in \(F_i\) containing a box Y is unique: round each lower face of Y down to \(F_i\) and each upper face up. An isometry with \(gF_i=F_i\) maps this criterion to itself, and \(g(Y+[-m_i,m_i]^4)=gY+[-m_i,m_i]^4\). Increments lie in \([m_i,2m_i)\). They are multiples of \(m_{i-1}\), because the faces of \(D_{i-1}\) lie in \(F_{i-1}\supset F_i\). Containment: \(D_i\subset D_{i-1}+[-2m_i,2m_i]^4\subset H_i+[-8s_i,8s_i]^4=A_i\), since \(D_{i-1}\subset B_{i-1}\subset H_i\) and \(s_i\ge m_i\).
- **Aged data.** M is a power of L (SA 5586). \(\check R_j\) is the least power of L not below \((\log\min_{i\le j}x_i)^r\) (SA 17334). So \(M\check R_j\le L^{m+1-j}\) gives divisibility.
- **Section 5.** (6) is the triangle inequality with \(d_j(gX)=d_j(X)\). In (7), \((\log\bar g^{-2})^{4r}\le2^{4r}t^q\) for \(t\ge1\), and \(e^{\epsilon t}\ge(\epsilon t)^q/q!\) gives \(t^qe^{-\epsilon t}\le q!\epsilon^{-q}\). This needs \(\kappa_0>4\), so that \(\epsilon=(\kappa_0-4)/2>0\).

**Precision 1: the base of the sharp box.** The bond balls of (2) must be centred at a base with \(V^{\rm bg}(gW)=g\cdot V^{\rm bg}(W)\) exactly. A gauge change of the base alone changes \(|\mathcal A(b)|\). SA forms the third test with the true averaged background, \(\mathcal A_k=\frac1i\log(V_k(V_k^{\rm bg})^{-1})\) (SA 17336). Under (Id) the background is the augmented branch. That branch is the constrained critical configuration in the contour gauge, where every contour variable equals 1 (`prefactor.md` Section 3, last lines; SA 7185, \(\operatorname{Ax}^\circ\)). This slice is isometry invariant, because contour variables average over all coordinate orders. A comb tree of order 4,3,2,1 (the box axial gauge, SA 7178) would not do. I name this reading (K) in Section 3.

**Precision 2: later backgrounds.** "S is invariant at every background read" concerns totals of members of level \(i<j\) at the backgrounds of a later step. It needs \(U_{j-1}(V)=U_i(\mathcal M^iU_{j-1}(V))\), and \(\mathcal M^iU_{j-1}(V)\) in the class where the total of \(E^{(i)}\) equals \(\mathcal E^{(i)}\). Lemma 1 (b) below proves the first from A1. The second is premise (DOM).

**Precision 3: older grids at the insertion age.** A level-j remainder is formed also on older region grids (side \(M\check R_i\), \(i<j\), in level-i units) and on test-cube grids. In level-j units their sides are powers of L at most \(M\check R_j\), by Lemma 3 (a) below. So the divisibility of §4 covers them too.

Not shown by this check: the premises that ti-cov retains (support-domain covariance and invariant remainder totals). Sections 3-4 below treat them.

## 2. The adopted covariant versions and their readers

These are supplied formation data. SA 6055-6078 leaves the regions, nests and tests to the formation data, and SA 6229-6231 leaves the localization rule open. Each rule is a choice, not a consequence of the outline.

**(N) Nest selector.** For each eligible component, \(D_a:=C\) and, for \(a<i\le k\), coordinate by coordinate,
\[
 \alpha_i:=\max\{u\in F_i:u\le\alpha_{i-1}-m_i\},\qquad
 \beta_i:=\min\{u\in F_i:u\ge\beta_{i-1}+m_i\},\qquad F_i=m_i(\mathbb Z+\tfrac12).
\]
So \(D_i\) is the smallest box with faces in \(F_i\) that contains \(D_{i-1}+[-m_i,m_i]^4\) (ti-cov (5)). It replaces the alternating recursion of `geo-prop23.md` (3.3) and `geo-3.md` Section 2. By Section 1:
- (N1) \(D_{i-1}\subset D_i\), and \(D_i\) is a union of level-i M-cubes.
- (N2) Every face increment lies in \([m_i,2m_i)\) and is a multiple of \(m_{i-1}\). So \(d_\infty(D_{i-1},D_i^c)\ge m_i\) and \(D_i\subset D_{i-1}+[-Km_i,Km_i]^4\) with \(K=2\).
- (N3) \(D_i\subset A_i=H_i^{[8]}\subset B_i\subset H_{i+1}\).
- (N4) \(D_i(gC)=gD_i(C)\) for every isometry g with \(gF_i=F_i\) for all i; with the grids carried, for every isometry.

**(T) Tie rule of Definition R.** In the summand of frame r, \(z_c\) is the first site, in the lexicographic order of \((\langle x,re_1\rangle,\dots,\langle x,re_4\rangle)\), among the level-\(k_\flat\) sites of the core nearest its centre (ti-cov §3 item 6). Definition R is formed inside the frame sum (SA 17585), so the frame average carries it.

**(F) Averaged filing in Lemma P.** Let \(\mathfrak M(\mu)\) be the set of connected unions of least cardinality that contain every cube meeting the carrier of \(\mu\). Put
\(\mathsf B^\times(X):=-\frac12\sum_{\mu\ \rm rejected}\#\mathfrak M(\mu)^{-1}\mathbf 1[X\in\mathfrak M(\mu)]\langle A',\mu A'\rangle\) (ti-cov §3 item 5).

**(INS) Symmetric insertion of aged remainders.** A level-j remainder family H enters the regular list at step m+1, when \(M\check R_j\le L^{m+1-j}\) (SA 20649-20654). The list then receives
\[
 \mathcal R_{m+1}H:=|\mathfrak G^{(m+1)}|^{-1}\sum_{g\in\mathfrak G^{(m+1)}}g_*H,\qquad (g_*H)(X,\mathbf P):=H(g^{-1}X,g^{-1}\cdot\mathbf P),
\]
where \(\mathfrak G^{(m+1)}\) is the level-(m+1) torus group of Section 3. The difference \(D_H:=H-\mathcal R_{m+1}H\) is filed as a scale-small noncovariant defect. The ordinary source box admits such defects (SA 4007-4010), and a defect has no coupling counterterm (SA 16057). If the total of H is already invariant, \(D_H\) has total zero and can be dropped. This is ti-cov (6), used at insertion.

**(K) Reading of the whole-lattice kernel (no change).** The kernel of SA 7142 has Haar measure, the R3 constraint, \(\mathfrak G_{j-1}\) on all blocks, and the third test \(\mathbf 1\{|\mathcal A(b)|<\delta_{j-1}\}\) at every non-pivot bond, with \(\mathcal A\) formed from \(V^{\rm bg}=\mathcal M^{j-1}U_j(W)\) and \(U_j(W)\) the \(\operatorname{Ax}^\circ\) representative (Section 1, Precision 1).

**Readers.**

| Rule | Reader | What it reads | Kept |
|---|---|---|---|
| (N) | `geo-3.md` §2, (2.2)-(2.6), junction and cross-component clearance | nesting; gap \(\ge m_i\); increments \(\le Km_i\); \(D_i\subset A_i\); \(D_i\subset B_i\subset H_{i+1}\) | yes, with K = 2. The gap equality in (2.2) is a by-product; no consumer reads it (`geo-5.md` (3.1) reads \(\ge\)) |
| (N) | `geo-2.md` §6, (6.1)-(6.2) | upper bound \(Km_i\), K fixed before R | yes, K = 2 |
| (N) | `geo-5.md` (3.1), §§3.2-5 | nesting, \(D_i\subset X\cap\Omega_i^{\circ c}\), gap \(\ge m_i\), faces on the common face grid | yes |
| (N) | `geo-4.md` §§3-6 | \(D_k\subset A_k\) and the rule of `geo-2.md` §6 | yes |
| (N) | `geo5c-count.md` | does not read the face rule (its line 51) | yes |
| (N) | `geo-prop23.md` §§3-5, `geo-2.md` §§3-5 | example nests inside counterexamples | not consumers. The profile counterexample needs only a final box of size O(M) (`geo-prop23.md` §3, last paragraph), which (N2) gives |
| (N) | `cond-c.md` Lemma M, Rule W | the gap lower bound LM in level-(i-1) units, which is \(m_i\) (SA 17402). It does not read the face rule (its line 207) | yes |
| (N) | `inn-213.md` §7, `inn-fix.md` | the nest box \(N_{\rm c}\) and the GEO3 shell bounds | yes, through `geo-2.md` §6 with K = 2 |
| (N) | `sa-2.8-terms.md` Lemma W, `meet-6c.md`, `a3-close-meet-gate.md` §B | GEO1-GEO6, EXT-out, W3 through the geo notes above | yes |
| (T) | `inn-213.md` §7a (R1)-(R4), Proposition D (7.1); `inn-fix.md` Theorem I\(^R\), Corollary P\(^R\), (7.2\(^R\)) | \(z_c\) in the core, \(|c_--z_c|_1\), and \(D_W\) bounded by the nest box of levels \(\le s'\) | yes; each bound holds for every core site |
| (F) | `carrier-adopt.md` Lemma P (P), Theorem A (iv), and their readers | bound (P), the total of \(\mathsf B^\times\), locality | yes (Section 1) |
| (INS) | `b4-step.md` (19); `b2-extract.md` Proposition W and its WF10 remark | defects enter only through \(\rho_j^2(d_j+r_j)\) | yes: \(d_j\) gains at most \(2\|H\|\le2\bar g_j^{\kappa_0}\) (Lemma 4) |
| (INS) | SA (R17) slot families \(H^{(j)}\) | companion, term covariance under localization translations, invariant totals | yes (Lemma 4 (c)) |

So the four rules keep every reader. Only (N) changes a geometric object, and it changes it inside the bounds that the readers use.

## 3. Theorem TI: invariance of every regular total, by induction over the steps

### 3.1 Setting

- T is a cubic torus whose side is a multiple of every grid side (SA 24063). The origin is a site of every level (L odd, centred blocks).
- \(\mathfrak G^{(j)}\) is the group generated by the level-j unit translations and the \(2^44!\) signed permutations about the origin. Level-j sites form a sublattice of level-i sites for \(i\le j\), so \(\mathfrak G^{(j)}\subset\mathfrak G^{(i)}\). \(\mathfrak G^{(j)}\) is the group \(\mathfrak G_N\) of Lemma R.
- Isometries act on configurations and pairs with the reversed-bond twist (SA 7119-7124). Put \(\mathbf p_U:=(U,J(U))\). The current is natural, so \(g\cdot\mathbf p_U=\mathbf p_{gU}\).
- Elements of \(\mathfrak G^{(j)}\) map blocks of every level \(n\le j\) to blocks and \(\mathcal G(y,x)\) to \(\mathcal G(gy,gx)\). So \(\mathcal M^n(gU)=g\mathcal M^n(U)\) for \(n\le j\) (Section 1).
- \(\mathcal E^{(j)}(W)\) is the step functional (RF16), with the kernel \(\mathbf T^{\rm sf}_{j-1}[\theta]\) and the list action \(S_j\) of (R17). Under (INS), \(S_j\) holds the members \(E^{(i)}\), \(i<j\), their constants \(E^{(i)}(X,\mathbf 1,z)\), the terms \(-e_iA\), and the families \(\mathcal R_{m+1}H\) inserted at steps \(m+1\le j\).
- \(\mathcal K_j\) is the covariance class of level j (SA 5903-5915): real level-j fields whose backgrounds exist, whose restrictions lie in the cores, and which satisfy (R15). If a clause of this class uses towers of a fixed grid, read \(\mathcal K_j\) as the intersection of its \(\mathfrak G^{(j)}\)-translates.
- \(\mathrm{Tot}\,E(\mathbf P):=\sum_{X,z}E(X,\mathbf P,z)\).

### 3.2 Premises, named once

- **(A1)** `a1-balaban.md` (checked, row 81): for data in the existence domain, the critical residual orbit exists and is unique in a fixed regularity neighbourhood \(\mathcal N_i\). \(\mathcal N_i\) and the existence domain are defined by \(r(U)\) and by test-loop errors. Isometries permute plaquette variables, currents and test loops, so both sets are \(\mathfrak G^{(i)}\)-invariant.
- **(Id)** `b2-extract.md` §4 with `prefactor.md` §3: \(U_i(W)\) is the \(\operatorname{Ax}^\circ(T,\mathbf 1)\) representative of that orbit (all contour variables of all levels \(n<i\) equal 1). This slice meets each residual orbit once (SA 7185).
- **(K)** Section 2.
- **(DOM)** For \(j\ge1\), \(W\in\mathcal K_j\) and V in the support of \(\mathbf T^{\rm sf}_{j-1}\) at W:
  (a) V lies in the existence domain of A1 at level j-1;
  (b) for each \(i\le j-1\), \(U_{j-1}(V)\in\mathcal N_i\) as a level-i configuration, and \(\mathcal M^iU_{j-1}(V)\in\mathcal K_i\);
  (c) the same holds for \(U_j(W)\), for each \(i\le j\);
  (d) \(\mathcal K_j\) is \(\mathfrak G^{(j)}\)-invariant;
  (e) \(\mathbf p_{U_{j-1}(V)}\) and \(\mathbf p_{U_j(W)}\) lie in the \(\mathfrak G^{(m+1)}\)-invariant core of every family inserted at a step \(m+1\le j\).
- **(ID)** For \(i\ge1\) and \(W'\in\mathcal K_i\): \(\mathrm{Tot}\,E^{(i)}(\mathbf p_{U_i(W')})=\mathcal E^{(i)}(W')+c_i\), with \(c_i\) independent of \(W'\) (SA 6229-6234, 20593-20597).
- **(INS)** Section 2.

(DOM) and (ID) are not new to (TI). SA defines the step functional only on fields whose step backgrounds exist and give pairs in the domains of the terms (SA 7581), and it lists the common covariance class of the fluctuating backgrounds as part of closure (SA 20636-20646). B4 must deliver both.

### 3.3 Lemmas

**Lemma 1 (backgrounds on the full support).** Assume (A1), (Id) and (DOM). Let \(W\in\mathcal K_j\), V in the support at W, and \(g\in\mathfrak G^{(j)}\).
- (a) \(U_{j-1}(gV)=gU_{j-1}(V)\) and \(U_j(gW)=gU_j(W)\).
- (b) \(U_{j-1}(V)=U_i(\mathcal M^iU_{j-1}(V))\) for \(i\le j-1\), and \(U_j(W)=U_i(\mathcal M^iU_j(W))\) for \(i\le j\).
- (c) g maps the support at W onto the support at gW.

*Proof.* (a) \(\mathcal M^{j-1}\) is covariant and the Wilson action is invariant. So g maps critical points on \(\{\mathcal M^{j-1}U'=V\}\) to critical points on \(\{\mathcal M^{j-1}U'=gV\}\). By (DOM) (a) and invariance of the existence domain, \(U_{j-1}(gV)\) exists. \(gU_{j-1}(V)\) lies in the invariant set \(\mathcal N_{j-1}\). By A1 it lies in the residual orbit of \(U_{j-1}(gV)\). The slice \(\operatorname{Ax}^\circ\) is cut out by the conditions \(U'(y,x)=\mathbf 1\) on the contour variables of every \(\mathcal M^nU'\), \(n<j-1\). g permutes these conditions, because \((gU')(gy,gx)=U'(y,x)\). So g maps the slice to itself. The slice meets the orbit once, so \(gU_{j-1}(V)=U_{j-1}(gV)\). The same argument at level j gives \(U_j(gW)=gU_j(W)\).
(b) Put \(U:=U_{j-1}(V)\) and \(W':=\mathcal M^iU\). By the semigroup law (SA 7127), \(\{\mathcal M^iU'=W'\}\subset\{\mathcal M^{j-1}U'=V\}\), and the smaller fibre contains U. A critical point on the larger fibre is critical on the smaller one. By (DOM) (b), \(U\in\mathcal N_i\) and \(W'\in\mathcal K_i\), so \(U_i(W')\) exists. By A1 at level i, U lies in the residual orbit of \(U_i(W')\). U satisfies the slice conditions of every level \(n<j-1\), hence of every level \(n<i\). Both points lie in the level-i slice, which meets the orbit once. So \(U=U_i(W')\). The case of \(U_j(W)\) is the same, with (DOM) (c).
(c) The support at W is cut out by \(\delta(\mathcal M(V)W^{-1})\), by \(\mathfrak G_{j-1}\), and by the third test relative to \(V^{\rm bg}(W)=\mathcal M^{j-1}U_j(W)\). By (a), \(V^{\rm bg}(gW)=gV^{\rm bg}(W)\). By Section 1, g maps each condition at W to the same condition at gW. \(\square\)

**Lemma 2 (the kernel).** Assume (K) and Lemma 1. For \(W\in\mathcal K_j\), \(g\in\mathfrak G^{(j)}\) and F integrable on the support,
\[
 (\mathbf T^{\rm sf}_{j-1}F)(gW)=(\mathbf T^{\rm sf}_{j-1}(F\circ g))(W).
\]
*Proof.* Substitute \(V=gV'\). Haar measure is invariant under bond permutation and inversion. The delta factor and \(\mathfrak G_{j-1}\) map as in Section 1. For the third test at gW: on a bond \(b'\) with \(g^{-1}b'=b\), \(\mathcal A_{gW}(gV')(b')=\mathcal A_W(V')(b)\). If \(g^{-1}b'=\bar b\), then \(\mathcal A_{gW}(gV')(b')=-\operatorname{Ad}(V^{\rm bg}(b)^{-1})\mathcal A_W(V')(b)\), by (1) and Lemma 1 (a). Both have the same norm, and pivots map to pivots. \(\square\)

**Lemma 3 (scales).** (a) Let \(y_k=\min_{u\le k}x_u\), \(|x_{k+1}-x_k|\le B_\sharp\) (SA 7518), and assume the floor \(y_k\log y_k\ge rB_\sharp\) for all k. Then \(\check R_k\le L\check R_{k+1}\), hence \(\check R_i\le L^{j-i}\check R_j\) for \(i\le j\). (b) At the insertion step m+1 of a level-j remainder, every element of \(\mathfrak G^{(m+1)}\) maps to itself every centred partition of a level \(i\le j\) whose side, in level-j units, is a power of L at most \(M\check R_j\). These include the \(M\check R_i\)-cube partitions, the partitions \(\pi_i\), and the test-cube partitions of side \(M_2\check R_i\) (SA 17334), for \(i\le j\).

*Proof.* (a) \(y_{k+1}=\min(y_k,x_{k+1})\ge y_k-B_\sharp\). With \(\log(y+B)\le\log y+B/y\),
\[
 (\log y_k)^r\le(\log y_{k+1})^r\Big(1+\frac{B_\sharp}{y_{k+1}\log y_{k+1}}\Big)^r\le(1+\tfrac1r)^r(\log y_{k+1})^r\le L(\log y_{k+1})^r ,
\]
since \((1+1/r)^r\le e<L\). Let P(t) be the least power of L not below t. P is monotone and \(P(Lt)=LP(t)\). So \(\check R_k=P((\log y_k)^r)\le LP((\log y_{k+1})^r)=L\check R_{k+1}\) (SA 17334 states this). Iterate. (b) A level-(m+1) unit translation has length \(L^{m+1-j}\) in level-j units. In level-j units the listed sides are \(M\check R_iL^{i-j}\le M\check R_j\) by (a), \(ML^{i-j}\le M\) and \(M_2\check R_iL^{i-j}\le M\check R_j\). Each is a power of L at most \(M\check R_j\le L^{m+1-j}\), so it divides \(L^{m+1-j}\). A signed permutation about the origin maps each centred partition of odd side to itself. \(\square\)

**Lemma 4 (inserted remainders).** Let H be a level-j remainder family inserted at step m+1, bounded on a \(\mathfrak G^{(m+1)}\)-invariant core.
- (a) \(\sum_X\mathcal R_{m+1}H(X,g\cdot\mathbf P)=\sum_X\mathcal R_{m+1}H(X,\mathbf P)\) for every \(g\in\mathfrak G^{(m+1)}\) and every pair P of the core.
- (b) \(\|\mathcal R_{m+1}H\|_{j,\kappa}\le\|H\|_{j,\kappa}\) and \(\|D_H\|_{j,\kappa}\le2\|H\|_{j,\kappa}\).
- (c) If the terms of H are covariant under the translations that preserve its partitions (SA 7477), then \(\mathcal R_{m+1}H=|W_4|^{-1}\sum_{w\in W_4}w_*H\), over the signed permutations about the origin. Its domains are domains of the same partitions, the rooted count does not grow, and \(|W_4|^{-1}\sum_ww_*\widehat H\) is its companion.
- (d) If the total of H is \(\mathfrak G^{(m+1)}\)-invariant at P, then \(\sum_XD_H(X,\mathbf P)=0\).

*Proof.* (a) \(\sum_X(g_*H)(X,\mathbf P)=\sum_XH(X,g^{-1}\cdot\mathbf P)\), and \(g'\mapsto hg'\) permutes the group. (b) Each \(g_*H(X)\) is at most \(\|H\|e^{-\kappa d_j(g^{-1}X)}=\|H\|e^{-\kappa d_j(X)}\); then use the triangle inequality. (c) By Lemma 3 (b), each translation t of \(\mathfrak G^{(m+1)}\) preserves the partitions of H, so \(t_*H=H\). For \(g=tw\), \(g_*H=w_*(w^{-1}tw)_*H=w_*H\), since \(w^{-1}tw\) is again such a translation. Each \(w_*\) maps centred partitions to themselves and commutes with lifts of non-wrapping domains. (d) is immediate. \(\square\)

### 3.4 The theorem

**Theorem TI (implication; proved by Claude, not yet checked by the other model).** Assume (A1), (Id), (K), (DOM), (ID) and (INS). Then for every \(j\ge1\):
- (i) \(\mathcal E^{(j)}(gW)=\mathcal E^{(j)}(W)\) for every \(W\in\mathcal K_j\) and \(g\in\mathfrak G^{(j)}\);
- (ii) \(\mathrm{Tot}\,E^{(j)}(g\cdot\mathbf p_{U_j(W)})=\mathrm{Tot}\,E^{(j)}(\mathbf p_{U_j(W)})\) for the same W and g. By Lemma 1 (b), every background at which the chain reads \(E^{(j)}\) is of this form;
- (iii) both identities continue holomorphically on every connected domain where both sides are holomorphic and which contains a real open set of such points. In particular (ii) holds at \(P_j(B)\) for B in a connected complex neighbourhood of 0.

*Proof.* Induction on j. The hypothesis H(j-1) is (i) at every level \(i<j\).

*Step 1: earlier members at the read backgrounds.* Fix \(W\in\mathcal K_j\) and \(g\in\mathfrak G^{(j)}\). Let U be \(U_{j-1}(V)\), with V in the support at W, or \(U_j(W)\). Let \(i<j\) and \(W':=\mathcal M^iU\). By (DOM), \(W'\in\mathcal K_i\). By Lemma 1 (b), \(U=U_i(W')\), so (ID) gives \(\mathrm{Tot}\,E^{(i)}(\mathbf p_U)=\mathcal E^{(i)}(W')+c_i\). By (DOM) (d), \(gW'\in\mathcal K_i\), and Lemma 1 (a) at level i gives \(gU=U_i(gW')\). So
\[
 \mathrm{Tot}\,E^{(i)}(g\cdot\mathbf p_U)=\mathrm{Tot}\,E^{(i)}(\mathbf p_{U_i(gW')})=\mathcal E^{(i)}(gW')+c_i=\mathcal E^{(i)}(W')+c_i=\mathrm{Tot}\,E^{(i)}(\mathbf p_U),
\]
by H(j-1), since \(g\in\mathfrak G^{(j)}\subset\mathfrak G^{(i)}\).

*Step 2: the list action.* \(S_j\) consists of the totals of Step 1, constants, the terms \(-e_iA\), and the totals of the inserted families. A is invariant. By Lemma 4 (a) and (DOM) (e), each inserted total is invariant under \(\mathfrak G^{(m+1)}\supset\mathfrak G^{(j)}\). So \(S_j(gU)=S_j(U)\) for both kinds of U.

*Step 3: the step functional.* Put \(F(V):=\exp[-xA(U_{j-1}(V))+S_j(U_{j-1}(V))]\) on the support at W. By Lemma 1 (a) and Step 2, \(F(gV)=F(V)\), and by Lemma 1 (c), \(F\circ g\) is defined there. Lemma 2 gives \((\mathbf T^{\rm sf}_{j-1}F)(gW)=(\mathbf T^{\rm sf}_{j-1}F)(W)\). Both are positive reals, so their logarithms agree. Also \(xA(U_j(gW))-S_j(U_j(gW))=xA(U_j(W))-S_j(U_j(W))\), by Lemma 1 (a) and Step 2. So \(\mathcal E^{(j)}(gW)=\mathcal E^{(j)}(W)\). For j = 1 the list is empty (SA 20649), \(U_0(V)=V\), and Steps 1-2 are void. This proves (i).

*(ii).* By (ID) and Lemma 1 (a), \(\mathrm{Tot}\,E^{(j)}(g\cdot\mathbf p_{U_j(W)})=\mathrm{Tot}\,E^{(j)}(\mathbf p_{U_j(gW)})=\mathcal E^{(j)}(gW)+c_j\). Apply (i).

*(iii).* For real B near 0, \(e^{iB}\in\mathcal K_j\) (R15), and \(P_j(g\cdot B)=g\cdot P_j(B)\) (`b2-extract.md` §4, the \(P_j\) side). Both sides of (ii), composed with \(P_j\), are holomorphic near 0 (A1 (9.2) and the member cores). They agree on a real open neighbourhood of 0. A holomorphic function on a connected domain that vanishes on a real open set vanishes identically. \(\square\)

**What the proof does not use.** No covariance of any large-field rule enters: the regular totals read only the kernel, the backgrounds, the list totals and the inserted families (SA 17548: \(E^{(j+1)}\) comes from the part with the old R-terms; it is the same for every label). Localization rules never enter a total.

### 3.5 Consequence: (R14) and (20) for every old regular member

**Corollary R14 (implication; proved by Claude, not yet checked).** Assume the hypotheses of Theorem TI. Let \(G=E^{(j)}\) be an old regular member, and \(\bar G\) its re-pointing by Lemma R of `b2-extract.md` on each symmetric torus.
- (a) \(\bar G\) has the total of G at every pair covered by Theorem TI (ii)-(iii), by Lemma R (v). So \(\bar G\) is a localization of the same step functional, and SA 6229-6231 allows it as the supplied rule.
- (b) \(\bar G\) satisfies (R14) (Lemma R (i)), with \(\|\bar G\|\le\|G\|\), the same locality, gauge invariance and reality, and the rooted count multiplied by at most \(M^4\) (Lemma R (ii)-(iv)). Its companion exists by Lemma R's companion argument, given the grid covariance of the terms of G (checked in ti-cov §1).
- (c) With \(\bar G\) adopted, Theorem P gives (20) at every base point, with the single coefficient \(b_j=b[\bar G]\). This is the bulk coefficient of the Hessian of the total at the trivial datum, so the total fixes it. (D), (C), (G), (Mo) pass to \(\bar G\): (Mo) with \(\sup_zC_m(z)\).
- (d) So the pointed Hessian cancellation retained by `wf7-bf.md` §3 and `cond-c.md` §§6.1-6.2 holds for every old regular member. B4's (19) for the regular members follows from Proposition W of `b2-extract.md`, given (ER8u), (BX), (UR) and (YA).

Theorem P and Lemma R were checked line by line by Codex (ti-cov §1).

## 4. Without (INS): what the covariant route needs

Theorem TI also holds with plain insertion (H itself in the list) under **(R-inv)**: the total of every inserted remainder is \(\mathfrak G^{(m+1)}\)-invariant at every read pair. By Lemma 4 (d), (R-inv) says exactly that every \(D_H\) has total zero. Then (INS) and plain insertion give the same list action.

(R-inv) follows from two inputs.
- **(NAT)** Every rule that the total of H reads is natural: covariant under every isometry when the grids, frames and parameters are carried.
- **Lemma 3 (b).** At the insertion age, every element of \(\mathfrak G^{(m+1)}\) preserves all those grids, and it fixes the origin's centred partitions.

Then \(g_*H\) has the total of H, by reindexing polymers, histories and frames, as in YM3_I 38578-38609 and ti-cov §3 (last paragraph).

**Status of (NAT).** The family \(R^{(k)}\) contains the healed-gas part of SA 17996, so its total reads the large-field operation. Rules that only split a fixed total do not enter: the Definition A localizations, Rule W, box first, the stopping nest of `s210-fix.md` Lemma N', and the filing in Lemma P. Rules that change the integrand must be natural. With (N), (T) and (F), ti-cov §3 gives naturality for every rule of the lead's list: Definition A and the cube-localised test backgrounds ((A7)), the half-cell profile, the nests, Definition D and [RED], the stored carrier series, Definition R, and the frame sum (SA 17585). I did not audit the rest of the operation: the stage tests at the sharper threshold, the strip rules (L0)-(L4) of `s210-3.md` and `s210-fix.md`, the healing gauge (SA 17664) and the hard-core decomposition. Their wording uses region membership, test outcomes, distances and frames only, but naturality is not proved here. So (NAT) stays open beyond the lead's list. (INS) makes it unnecessary for (TI). Under complete naturality the defect of (INS) vanishes.

## 5. The first input that is not supplied: (DOM)

In the order in which the induction step reads its inputs, the first one that no checked note supplies is **(DOM)**: the backgrounds of the whole-lattice fluctuation support lie in the earlier members' covariance classes. A1 is checked (row 81; conditional on its cited flat kernels F0). (Id) is the adopted reading of `b2-extract.md` §4. (K) is a reading of SA 7142 and 17336. (DOM) is cited from SA (Lemma 2.2 (a), SA 17369; the threshold ratio at SA 7873; closure at SA 20636-20646) and is not rebuilt: `s210-fix.md` cites Lemma 2.2 as (L2.2), and `sa-histories.md` lists it as conditional. (ID) is B4's own identity and stays open with B4.

**What (DOM) reduces to (sketch, not proved).**
1. *Downward clauses.* If \(W\in\mathcal K_j\), then \(\mathcal M^iU_j(W)\in\mathcal K_i\) for \(i<j\). By Lemma 1 (b), \(U_j(W)=U_i(\mathcal M^iU_j(W))\). In level-i units its curvature is the level-j curvature times \(L^{-2(j-i)}\), and its current gains \(L^{-3(j-i)}\). The (R15) radii \(c\,\varepsilon(\theta)\) change by at most a polynomial factor in \(j-i\), by the frame bound \(\theta_i\le\theta_j+\bar B(j-i)\). The tower and core clauses need the same comparison; I did not write them out.
2. *The one-step clause (DOM1).* If \(W\in\mathcal K_j\) and V is in the support at W, then \(V\in\mathcal K_{j-1}\) and \(U_{j-1}(V)\in\mathcal N_{j-1}\). At \(\mathcal A=0\), \(V=V^{\rm bg}\) and \(U_{j-1}(V^{\rm bg})=U_j(W)\) exactly, by the argument of Lemma 1 (b). Its level-(j-1) curvature is at most \(L^{-2}c\,\varepsilon(\theta_j)\). The fluctuation moves the background by at most \(B'\delta_{j-1}\), by the background response (A3, `a3-*.md`). With \(\delta_{j-1}=(A_1/A_0)\varepsilon_{j-1}\), (R15) at level j-1 follows once \(L^{-2}\varepsilon(\theta_j)\le\frac12\min\{\varepsilon(\theta_{j-2}),\varepsilon(\theta_{j-1})\}\) and \(B'(A_1/A_0)\varepsilon(\theta_{j-1})\le\frac c4\min\{\varepsilon(\theta_{j-2}),\varepsilon(\theta_{j-1})\}\). The second is a choice of \(A_1/A_0\) after c and B', given that neighbouring thresholds are comparable. This is SA's Lemma 2.2 (a) mechanism.
3. *Invariance and cores ((d), (e)).* Every clause is a bound on plaquette deviations, currents, test loops and localised backgrounds. Read with the intersection of translates (Section 3.1), the classes are invariant. The localised backgrounds of offset towers obey the same estimates as those of the fixed grid, because Definition A is natural ((A7)).

So (DOM) needs A3's response bound on the real support at the class radius, and the order of constants above. That is a quantitative statement of the step construction (B4), not a symmetry statement. This is the second reduction of this item, so I stop here.

## Result

**Check (Section 1).** `ti-cov.md` Sections 2-5 (Codex): checked line by line by Claude, first failing step none. (1)-(3), the WRONG counterexample (4) to the formation-rule implication, the selector (5), the aged-data divisibility, (6) and (7) ADVANCE as implications. Three precisions: the sharp box needs an exactly covariant base (the \(\operatorname{Ax}^\circ\) background, (K)); later backgrounds need compatibility (Lemma 1 (b)) and (DOM); the divisibility also covers the older region grids and the test-cube grids (Lemma 3).

**Adopted (Section 2).** (N) the symmetric nest selector (5); (T) the frame-ordered tie rule for Definition R; (F) averaged filing in Lemma P; (INS) symmetric insertion of aged remainders, with the defect \(D_H\) filed under SA 4007-4010. Every reader in `geo-*.md`, `geo5c-count.md`, `cond-c.md`, `inn-213.md`, `inn-fix.md`, `carrier-adopt.md`, `b4-step.md` (19) and `b2-extract.md` Proposition W is kept; (N) holds with K = 2.

**Proved here by Claude, not yet checked by the other model.**
- Lemma 1: covariance and compatibility of the backgrounds on the full support, from A1's uniqueness and the isometry-invariant contour slice.
- Lemma 3: \(\check R_i\le L^{j-i}\check R_j\), and at the insertion age the level-(m+1) group preserves every grid a remainder reads.
- Lemma 4: the inserted family \(\mathcal R_{m+1}H\) has invariant totals, norm at most \(\|H\|\), the same partitions, a companion, and \(\|D_H\|\le2\|H\|\).
- **Theorem TI.** Under (A1), (Id), (K), (DOM), (ID) and (INS), every regular step functional and every regular total is invariant under the level-j torus group, at every background the chain reads, and on the continued domain near the trivial datum. The proof uses no covariance of any large-field rule.
- **Corollary R14.** With Lemma R's re-pointing adopted, (R14) holds for every old regular member, and Theorem P gives (20) with one coefficient \(b_j=b[\bar G]\), fixed by the total.

**First input not supplied:** (DOM), the real inclusion of the fluctuation support's backgrounds in the earlier covariance classes (SA Lemma 2.2 (a) mechanism; cited, not rebuilt). It reduces to A3's response bound on the real support at the class radius and the order of constants of Section 5.

**Still open.** (DOM); (ID), which is B4's identity; (NAT) beyond the lead's list, needed only if (INS) is not adopted; the check of this note. For B4's (19), still (ER8u) = (ER7), (BX) (with `bx.md`'s counterexample, row 210), (UR) and (YA).

**What would change.** If (DOM) and (ID) hold, (TI), (R14) and (20) hold for every old regular member, and B4's (19) and WF7's retained premise reduce to (ER7), (BX), (UR) and (YA). If (INS) is refused, (TI) also needs (NAT) for every pre-frame rule of the large-field operation.

**Evidence for other owners (not edited here).**
- `geo-3.md` §2 and `geo-prop23.md` (3.3): the adopted nest selector is now (N); formation compatibility holds for it with K = 2 (Section 1, (5)).
- `inn-213.md` §7a, Definition R: add the tie rule (T).
- `carrier-adopt.md` Lemma P: use the averaged filing (F); (P) is unchanged.
- `b2-extract.md` §6 and §8: "(TI) is not proved" becomes "(TI) proved as an implication from (DOM), (ID), A1, (Id), (K) and (INS) (`ti-2.md`, not yet checked)".
- `t0-skeleton.md` row B2: open item "(R14) ⇐ (TI)" becomes "(TI) ⇐ (DOM), (ID)".
- `b4-step.md` §11, `wf7-bf.md` §3, `cond-c.md` §§6.1-6.2: (20) is available for every old regular member under Theorem TI's premises.
- A candidate for Sussman-Alpoge, after Codex checks it and only with the owner's approval of the text: their outline asserts (R14) for all isometries (SA 5889-5898, 7581) but supplies no covariant nest selector (SA 17398-17415), and ti-cov (4) shows that a nest meeting their stated bounds can break reflection covariance. Lemma R, Theorem TI and (N) give a proof route for (R14) under their own closure requirements.

**Numerics.** None were run. Every step is by hand.
