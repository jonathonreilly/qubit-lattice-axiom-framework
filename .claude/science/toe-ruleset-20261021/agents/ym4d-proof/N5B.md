# N5B — does the sphere seam import an infrared theorem?

**Verdict: UNDECIDED for the sphere route.** The supplied results do not
prove N5 on the actual prism regulator, so they do not justify GO. They
also do not show that infrared decorrelation, or a physical mass gap, is
necessary, so they do not justify NO-GO. There is a valid conditional route
using only integration below fixed reference scales. Its missing estimate
is uniform transparency of the seam's conditional image for arbitrary
coarse crossing data. The hypercubic-to-sphere transfer F13 remains OPEN.

This answers the route question, not the full Yang–Mills existence problem.
**PROVEN** below means a written mathematical implication or counterexample
with its stated premises; it does not mean an audit verdict. **ARGUED**
marks mechanisms. **OPEN** marks an estimate not established on the actual
Yang–Mills measures. No result here is promoted to retained status.

Method credit: Tadeusz Balaban and Jonathan Dimock for constructive RG
methods discussed by the source packet. No external theorem, numerical
experiment or recalled [m] item carries a step of the proofs below.

## 1. The exact consumer and its corrected inputs

### 1.1 Regulator, observable and target

Use precisely SPHERE55 §1.3's doubled digital ball with the prism collar,

\[
 K_a=D_a\cup(\partial D_a\times[0,1])\cup\theta D_a,
 \qquad S_a(U)=\sum_p\widehat\beta_p\,s(U_p),\quad
 \widehat\beta_p=\tfrac14\sum_{Q\supset p}\beta_Q.
\]

The cell coefficients follow the chosen radial bare profile, and the
soft kernels are the normalized positive kernels of SPHERE55 §1.6,
including its shortest-path seam contours. Keep the profile, kernel
stiffness interval and renormalization rule fixed throughout a comparison.
No alternative identification seam or hard constraint is substituted.

Write \(h_i=aL^i\), \(h_n=\ell_{\rm ref}\), with odd blocking factor
\(L\ge3\), and \(U_0\to\cdots\to U_n\) for that positive Markov chain.
The local **chart-spacing** ceiling is \(2\ell_{\rm ref}\), because
\(1\le\Omega\le2\). This is not a bound on every prism crossing edge
or whole RG neighborhood. A physical ceiling on those neighborhoods
requires an explicit geometry/contour factor \(C_{\rm geom}\), covering
their diameters, and \(C_{\rm geom}\ell_{\rm ref}\le\ell_{\rm UV}\).
Matching that factor and the weak-coupling interval is part of the K_a
RG input. Small coupling at a differently interpreted reference scale
is not interchangeable with that premise.

Fix finite \(R\), a Killing field \(v\), and a compact interval of flow
parameters \(t\). Let \(F_{a,t}=\prod_{j=1}^q\widetilde O_a(f_{j,t})\)
and \(Z_a=Z_e(a)>0\), with every support along the path a physical distance
at least \(d_0>0\) from the equator. Initially the test supports are
mutually separated, as in SEAM55 §2. The seam insertion is the **net**
flux \(\mathfrak S_a(v)=-T_\chi\) of SPHERE55 §3.4, with its E9 index
correction, measured on the two transition shells. It is not the action,
a single north or south flux, or an arbitrarily chosen stress tensor.
The matched current, including profile contributions, is an input.

The precise seam target is

\[
 \sup_t Z_a^{-q}|\operatorname{Cov}_{\mu_{a,R}}
                 (F_{a,t},\mathfrak S_a(v))|\longrightarrow0
 \quad(a\to0,\ R\text{ fixed}). \tag{N5}
\]

This is SPHERE55 §4.1 for \(q=2\), and SEAM55 §2 for all separated
products. The exact Ward split consumes it as

\[
 \frac{d}{dt}\mu_{a,R}(F_{a,t})
 =-C_a(t)+\operatorname{Cov}(F_{a,t},B_a)
                  +\operatorname{Cov}(F_{a,t},\mathfrak S_a).
 \tag{1}
\]

