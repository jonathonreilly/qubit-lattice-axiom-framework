# causal-clauses — attempt a2

Worker `w-jonathonsmac4f50-j8f9d` (model claude-opus-5). Check script: `check.py` in this directory (exact rational arithmetic, about 5 s).

**How this attempt was prepared.**

- The plan was made before reading prior material: prove (a) by summing over formation sequences for fixed values, and enumerate the
  smallest windows for (b).
- No attempt of this problem existed at claim time.
- I then read the three round-1 referee reports on `formation-clauses-in-level-time`. They show that the round-1 attempts failed in
  two ways:
  - claiming joint formation as the unique order-independent clause without treating rate clauses;
  - giving a same-level unit a bond the rule does not have.

  This attempt treats rates explicitly and uses only bonds the rule has.
- Definitions:
  - block 01: records-only sequential law;
  - block 14 (PR #8148): clock model and clause candidates (a), (b), (c);
  - block 15 (PR #8149): joint formation of a unit (the rule-consistent law, U1) and its clause candidates;
  - block 24 (PR #8158): free window (R1) and integrated exterior (R2).

## 1. Statements attempted

**Setting.** The level-ordered `Z³`:

- the level of `x` is `x₁ + x₂ + x₃`, and the parents of `x` are `x − e_i`;
- every nearest-neighbour pair is a parent–child pair, and two sites of one level are never neighbours;
- a *window* is a finite set of sites with the induced parent structure;
- the *causal law* of a window is `P_c(v) = Π_x r(v_x | v_{Pa(x)})`, with block 01's kernel
  `r(a | A) = Π_{y∈A} K(v_y, a)/K_{|A|}(v_A)` and `r(a | ∅) = 1/6`.

Everything in (a) and (c) holds verbatim for any finite DAG, provided its undirected neighbour relation is the parent–child relation.

**(a) Theorem.** A *causal process*:

- forms every site of the window exactly once;
- forms a site, or a unit, only after all its parents are recorded;
- chooses what to form next by any rule depending on the history of formed values and on independent randomness: clocks of any rates,
  value-dependent, with memory, or not;
- forms a chosen site from the rule given its recorded neighbours;
- forms a chosen *antichain unit* (pairwise incomparable sites) jointly by block 15's rule-consistent law.

Every causal process finishes in `P_c`.

**(b)** The recorded candidates that change the law, the smallest window where each does, and the exact TV from `P_c` at `(3,1,2)` are
in the table of step S6. Three sites is the smallest window where any candidate acts. None of the candidates re-forms a record.

**(c)** Under causality every recorded set is down-closed. On a down-closed set, the free window (R1) equals the marginal of the causal
law (the causally integrated exterior). Causality settles block 24's fork: the two readings coincide. Block 24's static exterior (R2
integrated under the static law) lets a later site act on earlier ones, and changes the law by `1/72`.

**(d)** What remains open about how records form is the causal structure itself: which DAG, which parent stencil, which boundary. See
section 4.

## 2. Steps

**S1 (PROVED) Recorded neighbours are parents.** In a causal process, a site `x` is formed after its parents and before its children
(each child waits for `x`). Same-level sites are never neighbours. So when `x` forms, its recorded neighbours are exactly `Pa(x)`, and
block 01's draw is `r(v_x | v_{Pa(x)})`.

For an antichain unit `U` whose parents are all recorded:

- `U` has no internal edges, because neighbours are comparable;
- each member's recorded neighbours are its parents.

Block 15's joint law `∝ Π_{edges inside U} φ · Π_{edges U–recorded} φ` therefore factorizes into `Π_{u∈U} r(v_u | v_{Pa(u)})`.

**S2 (PROVED) Theorem (a).** Fix a value configuration `v` and a formation sequence `s = (U₁, U₂, …)`, where the units may be single
sites. The probability that the process follows `s` and produces `v` is
`Π_k P(U_k | done_{k−1}, v_{done_{k−1}}) · Π_k Π_{u∈U_k} r(v_u | v_{Pa(u)})`, by S1.

The second product runs over every site once, so it equals `P_c(v)` for every `s`. Summing over `s`,
`Σ_s Π_k P(U_k | done_{k−1}, v_{done_{k−1}}) = 1`. This is the total probability of a finite probability tree: in each state
`(done, v_done)` the choice probabilities sum to 1, and each choice strictly enlarges `done`. Induction on the number of unformed sites
gives the sum.

Conditions used:

- every state with unformed sites offers a choice (a minimal unformed site is formable);
- the rates of the formable sites do not all vanish; with any rates, choice `x` has probability `λ_x/Σλ`.

Independent auxiliary randomness (clock times, memory) is integrated inside the choice probabilities. So the finished law is `P_c(v)`.
∎

**S3 (CHECKED A1, A2).**

- *A1.* Every linear extension of six windows gives `P_c` exactly (the GIVEN). The windows are the bent and straight chains, the V, the
  Λ, the oriented plaquette and the three-parent claw; the rules are `(3,1,2)` and `(5,1,2)`.
- *A2.* 60 random value-dependent causal policies also give `P_c` exactly:
  - clocks with random integer rates keyed by the recorded set and its values, zero on non-formable sites;
  - random antichain units of formable sites, formed by block 15's joint law, computed from U1 with no factorization assumed.

**S4 (PROVED) Where a clause can act.** A process departs from `P_c` only through a site formed with a recorded child, or a draw that
conditions on or integrates unformed sites.

On a two-site window both orders give each site at most one recorded neighbour. Since `K₁ ≡ 1`, every candidate then gives `P_c`
(CHECKED B2). The three-site windows are the undirected path `x – y – z` in its three causal orientations: chain `x → y → z`, V
`x → y ← z`, Λ `x ← y → z`.

On the path, every order except the two with `y` last gives the static law (each site has at most one recorded neighbour). The two
`y`-last orders give `μ'`, in which `x` and `z` are free and `y` sees both. `P_c` is the static law for the chain and the Λ, and `μ'`
for the V. `TV(static, μ') = ½ Σ_{a,b} |K₂(a,b)/6 − 1/36| = 1/72` at `(3,1,2)`, because `144 K₂ ∈ {26, 22, 24}` for equal, opposite and
orthogonal values.

**S5 (PROVED) Block 14's clock laws as mixtures.**

- The uniform clock gives `(2/3)·static + (1/3)·μ'`.
- The seeded clock (start anywhere, then only next to records) gives only orders without `y` last, so it gives the static law.
- The attracting clock (rate `1 + #` recorded neighbours) puts `2/9` on the `y`-last orders.

The resulting distances:

- **V:** uniform `(2/3)(1/72) = 1/108`, seeded `1/72`, attracting `(7/9)(1/72) = 7/648`.
- **Chain and Λ:** uniform `(1/3)(1/72) = 1/216`, seeded `0`, attracting `(2/9)(1/72) = 1/324`.
- **Parallel growth** (value-dependent) gives `37/3888` on the V and `17/3888` on the chain and the Λ (computed).

**S6 (CHECKED B1) The list for (b)**, TV from `P_c` at `(3,1,2)`. `—` means the candidate never changes the law.

| candidate (block) | causal? | smallest window where the law changes | exact TV there |
|---|---|---|---|
| 14 (a) uniform clocks on every unrecorded site | no: children can form before parents | 3 sites: chain, Λ; V | `1/216`; `1/108` |
| 14 (b) seeded clock (as executed) | no | 3 sites: V (on chain and Λ it gives `P_c`) | `1/72` |
| 14 (b) attracting clock | no | 3 sites: chain, Λ; V | `1/324`; `7/648` |
| 14 (b) parallel growth (value-dependent) | no | 3 sites: chain, Λ; V | `17/3888`; `37/3888` |
| 14 (b) the causal member (rates only on formable sites, any values) | yes | — (Theorem (a)) | `0` |
| 14 (c) no clause | with causality imposed there is no rate-dependent statistic left | — | `0` |
| 15 "for each site" along a causal order | yes | — | `0` |
| 15 covariant unit containing a parent–child pair (domino `{x, y}` on the V, formed after `z`) | no: the parent's draw conditions on its child | 3 sites: V (this law is the static law there) | `1/72` |
| 15 whole-window unit (the static reading) | no: conditions every record on all others | 3 sites: V (on chain and Λ it equals `P_c`) | `1/72` |
| 15 antichain units (e.g. a whole level) | yes | — (Theorem (a)) | `0` |
| 24 R1 free window | yes (on down-closed windows, S7) | — | `0` |
| 24 R2 integrated exterior under the static law | no: an unrecorded later site acts on earlier ones | 3 sites: V with `y` unrecorded (block 24's own witness, factor `144 K₂ ∈ {22, 24, 26}`) | `1/72` |

- *Larger window.* On the level-ordered plaquette (a four-site cycle: bottom, two middles, top), the static law and every executed
  clock differ from `P_c`. The exact TVs are static `455/31176` (block 15's path-order number), uniform `53347/4416984`, seeded
  `691/61776`, attracting `129427/11042460` and parallel growth `12853/1070784`.
- *Re-forming records.* No recorded candidate re-forms a record: each forms each site once, and R2 is a marginal, not a dynamics. The
  static law arises dynamically only by re-forming records (heat-bath re-recording), which the causal hypothesis excludes.

**S7 (PROVED; CHECKED C1) (c).** Let `S` be down-closed: every parent of a site of `S` is in `S`.

- Summing `P_c` over the values of the sites outside `S` gives the causal law of `S` alone. Sum out a maximal unformed site first; its
  kernel sums to 1 and no other factor contains it. Then induct.
- A causal process only ever produces down-closed recorded sets. So the free window and the causally integrated exterior coincide on
  every window that can occur.
- The static R2 is the marginal of a law that weighs later sites into earlier ones. With `x, z` recorded and their common child `y`
  unrecorded, it gives `P(x, z) ∝ K₂(x, z)` against the free `1/36`: TV `1/72`.

*CHECKED:* on six windows, for every down-closed subset, the marginal of `P_c` equals the sub-window's causal law exactly.

## 3. What fails, and where

Nothing in (a)–(c) fails. The limits are these:

- the theorem needs "no record re-formed" and "parents first" as hypotheses. It says nothing about processes that re-record, which is
  the round-1 `re-recording` problem;
- the smallest-window TVs in (b) are at `(3,1,2)`, and they are rule-dependent. The structure (zero or not) is the same at `(5,1,2)`
  for the checks run in A1–A2, but the (b) numbers were computed at `(3,1,2)` only.

## 4. (d) What remains open about how records form once the lattice is causal

By (a) and (c), once parents come first and nothing is re-formed, rates, units and the treatment of unrecorded sites carry no further
information. The law is fixed by three things:

1. **The causal structure itself.** Which sites are an event's parents, i.e. the stencil and the level function.
   - The monotone class (three parents `x − e_i`; covariant only under the rotations fixing `(1,1,1)`) and the light-cone lattice
     `Z³ × Z` (seven parents: self and six neighbours; full cubic covariance in space) are different laws, e.g. the NEC automaton
     against the seven-stencil automaton.
   - The axioms' "nearest-neighbour conditions" name the neighbours, not their orientation in formation.
2. **The kernel given the parent set.** Block 01's `r(· | Pa)` with the product rule's normalizer `K_{|Pa|}`, or another covariant
   kernel of the same one-site conditionals.
3. **The boundary.** Which events have missing parents (the first level, a seed), and the memory depth (parents from one level or
   several).

The question "in what order, at what rate, in what units" is closed on causal lattices. The open question is "on which event lattice,
with which stencil and which initial level" — a statement about the causal structure, which the recorded clauses do not fix.
