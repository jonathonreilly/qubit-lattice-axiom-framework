# LAYER-THM, second round

Provenance: Codex; checkout
`6bca34c8907f3aa799e2319ab8a17d415c400448`. Research text, not an audit.
This note grants no status. No numerical argument enters a proof.

Credit: Balaban supplied the chart and walk method. The definitions below
come from the Sussman–Alpoge outline and accompanying account.
The contraction argument below ports their method, with explicit margins.

I, II, III and SA denote the four files in `/Users/jonreilly/ym4d-lead/sa`.
Their supplied revision is `31a47c543775`. That directory has no Git HEAD.
Their SHA-256 identities are:

| File | SHA-256 |
|---|---|
| SA | `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f` |
| I | `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93` |
| II | `6a1f74b05f74ba44a2186c11fb08e139178d86b15c1494a95c434212944b2b8f` |
| III | `7e36523b85fb4f85aefdd45ab175420459f24e34fe56a4e83e53a6829c7a352d` |

The prior file `library/prior/layer-r2.md` is absent. I read `layer-thm.md`
whole and `layer-find.md:658–674`. The workflow file named by AGENTS is
absent. LAYER-THM belongs to this lane family. CA-LAYER/(N1) remains an
input owned by stage-claude. I neither prove it nor broaden its meaning.

## 1. What the existing chart theorem supplies

I 14498–14503 says, “Assume the following two statements”. The statements
are the free-current operator lemma and the nonlinear-correction lemma.
I 14517–14521 says the constants are “uniform in” the domains, including
“arbitrarily large” domains. Thus the native block-chart theorem **already
has uniform radii, conditional on its operator and averaging hypotheses**.
Its remaining contraction proof is not an open radius-selection problem.

I 14551–14556 imposes
\[
 B_0c_9\le\bar\varepsilon_4\le a_3/4.
\]
I 14586–14595 obtains the Lipschitz factor
\[
 B'_0(C_\Theta a_\gamma+8C_4^J\bar\varepsilon_4)\le\tfrac12.
\]
I 14596–14652 proves convergence and analyticity from these bounds.
These are first-order field balls, in the norm \(N\).
They are not balls in the full component-Laplacian norm.

I 15311–15320 defines the switched outer equation by
\[
 z=G\Theta_JH_0b-GV'_\sigma(z+H_0b).
 \tag{1}
\]
I 15323–15334 gives the switched operator bounds and the smaller datum
ceiling. The source term has no \(z\)-dependence. Thus its size restricts
the datum radius; it does not restrict the contraction factor.

This walk statement has an explicit hypothesis too. I 15270–15273 says
the constrained covariance inverse has the stated bounds and expansion,
“printed without proof”. I 15349–15445 spends a spare exponential to pay
the switch monomial. It does not construct that primitive expansion.

Here is the majorant step in that port. Suppose a tagged term
has majorant
\(a_\omega e^{-2\delta\tau_\omega}\), with
\(\sum_\omega a_\omega\le B\). Suppose its monomial has modulus at most
\(e^{c\kappa}e^{\delta\tau_\omega}\). Then
\[
 \sum_\omega\|s^\omega O_\omega\|
 \le e^{c\kappa}\sum_\omega a_\omega e^{-\delta\tau_\omega}
 \le e^{c\kappa}B.                                      \tag{2}
\]
The same calculation bounds every tail by the corresponding tail of the
nonnegative summable series. It gives local uniform convergence on any
strictly smaller switch polydisc. Finite sums are holomorphic. Their
Cauchy integrals converge uniformly, so the sum is holomorphic.
Finite compositions multiply the bounds. This proves the majorant step;
the two stated majorants are premises, not conclusions of this calculation.

I 14145–14154 says, “No Landau gauge condition is imposed on” the field
ball. I 14156–14375 defines the seven-term nonlinearity on this entire
ball. Therefore adding a field forcing to (1) does not require extending
that functional from a Landau slice. This is the useful scope fact for (S5).

## 2. A quantitative port, including the field datum

This is an implication with its native chart hypotheses attached.
It does not assert those hypotheses for a new determining set.

