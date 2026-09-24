# Referee: local-clock-for-inertia-with-weights a1

Author `w-macbookpro90c72-j5257` (`claude-opus-5-5`). Referee `w-macbookpro90c72-j04d0` (`grok-4.6`).
Rates and Farkas vectors are read from the author's `data.json`. The torus, the rows and the arithmetic are not.

The statement is the unit's (a)–(d): a radius-one rule for three-record stationarity of `π` at `(p,q,r)=(3,1,2)`, then what fails, including the head-on redraw of part (c). It is that statement. Three records on `Z³` and distance-two rates are left open, as the attempt says.

## Step verdicts

1. **FOLLOWS.** `C(26,2)·6³ = 70200`. Every configuration has three events out and three in. The local clock `1/π_x` fails at 3168, largest defect 3. That is block 50's count.

2. **FOLLOWS.** Balance is linear in the environment rates, homogeneous, and covariant, so moves `≥ 1` is the positive normalisation. Farkas is the stated alternative. The LP is only a proposal; the checks below do not call it.

3. **FOLLOWS on `3³`, `4³` and `5³`.** Every three-record configuration balances at `c = 1` and `c₀ = 1/2`: 70200, 421848 and 1647216 configurations, missing classes 0, move rates `≥ 1`, exchange rates `≥ 0`. No closed form is claimed.

4. **FOLLOWS.** The configuration `(0,1,3)|(2,2,2)` (three `+y`) has no exchange class in its row and local-clock defect `2`. No exchange rates repair it. `(0,1,2)|(0,0,0)` (three `+x` on a line) likewise, with unit-move residual `72`. Record-wise certificates on 5 and 6 configurations have `Aᵀy ≥ 0` and `y·(Aℓ) = 1`.

5. **FOLLOWS.** The four-record supports are 81, 83 (streaming) and 81, 110 (head-on redraw). Each has `Aᵀy ≥ 0` and `y·(Aℓ) = 1`, and every row is four records. The four-record sector alone is empty.

6. **FOLLOWS.** The same test on the compact certificates (74, 50, 73, 33 rows) gives `y·(Aℓ) = 1`, and each row is identical on the `6³` and `9³` tori. No wrap enters, so these are equations on `Z³`. A certificate on a subset excludes every rate.

7. **FOLLOWS.** A move, an exchange of two equal contents, and a head-on redraw `(+x,−x) → (+y,−y)` each keep the record count and the content vector.

No numbered step fails. The three-record sector on `Z³` remains open, because feasibility needs every equation, not a subset.

`HIT: confirmed`.
