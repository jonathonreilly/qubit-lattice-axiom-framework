# The Admissibility Rule Is Achiral by Minimality: Reflections Are Substrate Symmetries, a Chiral Rule Needs One Reflection-Odd Bit the Axioms Do Not Supply, and the Qualification Clause Licenses Only the Achiral Rule Unless That Bit Is Explicitly Admitted — the Law Is Achiral While the State Stays Free to Be Chiral (Bounded Theorem + Minimality Licensing Argument)

**Date:** 2026-07-04
**Type:** bounded_theorem
**Claim type:** bounded_theorem (exact finite rule-space structure — the
achiral/chiral-pair trichotomy, the one-bit count, the reflection-odd
selecting datum, odd non-sourcing, and the spontaneous-state escape — plus a
licensing argument that invokes the axiom memo's Qualification clause, stated
as such; not a determination that retires the theta admission, not a
Strong-CP claim, not an axiom change).
**Status authority:** independent audit lane only. This note does not set an
audit verdict, edit registries, register primitives, change axioms, retire or
re-grade any Tier-A admission, or claim Strong-CP closure.
**Primary runner:**
[`scripts/rule_achirality_substrate_minimality_bit_count_2026_07_04.py`](../scripts/rule_achirality_substrate_minimality_bit_count_2026_07_04.py)
**Runner cache:**
[`logs/runner-cache/rule_achirality_substrate_minimality_bit_count_2026_07_04.txt`](../logs/runner-cache/rule_achirality_substrate_minimality_bit_count_2026_07_04.txt)

## Question

The prior blocks localized the gauge side of the theta parameter to a single
reflection-odd orientation bit and reduced the realized-alphabet chirality
question to a single residual: whether the fixed admissibility rule is
chiral. The Admissibility axiom fixes "one fixed nearest-neighbor
admissibility rule, covariant under lattice translations and proper cubic
rotations" ([`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md))
— it names proper covariance and is silent on reflections. Two options were
noted: add mirror symmetry to the axiom (over-strong — it would forbid the
observed weak-sector chirality too), or leave the bit an honest open datum.

This note asks a third question: is the rule's achirality **derivable** — not
from the four axioms in isolation (they are silent), but from the axioms
together with the framework's own minimality discipline, written into the axiom
memo's Qualification:

> "These axioms state only their named primitive content. Further physical
> structure requires derivation, bridge, explicit admission, or approved
> primitive registration before use as a premise. In particular, a law may not
> depend on a choice not fixed by the supplied structure, unless that choice is
> admitted."

The second sentence is the owner-approved 2026-07-04 Qualification
clarification (landed, commit `cc428cfa71`). This note was drafted before it
landed, flagging its content as a "counts-as-import" premise for owner
adjudication; that adjudication is now made — by the owner approving and
landing the clarification — so the licensing below rests on **stated axiom
text**, not on an interpretive reading. The soft-spot section records the
resolution. The honest scope (this does not by itself give `theta = 0`, and
does not resolve chiral-fermion emergence) is unchanged.

## Answer

**Yes, on the same footing as every other minimality-backed result in the
repo.** The argument has two proven substrate facts and one licensing step
that invokes the Qualification clause explicitly.

1. **Reflections are symmetries of the supplied substrate (Theorem 1).**
   `O_h = G+ . Z2^3`: every reflection is a proper rotation composed with an
   axis-sign flip, and those flips are the `Cl(3,0)` presentation freedom the
   Qubit axiom declares "adds no further primitive structure". The lattice
   adjacency is reflection- and inversion-invariant. So the substrate the
   rule lives on carries a reflection symmetry with no extra primitive — this
   is derived, not assumed.

