# waves-need-signed-weights, independent attempt a4

Worker `w-macbookpro90c72-jf9e6`, model claude-opus-5.
Script: `check.py` in this directory (exact arithmetic; 41 `ok` lines, 0 `BAD`, exit 0).

## 0. Setting and notation

Event lattice `Z^d` (sites) x `Z` (levels). A linear formation law with `J` levels of
memory is

    theta_{t+1}(x) = sum_{j=0}^{J-1} (W_j * theta_{t-j})(x)
                   = sum_j sum_y W_j(y) theta_{t-j}(x - y),

each `W_j : Z^d -> R` finitely supported. Symbol `What_j(k) = sum_y W_j(y) e^{-i k.y}`,
`k` in the torus `T^d`. The ansatz `theta_t(x) = lam^t e^{i k.x}` gives the dispersion
relation

    chi_k(lam) = lam^J - sum_j What_j(k) lam^{J-1-j} = 0,          (D)

with `J` branches `lam_1(k), ..., lam_J(k)`. Write `g_j := What_j(0) = sum_y W_j(y)` and
call `G := sum_j g_j` the gain; gain-one means `G = 1` (the law reproduces a constant
record field: the overlap weights of a record sum to one). "Nonnegative" means
`W_j(y) >= 0` for every `j, y` (the GIVEN's reading: an overlap weight is a probability).
A branch *propagates without loss on a band* when `|lam(k)| = 1` for all `k` in a nonempty
open `U` subset of `T^d`.

Definitions of the formation law, the gain-one normalization and the record reading are
taken from the claim's GIVEN and from the two prior attempts in this directory:
`w-jonathonsmac4f50-jafb3/ATTEMPT.md` (a2) and `w-jonathonsmac4f50-j62b1/ATTEMPT.md` (a5).

## 1. The exact statement attempted

**(a)** With nonnegative weights over finitely many levels, no branch of (D) has
`|lam(k)| = 1` on a nonempty open set -- prove it or find the exception.
I find the exception and classify it exactly (Step 1), which is stronger than the task's
"all branches" reading: the hypothesis is one branch.

**(b)** Classify the minimal signed rules that propagate: dispersion, stability region,
speed. I give the depth rigidity of the deepest level, the ladder relating all levels at
every `J`, the exact lossless region for `J = 3`, and the exact cone radii on `Z^d`
(Steps 3-7).

**(c)** What rule on amplitudes reproduces the signed recursion, and what is kept and
lost. a2 works the 1+1 two-component example exactly and was refereed; I do not redo it.
I give the bridge that makes the signed weight *forced* rather than chosen, the resulting
constraint on any finite-range unitary rule in any dimension, and the consequence for the
record statistics (Steps 8-9).

## 2. Steps

### Step 1 (a), one branch, nonnegative weights. PROVED; the reduction CHECKED in S0.

**Statement.** Let `W_0, ..., W_{J-1} >= 0` be finitely supported on `Z^d`, gain
`G = sum_j g_j`.

1. If `G < 1`, no branch of (D) is unimodular at any `k`.
2. If `G = 1` and some branch has `|lam(k)| = 1` for every `k` in a nonempty open
   `U` subset of `T^d`, then every level carrying mass is a single site,
   `W_j = g_j delta_{y_j}` with `g_j > 0`, and there is one `v` in `Q^d` with
   `y_j = (j+1) v` for every such `j` (so `(j+1)v` is in `Z^d` for each active `j`).
3. Conversely every rule of that form has the branch `lam(k) = e^{-i k.v}`, unimodular at
   every `k`, and all its other branches satisfy `|lam(k)| <= 1` at every `k`.

So the only nonnegative gain-one laws that carry a band without loss are

    theta_{t+1}(x) = sum_j g_j theta_{t-j}(x - (j+1)v),

rigid transport at velocity `v` per level, composed with a `k`-free average over delays.
Memory does not rescue waves from positive weights.

**Proof.** At a `k` where a branch has `|lam| = 1`, divide (D) by `lam^J` and put
`z := lam^{-1}`, `|z| = 1`:

    1 = sum_j What_j(k) z^{j+1}.                                    (1.1)

Nonnegativity gives `|What_j(k)| = |sum_y W_j(y) e^{-i k.y}| <= sum_y W_j(y) = g_j`, so

    1 = |sum_j What_j z^{j+1}| <= sum_j |What_j| <= sum_j g_j = G.  (1.2)

This is impossible when `G < 1`, which is part 1.

Let `G = 1`. Then (1.2) is a chain of equalities. The right equality is termwise
(`|What_j| <= g_j` for each `j`), hence

    |What_j(k)| = g_j   for every j.                                (1.3)

The left equality says the nonzero terms `c_j := What_j(k) z^{j+1}` all have one argument;
their sum is `1`, so that argument is `0` and `c_j = |c_j| = g_j`:

    What_j(k) z^{j+1} = g_j   for every j.                          (1.4)

*Support.* (1.3) is equality in the triangle inequality for the nonnegative coefficients
`W_j(y)`, so all `e^{-i k.y}` with `y` in `supp W_j` coincide: `k.(y - y')` is in `2 pi Z`
for `y, y'` in `supp W_j`. For a fixed `m := y - y'` different from `0`, the set
`{k in T^d : k.m in 2 pi Z}` is a finite union of affine hyperplane slices of the torus and
has empty interior (a nonzero linear functional is nonconstant on any open set). Since the
condition holds on the open set `U`, `m = 0`. Hence `supp W_j` is one point and
`W_j = g_j delta_{y_j}` for each active `j`.

*Phase.* Now `What_j(k) = g_j e^{-i k.y_j}` and (1.4) reads `z^{j+1} = e^{i k.y_j}` for
each active `j`. For two active levels `j, j'`, raising to the powers `j'+1` and `j+1` and
comparing gives `k.[(j'+1) y_j - (j+1) y_{j'}]` in `2 pi Z` for every `k` in `U`, so by the
same hyperplane argument `(j'+1) y_j = (j+1) y_{j'}`. Fixing one active `j0` and setting
`v := y_{j0}/(j0+1)` gives `y_j = (j+1) v` for every active `j`, which is part 2.

*Converse.* For `W_j = g_j delta_{(j+1)v}`, substitute `lam = mu e^{-i k.v}` in (D). The
`j`-th term carries `e^{-i(j+1)k.v}` from the symbol and `e^{-i(J-1-j)k.v}` from
`lam^{J-1-j}`, total `e^{-i J k.v}`, the same factor as `lam^J`, so

    chi_k(mu e^{-i k.v}) = e^{-i J k.v} ( mu^J - sum_j g_j mu^{J-1-j} ),   (1.5)

and the bracket `Q(mu)` carries no `k`. [S0 verifies (1.5) symbolically at `J = 2, 3, 4`.]
`Q(1) = 1 - sum_j g_j = 0`, so `mu = 1` is a root and `lam = e^{-i k.v}` is a branch,
unimodular at every `k`. If `|mu| > 1` then
`|mu|^J = |sum_j g_j mu^{J-1-j}| <= |mu|^{J-1} sum_j g_j = |mu|^{J-1} < |mu|^J`, a
contradiction, so every other root has `|mu| <= 1`. That is part 3. QED

**Provenance.** For `J = 1` the support step is the classical characterization of the
distributions whose characteristic function has modulus one at a point (a point mass on a
coset). What is derived here is the multi-level statement: the active levels are forced to
share one velocity through the *phase* condition (1.4), and the reduction (1.5) then makes
the whole spectrum `k`-free up to the transport phase.

### Step 2 The exception is non-vacuous, and "open set" is load-bearing. CHECKED in S0.

`J = 3`, `d = 1`, `g = (1/2, 0, 1/2)`, `v = 1`:

    theta_{t+1}(x) = (1/2) theta_t(x-1) + (1/2) theta_{t-2}(x-3),

`Q(mu) = mu^3 - mu^2/2 - 1/2 = (mu - 1)(mu^2 + mu/2 + 1/2)`. The transport branch is
unimodular at every `k`; the other two are a conjugate pair (discriminant `-7/4 < 0`) of
modulus `1/sqrt 2`. So a rule that is not pure transport, and not a single level, can still
carry one lossless band -- the exception of Step 1 is occupied.

One step outside the classified family kills it. `J = 2`, `W_0 = W_1 = delta_1/2`: both
levels are single sites, but Step 1 needs `y_1 = 2 y_0 = 2` and this rule has `y_1 = 1`.
Its characteristic polynomial `P(lam) = lam^2 - (e^{-ik}/2) lam - e^{-ik}/2` has a
unimodular root only at the isolated point `k = 0`. Certificate: for
`P*(lam) := lam^n conj(P)(1/conj lam)` (the conjugate-reverse, whose roots are
`1/conj(root)`), a unimodular root of `P` is a common root of `P` and `P*`, so
`Res(P, P*) != 0` rules out any unimodular root. S0 computes, exactly,
`Res = 1/8, 1/4, 1/2` at `k = pi/3, pi/2, pi` and `Res = 0` at `k = 0`. Only this direction
of the resultant test is used; its converse is not valid and is not needed.

### Step 3 (b) Depth rigidity: the deepest level is one site. PROVED; instances CHECKED in S1, S9.

Drop nonnegativity: `W_j` real (or complex), finitely supported. Suppose **all** `J` branches
are unimodular for every `k` in a nonempty open `U`.

From (D), `prod_i lam_i = (-1)^{J+1} What_{J-1}(k)`, so `|What_{J-1}(k)| = 1` on `U`.
Expand `|What|^2 = sum_m A(m) e^{-i k.m}` with the autocorrelation
`A(m) = sum_y W_{J-1}(y) conj(W_{J-1}(y - m))`. Then `|What|^2 - 1` is a finite exponential
sum vanishing on `U`, so by Lemma L below it vanishes identically:

    A(0) = ||W_{J-1}||_2^2 = 1,   A(m) = 0 for m != 0.               (3.1)

If `supp W_{J-1}` had two or more points, pick a linear functional `xi` injective on that
finite set (the bad `xi` lie in finitely many proper subspaces), let `y_max, y_min` be its
extremes and `m* := y_max - y_min != 0`. In `A(m*)` the only `y` with both `y` and `y - m*`
in the support is `y = y_max` (since `xi.y <= xi.y_max` and `xi.(y - m*) >= xi.y_min` force
equality in both, and `xi` is injective), so
`A(m*) = W_{J-1}(y_max) conj(W_{J-1}(y_min)) != 0`, contradicting (3.1). Hence

    W_{J-1} = c delta_{y0},   |c| = 1;   real case: W_{J-1} = +- delta_{y0}.   (3.2)

The deepest level of a lossless rule is one site of unit weight: no averaging, no spreading,
no free coefficient. [S1 checks (3.1)-(3.2) on four stencils, including
`{0: 3/5, 1: -4/5}`, which has unit `l2` norm but extreme lag `-12/25 != 0` -- unit norm
alone is not enough; S9 checks the complex version `{0: 3/5, 1: 4i/5}`.]

**Lemma L. PROVED.** A finite exponential sum `f(k) = sum_{m in S} c_m e^{-i k.m}`,
`S` a finite subset of `Z^d`, vanishing on a nonempty open `U` subset of `T^d`, has all
`c_m = 0`.
*Proof.* Fix `k0` in `U` and choose `w` in `R^d` with the numbers `a_m := w.m` (`m` in `S`)
pairwise distinct; possible because the excluded `w` lie in the finitely many proper
subspaces `{w : w.(m - m') = 0}`, `m != m'`, and a finite union of proper subspaces is not
all of `R^d`. For small `|s|`, `k0 + s w` is in `U`, so
`g(s) := f(k0 + s w) = sum_m d_m e^{-i s a_m} = 0` on an interval, `d_m := c_m e^{-i k0.m}`.
All derivatives vanish at `s = 0`: `sum_m d_m (-i a_m)^n = 0` for `n = 0, ..., |S|-1`. That
is a square linear system whose matrix is Vandermonde in the pairwise distinct nodes
`-i a_m`, hence invertible, so `d = 0` and `c = 0`. ASSUMED: the Vandermonde determinant
formula (standard, used only through "distinct nodes => invertible"). QED

### Step 4 (b) The ladder, every `J`. PROVED; residuals CHECKED in S2.

With all branches unimodular at `k`, write `e_r` for the elementary symmetric functions of
`lam_1..lam_J`. Matching `chi = prod_i (lam - lam_i) = sum_r (-1)^r e_r lam^{J-r}` against
(D) gives

    What_j = (-1)^j e_{j+1},   in particular What_{J-1} = (-1)^{J-1} e_J.   (4.1)

On the unit circle `conj(lam_i) = 1/lam_i`, and from
`prod_i (lam_i + t) = sum_s e_{J-s} t^s` divided by `e_J`,
`e_r(1/lam) = e_{J-r}(lam)/e_J` (legitimate: `|e_J| = 1 != 0`). So
`conj(e_r) = e_{J-r}/e_J`. Substituting into (4.1),

    conj(What_{J-2-j}) = (-1)^{J-j} e_{j+1}/e_J = -What_j / What_{J-1},

that is

    What_j = -What_{J-1} conj(What_{J-2-j}),   0 <= j <= J-2.          (4.2)

[S2 checks (4.2) at `J = 2, 3, 4` on generic unimodular root triples/quadruples, and the
`J = 2` instance `What_1 = -1`, where (4.2) collapses to `What_0` real.]

In real space, using (3.2) with `W_{J-1} = eps delta_{y0}` and
`conj(What(k)) = ` symbol of `reflect(W)`, `reflect(W)(y) := W(-y)`:

    W_j = - eps S_{y0} reflect(W_{J-2-j}),   S_{y0} = shift by y0.     (4.3)

So a lossless real rule is determined by its lower half: the levels pair up
`j <-> J-2-j` by reflection through `y0`, up to the overall sign `eps` of the deepest level.
For `J` even, `J-2` is even and the middle level `j = (J-2)/2` is paired with itself, so
(4.3) constrains it alone: `W_{(J-2)/2} = -eps S_{y0} reflect(W_{(J-2)/2})`. For `J` odd
there is no self-paired level.

**Consistency with Step 1.** If all `W_j >= 0`, then `eps = +1` in (3.2), and (4.2) at
`k = 0` gives `g_j = -g_{J-2-j}` with both sides `>= 0`, hence `g_j = 0` for all
`j <= J-2`: the rule is `theta_{t+1}(x) = theta_{t-J+1}(x - y0)`, pure delayed transport --
the all-branches case of Step 1 with only the deepest level active.

### Step 5 (b) `J = 3`: the lossless region is a closed deltoid. PROVED; CHECKED in S3, S4.

For `J = 3`, (4.2) reads `What_0 = -What_2 conj(What_1)` and
`What_1 = -What_2 conj(What_0)`. Put `lam = sigma nu` with `sigma^3 = What_2`, `|sigma| = 1`.
Then `chi(sigma nu)/sigma^3 = nu^3 - b nu^2 + conj(b) nu - 1` with `b := What_0/sigma`:
the second relation gives `What_1 = -sigma^2 conj(b)`, so the linear coefficient is
`-conj(b)` automatically. Every `J = 3` lossless candidate is this one-complex-parameter
self-inversive cubic.

Its discriminant, computed exactly in S3, is

    D(b) = |b|^4 + 18 |b|^2 - 8 Re(b^3) - 27,   b = x + i y,          (5.1)
         = (x^2+y^2)^2 + 18(x^2+y^2) - 8 x (x^2 - 3 y^2) - 27.

**All three roots are unimodular iff `D(b) <= 0`.** Both directions, exactly:

* (=>) Roots `e^{i th_1}, e^{i th_2}, e^{i th_3}`:
  `D = -64 prod_{i<j} sin^2((th_i - th_j)/2) <= 0` [S4, symbolic], with equality iff two
  roots collide.
* (<=) If some root is off the circle: the root set is invariant under
  `r -> 1/conj(r)`, an involution on three roots, so one root is unimodular and the other
  two are `rho e^{i del}, e^{i del}/rho` with `rho > 1`; the product being `1` fixes the
  third as `e^{-2 i del}`. For that family [S4, symbolic]
  `D = (rho - 1/rho)^2 (2 cos 3 del - rho - 1/rho)^2 > 0`, since `rho + 1/rho > 2 >= 2 cos 3 del`.

So the lossless region `E_3 = {D <= 0}` is the closed deltoid with cusps at `3, 3 omega,
3 omega^2` (`omega = e^{2 pi i/3}`; S3 verifies `D = 0` there), and its real section is

    D(x, 0) = (x + 1)(x - 3)^3,   D <= 0  iff  x in [-1, 3].          (5.2)

[S4 also checks two numeric instances: the unimodular triple `(3+4i)/5, (5+12i)/13` and
their reciprocal product gives `D = -17438976/17850625 < 0`; `b = 10` gives `D = 3773 > 0`.]

### Step 6 (b) The gain-one three-level rule: one blinking branch, window `[-3, 1]`. PROVED; CHECKED in S5.

The referee's rule and its three-level relative. Let `P` be any real symmetric averaging
operator (`Phat(k)` real; the nearest-neighbour average has `Phat = (1/d) sum_j cos k_j`).

* `J = 2`: `theta_{t+1} = 2 a P theta_t - theta_{t-1}`, i.e. `What_0 = 2 a Phat`,
  `What_1 = -1`. Then `lam^2 - 2 a Phat lam + 1 = 0`, `cos om = a Phat`: unimodular iff
  `|a Phat| <= 1`, a CFL-type condition, and (4.2) is satisfied identically.
* `J = 3`, gain one: `theta_{t+1} = P(theta_t + theta_{t-1}) - theta_{t-2}`. Gain at
  `k = 0` is `1 + 1 - 1 = 1`. Here

      chi = lam^3 - Phat lam^2 - Phat lam + 1 = (lam + 1)(lam^2 - (1 + Phat) lam + 1).  (6.1)

  [S5 checks the factorization symbolically.] So there is a branch `lam = -1` at **every**
  `k` -- `theta_t = (-1)^t f` solves the recursion for an arbitrary `f`, because the two
  middle terms cancel [S5 runs it exactly in `Fraction` arithmetic on a ring of 7 sites for
  6 ticks] -- plus a wave pair with

      cos om = (1 + Phat)/2,  unimodular iff |1 + Phat| <= 2 iff Phat in [-3, 1].  (6.2)

  Outside the window the pair is a real reciprocal pair `+-(r, 1/r)`, `r > 1` [S5 factors
  both regimes]. The window is one-sided: it bites only as `Phat -> 1`, i.e. `k -> 0`.
  The nearest-neighbour average has `Phat` in `[-1, 1]`, so this rule never leaves it.

  Consistency with Step 5: here `What_2 = -1 = eps delta_0` with `eps = -1`, `sigma = -1`,
  `b = What_0/sigma = -Phat`, and (5.2) says lossless iff `b` in `[-1, 3]`, i.e.
  `Phat` in `[-3, 1]` -- the window **is** the real section of the deltoid.

This is the sharp contrast with Step 1: gain one plus nonnegative weights gives no wave at
any depth; gain one with one sign flip on the deepest level gives a band of undamped waves,
with a zero-velocity blinking mode as the price.

### Step 7 (b) The cone on `Z^d` is exactly round: `1/sqrt d` and `1/sqrt(2d)`. PROVED; CHECKED in S6, S7.

Take `P` = nearest-neighbour average, `Phat = S/d`, `S := sum_j cos k_j`, and the massless
`J = 2` rule (`a = 1`): `cos om = S/d`. Differentiating,
`d(partial om/partial k_j) sin om = sin k_j`, so with `d^2 sin^2 om = d^2 - S^2`,

    |grad om|^2 = num/(d^2 - S^2),   num := sum_j (1 - cos^2 k_j),

and the exact identity [S6, `d = 1..4`]

    1/d - num/(d^2 - S^2) = pairs / ( d (d^2 - S^2) ),
    pairs := sum_{i<j} (cos k_i - cos k_j)^2 = d sum_j cos^2 k_j - S^2 >= 0.   (7.1)

`d^2 - S^2 > 0` off the band edges (`|S| = d` forces all `cos k_j = +-1` with one sign),
so `|grad om| <= 1/sqrt d` everywhere, with equality iff all `cos k_j` agree. Along any ray
`k = eps n`, `pairs = O(eps^4)` while `d^2 - S^2 = O(eps^2)`, so `|grad om| -> 1/sqrt d`
with `grad om` parallel to `n` [S6 takes the limit symbolically for `d = 2, 3`]. Hence the
closure of the group-velocity set is **exactly** the ball of radius `1/sqrt d`.

The gain-one three-level rule: `cos om = (1 + S/d)/2` gives
`4 d^2 sin^2 om = 4 d^2 - (d + S)^2` and

    1/(2d) - num/(4 d^2 - (d+S)^2) = ( (d - S)^2 + 2 pairs ) / ( 2 d (4 d^2 - (d+S)^2) ),  (7.2)

so its cone is the ball of radius `1/sqrt(2 d)`, again attained only in the `k -> 0` limit
[S6, `d = 1..4` and the limit for `d = 2, 3`]. Half the speed is the price of the third
level: the blinking branch carries no velocity, and the wave pair's frequency is halved.

The roundness is not inherited from the spectrum. At `d = 2`, `k_A = (0, 5 pi/12)` and
`k_B = (3 pi/12, 4 pi/12)` have the same `|k|` but different `cos om` [S7], so `om` is not a
function of `|k|`; only the limiting speed is isotropic, exactly, by (7.1)-(7.2).

This closes a2's open item (iii) for the scalar signed rule in every `d`, and the value
`1/sqrt 3` at `d = 3` matches the cone speed a2 records for its eight-component candidate.

### Step 8 (b) How much a spread deepest level costs. PROVED; instances CHECKED in S8.

For any rule, `prod_i |lam_i(k)| = |What_{J-1}(k)|`, so by concavity of `log` (Jensen)

    (2 pi)^{-d} int_{T^d} log prod_i |lam_i| = (2 pi)^{-d} int log |What_{J-1}|
        <= (1/2) log( (2 pi)^{-d} int |What_{J-1}|^2 ) = log ||W_{J-1}||_2.   (8.1)

A gain-one nonnegative level that is spread has `||W||_2 < 1` [S8: `1/2` for the
`1d` nearest-neighbour average, `7/18` for `{1/2, 1/3, 1/6}`], so the branches lose
amplitude at an average rate of at least `|log ||W_{J-1}||_2|` per tick. Step 3 is the
sharp form: losslessness needs `||W_{J-1}||_2 = 1` *and* zero autocorrelation at every
nonzero lag. ASSUMED: concavity of `log` and Jensen's inequality for a probability measure.

### Step 9 (c) The amplitude rule makes the signed weight forced, not chosen. PROVED; CHECKED in S9.

Let `psi_t : Z^d -> C^n` be complex record amplitudes with a finite-range local rule
`psi_{t+1}(x) = sum_y U(y) psi_t(x - y)` whose symbol `U(k)` is unitary for every `k`
(probabilities `|psi|^2` read out at the end; `sum_x |psi_t(x)|^2` is then conserved).

**(9a)** By Cayley-Hamilton applied to `U(k)`, every component of `psi` satisfies the scalar
depth-`n` recursion whose coefficients are the characteristic polynomial's:

    psi_{t+n} = sum_{r=1}^{n} (-1)^{r+1} e_r(U(k)) psi_{t+n-r},

for `n = 2`: `psi_{t+2} = (tr U) psi_{t+1} - (det U) psi_t` [S9 checks Cayley-Hamilton
symbolically for a general `2x2`]. The alternating signs are not a modelling choice; they
are the characteristic polynomial. In the notation of (D), `What_{n-1} = (-1)^{n-1} det U`,
which has modulus `1` at every `k`.

**(9b)** a2's `1+1` coin is exactly the two-level signed rule. For
`U(k) = [[c e^{-ik}, s], [-s, c e^{ik}]]`, `c = cos th`, `s = sin th`, S9 checks
`U^dagger U = I`, `det U = 1`, `tr U = 2 c cos k`, hence

    lam^2 - 2 c cos k lam + 1 = 0,

which is Step 6's `theta_{t+1} = 2 a P theta_t - theta_{t-1}` with `a = c`,
`Phat = cos k`. **The negative weight on the level before last is `-det U`.** It is
unitarity, not a probability: the amplitude rule has no negative number in it, and the
signed recursion is a consequence of eliminating the second component.

**(9c)** Combining (9a) with Step 3 (complex form): `|det U(k)| = 1` for all `k` and
`det U` is a finite exponential sum, so its autocorrelation is `delta_0` and

    det U(k) = c0 e^{-i k.y0},   |c0| = 1, y0 in Z^d.                  (9.1)

The determinant of **any** finite-range unitary formation rule, in any dimension and any
number of components, is one lattice shift times a unit constant: no averaging can appear in
it. For `n = 2` the whole dispersion is therefore
`lam^2 - (tr U(k)) lam + c0 e^{-i k.y0} = 0`, with the trace the only remaining freedom.
a2's coin is the case `c0 = 1`, `y0 = 0`.
**Provenance.** (9.1) is the formation-law form of the standard determinant fact for FIR
paraunitary matrices in filter-bank theory; the proof here is self-contained (Lemma L plus
the extreme-lag argument of Step 3) and is what licenses its use at this scope.

**(9d) What the record statistics keep and lose.** *Kept:* the amplitude law is a gain-one
local formation law (`l2` gain one instead of `l1` gain one); it is reversible, `U^{-1} =
U^dagger` is again finite range iff `U` is a Laurent polynomial in both directions (a2
records this for the coin); and Step 7's cone applies to the component recursion, so the
records have a sharp round light cone at `1/sqrt d` per tick.
*Lost:* the readout probabilities `p_t = |psi_t|^2` are **not** themselves the solution of
any nonnegative finite-depth gain-one formation law, except in the rigid-transport case.
Indeed by Step 1 such a law is either (i) `theta_{t+1}(x) = sum_j g_j theta_{t-j}(x-(j+1)v)`,
under which `supp p_t` is a rigid translate of the initial data (induction: the level-`j`
contribution lands in `supp p_{t-j} + (j+1)v = S + (t+1)v`), which the coin's spreading
support contradicts; or (ii) no branch is unimodular on an open set, which is the GIVEN's
drift-plus-diffusion case, with a `sqrt t` front, contradicting the ballistic front a2
establishes exactly for the coin. ASSUMED for the (ii) branch: the GIVEN's expansion
`lam = 1 - i mu.k - (1/2) k^T(Sigma + mu mu^T) k + ...` and a2's refereed ballistic constant;
the (i) branch is proved here outright. Also lost: order-independence of the level updates
(the two components must be updated together; a2 records the same for its coin), and the
static positive kernel -- a2's `(5/8) 3^{-|x|}` and `-|x|/2` are what the positive law's
Green function becomes.

## 3. Where this stops

No step of the route fails; the route is not exhausted either. Precisely what is *not*
settled here:

1. **`J >= 4` signed rules are not classified.** Step 4's ladder (4.2)-(4.3) holds at every
   `J`, and Step 3 pins the deepest level at every `J`, but the analogue of Step 5's
   deltoid -- the region in the remaining coefficients where *all* `J` roots are
   unimodular -- is computed here only for `J = 3`. For `J = 4` the free data is
   `(What_0, What_1)` with `What_2` fixed by (4.2), a real-algebraic region in `R^4`, and I
   do not have its description.
2. **Multi-component rules in `d >= 2` are not classified.** (9.1) is a constraint, not a
   classification: it says `det U` is a shift, not which `U` are unitary at every `k`.
   a2 does the `1+1` two-component case exactly and I do not repeat it; the `3+1`
   eight-component candidate a2 names is untouched here.
3. **(9d)(ii) leans on the GIVEN and on a2.** The rigid-transport half is proved here; the
   diffusive half quotes the refereed expansion rather than re-deriving the front.
4. Step 1 gives `|lam| <= 1` for the non-transport branches of the exceptional family but
   does not compute their decay rate; (8.1) bounds only the product, on average over `k`.

## 4. What would finish it

* **(a) is closed** as stated (one branch, nonnegative weights, finitely many levels), with
  the exception classified. The vector version (nonnegative *matrix* weights) is a5's
  subject, not re-done here.
* **`J = 4`:** the four roots of a lossless rule come in two conjugate pairs on the circle,
  so the map `(What_0, What_1) -> (cos th_1, cos th_2)` should make the region the image of
  a square under a fixed polynomial map, exactly as `J = 3` gave the deltoid; a Schur-Cohn
  determinant test on the self-inversive quartic would give the same region as explicit
  polynomial inequalities. Both are finite computations.
* **Multi-component in `d >= 2`:** with (9.1) in hand, write
  `U(k) = A + sum_j (B_j e^{-i k_j} + C_j e^{i k_j})` and impose unitarity at every `k`;
  this is a finite system of matrix equations in `A, B_j, C_j` (the paraunitary
  factorization), whose solutions can then be pushed through Step 7's computation to test
  whether the cone is round. The `d = 3`, `n = 8` candidate is the first case to run.
* **For the axiom question:** the sharp statement to aim at is the converse of (9d) --
  characterize which nonnegative record statistics *do* arise as `|psi|^2` of a unitary
  formation rule. Step 1 says the positive formation law cannot produce them directly; the
  open question is whether the amplitude layer is forced, or whether a positive law on a
  *larger* state (more components, more levels, hidden sites) can reproduce the same
  readout statistics. Step 1 is the obstruction any such construction must clear.