Here W3 controls the normalized observable-side error \(C_a\), and
W0/W1 control the **coefficient-weighted, integrated** bulk term,
including the trace/tensor channels and source contacts. Small matching
coefficients alone do not bound their products with insertions. Uniform
vanishing of all three terms along the path proves the corresponding
moment invariance by integration of (1). This implication is **PROVEN**;
its actual all-product analytic hypotheses are **OPEN**.

### 1.2 What N5a and N5b literally say

At an intermediate resolution \(s\), set
\(H_s=E[F\mid W_s]\), \(M_s=E[\mathfrak S\mid W_s]\), and
\(V=U_n\). SPHERE55 §4.1 requires

\[
 A_s:=Z_a^{-q}\sup_V E[|\operatorname{Cov}(F,\mathfrak S\mid W_s)|\mid V]
       \longrightarrow0,\qquad
 \tau_s^2:=\inf_c\sup_V E[|M_s-c|^2\mid V]\longrightarrow0. \tag{2}
\]

The second clause is N5b. The constant \(c\) may depend on the cutoff,
radius, generator and resolution, but **not** on \(V\) or \(W_s\).
All coarse fields, including rough crossing data, enter the supremum.
Complex observables use absolute squares and complex constants.

Total covariance and Cauchy–Schwarz give the exact sufficient bound

\[
 Z_a^{-q}|\operatorname{Cov}(F,\mathfrak S)|
 \le A_s+B_s\tau_s,\qquad
 B_s=Z_a^{-q}\|H_s-EF\|_2. \tag{3}
\]

Indeed, the remaining term is \(E[(H_s-EF)(M_s-c)]\), and
\(\|M_s-c\|_2^2\le\sup_V E[|M_s-c|^2\mid V]\).
Thus the actual consumer needs \(A_s+B_s\tau_s\to0\), not just
\(\tau_s\to0\) when \(B_s\) can grow. The old proof bounded \(B_s\)
by the fine-field variance (SRC-E). SEAM55 §2.1 correctly replaces that
by a norm of the **conditional image**. Neither fine-field variance
control nor actual Yang–Mills coarse-image control is supplied here.

SPHERE55 E10 withdraws the bare-cutoff prefactor and the proposed
\(s\asymp\sqrt{a\ell_{\rm ref}}\) rate. For example, its conditional
seam power count \(a s^{-7/2}\) diverges with that choice. At shrinking
\(s\), the observable-image norm and all logarithmic losses must also
be included. The fixed-resolution argument below avoids asserting any
of those unproved rates.

### 1.3 N5-RG and the OS1 boundary

N5-RG is an analytic extension requirement, not a new name for the tower
identity. SPHERE55 §4.5 asks BFT, large-field bounds and flow for this
seam family, uniformly over terminal fields. N5-op must control the
actual effective seam insertions; N5-CD must control the conditional
covariances. Section 4 records why current producers do not meet that
contract.

N5 alone is not H_Euc or OS1. The necessary distinctions, following
CODEX_REVIEW_SPHERE F7/F12/F14, CODEX_REVIEW_SEAM F9 and
SPHERE2_55 §3, are:

| Consumer | Additional requirement beyond N5 |
|---|---|
| Fixed-R cap moment symmetry | W0/W1/W3 for every relevant product and derivative test, uniformly along each permitted path, with compatible normalizations and convergence. |
| Full observable algebra | A precise regularity/contact/multiplication bridge, compatible with positivity, from the separated tests to the chosen OS domain; or direct Ward estimates on that domain. Separated products do not by themselves determine contact distributions. |
| Flat-limit H_Euc/OS1 | Radius-uniform local bounds and equicontinuity on that same domain, common observable maps, and selection for every observable/group pair. |
| Existence with RP and non-freeness | The separately specified H_reg, H_RP and H_int on the common algebra/subsequence. Neither a seam theorem nor a conditional assembly proves these. |

This lane leaves those inputs named. It does not repeat the old assertion
that two-point invariance proves state invariance, or that separation of
the two RP halves removes repeated supports inside a half. A contact
distribution \(h(x)\delta(x-y)\) is already invisible to separated pairs.

