# A1: the regular constrained critical orbit
Provenance: Codex (GPT-6; exact model variant and runtime effort setting not exposed), requested effort max; checkout `db05f4037b3a033e4e6582ecad71a45b88f64871`; Sussman–Alpoge outline `31a47c543775`; research text, not an audit, and no status granted.

**Full A1: STOPPED at the session budget.** Section 8 proves the
single-lattice statement for each fixed finite geometry, real first and
then holomorphic, with geometry-dependent constants and radii.
Section 7.4 also constructs an exact curved family with depth-independent
regularity bounds and a one-parameter holomorphic radius.

## 1. Target and sources

This is queue row 79, targeting item 1 of `sa-ledger.md`: obligation A1 and
Theorem 1 of (1b), together with the holomorphic representative required by A1.
The first attack is a real regular datum with inequivalent regular critical
configurations. A counterexample must obey the actual constraints and
regularity tests, including the treatment of global holonomies and seams.
If this attack fails, the task is existence and uniqueness with constants
independent of depth, followed by holomorphic continuation. No numerical or
machine-assisted step can discharge any assertion here.

The outline and its constructions are credited to Ethan Sussman and Levent
Alpoge, with Claude and Codex as authors of their text. The variational and
multiscale background constructions are credited to Tadeusz Balaban and
J. Dimock wherever used below. Literature results are not treated as proved
merely because they are cited. The source reading and mathematical
arguments are recorded below.

## 2. The statement actually under attack

Use the outline's (1b), lines 9593–9667. In level-\(k\) units the bare mesh is
\(\eta=L^{-k}\), level \(j\) has spacing \(\xi_j=L^{j-k}\), and
\(\Omega_0\supset\cdots\supset\Omega_k\), \(\Omega_{k+1}=\varnothing\),
are cubical regions with gaps exceeding \(\rho\xi_j\). The determining
bonds \(\Gamma_j\) have an endpoint in \(\Omega_j\) and no endpoint in
\(\Omega_{j+1}\); inward bonds are omitted in the construction's default
convention. The constraint and action are

\[
 M_{\mathbf B}(U)=(\mathcal M^jU|_{\Gamma_j})_j=\mathbf V,
 \qquad S(U)=\sum_{p\subset\Omega_0}a_p(U).
\]

Residual gauges are the identity at the endpoints of the determining bonds.
Regularity means
\[
 |U_p-1|<\varepsilon\eta^2\mathsf L(p)^{-2},\qquad
 |J(U)(b)|<\varepsilon\mathsf L(b)^{-3}.
\]
Datum regularity tests plaquettes with the finer-layer averages substituted
on seam edges; kept inward bonds require the additional pinch tests. The
torus floor excludes wrapped double blocks. Theorem 1 asserts one nonempty
regular critical residual orbit, with both bounds linear in the datum's
test radius. Theorem 3 continues its comb representative on a full complex
datum ball. These are stronger than an unrestricted minimum or a theorem
on flat data alone.

Theorem 1 is consumed by restriction in Theorem 6(b), by the real estimates
in Theorem 5 and its continuation argument (outline lines 9795, 9911), and
by the interpretation of backgrounds in later RG steps. In particular the
restriction proof at line 9913 needs extension of admissible variations;
uniqueness alone would not prove that identity. Theorem 4's response and
Theorem 6(c)'s comparison concern more than existence of an orbit.

## 3. Literature and local inputs read

