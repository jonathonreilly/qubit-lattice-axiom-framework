# Independent review of the charged stationary jets

**Source-only disposition: confirmed within the stated mathematical model,
with the full-colour quartic bound conditional on CJ18.** The reviewed source is
[CHARGED_STATIONARY_JET_ASTRA.md](CHARGED_STATIONARY_JET_ASTRA.md), SHA256
`85b91738993f09f7e40a49f4c957c164a684bf499185629a82775229f6437254`.
No material mathematical defect was found in its asserted conclusions. No
source repair was requested or performed in this review.

This confirms the actual cubic and completed stationary quartic identities,
the weighted potential lift and cubic bound, the forced second-current
recursion and its bound, and the implication from CJ18 to the quartic bound.
**CJ18 itself remains OPEN.** The source concerns the normalized,
u-stripped **tree phase**. Full four-dimensional Yang–Mills existence and
the physical continuum mass gap both remain **OPEN**. This is not whole-PR
approval, an audit verdict, retained status, a nonlinear RG construction,
or a finite-u density theorem.

## Independence, identities and scope

The [prospective criteria](checks/review_charged_jet_criteria.md) were written
before implementing independent controls and before inspecting an author
checker. The full author note, receipt, manifest and coordinator's summary
were already exposed. This is a fresh-context, source-exposed review, not a
blind experiment. The requested configuration was `gpt-6-astra/max`;
independently observable backend metadata was unavailable. No cross-family
independence is claimed.

I read the complete changed argument and its consumed proof contracts. The
[read manifest](checks/review_charged_jet_read_manifest.json) distinguishes
complete reads, selected proof ranges, historical context and discovered but
unread files. A file hash is not a claim to have read every line. Installed
physics-loop and review-loop instructions were reconciled to the
coordinator-fetched current-main methodology revision
`ca2bc7ddf64790da96cd43d42017d000fbfe4808`; the local `origin/main` object was
verified. Stale local main was not used as authority. The coordinator owns
locks, shared registers, source edits, git, PRs and combined validation.

The author [receipt](checks/charged_stationary_jet_receipt.json), SHA256
`83ba5129c3b6ca9c6e0d6a4577938531658ddf8fa2a8f21d728831d3edb66b6a`, still
matches all fourteen bound artifacts. Its historical
[source manifest](checks/charged_stationary_jet_source_manifest.json), SHA256
`c8ad3708cb24b231e64538c79da61420ebc35a8c6042bc86f7f2a5955296467d`, is
preserved. The shared assumptions and literature registers subsequently
changed; their current relevant entries were read and separately bound.
The mathematical predecessor bytes used here still match that manifest.

The model hypotheses are supplied SU(N), N>=2, the Wilson action, the exact
normalized soft S4-prime kernel, fixed positive kappa bounds, counting
pairings, periodic geometry and the stated local gauge domain. They are not
derived from the repository's primitive ontology. No measured value, fitted
selector, new physical axiom or new framework primitive enters this review.
The registered primitives retain only their actual grants; none supplies the
missing Yang–Mills construction or physical identification.

## Reconstruction of the local and stationary identities

The actual path family pairs the same coordinate ordering at both ends,
uses every centered offset, and averages over `24 L^4` labelled contours.
Reversing a link changes its sign and reverses its product position. For
each contour the degree-two logarithm is
`B = (1/2) sum_(i<j)[a_i,a_j]`; it cannot be replaced by an abelian endpoint
sum on noncommuting data. The Wilson terms in CJ4 follow by expanding the
trace of the exponential of the plaquette logarithm through degree four.

For the soft kernel write `M=I+epsilon A+epsilon^2 M2+epsilon^3 M3+...`.
The degree-two term of `M* M-I` is `R2=M2+M2*-A^2`; its degree-one term
vanishes. The degree-four trace coefficient of its square root is

```
Re tr(M4 - A M3 + M2* M2/2 - R2^2/8).
```

