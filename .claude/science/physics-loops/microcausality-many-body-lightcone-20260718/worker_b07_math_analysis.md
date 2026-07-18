# Worker B (math build): weighted-norm quasilocal-class walk expansion — full inequality chain

Provenance: this analysis file is the deliverable of the Worker-B math seat
(Opus 4.8, max reasoning effort; owner-directed, supervisor responsible). It
executes the summation/counting layer requested by
`worker_b07_math_spec.md`. The Duhamel / norm-transport machinery (Jacobi,
boundary reduction, self-drop, `||f(t)|| <= ||f(0)|| + int ||R||`, iterated
integrals `t^k/k!`, and the resulting unrolled series shape used in Section 4)
is TAKEN AS GIVEN from the sibling note; only the counting layer on top is
derived here. Every load-bearing constant is exact rational / closed form;
floats are advisory only.

## Notation and standing hypotheses

- `Lambda` finite subset of `Z^3`, nearest-neighbor graph, ambient graph
  distance `d(.,.)` (= l^1 / Manhattan distance for the standard cubic graph).
- Each interaction set `S` is finite and CONNECTED; `diam(S) := max_{u,v in S} d(u,v)`
  is the ambient graph diameter. Key consequence used repeatedly:
  for all `u,v in S`,  `d(u,v) <= diam(S)`.   (D)
- `h_S = h_S^*` Hermitian, `H = sum_S h_S`.
- Observables: `A` supported on `X`, `B` supported on `Y`,
  `d := d(X,Y) = min_{x in X, y in Y} d(x,y) >= 1`.
- Heisenberg flow `tau_t(A) = e^{iHt} A e^{-iHt}` (sign convention immaterial
  to norms).
- Supplied weighted activity, for a supplied `mu > 0`:
  `kappa := sup_x sum_{S: x in S} ||h_S|| * |S| * e^{mu * diam(S)} < infinity`.  (K)

