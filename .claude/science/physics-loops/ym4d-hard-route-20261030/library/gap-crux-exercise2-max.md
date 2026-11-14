# Crux exercise from latest status (FINISH row 878), Claude Fable 5.2 max

(file seeded by the lead; the author writes below)


## Provenance and plan (written first, before any deep reading)

- Author: Claude Fable 5.2, max effort. FINISH row 878. No subagents. No repository edits.
- Clone: /Users/jonreilly/ym4d-lead/clone at commit cd67a48b3fa7e118dbc93ff0a4968e27e6489951 (pull --ff-only: already up to date, 2026-11-13).
- Skill: docs/ai_methodology/skills/exercise/SKILL.md at 1eb15ac428 (to be read next; the plan below is provisional until then and is refined in place by a later append).

Plan (one step per response, each appended here before the next):

1. Read the skill text (steps 0 to 9). Append the refined step list.
2. Step 0: state the wall. Sources allowed: gap-finishline-opus.md lines 110-160; gap-assume-opus.md table rows 43 and 112 and the lines they cite; gap-skeleton-final.md Sections 0-3 and 13.15-13.20; account statements; FINISH RESULT text of rows 860-875 only where needed.
3. Step 1 to Step 3 of the skill (as the skill names them), one per response.
4. Step 4: every assumption of the present formulation, one group per response: (a) the action; (b) the transfer operator on a torus; (c) the centre and the twists as variables; (d) one scale versus many; (e) SU(2) directly versus a larger or deformed theory; (f) Euclidean versus not; (g) assumptions that look like definitions. For each: what follows if dropped or changed, and the exact cost.
5. Candidate routes: each with its CRUX lemma. Run the four fact tests on each (U(1) Coulomb; Q_8 and 2T; proved obstructions; no fixed small number).
6. Attack the CRUX lemma of the best route as a real proof, one stage per response. Record failures as they occur.
7. Attack the CRUX lemma of the second route the same way.
8. Step 5 (compare): only now open the other gap-*.md files, prior/*, exercise-skill-v2.md, FINISH rows 697-877; grep main and open YM4D PR branches (bounded). Name every earlier statement repeated, with path and line. Mark new only after the search.
9. Steps 6 to 9 of the skill, one per response.
10. Measure of the skill (row 721 Section 4.6). Final line "RESULT:".

Labels used: PROVED (mine), READ (path and line), ARGUED, GUIDE, OPEN.
Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the account YM4_1400; Balaban for his estimates.

## Header (skill output rules)

- Written by: Anthropic, Claude Fable 5.2 (claude-fable-5-2), max effort, one agent session, no subagents. Date 2026-11-13.
- Nothing in this file is checked by another model.
- What this run did not cover: kept current at the end of the file (see "Not covered").

## Refined plan after reading the skill (1eb15ac428, read in full)

The skill has steps 0 to 9. I follow its order. Each bullet is one or more responses; each is appended before the next starts.

- S0. Locate the record. Open-now list and closed-until-step-5 list (the brief fixes both). Refresher read replaced by the lane contract (GOAL.md), since this is a standalone proof target.
- S1. State the wall twice: plain (150 words) and precise. No blind check can run (no subagents); I say so.
- S2. Inventory: what is known to be true, each item marked DEF / SUPPLIED / THM / BELIEF with source and reading state.
- S3. Reason up from the inventory only: what follows at once; the least a solution must contain; the smallest object; where the result can come from; make the requirement less wrong; price it. Conclusions C1, C2, ...
- S4. Assumptions table, six groups (a) target, (b) formulation, (c) reduction, (d) discard tests, (e) beliefs, (f) working rules. The brief's list goes in (b) and (c): the action; the transfer operator on a torus; the centre and the twists as variables; one scale versus many; SU(2) directly versus a larger or deformed theory; Euclidean versus not. For each: what follows if dropped or changed, the exact cost. Ranking. Fresh candidate routes are written here with their CRUX lemmas, before the closed files open.
- S5. Compare: open the closed list; grep the lane, main and open YM4D PR branches (bounded). Yes / partly / new for each conclusion and each ranked assumption, with path and line.
- S6. The blockage: 6a set-aside methods; 6b first principles on the blockage; 6c audit of every discard test in its logical form; 6d re-judge every verdict.
- S7. Routes: generate, try to kill, rank. Fact tests of the brief applied to each.
- S8. Real attempts on the best two or three routes: the CRUX lemma of each attempted as a real proof, one stage per response.
- S9. Report (plain language first), work items, appendix pointers.
- S10. Measure of the skill (row 721 Section 4.6). Then one line "RESULT:".

### Status block (appended as lines; the last line for a step is the current one)

- S-plan: done.

---

## Step 0. Locate the record; open and closed lists

**Refresher read, replaced.** This is a standalone proof target. Its contract is D/GOAL.md (READ in full, 92 lines). It reads no framework axiom or primitive. So the contract and its rules replace the framework refresher list. The rules that bind this run: no computer-assisted step (every proof step a written argument that could be formalized in Lean; a run may refute or guide only); the chain to T0 is the ported account of Sussman and Alpoge; the mass gap is a later target of GOAL.md and the present main work by the lead's decision.

**Paths.** Clone C = /Users/jonreilly/ym4d-lead/clone. D = .claude/science/physics-loops/ym4d-hard-route-20261030. SK = D/library/gap-skeleton-final.md. FL = D/library/gap-finishline-opus.md. AS = D/library/gap-assume-opus.md. FIN = D/FINISH.md (row n at line n + 76).

### 0.1 Open now (statements only)

1. The finish line (SEED-FP): READ FL L110-160 (Section 2.2 to 2.5). Exact text of the statement, FL L114-118:
   "There are K_0, a physical size ell with ell/(2 a_K) an integer at least 3 for every K >= K_0, and a number s_* < 1/5041 such that, for every first-passage datum (K, beta) at g with K >= K_0, S_(K,beta)(ell/(2 a_K); (ell/a_K)^3) <= s_*, the thermal sum of the bare Wilson transfer operator of the periodic cube of physical side ell at physical time ell/2."
   Section 2.5 there (table, steps (a) to (f)) gives (GAP) from (SEED-FP) with the account; steps (c), (e), (f) are ARGUED there and not checked.
2. Definitions: SK Sections 0 to 3 (L1-68) and 13.15 to 13.20 (L547-644), READ in full.
3. The crux in its weakest fixed-coupling forms. READ at the lines AS rows 42 to 45 and 67 cite:
   - Twisted weights (READ D/library/gap-ext-astra.md L79-103): lattice torus n = (a, a, c, d), a >= 3, c, d in {a, 2a}; s_p(U) = tr(U_p)/2; for a spatial twist m with closed sign cocycle eta_m, S_m(U) = beta sum_p (1 - eta_(m,p) s_p(U)), d mu_m = Z_m^(-1) e^(-S_m) dU; for a temporal twist v = v_(ri) with representative Sigma, R_m(v) = E_(mu_m) exp(-2 beta sum_(p in Sigma) eta_(m,p) s_p) = Z^(m+v)/Z^m, and 0 < R_m(v) <= 1.
   - The twist deficit and its trace form (READ D/library/gap-expose-astra.md L576-583, (E16)): p_(m,i)(a) = Tr(P_(-,i) L_m^a)/Tr(L_m^a) = (1 - R_m(v_(1i)))/2, and Q_F = max over m_2 = 0, i = 3, 4 of p_(m,i)(a).
   - (FQ) (READ gap-ext-astra.md L118-124; D/library/gap-vortex-astra.md L198-203): 8 Q_F <= K(a) sqrt(S_ev(a; (a, c, d))), Q_F < 1/192, K(a) <= C_1 a^(p_1). "It gives the fusion input (F-h), not the separate even seed."
   - (E17) (READ gap-expose-astra.md L585-593): Q_F <= C a^p eta_*^(a/2), 0 < eta_* < 1, where the proved witness is S_ev(t; B) >= eta(beta)^t, eta(beta) = e^(-80 beta) r^4/(4 + 16 r^4), r = I_2(beta)/I_1(beta) (READ D/library/gap-fusion-astra.md L88-101).
   - (V) (READ gap-vortex-astra.md L100-105): max_k [-log(Z^k/Z^0)] <= C a^p e^(-sigma a^2) on a fixed compact beta interval.
   - (J12) (READ D/library/gap-joint-astra.md L346-356): sup_p of the sum over surfaces S with v(S) = 1 and root(S) = p of |D_m(S)| <= C_1 a^b e^(-kappa a), kappa >= (1/2) log(1/eta_*). Here (J2)-(J4), L105-146: Z_m = integral of C(U) Xi(w_m; U) dU with t_p = tanh(beta x_p), and p_m(v) = sum over S with v(S) = 1 of D_m(S), a signed sum over closed mod-2 surfaces against the original Z_m.
   - (G2) (READ FIN L889, the brief text of row 813): "the mean of Hess S(grad f, grad f) is at least -theta times the mean of the squared Hessian of f minus (2 - kappa) times the mean of the squared gradient, with theta below 1 and kappa above 0, for every gauge-invariant f, uniformly in volume, at a compact order-one beta interval"; its RESULT there: (G2) on a compact beta interval is equivalent to a volume-uniform gauge-invariant Langevin gap.
4. The newest form of the crux, from the RESULT text of FIN rows 860 to 875 (READ L937-952; only the RESULT text):
   - Row 860 (checked row 864): "P_- is exactly the event of an odd number of half-integer edges in the cut, i.e. the half-integer Z_2-cycle of a slice has odd omega-class"; "(LS) equals (E17) up to e^(-c#E)". The carrying statement, OPEN: "the dense half-integer Z_2-cycle has trivial omega-class except with probability C a^p eta_*^(a/2); its proof must fail for U(1) and for frozen 2T and Z_2, and work on a percolating set (no Peierls count)." Row 864: U(1) does not satisfy the spin-5/2 filter bound on Sym^5 V, so the filter is SU(2)-specific.
   - Row 867 (checked row 869, holds after repairs): Proposition TL: "the parity of any edge set is a 't Hooft loop, E[(-1)^N_h(R)] = Z(flip R)/Z, so the parity statement is the wrapping 't Hooft surface". Lemma QS: deleting one plaquette's weight makes its four links conditionally independent. Row 869: the six-candidate exclusion FAILS and fact test T3 is not established.
   - Rows 866, 870: relative homological analyticity (HA) of the centre-odd marker implies (E17); HA is strictly stronger; HA fails for Z_2 at beta 5/2 and in a background-uniform SU(2) version.
   - Rows 871, 874: with mu_(k,lambda) (each plaquette weight 1 + lambda eta t_p), the deficit is F(1) = integral over [0, 1] of the response R; (C2), a bound C a^p e^(-ga) on the integral of |R| over [lambda_0, 1], with (C1) implies (E17); (C2) restates (E17) or is stronger.
   - Rows 872, 873: Proposition EXP: d log Tr(P L(s)^t)/d log s = t times the one-slice count of high-spin edges; the filter carries (E17) exactly when EXC holds (the integral of Delta(s) ds/s is at least c_0, Delta = Cov(N_hi, 1_odd)/p); EXC is OPEN and not ruled out. Row 875 (attack on EXC): queued, no RESULT in the clone at cd67a48b3.
   - Row 861 (final, unchecked): an exact soft block step gives the zone's per-link size for free for any input and for U(1) (Proposition FREE); "the vacuum constant of any exact step equals F_T - log Z_T (Proposition VAC), so soft step then Theorem HO is circular for the seed"; OPEN (PATH) and PIN-MIX.
5. Fact tests of the brief (taken as given facts with their rows): the Villain U(1) twist theorem (row 786); Q_8 and 2T as binding tests (rows 838, 843); ceilings 0.775 (vertex blocks) and 2/3 (single-site, slab); background-uniform one-layer twist bounds fail above beta_W = 4 G_3 = 1.0109 (row 839); (AN1) equivalent to the worst-case exterior bound (row 845).
6. The account YM4_1400 at 2bc0658f91d2: statements only, as cited by FL (SA L6863-6869 dilation identity; L6879 volume-first limits; L6913, L21518-21532 the tori T_ell; L17285 and CA-I L2582 the mass identity; L22310 the size of E_0).

### 0.2 Closed until Step 5

Every other D/library/gap-*.md file (including gap-crux-exercise-max.md); D/library/prior/*; D/library/exercise-skill-v2.md; FIN rows 697 to 877 (apart from the RESULT text above); main and the open YM4D pull-request branches. I read lines of gap-expose-astra.md, gap-ext-astra.md, gap-vortex-astra.md, gap-joint-astra.md and gap-fusion-astra.md only at the cited statement lines above; their arguments stay closed. AS: header and ledger rows 32 to 67 read as statements (more rows than the brief names; their "what if wrong" columns in Part 2 stay closed, except the two lines of rows 43 and 112 that the grep printed: L245 and L335).

### 0.3 Literature record

The lane has one (D/library/prior/, closed until Step 5). Before Step 5, I use only statements of results that I recall, each marked "recalled".

Status: S0 done.

---

## Step 1. The wall, stated twice

### 1.1 Plain version (about 150 words)

We want to prove that the lightest excitation of the four-dimensional SU(2) gauge theory has a positive mass. This is the missing half of a famous open problem; an account of the other half (existence) exists in conditional form. The lane has reduced the mass statement to one inequality on one finite periodic box. The box must be many times larger than the distance over which the field forgets itself. At that distance the force is neither weak nor strong. Every exact tool we hold (mirror positivity, the step operator in time, convexity) is also true for a light-like theory that has no mass, so it cannot prove the inequality. Every tool with a small number works only where the force is very weak or very strong. The proofs cover both ends and not the middle. Getting past it means: a way to verify the inequality at middle strength that uses a property the massless theory lacks. Analogy: we can test a rope at both ends and not in the middle, where it carries the load.

### 1.2 Precise version

**Target.** (SEED-FP), READ FL L114-118, quoted in 0.1. Quantifiers: there exist K_0, ell, s_* < 1/5041; for all first-passage data (K, beta) at the one reference coupling g with K >= K_0. Domain: bare Wilson SU(2), periodic cube of physical side ell, physical time ell/2, spacing a_K = L^(-K) in the first-passage unit. Consumer: FL 2.5 gives (GAP) on the tr F^2 sector from it, given the account's packages A to H (READ FL L154-164; steps (c), (e), (f) ARGUED there).

**Equivalent and sufficient forms (READ; each with its check state as the sources give it).**
- (SEED-L): the defect of one more block step, Phi_L <= phi_* < 0.131 L (FL L123; Lemma FL argued, not checked).
- (ES) at one physical size, uniformly in the cutoff: the even thermal sum and the vacuum-energy defect both at most 1e-7 (SK L620; Theorem R checked by Codex gpt-6-astra max, row 744).
- The consumer route at one size: small even sums and (FQ), with K bounded in physical units (FL 2.4 item 3). At fixed coupling: (E17), (V), (J12), HA, (C2), EXC (0.1 items 3 and 4), each sufficient for the flux half, none proved at order-one coupling.

**The wall.** No statement in this list is proved at an effective coupling of order one. In the bare Wilson theory the proved range ends near beta = 2/9 for the seed and beta below 2/3 for the area law (READ AS row 48), while the crossover window is bare beta_W about 2.3 to 2.6 (brief). The continuum statement needs the same control at the scale of the correlation length, along the whole first-passage trajectory. No fixed beta gives that.

**Allowed premises.** Definitions; the lane's checked theorems (Theorem S, SH, EV-L, R, L3, the transfer operator facts (TM), (TM-c), (TM-tw)); the account's statements, as conditional inputs; Balaban's estimates as the account uses them.

**Forbidden weakenings.** A fixed bare coupling in place of the trajectory. A numeric certificate in place of a written proof. An argument that holds verbatim for U(1) in its Coulomb phase. An argument whose only non-abelian input also holds for Q_8 or 2T at a coupling where those are frozen.

**Boundary cases a proof must respect.** U(1) Coulomb: the twist deficit does not decay (row 786, taken as a fact). Z_2 at large beta: (G_ev) holds and the periodic seed fails (SK L580). Finite subgroups Q_8 and 2T at order one. A slab of width 1/T_c (SK Section 3, recalled there). The proved obstructions: worst-case Dobrushin ceilings 2/3 and 0.775; background-uniform one-layer twist bounds stop at beta_W = 1.0109; (AN1) is the worst case.

**Outcomes that do not count.** Another equivalent form with no proof. A map of attacks with nothing tried. A proof at small or large beta only.

**What counts as progress.** One of: (i) a route whose CRUX lemma is stated with quantifiers and attempted as a proof, with the exact line where the proof stops; (ii) an exact price (an equivalence with a named statement, proved); (iii) a misframing shown by a proof or a counterexample; (iv) a discard test or verdict corrected, with what comes back.

**Blind check.** Not run: no subagents are allowed. The plain version is corrected in Step 9 if the exercise changes it.

Status: S1 done.

---

## Step 2. The inventory: what is known to be true

Sources: the open-now list of Step 0 and recalled statements of published results. "recalled" means stated from memory in this run and not re-read. No proof step below may use a BELIEF.

| # | Item | Mark | Source | Standing and reading state |
|---|---|---|---|---|
| I1 | The model. Links U_e in SU(2) on a periodic lattice torus; s_p = tr(U_p)/2; weight exp(beta sum_p s_p) dU, Haar normalized. Compact link space, strictly positive continuous density, exact gauge invariance. | DEF | gap-ext-astra.md L79-87; AS row 66 | - |
| I2 | Twists. A class k in H^2(T^4; Z_2) (six bits) with a closed sign cocycle eta_k; Z^k = integral of exp(beta sum_p eta_(k,p) s_p). Z^k > 0 and Z^k <= Z^0; Z^(m+v) <= Z^m for a temporal twist v. | DEF + THM | AS rows 60, 61; gap-vortex-astra.md L93-96 | lane-proved, READ as statement |
| I3 | (TM): in each axis direction a positive trace-class transfer operator with a simple top eigenvalue, on boxes with sides >= 3. (TM-c): centre flips commute with T; twisted partition functions are traces with a flip inserted. | THM | AS rows 56, 57 | checked (rows 667, 671, 698, 699); READ as statement |
| I4 | Theorem S, SH: a thermal sum below a shape threshold on one box gives the gap on every larger box. It uses only (TM) and axis exchange; it holds for every group and every symmetric model with positive transfer operators. | THM | FL L108; AS rows 32, 34 | checked (row 707); READ as statement |
| I5 | Theorem EV-L and Theorem R: the limit half needs only the centre-even sector; the even seed (ES), two numbers, is equivalent at some size to each of three flux seeds. | THM | SK L574, L620 | checked by Codex gpt-6-astra max (rows 732, 744); READ as statement |
| I6 | The flux half as a probability. p_(m,i)(a) = Tr(P_(-,i) L_m^a)/Tr(L_m^a) = (1 - Z^(m+v_(1i))/Z^m)/2. P_- is the event that the half-integer Z_2-cycle of a time slice has odd class. | THM | gap-expose-astra.md L576-583; FIN L937 | checked (row 864); READ as statement |
| I7 | Proposition TL: the parity of an edge set of half-integer spins is a 't Hooft loop, E[(-1)^(N_h(R))] = Z(flip R)/Z. So the flux half is the free energy of a wrapping 't Hooft surface (a centre vortex sheet that wraps the torus). | THM | FIN L944, L946 | holds after repairs (row 869); READ as statement |
| I8 | Sufficient forms of the flux half, all OPEN at order one: (E17); (V); (J12); HA; (C2) with (C1); EXC. HA fails for Z_2 at beta 5/2. | THM (implications) | 0.1 items 3, 4 | implications checked (rows 870, 874, 873); READ as statements |
| I9 | Proved bare-coupling ranges for Wilson SU(2): seed and lattice gap for beta < 2/9; Langevin gap for beta < 1/4; area law for beta < 2/3. | THM | AS row 48 | lane rows 790, 818, 829 and others; READ as statement |
| I10 | Proved obstructions. Worst-case single-site Dobrushin stops at 2/3 in the slab; vertex blocks at 0.775 (row 861 corrects: this caps one family of majorants). Every background-uniform one-layer twist bound fails above beta_W = 4 G_3 = 1.0109. (AN1) is equivalent to the worst-case exterior bound. | THM | brief; FIN L938 | rows 839, 845 checked (brief); READ as statement |
| I11 | Soft block steps. An exact soft block step gives the strong-coupling zone's per-link size for free, for any input and for U(1); the vacuum constant of any exact step equals F_T - log Z_T, so the step then a high-temperature theorem is circular for the seed. | THM | FIN L938 (row 861) | not checked (row 877 queued) |
| I12 | The account. On its own untwisted tori T_ell (ell = 2 L^m >= ell_*(g)) the account constructs unit-lattice densities rho_K with total mass exactly Z; the dilation identity maps (K, L ell) to (K+1, ell). It stops at first passage (effective coupling g small). It makes no statement on the law of the block field. | SUPPLIED (conditional outline) | FL L119-123, L136; Sussman and Alpoge, with Claude and Codex, YM4_1400 at 2bc0658f91d2 | statements read through FL only |
| I13 | U(1), four dimensions, Wilson or Villain action, large beta: massless phase, no gap; Wilson loops have perimeter law. | THM (published) | Guth 1980; Froehlich and Spencer 1982 | recalled; not re-read |
| I14 | Villain U(1) twist theorem (row 786): in the Coulomb phase the Z_2 twist deficit does not decay. | THM (lane) | brief | taken as a fact from the brief; statement not re-read |
| I15 | Z_2 gauge theory, four dimensions: self-dual; at large beta it is gapped and deconfined (perimeter law, 't Hooft loop area law); the twist ratio Z^v/Z^0 tends to 0 with the area, so p tends to 1/2 and the periodic seed fails. | THM (published; the gap at weak coupling) + lane | SK Section 3; SK L580 | recalled there |
| I16 | Finite subgroups Q_8, 2T, 2O, 2I of SU(2) with the Wilson action freeze at a finite coupling (first-order transition; frozen side deconfined). Recalled values: 2T near 2.2, 2O near 3.2, 2I near 5.8. | BELIEF (numerics) | Petcher and Weingarten 1980, recalled; AS header cites Hartung et al. arXiv:2201.09625 Table IV | recalled |
| I17 | Tomboulis-Yaffe inequality: a Wilson loop is bounded by a power of the twist deficit, exponent area/(cross-section). So decay of the vortex free energy gives the area law. Holds at every beta. | THM (published) | Tomboulis and Yaffe 1985; SK L612 names it with Kanazawa's extension | recalled |
| I18 | Froehlich 1979; Mack and Petkova 1979, 1980: SU(2) Wilson loops are bounded by Z_2-type quantities; a sufficient condition for confinement by vortex condensation in terms of "vortex containers" with the exterior held fixed. | THM (published) | Phys. Lett. 83B; Ann. Phys. 123, 125 | recalled; statements only, not re-read |
| I19 | Borgs and Seiler 1983: SU(N) at fixed time extent N_t and large beta is deconfined (the Polyakov loop orders). | THM (published) | Comm. Math. Phys. 91 | recalled; row 869 found a mismatch in one use of it |
| I20 | Exact solutions and proved gaps elsewhere: two dimensions (exact); three-dimensional U(1) at every coupling (Goepfert and Mack) by a second small number, the monopole activity. | THM (published) | SK L590 | recalled there |
| I21 | Finite-size criteria: Dobrushin-Shlosman and Martinelli-Olivieri type conditions verify mixing from one finite volume, under worst-case boundary conditions. | THM (published) | SK L590 | recalled |
| I22 | SU(2) Wilson theory in four dimensions has no phase transition in beta; crossover near 2.2; string tension about 0.14 in lattice units at beta 2.3; half-integer edge density about 0.33 at beta 2.3. | BELIEF (numerics) | FIN L943 (GUIDE); recalled Monte Carlo values | used in no proof |
| I23 | Asymptotic freedom: the correlation length in first-passage units is of order exp(12 pi^2/(11 g^2)). | BELIEF + account (conditional) | SK L33 | used in no proof |
| I24 | The fundamental-adjoint action has a first-order line with an end point near the Wilson axis. | BELIEF (numerics) | SK Section 3 (K7) | recalled there |
| I25 | The character expansion of 4D Wilson SU(2) has a term with a minus sign (a projective plane of 92 plaquettes). | THM (lane) | SK L610, L624 | checked (row 744) |
| I26 | Supplied choices: Wilson action; periodic tori; transfer operator one lattice step along an axis; centre twists as the flux variables; one fixed physical box. | SUPPLIED | AS rows 54, 55, 60, 62 | - |

Nearest models where the target is false or true for a known reason (they become tests in Step 6): I13, I14 (false: no gap, twist deficit stays); I15 (even gap true, periodic seed false); I16 (frozen: flux half false); I20 (true, by exact closure or a second small number); a slab at the critical width (SK Section 3).

Status: S2 done (26 items).

---

## Step 3. Reasoning up from the inventory (written in parts; earlier attacks closed)

### 3.1 What follows at once

**F1 (argued from I4, I5, I15).** The target (GAP) is not a confinement statement. Any one of the three seeds gives it. Z_2 at large beta is deconfined and still has the even gap. So the enemy of the target is a massless phase or a critical point, and nothing else. Confinement enters only through the choice of the periodic seed and its flux half.

**F2 (argued from I6, I7).** The flux half is a lower bound on an energy. In the trace state, p_(m,i) is the weight of the states that are odd under the centre flip T_i of direction i. So (E17) says: the lowest odd level lies at least kappa = (1/2) log(1/eta_*) above the ground level, up to (p log a)/a. Write the lowest odd state as f Omega with Omega the positive ground state of (TM). Then f is odd under T_i, so f is orthogonal to constants in L^2(Omega^2), and the odd gap is at least the full gap of the box. So the flux half follows from the full seed and is no easier than "the box has a gap times side that is large" (this is the known equivalence periodic seed = even seed + flux half, seen from the ground-state side).

**F3 (argued from I13, I14, I16; the tests are not parallel).** U(1) Coulomb fails the target itself. Frozen Q_8 and 2T do not fail the target (they are gapped, by the same reason as Z_2 at large beta; this is a BELIEF for Q_8 and 2T, a recalled theorem for Z_2). They fail only the flux half in its confining form. So the U(1) test binds every route to (GAP). The finite-group tests bind only routes that go through the periodic seed. A route through the full seed or through (G_ev) directly must pass U(1) and need not separate SU(2) from frozen 2T.

**F4 (argued from I12).** Given the account, the finish line is a statement about a family of unit-lattice weights rho_K that are close to the Wilson weight at one small coupling g, on a torus of side about 15 correlation lengths, that is exp(c/g^2) lattice units. So it is as hard as the lattice gap at weak bare coupling with the right rate. Any proof must cross about 12 pi^2/(11 g^2 log L) block scales between first passage and the correlation length, on which the effective coupling grows from g to order one.

**F5 (PROVED here, a short lemma; uses only a self-adjoint family H(x) = A - x B with B bounded and a simple ground level).** Let E_0(x) < E_1(x) be the two lowest levels, Delta = E_1 - E_0, both differentiable at x. Then for every h > 0:

  -Delta'(x) <= Delta(x)/h + [E_0(x) + h E_0'(x) - E_0(x + h)]/h.

Proof. Let psi_1 be a normalized eigenvector for E_1(x). The variational principle at x + h gives E_0(x + h) <= <psi_1, H(x + h) psi_1> = E_1(x) - h <B>_1. So <B>_1 <= (E_1(x) - E_0(x + h))/h. Feynman-Hellmann gives E_0'(x) = -<B>_0 and E_1'(x) = -<B>_1 (for a simple level; for a degenerate level take the one-sided derivative of the lowest branch). So -Delta' = <B>_1 - <B>_0 <= (E_1(x) - E_0(x + h))/h + E_0'(x), which is the claim. QED.
The bracket is the concavity defect of E_0, at most (h^2/2) sup |E_0''|. With h = (2 Delta/|E_0''|)^(1/2): -Delta' <= (2 Delta sup|E_0''|)^(1/2). The second derivative of the ground energy is extensive (a specific heat times the volume). So this a priori bound lets the gap close at a finite coupling in a finite volume, as it must: a first-order point does that. It is not volume-uniform. I record it because 3.4 uses its form: what a continuity method in the coupling would need is the linear law -Delta' <= C Delta with C free of the volume, and the lemma shows the general theory gives only the square-root law with a volume factor.

### 3.2 The least a solution must contain

1. It must contain a statement that is verified at the scale of the correlation length, in a box of at least about 13 correlation lengths (SK L553), with no small number there. So it contains either an exact structure that survives to that scale, or an inequality that carries information from a scale where a small number exists.
2. It must fail for U(1) Coulomb (F3). The properties of SU(2) that U(1) lacks, from the definitions (I1): (a) the centre -1 is a commutator; (b) the group is simply connected, so the quotient by the centre has a finite fundamental group; (c) there is no nontrivial one-dimensional representation, so no gauge-invariant function of one link, and no conserved integer flux; (d) the Lie algebra has no centre, so no nonzero element is fixed by the adjoint action: the group has no continuous family of flat directions that survives conjugation; (e) the Casimir is bounded below by 3/4 on every nontrivial representation and the tensor square of the fundamental contains the trivial representation. A proof must use at least one of (a) to (e). For the periodic seed it must also fail for frozen Q_8 and 2T, which share (a), (c), (e) and part of (b); what they lack is connectedness (no path from 1 to -1) and (d) in its continuous form.
3. Along the trajectory it must be stable under the changes of the weight that the account allows between the Wilson weight and rho_K (I12), or it must work with the Wilson measure on the fine lattice directly (FL 2.3).
4. It must not be a worst-case statement over exteriors above the proved ceilings (I10): the input at order one has to be an averaged or typical statement about the measure itself.

(continued in 3.3)

### 3.3 The smallest object

**F6 (argued from I3, I6; the magnetic frame).** Take the direction j orthogonal to the twist plane (1, i) as time. Then v_(1i) is a spatial twist of that frame, and Z^(m+v)/Z^m = Tr(T_tw^n)/Tr(T^n) with two transfer operators on the same link space, one with the plaquettes of one dual line flipped. As n grows the ratio behaves as exp(-n (E_0^tw - E_0)). So the flux half, seen from the crossed frame, is an upper bound on one number: the ground energy of the twisted spatial box minus that of the periodic box (the energy of a centre vortex tube through the cross-section). An upper bound on a ground energy is a variational statement. A trial vector that is the periodic ground state itself gives only the thin-vortex cost, 2 beta times the plaquette mean per unit length (PROVED by Jensen: Z^(m+v)/Z^m >= exp(-2 beta sum over Sigma of E_m[eta s_p])). So the smallest object that holds the flux half is one pair of ground energies of one spatial box, and the missing piece is a trial vector for the twisted box built from the unknown periodic ground state.

**F7 (argued; the dimension count).** Spreading an abelian flux pi over a cross-section of sides a_1, a_i costs beta pi^2 a_j a_k/(2 a_1 a_i) in the Gaussian approximation. This is scale-invariant in four dimensions. It is the gauge analogue of the helicity modulus of a two-dimensional spin system. So the four-dimensional gauge problem sits where the two-dimensional spin problem sits: U(1) corresponds to the XY model (a massless phase exists), SU(2) to the O(3) or principal chiral model (a gap is believed at every coupling and is not proved). This is an analogy and a BELIEF; I use it only to choose where to look.

**The smallest sector that holds the target.** The centre-even sector of one periodic cube, two numbers (I5). A toy model in which the wall still bites: the two-dimensional SU(2) principal chiral model, same asymptotic freedom, same absence of a proof. I did not build a numeric toy: no run can discharge a step here, and the lane has guide runs already (FIN L937, L944).

### 3.4 Where the result can come from

Mechanisms that could make the target true, each with the way it can fail:

- (m1) A flow across scales with a quantity that moves one way. Fails where no monotone quantity is known that is not group-blind (I11).
- (m2) A second small number after an exact change of variables (as in Goepfert-Mack). For SU(2) the candidates are: a vortex activity after separating the centre (Z_2) part of the links from the SO(3) part; the numerical smallness of high-spin character coefficients (I8, the spin filter); 1/(number of faces at an edge). None is known to be small at the scale of the correlation length.
- (m3) Exact closure. Holds in two dimensions for the heat-kernel weight (the semigroup law in the area). In four dimensions each face of the lattice still carries an exact two-dimensional theory, but six faces meet at every edge.
- (m4) An inequality with a parameter that gives a dichotomy, and a separate exclusion of the bad branch. The bad branch here is "massless" (F1). No theorem excludes a massless branch for SU(2) by symmetry alone: the one-form symmetry is only Z_2, which permits a gap and does not force one (argued from I1).
- (m5) A continuity method in a parameter: the set where the seed holds is open (AS row 51), so one needs an a priori bound at a first bad point. F5 shows the general bound is the square-root law with a volume factor; the linear law is what scaling predicts and what a proof would need.

Is it one problem or several? By scale it is three: (S-uv) from the cutoff to first passage, covered by the account in conditional form; (S-mid) from first passage, effective coupling g, to an effective coupling of order one, where the account's method (small coupling) is still the right tool in principle but the account stops; (S-ir) at order-one effective coupling, where no small number exists. By sector it is two: the even gap and the vacuum-energy defect (I5).

### 3.5 Make the requirement less wrong

- The consumer (FL 2.5) needs the gap on the tr F^2 sector of every volume-first limit. It does not need confinement (F1), a string tension, or the periodic seed in particular.
- It needs one physical size and no rate. Any m > 0 at any size ell passes (FL L117: s_* < 1/5041 at one ell).
- (E17) is a fixed-coupling proxy. It is stronger than needed in one way (its exponent is tied to a one-step witness, about 93 per lattice unit at beta 2.3) and useless in another (AS L245: it is not a continuum consumer). A lower bound on the odd level by a constant that grows with the side in physical units is what the continuum form needs.
- A statement at one fixed bare coupling in the window is not on the path unless it comes with stability under the account's changes of the weight (FL 2.3 item 3).

### 3.6 Price

If the target cannot be derived with present tools, the missing input is exactly one of: (P-a) a seed for the family rho_K at one physical size (the finish line itself); (P-b) the same at (S-ir) for a class of weights that provably contains the weights that (S-mid) delivers, plus (S-mid) itself. No smaller price follows from the inventory alone.

### 3.7 Conclusions of Step 3

- C1 (from I4, I5, I15): the target needs only the exclusion of a massless branch; confinement is an artefact of one of three seeds. [argued]
- C2 (from I6, I7, I3): the flux half is a lower bound on the lowest centre-odd level; from the crossed frame it is an upper bound on a twisted ground energy, a variational statement whose trial vector is missing. [argued; the Jensen bound is proved]
- C3 (from I13, I16): the U(1) test binds every route; the finite-group tests bind only routes through the periodic seed. [argued; rests on a BELIEF for Q_8 and 2T being gapped when frozen]
- C4 (from I1): a proof must use one of: the centre is a commutator; finite fundamental group of the adjoint group; no gauge-invariant function of one link and no conserved integer flux; positive curvature and connectedness. [argued]
- C5 (F5): a continuity method in the coupling has a general a priori bound of square-root type with a volume factor; the linear law -Delta' <= C Delta, uniform in volume, is the exact missing estimate of that method. [the lemma is proved here; the reading is argued]
- C6 (from I12, FL 2.3): the problem splits by scale into (S-uv), (S-mid), (S-ir); only (S-ir) lacks a tool in principle. [argued]
- C7 (F7): the wall is the gauge twin of the two-dimensional O(3) mass-gap wall. [belief]

Status: S3 done (C1 to C7; one short lemma F5 proved here; the Jensen bound of F6 proved).

---

## Step 4. The assumptions table (written group by group; attack files still closed)

Columns: ID | assumption | where used | needed by target (T) / needed by method (M) / habit (H) | if wrong or dropped | easier? | cost and check.

### 4.a Target

| ID | Assumption | Where | Kind | If wrong or dropped | Easier? | Cost / check |
|---|---|---|---|---|---|---|
| a1 | The gap is asked on the tr F^2 sector of every volume-first limit at g. | SK L27-31; FL L164 | T | Asked for one limit only: the seed is needed along one sequence (FL 2.4 item 1). | A little: no uniformity over W_K(g). | Free; FL already says it. |
| a2 | The gap is asked for the continuum theory, not for a lattice theory at a fixed bare coupling. | brief; FL 2.3 | T | A fixed-beta lattice gap in the window would be a theorem short of the target. | Yes, but off the path unless it is stable under the account's changes of the weight. | A fixed-beta proof costs the same order-one input, without (S-mid). |
| a3 | The seed must hold with a universal margin (1/5041) at a time equal to half the side. | FL L114-118; I4 | M (Theorem S) | Another criterion at one size, with another shape or margin, would do if it has its own step theorem. | Unknown. | A new step theorem; the lane has three seeds and (ES) (I5). |
| a4 | The target does not ask for confinement. | AS row 15; C1 | T | - | Yes: only a massless branch must be excluded. | Free. Consequence: finite-group tests do not bind the target (C3). |

### 4.b Formulation (the brief's list is b1 to b6)

| ID | Assumption | Where | Kind | If changed | Easier? | Exact cost; does it hold? |
|---|---|---|---|---|---|---|
| b1 | The action is Wilson's. | I1; the account | M (the account) | (i) Heat-kernel weight: the character coefficients become d_j exp(-t C_j/2) and each face carries an exact two-dimensional theory (semigroup law in the area). (ii) A weight with no Z_2 monopoles (the sign of tr U_p has no odd cube): the centre part of the links becomes, for each fixed SO(3) part, an unfrustrated Z_2 gauge theory with couplings beta abs(s_p) >= 0, so Griffiths inequalities hold for it conditionally. (iii) Mixed fundamental-adjoint: worse (I24). | (i) and (ii) add exact structure. Neither is known to remove (S-ir). | The account covers the Wilson action only (READ by grep of YM4_1400.tex at the local copy: no other action is named; the words Villain, Manton, heat kernel do not occur). So any change of action costs the whole chain of the account for the new weight, plus (TM) for it. Does (TM) hold? For (i) yes in principle (a positive class function with positive character coefficients; not written in the lane as far as the open files show). For (ii) the cube constraint is reflection-symmetric and local; (TM) is plausible and not written. |
| b2 | The transfer operator is one lattice step along an axis of a periodic torus. | I3; AS rows 54, 55 | M | (i) The crossed frame: the same ratio is a difference of two ground energies, an upper bound, a variational statement (C2). (ii) Hamiltonian (continuous time): same spectrum questions, with the Kogut-Susskind operator; kinetic term diagonal in spins, Casimir at least 3/4 on each half-integer edge. (iii) Free or fixed walls: lose (TM-c) as a symmetry statement. | (i) changes the kind of statement (upper bound instead of lower bound). | (i) is free: (TM), (TM-tw) cover it (I3, AS row 58). (ii) costs a time-continuum limit of the account, not available. |
| b3 | The centre flips and the six twist bits are the flux variables. | I2, I6 | M | (i) Read the twist as an antiperiodic boundary condition for the Polyakov line of direction 1 in direction i: the flux half is "a three-dimensional Z_2-odd spin system of lines of length a is in its high-temperature phase". (ii) Interpolate the centre element through conjugacy classes: Z(phi) with the class of exp(2 i phi sigma_3) inserted on the plaquettes of Sigma, phi from 0 to pi/2; exact, positive, and non-topological for interior phi. (iii) Split each link into its Z_2 part and its SO(3) part. | (i) gives a second small number candidate: the one-step factor r_(1/2) to the power a_i. (ii) and (iii) are exact rewritings. | All three are exact identities and cost nothing. Whether any of them yields an estimate is the question of Step 8. |
| b4 | One scale: the criterion is verified once, at one physical size. | I4; SK L598 (rule) | M / H | Many scales: an induction over block scales through the order-one zone, with an invariant that the step reproduces. | Only if a reproducing invariant exists that is not group-blind and does not need worst-case exteriors (I10, I11). | Needs a mixing statement for the fine field given the block field at order-one coupling (I11 names it PIN-MIX). Open. |
| b5 | SU(2) pure gauge theory is attacked directly. | I1 | H | (i) Add a fundamental Higgs field of fixed length: for a large hopping parameter the theory has a convergent expansion at every beta (Osterwalder and Seiler, Fradkin and Shenker; recalled). The pure theory is the limit of zero hopping. (ii) Quotient or extend the group: SO(3) times Z_2 (as b1 (ii), b3 (iii)). (iii) Finite subgroups as approximants: 2I agrees with SU(2) to high order in the character expansion below its freezing point (BELIEF from numerics). | (i) moves the wall to a path in a two-parameter plane: the seed set is open (AS row 51), and the missing piece is again an a priori bound along the path (C5). | (i) costs the account for the Higgs model, or an exact identity that removes the Higgs field at the end (I11 names a Higgs-line identity, Theorem HL, unchecked). (iii) costs a comparison theorem between 2I and SU(2) at order one; none is known to me. |
| b6 | Euclidean lattice measure. | I1 | H | Hamiltonian or stochastic (Langevin) dynamics. (G2) is the Langevin form; it is equivalent to a volume-uniform Langevin gap (0.1 item 3). | No: an equivalent restatement. | Free as a restatement; no gain known. |
| b7 | Periodic tori with four sides from {a, 2a}. | 0.1 item 3 | M (crossing, fusion) | Anisotropic tori with two short transverse sides: the twist observable then has small variance in the transverse plane. | Possibly for clustering arguments; but a short side risks the critical slab (SK Section 3). | The step theorems hold for every shape (I4); the seed threshold changes with the shape (AS row 32). |
| b8 | Haar measure, compact group, strictly positive density. | AS row 66 | T (the model) | - | - | - |
| b9 | The half-integer edges or faces of the character expansion carry the flux; their weights are real and one known term is negative. | I6, I25 | M | The sign of a closed surface with one half-integer spin is (-1)^(Euler characteristic) (ARGUED here: the integral of chi_j(g^2) is the Frobenius-Schur indicator, -1 for half-integer j; a surface with k crosscaps gets d_j^(2-k) times indicator^k). So the signs come only from pseudo-reality and only on surfaces of odd Euler characteristic. U(1) has no such terms at all; SO(3) has no signs. | Unknown. It is a property U(1) lacks; Q_8 and 2T share it. | Free. The general (multi-spin, branched) sign rule is not derived here. |

(continued in 4.c)

### 4.c Reduction

| ID | Assumption | Where | Kind | If wrong or dropped | Easier? | Cost / check |
|---|---|---|---|---|---|---|
| c1 | (GAP) follows from (SEED-FP) with the account. | FL 2.5 | M | Steps (c), (e), (f) are argued and unchecked. If one fails, the finish line moves; the order-one problem stays. | No. | A check of FL 2.5 by another model. |
| c2 | The seed is reached through (ES): a small even sum and a small defect, the defect through the flux half (FQ). | I5, 0.1 | M | A direct proof of (ES) need not separate SU(2) from frozen finite groups (C3): both numbers of (ES) are small there too. | It removes two of the four fact tests for that sub-route. | Free as logic. No direct tool for (ES) is known. |
| c3 | The flux half is studied at a fixed bare coupling in the window as a proxy. | brief; AS L245 | H | A fixed-beta result is off the path. A proof whose input is stable under the account's changes of weight would be on it. | - | State every order-one lemma for a class of weights, not for one weight. |
| c4 | The surface (character) expansion is the representation of the odd sector. | 0.1 (J2)-(J4), I6 | H | Magnetic frame: the same number is a twisted ground energy (C2). Spin-system frame: an antiperiodic boundary condition for the Polyakov line (b3 (i)). | Changes the statement type. | Free. |
| c5 | The block law of the effective field is not used (its reflection positivity is not known). | FL 2.3 item 2 | M | If a block map kept reflection positivity at planes that cut no block, Theorem S could run on the block law. | Unknown. | For a kernel that factorizes across the mirror and commutes with it, positivity of the block law at that mirror follows in two lines (ARGUED: put F(U_+) = integral of G(V_+) kappa(V_+ given U_+); then E[theta G G] = E[theta F F] >= 0). The account's averaging uses blocks centred on coarse sites, so coarse links cross every mirror between blocks; the two-line argument does not apply as it stands. |
| c6 | The seed is a trace over all states with multiplicity. | AS row 33 | M | - | - | - |

### 4.d Discard tests

| ID | Test | Where | If the test is wrong or too strong | Check |
|---|---|---|---|---|
| d1 | "It also holds for U(1)": kills. | brief; SK Section 3 | Valid only in the form of Step 6: U(1) refutes a tool only if the hypothesis is true in U(1) and the conclusion false. | Step 6. |
| d2 | "It also holds for Q_8 or 2T": kills. | brief | Binds only statements whose conclusion is false for frozen Q_8 or 2T. The target and (ES) are true there (C3, belief for the finite groups). So d2 does not bind a direct route to (ES). | Step 6. |
| d3 | "No fixed small number reaches order one." | brief | Too strong if a number exists that is small because of the size of the box (for example a one-step factor to the power of a side) or because of arithmetic at order one (high-spin coefficients). | Step 6, Step 8. |
| d4 | "Worst-case exterior bounds have ceilings." | I10 | Says nothing about averaged or typical statements. | - |
| d5 | "A one-way step for a torus quantity is not queued." | SK L598 | A step with an exact invariant that is not a torus free energy is not covered by the rule. | - |
| d6 | "Soft block step then high-temperature theorem is circular for the seed." | I11 | Circular for the partition function only; not for a statement that needs no vacuum constant (for example a ratio of twisted partition functions, which an exact centre-covariant step preserves). | Step 6. |

### 4.e Beliefs

| ID | Belief | Used where | If wrong |
|---|---|---|---|
| e1 | Wilson SU(2) has no transition in beta. | everywhere | Then (NOCRIT) is false and the target fails at that coupling; the continuum target could still hold. |
| e2 | For SU(2) every seed is a confinement statement; the full seed is false. | SK L582, L584 | If the continuum theory had light magnetic flux instead, the full seed would be the right one. No evidence for it. |
| e3 | The effective weights at order one are "not the Wilson weight, and nothing known bounds their distance from it". | FL 2.3 | If the trajectory of effective weights stays in a small explicit neighbourhood of a known family, a fixed-family proof would be on the path. |
| e4 | The wall is the gauge twin of the two-dimensional O(3) wall (C7). | 3.3 | If the gauge problem has structure the spin problem lacks (twists are isolated; flux is Z_2-valued), it could be easier. |

### 4.f Working rules (questioned on paper only; all obeyed)

| ID | Rule | Not used: what a different rule would give |
|---|---|---|
| f1 | No computer-assisted step. | A fixed-beta seed is a finite statement; a certified computation could not reach the continuum trajectory anyway. |
| f2 | Port the account; do not redo it. | A change of action (b1) breaks this rule's economy: it costs the whole chain. |
| f3 | An author brief names its means (M1) to (M4) or a fifth. | - |
| f4 | Never call a route the only or last one. | - |

### 4.g Ranking (by how much the problem changes if the assumption is dropped)

1. b4 (one scale versus many). The lane would look for an invariant that an exact step reproduces at order one, instead of one verified inequality.
2. a4 with c2 (the target is not confinement). The lane would attack (ES) directly and drop the finite-group tests for that sub-route.
3. b3 (the twist as a variable). The lane would use the crossed frame (an upper bound, variational) or the spin-system frame.
4. b1 (the action). The lane would trade the Wilson weight for one with exact structure, at the price of the account's chain.
5. d3 (no small number). The lane would look for numbers that are small because of the box side.

None of these changes an owner decision by itself. b1 would (it breaks f2).

Status: S4 table done. Fresh candidate routes with their CRUX lemmas: next append.

### 4.h Fresh candidate routes, each with its CRUX lemma (written before the closed files open; novelty is judged in Step 5)

Notation: R_beta(n) is the twist ratio Z^(m+v)/Z^m of the consumer on a torus with sides from {n, 2n} at bare coupling beta.

**R1. Asymptotic freedom as an inequality (drops b4, uses d6).** CRUX lemma (AF-step): there are c > 0, beta_1 and n_0 such that for every beta >= beta_1 and n >= n_0, R_(beta + c)(2n) >= R_beta(n). With a base R_beta(n_1) >= 1 - eps for beta in [beta_1, beta_1 + c], induction gives the flux half at coupling beta_1 + k c on the box 2^k n_1, for every k. Fact tests. U(1): the Coulomb twist ratio is scale-invariant and decreases in beta, so (AF-step) fails for every c > 0 and holds only at c = 0. Good: the lemma is false for U(1), and c > 0 is exactly the non-abelian content (the true shift per halving of the spacing is about 0.257 in beta, recalled one-loop value 2 b_0 log 2 times 4). Finite groups: fails across the freezing point. Small number: none is needed at order one; the base carries it. What it costs: a proof of a one-sided comparison between a blocked fine theory and a coarse Wilson theory; and a base beyond beta = 2/3. What would prove it: an order on plaquette weights for which the twist ratio is monotone, together with a one-sided bound of the exact effective weight in that order.

**R2. A direct criterion for (ES) that never mentions flux (uses a4, c2).** CRUX lemma: none stated; I found no tool that bounds the even thermal sum at order one. Recorded as an empty route, so that Step 6 can say what a tool would have to be.

**R3. The thick vortex as a trial vector (b2 (i), C2).** CRUX lemma (TV): there is a family of Markov kernels K_n from periodic to twisted configurations of the spatial box, with E[S_tw after K_n] - E[S] plus the entropy cost at most C exp(-kappa n). First obstruction, PROVED here: let g = exp(i alpha n.sigma) be a fixed element and insert it on one link of a plaquette. In any gauge-invariant state, E[tr(.. U_e g ..)] = cos(alpha) E[tr(.. U_e ..)], because the average of h g h^(-1) over h in SU(2) is (tr g/2) times the identity. So a rotation by an angle alpha about a fixed colour axis costs 1 - cos(alpha) of the plaquette mean on every plaquette through the link: the cost is of order alpha^2 per link, not (d alpha)^2 per plaquette. Spreading the centre flip over w links therefore costs area/w, not 1/w^2: a thick vortex made of rotations about a fixed colour axis is no cheaper per unit sheet area than a thin one, in any gauge-invariant state. In U(1) the same insertion costs (d alpha)^2. So the abelian mechanism of spreading is exactly what SU(2) lacks, and a trial vector needs a gauge-covariant colour direction with small covariant derivative. None exists in a state without long-range order. The route stops here.

**R4. The unfrustrated centre (b1 (ii)).** CRUX lemma (QA): for the weight with no Z_2 monopoles, R = sum over SO(3) sectors of the annealed sector weights; the Z_2 part is a ferromagnetic Z_2 gauge theory for each SO(3) field and obeys Griffiths inequalities. Identity, PROVED here for the Wilson weight too: R = E[r(U)], where r(U) = Z_v(U)/Z_0(U) is the twist ratio of the Z_2 gauge theory with couplings J_p = beta s_p(U) on the centre orbit of U. (Average the density over the 2^(number of links) sign changes of the links; Haar measure is invariant.) Obstruction, ARGUED: r is not concentrated; typical fields give r far below 1 and fields in the twisted SO(3) sector give r far above 1; the statement R near 1 is a balance of sector weights, which is the original problem in SO(3) language. The route gives monotonicity of r in the Z_2 couplings and nothing on the sector weights.

**R5. The Higgs plane (b5 (i)).** CRUX lemma (HP): along some path from the large-hopping region to the pure theory, the seed set (open) is also closed. Obstruction, BELIEF plus a recalled theorem: at beta = infinity the fixed-length model is the four-dimensional O(4) spin model, which has a critical hopping parameter; a line of transitions or sharp crossover leaves that point into finite beta. So the corner of the plane that contains the pure theory at large beta is not free of critical points, and no monotone path is known.

**R6. Localization by linear tilts (d3, d4; a technique from outside the lane's vocabulary: stochastic localization and the multiscale Bakry-Emery criterion of Bauerschmidt, Bodineau and Dagallier; Eldan; Chen and Eldan; all recalled).** Fact, PROVED here in two lines: for every gauge-invariant probability measure on SU(2) links, viewed as unit vectors of R^4, Cov(U_e, U_e') = delta_(e e')/4. (Two distinct links have an endpoint that is not shared; averaging over the gauge group at that site kills the mixed moment; and E[x_a x_b] = delta_ab/4 on the unit sphere of R^4 by invariance under left multiplication.) So the covariance of the untilted measure carries no information. CRUX lemma (TC): sup over all external fields h of the operator norm of Cov under the measure tilted by exp(sum_e <h_e, U_e>) is finite, uniformly in the volume. A tilt is a frozen fundamental Higgs field in unitary gauge. Obstruction: the sup contains the homogeneous Higgs model at every hopping parameter, hence its critical points (R5), and inhomogeneous tilts can freeze all links outside a film. So (TC) is false wherever the Higgs line or a film is critical. Recorded as a technique that the tests kill, with the reason.

**R7. Pseudo-reality as the non-abelian input (b9).** SU(2) = Sp(1). The sign rule (-1)^(2 j chi) of b9 is the "negative dimension" rule: Sp(2n) invariants are O(-2n) invariants (Parisi and Sourlas; Cvitanovic; recalled). CRUX lemma: none yet. It is a lens: it says the half-integer sector behaves as a fermionic loop or surface gas of fugacity -2 per closed component. U(1) lacks it; Q_8 and 2T share it, so by C3 it could serve a direct route to (ES) and not the flux half.

**Which of these could carry the difficulty.** Only R1 has a CRUX lemma that (a) is false for U(1) for a structural reason, (b) needs no small number at order one, and (c) is a statement about ratios of twisted partition functions, which exact centre-covariant block steps preserve. R3, R4, R5, R6 stop at obstructions written above. So the real attempt of Step 8 goes to R1 first. The second attempt goes to the obstruction side: the film statement behind R6 and d4, as a corrected filter.

Status: S4 done (table, ranking, seven fresh routes; three short facts proved here: the cos(alpha) insertion rule, R = E[r(U)], and the link covariance identity).

---

## Step 5. Compare with the earlier work (closed list opened)

**What I opened.** BR = D/library/gap-brainstorm-max.md (row 859; Claude Fable 5.2 max for ideas 1-52, Claude Opus 5.5 max from L414): L271-343 (all 52 ideas), L344-455 (settling), L468-513 (G1-G21), L603-699 (top five, attempts, novelty, summary). D/library/gap-crux-exercise-max.md (row 743/858): 60 lines, stops at Step 1. D/library/gap-es1-opus.md L40-112 (Theorem V, Theorem LB). Grep with line output over D/library/gap-*.md, D/library/prior/*.md and FIN for the objects of each of my items (two wordings each; patterns in the commands of this session). Main: git grep on origin/main for three wordings (no hit). PR branches: listed by name only; none opened. FIN rows 697-859 and 876-877: not read beyond the RESULT text used above and grep hits. D/library/exercise-skill-v2.md, gap-crux-skeleton-max.md (row 863), gap-exit-max.md (row 861): not opened beyond FIN RESULT text. So every "new" below means "not found in the searched scope", and the scope is stated per item.

| My item | In the earlier work? | Where | Scope of a "new" mark |
|---|---|---|---|
| C1, F1, a4: the target is not confinement; any seed gives it | yes | SK L574-584 (three seeds; Z_2 test binds the periodic seed only); AS row 15 | - |
| C3, d2: finite-group tests bind only the flux half in its confining form | partly | SK L580 states it for Z_2; BR L512 and FIN L937 keep "must fail for frozen 2T" for the parity statement only. The explicit sentence "a direct proof of (ES) need not separate SU(2) from frozen 2T" was not found | grep "frozen" with "(ES)" in gap-*.md: no hit in one line; not a full read |
| F2: the odd gap is at least the full gap (ground-state transform) | yes in substance | SK L64 region and AS row 64 (seed = glue half + flux half); BR G1 L470 | - |
| F5, C5, R5: Hellmann-Feynman continuation, linear law, Gronwall | yes | BR idea 46 L330; BR G8 L484; BR 4b (3) L619-622 "(NOCRIT-HF)"; BR L686 "variant; the Gronwall continuation is folklore". The square-root bound with the volume factor (my F5) was not found; it is a two-line consequence | grep "Hellmann" in gap-*.md and FIN: 10 files; opened BR only |
| F6, C2, R3: crossed frame, twisted ground energy, trial vector | yes | BR G10 L488 ("a variational upper bound needs a twisted trial state; thin trials cost order L_2; thick trials are Wall F") | - |
| R3's proved fact: a fixed-axis rotation costs the square of the link angle | yes, same proof | BR idea 7, L356: "PROVED here (two lines) ... the mean action change is beta <x> times the sum of SQUARED LINK ANGLES, not of their curl" | - |
| F7, C7, e4: the two-dimensional O(4) or O(3) twin | yes | BR idea 22 L303 and L371 (with a dictionary proved) | - |
| b3 (ii): interpolation through conjugacy classes | yes | BR idea 6 L282; BR G2 L472 ("Gukov-Witten defect family", with the character formula) | - |
| b3 (i): Polyakov-line spin system and the factor r^(a_i) | partly | FIN L949 (row 872: the wrapping line, "the only state-blind bound loses a volume factor", refuted in part by row 873) | - |
| R4: R = E[r(U)], SO(3) times Z_2, Griffiths for the centre part | yes | BR idea 15 L293, idea 38 L411, idea 52 L451 (tower property in Nishimori form), G5 L478; Froehlich 1979 and Mack-Petkova credited there | - |
| R5: Higgs plane | yes | BR idea 33 L318, L408; FIN L938 (Theorem HL, row 861) | - |
| R6: stochastic localization; link covariance identity | yes / partly | BR idea 4 L280, G14 L496 (plaquette tilts; "weak"); BR idea 48 L332 (Elitzur: the mean Hessian is diagonal). My version tilts links (a frozen Higgs field) and notes Cov(U_e, U_e') = delta/4; that identity is the same Elitzur argument. The observation "the sup over tilts contains the critical Higgs point and frozen films, so the criterion is false there" was not found | grep "localization" in gap-*.md: 23 files; opened BR only |
| R7, b9: pseudo-reality sign, Sp(1), negative dimension | partly | D/library/gap-means-max.md L65-102 per gap-z2parity-astra.md L112 ("the pseudoreal Haar sign"); gap-means-max-check.md L462 ("Set N=2, so Sp(1)=SU(2)"); prior/gap-lit-assoc.md L109, L141 (Frobenius-Schur sign). The O(-2) reading as a lens was not found | grep "negative dimension", "O(-2)": no hit |
| R1: (AF-step), a one-sided step-scaling inequality | yes | BR idea 8 L284, idea 36 L321 ("a rigorous one-sided step-scaling INEQUALITY is the form idea 8 should take"), idea 40, (MON') L652; SK L598 (rule against one-way steps); D/library/gap-phys-seed.md L351-384 ((MONO-Delta), Proposition MB: base at weak coupling, a sign condition, (Z-UNB)) | - |
| b2: concavity of sector ground energies in a box length | yes | D/library/gap-skeleton-max.md L130: "the flux energies are concave in the length: at most linear growth" | - |
| d4, film obstruction (pinned exteriors can freeze a film, and films order) | partly | SK L63 (K6, the slab test); D/library/gap-arealaw-opus.md L486 ("the slab is the 3D O(4) model. That model orders above a critical coupling near 0.94"); brief (row 839). The word "film" has no hit; the content is there for layers | - |
| The two-column covariance identity 1 - R^2 = Cov(X_A, X_B) (found during Step 4, not written into the table) | yes | BR idea 43 L327 and L434-436 (proved there, with the correct reading: a conserved-charge variance) | - |

**Corrections to my Steps 2 to 4 from this comparison.**
- 4.h "three short facts proved here": all three are in BR (L356; L451; L332) with the same proofs. They are re-derivations, not new. Credit: row 859 (Claude Fable 5.2 max, Claude Opus 5.5 max).
- R1's claim "only R1 has a CRUX lemma with (a), (b), (c)" stands as a description, but R1 is the lane's idea 8 / (MON') / (MONO-Delta) family. BR L659 states the common finding: every such reformulation has "a group-blind propagation step and a group-selective seed" in the order-one band.
- The stronger form in the earlier work: Theorem V and Theorem LB (gap-es1-opus.md L58-112, checked by row 753 per SK L634) make "the defect is the weight of the heavy flux sectors" exact. I use them and do not re-derive them.

**What the fresh pass added (not found in the searched scope).**
1. The explicit logical point that a direct route to (ES) is exempt from the finite-group tests (C3). Small.
2. The tilt form of a localization criterion and the reason it dies (R6). A discard with a reason, small.
3. The volume-dependent square-root law of F5. Small.

**What it only found again.** Everything else: the target is not confinement; the crossed-frame variational reading; the squared-angle obstruction to thick vortices; SO(3) times Z_2 with Griffiths for the centre; the Higgs plane; Hellmann-Feynman continuation; step-scaling inequalities; the two-dimensional twin; class-function defect families; concavity of flux energies.

**Reading (argued).** Two max runs of the same model, with the attack files closed, produce the same list. SK L18 says it: "Two runs of one model are two samples." The fresh list is saturated at this depth. So the rest of this run does not add a 53rd framing. It audits the filters (Step 6), then spends the attempts (Step 8) on proving something at one named crux, not on restating it.

Status: S5 done. Almost all of S3 and S4 is found again; three small additions; the remaining budget goes to Step 6 and to proofs.

---

## Step 6. The blockage: discard tests and set-aside methods

### 6a. Methods set aside (from BR and SK; "digest" = taken from those files, not read first-hand)

| # | Method | Reason given | Where | Kind of reason |
|---|---|---|---|---|
| 1 | Worst-case Dobrushin, single-site and vertex blocks | ceilings 2/3 and 0.775 | brief; FIN L938 (digest) | needs a small number |
| 2 | Background-uniform one-layer twist bounds | fail above beta_W = 1.0109 | brief, row 839 (digest) | fails a test (flat background is a ferromagnet) |
| 3 | Annealed block condition (AN1) | equivalent to the worst case | brief, row 845 (digest) | circular |
| 4 | One-way step for a torus quantity; step-scaling couplings | each step as hard as the seed; fails where two confining phases coexist | SK L553, L598 | open premise |
| 5 | (MONO-Delta) | false for the ordered Ising model, so not a property of the class | gap-phys-seed.md L371-373 | fails a test |
| 6 | Linear (ES-1) | false: defect of order X^9 against even sums of order X^12 | SK L632 | refuted |
| 7 | Wilson-loop association, (EP) | false for SU(2) (Theorem EP-NO) | SK L638 | refuted |
| 8 | Fixed-radius loop-equation certificates | cannot reach (ES) at large size | SK L640 | wrong quantity |
| 9 | Full-L2 block certificate PA | fails at weak coupling by a gauge corner | SK L642 | refuted |
| 10 | Soft block step then high-temperature theorem | circular for the seed | FIN L938 | circular |
| 11 | Spin-5/2 filter plus (HS) as carrier of (E17) | negative verdict of row 872 FAILS in check 873; so not set aside | FIN L950 | (verdict withdrawn) |
| 12 | Peierls or strand counting on half-integer edges | needs density below 0.2135; guide value 0.267 | BR L663-666 | needs a small number (rests on a GUIDE) |
| 13 | Flux half from glue half by clustering | the tube covariance is a conserved-charge variance | BR L434-436 | wrong quantity |
| 14 | Thin Z_2 lift with Griffiths inequalities | frozen at order one (mean coupling 1.5 against 0.44) | BR L411, L478 | needs a small number |
| 15 | Vacuum Bakry-Emery, (G2) | equivalent to the Langevin gap | FIN L889 | circular |
| 16 | Stochastic localization along plaquette tilts | order-one covariances | BR L496 | needs a small number |
| 17 | Thick vortex by field-independent spreading | cost is the square of the link angle | BR L356 | refuted as a method |
| 18 | Hierarchical and Migdal-Kadanoff lattices | group-blind: they confine 4D U(1) too | BR L409 | fails a test |

Not a complete list: I did not open rows 763 to 858 one by one. Missing rows are "not re-judged".

### 6b. First principles on the blockage

A tool must verify one inequality between partition functions of boxes of side at least about 13 correlation lengths, uniformly along the trajectory. Only three kinds of statement can do that: (K1) a statement with a small number at that scale; (K2) an induction over scales whose step is true for a structural reason; (K3) an exact formula. For (K2) the step must be selective somewhere: if every step is blind (true in the whole class of reflection-positive models with a centre), then the seed is selective and sits where the model first differs from a scale-invariant member of the class, which is the band of order-one effective coupling. The least a tool must use is the non-abelian Lie algebra at weak coupling (the sign of the one-loop coefficient) or one of the items of C4 at order one.

**The blockage in one sentence.** Every engine found is blind, so its seed sits in the order-one band; and the one selective fact that is provable today (asymptotic freedom at small coupling) has no engine that carries it across the band.

### 6c. The discard tests in their logical form

| Test (model M') | Class K | The exact T that fails in M' | How the failure is known | What a tool must use to pass | Binds from |
|---|---|---|---|---|---|
| U(1) Coulomb | RP gauge theories with a Z_2 subgroup of the centre | (GAP); (G_ev); every seed; (E17) | THM, published (Guth; Froehlich-Spencer), recalled; twist form by row 786 (lane, Villain, beta >= 2^14 per FIN L889) | the non-abelian structure | proved only at very large beta; at order-one beta (Coulomb branch 1.01 to a few) it is a BELIEF from numerics |
| Z_2 at large beta | same | the periodic seed; (E17); (FQ); HA | THM (lane, Peierls, beta above 2.191 per FIN L947); (G_ev) is true there | a tool for the periodic seed must use connectedness | beta above 2.191 (proved) |
| Frozen Q_8, 2T | same | the periodic seed; (E17) | BELIEF: transition couplings from numerics (AS header: Hartung et al., Table IV); BR idea 18: a Peierls proof needs large beta | as for Z_2 | at order one only as a belief |
| Critical slab (K6) | boxes with one short side | decay uniform in the width | THM for existence of an ordered thin slab at large beta (Borgs-Seiler, recalled); the critical widths at order one are a BELIEF | the long sides of the seed box | - |
| Ordered Ising | RP spin models | (MONO-Delta) | GUIDE (exact transfer matrices) | - | - |

Three points follow from the valid form.

1. **The finite-group tests are constraints on proofs of the flux half only.** T false in frozen 2T means: a hypothesis H that implies the periodic seed is false for frozen 2T. For T = (ES) or (G_ev), T is true in frozen 2T (belief) and in Z_2 at large beta (lane, argued in SK L600). So these models say nothing about a tool for (ES). The brief's wording "the binding finite-group tests at order one" is too strong as a general filter: valid for routes through (E17), (FQ), HA, EXC; void for a direct route to (ES). What comes back: nothing concrete, because no direct tool for (ES) is known (R2 is empty). It matters for the form of any future brief on the even half.
2. **The finite-group tests at order one rest on a BELIEF.** Their theorem-grade form is Z_2 above 2.191. A route should be tested against that theorem first.
3. **A pass is no support.** (E17), HA, (C2), EXC, (CVX) below all "pass U(1)". That says only what their proofs must use.

### 6d. Verdicts re-judged

| # of 6a | The verdict assumes | Valid in corrected form? | If not: what comes back |
|---|---|---|---|
| 1, 2, 3 | worst case over exteriors, any region shape | valid as reported; not re-derived. Reason in one line (argued): a pinned exterior can freeze everything outside a thin layer, and thin layers order (gap-arealaw-opus.md L486) | - |
| 4 | a first-order (monotone) step | valid in range: it does not cover a second-order condition (convexity along doublings) whose base is at weak coupling. That form goes to Step 8 as route CX | route CX; it is of the same kind as (MONO-Delta), a sign with no small number |
| 5 | (MONO-Delta) as a class property | valid; it says a proof must be selective, not that the statement is false for SU(2) | - |
| 10 | the seed needs the vacuum constant | valid as reported; not re-derived. With an exponentially local landed action the circle opens; that is PIN-MIX, open | - |
| 12 | independent-like strands | valid only as a statement about support counting; it rests on a GUIDE number | - |
| 13 | bounding the odd weight itself by clustering of flux-neutral observables | valid for that use. Too strong if read as "the even gap gives no information on flux": the even gap can still control how flux free energies change when the transverse sides double (Step 8, statement (TS-theta)). Argued, not proved | a named open statement, not a tool |
| 16 | plaquette tilts | valid as reported. The link-tilt variant is judged in Step 8 (route LT) | - |
| 6, 7, 8, 9, 14, 15, 17, 18 | - | valid as reported; not re-derived | - |

Where the corrected verdicts matter: 6c point 1 is on the path only if a tool for (ES) appears. The re-reading of 4 and 13 is on the path of the flux half.

Status: S6 done. One filter narrowed (finite-group tests: flux half only; belief-grade at order one). No verdict shown wrong.

---

## Step 7. Routes: generate, try to kill, rank

No subagents. The "independent passes" are Step 4.h (fresh, files closed) and the lane's own 73 ideas (BR), which I use as the second sample. Sources of routes: the ranked assumptions of 4.g; 6b; the two re-read verdicts of 6d.

**Outside view (recalled; nothing downloaded in this run).** One method family was not found in the lane by grep ("marginal triviality", "Aizenman" with "Duminil": no hit): the proof of marginal triviality of four-dimensional Ising and phi^4 fields by Aizenman and Duminil-Copin (Annals of Mathematics 2021). It is a proof at the marginal dimension with no small parameter: a logarithmic gain per scale, from a multi-scale argument on intersections of random currents. It is the one known rigorous example of the kind of engine 6b asks for. It needs a positive geometric representation with a switching lemma. SU(2) has a signed surface expansion (I25), so the method does not transfer as it stands. Lens considered and found empty for now; it is worth one reading row (Step 9).

| Route | Family | Assumption changed | What you would have to believe | Kill verdict | Terminal obligation | Cost | First artifact |
|---|---|---|---|---|---|---|---|
| E | selective engine for the flux half: exact worldsheet doubling plus a spreading exponent | b4, 6d row 13 | when both transverse sides double, the flux free energy falls by a factor below 4 | wounded: its seed is of order one (Theorem E below), so it does not leave the band; (TS-theta) is open | (TS-theta) for all sizes above the seed | open; no tool | Step 8, attempt 1 |
| CX | second-order sign condition with a weak-coupling base | 6d row 4 | the dimensionless flux free energy and the dimensionless gap are convex along doublings | wounded: convexity is false in the class near an ordered critical point; no blind proof | (CVX) and a two-loop base in small twisted volumes | the base is weak-coupling work outside the account | Step 8, attempt 1b |
| LT | link-tilt localization (Fradkin-Shenker as a criterion) | d3, d4 | the link susceptibility of the SU(2)-Higgs family is bounded along the tilt path at the given beta | wounded: moves the wall to the Higgs crossover band at the same beta; false above the end point of the Higgs transition line (belief) | (TC-typ) | adaptation of a recalled theorem to sphere-valued links | Step 8, attempt 2 |
| R2 | direct (ES) | a4, c2 | - | empty | - | - | - |
| lane (1) | decoder plus chessboard (BR 4b) | - | - | not re-judged here; its seed is in the band (BR L645) | (SEED-DEC), (TOP_j) | - | - |
| lane (2), (3) | (MON'), (NOCRIT-HF) | - | - | not re-judged; same band | - | - | - |

**Rank (change if it worked, over cost to find out).** 1: E. 2: LT. 3: CX. None is past the wall. None is called the only route.

Status: S7 done.

---

## Step 8. Real attempts

Budget note: the brief gives no hour budget; I stopped each attempt at the first statement that needs an order-one input. Before each attempt I searched the lane for the statement (grep lines in Step 5 and below).

### 8.1 Attempt 1: route E, a selective engine for the flux half

**Objects.** Torus n = (n_1, n_i, n_j, n_k), every side at least 3. v = v_(1i). Z^0, Z^v the periodic and twisted partition functions (any fixed admissible spatial background m may be added to both). Z^+ = (Z^0 + Z^v)/2, Z^- = (Z^0 - Z^v)/2, q = Z^-/Z^+, F = -log q. By I2, 0 < Z^v <= Z^0, so 0 <= q < 1 and F > 0. In frame 1, with T_1 the transfer operator of the box (n_i, n_j, n_k) and C_i the centre flip, Z^(+-) = Tr(P_(+-) T_1^(n_1)), P_(+-) = (1 +- C_i)/2 (I3). So q is the weight of the C_i-odd states over the weight of the C_i-even states: q = p/(1 - p) with p of I6.

**Lemma WS (time doubling; PROVED; found again: it is Lemma A (a) with (b) of Theorem F, gap-crux-restate.md L240-244).** Let s_+(n_1) = Z^+(n_1)/lambda_0^(n_1) - 1 >= 0 be the thermal sum of the C_i-even part. Then q(2 n_1) <= q(n_1)^2 (1 + s_+(n_1))^2.
Proof. T_1 P_- is positive and trace class, so Tr (T_1 P_-)^(2 n_1) <= (Tr (T_1 P_-)^(n_1))^2. The ground state is C_i-even (it is positive and C_i maps it to a positive top eigenvector), so Z^+(2 n_1) >= lambda_0^(2 n_1) = Z^+(n_1)^2/(1 + s_+(n_1))^2. Divide. QED
By exchange of the axes 1 and i the same holds for n_i, with the thermal sum s'_+ of the C_1-even part of the transfer operator in direction i. Two uses give

  (WS2)  F(2 n_1, 2 n_i | n_j, n_k) >= 4 F(n_1, n_i | n_j, n_k) - 6 log(1 + s),

with s the larger of the two thermal sums that occur. So at fixed transverse sides the flux free energy grows by the factor 4 of the area, up to an entropy term. This is exact and blind.

**Lemma TD (transverse doubling; PROVED here; elementary).** Let T_0 and T_v be the transfer operators in direction j of the box (n_1, n_i, n_k), without and with the twist v (both positive and trace class by (TM-tw); v is a spatial twist of that frame). Let S_0, S_v be their full thermal sums at time n_j and S = max(S_0, S_v). Then

  q(n_1, n_i | 2 n_j, n_k) <= 2 (1 + S)^2 [ q(n_1, n_i | n_j, n_k) + S_v/2 ].

Proof. Put a = Tr T_0^n, b = Tr T_v^n, A = Tr T_0^(2n), B = Tr T_v^(2n), n = n_j. Then 0 < b <= a, A <= a^2, B >= tau_0^(2n) = b^2/(1 + S_v)^2, A >= a^2/(1 + S_0)^2. So A - B <= a^2 - b^2 + b^2 (1 - (1 + S_v)^(-2)) <= (a - b)(a + b) + 2 S_v b^2, and A + B >= (a^2 + b^2)/(1 + S)^2 >= (a + b)^2/(2 (1 + S)^2). Divide, and use b <= (a + b)/2. QED
Reading. The factor 2 is the entropy of the position of the flux tube: with S_0 = S_v = 0 the exact law is q(2n) = 2 q(n)/(1 + q(n)^2) (PROVED by the same algebra with A = a^2, B = b^2). The additive term S_v/2 is the weak point: it is the thermal sum of the crossed frame, of order (volume) exp(-m n_j), and at large size it is far above q itself. So Lemma TD controls the transverse step only while q is at least of the order of the crossed thermal sums. This is the mechanism inside Theorem S (which works with the full periodic sum, where the flux weights are part of the sum); I claim no new content for it.

**The selective statement.** (TS-theta): there are theta < 4, a constant C and n_0 such that for all sides at least n_0 in the consumer's shapes,

  F(n_1, n_i | 2 n_j, 2 n_k) >= F(n_1, n_i | n_j, n_k)/theta - C.

**Theorem E (PROVED here from (WS2); the hypothesis (TS-theta) is OPEN).** Assume (TS-theta), and that the thermal sums in (WS2) are at most s_* on the tori used. Put Phi(n) = F(n, n | n, n), D = (6/theta) log(1 + s_*) + C and Phi_* = D/(4/theta - 1). Then Phi(2n) >= (4/theta) Phi(n) - D for n >= n_0, and if Phi(n_1) > Phi_* at one size n_1 >= n_0 then Phi(2^k n_1) - Phi_* >= (4/theta)^k (Phi(n_1) - Phi_*) for every k.
Proof. (WS2) at (n, n | n, n), then (TS-theta) at (2n, 2n | n, n). Induction. QED

**Fact tests of the pair (TS-theta), seed.**
- U(1) Coulomb. In the Gaussian (Villain) description q is a ratio of theta sums in x = exp(-tau), tau = (e^2/2) n_1 n_i/(n_j n_k): q = (sum over odd e of x^(e^2))/(sum over even e of x^(e^2)), so F = tau - log 2 + o(1) at large tau and F depends on the sides through tau only (ARGUED from the Gaussian form; the proved lane statement is row 786, not re-read). Doubling both transverse sides divides tau by 4. So (TS-theta) fails for every theta < 4 and holds with theta = 4. The abelian theory is exactly marginal for the engine: 4/theta = 1.
- Z_2 at large beta, frozen Q_8 and 2T. F is tiny at every size, so (TS-theta) holds trivially (F >= 0) and the seed Phi(n_1) > Phi_* fails. 
- So the two selectivities separate: (TS-theta) is false only for a Coulomb phase; the seed is false only for a deconfined phase. This separation is the one structural gain of the attempt (ARGUED; not found in the searched scope: grep "spread" gives gap-filter-ls-opus.md L282, L355, which describe spread flux for EXC, not an exponent).
- Proved obstructions: no worst-case exterior enters. Small number: none; the seed is of order one. With s_* = 4 (three other flux sectors at most 1 each, and a glue sum at most 1) and theta = 1: Phi_* = (6 log 5 + C)/3, about 3.2 + C/3. So the seed asks for an odd-flux weight below about four per cent on a symmetric torus whose glue thermal sum is at most 1.

**Where the attempt stops.** (TS-theta) is open at every size. Lemma TD proves a transverse step only with an additive crossed thermal sum. To remove it one needs that the vortex energy (the shift between the spectra of T_0 and T_v) is nearly the same in the excited states as in the ground state. That is a locality statement for excited states, of the same kind as the lane's (F-h) and (LOC) (SK L636). And the seed of Theorem E, though weak, sits near ten correlation lengths, inside the band. So route E does not pass the wall. It replaces the flux half by: a blind exact step (WS2), a Coulomb-selective exponent (TS-theta), and a deconfinement-selective seed of a few per cent.

### 8.1b Route CX: convexity along doublings with a base at weak coupling

**Lemma CX1 (PROVED; one line).** Let G be a function on the sizes 2^k n_0 with G(4n) - 2 G(2n) + G(n) >= 0 for all such n, and d_0 = G(2 n_0) - G(n_0) > 0. Then G(2^k n_0) >= G(n_0) + k d_0. (The increments are non-decreasing.) With G = Phi this gives q(2^k n_0) <= q(n_0) exp(-k d_0): a power-law fall of the odd-flux weight, which reaches any threshold at a finite size, with d_0 measured at a weak-coupling scale.

**Attempt at (CVX) for Phi with the exact tools; it fails, with the reason (PROVED).** log Z^+ and log Z^- are each convex in n_1 and in n_i separately (traces of powers of positive operators; for Z^- in n_i by the axis exchange). So F = log Z^+ - log Z^- is a difference of two functions that are convex in each worldsheet side. The exact tools give convexity of each term and no sign for the difference; they give the opposite information on the sector energies (concave in a length: gap-skeleton-max.md L130). And (CVX) is false in the class: on the ordered side near a critical point the analogous quantity falls linearly in n/xi from its critical value, so its second difference along doublings is negative (ARGUED from finite-size scaling; no run made). So (CVX) is selective; no blind proof exists; its status is that of (MONO-Delta) (gap-phys-seed.md L384: "a sign with no small number in it"). What CX adds to that family: with a second-order condition the base is an increment at weak coupling, and no infrared input such as (Z-UNB) is needed. The base itself (a positive increment of Phi between two small twisted volumes, a statement at relative order g^2) is not available from the account, which runs on untwisted tori above a floor (FL 2.4 item 4). OPEN, both parts.

Status: S8 attempt 1 done. Proved: Lemma TD, Theorem E, Lemma CX1 (all elementary). Found again: Lemma WS. Open: (TS-theta), (CVX), the base.

### 8.2 Attempt 2: route LT, localization by link tilts

**Statement.** For h in (R^4)^E let nu^h be the Wilson measure tilted by exp(sum_e <h_e, U_e>), links viewed as unit vectors of R^4. This is the SU(2) gauge theory with a frozen fundamental Higgs field in unitary gauge. (TC): sup over h of the operator norm of Cov_(nu^h)(U) is at most K, uniformly in the volume.

**LT1 (PROVED; found again: BR idea 48, L332, the same gauge-averaging argument).** Cov_(nu^0)(U_e, U_e') = delta_(e e')/4.

**LT2 (ARGUED, given a recalled theorem that I did not re-read or adapt: Chen and Eldan, localization schemes, FOCS 2022; Eldan, Koehler and Zeitouni 2021; Bauerschmidt, Bodineau and Dagallier 2023).** For the stochastic localization process of nu, the tilted measures at time s are the nu^h with h = s x + B_s. The variance of any f obeys Var_nu(f) <= exp(integral over [0, T] of K_s ds) E[Var_(nu_T)(f)], with K_s the essential supremum of the covariance norm at time s. At T of order 6 beta plus a constant, almost every link is strongly tilted and the tilted measure mixes by pinning (the regime of FIN L938, Theorem STEP). So (TC) would give a volume-uniform Glauber gap for nu, hence decay of invariant correlations at that beta.

**Kill attempt (ARGUED).** Two findings.
1. *The first step is not free.* At small s the tilt is weak, and the covariance of a weakly tilted measure is Id/4 plus terms that are sums over the volume of connected correlations of nu itself (pairs of closed hopping loops through the two links). Those sums are bounded only if the loop correlations of nu decay summably. So (TC) at small tilt already contains a clustering statement for the pure theory. In the Ising case the same step is free because the interaction is a bounded quadratic form; here the interaction is quartic in the links and the hopping loops interact through the unknown gauge measure. Verdict under the proof-search governance: blocked-equivalent. (TC) restates the target at the given beta and adds a demand on the whole Higgs line.
2. *The Higgs line.* For a gapless pure theory the tilt line must cross a transition before the frozen region (Fradkin and Shenker, recalled), so (TC) fails for U(1) Coulomb: it passes the U(1) test as a target. For SU(2) the homogeneous fixed-length Higgs line is believed to have a first-order piece that ends near beta 2.7 (recalled numerics, Bonati and others 2010; BELIEF, not re-read). At a first-order point the covariance norm is of the order of the volume. So above that end point (TC) is false although the pure theory is believed gapped. The essential supremum in LT2 runs over all tilts, since the noise has full support; a typical-tilt form would need a different theorem.

**Result.** Route LT is dead as a route to the seed: its hypothesis is at least as strong as the target at the same beta, and false at large beta. It is recorded so that the link form of idea 4 of BR is not tried again without a typical-tilt theorem. Off the path.

Status: S8 done. Attempt 1 (routes E and CX): three elementary statements proved, crux statements open, no passage. Attempt 2 (route LT): killed with a reason. No route past the wall was found. No numeric run was made in this exercise.

---

## Step 9. Report

### 9.1 The wall, in plain words (corrected)

We want to prove that the lightest excitation of the four-dimensional SU(2) gauge theory has a positive mass. The lane has reduced this to one inequality on one periodic box about ten or more correlation lengths wide. Proofs exist where the force is very strong, and a conditional account exists where it is very weak. In between, every exact step we hold is also true for theories with no mass, and every step that tells SU(2) apart needs a small number that is not there. The correction from this run: the problem is not a missing reformulation. Two independent sittings of the same model, with the earlier work closed, produced the same list of reformulations. What is missing is one step, valid at every scale, that is true for SU(2) and false for the massless theories.

### 9.2 What the exercise found

- The fresh pass (Steps 2 to 4) rediscovered the lane's own ideas almost one for one, including three "proved here" facts that row 859 had already proved (Step 5). I read this as evidence that the idea list is saturated for this model and this inventory. [reading]
- One filter was narrowed: the finite-group tests bind proofs of the flux half only, and at order one they rest on numerics; their theorem-grade form is Z_2 above 2.191 (6c). [argued]
- Attempt 1 gave a split of the flux half: a blind doubling step in the two directions of the flux sheet (found again), an elementary transverse doubling bound with an additive thermal error (Lemma TD, proved), and one selective exponent: when both transverse sides double, the flux free energy must fall by a factor below 4. Abelian theory has exactly 4. Deconfined finite-group theories pass the exponent test and fail the seed. So the two kinds of failure separate (Theorem E, proved given the open exponent statement). The seed of this engine is weak (odd-flux weight below about four per cent) but still sits near ten correlation lengths. [proved pieces; the exponent statement is open]
- Attempt 2 killed a technique from outside the lane's vocabulary in its link form (localization by tilts): its hypothesis already contains the target. [argued]
- A second-order sign condition (convexity along doublings) would move the base to weak coupling and remove the infrared input, but it is a sign with no small number, false in the class, and its base is outside the account. [argued]
- No route past the wall. This run is mostly a map. I say so plainly.

### 9.3 Filters corrected

One, narrowed, not overturned: "Q_8 and 2T are binding tests at order one" holds for routes through (E17), (FQ), HA, EXC, and is void for a direct route to the even seed (ES); and at order one it is a belief. Nothing comes back today, because no direct tool for (ES) exists.

### 9.4 Routes worth doing (at most three)

1. **(TS-theta), the spreading exponent.** Believe: in SU(2) the flux free energy at fixed sheet falls by less than a factor 4 when the transverse area quadruples, at every size above some n_0. Cost: unknown; it needs a locality statement for excited states, like (F-h). First test: decide (TS-theta) in two theorem-grade models, Villain U(1) at large beta (expected: exactly 4, from row 786) and Z_2 above 2.191 (expected: trivially true), and in the strong-coupling range of SU(2) (expected: theta = 1 with C from the area-law expansion). What it would change: the flux half becomes "not Coulomb" (the exponent) plus "not deconfined" (a four per cent seed), two statements with different comparison models.
2. **A reading row on the marginal-dimension method** (Aizenman and Duminil-Copin 2021; Aizenman, Geometric analysis of Ising models, Part III, arXiv:2509.02850, which the lane's literature note lists as extending random currents to frustration). Believe: a logarithmic gain per scale can be proved with no small parameter when a positive geometric representation exists. Cost: one reading. First test: does any step survive a signed measure with the sign rule (-1)^(2 j chi)? What it would change: it would give the first template for a selective engine.
3. **None further.** I do not propose route CX or route LT.

### 9.5 What not to do next

- Another fresh-framing run by this model on the same inventory. Reason: Step 5.
- The link-tilt localization criterion. Reason: 8.2.
- A blind proof of any convexity or monotony along scales. Reason: 8.1b and gap-phys-seed.md L371-373: such statements are false in the class.

### 9.6 The exact price

Not found as a proved equivalence. In words (argued, 6b): the wall equals the absence of one selective inequality that holds at every scale between first passage and about ten correlation lengths. (TS-theta) with theta below 4 is one exact form of such an inequality for the flux half; the lane's (MON') and (NOCRIT-HF) are others. None is proved at any order-one scale.

### 9.7 Work items

1. **Check request (another model).** Check line by line, in this file: lemma F5 (Step 3.1); the Jensen bound of F6; Lemma WS, Lemma TD and its exact free law, Theorem E (Step 8.1); Lemma CX1 (8.1b); the logical narrowing of 6c point 1. Verdict per statement: holds, holds after correction, fails. Also check each "not found in the searched scope" mark of Step 5 by a wider search of D/library and FIN rows 763 to 858. Stop rule: first failing step per statement. Output: a check file beside this one.
2. **Decide (TS-theta) in the theorem-grade models (author, medium).** Statement: 8.1. Read: gap-crux-restate.md L236-250 (Theorem F), gap-es1-opus.md L58-112, the Villain twist theorem of row 786 (gap-tu-retry.md L92). Test first: Villain U(1), large beta: compute F on (n_1, n_i | n_j, n_k) and on doubled transverse sides. Stop rule: one counterexample to "theta = 4 exactly" or a proof. Output: a short note.
3. **Reading (reader model; downloads allowed under the lane's rule).** The two papers of 9.4 item 2. Report only: the inequalities used, where positivity enters, and whether a signed version is stated anywhere.
4. **Lead note.** Record in the skeleton: the finite-group tests are tests of the flux half; at order one they are belief-grade.

Not proposed, with reasons: a proof lane on (CVX) (no tool; base outside the account); a numeric guide run on (CVX) (it would only confirm a sign the physics already predicts); route LT; any change of action (b1: costs the whole account).

### 9.8 Appendix pointers

Tables: Step 2 (inventory), Step 4 (assumptions), Step 5 (comparison), Step 6 (filters), Step 7 (routes). Approach registry: Step 7 table. Assumptions most likely to be wrong: e2 (every seed is a confinement statement), c1 (FL 2.5 unchecked). Most expensive to be wrong: c1; I12 (the account). Literature proofs worth translating: none identified beyond 9.4 item 2.

Status: S9 done.

---

## Step 10. Measure of the skill (row 721, Section 4.6), strong-word check, and the result

**Strong words read against what the run did.**
- "saturated" (Step 5, 9.2): a reading from two samples of one model; not a theorem. Kept with that mark.
- "every engine found is blind" (6b): means every engine in the files I opened and in this run. Rows 763 to 858 were not opened one by one.
- "dead" (8.2, route LT): an argued kill, not a proved no-go.
- "exact" (8.1): only (WS2), the free law of Lemma TD and the U(1) value theta = 4 in the Gaussian form are exact; the split of the flux half is a conditional theorem (Theorem E) with an open hypothesis.
- "new": no statement of this file is called new without the words "not found in the searched scope". The scope is in Step 5.
- "proved": all proofs here are a few lines, written in this file, not checked by another model.

**Measure.**
- Discard tests or verdicts corrected: none shown wrong. One narrowed in range (the finite-group tests: flux half only; belief-grade at order one). Two verdicts re-read as valid only in a stated range (the rule against one-way steps does not cover a second-order condition; "flux half from glue half fails" is valid for bounding the odd weight by clustering and says nothing on transverse stability).
- Statements for the check (work item 1): F5; the Jensen bound; Lemma WS (found again); Lemma TD and the free law; Theorem E; Lemma CX1; 6c point 1. Counts of right, right after correction, wrong: not known until a check exists.
- Marks "not found in the searched scope" that a check must test: (i) the sentence that a direct route to (ES) is exempt from the finite-group tests; (ii) the link-tilt criterion and its kill; (iii) the square-root law of F5; (iv) (TS-theta), Theorem E and the separation of the two selectivities; (v) the absence of the marginal-triviality method from the lane's record.
- Statements that the fresh pass called "proved here" and Step 5 found in row 859: three (the squared-angle rule, R = E[r(U)], the Elitzur covariance identity). Step 5 caught them before any "new" mark was written. So step 5 of the skill did its job in this run.
- Cost: one agent session at max effort; no numeric run; no download; no subagent. Token count not available to me.
- Was the next long run changed or cancelled by it? Advice to the lead: cancel further fresh-framing runs of this model on this inventory; queue work items 2 and 3 instead. The decision is the lead's.
- Against the revert clause of Section 4.6: this run corrected no filter outright and gave no statement that moves the target; it gave elementary lemmas on the path of the flux half and one narrowed filter. I count it as a weak run for the skill.

**Not covered (kept true).**
- FIN rows 697 to 859 and 876 to 877 were not read as rows, apart from RESULT text of rows 860 to 875 and 861 and grep hits. D/library/exercise-skill-v2.md was read at L1162-1200 only. gap-crux-skeleton-max.md (row 863) and gap-exit-max.md (row 861) were not opened. D/library/prior/* was searched by grep only.
- BR was read at L271-513 and L603-699; its Phase 1 map (L30-270) and scoring table (L514-602) were not read.
- Main was searched for three wordings only. No pull-request branch was opened.
- The account YM4_1400.tex was not read beyond a grep for action names and the lines FL quotes.
- No primary paper was read in this run. Every literature statement is recalled.
- The proof-search governance file of the skill (physics-loop/references/proof-search-governance.md) was not read; I used its terms (blocked-equivalent) as the skill text gives them.
- No blind check of the plain version ran. No check by another model exists.
- Steps (c), (e), (f) of FL 2.5 were taken as argued there.

**Final status block.**
- S0 done: record located; open and closed lists.
- S1 done: wall stated twice; no blind check.
- S2 done: 26 inventory items with marks.
- S3 done: C1 to C7; F5 proved.
- S4 done: assumptions table, ranking, seven fresh routes.
- S5 done: almost everything found again in row 859 and earlier rows; three small additions.
- S6 done: one filter narrowed; none overturned.
- S7 done: routes E, LT, CX ranked; none past the wall.
- S8 done: attempt 1 (Lemma TD, Theorem E, Lemma CX1 proved; (TS-theta), (CVX) open); attempt 2 (route LT killed, argued).
- S9 done: report and four work items.
- S10 done: measure.

RESULT: no route past the wall and no mass gap; the fresh pass re-derived the lane's idea list (row 859) almost one for one, which I read as saturation of reformulations for this model (reading). PROVED here, elementary and unchecked: the a priori bound -Delta' <= Delta/h + concavity defect (F5); the transverse doubling bound q(2 n_j) <= 2(1+S)^2 (q + S_v/2) with its exact free law q -> 2q/(1+q^2) (Lemma TD); Theorem E: exact sheet doubling (found again: Theorem F of gap-crux-restate.md L240-244) plus the OPEN exponent statement (TS-theta), theta < 4, gives geometric growth of the flux free energy above a seed of about four per cent odd-flux weight; Lemma CX1. ARGUED: U(1) Coulomb has theta = 4 exactly and frozen finite groups pass the exponent and fail the seed, so the two failures separate; the link-tilt localization criterion is blocked-equivalent and false above the Higgs end point. CORRECTED (narrowed): the finite-group tests bind the flux half only and are belief-grade at order one. OPEN: (TS-theta), (CVX) and its weak-coupling base, (ES), (E17), (SEED-FP). Top two routes: E with crux (TS-theta); a reading of the marginal-dimension method (Aizenman and Duminil-Copin) as the one known template for a selective engine with no small parameter.
