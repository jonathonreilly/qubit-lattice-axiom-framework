# Review history

## 2026-10-10 author check, cycle 1

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The two parents
   are the minimal axioms and the 2026-09-22 order-blind note, both on
   origin/main at the base `0b208e91cfc`.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope rewrote
   `logs/runner-cache/one_orbit_bond_factor_dimension_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `d0361b815a1fc0417acb48aeb9ee40df8249d7e60954969a6068f4a04b04377b`.
3. Scope. Dimension 84 and affine dimension 78 on one 24-point orbit.
   Status line is `proposed_retained`. Surface status is `bounded-support`.
4. N-gate does not apply. The artifact is a positive finite count. The
   sentences that name what the count does not select are scope boundaries,
   not a claim that no route can select a factor.
5. Obligations are in the note: target sentence, lemmas proved here, and
   the missing order-blindness cut.
6. Mutations, each on a scratch copy, exited 1: group order 23, dimension
   83, ordered count 143, rank 5, stand-in forced to dimension 1, and
   reversal dropped. An independent generator closure gave 84 orbits,
   sizes 60 of 24 and 24 of 12, 144 ordered orbits, 6 direction-record
   orbits, row sums 24, and Gram determinant 140800000.
7. One primary runner. No packet helper, so no helper-registry edit.
8. Two markdown links, both to tracked notes. Manifest node_count 6870
   and edge_count 15420. The new node has out_degree 2. `citation_graph.json`
   was deleted.
9. Machine-status fields match the certificate. An imports paragraph names
   the enumerated rotations and states that no rate is imported.
10. No audit status, effective status, or ledger output is written.
11. The counts above were recomputed in this session.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the committed
    prose. The full audit pipeline was not run; it would write surfaces
    this branch must not commit.

## 2026-10-10 author check, cycle 2

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms and the 2026-09-22 order-blind note, both on
   origin/main at the base `0b208e91cfc`. The cycle-1 dimension count is
   not a lemma of this proof.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/three_cap_order_blind_lines_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `4cb0b46cdaa8663b9ffec8e65267122edf7d1cd33cd448a17c8bc86706808650`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=22 FAIL=0`.
3. Scope. Three cap lines, product mean 1 on all 729 weight patterns,
   and a mixture moment `25/24`. Status line `proposed_retained`. Surface
   status `bounded-support`. The rest of the order-blind set is open.
4. N-gate does not apply. The artifact is an existence witness for two
   further lines and one mixture moment. It does not claim that no other
   order-blind factor exists.
5. Obligations are in the note. The missing lemma is whether every
   soldered order-blind factor on this orbit is one of the three lines.
6. Mutations, each on a scratch copy, exited 1: cap size forced to 5,
   mixture moment forced to `26/24`, pure mean forced away from 1, and
   the right-hand record left unrotated. An independent generator closure
   agreed: supports `{4}`, means `{0}`, generator covariance failures 0,
   and the witness cross term gives moment `25/24`.
7. One primary runner. No packet helper.
8. Two markdown links, both to tracked notes on origin/main. The manifest
   refresh for the new node is part of this commit. `citation_graph.json`
   is deleted after the write.
9. Machine-status fields match this certificate. The imports paragraph
   names the parent converse and states that no rate is imported.
10. No audit status, effective status, or ledger output is written.
11. Counts recomputed in this session: group 24, orbit 24, cap size 4,
   729 patterns, moment `25/24`.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the note. The
    full audit pipeline was not run.

## 2026-10-10 author check, cycle 3

Author checks only. No review-loop PASS and no audit verdict.

1. Self-containment. Parents are the minimal axioms and the 2026-09-22
   note on origin/main. The cycle-2 lines are not a lemma here; the axis
   case is proved from mean 0 and disjoint caps.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. Envelope cache
   `logs/runner-cache/cap_span_order_blind_axes_2026_10_10.txt`, timeout
   180, status ok, sha256
   `49e3ab1cdac4cd3aa1abcdd981877dd4c735d4680f554bb53f4eca64935a9444`,
   matching `shasum -a 256`. `TOTAL: PASS=9 FAIL=0`.
3. Scope is the three-cap span only. Status line `proposed_retained`.
   Surface status `bounded-support`.
4. N-gate does not apply. The claim is which members of one span meet
   the product-mean identity. It does not say that no factor outside the
   span is order-blind.
5. The missing lemma is named in the note.
6. Mutations exited 1 for the moment forced to 1, the mixture moment
   forced to 1, and the off-diagonal correlation forced to 0. An
   independent generator closure reproduced correlation `1/24`, moment
   `13/12`, and moment `-3`.
7. One primary runner. No packet helper.
8. Two markdown links to notes on origin/main. The manifest refresh for
   the new node is part of this commit. `citation_graph.json` is deleted
   after the write.
9. Machine-status fields match the certificate.
10. No audit status or ledger output is written.
11. Counts recomputed this session: orbit 24, correlations `1/24` and
    `1/8`, moments `13/12` and `-3`.
12. Vocabulary lint is run on the note before commit. The full audit
    pipeline was not run.

## 2026-10-10 author check, cycle 4

Author checks only. No review-loop PASS and no audit verdict.

1. Self-containment. Parents are the minimal axioms and the 2026-09-22
   note on origin/main. The positive caps are the span being exited.
   Their product means are not a lemma here.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. Envelope cache
   `logs/runner-cache/opposite_cap_lines_outside_the_three_cap_span_2026_10_10.txt`,
   timeout 180, status ok, sha256
   `56872d459dcfab37995ea7836e1fe931e6b0b98759cb9a98bec8ce8c3a9484c6`,
   matching `shasum -a 256`. `TOTAL: PASS=23 FAIL=0`.
3. Scope is the three opposite caps on one 24-point orbit. Status line
   `proposed_retained`. Surface status `bounded-support`.
4. N-gate does not apply. The claim exhibits three lines outside the
   positive span. It does not say that no further factor exists.
5. The missing lemma is named in the note.
6. Mutations exited 1 for the cap size forced to 5, the product mean
   forced away from 1, the outside-span witness reversed, the right-hand
   record left unrotated, and the named product forced from `-1` to `1`.
   An independent closure under quarter-turns about `z` and about `x`
   gave 24 rotations, orbit 24, means `{0}`, supports `{4}`, no double
   activation, product mean 1, a witness on each level, and covariance
   failures 0.
7. One primary runner. No packet helper.
8. Two markdown links to notes on origin/main. The manifest refresh for
   the new node is part of this commit. `citation_graph.json` is deleted
   after the write.
9. Machine-status fields match the certificate.
10. No audit status or ledger output is written.
11. Counts recomputed this session: orbit 24, cap size 4, 729 patterns,
    named product `-1`.
12. Vocabulary lint is run on the note before commit. The full audit
    pipeline was not run.

## 2026-10-10 author check, cycle 5

Author checks only. No review-loop PASS and no audit verdict.

1. Self-containment. Parents are the minimal axioms and the 2026-09-22
   note on origin/main. The cap signs are the span being exited. Their
   product means are not a lemma here.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. Envelope cache
   `logs/runner-cache/transverse_cross_kernel_outside_six_caps_2026_10_10.txt`,
   timeout 180, status ok, sha256
   `47895b2b14e2493facc040f3dce8850b2026e1d70f72354e0695e82d048296ef`,
   matching `shasum -a 256`. `TOTAL: PASS=14 FAIL=0`.
3. Scope is one transverse-cross kernel on one 24-point orbit. Status
   line `proposed_retained`. Surface status `bounded-support`.
4. N-gate does not apply. The claim exhibits one kernel outside the six
   cap signs. It does not say that no further kernel exists.
5. The missing lemma is named in the note.
6. Mutations exited 1 for the witness value forced from `-1` to `1`,
   the value set forced to `{0, 1}`, the live count forced to 2, and
   the transporting matrix left uninverted. An independent closure
   under quarter-turns about `z` and about `x` gave 24 rotations, orbit
   24, four carriers, transport mismatches 0, bond-symmetry failures 0,
   one live direction, slice sums `{0}`, named value `-1`, and inner
   products 0 against all six levels.
7. One primary runner. No packet helper.
8. Two markdown links to notes on origin/main. The manifest refresh for
   the new node is part of this commit. `citation_graph.json` is deleted
   after the write.
9. Machine-status fields match the certificate.
10. No audit status or ledger output is written.
11. Counts recomputed this session: orbit 24, carriers 4, named value
    `-1`, values `{-1, 0, 1}`.
12. Vocabulary lint is run on the note before commit. The full audit
    pipeline was not run.

## 2026-10-10 author check, cycle 6

Author checks only. No review-loop PASS and no audit verdict.

1. Self-containment. Parents are the minimal axioms and the 2026-09-22
   note on origin/main. The 24-point dimension count is not a lemma.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. Envelope cache
   `logs/runner-cache/chiral_pair_bond_factor_dimension_2026_10_10.txt`,
   timeout 180, status ok, sha256
   `4bde0d6d07247e27cf41eddfa3d7ef628bdf6138413500d9eb0cf1f201027f90`,
   matching `shasum -a 256`. `TOTAL: PASS=15 FAIL=0`.
3. Scope is the linear bond space on the 48 signed permutations.
   Status line `proposed_retained`. Surface status `bounded-support`.
4. N-gate does not apply. The artifact is a positive finite count. It
   does not claim that no route can select a factor.
5. The missing lemma is whether order-blindness cuts the affine space.
6. Mutations exited 1 for the dimension forced to 311, the ordered
   count forced to 575, the rank forced to 11, and the stand-in forced
   to dimension 1. An independent closure under quarter-turns about
   `z` and about `x` gave 24 rotations, alphabet 48, two orbits of 24,
   dimension 312, sizes 264 of 24 and 48 of 12, 576 ordered orbits, 12
   rows, rank 12, and row sums 48.
7. One primary runner. No packet helper.
8. Two markdown links to notes on origin/main. The manifest refresh for
   the new node is part of this commit. `citation_graph.json` is deleted
   after the write.
9. Machine-status fields match the certificate.
10. No audit status or ledger output is written.
11. Counts recomputed this session: dimension 312, ordered 576, rank 12,
    affine dimension 300.
12. Vocabulary lint is run on the note before commit. The full audit
    pipeline was not run.

## 2026-10-10 author check, cycle 7

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms and the 2026-09-22 order-blind note, both on
   origin/main at the base `0b208e91cfc`. The earlier cap lines and the
   modulus-3 transverse cross are rebuilt in this runner as comparison
   vectors. They are not lemmas imported from this branch.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/lower_height_transverse_crosses_outside_modulus_three_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `5adff7cc8b73792672cdee785ad4b48f38768faeb1bf810102c2ca61da56a6c9`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=19 FAIL=0`.
3. Scope. Two kernels, rank 9 against the six cap lines and the
   height-3 cross, and mixture moment `23/24`. Status line
   `proposed_retained`. Surface status `bounded-support`. Kernels
   outside the three crosses stay open.
4. N-gate does not apply. The artifact exhibits two further kernels.
   It does not claim that no other order-blind kernel exists.
5. Obligations are in the note. The missing lemma is whether any
   soldered order-blind kernel remains outside the three crosses.
6. Mutations, each on a scratch copy, exited 1. Forcing every nonzero
   cross to `+1` gave `PASS=11 FAIL=8`. Leaving the transporting matrix
   uninverted gave `PASS=16 FAIL=3`. Dropping the height-2 term from the
   sum gave `PASS=18 FAIL=1` on the moment `23/24`. An independent
   closure under quarter-turns about `z` and about `x` gave 24
   rotations, orbit 24, four carriers, witnesses `-1`, ranks 7, 8, 8,
   and 9, and moment `23/24`.
7. One primary runner. No packet helper.
8. Two markdown links to notes on origin/main. The manifest refresh for
   the new node is part of this commit. `citation_graph.json` is deleted
   after the write.
9. Machine-status fields match the certificate.
10. No audit status or ledger output is written.
11. Counts recomputed this session: witnesses `-1`, rank 9, moment
    `23/24`, `PASS=19 FAIL=0`.
12. Vocabulary lint reported 0 violations on the note. The full audit
    pipeline was not run.

## 2026-10-10 author check, cycle 8

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms and the 2026-09-22 order-blind note, both on
   origin/main at the base `0b208e91cfc`. The cap lines and the matched
   crosses are rebuilt in this runner as comparison vectors. They are
   not lemmas imported from this branch.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/swapped_transverse_crosses_outside_matched_crosses_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `ff209cb71e685f164de3be5ccd4d5f6a8794b452a7bfc0da6e7982cb3f7cabf7`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=20 FAIL=0`.
3. Scope. Three swapped kernels, rank 12 against the six cap lines and
   the three matched crosses, a one-hot height-3 sum, and mixture
   moment `23/24`. Status line `proposed_retained`. Surface status
   `bounded-support`. Kernels outside the twelve stay open.
4. N-gate does not apply. The artifact exhibits three further kernels.
   It does not claim that no other order-blind kernel exists.
5. Obligations are in the note. The missing lemma is whether any
   soldered order-blind kernel remains outside the twelve.
6. Mutations, each on a scratch copy, exited 1. Forcing every nonzero
   swapped cross to `+1` gave `PASS=11 FAIL=9`. Leaving the transporting
   matrix uninverted gave `PASS=16 FAIL=4`. Dropping the height-2 term
   from the sum gave `PASS=19 FAIL=1` on the moment `23/24`. An
   independent closure under quarter-turns about `z` and about `x` gave
   24 rotations, four carriers, witnesses `-1`, ranks 9, 10, 10, 10,
   and 12, and moment `23/24`.
7. One primary runner. No packet helper.
8. Two markdown links to notes on origin/main. The manifest refresh for
   the new node is part of this commit. `citation_graph.json` is deleted
   after the write.
9. Machine-status fields match the certificate.
10. No audit status or ledger output is written.
11. Counts recomputed this session: witnesses `-1`, rank 12, moment
    `23/24`, `PASS=20 FAIL=0`.
12. Vocabulary lint reported 0 violations on the note. The full audit
    pipeline was not run.

## 2026-10-10 author check, cycle 9

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms and the 2026-09-22 order-blind note, both on
   origin/main at the base `0b208e91cfc`. Earlier crosses are rebuilt
   here as comparison vectors. They are not lemmas imported from this
   branch.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/one_hot_cap_pair_kernel_span_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `8af58ea2b813218152ee2f00d35d97c8545261ad2752d51c5f67446068130bee`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=22 FAIL=0`.
3. Scope. Six patterns, four bond orbits, slice rank 1, kernel
   dimension 3, total dimension 18, and mixture moment `23/24`. Status
   line `proposed_retained`. Surface status `bounded-support`. Kernels
   with two live directions stay open.
4. N-gate does not apply. The artifact classifies one named ansatz. It
   does not claim that no other order-blind kernel exists.
5. Obligations are in the note. The missing lemma is a kernel with two
   live directions.
6. Mutations, each on a scratch copy, exited 1. Forcing every nonzero
   sign to `+1` gave `PASS=14 FAIL=8`. Leaving the transporting matrix
   uninverted gave `PASS=18 FAIL=4`. Dropping the height-2 term from
   the sum gave `PASS=21 FAIL=1` on the moment `23/24`. An independent
   closure under quarter-turns about `z` and about `x` gave 24
   rotations, orbit 24, pattern dimensions `3, 3, 3, 3, 3, 3`, and the
   height-3 matched witness cross `-4`.
7. One primary runner. No packet helper.
8. Two markdown links to notes on origin/main. The manifest refresh for
   the new node is part of this commit. `citation_graph.json` is deleted
   after the write.
9. Machine-status fields match the certificate.
10. No audit status or ledger output is written.
11. Counts recomputed this session: dimension 3 on each pattern, total
    18, moment `23/24`, `PASS=22 FAIL=0`.
12. Vocabulary lint reported 0 violations on the note. The full audit
    pipeline was not run.

## 2026-10-10 author check, cycle 10

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms and the 2026-09-22 order-blind note, both on
   origin/main at the base `0b208e91cfc`. The cap line and the matched
   cross are rebuilt in this runner. They are not lemmas imported from
   this branch.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/opposite_cap_cross_mixture_two_live_directions_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `e5ce15a20b489c0bdd8ff7167ca61bd40ae86d6bf0d19d6797160d01468cd4b6`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=14 FAIL=0`.
3. Scope. One two-direction mixture with product mean 1, and the cap
   moment `7/6`. Status line `proposed_retained`. Surface status
   `bounded-support`. Kernels outside the cap-pair span stay open.
4. N-gate does not apply. The artifact exhibits one mixture. It does
   not claim that no kernel exists outside the cap-pair span.
5. Obligations are in the note. The missing lemma is a kernel outside
   that span.
6. Mutations, each on a scratch copy, exited 1. Forcing every nonzero
   sign to `+1` gave `PASS=12 FAIL=2`. Leaving the transporting matrix
   uninverted gave `PASS=13 FAIL=1`. Replacing the cross by the
   opposite cap gave `PASS=13 FAIL=1`. An independent closure under
   quarter-turns about `z` and about `x` gave 24 rotations, orbit 24,
   cap-product sum 4, and moment `7/6`.
7. One primary runner. No packet helper.
8. Two markdown links to notes on origin/main. The manifest refresh for
   the new node is part of this commit. `citation_graph.json` is deleted
   after the write.
9. Machine-status fields match the certificate.
10. No audit status or ledger output is written.
11. Counts recomputed this session: two opposite live directions,
    product mean 1, cap moment `7/6`, `PASS=14 FAIL=0`.
12. Vocabulary lint reported 0 violations on the note. The full audit
    pipeline was not run.

## 2026-10-10 author check, cycle 11

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms and the 2026-09-22 order-blind note, both on
   origin/main at the base `0b208e91cfc`. The cap line and the crosses
   are rebuilt in this runner. They are not lemmas imported from this
   branch.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/single_height_signature_order_blind_kernel_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `547f16c1b8e1afb2545309fd95514c77a23abd47e40f043cc39aa2febdee00b5`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=27 FAIL=0`.
3. Scope. Twenty-one height signatures, each of kernel dimension 3.
   The six opposite signatures are the eighteen cap-pair kernels. The
   other fifteen have only the zero order-blind kernel. Witness
   averages `-1/24` and `1/24`. Status line `proposed_retained`.
   Surface status `bounded-support`. A sum of two signatures stays open.
4. N-gate does not apply. The artifact classifies one named ansatz. It
   does not claim that no kernel on two signatures exists.
5. Obligations are in the note. The missing lemma is a kernel supported
   on two height signatures.
6. Mutations, each on a scratch copy, exited 1. Forcing every nonzero
   sign to `+1` gave `PASS=25 FAIL=2` on independence and spanning.
   Dropping reversal from the signature failed the count of 21 and the
   kernel dimension. Leaving the transporting matrix uninverted exited
   because the explicit kernel was not constant on a bond orbit. An
   independent closure under quarter-turns about `z` and about `x`
   gave 24 rotations and orbit 24, with the axis swap of the seed
   outside the orbit.
7. One primary runner. No packet helper.
8. Two markdown links, both to tracked notes on origin/main. Manifest
   node_count 6880 and edge_count 15440. The new node has out_degree 2.
   `citation_graph.json` was deleted.
9. Machine-status fields match this certificate. The imports paragraph
   names the parent converse and states that no rate is imported.
10. No audit status, effective status, or ledger output is written.
11. Counts recomputed in this session: 21 signatures, kernel dimension
    3, witness sums `-1` and `1`, `PASS=27 FAIL=0`.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the note. The
    full audit pipeline was not run.

## 2026-10-10 author check, cycle 12

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms and the 2026-09-22 order-blind note, both on
   origin/main at the base `0b208e91cfc`, and the cycle-11
   single-signature note on this branch. The 240 pair reductions are
   computed in this runner. The drop from one signature to the eighteen
   is cited, not rebuilt.
2. Cache. `AUDIT_TIMEOUT_SEC = 300`. The envelope wrote
   `logs/runner-cache/unequal_height_signature_with_one_partner_2026_10_10.txt`.
   Header `timeout_sec: 300`, `status: ok`, sha256
   `6a9db2b13b144c9a47d3aa923991704391cc68db35b79f88ce6cd7ea74ae0698`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=9 FAIL=0`.
   Elapsed 14.23 seconds.
3. Scope. Twelve unequal signatures, each beside the other twenty, so
   240 pairs. The six unequal monomials are pivots with no partner
   term, so the kernel drops to the partner. Status line
   `proposed_retained`. Surface status `bounded-support`. The control
   pair `(-3, -3)` beside `(3, -3)` is not forced. Two equal-height
   signatures stay open. The 84-dimensional bond space is not
   classified.
4. N-gate does not apply. The artifact classifies one named ansatz. It
   does not claim that no kernel on an equal-height pair exists.
5. Obligations are in the note. The missing lemma is an equal-height
   signature beside one opposite signature, or two equal-height
   signatures.
