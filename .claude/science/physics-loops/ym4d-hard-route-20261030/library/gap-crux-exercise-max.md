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


---

## Resumed again 2026-11-13 after the 03:06Z interrupt

Author: Claude Fable 5.2, max effort, laptop, one session, no subagents. Clone commit now: 9f1e04272b03270994c98fb4b9716e071924bac4 (branch claude/ym4d-hard-route; `git pull --ff-only` reported "Already up to date"; the run before this one was pinned at 93b3066d92, so the clone moved in between and the definition files are re-read only where a step uses them).
Finished and on disk above: Steps 0, 1, 2 (2.0, 2.1, 2.2), 3 (3.1 to 3.7), 4.A, 4.C (with Lemma C-alpha), 4.B. Not redone.

Remaining plan (one step per response; each appended before the next starts):

1. Step 4.D: one scale versus many (includes the thin twisted box that 4.B row B3 points to).
2. Step 4.E: SU(2) directly versus a larger or deformed theory that reduces to it (uses the angle family of Lemma C-alpha, as 4.C says).
3. Step 4.F: Euclidean versus not.
4. Step 4.G: the target, the discard tests, the beliefs and the working rules; then the summary of Step 4 (which assumptions, when changed, give a candidate route).
5. Step 4 continued: for each candidate route, its CRUX lemma, attempted as a real proof, one stage per response; fact tests applied (U(1) Coulomb, Q_8 and 2T, the Dobrushin and one-layer ceilings, (AN1), no fixed small number).
6. Step 5 (compare): open the closed files; search main and the open YM4D pull-request branches; name every repeat with path and line.
7. Steps 6 to 9 of the skill (filters, routes, attempts, report), as the skill text states them; correct the plain version of the wall.
8. The measure of the skill (row 721 Section 4.6), then the RESULT line.

### 4.D One scale or many

Read for this group: SK:586-600 again (the rule of 13.17 and the four means: (M1) a small number at the scale of the correlation length; (M2) a second small number after an exact change of variables; (M3) exact closure; (M4) a correlation inequality with a parameter, which gives a dichotomy). Nothing else.

| ID | Assumption | Where | Needed or habit | If dropped or changed | Cost | Easier? |
|---|---|---|---|---|---|---|
| D1 | The hypothesis is verified at ONE size, and the engine carries it up (Theorem S). | FL:117-123; I6 | Needed by the method. | A family P(n) with P(n_0) perturbative and a step P(n) => P(2n). | READ SK:592-596: a one-way step for a torus quantity is not queued (rows 720, 735: each candidate step is as hard as the seed; no precedent outside exact closure). The verdict is stated for torus quantities (periodic free energies). | No for a periodic free energy. Open for a quantity that is not one (rows D2, D4). |
| D2 | All sides of the box are comparable, so "size" is one number. | FIN:891 (boxes (a, a, c, d), c and d in {a, 2a}) | Needed by the crossing step. | Two sizes: a long plane (a, a) and a thin plane (n, n) that carries the background twist m = (3,4). The crux pair of the lane, m = (3,4) and v = (1,2), is then the twist of the long plane over a thin twisted plane. See Lemma D-tw and the three remarks below. | (i) The account on twisted tori (not in its scope, READ FL:153). (ii) A statement that joins thin n to n = a. | Easier at thin n for every group; the passage in n is the wall in a new place. |
| D3 | The many scales of the problem are the ultraviolet ones, and they are the account's work; the physical size is one. | I4, I24 | Needed (the account stops at coupling gamma_H). | Continue the flow to order-one coupling. | The crux in another form (READ SK:565, as 4.A row A4 says). | No. |
| D4 | The coupling is a fixed label; statements are proved one beta at a time. | I16 (ranges in beta) | Habit of the fixed-beta tools. | Treat beta as the scale: at a fixed number of sites, beta moves the physical size. Two exact tools then exist: Theorem CRIT (seeds form an open set, I18) and the derivative identity (D-beta) below. A continuity method needs the closed half: an a priori bound that keeps the seed size finite as beta grows. A monotone quantity would give one. | An inequality between the mean action of two twist sectors (below). No such inequality is in the inventory. | Unknown. Candidate route M (Step 7). |
| D5 | The scale of verification is the correlation length. | I17 (P1); I26 | Needed for any criterion whose conclusion is a gap at rate about 1/size (P1 is a spectral fact). | A criterion whose conclusion is weaker than a rate: for example a dichotomy (either a seed at some larger size, or a named kind of order), with the order ruled out by a separate argument. | The dichotomy and the refutation of the order, both for SU(2) only. | This is the form (M4) takes in every proved case (SK:590). It does not need a small number; it needs an inequality with a parameter. |

