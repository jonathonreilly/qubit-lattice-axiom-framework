# LAYER-THM: conditional package and realization obligations

**Provenance:** Codex (gpt-6-astra), laptop, 2026-11-07; FINISH row 441,
requested max effort. Checkout 94df5579a4f6b9fe19bfea322991e8a4a761dc9f.
Research text, not an audit; no scientific status is granted. This is the
generation round. Distillation and an independent referee are separate work.
No computer-assisted step discharges an assertion below. Runs only located
text and recorded source identities.

**Result.** The conditional theorem below is proved. LAYER-THM on the
account's actual completion domains is **not proved**. The switched graph
estimates, localized admission and general-field identification remain open
at the specific proof steps recorded below. Clause (e) has no recovered independent
content. U33 has an existing conditional supplier in CA-II §5.8, whose
identification with the required response remains an obligation. Every
requested item is treated; failure at one was not used to skip another.

Credit: Tadeusz Balaban for the averaging, propagator, chart and walk
constructions; Ethan Sussman and Levent Alpoge, with Claude and Codex as
authors of their account, for the supplied texts. Existing contraction and
cutoff proofs are reused with their check reports' repairs.

## 1. Sources, ownership and objects

I, II, III and SA mean the three complete-account files and
YM4_sketch_500.tex in /Users/jonreilly/ym4d-lead/sa, supplied revision
31a47c543775. Locators are physical lines. This directory is a source
snapshot, not a separately verified Git HEAD.

| Source | SHA-256 |
|---|---|
| I | 4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93 |
| II | 6a1f74b05f74ba44a2186c11fb08e139178d86b15c1494a95c434212944b2b8f |
| III | 7e36523b85fb4f85aefdd45ab175420459f24e34fe56a4e83e53a6829c7a352d |
| SA | d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f |

library/prior/layer-pkg.md is absent. The registry assigns LAYER-THM and
CA-LAYER/(N1) to layer-thm; older stage-claude attribution is superseded.
B98-P5, PRINT-INVERSE and stage-response-identification retain their owners.
Their existing proofs and the latter's full stage-family identification are
not redone here. The workflow path named by AGENTS.md is absent.
Only this library file is changed.

Outline navigation used sa-index/README.md, neighbouring rows in chunks
05 and 10 and obligations.md, then the cited bounded source lines.
SA 10562–10578 distinguishes the two response systems and warns about
switched second-order bounds. The ca-full index locates §5.8 below; its
status labels are not used as evidence. Balaban's originals were not
consulted: his citations identify quotations in the account and
library/lit-balaban.md.

The reusable inputs are layer-r2.md §2 (uniform contraction from (3));
gates/layer-thm-gate.md (four-entry repair, U07, cutoff and failure of B4);
print-inverse-r2.md §§3,11 with its gate; b98p5-r2.md with its gate;
gates/stage-gate.md and ca-f.md §3. b98p5-r3.md is absent.

### 1.1 Norms, datum and base

Use the consumer's finite four-dimensional hierarchy, spacing \(\eta\),
scales \(\ell_j=L^j\eta\), enlarged cells and **full** difference stencils.
Set
\[
 N_y(a)=\max\{\ell_y|a|_y,\ell_y^2|\nabla_Wa|_y\},\qquad
 N_y^\Delta(a)=\max\{N_y(a),\ell_y^3|\Delta_Wa|_y\}.       \tag{1.1}
\]
\(\Delta_W\) is the component covariant Laplacian, not the Wilson Hessian
\(\mathcal D(W)\). Transposes are bilinear trace transposes.
Write \(E,E^\Delta,B,F\) for first-order fine fields, graph-norm fine
fields, dimensionless block data and sources of weight \(-3\).
For positive admitted \(p\),
\[
 \|a\|_p=\sup_yN_y(a)/p(y),\quad
 \|a\|^\Delta_p=\sup_yN_y^\Delta(a)/p(y),\quad
 |f|_{-3,p}=\sup_y\ell_y^3|f|_y/p(y),                       \tag{1.2}
\]
and \(|b|_p\) uses the consumer's block-to-cell convention. The datum is
\[
 d=(j,b),\quad j\text{ a field},\qquad
 \|d\|_{\mathrm{dat},p}=\|j\|^\Delta_p+|b|_p.              \tag{1.3}
\]
Changing the first-slot norm requires a conversion.
Weights are the actual \(\mathfrak M_\delta\); their estimates use
\(p(y')\le e^{\delta d^\wedge(y,y')}p(y)\). If that inequality alone
does not define the class, a new weight's other admission conditions
must also hold. The constant weight \(1\) is admitted, and
\(N(a)=\|a\|_1\). The norm \(|SA|\) is the dimensionless fine-value
supremum, so \(|SA|\le N(A)\).

\((W,J)\) has independent complex \(J\) with its stated weight-\(-3\)
bound only. No current derivative, Hölder bound or own-current identity
is assumed.

### 1.2 The equation is fixed before its estimates