Two per-set weights (used to keep the bookkeeping honest):
- plain weight        `w(S)  := ||h_S|| e^{mu diam(S)}`,
- site-weighted       `w*(S) := ||h_S|| |S| e^{mu diam(S)} = |S| * w(S)`.
Since `|S| >= 1`,  `w(S) <= w*(S)`.   (W)
With this notation (K) reads:  `sup_x sum_{S ni x} w*(S) <= kappa`, i.e.
  for every site `x`:   `sum_{S: x in S} w*(S) <= kappa`.   (K')

A "chain of length k" is an ordered tuple `(S_1,...,S_k)` of interaction sets with
- `S_1 cap X != {}`            (anchored at X),
- `S_{j+1} cap S_j != {}`      (consecutive overlap), for `1 <= j <= k-1`,
- `S_k cap Y != {}`            (anchored at Y).
These are exactly the sets that survive the Duhamel expansion of `[tau_t(A),B]`
(boundary reduction pins `S_1 cap X != {}`; nested commutators force
consecutive overlap; the base commutator `[h_{S_k},B]` vanishes unless
`S_k cap Y != {}`).

---

## Section 1 — CHAIN LEMMA

Claim. For any chain `(S_1,...,S_k)` (constraints above), every site of `S_j`
lies within ambient distance `D_j := sum_{i=1}^{j} diam(S_i)` of `X`; hence
  sum_{j=1}^{k} diam(S_j) >= d.

Proof of the reach claim by induction on `j`.

Base `j = 1`. Since `S_1 cap X != {}`, fix `a in S_1 cap X`. For any `z in S_1`,
`a,z in S_1` so by (D) `d(z,a) <= diam(S_1)`. As `a in X`,
  d(z,X) = min_{x in X} d(z,x) <= d(z,a) <= diam(S_1) = D_1.

Step `j -> j+1`. Assume every site of `S_j` is within `D_j` of `X`. Since
`S_{j+1} cap S_j != {}`, fix `c in S_{j+1} cap S_j`. Because `c in S_j`, the
hypothesis gives `d(c,X) <= D_j`. For any `z in S_{j+1}`, both `z,c in S_{j+1}`
so by (D) `d(z,c) <= diam(S_{j+1})`. Triangle inequality of the ambient metric:
  d(z,X) <= d(z,c) + d(c,X) <= diam(S_{j+1}) + D_j = D_{j+1}.
This closes the induction.

Conclusion. Since `S_k cap Y != {}`, fix `b in S_k cap Y`. Applying the reach
claim at `j = k` to the site `b in S_k`:
  d(b,X) <= D_k = sum_{j=1}^{k} diam(S_j).
But `b in Y`, so `d(b,X) = min_{x in X} d(x,b) >= min_{x in X, y in Y} d(x,y) = d(X,Y) = d`.
Chaining the two displays:
  sum_{j=1}^{k} diam(S_j) >= d(b,X) >= d.            (CL)
QED. (Only used: connectedness via (D), triangle inequality, and the anchoring
of the two endpoints. No use of `mu`, norms, or `|S|` here.)

---

## Section 2 — WEIGHT SPLIT

Claim (per chain). For any chain `(S_1,...,S_k)`,
  Prod_{j=1}^{k} ||h_{S_j}||  <=  e^{-mu d} * Prod_{j=1}^{k} ( ||h_{S_j}|| e^{mu diam(S_j)} ).

Proof. Factor the exponentials out of the right-hand product:
  Prod_{j} ( ||h_{S_j}|| e^{mu diam(S_j)} )
    = ( Prod_{j} ||h_{S_j}|| ) * e^{ mu * sum_{j} diam(S_j) }.
By (CL), `sum_j diam(S_j) >= d`, and `mu > 0`, so the scalar exponential obeys
  e^{ mu * sum_j diam(S_j) }  >=  e^{ mu d }  >  0.
Since `Prod_j ||h_{S_j}|| >= 0`, multiplying the inequality by it preserves it:
  Prod_{j} ( ||h_{S_j}|| e^{mu diam(S_j)} )  >=  ( Prod_{j} ||h_{S_j}|| ) * e^{mu d}.
Divide by `e^{mu d} > 0` and rearrange:
  Prod_{j} ||h_{S_j}||  <=  e^{-mu d} * Prod_{j} ( ||h_{S_j}|| e^{mu diam(S_j)} )
                        =  e^{-mu d} * Prod_{j} w(S_j).            (WS)
QED. The `e^{-mu d}` gain is precisely the exponential "cost" of crossing the
gap `d`, paid for once against the accumulated diameters.

## Section 3 — STEPWISE FACTORIZATION (the |S|-weight bookkeeping)

Goal. Bound the fully weighted chain sum
  Sigma_k := sum over chains (S_1,...,S_k) of  Prod_{j=1}^{k} w(S_j),
    w(S) = ||h_S|| e^{mu diam(S)},
where the sum ranges over all chains satisfying the three constraints.

### 3.0 The single-step meeting bound (this is the crux)

For a FIXED set `S_j`, sum the site-weighted `w*` over all sets meeting it:
  sum_{S': S' cap S_j != {}} w*(S').
"`S' cap S_j != {}`" means there is a contact site `x in S_j` with `x in S'`,
hence
  { S' : S' cap S_j != {} }  =  Union_{x in S_j} { S' : x in S' }.
Bounding a union-indexed sum of nonnegative terms by the sum over the index
(a set meeting `S_j` in two or more sites is counted once per contact site, so
this is `<=`, with equality iff every contributing `S'` meets `S_j` in exactly
one site):
  sum_{S': S' cap S_j != {}} w*(S')
    <= sum_{x in S_j} sum_{S' ni x} w*(S')      [union over contact sites]
    <= sum_{x in S_j} kappa                      [by (K'), once per x]
    =  |S_j| * kappa.                                                    (STAR)

So:  sum_{S' cap S_j != {}} ||h_{S'}|| |S'| e^{mu diam(S')}  <=  |S_j| * kappa.
Read this carefully: the |S'| weight INSIDE kappa is what let (K') absorb the
`|S_j|` distinct choices of contact site — but the output STILL carries a `|S_j|`
factor and each summed set `S'` STILL carries its own `|S'|` (inside w*). That
surviving `|S'|` is exactly the fuel for the NEXT step. We now track this
through an iterated (back-to-front) peeling so no `|S|` is ever created or
destroyed spuriously.

### 3.1 Back-to-front peeling — exact tail recursion

Write `Sigma_k` as an iterated sum (outer index first):
  Sigma_k = sum_{S_1 cap X != {}} w(S_1) [ sum_{S_2 cap S_1 != {}} w(S_2) [ ...
              [ sum_{S_k cap S_{k-1} != {}, S_k cap Y != {}} w(S_k) ] ... ] ].

Define the innermost tail and, recursively, the deeper tails:
  U_k(S_{k-1}) := sum_{ S_k cap S_{k-1} != {},  S_k cap Y != {} }  w(S_k),
  U_j(S_{j-1}) := sum_{ S_j cap S_{j-1} != {} }  w(S_j) * U_{j+1}(S_j),   (2 <= j <= k-1).

Claim:  U_j(S_{j-1})  <=  |S_{j-1}| * kappa^{(k-j+1)}   for all  2 <= j <= k.   (T)

Base case j = k. Drop the `S_k cap Y` constraint (nonneg terms), then use (W)
`w <= w*`, then (STAR):
  U_k(S_{k-1})
    = sum_{ S_k cap S_{k-1} != {}, S_k cap Y != {} } w(S_k)
    <= sum_{ S_k cap S_{k-1} != {} } w(S_k)          [drop Y-constraint, terms >= 0]
    <= sum_{ S_k cap S_{k-1} != {} } w*(S_k)          [by (W), since |S_k| >= 1]
    <= |S_{k-1}| * kappa.                              [by (STAR)]
So (T) holds at j = k with exponent `k-k+1 = 1`. The `|S_{k-1}|` was PRODUCED by
(STAR); it did not exist in `w(S_k)`.

Inductive step (downward), assume (T) at `j+1`:
  U_{j+1}(S_j) <= |S_j| * kappa^{(k-j)}.
Then
  U_j(S_{j-1})
    = sum_{ S_j cap S_{j-1} != {} } w(S_j) * U_{j+1}(S_j)
    <= sum_{ S_j cap S_{j-1} != {} } w(S_j) * |S_j| * kappa^{(k-j)}   [induction hyp]
    =  kappa^{(k-j)} * sum_{ S_j cap S_{j-1} != {} } |S_j| w(S_j)
    =  kappa^{(k-j)} * sum_{ S_j cap S_{j-1} != {} } w*(S_j)          [|S_j| w = w*]
    <= kappa^{(k-j)} * ( |S_{j-1}| * kappa )                          [by (STAR)]
    =  |S_{j-1}| * kappa^{(k-j+1)}.
This is (T) at `j`. KEY OBSERVATION realized here: the factor `|S_j|` handed up
by `U_{j+1}` combined EXACTLY with `w(S_j)` to reconstitute `w*(S_j) = |S_j| w(S_j)`,
which is the precise object (STAR) knows how to sum. The `|S_j|` is consumed at
this step and replaced by a fresh `|S_{j-1}|` for the step below. No `|S|` weight
is ever left over or invented. This is the bookkeeping the spec flagged.

### 3.2 Outermost sum and the start factor

Apply (T) at `j = 2` (i.e. `U_2(S_1) <= |S_1| kappa^{k-1}`) and sum over `S_1`:
  Sigma_k = sum_{ S_1 cap X != {} } w(S_1) * U_2(S_1)
    <= sum_{ S_1 cap X != {} } w(S_1) * |S_1| * kappa^{k-1}          [by (T), j=2]
    =  kappa^{k-1} * sum_{ S_1 cap X != {} } w*(S_1).               [|S_1| w = w*]
Define the START FACTOR
  n_X^w := sum_{ S: S cap X != {} } ||h_S|| |S| e^{mu diam(S)}  =  sum_{S cap X != {}} w*(S).
By the same union-over-sites bound as (STAR), now over `X`:
  n_X^w = sum_{S cap X != {}} w*(S)
    <= sum_{x in X} sum_{S ni x} w*(S)                              [union over x in X]
    <= sum_{x in X} kappa  =  |X| * kappa.                          [by (K')]
Therefore
  Sigma_k  <=  n_X^w * kappa^{k-1}  <=  |X| * kappa^{k}.            (3)

Edge case k = 1. A length-1 chain is a single `S_1` with `S_1 cap X != {}` and
`S_1 cap Y != {}`. Then
  Sigma_1 = sum_{S_1 cap X != {}, S_1 cap Y != {}} w(S_1)
    <= sum_{S_1 cap X != {}} w(S_1) <= sum_{S_1 cap X != {}} w*(S_1) = n_X^w,
matching (3) at `k = 1` (`kappa^0 = 1`). Consistent.

### 3.3 Combine with the weight split — the plain-norm chain sum

Summing the per-chain inequality (WS) over all chains of length `k` (every such
chain satisfies the three constraints, so (WS) applies term by term):
  sum over chains of  Prod_{j} ||h_{S_j}||
    <= e^{-mu d} * sum over chains of Prod_{j} w(S_j)
    =  e^{-mu d} * Sigma_k
    <= e^{-mu d} * n_X^w * kappa^{k-1}
    <= e^{-mu d} * |X| * kappa^{k}.                                 (3')
This is the object the Duhamel series consumes in Section 4.

## Section 4 — ASSEMBLY (2-powers bookkeeping made exact)

### 4.1 The supplied unrolled series (sibling, taken as given)

  ||[tau_t(A),B]||  <=  ||[A,B]||
      + 2||A|| * sum_{k>=1} 2^{k-1} * Xi_k * |t|^k / k! ,
where the order-k "chain sum with base" is
  Xi_k := sum over chains (S_1,...,S_k) of  ||h_{S_1}|| ... ||h_{S_{k-1}}|| * ||[h_{S_k}, B]||,
and the base commutator obeys `||[h_{S_k}, B]|| <= 2 ||h_{S_k}|| ||B||`.
Structure of the 2's, as delivered: prefactor `2||A||` (one 2 from the outer
`[.,A]` commutator), then each of the `k-1` interior Duhamel iterates contributes
a factor 2 via `||[h_{S_j}, .]|| <= 2||h_{S_j}|| ||.||` (that is the `2^{k-1}`),
and the base contributes one more 2 via `||[h_{S_k},B]|| <= 2||h_{S_k}|| ||B||`.

### 4.2 Insert the base bound

  Xi_k <= 2 ||B|| * sum over chains of Prod_{j=1}^{k} ||h_{S_j}||.
Hence
  ||[tau_t(A),B]||
    <= ||[A,B]|| + 2||A|| sum_{k>=1} 2^{k-1} ( 2||B|| sum_chains Prod_j ||h_{S_j}|| ) |t|^k/k!.

### 4.3 Total power of two (cross-check by direct count)

Collect the explicit 2's at order k:
  (prefactor) 2  *  (interior) 2^{k-1}  *  (base) 2  =  2^{1 + (k-1) + 1} = 2^{k+1}.
Scalar amplitudes: `||A||` (prefactor) and `||B||` (base). So the order-k term is
  2^{k+1} ||A|| ||B|| ( sum_chains Prod_j ||h_{S_j}|| ) |t|^k / k!.

### 4.4 Insert the counting bound (3')

Using `sum_chains Prod_j ||h_{S_j}|| <= e^{-mu d} n_X^w kappa^{k-1}`:
  ||[tau_t(A),B]||
    <= ||[A,B]|| + ||A|| ||B|| e^{-mu d} n_X^w * sum_{k>=1} 2^{k+1} kappa^{k-1} |t|^k / k!.

### 4.5 Resum the series exactly

Rewrite the summand to expose `(2 kappa |t|)^k`:
  2^{k+1} kappa^{k-1} |t|^k
    = 2^{k+1} kappa^{k-1} |t|^k * ( 2^k kappa^k |t|^k ) / ( 2^k kappa^k |t|^k )   [multiply/divide]
    = ( 2^{k+1} kappa^{k-1} / (2^k kappa^k) ) * (2 kappa |t|)^k
    = ( 2 / kappa ) * (2 kappa |t|)^k.
Therefore
  sum_{k>=1} 2^{k+1} kappa^{k-1} |t|^k / k!
    = (2/kappa) sum_{k>=1} (2 kappa |t|)^k / k!
    = (2/kappa) ( e^{2 kappa |t|} - 1 ).          [exponential series minus k=0 term]

### 4.6 Final display

  ||[tau_t(A),B]||
    <= ||[A,B]|| + ||A|| ||B|| e^{-mu d} n_X^w * (2/kappa)(e^{2 kappa |t|} - 1)
    =  ||[A,B]|| + ( 2 ||A|| ||B|| n_X^w / kappa ) * e^{-mu d} ( e^{2 kappa |t|} - 1 ).
Using the start-factor bound `n_X^w <= |X| kappa`, i.e. `n_X^w / kappa <= |X|`:

  ==================================================================
  ||[tau_t(A),B]||  <=  ||[A,B]||  +  2 ||A|| ||B|| |X| * e^{-mu d} ( e^{2 kappa |t|} - 1 ).
  ==================================================================                    (LR)

Matching the requested form `||[A,B]|| + C * e^{-mu d} (e^{c kappa |t|} - 1)`:
  c = 2                        (pure dimensionless number),
  C = 2 ||A|| ||B|| |X|        (coarse start factor),
  C = 2 ||A|| ||B|| n_X^w / kappa   (SHARP start factor; always <= 2||A|| ||B|| |X|),
  with  n_X^w = sum_{S cap X != {}} ||h_S|| |S| e^{mu diam(S)}.

Independent cross-check of the constant (via the spec's own literal grouping
`2||A|| * 2^{k-1} * (2||B||)`): `2 * 2^{k-1} * 2 = 2^{k+1}` — identical to 4.3, so
the two counting routes agree; the final constant is not sensitive to how the 2's
are attributed to prefactor/interior/base.

Sanity checks on (LR):
- t = 0: `e^{0} - 1 = 0`, so `||[A,B]|| <= ||[A,B]||`. Tight, as required.
- d = 0 (X meets Y): `e^{-0} = 1`, bound is finite but non-decaying — correct,
  the causal statement is vacuous when the supports touch.
- k = 1 term check: order-1 coefficient of `(2/kappa)(e^{2kappa|t|}-1)` is
  `(2/kappa)(2 kappa|t|) = 4|t|`; times `||A|| ||B|| e^{-mu d} n_X^w` gives
  `4 ||A|| ||B|| e^{-mu d} n_X^w |t|`, equal to the direct order-1 term
  `2^{1+1} ||A|| ||B|| (e^{-mu d} n_X^w) |t|`. Consistent.

### 4.7 Velocity reading

The exponent balance `-mu d + 2 kappa |t| = 0` defines the light cone
`d = v_LR |t|` with
  v_LR = 2 kappa / mu.
Outside the cone (`d > v_LR |t|`) the bound decays exponentially in `d - v_LR|t|`;
the prefactor of the growing exponential is `2||A|| ||B|| |X|` (or the sharp
`2||A|| ||B|| n_X^w / kappa`).

## Section 5 — CONSISTENCY REDUCTION (strict bond class)

Specialize: `h_S = 0` unless `S` is a bond (nearest-neighbor pair), and
`||h_b|| <= J` for every bond `b`.

### 5.1 Exact kappa for bonds

For a bond `b = {x,y}` with `x,y` nearest neighbors: `|b| = 2`,
`diam(b) = d(x,y) = 1`. On `Z^3` each site has `2*3 = 6` incident bonds. Hence
  kappa = sup_x sum_{b ni x} ||h_b|| |b| e^{mu diam(b)}
        <= sup_x sum_{b ni x} J * 2 * e^{mu*1}
        =  (6 bonds) * J * 2 * e^{mu}
        =  12 J e^{mu}.
Saturated when every `||h_b|| = J`, so exactly
  kappa_bond = 12 J e^{mu}.                                            (5.1)

### 5.2 General bound specialized

Plug (5.1) into (LR). The exponential rate is `c*kappa = 2*kappa`:
  rate_gen = 2 * kappa_bond = 2 * 12 J e^{mu} = 24 J e^{mu},
  ||[tau_t(A),B]|| <= ||[A,B]|| + 2||A|| ||B|| |X| e^{-mu d} ( e^{24 J e^{mu} |t|} - 1 ),
  v_gen = 2 kappa_bond / mu = 24 J e^{mu} / mu.                        (5.2)

### 5.3 Sibling direct-bond comparator (supplied)

Supplied form: "activity 20J, mu-form  e^{-mu d + 20 J |t| e^{mu}}", i.e.
  rate_sib = 20 J e^{mu},   v_sib = 20 J e^{mu} / mu.                  (5.3)
Same shape as (5.2): `e^{-mu d}` times an exponential growing in `|t|` at a
constant rate (the sibling's `e^{...}` versus our `(e^{...}-1)` differ only by
the harmless subtracted `t=0` term).

### 5.4 Which is stronger, and by how much

  rate_gen / rate_sib = 24 J e^{mu} / (20 J e^{mu}) = 24/20 = 6/5,
  v_gen / v_sib       = 6/5 = 1.2.
The GENERAL bound is WEAKER: larger exponential rate, larger LR velocity (a
looser causal cone), by an exact factor 6/5 (20% slower decay onset). Same
functional shape, as anticipated.

### 5.5 Exact accounting of the 6/5 gap (where the slack lives)

Track the per-step "activity" each derivation uses (rate = 2 * per-step activity;
the Duhamel factor 2 is common to both, so the whole gap is in the activity):
- General per-step activity = kappa_bond = 12 J e^{mu}. The "12" is
  `|b| * (bonds per site) = 2 * 6`. The factor `|b| = 2` is the site-weight that
  the general machinery must carry; the "6" is the site degree. This "12" is the
  union-bound value of (STAR): for a fixed bond `b_j`,
    sum_{b' cap b_j != {}} w*(b') <= |b_j| * kappa = 2 * 12 J e^{mu} = 24 J e^{mu}
  (this is the k-independent per-step multiplier is kappa = 12 J e^{mu} once the
  carried |b_j|=2 is accounted, i.e. 24/2).
- The TRUE bond meeting count is smaller. Bonds meeting `b_j = {x,y}` =
  (6 through x) + (6 through y) - (1 shared, = b_j itself) = 11 distinct bonds.
  The union bound in (STAR) double-counts the shared bond `b_j`, giving 12
  instead of 11 — that is the (12 -> 11) unit of slack.
- The sibling's Duhamel SELF-DROP removes the self-continuation `b' = b_j`,
  leaving 10 non-self neighboring bonds. Per-step activity `10 J e^{mu}`, hence
  rate `2 * 10 J e^{mu} = 20 J e^{mu}` — exactly (5.3).
Summary of the ladder (per-step activity, in units of `J e^{mu}`):
  12  (general: site-weight union bound, keeps self, double-counts self)
  11  (distinct bonds meeting b_j)                         [remove union double-count]
  10  (distinct non-self bonds meeting b_j)                [remove self via self-drop]
  rate = 2 * activity:  general 24  vs  sibling 20;  ratio 6/5.
So the general bound is looser by exactly the two coarsenings it makes relative
to a bond-tailored count: (i) the site-weighted union bound in (STAR) (12 vs 11),
and (ii) retaining the self term that the sibling's self-drop discards (11 vs 10).
Both are structural features of the general summation layer, not arithmetic
errors. (The sibling's "20" is SUPPLIED; the reconstruction here rationalizes it
as `2 x 10 J e^{mu}` — see LIMITS item L7 for the caveat.)

## Section 6 — INSTANCE FAMILY (exactly summable, for runner gates)

Supplied family: pair interactions only,
  h_{x,y} = lambda^{|x-y|} * (2-site Hermitian),   rational `lambda`, `0 < lambda < 1`,
where `|x-y| = d(x,y)` is the ambient graph (l^1) distance and equals the pair's
diameter. Let `J_0 := ||2-site Hermitian part||` (norm of the fixed 2-site
factor), so `||h_{x,y}|| = J_0 lambda^{|x-y|}`; the clean normalization is
`J_0 = 1`. No on-site term (`x != y`). Set the standing abbreviation
  rho := lambda * e^{mu}.

For every pair `S = {x,y}`:  `|S| = 2`, `diam(S) = |x-y| = r >= 1`,
`||h_S|| = J_0 lambda^{r}`, so
  w*(S) = ||h_S|| |S| e^{mu diam(S)} = J_0 lambda^{r} * 2 * e^{mu r}
        = 2 J_0 (lambda e^{mu})^{r} = 2 J_0 rho^{r}.

### 6.1 Site-distance counts (exact)

Z^3: number of sites at graph distance `r` from a fixed site (the l^1 sphere
`|y_1|+|y_2|+|y_3| = r`):
  N_3(r) = 4 r^2 + 2   for r >= 1.
Verification (small r):
  r=1: 6 axis neighbors;  4*1+2 = 6.                                    OK
  r=2: (one coord +-2: 6) + (two coords +-1: C(3,2)*2*2 = 12) = 18;  4*4+2 = 18.  OK
  r=3: (+-3: 6) + (+-2 & +-1: 3*2*2*2 = 24) + (+-1,+-1,+-1: 2^3 = 8) = 38; 4*9+2 = 38.  OK

1D chain (Z): sites at distance `r` are `x+r` and `x-r`, so
  N_1(r) = 2   for r >= 1.

### 6.2 kappa on Z^3 (exact rational function of lambda, e^{mu})

  kappa_3D = sup_x sum_{S ni x} w*(S)
           = sum_{r>=1} N_3(r) * 2 J_0 rho^{r}     [translation invariance; group by r]
           = 2 J_0 sum_{r>=1} (4 r^2 + 2) rho^{r}.
Exact geometric identities (valid for |rho| < 1):
  sum_{r>=1} rho^r     = rho/(1-rho),
  sum_{r>=1} r rho^r   = rho/(1-rho)^2,
  sum_{r>=1} r^2 rho^r = rho(1+rho)/(1-rho)^3.
Hence
  sum_{r>=1}(4 r^2 + 2) rho^r
    = 4 * rho(1+rho)/(1-rho)^3 + 2 * rho/(1-rho)
    = [ 4 rho(1+rho) + 2 rho (1-rho)^2 ] / (1-rho)^3.
Numerator, expanded exactly:
  4 rho(1+rho)        = 4 rho + 4 rho^2,
  2 rho (1-rho)^2     = 2 rho - 4 rho^2 + 2 rho^3,
  sum                 = 6 rho + 2 rho^3 = 2 rho (3 + rho^2).
Therefore
  ============================================================
  kappa_3D = 2 J_0 * 2 rho (3 + rho^2) / (1-rho)^3
           = 4 J_0 * rho (3 + rho^2) / (1 - rho)^3,   rho = lambda e^{mu}.
  ============================================================                      (6.2)
Convergence condition:  rho = lambda e^{mu} < 1, i.e.  lambda e^{mu} < 1
(equivalently mu < ln(1/lambda)). The polynomial `4r^2+2` does not change the
radius of convergence `rho < 1`.
Consistency check (small rho, i.e. near-nearest-neighbor dominance):
  kappa_3D = 4 J_0 rho (3 + O(rho^2))/(1-rho)^3 -> 12 J_0 rho = 12 J_0 lambda e^{mu},
matching the leading nearest-neighbor term `N_3(1)*2 J_0 rho = 6*2 J_0 rho`, and
structurally the bond "12" of Section 5.1. OK.

### 6.3 kappa on the 1D chain (exact)

  kappa_1D = sum_{r>=1} N_1(r) * 2 J_0 rho^r = 2 J_0 sum_{r>=1} 2 rho^r
           = 4 J_0 sum_{r>=1} rho^r
  ============================================================
  kappa_1D = 4 J_0 * rho / (1 - rho),   rho = lambda e^{mu},  converges iff lambda e^{mu} < 1.
  ============================================================                      (6.3)

### 6.4 Resulting exact LR rate / velocity for these families

Rate = 2 kappa, velocity v = 2 kappa / mu (Section 4.7). Exact closed forms
(rational in `lambda, e^{mu}`, times 1/mu), ready for runner gate assertions:
  Z^3:   rate_3D = 8 J_0 rho (3 + rho^2) / (1-rho)^3,   v_3D = rate_3D / mu.
  chain: rate_1D = 8 J_0 rho / (1-rho),                 v_1D = rate_1D / mu.
Full bound, e.g. Z^3:
  ||[tau_t(A),B]|| <= ||[A,B]|| + 2||A|| ||B|| |X| e^{-mu d}
                        ( exp[ 8 J_0 rho (3+rho^2)/(1-rho)^3 * |t| ] - 1 ),  rho = lambda e^{mu}.

Worked rational sample (advisory floats in brackets), `J_0 = 1`, `lambda = 1/2`,
`e^{mu} = 3/2`  =>  `rho = 3/4 < 1`:
  1 - rho = 1/4,  (1-rho)^3 = 1/64,  3 + rho^2 = 3 + 9/16 = 57/16.
  kappa_3D = 4 * (3/4) * (57/16) / (1/64) = 3 * (57/16) * 64 = 3 * 57 * 4 = 684.
  [exact kappa_3D = 684 J_0 ;  rate_3D = 1368 J_0]
  kappa_1D = 4 * (3/4) / (1/4) = 3 * 4 = 12.   [exact kappa_1D = 12 J_0; rate_1D = 24 J_0]
All exact rationals — no floats enter the gate values.

## Section 7 — LIMITS (assumptions and supervisor double-check list)

L1. Duhamel/norm-transport layer taken as GIVEN. The whole of Section 4 consumes
    the sibling's unrolled series verbatim: prefactor `2||A||`, interior `2^{k-1}`,
    base `||[h_{S_k},B]|| <= 2||h_{S_k}|| ||B||`, iterated integrals `|t|^k/k!`,
    boundary reduction `[H,A] = sum_{S cap X != {}} [h_S,A]`, self-drop, and
    `||f(t)|| <= ||f(0)|| + int ||R||`. I did NOT re-derive these. Supervisor must
    confirm the sibling's actual series constant matches the transcribed shape;
    the final constant `C` and rate `c=2` inherit directly from it. (I cross-checked
    the 2-powers two ways in 4.3/4.6, but both routes assume the same input shape.)

L2. CONSECUTIVE-overlap chain structure is load-bearing for Section 3. The step
    bound (STAR) sums over `S_{j+1}` meeting only the IMMEDIATELY preceding `S_j`.
    If the sibling's expansion instead produces overlaps with the CUMULATIVE
    support `Union_{i<=j} S_i`, the clean `|S_j| kappa` step fails (it would become
    `|Union_{i<=j} S_i| kappa`, which grows in j). The standard reduction to
    consecutive overlaps (reproducing/convolution property of the weight) is part
    of the "given" machinery; my counting layer REQUIRES the consecutive-overlap
    form as delivered. Supervisor: confirm the sibling delivers consecutive overlap.

L3. `diam(S)` = AMBIENT graph-distance diameter, `max_{u,v in S} d(u,v)`. Only used
    via (D) `d(u,v) <= diam(S)` and the triangle inequality. If the sibling uses
    the INTRINSIC (within-S path) diameter, the chain lemma still holds a fortiori
    (intrinsic >= ambient), but the numerical value of `kappa` in (K) would differ.
    Confirm which diameter the sibling's `kappa` uses; the two must be the SAME
    definition for Sections 3-6 to interlock.

L4. Connectedness of each interaction set `S` is used (only) to make (D) hold with
    the ambient diameter. If disconnected `S` carry `h_S != 0`, redefine `diam(S)`
    or the reach bound breaks. Spec assumes connected — carried as hypothesis.

L5. `d = d(X,Y) >= 1` assumed. For `d = 0` (touching supports) the bound is finite
    but non-decaying (correct, but outside the causal regime).

L6. The union bound in (STAR) and in the start factor `n_X^w <= |X| kappa` is the
    ONLY slack in the counting layer: a set meeting `S_j` (resp. `X`) in >= 2 sites
    is over-counted. Quantified exactly in Section 5.5 for bonds (12 vs 11). If a
    sharper per-step "meeting activity" is available, `kappa` can be replaced by it
    throughout with no other change; the sharp start factor `n_X^w` is already
    retained in the sharp form of `C`.

L7. The sibling bond comparator "activity 20J / e^{-mu d + 20 J |t| e^{mu}}" is
    SUPPLIED, not re-derived here. My Section 5.5 reconstruction (`rate = 2 x 10 J e^{mu}`,
    the 10 = distinct non-self bonds meeting a bond, self removed by the Duhamel
    self-drop) rationalizes the "20" and yields the exact 6/5 gap. If the sibling's
    20 arises from a DIFFERENT mechanism (different normalization, U-integrated
    figure, or a different weight), only the QUALITATIVE conclusion survives
    ("general is weaker, same shape"); the exact 6/5 ratio then needs the sibling's
    derivation to match this reconstruction. Supervisor: verify against the sibling
    note that (i) the sibling rate is `20 J e^{mu}`, (ii) it comes from a bond count
    of 10 non-self neighbors times the Duhamel 2.

L8. Instance family assumptions (Section 6): pair-only (no on-site term, `x != y`);
    `||h_{x,y}|| = J_0 lambda^{|x-y|}` with `|x-y|` = l^1 graph distance = pair
    diameter. The count `N_3(r) = 4r^2 + 2` is specific to l^1 distance on the cubic
    `Z^3` graph (verified r=1,2,3). A different metric for `diam` (l^inf, Euclidean-
    rounded) changes `N(r)` and hence the closed form (6.2). The 2-site factor is
    assumed uniform (same operator, only the scalar `lambda^{|x-y|}` varies); a
    site/direction-dependent factor only needs `sup` <= `J_0` and the bounds persist
    as upper bounds.

L9. Convergence `lambda e^{mu} < 1` is NECESSARY for `kappa < infinity` in the
    instance family (both Z^3 and chain). For fixed `lambda < 1`, admissible
    `mu in (0, ln(1/lambda))`. The velocity `v(mu) = 2 kappa(mu)/mu` may be
    OPTIMIZED over that interval for the tightest cone — NOT done here (advisory).
    As `mu -> ln(1/lambda)^-` (rho -> 1^-) both `kappa_3D` and `kappa_1D` blow up
    like `(1-rho)^{-3}` resp. `(1-rho)^{-1}`; the best `mu` is interior.

L10. Exact-arithmetic identities used and their provenance: geometric sums
     `sum r rho^r = rho/(1-rho)^2`, `sum r^2 rho^r = rho(1+rho)/(1-rho)^3` (standard;
     the load-bearing algebra `4rho(1+rho)+2rho(1-rho)^2 = 6rho+2rho^3` is shown in
     full in 6.2). The Section 6.4 sample (`lambda=1/2, e^mu=3/2 => kappa_3D=684 J_0,
     kappa_1D=12 J_0`) is exact rational; bracketed decimals elsewhere are advisory.

L11. `kappa`-uniformity / thermodynamic limit: all bounds are uniform in the finite
     region `Lambda` provided `kappa` (a `sup_x` of a per-site sum) is
     `Lambda`-independent, which holds for translation-invariant-bounded families.
     Only the finite-`Lambda` statement is claimed here.

L12. (LR) is a one-sided UPPER bound. It certifies a light cone `v_LR = 2 kappa/mu`
     but says nothing about optimality/tightness of that velocity, nor about lower
     bounds on information propagation. `C = 2||A|| ||B|| |X|` scales with `|X|`
     (support of A) but not `|Y|` — asymmetric by construction (B enters only
     through the base commutator `||B||`).

---

## Final-display recap (load-bearing results)

Master bound (Section 4.6, eq. (LR)):
  ||[tau_t(A),B]||  <=  ||[A,B]||  +  C * e^{-mu d} ( e^{c kappa |t|} - 1 ),
    c = 2,
    C = 2 ||A|| ||B|| |X|              (coarse),
    C = 2 ||A|| ||B|| n_X^w / kappa    (sharp),   n_X^w = sum_{S cap X != {}} ||h_S|| |S| e^{mu diam(S)} <= |X| kappa.
  Light cone velocity:  v_LR = 2 kappa / mu.

Counting-layer intermediates:
  (CL)  sum_j diam(S_j) >= d                                    [chain lemma]
  (WS)  Prod_j ||h_{S_j}|| <= e^{-mu d} Prod_j w(S_j)           [weight split]
  (STAR) sum_{S' cap S_j != {}} ||h_{S'}|| |S'| e^{mu diam S'} <= |S_j| kappa   [single-step]
  (3)   Sigma_k = sum_chains Prod_j w(S_j) <= n_X^w kappa^{k-1} <= |X| kappa^k
  (3')  sum_chains Prod_j ||h_{S_j}|| <= e^{-mu d} n_X^w kappa^{k-1}

Exact kappa values:
  Strict bonds (||h_b|| <= J):   kappa = 12 J e^{mu}         [Section 5.1]
  Pair family lambda^{|x-y|} on Z^3:  kappa_3D = 4 J_0 rho (3 + rho^2) / (1-rho)^3,  rho = lambda e^{mu} < 1   [6.2]
  Pair family on 1D chain:            kappa_1D = 4 J_0 rho / (1-rho),                  rho = lambda e^{mu} < 1   [6.3]

Consistency (Section 5.4-5.5): specializing (LR) to bonds gives rate
`2 kappa = 24 J e^{mu}` vs the sibling's direct `20 J e^{mu}`; general is weaker
by exactly 6/5 (same shape), the gap being the site-weighted union bound (12->11)
plus the retained self term (11->10).

