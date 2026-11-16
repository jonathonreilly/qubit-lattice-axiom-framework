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
3. not done.
4. not done.
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

