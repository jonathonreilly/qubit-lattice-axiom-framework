Reviewer model: claude-opus-5-5

# LOCE55 — (CAN-e): one estimate for (LOC-e) and (PL-1L); re-derivation of (LGF)

Role: Opus 5.5 WORKER (not a reviewer of others' work, but the REVIEW_BRIEF_55 rules apply).
Started: 2026-10-29 06:26 UTC.
Writes only: `$L/LOCE55.md` and `$L/checks/le55_*`.

## PRE-STATED (written before any derivation)

Targets (from the brief `queue/loce.md`):
- T1. State ONE estimate (CAN-e) with every norm and quantifier, such that (CAN-e) implies
  SRCAN55's (LOC-e) and TSE55's (PL-1L).
- T2. Prove (CAN-e) conditionally on named inputs: the per-step package (STEP55; incl. (B2) at
  levels >= 1), the flow (named), and a named large-field input -- OR isolate the obstruction precisely.
- T3. Re-derive (LGF) (the lattice Green's-function asymptotics TSE55 cited) from primitives
  (lattice Laplacian / field-strength propagator symbols in LINEAR_PACKAGE), with explicit error terms,
  in the form Theorem TS consumes.

What would count as a refutation / failure of each target (stated in advance):
- T1 fails if the stated (CAN-e) does not literally imply (LOC-e) as SRCAN55 consumes it (oscillation
  over coarse fields of the level-r term <= c_r ||h||_{L^1} l_ref^{-4}, sum_r c_r < infinity) or does
  not imply (PL-1L) as TSE55 consumes it (per-step contribution = one-loop running-coupling value up to
  relative u^{-theta}); or if one of the two is shown to need a strictly different object (then the
  "one estimate" premise of the brief is itself REFUTED and I must say so).
- T2 fails (obstruction, not proof) if any step needs an input not supplied by STEP55/flow/large-field
  input as stated in those files; in particular if the Codex a^{-4} singleton counterexample
  (CODEX_REVIEW_SRCAN items 7-8) applies to the argument -- i.e. if the argument controls only scalar
  flow quantities and not the first-order image of e. A proof that uses gauge invariance must exhibit
  the quadratic-in-curvature mechanism concretely (which operator, which norm), not assert it.
- T3 fails if the derived asymptotics differ from what TSE55 consumes (exponent, constant, or error
  term), if the error term is not explicit, or if a numeric constant used by Theorem TS cannot be
  reproduced by exact rational arithmetic in a pre-registered check. A check that could not fail
  (tautology, built from its own primitives) does not count.
- Any claim I make will carry a verdict label: PROVEN-HERE (load-bearing step derived in this file),
  CONDITIONAL (on named inputs), NOT-VERIFIED, or OBSTRUCTED (with the precise obstruction).

