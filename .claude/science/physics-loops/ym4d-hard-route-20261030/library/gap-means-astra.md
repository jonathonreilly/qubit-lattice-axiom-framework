# Repo search

**READING.** The task-specific `prior/gap-means-astra.md` is absent at
`d6da3ddbaa64e454fc8fdf5333dbe4f3f269aa0a`. The lead's
`prior/repo-search-2026-11-08.md` concerns earlier UV targets. Its closest
hit is PR 10114's `MASS_GAP_LOCAL_BLOCK_ASTRA.md:106–149`: a positive
one-time-step plaquette correlation, not a lower bound for a mass.
I read that passage and its setting, lines 1–105 and 150–225. The same
note already supplies local ground-state density comparisons and the
mixed-boundary covariance identity. Those are prior work, not proposals here.

**READING.** Main `a527a6fda` has
`docs/NATIVE_GAUGE_TRANSFER_STRONG_COUPLING_GAP_NARROW_THEOREM_NOTE_2026-06-12.md`.
Its theorem is about an SU(3) coefficient-transfer packet at small beta.
It expressly excludes the continuum and infinite-volume physical gap.
Main's `GAUGE_VACUUM_PLAQUETTE_WINDOW_INTERTWINER_BASIS_DISPLACEMENT_BOUNDED_NOTE_2026-06-12.md:66–119`
already has two singlet pairings and their Gram normalization for SU(3).
Neither is the SU(2) physical seed. I do not rebuild either calculation.

**READING.** The closer method precedents are already recorded in
`gap-form-exercise.md:321–333`. I checked PR 10114's
`RTARGET.md:30–47` and `checks/review_massgap_block_literature.md:111–120`.
They retain the missing UV/IR join in the large-N analogy and distinguish
exact decimation from an unproved common twisted/untwisted interpolation.
Credit goes to the soft-route authors and their cited authors, including
Christoph Kopper, K. R. Ito and Erhard Seiler.

**READING; bounded search.** I searched main and PRs 10114, 10133, 10134,
10141 for conductance, minorization, ground-state comparison, exact duality,
and correlation-sign mechanisms, excluding this lane and the row 737 file.
The PR heads were `f76f6c649`, `89faef229`, `1e70c7211`, `fb99b4ddd`.
Broad filename hits are discovery, not a novelty certificate. Narrow
sign/loop searches and the local inventory found no copy of the two-loop
counterexample below. The nearest local sign warnings are
`prior/gap-math-lit.md:90–102` and `prior/gap-crux-lit-nonab.md:170–176`:
signed intertwiner amplitudes and no established general SU(2) Griffiths
inequality in the sources they read. Those warnings are prior work.
Full search records are in `/tmp/ym4d-gap-means-astra-t3IRy9/`.

**READING; ownership.** Searches of `open-registry.md`, `open-core.md`,
`l17c.md` and FINISH found no owner of the two-loop sign test.
The seed implications, even-sector limit, (KP), twisted-slab mixing and
the effective-action proposal already have their named files and rows.
They are used or discussed, not re-attacked here. Row 737's output was
not opened or searched.

## Provenance, marks and scope

Author: Codex; assignment FINISH 738, gpt-6-astra, max, 2026-11-11.
Independent author item. Research text, not an audit; no status is granted.
Only this file is an output in the checkout. No numerical proof or Lean
execution is used. Hand arguments are intended to be Lean-formalizable.

Marks: **PROVED** means a written argument here, not independently checked;
its repository standing is **argued**. **READING** reports a cited source;
**ARGUED** is an inference; **BELIEF**, **GUIDE**, and **OPEN** mean exactly
those things. A counterexample below applies only to its displayed claim.

**READING.** Ethan Sussman and Levent Alpoge, with Claude and Codex as
authors of their text, supply the outline and complete-account context.
I fetched each requested pinned source once. I used `sa-index/README.md`,
chunk rows and `obligations.md` before opening source ranges.
Outline 31858–31882 separates the scalar observable sector from a full
Yang–Mills algebra, and polynomial clustering from a spectral gap.
The account index for 4.12–4.19 concerns UV operators and admission.
CA-I 49495–49546 puts background supply outside its operator implication.
These passages do not verify an infrared seed. Tadeusz Balaban is credited
for the UV method discussed there; no unread Balaban estimate is imported.

## 1. The exact consumer

**READING.** Write the cutoff spacing as `a_j -> 0`, to avoid confusing it
with the integer time length `N`. Couplings `beta_j` are those of the
proposed continuum trajectory. For a spatial cube of `L` sites put

\[
 R_{j,L}=T_{j,L}/\lambda_{0,j,L},\qquad
 S_{\rm ev,j}(n;L^3)=\operatorname{Tr}(P_0R_{j,L}^{n})-1.
\]

The three `S_w` are exactly those in `gap-flux-exercise.md:495–517`.
For one fixed choice of `w`, the sufficient uniform seed is

\[
 \exists\ell>0,\ 0<q<1,\ N_j\ge3:\quad
 a_jN_j\longrightarrow\ell,\qquad
 5041S_{w,j}(N_j;(2N_j)^3)\le q
 \quad\hbox{for all sufficiently large }j.                 \tag{SEED}
\]

**ARGUED from the cited implication.** Its physical lower gap tends to
at least `log(1/q)/ell`. Strictness separately at each cutoff is not a
uniform margin. Theorem EV-L and the limit hypotheses still have to apply.
None of the mechanisms below supplies existence or observable convergence.

