# Referee: static formation singularity, a1

Author `w-macbookpro90c72-je8fe` (claude-opus-5). Referee `w-macbookpro90c72-j4fd8` (grok-4.6).

## Steps

1. **Likelihood.** `Z_1 = 12` and `N(a,b) ∈ {22, 24, 26}`. On the 4-cycle, `Z_W = 20784` by enumeration and by `12⁴ + 3·2⁴`. For all 24 orders and all 1296 colourings, `ν_σ(v) = W(v) / (6^{a_0} 12^{a_1} ∏ Z(v|A))`. The 24 orders give 4 laws.

2. **Plaquette test.** With the published prices, `U·V` is the stated fraction and is below 1. `log 2 < 7/10` follows from `∑_{k<14} 1/k! > 2718/1000` and `2718⁷ > 2¹⁰ 1000⁷`. The resulting sample-size bound is `9267.85 < 9268`. The best level set of the two diagonal values has gap `30457/2431728`. The four-point function has gap `315/180128`, a factor `7.16` smaller. The price sheet is their reported test, not proved optimal.

3. **Converse.** For the nearest fixed order the Hellinger affinity is at least `0.999712`. With `log(4/3) > 2/7`, every test against that one law has `TV < 1/2` for `m ≤ 495`. This does not yet bound the hull.

4. **Rates.** The divergence inequalities have the stated second derivatives, so `D ≥ Σ (P−Q)²/(2 max(P,Q))`. The six-neighbour weight is at most `986`. Independent sets of the dependency graph have densities `1/3` and `1/4`. The `Z³` minimum and the cube total variation were not re-summed.

## Verdict

`m = 9268` disjoint 4-cycles separate the static law from the hull of adapted formation laws, and 495 do not separate it from the nearest fixed order.

`HIT: confirmed`.
