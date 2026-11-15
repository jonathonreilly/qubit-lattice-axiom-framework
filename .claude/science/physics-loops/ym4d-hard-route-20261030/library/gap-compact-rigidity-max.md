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

## 3. Step 3 result (Task 1): the compactness step, stated exactly and proved; what is kept, what is lost; the first tests

Everything in 3.1-3.6 is proved by hand here from the lane's checked statements A1-A4 and Lemma Z. Nothing is checked by another model. No run was made.

### 3.1 Definitions

**Datum.** A datum is a function Z from quadruples n of integers n_i >= 3 to the positive numbers with:

- (E1) Z is symmetric under permutations of the four sides;
- (E2) for each box B = (n_2, n_3, n_4) there are numbers lambda_0(B) > lambda_1(B) >= lambda_2(B) >= ... >= 0 with Z(k, B) = sum over r of lambda_r(B)^k for every k >= 3;
- (E3) f := inf over n of log Z(n)/abs(n) is finite.

Every model of the engine's class at one coupling is a datum (A1). For a datum: Delta(n) = log Z(n) - f abs(n) >= 0, D(a) = Delta(a, a, a, a), and the levels E_r(B) := - log lambda_r(B) + f abs(B) (with E_r = +infinity if lambda_r = 0), so that

 exp Delta(k, B) = sum over r of exp(- k E_r(B)).

E_0(B) <= 0, because Delta(k, B) >= 0 for all k and Delta(k, B) + k E_0(B) = log(1 + S(k; B)) tends to 0 as k grows. S(k; B) = sum over r >= 1 of exp(- k (E_r(B) - E_0(B))) and m(B) = E_1(B) - E_0(B).

**Dyadic scales.** DD = {2^i : i in Z}. A quadruple x in DD^4 is a physical torus in units of one size l_1. An **eternal datum** is a function Delta_* from DD^4 to [0, infinity).

**Rescaling.** Let Z_j be data and u_j >= 3 integers (the number of lattice sites in the length l_1; for one model at one coupling, Z_j = Z and u_j = u). For k >= 0 and x in DD^4 with all x_i >= 2^(-k) put

 Delta^(j,k)(x) := Delta_j(2^k u_j x), and e_r^(j,k)(B) := 2^k u_j E_r^(j)(2^k u_j B) for B in DD^3.

Then exp Delta^(j,k)(T, B) = sum over r of exp(- T e_r^(j,k)(B)). Put D^(j,k)(b) = Delta^(j,k)(b, b, b, b), s^(j,k)(b) = S_j at the time 2^k u_j b/2 on the cube of side 2^k u_j b, and z^(j,k)(b) = b (e_1^(j,k) - e_0^(j,k))(b, b, b).

**Admissible sequence, with the bound D_0.** A sequence (j_i, k_i), k_i -> infinity, such that for every m in Z there is i(m) with, for all i >= i(m):

- (H1) D^(j_i,k_i)(2^m) <= D_0 + 1/i;
- (H2) s^(j_i,k_i)(2^m) >= 1/5041 (no seed of Theorem S at the size 2^(k_i+m) u_(j_i)).

**Critical element.** An eternal datum Delta_* with, for every b in DD: s_*(b) >= 1/5041, d_min <= D_*(b) <= D_0 with d_min := (1/8) log(1 + 1/5041) > 2.47 x 10^(-5), and z_*(b) <= 256 D_*(b/4) + 34.11. (The quantities s_*, z_* are defined from the levels of the limit in Theorem CE (b).)

### 3.2 Lemma UF (the failure of the seed has a uniform form; PROVED given Theorem S)

Let Z_j, u_j be as above and P = {2^i : i >= 0}. Suppose that for every l in P the upper limit over j of S_j(l u_j/2; (l u_j)^3) is at least 1/5041. (This is the failure of (PHYS-SEED) with the threshold of Theorem S.) Then there is a subsequence along which, for every l in P, S_j(l u_j/2; (l u_j)^3) >= 1/5041 for all large j.

