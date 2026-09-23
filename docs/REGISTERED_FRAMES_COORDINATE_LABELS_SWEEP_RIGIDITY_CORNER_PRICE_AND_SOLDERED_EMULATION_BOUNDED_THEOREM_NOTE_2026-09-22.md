---
claim_id: registered_frames_coordinate_labels_sweep_rigidity_corner_price_and_soldered_emulation_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "Formation model with supplied skip-and-continue semantics, fixed external orders, fresh conditional draws, and unsoldered covariance. Letters carrying coordinate labels c in Z_4^K with a tag let the record carry the lattice frame (c(x) = c0 + sigma(x) mod 4, sigma sending the three lattice directions to generators of different axes), although the rule never sees a direction. For K=3 in a sweep, where every site forms after its three back-neighbours, the complete stationary records of the three-neighbour rule on Z^3 are exactly the frames aligned with the sweep (plaquette and frame lemmas; complete search on the torus Z_4^3 finds exactly 6 with c(0) = 0). A record with a frame carries the ice support (a link is occupied when its odd label coordinate is 1) and the parity-role letters, and emulates a soldered rule: for the soldered ice vertex-record rule on one vertex star the pulled-back law is exact in each frame. At a first formation the frame has a price set by the order: in corner growth the corner's three forward neighbours are independent and identically distributed, so the frame has probability at most (m-1)(m-2)/m^2 for m letters, and (K-1)(K-2)/K^2 for coordinate labels (2/9 at K = 3), attained; from a centre at most 1/972; a designed order reaches the frame with probability 1 on five listed boxes. No rule, reading, alphabet or order law is adopted."

upstream_dependencies:
  - minimal_axioms
runner: scripts/registered_frames_coordinate_labels_sweep_rigidity_corner_price_and_soldered_emulation_2026_09_22.py
---

# Registered frames: coordinate labels let an unsoldered rule carry the lattice frame; sweep rigidity, the price at a first formation, and emulation of soldered rules

**Date:** 2026-09-22
**Type:** bounded_theorem
The [framework axioms](MINIMAL_AXIOMS_2026-06-29.md) do not select the
abstract record alphabet or stochastic model used below. In the formation
models an external fixed order is supplied, and each draw uses fresh
randomness conditional on its already formed nearest neighbours. These are
stronger conditions than equality of one-site marginals. Skipping failed
attempts and continuing is also supplied; it is not implied by unreadability.
Random/adaptive orders and correlated draws are outside the exclusions.
The static models instead test the explicitly defined conditional-locality
property on a supplied finite joint law. No qubit encoding, physical
realizability, retained grade, photon identification or gravity conclusion
is established by these abstract finite models.


## Result up front

1. **Letters can carry what the rule cannot see.** Under the unsoldered
   reading a rule sees its formed neighbours' values and their relative
   geometry, never a bond direction. A letter can still carry a
   coordinate label c in Z_4^3, with a small tag. A rule can then require
   that its formed neighbours' labels differ from its own by distinct
   generators. A record carries a frame when c(x) = c0 + sigma(x) mod 4
   for a map sigma from the three lattice directions to generators of
   three different axes. In such a record every site reads each
   neighbour's direction as a label difference.

2. **In a sweep the frame is forced.** For K=3, in a sweep every site forms after
   its three back-neighbours, one along each of three perpendicular
   directions (open PR 8670). Let each site take the unique label whose
   differences from its back-neighbours' labels are distinct positive
   generators. On Z^3 the complete stationary records are then exactly the
   frames aligned with the sweep: sigma(d_i) = u_pi(i) for one
   permutation pi, plus an offset. A complete search on the torus Z_4^3
   finds exactly 6 such records with c(0) = 0, all aligned. The sweep's
   frame is copied into the record. The soldered supports of open PR 8670
   carried that frame without showing it. The rule does not fix which
   aligned frame or offset occurs, because a sweep has no first formation.

