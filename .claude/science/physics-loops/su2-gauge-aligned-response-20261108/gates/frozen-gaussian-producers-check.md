# Independent check of the frozen real Gaussian producers

2026-11-09. Research signal **advance** on the corrected frozen source.
One endpoint-count prefactor was missing and has been repaired by the author.
No unresolved material mathematical defect was found in the stated frozen,
zero-source covariance, principal-inverse, local-remainder or restricted
Gaussian identities. This is a research check, not retained status, an audit
verdict, or certification of a density-forest/connected-log consumer.

## Source identity, correction and scope

The complete 309-line initial draft `parts/frozen-gaussian-producers.md` was
read under
`/Users/jonreilly/.codex/worktrees/su2-two-block-response/Physics/.claude/science/physics-loops/su2-gauge-aligned-response-20261108`.
Initial SHA-256:
`c9f2c2fbf5cc3f504cbeafd51c7fe5fe842eadd4a78072fbea646821ee678f1c`.
Final checked SHA-256:
`ac4984909f5edbc5e79f9cb3ffd212862f43295d9a0537e0102fb4e38d0900c3`.
The changed equation (11), at lines 194–195, was reread. Removing its single
`exp(beta)` prefactor reconstructs the exact initial hash; no other source
byte changed. Necessary original premise text and the complete changed
argument were checked rather than inferred from prior verdicts.

| Severity | Finding and disposition |
|---|---|
| Low, resolved | An endpoint-inclusive shortest path at cell distance t has t+1 cells. The pinned norm weights its cardinality, but the original right side of (11) bounded only exp(beta*t). The author inserted exp(beta); the corrected explicit inequality and its uniform small-tail consequence now follow. |
| Critical / high / medium | None found within the stated supplier scope. |
| Unresolved material findings | None. Applicability of a later forest engine is expressly outside this check. |

| Mathematical input | SHA-256 |
|---|---|
| nonlinear-chart-response.md | 5edacc8ee78d54b7fb853fb34da3d8cceffd8eb0e476f8510d15048f8f10f2d1 |
| flat-two-step-bound.md | 0f028f694bb686cf4272d8620329f1f2e8535d8af9a2d028bbde6965cab3f03a |

These exact premises were read and checked earlier in this coherent task;
their original action, radial-normalizer and actual-Q precision arguments
remain unchanged. Source hashes were refreshed for this check. The inherited
source base is `55fd670ff8995427b24617b2273bd3f78b7559d9`. Main refreshed to
`bf92a1d763030836ed55631d5d7a7ef3b288f284` with audit metadata changes only;
the applicable instructions and mathematical inputs did not change.

The inherited supervising model/effort and applicable AGENTS, science
workflow and physics-claim-reviewer procedure were retained. No model
substitution, numerical job, source edit, Git/network mutation, formal
verification or status operation was performed. Only this designated report
was written; earlier gates remain immutable. No editable prompt changed.

## 1. Exact action, normalization and frozen Hessian

For U=exp(i a dot sigma), probability Haar on the injective identity chart
is `(2*pi^2)^(-1)(sin|a|/|a|)^2 d^3a`. The negative logarithm of each
normalized kernel is exactly

```
-kappa*u <output,M> + log Z(kappa*u*r)
 = kappa*u*(r-<output,M>) + h(kappa*u*r).
```

Thus (1) includes both kernel levels, the retained intermediate outputs,
the supplied fine normalization, and every coordinate Haar constant. The
normalizer has not been removed because it is independent of its output.
Each scalar local term is invariant under simultaneous conjugation; at
identity a linear term would be an invariant linear functional of a direct
sum of adjoint SO(3) vectors. Holding all but one vector zero shows that
each coefficient must vanish. This proves the stationary-point assertion
without requiring a rotation-invariant Cartesian domain.

The quadratic action is the actual flat-supplier quadratic with the
nonnegative variance correction
`eta_u = kappa*(1-Z'(kappa*u)/Z(kappa*u))`. In particular the coercive
piece contains `Q_1 a_1` and `a_1-Q_0 a_0`, with the actual contour-average
maps, not a substitute single-layer action. Also
`-log j(a)=|a|^2/3+O(|a|^4)`, so the rescaled Haar Hessian is exactly
`2/(3u)` per scalar coordinate. This recovers (3) and the uniform gap.

The range-two assertion uses the supplied complete factor geometry, and
the scalar absolute row bound uses its bounded reader count, bounded
incidence and finite family of normalized local Hessians. It does not
follow from an operator norm bound alone. These hypotheses hold for the
specified translated terminal-root forest slice; a different slice would
require rechecking them.

## 2. Covariance decay and positive truncation

With `T=I-H_u/M'`, the spectrum is nonnegative and its norm is at most
`r=1-g/M'<1`. In `H_u^(-1)=M'^(-1) sum_(m>=0) T^m`, all cell blocks
below `m=ceil(d/2)` vanish. Summing the remaining geometric series gives
`g^(-1) r^ceil(d/2)`, hence (4). The loose shell count `(2t+1)^4` is
uniform on periodic tori, including when balls have saturated the torus.
Multiplying by k scalar coordinates per cell proves the stated weighted
absolute row tail.

Entrywise truncation need not preserve positivity. Here the remainder is
symmetric, so its operator norm is at most its absolute row norm. Since
`C_u >= M^(-1)I`, choosing that tail at most `1/(2M)` proves
`P_u >= p0 I`, `p0=1/(2M)`. The upper and absolute-row bounds in (7)
follow from the same decomposition and `|P_ij|<=|C_ij|`. These estimates
are uniform in u and volume. The remainder E need not be positive; the
source correctly avoids treating it as an independent Gaussian covariance.
Positivity of the straight segment from P to C by itself establishes no
multi-parameter forest interpolation result.