## 2. The usable finite-resolution reduction

### 2.1 Covariance at a cut — PROVEN, with OPEN analytic premises

For one of the positive chains above define
\(F_i=E[F\mid U_i]\), \(S_i=E[\mathfrak S\mid U_i]\).
For \(0\le i<k\le n\), the Markov property gives
\(E[F_i\mid U_{i+1}]=F_{i+1}\) and the analogous identity for \(S_i\).
This is not a tower theorem for arbitrary nonnested sigma-fields: it
uses conditional independence of the past and future given \(U_i\).
Applying total covariance at each step and telescoping gives

\[
 \operatorname{Cov}(F,\mathfrak S)
 =\sum_{i<k}E\operatorname{Cov}(F_i,S_i\mid U_{i+1})
       +\operatorname{Cov}(F_k,S_k). \tag{4}
\]

For every scalar \(c\), positivity also gives
\(\sup_{U_j}|S_j-c|\le\sup_{U_k}|S_k-c|\) for \(j\ge k\).
Likewise \(\|F_j-EF\|_2\le\|F_k-EF\|_2\).
These are statements about one real positive chain. Complex source
tilts would need bounds on backward-kernel total variation and
denominators; positivity-based contraction does not extend to them.

Take \(k=n-J\) and \(\ell_J=\ell_{\rm ref}L^{-J}\). Assume, for every
fixed \(J\), finite constants and bounds uniform in the path parameter:

\[
 \begin{split}
 &Z_a^{-q}\|F_k-EF\|_2\le C_{R,F,v}(J)<\infty,
                                                        &&\text{(E)}\\
 &\tau_R(a,J):=\inf_c\sup_{U_k}|S_k-c|\longrightarrow0,
                                                        &&\text{(T)}\\
 &Z_a^{-q}\sum_{i<k}E|\operatorname{Cov}(F_i,S_i\mid U_{i+1})|
       \le\delta_{R,F,v}(J),\quad\delta_{R,F,v}(J)\longrightarrow0
       \ (J\to\infty).                                 &&\text{(D)}
 \end{split} \tag{5}
\]

Each bound need only hold for \(a\le a_0(R,F,v,J)\) with \(n>J\).
The \(R,F,v\) dependence is allowed; every fixed product order is covered.
An all-data sup bound for \(F_k\) about a scalar implies (E). That
stronger form removes any need to estimate the terminal marginal for
the observable as well as for the seam.

From (4),

\[
 \sup_t Z_a^{-q}|\operatorname{Cov}(F_{a,t},\mathfrak S_a)|
 \le \delta_{R,F,v}(J)+C_{R,F,v}(J)\tau_R(a,J). \tag{6}
\]

Given \(\epsilon>0\), first fix \(J\) with \(\delta(J)<\epsilon/2\).
Then choose \(a<a_0(J)\) so that \(C(J)\tau_R(a,J)<\epsilon/2\).
This proves N5. No uniform bound in \(J\), rate in \(a\), or prescribed
moving \(J(a)\) has been used.

This is the direct-cut improvement already proved in
CODEX_REVIEW_SPHERE2 F9, rebuilt here rather than claimed as new.
It avoids SPHERE2_55's unnecessary factor \(J+1\). The review correctly
rejects its proposed optimized moving-J rate without control of
\(C(J)\), \(a_0(J)\) and the transparency constants.

### 2.2 Why the conditional decay factor is not a physical mass gap

A sufficient **hypothesis** for (D), with intermediate large fields
included, is the renormalized one-step bound

\[
 Z_a^{-q}E|\operatorname{Cov}(F_i,S_i\mid U_{i+1})|
 \le\Gamma_{R,F,v}L^{p(n-i)}
        e^{-m d_0/(2h_{i+1})}, \tag{7}
\]

where \(m>0\), \(p\ge0\) and \(\Gamma\) are independent of the cutoff
and step. Setting \(j=n-1-i\), (D) follows with