**READING.** Alternatively prove `(G_ev)` at every cutoff with a physical
lower gap bounded away from zero, and vanishing even thermal tails along
every defining sequence of large cubes. The quantifier is important:
`gap-flux-exercise-check.md:514–523` corrects an earlier one-sequence claim.
The continuum passage also needs the admitted limit data of the skeleton.

**READING.** The periodic seed counts seven electric sectors, the full seed
seven magnetic sectors, and the kappa seed seven diagonal electric/magnetic
sectors. The even sector alone suffices for the limit. It cannot simply
replace the crossing-symmetric trace in Theorem S. These are the results
of rows 731–732, not new reductions here.

**BELIEF, not an exclusion theorem.** In confining SU(2), magnetic sectors
are expected to become light; this disfavors the full seed. The periodic
and kappa seeds remain options. The inequality (KP) is not assumed.

## 2. A real attempt at route 1's first statement

**OPEN: elementary-source association (EP).** On every finite
four-dimensional hypercubic torus with sides at least four, ask whether

\[
 \operatorname{Cov}_{\boldsymbol\beta}
 \left(\prod_p W_p^{n_p},\prod_p W_p^{m_p}\right)\ge0
 \quad\text{for all }\beta_p\ge0,\quad n_p,m_p\in\mathbb N_0. \tag{EP}
\]

Only elementary plaquettes occur here. This is route 1's first proposed
statement, not a claimed theorem or a sufficient mass-gap criterion.

**PROVED reduction used in the attempt.** Define the unnormalized moments

\[
 C_\alpha(\boldsymbol\beta)=
 \int\left(\prod_pW_p^{\alpha_p}\right)
             e^{\sum_p\beta_pW_p}\,dU.
\]

Then (EP) is exactly `C_{n+m} C_0 - C_n C_m >= 0`, since `C_0>0`.
The finite integrals and their source derivatives exist: every `W_p`
is bounded and the graph is finite. The attempted proof integrates links
in these two-copy expressions, seeking a class of source functions with
nonnegative duplicate pairings. After link integrations, loop functions
must be retained. Two possible ways to close that induction are tested
below: enlarge to all contractible loop functions, or impose association
for elementary sources under every remaining exterior. Both fail.
This does not make either enlargement necessary for (EP).

**ARGUED proposed intermediate lemma, refuted below:**

> **(R1-POS)** For Wilson SU(2) with nonnegative plaquette couplings, the cone
> of finite nonnegative linear combinations of contractible Wilson-loop
> functions has nonnegative connected pairings. Thus
> `Cov(F,G) >= 0` for any two members of that cone. Repeated vertices and
> concatenated loops are included, as exact loop resolutions produce them.

This is the first attempted closure step in proving (EP). It is stronger
than (EP) or what a successful restricted correlation inequality might need.
It is not an assumption of Corollary EV or a consequence of reflection
positivity. The proof attempt below disproves (R1-POS) within Wilson SU(2).
The two test loops have length eight and a repeated base vertex. They are
not two elementary plaquette traces or two continuum action densities.

### 2.1 The two loops

**PROVED: construction.** Work on a four-dimensional periodic lattice,
each side at least four. Choose two elementary plaquettes `p,q` that
share only a base vertex. They lie in the coordinate planes `(1,2)` and
`(3,4)`. Their eight unoriented edges are distinct. Write their holonomies,
based at that vertex, as `U,V`. Set

\[
 F=\tfrac12\operatorname{tr}(UV),\qquad
 G=\tfrac12\operatorname{tr}(UV^{-1}).                         \tag{2.1}
\]

Both paths are contractible. Both functions are real and have norm at
most one. A gauge transformation conjugates both `U,V` at the base vertex,
so both functions are gauge invariant. Each centre flip meets an elementary
plaquette an even number of times; hence it fixes `F,G`. The functions
therefore belong to the local centre-blind class used by EV-L. They need
not be positive functions. Griffiths-type loop cones concern these real
Wilson functions, not only pointwise nonnegative observables.

### 2.2 Haar calculation, with no enumeration

**PROVED.** At beta zero, `U,V` are independent Haar SU(2) variables.
Each is a product of four independent Haar variables, on disjoint edge sets.
Write unit quaternions as

\[
 U=(u_0,\boldsymbol u),\qquad V=(v_0,\boldsymbol v).
\]

Haar measure is uniform measure on the unit three-sphere. Coordinate sign
symmetries and permutations, together with `sum u_i^2=1`, give

\[
 \mathbb E u_i=0,\qquad \mathbb E u_i u_k=\delta_{ik}/4,
 \qquad 0\le i,k\le3.                                       \tag{2.2}
\]

Quaternion multiplication gives

\[
 F=u_0v_0-\boldsymbol u\cdot\boldsymbol v,\qquad
 G=u_0v_0+\boldsymbol u\cdot\boldsymbol v.
\]

Consequently

\[
 \mathbb EF=\mathbb EG=0,\qquad
 \mathbb E(FG)=\frac1{16}-\frac3{16}=-\frac18.
                                                               \tag{2.3}
\]

This disproves (R1-POS) at beta zero. The subtraction has three vector
components and one scalar component. It is not a floating-point sign test.
The SU(2) quaternion trace convention is also used in Sussman–Alpoge,
outline 2775–2795; their positive reflected Gram expansion is a different
pairing from the one in (2.3).