For the intended realization, at switches one,
\[
 \begin{split}
 G_0&=(\mathcal D(W)+D_0RD_0^T+Q^TaQ)^{-1},\quad
 q_0=(QG_0Q^T)^{-1},\quad a=\ell^{-2},\\
 H_0&=G_0Q^Tq_0\ell^{-1},\quad B_0=G_0-G_0Q^Tq_0QG_0,\\
 G_\pi^J&=(I-G_0\Theta'_J)^{-1}G_0,\quad
 q_J=(QG_\pi^JQ^T)^{-1},\quad H^J=G_\pi^JQ^Tq_J\ell^{-1},\\
 \langle A,\Theta_JA\rangle&=2\langle H^JC^{(2)}(\ell A),J\rangle,
 \quad \widetilde G^J=(I-B_0\Theta_J)^{-1}B_0 .
 \end{split}                                                \tag{1.4}
\]
\(Q,Q'\) are the literal CMP 98 rows; \(C\) is their nonlinear
constraint remainder. \(R\) is the scalar gauge projection;
\(\Theta'_J,\Theta_J\) are distinct insertions, I 13683–13798.
At switches the symbols mean the account's specified walk sums and
composites. The inverse identities in (1.4) are not asserted there.

Take \(H=H^J(\sigma)\), \(G=\widetilde G^J(\sigma)\),
\(S:A\mapsto\ell A\), \(\Gamma=G\Theta_J\), \(T=I+\Gamma\).
The proposed general-field extension is
\[
 z=-Tj+\Gamma H_0b-GV'_\sigma(z+H_0b),\quad
 A'=z+H_0b,\quad X=C_\sigma(SA'-SHX),\quad \mathbb H=A'-HX .
                                                               \tag{S5}
\]
It is the account's block chart at \(j=0\), I 14386–14425,
15311–15320, with its hypotheses.
\(V'\) is the actual seven-term function I 14156–14375. To fix it, write
\(D(A)=X(A)\), \(\mathfrak D=D_AD\),
\(D_3=D-C^{(2)}(SA)\), \(\mathfrak D_3=D_AD_3\); then
\[
 \begin{split}
 V'(A)={}&-\mathfrak D_3^TH^TJ-Q^T\mathsf kD
 -\mathfrak D^T\mathsf k^TQA+\mathfrak D^T\ell^{-1}\mathsf kD\\
 &+(I-H\mathfrak D)^T\nabla V_0(A-HD)
 -\Lambda^T\mathfrak j_J(HD)-\mathfrak D^TH^T\mathfrak k_J(\Lambda A).
 \end{split}                                                \tag{1.5}
\]
The account's \(\mathsf k,\Lambda,\mathfrak j_J,\mathfrak k_J,V_0\)
and every tag are retained. An arbitrary quadratic substitute is not
a realization. General-field identification is addressed separately in §7.

## 2. Literature inputs and their domain

### 2.1 PI

Use repaired Theorem PI with literal rows and Dirichlet spaces: fine bonds
have at least one endpoint in \(\Omega_0\), scalar sites are in
\(\Omega_0\), and the Hessian reads protruding plaquettes on
\(\Omega_0^+\). Its hypotheses include:

* (S1-loc): every prescribed model box \(N(x)\), half-side \(r_N\ell_j\)
  at a centre of height \(j\), has one real gauge \(U_r^u=e^{i\eta A}\)
  with \(\ell_{\lambda(z)}|A|,\ell_{\lambda(z)}^2|\nabla A|\le L^2a_0\).
  Exterior reads have height zero.
* (S2), plus (S2+) on the entire exterior coefficient read.
* The theorem's block/gap floors, fixed model parameters and torus room
  \({\rm side}(\mathbb T)\ge(2\widehat r+2)\ell_k\).

It gives the bare inverse, bilinear symmetry, holomorphy and
\[
 |q_0(y,y')|\le C_q\ell_j^{-2}\ell_{j'}^{-4}
                              e^{-\delta_qd(y,y')},        \tag{2.1}
\]
with source measure \(\ell_{j'}^4\), and analytic local walks with
absolute sums, spare factors and full footprints \(F_\tau\).
For K10 use rate at most \(\delta_q/17\), decoupling side greater than
\(2\widehat r\ell\), and subsequent floors at that rate. The checked
anchored-tree bound is \(17D_X(n+1)\).

If word bounds are \(a_\omega e^{-2\mu t_\omega}\), \(\sum a_\omega\le B\),
and tags obey \(|\sigma^\omega|\le e^{c\kappa_1}e^{\mu t_\omega}\), then
\[
 \sum_\omega\|\sigma^\omega O_\omega\|
 \le e^{c\kappa_1}\sum_\omega a_\omega e^{-\mu t_\omega}
 \le e^{c\kappa_1}B.                                      \tag{2.2}
\]
The same bound for tails proves local uniform convergence and holomorphy.
Connected retained footprints prove zero-switch component separation.
This assembly does not manufacture missing majorants for other operators.

**Loc[U]**, for each invocation U, names the obligation to supply all
these local gauges, exterior twists, torus room and common-rate floors
at every base and determining set U actually evaluates.
Proposition 3.1 supplies its interior (S1-loc) part from (S1) on a
verified thick tower, with \(N(x)\subset\Omega_0\): its aligned cells
have sides at least \(12M_b\ell_i\), at the same propagator block size.
A proper outer boundary still needs its gauges. On
\(\Omega_0=\mathbb T_\eta\) the boundary issue disappears, not thickness.
The previously checked thin-finger and crossing-bond examples are reused.
Writing “global” or \(\mathfrak K_{109}\) is not a Loc[U] certificate.

PI supplies neither all vector/Hölder propagator bounds, graph-norm walk
majorants, nor termwise lattice covariance of the full one-family
hypothesis. These remain separate inputs.

### 2.2 B98-P5

The checked carrier bridge uses the real-reference condition
\[
 \|U_r(\partial p)-I\|_F
 \le\sqrt N\,\alpha(\eta/\ell_{\min\{\lambda(v):v\in p\}})^2,
 \qquad\alpha\le8a_0                                    \tag{PL}
\]
on every relevant plaquette, defining \(\mathfrak S^{\rm pl}\) when
adjoined to the other base conditions. The row's double block
\(E_c\subset\Omega_{j-1}\) gives (D) with constant \(8\sqrt N L^2a_0\).
On (TH), a class cube of height \(j-1\) or \(j\) contains \(E_c\);
the one-gauge calculation gives \(4\sqrt N L^2a_0\).
Height-zero rows are linear. These existing proofs are not repeated.

**AV** is the named local analytic port of CMP 98 Proposition 5,
including fine derivative densities and Hessian contractions on a common
larger complex ball, after either carrier bridge or a supplied frame.
It remains unchecked in the prescribed sources. A value estimate alone
does not bound the transpose derivatives in (1.5).

CMP 109 (i)–(iii), including the real-reference (1.11), imply (PL) under
I 13000–13034's inclusion ceilings. U02's induction and U19/U27's stage
setting invoke that space. **On its full representative and under those
ceilings**, their admitted bases lie in \(\mathfrak S^{\rm pl}\);
this does not prove induction-wide membership.
The localized class at I 94448–94456 instead lists only cube (3.35),
twist (3.37) and current size. It does not thereby imply (PL).
U05's separate \(\mathsf p(U^0)\le1\) is not the required
\(\alpha\le8a_0\) smallness. A supplied frame is a separate route to AV.

**Avg[U]** names this carrier/frame and complex-radius obligation at
every call made by U. The final table records the PL implications and
the admissions that remain unverified.

## 3. One conditional LAYER theorem

This theorem is an implication for the specified operator datum. Its
primitive hypotheses are exposed; proving the implication does not
establish them on actual completion kernels.

### 3.1 Hypotheses and radii

On a common open analytic base/switch domain, uniformly in mesh, volume,
depth and determining set, suppose the following bounds. All named
operators and nonlinear maps, including \(P_1,m_H\) and the rider's
coefficients and \(F\), are analytic there in the actual base coordinates.
\[
 \begin{gathered}
 \|SH\|\le h,\quad \|H_0\|_{B\to E}\le h_0,\quad
 \|G\|_{F\to E}\le g,\quad \|\Theta_J\|_{E\to F}\le\theta,\\
 C(0)=DC(0)=0,\quad\|D^2C(u)\|\le c\quad(|u|<s_C),\\
 V'(0)=DV'(0)=0,\quad |V'(A)|_{-3}\le vN(A)^2
                                     \quad(N(A)<s_V).
 \end{gathered}                                             \tag{3}
\]
The last line is on the inner small branch, with surrounding analytic
room as in the proof below. Enlarge \(c,h,h_0,g,v\) to at least one.
Set
\[
 q=gv,\quad t=1+g\theta,\quad k=g\theta h_0,\quad
 a_*=1+h_0+t+k,\qquad
 r\le\min\{s_C/32,s_V/8,(64ch)^{-1},(64q)^{-1}\},
\]
\[
 r_X=8cr^2,\qquad\varepsilon=r/(8a_*),\qquad r>0.          \tag{3.1}
\]
For every admitted weight, suppose additionally
\[
 \begin{array}{lll}
 \|Hb\|_p\le h_1|b|_p,&\|H_0b\|_p\le h_0|b|_p,&
 \|\Gamma u\|_p\le\gamma\|u\|_p,\\
 |DC(v)Su|_p\le c_wr\|u\|_p,&
 \|D(GV')(A)u\|_p\le\nu\|u\|_p,&\nu\le\tfrac12,\\
 \|H_0b\|^\Delta_p\le h_\Delta|b|_p,&
 \|\Gamma u\|^\Delta_p\le\gamma_\Delta\|u\|_p,&
 \|D(GV')(A)u\|^\Delta_p\le\nu_\Delta\|u\|_p,\\
 |P_1u|_{-3,p}\le p_1\|u\|_p,&
 |m_Hb|_{-3,p}\le m_1|b|_p.&
 \end{array}                                                \tag{W}
\]
Constants are uniform in \(p\). The \(DC\) bound holds for \(|v|\le3r\);
the nonlinear derivative bounds hold for \(N(A)\le2r\).
Also \(\|Su\|_{0,p}\le\|u\|_p\). Reduce \(r\) so \(c_wr h_1\le1/2\).
There is no graph bound on \(H\) or \(\mathbb H\). A graph bound on
all of \(G\) is a stronger sufficient input, not necessary to this
statement: (W) asks only for its two composites used in (S5).

The following structural premises are attached only where used:

* **EQ:** the operators, nonlinear functions and data intertwine under
  the gauge, conjugation or restriction map in question, tags included.
* **PH:** the specified physical critical solution satisfies the same
  unswitched equation, constraint and logarithm branch at
  \(j=0,J=\mathcal J(W)\), and lies in (3.2). Alternatively both it
  and our constructed branch lie in the existing chart's known
  uniqueness domain. Its chart current has the physical current identity.
  I 15669–15701 supplies this on its admitted diagonal domain; a
  smaller branch can be compared inside that chart's uniqueness ball.
* **LC:** at zero wall switches the primitives read only their retained
  component, full stencils included, and restrict to the identical
  component construction. Both datum slots vanish on a component asserted
  to have no data.

For the rider also assume (R) of §5 for the specified \(P_1,m_H\).
Reduce the datum ceiling if necessary to meet its local smallness.
Every reduction precedes the final running-coupling ceiling.

### 3.2 Clauses, corollary and parameterized form

For \(\|d\|_{\mathrm{dat},1}<\varepsilon\), the following hold.

**(a)** (S5) has exactly one solution in the product domain
\[
 N(z)\le r,\qquad |X|\le r_X.                              \tag{3.2}
\]
Its triple is jointly holomorphic in admitted base, independent current,
switches and datum; it vanishes at datum zero. This is the uniqueness
domain, not an assertion of uniqueness among all fields.

**(b)** At a fixed kernel, any two admitted data obey, for every admitted
weight,
\[
 \max\{\|\delta A'\|^\Delta_p,\|\delta\mathbb H\|_p,
 |P_1\delta A'|_{-3,p},|m_H\delta X|_{-3,p}\}
 \le B_{\mathbb H}\|\delta d\|_{\mathrm{dat},p}.             \tag{N1}
\]
There is no \(\|\delta\mathbb H\|^\Delta_p\) conclusion, and no idle
\(|\delta X|_p\) entry. The existing (B4) counterexample refutes the
former stronger demand, not (N1).

**(c)** Under EQ, transport commutes with the solution whenever its image
lies in the target uniqueness domain. Real data at a real base and real
switches give a real solution. Bounded complex-gauge charts glue after
shrinking their datum radii to fit their overlap domains. No invariance
under unbounded complex gauges is asserted.

**(d)** Under PH, at switches one and \(j=0\), the solution equals the
specified Landau representative of Balaban's response, with its physical
current increment. Continuation is in the admitted block datum, not off
the own-current graph.

**(e), proposed minimal convention:** holomorphic restriction of the
parameters/data inside this domain gives the same solution and bounds;
identical operator data in two descriptions give identical small solutions
on their admitted overlap. This redundant clause is not a recovered
statement of the unnamed side clause in the account.

**(f)** Under LC the solution and rider commute with component restriction.
A component with both datum slots zero has zero solution. Off the retained
region, zero requires the field forcing to vanish there too.

**Corollary.** Relative to datum zero, each local entry of (N1) is at most
\(B_{\mathbb H}\|d\|_{\mathrm{dat},p}p(y)\). Independently,
\[
 N_y(HX)\le N_y(A')+N_y(\mathbb H)
           \le N_y^\Delta(A')+N_y(\mathbb H).                \tag{3.3}
\]
A field-datum operator with
\(\|L_\sigma f\|^\Delta_p\le K_\#|f|_{-3,p}\) may be substituted as
\(j=L_\sigma f\) when its source convention and support match (S5).
This does not prove that field-datum bound.

**Parameterized form.** Holomorphic substitution of any admitted
parameter family is allowed. A finite chain is jointly holomorphic
provided every intermediate image remains in its own domain on the whole
product polydisc, not only at the physical centre.

**Rider.** The formulas in §5 are holomorphic and satisfy (5.3), (5.9)
under (R) and the smallness conditions there. Physical interpretation
uses (d).

### 3.3 Proof of (a): the common radius

This is the existing layer-r2 proof, included to make the implication
self-contained. For \(N(A')\le2r,\ |X|\le8cr^2\),
\[
 |SA'-SHX|\le2r+8chr^2\le17r/8<3r.
\]
Taylor's integral formula gives \(|C(v)|\le c|v|^2/2\) and
\(\|DC(v)\|\le c|v|\). The inner map has image at most
\(9cr^2/2<r_X\) and contraction factor \(3chr\le3/64\).
For \(N(A')\le4r\), use auxiliary radius \(32cr^2\): its argument is
at most \(9r/2\), image at most \(81cr^2/8\), and contraction factor
at most \(9/128\). The branches agree by uniqueness. This supplies room
around the smaller branch.

The datum ceiling gives
\[
 N(H_0b)\le r/8,\qquad N(-Tj+\Gamma H_0b)\le r/8.
\]
On \(N(z)\le r\), \(N(A')\le9r/8<2r\), so the outer map is bounded
by \(r/8+4qr^2\le3r/16<r\). For \(N(A)\le2r\), Cauchy's formula on
\(A+\zeta u\), \(N(u)=1,|\zeta|=2r\), bounds \(D(GV')(A)\) by
\(16qr^2/(2r)=8qr\le1/8\). Apply norm-one linear functionals to
justify the vector-valued estimate and integrate along segments.

Both Picard sequences converge geometrically in their common balls.
Their locally uniform holomorphic limits are holomorphic by the Cauchy
integral formula. Zero solves the equation at datum zero. The two
contractions prove uniqueness in (3.2). Finite-dimensional invertibility
alone would not have supplied this uniform radius.

### 3.4 Proof of (c)–(f) and the corollary

Apply an intertwiner to every equation of (S5); EQ gives the target
equations. Uniqueness proves equality when the transported solution is
admitted. Conjugation at real inputs preserves the ball, proving reality.

For bounded gauges, covariance of differences and the component Laplacian
gives a finite norm conversion \(K\). Include both directions and overlap
compositions in \(K\). The bounds \(K_A,K_X\) of §4.1 show that at datum
size \(s\), a transported \(z\) has norm at most \(K(K_A+h_0)s\), and a
transported \(X\) has size at most \(KK_Xs\). Choose these below \(r,r_X\)
and the pulled-back data below \(\varepsilon\). This proves overlap
compatibility; the whole larger ball need not be invariant.

PH identifies the admitted physical solution by uniqueness. Equality
on an open real part of the block-data polydisc extends by successive
one-variable identity theorems. The independent current remains on its
physical graph throughout this argument.

Under LC, restriction commutes with both equations and preserves the
uniqueness bounds, so it commutes with the solution. On a component with
zero data, use the zero solution. Outside the retained region the
equation can still read \(-j\); the field-support qualification is essential.
Specialization and parameterization follow by composition and uniqueness.
(3.3) is the triangle inequality and (1.1); it needs neither (N1) nor
the field equation. The rest of the corollary follows by taking the second
datum to be zero. Clauses (b) and the rider are proved next.

## 4. The open item (N1): four entries, all weights, actual kernels

### 4.1 A complete four-entry deduction from primitive bounds

Let \(D_*=\|\delta d\|_{\mathrm{dat},p}\). Subtract the equivalent
outer equations
\[
 A'=-j+H_0b+\Gamma(-j+H_0b)-GV'(A').
\]
Both \(A'_i\) and their segment have \(N<2r\). By (W),
\[
 \|\delta A'\|_p\le(1+\gamma)(1+h_0)D_*+\nu\|\delta A'\|_p.
\]
Thus, with \(K_A=2(1+\gamma)(1+h_0)\),
\(\|\delta A'\|_p\le K_AD_*\).
The inner arguments lie in \(|v|<3r\); subtracting and integrating \(DC\)
along their segment gives
\[
 |\delta X|_p\le c_wr(\|\delta A'\|_p+h_1|\delta X|_p)
 \le K_XD_*,\qquad K_X=2c_wrK_A .                         \tag{4.1}
\]
This is an intermediate bound, not an extra theorem entry.

The graph estimate uses the outer equation directly:
\[
 \|\delta A'\|^\Delta_p
 \le[1+h_\Delta+\gamma_\Delta(1+h_0)+\nu_\Delta K_A]D_*
 =:K_\Delta D_* .                                        \tag{4.2}
\]
No Laplacian is applied to \(HX\). The other entries are
\[
 \|\delta\mathbb H\|_p\le(K_A+h_1K_X)D_*,\quad
 |P_1\delta A'|_{-3,p}\le p_1K_AD_*,\quad
 |m_H\delta X|_{-3,p}\le m_1K_XD_* .
 \tag{4.3}
\]
Hence (N1) holds with
\[
 B_{\mathbb H}=\max\{1,K_\Delta,K_A+h_1K_X,p_1K_A,m_1K_X\}.
                                                               \tag{4.4}
\]
This proves all four entries for arbitrary admitted \(p\), for complex
data and switches, **if (W) holds for those actual kernels**. There is
no use of B4, a current derivative, a real-data maximum principle, or
an inference from an unweighted bound to a weighted one.

### 4.2 Where the weighted primitive bounds come from

For completeness, a usable kernel lemma is as follows. Suppose an
operator has a local-size majorant \(k(y,y')\) with
\[
 \sup_y\sum_{y'} k(y,y')e^{\delta d^\wedge(y,y')}\le K.
 \tag{4.5}
\]
Source measures and all scale factors are included in \(k\).
Then
\[
 \operatorname{size}_y(Of)\le
 \sum_{y'}k(y,y')p(y')\|f\|_p\le Kp(y)\|f\|_p .
 \tag{4.6}
\]
The proof is just the weight inequality and summation of nonnegative
terms. A local factor of range \(R\) costs \(e^{\delta R}\); products
multiply constants. A nonlinear difference is the integral of its
derivative on the segment. If the derivative has (4.5) with coefficient
\(Cr\) on the ball, its weighted Lipschitz constant is \(Cr\).
For infinite walk sums use the same absolute majorants on tails.

This is the correct extension from kernel bounds to **every** admitted
weight. One needs the account's scale-sensitive summability floors; no
polynomial growth of the graded metric is asserted. The source's
exponential-weight K8 estimate alone is not a proof for every possible
weight unless its kernel/density proof gives (4.5).

Apply this calculation term by term to the seven terms (1.5): local
averaging derivatives use AV's fine densities, transposed legs use the
column versions of (4.5), kernel products use the native algebra, and
each derivative of the quadratic remainder retains one small field
factor. The inner derivative follows by
\[
 D_AX=(I+DC(SA'-SHX)\,SH)^{-1}DC(SA'-SHX)\,S.
 \tag{4.7}
\]
The inverse has weighted norm at most \(2\) under \(c_wr h_1\le1/2\).
This is a deduction conditional on those local density and kernel
majorants. PI supplies only its \(q_0\) factors. The needed vector,
Hölder and transpose inputs are not consequences of PI's energy norms.

### 4.3 Unswitched graph entry: the route that works

At \(\sigma=1\) let the bare constrained propagator obey, at every
admitted weight,
\(\|B_0f\|^\Delta_p\le b_\Delta|f|_{-3,p}\) and
\(\|B_0f\|_p\le b|f|_{-3,p}\). In this paragraph also assume
\(|\Theta_Ju|_{-3,p}\le\theta\|u\|_p\), uniformly in \(p\), enlarging
\(\theta\) if needed; this is a weighted kernel-algebra premise,
not an inference from (3)'s unweighted bound. Suppose
\(b\theta\le1/2\). The actual identity
\[
 G=B_0+B_0\Theta_JG
 \tag{4.8}
\]
gives \(\|Gf\|_p\le2b|f|_{-3,p}\), and consequently
\[
 \|Gf\|^\Delta_p\le b_\Delta(1+2b\theta)|f|_{-3,p}.
 \tag{4.9}
\]
Only \(\Theta_J\), a bounded source insertion, occurs. No differentiation
of \(J\) is introduced. The bare graph bound follows from those for
\(G_0,H_0\) and the bounded map \(\ell QG_0:F\to B\) through
\(B_0=G_0-H_0\ell QG_0\). These are precisely the **bare** graph inputs,
not a graph assertion for \(G_\pi^J\).
Combining (4.9) with the source norm of \(DV'\) supplies
\(\gamma_\Delta,\nu_\Delta\) in (W); the bare \(H_0\) bound supplies
\(h_\Delta\).

For the remaining entries, \(P_1=D_0(I-R)D_0^T\) uses its native
weight-\(-2\) kernel estimate. In the block chart at switches one the
current representation identifies
\[
 m_H=Q^T\mathsf k+\Lambda^T\mathfrak j_JH^J-\Delta'H^J ,
 \tag{4.10}
\]
where \(\Delta'=\mathcal D(W)-D_1^TD_1\). The quoted bounds on
\(\Delta'\) are local first-order bounds, so (4.10) is estimated by
the first-order kernel algebra; it is not \(\Delta_WH^J\).
Here is the algebra behind the identification. Put
\(\Xi=\Theta_JA'-V'(A')\), \(P_0=I-G_0Q^Tq_0Q\), and
\(\Delta_a=G_0^{-1}\). For the block chart, \(QA'=\ell^{-1}b\) and
\[
 \Delta_aA'=P_0^T\Xi+Q^Tq_0\ell^{-1}b .
\]
In I 14386–14425 the chart current before \(F\) is
\[
 P_0^T\Xi+Q^T(q_0-a)\ell^{-1}b
       -Q^T\mathsf kX-\Lambda^T\mathfrak j_J(HX)-\Delta'\mathbb H .
\]
The first two terms are
\((\mathcal D(W)+D_0RD_0^T)A'\), by the preceding identity and the
constraint. Since
\(\mathcal D(W)+D_0RD_0^T=\Delta_W+K_W-P_1+\Delta'\) and
\(A'-\mathbb H=HX\), collecting the coefficient of \(X\) gives
(4.10) and (5.1). This derivation uses \(j=0,\sigma=1\).
For a general/current-rider convention this identification must be
verified, including the tags. Merely writing the symbol \(m_H(\sigma)\)
does not do it.

This proves an unswitched sufficient route from the stated bare
propagator inputs, AV and local coefficient bounds. It is not a new
proof of the quoted CMP 99b pointwise estimates on enlarged domains.

### 4.4 Switched \(N^\Delta(\delta A')\): exact remaining step

The gate's pointer (i) survives. Uniform first-order K10 estimates and
PI's \(q_0\) words do not yet give
\[
 H_0(\sigma):B_p\to E^\Delta_p,\quad
 G(\sigma)\Theta_J(\sigma):E_p\to E^\Delta_p,\quad
 D(G(\sigma)V'_\sigma)(A):E_p\to E^\Delta_p
 \tag{GW}
\]
with constants uniform in the actual completion kernels, weights and
\(|\sigma|\le e^{\kappa_1}\). These are exactly the three graph lines
used in (4.2). We name this obligation GW, rather than assume (N1).

Three routes were checked.

1. **Use the unswitched inverse identity.** (4.8) holds at one. The
   switched word convention counts each visited cube once, whereas a
   product of switched sums counts it separately in each factor.
   Therefore (4.8) with every factor switched is not an identity proved
   by the unswitched formula. The explicit word diagnostic in §7.2
   exhibits the defect.
2. **Differentiate the absolutely convergent walks.** This works if one
   has absolute majorants for the differentiated endpoint words. For
   example, if the leftmost bare word has total \(F\to E^\Delta\)
   majorant \(b_\Delta^*\), the remaining first-order words have total
   \(b^*\), and current insertions cost \(\theta^*\) with
   \(b^*\theta^*<1\), the product estimate gives
   \(b_\Delta^*/(1-b^*\theta^*)\). The spare exponential pays the union
   tag by (2.2). This is a rigorous sufficient route. The missing step
   is the endpoint graph majorant for the **actual** vector walks and
   their cutoff coefficients. PI gives a bare scalar inverse row,
   not that derivative estimate. Applying a Laplacian to a norm-convergent
   first-order series is not a uniform estimate.
3. **Use holomorphy or a finite-lattice elliptic bound.** Cauchy in the
   datum bounds a derivative only in a norm already bounded on its
   circle. It cannot create a mesh-free graph bound. This can be seen
   from \(a_n(k)=n^{-1}(-1)^k\) on an even periodic mesh \(\eta=1/n\),
   at scale one: \(|a_n|=1/n,\ |\nabla a_n|=2,\ |\Delta a_n|=4n\).
   The entire map \(u\mapsto u a_n\) has a uniform first-order bound
   on a fixed disc and no uniform graph bound. This is a diagnostic
   about the proposed inference, not a counterexample to the actual
   completion kernels.

There is also a useful necessary test. Differentiating (S5) at zero,
\[
 D_jA'(0)=-T,\qquad D_bA'(0)=TH_0,\qquad DX(0)=0.          \tag{4.11}
\]
Thus actual (N1) must at least bound \(T:E^\Delta_p\to E^\Delta_p\)
and \(TH_0:B_p\to E^\Delta_p\), uniformly at switches. This isolates
a linear obstruction to any claimed proof; it does not assert failure
of those actual operators.

**Disposition of the requested full (N1).** Equations (4.1)–(4.4) prove
the reduction and all four entries under explicit primitive bounds.
The unswitched route (4.8)–(4.10) is available under bare graph inputs.
GW, the weighted density/pointwise inputs on actual completion domains,
and the switched identification/bound of \(m_H\) have not been supplied.
Full actual-kernel (N1) is therefore not discharged. B4 is not an open
obligation and must not be reinstated.

## 5. Current rider and the completed cutoff step

This section incorporates layer-thm.md (R1)–(R17) with the gate's repairs.
It is a direct implication for a furnished triple and local coefficients.
It neither assumes nor proves that a cut triple solves a new layer equation.

Put \(P_1=D_0(I-R)D_0^T\) at switches one, with its specified switched
continuation, and
\[
 K_W=D_1^TD_1+D_0D_0^T-\Delta_W .
\]
Take the specified \(m_H(\sigma)\) and curvature remainder \(F\), with
\(F(W,0)=0\). Define
\[
 J^\sharp[1]=(\Delta_W-P_1+K_W)A'-m_HX+F(W,\mathbb H),       \tag{5.1}
\]
\[
 J^\sharp[\chi]=(\Delta_W-P_1+K_W)(\chi A')-\chi m_HX
       -[D_1^TD_1,\chi]HX+F(W,\chi\mathbb H).                \tag{5.2}
\]
These are the account's current-rider formulas, I 111397–111406,
111538–111545. They are definitions at independent currents. Under PH,
(5.1) has the physical interpretation of I 15669–15701.

### 5.1 The uncut estimate

Use the explicitly local premises, I 94996–95013, 111446–111460,
\[
 \ell_y^3|K_WB|_y\le18d\,\mathsf p(W)\ell_y|B|_y,\qquad
 \ell_y^3|F(W,h)|_y\le
 K_J(\mathsf p(W)+\Theta_0+\Theta_1)(\Theta_0+\Theta_1),
 \quad\Theta_0+\Theta_1\le2N_y(h),                           \tag{R}
\]
on the analytic stencil ball \(N_y(h)\le1/20\), with \(\mathsf p(W)\le1\).
They are named uniform coefficient inputs on new complex domains.
For \(N_y(h_i)\le1/40\), set \(D=N_y(h_1-h_2)\).
If \(D=0\), locality gives zero remainder difference. Otherwise the
disc \(h_2+z(h_1-h_2)\), \(|z|\le1/(40D)\), lies in the \(1/20\) ball.
(R) bounds its remainder by \(0.11K_J\) in scaled units and its
difference from the centre by \(0.22K_J\).
If the radius is at least one, divide by \(z\) and use the maximum
principle to bound the difference at one by \(8.8K_JD\).
If the radius is smaller, the endpoint bound gives the same inequality.
Thus the difference costs at most \(9K_JD\).

Subtracting (5.1), the linear terms cost \(1+1+18d+1\) times the maximum
of the four (N1) entries. In the \(K_W\) term use
\(N_y(\delta A')\le N_y^\Delta(\delta A')\), not the printed
unsupported replacement by \(N_y(\delta\mathbb H)\). Therefore
\[
 \ell_y^3|\delta J^\sharp[1]|_y\le
 K_{\mathsf j}\max\{N_y^\Delta(\delta A'),N_y(\delta\mathbb H),
 \ell_y^3|P_1\delta A'|_y,\ell_y^3|m_H\delta X|_y\},
 \quad K_{\mathsf j}=3+18d+9K_J .                          \tag{5.3}
\]
Together with (N1) this is the weighted datum-Lipschitz rider.
For size relative to zero one may retain the smaller direct remainder
constant from (R); (5.3) is a common valid choice.

### 5.2 The commutator count

Let \(T_\mu\) be covariant forward translation and
\(\nabla_\mu=(T_\mu-I)/\eta\),
\(\nabla_\mu^T=(T_\mu^{-1}-I)/\eta\).
The transpose formula holds for complex links because the trace pairing
is Ad-invariant. Let \(f_\alpha=\partial_\alpha\chi\) and
\(g_\mu=\partial^-_\mu\chi\), using ordinary scalar differences.
Exact multiplication gives
\[
 [\nabla_\mu^T\nabla_\alpha,\chi]B
 =f_\alpha\nabla_\mu^TT_\alpha B
 -(\partial^-_\mu f_\alpha)T_\mu^{-1}T_\alpha B
 -g_\mu T_\mu^{-1}\nabla_\alpha B .                        \tag{5.4}
\]
No derivative of a link is introduced. Use
\[
 \nabla_\mu^TT_\mu=-\nabla_\mu,\qquad
 \nabla_\mu^TT_\nu
   =T_\mu^{-1}\nabla_\nu+\nabla_\mu^T-\nabla_\nu.            \tag{5.5}
\]
For the \(\nu\)-component of curl-transpose-curl, sum
\(\nabla_\mu^T\nabla_\mu B_\nu-\nabla_\mu^T\nabla_\nu B_\mu\)
over \(\mu\ne\nu\). If each elementary transport has norm at most
\(\vartheta\le5/4\), the gradient coefficient per \(\mu\ne\nu\) is
\((1+\vartheta)+(1+3\vartheta)=2+4\vartheta\);
the value coefficient is \(1+\vartheta^2\le2+4\vartheta\).
All terms are on the full stencil. For scalar first- and second-difference
bounds \(s_1,s_2\),
\[
 \ell_y^3|[D_1^TD_1,\chi]B|_y
 \le c_d(\ell_ys_1+\ell_y^2s_2)N_y(B),\qquad
 c_d=(2+4\vartheta)(d-1).                                 \tag{5.6}
\]
This is the step marked (*) in I 111614–111626.

### 5.3 The replacement cutoff and the unchanged constant

The printed \(C^2\) cutoff, one on \([-1/3,1/3]\), zero outside
\((-2/3,2/3)\), with \(|\zeta''|\le5\), does not exist.
Its derivatives vanish at the transition endpoints. Integrating
\(|\zeta'(x)|\le5\min(x-1/3,2/3-x)\) permits a drop at most \(5/36<1\).
This already checked defect is retained.

Here is the existing explicit repair, restated in full. On \([0,1]\)
let \(v_0\) rise linearly from \(0\) to \(3/2\) with slope \(9/2\)
on the first third, be \(3/2\) on the middle third, and fall with slope
\(-9/2\) on the last third; extend by zero. Its integral is one.
Let \(\epsilon_0=1/200\), \(c_0=99/100\), and
\[
 v_{\epsilon_0}(u)=c_0^{-1}v_0((u-\epsilon_0)/c_0),\quad
 k_{\epsilon_0}(u)=(\epsilon_0-|u|)_+/\epsilon_0^2,\quad
 v=v_{\epsilon_0}*k_{\epsilon_0}.
 \tag{5.7}
\]
Both factors have integral one. \(v\) is supported on \([0,1]\),
is \(C^2\), and
\(\|v\|_\infty\le50/33\), \(\|v'\|_\infty\le45000/9801\).
For \(C^2\), the distributional second derivative of the trapezoid is
a finite sum of point masses; convolution makes it a finite sum of
translates of the continuous triangle. Define
\[
 q(u)=1-\int_{-\infty}^u v(s)\,ds,\qquad
 \zeta(x)=q(3|x|-1).
 \tag{5.8}
\]
It is constant near \(x=0\), hence smooth across the absolute value
there. It has the required plateau/support, \(0\le\zeta\le1\),
\(|\zeta'|\le50/11<5\), \(|\zeta''|<42\).
For its tensor-product bump, mixed second partials are less than \(25\).
Ordinary finite differences obey the same derivative bounds by integration.

Use \(\chi=t+\tau\widehat\chi_\square\), \(0\le t\le1\), with the
bump scaled by \(M\ell_\square\). Then
\[
 s_1\le5|\tau|/(M\ell_\square),\qquad
 s_2\le42|\tau|/(M\ell_\square)^2 .
\]
The collar geometry gives \(\ell_y\le L\ell_\square\) whenever the
commutator stencil meets the bump. With \(M\ge2L^2,L\ge3\),
\[
 \ell_ys_1+\ell_y^2s_2
 \le|\tau|\{5/(2L)+42/(4L^2)\}\le2|\tau|.
\]
Outside those stencils the commutator vanishes. Therefore
\(c_\zeta=2c_d\), exactly the consumer's constant, survives the repair.

Assume \(N_y(\chi\mathbb H)\le1/40\). The four noncommutator terms
of (5.2) are bounded by \(K_{\mathsf j}\) times
\[
 N_y^\Delta(\chi A'),\quad N_y(\chi\mathbb H),\quad
 \ell_y^3|P_1(\chi A')|_y,\quad\ell_y^3|\chi m_HX|_y .
\]
Use (5.6) on the remaining term with \(B=HX\). This proves
\[
 \ell_y^3|J^\sharp[\chi]|_y\le(K_{\mathsf j}+c_\zeta)
 \max\left\{\text{those four entries},
 |\tau|N_y(HX)\mathbf1[\widetilde\Delta(y)\cap\square\ne\varnothing]\right\}.
                                                               \tag{5.9}
\]
No \(\Delta_W\mathbb H\) estimate has been used. Thus the repaired U14
step is complete as an implication from the furnished triple, (R),
the stated transport/collar bounds and smallness. U15 uses only (3.3)
and its own assumed size bound (e2), and is covered without (N1).

The all-block dilation U27 uses instead
\((e^{i\eta\chi\mathbb H}W,J+\chi J^\sharp[1])\).
Its second slot is a local product; it is not (5.2).
The proof at II 13888–14105 explicitly uses this distinction.
Its bump/room/entry and space-identification premises remain attached.

## 6. The open item (3) on \(\mathfrak B^0,\mathfrak B^C\)

The two sets are the minimal \(\mathbb B_k(C)\) and two-level
\(\mathbf B''_k(C)\). I 94763–94843 verifies localization provisos and
conditions (c1)–(c3): nesting, own-scale fine-cube structure and widths;
refinement/agreement off the collar; and the host-cube condition at
\(\sigma=1\). It then explicitly invokes the small-solution hypothesis.
It is not a proof of (3).

**What transports.** Suppose the literal local operators at either set
have Loc[U], Avg[U], the native vector/Hölder/transpose and summability
bounds, and their coefficient reads are those of (1.4)–(1.5).
The algebraic proofs of (3) and §4 use only these constants, not the
name of the set, its age or number of components. With common constants,
(3.1) supplies exactly the same radii at both sets. This is a valid
localization implication, including parameter families with uniform
operator bounds. It does not extend a solution across an unverified
boundary read.

Three direct attempts to verify its hypotheses have distinct failures.

1. **Use (c1)–(c3) as the PI certificate.** Their own-scale width lower
   bound is not PI's assertion that every \(N(x)\) lies in one supplied
   small gauge, including the exterior Hessian read. A fixed-side
   \(12M_b\) cube test cannot be made into that assertion merely by
   making its own \(M_b\) larger. If one proves the *additional* aligned
   thick-cell condition at the same \(M_b\), Proposition 3.1 supplies
   interior points. Boundary points still require Loc[U].
2. **Restrict a parent inverse or a parent gauge.** A compressed inverse
   is generally not the inverse of the compressed operator:
   block elimination introduces the exterior Schur term
   \(A_{12}A_{22}^{-1}A_{21}\). A parent gauge helps only if it is supplied
   on the entire local read with the required scaled bounds and compatible
   boundary data. Neither follows from refinement alone. The exact
   required identity is equality of the localized rows, boundary
   coefficients and inversion problem, not only equality on an interior
   core.
3. **Invoke the localized \(\mathfrak K_{109}\) label.** Its explicit
   definition at I 94448–94456 gives (3.35), (3.37), current size.
   The B98 fixed-side cube example prevents inferring its needed
   carrier bound from that alone. Add PL with its numerical ceiling,
   a verified TH carrier cube, or a supplied frame. Even then the
   exterior PI gauge and the other operator estimates still have to hold.

Consequently (3) on the full localized domain printed in the account
is not established. This is a missing-domain implication, not a
counterexample to the particular physical local minimizers.
The exact local certificate consists of: literal boundary/rows;
Loc[U]; Avg[U] and AV; native vector and transpose bounds; the resulting
seven-term quadratic bound on a common larger ball. GW is additional
when full (N1) is requested.

For U07 one can obtain more without reinstating B4. At zero block datum
\(DX=0\), so
\[
 \mathsf T^{\mathsf L}a=(I+G(1)\Theta_J)H_0a.
 \tag{6.1}
\]
Equations (4.8)–(4.9) and the bare graph bound for \(H_0\) give
\[
 \|\mathsf T^{\mathsf L}a\|^\Delta
 \le[h_\Delta+b_\Delta(1+2b\theta)\theta h_0]|a|.
 \tag{6.2}
\]
It is holomorphic on the admitted local domain. The covariance/reality
and physical differential identification follow from (c),(d).
The alternative \(\mathsf T^\sharp=H^J\) does not inherit (6.2).
This is the already checked U07 repair, with its propagator premises
explicit.

## 7. The open item: every general-field use and the (S5) convention

The existence of an independent current \(J\) in the base does not supply
a field-source slot \(j\). There are two separate questions: which field
is the first datum, and which forcing does that datum produce?

### 7.1 The exact unswitched conversion

At switches one, \(G=(I-B_0\Theta_J)^{-1}B_0\), so
\(T=(I-B_0\Theta_J)^{-1}\). Multiply (S5) by \(I-B_0\Theta_J\):
\[
 z=-j+B_0\{\Theta_JA'-V'(A')\}.                           \tag{7.1}
\]
Thus a source equation with the term \(-B_0f\) is exactly (S5) with
\(j=B_0f\). The sign is fixed by this computation. In addition to this
algebra, a quantitative application needs
\[
 \|B_0f\|^\Delta_p\le K_\#|f|_{-3,p},
 \tag{FD}
\]
and the appropriate component support. The bare unswitched graph route
of §4.3 supplies (FD) under its bare inputs.
An arbitrary field \(j\) need not have \(Qj=0\). Consequently a physical
constraint or a Landau identity derived from \(QB_0=0\) cannot be
asserted for all fields merely because (S5) is defined there.

At switches the algebraic substitution \(j=B_0(\sigma)f\) defines
a solution of (S5) with forcing
\[
 -[I+G(\sigma)\Theta_J(\sigma)]B_0(\sigma)f .              \tag{7.2}
\]
The account's use of a name such as \(\widetilde G_0(\sigma)f\) for a
datum identifies that datum; it does not prove that its source-driven
critical equation has the forcing (7.2).
The needed **FM** identity is equality of these forcings, operators,
nonlinear conventions and branches with those of the actual layer.

### 7.2 Why switching does not commute with the conversion

At I 15265–15412 a concatenated primitive word is tagged by the union
of its visited cubes, each once. Multiplying already switched sums can
repeat a cube's factor. This distinction can be checked without any run.

Consider scalar formal words \(B=\beta>0\), \(\Theta=\theta\),
\(0<\beta\theta<1\), all visiting one cube. Tagging each whole resolvent
word once gives
\[
 B_\sigma=\sigma\beta,\qquad
 G_\sigma=\sigma\sum_{n\ge0}\beta^{n+1}\theta^n
          =\frac{\sigma\beta}{1-\beta\theta}.
\]
If the local insertion is left untagged,
\[
 (1+G_\sigma\theta)B_\sigma-G_\sigma
   =\frac{\sigma(\sigma-1)\beta^2\theta}{1-\beta\theta}.
 \tag{7.3}
\]
If the insertion itself carries one factor \(\sigma\), the numerator
is instead \(\sigma(\sigma^2-1)\beta^2\theta\). Both differ from zero
at general switches. This is an exact example in the tagged-word
algebra, not a counterexample claiming these are the Yang–Mills kernels.
It refutes the proposed formal inference from an unswitched resolvent
identity to the same identity between switched products.

Two further possible conversions also need missing information.
One can *define* a new datum \(j=T_\sigma^{-1}f_\sigma\), but first must
prove invertibility and graph-norm/support bounds of \(T_\sigma^{-1}\),
and that this is the datum prescribed by the consumer. It cannot replace
the given datum without proof. Or one can compare the two equations at
the physical diagonal; equality there does not extend to independent
\(J\), since a holomorphic factor \(J-\mathcal J(W)\) vanishes on that
graph but need not vanish elsewhere. This is the already established
two-system obstruction, not a new no-go assertion about FM.

### 7.3 Use-by-use datum reconciliation

This table accounts for every source-bearing use and for the uses that
only inherit such a call. “Formal” means a valid substitution into (S5);
it does not assert identification with the account's unstated general map.

| Uses | Datum actually read | Conversion and exact remainder |
|---|---|---|
| U01 | General \(d=(j,b)\), with \(j=\widetilde G_0(s)f\) in the field-source corollary, I 72373–72538 | Formal substitution is (7.2); at one (7.1) proves the forcing conversion. At switches need FM, FD and the component support of the actual field operator. |
| U02 | Stage 3 has \(j_3=\widetilde G_0(\sigma)J_3\), I 73103–73140; the other links use their specified data | Same conversion as U01. Regularity/size of every intermediate pair is separately an induction hypothesis. |
| U03 | The four links at \(\mathbf B''_k,\mathbf B''_k,\mathbf B_1,\mathbf B_k\), independent switch families | Inherits U02's stage-3 FM/FD. Joint holomorphy follows only on the true product domains; replacing a global determining set by a local scaffold does not supply it. |
| U04 | General source-presentation layer, I 89955–90008 | Its supplied layer theorem/rider are antecedents. Needs the defining first-slot map and FM/FD, not only the source-variable holomorphy label. |
| U14–U18 | Furnished triples, arbitrary differences at U16, and the source-bearing healing links at U17 | U14/U15 are formulas on a furnished triple, with no new first slot. U16 uses two fields with norm (1.3). U17/U18 inherit the actual link's FM/FD; cutting \(\mathbb H\) does not introduce a new layer datum. |
| U20, U23, U25, U26, U29, U30, U34 | Constants, component identities or current formulas for previously supplied layers | They inherit FM/FD when the underlying link is stage 3. For U23/U25/U34 the field forcing must vanish on the claimed no-data component, full stencils included. A bounded arbitrary current extension does not by itself prove this. |
| Completion calls underlying U26 | I 92560–92588: \(f_1=G''(\sigma)J^c+[G''(\sigma)-G''(1)]Q''^*\mu\); I 142530–142543 uses \(\widetilde G_0(\sigma_3)J_3\) | The first expression is explicitly a decaying, noncompactly supported field. To identify the notation with \(B_0(\sigma)\), need literal operators, tags and boundaries. The pointwise decay quoted there is not its graph norm. FD for the difference operator and FM remain. |
| U05–U13, U19, U21, U22, U24, U27, U28, U31, U32 | The specified calls have \(j=0\), or are domains/constants/derivatives of those calls | No new field-slot conversion. Use the actual block chart, with local-domain and primitive hypotheses. U31's \(b=\mathsf B(t,\mathsf t)\) must stay in the datum ball for the whole interpolation domain. |
| U33 | Comparison of already constructed responses at different bases/frames | A same-datum conversion is insufficient; identify the response with the constrained critical-point map of §9 on its full domain. |

There is a further source limitation already identified in ca-f.md:
the quoted CMP 99b Theorem 3.13 excludes its covariant-Laplacian member.
Thus replacing \(G''\) by an unspecified “propagator of that type” does
not prove FD. I 142537 explicitly assumes the graph estimate needed by
this application; it is not a derivation of it.

**Disposition.** Unswitched source forcing is converted by (7.1) on
its matched domain. Every block-only call uses the existing chart.
The general-field calls are reconciled as above but their switched FM/FD
and actual-kernel identification remain unproved. No value-decay bound
has been promoted to a datum graph bound.

## 8. The open item: clause (e)

I 72392–72399 assumes clauses (a)–(f); I 94839–94841 mentions (e) only
as a side clause. layer-find.md's full-text locating work found no
statement of its content. There is no independent conclusion in U01–U34
from which to recover it.

Three interpretations were examined. Taking the fifth clause of the
ten-clause chart would import unrelated numbering. Treating (e) as
physical identification duplicates (d) without source evidence. Treating
it as holomorphic specialization gives exactly §3.2(e), already proved
by composition and uniqueness. Only this last **proposed convention**
adds no unsupported mathematical claim.

It cannot establish that all of the unknown original (e) is supplied.
U08's main (a),(b) use can be covered conditionally without inventing
(e); its assertion that every side clause is available cannot. This is
an underdetermined statement, not a false mathematical theorem.

## 9. The open item U33: comparison across kernels and bases

### 9.1 A later supplier is already present

U33, II 52390–52492, requests a bound linear in the inherited discrepancy,
at profile
\[
 p(x)=\sup|b|\,e^{-(5/2)\delta_1d^\wedge(x,\mathcal C_j)},
 \qquad\delta=4\delta_1,
 \tag{9.1}
\]
on the full interpolation discs. It describes six residuals, with two
profile smears and a fifth residual also smearing the discrepancy.
It expressly leaves the requisite reweighting proof outstanding.

The later account already contains a conditional answer to the
**reweighting** problem:

* Weighted calculus, II 54662–54770: weights through rate \(6\delta_1\),
  from the quoted local \(8\delta_1\) kernels and scale/summability floors.
* Projection Lipschitz and nesting statements, beginning II 55584 and
  55765; these retain their algebraic and averaging hypotheses.
* Theorem 5.8:thm-response-comparison, II 55882–56284: for exactly paired
  sets, real reference backgrounds \(U',U,W=M(U')\), complex data and
  source vectors, profiles \(p\in\mathfrak M_\rho\),
  \(M\in\mathfrak M_\tau^A\), \(p_\delta\in\mathfrak M_{\rho+\tau}\),
  \(\rho+\tau\le5\delta_1\), and its smallness/local comparison inputs,
  \[
  |Y[X';U']-X|_x\le C_B^\sharp\{A p(x)M(x)+p_\delta(x)\}.
  \tag{9.2}
  \]
  Its proof displays and bounds all six residuals. The residual identity,
  extension/transfer, divergence/constraint and local action comparisons,
  and their complex-data validity are **assumed** in the theorem.
* Lemma 5.8:lem-energy-difference, II 57711–57865, and Corollary
  5.8:cor-three-member, II 58123–58205: the full-disc, linear comparison
  on the stated real presented or diagonal-entry family, with healing,
  hybrid gauge, entry, covariance, local-majorant and radius hypotheses.
  The response is explicitly Balaban's constrained critical-point/Landau
  function, not an unspecified representation formula.

I stop the attempted reconstruction of those six estimates here and reuse
this supplier. It is already present; doing it again would violate the
prior-work instruction. Its conditional scope is what matters.

For the rates of U33, take \(\rho=(5/2)\delta_1,\tau=\delta_1\).
Then \(\rho+\tau=(7/2)\delta_1<5\delta_1\). The factor \(L\) in
\(\Psi(y)\le L e^{\delta_1d(x,y)}\Psi(x)\) is handled by the theorem's
\(\mathfrak M_\tau^A\) hull, with \(A=L\), rather than silently replacing
it by the narrower slowness convention. Supremum smallness, mismatch
majorization and the full-domain inclusion remain hypotheses.

The rate arithmetic in U33 is valid. Once the required densities are
available,
\[
 \sum_y e^{-4\delta_1d(x,y)}|a|_yp(y)
 \le p(x)\sum_y e^{-(3/2)\delta_1d(x,y)}|a|_y .
 \tag{9.3}
\]
Triangle inequality and summability at \(\delta_1/2\) give
\[
 \sum_xe^{-(3/2)\delta_1[d(x_0,x)+d(x,y)]}
 \le c_1^b e^{-\delta_1d(x_0,y)}.                          \tag{9.4}
\]
Thus \(4\delta_1=(5/2)\delta_1+\delta_1+\delta_1/2\).
This is the existing rate budget, not proof of the residual hypotheses.

### 9.2 What must match to use it for (S5)

Define **RC** to be the following finite list at the actual U33 pair:

1. Identify both (S5) responses, their independent source vectors and
   logarithm/gauge representatives with the constrained critical-point
   functions \(X,X'\) in (9.2), on the entire data and interpolation
   domains. Match the cross-grid map \(Y\), boundaries and frames.
2. Supply exact pairing, healing and the real reference backgrounds of
   that theorem. Complex data at fixed real references are allowed;
   arbitrary complex backgrounds without such a representation are not
   included merely by holomorphy.
3. Supply the six-residual identity and local comparison hypotheses,
   including the projection and gauge-component estimates at the product
   weights and the discrepancy majorant. The \(C^{1,\beta}\) and multiplier
   sizes used here need their native bounds; the four-entry (N1) alone
   does not define a Hölder estimate or a multiplier.
4. Supply the hybrid/entry mismatch bounds and common radii on the full
   discs. For nontrivial switches, supply the switched comparison of
   the prescribed words: the energy-difference lemma just cited fixes
   \(\sigma=1\).

Under RC, use (9.2) and the existing three-member corollary; their
linear mismatch factors and (9.3)–(9.4) give U33's requested profile
without a fractional power. This is a conditional coverage statement.
It is not new closure of U33 on the general completion family.

### 9.3 Why the other proposed routes do not fill RC

**Same-kernel Lipschitz.** Write the two outer equations, after a
specified common-space transport, as
\(A_i=F_i-G_iV_i(A_i)\), \(F_i=T_i(-j_i+H_{0,i}b_i)\).
Their exact difference is
\[
 \delta A=R_A-G_1[V_1(A_1)-V_1(A_2)],
\quad
 R_A=F_1-F_2-(G_1-G_2)V_2(A_2)
                 -G_1[V_1(A_2)-V_2(A_2)] .               \tag{9.5}
\]
If the first family contracts in a common weighted norm with factor
\(\nu<1\), then \(\|\delta A\|_p\le(1-\nu)^{-1}\|R_A\|_p\).
This elementary proof follows by taking norms in (9.5).
The inner equation has, in addition, the residual
\[
 R_X=C_1(S_1(A_2-H_1X_2))-C_2(S_2(A_2-H_2X_2)).
 \tag{9.6}
\]
It yields
\(|\delta X|_p\le2(|R_X|_p+c_wr\|\delta A\|_p)\) under the
same inner smallness. The response difference then includes
\((H_1-H_2)X_2\). Graph norms also require a comparison of the two
covariant Laplacians. None of these kernel/base residuals is a
datum difference at a fixed kernel. (N1) gives no bound for them.
For nonlinear cross-grid \(Y\), (9.5) itself is replaced by its transported
residual, so it cannot be used without the RC identities.

**Interpolation.** The source already explains that a fractional power
of \(\mathsf T_p\) is unusable in the recursion. For \(0<\alpha<1\),
\(C x^\alpha/x=Cx^{\alpha-1}\) diverges at zero. An absolute analytic
bound and real-slice smallness do not provide the required relative
linear factor on the full complex disc.

**Analytic continuation of a physical equality.** Physical diagonal
matching proves neither equality at independent currents nor the
quantitative comparison of distinct kernels. Even with a fixed real
reference, one must identify the source vectors and local action; a
label saying “response” does not establish that identity.

**Disposition.** The profile-reweighting part has an existing conditional
supplier and is not redone. RC is the exact remaining bridge. U33 at
arbitrary actual completion kernels and full switches is not covered.
The global stage-response-identification component is separately owned
by shift-map and is retained as an input, not reassigned here.

## 10. Recovery point and consumer coverage

The current proof state is:

* Proved here as deductions: the single conditional theorem, its four-entry
  constants (4.1)–(4.4), the unswitched graph reduction, the exact
  unswitched field conversion, and the conditional residual comparison
  identity. The contraction/cutoff proofs reproduce already checked work.
* Reused without reopening: failure of B4; the PI and B98 carrier results;
  U07's linearized repair; the later §5.8 conditional comparison.
* Not established on the actual full consumer family: the primitive
  domain certificates, endpoint graph-walk bounds GW, the actual switched
  \(m_H\) identification, FM/FD, the original meaning of (e), and RC.
  None is replaced by a run, an audit status or a physical-diagonal argument.

There is a precise optional strengthening of the cited J8 input.
I 13787–13798 says its walks have bounds in the norms listed in J2;
J2 reserves the Laplacian member for the bare \(G_0,H_0\).
If this is supplied as an **absolute weighted endpoint-word graph
majorant**, including the cutoff coefficients, call it \(BW_\Delta\).
Then §4.4 route 2, (2.2) and (4.5) supply GW. This is the exact useful
reading to verify; it does not demand a graph bound for \(G_\pi^J\).
PI alone does not establish \(BW_\Delta\), and the quoted global statement
does not verify it on the localized/completion domains. There is no
remaining nonlinear mystery once these primitive bounds and identities
are actually supplied.

For recovery, preserve the pinned sources above and this file. The next
scientific decisions are whether the native vector walks supply
\(BW_\Delta\) on the required domains, whether those domains admit the
literal local models and averaging carriers, and whether the actual
source conventions satisfy FM and RC. The separate planned distillation
and referee should preserve these qualifications. No queue, registry,
audit result, editable prompt or platform instruction was changed.

The table concerns the **layer content actually consumed** at each U,
not every other antecedent of the surrounding theorem.
Abbreviations:

* **E[U]**: actual operators/equations on U's full domain satisfy (3),
  with Loc[U], Avg[U], AV and the remaining native vector/transpose
  inputs; hence (a). It includes any required admission of intermediate
  bases and datum radii.
* **N[U]**: the actual weighted primitive bounds (W), including GW and
  the \(P_1,m_H\) identification, at every admitted weight; hence (N1).
* **R[U]**: the local coefficient conditions (R), transport bounds and
  required smallness; for cut currents also the collar geometry and
  the repaired cutoff.
* **PL109**: membership in \(\mathfrak S^{\rm pl}\) follows from the
  expressly invoked full CMP 109 (i)–(iii) representative and inclusion
  ceilings. It does not prove that every reached pair is a member.
* **PL?**: the cited use does not establish PL or a complete alternative
  carrier/frame certificate. Avg[U] remains.

Each Loc[U] below has the explicit supplier rule of §2.1: Proposition 3.1
only at verified thick interior points; otherwise the named local-gauge
obligation, including the boundary. It is not implicit in PL109.

| Use and source | Disposition of the layer use | PI / averaging admission |
|---|---|---|
| U01 — I 72373–72538 | **Not covered in full.** Conditional (a),(b),(f), corollary and rider require E[U01], N[U01], R[U01], LC, FM/FD; (d) requires PH. The asserted whole (a)–(f) package still lacks the original (e). | Loc[U01]; Avg[U01], PL? on its actual exempted-family base. Restrictions must preserve full reads. |
| U02 — I 73103–73140 | **Covered conditionally:** E[U02], N[U02], R[U02], LC and the induction's domain/size hypotheses. Stage 3 additionally requires FM/FD for its explicit \(\widetilde G_0(\sigma)J_3\). | Loc[U02] for each of four sets. PL109 follows under the induction's full membership hypothesis; actual admission and Avg[U02]'s complex radius remain. |
| U03 — I 73546–73633 | **Covered conditionally** by (a) and parameterized form on E[U03], with the inherited FM/FD and every intermediate image admitted on the full product switch polydisc. No change to the global determining sets. | Loc[U03] and Avg[U03] at each true global set/base; inherited CMP 109 membership must be supplied, not inferred from the local scaffold. |
| U04 — I 89955–90008 | **Covered conditionally:** E[U04], N[U04], R[U04], LC and the source convention FM/FD. Its presentation statement assumes these inputs. | Loc[U04], Avg[U04], PL? for the actual source-presentation family. |
| U05 — I 94180–94286 | **Covered conditionally** as a radius choice after E[U05], N[U05] and the explicitly required real-base/perturbed-base admissions. A free constant is fixed before the final coupling ceiling; small coupling alone does not establish operator admission. | Loc[U05] at both local sets; Avg[U05], PL?; the isolated \(\mathsf p\le1\) requirement is not PL's small ceiling. |
| U06 — I 94303–94422 | **Covered conditionally** by (a) for the two \(j=0\) block calls, E[U06], and their whole bidisc's datum/base admission. Zero at zero follows without a physical identification. | Loc[U06] at \(\mathfrak B^0,\mathfrak B^C\); Avg[U06], PL?. |
| U07 — I 94448–94586 | **Covered conditionally for \(\mathsf T^{\mathsf L}\):** E[U07], the bare unswitched graph inputs and (6.1)–(6.2); PH for physical identification. The alternate \(\mathsf T^\sharp\) is not given a graph bound by this argument. | Loc[U07], Avg[U07], PL?; its explicit three-clause localized class is insufficient. |
| U08 — I 94608–94842 | **Not covered as the full claimed scope.** The main uses follow conditionally from E[U08], N[U08], R[U08], EQ/PH and parameterization. Geometry (c1)–(c3) does not prove those inputs; the original side clause (e) is unspecified. | Loc[U08] and Avg[U08] at both localized sets; PL?. |
| U09 — I 94846–95085 | **Covered conditionally in the repaired consumed norms:** E[U09], N[U09], R[U09], and whole-bidisc admission. Use \(N(\mathbb H)\) and the four current entries, not the stronger printed \(N^\Delta(\mathbb H)\) shorthand. | Loc[U09], Avg[U09], PL? throughout both constructed block-data families. |
| U10 — I 95682–95700 | **Covered conditionally** by (a),(c): E[U10] and conjugation preserving the real-data equations/domain. Reality of the derivative follows. No arbitrary complex-gauge invariance of the ball is needed. | Loc[U10], Avg[U10], PL? inherited from the local chart. |
| U11 — I 95750–95790 | **Covered conditionally** by (c),(d), E[U11], PH and the physical free-current identity in its matched gauge; then differentiate the block datum. | Loc[U11], Avg[U11], PL? on the shifted local physical chart. |
| U12 — I 95872–95908 | **Covered conditionally** by EQ and the admitted physical/holomorphic overlap. The \(\mathsf T^\sharp\) alternative remains a different form with its extra source conditions; it is not identified with the \(\mathsf T^{\mathsf L}\) form. | Reuse Loc[U12], Avg[U12] of that local chart; PL?. |
| U13 — I 99780–99796, 99878–99892 | **Covered conditionally** as a fixed-order choice of constants after the common local certificates E[U13], N[U13], R[U13]. These certificates, not the words “four floors,” supply the needed uniformity. | Loc[U13], Avg[U13], PL? at the two localized sets. |
| U14 — I 111489–111716 | **Covered as a rider implication** by §5 from a furnished triple, R[U14] and the stated collar/smallness conditions. The impossible printed cutoff is replaced by (5.7)–(5.8), with unchanged \(c_\zeta\). | No fresh inverse is used in this implication. The furnished layer separately requires its Loc[U14]/Avg[U14]; PL is not asserted by the rider. |
| U15 — I 112180–112230 | **Covered:** (3.3), the seminorm definitions and the consumer's own (e2) suffice. Neither (N1) nor B4 is needed. | No new PI or B98 invocation. |
| U16 — I 112589–112610 | **Covered conditionally** by N[U16] at both stated exponential weights, with their class membership and (1.3) datum norm. The consumed four-entry size does not use the idle \(X\) norm or \(N^\Delta(\mathbb H)\). | Loc[U16], Avg[U16], PL? for every actual kernel whose datum differences are compared. |
| U17 — I 114790–114880 | **Covered conditionally** by E[U17], N[U17] at weight one, R[U17], inherited FM/FD and the separate amplitude/composition/admission assumptions of the healing presentation. | Loc[U17], Avg[U17]; the stated base membership must include a verified PL109 representative or a different carrier certificate. |
| U18 — I 115382–115405 | **Covered conditionally:** N[U18], R[U18], weight admission and the separately stated product-profile bound for the nonlocal \(P_1(\widehat\chi A')\) tail. That tail is not a direct consequence of (N1). | Loc[U18], Avg[U18], PL? at the underlying (T)/(L) layer kernels. |
| U19 — I 116555–116669 | **Covered conditionally:** E[U19], N[U19], R[U19] for \((0,b)\), the actual stage/chart identification, and all collar/switch radius ceilings. First-order chart size alone does not supply the \(A'\) graph entry. | Loc[U19]. PL109 under the stated full \(\mathfrak K_P\) membership; Avg[U19]'s complete carrier/complex-domain inclusion still must hold. |
| U20 — I 125775–125792 | **Covered conditionally:** N[U20] supplies a finite \(B_{\mathbb H}\) for the stated \(66B_{\mathbb H}K_{\rm cv}\). The other near-pair inputs are unchanged. | Inherited Loc[U20], Avg[U20] for the actual stage class; PL109 only under its full membership certificate. |
| U21 — I 131621–131695 | **Covered conditionally in the repaired norms:** E[U21], N[U21], R[U21], PH for the physical subcase. Also use the source's proposed normalization \(C_H^\sharp\mapsto\max(C_H^\sharp,1)\), or impose datum smallness explicitly; positivity alone does not discharge (*). | Loc[U21], Avg[U21]; PL? for the class obtained from the heredity input. Real criticality alone does not supply every omitted CMP 99b condition. |
| U22 — I 131725–131746 | **Covered conditionally** by E[U22], N[U22], PH and the same-constant certificate on the distinct localized \(\mathfrak B_Z\), including its whole holomorphy domain. A \(\mathfrak B^0,\mathfrak B^C\) scope check does not supply this. | Loc[U22], Avg[U22], PL? at \(\mathfrak B_Z\) and its ambient reads. |
| U23 — I 136750–136770 | **Covered conditionally** by (a),(f), E[U23], LC and field-slot support/FM where present. The freedom to choose a bounded independent second-slot extension is not a proof of first-slot zero. | Inherited Loc[U23], Avg[U23], PL?; component restriction includes all boundary stencils. |
| U24 — I 137562–137603 | **Covered conditionally** by E[U24], N[U24] at its exponential profile and the explicitly assumed localized input 10, including its shift-domain ceiling. | Loc[U24], Avg[U24], PL? at \(\mathfrak B_Z\); the source itself says this lies outside the earlier space geometry. |
| U25 — I 137978–138001 | **Covered conditionally** by (a),(f), E[U25], LC and the actual datum/support convention. The continuation gluing uses that identity; it does not prove it. | Loc[U25], Avg[U25], PL? inherited at the later operation and its full stencil. |
| U26 — I 138640–138667 | **Covered conditionally** by N[U26], R[U26], FM/FD for the actual completion operators, and the separate threshold/frame conversions. In particular I 142537's field graph bound remains an input. | Loc[U26], Avg[U26], PL? for actual completion kernels, including raw points and the separately treated core. |
| U27 — II 13888–14105 | **Covered conditionally** by E[U27], N[U27], the uncut R[U27], and all its named bump, room, entry and weighted-space hypotheses. Its local second slot is \(\chi J^\sharp[1]\), not \(J^\sharp[\chi]\). | Loc[U27], PL109 from the full stage membership, and Avg[U27]. The independent stage-family/space identification is retained. |
| U28 — II 15390–15404 | **Covered conditionally** as reuse of U27's admitted response data and the separate A-slot assumptions. No new layer construction is supplied here. | Reuse Loc[U28]/Avg[U28] from the same admitted stage calls; no new PL census is inferred. |
| U29 — II 20798–20808 | **Covered conditionally** by the furnished bracket layer and (5.2), its domain and locality hypotheses. Only the \(P_1\) term is nonlocal in the cut multiplier, as the source states. | Inherited Loc[U29], Avg[U29], PL? for each bracket; the current formula does not provide them. |
| U30 — II 23160–23177, 23990–24005 | **Covered conditionally** by the parameterized rider and the supplied layer/domain at each bracket, with R[U30] when an estimate is read. These appearances are not new existence theorems. | Inherited Loc[U30], Avg[U30], PL? for the actual bracket kernels. |
| U31 — II 51814–52070 | **Covered conditionally** by E[U31], the value part of N[U31], and the averaging map/radius bound keeping \(\mathsf B(t,\mathsf t)\) in the block-data ball on the full disc. Cross-construction estimates are separate. | Loc[U31], Avg[U31], PL? on both frames and for the nonlinear averaged datum. |
| U32 — II 52107–52186 | **Covered conditionally** by (a),(d), E[U32], PH, exact pairing and the source's refinement/relative-real-slice inputs. Continue within the paired critical family, not to independent currents. | Loc[U32], Avg[U32]; verify the physical/minimizer carrier certificate on the entire continued family, not only at its real centre. |
| U33 — II 52390–52492 | **Not covered on the full actual family.** The later §5.8 theorem already supplies the conditional profile comparison. RC is still needed: identity of responses/source vectors, paired domains, local residual inputs, full discs and any switched extension. (N1) alone cannot compare kernels or bases. | Loc[U33] and Avg[U33] for both frames, plus the relative theorem's native propagator and Hölder inputs; PL? for general rippled parents. |
| U34 — III 49210–49230, 49272–49288, 49454–49502 | **Not covered on the literal relaxed class.** Conditional (a),(f) would follow from E[U34], LC and its field-source support/FM, but its cube/twist continuation conditions do not supply the missing local/carrier certificate or boundary-crossing identity. | Loc[U34], Avg[U34], PL? at every earlier dated frame; the two quoted coarse conditions alone do not imply them. |