\[
 \delta(J)=\Gamma\sum_{j\ge J}L^{p(j+1)}
       e^{-m d_0 L^j/(2\ell_{\rm ref})}\longrightarrow0. \tag{8}
\]

The ratio of consecutive summands is
\(L^p\exp[-m d_0(L-1)L^j/(2\ell_{\rm ref})]\), tending to zero;
hence the positive series converges and its tails vanish. This proves
the implication (7) ⇒ (D), not (7) for K_a.

At fixed \(j\), this exponential has **no cutoff dependence**. At the
finest levels it is extremely small, but the top levels and terminal
covariance remain. Calling it a mass of order \(1/h_{i+1}\) describes
the conditioned fluctuation problem. It is no assertion about the
Hamiltonian of the reconstructed unconditioned theory. In (6), the
top levels are handled by transparency, not by a physical spectral gap.

### 2.3 Exact failure of the decay-only shortcut

Let \(X,E,H\) be independent uniform signs, \(F=X+E\) and
\(\mathfrak S=X+H/3\). Conditional on \(X\), the covariance is zero;
the two conditional means both equal \(X\), so the total covariance
is \(E[X^2]=1\). The two local observables can be put at arbitrarily
distant sites without changing this computation. Perfect conditional
decay alone therefore does not imply N5. Choosing \(c(X)=X\) would
erase the entire missing term falsely. This is a **PROVEN logical
counterexample**, not a Yang–Mills measure or a NO-GO for the sphere.

Conversely, replace the seam conditional mean by \(\varepsilon_a X\)
with \(\varepsilon_a\to0\). The contribution becomes
\(\varepsilon_a\), despite the same completely correlated coarse
variable. Conditional transparency can remove a seam defect without
decorrelating the coarse law.

## 3. Infrared content and the order of limits

### 3.1 The distance πR/2 does not decide the issue

For observables near the pole, \(d_0\simeq\pi R/2-O(\rho_F)\).
This is a separation, not a theorem that its covariance decays. The
brief's statement that the route "needs decorrelation" is precisely
the **conditional failure scenario** at SPHERE55 §6, not an established
necessity. Equations (5)–(6) give the alternative: first remove the
seam's conditional image at every fixed resolution, independently of
the terminal marginal. Such bounds are UV in the operational sense
used by CODEX_REVIEW_SPHERE F11: only scales below a fixed physical
ceiling are integrated, with arbitrary coarse data retained.

That description does not make (T) easy or prove it. In particular,
the tower contraction moves a proved all-data estimate from a finer
fixed scale to a coarser one; it does not convert typical data into all
data or produce a missing estimate at the finer scale. The fact that
the coupling can be made small there does not exclude rough constrained
saddles or bad conditional normalization.

### 3.2 Typical fields leave an amplitude budget, not an automatic IR theorem

Here is a precise alternative to an unjustified supremum. At a fixed
cut put \(H=(F_k-EF)/Z_a^q\), \(r=S_k-c\), and let \(G\) be a good-data
event. If \(\|H\|_2\le C\) and \(\sup_G|r|\le\tau\), then

\[
 |E[Hr]|\le C\tau+C\|r\,1_{G^c}\|_2. \tag{9}
\]

Proof: split the expectation over \(G\) and its complement; use
\(E|H|\le C\) on the first and Cauchy–Schwarz on the second. More
minimally one may control \(E[|Hr|1_{G^c}]\) directly. If for some
\(p>1\), \(\|r\|_{2p}\le M\), Hölder gives
\(\|r1_{G^c}\|_2\le M P(G^c)^{(p-1)/(2p)}\).
All cutoff, J and normalization dependences in these products matter.

Small probability alone is insufficient. Let
\(P(B=1)=n^{-2}\), \(F=nB\), \(S=nB\), with \(n\to\infty\).
Then \(\operatorname{Var}F=1-n^{-2}\le1\), the good-event image is
zero, but \(\operatorname{Cov}(F,S)=1-n^{-2}\) and
\(E[S^2 1_{B=1}]=1\). Changing only \(S\) to \(B\) gives covariance
\((1-n^{-2})/n\to0\). This proves why the original-law **weighted
tail**, including insertion size, is required.

