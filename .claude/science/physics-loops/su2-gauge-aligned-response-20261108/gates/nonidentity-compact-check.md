# Nonidentity compact extension: independent research check

This is a fresh-context, same-family research check, not an independent audit
or a landing review. The checker retains the inherited selected model and
reasoning effort. Worktree HEAD is
`97fc90828ab071b5813d1c9b6c8a952dc042509b`; procedure source is current-main
`bf92a1d763030836ed55631d5d7a7ef3b288f284`. No science status is assigned.

## Phase 1 — frozen before candidate access

The derivation below was written before reading any new nonidentity author
proof, the supervisor's proposed proof, or the new prior-art extraction.
Only the five old mathematical sources listed at the end were read. Their
complete contents were read, with clipped combined displays recovered by
bounded reads. The compact coercivity and actual finite reader templates
inside those sources are explicit ancestral premises; this check does not
reprove the complete historical geometric chain.

### Exact target and independently reconstructed route

Fix odd L>=3 and kappa>0. Uniformity is in m>=3, u>=1, the position and
orientation of the seven deleted terminal edges, all permitted internal
trees, and every surviving terminal field with
`sup_c |V_c-I| <= epsilon_*`. Constants may depend on L and kappa. All
fine non-tree and intermediate links remain hidden. Every surviving kernel
is complete; a deleted terminal kernel contributes neither numerator nor
normalizer. The reference measure is product probability Haar.

Write `t=kappa*u`, `Z(s)=int exp(s w(Q)) dQ`, and `B=(log Z)'`. The exact
complete energy factor is

    Phi_u(v,M) = kappa(1-<v,M>)
                 + [log Z(t|M|)-log Z(t)]/u,
    K(v|M) = H(t) exp[-u Phi_u(v,M)], H(t)=exp(t)/Z(t).

This formula includes M=0. Since `0<=B<=1`, `Phi_u` is uniformly globally
Lipschitz in all group readers, even though its higher global derivatives
need not be uniform near zero means. On a fixed all-reader identity chart,
`|M|>=1/2`. The tilted-Haar cumulant calculation in the old chart supplier
gives `|h^(j)(s)|<=C_j(1+s)^(-j)`, `h=log Z-s`; hence all fixed-order
positive reader derivatives of `Phi_u` are uniform for u>=1 there.

Let `F_{u,V}` be the sum of the complete Phi factors and fine Wilson factors.
The inherited identity-output theorem gives

    F_{u,I}(q) >= c0 sum_e [1-w(q_e)], c0>0.

The identity Hessian `H_u` is bounded below by c0, has bounded absolute row
sums and fixed reader range, uniformly in u and geometry. Its inverse has
a uniform cell-block sup-norm bound: the Neumann series of `I-H_u/M`, for
M above the common spectral upper bound, has geometric decay and kth-term
range at most k times the fixed range. Summing that decay against the
four-dimensional polynomial shell bound gives the required row bound.
No translation invariance is used.

At identity, the V perturbation creates a cellwise force O(epsilon). The
gradient remainder in a cell-block sup ball of radius s has Lipschitz
constant O(s+epsilon), by the uniform third-derivative row sums. Therefore

    x -> -H_u^(-1)[grad F_{u,V}(0) + nonlinear remainder(x)]

is a contraction on a ball s=C epsilon after reducing epsilon_*. This
constructs a near-identity stationary field `a*_{u,V}` with
`sup_e |log a*_e|<=C epsilon`, continuously in finite u and V. The u
subscript matters: stationarity concerns the complete Haar energy, so in
general its center depends on u. There is no reason for this field to decay
toward I in the bulk when V forces every terminal cell.

Here is the compact stability argument, reconstructed factor by factor.
For one surviving physical factor f, let `f_0(q)` be its identity-background
value and define

    D_f(q)=f(a* q;V)-f(a*;V)-f_0(q),
    l_fe = D_{x_e} D_f(exp(ix)) at x=0,
    b(q)=Im(q),   T_e(q)=1-w(q_e).

