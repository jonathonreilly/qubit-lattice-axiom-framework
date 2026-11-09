# Independent check of original-source fourth response

2026-11-09. Research signal **advance** for the frozen bounded statement.
No material mathematical defect was found. This is a research check, not a
landing decision, audit verdict, retained status, or full compact spatial
response theorem.

## Sources, findings and reused coverage

The complete 280-line draft `parts/original-source-four-response.md` was read
from `/Users/jonreilly/.codex/worktrees/su2-two-block-response/Physics` in pack
`.claude/science/physics-loops/su2-gauge-aligned-response-20261108`.
Its SHA-256 is
`b305c708b5736f6dca707008bee7f3ceeb648b02bced785a82e5d1b3fa593f79`.
The source checkout and main pins remain
`55fd670ff8995427b24617b2273bd3f78b7559d9` and
`1e0d3b58dcda7f83152b0bb51729260247454d65`.

| Input | SHA-256 |
|---|---|
| full-compact-fourth-scaling.md | 549757b9574e7d50b8626ac0421889152cd2fae284f3d8589fe01309c3f86094 |
| nonlinear-chart-response.md | 5edacc8ee78d54b7fb853fb34da3d8cceffd8eb0e476f8510d15048f8f10f2d1 |
| compact-forest-exchange.md | b0d3a76a94a8cd43de186b1c93deb38327ea2b29aa2b1bbc16e1caa2e22ecef2 |

The same review session had already checked these exact inputs, including the
compact moments and cube mixed boundary covariance formula, in
`gates/four-response-independent-check.md`, SHA-256
`9eaa67d4f0d93db3578d01a12eca6741449291e9c04569129e5d89a0025a1860`.
That report is unchanged. Its source-specific mathematical coverage is reused;
its research signal is not substituted for the derivations below. Instructions
and the inherited supervising model/effort are unchanged. No model substitution,
numerical job, source edit, Git/network mutation or status operation was made.
Only this additional report was written; no editable prompt changed.

| Severity | Finding |
|---|---|
| Critical / high | None found. The conditional orbit covariance is retained with the correct cumulant and sign. |
| Medium | None found. The all-cut cancellation, u powers and merged-support comparison are valid. |
| Scope distinction, already explicit | This note's `tau_n` is a minimum spanning-tree weight built from distances between support sets. It is not the earlier chart note's nearest-neighbor connecting-graph length. A bounded support-diameter correction is needed when transferring between those conventions; the check below supplies it. |

## 1. Independent derivation of the complete identity

Let `F°=F-E_pi F`, and similarly center G,X,Y. Since X and Y are functions
of a, conditioning on a gives

```
E_h(F° G° | a) = C(a) + (f(a)-E_nu f)(g(a)-E_nu g).
Cov_pi(F,G) = E_nu C + Cov_nu(f,g).
Cov_pi(F,X) = Cov_nu(f,X),
```

with the analogous three other cross covariances. Substitute these identities
directly into the centered fourth-cumulant polynomial. The contribution from
the two conditional means is exactly `kappa4_nu(f,g,X,Y)`. What remains is

```
E_nu[C X° Y°] - E_nu C E_nu[X° Y°]
    = E_nu[(C-E_nu C) X° Y°]
    = kappa3_nu(C,X,Y).
```

This proves equation (1) without using the author's terminal-differentiation
argument or importing a total-cumulance formula. There is no other conditional
covariance term: a conditional cumulant involving X or Y with another argument
vanishes because X,Y are deterministic given a. As an algebraic identity it
even allows X=Y; distinct terminal links are required for its stated response
interpretation without a derivative-of-score term.

The original-link reader accounting is exact in the independent forest product
coordinates. `U_e=h(x)^* a_e h(y)` reads only its endpoint h variables and its
own retained a variable; for a fine tree edge a is fixed I. The fact that h
was constructed by a tree path in original coordinates does not introduce
additional h readers after the bijective change of variables. Thus f and g
have the stated a reader supersets, while C has their union. If the h reader
sets are disjoint, product Haar factorizes their conditional product at every
fixed a, giving C=0 even if the a reader sets overlap. No independence under
the quotient law is asserted or needed.

The terminal scores are functions of a alone because all intermediate h
variables telescope out of a terminal contour with root endpoints. Conditioning
on the fixed quotient cube changes only the a law, preserving the same Haar
conditional h law and the same identity.

## 2. Smoothness, symmetry and the two different scales

With h fixed, the retained-coordinate reconstruction is a product of left/right
group isometries and fixed coordinates. Differentiating F or G in a therefore
has uniform C2 bounds. Differentiation under compact Haar integration preserves
them. The product rule bounds the derivatives of C using the original C2 and
sup norms, with no tree-path or volume dependence.

Under a simultaneous conjugation, changing integration variables
`h -> k h k*` conjugates every reconstructed original link. Thus global
conjugation invariance of F,G implies it for f,g,C, although the original
sources can still depend on h. Their differentials at the quotient identity
vanish in every adjoint tangent copy. The global geodesic Hessian inequality
and the checked compact moments give
`||f-f(I)||_p, ||g-g(I)||_p, ||C-C(I)||_p = O(u^-1)`.
The score moments are `O(|v| sqrt(u))`.

For the first term of (1), fourth-order partition Holder gives the product
`u^-1 u^-1 u^1/2 u^1/2 = u^-1`. For the second term, the third cumulant is
unchanged after subtracting C(I), and its partition coefficients have absolute
sum six. Third-order Holder gives `u^-1 u^1/2 u^1/2 = 1`. A possibly nonzero
C(I) therefore does not produce an O(u) term. Conversely, these estimates do
not improve the variable part of C enough to assert O(u^-1) for the orbit term.
The draft correctly supplies neither that improvement nor a claim of a
nonvanishing O(1) leading coefficient.