2. **A chiral rule needs exactly one reflection-odd bit the axioms do not
   supply (Theorem 2).** In a concrete finite rule model, the space of
   proper-covariant rules splits under reflection-conjugation into achiral
   rules (reflection-fixed; an explicit alignment-rule witness) and chiral
   rules (an explicit reflection-odd-threshold witness), the latter occurring
   in mirror pairs `{R, R-bar}` that are distinct and connected by **no**
   proper element. Reflection-conjugation is an involution, so every
   proper-covariant rule is either reflection-fixed (achiral, zero extra
   data) or in a size-two mirror pair (chiral, one binary choice) — there is
   **no third case**. The datum distinguishing the twins is carried entirely
   by the reflection-odd channel `J2`; every proper- and reflection-invariant
   summary of a condition is blind to it. So selecting a chiral rule requires
   one reflection-odd bit that no supplied invariant provides.

3. **Licensing (the Qualification step).** A chiral rule uses that
   reflection-odd bit as a premise — it is load-bearing for which
   possibilities the rule makes available. By Theorem 2 the bit is a choice the
   supplied structure does not fix (the two mirror rules are
   supplied-structure-indistinguishable; the bit is not among the named
   primitive content and is not derivable from the supplied structure). The
   Qualification now states directly: "a law may not depend on a choice not
   fixed by the supplied structure, unless that choice is admitted." A chiral
   rule depends on exactly such a choice and does not admit it. Therefore the
   axioms **license only the achiral rule** — unless the handedness is
   explicitly admitted, which is the clause's own escape and a visible owner
   act, not a silent assumption. (A choice the structure does not fix is, by
   definition, underivable and unbridgeable — a derivation or bridge that fixed
   it would mean the structure fixes it — so admission is the only route the
   clause could name.)

4. **Law achiral, state free (Theorem 3).** An achiral rule cannot source the
   reflection-odd channel: the handedness functional of the alignment rule is
   identically zero, against a nonzero chiral positive control, and this ties
   to the concrete theta-seed odd part (`-2c sin(a) Im tr U`), which a
   conjugation-closed law averages to zero. Yet under the achiral rule a
   reachable record **configuration** can still carry `J2 != 0` at a site,
   with its mirror history equally reachable — the state carries a handedness
   the law does not. So minimality-achirality removes the bit from the *law*
   (no theta-seed source) while leaving the *state/vacuum* free to select a
   handedness spontaneously.

**Derivation summary.** The rule's achirality is not an extra axiom and not
an arbitrary choice: it follows from two proven substrate facts plus the
Qualification clause the framework already applies everywhere. A chiral rule
is an unadmitted import of a reflection-odd bit; minimality licenses only the
achiral rule, or an explicit admission of the handedness. And crucially the
minimality route is **strictly weaker than a mirror-symmetry axiom**: it
constrains the law, not the state, so it leaves *room* for the observed
weak-sector chirality to arise as spontaneous state-level symmetry breaking on
an achiral law — illustrated by (not derived from) the familiar picture of a
rotation-symmetric Hamiltonian with a directional ground state — whereas a
mirror-symmetry axiom would forbid state-level handedness too. Whether the
weak sector's chirality actually has such a spontaneous origin is not shown
here (its parity violation is conventionally law-level); the point is only
that the achiral-law result does not exclude it, which a mirror axiom would.

## The former soft spot, now resolved by the landed clause

At drafting, the licensing step had one contestable premise: whether the
chiral rule's handedness bit "counts as further physical structure used as a
premise", to which the Qualification applies. A skeptic could answer that a
chiral rule is a single fixed object and its handedness is an innocent internal
property — like the integer 3 in "three generations" — not an imported premise.
That was the one seam this note flagged for owner adjudication rather than
ruling.

