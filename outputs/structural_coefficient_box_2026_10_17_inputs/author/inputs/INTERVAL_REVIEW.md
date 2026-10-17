# Review of the fixed old-cap interval-to-wavepacket composition

**No blocking mathematical finding for this frozen conditional composition.**
The supplied positive two-body ladder meets the generic packet theorem's
concrete interval, channel, matching-norm and common-phase hypotheses. The
specified finite product preparation gives complete isometry error below
0.011 for every elapsed time at least `2*10^13` on the infinite half-line.
The embedded finite apparatus of `9*10^14` clock sites gives error below
0.012 for `2*10^13 <= t <= 4*10^13`. These are conditional analytic bounds,
not a large-device simulation, native preparation or all-site-cap theorem.

This review supports source-specific provisional mathematical reuse. It is
not an audit verdict, retained status, hardware realization, model-diverse
check or proof-assistant verification. The fixed central calibration error
remains in the bound. No arbitrary-accuracy family is established.

## Reviewed sources and coverage

The complete 513-line [candidate](sources/candidate/CANDIDATE.md), complete
interval certificate program and launcher, complete 600-line controlling
[generic theorem V2](sources/generic/THEOREM_V2.md), the complete separate
[generic review](sources/generic_review/REVIEW.md), and root qualification
and acceptance were read. The author execution receipt, freeze, source
manifest, V2 delta, certificate and serialized witnesses were inspected;
all JSON data were parsed and their identities checked. The new certificate
program was read as source, not executed by this reviewer.

| Source | SHA256 |
|---|---|
| Concrete CANDIDATE.md | `b386126649516e533da29182a6cf9eac2da314538ae9b072a2262d7c5c78ed45` |
| certify_interval.py | `06b71bb656d17289d0f1759f9dd385bf9a49e07d58e6c840f4741eca6ae1e07f` |
| CERTIFICATE.json | `a98e272fa5d65e6177670ce2dfb52498ed942b8bd9996a0b9b16838d4e0c2251` |
| POINT_WITNESSES.json | `7c231289b52353abee06063737bb202fd413fa17a426c13e696e5967014e86c2` |
| Generic THEOREM_V2.md | `db1a25ee639337a99800f8b8c27dbf366861a6707116f559029697c9f8aaf0e3` |
| Generic independent REVIEW.md | `bba09ef378466a3787ebfbbbd942a81fbe200031a24d04f799d2543e510673f6` |
| Root QUALIFICATION.md | `a1700102e8d15d37252469e3af6df5648d8054ff77e3bf836f3802328c25826f` |

The stationary reflection claim is reused within the exact scope of my earlier
[review](sources/prior_review/REVIEW.md), SHA256
`23b78506dc56fe141f9e19347b60ed0e420b4e817b599cafa246a502a2a3f830`.
Its old-cap source, exact parameters and certificate agree with the current
candidate inputs. Its full-basis witness is
`b04ab3b89b699814334d27e867bc2b5ed57295cb4d558eda1e8b9289ad96ec44`.
The old point search and author programs were not rerun. The earlier
reviewer program was reread to check the basis ordering and witness meaning.
The present calculation rechecks the physical point matrix, square-root and
inverse certificates; it does not recompute the old point-state residuals
or four reflection amplitudes. Those remain supported by that pinned prior
review and its execution. The present input packet preserves their complete
state witnesses, result and receipt as well as the inverse witnesses.

[SOURCE_PINS.json](SOURCE_PINS.json) records all 35 selected source snapshots,
including the complete inputs, prior calculation/receipt, process sources
and current-main instruction revision
`5b0e1cc44f422fb0138b02eb071d3d16b40dfbb2`. The current-main science workflow
controls this review. No Git or network freshness operation was attempted.
The task's explicit inherited-model instruction controls over older skill
defaults. No override or nested delegation was used.

