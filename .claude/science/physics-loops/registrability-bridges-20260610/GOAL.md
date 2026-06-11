# GOAL — registrability-bridges-20260610

## Goal text (verbatim from request)

> Close (or honestly bound) the two registrability bridges that gate both
> remaining Tier-A admission retirements — (a) the strong-CP
> determinant-readout bridge and (b) the AC_phi_lambda unordered-multiset /
> PL/ABSS equivariant global bridge.

## Mode / runtime / target

- mode: `run` → campaign (8h unattended work budget)
- runtime: 8h work budget
- target: `best-honest-status`
- loop slug: `registrability-bridges-20260610`

## The two genuine Tier-A admissions (verified on origin/main)

`docs/audit/data/tier_a_admissions.json` (origin/main) lists exactly two
genuine admitted derivation targets:

| id | label | leverage | statement |
|---|---|---|---|
| `staggered_dirac_realization_gate_note_2026-05-03` | `AC_phi_lambda` | 41 | generation mass-pattern input: the C_3-breaking phase/orientation plus the abstract-sector to physical-species bridge; bare e/mu/tau naming is a convention |
| `strong_cp_theta_zero_note` | `theta` | 20 | QCD vacuum angle theta = 0 (strong-CP); also unsolved in the SM |

Both gate substantial downstream fan-out (AC_phi_lambda: 65 inbound dependers
per PR #3428; theta: 124 transitive descendants per the strong-CP audit).

## The two named blockers (direct_blocker_closure targets) — quoted verbatim

### Blocker (a) — θ P2 determinant-readout bridge

From `docs/TIER_A_KORBIT_DETERMINANT_AND_ORIENTATION_INVARIANCE_BOUNDED_NOTE_2026-06-09.md`:

> To discharge that premise, a later retained bridge must show that the
> physical `arg det(M_u M_d)` contribution used by `STRONG_CP_THETA_ZERO_NOTE.md`
> is exhausted by this determinant-class registrable readout, and that no
> phase-sensitive non-multiplicative or action-level datum remains relevant to
> that premise. Until that bridge exists, the positive-real mass orientation
> remains an explicit condition of the strong-CP selected surface.

Hostile guard (must be respected): K/CPT orbit invariance alone gives
evenness, not phase erasure (`cos(arg z)` is K-invariant yet phase-dependent).
The bridge must establish the multiplicative determinant-character class as
*exhaustive* for the registrable mass-surface readout, from the Record axiom
boundary + retained surfaces only.

### Blocker (b) — AC_phi_lambda registrability bridge

From the same note's Registry Consequence:

> the orientation lemma may help reduce the admission to a magnitude-only atom
> only after the unordered-multiset registrability bridge is retained or
> confirmed as already supplied by existing audited surfaces.

PR #3428 owner-review surviving irreducible (verbatim from PR body):

```
R1b  the semantic matter anchor: "the hw=1 triplet is the physical generation
     sector" (carrier surface retained_bounded; imports NO number/phase/knob)
R2   the PL/ABSS equivariant global bridge (the retained arithmetic's named open)
R3   audit ratifications (the in-review package + the scheme-forcing note)
```

R2's exact statement, grounded in
`docs/KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`
(retained_bounded, audited_clean), Part D: the global geometric identification
`Cl(3)/Z^3 -> PL S^3 x R` provably requires the PL Poincare conjecture
(Perelman), TOP=PL in dim 3 (Moise), and van Kampen `pi_1 = 0` — all standard
external mathematics, named LIVE (a derivation target, not a foreclosure), not
on the framework surface.

The "confirmed as already supplied by existing audited surfaces" branch is a
valid closure shape: a route that PROVES the bridge is already implied by
retained rows (citing exact ledger rows by effective_status) closes the blocker.

## Hard constraints (binding)

- **Record axiom boundary (exact).** Record states durable realized-outcome
  registration ONLY: given a *supplied* readout context with a finite
  central-sector decomposition and a fixed K/CPT conjugation, the realized
  outcome is the K/CPT orbit of the realized central sector, and scalar readout
  is finitely additive over finite pairwise-disjoint record collections. It
  supplies NO readout context, decomposition, K/CPT structure, sector-generation
  rule, weighting, normalization, probability, P2/modulus, log-det,
  source/action, scale, or observable identification. Any bridge MUST respect
  this exactly.
- **No new axiom / no new primitive / no new import** without user approval.
  If a bridge truly requires a new primitive, that is an infeasible-as-stated
  finding with the wall named (recorded via the N1-N8 no-go gate), NOT a license
  to add one.
- **Both blockers live on the same layer** — what is registrable through
  Record's supplied readout context. Check early whether one theorem closes both
  before building two.

## Loop-start inherited PRs (historical; verify current state before acting)

These states were captured at loop start on 2026-06-11 and are not a live queue
snapshot.

| PR | title | state | head |
|---|---|---|---|
| #3509 | theta-chain dep wiring honesty repair | OPEN | science/theta-p1-p2-dep-wiring-repair-2026-06-10 |
| #3510 | microcausality conditional repair | OPEN | science/microcausality-quasilocality-dep-edge-2026-06-10 |
| #3511 | retire theta from Tier-A registry (GATED) | OPEN | audit-infra/retire-theta-tier-a-registry-2026-06-10 |
| #3512 | queue readiness honors accepted premises | OPEN | audit-infra/queue-ready-accepted-premises-2026-06-10 |

PR #3511 is the GATED θ-registry retirement; its named PENDING gate IS blocker
(a). Closing/bounding (a) directly informs whether #3511's gate can lift.

## Deliverable shape (per coherent block)

One source note (docs/, controlled vocab, `proposed_*` status only,
markdown-linked load-bearing deps) + one paired runner
(scripts/frontier_*, derives-not-asserts, prints SCORECARD PASS/FAIL) + one
cached output (logs/runner-cache/) + one review PR. V1-V5 promotion gate and
N1-N8 no-go gate applied before any PR.