All backgrounds a* and V are O(epsilon). Global Lipschitz bounds give
`|D_f(q)|<=C epsilon` everywhere. On a fixed product cap, the second
x-derivatives of D_f are O(epsilon); Taylor expansion and
`x-Im(exp(ix))=O(|x|^3)` give

    |D_f(q)-sum_e l_fe dot b(q_e)|
                  <= C epsilon sum_(readers e) T_e(q).       (P1)

Outside that cap one reader has fixed positive T_e, so the global bound
and bounded arity prove the same inequality without any derivative at a
zero mean. For each hidden e, `sum_f l_fe=0` exactly by global stationarity
and the zero identity-baseline differential. Summing (P1) therefore yields

    |F_{u,V}(a*q)-F_{u,V}(a*)-F_{u,I}(q)|
                                <= C epsilon sum_e T_e(q).  (P2)

For epsilon_* small enough this proves all-compact relative coercivity,
and hence uniqueness of the global Haar mode. The identity factor upper
bound also gives `F_{u,I}(q)<=C sum T_e`; thus the same reasoning supplies
a uniform upper quadratic bound as well. The compact perturbation route
is feasible under the pinned premises; the size of the terminal field
need not shrink with volume or u.

### The regional issue: compensation is necessary

Global stationarity does imply that the selected regional sum has zero
INTERIOR differential when all relative exterior coordinates equal I:
every factor reading an interior coordinate is selected. It does not make
the individual factors stationary, nor kill the EXTERIOR linear terms of
that selected sum. Applying the old regional moment proof directly to
`sum_selected [f(a*q;V)-f(a*;V)]` can therefore be false.

A closed discriminator is available on two SU(2) coordinates x,y. Put
`T=1-w`, `v(y)=Im(y)_1`, and for delta>0 use nonnegative factors

    f1(x,y)=T(x)+(1/2)T(y)+delta v(y)+delta^2,
    f2(y)  =(1/2)T(y)-delta v(y)+delta^2.

Nonnegativity follows from
`1/2-sqrt(1/4+delta^2)>=-delta^2`. Their sum has the unique global minimum
at (I,I) and relative energy T(x)+T(y). Region {x} selects f1. At
`x=I, y=exp(-i h sigma_1)`, its center-subtracted regional value is
`(1/2)(1-cos h)-delta sin h`. This cannot be bounded below by
`-K(1-cos h)` for any finite K as h decreases to zero. Thus global
stationarity plus global coercivity alone does not justify the uncorrected
regional lower bound. This is a counterexample to that transfer inference,
not a counterexample to the actual lattice target.

The correction follows directly from (P1). Define the compensated factor

    g_f(q)=f(a*q;V)-f(a*;V)-sum_e l_fe dot Im(q_e).

Then `|g_f(q)-f_0(q)|<=C epsilon sum_readers T_e`, and consequently
`|g_f(q)|<=K sum_readers T_e`. The global sum is exactly
`F_{u,V}(a*q)-F_{u,V}(a*)`, because the linear proxies cancel. In a
whole-factor regional selection R the interior proxies also cancel. Its
remaining proxy sum depends only on the frozen exterior. Therefore
`G_R=sum_selected g_f` gives EXACTLY THE SAME normalized conditional law
as the actual complete regional factors. This is a boundary-dependent
normalization cancellation, not deletion of an interaction or normalizer.

Extending the relative field by I outside R and its reader collar B gives

    c T_R-K T_B <= G_R(q_R,z) <= K(T_R+T_B),             (P3)

since the omitted compensated factors read no interior coordinate and have
absolute total at most K T_B. This is valid for every compact exterior,
including means equal to zero. It is the missing bridge from a globally
stationary center to the arbitrary-exterior moment mechanism.

### Exact moment mechanism on compact and centered chart domains

Keep a* fixed through every conditional and radial tilt. For any cell
profile `0<=theta_x<=c/2`, the tilted regional energy
`G_R-sum_(x in R)theta_x T_x` is at least `(c/2)T_R-K T_B` and at most
`K(T_R+T_B)`. On a product cap of chord radius d/sqrt(u), its denominator
is at least

    exp[-K u T_B-C n] (c_cap d^3)^n u^(-3n/2),

where n is the actual number of integrated hidden links. For lambda=c/4,
the exponential-moment numerator is at most

    exp[K u T_B] C_H^n u^(-3n/2).

