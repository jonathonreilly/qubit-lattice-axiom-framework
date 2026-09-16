# Coupled free-vacuum resolvent densities remain infrared finite

**Author theorem proposal for a specified Gaussian/Weyl reference.** No independent review or audit. This is a first-coefficient bound, not a convergent perturbation series or a fixed-coupling phase theorem.

[BLOCK03](BLOCK03_INFRARED_PROFILE_OF_THE_REFERENCE_VERTEX.md) showed that a bare inverse photon energy applied to a local reference vertex has a logarithmic norm divergence. The current acting on a filled Weyl sea also creates a particle-hole pair. This note retains that energy and proves a different, finite per-volume statement.

## 1. Supplied reference and exact quantities

Let V=L^3, L>=3, with periodic spatial momenta. The Maxwell reference has two transverse polarizations at every k!=0 and frequency

    omega(k)=|s(k)|, s_i(k)=2sin(k_i/2).

Its exact zero mode is omitted from this specified reference. Take two conjugate free Wilson sectors with opposite charges. The plus symbol is

    h(p)=sin(px)sigma1+sin(py)sigma2
          +(5/2-cos(px)-cos(py)-cos(pz))sigma3,
    epsilon(p)=|h_vector(p)|.

The minus symbol is h(-p)*, with entrywise complex conjugation. Fill the negative band. At any exact zero-energy momentum choose a rank-one occupied projector in its two-dimensional zero eigenspace, and the conjugate choice for the opposite species. This specifies a translation-invariant Slater reference Omega_m with equal particle numbers. It does not assert a unique free ground state; other zero-mode occupation patterns are outside the present finite-state specification.

Let Omega be this sea times the photon Fock vacuum, and let H0 be the sum of the nonnegative photon and particle-hole energies relative to Omega. H1 is the linear current coupling obtained from the leading vertex of BLOCK02 with eta=1, as appropriate to the coefficient linear in g. It is also independently defined by the ordinary linear expansion of the supplied Peierls hopping in a transverse Gaussian link field.

The following finite-volume quantities are unambiguous even when the fermion sea has zero modes:

    N_L=(1/V)||H0^(-1) H1 Omega||^2,
    D_L=(1/V)<H1 Omega,H0^(-1)H1 Omega>.              (1)

H1 Omega contains one nonzero-momentum photon, so the inverse on this vector has a strictly positive finite-volume denominator. No inverse is applied to a zero-photon ground state. We propose and prove below:

* N_L and D_L are bounded uniformly in L.
* They converge to finite six-dimensional momentum integrals as L grows.
* The limiting integrals do not depend on the allowed rank-one choices at exact Weyl nodes.
* The contribution to N_L from 0<omega(k)<=lambda satisfies

      N_L(omega<=lambda)
        <=C lambda^2+C[1+log_+(L lambda)]/V,         (2)

  for 0<lambda<=1, with a constant independent of L and those node choices.

The constants may depend on the fixed Wilson symbol. No numerical value for a uniform constant is inferred from the runner. The quantities are positive resolvent forms of the reference interaction. Calling -g^2 D_L an exchange contribution in formal perturbation theory does not include the separate Coulomb, diamagnetic and compact terms at order g^2.

## 2. Current convention and Ward identity

The directional hopping matrices are

    T_x=(-sigma3-i sigma1)/2,
    T_y=(-sigma3-i sigma2)/2, T_z=-sigma3/2.

With midpoint link phases, the plus current matrix taking momentum p to p+k is

    j_i(p,k)=-i[T_i exp(i[p_i+k_i/2])
                    -T_i^dagger exp(-i[p_i+k_i/2])],       (3)

Here the dagger is the Hermitian adjoint. Equivalently,

    j_x=-cos(px+kx/2)sigma1-sin(px+kx/2)sigma3,
    j_y=-cos(py+ky/2)sigma2-sin(py+ky/2)sigma3,
    j_z=-sin(pz+kz/2)sigma3.

Thus ||j_x||=||j_y||=1 and ||j_z||<=1. Elementary trigonometric subtraction gives the exact lattice identity

    sum_i s_i(k) j_i(p,k)=h(p)-h(p+k).               (4)

This verifies the link midpoint and charge-current conventions. No continuum derivative has replaced the finite difference.

Let P_T(k)=I-s(k)s(k)^T/omega(k)^2. For chosen band eigenvectors put

    M_i(p,k)=<u_+(p+k),j_i(p,k)u_-(p)>,
    W(p,k)=M(p,k)* P_T(k) M(p,k).

