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