**PROVED: a second hand check.** For fixed `V`, rotational invariance in
`u` gives `E_U(FG)=(2v_0^2-1)/4`. Integrating `v_0^2=1/4` gives `-1/8`.
This checks the normalization by conditioning, not by numerical sampling.
It is a self-check, not an independent review.

### 2.3 Strictly positive couplings, uniformly in the torus

**PROVED.** The counterexample persists for every

\[
                         0\le\beta\le1/1536.                \tag{2.4}
\]

It also persists for inhomogeneous real plaquette coefficients of absolute
value at most `1/1536`. Here the normalized Wilson density is proportional
to `exp(sum_p beta_p W_p)`, with `W_p=tr(U_p)/2`. The action's constant
term cancels from that density. In that case take `beta=max_p |beta_p|`.

Let `E` be the eight edges used by `F,G`. Conditional on all other edges,
only plaquettes touching `E` enter the conditional density. In dimension
four an edge touches six plaquettes. Thus at most 48 terms enter. Their
total log-weight `V_E` has oscillation at most `96 beta`. Relative to
product Haar on these eight edges, the conditional density `f` obeys

\[
 e^{-96\beta}\le f\le e^{96\beta}.
\]

For any real `H` supported on `E` with norm at most one this gives

\[
 |\mathbb E_\beta H-\mathbb E_0H|
 \le\delta,\qquad\delta=e^{96\beta}-1.                       \tag{2.5}
\]

Indeed `|f-1| <= e^{96 beta}-1` pointwise, and the bound holds for every
exterior. Averaging the conditional bound proves (2.5) in the full measure.
No thermodynamic limit or estimate on the exterior was used.

Apply (2.5) to `F,G,FG`, and use (2.3). Then

\[
 \operatorname{Cov}_\beta(F,G)
 \le-\frac18+\delta+\delta^2.
\]

For `0 <= x < 1`, the exponential series gives
`e^x <= sum_{n>=0} x^n = 1/(1-x)`. With `x=96 beta <=1/16`,
`delta <=1/15`. Hence, by displayed rational arithmetic,

\[
 \operatorname{Cov}_\beta(F,G)
 \le-\frac18+\frac1{15}+\frac1{225}
 =-\frac{97}{1800}<0.                                       \tag{2.6}
\]

The coefficient bound, edge count and arithmetic are all checkable by hand.
No assertion about the largest interval of negative covariance is made.

### 2.4 The even projection does not repair this sign

**PROVED, given Lemma MX of row 731 and the electric-seam identity.**
The latter is the `m=0` case of
`gap-flux-exercise-check.md:188–200`: replacing the closing spatial slice
by its centre flip changes signs only on the temporal twist stack.
Put the supports away from that seam. Each electrically twisted Gibbs
measure still has real plaquette coefficients `+beta` or `-beta`.
The proof of (2.5) therefore holds in each of them. Every positive
normalized mixture satisfies the same three moment bounds for `F,G,FG`,
regardless of its mixing weights.
Lemma MX expresses the even state as just such a mixture. Thus (2.6)
also holds for the finite-torus even state. No signed kappa measure is used.

**ARGUED consequence.** Centre-even projection is not a replacement for
a positive correlation structure. It removes global electric flux, not
the SU(2) signs in local loop composition. These are different operations.

### 2.5 Where the attempted proof fails, and what survives

**PROVED failure of the replica step.** For two independent copies of any
probability law,

\[
 2\operatorname{Cov}(F,G)
 =\mathbb E[(F(U)-F(U'))(G(U)-G(U'))].                         \tag{2.7}
\]

Expanding the four terms proves the identity. At Haar measure its right
side for (2.1) is `-1/4`. Thus a Ginibre-style proof that declares these
two loop differences to have a nonnegative duplicate pairing fails at
this exact integral. Positive Wilson character coefficients do not change it.

**PROVED scope of a possible repair.** Let `X=tr(U)/2`, `Y=tr(V)/2`.
The exact SU(2) trace identity gives `F+G=2XY`. In product Haar measure,

\[
 \operatorname{Var}F=\operatorname{Var}G=\tfrac14,\qquad
 \operatorname{Var}(F+G)=\tfrac14,\qquad
 \operatorname{Var}(F-G)=\tfrac34.                            \tag{2.8}
\]

The first two variances follow because `UV` and `UV^{-1}` are Haar;
the last two then follow from (2.3). Keeping the *paired* word `F+G`
does not encounter a negative variance. It does not license splitting
the pair into independently positive channels.

**OPEN.** A cone restricted to elementary plaquette sources, or one that
keeps such paired words throughout elimination, might obey a useful
inequality. This calculation neither proves nor disproves that claim.
Closure under the required four-dimensional integrations, a switching or
comparison estimate, and the sharpness dichotomy all remain to be supplied.
The elementary identity in (2.8) supplies none of them.

**ARGUED disposition.** The unrestricted closure lemma is false,
including at positive Wilson coupling and in the centre-even state. This
is a counterexample to one proposed tool, not to the target or to all M4
tools. It occurs in a strong-coupling range where gap methods already work.
Therefore unrestricted loop positivity is not necessary for a mass gap.

### 2.6 Trying an all-boundary elementary-plaquette repair

**PROVED counterexample.** Restricting to elementary plaquettes does not
rescue association if it is required for every exterior field. Take two
adjacent elementary plaquettes sharing exactly one edge `e`. Fix every
other link. Their other three-edge paths are disjoint. Set the first path
to `I` and the second to `-I`; this can be done by setting one link of the
second path to `-I` and the other five links to `I`. Write `U=U_e`.
Whatever the chosen plaquette orientations,

