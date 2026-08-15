---
claim_id: lock_content_without_m2_action_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Occupancy determines (S,k) without Aut(M_2). Spectral projectors of a Bloch image require an axis–Pauli pairing, which is extra. Displayed, not adopted. No Aut-pick."
upstream_dependencies:
  - minimal_axioms
runner: scripts/lock_content_without_m2_action_2026_08_15.py
---

# Lock Content Without An `M_2` Action: Object-Split Of The Cube-Action Boolean

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy algebra of a six-bit directed cube and the extra
axis–Pauli pairing needed to write rank-1 spectral projectors in `M_2`.
No cube action is adopted. No element of `Aut(M_2)` is selected.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/lock_content_without_m2_action_2026_08_15.py`](../scripts/lock_content_without_m2_action_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Let `c ∈ {0,1}^6` be occupancy of the six directed labels
`{+x,-x,+y,-y,+z,-z}`. Write

```text
n_μ = c_{+μ} - c_{-μ} ∈ {-1,0,1},
S = {μ : n_μ ≠ 0},
k = |n|^2 = |S|.
```

The displayed L1 coordinate is the rational vector `n_L1 := n/3`, so
`k = |3 n_L1|^2` as well. Both `S` and `k` are functions of occupancy
only. They do not consult `Aut(M_2)`.

A later lock on axis `μ` carries the two labels `{+μ,-μ}`. Any
permutation of those two labels sends `n_μ ↦ -n_μ` and leaves `(S,k)`
unchanged. Formation, in the current Record sense that records form and
that a present record locks one admissible local possibility, reads the
occupancy bits. It does not apply an automorphism of `M_2`.

A rank-1 projector

```text
P = (I + u·σ)/2,    u parallel to a displayed n ≠ 0,
```

is a different object. Writing the Bloch image `u·σ` pairs the three
lattice axes with a Pauli triad `{σ_x, σ_y, σ_z}`. That pairing is extra
data: a displayed cube action on `M_2`, not a function of `c`. The
displayed #6272 fork is a permutation of `{σ_x, σ_y, σ_z}`. For every
occupancy with `|S| ≥ 1` there is such a fork sending `P` to a different
matrix, because a supported axis can be swapped onto a different Pauli.
Therefore no occupancy-only map `c ↦ P ∈ M_2` hits those spectral
projectors for all `c`.

The leftover boolean “is a cube action on `M_2` required?” is
object-split, not a single yes/no on the member:

| Object | Cube action on `M_2` |
|---|---|
| formation | not used |
| occupancy label `(S,k)` | not used |
| L1 spectral projectors in `M_2` | used |

The pairing is displayed, not adopted. This note does not pick an
element of `Aut(M_2)`.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Occupancy identities for (S,k) are exact on the finite 64-point cube. The projector claim is an exact pairing-dependence identity for a displayed Bloch image. No cube action, Aut element, or physical lock law is selected."
trace_class: leftover_boolean_object_split
target_claim_id: lock_content_without_m2_action
target_blocker_text: "is a cube action on M_2 required"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the occupancy identities and the pairing-dependence of the displayed projectors; do not promote a single yes/no on the member"
conditional_surface_status: "exact for the declared six-bit occupancy and a displayed axis–Pauli pairing; no adopted frame and no Aut-pick"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premise Boundary

The live axiom memo supplies:

- physical sites as points of the cubic lattice `Z^3`, with nearest-neighbor
  adjacency, standard translations, and proper cubic rotations about each
  site;
- a one-site possibility domain with algebraic presentation `M_2(C)`;
- one fixed nearest-neighbor admissibility rule;
- `Records form.` and `When present, a record locks exactly one admissible
  local possibility.` A readout value is determined by record content alone.

Those sentences distinguish occupancy and locked content from any action of
the proper cubic group on `M_2`. The six-bit occupancy, the integer vector
`n`, the set `S`, the scalar `k`, and the displayed pairing are declared
algebraic test objects. They are not a derivation of the Admissibility
rule, a formation process, or an adopted frame.

This note is not a leftover-character claim about a formation set alone.
It is not a clone of a construction that assumes a Bloch action as given.
The Bloch image is displayed only after the pairing is named as extra.

## Algebra

Index the six directed labels as

```text
c = (c_{+x}, c_{-x}, c_{+y}, c_{-y}, c_{+z}, c_{-z}) ∈ {0,1}^6.
```

There are exactly `64` occupancy patterns. For each axis `μ ∈ {x,y,z}`,

```text
n_μ = c_{+μ} - c_{-μ}.
```

Each component lies in `{-1,0,1}`. Opposite occupancy on one axis
cancels: if `c_{+μ} = c_{-μ}`, then `n_μ = 0` whether that common value
is `0` or `1`. Define

```text
S(c) = {μ : n_μ ≠ 0},    k(c) = n_x^2 + n_y^2 + n_z^2.
```

Because each `n_μ` is in `{-1,0,1}`, one has `n_μ^2 ∈ {0,1}` and
therefore `k(c) = |S(c)| ∈ {0,1,2,3}`. The displayed L1 coordinate is

```text
n_L1(c) := n(c)/3,
```

so `3 n_L1 = n` and `|3 n_L1|^2 = |n|^2 = k`. These identities use only
integer arithmetic on occupancy. No matrix in `M_2` is formed.

A later lock on axis `μ` is the two-label pair `{+μ,-μ}`. Permuting those
two labels exchanges `c_{+μ}` with `c_{-μ}` and replaces `n_μ` by
`-n_μ`. The support set `S` and the quadratic scalar `k` are invariant.
The three axes may be permuted independently: the eight sign patterns
`n ↦ (±n_x, ±n_y, ±n_z)` all share one `(S,k)`.

A displayed axis–Pauli pairing is a bijection

```text
φ : {x,y,z} → {σ_x, σ_y, σ_z}.
```

It is extra data, not a function of `c`. Given `φ` and a nonzero `n`,
the displayed unit Bloch vector and rank-1 projector are

```text
u_φ = n_φ / |n|,    n_φ := n_x φ(x) + n_y φ(y) + n_z φ(z)  as a coefficient
                     triple in the Pauli frame,
