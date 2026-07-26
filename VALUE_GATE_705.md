# Promotion Value Gate — Cycle 705

Answered in writing before opening any PR, per `~/TOE_NEXT_2026-07-25.md`.

## Prior-art sweep (workflow step 2, PR #5611)

- **Ref refreshed:** `git fetch origin main:refs/remotes/origin/main`
- **Searched commit:** `0adcfef114b1f3e2a5fa646a89644dce16665e67`
- **Searched on the statement, not the lane name.** Commands run:
  - `git grep -l -iE "distinguishab|confusab|non-orthogonal|overlap floor" origin/main -- docs/*.md`
  - `git grep -l -iE "minimal orbit|smallest orbit|orbit of size six|face orbit|six-element" origin/main -- docs/*.md`
  - `git grep -l -iE "Tr\(rho|state overlap|fidelity" origin/main -- docs/*.md`
  - `git grep -n -iE "(A0|availability set)[^.]{0,120}(at least six|six element|>= 6|at least 6|minimum size|cardinalit)" origin/main -- docs/*.md`
  - `git grep -n -iE "availab[^.]{0,100}(distinguishab|orthogonal|overlap)" origin/main -- docs/*.md`
  - `git grep -n -iE "pairwise (non-?positive|obtuse)|at most 2d|antipodal pair" origin/main -- docs/*.md`
  - `git grep -n -iE "realized alphabet[^.]{0,120}(size|six|orthogonal|distinguish)" origin/main -- docs/*.md`

**Hits and classification.** The two conjunction searches — the ones that
would catch this statement — returned **zero** hits. Of the broad hits:

| hit | classification |
|---|---|
| `INFORMATIVE_FRACTION_COVARIANT_RULE_QUANTIZATION_..._2026-07-02` (64 neighbour patterns → 10 orbits, "antipodal pair" rows) | **different object.** Orbits of the *condition* domain (binary neighbour patterns), not of the *content* sphere. No overlap functional. Not duplicative. |
| `BORN_FORM_SCALED_PROJECTOR_MENU_..._2026-07-17`, `BORN_FORM_EFFECT_MENU_..._2026-07-17` (antipodal pairs, projector menus) | **adjacent, different question.** These classify gradings on projector *menus* and the paired-menu boundary. They do not treat `A0`, cubic orbits, or a confusability floor. Not duplicative. |
| `READOUT_BRIDGE_..._2026-07-06` ("orthogonal rank-1 projections in `M_2` are antipodal Bloch pairs") | **prior art I depend on.** Cited as landed usage for Theorem 5 rather than re-derived. |
| `EMPTY_STATE_BOOTSTRAP_..._2026-07-04`, `BOOTSTRAP_CONTINUATION_..._2026-07-04` | **the parents.** Supply `A0` nonempty, proper-invariant, the orbit dichotomy, and the residual. Cited; their content is not restated as new. |

No landed note states an overlap/confusability floor on `A0`, the uniqueness
of the face orbit as saturator, or a chirality cost. Sweep is clean.

## V1 — What is the claim, in one sentence?

Every nonempty proper-cubic-invariant first availability set has
confusability `conf(A0) = max_{v != w} Tr(P_v P_w) >= 1/2`, attained **only**
by the face orbit `<100>`, while every chiral `A0` has `conf >= 2/3` — so the
two sides of the free-orbit residual are separated by an exact gap.

## V2 — Is it new relative to `main` at the searched commit?

Yes, at `0adcfef114`. The parents classify `A0`'s orbits and reduce chirality
to unpaired free off-mirror orbits; **no landed note applies a state-overlap
functional to `A0` at all.** The three exact values (1/2, 2/3, 3/4), the
uniqueness of the saturator, the `2/3` chirality floor, and the
zero-distinguishable-pairs property of chiral alphabets are new.

## V3 — Is it load-bearing, or decoration?

Load-bearing on a named open residual. Residual 1 of the landed bootstrap
continuation asked "which side the fixed rule's `A0` sits on" and recorded the
two sides as **symmetric**. They are not symmetric. This does not close the
residual — and the note says so plainly — but it converts an open-ended search
into a single named sentence (`conf(A0) < 2/3`) whose adoption would close it.

Secondary load-bearing result: Theorem 5 says every lawful first alphabet is
at least 6 wide while at most 2 of its contents are mutually distinguishable,
and a chiral one has **no** distinguishable pair. That is a statement about
the readability of the record alphabet, on the Record axiom's own surface.

## V4 — What does it cost? Any new axiom, primitive, or import?

**None.** No axiom, no primitive, no dimensionless import, no counting
convention. The overlap `Tr(P_v P_w) = (1 + v.w)/2` is forced by the
`Cl(3,0)` algebra the Qubit clause already supplies — it is an algebraic
identity, not a normalization choice, which is why it survives the standing
"one dimensionful import, zero dimensionless imports" bar.

Two things are *carried*, both from `main` and both flagged in Scope: the
polar-vector content model (a named model, the largest scope limit) and the
Bloch-projector state reading (landed usage). The minimality premise that
would settle the residual is **named and explicitly not adopted**.

## V5 — Would an independent reviewer at the searched commit call it thin?

I do not think so, and the specific defences are:

- The theorems are **general**, not scan artifacts. Theorem 1 is
  orbit-stabilizer plus "no 6-fold axis"; Theorem 3/4 is the quarter-turn
  identity. The 290-direction scan is labelled a witness in both the note and
  the runner.
- The result is **exact rational arithmetic** end to end, with a wrong-formula
  control (C3), an invariance-is-load-bearing control (C9), and a control that
  **bounds the claim**: a rotated frame ties `1/2` without being invariant, so
  the note explicitly denies that `1/2` is special to invariance.
- The note **states what it does not do** in six scope bullets, including that
  it does not settle the residual and supplies no formation rule.
- Two construction-time errors (a mixed-length control set; a union check
  comparing different radii while passing) are **recorded in the note**, not
  silently fixed, and the assertion that caught them is retained in the runner.

**Risk I would flag to a reviewer myself:** the whole result is downstream of
the polar-vector content model, which is a named model rather than axiom
content. If a reviewer rejects that model the arithmetic is untouched but the
physical reading goes. The note says this in the first Scope bullet and calls
it the largest scope limit, rather than burying it.

## Verdict

**Proceed to cluster-cap evaluation.** Runner 9 PASS / 0 FAIL, cold-run in an
isolated worktree at `6cf0dcf0eb`, receipt pinned to the committed blob
(`ac7e3450...`, PIN MATCH).
