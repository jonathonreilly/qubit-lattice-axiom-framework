# The general layer theorem: proposed statement and partial proof

Written 2026-11-07 by Codex gpt-6-astra on the laptop.
Checkout: `b7f96f2c2a6fe2efe8b43bb9b398870758f79b58`.
Research text. Not an audit. This note grants no status.

Credit: Tadeusz Balaban for the background and propagator constructions.
Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their
text, supply the complete account and outline used here.
All proof arguments below are mathematical. File searches and hashes supply no proof.

I, II, III denote the complete-account files under `/Users/jonreilly/ym4d-lead/sa`.
SA denotes `YM4_sketch_500.tex` there. Their supplied revision is `31a47c543775`.
The source hashes match `layer-find.md`'s identity table.
The directory's provenance is supplied, rather than verified through a local Git HEAD.

Sources read: GOAL; FINISH's published-work, efficiency and rules sections;
`layer-find.md`; the former `layer-thm.md`; registry rows LAYER-THM, CA-LAYER and CA-FIELD;
the outline-index README and relevant rows in chunks 05, 09–12 and obligations;
`lit-balaban.md:131–168`; `ca-f.md:54–63`;
I 12935–13035, 13546–13793, 13981–14652, 14992–15143,
15265–15445, 15669–15855, 72373–72538 and 94123–94422;
SA 5762–5803, 9693–9744, 10246–10254, 10354–10464 and 10562–10578.
The invocation passages read are recorded with U01–U34 in Result below.
The rider passages are I 111391–111716. Further bounded passages used below
are identified at the argument that uses them.
`library/prior/layer-thm.md` and `docs/ai_methodology/SCIENCE_WORKFLOW.md` are absent.

Ownership follows the user's rerun instruction. CA-LAYER/(N1) remains with stage-claude.
This lane addresses the remaining statement and proof, without changing any registry status.

## Statement

This section is a **proposed completion of the missing statement**. It is a
target, not a theorem established by writing its hypotheses. The proofs below
establish a local version and several uniform implications. They stop at one
specified uniform estimate after three attacks. In particular, the displayed
uniform theorem is not claimed proved.

I 72392–72399 says, “Assume the following statements, each as stated and proved
for the decoupling family of its own setting”. This separates the layer theorem
from the localisation and field-datum lemmas. The layer takes a field as input.
It need not prove that a particular propagator sends a current into its datum
space. That separate question belongs to CA-FIELD.

### Geometry, bases and data

Work on a finite lattice with the graded blocks and determining sets of the
account. A local norm at a cell reads the cell's stipulated enlarged stencil.
Write \(\ell_y\) for its scale. Use the account's covariant differences and
bilinear transposes, without replacing the latter by Hermitian adjoints.
SA 10251–10253 says that the covariant Laplacian on one-forms is
\(\Delta_W=\sum_\nu\nabla_\nu^T\nabla_\nu\), and that it “is not the
\(\Delta=\Delta^{\rm W}_U\)” of its Notation. We keep this distinction.
Write \(\mathscr L_W\) for the Wilson Hessian denoted by \(\Delta\) in
the chart's propagator equations, and
\(\mathscr C_W=\mathscr L_W-D_1^*D_1\) for their local curvature remainder.
Here \(D_0\) maps site fields to one-forms and \(D_1\) maps one-forms to
two-forms. A star means the bilinear transpose in both degrees.
For a fine one-form \(h\), put
\[
 N_y(h)=\max\{\ell_y|h|_y,\ell_y^2|\nabla_W h|_y\},\qquad
 N_y^\Delta(h)=\max\{N_y(h),\ell_y^3|\Delta_W h|_y\}.
 \tag{S1}
\]
The stencil maxima, including boundary extensions, are part of the datum of
the problem. No sharp multiplication of a field datum by a block indicator is
allowed without checking these norms.

