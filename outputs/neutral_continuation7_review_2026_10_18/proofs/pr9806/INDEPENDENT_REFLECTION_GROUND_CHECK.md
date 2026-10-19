<!-- Original PR9806 source SHA256 3ec959d096d8959a4b830efd6a86d28f2c84c56da9dc24089653ec6bd4fdb333. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Independent check: two-cut reflection positivity and plane characters

Disposition: the proposed argument is valid for existence of an all-positive-plane global ground state on the stated finite even R by R by 10 periodic compass lattice, at J>0 and lambda>0. It does not prove uniqueness or exclude other ground-state characters. It bypasses, rather than estimates, the exponentially small winding splitting.

The primary mathematical context is Lieb and Schupp, *Singlets and reflection symmetric spin systems*, https://arxiv.org/abs/math-ph/9910037. I consulted that source but do not import its Heisenberg/singlet conclusion. The compass-specific matrix inequality and character bookkeeping are derived below.

## 1. Coefficient-matrix energy inequality

Identify the two reflected half-lattice Hilbert spaces and write a normalized state as a square coefficient matrix Psi, with tr(Psi^dagger Psi)=1. A reflection-positive Hamiltonian has the form

H=h tensor I+I tensor conjugate(h)-sum_b g_b A_b tensor conjugate(A_b),

g_b>=0, with the crossing A_b Hermitian. For the cuts used below h is real symmetric, because every internal YY bond contains two imaginary Pauli factors.

Set P=sqrt(Psi^dagger Psi), Q=sqrt(Psi Psi^dagger). Both coefficient matrices are normalized. The average internal energy of P and Q equals the internal energy of Psi. For each crossing operator, write a polar decomposition Psi=U P, extending the partial isometry to a unitary if necessary. Hilbert–Schmidt Schwarz, or 2 Re tr(X^dagger Y)<=||X||_2^2+||Y||_2^2, gives

Re tr(Psi^dagger A Psi A^dagger)
 <= [tr(P A P A^dagger)+tr(Q A Q A^dagger)]/2.

For example take the two matrices P^(1/2) U^dagger A U P^(1/2) and P^(1/2) A P^(1/2). The first squared norm is the Q term, and the second is the P term. Multiplying by each negative crossing coefficient proves

E(Psi)>=[E(P)+E(Q)]/2.

If Psi is a ground state, both P and Q are therefore ground states: their energies cannot lie below the ground energy and their average cannot exceed it. Singular Psi causes no obstruction; P and Q are uniquely defined and retain their unit Hilbert–Schmidt norm.

## 2. Plane constraints under polar replacement

For a spanning plane whose half operator A is real Hermitian with A^2=I, a character equation is A Psi A=s Psi, s=+1 or -1. This implies A commutes with Psi^dagger Psi and Psi Psi^dagger, hence with P and Q. Therefore A P A=P and A Q A=Q: both polar replacements have the positive spanning-plane character, regardless of s.

For a plane contained in one half, A Psi=s Psi implies A Q=s Q; similarly Psi A^T=s Psi implies P A^T=s P. After interpreting Q or P as a coefficient matrix on the reflected full lattice, this copies the retained half's character to its reflected partner. The assertion follows by support/function calculus even when the density matrix is singular. It does not require choosing a polar unitary compatible with every constraint.

## 3. First, the x cut

Choose reflection x->R-1-x, splitting the periodic torus into equal halves. Both boundary cuts have bonds joining a site to its reflected partner: the bonds between R/2-1 and R/2, and between R-1 and 0. Every crossing term is -J lambda X tensor X, exactly the required -g A tensor conjugate(A). Reflection reverses some internal bond orientations but leaves their operators and couplings unchanged. Thus both periodic boundaries satisfy the same inequality; no boundary term is omitted.

All physical plane operators commute: their cross-family intersections have even length R or 10. Start with a ground vector of simultaneous plane characters, which exists by this commutation. Y and Z planes span the x cut. A half-Y plane contains RL/2=5R sites, an even number since R is even. Its transpose equals itself, so the preceding spanning-plane argument sets every Y and Z character to +1. Z half operators are real directly. X planes are contained in the halves; choosing one polar replacement copies one half's X-character pattern to the other. The resulting ground vector still has definite X characters, although they need not yet be positive.

## 4. Second, the y cut and the twist

For a y cut the unmodified crossing term is -J lambda Y tensor Y, whereas conjugate(Y)=-Y. Apply the unitary Z product over the entire right y half. It reverses every crossing YY bond and leaves every internal bond unchanged: internal XX or YY has either two conjugated endpoints or none, and ZZ is unchanged. The crossing terms become +J lambda Y tensor Y=-J lambda Y tensor conjugate(Y), again reflection positive with identical real internal h.

This twist commutes with every full physical plane symmetry. An X plane meets the twisted region in RL/2=5R sites, even. A Y plane lies entirely inside or outside and, if inside, has RL=10R sites, even. All Z planes commute sitewise. Thus the twist preserves all plane character labels, including the already positive Y and Z values.

Apply polar replacement using the y reflection. X and Z now span the cut and have real half operators, so their characters become positive. The Y planes are contained within a half; the inherited positive Y pattern is copied and remains positive. Mapping back by the same right-half Z unitary preserves these characters and returns a ground state of the original compass Hamiltonian. All X, Y and Z plane characters are therefore +1 simultaneously.

## 5. Consequences and boundaries

This establishes an all-positive-plane global ground state for every finite even transverse R and the given even longitudinal height, without a small-lambda bound or a size-dependent tunneling remainder. The proof is exact and independent of the selected-sector perturbative reductions. Therefore a theorem using the ground state of that positive sector can now choose it to be a global ground state along the previously considered grid families.

It does not show that every ground state belongs to that sector, that the ground is unique, or that all ground-state observables agree across any remaining degeneracy. It does not evaluate the character gap, establish a full-system excitation gap, or remove the action/geometry/anisotropy premises. An 'arbitrary actual ground' claim would require an additional argument. The finite-volume existence conclusion is enough to remove an assumed higher-energy-sector objection for a specifically chosen positive-character ground, but not to infer a unique physical preparation.

The parity counts are essential. An odd transverse size or an odd half-Y transpose parity could alter the character conclusion; no such extension is claimed. Likewise the crossing couplings used in the inequality must have the displayed nonnegative magnitudes. No diagonal stoquastic gauge is assumed: the exact native sign-frustration obstruction to that different method remains compatible with this two-cut reflection argument.
