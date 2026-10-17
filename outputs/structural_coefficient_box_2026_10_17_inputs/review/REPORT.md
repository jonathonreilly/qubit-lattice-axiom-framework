---
review_type: bounded_independent_mathematical_review
exposure: source-exposed_same-model_with_prior-premise-reuse
disposition: conditional-new-argument-supported_no-material-blocker-found
retained_status: not_assessed
---
# Review of the structural coefficient box

The new argument follows conditionally from its pinned stationary, interval
and generic packet premises. I found no material mathematical correction
needed in the frozen candidate. In particular the sign in its surface
resolvent, the fixed-channel matching perturbation, the retained packet
constants and the actual-scalar phase contract are consistent. The declared
ten-coefficient box supports the complete isometry ceilings **0.0112** on
the infinite clock for every `t>=2*10^13`, and **0.0122** for the specified
finite clock only through `t=4*10^13`. These statements require the supplied
ready vector, prescribed positive block forms, exact dark vacuum, exact old
Hamiltonian and uniform exact clock hopping. They do not supply those physical
permissions or the exploratory emitter.

This is provisional mathematical review, not a formal audit, publication
approval, retained-status decision or demonstration of an installed device.
The phase and structural exclusions are essential: the countercases below
reject plausible stronger readings of the result.

## 1. Source identities, prior exposure and coverage

The reviewed candidate is
`structural_coefficient_robustness/CANDIDATE.md`, SHA256
`5d3c2dd41f6af96bf7bd793b5e5cfe39e5d0f5c7c0d16517c95249542cdc81ca`.
Its author freeze is SHA256
`5e526899bf7d17b1546f8eed8497bd48220c3238ffc4b5f186f044613005078a`.
The complete changed argument, author arithmetic source, result, source
binding, freeze and source-pin metadata were inspected. The historical author
receipt and both complete logs were read. They have been preserved unchanged.
[SOURCE_PINS.json](SOURCE_PINS.json) records sixteen exact snapshots and
[SOURCE_RECHECK.json](SOURCE_RECHECK.json) confirms their originals remained
unchanged at the final source check.

This reviewer previously authored the stationary and interval reviews.
Consequently this is source-exposed same-model checking, not blind or
model-diverse checking. The following complete prior mathematical bodies
had already been read in those reviews; their identities were verified and
the premises affected by the new coefficient argument were refreshed here:

| Reused source | SHA256 |
|---|---|
| Interval candidate | `b386126649516e533da29182a6cf9eac2da314538ae9b072a2262d7c5c78ed45` |
| Exact interval certificate | `a98e272fa5d65e6177670ce2dfb52498ed942b8bd9996a0b9b16838d4e0c2251` |
| Interval independent review | `a3ab8c94ce4c842980e2144766be0994b5f5d783f29d14d1cd25a7a2567dfe8a` |
| Generic packet THEOREM_V2 | `db1a25ee639337a99800f8b8c27dbf366861a6707116f559029697c9f8aaf0e3` |
| Root interval qualification | `33f4e340f2909d907e4c8fe166c86b306e82e369a6fa3ddb5eca1ab4f19405c8` |

The root qualification was read completely. In particular it retains the
stationary point-state/reflection premise from the earlier review SHA256
`23b78506dc56fe141f9e19347b60ed0e420b4e817b599cafa246a502a2a3f830`
and full-basis witness SHA256
`b04ab3b89b699814334d27e867bc2b5ed57295cb4d558eda1e8b9289ad96ec44`.
Their current file identities were refreshed in
[REUSED_PREMISE_PINS.json](REUSED_PREMISE_PINS.json). The earlier interval
run rechecked the point matrix/root/inverse certificate, while inheriting
the point-state/reflection calculation from the earlier stationary run.
**This new execution recomputes neither historical point calculation.**
It uses their qualified uniform bounds `g=9/50`, `A=166` and central common
phase error `1.76*10^-13` as pinned premises.

The supplied worktree revision is
`0e8375354c42963234cc4b15b14ab6bb553c713d`. Current workflow SHA256 is
`71cab17ea2d5ec892b5d9dbefd608c0d51e77ea398a62f33679736510d9f63d3`.
Current workflow and the physics-claim-reviewer skill were applied with the
explicit same-model/no-delegation instructions. No Git operation was used to
change or independently attest the supplied revision.

## 2. Fixed open channels and positive physical blocks

