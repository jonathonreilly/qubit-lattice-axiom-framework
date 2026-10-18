# Independent finite-time microscopic collision check

Disposition: the Cook/power-counting/scattering-normalization argument is sound. Its remaining analytic obligation is a differentiated threshold estimate for the finite-rank scattering matrix; an undifferentiated o(1) in the on-shell T formula alone does not supply that estimate. The finite-matrix route below closes that obligation if its regular-complement inverse is verified for the specified obstacle. This is a finite-time matched-state result, not an infinite-time scattering theorem for the full native Hamiltonian at fixed lambda.

## Fixed coefficient model and extension

Decoupling the finite removed core and assigning it kappa I with kappa above the free band makes the operator difference from K0 finite rank and bounded. The artificial core eigenstates are harmless for scattering on the continuum: wave operators act on the absolutely continuous channel, not on those isolated core states. Their presence must not be mistaken for extra physical native modes. The extension is a comparison device.

Use the free dispersion epsilon(p)=t|p|^2+O(|p|^4) near its unique relevant minimum. Normalize phi using the selected lattice Fourier measure, e.g. d^2p/(2pi)^2. A radial smooth phi compactly supported in 1<|u|<2 gives f_k(p)=k^(-1)phi(p/k) of unit norm (for sufficiently small support inside the Brillouin zone).

For each site in the fixed support of V,

    (exp(-i tau K0)f_k)(x)
       = k integral d^2u/(2pi)^2
             phi(u) exp[i k u.x-i tau epsilon(ku)].

For |tau|k^2 sufficiently large, the u-gradient of the phase has magnitude comparable to |tau|k^2 on this annulus. There is no stationary point: |u| stays away from zero, while x is bounded. Repeated integration by parts, combined with the trivial bound at shorter times, yields

    |local amplitude| <= C_N k (1+k^2|tau|)^(-N).

Thus the one-sided Cook remainder is bounded by

    C_N k^(-1)(1+Tk^2)^(1-N).

For T=k^(-3), N=5 this is O(k^3), as proposed. The argument is independent of the detailed finite support size except through constants.

## Outgoing packet: what must be proved

To use the same estimate for S f_k one needs uniformly bounded scaled C^N norms of k(Sf_k)(ku), with smooth annular support. Energy conservation preserves an annulus with comparable inner/outer radii; exact lattice isoenergy curves differ smoothly from circles by O(k^2). Smooth compact support remains away from its edges after using an energy-angular parametrization.

The scalar assertion

    T(E)=4pi t/[log(t/E)+4pi B+i pi+o(1)]

by itself is NOT a derivative estimate. One cannot differentiate an arbitrary o(1). A sufficient finite-rank proof is:

1. For the finitely many support displacements, establish the boundary-value Green expansion G_ij(E)=a log(E) + A_ij + E log(E) B_ij + ... with uniform bounds under (E d/dE)^r through the finite order needed, and the appropriate outgoing imaginary constant. This follows by isolating the quadratic minimum in the Fourier integral and Taylor-expanding its smooth amplitude; the complement is smooth. Fixed finite spatial support makes the constants uniform.
2. Separate the rank-one logarithmic vector from its finite-dimensional complement. Verify that the regular complement is invertible (the concrete finite-matrix form of the absence of an additional zero-energy resonance). Its Schur denominator has the known nonzero logarithmic leading coefficient and finite B.
3. Differentiate the inverse using the Schur formula. E=k^2 rho with rho in a compact positive interval turns E d/dE into a uniformly bounded rho derivative. The scalar inverse logarithm and all its scaled derivatives are bounded; residual E log^r(E) terms and their scaled derivatives vanish.
4. The plane-wave vectors on the finite support have uniformly bounded u derivatives. Combining them with the inverse gives the required scaled energy/angular derivative bounds for the on-shell kernel and then S f_k.

This supplies the needed finite-order symbol estimate without assuming that the whole native Hamiltonian is free. If the root's “no zero resonance” proof includes this regular-complement condition, the derivative step is closed by this finite-matrix argument. If it only proves a scalar threshold limit, the complement/derivative check should be retained explicitly as an obligation. A full statement with merely polylogarithmic derivative losses would also suffice: k^3 times any fixed power of log(1/k) is still negligible compared with 1/log(1/k).

With these bounds the two-sided finite collision approximates S f_k with O(k^3), or the harmless polylogarithmic variant. The incoming and outgoing Cook tails must both be included.

## Angular density and leading scattering signal

With Fourier measure d^2p/(2pi)^2, the quadratic two-dimensional density of states is 1/(4pi t). The constant angular channel therefore has

    S_0(E)=1-2pi i [1/(4pi t)] T(E)
          =[L(E)-i pi]/[L(E)+i pi]+o(1/L),

where L(E)=log(epsilon_star/E) includes the real scattering constant. This verifies the factor of two and pi. Inversion-even radial packets are suitable, but radiality, not merely evenness, is what makes the leading packet purely the constant angular channel. Higher angular corrections vanish in the threshold limit under the same finite-rank estimates.

Uniformly over the annular radial support,

    |S_0-1|=2pi/sqrt(L(E)^2+pi^2)
           =[2pi/log(1/k^2)] [1+o(1)].

Consequently a normalized radial packet satisfies

    ||(S-I)f_k||=[2pi/log(1/k^2)] [1+o(1)]
               =[4pi/log(1/lambda)] [1+o(1)]

when k=lambda^(1/4). This norm is a scattering-state difference, not a transition probability or emission rate. Its square has the corresponding squared-log scaling. To obtain the coefficient rather than only an upper bound, the uniform leading constant-angular amplitude and absence of other equally large channels must be included, as supplied by the regular finite-matrix expansion.

## Finite volume and microscopic scales

For k=lambda^(1/4), T=k^(-3)=lambda^(-3/4), R~lambda^(-1), one has Tk^2=k^(-1) and R/T->infinity. A scaled Schwartz incoming/outgoing packet has tail outside radius R/4 bounded by arbitrary powers of (kR)^(-1). After spatial truncation, finite-range coefficient-model propagation differs between the torus and the infinite lattice by a polynomial factor times exp[-mu(R/const-vT)], provided consistent periodization and normalization are used. These errors are superpolynomial in lambda after choosing the truncation order.

The stated microscopic norm comparison is

    O(lambda^2 T + R^2 lambda^(M-10) T)
      = O(lambda^(5/4) + lambda^(M-51/4)).

The arithmetic is correct. M>51/4 makes both vanish algebraically, hence o(1/log(1/lambda)); stronger inherited choices are acceptable. Constants must be uniform on the matched low-energy states, and common rest-energy/ground phases must be removed consistently.

Crucially, T here is the scaled coefficient-model time. If the physical energy scale is J lambda^10, the actual physical time is T/(J lambda^10). The condition R>>T is a coefficient-model locality comparison, NOT a microscopic Lieb-Robinson claim at that much longer physical time. The route is valid because the global finite-volume normal-form/Duhamel bound first controls the actual microscopic evolution on the matched states; only the coefficient dynamics is then compared with its infinite lattice. Applying the bare native LR speed directly at this physical time would not justify the proposed box size.

The construction does not show convergence to an actual-H infinite-volume S matrix at fixed lambda, nor does it identify an experimental preparation. It gives a possible controlled finite-time scattering signal for prepared, dressed model states under the stated uniform normal-form and threshold-symbol bounds.
