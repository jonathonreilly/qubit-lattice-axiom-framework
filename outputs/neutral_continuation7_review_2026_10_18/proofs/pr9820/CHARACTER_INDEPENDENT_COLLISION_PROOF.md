<!-- Original PR9820 source SHA256 4dfe6b5f2f83d54985c8e49b86d0973046ced9846b8f353a7b166834b191bd6c. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Neutral collisions without a chosen plane character

Status: conditional-support. Trace: direct_blocker_closure (partial).
Proposal allowed: false. The narrow removed choice is the X/Y plane character
of the low-energy reference state for the specified invariant readouts. The
Hamiltonian, even R, height ten, weak coupling, low-energy preparation and
measurement identification remain premises. There is no cosmological initial
state or generic thermalization derivation.

## Exact flat-space algebra

In the wall-free column space write a flat configuration as f_xy=a_x+b_y over
F2. Row and column flips form a group G with 2^(2R-1) elements; the product of
all row flips equals the product of all column flips. Let X_A flip the set A
of columns. Its group orbit on the all-aligned configuration is free.

At L=10 a whole Y column equals -Xbar in the aligned column doublet. A Y plane
contains even R columns, so the sign is +1. Physical X/Y planes therefore
implement the two group-generator families without extra phases. Every flat
configuration has positive Z-plane eigenvalues, since its number of reversed
columns is R sum a+R sum b modulo two. Compatible X/Y characters chi obey the
same one product relation as G. The normalized Fourier vectors

    |Omega_chi> = |G|^(-1/2) sum_(g in G) chi(g)|g>

span the flat space, with one vector in each compatible character sector.
These labels are physical symmetries; no gauge quotient discards their states.

A group element toggling a rows and b columns has weight
 a(R-b)+(R-a)b. Every nonidentity element has weight at least R. For a column
Pauli word X_A Z_B, direct orbit summation gives

    <Omega_chi|X_A Z_B|Omega_chi>
      = 1_[A in G] 1_[B in G_perp] chi(A).

Here B in G_perp means even overlap with every generator, precisely the
invariance of the Z word under those plane flips. Consequently an invariant
word with |A|<R compresses to the SAME scalar on the entire flat space.
The only surviving A is zero. This is stronger than equality of diagonal
energies and weaker than state independence for arbitrary observables.

