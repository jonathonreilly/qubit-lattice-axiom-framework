# Independent corrected-operator bounds review

**Disposition:** no material defect found for the specified six cases. The form realization, tail comparison, rational spectral counts, interval subtraction and upward decimal rounding support the claimed finite-case bounds. This is an independent bounded check, not a uniform asymptotic theorem, empirical model identification or formal audit.

## Form realization and compactness

The coefficient identity is correct: H0+xH1 has diagonal 4K(1−2x)n²−4delta(1−2x) and adjacent t_n=−2delta(1−2x)+4Kx n(n+1). For integer n, both n(n+1) and n(n−1) are nonnegative, and their sum is 2n². For 0<=x<1/4,

    |t_n|+|t_(n−1)| <= 4delta(1−2x)+8Kx n².

Using 2|psi_n psi_(n+1)|<=|psi_n|²+|psi_(n+1)|² gives the sharper lower estimate

    q[psi] >= 4K(1−4x)||n psi||² −8delta(1−2x)||psi||²,

which implies the stated weaker bound with −8delta. The corresponding upper bound is q[psi]<=4K||n psi||². Thus q+(8delta+1)||psi||² is a positive norm equivalent to ||psi||²+||n psi||² for every fixed allowed x. The sesquilinear form extends continuously to D(n); norm equivalence makes it closed there. Finite support is a form core by truncation. The representation theorem defines a unique self-adjoint operator for this specified closed form.

The embedding D(n) into ell²(Z) is compact: outside |n|<=N the unweighted squared norm is at most N^−2||n psi||². Therefore the form-associated operator has compact resolvent. This justifies the specified realization without assuming that an unbounded off-diagonal Jacobi matrix is a bounded perturbation of H0. It does not assert uniqueness of every possible operator-extension construction or a global microscopic equivalence.

## Tail and count argument

Restricting the form to either excluded half-line is equivalent to setting the retained components to zero, so the same lower bound applies with n²>=(L+1)². The omitted boundary contribution is zero on these restricted vectors, not an extra uncontrolled form term. For E below the tail lower bound, the direct-sum tail resolvent is positive and norm bounded by the inverse gap.

The coupling between the finite retained space and the tails is finite rank, even though the hopping coefficients grow at infinity. Its two boundary matrix elements are t_L and t_(-L−1)=t_L. With L30 the sites are distinct, giving B*B=t_L² Pi_boundary. Hence the proposed beta and operator-order self-energy sandwich are correct. Positive-tail block elimination and the closed-form Schur argument preserve the negative index. The finite comparison matrices have the stated diagonal and adjacent coefficients; exact Fraction pivots count their inertia correctly when nonzero. Matching counts provide global eigenvalue indices of the form-defined approximate operator. The endpoint conditions are checked at every accepted energy.

## Independent exact computation

`independent_corrected_bounds_check.py` imports no author implementation. It constructs diagonal and off-diagonal coefficients by adding separately written H0 and xH1 terms, then uses sign variations of exact leading principal determinants instead of the author's LDL pivot divisions. It checks both tail comparison matrices at all fourteen endpoints in each of the six cases—84 independently recomputed endpoint counts. Every case gives [j,j+1] for j=0…6, and every energy width is exactly 2e−9.

All gap intervals were reconstructed from the corresponding energy intervals. All six signed microscopic-minus-approximate gap-difference lists were independently obtained as [micro_lo−approx_hi, micro_hi−approx_lo]. Their maximum absolute endpoints agree exactly with corrected_operator_error_bounds.json. Each table entry was verified by an integer ceiling after multiplication by 10^12:

| delta, K=1 | S20 | S50 | S120 |
|---|---:|---:|---:|
| 1 | 0.004987235265 | 0.000136754425 | 0.000004229203 |
| 15803623/500000 | 6.647658236470 | 0.281239142371 | 0.009192992163 |

These are conservative bounds on the maximum absolute error across the six specified excitation gaps, not signed errors or exact error values. Exact subtraction needs no independence assumption about the enclosure errors.

A fresh run of the author certificate script also reproduced all six saved records exactly. Reducing the approximate-operator interior hopping magnitudes by 1% at the original frozen ground-state brackets gives counts [0,0] in every case and is rejected against the required [0,1]. This is a specified fault test, not proof that arbitrary coherent source/certificate errors are detected.

Evidence is saved in `independent_corrected_bounds_check.json` and `independent_fresh_corrected_certificate.jsonl`. The finite microscopic input intervals retain the verification scope recorded in INDEPENDENT_CERTIFICATE_REVIEW.md: all author cases were freshly rerun, with independent finite-matrix reconstruction at S20 and the larger ratio. This extension independently reconstructs all six approximate-operator cases and every interval subtraction.

## Limits and source identities

The form coercivity is for fixed 0<=x<1/4; its constant degenerates as x approaches 1/4. The six interval bounds do not establish a uniform O(x²) approximation, an asymptotic coefficient, an estimate for all spin values, or a bound for measured-device residuals. They concern the full spectrum of the specified approximate operator H0+xH1, not merely first-order expectation shifts; diagonalizing it incorporates higher powers of x and therefore need not have the same finite-case error as first-order perturbation theory. Physical parameter uncertainty, finite-spin identification, offset, cavity, and preparation/readout remain outside the claim.

No author source was edited and no publication or audit action was taken. Exact SHA-256 identities:

- `CORRECTED_OPERATOR_BOUNDS_DRAFT.md`: `705ac36ff6324a86cd911579451f04b81d6f52519aa5a4a45855702eb417a0f5`
- `corrected_operator_certificate.py`: `cc94b8ac7a4b5cd41e134e52fcf40b0f8501ec6d711293b35a9f003d832a6c2d`
- `corrected_operator_certificate.jsonl`: `a91436390fc3e8a0ee5d9bdce42da25328101fb15d77b73a5a0d66638f3b63dc`
- `corrected_operator_error_bounds.json`: `8625b7bec024614d9aa081c0476cfe09fca4b04d1a8274ccff8345497004b3e6`
- `rational_spectral_certificate.jsonl`: `cca2365d0e2a88a7d12c1ee1bff4d7b9a9a247637cbe575ae7b501643290ed18`
