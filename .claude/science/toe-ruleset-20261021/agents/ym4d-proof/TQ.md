# TQ — the infrared requirement of the flat Euclidean-invariance route

**Verdict: UNDECIDED for the actual flat Wilson H_Euc route.** TQ is OPEN.
No proof here establishes its failure, or that proving it requires a mass
gap. The finite-volume ultraviolet comparison has a valid use without
clustering, but does not by itself remove the orientation of the period
lattice. The minimal remaining lemma is stated in §5, including the
all-observable requirement absent from the old two-point result.

Date: 2026-10-29. Status vocabulary: **PROVEN** means the argument printed
here proves its stated implication; **ARGUED** identifies a possible
mechanism; **OPEN** means its Yang–Mills hypotheses or conclusion have not
been supplied. No retained-status or audit verdict is assigned. This is
research on the supplied Wilson/RG model, not a derivation of that model
from the repository's minimal axioms. The RG programme is due to **Tadeusz
Balaban**, with **J. Dimock's** expositions; no literature theorem is used
as an unproved proof step here.

Source revisions, read coverage, resource limits and the independent review
are recorded in [TQ_LOG.md](TQ_LOG.md). The targeted consumers are
[ASSEMBLY55](ASSEMBLY55.md), N4 and N10–N14, not only N12. The source and
contact estimates below remain named inputs from other lanes.

## 1. Exactly what the existing flat argument consumes

Use [ROTDEF](ROTDEF.md) §§2–7 and E4–E6, with the qualifications in
[CODEX_REVIEW_TQ](CODEX_REVIEW_TQ.md) §1 and
[CODEX_REVIEW_SRCCD](CODEX_REVIEW_SRCCD.md) §§5–6. Fix SU(N), N≥2, a reference
length ell=1, a common tuned coupling trajectory, and **one selected
sequence** of even periodic Wilson tori with a_j→0 and R_j→∞. This is not a
supremum over all Gibbs states or all limit selections.

For separated smooth tests f,g, let O_a(f) be ROTDEF's clover-energy smear,
Q_s=exp(sJ) a coordinate-plane rotation, f_s=f∘Q_s^{-1}, and

\[
 \widetilde F_{j,s}=(O_{a_j}(f_s)-\omega_jO_{a_j}(f_s))
                     (O_{a_j}(g_s)-\omega_jO_{a_j}(g_s)),\qquad
 S_j(s)=Z_j^{-2}\omega_j(\widetilde F_{j,s}),\quad Z_j>0.
\]

Z_j is the common, state-independent field normalization on the chosen
trajectory; it is not the fine variance. Its nonvacuity is a separate
input. Do not silently replace it by 1 because SRCCD55 proposes that
normalization under additional, still open hypotheses.

Let psi_r(x)=h(|x|/r), with h=1 on [0,1] and h=0 on [2,∞), and v_r=psi_r Jx.
For the identity's matched symmetric stress representative T_j, define

\[
 \mathfrak T_{j,r}=\sum_x a_j^4\sum_{\mu,\nu}
             \nabla^+_\mu v_r^\nu(x)\,T_{j,\mu\nu}(x),\qquad
 t_j(s,r)=Z_j^{-2}\operatorname{Cov}_{\omega_j}
                      (\widetilde F_{j,s},\mathfrak T_{j,r}).                 \tag{1}
\]

The full discrete expression is retained. By the discrete product rule and
symmetry/antisymmetry, its support is r−a_j≤|x|≤2r+a_j. A nonconstant trace
does not cancel exactly under forward differences. Choose r≥r_F+ell and
r≤R_j/4−a_j so the shell does not wrap around the torus.

Write E_K for conditional expectation onto the actual soft coarse field,
nu_j for its law, and J_{j,r}=E_K mathfrak T_{j,r}. The normalized coarse
quantity consumed by ROTDEF is

\[
 q_j(s,r)=Z_j^{-2}\operatorname{Cov}_{\nu_j}
                      (E_K\widetilde F_{j,s},J_{j,r}).
\]

**The precise two-point TQ condition is**

\[
 \boxed{\lim_{r\to\infty}\limsup_{j\to\infty}
                    \sup_{0\le s\le2\pi}|q_j(s,r)|=0.}                  \tag{TQ2}
\]

The normalization and the order of limits matter. A fixed-r shell is used
only for eventually admissible j. Conditional images need not be strictly
local functions of the coarse field.