The generic review assessed the original theorem. V2 changes only the
velocity and curvature equalities to certified lower/upper bounds, with
one explanatory sentence. I read V2 in full and checked that its proof uses
exactly those inequalities. The historical interval execution remains
correctly pinned to the original generic source; it is not relabeled as a
V2 execution. The old theorem's frozen metadata saying review pending is
historical source metadata; root qualification and this report separately
record later review scope.

## Uniform channels and physical inverse

Candidate sections 1–3, lines 44–209, preserve the exact sixteen-dimensional
old/source model. In the complete physical bit basis, the reviewer code
reconstructs `B`, both contacts and old parity, checks their exact symmetry
and reducing commutators, and verifies `B iota = iota K` on every source-vacuum
old vector. There is no assumption that the interacting Hamiltonian commutes
with `K`. The signed contact `mu1` is accompanied by the physical reserve
`nu=-mu1`, so the physical vacuum energies are `1+nu` and `3+nu`.

On the interval of half-width `1/1000`, `|epsilon'| <= 2J` gives the exact
rational energy enclosure used by the author. Positivity gives

```
B on source-excited states >= 1 + min(DeltaA,DeltaB),
source gap >= min Delta - 2 - epsilon_high
           = 0.18114012916808103... > 9/50,
other old-vacuum band gap >= 2 - 4J
                         = 1.879915571571872.
```

The source subspace is invariant for the fixed bulk `B`; source number
preservation is needed here, not during contact scattering. Within each
exact parity sector each vacuum old energy is simple. Consequently each
incident energy has exactly one open channel, and all seven others are
closed. The scalar `nu` shifts both band and incident energy, leaving these
gaps unchanged. This checks both old energies and both parity sectors.

For every closed channel, `|q+1/q| >= 2+g/J`, and the checked inequality
`2+g/J > 7+1/7` gives `|q| < 1/7`. Differentiation gives
`q'=2 sin(k) q^2/(1-q^2)` and `|q'| <= 1/24`, including negative roots.
The fixed bulk spectral projections have no momentum dependence. Thus

```
F_open' = i J exp(-ik),
F_closed' = 2J sin(k)/(1-q^2),
||M16'||2 <= 2J/(1-(1/7)^2) = 0.061293093676857.
```

The first matching diagonal block has derivative `epsilon' I`; the second
has the displayed spectral derivative; the off-diagonal bonds are constant.
This proves the stated spectral derivative estimate without eigenvector
rounding. Sine's Lipschitz bound gives positive velocity throughout the
interval and excludes both endpoints of `(0,pi)`; `v=1/40` and `E2=2J` are
valid conservative constants.

The author's point row-sum proof is sound: a complex symmetric inverse has
equal ordinary modulus one- and infinity-norms, so its spectral norm is
bounded by that row-sum ceiling. The certificate's `|Re|+|Im|` row sums
dominate the ordinary modulus norm. The square-root residual/Sylvester
argument and inverse perturbation are the same checked stationary method,
with exact rational comparisons. No unreported factor of the dimension is
needed to pass from the author's ceiling 164 to the spectral norm.

I additionally checked that step through a distinct full-basis calculation.
The prior independently proposed twelve-dimensional square root and
thirty-two-dimensional inverse matrices were read by immutable identity.
Their physical matrices were reconstructed from bit actions, and their exact
residuals recomputed. For the square root `S`, the positive lower bounds
`a=d-2J`, `b=d-||S-D||infinity` give the already checked Sylvester residual
bound. Here its *spectral* error contributes half that bound to the physical
matching matrix; there is no infinity-norm dimension conversion.

For each of the two total energies, the new argument uses

```
||N||2 <= ||N||F < 119,
||I-Mhat N||2 <= ||I-Mhat N||F < 10^-54,
||M-Mhat||2 <= delta,
||M^-1||2 <= 119 / (1 - 10^-54 - 119 delta) < 120.
```

