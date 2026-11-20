lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T19:59Z

# gap-mini-solve-x-opus: the mass gap for four-dimensional SU(2) Yang-Mills

Queue row 1238 of `FINISH.md`. Worker: Claude Opus 5.5, max effort, Mac mini worker 2, at branch
`claude/ym4d-hard-route` commit 6150ee2a3. Started 2026-11-20T07:59Z (date -u).

Labels: PROVED (complete written argument here or cited with its proof on file), ARGUED (argument
given, a step not fully written), GUIDE (heuristic or numeric orientation only), OPEN.

## Step 0. Reading log (reading only; no new claim)

Read at this pin: GOAL.md; FINISH.md L1-90 and L299-356 (rules, joining, efficiency) and the RESULT lines of rows
1218-1239; `parts/gap.md` L1-104 (state of attack, routes 1-36, lead rules); `library/prior/gap-onebound-read-sol.md`
(row 1218) in full; `library/gap-mini-solve-r-fable.md` Sections 1-4 (row 1225: Lemma A0, Theorem E-N);
`library/gap-mini-solve-t-opus.md` Steps 1.3-3 (row 1229); `library/gap-mini-solve-w-opus.md` Steps 0-1 and its
RESULT (row 1237); `library/gap-mini-solve-u-opus.md` (row 1233, as it stands at this pin: chapter 9 of the
complete account against (UNIV-K)); the statement table of `library/gap-univk-opus.md` (row 924, L430-466).

Where the problem stands on file (cited, not re-derived):

- Beside the account's premises (the T0 chain), the Jaffe-Witten gap clause on the account's tr F^2 sector follows
  from one lattice estimate, (N-phys) (row 1225 Theorem E-N; cross-provider check row 1232 HOLDS AFTER CORRECTION).
- (N-phys) holds iff every fine coupling has a finite one-cube seed size nu(beta_j) with limsup a_j nu(beta_j) finite
  (row 1180, checked 1187). Given (UNIV-K), a seed at one cutoff's window suffices (row 916 (ONE-K), checked 917).
- (UNIV-K) is OPEN in (MAPCONV), (VAC-ID), (DENS-K) B1-B2 (row 924); (CLASS) closed in corrected form and two clauses
  of (MAPCONV) by row 1237; row 1233 (running in parallel on worker 3) reads the account's chapter 9 for it.
- The infrared seed has no route: every structure valid at every coupling on file (twist stiffness, positivity,
  curvature, dilute defect duality, exact recursion, compactness) has a cited failing step (rows 1225, 1229, 1237
  tables; screening tables of rows 1189, 1194, 1199). Row 998 9.5 lists another fresh screening by this model family
  as waste.

Rule 0a: `library/open-core.md` has no gap-lane item (row 1237 Step 0 grep, repeated here for "N-phys", "neutral",
"seed": no hit outside hard-core rows). Gap rows 1161-1239 are the FINISH matches.

## Step 1. How best to attack it (judgement, ARGUED; written 08:15Z by date -u)

**1.1 The two open inputs of the gap path (cited).** Beside the T0 chain, the gap clause needs (N-phys). By row 916
(ONE-K) (checked 917), (N-phys) follows from a seed at ONE cutoff's window plus the ultraviolet carry (UNIV-K). So a
proof needs (A) the carry (UNIV-K) and (B) one infrared estimate at one fixed coupling, a lattice gap of Wilson SU(2)
with a finite seed (rows 1225, 1229, 1237 Step 1.1).

**1.2 Part (B), the seed.** I tried, before reading further, to name a band-crossing engine of a kind not in the
tables of rows 1229 (Step 1.2), 1237 (Step 1.2) and the screening tables of rows 1189, 1194, 1199. Each candidate I
could name maps to a row on file:

| Candidate | Where on file |
|---|---|
| level derivative of the seed size in beta (a K-flow bound d log nu/d beta <= C, consistent with asymptotic scaling) | (VIR), rows 708-711, 895, 934, 1128: needs kappa about 7 on the band |
| remnant global colour symmetry of a complete gauge (Landau, Coulomb, tree) as the rigid group of the 2D stiffness engine | frames, rows 1041, 1045, 1141; typical-field frame repair reads first-passage data (rows 1013, 1016 7.4) |
| confinement (string tension) implies the neutral gap | not true blind: a decoupled massless neutral factor keeps the area law; product tests of Lemma PT, Proposition NP |
| Schwinger-Dyson (loop) equations, whose splitting terms are the non-abelian part | master-loop contractions work at strong coupling only (Chatterjee; Basu-Ganguly; row 1199 table, random surfaces) |
| electric-basis (spin network) energy counting, glueball as closed flux | strong coupling only; at weak coupling the basis is not diagonal (rows 1132, 1215) |
| a positive dual for the heat-kernel action | crosscap and 6j signs (method 35, rows 737, 744, 878) |
| finite subgroup 2I at the window | frozen-group comparison cases (rows 884, 998); not frozen at beta 2.3-2.6 |