3. **A record with a frame carries the ice support and the roles, and
   emulates soldering.** Read a link as occupied when its one odd label
   coordinate is 1. Every vertex then has exactly one occupied link per
   axis, which is exactly 3 of 6, the ice support. The parity-role letter
   of every site is the weight of its label modulo 2. Both hold on all 6
   torus records and on every frame record of a 7x7x7 box. More
   generally, an unsoldered rule reads each formed neighbour's direction
   from its label difference and can apply any soldered rule in label
   coordinates. For the soldered ice vertex-record rule of open PR 8667 on
   one vertex star, the emulator's law pulled back by each of the six
   frames equals the soldered law exactly: (1/8)/C(3, 3-m), where m is the
   number of occupied back-links.

4. **At a first formation the frame has a price that depends on the
   order.**
   - *Corner growth.* Every site forms after its back-neighbours and
     before its forward neighbours. The corner's three forward neighbours
     each form seeing only the corner. The supplied fresh-draw convention and unsoldered covariance make their
     letters conditionally independent and identically distributed. They are
     pairwise distinct with probability 6 e_3(p) <= (m-1)(m-2)/m^2 for a
     law p on m letters. With labels in Z_4^K they must lie on three
     different axes, which gives at most (K-1)(K-2)/K^2, that is 2/9 at
     K = 3.
   - *The bound is attained.* The explicit corner rule gives
     P(no unrecorded site) = P(frame) = 2/9 on four boxes, with each of
     the 6 frames at mass 1/27, and 3/8 at K = 4. Every failure leaves an
     unrecorded site. The finished law is the same for every corner-growth
     order.
   - *Broadcast from a centre.* All six neighbours are i.i.d. A frame
     then costs 48 prod(p) <= 1/972.
   - *A designed order pays nothing.* One forward neighbour of the corner
     forms alone. The other two form after a site that carries a label
     derived from it. Their configurations then differ, and an unsoldered
     rule builds the identity frame with probability 1 (five boxes, up to
     6x5x4). The order fixes the frame.

