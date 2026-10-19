<!-- Original SHA256 76b8e51ee20610585eecf253517047798ea1e03e0e6c77262caa13a7d7e5d9c8 -->
**Provenance boundary:** Complete original source follows. Historical review labels and execution narratives are provenance, not fresh verification or current audit authority. Mathematical arguments retain their explicit hypotheses.

# An exact nonstationary two-excitation code with permanent plane records

2026-10-18. Unpublished constructive research result; independent check pending. No physical axiom, selected native phase, audit verdict, gap or novelty claim. Main-source conventions are those already read at `584755767deb8dfb670f07211d8446873fd0999b`; no repository source changed. This proves a positive n=2 family, not maximality of the entire invariant dark subspace.

## Result

On the unchanged homogeneous nearest-neighbour Heisenberg Hamiltonian on

    C_4 x C_L x C_M,  L even and L>=6, M>=3,
    H=J sum_{ordinary edges} sigma_v.sigma_w, J nonzero,

there is an explicit M^2-dimensional **two-excitation** invariant code in which every physical qubit in the planes x=0 and x=2 remains exactly up for all time. Inside this code, two independent periodic one-dimensional hopping degrees of freedom evolve nontrivially. All edges have the same J. No penalty, bath, measurement, auxiliary qubit, omitted edge or PHP generator is introduced.

The code requires a supplied correlated initial preparation: two mirror-pair singlets separated by two y rows, with staggered coherent translation in y. It does not follow from generic reflection parity, and it does not implement the earlier arbitrary-input operation W. It removes the compression supplier only for persistence of these already prepared local records and these encoded live inputs. Loading, formation, readout identification and native selection of the Heisenberg dynamics remain open.

## Physical states and normalization

Use |up> as the chosen q direction; simultaneous internal rotation gives any common unit q without changing H. There are N=4LM physical qubits, degree6, |E|=3N, and the all-up product Omega has exact energy

    E0=3JN=12JLM.

At each transverse cell i=(y,z), the live mirror pair consists of sites (1,y,z) and (3,y,z). Define normalized states

    |t>_i=|up up>,
    |s>_i=(|down up>-|up down>)/sqrt(2).

Let |i,j> mean the physical state with singlets at distinct live cells i,j, t at every other live cell, and up on all record-plane qubits. These states are orthonormal when their unordered occupied-cell sets differ. Each has exactly two physical spin flips relative to Omega.

For z,w in Z_M define

    B|z,w> = (1/sqrt(L)) sum_(y in Z_L) (-1)^y
                     |(y,z),(y+2,w)>.                         (1)

For L>=6 the unordered cell pair in each summand has a unique orientation with forward row separation2: a reverse orientation would require 4=0 modulo L, excluded here. Thus different (y,z,w) label different configurations. It follows that B is an isometry from C^M tensor C^M into the original full spin Hilbert space. The two logical coordinates are ordered by this orientation even though the two singlet excitations themselves are indistinguishable.

No singlets in (1) occupy neighbouring transverse cells: their y separation is2, with cyclic minimum at least2. Their z values may coincide. This absence of adjacent occupied cells is used by the full-spin proof, not imposed afterwards by projection.

## Full-Hamiltonian proof

### 1. Every x bond and every record-only bond is retained

For each cell i, its four x bonds join the two record sites x=0,2 to both live sites x=1,3. Their sum is

    J (sigma_(0,i)+sigma_(2,i)).(sigma_(1,i)+sigma_(3,i)).

On a singlet, the live sum annihilates the state exactly. On t with both record qubits up, all four bonds have energy J and the state is unchanged. Thus replacing t by s changes the x-bond energy by -4J, with no record excitation. Two singlets contribute -8J relative to Omega from these bonds. Record–record bonds in the y,z directions act on up/up and keep their original J energy. The records are not discarded or compressed.

### 2. Exact two-cell transverse action

For adjacent transverse cells i,j, both live layers contribute the physical operator

    h_ij=J[sigma_(1,i).sigma_(1,j)+sigma_(3,i).sigma_(3,j)].

Directly using sigma.sigma=2 SWAP-I gives

    h_ij |t,t> = 2J |t,t>,
    h_ij |s,t> = 2J |t,s>,
    h_ij |t,s> = 2J |s,t>.                              (2)

These are full physical identities, not projected matrix elements. An adjacent |s,s> does not satisfy a closed two-state rule; it can leave the t/s code. The construction never starts a term with such adjacency.

