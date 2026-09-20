# Independent local field and occupancy generator check

Completed independent derivation and exact checks, 2026-09-20, after sealing
the finite-rate bound in `BOUND_SEAL.json`. No new primary calculations or
draft sources have been read. The local generator, Fourier eigenvalue and
all-density uniform-weight occupancy equation below are confirmed within
their stated scopes. This supplies no audit/retention or physical verdict.

The menu is `v_a in {+e1,-e1,+e2,-e2,+e3,-e3}`. Set
`W(a,b)=1+j v_a dot v_b`, `|j|<1`, and empty bonds to one. Edges propose
vacancy hops at rate one, accepted with `w_new/(w_old+w_new)`. Every
vacant-site content channel has birth rate epsilon times its local weight.
Write `n_x=1_(x occupied)`, `m_i(x)=v_i(s_x)` when occupied and zero otherwise,
and let A be adjacency and `Delta=A-diag(degree)`.

**Pointwise local result.** Interpret the distance-two neighborhood as the
closed ball `B_2(x)={y:dist(x,y)<=2}`. On each configuration containing at
most one occupied site in this ball, with no restriction outside it,

```
(G m_i(x))(s) = (1/2) Delta m_i(x) + 2 epsilon j A m_i(x).
```

Indeed, an occupied x has only empty neighbors and every possible destination
neighbor also has no other occupied neighbor. Its hops all have old and new
weights one and remove `m_i(x)` at rate 1/2 per edge. If x is empty with
one occupied neighbor y, its incoming hop likewise has rate 1/2. A record
only at distance two gives no hop contribution at x.

At a vacant x, no occupied neighbor gives zero birth drift by menu symmetry.
With one occupied neighbor of content v, the drift is

```
epsilon sum_a v_(a,i) [1+j v_a dot v]
 = 2 epsilon j v_i,
```

because `sum_a v_a=0` and `sum_a v_a v_a^T=2 I_3`. At occupied x birth is
forbidden, and all neighboring fields vanish under the local condition.
This proves the stated formula in every allowed case. The factor 2 comes
from the unnormalized per-content birth rates: their total with one neighbor
is `6 epsilon`, while the normalized mean new content is `j v/3`.

**Spatial linear operator.** On a d-dimensional nearest-neighbor torus with
unit spacing and side lengths at least three, so that the `2d` neighbors are
distinct, the corresponding linear operator is

```
L_local = (1/2) Delta + 2 epsilon j A
        = (1/2+2 epsilon j) Delta + 4d epsilon j I.
```

For Fourier mode `exp(i k dot x)`, with `k_r=2 pi ell_r/L_r`, its eigenvalue is

```
lambda_local(k) = sum_(r=1)^d (cos(k_r)-1)
                  + 4 epsilon j sum_(r=1)^d cos(k_r)
                = (1+4 epsilon j) sum_(r=1)^d cos(k_r)-d.
```

The Fourier statement concerns this linear spatial operator. Equality to
the stochastic generator was proved only on the stated local configurations.
Births need not preserve that set of configurations. Therefore neither this
identity nor its Fourier diagonalization closes the finite-density mean
field evolution or supplies a physical field identification.

**Exact occupancy equation at W=1.** With no sparsity restriction, vacancy
hops occur at rate 1/2 and

```
G n_x = (1/2) sum_(y~x)[(1-n_x)n_y-n_x(1-n_y)]
        + 6 epsilon(1-n_x)
      = (1/2) Delta n_x + 6 epsilon(1-n_x).
```

For `h_x=1-n_x`, this is `G h_x=(1/2)Delta h_x-6 epsilon h_x`.
Hence, on the finite graph, the first moments satisfy exactly

```
partial_t E n_x = (1/2) Delta E n_x + 6 epsilon(1-E n_x),
partial_t E h_x = (1/2) Delta E h_x - 6 epsilon E h_x.
```

Starting from the empty configuration gives `E n_x(t)=1-exp(-6 epsilon t)`
at every site, on any such finite graph. This statement concerns first
moments only; no independence of site occupancies is needed or inferred.

## Checks and scope counterexamples

`field_check.py` computes hop rates using complete configuration weights,
then evaluates generator increments directly. On a five-site path it
exhausted every configuration satisfying the radius-two condition at each
chosen site, with arbitrary contents outside that ball, for
`j=-1/2, 0, 1/3, 3/4`. All 8972 configuration/site/j cases agree in all
three field components. Motion and the coefficient of epsilon were compared
separately, so these checks do not select a particular epsilon.

The unrestricted W=1 occupancy identity was checked for all 32 occupied-site
subsets on the five-site path and all five observation sites: 160 cases,
including blocked occupied-occupied bonds. All 84 Fourier modes on side-four
tori in dimensions 1, 2 and 3 satisfy the adjacency/graph-Laplacian symbols.
The latter checks use exact small Gaussian integers (the roots 1, i, -1,
and -i); the displayed formula for arbitrary d follows analytically from
the two translated neighbors in every coordinate direction.

Two explicitly computed counterexamples prevent extending the local field
claim beyond its hypotheses:

* On the graph consisting of one edge, put `+e1` and `-e1` at its two ends
  and take j=0. No hop or birth is allowed. Thus the actual generator of
  the first component at the first site is zero, while `(1/2)Delta m_1`
  gives -1. The local sparsity condition is violated.
* On the three-site path `x-y-z`, take x empty, y and z both `+e1`, and
  j=1/2. The radius-one ball around x has only one record, but the
  radius-two ball has two. The incoming hop loses a bond of weight 3/2,
  giving acceptance `1/(1+3/2)=2/5`, whereas the proposed local linear term
  would use 1/2. The actual birth drift at x is epsilon in both expressions.
  Hence a radius-one hypothesis is insufficient.

These are exact generator counterexamples, not observations of a simulation
at low or high density. They preserve the claimed radius-two statement and
the separate all-density occupancy equation at W=1.

## Reproduction and source identities

Run from `/Users/jonreilly/Documents/Codex/mobile-record-formation-20260920`:

```bash
python3 .claude/science/mobile-record-formation-20260920/independent/finite_rate_bridge/field_check.py > .claude/science/mobile-record-formation-20260920/independent/finite_rate_bridge/FIELD_RUN.log 2>&1
```

The run exited 0. Exact counts, counterexamples and input parameters are in
`FIELD_RESULTS.json`; the complete log is `FIELD_RUN.log`. The executed
`field_check.py` SHA-256 is
`51739fed48016607c611cffd62db8511135269c93b27491b5457db49fd75831b`.

The source context is the task's explicitly supplied model and the unchanged
instruction/source identities in `MANIFEST.json`: HEAD
`22e6df1c55c99434410b37d936991c7227bf591c`, planning revision
`068e916ca37b004757ad3a3c082857a91dc37215`, and workflow SHA-256
`d74718214335d4feae4b40d75720482ca93bd1560a3c35174e7bf875b5b59cc4`.
The mathematical definitions and test matrices are written locally in this
report and runner. No new primary source, external reference or imported
numerical constant was used. The prior finite-rate bound seal remains
unchanged. `FIELD_SEAL.json` pins these field-moment artifacts separately.