If that tail were proved by local large-field estimates, (9) could
close the remainder without distance-dependent coarse decorrelation.
Whether it can be proved here is **OPEN**. It is a named input from
the original-law/coercivity/tails work, not a result of this lane.
If neither (T) nor a weighted-tail replacement is available, the
coarse covariance remains OPEN; its mere presence does not prove that
every possible bound must be an IR decay theorem.

### 3.3 Infrared decay and a positive mass gap are different claims

Even a successful long-distance decay bound need not be exponential
or imply a gap. For an explicit logical comparison define

\[
 K(t)=\int_0^1 E^5 e^{-Et}\,dE\quad(t\ge0).
\]

Its reflection kernels are positive:
\(\sum_{ij}\overline z_i z_j K(t_i+t_j)
=\int_0^1 E^5|\sum_i z_i e^{-Et_i}|^2dE\ge0\).
Multiplication by \(E\) on \(L^2((0,1),E^5dE)\) has no positive
lower gap: vectors supported in \((0,\eta)\) have energy quotient at
most \(\eta\). Yet, for \(t\ge1\), substitution \(u=Et\) and five
integrations by parts give

\[
 \frac{e^{-1}}{6t^6}\le K(t)\le\frac{5!}{t^6}.
\]

Thus \(r^4K(r)\to0\) without a positive gap. This is a spectral
comparison, not a four-dimensional Yang–Mills model or proof of its
Ward bounds. It suffices to reject the logical inference "decay strong
enough to beat a polynomial shell volume ⇒ physical mass gap".
Requiring an unsupplied IR estimate would defeat a claimed **UV-only
reduction**, but would not by itself prove impossibility of existence
without a gap. These two meanings of NO-GO must not be conflated.

### 3.4 Fixed R first, then moments as R → ∞

For each fixed \(R\), finish the \(a\to0\) Ward limit using (6) and
the other named inputs. Its constants may depend on \(R\). Near the
pole set \(z=2x\). SPHERE55 §5.2 gives

\[
 g_R=(1+|z|^2/(4R^2))^{-2}\delta,\qquad
 v_R(z)=e+\frac{(e\cdot z)z-|z|^2e/2}{2R^2}.
\]

The latter is a rescaled sphere Killing field tending, with all
derivatives on each compact set, to translation by \(e\). Pole
rotations and coordinate reflections act exactly linearly. Any fixed
finite translation path of compact supports stays away from the seam
for sufficiently large \(R\). Assuming the common-domain local moment
bounds and equicontinuity in §1.3, one can pass these moment identities
to a subsequential flat limit. No clustering enters that passage.

For a lattice diagonal enumerate the **Cartesian product** of the
countable observable and group families, including the necessary
derivative/transport tests. At \(R_j\to\infty\), choose a fixed-R
continuum limit and then a sufficiently small cutoff approximating
its first j tested moments and Ward errors to \(1/j\). A subsequence
of the uniformly bounded moment vectors converges on the countable
family; equicontinuity extends within the specified common domain.
The contraction error tends to zero for each fixed test. This proves
the conditional diagonal mechanism without a radius-uniform Ward
rate. Pairing just the ith observable with the ith transformation
would not suffice (CODEX_REVIEW_SEAM F8).

Seam-contact Ward estimates are not needed for these cap paths. The
observable contact/positivity bridge is still needed. Uniform local
moments, nontrivial normalization and any H_int witness do not follow
from finite-volume compactness or from bounded coarse holonomies.

## 4. F13: what transfers to K_a, and what does not

**Verdict on F13: OPEN.** Geometry and normalized-kernel identities
transfer; the required analytic RG estimates have not been transferred.
This is a mismatch of hypotheses, not a theorem that transfer is impossible.