6. Mutations, each on a scratch copy, exited 1. Dropping reversal from
   the signature gave `PASS=6 FAIL=3` on the signature count, the
   opposite-equal-unequal split, and the 240-pair count. Swapping the
   two blocks, so the partner coordinates were tested in place of the
   unequal coordinates, gave `PASS=8 FAIL=1` on the 240-pair count.
   Replacing the control pair `(-3, -3)` by the unequal pair
   `(-3, -2)` beside `(3, -3)` gave `PASS=8 FAIL=1` on the control.
   An independent closure under quarter-turns about `z` and about `x`
   gave 24 rotations and orbit 24, with `(2, 1, 3)` outside the orbit.
7. One primary runner. No packet helper.
8. Three markdown links. Two point at tracked notes on origin/main.
   The third points at the cycle-11 single-signature note. Manifest
   node_count 6881 and edge_count 15443. The new node has out_degree 3
   and deps_hash `5859f1e27606`. Dependencies are `minimal_axioms`, the
   2026-09-22 note, and
   `single_height_signature_order_blind_kernel_bounded_theorem_note_2026-10-10`.
   `citation_graph.json` was deleted.
9. Machine-status fields match this certificate. The imports paragraph
   names the single-signature classification and the parent converse,
   and states that no rate is imported.
10. No audit status, effective status, or ledger output is written.
11. Counts recomputed in this session: 240 forced pairs, control not
    forced, `PASS=9 FAIL=0`.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the note. The
    full audit pipeline was not run.

## 2026-10-10 author check, cycle 13

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms and the 2026-09-22 order-blind note, both on
   origin/main at the base `0b208e91cfc`, and the cycle-11
   single-signature note on this branch. The joint-kernel counts, the
   normal forms, and the resultant are computed in this runner. The
   identification of an opposite signature with the eighteen is cited,
   not rebuilt.
2. Cache. `AUDIT_TIMEOUT_SEC = 300`. The envelope wrote
   `logs/runner-cache/equal_height_signature_with_one_partner_2026_10_10.txt`.
   Header `timeout_sec: 300`, `status: ok`, sha256
   `b8e2f1bd552dbde54131c5e8d31b1931b69643f912c228ca2e7622e9f2443b37`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=16 FAIL=0`.
   Elapsed 1.05 seconds.
3. Scope. All 210 signature pairs have joint slice kernel 6. Six
   same-modulus pairs, twelve different-modulus pairs, and three
   equal-height pairs match the stated normal forms. The three quadrics
   vanish only at the origin; the eliminant resultant is
   `113027603142816`. Status line `proposed_retained`. Surface status
   `bounded-support`. The triple `(-3, -3)`, `(-3, 3)`, `(3, -3)` has
   joint slice kernel 10, the maximum among 1330 triples, and stays
   open. The 84-dimensional bond space is not classified.
4. N-gate does not apply. The artifact classifies one named ansatz. It
   does not claim that no kernel on that triple exists.
5. Obligations are in the note. The missing lemma is the extra slice
   direction on `(-3, -3)`, `(-3, 3)`, and `(3, -3)`.
6. Mutations, each on a scratch copy, exited 1. Dropping reversal from
   the signature gave `PASS=9 FAIL=7` on the signature count, the
   joint-kernel counts, the opposite-equal-unequal split, and the three
   normal forms. Replacing the quadric coefficient `-4/3` by `-1` gave
   `PASS=13 FAIL=3` on the three normal forms. Demanding joint dimension
   7 instead of 6 gave `PASS=15 FAIL=1` on the 210-pair count. An
   independent closure under quarter-turns about `z` and about `x`
   gave 24 rotations and orbit 24, with `(2, 1, 3)` outside the orbit.
7. One primary runner. No packet helper.
8. Three markdown links. Two point at tracked notes on origin/main.
   The third points at the cycle-11 single-signature note. Manifest
   node_count 6882 and edge_count 15446. The new node has out_degree 3
   and deps_hash `5859f1e27606`. Dependencies are `minimal_axioms`, the
   2026-09-22 note, and
   `single_height_signature_order_blind_kernel_bounded_theorem_note_2026-10-10`.
   `citation_graph.json` was deleted.
9. Machine-status fields match this certificate. The imports paragraph
   names the single-signature classification and the parent converse,
   and states that no rate is imported.
10. No audit status, effective status, or ledger output is written.
11. Counts recomputed in this session: joint kernel 6 on 210 pairs,
    witness triple dimension 10, resultant `113027603142816`,
    `PASS=16 FAIL=0`.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the note. The
    full audit pipeline was not run.

## 2026-10-10 author check, cycle 14

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms and the 2026-09-22 order-blind note, both on
   origin/main at the base `0b208e91cfc`, and the cycle-11
   single-signature note on this branch. The complement line and the
   moment are computed in this runner. The support of the eighteen is
   cited, not rebuilt. The parent converse is not applied.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/modulus_three_triple_complement_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `b7b8531e204ae5da6e7f4acfc0ab2339713b7bb010af7c4706966520bec5d45e`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=13 FAIL=0`.
   Elapsed 0.38 seconds.
3. Scope. The joint slice kernel on `(-3, -3)`, `(-3, 3)`, and
   `(3, -3)` has dimension 10. The complement of the three signature
   kernels is one line, with values `-1`, `+1`, and `+1`. Every record
   has two live directions. The moment is `2` and the uniform average
   is `1/12`. Status line `proposed_retained`. Surface status
   `bounded-support`. A mixture with the signature kernels stays open.
   The 84-dimensional bond space is not classified.
4. N-gate does not apply. The artifact classifies one named ansatz. It
   does not claim that no mixture with the signature kernels is
   order-blind.
5. Obligations are in the note. The missing lemma is a mixture of the
   line with the three signature kernels.
6. Mutations, each on a scratch copy, exited 1. Dropping reversal from
   the signature failed the count of 21, the joint dimension, and the
   complement line, then raised `IndexError` before `TOTAL`. Requiring
   the witness moment to be `0` gave `PASS=12 FAIL=1` on the moment.
   Requiring joint dimension 9 gave `PASS=12 FAIL=1` on the dimension.
   An independent closure under quarter-turns about `z` and about `x`
   gave 24 rotations and orbit 24, with `(2, 1, 3)` outside the orbit.
7. One primary runner. No packet helper.
8. Three markdown links. Two point at tracked notes on origin/main.
   The third points at the cycle-11 single-signature note. Manifest
   node_count 6883 and edge_count 15449. The new node has out_degree 3
   and deps_hash `5859f1e27606`. Dependencies are `minimal_axioms`, the
   2026-09-22 note, and
   `single_height_signature_order_blind_kernel_bounded_theorem_note_2026-10-10`.
   `citation_graph.json` was deleted.
9. Machine-status fields match this certificate. The imports paragraph
   names the single-signature support of the eighteen and states that
   the parent converse is not applied and that no rate is imported.
10. No audit status, effective status, or ledger output is written.
11. Counts recomputed in this session: joint kernel 10, one complement
    line, moment `2`, average `1/12`, `PASS=13 FAIL=0`.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the note. The
    full audit pipeline was not run.

## 2026-10-10 author check, cycle 15

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms and the 2026-09-22 order-blind note, both on
   origin/main at the base `0b208e91cfc`, and the cycle-11
   single-signature note and the cycle-14 complement note on this
   branch. The pair moments and both singular loci are computed in this
   runner. The support of the eighteen and the complement coordinate
   vector are cited, not rebuilt. The parent converse is not applied.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/modulus_three_complement_mixture_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `0b0c9dde376872646f86a92cb6db413b8bc35e9326d4c1b33f1ff681d4ad16f7`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=12 FAIL=0`.
   Elapsed 0.77 seconds.
3. Scope. The ansatz is every rational linear mixture of the complement
   line with the three signature kernels, which is the joint slice
   kernel. Every cancelling mixture has complement coefficient zero and
   equal-height block zero, so it lies in the eighteen. No mixture in
   the ansatz both cancels the two-neighbour moments and leaves the
   eighteen. The cross moments between the opposite blocks are not
   solved. A fourth signature is outside the ansatz. The full bond
   space is not classified. Status line `proposed_retained`. Surface
   status `bounded-support`.
4. N-gate does not apply. The artifact prunes one named ansatz. It does
   not claim that no kernel on the full bond space leaves the eighteen.
5. Obligations are in the note. The missing lemma is an order-blindness
   cut on another alphabet.
6. Mutations, each on a scratch copy, exited 1. Requiring joint
   dimension 9 gave `PASS=11 FAIL=1` on the ansatz dimension. Replacing
   the plane factor `e0+e1` by `e0+e2` gave `PASS=10 FAIL=2` on the
   determinant identity and the plane kernel. Requiring the line sum to
   be 5 gave `PASS=11 FAIL=1` on the line `e0 = e1 = -e2`. An
   independent closure under signed permutation matrices of determinant
   1 gave 24 rotations and orbit 24, with `(2, 1, 3)` outside the orbit.
7. One primary runner. No packet helper.
8. Five markdown links. The runner link points at the primary runner.
   Two note links point at tracked notes on origin/main. Two point at
   the cycle-11 and cycle-14 notes on this branch. Manifest node_count
   6884 and edge_count 15453. The new node has out_degree 4 and
   deps_hash `9ac295ff0640`. Dependencies are `minimal_axioms`, the
   2026-09-22 note,
   `single_height_signature_order_blind_kernel_bounded_theorem_note_2026-10-10`,
   and
   `modulus_three_triple_complement_bounded_theorem_note_2026-10-10`.
   `citation_graph.json` was deleted.
9. Machine-status fields match this certificate. The imports paragraph
   names the single-signature support of the eighteen and the cycle-14
   coordinate vector, and states that the parent converse is not applied
   and that no rate is imported.
10. No audit status, effective status, or ledger output is written.
11. Counts recomputed in this session: the ansatz is the joint slice
    kernel, the complement coefficient and the equal-height block are
    both zero on every cancelling mixture, `PASS=12 FAIL=0`.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the note and
    the loop-pack prose. The full audit pipeline was not run.

## 2026-10-10 author check, cycle 16

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms and the 2026-09-22 order-blind note, both on
   origin/main at the base `0b208e91cfc`, and the cycle-6 chiral-pair
   bond note on this branch. Bond symmetry, soldered covariance, the
   far-end sums, and the moments are computed in this runner. Theorem 2
   supplies the moment obstruction and is not re-proved. Far-end sum 1
   is cited from the cycle-6 note. The dimension count is not repeated.
   The parent converse is not applied.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/chiral_pair_height_line_order_blind_cut_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `e1bf806ef5ff0f83f5d5de5579aa37e467476825877d3c3ec8cdcdff78ddbef0`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=12 FAIL=0`.
   Elapsed 4.05 seconds.
3. Scope. The ansatz is `phi_d(a, b) = 1 + c (a·d)(b·(-d))` on the 48
   signed permutations of `(1, 2, 3)`. Every far-end sum equals 48. At
   `c = 1/10` the factor is strictly positive and not constant, and the
   uniform moment on `±e_z` at `(1, 2, 3)` is `71/50`. Order-blindness
   cuts the normalised space. The order-blind subset is not classified.
   The parent's chiral-cap line is not re-derived. Status line
   `proposed_retained`. Surface status `bounded-support`.
4. N-gate does not apply. The artifact prunes one named line. It does
   not claim that no strictly positive order-blind factor exists.
5. Obligations are in the note. The missing lemma is an order-blind
   factor on this alphabet outside the exhibited chiral-cap line.
6. Mutations, each on a scratch copy, exited 1. Requiring the witness
   moment to be `71/49` gave `PASS=11 FAIL=1` on that moment. Requiring
   every far-end sum to be 47 gave `PASS=11 FAIL=1` on the far-end sum.
   Requiring the second moment to be `13/3` gave `PASS=11 FAIL=1` on
   that moment. An independent closure under signed permutation matrices
   of determinant 1 gave 24 rotations and orbit 24, with `(2, 1, 3)`
   outside the orbit.
7. One primary runner. No packet helper.
8. Four markdown links. The runner link points at the primary runner.
   Two note links point at tracked notes on origin/main. One points at
   the cycle-6 chiral-pair bond note on this branch. Manifest
   node_count 6885 and edge_count 15456. The new node has out_degree 3
   and deps_hash `41027eb0d307`. Dependencies are `minimal_axioms`, the
   2026-09-22 note, and
   `chiral_pair_bond_factor_dimension_bounded_theorem_note_2026-10-10`.
   `citation_graph.json` was deleted.
9. Machine-status fields match this certificate. The imports paragraph
   names Theorem 2 and far-end sum 1, and states that the parent
   converse is not applied and that no rate is imported.
10. No audit status, effective status, or ledger output is written.
11. Counts recomputed in this session: far-end sum 48, second moment
    `14/3`, witness moment `71/50`, `PASS=12 FAIL=0`.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the note and
    the loop-pack prose. The full audit pipeline was not run.

## 2026-10-10 author check, cycle 17

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms and the 2026-09-22 order-blind note, both on
   origin/main at the base `0b208e91cfc`, and the cycle-6 chiral-pair
   bond note on this branch. The transverse-sign product, the 729
   partner means, and the two-bond obstruction are computed in this
   runner. Theorem 2's converse is applied and not re-proved. Far-end
   sum 1 is cited from the cycle-6 note. The dimension count is not
   repeated.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/chiral_pair_transverse_sign_outside_cap_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `be8519058459b30aa18a06467281e04658b8be2560fbcc5776256f000c3561ee`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=10 FAIL=0`.
   Elapsed 3.77 seconds.
3. Scope. The ansatz is `phi_d(a, b) = 1 + (1/2) S_d(a) S_{-d}(b)` on
   the 48 signed permutations of `(1, 2, 3)`. All 729 partner patterns
   have product mean 1. The values are `1/2`, `1`, and `3/2`. Every
   far-end sum equals 48. The bonds on `e_z` from `(1, 2, 3)` and
   `(-2, 1, 3)` to `(1, 2, -3)` have transverse products `+1` and `-1`
   against chiral product `-1`. No scale of the chiral cap matches.
   The order-blind subset is not classified. Status line
   `proposed_retained`. Surface status `bounded-support`.
4. N-gate does not apply. The artifact exhibits one named line outside
   the chiral cap. It does not claim that no further order-blind factor
   exists.
5. Obligations are in the note. The missing lemma is a strictly positive
   order-blind factor outside both lines.
6. Mutations, each on a scratch copy, exited 1. Requiring every partner
   mean to be 2 gave `PASS=9 FAIL=1` on the 729 patterns. Requiring
   every far-end sum to be 47 gave `PASS=9 FAIL=1` on the far-end sum.
   Requiring the first transverse product to be 2 gave `PASS=9 FAIL=1`
   on the two-bond obstruction. An independent closure under signed
   permutation matrices of determinant 1 gave 24 rotations and orbit
   24, with `(2, 1, 3)` and `(1, 2, -3)` outside the orbit.
7. One primary runner. No packet helper.
8. Four markdown links. The runner link points at the primary runner.
   Two note links point at tracked notes on origin/main. One points at
   the cycle-6 chiral-pair bond note on this branch. Manifest
   node_count 6886 and edge_count 15459. The new node has out_degree 3
   and deps_hash `41027eb0d307`. Dependencies are `minimal_axioms`, the
   2026-09-22 note, and
   `chiral_pair_bond_factor_dimension_bounded_theorem_note_2026-10-10`.
   `citation_graph.json` was deleted.
9. Machine-status fields match this certificate. The imports paragraph
   names Theorem 2's converse and far-end sum 1, and states that no
   rate is imported.
10. No audit status, effective status, or ledger output is written.
11. Counts recomputed in this session: 729 partner patterns, values
    `1/2`, `1`, and `3/2`, far-end sum 48, transverse products `+1` and
    `-1`, `PASS=10 FAIL=0`.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the note and
    the loop-pack prose. The full audit pipeline was not run.

## 2026-10-10 author check, cycle 18

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms and the 2026-09-22 order-blind note, both on
   origin/main at the base `0b208e91cfc`, and the cycle-6 chiral-pair
   bond note on this branch. The sign-product cocycle, the 729 partner
   means, and the three-bond determinant are computed in this runner.
   Theorem 2's converse is applied and not re-proved. Far-end sum 1 is
   cited from the cycle-6 note. The dimension count is not repeated.
   The two exhibited caps are comparison tensors, not re-derived.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/chiral_pair_sign_product_outside_both_caps_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `a5fde6f7c382367792763f76f254cc3554a0e57ceec22242c050ece923571e43`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=11 FAIL=0`.
   Elapsed 2.45 seconds.
3. Scope. The ansatz is `phi_d(a, b) = 1 + (1/2) P_d(a) P_{-d}(b)` on
   the 48 signed permutations of `(1, 2, 3)`, with `P_d` the product of
   orbit chirality and the transverse sign on `a·d = 3`. All 729
   partner patterns have product mean 1. The values are `1/2`, `1`,
   and `3/2`. Every far-end sum equals 48. The bonds on `e_z` from
   `(1, 2, 3)`, `(2, -1, 3)`, and `(-2, -1, 3)` to `(-2, -1, -3)` have
   kernel rows `(1, 1, 1)`, `(1, -1, -1)`, and `(-1, 1, -1)`, and the
   determinant is `4`. A bond from `(1, 2, 3)` to itself has all three
   kernels equal to 0. The sign-product factor is not a linear
   combination of the two exhibited factors. The order-blind subset is
   not classified, and the 300-dimensional affine space is not
   classified. Status line `proposed_retained`. Surface status
   `bounded-support`.
4. N-gate does not apply. The artifact exhibits one named line outside
   the span of the two caps. It does not claim that no further
   order-blind factor exists.
5. Obligations are in the note. The missing lemma is a strictly positive
   order-blind factor outside the span of the three kernels.
6. Mutations, each on a scratch copy, exited 1. Requiring every partner
   mean to be 2 gave `PASS=10 FAIL=1` on the 729 patterns. Requiring
   every far-end sum to be 47 gave `PASS=10 FAIL=1` on the far-end sum.
   Requiring the determinant to be 0 gave `PASS=10 FAIL=1` on the
   three-bond obstruction. An independent closure under quarter-turns
   about `z` and about `x` gave 24 rotations and orbit 24, with
   `(2, 1, 3)` and `(1, 2, -3)` outside the orbit.
7. One primary runner. No packet helper.
8. Four markdown links. The runner link points at the primary runner.
   Two note links point at tracked notes on origin/main. One points at
   the cycle-6 chiral-pair bond note on this branch. Manifest
   node_count 6887 and edge_count 15462. The new node has out_degree 3
   and deps_hash `41027eb0d307`. Dependencies are `minimal_axioms`, the
   2026-09-22 note, and
   `chiral_pair_bond_factor_dimension_bounded_theorem_note_2026-10-10`.
   `citation_graph.json` was deleted.
9. Machine-status fields match this certificate. The imports paragraph
   names Theorem 2's converse and far-end sum 1, and states that no
   rate is imported.
10. No audit status, effective status, or ledger output is written.
11. Counts recomputed in this session: 729 partner patterns, values
    `1/2`, `1`, and `3/2`, far-end sum 48, determinant `4`,
    `PASS=11 FAIL=0`.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the note and
    the loop-pack prose. The full audit pipeline was not run.

## 2026-10-10 author check, cycle 19

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms and the 2026-09-22 order-blind note, both on
   origin/main at the base `0b208e91cfc`, and the cycle-6 chiral-pair
   bond note on this branch. The frame comparison, the left slices, and
   the five-bond determinant are computed in this runner. Theorem 2's
   converse is applied and not re-proved. Far-end sum 1 is cited from
   the cycle-6 note. The dimension count is not repeated. The three
   caps are comparison tensors, not re-derived.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/chiral_pair_transverse_crosses_outside_three_caps_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `b5df59b64d40efb61ab06e24d286dd62b78886f5d8b9194528da32ea6a709634`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=10 FAIL=0`.
   Elapsed 7.09 seconds.
3. Scope. The ansatz is the matched and swapped crosses on
   `a·d = 3` and `b·d = -3`, at coefficient `1/2`, on the 48 signed
   permutations of `(1, 2, 3)`. Each factor takes values `1/2`, `1`,
   and `3/2`. Each record meets at most one live direction and every
   left slice sums to 0. Every far-end sum equals 48. Five bonds from
   `(-2, -1, 3)` have determinant `8`. Neither cross is a linear
   combination of the three caps. The order-blind subset is not
   classified, and the 300-dimensional affine space is not classified.
   Status line `proposed_retained`. Surface status `bounded-support`.
4. N-gate does not apply. The artifact exhibits two named kernels
   outside the three caps. It does not claim that no further
   order-blind factor exists.
5. Obligations are in the note. The missing lemma is a strictly positive
   order-blind factor outside the span of the five kernels.
6. Mutations, each on a scratch copy, exited 1. Requiring the
   determinant to be 0 gave `PASS=9 FAIL=1` on the five-bond
   obstruction. Requiring every far-end sum to be 47 gave
   `PASS=9 FAIL=1` on the far-end sum. Requiring every left slice to
   sum to 1 gave `PASS=9 FAIL=1` on the slice check. An independent
   closure under quarter-turns about `z` and about `x` gave 24
   rotations and orbit 24, with `(2, 1, 3)` and `(1, 2, -3)` outside
   the orbit.
7. One primary runner. No packet helper.
8. Four markdown links. The runner link points at the primary runner.
   Two note links point at tracked notes on origin/main. One points at
   the cycle-6 chiral-pair bond note on this branch. Manifest
   node_count 6888 and edge_count 15465. The new node has out_degree 3
   and deps_hash `41027eb0d307`. Dependencies are `minimal_axioms`, the
   2026-09-22 note, and
   `chiral_pair_bond_factor_dimension_bounded_theorem_note_2026-10-10`.
   `citation_graph.json` was deleted.
9. Machine-status fields match this certificate. The imports paragraph
   names Theorem 2's converse and far-end sum 1, and states that no
   rate is imported.
10. No audit status, effective status, or ledger output is written.
11. Counts recomputed in this session: far-end sum 48, determinant `8`,
    values `1/2`, `1`, and `3/2`, `PASS=10 FAIL=0`.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the note and
    the loop-pack prose. The full audit pipeline was not run.

## 2026-10-10 author check, cycle 20

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms and the 2026-09-22 order-blind note, both on
   origin/main at the base `0b208e91cfc`, and the cycle-6 chiral-pair
   bond note on this branch. The frame comparison, the left slices, and
   the nine-bond determinant are computed in this runner. Theorem 2's
   converse is applied and not re-proved. Far-end sum 1 is cited from
   the cycle-6 note. The dimension count is not repeated. The five
   height-3 kernels are comparison tensors, not re-derived.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/chiral_pair_lower_height_crosses_outside_five_kernels_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `d9ebd5eb69a9152add1d32837a18ed22ebd058f936bf27d6b472058926aca4ee`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=10 FAIL=0`.
   Elapsed 13.39 seconds.
