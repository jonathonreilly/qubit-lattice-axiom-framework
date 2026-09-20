# tight-sibling-vacuity: derivation attempt 1 of 4

Worker `w-jonathonsmac4f50-j2496` (claude-opus-5), unit `J-derive-tight-sibling-vacuity-a1`.

**Provenance.** Three attempts existed at claim time. `a2` (`w-macbookpro90c72-jb9bd`) and `a4`
(`w-macbookpro90c72-je5f9`) are from another machine and another running worker; `a3`
(`w-jonathonsmac4f50-j041c`) is from mine. All four, including this one, are claude-opus-5, so
none of us is family-independent of the others; the machine and session are different for `a2`
and `a4`.

**What this attempt is.** `a2` refutes three statements at once — the task's (Q), block 33's
tight-sibling lemma, and the rooted inequality (H) — and bounds block 32's family constant below
by `10/9 > 1`, which removes the `c = 1` certificates behind block 33's threshold 453. A
refutation carrying that much weight should be re-derived by someone who shares no code with it,
especially since the task's own referee note warns that `probes/lib/family.py`'s `brute_min`
omits the level restriction, which is exactly the error that would manufacture a false
counterexample. **This attempt re-derives it from `a2`'s ten marks and nothing else.** It uses no
`probes/lib`, no `scipy` and no code of `a2`'s; the minimiser is a layered dynamic program in
exact integers, and `scipy` appears only as an optional cross-check at the end.

I did not attempt to prove (Q) independently first: with a published counterexample in hand,
forming an independent plan to prove a false statement would have been wasted effort. What I
formed independently is the verification method.

## 1. The statement attempted

> **(Q)** A processed site with at least two processed 1-predecessors cannot have all of them
> tight (`v = 0`).

**Result: (Q) is false, confirmed.** At the realization of `a2`'s marks
`M = {000, 001, 010, 100, 021, 102, 210, 113, 131, 311}`:

- the one-set is the same computed in `[0,3]³` and in `[−2,6]³` — 37 sites, one seed, 9 amplified,
  27 processed-type, level sizes `1,3,3,4,3,6,7,6,3,1`;
- `333` is processed-type and its three 1-predecessors `233, 323, 332` are all processed-type;
- **`v(233) = v(323) = v(332) = 0`** — all three are tight — and **`v(333) = +1 > 0`**.

So a processed site *can* have all its processed 1-predecessors tight, the tight-sibling lemma's
conclusion fails at `333`, and (H) fails with it.

**And:** `min(E − |A|) = 1` while `min(E − (10/9)|A|) = 0` at the root `333`, so
**`c*(η, 333) = 10/9`** exactly — with the level restriction and without it.

**New here:** the witness is **mark-minimal**. Dropping any one of the nine non-seed marks stops
`333` being processed-type, so no nine-mark sub-realization of this shape refutes the lemma.

## 2. Steps

**S1 (PROVED; CHECKED `V1`). The realization is the one on `Z³`.**
Computing from `M` inside `[0,3]³` and inside `[−2,6]³` gives the same one-set, so nothing escapes
the box and the finite computation is the infinite-lattice realization. (`a2` proves this by an
induction on the level; the two-box computation is the same fact, executed.)

**S2 (PROVED; CHECKED `V2`). The kinds.** One seed (`000`), nine amplified (the other marks), 27
processed-type; level sizes `1,3,3,4,3,6,7,6,3,1`; `333` is the only level-9 site and its three
1-predecessors are processed-type.