Let \(p\) belong to the actual admitted class \(\mathcal M_\delta\).
Its slow-variation condition used below is
\[
 p(y)\leq e^{\delta d^\wedge(y,y')}p(y')\quad\hbox{for all }y,y'.
 \tag{S2}
\]
We do not enlarge that class by dropping any of its admission conditions. Set
\[
 \|h\|_p^\Delta=\sup_y N_y^\Delta(h)/p(y),\quad
 \|h\|_p=\sup_y N_y(h)/p(y),\quad
 |q|_{-3,p}=\sup_y\ell_y^3|q(y)|/p(y).
\]
For a dimensionless block field use \(|b|_p=\sup_y|b(y)|/p(y)\).
The datum is \(d=(j,b)\), with a **field** \(j\), a block field \(b\), and norm
\[
 \|d\|_{\mathrm{dat},p}=\|j\|_p^\Delta+|b|_p.
 \tag{S3}
\]
A convention using the maximum instead changes constants by at most two.
The smallness domain uses \(p=1\). Weighted estimates compare two members of
that domain; a large weight does not admit a large unweighted datum.

The base is the independent pair \((W,J)\) of K109, not necessarily
\((W,\mathcal J(W))\). I 12935–13035 explicitly removes the equations numbered
(3.36) and (3.38) from this class. In each required real-reference patch,
\(W=e^{i\eta a}U_r\), with the stated real regularity bounds \(a_0\),
\(N_{U_r}(a)<a_1\), and \(|J|_{-3}<a_\gamma\).
Keep all patch-overlap, logarithm and boundary conditions in that definition.
Use its fixed bounded gauge orbit, with adjoint bounds \(K=4\), only on
overlapping admitted patches. A complex gauge with no such bound is outside
the statement. For the specialised real domains of I 94123–94286, also impose
the stated real-base/core conditions and the membership of every perturbed
datum. Realness alone does not prove those conditions.

Allow the global determining sets used in U03. Allow the localised sets of
U06, U08, U21–U25 and U34 only with their three geometric conditions:
the stated nested layers and stratum/grade bounds; refinement and agreement
off the localisation layer; and host-cube compatibility of the switches.
The stipulated floors on the block sizes and localisation widths remain in
force. In particular, a proof on a global set does not silently prove the
same assertion on an arbitrary cut-out set.

The switches are the actual completion switches, with
\(|\sigma_\square|\leq e^{\kappa_1}\). Each primitive walk retains its domain
tag and its prescribed switch monomial. Products retain the tags of every
factor. An exempted family uses the same rule with the exempted switches set
to one. A wall decouples only when every tagged crossing is killed. Neither
an inverse identity nor a constraint identity valid at \(\sigma=1\) is
asserted after switching merely because the notation still resembles it.

### Defining equation

I 14376–14420 defines the chart by
\[
 z=\widetilde G_0\{\Theta_J(z+H_0b)-V'(z+H_0b)\}.
 \tag{S4}
\]
I 15311–15320 instead switches the equation after resolving its linear
part. Accordingly the following is the proposed general-field extension of
that convention. Write \(G=\widetilde G^{\,J}(\sigma)\),
\(H=H^J(\sigma)\), with the account's actual kernels, and set
\[
 T=I+G\Theta_J,\qquad
 z=-Tj+G\Theta_J H_0b-GV'_\sigma(z+H_0b).
 \tag{S5}
\]
All composites in this formula use their specified tags; it does not
resum a switched inverse. The triple is
\[
 A'=z+H_0b,\qquad
 X=C_\sigma(\ell A'-\ell HX),\qquad
 \mathbb H=A'-HX.                                      \tag{S6}
\]
Here \(C(0)=C'(0)=0\) is the nonlinear block constraint of the account.
\(V'_\sigma\) is its seven-term response nonlinearity from I 14156–14375,
with the same inner solution \(X\), base pair and tags. It has
\(V'_\sigma(0)=DV'_\sigma(0)=0\). This fixes the equation independently of
any downstream desired response or current.

There is a reason for \(Tj\), rather than \(j\), in (S5). At switches one,
\[
 G=(I-\widetilde G_0\Theta_J)^{-1}\widetilde G_0,\qquad
 T=(I-\widetilde G_0\Theta_J)^{-1}.
\]
Multiplication of (S5) by \(I-\widetilde G_0\Theta_J\) gives
\[
 z=-j+\widetilde G_0\{\Theta_J A'-V'(A')\}.               \tag{S7}
\]
Thus \(j=\widetilde G_0J_{\rm src}\) has the sign of an added source
in the critical equation. At general switches (S5) is a proposed definition,
not an identity deduced from (S7). The block-only case is the stated chart.
An invocation with a differently defined first argument must supply the
conversion to this convention. The cited texts do not identify that
conversion for every general-field invocation.

### The single admitted input

**CA-LAYER/(N1), admitted, owned by stage-claude.** For every actual admitted
kernel, determining set and switch family just described, every admitted
weight \(p\), and two admitted data whose furnished layer triples are
\((A'_i,X_i,\mathbb H_i)\), there is the stated common \(B_{\mathbb H}\) with
\[
 \max\!\left\{
 N_y^\Delta(A'_1-A'_2),\
 N_y(\mathbb H_1-\mathbb H_2),\
 \ell_y^3|P_1(\sigma)(A'_1-A'_2)|,\
 \ell_y^3|m_H(\sigma)(X_1-X_2)|
 \right\}
 \leq B_{\mathbb H}\|d_1-d_2\|_{\mathrm{dat},p}p(y).
 \tag{N1}
\]
The furnished datum at zero is the zero triple. This is the input as stated
in ca-f, section 3, with its general field/block datum and actual complex
kernels. It is used as a bound on furnished solutions. It does not create
solutions at unadmitted data, identify (S5) with a missing definition, or
assert a Laplacian bound for \(\mathbb H\).

### Proposed clauses, domains and corollaries

The uniform version asks for positive radii and constants depending on the
fixed structural parameters, including the allowed switch loss, but not on
the fine mesh, volume, determining set or admitted base pair. The datum
radius must fit the base and logarithm domains and the small inner and outer
balls. It must also fit the specialised ceiling used in U05:
\[
 K_{\rm nat}(\gamma_0+\varepsilon_3)\leq1,\qquad
 \varepsilon_\sharp=\varepsilon_3/(4K_\sharp).
 \tag{S8}
\]
These numerical ceilings are restrictions of a radius, not a way to prove
that a positive uniform radius exists.

* **(a) Existence and analytic dependence.** Equation (S5), with (S6), has
  the small solution for every datum in that domain. It is jointly
  holomorphic in the independent base, datum and switch parameters, and is
  zero at zero datum. Real inputs and real switches give real output.
* **(b) Full weighted comparison.** For two such data at the same kernel,
  the maximum of
  \[
  \|\delta A'\|^\Delta_p,\quad
  \|\delta\mathbb H\|^\Delta_p,\quad
  |\delta X|_p,\quad
  |P_1(\sigma)\delta A'|_{-3,p},\quad
  |m_H(\sigma)\delta X|_{-3,p}
  \tag{S9}
  \]
  is at most a common constant times \(\|\delta d\|_{\mathrm{dat},p}\).
  This is exactly the five-member reading in I 112588–112610.
  It includes the full covariant Laplacian, not just a longitudinal
  combination or a first-order norm.
* **(c) Covariance.** Transport the entire equation, including \(j,b,J\),
  boundaries and the reference patch. The transported solution is the
  solution of the transported problem whenever both belong to the
  uniqueness domain. The same qualification applies to the rider.
* **(d) Physical identification.** At switches one, on a real critical
  base with its own current, take \(j=0\). If the nearby Balaban critical
  solution lies in the admitted logarithm, gauge and uniqueness domains,
  then this solution equals it. The identity continues in the complex
  block datum on the common connected analytic domain. It does not
  identify an independent \(J\) with an own-current response.
* **(e), proposed reading only.** At the two localised sets
  \(\mathfrak B^0,\mathfrak B^C\) of I 94835–94842, with switches one and the
  stated small datum and geometric conditions, the same applicable
  conclusions and parameterised substitution remain available.
  That passage merely calls (e) a “side clause”; it uses no further
  mathematical content of (e). This reading adds no new estimate.
* **(f) Restriction and zero components.** When the tagged kernels,
  constraints, boundary data and field datum restrict to a component
  without crossing a switched wall, restriction commutes with solution.
  A component with both data zero has zero triple. In particular the
  supported fields in U23 and U25 vanish outside their determining set,
  provided their actual field data have that support property.

**Uniqueness domain.** In each specified real-reference patch use the product
of the contraction balls \(\|z\|\leq r_z\), \(|X|\leq r_X\).
Uniqueness means uniqueness in that product. Choose smaller radii
\(r_z^-<r_z\), \(r_X^-<r_X\) to leave a transport margin.
Form an orbit domain only from bounded transports of that smaller product
whose closure stays in the corresponding contraction product in every patch
used for comparison. Overlaps must carry the transported equation and datum.
This gives a gauge-invariant domain in the precise
sense of invariance under those admitted transitions. It is not a ball
invariant under all complex gauges. Real conjugation must likewise preserve
the base, branches, boundaries and small balls. Every invocation involving
several layers or intermediate parameters must admit each intermediate
datum and each transported solution separately.

**Corollary.** Comparing with zero gives the corresponding size estimates.
The triangle inequality gives
\(\|HX\|_p\leq\|A'\|_p+\|\mathbb H\|_p\).
Exponential weights from (S2) give the stated decay away from an admitted
datum's support. A bound \(\|j\|^\Delta_p\leq K_\sharp|J_{\rm src}|_{-3,p}\),
when separately supplied, may be substituted into (S3). This is substitution,
not a proof of the field-datum lemma or of the legitimacy of a sharp cut.

**Parameterised form (i).** Compose the solution with holomorphic maps of
independent parameters into its open admitted domain. The result is
holomorphic and satisfies the same estimates at every parameter. Cauchy
estimates use only polydiscs whose closures remain in that domain. Along a
telescoping path every intermediate point must remain there. No hypothesis
about smallness only at the endpoints suffices.

**Current rider.** Fix the curvature convention
\(K_W=D_1^*D_1+D_0D_0^*-\Delta_W\).
Define the analytic partner of a furnished triple by
\[
 J^\sharp[1]=(\Delta_W-P_1(\sigma)+K_W)A'
                    -m_H(\sigma)X+F(W,\mathbb H).        \tag{S10}
\]
For the smooth cut \(\chi=t+\tau\widehat\chi_\square\), define
\[
 J^\sharp[\chi]=(\Delta_W-P_1(\sigma)+K_W)(\chi A')
       -\chi m_H(\sigma)X
       -[D_W^*D_W,\chi]HX+F(W,\chi\mathbb H).             \tag{S11}
\]
The required stencil, scale and cutoff conditions are those stated and
proved in the rider section below. The rider asserts the corresponding
local size and difference bounds there, and holomorphy and admitted
covariance. On the physical diagonal its uncut partner is the actual
current difference. Off that diagonal it is the defined partner. The maps
\((e^{i\eta\chi\mathbb H}W,J+\chi J^\sharp[1])\) and
\((e^{i\eta\chi\mathbb H}W,J+J^\sharp[\chi])\) are different constructions.
Each use must specify which one it needs and check its K109 admission.

**Smuggle check.** No downstream field or target is fixed in (S5).
The equations, norms and five outputs are finite and specified. The rider
does not identify a complex switched partner with an own current.
The statement adds no Hölder derivative of \(J\), no arbitrary-gauge
uniqueness and no second response equation. These would change the problem.
The proposed status of the general-field convention and of clause (e)
remains explicit.

## Clause (a): the finite-kernel extension

SA 10562 quotes Balaban's operator formulation: “we can replace the
propagators by arbitrary operators having the same regularity properties
and satisfying the same bounds”. The useful mathematical assertion here is
an operator implication. It is not permission to assume an absent bound.
We prove the implication, including the extra field datum.

Fix a finite lattice and a point where the specified operators are defined
and analytic. Take a small neighbourhood with compact closure inside that
operator domain. All vector spaces below are finite dimensional over
\(\mathbb C\). All constants in this paragraph are allowed to depend on this
neighbourhood and lattice. This qualification is essential.

The analytic ingredients can be checked algebraically. Matrix exponentials
converge by comparison with \(\sum \|A\|^n/n!\). On \(\|E\|<1\),
\(\log(I+E)=\sum_{n\geq1}(-1)^{n+1}E^n/n\) converges normally.
An invertible finite matrix \(B_0\) has the analytic inverse
\[
 (B_0+E)^{-1}=\sum_{n\geq0}(-B_0^{-1}E)^nB_0^{-1}
 \quad\text{if }\|B_0^{-1}E\|<1.
\]
These identities prove local analyticity of the unswitched constructions.
For a switched walk series, use its actual tagged coefficients. If their
norms have summable bounds \(a_\omega\) after multiplication by the largest
allowed switch monomials on a slightly larger polydisc, its tails are bounded
by \(\sum_{\omega\notin F}a_\omega\), uniformly on the smaller polydisc.
Finite partial sums are holomorphic; the Cauchy integral formula passes to
the uniform limit. This proves analyticity wherever that majorant holds.
It does not prove the majorant merely from the word “walk”.

Here is the complete local contraction calculation. Absorb scale
multiplications into the finite operator norms. Write \(a=\ell A'\) and
\(K=\|\ell H\|\). On an argument ball of radius \(s\), let
\(\|D^2C\|\leq c\). Taylor's integral formula, together with
\(C(0)=DC(0)=0\), gives
\[
 |C(u)|\leq\tfrac12c\|u\|^2,\qquad
 \|DC(u)\|\leq c\|u\|.
\]
Choose \(r_0>0\) with \(2r_0<s\) and \(4cKr_0<1\).
For \(\|a\|\leq r_0\), the map
\[
 \Psi_a(X)=C(a-\ell HX)
\]
sends \(|X|\leq2cr_0^2\) into itself: its argument has norm at most \(2r_0\),
and its value has norm at most \(2cr_0^2\). Its Lipschitz constant is
at most \(2cr_0K<1/2\). Starting at zero, successive differences are bounded
by a geometric series. Their sums converge in the complete finite-dimensional
space. The limit solves the equation. Two limits differ by at most half
their distance, hence are equal. Repeating the argument with the actual
\(\|a\|\) gives
\[
 |X(a)|\leq2c\|a\|^2.                                  \tag{A1}
\]
Uniform convergence of the iterates on smaller parameter polydiscs proves
holomorphy by the preceding Cauchy argument. In particular \(DX(0)=0\).

This also proves that the seven terms defining \(V'\) are quadratic or
higher. Indeed \(D=X=O(A'^2)\), \(D'=O(A')\), and
\(D_3=D-C^{(2)}(\ell A')=O(A'^3)\).
The nonlinear action remainder whose derivative is used here is
\[
 -\langle HD_3,J\rangle-\langle QA',kD\rangle
 +\tfrac12\langle\ell^{-1}D,kD\rangle
 +V_0(A'-HD)-\langle\Lambda A',j_J(HD)\rangle .
\]
Differentiate by the product and chain rules.
The first term gives one derivative term, the second gives two, the third
gives one, the fourth gives one, and the last gives two.
The third uses the symmetry of
\(\ell^{-1}k=\ell^{-1}(q_J-a)\ell^{-1}\);
the last uses \(j_J^T=k_J\). Both follow from the defining bilinear
pairings. In the printed order the seven terms are
\[
\begin{split}
&-D_3'^TH^TJ,\quad -Q^TkD,\quad -D'^Tk^TQA',\\
&D'^T\ell^{-1}kD,\quad (I-HD')^T\nabla V_0(\mathbb H),\\
&-\Lambda^Tj_J(HD),\quad -D'^TH^Tk_J(\Lambda A').
\end{split}                                             \tag{A2}
\]
Here \(V_0\) is the action remainder after its terms through degree two
have been subtracted. Its gradient therefore starts at degree two.
Every term in (A2) has degree at least two. The transpose is an algebraic
transpose. The assertion does not use positivity. Analyticity and the
order of vanishing give a finite constant \(v\) such that
\[
 \|V'(A)\|\leq\tfrac12v\|A\|^2,\qquad
 \|DV'(A)\|\leq v\|A\|
 \tag{A3}
\]
on a sufficiently small ball.

Put \(g=\|G\|\), \(h=\|H_0\|\), \(t=\|T\|\), and
\(k=\|G\Theta_JH_0\|\), in the spaces of (S5).
Choose \(r>0\) so that the \(A'\)-ball of radius \(2r\) is in the inner
domain and \(4gvr<1\). Admit data satisfying
\[
 h|b|<r,\qquad t\|j\|+k|b|<r/2.
 \tag{A4}
\]
For \(\|z\|\leq r\), (A3) bounds the nonlinear term by \(2gvr^2<r/2\).
It bounds the derivative in \(z\) by \(2gvr<1/2\).
The same geometric-series proof gives a unique \(z\) in that ball.
It gives joint holomorphy in every independent parameter. At \(d=0\),
\(z=X=0\) is the solution. If all maps preserve the stipulated real
subspaces, all iterates are real. Thus the solution is real.

This proves the **finite-kernel local version of (a)** for (S5).
It also proves its parameterised form: composition is holomorphic, and the
same convergent series is uniform on compact subsets of an admitted parameter
domain. For a scalar parameter disc of radius \(R\), the Cauchy formula gives
\(|f^{(m)}(0)|\leq m!\sup_{|z|=R}|f(z)|/R^m\).
This follows by expanding \((z-w)^{-1}\) in the contour formula and comparing
coefficients. It does not justify a contour that leaves the admitted domain.

I 15311–15340 gives a switched **block-only** contraction. Its uniform
conclusion cannot alone bound \(t\|j\|\) in (A4), or certify that a different
general-field construction uses (S5). We therefore do not promote the local
argument to uniform general-field existence. In the remaining sections,
“furnished solution” always retains this distinction.

## Clause (f): restriction, walls and zero components

I 15332–15333 says, “all kernels vanish across the components of
\(Y(\sigma)\), and the equations separate”. Here is the exact algebraic
extension of that conclusion to the general datum.

Let \(E=\bigoplus_\alpha E_\alpha\) be the decomposition into components
left by a switched wall. Assume every surviving primitive kernel maps each
component to itself. Assume the same for the boundary extension, block map,
and local nonlinear operations. These hypotheses say precisely that the
specified wall kills all tagged crossings; support of the final endpoints
alone would not suffice.

A composition of component-preserving maps preserves components. A sum of
them preserves components, including a normally convergent sum, because
each coordinate projection is continuous. Multiplication and a local
analytic power series preserve components when their arguments are
componentwise. Consequently every expression in (A2), the inner map, and the
outer map commutes with the projection \(\pi_\alpha\), with its inputs
restricted at the same time.

Start both the inner and outer iterations at zero. Induction on the iteration
number now proves that restriction of each iterate equals the corresponding
restricted iterate. Take the limit. This proves restriction of the solution.
If \(j_\alpha=b_\alpha=0\), both restricted iterations remain identically zero
at every step. The restricted triple is therefore zero. Equivalently,
zero solves the restricted equations and uniqueness identifies it.

This proves (f) for every furnished contraction problem with those
component-preserving kernels. It covers a general field datum without cutting
it or trying to estimate derivatives of an indicator. It also proves
compatibility on two determining sets whose restricted operators, boundary
extensions and data agree. It proves no compatibility when just their
names or underlying sets agree.

For an exempted family, the actual monomials are obtained by setting some
variables to one. This stays in \(|\sigma|\leq e^{\kappa_1}\).
Any already valid common majorant remains valid under this substitution.
The same induction then applies. The additional distance and field-datum
estimates in I 72373–72538 are not needed to prove this algebraic assertion.

## Clause (c): covariance and the uniqueness domain

I 15043–15045 says, “the fixed points defining the chart are unique”.
I 15048–15073 transports the chart equation and then uses that uniqueness.
That is the correct order. Transport of the equation by itself does not
put the transported solution inside a uniqueness ball.

For a gauge \(u\), let \(U_E\) denote its induced invertible linear map on
each field or block space. A covariant difference satisfies
\(\nabla_{uW}U_E=U_{E'}\nabla_W\): insert the transformed link
\(u(x)W(x,y)u(y)^{-1}\); the two middle factors cancel.
The same cancellation proves covariance of each parallel transport and
its inverse. A commutator satisfies
\([uAu^{-1},uBu^{-1}]=u[A,B]u^{-1}\).
Multiplication, sums, traces and convergent power series respect these
relations. Inversion does too, since
\((UBU^{-1})^{-1}=UB^{-1}U^{-1}\).
For the bilinear pairing the corresponding dual transformation is the
inverse transpose. Thus every transposed kernel in (A2) transports with
the correct dual action, without conjugating a holomorphic parameter.

Transport the determining set's boundary data and every tag as well.
These identities prove that (S5) and (S6) transform into the same equations
with transported inputs. They also apply to the general \(j\)-term,
including \(Tj\). The transformed triple solves the transformed equations.
If it lies in the admitted inner and outer balls, the uniqueness proof in
(a) identifies it with that chart's solution.

For real unitary gauges, the matrix norm is unchanged, and the covariant
derivative and Laplacian transform by the identities above. Thus their balls
are invariant. For a bounded complex gauge, let \(q_u\) be a common bound
for its induced maps on the norms being used. The sufficient condition is
\[
 q_u r_z^-<r_z,\qquad q_u r_X^-<r_X
 \tag{C1}
\]
for the two unknowns, together with transported-base and transported-datum
admission. One can use the account's conservative \(K^2\) distortion in
(C1). Applying this argument to two patches proves equality on their
admitted overlap. Equality on triple overlaps follows by transitivity.
This constructs the orbit domain specified in the Statement.

The same proof works for real conjugation when the log branch and domain
are conjugation invariant. It proves the realness argument used in U10.
It does not infer that an arbitrary complex gauge sends a small solution
back into its own ball. That stronger assertion is unnecessary in the
listed uses.

This proves covariance and the uniqueness-domain implication for the
furnished local charts. It proves neither uniform chart admission nor
admission of a particular intermediate layer; those must be verified using
the relevant datum estimates before invoking covariance.

## Clause (b): the additional members and the stopping lemma

I 112588–112610 lists the five norms, including
\(\|\mathbb H_1-\mathbb H_2\|_p^\Delta\) and \(|X_1-X_2|_p\).
These are stronger than the admitted input. We first isolate their exact
mathematical content.

For a fixed finite kernel, the inner contraction controls the auxiliary
field as follows. Subtract its two equations and integrate \(DC\) along
the line segment between their arguments:
\[
 \delta X=\int_0^1 DC(u_2+s(u_1-u_2))
           \bigl(\ell\delta A'-\ell H\delta X\bigr)\,ds.
 \tag{B1}
\]
Here \(u_i=\ell A'_i-\ell HX_i\).
For complex arguments the segment is a real-parameter segment in a complex
vector space; the fundamental theorem of calculus still gives this formula.

The weighted version is equally explicit. Let \(c_p r\) bound the weighted
operator norm of \(DC(u)\) on the inner ball, and let
\(h_p=\|\ell H\|_{p\to p}\). If \(c_prh_p\leq1/2\), (B1) gives
\[
 |\delta X|_p\leq2c_pr\,\|\delta A'\|_p.                 \tag{B2}
\]
One may take the supremum over admitted \(p\). On a fixed finite connected
geometry, normalise \(p\) at one cell. Condition (S2) bounds every ratio of
its values by \(e^{\delta\operatorname{diam}(d^\wedge)}\).
The weighted norm of a matrix with entries \(L_{xy}\) is bounded by the
finite sum \(\sup_x\sum_y\|L_{xy}\|p(y)/p(x)\).
This proves that the suprema defining \(c_*=\sup c_p\) and
\(h_*=\sup h_p\) are finite. Taking \(c_*rh_*\leq1/2\) proves (B2) for
every admitted weight, at a possibly mesh- and volume-dependent radius.
Disconnected geometries are treated componentwise as in (f).

The same proof would be uniform if these weighted operator bounds and the
radius were uniform. It never takes a derivative of a weight. It therefore
does not substitute a weighted sup norm for the graph norm of the field datum.

There is also an immediate uniform corollary for furnished triples:
\[
 \|H(X_1-X_2)\|_p
  \leq\|\delta A'\|_p+\|\delta\mathbb H\|_p
  \leq2B_{\mathbb H}\|\delta d\|_{\mathrm{dat},p}.
\]
This uses only \(\mathbb H=A'-HX\), the triangle inequality, and the
admitted input. Comparing with zero proves exactly the layer inference
in U15. It is a first-order estimate and requires no new kernel bound.

The other extra member has a particularly sharp reduction. Since the
kernel is fixed when comparing data,
\[
 \Delta_W\delta\mathbb H
       =\Delta_W\delta A'-\Delta_WH\,\delta X.            \tag{B3}
\]
The admitted input controls the first term. Thus the following is necessary
for (S9). Together with a uniform version of (B2) and the admitted input,
it is sufficient for (S9).

**Stopping lemma \(R_\Delta\).** For the actual completion kernels and their
furnished triples on the full stated datum domain, there is a constant
\(C_\Delta\), independent of mesh, volume, determining set and admitted base,
such that for every admitted weight
\[
 \sup_y\frac{\ell_y^3
   |\Delta_W H^J(\sigma)(X(d_1)-X(d_2))|_y}{p(y)}
       \leq C_\Delta\|d_1-d_2\|_{\mathrm{dat},p}.
 \tag{B4}
\]
This asks only about the auxiliary fields produced by the inner constraint.
It does **not** ask for a Laplacian estimate on arbitrary block inputs.
It does not add a derivative of \(J\), a new base relation, or a restriction
to switches one.

For necessity, add the two Laplacian members in (B3) with its terms
rearranged. For sufficiency, use the triangle inequality in (B3) and then
the already controlled first-order member. This proves both directions.
At a fixed finite kernel (B4) holds with
\(\|\ell^3\Delta_WH\|_{p\to p}\) times the constant in (B2).
Nothing in that finite-matrix argument bounds the constant as the mesh
shrinks. Here are three distinct attempts to obtain precisely that bound.

### Attack 1: use the actual elliptic equation

I 13730–13793 gives the identity
\[
 (\Delta_a-\Theta'_J)H^J=Q^*q_J\ell^{-1}
 \quad(\sigma=1),
 \tag{B5}
\]
and its accompanying text says, “The Laplacian member is not asserted for
\(G_\pi^J\)”. We therefore apply the equation rather than borrowing that
excluded estimate.

The \(\Delta\) in this chart equation is \(\mathscr L_W\), not the
component Laplacian in (S1). Use the definitions
\[
 \Delta_a=\mathscr L_W+D_0RD_0^*+Q^*aQ,\qquad
 \Theta'_J=k_J\Lambda+\Lambda^Tj_J+\Lambda^Tm_J\Lambda.
\]
The conversion to the required operator is exact. Expanding the curl and
its transpose gives
\[
 (D_1^*D_1+D_0D_0^*)B
   =\Delta_WB+K_WB,\qquad
 (K_WB)_\nu=\sum_\mu[\nabla_\nu,\nabla_\mu^*]B_\mu.
\]
For example the mixed terms are
\(-\nabla_\mu^*\nabla_\nu B_\mu+
\nabla_\nu\nabla_\mu^*B_\mu\); these are precisely the indicated commutator.
The diagonal commutator is zero since a shift and its inverse commute.
Together with \(\mathscr L_W=D_1^*D_1+\mathscr C_W\), this proves
\[
 \Delta_W=\mathscr L_W+D_0D_0^*-\mathscr C_W-K_W.
\]
At switches one, \(QH^J=\ell^{-1}\) and \(P_1=D_0(I-R)D_0^*\).
For any \(x\), substitution into (B5) now gives the exact identity
\[
\begin{split}
 \Delta_WH^Jx
  ={}&Q^*(q_J-a)\ell^{-1}x+P_1H^Jx
                      -(\mathscr C_W+K_W)H^Jx\\
    &+\Lambda^Tj_J(H^Jx)\\
    &+k_J\Lambda H^Jx+\Lambda^Tm_J\Lambda H^Jx .
                                                        \tag{B6}
\end{split}
\]
This is a useful reduction. It also identifies the point where the physical
argument uses more than the general-pair hypotheses.

At an admitted physical pair, the Ward/Landau relation \(RD_0^*H^J=0\)
annuls \(\Lambda H^J\) and the last two terms. At an independent pair
that relation is absent. In particular \(m_J=m_3+D_0^*m_4\) produces
\(\Lambda^TD_0^*m_4(\Lambda H^Jx)\).
Expanding the derivative of this product asks for regularity of the
independent current \(J\) that K109 does not impose.
Keeping the derivative on the operator instead produces
\(D_0RG'D_0^*\) acting on that product. I 13600–13617 states its relevant
type of two-sided derivative estimate on “Hölder data of exponent
\(\beta+\varepsilon\)”, not on arbitrary weighted sup-norm data.
The factors already controlled here do not supply that extra regularity
of \(J\). This is the unresolved term in this attack, even if the other
members of (B6) have their needed bounds.

A naive fine-lattice differentiation costs \(\eta^{-1}\). A resulting
bound proportional to \(\eta^{-1}\gamma\) is not uniform for fixed positive
\(\gamma\). This diagnoses the failed estimate; it does not exclude a
cancellation in the actual expression or a better estimate of the composed
operator. Either could still prove (B4).

At nontrivial switches, even (B5) and \(QH=\ell^{-1}\) cannot be used
without a new proof: a killed row has \(QH(\sigma)=0\).
Thus this attack fails to prove (B4) already on the independent-pair,
unswitched subdomain, and supplies no switched proof.

### Attack 2: use weighted first-order bounds and analytic dependence

SA 10576 states that “an oscillating kernel belonging to the class of data”
prevents a uniform Laplacian conclusion from those first-order bounds.
Here is a full finite-dimensional test of that proposed implication.
It is **not** a counterexample for the actual Yang–Mills kernels.

Take an even \(n\geq2\), a periodic lattice of spacing \(\eta=1/n\), and
at least two field components \(e_1,e_2\). Let the field depend only on the
first coordinate \(k\), and set
\[
 v_n(k)=n^{-1}(-1)^ke_2,\qquad H_nx=xv_n,\qquad
 H_0b=be_1,\qquad G=0.
 \tag{B7}
\]
Use one coarse cell of scale one. Let \(\pi_1\) be the average first
component and define \(C(u)=(\pi_1u)^2\). Take \(j=0\), block datum \(b=a\),
and \(V'=0\). The equations (S5)–(S6) then give, exactly,
\[
 A'(a)=ae_1,\qquad X(a)=a^2,\qquad
 \mathbb H(a)=ae_1-a^2v_n.
 \tag{B8}
\]
Indeed \(\pi_1H_nx=0\), so the inner equation has the unique value \(a^2\)
on every ball containing it. The outer equation is simply \(z=0\).
Everything is polynomial in \(a\); no analytic extension issue arises.

The forward physical difference of \(v_n\) has magnitude \(2\).
The positive flat transverse Laplacian has magnitude \(4n\):
\[
 \frac{v_n(k+1)-v_n(k)}{\eta}=-2(-1)^ke_2,\qquad
 \frac{2v_n(k)-v_n(k+1)-v_n(k-1)}{\eta^2}
       =4n(-1)^ke_2.
 \tag{B9}
\]
The same value is obtained from the flat curl-curl operator on this
transverse field. Meanwhile \(\Delta A'(a)=0\).
For \(|a|,|b|\leq r\leq1/4\),
\[
 |a^2-b^2|\leq2r|a-b|,\qquad
 N^\Delta(\delta A')=|a-b|,\qquad
 N(\delta\mathbb H)\leq2|a-b|.
\]
Set the two auxiliary output operators \(P_1\) and \(m_H\) to zero.
The four estimates in the admitted input's shape then hold with constant
two, independently of \(n\). Zero datum gives the zero triple.
Every weight on this single coarse cell is a positive scalar, so division
by that scalar proves the same claim for every admitted weight.
Also \(|\delta X|\leq2r|\delta b|\). Thus even the missing value-norm
member is harmless in this example.

The example also admits a general field datum. Set
\(A'=-j+be_1\), \(X=(\pi_1A')^2\), and
\(\mathbb H=A'-H_nX\) on \(\|j\|^\Delta+|b|\leq r\).
Then \(N^\Delta(\delta A')\leq\|\delta d\|_{\rm dat}\),
\(|\delta X|\leq2r\|\delta d\|_{\rm dat}\), and
\(N(\delta\mathbb H)\leq(1+4r)\|\delta d\|_{\rm dat}
\leq2\|\delta d\|_{\rm dat}\).
Thus the first-order comparison is not obtained by forbidding the general
field slot. The counterexample below uses its subfamily \(j=0\).

In contrast, at \(a=r\), \(b=0\),
\[
 |\Delta H_n(X(a)-X(0))|=4nr^2.
\]
No bound \(4nr^2\leq C_\Delta r\) holds for all even \(n\) at a fixed
positive \(r\). This calculation refutes the inference from analytic
dependence, a small quadratic inner correction, and uniform first-order
comparison alone to (B4).

Cauchy estimates in the datum variable do not change (B9). They bound
derivatives with respect to \(a\), not covariant spatial derivatives.
Weights do not change (B9) either. This second attack therefore fails
unless it uses additional structure of the actual kernels. The example
does not claim to possess that structure.

### Attack 3: transfer the second response system

SA 10438–10464 says, “Away from critical physical pairs the two systems
define separate functions.” This is a decisive scope restriction on the
proposed transfer, rather than a missing name for the same function.

The second system solves for a field \(T_{\rm fld}\) and a multiplier
\(\lambda\), with equations of the form
\[
\begin{split}
 T_{\rm fld}
   &=H_0(s)(B'-C(T_{\rm fld}))
       -\widetilde G(s)
            \{N(T_{\rm fld})-C'_{T_{\rm fld}}{}^T\lambda\},\\
 \lambda
   &=H(s)^TJ+(S(s)-a)(B'-C(T_{\rm fld}))
       +H(s)^T\{N(T_{\rm fld})-C'_{T_{\rm fld}}{}^T\lambda\}.
\end{split}                                             \tag{B10}
\]
The shifted multiplier is \(\lambda-H(s)^TJ\).
Its contraction requires the displayed bounds in its own two spaces and
the additional current ceiling of that system. It is stated on global
domains and strip sequences, not on arbitrary local cores.

On the critical real diagonal at switches one, the response satisfies the
average constraint, the Landau equation, and the multiplier equation.
Substitution then gives (B10). Uniqueness of the second contraction
identifies its field with the first response on their common physical
domain. This explains how its second-order estimate can apply there.

It does not transfer that estimate to the independent-pair problem.
Equality of holomorphic functions on the own-current graph does not
determine a holomorphic function of the independent pair. To check this
directly, the nonzero holomorphic function
\[
 (W,J)\longmapsto J-\mathcal J(W)
\]
vanishes identically on that graph. Likewise \(\sigma_\square-1\) vanishes
at switches one without vanishing on a switch polydisc.
Thus the identity theorem in the block variables cannot perform either
extension. One would have to prove that the first solution satisfies
(B10) on the larger domain. Its published restriction expressly does not
supply that assertion.

This third attack fails for the actual general domain, even if one grants
the second system's own contraction and bounds. We have neither proved nor
refuted (B4) for the actual completion kernels.

**Disposition of (b).** The admitted part remains an input. The auxiliary
value estimate and the full five-member estimate are proved locally at a
fixed finite analytic kernel, with constants that may depend on it.
The uniform upgrade stops at \(R_\Delta\), tested by the elliptic equation,
the analytic/weighted operator argument, and the second response system.
The latter two tests show exactly why two tempting replacements would not
prove the required assertion.

## Clause (d): identification on the admitted physical domain

I 15669–15701 assumes the physical critical solution lies in the chart's
small ball. Its proof uses \(P_0^TJ=0\) and the critical equation.
We retain that admission hypothesis and rebuild the identification.

Let the given nearby physical solution, expressed in the chart's
coordinates, be \(A'_{\rm phys}\). At switches one and on the real critical
base with its own current, it satisfies
\[
 QA'_{\rm phys}=\ell^{-1}b,\qquad RD^*A'_{\rm phys}=0.
 \tag{D1}
\]
The derivative of the constrained action in every direction \(v\in\ker Q\)
is
\[
 \langle v,J+(\mathscr L_W-\Theta_J)A'_{\rm phys}
                         +V'(A'_{\rm phys})\rangle=0.
 \tag{D2}
\]
This is the critical equation in these coordinates: the constant derivative
is \(J\), its linear part is the displayed quadratic form, and the chain
rule calculation preceding (A2) differentiates the nonlinear remainder.
It is a finite differentiation identity,
not a claim about criticality away from the physical base.

Put \(G_0=\Delta_a^{-1}\), \(q_0=(QG_0Q^*)^{-1}\),
\[
 H_0=G_0Q^*q_0\ell^{-1},\qquad
 P_0=I-G_0Q^*q_0Q,\qquad \widetilde G_0=P_0G_0.
\]
Direct multiplication gives
\[
 QP_0=0,\quad QH_0=\ell^{-1},\quad
 P_0^TQ^*=0,\quad
 G_0P_0^T=P_0G_0,\quad
 G_0P_0^T\Delta_a=P_0.
 \tag{D3}
\]
The transpose identity uses the symmetry of the quadratic form and hence
of its inverse and Gram matrix. For example,
\(G_0P_0^T=G_0-G_0Q^*q_0QG_0=P_0G_0\).
These are unswitched identities.

The real critical-base hypothesis gives \(J\in\operatorname{range}Q^*\).
Apply (D2) with \(v=P_0w\) for arbitrary \(w\). Thus
\[
 P_0^T\{(\mathscr L_W-\Theta_J)A'_{\rm phys}
                                      +V'(A'_{\rm phys})\}=0.
\]
By (D1), replacing \(\mathscr L_W\) by
\(\Delta_a=\mathscr L_W+D_0RD_0^*+Q^*aQ\) does not change this equation:
the first added term is zero, and \(P_0^T\) kills the second.
Multiply by \(G_0\) and use (D3). We obtain
\[
 A'_{\rm phys}-H_0b
       =\widetilde G_0\{\Theta_JA'_{\rm phys}
                                      -V'(A'_{\rm phys})\}.
\]
This is exactly (S4), hence (S5) with \(j=0,\sigma=1\).
Admission of \(A'_{\rm phys}-H_0b\) to the outer ball now permits uniqueness
to identify it with the chart solution. The inner equation and its uniqueness
identify \(X\) and therefore \(\mathbb H\).

Suppose both physical and chart constructions are holomorphic in \(b\) on
a common connected domain. Equality for real \(b\) in an open ball implies
equality on the complex ball: all real partial derivatives of their
difference vanish, and for a holomorphic function these are its power-series
coefficients up to factorials. The power series is therefore zero.
Overlapping analytic balls extend the equality through the connected domain.
This proves the continuation used in U32, in the block variables only.

Differentiating (S5) at datum zero gives, for a block direction \(v\),
\[
 D_b\mathbb H(0)v
       =(I+G\Theta_J)H_0v,\qquad D_bX(0)v=0.
 \tag{D4}
\]
The equality with the physical response identifies (D4) with its linear
response on the physical diagonal. It does not identify it with the
auxiliary lifting kernel \(H^J\). This distinction is needed in U07, U11
and U12.

Thus (d) is proved as an identification of **already admitted** physical
and chart solutions. It neither constructs the physical minimizer nor
proves the inclusion of a proposed one in the uniqueness domain.

## Clause (e): the minimal proposed side clause

I 94839–94842 says that (c), (d), (e) and parameterised (i) “enter only as
side clauses accompanying these”. No mathematical assertion from (e) is
used in that passage.

For the proposed reading in the Statement, take either of the two indicated
determining sets, switches one, and data satisfying the stated localised
admission conditions. Substitute these values into whichever clauses have
been proved at that scope. Substitution preserves their hypotheses and
conclusions. Composing with an admitted holomorphic parameter map is the
parameterised argument in (a). This proves the proposed side clause as a
specialisation, and nothing more. It cannot upgrade a local theorem to a
uniform one. It assigns no unrecorded content to the missing original (e).

## Current rider: a direct proof and a cutoff repair

I 111538–111545 defines the cut partner by the expression (S11).
I 111614 labels the commutator coefficient count as the incomplete step
“\((\ast)\)”. We prove that estimate directly. No second-order bound on
\(HX\) will enter it.

### The coefficient count

Write
\[
 (T_\mu B)(x)=R_{x,\mu}B(x+\eta e_\mu),\quad
 \nabla_\mu=(T_\mu-I)/\eta,\quad
 \nabla_\mu^*=(T_\mu^{-1}-I)/\eta.
\]
Let
\(\vartheta=\sup\max(\|R\|,\|R^{-1}\|)\), and assume
\(1\leq\vartheta\leq5/4\). The norm of an adjoint transport and of its inverse
has this bound on the stated stencil. For a scalar \(\chi\), write
\(f_\alpha=\partial_\alpha\chi\) and \(g_\mu=\partial^-_\mu\chi\).
Multiplication at the base point gives
\[
 [\nabla_\alpha,\chi]B=f_\alpha T_\alpha B,\qquad
 [\nabla_\mu^*,\chi]B=-g_\mu T_\mu^{-1}B.
\]
Indeed, expanding each left side cancels the terms with \(\chi(x)\);
the remaining numerator is the indicated scalar difference times the
transported field. Applying these identities once more gives
\[
\begin{split}
 [\nabla_\mu^*\nabla_\alpha,\chi]B
 ={}&f_\alpha\nabla_\mu^*T_\alpha B
   -(\partial^-_\mu f_\alpha)T_\mu^{-1}T_\alpha B\\
   &-g_\mu T_\mu^{-1}\nabla_\alpha B .
\end{split}                                             \tag{R1}
\]
In particular, (R1) does not differentiate \(R\).

For \(\alpha=\mu\),
\(\nabla_\mu^*T_\mu=-\nabla_\mu\) and \(T_\mu^{-1}T_\mu=I\).
Thus the coefficient of a first difference of \(\chi\) times a first
covariant derivative of \(B\) is at most \(1+\vartheta\).
The coefficient of a second difference times a value of \(B\) is one.

For \(\alpha=\nu\ne\mu\), insert and subtract \(T_\mu^{-1}B\) and \(B\):
\[
 \nabla_\mu^*T_\nu B
   =T_\mu^{-1}\nabla_\nu B+\nabla_\mu^*B-\nabla_\nu B,\qquad
 \nabla_\mu^*B=-T_\mu^{-1}\nabla_\mu B.
 \tag{R2}
\]
These identities hold for noncommuting transports. They do not commute
\(T_\mu\) with \(T_\nu\). The first term in (R1) now costs at most
\(1+2\vartheta\) derivatives of \(B\); its last term costs \(\vartheta\).
Its middle term costs \(\vartheta^2\) values of \(B\).

For a one-form, the specified pairing gives
\[
 (D^*DB)_\nu
    =\sum_{\mu\ne\nu}
        \nabla_\mu^*(\nabla_\mu B_\nu-\nabla_\nu B_\mu).
\]
For each \(\mu\ne\nu\), the total derivative coefficient is
\((1+\vartheta)+(1+3\vartheta)=2+4\vartheta\).
The value coefficient is \(1+\vartheta^2\leq2+4\vartheta\).
All values and derivatives read in (R1)–(R2) have base points in
\(\operatorname{st}(b)=\{x:|x-b_-|_\infty\leq\eta\}\).
For example \(T_\mu^{-1}T_\nu B\) reads \(B\) at
\(b_- -\eta e_\mu+\eta e_\nu\), which is in that stencil.
Taking the maxima \(s_1,s_2\) of the first and second scalar differences on
this stencil proves
\[
 |[D^*D,\chi]B(b)|
   \leq c_d\left(s_1(b)\sup_{\operatorname{st}(b)}|\nabla_WB|
                +s_2(b)\sup_{\operatorname{st}(b)}|B|\right),
 \quad c_d=(2+4\vartheta)(d-1).
 \tag{R3}
\]
This proves the missing coefficient count, including complex transports.

### A nonvacuous cutoff with the same final constant

I 111520–111525 asks for
\(\zeta=1\) on \([-1/3,1/3]\), \(\zeta=0\) outside
\((-2/3,2/3)\), and \(|\zeta'|,|\zeta''|\leq5\).
That combination is impossible for a \(C^2\) function.
At \(x=1/3\), \(\zeta(x)=1\) and \(\zeta'(x)=0\).
Taylor's integral formula would give
\[
 \zeta(2/3)
 =1+\int_{1/3}^{2/3}(2/3-s)\zeta''(s)\,ds
 \geq1-\tfrac52(1/3)^2=13/18>0,
 \tag{R4}
\]
contrary to continuity and the required zero value at \(2/3\).
The commutator argument must therefore not rely on the existence of that
printed cutoff.

Here is an explicit repair. On \([0,1]\) let \(v_0\) be the trapezoid
which rises with slope \(9/2\) to height \(3/2\) on \([0,1/3]\),
stays at that height on \([1/3,2/3]\), and falls with slope \(-9/2\)
to zero on \([2/3,1]\). Extend it by zero. Its integral is
\(1/4+1/2+1/4=1\).
Put \(\epsilon=1/200\), \(c=99/100\), and
\[
 v_\epsilon(u)=c^{-1}v_0((u-\epsilon)/c),\qquad
 k_\epsilon(u)=\frac{(\epsilon-|u|)_+}{\epsilon^2},\qquad
 v=v_\epsilon*k_\epsilon .
 \tag{R5}
\]
Both factors in the convolution are nonnegative and have integral one.
Their supports show \(\operatorname{supp}v\subset[0,1]\).
The convolution is \(C^2\): express \(v_\epsilon\) as a finite linear
combination of ramps \((u-a)_+\); the second derivative of the convolution
of a ramp with \(k_\epsilon\) is the continuous function
\(k_\epsilon(u-a)\). This also proves the asserted differentiability
without distribution notation.
An integral average preserves sup and Lipschitz bounds. Hence
\[
 0\leq v\leq50/33,\qquad |v'|\leq45000/9801,\qquad
 \int_{\mathbb R}v=1.
 \tag{R6}
\]
Define \(q(u)=1-\int_0^uv(s)\,ds\) on \([0,1]\), with its constant
extensions one and zero. Define \(\zeta(x)=q(3|x|-1)\) on
\(1/3\leq|x|\leq2/3\), with the required constant extensions.
It is \(C^2\), is between zero and one, and has the required plateau and
support. The endpoint derivatives agree because \(v\), with its zero
extension, is \(C^2\). Its bounds are
\[
 |\zeta'|\leq50/11<5,\qquad
 |\zeta''|\leq405000/9801<42.                           \tag{R7}
\]
This construction is independent of the fine lattice.

Use this repaired cutoff in
\[
 \widehat\chi_\square(x)
    =\prod_\nu\zeta((x_\nu-y_{\square,\nu})/(M\ell_\square)),
 \qquad \chi=t+\tau\widehat\chi_\square .
\]
Repeated-index second partial derivatives cost at most \(42\); mixed ones
cost at most \(25\). Integrating derivatives over one or two intervals of
length \(\eta\) bounds the corresponding lattice differences, so
\[
 s_1\leq\frac{5|\tau|}{M\ell_\square},\qquad
 s_2\leq\frac{42|\tau|}{(M\ell_\square)^2}.              \tag{R8}
\]
This replaces the impossible primitive bound in the printed proof.

For completeness, the scale comparison uses only the stated grading
geometry. Suppose \(\widetilde\Delta(y)\) meets \(\square\).
The cover cube contains a current cell \(c_\square\) of its own level.
If the current cell \(c_y\) had level at least two larger, graded separation
would give
\[
 \operatorname{dist}_\infty(c_y,c_\square)\geq M\ell_y/L .
\]
A point in the intersection lies within \(\ell_y\) of \(c_y\), and
within \(M\ell_\square\) of the subcube \(c_\square\). Thus the distance
is at most \(\ell_y+M\ell_y/L^2\). This is strictly smaller than
\(M\ell_y/L\), since \(M\geq2L^2\) and \(L\geq3\).
The contradiction proves \(\ell_y\leq L\ell_\square\).
Consequently (R8) gives
\[
 \ell_y s_1+\ell_y^2s_2
 \leq|\tau|\left(\frac5{2L}+\frac{42}{4L^2}\right)
 \leq2|\tau|.                                         \tag{R9}
\]
The last inequality is equality at \(L=3\) with these relaxed bounds and
decreases for larger \(L\).

If the doubled stencil misses \(\square\), its first and second cutoff
differences vanish. Indeed a nonzero difference must read a point of the
support within two lattice steps; \(M\ell_\square\geq18\eta\) keeps those
base points inside \(\square\). Combining this fact, (R3), (R9), and the
two defining entries of \(N_y(B)\) proves
\[
 \ell_y^3|[D^*D,\chi]B|
 \leq 2c_d|\tau|\,N_y(B)
          {\bf1}[\widetilde\Delta(y)\cap\square\ne\varnothing].
 \tag{R10}
\]
Thus the repaired cutoff preserves **exactly** the claimed
\(c_\zeta=2c_d\). At real kernels \(c_d=6(d-1)\); for
\(\vartheta\leq5/4\), \(c_d\leq7(d-1)\).
If an application fixes a particular cutoff in advance, it must check its
actual derivative bounds or replace it by (R5)–(R7). The impossible printed
bound is not a verification of that application.

### The partner estimate and its precise scope

I 111397–111406 gives the representation (S10).
Subtracting two instances at one kernel gives
\[
 \delta J^\sharp
  =\Delta_W\delta A'-P_1\delta A'+K_W\delta A'
             -m_H\delta X+F(W,\mathbb H_1)-F(W,\mathbb H_2).
 \tag{R11}
\]
No equation for the current of \(t\mathbb H\) was used here.

Here is a fully finite local version that needs no unproved uniform
remainder constant. Set
\[
 k_y=\sup_{B\ne0}\frac{\ell_y^3|K_WB|_y}{N_y(B)},\qquad
 f_y=\sup_{N_y(h)\leq1/20}
         \|D_hF(W,h)\|_{N_y\to\ell_y^3|\cdot|_y},
 \tag{R12}
\]
on a compact ball inside the actual analytic stencil domain.
Use the stencil quotient space if \(N_y\) has a kernel; locality makes
the maps factor through it. On a fixed finite lattice these numbers are
finite. To see the second assertion directly, bound the scaled remainder
by \(M_R\) on a slightly larger ball of radius \(R>1/20\).
For \(N_y(h)\leq1/20\) and \(N_y(u)=1\), apply the one-variable Cauchy
formula to \(z\mapsto F(W,h+zu)\) on discs of radius less than
\(R-1/20\), and let their radii increase to that number. It gives
\[
 f_y\leq\frac{M_R}{R-1/20}<\infty .
\]
Apply a norming linear functional to justify the vector-valued Cauchy bound.
The local analyticity used here follows from the finitely many plaquette products
and the exponential series, on the stated branch domain.

If \(N_y(\mathbb H_i)\leq1/40\), their segment lies in that ball.
The fundamental theorem of calculus bounds the last term of (R11) by
\(f_yN_y(\delta\mathbb H)\).
The other terms cost \(1,1,k_y,1\) times the appropriate entries.
Thus (R11) is bounded by \(3+k_y+f_y\) times the maximum of its four
input sizes. The admitted estimate then bounds its datum dependence.
This proves a finite-kernel local current rider.

The account's numerical normalisation is an additional useful implication.
Its displayed local coefficient inequalities are
\[
 \ell_y^3|K_WB|\leq18d\,\mathsf p(W)\,\ell_y|B|,\qquad
 \ell_y^3|F(W,h)|
 \leq K_J(\mathsf p(W)+\Theta_0+\Theta_1)(\Theta_0+\Theta_1),
 \quad \Theta_0+\Theta_1\leq2N_y(h).
 \tag{R13}
\]
They are printed at I 94996–95013 and I 111446–111460. For kernels on which
these local inequalities have been established with a common \(K_J\),
the following calculation recovers the account's current constant.
We state this premise explicitly; a citation to it does not establish its
uniform validity on a new complex kernel class.

Let \(D=N_y(\mathbb H_1-\mathbb H_2)\).
If \(D=0\), locality makes the remainder difference zero.
Otherwise put \(R_0=1/(40D)\) and
\(\phi(z)=F(W,\mathbb H_2+z(\mathbb H_1-\mathbb H_2))\).
For \(|z|\leq R_0\), the field size is at most \(1/20\).
Under \(\mathsf p(W)\leq1\), (R13) gives
\(\ell_y^3|\phi(z)|\leq(1+1/10)/10\,K_J=0.11K_J\).
Hence \(\ell_y^3|\phi(z)-\phi(0)|\leq0.22K_J\).
When \(R_0\geq1\), the zero at \(z=0\) gives
\[
 \ell_y^3|\phi(1)-\phi(0)|
       \leq0.22K_J/R_0=8.8K_JD\leq9K_JD.
 \tag{R14}
\]
For clarity, the zero estimate follows by applying the maximum principle
to \((\phi(z)-\phi(0))/z\) on smaller concentric discs and then taking
their radii to \(R_0\). Apply a norming linear functional for a
vector-valued output. If \(R_0<1\), the two endpoint bounds give
\(0.22K_J<8.8K_JD\) directly.

The linear contribution in (R11) is \(3+18d\).
The \(K_W\) term acts on \(\delta A'\), so its bound uses
\(N_y(\delta A')\leq N_y^\Delta(\delta A')\).
The appearance of \(N_y(\delta\mathbb H)\) in that line of the printed
proof is unnecessary and is not used here. We obtain
\[
 \ell_y^3|\delta J^\sharp|
       \leq(3+18d+9K_J)\,\mathsf N_y(\delta).
 \tag{R15}
\]

For the cut partner, apply the size bound with \(F(W,0)=0\) and
\(N_y(\chi\mathbb H)\leq1/40\).
The four terms other than the commutator are bounded directly by
\(K_{\mathsf j}=3+18d+9K_J\) times the first four entries
\[
 N_y^\Delta(\chi A'),\quad N_y(\chi\mathbb H),\quad
 \ell_y^3|P_1(\chi A')|,\quad
 \ell_y^3|\chi m_HX|.
 \tag{R16}
\]
This is a direct estimate of a formula. It does not pretend that
\((\chi A',X,\chi\mathbb H)\) is another layer solution.
Apply (R10) with \(B=HX\) to its fifth term. The result is exactly
\[
 \ell_y^3|J^\sharp[\chi]|
 \leq (K_{\mathsf j}+c_\zeta)\,
 \max\left\{\text{the four entries in (R16)},\
 |\tau|N_y(HX){\bf1}[\widetilde\Delta(y)\cap\square\ne\varnothing]\right\}.
 \tag{R17}
\]
With \(3+k_y+f_y\) in place of \(K_{\mathsf j}\), the same proof gives
the finite local version from (R12). No part of this proof needs (B4).

Every expression in (S10)–(S11) is holomorphic on its actual domain.
The transport identities in (c), with scalar \(\chi\) unchanged, prove
covariance. The physical identity can also be checked explicitly.
By definition of the current remainder,
\(\mathcal J(e^{i\eta h}W)-\mathcal J(W)=D_1^*D_1h+F(W,h)\).
At an admitted physical solution \(RD_0^*A'=0\), so the curl identity
proved in (B6)'s derivation gives
\[
 D_1^*D_1A'=(\Delta_W-P_1+K_W)A'.
\]
The physical lifting equation gives
\[
 D_1^*D_1HX
   =Q^*(q_J-a)\ell^{-1}X+\Lambda^Tj_J(HX)-\mathscr C_WHX.
\]
This is the physical \(m_HX\) term, denoted \(K_1X\) in the chart
representation at I 14450–14495. Subtracting these two identities and
using \(h=\mathbb H=A'-HX\) proves (S10). Away from that physical identification,
(S10) remains the definition of the partner; the proof has not equated
it with the current of an arbitrary complex switched field.

Finally, the rider gives a simple admission test, not automatic admission.
If the base current has size at most \(\gamma_0/2\) and the appropriate
partner increment has size at most \(\gamma_0/2\), their sum has size at
most \(\gamma_0\). For the links, the exponential series gives
\(\|e^{i\eta h}-I\|\leq\eta\|h\|e^{\eta\|h\|}\).
The covariant product rule bounds its first difference using that of \(h\)
and the base. These inequalities must fit the remaining margins in the
chosen K109 patch. They do not replace checking the specified patch,
core, gauge and intermediate-datum conditions in U02, U19 or U27.

## Result

The proposed statement specifies the datum, equation, weighted norms,
admission domain, uniqueness domain, switches, localised scope, corollary,
parameterised form and rider. It is not a proved uniform general layer
theorem. In particular, a choice of equations consistent with the block-only
chart does not by itself identify every previously undefined general-field
invocation with those equations.

The proved scopes are as follows.

| Part | Result proved here |
|---|---|
| (a) | A local analytic contraction theorem at a fixed finite analytic operator datum, with the general field forcing in (S5), explicit smallness inequalities, realness and parameterised substitution. No common mesh-independent radius is claimed. |
| (f) | Restriction and zero components for furnished contraction problems whose actual kernels, boundaries and data preserve the components. |
| (c), uniqueness | Covariance on admitted overlaps; uniqueness in the two small balls; gluing under bounded admitted gauge transitions; conjugation on invariant domains. |
| (b) | The auxiliary value bound (B2) and the five-norm theorem at a fixed finite kernel. The uniform extra Laplacian member is equivalent, in the stated sense, to the unproved estimate (B4). The admitted part is not reproved or relabelled as a result of this lane. |
| (d) | Identification of already admitted physical critical solutions, and continuation in the block datum on their common connected analytic domain. |
| (e) | Only the marked proposed specialisation. The missing original clause's content has not been recovered. |
| Corollary | Zero-comparison, the first-order \(HX\) estimate, exponential-weight substitution and legitimate parameter substitution. No current-to-field conversion is proved here. |
| Rider | The exact complex-transport coefficient count (R3); a nonvacuous cutoff construction preserving \(c_\zeta=2c_d\); the finite local partner bound; and the implication (R13) \(\Rightarrow\) (R15), (R17). The latter does not certify (R13) on a larger kernel class. |

Here is the invocation accounting. “Partial” means that the indicated
mathematical implication has been proved, but the invocation of a uniform
general layer theorem is **not** discharged. “Covered” refers to the layer
inference itself, conditional on the single admitted input and the actual
furnished representation; it does not certify the surrounding downstream
theorem. This distinction prevents a first-order corollary from counting as
a proof of the full five-norm theorem.

| Use | Bounded invocation passage read | Disposition at its requested scope |
|---|---|---|
| U01 | I 72373–72538 | Partial: exempted-switch substitution and component restriction. The assumed six-clause uniform package is not supplied. |
| U02 | I 73103–73140 | Partial: datum substitution and explicit intermediate-admission test. No general uniform four-layer construction is established. |
| U03 | I 73546–73633 | Partial: joint holomorphy on a common admitted domain. The domain for all four actual general layers is not certified. |
| U04 | I 89955–90008 | Partial: the wall and rider implications. Its uniform hypothesis remains an hypothesis. |
| U05 | I 94123–94286 | Not discharged: its common radius and constant selections require the uniform theorem. |
| U06 | I 94303–94422 | Partial: the two localised substitutions are specified. Their uniform general-field solutions are not proved here. |
| U07 | I 94448–94586 | Partial: the physical derivative identification (D4). Its general graph-norm derivative bound needs (B4). |
| U08 | I 94608–94843 | Partial: geometric admission, qualified covariance/identification and the proposed side clause are explicit. The main uniform (a), (b) call is not discharged. |
| U09 | I 94846–95085 | Partial: source-current estimation as (R11)–(R15). Its full response graph norm is not established. The proof does not conflate \(A'\) with \(\mathbb H\). |
| U10 | I 95682–95700 | Partial: conjugation plus admitted uniqueness gives realness. Uniform admission is not inferred from realness. |
| U11 | I 95750–95790 | Partial: physical covariance and linear identification on admitted overlaps. |
| U12 | I 95872–95908 | Partial: the same physical identification under the admitted real gauge. |
| U13 | I 99780–99796; 99878–99892 | Not discharged: common floors and a common ceiling still require a uniform analytic domain. |
| U14 | I 111489–111716 | Partial: its missing commutator count is proved. Its printed cutoff is impossible and is replaced here by (R5)–(R7), preserving the claimed constant. The partner estimate follows with the explicit local coefficient premises. |
| U15 | I 112180–112230 | **Covered:** \(HX=A'-\mathbb H\) and the triangle inequality give its first-order \(HX\) estimate from the admitted input. No extra Laplacian estimate enters this inference. |
| U16 | I 112570–112620 | Not discharged: its five weighted norms include the member equivalent to (B4). |
| U17 | I 114790–114880 | Partial: comparison at weight one and the rider admission test. The complete uniform healing-layer call is not supplied. |
| U18 | I 115382–115405 | Partial: the four admitted sizes and the first-order \(HX\) contribution. A tail estimate for a cut nonlocal operator is not inferred from those four sizes. |
| U19 | I 116555–116669 | Partial: current-size admission is reduced to explicit margins. The required full response graph norm is not established. |
| U20 | I 125775–125792 | Not discharged as a uniform full-layer invocation. The numerical choice of \(K_{\rm nr}\) does not prove the missing norm member. |
| U21 | I 131621–131695 | Partial: admitted physical identification and partner bounds. Its uniform full layer estimate remains conditional. |
| U22 | I 131725–131746 | Partial: parameter substitution on the actual localised domain. No extension from a different domain is made. |
| U23 | I 136750–136770 | Partial: exact vanishing follows from component preservation and zero data. Actual general-field admission must still be supplied. |
| U24 | I 137562–137603 | Partial: admitted localised substitution and the appropriate current partner. No independent extension theorem is asserted. |
| U25 | I 137978–138001 | Partial: restriction/gluing by the componentwise contraction proof. |
| U26 | I 138640–138667 | Not discharged as a uniform comparison in all stated layer units. |
| U27 | II 13888–14105 | Partial: joint holomorphy, the distinction between the two cut-current maps, and a direct current-admission test. All-block containment is not automatic. |
| U28 | II 15390–15404 | Partial: parameterised substitution, conditional on its general layer's admission. |
| U29 | II 20798–20808 | Partial: the defined cut formula and its local bound. It does not identify a general switched partner with an own current. |
| U30 | II 23160–23177; 23990–24005 | Partial: holomorphic cut-partner composition on an admitted parameter domain. |
| U31 | II 51814–51855; 52030–52070 | Partial: analytic substitution of the averaging datum. The uniform general-field layer call is not supplied. |
| U32 | II 52107–52186 | Partial: the identity theorem in the block variables on the common physical domain. It gives no independent-current or arbitrary-switch extension. |
| U33 | II 52390–52469 | Not discharged: the required uniform full-norm comparison includes (B4); kernel/base variation is not a same-kernel consequence of the admitted input. |
| U34 | III 49210–49230; 49272–49288; 49454–49502 | Partial: restriction and zero-component reasoning with complete boundary stencils. Uniform admission of the localised response remains conditional. |

Thus **U15's specified layer inference is covered**. The explicitly listed
parts of the other calls are now justified at their limited scopes.
No additional U01–U34 invocation is claimed covered in full by a uniform
general theorem.

In the requested clause order, the **first unproved sufficient input for
this proof** is the uniform actual-chart realization in (a). More precisely,
the contraction proof would close with common \(r_z,r_X,\varepsilon>0\),
independent of mesh, volume,
admitted base and determining set, with the following two properties for the
actual tagged operators and the general datum convention:
\[
\begin{array}{ll}
 \Phi_{K,A'}(X)=C_\sigma(\ell A'-\ell HX):
 &B_{r_X}\longrightarrow B_{r_X},\qquad
   \operatorname{Lip}_X\Phi_{K,A'}\leq\tfrac12
   \quad(N(A')\leq2r_z),\\[2pt]
 \Psi_{K,d}(z)=-Tj+G\Theta_JH_0b-GV'_\sigma(z+H_0b):
 &B_{r_z}\longrightarrow B_{r_z},\qquad
   \operatorname{Lip}_z\Psi_{K,d}\leq\tfrac12
   \quad(\|d\|_{\mathrm{dat},1}\leq\varepsilon).
\end{array}                                             \tag{G}
\]
The closed balls must lie in the actual analytic operator domain, and
\(\|H_0b\|\leq r_z\). This is a sufficient contraction premise, not a
necessary condition for every possible existence proof.
Section (a) proves it locally at each finite
analytic kernel; it does not prove common radii or identify a different
first-argument convention with (S5). Calling (B4) the first unfinished
step of the entire theorem would therefore be inaccurate.

The **stopping lemma tested by three distinct attacks** is \(R_\Delta\),
equation (B4), for the full-norm upgrade of furnished solutions at the
actual complex completion kernels. The three failed attacks are:
the lifting equation (B6); first-order
operator bounds plus analytic/weighted control, tested by (B7)–(B9); and
transfer from the second response system (B10).
This is a stopping lemma, not a no-go theorem for the actual kernels.
Proving it would remove this particular obstruction. It would not by itself
prove (G). Neither conclusion is hidden in the word “furnished”.

All calculations here are symbolic arguments. No numerical run, computer
algebra calculation, test count or source search discharges a mathematical
step. No registry, audit status or other repository file is changed.

RESULT: partial proof; finite-kernel extensions and the repaired cut-current commutator are proved, U15's layer inference is covered conditional on CA-LAYER/(N1), the first unproved uniform prerequisite is (G), and the full-Laplacian stopping lemma R_Delta (B4) remains unproved after three distinct attacks.