3. Scope. The ansatz is the matched and swapped crosses at absolute
   heights 1 and 2, at coefficient `1/2`, on the 48 signed permutations
   of `(1, 2, 3)`. Each factor takes values `1/2`, `1`, and `3/2`.
   Each record meets at most one live direction of that cross and every
   left slice sums to 0. Every far-end sum equals 48. Nine bonds on
   `e_z` have determinant `8`. None of the four crosses is a linear
   combination of the five height-3 kernels. The order-blind subset is
   not classified, and the 300-dimensional affine space is not
   classified. A sum across heights is outside the ansatz. Status line
   `proposed_retained`. Surface status `bounded-support`.
4. N-gate does not apply. The artifact exhibits four named kernels
   outside the five height-3 kernels. It does not claim that no further
   order-blind factor exists.
5. Obligations are in the note. The missing lemma is a strictly positive
   order-blind factor outside the span of the nine kernels.
6. Mutations, each on a scratch copy, exited 1. Requiring the
   determinant to be 0 gave `PASS=9 FAIL=1` on the nine-bond
   obstruction. Requiring every far-end sum to be 47 gave
   `PASS=9 FAIL=1` on the far-end sum. Requiring every left slice to
   sum to 1 gave `PASS=9 FAIL=1` on the slice check. An independent
   closure under quarter-turns about `z` and about `x` gave 24
   rotations and orbit 24, with `(2, 1, 3)` and `(1, 2, -3)` outside
   the orbit.
7. One primary runner. No packet helper.
8. Four markdown links. The runner link points at the primary runner.
   Two note links point at tracked notes on origin/main. One points at
   the cycle-6 chiral-pair bond note on this branch. Manifest
   node_count 6889 and edge_count 15468. The new node has out_degree 3
   and deps_hash `41027eb0d307`. Dependencies are `minimal_axioms`, the
   2026-09-22 note, and
   `chiral_pair_bond_factor_dimension_bounded_theorem_note_2026-10-10`.
   `citation_graph.json` was deleted.
9. Machine-status fields match this certificate. The imports paragraph
   names Theorem 2's converse and far-end sum 1, and states that no
   rate is imported.
10. No audit status, effective status, or ledger output is written.
11. Counts recomputed in this session: far-end sum 48, determinant `8`,
    values `1/2`, `1`, and `3/2`, `PASS=10 FAIL=0`.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the note and
    the loop-pack prose. The full audit pipeline was not run.

## 2026-10-10 author check, cycle 21

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms and the 2026-09-22 order-blind note, both on
   origin/main at the base `0b208e91cfc`, and the cycle-6 chiral-pair
   bond note on this branch. The covariance comparison, the left slices,
   and the two determinants are computed in this runner. Theorem 2's
   converse is applied and not re-proved. Far-end sum 1 is cited from
   the cycle-6 note. The dimension count is not repeated. The nine
   kernels are comparison tensors, not re-derived.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/chiral_pair_lower_height_caps_outside_nine_kernels_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `c39f7b5acdfbafde1e32ca63cd6964d0cabb1f0fbabbaf965382afd46b6a423e`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=10 FAIL=0`.
   Elapsed 11.11 seconds.
3. Scope. The ansatz is the chirality cap, the transverse-sign cap, and
   their sign product at absolute heights 1 and 2, at coefficient
   `1/2`, on the 48 signed permutations of `(1, 2, 3)`. Each factor
   takes values `1/2`, `1`, and `3/2`. Each cap sign has mean 0 and at
   most one live direction. Every far-end sum equals 48. Five bonds at
   each height have determinant `-16`. One bond at each height has all
   nine comparison kernels equal to 0. None of the six caps is a linear
   combination of the nine. The order-blind subset is not classified,
   and the 300-dimensional affine space is not classified. A
   mixed-height bond is outside the ansatz. Status line
   `proposed_retained`. Surface status `bounded-support`.
4. N-gate does not apply. The artifact exhibits six named kernels
   outside the nine. It does not claim that no further order-blind
   factor exists.
5. Obligations are in the note. The missing lemma is a strictly positive
   order-blind factor outside the span of the fifteen kernels.
6. Mutations, each on a scratch copy, exited 1. Requiring both
   determinants to be 0 gave `PASS=9 FAIL=1` on the ten-bond
   obstruction. Requiring every far-end sum to be 47 gave
   `PASS=9 FAIL=1` on the far-end sum. Requiring every left slice to
   sum to 1 gave `PASS=9 FAIL=1` on the slice check. An independent
   closure under quarter-turns about `z` and about `x` gave 24
   rotations and orbit 24, with `(2, 1, 3)` and `(1, 2, -3)` outside
   the orbit.
7. One primary runner. No packet helper.
8. Four markdown links. The runner link points at the primary runner.
   Two note links point at tracked notes on origin/main. One points at
   the cycle-6 chiral-pair bond note on this branch. Manifest
   node_count 6890 and edge_count 15471. The new node has out_degree 3
   and deps_hash `41027eb0d307`. Dependencies are `minimal_axioms`, the
   2026-09-22 note, and
   `chiral_pair_bond_factor_dimension_bounded_theorem_note_2026-10-10`.
   `citation_graph.json` was deleted.
9. Machine-status fields match this certificate. The imports paragraph
   names Theorem 2's converse and far-end sum 1, and states that no
   rate is imported.
10. No audit status, effective status, or ledger output is written.
11. Counts recomputed in this session: far-end sum 48, determinant
    `-16`, values `1/2`, `1`, and `3/2`, `PASS=10 FAIL=0`.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the note and
    the loop-pack prose. The full audit pipeline was not run.

## 2026-10-10 author check, cycle 22

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms and the 2026-09-22 order-blind note, both on
   origin/main at the base `0b208e91cfc`, and the cycle-6 chiral-pair
   bond note on this branch. The covariance comparison, the left slices,
   the two-bond separations, and the orbit ranks are computed in this
   runner. Theorem 2's converse is applied and not re-proved. Far-end
   sum 1 is cited from the cycle-6 note. The bond-space dimension count
   is not repeated. The fifteen kernels are comparison tensors, not
   re-derived.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/chiral_pair_parallel_transverse_dot_outside_fifteen_kernels_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `f3719dea23a6d108038d3f704532e2b1c2bfd1fa45cca0181b4d582880d6ff51`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=10 FAIL=0`.
   Elapsed 9.79 seconds.
3. Scope. The ansatz is the soldered bond-symmetric slice-zero kernels
   on one opposite-height pair. The exhibited kernel is the parallel
   transverse-dot sign at absolute heights 1, 2, and 3, at coefficient
   `1/2`, on the 48 signed permutations of `(1, 2, 3)`. Each factor
   takes values `1/2`, `1`, and `3/2`. Each record meets at most one
   live direction. Every far-end sum equals 48. Two bonds at each
   height agree on the fifteen comparison kernels and differ by 2.
   The opposite-height space is 10-dimensional, the five same-height
   kernels span 5, and this kernel raises the rank to 6. The
   5-dimensional complement is not based. The 300-dimensional affine
   space is not classified. A mixed-height bond is outside the ansatz.
   Status line `proposed_retained`. Surface status `bounded-support`.
4. N-gate does not apply. The artifact exhibits three named kernels
   outside the fifteen. It does not claim that no further order-blind
   factor exists.
5. Obligations are in the note. The missing lemma is an exact formula
   for a second vector in the 5-dimensional complement.
6. Mutations, each on a scratch copy, exited 1. Requiring the two-bond
   gap to be 0 gave `PASS=9 FAIL=1` on the three height pairs.
   Requiring every far-end sum to be 47 gave `PASS=9 FAIL=1` on the
   far-end sum. Requiring every left slice to sum to 1 gave
   `PASS=9 FAIL=1` on the slice check. An independent closure under
   quarter-turns about `z` and about `x` gave 24 rotations, all of
   determinant 1, and orbit 24, with `(2, 1, 3)` and `(1, 2, -3)`
   outside the orbit.
7. One primary runner. No packet helper.
8. Four markdown links. The runner link points at the primary runner.
   Two note links point at tracked notes on origin/main. One points at
   the cycle-6 chiral-pair bond note on this branch. Manifest
   node_count 6891 and edge_count 15474. The new node has out_degree 3
   and deps_hash `41027eb0d307`. Dependencies are `minimal_axioms`, the
   2026-09-22 note, and
   `chiral_pair_bond_factor_dimension_bounded_theorem_note_2026-10-10`.
   `citation_graph.json` was deleted.
9. Machine-status fields match this certificate. The imports paragraph
   names Theorem 2's converse and far-end sum 1, and states that no
   rate is imported.
10. No audit status, effective status, or ledger output is written.
11. Counts recomputed in this session: far-end sum 48, two-bond gap
    `-2`, opposite-height dimension 10, same-height rank 5, joint rank
    6, values `1/2`, `1`, and `3/2`, `PASS=10 FAIL=0`.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the note and
    the loop-pack prose. The full audit pipeline was not run.

## 2026-10-10 author check, cycle 23

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms and the 2026-09-22 order-blind note, both on
   origin/main at the base `0b208e91cfc`, and the cycle-6 chiral-pair
   bond note on this branch. The covariance comparison, the left slices,
   the two-bond separations, and the orbit ranks are computed in this
   runner. Theorem 2's converse is applied and not re-proved. Far-end
   sum 1 is cited from the cycle-6 note. The bond-space dimension count
   is not repeated. The eighteen kernels are comparison tensors, not
   re-derived.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/chiral_pair_matched_oblique_dot_outside_eighteen_kernels_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `6740b1d54423e1ce025e0c596d1ce24b4f84a1ba94b2adb60fae48c6d8f236ce`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=10 FAIL=0`.
   Elapsed 9.83 seconds.
3. Scope. The ansatz is the 10-dimensional soldered bond-symmetric
   slice-zero space on one opposite-height pair. The exhibited kernel
   is the matched oblique transverse-dot sign at absolute heights 1, 2,
   and 3, at coefficient `1/2`, on the 48 signed permutations of
   `(1, 2, 3)`. Each factor takes values `1/2`, `1`, and `3/2`. Support
   is disjoint from the parallel-dot kernel. Each record meets at most
   one live direction. Every far-end sum equals 48. Two bonds at each
   height agree on the fifteen comparison kernels, carry parallel dot
   0, and differ by 2. The five same-height kernels and the parallel
   dot have rank 6, and this kernel raises the rank to 7. The remaining
   3-dimensional complement is not based. The 300-dimensional affine
   space is not classified. A mixed-height bond is outside the ansatz.
   Status line `proposed_retained`. Surface status `bounded-support`.
4. N-gate does not apply. The artifact exhibits three named kernels
   outside the eighteen. It does not claim that no further order-blind
   factor exists.
5. Obligations are in the note. The missing lemma is an exact formula
   for a third vector in the remaining 3-dimensional complement.
6. Mutations, each on a scratch copy, exited 1. Requiring the two-bond
   gap to be 0 gave `PASS=9 FAIL=1` on the three height pairs.
   Requiring every far-end sum to be 47 gave `PASS=9 FAIL=1` on the
   far-end sum. Requiring every left slice to sum to 1 gave
   `PASS=9 FAIL=1` on the slice check. An independent closure under
   quarter-turns about `z` and about `x` gave 24 rotations, all of
   determinant 1, and orbit 24, with `(2, 1, 3)` and `(1, 2, -3)`
   outside the orbit.
7. One primary runner. No packet helper.
8. Four markdown links. The runner link points at the primary runner.
   Two note links point at tracked notes on origin/main. One points at
   the cycle-6 chiral-pair bond note on this branch. Manifest
   node_count 6892 and edge_count 15477. The new node has out_degree 3
   and deps_hash `41027eb0d307`. Dependencies are `minimal_axioms`, the
   2026-09-22 note, and
   `chiral_pair_bond_factor_dimension_bounded_theorem_note_2026-10-10`.
   `citation_graph.json` was deleted.
9. Machine-status fields match this certificate. The imports paragraph
   names Theorem 2's converse and far-end sum 1, and states that no
   rate is imported.
10. No audit status, effective status, or ledger output is written.
11. Counts recomputed in this session: far-end sum 48, two-bond gap
    `-2`, opposite-height dimension 10, rank 6 before this kernel, rank
    7 with it, values `1/2`, `1`, and `3/2`, `PASS=10 FAIL=0`.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the note and
    the loop-pack prose. The full audit pipeline was not run.

## 2026-10-10 author check, cycle 24

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms and the 2026-09-22 order-blind note, both on
   origin/main at the base `0b208e91cfc`, and the cycle-6 chiral-pair
   bond note on this branch. The covariance comparison, the left slices,
   the two-bond separations, and the orbit ranks are computed in this
   runner. Theorem 2's converse is applied and not re-proved. Far-end
   sum 1 is cited from the cycle-6 note. The bond-space dimension count
   is not repeated. The twenty-one kernels are comparison tensors, not
   re-derived.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/chiral_pair_swapped_transverse_dot_outside_twenty_one_kernels_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `740d1bea051a6063c92f4735c580cde1189f650dcab2eb5fe863233fc20e3a8e`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=10 FAIL=0`.
   Elapsed 10.29 seconds.
3. Scope. The ansatz is the 10-dimensional soldered bond-symmetric
   slice-zero space on one opposite-height pair. The exhibited kernel
   is the swapped transverse-dot sign at absolute heights 1, 2, and 3,
   at coefficient `1/2`, on the 48 signed permutations of `(1, 2, 3)`.
   Each factor takes values `1/2`, `1`, and `3/2`. Support is disjoint
   from the parallel-dot kernel and from the matched oblique dot. Each
   record meets at most one live direction. Every far-end sum equals 48.
   Two bonds at each height agree on the fifteen comparison kernels,
   carry parallel dot 0 and matched oblique dot 0, and differ by 2. The
   seven earlier kernels have rank 7, and this kernel raises the rank
   to 8. The remaining 2-dimensional complement is not based. The
   300-dimensional affine space is not classified. A mixed-height bond
   is outside the ansatz. Status line `proposed_retained`. Surface
   status `bounded-support`.
4. N-gate does not apply. The artifact exhibits three named kernels
   outside the twenty-one. It does not claim that no further order-blind
   factor exists.
5. Obligations are in the note. The missing lemma is an exact formula
   for a fourth vector in the remaining 2-dimensional complement.
6. Mutations, each on a scratch copy, exited 1. Requiring the two-bond
   gap to be 0 gave `PASS=9 FAIL=1` on the three height pairs.
   Requiring every far-end sum to be 47 gave `PASS=9 FAIL=1` on the
   far-end sum. Requiring every left slice to sum to 1 gave
   `PASS=9 FAIL=1` on the slice check. An independent closure under
   quarter-turns about `z` and about `x`, checked in this session, gave
   24 rotations, all of determinant 1, and orbit 24, with `(2, 1, 3)`
   and `(1, 2, -3)` outside the orbit.
7. One primary runner. No packet helper.
8. Four markdown links. The runner link points at the primary runner.
   Two note links point at tracked notes on origin/main. One points at
   the cycle-6 chiral-pair bond note on this branch. Manifest
   node_count 6893 and edge_count 15480. The new node has out_degree 3
   and deps_hash `41027eb0d307`. Dependencies are `minimal_axioms`, the
   2026-09-22 note, and
   `chiral_pair_bond_factor_dimension_bounded_theorem_note_2026-10-10`.
   `citation_graph.json` was deleted.
9. Machine-status fields match this certificate. The imports paragraph
   names Theorem 2's converse and far-end sum 1, and states that no
   rate is imported.
10. No audit status, effective status, or ledger output is written.
11. Counts recomputed in this session: far-end sum 48, two-bond gap
    `-2`, opposite-height dimension 10, rank 7 before this kernel, rank
    8 with it, values `1/2`, `1`, and `3/2`, `PASS=10 FAIL=0`.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the note and
    the loop-pack prose. The full audit pipeline was not run.

## 2026-10-10 author check, cycle 25

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms and the 2026-09-22 order-blind note, both on
   origin/main at the base `0b208e91cfc`, and the cycle-6 chiral-pair
   bond note on this branch. The covariance comparison, the left slices,
   the four-bond separations, and the orbit ranks are computed in this
   runner. Theorem 2's converse is applied and not re-proved. Far-end
   sum 1 is cited from the cycle-6 note. The bond-space dimension count
   is not repeated. The twenty-four kernels are comparison tensors, not
   re-derived.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/chiral_pair_orthogonal_swapped_cross_outside_twenty_four_kernels_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `2caac686431c4ec6d64bbd2bcdba73f0d8b101473f3f7603aa7aa2e66199e652`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=10 FAIL=0`.
   Elapsed 10.40 seconds.
3. Scope. The ansatz is the 10-dimensional soldered bond-symmetric
   slice-zero space on one opposite-height pair. The exhibited kernel
   is the orthogonal swapped cross at absolute heights 1, 2, and 3, at
   coefficient `1/2`, on the 48 signed permutations of `(1, 2, 3)`. Each
   factor takes values `1/2`, `1`, and `3/2`. Support is disjoint from
   the three dot kernels and is a proper subset of the swapped-cross
   support. Each record meets at most one live direction. Every far-end
   sum equals 48. Four bonds at each height, with weights `-1`, `-1`,
   `+1`, and `+1`, have alternating sum 0 on the twenty-four comparison
   kernels and alternating sum 2 on this kernel. The eight earlier
   kernels have rank 8, and this kernel raises the rank to 9. The
   remaining 1-dimensional complement is not based. The 300-dimensional
   affine space is not classified. A mixed-height bond is outside the
   ansatz. Status line `proposed_retained`. Surface status
   `bounded-support`.
4. N-gate does not apply. The artifact exhibits three named kernels
   outside the twenty-four. It does not claim that no further
   order-blind factor exists.
5. Obligations are in the note. The missing lemma is an exact formula
   for a fifth vector in the remaining 1-dimensional complement.
6. Mutations, each on a scratch copy, exited 1. Requiring the
   alternating sum to be 0 gave `PASS=9 FAIL=1` on the three height
   quadruples. Requiring every far-end sum to be 47 gave `PASS=9 FAIL=1`
   on the far-end sum. Requiring every left slice to sum to 1 gave
   `PASS=9 FAIL=1` on the slice check. An independent closure under
   quarter-turns about `z` and about `x`, checked in this session, gave
   24 rotations, all of determinant 1, and orbit 24, with `(2, 1, 3)`
   and `(1, 2, -3)` outside the orbit.
7. One primary runner. No packet helper.
8. Four markdown links. The runner link points at the primary runner.
   Two note links point at tracked notes on origin/main. One points at
   the cycle-6 chiral-pair bond note on this branch. Manifest
   node_count 6894 and edge_count 15483. The new node has out_degree 3
   and deps_hash `41027eb0d307`. Dependencies are `minimal_axioms`, the
   2026-09-22 note, and
   `chiral_pair_bond_factor_dimension_bounded_theorem_note_2026-10-10`.
   `citation_graph.json` was deleted.
9. Machine-status fields match this certificate. The imports paragraph
   names Theorem 2's converse and far-end sum 1, and states that no
   rate is imported.
10. No audit status, effective status, or ledger output is written.
11. Counts recomputed in this session: far-end sum 48, alternating sum
    `2`, opposite-height dimension 10, rank 8 before this kernel, rank
    9 with it, values `1/2`, `1`, and `3/2`, `PASS=10 FAIL=0`.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the note and
    the loop-pack prose. The full audit pipeline was not run.

## 2026-10-10 author check, cycle 26

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms and the 2026-09-22 order-blind note, both on
   origin/main at the base `0b208e91cfc`, and the cycle-6 chiral-pair
   bond note on this branch. The covariance comparison, the left slices,
   the four-bond separations, and the orbit ranks are computed in this
   runner. Theorem 2's converse is applied and not re-proved. Far-end
   sum 1 is cited from the cycle-6 note. The bond-space dimension count
   is not repeated. The twenty-seven kernels are comparison tensors, not
   re-derived.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/chiral_pair_scaled_cross_dot_bases_opposite_height_ansatz_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `073b218d91026ecbb36a2eaf28511d0338e1ed3e738e663c0eb883cd26640009`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=10 FAIL=0`.
   Elapsed 10.13 seconds.
