---
claim_id: lock_content_leftover_frame_p_odd_vs_l1chi_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the six-neighbor occupancy star, whether leftover-frame lock-content section f is P-odd while L1 occupancy formation is P-even is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/lock_content_leftover_frame_p_odd_vs_l1chi_2026_08_15.py
---

# Leftover-Frame Lock-Content Section Versus L1 Occupancy Achirality (Bounded Theorem)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact census of displayed L1 formation `n = d/3` and of
leftover-frame-positive lock-content section `f` on the six-neighbor
occupancy star `{0,1}^6`. Occupancy formation is two-letter and
`P`-even. Lock-content `f` is named as in the leftover-frame-positive
section of the July-3 pair. Uniqueness is not required. The `P`-parity
split is displayed, not adopted. Do not attach L1. Do not write `f` or
V−A into Admissibility. Do not reopen `color-unital-m3`. No occupancy
step on a new spatial patch.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/lock_content_leftover_frame_p_odd_vs_l1chi_2026_08_15.py`](../scripts/lock_content_leftover_frame_p_odd_vs_l1chi_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
and the July-3 classification
[`ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md`](ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md).
Declared audit inputs are this note and the axiom memo only.

## Result Up Front

Work on one six-neighbor star. Order the axis directions

```text
D = {+x, -x, +y, -y, +z, -z}.
```

An occupancy coloring is a tuple `c ∈ {0,1}^6`. Write
`d_μ = c_{+μ} − c_{−μ}` and `n = d/3`. Displayed L1 formation is
`n ≠ 0`. Inversion `P` swaps `+μ` with `−μ` and sends `n → −n`, so
`{c : n(c) ≠ 0}` is `P`-invariant. July-3 theorem 2 applies: a
proper-covariant two-letter openness rule is automatically full-cubic
covariant. Occupancy formation is automatically achiral.

Letters of lock content are `{0, +, −}` with `0` empty. Completions of
an occupancy `σ` and an age bit `b` are the July-3 pair members that
match occupancy `σ` and write opposite letters on the unique full axis
according to `b`. The leftover-frame sign of a completion is the
determinant of the ordered triple of directions (leftover `+`, leftover
`−`, full-axis `+` letter). Leftover-frame-positive section `f` takes a
completion of sign `+1`. Uniqueness is not required.

On each of the 64 occupancy tuples the lock-content bit is

```text
f(c) = 1  iff  leftover-frame-positive section exists at occupancy c
               for some age bit b ∈ {0,1}.