The actual N11 hypotheses needed for this reduction are:

- **U-pair:** the matched source estimate SRC-O and the corrected bulk/contact
  estimate SRC-W′ give, uniformly in s at each fixed r,
  \[
    |Z_j^{-2}\operatorname{Cov}(\widetilde F_{j,s},\mathfrak B_{j,r})|
       +|Z_j^{-2}\mathcal C_j(s)|
    \le C_F\{g_j^2+a_j^2\mathcal L(a_j)(1+r^5)\}\longrightarrow0.          \tag{2}
  \]
  Here mathfrak W=Xi S_W−div Xi for the Wilson action S_W,
  mathfrak B=mathfrak W+mathfrak T,
  and C_j=omega_j(Xi tilde F_{j,s})−d omega_j(tilde F_{j,s})/ds.
  In particular g_j=g_bare(a_j)→0 and a_j² L(a_j)→0 are hypotheses.
- **CD-mean:** the sufficient coarse-identification input is
  \[
   Z_j^{-2}\nu_j\bigl(|\operatorname{Cov}
       (\widetilde F_{j,s},T_{j,\mu\nu}(x)\mid U_K)|\bigr)
       \le C_F e^{-\mu\operatorname{dist}(x,\operatorname{supp}F)},
       \quad \mu>0,                                                       \tag{3}
  \]
  uniformly at admissible separations. It implies
  |t_j−q_j|≤C_F r⁴ exp[−mu(r−rho_F−1)]. A single random prefactor bounding
  every x is unnecessary. The reviewed graph-distance rate conversion and
  large-field moment qualifications must be preserved if (3) is derived.
- **E6-pair:** S_j and the two derivative-test correlations converge uniformly
  on the compact rotation orbit. This is needed for the converse below,
  not merely pointwise convergence of S_j.

All are **OPEN for the actual model at the required scope**. SRC-E′ means
coarse-image moments and separated conditional cumulants, with the product
image moment separately supplied. It does not assert a fine repeated-support
variance bound. The conditional exponential in (3) concerns eliminated
fluctuations, not the unconditional physical correlations. The proof below
can dispense with (3) altogether by using (1).

### 1.1 Library lemma: the fine charge and the defect — PROVEN conditional implication

Haar integration by parts gives
omega(Xi F)=Cov(F,Xi S_W−div Xi): integrate div(F Xi exp(−S_W)) on the finite
compact configuration space, then use F=1. Thus, exactly,

\[
 S'_j(s)+t_j(s,r)=
 Z_j^{-2}\{\operatorname{Cov}(\widetilde F_{j,s},\mathfrak B_{j,r})
                                      -\mathcal C_j(s)\}=:e_j(s,r).        \tag{4}
\]

The derivative of each centering constant multiplies a zero-mean factor,
so contributes zero to the derivative of the expectation. The Haar
divergence is not omitted. Under (2), ||e_j(.,r)||∞→0 at each fixed r.
Subtracting (4) at two fixed radii proves ||t_j(.,r)−t_j(.,r′)||∞→0.
The O(g_j²) contact is allowed in this subtraction and still vanishes.

Under E6, S_j→S and S'_j→H uniformly. Integrating the derivatives gives
S(s)−S(0)=int_0^s H(u)du, hence S′=H. Consequently

\[
 t_j(\cdot,r)\longrightarrow-S'(\cdot),\qquad
 \Lambda(r):=\limsup_j\|t_j(\cdot,r)\|_\infty=\|S'\|_\infty.               \tag{5}
\]

This is independent of fixed r. Therefore vanishing of the normalized
fine charge at **one** admissible fixed radius is equivalent to invariance
of this orbit. With (3), the triangle inequality and r⁴e^{−mu r}→0 make
(TQ2) equivalent to the same statement. Without E6, vanishing charge still
implies invariance by integration, but invariance of S need not force
convergence of derivatives. This rebuilds the used lemma rather than
promoting the earlier review's label to a proof.

Locality alone does not exchange joint and iterated limits. For example,
b_{n,L}=1_{L≤n²} tends to zero as L→∞ for each n, whereas b_{n,n}=1.
This is an array counterexample, not a Wilson counterexample.

## 2. Necessity: the charge is exact; absolute decay is only sufficient

**PROVEN.** Under §1's hypotheses, TQ2 is necessary for that selected
two-point orbit. It is not an additional stronger physical demand than
orbit invariance. An alternative successful proof of invariance would
imply TQ2; it need not use TQ2 as its intermediate estimate.

