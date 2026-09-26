# Referee: causal-clauses a2

Attempt `w-jonathonsmac4f50-j8f9d`. Formation sequences are recomputed here. The attempt's script is not imported.

The kernel is the six-axis product. A parent value contributes weight `p`, `q` or `r` according as the child is equal, opposite or orthogonal, and the one-parent normalizer is `p + q + 4r`. An empty parent set draws uniformly from the six values. The causal law of a window is the product of these one-site kernels on the parent sets.

## Verdicts

**Parent-first orders.** On the bent chain, the straight chain, the V, the Λ, the diamond and the three-parent claw, every linear extension equals the causal product, at both `(3,1,2)` and `(5,1,2)`.

**Causal clocks.** Rates that vanish off formable sites reproduce the same product on the four three-site windows.

**Pair gap.** At `(3,1,2)`, `144 K_2` is `26`, `24` or `22` for equal, orthogonal and opposite pairs. The two-parent marginal `K_2/6` differs from the free law `1/36` by total variation `1/72`.

**Three-site distances from the causal law, at `(3,1,2)`.**

| law | V | bent chain and Λ |
|---|---|---|
| static | `1/72` | `0` |
| uniform clocks | `1/108` | `1/216` |
| seeded clock | `1/72` | `0` |
| attracting clock | `7/648` | `1/324` |
| parallel growth | `37/3888` | `17/3888` |

**Domino.** On the V, drawing one parent freely and then forming the other parent jointly with the child is exactly the static law, at distance `1/72` from the causal law.

**Two sites.** A single bond does not separate any of these candidates from the causal law.

**Marginals.** On every down-closed subset of the six windows, the causal marginal equals that subset's own causal law.

**Diamond.** The four-site plaquette has total variations `455/31176` (static), `53347/4416984` (uniform), `691/61776` (seeded), `129427/11042460` (attracting) and `12853/1070784` (parallel growth).

## What stays open

The sample of 60 random value-dependent policies was not repeated. The identity for an arbitrary causal policy is the probability-tree sum used above; it was checked on these windows, not quantified over every rate table.

## Result

HIT: confirmed. On a causal window, parent-first clocks finish in the product of the kernels given the parents. The recorded noncausal candidates first differ from that product on a three-site window, by the total variations above.