Subtracting the coefficient of `Re tr(exp(-epsilon b)M)` gives exactly CJ5,
including the normalized trace, signs and polar `R2^2` term. The special
unitary constraint does not alter this coefficient: the polar determinant
phase begins at degree three, and the change in its maximizing trace begins
at degree six. This is an analytic order argument near the identity, not a
claim based only on SU(2), where the quaternion mean hides that phase.
Putting `b=A` gives `||B||^2/2`; hence the remainder in CJ6 vanishes at
zero residual and has the claimed residual factor. The formula is for all
colour directions.

Differentiation of `F3=<Da,Z(a)>` gives the bottom
`d*Bp + DBp* f`, each lower soft contribution
`kappa(Q_root* B - DB* r)`, and each upper contribution `-kappa B`.
These are CJ7, including the derivative of the nonlinear blocking map.
The hidden Hessian is `D_h* D_h`. Its nullspace consists of nested gauge
gradients with scalar restriction constant at the final roots; that
constant may be subtracted. Harmonic links are retained and have a soft
cost at fixed top data. A full-space inverse is therefore invalid, while a
fixed transverse slice or Moore–Penrose inverse on the orthogonal
complement gives the required inverse. Gauge invariance and quadratic
stationarity imply that the cubic source annihilates this nullspace.

Solving `H w2=-S` and expanding the stationary value gives
`T4=F4-(1/2)<S,H^-1 S>`. Neither the half nor the minus sign is optional.
The fourth-derivative polarization has the corresponding factor three in
the symmetric exchange tensor. An affine slice containing the selected
first-order lift can be used; finite-dimensional local gauge fixing
supplies a legitimate chart. No uniform nonlinear chart radius follows
from this finite-jet argument.

## Analytic lift and absolute weighted bounds

The consumed inputs are the repaired periodic TU-3 construction and T-UNIF
contracts in [TUNIF](TUNIF.md), [CODEX_REVIEW_TUNIF2](CODEX_REVIEW_TUNIF2.md)
and [REVIEW55_TUNIF](REVIEW55_TUNIF.md), the consecutive-level NQ-1 estimate
in [NQ_DEF](NQ_DEF.md), the coefficientwise norm accounting in
[NORMS](NORMS.md) and [FLOW55](FLOW55.md), and the actual linear kernel
bounds in [LINEAR_PACKAGE](LINEAR_PACKAGE.md) and
[UNIFORM_SOFT_MINIMIZER_ASTRA](UNIFORM_SOFT_MINIMIZER_ASTRA.md).
The latter's corrected tree-phase scope and its
[scope confirmation](checks/review_uniform_soft_scope_confirmation.md)
control its reuse. The unprimed positive uniform strip proved there is
enough; no questionable historical numerical primed strip is needed.

For a jointly holomorphic one-form family satisfying `nu wedge h=0` near
zero in dimension at least two, fix distinct components alpha and beta and
vary only `p_beta`. Then `nu_beta h_alpha=0` on that axis, so continuity
gives `h_alpha(0)=0`. Repeat for each component. This works with additional
holomorphic parameters. An arbitrary closed one-form at the single zero
fibre would not satisfy this argument; the family hypothesis is essential.

Here the actual `h=v-b_raw,n` has that hypothesis. TU-3 constructs a
periodic analytic bottom primitive, and forward propagation by the actual
rooted Q and residual kernels preserves analyticity on a fixed strip.
Its curvature equals the stationary chain curvature. At nonzero real
Bloch momentum the closed difference from that chain is exact; rooted Q
commutes with the corresponding scalar restriction. Thus the top defect
is closed. The finite-cell identities extend from the dense union of torus
momenta analytically. The axis argument removes its zero-momentum harmonic
component. There is no volume-spanning mean-restoration tail.

