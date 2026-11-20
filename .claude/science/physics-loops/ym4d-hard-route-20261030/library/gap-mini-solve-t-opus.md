lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T18:04Z

# gap-mini-solve-t-opus: four-dimensional SU(2) Yang-Mills mass gap

Queue row 1229 of `FINISH.md`. Started 2026-11-20T06:04Z on the Mac mini Claude worker 3, at commit ca359c011 of branch `claude/ym4d-hard-route`.

Labels: PROVED (a complete written argument here or in a cited, checked source), ARGUED (an argument with a named gap), GUIDE (heuristic or numeric), OPEN.

## Step 0. Reading (in progress)

Reading FINISH.md (rules, efficiency, RESULT lines of the gap rows), `parts/gap.md`, `library/prior/gap-onebound-read-sol.md`, `library/open-core.md`.

Sources read (06:04Z-06:40Z): `GOAL.md`; `FINISH.md` L1-84, L299-356 and the RESULT lines of rows 916-917, 924-925,
1007, 1009-1011, 1014, 1016, 1020, 1025, 1029, 1139-1140, 1179-1180, 1183, 1188, 1193, 1200, 1212-1232;
`parts/gap.md` L1-104; `library/prior/gap-onebound-read-sol.md` (row 1218) in full; `library/gap-mini-solve-r-fable.md`
(row 1225) in full.

What the record says (cited, not re-derived):

- The Jaffe-Witten gap clause on the account's tr F^2 sector follows from one open lattice estimate, (N-phys), beside
  the account's premises (row 1179 Theorem BP, check 1183; row 1225 Theorem E-N, same provider, check row 1232 queued).
  (N-phys): one physical side L and j_0 such that for every cutoff j >= j_0 some integer u_j with 3 <= u_j <= n_j/K
  has Tr_{H_+} U_j^{u_j} - 1 <= 1/2 on the periodic spatial cube of side n_j = L/a_j (K = 512).
- (N-phys) holds iff every fine coupling has a finite one-cube seed size nu(beta_j) with limsup a_j nu(beta_j) finite
  (row 1180). Modulo (UNIV-K) the crux is the lattice gap of SU(2) Wilson at one fixed coupling with seed side of
  order exp(c beta_0) (row 1225, ARGUED). (UNIV-K) is open and unowned since row 925; it lives in the account's
  ultraviolet steps (MAPCONV, VAC-ID, DENS-K, CLASS) and needs no infrared input.
- Row 1225's table: every structure valid at all couplings on file stops at a cited failure (positivity and
  association; positive duals; coupling integrals; loop and sector identities; curvature and Gribov geometry; the
  bracket stiffness step of the 2D O(N) proofs).
- The 2D O(N) proofs (rows 1007, 1009, 1010) cross the band by a uniform-in-coupling stiffness iteration whose gain is
  the Lie bracket; in 2D O(4) the bracket gives only the charged half, and the rotation-invariant half comes from
  positivity (row 1193, ARGUED). The 4D port fails at: no global non-abelian twist in a gauge theory (Lemma CEN,
  CEN+, rows 1011, 1016); pin suprema lose colour coherence (Propositions B, B'); the fourth-order commutator cost on
  a 3D slice is too large (Lemma PC, PC-c, rows 1188, 1193); the 4D positivity step fails (rows 1084, 1213).
- Row 1218's published inputs do not shorten the path (rows 1219, 1220).

Step 0 done 06:40Z.
