# O4-2pt: two-point O(4) invariance without H-U? (research text, 2026-11-05)

Provenance: Claude Opus 5.5 (subagent of the lead), 2026-11-05. Research text, not an audit. It grants no status. One reading by one model; no other model has checked it. Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the complete account (CA), the outline, and the plate, two-point and angular methods that RO1 ports.

**Question.** Does RO1 Theorem 6 (ro1.md L483) give two-point O(4) invariance without H-U (UV1, rooted D1), from CA statements at CA standing plus frozen LG1 and CL1?

**Short answer.** Yes, for the connected two-point function of volume-first limits through torus-limit DLR states. H-U enters Theorem 6 only through the plate vectors \(B_{\varphi;a}\Omega\) and their \(a^{-5}\) bound. For \(n=2\) the vectors (not the operators) suffice. They follow from CA (iii-b), used only qualitatively, plus the cube cone. The finite band is not needed: the spectral bound plus CA (iv) kills every \(|m|\ge2\) on horizontal lines. The rest of Theorem 6 runs unchanged. This proves, for that class of limits, the implication of CA Remark 10.1 (CA-III L79931–79990), whose proof CA does not reproduce (L79964–79966), and it supplies Remark 10.1's hypothesis (d) from LG1 + CL1.

Sources read (bounded ranges): `ro1-vs-ca.md` whole (L1–153); `ro1.md` whole (L1–702); `cl1.md` L1–335, L355–536; `lg1.md` L9–30, L365–367, L425–438, L460–485 and its header list; `sr1.md` header list and L540–568. CA-I L690–730, L2575–2800. CA-III L79931–79990, L110826–110836, L110862–110970, L110998–111012.

## 1. Where H-U enters RO1's proof of Theorem 6

A grep of ro1.md for "H-U", "rooted", "D1", "UV1" gives L54–62 (the import), L88–90 (constant order), L121 (Lemma 2 hypothesis), L161–166 (rooted count), L630 and L649 (Theorem 9), L668, L680, L689, L693 (records). No lemma after Lemma 2 names H-U. It reaches Theorem 6 through this chain.

**U0. Lemma 2 (UI), L121–215.** H-U is used here only. The rooted count (2.4) L163 and the decay sums (2.5) L168–171 use H-U's domain terms. The per-cell costs and \(B_0\) (2.6) L183–185 use H-U's \(C_{\rm st}\). The normalizer \(E_h\) L175, L191 uses locality and representation independence. Output: the insertion bound (2.1) L129, with a constant "independent of the numbers and coefficients of outside fields" (L132).

**U1. Lemma 3 (PD), L217–288.** "Lemma 2 applied to outside polynomials shifted forward by \(\eta/4\) gives a bounded form" (L245). This gives the plate operators \(B_{\varphi;a}\) and their bound \(\|B_{\varphi;a}\|\le Ca^{-5}\|\varphi\|_1\) (3.3) L237.

**U2. Lemma 4 (AK), L292–401.** The kernel (4.3) L314 is a product of plate operators. Its bound \(\delta^{-5n}\) (4.5) L327 comes from (3.3). That bound gives growth \(e^{5n|\Im z|}\) on pencils (L366) and hence the finite band \(4|m|\le5n\) (4.1) L296, L367–370. For \(n=2\) the band is \(|m|\le2\). The density formula (4.6) L340 also uses the plates.

**U3. Lemma 5, L405–481.** The spectral measure uses \(\zeta_{\varphi,a}=(1-P_\Omega)B_{\varphi;a}\Omega\) (L416). Finiteness of \(\Gamma(t)\) uses (4.3) (L420). The planar density formula for disjoint supports uses (4.6) (L422). The TU10 part (L424–481) uses only \(\mu\), (5.2) and H-T.

**U4. Theorem 6, L483–554.** The expansion \(g_r(z)=\sum_{m=-2}^2a_m(r)e^{4imz}\) is "Lemma 4 gives" (L487–489), that is, the band U2. The imaginary-axis bound (L493–494) then needs only \(\mu\) and \(\Gamma\). The diagonal step (L503–508) uses "the density formula and continuity" for the point limit, that is, U3. The remaining steps (L509–554) use only \(\mu\), \(\Gamma\), (6.1), the diagonal form and Fourier–Laplace uniqueness.

**U5. Hidden route through H-C.** RO1's H-C is "CL1(2)–(4), with its local SR1 bounds" (L66). CL1 imports these bounds as I3 from SR1 (cl1.md L63–74). SR1 "itself retains UV1's full D1" (cl1.md L74); SR1 status "Import UV1 ... remains open" (sr1.md L568). So RO1 Theorem 6 also uses D1 through the bounds behind its Hilbert spaces.

**What each use gives, for \(n=2\).** U0–U1 give two things: (i) existence of the sandwiched point vectors \(B_{\varphi;a}\Omega\); (ii) the power \(a^{-5}\). Theorem 6 uses (i) through U3 and U4. It uses (ii) only to get the band in U4. It never uses the operator character of \(B_{\varphi;a}\) between outside polynomials at \(n=2\): \(K_2(v)=\langle B_{\varphi_1;a}\Omega,T(v-2ae_0)B_{\varphi_2;a}\Omega\rangle\) by self-adjointness of real-label plates (L241). U5 gives position-uniform two-point bounds at fixed geometry.

**Where H-U is needed beyond \(n=2\).** The operator character (outside-field independence, L132) is needed for \(n\ge3\): the product kernels (4.3), the Gram identity (4.7) L361 and Lemma 7 (L558–582) sandwich plates between other fields. The diagonal-flat extension \(\Sigma_n\) needs H-S (L586, L628), that is SR1, that is D1. Neither is needed for the two-point statement on separated tests.

