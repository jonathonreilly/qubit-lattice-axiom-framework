# Working match of the open Wilson determinant to a fermionic boundary amplitude

Unverified working derivation. Generic Wilson transfer matrices and determinant reduction are established literature, not new mechanisms here. Relevant primary leads include Luescher, DESY76/54, https://bib-pubdb1.desy.de/record/396349/files/7611148.pdf?version=1 , and Wenger, arXiv2302.07385. The proposed task is to match the precise anisotropic open-boundary operator used by Block02, including its scalar prefactor and boundary state. No phase claim follows.

Fix temporal gauge on an open interval; all temporal links can be removed by a gauge transformation. In a gamma_0 diagonal basis write

    mu-K_s(t)=[a_t, b_t; -b_t*, d_t],
    h_t=gamma_0(mu-K_s(t))=[a_t,b_t;b_t*,-d_t].

The diagonal blocks are Hermitian and at least mI. This follows from the compressed spatial Wilson projectors: each is mu minus kappa/2 times the spatial covariant adjacency. The traces of a_t and d_t are both mu r, where r=2|Lambda_s|, because the open spatial shifts have zero diagonal. The off-diagonal sign follows from gamma_0 K_s gamma_0=K_s*. Consequently h_t is Hermitian. Its spectrum stays outside(-m,m), since multiplication by gamma_0 preserves singular values and ||K_s||<=3kappa.

Let A_t=I+delta a_t, B_t=delta b_t, C_t=-B_t*, D_t=I+delta d_t. The homogeneous finite-time Dirac equations are

    A_t u_t+B_t v_t-u_(t+1)=0,
    C_t u_t+D_t v_t-v_(t-1)=0,

with open endpoint values v_(-1)=0 and u_(M_t)=0. Solving one step gives

    [u_(t+1);v_t]=X_t [u_t;v_(t-1)],
    X_t=[A_t+B_t D_t^-1 B_t*, B_t D_t^-1;
                         D_t^-1 B_t*,D_t^-1].

X_t is strictly positive Hermitian by the factorization

    X_t=[I,B_t;0,I] diag(A_t,D_t^-1) [I,0;B_t*,I],

and X_t=I+delta h_t+O(delta^2) on each fixed finite spatial graph. This is a transfer of the homogeneous Dirac recurrence; its sign is plus h_t. It is not yet the physical many-body Euclidean evolution.

With X=X_(M_t-1)...X_0, block elimination is expected to give

    det(delta D_full)=product_t det D_t * det(X_(++)),          (H.1)

up to a sign that must be fixed explicitly by the K_s=0 normalization. For one time slice it is exactly the ordinary Schur complement. A full inductive or exterior-algebra proof and numerical check are still required for many slices; zeros of the recurrence alone would not determine the determinant prefactor.

Jacobi's complementary-minor identity gives det X_(++)=det X det(X^-1)_(--), and det X_t=det A_t/det D_t. Hence(H.1) would equivalently read

    det(delta D_full)=product_t det A_t * det((X^-1)_(--)).    (H.2)

The temporal normalization is(1+mu delta)^(2rM_t). Since each X_t is Hermitian, the modulus of the final determinant in(H.2) equals that of the negative-sector minor of the chronological product X_(M_t-1)^-1...X_0^-1. On fermion Fock space, that minor is the matrix element of the corresponding exterior-power product between states Omega_- filling all r negative gamma_0 orbitals. This fixes a boundary state, not a thermal trace.

As delta M_t->T at fixed spatial graph with a continuous external gauge history, X_t^-1=I-delta h_t+O(delta^2). The candidate paired determinant limit is therefore

    |<Omega_- | Texp[-integral_0^T (dGamma(h_t)+mu r I)dt]
                                                   |Omega_->|^2.     (H.3)

The scalar mu r comes from product det A_t divided by the fixed temporal normalization: log det A_t=delta Tr a_t+O(delta^2)=delta mu r+O(delta^2). At K_s=0 the filled state has dGamma(mu gamma_0) energy-mu r, so(H.3) equals1 as required. Omitting that scalar would produce an exponentially wrong normalization.

The exact finite-delta prefactor product det A_t is gauge dependent. It may approach the stated constant only after its error is priced, rather than being dropped at finite step. The finite-graph product error can be bounded by ordinary bounded-matrix estimates, but no spatial-volume-uniform operator norm follows. The pairing and time-order reversal in(H.2)-(H.3) also need an explicit check for noncommuting time histories.

The boundary filled state has two fermions per spatial site per flavor. A charge convention subtracting that supplied background is needed when joining a dynamical gauge Gauss law. The current fixed-background determinant/source bound does not itself construct that physical joint Hilbert space. Antiperiodic time would select a trace with winding terms, a separate problem.
