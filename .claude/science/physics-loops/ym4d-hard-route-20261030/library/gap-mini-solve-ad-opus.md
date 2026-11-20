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

## 2. Zeng's tunnelling package against the Wilson action (READ, ARGUED; written 09:58Z by date -u)

**2.0 Source.** Zeng Chunping, "From Four-Dimensional Wilson Lattice Gauge Theory to Quantum Yang-Mills Theory,
with a Conditional Mass-Gap Theorem", Hexagon 2611.00543v1 (17 November 2026), 57 pp., PDF fetched from
hexagonmath.org into a scratch folder outside the repository (not committed). Read in full: Part II, Sections 11-14,
pp. 45-50, and Appendix B.1, pp. 53-57 (Lemmas B.1-B.8, Proposition B.10, Corollary B.11, Remarks B.12-B.15).
Credit for everything quoted in this section: Zeng Chunping.

**2.1 What the package is (READ, with page).**
- Objects (p. 46): mu_p is "the Wilson measure on the time-slice configuration space", E_p "its Dirichlet form",
  rho_latt(p) the Poincare constant (11.3). The schedule is beta_N = beta_bar + 2 b_0 log(1/a_N) with b_0 = 22/(48 pi^2)
  (so beta_N = 1/g_N^2 at one loop), and kappa_N = beta_N kappa_*, kappa_* := 1/(2 b_0 c_K B_*) (11.1). Then
  exp(-c_K kappa_N B_*) = A a_N with A = exp(-beta_bar/(2 b_0)) (11.2). This is a definition of kappa_*, not a
  derived fact: kappa_* is chosen so that the barrier of (TUN) below produces exactly one power of a_N.
- (TUN) (pp. 46-47): two wells U^+-, a path gamma_p between them, and a foliation (s, y) in S^1 x Y_p of a
  neighbourhood of gamma_p with S(gamma_p(s, y)) = kappa_N Phi_p(s) + Psi_p(s, y); Phi_p has two nondegenerate
  minima (value 0) and two saddles, barrier Delta_p = c_K B_*, Morse curvatures uniformly bounded above and below;
  Psi_p and four y-derivatives bounded; Jacobian bi-Lipschitz. So along gamma_p the action barrier is
  beta_N/(2 b_0) + O(1): TUN asks the Wilson action to carry the one-loop number 1/(2 b_0) as a classical barrier.
- (SPEC) (p. 47) and Lemma B.1 (pp. 53-54): with E_p := E^tm_p(f, f) = <f, H_p f> (H_p = -log T_p on L^2(mu_p)),
  rho^tm_latt = -log(lambda_2/lambda_1) is a tautology. Zeng's own words (p. 54): "The substantive content of (SPEC) is
  then the identification of this temporal Dirichlet form with the spatial-bond Dirichlet form to which the
  semiclassical computation of Section 13 applies; that identification is part of the spectral side of the gap and
  is not proved here." This agrees with row 1220 (SPEC fails as an identity for the spatial form at beta = 0).
- (COH): Proposition B.10 proves only one-bond clauses (Lemmas B.2-B.8, defining representation); "the remaining
  clause of (COH) reduces to the design bound p >= p_0 > p_c ... and the multi-bond SU(2) transport extension;
  neither is supplied" (p. 56). The constants mu_harm "are numerical, obtained ... on three-dimensional
  bond-percolation resistor networks ... a model-level input ..., not a verbatim certificate for the Wilson
  transport measure" (Remark B.13, p. 56).
- Zeng's own status lines: Remark 11.2 (p. 47) "(TUN) is the spectral side of the mass gap itself"; Remark 14.3
  (p. 50) its construction "is the only step that cannot, even in principle, be certified a priori, since certifying
  it is equivalent to proving the gap"; Remark B.13 "The mass gap remains unproved."

