lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T23:16Z

# gap-mini-solve-ah-opus (FINISH row 1259): plain brief "prove the SU(2) mass gap", run by Opus 5.5 max

Branch claude/ym4d-hard-route, pinned commit c23b8c360. Writer: Claude Opus 5.5 (max), Mac mini worker. Not committed
by the writer; a relay copies the file. Labels: PROVED, ARGUED, GUIDE, OPEN, as the row asks.

## Status log

- 2026-11-20T11:16Z (date -u) file created; reading the row, `parts/gap.md`, row 1218's reading `library/prior/gap-onebound-read-sol.md`
  and the newest chain rows next.
- 2026-11-20T11:51Z (date -u) Step 1 written (reading, screen, choice).

## Step 1. How best to attack it (judgement; ARGUED where not cited)

**Read for this choice.** GOAL.md; FINISH.md L1-90 and L299-350 (rules); queue row 1259 in full; the RESULT parts of rows
1216-1258; `parts/gap.md` L1-104 (state, methods 19-36, lead rules); `library/prior/gap-onebound-read-sol.md` L25-125,
L255-272 (row 1218); `library/gap-mini-solve-ag-opus.md` L11-60, L228-300, L342-381 (row 1258, (SL), (RR)); the plan of
the running sibling row 1256 (`gap-mini-solve-af-opus.md` L11-66: it works on (EDGE)); `library/gap-seed-limit.md`
L196-245 (row 700: Propositions N1, N2, Corollary N3, (NS-gap)); `library/gap-phys-seed.md` L253-330 (row 720: Lemma Z,
Z', Z3, Theorem ZD, Corollaries Z1-Z4, Theorem ZD-c); `library/gap-crux-restate.md` L50-90 (C1-C5);
`library/gap-mini-solve-q-fable.md` L125-200, L252-272 (row 1224: A's hypothesis (M) and A's checked Section 11);
`library/gap-univk-opus.md` L341-398 (row 924: (DENS-K), B1-B3); the open-input lists of rows 1241 (L148-166) and 1255.
Branch tip at 8af5d34eb (scratch bare fetch, read-only): sibling files af and ag only; ai, aj not started.

**What the record fixes (cited, not re-derived; pointers, not evidence).**
- Beside the account's premises, the Jaffe-Witten gap on the account's tr F^2 sector reads one lattice estimate, (N-phys)
  (row 1161 L146-148; row 1179; row 1225 Theorem E-N, check 1232 HOLDS AFTER CORRECTION).
- At one coupling the seed is EXACTLY a gap inequality with a count term: Theorem ZD (C) of row 720
  (`gap-phys-seed.md` L296-310): there is b with b m(b^3) >= 256 D(b/4) + 29.64, D the Casimir free energy of the
  symmetric torus. Corollary Z2 (L312-317): a uniform gap plus liminf D(a)/a < m_0/64 gives the seed. So "seed =
  lattice gap" (rows 1225, 1233, 1238; FAILED as a deduction in check 1242) is true exactly modulo the count, and the
  count is (NS-gap) of row 700 (L234), open since rows 697/720 and never attacked.
- Every one-scale form on file asks for the same thing at the band (an order-one effective coupling): C1 seed, C3 (W),
  (SL)/(RR) (row 1258), A's (M) (row 1224, A's Definition 11.3), B's cube Poincare (row 1254 (1)). Hopf/Birkhoff
  contraction of the slab kernel is on file with its extensive diameter (`gap-crux-skeleton-max.md` L202, L373;
  `gap-fr-opus.md` L99; `gap-short-step-max.md` L482).

**My own screen this run (each grepped in `library/`, `library/prior/`, `parts/gap.md` before any work; counts are
files naming the tool).** Every idea is on file or dies at a stated step.

| Idea | Registry | Where it stops |
|---|---|---|
| Count from the gap: bound D(a) by the thermal sum at a shorter time (Proposition Delta, RP doubling f(2T) <= f(T)) | Prop. Delta row 708, Lemma Z row 720 | it IS Lemma Z / Corollary Z2; the sublinear bound on D is the open (NS-gap) |
| Count by recursion into prisms and slabs (D = sum of thermal densities with 1-4 short sides) | new as a form; ARGUED here | each density is a count per unit volume; a gap on prisms adds only an additive -t m, not a factor |
| Counterexample to (NS-gap) in the class (uniform gap, linear D) | row 720 L319 "I do not know a model" | subsystem and fracton models give linear D but their gap closes (degenerate sectors); none found |
| Birkhoff self-improvement of (RR): tanh(eta_*/4) submultiplicative, constant threshold | Birkhoff 19 files, Hopf L202 | a corollary of Hopf's theorem; the diameter stays extensive (`gap-mini-free-fable.md` L379) |
| Dobrushin contraction through slices: tau(s1+s2) <= tau(s1) tau(s2) | standard | true, but a whole-slice TV is near 1 until s ~ xi log abs(B): the same log |
| A's (M) at one coupling gives the seed | A Prop. 7.19 (product of rings) | false in general; maximal correlation misses the count (A's own example) |
| Seed gives B's/A's cube Poincare (static to dynamic) | row 1218 item 2 | needs worst-case mixing; B leaves the converse open |
| Higgs complementarity path kappa: infinity -> 0 at fixed beta | Fradkin 26, Osterwalder-Seiler 41 | the crossover W mass ~ Lambda is the band in the kappa direction |
| Lieb-Mattis ordering of sector ground levels | 0 files | no sign rule: the SU(2) character expansion has negative terms (crosscap, rows 737, 744) |
| Weinberg-Witten | 0 files | forbids only massless helicity > 1 with a covariant stress tensor; spin 0, 1 glueballs allowed |

Verdict (ARGUED): no engine for the band off the record, as in rows 1219-1258.

**Choice for this row.** Rule 0: the item must move a named open input. The infrared crux has no engine, and the
rules (FINISH L301) give Opus the ports and routine steps. Three inputs of the one-cutoff carry (row 1233 Proposition
3.7, as corrected by check 1242 and rows 1241, 1255) are unattacked and look like ports, not new mathematics: (DET)'s
structural inputs (S1)-(S3) (`gap-det-fable.md` L71-77, L290-316), the existence of the inverses at U = 1 ("pr-lay W",
`pr-lay.md` W, used at U = 1 by `gap-det-fable.md` L403), and 8.22's standing hypotheses. The running sibling row 1256
works on (EDGE); check row 1263 reads row 1255's (R). Next step: decide which of these the repository's CHECKED hard-core
work already supplies (FINISH L14: the flat package from Balaban CMP 89, 95, 96 was checked line by line, row 95), and
port it. If none is a port, I return to the count (NS-gap) and record its exact first failing step.
