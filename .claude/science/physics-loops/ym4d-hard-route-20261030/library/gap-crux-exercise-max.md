lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-12T13:30Z

# Exercise v2 on the gap crux, first run at max (row 743)

Provenance: Claude Fable 5.2, max effort, as author, one session, no subagents. An earlier run of this item wrote the header only (at commit 7c58883f4). This run is pinned at commit 18aeda83a, date 2026-11-12 UTC.
Nothing in this file is checked by another model. Nothing here grants status. Every statement below carries its own mark.

Skill: `docs/ai_methodology/skills/exercise/SKILL.md` at 1eb15ac428 (fetched to /tmp/gcx743/skill, read in full). The target reads no framework axiom, so the refresher read is replaced by `GOAL.md` and the rules of `FINISH.md` (lines 1-84, 299-349), as the skill allows for a standalone proof target.

**What this run did not cover** (kept true as the run goes):

- The account `YM4_1400.tex` was not opened. Its statements are used only as the definition files quote them.
- `library/gap-flux-exercise.md`: read 3.0, 3.1 (C1, C2), 8.2 to 8.4. Step 9 was not read; its content is taken from skeleton 13.16.
- `library/gap-flux-exercise-check.md` Section 7: not read; its three corrections are taken from skeleton 13.16.
- `library/gap-seed-limit.md`: Sections 1, 5, 7 and the statement of Theorem L3 read; proofs not read.
- `library/gap-seed-shape.md`: status block and Section 3 read; the rest not read.
- `library/gap-crux-restate.md`: Sections 1, 2, 3.1, 3.2, 3.4 read in full; 3.3, 4, 5 not read before step 5.
- No blind check of the plain version (no subagents).

## Status block

| Step | State | Main result |
|---|---|---|
| 0 record | done | lists below |
| 1 wall | done | below |
| 2 inventory | not started | |
| 3 reason up | not started | |
| 4 assumptions | not started | |
| 5 compare | not started | |
| 6 filters | not started | |
| 7 routes | not started | |
| 8 attempts | not started | |
| 9 report | not started | |

## Step 0. Where the record is; open and closed lists