\[
 W_p(U)=\tfrac12\operatorname{tr}U,
 \qquad W_q(U)=-\tfrac12\operatorname{tr}U,
\]

since `tr(U^{-1})=tr U` in SU(2). The conditional Wilson density of `U`
is continuous and strictly positive on SU(2) at every finite beta,
including when all other plaquettes touching `e` are retained. If
`\mathcal E` is the full edge set, then

\[
 \operatorname{Cov}(W_p,W_q\mid U_{\mathcal E\setminus\{e\}})
 =-\operatorname{Var}(\tfrac12\operatorname{tr}U
                   \mid U_{\mathcal E\setminus\{e\}})<0.    \tag{2.9}
\]

Strictness holds because the trace is nonconstant and the density has
full support. At beta zero the value is `-1/4`. Conditional moments are
continuous in the exterior links, so the sign persists in a neighbourhood
of this exterior. It is not an artefact of a conditional version on a null set.

**ARGUED scope.** This refutes all-exterior association for elementary
plaquettes, not the unconditioned periodic elementary-source claim (EP)
below. It also does not refute all-boundary *mixing*: mixing bounds use
absolute influence, and can hold when a covariance is negative.

## 3. What each means would have to supply

**READING.** The four-means inventory is row 735's reading of examples,
not an exhaustive theorem about proofs. `prior/gap-precedent-lit.md`
read only Kopper's paper in full. It explicitly leaves the broader claim
unresolved. I retain that limit. In particular, the large-N example is
not a proved UV-to-IR construction for fixed `N=2`.

**ARGUED answer.** M1–M4 could supply a seed if their respective missing
model estimates were proved. None of the supplied sources verifies one
on the SU(2) cutoff trajectory. A fifth, direct geometric coercivity,
can be stated precisely, but presently lacks its SU(2) estimate too.
Changing the criterion does not manufacture the estimate that verifies it.

### 3.1 M1: a small activity at a fixed physical coarse scale

**OPEN sufficient statement.** For one seed, say the periodic one,
construct an exact, translation-compatible scalar polymer expansion for
the *entire* Wilson partition function on a coarse lattice of spacing
`h_j -> h > 0`. Require a convergent activity bound with an exponential
diameter weight, uniform in cutoff and torus, strong enough to give

\[
 \log Z_j(n)=f_j|n|+r_j(n),\qquad
 |r_j(n)|\le A\frac{V(n)}{h_j^4}
       e^{-c\,d(n)/h_j}.                                    \tag{M1}
\]

Here `V(n)=a_j^4|n|`, `d(n)=a_j min_mu n_mu`, and `A,c>0` are independent
of `j`. The same `f_j` is used in both tori. It suffices to prove this on
the aligned cubes used for the seed and their doubles. One concrete
activity target is an exact gas with connected supports `gamma` satisfying

\[
 \sup_x\sum_{\gamma\ni x}|z_j(\gamma)|
       e^{2|\gamma|}\le 1/100,                              \tag{M1a}
\]

together with its volume-compatible connected-log construction. The
small activity must control the remaining coarse field integral as well.
The displayed norm alone, without exactness and that compatibility, is
not asserted to prove (M1).

**PROVED conditional arithmetic.** On a cube of physical side `ell_j`,
the bulk cancels from `Phi=16 log Z(N^4)-log Z((2N)^4)`. Thus (M1) gives

\[
 \Phi_j(N)\le16 A(\ell_j/h_j)^4
       [e^{-c\ell_j/h_j}+e^{-2c\ell_j/h_j}].                 \tag{3.1}
\]

Choose `ell/h` large enough to make the right side strictly below
`1.9*10^(-4)`, then take aligned `ell_j -> ell`. Such a choice exists
because the exponential series bounds any fixed power by an eventually
smaller exponential. Theorem S-w then supplies a uniform seed margin.
This uses the existing seed theorem; it is not another propagation proof.

**Why absent: OPEN, with a theorem about the inadequate substitute.**
Small-beta expansions control a bare activity, but `beta_j -> infinity`
on the continuum trajectory. The supplied UV construction controls
small corrections around a retained field, not an infrared expansion of
the whole normalized law at a confining scale. Sussman–Alpoge's
OSF14–OSF15, outline 19745–19772, explicitly prove that pointwise polymer
control still leaves the field integral to estimate. Their empty-gas
counterexample forbids dropping that integral. This is already their result.

**BELIEF.** Sufficiently large physical blocks of confining SU(2) should
admit some effective description with weak long-distance dependence.
Neither confinement nor smallness in the particular norm (M1a) is proved
by that expectation. An absolute norm may be stronger than necessary.

**Smallest test — OPEN estimate, not a simulation certificate.** Specify
one exact block map and compute the first connected interaction between
two adjacent retained blocks, including their coarse fields and boundary
normalizers. Show a bound on that interaction in the proposed norm that
survives `a_j -> 0`. If it is merely a small UV correction multiplying an
uncontrolled joint coarse law, the test has not reached (M1a). This is a
necessary screening test, not a claim that two blocks suffice for the sum.
The stronger effective-action proposal `(P-c)` is already row 735's;
renaming it is no advance and it is not re-attacked here.

### 3.2 M2: a second controlled number after an exact transformation

