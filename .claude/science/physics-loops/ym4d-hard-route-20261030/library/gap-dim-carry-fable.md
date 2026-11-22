lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-23T00:40Z

# gap-dim-carry-fable: the four-dimensional carry (queue row 1390)

Research-stage working state. Nothing here is a public claim. Pinned at commit a1f83f4da on branch
`claude/ym4d-hard-route`. Worker: Claude Fable 5.2 (high), one session, no subagents. Started 2026-11-22T12:40Z (date -u).

## 0. Plan (written first, before reading the inputs in full)

Target of the row: (M-neutral) of row 1367, with the checked chain to the mass gap (rows 1342, 1349, 1356, 1359).
State handed over by the row: every surviving fact separates SU(2) from compact U(1); none separates d = 4 from
d = 5 at the scales of the band. Missing: a carry over the scales of the band that uses d = 4 (requirement (b) of
row 1386, section 4.3).

Steps, each appended to this file as it is done:

1. Read rows 1379 to 1389 and their files; restate (M-neutral), the band, the filter (t1) to (t5), Remark PAIR,
   and requirement (b). Section 1.
2. List candidate carries that use d = 4, run the filter and the five-dimensional test on each, and grep
   `library/open-core.md`, `library/gap-*.md` and the FINISH rows for each before calling it new. Section 2.
3. Attack the surviving candidate: a first exact lemma, proved in full, or a quantified obstruction for a named
   class of carries. Sections 3 onward.
4. End with the next two rows and their decisive outcomes, and the RESULT line.

Status log (times from date -u):

- 2026-11-22T12:40Z file created with the plan; nothing derived yet.
- 13:05Z read: FINISH.md L1-84 and L299-360; GOAL.md; rows 1378 to 1391 in full; RESULT parts of rows 708, 977, 996,
  1025, 1128, 1141, 1332; `gap-mech-direction2-fable.md` in full; `gap-mech-direction-fable.md` L155-300
  (mechanism families M-A to M-F, Remark TAD); `prior/gap-outside-read-opus.md` L479-531 (flow monotones);
  `gap-afield-b-max.md` L180-192 (B10, B11); `gap-outside-box-max.md` L150-158 (I14 to I16). Not read in full:
  the check files of rows 1381, 1384, 1385, 1387, 1389 (RESULT parts only) and `gap-layer-force-cov-fable.md`.

## 1. The target and the hand-over, as read