```

This is named lock content, not occupancy `n ≠ 0`. The runner reports

```text
N_form = 56,    N_P_form = 56,    N_both = 56
N_f    = 12,    N_P_f    = 12,    N_both = 12.
```

The occupancy set `{c : f(c)=1}` is `P`-invariant, so it is not `P`-odd
as a set of 6-tuples. The lock-content section itself is `P`-odd: `P`
sends leftover-frame sign `+1` to sign `−1`, and the 24 leftover-frame-
positive 3-letter colorings are disjoint from their inversion images.
July-3 theorem 2 does not apply to that 3-letter section. Occupancy
formation is automatically achiral; lock-content `f` is not.

Displayed, not adopted. Do not write f or V−A into Admissibility. Do
not attach L1. Qubit remains `M_2(C)`. No axiom edit.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact enumeration of the 64 occupancy tuples establishes that displayed L1 formation is a two-letter P-even openness rule, that the occupancy fire-set of leftover-frame-positive f is P-invariant with N_f=12, and that the lock-content section itself is P-odd on the July-3 pair. Nothing is adopted."
trace_class: negative_route_pruning
target_claim_id: lock_content_leftover_frame_p_odd_vs_l1chi
target_blocker_text: "is leftover-frame lock-content section f P-odd on the same 64 occupancy tuples while L1 occupancy formation is P-even"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the 64-tuple census; do not attach L1 or write f or V-A into Admissibility"
conditional_surface_status: "exact for displayed n≠0 and leftover-frame-positive f on {0,1}^6; physical rule selection remains unclaimed"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: "V-A / P-odd is used only as the displayed comparison language; it is not derived"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Target And Proof Obligations

**Exact target.** On the six-neighbor occupancy star, report
`N_form`, `N_P_form`, `N_both` for displayed L1 formation `n ≠ 0`;
report `N_f`, `N_P_f`, `N_both` for leftover-frame lock-content section
`f`; say whether `{c : f(c)=1}` is `P`-odd (not `P`-invariant) as a set
of occupancy 6-tuples; and say whether occupancy formation is
automatically achiral while lock-content `f` is or is not. Displayed,
not adopted.

| Obligation | Disposition |
|---|---|
| occupancy `{c : n ≠ 0}` is `P`-invariant | proved here in Theorem 1 |
| census `N_form = N_P_form = N_both = 56` | proved here in Theorem 1 |
| July-3 theorem 2 applies to occupancy | cited and locally re-earned in Theorem 1 |
| lock-content bit `f` on the same 64 rows | proved here in Theorem 2 |
| census `N_f = N_P_f = N_both = 12` | proved here in Theorem 2 |
| occupancy `{c : f(c)=1}` is not `P`-odd | proved here in Theorem 2 |
| lock-content section is `P`-odd on the pair | proved here in Theorem 2 |
| occupancy automatically achiral; `f` is not | proved here in Theorem 3 |
| no attachment, no Admissibility rewrite | stated here and gated |

Boundary cases are not hidden. The eight colorings with `n = 0` do not
form. Occupancies without a unique full axis have `f(c) = 0`. Each
occupancy with `f(c) = 1` has two leftover-frame-positive completions,
one per age bit; uniqueness is not required. Occupancy evolution on a
new spatial patch is outside the target. No terminal lemma equivalent
to the target is left open.

## Inputs And Support Inventory

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  the nearest-neighbor Admissibility covariance sentence (proper cubic
  rotations), the reading note that Admissibility does not supply the
  formation site, the Record sentence that a readout value is
  determined by record content alone, and the Qubit presentation
  `M_2(C)`. As the registered `minimal_axioms` premise, it is not a
  bounded-status source.
- The July-3 classification supplies theorem 2 (openness-level patterns
  are automatically achiral) and theorem 3 (chirality requires three
  condition values; one chiral pair at `k = 3`). Those statements are
  cited as parents. The two-letter half is re-earned on this star. The
  pair is rebuilt as the union of proper orbits that are not
  `P`-invariant; the orbit census is not dumped.
- Occupancy bits, the formula `n = d/3`, the predicate `n ≠ 0`, and
  leftover-frame-positive section `f` are displayed mathematical
  hypotheses for this note. They are not a derived physical selector
  and are not attached as the framework's fixed rule.
- No measured, fitted, scale, or other phenomenological value is used.
- No new spatial patch is introduced.

## Exact Objects

Directions, inversion, dipole, and formation:

```text
c = (c_{+x}, c_{-x}, c_{+y}, c_{-y}, c_{+z}, c_{-z}) ∈ {0,1}^6
d_μ = c_{+μ} − c_{−μ} ∈ {−1, 0, +1}
n_μ = d_μ / 3 ∈ {−1/3, 0, +1/3}
f_L1(c) = 1  iff  n ≠ 0
P(c) = (c_{-x}, c_{+x}, c_{-y}, c_{+y}, c_{-z}, c_{+z})
n(P(c)) = −n(c)
```

Lock-content letters `{0, +, −}` encode as `0 ↦ 0`, `+ ↦ 1`, `− ↦ 2`.
Occupancy of a 3-letter coloring is its support. A unique full axis is
the unique axis with both slots occupied. Age bit `b` writes opposite
letters on that axis. Leftover-frame sign is

```text
sgn = det( leftover +, leftover −, full-axis + letter ).
```

Leftover-frame-positive `f` is a completion with `sgn = +1`. The
occupancy lock-content bit is `f(c) = 1` iff such a completion exists
for some `b`.

The live Admissibility, Record, and Qubit sentences, quoted and not
rewritten:

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> Read with Record, the distribution concerns which possibility a forming record locks, conditional
> on formation at that site; it does not supply the formation site, probability,
> or rate.

> A readout value is determined by record content alone.

> The full one-site possibility domain has algebraic presentation `M_2(C)`.

## Theorem 1 — occupancy `{c : n ≠ 0}` is `P`-invariant

The occupancy alphabet is `{0,1}`. Inversion swaps each pair
`(+μ, −μ)`, so each `d_μ` changes sign and `n(P(c)) = −n(c)`. Therefore
`n(c) ≠ 0` if and only if `n(P(c)) ≠ 0`. The set `{c : n(c) ≠ 0}` is
`P`-invariant.

The zero set is the product over three axes of the balanced pairs
`{(0,0), (1,1)}`, hence `2^3 = 8` tuples. The complementary formation
set has 56 members. Because the set is `P`-invariant,

```text
N_form = |{c : n(c) ≠ 0}| = 56
N_P_form = |{c : n(P(c)) ≠ 0}| = 56
N_both = |{c : n(c) ≠ 0 and n(P(c)) ≠ 0}| = 56.
```

July-3 theorem 2 states that every proper-covariant rule depending
only on the recorded/open pattern of the six neighbors is covariant
under the full cubic group. The runner re-earns the supporting fact:
each of the 64 two-letter colorings is proper-equivalent to its
`P`-image. Displayed L1 formation is automatically achiral.

## Theorem 2 — lock-content `f` on the same 64 rows

Leftover-frame-positive section `f` is a 3-letter object. Evaluated as
a lock-content bit on each occupancy 6-tuple, `f(c) = 1` exactly on the
twelve occupancies that admit a unique full axis and a leftover mixed
`{+,−}` pair — the perpendicular weight-4 masks. The runner finds

```text
N_f = 12,    N_P_f = 12,    N_both = 12.
```

`P` permutes those twelve among themselves, so `{c : f(c)=1}` is
`P`-invariant as a set of occupancy 6-tuples. It is not `P`-odd in the
sense “not `P`-invariant”. The set is not `{c : n(c) ≠ 0}`.

The lock-content section itself is a different object. The July-3 pair
has 48 colorings, 24 of leftover-frame sign `+1` and 24 of sign `−1`.
Sign is `P`-odd: `sgn(P(λ)) = −sgn(λ)`. The leftover-frame-positive
set is disjoint from its inversion image. Each occupancy with
`f(c) = 1` has two leftover-frame-positive completions (one per age
bit); uniqueness is not required. Those 24 colorings push forward onto
exactly the twelve occupancy tuples of the fire-set.

## Theorem 3 — occupancy formation is automatically achiral; lock-content `f` is not

Occupancy formation is a two-letter `P`-invariant openness predicate.
July-3 theorem 2 applies; it is automatically achiral.

Lock-content leftover-frame-positive `f` is a section of the unique
July-3 `k = 3` chiral pair. July-3 theorem 2 does not apply: the
alphabet has three letters, not two. The section is `P`-odd. It is not
automatically achiral.

The occupancy fire-set of `f` being `P`-invariant does not make the
3-letter section automatically achiral. That fire-set is a two-letter
projection. The section is lock content.

Displayed, not adopted. Do not write f or V−A into Admissibility. Do
not attach L1. Qubit remains `M_2(C)`. No axiom edit.

## Mutations

1. Identify occupancy `{c : f(c)=1}` with `{c : n(c) ≠ 0}`: the
   censuses are 12 and 56.
2. Treat occupancy `{c : f(c)=1}` as `P`-odd: the set is
   `P`-invariant, with `N_f = N_P_f = N_both = 12`.
3. Treat the occupancy fire-set as making lock-content `f`
   automatically achiral: the 3-letter section remains `P`-odd.
4. Require a unique leftover-frame-positive completion per occupancy:
   each fire-set occupancy has two, one per age bit.
5. Adopt `f` or write `f` / V−A into Admissibility: refused.
6. Run the occupancy step on a new spatial patch: refused; the census
   is the 64-tuple star only.

## What This Does Not Claim

- Do not attach L1 as the framework's fixed physical rule.
- Do not write `f` or V−A into Admissibility.
- Do not adopt a chirality bit.
- Do not reopen `color-unital-m3`.
- No occupancy step on a new spatial patch.
- No formation rate, no host rebuild, no hop-cost filter.
- Uniqueness of leftover-frame-positive completion is not required
  and is not claimed.

## No-Go Discipline Gate

The negative claim is only this: on the six-neighbor occupancy star,
displayed L1 formation is a two-letter automatically achiral rule,
while leftover-frame lock-content section `f` is not automatically
achiral. Occupancy `{c : f(c)=1}` is not itself `P`-odd. It is not a
claim that weak chirality is impossible in the framework, and it is
not a claim that some other, unstated content rule is the physical
rule.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| identify `f` with `n ≠ 0` | Treat leftover-frame occupancy fire as L1 formation. | Theorem 2 and runner check `thm2-f-is-not-n-nonzero` separate 12 from 56. | **ATTEMPTED** |
| occupancy fire-set is `P`-odd | Read `{c : f(c)=1}` as not `P`-invariant. | Theorem 2 and check `thm2-occupancy-f-set-not-p-odd` keep `N_f = N_P_f = N_both = 12`. | **ATTEMPTED** |
| fire-set implies automatic achirality of `f` | Apply July-3 theorem 2 to the occupancy projection and stop. | Theorem 3 and check `thm3-lock-content-not-automatically-achiral` keep the 3-letter section `P`-odd. | **ATTEMPTED** |
| unique completion | Demand one leftover-frame-positive coloring per occupancy. | Theorem 2 and check `thm2-uniqueness-not-required` find two per fire-set occupancy. | **ATTEMPTED** |
| adopt or rewrite | Write `f` or V−A into Admissibility, or attach L1. | Theorem 3 and check `thm3-displayed-not-adopted` refuse the rewrite. | **ATTEMPTED** |
| new spatial patch | Evolve occupancy on a new patch and read `f` there. | Check `no-new-spatial-patch`; the census is the 64-tuple star. | **ATTEMPTED** |

### N2 — wall independence and collapse

There are two conclusions, not a six-wall headline. Occupancy
automatic achirality is one conclusion (Theorem 1). Lock-content `f`
not being automatically achiral is the second (Theorems 2–3). The
fire-set `P`-invariance, the 12-versus-56 split, and uniqueness
refusal are certificates, not extra walls. Attachment refusal is a
scope marker.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| occupancy achirality / lock-content not achiral | no: a `P`-even openness rule does not classify a 3-letter section | no: a `P`-odd section does not by itself classify two-letter formation | independent conclusions on two alphabets |
| occupancy fire-set `P`-invariance / content `P`-oddness | no | no | projection versus section |
| 12-versus-56 split / uniqueness | no | no | supporting certificates, not walls |

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “displayed L1 formation” and `n = d/3` | explicit theorem hypothesis; not a derived physical selector |
| leftover-frame-positive section `f` | explicit named displayed section; rebuilt from the July-3 pair |
| occupancy alphabet `{0,1}` | explicit theorem hypothesis |
| July-3 theorems 2 and 3 | cited parent classification; two-letter half re-earned here |
| “automatically achiral” | July-3 theorem 2 applied only to the two-letter occupancy rule |
| “Do not attach L1” | scope refusal, not a hidden residual |
| Admissibility proper covariance | cited registered axiom premise |
| Admissibility does not supply formation | cited reading note; used only as a boundary |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | proper-only covariance of the named rule | Admissibility names proper cubic rotations | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:67` | formation site supplied by Admissibility | reading note: formation site is not supplied | yes; boundary stays open |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:82` | readout from lock content | readout is determined by record content alone | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:47` | Qubit presentation | `M_2(C)`; Qubit remains `M_2(C)` | yes |
| `scripts/lock_content_leftover_frame_p_odd_vs_l1chi_2026_08_15.py:274` | formation census | `N_form = 56` | yes |
| `scripts/lock_content_leftover_frame_p_odd_vs_l1chi_2026_08_15.py:275` | `P`-image and intersection census | `N_P_form = N_both = 56` | yes |
| `scripts/lock_content_leftover_frame_p_odd_vs_l1chi_2026_08_15.py:287` | `P`-invariance of the formation set | `{c : n(c) ≠ 0}` is `P`-invariant | yes |
| `scripts/lock_content_leftover_frame_p_odd_vs_l1chi_2026_08_15.py:312` | occupancy lock-content census | `N_f = N_P_f = N_both = 12` | yes |
| `scripts/lock_content_leftover_frame_p_odd_vs_l1chi_2026_08_15.py:316` | occupancy fire-set `P`-oddness | `{c : f(c)=1}` is `P`-invariant, not `P`-odd | yes |
| `scripts/lock_content_leftover_frame_p_odd_vs_l1chi_2026_08_15.py:343` | lock-content section `P`-oddness | leftover-frame-positive set is disjoint from its `P`-image | yes |

