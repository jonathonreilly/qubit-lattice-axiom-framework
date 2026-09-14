# Hard temporal-penalty limit: an integer-flux bridge

Personal working continuation of BLOCK14_MONOPOLE_KINETIC_DERIVATION.md.
This is a direct carrier/operator mapping with boundary qualifications,
not an independently reviewed result or a photon-phase proof.

As mu_t->infinity, a link move survives precisely when its branch mismatch
m_p vanishes on every incident plaquette. In the surviving moves,

    b' = b + sigma F e_l

as an equality of integers, with each entry staying in {-1,0,1}. Therefore
D b, the integer cube divergence, is exactly conserved because D F=0.
Here D is the cube-face incidence matrix. In contrast, the finite-mu_t
Hamiltonian conserves this divergence only modulo3 in general. For every
finite volume the difference of the two electric Hamiltonians obeys

    ||H_mu-H_infinity|| <= 2t |E| exp(-mu_t),

since each removed move has at least one nonzero integer mismatch, and
symmetric row sums bound the norm. More usefully, the difference is a sum
of bounded local terms of norm at most2t exp(-mu_t) per original link.
An extensive norm bound alone does not prove stability of a gapless phase.

On a contractible cell complex with trivial first and second cohomology,
physical Z3 link states have a flux basis indexed by b in {-1,0,1}^P
satisfying D b=0 modulo3. This follows from the finite cellular cochain
complex: the kernel of the flux map consists of gauge gradients, and every
closed face cochain is exact. If the domain has boundary conditions or
nontrivial topology, the corresponding relative complex and global
holonomy/flux data must be retained; they are not silently discarded.

Restrict the hard-limit Hamiltonian to the invariant integer sector D b=0.
Identify b_p with the electric quantum number -1,0,1 of a spin-one register
on the corresponding dual link. Let E+|-1>=|0>, E+|0>=|1>, E+|1>=0,
and E-=(E+)*. These are normalized shifts, equal to the usual spin-one
raising/lowering matrices divided by sqrt(2). A surviving original-link
move is the product of E+ or E- on its incident faces, with exponents
specified by sigma F_pl. In the bulk these faces make one dual plaquette.
Thus the kinetic operator is exactly a sum of dual plaquette flips on a
divergence-constrained spin-one carrier. Boundary original links produce
the explicitly corresponding shorter dual-boundary terms; a periodic
model additionally needs the global flux restrictions just described.

The diagonal Wilson potential becomes exactly

    K [1-cos(2pi b_p/3)] = (3K/2) b_p^2.

The spatial monopole penalty vanishes in the D b=0 sector. Hence this
restricted Hamiltonian has the standard finite-electric-range form of
an integer gauge quantum-link model, with the stated normalization and
topological restrictions. It is not the two-state ice model of PR8117,
and no theorem for that model transfers without a new hypothesis check.

The finite check uses one full cube: 12 original links, 8 vertices and
6 oriented faces. There are 3^5=243 physical mod3 flux states and141
integer-divergence-zero states. An independent tensor-product shift
construction on six spin-one registers agrees with the restricted hard
Hamiltonian. The check also retains finite-penalty integer-charge changes
and verifies the exponential local-rate/norm comparison.

The next scientific question is now concrete: establish a Coulomb phase
in this particular hard-limit sector, then control finite exp(-mu_t)
perturbations and finite spatial monopole penalty in the correct infinite
volume order. The mapping does not establish either stability statement.
A hard-limit emergent conservation law is not an approved native axiom.

The integer-neutral sector is an invariant sector of the hard model, not
a proved choice of its global ground state at a volume-independent lambda.
A simple finite-box sufficient bound illustrates the distinction: if
lambda>2t|E|, every sector with at least one nonzero cube charge has energy
at least lambda, whereas the zero-flux basis vector has expectation2t|E|.
This uses positivity of the electric summands and K>=0. It selects the
neutral sector on that box, but the displayed threshold grows with volume
and is therefore not a phase-selection theorem at fixed couplings.

For fixed box, fixed T and nonnegative V_spatial, the hard-penalty and
time-step limits can be compared in operator norm: the transfer remainder
in the kinetic note is uniform for mu_t>=0, and Duhamel gives

    ||exp(-T H_mu)-exp(-T H_infinity)||
       <= T ||H_mu-H_infinity|| <= 2Tt|E| exp(-mu_t).

Combining the two bounds proves commutation of these two limits at fixed
box and time. The extensive bound still supplies no interchange with the
thermodynamic or infrared limits. This is the exact boundary of the mapping.

A useful variational check prevents importing the earlier frozen-ice wall
into this different Hamiltonian. Assume every active original link has
nonzero face curl, and choose one link incident on r faces. In the neutral
sector, b=0 and b=F e_l are both allowed and connected with amplitude at
least t. Their diagonal energies, after the common constant2t|E|, are
0 and (3K/2)r. A two-state trial subspace therefore gives

    E_ground <= 2t|E| + 3Kr/4 - sqrt[(3Kr/4)^2+t^2]
             < 2t|E|.

The off-diagonal amplitude can be larger if multiple original moves have
the same flux action, which only improves this upper bound. In contrast,
a frozen flux basis vector, annihilated by every nontrivial hopping term,
has energy at least2t|E| for K,lambda>=0. Thus such frozen basis vectors
cannot be global ground states of this specified hard Hamiltonian when
t>0 and finite K. Disconnected mobile components, gaplessness and the
infinite-volume neutral-sector question are not settled by this trial.
The earlier ice wall used a different diagonal interaction; its conclusion
must not be transplanted merely because both models have plaquette flips.