## 2. Replacing each use at \(n=2\)

**U5 → CA (iii-b).** CA-I L2610–2622: for \(n\ge2\), \(R,\mathsf d>0\), "there is \(C^\infty_n(\mathsf{d};R)\), independent of \(K\), \(g_0\), \(m\) and the position and non-increasing in \(\mathsf{d}\)", with \(|S^T_{n;K,m}(\vec f)|\le C^\infty_n(\mathsf d;R)\prod_i\|f_i\|_\sharp\), for \(L^m\ge\ell(n,R,g)\), every \(g_0\in(0,g_-(g)]\), real Lipschitz \(f_i\) in radius-\(R\) balls at mutual distance \(\ge\mathsf d\). CA's norm is \(\|f\|_\sharp=\max\{\|f\|_\infty,40M\operatorname{Lip}f\}\) (CA-I L713), which is CL1's \(\|\cdot\|_\sharp\) (cl1.md L28) with \(c_M=40M\). CA's field is \(\mathcal O(f)=\sum_pf(x(p))[1-\operatorname{Re}\operatorname{tr}U(\partial p)]\), \(\operatorname{tr}\mathbf1=1\) (CA-I L697–699); this is CL1's (1) (cl1.md L11–12) and RO1's (L11–12). The Wilson action is \(A(U)=\sum_p[1-\operatorname{Re}\operatorname{tr}U(\partial p)]\) (CA-I L128), so \(\beta=g_0^{-2}\).
- CL1 uses I3 at order \(n\) only through "a position-independent bound \(M_n(d,R)\prod_i\|f_i\|_\sharp\)" (cl1.md L127, (6) L133–135) and, in Lemma 5, through boundedness under normal translation (L302). Only orders \(n\le2\) occur when every polynomial has degree \(\le1\). In the self-centered case \(\rho_j=\nu_j\), \(m_{j,1}=0\) and \(m_{j,2}=\kappa_2^{\rho_j}\) (cl1.md L182, L191). So (iii-b) at \(n=2\) supplies I3 for these orders. Monotonicity in \(\mathsf d\) covers L302, since normal translation does not decrease opposite-side distances (L298–301).
- Standing: CA-III L110895–110899. The bound "is proved as an implication from the correlation theorem", one Balaban inequality cited by statement, lattice reflection positivity "and the uniformity of the last-scale constants in the torus exponent. The last of these is of status ``stated; proof incomplete''."

**U0–U1, item (i) → point vectors from (iii-b) and the cube cone.** Lemma A below. It needs only that one-field vectors \([k]\) depend \(\|\cdot\|_\sharp\)-continuously on \(k\) at fixed geometry (from (iii-b)) and that \(w\mapsto T(w)\) is holomorphic on the cube-cone tube (CL1 Lemma 8). It uses RO1's parametrix (3.6) (L265–274), which is calculus, not a Yang–Mills estimate. It gives no power of \(a\). This matches CA's remark that its hypothesis (b) "enters it only qualitatively" (CA-III L79966).

**U0–U1, item (ii), and U2 → spectral bound plus CA (iv).** No a priori band is needed. In the time picture, \(|G(R_z(r,0))|\le\Gamma(r\cos\Re z\,e^{-|\Im z|})\) on \(|\Re z|<\pi/2\), from the spectral formula and the planar cone alone (Step 7 below). Hypercubic quarter turns glue these strips to an entire \(\pi/2\)-periodic function bounded by \(\Gamma(re^{-|\Im z|}/\sqrt2)\) on every horizontal line. RO1 Lemma 5's TU10 argument (L424–481), unchanged, gives \(t^8\Gamma(t)\to0\). Cauchy's formula on horizontal lines then kills every Fourier mode with \(|m|\ge2\). This is the same mechanism as RO1 L493–496, applied to the whole line rather than the imaginary axis. RO1's change log already records that the exponent of the band is not load-bearing (L700).

**U3, U4 → unchanged once \(\mu\), \(\Gamma\) and the density formula exist.** Lemma 5's TU10 part uses H-T only through test pairs \((\theta f_i^\pm,f_i^\pm)\in\mathfrak T(5h/2;\vartheta_*)\) (L455–466). CA (iv) supplies H-T for torus-limit states (below). Theorem 6 from (6.1) on (L496–554) uses no plate.

**The \(n=2\) step from planar kernels to all tests (RO1 Lemma 8 at \(n=2\)).** RO1 Lemma 8 uses plates only through (4.6) (L611) and the cube cone through (8.1)–(8.2) (L593–604). At \(n=2\) both are available without H-U. Step 9 below gives a shorter version.

**Conclusion of Task 2.** Every use of H-U in Theorem 6 at \(n=2\) is replaced by CA (iii-b) (qualitative), CA (iv) (upper member), LG1, and CL1 Lemmas 1–3, 5, 7, 8 read at degree \(\le1\). H-U is needed only for \(n\ge3\) (operator plates) and for the diagonal-flat extension (H-S).

## 3. The theorem