Proof. For each j let l*_j be the least l in P with S_j(l u_j/2; (l u_j)^3) < 1/5041, or infinity. By Theorem S (the map x -> ((1 + x)^64 - 1)^2 sends [0, 1/5041) into itself), a seed at l gives a seed at 2l, so the sizes with a seed are exactly the l >= l*_j. Suppose l*_j <= L for all large j. Then for all large j, S_j at the size L is below 1/5041, and by Theorem S, S_j at the size 2L is at most c_S := ((1 + 1/5041)^64 - 1)^2 <= (e^(64/5041) - 1)^2 < (0.01278)^2 < 1.64 x 10^(-4) < 1/5041. So the upper limit at 2L is below 1/5041, against the hypothesis. Hence for each i there are infinitely many j with l*_j > 2^i. Choose j_1 < j_2 < ... with l*_(j_i) > 2^i. QED

At one coupling the statement is empty: branch G of Corollary Z4 is "no seed at any size".

### 3.3 Theorem CE (compactness; PROVED given A1-A4, Lemma Z, Proposition Delta)

**(i) Existence of admissible sequences.** (a) One datum in branch G: if D(a) <= D_0 for all a >= a_0 and no size has a seed, then every sequence (j, k_i) with k_i -> infinity is admissible. (b) A trajectory: if (BDD-Delta) holds with the bound D_0 from L_0 on, and (PHYS-SEED) fails, then there is an admissible sequence with j_i -> infinity.

**(ii) Limit.** Every admissible sequence has a subsequence along which Delta^(j_i,k_i)(x) converges for every x in DD^4, to an eternal datum Delta_*, and e_r^(j_i,k_i)(B) converges in (-infinity, +infinity] for every r >= 0 and every B in DD^3, to e_r^*(B). The limit has these properties.

- (a) Delta_* is symmetric, and Delta_*(x) <= (x_1 x_2 x_3 x_4/mu^4) D_0 with mu = min x_i.
- (b) Spectral form. For every T in DD and B in DD^3: exp Delta_*(T, B) = sum over r of exp(- T e_r^*(B)), with e_0^*(B) <= e_1^*(B) <= ..., e_0^*(B) finite and at most 0. So in each of the four directions the limit is a sum of exponentials with multiplicities that are non-negative integers. S_*(T; B) := sum over r >= 1 of exp(- T (e_r^* - e_0^*)(B)) is the limit of the rescaled thermal sums.
- (c) Every inequality of the engine that is non-strict and reads finitely many values holds for the limit. Examples: Delta_*(2 x_1, x_2, x_3, x_4) <= 2 Delta_*(x); S_*(2b; (4b)^3) <= ((1 + S_*(b; (2b)^3))^64 - 1)^2; S_*(b; (2b)^3) <= exp(8 D_*(b)) - 1.
- (d) Delta_* is a critical element.
- (e) Centre grading. Along a further subsequence each twisted quotient Z^(1 nu)/Z converges, and each level r of each box has a limit sign eps_r^nu in {+1, -1}, nu = 2, 3, 4, with eps_0^nu = +1 and zeta_*^(1 nu)(T, B) exp Delta_*(T, B) = sum over r of eps_r^nu exp(- T e_r^*(B)).

Proof. (i)(a) is the definition. (i)(b): by Lemma UF take a subsequence J with l*_j -> infinity. Let i_0 be such that 2^(i_0) >= L_0. For i >= 1 put k_i = 2i + i_0 and choose j_i in J, j_i > j_(i-1), with l*_(j_i) > 2^(k_i + i) and D_(j_i)(2^(k_i+m) u_(j_i)) <= D_0 + 1/i for the finitely many m with abs(m) <= i. The second condition holds for all large j, because the sizes 2^(k_i+m) are at least 2^(i_0) >= L_0 and D^+ <= D_0 there. Then (H1) and (H2) hold with i(m) = abs(m).