The same n powers cancel exactly, giving

    log E_theta[exp(lambda u T_R)|z] <= A |R|+B u T_B.  (P4)

All normalizers are already in the complete factors. Their constant H(t)
powers, the center subtraction, and the exterior compensator are identical
in the actual conditional numerator and denominator and cancel there.
There is no all-terminal comparison or approximate normalizer.

The same-law tower then gives
`E_theta T_x <= C/u+C(2s+1)^4 q^s` for a cell s reader-shell steps inside
a region, with 0<q<1. On the full torus, take arbitrarily large s after
balls saturate, obtaining `E_theta T_x<=C/u`. Integrating this estimate
through the whole allowed profile box proves

    log E exp(t u T_A)<=C t |A|, 0<=t<=c/2,
    E |q_e-I|^p <= C_p u^(-p/2), p>0.                   (P5)

This proves radial moments, not signed centering or compact covariance.

For a centered product logarithm cube `q_e=exp(ix_e)`, Haar is
`const product_e j(x_e) dx_e`, `j=(sin|x|/|x|)^2`. The same conditional
proof works with each integral restricted to this cube if the cube contains
the chosen d/sqrt(u) cap. In particular it works for the supplied shrinking
radius `rho(u)=u^(-1/2) log(2+u)^A` once u is large enough that the cube is
within the fixed smooth chart. It does not require dividing a compact
moment by the probability of the full chart. For a statement at every
u>=1, one may use `min(rho0,rho(u))` and select a uniform smaller cap; the
precise radius and cap condition must be stated.

The Hessian of the translated complete energy in this small cube remains
uniformly positive by the same finite-template derivative bound, now with
perturbation O(epsilon+rho0). The Haar log term has Hessian 2/3 at zero and
positive Hessian in a sufficiently small cube. Thus a centered-chart
covariance estimate can use the inherited mixed-boundary cube argument,
with the actual density and actual gradient supports. This provides no
compact covariance estimate. A moving chart must be held fixed when
taking terminal derivatives, or its domain and center derivatives must be
included separately.

For a regional near-center collar, a separate regional mode can also be
constructed. Its difference from the restriction of the full a* has a
boundary-decaying bound by the same weighted inverse argument. A claim of
boundary decay to I for arbitrary nonidentity V would instead be false in
general because terminal forcing is present throughout the region.

### Symmetry and normalizer discriminators

Nonidentity V generally removes the global simultaneous-conjugation
symmetry at fixed V. A Haar mode does not imply exact zero mean in either
compact relative coordinates or a centered cube. To see the failed inference
without any asymptotics, set on one SU(2)

    F(q)=T(q)[1+eta Im(q)_1], 0<eta<1.

It is smooth, stationary at I, and between `(1-eta)T` and `(1+eta)T`.
Nevertheless the normalized density exp(-uF) has strictly negative mean
of v=Im(q)_1: inversion pairs its numerator into
`-int v exp(-uT) sinh(u eta T v) dH <0`. The same sign argument holds on
any inversion-symmetric centered cube. Thus (P5) must not be changed into
an exact mean-zero assertion. This discriminator does not assert that this
one-factor model is the two-layer lattice law.

For a surviving kernel at output I and mean `M=r I`, the exact ratio is

    K(I|rI)/K(I|I)=H(tr)/H(t),
    Phi_u(I,rI)=[log H(t)-log H(tr)]/u.

It is strictly less than one for 0<=r<1, since `B(s)<1` for finite s.
The leading mismatch `kappa(r-<I,rI>)` alone is zero throughout this radial
family. Any computation that substitutes that mismatch for the complete
energy misses this surviving-normalizer cost. At r=0 the exact kernel is
1, not an undefined expression. This tests the kernel algebra independently
of any proposed whole-lattice computation.

### Phase-1 conclusion and frozen scope

Conditional feasibility is established by the mechanism above: global
stationary centering, compact tangent-proxy cancellation, compensated
regional factors, and same-law profile moments. The raw regional transfer
and exact-zero-mean inferences have explicit counterexamples. The forthcoming
candidate must implement these obligations or an equally valid replacement;
its result is not presumed. No new candidate has yet been read.

The five old source SHA-256 values are:

