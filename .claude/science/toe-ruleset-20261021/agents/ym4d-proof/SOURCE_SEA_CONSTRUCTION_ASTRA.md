# A one-level sea estimate from a reflection-positive defect penalty

## Contract, inputs and falsifiers

Author unit, Astra/max, 2026-10-29. Claim type: bounded theorem; independent
review pending. This unit estimates an actual one-level sea integral **after
integrating the coarse field with its actual reference weight**. It supplies
neither a fixed-coarse-field logarithm nor a continuum existence or mass-gap
theorem.

The frozen predecessor is
[SOURCE_LOCAL_HISTORY_RETURN_ASTRA.md](SOURCE_LOCAL_HISTORY_RETURN_ASTRA.md),
SHA-256 `d2e9c49eedceb14b654f5be640e2b55efc16b902fd789acbc3d73c2849b9a850`;
its complete [independent review](REVIEW_SOURCE_HISTORY_RETURN_ASTRA.md) has
SHA-256 `a0205f0074b1e2a835eba453dae80ef7fb64b09aa792bd46e3d87aa3daf9b2d0`.
The [review receipt](checks/review_source_history_receipt.json) has SHA-256
`6b1e1ff3e62051063182e7d92e0c1b9c6e1dc3fe598ab15f7703a6fec55868f9`.
Their identities are checked in the accompanying manifest. H1–H28, including
the failure terms and the conditional SU(2) counterexample, are unchanged.

**Target.** Price exact rough-field histories in the actual joint bare
Wilson/normalized-soft measure, relative to a common good-field reference,
on every finite even four-dimensional torus. Keep arbitrary rough collars,
coarse mismatch and original Wilson-coefficient sources. A full-partition
probability bound alone is not the target: [HW §3.1](HW.md) already explains
why it cannot supply the reference ratio.

**New step.** Preserve site-reflection positivity along a uniform penalty for
bad *closed fine cells*. A cap lower bound is independent of that penalty.
Take its infinite-penalty limit only after applying the chessboard estimate.
This gives exact defective-set weights relative to the all-good weight,
uniformly in volume. Then use the actual product kernel on clean contour
regions, leaving contaminated coarse links unrestricted inside the enlarged
defect support. This is an exact, correlated history expansion, not an
assumed product gas.

The checks were specified before checker execution: actual four-dimensional
cell/plaquette incidence and reflection support; an independently enumerated
finite gauge measure along the entire penalty interpolation; exact reference
and hole identities; normalized coarse kernels and correlated hard insertions;
noncommuting SU(2) reflection and the actual SU(2) kernel normalizer; source
budget and cutoff-scaling arithmetic. Controls remove the penalty, reference
weight, kernel normalizer, shared-plaquette multiplicity, contaminated-link
exception or correlated insertion. Finite checks are diagnostics; the
uniform conclusions below require the written proof.

The coordinator owns git, PR #10114, the lock and shared summaries. This
worker owns only this note and `checks/source_sea_*`. Current-main methodology
is `ca2bc7ddf64790da96cd43d42017d000fbfe4808`, freshly fetched by the
coordinator and read through `git show`. The installed physics-loop and
review-loop skills were read; the current-main research, delivery, claim and
primitive procedures govern. The finite SU(N) Wilson model is explicit
mathematical input. No framework axiom, primitive, physical identification,
audited status or accepted running-coupling theorem is added.

## 1. Actual measures and the two references

Let the fine torus be `Lambda=(Z/nZ)^4`, `n=LT`, with odd fixed `L>=3` and
even `T>=2`. Set `v=|Lambda|`, `D=N^2-1`, `N>=2`, `u>=1`, and fixed
`0<kappa_min<=kappa<=kappa_max`. This even-torus restriction is explicit; the
predecessor identities continue to hold on their larger domain.

Use normalized probability Haar on each oriented positive fine and coarse
link, the reversed link being its inverse. Exactly as in H1,

    s(U_p)=1-Re tr(U_p)/N=||I-U_p||_F^2/(2N),
    w_0(U,V)=exp[-u sum_p s(U_p)] product_c k_(kappa u)(V_c;Mbar_c(U)),
    k_t(V;M)=exp[-t phi_M(V)]/N_t(M),
    phi_M(V)=1-Re tr(V^-1 M)/N,
    N_t(M)=int exp[-t phi_M(W)] dW.                         (Sea1)

