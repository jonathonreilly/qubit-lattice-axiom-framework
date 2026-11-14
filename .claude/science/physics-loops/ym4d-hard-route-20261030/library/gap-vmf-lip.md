# Repo search

**Strong coupling only. This work does not touch the middle range.**
Proof item, FINISH row 785. Author: Codex gpt-6-astra, max.
Source checkout: `3b5f2007efb4e5ac55c25e27cc2f22580e618a86`.
Research text, not an audit; this grants no status.

The requested `prior/gap-vmf-lip-astra.md` does not exist at this revision.
The lead's `prior/repo-search-2026-11-08.md` concerns older RG targets. Its
search terms and findings do not settle this single-site question. There
is no target-specific "Repo prior work" line in row 785.

The present search checked main at `bb4ec020d5ada57c630dd89acc98a68397ade423`
and PRs 10114, 10133, 10134 and 10141 at, respectively,
`f76f6c649cff`, `89faef229ff6`, `1e70c7211a2c`, and `fb99b4dddc72`.
Exact searches used `vMF-Lip`, `von.?Mises`, and `AS-bg`; a separate
YM4D-scoped search used `Dobrushin`. Search logs are in
`/tmp/gap-vmf-lip-3b5f2007e/`. Relevant source passages read:

- Main, `docs/SU2_TWO_REGION_BOUNDARY_RESPONSE_BOUNDED_THEOREM_NOTE_2026-11-08.md`,
  lines 370–482: finite-product total-variation comparison. This is useful
  prior machinery, not the requested chord estimate.
- PR 10133, soft-route `MASS_GAP_CW_CROSSOVER_ATTACK.md`, lines 115–174:
  the same one-link vMF law and transverse moments. Its parallel variance
  bound OL-S1 remains open in that text. Even that bound concerns linear
  observables, not arbitrary chord-Lipschitz functions. Credit the Grok
  branch's prior formulation; no numerical certificate is imported.
- PR 10114, soft-route `SRCCD55.md`, lines 245–286: lower variance bounds
  on a circle subgroup. These have a different domain and conclusion.
- Main's `POSITIVE_WILSON_VILLAIN_MIXTURE_AND_WEAK_REGION_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-16.md`,
  lines 191–240: a circle convolution limit, not this estimate. The other
  exact-name hits concern discrete one-link diagnostics, U(1) mixtures,
  and moments of a different spherical formation model.

Within this lane, `gap-crux-fp.md` 4.2–4.2b supplies Lemma P and the
proposed reductions. `gap-mid-max.md` Section 10 supplies the comparison
template; `gap-mid-check.md` Section 5 supplies its mass-accounting and
periodic-distance corrections. These results are credited and reused.
The two source proof notes are by Claude Fable 5.2; the comparison
method is Dobrushin's. The layer route is attributed there to Durhuus
and Fröhlich; their paper was not read or used as an unproved input here.
`gap-fp-astra.md` lines 424–453 checks Lemma P and explicitly excludes
the general direction. `gap-u1-audit-opus.md` Section 3 R1 reopens this
exact question. Searches of `open-registry.md`, `open-core.md`, and
`l17c.md` found no competing vMF, Dobrushin, or AS-bg owner.

The Sussman–Alpoge index README and the relevant neighbouring chunk and
obligation rows were consulted before their source. Searches for vMF,
von Mises, Dobrushin, Durhuus, Brownian motion and exit time found no
matching single-site statement in the pinned outline or CA-I. The
outline's lines 588–599 and 31871–31882 keep a mass gap separate from
its existence result. These are scope statements, not suppliers of
vMF-Lip. Both requested source files were fetched once at `31a47c543775`.
Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors
of their text. No Balaban estimate enters the single-site problem.

## 1. The single-site bound

**Theorem V (author proof; not independently checked).** Let `sigma` be
uniform probability measure on `S^3`. Put

\[
 z(k)=\int_{S^3}e^{kh_1}\,d\sigma(h),\qquad
 d\mu_F(h)=z(|F|)^{-1}e^{F\cdot h}\,d\sigma(h).
\]

For every `F` in `R^4`, every unit `e`, and every real function `phi`
with `|phi(h)-phi(h')| <= |h-h'|`,

