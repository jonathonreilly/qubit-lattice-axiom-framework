# Referee report: J:derive:chessboard-repair:a3

- **Author:** w-macbookpro90c72-j6ef3 (grok-4.6).
- **Referee:** w-jonathonsmac4f50-j8343 (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` at sha `98d04c92`, and its log.

**Disclosure.** This referee's model family wrote attempt a1 of the same problem, which uses bond-plane reflection positivity
with a mixed chessboard. a3 states that it is independent of a1. `check.py` here is written afresh: sympy for the spectrum,
and its own closure code for the orbits.

## The claim

The attempt claims three things:
- The bond weight `W` has eigenvalues `p + q + 4r` (once), `p − q` (three times) and `p + q − 2r` (twice). It is PSD iff
  `p ≥ q` and `p + q ≥ 2r`, which on `(p, 1, 2)` means `p ≥ 3`.
- Bond-plane reflections alone send a direction-`i` bond to an orbit of `N/2`, not `N`. Site reflections along the bond
  combined with bond reflections across it give `N`.
- Route (ii) with bond planes alone does not repair T3. The mixed group "would need site-plane RP … not claimed here".

## Step by step

**Step 1 (spectrum): holds.**
- The eigenvalues are as stated, and PSD holds exactly when `p ≥ q` and `p + q ≥ 2r` (C1).
- The witnesses match:

  | weights | eigenvalues | PSD |
  |---|---|---|
  | `(3,1,2)` | `{0, 2, 12}` | yes |
  | `(5,2,4)` | `{−1, 3, 23}` | no |
  | `(1,3,2)` | `{−2, 0, 12}` | no |
  | `(4,1,2)` | `{1, 3, 13}` | yes |

- This is block 17's T1, the lead the task asked to verify.

**Steps 2–3 (orbits): hold.** C2 closes orbits under all reflections on `(Z/4)²`, `(Z/6)²`, `(Z/4)³` and `(Z/6)³`:
- bond planes alone give `N/2`, exactly the direction-0 bonds with even longitudinal start;
- site planes alone give `N/2^{d−1}`;
- site planes in the bond direction with bond planes in the others give `N`.

**Step 4 (consequence): holds as stated, but the obstruction it names is already resolved.**
- Bond-plane RP alone disseminates to the wrong event.
- The mixed group needs site-plane RP. The attempt leaves this open, and section (4) asks for "a proof of site-plane RP on
  the same (p,q,r) region".
- That is block 17's T2, "reflection positivity through site planes, any weights" (C3 reads it from the note on the PR
  branch).
- So with `W` PSD the mixed chessboard disseminates to all `N` direction-`i` bonds, as the attempt's own Step 2 describes.
  That is the repair route of attempt a1.

## Classic failure modes

None in the claims. The "what would finish it" remark asks for a result that already exists (block 17 T2).

## Verdict

The partial result survives with no failing step. The stated obstruction to finishing the repair is already resolved by
block 17's T2.

`check.py` prints `HIT: confirmed - ...` and its SUMMARY line.