3. Scope. The ansatz is the 10-dimensional soldered bond-symmetric
   slice-zero space on one opposite-height pair. The exhibited kernel
   is the scaled cross-dot kernel at absolute heights 1, 2, and 3, at
   coefficient `1/4`, on the 48 signed permutations of `(1, 2, 3)`. Each
   factor takes values `1/2`, `3/4`, `1`, `5/4`, and `3/2`. The product
   with the parallel-dot kernel is 0, and so is the product with the
   orthogonal swapped cross. Each record meets at most one live
   direction. Every far-end sum equals 48. Four bonds at each height,
   with weights `+1`, `+1`, `-1`, and `-1`, have alternating sum 0 on
   the twenty-seven comparison kernels and alternating sum 4 on this
   kernel. The nine earlier kernels have rank 9, and this kernel raises
   the rank to 10. Those ten kernels are a basis of the ansatz. The
   order-blind subset of the span is not classified. The 300-dimensional
   affine space is not classified. A mixed-height bond is outside the
   ansatz. Status line `proposed_retained`. Surface status
   `bounded-support`.
4. N-gate does not apply. The artifact names a basis of one
   opposite-height ansatz. It does not claim that no further order-blind
   factor exists outside that ansatz, and it does not classify mixtures.
5. Obligations are in the note. The missing lemma is which rational
   mixtures of the ten basis kernels have every neighbour-product mean
   equal to 1.
6. Mutations, each on a scratch copy, exited 1. Requiring the
   alternating sum to be 0 gave `PASS=9 FAIL=1` on the three height
   quadruples. Requiring every far-end sum to be 47 gave `PASS=9 FAIL=1`
   on the far-end sum. Requiring every left slice to sum to 1 gave
   `PASS=9 FAIL=1` on the slice check. An independent closure under
   quarter-turns about `z` and about `x`, checked in this session, gave
   24 rotations, all of determinant 1, and orbit 24, with `(2, 1, 3)`
   and `(1, 2, -3)` outside the orbit.
7. One primary runner. No packet helper.
8. Four markdown links. The runner link points at the primary runner.
   Two note links point at tracked notes on origin/main. One points at
   the cycle-6 chiral-pair bond note on this branch. Manifest
   node_count 6895 and edge_count 15486. The new node has out_degree 3
   and deps_hash `41027eb0d307`. Dependencies are `minimal_axioms`, the
   2026-09-22 note, and
   `chiral_pair_bond_factor_dimension_bounded_theorem_note_2026-10-10`.
   `citation_graph.json` was deleted.
9. Machine-status fields match this certificate. The imports paragraph
   names Theorem 2's converse and far-end sum 1, and states that no
   rate is imported.
10. No audit status, effective status, or ledger output is written.
11. Counts recomputed in this session: far-end sum 48, alternating sum
    `4`, opposite-height dimension 10, rank 9 before this kernel, rank
    10 with it, values `1/2`, `3/4`, `1`, `5/4`, and `3/2`,
    `PASS=10 FAIL=0`.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the note and
    the loop-pack prose. The full audit pipeline was not run.

## 2026-10-11 author check, cycle 27

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms and the 2026-09-22 order-blind note, both on
   origin/main at the base `0b208e91cfc`, the cycle-26 opposite-height
   basis note, and the cycle-6 chiral-pair bond note, both on this
   branch. The covariance comparison, the left slices, the live-direction
   bound, and the moment sums are computed in this runner. Theorem 2's
   converse is applied only to strictly positive mixtures and is not
   re-proved. The basis is cited from cycle 26. Far-end sum 1 is cited
   from the cycle-6 note. The bond-space dimension count is not repeated.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/chiral_pair_opposite_height_basis_mixtures_product_means_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `6c4eef871499c749381e175593faaec07a06378c9153420fbfac6ed19c604f39`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=8 FAIL=0`.
   Elapsed 2.30 seconds.
3. Scope. The ansatz is the rational span of the ten basis kernels on
   one opposite-height pair, at each absolute height separately. Every
   rational mixture has neighbour-product mean 1. The equal mixture at
   coefficient `1/32` takes values `29/32`, `15/16`, `31/32`, `1`,
   `33/32`, `17/16`, and `19/16`. The sample means are 1. Coefficient
   `2` on the chirality cap takes values `-1`, `1`, and `3`. The integer
   box `1` through `10` is a moment check, not the span. A sum across
   heights is outside the ansatz. The 300-dimensional affine space is
   not classified. Status line `proposed_retained`. Surface status
   `bounded-support`.
4. N-gate does not apply. The artifact classifies product means on one
   named span. It does not claim that no order-blind factor exists
   outside that span, and it does not classify a sum across heights.
5. Obligations are in the note. The missing lemma is which rational
   mixtures of two opposite-height bases, at two distinct absolute
   heights, have every neighbour-product mean equal to 1.
6. Mutations, each on a scratch copy, exited 1. Requiring every record
   to have no live direction gave `PASS=7 FAIL=1` on the slice check.
   Requiring the witness value set to be empty gave `PASS=7 FAIL=1` on
   the equal mixture. Adding 1 to the one-neighbour target gave
   `PASS=5 FAIL=3` on the three moment checks. An independent generator
   closure gave 24 rotations, all of determinant 1, and orbit 24, with
   `(2, 1, 3)` and `(1, 2, -3)` outside the orbit.
7. One primary runner. No packet helper.
8. Five markdown links. The runner link points at the primary runner.
   Two note links point at tracked notes on origin/main. Two point at
   the cycle-26 basis note and the cycle-6 chiral-pair bond note on
   this branch. Manifest node_count 6896 and edge_count 15490. The new
   node has out_degree 4 and deps_hash `bcc638123a3f`. Dependencies are
   `minimal_axioms`, the 2026-09-22 note, the cycle-26 basis note, and
   `chiral_pair_bond_factor_dimension_bounded_theorem_note_2026-10-10`.
   `citation_graph.json` was deleted.
9. Machine-status fields match this certificate. The imports paragraph
   names Theorem 2's converse, the basis, and far-end sum 1, and states
   that no rate is imported.
10. No audit status, effective status, or ledger output is written.
11. Counts recomputed in this session: `PASS=8 FAIL=0`, witness values
    `29/32`, `15/16`, `31/32`, `1`, `33/32`, `17/16`, and `19/16`, both
    sample moments 1, overlap bond chirality `1` and scaled `-2`, split
    bond chirality `-1` and scaled `0`, coefficient-2 values `-1`, `1`,
    and `3`.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the note and
    the loop-pack prose. The full audit pipeline was not run.

## 2026-10-11 author check, cycle 28

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms and the 2026-09-22 order-blind note, both on
   origin/main at the base `0b208e91cfc`, the cycle-27 opposite-height
   mixture note, and the cycle-6 chiral-pair bond note, both on this
   branch. The covariance comparison, the witness moment, and the
   two-direction counts are computed in this runner. Theorem 2's
   converse is applied only to the passing mixture and is not re-proved.
   The one-height identity is cited from cycle 27. Far-end sum 1 is
   cited from the cycle-6 note. The bond-space dimension count is not
   repeated.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/chiral_pair_cross_height_cap_mixture_product_means_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `fcc4a74d41dc883a39a53de49a75090aa8e2d9ce7c08be05b82d987ef472333a`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=9 FAIL=0`.
   Elapsed 37.99 seconds.
3. Scope. Two named mixtures of caps at heights 1 and 2, each at
   coefficient `1/2`, on the 48 signed permutations of `(1, 2, 3)`.
   Both take values `1/2`, `1`, and `3/2`. The two chirality caps have
   witness moment `97/96` and `1536` failing unordered pairs. The
   chirality cap plus the height-2 sign-product cap has every
   two-direction mean equal to 1. The coefficient span of two bases is
   not classified. The 300-dimensional affine space is not classified.
   Status line `proposed_retained`. Surface status `bounded-support`.
4. N-gate does not apply. The failing moment prunes one reading of
   cross-height caps. It does not claim that no cross-height mixture
   has product mean 1, and the passing mixture is exhibited.
5. Obligations are in the note. The missing lemma is which rational
   coefficient pairs on two opposite-height bases have every cross
   moment equal to 0.
6. Mutations, each on a scratch copy, exited 1. Requiring the witness
   moment to be 1 gave `PASS=8 FAIL=1` on the chirality-cap check.
   Requiring the passing bad-pair count to be `-1` gave `PASS=8 FAIL=1`
   on the sign-product check. Requiring every far-end sum to be 49 gave
   `PASS=8 FAIL=1` on the far-end sum. An independent generator closure
   in this session gave 24 rotations, all of determinant 1, and orbit
   24, with `(2, 1, 3)` and `(1, 2, -3)` outside the orbit.
7. One primary runner. No packet helper.
8. Five markdown links. The runner link points at the primary runner.
   Two note links point at tracked notes on origin/main. Two point at
   the cycle-27 mixture note and the cycle-6 chiral-pair bond note on
   this branch. Manifest node_count 6897 and edge_count 15494. The new
   node has out_degree 4 and deps_hash `47c28a336ede`. Dependencies are
   `minimal_axioms`, the 2026-09-22 note, the cycle-27 mixture note, and
   `chiral_pair_bond_factor_dimension_bounded_theorem_note_2026-10-10`.
   `citation_graph.json` was deleted.
9. Machine-status fields match this certificate. The imports paragraph
   names Theorem 2's converse, the one-height identity, and far-end sum
   1, and states that no rate is imported.
10. No audit status, effective status, or ledger output is written.
11. Counts recomputed in this session: `PASS=9 FAIL=0`, witness moment
    `97/96`, failing unordered pairs `1536`, passing bad pairs `0`,
    values `1/2`, `1`, and `3/2`, far-end sum 48. The two cross centres
    are `(-1, -2, -3)` and `(-1, -2, 3)`, and their cross sum is `1/2`.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the note and
    the loop-pack prose. The full audit pipeline was not run.

## 2026-10-11 author check, cycle 29

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms and the 2026-09-22 order-blind note, both on
   origin/main at the base `0b208e91cfc`, the cycle-27 opposite-height
   mixture note, and the cycle-26 scaled cross-dot basis note, both on
   this branch. The odd and even bases, the rank-25 product equations,
   and the witness moments are computed in this runner. Theorem 2's
   converse is applied only to the odd-even mixture at coefficient
   `1/2` and is not re-proved. The ten-kernel basis is cited from
   cycle 26. Bond symmetry on one height is cited from cycle 27. The
   dimension count of the soldered bond space is not repeated.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/chiral_pair_cross_height_parity_span_cross_moments_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `c594649216b0c60cc5c503203797e9d66a699374e89f203811e7fa2ed8b46b07`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=9 FAIL=0`.
   Elapsed 1.39 seconds.
3. Scope. The parity span of two opposite-height bases on the 48
   signed permutations of `(1, 2, 3)`. Odd dimension 4, even dimension
   3, intersection 0. Every cross moment vanishes exactly when the odd
   coefficient vectors are not both nonzero and the even coefficient
   vectors are not both nonzero. Witness moments `97/96` and `95/96`.
   The odd-even mixture at coefficient `1/2` takes values `1/2`, `1`,
   and `3/2`. The matched cross, the swapped transverse dot, and the
   scaled cross-dot kernel are outside the ansatz. The ten-kernel
   coefficient span is not classified. The full soldered bond space is
   not classified. Status line `proposed_retained`. Surface status
   `bounded-support`.
4. N-gate does not apply. The failing moments prune both-odd and
   both-even pairs inside the parity span. The check does not claim
   that no further kernel outside that span has every cross moment
   equal to 0, and a passing family is exhibited.
5. Obligations are in the note. The missing lemma is whether a nonzero
   coefficient on the matched cross, the swapped transverse dot, or the
   scaled cross-dot kernel can pair with a nonzero vector at the other
   height and still have every cross moment equal to 0.
6. Mutations, each on a scratch copy, exited 1. Requiring the product
   rank to be 24 gave `PASS=8 FAIL=1` on the rank-25 check. Requiring
   the chirality moment to be 1 gave `PASS=8 FAIL=1` on the cap-moment
   check. Requiring the heights 2 and 3 swapped moment to be 1 gave
   `PASS=8 FAIL=1` on that witness. An independent generator closure
   in this session gave 24 rotations, all of determinant 1, and orbit
   24, with `(2, 1, 3)` and `(1, 2, -3)` outside the orbit.
   `1 + (1/2)/48 = 97/96` and `1 - (1/2)/48 = 95/96`.
7. One primary runner. No packet helper.
8. Five markdown links. The runner link points at the primary runner.
   Two note links point at tracked notes on origin/main. Two point at
   the cycle-27 mixture note and the cycle-26 scaled cross-dot basis
   note on this branch. Manifest node_count 6898 and edge_count 15498.
   The new node has out_degree 4 and deps_hash `96b7746df63d`.
   Dependencies are `minimal_axioms`, the 2026-09-22 note, the cycle-27
   mixture note, and the cycle-26 scaled cross-dot basis note.
   `citation_graph.json` was deleted.
9. Machine-status fields match this certificate. The imports paragraph
   names Theorem 2's converse, the cycle-26 basis, and one-height bond
   symmetry, and states that no rate is imported.
10. No audit status, effective status, or ledger output is written.
11. Counts recomputed in this session: `PASS=9 FAIL=0`, odd dimension
    4, even dimension 3, product rank 25, moments `97/96` and `95/96`,
    mixture values `1/2`, `1`, and `3/2`.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the note and
    the loop-pack prose. The full audit pipeline was not run.

## 2026-10-11 author check, cycle 30

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms on origin/main at the base `0b208e91cfc`, the
   cycle-29 parity-span note, the cycle-26 scaled cross-dot basis note,
   and the cycle-27 opposite-height mixture note, the last three on this
   branch. The partner determinants, the self-cross sets, and the
   witness mean are computed in this runner. The order-blind converse
   is not applied. The parity split is cited from cycle 29. The
   ten-kernel basis is cited from cycle 26. Mean 1 on one height is
   cited from cycle 27. The dimension count of the soldered bond space
   is not repeated.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/chiral_pair_excluded_kernel_span_cross_moments_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `b059ad14f394816014cbcfb426098a5afc9e709e6496a557425f7fa588c339da`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=9 FAIL=0`.
   Elapsed 37.24 seconds.
3. Scope. The rational span of the matched cross, the swapped
   transverse dot, and the scaled cross-dot kernel, against any
   ten-kernel partner, on the 48 signed permutations of `(1, 2, 3)`.
   Every kernel cross sum vanishes exactly when one of the two vectors
   is 0. The witness centre values are `(0, 1)` and `(0, -1)`, the
   kernel cross sum is `-1`, and the direct alphabet mean is `47/48`.
   A vector with both a parity-span component and a nonzero excluded
   coefficient is outside the ansatz. The ten-kernel coefficient span
   is not classified. The full soldered bond space is not classified.
   Status line `proposed_retained`. Surface status `bounded-support`.
4. N-gate does not apply. The witness mean `47/48` prunes a nonzero
   excluded vector against a nonzero partner. The check does not claim
   that no vector outside the excluded span has every cross moment
   equal to 0, and the zero partner is exhibited.
5. Obligations are in the note. The missing lemma is whether a vector
   with both a parity-span component and a nonzero excluded coefficient
   can pair with a nonzero ten-kernel vector and still have every
   cross moment equal to 0.
6. Mutations, each on a scratch copy, exited 1. Requiring the witness
   mean to be 1 gave `PASS=8 FAIL=1` on the witness-bond check.
   Requiring the height `(1, 2)` scaled self-cross set to end at 3 gave
   `PASS=8 FAIL=1` on the scaled-set check. Requiring the zero partner
   to fail gave `PASS=8 FAIL=1` on the zero-vector check. An independent
   generator closure in this session gave 24 rotations, all of
   determinant 1, and orbit 24, with `(2, 1, 3)` and `(1, 2, -3)`
   outside the orbit.
7. One primary runner. No packet helper.
8. Five markdown links. The runner link points at the primary runner.
   One note link points at the minimal axioms on origin/main. Three
   point at the cycle-29 parity-span note, the cycle-26 scaled
   cross-dot basis note, and the cycle-27 mixture note on this branch.
   Manifest node_count 6899 and edge_count 15502. The new node has
   out_degree 4 and deps_hash `75525bf61ec1`. Dependencies are
   `minimal_axioms`, the cycle-29 parity-span note, the cycle-26
   scaled cross-dot basis note, and the cycle-27 mixture note.
   `citation_graph.json` was deleted.
9. Machine-status fields match this certificate. The imports paragraph
   names the parity split, the ten-kernel basis, and one-height mean 1,
   and states that the order-blind converse is not applied and that no
   rate is imported.
10. No audit status, effective status, or ledger output is written.
11. Counts recomputed in this session: `PASS=9 FAIL=0`, witness slices
    `(0, 1)` and `(0, -1)`, kernel cross sum `-1`, alphabet mean
    `47/48`.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the note and
    the loop-pack prose. The full audit pipeline was not run.

## 2026-10-11 author check, cycle 31

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms on origin/main at the base `0b208e91cfc`, the
   cycle-30 excluded-span note, the cycle-29 parity-span note, and the
   cycle-26 scaled cross-dot basis note, the last three on this branch.
   The partner determinants, the kernel bases, and the witness sums are
   computed in this runner. The order-blind converse is not applied.
   The parity kernels are cited from cycle 29. A vector with parity
   coefficient 0 is cited from cycle 30 and is not re-proved. The
   ten-kernel basis is cited from cycle 26. The dimension count of the
   soldered bond space is not repeated.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/chiral_pair_one_parity_one_excluded_cross_moments_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `26898f51f543671d77867b892a86088b08b5d30072d1149a6d7118f59593bb20`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=10 FAIL=0`.
   Elapsed 51.05 seconds.
3. Scope. Each plane spanned by one parity kernel and one excluded
   kernel, on the 48 signed permutations of `(1, 2, 3)`. Twenty planes
   have partner rank 10 whenever both coefficients are nonzero. The
   oblique-matched plane has partner rank 7 at ratios `1` and `-1`,
   with the named three-vector bases, and rank 10 at every other
   rational ratio. Oblique plus matched against itself has every cross
   sum equal to 0 at heights 1 and 2. The witness sums are `2`, `-4`,
   and `-1`. A sum of two parity kernels is outside the ansatz. The
   ten-kernel coefficient span is not classified. The full soldered
   bond space is not classified. Status line `proposed_retained`.
   Surface status `bounded-support`.
4. N-gate does not apply. The witness sum `2` prunes chirality plus
   matched against a nonzero partner. The check does not claim that no
   vector outside these 21 planes has a nonzero partner, and oblique
   plus matched against itself is exhibited.
5. Obligations are in the note. The missing lemma is whether a vector
   with two or more nonzero parity-kernel coefficients and a nonzero
   excluded coefficient can pair with a nonzero ten-kernel vector and
   still have every cross moment equal to 0.
6. Mutations, each on a scratch copy, exited 1. Requiring the chirality
   witness sum to be 0 gave `PASS=9 FAIL=1` on that witness. Requiring
   the first kernel vector to use matched coefficient 3 gave
   `PASS=9 FAIL=1` on the kernel-basis check. Requiring the special
   ratios to have rank 8 gave `PASS=9 FAIL=1` on the ratio check. An
   independent generator closure in this session gave 24 rotations, all
   of determinant 1, and orbit 24, with `(2, 1, 3)` and `(1, 2, -3)`
   outside the orbit.
7. One primary runner. No packet helper.
8. Five markdown links. The runner link points at the primary runner.
   One note link points at the minimal axioms on origin/main. Three
   point at the cycle-30 excluded-span note, the cycle-29 parity-span
   note, and the cycle-26 scaled cross-dot basis note on this branch.
   Manifest node_count 6900 and edge_count 15506. The new node has
   out_degree 4 and deps_hash `a8dbf1667136`. Dependencies are
   `minimal_axioms`, the cycle-30 excluded-span note, the cycle-29
   parity-span note, and the cycle-26 scaled cross-dot basis note.
   `citation_graph.json` was deleted.
9. Machine-status fields match this certificate. The imports paragraph
   names the parity kernels, the excluded span, and the ten-kernel
   basis, and states that the order-blind converse is not applied and
   that no rate is imported.
10. No audit status, effective status, or ledger output is written.
11. Counts recomputed in this session: `PASS=10 FAIL=0`, witness sums
    `2`, `-4`, and `-1`, centre values `(1, 1)` and `(-1, -1)`,
    `(0, 0)` and `(-2, 2)`, and `(0, 0)` and `(-1, 1)`.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the note and
    the loop-pack prose. The full audit pipeline was not run.

## 2026-10-11 author check, cycle 32

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms on origin/main at the base `0b208e91cfc`, the
   cycle-31 one-parity plane note, the cycle-29 parity-span note, and
   the cycle-26 scaled cross-dot basis note, the last three on this
   branch. The bond classes, the partner kernels, and the witness sums
   are computed in this runner. The order-blind converse is not applied.
   The parity kernels are cited from cycle 29. The ten-kernel basis is
   cited from cycle 26. The two triples are named in cycle 31 and their
   cross sums are recomputed here. The dimension count of the soldered
   bond space is not repeated.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/chiral_pair_two_parity_excluded_partner_kernel_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `255822f9312f67da6a6f0ce21414deed2431a9dfea1cfb110b5e560c7e768c70`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=10 FAIL=0`.
   Elapsed 0.84 seconds.