In the exact physical bit basis `(old1,old2,A,B)`, independently constructed
derivative matrices satisfy `D*=D`, `D^2=mD`, with nonzero trace and
`m=(1,1,2,1,2,2)` for the six bulk coefficients. These identities establish
positive spectra `{0,m}` and exact norms `m`, without a floating eigensolver.
Every such derivative annihilates the entire four-dimensional embedding
`iota`, commutes with `X1X2`, and preserves source number. Therefore arbitrary
simultaneous real errors of magnitude at most `a=10^-8` give

    ||delta B|| <= 9a=b,
    ||delta VA||, ||delta VB|| <= 3a=c,
    Btilde iota = iota K.

The four simultaneous old-energy/parity vectors were constructed explicitly
as `( |00>+p|11> )/sqrt(2)` and `( |01>+p|10> )/sqrt(2)`, tensored with the
source vacuum. Their projections are unchanged. Selfadjointness then gives
both `Q Btilde P=0` and `P Btilde Q=0`. Within each parity sector, the closed
space has dimension seven: the other old-vacuum vector and all six
source-excited directions. The argument does not silently omit a second old
energy. Closed eigenvalue degeneracies or crossings do not change this fixed
projection argument.

The local contact `n_c(I+X_A)` satisfies the same positive norm-two
polynomial on the full two-qubit space; the vacancy `I-n_c1` is a positive
norm-one projector. All ten coefficients remain positive even at their
lower box endpoints. In the one-head sector the vacancy contributes
`nutilde I - nutilde P1`; its negative matching coefficient is accompanied
by the actual positive physical scalar. The script also verifies that the
interaction need not commute with literal `K`. No commutation shortcut is
needed for the later aging statement.

## 3. Surface resolvent, matching norm and shared right side

For the fixed closed space, write `R=(H_Q-lambda)^-1` and
`Rtilde=(Htilde_Q-lambda)^-1`. The infinite-tail perturbation is the bounded
operator `I_clock tensor Q delta B Q`, with norm at most `b`. The inherited
gap and the resolvent identity imply

    ||R|| <= 1/g,  ||Rtilde|| <= 1/(g-b),
    Rtilde-R = -Rtilde (delta H_Q) R,
    ||E*(Rtilde-R)E|| <= b/[g(g-b)].

This argument uses the bounded selfadjoint half-line operators, not a finite
tail truncation. A separate exact, noncommuting two-channel/two-site example
checked the identity and its compressed sign, but that finite example is
only an algebra discriminator.

The surface sign can be derived directly. If
`d=2J+b_channel-lambda=J(q+q^-1)`, an endpoint Green vector has
`G_1=qG_0`. Its endpoint equation is `dG_0-JG_1=1`, hence `G_0=q/J`.
Consequently

    F=lambda-2J-B+J exp(ik)P+J^2 G_Q

has closed entry `-d+Jq=-J/q` and open entry `-J exp(-ik)`.
Both real signs of the decaying root are covered. The independent exact
checks used `q=1/7` and `q=-1/8`; replacing `G_Q` by its negative gives
endpoint right side `-1` and changes `F` by `-2Jq`, which is nonzero in
both cases. Thus the sign is discriminating, not accepted merely because it
appears in both author formulas.

The two matching matrices differ only on their diagonal blocks. In Euclidean
operator norm, the norm of this block diagonal difference is the maximum
of the two block norms. The first is at most `b+c`; the second is at most
`b+c+J^2 b/[g(g-b)]`. Thus the candidate's `eta` is valid without assuming
commutation between the old and source interactions.

The site-1 exterior extrapolation is

    phi_2=Qlead phi_1+(exp(-ik)-exp(ik))u.

Substitution into the actual site-1 equation gives exactly
`rhs=[0; J(exp(ik)-exp(-ik))u]`. Its norm is at most `2J`. Both systems
have this same right side because `u`, `lambda`, `J` and the origin
convention remain fixed after the common scalar is removed. Therefore

    xtilde-x = -Mtilde^-1 (delta M) M^-1 rhs,
    ||xtilde-x|| <= 2J A^2 eta/(1-A eta).

An independent exact free-boundary solve checks the row-zero/sign convention;
a changed-matrix/same-RHS solve checks the inverse-to-state identity. A
changed RHS would add a term and is not covered by this estimate.

The exact arithmetic was reorganized through the common denominator
`g(g-b)-A[(b+c)g(g-b)+J^2 b]` and through
`e_R=2J(A_actual-A)`. The positive denominator and all strict ceilings were
verified by exact rational comparisons. Relevant values are:

