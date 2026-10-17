# Free-fermion static response and a conditional collective-channel criterion

Scope: mathematical response of a **specified** finite number-conserving free Hamiltonian. This does not assert a Dirac vacuum, a filled lower cone, an interaction in PR9671, or a self-generated scalar. The root author is inspecting the actual current full Bloch Hamiltonian; this note does not replace that calculation.

## Definitions and ensemble

Let the many-body Hamiltonian be

    H(m)=sum_ab c_a^dagger [h+m M]_ab c_b,
    O_M=sum_ab c_a^dagger M_ab c_b,
    Nhat=sum_a c_a^dagger c_a.

Both h and M are Hermitian, independent of m; m is a classical applied source. At fixed chemical potential mu and positive temperature T=1/beta,

    Omega(m)=−T Tr log[1+exp(−beta(h+mM−mu I))].

The trace is over all one-particle modes, not a presumed negative-energy subsector. Fix the reference number N_c of **original cells** and write omega=Omega/N_c. This gives

    omega'(0)=<O_M>/N_c,
    kappa_M=−omega''(0)
           =(1/N_c) integral_0^beta d tau <delta O_M(tau) delta O_M(0)> >=0.

The imaginary-time covariance is the isothermal equilibrium response to a source −J O_M, with J=−m. The opposite sign in H(m) changes the first derivative convention but not kappa. If the microscopic h depends nonlinearly on the physical source, an additional Tr[f(h) h''] term appears in Omega''; the simple negative-curvature interpretation then applies to the linear operator perturbation, not automatically to that nonlinear parameter.

## Divided difference, degeneracies and positivity

Diagonalize h|a>=epsilon_a|a>, let f_a=[1+exp(beta(epsilon_a−mu))]^−1, and define

    D_ab = (f_a−f_b)/(epsilon_a−epsilon_b) if energies differ,
    D_ab = f'(epsilon_a)=−beta f_a(1−f_a) if energies coincide.

Then, including **all ordered pairs** a,b,

    omega''(0)=(1/N_c) sum_ab D_ab |M_ab|²,
    kappa_M=−(1/N_c) sum_ab D_ab |M_ab|².

This follows either by differentiating Tr f(h+mM)M using the Frechet derivative of f or by Wick contracting the imaginary-time covariance. f is decreasing, so each −D_ab is nonnegative. An unordered interband pair carries twice the corresponding ordered-pair contribution; dropping that factor is a common normalization error.

At a degenerate eigenvalue epsilon, the complete within-subspace term is

    beta f(epsilon)[1−f(epsilon)] ||P_epsilon M P_epsilon||_F² /N_c.

It includes off-diagonal entries within the degenerate subspace. Omitting them or treating only diagonal M_aa is basis dependent. The projector expression is invariant under basis rotations within that subspace. For near degeneracies use a stable divided difference/series, not subtraction of nearly equal occupations and energies.

At T=0 for a finite spectrum with mu strictly in a gap, diagonal/degenerate occupation terms vanish and

    kappa_M=(2/N_c) sum_{a occupied,b empty}
                         |M_ab|²/(epsilon_b−epsilon_a).

The occupied set is determined by the supplied ensemble, not by naming a band Dirac-like. At a level exactly at mu, the zero-temperature finite-system grand potential may be nondifferentiable. In the thermodynamic limit, Fermi-surface terms are distributional limits and must be retained. Finite T is a useful regulator, but is not evidence for a physical temperature or filling.

## Original-cell normalization

Suppose the chosen Bloch cell contains q original cells, with N_s=N_c/q Bloch momenta. For a uniform supercell-periodic source,

    kappa_M=−[1/(q N_s)] sum_k sum_ab D_ab(k)|M_ab(k)|².

If numerical k weights sum to one, multiply their band-trace average by 1/q. Equivalently in d dimensions,

    kappa_M=−V_original/(2pi)^d integral_BZ_super d^d k
                                    sum_ab D_ab(k)|M_ab(k)|².

