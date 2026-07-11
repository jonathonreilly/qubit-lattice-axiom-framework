# The Cartan-Valued Cross-Plane Pairing: Diagonal-Weyl-Invariant Joint-Orbit Data, Provably Underdetermined by Per-Plane Weyl Orbits; Values in (1/3)Z with the Fractional Part Exactly the Mod-3 Center Pairing and an Integer Odd Witness on the Center-Trivial Subsector — the Frame Residual Sharpens to Relative-Frame Correlation Across the 4D Gluing (Bounded Theorem)

**Date:** 2026-07-02
**Current premise authority (2026-07-11):** every Tier-A/admission/registry
reference below is superseded historical context. It supplies no premise and
makes no dependency ready; the scientific conditions remain conditional/open.
**Claim type:** bounded_theorem (exact finite constructions plus scoped frame
obstructions; not a terminal no-go, not a discharge of the theta admission).
**Audit-status authority:** independent audit lane only. This note does not set an
audit verdict, edit registries, register primitives, change axioms, retire or
re-grade any Tier-A admission, or claim Strong-CP closure.
**Primary runner:**
[`scripts/theta_cartan_valued_cross_plane_pairing_weyl_frame_theorems_2026_07_02.py`](../scripts/theta_cartan_valued_cross_plane_pairing_weyl_frame_theorems_2026_07_02.py)
**Runner cache:**
[`logs/runner-cache/theta_cartan_valued_cross_plane_pairing_weyl_frame_theorems_2026_07_02.txt`](../logs/runner-cache/theta_cartan_valued_cross_plane_pairing_weyl_frame_theorems_2026_07_02.txt)

## Question

