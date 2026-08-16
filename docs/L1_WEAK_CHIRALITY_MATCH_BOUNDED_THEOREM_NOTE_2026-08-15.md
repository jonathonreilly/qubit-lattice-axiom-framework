---
claim_id: l1_weak_chirality_match_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the six-neighbor occupancy star, whether displayed L1 formation (n≠0) is a two-letter automatically achiral rule, and whether that matches observed weak P-violation, is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/l1_weak_chirality_match_2026_08_15.py
---

# Displayed L1 Formation Is Automatically Achiral And Does Not Produce Observed Weak Chirality

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact two-letter census of displayed L1 formation
`n = d/3`, form iff `n ≠ 0`, on the six-neighbor occupancy star
`{0,1}^6`. July-3 theorem 2 applies; July-3 theorem 3 does not.
The comparison with observed weak `P`-violation is displayed, not
adopted. Do not attach L1. Do not write L1 or V−A into Admissibility.
Do not adopt a chirality bit. No occupancy step on a new spatial patch.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/l1_weak_chirality_match_2026_08_15.py`](../scripts/l1_weak_chirality_match_2026_08_15.py)
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
`d_μ = c_{+μ} − c_{−μ}` and `n = d/3`, so each component of `n`
lies in `{−1/3, 0, +1/3}`. Displayed L1 formation is the predicate

```text
f_L1(c) = 1  iff  n(c) ≠ 0.
```

This is a two-letter function of occupancy bits. Lock labels do not
feed `n`. Inversion `P` swaps `+μ` with `−μ` and sends `n → −n`, so
the formation set `{c : n(c) ≠ 0}` is `P`-invariant. July-3 theorem 2
therefore applies: every proper-covariant rule that depends only on
the recorded/open pattern is automatically full-cubic covariant.
Displayed L1 formation is automatically achiral.

The neighbor alphabet has two letters, not three. July-3 theorem 3's
minimal chiral channel therefore does not live here. Among the 64
occupancy tuples the runner reports

```text
N_form = 56,    N_P_form = 56,    N_both = 56.
```

Observed weak chirality is a `P`-odd / V−A grading. A `P`-even
formation indicator cannot equal a `P`-odd grade except at zero.
Automatically achiral L1 formation does not produce that grading.
The match/mismatch is displayed only.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact enumeration of the 64 occupancy tuples establishes that displayed L1 formation is a two-letter P-even openness rule, that July-3 theorem 2 applies, and that the displayed comparison with a P-odd / V-A grade is a mismatch. Nothing is adopted."
trace_class: negative_route_pruning
target_claim_id: l1_weak_chirality_match
target_blocker_text: "does displayed L1 produce observed weak chirality"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the star census; do not attach L1 or write V-A into Admissibility"
conditional_surface_status: "exact for the displayed n≠0 predicate on {0,1}^6; physical rule selection and weak phenomenology remain unclaimed"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: "V-A / P-odd is used only as the displayed comparison target; it is not derived"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Target And Proof Obligations

**Exact target.** On the six-neighbor occupancy star, prove that
displayed L1 formation `n ≠ 0` is a two-letter openness-level rule
whose formation set is `P`-invariant, hence automatically achiral by
July-3 theorem 2; that the neighbor alphabet is not a 3-value chiral
channel; that the 64-tuple census is `N_form = N_P_form = N_both = 56`;
and that this `P`-even predicate does not produce a `P`-odd / V−A
grading. Report the match/mismatch. Displayed, not adopted.

| Obligation | Disposition |
|---|---|
| `n = d/3` and form iff `n ≠ 0` | proved here in Theorem 1 |
| lock labels do not feed `n` | proved here in Theorem 1 |
| formation set is `P`-invariant | proved here in Theorem 1 |
| July-3 theorem 2 applies | cited and locally re-earned in Theorem 1 |
| two letters, not three; census 56/56/56 | proved here in Theorem 2 |
| `f_L1` is not Hamming | proved here in Theorem 2 |
| `P`-even formation does not produce V−A | proved here in Theorem 3 |
| no attachment, no Admissibility rewrite | stated here and gated |

Boundary cases are not hidden. The eight colorings with `n = 0` (each
axis balanced: both sides empty or both occupied) do not form. The
Hamming-nonzero set has 63 members and is a different predicate.
A 3-letter content coloring is a different alphabet and is not this
star. Occupancy evolution on a new spatial patch is outside the
target. No terminal lemma equivalent to the target is left open.

## Inputs And Support Inventory

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  the nearest-neighbor Admissibility covariance sentence (proper cubic
  rotations), the reading note that Admissibility does not supply the
  formation site, and the Record sentence that a readout value is
  determined by record content alone. As the registered
  `minimal_axioms` premise, it is not a bounded-status source.
- The July-3 classification supplies theorem 2 (openness-level patterns
  are automatically achiral) and theorem 3 (chirality requires three
  condition values). Those two statements are cited as parents and
  the two-letter half is re-earned on this star by the runner.
- Occupancy bits, the formula `n = d/3`, and the predicate `n ≠ 0` are
  displayed mathematical hypotheses for this note. They are not a
  derived physical selector and are not attached as the framework's
  fixed rule.
- Observed weak chirality (V−A / `P`-odd) is an admitted comparison
  target only. It is not derived and is not written into Admissibility.
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

A lock-labeled star is a pair `(c, λ)` with `λ ∈ {0,1,2}^6`. The map
`(c, λ) ↦ n` discards `λ`. Hamming weight is `h(c) = Σ_i c_i` and is
not the formation predicate.

The live Admissibility and Record sentences, quoted and not rewritten:

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> Read with Record, the distribution concerns which possibility a forming record locks, conditional
> on formation at that site; it does not supply the formation site, probability,
> or rate.

> A readout value is determined by record content alone.

## Theorem 1 — two-letter openness, `P`-invariant, automatically achiral

The occupancy alphabet is `{0,1}`. The value `n(c)` is assembled from
the three axis differences of those bits and does not consult lock
labels: if `λ` and `λ'` are any two labelings of the same `c`, then
`n(c, λ) = n(c, λ') = n(c)`. Witness: `c = (1,0,0,0,0,0)` with three
distinct labelings all return `n = (1/3, 0, 0)`.

