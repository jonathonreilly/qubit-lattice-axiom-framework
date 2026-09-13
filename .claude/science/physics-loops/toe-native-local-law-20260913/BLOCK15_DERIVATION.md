# Flat holonomies and the finite-volume spectral floor

Provisional derivation, personally developed after the open-box spectrum
milestone. No independent review, retained status, phase theorem or axiom
update. The ring result below is elementary. The periodic rotor argument
is a proposed bounded theorem requiring a fresh focused proof review.

## Exact charged ring and a direct weak-coupling theorem

Take four vertices on an oriented cycle, one CAR orbital per vertex, two
particles, reference eta=(0,1,0,1), unit real hopping, and no onsite term.
There is no plaquette attached to this one-dimensional ring. The full loop
holonomy is therefore a flat global variable, not a plaquette defect.
Use integer electric links and Gauss divergence E=N-eta. For occupation f,
rho_f=N_f-eta and the exact electric field is

```text
E=E0(f)+n(1,1,1,1),
E0(f)=(rho_0,rho_0+rho_1,rho_0+rho_1+rho_2,0), n in Z.
H_g=(g^2/2) sum_l E_l^2
   +sum_(oriented links x,y)(c_x^dag U_(x,y)c_y+h.c.).
```

At finite S the domain is |E0(f)+n|_infinity<=S. The exact Fourier transform
of the untruncated n coordinate identifies it with L^2(S^1) tensor the six
dimensional two-particle space. Here n=-i partial_theta, tree hoppings have
unit comparator and the closing hop has exp(i theta). Thus

```text
H_g=(g^2/2) sum_l[-i partial_theta+E0_l(f)]^2 + H_free(theta).
```

The electric expression is a positive quadratic form, including the
occupation-dependent connection. The free matrix H_free(theta) is continuous
and periodic. Let e_*=min_theta lambda_min H_free(theta).

**Claim:** for every fixed eigenvalue index j, as g->0 and S->infinity
along any joint sequence, E_j(g,S)->e_*. The untruncated operator at each
g>0 has compact resolvent and obeys the same limit.

Proof of the lower bound: H_free(theta)>=e_* I pointwise, the electric form
is positive, and compression to the exact finite-S physical domain preserves
the inequality. Hence every eigenvalue is at least e_*.

Proof of the upper bound: choose theta_* minimizing the lowest eigenvalue
and a normalized matter eigenvector v_* there. On a sufficiently small open
interval I around theta_*, continuity gives
v_*^dag H_free(theta)v_*<=e_*+epsilon. Choose j+1 orthonormal smooth scalar
functions supported in I and multiply each by v_*. Their finite-dimensional
span has matter Rayleigh quotient at most e_*+epsilon and finite electric
quadratic form, with coefficient g^2. Approximate that entire span by
finite Fourier polynomials in form norm at fixed epsilon. Because there
are only six charge offsets, sufficiently large S contains every such
polynomial in the exact affine domain. The finite-span error can be made
arbitrarily small before taking g->0 and S->infinity. Min-max gives the
matching upper limit. No claim about a uniform index or rate is needed.

For this uniform ring, discrete Fourier diagonalization of the one-particle
matrix gives eigenvalues 2cos((theta+2pi m)/4), m=0,1,2,3. For 0<=theta<=2pi,
the two occupied negative levels sum to

```text
e(theta)=-2[cos(theta/4)+sin(theta/4)]
        =-2 sqrt(2) cos((theta-pi)/4).
e(0)=-2,       e(pi)=-2 sqrt(2)=e_*.
```

The minimum is unique on the circle. The theorem therefore excludes the
identity-comparator ground energy -2 as the weak-coupling ring limit.
It also gives E_j-E_0->0 for every fixed j. This low-level accumulation is
different from the discrete fixed-index oscillator spectrum of a contractible
box. The difference comes from a global flat coordinate, not a failed local
Gauss law or an axiom contradiction.

For any physical ground states with E_0->e_*, their angle probability
outside a neighborhood of pi tends to zero. Indeed the positive electric
term gives integral[e(theta)-e_*]||psi(theta)||^2<=E_0-e_*, and the continuous
gap e(theta)-e_* has a positive minimum on each closed complement. It follows
that the loop expectation <Re W_loop> tends to -1. Compression does not
alter this expectation in a finite-S state embedded by zero extension.

The local expansion has e''(pi)=sqrt(2)/8 and principal electric kinetic
term -2g^2 partial_theta^2. A formal harmonic expansion predicts

```text
E_0=-2sqrt(2)+2^(-5/4)g+O(g^2),
E_1-E_0=2^(-1/4)g+O(g^2).
```

The numerical prototype challenges these coefficients but is not a proof
of these rates. A uniform Born-Oppenheimer error estimate and finite-cutoff
error bound have not been supplied. Only the rate-free min-max statement
and holonomy concentration are asserted above.

## Proposed periodic-rotor extension

