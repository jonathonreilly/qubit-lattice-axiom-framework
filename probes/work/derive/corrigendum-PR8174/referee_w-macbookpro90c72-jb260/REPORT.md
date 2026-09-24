# Referee: corrigendum to PR8174, a1

Worker `w-macbookpro90c72-jb260` (`grok-4.6`). Author `w-macbookpro90c72-jc4c7` (`claude-opus-5`). The attempt's script is not imported.

## Verdict

Confirmed. Block 30's clause `d₁ ≤ max(d₂, d₃)` holds exactly on `p ≥ min(q, p*)`, and fails on a set of positive measure. Off that set the note's two-level coupling fails with positive probability. The minimal repair for that coupling is `ε₂ = max(d₁, d₂, d₃)`.

## What was checked

- **Closed forms.** Re-derived from the six-axis menu: `d₁ = (q³+4r³)/D₁`, `d₂ = (pq²+4r³)/D₂`, `d₃ = (rq²+r²(p+q)+2r³)/D₃`. All four choices of the orthogonal predecessor give the same `d₃`.
- **Signs.** `sign(d₂−d₁) = sign(p−q)` and `sign(d₃−d₁) = sign(g)`, with `g = r p² + (q²+qr+2r²)p − (q³+4r³)`. Each `dᵢ` is strictly decreasing in `p`.
- **Boundary.** `g(q) = 2r(q+2r)(q−r)` and `g(q−2r) = −4r²(q+r)`. So `q ≤ r` gives the naive half-line `p ≥ q`, while `q > r` puts `p*` strictly between `q−2r` and `q`.
- **Census.** At `(1,2,1)`, `d₁ = 12/13 > 9/10 = max(d₂, d₃)`. Exactly 127 of the 343 integer triples in `1..7` fail, and they are exactly `{p < q and g < 0}`.
- **Coupling.** The ten-site event has probability `24/(13⁸·1300)`. On it, `ξ = 1` and `η' = 0` at `(1,1,1)`. The three predecessor types `(a,a,a)`, `(a,a,−a)` and `(a,a,b)` are all reachable with one `η'` predecessor, so no smaller `ε₂` dominates this coupling.
- **Executed lines.** All 19 parameter lines named from PRs 8174–8177 have `p ≥ q` and `g > 0`, so `max(d₁,d₂,d₃) = max(d₂,d₃)`. Their numbers do not move.

Off the domain the repair sets `ε₂ = d₁`, and the two levels collapse.
