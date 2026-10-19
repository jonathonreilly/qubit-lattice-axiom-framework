<!-- Original PR9810 source SHA256 938a726207718c0a295d7ad0f042f462b8566d9ed309d80a8894c84db7e22984. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Positive microscopic light-column readout window

Status: bounded-support. Fix even L>=6 and even R>2L on the periodic physical
one-qubit grid R by R by L. All limits in this theorem hold R,L fixed before
lambda->0. The native Hamiltonian and original bond readout are unchanged.
This derives a low-energy positive spectral window, not an isolated scalar pole.

## 1. Two finite-dimensional reductions

At lambda0, the wall-free N0 subspace is separated from N>=1 by an order-J
gap. Finite-dimensional analytic spectral perturbation therefore gives an
exact wall-free block unitary. Choose the real native word-preserving gauge
used in WHOLE_COLUMN_MODE_PROOF.md and COLUMN_READOUT_PROOF.md. Take its
expansion sufficiently beyond order L for the remainders below; at fixed
geometry no increasing-order or thermodynamic estimate is required.

On N0 all coefficients below orderL are diagonal in column configurations.
Below order4 they are scalar. The first nonconstant diagonal energy and first
offdiagonal energy are respectively

 D4=-J L lambda^4/128 sum_p P_p,
 K=-gamma_L T, T=sum_<ij>_xy Xbar_i Xbar_j,
 gamma_L=J c_L lambda^L, c_L=binomial(2L-2,L-1)/8^(L-1).

Here Xbar flips all L physical spins in a column. The leading original
uniform-source coefficients in the SAME unitary frame are

 C_diag=a D4, a=3/(J sqrt(V)),
 C_off=b K, b=A_L/(2J sqrt(V)), A_L=6(L-1)(L-2)/(2L-3),
 V=R²L.

Orientation-independent source terms are scalar and cannot create transitions.
The native connection cancellation at first winding order was checked in the
source proof; it is not omitted by convention. Higher diagonal energy and
source terms give relative O(lambda) changes to the leading lambda4 scale.
Plane symmetries equate their diagonal values throughout P0={all P_p=+1}.
The first K maps P0 into P4={exactly four bad plaquettes}.

Subtract the common coefficient vacuum scalar and divide the N0 Hamiltonian
by lambda4. The limiting diagonal operator has a positive fixed gap above
P0, and its P4 energy is d=JL/16. On a transverse torus each row/column has
even bad-plaquette parity; four is the minimum nonzero number. Other nonzero
counts start at least at six, separated from P4. Standard finite-dimensional
spectral projectors thus continue both clusters. This does not imply that
all continued P0 vectors remain exact ground states: higher-order splittings
can select any smaller ground space. The estimates below are operator estimates
uniform over directions in P0, so they cover every actual ground state.

Let Delta4=d lambda4. For sufficiently small lambda at this FIXED geometry,

 I_lambda=[0.9 Delta4,1.1 Delta4]

above actual Eg contains precisely the continued P4 cluster and excludes the
other clusters. The N>=1 block remains at order-J energy. No claim is made
about a single eigenvalue, a lifetime, or the internal dispersion of P4.

## 2. Ground-state mixing changes the source vertex

For a leading matrix element k=<e|K|g>, g in P0 and e in P4, the ground
admixture is -k/Delta4 and the corresponding excited admixture has the opposite
sign. The diagonal source difference is a Delta4. Consequently the actual
transition coefficient is

 b k-a k=(b-a)k.                                              (1)

Equivalently, the second block unitary transforms the source by a commutator
with its diagonal part. This is the ground/excited mixing of the lambda4-scaled
block, not the first unitary connection already checked above.

Uniformly for every actual ground vector mapped to a normalized v in P0,
its source image in the continued P4 cluster, after unitary identification, is

 -gamma_L(A_L/2-3)/(J sqrt(V)) T v+O_(R,L)(lambda^(L+1)).      (2)