No absolute decay theorem is necessary for the integration of (4). In
particular, at any fixed admissible r_0, the weaker prelimit condition

\[
 \sup_{0\le u\le T}\left|\int_0^u t_j(s,r_0)\,ds\right|\longrightarrow0    \tag{6}
\]

suffices on that path. The difference is real without E6: t_j(s)=cos(js)
has primitives bounded by 1/j but supremum norm 1. This is only an analytic
example of the norms, not a model of the Wilson charge. Under E6, (5)
makes the all-endpoint version of (6) equivalent to zero limiting charge.

**PROVEN sufficient criterion, without a gap.** Define

\[
 A_F(r)=\limsup_j\sup_s\sum_{x:\ r-a_j\le|x|\le2r+a_j}a_j^4
       \sum_{\mu\nu} Z_j^{-2}
        |\operatorname{Cov}(\widetilde F_{j,s},T_{j,\mu\nu}(x))|.
\]

The shell coefficients are bounded by a fixed multiple of ||J|| ||h′||∞
for eventually a_j≪r. Therefore Lambda≤C A_F(r) at every fixed r. It
suffices that liminf_{r→∞} A_F(r)=0, even on sparse annuli. In particular,
the actual-site bound C_F |x|^{−4−epsilon}, epsilon>0, uniformly in j,s
at admissible sites, gives A_F(r)≤C′_F r^{−epsilon}. The shell has O(r⁴)
physical volume; no Riemann-sum substitution for an arbitrary sampled
envelope is made. This estimate is stronger than the signed condition
and is **OPEN** for Wilson Yang–Mills. It is a possible settling estimate,
not a proof of its own hypothesis.

**Repair to the RA shortcut.** TQ55's RA-1 proof bounded the fine variance
of tilde F by C Z_j⁴. Replacing the label SRC-E by SRC-E′ does not prove
that inequality: coarse L² bounds do not control the discarded conditional
variance. A legitimate repair must supply finite **separated reflected
autocorrelation** bounds and their required rate/product, or work directly
with (1)/(6). Even the balanced RA criterion remains conditional on those
actual autocorrelations. A stress autocorrelation c h^{−8}, c>0, does not
satisfy RA-1's o(h^{−8}) condition. This packet uses neither RA nor RA-1.

## 3. The proposed ultraviolet-only bypass on a flat torus

### 3.1 Fixed-volume comparison — PROVEN, with explicit strength

Rebuild UNIV55's Proposition T. On a common coarse space, let positive
unnormalized densities Z_1(V),Z_2(V) and conditional observables h_1,h_2
satisfy

\[
 \sup_V|h_1-h_2|\le\delta_c,\qquad
 \sup_V|\log Z_1-\log Z_2-c|\le\delta_d,\quad |h_2|\le M.
\]

Integration bounds the ratio of partition functions between exp(c±delta_d).
Thus the normalized density ratio lies in [exp(−2delta_d),exp(2delta_d)].
Splitting the expectation difference into the conditional-observable
difference and the density difference gives

\[
 |\omega_1(F)-\omega_2(F)|\le\delta_c+M(e^{2\delta_d}-1).                  \tag{7}
\]

If the difference of log densities is a sum of polymer terms with
sum_{X containing b} sup_V |delta P_X|≤eta(a), then delta_d≤N_b eta(a).
At fixed volume N_b is finite. **No infrared decay is used in (7).**
But both sup bounds are substantive inputs on every coarse configuration,
including large fields. Markov disintegration alone proves neither. Their
interpretation as purely ultraviolet needs the actual conditional
locality/control, not merely a new name for h_G.

For unbounded renormalized test polynomials, a proposed truncation extension
needs (7)'s comparison hypotheses for each fixed truncated observable
F 1_{|F|≤M}, and both expectations of |F|1_{|F|>M} must tend to zero
uniformly in the cutoff at this fixed volume. Comparison on a different
bounded algebra does not supply these truncated comparisons. Then take
a→0 first and M→∞ second. A collision-flat hierarchy is not
automatically an ordinary probability law with these moments. Alternatively
prove the comparison directly on its actual test domain. UNIV55's bounded
flowed-loop class has not been identified with the full N4 algebra.

### 3.2 A slow diagonal removes the volume factor, not the period orientation

