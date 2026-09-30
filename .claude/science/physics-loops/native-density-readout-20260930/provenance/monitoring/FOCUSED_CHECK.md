# Focused independent check of native occupation-monitoring energy

No material mathematical error was found in the complete candidate WORKING_PROOF.md, SHA25610f2a739fbf0674998720ad08526e06fcf39495b29094a5ce88fea41879b4bc6. Its exact pinned matrices, all-state operator inequality and integrated monitoring budget are supported at their supplied finite-volume scope. This is a focused provisional mathematical check, not a formal review, audit or physical-record theorem.

## Exposure, actual sources and method

My PRE.md, SHA42d34d02e0849e65287d0f01ae1d2b6d786317de4049415325400d26169123a1, was frozen before opening the candidate, any author code or author results. The brief named the target, actual model and candidate hash, but supplied no new formula or verdict. I previously authored the sharp-readout energy packet and native many-body proof packets; that role is disclosed. The previous c_read was known. The new incident matrix, Lindblad product rule and integrated inequality were independently derived in PRE before comparison. This is computational and derivational separation within the campaign, not external peer review.

The actual main density-onset source was fully read in the immediately preceding route, and its literal operator/positive-decomposition section was freshly reread before PRE. Its identity is7180c065165cb5db45f3405fcc9711ec38145a3d2391962ed767d55f4cc25ee0 at mainfb5da8dd5ac1b001b0c619070f27e5b7f8fe4be7. The current foundation memo, registry and all three approved primitive notes were fully read in the preceding route and their unchanged bytes reverified here. The preceding readout proof and complete root receipt84d0e46e are context, not substitutes for the new derivation. The parent first-moment/S-only work mentioned in the candidate's provenance was not consumed: the required estimate is reconstructed directly below from the literal Hamiltonian. No open EOS, threshold eigenvalue, phase theorem, apparatus theorem or external literature theorem is used.

One independent exact Fraction control was written after the analytic PRE and candidate read, with expectations and source frozen before execution. It assembles the pin from the original attraction and gradient terms, using the exact diagonal correction, rather than importing the candidate or reusing the earlier S-row assembly. A second part uses actual four-qubit occupation paths to test dissipator normalization. No author code was run or imported.

## 1. Exact full-carrier adjoint identity

Keep full tensor-product M2 site factors on the cubic torus L>=5, mu,tau>0, and the actual H0=S+mu Ddiag+W. The graph edges have offsets +/-2e_i or +/-e_i+/-e_j. Let B_e=b_i b_j for each unordered graph edge e={i,j}, and let K be the positive scalar edge matrix for S+W=B^dagger K B. Each e has two distinct sites. For the convention

    D[n]^*(O)=n O n-(nO+On)/2=-[n,[n,O]]/2,

write P_x for the numerical projection onto edges incident to x. Since [n_x,B]=-P_xB, the dissipator product rule yields

    sum_x D[n_x]^*(B^dagger K B)
       =sum_x B^dagger P_x K P_x B-2B^dagger K B.           (1)

The two loss terms each give minus B^dagger K B because sum_x P_x=2I. This identity does not assume that distinct B_e are independent physical annihilators. It is an exact algebraic identity on the original hard-core carrier. The positive diagonal Ddiag commutes with every n_x and has zero dissipative derivative. Define

    J=sum_x B^dagger P_x K P_x B,
    Q_read=sum_x D[n_x]^*(H0)=J-2(S+W).

Hence Q_read+2H0=J+2mu Ddiag. Retaining this diagonal term is essential to the all-state N bound.

A useful normalization check is an individual B_e^dagger B_f. Its coefficient under the summed dissipator is |e intersect f|-2. It is0 for e=f, -1 for one shared endpoint and -2 for disjoint pairs. Treating every offdiagonal entry as decaying at rate2 would be wrong. The four-qubit control verifies these values by literal input/output occupation factors in nOn-{n,O}/2, including the shared-endpoint case.

## 2. Full pin matrix and its two meanings of kernel

Fix x=0. The incident vector has eighteen components b_0 b_y: six axial neighbors and four sign choices in each of three coordinate planes. The actual compression P_0 K P_0, on these eighteen coordinates, is

    (2mu/3+4tau)I_6
    direct-sum three copies of
    (3mu/2+3tau)I_4+(mu/4-3tau/2)A_C4.                   (2)

Here the cycle joins plane sign patterns (s,t) differing in one sign. There is no axial/plane or distinct-plane mixing.

For S, a fixed incident axial word is alone in its centered singlet restriction, giving2mu/3. Each plane word occurs in three differences at each of its two centers, giving diagonal3mu/2. At either center the two incident signed plane words have opposite signs. Their difference Gram therefore gives positive offdiagonal mu/4; these pairs are exactly the cycle edges.