**S3 (PROVED; CHECKED `V3`). The minimiser.**
With a single seed, `3(|S| − 1) = 0` and a tree of the family is exactly a set `T` of 1-sites in
which every non-seed node has a 1-predecessor in `T`; `cost(T) = E − c|A|` with `E` the number of
processed-type nodes and `A` the number of amplified nodes. Every predecessor of a level-`(l+1)`
site lies at level `l`, so a sweep by level whose state is "which level-`l` sites are in `T`" is
**exact**: the transition from level `l` to `l+1` only has to check, for each candidate site, that
one of its three predecessors is in the state. The widest level here holds 7 sites, so the sweep
is `2⁷` wide and the whole computation is a few thousand operations in exact integers.
- This is where the referee's caution bites, and the DP respects it by construction: the sweep is
  run only up to level `τ(z)`, so no node above `z` can enter the tree. `V5` also runs it without
  that restriction, to separate the two questions.

**S4 (PROVED; CHECKED `V4`). The values.** `v(233) = v(323) = v(332) = 0`, `v(333) = +1`. The
optimal trees are exhibited: at each of the three predecessors, `|T| = 11` with `E = A = 5` and one
seed; at `333`, `|T| = 12` with `E = 6`, `A = 5`.
- Note these are **smaller** than the trees a node-closure integer program returns for the same
  values (`|T| = 19`, `E = A = 9`): the optimum is not unique, and the DP happens to find a
  cheaper-looking one. Only the value matters, and the two machineries agree on it (`V7`).

**S5 (PROVED; CHECKED `V5`). The family constant at this root.**
Running the DP with a rational parameter: `min(E − c|A|) = 1, 0, −1/100, −1` at
`c = 1, 10/9, 1001/900, 11/9`. The zero at `c = 10/9` says `min E/|A| = 10/9` over trees at this
root with `|A| ≥ 1`, so `c*(η, 333) = 10/9 > 1`. Lifting the level restriction gives the same
value, so this is the family's value and not an artefact of the rooted definition.

**S6 (CHECKED `V6`). Minimality.** For each of the nine non-seed marks, the realization of
`M ∖ {m}` was rebuilt and re-classified: in every case `333` ceases to be processed-type. So all
ten marks are load bearing and the witness cannot be shrunk by one mark.

**S7 (CHECKED `V7`). Cross-check.** A node-closure integer program (`x_y ≤ Σ_{p ∈ pred₁(y)} x_p`,
minimise `Σ w_y x_y`, solved by HiGHS) agrees with the DP at all four sites. This is an
independent encoding, not the flow encoding of `probes/lib`; it is optional and the DP needs
nothing but the standard library.

## 3. Where the route stops

- This attempt **verifies** a refutation; it does not prove anything new about the lemma's scope.
  What it adds is that the refutation survives a re-derivation that shares no code with it, that
  the level restriction the referee warned about is respected, and that the witness is minimal.
- Minimality is tested only for the removal of **one** mark, and only for this root. A smaller
  counterexample with a different mark set is not ruled out, and I did not search for one.
- I did not re-derive `a2`'s claims about what this does to block 33's threshold beyond the
  arithmetic of `c*`: the statement "the `c = 1` certificates fall" is `a2`'s and I take it as
  read.
- `a4`'s separate refutation (of a different conjecture) is untouched here.

## 4. What would finish it

1. A search for a smaller witness — fewer marks, or a lower root — would make the refutation
   cheaper to referee. The DP here is fast enough to drive such a search over mark sets in a small
   box, which is the obvious next unit.
2. The open question that matters is no longer (Q) but **what replaces it**: with `c* ≥ 10/9`, the
   tree route's floor moves, and the count needs either a larger `c` or a different family. The
   value `10/9` at this realization is a lower bound on `c*`; the supremum over all realizations
   is not known, and the same DP can be pointed at that question on small boxes.
3. Block 33's note and block 32's conjecture both need the corrigendum this implies; that is a
   supervisor action, not a probe's.

## 5. Running it

```
python3 probes/work/derive/tight-sibling-vacuity/w-jonathonsmac4f50-j2496/check.py
```
from the repository root. Needs only the standard library (`scipy` and `numpy` are used for the
optional `V7` cross-check and skipped if absent). A few seconds.
