# Explicit native local-contact family and its scaling

This is a positive construction of additional specified source couplings.
It proves what the flat carrier and its first source vertex leave variable;
it is not an axiom-wide impossibility argument or an instruction to modify
the framework's premises.

Let s_A(x), A=1,...,6, be the components of S(x) in a fixed orthonormal basis
of real symmetric matrices. On the finite native carrier, n_x is the sum of
the two orbital occupations at a cell. Each occupation is (1-B_v)/2, where
B_v is the product of Z over the incident physical edge qubits. It is a
bounded-star projector, not a single physical-site projector. No new hopping
or quantum register is needed. Choose
any real finite coefficient array c_AB^ij with the symmetry needed to make
the following scalar real, and define

    Q_c[S](x)=sum_ABij c_AB^ij
                 [s_A(x+e_i)-s_A(x)] [s_B(x+e_j)-s_B(x)],
    delta H_c[S]=sum_x Q_c[S](x) n_x.                     (C1)

The scalar coefficients depend only on neighboring cell source values.
This is a bounded-support Hamiltonian coupling, not a derivation of the
framework's strict physical nearest-neighbor admissibility law.
The extra operator is bounded for a bounded field on a finite lattice. It
vanishes for every constant S, and its zeroth and first source derivatives
vanish at S=0. Thus it preserves all constant-frame spectra and node data,
the flat ground state, and every linear strain vertex. It changes neither
the first-jet common-metric construction nor the scalar spin-connection
term to first order.

At the flat half-filled state <n_x>=1 exactly: its one-particle occupied
projector is translation invariant and has orbital trace one per momentum.
Because C1 starts at second order, its exact energy-Hessian contribution
comes only from the first-order expectation of that second-order operator:

    E_c''[0]-E_0''[0]=sum_x (Q_c[S](x))''.                (C2)

No susceptibility of n_x enters until higher source order. On a finite
gapped grid this follows from ordinary spectral perturbation theory; the
quadratic coefficient has the thermodynamic value by the explicit density
identity. The Fourier polynomial is an explicit local contact. In particular,
for Q_c=c sum_i tr[(Delta_i S)^2],

    delta chi_AB(q)=2c sum_i 4 sin^2(q_i/2) tr(A B).       (C3)

The factor of two is the Hessian convention in R5. A real cosine source has
half this kernel as its second derivative per cell, checked against the
full finite Hamiltonian's eigenvalue sum.

## The same one-particle continuum limit can have different vacuum contacts

Restore physical coordinates x=a n and h_a=h_lat/a. For a fixed smooth
source field, |Delta_i S|<=a sup|partial_i S|. Thus C1 changes the
one-particle operator by a multiplication operator whose norm is O(a):

    ||delta h_a|| <= a C(c) sum_i ||partial_i S||_infty^2. (C4)

It therefore tends to zero even in full operator norm on the lattice
one-particle Hilbert space. In particular it preserves the controlled
common Dirac low-band limit proved in BLOCK06, with an additional O(a)
error. This statement does not require a new momentum-support estimate.

Physical vacuum energy per physical volume, however, is the dimensionless
lattice energy divided by a^4 V. The contact density in C1 is O(a^2), so
its physical contribution is c/a^2 times the corresponding spatial gradient
quadratic form. If c is replaced by a^2 c_R, the one-particle error is
O(a^3), but the physical vacuum functional instead receives the finite
coefficient c_R multiplying that gradient form. All these versions have
the same constant-field spectra and first-order continuum matter operator.
The new coefficients are choices, not measured or derived values.

An arbitrary real quadratic form in first spatial derivatives can be
realized by C1. For example, select coefficients giving the three-dimensional
Fierz-Pauli spatial quadratic expression

    partial_k S_ij partial_k S_ij
    -2 partial_i S_ij partial_k S_kj
    +2 partial_i S_ij partial_j tr S
    -partial_k tr S partial_k tr S.                      (C5)

Its continuum TT and transverse-trace signs differ. A corresponding local
finite-difference form follows by replacing the derivatives in this exact
expression. Multiplying it by any c_R realizes that static coefficient
while C4 still holds. This does not establish a stable dynamical metric,
temporal constraints, a nonlinear generally covariant completion, or the
physical value/sign of c_R. It exhibits an explicit remaining source choice.

The universal logarithm derived in BLOCK07 is unchanged: C1 has no first
vertex and its second derivative is a finite Laurent polynomial in q.
It cannot add a q^4 log q term. More generally, purely local geometric
counterterms have the same separation, but C1 is an explicit native matter
realization, so this observation does not rely on merely declaring a bare
gravity functional. A principle selecting the nonlinear source coupling or
its local coefficients would have to be supplied or derived separately.