For any |i,j> in (1), the two occupied cells are nonadjacent. Each has four transverse neighbours, so exactly eight distinct transverse edges have one s endpoint and one t endpoint. Relative to Omega, (2) supplies -2J on the diagonal for each such edge and +2J for each allowed singlet hop. Therefore

    (H-E0)|i,j> = -24J |i,j>
                 +2J sum_(i'~i) |i',j>
                 +2J sum_(j'~j) |i,j'>.                (3)

The -24J is -8J from x bonds and -16J from transverse edges. All terms in (3) still have pure up records. Some y hops have adjacent singlets; those amplitudes must cancel in the superposition before any claim of invariant dynamics is valid.

### 3. Complete cancellation of y hops

For clarity define the possibly unnormalized physical vector

    W_d(z,w)=sum_y (-1)^y |(y,z),(y+d,w)>.

Only d=2 is used for input. Applying the four y-direction hops to W_2 produces:

- first singlet moves +y: after reindexing y'=y+1, contribution -W_1;
- second singlet moves -y: contribution +W_1;
- first singlet moves -y: after reindexing y'=y-1, contribution -W_3;
- second singlet moves +y: contribution +W_3.

The sums cancel as exact physical vectors. Reindexing preserves the sign because L is even. This remains valid when W_3 has repeated unordered representations, as at L=6: its two identical formal vector sums cancel before any basis independence is invoked. The potentially adjacent-singlet W_1 terms cancel too. No constraint is imposed on z,w, so the cancellation holds for every encoded input.

### 4. Remaining z hops and exact intertwining

z hops keep the row separation2, so every surviving state remains of the form (1). Let A_M be the simple cycle adjacency, A_M|z>=|z-1>+|z+1>, with indices modulo M. For M>=3 these are distinct neighbours. Equations (1)–(3) give the exact full-space intertwiner

    H B = B H_code,
    H_code=(E0-24J)I+2J(A_M tensor I+I tensor A_M).       (4)

Since H_code is Hermitian and B is an isometry in finite dimension, its range is an invariant (indeed reducing) subspace of H, and

    exp(-itH)B = B exp(-itH_code) for all real t.         (5)

This is the full-H proof of persistence, including every record and live interaction. The physical scalar E0-24J remains in (4)–(5). It is not removed from the actual unitary.

## Dynamics, records and passive references

The eigenvalues in the code are

    E(k,l)=E0-24J+4J[cos(2pi k/M)+cos(2pi l/M)].         (6)

For every M>=3 and J nonzero, these are not all equal. A basis input |z,w> therefore undergoes genuine motion; this is not merely a degenerate dark eigenspace. Arbitrary superpositions of all M^2 logical coordinates are allowed. Arbitrary entanglement with a passive reference is also allowed because (4) and (5) are operator identities, extend by tensor identity, and preserve the same code.

If P_R is identity on live sites times the product up projector on x=0,2, then P_R B=B. By (5), P_R exp(-itH)B=exp(-itH)B. Thus every pure or mixed encoded input has the record subsystem exactly in its original pure product state at every time, uncorrelated with the rest. No actual measurement or postselection is involved in that statement.

The two hopping coordinates interact only through their fixed correlated row encoding; the effective motion in z is noninteracting. This is a two-excitation extension of the previous single-excitation record-preserving sector, not a derivation of interacting matter, a universal processor or arbitrary density protection.

## Preserved failure cases

1. **Odd reflection alone at n=2.** The earlier construction with a generic reflected pair can leak into a recorded plane after one H action. That counterexample in the prior report remains valid; the present state uses a stronger encoded singlet-pair and staggered-row condition.
2. **The initial local boundary kernel is not enough.** Every product of t/s mirror cells initially kills the transverse record-flip coupling. Nevertheless adjacent singlets are not preserved by the live-layer Hamiltonian. In the controls, |s_(0,0) s_(1,0)> has zero record leakage after one H action but nonzero record leakage after two: at J=1 the squared norm of its normalized Q_R(H-E0)^2 image is256. Thus the original boundary kernel is not an invariant code. Because Q_R(H-E0)psi=0, the same second-order record leakage is obtained using H^2.
3. **Missing phase.** Replacing (-1)^y by a constant makes the two y-hop routes add instead of cancel. There is no claim of protection for that preparation. The exact operator equality in the code is a phase-sensitive interference mechanism.
4. **Geometry.** The proof assumes L even, L>=6, M>=3. L=4 has orientation redundancy and needs a different code dimension/normalization; it is not silently included. Odd L loses the periodic staggered reindexing. Other thicknesses need their own boundary coupling argument.
5. **Higher excitations.** No general tensor product of these codes is asserted. Independent row-translated pairs can collide, and the |s,s> conversion then matters. n>=3 remains an open extension, as does the maximal n=2 invariant subspace.

## Executed exact controls

`many_body_dark_check.py` is a fresh same-author implementation of the literal computational-basis Pauli action. It never uses a compressed Hamiltonian. For J=1 it subtracts E0 only as a bookkeeping identity: every unlike bond contributes -2 on the diagonal and +2 on exchange, retaining all ordinary torus edges. Four physical configurations represent each two-singlet product; their integer coefficients avoid floating arithmetic in the invariant-subspace checks.

It checks the exact identity (4), pairwise column orthogonality and normalization, and nonstationary motion on every basis column for:

| Physical torus | Qubits | Edges | Code dimension | Integer-column norm squared |
|---|---:|---:|---:|---:|
| 4x6x3 |72|216|9|24|
| 4x8x4 |128|384|16|32|
| 4x10x3 |120|360|9|40|

The adjacent-singlet two-action failure is checked in all three. Full output is `many_body_dark_result.json`. These exact finite checks support arithmetic and implementation, but the arbitrary-size proof is the algebra above. This is not an independent check; the root's earlier one-excitation independent results do not automatically certify this new code.

## Supplier ledger and next decisive work

Retired **within this stated code**: externally supplied permanence-as-compression, a projection or measurement cadence, and a hand-added protecting gap. The native H itself preserves the pure local record qubits and acts nontrivially on the code.

Still supplied/open: D-dyn and the selected K=D=0 member; the finite periodic geometry; polarized record/background content; the correlated row-staggered two-singlet encoded input; its preparation/loading map; formation of records; physical readout semantics and time scale. No robustness gap against generic perturbations or generic environment is proved. No theorem extends to unrestricted live inputs or the prior all-input target W.

The next useful check is an independent full-spin reconstruction of (2) and the reindexed y cancellations, plus direct H B-B H_code on at least one geometry. After that, the substantive frontier is either a native encoded-input loading mechanism or a finite-density invariant-code extension with nontrivial dynamics. A claim of maximality would require an actual invariant-kernel computation and proof; this report intentionally supplies a positive family instead.
