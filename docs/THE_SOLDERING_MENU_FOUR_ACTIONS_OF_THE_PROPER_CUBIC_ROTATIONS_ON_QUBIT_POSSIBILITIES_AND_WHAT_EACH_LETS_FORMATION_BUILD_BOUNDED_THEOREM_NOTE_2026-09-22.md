---
claim_id: the_soldering_menu_four_actions_of_the_proper_cubic_rotations_on_qubit_possibilities_and_what_each_lets_formation_build_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "Admissibility names covariance under proper cubic rotations but not how they move possibilities. An action on possibilities is a homomorphism from the proper cubic group O (= S4) into the qubit's automorphisms (SO(3) on the Bloch ball). Up to conjugacy there are exactly four: trivial (the unsoldered reading), a sign twist (A1+2A2), axis soldering (A2+E, through the axis permutation) and full soldering (T1), proved by the S4 character table with the determinant character sign^(#A2 + #E + #T2) and exhibited by explicit integer matrices. Their kernels have orders 24, 12, 4, 1 and orbits 1, 1, 3, 6 on the six bond directions; neighbours in one kernel orbit formed after a centre get identical conditionals, which gives exact broadcast bounds: ice count 5/16, 5/16, 1/2, 1; odd Gauss parity 1/2, 1/2, 1/2, 1; parity-role link profile at most 16/243, at most 16/243, certain, certain. No action is adopted."

upstream_dependencies:
  - minimal_axioms
  - possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14
  - admissibility_six_neighbor_affine_cq_channel_solder_support_boundary_bounded_theorem_note_2026-08-14
runner: scripts/soldering_menu_four_cubic_actions_on_qubit_possibilities_and_formation_bounds_2026_09_22.py
---

# The soldering menu: four actions of the proper cubic rotations on qubit possibilities, and what each lets formation build

**Date:** 2026-09-22
**Type:** bounded_theorem
**Campaign:** next-steps campaign after the TOE derivation campaign by
underdetermination witnesses. In the second-edition assembly (open PR
8648) every established formation route to downstream gravity uses the
soldering decision. The possibility-covariance block treated soldering
as a fork between two readings. This block asks how many readings the
text actually admits, and what each lets nearest-neighbour formation
build.

## Result up front