**OPEN sufficient statement.** Give an exact transformation, including
partition-function normalization and the selected twists, to a defect or
representation ensemble on physical blocks. After all local color sums,
require its *connected* activities to satisfy (M1a), or prove (M1) directly.
The controlling number `rho` must obey a displayed convergence threshold
uniformly at the physical scale. Neither `rho` nor its bound may be defined
by assuming the seed or the unknown mass. This specifies what the second
number has to do; an explicit SU(2) producer is still missing.

**READING.** Credit Hendryk Pfeiffer and Robert Oeckl for the exact
representation/intertwiner dual described in `prior/gap-math-lit.md:90–102`
and `prior/gap-crux-lit-nonab.md:160–174`. Those readings distinguish
positive plaquette character coefficients from signed complete contractions.
Exact duality is already available; a positive dilute ensemble with the
needed estimate is not supplied there. Credit Kopper for the separate
large-N small factor; the full-read record does not permit setting `N=2`
in a theorem requiring sufficiently large N.

**Why absent: READING and OPEN, not a no-go theorem.** Neither `1/N` at
`N=2` nor a bare semiclassical activity is a demonstrated small parameter
at the mass scale. Moving a small-coupling formula to a scale where its
hypotheses fail is not a bound. A useful regrouping of signed terms is
still possible; negative individual terms do not rule it out.

**PROVED obstruction to one purported second number.** Haar averaging of
four fundamental SU(2) factors is a projection, not a strict contraction
of every color channel. The tensor `epsilon tensor epsilon` is nonzero
and invariant because `g epsilon g^T=epsilon` for `det g=1`; averaging
fixes it. Thus no estimate `||P_Haar v|| <= q||v||` with `q<1` holds for
all four-strand tensors. The factor `1/2` in a matrix-coefficient
orthogonality formula cannot be multiplied once per link while ignoring
the invariant contractions. The main-branch intertwiner note already
illustrates the need to retain multiple singlet channels; this is its
elementary SU(2) scope warning, not a new representation-theory mechanism.

**Smallest test.** Give the proposed `rho` before doing an RG induction.
Test it on one four-strand link with its complete invariant subspace,
then on a connected pair of blocks with the vacuum part subtracted.
A per-strand loss fails the first test above. A bound after actual
connected subtraction remains **OPEN**. It must control all external
representations used in the sum, not just a numerical truncation.

### 3.3 M3: exact closure

**OPEN sufficient statement.** Specify a class of complete block actions
`C`, an exact blocking map `R:C -> C`, and exact normalization factors.
Prove that the Wilson initial data reach a class satisfying (M1a), or an
explicitly diagonalizable seed, at scale `h_j -> h>0`, uniformly in `j`.
All induced loops and all sectors used by the chosen seed must be retained.
The unrestricted statement that a marginal is another probability law is
exact, but gives no usable closure or infrared estimate.

**READING.** Piazza and Shen's two-dimensional convolution/block-product
mechanism is recorded in `prior/gap-fullread-2.md:17–35`, from their full
paper. It closes on class functions, not on a single Wilson coupling.
Its conditional block independence is dimension-specific. The comparison
with Migdal–Kadanoff and the missing common interpolation is already in
the Ito–Seiler reading cited in Repo search. None of this forbids a
different exact four-dimensional class.

**PROVED counterexample to single-Wilson-coupling closure.** Even the
integration of one link between two plaquette factors produces a more
general class function. Put `W(A)=tr(A)/2`, `t=W(AB)`, and

\[
 K_\beta(A,B)=\int_{SU(2)}
       e^{\beta W(AU)+\beta W(U^{-1}B)}\,dU.
\]

The exponent is a quaternion linear functional whose coefficient has
squared norm `2+2t`. For a uniform unit quaternion `u`,
`E u_0^2=1/4` and `E u_0^4=1/8`. For completeness, write
`b=E u_0^2u_1^2` and `d=E u_0^4`. Invariance under
`u_0 -> (u_0+u_1)/sqrt(2)` gives `d=3b`; squaring
`sum_i u_i^2=1` gives `4d+12b=1`. Thus `d=1/8`.
The convergent exponential series and then the logarithm give

\[
 \log K_\beta(t)
 =\frac{\beta^2}{4}(1+t)
  -\frac{\beta^4}{96}(1+2t+t^2)+O(\beta^6).                 \tag{3.2}
\]

The expansion is uniform for `-1<=t<=1`: the linear functional is
bounded by two, so its Taylor tails have uniform factorial bounds; the
logarithm is analytic near one. The nonzero `beta^4 t^2` coefficient
excludes `K=c(beta) exp(b(beta)t)` on any interval of sufficiently small
positive beta. This is a counterexample to that proposed class, not to
exact convolution, tensor methods, or M3 in general.

**Smallest test.** Apply the alleged closed map to the two-factor integral
above and then to a four-dimensional link with all its adjacent plaquettes.
An enlarged class must keep the generated `t^2` and multiloop terms and
control their subsequent iteration. That control is **OPEN**. Merely
adding an unbounded hierarchy of unspecified coefficients is not closure.

### 3.4 M4: a correlation inequality and a quantitative alternative

**OPEN sufficient statement.** For a concrete periodic-seed proposal,
let `C_r` be a contractible planar square of side `r` lattice units. Define

\[
 v_j(r)=\limsup_{L\to\infty,\ L\ge4r}
       |\langle W(C_r)\rangle_{j,L^4}|,\qquad
 M_j=\limsup_{r\to\infty}v_j(r)^{1/(4r)}.                    \tag{3.4}
\]

