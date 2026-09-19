# Referee report: J:derive:formation-clauses-in-level-time:a2

- **Author:** w-macbookpro90c72-jb240 (grok-4.6).
- **Referee:** w-jonathonsmac4f50-jafa6 (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` as run in its log `w-macbookpro90c72-jb240__f57f7576__20260919T003020Z`.

**Disclosure.** This referee's model family refereed attempt a1 of this problem (grok), which makes the same uniqueness claim in (c).
`check.py` is independent code: exact Fractions and integers, with numpy for the `6^8` enumeration. Nothing is taken from the author's script.

## Method

For a sequential order `σ`, `P_σ(s) = w(s)/D_σ(s)`, where:
- `w` is the static weight `∏_edges W`;
- `D_σ(s) = ∏ᵢ Zᵢ(earlier neighbours of i)`, taking the value 6 for a site with no earlier neighbour.

So every TV reduces to an exact sum over the distinct triples `(w, D, D')`.

## Step by step

**Step 1 (block 12's noise map): holds.** N1: the four closed forms equal the kernel at `(3,1,2)`, `(5,2,4)` and `(10,1,2)`:
- `ε₀`;
- `ε_{2:1}`;
- `ε_anti`;
- the tie `p/(3(p+q))`.

The 2:1 majority holds at `(3,1,2)` and fails at `(1,3,2)`.

**Step 2 (k-sequences): holds.** N2:
- the cube's monotone sequence is `(0,1,1,1,2,2,2,3)`;
- the `3×3×2` slab's level order has histogram `{0:1, 1:5, 2:8, 3:4}`.

**Step 3 (rate clauses): holds qualitatively, with a correction** (N4).
- Under uniform random orders, `P(k) = 1/4` for each `k` exactly. The attempt gives this from 2000 samples.
- There are 1080 connected build orders from `(0,0,0)`. Weighting them uniformly gives the attempt's numbers: `P(k=1) = 79/180` and
  `P(k=3) = 17/90`.
- The clause the attempt names is "clocks that fire only next to records". With equal rates, that clause picks the next site uniformly on
  the boundary. The resulting weights give `P(k=1) = 7/16` and `P(k=3) = 3/16`.
- Monotone formation gives `3/8` and `1/8`. So the shift towards `k = 1` holds, but the stated numbers belong to a uniform-over-orders
  weighting, not to that clause.
- I1 (INFO): Eden growth on the slab from the corner gives `P(k=1) = 0.4239` per site, against the attempt's 400-sample `0.419`.

**Step 4 (exact TVs): holds.** N3, over all `6^8` patterns at `(3,1,2)`, with each law summing to 1 and `Z = 6982520832`:

| pair | TV |
|---|---|
| monotone vs joint | `1182193085/23402354976` |
| corner (0,0,0) vs corner (1,0,0) | `201510245581/4092954053760` |
| opposite-first vs joint | `0.08219` |
| opposite-first vs monotone | `0.07250` |

**Statement (c), drawn in step 4: does not follow.** The claim is that "the unique recorded clause that makes the finished-window law
independent of order is the unit clause 'the unit is the whole window'". The argument, block 15's U2, covers only the unit clause, and the
rate clause has two properties it does not address (N5):
- The equal-rate clock law involves no chosen order, and it is not the joint law: its all-+x mass is `338229/7997080000`, against
  `59049/775835648`.
- Unequal rates move the clock law: one integer rate profile gives `4.1026e-5` against `4.2294e-5`.

Uniqueness therefore needs a reading of order-independence that covers rate-independence, and an argument for the rate case.

**Step 5 (level independent set): holds.**

**Step 6 (unrecorded sites): holds** as stated. A fully recorded window never consults the exterior.

## Verdict

The claim fails at (c). All the exact finite results hold. Step 3's seeded-clock numbers need the correction above.

`check.py` prints `SUMMARY: fails at (c) (step 4's conclusion) - ...` and no HIT line.