3. Scope. The two three-dimensional ratio spans on the 48 signed
   permutations of `(1, 2, 3)`. A nonzero vector in either span has two
   or more nonzero parity-kernel coefficients and a nonzero excluded
   coefficient exactly off that span's oblique-matched line. Every
   nonzero vector has partner rank 7. The partner kernel is the same
   span on height pairs `(1, 2)`, `(2, 1)`, `(2, 3)`, and `(3, 2)`, and
   the other span on `(1, 3)` and `(3, 1)`. The witness centre pairs are
   `(-2, 0)` and `(0, 2)`, with cross sum `0`, and `(0, 0)` and
   `(-2, 2)`, with cross sum `-4`. A vector outside both spans is
   outside the ansatz. The ten-kernel coefficient span is not
   classified. The full soldered bond space is not classified. Status
   line `proposed_retained`. Surface status `bounded-support`.
4. N-gate does not apply. The witness sum `-4` prunes the same-sign
   pair on heights 1 and 3. The check does not claim that no vector
   outside the two spans has a nonzero partner, and the height 1 and 2
   pair is exhibited.
5. Obligations are in the note. The missing lemma is whether the sum of
   the chirality cap, the transverse-sign cap, and the matched
   transverse cross can pair with a nonzero ten-kernel vector and still
   have every cross moment equal to 0.
6. Mutations, each on a scratch copy, exited 1. Requiring the height
   1 and 2 cross sum to be 1 gave `PASS=9 FAIL=1` on the centre-pair
   check. Requiring the scalar-matrix rank to be 4 gave `PASS=9 FAIL=1`
   on the scalar check. Requiring the eight directions to number 7 gave
   `PASS=8 FAIL=2` on the bond-class check and the partner-kernel check.
   An independent generator closure in this session gave 24 rotations,
   all of determinant 1, and orbit 24, with `(2, 1, 3)` and `(1, 2, -3)`
   outside the orbit.
7. One primary runner. No packet helper.
8. Five markdown links. The runner link points at the primary runner.
   One note link points at the minimal axioms on origin/main. Three
   point at the cycle-31 one-parity plane note, the cycle-29 parity-span
   note, and the cycle-26 scaled cross-dot basis note on this branch.
   Manifest node_count 6901 and edge_count 15510. The new node has
   out_degree 4 and deps_hash `e4033f935191`. Dependencies are
   `minimal_axioms`, the cycle-31 one-parity plane note, the cycle-29
   parity-span note, and the cycle-26 scaled cross-dot basis note.
   `citation_graph.json` was deleted.
9. Machine-status fields match this certificate. The imports paragraph
   names the parity kernels, the ten-kernel basis, and the two triples,
   and states that the order-blind converse is not applied and that no
   rate is imported.
10. No audit status, effective status, or ledger output is written.
11. Counts recomputed in this session: `PASS=10 FAIL=0`, centre pairs
    `(-2, 0)` and `(0, 2)` with cross sum `0`, and `(0, 0)` and
    `(-2, 2)` with cross sum `-4`.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the note and
    the loop-pack prose. The full audit pipeline was not run.

## 2026-10-11 author check, cycle 33

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms on origin/main at the base `0b208e91cfc`, the
   cycle-32 ratio-span note, the cycle-29 parity-span note, and the
   cycle-26 scaled cross-dot basis note, the last three on this branch.
   The partner rank and the witness sums are computed in this runner.
   The order-blind converse is not applied. The parity kernels are cited
   from cycle 29. The ten-kernel basis is cited from cycle 26. Both
   ratio spans are named in cycle 32, and this runner recomputes that
   every generator has chirality coefficient 0. The dimension count of
   the soldered bond space is not repeated.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/chiral_pair_chi_ts_matched_line_cross_moments_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `8d68570fe0a1b47f6a9fa1d4c7f5a08f732d9181513b83a4adb9dc01ffe599a1`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=7 FAIL=0`.
   Elapsed 0.53 seconds.
3. Scope. The equal-coefficient line on the 48 signed permutations of
   `(1, 2, 3)`. The sum of the chirality cap, the transverse-sign cap,
   and the matched transverse cross has two nonzero parity-kernel
   coefficients and one nonzero excluded coefficient, and chirality
   coefficient 1, so it lies outside both ratio spans. Every ordered
   height pair gives partner rank 10, and doubling the line doubles
   every partner row, so the only ten-kernel partner is 0. The witness
   centre pairs are `(2, 1)` and `(-2, -1)`, with cross sum `4`, and
   `(4, 1)` and `(-4, -1)`, with cross sum `8`. A different ratio of
   these three kernels is outside the ansatz. The ten-kernel coefficient
   span is not classified. The full soldered bond space is not
   classified. Status line `proposed_retained`. Surface status
   `bounded-support`.
4. N-gate does not apply. The artifact prunes one named line. It does
   not claim that no vector in the ten-kernel coefficient span has a
   nonzero partner.
5. Obligations are in the note. The missing lemma is whether the
   chirality cap plus twice the transverse-sign cap plus the matched
   transverse cross can pair with a nonzero ten-kernel vector and still
   have every cross moment equal to 0.
6. Mutations, each on a scratch copy, exited 1. Requiring the height
   1 and 2 cross sum to be 1 gave `PASS=6 FAIL=1` on the centre-pair
   check. Requiring the partner rank to differ from 9 gave `PASS=6
   FAIL=1` on the rank check. Requiring the doubled cross sum to be 4
   gave `PASS=6 FAIL=1` on the doubled-line check. An independent
   closure under signed monomial matrices of determinant 1 gave 24
   rotations, all of determinant 1, and orbit 24, with `(2, 1, 3)` and
   `(1, 2, -3)` outside the orbit.
7. One primary runner. No packet helper.
8. Five markdown links. The runner link points at the primary runner.
   One note link points at the minimal axioms on origin/main. Three
   point at the cycle-32 ratio-span note, the cycle-29 parity-span
   note, and the cycle-26 scaled cross-dot basis note on this branch.
   Manifest node_count 6902 and edge_count 15514. The new node has
   out_degree 4 and deps_hash `889f73d5d53c`. Dependencies are
   `minimal_axioms`, the cycle-32 ratio-span note, the cycle-29
   parity-span note, and the cycle-26 scaled cross-dot basis note.
   `citation_graph.json` was deleted.
9. Machine-status fields match this certificate. The imports paragraph
   names the parity kernels, the ten-kernel basis, and the two triples,
   and states that the order-blind converse is not applied and that no
   rate is imported.
10. No audit status, effective status, or ledger output is written.
11. Counts recomputed in this session: `PASS=7 FAIL=0`, centre pairs
    `(2, 1)` and `(-2, -1)` with cross sum `4`, and `(4, 1)` and
    `(-4, -1)` with cross sum `8`.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the note and
    the loop-pack prose. The full audit pipeline was not run.

## 2026-10-11 author check, cycle 34

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms on origin/main at the base `0b208e91cfc`, the
   cycle-33 equal-coefficient note, the cycle-32 ratio-span note, and
   the cycle-29 parity-span note, the last three on this branch. The
   partner rank and the witness sums are computed in this runner. The
   order-blind converse is not applied. The parity kernels are cited
   from cycle 29. The equal-coefficient line is cited from cycle 33.
   Both ratio spans are named in cycle 32, and this runner recomputes
   that every generator has chirality coefficient 0. The dimension
   count of the soldered bond space is not repeated.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/chiral_pair_chi_twice_ts_matched_line_cross_moments_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `67b8e27cc53677d63f61488100ee2126cea2cff882c42bff3b57e15e719394b7`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=7 FAIL=0`.
   Elapsed 0.60 seconds.
3. Scope. The doubled transverse-sign line on the 48 signed
   permutations of `(1, 2, 3)`. The chirality cap plus twice the
   transverse-sign cap plus the matched transverse cross has two
   nonzero parity-kernel coefficients and one nonzero excluded
   coefficient. The transverse-sign coefficient is 2 and the chirality
   coefficient is 1, so the sum is outside the equal-coefficient line
   and outside both ratio spans. Every ordered height pair gives
   partner rank 10, and doubling the line doubles every partner row, so
   the only ten-kernel partner is 0. The witness centre pairs are
   `(3, 1)` and `(-3, -1)`, with cross sum `6`, and `(6, 1)` and
   `(-6, -1)`, with cross sum `12`. A different ratio of these three
   kernels is outside the ansatz. The ten-kernel coefficient span is
   not classified. The full soldered bond space is not classified.
   Status line `proposed_retained`. Surface status `bounded-support`.
4. N-gate does not apply. The artifact prunes one named line. It does
   not claim that no vector in the ten-kernel coefficient span has a
   nonzero partner.
5. Obligations are in the note. The missing lemma is whether the
   chirality cap plus the transverse-sign cap plus twice the matched
   transverse cross can pair with a nonzero ten-kernel vector and still
   have every cross moment equal to 0.
6. Mutations, each on a scratch copy, exited 1. Requiring the height
   1 and 2 cross sum to be 1 gave `PASS=6 FAIL=1` on the centre-pair
   check. Requiring the partner rank to differ from 9 gave `PASS=6
   FAIL=1` on the rank check. Requiring the doubled cross sum to be 6
   gave `PASS=6 FAIL=1` on the doubled-line check. An independent
   closure under signed monomial matrices of determinant 1 gave 24
   rotations, all of determinant 1, and orbit 24, with `(2, 1, 3)` and
   `(1, 2, -3)` outside the orbit.
7. One primary runner. No packet helper.
8. Five markdown links. The runner link points at the primary runner.
   One note link points at the minimal axioms on origin/main. Three
   point at the cycle-33 equal-coefficient note, the cycle-32
   ratio-span note, and the cycle-29 parity-span note on this branch.
   Manifest node_count 6903 and edge_count 15518. The new node has
   out_degree 4 and deps_hash `de56e0d12f1b`. Dependencies are
   `minimal_axioms`, the cycle-33 equal-coefficient note, the cycle-32
   ratio-span note, and the cycle-29 parity-span note.
   `citation_graph.json` was deleted.
9. Machine-status fields match this certificate. The imports paragraph
   names the parity kernels, the equal-coefficient line, and the two
   triples, and states that the order-blind converse is not applied and
   that no rate is imported.
10. No audit status, effective status, or ledger output is written.
11. Counts recomputed in this session: `PASS=7 FAIL=0`, centre pairs
    `(3, 1)` and `(-3, -1)` with cross sum `6`, and `(6, 1)` and
    `(-6, -1)` with cross sum `12`.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the note and
    the loop-pack prose. The full audit pipeline was not run.

## 2026-10-11 author check, cycle 35

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms on origin/main at the base `0b208e91cfc`, the
   cycle-34 doubled transverse-sign note, the cycle-33 equal-coefficient
   note, and the cycle-32 ratio-span note, all three notes on this
   branch. The partner rank and the witness sums are computed in this
   runner. The order-blind converse is not applied. The parity kernels
   are cited from cycles 33 and 34. Both ratio spans are named in cycle
   32, and this runner recomputes that every generator has chirality
   coefficient 0. The dimension count of the soldered bond space is not
   repeated.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/chiral_pair_chi_ts_twice_matched_line_cross_moments_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `3cb5566e2a8aaeff1fac352400d378ad3496867a43a78391be09ee562e7556c7`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=8 FAIL=0`.
   Elapsed 0.56 seconds.
3. Scope. The doubled matched line on the 48 signed permutations of
   `(1, 2, 3)`. The chirality cap plus the transverse-sign cap plus
   twice the matched transverse cross has two nonzero parity-kernel
   coefficients and one nonzero excluded coefficient. The matched
   coefficient is 2 and the chirality coefficient is 1, so the sum is
   outside the equal-coefficient line. The transverse-sign coefficient
   is 1, so the sum is outside the doubled transverse-sign line. It is
   also outside both ratio spans. Every ordered height pair gives
   partner rank 10, and doubling the line doubles every partner row, so
   the only ten-kernel partner is 0. The witness centre pairs are
   `(0, 1)` and `(-2, -1)`, with cross sum `2`, and `(0, 1)` and
   `(-4, -1)`, with cross sum `4`. The first left contributes 0. The
   equal-coefficient vector on the same bond has centre pairs `(0, 1)`
   and `(-1, -1)` and cross sum `1`. A different ratio of these three
   kernels is outside the ansatz. The ten-kernel coefficient span is
   not classified. The full soldered bond space is not classified.
   Status line `proposed_retained`. Surface status `bounded-support`.
4. N-gate does not apply. The artifact prunes one named line. It does
   not claim that no vector in the ten-kernel coefficient span has a
   nonzero partner.
5. Obligations are in the note. The missing lemma is whether the
   chirality cap plus twice the transverse-sign cap plus twice the
   matched transverse cross can pair with a nonzero ten-kernel vector
   and still have every cross moment equal to 0.
6. Mutations, each on a scratch copy, exited 1. Requiring the height
   1 and 2 cross sum to be 1 gave `PASS=7 FAIL=1` on the centre-pair
   check. Requiring the partner rank to differ from 9 gave `PASS=7
   FAIL=1` on the rank check. Requiring the doubled cross sum to be 1
   gave `PASS=7 FAIL=1` on the doubled-line check. An independent
   closure under signed monomial matrices of determinant 1 gave 24
   rotations, all of determinant 1, and orbit 24, with `(2, 1, 3)` and
   `(1, 2, -3)` outside the orbit.
7. One primary runner. No packet helper.
8. Five markdown links. The runner link points at the primary runner.
   One note link points at the minimal axioms on origin/main. Three
   point at the cycle-34 doubled transverse-sign note, the cycle-33
   equal-coefficient note, and the cycle-32 ratio-span note on this
   branch. Manifest node_count 6904 and edge_count 15522. The new node
   has out_degree 4 and deps_hash `b39d8220dbf6`. Dependencies are
   `minimal_axioms`, the cycle-34 doubled transverse-sign note, the
   cycle-33 equal-coefficient note, and the cycle-32 ratio-span note.
   `citation_graph.json` was deleted.
9. Machine-status fields match this certificate. The imports paragraph
   names the two earlier lines, the parity kernels, and the two triples,
   and states that the order-blind converse is not applied and that no
   rate is imported.
10. No audit status, effective status, or ledger output is written.
11. Counts recomputed in this session: `PASS=8 FAIL=0`, centre pairs
    `(0, 1)` and `(-2, -1)` with cross sum `2`, `(0, 1)` and `(-4, -1)`
    with cross sum `4`, and `(0, 1)` and `(-1, -1)` with cross sum `1`.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the note and
    the loop-pack prose. The full audit pipeline was not run.

## 2026-10-11 author check, cycle 36

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms on origin/main at the base `0b208e91cfc`, the
   cycle-35 doubled matched note, the cycle-34 doubled transverse-sign
   note, and the cycle-32 ratio-span note, all three notes on this
   branch. The partner rank and the witness sums are computed in this
   runner. The order-blind converse is not applied. The parity kernels
   are cited from cycle 34. Both ratio spans are named in cycle 32, and
   this runner recomputes that every generator has chirality coefficient
   0. The dimension count of the soldered bond space is not repeated.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/chiral_pair_chi_twice_ts_twice_matched_line_cross_moments_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `5b4b65f1312bfe2d3a6c9dfa461b56cde7a04f596496085766f89bec9da108c1`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=8 FAIL=0`.
   Elapsed 0.56 seconds.
3. Scope. The line through the chirality cap, twice the transverse-sign
   cap, and twice the matched transverse cross, on the 48 signed
   permutations of `(1, 2, 3)`. The sum has two nonzero parity-kernel
   coefficients and one nonzero excluded coefficient. The matched
   coefficient is 2 and the chirality coefficient is 1, so the sum is
   outside the equal-coefficient line and outside the doubled
   transverse-sign line. The transverse-sign coefficient is 2, so the
   sum is outside the doubled matched line. It is also outside both
   ratio spans. Every ordered height pair gives partner rank 10, and
   doubling the line doubles every partner row, so the only ten-kernel
   partner is 0. The witness centre pairs are `(1, 1)` and `(-3, -1)`,
   with cross sum `4`, and `(2, 1)` and `(-6, -1)`, with cross sum `8`.
   The first left contributes 1 and the second left contributes 3. The
   doubled transverse-sign vector on the same bond has centre pairs
   `(1, 1)` and `(-2, -1)` and cross sum `3`. A different ratio of these
   three kernels is outside the ansatz. The ten-kernel coefficient span
   is not classified. The full soldered bond space is not classified.
   Status line `proposed_retained`. Surface status `bounded-support`.
4. N-gate does not apply. The artifact prunes one named line. It does
   not claim that no vector in the ten-kernel coefficient span has a
   nonzero partner.
5. Obligations are in the note. The missing lemma is whether twice the
   chirality cap plus the transverse-sign cap plus the matched
   transverse cross can pair with a nonzero ten-kernel vector and still
   have every cross moment equal to 0.
6. Mutations, each on a scratch copy, exited 1. Requiring the height
   1 and 2 cross sum to be 1 gave `PASS=7 FAIL=1` on the centre-pair
   check. Requiring the partner rank to differ from 9 gave `PASS=7
   FAIL=1` on the rank check. Requiring the doubled cross sum to be 1
   gave `PASS=7 FAIL=1` on the doubled-line check. An independent
   closure under signed monomial matrices of determinant 1 gave 24
   rotations, all of determinant 1, and orbit 24, with `(2, 1, 3)` and
   `(1, 2, -3)` outside the orbit.
7. One primary runner. No packet helper.
8. Five markdown links. The runner link points at the primary runner.
   One note link points at the minimal axioms on origin/main. Three
   point at the cycle-35 doubled matched note, the cycle-34 doubled
   transverse-sign note, and the cycle-32 ratio-span note on this
   branch. Manifest node_count 6905 and edge_count 15526. The new node
   has out_degree 4 and deps_hash `6e9e88396a5e`. Dependencies are
   `minimal_axioms`, the cycle-35 doubled matched note, the cycle-34
   doubled transverse-sign note, and the cycle-32 ratio-span note.
   `citation_graph.json` was deleted.
9. Machine-status fields match this certificate. The imports paragraph
   names the doubled matched line, the doubled transverse-sign line, the
   parity kernels, and the two triples, and states that the order-blind
   converse is not applied and that no rate is imported.
10. No audit status, effective status, or ledger output is written.
11. Counts recomputed in this session: `PASS=8 FAIL=0`, centre pairs
    `(1, 1)` and `(-3, -1)` with cross sum `4`, `(2, 1)` and `(-6, -1)`
    with cross sum `8`, and `(1, 1)` and `(-2, -1)` with cross sum `3`.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the note and
    the loop-pack prose. The full audit pipeline was not run.

