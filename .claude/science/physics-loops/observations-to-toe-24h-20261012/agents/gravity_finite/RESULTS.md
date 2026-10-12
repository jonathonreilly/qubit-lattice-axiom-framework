# Finite positive scalar check: numerical receipt

The construction and proofs are in `DERIVATION.md`; executable code is
`finite_check.py`; compact machine-readable evidence is
`CHECK_RECEIPT.json`. All calculations were independent of the parent
worker's finite-approximation code. Parameters here are dimensionless
mathematical examples, not fitted physical values.

The full receipt is at:

`/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012/gravity_measurements/finite/finite_results.json`

Reproduction from the campaign checkout:

```sh
python3 .claude/science/physics-loops/observations-to-toe-24h-20261012/agents/gravity_finite/finite_check.py
```

The checker pins all numerical-library thread counts to one, checks stop
markers and the deadline, and needs no network or parent implementation.
It ran in about one second with NumPy 2.4.1, SciPy 1.17.0, and mpmath
1.3.0. It checked 36 static windows, 90 noise points, three independent
generator/first-hitting identities, and the gamma low-frequency power
for `s=0.3,1,2.5`. Checked exact Gaussian moments had maximum relative
floating-point discrepancy `4.1e-14`.

## Accurate statics can coexist with a complete low-frequency gap

For `s=1`, `N=16`, and the entire interval `0 <= r/ell <= 1`, the
analytic uniform **relative** bounds are

* potential: less than `1.56e-13`;
* force: less than `1.87e-12`.

An independent 70-digit Jacobi diagonalization at the endpoint `r/ell=1`
gives relative errors `(Y-Y_N)/Y = 4.8244430494e-15` and
`(H-H_N)/H = -6.4050374548e-14`. The negative force error is expected:
its quadrature remainder does not have the potential's fixed sign.

The lightest mass is nevertheless
`mu_min ell = 0.08764941047892784036019809734`. For `a/ell=0.7`,

| `omega ell` | `ell j` continuum | `ell j_N` finite | Relative noise error |
|---:|---:|---:|---:|
| 0.01 | 1.98094531e-6 | 0 | 100% |
| 0.10 | 1.90037956e-4 | 2.51102751e-4 | 32.13% |
| 0.30 | 1.52874606e-3 | 1.43898405e-3 | 5.87% |
| 1.00 | 9.11519724e-3 | 8.25685053e-3 | 9.42% |
| 3.00 | 2.02788064e-3 | 1.77420821e-3 | 12.51% |

The refined CDF bound at `omega ell=1` is 11.86% relative, compared with
28.40% from the global CDF discrepancy and 9.42% actual error. In the
gap at `omega ell=.01`, the refined bound equals the actual error
exactly. Pointwise error is not monotonic in `N`: at `omega ell=.3`,
it is 1.29% for `N=64` and 4.93% for `N=128` because thresholds move.

## A concrete joint certificate

For `s=1`, `N=128`, choose the radial interval `0 <= r/ell <= 10`,
smearing `a/ell=.1`, and frequency band `4 <= omega ell <= 5`.
The analytic certificates give simultaneously:

| Response | Uniform relative error bound |
|---|---:|
| Static potential | less than `1.10e-16` |
| Static force | less than `7.88e-14` |
| Local noise | less than `0.0992` |

The static numbers refer to the exact Gauss-Laguerre masses and weights;
the double-precision scan itself has a roughly `1e-14` to `1e-13`
rounding floor, and does not resolve the smaller analytic bound.
`DERIVATION.md` supplies explicit mass/weight rounding corrections.
The noise certificate uses the computed CDF discrepancy
`delta_N=0.05941352667224` in the rigorous bound (12); printed numerical
evaluations are not interval enclosures of their final digits.

The lightest mass here is `mu_min ell=.01125138826368`. The same model
still has 100% relative noise error below that value. Thus the joint
certificate is expressly a finite-window statement.

## Independent identity checks

For `(s,N,t)=(.6,4,2)`, `(2.5,6,4)`, and `(1,1,.1)`, direct finite
Markov-generator exponentiation agrees with the Laguerre spectral sum.
The first-hitting convolution reproduces both potential and force errors
to better than `2e-13` absolute. In the second case the force error is
positive, while it is negative in the first and third cases. The signed
CDF integral reproduces the direct noise difference at all five table
frequencies. These checks exercise the normalization, the force
derivative, and both branches of the smearing variation bound.

A useful next calculation is to specify an actual radial window,
frequency band, Gaussian source width, and separate relative/absolute
noise tolerances. Reject candidate orders with `mu_min >= omega_lo`,
then evaluate the analytic static certificates and the CDF noise bound
for the surviving orders. This chooses a finite local candidate against
both readouts. A static-only choice of `N` cannot justify its noise
accuracy or a physical identification.
