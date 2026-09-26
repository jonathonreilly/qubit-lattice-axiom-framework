# Coherent dimer permutations and the literal qubit state-space question

2026-09-21. Root conditional construction and exact finite countercontrols.
Independent review is pending. This note tests a particular proposed bridge;
it neither excludes other quantum realizations nor derives a photon.

## 1. An orthogonal configuration lift does have the dimer Hamiltonian

Fix a graph with V=2K sites and K distinct permanent antipodal record keys.
At full packing, a marked configuration eta specifies every unchanged record's
position, with partners adjacent. Its unmarked matching is M. Each matching
has F=2^K K! such marked configurations. Introduce, as an **additional**
construction, the Hilbert space with orthonormal basis |eta>.

For a flippable unit square p, R_p rotates its four whole records one corner
clockwise. On a nonflippable configuration set R_p=I. This is a permutation,
R_p^4=I, and commutes with the flippability projector P_p. Every actual
displaced record takes one nearest-neighbor step and keeps its content.
The proposed Hermitian configuration-space Hamiltonian is

    H_mark = sum_p [v P_p - (t/2) P_p(R_p+R_p^dagger)].       (1)

The map

    U|M> = F^(-1/2) sum_(eta over M) |eta>                   (2)

is an isometry. Each R_p bijects the complete fiber over a flippable M with
the complete fiber over its geometric flip. Therefore

    H_mark U = U H_QDM,                                    (3)

where H_QDM has diagonal v times the number of flippable squares and
off-diagonal -t per geometric square flip. Multiplication by any geometric
observable also intertwines under U. Equations (2)-(3) are exact within
the supplied orthogonal configuration Hilbert space, for every finite graph
with the declared square moves. Multiple squares/channels are counted.

This is a positive algebraic bridge under its assumptions. The bare local
possibility algebra M_2(C) and the classical birth/transport rules do not
already supply that orthogonal Hilbert space, Hamiltonian, or preparation.

## 2. Classical lumping does not prepare the coherent fiber

One marked square orbit has four distinct states, with geometry alternating
between even and odd orbit positions. Let R be the four-cycle and
H=-(t/2)(R+R^dagger). Starting in one definite even state, the probability
of the other geometry after time tau is

    P_definite(odd) = (1/2) sin^2(t tau).                   (4)

The uniform incoherent mixture of the two even states has the same value.
Starting in their normalized coherent sum instead gives

    P_coherent(odd) = sin^2(t tau),                        (5)

the two-state QDM answer. At t tau=pi/2 the probabilities are 1/2 and 1.
The exact symbolic propagator checks both equations. Going around a closed
geometric flip path can permute actual record identities; the uniform fiber
is a particular coherent sector, not an automatic result of forgetting IDs.
The full square fiber consists of several such orbits, with the same issue.

In particular, a classical distribution uniform over completed matchings
does not by itself specify a coherent equal-amplitude vector or its phases.
The formation theorem cannot be substituted for this missing preparation.

## 3. The literal tensor-qubit map is nonorthogonal

Choose one normalized spinor for each record projector and define

    V|eta> = tensor_(sites x) |n_(eta(x))>,   G=V^dagger V. (6)

Here V denotes a linear map, not the number of sites. This proposed product
map is not an isometry. On a four-site square, take keys along the z and x
axes, with spinors (1,0), (0,1), (1,1)/sqrt(2), (-1,1)/sqrt(2).
The states with record labels (0,1,2,3) and (2,1,0,3) have distinct geometric
matchings and product-state overlap 1/2. The sixteen-column Gram matrix has
rank 11. Under the normalized uniform-fiber lift (2), its two-dimensional
Gram matrix is exactly

    U^dagger G U = [[1,1],[1,1]].                          (7)

Those two particular coherent geometry vectors collapse to the same
physical vector. This collapse is not universal: replace the x-axis pair
by (3/5,4/5), (-4/5,3/5), and the exact fiber Gram matrix becomes

    [[674/625,1],[1,674/625]],                             (8)

which has rank two but is still nonorthogonal. The marked configuration
space also quickly exceeds the literal tensor-qubit dimension: a six-site
ladder has 144 marked states versus dimension 64; a cube has 3,456 versus
256. Dimension alone does not rule out a smaller coherent sector.

There is a sharper necessary compatibility test for (1) and (6). If a
Hermitian physical operator satisfied H_phys V=V H_mark, then multiplying
by V^dagger and taking adjoints would give

    G H_mark = H_mark G.                                 (9)

For the ladder with edges 01,12,34,45,03,14,25 and square orders 0143,1254,
choose the three antipodal key axes z,x,y and t=1. Exact entries of the
commutator in (9), in the checker's declared enumeration, are:

| v | row, column | exact entry |
|---|---|---|
| 0 | 0,48 | -5/16-i/16 |
| 1 | 0,104 | 1/2 |
| 2/3 | 0,104 | 1/3 |

The corresponding configurations and all spinor phase conventions are
recorded in the checker and result. These entries show failure for the
specified Hamiltonians and product map. They do not exclude different
Hamiltonians, overlap-corrected effective operators, different coherent
sectors, or other record-to-quantum bridges. A change of representative
spinor phases must transform the proposed configuration Hamiltonian
consistently; it is not a license to identify different models unnoticed.

Unconditional physical permutations of tensor factors are well-defined
unitaries and obey their own Gram consistency. Conditioning the permutation
sharply on this nonorthogonal geometric label is the extra operation that
needs justification. Unconditional permutations also need not preserve the
nearest-neighbor antipodal-matching domain.

## 4. What the established quantum-dimer literature would add

Moessner and Sondhi's cubic quantum-dimer analysis uses an orthogonal dimer
space. At the Rokhsar-Kivelson point its equal-amplitude state relates
diagonal correlations to the classical matching ensemble, but its soft
dispersion there is quadratic. Their neighboring Coulomb-phase effective
action has a linear transverse mode when the curl-squared stiffness is
positive. This is a relevant phase mechanism, not a theorem transferred to
our record process by the similarity of its matchings.
[Primary paper, pinned v1](https://arxiv.org/abs/cond-mat/0307592v1).

Raman, Moessner and Sondhi address nonorthogonal valence-bond states through
overlap orthonormalization and controlled spin-model constructions. Their
additional interactions and decorated lattices illustrate a possible
different route, with premises that have not been supplied or checked for
permanent records here.
[Primary paper, pinned v2](https://arxiv.org/abs/cond-mat/0502146v2).

Neither external proof is imported as a native theorem. Bibliographic
identities, pinned PDFs and the exact sections read are recorded externally
in `physics-sync-2026-09-21-second/literature/QUANTUM_DIMER_SOURCE_RECEIPT.json`.
Those third-party files are not publication artifacts. The algebra above
does not depend on either paper.

## 5. Reproduction and next decision

`geometric_quantum_lift_check.py` verifies the integer form of (3), including
all marked configurations and both senses, on the square, ladder and cube.
It checks 32, 384 and 18,432 local channels respectively. It computes (4)-(8)
and the exact witnesses to (9); a floating-point search only selects an
entry before exact rational/complex verification. Source identities and
complete results are in `geometric_quantum_lift_checks/RESULTS.json`.
The first run completed with empty stderr. These are author controls,
pending separate scrutiny, not an operational quantum realization.

The useful next question is what physically justified quantum carrier and
preparation the records permit. Assuming orthogonality and coherence would
answer that question by adding the missing premises. The classical local
transport route remains available separately and must be tested on its own
state and field observables.