**PROVEN diagonal observation.** If a comparison error tends to zero at
each fixed R, enumerate the countably many required observables and choose
R_n→∞, then a_n sufficiently small that the first n errors are <1/n and
a_n<1/n. Restrict to commensurate cutoffs if needed. This gives a selected
diagonal with vanishing comparison errors; no estimate uniform in R or
exponential clustering is needed. Compactness/convergence must still be
supplied for the chosen states. This is an existence selection, not a
claim about every previously fixed diagonal.

The remaining issue is geometric. Write omega^{G,P}_{a,R} for grid aG Z⁴
on the torus R⁴/(R P Z⁴). I denotes the original frame. For a rational
rotation Q and compatible cutoffs, exact transport of all regulator and
observable data gives

\[
 \omega^{Q,I}_{a,R}(F_Q)=\omega^{I,Q^{-1}}_{a,R}(F),\qquad
 \omega^{I,I}_{a,R}(F_Q)-\omega^{I,I}_{a,R}(F)
  =\underbrace{\omega^{I,I}_{a,R}(F_Q)-\omega^{Q,I}_{a,R}(F_Q)}_{\text{same-torus UV comparison}}
   +\underbrace{\omega^{I,Q^{-1}}_{a,R}(F)-\omega^{I,I}_{a,R}(F)}_{\text{period-orientation comparison}}. \tag{8}
\]

All observables are supported in a common embedded bounded patch. The
first difference can vanish by (7) and the slow diagonal. The second is
not an instance of (7) on the same fixed geometry with the same embedding.
The global field Jx does not descend to a general cubic torus: at x+Rz
it changes by RJz. Only rotations preserving the period lattice act as
rotations of that same torus. An isometry to a rotated torus transports
the observable as well; it does not set the second difference to zero.

Here is a precise limitation of fixed-volume regulator independence alone.
On a torus with orthonormal period frame P, assign a scalar Gaussian
mixture, with equal weights over i=1,...,4, whose component covariance
operator has Fourier symbol

\[
 [m^2+|p|^2+\lambda(p\cdot Pe_i)^2]^{-1},\qquad m>0,\ \lambda>0.
\]

It is a positive translation-invariant probability law on generalized
fields (positive Fourier variances), intrinsic to the unordered period
axes and transported covariantly when the torus rotates. Assign the
same law to every regulator: fixed-volume regulator comparisons are then
exact. As R→∞ the local covariance is the mixture of these Fourier
kernels. For P=I its values at p=t e_1 and p=t(e_1+e_2)/sqrt(2) differ by

\[
 \frac14\left\{\frac1{b+c}+\frac1b-\frac2{b+c/2}\right\}>0,
 \quad b=m^2+t^2,\ c=\lambda t^2>0,                                     \tag{9}
\]

by strict convexity of 1/x. The smooth-test infinite-volume limit follows
from Fourier Riemann sums; m>0 controls zero momentum and test decay
controls the ultraviolet tail. Thus geometric covariance, compactness and
regulator independence do not alone remove orientation selection. This
toy assignment is **not** Wilson theory, does not meet its matched stress
assumptions, and is not evidence that TQ fails there.

A sufficient, decay-free replacement for the second difference is

\[
 \omega^{I,Q^{-1}}_{a_j,R_j}(F)-\omega^{I,I}_{a_j,R_j}(F)\longrightarrow0
                   \quad\text{for every determining }F.                 \tag{VQ}
\]

It requires no rate, uniqueness or comparison of all boundary conditions.
It is nevertheless a statement about the selected large-volume laws,
and remains **OPEN**. Under the matching first difference in (8), it is
equivalent to invariance under Q on that selection, not a solved weaker
problem. UNIV55's absolute covariance summability is one sufficient method;
its review correctly rejects calling that method necessary. Cancellations
or a same-state reflection argument are still live alternatives.

## 4. Feasibility without a mass gap

**PROVEN at the level of logical requirements.** The signed-charge condition,
the polynomial shell estimate in §2 and VQ contain no positive spectral
threshold. Adding unconditional exponential clustering with a uniform
physical rate and normalized prefactors would meet the brief's **NO-GO
for that proposed shortcut**: it would import the mass-gap-level input the
task forbids using to establish feasibility. No such input is used here.
The conditional decay in (3) is bypassed in (4) and must not be relabeled
as unconditional clustering.

A gapless comparator can be rebuilt explicitly. The massless scalar
Gaussian field in four dimensions has positive covariance