Inversion swaps each pair `(+μ, −μ)`, so each `d_μ` changes sign and
`n(P(c)) = −n(c)`. Therefore `n(c) ≠ 0` if and only if `n(P(c)) ≠ 0`.
The set `{c : n(c) ≠ 0}` is `P`-invariant. Each proper cubic rotation
permutes the three axes and preserves the vanishing of `n`, so `f_L1`
is proper-covariant.

July-3 theorem 2 states that every proper-covariant rule depending
only on the recorded/open pattern of the six neighbors is covariant
under the full cubic group: a chiral admissibility rule cannot live
at the openness level. The runner re-earns the supporting B1 fact on
this alphabet: each of the 64 two-letter colorings is
proper-equivalent to its `P`-image. Displayed L1 formation is
therefore automatically achiral.

## Theorem 2 — not a 3-value chiral channel; census 56/56/56

July-3 theorem 3 places the first chiral pair at a 3-letter condition
alphabet. The occupancy alphabet here has two letters, not three, so
that channel is not present. `f_L1` is not a 3-value content rule.

The 64 occupancy tuples split by `n = 0` versus `n ≠ 0`. The zero set
is the product over three axes of the balanced pairs `{(0,0), (1,1)}`,
hence `2^3 = 8` tuples. The complementary formation set has 56
members. Because the set is `P`-invariant,

```text
N_form = |{c : n(c) ≠ 0}| = 56
N_P_form = |{c : n(P(c)) ≠ 0}| = 56
N_both = |{c : n(c) ≠ 0 and n(P(c)) ≠ 0}| = 56.
```

Hamming-nonzero is a different set: `c_* = (1,1,0,0,0,0)` has
`h(c_*) = 2 ≠ 0` and `n(c_*) = 0`, so it is Hamming-nonzero and not
an L1 former. Thus `f_L1` is `n ≠ 0`, not Hamming.

## Theorem 3 — displayed mismatch with observed weak chirality

Observed weak chirality is a `P`-odd / V−A grading: it distinguishes
a configuration from its inversion image. Displayed L1 formation is
`P`-even: `f_L1(P(c)) = f_L1(c)`. The only function that is both
`P`-even and `P`-odd is zero. The comparison grade `χ(c) = n_x(c)` is
`P`-odd and nonzero on `c = (1,0,0,0,0,0)`, so it cannot equal
`f_L1`. Automatically achiral L1 formation does not produce that
grading.

