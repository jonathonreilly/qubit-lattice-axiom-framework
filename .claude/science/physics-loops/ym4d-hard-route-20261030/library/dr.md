# DR — the specified regional response

Provenance: Codex, 2026-11-05; pass 2 of Claude's 625-line dr-draft.md, read whole, at repository commit 7eaa2ca6a7324fe0203fe9218955f66dca49a27f. Research text, not an audit; grants no status. All arguments below are by hand. This text is not yet refereed.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text, supply the pinned outline (SA), complete accounts (CA), and YM3 at 31a47c543775. Their R9 prescription, multiplier method, walk tags, component argument and heat-kernel proof are used below. The background and localization methods originate with Tadeusz Bałaban; the flat port also credits Jonathan Dimock. Library imports retain their hypotheses and provenance.

## 1. Definitions and hypotheses

**Geometry and domains.** Fix one finite main step, determining sequence, boundary spaces, row ownership, real reference \(U\), and analytic branches. Use frozen ST1-r4 §1, including CV, (Tq0), the element cores and chain domain \(\mathcal D_{\rm in}\). The pair is \((\mathbf U,\mathbf J)\), with \(\mathbf U=e^{i\eta A'}U\) and independent \(\mathbf J\). Holomorphy initially means holomorphy in \((A',\mathbf J)\) at fixed \(U\). Equality at different splittings requires the intrinsic pair assignment below.

Write \(m_y=\xi_y\) for a pillar scale, \(m_b,m_p\) for the scales at a bond's or plaquette's base point, \(l(b)\) for the largest incident scale, and \(d_{\mathbf B}\) for the ambient layer distance, including paths outside \(\Omega_0\) (P82 (1); SA 9601–9605). Here \(d_{\mathbf B}=d_-\), the old (finer) layer metric; this is what the step \(d_-\ge d_+\) to NL1-L (7) uses. A based bond has \(m_b\le l(b)\le Lm_b\). Restrictions retain based coordinates with their specified stencils. Fine switches belong to NL1-L D1's level-\((i-1)\), side-\(M\) cubes. Wall-components use face adjacency; stencil sets use corner adjacency. Read boxes and margins must embed in their tori.

A source \(S=(S_c)\) is a dimensionless **reduced** raw-row datum in the product of all assigned row spaces; \(\|S\|_{\rm src}=\max_c|S_c|\). Its support is the assigned row locations. The physical source is \(b_V(B)\), not the raw logarithm \(B\) (ST1 (6)–(7)). Fine/site pairings include \(\eta^4\); raw-row pairings are counting pairings. Transposes are bilinear. For weights of rate \(\theta\), meaning \(w(x)/w(x')\le e^{\theta d_{\mathbf B}(x,x')}\), put
\[
 \|a\|_{X,w}=\sup_yw(y)\max(m_y|a|_y,m_y^2|\nabla_{\mathbf U}a|_y),\quad
 \|f\|_{F,w}=\sup_yw(y)m_y^3|f|_y,\quad
 \|b\|_{Y,w}=\sup_cw(c)|b_c|.
 \tag{1}
\]
All suprema include their read stencils. Centre and adjacent-scale comparisons cost fixed \(L\)-factors. The consumer seminorm is
\[
 n_b(h,j)=\max\{l|h(b)|,l^2|\nabla^Uh(b)|,l^3|j(b)|\}.       \tag{2}
\]

**Walk data W.** Import drlocp D, with h-walk-fix/h-walk-gate's fixed-region field-read repairs, O1D Definition D and LOC-3's endpoint hypotheses. Each of \(H,H_1,\mathfrak G,M_s^{\rm walk}\) has its own locally uniformly absolutely convergent expansion. Tag every closed fine cube meeting a coefficient's full connected enlarged hull once. A cell's enlargement has side \(8L^2M_1\xi_\kappa\); branches carry their own reads. For \(\mathfrak G\), compose undecoupled coefficients before tagging, as in pw-bridge (7.4). Subsequent products retain repeated switch powers. Require all these assignments to be jointly holomorphic in the intrinsic pair, real on real data and covariant under real site gauges.

Local maps and transpose stencils have reach \(r_g\le8L+1\). Retain
\[
 L\ge27,\quad R_1\ge8L^3,\quad M_1\ge\max(240,16Lr_g),\quad
 \rho_{\mathbf B}=3LM_1\ge80r_g.                            \tag{3}
\]
Write \(\operatorname{supp}s=\{\Delta:s_\Delta\ne0\}\), and let \(N_1(W)\) include \(W\) and its corner-neighbour cubes. A point is **deep in \(W\)** if every cube meeting its layer-metric radius-\(\rho_{\mathbf B}\) ball belongs to \(W\). The pair domain must lie inside the regular-pair envelope where all data and branches exist. **Outstanding — admission:** ST1 chain-domain notation alone does not prove that inclusion.

**Resummation ONE.** At \(s=\mathbf1\), require \(H=\ell,\ H_1=\ell_1,\ \mathfrak G=\mathfrak G_1,\ M^{\rm walk}=\Sigma,\ \widehat a=a_0I\), in ST1 (38)'s raw-row normalization. The scalar form \(\widehat a=a_0I\) is an explicit hypothesis: ST1 only says \(\widehat a\) is a positive diagonal mass. If \(\widehat a\) is not scalar, the corresponding term in (4) is \(-\widehat a\) and nothing else changes. The lift identity uses O1D Theorem B(a) and its saddle characterization. The other resummations remain imports, including the all-scale second-jet coefficient premise at dec-field L171. Put \(K_0=\widehat Q,\ \mathcal C_2=\mathcal C^{(2)}\), and \(N_0(t)=F'(t)-F'(0)-F''(0)t\), for \(F(t)=S_{\Omega_0}(e^{i\eta t}\mathbf U)\).

