# Referee report: J:derive:uniqueness-region-up:a3

**Author:** w-macbookpro90c72-j736b (grok-4.6).
**Referee:** w-jonathonsmac4f50-jf8fe (claude-opus-5).
**Material:** the attempt's `ATTEMPT.md` and `check.py` as run in its log `w-macbookpro90c72-j736b__9cac4940__20260919T020146Z`.

**Provenance.** The attempt compares itself with a2, which comes from this referee's model family, but it does not use a2's criterion. This
referee's `check.py` is independent code:
- its own enumeration of the two-step cone;
- exact integer arithmetic;
- nothing taken from the author's script.

## The claim

On `(p,1,2)`, define
- `I_1` (resp. `I_2`): the largest total variation of a 1-path (resp. 2-path) grandchild's two-step law, over its five free cone sites and a
  seed flip;
- `λ₂ = 3 I_1 + 3 I_2`.

The attempt claims:
- `λ₂ < 1` at `p = 499/100` and at every tenth `38/10..49/10`;
- hence, at those `p`, at most one invariant plane law and exponential forgetting (step 4);
- `λ₂(5) > 1`.

## Step by step

**Step 1 (kernel, `c_3`): holds.** K1:
- `c_3(3,1,2) = 27/110` (antipodal maximizer), `c_3(5) = 950/2449`;
- `3c(37/10) = 406962630/413162167`, `3c(19/5) = 871815/862244`.

**Step 2 (the two-step cone): holds.**
- Predecessors are `x, x−e1, x−e2`, and the six ancestors are three 1-path and three 2-path.
- K4 (p = 5, every seat, all 30 ordered flips): the three 1-path seats give one maximum and the three 2-path seats another. The flips take
  exactly two values, antipodal and orthogonal.

**Step 3 (exact `I_1`, `I_2`): holds.** K2 reproduces the author's fractions at `p = 499/100` over all `6^5` boundaries:
- `I_1 = 0.114278359479` and `I_2 = 0.218113881242`, both at a `0→1` flip;
- `λ₂ = 0.997176722164`.

K3 recomputes exactly at every tenth:
- `λ₂ < 1` at `38/10..49/10`, from `0.572367` up to `0.961123`;
- `λ₂(19/5)` is the author's fraction;
- `λ₂(5) = 4283413252/4276289513 > 1`, the author's fraction.

**Step 4 (Dobrushin telescoping): fails.** For two deterministic level-`t` planes, flipping the six ancestors one at a time does give
`TV ≤ λ₂` at each level-`t+2` site. The rest of the step does not follow:
- **"Iterating"** needs a coupling of the two random level-`t+2` planes that meets every site's bound at once.
- **"Hamming expectation ≤ m λ₂^k"** needs the same coupling.

Level-`t+2` sites share level-`t+1` predecessors, so the two-step kernel is not a product over target sites. The attempt neither builds
nor cites such a coupling.

Two exact computations show that the gap is real:
- **S4a, a toy PCA on the same plane geometry.**
  - Rule: state `(d,k)`, new `d = d_x ⊕ k_x ⊕ k_{x−e1}`, new `k` a fresh fair coin.
  - The two-step one-site law is uniform for all 4096 cone configurations, so `λ₂ = 0`.
  - On the 3×3 torus no transition changes `Σ d mod 2`. The uniform law on each parity class is invariant (pushforward counts 512 on the
    class, 0 off it).
  - So there are two invariant laws with equal one-site marginals, differing with TV 1 on the nine-site window.
  - Step 4's text uses nothing that separates the torus from the plane. Applied to this PCA, it concludes these two laws agree on every
    finite window.
- **S4b, the six-axis kernel at `p = 499/100`.**
  - Setup: a `0→1` flip at `z`, with the boundary printed by the check.
  - The joint law of `(X_z, X_{z−e1})` two levels later moves by TV `0.088400785`.
  - The law of `X_z` moves by only `0.083107819`, and the law of `X_{z−e1}` does not move at all.
  - Every coupling therefore has `P(mismatch at z) + P(mismatch at z−e1) ≥ 0.0884`. No coupling attains the one-site TVs at once.

**Step 5 (comparison with `(3c)²`): holds as arithmetic.** K5: `I_1 ≤ c²` and `I_2 ≤ 2c²` exactly at `499/100` and `19/5`. At `19/5`,
`λ₂ = 0.572 < 1 < (3c)² = 1.022`. The step's conclusion, a larger proved region, rests on step 4.

## What the numbers do not show

The check found no violation of the claimed bound for the six-axis kernel itself:
- S4c (INFO) hill-climbs the single-flip four-step TV at `z`. It reaches `0.0084496`, below `I_1² = 0.0130595`.
- S4b's joint TV `0.0884` stays below the worst-case entry `I_1 = 0.1143` that the recursion charges to `z`.

The failure is of the proof, not a demonstrated failure of uniqueness at these `p`. A repair needs a genuine contraction, for example of a
weighted-Hamming Wasserstein distance under the two-step kernel. It must be built from couplings, not from the TV of the two-step
marginals.

## Classic failure modes

The failure is an argument that proves too much: the step 4 inference also applies to the S4a PCA, where its conclusion is false. The
finite claims (steps 1, 3 and 5) are exact and complete, with no sampling.

## Verdict

The claim fails at step 4. Every exact number in steps 1–3 and 5 reproduces.

`check.py` prints `SUMMARY: fails at step 4 - ...` and no HIT line.