Use all actual band/spin/orbital degeneracies once. The number of states per original cell is (# Bloch bands)/q. A q=2 doubling with 12 displayed bands does not produce 12 states per original cell. If the mass perturbation carries momentum in the original zone, folding it into a supercell is legitimate, but the source and normalization must be folded together.

## Fixed density is a different response

For fixed particle density rather than fixed mu, Legendre transforming the free energy gives

    kappa_M|n = kappa_MM − kappa_MN²/kappa_NN,

where the susceptibilities use the same per-original-cell normalization and kappa_NN>0. This is the Schur complement of the joint isothermal covariance matrix. In an incompressible zero-T regime where kappa_NN=0, do not divide by zero; directly analyze the fixed-number spectrum or a controlled limiting ensemble. Changing mu with m without accounting for this distinction changes the proposed criterion.

## Uniform common rescaling O=H0

For the fixed operator O=H0, h(m)=(1+m)h0. It commutes with the unperturbed many-body Hamiltonian and is diagonal in its energy basis. Its grand-canonical **isothermal static** susceptibility is

    kappa_H = beta/N_c sum_a epsilon_a² f_a(1−f_a)
            = beta Var(H0)/N_c.

This is a population/thermal response, not interband virtual mixing. For a finite zero-T gapped ensemble and rescalings that do not cross occupations, Omega is linear in m and kappa_H=0. In a thermodynamic metal, a T->0 Fermi-surface limit can remain (proportional to mu² times the one-particle density of states under suitable regularity); do not apply the finite-gap statement at a Fermi surface.

Crucially, the isolated real-time retarded commutator response of the conserved total H0 is zero: [H0(t),H0(0)]=0. Its nonzero isothermal susceptibility requires redistribution under thermal equilibration. In Matsubara frequency it is a zero-frequency covariance contribution, with zero nonzero-frequency response. Thus a static thermodynamic response cannot by itself establish an oscillating collective scalar or a dynamical propagator. The ordering of zero-frequency, long-wavelength, thermalization and thermodynamic limits matters.

A fixed-number thermal version subtracts the covariance with Nhat as above. A physical common rescaling of *all* energies and clocks may also be operationally invisible in relative measurements; the calculation presumes fixed external energy/time standards.

## Explicit new interaction and actionable criterion

One possible **new candidate premise**, absent from the original free H unless separately demonstrated, is the separable attractive interaction

    H_int=−G O_M²/(2 N_c), G>0.

This is the question's V normalization with V=N_c in original-cell units. If V instead denotes physical volume, adjust G and the susceptibility density accordingly. A normal-ordered version differs from O_M² by a one-body term (for fermion bilinears, a term involving c^dagger M² c); declare which interaction is meant and include that term consistently.

A static Hubbard-Stratonovich / mean-field decoupling with energy-like field phi gives

    Omega_MF(phi)/N_c = phi²/(2G)+omega_0(h−phi M),
    stationarity: phi/G=<O_M>_phi/N_c,
    local curvature: d²Omega_MF/(N_c dphi²)=1/G−kappa_M(phi).

If a symmetry forces <O_M>_0=0, phi=0 is stationary and the candidate static instability threshold is

    G kappa_M(0)=1.

For G kappa_M>1 the symmetric saddle has negative static curvature **within this decoupling and supplied ensemble**. If <O_M>_0 != 0, zero is not stationary; subtracting its value changes the interaction/source convention or solve for the actual saddle before testing curvature. Do not label a nonzero linear response spontaneous symmetry breaking.

A positive quadratic coefficient means local stability in this channel only. A negative coefficient does not prove a continuous transition or the final ordered phase: higher-order coefficients, other channels, finite-size fluctuations, filling constraints and possible first-order transitions must be checked. This Kac-normalized interaction is infinite range in O_M; a thermodynamic saddle can be useful, but the mean-field expression is not automatically an exact finite-system solution for a noncommuting O_M.

The quadratic fluctuation kernel is conditionally of the form

    D^−1(i omega_n)=G^−1−chi_MM(i omega_n)

in the corresponding Hubbard-Stratonovich treatment. Away from zero-frequency population terms, the free bubble can be written

    chi_MM(i omega_n)=(1/N_c) sum_ab
        (f_a−f_b)|M_ab|²/[epsilon_b−epsilon_a−i omega_n],

with the static coincident-energy limit defined by the divided difference above. At nonzero frequency an exactly degenerate numerator vanishes; one must not incorrectly insert the static beta f(1−f) term at every frequency. Analytic continuation and the full spectrum determine poles, continua and damping.

The global O_M² interaction supplies only the uniform collective channel. It does not establish a spatially local scalar field. A local interaction such as −(G/2)sum_x O_M(x)², or a specified finite-range kernel, is another explicit premise. Then derive chi(omega,q), check a healthy time-dependent pole/kinetic coefficient, stable spatial stiffness, damping and the actual matter coupling. A divergent susceptibility of a selected two-band truncation is not sufficient when the full lattice bands, filling and UV cutoff change the response.

## Numerical sanity control

`/private/tmp/collective-response-check/check.py` compares the divided-difference formula with finite differences of the exact 4-mode grand potential, including a deliberately degenerate pair. It also checks invariance under a degenerate-subspace rotation, the conserved-H covariance identity, and the fixed-number Schur complement. The constructed value kappa=1.2622832464957017 agrees with the smallest-step finite difference to about 1.3e−8. This is a check of formulas and implementation conventions, not of PR9671's Hamiltonian or nature.