| Source in `parts/` | SHA-256 |
|---|---|
| marginal-normalized-regional-coercivity.md | bd3fa8b5eb989c7718ad5d760a913e33166f3e9edcf52b9f17f82cbd809ca255 |
| marginal-regional-relative-coercivity.md | 2d142414fb4992c2a1e907d42d15ca9f7164ee6e90c892d8c3d529b39e297385 |
| marginal-nonlinear-chart-estimates.md | b1e26baa37cf1dc47331d9a98a834afda5e7634d62f31df50600fd321fc45cb7 |
| marginal-regional-moments-and-ratios.md | b2d3d9bedfb52b11056788e1f72cd14c4f9846c733c86ee424c2240f13db647f |
| marginal-source-marked-compact-decomposition.md | 4a30c12ef9c58eaf3d6ca1c82bab94137f088ee59cba73304fe30da9e04dcdd3 |

The identity compact bound, full syntactic readers, quotient Haar law and
finite template family remain pinned ancestral premises. The old source
records identify the upstream seven-edge coercivity and actual path-variance
calculation; these upstream documents were outside this bounded read scope.
The parent's completed literature extraction is preserved and will be read
only after this independent phase is frozen. No new external theorem is
imported by the derivation above. No Git mutation, prompt edit, audit/status
change, numeric job, or sub-agent launch was performed.

## Phase 2 — final candidate check

**Research signal: advance, conditional on the pinned model and ancestral
identity coercivity/reader premises.** No material mathematical defect was
found in the six final surfaces below. No correction to those surfaces was
required by this check. This is confirmation of the displayed conditional
implications, not an audit verdict, retained status, or recertification of
every ancestor. The source count was explicitly extended by the supervisor
to include the new Gaussian producer and its exact forest consumer.

### Final source identities and actual read coverage

Paths without a leading `docs/` are relative to this pack.

| Final surface | Actual coverage | SHA-256 |
|---|---|---|
| parts/nonidentity-marginal-compact-mode.md | Full, 352 lines | 3ef73e9715111804f7ddc135e7bed62bbaaf36278f459e8d71d8fc15e127f83d |
| parts/nonidentity-centered-regional-estimates.md | Full, 352 lines | b125f4b80bb0143c4269024d426476deb118bc7b30030c15d31e5fbb0a98b9bc |
| parts/nonidentity-frozen-gaussian-producers.md | Full, 369 lines | 7c2330f535d4ca82e7527f305523eac8ebbde9634981403fa44c5e78401ddd12 |
| parts/nonidentity-compact-connected-response.md | Full initial 401-line argument, then complete final notation/provenance delta | 00ef56147969096ed19888450553286269b0ed8f0ae9ca02ede4856231e47d42 |
| docs/SU2_NONIDENTITY_COMPACT_CONTROL_BOUNDED_THEOREM_NOTE_2026-11-09.md | Full, 188 lines | a445c663df41e8ea521051be56467b700182f79489bd353bb0faf932355124d6 |
| PROOF_TREE.md | Complete changed section and necessary adjoining context, lines 174–237; unchanged earlier map not re-reviewed | 20007177ff4484b7a2ccc68cdcce7bc10d20c0e5401d07b06a58345fac4be9d5 |

The initial consumer hash was
`2ba1932169bbe46e460b3071d21345c3d8108a6c5a9432069d63dfdec7d71431`.
Reversing exactly the inspected H_Z notation and author-read-coverage edits
reproduced that SHA-256. The complete verified delta is preserved in
`logs/su2-nonidentity-compact-20261109/checker-consumer-final-delta.diff`.
Thus the unchanged argument was not presumed identical from a prose report.

Additional inherited sources, all read in full after freezing phase 1:

| Source in parts/ | SHA-256 |
|---|---|
| marginal-frozen-gaussian-producers.md, 347 lines | 598af873a6b9da46a94dafe94de05ebef6cc165b2420b32f46cd2983f31dcff6 |
| marginal-connected-density-expansion.md, 362 lines | 79d6f2d98f058180d98f576b1840681a42e504186e1be4975bbbaf47a5121d98 |
| zero-shift-marked-density-forest.md, 403 lines | d44adc900daf7ac665e502ac950230a8739b120d1a2be4940fd292ea9a09087f |

