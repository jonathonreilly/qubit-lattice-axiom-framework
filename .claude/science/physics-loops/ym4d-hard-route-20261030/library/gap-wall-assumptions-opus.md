lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-17T02:08Z

# Gap wall: first-principles assumptions exercise (row 1052, `gap-wall-assumptions-opus`)

Started 2026-11-16T14:08Z on Mac mini worker 3 at commit eb77948ca, branch claude/ym4d-hard-route. Research-stage working state; no status claimed.

Provenance note. Before the row was read, the worker read `GOAL.md` in full (the dispatch prompt asked for it). That is a lane file under the row's rule for steps 1-4. Its content (T0 existence without gap, the Sussman-Alpoge porting method, the no-computer-assist rule) is therefore known to this worker before step 5; steps 1-4 below are written from the target and general knowledge and flag where GOAL.md wording could have leaked in. No `parts/` or other `library/` file is opened before step 5.

## Plan (at most eight steps; one per response, appended here before the next)

1. Fetch the exercise skill (qubit-lattice-axiom-framework at 8b11ae2bb9) and its references into a new /tmp folder; record its steps 0-9 here. Also the procedural FINISH sections (Working efficiently, Rules, Build on published work).
2. Skill steps 0-2: target stated twice (plain, exact); known-true list with DEF/AXIOM/SUPPLIED/THM/BELIEF marks and sources.
3. Skill step 3: reason up to what any proof must establish; the Elon pass over every requirement (who requires it, can it be deleted, simplify).
4. Skill step 4: the full assumption set, six groups, at least forty, each with "if wrong" and a rank.
5. Skill step 5: read `parts/gap.md`, `library/gap-dichotomy.md`, `library/gap-crux-exercise4-max.md`, `library/gap-direction3-max.md`; say which assumptions the lane imposes silently and which requirements it does not need.
6. Skill step 6: audit every discard test on file with source line; re-judge set-aside methods.
7. Skill steps 7-8: routes from top-ranked dropped assumptions; kill tests; real attempts on the best one or two.
8. Skill step 9 and the RESULT line: five assumptions most likely wrong and what each opens.

## Step log

### Header (skill Output rules)

- Written by: Anthropic, Claude Opus 5.5 (claude-opus-5-5), effort high, one Claude Code session on Mac mini worker 3, no subagents.
- Commit: eb77948ca (claude/ym4d-hard-route). Date: 2026-11-16.
- **Nothing in this file is checked by another model.** Every statement here is `argued` at best until a check record by another model exists.
- Skill source: `docs/ai_methodology/skills/exercise/SKILL.md` of jonathonreilly/qubit-lattice-axiom-framework at 8b11ae2bb9 (703 lines, read in full), fetched to `/tmp/ex1052-skill/`. References it names, each fetched into its own new folder `/tmp/ex1052-ref-*`: `skills/SKILL_FRESHNESS_CHECK.md` (35 lines), `skills/physics-loop/references/proof-search-governance.md` (126 lines, read in full), `skills/physics-loop/references/assumption-import-audit.md` (171 lines), `RULES.md` (200 lines), `procedures/research.md` (150), `procedures/check.md` (148). The last four were fetched; only governance was read in full in step 1 (see "did not cover").
- Framework refresher: replaced. This is a standalone proof target whose contract (`GOAL.md`) reads no framework axiom or primitive, so per the skill the target contract and its rules (GOAL.md "No computer-assisted steps", FINISH.md "Working efficiently" and "Rules") replace the framework refresher list.

**What this run did not cover** (kept current):
- No blind check of the plain statement (no subagents allowed); corrected in step 9 instead.
- `assumption-import-audit.md`, `RULES.md`, `research.md`, `check.md`, `SKILL_FRESHNESS_CHECK.md`: fetched, not read in full (skill freshness: the row pins 8b11ae2bb9, so that revision is used for skill and references alike).
- FINISH.md was read only in its row 1052/1053 lines and the procedural sections "Working efficiently" and "Rules" (lines 320-351) and the line 64 "Build on published work" item before step 5. GOAL.md was read in full before the row (see provenance note).
- Literature in steps 2-4 is from statements of results only, mostly `recalled` (not re-read in this run) unless a page is named.

### Status block (one line per plan step)

1. done: skill and references fetched; skill steps 0-9 recorded below.
2. done: target stated twice (plain 148 words; precise T.1-T.4 with forbidden weakenings), facts A0, A1 argued; inventory I1-I34, nearest models N1-N14, beliefs B1-B8.
3. done: A2 argued (gap from uniform rate on a total set, F-dependent constants, passes to limits); conclusions C1-C11; Elon pass E1-E17 leaves (D); price = crossover-scale estimate or a transport mechanism (reading).
4. done: 62 assumptions in six groups (a1-a8, b1-b13, c1-c12, d1-d9, e1-e12, f1-f8), each with if-wrong; ranked; owner-decision rows f1, f2, f4, a1, a2, a8, c1.
5. not done.
6. not done.
7. not done.
8. not done.

### Step 1 result: the exercise skill's procedure, as this run will follow it

