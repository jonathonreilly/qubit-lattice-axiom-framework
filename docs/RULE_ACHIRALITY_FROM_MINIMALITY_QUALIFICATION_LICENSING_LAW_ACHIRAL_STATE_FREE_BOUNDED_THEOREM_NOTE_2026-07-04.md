# Bounded Rule-Achirality Diagnostic from the Qualification: a Chiral Rule Branch Needs an Unfixed Reflection-Odd Bit, While Chiral States Remain Allowed

**Date:** 2026-07-04
**Type:** bounded_theorem
**Claim type:** bounded_theorem (exact finite rule-space diagnostic: the
achiral/chiral-pair witnesses, the one-bit count under reflection
conjugation, the reflection-odd selecting datum in the named model, odd
non-sourcing, and the spontaneous-state escape; plus a conditional licensing
argument that invokes the axiom memo's Qualification clause, stated as such;
not an exhaustive classification of all admissibility laws, not a
determination that retires the theta admission, not a Strong-CP claim, not an
axiom change).
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

This note asks a third question: what is the strongest rule-achirality
statement the framework can make without adding a mirror axiom? The answer
below is bounded. It proves a finite diagnostic and a licensing pattern, not
an exhaustive theorem that every possible admissibility law has already been
classified. The relevant governance text is the axiom memo's Qualification:

> "These axioms state only their named primitive content. Further physical
> structure requires derivation, bridge, explicit admission, or approved
> primitive registration before use as a premise. In particular, a law may not
> depend on a choice not fixed by the supplied structure, unless that choice is
> admitted."