| Quantity | Display only | Proven ceiling |
|---|---:|---:|
| Remaining closed gap | 0.17999991 | greater than 0.17 |
| Matching perturbation | 1.2250352034045987e-7 | less than 1.226e-7 |
| Physical inverse | 166.00337577565486 | less than 167 |
| Bridge inverse | 367.3098974809548 | less than 368 |
| Extra reflection error | 0.00020268904500846948 | less than 0.000203 |

Exact fractions and positive margins are in
[RESULT.json](runs/attempt_1/RESULT.json); floating displays are not enclosures.

## 4. Packet constants, columns and complete outputs

From `g-b>0.17` and `2+0.17/J>7+1/7`, each closed root still obeys
`|q|<=1/7`. Differentiating at a fixed actual coefficient choice yields
`q'=2 sin(k)q^2/(1-q^2)` and `|q'|<=1/24`; the eigenbasis of that fixed
internal matrix is momentum-independent. No derivative of eigenvectors
with respect to coefficient error is used.

The inherited Schur elimination remains an exact algebraic identity in any
orthonormal actual channel basis. Its coefficient maps satisfy
`||Amap^-1||=||Qlead||=1`; eliminating the third row for an arbitrary
right-hand side costs `sqrt(2)`, stacking the reconstructed components costs
another `sqrt(2)`, and the remaining term costs `J^-1`. Hence the new
physical inverse ceiling gives `||M24^-1||<=2*167+J^-1<368`. This is the
same Euclidean norm convention as the generic theorem.

The independent scalar path bounded the derivative radical by `3.63`,
`sqrt(2)` by `99/70` and `sqrt(5)` by `56/25`, with their squares checked
as rational inequalities. It gives upper proxies `X0<15.625` and
`X1<666.402`, so the candidate's unchanged `X0=16`, `X1=700` remain safe.
The full localized correction, including both contacts and all closed tails,
then has `C0<31` and `C1<=2690.4<2700`. The second geometric derivative
sum `(1+kappa^2)/(1-kappa^2)^3` is included.

Selfadjoint current conservation gives `|r|=1` since the remaining channels
are closed and the matching problem is invertible. It follows that `L=700`
and `CA=CB=2001` still work. The grouped localized column bound is

    Dj <= 18601111/300,
    sqrt(2)*Dj < 88000.

The factor `sqrt(2)` is retained for the two potentially nonorthogonal
localized error columns within each parity. The propagating error columns
end in distinct fixed orthonormal vacuum old states, so their operator
norm uses the maximum reflection error. The new `e_R` is therefore added
once to the inherited phase budget, not four times and not multiplied by
elapsed time.

The ready vector and ideal clock packet depend on unchanged `J`, `f`, the
momentum interval and free reflection `r0`; none needs recalibration. The
generic incoming-packet construction applies separately to each fixed actual
operator with the same uniform bounds. Its normalization, initial mismatch
and bound-state residual estimates therefore remain available. This does
not assert that the actual supplied preparation has zero bound-state
amplitude, or infer an all-future result from a central point fit alone.

The entire output, including source and clock, is compared as an isometry
with arbitrary passive reference. In the generic eigenfunction evolution,
the old-energy phases accumulate for the full elapsed `t`, yielding the
literal `exp(-itK)W`. This uses the exact source-vacuum embedding and old
energy labels, without asserting `[Hphys,K]=0`.

## 5. Finite resources and physical loads

Independent summation of the positive bulk weights gives
`B_upper=19.11456446684866`, exactly agreeing with the old rational ceiling.
After the errors, `Btilde<=19.11456455684866 I<20I`, while positivity gives
`Btilde>=I`. Computing the two contact spectra gives the old maximum
`7.925057370220605`; adding `c` gives less than eight. Thus

    2J+(20-1)/2+8 < 18

is sufficient for both the infinite operator and its finite compression
around the stated center, with the actual `nutilde` shifting only that
center. The clock is still nearest-neighbor and its far-end `J n_(M-1)`
correction is unchanged. Onsite mixing does not shorten the omitted-hop
distance.

With `T=10^13`, `eta_p=10^-3` and `N=22*10^12`, the independent arithmetic
checks the inherited stronger finite-support inequality. Its positive margin
is `44695854048668/675`. With `M=9*10^14`, the first omitted site is at
distance `M-N+1=878000000000001`; the conservative Chebyshev condition
`dM>18*(4*10^13)*(6/5)+9` has margin `13999999999992`. The previously
checked analytic exponential estimates behind that sufficient condition
are reused. No chain of either size was allocated or evolved.

Adding the newly certified reflection error to the pinned complete budgets
gives displays `0.011147623271512414` and `0.012147623271512415`, with strict
exact bounds below `0.0112` and `0.0122`. Complete unhalved trace distance
is at most twice the corresponding isometry error. The fixed finite clock
has only the specified finite horizon.