| Interface | Checked content | Remaining obstruction |
|---|---|---|
| Positive soft chain | Integrating each normalized forward kernel over its new variable gives 1. Markov identities (3)–(6) are geometry-independent. | Normalization gives no Hessian lower bound, conditional insertion estimate or large-field suppression. |
| Bulk patch | The local Wilson rule and bulk S4′ contour definitions agree where their stencils lie inside a chart. | LOC-T must prove the conditional estimates, with the actual exterior integration, source norms and boundary conditions. Equality of local formulas does not give equality of conditional laws or R-uniform constants. |
| Seam blocks and contours | There are nonrectangular boundary blocks, valences 5–9 and shortest-path contour averages rather than the producer's bulk block map. | Rebuild the constrained linear operators, inverse/locality bounds, nonlinear charts, determinant/source estimates and normalized large-field bounds on this family; match every producer's coarse-field domain. |
| Weights and metric | Use incident-cell sums. The frozen formula \(k_e\beta/4\) is not exact for variable \(\beta_Q\). | Profile bounds and geometry must be included in constants; no uniformly shape-regular physical-mesh theorem applies automatically. |
| Large fields | Sphere reflections do not furnish the torus's full family of translated reflecting planes. | The torus chessboard argument does not transfer by citing RP. Supply action-based, source-weighted large-field bounds including intermediate fields and actual normalization. |
| Coupling/source domains | The sphere consumes the chosen slowly varying radial profile and matched current. | FLOW-pos/LCS and the actual source-domain controls are separate OPEN inputs. Constant-coupling small-field theorems do not discharge them. |

Two explicit checks prevent those gaps from being hidden by "locality."

First, an integrated exterior can change a local marginal even when the
local interaction is unchanged. For signs \(x,y\) with weight
\(e^{Jxy+hy}\), summing y gives \(2\cosh(Jx+h)\), and summing x gives
\(E x=\tanh J\tanh h\). The coupling to the local site is fixed while
an exterior parameter changes its law. This is an elementary logical
example, not a gauge-theory counterexample. LOC-T must bound such
dependence, not assume it away.

Second, rebuild CODEX_REVIEW_SPHERE F15's physical-mesh obstruction.
Take \(m\ge2\), \(q_m=R/a=m+1/2+1/(2m)\) and boundary vertex
\(v/a=(m+1/2,1/2,1/2,1/2)\). Its adjacent cube centered at
\((m,0,0,0)a\) is retained, whereas its next outward cube is not.
Writing \(r_m^2=|v/a|^2=m^2+m+1\),

\[
 q_m^2-r_m^2=\frac{(m+1)^2}{4m^2},\qquad
 \frac{\operatorname{length}(C_v)}a
 =\frac{2q_m(q_m^2-r_m^2)}{q_m^2+r_m^2}
 \sim\frac1{4m}\longrightarrow0. \tag{10}
\]

For \(m\ge2\), \(q_m^2\) is noninteger whereas squared half-grid vertex
radii in four dimensions are integers, so these radii are generic.
At fixed R take \(a=R/q_m\). There is no uniform lower physical edge
length comparable to a. The action and graph may still support a
combinatorial proof; (10) does not refute it. It refutes only the
unjustified substitution of a uniformly regular physical mesh.

### 4.1 The two-sided seam cannot be discarded by symmetry

CODEX_REVIEW_SPHERE2 F3 supplies a genuine missed operator in the
proposed no-tuning argument. Transport both boundary connections to
one gauge frame and set \(J_i=A_i^+-A_i^-\),
\(F^\Sigma_{ni}=F^+_{ni}+F^-_{ni}\), with a fixed signed normal.
Both transform by conjugation under the common gauge group. Then

\[
 \mathcal O_3=\sum_i\operatorname{tr}(J_i F^\Sigma_{ni}) \tag{11}
\]

is gauge invariant and has dimension three on a three-dimensional
seam. Equatorial reflection changes both factors' signs; tangential
coordinate reflection changes the contracted components together.
Thus (11) is even under the stated symmetries. With a common Abelian
Lie-algebra direction T, \(J_1=jT\) and
\(F^+_{n1}=F^-_{n1}=fT\), it equals \(2jf\operatorname{tr}T^2\ne0\)
for suitable j,f,T. The single-connection exclusion of Chern–Simons
does not exclude this two-sided operator.

