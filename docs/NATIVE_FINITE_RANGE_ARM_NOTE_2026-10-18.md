# Finite-range corrections to the native composite arm

**Status:** bounded-support.
**Primary runner:** [scripts/native_finite_range_arm.py](../scripts/native_finite_range_arm.py)

The [corrected fast-arm calculation](NATIVE_CORRECTED_FAST_STRIP_NOTE_2026-10-18.md)
controlled a quadratic kinetic polynomial. This block extends the local
nonreal-strip bound to every fixed-degree near-nearest-neighbor polynomial.
It also derives the affine-potential/finite-range form of the compressed
native long arm, rather than choosing that form as an extra interaction.

For T=S+S*, consider p_lambda(T)+f(n+1)+a+F_lambda, with
p_lambda(t)=-2t+O(lambda), fixed degree, and a fixed-supported Hermitian
endpoint correction F_lambda=O(lambda). For z=x-i eta, x-a=O(lambda), and
eta/f in a fixed positive compact interval, endpoint Green entries are
bounded and the first diagonal imaginary part has a positive lower bound.
Small lambda is required uniformly in small f; lambda/f need not be small.

The [proof](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/GENERAL_FINITE_RANGE_ARM_PROOF.md)
uses a smooth extension of the kinetic polynomial, Fourier Duhamel calculus,
a positive congruence to a nearest-neighbor Jacobi operator, and polynomially
weighted source localization. The unbounded potential is treated on its
natural domain. The comparison error is O(lambda f), not O(lambda) divided
by the tiny spectral imaginary part. The transformed endpoint source tends
to delta_1/sqrt(2), which is included in the positive-bound normalization.

Independent [algebra](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_GENERAL_ARM_ALGEBRA.md)
and [boundary](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_GENERAL_ARM_BOUNDARY.md)
checks pass. This is an ordinary self-adjoint arm resolvent statement,
not an outgoing-host continuation or a resonance-location theorem.

## Why the native long arm has this form

At fixed perturbative order, connected local coefficients have bounded
support. For a sufficiently long pair-column interval, such a term cannot
move both ends or change the transverse column pair. Interior diagonal
contributions count linearly with length; endpoint contributions are
constant. Endpoint moves have translation-independent amplitudes and finite
range. At zero longitudinal center-of-mass momentum this gives a real
Toeplitz hopping plus affine diagonal, modulo a finite endpoint block.
Every such hopping is a polynomial in T modulo endpoint corrections.

The [structural derivation](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/NATIVE_FINITE_RANGE_ARM_STRUCTURE.md)
and [independent check](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_NATIVE_LONGARM.md)
retain the supplied background, translation symmetry and plane-parity
sector explicitly. In the prior coefficient gauge, leading hopping is -2T
and f=lambda^3/16+O(lambda^4)>0 in fast units at fixed order at least four.
A [direct local tension argument](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/DIRECT_LOCAL_TENSION_PROOF.md)
now gives the same leading coefficient in the [actual local normal form](NATIVE_LOCAL_NORMALFORM_NOTE_2026-10-18.md):
a deep interior cluster has zero local walls; its squarefree plaquette chain
has no intermediate return and coefficient -P/128. Every other four-edge
diagonal graph is a repeated-edge pattern whose column-sign factors cancel.
Four odd-flux plaquettes per slice give the tension lambda^4 Jz/16.
The [independent check](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_DIRECT_LOCAL_TENSION.md)
uses a frozen ordered exterior to identify the local diagonal coefficient
with its one-dimensional zero-wall eigenvalue coefficient. This closes the
leading-tension transfer condition only. Higher matrices and source
identification still require a consistent gauge.

## Computation and limits

The runner checks a chosen cubic polynomial at lambda=.2,.1,.05, using
24,000, 192,000 and 1,536,000 arm sites and a 10% larger cutoff comparison.
It also checks polynomial-versus-Toeplitz boundary localization. These are
mathematical controls, not derived values for a new native cubic interaction.
The analytic argument carries the uniform claim.

Compression is not invariance. Short-interval host channels, other column
separations, complete effective coefficients, higher-order gauge alignment and physical
state/readout identification remain open. This removes a restricted
long-arm kinetic-form obstacle; it does not establish a full microscopic
scalar pole, a light mass or cosmological coupling. All inputs are exposed
model-development choices; no observational test is claimed.