The preserved Luna extraction was read only after phase 1. Its SHA-256 is
`f17b0579f4a7bf4d3a8d51f52e2519cf181f93c936f06daa03b1e4be6f3b1aae`;
its search log is
`3fa7c5d8846bf37cba770b5d2b81de1b4979278e198b06760b59096b633f2275`.
Neither was edited. No Fable approach advice, supervisor proof sketch, or
other checker conclusion was read before the independent phase. Fable
advice was not read at any time in this check. The later candidate contents
and supervisor's source/scope messages were necessarily shared inputs.

### Compact center and regional moments

The mode proof implements (P1)–(P2) for the actual complete kernel, including
zero means, arbitrary allowed trees and periodic coincidences. Its inverse
is controlled in weighted cell-block norms using the actual gapped,
finite-range Hessian. Perturbing all terminal outputs produces a uniform
sup-norm force; a localized perturbation produces a localized force. The
weighted inverse therefore proves its terminal localization and its
regional difference from the global center. The latter is a difference
from a*, not a claim of bulk decay to I. Its compact comparison uses the
same right-tangent proxy in every selected factor and cancels only sums
which actually vanish. The result is a unique global minimum/Haar mode;
it expressly makes no claim of a unique stationary point on the compact
space.

The regional candidate closes exactly the problem exposed by the phase-1
two-coordinate discriminator. Equations (3)–(5) compensate each factor;
the remaining selected linear sum is exterior-only and is retained inside
the common scalar C_A(z). Equation (6) then follows by extending q by I and
bounding omitted compensated factors in absolute value. Nonnegativity of
individual compensated factors is not assumed. Equations (7)–(10) use
identical actual C_A(z), hidden-link counts and Haar powers in numerator
and denominator. A single fixed center and profile law are used throughout
the nested conditionals. The chart contains the reference cap and remains
a product under further conditioning. This establishes its compact
all-u moments and its sufficiently-large-u centered-chart moments without
an extensive density comparison or division by a full-volume chart
probability.

The two different ratios in its §4 are kept distinct: the complement of an
entire-core-rough event is not the entire chart. The shell payment spends
both collar costs before extracting a core charge and retains a quadratic
bulk weight for integration. Whole source factors occur in the actual
marked numerator and marked chart denominator. The phase wedge and native
reader support are sufficient for the later conditional-integration
identity. The score jet is taken with center, chart and selectors frozen,
as required; it is not a derivative of a moving-domain family.

### Gaussian and connected consumer

The new Gaussian producer has no concealed per-factor linear remainder:
each compensated local action and each Haar term has value and differential
zero at the translated origin. Its precision is the actual translated
complete-energy Hessian plus `(2/(3u))Id`, and its common physical prefactor
retains `exp[-u E_u(a*;V)]`, the exact surviving kernel count, Q_J, Z_fine,
probability-Haar constants, rescaling power and Gaussian determinant.
Removing the surviving radial normalizer would fail the phase-1 radial
kernel discriminator and change this precision/prefactor.

I independently checked the finite-matrix estimates: C has exponential
entries by its Neumann series; truncation gives a positive core because
`||E||<=1/(2M)` and `C>=1/M`; unordered-pair paths are symmetric; the
pinned-path count uses both endpoints in the ball of the pin. Marginalizing
unactivated Gaussian coordinates uses the principal covariance C[I],
not an inverse of the principal precision. Taylor remainders are uniformly
O(u^(-1/2)p^3) after the exact quadratic subtraction. Whole-cell body
indicators pay for unused scalar coordinates as well.

The abstract forest's identity-terminal introduction is application
context. Its contract and proof require a fixed covariance, real fixed
integration domains, complete native readers, bounded analytic source
vertices and the stated positive budgets. Those properties hold at each
fixed V here. I inspected the proof, including the normalized-density heat
identity, determinant differentiation, scalar Cauchy factorial
`product_i sqrt(nu_i!)`, incoming-leg tree count, base/full-reader regrouping,
and coefficientwise removal of no-compact terms. None uses identity-output
conjugation symmetry. Covariance dependence on frozen V creates no varied
source reader; the candidate correctly makes no locality claim for a
moving covariance.

