lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-20T14:57Z

# gap-mini-solve-h-fable (queue row 1198): the mass gap of four-dimensional SU(2) Yang-Mills, eighth plain-brief row

Worker: Claude Fable 5.2 (max) on the Mac mini, single session, no subagents. Pinned at commit f763c22f1 of
`claude/ym4d-hard-route`. Started 2026-11-20T02:57Z (date -u). Research-stage working state; nothing here is a public claim.
Labels used below: PROVED (a written argument, complete in this file or cited to a checked row), ARGUED (an argument
with a named gap), GUIDE (numeric or heuristic, never a proof step), OPEN.

## 0. Status log (one line per step, times from `date -u`)

- 2026-11-20T02:57Z: file created; reading the row, GOAL.md, the rule sections of FINISH.md.
- 2026-11-20T03:32Z: record read; blind pass done (Section 1). Every candidate named blind was grepped at once; all with a mechanism are on file.
- 2026-11-20T03:42Z: Section 2 written (two remarks; one first draft claim was wrong and is corrected there). Section 3 next.
- 2026-11-20T03:44Z: Section 3 (outcome) and the RESULT line written; anchors printed and checked; PROVED items re-read.

## 1. Repo search and where the record stands (GUIDE: statements about the record, not evidence)

Read in this session: `GOAL.md` in full; `FINISH.md` L1-84, L299-362, row 1198 and the RESULT lines of rows
1186-1215; `parts/gap.md` L8-104; `library/gap-council-synthesis.md` L19-131; `library/gap-solve9-astra62.md`
L60-150 (row 1161, gpt-6.2-astra, checked by row 1162); the head of `library/gap-solve21-astra62.md` (row 1204);
`library/gap-phys-seed.md` L343-375 (row 720); the section lists of the sibling files g, i, k, l. Cross-branch
search: not repeated; rows 1188-1201 ran it and row 1204 cites the lead search of 8 November.

### 1.1 The open statements (cited, not re-proved)

1. **(N-phys)**, `gap-solve9-astra62.md` L148: on one periodic cube n^3 of one admissible physical side, uniformly in
   the cutoff, the centre-neutral excited trace s(u) at u = floor(n/K) is at most 1/2. Row 1179 (Theorem BP) says the
   Jaffe-Witten gap clause needs (N-phys) and the continuum datum of the T0 chain. Both are OPEN. The periodic wall
   (W) needs the branch selection (BS) in addition.
2. **The wall in one sentence** (`parts/gap.md`, State of attack): every engine found is blind to the group. The one
   selective fact that is provable today is asymptotic freedom at weak coupling. No step is known that carries it
   through the band of order-one coupling.
3. **Lead rules that bind a new row** (`parts/gap.md` L76, L97): no further fresh-framing list; a (K-one) input is a
   one-scale property and is tested against Proposition V and the K7 endpoint; a (K-flow) input reads the first-passage
   data of Wilson SU(2) and must fail for a product with a massless factor. "No mechanism for the selective step is
   on record."
4. **Siblings.** Rows 1188-1201 (a to k) each found the lane's map again and then worked one small item. Row 1202 (l)
   is running and says it repeats no screening.

### 1.2 Blind pass of this row (GUIDE; each line was derived from the target before reading, then grepped)

Counts are files among `library/gap-*.md`, `library/prior/gap-*.md`, `parts/gap.md` (one `grep -l -i -F` loop).

