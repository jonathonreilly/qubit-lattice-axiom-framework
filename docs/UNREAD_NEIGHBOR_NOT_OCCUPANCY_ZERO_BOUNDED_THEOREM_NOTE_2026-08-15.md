---
claim_id: unread_neighbor_not_occupancy_zero_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the supplied twelve-vertex two-cube, replacing off-patch `o=0` by “blank blocks readiness” empties the first wave. L1's wave uses the vacuum default. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/unread_neighbor_not_occupancy_zero_2026_08_15.py
---

# Unread Neighbor Is Not Occupancy Zero

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact first-wave comparison on one supplied twelve-vertex two-cube,
between a displayed L1 law that fills off-patch neighbors as occupancy `0`
and the alternative member that leaves those neighbors blank and blocks
readiness. No new patch, no leftover-character identity, and no vacuum axiom.
**Audit-status authority:** independent audit lane only. This note writes no
audit verdict and predicts none.
**Primary runner:**
[`scripts/unread_neighbor_not_occupancy_zero_2026_08_15.py`](../scripts/unread_neighbor_not_occupancy_zero_2026_08_15.py)

No runner cache is written.

## Result up front

Neighbor input on the cubic lattice is a six-tuple from `{0,1,blank}`.
Occupancy `0` and blank are distinct letters. Record unreadability says that
a site with no record cannot be read; it does not assign the letter `0` to
that site.

On the supplied two-cube, a seed lock at `(0,0,0)` is given. The displayed
L1 law treats each blank as `0` and forms at an unformed on-patch site iff
the neighbor occupancy sum `n` is nonzero. That first wave is exactly the
three axis sites

```text
(1,0,0), (0,1,0), (0,0,1).
```

Under blank-blocked readiness, `n` is defined at a site only when all six
lattice neighbors are on-patch and already in `{0,1}`. None of those three
axis sites is ready: each has at least one off-patch neighbor. The
blank-blocked first wave is empty.

Therefore the off-patch `o=0` default is load-bearing for L1's first wave.
It selects one member of a pair. It is not Record unreadability, not a
leftover-character identity, not an `n_μ` step on a new patch, and not a
vacuum axiom. L1 is displayed, not adopted. L2 is not adopted.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact first-wave comparison on one twelve-vertex two-cube; L1 is displayed; off-patch encoding is a member selector, not an axiom."
trace_class: negative_route_pruning
target_claim_id: unread_neighbor_not_occupancy_zero
target_blocker_text: "do not treat unread or off-patch neighbors as occupancy 0 when naming a formation-ready first wave"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "keep off-patch blank as a distinct letter; do not write unread=0 into axiom text"
conditional_surface_status: "exact only for the supplied twelve-vertex two-cube and the displayed L1 / blank-blocked pair; no axiom edit and no adopted formation law"
hypothetical_axiom_status: no edit
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premise boundary

The current axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies:

```text
Physical sites are the points of the cubic lattice Z^3, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

Records form.

When present, a record locks exactly one admissible local possibility.

Only records are readable. A readout value is determined by record content
alone. A site with no record cannot be read.
```

The last sentence is unreadability. It is not an assignment of occupancy
`0` to an unread site, and this note does not write that assignment into
axiom text.

Admissibility says that, for each site, the probability distribution over
the possibilities is determined by, and varies with, the nearest-neighbor
conditions. It does not supply a formation site, a first-wave rule, or a
default letter for a neighbor that is not on the declared patch.

The two-cube, the seed lock, the displayed L1 rule, and the blank-blocked
alternative are declared test objects. They are not derived here as the
physical formation kernel.

## Exact objects

Let

```text
A = {0,1}^3,
B = {1,2} x {0,1}^2,
P = A union B.
```

Then `|A|=8`, `|B|=8`, `|A intersect B|=4`, and `|P|=12`. These are the
twelve vertices of one two-cube. The construction is the same two-cube, not
an `n_μ` step on a new patch.

The six lattice shifts are the signed unit vectors. For `v` in `Z^3`,

```text
N(v) = { v ± e_1, v ± e_2, v ± e_3 }.
```

A site is **on-patch** when it lies in `P`, otherwise **off-patch**.
Off-patch sites carry the letter `blank`, not occupancy `0`.

A seed lock is placed at

```text
s = (0,0,0) in P.
```

The displayed occupancy field after the seed, before any first wave, is

```text
o(s) = 1,
o(v) = 0    if v in P and v ≠ s,
o(w) = blank    if w not in P.
```

The integer `n` at a site `v` is the sum of the six neighbor letters after
the displayed blank-to-zero map

```text
pi(0) = 0,   pi(1) = 1,   pi(blank) = 0,
n(v) = sum_{u in N(v)} pi(o(u)).
```

This `n` is a displayed occupancy sum on one patch. It is not a
leftover-character of an L1 identity.

**Displayed L1** (not adopted): an unformed on-patch site `v` forms in the
first wave iff `n(v) ≠ 0`. Blanks are treated as `0` before the test.

**Blank-blocked readiness:** `n` is defined at `v` only if every neighbor
in `N(v)` is on-patch and already in `{0,1}`. Otherwise `v` is
blank-blocked. A site is formation-ready only if `n` is defined and
`n(v) ≠ 0`. The blank-blocked first wave is the set of unformed on-patch
sites that are formation-ready.

## Theorem 1 — L1 first wave is the three axis sites

After the seed, evaluate `n` at every unformed site of `P`. The seed has
exactly three on-patch neighbors, namely the axis sites

```text
W = {(1,0,0), (0,1,0), (0,0,1)}.
```