No evidence citation is used to claim that L1 or `f` is the physical
rule, or that Admissibility has been rewritten.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: all 64 occupancy tuples | each has `n = d/3`, forms iff `n ≠ 0`, and a leftover-frame lock-content bit |
| per site | yes: one six-neighbor star | no host rebuild; no other site is used |
| per mode | yes: two-letter occupancy versus three-letter leftover-frame-positive `f` | occupancy is automatically achiral; lock-content `f` is not |
| per block | yes: 56/56/56 and 12/12/12 censuses | occupancy fire-set is `P`-even; content section is `P`-odd |
| lattice wide | no | no occupancy step on a new spatial patch |

The runner prints the same five resolution statements verbatim.

### N6 — partial closure and primitive scan

The primitive registry at `docs/audit/data/axiom_premise_nodes.json` was
checked. The only dependency used is the registered `minimal_axioms`
node. Approved primitives `scale_reference_primitive`,
`kinetic_isotropy_primitive`, and `realized_state_primitive` are not
used. Open derivation obligations on occupancy grain and readout are
not this star census. July-3 theorems 2 and 3 are cited parent
mathematics, not new primitives. None is reclassified as an import or
wall.

Two partial-closure mechanisms were tested rather than suppressed.
Identifying occupancy `{c : f(c)=1}` with a `P`-odd set would have made
lock-content `P`-odd already at two letters; that set is `P`-invariant.
Treating that `P`-invariance as automatic achirality of `f` would have
erased the 3-letter section; the section remains `P`-odd.