`Mbar` is the actual arithmetic mean of paired S4′ transporters, not its
polar projection. In particular `int k_t(V;M)dV=1` pointwise in U. Define

    Z_W=int exp[-u sum_p s(U_p)]dU=int w_0(U,V)dU dV,
    Z_cut,tot=int Z_cut^0(V)dV,
    dbar_nu_cut(V)=Z_cut^0(V)dV/Z_cut,tot.                   (Sea2)

The conditional sea `nu_cut^0(U;V)` and `Z_cut^0(V)` are precisely H5.
The measure on V in (Sea2) is essential; it is not uniform Haar. No
field-dependent kernel normalizer is discarded in deriving the fine marginal.

For each fine site x let `C_x=x+[0,1]^4` be its closed fine cell and put

    G_x(U)=1{max_(p subset C_x)||I-U_p||op >= delta},
    A(U)={x:G_x(U)=1},
    Z_delta=int exp[-u sum_p s(U_p)] 1{A(U)=empty}dU.       (Sea3)

Here `0<delta<=epsilon_1<=1` is fixed before u or volume varies. Every
plaquette belongs to four closed fine cells. Consequently `A=empty` is exactly
the condition that every fine plaquette, including inter-block plaquettes,
has norm defect below delta. It implies all the original cube-interior cuts.
The exact reference comparison is

    0<Z_delta<=Z_cut,tot<=Z_W.                              (Sea4)

`Z_delta` is a stronger reference introduced for this proof, not a renamed
H5 reference. The final bounds can use the original integrated reference by
(Sea4). All these quantities include their actual vacuum and Haar factors.

## 2. Penalty interpolation and an all-volume reference bound

Choose `c_H in (0,1]` with
`Haar{||U-I||op<=r}>=c_H r^D` for `0<r<=1`. This follows from the positive
Haar density in a fixed exponential chart. Put

    r_delta=delta/8,
    a_delta=delta^2/(8N),
    C_delta=exp(48 r_delta^2)c_H^(-4)r_delta^(-4D),
    q_delta(u)=C_delta u^(2D) exp(-a_delta u).              (Sea5)

No assertion that q is numerically small at a practical coupling is needed.
For fixed model parameters q tends to zero as u tends to infinity.

**Penalty lemma.** For every real `h>=0`, let

    Z(h)=int exp[-u sum_p s(U_p)-h sum_x G_x(U)]dU,
    dmu_h=Z(h)^(-1) exp[-u sum_p s(U_p)-h sum_x G_x]dU.

Then for every set A of distinct fine cells,

    mu_h(G_x=1 for every x in A)
                         <=[q_delta(u) exp(-h)]^|A|.      (Sea6)

*Reflection-positive hypothesis, checked for this measure.* Reflect in an
integer coordinate plane and its antipode. Split fine links into the two
closed halves, with tangential links on the two planes shared. No elementary
plaquette and no closed unit cell contains a link strictly in both halves.
Given the shared links, the remaining product Haar variables split and the
density is a positive boundary factor times `W_+(U_+,U_boundary)` times its
reflected copy. Each cell-penalty term is allocated once, to the half
containing that cell. Reversal of a reflected oriented link means inversion;
Haar is preserved and the plaquette defect is unchanged by conjugation and
inversion. Boundary tangential links are fixed. Hence, for a complex
half-measurable F, the reflection form is an integral of
`|int F W_+ dU_+|^2` against a positive boundary density. This proves site
reflection positivity, also for every h, without a gauge fixing.

The closed-cell event is reflection covariant. Apply the algebraic
chessboard estimate to the cell algebra, giving
`mu_h(G_A)<=mu_h(G_all)^(|A|/v)`. This is the same algebraic theorem as
FILS Theorem 4.3 / Biskup Theorem 5.8; its hypotheses and exact read coverage
are recorded in the [literature ledger](checks/source_sea_literature.md).
It permits shared boundary variables and all even side lengths, not only
powers of two. Bounded indicators follow directly from the reflection form
or by bounded approximation; no smooth cutoff hypothesis is used.