Then 0<=W<=sum_i||j_i||^2<=3. For numerical evaluation a phase-free equivalent is useful. Write h=epsilon n.sigma, j_i=b_i.sigma. Then

    W=(1/2)sum_ij P_T,ij [(1+n.n')b_i.b_j
                           -(n.b_i)(n'.b_j)
                           -(n.b_j)(n'.b_i)],       (5)

where n'=n(p+k). At a node the chosen rank-one projector defines n there. The imaginary Pauli triple products cancel against the real symmetric P_T.

For the conjugate charge species, n is transformed by diag(-1,1,1), and the current coefficient vectors by minus that same orthogonal matrix. Formula(5) is unchanged for conjugate node choices. The two species create orthogonal particle-hole states, so their squared contributions add.

## 3. Fock calculation and normalization

Normalize each Fourier mode by V^(-1/2). A photon creation mode has coefficient 1/sqrt(2omega), and its coupling to a momentum-changing matter bilinear therefore has coefficient 1/sqrt(2V omega). The current carrying momentum k is accompanied by a photon at -k, so total momentum is conserved; omega(-k)=omega(k). Acting on the sea, only occupied-to-unoccupied transfers survive. The excitation energy is

    Delta(p,k)=omega(k)+epsilon(p)+epsilon(p+k).

Distinct photon modes and particle-hole states are orthogonal. Fermionic ordering signs have modulus one and are retained in the direct CAR check. Consequently, after summing the two conjugate species,

    N_L=(1/V^2)sum_(k!=0,p) W(p,k)/[omega(k)Delta(p,k)^2],
    D_L=(1/V^2)sum_(k!=0,p) W(p,k)/[omega(k)Delta(p,k)]. (6)

The single-species formula has an additional factor1/2. Equation(6) is the complete first linear-current reference expression, not a loop-counting ansatz. Current matrix elements within exact fermion zero modes cause no zero denominator because k!=0.

## 4. Weyl phase space gives a uniform bound

The zero set of epsilon is exactly

    Z={(0,0,pi/3),(0,0,-pi/3)}.

Indeed sin px=sin py=0, and any pi choice in x or y leaves a nonzero third component. At the two zeros the linear coefficient matrix has singular values 1,1,sqrt(3)/2. Taylor's theorem near those points and compactness away from them yield a constant c>0 with

    epsilon(p)>=c dist(p,Z)

on the momentum torus. Hence elementary counting of grid points in two balls gives

    (1/V)# {p:epsilon(p)<=r} <=C r^3+C/V, 0<=r<=1.   (7)

The C/V term retains exact or near grid nodes. Replacing it by a finite-volume gap would be incorrect.

Let S_L(w)=(1/V)sum_p(w+epsilon(p))^(-2). Integrate the distribution function in (7), and bound the remaining compact energy interval by one. The identity with the derivative 2(w+r)^(-3) gives

    S_L(w)<=C+C/(V w^2), w>0.                        (8)

The possible atom at r=0 is included in the integral and produces the second term. Similarly

    (1/V)sum_p(w+epsilon(p))^(-1)<=C+C/(Vw).          (9)

Since Delta>=omega+epsilon(p) and W<=3, equation(6) implies

    N_L <=C[(1/V)sum_(k!=0)omega^(-1)
              +(1/V^2)sum_(k!=0)omega^(-3)],
    D_L <=C[(1/V)sum_(k!=0)omega^(-1)
              +(1/V^2)sum_(k!=0)omega^(-2)].         (10)

The cubic photon dispersion has a single linear zero. Integer shell counting gives uniformly bounded normalized sums at powers1 and2, and an O(1+log L) normalized sum at power3. Thus the last term in the first line is O(log L/V), not a logarithmic divergence of N_L. This proves the uniform bounds.

Restricting the same photon shell sums to omega<=lambda gives a C lambda^2 bound at power1 and C[1+log_+(L lambda)] at power3. Equation(2) follows. The smallest nonzero photon frequency is at least4/L; if the restricted set is empty the assertion is immediate.

## 5. Infinite-volume limit and node-choice independence

Remove neighborhoods of k=0, p in Z, and p+k in Z. On the remaining compact set the summands in(6) are continuous, bounded, periodic matrix functions, so the Riemann sums converge to their integrals with measures dk dp/(2pi)^6.

The omitted photon region is bounded by(2), uniformly after taking limsup in volume, and tends to zero with lambda. For a fermion-node neighborhood epsilon(p)<=delta, the truncated version of the distribution-function estimate gives

    (1/V)sum_(epsilon(p)<=delta)(w+epsilon(p))^(-2)
       <=C delta+C/(Vw^2).

This follows from its endpoint term at delta and the integral of (7); both the continuum terms are O(delta). Combining with the photon sums controls its contribution by C delta+C log L/V. The p+k neighborhood has the same bound after translating the momentum index. The first-power denominator is no worse on this bounded reference spectrum: 1/Delta<=Delta_max/Delta^2. Therefore D_L has the same uniform cutoff argument.

These estimates prove convergence to finite integrals by removing the cutoffs after the volume limit. Changing a rank-one occupation direction at an exact node alters only terms with p or p+k at one of finitely many momenta. Their total difference is bounded by C(1+log L)/V for N_L and tends to zero; the first-power expression is no worse. Finite-volume node choices remain real ambiguities and are not declared equal before this limit.

## 6. Interpretation and remaining fixed-coupling problem

The bare photon inverse in BLOCK03 and the coupled vacuum denominator here are different operators applied to different states. The photon inverse alone has a logarithmic norm problem. The occupied-to-unoccupied fermion phase space makes the first coupled vacuum correction per volume finite. Neither result overturns the other.

This establishes a useful first step for a ground-state expansion around the globally Gauss-constrained reference. It does not show convergence in perturbative order, uniform analyticity at nonzero g, convergence of a global infinite-volume state vector, a massless pole, infrared charge flow, or control of compact defects. The total first-order correction norm is extensive; finite density is not a global Hilbert-space convergence claim. The next nonperturbative argument must control current correlations and all relevant photon/matter sectors, rather than replace their denominators by a bare photon inverse.

## Personal evidence

The runner first constructs the actual real-space Wilson hopping/current matrices on L=3, rotates them into the band basis, and acts with CAR bilinears on the filled 54-mode reference. Its37,908 one-photon/particle-hole basis entries reproduce the momentum expression; the difference in paired norm density is about8.7e-18. This checks normalization, momentum routing and fermion signs by a distinct implementation.

It then evaluates the finite reference expressions for L=4,6,8,10,12, including exact Weyl nodes at L=6 and12. The Ward residual is near machine precision. These finite sums are diagnostics; the all-volume bound and convergence follow from the written phase-space proof. The printed cutoff at frequency1 is a floating comparison and is not used as an exact shell-count certificate or to fit a uniform constant. No actual compact three-dimensional ground state is solved here.
