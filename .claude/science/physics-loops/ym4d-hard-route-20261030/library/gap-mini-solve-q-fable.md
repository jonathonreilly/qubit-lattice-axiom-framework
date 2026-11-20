lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T16:39Z

# Row 1224 `gap-mini-solve-q-fable`: plain brief "prove that 4D SU(2) Yang-Mills has a mass gap (Jaffe-Witten)"

Provenance: queued for Claude Fable 5.2 max; the Mac mini account hit its Fable weekly limit at about 04:05Z, so per the
lead note of 2026-11-20 04:12Z this row runs on Claude Opus 5.5 (max reasoning) from its start. No Fable text existed in
this file at pin 4260d44bd (file absent). Branch claude/ym4d-hard-route, pin 4260d44bd. No commit, no push (relay copies).

Labels: PROVED, ARGUED, GUIDE, OPEN as the brief asks. A numeric run is never a proof step.

## Status log

- 2026-11-20T04:39Z started (date -u); file created as the first write of this run.
- 2026-11-20T04:41Z Section 1 written (sources read: FINISH rule sections L52-73, L299-350; GOAL.md; parts/gap.md L1-104;
  library/prior/gap-onebound-read-sol.md in full; RESULT lines of rows 1204, 1211, 1215, 1218, 1220).

## 1. What the target is, and where the lane stands (read, not re-derived)

The target is the Jaffe-Witten clause for SU(2): a quantum Yang-Mills theory on R^4 (Osterwalder-Schrader axioms)
whose Hamiltonian H satisfies spec(H) in {0} union [m, infinity) with m > 0. This lane takes existence (T0) from the
hard-core lane and works on the gap clause only. Its present reduction (cited, not re-derived here):

- Consumer. Row 1161 (`gap-solve9-astra62.md` L146-148): the gap clause follows from the one-cube neutral bound
  (N-phys) alone; the charged half is branch selection (BS), and row 1179 wrote a bypass for it.
- (N-phys) in explicit form (row 1218 reading, from row 1161 and row 1179 L304-310): there are a physical side L and
  a cutoff index j_0 such that for every j >= j_0 some integer u_j with 3 <= u_j <= n_j/K has
  s_{+,j}(u_j; n_j^3) = Tr_{H_+} U_j^{u_j} - 1 <= 1/2 (U_j the vacuum-normalised periodic spatial-cube transfer,
  H_+ its centre-neutral sector, n_j = L/a_j). It is a TRACE (all neutral levels with multiplicity).
- Row 1184: (N-phys) is the crux lemma (GLUE-FP)_sigma of rows 895 and 920 with other constants.
- Row 1218 (gpt-6.1-sol reading, unchecked): published work on the same target. A = Bhattacharjee, Bhattacharya,
  Lockwood, Romanov, Sessford, Singha Roy, "One Bound at One Scale" (Preprints.org 202611.1282 v1; authors' Zenodo
  copy read): a full-thermal one-scale seed (A-B*) / (A-B**) Z(s,T_0)^2 <= e^{gamma V(s)} Z(s, 2 T_0) on the shape
  window 2T_0 <= s_i < 48 T_0, gamma = y_0/(2 (96 T_0)^3), y_0 <= 1/20, with a proved conditional ascent (Theorem
  7.56) to a full periodic transfer gap. It is STRONGER than (N-phys). B = the same group's "One Cube Estimate
  Implies the Yang-Mills Mass Gap" (Hexagon 2610.00341v7): cube heat-bath criteria BP(n, varpi), different in kind,
  and a real but restricted weak-coupling theorem (Corollary 166, straight-path block law). C = Zeng Chunping,
  Hexagon 2611.00492 and 2611.00543: a common all-channel rate (C-MG) and a conditional tunneling package.
  None proves the lane's open Wilson estimate at weak coupling.
- Row 1220 (Opus 5.5, unchecked): B's Corollary 166 is the near-Haar property of long straight transports and holds
  for massless Villain U(1) too (Proposition U), so it is not selective; at a near-Haar step B's split inequality
  contains the finer-level Poincare inequality (Lemma NULL).
- Rows 1204, 1211, 1215 (gpt-6.2-astra, chain): each ends OPEN at the strict infrared estimate on the weak-coupling
  trajectory (Q of row 1204; the strict infrared bound of row 1211; the matched continuum construction of row 1215).

So every route on file ends at ONE kind of statement: an estimate at one physical scale, uniform in the cutoff, along
the weak-coupling trajectory, that fails for massless comparison models (free photon, Villain U(1) at weak coupling).
