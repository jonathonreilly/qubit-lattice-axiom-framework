# causal-clauses, attempt 1 (worker w-macbookpro90c72-jc4f8, model claude-opus-5)

Plan, locked from the task: write the hypothesis "every predecessor is recorded
before its successor, and no record is re-formed" as a constraint on a formation
process on finite level-ordered windows of Z^3; prove that every rate, order and
antichain-unit rule obeying it gives one law `mu_D`; measure each clause
candidate of blocks 14, 15 and 24 against `mu_D` on the smallest windows; say
what the constraint decides about unrecorded sites; list what it leaves free.
All numbers are exact rationals from `check.py` (21 checks, tags below; values
at `(p, q, r) = (3, 1, 2)` unless three are given for `(3,1,2), (5,2,4), (2,1,2)`).

## (1) The statement attempted

**Setting.** Menu `M = {±e_1, ±e_2, ±e_3}`. Rule `phi(v, v') = p` if `v = v'`,
`q` if `v = -v'`, `r` otherwise (`p, q, r > 0`); `Z_1 = p + q + 4r = sum_b phi(u, b)`
for every `u`. Orientation `s in {±1}^3` (default `S0 = (1,1,1)`), parents
`pa(x) = {x - s_k e_k : k = 1, 2, 3}`, level `l(x) = s.x`. A window is a finite
`D` in Z^3 with the nearest-neighbour bonds inside `D`; `pa_D(x) = pa(x) ∩ D`.
Ancestors are taken in the DAG `(D, pa_D)`. Kernel `r(a | u_1..u_k) = prod_j phi(u_j, a) / N(u)`, `N(u) = sum_b prod_j phi(u_j, b)`
(uniform `1/6` for `k = 0`). Causal law `mu_D(v) = prod_{x in D} r(v_x | v_{pa_D(x)})`.
Static law `P_D(v) ∝ prod_{<xy> in D} phi(v_x, v_y)`.