1. **The covariance sentence admits exactly four actions on possibilities.**
   Admissibility requires covariance "under lattice translations and
   proper cubic rotations", and the Qubit axiom distinguishes
   possibilities "by the supplied algebraic structure alone", whose
   automorphisms are the proper rotations of the Bloch ball. How a
   lattice rotation moves a possibility is a homomorphism from the
   proper cubic group O (isomorphic to S4) into SO(3). Up to conjugacy
   there are exactly four:
   - trivial, the unsoldered reading;
   - a sign twist, diag(1, s, s), with s the sign of the axis permutation
     (A1 + 2A2);
   - axis soldering, s(g) |g|, which permutes the three axes (A2 + E);
   - full soldering, g itself (T1).

   Proof: a real three-dimensional representation of S4 splits into
   irreducibles, and its determinant is sign^(#A2 + #E + #T2). Of the
   eight splittings, exactly these four have determinant 1. T2, and
   A1 + E, fail on a quarter-turn.

2. **Each action leaves some bond directions indistinguishable.** A
   kernel element fixes every possibility but moves bond directions.
   The kernels have orders 24, 12, 4 and 1. Their orbits on the six
   directions number 1, 1, 3 and 6; under axis soldering the orbits are
   {+x, -x}, {+y, -y} and {+z, -z}. Neighbours in one orbit that form
   after a centre, seeing only it, get identical conditionals given the
   centre's record, so the centre can send one instruction per orbit
   only.

3. **Exact broadcast bounds per action** (trivial / sign twist / axis /
   full):
   - ice count (3 of 6 occupied): 5/16 / 5/16 / 1/2 / 1;
   - odd Gauss parity: 1/2 / 1/2 / 1/2 / 1;
   - parity-role link profile: at most 16/243 / at most 16/243 / certain
     / certain.

   Axis soldering ties +x to -x, so the occupied count comes in pairs
   and any odd total needs a coin. Full soldering can occupy three chosen
   directions, or set one link, with certainty.

4. **What the menu decides, in the broadcast order.**
   - Registering the parity-role skeleton by broadcast needs at least axis
     soldering.
   - Forming the ice support by vertex broadcast, the photon route of the
     ice-support block, needs full soldering.
   - Gauss parity by broadcast also needs full soldering; a checker formed
     last absorbs it under any action.
   - The sign twist behaves like the unsoldered reading for all three.

   These statements hold for the broadcast order, where the centre forms
   first and each neighbour sees only it. Other orders, in which a
   neighbour also sees other formed sites and relative geometry, are not
   classified here. In such orders an unsoldered rule might register a
   frame of its own.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "every established formation route to downstream gravity uses the soldering decision; determine the readings the covariance sentence admits and what each lets formation build"
source_of_blocker_text: assembly_graph_open_pr_8648
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "refine the assembly's soldering group into its four entries (full soldering for ice by broadcast, axis soldering for roles by broadcast); classify orders beyond broadcast, where unsoldered rules might register a frame; test record statistics that separate axis from full soldering"
conditional_surface_status: "actions on possibilities are homomorphisms into the qubit's automorphisms; the three star constraints and the broadcast order are the previous blocks'; no action adopted"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "the classification is exact character theory of a finite group with explicit matrices; the bounds are exact grid maxima with explicit maximisers"
```

## Premises and declared objects

O is the group of 24 signed permutation matrices of determinant 1, acting
on lattice positions. The qubit's automorphisms act on the Bloch ball as
SO(3). The covariance sentence is read as allowing any homomorphism
rho: O -> SO(3) as the action on possibilities; the unsoldered reading is
rho trivial, the soldered reading of the possibility-covariance block is
rho = identity. The star constraints (ice count, odd parity, role link
profile) and the broadcast order, in which the centre forms first and each
neighbour sees only it, are those of open PRs 8667 and 8669.

## Prior art and what is new

- Landed possibility-covariance note (2026-09-14): the fork between the
  independent internal action and the diagonal action. New here: the
  complete list of actions, two of them intermediate, with their
  kernels.
- Landed solder-support note (2026-08-14): the diagonal soldering, and
  the vanishing occupancy response under independent internal
  naturality. New here: the axis and sign-twist readings, and a
  formation-level separation of all four.
- Open PRs 8667 and 8669: the unsoldered bounds 5/16 and 16/243. New
  here: the bounds for every action, which show which reading each
  structure needs.

## Theorem 1 — Four actions

The four listed maps are homomorphisms into SO(3), checked on all 576
pairs, and their characters on the five classes (sizes 1, 6, 3, 8, 6) are
(3,3,3,3,3), (3,-1,3,3,-1), (3,-1,3,0,-1), (3,1,-1,0,-1). The five
irreducible characters of S4 are orthonormal. Among the eight splittings
of dimension three, the determinant rule leaves exactly 3A1, A1+2A2,
A2+E and T1. The constructed characters decompose into exactly those, so
the four actions are pairwise inequivalent and form the complete menu. T2 has
determinant -1 on a quarter-turn.

## Theorem 2 — Kernel orbits and broadcast bounds

If g lies in the kernel of rho, then covariance gives a neighbour at gd
the same conditional as a neighbour at d, whenever the centre is the
only formed neighbour of both: g fixes the centre's record and every
value. So neighbours in a kernel orbit are independent and identically
distributed given the centre. The bounds are the grid maxima of the
target probability over per-orbit occupation probabilities: 5/16 for one
orbit of six, 1/2 for three orbits of two (odd totals need an odd pair),
and 1 for six singleton orbits (explicit assignments). The role profile
needs V on the link's own axis and different plaquette letters on the
two transverse axes. It can be dictated exactly when each kernel orbit
needs a single letter: true for axis and full soldering, false for one
orbit. A control shows a partition merging the transverse axes also
fails.

## No-Go Discipline Gate

The negative content is scoped: under the trivial action, the sign twist
or axis soldering, a centre formed first cannot dictate the ice count or
odd parity to its neighbours with certainty; under the first two it
cannot dictate the role profile.

- **N1 alternative routes.** Checker-last orders, joint units, and rules
  in which neighbours also see each other are outside the broadcast
  bounds.
- **N2 wall independence.** Finite group theory and exact grid maxima.
- **N3 hidden walls.** The reading of the covariance sentence as a
  homomorphism into the qubit's automorphisms is stated; the star
  constraints are the previous blocks'.
- **N4 residual matching.** The soldering decision's residual is a choice
  among four named actions, each with a stated formation reach.
- **N5 rhetoric audit.** "Exactly four" is a classification up to
  conjugacy; the bounds are exact.
- **N6 partial-closure paths.** Record statistics that separate axis
  from full soldering on finished windows are open.
- **N7 steelman.** For the intermediate readings: axis soldering is the
  least structure that registers the roles. Against them as a photon
  route: the ice count's 1/2 bound. Both are recorded.
- **N8 cross-cycle echo.** The two-reading fork of the
  possibility-covariance block is the trivial-and-full slice of this
  menu.

## Falsifiers

- A homomorphism O -> SO(3) not conjugate to one of the four, a failed
  homomorphism or orthogonality check, or a character decomposition other
  than stated falsifies Theorem 1.
- A broadcast rule beating a stated bound under the stated action, or a
  kernel of different order, falsifies Theorem 2.

## Boundaries and non-claims

No action is adopted. The classification concerns actions of the proper
cubic rotations on possibilities through the qubit's automorphisms;
antiunitary maps are not automorphisms and are excluded. The bounds
concern the broadcast order only. No physical identification is made.
Nothing here grades, unlocks or audits any other claim.

## Imports

Standard character theory of a finite group; the landed and open notes
cited. No audit grade, no new axiom, no new primitive, no new comparator
and no new framing is imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:** (i) the actions verified as homomorphisms
  entry by entry, and separately classified by characters; (ii) the
  kernels computed as sets of group elements and their orbits by direct
  action; (iii) each bound computed as a grid maximum and checked against
  an explicit assignment attaining it.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| mutation | substitution | result |
|---|---|---|
| axis action loses the sign | s(g)\|g\| to \|g\| | caught (2 FAILs) |
| sign twist on one entry only | diag(1, s, 1) | caught (2 FAILs) |
| E character wrong on 120 degrees | -1 to 1 | caught (2 FAILs) |
| E counted as determinant-neutral | determinant rule | caught (1 FAIL) |
| kernel read as a stabiliser | kernel test changed | caught (4 FAILs) |
| ice target 3 to 2 | wrong count | caught (2 FAILs) |
| odd parity factor wrong | (1-2p) to (1-p) | caught after strengthening (1 FAIL; one formula now serves every parity check) |
| profile ignores the plaquette letters | P_xy, P_xz merged | caught after strengthening (1 FAIL; merged-axis control) |

  Eight of eight mutants are caught, two after strengthening.
- **Vacuity guard:** every classification claim is compared with
  independently computed characters; every bound has an explicit
  maximiser.
- **Budget:** 10 checks, stdout 1852 characters (ceiling 6000), 0.5 s
  (ceiling 900 s), exact Fractions and integer matrices.

## Verification

```bash
python3 scripts/soldering_menu_four_cubic_actions_on_qubit_possibilities_and_formation_bounds_2026_09_22.py
```

Expected summary line: `TOTAL: PASS=10 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/soldering_menu_four_cubic_actions_on_qubit_possibilities_and_formation_bounds_2026_09_22.txt`.