Every squared Frobenius norm and `delta` is calculated exactly in
[RESULTS.json](RESULTS.json). This is the complete physical 32-by-32 system
with both parity channels, not the author's 16-by-16 parity row-sum test.
Unitary parity reduction makes each physical 16-by-16 inverse a restriction
of this full inverse. The frozen author's four inverse proposals also agree
with the exact parity compressions of these independent inverse proposals
to entrywise `|Re|+|Im|` error below `10^-50`; all their serialized entries
were included in that comparison.

Applying the same analytically derived derivative bound gives an independent
uniform spectral ceiling approximately `119.87434889384814`, with the strict
rational check `<121`. This supports the candidate's deliberately weaker
`<166`. In particular, the candidate's own exact expression

```
164 / (1 - 164*(0.061293093676857)/1000) < 166
```

is reproduced. This is a non-grid interval certificate. It does not infer
regularity or absence of a resonance from point sampling.

## Matching dimension, signs and common phase

Candidate section 4, lines 211–267, uses the actual generic theorem's
Euclidean coefficient convention. In an orthonormal bulk eigenbasis, set
`A=diag(exp(ik),q_l^-1)`, `E=diag(exp(2ik),1)`, and `Q=EA^-1`.
Then `||A^-1||2=||Q||2=1`. The third arbitrary-RHS matching row gives

```
y = A^-1 x1 + J^-1 A^-1 f2.
```

Substituting it into the second row yields

```
M16 [x0;x1] = -[f0; f1+Q f2],
D1-JQ = -(F-VB).
```

For closed channels the latter identity is precisely
`J(q+q^-1)-Jq=J/q`; for the open channel it uses
`2 cos k-exp(ik)=exp(-ik)`. This establishes the signs without assuming the
Schur complement. The RHS map has norm at most `sqrt(2)`. Stacking the
solution with `A^-1 x1` costs at most another `sqrt(2)`; the remaining
`J^-1 A^-1 f2` term costs at most `1/J`. Therefore

```
||M24^-1||2 <= 2*166 + 1/J < 366.
```

All internal changes of coordinates are unitary; the closed coefficients
are coefficients of orthonormal internal vectors at site 2. The inverse
estimate therefore applies to the theorem's genuine 24-by-24 matrix, not
a rescaled row convention. Its minimum singular value is strictly greater
than `1/366`.

The checker also constructs an exact three-channel instance with one open
root and positive and negative closed roots `1/7,-1/8`. For every RHS basis
column, the 6-to-9-dimensional Schur reconstruction multiplies back to the
identity. Replacing the reconstruction's positive `J^-1` term by a negative
term yields a residual entry exactly `-2`. This finite discriminator checks
the signs; the dimension-independent proof above supplies the 16-to-24
claim. The test does not substitute a toy matrix for the physical inverse.

Candidate section 5, lines 269–315, correctly converts the reference origin:
multiplying the site-1 incident stationary column by `exp(-ik)` produces
the absolute-site convention and gives

```
r_abs = exp(-2ik) r_site1,
r0_abs = -exp(2ik),
zeta = -exp(-4ik0) alpha,
alpha = exact r_site1_(s=-1,p=-1)(k0).
```

As an independent phase check, the missing-site condition at `n=-1` directly
gives `r_site1=-z^4`; no finite matching inverse is needed for that check.
The scalar algebra gives `r0_abs*zeta=exp(-2ik0)*alpha`. Dropping this
conversion yields the nonzero exact test residual `42/125-56i/125` at
`z=(3+4i)/5`, `alpha=(3-4i)/5`. Thus the test distinguishes the relevant
wrong phase convention.

Flux conservation gives exact unit modulus for `alpha`, with positive
velocity and only one open channel. The target has parity eigenvalues
`(-7+24i)/25` and `1`, commutes with `K`, and uses the *same* scalar for
all four logical columns. The inherited exact point error is retained as
`delta0=1.76e-13`; the new central rational replay agrees exactly with the
frozen point certificate. Since `|r_abs'|<=700` and `|r0'|=2`, the band
ceiling `Delta <= delta0 + 702 sigma` follows. The `700` is already in the
absolute-site convention; no missing origin-derivative term remains.

