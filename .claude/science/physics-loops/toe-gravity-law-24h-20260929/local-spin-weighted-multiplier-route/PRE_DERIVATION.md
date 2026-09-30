# Author derivation before new controls

The rotor multiplier is T=aI-O/delta, O=i(V*-V), from the checked sparse-dark proof. V maps a selected actual two-hop dark word at h to its clean axial G10 rotor output at c=h+2d. O is a partial signed permutation: every basis row and column has at most one nonzero entry, of magnitude one. Its occupancy selection is supported in B3(h); for an input at the bright endpoint its reconstructed old hole is within two steps. The physical spin-box projection P_S commutes with the diagonal reward Pi and Gauss. Therefore T_S=P_S T P_S is positive, uniformly bounded, and commutes with Pi_S even when O does not preserve the spin box.

Extend normalized spin shifts by zero outside their box as in the checked global comparison. H_S=Hbar_S+Delta_S is self-adjoint and preserves that box. Compression of the full algebra gives

 L_S(T_S)=P_S L_rotor(T)P_S + P_S E_S P_S,
 E_S=-a kappa(G_S-G_rotor)
     -i[H_S-H_rotor,O]
     +kappa/(2delta){G_S-G_rotor,O}.

This identity does not drop intermediate rotor leakage; it is absorbed in the actual extended-operator difference. The scalar part of T cancels every Hamiltonian difference, including the extensive diagonal compensation.

Each Hbar difference is a sum of at most744 actual two-hop words per hole row and column. A normalized-spin link differs from its rotor shift by at most2(1+|E|)^2/[S(S+1)], with exact boundary zeros. Telescoping two hops costs a fixed polynomial in only their link fields. In a product with O the net hole displacement is at most four and every affected link lies within a fixed radius (radius12 is deliberately loose) of BOTH its incoming and outgoing holes. Intermediate shifts are at most four. Thus each matrix coefficient can be bounded by a fixed constant times q_x q_y/[S(S+1)], where q_x,q_y are the moving-hole local weights of its input/output. Weighted row/column Schur then bounds the Hermitian form by a constant times <Q_loc^2>. The actual row budget must be counted before giving a numerical constant.

For [Delta_S,O], diagonal terms outside the changed hole/charge/link neighborhood cancel EXACTLY. Only compensation centers within distance two of a changed occupation gate, or incident to a changed charge/link, remain. Those lie within radius four of the old hole, and their electric links within radius five. Their number is finite independently of volume; every coefficient is bounded by its local squared fields divided by S(S+1). This is the decisive difference from bounding ||Delta_S|| globally. The loss difference is already a sum over at most six edges at the current hole; its product with O has the same finite weighted bound.

If the proposed form estimate is established, integrating the actual spin no-event path gives

 integral_0^T ||Pi_S Z_S(t)psi||^2 dt
 <= C_loc||psi||^2 + K/[S(S+1)] integral_0^T ||Q_loc Z_S(t)psi||^2 dt.

It does NOT bound the last integral, give all-background absorption, or transfer the rotor marked resolvent without another weighted argument. For Pi-supported forcing, the positive multiplier still controls the observed component up to this same local-field error; the exact passive identity then controls full terminal-plus-original-mark amplitudes. Any eventual source application must derive, rather than posit, the relevant moving-hole field weight.

A possible stronger exact-spin construction was considered and not assumed. The dark-compressed law preserves certain inner star fields, but can exchange charges at adjacent occupied A sites; clean rotor moves may meet actual spin boundary zeros. Requiring all output vacant-edge fields uniformly interior is not known to reduce the dark block. Thus simply declaring a field-cut sparse subspace invariant would be unjustified.
