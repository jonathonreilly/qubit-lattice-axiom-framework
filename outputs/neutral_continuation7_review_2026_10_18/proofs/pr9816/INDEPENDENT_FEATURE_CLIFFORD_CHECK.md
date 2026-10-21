<!-- Original PR9816 source SHA256 e6d041c2f3d03509df01b5cb6e61b650e5b6d73cf5c059845a2754c86c9e0050. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Feature Clifford dimension and commuting-port compression bound

Disposition: PASS. The dimension obstruction, trace bound and sharpness construction are valid under the stated finite-dimensional complex-Hilbert-space assumptions. They are kinematic statements and do not establish a native low-energy fermionic feature.

## Dimension

Let six Hermitian operators obey {Gamma_a,Gamma_b}=2 delta_ab I. Define B_j=i Gamma_(2j-1) Gamma_(2j), j=1,2,3. Each B_j is a Hermitian involution and the three commute. Their eight joint sign eigenspaces give an orthogonal decomposition. Gamma_(2j-1) is a unitary bijection that flips the jth sign and commutes with the other two B's. Hence all eight eigenspaces have equal dimension. A nonzero representation therefore has dimension 8m, m>=1.

If the feature is encoded in n physical qubits, 2^n must be at least eight, so n>=3. This is a bound on the total feature Hilbert space, not three qubits at each microscopic site. Equality can realize the abstract Clifford algebra, but it does not turn six commuting physical operators into six anticommuting ones by a unitary change of basis.

## Compression of commuting ports

Assume A_i are commuting Hermitian involutions on the physical space, V is an isometry from a d-dimensional encoded space, and V^dagger A_i V=alpha_i Gamma_i, with real alpha_i. Their joint spectral projectors Pi_s, s in {+/-1}^6, give positive operators E_s=V^dagger Pi_s V with sum E_s=I and marginals sum_s s_i E_s=alpha_i Gamma_i. Some Pi_s may vanish; independence of the ports is not required for the necessary bound.

Set A=sqrt(sum alpha_i^2) and F_s=sum_i alpha_i s_i Gamma_i. Clifford anticommutation gives F_s^2=A^2 I, so F_s<=A I. Therefore

 d sum_i alpha_i^2
 =sum_s Tr(E_s F_s)
 <=A sum_s Tr(E_s)=d A.

Thus A^2<=A, and either A=0 or A<=1. In particular sum alpha_i^2<=1 and equal nonnegative alpha satisfies alpha<=1/sqrt(6). The trace proof needs neither commuting E_s nor equality of their ranks. It also handles negative alpha through their squares.

**Deferred terminal interpretation — not an active promoted theorem; packet pending.** The complete original continuation is preserved below. The coefficient identities, commutators, compression inequality and specified finite residual calculations remain active with their exact hypotheses.

> Exact alpha_i=1 compression of all six commuting ports is impossible. More strongly, if a single compressed involution has alpha_i^2=1, its physical action leaves the code invariant; combining that with another exact port would preserve their physical commutator. A full three-qubit unitary encoding preserves all commutators automatically and cannot evade this obstruction.

## Sharpness and eight-qubit dilation

For any Clifford representation and sum alpha_i^2<=1, the explicit joint POVM

 E_s=2^-6 [I+sum_i alpha_i s_i Gamma_i]

is positive, normalized, and has the required marginals. Hence the norm bound is sharp when the physical dilation and commuting ports are free to be chosen. This does not prove attainability for an arbitrary fixed collection of native ports with additional dependencies.

At d=8 and alpha_i=1/sqrt(6), each E_s has rank four: its two eigenvalues are 0 and 1/32. The direct-sum Naimark dilation has dimension 64*4=256, exactly eight physical qubits. Label the 64 four-dimensional blocks by s. Six commuting Z ports on the sign-register bits then have eigenvalues s_i, and the isometry formed from factorizations E_s=W_s^dagger W_s has the desired compression. Thus the proposed eight-qubit construction is sufficient. This argument makes no claim that eight is the minimal possible dilation size.

Independent numerical construction with the standard three-qubit Jordan-Wigner Clifford matrices gives all 64 ranks equal to four, normalization error below 3e-17, and marginal error below 3e-18. Positivity at the boundary is exact algebraically; floating eigenvalues around -1e-17 are roundoff.

## Leakage and physical scope

At saturation each individual involutory port has exact code leakage

 V^dagger A_i (I-VV^dagger) A_i V=(1-alpha_i^2)I=5I/6.

This is compatible with the compressed Clifford algebra and explains why compression does not preserve products. It does not imply a corresponding lower bound on leakage of a particular native Hamiltonian, whose terms can combine differently. That Hamiltonian and its spectral separation must be checked separately.

The construction is an operator-code realization with unsharp physical marginals. It does not choose a low-energy projector, prove autonomous native dynamics, establish anticommutation between separated features, or derive fermion exchange statistics. No per-site enlargement or added interaction is justified by the kinematic dimension count alone.

No repository edits or formal audit.