So I do not claim an attack on (B), and I do not screen further (row 998 9.5).

**1.3 Decision: part (A), sub-item (MAPCONV-F).** Row 1237 Step 3 closed (CLASS) in a corrected form and the
transport, norm and b clauses of (MAPCONV), with one ARGUED step (Lemma 3.2: the classical field map B_xi of
(hit:actual-transferred-pointing) does not read the depth below the old scale). It left

    (MAPCONV-F) on the common domain, sup abs(r^A_j - r^B_j) + ||n^A_j - n^B_j|| + sup ||f^A_j - f^B_j|| <= C lambda_0^j,

"Not attacked further here". Rule 0a (grep at 08:16Z): open-core.md has no match; the only FINISH or QUEUE_DONE row
whose text names MAPCONV is 924; library files naming it are rows 924, 925 (check), 934 (in passing), 1225, 1229,
1233, 1237. None attacks (MAPCONV-F). Row 1233 (running) asks a different question, whether the complete account's
chapter 9 supplies (UNIV-K) as a whole. If it does, this step becomes moot, and I say so in the result.

Moves: (UNIV-K), the carry, which is needed even when a seed exists, because a structural seed bound is not expected
to be sharp (the 2D O(3) proof needs its RG carry for the same reason, row 1010). Success: the regular part of
(UNIV-K) is closed given endpoint matching. Failure: the exact missing account statement, by name and line.

Plan: (1a) fetch YM4_1400.tex at 2bc0658f91d2 into a new scratch folder; (1b) trace B_xi (the ARGUED step of row 1237
Lemma 3.2); (1c) read the definitions of r_j, n_j, f_j and find what each reads of the depth and the frame;
(1d) prove (MAPCONV-F) clause by clause or name the first clause that needs an estimate the account does not make.

## Step 2. (MAPCONV-F): what the account proves about depth, and what it does not (READ; written 08:22Z by date -u)

Source: YM4_1400.tex of the Sussman-Alpoge repository (Ethan Sussman and Levent Alpoge, with Claude and Codex as
authors of their text), fetched by URL at commit 2bc0658f91d2 into a new scratch folder; 136637 lines, the numbering of
rows 924 and 1237. "L n" is line n. Lines READ: 94030-94135 (fixed presentation, frame, recursion, derivative bounds),
93420-93620 (spaces, transport, adapted norm, Gaussian data), 93230-93420 (anisotropic Gaussian comparison and its
proposition), 61150-61225 (Gaussian weight jet), 60540-60640 (buffered formation), 57920-57945 (Taylor convergence
statement), 55995-56030 (nested physical step), 2236-2275 (Technical statement B3).

**2.1 What run A and run B differ in.** Row 1237 relabels so that step j of both runs acts on the same lattice. Then
run A's step j is the step of depth j+1 of its own run and run B's is the step of depth j. So the n clause of
(MAPCONV-F) is ||n_(j+1) - n_j|| <= C lambda_0^j, the convergence in depth of the step maps, and the r and f clauses
are the same for the formation remainder at the common frame, plus a frame difference of size at most
2 B_b lambda_b^j (row 1237 Observation 3.1) times the frame derivative.

**2.2 Depth comparisons the account does prove (READ).**
- (ach:weighted-Taylor-step), Proposition ach-Taylor-convergence (L57938 ff.): for m = 2, 3, 4,
  ||T_(j+1,m) - T_(j,m)||_(m, s_sigma) <= C_sigma L^(-sigma j), where T_(j,m) = D_B^m S_j(0) is the m-th Taylor
  coefficient of the actual classical action at the TRIVIAL FLAT reference, in a rooted exponential kernel norm.
- (agc:jet-Lipschitz) (L93341-93356): the Gaussian polarization Pi_j satisfies
  ||Pi_(j+1) - Pi_j||_(t,2) <= C ||J_(j+1) - J_j||_s, J_j = (T_(j,2), T_(j,3), T_(j,4)), "subtracting the formulas
  for two depths, one factor at a time".
- Proposition agc-actual-anisotropic-increment (L93360-93392): hence b_j and m_j, plane readouts of Pi_j, converge
  at rate L^(-sigma j); this gives (hrt:Gaussian-data)'s |b_j - b_infinity| <= B_b lambda_b^j.

