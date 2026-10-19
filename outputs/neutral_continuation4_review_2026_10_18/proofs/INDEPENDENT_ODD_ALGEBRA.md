<!-- Owning original: PR9762; source SHA256 c9644aec4c6d5834f9c82aaf3524c0aa5ad855d4fbffc34420386ffad2253757. -->
**Source boundary:** Complete mathematical source follows. Original review dispositions, execution stories, provisional questions and PASS labels are historical annotations, not current certification. Later explicit addenda supersede earlier provisional statements. Mathematical hypotheses and conclusions are retained; terminal exclusion interpretations require separate admission and are not promoted by this source enclosure.

# Independent odd-column ground-manifold algebra check

Scope: the stated leading column coefficient Hamiltonian, open odd column height L, even transverse M>=4, and its plaquette-plus manifold. This is not a full native perturbation-remainder or bulk-mode proof.

## Exact algebra

Represent configurations by s_xy=a_x b_y, modulo simultaneous reversal of every a and b. The dimension is 2^(2M-1). For even M, A=product a and B=product b are well-defined under this redundancy. With epsilon=(-1)^(M/2), physical plane actions are

X_x=R_x, Y_y=epsilon A C_y.

The Y phase follows directly from i^(ML) product_x s_xy^L=epsilon A for odd L; i^(ML)=epsilon because M is even and L odd. Thus every X_x anticommutes with every Y_y, within-family generators commute, and product X=product Y. There are 2M-1 independent Pauli generators, symplectic rank two and radical dimension 2M-3.

All central characters occur. Nonidentity center elements have zero trace in the pattern basis: a nontrivial flip has no fixed patterns, while a pure nontrivial diagonal character averages to zero. Each center block consequently has dimension four, comprising a protected physical-plane doublet times a neutral multiplicity doublet. The latter is an actual algebraic possibility, unlike the even-column Abelian representation with multiplicity one.

The matching operators are U_x=epsilon B R_x and V_y=C_y. A row's product of logical Ys is i^M product_y s_xy times its row flip, yielding exactly epsilon B R_x; a column's product of Xs gives C_y. U and V commute with every physical plane. U-family and V-family each commute internally; every U anticommutes with every V. Their products obey product U=product V. Signs and conventions in the proposed leading Hamiltonian -tau(sum U+sum V) are consistent.

An independent 128-dimensional M=4 implementation, /private/tmp/neutral_odd_ground_check.py, verifies all these commutators and product relations exactly (zero floating error). The all-relative-plus block has dimension four and eigenvalues (-4 sqrt(2),-4 sqrt(2),4 sqrt(2),4 sqrt(2)) in units tau.

## Neutral transition and constraints

Within a fixed center block choose U_x=u_x X_neutral and V_y=v_y Z_neutral, absorbing one common sign into each Pauli axis. Then H=-tau(r X_neutral+c Z_neutral), r=sum u, c=sum v, with energies +/-tau sqrt(r^2+c^2), each retaining protected degeneracy. The neutral transition within this block has gap 2 tau sqrt(r^2+c^2). The center relations constrain allowed sign collections: these expressions are not a license to vary r and c independently or identify the smallest inter-sector gap.

In the maximal all-relative-plus center, |r|=|c|=M; choose both positive. Its neutral gap is 2 sqrt(2) M tau. For W=sum U-sum V, the transition weight is |<+|W|->|^2=2M^2. M=4 therefore gives gap 8 sqrt(2) tau and weight 32. W is neutral under the plane group but is transverse nematic, not a square-rotation scalar.

## Original uniform readout is dark at this leading level

A uniform longitudinal C source preserves the transverse interchange symmetry and changes the two matching amplitudes equally at the isotropic point. The scalar leading effective readout is therefore constant plus a multiple of sum U+sum V; it has no transition between the two neutral energies. More securely, in the maximal center the physical transverse interchange exchanges the two neutral Pauli axes. Its invariant neutral Hermitian algebra is span{I,X_neutral+Z_neutral}. Any symmetry-equivariant effective scalar readout restricted to this isolated four-dimensional block therefore commutes with its symmetry-invariant effective Hamiltonian. This protects darkness within that block, provided the effective reduction and isolation hold; it does not assert darkness to other excited bands.

A parameter derivative of an effective Hamiltonian alone does not generally establish off-diagonal physical-source matrix elements: the parameter-dependent unitary contributes a connection commutator. The symmetry argument avoids that omission for the maximal isotropic block. In other center sectors exchanged by the spatial symmetry, or after anisotropy, darkness requires a separate check.

The nematic derivative accesses the perpendicular neutral combination. If native t_x,t_y scale as respective microscopic transverse couplings to power L, logarithmic microscopic anisotropy introduces the factor L in their derivatives. Conversion of a column-model response into a native source response must retain that factor and any K derivatives. It does not turn the nematic observable into the original scalar C.

Conclusion: the neutral multiplicity qubit and its leading ultrasoft intra-center transition are confirmed. The original isotropic scalar readout does not acquire that line merely because the neutral qubit exists. No global-gap, thermodynamic, or cosmological claim follows.