This is a displayed match/mismatch only. Do not adopt a chirality
bit. Do not attach L1. Do not write L1 or V−A into Admissibility.
The axioms name a proper-covariant nearest-neighbor rule and do not
supply the formation site.

## Mutations

1. Replace `f_L1` by Hamming-nonzero: `c_* = (1,1,0,0,0,0)` lies in
   one set and not the other.
2. Let lock labels feed `n`: distinct labels on a fixed occupancy
   still return the same `n`.
3. Treat the occupancy alphabet as a 3-value chiral channel: the
   alphabet has two letters.
4. Identify `f_L1` with a `P`-odd / V−A grade: even cannot equal odd
   except at zero.
5. Adopt a chirality bit or write L1 / V−A into Admissibility: refused.
6. Run the occupancy step on a new spatial patch: refused; the census
   is the 64-tuple star only.

## What This Does Not Claim

- Do not attach L1 as the framework's fixed physical rule.
- Do not write L1 or V−A into Admissibility.
- Do not adopt a chirality bit.
- Do not reopen `born-compiler` or `color-unital-m3`.
- Do not claim a 3-letter content channel on this star.
- No occupancy step on a new spatial patch.
- No formation rate, no Hamming formation rule, no lock-label
  feeding of `n`.
- Observed V−A is a comparison target, not a derived law.

## No-Go Discipline Gate

The negative claim is only this: displayed L1 formation on the
six-neighbor occupancy star is a two-letter automatically achiral
rule, and that rule does not produce a `P`-odd / V−A grading. It is
not a claim that weak chirality is impossible in the framework, and
it is not a claim that some other, unstated 3-letter content rule is
impossible.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| Hamming formation | Identify `f_L1` with Hamming-nonzero. | Theorem 2 and runner check `thm2-not-hamming` separate the sets at `c_* = (1,1,0,0,0,0)`. | **ATTEMPTED** |
| lock-label feeding | Let record content change `n`. | Theorem 1 and check `thm1-lock-labels-do-not-feed-n` show `n` discards labels. | **ATTEMPTED** |
| 3-value chiral channel | Treat occupancy as July-3 theorem 3's `k = 3` alphabet. | Theorem 2 and check `thm2-alphabet-not-three` keep two letters. | **ATTEMPTED** |
| even/odd identification | Set `f_L1` equal to a `P`-odd / V−A grade. | Theorem 3 and checks `thm3-even-cannot-equal-odd` / `thm3-mismatch-displayed` reject the identification. | **ATTEMPTED** |
| adopt or rewrite | Adopt a chirality bit or write L1 / V−A into Admissibility. | Theorem 3 and check `no-attachment` refuse the rewrite. | **ATTEMPTED** |
| new spatial patch | Evolve occupancy on a new patch and read chirality there. | Check `no-new-spatial-patch`; the census is the 64-tuple star. | **ATTEMPTED** |

### N2 — wall independence and collapse

There are two conclusions, not a six-wall headline. Automatic
achirality is one conclusion (Theorems 1–2). Displayed mismatch with
a `P`-odd grade is the second (Theorem 3). The Hamming, lock-label,
and `k = 3` attacks are certificates that the first conclusion's
hypotheses hold, not extra walls. Attachment refusal is a scope
marker, not a third wall.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| automatic achirality / V−A mismatch | yes, once formation is known to be `P`-even | no: a mismatch does not by itself classify the openness alphabet | second conclusion uses the first |
| Hamming rejection / two-letter alphabet | no | no | supporting certificates, not walls |
| lock-label blindness / two-letter alphabet | no | no | supporting certificates, not walls |

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “displayed L1 formation” and `n = d/3` | explicit theorem hypothesis; not a derived physical selector |
| occupancy alphabet `{0,1}` | explicit theorem hypothesis |
| July-3 theorems 2 and 3 | cited parent classification; two-letter half re-earned here |
| “automatically achiral” | July-3 theorem 2 applied to this `P`-invariant openness rule |
| “observed weak chirality / V−A” | admitted comparison target only; not derived |
| “Do not attach L1” | scope refusal, not a hidden residual |
| Admissibility proper covariance | cited registered axiom premise |
| Admissibility does not supply formation | cited reading note; used only as a boundary |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | proper-only covariance of the named rule | Admissibility names proper cubic rotations | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:67` | formation site supplied by Admissibility | reading note: formation site is not supplied | yes; boundary stays open |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:82` | readout from lock content | readout is determined by record content alone; `n` still ignores labels | yes |
| `scripts/l1_weak_chirality_match_2026_08_15.py:220` | formation census | `N_form = 56` | yes |
| `scripts/l1_weak_chirality_match_2026_08_15.py:222` | `P`-image and intersection census | `N_P_form = N_both = 56` | yes |
| `scripts/l1_weak_chirality_match_2026_08_15.py:231` | `P`-invariance of the formation set | `{c : n(c) ≠ 0}` is `P`-invariant | yes |
| `scripts/l1_weak_chirality_match_2026_08_15.py:271` | lock labels feeding `n` | distinct labels give the same `n` | yes |
| `scripts/l1_weak_chirality_match_2026_08_15.py:284` | Hamming formation | `f_L1` is `n ≠ 0`, not Hamming-nonzero | yes |
| `scripts/l1_weak_chirality_match_2026_08_15.py:317` | V−A identification | automatically achiral formation does not produce the `P`-odd grade | yes |

