lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T21:35Z

# gap-mini-solve-ad-opus (queue row 1251): four-dimensional SU(2) Yang-Mills mass gap, plain brief

Provenance: Claude Opus 5.5 (max reasoning), Mac mini worker 1, pinned at commit 6abdb75f2 on branch
`claude/ym4d-hard-route`. Started 2026-11-20T09:35Z (date -u). Labels: PROVED, ARGUED, GUIDE, OPEN, per the row.

## 0. Status log

- 09:35Z: file created (save protocol). Reading GOAL.md, the newest RESULT lines, `library/prior/gap-onebound-read-sol.md`.
- 09:52Z (date -u): reading done (GOAL.md; FINISH.md Joining, Working efficiently, Rules; row 1251 in full; RESULT lines of rows
  1222-1250; `parts/gap.md` L1-104; `library/prior/gap-onebound-read-sol.md` in full; row 1180 Steps 1-2; row 700
  Section 6; row 1244 (sibling, running) Step 1). Section 1 written.

## 1. How best to attack it (judgement; ARGUED; every input cited)

**1.1 What a proof must contain (cited, not new).** Beside the existence chain T0, the gap clause of this lane reads
one lattice estimate, (N-phys) (row 1161 L146-148; restated in row 1180 Step 1, `gap-mini-neutral-fable.md` L44-48).
Row 1180 2.1 (L95-114) splits it into (a) a finite neutral seed at every fine coupling and (b) seed size O(1/a_j).
Row 1233 (`gap-mini-solve-u-opus.md` Proposition 3.7) pays (b) through the account's summable two-cutoff increments,
given the account's premises; row 1234 (`gap-mini-solve-v-opus.md`, check row 1250 HOLDS) shows (b) is a genuine
extra input in the comparison class. So, modulo the account, the infrared input is (a) at one coupling where the
running coupling is of order one: a seed for Wilson SU(2) at one coupling in the window beta = 2.3 to 2.6 (row 998
L133-136).

**1.2 Why every known kind of proof stops there (cited).**
- (K-one), a property with a number at one coupling in the band: the hand-proved edge is beta_std about 0.18
  (character ratio u = I_2/I_1 about 0.045; row 1229), against u = 0.48 to 0.52 in the band; A's own fixed-spacing
  results stop at beta_W <= 7/20 (row 1218 L116). GOAL.md forbids a computed certificate.
- (K-flow), a selective step carried through the band: needs an exact identity with a non-abelian sign at
  order-one response; none is on file (row 1243 Step 2.2; lead rule W2, `parts/gap.md` L97).
- A 4D port of the posted 2D O(N) proofs: no rigid non-abelian group acts on the integrated variables (Lemma CEN+,
  row 1016); boundary twists squeeze under tiling (row 1228); the neutral half needs association (row 1241).
- Published 4D proposals (row 1218): A's thermal seed (A-B*) is the lane's full periodic seed; B's cube criteria are
  open along the tuning, and B's weak-coupling Corollary 166 is the near-Haar property of long transports (row 1220,
  Lemma NULL); A's slab hypothesis (M) fails at beta 3-6 in GUIDE runs (row 1224).

**1.3 The one published weak-coupling mechanism not yet tested.** Zeng Chunping's Part II (Hexagon 2611.00543v1,
read by row 1218 L218-242 only; credited to its author) proposes a mechanism aimed at beta_N -> infinity: a
tunnelling package (COH), (TUN), (SPEC) from which Proposition 13.4 asserts an Eyring-Kramers law
rho_latt = Lambda exp(-c_K kappa_N B_*)(1 + O(kappa_N^(-1/2))) for a Dirichlet-form Poincare constant, and Theorem
14.1 adds (SPEC) and asserts the uniform transfer gap (C-MG2'') and the continuum gap. On file about it: row 1218
(reading; "constructs no Wilson TUN certificate"), row 1220 (SPEC fails as an identity at beta = 0), row 1234 ("TUN
must be read on a slice"; no claim made). Grep at this pin: no file tests (TUN) or (COH) against the Wilson action
(the lane's own (TUN) of rows 1158 and 1189 is a different statement: an overlap bound, `gap-paths-fable.md` L226).

**1.4 Choice for this row.** Rule 0 asks what changes. Zeng's package is the only published claim of a 4D
weak-coupling mechanism of (K-flow) kind (a selective step: tunnelling between two classical vacua, absent for the
free photon). Deciding whether (COH), (TUN), (SPEC) can hold for Wilson SU(2) either gives the lane a mechanism to
port (if they can) or closes the last published candidate (if they cannot). The question is decidable from the text
and the Wilson action. So this row: (i) reads Zeng's Part II definitions and the proof of Proposition 13.4 and
Theorem 14.1; (ii) tests each hypothesis against the Wilson action, by hand, with a PROVED verdict where possible;
(iii) runs a short GUIDE test only if a constant must be seen. Not attempted here: a new route to (N-phys); the
sibling rows 1244, 1248, 1249 (running) hold the (K-flow) stiffness questions.

