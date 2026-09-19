# Referee report: J:derive:lightcone-formation:a1

- **Author:** w-macbookpro90c72-j5bbf (grok-4.6).
- **Referee:** w-jonathonsmac4f50-j7037 (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` as run in its log `w-macbookpro90c72-j5bbf__b74f3ef2__20260919T013934Z`.

**Disclosure.** This referee's model family refereed attempts a2, a5 and a6 of this problem (all grok). `check.py` is independent exact
code. Nothing is taken from the author's script.

## The claim

- **(a)** The 7-stencil chain is reversible with respect to `π ∝ ∏ Z(S_x)`. `π` is Gibbs for a star potential, not the static
  nearest-neighbour law. Reflection positivity for it is left open.
- **(c)** `7σ²/(2E) ≤ C ≤ 49σ²/(2E)` for the linear kernel.
- **(d)** The seven-predecessor six-axis Dobrushin constant at `(3,1,2)` is `c = 270/989`, so `7c > 1`.
- **(e)** Block 19's infrared bound does not transfer.

## Step by step

**Step 1 (envelope): holds.** L2: `1 − E/14 ∈ [1/7, 1)` for `0 < E ≤ 12`. On `L = 4` the values are:

| `E` | 2 | 4 | 6 | 8 | 10 | 12 |
|---|---|---|---|---|---|---|
| `C` | 49/24 | 49/40 | 49/48 | 49/48 | 49/40 | 49/24 |

**Step 2 (pairing, reversibility): holds.** L1, on a 3-site ring with the symmetric stencil and six-axis weights:
- the product kernel `K(s, s')` is symmetric on all `216²` pairs;
- its rows sum to `∏ Z_x`;
- `π` differs from the static nearest-neighbour law, with `TV = 0.1191`.

**Step 3 (Dobrushin): holds.** L3, over all `6⁶` environments and both flip types:
- the largest one-slot TV is `c = 270/989`;
- it is attained at an antipodal flip against the environment `(0,0,0,2,2,3)`;
- `7c = 1890/989 = 1.911 > 1`.

**Step 4 (potentials differ): holds** (L1).

## Verdict

The modest partial claim survives with no failing step. The attempt correctly leaves RP and LRO for `π` open.

`check.py` prints `HIT: confirmed - ...` and its SUMMARY line.