The local restoration is quantitatively adequate. For `s=L^(n-j)`, the
gradient of the multilinear interpolant of the top scalar potential is,
on a closed top one-form, a convex transverse average of neighboring top
links divided by s. Its absolute row sum is `1/s`; its column sum is
`s^3`, and its support has bounded diameter in top units. Odd centered
grids nest because `(ab-1)/2=(a-1)/2+a(b-1)/2`. It therefore restores the
top data without changing any prescribed curvature or residual.

NQ-1 bounds the raw forward terms. For a separation m, a residual term
has factor `L^m L^-3(s0+m)=L^-3s0 L^-2m`, where `s0=n-j`; it is a
geometric sum. The composed supports stay in a fixed top-scale
neighborhood, so locality constants are not multiplied once per level.
The TU-3 bottom primitive and the local restoration give the same
admissible lift with potential amplitude `L^-(n-j)` and an exponential
kernel. Summing that kernel over external top links gives CJ11's row
bound. Summing over level-j output links introduces the separate
four-dimensional density `L^4(n-j)`, giving column size `L^3(n-j)`.
This establishes both absolute norms for one representative; it is not
an L2 estimate or a cancellation-based replacement for an absolute norm.

For CJ12, polarize first and anchor each local coefficient before taking
absolute sums. The single bottom cubic has density `L^4n` and amplitudes
`L^-2n L^-n L^-n`, hence one O(1) term. A soft cubic at distance
`s=n-j-1` has density `L^4s` and amplitudes `L^-3s L^-s L^-s`, hence
`L^-s`. The series converges. The weighted diameter is bounded by the
sum of anchor-to-leg distances. Finite colour contractions and fixed
one-step path lengths add constants, not scale factors. The historical
sign-vector norm is not identified with the coefficientwise absolute
tensor norm.

## Log current, endpoint funnels and the remaining quartic obligation

The current `q_j=kappa_j(r2_j-B_j)` in CJ13 is a **log-coordinate** current.
Its right-current coefficient is
`J2_j=q_j-[a_(j+1),kappa_j r1_j]/2`. Covariance gives

```
d*J2_j = sum_out [a_(j+1),kappa_j r1_j],
d*q_j  = (sum_in + sum_out)[a_(j+1),kappa_j r1_j]/2.
```

Incoming and outgoing incidences remain separately labelled even for a
wrapped self-loop. Ordinary co-closedness is false. Substitution into the
intermediate Euler equation gives exactly

```
q_(j-1) = Q_root,j* q_j + kappa_j DB_j[a1_j]* r1_j
        = Q_str,j* q_j + E_j,
E_j = kappa_j DB_j[a1_j]* r1_j - alpha_j* d*q_j.
```

All degree-two polar/BCH terms are present because this was derived from
the complete cubic. No ratio of kappas belongs in front of `Q* q`: the
definition of q already contains its kappa.

The first-order potential and residual amplitudes make both summands of
E weighted bilinear kernels of size `L^-4s`, with `s=n-j-1` and fixed L
factors absorbed. The top boundary `q_(n-1)` is the derivative of the
bounded cubic. Its anchored tensor bound gives the product exponential
envelope after a fixed loss of rate. Straight counting-adjoint transport
has row amplitude `L^-3m`. Thus the forcing term has factor

```
L^-3(i-j-1) L^-4(n-i-1) = L^3 L^-3s L^-(n-i-1).
```

The last factor sums geometrically. This establishes CJ17's row size
`L^-3s` and anchored-column size `L^s`, the latter containing output
density `L^4s`. The column bound cannot be replaced by the row amplitude.

The bottom Euler, Bianchi and harmonic equations in CJ19 also follow with
the stated signs. In particular, `harmonic(d w2)=0` does not license
discarding the harmonic part of `Bp` from the total second curvature.

CJ18 is sufficient for the advertised conditional quartic conclusion.
Its closed bilinear bottom curvature kernel has amplitude `L^-2n` and
the corresponding weighted row and anchored-column control. Uniform
exponential control provides a fixed holomorphic strip. Use total external
momentum as the twisted variable and the other momentum as a parameter;
shrink the two original strips by fixed amounts to keep this change of
variables inside their domain. The actual stationary finite-cell equations
give consistent torus symbols. TU-3, applied parameterwise and then
symmetrized, gives a primitive of amplitude `L^-n`.

