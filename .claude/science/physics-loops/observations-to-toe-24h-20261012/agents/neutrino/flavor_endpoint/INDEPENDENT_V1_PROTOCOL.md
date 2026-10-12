# Independent endpoint-flavor calculation, V1

Frozen before the independent numerical calculation, 2026-10-12. This is a
conditional model check, not an axiom change, retained result or blind forecast.
Root's `gravity/FLAVOR_ENDPOINT_PROTOCOL.md` was read to match its exact mass-map
convention. Root's code and numerical outputs have not been read. Public target
values approximately motivated this line and JUNO/solar/accelerator summaries
have already been seen in source searches. No blind-prediction claim is allowed.

Supplied physical assumptions: three weak flavors are coordinates 0,1,2 of the
N=3 Laguerre Jacobi truncation, in electron/muon/tau order; its ordered
eigenvectors are the mixing matrix with normal ordering; ordinary unitary
three-flavor propagation and, for comparison to matter experiments, the usual
charged-current matter potential. A common scalar spectral shape s is an
additional physical identification. Neutrino and scalar dimensional scales
remain independent. No derivation of these assumptions is claimed.

Independent algebra:

```
J = [[s, -sqrt(s), 0],
     [-sqrt(s), s+2, -sqrt(2(s+1))],
     [0, -sqrt(2(s+1)), s+4]]
P(x) = x^3 - 3(s+2)x^2 + 3(s+1)(s+2)x - s(s+1)(s+2)
v(x) = [1, (s-x)/sqrt(s),
        (x^2-2(s+1)x+s(s+1))/sqrt(2s(s+1))]
w(x) = 1 / dot(v(x),v(x))
```

The eigenvalues x1<x2<x3 are positive for s>0, and U[:,i]=sqrt(wi)v(xi),
up to harmless row/column sign conventions. Thus sin²theta13=w3,
sin²theta12=w2/(1-w3), and sin²theta23=w3(s-x3)²/[s(1-w3)].
The real matrix gives zero Jarlskog invariant; the rephasing-invariant cosine
of the standard Dirac phase will be computed as an algebra check, not fitted.

Calibration only: Daya Bay arXiv:2211.14988v1 published standard-family fit
sin²(2theta13)=0.0851±0.0024, s in [0.01,10]. Its conditioned solar-sector
assumptions and the smaller sin²theta13 branch must be retained. Propagate
central ±1 and ±1.96 quoted standard errors by monotone inversion; these are
diagnostic bands, not a full confidence region of this conditional model.
Verify monotonicity numerically across the declared interval and verify the
analytical eigenvectors/polynomial against a symmetric eigensolver.

V1 outputs only: sin²theta12, sin²theta23, real mixing matrix, eigenvalues,
and r31=(x2^p-x1^p)/(x3^p-x1^p), r32=r31/(1-r31), for the fixed physical
maps m_i²=m0²+A*x_i^p with p=1,2 and A>0. The common offset is oscillation
invisible. No theta12/theta23/gap target is used to choose s or p.

Comparison rule: first retain the V1 output unchanged. Compare diagnostic
calibration bands with primary-experiment reported ranges, preserving normal
ordering and whether a range is a profile interval or marginalized Bayesian
credible interval. A clear nonoverlap is a summary-level incompatibility
under the supplied assumptions, not a likelihood-ratio significance, joint
exclusion level or independent combination. Do not multiply reactor-conditioned
summaries or infer correlations from one-dimensional errors. For the gap ratio,
use a explicitly labelled rectangle of published input ranges if covariance
or common nuisance priors are unavailable; that rectangle is not a joint CI.

Later candidates (variable p, other monotone positive mass maps, boundary
defect) require a separate protocol after V1 is frozen. Eigenvalue-only maps
cannot alter eigenvectors. A boundary defect would change the scalar spectral
measure as well and cannot silently reuse the gamma static/noise law.
