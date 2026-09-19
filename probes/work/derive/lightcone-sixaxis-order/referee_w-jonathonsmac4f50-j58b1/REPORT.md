# Referee report: J:derive:lightcone-sixaxis-order:a1

- **Author:** w-macbookpro90c72-jb723 (grok-4.6).
- **Referee:** w-jonathonsmac4f50-j58b1 (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` as run in its log `w-macbookpro90c72-jb723__92316183__20260919T014608Z`.

**Disclosure.** This referee's model family refereed attempts a2 and a3 of this problem (grok). `check.py` is independent exact code.
Nothing is taken from the author's script.

## The claim

`π ∝ ∏ₓ Zₓ`, with `Zₓ = Σ_u ∏_{y∈N(x)} W(u, s_y)`, is a 7-body (or 6-body) Gibbs weight and not pairwise. The evidence given is the
cross-ratio of the two opposite stencil sites, which is not 1. So block 17's pair-matrix RP does not transfer.

## Step by step

**Step 1 (explicit `Z`): holds.**

**Step 2 (cross-ratio): holds as a computation, but it shows less than claimed.**
- **The number is right.** Y1: `(p⁷+q⁷+4r⁷)(p⁵q²+p²q⁵+4r⁷)/(p⁶q+pq⁶+4r⁷)² = 128925/96721 ≠ 1` at `(3,1,2)`.
- **What it detects.** A cross-ratio measures the coupling between the two varied sites. Here those sites are opposite, at distance 2.
- **What it proves.** `π` is not the nearest-neighbour pair law `exp(Σ_{⟨xy⟩} log W)`, since the opposite sites are not neighbours. That is
  the question the attempt set out to decide.
- **What it does not prove.** It does not show that `log Z` is not a sum of pair terms. A single distance-2 pair term reproduces any
  cross-ratio (Y2).
- **"Not pairwise" is still true, by a higher difference.** Y3: the third-order mixed difference over three sites, each switching
  `+z ↔ −z`, is `Z₀Z₂³/(Z₁³Z₃) = 940662585/932487161 ≠ 1`. So `log Z` has a genuine three-body term.
- **"7-body" is also true, but needs mixed switches.** Y4:
  - in the `±z` sector the seventh-order difference is exactly 1, by the symmetry `Z_k = Z_{7−k}`;
  - with sites 1–3 switching `+z ↔ −z` and sites 4–7 switching `+z ↔ +x`, it is `1.0265 ≠ 1`.

**Step 3 (block 17 does not transfer): holds.** `π` is not the pair law `W`, so the pair-matrix RP of block 17's T2 would have to be
re-established for `log Z`.

## Verdict

The claim survives, with a corrected argument. The cross-ratio settles only "not the nearest-neighbour pair law". The third- and
seventh-order mixed differences settle "not pairwise" and "genuinely 7-body".

`check.py` prints `HIT: confirmed - ...` and its SUMMARY line.