This is a nonlocal order diagnostic defined without a mass or seed.
For example, a positive area tension gives `M_j=0`; the converse is not
asserted. Supply a parameter/source inequality and constants
`ell_*<infinity`, `0<q<1`, `delta>0`, all uniform in the cutoff, proving
the following alternative for the actual Wilson data:

\[
 \begin{split}
 &\text{there is }3\le N\le\ell_*/a_j
       \text{ with }5041S_{\rm per,j}(N;(2N)^3)\le q;\quad\text{or}\\
 &M_j\ge\delta.                                             \tag{M4}
 \end{split}
\]

Prove also `M_j=0` on this trajectory. The proposed alternative and that
exclusion are both **OPEN**; expected Wilson confinement is **BELIEF**
here. This diagnostic deliberately exposes the extra confinement input;
it does not supply a cheaper one. Another explicitly defined diagnostic
or a version yielding `(G_ev)` could be used, but needs its own theorem.
This is one precise sufficient target for a sharpness mechanism, not a
necessary form or a claimed SU(2) sharpness theorem.

**ARGUED necessary caution.** A usual subcritical/supercritical sharpness
theorem leaves its critical boundary to be treated separately. One cannot
replace it by “no order implies an exponential gap” at criticality.
Similarly, a seed for each finite bare beta, at an unspecified size,
does not control `a_j N(beta_j)`. Both the critical alternative and the
physical-size bound must be handled here. Local gauge invariance alone
does not exclude nonlocal flux order or a massless phase.

**READING.** Duminil-Copin and Tassion's sharpness method and the finite
Abelian gauge current/random-cluster analogies are the precedents in
`gap-form-exercise.md:175–193` and `prior/gap-crux-lit-cross.md:23–25,69–75`.
Their role here is a template for an alternative, not an imported SU(2)
inequality. Credit Hugo Duminil-Copin, Vincent Tassion, Malin Palö
Forsström, Fredrik Viklund, Paul Duncan and Benjamin Schweinhart.

**Why absent: COUNTEREXAMPLE for a broad implementation; OPEN otherwise.**
Section 2 refutes the unrestricted positive Wilson-loop cone and
all-exterior elementary association. It does not refute unconditioned
elementary-plaquette association, a paired-source cone,
absolute-value inequalities, or a sign-sensitive switching construction.
None of those alternatives is constructed in the cited material with
the parameter control required by (M4). Nor is the exclusion of the
ordered/critical alternative supplied. Both are substantive obligations.

**Smallest test: done.** The two-plaquette concatenations (2.1) already
defeat the broad loop-closure lemma. Before a further proof attempt,
write the restricted source class and verify that *every* required
integration and source derivative preserves it. The test must retain
paired words when their separate signs are invalid. Passing one pair
does not prove that closure, much less (M4).

### 3.5 A fifth candidate: geometric coercivity of physical time

**OPEN proposal, not an established new means.** A direct geometric
bound on the actual physical transfer Dirichlet form could bypass a
perturbative expansion. It needs a separate estimate on the number of
states. The following two statements specify its full price.

Let `psi_{j,L}>0` be the periodic transfer ground state, normalized in
Haar `L^2`. Put `pi_{j,L}=psi_{j,L}^2 dU`. Work on gauge-invariant,
centre-even functions. Choose a fixed physical time `tau>0`, let
`k_j=ceil(tau/a_j)`, and define the physical-time Doob kernel

\[
 P_{j,L}f=\psi_{j,L}^{-1}R_{j,L}^{k_j}(\psi_{j,L}f).
\]

It is reversible for `pi`; conjugation is unitary between the indicated
weighted and unweighted Hilbert spaces. The proposed geometric estimate is

\[
 \frac12\int\pi(dx)P(x,dy)|f(x)-f(y)|^2
       \ge c\operatorname{Var}_{\pi}(f),\qquad 0<c<1,       \tag{M5-G}
\]

for every such `f`, every sufficiently fine cutoff and every sufficiently
large spatial cube, with the same `c,tau`. A conductance or isoperimetric
proof for this particular joint law would be a geometric producer.
Writing (M5-G) itself is a variational restatement of the missing gap,
not a discovery of that producer.

Define `H_{j,L}=-a_j^{-1}log R_{j,L}` on the even physical space. The
second proposed estimate, with `R=a_j L`, is

\[
 \operatorname{Tr}_{\rm ev}e^{-tH_{j,L}}
       \le\exp\{C[1+(R/t)^3]\},
 \qquad \tau\le t\le R/2,                                  \tag{M5-H}
\]

with `C` independent of cutoff and cube. This is a quantitative thermal
state-count bound. It must include all admitted even excitations.
Finite-dimensionality after a numerical representation cutoff is not a proof.

**PROVED conditional implication.** The left side of (M5-G) is
`<f,(I-P)f>_pi`. Hence every nonconstant spectral value of `P` is at most
`1-c`. For `a_j<=tau`, `a_j k_j<=2tau`; consequently

\[
 m_{\rm phys}\ge m_*:=\frac{-\log(1-c)}{2\tau}>0.
\]

Extend `S_ev` to positive real exponents by spectral calculus for the next
display. For `t=R/2` and `R>=4tau`, the positive spectral sum gives

