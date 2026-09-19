# Referee report: J:derive:chessboard-repair:a4

- **Author:** w-macbookpro90c72-j2ec5 (grok-4.6).
- **Referee:** w-jonathonsmac4f50-j966c (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` at git sha `06f7c4b8`, and its log
  `logs/probes/J:derive:chessboard-repair:a4/w-macbookpro90c72-j2ec5__06f7c4b8__20260919T003615Z.json`.
- **Disclosure:** this referee's model family also wrote attempt a1 of the same problem (worker w-jonathonsmac4f50-j877a,
  issue #8280). Nothing below relies on a1, and a4 does not use a1.

Every finite fact below is re-verified by `check.py` in this directory. It uses independent code and none of the author's
code.

## The problem and the claim

The task (`probes/TASKS.json`, `J:derive:chessboard-repair:a4`) asks for a correct chain repairing block 17's T3 (PR #8151),
with the best constant one can prove, and the threshold proved in 2D and in 3D.

The attempt claims three things:
- the site-reflection dissemination and the per-class bounds `μ(E_i^π)^{1/N} ≤ 6m/p` (2D) and `≤ 6(m/p)^{3/4}` (3D);
- a Cauchy–Schwarz combination over the `2^{d−1}` parity classes, said to recover block 17's intended event;
- the conclusion that T4 holds in 2D at `p ≥ 216m`, and that route (i) is a "3D no-go" that stays at `p ≥ 1296m`.

Its log line reads "PARTIAL - ... repairs T4 in 2D at 216m and is a no-go for 216m in 3D (stays 1296m)".

## Step by step

**Step 1 (orbit): holds.** A site reflection `θ_{j,k}` with `j ≠ i` preserves the parity of coordinate `j` of a
direction-`i` bond, and `θ_{i,k}` moves the bond along `i` only. R1 closes the orbit under all reflections on `(Z/4)²`,
`(Z/6)²`, `(Z/4)³` and `(Z/6)³`, from every starting parity. The orbit is exactly the direction-`i` bonds with the same
transverse parities, of size `N/2^{d−1}` (8, 18, 16 and 54 bonds). The author checked `(Z/4)²` only.

**Step 2 (line lemma): holds.** The argument is complete: a good bond of `s` facing a proper `a` forces a mismatch at one of
its two ends, and each position lies in two bonds. R2 verifies `bad(s) + 2 bad(s, a) ≥ n` over the actual six-letter
alphabet, for every proper cyclic `a` up to relabelling and every `s`. The cases are `n = 4` (4 cycles × 1296 sequences)
and `n = 6` (41 × 46656). The author used alphabets of 5 and 4.

**Step 3 (counting): holds.** The 2D argument is correct:
- even rows give `N/2` bad bonds;
- each odd row gives `bad_h + U + D ≥ 2L` against its two even neighbours;
- every vertical bond is counted once.

The 3D argument is the same, line by line. The two odd-parity line families have their neighbours in the `(even, even)`
class, whose lines are proper. The counted bond sets are disjoint.

The author's `check.py` evaluates only the sharp patterns, which bound the minimum from above; the lower bound itself was
not checked by machine. R3a checks it exactly. Over all patterns whose even rows have every horizontal bond bad, a min-plus
transfer over all `6⁴` row states gives a minimum number of bad bonds of 16, 24 and 32 on the 4×4, 4×6 and 4×8 tori,
which is `N` in each case. R3b recounts the sharp patterns (`N` in 2D, `3N/4` in 3D, sides 4 and 6) and confirms that they
lie in the class event. The 3D lower bound is not checkable exactly at side 4 (`6⁶⁴` patterns), so it rests on the
argument, which is correct.

**Step 4 (mass bound): holds.** With `m ≤ p` a pattern with `b ≥ b₀` bad bonds weighs at most `m^{b₀} p^{dN−b₀}`. There
are at most `6^N` patterns, and `Z ≥ 6p^{dN}` (the constant patterns). On the 4×4 torus, a float transfer matrix
(R4, INFO) gives `μ(class)^{1/N}` = 0.0079, 0.0150, 0.110, 0.180 at four points. The bound `6^{15/16} m/p` gives 0.0248,
0.0497, 0.358, 0.536 there. The bound holds and is loose by a factor of about 3.2.

**Step 5 (Cauchy–Schwarz over classes): the inequality holds, but it plays no part in the argument.**
`μ(∩_α A_α) ≤ (Π_α μ(A_α))^{1/k} ≤ max_α μ(A_α)` is correct.
- Under site reflections, the chessboard estimate's factor for the cell event "the canonical direction-`i` bond is bad" is
  the mass of that event's dissemination. By step 1 that is one class `E_i^π`, and step 4 bounds exactly that.
- The intersection over classes ("every direction-`i` bond is bad", the event block 17 named) is a smaller event. R4 finds
  its mass below the class's at every tested point. No step of block 17's chain uses it, and a bound on it does not bound
  the class event.

So "CS recovers the intended event ... Therefore T4's `ε = 6m/p` is valid in 2D" reaches a correct conclusion by the wrong
route. The 2D repair is step 4 applied to the class event. Steps 1–4 carry the whole result.

**Step 6 (3D no-go): does not follow.** The step, marked PROVED, asserts:
- "CS cannot improve the exponent 3/4";
- "no further dissemination is available on this route";
- in the statement and in (4), that route (i) "does not recover the 3D constant 216" and "is complete as ... a 3D no-go".

What the argument shows:
- Cauchy–Schwarz never beats its worst factor (true and trivial);
- site reflections preserve transverse parity (step 1).

What a no-go needs: a lower bound on `μ(E_i^π)`, or on anything that site reflections can disseminate, that exceeds
`(1/36)^N` at `p < 1296m`. No such bound is given.

The sharp exponent `3/4` does not supply one. `(1/216)^{3/4} = 0.0178 < 1/36 = 0.0278` (R5, exactly
`36⁴ = 1679616 < 216³ = 10077696`). So at `p = 216m` the minimal patterns alone are compatible with `ε ≤ 1/36`. What
excludes `216m` in the attempt's bound is the factor `6` from counting all `6^N` patterns (step 4). The attempt does not
show that factor is necessary, and its 2D analogue is loose by about 3.2 on the 4×4 torus (R4).

The proved statement is therefore: site reflections with step 4's count give `p ≥ 1296m` in 3D. Whether site reflections
alone can reach `216m` in 3D is still open. This is the classic failure of reading a no-go off an upper bound.

## Classic failure modes

- *Quantifier or direction.* Step 6 infers "cannot do better" from an upper bound. That is the failing step.
- *Bound only at checked sizes.* No: steps 2–3 are proved for all sizes, and the checks are consistent with the proofs.
- *Outside theorem beyond its hypotheses.* Cauchy–Schwarz and Hölder (step 5) are used correctly, but on an event the
  chain does not need.
- *Circularity.* None.

## Verdict

- **First failing step: 6.** The 3D no-go is not proved.
- **Steps 1–4 hold** and give the thresholds `p ≥ 216m` in 2D (block 17's T4 as stated) and `p ≥ 1296m` in 3D. They were
  re-verified independently: orbits in 2D and 3D, the lemma over six letters, the 2D minimum `= N` by exact min-plus
  transfer, and the sharp patterns.
- **Step 5 is correct as an inequality** but plays no part in the chain.

`check.py` prints `SUMMARY: fails at step 6 - ...`. It prints no `HIT: confirmed` line, because the claim as logged includes
the no-go.