On `G_all=1`, at least v/4 distinct plaquettes are bad. Thus its numerator
is at most `exp[-u delta^2 v/(8N)-hv]`. For the denominator, restrict every
fine link to the radius `r_delta/sqrt(u)` identity cap. Then every plaquette
has norm defect at most `4r_delta/sqrt(u)<=delta/2`, so **every penalty
vanishes**. Its Wilson action is at most `48 r_delta^2 v`, and its Haar mass
is at least `[c_H r_delta^D u^(-D/2)]^(4v)`. This lower bound for Z(h) is
independent of h. Taking the v-th root proves (Sea6).

**Exact-history reference theorem.** Let

    Z_A=int exp[-u sum_p s(U_p)]1{A(U)=A}dU.

For every finite even torus, every u>=1 and every A,

    Z_A/Z_delta <= q_delta(u)^|A|,
    1<=Z_W/Z_delta<= [1+q_delta(u)]^v,
    0<=log(Z_W/Z_cut,tot)<=v log[1+q_delta(u)].             (Sea7)

*Proof.* Multiply (Sea6) by `exp(h|A|)Z(h)`. Its left side becomes

    int exp[-u sum_p s(U_p)] product_(x in A)G_x(U)
                              exp[-h sum_(x outside A)G_x(U)]dU.

As h tends to infinity this tends to Z_A, while Z(h) tends to Z_delta.
Bounded convergence applies on the finite compact product. Dividing by the
positive Z_delta gives the first inequality. Sum over all A for the second;
(Sea4) gives the third. This proves a reference ratio, not merely a
probability estimate relative to Z_W.

A useful exact hole consequence is

    int exp[-u sum s]1{A(U) subset H}dU / Z_delta
        =sum_(A subset H) Z_A/Z_delta <=[1+q_delta]^|H|.    (Sea8)

H is any prescribed set of fine cells, including disconnected or wrapping
sets. The reference on the left is the same global Z_delta. There is no
claim about an arbitrary frozen exterior or about a ratio between two
different outside-conditioned measures.

This step is stronger than the earlier exploratory union-bound criterion
`v q<1`. It uses a new, verified family of tilted measures; HW's Proposition
PF does not permit deriving (Sea7) from the h=0 estimate alone.

## 3. The actual soft field and enlarged histories

Set `A_L=3L(L-1)/2`, and choose fixed `0<eta<=1` and delta such that

    delta<=min{epsilon_1,epsilon_loc/2,eta^2/(8N A_L)},
    eta<=epsilon_loc/2.                                  (Sea9)

For a coarse link c, let Lambda_c be the union of its two actual endpoint
blocks, and let K_c be the set of closed fine cells having at least one
vertex in Lambda_c. This definition is geometric and reflection covariant;
`|K_c|<=2(L+1)^4`. It contains a cell witnessing every plaquette used by the
paired-contour ribbon bound. Define the contaminated coarse links

    D(A)={c:K_c intersects A}.

There are at most 128 such links per fine cell in A: a fine cell has at
most sixteen endpoint blocks, each incident to eight coarse links. Thus
`|D(A)|<=128|A|`, including small periodic tori. Contaminated coarse links
are integrated over their **entire** SU(N) domains, not declared small.

On `A(U)=A` and `c outside D(A)`, all ribbon plaquettes have norm defect
below delta. The actual S4′ ribbon estimate therefore gives
`max_(sigma,y)||T_y^sigma-S_c||op<=A_L delta`.
Keeping the actual normalizer in (Sea1), the centered-cap argument gives

    k_t(V;Mbar)<= e c_H^(-1)t^D
      exp[-t{||V-S_c||op^2/(2N)-2 A_L delta}],  t>=1.