P_φ = (I + u_φ · σ)/2.
```

Two pairings that differ by a permutation `π` of the Pauli triad give
coefficient triples related by `π`. Those triples are equal if and only
if `n` is invariant under `π`. They are not equal for a displayed
`n = (1,0,0)` under the transposition `σ_x ↔ σ_y`.

## Theorem 1 — `(S,k)` is occupancy-only

For every `c ∈ {0,1}^6` the pair `(S(c), k(c))` is computed from `n(c)`
by the formulae above. It is unchanged under every permutation of the two
labels on a later lock, and under every combination of such permutations
across the three axes. The construction does not invoke `Aut(M_2)`: no
invertible element of `M_2`, no inner automorphism, and no Pauli triad
enters the formulae.

In particular `k = |n|^2 = |S| = |3 n_L1|^2` is an occupancy scalar. The
k-class of `c` is this integer, not a conjugacy class in `Aut(M_2)`.

## Theorem 2 — rank-1 projectors require a pairing

Let `n ≠ 0` and let `P = (I + u·σ)/2` be a rank-1 projector with `u`
parallel to the displayed `n`. Forming `u·σ` requires a pairing of the
three lattice axes with a Pauli triad. That pairing is not occupancy.

Display the #6272 fork as a permutation of `{σ_x, σ_y, σ_z}`. For every
occupancy with `|S| ≥ 1` there exists such a permutation sending `P` to a
different matrix: choose `μ ∈ S` and transpose `φ(μ)` with a different
Pauli. The resulting coefficient triple is not the original triple, so
the unit vector changes and the projector changes.

Therefore there is no occupancy-only map `c ↦ P ∈ M_2` that hits those
spectral projectors for all `c`. Any candidate function of `c` alone
would have to equal both `P_φ(c)` and `P_{π∘φ}(c)` for a fork `π` that
moves a supported axis. Those two matrices differ on every `|S| = 1`
occupancy, and on every occupancy whose `n` is not invariant under `π`.

When `n` is totally symmetric, for example `n = (1,1,1)`, axis
permutations of the Pauli triad leave that particular `P` unchanged.
That coincidence does not supply an occupancy-only construction: writing
`P` still used a pairing, and the same pairing data still split the
`|S| = 1` patterns. The global map `c ↦ P` remains pairing-dependent.

The pairing is displayed, not adopted. The note does not select a
preferred `φ` and does not pick an element of `Aut(M_2)`.

## Theorem 3 — the boolean is object-split

A cube action on `M_2` is a pairing of lattice axes with a Pauli triad,
equivalently a displayed homomorphism from axis permutations into
`Aut(M_2)` acting by rotation of the Bloch sphere. Theorems 1 and 2
separate three objects on one occupancy `c`:

1. Formation uses the occupancy bits and the Record sentence that a
   present record locks one admissible local possibility. It does not
   use a cube action on `M_2`.
2. The occupancy label `(S,k)` is invariant under later-lock label
   permutation and is independent of any pairing. It does not use a cube
   action on `M_2`.
3. L1's spectral projectors `P_φ = (I + u_φ·σ)/2` use the pairing. A
   cube action on `M_2` is used by those projectors.

The leftover boolean is therefore not a single yes/no on the member. It
collapses by object: not required for formation or for `(S,k)`, required
for the displayed L1 spectral projectors.

## Representative Census

The `64` occupancies partition by `k = |S|` as follows.

| `k` | meaning | count |
|---:|---|---:|
| `0` | every axis cancelled or empty | `8` |
| `1` | exactly one axis occupied unstably | `24` |
| `2` | exactly two axes occupied unstably | `24` |
| `3` | all three axes occupied unstably | `8` |

On each later-lock pair the four bit patterns give `n_μ ∈ {0,0,+1,-1}`
with two cancellations (`00` and `11`). The eight `k = 0` rows are the
products of those cancellations. Every later-lock label swap preserves
the row's `k` class.

For the displayed `n = (1,0,0)` and the identity pairing,

```text
P_id = (I + σ_x)/2 = ((1/2, 1/2), (1/2, 1/2)).
```

The displayed transposition `σ_x ↔ σ_y` sends this to

```text
P_fork = (I + σ_y)/2 = ((1/2, -i/2), (i/2, 1/2)),
```

which is a different matrix. Both are rank-1 projectors. Occupancy of
this row is the same for both matrices; the matrices are not.

## Mutations

1. Replace `k` by a pairing-dependent scalar, for example the first
   Pauli coefficient of `n_φ`. Later-lock label swaps still fix `k`,
   but that substitute is not occupancy-only.
2. Assert a single occupancy-only map `c ↦ P` equal to every displayed
   `P_φ`. Already the `|S| = 1` census rejects it.
3. Treat total symmetry of `n = (1,1,1)` as proof that no pairing is
   needed. The same pairing still splits every `|S| = 1` row.
4. Identify the Pauli permutation with a proper cubic rotation of sites.
   The note does not do this. Proper cubic rotations act on sites of
   `Z^3`; the pairing is extra displayed data in `M_2`.
5. Adopt one `φ` as the physical frame. That would be an Aut-pick,
   which the claim excludes.

## What This Does Not Claim

- No adopted cube action on `M_2` and no Aut-pick.
- No derivation of the Admissibility nearest-neighbor law.
- No formation process, formation site selector, or rate.
- No physical identification of `P_φ` as a locked Record possibility.
- No claim that every transposition moves every `|S| ≥ 1` vector: a
  totally symmetric `n` is fixed by axis permutation, and that fact is
  recorded above rather than denied.
- No leftover-character statement about a formation set alone.
- No assumed Bloch action as a given primitive.
- No dynamics, kinetic symbol, or clock.
- No Qubit rewrite and no axiom edit.

## Proof-Obligation Graph

| Obligation | Disposition |
|---|---|
| define `n`, `S`, `k` from occupancy | closed by the integer formulae |
| identify `k` with `|3 n_L1|^2` | closed by `n_L1 = n/3` |
| prove later-lock label swaps preserve `(S,k)` | closed: `n_μ ↦ -n_μ` |
| prove `(S,k)` does not invoke `Aut(M_2)` | closed: no matrix data enter |
| exhibit the extra pairing for `P = (I+u·σ)/2` | closed by the displayed `φ` |
| prove a Pauli-axis fork changes `P` for `|S| ≥ 1` | closed: swap a supported axis |
| prove no occupancy-only map hits every `P_φ(c)` | closed by the `|S| = 1` split |
| split the leftover boolean by object | closed by Theorem 3 |
| select a physical frame or Aut element | outside the claim |

The obligation graph is acyclic. Every leaf of the bounded algebraic
theorem is closed. Frame adoption is not a proof leaf because it is
expressly not part of the target.

## Framework Boundary

The theorem uses Record only as the current sentences that records form
and that a present record locks one admissible local possibility. It
does not restore a retired scalar collection functional, finite Record
additivity, or a readout value at absence. Current Record assigns no
value to a site without a record.

Proper cubic rotations in the Lattice axiom act on sites of `Z^3`. They
are not identified here with inner automorphisms of `M_2`. The Pauli
triad permutation is not a cubic site rotation. A pairing of axes with
Paulis is extra displayed data.

The Qubit axiom supplies the one-site presentation `M_2(C)`. It does
not supply a preferred Pauli frame or a homomorphism from the cubic
group into `Aut(M_2)`.

## Imports And Claim Boundary

| Item | Role | Provenance / status |
|---|---|---|
| six-bit occupancy `c` | declared test domain | finite `{0,1}^6`; not a physical history |
| `n_μ = c_{+μ}-c_{-μ}` | declared integer difference | occupancy algebra |
| `n_L1 = n/3` | displayed L1 coordinate | rational rescaling; not an adopted Bloch law |
| later-lock label pair `{+μ,-μ}` | declared two-label lock | occupancy labels, not an `M_2` action |
| pairing `φ` | extra data for `u·σ` | displayed, not adopted |
| #6272 fork | displayed Pauli permutation | displayed, not adopted; no Aut-pick |
| `P = (I+u·σ)/2` | displayed rank-1 projector | pairing-dependent; not occupancy-only |

There are no measured, fitted, literature, or observational inputs. A
physical lock law, an adopted frame, and a cube action as a primitive
remain outside the result.

## No-Go Discipline Gate

The negative claim is only this: there is no occupancy-only map that
hits the pairing-dependent rank-1 projectors for all `c`. It is not a
claim that projectors cannot be written, and not a claim that a cube
action is forbidden. The action is extra for one object and unused by
the others.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| occupancy formulae for `(S,k)` | Evaluate `n`, `S`, `k` on all `64` rows and all later-lock label swaps. | Theorem 1: `(S,k)` is invariant and matrix-free. | **ATTEMPTED** |
| identify `k` with an Aut class | Compare `k` across pairings. | `k` is independent of `φ`. | **ATTEMPTED** |
| occupancy-only projector | Demand one `c ↦ P` equal to every displayed `P_φ`. | Theorem 2: already false on every `|S| = 1` row. | **ATTEMPTED** |
| total-symmetry repair | Use invariance of `n = (1,1,1)` to drop the pairing. | Writing `P` still used `φ`; `|S| = 1` still splits. | **ATTEMPTED** |
| formation-set-only leftover | Collapse the boolean to whether a formation set uses Aut. | Theorem 3 keeps three objects. Formation is only one of them. | **ATTEMPTED** |
| assumed Bloch action | Take a cube action on `M_2` as given and ask only about projectors. | The pairing is named as extra, not assumed as a primitive. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one leftover boolean and three objects. The occupancy
invariance and the projector pairing-dependence are independent
certificates: the first does not mention `P`, and the second does not
change `(S,k)`. They do not collapse. Together they force the
object-split rather than a second independent wall.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| `c ∈ {0,1}^6` and `n_μ = c_{+μ}-c_{-μ}` | explicit theorem hypotheses |
| `n_L1 = n/3` | displayed rational coordinate, not a physical L1 law |
| “later lock” | two occupancy labels on one axis; not a dynamics |
| “displayed pairing / #6272 fork” | extra data; displayed, not adopted |
| “cube action on `M_2`” | name for the displayed pairing; not a cubic site rotation |
| Record locks one | cited current axiom sentence; no process or rate |
| Aut-pick | excluded, not used |

## Review Record

The source leftover was the single boolean “is a cube action on `M_2`
required?”. Review splits that boolean by object. Formation and the
occupancy scalars `(S,k)` do not use Aut. Rank-1 projectors in `M_2`
do. The pairing is displayed, not adopted. No Aut-pick is performed.