The prior wide search is `lit-large-field.md`, Section 3. The targeted
search here retrieved [Dimock, *Multiscale block averaging for QED in
d=3*, arXiv:1712.10029v3](https://arxiv.org/abs/1712.10029), directly from
arXiv as TeX, kept only under `/tmp`. Section 3.6 constructs restricted
axial/Landau gauges and the quadratic constrained minimizer; Section 3.7.2
represents it as
\[
 H=GQ^T(QGQ^T)^{-1}.
\]
Its random-walk discussion obtains depth-independent estimates from local
inverses. At the local-inverse step it explicitly refers to Balaban for
details; this is not a self-contained derivation of that estimate. Section
3.9's regularity theorem also explains why the single-scale identity used
in an earlier argument fails for multiscale averaging. These constructions
and the minimizer formula below are credited to Dimock and Balaban.

Balaban's [*The variational problem and background fields in
renormalization group method for lattice gauge theories*, CMP 102 (1985),
277–309](https://doi.org/10.1007/BF01229381) is the relevant nonabelian
predecessor. The old Michigan PDF URL returned the new repository's HTML
shell, not the paper; its bibliographic abstract supplies no proof here.
The follow-up handle fetch returned HTTP 403, and Springer offered only
subscription access. Retrieval stopped at those access barriers.
The outline was fetched once at the specified revision. Its A1, (1b)
Theorems 1–6 and proof mechanisms 1–5, 8 and 9 were read in bounded excerpts,
as were the pointed-window datum requirement at 13439–13455 and the
later background/failed-test uses at 17678–17691.
All constructions taken from it retain the Sussman–Alpoge/Claude/Codex
credit in Section 1.

For our inputs, Lemma U and the starting-box repair in
`gates/share-check-199fac1cb.md` (c) give a real small-total-energy box
gauge. The Sobolev input is Section 1 of
`lattice_sobolev_box_gauge.md`, credited there to Gagliardo, Nirenberg,
Loomis and Whitney; its later union-of-cells claim based on enumeration is
not used. In `c0-loc.md`, Sections 7–10 and the input boundary in Section
11 require the admitted read boxes, top collars, and actual stationary
class map. They do not construct the outline's orbit. None of these
source labels is used as mathematical evidence in the direct arguments
below.

The same step was also read in the outline authors' manuscripts at the
same commit: `QED3/QED3.tex`, the photon Landau minimizer at lines
4335–4400, and `YM3/YM3_I.tex`, the regular-orbit uniqueness argument at
29970–30285. The former uses quadratic minimization modulo restricted
gradients. The latter first aligns the contour variables, then normalizes
one level at a time and resets a slice bound after each rescaling. That
reset, not an iteration of an arbitrary local implicit-function radius,
is the mechanism that would have to survive in four dimensions.

## 4. Flat data: the holonomy counterexample does not work

**Proved smaller statement.** Fix a finite compatible four-torus, odd
\(L\), and depth \(k\), with nonwrapping blocks, and take
\(\Omega_j=T\) for \(0\le j\le k\). For every flat coarse
\(SU(2)\) datum \(V\), there is exactly one *flat* residual orbit in
\(\{U:\mathcal M^kU=V\}\). It has a representative given by an explicit
continuous formula, with curvature and current identically zero. The
formula is holomorphic on the variety of flat \(SL(2,\mathbb C)\) data.
Here “flat” means every elementary plaquette product is the identity;
no assumption on the torus holonomies is made. This statement does not
assert that every regular critical orbit is flat.

**Construction.** Put \(s=L^k\) in bare lattice units and partition the
sites into the centered blocks \(P_y=B^k(y)\). Define the lift \(\mathcal L V\)
by identity links inside each \(P_y\), and by \(V(y,y+se_\mu)\) on
every positively oriented fine link crossing that common block face.
Use inverse values on reversed links. This is the lift of the outline
at line 7129, credited to Sussman–Alpoge/Claude/Codex and Balaban; the
claims needed here are verified next.

An elementary fine plaquette meets one, two, or four of these blocks.
In one block its product is 1. Across just one block face its two
crossing factors are \(V(c)\) and \(V(c)^{-1}\), so its product is 1.
At the intersection of two block faces its product is precisely the
corresponding coarse plaquette product, based in the same block.
Thus \(V\) flat implies \(\mathcal LV\) flat.

For completeness, the lift is an exact section of the *iterated* average,
not only of an average taken in a single stroke. Centered blocks are
nested because \(L\) is odd. At an intermediate level \(n<k\), every
level-\(n\) block lies in one \(P_y\). For a link between two such blocks,
all the paths in the averaging formula stay in one \(P_y\), or cross
one face between a fixed pair \(P_y,P_{y'}\). Their transports are
respectively 1 or the same \(V(y,y')\). Both endpoint contour transports
are 1. Consequently every closed factor \(W_x\) in the outline's
formula at lines 7072–7078 is 1, and the average equals its straight
transport. Applying this observation successively at \(n=0,\ldots,k-1\)
gives
\[
                     \mathcal M^k\mathcal LV=V.                 \tag{4.1}
\]
In fact (4.1) holds for arbitrary \(V\): a double block used by one row
sees only that pair of blocks, where the lifted field is flat. Plaquettes
at intersections of four large blocks are outside that double block.
No mean or logarithm of widely separated group elements occurs in this
verification.

**Uniqueness of the flat orbit.** In a rectangular block, the transport
of a flat field between two sites is path independent. Here is the
elementary justification. Project each vertex \(x\) to \(\pi x\) on
the box's lower face in its last coordinate, and let \(P_x\) be the
transport on the straight last-coordinate path from \(\pi x\) to
\(x\). For a transverse edge \(e=(x,x')\), multiplying the
plaquette identities in the strip between \(e\) and \(\pi e\)
gives \(P_xU(e)=U(\pi e)P_{x'}\); all intermediate strip edges
cancel. For a last-coordinate edge the same identity holds with
\(U(\pi e)=1\), by the definition of \(P_x\). For any loop,
these identities cancel the successive \(P_{x'}P_{x'}^{-1}\)
and express its transport as a conjugate of the projected loop's
transport. Repeat on the lower-dimensional face. In dimension one
only backtracks remain, and their factors cancel. The loop transport
is therefore 1. Apply this to a path followed by the reverse of a
second path to obtain path independence. Every strip stays in the box.

For a flat fine \(U\), choose a tree in each \(P_y\), rooted at \(y\),
and put \(g(x)=U(\gamma_{y,x})\), \(g(y)=1\). With the convention
\(U^g(x,x')=g(x)U(x,x')g(x')^{-1}\), path independence makes
every internal link of \(U^g\) the identity. For adjacent crossing
links along a block face, the fine plaquette between them has its two
tangential links internal to the blocks, hence equal to 1. Flatness
makes the crossing values equal. The face is a connected rectangular
grid; moving one transverse coordinate at a time proves that its value
is a single matrix \(W(c)\). Thus \(U^g=\mathcal LW\).
The gauge is residual, since it is 1 at every coarse node. Gauge
covariance and (4.1) give
\[
                  W=\mathcal M^kU^g=\mathcal M^kU=V.
\]
This also proves that the residual gauge fixing is unique: a residual
gauge preserving identity on the internal tree must equal its root
value 1 at every vertex.

Flat configurations are critical even before constraining: at an
identity plaquette the first variation of
\(1-\tfrac12\operatorname{tr}U_p\) is zero because every tangent
matrix has trace zero. Their current is therefore zero. The lift uses
only entries of \(V\), the identity, and inversion; it is continuous
and hence Borel. The same formulas and the same cancellation proof
hold for complex matrices of determinant one, and are holomorphic.
Finally the lift already satisfies the outline's hierarchical comb
gauge: every contour at every level below a pillar top stays within
that pillar and has transport 1. This completes the smaller statement.

In particular, taking commuting constant fine links with \(s\)-th
powers equal to 1 does not produce distinct orbits over \(V=1\).
They are flat, and the construction above supplies the residual gauge
that removes them. Nontrivial torus holonomies instead appear in the
prescribed coarse links and are retained by (4.1).

## 5. The real critical point near a fixed flat datum

**Proved smaller statement, with finite-geometry constants.** In the
single-lattice geometry of Section 4, fix a real flat datum \(V_0\).
There are positive radii \(r,\delta\), allowed to depend on that finite
torus and \(k\), such that each real datum
\(V(b)=e^bV_0\), \(\|b\|<r\), has exactly one constrained critical
residual orbit whose forest-gauge representative is within \(\delta\)
of \(U_0=\mathcal LV_0\). It is regular when \(r\) is made smaller.
Its representative is real analytic. Section 6 proves its continuation
on a full complex ball. The forest is used only to prove this local
statement; an exact conversion to the outline's comb gauge is given
there.

Here \(b_c\in\mathfrak{su}(2)\) is anti-Hermitian, so \(e^b\) replaces
the outline's \(e^{iB}\). Set
\(\langle X,Y\rangle=-\tfrac12\operatorname{tr}(XY)\) on the real
Lie algebra and use orthonormal real coordinates on its copies. All
norms in this section are Euclidean norms on the indicated finite
spaces. Their complexifications use the associated Hermitian norm for
estimates, but analytic transposes remain bilinear transposes.

### 5.1 An actual chart and a surjective constraint derivative

In each pillar choose a spanning tree rooted at its top. For any field,
the gauge \(g(x)=U(\gamma_{y,x})\) sets its tree links to 1 and is the
identity at the top. This works without flatness: the tree has exactly
one root path to each vertex. Such a representative is unique, since
the successive tree edges force every residual gauge value from the
root value. The gauge map uses finitely many matrix products and
inverses and is analytic. It preserves \(\mathcal M^kU\) wherever the
averages in this chart are defined.

The covariance used here follows from the actual formulas. A path
transport gains the gauge factors at its two endpoints. For a contour
mean, \(V_i\mapsto hV_i\widetilde h\) sends its candidate mean to
\(hV\widetilde h\): each defining logarithm is conjugated by \(h\).
The logarithm series commutes with that conjugation on the common
small branch. Uniqueness of the small mean proves its covariance.
Each \(W_x\) is then conjugated at the left endpoint, so the
exponential formula for \(\mathcal M\) has the same endpoint
covariance. Iteration proves it for \(\mathcal M^k\). The endpoint
factors are 1 for a residual gauge. For complex gauges we use only
the sufficiently small neighborhood of the real flat field, so both
sides remain on the branch just described.

Write fields in that slice as
\[
 U(a)_e=e^{a_e}(U_0)_e\quad(e\text{ not in the forest}),\qquad
 U(a)_e=1\quad(e\text{ in the forest}).
\]
For \(a\) small these are coordinates: on each free link the inverse is
\(a_e=\log[U_e(U_0)_e^{-1}]\). The matrix logarithm is its convergent
series \(\sum_{n\ge1}(-1)^{n+1}(W-1)^n/n\) for \(\|W-1\|<1\).
It takes values in the complexified traceless algebra near the identity.
To see the trace assertion, along any sufficiently small matrix path
\(W(t)\in SL(2,\mathbb C)\), differentiating the logarithm's trace
gives \(\operatorname{tr}(W^{-1}W')\), the derivative of
\(\log\det W\), which is zero; both traces start at zero.

The actual averages are analytic in this neighborhood. This includes
the contour mean (credited to Federbush by the outline): when its
arguments are near a common matrix, write
them as \(e^{Z_i}W_*\) and its value as \(e^YW_*\). The defining
equation becomes
\[
 n^{-1}\sum_i\log(e^{Z_i}e^{-Y})
       =n^{-1}\sum_i Z_i-Y+R(Z,Y)=0.
\]
The logarithm series shows that \(R\) is analytic and has zero value
and derivative at the origin. Fix a small \(Y\)-ball of radius
\(\rho\) and sufficiently small \(Z_i\) so that the
\(Y\)-derivative has norm below \(1/2\). Reduce the \(Z_i\) radius
further so that \(\|n^{-1}\sum_iZ_i+R(Z,0)\|\le\rho/2\).
The map \(Y\mapsto n^{-1}\sum_iZ_i+R(Z,Y)\) then maps the
closed \(\rho\)-ball into itself and contracts by \(1/2\).
Iteration converges, by the geometric error bound, to a unique small
mean. The holomorphic-limit argument is
written in Section 6 below and applies here as well. At \(U_0\) every
contour family has coincident transports, so this argument applies to
each mean. The remaining operations are products, exponential series,
and logarithm series near 1. There are finitely many such operations
for this fixed \(k\), so shrinking one neighborhood makes all of them
defined throughout it.

Define the constraint coordinate
\[
 C(a)_c=\log\big[(\mathcal M^kU(a))(c)V_0(c)^{-1}\big],\qquad
 Q=DC(0),\qquad C(0)=0.
\]
Let \(E\) be the space of the free fine-link coordinates and \(D\)
the space of coarse-link coordinates. Define \(T:D\to E\) by putting
\((Tb)_e=b_c\) on all fine links crossing face \(c\), and zero on
internal links. The exact lift identity (4.1) says
\[
                   C(Tb)=b,\qquad QT=I_D.                    \tag{5.1}
\]
Thus the actual constraint derivative is surjective. This does not
replace it by a straightened or comb average.

### 5.2 Positivity on the fibre, proved without a spectral estimate

Take the Wilson normalization
\(S(U)=\sum_p(1-\tfrac12\operatorname{tr}U_p)\) on real \(SU(2)\)
fields; the trace is real there. A positive fixed prefactor would not
change any critical point. At the flat \(U_0\), write the first
variation of a plaquette as
\(\log U_p(ta)=t(d_{U_0}a)_p+O(t^2)\). Products differentiated once
give exactly the transported oriented sum \(d_{U_0}a\).
Since the logarithm is traceless, expansion of its exponential gives
\[
 S(U(ta))=\tfrac12t^2\sum_p\|(d_{U_0}a)_p\|^2+O(t^3),
 \quad DS(0)=0,\quad
 \langle a,Ha\rangle=\|d_{U_0}a\|^2,\quad H=D^2S(0).          \tag{5.2}
\]

Suppose \(Qa=0\) and the last expression vanishes. On each pillar
\(U_0=1\), so \(da=0\) there. The additive version of the path
interchange proof of Section 4 says that the sum of \(a\) from the
root to a vertex is path independent. On the tree that sum is zero,
because the tree coordinates are zero. It follows that every internal
link coordinate is zero. For two adjacent crossing links on a face,
the linearized fine plaquette now reads \(a_e-a_{e'}=0\): its
tangential variations vanish and its two crossing background links
are the same \(V_0(c)\). Hence each whole face has one coordinate
\(b_c\), and \(a=Tb\). Equation (5.1) then gives \(0=Qa=b\), so
\(a=0\). We have proved
\[
             \ker H\cap\ker Q=\{0\}\quad\text{in the slice}.   \tag{5.3}
\]
Consequently \(H\) is positive definite on \(\ker Q\). This conclusion
uses no bound on a Fourier symbol and no numerical eigenvalue. A
positive finite-geometry lower bound exists: the continuous function
\(\|d_{U_0}a\|^2\) has a minimum on the unit sphere in \(\ker Q\);
a zero minimum would contradict (5.3). If that kernel has dimension
zero, the positivity assertion is vacuous and the arguments below
still apply.

This also rebuilds the quadratic minimizer algebra used by Balaban and
Dimock. Put
\[
 P=H+Q^TQ,\quad G=P^{-1},\quad N=(QGQ^T)^{-1},\quad H_{\rm min}=GQ^TN.
                                                                    \tag{5.4}
\]
By (5.2)–(5.3), \(\langle a,Pa\rangle>0\) for \(a\ne0\), so \(G\)
exists and is positive. By surjectivity of \(Q\), \(Q^Tz\ne0\) for
\(z\ne0\), and \(\langle z,QGQ^Tz\rangle>0\); thus \(N\) exists.
Equation (5.4) gives \(QH_{\rm min}=I\) and
\(HH_{\rm min}=Q^T(N-I)\). For any \(q\in\ker Q\), expansion yields
\[
 \tfrac12\langle H_{\rm min}b+q,H(H_{\rm min}b+q)\rangle
 =\tfrac12\langle H_{\rm min}b,HH_{\rm min}b\rangle
    +\tfrac12\langle q,Hq\rangle.
\]
The cross term vanishes because \(Qq=0\); the last term is positive
unless \(q=0\). This proves existence and uniqueness of the quadratic
constrained minimizer. Formula (5.4) is its real linear, hence entire
complex, representative. No depth-independent bound for these matrices
has been inferred from their invertibility.

### 5.3 Solving the nonlinear real problem

Use the saddle equations
\[
 \mathcal F(a,\lambda;b)
   =\begin{pmatrix}\nabla S(a)-DC(a)^T\lambda\\ C(a)-b\end{pmatrix}=0.
                                                                    \tag{5.5}
\]
At \((a,\lambda,b)=0\) their derivative in \(z=(a,\lambda)\) is
\[
            K=\begin{pmatrix}H&-Q^T\\ Q&0\end{pmatrix}.
\]
If \(K(a,\lambda)=0\), pairing its first equation with \(a\) and using
its second gives \(\langle a,Ha\rangle=0\). Equation (5.3) forces
\(a=0\); then \(Q^T\lambda=0\) and (5.1) forces \(\lambda=0\).
This square finite matrix is injective and therefore invertible
(its columns are a basis). Set \(M=\|K^{-1}\|\).

Let \(\mathcal N(z)=\mathcal F(z;0)-Kz\). It is analytic,
\(\mathcal N(0)=0\), and \(D\mathcal N(0)=0\). Choose \(R>0\) with
the closed complex \(R\)-ball inside the chart and
\[
           \sup_{\|z\|\le R}\|D\mathcal N(z)\|\le (2M)^{-1}.
                                                                    \tag{5.6}
\]
Such an \(R\) exists by continuity. For \(\|b\|<R/(4M)\), consider
\[
           z_{n+1}=K^{-1}(0,b)-K^{-1}\mathcal N(z_n),\qquad z_0=0.
                                                                    \tag{5.7}
\]
The line-segment integral of \(D\mathcal N\) gives a Lipschitz
constant \(1/2\) for the right side. It maps the closed \(R/2\)-ball
to itself: its two terms have norms at most \(R/4\) and \(R/4\).
Successive differences satisfy
\(\|z_{n+1}-z_n\|\le2^{-n}M\|b\|\), so their series converges.
The limit solves (5.5), and subtraction of two fixed-point equations
proves uniqueness in the \(R\)-ball. Indeed any fixed point in that
ball satisfies \(\|z\|\le M\|b\|+\|z\|/2\), hence already lies in
the \(R/2\)-ball. The useful bound is
\[
                         \|z(b)\|\le2M\|b\|.                  \tag{5.8}
\]
For real \(b\), every term of (5.7) is real in the chosen coordinates;
its limit is therefore real.

We check that this is uniqueness of critical points, not just of
chosen multipliers. From (5.1), \(DC(a)T\) is close to \(I\) for
small \(a\); when the difference has norm below \(1/2\), its inverse
is the convergent geometric series. Thus \(DC(a)\) is surjective.
Every \(v\in\ker DC(a)\) is tangent to a curve in the actual level
set: put \(T_a=T[DC(a)T]^{-1}\), and solve
\(C(a+tv+T_au)=C(a)\) for \(u\) by iteration after subtracting its
linear term \(u\). The derivative of the remaining term in \(u\)
is zero at \((t,u)=(0,0)\), so the same small-ball contraction works.
Differentiating at zero gives \(u'(0)=0\). Conversely differentiation
of any level-set curve gives \(DC(a)v=0\).

Consequently a critical point has
\(\nabla S(a)=DC(a)^T\lambda\): the orthogonal complement of the
kernel of a surjective matrix is the range of its transpose, as
follows by taking an orthonormal basis of that kernel and completing
it to a basis. Its unique multiplier is
\[
 \lambda=[DC(a)DC(a)^T]^{-1}DC(a)\nabla S(a).
\]
This expression is continuous near zero, with norm at most
\(C_1\|a\|\), because \(\nabla S(0)=0\). Choose
\(\delta>0\) so small that \(\|a\|<\delta\) implies
\(\|(a,\lambda)\|<R\) and the preceding surjectivity bounds hold.
Then reduce \(r\) below both \(R/(4M)\) and \(\delta/(2M)\).
Every critical point in that field neighborhood is the solution of
(5.7). Finally, gauge-fix any curve in the full constrained set by the
tree formula. It becomes a curve in the slice with exactly the same
action values, since plaquette traces are gauge invariant. Thus
stationarity in the slice is equivalent to stationarity in the full
constraint set. The unique forest representative identifies its
residual orbit, proving the real existence and uniqueness claimed at
the start of Section 5.

## 6. Holomorphic continuation of that finite-geometry result

The complex action in this chart is
\(S_{\mathbb C}(U)=\sum_p(1-\tfrac12\operatorname{tr}U_p)\).
It is holomorphic on \(SL(2,\mathbb C)\) link fields, is invariant
under complex gauges, and restricts to the real Wilson action on
\(SU(2)\). Hence (5.5) is its holomorphic Lagrange system, with
bilinear transposes. All statements (5.6)–(5.8) were established on
complex balls, not by assuming that real positivity extends to complex
quadratic forms.

Every iterate in (5.7) is holomorphic in \(b\). The geometric error
bound is uniform on every closed smaller datum ball, so its limit is
holomorphic. One can check that last step directly: choose a closed
polydisc strictly inside the datum ball, apply the one-variable Cauchy
integral formula successively in its coordinates to each iterate, and
pass the uniform limit through the finitely many integrals. The limit
then has the same convergent interior power-series representation as
the iterated Cauchy formula, proving holomorphicity. The same proof
justifies the mean construction in Section 5.1.

Here is the promised conversion to the *actual hierarchical comb
representative*. Set \(W_n=\mathcal M^nU(a(b))\). Start with
\(g_k(y)=1\) on the coarse nodes. Descend through
\(n=k-1,\ldots,0\): for \(x\in B(z)\) on the level-\(n\) lattice,
with parent \(z\) at level \(n+1\), put
\[
            g_n(x)=g_{n+1}(z)W_n(\Gamma_{z,x}).                \tag{6.1}
\]
At \(x=z\), the path is empty, so these definitions agree on nested
lattices. They define one gauge \(g_0\), equal to 1 at the original
nodes. Gauge covariance of each averaging step gives
\[
 (\mathcal M^nU^{g_0})(\Gamma_{z,x})
       =g_n(z)W_n(\Gamma_{z,x})g_n(x)^{-1}=1.
\]
Thus
\[
                  \Phi_{V_0}(b)=U(a(b))^{g_0(b)}              \tag{6.2}
\]
is the outline's comb representative. At \(b=0\), all the contours
in (6.1) are internal to a pillar and have value 1. All \(g_n\) are
therefore 1 there, and are holomorphic nearby. Shrink the finite datum
ball once more if necessary so that every complex average before and
after this gauge change remains in the same analytic branch. This is
possible because there are finitely many rows, they are in the branch
at zero, and every defining expression is continuous. No assertion of
a uniform radius is used in this step.

The comb representative of an orbit is unique. Indeed a residual
gauge relating two such representatives is 1 at the tops. At level
\(k-1\), covariance of the identity comb transports forces its value
at every child to equal its parent value, hence 1. Applying this
argument at \(k-2\), then each lower level, proves it is 1 at every
bare site. This is an exact group argument, valid for complex matrices
as well.

Equations (5.5), (6.1), and covariance show that (6.2) has the prescribed
averages and is a constrained complex critical point. It is real for
real \(b\) by the real iteration and real gauges. Any holomorphic map
agreeing with this real representative has the same Taylor coefficients:
its difference has all mixed derivatives in real coordinate directions
zero on the real ball, and for holomorphic functions these are the
complex Taylor coefficients. The difference is consequently zero near
zero, and then on the connected ball by overlapping Taylor discs.
This proves uniqueness of the holomorphic continuation claimed here.

Curvature and current are holomorphic functions of these finitely many
links and inverses. They vanish at zero. On a closed smaller ball their
first derivatives have a finite maximum; integrate those derivatives
along \(t\mapsto tb\) to obtain
\[
 \max_p\eta^{-2}|\partial\Phi_{V_0}(b)(p)-1|
       +\max_e|J(\Phi_{V_0}(b))(e)|
          \le C_{T,k,V_0}\|b\|.                              \tag{6.3}
\]
This proves real and complex regularity after reducing the datum
radius to meet any chosen fixed small regularity threshold. The real
representative is continuous and therefore Borel.

For a *fixed* finite geometry these radii and constants can even be
chosen uniformly over all real flat \(V_0\). The flat datum set is a
closed subset of a finite product of compact \(SU(2)\)'s, hence
compact. The lift, all the finite chart derivatives, and \(K\) depend
continuously on \(V_0\). Each \(K\) is invertible by Section 5.2;
the adjugate formula makes \(K^{-1}\) continuous. Its norm has a finite
maximum on this compact set. The analytic branch neighborhoods and
derivative bounds admit a finite subcover, so their minimum radii and
maximum constants are positive and finite, respectively. This removes
dependence on the flat holonomies for fixed geometry. It does not
remove dependence on depth, volume, or the norm conversion in (6.3).

## 7. Attack on depth uniformity

### 7.1 An exact growing constant in the gauge just used

The following is a configuration, not an estimate guessed from matrix
size. Keep the coarse torus fixed, with its side exceeding the outline's
floor, and let \(s=L^k\) increase. Fix
\(Z=\operatorname{diag}(i,-i)\), \(\|Z\|=1\), and prescribe
\[
               V_1(y)=e^{tZ},\qquad V_\mu(y)=1\ (\mu>1).
                                                                    \tag{7.1}
\]
This datum is flat. In the forest and hierarchical comb gauges its
flat representative is exactly \(\mathcal LV\). At \(t=0\), its
derivative has value \(Z\) on every fine link crossing a coarse
1-face, and zero elsewhere. Each such face has exactly \(s^3\)
crossing links. Therefore, with the counting Euclidean norms used in
Sections 5–6,
\[
        \|\partial_t a(0)\|_2=s^{3/2}\|\partial_t b(0)\|_2.    \tag{7.2}
\]
The derivative is the quadratic minimizer of (5.4), since its curvature
is zero and (5.3) proves uniqueness in that fibre. It solves
\(K(\partial_ta,0)=(0,\partial_tb)\). Thus
\(\|K^{-1}\|\ge s^{3/2}\) in those norms. Finite-dimensional
invertibility in that gauge cannot provide the depth-independent
constant needed in the weighted norm of A1.

This is **not a counterexample to A1**. Its scale-correct Landau form is
explicit and has uniform bounds. In level-\(k\) units put
\[
 U^{\rm L}_1(x)=e^{tZ/s},\quad U^{\rm L}_\mu(x)=1\ (\mu>1),
 \qquad H_1=tZ,\quad H_\mu=0\ (\mu>1).
\]
It is flat and \(\mathcal M^kU^{\rm L}=V\), since the nonwrapping
transports used in each averaging row agree. Its divergence and all ordinary
first differences vanish, so it satisfies the flat Landau condition.
For \(x\in P_y\), measure \(x-y\) in unwrapped **bare integer
coordinates** in that pillar, and set
\[
                    u(x)=e^{t(x_1-y_1)Z/s}.                   \tag{7.3}
\]
Internal links transform to 1. Across a 1-face, the exponents in
\(u(x)U^{\rm L}(x,x+e_1)u(x+e_1)^{-1}\) sum to \(tZ\);
across any other face they cancel. Hence
\((U^{\rm L})^u=\mathcal LV\), with \(u=1\) at the tops.
The mean displacement in every centered block is zero, so every
one-step node factor of this constant Cartan field is also 1.
For complex \(|t|<r\le1\), the exponential series and
\(|x_1-y_1|/s<1/2\) give
\[
       \sup_x\|u(x)-1\|\le (|t|/2)e^{r/2},\qquad
       \|H\|_X=|t|,\qquad \partial U^{\rm L}=1,
       \quad J(U^{\rm L})=0.                                 \tag{7.4}
\]
Thus the apparent growth in (7.2) is removed by the very Landau-pair
mechanism distinguished in the outline. It cannot be used to declare
the background foundation false. Equations (7.1)–(7.4) close this
specific proposed depth counterexample, in both real and complex data.

### 7.2 The exact section is not a uniformly regular seed

A second possible shortcut is false. On the same coarse torus set
one coarse link \(c\) to \(e^{tZ}\),
\(0<t<\min\{1,\bar\varepsilon/2\}\), and every other link
to 1. Every coarse plaquette is 1 or \(e^{\pm tZ}\). With the operator
norm, their maximum error is
\[
                  q(t)=2\sin(t/2),\qquad t/2\le q(t)\le t.
\]
The upper inequality follows by integrating \(\cos u\le1\).
For the lower one, \(\cos u\ge1-u^2/2\ge1/2\) on
\([0,1/2]\), so integration gives \(\sin(t/2)\ge t/4\).
Take any datum radius slightly larger than \(q(t)\); the datum is
regular with that radius at every depth.

There is a coarse plaquette incident to \(c\) and a fine plaquette
at the intersection of its two block faces. By the explicit computation
in Section 4, that fine plaquette of \(\mathcal LV\) has the same
error \(q(t)\), not \(q(t)/s^2\). In level-\(k\) units its
scale-normalized curvature is therefore
\[
                 \eta^{-2}|(\mathcal LV)_p-1|=s^2q(t).        \tag{7.5}
\]
For any fixed regularity radius, choose \(k\) so large that the
right side exceeds it. This is an explicit refutation of using the
exact section \(\mathcal L\) as a regular seed with uniform constants.
It is not a refutation of A1, which asks for a critical orbit, and does
not assert that this discontinuous-in-space lift is that orbit.

The next attempted repair is to replace \(\mathcal L\) by the quadratic
minimizer and solve the nonlinear equations in the scale-weighted Landau
norm. The finite formula (5.4) proves that the quadratic minimizer
exists, but (7.2) shows why it must first be put in the appropriate
gauge. The reset described in the outline's mechanism 3 and the
corresponding YM3 argument is doing mathematical work at precisely
this point; it cannot be replaced by the Euclidean inverse used above.

### 7.3 What the small-energy box gauge does give at this step

This checks the hypothesis needed to use our Lemma U, rather than
assuming that pointwise smallness implies a volume-free energy bound.
In a single layer let the local physical scale be \(\xi\), and let a
comparable-sided read box have at most \(N+1\) sites in each direction,
where \(N=\xi/\eta\ge1\) is an integer. Suppose
\(|U_p-1|\le\varepsilon N^{-2}\) on its plaquettes. Write its
principal plaquette angle as \(\theta_p\), with \(\varepsilon\) small
enough to stay in the angle ball. The identity
\(|e^{i\theta}-1|=2|\sin(\theta/2)|\), and
\(\sin u\ge2u/\pi\) on \([0,\pi/2]\), give
\(|\theta_p|\le2\varepsilon N^{-2}\). There are at most
\(6(N+1)^4\le96N^4\) plaquettes, so
\[
                         \|\theta\|_2\le20\varepsilon.       \tag{7.6}
\]
Thus \(20\varepsilon\le\varepsilon_0\) meets Lemma U's energy
threshold independently of depth. With its unit-cube seed repair,
that already-written proof provides a real Coulomb box gauge with
\(\|a\|_4+N^{-1}\|a\|_2\le20C_U\varepsilon\) and
\(\|\nabla a\|_2\le40\varepsilon\). On a box of side at most
\(mN\), the identical count costs \(m^2\), not a factor depending
on \(N\). This legitimately supplies a local real starting gauge
on a read box contained in one layer. The calculation does not apply
across an unrelated finer layer at the coarser scale.

It also does not give the required scaled supremum norm by dropping
the fourth norm: \(\sup|a|\le\|a\|_4\) only gives
\(\sup|A|\le20C_U\varepsilon/\eta\) for \(A=a/\eta\).
Moreover the gauge is not fixed at the prescribed nodes. The actual
remaining attack is therefore on a constraint-preserving Landau
correction and its weighted inverse, rather than on the existence of
a logarithm in a real box.

### 7.4. A curved alternating datum: an exact uniform critical family

The raw lift's concentration suggests a sharper attempted counterexample:
alternate a small Cartan datum at the coarse lattice's shortest wavelength
and let the depth grow. The following construction defeats that attempt.
It gives actual constrained critical fields, not just comparison fields.
The averaging and gauge conventions remain those of
Sussman–Alpoge/Claude/Codex; the elementary construction below is derived here.

Take a compatible torus with an even number of coarse sites in direction 1,
large enough to satisfy the outline's nonwrapping floor. Put
\(s=L^k\), \(h=(s-1)/2\), and
\(Z=\operatorname{diag}(i,-i)\). All integer coordinates in this
subsection are bare coordinates. Write the block in direction 1 as
\(B_j=\{js-h,\ldots,js+h\}\). For a scalar parameter \(\gamma\), set
\[
 p_{js+r}=(-1)^j\frac{\gamma}{s^3}(r+\tfrac12),\qquad
 f_i=\arcsin p_i,\qquad
 a_i=-\frac12\sum_{r=i}^{i+s-1}f_r.                         \tag{7.7}
\]
Use the branch of arcsine vanishing at zero. Directly, including at a
block boundary,
\[
 p_i-p_{i-1}=(-1)^j\gamma/s^3\quad(i\in B_j),\qquad
 p_{i+s}=-p_i,\qquad f_{i+s}=-f_i.
\]
The last identity and (7.7) give
\(a_{i+s}=-a_i\) and \(a_{i+1}-a_i=f_i\), so these formulas
are periodic on the stipulated torus. Define
\[
 U_2(x)=e^{a_{x_1}Z},\qquad U_1(x)=U_3(x)=U_4(x)=1.        \tag{7.8}
\]
Its only nonidentity oriented plaquettes are
\(U_{12}(x)=e^{f_{x_1}Z}\). For \(|\gamma|\le1/4\),
\(|p_i|\le|\gamma|/(2s^2)\) and the arcsine power series gives
\[
 |f_i|\le|\gamma|/s^2,\qquad |a_i|\le|\gamma|/(2s).        \tag{7.9}
\]

**Its actual iterated average.** In a common Cartan subgroup, within
the prescribed logarithm branches, a group mean is the exponential of
the arithmetic mean of the angles. At one step the plain angle average
is precisely
\(Q^{\rm pl}a=Q^{\rm s}a+\sigma(c_-)-\sigma(c_+)\),
with \(\sigma\) as in the outline's displayed formula at 7081.
For a field with only component 2 depending on coordinate 1, a contour
from \(y\) to \(x\) has angle
\((x_2-y_2)a(y_1)\) or \((x_2-y_2)a(x_1)\), according to
the order of directions 1 and 2. Its averaged angle is odd in
\(x_2-y_2\). Thus \(\sigma(y)=0\) on a centered block.
The straight average retains only component 2, and sums its angles
over the direction-1 block. Iterating over nested centered blocks
therefore gives, exactly,
\[
 (\mathcal M^kU)_2(y)=e^{b_jZ},\quad
 b_j=\sum_{i\in B_j}a_i=(-1)^j b_0,
 \qquad (\mathcal M^kU)_\mu=1\ (\mu\ne2).                 \tag{7.10}
\]
At level \(n\), the angle is a sum over \(L^n\) consecutive
bare angles. Its plaquette angle is a sum of \(L^{2n}\) of the
\(f_i\), bounded by \(|\gamma|(L^n/s)^2\). Consequently at
every step before the last its curvature is at most
\(2|\gamma|L^{-2}\). Choose once and for all
\(0<\rho\le1/4\), smaller also than one quarter of the fixed
one-step curvature threshold \(c\) in
\(\varpi<cL^{-2}\). Then \(|\gamma|<\rho\) keeps all steps
in that branch. The contour and closed-row angles are bounded by
\(C|\gamma|\): their rectangles have at most \(CL^2\) plaquettes
at the preceding level. Decrease \(\rho\) by this fixed factor
if necessary. These choices are independent of depth and torus size;
they also keep the complex logarithms and means on their local branches.

**The datum is a uniform parameter, not an implicit small quantity.**
Put \(t_s(\gamma)=-b_0\). Its derivative at zero can be evaluated
without a sum left unchecked. Differentiating (7.7) at zero gives,
on \(-h\le i\le h\),
\[
 a_i'(0)=\frac{i^2}{2s^3}-\frac{s^2+1}{8s^3}.
\]
Indeed its difference is \((i+1/2)/s^3\), and
\(a_{h+1}'(0)=-a_{-h}'(0)\) fixes the constant.
Using \(\sum_{i=-h}^h i^2=s(s^2-1)/12\) now gives
\[
 c_s:=t_s'(0)=\frac{s^2+2}{12s^2},\qquad
                     \frac1{12}\le c_s\le\frac14.         \tag{7.11}
\]
For complex \(|\gamma|\le\rho\), differentiating the double
sum in (7.7) and using
\(|(1-z)^{-1/2}-1|\le2|z|\) for \(|z|\le1/4\) yields
\[
 |t_s'(\gamma)-c_s|
 \le\frac{s^2}{2}\frac1{2s^2}
                \frac{|\gamma|^2}{2s^4}
 =\frac{|\gamma|^2}{8s^4}\le\frac{|\gamma|^2}{8}.          \tag{7.12}
\]
The power-series inequality used here follows by summing the positive
binomial coefficients at \(|z|\); at \(1/4\) their sum after
the constant term is less than \(2(1/4)\).
For \(|t|<\rho/24\), solve
\[
 \gamma=c_s^{-1}t-c_s^{-1}[t_s(\gamma)-c_s\gamma].
\]
This maps the closed \(\rho\)-disc into itself: its first term is
at most \(\rho/2\), and integration of (7.12) bounds its second
term by \(\rho^3/2\). Its contraction constant is at most
\(3\rho^2/2\le3/32\). The geometric iteration therefore gives
a unique holomorphic \(\gamma_s(t)\) there, real for real \(t\),
with
\[
                           |\gamma_s(t)|\le16|t|.           \tag{7.13}
\]
Holomorphy follows by the uniformly convergent iteration and the Cauchy
argument in Section 6. Thus (7.10) prescribes the same coarse datum
at every depth:
\(V_2(y)=e^{-(-1)^j tZ}\), \(V_\mu=1\) otherwise.
Its real plaquette size is \(\varepsilon_1=2|\sin t|\).

**Criticality against all constrained variations.** The Wilson action
derivative with respect to the bare Cartan angle at a direction-2
link is
\[
 \sin f_{i-1}-\sin f_i=-(-1)^j\gamma/s^3\quad(i\in B_j).
                                                               \tag{7.14}
\]
The other three components have zero derivative: the two direction-1
contributions cancel by translation invariance in direction 2, and
the remaining plaquettes are flat.

Put a Cartan multiplier \(-(-1)^j\gamma Z\) on every coarse
direction-2 link, constant in coordinates 2, 3 and 4, and zero on
the other directions. Its coarse divergence is zero. Consequently
pairing it with the derivative of the plain average kills the two
\(\sigma\) terms. The adjoint straight average sends it to the
same component, still independent of coordinate 2. To count its
coefficient at one step, fix a fine direction-2 link. There are exactly
\(L\) starting points of length-\(L\) forward segments containing
that link, each with weight \(L^{-4}\); its transverse coordinates
select their unique centered blocks. The resulting multiplier is
\(L^{-3}\) times the coarse one. It again has zero divergence,
so this argument repeats at every level. After \(k\) steps it is
\(-(-1)^j\gamma Z/s^3\) on \(i\in B_j\), exactly (7.14).
This proves the Lagrange identity for every Cartan variation, with no
translation-invariance restriction on that variation.

For variations perpendicular to the Cartan subalgebra, both sides
of the same identity vanish. The action derivative has only a Cartan
component by (7.14). For the average derivative, conjugate by a constant
\(e^{uZ}\): the background is unchanged, the average is covariant,
and its derivative commutes with every such conjugation. The fixed
subspace is the Cartan line, while its perpendicular plane is rotated;
an intertwining linear map cannot send that plane to the fixed line.
The Cartan multiplier therefore pairs to zero with its image. This
also proves the complexified identity. Any curve preserving the group
averages has zero left-trivialized derivative of those averages, so
the identity proves actual constrained criticality of (7.8).

The current normalization in (R1) multiplies (7.14) by
\(\eta^{-3}=s^3\). Hence, in the scalar Cartan identification,
\(J_2=-(-1)^j\gamma\) and the other components vanish. From
(7.9), (7.13), and \(|e^{fZ}-1|\le2|f|\) on this disc,
\[
 \max_p\eta^{-2}|U_p-1|\le32|t|,\qquad
 \max_e|J(U)(e)|\le16|t|.                                 \tag{7.15}
\]
For real \(t\), \(|t|\le\varepsilon_1\) at the chosen radius.
These are therefore uniform linear regularity bounds. The real
potential \(A_2=s a_i Z\), with the harmless conversion to the
outline's Hermitian convention, obeys
\(\|A\|_X\le|\gamma|\) and \(d^*A=0\).

There is also a uniformly bounded holomorphic comb representative.
Apply the recursive comb gauge of Section 6. At level \(n\), an
edge angle is at most \(L^n|\gamma|/(2s)\), and a comb inside
one level block contains at most \((L-1)/2\) direction-2 edges.
All other components are zero. The total angle of the gauge factor
along an ascent is therefore at most
\[
 \frac{(L-1)|\gamma|}{4s}\sum_{n=0}^{k-1}L^n
        =\frac{|\gamma|}{4}(1-s^{-1})\le|\gamma|/4.
\]
It equals 1 at the top nodes. The factor and representative are
holomorphic for \(|t|<\rho/24\), and real-unitary for real \(t\).
Because they remain in the Cartan subgroup, this gauge changes neither
the curvature nor the current in (7.15).

Within the real ansatz with these unwrapped block sums and
\(|a_{i+1}-a_i|<\pi/2\), the solution is unique. For two stationary
angle fields \(a,\tilde a\), pair the difference of their Euler
equations with \(\tilde a-a\). Their block multipliers disappear
because their block sums agree. Summation by parts leaves
\(\sum_i(\sin\tilde f_i-\sin f_i)(\tilde f_i-f_i)=0\).
Every term is nonnegative and vanishes only when
\(\tilde f_i=f_i\), since sine is strictly increasing on that
interval. The difference of the angle fields is then constant, and
its zero block sums make it zero.

This closes the alternating Cartan test, including a curved
one-parameter holomorphic family with bounds independent of depth and
volume. It neither proves uniqueness against all nonabelian critical
orbits nor supplies a holomorphic ball in all independent datum entries.

## 8. Closing the finite-geometry, arbitrary-regular-datum problem

The preceding local result can be pushed further without assuming a
uniform inverse. This section does so, real first and then complex.
Keep one finite torus and depth \(k\) fixed, with \(\Omega_j=T\).
Let \(s=L^k\), and let \(n_p\) be its number of coarse plaquettes.

**Proved.** There are positive \(\varepsilon_*,\varepsilon_{\rm d}\)
depending on this finite geometry such that every real datum with
\(\max_p|V_p-1|<\varepsilon_{\rm d}\) has exactly one critical
residual orbit regular at radius \(\varepsilon_*\). Its curvature and
current are bounded linearly in \(\max_p|V_p-1|\), with an explicit
finite-geometry constant below. The comb representative is continuous
in these real data and has a holomorphic continuation near each of
them. After reducing \(\varepsilon_{\rm d}\), the complex radius can
be chosen uniformly over these real data, for this fixed geometry.

**Step 1: uniqueness among all sufficiently regular critical points.**
If no positive \(\varepsilon_*\) worked, there would be pairs
\(U_m,W_m\) of inequivalent critical configurations with the same
datum, both regular at radius \(1/m\). The space of fine link fields
is a finite product of compact groups. Pass to a subsequence for
which both fields converge, to \(U_\infty,W_\infty\). Their plaquettes
are 1 because their curvature bounds tend to zero. Near a flat field
all the averages lie in the analytic branch, as established in
Section 5.1; continuity therefore gives a common limiting datum
\(V_\infty\). It is flat, since path transports around a coarse
plaquette can be reduced across the fine squares in its nonwrapping
blocks. Section 4 puts both limiting fields in the same flat residual
orbit, whose forest representative is \(\mathcal LV_\infty\).
The tree gauge is continuous, so both forest representatives converge
to that representative. For large \(m\) they lie in the uniqueness
neighborhood of Section 5, with datum sufficiently close to
\(V_\infty\). That section forces them into the same residual orbit,
a contradiction. Fix one such \(\varepsilon_*>0\), decreasing it
if necessary to be below the outline's small branch thresholds.

**Step 2: a compact regular minimization problem.** The zero set of
the real Wilson action is exactly the flat fields: each summand is
\(1-\cos\theta_p\ge0\), with equality only for \(U_p=1\).
This flat set is compact. It is contained in an open set on which all
\(k\) averaging steps are analytic and the scale-normalized curvature
and current are less than \(\varepsilon_*/2\). The current vanishes
on flat fields by its variational definition. There is \(E_0>0\)
such that the compact sublevel \(\{S\le E_0\}\) lies in this open
set: otherwise a sequence outside the set with actions tending to
zero would have a flat limit outside it, a contradiction.

The lift gives a sharper energy count than a maximum over all fine
plaquettes. A nonidentity fine plaquette of \(\mathcal LV\) crosses
two block faces. For each coarse plaquette, its two transverse
coordinates have \(s\) choices each; hence there are exactly \(s^2\)
copies with the same plaquette product. All other fine plaquettes
are 1. Consequently
\[
 S(\mathcal LV)=s^2 S(V)
       \le\tfrac12 s^2n_p\varepsilon_1^2,
 \qquad \varepsilon_1=\max_p|V_p-1|.                         \tag{8.1}
\]
Here \(1-\tfrac12\operatorname{tr}V_p=|V_p-1|^2/2\) for real
\(SU(2)\), by its eigenvalues \(e^{\pm i\theta}\).
Take \(\varepsilon_1<\sqrt{E_0/(2s^2n_p)}\). The set
\[
       \mathcal K_V=\{U:S(U)\le E_0,\ \mathcal M^kU=V\}
\]
contains \(\mathcal LV\), and is compact because the average is
continuous on that sublevel. A minimizing sequence has a convergent
subsequence in \(\mathcal K_V\); continuity of \(S\) proves attainment.
The minimum is at most \(S(\mathcal LV)<E_0/4\). It is therefore
interior to the energy cap. Every sufficiently short constrained curve
through it stays below \(E_0\), so its action derivative is zero.
It is a regular constrained critical point, not just an unrestricted
minimum. Step 1 makes its regular critical orbit unique.

**Step 3: the linear bound and its actual constants.** At this
minimum \(U_V\), (8.1) gives
\[
                      \max_p|(U_V)_p-1|
                            \le s\sqrt{n_p}\,\varepsilon_1.
\]
The current normalization is the outline's (R1), lines 5562–5573.
Varying one link by \(e^{i\eta tB}\) differentiates six plaquette
terms. After cyclically moving the varied factor to the base, one
term is bounded in absolute value by
\(\eta\|B\|\,|U_p-1|\); the identity contributes zero since
\(\operatorname{tr}B=0\). This estimate follows from matrix
Cauchy–Schwarz with the normalized trace; for an \(SU(2)\) matrix,
the normalized Hilbert–Schmidt norm of \(U_p-1\) equals its operator
norm. Unitary transports preserve it. Divide by \(\eta^4\) in
(R1) and take the supremum over unit \(B\). Thus
\[
 \max_p\eta^{-2}|(U_V)_p-1|
       \le s^3\sqrt{n_p}\,\varepsilon_1,\qquad
 \max_e|J(U_V)(e)|
       \le6s^4\sqrt{n_p}\,\varepsilon_1.                      \tag{8.2}
\]
Both are gauge invariant for real gauges. These are honest linear
bounds; their powers of \(s\) and \(n_p\) are not suppressed.

**Step 4: real measurability and complex continuation at curved data.**
Shrink the local charts of Sections 5–6 so that their real critical
points are regular at radius \(\varepsilon_*/2\), using (6.3).
They cover the graph
\(\{(\mathcal LV,V):V\text{ real and flat}\}\). This graph is
compact, so finitely many charts, with margins inside their datum
balls and field neighborhoods, cover it. For sufficiently small
\(\varepsilon_{\rm d}>0\), every minimizing pair
\((U_V^\text{forest},V)\) from Step 2 lies in those smaller chart
neighborhoods. To prove this last assertion, a contrary sequence would
have \(\varepsilon_1\to0\) and, by (8.1), \(S(U_V)\to0\).
Compactness and the continuous forest gauge would give a limiting
pair on that flat graph, contradicting exclusion from its open
neighborhood.

In the chosen chart the minimizer is its local critical branch, by
Section 5. On overlapping real neighborhoods the branches agree
after the comb gauge: both are regular critical points with the same
datum, so Step 1 and uniqueness of the comb representative apply.
This proves continuity, hence Borel measurability, of the real
representative on the whole small-test domain. Each branch already
has the holomorphic continuation of Section 6, including at a
nonflat real center in the interior of its datum ball.

There is a uniform positive complex radius for this fixed geometry.
Use smaller chart balls to retain a fixed positive margin within
each of the finitely many larger balls. The coordinate conversion
\(V'=e^hV\mapsto\log(V'V_\alpha^{-1})\), for a chart based at
\(V_\alpha\), is analytic on their closures and has bounded first
derivative there. Taking the minimum of the finitely many margins
divided by twice these derivative bounds keeps every \(\|h\|\)
below that minimum inside one larger chart. Reducing the radius if
necessary handles the closed line segments used for the derivative
bound. All continuing maps have finite derivative bounds there.
Together with (8.2), this also bounds their complex curvature and
current by \(C_{T,k}(\varepsilon_1+\|h\|)\). The real values specify
the holomorphic germ uniquely by the identity argument of Section 6.
The Euclidean complex ball contains a product ball: if there are
\(m\) coarse bonds, \(\|h\|_2\le\sqrt m\sup_c|h_c|\), so divide
the radius by \(\sqrt m\). This proves the finite-geometry statement.

## 9. Endpoint

**STOPPED, not PROVED or REFUTED for A1.** The completed result is
Section 8: every sufficiently regular datum on a fixed single lattice
has one regular critical residual orbit, a continuous real comb
representative, and a holomorphic local continuation. Its explicit
curvature/current constants are \(s^3\sqrt{n_p}\) and
\(6s^4\sqrt{n_p}\). Sections 7.1–7.2 supply exact configurations that
refute two attempted uniform estimates for a particular gauge/seed;
they also verify why neither configuration refutes A1.
Section 7.4 goes beyond the flat tests: for alternating Cartan data
it writes an actual constrained critical configuration, verifies
stationarity against all constrained variations, and constructs its
comb representative. Its scaled curvature and current are at most
\(32|t|\) and \(16|t|\), with a one-parameter complex radius
independent of depth and torus size.

The budget ends at replacing Section 8's fixed-geometry compactness
by a common Landau chart and constrained inverse with bounds uniform
over the actual separated families. That step was not proved, and
no configuration violating A1 was obtained. Consequently the uniform
real theorem, its uniform complex neighborhoods, and the seam and
restriction clauses remain undecided. This does not select between
the two research routes.

All proof checks above are written arguments. Source fetching,
navigation, and document editing supplied no mathematical discharge;
there was no numerical proof, enumeration, audit, or subagent.
