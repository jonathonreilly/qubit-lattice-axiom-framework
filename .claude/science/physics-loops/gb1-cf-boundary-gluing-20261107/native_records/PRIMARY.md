# Free coarse-vertex outputs: supervisor candidate

Status: conditional mathematical candidate, not a native record-only law; independent derivation pending. Frozen before reading the separate checker. Input science head 985f174411be88e0cb7e826f0df8f2ad3c16ea35. The proposed axiom PR is separate and this algebra does not depend on its adoption.

## Exact target

On a torus of side 5n, n>=3, retain the supplied four-qubit link isometry J and every origin p mod 5. V_p consists of sites congruent to p, A_p of sites with exactly one differing coordinate mod 5, and F_p of sites with at least two differing coordinates. Define E_p as the tensor product of J(R) on all coarse-edge interiors, arbitrary qubits on V_p, and fixed |0> on F_p. Test orthogonality, local phase detection, a finite local record instrument and compatibility with the supplied Hamiltonian. All tensor quantum kinematics, code preparation, probabilities and instrument interpretation are conditions.

## Geometry

For p != q let D be the coordinates where they differ. If |D|=1, choose an edge direction i outside D; every interior point of any q-edge in direction i differs from p in the fixed D coordinate and in direction i. If |D|=2 choose the remaining direction; two fixed differences persist. If |D|=3 choose any direction; two fixed differences persist. Thus an entire q-edge lies in F_p, still fixed to |0000>, while its q-code is orthogonal to |0000>. This proves E_p perpendicular to E_q even for arbitrary entangled data/output states. The six-edge projector D_x of the native note still restricts to I for x congruent p and to zero otherwise, by the same local witness. Its edge supports never include x. Native translations and proper rotations permute the E_p; reversal covariance FJ=JK is unchanged.

The enlarged total code has dimension 125 * 5^(3 n^3) * 2^(n^3), retaining one output qubit per coarse vertex. This is an encoding-subspace enlargement on the same native qubits. The record/no-record flag remains the framework's classical distinction; it is not identified with output bit 0/1. A blank output has supplied quantum preparation |0>, whereas a recorded zero has the same pointer vector and a different record flag.

## Local instrument on a blank site x

For each of six incident coarse edges e (length five), let P^e_b be the corner-encoded electric-sector projector J P_b J^dagger on its four interior qubits. P^e_0+P^e_1=Q_e and each commutes with D_x (the product of six Q_e). Set A_x=|0><0|_x D_x. It is an orthogonal projector. Define

  L_{x,e,b}= (1/sqrt(6)) |b><0|_x P^e_b D_x,
  L_{x,empty}= I-A_x.

Since sum_b P^e_b=Q_e and Q_e D_x=D_x,

  sum_{e,b} L^dagger L = A_x,
  L_empty^dagger L_empty = I-A_x.

Hence these operators define a trace-preserving instrument on the entire finite native Hilbert space. No giant matrix or off-code inverse is needed. The output label e may remain unobserved: group its six Kraus branches under the two recorded outcomes b. The resulting b-conditioned state is a mixture over the incident-link choice, not a specified single-link measurement. If the link identity is to be readable later, it must also be recorded using separate resources; the pointer records only the Casimir value.

At true-phase fresh x the no-event operator vanishes and the outcome probabilities are (1/6) sum_e Tr(P^e_b rho). At false-phase x the event operators vanish and the no-event operator is identity. These identities include arbitrary external entanglement. In a coherent sum of origins, an event at x projects onto its compatible origin; this changes origin coherence and must not be called coherent preservation of the origin superposition. The no-event branch retains the other origins. Covariance is an identity of the full instrument family: spatial operations permute x and the six edges, while reversal leaves P_b invariant. It does not say each realized event is symmetric.

Keep a classical record map R. If x is already recorded, use the identity/refusal branch and never write again. If x is fresh, a b-event appends R(x)=|b><b|. On reachable code states the new record lies at a coarse vertex and no other output/data record is modified. The input domain permits records only on compatible vertex registers, and every unrecorded vertex pointer must start in |0>. Sampling x uniformly from the finite native torus gives one covariant normalized update on the joint quantum/record state. This supplied finite-volume scheduler has no uniform-site extension to the infinite lattice claimed here.

## Magnetic evolution and Gauss constraints

Each supplied H_native seed acts on encoded edge interiors and D_x, with no true-phase coarse vertex in its support. On E_p false-phase seeds still vanish; true-phase seeds act as the coarse H on the logical links and identity on V_p. Thus H_native|E_p = H tensor I_output, including the magnetic plaquette terms, and every already-recorded output is frozen by its finite-volume exponential. Each P_b commutes with the endpoint gauge actions, so event branches preserve the full Gauss-invariant subspace; the statement does not require intermediate native gates to be gauge invariant.

This is compatibility of a supplied finite-range Hamiltonian with record storage, not its synthesis as an autonomous admissibility law or exact finite-depth circuit.

## Remaining target and falsifiers

At most n^3 outputs can form in one finite phase sector; no reset/reuse or infinite renewal follows. A complete current-record-only law must reconstruct the relevant quantum conditional state from specified preparation/program/outcome records, or prove the outcome measures factor through the complete permitted record condition. Two live preparations with identical R can have different electric probabilities, so the joint state (rho,R) cannot silently be equated with a framework state. The larger neighborhood wording does not by itself supply that missing data, Born weights, tensor composition, magnetic couplings or scheduler.

Geometry falsifier: free all spectator sites, or place outputs in the originally frozen witness edges; the separation argument then fails and arbitrary origin sectors need not remain orthogonal. Instrument falsifier: omit the no-event branch, use six unweighted edge branches, overwrite recorded zero, or assert direction recovery from the single output bit. Required checks are the exact residue geometry, projector completeness and record-flag handling, not a count of PASS lines.
