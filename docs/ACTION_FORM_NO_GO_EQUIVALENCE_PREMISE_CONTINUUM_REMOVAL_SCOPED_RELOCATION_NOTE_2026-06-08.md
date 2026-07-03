# Action-Form No-Go's Equivalence Premise Is Continuum-Removal-Specific — A Scoped Relocation

**Date:** 2026-06-08
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Primary runner:**
[`scripts/frontier_action_form_continuum_removal_scoping_2026_06_08.py`](../scripts/frontier_action_form_continuum_removal_scoping_2026_06_08.py)
**Cached output:**
[`logs/runner-cache/frontier_action_form_continuum_removal_scoping_2026_06_08.txt`](../logs/runner-cache/frontier_action_form_continuum_removal_scoping_2026_06_08.txt)

## Claim under test

The action-form uniqueness no-go
([`BRIDGE_GAP_ACTION_FORM_UNIQUENESS_NO_GO_NOTE_2026-05-06`](BRIDGE_GAP_ACTION_FORM_UNIQUENESS_NO_GO_NOTE_2026-05-06.md))
concludes that the retained primitives **cannot** select among the Wilson,
heat-kernel (HK), and Manton gauge actions. Its load-bearing premise (that note's
Step 4.2) is:

> "All three give the same continuum limit ... There's no continuum-limit lever
> distinguishing them."

and (Step 4.3) "The differences are at finite β = lattice scale = the framework's
evaluation point."

**Is that premise a framework-internal fact, or is it specific to reading the lattice
as a removable regulator?** If the latter, the no-go does not transfer to the
framework's own baseline.

## Verdict

**The premise is continuum-removal-specific, and is not invoked on the framework's
baseline physical-lattice semantics.** The three actions are equated *only* by their
shared a→0 limit; at the physical evaluation point they are quantitatively distinct
theories. This **relocates** the wall: under the baseline reading, action-selection is
a **well-posed open physical question**, not a structural no-go. The no-go is not
refuted — it stands in its regulator/continuum-removal frame; this note **scopes** it.

## The baseline this rests on (not an import)

[`PHYSICAL_LATTICE_FOUNDATIONAL_INTERPRETATION_NOTE_2026-05-08`](PHYSICAL_LATTICE_FOUNDATIONAL_INTERPRETATION_NOTE_2026-05-08.md)
(meta, baseline): *"Cl(3) on Z³ is physical, not a regulator … Review-loop should
therefore not count the physical-lattice reading itself as a new axiom, new theory
premise, or admitted-context input."* So the physical-lattice reading is **baseline
framework semantics**, and the a→0 continuum limit is a property of an
**un-taken** limit, not the physical content.

(The narrowed `PHYSICAL_LATTICE_NECESSITY_NOTE` retained_no_go is a *different*
statement — a two-invariant algebraic rigidity on the
canonical normalization surface — and explicitly does **not** bear on the
physical-vs-regulator reading; it neither forbids nor derives it.)

## What the runner verifies (`PASS=17 FAIL=0`)