Each `w` in `W` has `o(s)=1` as one neighbor, so `n(w)=1 ≠ 0`. Every other
unformed `v` in `P` is nonadjacent to `s`, so every neighbor occupancy
that L1 can see is `0` and `n(v)=0`. Therefore the displayed L1 first wave
is exactly `W`.

The paired runner computes this set from the occupancy field. It does not
embed `W` as its own output.

## Theorem 2 — blank-blocked first wave is empty

Each axis site has at least one off-patch neighbor. Explicitly:

```text
(1,0,0) has (1,-1,0) and (1,0,-1) off-patch,
(0,1,0) has (-1,1,0) and (0,1,-1) off-patch,
(0,0,1) has (-1,0,1) and (0,-1,1) off-patch.
```

So `n` is not defined at any point of `W`. No site of `W` is
formation-ready. The blank-blocked first wave is empty.

The same two-cube has no unformed site whose entire six-neighbor star lies
in `P`. Blank-blocked readiness is empty on the whole patch, not only on
`W`. The theorem needs only the emptiness of the first wave.

## Theorem 3 — off-patch `o=0` is a member selector

The two members differ only in the letter assigned to off-patch neighbors:

| member | off-patch letter | first wave |
|---|---|---|
| displayed L1 | `0` | `W`, size 3 |
| blank-blocked | `blank` | empty |

L1's nonempty first wave uses the vacuum default that fills off-patch
neighbors as `0`. Replacing that default by “blank blocks readiness”
empties the first wave. The default is therefore load-bearing for this
displayed wave. It selects a member. It is not Record unreadability: the
axiom sentence is that a site with no record cannot be read, not that the
site carries occupancy `0`.

The comparison is displayed, not adopted. It does not write a vacuum axiom,
does not adopt L1 or L2, and does not promote `unread = 0`.

## No-Go Discipline

The negative result is only that the off-patch `o=0` fill is load-bearing
for this displayed first wave. It is not a universal no-go against every
formation rule.

### N1 — materially distinct route scan

| route | marker | outcome relative to the narrow target |
|---|---|---|
| treat unreadability as occupancy `0` | **ATTEMPTED** | Record forbids reading an absent record; it does not supply the letter `0` |
| keep off-patch blank and still run L1 | **ATTEMPTED** | `n` is then undefined at each axis site; the first wave empties |
| move the same `n_μ` step onto a new patch | **ATTEMPTED** | the two-cube is held fixed; only the off-patch letter changes |
| read the wave as leftover-character of an L1 identity | **ATTEMPTED** | `n` here is a six-neighbor occupancy sum, not a leftover-character |
| adopt L1 or L2 as axiom text | **ATTEMPTED** | both laws remain displayed test objects; L2 is unused |
| write a vacuum axiom that empty sites are `0` | **ATTEMPTED** | the `o=0` fill is a member of a pair, not axiom content |
| invoke a Hamiltonian or record-production dynamics | **ATTEMPTED** | outside the finite two-cube comparison |

### N2 — wall independence

One type wall is claimed: blank and occupancy `0` are different neighbor
letters, and only the `0` fill produces L1's first wave on this patch. No
second impossibility wall is asserted.

### N3 — hidden-wall scan

The two-cube, the seed, the displayed L1 map, and blank-blocked readiness
are declared. No new patch, no leftover-character algebra, no adopted L2,
no vacuum axiom, and no axiom edit is imported.

### N4 — residual matching

The residual after this note is still a physical formation rule—site,
process, and rate—plus any lawful encoding of neighbors that are not on a
declared finite patch. The present witness neither closes nor enlarges that
residual. It only names the off-patch `o=0` fill as a selector on this
patch.

### N5 — certificate granularity

```text
per-element: executed — each of the twelve vertices is enumerated
per-site: executed — n and readiness are computed at every unformed site
per-mode: not applicable — no modal or spectral decomposition is used
per-block: executed — only the supplied two-cube and seed are checked
lattice-wide: not executed — no full Z^3 history or adopted formation law is claimed
```

### N6 — partial-closure paths

A later formation kernel could define readiness only from on-patch
neighbors, derive a different letter for off-patch sites, or work on a
larger patch whose six-neighbor stars close. Every such route remains live
and need not alter the axioms.

### N7 — steelman

The strongest objection is that an unread or off-patch site “is empty, so
it is `0`,” making the L1 fill automatic. Correct that emptiness is a
possible reading of no-record. Incorrect that Record supplies the letter
`0`: unreadability withholds a readout, and filling `0` is extra encoding.
On this two-cube that extra encoding is exactly what produces the first
wave.

### N8 — cross-cycle echo

Earlier formation-boundary notes already separate occurrence, content
support, and site choice. This note agrees with that separation and adds
only the exact two-cube witness that off-patch `o=0` is a selector for a
displayed L1 wave.

## Boundaries and explicit non-claims

- L1 is displayed, not adopted. L2 is not adopted.
- The theorem is conditional on the supplied twelve-vertex two-cube and
  seed. It does not derive a physical formation kernel.
- This is not an `n_μ` step on a new patch.
- This is not leftover-character of an L1 identity.
- This is not a vacuum axiom, and unreadability is not rewritten as
  occupancy `0`.
- No full-lattice history, process, clock, or rate is constructed.
- No axiom, primitive, registry, citation manifest, runner cache, or audit
  verdict is edited.

## Verification

Run:

```bash
python3 scripts/unread_neighbor_not_occupancy_zero_2026_08_15.py
```

The runner prints `TOTAL: PASS=<n> FAIL=<n>` with `FAIL=0` and at least
twelve `PASS` lines. It writes no cache.
