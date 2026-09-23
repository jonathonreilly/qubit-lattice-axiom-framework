---
claim_id: strong_cycle_letters_are_generic_every_obstruction_is_a_nontrivial_angle_relation_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "Cycle letters are three cycles of four angles c_{j,k} on the circle with each cycle summing to 0; they are strong (open PR 8856) when they decode, every square of links is straight for every sign pattern, and (U) holds under the rotation-covariant rule. Each failure of these conditions is an integer linear relation among the angles, modulo a full turn. With the cycle sums imposed, the angles have 9 free parameters. Every decoding coincidence and every vanishing angle reduces to a nonzero relation (135 hyperplanes); every non-straight square configuration reduces to a nonzero relation and every straight one to the zero relation (73344 non-straight configurations on 3645 hyperplanes); and the 24576 covariant stars have pairwise distinct symbolic neighbour classes, so a (U) collision needs a nonzero relation. The letters therefore fail to be strong only on a finite union of hyperplanes: on the continuous circle almost every choice of cycle angles is strong, and modulo a prime m a nonzero relation holds on a fraction 1/m of the parameter space. Random cycle sets are strong in 1, 34 and 56 of 60 samples at m = 1009, 10007 and 100003, and at the two larger primes the bad fraction lies within a factor 4 of H/m with H = 3780. No reading, rule, alphabet, unit or order law is adopted."

upstream_dependencies:
  - minimal_axioms
  - possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14
runner: scripts/strong_cycle_letters_are_generic_every_obstruction_is_a_nontrivial_angle_relation_2026_09_23.py
---

# Strong cycle letters are generic: every obstruction is a nontrivial angle relation

**Date:** 2026-09-23
**Type:** bounded_theorem
**Campaign:** second next-steps campaign. Open PR 8856 showed that strong
cycle letters record the frame and the roles on every window under the
rotation-covariant rule, and exhibited one strong set. This block asks how
special such letters are.

## Result up front

1. **Obstructions are angle relations.** Three conditions make cycle
   letters strong: decoding, straight squares for every sign pattern, and
   (U) under the rotation-covariant rule. Each failure is an integer linear
   relation among the twelve angles, holding modulo a full turn. The three
   cycle sums leave 9 free parameters.

2. **None of them is automatic.**
   - Every coincidence of two signed angles, and every vanishing angle,
     reduces to a nonzero relation in the 9 parameters: 135 hyperplanes.
   - Every non-straight square configuration reduces to a nonzero relation,
     and every straight one to the zero relation: 73344 configurations on
     3645 hyperplanes.
   - The 24576 covariant stars have pairwise distinct symbolic neighbour
     classes, so a (U) collision needs a nonzero relation.

3. **Strong letters are generic.** The letters fail to be strong only on a
   finite union of hyperplanes. On the continuous circle, almost every
   choice of cycle angles is strong. Modulo a prime m, each nonzero relation
   holds on a fraction 1/m of the parameter space.

4. **The count agrees with sampling.** Random cycle sets are strong in 1, 34
   and 56 of 60 samples at m = 1009, 10007 and 100003. At the two larger
   primes the bad fraction lies within a factor 4 of H/m, where H = 3780
   counts the decoding and square hyperplanes.

5. **What this means.** Under possibility covariance, the alphabet behind
   the relational route to roles is a choice of structure, three cycles of
   four angles, and not of values. Any generic angles work, and no
   particular angle is tuned.

## Machine status and trace

- **Runner:**
  `scripts/strong_cycle_letters_are_generic_every_obstruction_is_a_nontrivial_angle_relation_2026_09_23.py`
- **Result:** `TOTAL: PASS=6 FAIL=0`, about 7 s, stdout 943 characters.
- **Cache:**
  `logs/runner-cache/strong_cycle_letters_are_generic_every_obstruction_is_a_nontrivial_angle_relation_2026_09_23.txt`
- **Arithmetic:** integer coefficient vectors over the 9 free angles;
  sampling with fixed seeds.

## Premises and declared objects

- **Strong cycle letters** and the rotation-covariant rule (open PRs 8854
  and 8856).
- **Parameters:** c_{j,0}, c_{j,1}, c_{j,2} free for each cycle j, and
  c_{j,3} = −(c_{j,0} + c_{j,1} + c_{j,2}).

## Prior art and what is new

- Open PR 8856: strong letters, the folded-spiral theorem and one strong
  set.
- New here: every obstruction is a nontrivial relation; the hyperplane
  count; the sampling check.

## Theorem — Genericity

A condition fails exactly when some integer relation among the angles
holds modulo a full turn. Every such relation reduces, in the 9 free
parameters, to a nonzero integer vector; the runner checks this for all
decoding and square relations. For (U), two stars collide only if their
five neighbour-class forms agree, and the runner checks that the symbolic
forms of distinct stars differ, so some difference is a nonzero relation.
A nonzero integer relation cuts a closed set of measure zero from the torus
of angles. There are finitely many such relations, so their union has
measure zero, and its complement, the strong letters, has full measure.

## No-Go Discipline Gate

- **N1 alternative routes.** Other letter structures are outside this
  block.
- **N2 wall independence.** Symbolic reduction and an independent sampling
  check.
- **N3 hidden walls.** The cycle-sum parametrisation is checked directly.
- **N4 residual matching.** Only the hyperplanes are excluded.
- **N5 rhetoric audit.** "Generic" means outside a finite union of
  hyperplanes, a set of measure zero.
- **N6 partial-closure paths.** The smallest strong modulus is not
  computed.
- **N7 steelman.** For tuning: small moduli are rarely strong. Against: on
  the circle, almost every choice is strong. Both are recorded.
- **N8 cross-cycle echo.** Open PRs 8752, 8854 and 8856 are cited.

## Falsifiers

- A decoding, square or neighbour-class obstruction that reduces to the
  zero vector.
- A straight square that reduces to a nonzero relation.

## Boundaries and non-claims

- Cycle letters with three cycles of four angles and zero cycle sums.
- No reading, rule, alphabet, unit or order law is adopted.
- Nothing here grades, unlocks or audits any other claim.

## Imports

The minimal axioms, open PRs 8752, 8854 and 8856 and the landed
possibility-covariance note are cited. No audit grade, no new axiom, no new
primitive, no new comparator and no new framing is imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:** symbolic reduction, the parametrisation check,
  and random sampling modulo three primes.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| Mutant | Change | Result |
|---|---|---|
| fourth angle with the wrong sign | sign flipped | caught (1 FAIL) |
| hyperplanes without sign normalisation | normalisation removed | caught (2 FAILs) |
| straight test ignoring phases and senses | test weakened | caught (1 FAIL) |
| U key without the forward part | key shortened | caught (1 FAIL) |
| free angles scaled | scale 2 | caught (3 FAILs) |
| squares with X = Y admitted | constraint dropped | equivalent (see below) |
| decoding over one sign only | signs halved | caught (1 FAIL) |
| thirty samples | sample halved | caught (2 FAILs) |

  7 of 7 defect mutants are caught. Admitting X = Y adds only relations
  already among the 3645 hyperplanes, so it changes no output.

- **Vacuity guard:** hyperplane, configuration and sample counts are
  printed.
- **Budget:** 6 checks, stdout 943 characters (ceiling 6000), about 7 s.

## Verification

```bash
python3 scripts/strong_cycle_letters_are_generic_every_obstruction_is_a_nontrivial_angle_relation_2026_09_23.py
```

Expected summary line: `TOTAL: PASS=6 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/strong_cycle_letters_are_generic_every_obstruction_is_a_nontrivial_angle_relation_2026_09_23.txt`.
