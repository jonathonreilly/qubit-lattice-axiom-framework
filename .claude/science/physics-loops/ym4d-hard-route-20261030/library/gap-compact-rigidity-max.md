lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-16T07:56Z

# gap-compact-rigidity-max: the compactness-and-rigidity architecture for the short step

Queue row 1017 of `FINISH.md`, read at commit 2cdb35e78. Worker: Claude Fable 5.2, max effort, Mac mini worker 2. Started 2026-11-15T19:56Z (`date -u`). No file is edited except this one (and any new lemma file under `library/` named below). No commit, no push: a relay copies this file.

This is research-stage working state. It grants no status. Marks used: PROVED (every step written here, by hand), ARGUED (argument given, one named step not written out), OPEN, FAILS (explicit counterexample or failing step).

## Plan (at most eight steps; one step per response; each step is appended before the next starts)

1. **Read and pin.** FINISH rules; `parts/gap.md` (Corollary Z4, Theorem ZD-c, the test table); rows 1002, 1011, 1013 and their notes; grep the lane for earlier compactness, limit-point and rigidity attempts ((N) of row 978, limit points of effective actions, `library/gap-ladder-max.md`, `library/gap-crux-fp.md`). Duplicate-attack check against `library/open-core.md` and the FINISH rows. Output: the exact statements this note reads, with file and line.
2. **Exercise skill and literature lens.** Fetch the exercise skill at main commit 8b11ae2bb9 into a new folder under /tmp, follow it. Literature: Kenig-Merle concentration-compactness and rigidity; limits of lattice gauge measures; generalized symmetries; what is published and what each source proves.
3. **Task (1), the compactness step.** State it exactly: topology, what is kept, what can be lost. Test it against the no-rigidity models first (Lemma PT, Proposition NP, the five-dimensional test of `library/gap-crux-fp.md`, a product with a massless factor).
4. **Task (2), the rigidity statement.** State it exactly. Test it against compact U(1) (it must fail there), frozen Q_8 and 2T.
5. **Task (3), first surviving piece.** Prove it by hand, or build the counterexample.
6. **Task (3) continued** if step 5 grows long, or the second surviving piece.
7. **Task (4), the consumer.** Which form of (W) or of the seed the contradiction yields; what it changes in `parts/gap.md`.
8. **Verdict table and RESULT line.**

## Step log

(Each step below is appended when it is finished. A step that stops early says where it stopped.)

## 1. Step 1 result: what was read, what is pinned, what was found again

### 1.1 The statements this note reads (file and line at commit 2cdb35e78)

