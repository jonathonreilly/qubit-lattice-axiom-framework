lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T17:29Z

# gap-mini-solve-r-fable: four-dimensional SU(2) Yang-Mills mass gap (queue row 1225)

Worker: Claude Opus 5.5 at max effort, Mac mini worker 3, started 2026-11-20T05:29Z on branch
`claude/ym4d-hard-route` pinned at bf998a992. The row was queued for Fable 5.2; per the lead note of
2026-11-20 04:12Z it runs on Opus 5.5 max. No Fable text existed in this file at the pinned commit, so
this file starts fresh.

Labels: PROVED (a complete written argument here or in a cited, checked source), ARGUED (an argument
with a named gap), GUIDE (heuristic or numeric orientation, never a proof step), OPEN.

## 0. Status of this file

Step 0 (orientation): done 05:46Z, Section 1. Plan: Section 2. Steps follow below as they finish.

## 1. Orientation (read, not re-derived; 05:29Z-05:46Z)

Sources read: `GOAL.md`; `FINISH.md` sections 1-84, 299-360 and the RESULT lines of rows 916-917, 924-925,
1179-1222; `parts/gap.md` L1-104, L311-330; `library/prior/gap-onebound-read-sol.md` (row 1218) in full;
`library/gap-mini-branch-fable.md` L290-330 (row 1179, (N-phys) and Theorem BP);
`library/gap-solve9-astra62.md` L130-160 (row 1161, the finite-aspect statement and its consumer);
`library/gap-mini-solve-q-fable.md` L31-135 (row 1224, running beside this row on worker 1).

What the record says the gap needs (each item cited, none re-proved here):

- The Jaffe-Witten gap clause follows from ONE open lattice estimate, (N-phys), plus a matched continuum datum
  (row 1179 Theorem BP; check row 1183 "main chain HOLDS AFTER CORRECTION"). (N-phys): there are a physical side L
  and j_0 such that for every cutoff j >= j_0 some integer u_j with 3 <= u_j <= n_j/K has
  s_{+,j}(u_j; n_j^3) = Tr_{H_+} U_j^{u_j} - 1 <= 1/2, with K = 512 explicit (check row 1187, item (3): "row 1161
  already gives K = 512").
- (N-phys) holds iff every fine coupling beta_j has a finite one-cube seed size nu(beta_j) and
  limsup_j a_j nu(beta_j) < infinity (row 1180, checked HOLDS in row 1187). So (N-phys) is a uniform lattice gap
  for centre-neutral states at arbitrarily weak coupling plus a lower bound of asymptotic-scaling type.
- The continuum datum: rows 916-917 prove and check, given the account's premises, the passage from the seed
  (SEED-FP) to the gap on the tr F^2 sector (Lemma C, Theorem E, Proposition P'). Row 1219 reads this as covering
  (N-phys); the lead note there asks for that reading to be confirmed before it is relied on.
- The alternative (ONE-K) (row 916, checked 917): a seed at one cutoff's window suffices, given the
  cutoff-universality hypothesis (UNIV-K), which stays OPEN (rows 924-925).
- Published work of the same group (row 1218): A's (A-B*) is stronger than (N-phys); B's BP is different in kind;
  B's weak-coupling Corollary 166 is not selective (row 1220 Proposition U); C's rate is row 1204's Q. Row 1224
  (worker 1, now running) checks A's slab route (A-M) and runs a kill test of A's hypothesis in 4D. I do not repeat it.
- Seventeen plain-brief rows (1188-1224) screened candidate mechanisms against the record; every candidate was on file
  with a first failing step. Row 998 9.5 lists "another fresh-framing exercise by this model family" under
  "What not to do next". So this row does not screen again.

## 2. How to attack it (judgement, ARGUED)

The crux is (N-phys): a one-scale, cutoff-uniform estimate deep in the infrared (row 1181 GUIDE: at K = 512 the
premise sits near 1.1e4 correlation lengths). Every method on file is blind (it also holds for a massless comparison
model) or is not uniform in the cutoff. I see no route to a proof of (N-phys) in this session, and I say so now.

So I choose bounded work with a named consumer, in this order:

- Step A (consumer side, short): settle the lead's open note on row 1219. Does the checked chain of rows 916-917 take
  (N-phys) as its input, or does it need (SEED-FP) in a form that (N-phys) does not give? Moves: the exact statement
  of what is open for the gap clause. If it fails, the lead learns that the crux is (N-phys) plus a named bridge.
- Step B (producer side, the crux): one attack on (N-phys), not a screening. Chosen in Step B's own section after
  Step A, with its kind ((K-one) or (K-flow), lane rule W2) and the 4D or gauge-specific input it uses named first.

Status: Step A in progress (05:46Z).