**Response specification.** Reserve \(H(s)\) for the linear lift and \(h\) for the nonlinear field. Let \(q(t)=K_0t+\mathcal C(t)\), \(K_t=q'(t)\), and define
\[
\begin{split}
 h&=\alpha-H\mathcal C(h),\quad d_s(\alpha)=\mathcal C(h),\quad
 d_{3,s}=d_s-\mathcal C_2,\quad Z_s=I-Hd_s',\\
 M_s&=M_s^{\rm walk}-a_0I,\quad p_s=H^{\mathsf T}\mathbf J,\\
 W_s(\alpha)&=-d_{3,s}'{}^{\mathsf T}p_s-K_0^{\mathsf T}M_sd_s
 -d_s'{}^{\mathsf T}M_sK_0\alpha+d_s'{}^{\mathsf T}M_sd_s
 +Z_s^{\mathsf T}N_0(h),\\
 \alpha&=H_1S-\mathfrak G W_s(\alpha).
\end{split}                                                     \tag{4}
\]
The diagonal \(-a_0I\) is unparameterized; primes on \(d_s\) differentiate \(\alpha\). The current is **ST1's** continuation:
\[
\begin{split}
 E_hv&=\int_0^1\operatorname{Ad}(e^{it\eta h})v\,dt,\quad R_h=(E_h^{\mathsf T})^{-1},\\
 \lambda_0&=H^{\mathsf T}\mathbf J,\quad
 \lambda=(I+H^{\mathsf T}\mathcal C'_h{}^{\mathsf T})^{-1}
                   H^{\mathsf T}(F'(h)-F'(0)+\mathbf J),\\
 j&=R_hK_h^{\mathsf T}\lambda-K_0^{\mathsf T}\lambda_0 .
\end{split}                                                     \tag{5}
\]
The response is \(\mathfrak h=(h,j)\). No physical operator identity is imposed at arbitrary switches. *Dictionary.* The pair response is \((H,K)\) in ST1 (16), \(h\) in NL1-L (7), and \(\mathfrak h=(h,j)\) here. This text's \(H\) is ST1's \(\ell\); its \(K_0,K_h\) are row derivatives, while ST1's \(K\) is the current. Equation numbers (7) and (16) refer to the named text.

**Outstanding 1 — PW (the draft's PW♮).** On every required complex pair domain and \(|s_\Delta|<e^{\bar\kappa}\), require, for all weights of rate \(\theta\le\theta_{\rm PW}\),
\[
 \|H\|_{Y_w\to X_w},\ \|H_1\|_{Y_w\to X_w},\
 \|\mathfrak G\|_{F_w\to X_w}\le B=b_0e^{16\bar\kappa},\quad b_0\ge1.
 \tag{PW}
\]
The constants precede \(\kappa\), uniformly in mesh, depth, volume and admissible geometry. Theorem 9 proves the first lift's \(s=1\) bound on a specified real-reference class. A separate conditional route already exists in pw-bridge §§6–7, from its [Energy], [Coefficients], [Walk geometry] and [Parameter geometry]: respectively the full complex cut-down inverse package with graph-norm repair, the Wilson/averaging/all-scale second-jet coefficients, the repaired cutoffs/counts, and the full-hull parameter count. Those premises are not derived from frozen P82 here. The remaining obligation is to supply PW, directly or through those premises, on every actual domain; the draft's scalar-slot objection does not refute that represented-source route.

**Outstanding 2 — NL.** The actual holomorphic maps (4) vanish at zero and must satisfy, on unweighted balls of radius \(r\le r_0/B\),
\[
 \|W_s(a)-W_s(v)\|_{F,w}\le C_WB^2r\|a-v\|_{X,w},\qquad
 \|\mathcal C(a)-\mathcal C(v)\|_{Y,w}\le C_Cr\|a-v\|_{X,w}.       \tag{NL}
\]
Their constants/domains are uniform. SA 10383–10389 and 10562–10576 assert this input. Contrary to the draft's “no rebuild exists”, nl-r9 §§3–6 proves it conditionally for exactly (4), from its [Rows], regular-pair geometry, local Wilson bounds and (4.2): bounds on \(H,H^{\mathsf T},M_s\). The last uses the counting multiplier block of the repaired energy expansion; PW alone does not bound it. When invoking that implication, enlarge early \(b_0\) to dominate the column constant \(t_0\) below and the normalized \(M_s\) bound. We retain this named import, including its common complex domains, rather than treating a gate's verdict as their supply. Its [RED] specification is fixed by (4).

**Column and local inputs.** Import O1D Theorem B(c), with its local inverse, cut-down, energy, count and summability premises. Write its column constant \(T=t_0e^{16\bar\kappa}\), \(t_0\ge1\). It bounds the sums of \(|H|m^{-3}\) and \(|D_{\mathbf U}H|m^{-2}\), multiplied by \(\eta^4w(c)/w(x)\). B(b)'s energy estimate and the same pillarwise Cauchy–Schwarz argument also give the full-\(\nabla_UH\) version. In particular \(\|H^{\mathsf T}\|_{F_w\to Y_w}\le T\).

Fix early \(C_R\ge1,r_R>0,\gamma_*\le1,D_R\). For \(\|h\|_{X,1}\le r_R\), let \(\widehat n_b(h)\) be the largest normalized value/first difference on the row carriers reading \(b\); define \(\widehat n_p\) similarly on a plaquette's complete read stencil. Require
\[
\begin{split}
 m_b^3|(K_h-K_0)^{\mathsf T}\nu(b)|&\le C_R\widehat n_b(h)\max_{c\ni b}|\nu_c|,\\
 |R_h-I|(b)&\le C_R\widehat n_b(h),\quad |R_h|\le2,\\
 m_b^3|K_h^{\mathsf T}\nu(b)|&\le C_R\max_{c\ni b}|\nu_c|.
\end{split}                                                     \tag{Rows}
\]
All reads have diameter at most \(D_R\). Also require, for \(0\le t\le1\),
\[
 |\langle v,F''(th)h\rangle|
 \le C_R\eta^4\left(\sum_p|D_{\mathbf U}v(p)|m_p^{-2}\widehat n_p(h)
                  +\sum_b|v(b)|m_b^{-3}\widehat n_b(h)\right),     \tag{Pair}
\]
or its full-gradient version with the corresponding column bound. These are **complex-domain** inputs. P82 (17), a3-derivative (9)–(12) and §7.1 explain their real-reference provenance. **Outstanding — uniform local input:** their cited gate does not prove (Rows)/(Pair) and absolute derivative majorants on every complex pair in use. Impose the early bound \(\|\mathbf J\|_{F,1}\le\gamma_*\); later current radii lie below it. Also impose \(\gamma_*+a_{\rm reg}\le c_\sharp\) (Theorem 9), so that Theorem 9 covers this whole current ball; both are early constants.

For locality require drlocp UNQ's absolute derivative/Neumann majorants for these maps on common pair-independent solution balls; call this ABS. For torus transport require a common assignment of coefficients, cutoffs, region traces and branches under lifts of their **full** read hulls; call this LIFT. Fixed-region field locality does not prove LIFT. S-loc requires source completion, including external pair, stored data and pins, to read only the first fine-cube neighbour layer.

**Order.** Fix \(\beta\in(0,1)\), running exponents, geometry and odd \(L\) with IN1's amended floors. Choose the flat/scalar/walk/row constants, rates and reference ceilings, P82's auxiliary \(M_P\), then \(M_1,R_1\), margins and the constants below. All precede \(\kappa\), independently of \(M,\bar\kappa\). Choose \(\kappa\) in IN1's amended window; then \(\bar\kappa\ge1\), parameter length and source radius; then \(M\); then test/radius amplitudes. Finally reduce the coupling ceiling to enforce admission and source budgets. Early \(\gamma_*\) is a ceiling, not the later current radius \(\gamma_0\).

## 2. Algebraic and locality clauses

**Lemma 1 (fine grid and stencils).** Suppose the main step's layer indices satisfy \(m_+(b)\le i\). Express all lengths in common physical units, let \(\xi_{\max}\) be the largest layer length, and require
\[
 r_1=16L^3M_1+4L,\quad
 \ell_{\mathcal P}\ge\max(8r_1+1,256\bar\kappa/\tau_L),\quad
 M\xi_{i-1}\ge\ell_{\mathcal P}\xi_{\max}/2.                      \tag{6}
\]
Require at least three grid cubes per periodic direction. Then O1D (P) holds for the fine grid. The sufficient floor \(M\ge L\ell_{\mathcal P}/2\) follows from \(\xi_{\max}\le L\xi_{i-1}\). Decorated-tree estimates additionally retain dec-field Theorem 4.2's floor \(1024\bar\kappa/\tau_L\). For pw-bridge's composed assignment require its stronger \(\ell_{\mathcal P}\ge2048\bar\kappa/\tau_L\) and \(\ell_{\mathcal P}>8R_*\), where \(R_*=C_LM_1\) includes the composite hull enlargement. Retain each construction's tree-count floors. For \(M>4\), (2)'s stencil lies in a connected set of at most 16 fine cubes containing its initial-site cube.

*Proof.* Layer-metric diameter less than \(\ell_{\mathcal P}/2\) implies physical coordinate diameter less than one grid side. On a circle of at least three grid sides, such a set has a lift of that diameter: points on opposite sides of an anchor cannot have combined separation at least one side, since both circular separations would then be at least that side. Each projection meets at most two closed grid intervals. Their product meets at most \(2^4\) cubes. This is (P), including boundary tags. Its path-length argument applies; tree traversals keep their separate stronger floor.

The values and differences of (2) lie in the radius-\(2\eta\) cube about the initial site. Its diameter \(4\eta<M\xi_{i-1}\). Its interval-product cube set has at most 16 members and is face-connected. The strict inequality repairs the draft's \(M=4\) endpoint. \(\square\)

**Lemma 2 (specification at one and the two currents).** Under ONE, (4)–(5) at \(s=1\) are ST1 (42)–(43). Under that lemma's OPS/SLICE/UNQ, criticality, regularity, branches and source hypotheses, they have ST1 (34)–(36)'s physical identification. Let \(j^F\) replace the anchor in (5) by \(F'(0)\), with the same field and operators. Then
\[
 j-j^F=[R_hK_h^{\mathsf T}(I+H^{\mathsf T}\mathcal C'_h{}^{\mathsf T})^{-1}
             -K_0^{\mathsf T}]H^{\mathsf T}(\mathbf J-F'(0)).     \tag{7}
\]
It vanishes on \(\mathbf J=F'(0)\), but not identically.

*Proof.* The inner equation gives \(d_1=\mathcal D,\ h=\mathcal L(\alpha)\) in ST1 (40). Differentiating its (41) yields
\[
 -(\mathcal D'-\mathcal C_2')^{\mathsf T}\ell^{\mathsf T}\mathbf J
 -K_0^{\mathsf T}(\Sigma-\widehat a)\mathcal D
 -\mathcal D'^{\mathsf T}(\Sigma-\widehat a)K_0\alpha
 +\mathcal D'^{\mathsf T}(\Sigma-\widehat a)\mathcal D
 +\mathcal L'^{\mathsf T}N_0(\mathcal L(\alpha)).
\]
These are exactly (4)'s five terms. O1D's saddle characterization identifies its per-length lift times \(\mathsf m^{-1}\) with \(\ell\): both solve the same prescribed raw-row constraint and annihilate its tangent kernel under the same quadratic form; the row mass drops out. The outer equation is therefore (42).

Trace invariance gives \(E_h^{\mathsf T}=\int_0^1e^{-it\eta\operatorname{ad}h}dt=f(-i\eta\operatorname{ad}h)\). Thus \(R_h=f_h^{-1}\) and (5) is (43). The physical consequences use precisely frozen ST1 Lemma 6's hypotheses. Subtraction proves (7).

For an admitted example, take a sufficiently large torus, \(\Omega_0\) the torus, \(\Omega_1=\varnothing\), \(U=I,A'=0\). Every row is bare: \(Q'=I,R=0,K_0=\eta I,\mathcal C=0\). The determining map fixes every bond, so \(U\) is regular critical. The positive row mass makes the defining inverses nonsingular. On one positive bond \(b\), set \(S_b=\varepsilon\sigma_2,\ \mathbf J_b=\delta_0\sigma_1\), zero elsewhere. Nonzero real \(\varepsilon,\delta_0\) can be chosen inside all open source/current bounds at this finite mesh. Curvature and nontrivial towers are absent. Then \(h_b=\eta^{-1}\varepsilon\sigma_2,\ F'(0)=0\), and (7) is \((f_h^{-1}-I)\mathbf J\).

For \(z=-i\operatorname{ad}(\varepsilon\sigma_2)\), \(z\sigma_1=-2\varepsilon\sigma_3,\ z\sigma_3=2\varepsilon\sigma_1\). On this plane \(z=2\varepsilon J_2,\ J_2^2=-I\); multiplication by \(e^{2\varepsilon J_2}-I\) verifies
\[
 f(z)^{-1}=\varepsilon\cot\varepsilon\,I-\varepsilon J_2,\qquad
 (j-j^F)_b=\delta_0[(\varepsilon\cot\varepsilon-1)\sigma_1+\varepsilon\sigma_3]\ne0.
 \tag{8}
\]
Choose \(0<|\varepsilon|<\pi/2\); no numerical evaluation is used. More generally, under ST1 Lemma 6's hypotheses, for \(\delta=\mathbf J-F'(0)\) supported on bonds not touching \(\Omega_1\), its (33) gives \(K_0^{\mathsf T}\ell^{\mathsf T}\delta=\delta,\ \mathcal C'_h{}^{\mathsf T}\ell^{\mathsf T}\delta=0\). Thus (7) is \((f_h^{-1}-I)\delta\). That boundary-current locus is not the physical-current locus unless \(\delta=0\). \(\square\)

**Lemma 3 (vanishing, row locality and DR-locP).** Assume W, (3), Lemma 1, ABS, and existence/uniqueness in common balls. The response vanishes at zero source, zero switches, on zero-switch cubes and on source-free wall-components. At fixed pair a component reads only its own switches and assigned source rows. For two admitted pairs on the same fixed geometry agreeing on \(W\), and equal source rows there, responses agree at every coordinate based in the wall-component \(W\). With S-loc, completed responses read the external pair only in \(N_1(W)\).

The induced map is holomorphic on the image of coordinate restriction; these restrictions compose. Under LIFT it commutes with common lifts of the full nonwrapping component and required geometry/margins. Under W it is real and real-gauge covariant.

*Proof.* A surviving connected hull lies in one face-component: every cube at a boundary point is tagged, and its cube star is face-connected. Both kernel endpoints are deep in that component. Their layer-metric \(\rho_{\mathbf B}\)-balls cannot exit the enlarged cell, since
\[
 3L^2M_1<(4L^2-5/2)M_1,\qquad
 L(\rho_{\mathbf B}+r_g)<(4L^2-3/4)M_1.
\]
Tree-multiplier reads, including two local stencils, fit because
\((33/8+21L/4)M_1\xi_\kappa<4L^2M_1\xi_\kappa\).
These are drlocp (16)–(17)'s first-exit margins.

The fields \(\alpha,h\) are supported on the deep sets. For \(A=\mathcal C'_h\),
\[
 d_s'{}^{\mathsf T}=A^{\mathsf T}(I+H^{\mathsf T}A^{\mathsf T})^{-1}
       =\sum_{n\ge0}A^{\mathsf T}(-H^{\mathsf T}A^{\mathsf T})^n.
\]
Every split factor returns to a deep endpoint. The five terms of (4) have at most two consecutive local maps, including \(-a_0I\); their reach is \(2r_g<\rho_{\mathbf B}\). The multiplier series has a leftmost \(H^{\mathsf T}\) in every term. It reads the anchor \(\mathbf J\) on deep bonds; final \(K_h^{\mathsf T}\) adds only \(r_g\). All reads remain in the component.

Splice one solution into another on that component's deep set. Each elementary norm stencil sees one original field or zero, with matching connection coefficients. The splice stays in the original common balls. Its inner equation agrees componentwise, then so do the five outer terms and current. Uniqueness proves equality, also after changing exterior switches or sources.

At zero source, \(\mathcal C(0)=\mathcal C'(0)=N_0(0)=0\), whence \(\alpha=h=0,\lambda=\lambda_0,j=0\). Splicing zero gives the source-free claim. At zero switches every nonempty hull is killed. Deep support plus the final margin proves the zero-cube claim.

Coordinate projection is open. Fix exterior coordinates from one lift locally to obtain a holomorphic section; equality of responses identifies sections on overlaps. Restrictions compose. Under LIFT the entire restricted systems coincide, hence their unique solutions coincide. Conjugation and real gauges take solutions to solutions in the same balls, proving the last claims. \(\square\)

**Outstanding — full restriction and transport.** This does not construct solvers on every declared \(\mathcal O_\sigma(Y;U)\), or identify separately assigned regional constructions. Those need full-domain admission, uniform local contraction and equality of coefficients. An output collar alone cannot compare tori: a surviving walk can explore the entire component. Require the full common lifted component and geometry.

## 3. The complex-source implication

**Theorem 4 (H-DR and ST1 (16)).** Assume W, ONE, PW, NL, the column input, (Rows)/(Pair), and §1's domain hypotheses. Enlarge early \(D_R\) to include all centre/read comparisons and put
\[
 \theta=\min(\theta_{\rm PW},\tau_L/8,\log2/D_R),\quad \mu=\theta/2,
\]
\[
 c_*\le\min\{r_0/4,(16C_W)^{-1},(16C_C)^{-1}\},\qquad
 \epsilon_D=\min\{c_*b_0^{-4},(32C_Rt_0b_0)^{-1},r_R/(4b_0)\},
\]
\[
 s_D=\epsilon_De^{-64\bar\kappa},\qquad E_{\bar\kappa}=e^{48\bar\kappa}.       \tag{9}
\]
On the full source ball \(\|S\|_{\rm src}<s_D\) and open switch polydisc, the response exists uniquely in common balls, is jointly holomorphic, real on real data, zero at zero source, and
\[
 n_b(\mathfrak h)\le C_DE_{\bar\kappa}\|S\|_{\rm src}
                   e^{-\mu d_{\mathbf B}(b,\operatorname{supp}S)},\qquad
 C_D=C_{\rm conv}C_R^2b_0(1+t_0)^2(1+\gamma_*).                  \tag{10}
\]
The fixed \(C_{\rm conv}\) covers the finite incidence, centre, norm, numerical and unit factors below. With ABS/LIFT/S-loc, Lemma 3 supplies their respective clauses for this same response; shrink \(\epsilon_D\) by early factors if ABS's stated majorants require it. Lemma 1 supplies TD's stencil clause. The source domain is the full product ball, invariant under row masks and independent row scalings remaining in the ball.

If \(\|S\|_{\rm src}\le C_A\delta_{\rm src}<s_D\), (10) gives ST1 (16). Since \(d_-\ge d_+\), it also gives NL1-L (7) in the input metric; converting old to input scales costs at most \(L^3\), included in \(C_{\rm conv}\).

*Proof.* Put \(b=\|S\|_{\rm src},R=2Bb\). PW and NL contract the outer equation on \(\|\alpha\|_X\le R\), and the inner equation on \(\|h\|_X\le2R\). The constants are at most \(2C_WB^4b\le1/8\) and \(4C_CB^2b\le1/4\), and \(2R\le r_0/B\). Values at zero give ball preservation. Picard iteration from zero converges uniformly on smaller parameter domains. Passing its Cauchy integrals to the limit proves joint holomorphy. For comparisons between sources use the balls defined with the common bound \(s_D\).

For nonzero source take \(w(x)=e^{\theta d_{\mathbf B}(x,\operatorname{supp}S)}\). Then \(\|S\|_{Y,w}=b\). Weighted norms are finite at fixed finite volume; absorption in the same equations gives
\[
 \|\alpha\|_{X,w}\le(8/7)Bb,\qquad
 \|h\|_{X,w}\le(4/3)(8/7)Bb<2Bb.                              \tag{11}
\]
The zero-source case needs no distance to an empty set.

Local weight comparison costs at most two. Hence
\(\|\mathcal C'_h{}^{\mathsf T}\nu\|_{F,w}\le2C_R\|h\|_{X,1}\|\nu\|_{Y,w}\).
Even using \(4Bb\) gives
\(\|H^{\mathsf T}\mathcal C'_h{}^{\mathsf T}\|\le8C_RTBb\le1/4\).
The inverse norm is at most two and \(\|\lambda_0\|_{Y,1}\le T\gamma_*\).
Subtracting its equation yields
\[
 \lambda-\lambda_0=(I+H^{\mathsf T}\mathcal C'_h{}^{\mathsf T})^{-1}
 \{H^{\mathsf T}(F'(h)-F'(0))-H^{\mathsf T}\mathcal C'_h{}^{\mathsf T}\lambda_0\}.
\]
Integration of (Pair) along \(th\), and both column sums, bound the first brace term by \(4C_RT\|h\|_{X,w}\) (O1D Theorem B(c) bounds each of its two column sums by \(C_H\) separately); Rows bound the second by \(4C_RT^2\gamma_*\|h\|_{X,w}\). Thus
\[
 \|\lambda-\lambda_0\|_{Y,w}\le8C_RT(1+T\gamma_*)\|h\|_{X,w}.     \tag{12}
\]
Expand \(j=(R_hK_h^{\mathsf T}-K_0^{\mathsf T})\lambda_0+
R_hK_h^{\mathsf T}(\lambda-\lambda_0)\). Rows and (11)–(12) give
\(\|j\|_{F,w}\le C C_R^2BT(1+T\gamma_*)b\).
The field members are \(O(Bb)\). Replacing \(\nabla_{\mathbf U}\) by \(\nabla^U\) uses the admitted first-order \(A'\) bound. Finally
\(B(1+T)^2(1+\gamma_*)\le b_0(1+t_0)^2(1+\gamma_*)e^{48\bar\kappa}\).
This proves (10). Reality uses W and uniqueness; the other conclusions follow from Lemmas 1–3 and the ball definition. \(\square\)

Descent's Y3 relative Gaussian form does not occur in (4)–(5), so changing that Gaussian split leaves this response unchanged **at fixed pair and source**. Frozen descent Theorem B/Lemma 7 do not supply response inputs or admission of a completed source.


## 4. The real-reference \(s=1\) argument

**Additional definitions and premises.** In this section \(U\) is real, \(D\) is the covariant site gradient, \(K=K_0\) is the raw-row derivative, and \(q\) denotes P82's chosen covariant curl (not §1's nonlinear constraint map). Thus
\(S_q^\circ(a,\ell)=((q^{\mathsf T}q+DRD^{\mathsf T})a-K^{\mathsf T}\ell,Ka)\).
Set
\[
 A_{\rm sc}=\Delta_U+Q'^{\mathsf T}m^{-2}Q',\quad
 S_{\rm sc}=A_{\rm sc}^{-1},\quad
 P_{\rm sc}=S_{\rm sc}Q'^{\mathsf T}(Q'S_{\rm sc}^2Q'^{\mathsf T})^{-1}Q'S_{\rm sc},
 \quad R=I-P_{\rm sc}.
 \tag{13}
\]
These are P82 (5). Its \(S_q^\circ\), \(\mathbb M_q\), scalar subsystem \(\mathbb S\), and physical energy/dual norms are P82 (8)–(9), (20). We import exactly Theorem P's I1–I5, I8, matched boundary spaces, separation, divisibility, torus room and small real-gauge hypotheses. Theorem P82's application to actual critical references additionally retains I6–I7/F0. Frozen CP12 Lemma 5 supplies the heat-kernel estimates used in Lemma 6 below.

For the differentiated scalar argument require **Reg\(^{1,\beta}\)**: on every complete local cube used in P82 Lemmas 1 and 6, with the additional nested stencils used below, there is a real gauge \(U=e^{i\eta A_0}\) with
\[
 m|A_0|+m^2|\nabla A_0|+m^{2+\beta}[\nabla A_0]_\beta\le a_{\rm reg} .
 \tag{14}
\]
Scales throughout each cube are comparable within fixed \(L\)-factors. The constants and the small ceiling on \(a_{\rm reg}\) are early. This is stronger than P82's Reg. CP12 Theorem 7 (FH) can supply it **when its D5 curvature, actual-current, preliminary gauge and enlarged-cube hypotheses hold on these same cells, including seams**. It is not an automatic consequence of P82's theorem label.

We also sharpen the auxiliary Hölder norms. Take the family of local interior cubes about every base point used by P82's Lemma 6, with fixed-ratio enlarged reads; use scales comparable to \(m_y\), and include cubes crossing pillar interfaces. Use the bounded-mesh estimate when \(m_y/\eta\le C_L\). Define \(X^\beta_w\) by (1) plus the suprema \(w(y)m_y^{2+\beta}[\nabla_Ua]_\beta\) on this family. Define
\[
 \|g\|_{G^\beta,w}=\sup_yw(y)(m_y^2|g|+m_y^{2+\beta}[g]_\beta),\qquad
 \|\varphi\|_{\Phi^\beta,w}=\sup_yw(y)(m_y^2|\varphi|+m_y^{2+\beta}[\varphi]_\beta).
 \tag{15}
\]
Here \(g\) is a 2-form and \(\varphi\) a site field. Comparisons use the fixed coordinate-path transports; in (14)'s gauge the ordinary and transported norms, with their value terms, are equivalent. All suprema include the same enlarged neighbourhoods. This strengthened \(X^\beta\) dominates the draft's pillar-only norm; the converse is not asserted. Proving an inverse bound into this stronger space suffices for PW's weaker \(X\) target.

**Lemma 5 (the rough term and its gauge inverse).** Use ST1 (37)'s current correction, with \(\lambda_a=S_{\rm sc}RD^{\mathsf T}a\), and SLICE \(KD\chi=0\) for \(\chi\in\ker Q'\). Then
\[
 \Delta'_\pi[\mathbf J]a=E_0a+DRS_{\rm sc}Y_a+D\varphi_a,\quad
 \varphi_a=RS_{\rm sc}D^{\mathsf T}Z_a,\quad
 Z_a(b)=-\tfrac i2[\mathbf J(b),\lambda_a(b_-)] .                \tag{16}
\]
Pointwise,
\[
 |E_0a|\le C|\mathbf J|\max_{\pm}|\lambda_a|,\qquad
 |Y_a(x)|\le C\sum_{b\ni x}|\mathbf J(b)|(|a(b)|+|D\lambda_a(b)|).
\]
Explicitly, let \(r_-\lambda(b)=\lambda(b_-)\), \(r_+\lambda(b)=\operatorname{Ad}U(b)\lambda(b_+)\), with transposes in the fine/site pairings. The other terms in (16) are
\[
 E_0a=\tfrac i2[\mathbf J,r_-\lambda_a+r_+\lambda_a],\qquad
 Y_a=\tfrac i2\{r_-^{\mathsf T}[a-D\lambda_a,\mathbf J]
                         +r_+^{\mathsf T}[a,\mathbf J]\}.
\]
In particular \(\varphi_a\in\operatorname{ran}R\). For any \(\varphi\in\operatorname{ran}R\), put \(\chi=S_{\rm sc}\varphi\). Then
\[
 \chi\in\ker Q',\quad \Delta_U\chi=\varphi,\quad
 S_q^\circ(D\chi,0)=(D\varphi+q^{\mathsf T}\mathcal C_U\chi,0),
 \quad \mathcal C_U\chi=qD\chi .                               \tag{17}
\]
At a real critical reference and its physical current \(J\), replacing \(q^{\mathsf T}q\) by \(\Delta-\Delta'_\pi[J]\) makes the curvature term in (17) vanish exactly.

*Proof.* In ST1 (37), terms containing the test field \(v\) directly give \(E_0a\). Those containing its endpoint values \(r_\pm\lambda_v\) give \(\langle\lambda_v,Y_a\rangle\). The term containing \(D\lambda_v\) is
\(\langle D\lambda_v,-i[\mathbf J,\lambda_a]/2\rangle\), by trace cyclicity. Transposition gives respectively \(DRG'Y_a\) and \(DRG'D^{\mathsf T}Z_a\). The mass-independent inverse on \(\operatorname{ran}R=\Delta_U\ker Q'\) gives \(G'R=S_{\rm sc}R\); its transpose gives \(RG'=RS_{\rm sc}\). This proves (16) without differentiating \(\mathbf J\).

P82 Lemma 2 gives the first two identities of (17). Missing-neighbour boundary terms vanish on \(\ker Q'\), since those sites are bare tops. Thus \(DRD^{\mathsf T}D\chi=D\varphi\); SLICE gives \(KD\chi=0\). The remaining term is \(q^{\mathsf T}qD\chi\).

For the start-point curl,
\[
 (d_UD\chi)_{\mu\nu}(x)=\eta^{-2}
 [\operatorname{Ad}(U_\mu(x)U_\nu(x+\eta e_\mu))
 -\operatorname{Ad}(U_\nu(x)U_\mu(x+\eta e_\nu))]
 \chi(x+\eta e_\mu+\eta e_\nu).
 \tag{18}
\]
The terminal site matters. For the prefix plaquette curl, telescoping gives
\(\eta^{-2}(\operatorname{Ad}U(\partial p)-I)\chi(x_p)\).
Both are zero-order curvature times a transported site value. Expanding the two length-two products in (18) cancels their linear undifferenced potentials; the remainder is a first difference of \(A_0\) plus bounded quadratic products. The integral derivative of the exponential and the Hölder product inequality therefore give scaled \(C^\beta\) coefficient bound \(Ca_{\rm reg}\) from (14), uniformly in \(\eta\). This corrects the draft's base-site formula for the start-point curl.

At a critical physical pair, ST1's finite gauge algebra gives
\(\Delta-\Delta'_\pi[J]=\Pi^{\mathsf T}\Delta\Pi\), \(\Pi=I-D S_{\rm sc}RD^{\mathsf T}\), and \(\Pi D\chi=0\). The last assertion follows. It is not an identity at arbitrary independent current. \(\square\)

**Lemma 6 (F: flat divergence-form Schauder).** On \(\eta\mathbb Z^4\), let \(0<\beta<1\), \(\mu\eta\le1\), and \(R_\mu=(-\Delta_\eta+\mu^2)^{-1}\), with \(\Delta_\eta\le0\). For bounded \(g\) of finite Hölder seminorm and any forward/backward differences,
\[
 \|D_aR_\mu D_bg\|_\infty\le C_\beta\mu^{-\beta}[g]_\beta,\qquad
 [D_aR_\mu D_bg]_\beta\le C_\beta[g]_\beta.                       \tag{19}
\]
If \(\Delta_\eta u=f+\sum D_j^\pm g_j\) on the full reads of \(Q_{2R}\), \(R\ge64\eta\), then on \(Q_{R/2}\)
\[
\begin{split}
 \|Du\|_\infty&\le C_\beta(R^{-1}M+RF+\Gamma_0+R^\beta\Gamma_\beta),\\
 [Du]_\beta&\le C_\beta(R^{-1-\beta}M+R^{1-\beta}F+
                                  R^{-\beta}\Gamma_0+\Gamma_\beta),
\end{split}                                                     \tag{20}
\]
where \(M=\|u\|_\infty,F=\|f\|_\infty,\Gamma_0=\max\|g_j\|_\infty,\Gamma_\beta=\max[g_j]_\beta\) on the outer cube. Constants are mesh independent.

*Proof.* CP12 Lemma 5 (11), the rebuilt SA BGH5 estimate, gives for \(r=2,3\)
\[
 \sum_x\eta^4|x|^\beta|D^rp_t^\eta(x)|
 \le C_{r,\beta}\begin{cases}t^{(\beta-r)/2},&t\ge\eta^2,\\
                            \eta^{\beta-r},&t\le\eta^2.\end{cases}
 \tag{21}
\]
Indeed split at radius \(\sqrt t\), or \(\eta\), into dyadic shells and use tail power \(N=1\). Their ratio is \(2^{\beta-1}<1\). The same argument applies at \(\beta=0\).

The kernel \(k_t=D_aD_bp_t\) has zero sum. Therefore
\(k_t*g(x)=\sum_z\eta^4k_t(z)[g(x-z)-g(x)]\).
Integrating (21) gives
\[
 \|D_aR_\mu D_bg\|_\infty
 \le C[g]_\beta\left(\eta^\beta+
       \int_{\eta^2}^\infty e^{-\mu^2t}t^{\beta/2-1}dt\right)
 \le C_\beta\mu^{-\beta}[g]_\beta .
\]
For \(h=x'-x\ne0\), split the time integral at \(|h|^2\ge\eta^2\). The early part is \(C[g]_\beta|h|^\beta\). In the late part shift the kernel, use its zero sum, and telescope along a coordinate path of length at most \(2|h|\). Equation (21), for \(r=3,\beta\) and \(r=3,0\), bounds the integrand by
\[
 C[g]_\beta|h|(t^{(\beta-3)/2}+|h|^\beta t^{-3/2}).
\]
Its integral from \(|h|^2\) to infinity is \(C_\beta[g]_\beta|h|^\beta\). This proves (19). At each fixed mesh the second resolvent derivative is absolutely summable; its absolute norm need not be uniform in mesh. Cancellation, not a uniform absolute second-derivative bound, was used.

For (20), choose \(\chi=1\) on \(Q_R\), supported in \(Q_{3R/2}\), with first/second differences bounded by \(C/R,C/R^2\), and set \(\mu=R^{-1}\). The exact product rule
\(\chi D_jg=D_j(\chi g)-(D_j\chi)\tau_jg\)
splits the equation for \(v=\chi u\) into bounded forces, divergence of \(\chi g\), and \(-[\Delta_\eta,\chi]u\).
The force norms are \(F+R^{-2}M+C\Gamma_0/R\). CP12 (9) bounds their resolvent gradients and Hölder seminorms. Zero extension satisfies
\([\chi g]_\beta\le C(\Gamma_\beta+R^{-\beta}\Gamma_0)\);
use (19) for this term.

For the commutator, transfer it to the kernel using
\([\Delta_\eta,\chi]^{\mathsf T}=-[\Delta_\eta,\chi]\).
CP12's off-diagonal estimate
\(\|1_{|x|\ge cR}D^rG_{1/R}\|_1\le C R^{2-r}\), \(r\le3\),
bounds output derivatives of orders one and two by \(CM/R,CM/R^2\).
The collar remains separated after all stencils. Telescoping the first derivative gives its Hölder bound \(C_\beta MR^{-1-\beta}\). On the evaluation cube \(v=u\). Adding these estimates proves (20). \(\square\)

**Lemma 7 (local covariant flux and scalar estimates).** On fixed-ratio nested cubes of side \(r\), with all stencils present, suppose
\[
 \Delta_Uu=f+\operatorname{div}_\eta g+Eu,\quad
 r|A_0|+r^2|\nabla A_0|\le a_{\rm reg},\quad
 |Eu|\le Ca_{\rm reg} r^{-2}\max_{\text{two stencils}}|u|.
\]
For small fixed \(a_{\rm reg}\), write \(N=r^{-2}\|u\|_{2,\rm outer}+r^2\|f\|_\infty+r\|g\|_\infty\). Then on the inner cube
\[
 |u|+r^\beta[u]_\beta\le C_\beta N,                              \tag{22}
\]
and, when \(g\in C^\beta\),
\[
 |u|+r|\nabla_Uu|+r^{1+\beta}[\nabla_Uu]_\beta
       \le C_\beta(N+r^{1+\beta}[g]_\beta).                     \tag{23}
\]
Signs of the scalar Laplacian do not affect these bounds. Complex links are allowed for these local statements. If additionally (14) holds and \(\Delta_Uu=f\) with \(f\in C^\beta\), then
\[
 |u|+r|Du|+r^2|\nabla_UDu|+r^{2+\beta}[\nabla_UDu]_\beta
 \le C_\beta(r^{-2}\|u\|_{2,\rm outer}+r^2|f|+r^{2+\beta}[f]_\beta).
 \tag{24}
\]

*Proof.* First recall the flat value estimate
\[
 |u|_{\rm inner}\le C(r^{-2}\|u\|_{2,\rm outer}+r^2|f|+r|g|).     \tag{25}
\]
Here is its hand argument, as in dec-field (3.5). The four-dimensional Green kernel has
\(|D^qG_\eta(x)|\le C_q(|x|+\eta)^{-2-q}\), \(q=0,1\).
For unit mesh this follows by splitting its Fourier multiplier at \(|p|=|x|^{-1}\) and integrating by parts \(q+3\) times off that ball; the radial integral of the resulting \(|p|^{-5}\) bound is \(O(|x|)\). Smooth cutoff derivatives have the same powers. Rescale to \(\eta\).
Convolve the sources, cut off to the outer cube, with this kernel, moving the flux difference onto it. This gives a particular solution on an intermediate cube, of supremum \(C(r^2|f|+r|g|)\) there by dyadic shell summation. Its difference from \(u\) is harmonic there. Testing the harmonic equation against a squared cutoff gives
\(\|Dh\|_{2,\rm inner}\le Cr^{-1}\|h\|_{2,\rm outer}\).
Repeat for commuting differences on finitely many nested cubes. Applying one-dimensional telescoping successively in four coordinates, then Cauchy–Schwarz, gives \(|h|_{\rm inner}\le Cr^{-2}\|h\|_{2,\rm outer}\). The particular solution's local \(L^2\) norm is at most \(Cr^2\) times its supremum. This proves (25); bounded \(r/\eta\) follows directly from point evaluation.

Paired transports give \(\Delta_U-\Delta_\eta=\mathcal B\nabla+\mathcal C_0\), up to the harmless overall sign, with
\(|\mathcal B|\le Ca_{\rm reg}/r,\ |\nabla\mathcal B|+|\mathcal C_0|\le Ca_{\rm reg}/r^2\).
Rewrite the drift as \(\operatorname{div}(\widetilde{\mathcal B}u)\) plus a value term, retaining the one-mesh shift of \(\mathcal B\) in the exact product rule. The new flux is bounded by \(|g|+Ca_{\rm reg}|u|/r\); the new force by \(|f|+Ca_{\rm reg}\max|u|/r^2\).
Apply (25) on cubes proportional to distance \(d\) from the outer boundary, multiply by \((d/r)^2\), and take the supremum \(\Phi\). This gives
\(\Phi\le C(r^{-2}\|u\|_2+r^2|f|+r|g|)+Ca_{\rm reg}\Phi\).
For \(d<C\eta\), use \(|u|\le\eta^{-2}\|u\|_2\). Absorb the last term. This bounds \(u\) on an intermediate cube.

The cutoff resolvent proof of Lemma 6, now for output value and its Hölder modulus, requires only bounded flux: \(R_{1/r}\operatorname{div}g\) is a first resolvent derivative, bounded by \(Cr|g|\) with Hölder seminorm \(C_\beta r^{1-\beta}|g|\), by CP12 (9). Bounded forces and the transferred commutator give respectively \(Cr^2|f|\) and \(C|u|\), with their \(r^{-\beta}\) factors. Applied to the rewritten equation and the preceding value bound, this proves (22), without a derivative of \(g\).

For (23), (22) and \([\mathcal B]_\beta\le Ca_{\rm reg} r^{-1-\beta}\) bound the rewritten flux seminorm by
\([g]_\beta+Ca_{\rm reg} r^{-1-\beta}N\). Apply (20); local transports change the bound by fixed factors. This avoids the draft's circular gradient absorption. Use further fixed nested margins; if their sizes are bounded multiples of \(\eta\), direct finite differences prove the estimates.

For (24), first (23) with zero flux bounds \(u,Du,[Du]_\beta\). In the fixed gauge the flat equation is
\(\Delta_\eta u=f-\mathcal B\nabla u-\mathcal C_0u=:f_0\).
Equation (14) gives
\(|\mathcal C_0|+r^\beta[\mathcal C_0]_\beta\le Ca_{\rm reg}/r^2\);
hence \(f_0\) has the required \(C^\beta\) bound. Differences commute with \(\Delta_\eta\), so
\(\Delta_\eta D_ju=D_jf_0\).
Apply (20) to \(D_ju\) with this single Hölder flux. Its value is already bounded, giving the second-difference and Hölder bounds. Returning to covariant differences differentiates the transport coefficients once; (14) bounds exactly those terms. \(\square\)

**Theorem 8 (P\(^{\rm div}\) and S1–S4, with explicit regularity).** Under P82's hypotheses, sufficiently small Reg, and the full-neighbourhood norms (15),
\[
 \|(a,\ell)\|_{X^\beta_w\oplus Y_w}
 \le C_{\rm div}(\|f\|_{F,w}+\|g\|_{G^\beta,w}+\|b\|_{Y,w}),\quad
 (a,\ell)=S_q^{\circ-1}(f+q^{\mathsf T}g,b).                    \tag{26}
\]
Under Reg\(^{1,\beta}\), define \(V_w(u)=\sup_yw(y)|u|_y\). The four scalar bounds are
\[
\begin{array}{ll}
 {\rm S1}:&\|DRS_{\rm sc}Y\|_{F,w}\le C\sup_yw(y)m_y^4|Y|_y,\\
 {\rm S2}:&V_w(\lambda_a)+\|D\lambda_a\|_{X^\beta,w}\le C\|a\|_{X^\beta,w},
              \quad\lambda_a=S_{\rm sc}RD^{\mathsf T}a,\\
 {\rm S3}:&\|RS_{\rm sc}D^{\mathsf T}Z\|_{\Phi^\beta,w}
                        \le C\sup_yw(y)m_y^3|Z|_y,\\
 {\rm S4}:&V_w(S_{\rm sc}\varphi)+\|DS_{\rm sc}\varphi\|_{X^\beta,w}
                       \le C\|\varphi\|_{\Phi^\beta,w},
                       \quad\varphi\in\operatorname{ran}R .
\end{array}                                                     \tag{27}
\]
S1 and S3 need only Reg. The constants and a positive weight-rate ceiling are fixed before \(\kappa\), independent of mesh, depth, volume, \(M,\bar\kappa\) and actual \(M_1,R_1\) above the enlarged floors.

*Proof.* We rerun P82 Lemmas 4, 6 and 7; no new inverse existence theorem is assumed. Its scalar equations, with sources \((g_1,g_2,0)\), give the exact blocks
\[
 h=P_{\rm sc}g_1+RS_{\rm sc}g_2,\qquad
 \psi=S_{\rm sc}R g_1-S_{\rm sc}RS_{\rm sc}g_2,\qquad Q'\psi=0.
 \tag{28}
\]
The equations also give
\[
 \Delta_Uh=g_2+Q'^{\mathsf T}\mu-Q'^{\mathsf T}m^{-2}Q'h,\qquad
 \Delta_U\psi=g_1-h.                                           \tag{29}
\]
Their fine/top normalizations are P82's; no transpose is commuted through \(R\).

Use I2's smooth partition \(\sum_z\chi_z^2=1\), with support radius \(C_LM_Pm_z\), bounded overlap and two bounded differences. Split **the flux itself**, \(g=\sum_z\chi_z^2g\), and \(Z\) likewise; do not sharply cut a negative-order source. For a unit normalized piece at scale \(m_z\),
\[
 \|q^{\mathsf T}g_z\|_{\mathcal X^*}\le C\|g_z\|_2,\quad
 \|Y_z\|_{\mathcal X^*}\le\|m^2Y_z\|_2,\quad
 \|D^{\mathsf T}Z_z\|_{\mathcal X^*}\le C\|mZ_z\|_2,\quad
 \|(g_1)_z\|_{\mathcal X^*}\le\|(g_1)_z\|_2.                    \tag{30}
\]
The first inequality pairs \(g_z\) with \(qv\) in the field energy norm. The next two pair against the scalar \(\psi\) slot, whose norm contains \(m^{-2}\psi,m^{-1}D\psi\). The last pairs against the \(h\) slot. The amplitudes are respectively \(m_z^{-2},m_z^{-4},m_z^{-3},m_z^{-2}\). Volume \(O((M_Pm_z)^4)\) makes each right side \(O_L(M_P^2)\), an early fixed constant. Smooth cutoffs preserve scaled \(C^\beta\) norms by the product rule. The source supports have a fixed metric radius.

P82 Lemma 4 therefore gives local energy decay \(Ce^{-\delta_wd(y,z)}\) for each such piece. If \(m_y/\eta\le C_L\), the energy summands bound all needed point values and differences by \(\eta^{-2}\) evaluation and finitely many differences; dimensionless losses are bounded by \(C_L\). This includes the arbitrary outer boundary.

For larger \(m_y/\eta\), P82's interior cubes and (29) apply. The two top/pillar terms in its first equation are bounded by
\[
 C m_y^{-4}\big(\|m^2\mu\|_{\rm top,loc}+\|h\|_{2,\rm loc}\big).
 \tag{31}
\]
Thus \(g_2=Y_z\) gives \(|Dh|\le Cm_y^{-3}e^{-\delta_wd(y,z)}\) by (23). Since \(h=RS_{\rm sc}Y_z\), this is S1 for one piece.
For \(g_2=D^{\mathsf T}Z_z\), the local gauge expresses it as ordinary divergence of bounded shifted/transported flux plus a value term of size \(Ca_{\rm reg}\,m_y^{-1}|Z_z|\). Equation (22) gives
\(m_y^2|h|+m_y^{2+\beta}[h]_\beta\le Ce^{-\delta_wd(y,z)}\).
This is S3, without any Hölder assumption on \(Z\).

For \(g_2=0,\ g_1=(g_1)_z\), (31), (23) bound \(h=P_{\rm sc}(g_1)_z\) and its first differences locally. If \((g_1)_z\) has scaled \(C^\beta\) size one, the second equation of (29) has a \(C^\beta\) right side. Its \(\psi\) energy includes \(m^{-2}\psi\). Equation (24) yields
\[
 |\psi|+m_y|D\psi|+m_y^2|\nabla_UD\psi|
           +m_y^{2+\beta}[\nabla_UD\psi]_\beta
 \le Ce^{-\delta_wd(y,z)}.                                     \tag{32}
\]
Taking \(g_1=D^{\mathsf T}a\) is legitimate: backward divergence is a transported sum of the forward stencils of \(a\). The full-neighbourhood \(X^\beta\) norm bounds its scaled \(C^\beta\) norm, including across pillar interfaces. This proves S2. Taking \(g_1=\varphi\), then summing, gives \(S_{\rm sc}R\varphi=S_{\rm sc}\varphi\) when \(\varphi\in\operatorname{ran}R\), proving S4. The localized pieces need not individually lie in \(\operatorname{ran}R\); (28) projects each before inversion.

For (26), the source of P82's field system is
\((f+q^{\mathsf T}g+K^{\mathsf T}b,0,0,0,-b)\).
For a flux piece, row 3 of that system is unchanged, so (31)/(23) give its \(Dh\) bound. Its first row is P82 (30) with the extra \(q^{\mathsf T}g_z\). In a cell gauge this is divergence of shifted flux plus bounded value terms. All other terms are bounded as follows:
\[
 |K^{\mathsf T}Ka|\le C m_y^{-3}\|m^{-1}a\|_{2,\rm carrier},\qquad
 |K^{\mathsf T}\nu|\le C m_y^{-3}\|\nu\|_{\rm count,loc}.
\]
The curl/gauge sum differs from the component Laplacian by the curvature value/shift term of P82 L477–489, \(O(a_{\rm reg}/m_y^2)\); that comparison uses entry bounds, not a derivative of curvature. Equation (23) now gives the field value, gradient and Hölder members. The counting multiplier is bounded directly by its local energy norm. The proof works about every centre, hence on the full-neighbourhood norms. Longer comparisons use twice the gradient supremum. Forces and row data are P82 Lemma 6's original cases.

Finally multiply each piece's estimate by the output weight and compare with its source weight. The exponent becomes \(-(\delta_w-\theta)d(y,z)\). Choose \(\theta\le\delta_w/2\); I4 sums the remainder, with bounded anchor multiplicity from I2. No derivative of \(w\) is taken. This proves (26)–(27). Choose the local absorption ceiling before the actual geometry, reducing P82's allowed \(\alpha\) if necessary; \(M_P\) and all constants above were fixed first. \(\square\)

**Theorem 9 (corrected R1: the first lift at \(s=1\)).** Assume Theorem 8's real Reg\(^{1,\beta}\) class, SLICE, matched raw-row normalization, and the Wilson Hessian bound
\[
 \Delta=q^{\mathsf T}q+\Delta',\qquad
 \|\Delta'v\|_{F,w}\le C_H^{\rm rem}a_{\rm reg}\|v\|_{X,w}.     \tag{33}
\]
This is the finite curvature-remainder input of a3-derivative §7.1, with its gate's consistent-curl correction. That section bounds \(\|\Delta'v\|\) by its curvature parameter \(\kappa_{\rm A3}\) and also uses the reference-current bound, which \({\rm Reg}^{1,\beta}\) alone does not give; so (33) holds with \(a_{\rm reg}\) replaced by \(\max(a_{\rm reg},\kappa_{\rm A3})\) in the smallness condition. Theorem 9 assumes (33) explicitly. Let \(\|\mathbf J\|_{F,1}\le\gamma\), without any difference bound on \(\mathbf J\). For an early \(c_\sharp>0\), if \(a_{\rm reg}+\gamma\le c_\sharp\), then
\[
 S_{\mathbf J}=\begin{pmatrix}
 \Delta+DRD^{\mathsf T}-\Delta'_\pi[\mathbf J]&-K^{\mathsf T}\\K&0
 \end{pmatrix}
\]
is invertible and
\[
 \|S_{\mathbf J}^{-1}(f,b)\|_{X^\beta_w\oplus Y_w}
       \le2C_{\rm div}(\|f\|_{F,w}+\|b\|_{Y,w}).                \tag{34}
\]
Where ST1's defining massive and Gram inverses exist (OPS), its field block on \((0,b)\) is the raw-row lift \(\ell b\); ONE then identifies it with \(H(1)b\). Saddle invertibility alone is not substituted for existence of those defining inverses.

*Proof.* Write \(S_{\mathbf J}=S_q^\circ+\operatorname{diag}(\Delta'-\Delta'_\pi[\mathbf J],0)\).
Equation (33) and (26) control the first perturbation by \(Ca_{\rm reg}\).
For the second, S2 and (16) give
\[
 \|E_0v\|_{F,w}+\sup_yw(y)m_y^4|Y_v|_y+
                         \sup_yw(y)m_y^3|Z_v|_y
 \le C\gamma\|v\|_{X^\beta,w}.
\]
S1 and (26) handle the first two forces. S3 puts
\(\varphi_v=RS_{\rm sc}D^{\mathsf T}Z_v\) in \(\Phi^\beta_w\), and S4 bounds
\(\chi=S_{\rm sc}\varphi_v\) and \(D\chi\). By (17),
\[
 S_q^{\circ-1}(D\varphi_v,0)
   =(D\chi,0)-S_q^{\circ-1}(q^{\mathsf T}\mathcal C_U\chi,0).
\]
Equation (18), Reg\(^{1,\beta}\), and the product Hölder inequality give
\(\|\mathcal C_U\chi\|_{G^\beta,w}\le Ca_{\rm reg}\gamma\|v\|_{X^\beta,w}\).
Equation (26) bounds its inverse. Consequently the composed perturbation has norm at most \(C_\sharp(a_{\rm reg}+\gamma)\) on \(X^\beta_w\oplus Y_w\). Choose \(c_\sharp\le(2C_\sharp)^{-1}\). Its Neumann series has norm at most two, proving (34). Under OPS/ONE, the saddle characterization proves the identification with raw datum \(b\); no extra \(\mathsf m^{-1}\) is inserted after \(K=K_0\) has been fixed. \(\square\)

**Outstanding — the rest of PW at one.** Theorems 8–9 close the scalar/flux subproblem and the first lift under their stated real regularity imports. They do not prove the \(H_1,\mathfrak G\) bounds. Those operators contain the second-jet correction and, for \(\mathfrak G\), a separate gauge subtraction; its off-shell identification and all compositions require proof. Nor do these theorems cover arbitrary complex references. Complex local estimates in Lemma 7 do not supply a global complex scalar projection, its weighted inverse, or the required coefficient comparisons. These were outlines, not proved corollaries, in the draft. The remaining actual Reg\(^{1,\beta}\) cell/seam supply is also explicit in (14).

At nonconstant switches the assigned sums need not solve any saddle equation. In particular \(KH(s)=0\) near killed rows, rather than \(I\). Thus (17)'s inverse argument cannot be applied to a general walk sum. This identifies a missing proof, not an impossibility of PW.


## 5. The Boolean proposal and its remaining obligation

**Lemma 10 (Boolean interpolation).** For a finite cube set \(\mathcal P\), let \(F(Y)\), \(Y\subset\mathcal P\), take values in one fixed finite-dimensional operator space; regional operators must first be extended by specified input/output maps. Put
\[
 D_XF=\sum_{Y\subset X}(-1)^{|X\setminus Y|}F(Y),\qquad
 F^{\rm BI}(s)=\sum_{X\subset\mathcal P}s^XD_XF.                 \tag{35}
\]
Then \(F^{\rm BI}(\mathbf1_Y)=F(Y)\); the polynomial is affine in each switch. A fixed direct-sum decomposition \(F(Y)=F_1(Y\cap W)\oplus F_2(Y\setminus W)\) for **every** \(Y\) kills mixed coefficients. If, instead, \(F(\varnothing)=0\) and each \(F(Y)\) is supported on \(Y\) and additive over its face-components, then \(D_XF=0\) for disconnected \(X\), and \(F^{\rm BI}\) splits over components of \(\operatorname{supp}s\). For a smooth extension \(\widetilde F\) with the correct Boolean values,
\[
 D_XF=\int_{[0,1]^X}\partial_X\widetilde F(t_X,0_{X^c})\,dt_X .
\]

*Proof.* In \(\sum_{X\subset Y}D_XF\), the coefficient of \(F(Z)\) is
\(\sum_{Z\subset X\subset Y}(-1)^{|X\setminus Z|}=(1-1)^{|Y\setminus Z|}\).
This proves interpolation; the monomials are square-free. For a mixed \(X=X_1\sqcup X_2\), each fixed-block summand is independent of one nonempty group, whose alternating sum is zero. If \(X\) is disconnected, apply this cancellation to the fixed components of \(X\), since every \(Y\subset X\) splits over them. Surviving monomials at switch support \(W\) have \(X\subset W\); their connected support lies in one component. The integral formula is repeated one-variable fundamental calculus with the other variables fixed at zero. The case \(X=\varnothing\) is evaluation at zero. \(\square\)

This algebra does not validate the draft's proposed weighted-wall realization. Merely multiplying wall couplings by \(t_\Delta t_{\Delta'}\) leaves isolated cube operators present when every \(t=0\); it does not produce zero extension of the empty-region operator. Already on one cube there is no wall: the proposed matrix is constant in \(t\), whereas the required values are \(F(\varnothing)=0\) and \(F(\{\Delta\})\ne0\). Also, intersection with an arbitrary cube union can create a nonbare outer boundary. It is not automatically one of P82's admissible cut-down geometries.

**Lemma 11 (WW, a precise outstanding sufficient input).** For each required operator type, supply admissible regional systems with fixed-space readouts \(F(Y;P)\), \(F(\varnothing)=0\), component additivity, intrinsic local domains and the correct full-region value. Supply a smooth extension \(\widetilde F(t;P)\) attaining those Boolean values, holomorphic in \(P\). Let \(K_X\) be its integrated mixed derivative in Lemma 10. In physical kernel convention require, uniformly in the geometry,
\[
 \sup_x\sum_{X,y} e^{\bar\kappa|X|}\mu_y
       \frac{\sigma_y}{\sigma_x}e^{\theta d_{\mathbf B}(x,y)}
       \left(|K_X(x,y)|+m_x|\nabla_xK_X(x,y)|\right)
       \le C e^{16\bar\kappa}.                                \tag{36}
\]
For field output \(\sigma_x=m_x^{-1}\); row input has \(\mu_y=1,\sigma_y=1\), force input has \(\mu_y=\eta^4,\sigma_y=m_y^{-3}\). Include the declared read stencils and equivalent scale factors. Constants and \(\theta>0\) are early. Then this **alternative specified family** has PW's field bounds and the algebraic component properties.

*Conditional proof.* The integral formula identifies \(K_X=D_XF\). For \(|s_\Delta|\le e^{\bar\kappa}\), take absolute values in (35), multiply by output weight, and use \(w(x)/w(y)\le e^{\theta d(x,y)}\). Equation (36) gives the \(X_w\) bound for each input norm. Lemma 10 gives the Boolean values and splitting. Pair holomorphy and other data properties must hold on the supplied common domains. This does not identify the resulting interpolation with W's original walk assignment. \(\square\)

**Outstanding — proof of WW's premises.** No such family or mixed-derivative majorant has been constructed here. A uniform inverse norm for real wall weights alone does not imply (36). The draft's \(e^{-c\ell_{\mathcal P}|X|}\) claim fails already for one active bare cube, whose dimensionless lift has norm one. Anchor cubes must be exempted, as in SA's factor \(e^{16\bar\kappa}\). Nor can a fixed exponential per visited cube pay an unrestricted \(|X|!\) ordering count: successive factorial/exponential ratios eventually exceed one. A genuine linked expansion is needed.

The draft's suggested globally Hölder wall norm is also unavailable: coefficient jumps do not meet (14). No lattice counterexample to PW itself is inferred from a continuum transmission example. A wall argument needs its own norms, endpoint convention, mixed estimates and admissibility proof. Thus the draft did **not** reduce full PW to a single already well-defined inverse estimate.

## 6. Source checks, definitions and corrections

Upstream files were fetched once each, at 31a47c543775. SA is /tmp/sa_ym4.tex; CA-I is /tmp/sa_ca_I.tex; CA-II, CA-III and YM3-I are in /tmp/dr-work. No raw file was read whole. Source retrieval, hashes and text inventories are bookkeeping, not proof.

The SA index README, relevant chunk rows with neighbours, obligations, and CA 4.12–4.19 index guided bounded source reads. The following record distinguishes a source statement from a supplied proof.

| Source passage | Checked use |
|---|---|
| SA 5602–5609, 5880–5887 | Common lifts concern nonwrapping regions with necessary collars and compatible assignments; they do not construct that assignment. |
| SA 5762–5803 | R9 consists of specified maps; its independent current and response properties are substantive inputs. The splitting sentence is at 5795–5797, not the full range attributed by NL1-L L170. |
| SA 6017–6035; 9601–9605 | Running radii and the ambient layer metric have the stated conventions. |
| SA 10125–10201; 10354–10412; 10548–10583 | Independent current, scalar/current-corrected operators, reduced equations, norms and contraction mechanism are as used. The nonlinear estimate is asserted; no decoupled right-inverse identity is available. |
| SA 12385–12408, 12409–12722; 12753–12883 | The scalar heat-kernel and interior estimates are proved in detail. The nonlinear gauge/readout and seam inputs remain hypotheses. Lemma 6 extends the scalar argument to Hölder flux; it does not import an unstated uniform absolute second-derivative bound. |
| CA-I 49495–49547, indexed at ca-4.12-4.19/chunk-06 | Application admission and later drop-out spaces lie outside the displayed operator theorem's implication. They do not close the full regional-domain obligation. |
| YM3-I 49115–49182 | The component proof retains the unparameterized identity and interior margins, then uses uniqueness. This is the credited proof template, not automatic four-dimensional admission. |
| YM3-I 26804–26820, 28435–28452, 33180–33234, 33434–33480, 54449–54528 | The reduced action, multiplier continuation, resummation and bare-current change are the source mechanisms behind p81-crit-draft's specification. ST1's four-dimensional counting normalization is retained here. |
| CA-II, CA-III | The DR draft quotes no numbered passage from either. Neither supplies a mathematical premise in this manuscript; fetching them is not evidence for DR. |

The local proof reads used ST1-r4 §2 and Lemma 6 in full, NL1-L H-DR, descent's forms/PF and its frozen scope, P82's definitions/imports and Lemmas 1–7, frozen CP12 Lemma 5/Theorem 7, drlocp D/UNQ and Theorem 1's proof, O1D §§1–2, dec-field §§3–5, a3-derivative §§4/7 and its curl/domain gate qualifications, the field-read and graph-norm repairs in h-walk's gate, and the relevant NR9/PW-bridge/LOC-3/current specifications. A gate's verdict word has not replaced its argument.

Definitions supplied or made explicit in the distillation are:

- Geometry and function spaces: base scales \(m_b,m_p,\xi_{\max}\), complete-stencil restriction, assigned source rows and their product ball, weight-rate convention, \(X_w,F_w,Y_w,n_b\), switch support, deep points, \(N_1(W)\), and face versus corner connectivity.
- Specification: W/ONE, the raw-row conversion, \(q,\mathcal C_2,N_0,d_s,d_{3,s},Z_s,M_s,p_s,W_s\), and the distinct lift \(H\), field \(h\), anchor currents \(j,j^F\), \(E_h,R_h,\lambda,\lambda_0\). These spell out imported constructions, not new physical identifications.
- Locality/domain requirements: common solution balls, ABS, LIFT, S-loc, row-carrier maximum \(\widehat n_b\), read diameter \(D_R\), and the complex Rows/Pair bounds.
- Constant choices: \(B,T,\gamma_*,\theta,\mu,c_*,\epsilon_D,s_D,E_{\bar\kappa},C_D\), and the distinct geometric lengths \(r_1,R_*\).
- Scalar/flux proof: the renamed \(A_{\rm sc},S_{\rm sc},P_{\rm sc},R\); Reg\(^{1,\beta}\) and \(a_{\rm reg}\); full-neighbourhood \(X_w^\beta,G_w^\beta,\Phi_w^\beta,V_w\); \(r_\pm,E_0,Y_a,Z_a,\varphi_a,\chi,\mathcal C_U\); the flat resolvent and local force/flux quantities in (19)–(25).
- Boolean proposal: fixed-space regional readouts, \(D_XF,F^{\rm BI},\widetilde F,K_X\), and the typed measures/amplitudes \(\mu_y,\sigma_x,\sigma_y\) in WW.

The draft's proposed corrections to other texts have these dispositions:

1. **NL1-L L170:** its source-range correction is right, with the precise splitting sentence at SA 5795–5797. The mathematical hypothesis remains conditional. Pair locality is the additional Lemma 3 statement, not an unqualified deletion of “at fixed \(P\)”.
2. **ST1 L138:** the two phrases are not defined there. Image-domain restriction and full-carrier common-lift transport are the meanings supplied here, following SA. They do not prove full declared regional existence.
3. **ST1 (16) versus H-DR (7):** the draft is right. H-DR requires a jointly holomorphic, norm-linear estimate on a full complex source ball, including the current. ST1's estimate at the source in use is weaker. Theorem 4 proves only the stated implication from stronger inputs.
4. **Two currents:** the draft's algebra and Pauli sign are right; Lemma 2 makes admission explicit. It is the proposed identification in assembly-status item 4 that fails. drlocp L69 itself already warned that equality was unsupported; it did not assert equality. ST1 and its frozen consumers require (5). The locality arguments in D3-local §3, red §3(2) and loc-4 §6 must be read with this anchor off the physical locus; drlocp's repaired proof covers it.
5. **Fine grid:** the dimensional comparison in draft Lemma 2.3 is right with explicit matched units, top-scale and torus-room hypotheses. It supplies (P), not missing operator expansions or arbitrary cut-down admission. Decorated trees retain their stronger convergence floor.

Two further claims in the draft were stale: nl-r9 already supplies a conditional NL rebuild, and pw-bridge already treats the unfolded rough-current source with a represented-flux norm and a local \(L^p\) bootstrap. Their gate checks those implications, not their premises on every actual chain domain. Neither route is erased by the failure of a raw pointwise scalar-slot estimate. The P82 route in §4 is an additional real-reference argument, not the only available conditional route.

## Result

This manuscript proves the DR algebraic, vanishing, component, fixed-pair row-locality and DR-locP implications for the **specified ST1 current**, with image-domain restriction and common-lift transport under their explicit inputs. Theorem 4 proves H-DR's complex-source estimate, hence ST1 (16), with \(E_{\bar\kappa}=e^{48\bar\kappa}\) and \(s_D=\epsilon_De^{-64\bar\kappa}\). It remains conditional on W/ONE, PW, NL, the column and uniform complex local estimates, and admission; locality additionally retains ABS and transport retains LIFT. Completed sources retain S-loc.

The new hand argument proves the mesh-uniform flat/covariant flux estimates and reruns P82's supported-energy, pointwise and weighted assembly for P\(^{\rm div}\) and S1–S4. Theorem 9 then bounds the **first** current-corrected lift at \(s=1\), for real references satisfying the full Reg\(^{1,\beta}\) and matched-domain inputs, with an arbitrary small independent current. It imposes no Hölder bound on that current. Frozen P82's flat/local inputs and CP12's scalar estimates remain imports; actual cell/seam regularity supply remains conditional. This P82 argument leaves \(H_1,\mathfrak G\), complex-pair and switched PW **Outstanding**. The existing pw-bridge/nl-r9 implications offer the separate route named in §1; supplying their premises, uniform complex local inputs, full regional domains and inter-region/torus compatibility for this construction remains **Outstanding**.

Corrections made in this distillation, in addition to the five source/consumer dispositions above:

- Make the counterexample entirely bare and distinguish the boundary-current locus from the physical locus.
- Use \(M>4\), explicit torus room and the stronger decorated-tree/composite floors where needed.
- Keep \(C_R\), fixed incidence/unit factors and the early \(\gamma_*\) in the estimate; replace the draft's minimum of differently scaled thresholds by the explicit smaller radius (9). Separate norm convergence from the absolute majorants used for locality.
- Correct the terminal site in the start-point formula \(d_UD\chi\); state the SLICE premise and the exact scope of physical gauge absorption.
- Replace stale cp12-draft (9.3)/Theorem 9.9 references by frozen CP12 Lemma 5/Theorem 7, preserving their hypotheses. Retain cancellation in the flux proof; supply bounded-mesh cases, shifted product rules, nested margins and a noncircular covariant argument.
- Supply the scalar subsystem blocks and the divergence-source dual estimates; use smooth flux partitions, not sharp cuts of dual sources. Strengthen the auxiliary Hölder norms across interfaces and state Reg\(^{1,\beta}\) explicitly. Supply the weighted assembly rather than calling it a rerun without proof.
- Restrict R1's conclusion to the operator actually estimated. Remove the unsupported “same argument” promotion to \(H_1,\mathfrak G\) and complex references, and keep the raw-row normalization consistent.
- Repair the Boolean lemma's application using component additivity and fixed-space readouts. Replace the unconstructed wall-matrix shortcut, singleton decay and factorial payment claims by the explicit Outstanding WW premises.
- Correct the draft's claims that no NL rebuild or represented-source walk route exists; retain the actual conditional imports of nl-r9 and pw-bridge.

Only library/dr.md was changed in the checkout. Frozen notes, ledgers, audits and editable prompt files were not changed. **This text is not yet refereed.**

## Change log (freeze, 2026-11-05)

Refereed line by line by a fresh Claude session ([dr-gate](../gates/dr-gate.md)): first failing step none, 6 findings, all repairable. Applied by the lead (Claude):

1. \(d_{\mathbf B}=d_-\), the old layer metric, is stated at its definition.
2. A dictionary line for the pair-response names across ST1 (16), NL1-L (7) and this text.
3. (12): the constant is \(8C_RT(1+T\gamma_*)\), since O1D Theorem B(c) bounds each column sum separately. Only \(C_D\) changes, inside \(C_{\rm conv}\); the radius (9) and \(E_{\bar\kappa}\) do not.
4. (33): its provenance uses \(\max(a_{\rm reg},\kappa_{\rm A3})\) in the smallness condition. Theorem 9 assumes (33) and stands.
5. The order also imposes \(\gamma_*+a_{\rm reg}\le c_\sharp\), so Theorem 9 covers the whole current ball. No cycle.
6. ONE's scalar mass \(\widehat a=a_0I\) is marked as an explicit hypothesis.

Referee on the two currents: the bare example (8) is right and agrees with ST1 (35). drlocp L69 does not assert that the two currents agree; it says no reason is supplied for (8) to vanish. What fails is the two-current identification that assembly-status item 4 asked for. It is not needed: every frozen consumer reads ST1's current (43), and CP12 L60 sits on the physical locus, where the two agree.

Results resting on unchecked notes: Lemmas 1–2 (o1-decoupled), Lemma 3 (drlocp, o1-decoupled), Theorem 4 (o1-decoupled B(c), walk data W, and nl-r9 if NL is supplied that way), Theorem 9 ((33) from a3-derivative). Lemmas 5–8 and 10 rest only on frozen texts.

Status: **frozen.** All seven Outstanding marks stand as placed.