Indeed the phase at V is at least `||V-S_c||op^2/(2N)-A_L delta`, while
its minimum is at most its value at S_c, at most `A_L delta`. A radius-1/t
Haar cap at a minimizing unitary supplies the displayed normalizer bound.
Consequently, for `u>=max{1,1/kappa_min}`,

    int_(||V_c-S_c||op>=eta) k_(kappa u)(V_c;Mbar)dV_c
           <= p_eta(u),
    p_eta(u)=e c_H^(-1)(kappa_max u)^D exp[-b_eta u],
    b_eta=kappa_min eta^2/(4N).                            (Sea10)

This is the general-threshold specialization of [RLARGE, Lemma RS R4](RLARGE.md),
with its real coupling and exact normalizer. It is used conditionally on U
only on the clean region just proved. Distinct V_c are independent given U
under the product kernel; the fine field and its histories are not independent.

For every U,V define

    C(U,V)={c outside D(A(U)): ||V_c-S_c(U)||op>=eta}.

Let Psi_(A,C) be the indicator of the exact pair `(A(U),C(U,V))=(A,C)`.
It is zero unless `C subset coarse_links minus D(A)`. This finite family
partitions unity. All fine rough plaquettes, including arbitrary inter-block
collars, are recorded in A. A coarse link in D(A) is kept unrestricted;
every other coarse mismatch is recorded in C. Gauge transformations and the
fixed blocking symmetries carry these definitions covariantly.

Define the actual zero-source joint history weight

    Z_(A,C)[Xi]=int w_0(U,V) Psi_(A,C)(U,V) Xi(U,V)dU dV,

where Xi is any measurable hard insertion with `|Xi|<=1`. Then

    |Z_(A,C)[Xi]|/Z_delta <= q_delta(u)^|A| p_eta(u)^|C|,
    |Z_(A,C)[Xi]|/Z_cut,tot <= q_delta(u)^|A| p_eta(u)^|C|. (Sea11)

*Proof.* Take the absolute value before integration. At each fine U in the
exact A event, integrate the product kernel over V. The C mismatches cost
at most `p_eta^|C|` by (Sea10); the constraints on other clean links cost at
most one; every contaminated-link integral is exactly one. Apply (Sea7)
to the remaining fine integral. No probabilities under different laws are
multiplied. The second bound uses (Sea4).

In particular Xi may be any original H13 failure-history indicator Xi_F,
or any further correlated history. Impossible histories stay zero. Summing
Xi_F over F recovers the unchanged `(A,C)` weight. The original failure
family is retained by refinement rather than replaced by independent events.

## 4. Original complex sources, supports and the old sea identity

Write `delta S_epsilon=u sum_p epsilon_p s(U_p)` exactly as in H1.
Only these Wilson coefficients vary; the kernels keep their prescribed real
coupling. Let E(A) be the fine links in the closed cells of A. Each cell has
32 links, each read by six plaquettes. For a coarse link c, let E_c be all
fine links with both endpoints in Lambda_c; `|E_c|<=8L^4`.
Let P(E) denote every Wilson plaquette reading a link of E, including
plaquettes that extend outside E's site set. Set

    J(A,C)=P(E(A)) union union_(c in C union D(A)) P(E_c),
    n_A=192+6144 L^4,      n_C=48 L^4,
    |J(A,C)|<=n_A|A|+n_C|C|.                              (Sea12)

All contour means and normalizers affected by these defect links, as well
as all touched Wilson source terms, are retained. These are upper bounds;
overlap does not create independent copies of a source. The actual support
includes these links, their plaquettes, and the full contour data of every
incident coarse link, with the original plaquette labels. More explicitly,
let B_* be the blocks meeting the vertices of cells in A or the endpoint
blocks of links in C union D(A). Then
`|B_*|<=272|A|+2|C|`. Every kernel reading the specified fine links is among
the at most `8|B_*|` coarse links incident to B_*; its two-block contour
data lie in the one-block collar of B_*. No factor reading this collar is
silently discarded from the actual global density. The source variables
in (Sea12) are the Wilson plaquettes reading the specified fine links;
source-independent kernels may read additional collar data. Dirty coarse
links are included in the source budget, even though they are integrated
unrestrictedly. The absence conditions defining an exact history are global,
so this support bookkeeping is not a proof that its weight is a local
activity.