## 2026-10-11 author check, cycle 37

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms on origin/main at the base `0b208e91cfc`, the
   cycle-36 doubled sign and matched note, the cycle-34 doubled
   transverse-sign note, and the cycle-32 ratio-span note, all three
   notes on this branch. The partner rank and the witness sums are
   computed in this runner. The order-blind converse is not applied.
   The parity kernels are cited from cycle 34. Both ratio spans are
   named in cycle 32, and this runner recomputes that every generator
   has chirality coefficient 0. The dimension count of the soldered
   bond space is not repeated.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/chiral_pair_twice_chi_ts_matched_line_cross_moments_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `a27349db7aa59ce9ea524ce4b7001112f9ece48bc9a70e6829d69ceb9c2fe148`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=8 FAIL=0`.
   Elapsed 0.54 seconds.
3. Scope. The line through twice the chirality cap, the transverse-sign
   cap, and the matched transverse cross, on the 48 signed permutations
   of `(1, 2, 3)`. The sum has two nonzero parity-kernel coefficients
   and one nonzero excluded coefficient. The transverse-sign coefficient
   is 1 and the chirality coefficient is 2, so the sum is outside the
   equal-coefficient line and outside the doubled matched line. The
   transverse-sign coefficient is not twice the chirality coefficient,
   so the sum is outside the doubled transverse-sign line and outside
   the line with transverse-sign coefficient 2 and matched coefficient
   2. It is also outside both ratio spans. Every ordered height pair
   gives partner rank 10, and doubling the line doubles every partner
   row, so the only ten-kernel partner is 0. The witness centre pairs
   are `(-1, 1)` and `(0, -1)`, with cross sum `-1`, and `(-2, 1)` and
   `(0, -1)`, with cross sum `-2`. The first left contributes `-1` and
   the second left contributes 0. The doubled sign and matched vector
   on the same bond has centre pairs `(1, 1)` and `(-3, -1)` and cross
   sum `4`. A different ratio of these three kernels is outside the
   ansatz. The ten-kernel coefficient span is not classified. The full
   soldered bond space is not classified. Status line
   `proposed_retained`. Surface status `bounded-support`.
4. N-gate does not apply. The artifact prunes one named line. It does
   not claim that no vector in the ten-kernel coefficient span has a
   nonzero partner.
5. Obligations are in the note. The missing lemma is whether twice the
   chirality cap plus twice the transverse-sign cap plus the matched
   transverse cross can pair with a nonzero ten-kernel vector and still
   have every cross moment equal to 0.
6. Mutations, each on a scratch copy, exited 1. Requiring the height
   1 and 2 cross sum to be 1 gave `PASS=7 FAIL=1` on the centre-pair
   check. Requiring the partner rank to differ from 9 gave `PASS=7
   FAIL=1` on the rank check. Requiring the doubled cross sum to be 1
   gave `PASS=7 FAIL=1` on the doubled-line check. An independent
   closure under signed monomial matrices of determinant 1 gave 24
   rotations, all of determinant 1, and orbit 24, with `(2, 1, 3)` and
   `(1, 2, -3)` outside the orbit.
7. One primary runner. No packet helper.
8. Five markdown links. The runner link points at the primary runner.
   One note link points at the minimal axioms on origin/main. Three
   point at the cycle-36 doubled sign and matched note, the cycle-34
   doubled transverse-sign note, and the cycle-32 ratio-span note on
   this branch. Manifest node_count 6906 and edge_count 15530. The new
   node has out_degree 4 and deps_hash `2daef32d9e7f`. Dependencies are
   `minimal_axioms`, the cycle-36 doubled sign and matched note, the
   cycle-34 doubled transverse-sign note, and the cycle-32 ratio-span
   note. `citation_graph.json` was deleted.
9. Machine-status fields match this certificate. The imports paragraph
   names the doubled sign and matched line, the parity kernels, and the
   two triples, and states that the order-blind converse is not applied
   and that no rate is imported.
10. No audit status, effective status, or ledger output is written.
11. Counts recomputed in this session: `PASS=8 FAIL=0`, centre pairs
    `(-1, 1)` and `(0, -1)` with cross sum `-1`, `(-2, 1)` and
    `(0, -1)` with cross sum `-2`, and `(1, 1)` and `(-3, -1)` with
    cross sum `4`.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the note and
    the loop-pack prose. The full audit pipeline was not run.

## 2026-10-11 author check, cycle 38

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms on origin/main at the base `0b208e91cfc`, the
   cycle-29 parity-span note, and the cycle-37 doubled chirality note,
   both notes on this branch. The partner kernel, the stacked rank, and
   the witness sums are computed in this runner. The order-blind
   converse is not applied. The even bases are named in cycle 29 and
   recomputed here. The five lines are cited from cycle 37 and are not
   re-proved. The dimension count of the soldered bond space is not
   repeated.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/chiral_pair_chi_ts_matched_span_partner_kernel_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `d34ca9c864260c7bddf73f661c63cd099808f07fab83999b9462c1dc69c591c7`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=8 FAIL=0`.
   Elapsed 3.04 seconds.
3. Scope. The rational span of the chirality cap, the transverse-sign
   cap, and the matched transverse cross, on the 48 signed permutations
   of `(1, 2, 3)`. The span is 3-dimensional and meets each ratio span
   of the oblique-matched plane only at 0. A nonzero vector has partner
   rank 10 exactly when its matched coefficient is nonzero, and then
   the only ten-kernel partner is 0. When the matched coefficient is 0,
   the partner rank is 7 and the partner kernel is the even space of
   the partner height relative to the source height. The generators
   have excluded coefficients 0. The chirality cap pairs with the sign
   product. The witness centre pairs are `(-1, 1)` and `(1, 1)`, with
   cross sum `0`, and `(-1, 1)` and `(0, 1)`, with cross sum `-1`. The
   first left contributes `-1`. The second left contributes `1` for the
   chirality cap and `0` after the matched cross is added. The triples
   `(2, -3, 5)` and `(2, -3, 0)` have partner ranks 10 and 7. A vector
   outside the three kernels is outside the ansatz. The ten-kernel
   coefficient span is not classified. The full soldered bond space is
   not classified. Status line `proposed_retained`. Surface status
   `bounded-support`.
4. N-gate does not apply. The artifact classifies one named span. It
   does not claim that no vector outside that span has a nonzero
   partner.
5. Obligations are in the note. The missing lemma is whether the sign
   product has a ten-kernel partner outside the odd space of the
   partner height.
6. Mutations, each on a scratch copy, exited 1. Requiring the stacked
   rank to be 30 gave `PASS=7 FAIL=1` on the stacked-map check.
   Requiring the chirality-cap cross sum to be 1 gave `PASS=7 FAIL=1`
   on the centre-pair check. Requiring the cap partner rank to be 10
   gave `PASS=7 FAIL=1` on the even-space check. An independent
   generator closure gave 24 rotations, all of determinant 1, and orbit
   24, with `(2, 1, 3)` and `(1, 2, -3)` outside the orbit.
7. One primary runner. No packet helper.
8. Four markdown links. The runner link points at the primary runner.
   One note link points at the minimal axioms on origin/main. Two point
   at the cycle-29 parity-span note and the cycle-37 doubled chirality
   note on this branch. Manifest node_count 6907 and edge_count 15533.
   The new node has out_degree 3 and deps_hash `3d0e417d375a`.
   Dependencies are `minimal_axioms`, the cycle-29 parity-span note,
   and the cycle-37 doubled chirality note. `citation_graph.json` was
   deleted.
9. Machine-status fields match this certificate. The imports paragraph
   names the even bases and the five lines, and states that the
   order-blind converse is not applied and that no rate is imported.
10. No audit status, effective status, or ledger output is written.
11. Counts recomputed in this session: `PASS=8 FAIL=0`, stacked rank
    24, centre pairs `(-1, 1)` and `(1, 1)` with cross sum `0`, and
    `(-1, 1)` and `(0, 1)` with cross sum `-1`.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the note.
    The loop-pack directory is skipped by that lint. The full audit
    pipeline was not run.

## 2026-10-11 author check, cycle 39

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms on origin/main at the base `0b208e91cfc`, the
   cycle-29 parity-span note, and the cycle-38 chirality,
   transverse-sign, and matched note, both notes on this branch. The
   partner kernel, the stacked rank, and the witness sums are computed
   in this runner. The order-blind converse is not applied. The odd and
   even bases are named in cycle 29 and recomputed here. The cycle-38
   span is cited and not re-proved. The dimension count of the soldered
   bond space is not repeated.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/chiral_pair_even_span_partner_kernel_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `5d1c2af478ed102decd306aea526a3f1a1cd54dbcf879f69da08352ce0ccc72b`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=8 FAIL=0`.
   Elapsed 5.60 seconds.
3. Scope. The even span of the source height, on the 48 signed
   permutations of `(1, 2, 3)`. The span is 3-dimensional, its excluded
   coefficients are 0, and it meets the three excluded axes only at 0.
   Every nonzero vector has partner rank 6, and the partner kernel is
   the odd space of the partner height. The sign product lies in every
   even span and has no partner outside that odd space. The witness
   centre pairs are `(1, -1)` and `(1, 1)`, with cross sum `0`, and
   `(1, 0)` and `(1, 1)`, with cross sum `1`. The first left contributes
   `-1` against the chirality cap and `0` against the matched cross.
   The second left contributes `1` in both comparisons. The triples
   `(1, 0, 0)` and `(1, 1, 1)` have partner rank 6. A vector outside
   the even span is outside the ansatz. The ten-kernel coefficient span
   is not classified. The full soldered bond space is not classified.
   Status line `proposed_retained`. Surface status `bounded-support`.
4. N-gate does not apply. The artifact classifies one named span. It
   does not claim that no vector outside that span has a nonzero
   partner.
5. Obligations are in the note. The missing lemma is whether the
   swapped cross has a ten-kernel partner outside the even space of the
   partner height.
6. Mutations, each on a scratch copy, exited 1. Requiring the stacked
   rank to be 24 gave `PASS=7 FAIL=1` on the stacked-map check.
   Requiring the sign-product cross sum to be 1 gave `PASS=7 FAIL=1`
   on the centre-pair check. Requiring the generator partner rank to be
   10 gave `PASS=7 FAIL=1` on the odd-space check. An independent
   generator closure, recomputed in this session, gave 24 rotations,
   all of determinant 1, and orbit 24, with `(2, 1, 3)` and
   `(1, 2, -3)` outside the orbit.
7. One primary runner. No packet helper.
8. Four markdown links. The runner link points at the primary runner.
   One note link points at the minimal axioms on origin/main. Two point
   at the cycle-29 parity-span note and the cycle-38 span note on this
   branch. Manifest node_count 6908 and edge_count 15536. The new node
   has out_degree 3 and deps_hash `02e1180c1a5c`. Dependencies are
   `minimal_axioms`, the cycle-29 parity-span note, and the cycle-38
   span note. `citation_graph.json` was deleted.
9. Machine-status fields match this certificate. The imports paragraph
   names the odd and even bases and the previous span, and states that
   the order-blind converse is not applied and that no rate is imported.
10. No audit status, effective status, or ledger output is written.
11. Counts recomputed in this session: `PASS=8 FAIL=0`, stacked rank
    18, centre pairs `(1, -1)` and `(1, 1)` with cross sum `0`, and
    `(1, 0)` and `(1, 1)` with cross sum `1`.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the note.
    The loop-pack directory is skipped by that lint. The full audit
    pipeline was not run.

## 2026-10-11 author check, cycle 40

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms on origin/main at the base `0b208e91cfc`, the
   cycle-29 parity-span note, and the cycle-39 even-span note, both
   notes on this branch. The odd-pair partner kernel and the witness
   sums are computed in this runner. The order-blind converse is not
   applied. The odd and even bases are named in cycle 29. The even-pair
   partner kernel is cited from cycle 39 and not re-proved. The
   dimension count of the soldered bond space is not repeated.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/chiral_pair_swapped_cross_partner_kernel_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `fbc48b6e52742db912c3c8af36794e918b6044f20a2cb98ed7ab75ba579b5b5a`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=9 FAIL=0`.
   Elapsed 0.71 seconds.
3. Scope. The swapped cross on the 48 signed permutations of
   `(1, 2, 3)`. It is odd on `(1, 2)`, `(2, 1)`, and `(3, 1)`, and even
   on `(1, 3)`, `(2, 3)`, and `(3, 2)`. On each odd pair a nonzero
   scale has partner rank 7, and the partner kernel is the even space
   of the partner height, so no ten-kernel partner lies outside that
   space. On each even pair the cited partner kernel is the odd space,
   which meets the even space only at 0. The heights 1 and 2 centre
   pairs are `(1, -1)` and `(-1, -1)` with cross sum `0`, `(1, -1)` and
   `(-1, 1)` with cross sum `-2`, and `(1, 0)` and `(-1, 1)` with cross
   sum `-1`. The heights 1 and 3 centre pairs are `(-1, 1)` and
   `(-1, -1)` with cross sum `0`, and `(-1, 1)` and `(-1, 1)` with
   cross sum `-2`. A vector other than the swapped cross is outside the
   ansatz. The odd space is not settled. The ten-kernel coefficient
   span is not classified. The full soldered bond space is not
   classified. Status line `proposed_retained`. Surface status
   `bounded-support`.
4. N-gate does not apply. The artifact classifies the swapped cross. It
   does not claim that no other odd vector has a partner outside the
   even space.
5. Obligations are in the note. The missing lemma is whether a nonzero
   vector in the odd space, outside the chirality and transverse-sign
   plane and outside the swapped axis, has a ten-kernel partner outside
   the even space of the partner height.
6. Mutations, each on a scratch copy, exited 1. Requiring the odd-pair
   partner rank to be 10 gave `PASS=8 FAIL=1` on the partner-kernel
   check. Requiring the chirality cross sum to be 0 gave `PASS=8 FAIL=1`
   on the centre-pair check. Requiring the swapped cross to be even on
   the odd pairs gave `PASS=8 FAIL=1` on the membership check. An
   independent generator closure, recomputed in this session, gave 24
   rotations, all of determinant 1, and orbit 24, with `(2, 1, 3)` and
   `(1, 2, -3)` outside the orbit.
7. One primary runner. No packet helper.
8. Four markdown links. The runner link points at the primary runner.
   One note link points at the minimal axioms on origin/main. Two point
   at the cycle-29 parity-span note and the cycle-39 even-span note on
   this branch. Manifest node_count 6909 and edge_count 15539. The new
   node has out_degree 3 and deps_hash `95da1868a9cc`. Dependencies are
   `minimal_axioms`, the cycle-29 parity-span note, and the cycle-39
   even-span note. `citation_graph.json` was deleted.
9. Machine-status fields match this certificate. The imports paragraph
   names the odd and even bases and the even-span note, and states that
   the order-blind converse is not applied and that no rate is imported.
10. No audit status, effective status, or ledger output is written.
11. Counts recomputed in this session: `PASS=9 FAIL=0`, odd-pair partner
    rank 7, centre pairs `(1, -1)` and `(-1, -1)` with cross sum `0`,
    `(1, -1)` and `(-1, 1)` with cross sum `-2`, and `(1, 0)` and
    `(-1, 1)` with cross sum `-1`.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the note.
    The loop-pack directory is skipped by that lint. The full audit
    pipeline was not run.

## 2026-10-11 author check, cycle 41

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms on origin/main at the base `0b208e91cfc`, the
   cycle-29 parity-span note, and the cycle-40 swapped-cross note, both
   notes on this branch. The odd-space partner kernel, the stacked rank,
   and the witness sums are computed in this runner. The order-blind
   converse is not applied. The odd and even bases are named in cycle
   29. The swapped axis is included in the odd space. The even-span
   partner kernel is not re-proved. The dimension count of the soldered
   bond space is not repeated.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/chiral_pair_odd_space_partner_kernel_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `ab4b35964b4fcdb5d7bcd195627f80d720c0d95a18755e57c88f4993b33001d3`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=9 FAIL=0`.
   Elapsed 7.60 seconds.
3. Scope. The odd space of the source height, on the 48 signed
   permutations of `(1, 2, 3)`. The space is 4-dimensional, its excluded
   coefficients are 0, and it meets the even basis only at 0. Every
   nonzero vector has partner rank 7, and the partner kernel is the even
   space of the partner height. The parallel-oblique sum lies in that
   odd space at heights 1 and 2 and outside the chirality and
   transverse-sign plane, with swapped coefficient 0. The witness centre
   pairs are `(-1, -1)` and `(1, -1)` with cross sum `0`, `(-1, -1)` and
   `(1, 1)` with cross sum `2`, and `(-1, 0)` and `(1, 1)` with cross
   sum `1`. The coefficient tuples `(1, 0, 0, 0)`, `(0, 0, 0, 1)`, and
   `(1, 1, 1, 1)` have partner rank 7. The stacked map has rank 28 and
   nullity 12. A vector with both an odd part and an even part is
   outside the ansatz. The ten-kernel coefficient span is not
   classified. The full soldered bond space is not classified. Status
   line `proposed_retained`. Surface status `bounded-support`.
4. N-gate does not apply. The artifact classifies the odd space. It
   does not claim that no mixed odd-even vector has a nonzero partner.
5. Obligations are in the note. The missing lemma is whether a vector
   with both an odd part and an even part has a ten-kernel partner
   other than 0.
6. Mutations, each on a scratch copy, exited 1. Requiring the stacked
   rank to be 24 gave `PASS=8 FAIL=1` on the stacked-map check.
   Requiring the chirality cross sum to be 0 gave `PASS=8 FAIL=1` on
   the centre-pair check. Requiring the generator partner rank to be 10
   gave `PASS=8 FAIL=1` on the generator check. An independent generator
   closure, recomputed in this session, gave 24 rotations, all of
   determinant 1, and orbit 24, with `(2, 1, 3)` and `(1, 2, -3)`
   outside the orbit.
7. One primary runner. No packet helper.
8. Four markdown links. The runner link points at the primary runner.
   One note link points at the minimal axioms on origin/main. Two point
   at the cycle-29 parity-span note and the cycle-40 swapped-cross note
   on this branch. Manifest node_count 6910 and edge_count 15542. The
   new node has out_degree 3 and deps_hash `7a304fc545c5`. Dependencies
   are `minimal_axioms`, the cycle-29 parity-span note, and the cycle-40
   swapped-cross note. `citation_graph.json` was deleted.
9. Machine-status fields match this certificate. The imports paragraph
   names the odd and even bases and the swapped-cross note, and states
   that the order-blind converse is not applied and that no rate is
   imported.
10. No audit status, effective status, or ledger output is written.
11. Counts recomputed in this session: `PASS=9 FAIL=0`, stacked rank
    28, centre pairs `(-1, -1)` and `(1, -1)` with cross sum `0`,
    `(-1, -1)` and `(1, 1)` with cross sum `2`, and `(-1, 0)` and
    `(1, 1)` with cross sum `1`.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the note.
    The loop-pack directory is skipped by that lint. The full audit
    pipeline was not run.

## 2026-10-11 author check, cycle 42

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms on origin/main at the base `0b208e91cfc`, the
   cycle-29 parity-span note, and the cycle-41 odd-space note, both
   notes on this branch. The joint partner kernel and the witness sums
   are computed in this runner. The order-blind converse is not applied.
   The odd and even bases are named in cycle 29. The pure odd and pure
   even partner kernels are not the claim of this note. The dimension
   count of the soldered bond space is not repeated.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/chiral_pair_mixed_parity_partner_kernel_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `ce91f7fe6efe1d0f62efda9ae4b2b736cdbf77cfe253fcc1a876b56ab3817f4a`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=8 FAIL=0`.
   Elapsed 8.09 seconds.
3. Scope. A parity vector with both an odd part and an even part, on
   the 48 signed permutations of `(1, 2, 3)`. Every such vector has
   partner rank 10, so the only ten-kernel partner is 0. The orthogonal
   cross lies in the parity span and in neither summand. At heights 1
   and 2 it is half the swapped cross plus the even generator with
   swapped coefficient `-1/2` and orthogonal coefficient `1`. The
   chirality cap plus the sign product also has partner rank 10. The
   joint map has rank 46 and nullity 24. The witness centre pairs are
   `(0, -1)` and `(-1, -1)` with cross sum `1`, `(0, -1)` and `(-1, 1)`
   with cross sum `-1`, and `(0, 0)` and `(-1, 1)` with cross sum `-1`.
   The first left contributes 0 in each comparison. The second left
   contributes `1`, `-1`, and `-1`. A vector with a nonzero excluded
   coefficient is outside the ansatz. The ten-kernel coefficient span
   is not classified. The full soldered bond space is not classified.
   Status line `proposed_retained`. Surface status `bounded-support`.
4. N-gate does not apply. The artifact classifies mixed parity vectors.
   It does not claim that no vector with an excluded coefficient has a
   nonzero partner.
5. Obligations are in the note. The missing lemma is whether a vector
   with a nonzero coefficient on the swapped transverse dot or the
   scaled cross-dot kernel has a ten-kernel partner other than 0.
6. Mutations, each on a scratch copy, exited 1. Requiring the joint
   rank to be 40 gave `PASS=7 FAIL=1` on the joint-map check. Requiring
   the sign-product cross sum to be 0 gave `PASS=7 FAIL=1` on the
   centre-pair check. Requiring the orthogonal cross to lie in the even
   basis gave `PASS=7 FAIL=1` on the membership check. An independent
   generator closure, recomputed in this session, gave 24 rotations,
   all of determinant 1, and orbit 24, with `(2, 1, 3)` and
   `(1, 2, -3)` outside the orbit.
7. One primary runner. No packet helper.
8. Four markdown links. The runner link points at the primary runner.
   One note link points at the minimal axioms on origin/main. Two point
   at the cycle-29 parity-span note and the cycle-41 odd-space note on
   this branch. Manifest node_count 6911 and edge_count 15545. The new
   node has out_degree 3 and deps_hash `8259e48188f8`. Dependencies are
   `minimal_axioms`, the cycle-29 parity-span note, and the cycle-41
   odd-space note. `citation_graph.json` was deleted.