## Packet constants and complete physical outputs

The generic theorem's needed normalization, aging and tail arguments were
checked against its full V2 body and the separate review. Its exact packet
columns evolve at their actual energies; the identity

```
exp[-i(T+s)H] Gamma_-T = Gamma_s exp[-i(T+s)Db]
```

supplies the full elapsed old aging. It does not factor the interacting
propagator through `K`. Parseval at past infinity, vanishing reflected and
localized pieces, and constancy of the evolved Gram matrix justify exact
packet isometry. Completeness of the scattering family and absence of
bound states are not assumed.

For the concrete constants, the checker independently integrates the
parabolic profile: its squared-profile integral is `16/15`, its integral
is `4/3`, and its total derivative variation is `2`. This gives the stated
normalization and verifies `F0<1/750`, `F1<2000` at `sigma=10^-6`.
Alternative rational square-root bounds check `X0=16`, `X1=700`, `C0=31`
and `C1=2700`. In particular, the derivative-tail estimate includes both
coefficient derivatives and root derivatives, with the geometric second
moment `(1+kappa^2)/(1-kappa^2)^3`.

The two old-energy localized columns in each parity sector need not be
orthogonal. The bound uses

```
Dj <= 62003.703333333...,
D = 88000 > sqrt(2)*Dj.
```

The parity sectors are orthogonal reducing output spaces, so their maximum
is appropriate. Propagating vacuum columns have orthogonal old states and
use the maximum phase mismatch. No additional `sqrt(2)` is needed there;
using that maximum for localized columns would have been unjustified.

The complete physical comparator is exactly

```
zeta exp(-i nu t) beta_(t-T) tensor iota exp(-itK) W x.
```

The vacuum-well scalar, full old aging, free-reflection phase and
positive-real packet normalization all remain. Both contact-site source
amplitudes and the entire closed-channel source tail are bounded, not
traced out. The product preparation is independent of the old input.
All operator bounds survive tensoring a passive reference, and the complete
unhalved output trace distance is at most twice the isometry bound.

The possible point-spectrum amplitude of the infinite-apparatus preparation
is at most `2 delta_in(T)` and remains included in the preparation error.
Finite truncation adds at most `eta_p`. The proof's weak past limit makes
the exact packets orthogonal to point spectrum; it does not make the actual
product input exactly orthogonal. This statement is correctly restricted
to the infinite operator, since the entire finite spectrum is point spectrum.

## Finite preparation and observation costs

All following fractions were independently reconstructed from rational
inequalities and matched exactly to the candidate certificate:

| Quantity | Verified sufficient ceiling |
|---|---|
| `delta_in(T)`, `T=10^13` | `75042263/32475000000` |
| Infinite clock, untruncated preparation | `269134782504763/27062500000000000` |
| Infinite clock, finite supplied preparation | `296197282504763/27062500000000000 <0.011` |
| Infinite point-spectrum amplitude after truncation | `91279763/16237500000 <0.005622` |
| Embedded finite clock through `4*10^13` | `323259782504763/27062500000000000 <0.012` |

For preparation, `N=22*10^12` gives `N-2JT` greater than each of
`1`, `2JT`, and `16(F1+F0)^2/(3 eta_p^2)`, with `eta_p=1/1000`.
The last comparison has positive exact margin `44695854048668/675`.
Using `pi>3` gives omitted norm at most `eta_p/4`; the proven incoming
norm lower bound and positive-real renormalization give the claimed
`eta_p` vector error. This specifies `N` Fourier integrals and a normalized
one-head vector. It does not produce those amplitudes experimentally or
with a native generator. Any additional preparation-isometry error is
an additional term, not included in the displayed zero-error supply premise.