**Lemma D-tw (the thin twisted plane; PROVED here, classical: 't Hooft 1979, recalled; the lattice form is two lines).**
1. Two elements A, B of SU(2) with AB = -BA are A = i a.sigma, B = i b.sigma with a, b orthonormal; the pair is unique up to conjugation, and only +1 and -1 commute with both. Proof: tr A = tr(B A B^(-1)) = -tr A, so A = i a.sigma with |a| = 1, the same for B; AB + BA = -2 (a.b), so a.b = 0; SO(3) moves any orthonormal pair to any other; an element that commutes with both fixes two axes, so its rotation is the identity.
2. Put the twist m = (3,4) in as boundary conditions: fields are periodic in directions 3 and 4 up to conjugation by Omega_3 = A and Omega_4 = B. In the basis (a, b, a x b) of the Lie algebra, Ad(Omega_3) = diag(1, -1, -1) and Ad(Omega_4) = diag(-1, 1, -1). So each of the three components of a fluctuation field is antiperiodic in direction 3 or in direction 4.
3. Hence the lattice Laplacian on Lie-algebra-valued 1-forms with these conditions is at least 4 sin^2(pi/(2n)) > 0, for every length of directions 1 and 2, also infinite. There is no harmonic 1-form. On the co-closed fluctuations, the Hessian of the Wilson action at the vacuum U = 1 is beta/2 times d*d = beta/2 times this Laplacian (normalization of the trace form to be fixed when used). The twisted vacuum is isolated modulo gauge, and it is invariant under both centre flips of the thin directions (the flipped pair (-A, B) is conjugate to (A, B) by B).

**Three remarks on row D2 (ARGUED; physics recalled from Luscher and Weisz 1986 on the twisted tube, Gonzalez-Arroyo and Montero 1998, Tanizaki and Unsal 2022; none re-read).**
- (i) At thin n in physical units the system on (infinite, infinite, n, n) with the (3,4) twist has one vacuum and a fluctuation gap pi/n at tree level. The states with zero electric flux in the thin directions start near 2 pi/n. So in this geometry a gap of the centre-blind sector is a weak-coupling fact, and it does not come with confinement: the string tension of the long plane is exponentially small in 1/g^2(n).
- (ii) The crossed pair is the parity of the number of fractional instantons (charge 1/2, action pi^2 beta in lattice normalization, F4). In the dilute-gas form, with density zeta(n) per unit area of the long plane, Z^m is proportional to cosh(2 zeta a^2) and Z^(m+v) to sinh(2 zeta a^2). So R = tanh(2 zeta a^2) and the deficit is 2 exp(-4 zeta a^2) up to higher order. The crux number is small because the parity of a Poisson number of rare events is evenly split. This is the means (M2) at thin n.
- (iii) Fact tests. U(1) has no twisted vacuum of zero action, so it does not enter. Q_8 and 2T contain A and B, so they have the twisted vacuum and item 1; their vortex has action of order beta n^2 (no scale invariance), so zeta(n) falls like exp(-c beta n^2) and the deficit at n = a is not small above freezing. For SU(2) the classical action of the fractional instanton does not depend on n. This is where the Lie algebra enters (scale invariance of the classical action), as conclusion C1 of Step 3 asks.
- What is missing: the passage from thin n to n = a at fixed large a ("adiabatic continuity" in the physics literature, a conjecture there). A box that is thin and twisted is a small box: by the rate filter (I25) and P1 (I17) no seed holds in it, and the engine cannot start there. (Check of consistency: for a massless free field, antiperiodic in the thin directions, the gap times the side is a fixed number near 9; the engine's threshold needs about 26 to 32.)

**The derivative identity (D-beta) (PROVED, one line).** Write the Wilson weight as exp(-beta A(U)) with A(U) = sum over p of (1 - (1/2) tr U_p), and A^w for the same sum with the signs of the twist class w. Then for every pair of classes, d/dbeta log(Z^(m+v)/Z^m) = <A^m>_m - <A^(m+v)>_(m+v). So the twist ratio R_m(v) falls with beta at a fixed lattice exactly when the sector m + v carries more mean action than the sector m. Along a scaling trajectory, "R falls with beta at fixed lattice size" is "R rises with the physical size".

Checks of the sign of (D-beta) in known regimes (ARGUED): strong coupling (R = 1 - C exp(-sigma(beta) a^2) with sigma falling in beta: R falls); weak coupling at a fixed lattice, single-plane twist (the periodic sector has four flat toron directions that carry no action, the twisted sector has none: R falls like a power of beta); crossed pair at weak coupling (the sector m + v carries the fractional instanton: R falls like exp(-pi^2 beta)); two dimensions with the heat-kernel weight (R = a ratio of theta sums in A/beta: falls). I know of no regime where R rises with beta. For Z_2 and U(1) Villain the statement is a Griffiths-type inequality. For SU(2) it is OPEN; Corollary NS0 (I19) removes the term-by-term proof.

**What group D gives.** Two candidates for Step 7. Route T: the thin twisted plane as a second size, with (M2) at thin n and the passage in n as its crux. Route M: beta as the scale, with the sign of (D-beta) (a comparison of mean actions between twist sectors) as its crux, to be joined to a dichotomy (D5). Neither is past the wall yet. Their crux lemmas are attempted after 4.G.

### 4.E SU(2) directly, or a larger or deformed theory that reduces to it

Nothing new was read for this group. Every outside result is `recalled`.

| ID | Assumption | Where | Needed or habit | If dropped or changed | Cost | Easier? |
|---|---|---|---|---|---|---|
| E1 | The group is SU(2) at N = 2. | I3 (the target) | Needed by the target. | SU(N) at large N has a second small number (M2). | It is another theorem; nothing carries it to N = 2. | Not on the path. |
| E2 | The theory has no matter field. | I1 | Needed by the target. Not needed by the engine: the engine holds for any reflection-positive, axis-symmetric weight (I6). | Add a fundamental scalar of fixed length. In unitary gauge the weight gains exp((kappa/2) sum over links of tr U_l). The centre symmetry is gone: no flux sector, no twist, one vacuum; the periodic trace then sees only massive states. For beta small (all kappa) and for kappa large the theory is analytic and gapped (Osterwalder and Seiler 1978; Fradkin and Shenker 1979). At weak gauge coupling with the vector mass far above the confinement scale, the coupling is small at the scale of the correlation length: (M1) holds there in principle (precedent on a unit lattice for the abelian model: Balaban, Brydges, Imbrie, Jaffe 1984). | (i) The account with a scalar field: not written. (ii) The way back to kappa = 0 passes the region where the vector mass meets the confinement scale; the seed set is open there (CRIT) and nothing closes it. | Easier at large kappa. The way back is the wall in a new place. |
| E3 | The same, with an adjoint scalar. | - | - | The centre and the twists survive. In four dimensions the Higgs phase has a massless photon. | It moves toward the U(1) test, not away from it. | No. |
| E4 | The centre is not a dynamical variable (one class w at a time). | 4.C row C3 | Needed by the target (SU(2), not SO(3)). | U(2) = (SU(2) x U(1))/Z_2 with a separate U(1) coupling beta': a class w of the SU(2) part comes with U(1) flux pi w. At beta' = infinity only w = 0 survives (SU(2)); at beta' = 0 all classes have equal U(1) weight (the SO(3) sum of row C3). | - | No: the odds of the classes are the twist ratios times U(1) factors. Same content as C3. |
| E5 | The twist is put in at full strength. | 4.C row C1 | Habit. | The angle family of Lemma C-alpha. With the mirror identity Z(pi - alpha) = Z^v(alpha): R = exp(Phi(pi/2) - Phi^v(pi/2)), where Phi and Phi^v are the free energies of the half-angle defect (integer spins on Sigma) in the untwisted and in the twisted theory (PROVED from item 4 of the lemma: Z^v(0)/Z(0) = [Z^v(0)/Z^v(pi/2)] / [Z(0)/Z(pi/2)] and Z^v(pi/2) = Z(pi/2)). | Nothing. | Form only: the deficit is the difference of two extensive defect free energies with the same leading term. |
| E6 | The plaquettes of Sigma carry the same coupling as the rest. | I1 | Habit. | Let beta_Sigma run from 0 to beta. At beta_Sigma = 0 the plaquettes of Sigma are absent and R = 1 exactly. The local form of (D-beta) holds: d/dbeta_Sigma log R = <A_Sigma>_0 - <A^v_Sigma>_v. So R(beta) = exp(-integral over beta_Sigma of the excess action ON Sigma of the twisted sector) (PROVED: differentiate the two partition functions; A_Sigma is the sum over Sigma of 1 - (1/2) tr U_p, with the twisted sign in A^v). | Nothing. | It localizes route M on the surface: the twist deficit is an integral of a surface quantity. Used in the crux stage. |
| E7 | SU(2) variables are used directly. | I1 | Habit. | The split into SO(3) links and Z_2 link signs (Mack and Petkova 1979): for a fixed SO(3) configuration the signs form a Z_2 gauge theory with couplings K_p = (beta/2) abs(tr U_p) >= 0, frustrated exactly on the cubes where the SO(3) field has a Z_2 monopole. On monopole-free SO(3) configurations it is a ferromagnetic Z_2 gauge theory in the twist sector h + v, where h is the class of the SO(3) configuration. Ferromagnetic Z_2 gauge theory has Griffiths inequalities. | The monopoles (frustration), whose density is about exp(-c beta) per cube at large beta: small but not zero, and not uniformly controlled. | Unknown. It gives conditional monotonicity; see route M. |
| E8 | The weight is Wilson's and has no semigroup structure. | 4.A row A1 | Needed by the account as written. | With the heat-kernel weight the theory is two-dimensional Yang-Mills on the 2-skeleton of the lattice: each face is a disc of area 1/beta, and faces may be subdivided or merged freely where only two meet (the semigroup law). The insertion of Lemma C-alpha is a puncture with fixed holonomy class in each face of Sigma. | The account for the heat-kernel weight (4.A row A1: fixed-horizon universality only). Six faces meet at every link, so the closure stops there. | No. |

**What group E gives.** No route of its own. Every deformation that makes the theory gapped by a small number (E2) leaves the way back as a continuity question, which is the closed half that row D4 asks for. Three exact forms are kept for the crux stage: E5 (the deficit as a difference of two defect free energies), E6 (the deficit as an integral of the excess surface action; R = 1 at beta_Sigma = 0), E7 (the conditional ferromagnetic Z_2 theory).

**Fact test applied to E2 (the Higgs deformation).** U(1) with a charged scalar is gapped at large kappa as well, and loses its gap on the way back. So the deformation alone tells nothing apart; the way back must use the group. This is recorded so that the route is not counted as a route.

### 4.F Euclidean or not

Nothing new was read for this group. Outside results are `recalled`.

| ID | Assumption | Where | Needed or habit | If dropped or changed | Cost | Easier? |
|---|---|---|---|---|---|---|
| F1 | Time is a lattice direction; the object is the transfer operator. | I6 | Needed by the method (axis exchange) and by the account (a Euclidean flow). | Continuous time: the Kogut-Susskind operator H = (g^2/2) H_E + (2/g^2) H_B on gauge-invariant functions of the spatial links, with H_E = minus the sum of the link Laplacians and H_B = sum over spatial plaquettes of 1 - (1/2) tr U_p. It is a Schrodinger operator on SU(2)^E, a compact manifold whose Ricci curvature is 1/4 per link direction for every number of links. | The time-continuum limit (anisotropic couplings; 4.A row A2: Theorem S is lost in its present form). The account does not give it. | It gives operator inequalities (Lemma F-flux) and the ground-state form (F2). No route by itself. |
| F2 | The gap is read from thermal sums. | AS:71 | Needed by the method. | Ground-state form: E_odd - E_0 = (g^2/2) inf over c-odd f of (integral of grad f squared against Psi_0^2) / (integral of f^2 against Psi_0^2). The crux becomes a Poincare inequality for odd functions under the free involution c, for the measure Psi_0^2. | A handle on Psi_0. Bakry-Emery needs Hess(-log Psi_0^2) > -1/4 on every link direction; at weak coupling this fails pointwise (Psi_0 concentrates near flat connections), so only an integrated form can hold: the Hamiltonian twin of (G2). | No. |
| F3 | The fifth (stochastic) time is not used. | (G2), I15 | - | The Langevin generator is a sum of terms Q_l* Q_l that all vanish on the same state: a frustration-free form. A finite-size criterion of Knabe type would ask for a gap of each block generator above about 1/n. A block generator acts fibrewise over the exterior configuration, so its gap is the worst case over exteriors. | The lane has the worst-case ceilings (I22) and "(AN1) is equivalent to the worst-case exterior bound". | No, by I22 (to be confirmed against the files at Step 5). |
| F4 | Space is a flat torus. | FL:117 | Needed by the method and the account. | A four-sphere or a hyperbolic space: no flat directions, no flux sectors, one vacuum; on hyperbolic space the infrared is cut off by the curvature (Callan and Wilczek 1990). | No regular lattice, no transfer operator, no account. The return to flat space is a continuity question again (the pattern of 4.E). | No. |
| F5 | Only reflection positivity is used from the quantum structure. | I6 | Habit. | Real time: locality (Lieb-Robinson bounds) turns a gap into clustering, not clustering into a gap. Positive-commutator methods need an operator A with i[H, A] bounded below on the excited states; the dilation is the natural A, and its commutator is the trace anomaly, which is the lattice identity (D-beta) again: by Feynman-Hellmann, d(E_1 - E_0)/d log g^2 = the excess of (g^2/2) H_E - (2/g^2) H_B in the first excited state over the vacuum. | - | Form only. |

**Lemma F-flux (PROVED here; the strong-coupling tension as an operator bound; classical).** Let c be the centre flip of the links that cross one hyperplane perpendicular to direction 1, and a_1 the length of direction 1. On the c-odd gauge-invariant functions, H_E >= (3/4) a_1. Proof. Expand in the Peter-Weyl basis of each link: a basis function carries a spin j_l on each link, and H_E multiplies it by the sum of j_l (j_l + 1). Gauge invariance at a site forces an even number of half-integer spins there, so the links with half-integer spin form a closed chain mod 2. The flip c multiplies the basis function by (-1) to the number of half-integer links that cross the hyperplane. This parity is the same for every parallel hyperplane, because the chain is closed. So a c-odd basis function has a half-integer link on each of the a_1 hyperplanes, and each costs at least (1/2)(3/2) = 3/4.

Why it does not give the crux: the bound is on H_E alone. E_0 has a volume term from H_B, and the difference E_odd - E_0 needs the cancellation of volume terms. A map from the odd sector to the even one by multiplication with a Polyakov line gives only an upper bound on the flux energy (the bound that every compact group has, N20).

**What group F gives.** No route. One exact operator fact (Lemma F-flux), and the same identity (D-beta) in a third form (F5).

### 4.G The target, the discard tests, the beliefs and the working rules

| ID | Assumption | Where | Needed or habit | If dropped or changed | Cost | Easier? |
|---|---|---|---|---|---|---|
| G1 | The target is a spectral statement on the cyclic sector of tr(F^2) for the continuum state of the account. | SK:29-33 | Needed (the owner's target T0). | A lattice gap at one fixed beta is consumed by nobody (F6). Exponential clustering of the tr(F^2) two-point function alone is the same statement on that sector. | - | No change. |
| G2 | The target does not ask for confinement. | I3; C5 | Needed by the target; the method adds confinement (the trace over flux sectors). | A route that never meets a flux sector: free walls (B1), a sphere (F4), the fundamental scalar (E2), the thin twisted plane where the centre-blind gap is perturbative (D2 remark (i)). | Each has its own cost row. | Form only, in each case. |
| G3 | Discard test: "it also runs for U(1) in the Coulomb phase". | brief; SK:3 | Needed (a logical filter). | Nothing: it stands. Note what it binds: the infrared step taken ALONE. A route whose input is the account's flow already uses asymptotic freedom, which U(1) lacks. | - | - |
| G4 | Discard test: "it also runs for Q_8 or 2T at order one". | brief (rows 838, 843) | Needed for every argument at a FIXED order-one beta. Habit for an argument in physical units along first passage: there beta_K tends to infinity and the finite groups are frozen from some K on, so any statement that is uniform along first passage fails for them for a trivial reason, and the test tells nothing. | For first-passage routes the binding tests are U(1) and "no fixed small number". For fixed-beta routes the finite-group test stays. | - | It removes one test from routes of the first kind. It does not make them exist. |
| G5 | Discard test: "no fixed small number reaches order one". | brief; P1 (I17); I25 | Needed for a criterion whose conclusion is a rate. | See D5: a dichotomy does not need a small number. A group-blind dichotomy with an order-one threshold cannot be met from perturbative data, because U(1) in its Coulomb phase has twist ratios of order one at every scale (ARGUED: the Villain formula gives R = a ratio of theta sums in the renormalized coupling). So the threshold step must itself use the group. | - | No. |
| G6 | Discard test: "a statement below the correlation length does not count". | Step 1; SK:57 | Habit as a rule; true for rates (P1). | Statements below the correlation length count if an exact identity carries them up. The identity (D-beta) and its surface form (E6) are exact at every scale and for every group. What is missing is a sign or a size for their right side. | An inequality for the excess surface action. | Unknown. |
| G7 | The proved ceilings (worst-case Dobrushin, one-layer twist bounds, (AN1)). | brief; I22 | Needed: they are theorems about those methods. | - | - | - |
| G8 | Belief: SU(2) has a gap and no bulk transition; the crossover is near beta = 2.2. | N4 | The plan depends on it. | If false, the target is false for the account's state, or the first-passage sequence passes a transition. Numerics do not suggest it. | - | - |
| G9 | Belief B4: no proved case crosses many correlation lengths without one of (M1)-(M4). | SK:598 | Habit (a reading of ten families). | A fifth means. Candidates met in this step: (a) an exact identity in the scale with a signed right side (D-beta), which is (M4) with the scale as the parameter; (b) a soft-mode argument, which gives statements at every coupling but no rate (recalled: Mermin-Wagner proofs by relative entropy). | - | Unknown. |
| G10 | Belief: the account's packages A-H hold. | I2 | Needed by the target as stated. | The target becomes conditional. Not this run's matter. | - | - |
| G11 | Working rule: no computer-assisted proof; Lean-formalizable. (Paper only; the run obeys it.) | brief | Owner rule. | Not used: a certified numerical check of a seed. At 12.9 correlation lengths and beta in the window the lattice has about 30 sites per side or more; no certified integration reaches that. So the rule costs nothing here. | - | - |
| G12 | Working rule: build on the account; the seed is asked of the bare weight along first passage. | FL:140-146 | Owner rule and a need of the reduction. | Not used: a self-contained infrared construction. | - | - |
| G13 | Hidden: the constants of the engine (1/5041, 1/192, 1e-7) are part of the wall. | 3.5.3 | Habit. | They are consequences of the engine. Any engine has a threshold above the value that a massless free field reaches in a box (ARGUED in 4.D). | - | No. |
| G14 | Hidden: the dimension is exactly four and is not a parameter. | - | Needed by the target. | Nothing rigorous uses the dimension as a parameter. | - | No. |

### 4.H Ranking, and what Step 4 gives

Ranked by how much the problem changes if the assumption is dropped. One line each on what the lane would do differently.

1. **C2/C4/G2: the flux sectors and the twists are a cost of the trace, not of the target.** The lane would build a second engine on vector states with free walls (B1), where no flux sector exists. Changes an owner decision only if such an engine is proved; the wall (verification at the correlation length) stays.
2. **D4/G6: beta is a fixed label; statements below the correlation length do not count.** The lane would treat the twist ratio as a function of the coupling on the twist surface and study the exact identity (E6). A sign for its right side would be a monotonicity theorem in the scale. This is route M.
3. **D2: all sides are comparable.** The lane would compute the crossed pair on a thin twisted plane, where it is a dilute-gas parity (M2), and ask for the passage in the thin size. This is route T.
4. **G4: the finite-group test binds every route.** It binds fixed-beta arguments only. The lane would sort its routes into fixed-beta ones (finite-group test binding) and first-passage ones (U(1) test binding).
5. **C1: the twist is discrete.** The angle family (Lemma C-alpha) and the mirror identity give the deficit as a difference of two defect free energies (E5). No use found yet beyond the form.

Rows whose drop would change an owner decision: G11 and G12 (owner rules; questioned on paper only, not used); G1 (the target).

**Exact statements proved in Step 4 (all by me, none checked by another model):** Lemma C-alpha (six items); the odds identity of row C3; Lemma D-tw; the derivative identity (D-beta) and its surface form (E6); the defect form (E5); Lemma F-flux.

**Candidate routes for the crux stage:** M (monotonicity in the surface coupling; crux: the excess surface action of the twisted sector has a sign and a size), T (the thin twisted plane; crux: the passage in the thin size), W (free walls; crux: a criterion on vector states that is verified at the correlation length). The crux stage takes M first, because its crux is one inequality on a finite lattice and can be tested and attacked directly.