9. Machine-status fields match this certificate. The imports paragraph
   names the odd and even bases and the odd-space note, and states that
   the order-blind converse is not applied and that no rate is imported.
10. No audit status, effective status, or ledger output is written.
11. Counts recomputed in this session: `PASS=8 FAIL=0`, joint rank 46,
    centre pairs `(0, -1)` and `(-1, -1)` with cross sum `1`,
    `(0, -1)` and `(-1, 1)` with cross sum `-1`, and `(0, 0)` and
    `(-1, 1)` with cross sum `-1`.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the note.
    The loop-pack directory is skipped by that lint. The full audit
    pipeline was not run.

## 2026-10-11 author check, cycle 43

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms on origin/main at the base `0b208e91cfc`, the
   cycle-32 ratio-span note, and the cycle-41 odd-space note, both
   notes on this branch. The stacked partner kernels and the witness
   sums are computed in this runner. The order-blind converse is not
   applied. The two spans are named in cycle 32. The even space is
   named in cycle 41. The partner kernel of one ratio span is not the
   claim of this note. The dimension count of the soldered bond space
   is not repeated.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/chiral_pair_ratio_span_sum_partner_kernel_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `71737dc07b2850ccc23fd5e8b1ca845b957fd6ceebeeb6c73cab97a61c2c1ff8`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=8 FAIL=0`.
   Elapsed 14.45 seconds.
3. Scope. The sum of the two ratio spans, together with the chirality
   cap, on the 48 signed permutations of `(1, 2, 3)`. A nonzero vector
   in the sum has a nonzero ten-kernel partner if and only if it lies
   in exactly one span. A vector with a nonzero part in each span has
   partner rank 10. The six-generator map has rank 42 and nullity 18.
   The chirality cap lies outside the sum. The chirality map has rank
   49 and nullity 21, and the cap plus a nonzero sum vector has partner
   rank 10. The swapped transverse dot sits only on the
   swapped-orthogonal generator, and the scaled cross-dot kernel sits
   only on the cap generator. The witness centre pairs are `(0, 0)` and
   `(2, 2)` with cross sum `4`, and `(-1, -1)` and `(-1, -1)` with
   cross sum `2`. A vector outside the span of the chirality cap and
   the two ratio spans is outside the ansatz. The ten-kernel coefficient
   span is not classified. The full soldered bond space is not
   classified. Status line `proposed_retained`. Surface status
   `bounded-support`.
4. N-gate does not apply. The artifact classifies vectors inside the
   span of the chirality cap and the two ratio spans. It does not claim
   that no vector outside that span has a nonzero partner.
5. Obligations are in the note. The missing lemma is whether a vector
   outside that span, with a nonzero coefficient on the swapped
   transverse dot or the scaled cross-dot kernel, has a ten-kernel
   partner other than 0.
6. Mutations, each on a scratch copy, exited 1. Requiring the
   six-generator rank to be 40 gave `PASS=7 FAIL=1` on the
   six-generator map. Requiring the both-span cross sum to be 0 gave
   `PASS=7 FAIL=1` on the centre-pair check. Requiring the chirality
   cap to lie in the sum gave `PASS=7 FAIL=1` on the membership check.
   An independent generator closure, recomputed in this session, gave
   24 rotations, all of determinant 1, alphabet 48, and orbit 24, with
   `(2, 1, 3)` and `(1, 2, -3)` outside the orbit.
7. One primary runner. No packet helper.
8. Four markdown links. The runner link points at the primary runner.
   One note link points at the minimal axioms on origin/main. Two point
   at the cycle-32 ratio-span note and the cycle-41 odd-space note on
   this branch. Manifest node_count 6912 and edge_count 15548. The new
   node has out_degree 3 and deps_hash `2980de49e84f`. Dependencies are
   `minimal_axioms`, the cycle-32 ratio-span note, and the cycle-41
   odd-space note. `citation_graph.json` was deleted.
9. Machine-status fields match this certificate. The imports paragraph
   names the two spans and the even space, and states that the
   order-blind converse is not applied and that no rate is imported.
10. No audit status, effective status, or ledger output is written.
11. Counts recomputed in this session: `PASS=8 FAIL=0`, six-generator
    rank 42, chirality rank 49, centre pairs `(0, 0)` and `(2, 2)` with
    cross sum `4`, and `(-1, -1)` and `(-1, -1)` with cross sum `2`.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the note.
    The loop-pack directory is skipped by that lint. The full audit
    pipeline was not run.

## 2026-10-11 author check, cycle 44

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms on origin/main at the base `0b208e91cfc`, the
   cycle-39 even-span note, and the cycle-32 ratio-span note, both
   notes on this branch. The seven-generator kernel and the witness
   sums are computed in this runner. The order-blind converse is not
   applied. The even space and its odd partner are named in cycle 39.
   The two spans are named in cycle 32. The partner kernel of the even
   space alone is not the claim of this note. The dimension count of
   the soldered bond space is not repeated.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/chiral_pair_even_one_span_partner_kernel_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `c98edd2f397242e22641b66f9b3ee2e5523a26f443ccab17d2df65164dfb23c0`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=7 FAIL=0`.
   Elapsed 21.33 seconds.
3. Scope. The even space, the chirality cap, and one ratio span, on the
   48 signed permutations of `(1, 2, 3)`. A nonzero vector in the sum
   has a nonzero ten-kernel partner if and only if it lies in exactly
   one summand. The seven-generator map has rank 46 and nullity 24.
   The odd space, the even space, and the partner span meet pairwise
   only at 0. A nonzero swapped-dot or scaled coefficient has a
   nonzero partner exactly when the vector lies in the ratio span. The
   witness centre pairs are `(-1, 0)` and `(-1, 2)` with cross sum
   `-2`, and `(-3, 0)` and `(1, -4)` with cross sum `-4`. A vector
   that meets the other ratio span is outside the ansatz. The
   ten-kernel coefficient span is not classified. The full soldered
   bond space is not classified. Status line `proposed_retained`.
   Surface status `bounded-support`.
4. N-gate does not apply. The artifact classifies vectors inside the
   even space, the chirality cap, and one ratio span. It does not claim
   that no vector meeting both ratio spans has a nonzero partner.
5. Obligations are in the note. The missing lemma is whether a vector
   that meets both ratio spans and has a nonzero even part, with a
   nonzero coefficient on the swapped transverse dot or the scaled
   cross-dot kernel, has a ten-kernel partner other than 0.
6. Mutations, each on a scratch copy, exited 1. Requiring the
   seven-generator rank to be 40 gave `PASS=6 FAIL=1` on the product
   map. Requiring the swapped-orthogonal cross sum to be 0 gave
   `PASS=6 FAIL=1` on the centre-pair check. Requiring the sum of the
   even space, the chirality cap, and one span to have rank 6 gave
   `PASS=6 FAIL=1` on the membership check. An independent generator
   closure, recomputed in this session, gave 24 rotations, all of
   determinant 1, alphabet 48, and orbit 24, with `(2, 1, 3)` and
   `(1, 2, -3)` outside the orbit.
7. One primary runner. No packet helper.
8. Four markdown links. The runner link points at the primary runner.
   One note link points at the minimal axioms on origin/main. Two point
   at the cycle-39 even-span note and the cycle-32 ratio-span note on
   this branch. Manifest node_count 6913 and edge_count 15551. The new
   node has out_degree 3 and deps_hash `8817e2ad5d19`. Dependencies are
   `minimal_axioms`, the cycle-39 even-span note, and the cycle-32
   ratio-span note. `citation_graph.json` was deleted.
9. Machine-status fields match this certificate. The imports paragraph
   names the even space and the two spans, and states that the
   order-blind converse is not applied and that no rate is imported.
10. No audit status, effective status, or ledger output is written.
11. Counts recomputed in this session: `PASS=7 FAIL=0`, seven-generator
    rank 46, centre pairs `(-1, 0)` and `(-1, 2)` with cross sum `-2`,
    and `(-3, 0)` and `(1, -4)` with cross sum `-4`.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the note.
    The loop-pack directory is skipped by that lint. The full audit
    pipeline was not run.

## 2026-10-11 author check, cycle 45

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms on origin/main at the base `0b208e91cfc`, the
   cycle-39 even-span note, and the cycle-32 ratio-span note, both
   notes on this branch. The nine-generator kernel, the cap ratios, and
   the witness sums are computed in this runner. The order-blind
   converse is not applied. The even space is named in cycle 39. The
   two spans are named in cycle 32. The partner kernel of one ratio
   span is not the claim of this note. The dimension count of the
   soldered bond space is not repeated.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/chiral_pair_even_both_spans_partner_kernel_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `bcc80dcc991fa3024bc5a07bb1bb6afff1023dc39611448e103ed45406ac7d3f`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=9 FAIL=0`.
   Elapsed 11.32 seconds.
3. Scope. The even space and both ratio spans, on the 48 signed
   permutations of `(1, 2, 3)`. The sum is 9-dimensional and the
   chirality cap lies outside it. The nine-generator map has rank 42
   and nullity 48, and the kernel projects onto every even coefficient.
   The scaled coefficient `4/3` has partner rank 7, with the listed
   3-dimensional kernel on each ordered height pair. The scaled
   coefficient 4 has partner rank 10. The swapped-dot coefficient 1 has
   partner rank 10. The witness centre pairs are `(-1, 0)` and
   `(1, 2)` with cross sum `2`, and `(-3, 0)` and `(1, -4)` with cross
   sum `-4`. Each listed partner of the coefficient `4/3` vector has
   cross sum 0 on those directions. A nonzero chirality coefficient is
   outside the ansatz. The ten-kernel coefficient span is not
   classified. The full soldered bond space is not classified. Status
   line `proposed_retained`. Surface status `bounded-support`.
4. N-gate does not apply. The artifact classifies two cap ratios and
   one swapped-dot vector inside the even space and both ratio spans.
   It does not claim that no vector with a nonzero chirality
   coefficient has a nonzero partner.
5. Obligations are in the note. The missing lemma is whether a vector
   with a nonzero chirality coefficient, a nonzero even part, and a
   nonzero part in each ratio span, with a nonzero coefficient on the
   swapped transverse dot or the scaled cross-dot kernel, has a
   ten-kernel partner other than 0.
6. Mutations, each on a scratch copy, exited 1. Requiring the
   nine-generator rank to be 40 gave `PASS=8 FAIL=1` on the map check.
   Requiring the scaled coefficient to be `5/3` gave `PASS=8 FAIL=1`
   on the cap-ratio check. Requiring the sum of the even space and both
   spans to have rank 8 gave `PASS=8 FAIL=1` on the membership check.
   An independent generator closure, recomputed in this session, gave
   24 rotations, all of determinant 1, alphabet orbit 24, with
   `(2, 1, 3)` and `(1, 2, -3)` outside the orbit.
7. One primary runner. No packet helper.
8. Four markdown links. The runner link points at the primary runner.
   One note link points at the minimal axioms on origin/main. Two point
   at the cycle-39 even-span note and the cycle-32 ratio-span note on
   this branch. Manifest node_count 6914 and edge_count 15554. The new
   node has out_degree 3 and deps_hash `8817e2ad5d19`. Dependencies are
   `minimal_axioms`, the cycle-39 even-span note, and the cycle-32
   ratio-span note. `citation_graph.json` was deleted.
9. Machine-status fields match this certificate. The imports paragraph
   names the even space and the two spans, and states that the
   order-blind converse is not applied and that no rate is imported.
10. No audit status, effective status, or ledger output is written.
11. Counts recomputed in this session: `PASS=9 FAIL=0`, nine-generator
    rank 42, scaled coefficients `4/3` and 4 with partner ranks 7 and
    10, centre pairs `(-1, 0)` and `(1, 2)` with cross sum `2`, and
    `(-3, 0)` and `(1, -4)` with cross sum `-4`.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the note.
    The loop-pack directory is skipped by that lint. The full audit
    pipeline was not run.

## 2026-10-11 author check, cycle 46

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms on origin/main at the base `0b208e91cfc`, the
   cycle-39 even-span note, and the cycle-32 ratio-span note, both
   notes on this branch. The ten-generator kernel, the chirality
   restriction, and the witness sums are computed in this runner. The
   order-blind converse is not applied. The even space is named in
   cycle 39. The two spans are named in cycle 32. The partner kernel
   at chirality coefficient 0 is recomputed here. The dimension count
   of the soldered bond space is not repeated.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/chiral_pair_even_both_spans_chirality_partner_kernel_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `0c8c73fed0602c1a1ba5898a8ae9fd3056d5e4d73955ae49397c73b1ca28c5ea`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=11 FAIL=0`.
   Elapsed 25.87 seconds.
3. Scope. The even space, both ratio spans, and the chirality cap, on
   the 48 signed permutations of `(1, 2, 3)`. The sum is 10-dimensional.
   The ten-generator map has rank 49 and nullity 51. The chirality cap
   alone has partner rank 7. The scaled coefficient `4/3` has partner
   rank 7, and the chirality block has rank 3 on that partner, so every
   nonzero chirality coefficient removes those partners. Chirality
   coefficient 1 gives that vector, the scaled coefficient 4 vector,
   and the swapped-dot coefficient 1 vector partner rank 10. The
   witness cross sums are `-6/5`, `-1/4`, and `1/2`. A chirality
   coefficient other than 1 is outside the full partner-rank count.
   The ten-kernel coefficient span is not classified. The full soldered
   bond space is not classified. Status line `proposed_retained`.
   Surface status `bounded-support`.
4. N-gate does not apply. The artifact classifies chirality coefficient
   1 on three vectors in the even space and both ratio spans. It does
   not claim that no other chirality coefficient has a nonzero partner.
5. Obligations are in the note. The missing lemma is whether a
   chirality coefficient other than 1, on the scaled coefficient `4/3`
   vector, has a ten-kernel partner other than 0.
6. Mutations, each on a scratch copy, exited 1. Requiring the
   ten-generator rank to be 48 gave `PASS=10 FAIL=1` on the chirality
   check. Requiring the coefficient `4/3` plus chirality coefficient 1
   to have partner rank 9 gave `PASS=10 FAIL=1` on the chirality check.
   Requiring the chirality restriction to have rank 2 gave
   `PASS=10 FAIL=1` on the chirality check. An independent generator
   closure, recomputed earlier in this session, gave 24 rotations, all
   of determinant 1, alphabet orbit 24, with `(2, 1, 3)` and
   `(1, 2, -3)` outside the orbit. This runner repeats that closure.
7. One primary runner. No packet helper.
8. Four markdown links. The runner link points at the primary runner.
   One note link points at the minimal axioms on origin/main. Two point
   at the cycle-39 even-span note and the cycle-32 ratio-span note on
   this branch. Manifest node_count 6915 and edge_count 15557. The new
   node has out_degree 3 and deps_hash `8817e2ad5d19`. Dependencies are
   `minimal_axioms`, the cycle-39 even-span note, and the cycle-32
   ratio-span note. `citation_graph.json` was deleted.
9. Machine-status fields match this certificate. The imports paragraph
   names the even space and the two spans, and states that the
   order-blind converse is not applied and that no rate is imported.
10. No audit status, effective status, or ledger output is written.
11. Counts recomputed in this session: `PASS=11 FAIL=0`, ten-generator
    rank 49, chirality coefficient 1 with partner rank 10, and cross
    sums `-6/5`, `-1/4`, and `1/2`.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the note.
    The loop-pack directory is skipped by that lint. The full audit
    pipeline was not run.

## 2026-10-11 author check, cycle 47

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms on origin/main at the base `0b208e91cfc`, the
   cycle-39 even-span note, and the cycle-32 ratio-span note, both
   notes on this branch. The minor gcd and the witness sums are
   computed in this runner. The order-blind converse is not applied.
   The even space is named in cycle 39. The two spans are named in
   cycle 32. The dimension count of the soldered bond space is not
   repeated.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/chiral_pair_cap_ratio_chirality_scale_partner_kernel_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `87e6bb0b982aac5f35ec7cf015ab1bd8fae06f513ca19cfae4ca453e98072877`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=12 FAIL=0`.
   Elapsed 29.30 seconds.
3. Scope. The scaled coefficient `4/3` vector plus an arbitrary
   chirality coefficient, on the 48 signed permutations of `(1, 2, 3)`.
   Coefficient 0 has partner rank 7. The coefficient pairs compress to
   14 rows, and a running gcd of the 10-by-10 minors is a nonzero
   multiple of the cube of the chirality coefficient, so every nonzero
   coefficient has partner rank 10. The witness cross sums at
   coefficient 1 are `-6/5`, `-1/4`, and `1/2`. The scaled coefficient
   4 vector is outside this all-scale count. The ten-kernel coefficient
   span is not classified. The full soldered bond space is not
   classified. Status line `proposed_retained`. Surface status
   `bounded-support`.
4. N-gate does not apply. The artifact classifies every chirality
   coefficient on one cap ratio. It does not claim that the scaled
   coefficient 4 vector has partner rank 10 at every chirality
   coefficient.
5. Obligations are in the note. The missing lemma is whether every
   nonzero chirality coefficient on the scaled coefficient 4 vector has
   partner rank 10.
6. Mutations, each on a scratch copy, exited 1. Requiring the minor gcd
   degree to be 4 gave `PASS=11 FAIL=1` on the pencil check. Requiring
   the ten-generator rank to be 48 gave `PASS=11 FAIL=1` on the
   chirality check. Requiring the even space plus both spans to have
   rank 8 gave `PASS=11 FAIL=1` on the membership check. An independent
   generator closure, recomputed earlier in this session, gave 24
   rotations, all of determinant 1, alphabet orbit 24, with `(2, 1, 3)`
   and `(1, 2, -3)` outside the orbit. This runner repeats that
   closure.
7. One primary runner. No packet helper.
8. Four markdown links. The runner link points at the primary runner.
   One note link points at the minimal axioms on origin/main. Two point
   at the cycle-39 even-span note and the cycle-32 ratio-span note on
   this branch. Manifest node_count 6916 and edge_count 15560. The new
   node has out_degree 3 and deps_hash `8817e2ad5d19`. Dependencies are
   `minimal_axioms`, the cycle-39 even-span note, and the cycle-32
   ratio-span note. `citation_graph.json` was deleted.
9. Machine-status fields match this certificate. The imports paragraph
   names the even space and the two spans, and states that the
   order-blind converse is not applied and that no rate is imported.
10. No audit status, effective status, or ledger output is written.
11. Counts recomputed in this session: `PASS=12 FAIL=0`, minor gcd
    degree 3, and cross sums `-6/5`, `-1/4`, and `1/2`.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the note.
    The loop-pack directory is skipped by that lint. The full audit
    pipeline was not run.

## 2026-10-11 author check, cycle 48

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms on origin/main at the base `0b208e91cfc`, the
   cycle-39 even-span note, and the cycle-32 ratio-span note, both
   notes on this branch. The constant minor gcd is computed in this
   runner. The order-blind converse is not applied. The even space is
   named in cycle 39. The two spans are named in cycle 32. The
   dimension count of the soldered bond space is not repeated.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/chiral_pair_cap_sum_chirality_scale_partner_kernel_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `3e4a75259c4102892df4c07401f6b455a63ef3df5adfd91b8136e80d1368fe92`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=13 FAIL=0`.
   Elapsed 38.20 seconds.
3. Scope. The scaled coefficient 4 vector plus an arbitrary chirality
   coefficient, on the 48 signed permutations of `(1, 2, 3)`. The
   coefficient pairs compress to 17 rows, and a running gcd of the
   10-by-10 minors is a nonzero constant, so every chirality
   coefficient, including 0, has partner rank 10. The swapped-dot
   coefficient 1 vector is outside this all-scale count. The
   ten-kernel coefficient span is not classified. The full soldered
   bond space is not classified. Status line `proposed_retained`.
   Surface status `bounded-support`.
4. N-gate does not apply. The artifact classifies every chirality
   coefficient on the cap sum. It does not claim that the swapped-dot
   coefficient 1 vector has partner rank 10 at every chirality
   coefficient.
5. Obligations are in the note. The missing lemma is whether every
   chirality coefficient on the swapped-dot coefficient 1 vector has
   partner rank 10.
6. Mutations, each on a scratch copy, exited 1. Requiring the
   coefficient 4 minor gcd degree to be 1 gave `PASS=12 FAIL=1` on the
   constant-gcd check. Requiring the ten-generator rank to be 48 gave
   `PASS=12 FAIL=1` on the chirality check. Requiring the even space
   plus both spans to have rank 8 gave `PASS=12 FAIL=1` on the
   membership check. An independent generator closure, recomputed
   earlier in this session, gave 24 rotations, all of determinant 1,
   alphabet orbit 24, with `(2, 1, 3)` and `(1, 2, -3)` outside the
   orbit. This runner repeats that closure.
7. One primary runner. No packet helper.
8. Four markdown links. The runner link points at the primary runner.
   One note link points at the minimal axioms on origin/main. Two point
   at the cycle-39 even-span note and the cycle-32 ratio-span note on
   this branch. Manifest node_count 6917 and edge_count 15563. The new
   node has out_degree 3 and deps_hash `8817e2ad5d19`. Dependencies are
   `minimal_axioms`, the cycle-39 even-span note, and the cycle-32
   ratio-span note. `citation_graph.json` was deleted.
