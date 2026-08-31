# Methodology dossier: checker pathologies found by the 2026-08 full-read

Synthesis of the densify full-read over the 1,691-PR open backlog (979 family
members in complete diff, 575 risky deep reads, 40-sample, 19 citers, 11
deviants, all chain terminals). Every class below was found by reading runner
code and recomputing, not by reading PR descriptions. PR numbers are the
exemplars actually verified; band roll-ups in `archive/families/` hold the
per-member detail. Purpose: these are the failure modes our checker discipline
must be built against; several defeated the strongest existing gates (N1–N8
packets, cross-model checkers, 65/65-green runners).

## A. Checkers that cannot fail

1. **Stubbed clauses.** #6612's `thm1-pos-implies-q4` body contains two
   literal `and True` placeholders exactly where every sibling asserts the
   two load-bearing conditions; its PASS line prints "positivity implies Q4"
   while its own computed `pos_implies_Q4=0` and its own Theorem 1 heading say
   the opposite.
2. **Structural always-pass gates.** Post-conditions equivalent by
   construction to the code under test: #7622's two `edge_status`
   post-conditions ("P is a signed permutation", "det P = Orient(src)·Orient")
   cannot fail given how P is built; #7701's band census found 43/44 members
   always-pass. The largest single consequence of the tautology classes.
3. **Type-mismatch tautologies.** #7049 filters `if lock in PVM_LETTERS`
   where locks are 3-tuples and PVM letters are the strings {+,−}: the empty
   result is guaranteed by construction, and 39 PASS checks certify it as an
   `UNDEFINED/UNDEFINED` theorem.
4. **Circular selection without negative controls.** #6404 claims the
   conjunction (wt1,opp2,adj2,vertex3,mixed3)=(1,0,1,1,1) uniquely selects
   f_L1 among the eight F_cut fillers — but #6410's taxonomy shows the filler
   set IS the 3-cube over (opp2,vertex3,mixed3) with wt1=adj2=1 fixed, so the
   "selection" restates the coordinates of the target; #6404's own N7
   steelman says so verbatim. Contrast the two honest controls the corpus
   does contain: #7096 (the only non-hold in its family — the discovery
   event) and #7142 (recomputes a sibling cell on the same process and shows
   the verdict is frame-dependent). A positive without a companion of this
   kind is unpriced.

## B. Checkers that measure the wrong thing

5. **Fake mutation gates.** #7495's `lex_largest_cyclic_orient` is a literal
   alias `return lex_smallest_cyclic_orient(...)`, which itself calls
   `cyclic_slots(..., largest=True)`: the two named "mutants" are the same
   function, the variable `lex_small` holds the lex-LARGEST value, and the
   check `mutation-lex-largest-cyclic-differs` passes on a lie. #7500/#7507
   carry phrase-inverted `-differ` gates of the same kind. A mutation gate
   that has never been shown to kill a planted defect is decoration.
6. **Phrase-inversion pairs.** #7272 and #7278 run the same computation on
   the same cell — an exact axis partition — and report it as fail/fail and
   hold/hold respectively, because one predicate scores "empty leftover" as
   FAIL and the other as HOLD. Verdict labels must be defined once per band,
   not per member.
7. **Prose-grep checks.** Checks that grep the note's sentences instead of
   comparing computed values (~1/3 of all checks in the observable-status
   band; #7357's runner pins ~6 sentences and tests no metadata at all).
8. **Or-precedence false greens.** #7297: a 17-term AND — including the
   headline verdicts — never evaluated, because a misparenthesized 3-term
   right disjunct is true on its own.
9. **Provenance defects at full green.** #7357 is a copy-note describing the
   WRONG experiment (opposite-seed metadata, seed paragraph, obligation table
   and N8 all contradict its own Theorem 2) and passes 65/65. Green checkers
   certify runners, not notes.

## C. Physics artifacts mistaken for results

10. **Ball-wall artifacts.** Finite-host boundaries read as physics: #6757's
    "k=6 face reverse returns" refuted on B16; #6822/#6840's PASS-asserted
    k=8 face claim; #7701's "distance-4 locality scale" is shell exhaustion
    (the holder set has 5 members, max Manhattan distance exactly 3). Two
    celebrated "restores" in the arrival band were wall relocations. Any
    claim within one step of the host boundary needs a larger-host control.
11. **Host-name collisions.** `B_3(0)` names both the Euclidean 123-site ball
    and the taxicab 63-site ball in different members (#6684/#6692 use the
    63-site host); cross-member comparisons silently change the host.
12. **Name-overloaded predicates.** "Connection" as the LOCK-field
    gauge-connection reading vs the psi-overlap connection (caveat row in the
    family table); #7163's Born-adjacent PVM with rho posited. One word, two
    predicates, and citations inherit whichever the reader assumed.
13. **Cut-convention fractures.** #7693 reads both endpoints at a common seed
    cut while its title says "t+1" like the rest of its band; the band's only
    "composition fails" is entirely that undeclared convention — under the
    band's own per-site cut the face bit HOLDs at both ticks.
14. **Dual growth processes under one name.** The frame-transport band runs
    two different formation processes under the single name used by its
    conclusions (the band's deepest integrity finding; see the band roll-up).

## D. The process-level root cause

15. **Forbidden-token gates prevented synthesis.** The campaign's hygiene
    gates ban authority vocabulary in member notes. Enforced by grep, the ban
    also made it impossible for a member to STATE a cross-member conclusion,
    so no member could write "these 44 cells are one experiment and its
    verdict is X" — the sharpest observed form: the vocabulary ban prevented
    a band from diagnosing its own tautology (three inequivalent
    constructions, none establishing curvature, publishable only as
    per-member fragments). Direct consequences: 107 of the 153 HOLD cells
    uncited by anything; ~200-PR bands with no summarizing note anywhere;
    the 14 roll-ups in `archive/families/` had to be authored from outside
    the corpus during this consolidation. Self-exempting variants (split
    literals, source excision, strip-then-grep) let some runners pass the
    gates they impose on others.
16. **Template monoculture hides deviants.** 979 members stamped from one
    template make metadata triage blind: the only way block 128 (#6844), the
    #7133 causal census, and the seven open deviants were found was reading
    every member. Self-reported modesty language ("no TOE movement") is
    inadmissible as triage evidence — several forcing negatives carry it.

## What held

The science survived because verdicts were recomputed, not trusted: the seven
disputed rows (7234/7235/7237/7247/7586/7637/7711) are published claims that
failed independent recomputation and are flagged in the ledger; #7586's title
verdict contradicts its own note, cache, and a fresh recompute. The full-read
found every class above AND the load-bearing positives the template hid
(#7096's discovery event, #7133's interval census, the locked-slope theorem,
the trivial-holonomy telescoping at 5,724 squares / 40,141 loops).

## Rules going forward

1. A checker computes and compares; it never greps prose for its verdict.
2. Every mutation gate demonstrates teeth: a planted defect it provably
   kills, behind an import firewall.
3. Every positive claim ships a negative control (#7142 is the model).
4. Verdict predicates and cut conventions are defined once per band, in the
   band's constructor note, and members import them.
5. Boundary-adjacent claims require a larger-host control run.
6. Vocabulary gates scope to authority claims in prose, never to computed
   content, and NEVER to band-level synthesis notes — which are first-class
   deliverables, required per ~50 members, not forbidden.