Take the predecessor's fixed radius `rho_0=epsilon_1^2/(32N n_P)` and put

    rho_sea=min{rho_0,a_delta/(4n_A),b_eta/(4n_C)}>0,
    |epsilon_p|<=rho_sea+lambda/u for p in J(A,C),
    epsilon_p=0 outside J(A,C),   lambda>=0 fixed.          (Sea13)

This is an explicit, possibly smaller fixed polydisc. It is independent of
u, volume, history and source count. The old pointwise successful-gas theorem
still holds on it because `rho_sea<=rho_0`; no price on the whole larger
rho_0 disc is asserted for this enlarged architecture.

For any `|Xi|<=1`, define Z_(A,C)^epsilon[Xi] by inserting
`exp(-delta S_epsilon)` in (Sea11). It is entire in the original source
coordinates and obeys

    |Z_(A,C)^epsilon[Xi]|/Z_cut,tot
          <= q_src(u)^|A| p_src(u)^|C|,
    q_src=exp(2lambda n_A) C_delta u^(2D)
                              exp[-(a_delta-2rho_sea n_A)u],
    p_src=exp(2lambda n_C) e c_H^(-1) kappa_max^D u^D
                              exp[-(b_eta-2rho_sea n_C)u]. (Sea14)

Both remaining rates are at least half their zero-source rates. This follows
from `0<=s<=2`, (Sea12) and (Sea11). The source cost is one raw-action factor;
the two compensating source factors in the H6 representation cancel only
through its exact H8–H9 identity. They are not dropped from a pointwise
estimate. Cauchy bounds on any inner polydisc are available for these history
amplitudes. The theorem is not a connected-source logarithm and does not
bound a source spread over arbitrary remote plaquettes by |A|+|C|.

For clarity the exact connection to the **unchanged** common sea is

    Z_(A,C)^epsilon[Xi_F]/Z_cut,tot
      = int dbar_nu_cut(V) E_(nu_cut^0(. ;V))[
           exp(-delta S_epsilon(U))
           sum_(B subset old_blocks)
                    T_B^epsilon(Psi_(A,C) Xi_F)(U;V)].     (Sea15)

The replacement operator is H8 in its full JOINT form. Psi generally reads
replaced interiors and therefore must be placed inside that operator.
Evaluating it on the unmodified all-cut sea would be a different integral.
All Haar factors, local denominators, exterior source-only terms and kernel
normalizers are exactly those of H8–H9. (Sea14) estimates the actual outer
integral (Sea15), including its hard correlations.

At zero source, summing all refinements gives a direct estimate of the H14
expression itself, integrated over its actual coarse reference:

    int dbar_nu_cut(V) E_(nu_cut^0)[
         sum_F product_(Y in F) f_Y^0 G_ret,F^0]
       = Z_W/Z_cut,tot <= [1+q_delta(u)]^v.                (Sea16)

The volume-extensive exponent is explicit. It is not replaced by a constant
or by a claim that every pointwise f_Y is small. Individual old F weights
can be reconstructed by summing their `(A,C,F)` refinements; performing that
sum may incur a volume cost. No per-F product theorem is inferred for the
old unrefined activities.

## 5. What moves, and what remains to be produced

The new producer is (Sea7), (Sea11), (Sea14) and (Sea15): exact rough-cell
and clean-mismatch histories, including arbitrary original failures, now
have a one-level bound **relative to the same integrated all-cut reference**.
This is stronger than the already known unconditioned probability estimate.
The independent h-tilted RP input is what pays the reference normalization.

The initially considered condition `v q<1` would have missed the continuum
consumer. In the actual convention [RLARGE §0](RLARGE.md),
`u=beta_Wilson=2N/g_std^2`, and the proposed one-loop slope is
`beta_1=11N^2/(12pi^2)` per log L. Under that separately supplied scaling,
`u_0~beta_1 K log L`, `v~const L^(4K)`, so
`v q_delta` has exponential rate `4-a_delta beta_1`, with
`a_delta beta_1=11N delta^2/(96pi^2)`. At N=2 or3 and delta<=1 this is less
than4; the lane's much smaller actual thresholds make it smaller still.
Thus the union-bound window does not contain that cutoff limit. This is
conditional arithmetic using the stated flow convention, not a proof of
the running coupling. The final (Sea7) has **no such volume window**.
Its pressure correction per fine cell is small, but its total correction
need not vanish in a fixed physical volume. Counterterms and scale induction
still have to be constructed.