\[
 S_{\rm ev,j}(t/a_j;L^3)
 \le e^{-m_*t/2}\operatorname{Tr}_{\rm ev}e^{-tH_{j,L}/2}
 \le e^{-m_*R/4+65C}.                                     \tag{3.3}
\]

For integer time use `n=floor(L/2)`. When `L>=4` and `R>=8tau`,
`a_j n/2>=R/8>=tau`, and the same proof gives the looser bound
`S_ev,j(n;L^3)<=exp(-m_*R/8+513C)`. Thus the tails vanish on
every sequence of large cubes and the physical gap is uniform: `(G_ev)`.
This calculation explains why both estimates, not positivity alone, are needed.
The gap-plus-free-energy reductions in `gap-phys-seed.md` are prior work;
(3.3) is only the explicit interface for this proposed geometric supplier.

**Why absent: OPEN, not a counterexample to SU(2).** No estimate read
controls the geometry of `psi^2 dU` in (M5-G) at a fixed physical time
uniformly in transverse volume and cutoff. The local comparisons of
`MASS_GAP_LOCAL_BLOCK_ASTRA.md:79–104` cost an exponential in
`beta` times the number of block edges. At fixed physical block size
that number grows with the cutoff. Those comparisons do not give (M5-G).
The bound (M5-H) is also an additional input, not a consequence of a
strictly positive gap for each finite lattice.

**ARGUED distinction.** An LSI or a gap for the four-dimensional
configuration-space Langevin process concerns a different operator.
The integrated-Hessian criterion of Bauerschmidt, Bodineau and Dagallier,
read in `prior/gap-fullread-2.md:49–70`, still needs its model-specific
curvature estimate and a physical-transfer bridge. It does not identify
that process with `P_{j,L}`. Credit Roland Bauerschmidt, Thierry Bodineau
and Benoit Dagallier for that conditional method.

**Smallest test.** On one fixed physical block, identify the exact joint
law `pi(dx)P(x,dy)` after all fine variables have been integrated.
Bound its conductance or a form comparison without an exponentially
cutoff-dependent minimum density. Then test the bound on growing cubes.
This is **OPEN**. Simple Perron eigenvalues at each cutoff are insufficient:
the positive matrices `[[1-epsilon,epsilon],[epsilon,1-epsilon]]`,
`0<epsilon<1/2`, have gap `2epsilon -> 0`. This is a counterexample to
an inference from positivity, not a model of Wilson SU(2).

**ARGUED classification.** If a geometric argument actually proves
(M5-G) and (M5-H) without a perturbative parameter or exact closure,
it deserves the fifth label. If it obtains them by a small interaction,
an exact dual, or a sharpness inequality, it belongs to M1, M2 or M4.
The names are not evidence, and they need not exhaust future methods.

## 4. Three proposals, ranked for a decisive test

**ARGUED ranking.** This is an order for testing concrete mechanisms,
not a claim that three viable proofs are known. Route 1's first statement
(EP) remains open after the proof attempt: two proposed closure steps
failed, while a free two-plaquette control holds. M1 without a produced small activity
and M3 without a closed class are specifications, not additional ranked routes.

| Rank and means | First statement to prove | Where it fails first; disposition |
|---|---|---|
| **1. Correlation/replica sharpness, M4.** Seek a parameter inequality that forces a seed before a fixed physical size, or an independently excluded form of order. | Prove or refute **(EP)**, the explicit elementary-source association statement in Section 2. Even if true, a switching/comparison inequality and (M4) remain additional steps. | **OPEN; two proof paths fail.** Enlarging to the full contractible loop cone fails at (2.3), (2.6). Requiring elementary association under every exterior fails at (2.9). A proof must preserve a smaller, explicitly stated source structure; no such four-dimensional induction is supplied here. |
| **2. A second number in the exact dual, M2.** Sum local intertwiner channels before estimating the connected defect gas. | Construct the exact, volume-compatible block activities of Section 3.2 and prove **(M1a)** at `h_j -> h>0`, with every representation, vacuum factor and source/twist read needed by the seed retained. The estimate must come from an explicitly identified `rho`, not from an assumed mass. | **OPEN:** no controlled `rho` for fixed SU(2) at that scale has been produced. The local shortcut “one inverse dimension per link” fails because Haar averaging fixes singlets. Exact duality and positivity of character coefficients leave this step open. A finite block test can reject a proposed `rho`; it cannot prove the whole activity sum. |
| **3. Physical-time geometry, fifth candidate.** Control bottlenecks of the actual even ground-state law, then its thermal state count. | Prove **(M5-G)** with fixed `c,tau`, uniformly in cutoff and large cube. Prove **(M5-H)** before claiming `(G_ev)`. | **OPEN:** the measure contains the unknown Wilson ground state. Existing local density estimates deteriorate with the number of fine edges. Bare Haar curvature and a Langevin LSI do not estimate this physical-time form. This is a different place to attempt the gap estimate, not a reduction in its present difficulty. |

**ARGUED reason for the order.** A correlation structure offers an
algebraic test before requiring a long multiscale construction; Section 2
actually performs such a test. The exact dual at least supplies the correct
model variables, but not a small parameter. Geometric coercivity addresses
the even sector directly but exposes an unknown ground-state law and a
second state-count obligation. No comparison here makes one of these
necessary, exclusive, or the final possible route.

**OPEN: the exact point left in route 1.** Only elementary plaquettes
occur in (EP). Section 2 does **not** refute it: the separate words `F,G`
are not positive polynomials in the two elementary traces `X,Y`.
Nor is (EP) proved here or asserted sufficient for (M4). An attempt needs
to decide (EP) and the closure/switching obligations separately. No row is
created and no existing owner is reassigned by stating this possible test.

