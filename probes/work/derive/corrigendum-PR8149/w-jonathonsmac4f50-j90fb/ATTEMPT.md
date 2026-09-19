# Corrigendum packet for PR #8149 (block 15, the formation-unit clause witness) — attempt a2

Worker `w-jonathonsmac4f50-j90fb` (model claude-opus-5). Check script: `check.py` in this directory (exact rational,
integer and symbolic arithmetic; about 100 s). Sources read in full: the block 15 note and runner on
`origin/physics-loop/admissibility-induced-law-block15-formation-unit-clause-witness-20260915`, its runner cache, the
finder's and the confirmer's logs (`logs/probes/J:attack:PR8149/…2aaed46b…json`,
`logs/probes/J:confirm:J-attack-PR8149/…648b60c0…json`, issue #8255), and every file changed by PRs #8146–#8158,
#8168, #8170–#8180 (searched for block 15, #8149, the unit/joint vocabulary and U2/U4).

## 0. The defect, located

Block 15's U2 (note lines 142–177) claims, for every non-constant rule, unit, environment and order,
`μ_σ = μ^{joint}` **iff** no site records an inside neighbour together with a second recorded neighbour. U4
(lines 196–207) claims that in a full environment every connected unit with at least two sites differs from its joint
law under every order. The "only if" proof (lines 162–173) compares two values at one inside site `y` in "the
pattern in which every value in every `A_{w'}` with `y ∈ A_{w'}` equals `b`". When some `A_{w'}` contains recorded
**outside** sites, their values are fixed by the environment and cannot be set to `b`; the step is valid only when
those values are absent (isolated unit) or all equal (constant environment). U4's proof (lines 201–204) ends with
"U2 applies" and fails with it. The block's refuting pass re-read this step and accepted it
(`CHECKER_block15_findings.md`, line 14: "one consistent pattern"); the note's own N1 route 1 ("a cancellation among
normalizers … no compensation — RULED OUT AT SCOPE", line 234) is exactly the mechanism of the counterexample in S8.

## 1. The statements attempted

**Setting** (block 15's, with the environment allowed on any subset). Six-axis menu `M` (six values, the runner's
order `+x, −x, +y, −y, +z, −z`); rule `p, q, r > 0`, not all equal; `φ(a,b) = p, q, r` for equal, opposite and
orthogonal values; `K(b,a) = φ(a,b)/Z_1`, `Z_1 = p + q + 4r` (symmetric in its arguments);
`K_k(v_A) = Σ_s Π_{y∈A} K(v_y, s)`, `K_1 ≡ 1`. A unit `U ⊂ Z³` is finite, `O = N(U) ∖ U`, and the records sit on a
subset `O' ⊆ O` with values `v_{O'}` (`O' = O`: full environment; `O' = ∅`: isolated unit; block 15 uses these two,
its runner's code accepts any subset). For an order `σ` of `U`: `A_x` = the recorded outside neighbours of `x` and the
inside neighbours formed before `x`; `I_x = A_x ∩ U`, `E_x = A_x ∩ O'`;
`μ_σ(v_U) = Π_x r(v_x | v_{A_x})` with `r(a | ∅) = 1/6`, `r(a | A) = Π_{y∈A} K(v_y, a)/K_{|A|}(v_A)`;
`μ^{joint}(v_U) ∝ Π_{e ∈ E} φ(v_e)`, `E` = the edges inside `U` and from `U` to `O'` (block 15's U1; the runner's
`joint_law`). For `x` with `E_x ≠ ∅` put `H_x(s) = Π_{o∈E_x} K(v_o, s)` and `(K H_x)(a) = Σ_s K(a,s) H_x(s)`
(`= K_{1+|E_x|}(a, v_{E_x})`). For `y ∈ U`: `W_y = {x ∈ U : I_x = {y}, E_x ≠ ∅}` (its *dependents*) and
`Φ_y(a) = Π_{x∈W_y} (K H_x)(a)` (empty product `1`).

**U2′ (the corrected U2).** For every such rule, unit, recorded environment and order:

- (a) `μ_σ = μ^{joint}` iff `N_σ(v_U) := Π_{x∈U, A_x≠∅} K_{|A_x|}(v_{A_x})` does not depend on `v_U`;
- (b) if some site records two or more inside neighbours (`|I_x| ≥ 2`), then `μ_σ ≠ μ^{joint}`;
- (c) if every site records at most one inside neighbour, then `μ_σ = μ^{joint}` iff every `Φ_y` is constant on `M`.

Block 15's criterion is "(c)'s hypothesis and every `W_y = ∅`". Hence it is **sufficient in every environment**, and
it is **also necessary** — block 15's iff holds — (d) for isolated units and (e) for constant environments (all
recorded outside values equal). It is **not necessary in general** (S8, S11).

**U4′ (the corrected U4).** Let `U` be connected with `|U| ≥ 2` and `O' = O`. Then `μ_σ = μ^{joint}` iff `U` induces
a tree in `Z³`, `σ` is a growth order of it (every site after the first has an earlier neighbour), and every `Φ_y` is
constant. So U4 as stated holds for every unit containing a cycle (every order), for every non-growth order, and in
every constant environment. It fails for the star.

**Counterexamples to block 15's U2 "only if" and to U4.** (f1) The star (a site and its six neighbours), centre
first, in each of the 216 full environments equivariant under `g = −ρ` (called σ in the finder's log), for **every**
non-constant rule (S8). (f2) At `(3,1,2)`: the domino formed left then right, the right site's two recorded outside
neighbours carrying `+y` and `−y`, the rest unrecorded (a partial environment; S11). (f3) At `(4,1,2)`
(`pq = r²`): the straight path of three, middle first, full environment, the two end sites seeing
`{+x,+x,−x,+y,+z}` and `{+x,−x,−x,−y,−z}` (S11).

**The executed rule, full environments** (S11; value multisets, so every environment is covered). At `(3,1,2)` the
domino, both paths of three, the straight path of four and both three-leaf claws differ from their joint laws under
every order. The star differs under every order except centre first. Centre first agrees in the 216 environments of
(f1).

## 2. Steps

**S1 (PROVED) Edge accounting.** If `A_x ≠ ∅`, `r(v_x | v_{A_x}) = Π_{y∈A_x} K(v_y, v_x)/K_{|A_x|}(v_{A_x})`; if
`A_x = ∅` it is `1/6`. An edge `{x, y}` inside `U` contributes `K` exactly once, at its later endpoint (`y ∈ A_x` iff
`y` is formed before `x`). `K` is symmetric. An edge `{x, o}`, `o ∈ O'`, contributes once, at `x`. Edges to unrecorded
sites contribute nothing. Hence
`μ_σ(v_U) = 6^{−n_0} Z_1^{−|E|} w(v_U)/N_σ(v_U)`, where `n_0 = #{x : A_x = ∅}` and `w = Π_{e∈E} φ(v_e)`.

**S2 (PROVED; block 15's U1, unaffected).** `μ^{joint} = w/Z_U`. Its one-site conditionals are the rule given the
recorded neighbours (the factors without `v_x` cancel). Uniqueness is U1's telescoping-ratio argument, which is correct
as written.

**S3 (PROVED) U2′(a).** By S1–S2, `μ_σ/μ^{joint} = 6^{−n_0} Z_1^{−|E|} Z_U / N_σ(v_U)`. If `N_σ` is constant the
laws are proportional, hence equal. If they are equal the ratio is `1`, so `N_σ` is constant. *CHECKED* (C1): exact
equality of the two laws on every pattern against the constancy of `N_σ`, computed independently, in 2331 cases —
eight units, seven environments (isolated, two constant, two random full, two random partial), every order, rules
`(3,1,2)`, `(5,1,2)`, `(2,2,1)`. No mismatches.

**S4 (PROVED) Strict minor.** For `h : M → (0,∞)` put `G_h(α,β) = Σ_s K(α,s) K(β,s) h(s)` (symmetric, positive).
For orthogonal values `a ⊥ c`, Lagrange's identity for the inner product `⟨u, w⟩ = Σ_s h(s) u(s) w(s)` gives
`G_h(a,a) G_h(c,c) − G_h(a,c)² = ½ Σ_{s,t} h(s) h(t) (K(a,s)K(c,t) − K(a,t)K(c,s))²`. The bracket at `(s,t) = (a,c)`
is `(p² − r²)/Z_1²`, and at `(s,t) = (a,−a)` it is `r(p − q)/Z_1²`. So the minor is `> 0` unless `p = r` and `p = q`.
*CHECKED* (C-sym): the identity and both brackets symbolically in `p, q, r, h_1..h_6`.

**S5 (PROVED) U2′(b).** Let `y ≠ z` be in `I_x`. Fix every inside value except `α = v_y`, `β = v_z`. Sort the factors
`K_{|A_w|}(v_{A_w})` of `N_σ`:

- those with neither `y` nor `z` in `A_w` (constant here);
- those with `y` only (a positive `f(α)`);
- those with `z` only (a positive `g(β)`);
- those with both, `w ∈ B` (`x ∈ B`). For these, `K_{|A_w|}(v_{A_w}) = G_{h_w}(α, β)` with
  `h_w(s) = Π_{u∈A_w∖{y,z}} K(v_u, s) > 0`.

So `N_σ = C f(α) g(β) Π_{w∈B} G_{h_w}(α,β)`. If `N_σ` were constant, `Π_B G(α,β)` would be a function of `α` times a
function of `β`. Then `Π_B G(a,a) · Π_B G(c,c) = Π_B G(a,c) · Π_B G(c,a)` for `a ⊥ c`. By S4 and symmetry the left
side is strictly larger, a contradiction; by S3 the laws differ. No property of `Z³` enters, and `B` may be of any
size. *CHECKED* (C5): all 1428 executed cases violating (c)'s hypothesis differ.

**S6 (PROVED) U2′(c).** If every `|I_x| ≤ 1`, each factor of `N_σ` is one of three kinds:

- a function of `v_{O'}` alone (`I_x = ∅`);
- `K_1 ≡ 1` (`I_x = {y}`, `E_x = ∅`; indeed `Σ_s K(b,s) = 1`);
- `(K H_x)(v_y)` (`I_x = {y}`, `E_x ≠ ∅`).

So `N_σ = C Π_{y∈U} Φ_y(v_y)`, a product of positive one-variable functions. It is constant iff each `Φ_y` is
(change one `v_y` at a time). *CHECKED* (C3): 0 mismatches in the 2331 cases.

**S7 (PROVED) U2′(d), (e) and sufficiency.** Block 15's criterion is equivalent to "every `|I_x| ≤ 1` and every
`W_y = ∅`" (a violation is `I_x ≠ ∅` with `|A_x| ≥ 2`: either `|I_x| ≥ 2`, or `I_x = {y}` with `E_x ≠ ∅`).

- *Sufficiency:* every `Φ_y` is an empty product, so (c) applies.
- *(d)* If `O' = ∅` every `W_y = ∅`, so a violation has `|I_x| ≥ 2` and (b) applies.
- *(e)* Let every recorded outside value be `b`. If the criterion fails, either (b) applies or some `W_y ≠ ∅`. In the
  latter case `Φ_y(a) = Π_{x∈W_y} K_{1+m_x}(a, b, …, b)` with `m_x ≥ 1`. Block 15's lemma in its orthogonal form
  (`K_k(b,…,b) − K_k(c,b,…,b) = [(p−r)(p^{k−1}−r^{k−1}) + (q−r)(q^{k−1}−r^{k−1})]/Z_1^k > 0` for `c ⊥ b`, `k ≥ 2`,
  unless `p = q = r`; the lemma is correct) makes every factor larger at `a = b` than at `a = c`. So `Φ_y` is not
  constant and the laws differ by (c).

*CHECKED* (D-suff, D-nec): in every executed environment the criterion implies equality. In the isolated and constant
environments, equality holds iff the criterion does. Among the random partial environments at `(3,1,2)` the check
also met 6 cases where the laws agree although the criterion is violated (the corner claw). These are more failures of
the original "only if", and U2′ accounts for all of them.

**S8 (PROVED) The counterexample family (f1).** Let `ρ(x,y,z) = (z,x,y)` and `g = −ρ` (a linear lattice symmetry
fixing `0`).

- *Action on the values.* `g` acts on the six values as the six-cycle `+x → −y → +z → −x → +y → −z → +x` and
  preserves equal/opposite/orthogonal, so `K(g b, g a) = K(b, a)`.
- *Action on the sites.* `g` maps the star to itself and acts freely on its 18 outside sites (the six `2e` and the
  twelve `e + f`, `e ⊥ f`). `g³ = −I` fixes only `0`. `g², g⁴` are the rotations about `(1,1,1)`, whose lattice fixed
  points are multiples of `(1,1,1)`, and no outside site is one. `g, g⁵` have no fixed point but `0` because `ρ` has no
  eigenvalue `−1`. So there are 3 orbits of 6 sites.
- *The 216 environments.* An environment with `v_{g o} = g v_o` is fixed by 3 free values: 216 environments.

Order the centre first. The centre has no outside neighbour, so `A_centre = ∅`. Each leaf `e` records the centre and
its five outside neighbours `O_e`: `I_e = {centre}`, `|A_e| = 6`. The criterion is violated at every leaf, (c)'s
hypothesis holds, and `W_centre` = the six leaves (leaves have no later neighbours). Now
`(K H_e)(g a) = Σ_t K(a,t) H_e(g t)`, and `H_e(g t) = Π_{o∈O_e} K(g^{−1} v_o, t) = Π_{o∈O_e} K(v_{g^{−1} o}, t) = H_{g^{−1} e}(t)`
because `g^{−1}` maps `O_e` onto `O_{g^{−1} e}`. So `Φ_centre(g a) = Φ_centre(a)`. Since `g` is transitive on the six
values, `Φ_centre` is constant, and by (c) `μ_σ = μ^{joint}` for every non-constant rule.

*CHECKED*:

- S0: the six-cycle, relation preservation, the free action, and the count 216.
- S1: `Φ_centre` is constant in 216/216 environments at eight rules: `(3,1,2)`, `(5,1,2)`, `(7,2,3)`, `(2,2,1)`,
  `(4,1,2)`, `(1,3,2)`, `(2,1,1)`, `(1,1,2)`.
- S2: the two full laws agree on all `6⁷ = 279936` patterns in one environment at `(3,1,2)` and one at `(5,1,2)`.
- S3: in the same environment the leaves-first order still differs (the centre records six inside neighbours).

**S9 (PROVED) U4′.** Take `U` connected, `|U| ≥ 2`, `O' = O`. Counting the edges of the induced graph at their later
endpoint, `|E(U)| = Σ_x |I_x|`.

- *(c)'s hypothesis ⇒ tree and growth order.* Under the hypothesis, `|E(U)| ≤ |U| − #{x : I_x = ∅}`. Connectivity
  gives `|E(U)| ≥ |U| − 1`, so only the first site has `I_x = ∅` and `|E(U)| = |U| − 1`. So `U` is a tree and every
  later site has exactly one earlier neighbour: a growth order.
- *Tree and growth order ⇒ the hypothesis.* In a tree under a growth order, a site with two earlier neighbours `y, z`
  would close a cycle with the path from `y` to `z` inside the connected earlier set.

With U2′(b), (c) this is U4′. Consequences:

- every unit with a cycle, and every non-growth order, differs;
- in constant environments U2′(e) applies;
- the last site of a growth order is a leaf of the tree with five recorded outside neighbours, so if it is its
  parent's only dependent the order differs (S10).

*CHECKED* (T1): the equivalence on all 110 orders of seven connected units.

**S10 (PROVED) One dependent.** On functions of the six values, `K = P_0 + λ_1 P_1 + λ_2 P_2`:

- constants carry eigenvalue `1`;
- the odd functions `a ↦ a·n` carry `λ_1 = (p − q)/Z_1`;
- the even mean-zero functions `a ↦ aᵀQa` (`tr Q = 0`) carry `λ_2 = (p + q − 2r)/Z_1`.

This follows from `(K f)(a) = (p f(a) + q f(−a) + r Σ_{s⊥a} f(s))/Z_1`. So `K H` is constant iff `λ_1 P_1 H = 0` and
`λ_2 P_2 H = 0`. For `H(s) = Π_{j=1}^m K(v_j, s)`, with `n_i^±` the number of values `±e_i`,
`H(±e_i) = p^{n_i^±} q^{n_i^∓} r^{m − n_i^+ − n_i^−}/Z_1^m`.

- *`p ≠ q`:* `P_1 H = 0` iff `n_i^+ = n_i^−` for every `i` (balanced). Then `H(±e_i) = r^m (pq/r²)^{n_i}/Z_1^m`, so
  `P_2 H = 0` iff `pq = r²` or `n_1 = n_2 = n_3`. When `λ_2 = 0` (`p + q = 2r`, e.g. `(3,1,2)`) the second condition
  is void.
- *`p = q` (then `r ≠ p`, `λ_1 = 0 ≠ λ_2`):* `H` is even with `H(±e_i) = p^{a_i} r^{m − a_i}/Z_1^m`, where
  `a_i = n_i^+ + n_i^−`, so `K H` is constant iff `a_1 = a_2 = a_3`.

In particular no factor with `m = 5` outside records is constant for any non-constant rule (odd `m` when `p ≠ q`;
`3 ∤ 5` when `p = q`). *CHECKED* (L1, L2): the characterization against every value multiset of size 1–6 at the eight
rules (7384 cases, 0 mismatches). The counts of constant factors for `m = 1..6` are `0,3,0,6,0,10` at `(3,1,2)` and
`0,0,0,0,0,1` at `(5,1,2)`.

**S11 (CHECKED) The executed rule and two further counterexamples.**

- *X1:* at `(3,1,2)`, `(5,1,2)` and `(7,2,3)`, no product of `d = 1, 2, 3, 4` factors with five outside records each
  is constant, over all value multisets.
- *X2:* at `(3,1,2)` also `d = 5` is excluded, exhaustively over all multiset choices. This uses modular images of the
  exact rationals modulo `2⁶¹ − 1`, with every denominator checked prime to the modulus. Equal rationals have equal
  images, so zero modular matches means zero exact matches.

Consequences at `(3,1,2)` in every full environment (the environment enters only through the multisets `E_x`):

- *Domino.* The second site is the first site's only dependent with `m = 5` (S10): it differs.
- *Path of three, straight or bent.*
  - Middle first: two five-record factors (X1).
  - End first: the last end is the only dependent of the middle (S10).
  - Middle last: (b).
- *Straight path of four.* Every growth order has a site whose only dependent is a five-record leaf. Only the first
  site can have two later neighbours, and then the far end's parent has only that end.
- *Three-leaf claws, planar or corner.*
  - Centre first: three five-record factors (X1).
  - A leaf first: the centre becomes that leaf's only dependent with `m = 3` outside records, not balanced (S10).
  - Centre third or later: (b).
- *Star.*
  - `k ≥ 2` leaves before the centre: (b).
  - `k = 1`: the centre records only the first leaf (`E = ∅`), the five later leaves are its dependents, and X2
    applies.
  - `k = 0`: agreement in the environments of S8.

Further counterexamples:

- *X3:* the partial-environment domino (f2) agrees at `(3,1,2)` (a balanced pair and `λ_2 = 0`, so `K H` is constant)
  and differs at `(5,1,2)`.
- *X4:* the path of three (f3) agrees at `(4,1,2)` and differs at `(3,1,2)`.

In both the criterion is violated.

**S12 (CHECKED) Agreement with block 15's own executions.** For the centre-first order,
`TV(μ_σ, μ^{joint}) = ½ Σ_a |r(a | v_{E_c}) − h_c(a) Φ(a)/Σ h_c Φ|`, the total variation of the centre marginals
(`h_c` is the centre's own outside factor; for the star `r = 1/6` and `h_c ≡ 1`). This holds because both laws share
every leaf's conditional given the centre. The formula agrees with full enumeration on the two claws. It reproduces
the runner's cached star values exactly: all-`+x` `0.40289` (`= 52714185721813/130837033008291`) and the seeded
mixed environment `0.14626`. My definitions are therefore the runner's.

## 3. Where the original route fails

The first failing step is block 15's U2 proof, "(⇒)", the comparison pattern (note lines 166–168). Its claim that each
normalizer `K_{|A_{w'}|}(v_y, …)` is larger at `v_y = b` needs every other member of `A_{w'}` equal to `b`. Recorded
outside members are not free. S8 shows the resulting gap is real: six normalizers that each depend on the centre value
multiply to a constant. U4 (lines 201–204) inherits the failure. U1, the normalizer lemma, U3 (isolated units, S7(d))
and every executed number of the runner are correct.

## 4. What remains open (not needed for the corrigendum)

- Which (tree, growth order, rule, environment) satisfy U2′(c) beyond the units settled in S11: the star's `k = 1`
  order at rules other than `(3,1,2)`; trees with more sites; mixed dependents (leaves together with interior children,
  whose factors can be constant at `(3,1,2)` when balanced).
- The number of centre-first star environments that agree. At the level of value multisets, 24880 ordered matches of
  two factor-triples give a constant product at `(3,1,2)` (an exploratory count, not in `check.py`, and not a count of
  realizable environments). The 216 equivariant ones are exhibited.
- U2′ and U4′ themselves are complete criteria. Only S9's edge count and the leaf's five outside neighbours use `Z³`.

## 5. Uses of the defective statements (task (b))

| where | statement | verdict |
|---|---|---|
| #8149 note, U1 (126–140) | uniqueness of the joint law | unaffected |
| #8149 note, normalizer lemma (149–156) | closed forms | unaffected (correct; used in S7(e)) |
| #8149 note, U2 (142–177) | the iff for every environment | needs its own repair: U2′ |
| #8149 note, U3 (179–194) | isolated star and plaquette | holds on the corrected domain (isolated units, U2′(d)); its proof "U2 with the star's recorded sets" is valid there |
| #8149 note, U4 and its Reading (196–214) | every connected multi-site unit differs in an environment | needs its own repair: U4′; the star centre first agrees in 216 full environments (every rule) |
| #8149 note, clause table row 2 (221) | "in an environment never (U4)" | needs its own repair |
| #8149 note, Result up front (26–36), title (12), claim_scope (4), next_trace_action (57), conditional_surface_status (58), claim_type_reason (63), New here (111–113), obligation rows U2/U4 (120, 122) | the environment theorem and the unconditional iff | need repair (text below) |
| #8149 note, No-Go gate (227–228), N1 routes 1, 3, 4 (234, 236, 237), N5 lattice-wide (257), N7 (263), Imports (280), Review record (284) | "proved for every non-constant rule"; "no compensation"; "U4 holds for every order" | need repair; route 1 is the failing mechanism |
| #8149 note, Falsifiers bullet 4 (272) | "A connected multi-site unit in a full environment with an order reproducing the joint law" | fires (S8); after repair it becomes the U2′(c) test |
| #8149 pack: `RESULTS_block15.md` 8, `CLAIM_STATUS_CERTIFICATE_block15.md` 6, `HANDOFF.md` 30, `NO_GO_LEDGER.md` 13–14, `TRACE_GATE.md` 75, `CHECKER_block15_findings.md` 14 | the iff, U4, the refuting pass's acceptance of the comparison pattern | need repair |
| #8150 (block 16) note X3 (175–194) | mixtures in a **constant** environment iff every charged order meets block 15's criterion; "In a full constant environment every connected unit with two or more sites therefore has no such mixture" | holds on the corrected domain (constant environments: U2′(e)); its proof is the flip lemma, not U4. The sentence "The last sentence is the formation-unit note's U4." (191–192) cites the defective theorem: re-point it to U2′(e)/U4′ or to the last-site observation (the last site of every order records an inside neighbour and five outside records) |
| #8150 note, N1 route 5 (217) | "per-order statements in PR #8149" for non-constant environments | pointer update: those statements are now U2′(c) |
| #8150 note, lemma "from the formation-unit note" (102) and runner D1–D2 | the normalizer lemma; the all-`+x` executions | unaffected |
| #8158 (block 24) note line 175 | "Block 15's criterion (sequential equals joint iff no site records an inside neighbour with a second) … the recorded-environment relatives of this fork" | needs its own repair (a context sentence restating the defective iff; scope it to isolated units and constant environments or cite U2′). Lines 135 and 187, and `ASSUMPTIONS_AND_IMPORTS.md` 28, 33: unaffected |
| #8179 decision record, `DECISION_RECORD.md` line 11 | "'joint' formation of a unit equals sequential formation iff no site of the unit records an inside neighbour with a second (block 15)" | needs its own repair (U2′ wording; the plaquette witness it relies on is isolated, U3, and stands) |
| #8179 `HANDOFF.md` 30 | "plaquette witnesses (14, 15)" | unaffected (isolated plaquette) |
| #8148 (block 14) note lines 66, 153, 304, 341 and runner 516 | mentions of the formation-unit block and of joint formation as "not this note" | unaffected |
| #8180 (block 35) note line 21 | "the rule as the full conditional of one joint law on `Z³`" | unaffected (the static comparator, not block 15's law) |
| #8146, #8147, #8151–#8157, #8168, #8170–#8178 | none (the search's only matches are generic: the main-branch ledger row "full conditional of one joint law", a function named `unit`, `mu4`) | unaffected |

## 6. The exact lines that must change (task (c))

Note (`docs/ADMISSIBILITY_RULE_FORMATION_UNIT_CLAUSE_WITNESS_…_2026-09-15.md` on the PR branch):

- **Line 4 (claim_scope).** Replace the U2 clause by: "(U2) sequential formation along an order equals the joint law
  iff the normalizer product `Π_{A_x≠∅} K_{|A_x|}(v_{A_x})` does not depend on the unit's values; a site recording two
  inside neighbours always separates; otherwise equality iff for every site `y` the product of `(K H_x)` over the sites
  recording `y` together with outside records is constant. The criterion 'no site records an inside neighbour together
  with a second recorded neighbour' is sufficient in every environment and necessary for isolated units and constant
  environments." Replace the U4 clause by: "(U4) in a full environment a connected unit with at least two sites agrees
  with its joint law under an order iff it is a tree, the order a growth order, and the product condition holds; every
  unit with a cycle differs under every order; the star formed centre first agrees in the 216 environments equivariant
  under `−ρ`, for every rule."
- **Line 12 (title).** Replace "a recorded environment always does" by "a recorded environment separates them unless
  the unit is a tree formed outward and the dependents' normalizers cancel".
- **Lines 27–29.** The sentence "exactly the joint law when, and only when, no site ever records an inside neighbour
  together with any other neighbour" must be scoped: "for an isolated set or in a constant field of records".
- **Lines 31–36.** Replace "it never happens for any connected set of two or more sites, because the last site to form
  sees all its neighbours" by "it happens only for tree-shaped sets formed outward whose outside records make the
  normalizers cancel — never for a set with a cycle, never in a constant field, but for the star formed centre first
  in 216 symmetric fields".
- **Lines 57, 58, 63, 111–113, 120, 122.** "every multi-site unit does in an environment" → "every unit with a cycle
  does; trees formed outward in a symmetric environment need not". "U1, U2, U4 proved" → "U1, U2′, U4′ proved".
  "(U2) a one-site-conditional comparison" → "(U2′) the normalizer product and a strict Lagrange minor".
  "the environment theorem (U4)" → "the environment criterion (U4′)".
- **Lines 144–147 (U2 statement).** Replace by U2′ (a)–(e) of this attempt.
- **Lines 162–173 (the "⇒" proof).** Replace by S5 (two inside neighbours) and S6–S7. The all-`b` comparison is kept
  only for constant environments.
- **Lines 198–199, 201–204, 209–214 (U4, its proof, its Reading).** Replace by U4′ and S9. The Reading's "never forms
  'as if one at a time'" becomes "forms 'as if one at a time' only as a tree grown outward with cancelling normalizers
  (the centre-first star in a symmetric field)".
- **Line 221 (clause table).** "in an environment never (U4)" → "in an environment only under U4′'s product
  condition; never for units with a cycle or in constant environments".
- **Lines 227–228, 234, 236, 237, 257, 263, 272, 280, 284.**
  - "The negative sentences are U2's 'only if' and U4. Both are proved for every non-constant rule." → "The negative
    sentences are U2′(b) and U4′'s cycle and constant-environment cases."
  - Route 1 → "a cancellation among normalizers | several `K` factors compensating | happens: S8's star; the corrected
    criterion is the product condition | ACCOUNTED FOR".
  - Routes 3–4 → cite U4′.
  - N5 lattice-wide → "U1, U2′, U4′ proved".
  - N7 → "the environment criterion".
  - Falsifier 4 → "a (unit, order, environment) where exact equality and U2′(c) disagree".
  - Imports → "U2′, U4′".
  - Review record → "the campaign's expected star witness holds in constant environments and fails in 216 symmetric
    ones".

Runner (`scripts/admissibility_rule_formation_unit_clause_witness_sequential_equals_joint_iff_criterion_2026_09_15.py`):

- **Lines 2–3 (docstring title)** and **line 463 (the printed scope)**: "sequential equals joint iff no site records
  an inside neighbour with a second" → "sequential equals joint iff the normalizer product is constant (the site
  criterion is sufficient; necessary isolated and in constant environments)".
- **Line 435 (`N5_LINES`, lattice_wide)**: "U1, U2, U4 proved for every non-constant rule" → "U1, U2′, U4′ proved for
  every non-constant rule".
- **Lines 303, 374 (the C2 and E1 labels)**: executed facts, true as printed. Their "U2 (environment)" / "U4" prefixes
  should read "U2′" / "U4′".
- **New checks to add** (no existing number changes): the exact criterion `N_σ` constancy against equality on the
  executed cases (this attempt's C1/C3), the Lagrange minor (C-sym), and the centre-first star in the 216 equivariant
  environments (S1–S2, one full-law comparison takes about 2 s). Add a matching mutation (e.g.
  `equivariant_star_differs_claimed`, family E). The mutation `environment_unit_agrees_claimed` (line 55) stays valid
  for the domino and the path.
- The runner's `violates()` (lines 182–192) encodes the original criterion and can stay as the sufficient condition.
  The iff claimed through it in C1 (isolated) remains true.