- **Objects (DEF).** `library/gap-crux-restate.md` L29-45. Wilson SU(2), torus n = (n_1, ..., n_4), sides at least 3, Z(n), F = log Z, f = inf F(n)/abs(n), Delta(n) = F(n) - f abs(n) >= 0. Box B, transfer operator T_B, eigenvalues lambda_0 > lambda_1 >= ..., m(B) = log(lambda_0/lambda_1), S(k; B) = sum over i >= 1 of (lambda_i/lambda_0)^k. D(a) = Delta(a, a, a, a) (`library/gap-phys-seed.md` L247).
- **Engine.** Theorem S, `gap-crux-restate.md` L192-203; Corollary S3', L217-219. Lemma A, Lemma K, Lemma X, Lemma E (L37, L178-190). Checked in rows 698, 699.
- **Theorem ZD** (`gap-phys-seed.md` L296-304): at one coupling, (A) seed, (B) D(a) <= 6.1 x 10^(-4) for one a, (C) b m(b^3) >= 256 D(b/4) + 29.64 for one b, (D) "D bounded and sup of b m(b^3) infinite" are equivalent.
- **Theorem ZD-c** (L311-320): along a trajectory (a_j, beta_j) with the sizes P = {2^i l_1}, D^+(L) = limsup_j D_j(L/a_j), z^-(L) = liminf_j (L/a_j) m_j((L/a_j)^3): (PHYS-SEED) iff (BDD-Delta) and (Z-UNB).
- **Corollary Z4** (L322-323): if D(a) <= D_0 for a >= a_0, then either b m(b^3) < 256 D_0 + 29.64 for every multiple b >= 4 a_0 of 4 (**branch G, the gapless branch**), or there are N, c > 0 with m(L^3) >= c/N for all L >= 2N.
- **The wall (W)** (`parts/gap.md` L18-20): along the account's trajectory there is a physical size L in P with z^-(L) > 256 D_0 + 30, D_0 a bound of D^+ on the sizes from L/4 on.
- **Test table** (`parts/gap.md` L193-207) and its five points (L211-223). Point 5: no model of the SU(2) class with first-passage data and no gap is on record.
- **Lemma PT, Corollary PT1** (`library/gap-crux-exercise3-max.md` L690-720): products; a product with compact U(1) in its massless phase has no seed. **Proposition NP**: `library/gap-crux-exercise4-max.md` 5.1 (read in Step 3). **Five-dimensional test**: `library/gap-crux-fp.md` F15 (L50), L76, L88 (GUIDE grade).
- **Row 1002** (`library/prior/gap-kflow-read-opus.md` L95-102, L299, L324): every published monotone is blind; for SU(2) a_UV = 3 a_V, so an end with one or two free photons is allowed by the a-theorem.
- **Row 1011** (`library/gap-pinned-cell-gauge-max.md`): Proposition W (L184-199), the exact second-order Ward identity with its bracket term; Lemma CEN and Corollary CEN2 (L263-286): a link twist that is an exact symmetry is central, so it has no bracket. In its own reading (L290-292): "the symmetric link twists are the one-form symmetry, and a one-form symmetry is abelian."
- **Row 1013** (`library/gap-invent-selective-max.md` L250-252, L275-277): the 2D engine in 4D works only while a colour frame exists; the missing object is a short step at order-one response. Reopen conditions (i), (ii).

### 1.2 Earlier compactness, limit-point and rigidity attempts in the lane (found again; none is a Kenig-Merle architecture)

Grep of `library/gap-*.md`, `library/prior/gap-*.md`, `parts/*.md` for: Kenig, concentration compactness, critical element, profile decomposition (no hit outside this file); rigidity; limit point, limit object, subsequence, tightness, scale-invariant limit, massless limit; one-form, generalized symmetry, emergent.

| Earlier item | Where | What it holds | Relation to this row |
|---|---|---|---|
| Crux lemma (N) of A1, row 978 | `library/gap-ladder-max.md` L67 | "a seed with margin for every limit point of the reference-scale effective actions, in a topology in which the seed functional is continuous"; first doubt: closeness of order 1/volume in the local sup norm is needed | This is the compactness step in its direct form. It was named, not attacked. Step 3 below states it exactly and tests it. |
| A6, continuum value, row 978 | same file L77 | "(C + N): the limit exists, and it is below 1/5041 at one ell_*"; doubt: the thermal sum is a trace over all states of a large box | Same object: a limit of ratios of torus partition functions. |
| Limit states of a seeded sequence | `library/gap-seed-limit.md` L140-172, L258-282 | Tychonoff compactness for states on local functions of the lattice at one coupling; every limit state clusters, GIVEN the gap hypothesis (G) | Compactness of the gapped branch, on the lattice at fixed coupling. Not a limit along the trajectory, and not the gapless branch. |
| Item 29 of the second brainstorm | `library/gap-brainstorm2-max.md` L179, L239, L318 | "either (Z-UNB) holds, or the limit theory contains a massless singlet vector state, that is, an emergent conserved two-form current. Then exclude the second branch for SU(2) (no continuous one-form symmetry survives non-abelian fusion)"; verdict there: "needs a monotone parameter ... equals Theorem R" | The rigidity seed of this row, in one sentence, dropped without a statement. This row states it and tests it (Step 4). |
| Row 745 literature | `library/prior/gap-lit-rigid.md` | Nguyen, Tanizaki and Unsal 2023 (arXiv:2306.02485): for a gapped 4D theory with Z_N one-form symmetry, the pattern of light flux sectors, under a 0/1 assumption on sector ratios | Rigidity inside the gapped branch (Theorem R of row 742). Not the gapless branch. |
| Soft exclusion of branch G | row 988 Route 3 (`parts/gap.md` L61-62, L65-66) | set aside; re-judged "too strong" by row 998 6d | The only earlier attempt on branch G by soft means. Its verdict binds Step 4: a class-wide soft statement with no ultraviolet hypothesis is refuted by w_p (Proposition V) and by U(1). |
| "Rigidity" elsewhere in the lane | `gap-means-max.md` (duality rigidity, Theorem R); `gap-seeddec-max.md` (rigidity of minimal fillings) | other meanings of the word | none |

