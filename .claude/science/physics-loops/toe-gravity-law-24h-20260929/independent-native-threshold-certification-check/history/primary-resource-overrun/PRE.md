# Independent pre-exposure reconstruction: native threshold certification

Prepared before opening native-threshold-certification-route/REPORT.md, new code or results. Only its CONTRACT was read. It exposes the1487 connected perfect-matching compression, full15-dimensional raw quadratic frame, mu=tau=1 benchmark, factor-two concern and proposed ordered pair-removal lift. These are disclosed expectations, not blind predictions. The checker previously authored the original native threshold route and read its focused receipts; this is independence of the new certification derivation/implementation, not blank-slate discovery.

Inputs read: actual main30a native qubit density source completely; full prior native threshold proof and independent check; complete load-bearing pulse derivation and independent675-entry check; strict-positivity extension/check; actual pair-removal/lower comparison and threshold variational normalization/check. Only documented law identities and old bare-quartic coefficients may be reused. No new author implementation is read/imported. Procedures7146 remain selected. The supplied qubit Hamiltonian/vacuum/couplings and infinite-lattice K=0 sector are assumptions, not native selection or a physical record law.

## 1. Raw and normalized incoming frames

Use x=(u1,u2,v12,v13,v23), u3=-u1-u2. For each physical unordered G edge e let w_e(x) be u_i on axial edges and -d_i d_j v_ij on diagonal displacement d_i e_i+d_j e_j. For four distinct sites define M_x(S) as the sum of the three physical perfect-matching products. Then C_x²Omega has coefficient2M_x(S), while the identical-pair incoming profile is sqrt(2)M_x(S). All overlap-zero and multiple-matching sums are physical.

Let m(x) contain x_i x_j for i<=j, without offdiagonal sqrt(2), and write M(S)=m_S m(x). If B is the raw pulse matrix, its affine finite-energy meaning is E(M_x)=m(x)^*B m(x). The actual raw threshold matrix is therefore

    2[B-F^*G_H(0)F],       F=H M.                      (P1)

A compact matrix X of raw M corrections gives

    B_X=B+F^*X+X^*F+X^*H X,
    R=F+H X,
    T_raw=2[B_X-R^*G_H(0)R] <=2B_X.                    (P2)

These are full fifteen-channel forms, not only real/coherent samples. The pulse coefficient is half the identical-pair threshold form.

For the normalized one-pair coordinate z, x=Lz with
u1=z1/sqrt2+z2/sqrt6, u2=-z1/sqrt2+z2/sqrt6, vij=z_Tij/sqrt2.
The raw one-pair Gram is G=[[2,1],[1,2]] direct_sum 2I3. A general normalized symmetric matrix A has HS norm; its raw matrix is L A L^T. Let R_frame map the normalized Sym² basis (diagonal A_ii and sqrt2 A_ij) to raw entries (L A L^T)_ij, i<=j. The physical normalized upper matrix is

    2 R_frame^* B_X R_frame.                           (P3)

The raw quadratic metric G2 is defined by ||G^(1/2) A_raw G^(T/2)||_HS² and satisfies R_frame^*G2 R_frame=I. Its value on m(x) is (x^*Gx)². Normalized eigenvalues may equivalently be computed from (2B_X,G2), never the unweighted raw matrix. A factor or offdiagonal convention error changes this test.

## 2. Independent complete source assembly

Use the actual positive local rows H=A+mu D+W, rather than applying the author's new action builder. For a bare edge e and residual unordered pair eta, subtract the disconnected polynomial w_e w_eta from the actual M(e union eta) coefficient (zero when they overlap). Each local square row annihilates the uniform one-pair coefficients, so the subtraction cancels exactly within the row.

A nonzero defect requires either eta sharing an endpoint and being a G edge, or one eta endpoint in N_G of each endpoint of e. This gives a finite EXHAUSTIVE candidate set. At fixed center0 (and the neighbor center for a gradient), form the row polynomial d_L(eta), its Gram contribution and its actual hard-core adjoint image. Summing over all local row types, residual eta and allowed output edges gives COMPLETE F=H M, including Q and exterior components. Disconnected pair outputs are not discarded merely because the trial X is supported in the connected matching core.