Each old site's incident change is at most `2a`; each source site's is at
most `8a` from weights `1+2+1+2+2`; each contact clock site's is at most
`3a`. The source weights include its contact coupling. The bulk clock
bonds are fixed. The added old-site cap of two remains strict; source and
contact loads remain substantially larger. Existing old-edge load is still
additional. No all-site cap, laboratory cost or preparation algorithm follows.

## 6. Phase contract and discriminating excluded cases

The origin conversion is `r_abs=exp(-2ik)r_site1`. The independent free
boundary solve yields `r_site1=-exp(4ik)` and therefore
`r0=-exp(2ik)`. The fixed calibration scalar
`zeta=-exp(-4ik0)alpha` satisfies
`r0(k0)zeta=exp(-2ik0)alpha`. The coefficient comparison uses this same
nominal scalar and target `W`; it does not refit a column phase.

The physical vacancy scalar is separate. The correct complete comparator is

    zeta exp(-i nutilde t) beta_(t-T) tensor iota exp(-itK)W.

If one insists on nominal `nu`, the exact extra pure-isometry cost is
`|exp(-i delta_nu t)-1|`, bounded by `min(2,a t)` but not uniformly small.
For the allowed choice `delta_nu=a` and
`t=80001*pi/a>2*10^13`, this difference is exactly two. Conditional on the
proved actual-scalar estimate, the actual output is then more than
`2-0.0112=1.9888` away from the nominal comparator. This is an exact
comparator calculation and triangle inequality, not a simulated trajectory.
The nine-coefficient corollary with `nu` fixed avoids that obstruction and
may retain the conservative same bounds. A reduced channel's indifference
to global phase does not alter this chosen pure-isometry contract.

For darkness, the positive two-level perturbation
`epsilon[[1,1],[1,1]]=epsilon(I+X)` has norm `2epsilon` yet a nonzero
`Q delta B P=epsilon` for the original vacuum projector. The independent
test uses `epsilon=10^-12`. Arbitrarily small positive errors can thus
destroy the fixed-channel premise when they are allowed to leak from the
vacuum. This example is outside the prescribed coefficient box; it exposes
why an arbitrary-operator-norm noise claim would require a different proof.
It is not a no-go theorem for all other error models.

## 7. Actual execution, provenance limitations and disposition

[check_structural_box.py](check_structural_box.py), SHA256
`e82bc008d335e439c84bfa0117ad2aa391539e40bade3c53be8cce68684dd7ad`,
was executed exactly once by [run_check.py](run_check.py). The predeclared
limits were 45 CPU seconds, 60 wall seconds and dimension at most 32.
Actual wall time was **0.6041657919995487 seconds**, exit code zero, with
empty stderr. The largest matrix was **16**, and the largest inverse was
**4**. Python was 3.13.5 and SymPy 1.14.0. No failed execution occurred;
the rejected wrong-sign/origin and excluded-case tests remain recorded in
the complete result. Both stdout and stderr, launch-time source/input pins,
executed source copy and receipt are under [runs/attempt_1](runs/attempt_1).
The checker and input pins were unchanged across execution.

This was a distinct physical-basis, recurrence, noncommuting identity and
exact scalar derivation. It did not execute or import the author checker,
fit parameters, sample the coefficient box, invert the historical fitted
matrix, recertify the stationary amplitudes, perform quadrature, or simulate
time evolution. The infinite resolvent and packet implication above are
reviewed analytical steps, not claims established by the count of finite
assertions. [RESULT.json](runs/attempt_1/RESULT.json) contains the complete
exact margins and countercases rather than only a PASS summary.

The historical author execution receipt has a null child-source-at-launch
field because it ran through a `python -c` wrapper. Its separate source
binding is explicitly post-execution author testimony. I preserve that
limitation and do not treat it as a contemporaneous source pin. It does
not block this result: the frozen script was read and the load-bearing new
comparisons were independently reconstructed in a launch-pinned execution.

The safe disposition is conditional provisional reuse of this exact new
argument and its stated box, retaining the actual-scalar qualification,
structural darkness, supplied readiness, infinite blank tail for permanence,
and finite horizon for a finite apparatus. There is no new closure of
native preparation, the autonomous emitter's missing inverse/overlap/time,
generic noise robustness, precision installation, feasible hardware, reset,
reuse, or arbitrary exact accuracy. No author file, repository file, shared
checkpoint, editable prompt, physical axiom, Git state or audit output was
changed by this review.
