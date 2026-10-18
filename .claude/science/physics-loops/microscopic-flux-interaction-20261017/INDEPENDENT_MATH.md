# Scoped mathematical check: central flux sectors and interactions

This note checks the architecture specified by the root author, not every one-qubit Hamiltonian: an exact BKSF representation of a number-conserving quadratic fermion Hamiltonian, additional polynomial functions of commuting central loop/repetition constraints, and an embedding with genuinely decoupled frozen spectators. No microscopic flux-changing operator, interacting matter vertex, local occupation penalty, dynamical boson, measurement feedback or bath is assumed.

## 1. Central sectors cannot provide virtual-flux exchange

Let the mutually commuting constraint operators be C_a, let P project onto a selected joint eigensector, and Q=1−P. Suppose every actual Hamiltonian term commutes with every C_a. Then

    [H,P]=0,
    P H Q = P H (1−P)=H P(1−P)=0.

This is an exact operator identity, independent of a large-penalty approximation or perturbative truncation. Adding f(C_1,...,C_n) changes sector energies but not the identity. In particular the usual Feshbach correction

    P H Q [E−Q H Q]^−1 Q H P

vanishes wherever the inverse exists. There is no second-order virtual excursion to other flux sectors, and no higher-order sequence can start one. In Schrieffer-Wolff language there is no off-block generator to eliminate if the **full actual** H is already block diagonal. A small energy denominator cannot produce an effect when its matrix-element numerator is exactly zero.

The assertion requires centrality with respect to the full dynamical Hamiltonian, not just mutual commutation among constraint terms. An added operator V with [V,C_a]!=0 invalidates it and can allow virtual flux exchange. Such an operator must be shown in the microscopic model; it cannot be supplied by the name 'fluctuating flux'.

If a repetition constraint has not actually been checked against every embedded interaction, this argument is only conditional. Decoupled spectator qubits do not change PHQ: their independent evolution factors, and freezing them cannot mediate a source–source interaction.

## 2. Fixed-sector matter dynamics stays quadratic

Within a physical sector admitting the claimed faithful fermionic representation, take

    H_c = sum_ij (h_c)_ij c_i^dagger c_j + E_c,

where E_c is the constraint polynomial's constant value in that sector. Flux dependence of h_c, e.g. a static boundary twist, does not make it an operator-valued dynamical interaction within that sector.

For any number-conserving bilinears O_A=c^dagger A c and O_B=c^dagger B c, the canonical anticommutation relations give

    [O_A,O_B]=c^dagger[A,B]c.

The apparent four-operator terms cancel exactly. Consequently nested commutators of quadratic matter terms remain quadratic. Unitary mode changes, time evolution under prescribed time-dependent quadratic coefficients, and an ordinary quadratic Schrieffer-Wolff block diagonalization cannot generate an independent quartic fermion vertex. A time-dependent *externally prescribed* hopping or mass remains a driven free system, not an autonomous mediating field.

The faithful-sector qualification matters. If the claimed encoded operator algebra is incomplete or the embedding has undisclosed leakage/couplings, check that mapping first; the algebra here does not prove the implementation.

## 3. Eliminating high-energy fermion bands

Partition one-particle modes into retained L and eliminated H. The exact one-particle resolvent has the Schur complement

    h_eff(z)=h_LL+h_LH(z−h_HH)^−1 h_HL.

It is energy dependent but is still a one-particle matrix. Equivalently, integrating high Grassmann variables out of a quadratic action produces a quadratic, potentially time-nonlocal low-mode kernel plus a determinant independent of the retained fields. No four-low-fermion term arises when the original coefficients are c-numbers and there is no interaction. Expanding the kernel in energy/frequency yields higher time derivatives or hopping renormalization, not a genuine four-point interaction.

If high modes are already exact band eigenmodes, their occupations are conserved and the free many-body spectrum is additive. Fixing their occupations only adds a constant energy to the retained Fock problem. In perturbative non-eigenmode bases, terms that seem quartic must be checked against bilinear commutator closure and omitted exchange/Pauli contributions before interpreting them as interactions.

Scope limitation: this statement retains the complete Fock space of selected low single-particle modes (possibly within a fixed total parity/number sector). An arbitrary projected many-body subspace—such as imposing local single occupancy, a nonlinear occupation-dependent penalty, or retaining selected correlated states—is not the same operation. Such a projection can produce nonlinear-looking effective operators. If its enforcing Hamiltonian does not commute with hopping, it is a new interacting microscopic premise. A noninvertible encoding/relabeling may also express a quadratic operator using products of new variables; that is not by itself an additional physical scattering vertex.

