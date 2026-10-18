# Native conserved scalar fluctuation route

Supplied cubic compass H=-sum_(r,a) Ja sigma_r^a sigma_(r+ea)^a, one physical qubit/site, periodic large lattice. State rho=I/2^V is explicitly supplied infinite-temperature ensemble, not derived cosmological state. Use normalized HS trace. Define h_b=-Ja Pauli_b and E_q=V^-1/2 sum_b exp(-iq r_b)h_b at bond centers. At q=0 E0=H/sqrtV. Every h_b commutes with exact plane symmetries, hence neutral. Equal Ja gives cubic scalar density (q transforms geometrically).

Moment m0=<E_q† E_q>=sum_a Ja² from distinctPauli orthogonality. For unordered incident perpendicular bonds b,c,
 [H,E_q]=V^-1/2 sum_(b,c)(exp(-iq r_c)-exp(-iq r_b))[h_b,h_c].
Their commutators are unique three-site Pauli strings of norm2 JaJb. Same-axis commute. For lattice lengths>=5 avoid shortwrap aliases. Thus
 m2=||[H,E_q]||HS²=32 sum_(a<b) Ja²Jb²[1-cos(qa/2)cos(qb/2)].
Smallq m2=4sum_(a<b)Ja²Jb²(qa²+qb²)+O(q4); isotropic m2/m0=(8/3)J²|q|²+O(q4).

The exact positive spectral measure mu_q(omega)=2^-V sum_mn |<m|E_q|n>|² delta(omega-(Em-En)) has massm0 and secondmomentm2. Chebyshev gives mu_q(|omega|>Omega)<=m2/Omega². For Omega=|q|^alpha J with0<alpha<1, normalized weightoutside tends0. This is a genuine low-frequency neutral collective fluctuation without adding a field or interaction; it does NOT imply a delta pole, relativistic dispersion, diffusion coefficient, zero-temperature excitation, or a cosmological state. At beta0 the usual retarded commutator expectation vanishes, so this is fluctuation spectral weight, not nonzero susceptibility.

Use existing native cubic scalar Q=sum_a[Ha,[H,Ha]] at isotropicJ. Earlier exactPauli result Q=-32J²H+Q4 (fourspin strings). At beta0, <Q H>/<H²>=-32J² exactly. Hence Q/sqrtV=-32J² E0+Q4/sqrtV, HSorthogonal Q4 toH, and the conserved spectral weight in Q is at least(32J²)² <H²>/V=3072J6. This is a derived coupling of a specified scalar diagnostic to the conserved collective energy component, not physical detector coupling. Need exactQ norm and longwavelengthdensity definition to boundfraction/derive q-dependentprojection, plus finite-volume checks.

Original Cz=sum_r Zr Zr+2ez has beta0 overlap withH zero. HighT expansion: <Cz>=V beta² Jz²+O(beta³) (eachlength2zpath appears twice inH² and1/2 cancels), so cov(Cz,H)=-2V beta Jz²+O(beta²), varH=V sumJa²+O(beta). This derives g_C(beta)=-2beta Jz²/sumJa²+O(beta²) only conditional on chosenGibbsstate. No beta or environment selection. Distance2readout is directional, not automatically cubic scalar. Finite beta locality/cluster convergence would be needed for uniform thermodynamic remainder.

## Finite momentum source transfer
Define Ha_q by the same bond-center phases restricted to axis a and Q_q=sum_a[Ha,[H,Ha_q]]. This has Q_0=Q/sqrtV and is a local Fourier density, with adjoint Q_-q. Direct doublecommutator on the repeated outer/inner a bond gives its b-bond component -16 sum_(a!=b)Ja² cos(qa/2)cos(qb/2) h_b. Thus
 g(q)=<E_q,Q_q>/m0=-32 sum_(a<b)Ja²Jb² cos(qa/2)cos(qb/2)/sumJa².
At isotropy q0, Q variance/site5376J6 from3072J6 two-spin plus2304J6 four-spin. Fourspin count12V same-end and24V cross-end strings eachamplitude8J3. Conserved fraction4/7.

Let P_low be spectral projection of the selfadjoint Liouvillian [H,.] in the HS operator Hilbert space to |omega|<=Omega. Then
 ||P_low Q_q|| >= max(0, |<E_q,Q_q>|/sqrt(m0) - sqrt(m2/(m0 Omega²))*||Q_q||).
Proof: split overlap into low/high, bound high by||P_high E||||Q|| and low bysqrt(m0)||P_low Q||. For Omega=J|q|^alpha,0<alpha<1, higherror→0. Locality makes||Q_q||² a finite trigonometric polynomial continuous atq0. Therefore liminf lowfraction>=4/7. Orthogonal remainder is not assumed unable to cancel atfiniteq; this inequality handles cancellation.

## Why this does not yet deliver gravity
The state is infinite-temperature, where trace[A(t),B]=0 identically. Fluctuation weight alone is not a force response. At a pure energy eigenstate energy variance atq0 iszero, so the finite-density fluctuation argument cannot be transplanted to the vacuum. Finite-temperature equilibrium gives different state-dependent response, requiring explicit state and thermodynamic control. No pole width, propagation speed, or inverse-square static response is derived. These are constraints on this proposed route, not a no-go against all native scalar modes.


## Exact finite-q norm certificate
At isotropic J1, contract identical Pauli strings while keeping their inner-bond Fourier centers. The exact integer numerator per volume has55 displacement terms: doubled displacement0 coefficient1536; permutations of(±2,0,0) coefficient256; permutations of(±2,±2,0) coefficient64; permutations of(±1,±1,0) coefficient64; permutations of(±2,±1,±1) coefficient32. These groups have1,6,12,12,24 members. Their support fits without aliases on length5; this is a local contraction identity for every larger torus, not an interpolating fit. The source now accumulates integer numerators before exact division byV, strengthening the initial float-rounding control noted by the independent checker.

For Omega=A J|q|, the spectral projection bound gives liminf Q low-window fraction at least[max(0,sqrt(4/7)-sqrt(8/3)/A)]². It is strictly positive forA>sqrt(14/3). This does not locate a pole.