The consumer's compact primitive count retains the unique d_conn-component
partition of the core union. A connected n-cell core union is overcounted
by the displayed depth-first walk count, shell choices cost at most K^n,
and all native-reader collars and Gaussian full-cell factors are paid.
The positive logarithmic costs are O(log(u)^4), while the compact charge
is a positive multiple of p^2. This verifies the small compact budget
without reusing a Gaussian tail on compact cap fields. The marked
source-complete insertion identity gives the exact physical Z_* and Z_a,
so the connected correction is their ratio rather than a difference of
unrelated normalized laws.

For the source estimate I rederived the chart weights using the phase-1
moments, without exact zero means. Singlet invariance gives DF(I)=0; at a*
the local derivative is O(epsilon). Thus
`w=epsilon*u^(-1/2)+u^(-1)` bounds centered F,G moments, with gradient
weight sqrt(u)w. The centered scores have weight sqrt(u), with gradients
O(u). Every nontrivial fourth-cumulant cut is a crossing covariance after
its appropriate pairings are subtracted. The cube estimate then costs
`u w^2 <= 2(epsilon^2+u^(-1))`. A longest MST edge supplies the asserted
tree decay, and splitting its remaining exponential among the F–G and
two F–score distances gives the volume-uniform boundary-pair sum. The
compact correction is absorbed because `u^3 exp(-c p^2)` is bounded.

The original-source identity keeps
`kappa3(C_FG,A_c,A_d)` in addition to the quotient fourth cumulant.
Its three-label cut gives the stated allowance `u w=1+epsilon sqrt(u)`;
no odd-cumulant or mean-zero cancellation is assumed. Independent orbit
readers make C_FG identically zero. Overlap puts its reader union in a
bounded extension of both source regions, justifying the four-region
tree notation. These are upper bounds, not sharp asymptotics or claims
that the allowances are nonzero.

Finally, restoring all seven kernels preserves the identity reference
gap by adding nonnegative leading factors. The complete local templates
already cover their incidence. Every construction can therefore be applied
to the restored law with its own center, precision and kernel count.
Direct differentiation of log N minus log Q_J proves the displayed
distinct-label subtraction, with zero Q_J derivatives on deleted outputs.
Both laws must be bounded separately. The primary correctly requires all
terminal values, including J, to be small for this corollary.

### Scope and recovery

The primary and changed map distinguish all-u compact control from the
sufficiently-large-u connected conclusion. They retain the source class,
orbit allowance, fixed-background meaning, and inherited-premise boundary.
They do not promote the auxiliary Haar mode or posterior Hessian to a
physical Yang–Mills gap, or assert closure under a third transition.

This check establishes the new implication at the six hashes above.
The exact forest quotient, actual reader locality/incidence and the
ancestral seven-edge identity compact inequality are still supplied
premises. Their full geometric/history closure was not re-proved here.
The old cube and density-forest arguments were read and their relevant
analytic mechanisms checked; their publication/audit history was not
recertified. The primary's administrative review-history and later advice
records are not mathematical evidence and were outside this check.

Only this gate and its own bounded logs were written by this checker.
Candidate copies, the primary and map were supplied by the supervisor and
were not edited by the checker. No editable prompt file, Git ref/index,
audit/status record or platform instruction was modified. No numerical
job, external theorem import or sub-agent was used. The remaining research
obligation is the actual third-transition conditional class, including rough
terminal components and inherited-action closure; it is not discharged by
this fixed small-background result.

## Post-verdict approach-advice disposition

After completing the independent six-surface verdict above, I read all 207
lines of `sources/fable-nonidentity-compact-approach-20261109.md`, SHA-256
`719306e98b51c038d95130f7fe3b8e9bd0260943156da2f8238df408bda9fe0b`.
The pre-advice gate hash was
`59735fab609678c683cd07d6aeb91d86e41ecad7d19296df498daabfb6cb4f51`.
This later reading does not alter the recorded pre-candidate or pre-advice
independence. The advice did not read the new proofs or the abstract forest
proof, so its affirmative language is not evidence for those documents.

