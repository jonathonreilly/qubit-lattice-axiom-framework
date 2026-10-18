# All-height prepared assisted vertex: focused check

PASS conditional on the separately checked canonical coefficient a_L=2^{-(L-2)} and the stated order-three cancellation. No lower-order diagonal contamination or competing background-changing output is forced by the native symmetries. This check is for fixed admissible transverse box and fixed even longitudinal L>=6, followed by lambda tending to zero; it is not uniform in L or transverse size.

## Exhaustion of background-changing outputs

Consider a nearest x hop i to j of a singleton at the same longitudinal layer. Let A be the set of columns whose background signs differ between initial and final canonical majority labels. Conservation of each longitudinal plane parity forces |A| even. For this output the number of physically changed spins is

    |A| L + 2 - 2 |A intersect {i,j}|.

Each native transverse insertion changes two spins. Consequently a nonempty background change needs at least L-1 insertions, and equality is possible only for A={i,j}. Any other pair A needs at least L insertions; four or more changed columns require still more. At equality the physical changes occur on the edge (i,j) at every layer except the singleton layer, so the minimal process is precisely the asserted complementary open-column path family. This establishes uniqueness of the E_edge background output at that order, independently of its separately evaluated coefficient.

For empty A, the parity of the number of inserted bonds is fixed by the number of flipped spins on one transverse sublattice. A nearest hop has odd parity, while an even-L full-column reversal does not change it. Thus only odd orders contribute to this nearest-hop block. This requires the declared even, bipartite transverse geometry.

## Diagonal terms and the true vacuum

A background-diagonal coefficient multiplying a nearest x hop is invariant under the native row/column plane transformations. For x-plane X flips there is no singleton phase; for y-plane Y flips the singleton phase is the same at i and j because their y coordinate agrees. Hence the diagonal coefficient is constant on the flat-plaquette orbit P0, including arbitrary superpositions in P0. This is the relevant symmetry argument; mere locality by itself would not imply the assertion.

Write D_j P0=d_j P0 for such a coefficient. For a normalized actual vacuum-block ground g_lambda with ||(I-P0)g_lambda||=O_(R,L)(lambda^(L-4)),

    ||(I-|g_lambda><g_lambda|)D_j g_lambda||
      <= 2 ||D_j-d_j I|| ||(I-P0)g_lambda||.

The order-one and order-three diagonal terms in the stated canonical block are scalar on the entire background space, so their centered contributions vanish exactly. The first potentially nonconstant diagonal term is order five; its centered contribution is therefore O_(R,L)(Jlambda^(L+1)). All later diagonal terms are smaller. Thus weak vacuum admixture does not produce an earlier prepared vertex.

The vacuum estimate uses the order-lambda^4 gap from P0 to bad plaquettes, diagonal higher terms preserving P0, and the first background-changing vacuum term at order L. It does not require selecting a particular limiting vector inside the possibly degenerate flat subspace. One may define g0(lambda)=P0 g_lambda/||P0 g_lambda|| and make the statement uniformly for these vectors. A limit of g0 need not be assumed.

## Neutral-window weight

For any normalized flat vector g0, E_edge g0 has exactly four bad plaquettes, is orthogonal to P0, and has norm one (E_edge is an involution). In the stated geometry its leading vacuum-background excitation energy is Delta4=JLlambda^4/16. Finite-box perturbation places this whole leading four-bad-plaquette component in the corresponding neutral window Delta4[1+O_(R,L)(lambda)]. Mixing and projection corrections are higher order at fixed R,L.

With matching preparation/readout and centering against the actual vacuum background, the leading projected nearest-hop vertex is therefore

    -J 2^{-(L-2)} lambda^(L-1) E_edge g0,

and its window weight is

    J^2 2^{-2(L-2)} lambda^(2L-2) [1+o_(R,L)(1)].

The conservative relative O_(R,L)(lambda) form is also consistent with analytic fixed-box corrections. No extra degeneracy or background-dimension factor occurs. The four-bad-plaquette statement requires nondegenerate transverse edge/plaquette conventions and a sufficiently large box so that the specified flip really changes four distinct plaquettes; retain the geometric assumptions of the inherited fixed-height winding proof.

## Gauge and interpretation

This conclusion refers to the exact declared canonical N2 block and its matching canonical N0 background identification. Arbitrary intra-block gauge changes can redistribute the vertex; simultaneous transformation of prepared states and readout leaves the matrix element invariant. A numerical or symbolic coefficient in another effective gauge is not transferable without this matching. Higher-order canonical completion does not alter already fixed lower coefficients, but any explicit order-L-2 intra-N2 rotation must be tracked because it can modify an order-L-1 hopping coefficient.

The neutral-window energy is the spectrum of the prepared vacuum background Hamiltonian. It is not automatically the energy of an outgoing eigenchannel of the full heavy Hamiltonian, which acts on particle and environment together. This is a prepared background-channel infinitesimal Hamiltonian vertex, not a scattering rate, decay width, relaxed-heavy response, or bare-preparation result. No uniform joint large-L/weak-lambda conclusion has been established here.