(ii) Step 1, bounds. Fix x in DD^4 with least entry mu = 2^m. The torus 2^k u x arises from the symmetric torus of side 2^k u mu by multiplying sides by powers of 2. By A2, Delta^(j,k)(x) <= (x_1 x_2 x_3 x_4/mu^4) D^(j,k)(mu) <= C(x) := (x_1 x_2 x_3 x_4/mu^4)(D_0 + 1) for i >= i(m). Fix B in DD^3 and T in DD. From exp(- T e_0) <= exp Delta(T, B): - C(T, B)/T <= e_0^(j,k)(B) <= 0. The number of levels r with e_r <= E is at most exp(T E + C(T, B)), because each such level adds at least exp(- T E) to exp Delta(T, B).

Step 2, extraction. DD^4 and DD^3 x {0, 1, 2, ...} are countable. The numbers Delta^(j_i,k_i)(x) lie in [0, C(x)] for large i, and each e_r^(j_i,k_i)(B) lies in [- C/T, +infinity]. A diagonal subsequence makes all of them converge.

Step 3, the spectral form. Fix T and B, and write C' = C(T/2, B). For E > 0 let R(E) be the integer part of exp(T E/2 + C') + 1. By Step 1 at the time T/2, for every i (large) the levels with index r >= R(E) are above E, so e_r^* >= E for these r, and

 sum over r >= R(E) of exp(- T e_r^(i)) <= exp(- T E/2) sum over r of exp(- (T/2) e_r^(i)) <= exp(- T E/2 + C').

The same bound holds for the limit levels (each partial sum of the limit series is a limit of partial sums). The finite sum over r < R(E) converges term by term (a term with e_r -> +infinity tends to 0). So the upper and lower limits of sum over r of exp(- T e_r^(i)) differ from sum over r of exp(- T e_r^*) by at most 2 exp(- T E/2 + C'), for every E. This gives (b). e_0^* is finite by Step 1. Symmetry and the bound in (a) pass to the limit.

Step 4, the thermal sums. S^(i)(T; B) = exp(Delta^(i)(T, B) + T e_0^(i)(B)) - 1 converges to exp(Delta_*(T, B) + T e_0^*(B)) - 1 = S_*(T; B). So every non-strict inequality between finitely many values of Delta, S, e_0, e_1 that holds for each datum holds in the limit: (c). The three examples are A2, Theorem S, and Proposition Delta at b = 2a.

Step 5, (d). By (H2) and Step 4, s_*(b) >= 1/5041. By (H1), D_*(b) <= D_0. For each datum, Proposition Delta gives S(a; (2a)^3) <= exp(8 D(a)) - 1, so (H2) gives exp(8 D^(i)(b/2)) - 1 >= 1/5041 at every scale, and D_* >= d_min. For each datum, Lemma Z with T_0 = b/4 and T = b/2 gives S(b/2; b^3) <= exp(64 D(b/4) - (b/4) m(b^3)). With (H2): (b/4) m(b^3) <= 64 D(b/4) + log 5041, and 4 log 5041 < 34.11. Since z^(i)(b) = b (e_1^(i) - e_0^(i)) converges to z_*(b), the bound passes to the limit; in particular e_1^* is finite on cubes.

Step 6, (e). The centre flips commute with T_B, so the levels can be listed with signs: Z^(1 nu)(k, B) = sum over r of eps_r^nu lambda_r^k, eps_0^nu = +1 (A4). The quotients lie in (0, 1] and the signs in a finite set, so a further diagonal subsequence makes them converge. The proof of Step 3 applies to the signed series, because its tail is bounded by the unsigned tail. QED

Remarks. (1) Only doublings are used, so the limit is defined on dyadic sizes. (2) The hypothesis of (i)(b) is exactly the branch that Theorem ZD-c leaves when (BDD-Delta) holds. If (BDD-Delta) fails, (W) fails by Theorem ZD-c and no limit is extracted here; that branch is the open statement (BDD-Delta) (A6), which I do not attack. (3) The constants 2.47 x 10^(-5) and 34.11 replace the lane's 6.1 x 10^(-4) and 29.64. They come from Theorem S's threshold alone and need the same scale only. The lane's sharper values (Theorem SH) also pass to the limit, with five more doublings in the window.

### 3.4 What the limit keeps and what it can lose

| Kept (PROVED in Theorem CE) | Form in the limit |
|---|---|
| Positivity of the transfer operator in each direction (reflection positivity of partition functions) | (b): a sum of exponentials with non-negative integer multiplicities, in each of the four directions |
| The exchange of axes | (a) |
| The engine | (c) |
| The centre symmetry | (e): a Z_2^3 grading of the levels of each box, vacuum even |
| The gapless branch at every scale, upwards and downwards | (d) |

| Can be lost | Why, with an example |
|---|---|
| The simple ground state | Levels can merge with the vacuum: z_* = 0 is allowed. Example: the data A_eps of 3.6 (limit constant log m). |
| Levels above every bound | e_r^* = +infinity is allowed; harmless. |
| **The ultraviolet data of the trajectory** | By (d), D_* <= D_0 at every scale, small scales included. On the trajectory the Casimir free energy is believed to grow like log(1/g(L)) at small L (`gap-phys-seed.md` L109, GUIDE). The blow-down shifts every fixed physical scale to zero. Asymptotic freedom is a statement at fixed physical scales, so the limit does not carry it. |
| The gauge group, the action, the Markov property of the plaquette weight | The limit is a function of four sizes with signs. Lemma PT-inf (3.6): it is the same for a model and for its product with any seeded factor. |
| Sizes that are not dyadic; rotations beyond the exchange of axes | not in the construction |
| Scale invariance | not automatic: the limit set is invariant under the doubling, a limit need not be a fixed point (3.5) |
| Uniqueness | different subsequences may give different limits |
| Completeness of the gauge-invariant observables | The limit holds no observables. An enriched limit is discussed in Section 4. |

So the answer to the row's first question is: reflection positivity and the centre symmetry are kept; **the account's ultraviolet data are not kept by any blow-down limit.** A limit that keeps them is the continuum limit at fixed physical sizes (k_i fixed, j_i -> infinity; it needs A5 at each size). That object is the theory itself, not a scale-compact critical element, and a Liouville statement for it is (W) in other words.

### 3.5 Proposition OM (the set of critical elements; PROVED, elementary topological dynamics)

Fix the family (Z_j, u_j) and D_0. Let Omega be the set of all limits of admissible sequences, with the topology of pointwise convergence on DD^4, and sigma the doubling: (sigma Delta)(x) = Delta(2x).

- (a) Omega is compact, and sigma is a homeomorphism of Omega onto itself.
- (b) Omega is empty if and only if no admissible sequence exists. For a trajectory with (BDD-Delta): Omega is empty if and only if (PHYS-SEED) holds.
- (c) (Stall.) If Omega is not empty, then for every continuous function Lambda on Omega there are elements E_+ and E_- with Lambda(sigma E_+) >= Lambda(E_+) and Lambda(sigma E_-) <= Lambda(E_-). In particular some critical element has D_*(2) >= D_*(1).
- (d) (Recurrence.) If Omega is not empty, it contains a uniformly recurrent element E: for every finite set of quadruples and every eps > 0, the integers t with abs(sigma^t E - E) < eps on that set have bounded gaps.
- (e) (A monotone gives stationarity.) If Lambda is continuous and Lambda(sigma E) <= Lambda(E) on Omega, then Lambda is constant on the orbit closure of every uniformly recurrent element.

Proof. (a) Omega lies in the product of the intervals [0, C(x)], which is compact and metrisable. Closed: let E_n in Omega tend to E. Enumerate DD^4. For each n choose an index of the admissible sequence of E_n so far out that the rescaled datum is within 1/n of E_n on the first n quadruples, k >= n, and (H1), (H2) hold for abs(m) <= n with 1/n in place of 1/i. These indices form an admissible sequence with limit E. sigma maps the limit of (j_i, k_i) to the limit of (j_i, k_i + 1), which is admissible; the same for k_i - 1. sigma is continuous for pointwise convergence.
(b) The first sentence is Theorem CE (ii). If (PHYS-SEED) fails, Theorem CE (i)(b) gives an admissible sequence. If it holds at a size l with S_j <= q'/5041, q' < 1, for all large j, then Theorem S gives S_j <= q'^(2^k)/5041 < 1/5041 at the sizes 2^k l, so (H2) fails at every scale for large i.
(c) If Lambda(sigma E) < Lambda(E) for all E, the continuous function Lambda - Lambda o sigma has a positive minimum delta on the compact set Omega, and Lambda(sigma^n E) <= Lambda(E) - n delta is unbounded below; but Lambda is bounded. The other case is the same for sigma^(-1). Take Lambda(E) = D_E(1); then Lambda(sigma E) = D_E(2).
(d) The closed non-empty sigma-invariant subsets of Omega, ordered by inclusion, have a minimal member (Zorn's lemma; a chain has a non-empty intersection by compactness). Let M be minimal, E in M, and U an open neighbourhood of E. For y in M the orbit of y is dense in M, so M is covered by the open sets sigma^(-n) U, n in Z, and by finitely many of them, n = n_1, ..., n_p. For each t, sigma^t E lies in some sigma^(-n_l) U, so sigma^(t + n_l) E lies in U. The return times have gaps at most 2 max abs(n_l).
(e) Lambda(sigma^n E) is non-increasing in n and bounded. By (d) there are n_i -> +infinity with sigma^(n_i) E -> E (the forward limit set of E is closed, invariant and not empty, so it is M). So Lambda(E) = lim Lambda(sigma^(n_i) E) = inf over n >= 0, and Lambda(sigma^n E) = Lambda(E) for n >= 0. The same argument at sigma^(-n) E gives all n. Lambda is continuous and the orbit is dense in its closure. QED

### 3.6 Theorem CR (the wall in Liouville form) and what it adds to (CAS)

**Theorem CR (PROVED given Theorem ZD-c and 3.2-3.5).** For a trajectory with (BDD-Delta), these are equivalent: (1) (W); (2) (PHYS-SEED); (3) Omega is empty; (4) Omega has no uniformly recurrent element; (5) for one continuous Lambda, no element of Omega has Lambda(sigma E) >= Lambda(E).

Proof. (1) and (2) are equivalent by Theorem ZD-c given (BDD-Delta). (2) and (3): Proposition OM (b). (3) gives (4) and (5) at once; (4) gives (3) by OM (d); (5) gives (3) by OM (c). QED

**What is new against (CAS).** Row 708 (`gap-mid-max.md` L64-67) states (CAS) with a number theta < 1 on a range, and judges: "(CAS) is the statement that the theory has no fixed point of the doubling map above the threshold ... it restates the seed in steps." Theorem CR is the exact form of that sentence. It shows: (i) no rate is needed. A strict inequality on each limit object, with no uniformity, is enough: this is (5). (ii) The objects that must be excluded are not only fixed points. They are the uniformly recurrent critical elements; they are fixed points only if a monotone exists (OM (e)), and a blind monotone would do for that. (iii) The form (5) with Lambda = D reads: the wall holds as soon as no critical element has a doubling on which its Casimir free energy does not fall.

**What is not new.** The content. Theorem CR is an equivalence, so each of (3)-(5) is target-equivalent. The gain is in the form: the order-one input is now a statement about limit objects with exact scale covariance, and with no number in it.

### 3.7 The first test: no-rigidity models inside the limit class (Lemma PT, Proposition NP, five dimensions)

**The data A_(m,eps) (PROVED; an explicit family).** For an integer m >= 2 and eps > 0 put Z(n) = 1 + (m - 1) exp(- eps abs(n)). (E1) is clear. (E2): T_B = diag(1, t, ..., t) on C^m with t = exp(- eps abs(B)) < 1. (E3): f = 0. So A_(m,eps) is a datum, with Delta(n) = log(1 + (m - 1) exp(- eps abs(n))). Take eps_j -> 0, u_j = 3 and k_i with eps_(j_i) 16^(k_i + i) 3^4 -> 0. Then (H1) holds with D_0 = log m, (H2) holds because s = (m - 1) exp(- eps abs(n)) -> m - 1 >= 1, and the limit is the constant Delta_* = log m. So **the constants log m, m >= 2, are critical elements**, fixed by sigma, with z_* = 0 and all m levels at the vacuum.

Realisations in lattice models (recalled, not rebuilt): the Ising model on Z^4 in its ordered phase gives log 2 (the model of Proposition NP's input (i5)); frozen Z_2 gauge theory gives log 8 (eight flux sectors, `gap-mid-max.md` L66). The data A_(m,eps) themselves are a model of slow tunnelling between m vacua.

**Lemma PT-inf (products in the limit; PROVED given Lemma PT (a), (c)).** Let two families of data share the units u_j, and let (j_i, k_i) be a sequence along which both rescaled families converge, to Delta_*^1 and Delta_*^2. Then the product family converges to Delta_*^1 + Delta_*^2, its levels are the sums e_r^1 + e_q^2, and 1 + S_* = (1 + S_*^1)(1 + S_*^2). Consequences:

- (i) If Delta_*^1 is a critical element and D_*^2 is bounded, the sum is a critical element (with the bound D_0^1 + D_0^2 and with z_* = min).
- (ii) If the second family has a seed (uniformly: (PHYS-SEED)), then Delta_*^2 = 0 (Lemma Z3: its Casimir free energy tends to 0 along the doublings), and the limit of the product is Delta_*^1. **The blow-down limit forgets every seeded factor.**

Proof. Lemma PT (a), (c) for each datum, and Theorem CE (b) for the limits. For (i): S_* >= S_*^1 >= 1/5041; D adds; the gap of a product is the least of the two gaps. For (ii): by Lemma Z3, D_j(L) <= 1024 q'^(2^k)/5041 at the sizes from 2^k l on, so D^(j_i,k_i)(b) -> 0 for every b, and Delta_* <= C(x) D_* = 0 by Theorem CE (a). QED

**Proposition NR (no rigidity on torus data; PROVED).** Let CC be any set of eternal data that is closed under pointwise limits and contains the rescaled data of every family of the engine's class (so every condition that defines CC is "kept"). Then CC contains critical elements: the constants log m. If in addition the photon limit exists (A7 with bounded D; recalled), CC contains it and all its sums with other limits. So the statement "CC contains no critical element" is false for every such CC. A rigidity statement must cut the class by a property that the limits of A_(m,eps), of the photon, and of every product with them do not have.

**Verdicts of the three tests named in the row.**

- **Lemma PT.** The limit class is closed under sums, and the critical elements are absorbing: critical plus bounded is critical (PT-inf (i)). So "a product with a massless factor is a scale-invariant limit too": yes, exactly. What rigidity would have to use that the product lacks: by PT-inf (ii) the limit of (gapped SU(2)) x (photon) is the photon limit, with no trace of SU(2). So no property of the limit torus data can be "the SU(2) part has property P". Rigidity must read an object in which "generated by the SU(2) variables alone" is a kept property. The torus data are not such an object.
- **Proposition NP.** Its model M is K copies of strong-coupling SU(2) times ordered Ising. By PT-inf (ii) its blow-down limit is the constant log 2: the J contracting doublings leave no trace. So a limit argument is not refuted by NP, and it cannot use a finite history either. This agrees with NP's remark 4.
- **Five dimensions.** The construction is the same with five sides. If five-dimensional SU(2) at weak coupling has massless gluons (A17, belief), it has critical elements. A rigidity statement must use the dimension through a kept property; the number of sides is the only place where the limit shows it.

**Result of Task 1.** The compactness step holds (Theorem CE, PROVED). The extracted object lies in a class with theorem-grade no-rigidity models (the constants log m), and the class is closed under products. On torus data the architecture is therefore an exact restatement of the wall (Theorem CR), with one gain in form (no rate). Mark for "rigidity on torus data": FAILS (Proposition NR).