The second sentence is the owner-approved 2026-07-04 Qualification
clarification (landed in PR #4952, commit `cc428cfa71`). This note was drafted
before it landed, flagging its content as a "counts-as-import" premise for
owner adjudication; that adjudication is now made — by the owner approving and
landing the clarification — so the licensing below rests on **stated axiom
text**, not on an interpretive reading. The honest scope (this does not by
itself give `theta = 0`, does not resolve chiral-fermion emergence, and does
not enumerate every admissibility law) is unchanged.

## Answer

The runner proves a bounded finite-model fact, not a universal classification
of every possible admissibility law. In the named six-direction
nearest-neighbor rule model, reflection conjugation exposes exactly the branch
relevant to the Qualification: an achiral witness is full signed-permutation
covariant; a chiral witness is proper-covariant but differs from its mirror
only through the reflection-odd datum `J2`; and a reachable state may still
carry `J2` under the achiral witness.

The licensing consequence is conditional and governance-facing: if a proposed
admissibility law depends on such a reflection-odd choice, and that choice is
not fixed by the supplied structure, the Qualification requires derivation,
bridge, explicit admission, or approved primitive registration. This note
supplies a finite witness and a test pattern for that boundary. It does not
prove that every proper-covariant admissibility law has been enumerated, does
not promote reflection covariance to an axiom, and does not by itself retire
`theta`.

1. **Reflection diagnostic on the signed-permutation substrate (Theorem 1).**
   `O_h = G+ . Z2^3`: every signed permutation can be represented as a proper
   cubic rotation composed with an axis-sign flip, and those flips are the
   `Cl(3,0)` presentation freedom the Qubit axiom declares "adds no further
   primitive structure". The lattice adjacency is reflection- and
   inversion-invariant. This gives a no-new-primitive reflection diagnostic on
   the finite substrate model; it is not an added mirror axiom.

2. **A chiral rule witness needs exactly one reflection-odd bit in this
   model (Theorem 2).** The runner exhibits an achiral alignment-rule witness
   and a chiral reflection-odd-threshold witness. The chiral witness and its
   mirror form a size-two pair not connected by any proper element. More
   generally, reflection conjugation is an involution, so any object on which
   it acts is either reflection-fixed or in a size-two mirror pair. The datum
   distinguishing the displayed twins is carried by the reflection-odd channel
   `J2`; the runner checks that the tested mirror-even base-value summary is
   blind to it.

3. **Licensing (the Qualification step).** A chiral rule that uses this
   reflection-odd bit as load-bearing law data depends on a choice not fixed
   by the supplied structure, unless some later derivation, bridge, admission,
   or primitive registration supplies it. The Qualification now states
   directly: "a law may not depend on a choice not fixed by the supplied
   structure, unless that choice is admitted." Therefore the finite model
   licenses the achiral witness directly, and treats the chiral witness as a
   rule requiring an explicit supplied source for its handed choice.

4. **Law achiral in the witness; state free (Theorem 3).** The achiral witness
   cannot source the reflection-odd channel: the handedness functional of the
   alignment rule is identically zero, against a nonzero chiral positive
   control, and this ties to the concrete theta-seed odd part (`-2c sin(a) Im
   tr U`), which a conjugation-closed law averages to zero. Yet under the
   achiral witness a reachable record **configuration** can still carry
   `J2 != 0` at a site, with its mirror history equally reachable — the state
   carries a handedness the law does not.

**Derivation summary.** The useful landed statement is bounded: the finite
model shows how a chiral law branch consumes an unfixed reflection-odd bit,
and the landed Qualification says such dependence needs a supplied source.
That is strictly weaker than a mirror-symmetry axiom because it constrains the
law data in the diagnostic, not state-level realized chirality. Whether the
weak sector's chirality actually has such a spontaneous origin is not shown
here (its parity violation is conventionally law-level); the point is only
that the achiral-witness result does not exclude it, whereas a mirror axiom
would.

## The former soft spot, narrowed by the landed clause

At drafting, the licensing step had one contestable premise: whether the
chiral rule's handedness bit "counts as further physical structure used as a
premise", to which the Qualification applies. A skeptic could answer that a
chiral rule is a single fixed object and its handedness is an innocent internal
property — like the integer 3 in "three generations" — not an imported premise.
That was the one seam this note flagged for owner adjudication rather than
ruling.

**That adjudication has now been made for the licensing rule.** The
owner-approved 2026-07-04 Qualification clarification (landed in PR #4952,
commit `cc428cfa71`) states in axiom text that "a law may not depend on a
choice not fixed by the supplied structure, unless that choice is admitted."
The finite chiral witness depends on exactly such a choice: the displayed
handedness is not fixed by the tested mirror-even data, and the rule's
availability outputs depend on it. The clause therefore governs the witnessed
dependence and licenses it only via a supplied source. This note does not take
the further step of asserting that all admissibility laws have been exhausted.

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

### Theorem 1 (signed-permutation reflection diagnostic)

`O_h = G+ . Z2^3` with `|G+ ∩ Z2^3| = 4`; the nearest-neighbor adjacency is
reflection- and inversion-invariant.

*Proof.* Product-set count and adjacency set-equality, runner A1-A2. The
axis-sign flips are the `Cl(3,0)` presentation freedom (non-primitive), so the
finite diagnostic can use signed-permutation reflections without adding a new
primitive. This is not a mirror-symmetry axiom for all laws or states.

### Theorem 2 (the finite chiral witness is reflection-odd and one-bit)

The displayed proper-covariant chiral witness and its mirror form a size-two
pair under reflection-conjugation; the distinguishing datum is the
reflection-odd channel; the tested mirror-even base-value summary does not
recover it.

*Proof.* Concrete witnesses: `R_align` is `O_h`-covariant (achiral,
reflection-fixed); `R_J2` is `G+`-covariant but breaks improper covariance
(chiral), with `sigma`-conjugate `R_J2bar` distinct and connected to `R_J2`
by no proper element (runner B1-B3, C1-C3). Reflection-conjugation is an
involution, so orbit sizes are one (fixed) or two (pair) for objects under
that action — no third case inside the named action (C3). The twins agree
whenever `J2 = 0`, so they differ **only** on chiral
conditions (`J2 != 0`) — the difference set is a subset of the chiral set,
verified on an unbiased sample (D1; equality does not hold in general, since a
chiral condition with nothing exactly at the threshold leaves the twins equal
— the load-bearing direction is that a difference *requires* `J2 != 0`). `J2`
is reflection-odd while the tested even summary (the multiset of base-values)
is reflection-invariant (D1); the achiral rule's handedness selector is zero
and the two chiral selectors are exact negations (D2). So the displayed
chiral rule carries one reflection-odd bit not supplied by the tested
mirror-even data.

### Theorem 3 (law achiral, state free)

An achiral rule sources no reflection-odd content; a chiral state survives an
achiral rule.

*Proof.* `Omega(R_align) = 0` against `Omega(R_J2) > 0` (E1), tied to the
theta-seed odd part which a conjugation-closed law averages to zero (E2).
Under `R_align` a reachable configuration carries `J2 != 0` at a site with its
mirror history equally reachable (E3). So the handedness bit is absent from
the law but available to the state.

## What this note does and does not claim

- **It does not impose a mirror-symmetry axiom.** The licensing boundary is a
  law-dependence restriction, not a mirror-symmetry axiom on states (which
  would be over-strong — it would forbid state-level handedness too). The
  enabling Qualification clarification was owner-approved and landed in PR
  #4952 (`cc428cfa71`); this note relies on it as stated axiom text, and does
  not itself add or amend axioms.
- **The former licensing soft spot is narrowed by that landed clause.** The one
  premise this note flagged for owner adjudication (does the handedness "count
  as an imported premise") is settled for the finite chiral witness by
  owner-approved axiom text. The note does not claim an exhaustive
  classification of all admissibility laws.
- **It does not retire the theta admission or claim theta = 0.** It settles the
  finite gauge-side rule-chirality diagnostic on stated axiom text; the mass
  side (`arg det M`) is a separate lane, the residual loop-level protection is
  the mass-side determinant-reality argument, and the audit lane owns any
  status.
- **The rule model is a named finite model.** Its witnesses instantiate the
  trichotomy and the bit-count exactly; the structural conclusions (involution
  orbits one-or-two, reflection-odd selector) are model-independent group
  facts.
- No fermion-sector claim: that an achiral law leaves room for spontaneous
  weak-sector chirality is noted as consistency, not derived; the weak
  sector's origin is entirely its own lane.

## No-Go Discipline Gate

**Status: PASS after narrowing.** The claim shipped here is not "no chiral
law exists" and not "no route can supply the handedness." It is the bounded
finite diagnostic plus the Qualification condition: if a law uses the displayed
reflection-odd bit, a supplied source for that bit is required.

- **N1 — alternative routes.** Five attacks were separated. Finite
  factorization attack: attempted and closed by runner A1. Adjacency
  reflection attack: attempted and closed by runner A2. Chiral-witness
  covariance attack: attempted and closed by B1-B3/C1-C3. Reflection-odd data
  attack: attempted and narrowed to the tested `J2`/base-multiset surface by
  D1-D2. Supplied-source attack (derivation, bridge, admission, or primitive
  registration): left open by design, because it is the Qualification's named
  escape and would not contradict the narrowed finite claim.
- **N2 — wall independence.** The narrowed claim has one explicit conditional:
  no supplied source for the displayed handed bit. No independent wall set is
  inflated.
- **N3 — hidden-wall scan.** The note was searched for hidden-admission phrases
  (`we assume`, `by construction`, `as is standard`, `framework provides`,
  `background`, `naturally`, `obviously`, `standard QFT`, `registered`,
  `canonical`, and close variants). No load-bearing hidden wall was kept;
  state-selection language remains bounded by the realized-state primitive,
  which supplies pointwise evaluation only and no selector.
- **N4 — residual matching.** Theta, gauge, and weak-chirality references are
  assessment context only. No prior no-go is consumed as a closure witness, so
  no non-matching residual is carried.
- **N5 — rhetoric audit.** Universal negatives were removed. The note now says
  finite `J2` rule branch, tested mirror-even base-value summary, finite
  witness, and state-level consistency; it does not claim all rule spaces,
  all summaries, or all states were exhausted.
- **N6 — partial-closure scan.** The source path remains open through the
  Qualification's own routes: derivation, bridge, explicit admission, or
  approved primitive registration. Existing approved primitives do not supply
  a handed law selector; the realized-state primitive supplies only pointwise
  evaluation at a realized law-admissible state.
- **N7 — steelman.** A hostile reviewer can argue that the finite
  six-direction model is only a witness and does not enumerate all
  admissibility laws; that steelman is correct, so the source was demoted to a
  bounded diagnostic rather than a universal no-go.
- **N8 — cross-cycle echo.** Prior theta and chirality gates show that
  orientation-like walls can move by admission, registrability, or reframe;
  those mechanisms are not ruled out here and are explicitly left as the next
  paths.

## What this unlocks (assessment, not a claim of closure)

- **The gauge side of the theta admission**: under the Qualification licensing,
  a gauge-side handedness of the finite `J2` form would be unlicensed unless a
  supplied source is added. Combined with the in-review gauge chain (Z2
  collapse, positive-class zero-branch) this is bounded support for the gauge
  half of the `theta_bar = theta_gauge + arg det M` decomposition, on stated
  axiom text (the licensing premise landed in PR #4952, `cc428cfa71`),
  pending audit grading.
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

1. **The counts-as-import adjudication — resolved for this finite witness.** The premise this note
   flagged was adjudicated by the owner approving and landing the 2026-07-04
   Qualification clarification (`cc428cfa71`); the licensing boundary now
   rests on stated axiom text. The machine registry mirror
   `docs/audit/data/axiom_premise_nodes.json` already carries that axiom text
   on `main`; premise-hash re-audit remains the audit lane's / owner's path.
2. **Law-achiral / state-chiral for the weak sector**: making the spontaneous
   weak-chirality picture (achiral rule, chirality-selecting vacuum) concrete
   enough to test against the observed maximal parity violation — the
   Nielsen-Ninomiya / domain-wall chiral-from-achiral program, the natural
   bridge from this note to the chirality gate.
3. **The mass side**: unchanged — `arg det M` and the determinant-reality
   protection, the sister lane, where the residual loop-level `theta_bar`
   contribution is controlled.
