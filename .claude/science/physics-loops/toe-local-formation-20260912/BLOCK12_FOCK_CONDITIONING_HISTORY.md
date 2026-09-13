# Fock check conditioning history

The first run formed its finite source Gram matrix in unscaled fields K^j a,
K^j d,w. Its compressed free generator had a relative anti-Hermitian roundoff
residual2.028344229557965e-9, exceeding the fixed2e-9 gate, and refused before
any moment comparison. The corrected implementation first normalizes the
thirteen field coordinates, constructs the same compressed Hermitian form,
and then restores original field amplitudes. The gate and claimed moments
are unchanged. The earlier refused check is not counted as passing evidence.

Normalizing field coordinates alone still refused with anti-Hermitian residual
1.9271550342345304e-8. The revised implementation therefore constructs the
actual positive-frequency vectors(f+i Gamma f)/sqrt2 on the finite AP torus,
uses their thin SVD, and compresses the diagonal positive one-particle frequency
operator directly. This avoids forming/inverting the ill-conditioned Gram
matrix. All moment, reconstruction and Hermiticity gates remain unchanged.
