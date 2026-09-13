# Native realization needed for the response theorem

This reconstructs only the finite-range placement and occupation dictionary
used by BLOCK07; it does not import the unmerged common-frame PR's broader
geometric or approximation conclusions. The vertex functions, node jets,
connection expansion and response proofs are specified again in this block.

The current-main source
docs/NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md
at b8c9d9d819911c5f3fec98b23d53355e7ff8c8bf, Theorem 1, supplies the
conditional ordinary-tensor edge-qubit cycle code. Its dictionary is

    B_v=product_(e incident v) Z_e=1-2 c_v^* c_v,
    A_vw=-i gamma_(2v) gamma_(2w),
    gamma_(2v)=c_v+c_v^*.

For an ordered simple path p from v to w of length l, canceling the internal
Majoranas gives A_p=i^(l-1) product_p A_e=-i gamma_(2v) gamma_(2w). Thus

    T_p=i A_p(B_v-B_w)/2=c_v^*c_w+c_w^*c_v,
    J_p=-A_p(1-B_v B_w)/2=i(c_v^*c_w-c_w^*c_v).

Both real and imaginary hopping coefficients are therefore finite physical
operators. A cell's n_x is the sum of its two bounded-star occupation
projectors. It is not a single physical edge-Z event. The unaugmented finite
code represents even total fermion parity; choose an even number of cells
for a half-filled state. The 60-cell position checks obey that restriction,
and the thermodynamic argument can use even-volume sequences.

Place orbital r in {0,1} of cell x at virtual v=(2x1+r,x2,x3), with actual
edge qubits at doubled virtual-edge centers as in the source. Protect every
x,z edge and the y edges whose lower-y tail has even x+y. Each unprotected
y edge has a protected x-plaquette detour. The trigonometric frame vertices
in BLOCK07 have only these path types:

| Symbol contribution | Orbital action | Protected path length |
|---|---|---|
| sigma1/2 sin k1 | Flip orbital, one x cell | At most 3 |
| sigma1/2 sin k2 | Flip orbital, one y cell | 2, choosing the x/y ordering |
| sigma1/2 sin k3 or sin 2k3 | Flip orbital, one or two z cells | At most 3 |
| sigma3 sin k3 sin k1 | Same orbital, x and z cell displacement | 3 |
| sigma3 sin k3 sin k2 | Same orbital, y and z displacement | At most 4, with an x detour if needed |
| sigma3 cos k3, scalar sin k3, or on-site terms | Same orbital | At most 1, or the occupation star |

The flat Wilson cos k1 term uses two x edges; cos k2 uses either one
protected y edge or a three-edge x detour; cos k3 uses one z edge. These
statements hold on the infinite graph and on open boxes with enough x width
to take an inward detour. A periodic Fourier regulator is an auxiliary
operator computation, not a short physical wrap edge in an open box.

Record compatibility is only the current-main conditional one: on a
surviving cycle the physical Z projector has a fair isometric restriction,
and every surviving even word intertwines it. A prepared initial code,
ordinary quantum composition, Hamiltonian, state and Born interpretation
remain supplied. This note supplies no formation rate, autonomous control,
strict nearest-neighbor admissibility distribution or axiom-selected metric.