On SU(2) (clean Bessel/character closed forms) and SU(3) (the framework's N_c, the
no-go's own numbers):

**(A) Leading order (a→0): the three actions AGREE.** With the matched family
(`t = 2N_c/β`, Manton coefficient = Wilson's small-field coefficient), the small-field
quadratic actions coincide (reproducing the no-go's Step 1), and `⟨P⟩_W, ⟨P⟩_HK,
⟨P⟩_M → 1` together as β→∞ (spread `0.003 → 0.0008 → 0.0002`).

**(B) Finite physical β: the three are DISTINCT theories.** SU(3) at β=6 reproduces
the no-go's exact figures — `⟨P⟩_W = 0.4225317396` (maximal-torus/Weyl integral) and
`⟨P⟩_HK = exp(−2/3) = 0.5134171190` (closed form, `C₂(fund)=4/3`) — a **21 % spread**,
`303 × ε_witness`.

**(C) The teeth — the agreement is SPECIFICALLY the a→0 limit.** The Wilson/HK spread
is **monotonically decreasing** in β and `→ 0` as β→∞ (`8×10⁻⁵ < ε_witness` at β=96),
vanishing as a positive power of the spacing (log-log slope `≈ 1.95`), while at the
physical point it is `O(1) ≫ ε_witness`. The equivalence lives entirely in the
un-taken a→0 limit.

**(D) Relocation: selection is well-posed; coincidence is the regulator frame.** A
second, independent observable (the plaquette variance) **also** separates Wilson and
HK at the physical point — so the candidates are observably distinct (selection
well-posed). A control confirms that as a→0 they coincide on *both* observables — the
no-go is correct *there*.

## Why this is a relocation, not a refutation

The no-go's logic is valid: **if** the lattice is a regulator whose a→0 limit defines
the physics (Symanzik universality), **then** actions sharing that limit are
equivalent and indistinguishable. This note shows that "if" is the load-bearing
clause. On the framework's baseline — where a is physical and never removed — the
antecedent is absent, the three actions are distinct theories, and the question
"which action does the framework realize?" is a genuine, answerable physical question
about finite-β data. The no-go's verdict is **scoped to the regulator reading**, not a
property of the framework.

This is the §3 strategic point made precise and minimal: it converts the
action-selection problem from *foreclosed* to *well-posed and open*. It is the
necessary first step before any selection argument can be legitimate.

## What this does NOT claim (boundary)

- **No derivation that HK (or any action) is the selected one.** That is the open
  follow-on. The natural candidate is the no-go's **own Step-3b** Brownian /
  heat-semigroup naturality argument — there dismissed as "suggestive" precisely
  because it treated the action as a *free functional choice optimized by an external
  criterion*. Once the continuum-equivalence that motivated that dismissal is removed
  (this note), the heat semigroup `exp(tΔ_g)` — uniquely determined by the canonical
  metric, with no convention freedom — is reinstated as a **well-posed selection
  candidate**. Whether it is the framework's emergent-time generator (RECORD axiom:
  time = monotone record accumulation) is the load-bearing open question, not asserted
  here.
- **No new axiom or import.** The physical-lattice reading is baseline semantics (cited
  above); the candidate actions, Haar measures, characters, Bessel functions, and the
  no-go's numbers are standard math / existing framework content.
- **No continuum-limit claim, no coupling value, no g_bare statement.**
- The no-go itself is **not** retired or contradicted; it is scoped.

## No-Go Discipline Boundary

This is not a `no_go` row and does not assert that all action-selection routes
fail. It does not claim an N1-N8 closure. The only negative statement is the
narrow one checked by the runner: continuum-equivalence does not identify the
candidate actions unless the `a→0` limit is actually taken. The residual
selection route remains open.

## Cross-references

- Scoped no-go: [`BRIDGE_GAP_ACTION_FORM_UNIQUENESS_NO_GO_NOTE_2026-05-06`](BRIDGE_GAP_ACTION_FORM_UNIQUENESS_NO_GO_NOTE_2026-05-06.md)
- Baseline reading: [`PHYSICAL_LATTICE_FOUNDATIONAL_INTERPRETATION_NOTE_2026-05-08`](PHYSICAL_LATTICE_FOUNDATIONAL_INTERPRETATION_NOTE_2026-05-08.md)
- HK candidate open follow-on, plain references only:
  `BRIDGE_GAP_HK_TIME_DERIVATION_NOTE_2026-05-06`,
  `BRIDGE_GAP_HK_PLAQUETTE_CLOSED_FORM_NOTE_2026-05-06`.
- Companion context, plain reference only: PR #3332 link-connection/fibre-frame review.
- Standard methodology (not imports): Drouffe–Zuber 1983; Menotti–Onofri 1981; heat kernel / Brownian motion on compact Lie groups (Helgason 1978).