**Target.** (M-neutral), `gap-seed-astra62.md` L11 (gpt-6.2-astra, row 1367; Lemma M1 and Corollary M2 are Claude
Fable's row 1356, checked by row 1359): one physical side L on the trajectory, n_j = L/a_j, 4 | n_j, beta_0 <=
beta_j <= B_0 log n_j; in the range of P_0 put s_(n,beta)(t) = sum over a >= 1 of (lambda_a/lambda_0)^t; wanted
s_(n_j,beta_j)(2 w_j) <= 4/21 at every late cutoff, w_j = floor(n_j/1024).

**Where the carry sits.** Theorem T of row 1332 (Claude Fable; check 1335): one finite inequality, (A1) the
ultraviolet carry (row 1391 runs in parallel), (A2) the infrared carry: a seed at a window coupling beta_w gives a
seed at every larger coupling at a size at most C exp(c beta), c below about 4.0 (GUIDE), against 3 pi^2/11 = 2.69
at one loop. (A2) is the band. Row 1386 4.1 writes it per doubling as (STEP), with delta > 0.173 against the
one-loop 0.2575.

**Hand-over (rows 1379 to 1389).** Every surviving proved fact separates SU(2) from compact U(1) and none separates
d = 4 from d = 5 at the scales of the band. Remark PAIR (row 1386 4.2, credited there to row 1128): a mechanism
is a local gain that reads the group times a carry that reads the dimension, x(2L) = 2^(d-4) x(L) - g_G; the lane
holds gains and no carry with a sign. Requirement (b) (row 1386 4.3): the carry uses d = 4 through the exact
classical factor over all scales of the band, not through local counts. The filter (row 1386 4.5): (t1) compact
U(1); (t2) SU(2) in d = 5, applied to the step; (t3) SU(3); (t4) the hypothesis fails as beta grows at a fixed
lattice; (t5) not the target renamed: name the method.

**Kind of result of this file (stated first).** I found no carry with a sign that reaches (M-neutral). The file
gives: (i) the list of the exact ways in which d = 4 can enter a statement about the lattice law, each with its
match on file (Section 2); (ii) proofs that close one class that was not on file by name, the grid (metric,
dilation) carries: Lemma CW, Proposition REF, Corollary MKO, Remark NOSIGN (Section 3); (iii) the candidate that
survives the filter best, with what it lacks (Section 4); (iv) the next two rows (Section 5).

## 2. The exact ways d = 4 can enter, each with its match on file

"Exact" means: an identity or an inequality of the lattice model at every coupling. Repo search for this section:
one loop of `grep -l -i -F` over `library/gap-*.md`, `library/prior/gap-*.md`, `parts/gap.md` (counts of
files in brackets); `library/open-core.md` has no line on a carry, on the marginal dimension or on five
dimensions (grep for carry, "d = 4", "five dim", marginal: no hit).

| # | How d = 4 enters | Exact lattice form | On file | Step-level test in d = 5 | Verdict |
|---|---|---|---|---|---|
| D1 | Marginality under coarsening: a block plaquette is 2^2 plaquettes in series in its plane and 2^(d-2) in parallel across it | bond moving and decimation; exact as an inequality for Z only | rows 1025 (Tomboulis's line; Propositions BR, SIGN, Lemma FAC, Identity MOV), 1128 (G1); Migdal-Kadanoff [41], Tomboulis [117] | the factor is 2^(d-4) by construction | no sign on a quotient (row 1025); Section 3 re-derives the inequality by a trace inequality and adds the order of the two operations plane by plane |
| D2 | Conformal weight: the plaquette weight of a diagonal metric, w_(mu nu) = prod over rho not in {mu, nu} of a_rho / (a_mu a_nu), has degree d - 4 | Lemma CW below | anisotropic couplings [111], Karsch [17]; "soft dilation", "dilation move", "anisotropy field", "conformal factor": no hit | degree 1: a dilation is a first-order change of every coupling | new by name; closed in Section 3: in d = 4 a dilation is not a move of the lattice law, and the grid refinements that remain are D1 |
| D3 | Self-duality of 2-forms and of the centre: electric and magnetic flux are both 3-vectors; Z_2 and Villain U(1) gauge theory are self-dual | 't Hooft's twist relations on a symmetric torus; Wegner duality of the Z_2 part of the SO(3) x Z_2 form | twists throughout the lane; Wegner [9]; Kramers [5]; electric-magnetic [9] | the twist relation Z(n_(1d)) = Z(n_(12)) holds in every d; the self-dual form does not | serves the flux half only (rows 1175, 1177, as quoted in row 1380 M-B); the Z_2 part is ordered at the lattice scale in the window. Not a carry |
| D4 | Topology: pi_3(SU(2)) = Z, the twist n_12 = n_34 = 1 has charge 1/2 and a scale-free classical action pi^2 beta | Z_kappa/Z_0 is an exact lattice quotient; its classical value is exact only as beta grows at a fixed lattice | fractional instanton [13], instanton [46], n_12 = n_34 [10 or more], `gap-kappa-order.md`; B10 of row 1005's line (Chern-Simons form) | cost pi^2 beta n: grows | a coupling in a twist scheme: passes (t1) to (t4), reads the flux half, and its carry is (K-flow) renamed (t5) |
| D5 | The logarithmic bubble, sum over x of G(x)^2 | the marginal method of Aizenman and Duminil-Copin needs a current representation with positivity | `prior/gap-lit-marginal.md` (row 885): no gauge transfer; Aizenman [37], random current [12] | no logarithm | no positivity for SU(2) (row 737's negative term); proves triviality-type bounds, the wrong direction |
| D6 | Borderline monotonicity: r^(4-d) times the energy in a ball (Price), the Yang-Mills heat flow (Hamilton; Struwe), t^2 <E(t)> | per configuration the flowed action decreases; under a translation-invariant law that is all it says | B11 of `gap-afield-b-max.md`; I15 of `gap-outside-box-max.md`; `prior/gap-outside-read-opus.md` F1 to F6 | exponent d/2 against 2 (Section 4.1) | exact identity for the flow-scheme beta function (Section 4.1); no monotonicity theorem and no consumer (I15) |

**What the table says.** There are two exact dimension-reading inequalities at every coupling: the bond-moving
bound of D1 and, in the same family, the refinement bound of D2. Both bound a partition function and neither
bounds a quotient. D3 to D6 are identities or schemes: each gives a running coupling whose monotonicity is the
missing carry, not a proof of it.

