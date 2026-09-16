# Working extension: the first transverse excitation sector

Exploration, not a completed theorem. The new all-affine normalization estimate can control a true orthogonal excitation sector of the variational embedding, rather than replacing its leakage by a small compressed error.

Use the BLOCK01 notation. In charge sector Q, let m_Q=<n>_Q and define, for a real or complex f in S,

    W_Q(f)=sqrt(2) g [(K^(1/2)f).(n-m_Q)] psi_Q.

Use the usual complex-linear convention for f and Hilbert inner products. These vectors are orthogonal to psi_Q. Their Gram matrix is

    G_Q=I_S+(1/(2g^2)) A^(1/2) F''(a_Q) A^(1/2),
    ||G_Q-I||<=sqrt(12) epsilon/(2g^2)=:rho.

Thus, for the small-g range of BLOCK01, W_Q G_Q^(-1/2) is an isometry from the transverse one-particle space S to a subspace exactly orthogonal to psi_Q. This is the first centered polynomial sector of the chosen Gaussian reference, not an eigen-subspace of the full compact Hamiltonian.

For a link raising E by e, put t=P e and a=a_Q. The overlap weight has midpoint coset a+t/2. Writing m(b)=-A grad F(b)/(2g^2), its exact vector in the final centered sector is

    b_Q(e)=sqrt(2)g G_(Q+De)^(-1/2) K^(1/2)
             [m(a+t/2)+t/2-m(a+t)] I_Q(e).

The gradient difference, rather than either extensive mean, is the useful quantity. The Hessian bound implies

    ||K^(1/2)[m(a+t/2)-m(a+t)]||
      <=sqrt(||A||) epsilon ||t||/(4g^2).

Together with ||K^(1/2)t||^2=K_ee<=14 and the Gram inverse-square-root bound, this suggests

    ||b_Q(e)-(g/sqrt(2)) eta_e K^(1/2)P e|| <=C epsilon/g

uniformly in volume and in Q. Opposite link shifts reverse the leading vector. Summing the oriented hopping and its adjoint therefore exposes a current vertex with the expected transverse square-root covariance, while compact corrections remain exponentially small.

Critical remaining steps: fix bra/ket and charge-shift signs against a direct physical-basis calculation; prove the exact orthonormalized-sector formula; give explicit constants; distinguish a per-link bound from an extensive sum; do not identify this sector with actual stable photons or infer a Feshbach gap. The free small-k form factor is |k|^(-1/2), so a global dynamical elimination requires more than the finite norm of a local vertex.