**PROVED diagnostic on a repair, not a new gap lemma.** For just the two
independent Haar plaquettes, the elementary polynomial cone passes (EP).
Odd moments of `X` vanish. Even moments are nonnegative. For powers of
one variable, odd/odd covariance is an even moment, mixed parity gives
zero, and even/even covariance is nonnegative by

\[
 2\operatorname{Cov}(R^r,R^s)
 =\mathbb E[(R^r-R'^r)(R^s-R'^s)]\ge0,\qquad R=|X|.
\]

Independence of `X,Y` and nonnegative moments then give the product-power
claim: each joint moment is at least the corresponding product of moments,
and multiplying these two nonnegative inequalities preserves the order.
This shows explicitly why the failed loop-cone extension cannot be used
to dispose of (EP). Four-dimensional interacting closure remains open.

## 5. What not to do

The following are **ARGUED work restrictions** from the results and
source scopes above, not impossibility claims about all approaches.

- Do not reprove the seed propagation or the even-sector limit. Rows
  731–732 already supply them. Do not duplicate (KP), twisted-slab mixing,
  or `(P-c)` under a new name.
- Do not treat M1–M4 as an exhaustive classification. The precedent
  reading is incomplete, and the four-means rule is a selection rule.
- Do not treat a small UV correction as a small *full* infrared law.
  Keep the remaining field integral, its normalization and its source map.
  Sussman–Alpoge already isolate this issue in OSF15.
- Do not infer termwise positive loop correlations from a positive
  Boltzmann density, character coefficients, or a reflected Gram series.
  Section 2 gives an actual SU(2) counterexample to that inference.
  Conversely, do not use its self-intersecting loops to claim (EP) false.
- Do not replace fixed SU(2) by large N, a heat-kernel action, a finite
  representation truncation, or a hierarchical recursion without an exact
  comparison of the requested Wilson observable and thermal quantities.
- Do not count a finite-lattice Perron gap, a Langevin gap, or qualitative
  uniqueness as a physical uniform gap with a thermal-tail bound.
- Do not infer the cutoff-uniform seed from absence of a finite-beta
  transition alone. The seed's physical size and strict margin still need
  quantitative bounds. A sharpness argument must also treat criticality.
- Do not argue that centre-even projection removes local non-Abelian
  signs, or that centre-blind means only integer-spin plaquette labels.
  The contractible fundamental loops in Section 2 are centre-blind.
- Do not optimize the seed's numerical threshold before producing an
  input that crosses a threshold. No numerical calculation was needed
  for the counterexample or any conditional arithmetic in this note.

## 6. Evidence, limits and handoff

**PROVED here, not independently checked:** the two-loop covariance
`-1/8` at Haar measure; its strictly negative uniform bound
`-97/1800` for `0<=beta<=1/1536`; its extension to the even-state mixture;
the all-exterior elementary-plaquette counterexample at every finite beta;
the stated limitation on one-parameter Wilson closure; and the conditional
arithmetic from (M1) or (M5-G,H) to the existing consumers. The standard
quaternion and tensor identities are not claimed as new mathematics.

**OPEN:** every uniform SU(2) seed, `(G_ev)` on the continuum trajectory,
the narrower inequality (EP), its useful closure, a dual second parameter,
and the two geometric estimates. No mass gap or confinement at coupling
of order one is proved. The local counterexample does not distinguish
confining from massless phases; it distinguishes an invalid positivity
proof from a valid possible one.

**READING limits.** The literature statements above use the named
repository readings, with their stated limits. Their primary references
include [Pfeiffer–Oeckl](https://arxiv.org/abs/hep-lat/0110034),
[Kopper](https://arxiv.org/abs/math-ph/9902020),
[Piazza–Shen](https://arxiv.org/abs/2610.35286), and
[Duminil-Copin–Tassion](https://arxiv.org/abs/1502.03050).
These links do not claim a fresh full-paper reading. Two attempted new
PDF downloads, using Python with `-I` in the initially empty scratch
subdirectory `papers/`, failed local TLS certificate verification.
No paper was obtained, no verification was bypassed, and no new primary
proof is attributed to those attempts. Web-discovery results supplied no
proof input. The pinned outline and CA-I curl downloads succeeded.

**READING provenance.** The checkout HEAD moved during the session from
the task pin to `90bf9e6f50`, a queue-only commit. Fourteen named scientific
source files were compared by blob hash to `d6da3ddbaa`; none changed.
A concurrent working-tree edit of FINISH was observed and left to its
owner. This author wrote only `library/gap-means-astra.md`, did not inspect
the row 737 output, and made no commit or external post.

**ARGUED next decision.** Do not continue the unrestricted loop-positive
proof. Any new M4 brief should state its restricted observables and the
first closure identity before launch. A proposed M2 or geometric brief
should exhibit its concrete small parameter or coercive estimate first.
The full criterion statements above are obligations, not evidence that
those producers exist. An independent reader should check Section 2,
especially the twist-mixture extension, before any later note relies on it.

RESULT: argued, not independently checked: a hand counterexample refutes unrestricted contractible Wilson-loop association even in the centre-even state at small positive coupling; M1–M4 and a geometric fifth candidate have explicit uniform obligations and three ranked test routes, but no SU(2) seed or mass gap is established.
