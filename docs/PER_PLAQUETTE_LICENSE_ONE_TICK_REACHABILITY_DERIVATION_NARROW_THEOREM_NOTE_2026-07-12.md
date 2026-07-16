# Unit-Neighborhood Link-Support from One-Tick Reachability (Narrow)

**Date:** 2026-07-12  
**Claim type:** bounded_theorem  
**Type:** bounded_theorem  
**Status:** bounded theorem conditional on the named `(P-FUND-1TICK)` packet  
**Status authority:** independent-audit-lane block; this source note does not
set or predict an audit outcome.  
**Primary runner:**
[`scripts/per_plaquette_license_one_tick_reachability_derivation_2026_07_12.py`](../scripts/per_plaquette_license_one_tick_reachability_derivation_2026_07_12.py)  
**Cached output:**
[`logs/runner-cache/per_plaquette_license_one_tick_reachability_derivation_2026_07_12.txt`](../logs/runner-cache/per_plaquette_license_one_tick_reachability_derivation_2026_07_12.txt)

## Statement and claims

Let `R` be the self-plus-nearest-neighbor dependency relation on the cubic
lattice.  For a set of sites `S`, write

```text
C_0(S) = S,
C_{t+1}(S) = C_t(S) union {v : there exists u in C_t(S) with (u,v) in R}.
```

The reachability result used here is only the finite-graph theorem: when an
update has already been established to be `R`-local, differences initially
confined to `S` remain confined to `C_t(S)` after `t` ticks.  The local
one-step identities below are identities on `Z^3`; the executable certificate
checks them inside a finite window with every tested neighborhood away from
the boundary.

### Lemma A (definitional identity)

For a nearest-neighbor link `l=(a,b)`, define the closed unit neighborhood
`N(s)={s} union NN(s)`.  Then

```text
C_1({a,b}) = N(a) union N(b)
            = {p : min(d(p,a), d(p,b)) <= 1},
```

where `d` is cubic graph distance.  This is exactly the set in the
unit-neighborhood link-support license.

### Lemma B (bridge; conditional closure status)

Let a fundamental multi-link admissibility term have constituent link set `L`
and joint carrier support `vertices(L)`.  Suppose the term is one-tick
confined at each `l in L` in the sense of `(P-FUND-1TICK)`: the whole term
presented at `l=(a,b)`—its entire joint carrier, not merely a derived
availability scalar—is supported on tick-`t` data drawn from `l`'s one-step
dependency set `C_1({a,b})`.  Then

```text
vertices(L) subseteq C_1(l)  for every l in L.
```

This is verbatim the unit-neighborhood link-support license in support-set
form.  The condition constrains the term's full carrier: a term whose recorded
availability scalar is constant, or otherwise ignores part of its carrier,
would meet a scalar-only dependency bound while still spreading `vertices(L)`
outside some `C_1(l)`, so the carrier-level statement is the load-bearing one.
The R4 attempt below does not derive this one-tick carrier-confinement
condition from the accepted surface, so this lemma is used conditional on the
named `(P-FUND-1TICK)` packet.

### Corollary C (the license, derived conditionally)

Under Lemma A and Lemma B with `(P-FUND-1TICK)`, the parent license is exactly
the one-tick reachability upper bound: the allowed dependence of every
constituent link `l` is `C_1(l)`, and the joint support is contained in every
such `C_1(l)`.  Therefore the inherited finite consequence checks give 24 of
24 rooted simple length-4 plaquette loops passing and 0 of 264 rooted simple
length-6 loops passing.  The reachability form and the parent's literal
`min(d(.,a),d(.,b)) <= 1` predicate have identical pass/fail vectors on both
enumerated loop domains.

## Proofs

### Proof of Lemma A

Unfold the recursion once.  For any source set `S`,

```text
C_1(S) = S union {v : there exists s in S with (s,v) in R}
       = union over s in S of C_1({s}).
```

The second equality is ordinary distribution of the existential quantifier
over the source set.  Because `R` contains exactly self-edges and directed
nearest-neighbor edges,

```text
C_1({s}) = {s} union NN(s) = N(s).
```

Taking `S={a,b}` gives `N(a) union N(b)`.  Cubic graph distance is one exactly
on nearest-neighbor pairs, so membership in that union is equivalent to
`min(d(p,a),d(p,b)) <= 1`.  No dynamical or physical-light-cone reading enters
this definition-unfolding.

### Proof of Lemma B under its named hypothesis

Fix a constituent link `l`.  `(P-FUND-1TICK)` states that the whole term
presented at `l`, its carrier included, is supported on tick-`t` data drawn
from `C_1(l)`; in particular the term's joint carrier support is contained in
`C_1(l)`.  That carrier support is `vertices(L)`, so
`vertices(L) subseteq C_1(l)`.  The link `l` was arbitrary, hence the
containment holds for every `l in L`.  A scalar-only reading—"the availability
value at `l` is a function of `C_1(l)` data"—does not suffice on its own: a
constant availability is such a function yet constrains no carrier vertex,
which is why the carrier-level condition is the one that is load-bearing.

Lemma A replaces each `C_1(l)` by the parent's literal unit-neighborhood set,
which proves the stated bridge once the one-tick carrier-confinement condition
is supplied.

### Proof of Corollary C

Lemma B gives `vertices(L) subseteq C_1(l)` for every constituent link.
Lemma A identifies that set exactly with the literal distance predicate.
Thus the derived-form and literal-form licenses are the same predicate, not
merely bounds with matching sample counts.  The paired runner independently
recomputes their identical finite consequences at lengths 4 and 6.

## R4 closure attempt and named residual

The Admissibility axiom states:

> There is one fixed nearest-neighbor admissibility rule, covariant under
> lattice translations and proper cubic rotations. For each site, the
> available possibilities are determined by, and vary with, the
> nearest-neighbor conditions.

The Record axiom says that, when present, a record locks exactly one
admissible local possibility.  These statements establish a spatially local
per-site availability and a local lock.  They do not identify a ticked update
law, register one common multi-link availability at every constituent link,
or state that such an availability can be evaluated from the preceding
tick's data.  Indeed, the axiom memo expressly separates Admissibility from
dynamics and leaves the time metric and formation rule downstream.

The bounded commuting joint-presentation bridge supplies a common finite
multi-site tensor carrier under its declared `(J1)`/`(J2)` packet.  That makes
a joint presentation available, but the bridge expressly supplies no
dynamics and imposes no dependency support on the term's carrier.
Commutation therefore does not turn the per-site clause into per-link
one-tick carrier confinement.

Finally, the finite-graph reachability theorem applies after a rule is known
to be `R`-local.  Using that theorem to declare this multi-link term
`R`-local would assume the bridge being sought.  The decisive residual is:
the accepted sources supply spatial locality and a joint carrier, but no
statement makes a fundamental multi-link availability, at each constituent
link, read only tick-`t` data on that link's `C_1` set, nor confines the
term's carrier `vertices(L)` to that set.  The R4 closure
attempt therefore does not certify, and the residual is named exactly as
follows.

```text
(P-FUND-1TICK) Fundamental one-tick carrier-confinement packet (2026-07-12).
A fundamental multi-link admissibility term is one-tick confined at each
constituent link: the whole term presented at constituent l=(a,b) -- its
entire joint carrier, not merely its availability scalar -- reads only, and is
supported on, tick-t data on l's one-step dependency set C_1({a,b}); in
particular its carrier vertices(L) lie in C_1(l). This is the block's
load-bearing open condition. It is a named conditional packet on this note's
surface only, not an entry in axiom_premise_nodes.json and not a
chain-satisfying premise; the R4 closure attempt above did not derive it.
```

## Route-pruning remark: minimal-nonempty covariant lift only

The alternative selector "choose the minimal nonempty covariant lift" is
false as a derivation route.  This statement is scoped only to that selector.

For the undirected reference link `{0,e1}`, the eight proper cubic rotations
that stabilize its axis as an undirected link (four endpoint-preserving axial
rotations and four endpoint-swapping elements) partition `C_1({0,e1})` into
three orbits:

- endpoints, of size 2: `{0,e1}`;
- axial exterior points, of size 2: `{-e1,2e1}`;
- transverse points, of size 8:
  `{+-e2,+-e3,e1+-e2,e1+-e3}`.

The endpoint-plus-transverse orbit union is a strict 10-point subdomain of
the 12-point full unit neighborhood.  Transporting this domain covariantly to
each link still gives mutual containment for all 24 rooted plaquette loops;
it excludes the axial orbit.  It therefore falsifies minimality as a selector
for the full `C_1` domain.  For context only, the same witness passes 0 of the
264 enumerated length-6 loops.  This is not a no-go for other derivations or
for the named one-tick packet.

Consequently, the finite length-4/length-6 consequence checks alone do not
distinguish the full `C_1` domain from this strict transverse subdomain:
both reproduce the identical 24/0 selection on the enumerated domains.  What
pins the full `C_1` set is the derivation itself — the license is the
permissive one-tick reachability bound on allowed dependence (Lemmas A and
B), not a domain selected by the enumeration outcomes.

## Boundaries

- This does **not** prove that the fundamental action is per-plaquette.
- The length-4 and length-6 enumeration domains are inherited from the parent
  note only for the consequence checks; no claim about other lengths is made.
- This does not amend the framework axioms or approved primitives.
  `(P-FUND-1TICK)` is a named conditional packet on this block's surface.
- `theta_bare` is untouched.
- The parent note is not modified in this block; proposed consumption wiring
  is deferred to block 03.
- The finite-graph theorem is not enlarged into a physical-spacetime,
  Lorentz-invariance, continuum, or universal-speed statement.

## Dependencies

- [LATTICE_NN_LIGHT_CONE_NOTE.md](LATTICE_NN_LIGHT_CONE_NOTE.md) — used only
  at its finite-graph reachability scope and for the recursion defining `C_t`.
- [MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md) — supplies the
  quoted Admissibility clause and the bounded R4 Record reading.
- [QUBIT_LATTICE_JOINT_PRESENTATION_TENSOR_SUBSTRATE_BRIDGE_NOTE_2026-07-09.md](QUBIT_LATTICE_JOINT_PRESENTATION_TENSOR_SUBSTRATE_BRIDGE_NOTE_2026-07-09.md)
  — consumed only at its declared commuting joint-presentation carrier scope;
  its lack of dynamics is part of the R4 boundary.
- `PER_PLAQUETTE_FROM_ADJACENCY_LICENSE_BOUNDED_THEOREM_NOTE_2026-06-09.md`
  is the downstream consumer context.  It is deliberately not linked as a
  dependency here so block 03 can wire that parent to this upstream note
  without creating a citation cycle.
- `KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md` is context only and supplies
  no proof step in this block.

## Verification

```bash
python3 scripts/per_plaquette_license_one_tick_reachability_derivation_2026_07_12.py
python3 scripts/precompute_audit_runners.py --runners scripts/per_plaquette_license_one_tick_reachability_derivation_2026_07_12.py --force --allow-non-main --push-mode none
python3 scripts/frontier_per_plaquette_from_adjacency_license_2026_06_09.py | tail -3
git status --short
```

```yaml
claim_type_author_hint: bounded_theorem
claim_scope: "Conditional on P-FUND-1TICK, the unit-neighborhood link-support license is exactly the per-constituent one-tick reachability bound."
```
