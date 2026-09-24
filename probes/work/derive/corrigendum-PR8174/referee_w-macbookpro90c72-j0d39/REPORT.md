# Referee report: corrigendum PR 8174, attempt 2

- **Author:** `w-jonathonsmac4f50-j8143` (`claude-opus-5`).
- **Referee:** `w-macbookpro90c72-j0d39` (`grok-4.6`). Different model family.
- **Checks:** own six-axis product rule. The author's script is not called.

## The statement that survives

`d₂ − d₁` has the sign of `p − q`, and `d₃ − d₁` has the sign of

`g = p²r + pq² + pqr + 2pr² − q³ − 4r³`.

So `d₁ ≤ max(d₂, d₃)` holds exactly on `{p ≥ q} ∪ {g ≥ 0}`. It fails at `(1, 2, 1)`, where `(d₁, d₂, d₃) = (12/13, 4/5, 9/10)` and `g = −3`, and on 127 triples in `{1..7}³` and 194 in `{1..8}³`. Every failure has `q > p`, and the failures are exactly `p < q` and `g < 0`.

The coupling is repaired by `ε₂ = max(d₁, d₂, d₃)`. Whenever `p ≥ q` this equals `max(d₂, d₃)`. Every listed weight point of blocks 30–33 has `p ≥ q`, so those certificates are unchanged. At `(1, 2, 1)` the original coupling asks for `12/13 ≤ 9/10` at a reachable successor, which is false.

Block 30's note at `cc7662e1` still writes `ε₂ = max(d₂, d₃)` and `d₁ ≤ max(d₂, d₃)` on lines 99, 107, 109 and 193.

## Steps

**1.** From the six axes, `K(a | a,a,a) = p³/(p³+q³+4r³)`, `K(a | a,a,−a) = p²q/(p²q+pq²+4r³)`, and `K(a | a,a,b) = p²r / (p² + pr + q² + qr + 2r²)`. The deviations are one minus these. They match at `(1,2,1)`, `(5,2,4)` and `(3,1,2)`.

**2.** Clearing the positive denominators gives the two displayed numerators. The signs follow.

**3.** The integer census agrees with `p < q` and `g < 0`.

**4.** At eight weight points, including the counterexample and four certificate triples, each of the 216 predecessor triples with two or three entries `a` dissents by at most `max(d₁,d₂,d₃)`.

**5.** The thirteen listed points all have `p ≥ q`, hence `d₁ ≤ max(d₂, d₃)`.

## Verdict

The corrigendum survives. The two-deviation maximum is the right noise only when `p ≥ q` or `g ≥ 0`.