For two-column orbit states |T;chi>=X_T|Omega_chi>, |T|=2, the matrix element is

    <T';chi|X_A Z_B|T;chi>
      = (-1)^(B dot T) 1_[T' xor A xor T in G]
        1_[B in G_perp] chi(T' xor A xor T).

If |T'|+|A|+|T|<R, the group element in this expression must be zero.
Thus the matrix element is independent of chi. Distinct unordered two-column
sets are orthonormal within each character for R>4; distinct characters are
orthogonal by symmetry. Coincident columns represent the vacuum and are not
included in this pair basis. The support bound counts flipped columns, not
just the diameter of an operator's support.

The exact control enumerates G for R=4,6,8, checks its minimum nonzero weight,
and directly sums 3072 finite-orbit matrix elements against the formula.
It also preserves two sharp limitations: a whole-row X word distinguishes
characters at support R, while a single noninvariant Z distinguishes a
classical flat configuration from character states. Nothing here makes all
local observables or arbitrary preparations equivalent.

## Uniformly dressed sector vacua

Use the equivariant local normal forms in
[POLYNOMIAL_GRID_NEUTRAL_POLE_PROOF.md](POLYNOMIAL_GRID_NEUTRAL_POLE_PROOF.md).
All generators can and do preserve the physical plane symmetries. At any
fixed final order M, their retained connected words have a bounded number
s_M of flipped columns, independent of R. Eventually R>s_M+4 in every fixed
polynomial-volume limit. Their Q0 compression is the same scalar in every
character, and the Q0 rank in each compatible sector is one.

The inherited relative positivity excludes lower states with defects or
walls: in this low-energy window the Q gap is at least c J lambda^4, while
walls have an order-J cost. The final norm remainder is C J R² lambda^M,
uniform across characters. Hence each compatible character sector with
positive Z planes has a unique lowest state in this window, with energy

    E_chi = e_M + O(J R² lambda^M),

and its dressed flat vector differs in norm by O(R² lambda^(M-4)), after
choosing its phase. These bounds use the rank-one sector projector and the
defect gap. They do not sum over the exponentially many characters; a direct
sum of uniformly bounded blocks has the maximum block norm.

These states need NOT all be exact global grounds. The earlier reflection
argument supplies a global ground in the positive character. Other character
vacua can be split by wrapping processes beyond any fixed retained order in
the polynomial limit. Their near-degeneracy alone is not the locality proof;
the exact orbit matrix elements above are essential.

## Same native collision for every character

Apply the pair-channel reductions in
[NATIVE_PAIR_SCATTERING_PROOF.md](NATIVE_PAIR_SCATTERING_PROOF.md) to the whole
two-column space before restricting its defect-coordinate center motion.
The local diagonal coefficients and winding moves are plane invariant.
The fixed-Q relative bounds and the uniform shape gaps are independent of
chi. At fixed order, compositions and denominators remain supported on a
bounded set of column flips; they cannot realize a complete nontrivial flat
row when R>s_M+4. Therefore the same derived collision generator acts in every
character block, up to the uniform already stated remainder.

In particular the core F, three boundary ratios, finite-integral scattering
scale and finite-time signal are unchanged. For a generic chi a physical
translation changes the character pattern. There is then NO exact physical
momentum fibre within that sector. The construction instead uses the identical
defect-coordinate pair basis and a uniform center superposition in that basis.
Its leading local generator is translation invariant in those coordinates;
possible wrapping effects are bounded by the remainder. No exact microscopic
zero-momentum label is assigned to a generic character vacuum.

In the matched representation one may write, to the controlled order,

    H_pair = e_M I + I_character tensor H_collision + remainder.

The same statement holds for the invariant preparation/readout operators.
Thus the character label is a spectator for this experiment. For
k=lambda^(1/4), T=k^-3 and R~lambda^-1, the collision signal still obeys

    ||(S-I)f_k|| ~ 4pi/log(1/lambda),

with the earlier algebraically smaller errors. Possible differences of the
sector vacuum energies contribute at most O(lambda^(M-51/4)) over this physical
time, already within the remainder. The projector-matching error
O(lambda^(M-6)) at R~lambda^-1 is also smaller when M>=20.

An arbitrary mixture of compatible sector vacua gives the same invariant
collision statistics to this accuracy. So does a coherent superposition,
provided the same matched packet is prepared in every occupied character:
exact symmetry makes the readout block diagonal, while the coefficient
collision operator is the same in every block. Character coherences cannot
contribute cross terms to these invariant observables. This does not cover
initial correlations with different packets in different sectors, arbitrary
noninvariant readouts, or states outside the prepared low-energy manifold.

## Assumption movement and boundary

The all-positive X/Y character is no longer needed for this neutral collision
observable. No averaging measure over characters, environment-selected sector,
or additional interaction was supplied to obtain the result. Positive Z-plane
restriction and the low-energy reference manifold remain. Preparation of that
manifold, cooling across exact symmetry sectors, the choice of microscopic
Hamiltonian and scales, and a physical detector/environment map are still open.
This is an operational removal of one state-selection import, not a derivation
of the universe's state or of universal scalar gravity.

## Low-temperature preparation without selecting a character

A further conditional extension uses the full Gibbs state of the SAME physical
Hamiltonian, not an imposed character projection. Write U H U^dagger=B+R_M,
with delta=||R_M||<=C J R^2 lambda^M and the global block bounds inherited
from the normal-form proof. B commutes with N and with Q inside N=0. For
sufficiently large R at fixed order, its flat block P has dimension
G=2^(2R-1), B P=e_M P, and

    B|_(N=0,Q=q) >= e_M + g q,   g=c J lambda^4,
    B|_(N>=2) >= e_M + J.

These require global form bounds, not only a few-defect norm estimate. The
column-to-plaquette syndrome map is linear over F2, with kernel the flat flip
group. Each admissible syndrome has G preimages. Hence

    dim(N=0,Q=q) <= G binom(R^2,q).

The Gibbs nonflat weight w_B therefore satisfies

    w_B <= (1+exp(-beta g))^(R^2)-1
           + 2^(10R^2) exp(-beta J)/G.

The flat conditional Gibbs state is exactly P/G for the retained B; no exact
flat-band degeneracy of H is asserted. Its trace distance from the full
B-Gibbs state is 2 w_B. Noncommutativity of R_M causes no problem: the relative
entropy identity and |log Z_H-log Z_B|<=beta delta give

    D(rho_(B+R_M)||rho_B) <= 2 beta delta,
    ||rho_(B+R_M)-rho_B||_1 <= 2 sqrt(beta delta).

The second inequality is quantum Pinsker with natural logarithms. Unitary
invariance and the triangle inequality consequently yield

    ||rho_H-U^dagger(P/G)U||_1 <= 2 w_B+2 sqrt(beta delta).

At R~lambda^-1 and beta g=a log(1/lambda), a>2, the wall entropy is dominated
by beta J~lambda^-4 log(1/lambda), and

    error = O(lambda^(a-2))
          + O(lambda^((M-6)/2) sqrt(log(1/lambda)))
          + superpolynomially small terms.

For a=10 and M=20 this is O(lambda^8)+O(lambda^7 sqrt(log(1/lambda))),
smaller than the neutral collision signal. The SAME trace-preserving matched
preparation channel and bounded-outcome measurement contract this error.
Normalized postselection is not covered without a success-probability bound;
unbounded observables require their operator norms in expectation bounds.
The channel is an operational assumption, not a newly derived physical device.

This replaces selecting a pure character vacuum by an adopted low-temperature
condition. It does not derive thermalization, cooling, the inverse temperature,
or cosmological formation. Exact isolated unitary dynamics cannot itself
change the Gibbs temperature. No bath or new interaction has been inserted.