\[
 C(f,g)=\int\frac{\overline{\widehat f(p)}\widehat g(p)}{|p|^2}
                      \frac{d^4p}{(2\pi)^4}.
\]

It is finite for smooth rapidly decreasing tests: near zero the radial
integral is proportional to int_0^1 r dr. It is rotation invariant by a
change of variables. Gaussian moments are sums of products of this
covariance, so all polynomial moments are invariant. In spatial Fourier
variables its time kernel is exp(−|k||t|)/(2|k|); across t=0 this is a
positive square kernel. Its spectral energies |k| reach zero with
nonzero weight in every positive neighborhood, so there is no mass gap.
These formulas establish compatibility of H_Euc with gaplessness, not
the Wilson construction.

There is also a separated stress-channel check. For F=phi(f)phi(g), define
one distant, centered stress insertion by point splitting
T_{mu nu}=d_mu phi d_nu phi−delta_{mu nu}(d phi)²/2 and subtracting its own
internal Gaussian contraction. Wick differentiation then gives, away
from the supports,

\[
 \langle F;T_{\mu\nu}(x)\rangle
 =\partial_\mu C_f(x)\partial_\nu C_g(x)
  +\partial_\nu C_f(x)\partial_\mu C_g(x)
  -\delta_{\mu\nu}\partial_\alpha C_f(x)\partial_\alpha C_g(x),
 \quad C_f=C*f,\quad C(x)=\frac1{4\pi^2|x|^2}.
\]

For compact supports, each derivative is O(|x|^{−3}), hence the mixed
insertion is O(|x|^{−6}) and its absolute shell bound is O(r^{−2}). This
calculation only defines the indicated separated insertion; it does not
assume a finite coincident stress variance or an ordinary random composite
field on all tests. It supplies a concrete gapless example of the sufficient
power count, with different observables from the Yang–Mills clover field.

**ARGUED feasibility; OPEN Yang–Mills theorem.** An actual model-specific
estimate of the signed stress channel, or VQ, might close the route without
a gap. RP alone supplies no rate: for alpha>0 the finite positive spectral
measure t^{alpha−1}e^{−t}dt/Gamma(alpha) gives the correlation
(1+h)^{−alpha}, by the substitution u=(1+h)t in its Laplace integral.
Its reflected kernel at h=s+t is an integral of positive squares, and an
atom at energy zero gives a constant. This proves only a limitation of
spectral positivity as a rate constraint. It does not exclude a Wilson
Ward/RP proof of signed-charge cancellation.

Similarly, the exterior tensor
sigma_{mu nu}=((Mx)_mu x_nu+(Mx)_nu x_mu)/|x|^6, M antisymmetric,
is symmetric and divergence-free off zero: differentiating gives
(d+2−6)(Mx)_nu/|x|^6=0 for d=4. Its flux for J is
|S³| tr(M^T J)/4, since int n_i n_j dOmega=|S³|delta_ij/4.
It is an analytic nonzero-flux witness, not a joint RP/Wilson correlation.
Neither this tensor nor the spectral example proves a Yang–Mills NO-GO.
A nonzero charge does not establish a pointwise rotlet asymptotic or a
unique Goldstone mechanism.

## 5. Minimal settling lemma and the all-observable interface

N4 consumes **every compactly supported test polynomial on one common
algebra**, while ROTDEF/TQ55 supply only the specified two-point orbit.
N10's insertion estimate stops at two further energy insertions. Even a
proof of TQ2 for every f,g would not by itself close H_Euc at all orders.

Here is the exact minimal endpoint lemma for this architecture. Let G_c be
the countable group generated by the Q fixed below, H(4), and translations
by vectors with four rational coordinates. Let D be a countable dense determining test family in
the actual common domain, closed under G_c. The H_reg extension must give
a continuous limiting functional S and a continuous motion action on that
test domain. Let P_j(F) be the normalized Wilson approximants, including
all specified subtractions, and set S_j^F(s):=omega_j(P_j(F_s)). Assume:

1. One common (a_j,R_j) sequence gives convergent expectations on D and
   preserves hypercubic symmetries; continuous translations of the limit
   follow from lattice translations and the supplied equicontinuity.