Corrections from higher diagonal energies or source coefficients are relative
O(lambda). Further block mixing begins at relative order lambda^(L-4), which
is at most O(lambda²) for evenL>=6. Common scalars cancel from transitions.
Centering does not affect a strictly positive spectral window. The result is
not a perturbation of a chosen unique ground vector and requires no ground-rank
identification. The finite-dimensional remainders can be taken to sufficiently
high order before dividing by lambda4; all constants depend on R,L.

## 3. Exact edge isometry and positive original-source weight

Every adjacent column-pair flip creates four bad plaquettes, with no vertical
walls. It changes2L physical spins. There are2R² distinct undirected transverse
edges. Two different edge flips differ on at most four columns. A nontrivial
row/column sign pattern in P0 has Hamming weight at leastR>4, so no cross-edge
product connects two P0 configurations. Hence

 P0 T^dagger T P0=2R² P0.                                    (3)

This exact operator identity is independent of any coherent ground superposition.
Combining(2)-(3) gives the actual microscopic positive spectral weight

 W_0=<g|(C0-<C0>)^dagger 1_(H-Eg in I_lambda)(C0-<C0>)|g>
    =2 gamma_L²/(J² L)(A_L/2-3)²[1+O_(R,L)(lambda)]
    =18 c_L²/L [(L²-5L+5)/(2L-3)]² lambda^(2L)[1+O(lambda)].  (4)

The coefficient is positive for evenL>=6. Uniformity extends to every exact
ground density. This is a derived actual low-energy original-readout window:
its energy is of orderlambda4 and its weight of orderlambda^(2L).
The small coefficient is a result, not a fitted detector parameter.

## 4. Momentum-resolved source form factor

Let Qz=0 and a=x ory, with b the other transverse axis. The bare winding
source for an edge has the extra factor exp(-iQ.edgecenter)cos(Qa/2), because
its two columns contribute equally to each intermediate source difference.
The four-corner static source contrast of that domino, from the earlier
marked-square calculation, is

 a Delta4 exp(-iQ.edgecenter)cos(Qa/2)cos(Qa)cos²(Qb/2).

Thus ground mixing and bare source together give each edge amplitude

 -gamma_L/(J sqrt(V)) exp(-iQ.edgecenter)cos(Qa/2)
             [A_L/2-3cos(Qa)cos²(Qb/2)].                     (5)

Weighted versions of the orthogonality in(3) yield

 W_Q=gamma_L²/(J² L) sum_(a=x,y) cos²(Qa/2)
                  [A_L/2-3cos(Qa)cos²(Qb/2)]²
        +O_(R,L)(lambda^(2L+1)).                             (6)

The error is absolute. At Q=(pi,pi) the displayed leading term vanishes;
no relative-error or exact transverse-darkness statement follows there.
At Q0, (6) reduces to(4). At nonzero allowed Qz the entire window response
is exactly zero for sufficiently small lambda: N0 has Tz=I, translation
preserves the exact block, and every nontrivial longitudinal character is
separated by the wall gap. These statements specify spectral weight versus
probe momentum; they do not infer a dispersion from a source envelope.

## 5. Validation and interpretation

Exact column-bit controls enumerate all2048 P0 backgrounds atR6 and sampled
backgrounds atR8, checking edge-image orthogonality and four-plaquette count.
Explicit discrete Fourier sums over the bad plaquettes check(5). A derived
two-cluster matrix checks the subtraction b-a directly; it is an algebra
control, not a full-H numerical spectrum. The native winding and source
coefficients have separate rational Pauli/path and virtual-dressing controls.
Independent mathematical and physical checks cover the microscopic reductions.

For each arbitrarily large FIXED evenL the theorem supplies light neutral
weight from a many-spin winding feature, with no added interaction or oscillator.
There is no uniformity whenL grows withlambda^-p. In particular it is consistent
with the prior superalgebraic low-readout darkness in that different joint limit.
The excitation cluster may contain many split states and has no derived
three-dimensional propagating scalar interpretation. Hamiltonian, weak regime,
ground-state restriction, units and the identification of C with a physical
detector remain premises. No empirical calibration or independent observation
test has been performed, and no cosmological scale or universal matter coupling
is inferred from(4).