**Open now** (the brief's list): `library/gap-skeleton-final.md` Sections 0 to 3 and 13.15 to 13.17; `library/gap-flux-exercise.md` Step 9 and 8.2 to 8.4; `library/gap-flux-exercise-check.md` Section 7; `library/gap-crux-restate.md`; `library/gap-seed-limit.md`; `library/gap-seed-shape.md`; the account's statements. Reading state: see the list above.

**Closed until step 5** (the brief's list): `library/gap-means-max.md` (row 737), `library/gap-means-astra.md` (738), `library/gap-form-exercise.md` (735), `library/prior/gap-lit-*.md` (739 to 742), every other `library/gap-*.md`, `library/exercise-skill-v2.md`, FINISH rows 697 to 742. I add skeleton Section 13.18 (written from rows 737 to 744 after this row was queued) and FINISH rows 744 to 747.

One exposure to record: my memory note on this lane (written by an earlier session on row 737) says in one line that row 737 has a "Theorem R (even seed (ES) gives two of the three seeds)" and a lattice projective plane with a negative character term. I read that line while looking for navigation hints. I did not open the files. Steps 2 to 4 below do not use it.

Literature: the lane's records (`library/prior/gap-lit-*.md`) are on the closed list. Before step 5 I use only statements of results that the open files quote, and results I recall, marked `recalled`.

## Step 1. The wall, stated twice

**Plain version.** We want to show that the quantum theory of the SU(2) gauge field in four dimensions has a mass gap: the lightest excitation has a positive mass, so all correlations die off exponentially with distance. The lane has a proved machine for this. If, on one periodic box of one physical size, the excited states together carry little thermal weight (a "seed"), then every larger box has a gap, and so has the infinite-volume theory. The machine works for any model. What keeps failing is the seed itself. It has to be checked on a box many correlation lengths wide, where the interaction is strong. There no expansion has a small parameter, and every exact tool known to the lane also holds for models that have no gap. Getting past the wall means: a proof of one seed, or of the gap by a route that needs no seed. Analogy (only an analogy): we have a proved domino chain and no hand to push the first domino.

**Precise version.** Quoted, not rewritten.

- Target (GAP): `library/gap-skeleton-final.md` Section 1: sigma a canonical component of a volume-first limit at reference coupling g; then spec(H) is in {0} union [m, infinity) with m > 0, on the cyclic sector of tr(F^2).
- Lattice engine (proved, checked by two models): Theorem S and Corollary S3' (`library/gap-crux-restate.md` L170-222). If s = S(N; (2N)^3) < 1/5041 at one N >= 3, then m(L^3) >= log(1/(5041 s))/N for every L >= 2N.
- The three seeds (checked): Theorem S-w and Corollary EV (`library/gap-flux-exercise.md` 8.4): S_w(N; (2N)^3) < 1/5041 for w one of per, full, kappa gives (G_ev) on all cubes; Theorem EV-L (8.2) turns (G_ev) into clustering of every periodic limit on centre-blind functions.
- Scaling form: (SEED-phys) and Propositions P, P' (`library/gap-seed-limit.md` Section 5): the seed at physical size at most ell_*, uniformly in the cutoff, gives spec(H) in {0} union [M_*, infinity), given the T0 chain's continuum datum, (H2), (TOT).
- The wall: (SEED-phys), or its even form, at an effective coupling of order one. By the rate filter the seed size is more than 8.5 correlation lengths of its cube. Skeleton 13.15: equivalently (BDD-Delta) and (Z-UNB). Skeleton 13.17: a brief must name the means (M1) to (M4), or a fifth, by which the criterion is verified at the scale of the correlation length.
- Does not count: a statement at a size below the correlation length; a gap in lattice units that is not uniform in the cutoff; an argument that also runs for U(1) at weak coupling, for the fundamental-adjoint action at its transition line, or on a slab of critical width (skeleton Section 3); a route whose last step is the seed again.
- Counts as progress: a seed proved; an exact equivalence of the seed with a statement that a known tool reaches; a filter of the lane shown wrong; a route outside the frame with its first statement proved.

No blind check ran (no subagents). The plain version is corrected in step 9.

---

## Resumed 2026-11-13 (laptop, Claude Fable 5.2 max)

FINISH row 858, resuming row 743. Clone commit: 93b3066d92b017987957fe60282a26a0d81820e8 (branch claude/ym4d-hard-route, `git pull --ff-only` reported "Already up to date").
Steps 0 and 1 above were written on 2026-11-12. This run continues from Step 2.

Plan of the remaining exercise steps (one step per response, each appended here before the next starts; the step names are refined below once the skill text at 1eb15ac428 is read):

1. Step 2: restate the wall from the moved definitions only (SEED-FP at gap-finishline-opus.md lines 110-160; the crux in its weakest forms (E17), (FQ), (J12), (G2) at gap-assume-opus.md rows 43 and 112; gap-skeleton-final.md Sections 0-3 and 13.15-13.20).
2. Step 3: the skill's Step 3 (as the skill text states it), on the restated wall.
3. Step 4: list every assumption of the present formulation, one group per response: (a) the action; (b) the transfer operator on a torus; (c) the centre and the twists as variables; (d) one scale versus many; (e) SU(2) directly versus a larger or deformed theory; (f) Euclidean versus not; (g) assumptions that look like definitions. For each: what follows if dropped or changed, and what it costs.
4. Step 4 continued: for each new route, state its CRUX lemma and attempt it as a real proof, one stage per response. Apply the fact tests (U(1) Coulomb phase, Q_8 and 2T, the proved Dobrushin and one-layer ceilings, AN1, the no-fixed-small-number test).
5. Step 5 (compare): open the closed files (other gap-*.md, prior/*, exercise-skill-v2.md, FINISH rows 697-857), search main and the open YM4D pull-request branches, and name every earlier statement the result repeats, with path and line.
6. Steps 6 to 9 of the skill, as its text states them.
7. The measure of the skill (row 721 Section 4.6), then the RESULT line.

### Reading state of the resumed run (kept true as the run goes)

Skill: read in full at 1eb15ac428 (700 lines). Short names: FL = `library/gap-finishline-opus.md`; AS = `library/gap-assume-opus.md`; SK = `library/gap-skeleton-final.md`; FIN = `FINISH.md`, all under D in the clone at 93b3066d92.

- FL: lines 100-165 read (the brief names 110-160; lines 100-109 are the last rows of its table of proved statements). Nothing else of FL read.
- AS: header (L1-26), ledger rows 32-53 (L70-92), rows 65-67 (L108-110), Part 2 rows 43 and 112 (L245, L335). Nothing else.
- Lines those rows cite, statements only: `gap-expose-astra.md` L577-593 ((E16), (E17)); `gap-fusion-astra.md` L66-69, L97-105 (the witness); `gap-vortex-astra.md` L194-203 ((FQ)); `gap-joint-astra.md` L141-156, L340-356 ((J4), (J12)); FIN L888 and L891, first 2200 characters each (the task texts of rows 811 and 814, which state the twist deficit and (G2)).
- SK: Sections 0-3 (L10-68) and 13.15-13.20 (L547-644) read in full.
- The account `YM4_1400.tex`: not opened so far. Its statements are used as FL and SK quote them.
- Closed until Step 5: every other `library/gap-*.md`, `library/prior/*`, `library/exercise-skill-v2.md`, FIN rows 697-857 (except the two cited lines above).
- The brief's fact tests (rows 786, 838, 839, 843, 845 and the Dobrushin ceilings) are used as the brief states them. Their files are closed until Step 5.

Marks used below: the brief's (PROVED = proved by me in this file, not checked by another model; READ path:line; ARGUED; GUIDE; OPEN), and for inventory items the skill's kinds (DEF, SUPPLIED, THM, BELIEF) in a second column. "recalled" = a published result stated from memory, not re-read in this run.

## Step 2. The wall restated (it has moved), and the inventory

### 2.0 The wall, restated from the moved definitions

**Plain version (replaces Step 1's where they differ).** The lane has a proved chain: one inequality on one periodic box of one physical size, true for every fine enough lattice, gives the mass gap of the continuum theory that the Sussman-Alpoge account constructs. The inequality says that the excited states of the box carry little thermal weight. All that is left of it, after the lane's reductions, is one family of numbers: how much the partition function of a box drops when a centre twist is put through it (the twist deficit). The drop must be tiny, exponentially small in the side of the box, for the "crossed" twists, at a coupling of order one, on boxes many correlation lengths wide. In physical words: magnetic flux must cost nothing, which is the same as: electric flux is heavy. (Corrected in place on 2026-11-13: my first wording said the drop must be close to total; by (E16) and (FQ) the deficit 1 - R = 2p must be small.) At that coupling nothing is small. Every method tried either needs a small number (and the proved ranges stop near beta = 2/3, a factor of four below the window 2.3 to 2.6), or is true as well for a model whose twist cost is not large.

**Precise version (quoted).**

- **Finish line (SEED-FP)** (READ FL:117-123): there are K_0, a physical size ell with ell/(2 a_K) an integer at least 3, and s_* < 1/5041 with S_(K,beta)(ell/(2 a_K); (ell/a_K)^3) <= s_* for every first-passage datum (K, beta) at g with K >= K_0. S is the thermal sum of the bare Wilson transfer operator of the periodic cube of physical side ell at physical time ell/2.
- **From it to (GAP)** (READ FL:150-159, Section 2.5): steps (a), (b) are proved and checked (rows 698, 699, 703); (c), (e), (f) are argued by row 837, not checked; (d) is the account's continuum datum, conditional on its packages A-H.
- **What the seed must be about** (READ FL:140-146): the bare Wilson measure along first passage (equivalently the total masses of the account's densities rho_K, by two exact identities). A seed for a plain Wilson weight at the unit scale does not give it. The margin is absolute: one size and one number for all large cutoffs (FL:148-153).
- **The crux, weakest forms on file** (READ FIN:891, AS:80-83, EX:577-593, VO:199-203, JO:346-354):
  - the twist deficit 1 - Z^(m+v)/Z^m of 4D Wilson SU(2) on the boxes (a, a, c, d), c and d in {a, 2a}, on a compact order-one beta interval, at the original Wilson normalization, for the crossed pairs; with p_(m,i)(a) = Tr(P_(-,i) L_m^a)/Tr(L_m^a) = (1 - R_m(v_(1i)))/2 and Q_F = max over m_2 = 0, i = 3, 4 of p_(m,i)(a) (E16);
  - (FQ): 8 Q_F <= K(a) sqrt(S_ev(a)), Q_F < 1/192, K(a) <= C_1 a^(p_1);
  - (E17): Q_F <= C a^p eta_*^(a/2), 0 < eta_* < 1, sufficient because S_ev(t; B) >= eta(beta)^t with eta(beta) = e^(-80 beta) r(beta)^4/(4 + 16 r(beta)^4) (READ FU:97-105);
  - (J12): sup over root faces p of the sum over closed mod-2 surfaces S with v(S) = 1 rooted at p of |D_m(S)| <= C_1 a^b e^(-kappa a), kappa >= (1/2) log(1/eta_*), for the dressed activities D_m of the exact representation (J4);
  - (G2): an integrated curvature bound equivalent to a volume-uniform gauge-invariant Langevin gap (proved for beta < 2/9; its missing piece at order one is a joint mixed-Hessian estimate).
- **The form that the continuum needs** (READ AS:245, FL:151): (E17) is a fixed-coupling statement. Along the account's sequence its right side tends to zero at fixed physical size while the physical twist deficit should stay positive. So the consumer needs K bounded independently of the cutoff at fixed physical size, or a lower bound on S_ev in physical units (OPEN). The twisted forms are outside the account's present scope: it runs its flow on untwisted tori only (READ FL:153).
- **The order-one window** (the brief): bare beta_W about 2.3 to 2.6. No fixed beta finishes the proof.
- **Does not count**: a statement below the correlation length; a lattice gap not uniform in the cutoff; an argument that also runs for U(1) in its Coulomb phase (where the Villain twist theorem of row 786 holds), or for Q_8 or 2T at order one where they are ordered; a background-uniform one-layer twist bound above beta_W = 1.0109; a worst-case single-site or vertex-block Dobrushin condition; (AN1); any fixed small number.
- **Counts**: a new route whose CRUX lemma is attempted as a real proof; a seed proved; an exact equivalence of the crux with a statement a known tool reaches; a filter shown wrong.

**What moved since Step 1 (READ SK 13.16-13.20, FL 2.2-2.5).** (i) The flux sectors left the form of the crux: the even seed (ES), two numbers of the centre-even sector, is equivalent at some size to each of the three seeds (Theorem R, checked row 744). (ii) The second number, the vacuum-energy defect, is the weight of the twelve heavy crossed flux sectors (Theorem V); it does not follow linearly from the first ((ES-1) fails). (iii) The remaining input is the crossed twist deficit, with the consumer (FQ). (iv) The finish line is now stated on the account's objects, (SEED-FP), and Section 2.5 closes the path from it to (GAP) given the account. (v) Four families of attack are ruled out in stated forms: (EP), fixed-radius separate-state loop certificates, the full-L2 block certificate, and (tonight) the worst-case Dobrushin and one-layer bounds.

### 2.1 The inventory (part 1 of 2: the lane's own facts)

| # | Item | Kind | Source | Standing |
|---|---|---|---|---|
| I1 | Model: Wilson SU(2) on a periodic 4D lattice, normalized Haar measure, compact link space, strictly positive density, exact gauge invariance. | DEF | READ AS:109 | - |
| I2 | The account of Sussman and Alpoge (with Claude and Codex), YM4_1400 at 2bc0658f91d2: a conditional outline of the continuum tr(F^2) theory at small reference coupling g; hypotheses are packages A-H; existence is not proved. | SUPPLIED | READ SK:27 | statements read by the lane, not by me |
| I3 | Target (GAP): spec(H) in {0} union [m, infinity) on the cyclic sector of tr(F^2), for a canonical component of a volume-first limit at g. Confinement is not asked. | DEF | READ SK:29-33; AS:43 | - |
| I4 | Scales: the unit is where the running coupling is g; between distance 1 and 1/m the coupling runs from g to order one; no estimate of the account reaches those scales. | READ + BELIEF (the size of m) | READ SK:34 | - |
| I5 | (SEED-FP) and its forms (SEED-Delta), (SEED-L) on the account's own untwisted tori; the integral of rho_k equals Z exactly at each level; the dilation identity. | DEF + THM (account) | READ FL:117-128 | read by row 837 in the account |
| I6 | Theorem S, Corollary S3', Theorem SH: one seed at one size gives a gap on every larger cube. They use only a positive transfer operator and axis symmetry. They hold for every group and every symmetric model with positive transfer operators. | THM | READ FL:100-101, 112 | checked (rows 698, 699, 707) |
| I7 | Theorem ZD-c: (PHYS-SEED) iff (BDD-Delta) and (Z-UNB); in every comparison model the half that fails is (Z-UNB). | THM | READ FL:103; SK:557-562 | checked (row 727) |
| I8 | Theorem L, Propositions P, P': the uniform seed gives spec(H) in {0} union [M_*, infinity) for the continuum datum. | THM | READ FL:104, 150-159 | checked (row 703); steps (c), (e), (f) of FL 2.5 argued, not checked |
| I9 | Theorem EV-L: the limit half needs only the centre-even sector, (G_ev). | THM | READ SK:574 | checked (row 732) |
| I10 | Theorem R: the even seed (ES) (even thermal sum and vacuum-energy defect, each <= 1e-7 at one size) gives two of the three seeds and (G_ev) on all larger cubes. | THM | READ FL:105; SK:620 | checked (row 744) |
| I11 | Theorem V: the defect equals the weight of the twelve heavy crossed flux sectors up to even sums. (ES-1) fails in its linear form. | THM | READ SK:634-636 | checked (row 753) |
| I12 | (FQ) gives (F-h); FUSE-suff: (F-h), (F-l) at three shapes and small even sums give delta < 1e-7. | THM | READ FL:107-108 | checked (rows 753, 780) |
| I13 | Witness: S_ev(t; B) >= eta(beta)^t for every beta > 0, sides >= 3, t >= 3. | THM | READ FU:97-105 | standing not read |
| I14 | (J4): the odd-sector ratio p_m(v) is an exact signed sum over closed mod-2 surfaces with dressed activities D_m(S), against the original Z_m. At beta = 1/2 a dressed flat plane has activity above 216^(-A), so a uniform per-face budget fails. | THM | READ JO:141-156; FIN:891 | checked (row 816) |
| I15 | (G2) holds for beta < 2/9; so a uniform Langevin gap there. | THM | READ FIN:891 | checked (row 815) |
| I16 | Proved bare ranges: seed and lattice gap beta < 2/9; Langevin gap beta < 1/4; area law beta < 2/3; SOS surface classes beta <= 5/11. | THM | READ AS:86 | as their rows say |
| I17 | P1: a seed at threshold t forces n m >= log(1/t): the seed cube is at least 12.9 of its own correlation lengths. | THM | READ AS:73 | - |
| I18 | Theorem CRIT: the set of couplings with a seed is open. | THM | READ AS:89 | row 709 |
| I19 | Corollary NS0: a lattice projective plane of 92 plaquettes enters the 4D SU(2) character expansion with a minus sign. No term-by-term positive surface representation. | THM | READ SK:608-626 | checked (row 744) |
| I20 | (EP) (the narrow loop association) is false for SU(2); U(1) and Z_2 satisfy it. | THM | READ SK:638 | checked (row 756) |
| I21 | No fixed-radius loop-equation certificate with separate states for two volumes reaches (ES) at large a (Theorem O). The block certificate PA fails at weak coupling by a gauge corner. | THM | READ SK:640-642 | checked (rows 758, 762) |
| I22 | Ceilings (the brief): worst-case single-site Dobrushin in the slab: exactly 2/3; vertex blocks: 0.775; every background-uniform one-layer twist bound fails above beta_W = 4 G_3 = 1.0109 (row 839); (AN1) is equivalent to the worst-case exterior bound (row 845). | THM | the brief | checked, as the brief says |
| I23 | The Villain U(1) twist theorem (row 786) holds in the Coulomb phase. Q_8 and 2T pass the commutator contraction and several "SU(2)-only" steps verbatim (rows 838, 843). | THM | the brief | as the brief says |
| I24 | The account runs its flow on untwisted tori of four equal sides above a floor; it bounds log Z up to C l^4; nothing bounds the distance of its effective weights from a Wilson weight at order-one coupling. | READ | FL:125, 142-146; SK:553 | - |
| I25 | Rate filter: the lattice gap is at most C' exp(-c_AF beta (1+o(1))). Upper bounds on m. | THM | READ SK:66-67 | proved, unchecked |
| I26 | Rule: an author brief on the crux names the means (M1)-(M4), or a fifth, by which its criterion is verified at the scale of the correlation length. | SUPPLIED (lead's rule) | READ SK:592-596 | - |

### 2.2 The inventory (part 2 of 2: nearest models and recalled literature)

All items here are stated from memory (`recalled`); none was re-read in this run. No proof step below rests on one without saying so.

| # | Item | Kind | Standing |
|---|---|---|---|
| N1 | 4D U(1), Wilson or Villain: Coulomb phase at weak coupling, no gap (Guth 1980; Frohlich and Spencer 1982). | THM | recalled |
| N2 | 4D Z_2 gauge theory: self-dual, one transition at beta_c = (1/2) log(1 + sqrt 2); gapped on both sides; the centre-even sector at large beta has a gap. | THM (duality), BELIEF (order of the transition) | recalled |
| N3 | Finite subgroups Q_8, 2T, 2O, 2I of SU(2) with the Wilson action: each has a freezing transition; above it the Wilson loop has a perimeter law and the crossed twist deficit is not near 1. Q_8 freezes near beta of order 1; 2T near 2.2; 2I near 5.8 (numbers from memory of Hartung et al. 2022). | BELIEF (numerics) for the values; THM (Peierls at large beta) for the ordered phase | recalled |
| N4 | SU(2) Wilson, 4D: no bulk transition seen; crossover near beta = 2.2; string tension and glueball mass scale as asymptotic freedom predicts. | BELIEF (numerics) | recalled |
| N5 | SU(2) on a slab of N_t layers deconfines at beta_c(N_t); beta_c(2) is near 1.87, beta_c(4) near 2.30 (from memory). Rigorous: deconfinement at large beta for fixed N_t (Borgs and Seiler 1983). | BELIEF (values), THM (Borgs-Seiler) | recalled |
| N6 | Fundamental-adjoint SU(2) action: a first-order line ending at a point near (beta_F, beta_A) = (1.5, 0.9); SO(3) theory with Z_2 monopoles has a bulk transition (Bhanot and Creutz 1981; Halliday and Schwimmer 1981). | BELIEF (numerics) | recalled |
| N7 | 't Hooft 1979: on a torus the twisted partition functions Z(k, m) and the electric-flux free energies are related by a Z_2 Fourier transform; in a gapped phase each flux is light or heavy. | THM (the duality identity) | recalled |
| N8 | Tomboulis and Yaffe 1985: a Wilson loop is bounded by a power of a twist ratio (vortex free energy), at every beta, by reflection positivity. Kanazawa extended it. | THM | recalled; quoted at SK:612 |
| N9 | Mack and Petkova 1979-80: Wilson loops bounded by vortex-container free energies after the Z_2 x SO(3) change of variables; Z_2 monopoles are the endpoints of thin vortices. | THM | recalled |
| N10 | Osterwalder and Seiler 1978: convergent strong-coupling expansion, area law and gap for small beta. | THM | recalled |
| N11 | Chessboard estimates (Frohlich, Israel, Lieb, Simon 1978): for a reflection-positive measure, the expectation of a product of local functions is at most the product of their "constant-configuration" norms. | THM | recalled |
| N12 | Dobrushin and Shlosman 1985-87: complete analyticity; a finite-volume condition C_V at ONE finite box of side comparable to the correlation length gives uniqueness, exponential mixing and analyticity; the constructive condition needs a compact spin space and finite range. | THM | recalled |
| N13 | Martinelli and Olivieri 1994; Lu and Yau 1993; Stroock and Zegarlinski 1992: for compact spins, mixing in finite cubes ("strong mixing") is equivalent to a uniform log-Sobolev or spectral gap of the Glauber or Langevin dynamics. | THM | recalled |
| N14 | Bakry and Emery; for the lattice gauge Langevin dynamics: the Ricci curvature of SU(2)^E is 1/4 per link direction in the bi-invariant metric of the standard normalization; a Hessian bound on the action smaller than that gives a gap (Shen, Zhu and Zhu 2022 use this). | THM | recalled; quoted at FIN:891 |
| N15 | Gopfert and Mack 1982: 3D U(1) has a gap at every coupling, by the monopole gas with a second small parameter. | THM | recalled; SK:590 |
| N16 | Finite-size criteria: Knabe 1988; Gosset and Mozgunov 2016; Lemm and Mozgunov 2019: a spectral gap of a frustration-free Hamiltonian on a finite patch above a threshold of order 1/n gives a gap in infinite volume. | THM | recalled |
| N17 | Aizenman, Simon 1980 / Lieb 1980 / Simon 1980: a finite-size correlation criterion (the sum of correlations across the boundary of ONE finite set is below 1) gives exponential decay, for models with the Lieb-Simon inequality (O(N), N <= 4 with caveats; Ising). Duminil-Copin and Tassion 2016 made it sharp for Ising and percolation. | THM | recalled; SK:590 |
| N18 | Brydges, Frohlich, Seiler 1979: the diamagnetic inequality; Kato-type bounds for matter in a gauge background; reflection positivity of the Wilson action in the link and site reflections. | THM | recalled |
| N19 | Luscher 1982 and van Baal: the SU(2) theory in a small periodic box is a quantum mechanics of the constant abelian modes (torons); the spectrum is computable in perturbation theory in the box coupling up to a size near 0.2 to 0.7 fm; the electric-flux energies split by tunnelling through a barrier. | THM (formal expansion), BELIEF (range) | recalled |
| N20 | Seiler 1982 (Lecture Notes in Physics 159): Wilson loop upper bound by the Z_2 or U(1) comparison? Recalled exactly only for this: for every compact group the Wilson loop has at least a perimeter-law decay and at most area-law decay (Seiler; Simon and Yaffe 1982). | THM | recalled |

**Nearest models where the target statement is false or true for a known reason** (these are the tests of Step 6): N1 (false), N3 above freezing (false), N5 at critical width (false along the slab), N6 on the line (false at the end point), N2 (true by duality and expansion), N10 (true by M1), N15 (true by M2).

## Step 3. Reasoning up from the inventory

### 3.1 What follows at once

- **F1 (ARGUED from I6).** The engine is blind to the group. It holds for U(1), Q_8, 2T. So the group enters only through the seed, and the seed is false for N1 and for N3 above freezing.
- **F2 (ARGUED from (E16), I12).** The direction of the crux: the deficit 1 - R = 2p must be small. R = Tr(c L^a)/Tr(L^a) is the thermal mean of the centre flip c of one hyperplane of links, a unitary of order two that commutes with the transfer operator. The crux says: the thermal state of the box sits on c-even states up to an exponentially small weight. The ground state is c-even at every beta (positive kernel; recalled Perron-Frobenius). So the crux is a statement about the lowest c-odd state only when the box is long, and about all c-odd states at time a.
- **F3 (PROVED, two lines; known since 't Hooft 1979).** For SU(2) a twist in one plane costs zero classical action. Take U = i sigma_1 on the 1-links that cross x_1 = L_1, U = i sigma_2 on the 2-links that cross x_2 = L_2, and U = 1 elsewhere. Every plaquette is 1, except the (1,2) plaquettes at the corner, which are (i sigma_1)(i sigma_2)(i sigma_1)^(-1)(i sigma_2)^(-1) = -1. The twisted action flips exactly these signs, so it vanishes. For U(1) no such configuration exists: the plaquette angles on each (1,2) section sum to pi mod 2 pi, so the Wilson action is at least of order beta pi^2/(2 n_1 n_2) per section, and the total over the n_3 n_4 sections is of order beta pi^2 n_3 n_4/(2 n_1 n_2), which does not tend to zero on a symmetric box. So the twist costs U(1) energy and costs SU(2) no energy. In SU(2) the whole deficit is a fluctuation (entropy) effect.
- **F4 (ARGUED).** Two crossed twists (planes (1,2) and (3,4)) admit no constant solution in SU(2): a matrix that commutes with i sigma_1 and i sigma_2 is +1 or -1 and cannot anticommute with anything. So the crossed twist has a positive classical cost (recalled: half an instanton, pi^2 beta in the continuum normalization). The crux asks for a small deficit for exactly these pairs.
- **F5 (ARGUED from I5, FL:128).** Every form of the seed is a LOWER bound on a partition function: Z^(m+v) >= (1 - delta) Z^m; or log Z((L ell)^4) >= L^4 log Z(ell^4) - 0.131 L. The opposite bounds are the free ones (reflection positivity gives R <= 1 and Phi_L >= 0). Lower bounds on a partition function are what a trial map or trial measure gives (Jensen). The difficulty is the precision: the loss allowed is absolute, not per unit volume.
- **F6 (ARGUED from I4, I24, FL:140-146).** A proof at one bare beta in the window does not finish. What finishes is a statement at lattice size ell/a_K and bare coupling beta_K, both tending to infinity. A fixed-beta result helps only if it holds for an open class of weights that contains the account's effective weight at the scale where the coupling is of order one, and the account does not reach that scale.

### 3.2 The least a solution must contain

1. **A use of the Lie algebra together with non-commutativity (ARGUED from N1, N3, I23).** U(1) is continuous and abelian; Q_8 and 2T are non-abelian and discrete. 2T freezes near beta = 2.2, just below the window. So a proof for SU(2) in the window uses a step that fails for 2T there and fails for U(1) at weak coupling. A step that only uses "non-abelian" (commutators of group elements, the degree of representations) holds for 2T. A step that only uses "continuous" (integration by parts, Langevin, soft deformations) holds for U(1). The step must use both in one move: for example the bracket of two infinitesimal rotations, the positive Ricci curvature of the group (it is the square of the bracket), or the fact that a rotation by pi about one axis can be turned continuously into a rotation by pi about another.
2. **A statement at the scale of the correlation length with an absolute margin (READ I17, I26).**
3. **A passage to the continuum (F6).** Either the statement is uniform along first passage, or it is robust in an open class of weights and the flow is controlled into that class.
4. **It must fail on a slab of critical width (N5) and on the fundamental-adjoint line (N6).** So it uses all four directions on the same footing, or the size in every direction; and it uses the Wilson form, or the continuum limit.

### 3.3 The smallest object

The smallest object is one number per box: R = Z^(m+v)/Z^m = <prod over p in Sigma of exp(-beta tr U_p)>_m, the mean of the sign flip of the plaquettes of one closed dual surface Sigma (ARGUED from the Wilson weight exp((beta/2) tr U_p): flipping the sign of a plaquette multiplies the weight by exp(-beta tr U_p)). Three equal readings of it:

1. R = the thermal mean of the centre flip c (F2).
2. R = the ratio of the partition functions of the torus with boundary conditions twisted by two colour rotations, by pi about axis 1 in direction 1 and by pi about axis 2 in direction 2, and of the periodic torus. The two rotations commute in SO(3); their lifts to SU(2) anticommute (recalled, 't Hooft 1979; the lattice form is F3).
3. R = the ratio of the partition functions of the two SO(3) bundles over the torus, w_2 = v and w_2 = 0 (recalled).

Toy model where the wall still bites: none in dimension four. In two dimensions R = sum over j of (-1)^(2j) e^(-A c_j) / sum over j of e^(-A c_j) exactly, so the deficit is about 2 e^(-A c_(1/2)) (recalled; exact closure, the means (M3)). The nearest model with the wall is the twist free energy of the 2D O(3) model, which is open at large beta (recalled).

### 3.4 Where the result can come from

Mechanisms that make the deficit small: (a) disorder at the plaquette scale (strong coupling, (M1)); (b) entropy of thick vortices: after the split SU(2) = Z_2 x SO(3) the twist is the topological class of the SO(3) field, and the two classes have the same local weight; (c) the heavy electric flux: the lowest c-odd state lies sigma a above the ground state; (d) an exact symmetry or duality that maps the twisted ensemble onto the untwisted one up to a boundary term.

Ways it can fail: a Coulomb phase (stiffness stays positive: U(1)); freezing (finite groups); two coexisting phases (N6); a critical slab (N5).

It is several problems by scale. Below the correlation length the deficit is of order one and that is correct physics (small-volume expansion, N19). The statement is needed only at about 13 or more correlation lengths. It is one problem by sector (the c-odd sector of crossed pairs).

### 3.5 Making the requirement less wrong

1. The consumer needs Q_F against sqrt(S_ev), not against a fixed rate (READ VO:199-203). (E17) is stronger than needed and is wrong for the continuum (AS:245). The physical statement is: the lowest electric flux energy of the box of side a exceeds half the even gap by a margin that grows with a. With an area law it holds from a = m_ev/(2 sigma) on, about one correlation length (BELIEF: sqrt(sigma)/m is about 0.3 for SU(2)).
2. The target (GAP) does not ask for confinement (I3). The seed does. This is a cost of the method (the trace over all sectors, AS:71), not of the target. Theorem R moved the flux sectors out of the form, and they came back through the vacuum-energy defect (I11). A proof of (G_ev) that never meets the odd sector is not excluded by anything in the inventory.
3. The margin 1/5041, the sizes and the shapes are consequences of the engine, not needs of the target.
4. The target needs the continuum limit state only. Nothing in the inventory forces the proof to pass through a statement about the bare lattice at an order-one beta (F6). The window 2.3 to 2.6 is where the bare lattice at a FIXED number of sites would be tested; the finish line never sits there.

### 3.6 The price

If the seed cannot be derived, the missing input is, in one sentence: **a bound, uniform along first passage, on the thermal weight of the c-odd states of one periodic box of fixed physical size** (and of the even excited states). In the lane's forms: (SEED-FP); or (ES); or (FQ) with K bounded in physical units.

### 3.7 Conclusions of Step 3

- **C1 (from F1, 3.2.1).** The proof must use the Lie algebra and its bracket in one move. Group-commutator identities hold for 2T; integration by parts alone holds for U(1).
- **C2 (from F3, F4).** For SU(2) the single-plane twist costs no classical energy; for U(1) it costs a scale-invariant positive energy. So in SU(2) the deficit is all entropy, and in U(1) it is energy. A proof can use this: it is a property that U(1) lacks at every beta. The finite groups Q_8 and 2T share it (i sigma_1 and i sigma_2 lie in Q_8), so alone it does not pass the finite-group test.
- **C3 (from F5).** The seed is a lower bound on a partition function. Trial maps point the right way. The precision needed is absolute.
- **C4 (from F6, 3.5.4).** The finish line is not at an order-one bare beta. A route that works directly in physical units along first passage is not excluded, and a fixed-beta route needs robustness in an open class of weights plus control of the flow into it.
- **C5 (from 3.5.2).** The odd sector is forced by the method, not by the target.
- **C6 (from N12, N13, N16, I21, I22).** Every finite-size criterion in the inventory needs its hypothesis checked on a block of the size of the correlation length. By hand that needs one of (M1) to (M4). C6 is a reading, not a theorem.

## Step 4. The assumptions table (one group per response)

Row format: ID | assumption | where used | needed or habit | if dropped or changed | cost | easier? Groups follow the brief: (A) the action; (B) the transfer operator on a torus; (C) the centre and the twists as variables; (D) one scale or many; (E) SU(2) directly or a larger or deformed theory; (F) Euclidean or not; (G) target, discard tests, beliefs and working rules.

### 4.A The action

Read for this group: the account `YM4_1400.tex` (local copy /Users/jonreilly/ym4d-lead/sa1400/YM4_1400.tex, 136637 lines), lines 94031-94062 only (the opening of its subsection "Universality for bounded ultraviolet profiles at a fixed horizon"), plus counts of the words Villain (0), heat kernel (17), Symanzik (0), twisted (8), Wilson action (57).

| ID | Assumption | Where | Needed or habit | If dropped or changed | Cost | Easier? |
|---|---|---|---|---|---|---|
| A1 | The bare weight is Wilson's, exp((beta/2) tr U_p) on every plaquette. | SK:27; FL:117 | Needed by the account as written. Not needed by the engine (I6: any reflection-positive, axis-symmetric weight). Not needed by the target, which is a statement on the continuum state. | Another plaquette class function with positive character coefficients (heat kernel, Manton, a mixed action) keeps the engine. | The account must be re-run for the new weight. READ account L94035-94040: at a fixed horizon the ultraviolet irrelevant profile "may now be any member of a bounded ball. Retuning the bare coupling to the same infrared value makes the final profiles exponentially close"; it "does not compare different horizons or construct an infinite-horizon flow". So the account has a fixed-horizon universality statement, not a statement that the continuum state is the same. | No, unless the new weight has an exact structure at the scale of the correlation length. I know of none in four dimensions (heat kernel: exact closure in two dimensions only). |
| A2 | The weight is the same on every plaquette (homogeneous, isotropic). | FL:112 (axis symmetry is used by Theorem S) | Needed by the method (the crossing step). | Anisotropic couplings (a Hamiltonian limit) break the axis exchange; Theorem S is lost in its present form. | Theorem S for unequal axes (the lane has boxes with unequal sides, not unequal couplings). | No. |
| A3 | The weight is real and positive. | AS:109 | Needed by reflection positivity. | Complex beta: the lane's Route Z (zeros) already lives there (SK:94). | - | Not re-examined here. |
| A4 | The seed is asked of the bare weight along first passage, not of an order-one effective weight. | FL:140-146 | Needed: the account does not reach order-one coupling and nothing bounds its effective weights there. | A seed for a class of weights at order one would need the flow into that class. | The flow from coupling gamma_H to order one, which is the crux in another form (SK:565). | No. |

**What group A gives.** No route. The freedom in the bare action is real (A1) and cheap for the engine, and the account has a partial universality statement. But no member of the class has a known handle at the correlation length. One observation is kept for Step 7: only the plaquette class function matters, so the natural variable is its list of character coefficients a_j(beta), and any exact operation on the theory acts on these lists (4.C uses this).

### 4.C The centre and the twists as variables

(Group B, the transfer operator, comes after this group; C was written first because 4.A pointed at it.)

| ID | Assumption | Where | Needed or habit | If dropped or changed | Cost | Easier? |
|---|---|---|---|---|---|---|
| C1 | The twist is a discrete datum: a class in H^2(torus; Z_2), put in by flipping the sign of the plaquettes of a dual surface Sigma. | FIN:891; (E16) | Habit. The target does not mention it (I3). | For SU(2) the element -1 is joined to +1 through conjugacy classes. The twist is the end point of a one-parameter family of surface insertions (Lemma C-alpha below). U(1) has the family with a central insertion at every angle; Q_8 and 2T have no family. | Nothing: the family is exact. | Not by itself (see below). |
| C2 | The twist ratio is read as a thermal mean of the centre flip c of a hyperplane of links (a "one-form" symmetry). | F2; (E16) | Habit. | In the box twisted in direction i by the colour rotation Omega_i, the same number is the thermal mean of a GLOBAL colour rotation Omega_1 (reading 2 of 3.3). The residual global group of that box is the normalizer of a circle in SU(2), whose component group is Z_2. | Nothing. | Opens soft-mode arguments (rotations by an angle), but a rotation by an angle other than 0 or pi does not respect the twisted box. |
| C3 | The sectors are summed with fixed weights (periodic, full, kappa, even). | SK:574-576 | Needed by the crossing step. | Make the class w a random variable: the ensemble with all classes summed is the SO(3) form; the ratio R is the odds P(w = v)/P(w = 0). With free Z_2 monopoles (a chemical potential lambda < infinity for cubes with odd sign product) the odds are exactly 1 for every lambda < infinity: PROVED by the change of variables sigma -> sigma sigma^v on the plaquette signs, which leaves d sigma unchanged. So the model with monopoles has no twist ratio at all; the SU(2) question lives only at lambda = infinity. | - | No route found. |
| C4 | The even sector is reached through the flux sectors (Theorem R, FUSE-suff, (FQ)). | SK:620-636 | Needed by the method, not by the target (C5 of Step 3). | A direct proof of (G_ev) would not meet c-odd states. | A criterion for the even sector alone, (EV-STEP); the lane has it only with (ES) as hypothesis. | Unknown. |

**Lemma C-alpha (the angle family; PROVED here, not checked by another model).** Let Sigma be the set of (1,i) plaquettes at one corner position, one for each transverse position y. For k in SU(2) let Z(k) be the periodic partition function in which each plaquette of Sigma is replaced by U_1(x) U_i(x+1) k U_1(x+i)^(-1) U_i(x)^(-1) (k is inserted at the far corner). Then:

1. Z(1) = Z and Z(-1) = Z^v.
2. Z depends on k only through its conjugacy class; more generally, with a different k_y at each plaquette, Z depends only on the classes of the k_y. Proof: the gauge transformation by h at the far corner site of the plaquette at y leaves every other plaquette unchanged and replaces k_y by h^(-1) k_y h; Haar measure is invariant; that site is a corner of exactly one plaquette of Sigma.
3. Averaging over h gives a class-function weight on the plaquettes of Sigma: for k of angle alpha (eigenvalues e^(+-i alpha)) and a plaquette of angle theta, w_alpha(theta) = exp(beta cos theta cos alpha) sinh(beta sin theta sin alpha)/(beta sin theta sin alpha). In characters: the coefficient d_j a_j of the Wilson weight is multiplied by psi_j(alpha) = sin((2j+1) alpha)/((2j+1) sin alpha). Proof: (1/2) tr(V k') = cos theta cos alpha - u sin theta sin alpha with u uniform on [-1, 1] when k' is uniform on the class; integrate; the character form is the identity "the average over h of chi_j(V h^(-1) k h) equals chi_j(V) chi_j(k)/d_j".
4. psi_j(pi - alpha) = (-1)^(2j) psi_j(alpha). So Z(pi - alpha) = Z^v(alpha): the twisted family is the mirror image of the untwisted one. At alpha = pi/2 the plaquettes of Sigma carry integer spins only, the weight is sinh(beta sin theta)/(beta sin theta), and twisted and untwisted are the same ensemble.
5. To second order, w_alpha = w_0 + (alpha^2/6) Laplacian(w_0): a small insertion is a heat-kernel smoothing of the plaquette weight on Sigma.
6. Exact flux form: Z({alpha_y}) = sum over labels J_y of prod_y [a_(J_y) chi_(J_y)(alpha_y)] times the integral of prod_y chi_(J_y)(U_(p_y)) against the weight with the plaquettes of Sigma deleted. So R is the mean of (-1)^(2 sum J_y) under a signed measure of total mass one on the flux labels of Sigma.

Remarks. (i) For 0 < alpha < pi the insertion is not central, Sigma cannot be moved, and Z(alpha)/Z(0) is expected to fall like exp(-phi(alpha) |Sigma|) (ARGUED at small alpha and large beta: phi is about beta alpha^2/4). The family joins Z and Z^v through an extensive barrier. So thermodynamic integration in alpha does not give R directly: R is the tiny asymmetry of the barrier. (ii) In the continuum such insertions are the surface operators of Gukov and Witten (recalled); I do not know a lattice source for items 2 to 4 (to be searched in Step 5). (iii) The family is the kind of object conclusion C1 of Step 3 asks for: it exists because the group is connected, and it is non-trivial because the group is not abelian.

**What group C gives.** An exact object (the angle family) and one exact negative fact (C3: with free monopoles there is no twist ratio). No route yet. The family is used in 4.E.

### 4.B The transfer operator on a torus

| ID | Assumption | Where | Needed or habit | If dropped or changed | Cost | Easier? |
|---|---|---|---|---|---|---|
| B1 | The box is a torus, periodic in all four directions. | FL:117-123; I6 | Needed by the method (the seed is a trace; the crossing step exchanges two periodic axes). Not needed by the target. | Free walls in all four directions. Then Z_free(n_1, ..., n_4) = <1, L^(n_1) 1> is a moment sequence of ONE vector, the constant function, for the transfer operator of the box with free walls. Only states that overlap the constant function enter: no flux sector, no twist, no centre flip. The normalization (the overlap of 1 with the ground state, a surface term) drops out of the second difference D = log Z_free(n_1) + log Z_free(n_1 + 2) - 2 log Z_free(n_1 + 1) >= 0. Volume, wall, edge and corner terms are affine in n_1 and cancel in D. So a gap seen from free walls is "log Z_free is affine in each side up to an exponentially small error" (ARGUED; a moment-sequence fact plus the multi-affine form of the bulk and boundary terms, which itself needs clustering to be proved). | A crossing engine for vector states in place of traces (not written anywhere I have read; SK:94 says the lane's Route Z uses boxes with free walls for zeros, to be compared in Step 5). The limit theorem (I8) would have to be redone for free walls. | It removes the odd sector from the form of the crux. It does not remove the wall: the hypothesis still has to be verified at the correlation length. |
| B2 | The seed is a trace over all states (the thermal sum). | AS:71 | Needed by the method. | A vector state, or a trace weighted by a symmetry (a "graded" trace Tr(c L^t)), sees fewer states. | See B1. | Form only. |
| B3 | The four axes are on the same footing; sides are comparable (a, a, c, d with c, d in {a, 2a}). | FIN:891 | Needed by the crossing step. | Boxes that are thin in two directions. On (N, N, n, n) with n fixed and N large every compact gauge group is disordered in the large plane, because the reduced theory is two-dimensional. For U(1) Villain the deficit of the large-plane twist is exactly of order exp(-N^2/(2 beta n^2)) (recalled two-dimensional formula with beta_2 = beta n^2). This does not contradict the U(1) test: the test binds on boxes of comparable sides. | The engine has no step from a thin box to a cube, and the physics says there is none in general (a slab of critical width is critical, N5). | Easier but off the path, unless the thin directions are twisted (see 4.D). |
| B4 | The time step is one lattice spacing; the transfer operator is positive (reflection positivity through sites and through links). | I6 | Needed. | - | - | - |
| B5 | Finite volume first, then the limit (I8). | FL:150-159 | Needed by the method. | Infinite volume directly (Dobrushin-Shlosman type uniqueness, cluster properties of the limit state). | Needs a mixing input at the correlation length (N12, N13); the lane's block criteria (I21) are of this kind. | No. |

**What group B gives.** One change of form (B1: free walls remove the flux sectors; price: a new engine). No route past the wall.