At mu=tau=1 all arithmetic is integer after multiplying H and B by12. The rational E projector can be represented by three gradient rows of weight12 minus their sum row of weight4. The positive combined projector is retained exactly; this algebraic signed-row representation does not make H indefinite. Singlet rows have weight8, plane-complement rows weight3, and plane-gradient signed-sum rows weight3. Diagonal degree-three stars give12 D M; isolated configurations have M=0. The old independently checked bare matrix supplies a225-entry comparison control, not the source values.

Separately implement the exact removal identity to construct actual columns: remove each occupied physical G edge e from S, apply the physical pair operator K2 to e, create an edge disjoint from the residual pair, and add mu D(S) on the diagonal. K2 comes directly from the axial projector and the signed plane coefficients, including both shared shell centers and every center-gradient term. This is distinct from an assumed independent-pair carrier. Core-to-all columns are kept. Their transpose relation must hold in the ordinary infinite-lattice translation-orbit normalization.

Generate connected four-site shapes by neighbor growth and retain perfect-matchable shapes only for the trial domain. Finite sets on Z3 have no nonzero translation stabilizer. This does not normalize a finite torus N4 space or suppress its possible stabilizers.

## 3. Dual residual inequality and its normalization

Write the exact fiber form as H=mu D+T^*K2 T, where T records an ordered removal (residual unordered physical pair eta, removed G edge e). There is no matching chosen by T. Split any compact residual r into perfect-matchable r_P and nonmatching r_Q. On Q, D>=1. Put d(S)=r_Q(S)/sqrt(mu D(S)). On P set

    g(eta,e)=r_P(eta union e)/(2m(eta union e))           (P4)

when eta and e are disjoint G edges, where m is the number of perfect matchings; set g=0 otherwise. A four-set with m matchings has exactly2m such ORDERED removals, so T^*g=r_P. The residual G pair eta has one of nine physical bond orientations. Fix its anchor0 to implement the K=0 quotient. For each of those nine residual orientations, g_eta is a compact nine-component field in the removed-edge anchor. Both ordered removals are present; no extra sqrt2 or torus-orbit factor belongs in(P4).

Cauchy-Schwarz in the direct sum of the D and K2 energy spaces gives

    <r,G_H(0)r>
      <=sum_Q |r(S)|²/[mu D(S)]
                   +sum_(eta orientations)<g_eta,K2^-1 g_eta>. (P5)

One can first use finite-support test vectors and the variational inverse form. The known compact-source inverse is finite; K2^-1 is also only a compact-source quadratic form. At q=0 K2 has soft modes, so a bounded inverse on l2 is not assumed.

The full9-by9 symbol satisfies K2(q)>=a ell(q), a=min(tau,mu/6), ell=2sum(1-cos q_i). In3D its inverse is integrable. For a compact removal source the free term is a normalized Brillouin integral of ghat^*K2^-1 ghat. Ordinary floating samples do not certify it, especially near q=0. A universal conservative certificate is available without quadrature: g_scalar=integral ell^-1<=sqrt3*pi/8, and a compression to M_eta physical edge entries has norm<=M_eta g_scalar/a by its trace. At mu=tau=1, pi<22/7 and sqrt3<7/4 give g_scalar/a<33/8. Thus a rational fifteen-channel dual matrix can be built as

    D_dual=(1/mu) r_Q^*D^-1 r_Q
                    +(33/8)sum_eta M_eta g_eta^*g_eta. (P6)

It may be too large to be numerically useful, but is a valid finite certificate. The sharper Green integral requires an explicit singular-ball remainder and certified off-ball quadrature/rounding. Applying(P5) to every channel vector gives the Loewner interval

    2 R_frame^*(B_X-D_dual) R_frame <=T0
                               <=2 R_frame^*B_X R_frame. (P7)

No factor two is inserted in(P5); the factor two in(P7) belongs to the chosen raw incoming M normalization. Anisotropy or eigenvalue ordering of the UPPER trial matrix alone does not establish that of T0.

## 4. Initial independent job price

One foreground exact sparse job, <=30CPU seconds, <=150MB peak RSS, one BLAS/OpenMP thread, hard CPU25seconds, deadline and both STOP forms checked. No author new code is imported. Construct the complete source by the square-row defect method and actual core columns by the pair-removal method. Compare the old full bare quartic matrix, check selected source entries by direct rows, and evaluate a separately chosen rational Jacobi trial X=-F_core/160. This is a discriminator, not an attempt to reproduce the author's optimizer or read its numerical conclusions. Store full source/support/core-boundary evidence, normalized raw metric and exact trial matrix for later comparison. If the envelope fails, preserve the failure, stop and re-price before another attempt.
