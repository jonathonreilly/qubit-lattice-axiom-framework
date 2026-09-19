# tight-sibling-lemma, attempt 3 (worker w-macbookpro90c72-jf5ff, model grok-4.6)

No prior attempt was printed at claim time. Route (i): a local statement about the depth-2 predecessor cone of a processed site. Definitions from block 33 (PR #8177) and `probes/lib/family.py`: two-level noisy majority; kinds seed / amplified / processed; rooted value `v(z) = min E − 3(|S|−1) − |A|` over the counted family of marked explanation trees with nodes at levels `≤ level(z)`; tight means `v=0`. The lemma: a processed site all of whose 1-predecessors are tight processed sites has `v ≤ 0`.

## (1) The statement attempted

On the isolated depth-2 predecessor cone of a site `z` (10 sites, every mark pattern, automaton run on the depth-3 cone of 20 sites with unmarked exterior), every pattern that makes `z` processed with two or more processed 1-predecessors has exact `brute_min` rooted value `v(u) ∈ {−5,−6,−8,−9,−11,−14}` for each such predecessor `u`, never `v(u)=0`. There are 512 such patterns out of 1024, and 1248 predecessor instances. Tight processed siblings sharing a processed successor do not occur in the isolated cone. Route (i) therefore holds locally. It does not prove the lemma on `Z^3`, because a rooted tree may use 1-sites outside the cone.

## (2) Steps

**Step 1 — geometry (PROVED; CHECKED E.1–E.2).** The predecessors of `z` are `z−e_j`. Any two of them differ by `e_i−e_j`, a fork offset, so they are siblings. The depth-2 cone of `z=(2,2,2)` has 10 sites; the depth-3 cone has 20. Marks are placed only on the depth-2 cone; the automaton is run on the depth-3 cone so majority can still light unmarked sites one layer below.

**Step 2 — kinds, not yet values (PROVED; CHECKED E.3).** Of 1024 mark patterns, 512 make `z` processed with at least two processed 1-predecessors. The local automaton therefore *does* produce processed siblings sharing a processed successor. Route (i) cannot be “processed siblings never share a processed successor”; the extra word is *tight*.

**Step 3 — rooted values on the isolated cone (CHECKED E.5–E.12).** For each of those 512 patterns, `family.brute_min` (the exact enumeration of the counted family on a tiny 1-set) is computed at each processed 1-predecessor and at `z`. All 1248 predecessor values are defined integers in `{−5,−6,−8,−9,−11,−14}`; the maximum is `−5`; none is `0`. All 512 successor values are `≤ 0`. So on the isolated cone the hard inductive case never arises: the processed 1-predecessors are cheaper than tight.

**Step 4 — why the values are negative (PROVED at the level of the cost formula).** On a finite isolated cone the 1-component is small and typically has several seeds (the bottom of the cone). Each extra seed contributes `−3` to the cost after the first, and amplified sites contribute `−1`. The observed values `−5` through `−14` are the possible `(E,A,S)` combinations on this 10-site support. Tightness `v=0` needs a balance `E = 3(|S|−1) + A`; the isolated cone overshoots toward more seeds.

**Step 5 — the global gap (PROVED as a no-go for closing the lemma by this enumeration).** A configuration on `Z^3` can place additional 1-sites outside the cone, add processed nodes without adding seeds, and raise `v` toward 0. The local enumeration does not constrain those trees. Hill-climbs on larger windows (the tools on this branch) are the remaining search; they are not a proof.

## (3) Where the route stops

The first step that fails as a proof of the lemma is the passage from the isolated cone to `Z^3`: tightness is a global minimum over trees, not a local function of the cone marks. Route (i) survives as a local theorem (no tight processed siblings-with-successor in the isolated depth-2 cone) and as evidence that the hard case, if it exists, requires 1-sites outside that cone.

## (4) What would finish it

An argument that any 1-sites added outside the cone cannot raise every processed 1-predecessor’s `v` to exactly 0 simultaneously without also supplying a cheap tree for `z` (a surgery / grafting lemma); or a counterexample on a window large enough that outside nodes are present (the existing climbers have not found one). Exhausting the depth-3 cone (`2^{20}` patterns) is feasible in principle with the same `brute_min` cut when `|ones|` is large.
