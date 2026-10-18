# Rational polar residual eigenvalue enclosure

The proposed bound is valid for the operator/spectral 2-norm. Let A=A^dagger be dxd, U square with rational complex entries, D real diagonal, and suppose exact rational upper bounds satisfy

    ||U^dagger U−I|| <= delta < 1,
    ||AU−UD|| <= r.

Then U is invertible and its polar unitary V=U(U^dagger U)^−1/2 satisfies

    ||V−U|| = max_j |1−sigma_j(U)|
             <= 1−sqrt(1−delta)
             =delta/[1+sqrt(1−delta)] <= delta.

The last, weaker version is entirely rational. Since V is unitary,

    ||V^dagger A V−D|| = ||AV−VD||
       <= ||AU−UD|| + (||A||+||D||)||V−U||
       <= r+(||A||+||D||)delta = e.

Weyl's Hermitian eigenvalue inequality therefore places each sorted eigenvalue of A within e of the corresponding sorted diagonal value of D. D need not be stored sorted; sorting for interval comparison is enough. No claim that a particular column labels an exact eigenvector is required.

For any rational complex matrix X, replace each entry modulus by |Re X_ij|+|Im X_ij|. Its maximum row sum bounds ||X||_infinity, its maximum column sum bounds ||X||_1, and max(those two) bounds ||X||_2 because ||X||_2<=sqrt(||X||_1 ||X||_infinity). For Hermitian X the two true absolute-sum maxima agree, and either appropriately computed symmetric bound suffices. D's norm is max |D_jj|. All arithmetic can therefore remain rational; there is no need to trust floating-point eigensolver orthogonality or residuals once the approximate U,D entries are frozen as rationals and checked.

For two momenta, four such one-particle enclosures give transition intervals

    lambda_b[h(k+Q)]−lambda_a[h(k)]
      in [D_b^+−D_a^−−(e_++e_-),
          D_b^+−D_a^−+(e_++e_-)].

If **every** transition interval at the first momentum is strictly disjoint from **every** transition interval at the second, the two exact transition spectra have no common real energy. That is enough for the analytic no-flat argument, independent of a modular polynomial certificate.

For a rounding-robust neighborhood, add independently certified operator-norm bounds on changes in each h(k), including both momenta. Weyl enlarges each eigenvalue interval by that perturbation bound, and transition intervals by the sum of endpoint bounds. Strict interval separation surviving these enlargements proves the same no-common-real-root property throughout that declared neighborhood. The perturbation set and its norm bound must be supplied explicitly; a positive nominal separation alone is not yet a quantified coefficient-neighborhood theorem. Hermiticity and finite-range analyticity must remain true throughout the neighborhood.