For W, every center containing a pair incident to0 is one of the six nearest neighbors of0. No two distinct such centers are nearest neighbors to one another at L>=5. Thus a gradient between adjacent centers cannot have incident terms on both sides. The cross-center pin block vanishes, although the unpinned Hamiltonian cross terms certainly do not. Each center occurs six times in the three-direction gradient sum. The E Gram gives axial4tau. The T Gram at a fixed center has opposite coefficients1/2 and-1/2 for its two incident words, giving negative offdiagonal-3tau/2. Including both centers supplies diagonal3tau. This accounts for the entire W contribution in (2). It uses the actual six-center geometry and does not assume global bipartiteness on odd tori.

The plane characters1,s,t,st give eigenvalues

    2mu,    3mu/2+3tau,    3mu/2+3tau,    mu+6tau.

Together with six axial eigenvalues2mu/3+4tau, their minimum is

    lambda_pin=min(2mu/3+4tau,2mu)=2c_read,
    c_read=min(mu/3+2tau,mu)>0.                            (3)

In particular dropping W is a valid weaker estimate but loses this actual parameter-dependent pin. Its offdiagonal sign cannot be replaced by a diagonal row count.

The numerical18x18 matrix has no nullspace. On the full carrier, the positive operator J does have a kernel: it consists exactly of states annihilated by every graph-edge B_e. Since ||B_e psi||^2=<n_i n_j>, this is the span of occupation configurations that are independent sets in the eighteen-neighbor graph. This distinction is consistent with the candidate's explicit warning that (2) is a numerical kernel compression, not a compression of the many-body Hilbert space. Adding2mu Ddiag removes every nonvacuum vector in that kernel; the eventual comparison controls particle number.

## 3. All-state comparison and sharp normalization

For every vector psi, apply (3) to the Hilbert-space-valued incident components B_e psi and sum over x. Each unordered edge is counted at its two endpoints. Therefore

    J>=2c_read sum_x n_x m_x=4c_read E_pair,
    E_pair=sum_(unordered graph edges ij)n_i n_j.          (4)

No independence, factorization, condensate, fixed-N restriction or real-amplitude assumption is used. Arbitrary complex coherent and mixed states are included by the operator inequality.

The actual diagonal count identity is

    Ddiag=N-2E_pair+V3/mu,
    V3=mu sum_x n_x binom(m_x,2).

Consequently the candidate's stronger remainder formula is correct:

    Q_read >=2c_read N-2H0
             +2(mu-c_read)Ddiag+(2c_read/mu)V3
           >=2c_read N-2H0.                              (5)

Both remainders are positive on the full carrier because m_x has integer spectrum, f(m)=(m-1)(m-2)/2>=0 there, V3>=0 and c_read<=mu. The last inequality does not require a low-energy input.

As an additional coefficient discriminator,2c_read is sharp if the coefficient of H0 is held at-2. A monomer has <Q_read>=0 and H0 expectationmu, realizing ratio2mu in Q_read+2H0 per particle. An axial dimer has <Q_read>=0 and H0 expectation2mu/3+4tau, realizing ratio2mu/3+4tau per particle. These occupation configurations are legitimate at every stated L. This is sharpness of the comparison constant, not equality in the integrated bound for an arbitrary evolving state.

The adjective heating requires a state qualification: Q_read is not claimed positive as an operator. The adjoint of this unital finite-dimensional dissipator has zero trace on every input, so a nonzero Q_read cannot be positive everywhere. Equation(5) instead supplies a useful lower derivative while E<c_read nbar and a general comparison at all energies.

## 4. Differential integration and necessary budget

Supply the stated master equation, with real fixed nu,

    rho_dot=-i[H0-nuN,rho]+gamma(t)sum_x D[n_x](rho),

where gamma>=0 is bounded and integrable on the time interval being considered. The finite-dimensional linear equation has a unique absolutely continuous density-matrix solution. Equivalently, piecewise constant positive-rate propagators are completely positive and trace preserving, and their norm limits give the solution. There is no thermodynamic-limit dynamics assertion here. Bounded local integrability suffices for every finite time interval.

Both [H0,N]=0 and [n_x,N]=0 hold literally. Thus nbar=Tr(Nrho(t)) is constant, and all Hamiltonian contribution to E'(t), E=Tr(H0rho), vanishes, including the supplied chemical-potential term. Equation(5) gives almost everywhere

    E'(t)>=2gamma(t)(c_read nbar-E(t)).