The exact history weights are correlated global integrals with good-field
constraints on their complements. A bound by a product of numbers does not
factor them over disconnected components and does not give a local cluster
logarithm. The all-good sea also retains flat holonomies and all gauge orbits.
There is no proved ultralocal fluctuation law here. The independent data-kernel
worker reports that LINEAR_PACKAGE's N2-exp results concern top-data-to-field
and residual maps; they are not the conditional fluctuation inverse needed
for this sea calculation.

A concrete reusable next route is Dimock's *Covariant Axial Gauge*,
`1410.2798v3`, §§3.7–3.10: a local parameterization C of the exact constraints
`QZ=tau Z=0`, followed by the constrained covariance
`C_k=(C^T Delta_k C)^(-1)`, its resolvent/square-root representation, and
the transformation to independent Gaussian variables in (152). The actual
producer needed here must instead derive the fluctuation quadratic form
from the normalized soft group kernel, specify its four-dimensional gauge
slice and background domain, and retain the cut/hole, Haar and source
remainders. Substituting a soft minimizer or discarding the kernel's
field-dependent normalizer does not establish that identification. The
versioned primary text and exact mismatch are in the literature ledger.

The next producer is a localization of these reference-relative correlated
weights, or of the conditional all-good sea, on the consumer's actual coarse
field domain: connected original-source coefficients with a summable support
norm and a nonzero normalized complex average. At fixed V the kernel factors
do not integrate to one, and the fine cell penalty no longer has the proved
reflection-positive density decomposition. No fixed-V theorem follows from
(Sea16). The earlier frustrated SU(2) slice remains a valid warning against
that substitution. Higher-level effective actions also need their own
penalty/localization argument; the bare Wilson proof cannot be iterated by
renaming u. Hard selectors have no asserted complex-coarse continuation.

The localized all-good conditional estimate is strictly stronger than the
scalar one-level pressure bound proved here and remains a substantive part
of the source-return problem. It is weaker than full Yang–Mills existence
and the physical continuum gap, both of which remain OPEN. No small activity,
reflection form, or defect-cluster tail is identified with a physical gap.

## 6. Literature, prior art and evidence

The [literature ledger](checks/source_sea_literature.md) records fresh primary
searches, exact theorem/page coverage, model mappings and access failures.
The classical chessboard theorem is reused, not claimed new. The existing
lane's [PROOF E8.1](PROOF.md) already gives the h=0 fine-cell estimate and
[RLARGE RS](RLARGE.md) already gives the soft-kernel tail. The structural
addition is the penalty family and its exact-history/common-reference limit,
then its application to the present hard-history source identity.

Narrow statement searches on current main and the actual PROOF, HW, RLARGE,
PLD and source-return notes found the existing h=0 estimates and HW's
normalization warning. No matching penalty-family/reference construction
was found in those searches. A current-main native Majorana flux note uses
another measure and an unconditioned chessboard estimate; it does not supply
the gauge-model bridge here. This is scoped repository novelty evidence,
not a claim of literature priority or an exhaustive search.

The [criteria](checks/source_sea_criteria.md), checker implementations,
paired outputs, access record and [manifest](checks/source_sea_manifest.json)
give the execution evidence and exact source identities. Author checks do
not replace the coordinator's fresh independent review. Any failed attempts
are preserved and distinguished from the final runs.

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Actual one-level joint sea and refined failure-history bounds relative to the integrated all-cut reference; localization, fixed-V complex source return, induction, existence and continuum mass gap remain open."
audit_required_before_effective_retained: true
bare_retained_allowed: false
full_existence_established: false
physical_continuum_mass_gap_established: false
```
