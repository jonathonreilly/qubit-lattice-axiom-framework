# The Admissibility-Rule Covariance Extension Classified: Openness-Level Patterns Are Automatically Achiral, Chirality Requires Three Condition Values (One Chiral Pair at k = 3; Canonical Carrier the Oriented Frame), the Antilinear Value Twist Pairs Odd With Odd, and a Chiral Fixed Rule Is the Same Single Orientation Bit as the Theta Seed (Bounded Theorem + Classification)

**Date:** 2026-07-03
**Type:** bounded_theorem
**Claim type:** bounded_theorem (exact finite classification of
nearest-neighbor rule spaces under the proper-to-full cubic covariance
extension, on explicitly named condition-alphabet models; not a
determination of the framework's physical rule, and no import is introduced
— what an import would be is what gets classified).
**Status authority:** independent audit lane only. This note does not set an
audit verdict, edit registries, register primitives, change axioms, retire
or re-grade any retired Tier-A target, or claim Strong-CP closure.
**Primary runner:**
[`scripts/admissibility_rule_covariance_extension_classification_2026_07_03.py`](../scripts/admissibility_rule_covariance_extension_classification_2026_07_03.py)
**Runner cache:**
[`logs/runner-cache/admissibility_rule_covariance_extension_classification_2026_07_03.txt`](../logs/runner-cache/admissibility_rule_covariance_extension_classification_2026_07_03.txt)

**Current-main posture (2026-07-07):** the theta Tier-A target is already
retired on `main` by the 2026-07-05 retained-derivation decision. This note
banks a bounded admissibility-rule classification and theta-orientation
cross-check only; it does not reopen, modify, or supply authority for the
theta retirement record, registry, or physical `theta_bar` value.

## Question