**That adjudication has now been made.** The owner-approved 2026-07-04
Qualification clarification (landed, commit `cc428cfa71`) states in axiom text
that "a law may not depend on a choice not fixed by the supplied structure,
unless that choice is admitted." A chiral rule depends on exactly such a choice
(Theorem 2: the handedness is not fixed by the supplied structure, and the
rule's availability outputs depend on it). So the clause settles the seam the
way the note's own reasoning pointed: the handedness dependence is governed,
and licensed only via admission. The achirality is therefore **derivable on
stated axiom text**, no longer conditional on an interpretive premise.

The honest scope is unchanged by this resolution: it does not by itself give
`theta = 0` (the residual loop-level protection is the mass-side
determinant-reality argument) and does not resolve chiral-fermion emergence
(the Nielsen-Ninomiya / domain-wall route, downstream).

This is a **different and firmer** argument than the structuralist reading
quarantined in the presentation-gauge note: that reading turned on parsing one
Qubit sentence ("distinguished by the supplied algebraic structure alone") a
particular way, an interpretive act reserved to the owner. The present argument
rests on the Qualification clarification — explicit, owner-approved,
repo-wide-operative axiom text — as its named premise.

## Authorities and premises

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) — quoted:
  the Admissibility sentence ("one fixed nearest-neighbor admissibility rule,
  covariant under lattice translations and proper cubic rotations"); the
  Qualification clause ("Further physical structure requires derivation,
  bridge, explicit admission, or approved primitive registration before use
  as a premise"); the Qubit `Cl(3,0)` "adds no further primitive structure"
  clause; the Lattice proper-rotation and adjacency sentences; "A state is a
  configuration of records"; "Records form."
- Prior-block companions carried in prose only (in-review, not on this
  branch): the presentation-gauge note (`O_h = G+ . Z2^3`, axis-sign flips
  non-primitive, `Psi9`/reflection-odd channel), the bootstrap and
  continuation notes (`J2` reflection-odd channel, spontaneous-state
  registration, free-orbit reduction). Every substrate fact used here — the
  factorization, the `J2` channel's odd covariance, the achiral/chiral
  witnesses, the spontaneous escape — is **re-earned by this note's runner**,
  so no theorem depends on an off-branch file.

## Theorem statements and proofs

### Theorem 1 (reflections are substrate symmetries)

`O_h = G+ . Z2^3` with `|G+ ∩ Z2^3| = 4`; the nearest-neighbor adjacency is
reflection- and inversion-invariant.

*Proof.* Product-set count and adjacency set-equality, runner A1-A2. The
axis-sign flips are the `Cl(3,0)` presentation freedom (non-primitive), so
reflection symmetry of the substrate is present without extra primitive
structure.

### Theorem 2 (the chiral bit is reflection-odd and unsupplied; the trichotomy)

The proper-covariant rules split under reflection-conjugation into
reflection-fixed (achiral) and size-two mirror pairs (chiral); the
distinguishing datum is the reflection-odd channel; no proper- or
reflection-invariant of a condition recovers it.

*Proof.* Concrete witnesses: `R_align` is `O_h`-covariant (achiral,
reflection-fixed); `R_J2` is `G+`-covariant but breaks improper covariance
(chiral), with `sigma`-conjugate `R_J2bar` distinct and connected to `R_J2`
by no proper element (runner B1-B3, C1-C3). Reflection-conjugation is an
involution, so orbit sizes are one (fixed) or two (pair) — no third case
(C3). The twins agree whenever `J2 = 0`, so they differ **only** on chiral
conditions (`J2 != 0`) — the difference set is a subset of the chiral set,
verified on an unbiased sample (D1; equality does not hold in general, since a
chiral condition with nothing exactly at the threshold leaves the twins equal
— the load-bearing direction is that a difference *requires* `J2 != 0`). `J2`
is reflection-odd while every even summary (the multiset of base-values) is
reflection-invariant (D1); the achiral rule's handedness selector is zero and
the two chiral selectors are exact negations (D2). So a chiral rule carries
one reflection-odd bit no supplied invariant provides.

### Theorem 3 (law achiral, state free)

An achiral rule sources no reflection-odd content; a chiral state survives an
achiral rule.

*Proof.* `Omega(R_align) = 0` against `Omega(R_J2) > 0` (E1), tied to the
theta-seed odd part which a conjugation-closed law averages to zero (E2).
Under `R_align` a reachable configuration carries `J2 != 0` at a site with its
mirror history equally reachable (E3). So the handedness bit is absent from
the law but available to the state.

## What this note does and does not claim

- **It does not impose a mirror-symmetry axiom.** Achirality is derived under
  the Qualification (a law-dependence restriction), not a mirror-symmetry axiom
  on states (which would be over-strong — it would forbid state-level handedness
  too). The enabling Qualification clarification was owner-approved and landed
  (`cc428cfa71`); this note relies on it as stated axiom text, and does not
  itself add or amend axioms.
- **The former licensing soft spot is resolved by that landed clause.** The one
  premise this note flagged for owner adjudication (does the handedness "count
  as an imported premise") is now settled by owner-approved axiom text; the
  achirality rests on the Qualification directly, not on an interpretive
  reading.
- **It does not retire the theta admission or claim theta = 0.** It settles the
  gauge-side rule-chirality residual on stated axiom text; the mass side
  (`arg det M`) is a separate lane, the residual loop-level protection is the
  mass-side determinant-reality argument, and the audit lane owns any status.
- **The rule model is a named finite model.** Its witnesses instantiate the
  trichotomy and the bit-count exactly; the structural conclusions (involution
  orbits one-or-two, reflection-odd selector) are model-independent group
  facts.
- No fermion-sector claim: that an achiral law leaves room for spontaneous
  weak-sector chirality is noted as consistency, not derived; the weak
  sector's origin is entirely its own lane.

## What this unlocks (assessment, not a claim of closure)

- **The gauge side of the theta admission**: under the Qualification licensing,
  the gauge-side handedness that a nonzero `theta_gauge` would require is
  unlicensed — so the gauge summand carries no orientation datum in the law.
  Combined with the in-review gauge chain (Z2 collapse, positive-class
  zero-branch) this is the gauge half of the `theta_bar = theta_gauge + arg
  det M` decomposition, on stated axiom text (the licensing premise landed,
  `cc428cfa71`), pending audit grading.
- **The chirality gate (consistency, not a derivation)**: the weak sector's
  observed chirality is also a reflection-odd datum. Whether it is *literally*
  the same bit as this note's rule-level `J2` datum is a conjecture motivated
  by the no-coincidence principle, **not established here** — no structural
  bridge from the weak sector's chiral gauge coupling to `J2` is given. And a
  caution: the Standard Model's parity violation is conventionally **law-level**
  (an explicit chiral coupling in the Lagrangian), not known to be spontaneous.
  Theorem 3 shows an achiral law leaves the *state* free to carry handedness,
  so a state/vacuum-level origin for weak chirality is **not excluded** — but
  this note does not derive such a mechanism, and reproducing the observed
  maximal parity violation from a spontaneous origin on an achiral law is an
  open lane, not a claim.
- **What it does NOT unlock**: it does not retire any Tier-A admission (audit +
  owner + mass side), does not settle whether the handedness is instead worth
  admitting explicitly, and does not touch the mass side.

## Residuals and next paths

1. **The counts-as-import adjudication — resolved.** The premise this note
   flagged was adjudicated by the owner approving and landing the 2026-07-04
   Qualification clarification (`cc428cfa71`); the achirality now rests on
   stated axiom text. (The machine registry mirror
   `docs/audit/data/axiom_premise_nodes.json` and the premise-hash re-audit are
   the audit lane's / owner's to finalize.)
2. **Law-achiral / state-chiral for the weak sector**: making the spontaneous
   weak-chirality picture (achiral rule, chirality-selecting vacuum) concrete
   enough to test against the observed maximal parity violation — the
   Nielsen-Ninomiya / domain-wall chiral-from-achiral program, the natural
   bridge from this note to the chirality gate.
3. **The mass side**: unchanged — `arg det M` and the determinant-reality
   protection, the sister lane, where the residual loop-level `theta_bar`
   contribution is controlled.
