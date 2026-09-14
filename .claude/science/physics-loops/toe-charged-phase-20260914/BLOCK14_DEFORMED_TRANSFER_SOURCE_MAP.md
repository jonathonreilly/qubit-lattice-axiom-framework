# Deformed small-clock photon actions: exact transfer-source distinctions

Author working source check, not an independent audit or a phase theorem.
Read arXiv2505.00079v2 (11 pages of extracted text including supplement;
figure curves not independently digitized or statistically reanalyzed).
The work is numerical evidence on isotropic four-dimensional Euclidean
tori. Its N=7 example uses the standard Wilson action. Its N=4 examples
add a second plaquette harmonic, and its N=3 examples add a monopole-cube
penalty. These are different models, not established instances of the
continuous-time nearest-clock Hamiltonian used in PR8120/8121.

## 1. N=4 link kernel: exact positivity region

For temporal weight

    w(r)=exp[beta cos(pi r/2)+beta2 cos(pi r)], r in Z4,

define Fourier coefficients lambda_q=(1/4)sum_r w(r)i^(-qr).
They are exactly

    lambda_0=(exp(beta2)cosh(beta)+exp(-beta2))/2,
    lambda_1=lambda_3=exp(beta2)sinh(beta)/2,
    lambda_2=(exp(beta2)cosh(beta)-exp(-beta2))/2.

For beta>0, positivity of all four coefficients is equivalent to
exp(2 beta2)cosh(beta)>1 (with equality yielding a zero mode). At the
paper's plotted correlator parameters beta=1.514, beta2=-0.393, the four
coefficients are approximately 1.544820666, 0.729848824, 0.063402277,
0.729848824 and the convolution is positive definite. At the separate
parameter pair beta=1.4, beta2=-0.407 within its displayed scan rectangle,
lambda_2 is negative, approximately -0.035285519. No claim is made here
that this second pair is in the paper's photon phase.

Gauss projection does not generally repair that negative mode. On the
open two-plaquette strip, the closed mod4 current F^T(1,3) has six outer
edges with q=1 or3 and the shared edge with q=2. Its physical temporal
convolution eigenvalue is lambda_1^6 lambda_2, up to a common positive
normalization factor. It is negative whenever lambda_2<0. At the exact
illustrative parameters beta=log3, beta2=-log2,

    (lambda_0,lambda_1,lambda_2,lambda_3)=(17/12,1/3,-7/12,1/3),
    lambda_1^6 lambda_2=-7/8748.

All coordinate Boltzmann weights remain strictly positive. This is a
finite physical-sector counterexample to inferring positive transfer
operators merely from positive local statistical weights. It is not a
claim that the paper's specific positive-kernel photon candidate fails.

## 2. Positive transfer need not embed in a positive history semigroup

When all lambda_q>0, normalize by lambda_0 and set E_q=-log(lambda_q/lambda_0).
The one-link logarithmic generator is

    h=t1(2-X-X*)+t2(2-X^2-X*^2),
    t1=E_2/4, t2=(2E_1-E_2)/8.

A useful exact identity is

    lambda_0 lambda_2-lambda_1^2=(exp(2 beta2)-exp(-2 beta2))/4.

Thus for beta2<0 within the positive-kernel region, E_2>2E_1 and t2<0.
The coordinate off-diagonal matrix element h_(a,a+2)=-2t2 is positive.
Consequently exp(-s h) has a negative corresponding matrix element for
sufficiently small positive s. The positive one-step kernel is not embedded
in an entrywise-positive continuous-time semigroup in this coordinate basis.
This does NOT invalidate h as a Hermitian quantum generator.

At beta=1.514, beta2=-0.393, E_1=0.7498256866, E_2=3.1931633388,
t1=0.7982908347 and t2=-0.2116889957. The positive-history/Perron-Frobenius
assumption behind section12 of BLOCK14_DERIVATION.md is therefore not
supplied by taking this link logarithm. The full transfer with spatial
plaquette factors also requires a locality analysis of its logarithm;
this one-link calculation does not establish that full logarithm.

## 3. N=3 monopole penalty: finite positive samples, global question open

For a one-time-step prism over the open two-plaquette strip, label spatial
fluxes b,b' in Z3^2 and link differences delta in Z3^7. If F is the oriented
face-edge matrix and principal(r) is in {-1,0,1}, the temporal-gauge,
Gauss-projected kernel, omitting positive diagonal spatial factors, is

    K(b,b')=sum_(F delta=b'-b mod3)
      exp[beta sum_ell cos(2pi delta_ell/3)]
      exp[-mu sum_p ((principal(b'_p)-principal(b_p)
                      -(F principal(delta))_p)/3)^2].

The numerator in the monopole term is divisible by3. This is the integer
Bianchi mismatch on each temporal cube. All 2187 link-difference vectors
are enumerated. The 9-by-9 kernel is symmetric and has positive sampled
minimum eigenvalues for beta=0.1,0.265,0.5114,1,2 and mu=0,0.3,1,3,10.
At beta=0.5114, mu=1, the smallest-to-largest ratio is about0.000567409.

These finite samples are compatible with positive transfer in that fixture.
They do not prove reflection positivity on arbitrary three-dimensional
spatial complexes, a continuous-time local Hamiltonian correspondence, or
a photon phase. No negative result was obtained for this N=3 fixture, and
its positive output is preserved as such.

## Implication for the next campaign

The new small-clock numerical results motivate alternative action families.
They do not discharge the current same-Hamiltonian infrared obligation.
If one pursues those alternatives, first establish the exact physical
transfer and its generator/locality/positivity properties. Alternatively,
continue the existing larger-N clock Hamiltonian with the full quantum
loop and transition-norm bounds of BLOCK14_DERIVATION.md. None of these
source distinctions is a contradiction of the TOE axioms.
