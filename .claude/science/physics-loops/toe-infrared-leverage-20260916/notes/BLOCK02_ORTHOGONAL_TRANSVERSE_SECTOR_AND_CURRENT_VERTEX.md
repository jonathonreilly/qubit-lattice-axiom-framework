# An orthogonal transverse sector and its current vertex

**Author theorem proposal.** This depends on the provisional [global Gauss-dressing theorem](BLOCK01_GLOBAL_GAUSS_DRESSING_AND_VARIATIONAL_COMPRESSION.md). No independent review, audit, eigenstate interpretation or dynamical phase theorem is asserted.

The new result identifies the leading hopping matrix element from the charge-dependent trial vacuum into a normalized, exactly orthogonal transverse excitation sector. Its compact correction is uniform in box size and charge configuration. It does not identify that sector with stable physical photons.

## 1. Exact first centered sector

Use BLOCK01 notation, and let S_C be the complexification of S. The Gaussian electric state in charge sector Q has n=E-e_Q and mean m_Q. For f in S_C define the complex-linear map

    W_Q f = sqrt(2)g [(K^(1/2)f).(n-m_Q)] psi_Q.

The dot product in the wave function is bilinear, so the resulting Hilbert inner product is conjugate-linear in the first f. By centering, W_Q f is exactly orthogonal to psi_Q. Its Gram matrix is

    G_Q=W_Q*W_Q
       =I_S+(1/(2g^2))A^(1/2)F''(a_Q)A^(1/2).        (1)

This follows from the exact covariance in BLOCK01, not from a continuum approximation. With

    rho=sqrt(12)epsilon/(2g^2),

we have ||G_Q-I||<=rho. In the stated g<=0.1 range, rho<1/2. Thus W_Q G_Q^(-1/2) is an isometry from S_C into the gauge charge sector. Define the whole-matter map

    V_1(f tensor |b>)=|b> tensor W_(Q(b))G_(Q(b))^(-1/2) f.

It is an isometry, and V_1*V_g=0 exactly. Matter basis orthogonality handles different b even when their charges coincide. This is a centered polynomial sector of a chosen reference, not a conserved photon-number subspace of the full Hamiltonian.

## 2. Exact normalized link vertex

Consider a positive link shift U(e), from charge Q to Q+De, and put a=a_Q, t_e=P e. The new integer representative may be E0+e, so its affine coordinate is a+t_e. All formulas are invariant under changing that representative by Lambda.

The electric overlap weight in equation(10) of BLOCK01 has midpoint variable y=n+t_e/2 distributed with the Gaussian weight on Lambda+a+t_e/2. In the final sector n'=n+t_e=y+t_e/2. Therefore the exact vector obtained by projecting U(e)psi_Q onto the normalized final centered sector is

    b_Q(e)=sqrt(2)g I_Q(e) G_(Q+De)^(-1/2) K^(1/2)
             [m(a+t_e/2)+t_e/2-m(a+t_e)],             (2)
    m(b)=-A grad F(b)/(2g^2).

The final mean must be subtracted. Dropping either affine mean before establishing a difference bound is incorrect; the individual means are not bounded in volume by their Euclidean norm.

By the uniform Hessian estimate,

    ||K^(1/2)[m(a+t_e/2)-m(a+t_e)]||
       <=sqrt(||A||)epsilon ||t_e||/(4g^2).           (3)

The cancellation in (3) is why the volume-independent bound survives. It uses K^(1/2)A=A^(1/2), ||t_e||<=1, and a difference of gradients separated by t_e/2.

Let v_e=K^(1/2)P e, so ||v_e||^2=K_ee<=14. Cauchy-Schwarz gives 0<I_Q(e)<=1, and BLOCK01 gives |I_Q(e)-eta_e|<=epsilon/4. Spectral calculus on [1-rho,1+rho] gives

    ||G_Q^(-1/2)||<=sqrt(2),
    ||G_Q^(-1/2)-I||<=2rho.

Insert these in (2)-(3) to obtain

    ||b_Q(e)-(g/sqrt(2))eta_e v_e||
      <=[sqrt(sqrt(12))/2+sqrt(7)sqrt(12)+sqrt(7)/4]
           epsilon/g
      <12 epsilon/g.                                (4)

The same argument applies to -e, with the leading vector negated. This is a per-link bound for every allowed source charge Q and every box size, at fixed sufficiently small g. It includes the Gram normalization and affine charge dependence.

## 3. The hopping current and the extensive bound

Write the free oriented matter hop as

    h_(e,s)=c_(x,s)^dagger T_(e,s)c_(y,s), s=+1,-1.

Only the hopping part of the full Hamiltonian is considered in this section. Its exact matrix from V_g to V_1 satisfies

    V_1* H_hop V_g
      =(g/sqrt(2)) sum_(e,s) s eta_e v_e tensor
                        [h_(e,s)-h_(e,s)^dagger] + R_10,
    ||R_10|| <=144 t_* V epsilon/g.                  (5)

Each error is a vector-valued diagonal charge function of norm <=12epsilon/g followed by the corresponding free hop, whose norm is <=t_*. Adding both orientations and species and E_edges<=3V gives the displayed conservative bound. A per-link estimate is not silently substituted for the norm of an extensive sum.

With the Hermitian current convention

    J_e=-i sum_s s[h_(e,s)-h_(e,s)^dagger],

which equals minus the derivative of the unscaled hopping Hamiltonian with respect to the link angle at zero, the leading expression is

    i(g/sqrt(2)) sum_e eta_e v_e tensor J_e.

The factor i belongs to the convention in which the reference excitation is a real centered electric-coordinate polynomial. Its sign is fixed by the charge-raising shift in (2); changing an excitation's overall phase changes this display and no physical prediction.

H_on has zero matrix between V_g and V_1 because it preserves every local charge and the two gauge sectors are orthogonal. Equation(5) does not include the electric and magnetic Hamiltonian's matrix into V_1 or any higher excitation sector. Those are separate matrix elements, not assumed absent in the compact model.

## 4. Scientific consequence and limit

The same globally Gauss-constrained reference that yields the Coulomb variational matrix has a nonzero transverse current vertex of order g. Its local norm remains finite as the box grows. Thus an exponentially small compact correction in the vacuum compression does not mean that the coupling to transverse excitations is exponentially small. The actual charged-ring calculation in BLOCK01 already exhibits this distinction directly.

The mode profile v_e involves A^(-1/2). A dynamical elimination also needs energy denominators and actual matter-current correlations; none follows from the local finiteness of v_e. This result supplies a controlled reference vertex for that next calculation. It proves neither physical photon stability nor a vanishing effective interaction at long distances.

## 5. Personal verification

The separate rank-five cube implementation constructs the electric sums and centered polynomial wave functions directly, then compares their Gram matrix, orthogonality, orthonormalization and charged-hop projection to dual-theta derivatives. It uses g=0.8,1.2,1.6 to expose charge-dependent corrections in finite identities. These values are outside the conservative uniform theorem range and are not used to validate an all-volume small-coupling bound by sampling.

Observed Gram and vertex discrepancies are near floating arithmetic precision; omitting the affine means gives a visible error, about0.108 in the last case. The comparison retains its actual finite cutoffs. It is an author calculation, not an independent mathematical review or a computation of an infinite-volume phase.