| Candidate derived blind | Selective? | Where it sits on the record | Status |
|---|---|---|---|
| Thermal form: (N-phys) is p(T)/T^4 at most log(3/2)/K^3 = 3.0e-9 at T = K/L; flow form "interaction measure Theta = eps - 3p at least gamma p" (then p/T^4 falls like T^gamma) | yes: Theta = 0 for a free photon, Theta has the sign of the beta function at weak coupling | route RB (row 934); (ANOM) `gap-direction-max.md` L189 (row 931: log pi(t_1) = log pi(t_0) minus the integral of (eps/p - 3) dt/t), read against published SU(2) data in row 983; (MONO-Delta), Proposition MB, Proposition NM `gap-phys-seed.md` L351, L353, L375; (NOCRIT) `gap-mid-max.md` L207; (CAS) row 708 | on file in this exact form; "restates the seed in steps" |
| Spectral form of the same: every neutral level of the box, in units of 1/L, grows with L; lattice form: at fixed n the neutral gaps of the transfer operator fall when beta rises | same | same family; (VAC-SUB) `gap-vacsub-max.md` L681 (row 934: prefix sums of the response excess of the levels, with Ky Fan concavity in the magnetic coupling) | on file; needs a Griffiths-type inequality that SU(2) does not have |
| Concavity of log(p/T^4) in log T as the carrier of the first-passage slope | yes | not found by name | FAILS as a belief: at a continuous deconfinement point with a positive specific-heat exponent the second derivative is plus infinity; for p/T^4 itself the inflection sits where p/T^4 is of order 0.01 to 0.1, not 3e-9 |
| Integrate all links through positive auxiliary fields (Budczies-Zirnbauer weight; for the Wilson weight the two-stage quaternion Gaussian); the dual model couples site-local quaternion Gram entries by O(4) inner products | no (the U(1) form is an XY ferromagnet of relative phases, the SU(2) form has the Hopf signs again) | idea 28 `gap-brainstorm2-max.md` L178, L233; C4 `gap-invent-selective-max.md` L113, L194; Identity HS1 `gap-global-reform-max.md` L382; row 1157; row 1199 table | on file |
| Hopf split with Ginibre and FKG (the neutral step of the posted 2D O(4) proof); SU(2) matrix entries carry the sign of U_21 = - conj(w), K_4 is not bipartite | - | row 1084, Lemma HF (row 1188), row 1190 | on file. My first remark here ("the sign is exactly compactness") was WRONG as a lattice statement and is corrected in 2.2 |
| Durhuus-Frohlich with the posted 2D O(4) theorems (3D area law at every coupling) | flux half, 3D | method 36 `parts/gap.md` L70 (row 1139, check 1140): no background-uniform rate at large b; rows 825-834; row 1199 | on file, dead in uniform form |
| Reduction on a 1 x 1 or 2 x 2 twisted two-torus (a 2D model that is semiclassical at weak coupling) | no engine from a small box: a seed needs n m at least K log 2 (row 1184, Lemma N2) | Route T, (AC'), row 842, `gap-ac-lat.md` | on file |
| Spacetime symmetries as the rigid non-abelian group (shifted and rotated periods, stress-tensor response) | no: the free photon passes | row 1201 (`gap-mini-solve-k-fable.md` L84), rows 960-965 | on file |
| Projective (Birkhoff) contraction: cross-ratios of the one-step kernel do not see the spatial weight | no | statement (A), row 1132; 22 files name Birkhoff | on file; the diameter is extensive |
| Born-Oppenheimer lower bound over a block map; Kirsch-Simon comparison | no | not by name; in substance rows 957, 968 (two-level Poincare; Holley-Stroock loss is extensive) | on file in substance |
| Rokhsar-Kivelson form: the Kogut-Susskind operator is the Langevin operator of the 3D Wilson measure minus a positive potential | no | 2 files; ground-state forms rows 863, 957 | on file; eigenvalue differences are not monotone under it |
| a-theorem and thermal counting of massless modes | excludes three free photons only | `prior/gap-kflow-read-opus.md` L99; `gap-direction3-max.md` L474 | on file |
| Fixed-lattice weak-coupling value D(n; beta) = (3/2) log beta + O(log log beta) (twelve quartic constant modes, marginal divergence of the SU(2) matrix integral in four dimensions) | base only | `gap-phys-seed.md` L451 (Item 6) | on file (my first count, 9/4, was wrong: the three global gauge directions are angular directions of the twelve constant modes) |
| Gap from confinement ("all states are flux"); neutral trace bounded by the untwisted periodic excess | needs a Lebowitz-type inequality | row 1190 list; rows 1161 (9), 1179 | on file |
| Other regularizations with a positivity structure (deformed theory on a small circle, finite subgroups, quantum links) | - | row 1190 ("on file in part"); 4 files name deformed Yang-Mills | none reaches R^4 without the same band |

Result of the pass: one more screening finds the map again. No candidate with a mechanism is new. Two remarks have
no file hit by name (the failure of log-concavity of p/T^4 at the deconfinement point; the sign pattern of the
non-compact real form). They are written in Section 2. Neither has a consumer.

## 2. The two remarks without a file hit (no consumer; kept so that they are not derived again)

### 2.1 Remark TH: the logarithmic rate eps/p is not monotone across the deconfinement point (identity PROVED; the use of it is GUIDE)

Setting: the thermal form on file, (ANOM) of row 931. Write x = log T and P(x) = log(p(T)/T^4) for the
vacuum-subtracted pressure in infinite volume. With p' = (eps + p)/T:

  P' = eps/p - 3,   P'' = T C_V/p - eps (eps + p)/p^2,   C_V = d eps/dT.

Proof: P = log p - 4x gives P' = T p'/p - 4 = eps/p - 3. Then P'' = T d(eps/p)/dT = T C_V/p - eps T p'/p^2. QED

A blind candidate for the missing flow step was: "the rate P' = eps/p - 3 is non-increasing in T, so its
first-passage value gamma_1 > 0 is a lower bound at every lower temperature, and p/T^4 falls at least like
T^(gamma_1)". This asks for P'' <= 0, that is, T C_V p <= eps (eps + p).

GUIDE (recalled lattice physics, not a proof, not re-read in this row): the deconfinement point of SU(2) in four
dimensions is continuous, in the class of the three-dimensional Ising model (Svetitsky and Yaffe; critical
couplings on file at `gap-face-exercise-fable.md` L236), with a positive specific-heat exponent. Then C_V is
unbounded at T_c while eps and p stay finite and positive, so P'' is positive near T_c. The candidate is false in
this form. The same holds for p/T^4 itself: its second derivative in x is the slope of (eps - 3p)/T^4, which is
positive below the peak of the interaction measure, and at that peak p/T^4 is of order 0.1 (recalled), far above
the 3e-9 that (N-phys) asks for.

What survives is only the lower bound eps/p - 3 >= gamma_1 below first passage. That is the integrand condition of
(ANOM) and has the strength of the seed (row 931 Step 4; row 708 on (CAS)). So this remark removes one candidate
carrier and adds nothing else. Selectivity note (GUIDE): at weak coupling eps - 3p has the sign of the
beta function times the sign of d p/d g^2, so it is zero for a free photon and negative for an infrared-free
interacting field; `gap-direction3-max.md` L474 already says that (BDD-Delta) excludes infrared freedom only.

### 2.2 Remark OR: sign patterns of the two real forms on a plaquette (PROVED, elementary; corrects my first draft)

Let eps = -1 or +1 and G_eps = { [[z, w], [eps conj(w), conj(z)]] : |z|^2 - eps |w|^2 = 1 }. G_(-1) = SU(2),
G_(+1) = SU(1,1). The inverse is [[conj(z), -w], [-eps conj(w), z]].

(a) Product without inverses. tr(U_1 U_2 U_3 U_4) is the sum over the 16 closed index paths in {1, 2}. A path with
m steps from index 2 to index 1 has m steps from 1 to 2 and coefficient eps^m. So there are eight monomials up to
conjugation: one with no off-diagonal entry, six with one entry w_i and one entry conj(w_j) (coefficient eps), one
with four off-diagonal entries (coefficient 1). For eps = +1 all coefficients are +1.

(b) Lattice plaquette U_1 U_2 U_3^(-1) U_4^(-1). The inverse changes the sign of one off-diagonal entry for
eps = -1 and of both for eps = +1. For a monomial with off-diagonal entries on the links i and j the coefficient is:
eps = -1: minus for the pairs {1,2} and {3,4} (same direction of traversal), plus for the four mixed pairs;
eps = +1: plus for {1,2} and {3,4}, minus for the four mixed pairs.

(c) Removal by the shifts w_l -> -w_l on a set A of links. A pair {i, j} changes sign iff exactly one of i, j is
in A. For eps = -1 one needs a_1 + a_2 = 1, a_3 + a_4 = 1 and a_1 = a_3 = a_4 (mod 2): impossible. This is the
single-plaquette frustration of Lemma HF (`gap-mini-solve-a-fable.md` L85; row 1084). For eps = +1 the choice
A = {3, 4} works on one plaquette.

(d) On the lattice Z^d with d >= 3 the pattern of eps = +1 is not removable by such shifts either. One needs
a(l) to take one value on the two forward links of every plaquette and the other value on its two backward
links. (Reversing the orientation of a link is a relabelling with a -> a + 1 on it, so the question does not
depend on the orientation convention; take the plaquette U_mu(x) U_nu(x + mu) U_mu(x + nu)^(-1) U_nu(x)^(-1).) Writing
a(U_mu(x)) = f_mu(x): f_mu(x + nu) = f_mu(x) + 1 for nu != mu, so f_mu(x) = g_mu(x_mu) + sum over nu != mu of x_nu;
and f_mu(x) = f_nu(x + mu) for mu < nu gives g_mu(t) - t = c_mu with c_mu = c_nu + 1 for every pair mu < nu.
Three directions give c_1 = c_2 + 1 = c_3 + 1 and c_2 = c_3 + 1, a contradiction mod 2. In d = 2 the choice
c_1 = c_2 + 1 works. QED

So my first-draft sentence "the sign obstruction is exactly compactness" is false. Correct statement: without
inverses the compact form has six negative monomials and the non-compact form none; with the inverses of a
lattice plaquette the two forms have complementary patterns, the compact one frustrated on one plaquette and
the non-compact one from three directions on. Scope: only the shifts by pi of the phases of w are treated in (c)
and (d); general phase shifts are the subject of row 1190's statement, which I did not re-prove. No consumer:
a non-compact gauge group has no finite Wilson partition function.

## 3. Outcome

### 3.1 What was attacked and where it stops

The best attack I could name blind was the flow form of the thermal reading: carry the first-passage value of the
relative interaction measure, gamma_1 = eps/p - 3 > 0 at a temperature where the coupling is small, down to low
temperature, and get p/T^4 <= C T^(gamma_1), which reaches the 3e-9 of (N-phys) at one physical size. Its steps:

1. (N-phys) as a pressure bound. On file: row 931 (ANOM), rows 934, 983.
2. gamma_1 > 0 from first-passage data. Not checked here; it needs the pressure to two-loop accuracy.
3. **First failing step:** eps/p - 3 >= gamma_1 at every lower temperature. This is a lower bound at order-one
   coupling. It is false as a monotony statement (Remark TH) and, as a bare lower bound, it is the integrand
   condition of (ANOM), which the record prices as the seed itself ((CAS), row 708; (NOCRIT), row 708).
   No mechanism: every exact tool I can name (reflection positivity in each direction, the crossing identity of
   the torus, Ky Fan concavity, convexity in beta) holds for the free photon, where gamma is zero.

So the attack ends at the lane's wall, in the lane's own words: one selective inequality through the band of
order-one coupling is missing, and no mechanism for it is on record.

### 3.2 Statements of this file

| Statement | Label | New? |
|---|---|---|
| Blind pass, fifteen candidates (1.2) | GUIDE | no: every candidate with a mechanism is on file |
| Remark TH: P'' = T C_V/p - eps (eps + p)/p^2; the rate eps/p is not monotone across a continuous deconfinement point with unbounded specific heat | identity PROVED; the physical premise is GUIDE (recalled) | no file hit by name; no consumer |
| Remark OR (a)-(d): sign patterns of SU(2) and SU(1,1) on a plaquette; the non-compact pattern is removable on one plaquette and in d = 2, not for d >= 3 | PROVED, elementary, for shifts by pi only | no file hit; no consumer; (c) for SU(2) is Lemma HF found again |
| The mass gap of 4D SU(2) Yang-Mills; (N-phys); the continuum datum; (BS); (W) | OPEN | - |

### 3.3 Not done, and one error caught

- No numeric run (none was needed; so no lock was taken and memory was not read).
- No cross-branch search and no literature probe: rows 1188-1201, 1204 and 1216 ran them hours ago.
- The sibling files a to f were read by their RESULT lines only; g, i, k, l by their section lists.
- Error caught before the end: I first wrote "the Hopf sign obstruction is exactly compactness" into the table of
  1.2 without testing it. With the inverses of a lattice plaquette it is false (2.2 (b), (d)). I also first counted
  the fixed-lattice value of D as (9/4) log beta; the record's (3/2) log beta is right.
- Credit: the thermal form and (ANOM) are row 931's (Claude Fable); the (N-phys) reduction is row 1161's
  (gpt-6.2-astra) with row 1179; Lemma HF is row 1188's; the posted two-dimensional O(N) proofs are OpenAI's and
  Ding, Huang and Yang's (arXiv:2611.04908), read here only through the lane's digests; the universality class of
  the SU(2) deconfinement point is Svetitsky and Yaffe's conjecture, recalled.

### 3.4 For the lead (a measured fact, not a request)

Rows 1188 to 1201 and this row are plain-brief rows of one model family. Each found the lane's map again and
none produced a mechanism for the selective step. `parts/gap.md` L76 ("What not to do next") had predicted this
for fresh-framing rows of this family. One more sample changes nothing in that reading.

RESULT: Row 1198 (Claude Fable 5.2 max, Mac mini worker 1; author only, checked by no one; no numeric run, no
subagents). The mass gap is NOT proved and nothing is disproved; (N-phys), the continuum datum, (BS) and (W)
stay OPEN. One more plain-brief screening (fifteen candidates, each grepped when named) found no route off the
lane's map. The best attack named, the thermal flow form (carry the first-passage value of eps/p - 3 to low
temperature), stops at a lower bound at order-one coupling that is (ANOM) of row 931 and has the strength of the
seed. Two small remarks have no file hit and no consumer: Remark TH (identity PROVED, premise GUIDE: the rate
eps/p is not monotone across the SU(2) deconfinement point, so monotony of that rate cannot be the carrier) and
Remark OR (PROVED, elementary: the Hopf sign pattern of SU(1,1) is removable on one plaquette and in two
dimensions but not from three directions on; the SU(2) part is Lemma HF found again). One first-draft claim was
wrong and is corrected in 2.2. Output `library/gap-mini-solve-h-fable.md`.