## 4. Gaussian dynamics does not mean every state is quasifree

A quasifree initial state evolved under a quadratic Hamiltonian remains quasifree. The unprojected grand-canonical thermal state of a fixed quadratic H is quasifree, and its correlators obey Wick factorization. A pure Slater determinant is quasifree.

But an arbitrary state in a fixed flux sector is **not** necessarily quasifree. Quadratic dynamics can preserve/evolve initially non-Gaussian correlations. Canonical fixed-number thermal mixtures and fermion-parity-projected grand-canonical ensembles are generally not quasifree at finite size. BKSF commonly represents a fixed fermion-parity sector; therefore 'fixed physical code sector' alone does not justify applying unrestricted grand-canonical Wick identities. State and ensemble assumptions must be stated separately.

Those ensemble/initial-state correlations do not establish a generated quartic term in the Hamiltonian. They can change response functions, and they can invalidate a naive Wick-based numerical prediction if the ensemble is wrong, without changing the exact operator closure above.

## 5. Superposed or mixed static sectors

A global state can be a mixture of central sectors, or contain cross-sector coherences if the full Hilbert space and observables allow them. Since H preserves sectors, their weights do not undergo flux hopping. Sector-dependent phases or matter evolutions can entangle the static sector label with matter. Tracing that label gives a mixture of different free evolutions, which need not be a Gaussian channel or yield Wick-factorizing matter statistics.

For observables commuting with all C_a, cross-sector coherences are unobservable and expectations are weighted sector sums. Such sums can show connected higher correlations even if each component is quasifree. This is static-sector/ensemble uncertainty, not an autonomous flux-exchange interaction. If sector-changing observables are measurable, their transitions and phases require separate analysis; that does not imply H contains the corresponding transition operator.

Treating static sector labels as 'annealed' variables and summing them in a global partition function can yield a nonlinear effective statistical weight for matter. It assumes an ensemble over sectors, potentially prepared by physics outside the stated sector-conserving Hamiltonian. It must not be silently equated with a local dynamical quartic interaction generated by virtual flux. A real bath or perturbation that changes sectors would be an additional ingredient.

## 6. Particle–hole poles versus an autonomous scalar

A free bilinear observable has particle–hole response. For a specified quasifree equilibrium ensemble its spectral denominators are free energy differences epsilon_b−epsilon_a with occupation weights and matrix elements. Finite systems have discrete response poles, and special flat bands, selection rules or kinematic gaps can isolate some transitions. Therefore it would be false to claim 'a free system cannot have any isolated response pole'.

What is absent from the stated quadratic model is a new interaction-generated collective bound state or an independently self-consistent scalar degree of freedom. A pole corresponding to a free particle–hole transition is already accounted for by the free many-body spectrum. Calling it a scalar requires an additional operational identification and does not give it universal matter coupling, a nonlinear restoring potential, a healthy local field action, or the source/detector–cosmology map.

In a thermodynamic dispersive system, particle–hole transitions commonly form continua, but whether an isolated free pole survives is a concrete spectral question, not a universal prohibition. Conservation laws also produce static response/order-of-limits subtleties. A putative collective pole must be distinguished from these effects using its spectral weight, finite-size scaling, dispersion, damping and dependence on any actual interaction.

## 7. Actionable conclusion and loopholes to inspect

Under the exact stated assumptions:
- PHQ=0 blocks virtual-flux Schrieffer-Wolff mediation.
- Bilinear commutator closure and Gaussian elimination prevent a generated independent four-fermion vertex from free high-band elimination.
- Static constraint-sector mixtures may generate statistical correlations but do not supply an autonomous fluctuating mediator.
- Free particle–hole excitations remain available for study; their interpretation as a scalar connection is not supplied by the encoding.

Concrete changes that could open a genuinely different route, each requiring an explicit term/derivation, include:
1. A noncentral microscopic perturbation that flips flux/repetition constraints, with verified nonzero PHQ and controlled denominators.
2. An actual density/exchange/quartic term or a noncommuting local occupation penalty.
3. A quantum dynamical hopping/mass variable with its own Hamiltonian, rather than a c-number source.
4. A genuinely coupled spectator/bosonic sector whose elimination produces a retarded matter interaction.
5. A bath/measurement mechanism, with its nonunitary and preparation assumptions made explicit.

This is a scoped closure result for the specified free encoded architecture. It is not a no-go theorem for all one-qubit Hamiltonians, all encodings, all constrained systems, or emergent scalar mechanisms generally.
