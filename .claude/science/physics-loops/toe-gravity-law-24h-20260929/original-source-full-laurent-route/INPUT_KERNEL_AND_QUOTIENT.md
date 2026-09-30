# A physical first-hop input kernel and the weaker history-image consumer

This separate exact discriminator uses the same supplied rotor/Gauss/mark definitions as SOURCE_FRAME_PROOF.md. It neither edits that frozen proof nor supplies an actual Omega source-weight estimate. No scientific execution is needed for the eight-word cancellation.

## 1. Eight physical inputs killed by the complete first hop

Fix h in A on a safe even torus, and partition its six B neighbors into three arbitrary disjoint pairs (1,2),(3,4),(5,6). In each of the eight basis inputs, h has charge +, exactly one B in each pair is occupied with charge +, and the other three star B sites are empty. All other A sites are occupied. Fix one distant A site u to have charge -, all other A sites +; fix one distant B site v to have charge -, all other nonstar B sites empty. The global input has W=0, NB=4, exactly two minus occupations and total charge n=|A|. The observed original history labels are not changed or identified with these occupations.

Choose one of these words as reference. It has an integer physical field solution because its prescribed divergence q-1_A sums to zero on the connected finite graph. A spanning tree constructs such an integer flow. Keep all fields outside the six star links fixed. If q_b^0 are the reference star charges, replace each star field by

    E_hb = E_hb^0 - (q_b-q_b^0).                          (1)

Every B Gauss equation is then preserved. The sum of the three star charges is always three, so the A_h Gauss equation is also unchanged. Thus all eight inputs lie in one actual exterior-fixed Gauss block. Their charge words are distinct and orthogonal, and their fields differ only locally.

Use x_b only as notation for an occupied B+ site in this physical block; x_b^2=0 records hard-core exclusion, not a new scalar-field dynamics. The normalized vector is the eight-term physical superposition represented by

    v = 8^(-1/2) (x_1-x_2)(x_3-x_4)(x_5-x_6),           (2)

with the common A/exterior data above. Its relative coefficients are real + or -. The actual rotor F_h moves the A+ into one empty B neighbor with amplitude one and the correct field shift -1. On this particular all-plus block it is therefore the square-free incidence map multiplying (2) by x_1+...+x_6. Each pair gives

    (x_(2j-1)+x_(2j))(x_(2j-1)-x_(2j))=0.

Consequently

    F_h v=0.                                             (3)

Equivalently, a four-subset output has either no predecessor in (2), or exactly two predecessors of opposite signs. Their final actual electric fields agree by (1), since the occupied output subset agrees. This checks charge and field cancellation, not just an occupation proxy. Every output is physical and the rotor shifts have unit amplitude; no spin-boundary deletion is used.

The complete source and ordinary formation at center h share this first hop. Hence for every original resolved sign or unnormalized coherent edge label,

    B_(h,mu)^+ v = -F_h j_mu F_h v = 0,
    b_(h,mu) v = j_mu F_h v = 0.                         (4)

Yet P_(h,3)v=v and ||v||=1. In particular no positive state-independent constant c can satisfy

    sum_mu (B_(h,mu)^+)* B_(h,mu)^+ >= c P_(h,3)          (5)

on the full physical input sector. This is fully compatible with the checked OUTPUT frame BB*>=c_out D_(h,mix). A row map can be onto its output range while retaining a nontrivial input kernel.

The precise finite block confirms the dimension. On all twenty choices of three occupied B+ sites, F_h is the three-subset-to-four-subset incidence map. Its product FF* on four-subsets is 4I+A_(6,4). Complementation identifies A_(6,4) with A_(6,2), whose elementary incidence eigenvalues are 8,2,-2 with multiplicities 1,5,9. Thus FF* has positive eigenvalues 12,6,2, rank fifteen, and the first-hop input kernel has dimension five. Equation (2) is one explicit kernel vector.

## 2. Exact weaker sufficient input-span condition

Keep a fixed physical W0 input B count and let C be the actual closed original-history span from Omega at that count. Define

    A_h = F_h P_(h,3),       M_h = closure(Ran A_h).       (6)

For a dark vector psi, source adjoints already restrict the input to P_(h,3). Factor their pairing as

    <psi, B_(h,mu)^+ P_(h,3) phi>
       = -<j_mu* F_h* psi, A_h phi>.                    (7)

Suppose psi is orthogonal to every actual source B_(h,mu)^+ C. Since the adjoint on psi is P_(h,3)-supported, the same vanishing holds with P_(h,3) inserted on the actual input. The following is a sufficient condition weaker than full projected-history density:

    closure(A_h C)=M_h.                                  (8)

Under (8), (7) vanishes for every formal input phi, so A_h* j_mu* F_h* psi=0. The checked source-frame bound then gives D_(h,mix)psi=0, after summing original labels. No injectivity of A_h is required; its kernel is explicitly present in section 1.

The exact minimal condition is only absence of annihilator vectors in the relevant projected j_mu* F_h* dark-adjoint range. Equation (8) is a concrete stronger sufficient condition with an explicit consumer space. It remains an ACTUAL history-image reachability theorem, not something implied by the dimension calculation or the formal source frame. In particular, closure(A_h C)=M_h is not proved here.

## 3. Limits and failed shortcut

The eight-word vector is a permitted physical input, not a claimed actual conditional density produced by the supplied Omega process. Reachability of individual words, positive diagonal populations, local occupation probability, or a finite electric cutoff cannot by themselves remove its coherent cancellation. This proof does not say that the actual source places positive weight on this kernel, that all centers annihilate it, or that its kernel is preserved by the true W0 waiting Hamiltonian or by fast H2. It is not an invariant dark branch or an actual-source obstruction to eventual absorption.

The result prunes one proposed shortcut: a state-independent positive lower source intensity based only on the P_(h,3) occupation event cannot be used to infer source faithfulness. The remaining aligned-star invariant-module question is independent and still open. No finite-spin, common-time microscopic, energy/work or physical selection statement is added.