5. **Scope.** These are conditional mathematical results. No exhaustive
   decision set, physical necessity or infinite-volume phase is inferred.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "test the explicitly supplied finite record models within their stated domains"
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "test extensions beyond the finite hypotheses; no physical downstream conclusion is established"
conditional_surface_status: "formation reading; supplied failure convention; unsoldered reading; coordinate-letter alphabet, rules and orders declared; the soldered ice vertex-record rule supplied as the emulated rule; supplied superlattice roles for the reference law"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "Theorems 1 and 4 have short complete proofs with their finite cores checked by complete enumeration; Theorems 2, 3 and 5 are exact enumerations on declared windows and orders"
```

## Premises and declared objects

Admissibility as written: one fixed nearest-neighbour rule, covariant
under lattice translations and proper cubic rotations, with each site's
distribution determined by, and varying with, its nearest-neighbour
conditions. Formation model with supplied skip-and-continue semantics: a site with
no admissible possibility carries no record, and formation continues. The
unsoldered reading of the landed possibility-covariance note: rotating
positions with values fixed leaves the rule unchanged.

Declared objects:
- *Coordinate letters* (c, t), with c in Z_4^K and the generators u_i.
- *The corner rule*, with tags N, axis i and B:
  - no formed neighbour: (0, N);
  - one neighbour tagged N: a uniform axis i, giving (u_i, i);
  - one neighbour tagged axis i: continue along u_i;
  - two or three mutually perpendicular neighbours: the unique label whose
    differences from theirs are distinct positive generators;
  - anything else: unrecorded.
- *The designed rule and designed order* of Theorem 5.
- *The emulator* of Theorem 3.
- *Orders:*
  - corner growth from the corner of a box;
  - broadcast from a centre;
  - the designed order;
  - the sweep, read on Z^3 and on the torus Z_4^3 as a stationary
    condition: each site equals the rule's output on its three sweep
    back-neighbours.
- *Roles and the ice rule:* the superlattice roles (parity vectors) of the
  landed roles note, and the soldered ice vertex-record rule of open
  PR 8667.

## Relation to earlier work

The mathematical models and proofs used here are stated locally. Earlier
campaign labels and open-PR comparisons supply no load-bearing premise.

## Exact target and obligation graph

Target: can the unsoldered reading register the lattice frame in the
record, so that the formation routes to the ice support and the roles do
not need soldering?

- O1: sweep rigidity (Theorem 1).
- O2: readouts of ice and roles (Theorem 2).
- O3: emulation of a soldered rule (Theorem 3).
- O4: the price at a first formation, with its sharpness (Theorem 4).
- O5: an order with no price (Theorem 5).

## Theorem 1 — Sweep rigidity

For K=3, let a sweep have signed frame (d_1, d_2, d_3), so site s forms after
s - d_1, s - d_2, s - d_3. In a complete stationary record, each site's
label satisfies c(s) - c(s - d_i) = u_{pi_s(i)} for a permutation pi_s.

Take the two paths from s - d_i - d_j to s. They give

u_{pi_s(i)} + u_{pi_{s-d_i}(j)} = u_{pi_s(j)} + u_{pi_{s-d_j}(i)}.

The plaquette lemma says that u_a + u_b = u_c + u_d mod 4 holds exactly
when {a, b} = {c, d}. Together with pi_s(i) != pi_s(j), it gives
pi_s(i) = pi_{s-d_j}(i). So pi_s(i) depends only on the coordinate
s.d_i.

The frame lemma: if f_1, f_2, f_3 always give a permutation, each is
constant. Indeed, if f_1 took two values, f_2 and f_3 would both have to
equal the third value, and then (f_1, f_2, f_3) would not be a
permutation. So pi is constant, and c(s) = c0 + sum_i (s.d_i) u_pi(i).

Checks:
- the plaquette lemma, all 81 cases;
- the frame lemma on Z_3: all 19683 triples, of which 6 survive, all
  constant;
- a complete search on the torus Z_4^3: exactly 6 stationary records with
  c(0) = 0, each an aligned frame.

## Theorem 2 — What a frame carries

Vertices are the sites with all-even labels and links those with one odd
label coordinate. A vertex's two links along one axis have that
coordinate equal to e + 1 and e - 1 for an even e, which is 1 and 3 in
some order. So reading "occupied when the odd coordinate is 1" gives
exactly one occupied link per axis, and 3 of 6: the ice support. The
weight of a label modulo 2 is the site's parity-role letter, in the phase
set by c0 modulo 2.

Checks:
- all 6 torus records, at 8 vertices and 64 sites;
- the 6 frame records of corner growth on 7x7x7, at 8 interior vertices
  and all 343 sites.

The carried ice configuration is the same for all six corner frames.

## Theorem 3 — Emulation of a soldered rule

On a record with a frame, the emulator works in three steps:
1. a forming site takes its label by the coordinate rule;
2. it reads each formed neighbour's direction as the generator
   g = c_neighbour - c_self;
3. it draws its content from the soldered rule evaluated on the
   neighbours placed at those generators, with contents in label
   coordinates.

The emulator uses values and relative geometry only, so it is unsoldered.
It is also invariant under the 24 rotations on all 896 arising
configurations. Pulling back by sigma turns its content law into the
soldered law, or into the mirror rule when sigma is improper.

For this emulator the supplied role phase is shifted: vertices have three
odd coordinates, links two, plaquettes one and cubes zero, so the reference
vertex is (1,1,1). This is separate from the all-even-vertex readout above.
The ice vertex-record rule is covariant under all 48 cubic symmetries, so
the pullback is exact in all six frames. On the 3x3x3 window with the
vertex at the centre and corner growth, the soldered law is
(1/8)/C(3, 3-m) over the 20 ice configurations, with no defect. The
emulator reaches a frame with probability 2/9, and in each frame its
pulled-back law is identical to the soldered law.

## Theorem 4 — The price at a first formation

(a) *The corner's forward neighbours.* In corner growth the corner's
three forward neighbours are exactly the sites that form with the corner
as their only formed neighbour. This is checked on three orders. Their
configurations are related by proper rotations. Covariance gives identical marginals; the supplied fresh draws give
conditional independence given the corner's letter.

(b) *The bound.* They are pairwise distinct with probability 6 e_3(p).
Maclaurin's inequality e_3/C(m,3) <= (e_1/m)^3 bounds this by
(m-1)(m-2)/m^2, with equality exactly for the uniform law when m>=3. One elementary
proof maximizes e3 on the probability simplex: averaging a pair of unequal
positive coordinates increases their product term with the remaining mass
fixed. On a support of size r the maximum is C(r,3)/r^3, which increases
with r>=3, so the global maximum occurs on all m equal coordinates. With labels in
Z_4^K the three letters must lie on different axes, so the bound becomes
6 e_3(q) over the K axis masses, which is at most (K-1)(K-2)/K^2.

Checks:
- 205 rational laws, with equality at the uniform law;
- the identity P(distinct axes) = 6 q_1 q_2 q_3, by brute force over the
  216 first-shell assignments.

(c) *The bound is attained.* The corner rule gives P(frame) = 2/9 on the
boxes 2x2x2, 3x3x3, 6x3x2 and 4x4x4, and 3/8 at K = 4. Each failure is
two forward neighbours on one axis. The face-diagonal site between them
then sees two equal labels and is unrecorded. So "no unrecorded site"
and "frame" coincide.

(d) *Independence of the order.* Every corner-growth order gives each
site the same formed neighbours, so the finished law is the same for
all of them. Checked for three orders on 3x3x2.

(e) *Broadcast.* The six neighbours are i.i.d. A frame needs the six
signed generators, with opposite directions receiving opposite
generators. That has probability 48 prod(p) <= 48/6^6 = 1/972: exactly
1/972 at the uniform law, and 1280/3176523 for a skewed law.

## Theorem 5 — A designed order pays nothing

The order runs in three stages:
1. the corner, (1,0,0), (1,1,0), (0,1,0), (0,1,1), (0,0,1), (1,0,1),
   (1,1,1);
2. along each axis a ladder: a rail site offset by one, then the axis
   site beside it;
3. the rest in sweep order.

The designed rule gives the corner's lone forward neighbour the label
u_1, and that neighbour's lone child the label u_1 + u_2. Each closing
site takes the label its configuration fixes. Rails continue straight,
and an axis site takes its rail neighbour's label minus the offset.

The corner's forward neighbours see 1, 2 and 2 formed neighbours, so
they are not identically distributed. This finite computational claim concerns only the listed boxes. The record is the identity frame
with probability 1 on the boxes 2x2x2, 3x3x3, 5x3x2, 4x4x4 and 6x5x4.
The designed rule is invariant under the 24 rotations on all 114
arising configurations. The frame comes from the order, as in a sweep
(Lemma C). Mixing the order over rotations gives a covariant law with a
random frame.

## No-Go Discipline Gate

**N1 — Alternative challenges.**

- **Correlated first-shell draws (ATTEMPTED):** distinct-generator bounds assume conditionally independent draws; shared randomness evades that hypothesis.
- **Designed order (ATTEMPTED):** the five enumerated boxes register an identity frame with probability one.
- **Infinite sweep (ATTEMPTED):** the rigidity proof classifies complete stationary label fields, not a process initialized from an empty lattice.
- **Extra axes (ATTEMPTED):** the exact K=4 controls yield 3/8 rather than the K=3 value 2/9.
- **Different record content (ATTEMPTED):** the emulator is an abstract product alphabet; no one-qubit equivariant encoding is constructed.

**N2–N4 — Conditions and residuals.** Alphabet, fixed order, fresh draws,
record content and window are joint hypotheses, not independent physical
walls. The local proofs below support only their stated implications;
no historical campaign residual is closed by analogy. Standard finite
probability, counting and the named elementary inequalities are imports.

**N5 — Resolution.** The runner states its executed windows and enumeration
sizes. Source arguments support universal statements; finite tests do not
execute infinite formation, continuum spectra or a thermodynamic limit.

**N6–N8 — Remaining routes and cross-check.** Informative auxiliary records,
shared randomness, alternative orders and other alphabets remain possible.
The positive alternative constructions identify concrete ways outside each
negative hypothesis. No new axiom/primitive or general physical exclusion
is claimed. Related formation results retain their own declared domains.


## Falsifiers

- A complete stationary sweep record on Z_4^3 that is not an aligned
  frame falsifies Theorem 1.
- A frame record that violates the ice count or the role letters
  falsifies Theorem 2.
- A frame in which the emulator's pulled-back law differs from the
  soldered law falsifies Theorem 3.
- An unsoldered rule in corner growth whose frame probability exceeds
  (m-1)(m-2)/m^2 falsifies Theorem 4.
- One of the five tested boxes on which the designed order does not give the identity frame
  with certainty falsifies Theorem 5.

## Boundaries and non-claims

No rule, reading, alphabet or order law is adopted. Coordinate letters
are a declared candidate for the alphabet decision, not a derivation.
The sweep result does not fix which aligned frame or offset occurs.
Emulation reproduces the declared vertex rule; the directly carried ice
configuration is one fixed configuration. Neither comparison excludes all
other ways of generating a uniform ice measure. Independent clocks are not computed. The designed
order is one order per box, not a covariant law. Nothing here grades,
unlocks or audits any other claim.

## Imports

The Admissibility text is quoted. The landed notes and open PRs are
cited. Maclaurin's inequality and AM-GM are used as standard mathematics.
No audit grade, no new axiom, no new primitive, no new comparator and no
new framing is imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:**
  - the torus search enumerates every stationary label field rather than
    testing the claimed frames;
  - the corner price is compared with Maclaurin's bound, computed
    separately, and the i.i.d. identity is checked by brute force;
  - emulation compares the emulator's law with the soldered law, computed
    by a separate formation programme over lattice directions with
    supplied roles;
  - covariance is tested by rotating every arising configuration.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| mutation | substitution | result |
|---|---|---|
| first shell uses two of three axes | axis list cut | caught (5 FAILs) |
| axis continuation turns | u_i to u_{i+1} | caught (4 FAILs) |
| completion steps backwards (fold) | + to - | caught (6 FAILs) |
| torus back-neighbour along z forward | s - d_3 to s + d_3 | caught (1 FAIL) |
| ice readout occupies every link | odd-value test dropped | caught (2 FAILs) |
| role readout from the label mod 4 | parity to a mod-4 bit | caught (2 FAILs) |
| designed closing uses the offset axis | straight to offset | caught (1 FAIL) |
| designed rule loses the axis rule | rule removed | caught (1 FAIL) |
| emulator reads link directions reversed | g to -g | caught (1 FAIL) |
| reference link reads the record forwards | -d to d | caught (1 FAIL) |
| broadcast frame drops opposite pairing | pairing test dropped | caught (1 FAIL) |
| price bound constant weakened | (m-1)(m-2) to (m-2)^2 | caught (1 FAIL) |
| first shell reads the bond direction | direction-dependent choice | caught (6 FAILs) |
| frame lemma counts near-permutations | == 3 to >= 2 | caught (1 FAIL) |

  Fourteen of fourteen defect mutants are caught. An assertion-only
  mutant (dropping the constancy clause of the frame lemma) passed, since
  the data satisfy both clauses, and was replaced by a computational
  mutant. The z-forward mutant first crashed on an empty neighbour list;
  a guard now turns that case into a FAIL line.

- **Vacuity guard:**
  - the enumerations report their sizes (27, 27, 75 and 171 finished
    states; 602, 114 and 896 configurations; 19683 lemma triples);
  - laws are compared as whole distributions, not by size;
  - hole states are pruned only in the 7x7x7 run, whose kept mass is
    checked to be 2/9.
- **Budget:** 16 checks, stdout 2435 characters (ceiling 6000), about
  1.5 s (ceiling 900 s), exact Fractions.

## Verification

```bash
python3 scripts/registered_frames_coordinate_labels_sweep_rigidity_corner_price_and_soldered_emulation_2026_09_22.py
```

Expected summary line: `TOTAL: PASS=16 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/registered_frames_coordinate_labels_sweep_rigidity_corner_price_and_soldered_emulation_2026_09_22.txt`.

## Pre-landing correction record

Review in the current primary Codex session narrowed unsupported physical and
off-domain conclusions, made model premises explicit, and checked the source
arguments against the paired runner. Original author mutation counts above
are historical reports, not a separate review or a rerun by this session.
No subagents or audit verdicts were used.