## 3. Arbitrary principal inverses, uniformly as R0 grows

This was reconstructed for arbitrary scalar subsets I, not merely cell
unions. Every principal covariance `P[I]` has gap p0. For weights
`W_i=exp(theta*d(X(i),X))`, the triangle inequality gives

```
|W_i/W_j-1| <= exp(theta*d(X(i),X(j)))-1.
```

Using the original covariance envelope to bound P entries therefore
bounds both row and column sums of `W P[I] W^(-1)-P[I]` by A(theta).
For `theta<=gamma/2`, its summands are bounded by a fixed polynomial
times `theta*t*exp(-gamma*t/2)`, so A(theta) tends to zero. One theta
with `A(theta)<=p0/2` works simultaneously for every I, R0, u and volume.
Schur's test and the inverse perturbation series give operator norm at
most `2/p0` for the weighted inverse.

Set the base cell to X(j). The i,j entry of that inverse is
`exp(theta*d(X(i),X(j)))*(P[I]^(-1))_ij`, which proves (8). Summing
over j proves (9), with the same k-coordinate and polynomial-shell count.
Large individual finite-volume weights cause no problem because only
ratios enter the perturbation. The proof specifically uses the inverse
of the principal covariance, not the generally different principal
restriction of the full inverse. Empty I is vacuous.

Crucially, theta and v_core were chosen from the C envelope and p0,
without any R0 factor. One may consequently increase R0 until E is small
relative to any fixed positive tolerance depending on v_core. This would
not follow from a generic finite-range inverse estimate whose constants
deteriorated with the core radius.

## 4. Remainder paths and the corrected pinned norm

The ordered matrix atoms sum exactly to E. Their deterministic paths are
shortest periodic nearest-neighbor paths, with both endpoint cells retained.
A shortest path of length t has t+1 cells. If it contains a given cell x,
both endpoints lie within distance t of x. Thus at most `(2t+1)^8` ordered
cell pairs and k^2 scalar pairs can contribute at distance t. This safely
overcounts congestion, including for a torus with wraparound.

Combining this count with the covariance envelope gives

```
Pin_beta(E)
 <= exp(beta)*(k^2/g)
       * sum_(t>R0) (2t+1)^8 exp(-(gamma-beta)*t).
```

The corrected source now states this inequality. Its tail tends to zero
uniformly for fixed `0<beta<gamma`; the extra endpoint factor is harmless
to that conclusion. Reverse paths need not coincide. Pairing transpose
atoms, if a future consumer needs symmetric atoms, changes only fixed
constants and must still preserve endpoint readers.

These paths declare spatial supports for frozen matrix atoms. They do not
prove locality under variation of a coarse field or source-dependent
covariance. Full action-vertex syntactic supports are separately retained;
the construction never substitutes a covariance path for those readers.

## 5. Complete local normalizers and bounded remainder vertices

On the fixed smooth chart, all r_c are at least 1/2. The supplied bounds
`|h^(j)(t)|<=K_j*(1+t)^(-j)`, for j through three, make the chain-rule
coefficients

```
(kappa*u)^j * h^(j)(kappa*u*r_c)
```

uniformly bounded: their absolute values are at most `K_j*r_c^(-j)`.
Every derivative of r_c needed here is also bounded on that fixed chart.
This explicitly prevents a spurious u^3 cost for the kernel normalizers.
The leading kernel and plaquette terms cost O(u), and the smooth Haar term
costs O(1), giving the full local third-derivative bound (12).

With bounded local arity, Taylor's integral remainder on the straight
reader segment is at most `K*u*sigma^3*p^3 = K*sigma*p^3`.
For every fixed finite exponent in `p=log(2+u)^a_exp`, this tends to zero.
The fixed gap, chart radius and derivative hypotheses therefore admit a
single sufficiently large u threshold independent of volume. The exponent
restriction `a_exp>5/2` is unnecessary for this supplier and does not
establish any later consumer's exponent condition.

The local Taylor polynomials sum to the full vacuum, zero linear term and
exact quadratic `x^T H_u x/2`. On each reader cube,
`|exp(-R_v)-1| <= exp(K*sigma*p^3)-1`. Extending this function by zero
off that cube preserves bounded measurability and the declared reader
superset, giving (14). It need not be differentiable across the cube
boundary. No smooth-cutoff derivative bound has been proved or used.

## 6. Restricted identity and remaining scope

Substitute `a=sigma*x` into the actual chart integral. The coordinate
Jacobian is sigma^q, and converting the quadratic Lebesgue integral to a
normalized Gaussian contributes `(2*pi)^(q/2)*(det H_u)^(-1/2)`.
The remaining constant is exactly `exp(-S_u(0))`. This reproduces (15)
with every vacuum term and both normalizer levels retained. At zero source
the separate normalized Haar orbit integrates to one.

The indicator of the global product cube is essential: the zero extension
of W_v does not represent the original action outside the cube. Equation
(15) is consequently an exact restricted identity, not a compact-law
identity or a conclusion about rough sectors.

This check establishes the specified finite-volume frozen suppliers, with
their stated uniform constants. It does not establish forest positivity,
density-derivative bounds, a convergent connected logarithm, source or
coarse-field covariance derivatives, noninvariant-source orbit reconstruction,
rough-sector gluing, full response decay, or a physical mass gap. Those
remain separate proof obligations. No numerical experiment or earlier
PASS label was used as a substitute for these derivations.
