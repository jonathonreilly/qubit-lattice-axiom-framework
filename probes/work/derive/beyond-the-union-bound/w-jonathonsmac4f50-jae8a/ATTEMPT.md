# beyond-the-union-bound, attempt 3 (worker w-jonathonsmac4f50-jae8a, model claude-opus-5)

Route taken: candidate (i) in a specific form. Block 30's construction outputs one canonical object per configuration:
its refinement history. The history is counted directly, instead of every tree allowed by block 30's budgets.
No prior attempt was on `ai/probes` when this one started.

## (1) The statement attempted

Objects are as in block 30 (PR #8174), whose definitions are used verbatim:
- the six-axis formation law in level time, started from the all-`a` plane, and its dissent indicator `ξ_x = 1{v_x ≠ a}`;
- the deviations `d_1, d_2, d_3`, with `ε₁ = d_1` and `ε₂ = max(d_2, d_3)`;
- the two-level automaton `η'`: i.i.d. uniforms `U_x`, `η' ≡ 0` on levels `≤ 0`. A site is `1` if it has at least two
  1-predecessors, with probability `ε₂` if it has exactly one, and with probability `ε₁` if it has none;
- seeds, amplified sites, amplification directions, winning pairs, `Excuse_k`, bad pairs, clusters, spanned sets and the
  functionals `M_k`.

For `σ ∈ (0, 1]` put

```
μ = σ (2 + ε₂/σ)³ ,      c = 6 ε₁ / σ .
```

**Statement.**
- (H1) If `Z̄ ≥ 1` satisfies `c Z̄ < 1` and `Z̄ ≥ 1 + μ Z̄ / (1 − c Z̄)³`, then `P(η'_x = 1) ≤ ε₁ Z̄` at every site `x`.
  With block 30's domination, the formation law from the all-`a` plane then has `P(v_x ≠ a) ≤ ε₁ Z̄` at every later site.
- (H2) Exact certificates:

  | line | `σ` | `Z̄` | threshold | `ε₁ Z̄` at the threshold | block 30 |
  |---|---|---|---|---|---|
  | `(p, 1, 2)` | `161/5000` | `5119922891/10⁹` | `p ≥ 84` | `2.85·10⁻⁴` | `p ≥ 4165` |
  | `(p, 1, 1)` | `313/10000` | `230312929/(5·10⁷)` | `p ≥ 44` | `2.70·10⁻⁴` | `2085` |
  | `(p, 2, 4)` | `161/5000` | `5119922891/10⁹` | `p ≥ 168` | `2.85·10⁻⁴` | `8330` |
  | `(p, 1, 3)` | `13/400` | `655476451/(1.25·10⁸)` | `p ≥ 125` | `2.93·10⁻⁴` | `6247` |

  These points lie beyond both ceilings of the tree route on `(p, 1, 2)`: `p > 4150` (budget `c = 2`, `ε₂ < 256/531441`)
  and `p > 367` (budget `c = 1`, `ε₂ < 4/729`).
- (H3) This route's own ceiling: every certificate needs `27 ε₂ < 1`. Letting `ε₁ → 0` on `(p, 1, 2)` gives `p ≥ 58`, and
  the located strength `p ∈ (10.5, 11)` is out of this route's reach.

## (2) Steps

**Step 1: the domination (ASSUMED: block 30, T1; CHECKED as A1, A2).** `ξ ≤ η'` under a coupling, with `ε₁ = d_1` and
`ε₂ = max(d_2, d_3)`. `check.py` verifies the following:
- the closed forms against the one-site conditional;
- `d_1 ≤ max(d_2, d_3)`;
- the coupling inequality at all 216 predecessor triples, at the four certificate points and at `(11, 1, 2)`.

A1 verifies that the three p-derivatives are negative expressions over squares, so all three deviations strictly decrease
in `p`.

**Step 2: the construction (ASSUMED: block 30, T2, whose proof uses block 25's spanning lemma T3, PR #8168; CHECKED as B1–B3
by executing block 30's own implementation).** Start from `𝒰 = {({x}; x, x, x)}`. While some unprocessed cluster
`(K; v_1, v_2, v_3)` at level `s` has a non-seed pole, refine it (then `K` has no seed, since a seed is a singleton
cluster). The facts used are these.
- (2a) *Terminals are moves.* `u_k := Excuse_k(v_k)` is a 1-predecessor of `v_k`, so `u_k = v_k − e_{d_k}` with
  `d_k ∈ {1, 2, 3}`. If `v_k` is processed, `u_k` is the winning-pair member with index `≠ k`, so `d_k ≠ k`. If `v_k` is
  amplified with direction `j`, then `d_k = j`, and `d_k = k` exactly when `(v_k, k)` is a bad pair.
- (2b) *Steiner tree and poles.* `𝒯` is a minimal subtree of the cluster–fork graph of `V_K` containing the clusters
  `C_k ∋ u_k`, as in block 25 T3. Every leaf of `𝒯` is some `C_k`, and a fork has degree two. The poles of a cluster
  `X ∈ 𝒯` are `u_{X,k} = u_k` if `X = C_k`; otherwise `u_{X,k}` is the meeting point of `X` with its neighbour on the path
  toward `C_k`. The clusters of `𝒯` enter `𝒰` with these poles, and its forks become edges.
- (2c) *Potential.* `Φ = Σ_𝒰 Span + #forks` starts at `0` and rises by at least `1 − b` per refinement, where `b` is that
  refinement's number of bad pairs. The procedure ends with every unprocessed cluster a seed singleton of span `0`.
- (2d) *Uniqueness and termination.* A cluster enters `𝒰` at most once. A point is a pole of at most one refined cluster
  and is bad for at most one charge. The procedure terminates, because levels descend and every 1-site at level `1` is a
  seed.

B1 and B2 cover all configurations of `η'` on the depth-2 cone (308) and the depth-3 cone (47952, of which 38752 have
`η'_x = 1`). B3 covers 1500 seeded random cones of depth 3–8. On all of them `check.py` asserts the following:
- 2a, including `d_k = k` exactly at the bad pairs;
- the pole rule 2b;
- block 30's asserted span identity at every refinement;
- the consequences in steps 3 and 4.

**Step 3: two counts of a history (PROVED; CHECKED as B1–B3).** Let `R` be the number of refinements, `F` the total number
of forks of all the `𝒯`, and `B` the total number of bad pairs.
- (3a) `|S| = F + 1`, where `S` is the set of seed singletons left at the end.
  *Argument.* A refinement replaces one cluster of `𝒰` by the `n_𝒯` clusters of `𝒯`. Since forks have degree two, `𝒯` is a
  tree on its clusters with its `f_𝒯 = n_𝒯 − 1` forks as edges. Starting from one cluster, the procedure ends with
  `1 + Σ (n_𝒯 − 1) = 1 + F` unprocessed clusters. All of them are seed singletons, and they are distinct by (2d).
- (3b) `R ≤ F + B`.
  *Argument.* By (2c), `Σ_refinements (1 − b) ≤ Φ_end − Φ_start = F − 0`.

**Step 4: the abstract history determines the seeds and the bad sites (PROVED; CHECKED as B1–B3).**
*Encoding.* A cluster is encoded as `seed` or as `(ref; d_1, d_2, d_3; tree)`. The `tree` is `𝒯` rooted at the cluster
holding charge `1`'s terminal and read recursively as `(cl; charges whose terminal lies here; the cluster's own encoding;
kids)`. Each kid records:
- the set of charges whose terminals lie beyond the fork;
- the fork's displacement `m(f, Y) − m(f, X)`, one of the six vectors `e_i − e_j`;
- the subtree beyond the fork.

This is the only data used below. No position appears in it.

*Argument.* The recursion has two passes.
- *Bottom-up.* For every encoded cluster, compute the offsets of its three poles from its charge-1 pole. A seed has all
  offsets `0`. For a refined cluster, place its tree in a local frame as follows.
  - Put the root cluster's charge-1 pole at the origin and its other poles by their offsets.
  - Cross each fork from `X` to `Y`: `m(f, X)` is `X`'s pole for any charge beyond `f` (this is rule 2b), and
    `m(f, Y) = m(f, X) + displacement`.
  - `m(f, Y)` is `Y`'s pole for any charge not beyond `f` (rule 2b again), and the other poles of `Y` follow from its
    offsets.
  - This places every terminal `u_k`, and `v_k = u_k + e_{d_k}` then gives the cluster's own offsets.
- *Top-down.* Start from `(x, x, x)`, set `u_k = v_k − e_{d_k}`, and place the children the same way.

The seeds are the placed seed clusters, and the bad sites are the poles `v_k` with `d_k = k`, by (2a).

B1–B3 rebuild them from the encoding alone and find them equal to the realized ones on every configuration. They are
distinct seed sites and amplified sites.

**Step 5: union bound over histories (PROVED; CHECKED as D1, D2).**
The construction is deterministic once its tie-breaks are fixed, so its history `h(ω)` is a function of the configuration
`ω`. For a history `h` realized at `x`, `{h(ω) = h}` lies inside the following event:
- `U_z < ε₁` at the seeds of `h`, since a seed is a 1-site without 1-predecessors;
- `U_z < ε₂` at the bad sites of `h`, since a bad pole is amplified.

These sites are determined by `h` (step 4) and are pairwise distinct (2d). So

```
P(η'_x = 1) ≤ Σ_{h realized at x} ε₁^{|S(h)|} ε₂^{B(h)} = Σ_h ε₁^{F+1} ε₂^{B} ≤ ε₁ Σ_h σ^R (ε₁/σ)^F (ε₂/σ)^B ,
```

where the last step uses `σ ≤ 1` and `R ≤ F + B` (3b).

D1 and D2 work on the complete depth-2 and depth-3 cones. They compare two exact computations of `P(η'_x = 1)` (the sum
over configurations, and an independent level-by-level DP), which agree. At three stress points and at two certificate
points, they check three things:
- the configurations mapped to each history weigh at most its `ε₁^{|S|} ε₂^B`;
- the union over histories is at least `P`;
- at the certificate points, the union is at most `ε₁ Z̄`.

On the depth-3 cone at `(84, 1, 2)`, `P = 6.026·10⁻⁵` and the union over realized histories is `6.028·10⁻⁵`.

**Step 6: the generating function of the grammar (PROVED; CHECKED as C1–C3).**
Let `𝔊` be the set of all encodings of step 4. Each has:
- arbitrary moves `d ∈ {1, 2, 3}³`, with a charge bad iff `d_k = k`;
- a minimal Steiner tree on the three labelled terminals, with any of the six displacements per fork;
- an independent encoding at every cluster.

Every realized history lies in `𝔊`, by (2a) and (2b) and because a minimal subtree with three terminals is a single cluster,
a path or a Y whose centre is a cluster. Put `W = Σ_{h∈𝔊} σ^R r^B φ^F`. Then, as formal power series,

```
W = 1 + σ (2 + r)³ · W / (1 − 6 φ W)³ .
```

*Argument.* A cluster is a seed (term `1`) or is refined (factor `σ`).
- *Moves.* The moves contribute `Σ_{d∈{1,2,3}³} r^{#{k: d_k = k}} = (2 + r)³`.
- *Arms.* An arm is a path of `j ≥ 1` forks and `j − 1` intermediate clusters. Summed over `j`, an arm gives
  `a = Σ_{j≥1} (6φ)^j W^{j−1} = 6φ/(1 − 6φW)`.
- *Shapes.* All terminals in one cluster give `W`. Two terminal clusters give `W² a`, in 3 ways. Three terminal clusters on
  a path with a terminal in the middle give `W³ a²`, in 3 ways. A Y with a non-terminal centre gives `W⁴ a³`. The sum is
  `W (1 + W a)³ = W / (1 − 6 φ W)³`.

C1 and C2 check this without using the recursion. They enumerate the grammar directly (1148689 histories up to `σ²φ²`, and
2186056 up to `σ³φ`) and find every coefficient equal to the series. C3 checks that the distinct realized histories of the
depth-2 and depth-3 cones never exceed the coefficients.

**Step 7: the super-solution bound (PROVED).** Let `W_h` be the sum over histories whose refinement tree has height at
most `h`. Then `W_0 = 1` and `W_{h+1} = 1 + μ W_h (1 − c W_h)^{−3}` whenever `c W_h < 1`, with `r = ε₂/σ` and `φ = ε₁/σ`,
so that `σ(2 + r)³ = μ` and `6φ = c`. The map `Z ↦ 1 + μ Z (1 − c Z)^{−3}` is increasing on `[0, 1/c)`. So `Z̄ ≥ W_0` and
`Z̄ ≥ 1 + μ Z̄ (1 − c Z̄)^{−3}` give `W_h ≤ Z̄` for every `h`, by induction. Every realized history is finite, so the sum over
all of them is `lim W_h ≤ Z̄`. Steps 5–7 give (H1).

**Step 8: the certificates (CHECKED as E1, E2).** The four rational pairs `(σ, Z̄)` of (H2) satisfy the conditions exactly.
Along each line `ε₁` and `ε₂` decrease in `p` (A1), so `μ` and `c` decrease, the right side decreases, and the same `Z̄`
serves every larger `p`. E2 checks that every certificate point has `ε₂ > 4/729 > 256/531441`, and that
`d_3(4150) > 256/531441` and `d_3(367) > 4/729` on `(p, 1, 2)`. These are the tree route's two ceilings.

**Step 9: this route's ceiling (PROVED; CHECKED as F1).**
`σ(2 + ε/σ)³ − 27 ε = (σ − ε)²(8σ + ε)/σ²`, so `μ ≥ 27 ε₂`, with equality at `σ = ε₂`. Any super-solution has
`Z̄ ≥ 1 + μ Z̄`, since `(1 − cZ̄)^{−3} ≥ 1`, and so `μ < 1`. So the route needs `ε₂ < 1/27`. That is `76.9` times the tree
route's `256/531441` at `c = 2`.

On `(p, 1, 2)`, `ε₂ = d_3` at `p = 57, 58`, and `d_3(57) = 125/3374 > 1/27 ≥ d_3(58) = 127/3491`. So even with `ε₁ = 0`
the route stops at `p = 58`. At the actual `ε₁` the fork factor `c` sets the certificate thresholds. Numerically (INFO F2,
not a claim), no fixed point exists one step below any certificate for `σ = i/10000`, `i = 50..399`.

## (3) Where the route stops

No step fails for (H1)–(H3). The route stops short of the problem's target, the located strength `p ∈ (10.5, 11)` on
`(p, 1, 2)`: there `ε₂ = d_2(11, 1, 2) = 43/164 ≈ 0.262`, which is far above this route's ceiling `1/27` (step 9).

## (4) What would finish it

1. **The domination.** `η'` charges every site with one dissenting predecessor the worst deviation `max(d_2, d_3)`. At
   `p = 11` that is `0.26`, where the two-level automaton itself may not order. Any count of `η'` is capped by that
   automaton's threshold. Reaching `11` needs a value-aware domination: which record dissents, antipodal or orthogonal,
   and the actual predecessor state.
2. **The free moves.** The history pays only for seeds and bad poles. A processed pole's move is counted as one of two free
   choices, although that pole needs a second 1-predecessor that is never charged. In a single-seed chain this is the whole
   gap between `27 ε₂` per level and the actual survival rate.
3. **The fork factor.** `c = 6ε₁/σ` sets the certificates (`84` against the ceiling `58` on `(p, 1, 2)`). A cheaper fork
   accounting would move the certificates toward the ceiling.
4. **Coincident poles.** When the three poles coincide, a refinement has `3 + 3r` move patterns, not `(2 + r)³`, and two
   coincident poles have `2(2 + r)²`. A recursion typed by pole configuration lowers `μ` near the root. It does not move the
   ceiling `1/27`, which comes from separated poles.

Imports: block 30's T1 and T2 and block 25's T3 are ASSUMED as stated in their notes, and executed in `check.py` through
block 30's own implementation, copied verbatim from its runner at commit `cc7662e1` with one recording line added.
Everything else in steps 3–9 is argued above in full, and every finite claim is checked with exact arithmetic.
