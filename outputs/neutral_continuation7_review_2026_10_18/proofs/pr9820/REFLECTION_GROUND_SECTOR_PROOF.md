<!-- Original PR9820 source SHA256 23b7f439e2ad66896a01700867927630a7098adbbb456a4ea26ea9ff8c540945. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Exact global ground-state existence in the positive plane sector

Status: exact-support for the supplied finite even compass lattice. No claim of uniqueness, preparation or observational identification. This is an application of established reflection-positivity mathematics, not a claim to invent that method.

## Theorem

For the periodic R×R×10 one-qubit Hamiltonian

 H=-J sum_z ZZ-Jlambda sum_x XX-Jlambda sum_y YY,

with even R, J>0 and lambda>0, at least one global ground state has character +1 under every exact X plane normal to x, Y plane normal to y and Z plane normal to z. The result is uniform in finite R and needs no weak-coupling threshold. It does not establish that all ground states have these characters or that the ground is unique.

## Matrix inequality

Identify two reflected half-lattice Hilbert spaces. A state is a coefficient matrix Psi of Hilbert–Schmidt norm one. Suppose

 H=h tensor I+I tensor conjugate(h)-sum_b g_b A_b tensor conjugate(A_b),

where g_b>=0 and A_b are Hermitian. In our application h is real symmetric. Let P=sqrt(Psi†Psi), Q=sqrt(Psi Psi†), and write Psi=UP with a unitary extension of the polar partial isometry. Both P and Q have Hilbert–Schmidt norm one. For each A, apply the elementary squared-norm inequality to

 X=P^(1/2) U† A U P^(1/2), Y=P^(1/2) A P^(1/2).

It gives Re Tr(Psi†A Psi A†) <= [Tr(P A P A†)+Tr(Q A Q A†)]/2. The average internal energy of P and Q equals that of Psi. Therefore

 E(Psi)>=[E(P)+E(Q)]/2.

If Psi is a ground state, both P and Q are ground states. This includes singular matrices; no invertibility is assumed. The standard trace inequality appears in Lieb and Schupp, *Singlets and reflection symmetric spin systems*, [arXiv:math-ph/9910037](https://arxiv.org/abs/math-ph/9910037), Eq. (4). We have derived the needed matrix statement here; the paper's singlet/Heisenberg conclusion is not imported into the compass model.

## Character transport

A plane spanning the cut has character equation A Psi A=s Psi when its half operator A is real Hermitian and A²=I. Consequently A commutes with both Psi†Psi and Psi Psi†, hence with P and Q. Both replacements therefore have positive character: A P A=P and A Q A=Q. A negative spanning character need not be preserved by this energy-preserving ground-state replacement.

For a plane entirely in the left half, A Psi=s Psi implies that Q is supported on A's s eigenspace. Thus A Q=sQ and Q A=sQ. Interpreting Q on the reflected full lattice copies that left character to its reflected right partner. A right-half constraint works analogously with P. Functional calculus proves these support statements even at zero singular values.

## First cut: x

All plane operators commute because their cross-family intersections contain even numbers of sites. Start with a global ground vector of definite simultaneous plane characters. Reflect x to R-1-x. The two periodic crossing boundaries both join reflected sites and have terms -Jlambda X tensor conjugate(X). Internal YY bonds contain two imaginary factors, so h is real and reflection gives its conjugate on the other half.

The Y and Z planes span this cut. A half-Y plane has RL/2=5R sites, even, so its transpose sign is positive and its half operator is real Hermitian. The Z half operator is real directly. Polar replacement sets all Y and Z characters positive. X planes lie within halves; their definite characters are copied from one half and remain definite, though possibly negative.

## Second cut: y

A y crossing originally has -Jlambda Y tensor Y. Conjugate the entire right y half by its global Z product. Every internal XX or YY bond has both endpoints conjugated or neither, so internal h is unchanged; ZZ is unchanged. The crossing becomes +Jlambda Y tensor Y=-Jlambda Y tensor conjugate(Y), the required sign.

This half twist commutes with every full-plane symmetry. An X plane intersects it in RL/2=5R sites, even. A Y plane is wholly inside or outside; the former has RL=10R sites, even. Z planes commute sitewise. Thus the twist preserves the positive Y/Z characters already obtained.

Apply the matrix replacement for this cut. X and Z now span it, with real half operators, and acquire positive characters. Contained Y planes copy their already positive pattern. Undo the twist, which preserves all characters and restores the original Hamiltonian. The resulting global ground state has every plane character positive. Both periodic boundaries have been retained at each cut.

## Consequence for the native neutral pole

[ISOTROPIC_BOUND_FEATURE_PROOF.md](ISOTROPIC_BOUND_FEATURE_PROOF.md) constructs the low state and visible lower neutral pole in this positive plane sector on R~lambda^-5 at fixed height ten. Its low-energy sector ground is unique for sufficiently small lambda along that family because Q0 is one dimensional in the chosen fibre and the next Q sector is separated at order lambda4 after the controlled remainders. The exact theorem above guarantees that this sector's minimum equals the full global minimum.

Accordingly there exists an actual global ground state from which the derived original-source pole has the stated positive resolved-grid isotropic dispersion and nonzero weight. This removes the premise that the calculated sector might sit above the global ground. It does not turn a statement about that ground into a statement about every possible ground, nor derive unique physical preparation. The original uniform-source operator commutes with plane symmetries, so transitions from this state remain in its sector; other-character degeneracies do not enter its spectral-projector denominator.

The earlier all-history winding estimate remains unnecessary for this existence conclusion and remains open for quantitative character splitting or uniqueness. See [UNIFORM_GROUND_SELECTION_OPEN.md](UNIFORM_GROUND_SELECTION_OPEN.md). No new selector or boundary field was added.

## Numerical sanity checks and limits

neutral_reflection_ed.py compares unrestricted and positive-sector ground calculations for 2×2×2 and 2×2×4 periodic grids at lambda=.2,.7,1. These deliberately small controls use the same directed periodic bond convention, including coincident neighbors at length two. They check signs and projector implementation, not the all-size theorem; the L10 application follows from the analytic parity argument. Residuals and all plane expectations are recorded. All are exposed model-development data, not empirical tests.

The native Hamiltonian, periodic even geometry, fixed slab height, anisotropy, physical units and observable identification remain supplied. No three-dimensional continuum, Lorentz invariance, massless gravity, fermion statistics or cosmological matching follows. The proof makes no odd-size, negative-coupling, boundary-disordered or all-ground-states extension.