The known residual `r2=B+q/kappa` has amplitude at most
`L^-2(n-j)`, so NQ-1 makes its forward potential sum geometric. The top
defect is again analytic and closed, now with the second momentum as a
parameter. The same local restoration enforces `w2_n=0`; it requires no
new harmonic lift or unrestricted inverse. Nullspace changes do not
change the stationary value because S annihilates them.

The bottom total-curvature square then contributes O(1) once. Soft q
squares contribute a convergent `L^-2s` series. In `U_a(w2)`, the bottom
term has amplitudes `L^-2n L^-n L^-n` against density `L^4n`, while soft
terms have a summable `L^-s` factor. The residual-containing R4 terms are
already summable. Polarizing before anchored absolute sums gives CJ2 at
q=4, conditional on CJ18. I found no additional unproved primitive beyond
CJ18 and the explicitly consumed contracts.

This is a substantive reduction to a source-specific bilinear curvature
estimate, not a proof that the estimate holds. No reverse implication
from the quartic bound to CJ18 has been established here; the strength
comparison is sufficient implication with converse unknown. Separate
absolute estimates of the bare commutator square and exchange can cost
O(n), but this is not a growth theorem for their completed difference.

## Independent computations and preserved failures

The [independent program](checks/review_charged_jet_independent.py) constructs
the actual paths with centered roots at zero, a translation of the author's
root convention. Sparse Q is assembled from a separately aggregated
geometric motif. Labelled product paths retain wrapped repetitions.
The source derivative uses explicit prefix/suffix cross products, and the
quartic uses direct multiplication of exponential Taylor polynomials.
Neither author BCH3 code nor automatic differentiation is imported.
Two rectangular least-squares solves implement the Moore–Penrose hidden
slice instead of the author's gauge-completed conjugate-gradient solver.
This is the stated implementation change from the criteria's proposed
gauge-completed solve; both fix the same gauge nullspace.

| Independent fixture | Result and discriminating evidence |
|---|---|
| [One-step SU(2)](checks/review_charged_jet_n1_02_out.json), fine `(3,6,3,3)`, top `(1,2,1,1)`, kappa=.8; 648 hidden links, 15,552 contours | 28/28 predicates. Bare quartic .1900390842, exchange .05152441268, completed .1385146716. Direct group extrapolation .1385154490 differs by 7.77e-7, below 4.77e-6. Source directional check differs by 9.62e-13. |
| [Depth-two SU(2)](checks/review_charged_jet_n2_01_out.json), bottom `(9,18,9,9)`, middle `(3,6,3,3)`, top `(1,2,1,1)`, kappas=(.8,1.3); 53,136 hidden links, 1,275,264 contours | 35/35 predicates. Intermediate Euler/forced transport residual 5.88e-12. Omitting DB gives .3794; omitting the funnel gives .2597; wrong kappa ratio gives .2267. Log covariance residuals at most 4.08e-12. |
| [SU(3) local matrix series](checks/review_charged_jet_su3_01_out.json), actual 1,944 centered paths; [criteria](checks/review_charged_jet_su3_criteria.md) | 15/15 predicates. CJ5 differs by 1.39e-17 and CJ6 by 2.39e-17. Removing the polar square changes the quartic by .04835. Determinant phase scales cubically and its trace correction sextically on the declared epsilon sequence. |
| [Gauge/counting supplement](checks/review_charged_jet_gauge_01_out.json), declared [after author-checker exposure](checks/review_charged_jet_gauge_criteria.md) | 10/10 predicates. Hidden gauge null residual 8.95e-15, source/gauge pairing 6.80e-16, and counting-adjoint equality exact to displayed precision. A false L^-4 adjoint changes the pairing by .2901. Constant harmonic links have zero curl but nonzero hidden soft cost. |

