# B5 independent check: the refutation holds, with corrections

Provenance: a fresh-context agent of the same model family. It read the PR #9695 and #9696 heads and main directly. Saved by the supervisor from the hand-back.

## Arithmetic reproduced from the notes' own bounds

- tol·M is 50 for the structured device and 0.192 for the mediated one: a ratio of 260.
- The bond increment is < 5.3e6·ε, with no dependence on T or M.
- The onsite increment is 422·ξ/λ.

## Corrections

1. **The margin is larger than reported.** Against the note's own 0.0005 target, ε ≈ 1e−9 still passes. The onsite 1e−26 is a budget choice; ξ ≈ 2e−24 still passes. Neither tolerance tracks 1/M, nor a fixed multiple of λ.
2. **Receiver errors.** A common receiver-bond error scales exactly as 1/(γT): it is a time rescaling. The FINDINGS exponent T^−0.4…−0.5 belongs to independent bond errors, a different class.
3. **The nominal-clock "1/T obligation" is overstated.** C(w)·I is a global phase on the whole Hilbert space, passive references included. The fixed-phase vector metric sees it, but no channel or relational measurement can detect it. So a co-transported reference adds nothing for this term. The physically real 1/T effects come from receiver errors and global onsite errors, which act as clock-rate errors.

## Own model (`b5c_fast.py`, `b5c_fast.log`)

| Error | Result |
|---|---|
| Source bond, actual scalar | ≈9.8e−3, flat in T (312, 625, 1250) and in λ (0.01–0.16) |
| Source onsite, actual scalar | ≈0.014·λ, flat in T |
| Source bond, nominal clock | exactly 1e−2/(γ·2T) |

## Caveats

- The source-bond tolerance is O(m·ε), weakening like 1/log M along the design family; that is not 1/M.
- 5 of 7 planned scan rows finished.