Fix a finite periodic cubic box with L_i>=3, all plaquettes, four CAR
orbitals per site and a nonempty fixed total-number sector. Supply positive
electric/magnetic weights, a>0 and bounded number-preserving hopping/onsite
matrices. Use untruncated integer rotors for this argument. The preceding
Gauss reduction E=E0(f)+C n is valid on any connected graph; only the claim
that plaquettes generate all cycles changes with topology.

After Fourier transformation, theta belongs to T^c and

```text
H_g=(g^2/(2a))(C[-i partial_theta]+E0(f))^T W_E
                         (C[-i partial_theta]+E0(f))
    +V(theta)/(g^2 a)+H_matter(theta),
V(theta)=sum_p w_p[1-cos(z_p dot theta)],
K=C^T W_E C>0,   A=Z W_B Z^T>=0.
```

The flat manifold M={theta:z_p dot theta=0 modulo2pi for every p} is the
torus of flat connections modulo vertex gauge transformations. For this
periodic cubic complex, H_1=Z^3 makes M a connected three-dimensional torus.
It has a constant normal Hessian A and rank r=c-3. The gauge normal oscillator
has positive frequencies sqrt(lambda_+(K^(1/2) A K^(1/2)))/a, equivalently
the nonzero weighted curl frequencies. Write E_perp for half their sum and
e_M=min_(theta in M)lambda_min H_matter(theta).

**Proposed leading result:** for every fixed index j of the untruncated
periodic operator, E_j(g)->E_perp+e_M as g->0. This is a spectral floor and
accumulation statement, not the full photon/fermion excitation spectrum.

Proof strategy with quantitative local bounds:

1. The positive electric form is elliptic on the compact torus at fixed g,
so the operator has compact resolvent. Its charge-dependent constant
connection can be completed into the K metric plus a nonnegative longitudinal
constant. On each simply connected chart the connection is removed by a
componentwise scalar phase for lower kinetic estimates. Pointwise matter
eigenvalue bounds are unchanged by that phase.

2. Cover the flat torus with finitely many linear tubular charts and an
exterior region, and choose a smooth quadratic partition of unity. For
fixed chart width delta, the localization identity subtracts an electric
error bounded by C_delta g^2. Magnetic and matter terms commute with the
scalar partition. Outside a delta tube, V has a strictly positive lower
bound, so the exterior form exceeds any fixed energy for small enough g.

3. In a tube choose linear normal and tangent coordinates making the constant
kinetic metric block diagonal. This is possible by shifting the tangent
coordinate by a linear function of the normal coordinate; it leaves the
normal coordinates and V unchanged. On normal radius delta,
V is bounded below by (1-C delta^2) times its normal quadratic form. This
follows from the cosine Taylor remainder and finite fixed plaquette vectors.
The Dirichlet-localized normal kinetic/potential form is bounded below by
the full-space normal oscillator ground energy, multiplied by
sqrt(1-C delta^2). The remaining tangent kinetic term is nonnegative.
Continuity gives H_matter(theta)>=(e_M-C' delta)I in the tube. Combining
the partition gives liminf E_0>=E_perp+e_M after delta->0.

4. For the upper bound select a point of M minimizing the matter energy,
a fixed matter vector there, and j+1 orthonormal smooth tangent functions
supported in a small common chart about that point. Multiply them by the
normal oscillator Gaussian with width g, with a fixed compact normal cutoff.
The normal energy tends to E_perp; cosine quartic errors have size O(g^2)
for these Gaussians. Tangent electric energy and the fixed charge-connection
terms tend to zero. The finite matter matrix varies continuously, giving
energy at most e_M+o(1)+O(delta). Min-max and delta->0 produce the upper
limit for every fixed j. Infinite-dimensional tangent functions are what
permit arbitrary fixed multiplicity at the limiting floor.

This argument still needs a fresh proof review of the tubular coordinate,
localization and charge-connection estimates. It does not assume a gapped
matter band on all of M and does not derive the next-order Berry connection
or tangent effective Hamiltonian. Matrix degeneracies can matter at that
next order.

For fixed g>0, finite Fourier sums in the exact affine electric domain form
a core as S->infinity. Variational compression therefore recovers each
untruncated eigenvalue. This supplies an iterated S->infinity then g->0
comparison. No rate or sufficient joint S(g) is claimed for the periodic
extension. In particular this is not a proof at one fixed finite payload
uniform in volume and infrared scale.

## Consequence for the next campaign

The free matter input in a periodic weak-coupling comparator must include
global twists. A nonzero flat holonomy costs no plaquette magnetic energy,
so its matter energy cannot be discarded. The correct first question is
the twist-dependent fixed-volume matter energy and its minima; the next
question is the induced slow holonomy Hamiltonian and its volume dependence.
Neither a ring holonomy nor this proposed finite-volume spectral floor
establishes confinement, deconfinement, a Weyl charged pole, metric attraction
or selection of the native Hamiltonian by the framework axioms.
