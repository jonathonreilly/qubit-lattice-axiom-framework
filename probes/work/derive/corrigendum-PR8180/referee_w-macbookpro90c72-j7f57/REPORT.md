# Referee report: J:derive:corrigendum-PR8180:a1

- **Author:** `w-macbookpro90c72-j4077` (`claude-opus-5-5`).
- **Referee:** `w-macbookpro90c72-j7f57` (`grok-4.6`). Different model family.
- **Checks:** characters on `L = 3, 4, 6`, the real-mode criterion, the Hessian, and the cone expansion. The author's script is not called.

## The statement

With the minus transform, `P` multiplies `e^{ik·x}` by `conj(φ)` and `Pᵀ` by `φ`. The covariance display `φ^s Var` matches the pairing `E[X conj(Y)]`. The evolution line `φ^s` is the wrong multiplier except where `φ^s` is real. The comparator `E` is elliptic and the formation symbol is parabolic along `(1,1,1)`.

## Steps

**S1–S2.** On every mode of `L = 3, 4, 6`, `(Pe_k)/e_k = conj(φ)`. `Im φ = (2/3) sin((k₁+k₂)/2) cos((k₁−k₂)/2)`, so `φ` is real exactly when `k₁+k₂ ∈ 2πℤ` or `k₁−k₂ ∈ π+2πℤ`. Non-real modes: 6 of 9, 10 of 16, 24 of 36, counting the zero mode. On `L = 4` the mode `(1,0)` is a genuine eigenvector with eigenvalue `conj(φ)`, and `φ` is not real.

**S3–S5.** The display and the gloss agree when `φ^s` is real: 8 of 24 pairs on `L = 3`, 19 of 45 on `L = 4`, 47 of 105 on `L = 6`. They differ on the rest, not on every nonzero mode.

**T3.** `3|1−z|² = E − 3(1−u)`. Both vanish only when every momentum is in `2πℤ`, so in a full neighbourhood of the origin neither is a product of a plane function and a line function. `Hess E = 2I` and `Hess 3D = (2/3)11ᵀ`. Along `K = εa + ε²b(1,1,1)` with `a` perpendicular to `(1,1,1)`, `E = ε²|a|² + O(ε³)` and `3D = ε⁴(3b² + |a|⁴/12) + O(ε⁵)`.

The line-by-line pack audit was not repeated.

## Verdict

The corrected T1 and T3 survive. The display stands; the multiplier sentence has to say `conj(φ)`.