Let \(E_K\) be the fine-field space in norm \(N\), and \(B_K\) the
block space in its scaled sup norm. Write \(S_KA=\ell A\), measured in
the dimensionless value norm, so \(\|S_KA\|\le N(A)\).
Take the actual tagged operators and actual nonlinear functions of (S5).
Assume the following numerical bounds hold throughout their indicated
analytic domains, with constants independent of \(K\):
\[
\begin{gathered}
 \|S_KH\|\le h,\qquad \|H_0\|_{B_K\to E_K}\le h_0,
 \qquad \|G\|_{(-3)\to E_K}\le g,\\
 \|\Theta_J\|_{E_K\to(-3)}\le\theta,\\
 C(0)=DC(0)=0,\quad \|D^2C(u)\|\le c\quad(\|u\|<s_C),\\
 V'(0)=0,\qquad |V'(A)|_{(-3)}\le vN(A)^2
                       \quad(N(A)<s_V).                 \tag{3}
\end{gathered}
\]
Here \(s_C,s_V>0\) are common analytic radii, not finite-kernel radii.
The definition of \(V'\) uses the small inner branch. All base operators
are analytic on the actual base domain. Increase \(c,h,h_0,g,v\) to at
least one. This only weakens the bounds.

I 13762–13790 states the first-order bound on \(H^J\), the finite-range
bound on \(\Theta_J\), and the bound on \(\widetilde G^J\).
I 13980–14096 supplies the inner-chart argument, with its explicitly
assumed averaging bounds. I 14267–14375 gives the quadratic gradient
bound, with its propagator and averaging inputs. These explain (3)'s
native provenance. They do not verify (3) by citation here.

Put
\[
 q=gv,\quad t=1+g\theta,\quad k=g\theta h_0,
 \quad a=1+h_0+t+k,
\]
and choose
\[
 0<r\le\min\{s_C/32,s_V/8,(64ch)^{-1},(64q)^{-1}\},
 \qquad r_z=r,\quad r_X=8cr^2,\quad
 \varepsilon=\frac{r}{8a}.                              \tag{4}
\]
Every right-hand side is positive and independent of \(K\).
The slack in (4) keeps each closed ball strictly inside an analytic ball.

**Inner map.** If \(N(A')\le2r\) and \(|X|\le r_X\), then
\[
 \|S_KA'-S_KHX\|\le2r+8chr^2\le17r/8<3r<s_C.
\]
Taylor's formula on the segment from zero gives
\[
 |C(u)|\le\tfrac c2\|u\|^2,\qquad \|DC(u)\|\le c\|u\|.
\]
Consequently
\[
 |C(S_KA'-S_KHX)|\le\tfrac92cr^2<r_X,
 \qquad \operatorname{Lip}_X\Phi_{K,A'}\le3chr\le3/64.
 \tag{5}
\]
The segment between two arguments stays in the same ball. This justifies
the derivative estimate for their difference.

For analytic continuation needed in the outer calculation, repeat the
same argument for \(N(A')\le4r\), with auxiliary radius \(32cr^2\).
The argument of \(C\) then has norm at most \(9r/2\).
Its image has norm at most \((81/8)cr^2<32cr^2\).
Its Lipschitz factor is at most \((9/2)chr<1/2\).
Both branches agree where the smaller branch exists, by uniqueness in
the larger ball. Thus the inner branch has room around \(N(A')\le2r\).

**Field forcing.** The definition \(T=I+G\Theta_J\) gives
\[
 N(Tj)\le tN(j)\le t\|j\|_1^\Delta.                    \tag{6}
\]
This proof uses multiplication of the specified operators. It uses no
inverse identity at nontrivial switches. In particular, no bound on a
current-to-field conversion is needed: the datum here is already a field.

For \(\|j\|_1^\Delta+|b|\le\varepsilon\), equations (3)–(4) give
\[
 N(H_0b)\le r/8,
 \quad N(-Tj+G\Theta_JH_0b)\le r/8.                     \tag{7}
\]

**Outer map.** Set \(F(A)=GV'(A)\). If \(N(z)\le r\), then
\(N(z+H_0b)\le9r/8<2r\). Hence
\[
 N(\Psi_{K,d}(z))\le r/8+4qr^2\le3r/16<r.              \tag{8}
\]
For \(N(A)\le2r\) and \(N(u)=1\), apply the Cauchy formula to
\(F(A+\zeta u)\) on \(|\zeta|=2r\). Its argument has norm at most
\(4r<s_V\), and its norm is at most \(16qr^2\). Therefore
\[
 N(DF(A)u)\le8qr\le1/8.                                \tag{9}
\]
For vector values, apply a norm-one linear functional and take the
supremum. Integrating (9) along the segment between the two arguments
proves \(\operatorname{Lip}_z\Psi_{K,d}\le1/8\).

Equations (5), (7), (8), (9) prove exactly (G) from (3), with room to spare.
They prove it for the general datum (S5), not only for \(j=0\).

For completeness, a contraction of either closed ball has its fixed point
there: start at zero and bound consecutive differences by a geometric
series. Completeness gives a limit; continuity gives the fixed equation.
Two fixed points differ by at most half their distance and hence coincide.
The iterates are holomorphic. On each smaller parameter neighbourhood,
the geometric tail is uniform. Cauchy integrals pass to the limit, proving
joint holomorphy. No numerical iteration is used in this argument.

**Scope of the port.** The native theorem does give uniform block radii.
Equations (4)–(9) extend that *conditional* conclusion to the field slot.
They do not prove the unqualified actual-kernel assertion in
`layer-thm.md`, (G). In particular, (3) requires a common analytic
domain and bounds on the actual primitives, at every determining set.
Declaring each finite matrix analytic does not supply those constants.

The primitive-construction part is already assigned elsewhere:
`open-registry.md` assigns S1 to `b109`, and B99-W/CM-RW to `b99-w`.
I stop that subtask at its ownership boundary. I do not open a new proof
of their primitive walks. No assertion below silently promotes (3) to a
proved property of the full proposed K109 domain.
The separate PRINT-AVERAGE row remains open and unowned. I have not
claimed that ownership of the primitive walks settles that averaging input.

There is a further forcing bound from the single admitted input.
`layer-thm.md`, (N1), bounds \(A'_1-A'_2\) in the full graph norm and
specifies the zero triple at zero datum. For the furnished (S5) maps to
which that input applies, take data \((-ta,0)\) and zero. The defining
equation gives \(A'(t)=tTa+O(t^2)\) at each finite kernel. Divide (N1)
by \(|t|\) and let \(t\to0\). It follows that
\[
       \|Ta\|_p^\Delta\le B_{\mathbb H}\|a\|_p^\Delta.  \tag{7a}
\]
The same argument at \(J=0\), with data \((0,tb)\), gives
\(\|H_0b\|_p^\Delta\le B_{\mathbb H}|b|_p\).
These are consequences of (N1), not a proof of it. They do not identify
a different general-field convention with (S5), or create its solutions.

## 3. An exact tangent test for the remaining estimate

I 112589–112605 says the comparison bounds “each of the five weighted
norms”, and lists the full graph norm of \(\mathbb H_1-\mathbb H_2\).
Thus replacing this norm by a first-order norm would change U16's premise.
The requested \(R_\Delta\) concerns the actual correction \(HX\).

Keep a fixed kernel and write \(S=\ell\),
\[
 u=S(A'-HX),\quad B_d=DC(u),\quad V_d=DV'(A'),
\]
\[
 E_d=(I+B_dSH)^{-1}B_dS,\qquad
 P_d=(I+GV_d)^{-1}T.                                    \tag{10}
\]
These formulas concern furnished solutions in the contraction balls.
The two inverses exist there. Indeed, their perturbations have norm at
most one half. The geometric series gives their inverses with norm at
most two; multiplication and telescoping verify both inverse identities.

The defining equations are
\[
 A'=-Tj+TH_0b-GV'(A'),\qquad X=C(S(A'-HX)).
\]
Differentiate them in a datum direction \(v=(\dot j,\dot b)\).
The operators stay fixed. The chain rule gives
\[
 DA'[v]=P_d(-\dot j+H_0\dot b),\qquad
 DX[v]=E_dP_d(-\dot j+H_0\dot b).                         \tag{11}
\]
This calculation neither differentiates the independent current nor
uses a switched inverse identity.

Consequently, on a convex datum ball, (B4) is equivalent to the bound
\[
 \left|\Delta_WH E_dP_d(-\dot j+H_0\dot b)\right|_{-3,p}
 \le C\|v\|_{\mathrm{dat},p}                             \tag{12}
\]
at every datum in that ball, with the same uniform constant.
Necessity follows by dividing (B4) by the size of a datum increment and
taking its limit. For sufficiency, join two data by their line segment,
insert (11), and integrate. The triangle inequality for the finite
weighted sup norm gives (B4). Closed-ball endpoints follow by continuity.
This proves the equivalence. It asks for no estimate on arbitrary block
inputs to \(H\).

The next sections test a necessary sublemma of (12) on the actual
quadratic image. The final contradiction assumes the common analytic
realization explicitly; it does not infer it from finite germs.

## 4. The exact image of the nonlinear constraint

I 13995–14002 writes the inner equation as
“\(X\mapsto C(\ell A'-\ell H^JX)\)”.
I 14143–14147 subtracts \(C^{(2)}(\ell\,\cdot)\) from \(D^J\).
These lines identify the quadratic term of the *actual* constraint.
Write \(C_2(u,v)=\tfrac12D^2C(0)[u,v]\); hence
\(C^{(2)}(u)=C_2(u,u)\).

Take the allowed field datum \(d(t)=(-ta,0)\). No current-to-field
conversion is involved. The equations and their first derivatives give
\[
 A'(0)=X(0)=0,\quad \frac{dA'}{dt}(0)=Ta,
 \quad \frac{dX}{dt}(0)=0.
\]
Differentiating the inner equation a second time gives
\[
 \frac{d^2X}{dt^2}(0)=D^2C(0)[STa,STa].
\]
The term involving the second derivative of its argument is multiplied
by \(DC(0)=0\). Thus, at each fixed finite kernel,
\[
 X(t)=t^2 C_2(STa,STa)+O(t^3),
 \qquad
 HX(t)=t^2 H C_2(STa,STa)+O(t^3).                        \tag{13}
\]
The remainder constants in this identity are not asserted uniform.
The coefficient identity itself is exact.

Suppose (B4) holds on \(\|d\|_{\mathrm{dat},1}<\varepsilon\).
For \(\|a\|_1^\Delta=1\), compare \(d(t)\) with zero and use
\(|t|=\varepsilon/2\). The bound is
\[
 |\Delta_WH X(t)|_{-3,1}\le C_\Delta|t|.
\]
The Cauchy formula for the coefficient of \(t^2\), applied componentwise,
then gives
\[
 |\Delta_WH C_2(STa,STa)|_{-3,1}\le2C_\Delta/\varepsilon.
 \tag{14}
\]
Homogeneity supplies the factor \((\|a\|_1^\Delta)^2\) for general \(a\).
If the norm is zero, \(a=0\) and the assertion is immediate.

This reduction retains the *produced* nature of \(X\).
Equation (13) gives an exact answer at its first nonzero order: feedback
through \(-SHX\) cannot cancel this coefficient. That feedback first
enters the quadratic map at degree three. Higher terms of \(C\), and
the nonlinear outer correction, also cannot alter the degree-two term.
Thus (14) concerns an actual quadratic image. It does not ask for an
estimate on arbitrary block data. The following necessary statement
will be contradicted by an exact finite Fourier calculation.

**\(Q_\Delta\), actual quadratic-image estimate.** Set all switches to one
and the background to \(W=1\). Use the actual admitted periodic
determining systems, scales and boundary conventions. Keep the independent
current \(|J|_{-3}<a_\gamma/2\). At each such kernel set
\[
 T_J=I+\widetilde G^J\Theta_J,
 \qquad
 \mathcal Q_J(a)=\Delta H^J C_2(\ell T_Ja,\ell T_Ja).
\]
Prove one constant \(C_Q\), independent of the mesh, volume, determining
system and independent current, such that
\[
             |\mathcal Q_J(a)|_{-3,1}
                  \le C_Q(\|a\|_1^\Delta)^2.           \tag{Q}
\]
This subdomain is part of the original target. The norm and the operators
are the original ones. In particular, (Q) is not a claim about a freely
chosen oscillating replacement kernel. Equations (13)–(14) prove that
(B4), with a common analytic datum ball, implies (Q).

## 5. Polarise the independent current

I 12968–12971 says, “no relation between \(J\) and \(U\) is required”.
I 13774 says the identity \(RD_U^*H^J=0\) “is neither asserted nor used”.
The current can therefore be varied at the fixed flat background in (Q).
This route examines its exact Taylor coefficients. It does not use the
lifting equation (B6) or the second response system (B10).

Put \(A_J=\Theta'_J\) and \(B=\widetilde{\mathfrak G}_0=P_0G_0\).
The symbol \(A_J\) in this section is an operator, not the chart field.
I 13723–13733 defines the insertion by
\[
 A_J=\mathfrak k_J\Lambda+\Lambda^T\mathfrak j_J
                       +\Lambda^T\mathfrak m_J\Lambda.
\]
I 13719–13738 defines \(G_\pi^J\), \(\mathsf q_J\), and \(H^J\) by their
inverse and Gram formulas. Those formulas imply
\[
                    H^J=H_0+BA_JH^J.                  \tag{15}
\]
Here is a direct algebraic proof. First \(QH^J=\ell^{-1}\), by multiplying
the Gram inverse in its definition. Next,
\((I-G_0A_J)H^J=G_0Q^*\mathsf q_J\ell^{-1}\).
Apply \(P_0\). The identities
\(P_0G_0Q^*=0\) and
\(P_0H^J=H^J-G_0Q^*\mathsf q_0QH^J=H^J-H_0\)
give (15). This uses finite inverse algebra at switches one.

Let \(J=sJ_1+tJ_2\), and write \(A_i=\Theta'_{J_i}\).
This dependence is linear, by its definition. Near zero, the Neumann
series for this finite matrix equation gives the exact coefficients
\[
 H_i=BA_iH_0,\qquad
 H_{12}=BA_1BA_2H_0+BA_2BA_1H_0.                        \tag{16}
\]
Here subscripts \(i\) and \(12\) mean derivatives at \(s=t=0\).
These identities do not assume any uniform convergence radius.

Keep the dependence of the reachable block input as well. Write
\(x(J)=C_2(\ell T_Ja,\ell T_Ja)\). Since \(\Theta_0=0\), \(T_0=I\), and
\[
\begin{split}
 x_0&=C_2(\ell a,\ell a),\\
 x_i&=2C_2(\ell a,\ell T_i a),\\
 x_{12}&=2C_2(\ell T_1a,\ell T_2a)
                   +2C_2(\ell a,\ell T_{12}a),\\
 \partial_s\partial_t\mathcal Q_J(a)\big|_0
   &=\Delta\{H_{12}x_0+H_1x_2+H_2x_1+H_0x_{12}\}.      \tag{17}
\end{split}
\]
Every term in the last line is necessary. Ignoring the variation of
\(x(J)\) would not test (Q).

I 13811–13823 polarises the gauge commutator and decomposes
\(\mathfrak m_J\) as \(m_3+D^*m_4\). Its divergence term can be checked
directly. On an oriented flat bond the defining pairing is
\[
 \frac1{2i}\langle[\lambda_1,D\lambda_2]
                         +[\lambda_2,D\lambda_1],J\rangle.
\]
Invariance of the trace pairing gives
\(\langle[\lambda_2,D\lambda_1],J\rangle
 =\langle D\lambda_1,[J,\lambda_2]\rangle\).
The definition of the bilinear transpose moves \(D\) to the other factor.
Consequently this term is
\[
       m_4(J,\lambda)=\frac1{2i}[J,\lambda_-].           \tag{18}
\]
The first commutator supplies \(m_3\), with \(D\lambda\), and no
derivative of \(J\). Endpoint placements remain as in the displayed
pairing. This rebuilds the decomposition used below.
Explicitly, at a flat base,
\[
 (m_3(J,\lambda))(x)
   =\frac1{2i}\sum_\mu[D_\mu\lambda(x),J_\mu(x)].
\]

Inserting (18) in (16) produces, among the terms of (17),
\[
 \Delta B\Lambda^T D^*m_4(J_1,\Lambda BA_2H_0x_0)
       +(1\leftrightarrow2).                           \tag{19}
\]
The other terms of (17) remain attached. The purpose of (19) is to test
the proposed cancellation, not to declare the displayed part the answer.

## 6. Counterexample on the actual flat periodic sector

The following calculation retains every term in (17). It proves an
incompatibility, with its quantifiers explicit:

**Theorem.** Suppose the proposed (S5)–(S6) charts have a common positive
datum radius and are jointly holomorphic on the admitted independent-current
domain, as requested in (G) and clause (a). Then (B4) cannot have a common
constant on that domain. This failure already occurs at \(W=1\), at
switches one, with weight one and fixed physical volume.

Thus this theorem rules out the conjunction of the requested uniform
analytic realization and (B4). It does not prove (G) separately. Its
counterexample concerns the proposed general-field convention (S5).
It does not refute an unstated alternative definition of the layer map.

### 6.1 The invariant periodic sector and its exact operators

SA 11261–11266 says the flat straightened per-length average is
\[
 (Q_k^0a)_\mu(y)=n^{-5}\sum_{v\in\mathcal B_n}
                         \sum_{j=0}^{n-1}a_\mu(y+\eta v+\eta j e_\mu),
 \qquad n=L^k,\quad\eta=n^{-1}.                         \tag{20}
\]
Here \(\mathcal B_n\) consists of the centered \(n^4\) fine sites.
SA 11445–11449 gives its composition by centered digits. We only need
the displayed finite averaging formula, and rebuild its consequences.

Fix an admitted physical torus with integer side \(P\), divisible by the
fixed coarse grid sizes and large enough for all geometric floors.
Take every \(\Omega_j\) to be that torus. Only the top
layer has rows; its scale is one. Empty complements satisfy the separation
conditions. Work with fine fields periodic under translation by one unit
in each coordinate. Coarse fields in this sector are constant.
Choose a top-level site as the coordinate origin.

For a field in this sector, the \(n\) longitudinal sites in (20) run
through a whole period. Summing over the remaining three coordinates,
and then the repeated longitudinal starting coordinate, shows
\[
                         Qa=\langle a\rangle.           \tag{21}
\]
Brackets here mean the normalized fine average over one period.
The site average \(Q'\) has the same property. Indeed, its flat one-step
formula is the arithmetic site average; iterating tiles the centered
block by its digits, with no multiplicity.

The transposes send constant coarse inputs to constant fine inputs.
For the field rows this can also be checked before restriction: each
fine bond occurs \(n\) times in the sum over all rows and longitudinal
positions in (20). The normalization \(n^{-5}\), with the physical fine
measure \(n^{-4}\), gives
\(\sum_c Qa(c)=\sum_b\eta^4a(b)\).
This proves the transpose assertion by its defining pairing. The site
calculation has one occurrence per fine site and is identical in purpose.

Write \(\Pi_0\) for the fine mean projection. Let
\(\Delta=\sum_\nu D_\nu^*D_\nu\), with
\(D_\nu f(x)=(f(x+\eta e_\nu)-f(x))/\eta\).
Let \(\Delta^{-1}\) mean the inverse on mean-zero fields, extended by zero
on constants. The inverse exists: on a nonconstant Fourier mode
\(\Delta\) has eigenvalue
\(4n^2\sum_\nu\sin^2(\pi m_\nu/n)>0\).
The geometric-series identity for roots of unity proves the finite
Fourier basis and this diagonalisation directly.

SA 10141–10155 defines \(G'\), \(R\), and the completed field inverse.
With the top mass \(a=\ell^{-2}=1\), substitution of (21) gives, on this
invariant sector,
\[
\begin{gathered}
 G'=(\Delta+\Pi_0)^{-1},\quad R=I-\Pi_0,\quad
 \Lambda=\Delta^{-1}D^*,\quad \Lambda^T=D\Delta^{-1},\\
 G_0=(\Delta+\Pi_0)^{-1},\quad
 H_0b=b,\quad B=P_0G_0=\Delta^{-1}.                     \tag{22}
\end{gathered}
\]
Here \(D\) is the site-to-one-form difference. To verify the field identity,
SA 11317–11328 states that the flat plaquette Hessian is the trace of
“the product of the two sums of insertions”. Here is that calculation.
In \(1-\tfrac12\operatorname{Tr}\prod_{r=1}^4e^{i\eta v_r}\),
the mixed second variation is
\(\tfrac12\operatorname{Tr}((\eta\sum v_r)(\eta\sum w_r))\).
Trace cyclicity cancels the insertion commutators. Each oriented sum
is \(\eta\) times the forward curl. Thus the physical \(\eta^4\)
pairing gives precisely \(D_{\rm curl}^*D_{\rm curl}\). Moreover
\(D_{\rm curl}^*D_{\rm curl}+DD^*=\Delta\) on one-forms.
In component \(\mu\), expand the curl square as
\(\sum_{\nu\ne\mu}D_\nu^*(D_\nu a_\mu-D_\mu a_\nu)\).
The mixed terms cancel those of \(D_\mu\sum_\nu D_\nu^*a_\nu\), since
flat shifts commute. The diagonal term supplies the missing \(\mu\)
summand. Also \(D^*a\) has mean zero. Thus \(DRD^*=DD^*\), which proves
the asserted formula for \(G_0\). The Gram formulas now give \(H_0\)
and \(B\) in (22).

All these assertions concern restrictions of the actual operators.
Translations by a whole coarse cell preserve the base, grids and rows.
They therefore commute with the displayed matrices and their inverses.
For a current of period one the same holds for its insertion matrices.
Consequently the actual analytic germs preserve this sector. No substitute
Green kernel has been inserted.

### 6.2 An actual, nonzero quadratic block datum

Use the Pauli matrices
\[
 \tau_1=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
 \tau_2=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\quad
 \tau_3=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]
Matrix multiplication gives \([\tau_i,\tau_j]=2i\epsilon_{ijk}\tau_k\)
and \(\|u\tau_1+v\tau_2\|=\sqrt{u^2+v^2}\) for real \(u,v\), in
operator norm. A different fixed Lie norm only changes fixed constants.
Put \(A_*=1+2\pi+4\pi^2\), and choose the fine field
\[
 a_1(x)=A_*^{-1}\{\cos(2\pi x_1)\tau_1+
                         \sin(2\pi x_1)\tau_2\},\qquad a_\nu=0\ (\nu\ne1).
 \tag{23}
\]
Its mean is zero. Its value, first difference and component Laplacian
are bounded respectively by \(A_*^{-1}\), \(2\pi A_*^{-1}\), and
\(4\pi^2A_*^{-1}\). These follow from
\(2n\sin(\pi/n)\le2\pi\). Hence \(\|a\|_1^\Delta\le1\), uniformly.
In particular \(Qa=0\). Even the optional source-field interpretation
is available here: \(a=B\Delta a\) by (22).

SA 7065–7073 constructs the average from contours and their means.
For \(e^{i\eta u a}\) with (23), all bonds except direction one are
identities, and direction-one bonds depend only on \(x_1\). Every contour
transport reduces, by cancellation of backtracks, to the same ordered
one-dimensional transport. Thus comb and symmetrised contour choices
agree on this field. A mean of identical matrices is that matrix, by
its defining logarithm equation and the small branch.

The plain top average in direction one is therefore
\[
             P_n(u)=\prod_{j=0}^{n-1}\exp(iu a_1(j/n)/n).
 \tag{24}
\]
All other directions give the identity. The straightening of
SA 7092–7106 conjugates this product by the accumulated node factor:
the two endpoint factors coincide by period one. This can also be seen
by telescoping the intermediate endpoint factors along the coarse path.
The node factor is \(I+O(u)\). Since the linear coefficient of (24)
vanishes, conjugation does not change its quadratic logarithmic coefficient.

I 13980–14012 specifies both the fixed equation for \(X\) and
“\(Q_j(U;\eta\,\mathfrak L^J(A'))=\ell_j Q_jA'\)”.
Here the identity follows directly from the remainder definition.
Write \(q(A)\) for the actual average logarithm. In this unit-scale
sector \(C(A)=q(A)-QA\). Since \(QH^J=I\), the inner fixed equation gives
\[
 q(A'-H^JX)=QA'-X+C(A'-H^JX)=QA'.
\]
At \(J=0\), substitute \(A'=ua\). If \(q_2(a)\) denotes the quadratic
logarithmic coefficient, the order-two equation is
\(-QH_0x_0+q_2(a)=0\). Hence \(x_0=q_2(a)\). This identifies the
coefficient with \(C_2(\ell a,\ell a)\), including its sign.

Expanding the finite product and its logarithm through degree two gives
\[
 C_2(\ell a,\ell a)=x_0,
 \qquad (x_0)_1=c_n\tau_3,\quad (x_0)_\nu=0\ (\nu\ne1),
 \qquad c_n=-\frac1{2nA_*^2}\cot(\pi/n).                 \tag{25}
\]
This is an actual produced quadratic datum. For detail, the commutator
of the unnormalised fields at indices \(r<s\) is
\(2i\sin(2\pi(s-r)/n)\tau_3\). The coefficient of
\(i^{-1}\log P_n\) is consequently
\(-n^{-2}A_*^{-2}\sum_{m=1}^{n-1}(n-m)\sin(2\pi m/n)\tau_3\).
For \(z=e^{2\pi i/n}\), differentiating the finite geometric sum gives
\(\sum_{m=1}^{n-1}(n-m)z^m=nz/(1-z)\).
Its imaginary part is \((n/2)\cot(\pi/n)\), proving (25).
For \(n\ge3\), \(\cos(\pi/n)\ge1/2\) and \(\sin(\pi/n)\le\pi/n\), so
\[
                       |c_n|\ge\frac1{4\pi A_*^2}.      \tag{26}
\]
Only this lower bound will be used.

### 6.3 Bounded independent currents which isolate one coefficient

Write \(\theta_1(x)=2\pi(x_1+\eta/2)\),
\(\theta_2(x)=2\pi(x_2-\eta/2)\), and \(\phi(x)=\cos\theta_2(x)\).
Choose \(M=\lfloor n/8\rfloor\), for \(n\) large enough that \(M\ge4\), and set
\[
 S_M(\theta)=\sum_{k=1}^M\frac{\sin(k\theta)}k,
 \quad P_M(\theta)=\sum_{l=2}^M\frac{\sin(l\theta)}l,
 \quad C_*=2+\pi,
\]
\[
 f_n(x)=C_*^{-2}S_M(\theta_1(x))P_M(\theta_2(x)),\qquad
 (J_1)_1=\phi\tau_1,\quad (J_2)_1=f_n\tau_3,
 \quad (J_i)_\nu=0\ (\nu\ne1).                         \tag{27}
\]
Both currents have mean zero and sup norm at most one.

I 94452–94456 defines the K109 current condition as
“\(\sup\ell^3|J'|\le\gamma^\flat\)”. I 95072 says this class
“imposes no other condition on \(J\)”. These lines remove a possible
admission ambiguity. The flat real reference and zero potential
satisfy its curvature, potential, local-gauge and logarithm
conditions exactly. The domain does not impose a derivative bound
on the independent currents in (27). We use the global periodic
determining set, so no cut boundary or specialised real-core
invocation is needed.

Here is the uniform sine-sum bound used in that assertion. Reduce an
angle to \(0<\theta\le\pi\) by periodicity and reflection. A geometric
sum bounds any consecutive partial sum of \(\sin(k\theta)\) by
\(1/\sin(\theta/2)\le\pi/\theta\). If \(0<\theta\le1\), take
\(m=\lfloor1/\theta\rfloor\). The first \(\min(m,M)\) terms of
\(S_M\) have total absolute value at most one, since
\(|\sin(k\theta)|/k\le\theta\). When \(M>m\), summation by parts bounds
the remaining terms by \(\pi/(\theta(m+1))\le\pi\).
For \(\theta>1\), summation by parts from the first term gives the
bound \(\pi/\theta\le\pi\). The zero angle is immediate. Thus
\(|S_M|\le1+\pi\), and \(|P_M|\le2+\pi=C_*\).
The inequality for \(\sin(\theta/2)\) is the chord bound from its
concavity on \([0,\pi/2]\). The means vanish by the finite geometric sum;
all frequencies used are nonzero and smaller than \(n\).

Let \(J=sJ_1+tJ_2\). Derivatives below are at \(s=t=0\).
Put \(d_k=2n\sin(\pi k/n)\). From the defining insertion pairings,
at a flat base,
\[
 \mathfrak j_J(A)(x)=\frac i2\sum_\mu
 \{[A_\mu(x),J_\mu(x)]+[A_\mu(x-\eta e_\mu),J_\mu(x-\eta e_\mu)]\}.
 \tag{28}
\]
To check this, insert \(c^{(1)}=(i/2)[\lambda_-+\lambda_+,A]\), expand
the trace pairing, and collect the two occurrences of each site variable.
This also checks the endpoint convention in (28).
Collecting the field variable instead gives the companion insertion
\[
 (\mathfrak k_J\lambda)_\mu(x)
      =\frac i2[J_\mu(x),\lambda(x)+\lambda(x+\eta e_\mu)].
\]

For any constant coarse input \(b\), \(\Lambda H_0b=0\). Thus (16),
(22), and the definition of \(\Theta'_J\) give
\[
                  H_i b=D\Delta^{-2}\mathfrak j_{J_i}(b).
 \tag{29}
\]
For \(J_1\), the right side has only field component two, because its
site input depends only on \(x_2\). For \(J_2\), it is a gradient.
Consequently, for every such \(b\),
\[
 \langle H_1b,J_2\rangle=0,
 \qquad \langle H_2b,J_1\rangle
       =\langle\Delta^{-2}\mathfrak j_{J_2}(b),D^*J_1\rangle=0.
 \tag{30}
\]
Here \(D^*J_1=0\), since its only component is direction one and it is
independent of \(x_1\). Periodicity makes the coarse vectors
\(H_i^TJ_j\) constant. Pairing them with every constant \(b\) in (30)
therefore proves that they vanish, not merely that their total means do.
Likewise \(H_0^TJ_i=0\), since both currents have mean zero.

The operator \(\Theta_J\) is the quadratic constraint paired against
\(H^{J,T}J\), by I 13728–13733. It follows from (30) that
\[
        \Theta_1=\Theta_2=\Theta_{12}=0,
        \qquad T_1=T_2=T_{12}=0.                        \tag{31}
\]
For example the mixed derivative of its weight is
\(H_1^TJ_2+H_2^TJ_1=0\). Differentiating \(T=I+G\Theta\), with
\(\Theta_0=0\), proves the second set of identities. Thus all three
extra terms involving \(x_1,x_2,x_{12}\) in (17) vanish exactly.

For the particular input (25), equation (28) gives
\[
 \mathfrak j_{J_1}(x_0)=-2c_n\phi\tau_2,
 \quad \mathfrak j_{J_2}(x_0)=0,
 \quad H_2x_0=0,
 \quad \lambda_1:=\Lambda H_1x_0=-2c_nd_1^{-4}\phi\tau_2.
 \tag{32}
\]
Since \(H_1x_0=D\lambda_1\) has only component two,
\(\mathfrak j_{J_2}(H_1x_0)=0\). The \(m_3\) term also vanishes:
it pairs \(D_1\lambda_1=0\) with the only nonzero component of \(J_2\).
Equation (18) gives
\[
 m_4(J_2,\lambda_1)=2c_nd_1^{-4}f_n\phi\tau_1.
\]
The remaining \(\mathfrak k_{J_2}\lambda_1\) has only field component one.
Therefore (16), (22), and (31) yield the exact component identity
\[
 \left(\partial_s\partial_t\mathcal Q_{sJ_1+tJ_2}(a)\big|_0\right)_2(0)
   =2c_nd_1^{-4}
         \bigl(D_2\Delta^{-1}D_1^*(f_n\phi)\bigr)(0)\,\tau_1.
 \tag{33}
\]
The mean projection in \(\Delta B=I-\Pi_0\) has no effect here:
the displayed component is a difference and has mean zero. No other
term of the full mixed coefficient was omitted.

### 6.4 The discrete coefficient diverges, by a finite-sum estimate

Expand
\[
 \cos\theta\,P_M(\theta)=\sum_{r=1}^{M+1}\beta_r\sin(r\theta).
\]
The identity \(2\cos\theta\sin(l\theta)=\sin((l+1)\theta)+\sin((l-1)\theta)\)
shows that every \(\beta_r\ge0\). For \(2\le r\le M-1\), it also gives
\(\beta_r\ge1/(4r)\): the term \(l=r+1\) alone contributes
\(1/(2(r+1))\ge1/(4r)\).

The half-lattice shifts in (27) fix the signs in the next computation.
For a sine mode in coordinate one,
\[
 D_1^*\sin(2\pi k(x_1+\eta/2))=-d_k\cos(2\pi kx_1).
\]
In coordinate two,
\[
 \left.D_2\sin(2\pi r(x_2-\eta/2))\right|_{x_2=0}=d_r.
\]
The component Laplacian has eigenvalue \(d_k^2+d_r^2\) on their product.
It follows, term by term in the finite sum, that
\[
 \bigl(D_2\Delta^{-1}D_1^*(f_n\phi)\bigr)(0)
 =-C_*^{-2}\sum_{k=1}^M\sum_{r=1}^{M+1}
       \frac{\beta_r}{k}\frac{d_kd_r}{d_k^2+d_r^2}.       \tag{34}
\]
All summands have the same sign. No limiting Green-kernel asymptotic
or computer summation is involved.

For \(1\le k\le n/2\), the chord and tangent bounds for sine give
\(4k\le d_k\le2\pi k\). Take \(K=2^j\), with \(j\ge1\) and
\(2K\le M-1\). For \(K\le k,r<2K\),
\[
 \frac1k\ge\frac1{2K},\qquad
 \beta_r\ge\frac1{8K},\qquad
 \frac{d_kd_r}{d_k^2+d_r^2}\ge\frac1{2\pi^2}.
\]
There are \(K^2\) ordered pairs in this square. Its contribution to the
absolute value of (34) is therefore at least
\(1/(32\pi^2C_*^2)\).
The squares for different \(j\) are disjoint. Define
\[
 q_n=\#\{j\ge1:2^{j+1}\le\lfloor n/8\rfloor-1\}.
\]
Then \(q_n\to\infty\) as \(n=L^k\to\infty\), and
\[
 \left|\bigl(D_2\Delta^{-1}D_1^*(f_n\phi)\bigr)(0)\right|
                   \ge\frac{q_n}{32\pi^2C_*^2}.         \tag{35}
\]
This is a symbolic counting argument over disjoint integer intervals.
For any prescribed number of intervals, choosing \(L^k\) sufficiently
large includes them. No numerical count is used.

Since \(d_1\le2\pi\), equations (26), (33), and (35) prove
\[
 \left|\left(\partial_s\partial_t\mathcal Q_{sJ_1+tJ_2}(a)
                  \big|_0\right)_2(0)\right|
       \ge c_*q_n,\qquad
 c_*:=\frac{2}{4\pi A_*^2(2\pi)^4\,32\pi^2C_*^2}>0.   \tag{36}
\]
The calculation has isolated a term of the *complete* actual coefficient.
The other terms vanished by (30)–(32), rather than by an assumed spatial
regularity bound or an identity on the physical current graph.

### 6.5 Consequence for (Q), (B4), and the requested common domain

Let \(\gamma_*\le a_\gamma\) be the fixed positive current ceiling
of the chosen K109 domain. Take \(r=\gamma_*/8>0\). Equations (27) give
\(|sJ_1+tJ_2|_{-3}\le2r<\gamma_*/2\) on the closed bidisc
\(|s|,|t|\le r\). These are admitted independent currents. The background
is exactly flat. No current derivative is an admission condition here.

If (Q) held with a common \(C_Q\) and the actual maps were holomorphic
on this bidisc, Cauchy's coefficient formula would give
\[
 \left|\partial_s\partial_t\mathcal Q_{sJ_1+tJ_2}(a)\big|_0\right|_{-3,1}
                         \le C_Q/r^2.                  \tag{37}
\]
This contradicts (36). Thus (Q) fails on any such common analytic domain.
By (14), (B4) fails there as well.

One can describe the violating furnished triples without choosing a
Taylor truncation as a field. Let \(\varepsilon>0\) be the common datum
radius, and fix \(\rho=\varepsilon/2\). For the actual furnished solution,
let \(F_n(s,t,u)\) be the scalar \(\tau_1\)-coefficient of
\((\Delta H^{sJ_1+tJ_2}X(-ua,0))_2(0)\).
The coefficient of \(stu^2\) in this holomorphic function is exactly
the scalar coefficient in (33), by (13) and (31). Its magnitude is at
least \(c_*q_n\).
The three Cauchy coefficient integrals imply
\[
 \max_{|s|=|t|=r,\ |u|=\rho}|F_n(s,t,u)|
                       \ge r^2\rho^2c_*q_n.             \tag{38}
\]
The maximum exists by continuity on the compact product of three circles.
Choose a maximizer. At this admitted base, compare the actual furnished
triples with data \((-ua,0)\) and zero. Their datum distance is at most
\(\rho\), while (38) is a lower bound on their Laplacian correction.
The ratio is at least \(r^2\rho c_*q_n\), which tends to infinity.
This is an existence choice of actual witnesses, not a numerical search.

Only a fixed matrix coefficient was used. In operator norm its absolute
value is at most the matrix norm, since
\(|\tfrac12\operatorname{tr}(\tau_1 A)|\le\|A\|\).
Thus the scalar lower bound is also a lower bound for the required norm.
All fields have physical period one on the same fixed torus. The failure
is in mesh uniformity alone.

The analytic-domain qualification is essential. This argument proves
\[
 \boxed{\text{the common analytic realization requested in (G)}
                  \ \Longrightarrow\ \neg\text{(B4) on that domain}.}
 \tag{39}
\]
It does not infer existence on a common domain from finite germs.
If that realization is not supplied, (36) still holds for the actual
finite germs, but (38)'s common circles are not asserted to exist.
This is why the result is stated as an incompatibility of the two
requested uniform assertions, rather than an unconditional existence
claim for all the violating triples.

## Result

**Target 1.** The native block-chart theorem already gives uniform radii
under its stated operator and averaging hypotheses. Equations (3)–(9)
port that implication with explicit closed-ball margins and extend it to
the field datum (S5). Equation (7a) also gives the forcing graph bound
from the admitted (N1), wherever that input applies to these furnished maps.
The actual primitive hypotheses on every proposed determining set are
not proved here; their construction reaches the S1/B99-W ownership
boundary. Thus the unqualified actual assertion (G) remains unproved.

**Target 2.** Equations (20)–(39) prove a counterexample conditional on
the requested common analytic realization: (G) and (B4) cannot both hold
for the proposed general datum (S5). The actual flat periodic coefficient
grows at least as \(c_*q_n\), with \(q_n\to\infty\). Equations (37)–(38)
turn that calculation into failure of any common (B4) constant on such
a domain. The inner input is the actual quadratic constraint image,
not an arbitrary block vector. All extra terms from its current
dependence were checked and vanish. No computer-assisted step enters.

This is a proof of an incompatibility, not a proof that (G) alone is
false. It does not refute the block-only physical chart or identify the
missing general layer theorem with (S5). It shows that this proposed
general-field extension cannot supply the uniform five-norm package on
the stated independent-current domain. Replacing that domain by an
own-current graph, or changing the layer equation or the norm, would be
a different statement. No such replacement is claimed proved here.

**Invocation changes:** none of U01–U34 moves from partial to covered.
U15 retains its first-round coverage conditional on (N1); this note does
not recheck or promote it. U16's general five-norm invocation cannot be
discharged by combining (S5), the common analytic realization, and (B4).
No conclusion about the surrounding downstream theorem is asserted.

Recovery checkpoint: source identities appear above. Equations (3)–(9)
are the conditional radius port. Equations (20)–(36) are the exact flat
counterexample calculation. Equations (37)–(39) state precisely what it
rules out.
Do not reopen the owned primitive-walk task here. CA-LAYER/(N1) remains
the named input; this note neither attacks it nor changes its status.

Sources used: GOAL; FINISH's published-work, efficiency and rules text;
the whole first-round note; `layer-find.md:658–674` and its source table;
the registry and port-map matches; the outline-index instructions,
chunks 05, 07 and 10's relevant rows and neighbours, and obligations 534–552;
`lit-balaban.md:131–168`; I 12935–13035, 13165–13245,
13546–14710, 15265–15445, 94176–94206, 94444–94478, 95038–95080,
112570–112620; SA 7054–7073, 7092–7116,
10111–10186, 10354–10410, 10562–10576, 11257–11282, 11313–11358, 11441–11449.
Source searches and hashes establish provenance only. No independent
provider has checked this note. Only `library/layer-r2.md` was written.

RESULT: the uniform-radius port is proved with its native hypotheses; an exact flat periodic calculation proves that the common analytic (S5) realization and R_Delta (B4) are incompatible; no additional U01–U34 invocation is covered.