The theta campaign (PRs #4784, #4796, #4811 — landed; PR #4832 — in-flight)
left `W_theta_Q_context` with residual (i-b'): the torus-dual integer flux
data exist exactly per plaquette but only modulo the Weyl group; a
glued-surface flux-sector readout appears to need a Weyl-frame choice (the
abelian-projection question). The current `MINIMAL_AXIOMS_2026-06-29.md`
text on optional record presence, admissibility nonvacuity, and readout
discipline supplies exactly the discipline that governs this residual,
quoted below.

Question answered here: which flux-sector data are frame-free, which
provably are not, what are the exact values of the pairing the theta chain
needs, and what does the frame residual reduce to?

## Answer

Four exact finite results (runner-verified, exact rationals throughout):

1. **The rank-2 pairing exists exactly at the cochain level.** Extending the
   block-3 cup pairing to Cartan-valued (rank-2) closed integer 2-cochains
   with the su(3) Gram form, `Q_G = (1/2) sum_ab G_ab n^(a) u n^(b)` is
   componentwise class-invariant, purely cross-plane (single-plane rank-2
   fluxes give exactly zero), reflection-odd, and reduces exactly to the
   Gram-intersection of the flux classes — the SU(3)-shaped carrier pairing,
   now explicit.

2. **Values: thirds, with the fractional part exactly the center pairing.**
   On weight-valued fluxes `Q_G in (1/3)Z`; root-lattice shifts change `Q_G`
   by integers, so `Q_G mod 1` is a function of the triality classes alone,
   and the full 3 x 3 table is

   ```text
   Q_G mod 1 = (2 t t' / 3) mod 1     (t, t' = triality classes),
   ```

   i.e. the mod-3 center pairing of blocks 1 and 3 reappears **derived** as
   the fractional part of the abelianized pairing. On root-valued
   (center-trivial) fluxes `Q_G in Z`, with the explicit odd witness
   `Q_G(alpha_1, alpha_2) = -1`: the pointwise selector's
   integer-with-odd-support interface is populated on the center-trivial
   subsector.

3. **Frame theorems.** `Q_G` is invariant under the **diagonal** Weyl action
   (one frame rotating all planes together): the pairing is joint-orbit
   data, so the frame requirement on a surface is a single Weyl class, not
   one per plaquette. But per-plane-**independent** Weyl action changes
   `Q_G` — explicit witnesses rotate the first slot inside its own orbit
   while `Q_G` runs over `{-2, -1, 1, 2}`. Per-plane orbit data therefore
   **underdetermine** the pairing: no function of the separate orbits can
   compute `Q_G`.

4. **The 2D witness.** On the fully glued 2D dual (blocks 2 and 4) the
   sector label is a dominant weight, and dominant labels biject with
   regular Weyl orbits (runner-verified in a window): the glued 2D label
   **is** the orbit invariant — no frame choice enters. The frame question
   is genuinely a relative, multi-flux phenomenon.

**Readout-discipline consequence (clarified Record axiom, consumed here).**
The live axiom memo now states: "Only records are readable. A readout value
is determined by record content alone." and "A law privileges no states. Its
domain is a supplied condition, and at every state where the condition
holds it gives exactly one answer." An arbitrary per-plaquette Weyl-chamber
choice is neither record content nor such a law; by Theorem 3 the pairing
readout on independently-framed fluxes is not determined by per-plane orbit
(record-candidate) data alone. So a licensed `Q_G` readout requires the
**relative frame** between plane fluxes to be itself derived or registered.
The residual (i-b') accordingly sharpens to:

```text
(i-b'') relative-frame correlation: derive, from the 4D gluing structure
        (link integration across the six-plaquette link stars / the
        recoupling data), that the abelianized plane fluxes of a glued
        surface carry a joint diagonal-Weyl orbit — i.e. that gluing
        correlates the per-plaquette Cartan frames, as it demonstrably
        does in the fully glued 2D case.
```

## Source surface (named authorities)

1. **Record axiom** (approved axiom node `minimal_axioms`,
   [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md), as
   landed on main at commit 7950d9202c), quoted:

   > "When present, a record locks exactly one admissible local possibility. A
   > site never carries more than one record; records are permanent. Only
   > records are readable. A readout value is determined by record content
   > alone. For any finite collection of pairwise-disjoint records, scalar
   > readout `I` is additive, with `I(empty)=0`."

   and from the Qualification section:

   > "A state is a configuration of records. A law privileges no states.
   > Its domain is a supplied condition, and at every state where the
   > condition holds it gives exactly one answer."

   Housekeeping flag: the campaign notes landed before these clarifications
   (PRs #4784, #4796, #4811) quote the pre-clarification Record wording
   (verbatim then; the inserted readout-discipline sentence postdates them).
   No claim in them conflicts with the added text — it strengthens the
   direction they already respected — but their quotes are no longer
   contiguous excerpts of the live memo; flagged for owner/reviewer
   discretion.

2. **Campaign chain** (landed: PRs #4784, #4796, #4811; in-flight:
   PR #4832): the cup-pairing machinery and flux representatives re-derived
   here are the block-3 objects extended to rank 2; the weight-lattice /
   Weyl facts are the block-4 ground. All are re-earned inline by this
   runner (exact rational Gram/Weyl algebra; integer cochain algebra on
   `T^4_2`); no landed note is consumed as a premise.

3. **Tier-A theta registry text**
   ([`docs/audit/data/premise_decision_history.json`](audit/data/premise_decision_history.json),
   gauge side): the residual is "localized to the multi-plaquette /
   large-gauge-winding account"; the object constructed here is that
   account's SU(3)-shaped pairing.

No external comparator, measured value, fitted number, or continuum input
enters anywhere. The Gram normalization (`|alpha|^2 = 2`,
`<alpha_i, omega_j> = delta_ij`) is declared and verified inline (exact
rationals).

## Theorem 1 (ground: lattice, form, group)

In fundamental-weight coordinates with Gram form
`G = (1/3) [[2, 1], [1, 2]]`:

- `|alpha_1|^2 = |alpha_2|^2 = 2`, `<alpha_1, alpha_2> = -1`,
  `<alpha_i, omega_j> = delta_ij`, `<omega_1, omega_1> = 2/3`,
  `<omega_1, omega_2> = 1/3` (exact rationals);
- the two simple reflections generate a group of order 6 preserving `G`,
  with W-average exactly the zero map (no fixed direction — the block-4
  obstruction re-derived in weight coordinates);
- every regular orbit in the tested window contains exactly one dominant
  representative: dominant labels are precisely the W-orbit invariants.

## Theorem 2 (rank-2 cochain pairing on T^4)

For pairs `(n^(1), n^(2))` of closed integer 2-cochains on `T^4_2`
(weight-coordinate components of a Cartan-valued branch cochain), with
`Q_G = (1/2) sum_ab G_ab n^(a) u n^(b)`:

- `Q_G` equals the Gram-intersection of the flux classes,
  `Q_G = sum_(complementary pairs) (sign) <m_P, m_P'>`, on random rank-2
  flux assignments (exact);
- `Q_G` is invariant under independent exact shifts of both components
  (componentwise class invariance);
- every single-plane rank-2 flux has `Q_G = 0` (cross-plane structure);
- a coordinate reflection flips the sign of `Q_G` (witness: `-4/3 -> 4/3`)
  — the sector-pairing mechanism of block 3 is intact at rank 2.

## Theorem 3 (values)

- Weight-valued fluxes give thirds: `Q_G(omega_1, omega_1) = 2/3`,
  `Q_G(omega_1, omega_2) = 1/3`.
- Root-lattice shifts of any flux change `Q_G` by integers (Cartan
  integrality), so `Q_G mod 1` depends only on the triality classes
  `(t, t')`; the verified table is `Q_G mod 1 = (2 t t'/3) mod 1` — the
  mod-3 center pairing, now derived as the fractional part of the
  abelianized pairing. (Consistency: block 3's mod-3 descent and no-Z-descent
  results are the shadow of exactly this structure.)
- Root-valued fluxes give integers, with `Q_G(alpha_1, alpha_2) = -1` an
  odd witness; a positive weight family on root-valued flux pairs gives
  `Z_Q > 0`, conjugation/reflection-paired, with odd support, and at
  `theta = pi` every odd sector carries negative weight —
  the selector interface arithmetic populated on the center-trivial
  subsector.

## Theorem 4 (frame theorems)

- **Diagonal invariance:** for every `w` in the six-element Weyl group and
  every tested flux assignment, applying `w` to all plane fluxes together
  leaves `Q_G` unchanged (Gram invariance). The pairing is a function of
  the joint diagonal orbit.
- **Independent-frame breaking:** rotating one plane's flux inside its own
  Weyl orbit while holding the other fixed changes `Q_G`: from the base
  value `-1` at `(alpha_1, alpha_2)`, the first-slot orbit yields
  `{-2, -1, 1, 2}`. Hence per-plane orbit data underdetermine the pairing —
  there is no function of the separate orbits computing `Q_G`.
- Together: the frame requirement for a `Q_G` readout is exactly ONE
  relative-frame datum per flux pair (equivalently a single global Weyl
  class per surface once frames are correlated), never a per-plaquette
  convention.

## Corollary (wall state and the axiom-discipline consequence)

By the clarified Record axiom, a readout value is determined by record
content alone, and a law privileges no states. An uncorrelated
per-plaquette Weyl-chamber choice is a privileged convention, not record
content and not a condition-determined law; Theorem 4 shows the pairing
readout cannot be built from per-plane orbit data alone. Therefore:

```text
W_theta_Q_context (current decomposition):
  (i-a)   defect closure on the abelianized multi-plaquette dual (block 3);
  (i-b'') relative-frame correlation: derive from the 4D gluing (link
          integration on six-plaquette link stars / recoupling data) that
          glued-surface plane fluxes carry a joint diagonal-Weyl orbit —
          the 2D case has this automatically (the matched label is the
          orbit invariant), and the pairing needs nothing more than the
          joint orbit (Theorem 4);
  (ii')   derive the F u F-shaped multi-plaquette insertion from the
          framework surface (block 3 supplies its sector reduction; block 4
          obstructs the per-plaquette shift-slot alternative).

W_theta_bar_assembly: unchanged (in-flight PR #4768).
```

The center-trivial subsector result (integer `Q_G` with odd support) means
the interface the theta chain consumes is populated as soon as (i-a),
(i-b''), and (ii') are supplied — no additional value-structure obstruction
hides in the rank-2 pairing.

## Identification checkpoint (what objects these are)

The Cartan-valued fluxes and their pairing are reconstruction-surface
objects of the abelianized dual (block 4): frame data modulo Weyl,
per-plaquette. No claim is made that a record registers a flux vector, that
the pairing is the physical theta charge, or that fractional sectors are
physically realized (the weight-vs-root-valued distinction is presented as
exact lattice arithmetic, not as a global-form/physical-sector claim). The
headline is a theory of the carrier pairing's exact value and frame
structure — not a registration claim.

## Relation to the RP-half no-go (route independence)

The retained no-go row
[`STRONG_CP_RP_HALF_CANNOT_FORBID_CP_ODD_IMAGINARY_NO_GO_NOTE_2026-05-16.md`](STRONG_CP_RP_HALF_CANNOT_FORBID_CP_ODD_IMAGINARY_NO_GO_NOTE_2026-05-16.md)
forecloses only "the RP half-square identity alone cannot derive a
no-bare-theta-slot exclusion." Nothing here uses reflection positivity or
asserts a bare-theta-slot exclusion; the reflection map is the block-3
cochain pullback used for weight pairing.

## What moves

| Prior state | After this note |
|---|---|
| (i-b') "Weyl-frame consistency" — undifferentiated frame question | split exactly: diagonal-orbit (joint) data SUFFICE (pairing invariant); per-plane orbit data provably UNDERDETERMINE; residual = relative-frame correlation (i-b'') |
| SU(3)-shaped carrier pairing — implicit | explicit and exact: rank-2 cochain pairing, class-invariant, cross-plane, reflection-odd, reducing to the Gram-intersection of fluxes |
| center Z_3 vs integer charge (blocks 1/3) | unified: Q_G mod 1 = (2 t t'/3) mod 1 — the center pairing IS the fractional part; integer sector = center-trivial (root-valued) fluxes |
| selector interface on the SU(3)-shaped carrier | populated: odd integer witness Q_G = -1; positive family with paired weights, odd support, theta = pi negativity |
| frame discipline | grounded in the clarified Record axiom: readout from record content alone; per-plaquette chamber conventions are not licensed inputs |

## What remains

```text
(i-a)   defect closure (block 3's residual, unchanged);
(i-b'') relative-frame correlation across the 4D gluing (the finite
        recoupling question; 2D witness in hand);
(ii')   the F u F-shaped insertion from the framework surface.
```

## Non-claims

This note does not claim:

- Strong-CP closure, theta retirement, or any change to the Tier-A registry;
- a derivation of (i-a), (i-b''), or (ii');
- that gluing in 4D does or does not correlate frames (that is the open
  question (i-b''), posed — only the 2D case is settled here);
- that fractional sectors are physical, or any global-form (SU(3) vs
  SU(3)/Z_3) statement — the value structure is exact lattice arithmetic on
  the stated objects;
- that records register flux vectors, frames, or the pairing (readout
  licensing is analyzed, not asserted to be satisfied);
- exclusion of frame-free constructions beyond the tested scope (the
  underdetermination theorem binds functions of separate per-plane orbits;
  joint invariants are exactly what remains and what (i-b'') targets);
- any new axiom, import, primitive, or admission.

## No-Go Discipline Gate (for the negative boundary)

**No-Go Discipline result:** PASS as bounded scoping inside positive constructions. The
negative content is exactly: per-plane-independent Weyl orbit data
underdetermine the cross-plane pairing (explicit same-orbit witnesses), so
an uncorrelated per-plaquette frame convention cannot license a pairing
readout under the clarified readout discipline.

### N1 — Alternative-route enumeration

| Route to a licensed pairing readout | Standing here |
|---|---|
| function of separate per-plane W-orbits | EXCLUDED (Theorem 4: same orbits, different Q_G) |
| arbitrary per-plaquette chamber convention | NOT LICENSED under the clarified Record axiom (readout from record content alone; laws privilege no states) — and unnecessary given the diagonal result |
| joint diagonal-orbit data | SUFFICIENT (Theorem 4, diagonal invariance) — the (i-b'') target |
| relative-frame correlation derived from 4D gluing/recoupling | OPEN — named residual (i-b''); 2D case settled affirmatively |
| frame registered as record content | LOGICALLY OPEN — would need a derivation that records form on frame data; not pursued, not claimed |
| center-projected (Z_3) data alone | insufficient for the integer pairing (block 3); here seen as exactly the fractional part |
| operational primitive registration | APPROVED-PRIMITIVE PROPOSAL, not proposed (standing direction 2 -> 0) |

### N2 — Wall-independence audit

Nothing here binds the mass side or `W_theta_bar_assembly`. The
underdetermination theorem is scoped to functions of separate per-plane
orbits; it does not obstruct joint constructions (it motivates them). The
readout-discipline consequence uses the axiom text as discipline, not as a
physics derivation: it classifies which readouts would be licensed, without
asserting any record occurs.

### N3 — Hidden-wall scan

The Gram normalization and Weyl realization are declared and verified
inline (exact rationals; group closure computed, not assumed). The
(1/2)-normalization of `Q_G` is fixed by the Gram-intersection reduction
and the block-3 consistency (root-diagonal case).
"Underdetermine" means precisely: two assignments with identical per-plane
orbits and different `Q_G` exist (witnesses shown). The clarified axiom
sentences are quoted verbatim from the live memo.

### N4 — Residual matching

Block 4's (i-b') is consumed and refined into (i-b''); blocks 1/3's mod-3
structures are matched exactly as the fractional table; block
3's integer pairing is the root-valued diagonal of this object; the Tier-A
registry's multi-plaquette localization is respected throughout. The landed
`retained_bounded` instanton-infrastructure certificate (2026-05-17)
records twisted-`T^4` fractional-charge arithmetic under imported continuum
conventions; the fractional table here arises inside the campaign's own
finite cochain chain with no continuum input — complementary, not consumed,
not contradicted.

### N5 — Rhetoric audit

No "closes/exhausted/only-route" framing. The negative statements are
scoped (functions of separate orbits; convention licensing); live paths are
named; (i-b') is refined, not declared done.

### N6 — Partial-closure path scan

Live paths: derive (i-b'') from the finite link-star/recoupling structure
(the 2D mechanism's 4D analogue); construct joint invariants directly on
glued surfaces; derive record formation on frame data (unexplored); (i-a)
and (ii') as before; the assembly side (PR #4768).

### N7 — Steelman

A hostile reviewer can press: (1) "The Gram/Weyl facts are textbook." The
deliverable is the exact finite theorem set wired to the campaign's wall
decomposition — the same-orbit breaking witnesses, the fractional table
identified with the center pairing, and the licensing analysis under the
freshly clarified axiom text; no novelty beyond that wiring is claimed.
(2) "Using the axiom clarification as a premise is fragile — the memo just
changed." The clauses are quoted verbatim from the live memo and used as
discipline (which readouts are licensed), not as physics; if the memo
changes again the classification adjusts, and the mathematical theorems
(1-4) are axiom-independent. (3) "The 2D witness does not make the 4D
correlation plausible — recoupling could scramble frames." Agreed: (i-b'')
is posed as genuinely open; the note stakes nothing on its outcome. All
three objections are absorbed into scope.

### N8 — Cross-cycle echo

Cumulative guards: no integer-from-character-grading (block 1); no
label-existence-only claims (block 2); no unrestricted-sum sectors, no
center-dual integer charge (block 3); no per-plaquette shift-slot, no
frame-free treatment of modulo-W data (block 4). This block adds: no
pairing readout from separate per-plane orbits, and no arbitrary
per-plaquette chamber conventions as readout inputs. Future cycles citing
this chain must supply (i-a), (i-b''), and (ii') explicitly.

## Verification

Run:

```bash
python3 scripts/theta_cartan_valued_cross_plane_pairing_weyl_frame_theorems_2026_07_02.py
```

Expected close:

```text
TOTAL: PASS=21 FAIL=0
```

Sections: A weight-lattice ground (Gram values, Cartan integers, order-6
group closure, G-invariance, zero W-average, dominant = orbit
representatives); B rank-2 cochain pairing on `T^4_2` (reduction to
Gram-intersection, componentwise class invariance, cross-plane nullity,
reflection-oddness); C values (thirds; root-shift integrality; the 3 x 3
fractional table = mod-3 center pairing; integer odd witness on root-valued
fluxes); D frame theorems (diagonal invariance; independent-frame breaking
with same-orbit witnesses); E 2D joint-frame witness; F interface
arithmetic on the integer subsector.