As a limiting check, if both sources are the trace of the same fine tree link,
then f=g=0 and C=1/4 is constant. Both cumulants on the right vanish. Thus a
nonconcentrating original source does not by itself imply a nonzero response;
the note's distinction between a failed source-moment step and the actual
response is necessary and is preserved.

## 3. Generalized cut cancellation

The input chart moment estimates remain valid for the globally invariant
quotient functions f,g,C by the already checked cube symmetry and linear-tilt
gap argument. They do not follow by conditioning the full-law concentration
bound on a possibly rare global chart. With `q0=q-q(I)` and `B=A/u`, the
usable scales are

```
q0:  Lp size u^-1,    gradient Lp size u^-1/2;
B:   Lp size u^-1/2,  gradient Lp size 1.
```

The generalized cut argument works for these noncentered functions. To check
it, form an auxiliary law which is the product of the two *families of
insertion values* on the sides of a fixed cut. Its partition moments are
exactly `m'_B=m_(B intersect I)m_(B intersect I^c)`, and its mixed cumulant is
zero. This does not assert a factorization of the actual spatial Gibbs law.

Telescoping each partition product between m and m' leaves a sum of terms
with one crossing covariance. The variables in that covariance appear once
each; the remaining partition blocks contain precisely the remaining labels.
The product gradient rule and Holder with exponents at most 2n bound its two
gradients. The covariance prefactor u^-1 cancels their combined extra u,
while ordinary or split block moments contribute the other insertion powers.
Every label is consequently counted exactly once and every term has
`u^(-sum a_i) exp[-alpha r(I)]`. Fixed n=3,4 gives a fixed combinatorial
constant. The construction includes every `2|2` cut, so two internally
correlated, widely separated pairs do not evade the subtraction.

Applying this first with exponents `(1,1,1/2,1/2)` and then with
`(1,1/2,1/2)`, and restoring the two score factors u, gives respectively
O(u^-1) and O(1). The proof uses at most L8 insertion/gradient bounds and
finite coordinate moments; no third or fourth source derivative is needed.

## 4. Set-distance trees and the merged orbit support

For arbitrary finite nonempty supports, their pairwise set distances are
nonnegative weights on a complete label graph, even though they need not form
a metric. The minimum-spanning-tree exchange argument needs only these edge
weights. Removing its largest edge gives a cut all of whose crossing weights
are at least that edge. The largest edge is at least total weight divided by
n-1. This independently verifies the rate `alpha tau_n/(n-1)` from the
all-cut bound, including zero-distance overlaps.

For the merged support `T_F union T_G`, its distance to any other support is
the minimum of the two individual distances. Each edge incident to the merged
vertex in a minimizing three-label tree can therefore be assigned to a source
region that realizes that minimum. Splitting the vertex and adding the F--G
edge gives a connected four-label graph of weight
`tau_3^merge + d(T_F,T_G)`. The four-label minimum spanning tree cannot have
larger weight. This proves the inequality at lines 224–229 with the stated
direction, without treating set distance as a metric.

If the original sources share an h reader, their endpoint-inclusive source
regions both contain that endpoint's owner cell, so this added edge has zero
weight. For a fixed nonzero separation bound D it costs at most D, giving
the displayed factor `exp(alpha D/2)`. Enlarging a valid support decreases
the set distances and weakens the exponential bound; it is legitimate, but
does not establish decay inside that enlarged region.

For clarity when this result is reused with the earlier chart note, let
`tau_geom` be the minimum nearest-neighbor connected-graph length meeting
n support sets, each of diameter at most D. Realize the n-1 set-distance MST
edges by shortest paths between their minimizing endpoints. Inside support i,
join the endpoints of its incident edges by at most `(degree_i-1)` paths of
length D. These paths need not stay inside the support, which is allowed for
`tau_geom`. Since `sum_i(degree_i-1)=n-2`, this proves

```
tau_geom <= tau_n + (n-2)D.
```

Thus fixed support diameters convert the displayed regional exponential
bounds into geometric connecting-graph bounds with a fixed multiplicative
constant. Without such diameter control, that conversion is not valid. The
draft already distinguishes its merged support and its limited locality
claim, so no correction is requested.

## 5. Response normalization and exact scope

The reconstruction and the fixed chart do not move with the source or terminal
parameters. At zero sources the conditional h law is Haar. Distinct terminal
link scores have zero cross derivative, so the source/terminal logarithmic
coefficient is the full fourth cumulant just decomposed. The logarithm of a
normalizing denominator contributes its own coefficient with a minus sign.
It vanishes only when that denominator is independent of the varied terminal
coordinates, such as integration over all terminal links. No different
terminal-integrated or rough-exterior law is bounded by the numerator proof.

At nonzero source tilt the conditional orbit averages and covariance change
to their tilted versions; the Haar functions f,g,C cannot simply be reused.
The draft correctly restricts its identity as written and its new estimates
to zero source. It also leaves same-link score derivatives separate.

The supported result is the exact original-source decomposition, full compact
nonspatial O(u^-1)+O(1) control for the stated invariant C2 sources, exact
removal of the orbit term for disjoint h readers, and the displayed fixed-cube
regional tree estimates. Full compact spatial gluing, additional normalizing
laws, arbitrary terminal backgrounds and further blocking remain outside it.
Reopen this check if any frozen source, source class, reader convention or
domain/normalization input changes.