This defeats the exhaustive classification, **not N5**. For a positive
inner product, the elementary quadratic identity

\[
 K\|J\|^2+c\langle J,F\rangle
 =K\|J+cF/(2K)\|^2-\frac{c^2}{4K}\|F\|^2
\]

suggests an irrelevant residual when \(K\asymp u/a\) and the actual
coefficient c has sufficiently slow growth. For example bounded c
would give \(c^2/K\to0\). This is an **ARGUED mechanism**, conditional
on coercivity, coefficient bounds, other terms, normalized integration
and its Ward/source derivatives. None is proved for arbitrary coarse
data by completing a quadratic square.

Nor does a finite soft step impose exact gluing: the Wilson density
and all soft kernels are strictly positive at finite cutoff, so their
integrated coarse density is positive on every open set of mismatch
data. Asymptotic transparency remains possible. Finally, comparing
only "all jump" and "all kernel mismatch" misses intermediate
minimizers: \(A t^2+B(\Delta-t)^2\) is minimized at
\(t=B\Delta/(A+B)\), nonzero even for \(0<B<A\). Consequently the
suggested kernel threshold in SPHERE2_55 §2.4 is not a proved safe
interval (its Codex review F10). The interval must also satisfy the
separate constrained-Hessian requirement; neither may be chosen after
the other without a compatibility proof.

## 5. Minimal settling lemma and its strength

**ST(K_a), OPEN:** for the actual real Wilson profile, its actual
normalized soft chain, fixed finite R, every cap-admissible Killing
generator and every fixed \(\ell_J=\ell_{\rm ref}L^{-J}\), prove

\[
 \inf_c\sup_{U_{n-J}}
 \left|E_{a,R}[\mathfrak S_a(v)\mid U_{n-J}]-c\right|
      \xrightarrow[a\to0]{}0. \tag{ST}
\]

The supremum includes all boundary, chart and crossing data. The
constant is a single scalar. Rates may depend arbitrarily on R and J.
One may prove this only on an unbounded subsequence of fixed J's if
(E) and (D) also hold on it. For boosts, equivariance and oddness give
a symmetric range, so c=0 is optimal. No field-dependent subtraction
or conditioning on a good event is an allowed replacement for ST
without a bound such as (9) for its complement.

ST is the minimal **additional seam conditional-mean input in the
direct-cut architecture**, once the independent named inputs are:

1. **CD-K:** (D), or (7), for the full normalized one-step laws on K_a,
   including intermediate large fields and renormalized amplitudes.
2. **IMG-K:** (E), preferably its law-independent sup form, for every
   required product and path.
3. **BULK/ALG:** the W0/W1/W3, profile/domain, common OS-algebra and
   radius-uniform moment/extension hypotheses of §1.3.

Equations (4)–(8) prove ST + CD-K + IMG-K ⇒ N5. With BULK/ALG,
equation (1) and §3.4 give the intended conditional H_Euc/OS1 passage.
ST by itself does not settle the complete sphere construction.

This is a sufficient criterion, not a necessary characterization of
N5. It is stronger than vanishing of the actual tested covariances;
cancellations or the weighted-tail route (9) may suffice when ST fails.
It is an intermediate RG defect statement, not a renamed physical gap
or the full existence theorem. A cutoff sequence with nonvanishing
unavoidable oscillation of the seam image, even between rare coarse
configurations, would refute ST, but would not alone refute N5. A
nonzero constant image does not refute ST: its scalar is subtracted.

The most discriminating next task is a proof or counterexample for
(ST) at rough crossing data **on this K_a**, including the allowed
mixed operator, the actual backward conditional normalization, and a
compatible soft-kernel/Hessian interval. Source-radius, finite-coupling
kernel-remainder, and original-law coercivity/tail estimates remain
named coordinator inputs. This lane does not claim to supply them.
An actual NO-GO for N5 would need a nonzero normalized Ward covariance
along an admissible continuum sequence, or another necessary-condition
contradiction at that scope. No such witness has been obtained here.