**Disposition: no material defect in the checked six surfaces is exposed.**
Its cautions about the actual u-dependent Haar mode, common tangent frame,
one frozen global center, exterior compensation, retained normalizers,
shifted minimum, nonzero score at the center, and all-small restored J
outputs are already implemented in the inspected files. Its warning that
the old identity response powers do not follow from the cut method at fixed
nonzero epsilon agrees with the current theorem: that theorem states
`C(epsilon^2+u^(-1))` and retains the separate original-orbit allowance
`C(1+epsilon sqrt(u))`. Neither allowance is asserted sharp or nonzero.

The advice's opening claim that the true orders remain u^(-1) and 1 is
stronger than its supplied argument. Its later table itself limits the
suggested u^(-1) fourth-cumulant conclusion to C3 sources, and gives
`u^(-1)+epsilon/sqrt(u)` for C2. The checked source class is C2. One cannot
replace that distinction by an implicit regularity upgrade. As a simple
scaling discriminator for a generic C2 strengthening, let x=u^(-1/2)Z
with Z standard Gaussian and h(x)=sign(x)|x|^(2+alpha), 0<alpha<1. Then

    kappa4(x,h(x),u x,u x)
      =(1+alpha) E|Z|^(3+alpha) u^(-(1+alpha)/2).

Here h is C2 but not C3 at zero. Fixed smooth cutoffs make the observables
bounded without changing the displayed leading order. This is not a
counterexample to the lattice theorem; it shows why its generic proposed
linear-leg lemma cannot receive a C2 u^(-1) interpretation for free.

The compact Haar integration-by-parts identity is a reasonable proposed
route. A pointwise quadratic remainder bound does not itself establish
the stated higher connected-cumulant induction with spatial tree decay.
The necessary regularity, remainder cumulants, uniform constants and any
use of noncommuting group derivatives need a separate proof. The proposed
tree-level expressions are likewise not remainder-controlled asymptotics
here. None is imported into the current result.

The suggested block-gauge extension also requires an explicit covariance
and domain/source-hypothesis match before becoming a theorem clause. In
particular a block-gauge transform of a global-conjugation singlet need not
remain in that same singlet class, and a Cartesian cube needs its own
transport. Strict terminal-parameter locality of activities and probability
of the small-background class are further tasks. No such extension is
needed for the fixed-background statements already checked.

All six final source SHA-256 values in the phase-2 table were refreshed and
remain unchanged. The research signal and its ancestral-premise limits
therefore remain unchanged. Only this advice disposition and its bookkeeping
receipt were added; no candidate proof, primary or map was edited.

## Final map-summary alignment

After the advice receipt, the supervisor revised only the opening summary
and Mermaid diagram of `PROOF_TREE.md`. The new map SHA-256 is
`76f1bae7fbdc4008e2d7c077e8461b2b6691cf0610712e44301e1106eca2acec`,
superseding the earlier checked map identity
`20007177ff4484b7a2ccc68cdcce7bc10d20c0e5401d07b06a58345fac4be9d5`.
I read the entire revised map, including its complete opening and diagram.
Reversing exactly the three inspected summary/diagram replacements recovered
the earlier map SHA-256. The verified delta is preserved in
`logs/su2-nonidentity-compact-20261109/checker-map-final-delta.diff`.

The new solid arrows are supported by the checked arguments: K and U
supply the identity compact gap and local complete-energy bounds for Vm;
Vm supplies the center/coercivity premise for Vr; Vm and Vr supply the
centered precision and compensated action for Vg. Vr, Vg and the fixed
abstract density forest in G supply Vc. Q supplies the exact normalization
identity for Dv, and Vc includes the separately centered restored-kernel
companion needed to control both laws. These arrows summarize those
conditional arguments; they do not promote their ancestral premises.

The opening correctly limits the new background class to a fixed small
neighborhood and the conditional subtraction to all-small terminal values.
Rough terminals and required new conditional classes remain explicitly
OPEN. Arrows into the third transition, iteration, limits and physical
spectral conclusions remain dotted and unproved. No iteration theorem or
physical-gap inference has been introduced. No material defect was found
in this map correction.

The current six-surface identity set is the four proof hashes and primary
hash in the phase-2 table, all refreshed unchanged, plus the new map hash
above. The previous six-surface and advice receipts describe their earlier
snapshots and are preserved. The checker edited only this gate and its
bookkeeping logs; the map revision was supplied by the supervisor.
