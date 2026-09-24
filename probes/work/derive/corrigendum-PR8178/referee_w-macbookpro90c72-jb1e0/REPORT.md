# Referee: corrigendum PR #8178, a2

Author `w-jonathonsmac4f50-j888a` (claude-opus-5). Referee `w-macbookpro90c72-jb1e0` (grok-4.6).

## Steps

1. **S1–S5 follow.** A shift `θ ↦ θ_{·−e}` multiplies `Σ e^{∓ik·x} θ_x` by `e^{∓ik·e}`. So the backward average has multiplier `φ_c` under `e^{−ik·x}` and the stated `φ` under `e^{+ik·x}`. `φ − φ_c = (2i/3)(sin k₁ + sin k₂)` and `|φ| = |φ_c|`, with `|φ|² = (3 + 2 cos k₁ + 2 cos k₂ + 2 cos(k₁−k₂))/9`. On `L = 3, 4`, every mode satisfies `P e_k = φ_c e_k` and `Pᵀ e_k = φ e_k` for `e_x = e^{+ik·x}`. Since `conj(φ_c) = φ`, an `fft2` coefficient that steps by `φ_c` is measured as `φ`.

2. **S6 follows at `e6ffae5b460b`.** Note line 85 states both the minus transform and the multiplier `φ` in one sentence. T1.1's proof says the conjugate convention gives the stated `φ`. A search of the PR's formula lines finds exactly ten, and the one absent from a1's nine is `HANDOFF.md:30`. The runner writes `φ` with `+i`, so repair B is two clauses of prose and repair A edits executed code, the check text, and the frozen cache.

Both repairs are correct. The cheaper one, if the executed evidence is to stay put, is the transform.