9. Machine-status fields match this certificate. The imports paragraph
   names the even space and the two spans, and states that the
   order-blind converse is not applied and that no rate is imported.
10. No audit status, effective status, or ledger output is written.
11. Counts recomputed in this session: `PASS=13 FAIL=0`, minor gcd
    degree 0, and partner rank 10 at every chirality coefficient.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the note.
    The loop-pack directory is skipped by that lint. The full audit
    pipeline was not run.

## 2026-10-11 author check, cycle 49

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms on origin/main at the base `0b208e91cfc`, the
   cycle-39 even-span note, and the cycle-32 ratio-span note, both
   notes on this branch. The pivot-minor gcd is computed in this
   runner. The order-blind converse is not applied. The even space is
   named in cycle 39. The two spans are named in cycle 32. The
   dimension count of the soldered bond space is not repeated.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/chiral_pair_dot_chirality_scale_partner_kernel_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `36563ad24d57f2bf60d3e32be1696dfd65af4c63d9ae6df0cbe6c838a8a910b2`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=14 FAIL=0`.
   Elapsed 42.34 seconds.
3. Scope. The swapped-dot coefficient 1 vector plus an arbitrary
   chirality coefficient, on the 48 signed permutations of `(1, 2, 3)`.
   The coefficient pairs compress to 17 rows. Gaussian elimination at
   chirality coefficients `0`, `1`, `1/3`, and `-1` selects ten pivot
   rows, and the running gcd of those maximal minors is a nonzero
   constant, so every chirality coefficient, including 0, has partner
   rank 10. A vector with both a nonzero swapped-dot coordinate and a
   nonzero scaled coordinate is outside this all-scale count. The
   ten-kernel coefficient span is not classified. The full soldered
   bond space is not classified. Status line `proposed_retained`.
   Surface status `bounded-support`.
4. N-gate does not apply. The artifact classifies every chirality
   coefficient on one swapped-dot vector. It does not claim that every
   vector meeting both spans, with a nonzero even part, has partner
   rank 10 at every nonzero chirality coefficient.
5. Obligations are in the note. The missing lemma is whether every
   nonzero chirality coefficient, on every vector that meets both ratio
   spans and has a nonzero even part, has partner rank 10.
6. Mutations, each on a scratch copy, exited 1. Requiring the
   pivot-minor gcd degree to be 1 gave `PASS=13 FAIL=1` on the
   pivot-gcd check. Requiring the ten-generator rank to be 48 gave
   `PASS=13 FAIL=1` on the chirality check. Requiring the even space
   plus both spans to have rank 8 gave `PASS=13 FAIL=1` on the
   membership check. An independent generator closure, recomputed
   earlier in this session, gave 24 rotations, all of determinant 1,
   alphabet orbit 24, with `(2, 1, 3)` and `(1, 2, -3)` outside the
   orbit. This runner repeats that closure.
7. One primary runner. No packet helper.
8. Four markdown links. The runner link points at the primary runner.
   One note link points at the minimal axioms on origin/main. Two point
   at the cycle-39 even-span note and the cycle-32 ratio-span note on
   this branch. Manifest node_count 6918 and edge_count 15566. The new
   node has out_degree 3 and deps_hash `8817e2ad5d19`. Dependencies are
   `minimal_axioms`, the cycle-39 even-span note, and the cycle-32
   ratio-span note. `citation_graph.json` was deleted.
9. Machine-status fields match this certificate. The imports paragraph
   names the even space and the two spans, and states that the
   order-blind converse is not applied and that no rate is imported.
10. No audit status, effective status, or ledger output is written.
11. Counts recomputed in this session: `PASS=14 FAIL=0`, pivot-minor
    gcd degree 0, and partner rank 10 at every chirality coefficient.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the note.
    The loop-pack directory is skipped by that lint. The full audit
    pipeline was not run.

## 2026-10-11 author check, cycle 50

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms on origin/main at the base `0b208e91cfc`, the
   cycle-39 even-span note, and the cycle-32 ratio-span note, both
   notes on this branch. The projected minor gcd is computed in this
   runner. The order-blind converse is not applied. The even space is
   named in cycle 39. The two spans are named in cycle 32. The
   dimension count of the soldered bond space is not repeated.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/chiral_pair_mixed_even_rank_partner_kernel_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `dca3919ae95467ffc49a8fea59e2c5ad74d85a4c572666e2f327f9afe6f53465`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=15 FAIL=0`.
   Elapsed 38.17 seconds.
3. Scope. The second even generator plus both swapped-dot generators,
   on the ordered height pairs `(1, 3)`, `(2, 3)`, and `(3, 2)`. The
   summed kernel vector has swapped coordinate `-1` and orthogonal
   coordinate `2`. The base image has rank 7 and contains every
   chirality row. The projected 7-by-7 pivot minors at coefficients
   `0` and `-1` have a nonzero constant gcd, so every chirality
   coefficient has partner rank 7. The source-same form of these
   coefficients is outside this rank-7 count. The ten-kernel
   coefficient span is not classified. The full soldered bond space is
   not classified. Status line `proposed_retained`. Surface status
   `bounded-support`.
4. N-gate does not apply. The artifact shows that one mixed vector has
   partner rank 7 at every chirality coefficient. It does not claim
   that the source-same form of those coefficients has partner rank 10.
5. Obligations are in the note. The missing lemma is whether every
   chirality coefficient on the source-same form of these coefficients
   has partner rank 10.
6. Mutations, each on a scratch copy, exited 1. Requiring the projected
   minor gcd degree to be 1 gave `PASS=14 FAIL=1` on the rank-7 check.
   Requiring the ten-generator rank to be 48 gave `PASS=14 FAIL=1` on
   the chirality check. Requiring the even space plus both spans to
   have rank 8 gave `PASS=14 FAIL=1` on the membership check. An
   independent generator closure, recomputed earlier in this session,
   gave 24 rotations, all of determinant 1, alphabet orbit 24, with
   `(2, 1, 3)` and `(1, 2, -3)` outside the orbit. This runner repeats
   that closure.
7. One primary runner. No packet helper.
8. Four markdown links. The runner link points at the primary runner.
   One note link points at the minimal axioms on origin/main. Two point
   at the cycle-39 even-span note and the cycle-32 ratio-span note on
   this branch. Manifest node_count 6919 and edge_count 15569. The new
   node has out_degree 3 and deps_hash `8817e2ad5d19`. Dependencies are
   `minimal_axioms`, the cycle-39 even-span note, and the cycle-32
   ratio-span note. `citation_graph.json` was deleted.
9. Machine-status fields match this certificate. The imports paragraph
   names the even space and the two spans, and states that the
   order-blind converse is not applied and that no rate is imported.
10. No audit status, effective status, or ledger output is written.
11. Counts recomputed in this session: `PASS=15 FAIL=0`, projected
    minor gcd degree 0, and partner rank 7 at every chirality
    coefficient on the three height pairs.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the note.
    The loop-pack directory is skipped by that lint. The full audit
    pipeline was not run.

## 2026-10-11 author check, cycle 51

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms on origin/main at the base `0b208e91cfc`, the
   cycle-39 even-span note, and the cycle-32 ratio-span note, both
   notes on this branch. The pivot-minor gcd is computed in this
   runner. The order-blind converse is not applied. The even space is
   named in cycle 39. The two spans are named in cycle 32. The
   dimension count of the soldered bond space is not repeated.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/chiral_pair_source_same_mixed_even_partner_kernel_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `80acbb3fb09f7b7859cbcd29b3d625652fd38cc62e3d4b2c37f6d7fd765a5566`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=16 FAIL=0`.
   Elapsed 38.98 seconds.
3. Scope. The second even generator plus both swapped-dot generators,
   on the source-same ordered height pairs `(1, 2)`, `(2, 1)`, and
   `(3, 1)`. The summed kernel vector has swapped coordinate `-2`,
   parallel coordinate `-1`, oblique coordinate `1`, and orthogonal
   coordinate `2`. The base image has rank 10. The coefficient pairs
   compress to 17 rows. The monic pivot minor at chirality coefficient
   1 is `(c - 2)^2`, and at coefficient 2 it is `c^3(c - 1)`. Their
   gcd is a nonzero constant, so every chirality coefficient has
   partner rank 10. The sign product plus both swapped-dot generators
   is outside this count. The ten-kernel coefficient span is not
   classified. The full soldered bond space is not classified. Status
   line `proposed_retained`. Surface status `bounded-support`.
4. N-gate does not apply. The artifact shows that one source-same
   mixed vector has partner rank 10 at every chirality coefficient. It
   does not claim that the sign product plus both swapped-dot
   generators has partner rank 10.
5. Obligations are in the note. The missing lemma is whether every
   chirality coefficient on the sign product plus both swapped-dot
   generators has partner rank 10.
6. Mutations, each on a scratch copy, exited 1. Requiring the
   pivot-minor gcd degree to be 1 gave `PASS=15 FAIL=1` on the
   source-same rank-10 check. Requiring the ten-generator rank to be
   48 gave `PASS=15 FAIL=1` on the chirality check. Requiring the even
   space plus both spans to have rank 8 gave `PASS=15 FAIL=1` on the
   membership check. An independent generator closure, recomputed in
   this session, gave 24 rotations, all of determinant 1, alphabet
   orbit 24, with `(2, 1, 3)` and `(1, 2, -3)` outside the orbit. This
   runner repeats that closure.
7. One primary runner. No packet helper.
8. Four markdown links. The runner link points at the primary runner.
   One note link points at the minimal axioms on origin/main. Two point
   at the cycle-39 even-span note and the cycle-32 ratio-span note on
   this branch. Manifest node_count 6920 and edge_count 15572. The new
   node has out_degree 3 and deps_hash `8817e2ad5d19`. Dependencies are
   `minimal_axioms`, the cycle-39 even-span note, and the cycle-32
   ratio-span note. `citation_graph.json` was deleted.
9. Machine-status fields match this certificate. The imports paragraph
   names the even space and the two spans, and states that the
   order-blind converse is not applied and that no rate is imported.
10. No audit status, effective status, or ledger output is written.
11. Counts recomputed in this session: `PASS=16 FAIL=0`, pivot-minor
    gcd degree 0, base rank 10, and partner rank 10 at every chirality
    coefficient on the three source-same height pairs.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the note.
    The loop-pack directory is skipped by that lint. The full audit
    pipeline was not run.

## 2026-10-11 author check, cycle 52

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms on origin/main at the base `0b208e91cfc`, the
   cycle-39 even-span note, and the cycle-32 ratio-span note, both
   notes on this branch. The pivot-minor gcd is computed in this
   runner. The order-blind converse is not applied. The even space is
   named in cycle 39. The two spans are named in cycle 32. The
   dimension count of the soldered bond space is not repeated.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/chiral_pair_sign_product_dot_partner_kernel_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `b2fe810ab08648c45ad2fd3aff631bbdae80d088c23841c817a979e92927e380`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=17 FAIL=0`.
   Elapsed 44.76 seconds.
3. Scope. The sign product plus both swapped-dot generators, on every
   ordered height pair. The summed kernel vector has sign-product
   coordinate `1`, swapped coordinate `-2`, and orthogonal coordinate
   `2`. The base image has rank 10. The coefficient pairs compress to
   17 rows. The pivot minors at chirality coefficients `0`, `1`, `-1`,
   and `-1/3` have a nonzero constant gcd, so every chirality
   coefficient has partner rank 10. On the source-same pairs the monic
   pivot minor at coefficient 0 is `(c - 1)^7`. The third even
   generator plus both swapped-dot generators is outside this count.
   The ten-kernel coefficient span is not classified. The full soldered
   bond space is not classified. Status line `proposed_retained`.
   Surface status `bounded-support`.
4. N-gate does not apply. The artifact shows that one vector has
   partner rank 10 at every chirality coefficient. It does not claim
   that the third even generator plus both swapped-dot generators has
   partner rank 10.
5. Obligations are in the note. The missing lemma is whether every
   chirality coefficient on the third even generator plus both
   swapped-dot generators has partner rank 10.
6. Mutations, each on a scratch copy, exited 1. Requiring the
   pivot-minor gcd degree to be 1 gave `PASS=16 FAIL=1` on the
   sign-product check. Requiring the ten-generator rank to be 48 gave
   `PASS=16 FAIL=1` on the chirality check. Requiring the even space
   plus both spans to have rank 8 gave `PASS=16 FAIL=1` on the
   membership check. An independent generator closure, recomputed in
   this session, gave 24 rotations, all of determinant 1, alphabet
   orbit 24, with `(2, 1, 3)` and `(1, 2, -3)` outside the orbit. This
   runner repeats that closure.
7. One primary runner. No packet helper.
8. Four markdown links. The runner link points at the primary runner.
   One note link points at the minimal axioms on origin/main. Two point
   at the cycle-39 even-span note and the cycle-32 ratio-span note on
   this branch. Manifest node_count 6921 and edge_count 15575. The new
   node has out_degree 3 and deps_hash `8817e2ad5d19`. Dependencies are
   `minimal_axioms`, the cycle-39 even-span note, and the cycle-32
   ratio-span note. `citation_graph.json` was deleted.
9. Machine-status fields match this certificate. The imports paragraph
   names the even space and the two spans, and states that the
   order-blind converse is not applied and that no rate is imported.
10. No audit status, effective status, or ledger output is written.
11. Counts recomputed in this session: `PASS=17 FAIL=0`, pivot-minor
    gcd degree 0, base rank 10, and partner rank 10 at every chirality
    coefficient on every ordered height pair.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the note.
    The loop-pack directory is skipped by that lint. The full audit
    pipeline was not run.

## 2026-10-11 author check, cycle 53

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms on origin/main at the base `0b208e91cfc`, the
   cycle-39 even-span note, and the cycle-32 ratio-span note, both
   notes on this branch. The pivot-minor gcd is computed in this
   runner. The order-blind converse is not applied. The even space is
   named in cycle 39. The two spans are named in cycle 32. The
   dimension count of the soldered bond space is not repeated.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/chiral_pair_third_even_dot_partner_kernel_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `a9c3b633bf1afb02a1425820a481ceccb89ee099b69f62c7d9fc752813d61c62`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=18 FAIL=0`.
   Elapsed 47.38 seconds.
3. Scope. The third even-dot family is the third even generator plus
   both swapped-dot generators, on every ordered height pair. On the
   source-same pairs the summed kernel vector has swapped coordinate
   `-5/2` and orthogonal coordinate `3`. On `(1, 3)`, `(2, 3)`, and
   `(3, 2)` it has swapped coordinate `-2`, parallel coordinate `1`,
   oblique coordinate `1`, and orthogonal coordinate `2`. The base
   image has rank 10. The coefficient pairs compress to 17 rows. The
   pivot minors at chirality coefficients `0`, `1`, `-1`, `-1/2`, and
   `5/2` have a nonzero constant gcd, so every chirality coefficient
   has partner rank 10. A sum of two even generators is outside this
   count. The ten-kernel coefficient span is not classified. The full
   soldered bond space is not classified. Status line
   `proposed_retained`. Surface status `bounded-support`.
4. N-gate does not apply. The artifact shows that one family has
   partner rank 10 at every chirality coefficient. It does not claim
   that a sum of two even generators has partner rank 10.
5. Obligations are in the note. The missing lemma is whether every
   chirality coefficient on the sum of the second and third even
   generators plus both swapped-dot generators has partner rank 10.
6. Mutations, each on a scratch copy, exited 1. Requiring the
   pivot-minor gcd degree to be 1 gave `PASS=17 FAIL=1` on the third
   even-dot check. Requiring the ten-generator rank to be 48 gave
   `PASS=17 FAIL=1` on the chirality check. Requiring the even space
   plus both spans to have rank 8 gave `PASS=17 FAIL=1` on the
   membership check. An independent generator closure, recomputed in
   this session, gave 24 rotations, all of determinant 1, alphabet
   orbit 24, with `(2, 1, 3)` and `(1, 2, -3)` outside the orbit. This
   runner repeats that closure.
7. One primary runner. No packet helper.
8. Four markdown links. The runner link points at the primary runner.
   One note link points at the minimal axioms on origin/main. Two point
   at the cycle-39 even-span note and the cycle-32 ratio-span note on
   this branch. Manifest node_count 6922 and edge_count 15578. The new
   node has out_degree 3 and deps_hash `8817e2ad5d19`. Dependencies are
   `minimal_axioms`, the cycle-39 even-span note, and the cycle-32
   ratio-span note. `citation_graph.json` was deleted.
9. Machine-status fields match this certificate. The imports paragraph
   names the even space and the two spans, and states that the
   order-blind converse is not applied and that no rate is imported.
10. No audit status, effective status, or ledger output is written.
11. Counts recomputed in this session: `PASS=18 FAIL=0`, pivot-minor
    gcd degree 0, base rank 10, and partner rank 10 at every chirality
    coefficient on every ordered height pair.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the note.
    The loop-pack directory is skipped by that lint. The full audit
    pipeline was not run.

## 2026-10-11 author check, cycle 54

Author checks only. No review-loop PASS and no audit verdict.

Conformance, section by section:

1. Self-containment. The note and runner are in this delta. The parents
   are the minimal axioms on origin/main at the base `0b208e91cfc`, the
   cycle-39 even-span note, and the cycle-32 ratio-span note, both
   notes on this branch. The pivot-minor gcd is computed in this
   runner. The order-blind converse is not applied. The even space is
   named in cycle 39. The two spans are named in cycle 32. The
   dimension count of the soldered bond space is not repeated.
2. Cache. `AUDIT_TIMEOUT_SEC = 180`. The envelope wrote
   `logs/runner-cache/chiral_pair_second_third_even_dot_partner_kernel_2026_10_10.txt`.
   Header `timeout_sec: 180`, `status: ok`, sha256
   `982e0545dd44abf503951debefdd7294136740408363800fc008d001497a2057`,
   matching `shasum -a 256` of the runner. `TOTAL: PASS=19 FAIL=0`.
   Elapsed 49.82 seconds.
3. Scope. The second-plus-third even-dot sum is the second even
   generator plus the third even generator plus both swapped-dot
   generators, on every ordered height pair. On the source-same pairs
   the summed kernel vector has swapped coordinate `-5/2`, parallel
   coordinate `-1`, oblique coordinate `1`, and orthogonal coordinate
   `3`. On `(1, 3)`, `(2, 3)`, and `(3, 2)` it has swapped coordinate
   `-1`, parallel coordinate `1`, oblique coordinate `1`, and
   orthogonal coordinate `2`. The base image has rank 10. The
   coefficient pairs compress to 17 rows. The pivot minors at chirality
   coefficients `0`, `1`, `-1`, `-1/2`, and `5/2` have a nonzero
   constant gcd, so every chirality coefficient has partner rank 10.
   The sum of the first and second even generators is outside this
   count. The ten-kernel coefficient span is not classified. The full
   soldered bond space is not classified. Status line
   `proposed_retained`. Surface status `bounded-support`.
4. N-gate does not apply. The artifact shows that one sum has partner
   rank 10 at every chirality coefficient. It does not claim that the
   sum of the first and second even generators has partner rank 10.
5. Obligations are in the note. The missing lemma is whether every
   chirality coefficient on the sum of the first and second even
   generators plus both swapped-dot generators has partner rank 10.
6. Mutations, each on a scratch copy, exited 1. Requiring the
   pivot-minor gcd degree to be 1 gave `PASS=18 FAIL=1` on the
   second-plus-third check. Requiring the ten-generator rank to be 48
   gave `PASS=18 FAIL=1` on the chirality check. Requiring the even
   space plus both spans to have rank 8 gave `PASS=18 FAIL=1` on the
   membership check. An independent generator closure, recomputed in
   this session, gave 24 rotations, all of determinant 1, alphabet
   orbit 24, with `(2, 1, 3)` and `(1, 2, -3)` outside the orbit. This
   runner repeats that closure.
7. One primary runner. No packet helper.
8. Four markdown links. The runner link points at the primary runner.
   One note link points at the minimal axioms on origin/main. Two point
   at the cycle-39 even-span note and the cycle-32 ratio-span note on
   this branch. Manifest node_count 6923 and edge_count 15581. The new
   node has out_degree 3 and deps_hash `8817e2ad5d19`. Dependencies are
   `minimal_axioms`, the cycle-39 even-span note, and the cycle-32
   ratio-span note. `citation_graph.json` was deleted.
9. Machine-status fields match this certificate. The imports paragraph
   names the even space and the two spans, and states that the
   order-blind converse is not applied and that no rate is imported.
10. No audit status, effective status, or ledger output is written.
11. Counts recomputed in this session: `PASS=19 FAIL=0`, pivot-minor
    gcd degree 0, base rank 10, and partner rank 10 at every chirality
    coefficient on every ordered height pair.
12. `scripts/vocab_lint.py --fix` reported 0 violations on the note.
    The loop-pack directory is skipped by that lint. The full audit
    pipeline was not run.