2. **U-all (OPEN):** for every F in D the finite-cutoff Ward identity holds
   for its full path F_s, with matched source/contact estimates making
   \[
     S^F_j{}'(s)+\tau^F_j(s,r_F)=e^F_j(s,r_F),\qquad
     \|e^F_j(\cdot,r_F)\|_\infty\to0,
     \quad\tau^F_j=\operatorname{Cov}(P_j(F_s),\mathfrak T_{j,r_F}),         \tag{10}
   \]
   at one fixed shell containing the whole path. This is a genuine
   all-order extension, not an asserted consequence of N11's pair input.

Choose the unit angular generator J in the (1,2) plane, zero on its
orthogonal complement, and theta=arctan(4/3) in (0,pi/2), so
cos(theta)=3/5 and sin(theta)=4/5.
The **minimal settling lemma** is

\[
 \boxed{\text{For every }F\in D,\qquad
       \int_0^\theta\tau^F_j(s,r_F)\,ds\longrightarrow0
       \text{ along that same sequence.}}                               \tag{TQ-min}
\]

**PROVEN implication and necessity relative to U-all.** Integrate (10).
TQ-min is equivalent to S(F_Q)=S(F), Q=exp(theta J), for every F∈D.
If theta/pi were rational, z=exp(i theta) would be a root of unity and
z+z^{-1}=6/5 a rational algebraic integer, impossible: a rational root of
a monic integer polynomial is an integer. Thus powers of Q are dense in
the (1,2)-plane circle. Conjugation by the exact hypercubic symmetries
gives the other coordinate-plane circles; successive plane rotations
eliminate the off-diagonal entries of an orthogonal matrix and generate
SO(4). Reflections supply O(4). Group stability of D and continuity extend
the equalities to its completed test domain. Together with translations,
this is H_Euc. Conversely H_Euc and (10) force each displayed integral
to vanish. No derivative convergence is needed for this endpoint argument.

This is a **target-equivalent residual**, not a proof of progress merely
from renaming H_Euc. The sufficient annular estimate in §2, proved for
all F with the U-all source matching, is a stronger, concrete producer
target. VQ for the same Q and D is another target-equivalent residual
if the all-observable fixed-torus comparison in (8) is supplied. Either
route must use the same state, normalization and coupling trajectory as
the other assembly inputs. The chosen Q admits commensurate even tori,
for example R_j/a_j divisible by 10; a free diagonal can respect this.

To change this verdict to **GO**, supply U-all and TQ-min/a genuine
producer estimate, or supply the all-observable universality-plus-VQ
theorem without needing the Ward route. A nonzero defect would refute
only the actual selection/domain exhibiting it. A **NO-GO** for flat
existence would have to exclude all admitted selections, or prove that
every continuation in the explicitly claimed scope needs the forbidden
gap-level input. Neither has been done.

## 6. Comparison with the sphere's UV-only claim

**PROVEN conditional distinction.** On the round sphere a global Killing
field obeys nabla_{(mu}v_{nu)}=0 and needs no compact spatial cutoff. A
matched symmetric continuum stress therefore gives no radial shell term.
At fixed radius, an actual UNIV-S comparison plus exact transport compares
the same geometry and the rotated observable, so it can establish SO(5)
invariance before any radius limit. On the cubic torus, (8) instead leaves
the period-orientation term.

Suppose invariant continuum sphere states mu_R have been constructed.
At a chosen pole N, exp_N(Qx)=diag(Q,1) exp_N(x) for Q∈SO(4). Covariant
observable maps therefore give SO(4) invariance of pulled-back local
correlations for every R; compatible convergent R→∞ limits preserve
these equalities without clustering. Reflections need an additional
reflection-invariant construction. For translations, sphere isometries
moving N a fixed tangent displacement act on bounded coordinate patches
as flat translations plus an error tending to zero; the supplied local
continuity/uniform bounds must control that error.

**OPEN construction requirements:** marginal coupling-profile matching,
all-product source/contact bounds, seam transparency including the allowed
two-sided operator, the correct great-sphere RP domain, the common
observable algebra, radius-uniform compactness/continuity and the witness.
These are named inputs, not outputs of this lane. Fixed-volume constants
can depend on R; passing to flat space still needs the separate compactness
and observable bounds. “UV-only” is valid for the specified **conditional
symmetry-restoration estimate**, not a completed theorem or a claim that
all long-distance construction issues disappear. Sphere and torus limits
are not identified without a state-selection comparison.

## 7. No-Go Discipline Gate — scope check, not a NO-GO certificate

**N1 — genuine alternatives.** The following were examined; no family is
claimed exhausted by the number of entries.