**2.3 What is not in the account (READ, by the statements' own scope).**
- (hrt:Gaussian-data) (L93586-93592) gives only ||n_j||_(j+1,*) <= B_n for n_j = N_j - b_j e_(j+1), where N_j is "the
  vacuum-subtracted physical Gaussian pointing for the step from j to j+1" (L93573-93575): a complete pointed analytic
  family, that is, a function of the background to all orders. Pi_j is its quadratic jet at the flat field only.
- Proposition lcf-buffered-formation (L60548-60580): F_j is holomorphic on fixed domains with bounds "independent of
  depth and compatible volume"; it states no comparison of F_j and F_(j+1).
- Proposition ach-Taylor-convergence stops at order four and at the flat reference.

**2.4 Consequence (ARGUED from 2.1-2.3).** (MAPCONV-F) is not one lemma. It needs three depth-convergence theorems
that the account does not make: (M1) the actual classical background map W -> U_j(W), to all orders and on the whole
small-field domain of the regular step, in an analytic norm (the account has orders 2-4 at the flat reference);
(M2) the full Gaussian pointing N_j in the adapted norm (the account has its quadratic jet); (M3) the formation map
F_j at a common frame, plus a bound on its frame derivative of order e_j (to absorb the frame difference). The
account's own technique for Pi_j (subtract the two depth formulas factor by factor) would carry (M2) once (M1) holds
on a fixed complex neighbourhood, by Cauchy in the background; (M3) needs the same for the whole fluctuation integral,
whose depth dependence enters through the fine lattice of each depth (L56017: "Choose the flat fine extensions
compatibly at the two depths"). This is a programme across the formation chapter, not a session item, and I stop it
here. Row 1229 Step 3 ("not a session item") is confirmed with the exact list.

**2.5 Whether (UNIV-K) needs a geometric rate (corrected at 08:29Z by date -u; the first version of this paragraph overstated).**
(UNIV-K) asks only for summable increments eps_K of a scalar on two fixed tori (row 924 Lemma 1.1), so a geometric
rate in (MAPCONV-F) is more than the conclusion needs. But a polynomial rate does not pass through row 924's linear
system as easily as I first wrote. With sources |sigma_j|, ||tau_j|| <= C (1+j)^(-alpha), the coupling component
u_i is of order sum over l >= i of (1+l)^(-alpha), that is (1+i)^(1-alpha); the loop u -> v -> u through
(Ku)_j = sum_(i<j) U_(ji) F_i u_i and (Bv)_i = sum_(l>=i) P_(il) R_l v_l loses one power of (1+j) per pass under the
crude bounds e_l <= e_*/c, k_l <= k-bar of R14, and only the dependence of e_l on N - l (e_l of order
(log(X_0 + N - l))^m/(X_0 + N - l)) can restore it, with logarithmic losses. So the claim "a source decaying like
j^(-3/2)(log j)^c is enough" is NOT established; I expect a threshold alpha > 2 plus a margin, and I did not prove it.
The comparison with chapter 9's transition defects (row 1233) was also loose: those bound coupling-transition maps
between horizons, not the step-map differences of (MAPCONV-F). Withdrawn as a claim; kept as a remark.

**2.8 Why (M1) is not in the account (READ YM4_1400 L92944-93003; written 08:30Z by date -u).** The proof of
Proposition ach-Taylor-convergence first proves a real, per-volume mesh comparison of the whole classical action,
(ach:real-mesh-comparison): |S_(j+1)(B) - S_j(B)|/V <= C_beta h_j^beta for real B in a fixed ball, h_j = L^(-j). It then
reads each Taylor order m separately: a Chebyshev real-to-jet step gives the mixed derivative bound
C h_j^beta (1+j)^(2(m+1)), and an iterated strip interpolation gives the kernel norm with the power
theta = (1 - s/s_0)^(4(m-1)) of the real bound. The exponent theta degrades with m, and the text says the exponential
moments "require no all-arity claim". So the account's method gives every fixed order at its own rate, and no
common rate for all orders in a local (rooted kernel) norm. (M1) needs exactly such an all-arity local estimate; the
per-volume bound alone does not localise (it is proportional to the total volume V, not to the support of B).


**2.6 Which text the gap chain reads (READ; written 08:24Z by date -u).** I fetched the complete account
(theorem_0_complete_account_raw_I, II, III at 31a47c543775; 166711, 145624, 111583 lines) into the same scratch
folder. A count of the regular-trajectory vocabulary ("regular trajectory", "homogeneous regular", "profile ceiling",
"irrelevant profile", "Gaussian pointing", "formation map") gives 0, 1 and 0 lines in CA-I, CA-II, CA-III, against 27 in
YM4_1400.tex; the one-loop constant 11/(3 pi^2) and the adapted norm do not occur in CA at all. So the construction that
rows 924 and 1237 read, and that (MAPCONV-F) is about, is YM4_1400's, not the complete account's.

The gap chain itself reads YM4_1400 too: row 916 (`library/gap-chain-ce-opus.md` L8, L35-37) cites "CA Lnnn" for
the lead's sa1400 copy of YM4_1400.tex and says CA-I line numbers "need not match"; row 1225's Theorem E-N inherits
those citations. GOAL.md pins the T0 chain to the complete account (CA-I, II, III). So, at this pin:

- the continuum datum of the gap chain (rows 916, 1225) and the regular part of (UNIV-K) (rows 924, 1237) rest on
  YM4_1400's statements and premises (its L1748-1751 hypotheses);
- the T0 chain, and row 1233's chapter-9 route to (UNIV-K), rest on the complete account.

Correction (08:29Z by date -u): the lead already tracks this. Row 605 (FINISH L682, lead, 2026-11-09) records that their
repository moved the Theorem 0 sources to YM4/Old/ and added component manuscripts; row 608 (FINISH L685) sets the T0
approach "against the CURRENT frontier of Sussman and Alpoge's YM4_1400, not against CA-I certificates". So the gap
chain (rows 916, 1225), the regular part of (UNIV-K) (rows 924, 1237) and the T0 approach all read YM4_1400; only
GOAL.md's method section still names CA-I, II, III. Two consequences: (MAPCONV-F) is about the current text; and row
1233's chapter-9 reading is of CA-III, now under YM4/Old, so its conclusions need re-location in YM4_1400 or its
submanuscripts before the gap chain can use them (2.7 shows the newest form of that comparison is a hypothesis).

**2.7 The account's newest texts (READ; written 08:26Z by date -u).** The Sussman-Alpoge repository's HEAD is c7fef8b21b58 (2026-11-10, GitHub API).
Its commit ed82e1fea012 (2026-11-09) "Move Theorem 0 sources into YM4/Old": the complete account CA-I, II, III now sits
under YM4/Old, and YM4/YM4_1400.tex (same size, 6318570 bytes, as the 2bc0658f91d2 copy read above) stays current.
Nine YM4 submanuscripts were added on 2026-11-09 and 2026-11-10: BA (block averaging), CL (a scalar continuum theory
from lattice correlations), EM (iteration of regular interactions on prescribed coupling prefixes), FP (short-distance
asymptotics of the action density), GI (Gaussian block integration), LP (periodic Wilson states and reflection
positivity), MB (linear lattice PDE with block constraints), RT (coupling trajectories and partition stability), SI
(scalar sources and uniform insertions). Fetched at c7fef8b21b58 into the scratch folder. Of these only EM and GI are
cited in a gap file (row 986, `library/gap-detlemma-read-opus.md` L91); CL and RT are not cited anywhere in the gap
lane (grep of `library/gap-*.md` and `library/prior/gap-*.md`).

What they say on the cutoff comparison (READ):
- YM4_SI Proposition si:prop-cutoff-comparison (YM4_SI L1899-1960) is a SUFFICIENT condition, with its comparison as
  hypotheses: paired local energies at cutoffs K and K+1 differ by C(1+s) eps_K e^(-kappa m(X)), the normalised
  residuals h_K = Gamma_K e^(-E_K) satisfy |h_(K+1) - h_K| <= eps_K, and sum eps_K < infinity; then the separated
  cumulants (n >= 2) converge. It is about Gamma_K(z) = Z_K(sum z_i f_i)/Z_K(0), normalised at zero source, so it
  reads nothing of the zero-source free energy that (UNIV-K) is about (same point as row 1233 Lemma 3.1 (1), (3)).
  Its last sentence: "Individual bounds at the two cutoffs supply neither comparison."
- YM4_RT's abstract (L112-124): "The local analytic constructions, the one-loop coefficient and the quantitative
  history estimates are explicit inputs. No complex-source stability or continuum limit is asserted here."
- A grep of all nine for "consecutive cutoff", "two cutoffs", "different horizons", "universality" finds only SI's
  proposition above and horizon-uniform constants in EM (L1738, L1864).

So no text of the account, old or new, states (MAPCONV-F) or the zero-source comparison that (UNIV-K) needs; the
newest texts make the two-cutoff comparison an explicit hypothesis. Credit: Ethan Sussman and Levent Alpoge, with
Claude and Codex as authors of their text.

Status of Step 2: (MAPCONV-F) OPEN, stated as (M1)-(M3); not in any account text, old or new; not attacked
further. Next: Step 3.