**Standing hypotheses (CA's).** \(N=2\); CA's hypotheses for clauses (iii) and (iv) (CA-I L2598, "\(N=2\); (H7)"; L2716–2717, "in the regime of (iii)"). Fix \(\vartheta_*=1/12000\in(0,1]\) and \(g\le\gamma_W^{\mathbb T}(\vartheta_*)\) (CA-I L2720–2721, L2765; note \(\gamma_W^{\mathbb T}\le\gamma_J\), L2721).

**The class \(\mathfrak V\) of volume-first limits.** Take \(g_0^{(j)}\in(0,g_-(g)]\) with \(K_j=K(g_0^{(j)},g)\to\infty\), bare spacing \(a_j=L^{-K_j}\) (CA-I L690), \(\beta_j=(g_0^{(j)})^{-2}\) (CA-I L128). Let \(\rho_j\) be a weak limit point, as \(m\to\infty\), of the periodically lifted Wilson laws on \(\mathbb T_m\) at cutoff \(K_j\) (the class \(\mathcal G^{\rm tor}_{a_j,\beta_j}\), cl1.md L17). Suppose
\[
 S_2(f,h)=\lim_{j}\kappa_2^{\rho_j}\bigl(\mathcal O_{a_j}(f),\mathcal O_{a_j}(h)\bigr)
 \tag{V}
\]
exists for all real \(f,h\in C^1_c(\mathbb R^4)\) with disjoint supports. Then \(S_2\in\mathfrak V\). Step 1 shows that every such sequence has a subsequence with (V). The observable is CA's smeared action density (CA-I L697–699), with no spacing prefactor; \(\kappa_2\) is the connected (cumulant) function, so no centering state enters.

**Theorem O4-2.** Under the standing hypotheses, every \(S_2\in\mathfrak V\) satisfies
\[
 S_2(Rf,Rh)=S_2(f,h)\qquad(R\in\mathrm O(4)),
 \tag{O4-2}
\]
for all real (hence, by bilinearity, complex) \(f,h\in C^1_c(\mathbb R^4)\) with disjoint supports, \(Rf=f\circ R^{-1}\).

**Inputs and their standing.**

| | Input | Source | Standing |
|---|---|---|---|
| A | (iii-b) at \(n=2\), used only qualitatively | CA-I L2610–2622 | CA: proved as an implication; rests on one item "stated; proof incomplete" (CA-III L110895–110899) |
| B | (iv), upper member, and \(s(\mathsf d)\to\infty\) | CA-I L2745–2746, L2758–2789 | CA: proved as an implication (CA-III L110909–110918); beneath it one "stated; proof incomplete" part (L110943), the source lemma and flat shell bound "with their proofs outstanding" (L110953–110954), and the continuum kernel, "whose statement and proof are not written out" (L110955) |
| C | LG1: every periodic Wilson DLR state at \(\beta>0\) is \(\mathbb Z^4\rtimes W_4\)-invariant and RP at coordinate site, coordinate bond and diagonal lattice mirrors | lg1.md Theorem 10 L365, Theorem 13(5) L431 | Frozen (L485); "No mathematical step ... is left **Outstanding**" (L475); one Claude gate. Not a CA statement: CA uses no diagonal RP (CA-III L79973–79977) |
| D | CL1 Lemmas 1, 2, 3, 5, 7, 8, read for polynomials of degree \(\le1\), with A in place of I3 | cl1.md L99–199, L275–324, L362–453 | CL1 frozen as an implication from SR1, LG1, IN1(4) (L536). The substitution of A for I3 is checked in §2 of this note (one reading). Lemma 7 is measure theory only |
| E | RO1 text used unchanged: parametrix calculus (3.6); Lemma 5's TU10 argument; Theorem 6 after (6.1); SO(4) generation | ro1.md L265–274, L424–481, L496–554, L645 | RO1 frozen as a conditional implication (L702). These parts use no H-U once \(\mu\), \(\Gamma\) and the density formula are given |

**Not used:** H-U (UV1, D1), SR1 and H-S, IN1, PH1, TP1, (IR-fl), CA clause (ii-\(\mathbb R^4\)) itself, CA's correlation theorem directly. No computation is a proof step.

## 4. Proof

Coordinates: \(t=x_4\) is time; the rotation plane is \((t,u)=(x_4,x_1)\); \(z=(x_2,x_3)\) is transverse. CA's \(e_0\) is our \(e_4\) (CA-III L79937). A planar rotation \(R_\vartheta\) acts as in RO1 (D.3) L33, with \(R_z(r,0)=(r\cos z,r\sin z)\) (consistent with RO1 L535).

**Step 0. Lattice states and the CA bounds.** Fix \(j\). CL1 Lemma 1 (cl1.md L101) gives that \(\rho_j\) exists and is a translation-invariant Wilson DLR state; its proof (L105–113) uses only \(a_j,\beta_j>0\), not IN1's data. So \(\rho_j\) is periodic, and LG1 (input C) gives \(W_4\)-invariance and RP at coordinate site, coordinate bond and diagonal lattice mirrors. For fixed compact \(f,h\), finitely many plaquettes carry \(\mathcal O(f),\mathcal O(h)\). Weak convergence gives \(\kappa_2^{\rho_j}(\mathcal O(f),\mathcal O(h))=\lim_m S^T_{2;K_j,m}(f,h)\) along the defining torus sequence (as at cl1.md L470). Both A and B are uniform in \(m\) (CA-I L2611, L2782) and in the position. So A and B hold for \(\kappa_2^{\rho_j}\) with the same constants.

**Step 1. Limit, symmetries, positivity (CL1 Lemmas 2–3 at degree \(\le1\)).** Work with the self-centered pair \((\rho_j,\rho_j)\), so \(m_{j,1}=0\) and \(m_{j,2}=\kappa_2^{\rho_j}\) (cl1.md L182, L191). Input A with complexification gives (6) at \(n\le2\) with \(M_2(d,R)=4C^\infty_2(d;R)\). CL1 Lemma 2 (L117–140) then gives one subsequence with (V), and moving-test continuity. CL1 Lemma 3 (L144–165) gives: \(S_2\) is symmetric, real, invariant under translations and \(W_4\). The functional \(\sigma_S\) with \(\sigma_S(1)=1\), \(\sigma_S(f)=0\), \(\sigma_S(f,h)=S_2(f,h)\) is RP at every coordinate and diagonal affine mirror on polynomials of degree \(\le1\). The proof rounds the mirror to the lattice (L157), uses lattice positivity from LG1 (L159–162), and passes to the limit by (6). Bounds A and B pass to \(S_2\).

**Step 2. One-field Hilbert spaces (CL1 Lemma 5 at degree \(\le1\)).** For a coordinate or diagonal unit normal \(u\), put \(V_u^{\le1}=\operatorname{span}\{1,(f):\operatorname{supp}f\subset\{u\cdot x>0\}\}\). CL1 Lemma 5 (L277–324) on this space gives a separable Hilbert space \(\mathcal H_u\), vacuum \(\Omega\), normal contraction semigroup \(e^{-tH_u}\), \(H_u\ge0\), strongly continuous tangential unitaries, and the dictionary (17) (L286–289). The only bound it uses is the fixed-geometry bound at order 2, monotone under normal translation (L302): input A. One-field classes are orthogonal to \(\Omega\) because \(\sigma_S(f)=0\). Write \(\mathcal H=\mathcal H_{e_4}\), \(U_x=e^{ix\cdot P}\), \(\Pi\) for the joint spectral measure of \((H,P_1,P_2,P_3)\), and \(T(w)=\int e^{-w_4E+i\mathbf w\cdot\mathbf q}\,d\Pi\).

**Step 3. Cube cone (CL1 Lemmas 7–8 at degree \(\le1\)).** In CL1 Lemma 8 (L418–453) take \(F\) of degree \(\le1\). Then (27) (L434–438) involves only \(S_2\) and the one-field spaces of Step 2; \(F,rF\in V_u^{\le1}\) as written there (L427–431). Lemma 7 (L364–414) is a statement about measures and two operators; it needs nothing else. The time-shift and injectivity argument (L442) stays inside \(\mathcal H\). So \(\Pi\{E<\max_i|q_i|\}=0\). By \(W_4\) the same holds in each coordinate picture. Consequently, for \(\Psi\in\mathcal H\), \(w\mapsto T(w)\Psi\) is norm-holomorphic on \(\{\Re w_4>\sum_{j\le3}|\Im w_j|\}\), and
\[
 \|\partial_w^\alpha T(w)\Psi\|\le|\alpha|!\,\delta^{-|\alpha|}\|\Psi\|
 \quad\text{when }\Re w_4-\textstyle\sum_j|\Im w_j|\ge\delta>0,
 \tag{4.1}
\]
since the multiplier's derivative is bounded by \(E^{|\alpha|}e^{-\delta E}\le|\alpha|!\delta^{-|\alpha|}\) (the reasoning of RO1 L255). For real \(w\) with \(w_4\ge0\) and positive-time \(k\), \(T(w)[k]=[\tau_wk]\) by (17).

**Step 4. Lemma A (point vectors, without H-U).** *There is a continuous map \(y\mapsto P(y)\in\mathcal H\) on \(\{y_4>0\}\) with:*
*(i) \([k]=\int k(y)P(y)\,dy\) (Bochner) for every compact \(C^1\) \(k\) supported in \(\{y_4>0\}\);*
*(ii) \(P(y+se_4+x)=e^{-sH}U_xP(y)\) for \(s\ge0\), \(x\in\mathbb R^3\).*

*Proof.* (a) *Continuity of the class map.* For positive-time \(k,k'\), the supports of \(\theta k\) and \(k'\) are separated, so \(k\mapsto[k]\) is linear. For \(k\) in a fixed container \(B(c,\varrho)\) with \(c_4>\varrho\), \(\|[k]\|^2=S_2(\theta\bar k,k)\le4C^\infty_2(2(c_4-\varrho);\varrho)\|k\|_\sharp^2\) by input A (Step 1). So the class map is \(\|\cdot\|_\sharp\)-continuous on each such container. Riemann sums of \(y\mapsto g(y)\tau_yn\), for continuous compact \(g\) and \(C^1\) compact \(n\), converge in \(\|\cdot\|_\sharp\) (uniform continuity of \(\nabla n\), as in cl1.md (7) L150–153). Hence \([g*n]=\int g(y)[\tau_yn]\,dy\) when all translates stay in one container.
(b) *Local construction.* Fix \(y_0\) with \(b=y_{0,4}>0\). Put \(r=b/16\), \(z_*=y_0-(b/2)e_4\). Take RO1's \(n_r,s_r\) (3.6), L267–273: \(n_r\) is \(C^1\), \(s_r\) is smooth, both are supported in \(B(0,r)\), and \(\Delta^3n_r=\delta_0-s_r\). Set \(\Psi_n=[\tau_{z_*}n_r]\), \(\Psi_s=[\tau_{z_*}s_r]\); both supports lie at times \(\ge b/2-r>0\). For \(y\in B(y_0,b/8)\) define
\[
 P(y)=\Delta_y^3\,T(y-z_*)\Psi_n+T(y-z_*)\Psi_s .
\]
Here \((y-z_*)_4\ge3b/8\), so (4.1) applies with \(\delta=3b/8\) and \(P\) is real-analytic. By Step 3, \(T(y-z_*)\Psi_n=[\tau_yn_r]\).
(c) *Representation.* For smooth \(k\) supported in \(B(y_0,b/16)\), RO1 L274 gives \(k=(\Delta^3k)*n_r+k*s_r\). Both terms are supported in \(B(y_0,b/8)\), at positive time. By (a), \([(\Delta^3k)*n_r]=\int(\Delta^3k)(y)T(y-z_*)\Psi_n\,dy\). Integrate by parts six times; \(k\) has compact support and the vector function is smooth, so there are no boundary terms. With the \(s_r\) term this gives \([k]=\int kP\). Mollification and (a) extend this to compact \(C^1\) \(k\) in the ball.
(d) *Gluing.* Two local constructions give continuous \(P,P'\) with \(\int k(P-P')=0\) for every smooth \(k\) on the overlap. Pairing with any vector shows \(P=P'\) there. So \(P\) is defined on \(\{y_4>0\}\), and (i) follows by a partition of unity.
(e) *Covariance.* For \(s\ge0\), \([\tau_{se_4+x}k]=e^{-sH}U_x[k]\) by (17). Both sides of (ii), integrated against every smooth \(k\), agree by (i). Continuity gives (ii). \(\square\)

No power of the distance and no outside-field independence enters. This is the point where H-U (U0–U1) is removed at \(n=2\).

**Step 5. Planar kernel, spectral measure, density formula.** For real compact \(C^1\) \(\varphi\) on \(\mathbb R^2_z\), put \(P_\varphi(t,u)=\int\varphi(z)P(t,u,z)\,dz\) (\(t>0\)) and \(\zeta_{\varphi,a}=P_\varphi(a,0)\). Then \([\alpha\otimes\varphi]=\int\alpha(t,u)P_\varphi(t,u)\,dt\,du\) for planar compact \(C^1\) \(\alpha\) at positive times (Lemma A(i), Fubini). Define, as RO1 L417–419,
\[
 d\mu=e^{2aE}\,d\langle\zeta_{\varphi,a},\Pi^{(E,q_1)}\zeta_{\varphi,a}\rangle,\qquad
 G(t,x)=\int e^{-tE+ixq}\,d\mu\ (t>0),\qquad \Gamma(t)=G(t,0).
\]
By Lemma A(ii), \(\zeta_{\varphi,b}=e^{-(b-a)H}\zeta_{\varphi,a}\), so \(\mu\) does not depend on \(a\). It is positive, supported in \(\{E\ge|q|\}\) (Step 3), and \(\Gamma(t)=\|\zeta_{\varphi,t/2}\|^2<\infty\) for every \(t>0\). \(\Gamma\) is non-increasing.
- *Density formula.* If \(\sup\{t:\operatorname{supp}\alpha_1\}<\inf\{t:\operatorname{supp}\alpha_2\}\), then \(S_2(\alpha_1\otimes\varphi,\alpha_2\otimes\varphi)=\iint\alpha_1(y_1)\alpha_2(y_2)G(y_2-y_1)\,dy_1dy_2\). Translate so the cut is \(t=0\). Then \(S_2(\alpha_1\otimes\varphi,\alpha_2\otimes\varphi)=\langle[\theta(\alpha_1\otimes\varphi)],[\alpha_2\otimes\varphi]\rangle\) (RO1 (D.2) L27; \(\varphi\) real). Expand both vectors by Lemma A(i). By Lemma A(ii), \(\langle P_\varphi(s_1,u_1),P_\varphi(s_2,u_2)\rangle=G(s_1+s_2,u_2-u_1)\).
- *Gluing by quarter turns.* Let \(\rho(t,x)=(x,-t)\), a signed permutation of \((x_4,x_1)\); it fixes \(\varphi\). For \(w\) in the open quadrant \(\{t>0,x>0\}\), both \(w\) and \(\rho w\) have positive time. \(W_4\)-invariance of \(S_2\), the density formula in both frames, and continuity give \(G(\rho w)=G(w)\). Put \(G^{\rm gl}(w)=G(\rho^kw)\) for any \(k\) with \((\rho^kw)_t>0\). The quadrant identity makes this well defined. \(G^{\rm gl}\) is continuous on \(\mathbb R^2\setminus\{0\}\) and \(\rho\)-invariant. RO1's partition argument (L422) extends the density formula to all \(\alpha_1,\alpha_2\) with disjoint planar supports. Since some frame has time component \(\ge|w|_\infty\ge|w|/\sqrt2\), \(|G^{\rm gl}(w)|\le\Gamma(|w|/\sqrt2)\).
- *Symmetries.* \(x_1\mapsto-x_1\) is in \(W_4\), so \(G(t,-x)=G(t,x)\). Reality of \(S_2\) makes \(G\) real.
- *Mixed labels.* For real \(\varphi,\psi\) the same construction with \(\zeta_{\varphi,a},\zeta_{\psi,a}\) gives \(G^{\rm gl}_{\varphi,\psi}\) and its density formula.

**Step 6. TU10 gives \(t^8\Gamma(t)\to0\) (RO1 Lemma 5, L424–481, unchanged).** (5.2) L426–427 holds by Step 5: \(\|[\alpha\otimes\varphi]\|^2=\int|\int\alpha e^{-tE+ixq}|^2d\mu\), with the vacuum part zero. The shapes (L432–462) give pairs \((\theta f_i^\pm,f_i^\pm)\) in RO1's \(\mathfrak T(5h/2;\vartheta_*)\). These are compact \(C^1\), so they lie in CA's \(\mathfrak T(\mathsf d;\vartheta_*)\) (CA-I L2758–2763). Input B gives, for those \(\mathsf d\) with \(\max\{s_W,s^\star_{\rm vol},s_T\}\le s(\mathsf d)\) (CA-I eq-main-1, L2767) and all \(j\) with \(K_j-s(\mathsf d)\ge k_W\) (eq-main-2),
\[
 0\le S^T_2(f_1,f_2)\le u(\mathsf d)\|f_1\|_\infty\|f_2\|_\infty,\qquad
 u(\mathsf d)=\tfrac83b_0C_{\mathcal K}\bigl(g^{-2}+\lambda_\sharp s(\mathsf d)-c_5\bigr)^{-2}
\]
(CA-I L2782–2789), uniformly in \(K,g_0,m\) and the position. \(s(\mathsf d)\) is non-increasing in \(\mathsf d\) and tends to \(\infty\) as \(\mathsf d\downarrow0\) (L2745–2746), so the floor holds on some \((0,\mathsf d_0]\). \(\lambda_\sharp\ge c_0/4>0\) (CA-I L1659), so \(u(\mathsf d)\to0\). By Step 0 and (V) the bound holds for \(S_2\). This is H-T (RO1 (H.T) L68–73) for \(\mathfrak V\). The rest of RO1 L463–481 then gives \(m_\mu(Q)=o(Q^8)\) and \(t^8\Gamma(t)\to0\).

**Step 7. Entire periodic extension; all \(|m|\ge2\) vanish (replaces RO1 Lemma 4's band).** Fix \(r>0\) and an equal real label. On the strip \(S_0=\{|\Re z|<\pi/2\}\) put
\[
 H_0(z)=\int e^{-r\cos z\,E+ir\sin z\,q}\,d\mu .
\]
For \(z=\vartheta+is\): \(\Re(r\cos z)=r\cos\vartheta\cosh s\), \(\Re(ir\sin z\,q)=-rq\cos\vartheta\sinh s\). The cone \(|q|\le E\) gives \(E\cosh s+q\sinh s\ge Ee^{-|s|}\). So the integrand has modulus at most \(e^{-r\cos\vartheta\,e^{-|s|}E}\). Since \(\Gamma(t)<\infty\) for all \(t>0\), dominated convergence makes \(H_0\) holomorphic on \(S_0\), with
\[
 |H_0(\vartheta+is)|\le\Gamma(r\cos\vartheta\,e^{-|s|}),\qquad H_0(\vartheta)=G(R_\vartheta(r,0))\ (|\vartheta|<\pi/2).
 \tag{7.1}
\]
Define \(g_r(z)=H_0(z-k\pi/2)\) on \(S_k=S_0+k\pi/2\). Adjacent strips overlap in \(\{k\pi/2<\Re z<(k+1)\pi/2\}\), which is connected; non-adjacent open strips do not meet. On the real part \(\vartheta\in(0,\pi/2)\) of the overlap of \(S_0,S_1\): \(H_0(\vartheta-\pi/2)=G(r\sin\vartheta,-r\cos\vartheta)=G(\rho R_\vartheta(r,0))=G(R_\vartheta(r,0))=H_0(\vartheta)\) by the quadrant identity of Step 5. The identity theorem gives agreement on the whole overlap; shifts give the other overlaps. So \(g_r\) is entire, \(\pi/2\)-periodic, and equals \(G^{\rm gl}(R_\vartheta(r,0))\) on the real axis. Each real \(\vartheta\) lies within \(\pi/4\) of some \(k\pi/2\), and \(\Gamma\) is non-increasing, so by (7.1)
\[
 \sup_{\vartheta\in\mathbb R}|g_r(\vartheta+is)|\le\Gamma\bigl(re^{-|s|}/\sqrt2\bigr).
 \tag{7.2}
\]
The entire periodic \(g_r\) descends under \(w=e^{4iz}\) to a holomorphic function on \(\mathbb C\setminus\{0\}\) (as RO1 L370). So \(g_r(z)=\sum_{m\in\mathbb Z}a_me^{4imz}\), locally uniformly, with \(a_m=\frac2\pi\int_0^{\pi/2}g_r(\vartheta+is)e^{-4im(\vartheta+is)}d\vartheta\) for every \(s\). Thus \(|a_m|\le e^{4ms}\Gamma(re^{-|s|}/\sqrt2)\). By Step 6, for every \(\varepsilon>0\) there is \(t_\varepsilon\) with \(\Gamma(t)\le\varepsilon t^{-8}\) for \(t<t_\varepsilon\). For \(m\ge2\) take \(s=-\sigma\to-\infty\): \(|a_m|\le e^{-4m\sigma}\varepsilon(\sqrt2/r)^8e^{8\sigma}\le\varepsilon(\sqrt2/r)^8\). For \(m\le-2\) take \(s=\sigma\to+\infty\). Hence \(a_m=0\) for \(|m|\ge2\), including the critical frequencies \(\pm8\). Evenness (Step 5) gives \(a_{-1}=a_1\); reality gives \(a_m\in\mathbb R\). So
\[
 g_r(z)=c_0(r)+2c_1(r)\cos4z,\qquad c_0,c_1\in\mathbb R,
\]
which is RO1 (6.1) L497–499. As RO1 L501 notes, a merely bounded \(u\) would not kill \(m=\pm2\).

**Step 8. The modes \(m=\pm1\) vanish (RO1 Theorem 6, L503–554, unchanged).** The inputs of that text are now all available:
- (6.2) L503–508: diagonal RP of \(\sigma_S\) on degree-\(\le1\) polynomials at a diagonal mirror of the \((x_4,x_1)\) plane (Step 1, from LG1). Use mollified points \(\beta_\varepsilon\otimes\varphi\), \(\beta_\varepsilon\) a radial planar bump. Reflected pairs are planar-disjoint, so the density formula of Step 5 and continuity of \(G^{\rm gl}\) give the point limit. Connected subtraction is automatic: \(\sigma_S(f)=0\).
- The orbit bound \(B_v\) (L509) uses \(|G^{\rm gl}(y)|\le\Gamma(|y|/\sqrt2)\) (Step 5).
- \(D(t,x)=G^{\rm gl}(R_{\pi/4}(t,x))=g_r(\vartheta+\pi/4)\) for \((t,x)=R_\vartheta(r,0)\) (Step 7).
- The boost formula \(\int e^{-tE+ixq}d\mu_s=g_r(\vartheta+is)\) (L532–535) is \(H_0(\vartheta+is)\) of Step 7, for \(t>0\).
- Fourier–Laplace uniqueness (L523) and the group law of \(L_s\) (L527–530) are background.
RO1's text then gives \((C-1)\nu+\mu_1+\mu_{-1}=(C+1)\mu\), \(0\le\nu\le\frac{C+1}{C-1}\mu\), and \(c_0\pm2c_1\cosh4s\ge0\) for all \(s\) (L541–548). So \(c_1=0\). Equal-label kernels are radial. Symmetry, a half turn and polarization (L550–553) make \(G^{\rm gl}_{\varphi,\psi}\) radial for all real compact \(C^1\) \(\varphi,\psi\).

**Step 9. Planar rotations on all separated pairs (RO1 Lemma 8 at \(n=2\), shortened).** Fix \(u\in\mathbb R\) and put \(D_u(f,h)=S_2(f,h)-S_2(R_uf,R_uh)\), with \(R_u\) a rotation of the \((x_4,x_1)\) plane.
- *Case 1: disjoint planar projections.* Approximate \(f,h\) in \(\|\cdot\|_\sharp\) by finite sums of plates \(\alpha\otimes\varphi\) whose planar boxes stay disjoint (Fourier construction of RO1 L611, after mollification). \(R_u(\alpha\otimes\varphi)=(\alpha\circ R_u^{-1})\otimes\varphi\) is again a plate, still planar-disjoint. The density formula and radiality give \(D_u=0\) on the plates. Continuity (6) (input A) gives \(D_u(f,h)=0\).
- *Case 2: supports separated by a transverse cut* \(x_j=c\), \(j\in\{2,3\}\). Let \(F(s)=S_2(f,\tau_{se_4}h)-S_2(R_uf,\tau_{sR_ue_4}R_uh)=D_u(f,\tau_{se_4}h)\). The vectors \(e_4,R_ue_4\) are tangential to the cut, and \(R_u\) keeps the cut. In the \(x_j\)-picture (Step 2 with \(u=e_j\)) and its cube cone (Step 3 with \(W_4\)), RO1 (8.1)–(8.2) L595–602 make both terms holomorphic in \(s\) on \(|\Im s|<d/\sqrt2\), \(d\) the cut gap. For real \(|s|\) above the planar diameters, \(f\) and \(\tau_{se_4}h\) have disjoint planar projections, so \(F(s)=0\) by Case 1. The strip is connected, so \(F\equiv0\) and \(D_u(f,h)=F(0)=0\).
- *General pairs.* Let \(\delta=\operatorname{dist}(\operatorname{supp}f,\operatorname{supp}h)>0\). Split \(f,h\) by partitions of unity into pieces of diameter \(<\delta/8\). For two pieces, either their planar projections are disjoint (Case 1), or their centres have planar distance \(<\delta/4\). Then their transverse distance exceeds \(\delta/\sqrt2\), so one transverse coordinate differs by more than \(\delta/2\), and a cut \(x_j=c\) separates the pieces (Case 2). Bilinearity on separated supports (cl1.md L31) sums the pieces.
No time-tie induction is needed at \(n=2\), and no distribution theory: only product tests occur.

**Step 10. O(4) (RO1 Theorem 9 proof, L645).** \(W_4\)-conjugation moves Step 9 to all six coordinate planes. Coordinate-plane rotations generate SO(4) (L645). A coordinate reflection in \(W_4\) gives the other component. Each \(R\) maps separated compact \(C^1\) pairs to such pairs, so the invariances compose. This proves (O4-2). \(\square\)

## 5. Relation to CA, and limits of the claim

**CA Remark 10.1.** CA states the implication "(a)–(d) ⇒ two-point O(4)" for "any subsequential continuum limit on \(\mathbb{R}^4\) ... of the family of clause (ii-\(\mathbb{R}^4\))" (CA-III L79944–79946). Its hypotheses: (a) coordinate RP on one-field vectors and \(\mathbb R^4\rtimes W_4\); (b) clause (iii-b); (c) the upper member of clause (iv); (d) diagonal RP of \(S_2\) on one-field vectors at \(v_{01}^\perp\) (L79947–79957). CA refers the proof to a theorem "it is not reproduced here" (L79964–79966); ro1-vs-ca.md L108 found no numbered statement for it. Theorem O4-2 uses the same four ingredients, at degree \(\le1\): (a) and (d) in Steps 1–2, (b) qualitatively in Steps 1, 2, 4, (c) in Step 6. In addition it uses the cube cone, which Step 3 derives from (a) and (d). So §4 is a written proof of Remark 10.1's implication, for the class \(\mathfrak V\).

**Hypothesis (d) is supplied, not assumed.** CA: "For the periodic family of tori, hypothesis (d) would amount to independence of the limit from the shape of the box. It is not proved, and it is not assumed by Theorem 0" (CA-III L79975–79977). Here (d) comes from LG1 Theorem 10 for the DLR states \(\rho_j\) on \(\mathbb Z^4\) at fixed cutoff (Step 0), passed to the limit by CL1 Lemma 3 (Step 1). This agrees with CA's own sentence that diagonal RP "holds for the Wilson weight on \(\mathbb{Z}^4\)" (L79973). It is the order of limits (volume first), not box-shape independence.

**What this changes relative to CA clause (vi).** CA (vi) is "Not proved" (CA-III L111006); it is a deduction from (IR-fl), which "is a hypothesis of clause (vi) and is derived nowhere in this book" (L110834–110835). Theorem O4-2 uses no rotation current, no Ward identity and no decay at large distance. The only large-distance operation is the volume limit at fixed cutoff (Step 0). So, for \(n=2\), on \(\mathfrak V\), the O(4) statement moves from an unproved infrared hypothesis to CA's own ultraviolet clauses (iii-b), (iv), plus LG1.

**Limits of the claim.**
1. *Class.* \(\mathfrak V\) is the volume-first subclass. It is not every (ii-\(\mathbb R^4\)) limit: CL1 Theorem 9(1) shows volume-first limits are of finite-torus type (cl1.md L459, L470–485), and "neither identifies an arbitrary periodic DLR state as a torus limit point nor claims the converse" (L485). A general (ii-\(\mathbb R^4\)) limit is not covered.
2. *Connected function only.* Two-state moments \(\sigma_2=S_2+c^2\!\int\!f\!\int\!h\) need a one-point bound; CA (iii) does "Not assert: \(n=1\)" (CA-I L2658). The connected function needs none.
3. *Two points only.* For \(n\ge3\), RO1 needs operator plates (U2 at \(n\ge3\), Lemma 7), hence H-U. CA's reason is different but points the same way (CA-III L79979–79981).
4. *Separated tests only.* No coincident-point or diagonal-flat statement; that needs H-S (SR1, hence D1).
5. *Standing.* No better than inputs A and B at CA standing ("proved as an implication", with the outstanding items in the table), plus LG1 (frozen, one Claude gate, not a CA statement), plus the degree-\(\le1\) reading of CL1 and Lemma A in this note (one reading by Claude Opus 5.5; no second model).

**Where a reader should look hardest.**
1. Lemma A (Step 4), especially (a): \(\|\cdot\|_\sharp\)-continuity of the one-field class map from A, and the interchange of the class map with the convolution integral.
2. Step 7: the gluing of \(H_0\) by quarter turns and the bound (7.2) on whole horizontal lines.
3. Step 3: CL1 Lemma 8 restricted to degree \(\le1\).
4. LG1 Theorem 10 (input C), which carries diagonal RP for every periodic DLR state. CA neither states nor refutes it (ro1-vs-ca.md L118).

## 6. Result

**The shortcut works.** RO1 Theorem 6, rebuilt at \(n=2\) as in §4, gives Theorem O4-2: for every volume-first limit \(S_2\in\mathfrak V\) through torus-limit Wilson DLR states at CA's first-passage data, the connected plaquette-action-density two-point function is O(4)-invariant on real compact \(C^1\) tests with disjoint supports. H-U is removed: its \(n=2\) role was only to make the sandwiched point vectors exist (replaced by Lemma A from CA (iii-b), qualitatively) and to give a finite band (replaced by the spectral bound (7.2) with CA (iv)). Inputs: CA (iii-b) and CA (iv) at CA standing (proved as implications, with named outstanding items, CA-III L110895–110899, L110909–110955); LG1 (frozen); CL1 Lemmas 1–3, 5, 7, 8 at degree \(\le1\) with (iii-b) for I3; unchanged RO1 text (L265–274, L424–481, L496–554, L645). Not used: UV1/D1, SR1, IN1, PH1, (IR-fl). H-U remains needed for \(n\ge3\) and for the diagonal-flat extension.

This is research text by one model, one reading. It grants no status and goes nowhere outward.

## Change log (freeze, 2026-11-05)

Written by Claude (one reading). Refereed line by line by Codex ([o4-two-point-gate](../gates/o4-two-point-gate.md)): first failing step none; verdict "Theorem O4-2 is proved as the stated conditional implication on the whole class V". Applied by the lead (Claude):

1. The standing of (iii-b) is cited at CA-III 110895–110899 (was 110903–110907, which concern clause (ii)).
2. Lemma A: the parametrix at any \(r>0\) (or \(r=\min(1,b/16)\)); local densities glued on the inner balls \(B(y_0,b/16)\) where their representation is proved; complex first profiles use the conjugate pairing, proved first for real profiles.
3. The TU10 step: at fixed \(d\), volume first at fixed cutoff, then \(j\) with \(K_j-s(d)\ge k_W\), then \(d\to0\); no bound uniform in small \(d\) at one cutoff is used.
4. **Credit.** The holomorphic angular strip, the quarter-turn gluing, the whole-horizontal-line bound and the removal of all modes \(|m|\ge2\) (Step 7) are already in Sussman and Alpoge's outline, SA 30270–30318, by them with Claude and Codex. What is new here is how the one-field vectors and the spectral measure are obtained without H-U (Lemma A and the restricted CL1), and the use of LG1's diagonal reflection positivity of periodic DLR states, which their Remark 10.1 says is not proved for their torus limits.
5. Large real translations (CL1, Step 9) use boundedness and analytic uniqueness, not decay; no (IR-fl), stress-tensor estimate, clustering or mass gap enters.
6. Nonemptiness of the class has the same conditional standing as their first-passage construction (CA-I 2533–2540, 3636–3720); every limit in the class is the two-point member of a family covered by their (ii-R4).

Status: **frozen.** Checked by Claude (author) and Codex (referee). Candidate contribution to Sussman and Alpoge, with the credit in item 4; not sent.