**2.2 The proof of Proposition 13.4 (READ p. 49; ARGUED verdict).** Proposition 13.4 asserts the two-sided law
rho_latt(p) = Lambda(p) exp(-c_K kappa_N B_*)(1 + O(kappa_N^(-1/2))). Theorem 14.1 uses only its lower half. The proof
has three steps: (i) the coarea comparison (13.1) of E_p with the s-derivative form on the tube around gamma_p;
(ii) "conditioned on the transport coordinate s, the y-fibers contribute a gap bounded below by a kappa_N-independent
constant (Lemma 12.1, tensored over blocks with the uniform coherent-block control of (COH)), so the Rayleigh quotient
is minimized by functions of s alone"; (iii) the one-dimensional two-well Muckenhoupt law, Lemma 13.1 (correct as
stated, a Laplace computation). I find two steps that the hypotheses do not carry.
- Step (ii) tensorizes one-bond Poincare constants over blocks that interact. Tensorization holds for product
  measures; for an interacting Gibbs measure the joint constant can be smaller than every conditional one by a
  factor of the system size (any ferromagnetic ring of SU(2) spins at coupling kappa: each one-site conditional law
  is a von Mises-Fisher law with constant at least c min(1, kappa), while the averaged rotation mode
  f = n^(-1) sum_i g(u_i) has Dirichlet form of order 1/n and variance of order one). (TUN) bounds Psi_p and its
  y-derivatives, not the Poincare constants of the fibre measures dnu_s, so nothing in (TUN) or (COH) supplies step (ii).
- (TUN) describes a tube around one loop. The lower half of (13.4) is a statement about all of the configuration
  space Omega_p. A lower bound on a Poincare constant needs every bottleneck of mu_p, not one: a tube statement gives
  an upper bound (a test function in the tube), never a lower one. No hypothesis says that mu_p is carried by the tube.
- With E_p = E^tm_p, step (i) is the unproved identification that Zeng names on p. 54; with E_p the spatial-bond
  (gradient) form, (SPEC) is the unproved identification. Either reading leaves one identification of the size of
  the gap itself.

**2.3 The barrier normalization (ARGUED; one GUIDE remark).** In TUN the classical object S, evaluated at the saddle,
must equal beta_N/(2 b_0) + O(1) with a bounded residual. For a classical action of Wilson type, S = beta_N E(U) with E
independent of g, so the minimax barrier between two fixed wells is beta_N E_bar with E_bar a number fixed by the
geometry; (TUN) then forces E_bar = 1/(2 b_0) = 10.77 exactly in the limit (in the normalization S = beta_N E), a
coincidence between a classical lattice minimax and the one-loop coefficient. GUIDE (continuum values, not a lattice
proof): for tunnelling between topologically distinct vacua the natural barrier is the instanton action 8 pi^2/g^2,
and exp(-8 pi^2/g_N^2) = (a_N Lambda)^(22/3) for SU(2), seven powers of a_N too many; this is why kappa_* must be set
by hand in (11.1). Zeng's Remark B.14 (p. 57) also withdraws the strong-coupling de-conditioning route.

**2.4 Verdict for the lane.** Part II of 2611.00543v1 contains two correct one-dimensional lemmas (Lemma 12.1, the
one-bond fibre reduction; Lemma 13.1, two-well Muckenhoupt asymptotics on S^1) and one-bond (COH) clauses. Its
mechanism step, the passage from a tube around one loop to the Poincare constant of the time-slice Wilson measure,
is not proved, and its hypothesis (TUN), by Zeng's own Remarks 11.2 and 14.3, is equivalent to the gap. So Part II
supplies no (K-flow) step and nothing to port: the last published 4D weak-coupling proposal of row 1218 is closed as a
mechanism. This does not refute Theorem 14.1 as an implication (no counterexample to (COH) + (TUN) => (13.4) for the
Wilson measure is constructed here; the two defects of 2.2 are gaps in its written proof). Novelty check: row 1218
(L218-242) and row 1220 read the package and its SPEC remark; no file on record reads Proposition 13.4's proof or
Lemma B.1 (grep `Lemma B.1`, `13.4`, `tensor` in files naming Zeng returns none of these points).

