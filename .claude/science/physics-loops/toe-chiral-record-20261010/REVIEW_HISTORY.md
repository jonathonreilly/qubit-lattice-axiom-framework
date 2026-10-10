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