### 1.3 Duplicate-attack check (rule 0a)

`library/open-core.md`: no line on compactness, rigidity, a critical element, a limit object, branch G, or a one-form symmetry (grep, zero hits). FINISH rows naming these words: 745 (literature on flux-sector rigidity) and 1017 (this row). Row 1016 (`gap-global-reform-max`, running now on worker 1) takes reopen condition (i) of row 1013: an exact reformulation with a global non-abelian symmetry. It is not this architecture. I do not attack its candidates. I do not attack (CAS), (HC-phys), (MONO-Delta), (TUBE'), (NOCRIT) or any statement that an earlier row holds; where a step below reduces to one of them, I name the match and stop there.

### 1.4 Not read in Step 1

The bodies of rows 1003, 1004, 988, 982; the account's TeX; every primary paper. Each is read at the step that needs it.

## 2. Step 2 result: the exercise frame, the inventory for this architecture, the literature lens

### 2.1 How the exercise skill is applied

Skill text: `docs/ai_methodology/skills/exercise/SKILL.md` at main commit 8b11ae2bb9 and the reference it names for proof work, `skills/physics-loop/references/proof-search-governance.md`, both fetched by URL into new scratch folders under /tmp and read in full. This target is a standalone proof target, so `GOAL.md` and the FINISH rules replace the framework refresher read (the skill allows this replacement and asks that it is said). No subagents; the "independent passes" of skill step 7 are separate passes of this one session and are not independent.

The wall has had four exercises (rows 878, 998, 1003, 1011) and one invention row (1013). By skill step 0 ("do not re-derive a mapped wall") their inventory (row 998 Section 2, 40 items), assumption table and set-aside list are reused, not rewritten. This row runs the skill on one architecture only. The skill steps map to the plan as follows: steps 0-1 are Section 1 and 2.2; step 2 is 2.3; step 3 is 2.5; steps 4-6 are in Sections 3 and 4 (the assumptions and the discard tests that bind a limit argument); step 7's literature lens is 2.4; step 8 is Sections 5-6; step 9 is Sections 7-8.

**Target contract (governance format).** Target statement: (W) of `parts/gap.md` L18-20. Quantifiers: one trajectory of the account (first-passage data, dilated); there exists one physical size. Allowed premises: the account's statements as cited (unchecked), the lane's checked lemmas, published theorems rebuilt or named. Forbidden weakenings: a statement for a sector only, a statement with an unproved monotony. Required comparison cases: compact U(1), frozen Q_8 and 2T, products with a massless factor, five dimensions. Completion witness: a written proof of (W), or of a statement proved here to give (W). Outcomes that do not count: a renamed crux; a conditional chain whose terminal statement is (W) or stronger.

### 2.2 The wall and the architecture, in plain words

We want to show that the four-dimensional SU(2) theory has a lowest particle mass above zero. The lane has reduced this to one inequality at one physical box size. The lane cannot prove it, because every exact tool it has also holds for theories with a massless particle. The architecture of this row is a proof by contradiction of a kind that solved hard problems for nonlinear waves (Kenig and Merle). Suppose the inequality fails at every size. Look at the theory at larger and larger sizes and rescale. If the rescaled pictures stay in a compact set, a limit picture exists. This limit would be a theory that looks the same at all scales and has no mass gap. Then show that no such limit can come from SU(2). The first half (a limit exists) is soft. The second half (no such limit) must use what SU(2) has and a photon lacks. Passing means: a proof of both halves, or an exact statement of what the second half must use, with the cases where it fails.

### 2.3 Inventory for the architecture (items the limit argument reads; marks as in the skill)

| # | Item | Mark | Source | Standing, reading state |
|---|---|---|---|---|
| A1 | For every torus n, Z(n) = Tr T_B^(n_1), T_B positive and trace class, top eigenvalue simple; Z is symmetric in the four sides. | THM, lane | `gap-crux-restate.md` L33, L174-176 | checked rows 671, 698, 699 |
| A2 | Delta(n)/abs(n) does not increase when a side is multiplied by an integer. Delta >= 0. | THM, lane | same file L39-43 | checked rows 698, 699 |
| A3 | The engine: Theorem S, Theorem SH, Proposition Delta, Lemmas Z, Z', Z3, Theorem ZD, Corollary Z4. Each is a finite chain of inequalities between values of Z at finitely many tori. | THM, lane | Section 1.1 above | S, SH, Delta checked; ZD, Z4 "PROVED GIVEN", lane check row 727 |
| A4 | The centre flips C_nu commute with T; twisted partition functions are traces with C_nu inserted; 0 <= Z_odd <= Z. | THM, lane | `gap-crux-restate.md` L35, L98, L105 | checked rows 698, 699 |
| A5 | Along the account's trajectory the Casimir free energy of each of its tori is bounded for each fixed physical size, given (UV-Z) and the density statement: (TH), 1.1.5 (iii). | THM given the account | `gap-phys-seed.md` L92; `gap-ladder-max.md` L150, L197 | conditional; checked as a conditional, row 727; assumptions (a), (b) unchecked |
| A6 | (BDD-Delta), a bound of D^+ uniform in the physical size, is not proved. It holds in every comparison model on record. | OPEN; BELIEF for SU(2) | `gap-phys-seed.md` L316-318, L336 | - |
| A7 | Compact U(1), Villain form, beta >= 2^14: no uniform Langevin gap on periodic tori; a massless phase (Guth; Frohlich and Spencer). | THM, published, recalled; THM, lane for the Langevin form | row 786; I28 of row 998 | lane: proved by Codex, check row 794; the seed form "no seed" is taken from I28 |
| A8 | Frozen Z_2 at large beta: eight degenerate flux sectors on every periodic box. | THM, lane | test table, `parts/gap.md` L198 | Peierls, beta above 2.191 |
| A9 | Kenig and Merle: for the energy-critical focusing NLS (radial) and NLW, below the ground-state energy, failure of scattering gives a critical element that is compact modulo the symmetries and has minimal energy; a rigidity theorem excludes it. | THM, published | arXiv:math/0610266, math/0610801 | abstracts read in this run; proofs recalled |
| A10 | In a four-dimensional conformal Haag-Kastler net the massless particle spectrum is generated by a free field subnet; for a scalar spectrum the free subnet is a tensor factor. | THM, published | Tanimoto, arXiv:1310.4744 | abstract read; proof not read |
| A11 | A one-form symmetry of a four-dimensional conformal theory "can be realized by free Maxwell electrodynamics". A perimeter law for a line charged under a continuous one-form symmetry gives a gapless mode. | physics theorem | Hofman and Iqbal, arXiv:1802.09512; Lake, arXiv:1802.07747 | abstracts read |
| A12 | Emergent higher-form symmetries are exact at low energy: "robust to arbitrary local UV perturbations in the thermodynamic limit". | physics argument with lattice models | Pace and Wen, arXiv:2301.05261 | abstract read |
| A13 | Every local net has a scaling limit, possibly not unique (ultraviolet side; compactness of states on the scaling algebra). | THM, published | Buchholz and Verch, arXiv:hep-th/9501063 | abstract read |
| A14 | For a conformal theory on a spatial torus, scale and Lorentz invariance give the density of states at high energy from the vacuum energy between plates. | physics theorem | Shaghoulian, arXiv:1508.02728 | abstract read |
| A15 | A unitary four-dimensional theory whose infrared asymptotics is perturbative is asymptotically conformal; scale invariance gives conformal invariance under conditions. | physics theorem | Luty, Polchinski and Rattazzi, arXiv:1204.5221; Dymarsky, Komargodski, Schwimmer and Theisen, arXiv:1309.2921 | abstracts read |
| A16 | Gauge theories with adjoint matter keep the centre one-form symmetry and are asymptotically free for few flavours; some are believed to have a massless infrared end (the Coulomb branch of N = 2 SU(2), Seiberg and Witten; the Georgi-Glashow Coulomb phase; a conformal window). | BELIEF (physics; no construction) | recalled | not read in this run |
| A17 | SU(2) Wilson in five dimensions at weak coupling has massless gluons. | BELIEF (numerics) | `gap-crux-fp.md` F15 | GUIDE there |

### 2.4 Literature lens (skill step 7): templates, known no-go results, known escapes

One search, by the arXiv API, 14 records fetched into a new scratch folder, abstracts read (list in 2.3 and below). No paper or passage is copied. The lane's records on monotones (row 1002), on gauge stiffness (row 1012) and on flux rigidity (row 745) are reused and were not searched again.

| Source | What it shows | Maps to the lane? | What does not map | Read |
|---|---|---|---|---|
| Kenig and Merle 2006, 2008 (arXiv:math/0610266, math/0610801) | The roadmap: a small-data theory; a critical element by concentration compactness, compact modulo the symmetry group; rigidity by a virial identity with a sign. | Yes, in form. Small data = the seed basin (Theorem S). The symmetry is the dilation. The critical element is the object of Theorem CE below. | The minimisation over data. The continuum theory is one orbit of the dilation, so there is no family to minimise over. The virial identity has no counterpart with a sign (it would be (CAS) or (MONO-Delta)). | abstracts; proofs recalled |
| Gidas and Spruck 1981 (Comm. PDE 6) | A priori bounds from "blow-up, then a Liouville theorem on the limit". | Yes: this is the closer template. A uniform bound is equivalent to the absence of entire limit objects. | The Liouville theorem there is for one explicit equation. | recalled, not fetched |
| Buchholz and Verch 1995 (arXiv:hep-th/9501063) | Limits under dilation always exist as states on a scaling algebra; they can be non-unique or classical. | Precedent for the compactness step. | It is the ultraviolet limit, and it keeps no finite-volume spectrum. | abstract |
| Tanimoto 2014 (arXiv:1310.4744); Buchholz and Fredenhagen 1977 (J. Math. Phys. 18, recalled) | Rigidity of conformal limits: massless particles are free; a scalar free part is a tensor factor. | It says what a scale-invariant massless limit looks like: free part times a rest. This is the product of Lemma PT. | It needs a conformal net on Minkowski space. It does not exclude the limit; it describes it. | abstract; BF recalled |
| Hofman and Iqbal 2018; Lake 2018; Gaiotto, Kapustin, Seiberg and Willett 2014 (arXiv:1412.5148) | Photon = Goldstone mode of a continuous one-form symmetry; in a CFT_4 a one-form symmetry current is a free Maxwell field. | It is the row's first rigidity seed in published form. | It runs from a symmetry to a photon. The row needs the converse, and then an exclusion. | abstracts |
| Pace and Wen 2023 (arXiv:2301.05261); Cordova, Ohmori and Rudelius 2022 (arXiv:2202.05866) | Emergent one-form symmetries are exact below the scale of the charged objects. | **Known escape for the first seed.** "It would have to emerge exactly" is not an obstruction: exact emergence is the generic case. | - | abstracts |
| Nguyen, Tanizaki and Unsal 2023 (arXiv:2306.02485), on file in row 745 | The flux pattern of gapped phases with a Z_N one-form symmetry. | Rigidity inside the gapped branch (Theorem R). | Not the gapless branch. | row 745's reading |
| Shaghoulian 2015; Belin and others 2016 (arXiv:1610.06186) | Torus partition functions of conformal theories in d > 2: crossing gives a Cardy formula and constraints. | The engine's class at a scale-invariant point. Theorem ZD (C) is a bound of this kind (the gap of the box is bounded by the Casimir free energy). | No statement excludes a massless spectrum; free Maxwell is one of their checks. | abstracts |
| Komargodski and Schwimmer; Casini, Teste and Torroba (row 1002) | Monotones along the flow. | A blind monotone is still useful in this architecture: it would turn a recurrent limit set into a set of fixed points. It cannot give rigidity. | No lattice or rigorous form. | row 1002's reading |

**Known no-go for soft rigidity (from the table).** A limit of the kind the architecture extracts exists in theories that share the gauge group, the centre symmetry, reflection positivity and asymptotic freedom with pure SU(2) (A16, belief grade), and in pure lattice gauge theories of the lane's class at tuned couplings (the K7 end point, belief grade; frozen Z_2, theorem grade). So no rigidity statement can rest on those four properties alone.

**No published source was found** that runs a compactness-and-rigidity argument for a lattice gauge theory or for a mass gap in quantum field theory. Scope of this "not found": the 14 records above, the lane's literature files named in 1.2, and recall. It is not a claim of novelty.

### 2.5 Reasoning up (skill step 3): what follows at once for this architecture

- **C1 (from A1-A4).** The whole engine reads one function, Z on quadruples of sizes, and its twisted forms. A limit of such functions keeps every non-strict inequality between finitely many values. So the engine holds on every limit object. Compactness in this topology costs one bound: the Casimir free energy at the sizes used.
- **C2 (from A3).** For one cutoff, the set of dyadic sizes that carry a seed is closed upwards (Theorem S). So the failure of (PHYS-SEED) has a uniform form along a subsequence: the first seed size runs to infinity. This is what makes a common limit possible (Lemma UF in Section 3).
- **C3 (from A1, A9).** The object the lane can extract is not a minimal counterexample. It is a blow-down limit: an object defined at all dyadic scales, upwards and downwards, with no seed at any scale and bounded Casimir free energy. Its ultraviolet end is not asymptotically free: the limit forgets the ultraviolet data of the trajectory.
- **C4 (from A7, A8, C1).** The limit class contains the photon (theorem grade for Villain U(1) at large beta, given the lane's reading of A7), the frozen Z_2 object (constant Delta = log 8), and every product of a limit object with these. So rigidity in the limit class is false. A rigidity statement has to read a property that the limit keeps from the SU(2) trajectory and that these objects lack.
- **C5 (from C3, A16, A17).** The properties a limit keeps are closed conditions that hold at every large scale. The gauge group, the centre symmetry, reflection positivity and integer multiplicities are kept, and they do not separate SU(2) from the comparison objects. The asymptotic freedom of the trajectory is a statement at small scales and is not kept by the blow-down. It can enter only through a quantity that is monotone or conserved along the scales.
- **C6 (the gain of the architecture, to be proved in Section 3).** Compactness turns a strict inequality without a rate into a uniform one. So the order-one input can be a statement about each limit object, with no number in it (a Liouville statement). This is weaker in form than (CAS) with theta below 1.
- **C7 (belief).** A rigidity proof must use that the theory is pure gauge and that its continuum limit is unique. These are the properties that A16 lacks. No exact identity on record carries them to the limit.