For the finite horizon, the full internal positive-block enclosure is
`1<=B<=(955728223342433/50000000000000)I<20I`, and the signed contact norm is exactly
`Vmax=7.925057370220605`. Thus `rho=18` bounds the centered full operator
and its finite compression. The physical `nu` shifts only the center.
The far endpoint term `J n_(M-1)` is required to preserve the diagonal
`2J`; omitting it would change the stated compression and require a
different comparison.

For `M=9*10^14`, the shortest hop count from the preparation support to
the omitted site is `M-N+1=878000000000001`. Internal onsite mixing cannot
shorten it. Degree-below-hop-count polynomial equality, followed by the
Chebyshev/Bessel tail, uses the full physical internal operator rather
than a false old-generator factorization. Independent elementary Taylor
enclosures of `e` verify `sinh(1)<6/5` and the logarithmic allowance `<9`.
The sufficient exponent inequality has exact positive margin
`13999999999992`. The boundary error is below `1/1000` throughout the
stated horizon. No clock of this size was allocated or evolved.

The finite comparison is explicitly made after embedding its output into
the half-line space. It does not claim that the finite device contains the
entire ideal outgoing packet, nor accuracy at all future times for fixed
finite `M`.

## Qualifications and execution limits

There is no new rounding defect: `display_float` fields are visibly
approximate displays, and rigorous comparisons use rational strings.
The older `upper_float` labeling defect remains covered by the prior
qualification. The fixed target and fitted coefficients were exposed to
the author and reviewer; this is calibration verification, not a prediction
or blind target discovery. The positive point ceiling is not a lower bound
on the optimum, but it remains in every guaranteed accuracy statement.

Only the added old-site loads meet two: `1.993757127633340` and
`1.198638631120596`. Source loads are approximately `20.33` and `17.08`,
and entrance-clock loads approximately `8.02` and `6.73`; the separate old
edge has norm three. The full supplied positive nearest-neighbor two-body
Hamiltonian and one-head sector are inherited from the pinned stationary
review. There is no all-site cap-two result, native coefficient supplier,
precision robustness result, reset/reuse mechanism or selected Record
assertion. An infinite blank clock tail remains necessary for the stated
all-future half-line version. The finite apparatus has its explicit horizon.

[check_composition.py](check_composition.py) was run once through
[run_check.py](run_check.py), with a **60 CPU-second / 90 wall-second cap**,
and exited zero. The measured wrapper elapsed time was
**2.465158416889608 seconds**, user CPU **1.27571 seconds**, system CPU
**0.117984 seconds**, and macOS peak RSS **76,939,264 bytes**. Maximum
matrix dimension was **32**; reused square-root matrices were dimension
12 and the symbolic Schur discriminator dimension 9. Exact arithmetic
used Python Fraction and SymPy 1.14.0; NumPy 2.4.4 stored object matrices;
Python was 3.13.5. BLAS/OMP thread requests were one, without a measured
thread-count claim.

[EXECUTION.json](EXECUTION.json) preserves the command, environment requests,
source/output hashes and actual resource data. [check.stdout](check.stdout),
[check.stderr](check.stderr) and [RESULTS.json](RESULTS.json) are complete;
stderr is empty. No failed execution occurred in this review. The wrong
sign and wrong phase attempts remain recorded as rejected discriminators
within the successful run, rather than silently omitted.

The check is independent in its new load-bearing inverse arithmetic and
Schur/phase derivation, while openly sharing the same model, physical input
coefficients, generic theorem and earlier reviewer-owned rational proposals.
It is source-exposed, not blind or model-diverse. Numerical proposal matrices
were not newly generated here: their exact residuals and new spectral bounds
were recalculated. The infinite-time conclusion follows analytically from
the checked hypotheses and generic theorem; no finite computation measures
all future times. Full source and artifact identities were refreshed at
completion. No source theorem, shared checkpoint, editable prompt, axiom,
audit output, Git state, PR or other chat was changed.
