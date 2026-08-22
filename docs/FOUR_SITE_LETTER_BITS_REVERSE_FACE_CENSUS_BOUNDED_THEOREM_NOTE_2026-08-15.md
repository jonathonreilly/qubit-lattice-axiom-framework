---
claim_id: four_site_letter_bits_reverse_face_census_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Census of reverse and face content-bits over 16 letterings of four occupancy-formed sites is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/four_site_letter_bits_reverse_face_census_2026_08_15.py
---

# Four-Site Letter Bits: Reverse And Face Census

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact census of two named displayed content-bits on 16 letterings
of four declared occupancy-formed sites. Uniqueness is not required. The
lettering is not a formation mask. Letters are not written into Admissibility.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/four_site_letter_bits_reverse_face_census_2026_08_15.py`](../scripts/four_site_letter_bits_reverse_face_census_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Let the origin be held at letter `+`. The four non-origin occupancy-formed
sites of the declared `k=1` display are

```text
A = (1,0,0),  B = (1,1,1),  C = (2,0,0),  D = (1,1,0).
```

A lettering is a map `L : {A,B,C,D} → {+,−}`. There are exactly `2^4 = 16`
letterings. Origin is not one of the four lettered sites.

Named displayed content-bits:

- `reverse` is true if and only if `L(A)=+` and `L(B)=−`;
- `face` is true if and only if `L(C)=+` and `L(D)=−`.

**Theorem 1.** `N_Rev`, the number of the 16 letterings with reverse true,
equals 4.

**Theorem 2.** `N_Face`, the number of the 16 letterings with face true,
equals 4.

**Theorem 3.** `N_both`, the number of the 16 letterings with reverse and
face both true, equals 1.

These three integers are a reported census. They are displayed, not adopted.
The note does not write the letters into Admissibility, does not treat the
lettering as a formation mask, and does not require a unique lettering.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 16 letterings and the reverse/face census are finite exact counts on four declared sites; the letters remain displayed data, not adopted Admissibility or Record content."
trace_class: frontier_discovery
target_claim_id: four_site_letter_bits_reverse_face_census
target_blocker_text: "report the reverse and face content-bit census over letterings of the four occupancy-formed sites without adopting those letters"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the displayed census; do not adopt the letters or treat them as a formation rule"
conditional_surface_status: "exact for the 16 letterings of the four declared sites; displayed, not adopted"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Current Premise Boundary

The Lattice, Qubit, Admissibility, and Record premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

The full one-site possibility domain has algebraic presentation `M_2(C)`.

For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

Records form.

When present, a record locks exactly one admissible local possibility.

A readout value is determined by record content alone.

A site with no record cannot be read.

The Admissibility reading note says the distribution concerns which possibility
a forming record locks, conditional on formation at that site; it does not
supply the formation site, probability, or rate.

This census uses Lattice only to name four cubic sites. It uses Record only
as a boundary: a readout, if any, would be content, not a formation selector.
It does not rewrite Admissibility. The `{+,−}` alphabet, the four-site list,
and the reverse/face names are displayed theorem-domain data. They are not
axiom content.

## Exact Objects

Write `0=(0,0,0)`. The lettered set is `S={A,B,C,D}` with the coordinates
above. These four points are pairwise distinct and exclude the origin.

The origin letter is the displayed constant `+`. It is not a free bit in the
census.

The lettering space is

```text
Lambda = { L | L : S → {+,−} }.
```

`|Lambda| = 16`. Enumeration is by independent choice of `L(A), L(B), L(C),
L(D)`.

Define boolean predicates on `Lambda`:

```text
reverse(L)  <=>  L(A)=+ and L(B)=−
face(L)     <=>  L(C)=+ and L(D)=−
```

Then

```text
N_Rev  = |{ L in Lambda : reverse(L) }|
N_Face = |{ L in Lambda : face(L) }|
N_both = |{ L in Lambda : reverse(L) and face(L) }|
```

Reverse depends only on `{A,B}`. Face depends only on `{C,D}`.

## Proofs

**Theorem 1.** Reverse constrains `L(A)` and `L(B)` and leaves `L(C)` and
`L(D)` free. The constrained pair `(L(A),L(B))` has exactly one allowed
value, `(+,−)`. The free pair has `2^2=4` values. Therefore `N_Rev=4`.
Exhaustive listing of `Lambda` returns the same count.

**Theorem 2.** Face constrains `L(C)` and `L(D)` and leaves `L(A)` and
`L(B)` free. The constrained pair is exactly `(+,−)`. The free pair has 4
values. Therefore `N_Face=4`. Exhaustive listing agrees.

**Theorem 3.** Both bits true means

```text
(L(A),L(B),L(C),L(D)) = (+,−,+,−).
```

That is one lettering, so `N_both=1`. Equivalently, reverse and face use
disjoint site pairs, so

```text
N_both = N_Rev * N_Face / 16 = 4 * 4 / 16 = 1.
```

The four reverse letterings are

```text
(+,−,+,+),  (+,−,+,-),  (+,−,−,+),  (+,−,−,−)
```

in order `(A,B,C,D)`. Exactly one of these also has face true, namely
`(+,−,+,−)`.

Uniqueness is not required: four reverse letterings exist, not one.

## Displayed, Not Adopted

The census reports how often the named bits occur in the 16 letterings. It
does not select a physical lettering, does not add a fifth axiom, and does
not write `{+,−}` into Admissibility. A later adoption, if any, would be a
separate act.

The lettering is not a formation mask. Occupancy of the four sites is a
declared input naming those sites as occupancy-formed. The bits `reverse`
and `face` are functions of letters on already named sites. They do not
choose which sites form, and they do not replace the open formation-site,
probability, or rate residual.

No clock parameter is introduced. The census is a static count of maps.

## Exact Target And Obligation Graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| four occupancy-formed sites | declared coordinates; origin held at `+` |
| 16 letterings of `{A,B,C,D}` | exact enumeration |
| named reverse and face content-bits | displayed definitions |
| `N_Rev`, `N_Face`, `N_both` | Theorems 1–3 |
| unique lettering | not required; four reverse maps exist |
| letters as Admissibility content | not adopted |
| formation mask / formation site / rate | open; not this census |
| physical Record readout of the bits | open |

## Promotion Value Gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display census question for reverse and face on the four declared sites. |
| V2 | Current main has no landed 16-lettering reverse/face count on these four sites. |
| V3 | The three integers are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it enumerates a displayed alphabet on named sites. |
| V5 | It is not an adopted content rule: the letters remain displayed. |

## No-Go Discipline Gate

The negative content is narrow: the census does not force a unique lettering,
does not write letters into Admissibility, and does not convert content-bits
into a formation mask. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| unique reverse lettering | require `|reverse|=1` | fails; `N_Rev=4` |
| free origin letter | letter five sites including origin | different object; 32 maps, not this census |
| reverse as `L(A)=+` only | drop the `L(B)=−` conjunct | would give 8, not 4 |
| face on `{A,B}` | swap site pairs | different named bits |
| formation mask | let bits choose which sites form | not executed; occupancy is declared |
| adopt letters into Admissibility | rewrite the local rule by `{+,−}` | refused; displayed, not adopted |
| clocked sequence | introduce a time parameter | not used; static maps |

### N2 — wall independence

Missing physical adoption, missing formation-site rule, and missing Record
identification of the named bits are distinct open premises. This note claims
no complete wall collection.

### N3 — hidden-condition scan

The four sites, origin letter, binary alphabet, and reverse/face definitions
are declared. No uniqueness, no formation selector, and no Admissibility
rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, content-conditional-on-formation,
and unreadable absence. The residual that formation site, probability, and
rate remain unsupplied is unchanged. The census does not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each letter in `{+,−}` on each of four sites | no continuum alphabet |
| per site | `A,B,C,D` only; origin held at `+` | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | the 16 letterings and three census integers | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later derived selector among the 16 letterings, a
separate formation rule, and a Record content map for reverse/face. None is
taken here.

### N7 — hostile steelman

**Steelman:** Four occupancy-formed sites with a binary alphabet should pick
one reverse lettering and one face lettering, and those bits should decide
formation.

**Answer:** Reverse is a two-site conjunct, so four letterings satisfy it.
Face is independent of `{A,B}`, so the bits do not single out a unique map.
Occupancy is already the naming of the sites; the bits are letters on those
sites, not a mask that forms them. Uniqueness is not required.

### N8 — cross-cycle echo

A support-versus-formation type split already says content law does not pick
a formation site. This census does not reverse that split: it counts letters
on declared occupancy-formed sites and leaves formation unsupplied.

**Gate disposition:** PASS for the 16-lettering reverse/face census above.
FAIL / DO NOT SHIP for “the lettering is unique,” “letters are Admissibility,”
or “reverse/face is a formation mask.”

## Primary Runner

The companion runner enumerates the 16 letterings, evaluates the displayed
reverse and face predicates, and checks Theorems 1–3 together with origin
exclusion, non-uniqueness, pair independence, the closed-form `2^{4-2}=4`,
a drop-conjunct mutation, current premise quotes, and forbidden-phrase
hygiene. It authors no audit verdict. Declared review inputs are this note
and the axiom memo only.