The first independent one-step attempt completed its calculations but failed
to serialize NumPy integer shape entries. Its
[original code](checks/review_charged_jet_independent_initial.py),
[empty stdout](checks/review_charged_jet_n1_01_out.json) and
[traceback](checks/review_charged_jet_n1_01_err.txt) are preserved. The sole
code repair converts those shapes to Python ints. No formula, criterion or
tolerance was changed. The successful retry, depth-two run and SU(3) run
all preceded author-checker inspection. The later gauge supplement is
explicitly post-exposure. The [attempt record](checks/review_charged_jet_attempts.json)
records chronology, commands, limits and failures.

The independent mutations detect exchange omission/sign/half-factor,
path-divisor error, endpoint removal, colour-commutator removal, polar
square omission, current half-factor error, source/funnel omission,
kappa-ratio error, self-loop incidence collapse, counting-adjoint
rescaling, and omitted four-dimensional density. Their observed witnesses
exceed the matching numerical residuals by the declared margins. Pure
scale arithmetic is only an arithmetic check; the uniform estimates above
come from proof, not this predicate count.

The rectangular quotient deliberately contains self-loops at the top. Its
incidence difference `d*` cancels a self-loop, but the incoming-plus-outgoing
bracket counts it twice. Using `abs(d)` after sparse cancellation would be
wrong; the independent program keeps both labels and detects that mutation.
Neither this geometry nor the author's rotated `(2,1,1,1)` fixture proves
a uniform theorem by sampling. No depth-two quartic group comparison was
run, and the one-step comparison is not interval-certified.

The author programs, outputs, initial/final diff, criteria and failure record
were inspected only after the independent controls. They were not rerun;
their 40/40 and 19/19 are author evidence, not additional independent
validation. The original 36/37 outcome is correctly preserved: its
constant-field endpoint detector was ineffective. For constant
noncommuting links, an individual contour has nonzero BCH2, but centered
offset averaging kills its mean exactly. The linear curl and residual
vanish, the constant plaquette commutator has zero counting divergence,
and CJ7 gives zero cubic source. The surviving quartic is the single
bottom Wilson contribution. This provides no marginal-growth conclusion
for nonconstant data.

## Literature boundary and final handoff

Existing registered literature was consulted before considering any new
import. Dimock's [Covariant Axial Gauge](https://arxiv.org/html/1410.2798v3)
uses abelian hard averaging and axial constraints; Proposition 6 requires
`QA=0` and `tau A=0`, and its displayed proof specializes to d=3. Its torus
discussion separately suppresses torons. These domains do not supply the
soft full-colour inverse in CJ18. Selected definitions and proof passages
were read directly, not the entire paper.

Dimock's [multiscale QED paper](https://arxiv.org/html/1712.10029v3)
defines hard constrained minimizing orbits with Landau/axial gauge and
prescribed nested regions. Theorem 1 also requires earlier axial data,
admissible scale weights and sufficiently large M. Those hypotheses and
its d=3 connection normalization differ from the present d=4 soft
integrated-link problem. Its locality architecture is comparison material;
no estimate from it is adopted to close CJ18. The existing Bałaban access
record was treated as historical context, not proof of an unread theorem.

One scientific review iteration is complete: zero material source findings,
zero source fixes, no skipped known defect. There was one repaired reviewer
serialization failure and one explicitly disclosed post-exposure supplement.
No commits, PRs, audit operations or full validation pipelines were performed
by this reviewer. The coordinator's combined gates and any later independent
audit remain separate. The final
[evidence receipt](checks/review_charged_jet_receipt.json) freezes this report,
read identities, criteria, code, successful outputs and failed attempt.

The next mathematical obligation is precisely CJ18 for the actual source
and hidden gauge domain. A one-step identity-background finite-u covariance
does not establish it. Even a future CJ18 proof would close only this
quartic producer: the finite-part increment, nonlinear flow, complete
continuum hierarchy and physical Hamiltonian gap require their own proofs.