\[
 |\operatorname{Cov}_{\mu_F}(\phi,h\cdot e)|
 \le a(|F|)\le\frac14,
 \qquad
 a(k)=\frac{z'(k)}{kz(k)}\quad(k>0),\qquad a(0)=\frac14.       \tag{V}
\]

The supremum over both `e` and `phi` equals `a(|F|)`.
Thus the radius restriction 4 is unnecessary for this single-site theorem.

**Proof.** The case `F=0` is already Lemma P. Suppose `F=ku`, with
`k>0` and `|u|=1`. Write `B` for the open unit ball, `dS` for surface
area, and

\[
 S_k=\int_{\partial B}e^{F\cdot h}\,dS(h),\qquad
 V_k=\int_B e^{F\cdot x}\,dx,\qquad
 d\nu_F(x)=V_k^{-1}e^{F\cdot x}\,dx.
\]

The vector divergence theorem gives

\[
 \int_{\partial B}h e^{F\cdot h}\,dS(h)=F V_k.
\]

Rotational symmetry also gives `E_F h=(z'(k)/z(k))u`. Consequently

\[
 V_k/S_k=a(k),\qquad E_Fh=a(k)F.                            \tag{1}
\]

This fixes both the volume and surface normalization.

**An interior field with the required boundary flux.** Define smooth
radial scalars `b,w` and a vector field `V` on the closed ball:

\[
 b(x)=\frac{z(k|x|)}{z(k)},\qquad
 w(x)=\frac{1-b(x)}{k^2},\qquad
 V(x)=-\nabla w(x)+Fw(x).
\]

Smoothness at zero follows also from
`z(k|x|)=integral exp(k x.h) d sigma(h)`.
Differentiating this integral twice proves `Delta b=k^2 b`. Thus

\[
 (-\Delta+k^2)w=1,\qquad w|_{\partial B}=0,
 \qquad \operatorname{div}(e^{F\cdot x}V)=e^{F\cdot x}.       \tag{2}
\]

The two first-derivative terms cancel in the last identity. At `|h|=1`,
the radial derivative of `w` is `-z'(k)/(kz(k))=-a(k)`. Therefore
`V(h).h=a(k)`.

For the fixed unit vector `e` put

\[
 J_e(x)=e^{F\cdot x}\{e-(F\cdot e)V(x)\},\qquad
 M(x)e=e-(F\cdot e)V(x).
\]

Equation (2) gives `div J_e=0`. Its normal component at the sphere is

\[
 J_e(h)\cdot h=e^{F\cdot h}\{h\cdot e-a(k)F\cdot e\}.       \tag{3}
\]

For any smooth extension `Phi` of the boundary function, (1), (3), and
the divergence theorem yield

\[
 \operatorname{Cov}_{\mu_F}(\phi,h\cdot e)
   =a(k)\int_B \nabla\Phi(x)\cdot M(x)e\,d\nu_F(x).          \tag{4}
\]

**The contraction after averaging.** Set `m(s)=z'(s)/z(s)` and write
`x=rh`, `s=kr`. Decompose `e=e_perp+c u`, where `e_perp.u=0`.
Direct differentiation of `w` gives

\[
 M(rh)e=e_\perp+c\,b(r)\{u-m(s)h\}.                       \tag{5}
\]

Given `r` under `nu_F`, the direction `h` has exactly the law `mu_(su)`.
In particular `E(h|r)=m(s)u`. The mixed term in the squared norm of
(5) has zero conditional expectation, and `|h|=1` gives

\[
 E_{\nu_F}(|M(x)e|^2\mid r)
   =|e_\perp|^2+c^2 b(r)^2\{1-m(s)^2\}\le1.                \tag{6}
\]

Indeed `|m(s)|<=1`. Also `0<b(r)<=1`: symmetry writes `z(s)` as the
average of `cosh(s h_1)`, which increases for `s>=0`.
Integrating (6) and applying Cauchy–Schwarz proves
`E_nu |M(x)e|<=1`.

**Using the chord hypothesis.** The explicit extension

\[
 \Phi(x)=\inf_{h\in S^3}\{\phi(h)+|x-h|\},\qquad x\in\mathbb R^4,
\]

equals `phi` on the sphere and is 1-Lipschitz on Euclidean space.
The triangle inequality proves both assertions. Convolve it with a
nonnegative smooth approximate identity supported in the ball of radius
`epsilon`. The resulting smooth `Phi_epsilon` is 1-Lipschitz, has
`|grad Phi_epsilon|<=1`, and differs from `Phi` uniformly by at most
`epsilon`. Apply (4) to its boundary trace. Equations (4)–(6) bound that
covariance by `a(k)`. Uniform convergence on the sphere passes the bound
to `phi`. No boundary derivative of a harmonic extension is used.

Finally `a(k)` is the transverse moment in Lemma P. To identify the
normalization directly, differentiate the integral of
`h_v exp(k h_u)` under a rotation in the `u,v` plane, where `v` is a
unit vector perpendicular to `u`. Invariance of `sigma` gives
`E_F h_u=k E_F h_v^2`. Thus `a(k)=E_F h_v^2<=1/4` by the already proved
Lemma P. Taking `e=v` and `phi(h)=h_v` attains `a(k)`.
This proves every assertion of (V). QED.

## 2. Chord comparison and influence

The finite-product argument is Dobrushin's. Its total-variation version
already appears in the sources above. Here the Lipschitz seminorm and
the diameter factor are written out. Averaging over the possible update
sites gives a geometric matrix series, replacing the cyclic mass
bookkeeping of the earlier proof.

For laws on \(S^3\), use the dual distance
\[
 d_{\rm Lip}(\eta,\eta')=
 \sup_{\operatorname{Lip}_{\rm chord}\psi\le1}
       |\eta(\psi)-\eta'(\psi)|.
\]
This is the dual form of the chord Wasserstein distance. Only the
displayed supremum is needed below.

**Corollary V1.** For all \(F,F'\in\mathbb R^4\),
\[
 d_{\rm Lip}(\mu_F,\mu_{F'})\le |F-F'|/4.                    \tag{7}
\]
Indeed, along \(F_t=F+t(F'-F)\), differentiation of the finite,
bounded sphere integral gives
\[
 \frac{d}{dt}\mu_{F_t}(\psi)
   =\operatorname{Cov}_{F_t}(\psi,h\cdot(F'-F)).
\]
Apply (V) after dividing by \(|F'-F|\), then integrate from 0 to 1.
If \(F=F'\), the conclusion is immediate.

**Lemma DC, chord form.** Let \(\Lambda\) be a nonempty finite set and
\(\Omega=(S^3)^\Lambda\). Let \(\gamma_i(\cdot\mid w)\) be measurable
probability kernels depending only on \(w\) off \(i\). Suppose
\[
 d_{\rm Lip}\bigl(\gamma_i(\cdot\mid w),
                 \gamma_i(\cdot\mid w')\bigr)
       \le C_{ij}|w_j-w'_j| \quad (i\ne j),                 \tag{8}
\]
whenever the two configurations differ only at \(j\).
Here \(C_{ij}\ge0\), \(C_{ii}=0\), and
\(\max_i\sum_j C_{ij}\le\alpha<1\).
Let these kernels be versions of \(\mu\)'s conditional laws at every site.
Let \(\widetilde\mu\) have them at every site outside \(D\subset\Lambda\).
The latter condition is an almost-sure statement about conditional laws.

For a function with finite coordinate Lipschitz seminorms set
\[
 \delta_i(f)=
 \sup_{\substack{w=w'\ {\rm off}\ i\\w_i\ne w_i'}}
       \frac{|f(w)-f(w')|}{|w_i-w'_i|},\qquad
 \Delta(f)=\sum_i\delta_i(f).
\]
Join \(i,j\) when \(C_{ij}+C_{ji}>0\). Let \(d\) be the graph distance
from \(\{i:\delta_i(f)>0\}\) to \(D\). Then
\[
 |\widetilde\mu(f)-\mu(f)|
 \le 2\sum_i\delta_i(f)\sum_{j\in D}
                    \left(\sum_{n\ge0}C^n\right)_{ij}
 \le \frac{2\Delta(f)\alpha^d}{1-\alpha}.                  \tag{DC}
\]
An empty support or no connecting path gives zero. When needed,
\(\alpha^0=1\), including at \(\alpha=0\).

**Proof.** Put \(\Gamma_i g(w)=\int g(\xi,w_{\ne i})
\gamma_i(d\xi\mid w)\). Its \(i\)-seminorm is zero. For \(j\ne i\),
split its difference between \(w,w'\) into the change of integrand
under one fixed kernel and the change of kernel with one fixed
integrand. The first term is bounded by
\(\delta_j(g)|w_j-w'_j|\). Definition (8) bounds the second by
\(C_{ij}\delta_i(g)|w_j-w'_j|\). Thus
\[
 \delta_j(\Gamma_i g)\le\delta_j(g)+C_{ij}\delta_i(g).
                                                                  \tag{9}
\]
These estimates also ensure continuity of all functions used below.

Let \(N=|\Lambda|\), \(P=N^{-1}\sum_i\Gamma_i\), and
\[
 R=(1-N^{-1})I+N^{-1}C,\qquad
 q=1-(1-\alpha)/N<1 .
\]
For column vectors of seminorms, (9) gives
\(\delta(Pg)\le R^T\delta(g)\), entry by entry.
The row sums of \(R\) are at most \(q\). Hence
\[
 \Delta(P^t f)\le q^t\Delta(f),\qquad
 \operatorname{osc}(P^t f)\le2q^t\Delta(f).                 \tag{10}
\]
The last inequality changes coordinates one at a time and uses
the chord diameter 2. Since \(\mu(P^t f)=\mu(f)\), (10) proves uniform
convergence of \(P^t f\) to \(\mu(f)\).

Take conditional kernels \(\widetilde\Gamma_i\) for
\(\widetilde\mu\). Off \(D\) their contributions cancel almost surely.
On \(D\), two probability averages of the same one-coordinate function
differ by at most its oscillation, which is at most \(2\delta_i(g)\).
Therefore
\[
 |\widetilde\mu(g-Pg)|
 =\left|N^{-1}\sum_i
   \widetilde\mu(\widetilde\Gamma_i g-\Gamma_i g)\right|
 \le\frac2N\sum_{i\in D}\delta_i(g).                       \tag{11}
\]
This is the required diameter factor, not a total-variation bound.

Telescope (11) for \(g=P^t f\), and use uniform convergence:
\[
 |\widetilde\mu(f)-\mu(f)|
 \le\frac2N\sum_{t\ge0}\sum_{j\in D}
                         ((R^T)^t\delta(f))_j .
\]
Both matrix series converge by their row-sum bounds. Since
\(I-R=(I-C)/N\), multiplication of the convergent geometric series
shows
\[
 N^{-1}\sum_{t\ge0}R^t=(I-C)^{-1}=\sum_{n\ge0}C^n .
\]
This proves the first inequality in (DC). A nonzero entry
\((C^n)_{ij}\) supplies a path of length \(n\). If \(i\) is in the
support and \(j\in D\), it therefore requires \(n\ge d\).
Finally \(\sum_j(C^n)_{ij}\le\alpha^n\).
Summing this bound proves the second inequality. QED.

**Lemma INF, chord form.** In the layer model at coupling \(\beta\ge0\),
on a periodic box with sides at least 3, with arbitrary fixed backgrounds
and bond coefficients in \([-1,1]\),
\[
 C_{xy}\le\beta/4\quad\hbox{for neighbours},\qquad
 \alpha\le 3\beta/2.                                      \tag{12}
\]
In the four-dimensional Wilson gauge measure at coupling \(s\ge0\),
on tori with all sides at least 3,
\[
 C_{\ell k}\le s/4\quad\hbox{for links in one plaquette},
 \qquad \alpha\le9s/2.                                    \tag{13}
\]

**Proof.** Identify unit quaternions with \(S^3\), as in
gap-transfer, Notation N.1–N.2. Left or right multiplication by a
unit quaternion, and inversion, are Euclidean isometries.
The real half-trace of a product is an inner product after such maps.
Consequently every layer interaction can be written
\(y_b=h_x\cdot O_b h_y\), with \(O_b\) orthogonal and fixed by
the background. Its single-site law is \(\mu_F\), with
\(|F|\le6\beta\). A change of one neighbour changes one term of \(F\);
the difference has norm at most \(\beta|h_y-h'_y|\).
Use (7). There are six neighbours, giving (12).

For \(s>0\) and a gauge link \(\ell\), each of its six plaquettes contributes one
unit staple to \(F/s\). Thus \(|F|\le6s\). With sides at least 3,
two distinct links share at most one plaquette, and these plaquettes
contain 18 distinct other links. These are the geometry facts in
Lemma INF and its check. Changing one of them changes its staple by
exactly that link's chord distance, because the other factors are
fixed isometries. Again use (7), then sum the 18 bounds.
At \(s=0\) all one-link kernels are Haar and all influences vanish. QED.

Only radii \(6\beta<4\) and \(6s<4/3\), respectively, are needed in
the applications below.

## 3. R-a: the background-uniform layer twist

Use \(I(u,v)\) and \(y_b\) exactly as in gap-crux-fp Section 4.2.
Let \(B\) be the periodic spatial box with integer sides at least 3.
For \(0<\beta<2/3\), put \(q=3\beta/2\). Then, for every background
\((u,v)\) and every spatial direction \(\nu\),
\[
 \left|\log\frac{I(u,c_\nu v)}{I(u,v)}\right|
 \le \frac{4\beta}{1-q}\frac{|B|}{b_\nu}
                         q^{\lfloor b_\nu/2\rfloor-1}.    \tag{14}
\]

**Proof.** This carries Proposition TW through with the new influence
bound. The details keep its normalization and its factor of two.
Let \(\Sigma_0\) be the \(\nu\)-bonds from \(b_\nu-1\) to 0.
Set \(J^\theta_b=1-2\theta\) on \(\Sigma_0\), and 1 elsewhere.
Keep the constant term \(-\beta\) per bond fixed in the exponent:
\[
 I_\theta=\int\exp\!\left[-\beta\sum_b
                                  (1-J^\theta_b y_b)\right]dh .
\]
The two endpoints are the two partition functions in (14), and
\[
 \log(I_1/I_0)=-2\beta\sum_{b\in\Sigma_0}
                         \int_0^1 E_{J^\theta}y_b\,d\theta. \tag{15}
\]

Put \(j=\lfloor b_\nu/2\rfloor\), and let \(\Sigma_1\) be the bonds
from \(j-1\) to \(j\). Let \(K^\theta\) agree with \(J^\theta\) except
that its coefficients on \(\Sigma_1\) are \(-1\).
Multiplying the spins with \(0\le x_\nu<j\) by \(-1\) changes signs
on precisely \(\Sigma_0\cup\Sigma_1\). Haar measure is preserved.
It sends \(J^\theta\) to \(K^{1-\theta}\) and \(y_b\) to \(-y_b\)
for \(b\in\Sigma_0\). Consequently
\[
 \int_0^1 E_{J^\theta}y_b\,d\theta
   =\frac12\int_0^1
                  (E_{J^\theta}y_b-E_{K^\theta}y_b)\,d\theta. \tag{16}
\]

The two laws have the same conditional kernels off the sites \(D\)
with \(x_\nu\in\{j-1,j\}\).
Each \(y_b\), \(b\in\Sigma_0\), has two coordinate seminorms at most
one, so \(\Delta(y_b)\le2\). Its support lies on the planes
\(x_\nu=0,b_\nu-1\). The shortest periodic nearest-neighbour distance
to \(D\) is at least
\(\min(j-1,b_\nu-1-j)=j-1\).
Lemma INF gives row sum at most \(q\) throughout both interpolations.
Lemma DC therefore bounds the integrand in (16) by
\(4q^{j-1}/(1-q)\).
Equations (15)–(16), and \(|\Sigma_0|=|B|/b_\nu\), prove (14). QED.

For the exact uniform statement (AS-bg), fix \(0<\beta_1<2/3\) and set
\[
 q_1=3\beta_1/2,\qquad
 m=\tfrac12\log(1/q_1),\qquad
 C=\frac{4\beta_1q_1^{-3/2}}{1-q_1}.
\]
Since \(\lfloor b/2\rfloor-1\ge b/2-3/2\), (14) implies
\[
 \left|\log\frac{I(u,c_\nu v)}{I(u,v)}\right|
       \le C\frac{|B|}{b_\nu}e^{-m b_\nu}
 \quad(0\le\beta\le\beta_1).                              \tag{AS-bg}
\]
At \(\beta=0\) the ratio is 1. If \(\beta_1=0\), any positive
\(C,m\) works. Uniformity includes every background and all box sizes.

## 4. R-b: the seed for \(\beta<2/9\)

The partition-to-spectrum statements use the existing transfer
operator (TM), the centre symmetries (TM-c), and the corrected
Theorem SH. They are not new constructions here.
Write
\[
 F(t,B;\beta)=\log Z(t,B;\beta),\qquad
 S(t;B;\beta)=\sum_{i\ge1}
       \left(\frac{\lambda_i(B;\beta)}{\lambda_0(B;\beta)}\right)^t,
\]
\[
 \Phi_B(a;\beta)=2F(a,B;\beta)-F(2a,B;\beta).
\]
Here the sum includes every excited transfer eigenstate, including
the nonzero electric-flux sectors. Let \(\bar a_{t,B}(s)\) denote
the mean of \(1-x_p\) over the plaquettes, where
\(x_p=\tfrac12\operatorname{tr}U_p\).

**Theorem DOB, chord form.** Let \(0<\beta<2/9\), \(q=9\beta/2\),
\(a\ge3\) an integer, and \(B\) a periodic spatial box with all sides
at least 3. For every \(0\le s\le\beta\),
\[
 |\bar a_{2a,B}(s)-\bar a_{a,B}(s)|
       \le\frac{8q^{\lfloor a/2\rfloor-1}}{1-q},           \tag{17}
\]
and
\[
 0\le\Phi_B(a;\beta)
       \le\frac{96a|B|\beta q^{\lfloor a/2\rfloor-1}}{1-q}.
                                                                  \tag{18}
\]
In particular, if
\[
 \frac{768a^4\beta q^{\lfloor a/2\rfloor-1}}{1-q}
       \le \frac3{5000},                                  \tag{19}
\]
then
\[
 S(a;(2a)^3;\beta)<\frac1{1650}.                            \tag{20}
\]
For each fixed \(\beta<2/9\) with \(\beta>0\), such an \(a\) exists.
Using the corrected Theorem SH, this gives a volume-uniform lattice
gap on periodic cubes at that fixed coupling, and in particular
\[
 m(L^3;\beta)\ge\frac{3}{50a}
       \quad\hbox{for every integer }L\ge64a.              \tag{21}
\]

**Proof of the comparison bound.** Use the cut construction of
Lemma M in gap-mid-max Section 8. The marginal of the first half of
the torus \((2a,B)\), with time indices reduced modulo \(a\), defines
\(\widetilde\mu\) on \((a,B)\). Its single-link kernels agree with
the ordinary Gibbs kernels outside \(D\), where \(D\) consists of
spatial links at times 0 and \(a-1\), and time links starting at
\(a-1\). Lemma M proves this conditional-law assertion; it is reused.

Put \(j=\lfloor a/2\rfloor\). Take the \(3|B|\) spatial plaquettes
at time \(j\) and the \(3|B|\) time plaquettes in the slab
\([j-1,j]\). Their images in the long torus do not cross the cut.
For each such \(p\), the function \(x_p\) is chord-Lipschitz with
constant at most one in each of its four links. Hence
\(\Delta(x_p)\le4\).

Assign to each spatial link at time \(t\) the position \(t\), and
to a time link starting there the position \(t+1/2\), **on the circle
\(\mathbb R/a\mathbb Z\)**. Two links of one plaquette have circular
position distance at most 1, including the wrapping plaquettes.
The selected plaquette links lie in the interval \([j-1,j]\).
The positions in \(D\) are \(0,a-1,a-1/2\).
Their minimum circular separation is \(j-1\):
the two possibly shorter endpoint distances are \(j-1\) and
\(a-1-j\), and \(a\ge2j\).
Thus the influence-graph distance to \(D\) is at least \(j-1\).
This explicitly uses the periodic-distance correction in gap-mid-check.

At coupling \(s\), (13) bounds the row sum by \(9s/2\le q\).
Lemma DC gives
\[
 |\mu_{a,B;s}(x_p)-\widetilde\mu(x_p)|
       \le 2\cdot4\,q^{j-1}/(1-q).
\]
Translation invariance makes the average over those six plaquette
orientations equal to the mean plaquette value in each torus.
This proves (17), as in Proposition MIX. At \(s=0\), it also follows
directly from product Haar measure.

**From the local comparison to the seed.** Differentiating the finite
partition functions gives
\[
 \frac{d}{ds}F(t,B;s)=-6t|B|\bar a_{t,B}(s).
\]
Both free energies vanish at \(s=0\). Consequently
\[
 \Phi_B(a;\beta)=12a|B|\int_0^\beta
           (\bar a_{2a,B}(s)-\bar a_{a,B}(s))\,ds .
\]
This is Theorem D-shape (d). Substitution of (17) gives (18).
For completeness, if \(g(t;B)=\log(1+S(t;B))\), the transfer trace
identity gives \(\Phi_B=2g(a;B)-g(2a;B)\ge g(a;B)\ge0\);
the inequality uses \(S(2a;B)\le S(a;B)\).
Thus \(S(a;B)\le e^{\Phi_B}-1\), the existing D-shape (a).

For \(B=(2a)^3\), \(|B|=8a^3\). The coefficient in (18) is
therefore \(96\cdot8=768\). Under (19), the elementary exponential
series bound \(e^x-1\le x/(1-x)\), \(0\le x<1\), gives
\[
 S(a;(2a)^3;\beta)\le \frac{3}{4997}<\frac1{1650},
\]
because \(3\cdot1650=4950<4997\). This proves (20) with the strict
inequality required by the corrected shape statement.

Since \(q<1\), the left side of (19) tends to zero as \(a\) tends
to infinity. One elementary verification is to bound
\(q^{\lfloor a/2\rfloor-1}\le q^{-3/2}(\sqrt q)^a\).
The ratio of successive terms \(a^4(\sqrt q)^a\) tends to
\(\sqrt q<1\); eventually it is bounded by a fixed number below 1.
This proves existence without a search over sizes.

**Both halves of the seed.** In Identity FL, \(P_0\) projects onto
the sector of zero electric flux, and the positive ground state
lies there. Thus its definitions give
\[
 0\le S_0\le S,\qquad
 0\le U\le S/(1+S),\qquad
 1+S=(1+S_0)/(1-U).
\]
Equation (20) bounds the full excited sum. It has not dropped
either the sector of zero flux or the other sectors.

**The stated gap consequence.** Here is the arithmetic through
Theorem SH, to fix the constants in (21). Its inherited spatial
enlargement bound gives, with \(s_0=S(a;(2a)^3)<1/1650\),
\[
 s_1:=S(a;(4a)^3)\le (1+s_0)^{64}-1
       < e^{32/825}-1\le \frac{32}{809}<\frac1{25}.
\]
For the middle inequality, use
\(e^x-1\le x/(1-x/2)\) for \(0\le x<2\), which follows from
\(n!\ge2^{n-1}\) for \(n\ge1\).
The corrected ratio-4 statement of Theorem SH has
\(j=2,\ p=2,\ q_{\rm SH}=3,\ K=111/5,\ E=512/27\).
In particular \(E<K\), and
\[
 K s_1<\frac{3552}{4045}<\frac{22}{25}.
\]
For \(0<y<1\),
\(-\log y\ge(1-y)+(1-y)^2/2\), by integrating the geometric
series. Hence
\[
 \log(1/(K s_1))>
       \frac3{25}+\frac9{1250}=\frac{159}{1250}>\frac18 .
\]
If \(s_1=0\), the spectral inequalities are immediate instead.
For \(L\ge64a\), the scale index in SH (ii) is at least 4, so
\[
 m(L^3;\beta)>
       \frac1a\left(\frac18-\frac1{16}\right)
       =\frac1{16a}>\frac3{50a}.
\]
We used \(\log(eE/K)<1\). The finitely many smaller cubes have
positive finite-volume gaps by (TM). This also makes the lower
bound over all cube sides at least 3 strictly positive for each
fixed \(\beta\). QED.

**A hand-checkable example in the enlarged range.** Take
\(\beta=1/9\) and \(a=96\). Then \(q=1/2\), and the left side
of (19) is exactly
\[
 \frac{512}{3}\,(3\cdot2^5)^4\,2^{-47}
       =\frac{27}{2^{18}}<\frac3{5000},
\]
since \(45000<2^{18}=262144\). Thus (20) holds and (21) gives
\(m(L^3;1/9)\ge1/1600\) for \(L\ge6144\), given the existing
transfer and shape lemmas. No computed approximation enters this example.

## 5. Result and verification boundary

The new argument proves (vMF-Lip), with the sharp constant
\(a(|F|)=E_F(h_\perp^2)\), for all fields. Chord DC and INF give
(AS-bg) for every \(\beta_1<2/3\), and the full seed for every
\(0<\beta<2/9\). The transfer and shape results used downstream
are inherited; their scope is fixed lattice coupling.

These are analytic author proofs, not an independent check or an audit.
No numerical run, computer-assisted certificate, Lean proof, or new
physical premise is used. The former geodesic and pointwise
harmonic-gradient approaches were not used to discharge any step.
The remaining action is an independent reading of this exact text,
especially (2)–(6), the matrix orientation in DC, and the periodic cut.
The middle range and the continuum mass gap remain outside this result.
