# Referee: corrigendum PR 8149, attempt 2

Attempt `w-jonathonsmac4f50-j90fb`. Sequential and joint formation laws are recomputed here. The attempt's script is not imported.

The six-axis kernel is `K(b, a) = φ(a, b)/(p + q + 4r)`. For an order, `N_σ` is the product of the normalizers of the nonempty recorded sets. Block 15's old criterion says equality holds exactly when no site records an inside neighbour together with a second record.

## Verdicts

**Lagrange.** For an orthogonal pair and any positive weights `d_s`, the Gram minor equals `½ Σ d_s d_t (K_as K_ct − K_at K_cs)²`. The brackets at `(a, c)` and `(a, −a)` are `(p² − r²)/Z₁²` and `r(p − q)/Z₁²`. The minor is positive unless `p = q = r`.

**Executed cases.** On eight units, seven environments, every order, and the rules `(3,1,2)`, `(5,1,2)` and `(2,2,1)`, there are 2331 cases. The sequential law equals the joint law exactly when `N_σ` is constant. That happens exactly when no site records two inside neighbours and every dependent product `Φ_y` is constant. Every case with two inside neighbours differs. The old criterion implies equality in every environment, and it is necessary for the isolated and constant environments. Fourteen agreements, from the independent partial environments, violate the old only-if.

**Star.** The symmetry `g(x,y,z) = (−z, −x, −y)` acts on the values as the six-cycle `+x → −y → +z → −x → +y → −z`. It has three free orbits on the 18 outside sites, hence 216 equivariant environments. In all 216, and for eight non-constant rules, the centre-first dependent product is constant. In one such environment at `(3,1,2)`, the centre-first sequential law equals the joint law on all `6⁷` patterns. The leaves-first order does not.

## What stays open

The exhaustive product of five-record leaf factors was not rebuilt. The repair of the downstream notes was not edited.

## Result

HIT: confirmed. Sequential formation equals the joint law exactly when the normalizer product is constant. Two inside neighbours always separate. The centre-first star is a counterexample to the old only-if.