## 6. Comparison with the flat route

| Question | Sphere route | Flat torus route |
|---|---|---|
| Remaining geometric Ward term | Net flux into the thin seam, N5. | Far-shell torque TQ after the bulk errors are controlled. |
| How it can vanish | Conditional seam transparency at every fixed finer resolution plus a summable fine tail; no terminal-law decorrelation in (6). | Cancellation of the actual limiting shell charge. Sampling-safe power-law decay is one sufficient route, not the only logical mechanism. |
| Present analytic gap | ST, CD-K/IMG-K, F13, profile matching and the common-algebra bridge are OPEN. | The actual Wilson TQ and all-order source/regularity inputs are OPEN. The torus geometry matches more of the producers. |
| Does it imply a gap? | No gap conclusion in the conditional construction. | TQ controls a particular symmetry charge; it is not equivalent to a physical mass gap. Polynomial decay can suffice. |
| Additional costs | Seam contour/hessian/source analysis, position-dependent coupling, action-based large fields instead of the torus chessboard. | No prism seam or sphere-profile transfer, but no sphere cancellation of the far shell. |
| State selection | A limit of the stated sphere regulators. | A limit of the specified flat Wilson regulators. Their identification is an additional theorem, not a consequence of either route. |

More explicitly, a uniformly sampled coarse stress covariance bounded
by \(C Z_a^q(1+|x|)^{-4-\eta}\), \(\eta>0\), makes a bounded-weight
four-dimensional annular torque at radius r at most \(C' r^{-\eta}\):
the annulus contains at most \(C r^4\) sites in reference units and
each summand is at most \(C r^{-4-\eta}\). Continuum radial envelopes
alone do not justify sampling a lattice; the bound here is pointwise
on the sampled sites. This is a **PROVEN sufficient estimate**, not
a Wilson decay result.

CODEX_REVIEW_TQ §1 and its bankable item 1 instead identify the limiting
Wilson torque with the negative derivative of the specified two-point
orbit, given its source/convergence hypotheses. Zero torque is then
equivalent to invariance **of that orbit**, not automatically of the
full OS algebra. Its §8 also permits different sphere and flat
selections; symmetry of one does not prove equality with the other.
ASSEMBLY55 N12/F19's SRC-E problem must not be reimported through a
flat-route sufficient condition. The conditional-image repair is
available as bookkeeping, not as a proved Yang–Mills producer.

## 7. Disposition and review boundary

| Item | Status in this deliverable |
|---|---|
| Exact N5 consumption and all-product/OS-domain distinction | PROVEN as the displayed conditional Ward/covariance implications; actual input estimates OPEN. |
| Positive Markov direct-cut bound and fixed-J limit | PROVEN; rebuilt prior result, no new rate claimed. |
| Decay-only and probability-only shortcuts | PROVEN counterexamples at the stated abstract scope. |
| Original-law weighted-tail alternative | PROVEN inequality; actual tail estimate OPEN. |
| Fixed-R UV route followed by moment limits | PROVEN conditional mechanism; its YM hypotheses OPEN. |
| Seam gluing/power-counting mechanism | ARGUED; mixed operator and arbitrary-data normalization must be handled. |
| Torus RG ⇒ K_a RG (F13) | OPEN; identities transfer, analytic estimates do not follow from the cited hypotheses. |
| Sphere-route verdict | **UNDECIDED**. No established GO and no established NO-GO. |

Source locators above are section/finding names, not claims that prior
review labels establish the hypotheses. Source identities, finite-check
results and fresh independent review are recorded in [N5B_LOG.md](N5B_LOG.md)
and the allowed checks/n5b_* artifacts. Finite checks validate only the
displayed probability algebra; they cannot establish ST or F13. Full
existence, non-freeness and the physical mass gap remain outside the
proved scope.

The preregistered finite rational checks completed with **26 PASS
criteria/control reports**, including all three shortcut detections;
the [successful output](checks/n5b_checks_run2_out.txt) also records the
resource guards. The first resource-setup failure is preserved separately
and is not counted as a numerical result.
