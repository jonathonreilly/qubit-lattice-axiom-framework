# Exact positive two-body diamond gate: proposed algebraic interface

ROOT original derivation, not independently checked. Motivation: replace approximate resonant gate action with an exact data-gauge identity. No finite performance, capture or native realization theorem is claimed. This is a distinct supplied primitive candidate, not a modification to published PR9733.

Let four physical head qubits be L,u,v,R and one ordinary data qubit D. Let n_i be the head occupation projector and X a real Hermitian involution on D (X_D or Z_D). On a pair of head qubits define

Q_s(i,j;a)=a[n_i+n_j-s(sigma_i^+ sigma_j^-+sigma_i^- sigma_j^+)], s in {+1,-1}, a>0.

This full two-qubit block is positive: its vacuum eigenvalue is0, its one-head eigenvalues0,2a, and its double-head eigenvalue2a. Its norm is2a. Set g>0 and install

H=Q_+(L,u;a)+Q_+(L,v;a)+Q_+(u,R;a)+Q_-(v,R;a)
  +g n_u(I+X)+g n_v(I-X).

The last two blocks are positive of norm2g, on one head and one data qubit. Every term is real, number preserving and at most two-body. All terms annihilate the entire head vacuum, on arbitrary data. There is no free data Hamiltonian. Six listed blocks; five qubits. Head-data products do not mean an extra third support.

In the one-head sector set B=(u+v)/sqrt(2), C=(u-v)/sqrt(2). In the ordered coordinates L,B,C,R the exact matrix is

[2a I, -sqrt(2)a I, 0, 0;
 -sqrt(2)a I, (2a+g)I, gX, 0;
 0, gX, (2a+g)I, -sqrt(2)a I;
 0, 0, -sqrt(2)a I, 2a I].

The off-diagonal gX follows from the difference of the two arm data terms; their common scalar part g is retained. The two signed paths cancel the direct L-R transfer, but the first nonzero central transition already carries X. Let W=diag(I,I,X,X). Since X*=X=X^-1,

W* H W = h tensor I_D,

where h is the real four-site Jacobi matrix with the same diagonals and off-diagonal entries -sqrt(2)a, +g, -sqrt(2)a. Equivalently H W=W(h tensor I). No perturbative limit or on-shell assumption enters. Adding arbitrary data-independent on-site terms or scalar couplings inside a left extension at L and a right extension at R preserves the identity, provided W is I on every left extension coordinate and X on every right extension coordinate. There must be no extra left-right bypass or additional data term. Left/right leads may be finite. All passive reference spaces tensor through this identity.

For a head initially at a left coordinate x and an arbitrary state psi on D and its passive reference, the amplitude at any right coordinate y is exactly

<y|exp(-itH)|x> psi = <y|exp(-ith)|x> X psi.

Thus if the right-sector event has nonzero probability, its normalized data channel is EXACTLY X for every time, independently of how small the probability is. The scalar head profile is independent of the data. Reflection to the left has data action I. The entire evolving state remains W[exp(-ith)|x> tensor psi]; internal physical u/v amplitudes are (f_B I +/- f_C X)/sqrt(2), so the complete apparatus generally entangles with data during passage. No claim that internal head postselection implements X is made. A freely chosen physical record bit is not automatically the right-sector event.

One short-time check: <R|H^2|L>=a^2-a^2=0, while <R|H^3|L>=2a^2 g X, agreeing with the gauged chain product (-sqrt(2)a)(g)(-sqrt(2)a). All shorter right-terminal amplitudes vanish. This check supports the exact matrix identity but does not substitute for checking it.

Full-support incident norm sums for this isolated primitive are4a at L/R,4a+2g at u/v and4g at D. External blocks add their actual loads. Positivity does not eliminate the scalar on-site structure: h has endpoint2a and central2a+g diagonals. Coupling uniform rays adds their endpoint diagonal contributions. One cannot simply call h a matched uniform chain, inherit a perfect transmission phase or transfer a previous runtime theorem. In particular a=j/sqrt(2), g=j gives central diagonal(sqrt(2)+1)j, not2j. Exact gate action is independent of that scattering mismatch; useful success probability still needs a separate analysis.

For a scalar identity version replace X by I. The same formulas hold with g n_u(I+I)=2g n_u and the zero v term omitted. The data-free scalar operator h is identical after B/C rotation, so these can be used as matched identity/gated lanes at the algebraic level. This does not yet prove a composed multi-rail CNOT/SWAP construction: channel mixers, shared-data gauges, every port and ordinary data reuse need their own exact global identity. Geometry and cap for a composed network must be counted anew.

This is an exact conditional interface under supplied signed positive bonds, exact symmetric arms and supplied data-dependent blocks. It is not a derived native interaction, robust fabrication tolerance, ordinary-input preparation or permanent halt result. No scientific executable has been run for this source. ROOT derived the matrix before exposure to any checker. The forthcoming review must independently reconstruct full-block positivity, signs, vacuum condition, one-head transform, phase and extension qualifications; it should also assess overlap with prior primitives rather than assume novelty from a new name. No editable prompt files changed.