A formation history is a sequence of disjoint nonempty units covering `D`. A
unit `U` forms jointly with law `∝ prod_{<xy> in U} phi · prod_{x in U, y recorded, x~y} phi(v_x, v_y)`
(one site: the rule's kernel given its recorded neighbours). The next unit is
chosen by any rule: random or deterministic, depending on the whole history
including recorded values; clocks with any rates are one such rule.

**Hypothesis H.** (H1, gating) every site's in-window parents lie in strictly
earlier units; (H2) every site lies in exactly one unit; (H3, non-stalling) at
every reachable history the choice rule is a probability distribution over the
available units.

**Theorem A (part (a)).** Under H the finished records have law `mu_D`, for every choice rule.

**Theorem B (part (b)).** The block 14, 15, 24 candidates that break H, each with its
smallest window and exact TV from `mu_D`: the list in Step 14.

**Theorem C (part (c)).** Under H, a site unrecorded when `W` (a subset of `D`) completes is not an
ancestor of `W`, and non-ancestors drop out exactly, so summing over an
unrecorded site and omitting it give the same law on `W`. Which recorded
ancestors belong to the window changes `W`'s law and is not decided by H.

**Part (d).** What H leaves free: the orientation (Step 19), the multi-parent
kernel (Step 20), the extent of the recorded past (Steps 17, 18), timing
statistics (Step 21); H itself is not derived (Step 2).

Candidates, quoted from the notes:
- Block 14 (PR #8148): (a) "records form at a rate that does not depend on the
  nearest-neighbour conditions"; (b) "records form at a rate determined by the
  nearest-neighbour conditions"; (c) no clause: "every rate-dependent statistic
  is registered data under the realized-state primitive".
- Block 15 (PR #8149): keep "for each site" (the site is the unit); "for each
  admissible set of sites" (a covariant set is the unit).
- Block 24 (PR #8158): (R1) "The static law of a configuration of records is
  normalized over the recorded sites alone; a site without a record contributes
  no factor." (R2) "Every site's admissible possibilities enter the static law;
  a record locks one of them, and the possibilities of a site without a record
  are summed."

## (2) Steps

**Step 1: level lemma (PROVED).** A bond joins `x` and `x + eps e_k`, so `l`
changes by `±1`. Same-level sites are never neighbours. Every bond joins a site
to one of its parents: if `eps s_k = -1` then `x + eps e_k = x - s_k e_k` is in `pa(x)`,
otherwise `x` is in `pa(x + eps e_k)`. Z^3 has no triangle: a common neighbour of
two sites at levels `l`, `l+1` would have level in `{l-1, l+1} ∩ {l, l+2}`, which is empty.

**Step 2: the transcription (ASSUMED).** H as a constraint on the process
(the choice rule never offers a site whose in-window parents are unrecorded);
the window is the whole system (parents outside `D` are absent, roots uniform);
orientation `S0`; the unit formation law above; a covariant clock's rate is a
function of the recorded configuration seen from the site (not of the window's
shape); the reading of each quoted sentence as a process in Step 14.

**Step 3: down-set lemma (PROVED).** Under H1, after every step the recorded set
`S` satisfies `x in S => pa_D(x) ⊂ S`, by induction over units. So every ancestor
in `D` of a recorded site is recorded.

**Step 4: a ready site's recorded neighbours are its parents (PROVED; asserted in
every gated run of A1).** Let `S` be a down-set and `x` not in `S` with `pa_D(x) ⊂ S`.
A recorded neighbour `y` is a parent or a child of `x` (Step 1); a recorded child
would put `x` in `pa_D(y) ⊂ S`. So `x` forms from `r(. | v_{pa_D(x)})`.

**Step 5: antichain units factor (PROVED).** Two ready sites are not neighbours:
otherwise one is the other's parent (Step 1) and readiness would have it
recorded. So a unit of ready sites has no inner bond and, by Step 4, law
`prod_{x in U} prod_{y in pa_D(x)} phi(v_y, a_x) / prod_{x in U} N(v_{pa_D(x)}) = prod_{x in U} r(a_x | v_{pa_D(x)})`.
Under H1 every site of a unit is ready when the unit forms; ready sites are
pairwise incomparable (their proper ancestors are recorded, Step 3), so H1's
units are exactly the sets of ready sites, all antichains.

**Step 6: frozen-order identity, Theorem A (PROVED; CHECKED as A1, A2).** By Steps
4 and 5 a history `h = (U_1..U_m)` ending in `v` has probability
`prod_t c(U_t | h_{<t}) · prod_{x in D} r(v_x | v_{pa_D(x)})`, where `c` is the choice
probability given the history so far (values included). The kernel product does
not depend on the unit sequence, so `P(v) = mu_D(v) f(empty)`, where `f(h)` sums
`prod c` over the gated completions of `h` with values read from `v`. `f = 1` on
complete histories, and otherwise `f(h) = sum_U c(U | h) f(hU) = sum_U c(U | h) = 1`
by induction on the number of unrecorded sites and H3. So `P = mu_D`. A1: 8
windows (collider, plaquette, T4, T5, cross, plaquette plus a site above a corner, 2x3 slab,
plaquette under `s = (-1,1,1)`) x 6 clock laws (uniform, attracting, parallel
growth, `eps = 1/10`, arbitrary site-, set- and value-dependent rates, a random
rotation-covariant law) x 3 rules: 144/144 exactly `mu_D`. A2: random and
deterministic history- and value-dependent orders, single sites and antichain
units, 3 windows x 3 rules: 72/72.

**Step 7: conditioning instead of gating (PROVED; CHECKED as A3).** Block 14's
clocks run on every unrecorded site. Conditioned on the realized order being
causal, `P(v) ∝ mu_D(v) · sum_{causal sigma} prod_t lambda_{sigma_t}(h) / Lambda(h)`,
where `Lambda` sums the rates of all unrecorded sites, ready or not (Step 4 gives
the kernel product on causal orders). If the rates do not read recorded values,
the sum does not depend on `v` and the law is `mu_D` (A3: uniform, seeded,
attracting, `eps` laws on the 15 three-site windows, plaquette, T4, 3 rules,
whenever a causal order has positive probability). If they do, the sum can
depend on `v`: parallel growth on the bent chain `{(0,0,0), (1,0,0), (1,1,0)}` gives
TV `5/114`; parallel growth on a bonded pair gives 0.

**Step 8: block 14's clocks on the collider (PROVED; CHECKED as B0, B1, B2).**
Collider `{a, m, c} = {m - e_1, m, m - e_2}`, `pa_D(m) = {a, c}`, `a`, `c` not adjacent.
`mu_D = C`, `C(v) = phi(v_a,v_m) phi(v_c,v_m) / (36 Z_2(v_a,v_c))`,
`Z_2(u,w) = sum_b phi(u,b) phi(w,b)`. The static law is a tree law:
`P(v) = phi(v_a,v_m) phi(v_c,v_m) / (6 Z_1^2)`, equal to the chain product
`(1/6) r(v_m|v_a) r(v_c|v_m)` and the fork product `(1/6) r(v_a|v_m) r(v_c|v_m)`.
Under a translation-covariant clock law (Step 2), all rates are equal while
nothing is recorded, so the first site is uniform. `m` first: fork product, `P`.
`a` first with value `v_a`: `m` next (probability `1 - lambda(v_a)`) gives the chain
product `P`; `c` next (`lambda(v_a)`) forms uniformly (no recorded neighbour), then
`m` from both: `C`. `c` first: the same with `lambda'(v_c)`. So the law is
`(1 - w) P + w C`, `w = (lambda(v_a) + lambda'(v_c)) / 3` in `[0, 2/3]`, i.e.
`law - C = g (P - C)` with `g = 1 - w` in `[1/3, 1]` a function of `(v_a, v_c)`, and
`TV(law, mu_D) = (1/2) sum_v g |P - C|` lies in `[t/3, t]`, `t = TV(P, C) = 1/72, 29/3174, 5/726`
(B0). Uniform rates: `g = 2/3`, `1/108`. Seeded: `g = 1`, `1/72`, and no causal order
ever occurs. `eps` rates approach `t/3` (`eps = 1/100`: `103/303 · t`). On the
straight, bent and fork windows `mu_D = P`, and an order gives `C` if `m` is last
and `P` otherwise (Step 10), so the law is `P + w (C - P)` with `w(v)` the
probability that `m` is last (the sum of the orders' choice products, Step 13);
`m` is first with probability `1/3`, so `w <= 2/3` and `TV <= 2t/3`. B2: 12
covariant laws x 15 windows x 3 rules within these bounds.

**Step 9: two-site windows (PROVED; CHECKED as B3).** A bonded pair is a tree:
every order gives `(1/6) r(v_2 | v_1) = P = mu_D`. An unbonded pair forms uniformly
and independently. B3: all 24 two-site windows (`0 < |d|_1 <= 2`) x 7 laws TV 0
(seeded stalls on the 18 unbonded ones); a bond with one far site, TV 0.

**Step 10: block 15's unit sequences on three sites (PROVED; CHECKED as B4).** A
connected three-site window is `{a, m, c}` with `m` adjacent to both ends and the
ends not adjacent. Its 13 ordered partitions give:
- `m` alone after both ends (3 sequences): the ends form uniformly (as a unit:
  no inner bond, no recorded neighbour), then `m` from both: `C`;
- `m` alone first (3): fork product, `P`; `m` alone second (2): chain product, `P`;
- `m` with one end (4): `{a, m}` first has law `phi(v_a,v_m) / (6 Z_1)`, then `c` from `m`:
  `P`; `c` first, then `{a, m}` with bonds `a-m` and `m-c`: `(1/6) phi phi / Z_1^2 = P`;
- the whole window (1): `P`.
`mu_D` is `C` on the collider and `P` on the straight chain, bent chain and fork,
and `P`, `C` have the same formulas on every three-site window (`phi` reads values
only). So `TV(law, mu_D) = t` iff [`m` alone last] xor [collider], else 0. The
law moves under 3 of 13 sequences on straight, bent and fork windows and under 10
of 13 on the collider; the causal sequences (1, 3, 3, 1 on straight, fork,
collider, bent) never move it.
B4: 585 cases; two-site windows 0.

**Step 11: a whole window as one unit (PROVED; CHECKED as B5).** Its law is
`∝ prod_bonds phi = P_D`. Plaquette: the level sets as units give `mu_D` (Theorem A);
the whole plaquette as one unit gives TV `455/31176`.

**Step 12: re-formation fixes the static law (PROVED; CHECKED as B6).** Let `K_i`
re-form site `i` from all its window neighbours:
`K_i(v -> v') = [v'_{-i} = v_{-i}] k_i(v'_i | v_{N(i)})`, `k_i(a | u) ∝ prod_{j in N(i)} phi(u_j, a)`.
`k_i` is `P`'s conditional at `i`, so `P K_i = P`. Conversely, let `nu K_i = nu` for
every `i`. Then `nu(v) = nu_{-i}(v_{-i}) k_i(v_i | v_{N(i)})`; since `k_i > 0`, positivity
survives single-site changes, so `nu > 0` everywhere with conditionals `k_i`. For
`z^j = (v_1..v_j, w_{j+1}..w_n)`, `nu(z^j) / nu(z^{j-1}) = k_j(v_j | .) / k_j(w_j | .)`, and the
product over `j` fixes `nu(v)/nu(w)`, so `nu = P`. As `mu_D ≠ P` on the collider and
plaquette, some `K_i` moves `mu_D` (B6, 3 rules). On the collider, re-forming `a` then
`c` (each from `m`, their child) sends `mu_D` to `mu_D(v_m) r(v_a|v_m) r(v_c|v_m) = P`:
`mu_D(v_m) = 1/6` because the signed axis permutations act transitively on `M` and
preserve `phi` and `Z_2`, hence `C`.

**Step 13: covariant partitions are single sites (PROVED).** Let a partition of
Z^3 into finite units be carried to itself by every translation. If `x ≠ y` lie in
one unit `U`, the unit `U + (y - x)` contains `y`, so equals `U`; but a finite
nonempty set is carried to itself by no nonzero translation (`U + d = U` iff
`U - d = U`; translate its lexicographically largest point by whichever of `d`,
`-d` is lexicographically positive). So its units are single sites. A family of `k`-site units (`k >= 2`) closed under
translations puts each site in at least `k` distinct members (`U + x - y`, `y` in `U`),
so forming them all re-forms records (H2 fails), and a fixed sub-family that
partitions Z^3 is not covariant. A random unit sequence chosen by any
non-stalling rule, gated or not, gives `P(v) = sum_sigma c_sigma(v) law_sigma(v)`, where
`c_sigma(v)` is the product of the choice probabilities along `sigma` with values
read from `v`, `law_sigma` the product of the unit laws, and `sum_sigma c_sigma(v) = 1`
for every `v` (Step 6's induction). On three sites each `law_sigma` is `P` or `C`
(Step 10), so the law is `C + g (P - C)` with `0 <= g(v) <= 1` and TV `<= t`.

**Step 14: the list for (b) (from Steps 7 to 13; the readings are part of Step 2).**
Every candidate needs three sites: two-site windows never move (Step 9).
- 14 (a): the clocks run on unready sites (H1 fails with probability 5/6 on straight
  and bent windows, 2/3 on fork and collider); TV `1/216` (straight, fork, bent),
  `1/108` (collider); `t/3` (straight, fork, bent) and `2t/3` (collider) at every rule.
- 14 (b), covariant rates without an orientation: collider TV in `[1/216, 1/72]` for
  every such law; seeded `1/72`, attracting `7/648`, parallel `37/3888`, `eps = 1/10`
  `13/2376`; other windows seeded 0, attracting `1/324`, parallel `17/3888`, `eps`
  `5/594` (B1). Once an orientation is given (and the window is the system), the
  gate (rate 1 when every in-window parent is recorded, else 0) reads only which
  nearest neighbours are recorded, and gives `mu_D` (Theorem A).
- 14 (c): no clause leaves the order unconstrained; a registered non-causal order
  moves the collider by `t = 1/72` (Step 10). Under H the rates move no finished law
  (Theorem A), only timing statistics (Step 21).
- 15, "for each site": an order moves the law iff [`m` last] xor [collider], by
  `t = 1/72`; causal orders never do.
- 15, "for each admissible set of sites": a unit with a comparable pair forms a
  successor no later than its predecessor (H1 fails); on three sites it moves the
  law by `t` iff [`m` alone last] xor [collider] (Step 10): collider `{a, m}` then
  `c`, `1/72`; chain `{a, c}` then `m`, `1/72`; chain `{a, m}` then `c`, 0; the whole
  collider `1/72`; the whole plaquette `455/31176` (Step 11). All translates of a
  unit re-form records, and a fixed partition is not covariant (Step 13).
  Antichain units of ready sites obey H and give `mu_D` (Step 5); an antichain
  formed before its parents does not: fork `{a, c}` then `m`, `1/72`.
- 24 (R1): a static-law reading; a recorded collider has law `P`, `1/72` from `mu_D`.
  No process obeying H gives `P` there (Theorem A); `P` is the law that re-forming
  sites from all their neighbours fixes (Step 12).
- 24 (R2): the same, and in addition an unrecorded common child of two recorded
  sites moves their law by `1/72`, where the causal law gives 0 (Step 16).

**Step 15: non-ancestor lemma, Theorem C (PROVED; CHECKED as C1, C3, C4, C5).** If
`E = D \ W` contains no ancestor of `W`, then `pa_D(x) ⊂ W` for `x` in `W` and the marginal
of `mu_D` on `W` is `mu_W`. Proof: a site `y` of `E` with no child in `E` has no child in `W`
either (it would be an ancestor), so `v_y` enters only its own kernel, which sums
to 1; remove `y` and repeat. Parents of ancestors are ancestors, so the
non-ancestors are closed under children and drop out together. By Step 3, under
H every site unrecorded when `W` completes is a non-ancestor of `W`. C1: 246 pairs
(`W` two sites with `0 < |d|_1 <= 2`, `E` one adjacent site): the causal TV is nonzero
only when `E` is an ancestor. Future exteriors give 0 in C3, C4, C5.

**Step 16: the static and causal criteria cross (CHECKED as C1).** Common child of
two unbonded sites: static TV `1/72` (it touches two recorded sites), causal 0.
Second parent of `W`'s child, `W` a bond: static 0 (pendant), causal `5/1716`,
`2435/1976436`, `1/2772`. Under H the second case cannot be unrecorded when `W`
completes: it is an ancestor.

**Step 17: the recorded past (PROVED for the two exceptions; CHECKED as C1 to C5).**
Root parent: if `e` has no parent in `W` and its only child in the window is a
root `x` of `W`,
`sum_{v_e} (1/6) r(v_x | v_e) = Z_1 / (6 Z_1) = 1/6` and `W`'s law is unchanged (C1 row
"parent of W's root", C5's 3 root parents). Diamond: `W = {o, x}`, `x = o + e_1`, second
parent `b = x - e_2`, common parent `c = o - e_2 = b - e_1`:
`sum_{v_c} (1/6) r(v_o|v_c) r(v_b|v_c) = Z_2(v_o, v_b) / (6 Z_1^2)` cancels the normalization
of `r(v_x | v_o, v_b)`, and summing `v_b` leaves `(1/6) r(v_x | v_o) = mu_W` (C2: TV 0 at the three
rules, while `b` alone gives `5/1716`; the same cancellation makes the past edge
drop out in C3 when `s_2 = +1`). In the other checked cases recorded ancestors
outside `W` move `W`'s law: plaquette with the edge above `c0, c1` in its past (`s = (±1, -1, -1)`)
`595909/132509520`; cube with the top face in its past `356696849/806187919680`; the
sink's third parent `437/102960` (enumeration and variable elimination agree).

**Step 18: a coupling bound on the extent of the past (PROVED given D4's values; CHECKED
as D4).** Let `alpha_3` be the largest TV between two three-parent kernels differing
in one parent: `27/110, 10650/63407, 1/9` (D4). Cut the past of a finite `W` at level
`-L` (all ancestors of level `>= -L`; each non-root has three parents there). Couple
the cuts at `L` and `L' > L` level by level, each site's two kernels maximally (mass
`min(rho, rho')` on the diagonal), independently within a level. Changing one parent
at a time, `TV(r(.|u), r(.|u')) <= alpha_3 · #{j : u_j ≠ u'_j}`, so `P(x differs) <= (3 alpha_3)^{l(x)+L}`.
With `3 alpha_3 = 81/110, 31950/63407, 1/3 < 1`, `W`'s law converges as `L -> infinity`. At
`(40, 1, 1)`, `3 alpha_3 = 390/137` and this bound gives nothing.

**Step 19: orientation (CHECKED as D1).** The 24 proper rotations act transitively
on the 8 orientations (stabilizer of `S0` of order 3); one of them sends `S0` to `-S0`.
`{m - e_1, m, m - e_2}` is a collider under `S0` and a fork under `-S0`: TV `1/72`.

**Step 20: the multi-parent kernel (PROVED and CHECKED as D2; CHECKED as D3).** By
Step 1 every bond is a parent-child pair, so `mu_D = prod_bonds phi / prod_x N(v_{pa_D(x)})`;
`mu_D = P_D` whenever every site has at most one in-window parent (chains, forks).
The product kernel is one covariant two-parent kernel with the rule's one-parent
kernel; the mixture `(phi(u,a) + phi(w,a)) / (2 Z_1)` is another. On the collider they
differ by `841/10296, 35731/494109, 47/693` (D3).

**Step 21: timing statistics (CHECKED as D5).** On the plaquette, gated uniform clocks
and gated parallel growth both give `mu_D`, while
`P(second site = (1,0,0), v_(0,0,0) = +e_1) = 1/12` and `1/9`.

**Step 22: block 24's Q4(a) witness is not a Z^3 window (CHECKED as E1).** Block 24
declares "the nearest-neighbour graph of `Z³` restricted to `W ∪ E`" (line 81) and
states "(a) `W` a plaquette, `E` one site adjacent to two adjacent corners:
`78621/4563820` at `(3, 1, 2)`, `675203620/64463986907` at `(5, 2, 4)`,
`221667/30063356` at `(2, 1, 2)`" (line 125; the same value in lines 39-41). By Step 1
two adjacent sites have no common neighbour. E1 reproduces the three values
exactly on the abstract graph "4-cycle plus a vertex joined to two adjacent
cycle vertices". In Z^3 each of the 16 one-site exteriors of a plaquette touches
one corner and gives TV 0 (the note's own pendant case). A Z^3 exterior touching
two corners of the same plaquette, the edge above `c0, c1`, gives `78621/27062500`,
`5414568900/4422807263221`, `490620/1322243321`. The cube value `9778807/1312253264`
(Q4(b)) is reproduced (C4).

## (3) Where the route stops

First failing step: Step 2 (the transcription, ASSUMED). Theorem A reads H as
gating, a constraint on the process. If H is instead imposed by conditioning
block 14's clocks on a causal realized order (Step 7), the law is `mu_D` for
rates that do not read recorded values, and parallel growth on the bent chain
moves it by `5/114`.

For (c) the route stops at Step 17. H decides unrecorded sites (they drop out),
but not which recorded ancestors belong to the window. The truncated pasts
differ (edge, cube, third-parent values), and Step 18 gives a limit only where
`3 alpha_3 < 1`.

## (4) What would finish it

- Derive H1 and H2 from the axiom sentences, or record them as a clause candidate:
  nothing here derives them, and block 14's clocks do not impose them.
- Fix the orientation (Step 19: the rule's rotations do not).
- Fix the multi-parent kernel (Step 20).
- Fix the extent of the past: the finite window of Step 2 or the infinite-past
  limit (Step 18). This includes a uniqueness proof or a counterexample where
  `3 alpha_3 >= 1`.
- Say whether timing statistics are registered data or set by a rate clause;
  under H they do not reach the finished law (Steps 6, 21).
- Block 24's Q4(a) needs a Z^3 exterior touching two corners (Step 22).

Imports: none beyond finite probability. The telescoping identity (Step 12) and
the maximal coupling (Step 18) are proved in place.
