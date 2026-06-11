# ROUTE_PORTFOLIO — registrability-bridges-20260610

Routes scored by likely claim-state movement. Both blockers share the
Record-registrability layer; the portfolio is organized around the shared-core
theorem first, then the residual split.

## Route R-1 (PRIMARY): shared-core registrability theorem (additive + even = phase-free)

**Statement.** From the Record axiom boundary alone, prove: in a supplied
readout context, a scalar readout that is (i) additive over disjoint sector
records and (ii) constant on K/CPT orbits carries no additive phase information;
equivalently the determinant *phase* character has `k = 0` not by assuming the
det-class but by deriving that additive+even phase data vanish.

**Closes:**
- blocker (a): the physical arg det(M_u M_d) = sum of sector phases is additive;
  registration keeps only its K/CPT-even part = 0; so it is exhausted by the
  modulus (phase-free) registrable readout. Hostile guard threaded: the proof
  does NOT use evenness alone (cos(arg z) excluded as non-additive, not
  Record-constrained).
- blocker (b-i): the eigenvalue-label/sign flip delta -> -delta IS the K/CPT
  conjugation; its odd part is unregistrable by the same theorem; so the
  registrable species surface is the unordered (K/CPT-orbit) multiset, reducing
  AC_phi_lambda to the magnitude-only atom |delta|.

**Trace class:** `direct_blocker_closure` (two quoted blockers).
**Risk:** the proof must avoid a hidden regularity/linearity assumption. The
final route uses only the algebraic fact that additive `R`-valued functions are
odd, so Cauchy/Hamel pathologies do not matter. Score: HIGH value, MEDIUM risk.
DO FIRST.

## Route R-2: residual split for blocker (b) — is R2 (PL/ABSS) load-bearing for registrability?

**Statement.** Determine whether the unordered-multiset registrability bridge
(b-i) routes through the PL/ABSS global identification (R2) at all, or whether
R2 is load-bearing ONLY for the separate eta-invariant / single-summand readout
(which is NOT the registrability question). If (b-i) is independent of R2, then:
- (b-i) closes via R-1;
- (b-ii)/R2 is honestly bounded as external-math LIVE (Perelman/Moise/van
  Kampen), an import-required wall, recorded via N1-N8.

**Trace class:** `negative_route_pruning` (prunes the claim that R2 blocks the
registrability reduction) + `direct_blocker_closure` boundary on (b-ii).
Score: HIGH value (clarifies what actually remains), LOW risk. DO SECOND.

## Route R-3: strong-CP premise-2 isolation (what remains after R-1 for theta)

**Statement.** After R-1 exhausts the det-phase readout, the strong-CP surface
still carries premise 1 ("no bare theta slot is admissible", RP-no-go'd) as a
SEPARATE action-surface premise. R-1 closes ONLY premise 2 (mass orientation).
Make explicit, with the ledger, exactly which strong-CP premises R-1 retires
and which survive, so PR #3511's gate is correctly characterized (the
det-readout bridge lifts the mass-orientation gate; the action-form premise is
a distinct surviving gate).

**Trace class:** `direct_blocker_closure` (PR #3511 named gate) + honest
residual. Score: MEDIUM value, LOW risk. DO THIRD (folds into R-1's note as the
"what this does not close" boundary, or a short companion).

## Route R-4 (stretch / fallback): if R-1's additivity step fails

If finiteness does NOT remove the additivity pathology, or if a registrable
non-additive even readout genuinely exists, then R-1 becomes a bounded result
("the det-phase is unregistrable WITHIN the additive class; a non-additive
registrable even readout is not excluded"), and the honest output is a
bounded-support + named residual. This is the N1-N8 fallback shape. Recorded so
the loop does not overclaim if the math resists.

## Decision

Execute R-1 first as a single coherent block (it closes/bounds the shared core
of BOTH blockers). R-2 and R-3 fold into the same note as boundary sections OR
become a short second block if substantial. This honors the request's
"check early whether one theorem closes both before building two."