### N7 — hostile steelman

The strongest objection is that leftover-frame-positive `f` is already
classified by its occupancy fire-set: that set is `P`-invariant, every
two-letter coloring is proper-equivalent to its `P`-image, and July-3
theorem 2 would then make `f` automatically achiral. That objection
names the occupancy projection, not the lock-content section. The
section is a 3-letter coloring of leftover-frame sign `+1`. Inversion
flips that sign, and the positive set is disjoint from its inversion
image. To overturn the negative claim the objection would have to show
that the 3-letter section is proper-equivalent to its `P`-image, or
that leftover-frame sign is `P`-even. Both fail on the rebuilt pair.

### N8 — cross-cycle echo

Repository search found three nearby landed mechanisms. They are
context, not load-bearing dependencies, and the star census is
recomputed here.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md` | two-letter openness is automatically achiral; chirality starts at `k = 3` | applied to displayed `n ≠ 0`; lock-content `f` is kept on the `k = 3` pair |
| `docs/ADMISSIBILITY_SUPPORT_CONSTRAINS_CONTENT_NOT_FORMATION_SITE_BOUNDED_THEOREM_NOTE_2026-08-13.md` | Admissibility constrains content, not the formation site | formation and lock-content bits are displayed predicates; neither is written into Admissibility |
| `docs/ONLY_CUBIC_INVARIANT_BLOCH_VECTOR_IS_ZERO_BOUNDED_THEOREM_NOTE_2026-08-13.md` | cubic invariants can vanish while a directed object does not | occupancy formation can be `P`-even while a lock-content section is `P`-odd |

No earlier mechanism attaches L1 or writes leftover-frame-positive `f`
into Admissibility. This note does not reopen `color-unital-m3`.

No-Go Discipline disposition: **PASS** for the algebraic negative
boundary stated at the start of this section.

## Live Parent Quotes

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> it does not supply the formation site, probability,
> or rate.

> A readout value is determined by record content alone.

> For the two-letter alphabet (recorded/open — content-blind conditions),
> every coloring of the six directions is proper-equivalent to its
> `P`-image (all 64, exhaustively; Burnside orbit counts agree at 10 and
> 10). Every proper-covariant rule depending only on the openness
> pattern is therefore automatically covariant under the full cubic
> group. **A chiral admissibility rule cannot live at the openness
> level**; chirality requires distinguishable record contents.

> At `k = 2` there is no chiral pair (Theorem 2); at `k = 3` there is
> exactly one, whose members are the handed fully-mixed patterns

## Runner Contract

The companion runner enumerates all 64 occupancy tuples, computes
`n = d/3` over `Fraction`, reports `N_form`, `N_P_form`, and
`N_both`, rebuilds leftover-frame-positive section `f` from the July-3
pair, reports `N_f`, `N_P_f`, and `N_both`, checks that occupancy
`{c : f(c)=1}` is `P`-invariant, checks that the lock-content section
is `P`-odd, and verifies the refusal and no-go gate. Declared audit
inputs are this note and the axiom memo. No runner cache is written.
No occupancy step is run on a new spatial patch.