The Admissibility axiom supplies "one fixed nearest-neighbor admissibility
rule, covariant under lattice translations and proper cubic rotations", with
"the available possibilities ... determined by, and vary[ing] with, the
nearest-neighbor conditions"
([`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)). The
axiom names **proper** covariance; its behavior under improper elements
(spatial inversion, reflections) is an unstated property. A neighbor's
condition is its record content or openness — the condition is a predicate
on states with record absence included
([`READING_NOTE_FINAL_DERIVATIONS_MOTION_CLOSURE_BOUNDED_NOTE_2026-07-02.md`](READING_NOTE_FINAL_DERIVATIONS_MOTION_CLOSURE_BOUNDED_NOTE_2026-07-02.md)).

Questions answered here, by exact finite classification on named
condition-alphabet models (colorings of the six nearest-neighbor directions
by a `k`-letter alphabet, with rule values acted on complex-antilinearly by
improper elements — the conjugation action of the one-site algebra's
`Cl(3,0)` presentation, re-earned in miniature by the runner):

1. When is proper covariance automatically full-cubic covariance
   (achirality)?
2. If not automatic, what is the minimal chiral channel, and what would a
   chiral fixed rule cost?
3. How does rule chirality relate to the theta-slot orientation
   structure?

## Answer

Five exact results:

1. **Structure (Theorem 1).** The full cubic group is `G = G+ x {1, P}`
   with the inversion `P` central; the direction action is faithful (48
   distinct permutations of the six axis directions), and the antipodal
   permutation is not realized by any proper element. So the improper
   question is exactly the action of the single central element `P`.

2. **Openness-level patterns are automatically achiral (Theorem 2).** For
   the two-letter alphabet (recorded/open — content-blind conditions),
   every coloring of the six directions is proper-equivalent to its
   `P`-image (all 64, exhaustively; Burnside orbit counts agree at 10 and
   10). Every proper-covariant rule depending only on the openness
   pattern is therefore automatically covariant under the full cubic
   group. **A chiral admissibility rule cannot live at the openness
   level**; chirality requires distinguishable record contents.

3. **Chirality requires three condition values, and at exactly three it
   is unique (Theorem 3).** At `k = 3` the proper/full orbit counts are
   57 and 56: exactly **one** chiral pair, whose members are the handed
   fully-mixed patterns — every axis bi-colored with two distinct values,
   every value used exactly twice, the value-to-axis incidence encoding a
   handedness (runner-anchored representative reported). At `k = 4`
   (three record contents plus openness) the count grows to 20 pairs and
   includes the **canonical carrier**: the oriented-frame coloring
   (`+x, +y, +z` carrying the three distinct contents, the rest open),
   verified chiral directly. The invariant carrying the canonical channel
   is the frame sign — the determinant sign of the labeled direction
   triple — which is proper-invariant and `P`-odd, and spans the
   one-dimensional `P`-odd part of the proper-invariant function space on
   the chiral orbit.

4. **The antilinear value twist pairs odd with odd (Theorem 4).** With
   rule values acted on antilinearly under improper elements (conjugation
   — the `Cl(3,0)` presentation's improper action), the rule
   `R0 = i x frame_sign` is fully `G`-covariant: an achiral rule may use
   the odd pattern channel, paired with the odd value direction. The
   bare-sign rule `R1 = frame_sign` transforms by the determinant
   character (chiral). The twist is load-bearing: under the untwisted
   action `R0` is chiral too. And the **readable scalar part of the
   achiral odd channel vanishes identically** (`Re R0 = 0` on the whole
   orbit): achiral rules can carry the oriented-frame structure only in
   the direction that scalar readout cannot see.

5. **Dichotomy and theta-seed equivalence (Theorem 5).** A chiral rule
   comes in a supplied-structure-indistinguishable pair `{R1, -R1}` (both
   fixed by every proper element, exchanged by `P`): fixing one is a
   one-bit selection no supplied structure determines. That bit is the
   theta-seed bit: the chiral rule's sign makes the frame-dependent
   density of the theta slot frame-invariant and nonzero (seed
   constructible), flipping the frame alone or the rule alone flips it,
   and flipping both restores it — **one orientation bit total**, shared
   between the rule and the seed. Conversely, an achiral rule supplies no
   seed sign: its readable odd part is identically zero and swap-closed
   pattern ensembles sum the chiral channel to zero exactly.

**Classification summary.** Either the framework's fixed rule is achiral —
in which case full-cubic covariance is derived, no orientation exists at
rule level, and the theta-slot conclusions proceed import-free — or the
rule is chiral, in which case it necessarily carries an
orientation-encoding content channel — impossible at openness level,
minimally the handed bi-coloring at three condition values, canonically
the oriented frame at three contents plus openness — and the choice
within its pair is exactly one orientation-odd import, the same single
bit the theta seed needs. One bit is in question anywhere in this sector,
and this note locates where it can live.

## Authorities and premises

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) — quoted:
  the Admissibility sentences ("one fixed nearest-neighbor admissibility
  rule, covariant under lattice translations and proper cubic rotations";
  "For each site, the available possibilities are determined by, and vary
  with, the nearest-neighbor conditions"); the Lattice axiom's proper
  cubic rotations; the Qubit `Cl(3,0)` equivalence clause; the Record
  readout sentence ("Only records are readable. A readout value is
  determined by record content alone", scalar additive readout); the
  Qualification's law sentence ("A law privileges no states. Its domain is
  a supplied condition...").
- [`READING_NOTE_FINAL_DERIVATIONS_MOTION_CLOSURE_BOUNDED_NOTE_2026-07-02.md`](READING_NOTE_FINAL_DERIVATIONS_MOTION_CLOSURE_BOUNDED_NOTE_2026-07-02.md)
  — condition typing: the condition as a predicate on states with record
  absence included (openness is a condition value).
- [`THETA_4D_CARRIER_FLUX_COHOMOLOGY_INTERSECTION_PAIRING_CLOSED_BRANCH_AND_DEFECT_CLOSURE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md`](THETA_4D_CARRIER_FLUX_COHOMOLOGY_INTERSECTION_PAIRING_CLOSED_BRANCH_AND_DEFECT_CLOSURE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md)
  — the theta-slot pairing whose frame-dependent density Theorem 5
  transports to.
- [`THETA_LINK_STAR_GLUING_FRAME_CORRELATION_PAIR_COMPOSITE_DAGGER_EVENNESS_AND_ODD_BRANCH_PHASE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md`](THETA_LINK_STAR_GLUING_FRAME_CORRELATION_PAIR_COMPOSITE_DAGGER_EVENNESS_AND_ODD_BRANCH_PHASE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md)
  — evenness of supplied pair reads (the readable-sector face of
  Theorem 4's vanishing).
- The antilinear improper action on the one-site algebra is carried from
  the in-review native orientation analysis (prose reference only, not a
  dependency edge); its use here is confined to the value-twist
  definition, re-earned in miniature by the runner (`sigma_2`-conjugation
  sends each Clifford generator to its negative and is antilinear).

## Theorem statements and proofs

### Theorem 1 (the improper question is one central bit)

`O_h = G+ x {1, P}` with `P = -I` central; the action on the six axis
directions is faithful; the antipodal permutation is not proper-realizable.

*Proof.* `P` commutes with every signed permutation; the direction action
is faithful because an orthogonal map fixing all six axis vectors is the
identity; if a proper `g` induced the antipodal permutation then `g P`
would induce the identity, forcing `g = P`, a contradiction. Runner:
A1-A4, including the unique factorization `g = g+ P^eps`.

### Theorem 2 (openness achirality)

Every proper-covariant rule depending only on the recorded/open pattern of
the six neighbors is covariant under the full cubic group.

*Proof.* Exhaustive: each of the 64 two-letter colorings is
proper-equivalent to its `P`-image (B1; Burnside cross-check 10 = 10). A
`G+`-invariant function on a set where `P` preserves every `G+`-orbit is
`G`-invariant. Content-blind conditions cannot carry chirality.

### Theorem 3 (chirality threshold and the minimal/canonical channels)

At `k = 2` there is no chiral pair (Theorem 2); at `k = 3` there is
exactly one, whose members are the handed fully-mixed patterns (every
axis bi-colored, every value used twice); at `k = 4` the sector grows
(difference 20) and contains the oriented-frame coloring as the canonical
carrier; the frame sign spans the `P`-odd proper-invariant functions on
the canonical chiral orbit.

*Proof.* Burnside differences 57 - 56 = 1 and 240 - 220 = 20, each
cross-checked by direct orbit enumeration, with the `k = 3`
representative's structure gated (every axis bi-colored, value counts
2/2/2) (B2-B3); the oriented-frame witness lies in a `k = 4` chiral pair
and its `P`-image is not reached by any of the 24 proper elements
(B4-B5); the frame sign is proper-invariant, `P`-odd, and the odd
projector on the two-dimensional proper-invariant function space of the
canonical orbit has rank one with the sign as its image (C1-C2).

### Theorem 4 (antilinear pairing law)

With improper elements acting on values by conjugation:
`R0 = i x frame_sign` is `G`-covariant (achiral); `R1 = frame_sign`
transforms by the determinant character (chiral); under the untwisted
action `R0` is chiral (the twist is load-bearing); and `Re R0 = 0`
identically — the achiral realization of the oriented-frame channel is
invisible to scalar readout.

*Proof.* Direct computation over the full 48-element group on the whole
chiral orbit (D0-D4). Odd pattern times odd value direction is even
because conjugation flips `i`; that flip is exactly what the improper
action supplies.

### Theorem 5 (one bit, shared)

A chiral fixed rule is a selection within the `P`-exchanged pair
`{R1, -R1}` that no supplied transformation determines (E1). The selected
sign transports to the theta slot: `s x D(frame)` is invariant under the
simultaneous `P`-flip of rule witness and frame, and nonzero on generic
fluxes (E2); flipping either alone flips it, flipping both restores it —
one bit total (E4). An achiral rule supplies no such sign: readable odd
part identically zero, swap-closed ensembles sum the channel to zero (E3).

## What this note does and does not claim

- **It does not determine the framework's physical rule.** The axiom fixes
  one rule; whether that rule is achiral or chiral is a property this
  note classifies but does not decide. What it derives: where chirality
  could live (only in content-level structure, minimally the
  oriented-frame channel), and what it would cost (one orientation-odd
  bit, identical to the theta-seed bit).
- **The condition-alphabet models are named models.** Identifying the
  physical condition alphabet (how many record contents the admissibility
  rule distinguishes) is downstream content; the classification is exact
  for each `k` and the structural conclusions (openness achirality,
  oriented-frame minimality, the pairing law) are alphabet-graded
  statements.
- **No fermion-sector claim.** That any derived rule chirality would also
  surface in fermion-sector structure is left entirely to that sector's
  own lane; nothing here asserts or constrains it beyond the shared-bit
  bookkeeping at rule level.
- The antilinear twist premise is carried from the in-review companion
  (prose only) and re-earned in miniature; Theorem 4's pairing statement
  is unconditional for the stated value action.

## Residuals and next paths

1. **Physical alphabet identification**: how many neighbor contents the
   fixed rule distinguishes — the classification says nothing chiral can
   happen below three; a derivation pinning the alphabet would immediately
   grade the rule's chirality question.
2. **Achirality derivation route**: if the rule's dependence is derivably
   openness-graded (content-blind at the covariance level), Theorem 2
   would upgrade "proper covariance" to full-cubic covariance as a
   theorem — the next path this opens on the covariance side.
3. **Chirality route accounting**: any future proposal of a chiral rule
   now has a named price — the oriented-frame channel and one
   orientation-odd bit shared with the theta seed — so proposals can be
   audited against exactly that carrier.
4. **Theta-chain wiring**: when the in-review orientation and Z2 companions
   land, Theorem 5's transport statement connects the rule-level bit to
   the theta branch table on cited premises.