No evidence citation is used to claim that L1 is the physical rule,
that V−A is derived, or that Admissibility has been rewritten.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: all 64 occupancy tuples | each has `n = d/3` and forms iff `n ≠ 0` |
| per site | yes: one six-neighbor star | lock labels do not feed `n`; no other site is used |
| per mode | yes: two-letter openness versus a displayed `P`-odd grade | the even indicator cannot equal the odd grade |
| per block | yes: the 56/56/56 census and the Hamming comparison | Hamming-nonzero is a different set |
| lattice wide | no | no occupancy step on a new spatial patch |

The runner prints the same five resolution statements verbatim.

### N6 — partial closure and primitive scan

The primitive registry at `docs/audit/data/axiom_premise_nodes.json` was
checked. The only dependency used is the registered `minimal_axioms`
node. July-3 theorems 2 and 3 are cited parent mathematics, not new
primitives. None is reclassified as an import or wall.

Two partial-closure mechanisms were tested rather than suppressed.
Hamming-nonzero is a well-defined `P`-even occupancy predicate, and a
3-letter content coloring is the July-3 chiral threshold. The first
is a different set from `{c : n(c) ≠ 0}`. The second is a different
alphabet. Neither turns displayed L1 formation into a `P`-odd grade.

### N7 — hostile steelman

The strongest objection is that `n` itself is a `P`-odd 3-vector, so
the formation rule “secretly carries” the V−A grade as the sign of
`n`. That objection names a different object. Formation is the
predicate `n ≠ 0`, which is the vanishing of that vector and is
`P`-even. The sign of `n` is not consulted, is not adopted as a
chirality bit, and is used here only as a comparison grade `χ = n_x`
to exhibit the mismatch. To overturn the negative claim the objection
would have to show that `f_L1` itself is `P`-odd, or that lock labels
change `n`. Both fail on the 64-tuple star.

### N8 — cross-cycle echo

Repository search found three nearby landed mechanisms. They are
context, not load-bearing dependencies, and the star census is
recomputed here.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md` | two-letter openness is automatically achiral; chirality starts at `k = 3` | applied to displayed `n ≠ 0`; the two-letter half is re-earned |
| `docs/ADMISSIBILITY_SUPPORT_CONSTRAINS_CONTENT_NOT_FORMATION_SITE_BOUNDED_THEOREM_NOTE_2026-08-13.md` | Admissibility constrains content, not the formation site | formation is the displayed predicate under test; it is not written into Admissibility |
| `docs/DOMAIN_WALL_CHIRAL_EDGE_FROM_ACHIRAL_CL3_BULK_FREE_FIELD_BOUNDED_THEOREM_NOTE_2026-07-04.md` | an achiral bulk can still host a chiral edge | not used; this note classifies the star formation predicate only |

No earlier mechanism attaches L1 or writes V−A into Admissibility.
This note does not reopen `born-compiler` or `color-unital-m3`.

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
`N_both`, checks `n(P(c)) = −n(c)`, checks lock-label blindness,
separates Hamming-nonzero from `n ≠ 0`, re-earns proper-equivalence
of each 2-letter coloring to its `P`-image, exhibits the `P`-even /
`P`-odd mismatch, and verifies the refusal and no-go gate. Declared
audit inputs are this note and the axiom memo. No runner cache is
written. No occupancy step is run on a new spatial patch.