Multiplying by exp(2Gamma(t)), Gamma(t)=integral_0^t gamma, and integrating proves

    E(t)>=c_read nbar+[E(0)-c_read nbar]exp(-2Gamma(t)).    (6)

Nonconstant rates and intervals with gamma=0 are handled by the same absolutely continuous integrating-factor calculation. There is no division by gamma. If nbar=0, positivity of N forces the vacuum state and both sides vanish. If E(0)>=c_read nbar, (6) remains valid but does not assert monotonic heating. If E(0)<c_read nbar, its lower bound rises toward the floor with integrated monitoring strength.

For an input with E0<c_read nbar, an endpoint condition E(t)<=Emax<c_read nbar requires

    Gamma(t)<=0.5 log[(c_read nbar-E0)/(c_read nbar-Emax)]. (7)

This is the candidate's direction and factor, with both denominators positive. If Emax<E0, its negative right side simply shows that the condition cannot hold; if one says maintaining the tolerance over an interval, Emax>=E0 is necessary already at time0. A necessary condition is not a sufficient control or attainability theorem.

For fixed mu,tau and nbar>0, put e0=E0/nbar, emax=Emax/nbar. If e0 and emax are O(r) as r->0, with e0<=emax<c_read, then the right side of (7) is O(r). The energy scale c_read must remain fixed in this statement; no joint limit mu,tau->0 is implied. In the concrete density notation r=nbar/V, a target E(t)/V<=C r^2 with C r<c_read implies, using E0>=0 alone,

    Gamma(t)<=-0.5 log(1-C r/c_read)=O(r).

This is only the supplied tolerance implication. The landed normalized unitary trial supplies actual small energy-per-particle initial states, but it does not select a phase, a tolerated energy, a measurement strength or a physical clock. No open EOS is necessary for this conclusion.

## 5. Instrument and physical scope

The master equation is a supplied uniform independent on-site dephasing law. It specifies unconditional dynamics; it does not uniquely specify monitored trajectories or a readout instrument, prove a realized outcome, or make records permanent. The inequality concerns expected energy, not pathwise energy injection in every noise realization or conditional history.

The sum of local dissipators is load-bearing. Monitoring only the conserved global N would give D[N]^*(H0)=0 and none of the positive bound. That is a different observable and a different instrument. Likewise no identical bound is established for low-wavevector-only density noise, arbitrary local rate patterns or a coarse observable. The result concerns the local monitoring sum, not a soft collective mode or its spectrum.

The system-energy increase still requires a complete apparatus ledger before being called supplied work. If an implementation has endpoint interaction-energy change, it enters the first law; (6) alone does not bound the initial apparatus energy without those endpoint conditions. No finite apparatus, autonomous implementation, finite-temperature work optimization, universal per-Record price or axiom inconsistency follows. Current registered primitives keep their grants but do not choose H0, basis, state, master equation, gamma, clock or apparatus.

## 6. Actual independent controls and limits

The one guarded control run exited0 without a failure or revision. Scientific CPU0.464767 seconds, wall0.465278 seconds, peak RSS21,397,504 bytes; supervisor wall0.613518 seconds. The declared5 CPU/30 wall/100 MiB envelope and BLAS1 were enforced with deadline/STOP guards. There are no unmanaged workers.

Actual evidence:

- Original-Hamiltonian attraction plus actual gradient assembly on L5 and L6 gives each full18x18 pin. All324 entries of each mu and tau matrix are compared exactly, including mixing zeros and negative W offdiagonals. The exact matrices are retained in RESULTS.json. No S-row or candidate-code builder was imported.
- All12 plane sign-character eigenvectors per torus have the displayed symbolic mu/tau coefficients. Six axial entries are separately exact. No floating eigensolver is used.
- All36 ordered pair pairs and16 occupation inputs on four actual M2 factors are checked. The78 nonzero physical B_e^dagger B_f paths give24 zero,48 minus-one and6 minus-two dissipator coefficients. This directly checks the product-rule normalization and shared endpoints.
- All1024 occupation masks on ten embedded actual lattice sites satisfy the full Ddiag/N/edge/V3 identity, with four rational parameter cases per mask also checking the positive remainder equality. This is a finite count check, not an all-N enumeration.

The all-volume and arbitrary-state conclusions are supplied by the algebra above, not the finite fixtures. No author code rerun, dense many-body matrix, evolution solver or numerical inequality fit was used. The candidate's exact source bytes were reverified after comparison. No correction to the frozen author source is requested. The permitted reuse is the stated conditional all-state mean-energy comparison and necessary monitoring budget; all instrument-selection, permanence, phase and spectral obligations remain separate.
