# Beta=6 Plaquette Moment-Positivity No-Go Note

**Date:** 2026-05-30
**Type:** no_go
**Status:** exact no-go proposal for one resummation subfamily. Audit and
effective status are ledger-derived, not source-prose claims.
**Runner:** [`scripts/frontier_beta6_cumulant_moment_positivity.py`](../scripts/frontier_beta6_cumulant_moment_positivity.py)

## Scope

Let

```text
Delta(beta) = P_full(beta) - P_1plaq(beta)
            = sum_{n>=5} d_n beta^n.
```

This note tests only the positive-measure / real-axis continuation family for
`Delta(beta)`: representations whose coefficients are moments of a positive
real-axis measure. It does not claim `P(6)`, does not close beta=6, and does
not decide any non-Stieltjes continuation family.

The exact inputs are the current source-note values

```text
d_5 = 1/472392
d_6 = 7/5668704
d_7 = 5/17006112
```

from the beta6 connected-coefficient lane. The current `d_8` and `d_9` results
give additional diagnostics for d-log-Pade, but they are not needed for this
three-coefficient positivity test.

## Claim

The window `{d_5, d_6, d_7}` is not a Hamburger moment window, hence not a
Stieltjes moment window. Therefore `Delta(beta)` is not the
Laplace/Stieltjes transform of a positive measure on the real axis.

The proof is the exact 2 by 2 Hankel minor

```text
det [[d_5, d_6],
     [d_6, d_7]]
  = d_5 d_7 - d_6^2
  = -29 / 32134205039616
  < 0.
```

Every Hamburger moment sequence has positive-semidefinite Hankel matrices. A
single negative principal minor is enough to rule out that positive-measure
class. Stieltjes positivity is stronger, so it fails as well.

The same sign has an integer witness. With `m_n = d_n 18^n`,

```text
m_5 = 4,    m_6 = 42,    m_7 = 180,
m_5 m_7 - m_6^2 = 4*180 - 42^2 = -1044.
```

The weights are geometric, so this rescaling preserves the Hankel-minor sign:
`18^5 18^7 = (18^6)^2`.

## Boundary

This no-go forecloses only the positive-measure / real-axis branch-cut family.
It does not refute a general non-Stieltjes continuation. In particular, the
current beta6 map already records that exact `d_8` and `d_9` sharpen the
d-log-Pade route separately: the simplest single-complex-pair sign prediction
fails at `d_8`, and the first activated `[1/1]` d-log-Pade gets the `d_9` sign
but not the magnitude. Those are separate diagnostics, not premises of this
Hankel-minor result.

## No-Go Discipline Gate

**Status:** PASS for the narrow positive-measure / real-axis foreclosure only.

### N1 - Alternative Routes

| route | what it would attempt | why it fails for this scoped no-go | marker |
|---|---|---|---|
| Direct positive measure | Find `mu >= 0` with `d_k = integral t^k d mu(t)` for the displayed window. | Hamburger positivity requires the displayed Hankel minor to be nonnegative; it is strictly negative. | ATTEMPTED |
| Integer rescaling | Clear the `18^n` denominators and hope the sign changes. | The rescaling is geometric, so the minor sign is preserved exactly; the integer witness is `-1044`. | ATTEMPTED |
| Stieltjes half-line measure | Put the measure on `[0, infinity)` instead of the whole real axis. | Stieltjes positivity implies Hamburger positivity; Hamburger already fails. | ATTEMPTED |
| Alternating-sign convention | Test `(-1)^n d_n` instead. | The same 2 by 2 determinant keeps the same sign under that alternating rescaling. | ATTEMPTED |
| Non-Stieltjes continuation | Use a complex or multi-singularity continuation not representable by a positive real-axis measure. | This is out of scope and remains a separate open diagnostic; the negative minor is compatible with non-Stieltjes behavior. | OUT OF SCOPE |

### N2 - Wall Independence

There is one wall: `d_5 d_7 - d_6^2 < 0`. The integer witness is the same
wall after a sign-preserving rescaling, not a second condition.

### N3 - Hidden-Wall Scan

The load-bearing inputs are exactly the three rational coefficients, the
standard Hamburger necessary condition, and the inclusion of Stieltjes
positivity inside Hamburger positivity. No beta=6 value, Monte Carlo
comparator, fitted exponent, or new premise is used.

### N4 - Residual Matching

The residual is the positive-measure / real-axis continuation family. The
geometric-ratio and d-log-Pade diagnostics attack other residuals and are cited
only to place this result in the beta6 map.

### N5 - Rhetoric Audit

"No-go" means only "no positive real-axis measure can reproduce this
coefficient window." It does not mean no analytic continuation, no
resummation, or no beta=6 route.

### N6 - Partial-Closure Path Scan

The route remains open for non-Stieltjes analytic classes, higher-order
coefficient organization, and direct spatial-environment evaluation. None of
those paths is relabeled as an axiom or primitive by this note.

### N7 - Steelman

The strongest objection is that a non-Stieltjes continuation could still be the
right beta6 analytic class. That objection is correct and is exactly why the
claim is limited to positive real-axis measures.

### N8 - Cross-Cycle Echo

The beta6 lane has repeatedly overread narrow falsifiers as route closures.
This note avoids that pattern by keeping the surviving non-Stieltjes route
separate from the positive-measure family it actually rules out.