- Step 0: locate the record without reading arguments; split into "open now" (target, wall statement, definitions, statements of cited theorems) and "closed until step 5" (attack files, route notes, digests, set-aside lists, earlier exercises). Literature: statements of results only before step 5.
- Step 1: wall stated twice (plain at most 150 words, one analogy at most; precise with quantifiers, allowed premises, forbidden weakenings, what counts).
- Step 2: inventory, every item marked DEF / AXIOM / SUPPLIED / THM (with standing and reading state: read in full / in part / recalled) / BELIEF; include nearest models where the target is false or true for a known reason (these become step-6 tests).
- Step 3: reason up only from the inventory: what follows at once; least a solution must contain; smallest object; where the result can come from; make the requirement less wrong; price it. End with conclusions C1, C2, ... naming inventory items.
- Step 4: assumptions table in groups (a) target, (b) formulation, (c) reduction, (d) discard tests, (e) beliefs, (f) working rules; columns ID / assumption / where used / needed-by-target vs method vs habit / if wrong / easier? / check. Rank by how much the problem changes when dropped; first five with one line each; mark rows whose drop would change an owner decision. Group (f) questioned on paper only.
- Step 5: open the closed list; per conclusion and per ranked assumption: already in earlier work (yes / partly / new), where, search scope. "New" only after a search of the whole lane record by two wordings.
- Step 6: 6a every set-aside method; 6b first principles on the blockage (one sentence); 6c audit each discard test in valid logical form (refutation needs M' in K with H(M') true and T(M') false; otherwise it is a constraint, with a range); 6d re-judge every verdict.
- Step 7: routes from top-ranked dropped assumptions, returned tools, a new target form, and 6b; concrete-return contract; one outside-vocabulary lens and one misframing pass; kill pass (assumes target? contradicts checked result? already tried? fails a valid test? breaks an owner rule? terminal obligation target-equivalent => blocked-equivalent); rank by change / cost.
- Step 8: real attempts on the best one or two; search registry and queue first; reductions count only if proved or exactly named; runs pre-registered, under the numeric lock.
- Step 9: plain report for the owner (wall, found, filters corrected, at most three routes, what not to do, exact price, work items with first being a check request, appendix), ending in one `RESULT:` line; strong words re-read.

Row 1052's additions to the skill: steps 1-4 from first principles about the Jaffe-Witten target (existence plus mass gap, SU(2), R^4), at least forty assumptions including the listed field-wide ones, an Elon pass (who requires each requirement; delete; simplify; only then optimise), and a RESULT line naming the five assumptions most likely wrong and what each opens.

### Step 0 of the skill (record located, files sorted; no arguments read)

Brief: row 1052 is the brief. Output file: this file. Budget: no cost cap; owner rules bind (no computer-assisted steps; numeric lock; no subagents; no commits).

- **Open now:** the target as stated in row 1052 (Jaffe-Witten: SU(2) quantum YM on R^4, OS or Wightman axioms, non-trivial, mass gap Delta > 0); the general literature's statements of results (recalled; listed in step 2).
- **Closed until step 5:** `parts/gap.md`, `library/gap-dichotomy.md`, `library/gap-crux-exercise4-max.md`, `library/gap-direction3-max.md`, and every other `parts/` and `library/` file; FINISH.md beyond row 1052-1053 and the procedural sections; the folders `~/ym4d-papers/gap-precedent-lit-*` and `gap-mono-lit-*` (the lane's literature record; their directory names show the lane looked at Balaban-Federbush (bf?), Glimm-Jaffe-type (gk?), Gawedzki-Kupiainen, Ito 1984, Ito-Tamura, Kopper, Kupiainen, Engels, approximate duality 1703.07335, Giudice-Piemonte 1708.01216; only these names were seen, no contents).
- **Already known to this worker from GOAL.md (leak, disclosed):** the lane's existence target T0 (OS axioms without gap) built on Balaban and the Sussman-Alpoge complete account; the no-computer-assist rule; that the far-sphere flux hypothesis behind SA's O(4) clause is not derived. Nothing about the gap lane's (W), seed or dichotomy is known before step 5 beyond the words in row 1052 itself ("the repaired (W), the seed, the dichotomy, route (ii)").

### Plan step 2 = skill steps 1-2: the target twice, and the inventory

Written from the target only. No lane file beyond row 1052 and GOAL.md (disclosed) was open. Literature items are `recalled` (from memory, not re-read in this run) unless a page is named; their standing is "published, not checked in this repository" unless said otherwise.

#### Skill step 1, plain version (148 words; no blind check was possible, see header)

We want a written, checkable proof that one particular quantum field theory exists. It is the simplest relative of the theory of gluons, the particles that carry the strong nuclear force (gauge group SU(2)), in our four dimensions of space and time. "Exists" means a mathematical object that obeys the standard rules every relativistic quantum theory must obey. It must also be genuinely interacting, not a disguised free theory. And it must have a mass gap: every excitation above the empty state costs at least some fixed positive energy. Why it matters: it would show from first principles why this force has short range; it is a Clay Millennium problem. What the evidence covers: proofs for simpler models, for coarse lattices at strong coupling, and for short distances; computer simulations at the scales in between. Nothing proved covers those middle-to-large distances. Passing means a proof of all three properties together.

#### Skill step 1, precise version

Source of the target: A. Jaffe and E. Witten, "Quantum Yang-Mills theory", Clay Mathematics Institute official problem description (2000; in *The Millennium Prize Problems*, CMI/AMS 2006, pp. 129-152). Recalled, not re-read in this run; the official one-sentence statement is recalled as: "Prove that for any compact simple gauge group G, a non-trivial quantum Yang-Mills theory exists on R^4 and has a mass gap Delta > 0. Existence includes establishing axiomatic properties at least as strong as those cited in [Streater-Wightman; Osterwalder-Schrader]." The description also asks (recalled) for local quantum fields in correspondence with gauge-invariant local polynomials in the curvature F and its covariant derivatives, and that correlation functions agree at short distances with asymptotic freedom and perturbative renormalisation theory, including a stress tensor and an operator product expansion with the singularities asymptotic freedom predicts.

Target **T** (this row restricts G to SU(2)): there exist

1. a separable Hilbert space H_phys, a unit vector Omega, a strongly continuous unitary representation U of the Poincare group (covering group) with Omega invariant and unique up to phase among invariant vectors, joint spectrum of the energy-momentum P in the closed forward cone;
2. operator-valued tempered distributions O_alpha(x) (at least one for each gauge-invariant local polynomial alpha in F and covariant derivatives, e.g. tr F_{mu nu}F_{rho sigma}), with a common dense invariant domain, Poincare covariant, local (spacelike commutativity), with Omega cyclic for the polynomial algebra they generate (Wightman axioms W0-W3); equivalently, by Osterwalder-Schrader reconstruction, Schwinger functions S_n satisfying OS0 (temperedness with the OS-II linear growth condition), OS1 (Euclidean covariance under E(4)), OS2 (reflection positivity), OS3 (symmetry), OS4 (clustering);
3. **non-triviality:** the theory is not a generalised free field; in the JW sense, its short-distance behaviour matches asymptotically free perturbation theory (running coupling g(mu) -> 0 as mu -> infinity at the one-loop rate b_0 = 11/(24 pi^2) for SU(2) in the convention dg/dlog mu = -b_0 g^3 + ...; recalled), with a stress tensor and an OPE;
4. **mass gap:** there is Delta > 0 with spec(H) restricted to Omega-perp contained in [Delta, infinity), where H = P_0.

Quantifiers: one theory (exists), one Delta (exists), all of Omega-perp (for all states of H_phys). Domain: R^4, infinite volume, no cutoffs. G = SU(2) fixed (JW asks for every compact simple G; the row restricts).

Allowed premises (owner contract): mathematics; written proofs; literature rebuilt in the repository; no computer-assisted step (GOAL.md, "No computer-assisted steps").

Forbidden weakenings: gap only in finite volume, or only at a fixed lattice spacing, or only in lattice units that go to zero in physical units; gap only on a subspace generated by fewer fields than the theory's local gauge-invariant fields (unless the reduced field set is shown to generate the whole H_phys); "existence" of a trivial theory (H_phys = C Omega, or a Gaussian/free theory); a gap for a theory with no proved connection to Yang-Mills (no asymptotic-freedom identification); a gap holding along a subsequence of cutoffs whose limit theory is not shown to satisfy the axioms.

Required degenerate cases: the trivial theory satisfies every axiom and has a vacuous "gap" (H_phys = C Omega), so non-triviality is load-bearing; a massive free field has a gap and is excluded by non-triviality; a theory with several vacua violates uniqueness and so violates the gap clause on Omega-perp.

Outcomes that do not count as closure: existence without gap (that is T0 of GOAL.md, a sub-target); gap for lattice theory at strong coupling only; any gap that is not uniform in the cutoff in physical units; the gap reduced to an unproved statement (that is a price, not closure).

**Argued fact (A0), used below.** In a Wightman theory, "spec H on Omega-perp in [Delta, inf)" is equivalent to "joint spectrum of P on Omega-perp in {p : p^2 >= Delta^2, p_0 > 0}". Proof: (<=) on Omega-perp, p_0 >= sqrt(Delta^2 + |p|^2) >= Delta. (=>) if a spectral point p with 0 <= p^2 < Delta^2 and p_0 > 0 existed on Omega-perp, the spectral measure of P gives nonzero spectral projections near p; a Lorentz boost (U is unitary and leaves Omega-perp invariant, since Omega is invariant) carries them to a neighbourhood of (sqrt(p^2), 0) with energy below Delta if p^2 > 0; for p^2 = 0 boost to energy below Delta. Contradiction. Mark: argued (spectral theorem plus covariance; no further input).

**Argued fact (A1): Euclidean form of the gap.** In the OS setting, with E_+ the positive-time algebra, (.,.)_OS the reflection-positive form and T_t the Euclidean time translation, the gap Delta on Omega-perp is equivalent to: for all F in E_+ and t >= 0, |(F, T_t F)_OS - |<F>|^2| <= e^{-Delta t} ((F,F)_OS - |<F>|^2). Proof: OS reconstruction gives e^{-tH} as the image of T_t on the quotient of E_+ (contraction semigroup, H >= 0); the spectral theorem on the closed span of the images of E_+ minus their Omega component gives (=>); (<=): if the spectral measure of some unit vector psi in Omega-perp put mass on [0, Delta - eps), approximate psi by images of E_+ (they are dense) and the inequality at large t fails. Mark: argued, given OS reconstruction (THM, recalled below).

#### Skill step 2, inventory

Columns: # | item | mark | source | standing and reading state.

**Definitions**

| # | Item | Mark | Source | Standing |
|---|---|---|---|---|
| I1 | Wightman axioms W0-W3, and mass gap as in T.4 | DEF | Streater-Wightman, *PCT, Spin and Statistics, and All That* (1964); JW 2000 | recalled |
| I2 | OS axioms OS0-OS4 with the linear growth condition | DEF | Osterwalder-Schrader, CMP 31 (1973) 83; CMP 42 (1975) 281 | recalled |
| I3 | Yang-Mills action S(A) = (1/(4 g^2)) int tr-norm |F_A|^2, gauge group SU(2), gauge-invariant local polynomials in F and covariant derivatives | DEF | standard | - |
| I4 | Lattice gauge field: U: oriented links -> SU(2), U(-l) = U(l)^{-1}; gauge group acts at sites; plaquette holonomy U_p | DEF | Wilson, PRD 10 (1974) 2445 | recalled |
| I5 | Gap on Omega-perp is equivalent to uniform exponential decay of truncated positive-time correlations in OS norm (fact A1) | DEF/argued | this file, A1 | argued |
| I6 | Non-triviality has no single agreed formal definition; JW gives it by agreement with asymptotically free perturbation theory at short distance | DEF (incomplete) | JW 2000 | recalled |

**Theorems (published; none checked in this repository by this run)**

| # | Item | Mark | Source | Standing / reading |
|---|---|---|---|---|
| I7 | OS reconstruction: Schwinger functions with OS0 (linear growth), OS1-OS3 give a Wightman theory; OS4 gives uniqueness of the vacuum | THM | Osterwalder-Schrader 1973, 1975 (OS II supplies the growth condition after the 1973 gap) | recalled; the source writes the proof |
| I8 | Wilson's lattice action beta sum_p (1 - (1/2) tr U_p) is reflection positive (site and link reflections); a positive self-adjoint transfer matrix T with norm at most 1 exists on gauge-invariant L^2 of a time slice | THM | Osterwalder-Seiler, Ann. Phys. 110 (1978) 440; Seiler, LNP 159 (1982) | recalled |
| I9 | Strong coupling: for beta below some beta_0(d) > 0, the infinite-volume Wilson lattice theory exists, is unique, has exponential clustering (lattice mass gap) and an area law for Wilson loops | THM | Osterwalder-Seiler 1978 (cluster expansion) | recalled |
| I10 | Functional-inequality form of I9: for beta < c/d (explicit c), lattice SU(N) Yang-Mills satisfies a log-Sobolev / Poincare inequality uniform in volume, hence exponential decay; uses Ricci curvature of SU(N) via Bakry-Emery | THM | H. Shen, R. Zhu, X. Zhu, "A stochastic analysis approach to lattice Yang-Mills at strong coupling", CMP 400 (2023) | recalled |
| I11 | Area law extended beyond the classical strong-coupling region (still beta of order one in lattice units, not beta -> infinity) | THM | S. Cao, R. Nissim, S. Sheffield, "Expanded regimes of area law for lattice Yang-Mills theories" (2023 preprint) | recalled; exact range not re-read |
| I12 | UV stability of four-dimensional lattice Yang-Mills: bounds on effective actions and partition function on a fixed physical torus, uniform in the lattice spacing, by block renormalisation group with small- and large-field regions | THM | T. Balaban, CMP 95 (1984) 17; 96 (1984) 223; 98 (1985) 17; 99 (1985) 75, 389; 102 (1985) 277; 109 (1987) 249; 116 (1988) 1; 119 (1988) 243; 122 (1989) 175, 355 | recalled; PDFs and text at `~/ym4d-papers/` not read in this run; Balaban does not construct the continuum limit of correlations, infinite volume or a gap |
| I13 | Continuum construction of YM_4 in finite volume with an infrared cutoff, in a gauge-fixed continuum regularisation | THM | J. Magnen, V. Rivasseau, R. Seneor, CMP 155 (1993) 325 | recalled |
| I14 | Abelian compact U(1) lattice gauge theory in d = 4 has, at weak coupling, a Coulomb phase with a massless photon: no mass gap | THM | A. Guth, PRD 21 (1980) 2291; J. Frohlich, T. Spencer, CMP 83 (1982) 411 | recalled |
| I15 | Compact U(1) in d = 3 has a mass gap at all couplings (monopole plasma, Debye screening; Polyakov's mechanism) | THM | M. Gopfert, G. Mack, CMP 82 (1982) 545 | recalled |
| I16 | Finite gauge groups (Z_2, and finite non-abelian groups) in d = 4 at weak coupling: exponential decay of correlations (a gap) together with a perimeter law (no confinement) | THM | S. Chatterjee, CMP 377 (2020) (Z_2); S. Cao, CMP 380 (2020); A. Adhikari, S. Cao, "Correlation decay for finite lattice gauge theories at weak coupling" (Ann. Probab. 2025?) | recalled; exact journal details not re-checked |
| I17 | Elitzur: local gauge symmetry is not spontaneously broken; gauge-non-invariant expectations vanish | THM | S. Elitzur, PRD 12 (1975) 3978 | recalled |
| I18 | Two-dimensional Yang-Mills is exactly solvable (area law; on a cylinder the Hamiltonian is the Laplacian on the group, discrete spectrum with gap); no propagating local degrees of freedom | THM | Migdal 1975; Gross-King-Sengupta, Ann. Phys. 194 (1989); Driver CMP 123 (1989); Sengupta; Levy | recalled |
| I19 | 2D O(2) (XY) model: no mass gap at low temperature (Kosterlitz-Thouless phase, power-law decay) | THM | J. Frohlich, T. Spencer, CMP 81 (1981) 527 | recalled |
| I20 | Large-N Gross-Neveu in 2D: rigorous dynamical mass generation (an asymptotically free theory with a gap not put in by hand), with 1/N as the small parameter | THM | C. Kopper, J. Magnen, V. Rivasseau, CMP 169 (1995) 121 | recalled |
| I21 | Asymptotically free 2D Gross-Neveu (massive or with infrared cutoff) constructed by convergent RG | THM | K. Gawedzki, A. Kupiainen, CMP 102 (1985) 1; J. Feldman, J. Magnen, V. Rivasseau, R. Seneor, CMP 103 (1986) 67 | recalled |
| I22 | Lattice topological charge is well defined on admissible fields (all plaquettes close to 1); admissibility is a hard constraint | THM | M. Luscher, CMP 85 (1982) 39 | recalled |
| I23 | No continuous global gauge fixing exists for non-abelian bundles over S^4 (Gribov ambiguity) | THM | I. Singer, CMP 60 (1978) 7; V. Gribov, NPB 139 (1978) 1 | recalled |
| I24 | Finite-volume, finite-lattice Hamiltonian (Kogut-Susskind) or transfer matrix: discrete spectrum, unique ground state (Perron-Frobenius on a compact configuration space), positive gap in lattice units | THM | Kogut-Susskind PRD 11 (1975) 395; Perron-Frobenius for positivity-improving semigroups (Reed-Simon IV, XIII.12) | recalled; elementary |
| I25 | Mack-Petkova: SU(2) confinement reduces to the behaviour of Z_2 (centre) vortex free energies; comparison inequalities between SU(2) and Z_2 lattice gauge theory | THM | G. Mack, V. Petkova, Ann. Phys. 123 (1979) 442; 125 (1980) 117 | recalled |
| I26 | 't Hooft flux: on a periodic box, electric and magnetic flux free energies classify phases; exact lattice relations between centre-vortex free energy and Wilson loops | THM | G. 't Hooft, NPB 153 (1979) 141; T. Kovacs, E. Tomboulis, PRL 85 (2000) 704 | recalled |
| I27 | Migdal-Kadanoff / hierarchical approximations: SU(2) in d = 4 flows to strong coupling (confinement) at every beta in the approximate recursion | THM (in the approximation) | A. Migdal, JETP 42 (1975) 743; K. R. Ito, PRL 55 (1985) 558 | recalled |
| I28 | A claimed proof of confinement at all beta via a Migdal-Kadanoff interpolation was critiqued and is not accepted | THM status: disputed | E. Tomboulis, arXiv:0707.2179; K. R. Ito, E. Seiler, arXiv:0711.4930 | recalled |
| I29 | Higgs-confinement complementarity: with a fundamental Higgs field, Higgs and confinement regions are analytically connected | THM | Osterwalder-Seiler 1978; Fradkin-Shenker PRD 19 (1979) 3682 | recalled |
| I30 | Perturbative asymptotic freedom (one-loop beta function) | THM in formal power series | Gross-Wilczek, Politzer 1973 | recalled |
| I31 | Small spatial volume: SU(2) on T^3 x R with small side L has a gap computable from an effective Hamiltonian on constant abelian modes | THM (perturbative, with rigorous parts) | M. Luscher, NPB 219 (1983) 233; P. van Baal, J. Koller | recalled |
| I32 | Infinite-volume lattice Gibbs states exist for every beta (compactness of SU(2)), not known unique at large beta | THM | DLR compactness (Georgii, *Gibbs Measures*, ch. 4) | recalled; elementary |
| I33 | Stochastic quantisation of 2D and 3D Yang-Mills: local-in-time Langevin dynamics on a gauge-invariant state space; invariant measure in 3D not constructed | THM | A. Chandra, I. Chevyrev, M. Hairer, H. Shen, Publ. IHES (2024) and arXiv:2201.03487 | recalled |
| I34 | Existence (no gap) of 4D SU(2) YM: announced by OpenAI 2026-10-26 (write-up not public); and the Sussman-Alpoge complete account (CA-I to CA-III) | SUPPLIED knowledge (from GOAL.md, disclosed) | GOAL.md | not read in this run; standing unknown |

**Nearest models (inventory rows for step-6 tests)**

| # | Model | Gap? | Interacting? | Why | Mark |
|---|---|---|---|---|---|
| N1 | Free massless vector field (the beta -> infinity limit at fixed lattice spacing) | no | no | Gaussian | THM (elementary) |
| N2 | Free massive field | yes | no | mass put in | THM |
| N3 | Compact U(1), d = 4, weak coupling | no | yes on the lattice; continuum free photon | I14 | THM |
| N4 | Compact U(1), d = 3 | yes | yes | I15 | THM |
| N5 | Finite group (Z_2, Q_8, binary tetrahedral) in d = 4, weak coupling | yes | lattice yes; no continuum AF limit | I16 | THM |
| N6 | 2D Yang-Mills | yes (cylinder) | no local dof | I18 | THM |
| N7 | 2D XY | no (low T) | yes | I19 | THM |
| N8 | 2D O(N >= 3) sigma model | believed yes | AF | Polyakov; Bethe ansatz (Polyakov-Wiegmann 1983; Hasenfratz-Maggiore-Niedermayer 1990 exact mass gap) | BELIEF (open as a theorem; the lattice model's gap at large beta is unproved, and was challenged by Patrascioiu-Seiler) |
| N9 | 2D Gross-Neveu, large N | yes | AF | I20 | THM |
| N10 | SU(2) lattice in d = 5, weak coupling | believed no (Coulomb-like phase after a bulk transition) | yes | Creutz, PRL 43 (1979) 553, Monte Carlo | BELIEF (numerics) |
| N11 | SU(2) with theta = pi | believed no unique gapped vacuum ('t Hooft anomaly between centre 1-form symmetry and time reversal) | yes | D. Gaiotto, A. Kapustin, Z. Komargodski, N. Seiberg, JHEP 05 (2017) 091 | BELIEF (physics-level theorem, not rigorous) |
| N12 | SU(2) with fundamental Higgs | yes | yes | I29 (complementarity), perturbative Higgs mass | THM in parts (the gap at weak coupling is not rigorously proved in d = 4 either, to my recollection; mark recalled) |
| N13 | Migdal-Kadanoff SU(2), d = 4 | confines at every beta | approximate | I27 | THM in the approximation |
| N14 | Lattice SU(2), d = 4, strong coupling | yes (lattice units) | yes | I9, I10 | THM |

**Beliefs (used in no proof)**

| # | Item | Mark | Source |
|---|---|---|---|
| B1 | 4D SU(2) YM has a gap; lightest glueball 0++ with m/sqrt(sigma) about 3.7 to 4.7 | BELIEF (numerics) | M. Teper, hep-th/9812187; Lucini-Teper-Wenger 2004 |
| B2 | No bulk phase transition along the Wilson axis for SU(2) in d = 4 (a crossover near beta about 2.2) | BELIEF (numerics) | M. Creutz, PRD 21 (1980) 2308 |
| B3 | For mixed fundamental-adjoint actions a first-order bulk line exists, ending near the Wilson axis (so "no transition" depends on the action) | BELIEF (numerics) | Bhanot-Creutz PRD 24 (1981) 3212 |
| B4 | Confinement (area law) and gap hold together in SU(2); but gap does not need confinement (N5, N12) | BELIEF for the first part; THM-backed for the second | I16, I29 |
| B5 | Mechanisms: centre vortices ('t Hooft, Mack, Greensite), dual superconductor (Mandelstam, 't Hooft), Gribov-Zwanziger | BELIEF | Greensite, *An Introduction to the Confinement Problem* (2011) |
| B6 | theta = 0 vacuum is unique (no spontaneous CP breaking) | BELIEF | Vafa-Witten PRL 53 (1984) 535 (argument for theta = 0 parity) |
| B7 | Deconfinement at finite temperature, second order, Ising class | BELIEF (numerics) + THM for high-T deconfinement on the lattice (Borgs-Seiler CMP 91 (1983)) | recalled |
| B8 | The physical scale Lambda equals a constant times a^{-1} exp(-1/(2 b_0 g_0^2)) times a power; the gap in lattice units is non-perturbatively small at weak coupling | BELIEF (perturbation theory) | I30 |

Skill step 2 is complete. Next: plan step 3 (skill step 3, reason up; Elon pass).

### Plan step 3 = skill step 3: reason up from the inventory; the Elon pass

Reasoning uses only the inventory of step 2 (and facts A0, A1). No lane file opened.

#### 3.1 What follows at once

**A2 (argued).** Let the OS data be given (RP and time-translation invariance only; no O(4), no growth bound used). Let S be a set of positive-time observables F whose vectors [F] are total in H_phys. If there is Delta > 0 and, for each F in S, a constant C_F with
  |(F, T_t F)_OS - |<F>|^2| <= C_F e^{-Delta t} for all t >= 0,
then spec(H) restricted to Omega-perp lies in [Delta, inf), and Omega is the unique invariant vector.
Proof. Write psi_F = [F] - <F> Omega, which lies in Omega-perp. The left side equals <psi_F, e^{-tH} psi_F> = int e^{-t lambda} d mu_F(lambda) with mu_F the (positive) spectral measure of psi_F. For eps > 0, mu_F([0, Delta - eps]) e^{-t(Delta - eps)} <= C_F e^{-Delta t}, so mu_F([0, Delta - eps]) <= C_F e^{-eps t} -> 0. Hence the spectral projection E([0, Delta)) kills every psi_F; the psi_F together with Omega are total, and E([0,Delta)) Omega... is Omega itself (H Omega = 0), so E([0, Delta)) is the projection onto C Omega, which is the claim, uniqueness included. QED. Inputs: spectral theorem; OS reconstruction for the identification (I7). Mark: argued.
Consequences: (i) constants may depend on F; only the rate must be uniform; (ii) S must be total, so it must contain products of fields at several positive times (multi-point clustering between a reflected group and a translated group), not only two-point functions of single fields; (iii) the bound passes to limits: if lattice or finite-volume theories satisfy it with a rate Delta and constants C_F uniform in the cutoffs, and the Schwinger functions of the F converge along a subsequence, the limit satisfies it (pointwise limits of the left side). Mark of (iii): argued.

**C1 (I24, A1, A2).** At fixed lattice spacing and finite volume the gap is automatic. All the content of the target's gap clause is uniformity: a rate in physical units that survives a -> 0 and L -> infinity. Argued.

**C2 (A2).** The gap clause needs only reflection positivity, time translations and a uniform clustering rate for a total set. O(4), the growth bound and non-triviality are separate clauses; a gap proof need not touch them, except that non-triviality must hold for the same limit theory (the trivial theory has a vacuous gap). Argued.

**C3 (N3 = I14).** Compact U(1) in d = 4 is reflection positive, compact, local, four-dimensional, lattice-regularised, and has no gap at weak coupling (THM). So any proof must use a property U(1) lacks. Candidates visible in the inventory: non-abelian Lie bracket (b_0 > 0, I30); strictly positive Ricci curvature of the group manifold SU(2) = S^3 (used by I10; U(1) is flat); the non-trivial pi_3(SU(2)) (instantons; Luscher's charge I22); the finite centre Z_2 (I25, I26). Argued (the list is of candidates, not shown sufficient).

**C4 (N1, I30, B8).** Around the free field, every order of weak-coupling perturbation theory is gapless (massless gluons). So the gap is invisible at any fixed order in the small coupling; it must come from a scale where the effective coupling is not small, or from a small parameter that is not the coupling (a deformation, 1/N, a compact direction). Argued for the first sentence (elementary: the free propagator has no gap); the conclusion is a reading.

**C5 (I9, I10, I12).** Rigorous control exists at small effective coupling (Balaban's RG, I12, for beta above some large beta_1) and at large effective coupling (cluster expansion and Bakry-Emery, I9 and I10, for beta below some beta_0 of order 1/d). These are explicit constants with beta_0 far below beta_1. No rigorous tool in the inventory covers the band between them. Reading (the size of the band is recalled, not computed).

**C6 (N5, N12, I16, I29).** A gap does not require confinement: finite gauge groups at weak coupling and Higgs models are gapped with a perimeter law. So a gap proof need not prove an area law. The two known non-confining gapped mechanisms each have a small parameter at weak coupling (discreteness of the group; the Higgs mass); SU(2) pure has neither. Argued for the first two sentences (THM inputs); reading for the last.

**C7 (N11, B6).** At theta = pi the physics anomaly argument forbids a unique gapped vacuum. A uniqueness proof therefore must use theta = 0 through something theta = pi lacks; the cleanest such property is positivity of the Euclidean measure (theta = pi has a sign problem). Belief-level (N11 is BELIEF), as a test it constrains but refutes nothing.

**C8 (N8).** 2D O(N >= 3) is the nearest model where the wall bites in full: asymptotically free, compact target, reflection positive, believed gapped, and the gap is unproved after forty years. A method that uses none of: gauge invariance, d = 4, the centre, pi_3, would apply to it with small changes and would settle Polyakov's conjecture. Not a refutation (the O(3) gap is a belief, challenged by Patrascioiu-Seiler); a calibration of cost. Reading.

**C9 (A2(iii), I7, I32).** The gap clause, in the form of A2, is proved at cutoff level and passed to the limit; it does not need the limit theory first. Uniform clustering is also what gives a unique infinite-volume limit and OS4 at once. Existence by compactness (I32) without clustering, followed by a gap proof, must redo the infinite-volume control in the second stage. So "existence first, gap after" is an ordering of convenience, and it duplicates the infinite-volume work. Argued for the logic; the cost claim is a reading.

**C10 (finite-size criteria; recalled THM).** For finite-range lattice spin systems, a mixing condition in one finite box, uniform in boundary conditions, implies exponential decay in infinite volume (R. Dobrushin, S. Shlosman, "Completely analytical interactions", J. Stat. Phys. 46 (1987) 983; F. Martinelli, E. Olivieri, CMP 161 (1994) 447; D. Stroock, B. Zegarlinski, CMP 149 (1992) 175). Analogues hold for gaps of frustration-free quantum Hamiltonians (S. Knabe, J. Stat. Phys. 52 (1988) 627; D. Gosset, E. Mozgunov, J. Math. Phys. 57 (2016); M. Lemm, E. Mozgunov, J. Math. Phys. 60 (2019); M. Kastoryano, A. Lucia, J. Stat. Mech. (2018) 033105). Reading: by C5, a gap proof can be organised as a finite-box statement for an effective theory at the one scale where the coupling is of order one, transported by such a criterion. Whether a criterion of this kind holds for lattice gauge theories (with gauge-invariant boundary data) is not in the inventory: open.

**C11 (I15, I29, I31; Unsal-Yaffe recalled).** Deformations with a small parameter at all scales are available: a fundamental Higgs (I29; Balaban, Brydges, Imbrie, Jaffe, "The mass gap for Higgs models on a unit lattice", Ann. Phys. 158 (1984) 281, abelian, recalled); small spatial volume (I31); centre-stabilised YM on R^3 x S^1 of small radius, which abelianises and reduces at long distance to a 3D compact abelian theory with monopole-instantons, the Polyakov mechanism (M. Unsal, L. Yaffe, PRD 78 (2008) 065035, recalled; cf. I15 for the lattice abelian 3D gap). Each gives a gapped interacting theory with a small parameter throughout, but the target needs continuity back to the undeformed theory on R^4 (Higgs coupling -> 0, radius -> infinity, deformation -> 0), and that continuity is a statement with no small parameter. Reading; the small-parameter gaps themselves are not proved for the non-abelian 4D cases by any inventory item (open).

#### 3.2 The least a solution must contain

1. A limit theory for which the gap is asserted, and the identification of that theory as Yang-Mills (non-triviality) in the same limit (C2).
2. A uniform rate in the sense of A2 for a total set (C1, A2).
3. Use of a property that compact U(1) in d = 4 lacks (C3), and that the free field lacks at any fixed perturbative order (C4).
4. Either an estimate at a scale of order-one coupling, or a mechanism that transports a gap across that scale without an estimate there (monotonicity, comparison, a soft argument by contradiction, or continuity of a deformation) (C5, C11).
5. Uniqueness of the vacuum from something theta = pi lacks (C7), e.g. positivity of the measure; A2 gives uniqueness for free once the rate holds.

#### 3.3 The smallest object

- The single number m(beta) = -lim_t (1/t) log of the second transfer-matrix eigenvalue ratio, in infinite volume, at coupling beta; the target is m(beta) >= c * Lambda * a(beta) along the trajectory on which the continuum limit is taken, i.e. the ratio of two non-perturbative scales bounded below. Argued as a reformulation given A2 and a continuum limit; constants unspecified.
- Finite-volume version: the continuum gap Delta(L) on a spatial torus of side L. Small L: Delta(L) is computable in perturbation theory (I31). The target needs inf over L >= L_0 of Delta(L) > 0. This is a scale-transport statement from a calculable small-volume regime to infinite volume. Reading.
- Toy where the wall bites: the 2D O(3) model (C8). It takes no hour to build; it is a known open problem, so the wall is confirmed to bite there in the sense that no proof exists (not in the sense of a proof that one cannot exist).

#### 3.4 Where the result can come from

One problem in three scale bands: UV (small coupling: RG, existence, non-triviality), crossover (coupling of order one: no small parameter), IR (large effective coupling in block units: cluster expansion, Bakry-Emery). The gap lives in the crossover and IR bands; the identification with Yang-Mills lives in the UV band. Mechanisms visible from the inventory: (M1) strong-coupling seed in block units plus RG bridge; (M2) centre vortex disorder via Mack-Petkova comparison (I25) and 't Hooft flux (I26); (M3) curvature (Bakry-Emery on the group, I10; formally, positive curvature of the orbit space of connections, I. Singer, Phys. Scripta T24 (1981) 817, recalled, heuristic); (M4) finite-size criteria (C10); (M5) deformation continuity (C11); (M6) a soft dichotomy: if there is no gap, the infrared limit is a scale-invariant theory, then exclude each candidate (free gluons are excluded by b_0 > 0 at the heuristic level; an interacting IR fixed point is not excluded by anything in the inventory). Failure modes: a bulk transition at intermediate coupling for the chosen action (B2, B3: depends on the action); a Coulomb-like phase (N3, N10); vacuum degeneracy (N11).

#### 3.5 Make the requirement less wrong: the Elon pass

For each requirement of T and of any chain to it: who requires it; can it be deleted; what is left.

| Requirement | Who requires it | Delete? | Simplified form |
|---|---|---|---|
| E1 Every compact simple G | JW | Deleted by the owner for this row (SU(2)) | SU(2) |
| E2 R^4, infinite volume | JW; and C1 (finite-volume gap is empty) | No | Uniform in L, or infinite volume directly |
| E3 Wightman axioms in full | JW ("at least as strong as") | Not for T; yes for the gap clause (C2) | Gap clause needs RP + time translations only |
| E4 O(4) covariance | JW via Lorentz; A0 needs it to turn H-gap into a mass-hyperboloid gap | Not for T; yes for the gap clause | Prove gap in A2 form; add O(4) once, in the existence chain |
| E5 Local fields for every gauge-invariant polynomial in F | JW | Not for T; but the gap only needs a total set (A2) | Use a total set of bounded smoothed observables (e.g. gradient-flowed observables at positive flow time, M. Luscher JHEP 08 (2010) 071, recalled) and show local fields act in the same H_phys |
| E6 Non-triviality as AF agreement | JW | No (trivial theory has vacuous gap) | Needed for the same limit, not inside the gap proof |
| E7 Unique vacuum | JW gap clause on Omega-perp | No; it is free once A2 holds | Absorbed into A2 |
| E8 Lattice regularisation | No one (method) | Yes in principle | Any regularisation with RP at cutoff level |
| E9 Wilson action | No one (method) | Yes | Any RP action with the right continuum limit (heat-kernel, admissibility-constrained, mixed); choose the one that makes the crossover provable |
| E10 Euclidean formulation | No one (method; OS route) | Yes | Hamiltonian lattice or continuum-time also allowed |
| E11 Existence proved before gap | No one (ordering habit) | Yes (C9) | Prove uniform clustering at cutoff level along with existence |
| E12 Block RG frame (Balaban; Sussman-Alpoge) | Needed in the UV band only (C5) | Not in UV; yes for crossover/IR | RG to the crossover scale; any tool after it |
| E13 Gap reduced to a seed plus transport | No one (method) | Yes | One option among M1-M6 |
| E14 Correlation decay as the route to gap | A1/A2 make it equivalent | No as a statement; yes as a route (spectral or Hamiltonian lower bounds are the same statement) | A2 |
| E15 Area law / confinement | No one (C6) | Yes | Not needed |
| E16 SU(2) before SU(N) | Owner order | On paper only | - |
| E17 No computer-assisted step | Owner (GOAL.md) | Not questioned in the run (group f) | Finite-box estimates must be explicit by hand |

**What is left after deletion.** (D) For SU(2) on R^4: a reflection-positive family of cutoff theories (any regularisation), with a UV limit identified with asymptotically free Yang-Mills, such that a total set of bounded positive-time observables has truncated reflection pairings decaying at one rate Delta > 0 in physical units, uniformly in the cutoffs. Plus, in the existence chain, O(4) and the growth bound. Argued (as a sufficient reformulation, given I7 and A2).

#### 3.6 Price (from first principles)

The exact missing input, as far as the inventory shows: a non-perturbative estimate on an effective theory at the one scale where the running coupling is of order one, of the strength "correlation length at most a fixed multiple of that scale", or a mechanism that carries a gap across that scale without such an estimate (C5, C10, C11). Mark: reading (no equivalence proved here).

#### Conclusions of step 3

C1 uniformity is all (I24, A1, A2). C2 gap clause needs only RP + time translations + uniform rate on a total set (A2). C3 must use what compact U(1) lacks (I14). C4 invisible at fixed perturbative order (N1, I30). C5 no rigorous tool spans the crossover band (I9, I10, I12; reading). C6 no confinement needed (I16, I29). C7 uniqueness must use theta = 0 (N11; belief-level). C8 2D O(3) calibrates cost (N8; reading). C9 existence-then-gap duplicates infinite-volume work (A2, I32; reading for cost). C10 finite-size criteria could localise the crossover estimate to one box (recalled THM for spin systems; open for gauge). C11 deformations move the wall to a continuity statement (reading).

### Plan step 4 = skill step 4: the assumptions table

Written before any lane file was opened, so "where used" cites the row (FINISH.md:1133, 1134), GOAL.md, or the field's literature; step 5 adds lane path:lines. Columns: ID | assumption | where used | needed by target / method / habit | if wrong or dropped | easier? | check.

#### (a) Target

| ID | Assumption | Where used | Needed? | If wrong or dropped | Easier? | Check |
|---|---|---|---|---|---|---|
| a1 | The group is SU(2), not every compact simple G | FINISH.md:1133; GOAL.md:22 | owner choice | SU(N): same structure, 1/N gives no rigorous handle at finite N; SO(3) = SU(2)/Z_2 adds Z_2 monopoles and (belief) a bulk transition for its natural action; nothing opens rigorously | no | none known |
| a2 | The space is R^4 (infinite volume, no compact direction) | JW; FINISH.md:1133 | target | Replacing R^4 by R^3 x S^1 of small radius with centre stabilisation (C11) gives a problem with a small parameter at every scale (abelianisation, Polyakov mechanism); a fixed spatial torus T^3_L gives a trivially positive gap (I24). The target then needs continuity L -> infinity: no small parameter there | yes for the deformed target, no for T | none known in the inventory |
| a3 | "Gap" means spec H on all of Omega-perp, the space generated by every local gauge-invariant field | JW (T.4) | target | A gap on the cyclic subspace of one chosen field family (e.g. the tr F^2 sector) is weaker unless that family is total (A2) | yes (weaker) | A2: totality of the family is the exact missing step |
| a4 | Non-triviality means agreement with asymptotically free perturbation theory at short distance | JW | target | If non-triviality is a weaker property (non-Gaussian only) a trivial or wrong limit could pass; if stronger (full OPE), existence gets harder; the gap is unaffected (C2) | no for gap | C2 |
| a5 | Existence includes O(4), growth, locality at Wightman strength | JW | target | Not needed by the gap clause (C2, E3, E4); needed by T | gap lane: yes | A2 |
| a6 | The vacuum is unique (theta = 0) | JW gap clause | target | Degenerate vacua (as believed at theta = pi, N11) make the clause fail although each pure phase may be gapped | no | A2 gives uniqueness from the rate |
| a7 | One Delta covers the whole H_phys | JW | target | On R^4 there are no flux sectors in the vacuum representation; on a torus, 't Hooft flux sectors would need separate bounds (I26) | no | none needed |
| a8 | The gap is the next consumer-relevant target | FINISH.md:1133; GOAL.md (T0 excludes the gap; "Later targets: ... the mass gap") | owner | If T0 (existence) is the owner's real priority, gap work is off the critical path; C9 says the clustering work overlaps T0's missing clustering clause anyway | - | owner decision |

#### (b) Formulation

| ID | Assumption | Where used | Needed? | If wrong or dropped | Easier? | Check |
|---|---|---|---|---|---|---|
| b1 | The theory is built as a continuum limit of a lattice theory at all | FINISH.md:1133 (listed); field habit since Wilson 1974 | method | Other constructions: gauge-fixed continuum regularisation (I13, Magnen-Rivasseau-Seneor), stochastic quantisation (I33), loop (Makeenko-Migdal / Schwinger-Dyson) equations (S. Chatterjee, CMP 366 (2019) 203, recalled), Hamiltonian; lose compactness and RP at cutoff level, gain other structure (loop equations characterise the measure; SPDE gives Bakry-Emery-type tools) | unknown | none run |
| b2 | The lattice action is Wilson's | FINISH.md:1133; GOAL.md:22 ("Wilson SU(2)") | method | Any RP action with the same continuum limit is allowed: heat-kernel (Villain-type) action (exact Migdal recursion in 2D, positive characters), Luscher's admissibility-constrained action (hard constraint, no large fields, topological charge defined), mixed fundamental-adjoint, improved actions. The choice can remove bulk transitions (B3 shows they depend on the action) and decide whether a crossover estimate is provable | possibly | none known |
| b3 | Euclidean, not Minkowski or Hamiltonian | FINISH.md:1133; GOAL.md (OS route) | method | Hamiltonian lattice (Kogut-Susskind) gives a Schrodinger operator on L^2(SU(2)^links)^gauge: spectral tools, operator inequalities, quantum finite-size criteria (C10), at the cost of an extra continuum limit in time; A1 makes the two gap statements equivalent | maybe | none run |
| b4 | Gauge-invariant (no gauge fixing) | field habit for lattice | method | Gauge fixing meets the Gribov ambiguity (I23) globally; gains perturbative tools locally; axial gauge on the lattice is complete and exact (it is how I10 runs) | no globally | I23 |
| b5 | Link variables are compact group elements | lattice habit | method | Non-compact potentials lose finite-volume existence for free and RP proofs; gain linear structure | no | - |
| b6 | Finite volumes are periodic tori, then L -> infinity | field habit | method | Twisted ('t Hooft) boundary conditions give flux free energies as order parameters (I26); free or Dirichlet conditions give monotonicity in some abelian cases | maybe | none run |
| b7 | theta = 0 | JW (implicit), Wilson measure | target | theta != 0 gives a complex measure; theta = pi believed degenerate (N11) | no | - |
| b8 | Observables are local composite fields and Wilson loops | JW; GOAL.md:22 (tr F^2 sector) | target for the field list; method for the gap | The gap needs only a total set (A2); smoothed (gradient-flowed) bounded observables avoid composite-operator renormalisation inside the gap proof (E5) | yes for the gap | A2 |
| b9 | Four dimensions as given | JW | target | d = 3 is super-renormalisable (existence easier) and its gap equally non-perturbative; not the target | no | - |
| b10 | Hypercubic, isotropic lattice spacing | habit | method | Anisotropic a_t << a_s (Hamiltonian limit) makes the transfer matrix e^{-a_t H} close to 1 - a_t H, simplifying spectral statements | slightly | - |
| b11 | Pure gauge, no matter | target | target | Heavy or Higgs matter (C11) gives a small-parameter gap; the target needs decoupling continuity | yes for deformed target | - |
| b12 | The relevant degrees of freedom are SU(2) fields; centre Z_2 and pi_3 enter only through them | habit | method | Writing SU(2) = Z_2 x (SO(3) data) explicitly (Mack-Petkova, I25) exposes vortex variables; writing pi_3 sectors (I22) exposes instantons | maybe | none run |
| b13 | The coupling trajectory is beta(a) set by the one-loop running | GOAL.md:27 (T1 "along a coupling trajectory the proof chooses") | method | The proof may choose any trajectory with the right limit; additional irrelevant couplings are free parameters | maybe | - |

#### (c) Reduction

| ID | Assumption | Where used | Needed? | If wrong or dropped | Easier? | Check |
|---|---|---|---|---|---|---|
| c1 | Existence first (T0), gap after | GOAL.md:22 ("no mass gap claimed"), GOAL.md critical path; FINISH.md:1133 (listed) | habit / owner order | C9: uniform clustering at cutoff level gives the gap, the unique infinite-volume limit and OS4 together; existence by compactness then gap duplicates the infinite-volume work | yes (less duplication) | C9 (argued logic) |
| c2 | Balaban / Sussman-Alpoge block RG is the frame at all scales | GOAL.md:39-48; FINISH.md:1133 (listed) | needed in the UV band; method elsewhere | After the crossover scale any tool may take over (cluster expansion, Bakry-Emery, finite-size criteria); a frame built for small coupling need not carry the IR | maybe | C5 |
| c3 | The gap reduces to a finite-scale seed plus a scale-transport statement | FINISH.md:1133 ("the seed"); field (C10) | method | Alternatives: a soft dichotomy (no gap => scale-invariant IR, then exclude it, M6), deformation continuity (C11), a monotone quantity along scales, comparison inequalities (Mack-Petkova, I25). If the seed/transport form is wrong, the work goes to one of these | unknown | none run |
| c4 | Order-one coupling is the hard regime | FINISH.md:1133 (listed) | belief / method | The hard part might be elsewhere: large-field configurations at weak coupling (instantons, I22), the non-locality of effective actions at strong effective coupling, or the infinite-volume limit; a route aimed at the crossover then misses | unknown | none |
| c5 | Transfer-matrix / spectral methods for the gap | FINISH.md:1133 (listed) | equivalent to decay (A1, A2) | Not wrong as a statement; as a route, spectral lower bounds and decay are the same statement, so the choice is only of tools | no | A1 |
| c6 | Correlation decay is the route to the gap | FINISH.md:1133 (listed) | equivalent (A2) | Decay of two-point functions of single fields is not enough (A2 ii): multi-time products are needed for totality | - | A2 |
| c7 | The effective action at each scale stays local and close to a Wilson-type form (polymer expansion) | Balaban I12 (recalled) | method | At the crossover the effective action may be far from any finite-range form; a seed that assumes a near-Wilson form at strong effective coupling fails | no | none |
| c8 | Small-field / large-field split | Balaban I12; GOAL.md:60 (hard-constraint RG) | method | Under a hard (admissibility) constraint there is no large-field region at the bare scale; whether blocked fields stay admissible is a separate question | maybe | none |
| c9 | One tool proves the whole gap | habit | habit | Tools combine by scale band (C5) | yes | - |
| c10 | Clustering (OS4) is handled apart from the gap | GOAL.md:22, 39-48 (SA Theorem 0 lacks clustering) | habit | The gap gives clustering (A2); the two are one statement in the gap lane | yes | A2 |
| c11 | A seed at one fixed coupling of order one must be proved by hand | GOAL.md:10-18 | owner rule | If the seed is parametric (a scale chosen large, an explicit small quantity), "by hand" is possible; if it is a genuine finite computation at coupling of order one, it is forbidden as a computer step and hard by hand | - | none |
| c12 | The gap is passed from cutoff theories to the limit | field habit | method | A2 (iii) makes this automatic when constants are uniform | no | A2 |

#### (d) Discard tests (field-wide; the lane's own tests are known before step 5 only by their names in FINISH.md:1134)

| ID | Test | Where used | Valid form? (pre-audit) | If the test is wrong: what comes back | Check |
|---|---|---|---|---|---|
| d1 | "It also holds for compact U(1) in d = 4" (N3) | FINISH.md:1134 (named) | THM-backed (I14); valid refutation for any tool whose class contains U(1) | - | I14 |
| d2 | "It also holds for a frozen finite subgroup (Q_8, 2T)" | FINISH.md:1134 (named) | Finite groups at weak coupling are gapped (I16, THM). So this test cannot refute a gap tool (T is true there); it can refute a confinement tool (perimeter law) or an identification of the continuum limit | Any gap tool discarded by this test comes back | step 6 |
| d3 | "It also holds in five dimensions" | FINISH.md:1134 (named) | Rests on a belief (N10, Monte Carlo) unless a theorem of a gapless 5D phase exists; as a belief it constrains, refutes nothing | Tools discarded by it come back as candidates | step 6 |
| d4 | "It needs a small number" | field habit | valid only as a range | Tools come back in the range where their small number holds | step 6 |
| d5 | "It also holds at theta = pi" | field (N11) | belief-level | - | - |
| d6 | "It also holds for the free field" (N1) | field | THM (elementary); valid for gap tools | - | - |
| d7 | "It renames an open statement" (GS-eq example) | FINISH.md:1134 | valid as a strength test (target-equivalent) | - | proof-search governance |
| d8 | "It also holds for 2D O(3)" | field | calibration only (N8 is belief) | Tools discarded by it come back | - |
| d9 | "It also holds for the Migdal-Kadanoff model" | field | the MK model confines at all beta (I27); T true there; cannot refute | Tools discarded by it come back | - |

#### (e) Beliefs

| ID | Belief | Where used | If wrong | Check |
|---|---|---|---|---|
| e1 | SU(2) YM on R^4 has a gap (B1) | the whole target | the target is false; a gapless proof would be the result; existence survives | none possible by numerics alone |
| e2 | Confinement / area law holds | field | no effect on the gap (C6) | - |
| e3 | No bulk transition on the Wilson axis (B2) | field; b2 | the continuum limit along the Wilson axis may pass through a transition; change the action | B3 (action-dependence, numerics) |
| e4 | Asymptotic freedom holds non-perturbatively, and the beta -> infinity point is the AF continuum theory | field | Patrascioiu-Seiler dissent (A. Patrascioiu, E. Seiler, e.g. "Is the 2D O(3) nonlinear sigma model asymptotically free?" and their 4D remarks, recalled): a different continuum limit or a soft phase | none |
| e5 | Gap in lattice units scales like Lambda a(beta) (B8) | field | gap closes faster: no continuum gap | - |
| e6 | Centre vortices or dual superconductivity are the mechanism (B5) | field | routes built on them die; the target is unaffected | - |
| e7 | The Gribov problem is an obstruction | field | Gribov-Zwanziger suggests the restriction to the Gribov region generates a mass scale (belief); a gauge-fixed route may help, not hurt | - |
| e8 | Instantons are irrelevant to the 4D gap (dilute gas is IR divergent) | field (Callan-Dashen-Gross, recalled) | instanton or meron mechanisms come back | - |
| e9 | Once the effective coupling is large, the IR is easy (strong-coupling expansion) | field; c4 | the IR seed itself is hard (non-local effective actions) | none |
| e10 | Strong-coupling expansions (I9, I10) are the only rigorous source of non-abelian gaps | inventory | other sources: deformations (C11), finite-size criteria (C10) | - |
| e11 | Large N is not easier rigorously | field | Chatterjee and Basu-Ganguly control large N only at strong coupling (recalled) | - |
| e12 | The gap is independent of irrelevant terms in the action (universality) | field | the gap would depend on the scheme; the proof must fix the action | - |

#### (f) Working rules (questioned on paper only; all obeyed in this run)

| ID | Rule | Where | If a different rule were used (not used) |
|---|---|---|---|
| f1 | No computer-assisted steps; Lean-formalizable written proofs | GOAL.md:10-18 | A finite-box seed at coupling of order one could be verified by rigorous interval arithmetic; the crossover becomes a computation. Not used; owner decision |
| f2 | Port the Sussman-Alpoge account; proof work only on their open statements | GOAL.md:39-48 | Own existence routes. Not used |
| f3 | SU(2) first | GOAL.md:22 | - |
| f4 | T0 (existence without gap) is the target; gap later | GOAL.md:22 and critical path | Gap work merged with clustering (C9). Owner decision |
| f5 | No subagents; one item per fresh session | dispatch; FINISH.md:329 | - |
| f6 | Hardest first | FINISH.md:322 | - |
| f7 | Literature rebuilt in library/, credited | FINISH.md:64 | - |
| f8 | Numeric runs refute or guide only, under the lock | FINISH.md:343 | - |

Count: 8 + 13 + 12 + 9 + 12 + 8 = 62 assumptions.

#### Ranking (by how much the problem changes when the assumption is dropped)

1. **e1** gap true. Dropped: the target is false. (Problem changes completely; least likely to be wrong.)
2. **f1** no computer steps (on paper only). Dropped: a seed at order-one coupling becomes a finite verified computation. *Owner decision.*
3. **a2** R^4 rather than a small compact direction with deformation. Dropped: a small-parameter problem at every scale, leaving one continuity statement. *Changes the target; owner decision.*
4. **c3** seed plus scale transport. Dropped: soft dichotomy, deformation continuity, comparison inequalities, monotone quantities.
5. **c4** order-one coupling is the hard regime. Dropped: the hard part may be large fields, non-local effective actions, or infinite volume.
6. **e4** AF non-perturbatively, beta -> infinity is the right point.
7. **b2** Wilson action. Dropped: the action becomes a free design choice for provability.
8. **c1** existence before gap. Dropped: clustering and gap proved together. *Owner decision (T0 order).*
9. **b3** Euclidean. Dropped: Hamiltonian spectral tools.
10. **a3** gap on all of Omega-perp vs a chosen family's cyclic subspace (a silent weakening risk).
11. **c7** effective actions near-Wilson at the crossover.
12. **e9** IR easy once strong.
13. **b1** lattice at all.
14. **c2** RG frame at all scales.
15. **d2, d3, d9** discard tests resting on models where the target is true or on beliefs.

One line each for the first five (what a lane would do differently):
- e1: spend a bounded effort looking for a rigorous obstruction to the gap (a gapless scenario consistent with all theorems), so that the lane is not blind to a false target.
- f1: (not used) price the crossover as a finite certified computation and ask the owner whether that price changes the rule.
- a2: prove the gap for centre-stabilised SU(2) on R^3 x S^1_small as a rigorous intermediate result, and isolate the continuity statement as the single remaining obligation.
- c3: write the gap as a dichotomy whose gapless branch is excluded by a structural property, instead of carrying a numeric seed up the scales.
- c4: test, before investing in the crossover, whether large fields or effective-action non-locality are where every proof dies.

Rows whose drop would change an owner decision: f1, f2, f4, a1, a2, a8, c1.