| Family | Attempt and present result |
|---|---|
| Signed Ward charge | ATTEMPTED: (4), (6), (10) give exact conditional reductions; TQ-min OPEN. |
| Absolute annular decay | ATTEMPTED: shell-volume proof gives a polynomial sufficient input; actual stress bound OPEN. |
| Fixed-volume universality and diagonal selection | ATTEMPTED: (7) removes susceptibility from that estimate; (8) leaves VQ OPEN. |
| Model-specific RP/analytic kernel route | Read scoped current import/review: same-state diagonal RP and stronger source/domain hypotheses remain OPEN; not ruled out. |
| Compact invariant geometry | ATTEMPTED conditionally in §6: no radial shell; actual sphere estimates OPEN. |

**N2 — dependencies, not independent wall counts.** Denote U=U-all,
T=TQ-min, and B=the all-observable UV comparison together with VQ on
matching selections. No pairwise independence is claimed.

| Pair | Implications established here |
|---|---|
| U,T | U alone supplies a remainder estimate, not T; T alone does not supply U. No nonimplication theorem on Wilson laws is asserted. |
| U,B | B proves rotational invariance under the common continuity/domain assumptions, not the Ward-source estimates U; the reverse relation is unresolved. |
| T,B | Given U and the UV half of B, T and VQ express the same invariance by (8), (10); do not count them as separate obstructions. |

**N3 — hidden premises.** The full argument explicitly retains trajectory,
normalization, nonvacuity, large-field coverage, contact terms, observable
domain, common selection, derivative convergence where used, and uniform
tails for the proposed bounded-observable extension. None is supplied by
the words ultraviolet, symmetry, or compactness alone. Phrase-scan results
are in the log.

**N4 — matching residuals.** CODEX_REVIEW_TQ §1 addresses the pair charge
and limit exchange; §4 addresses the fine-variance and RA-1 input; §6
limits the Goldstone classification. CODEX_REVIEW_SRCCD §§5–6 addresses
exactly N11's averaged decay/contact/product-image qualifications.
CODEX_REVIEW_UNIV §§1–2 addresses only fixed-volume comparison and the
overclaimed necessity of absolute summability. These match the narrow
uses here. The array, Gaussian assignment, spectral kernel and exterior
tensor are not counterexamples on the full Wilson premise set.

**N5 — resolutions actually considered.** Per insertion: centering and
normalization in (1)–(4). Per site: actual sampled shell bound, not a
Lebesgue-only envelope. Per mode: the explicitly defined Gaussian and
positive spectral kernels. Per block: N_b eta in (7). Whole state/limit:
(8), (10) with one sequence and determining domain. No numerical check at
any resolution or all-Wilson no-go is claimed.

**N6 — no new axiom needed for a mathematical repair.** Removing CD via
the fine identity, weakening absolute torque to its signed integral and
choosing a slow diagonal are legitimate reformulations. They do not prove
TQ-min or VQ. The registered kinetic-form isotropy primitive is acknowledged
at its stated scope; it is not a theorem about the interacting continuum
state. No axiom or registry edit is proposed.

**N7 — strongest counter-route to a NO-GO.** A Wilson-specific Ward/RP
argument could cancel the signed angular charge even when absolute stress
correlations decay too slowly for §2's bound. Alternatively, a same-state
orientation comparison could establish VQ without uniqueness or a rate.
The generic examples here satisfy neither the full matched Wilson Ward
package nor the source hypotheses of the current reflection-to-rotation
proposal. They cannot defeat either possibility. This is why the verdict
is UNDECIDED, with actual settling lemmas, rather than NO-GO.

**N8 — prior work and reopening.** The closest prior results are the
TQ/ROTDEF conditional reductions and the UNIV review's cancellation
counterexample to necessary summability. The newer
[Euclidean rotation import](EUCLIDEAN_ROTATION_IMPORT_ASTRA.md) and its
[review](REVIEW_EUCLIDEAN_ROTATION_IMPORT_ASTRA.md) keep same-state diagonal
RP, an ordinary-field/global-source bound and full external-theorem
verification open. Their bounded spectral cone does not prove rotation
invariance. Those unresolved routes leave a universal NO-GO unproved by
this packet. This lane neither certifies that external theorem nor
duplicates the active source,
coercivity, kernel or tail producers.

The N1–N8 discussion is a scope audit of an open research answer. There is
no negative-claim packet PASS, runner certificate, commit or landing claim.
