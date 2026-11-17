lead: Claude Opus 5.5 (lead session), dispatched 2026-11-17
row: 1103

# Exercise: end-points for the bridge to the isotropic window (row 1103)

**Who wrote this file.** Anthropic, Claude Fable 5.2, effort high, a laptop
subagent of the lead session (no subagents of its own; `--subagents 0`,
context-isolated passes by the one writer). Lane commit `061d46c6f`
(branch `claude/ym4d-hard-route`); the lead pulled the checkout to
`a4ebff848` during step 3 (it brought `library/prior/gap-face-alt-read-luna.md`). Exercise skill read at main commit
`8b11ae2bb9` (`docs/ai_methodology/skills/exercise/SKILL.md`), with
`SKILL_FRESHNESS_CHECK.md`, `physics-loop/references/proof-search-governance.md`,
`physics-loop/references/assumption-import-audit.md`, `RULES.md`,
`procedures/research.md` (all in full) and `procedures/check.md` (first 60
lines) at the same commit. Date 2026-11-17.

**Nothing in this file is checked by another model.** Every statement of the
run is `argued`, `guide`, `reading` or `open` (the skill's marks). No mass gap
is claimed.

**Refresher read, replacement.** This is a standalone proof target. The skill
replaces the framework refresher by the target contract `GOAL.md`. The row
keeps `GOAL.md` closed until step 5. So for steps 0-4 the contract is the row
text alone (target, family, wall). `GOAL.md` is opened in step 5.

**What this run did not cover** (kept current; final state):
- **The nine check files were read in part, not in full** (RESULT lines of
  all nine; three passages of two of them). The row asked for full reading.
  Their verdicts were taken from `parts/gap.md` L156-168, read in full.
- Of `parts/gap.md` only L156-168 and L221-275 were read. The other 380
  `gap` files of `library/`, the other rows of `FINISH.md`, `checks/` and
  `library/open-registry.md` were searched by `grep` only. Rows 859, 962,
  998, 1053 and 1063 enter through the grepped lines quoted in step 5.
- Open PR branches and `main` were not searched. So no item is called new;
  the strongest mark is "not found in the lane folder".
- Literature: Durhuus-Fröhlich 1980, Osterwalder-Seiler 1978, Borgs-Seiler
  1983, Fröhlich 1979, Bhanot-Creutz 1981, Fu-Nielsen 1984 and Koma 2010
  were not read (recalled or abstract-level). Fingberg-Heller-Karsch: Table 5
  only, through a fetch tool. The two OpenAI preprints and the Hexagon
  preprint were not read by this run (row 1104's reading is used).
  Cao-Nissim-Sheffield arXiv:2509.04688v2: pages 1-4 read.
- No literature search was made for the mixed-only corner of route F4. Its
  prior art is unknown to this run.
- No blind check of the plain version. No check by another model. The
  passes of step 7 are by one writer and are not independent.
- (F4-KP) is not proved; the entropy bound is not written. The corner
  "$K_4$ minus an edge" was not analysed. Rates of forests other than the
  star were not written out. C2' with one short side was not analysed.
- Two exact enumeration runs (guides). No Monte Carlo. No Lean.

## Plan (eight steps; one step per response)

1. Skill steps 0 and 1: locate the record by file name only, write the open
   and closed lists, state the wall twice.
2. Skill step 2: the inventory, with marks. Nearest models where the target
   is false or true for a known reason. Literature: statements of results only.
3. Skill step 3: reason up from the inventory. Classify the end-points of the
   family. Conclusions C1, C2, ...
4. Skill step 4: the assumptions table in six groups, and the ranking.
5. Skill step 5: open the six named lane files, their check files, the
   `parts/gap.md` entries for rows 1089-1100, `GOAL.md`, and the luna
   literature file if present. Compare. Correct the inventory.
6. Skill step 6: set-aside methods, the blockage in one sentence, the discard
   tests in their valid form, the re-judged verdicts.
7. Skill steps 7 and 8: routes (with one pass from outside the lane's
   vocabulary and one pass that argues the bridge is misframed), kill pass,
   ranking; then real attempts inside the 2-hour test budget.
8. Skill step 9: the report, the strong-word pass, the RESULT line.

## Status block

- S0 locate the record: done. Open and closed lists written; luna file of row 1104 not present yet.
- S1 wall stated twice: done. No blind check (no fresh agent allowed).
- S2 inventory: done. 4 definitions or supplied items, 25 nearest-model items, 3 beliefs; most literature recalled or abstract-level.
- S3 reason up: done. C1-C13 argued: forest faces solved exactly; (i) is free and all cost is in (ii); four properties (ii) must use; exact sum-rule form of (ii) on a star path. Corrected later in place: the sheet face is a proved end-point given N4c (after step 3); C12 and the block-product row (step 5).
- S4 assumptions: done. 32 rows in six groups; first five: A4 Wilson must be reached, A11 a bridge is needed, A12 two comparable halves, A14 gap along the whole path, A2 box quantifier. Inventory corrected after step 3 from the row 1104 reading (N4c, N1b).
- S5 compare with the lane: done. Six primary files, GOAL.md, parts entries and the row 1104 reading read in full; nine check files read in part (RESULT lines and three passages). Most conclusions found again; added: general leaf lemma, 2-core classification, half-density bound, frozen-star rate 0. Lane distinction stiff or floppy end-point adopted.
- S6 discard tests: done. 26 set-aside end-points or end-point proofs listed and re-judged; no lane verdict found wrong; the doubly flat corner (row 1053 6.8) comes back as a named stiff end-point.
- S7 routes: done. C14: the only stiff faces of the Wilson cube are one frozen plane and two opposite frozen planes. C15 and route F4: the mixed-only corner (0, beta, 0), four of six orientations at window coupling, expected provable by a hand contour expansion; not found in the lane folder. Misframing pass: no third stiff face exists; the choice is which of three things to give up.
- S8 attempts: done. Attempt 1: classification (argued). Attempt 2: C15 argued, (F4-KP) named and open, two exact enumeration runs pass as pre-registered (guide). Attempt 3 not run. Nothing moved the wall.
- S9 report: done. RESULT line written.

## Step 0. Locate the record; keep the attack files closed

Done by file name only (`ls`); no lane file was opened.

**Open now** (steps 0-4):
- Row 1103 of `FINISH.md` (the brief): the target, the family, the wall.
- The exercise skill and its reference files at `8b11ae2bb9`.
- Published literature: statements of results only (theorems, no-go results,
  counterexamples).
- Deviation, on purpose: the skill lets a run read the *statements* of the
  lane's checked theorems before step 5. The row closes all of `parts/` and
  `library/`. The row wins. So steps 2-4 use no lane theorem.

**Closed until step 5** (opened in full in step 5, as the row orders):
- `library/gap-bridge-exercise-opus.md` (+ `-check-astra`, `-check-opus`)
- `library/gap-bridge-vectors-max.md` (+ `-check-astra`)
- `library/gap-face-2d-astra.md` (+ `-check-opus`)
- `library/gap-face-stability.md` (+ `-check-astra`, `-check-opus`)
- `library/gap-sheet-field.md` (+ `-check-astra`, `-check-opus`)
- `library/gap-pinu-ev.md` (+ `-check-opus`)
- `parts/gap.md`, entries for rows 1089-1100
- `GOAL.md` (the target contract)
- `library/prior/gap-face-alt-read-luna.md` (row 1104; **not present** at
  2026-11-17 10:44Z in this checkout)

**Closed, and searched by `grep` only in step 5** (not read in full by this
run): the other 380 files of `library/` whose names contain `gap`, the other
69 files of `library/prior/` whose names contain `gap`, `checks/`, the other
rows of `FINISH.md`, `QUEUE_DONE.md`, the four `CHARTER_*.md` files. No
exercise packet exists under `.claude/science/exercises/` in this clone.

**Literature record.** The lane has reading files under `library/prior/`
(names seen: `gap-aniso-read-luna`, `gap-bridge-read-luna`,
`gap-face-stability-read-luna`, `gap-collapse-frame-read-luna`,
`gap-coulomb-frame-read-luna`, `gap-2don-proofs-read-opus`, and others). They
are closed until step 5. For steps 2-4 this run uses its own recall and its
own search, and takes statements of results only.

## Step 1. The wall, stated twice

### Plain version (148 words)

We study a mathematical model of the strong nuclear force on a
four-dimensional grid. The model has a strength dial. We want to prove that,
at the dial settings used in real computer simulations, a disturbance in one
place has an effect far away that dies off at a fixed exponential rate, no
matter how large the grid is. This is what makes the particles of the model
heavy. Today a proof exists only at dial settings far from the ones we need,
and for altered versions of the model that fall apart into simple
lower-dimensional pieces. The plan is a bridge: start at an altered version
where the proof works, then change the model in small steps into the one we
want, and keep the decay rate under control all the way. This exercise asks
which starting versions exist, what each costs, and whether the choice of
start makes the rest of the bridge easier.

No picture is used. No blind check ran (no fresh agent was allowed).

### Precise version

**Objects.** Gauge group $G=SU(2)$ with Haar measure. A periodic box
$\Lambda=\prod_{\mu=1}^4(\mathbb Z/L_\mu\mathbb Z)$. One variable
$U_\ell\in G$ on each link. For a plaquette $p$, $U_p$ is the ordered product
around $p$ and $w(U_p)=\tfrac12\operatorname{tr}U_p\in[-1,1]$. The isotropic
Wilson measure is
$$d\mu_{\Lambda,\beta}=Z^{-1}\exp\Big(\beta\sum_{p}w(U_p)\Big)\prod_\ell dU_\ell .$$
A local observable is a bounded measurable function of the links in a finite
set; it is gauge invariant if it is unchanged by
$U_{xy}\mapsto g_xU_{xy}g_y^{-1}$.

**Target T (row 1103).** For each $\beta\in[2.3,2.6]$ there is $m(\beta)>0$
such that for all gauge-invariant local $A,B$ there is $C_{A,B}<\infty$ with
$$|\langle A\,\tau_xB\rangle_{\Lambda,\beta}-\langle A\rangle\langle\tau_xB\rangle|\le C_{A,B}\,e^{-m(\beta)|x|}$$
for all periodic boxes $\Lambda$ (large enough to hold the supports) and all
translations $x$. The rate $m(\beta)$ does not depend on $\Lambda$.
*Quantifier that the row leaves open:* which boxes. Step 2 (item N9) and
step 4 (A2) show that "all periodic boxes" must mean boxes with every side
at least some $L_0(\beta)$.

**Family $\mathfrak F$ (row 1103).** All lattice gauge theories on
$\mathbb Z^4$ with group $SU(2)$, local and reflection-positive action, with
$\mu_\beta$ as one member. Named members: plane-dependent couplings
$W(\beta_1,\dots,\beta_6)$ (one per plane orientation
$12,13,14,23,24,34$), with the limits $\beta_i\to0$ and $\beta_i\to\infty$;
mixed and improved actions; added gauge-invariant local terms.

**Wall (row 1103, neutral form).** A gap can be proved at some points of
$\mathfrak F$. The window is not such a point. A bridge needs
(i) an end-point $e\in\overline{\mathfrak F}$ with a proved gap, and
(ii) control of the clustering rate along a path in $\mathfrak F$ from $e$ to
$\mu_\beta$, $\beta\in[2.3,2.6]$.

**Question of this row.** (i): which end-points, which proofs of a gap
there, and what each costs. (ii) only as far as the choice of end-point
changes what (ii) must do.

**Allowed premises.** Definitions; theorems with written proofs that can be
formalized in principle. A run may guide or refute; it proves nothing.
**Forbidden weakenings.** A gap only at the end-point; a gap for a box family
that leaves out large boxes with four long sides; a rate that depends on the
volume; a statement for one observable only; numerical evidence in place of
a proof.
**Outcomes that count.** Progress: an end-point with a written gap proof and
an exact statement of what (ii) must then prove. A corrected filter. A
priced wall: an exact open statement to which the wall is equivalent.
Closure of the wall is (i) plus (ii); this row does not ask for it.

**Blind check.** Not run. The plain version is corrected in step 9 if the
run shows it is off.

## Step 2. The inventory: what is known to be true

Sources for this step: the row, recall, and a web search made by this run on
2026-11-17. Reading states are exact: "recalled" means not re-read in this
run. No lane file was used.

Convention: $\beta$ is the SU(2) Wilson coupling, weight
$\exp(\beta\,\tfrac12\operatorname{tr}U_p)$. Papers that write
$N\beta\operatorname{Re}\operatorname{Tr}$ have $\beta_{\rm here}=4\beta_{\rm theirs}$ for $N=2$
(argued here: $2\beta\operatorname{Re}\operatorname{Tr}=4\beta\cdot\tfrac12\operatorname{Tr}$).

### 2a. Definitions and supplied items

| # | Item | Mark | Source | Standing / reading |
|---|---|---|---|---|
| D1 | The model, the target T, the family $\mathfrak F$, the wall. | DEF / SUPPLIED | row 1103; step 1 above | - |
| D2 | Character expansion. $e^{\beta w(U)}=\frac{2I_1(\beta)}{\beta}\sum_{j\in\frac12\mathbb N}(2j+1)\,c_j(\beta)\,\chi_j(U)$ with $c_j(\beta)=I_{2j+1}(\beta)/I_1(\beta)\in(0,1)$, $c_0=1$. | THM | classical (Migdal 1975; Drouffe-Zuber 1983 review) | recalled; elementary. Values computed here (guide): $c_{1/2}=0.479,\ 0.494,\ 0.507,\ 0.520$ at $\beta=2.3,2.4,2.5,2.6$; $c_1(2.5)=0.188$; $c_{1/2}(1/12)=0.021$. |
| D3 | Reflection positivity. The Wilson action with plane-dependent couplings $\beta_{\mu\nu}\ge0$ is reflection positive for reflections in hyperplanes orthogonal to a coordinate axis (through sites, and between sites). So each coordinate direction has a positive self-adjoint transfer matrix. | THM | Osterwalder-Seiler 1978; Seiler, LNP 159 (1982) | recalled. The sources write the isotropic case. The proof uses only that each plaquette term is reflection symmetric with positive coefficient; so it covers plane-dependent couplings (argued here, not written out). Diagonal reflections are lost off the isotropic line. |
| S1 | The bridge: "an end-point with a proved gap, plus control along a path". | SUPPLIED (method) | row 1103 | a chosen method, not part of T |
| S2 | The window $[2.3,2.6]$. | SUPPLIED | row 1103 | the reason for this window is in `GOAL.md`, closed until step 5 |
| S3 | Periodic boxes; Wilson action as the member that must be reached. | SUPPLIED | row 1103 | - |
| S4 | No computer-assisted proof step; a run only guides or refutes. | SUPPLIED (owner rule) | row 1103; dispatch text | obeyed |

### 2b. Nearest models where the target is true or false for a known reason

"T-analog" means the statement of T for that model.

| # | Model and fact | Mark | Source | Standing / reading |
|---|---|---|---|---|
| N1 | **Strong coupling, any compact group, any $d$.** T-analog true for $\beta<\beta_0$ small (convergent cluster expansion; gap and area law). | THM | Osterwalder-Seiler, Ann. Phys. 110 (1978) | recalled; the source writes the proof for the Wilson action. |
| N1a | Explicit ranges. Gap (exponential decay, log-Sobolev) for SU(N) when $\beta_{\rm theirs}<1/(16(d-1))$: for SU(2), $d=4$: $\beta<1/12\approx0.083$. Area law for $\beta_{\rm theirs}<1/(8(d-1))$: $\beta<1/6\approx0.167$. | THM | Shen-Zhu-Zhu, CMP 400 (2023), arXiv:2204.12737; Cao-Nissim-Sheffield, arXiv:2509.04688v2, Thm 1.6 | SZZ: abstract only (through a search tool). CNS: pages 1-4 read (own text extraction). Conversion to $\beta$ argued here. |
| N2 | **Two-dimensional gauge theory, any compact group.** Exactly solvable. With free boundary the plaquette variables are independent, each with density $\propto e^{\beta w}$. T-analog true for every $\beta<\infty$; the string tension is $-\log c_{1/2}(\beta)$. | THM | Migdal 1975; Gross-Witten 1980 | recalled; elementary. Re-proved in general form in step 3 (C2). |
| N3 | **One-dimensional chain** $\prod_t e^{\beta w(V_tV_{t+1}^{-1})}$, any compact group: increments independent; correlations of the spin-$j$ matrix elements decay as $c_j(\beta)^{|t|}$; rate $-\log c_{1/2}(\beta)>0$ for every $\beta<\infty$, and $\to0$ as $\beta\to\infty$ ($c_{1/2}\approx1-\tfrac{3}{2\beta}$). | THM | elementary (Peter-Weyl) | proved in step 3 (C1). |
| N4 | **Two-dimensional O(N) and principal chiral models.** Gap for small $\beta$: THM (high-temperature expansion). $N=2$: no gap at large $\beta$ (Kosterlitz-Thouless phase): THM, Fröhlich-Spencer, CMP 81 (1981). Large $N$ at fixed $\beta$: gap for $N>N_0(\beta)$: THM, Kupiainen, CMP 73 (1980). SU(2) principal chiral = O(4). $N\ge3$, all $\beta$: this run first wrote "**open**" from recall. **Corrected 2026-11-17 after step 3**, from the reading of row 1104: see N4c. | THM | as named | all recalled. |
| N4c | **Two-dimensional O(4), every finite $\beta$** (added after step 3). (1) O(n), $n\ge3$: for every finite $\beta$, every finite subgraph of the square lattice and every bond strengths in $[0,\beta]$, $0\le\langle\sigma_x\cdot\sigma_y\rangle\le Ae^{-m|x-y|}$, no field, no fixed spins. (2) O(4), homogeneous periodic squares: a unique periodic local limit and a full transfer gap $m_{\rm lat}(\beta)\ge c\exp\{-\pi\beta-C\sqrt{(1+\beta)\log(2+\beta)}\}>0$ for every finite $\beta$; for $\beta\ge\beta_0$, $c\sqrt\beta e^{-\pi\beta}\le m_{\rm lat}\le C\sqrt\beta e^{-\pi\beta}$. Its Theorem 3.1 gives uniform mixing for bond strengths $0\le\beta_e\le\beta$ on unpinned tori and free subgraphs. No theorem with external fields, pins, or several coupled copies. | THM (research preprints, September 2026) | OpenAI Math preprints *Exponential decay in two-dimensional classical O(n) models* (Thm 1.1, Cor 1.2) and *Sharp mass bounds for the two-dimensional O(4) model* (Thm 1.1, Cor 1.2, Thm 3.1) | **read by gpt-6-luna (row 1104, `library/prior/gap-face-alt-read-luna.md` section 2), not by this run.** Standing: argued (published by its authors); not checked by the reading or by this run. |
| N1b | **A wider strong-coupling range** (added after step 3). SU(2), $0\le\beta<1/3$: unique gauge-invariant local limit of free-boundary boxes, transfer gap $m\ge-\log(3\beta)$. A larger range ($\beta\le0.345$) in the same paper rests on machine interval certificates and is not usable here (S4). | THM (research preprint) | Bhattacharjee-Bhattacharya-Lockwood-Romanov, hexagonmath 2610.00341v5, Thm 1.1 | read by gpt-6-luna (row 1104 file, section 4), not by this run; unchecked. The same file confirms N1a ($\beta<1/12$ from Shen-Zhu-Zhu Cor 1.6; it prints the assumption once as $1/[16N(d-1)]$ and then uses $1/48$ for $N=2$, $d=4$; the abstract seen by this run says $1/(16(d-1))$). |
| N4b | Numerics and asymptotic freedom say the O(N$\ge$3) gap is positive for all $\beta$. Patrascioiu and Seiler argued the opposite. | BELIEF | Monte Carlo literature; Patrascioiu-Seiler 1990s | recalled. Used in no proof. |
| N5 | **Three-dimensional SU(2) gauge theory.** Gap for all $\beta$: **open** beyond strong coupling; believed true. Three-dimensional U(1) (Villain): gap and confinement for all $\beta$: THM, Göpfert-Mack, CMP 82 (1982). | open / BELIEF / THM | as named | recalled. |
| N6 | **Four-dimensional U(1).** At large $\beta$ there is a massless (Coulomb) phase: T-analog false. | THM | Guth, PRD 21 (1980); Fröhlich-Spencer, CMP 83 (1982) | Guth recalled. FS: abstract seen through a search tool ("transition to a massless (QED) phase"). The papers treat the Villain action. |
| N6b | Wilson U(1) transition at $\beta\approx1.01$. | BELIEF | Monte Carlo | recalled. |
| N7 | **Layered phase.** Anisotropic U(1) in $4+1$ dimensions: for strong coupling across layers and weak coupling inside, each 4D layer is in its Coulomb phase while the layers are confined from each other. | BELIEF | Fu-Nielsen, NPB 236 (1984) (mean field); later Monte Carlo | abstract-level, through secondary sources. No proof known to this run. For non-abelian groups layers of dimension 4 confine, so no layered phase is expected in total dimension 4 or 5 (BELIEF). |
| N8 | **Durhuus-Fröhlich criterion.** Cut $\mathbb Z^d$ into height-1 slabs. With the horizontal links fixed to $A$ (top) and $B$ (bottom), the vertical links form a $(d-1)$-dimensional $\sigma$-model $\mu_{A,B}$ with action $\beta\sum_{(x,y)}\tfrac12\operatorname{tr}(Q_xA_{xy}Q_y^{-1}B_{xy}^{-1})$. If the covariances of matrix elements of $Q_x$, $Q_y^{-1}$ decay exponentially **uniformly in $A,B$**, and $G$ has non-trivial centre, then $d$-dimensional Yang-Mills at that $\beta$ has an area law. | THM | Durhuus-Fröhlich, CMP 75 (1980), Thms 1.2, 1.3 | read only as restated in Cao-Nissim-Sheffield arXiv:2509.04688v2, Thm 2.3 (read). DF80 itself not read (the preprint scan is over the fetch size limit). |
| N8b | For $d=4$, $A=B=1$: $\mu_{1,1}$ is the three-dimensional O(4) model at coupling $\beta$. It has long-range order at large $\beta$. So the hypothesis of N8 is false in $d=4$ at large $\beta$. | THM (order at large $\beta$) / BELIEF (threshold $\beta\approx0.94$) | Fröhlich-Simon-Spencer, CMP 50 (1976); Monte Carlo for the threshold | recalled. |
| N9 | **Finite temperature.** For fixed $N_\tau$ and space dimension $\ge3$, SU(N) lattice gauge theory has a deconfined phase at large $\beta$ and a confined phase at small $\beta$. | THM | Borgs-Seiler, NPB 215 (1983); CMP 91 (1983) | title and summary seen through a search tool; not read. |
| N9b | SU(2) critical couplings: $\beta_c(N_\tau)=1.8800(30),\ 2.1768(30),\ 2.2986(6),\ 2.3726(45),\ 2.4265(30),\ 2.5115(40),\ 2.7395(100)$ for $N_\tau=2,3,4,5,6,8,16$. The transition is continuous, in the 3D Ising class. | BELIEF (numerics) | Fingberg-Heller-Karsch, NPB 392 (1993), Table 5 | table read through a fetch tool's extraction of the ar5iv page; the rest not read. Ising class: recalled (Svetitsky-Yaffe 1982; Engels et al.). |
| N9c | Consequence of N9b: for $N_\tau\in\{5,6,8\}$ (and by interpolation $7,9,10$) the point $\beta_c(N_\tau)$ lies **inside** $[2.3,2.6]$. On boxes $N_\tau\times L^3$, $L\to\infty$, at $\beta=\beta_c(N_\tau)$ the correlation length diverges, and plaquette-plaquette correlations decay by a power law (the plaquette couples to the Ising energy operator). So T is false for box families with one side fixed below about 11. | BELIEF | from N9b | a reading of numerics; used in no proof. |
| N10 | **Mixed action** $\beta_F\tfrac12\operatorname{tr}U_p+\beta_A\tfrac13\operatorname{tr}_{\rm adj}U_p$. First-order lines from the SO(3) transition ($\beta_F=0$, $\beta_A\approx2.5$) and the $\mathbb Z_2$ transition ($\beta_A=\infty$, $\beta_F\approx0.44$) join and run into the plane; the line ends at a critical point; its continuation crosses the Wilson axis as the crossover near $\beta_F\approx2.2$. | BELIEF (numerics) | Bhanot-Creutz, PRD 24 (1981) | described through later papers (search tool); end-point position $\approx(1.5,0.9)$ recalled, not verified. At the end-point the scalar correlation length diverges (BELIEF): T-analog false there. |
| N11 | **$\mathbb Z_2$ gauge theory, $d=4$.** Self-dual; gap at small $\beta$ and at large $\beta$ (THM, convergent expansions); a first-order transition at $\beta=\tfrac12\ln(1+\sqrt2)\approx0.44$ (BELIEF, numerics), where a periodic box holds a mixture and clustering of the plaquette fails. | THM / BELIEF | Wegner 1971; Balian-Drouffe-Itzykson 1975; Creutz-Jacobs-Rebbi 1979 | recalled. |
| N12 | **Comparison with $\mathbb Z_n$.** The SU(n) Wilson loop is bounded by the $\mathbb Z_n$ Wilson loop at a related coupling (write $U=zV$, condition on $V$, use Griffiths inequalities for the $z$). Area law for SU(2) when $\mathbb Z_2$ confines. | THM | Fröhlich, PLB 83 (1979) | recalled; not re-read. It gives nothing above $\beta\approx0.44$. |
| N13 | **SU(2) in $d=5$.** A first-order transition near $\beta\approx1.64$ to a Coulomb phase. T-analog false at window couplings in $d=5$. | BELIEF (numerics) | Creutz, PRL 43 (1979) | recalled. |
| N14 | **Large N.** $d=2$, $N=\infty$: third-order transition (THM, exact solution; Gross-Witten 1980, Wadia 1980). $d=4$: a first-order bulk transition for $N\ge5$ with the Wilson action (BELIEF, numerics). Strong coupling at large $N$: THM (Chatterjee 2019; Jafarov 2016), and the ranges of N1a are uniform in $N$. Nothing at 't Hooft coupling of window size. | THM / BELIEF | as named | recalled. |
| N15 | **SU(2) with a fundamental Higgs field** (frozen length, hopping $\kappa$). Convergent expansion, hence a gap, for $\kappa$ large at any $\beta$, and for $\beta$ small at any $\kappa$; the two regions are connected. The pure gauge theory is $\kappa=0$. | THM | Osterwalder-Seiler 1978; Fradkin-Shenker, PRD 19 (1979) | recalled. At fixed $\beta$ in the window the path $\kappa:\infty\to0$ shows a crossover only (BELIEF, numerics, recalled). |
| N16 | **Strong gap gives area law.** Exponential decay under arbitrary boundary conditions, with non-trivial centre, gives confinement. The usual gap is said not to suffice. | THM | Chatterjee, CMP 385 (2021), arXiv:2006.16229 | abstract-level, through a search tool. |
| N17 | SU(2) in $d\ge4$ as an O(4) $\sigma$-model in a heat bath: fluctuations destroy the long-range order; for U(1) the transition stays. | argued (published) | Koma, PRD 82 (2010), arXiv:0907.1938 | abstract seen; not read. |
| N18 | Anisotropic $(2+1)$-dimensional Yang-Mills as $(1+1)$-dimensional principal chiral models coupled weakly; gap and string tension at small anisotropy coupling, from the exact S-matrix and form factors. | BELIEF for our purpose (not a rigorous proof) | Orland, hep-th/0607013 and sequels | abstract-level, through a search tool. |
| N19 | **Mixing and functional inequalities.** For compact spins and finite range: Dobrushin-Shlosman mixing $\iff$ uniform log-Sobolev inequality. Dobrushin-Shlosman: a condition on one finite box, uniform in boundary conditions, gives decay in all volumes. | THM | Stroock-Zegarlinski, CMP 144/149 (1992); Dobrushin-Shlosman 1985 | recalled. |
| N20 | **Window numerics.** Lowest glueball mass in lattice units about $0.9$ at $\beta=2.4$, $0.7$ at $2.5$, $0.5$ at $2.6$; $\sqrt\sigma a\approx0.27,\ 0.19,\ 0.14$. So the correlation length in the window is 1 to 2 lattice spacings. | BELIEF (numerics) | Michael-Teper 1988 and later | recalled, not verified in this run. |
| N21 | **Stability of a gapped lattice Hamiltonian.** On-site gapped Hamiltonian with unique ground state, plus small relatively bounded local terms: the gap and exponential clustering persist. | THM | Yarotsky, CMP 261 (2006) | recalled. |
| N22 | **Local gauge invariance does not break.** | THM | Elitzur, PRD 12 (1975) | recalled. |
| N23 | **Finite-size criteria for frustration-free Hamiltonians.** If the gap of the patch Hamiltonian on patches of size $n$ exceeds an explicit threshold of order $n^{-2}$ (or $n^{-3/2}$), the infinite system is gapped. A gap gives exponential clustering of the ground state. | THM | Knabe 1988; Gosset-Mozgunov 2016; Lemm-Mozgunov 2019; Hastings-Koma 2006 | recalled. |
| N24 | **Log-Sobolev up to the critical point** for Ising-type models by a renormalisation-flow form of the Bakry-Émery criterion. Uses a quadratic interaction and a covariance bound that comes from ferromagnetic inequalities. | THM | Bauerschmidt-Bodineau 2019; Bauerschmidt-Dagallier 2022 | recalled. |
| N25 | **Action sum rule.** The derivative of a mass with respect to a coupling equals the difference of the action expectation between the state and the vacuum. | THM (finite volume, non-degenerate level: first-order perturbation theory) | Michael, NPB 280 (1987) | recalled; re-derived in step 3 (C9). |

### 2c. Beliefs that the plan may depend on

| # | Item | Mark | Source |
|---|---|---|---|
| B1 | T is true. | BELIEF | Monte Carlo; N20 |
| B2 | For SU(2) in $d=4$ the whole open cube $(0,\infty)^6$ of plane couplings is one phase with a positive gap. | BELIEF | folklore; no source checked in this run |
| B3 | The strong-coupling series in $\beta$ has its nearest singularity at complex $\beta$ with $|\beta|\approx2.2$, linked to N10. | BELIEF | series analyses, recalled |

**Not covered in step 2.** DF80, OS78, Borgs-Seiler, Fröhlich 1979,
Bhanot-Creutz, Fu-Nielsen and Koma were not read; they enter as recalled or
abstract-level. FHK 1993: Table 5 only. The search was short (about 12
queries); it is not a full literature search.

## Step 3. Reason up from the inventory

Only the items of step 2 are used. All statements here are **argued**
(proved by Claude Fable 5.2 in this file, not yet checked), unless marked.
Notation: a *weight* is a positive continuous class function $f$ on $G$
with $\int f=1$; $c_j(f)=\frac1{2j+1}\int f\chi_j$. For the Wilson weight
$c_j=I_{2j+1}(\beta)/I_1(\beta)$ (D2), and $1>c_{1/2}>c_1>\dots>0$.
The six plane orientations are the edges of the complete graph $K_4$ on the
directions $\{1,2,3,4\}$. For a model with plane-dependent weights let
$E$ be the set of orientations whose weight is not constant.

### 3.1 What follows at once

**C1 (chain).** Let $V_0,\dots,V_n\in G$ have density
$\prod_{t<n}f(V_tV_{t+1}^{-1})$ with respect to Haar measure. Then $V_0$ is
Haar distributed, the increments $h_t=V_tV_{t+1}^{-1}$ are independent with
density $f$, and independent of $V_0$. For the spin-$j$ matrix
$D^j$: $\mathbb E\,D^j(V_0V_t^{-1})=c_j(f)^t\,\mathbf 1$.
*Proof.* The map $(V_0,\dots,V_n)\mapsto(V_0,h_0,\dots,h_{n-1})$ is a
bijection of $G^{n+1}$; each step $V_{t+1}\mapsto h_t=V_tV_{t+1}^{-1}$ is an
inversion followed by a left translation, so it preserves Haar measure. The
density becomes $\prod f(h_t)$. For a class function,
$\int f(h)D^j(h)\,dh=c_j(f)\mathbf 1$ (Schur). $\square$ Uses N3, D2.

**C2 (leaf lemma).** Let the box have free boundary in direction $\nu$
(sites $x_\nu\in\{0,\dots,L_\nu\}$); the other directions are free or
periodic. Let the measure be
$Z^{-1}\,\Psi(U')\prod_{p\,\parallel\,\mu\nu}f_p(U_p)\,\prod dU$, where the
$f_p$ are weights (they may differ from plaquette to plaquette) and $\Psi\ge0$
is any integrable function of the links $U'$ that are **not** in direction
$\mu$. (So the $\mu$-links occur in $\mu\nu$-plaquettes only: "$\mu$ is a
leaf".) Then:
(a) the $\mu\nu$-plaquette variables are independent, $U_p$ has density
$f_p$, and they are jointly independent of $U'$;
(b) the law of $U'$ is $\propto\Psi(U')\prod dU'$, the model with the
$\mu\nu$-plaquettes removed.
*Proof.* Fix $U'$. Fix the coordinates other than $x_\nu$ and write
$M_k=U_\mu(x+ke_\nu)$, $a_k=U_\nu(x+e_\mu+ke_\nu)$, $b_k=U_\nu(x+ke_\nu)$,
$k=0,\dots,L_\nu$. The plaquette between levels $k$ and $k+1$ is
$P_k=M_ka_kM_{k+1}^{-1}b_k^{-1}$, so $M_{k+1}=b_k^{-1}P_k^{-1}M_ka_k$. For
fixed $a_k,b_k,M_k$ the map $P_k\mapsto M_{k+1}$ is an inversion and two
translations: Haar preserving. So $\prod_kdM_k=dM_0\prod_kdP_k$ on each
ladder, and different ladders use different $\mu$-links. The density in the
new variables is $\Psi(U')\prod_pf_p(P_p)$. This is a product; it gives (a).
Integrating the $P_p$ and $M_0$ gives the constant 1; this gives (b).
$\square$

**C2' (periodic ladder).** If direction $\nu$ is periodic with length $L$,
the same integration gives, for each ladder, the factor
$1+\sum_{j\ge1/2}\Big(\prod_{k}c_j(f_k)\Big)\chi_j(A)\chi_j(B)$, where
$A,B$ are the two $\nu$-holonomies (Polyakov lines) at the ends of the
ladder. *Proof.* Expand $f_k=\sum_j(2j+1)c_j(f_k)\chi_j$ and use
$\int\chi_j(XM^{-1})\chi_{j'}(MY)\,dM=\delta_{jj'}\chi_j(XY)/(2j+1)$ $L-1$
times, then $\int\chi_j(MAM^{-1}B^{-1})dM=\chi_j(A)\chi_j(B^{-1})/(2j+1)$;
characters of SU(2) are real. $\square$ The factor differs from 1 by at most
$\sum_{j\ge1/2}(2j+1)^2c_j^{L}$. So in a periodic box C2 holds up to a
nearest-neighbour interaction of Polyakov lines of strength
$\lambda\approx c_{1/2}^{L}$. With all sides $\ge L$ and $L\to\infty$ the
total effect is at most $(1+5c_{1/2}^L)^{L^3}-1\to0$. With one side short
it is a real interaction (see C11).

**C3 (forest faces are exactly solvable).** Let $E$ be a forest (no cycle
in the graph on $\{1,2,3,4\}$). Take free boundary conditions. Then all
plaquette variables with orientation in $E$ are independent, with density
their own weight. Links in a direction that lies in no plane of $E$ are
independent Haar.
*Proof.* Induction on $|E|$. A forest with an edge has a leaf $\mu$ with one
neighbour $\nu$. Apply C2 with $\Psi$ the product of all other plaquette
weights (they contain no $\mu$-link). The $\mu\nu$-plaquettes are
independent of everything else, and the rest is the model with
$E\setminus\{\mu\nu\}$, again a forest. $\square$ The lemma is blind to the
group: it holds for every compact group, U(1) included.

**C4 (the star face, with its rate).** Let $E=\{14,24,34\}$ with weight $f$
on these planes (for example Wilson at any $\beta_t<\infty$), free boundary
in direction 4. For gauge-invariant local $A,B$ whose supports are separated
by $T$ steps in direction 4:
$|\langle A;B\rangle|\le\|A\|_2\|B\|_2\,c_{1/2}(f)^{4T}$. If the supports
share no spatial link position, $\langle A;B\rangle=0$. So the T-analog
holds with rate $4(-\log c_{1/2}(\beta_t))$ in direction 4:
$2.94,\ 2.82,\ 2.72,\ 2.61$ at $\beta_t=2.3,2.4,2.5,2.6$ (numbers: guide).
*Proof.* Fix the gauge $U_4=1$ (free boundary in direction 4); $A,B$ do not
change. By C1 and C2 each spatial link $\ell$ carries an independent
stationary chain $U_\ell(t+1)=P^{-1}U_\ell(t)$ with $P\sim f$, started from
Haar. The one-step operator is $K=\bigotimes_\ell K_\ell$, and
$K_\ell D^j=c_j(f)D^j$. By the Markov property
$\langle A;B\rangle=\langle a-\bar a,K^T(b-\bar b)\rangle_{L^2(\rm Haar)}$,
where $a,b$ are conditional expectations on single time slices. They are
invariant under time-independent gauge transformations. A function of the
spatial links that is invariant and orthogonal to the constants lies in the
span of $\bigotimes_\ell D^{j_\ell}$ whose support $\{\ell:j_\ell\ne0\}$ has
no site of degree 1 (at such a site the tensor product holds no invariant).
A graph without degree-1 sites contains a cycle; cycles of the cubic lattice
have at least 4 links. So $K^T$ has norm at most $c_{1/2}^{4T}$ on that
space. If the spatial supports are disjoint, $A$ and $B$ are functions of
independent chains. $\square$ Other forests are handled the same way (not
written out here).

**C5 (the faces at infinity carry no gap, or an open problem).**
(a) $\beta_{14}=\beta_{24}=\beta_{34}=\infty$ (free boundary in 4): in the
gauge $U_4=1$ all time slices are equal. So
$\langle A;\tau_{te_4}A\rangle=\operatorname{Var}A$ for all $t$: rate 0.
T-analog false. *(argued.)*
(b) $\beta_{12}=\beta_{13}=\beta_{23}=\infty$ (free boundary in 1,2,3): the
spatial links are pure gauge; set them to 1. For each layer the links
$U_4(\cdot,t)$ form a three-dimensional O(4) model with couplings
$\beta_{14},\beta_{24},\beta_{34}$. Gauge-invariant observables are the
O(4)-invariant ones. At large coupling the model is ordered (N8b, THM
recalled); invariant observables then decay by a power law (BELIEF,
Goldstone modes). T-analog false there (BELIEF).
(c) $\beta_{12}=\infty$ only (free boundary in 1,2): set $U_1=U_2=1$. On each
12-sheet $U_3$ is a two-dimensional O(4) model with couplings
$\beta_{13},\beta_{23}$, and $U_4$ one with $\beta_{14},\beta_{24}$; the
34-plaquettes couple them. For $\beta_{34}=0$ the gap is exactly the gap of
the two-dimensional O(4) model. *(argued reduction.)* **Corrected after
step 3 (N4c):** that gap is positive at every finite coupling by a
September 2026 preprint (read by luna, not by this run), for homogeneous
periodic squares, and of order $e^{-\pi\beta}$: about $4\cdot10^{-4}$ times a
constant at $\beta=2.5$. So this face is a proved end-point given N4c, with
an exponentially small rate; and the rate tends to 0 only as the sheet
couplings tend to infinity. The first text of this run said "open".
So a face at infinity is either false (a, b) or a proved end-point with a
very small rate that rests on N4c (c). Uses N3, N4c, N8b.

**C6 (classification of the corner models).** Consider models whose
plane couplings are each $0$ or finite. By C2 a leaf orientation can be
integrated out exactly (free boundary); what remains is the *2-core* of the
graph $E$. The graphs on four vertices give:

| $E$ (up to relabelling) | 2-core | What the model is | Gap at window-size couplings |
|---|---|---|---|
| empty; one edge; two edges (adjacent or not); star $K_{1,3}$; path $P_4$ | empty | independent plaquettes (C3) | **proved, all finite couplings** (C3, C4) |
| triangle $\{12,13,23\}$; triangle + pendant edge | triangle | independent three-dimensional gauge theories (plus chains) | **open** (N5) |
| four-cycle $\{12,23,34,41\}$ | itself | a model with planes 13 and 24 missing; its closed surfaces are products of a loop in the 13-plane with a loop in the 24-plane | unknown to this run at step 3; no source found. Taken up in step 7.2 (C15, route F4), there with the relabelling in which planes 12 and 34 are the missing ones |
| $K_4$ minus an edge | itself | contains the triangle model as a sub-face | at least as hard as N5 |
| $K_4$ | itself | the full model | the target |

So the proved corners are exactly the forests. The largest are the spanning
trees: the star (4 choices of hub) and the path $P_4$ (12 choices). There
**three of the six orientations sit at any finite coupling, the other three
at zero**. *(argued; the "unknown" rows are open, not no-go.)*

**C7 (no pattern of switched-off plaquettes does better than half).** Let
$K$ be any set of plaquettes of a periodic box with $V$ sites such that no
non-empty subset of $K$ is a closed surface mod 2. Then $|K|\le3V-3$: at most
half of the $6V$ plaquettes. Spanning-tree faces reach $3V$ up to boundary
terms. *Proof.* The boundaries $\partial p$, $p\in K$, are linearly
independent over $\mathbb Z_2$. So $|K|\le\operatorname{rank}\partial_2
=\dim Z_1-\dim H_1=(4V-(V-1))-4$. $\square$ Closed surfaces are what an
exactly solvable "independent plaquettes" structure must exclude, since a
closed surface carries a non-trivial term of the character expansion. So
position-dependent patterns give no end-point of this kind that is "more
than half way". *(argued.)*

**C8 (block products: a trivial gap with almost all plaquettes on).**
Switch off only the plaquettes that cross the walls of a periodic array of
blocks of side $B$. The measure is a product over blocks. Observables in
different blocks are independent, so the T-analog holds trivially, at every
coupling, with a fraction $O(1/B)$ of the plaquettes switched off. So the
fraction of plaquettes at full coupling does not measure the distance to the
window. *(argued; trivial.)*

### 3.2 The least a solution must contain

A solution is (i) plus (ii). By C3, C4, C8 part (i) is free. So a solution is
a proof of (ii) from a free end-point. What must it use?

**C9 (four properties that (ii) must use).** Each line is a test model where
the end-point is the same kind of free end-point, and the far end fails.
- **(a) The group.** C3 holds for U(1). The isotropic U(1) model is massless
  at large $\beta$ (N6, THM for Villain; at Wilson $\beta=2.5$: BELIEF, N6b).
  So on every path from a forest face to the isotropic point the U(1) gap
  must close. A proof of (ii) that uses only compactness, locality and
  reflection positivity proves a false statement for U(1). It must use that
  the group is non-abelian.
- **(b) The dimension.** C3 holds in every dimension (forests on $d$
  vertices). SU(2) in $d=5$ at window couplings is in a Coulomb phase (N13,
  BELIEF). A proof of (ii) must use $d=4$.
- **(c) Four long sides.** By N9c, on boxes with one periodic side fixed at
  $N_\tau\in\{5,\dots,10\}$ the gap closes at $\beta_c(N_\tau)\in[2.3,2.6]$
  (BELIEF). The end-point statement C4 survives such boxes only up to C2'.
  A proof of (ii) must use that every side is long: at least about 11 at
  $\beta=2.6$, 5 at $\beta=2.3$.
- **(d) The weight.** In the plane of mixed actions there is a critical
  end-point near the Wilson axis (N10, BELIEF). A proof of (ii) that is
  blind to an added adjoint term of size $\beta_A\le1$ proves a false
  statement.
*(argued, given the marks of N6, N9c, N10, N13: (a) rests on a THM for the
Villain action and a BELIEF for Wilson at 2.5; (b), (c), (d) rest on
BELIEFs.)*

### 3.3 The smallest object

**C10.** By C9(c) the smallest region that can carry a proof at $\beta=2.6$
has every side at least about 11 lattice units (BELIEF). The correlation
length there is about 2 (N20). So the difficulty is not a long correlation
length. It is that slabs thinner than about 11 are, at some $\beta$ of the
window, critical. A finite-size criterion that uses a box with a short
periodic side cannot work across the window.

**Toy where the wall bites.** The U(1) star family: the end-point
$\beta_s=0$ has the gap of C4, the isotropic end at large $\beta$ has none
(N6). No computation was needed, so none was run. A second toy: $\mathbb
Z_2$ in $d=4$ on the star path at $\beta_t=2.5$. Both ends have a gap (C4;
N11 at large $\beta$), yet the Wilson loop changes from area law to
perimeter law, so the path crosses a phase boundary (N11; where: not
computed). This shows that (ii), a gap along the whole path, is strictly
stronger than a gap at both ends. *(argued for U(1) given N6; the
$\mathbb Z_2$ toy is a reading, not proved here.)*

### 3.4 Where the result can come from, and how it can fail

**C11 (an exact formula for (ii) on a star path).** Take a periodic spatial
box and the transfer matrix in direction 4,
$T(s)=e^{sW/2}Ke^{sW/2}$, where $K$ comes from the timelike plaquettes at
fixed $\beta_t$ and $W=\sum_{p\ \rm spatial}w(U_p)$ acts by multiplication;
$s=\beta_s$. On gauge-invariant functions $T(s)$ is positive, self-adjoint,
compact, with strictly positive kernel. Let $\lambda_0(s)>\lambda_1(s)$ be
its two largest eigenvalues and $m(s)=\log\lambda_0-\log\lambda_1$ the
rate in direction 4. Where $\lambda_1$ is simple,
$$m'(s)=\langle W\rangle_{\psi_0}-\langle W\rangle_{\psi_1},\qquad
m(\beta)=m(0)-\int_0^\beta\big(\langle W\rangle_{\psi_1}-\langle W\rangle_{\psi_0}\big)ds .$$
*Proof.* $T'(s)=\tfrac12(WT+TW)$, so
$\lambda_i'=\langle\psi_i,T'\psi_i\rangle=\lambda_i\langle\psi_i,W\psi_i\rangle$.
$\square$ (At crossings $m$ is Lipschitz and the formula holds for almost
every $s$ with a suitable eigenvector; not written out.) By C4,
$m(0)=-4\log c_{1/2}(\beta_t)$ up to the terms of C2'. So on the star path
at $\beta_t=\beta$: **T in direction 4 holds if and only if the excess of
the spatial plaquette sum in the first excited state over the vacuum,
integrated over $\beta_s\in[0,\beta]$, stays below $2.72$ (at
$\beta=2.5$), uniformly in the box.** This is the action sum rule (N25).
It is an identity, not a bound: nothing in the inventory bounds the
excess. *(argued, finite volume.)* By lattice symmetry the rate in the
other directions equals $m$ at the isotropic end.

**C12 (path trees give a symmetric family).** Let $P=\{12,23,34\}$ and
$P'=\{13,24,14\}$ (the complement; also a path). The relabelling
$1\to2\to4\to3\to1$ maps $P$ to $P'$ and $P'$ to $P$. So the family
$W(a\text{ on }P,\ b\text{ on }P')$ has the gap proved on both axes
($b=0$ and $a=0$, C3) and is symmetric under $a\leftrightarrow b$; the
isotropic line is the diagonal. For a star, the complement is a triangle,
and the second axis is the open three-dimensional problem (N5).
If a lower bound for the rate were concave along the segment from
$(2\beta,0)$ to $(0,2\beta)$, T would follow at its midpoint. **This fails
for U(1)** (C9a): the U(1) rate is positive at both ends and zero at the
midpoint for large $\beta$. So no group-blind concavity holds. *(argued,
given N6.)*

**Ways T can hold or fail, and whether it is one problem.** The lightest
state is the scalar (N20, BELIEF); it is the channel that becomes critical at
the mixed-action end-point (N10). Along a star path the rate in direction 4
and the rates in directions 1-3 are different functions; only the first
enters C11. (ii) is one problem in the scalar channel of one transfer
matrix; (i) is not a problem.

### 3.5 Make the requirement less wrong

- T needs a statement of which boxes (C10). "All sides $\ge L_0(\beta)$" is
  the form that can be true.
- (ii) asks for a gap along a whole path. T asks for it at one end. The
  $\mathbb Z_2$ toy shows the difference. A method that does not go through
  a path (a criterion at the window point itself) is not excluded by T.
- Who consumes T, and why this window, is in `GOAL.md` (closed here).

### 3.6 Price

**C13.** The row asks for the cost of each end-point. From the inventory:

| End-point | Proof of the gap there | Cost of (i) | What (ii) must then do |
|---|---|---|---|
| E1 isotropic, $\beta<1/12$ | Bakry-Émery (N1a) or cluster expansion (N1) | none (published) | move six orientations from $0.08$ to $2.5$, through the crossover; full lattice symmetry on the path |
| E2 spanning-tree face (star or path), tree couplings at $\beta$ | C3, C4: a page | none | move three orientations from $0$ to $\beta$. Star: one transfer matrix with fixed kinetic part (C11); start rate 2.72 at $\beta=2.5$. Path: symmetric family (C12) |
| E3 a layer around E2 (small complementary couplings) | an expansion around independent plaquettes; not written | a standard but real proof; expected width a few hundredths (guide: $\varepsilon\cdot12\cdot\frac{1+c}{1-c}<1$ gives $\varepsilon<0.03$ at $c=0.5$) | the same as E2 minus a few per cent |
| E4 block product (C8) | trivial | none | switch on the block walls. Convergence up to full strength is a statement of Dobrushin-Shlosman type on one block (N19): a criterion at the window point, not a path |
| E5 triangle face (three-dimensional slices) | needs N5 | **an open problem** | switch on three timelike orientations |
| E6 sheet faces ($\beta_{12}=\infty$, $\beta_{34}=0$, the four mixed orientations at $\beta$) | N4c (corrected after step 3; first written as "an open problem") | none for homogeneous sheets, **given N4c** (a preprint, read by luna, unchecked). Rate of order $e^{-\pi\beta}$: very small. Sheets coupled to each other, or in fields, are not covered by N4c | lower $\beta_{12}$ from infinity to $\beta$ and raise $\beta_{34}$ from 0 to $\beta$: two singular moves, from a start rate near $10^{-3}$ |
| E7 other faces at infinity | - | T-analog false (C5a, C5b) | - |
| E8 Higgs field, large hopping (N15) | published | outside $\mathfrak F$ as the row words it | lower $\kappa$ to 0 through a crossover |

**The exact missing input** is not an end-point. It is a mechanism that
keeps the set of gapped parameters closed along the path: in the form of
C11, a volume-uniform bound on the action excess of the first excited
state. No item of the inventory supplies one. *(reading.)*

### Conclusions of step 3

- **C3/C4/C6** (D2, N2, N3): forest faces are exactly solvable for every
  finite coupling; they are the only proved corners; the star face has rate
  $4(-\log c_{1/2})$.
- **C5** (N3, N4c, N8b): faces at infinity give rate 0 (a, b) or, for the
  sheet face, a rate of order $e^{-\pi\beta}$ that rests on N4c (corrected
  after step 3).
- **C7** (definitions): no acyclic pattern keeps more than half of the
  plaquettes.
- **C8** (definitions): block products have a trivial gap with almost all
  plaquettes on; so "how many couplings are in place" is not the distance.
- **C9** (N6, N9c, N10, N13; mostly BELIEF): (ii) must use the non-abelian
  group, $d=4$, four long sides and the weight.
- **C10** (N9c, N20; BELIEF): the box quantifier of T; the smallest region.
- **C11** (N25, C4): (ii) on a star path is an exact integral condition on
  an action excess.
- **C12** (C3, N6): the path-tree family is symmetric with two solved axes;
  concavity fails for U(1).
- **C13** (all): (i) is free; the whole cost is in (ii); the missing input is
  a closing mechanism.

**Not covered in step 3.** General forests: only the star's rate is written
out. C2' in boxes with one short side: not analysed beyond the size of the
factor. The four-cycle face: no analysis. E3: no proof, only a guide
estimate. No run was made.

## Step 4. The assumptions table

Taken from the row text and from steps 1-3 (the lane files are still
closed; the lane's own discard tests are added in step 6). "Used" names the
place. Columns: needed by the **target**, needed by the **method**, or
**habit**; what follows if wrong or dropped; easier?; check.

### (a) Target

| ID | Assumption | Used | Needed? | If wrong or dropped | Easier? | Check |
|---|---|---|---|---|---|---|
| A1 | T is wanted on the whole interval $[2.3,2.6]$. | row | target (as supplied) | One point would do for some consumers. At $\beta=2.3$ the smallest slab is thinner (C10) and the correlation length shorter. | a little | read the consumer in `GOAL.md` (step 5) |
| A2 | "Uniform in the volume of periodic boxes" means all periodic boxes. | row | habit of wording | False as worded for boxes with one fixed short side (N9c, BELIEF). T must read "all sides $\ge L_0(\beta)$". | it makes T true | cheapest: check the wording in `GOAL.md`; the numbers are N9b |
| A3 | All gauge-invariant local observables, not one. | row | target | With reflection positivity the rate for all observables is the transfer gap on the invariant sector. Dropping it gains nothing. | no | none needed |
| A4 | The isotropic **Wilson** action must be reached. | row | target (as supplied) | If any reflection-positive local SU(2) action will do, T is free (C3, C8). If an action "in the same universality class with correlation length $\ge\xi_0$" will do, the problem is a different one. | yes, drastically | owner / consumer decision; see `GOAL.md` |
| A5 | The rate may depend on $\beta$; no size is asked. | row | target | A required size (for example $m\ge$ a named number) would exclude end-points with rate $e^{-\pi\beta}$ (E6). | - | `GOAL.md` |

### (b) Formulation

| ID | Assumption | Used | Needed? | If wrong or dropped | Easier? | Check |
|---|---|---|---|---|---|---|
| A6 | The family is pure SU(2) gauge theory on $\mathbb Z^4$. | row | method | With matter fields the Higgs end-point E8 enters (N15). With other groups: finite subgroups, U(1) tests. With $d\ne4$: the tests of C9(b). | new end-points, no new closing mechanism | none known |
| A7 | Couplings do not depend on position. | row's examples | habit | Position-dependent patterns are allowed by "local and reflection positive" (reflections through block walls). They give E4 (C8) and are bounded by C7. | new end-point E4 | argued in C7, C8 |
| A8 | Periodic boundary. | row | target (as supplied) | With free boundary C2 is exact and C2' disappears; thermal effects of short periodic sides (C9c) disappear from the end-point, not from the far end. | a little, at the end-point only | - |
| A9 | The reflection planes are the coordinate ones. | D3 | method | Plane-dependent couplings keep a transfer matrix in each coordinate direction but lose diagonal reflections. Nothing in step 3 used the diagonal ones. | no | - |
| A10 | "Rate" is one number. | row | habit | Off the isotropic line the rate depends on the direction (C4: finite in direction 4, infinite across). (ii) needs only one direction at the isotropic end (C11). | yes: follow one transfer matrix | argued in C11 |

### (c) Reduction

| ID | Assumption | Used | Needed? | If wrong or dropped | Easier? | Check |
|---|---|---|---|---|---|---|
| A11 | A proof of T goes over a bridge: end-point plus path. | row (the wall) | **habit / method** | Other shapes exist: a criterion at the window point itself (E4, N19, N23); a map that carries the window to strong coupling (renormalisation). | unknown; it changes what is asked | step 7 routes |
| A12 | The bridge has two comparable halves, and the end-point is the half in question ("second leg"). | row; owner's question | habit | By C13 the end-point half is free. All cost is in the path half. Work on end-points buys nothing unless it comes with a closing mechanism. | it redirects work | argued in C13; compare in step 5 |
| A13 | A good end-point is "close" to the window: many couplings already at window size. | implied by "falls apart into lower-dimensional pieces" | habit | C7: at most half the plaquettes for independent-plaquette end-points. C8: almost all plaquettes with a trivial gap. So closeness in couplings is not the right measure. | - | argued |
| A14 | The gap must be controlled along the whole path. | row (ii) | method | T needs it only at the end. The $\mathbb Z_2$ toy shows a path can fail while both ends hold. | - | - |
| A15 | The path stays at one lattice scale, inside the coupling family. | row | method | A scale-changing map is a different object: its "path" is a sequence of effective actions, not members of $\mathfrak F$ with plaquette terms only. | unknown | step 7 |
| A16 | The end-point's gap is proved by decoupling into lower-dimensional pieces. | row's examples | habit | Other proofs at an end-point: Bakry-Émery (N1a), independence (C8). | - | - |
| A17 | One tool does (ii) for the whole window. | not stated; hidden | habit | The window may need different tools on each side of a slab threshold $\beta_c(N_\tau)$ (C10). | - | none known |
| A18 | The rate changes continuously along the path. | hidden in "control" | method | A first-order transition makes it jump; in periodic boxes the state is then a mixture. For SU(2) none is expected in the open cube (B2, BELIEF). | - | Monte Carlo could look; not a proof |

### (d) Discard tests (this run's own; the lane's follow in step 6)

| ID | Test | Used | Valid form | From which value it binds |
|---|---|---|---|---|
| A19 | "It also holds for U(1)." | C9a, C12 | Refutes a tool whose hypothesis holds for U(1) and whose conclusion (gap at the isotropic point) fails for U(1). | Villain: large $\beta$ (THM, threshold not known to this run). Wilson: $\beta>1.01$ (BELIEF). So in the window it rests on a BELIEF for the Wilson weight. |
| A20 | "It also holds in $d=5$." | C9b | Same form. | $\beta\gtrsim1.64$ (BELIEF). |
| A21 | "It does not use four long sides." | C9c | Refutes a tool that proves a volume-uniform gap for boxes with a fixed side $N_\tau$. | at the single points $\beta_c(N_\tau)$; inside the window for $N_\tau=5..10$ (BELIEF). |
| A22 | "It is blind to an adjoint term." | C9d | Same form. | near the end-point $(\beta_F,\beta_A)\approx(1.5,0.9)$ (BELIEF, position recalled). Off the Wilson axis; it binds only tools that are uniform in $\beta_A\in[0,1]$. |
| A23 | "The end-point's own gap is open" (sheets need two-dimensional O(4)). | this run's first C5(c) | **Now false as a reason** for homogeneous sheets, given N4c. Still valid for coupled sheets or sheets in fields. | - |
| A24 | "It needs a small number" (strong coupling). | E1, E3 | A range only: $\beta<1/12$ (N1a), $<1/3$ (N1b, preprint). | not a refutation |

### (e) Beliefs

| ID | Belief | Plan depends on it? | If wrong |
|---|---|---|---|
| A25 | T is true (B1). | yes | then the wall is a real phase boundary and no bridge exists |
| A26 | The open cube of plane couplings is one phase for SU(2) (B2). | yes, for every path in the cube | a path would have to be chosen around the boundary |
| A27 | N4c is right. | only E6 | E6 returns to "open" |
| A28 | The table N9b and the Ising class. | C9c, C10, A2 | the box quantifier A2 could stay as worded |
| A29 | The scalar channel is the lightest all along the path. | C11 reading | another sector would set the rate |

### (f) Working rules (questioned on paper only; all obeyed)

| ID | Rule | If it were different (not used) |
|---|---|---|
| A30 | No computer-assisted proof step; Lean-formalizable. | A finite-size criterion (E4) would become a finite computation. By C10 its region has side $\ge11$ at $\beta=2.6$ with continuous variables: far beyond any certified computation known to this run. So the rule is not what blocks. |
| A31 | Lane files closed until step 5. | - |
| A32 | No subagents; one numeric job at a time. | - |

### Ranking (by how much the problem changes if the assumption is dropped)

1. **A4** (Wilson must be reached). *Owner decision.* The lane would first
   fix which actions the consumer accepts; with a wide answer, (i) alone
   could serve.
2. **A11** (a bridge is needed). The lane would brief routes that are not
   paths: a criterion at the point, or a scale-changing map.
3. **A12** (two comparable halves). The lane would stop pricing end-points
   and put the budget on closing mechanisms for (ii).
4. **A14** (gap along the whole path). The lane would accept methods that
   prove nothing in the middle.
5. **A2** (box quantifier). *Owner decision on wording.* The lane would
   restate T with all sides $\ge L_0$ and add the slab test A21 to its tests.

Next: A13, A7, A1 (*owner decision*: the window), A30 (*owner rule*; not
the blocker).

**Not covered in step 4.** The lane's own assumption ledgers
(`gap-assume-opus`, `gap-wall-assumptions-opus`, and others, by name) were
not opened; step 5 compares only with the files the row names.

## Step 5. Compare with the earlier work

Files are opened in the order below; notes are appended file by file, then
the comparison table.

### 5.0 Reading notes (working memory)

**`GOAL.md`, read in full.** It is the contract of the existence target
(T0, T1). The mass gap is named there only as a later target. So the
contract for this row stays the row text; the gap contract of the lane is
in `parts/gap.md` ("(SEED) at each beta of the window with a carry", per
row 1072's citation of L24-26). `GOAL.md` repeats the rule S4 in full.

**`parts/gap.md` L156-168 (entries for rows 1072-1100), read in full.**
The lane's frame, which this run did not have in steps 1-4:
- Split $2+2$: couplings $\beta_L$ (plane 12), $\beta_T$ (plane 34),
  $\beta_M$ (the four mixed planes). Anchor: $(\beta_L,\beta_T)=(\infty,0)$,
  a product of two-dimensional O(4) sheets. This is my E6 with
  $\beta_{34}=0$.
- Route BR-2 (row 1072): step (i) a gap on the face $\beta_L=\infty$ at
  $\beta_T=\beta$ ((FACE-SG-T)); step (ii) descent in $\beta_L$ with a rate
  that does not drop ((MON-L)).
- Step (i) was attacked through "sheets": the face is a family of O(4)
  sheets, each in a field set by its neighbours (rows 1077, 1091, 1096,
  1099). It stands at three open inputs: PIN-2 or PIN-U (crossing bounds
  under mixed-sign pins), long clusters in a field, EV. A GUIDE run shows
  swap clusters filling 95-98% of the torus at $\beta=2.3,2.5$.
- Step (ii): counterexamples at GUIDE grade to (MON-L) "at all couplings on
  every box" (row 1085, $\beta_M\ge8.5$); in the window all tested signs are
  positive on small boxes (rows 1089, 1090); the heat-kernel sign turns
  negative near $\beta\approx3.4$-$4.0$ and the crossing moves down with the
  box.
So the owner's "second half" is the proof of a gap at the end-point of the
descent, and "sheets" is the method that stalled there.

**`library/gap-bridge-exercise-opus.md` (row 1072), read in full (506
lines).** Already there, and stronger or earlier than this run:
- Remark RP-ANI = my D3 (argued there with the same one-line proof).
- Lemma CONT and conclusion C5 there ("any carry needs an a priori estimate
  that prevents the gap from closing along the path"; it must read the
  group and the dimension) = my C9(a),(b) and the "missing input" of C13.
  Row 1072 credits exercise 2 (row 878, F5) for the stronger form: the
  general law $-\Delta'\le(2\Delta\sup|E_0''|)^{1/2}$ with a volume factor
  and the missing linear law. My C11 is the first-order (Hellmann-Feynman)
  form of the same object.
- Proposition CA-FAIL there: uniform Dobrushin-Shlosman mixing is false at
  window couplings, because a pinned slab carries an ordered
  three-dimensional O(4) model. This is my N8b turned on N19. **It corrects
  my E4 and A30:** the block-product end-point's closing condition, in the
  form uniform over boundary data, is false, not just unproved.
- The U(1) filter correction there (U(1) binds window-only bridges at
  belief grade) = my A19.
- Its set-aside method 10 ("the $\beta_t$ path from zero temporal coupling",
  method 27 of the lane) is my E5 (triangle face). Its route BR-9 ("path
  from the transverse-lattice point $(\beta,\beta,0)$") is the face
  $\beta_T=0$, which is not a forest (the mixed planes form a four-cycle,
  my C6 row 3, plus $L$).
- Its I13 correction: Dobrushin-Shlosman's read setup is finite spin.
Not found in that file: forest faces as exact end-points (C3, C4, C6);
the half-density bound C7; the thermal test C9(c) and the box quantifier
(C10); the symmetric path-tree family (C12). These get a lane-wide search
below before any mark.

**`library/gap-bridge-vectors-max.md` (row 1076), read in full (499
lines).** What it holds that bears on this run:
- **The reason for the lane's end-point.** BR-2 uses the face
  $\beta_L=\infty$ because the gap there is believed *smaller* than at the
  window. Then the carry needs only a sign ((MON-L): the gap does not drop as
  $\beta_L$ comes down), not a quantitative law. A start whose gap is
  *larger* than the window's needs a volume-free bound on a decrease
  ((LIN-path), (NOCRIT)), which the lane marks blocked-stronger (row 878's
  missing linear law). My step 3 did not have this distinction. It sorts all
  end-points of C13 into two kinds: **stiff** (rate below the window's; carry
  = a sign) and **floppy** (rate above; carry = a bound on a decrease).
  E1-E5 are floppy. E6 is stiff.
- Lemma KIN: the transfer operator in a longitudinal direction is
  $S^*D(\beta_L)S$ with $D=e^{-tN}$ (heat-kernel form), $N$ a sum of
  Casimirs. Identity KIN-5: $dm/dt=n_1-n_0$. This is the same
  Hellmann-Feynman identity as my C11, for the kinetic coupling, where the
  varied operator is non-negative. My C11 varies the magnetic term, which
  has no sign. KIN-5 is the better form.
- Lemma SWAP (free energy convex and symmetric under exchange of the two
  pairs of directions; "the gap is also symmetric on that segment, but it is
  a difference of two convex functions"). This is the lane's form of my C12
  remark; mine uses the path-tree family, the conclusion is the same: no
  bound for the gap.
- VB-12 "the plane $\beta_M=0$ as a start" (idea 23 of
  `gap-brainstorm2-max.md`): a product of exactly solved two-dimensional
  Yang-Mills planes, group-blind. This is my forest $\{12,34\}$ (two of six
  orientations). Its carry is (NOCRIT) in $\beta_M$.
- VB-8 (Higgs path) = my E8; VB-9 (mixed action as a path); VB-11
  (couplings on a sublattice: checkerboard models GH2, P4) is a
  position-dependent pattern (my A7), used as start data.
- VB-15 "other endpoints: no vector"; VB-16: in the split $2+2$ every link
  is a spin of a two-dimensional sheet; "k = 2 is the only split where the
  group decides" (row 1053 L245).
- Example KIN-7: (MON-L) is false for frozen $Q_8$ on a small box; so a
  proof of the sign must use that the group is continuous.
Not in that file: spanning-tree faces (star, path) as exact starts with
three orientations at window size (they need different couplings inside the
four mixed planes, outside the lane's three-coupling family); the bound C7;
a list of all faces at infinity; finite-temperature points as a test.

**`library/gap-face-2d-astra.md` (row 1077), `library/gap-face-stability.md`
(row 1091), `library/gap-sheet-field.md` (row 1096),
`library/gap-pinu-ev.md` (row 1099): each read in full.** They are the
"sheets" attack on step (i) of BR-2, the face at $\beta_T>0$:
- Row 1077: the face on a transverse torus is a two-dimensional system with
  spin space $SU(2)^{E_T}$ and a $G_T$-invariant on-site potential; the Ward
  step ports for the residual group only; the independent-sheet port fails at
  (9); the association step fails at (12); the perturbative interval uniform
  in the transverse size is $\{0\}$ (15); a gap alone gives no stability
  (Ising example (16)).
- Row 1091: M1 (each sheet is an O(4) model in a field of norm $\le2\lambda$
  set by six neighbours); Theorem FST-BD (block criterion); the face bound
  (17) GIVEN FST-F, FST-P or FST-T, all open; counterexamples G1, G2 to
  single steps.
- Row 1096: FST-F1 suffices; Pei's transfer survives as Lemma RN/MK; the
  pinning monotonicity fails in a field (P1); Proposition SS (sign part);
  open inputs PIN-U and EV; model 5.4 (PIN-U without EV).
- Row 1099: PIN-U replaced by PIN-2; Lemma LS (one-signed layers); Lemma W
  (wall monotonicity fails); Lemma BF (block fields); EV-split; Proposition
  SW with a GUIDE run where swap clusters fill the torus.
None of these files proposes another end-point. They bear on this run in one
way: they show what the end-point (i) of BR-2 costs. Its last open inputs
(PIN-2 or PIN-U for sign changes along a layer; long clusters in a field;
EV) have no counterexample and no proof.

**The nine check files.** Read in part, not in full: the RESULT line of each
(all nine), and in `gap-bridge-exercise-check-astra.md` L171-192 (the
correction of RP-ANI) and in `gap-bridge-vectors-check-astra.md` L554-566,
L587-595 (the VB table and the correction of the gap symmetry). The verdicts
of all nine are also in `parts/gap.md` L156-168, read in full. **This is
less than the row asked** ("open in full ... their check files"). Reason:
the nine files hold 362 kB, and this run kept its reading budget for the six
primary files (349 kB, all read in full) and the literature file.
Corrections taken from the checks:
- Check 1074 (astra): positivity of the transfer operators does not by
  itself identify an infinite-volume clustering rate with a gap on a finite
  torus; at a zero coupling the transfer operator can have a kernel. My D3
  and C11 are read with this limit (C11 is a finite-box identity with all
  couplings positive on the path, $s>0$; at $s=0$ the operator $K$ alone is
  injective for $\beta_t>0$).
- Check 1075 (opus): the Fröhlich-Simon-Spencer sufficient threshold for the
  three-dimensional O(4) model is $2W_3=1.0109$ in the normalization
  $\beta\,s\cdot s'$, below 2.3 by a hand bound. My N8b gave "about 0.94"
  (the Monte Carlo critical point, recalled); the theorem-grade number is
  1.0109.
- Check 1079 (astra): the exchange of the two pairs of directions also
  changes the transfer direction, so "the fixed-direction gap is symmetric"
  fails. **This corrects my C12:** the relabelling
  $1\to2\to4\to3\to1$ maps the rate in direction $\mu$ at $(a,b)$ to the
  rate in direction $\sigma(\mu)$ at $(b,a)$. Only a direction-symmetric
  quantity (for example the smallest rate over the four directions) is
  symmetric under $a\leftrightarrow b$. The U(1) remark of C12 stands.

**`library/prior/gap-face-alt-read-luna.md` (row 1104), read in full**
(after step 3; see N4c, N1b). Its other findings: no rigorous theorem for a
gapped layered or dimensionally reduced phase of four-dimensional SU(2), nor
a monotone gap along a path to the isotropic point; Fu-Nielsen is mean
field, for U(1), $D\ge5$; Del Debbio, Kenway, Lambrou and Rinaldi (2013):
five-dimensional anisotropic SU(2), a first-order transition, Monte Carlo;
no proved monotonicity of a non-abelian mass gap in a plane coupling; no
rigorous gap for the Kogut-Susskind Hamiltonian at window coupling;
Fradkin-Shenker is analyticity, not a quantitative gap.

### 5.1 Item by item

Search scope for every "not found": `grep -rliE` over all `*.md` files of
the lane folder at `a4ebff848` (`library/`, `library/prior/`, `parts/`,
`checks/`, `gates/`, `FINISH.md`, `GOAL.md`), with the patterns named. Open
PR branches and `main` were **not** searched. So the strongest mark is "not
found in the lane folder".

| Item of this run | In the earlier work? | Where | Patterns for a "not found" |
|---|---|---|---|
| D3 reflection positivity with plane couplings | **yes** | Remark RP-ANI, row 1072 (as corrected by check 1074) | - |
| C1 chain | **yes** | row 859 idea 32 (`gap-brainstorm-max.md` L317: "independent link chains, explicit gap and string tension") | - |
| C2 leaf lemma, general form (any weight, any rest $\Psi$) | **partly**: special cases | Lemma FACE-LIM's comb forest (row 1053); Lemma FACE-PROD (row 1085); row 962 A2 | "leaf" (147 files, other senses), "independent plaquettes", "plaquette variables are independent": no general statement |
| C3 forest faces solved | **partly** | star: row 859 idea 32, row 962 A2 ("the solvable line $\beta_s=0$"), row 1053 L245 ($k=1$). Two opposite planes: idea 23 of `gap-brainstorm2-max.md`, VB-12 of row 1076. Path tree $\{12,23,34\}$: not found | "path tree", "12, 23, 34", "{12,23,34}", "three (plane) orientations", "six couplings", "plane-dependent": 0 relevant hits |
| C4 star rate $4(-\log c_{1/2})$ | **yes** | `gap-crux-skeleton-check-astra.md` L383 ("its normalized electric spectrum does give the exact beta_s=0 gap") | - |
| C5(b),(c) frozen triangle = ordered 3D O(4); frozen plane = sheets | **yes** | row 1053 L177 ("why more freezing does not help"), L245 ("k = 2 is the only split where the group decides"); Lemma ANCH; Lemma SLAB (row 1013); CA-FAIL | - |
| C5(a) frozen star has rate 0 | not found as a statement (row 1053 L245 says for $k=1$ "nothing to freeze") | - | "static", "frozen pair", "adjacent (frozen) planes", "two frozen planes": no relevant hit |
| C6 classification of the corners by 2-core (triangle, four-cycle, $K_4$ minus an edge) | not found in the lane folder | - | "four-cycle", "4-cycle", "Clifford", "K_{2,2}", "2-core": no relevant hit |
| C7 no acyclic pattern keeps more than half of the plaquettes | not found in the lane folder | - | "half (of) the plaquettes", "rank of the boundary", "linearly independent boundaries", "closed surface mod 2": 0 hits |
| C8 block products | **partly** | VB-11 (couplings on a sublattice, row 1076); route RC and Theorem S (`parts/gap.md`); and CA-FAIL shows the uniform closing condition is false | - |
| C9(a),(b) group and dimension must be read | **yes**, stronger | rows 1053, 1066, 1072 (C5), with the corrected range of the U(1) test (theorem grade only at Villain $\beta\ge2^{14}$) | - |
| C9(c), C10 four long sides; box quantifier | **yes** in substance | row 1063, `gap-measured-assumptions-opus.md` L115 (L3), L316 (b6: "periodic boxes of side < 1/(T_c a) are deconfined"), L332 (c6: "Use boxes >= 4 (beta 2.3), >= 8 (2.5), >= 14 (2.7)") | the sharper form "T is false at $\beta_c(N_\tau)$ for a fixed side $N_\tau=5..10$" was not found stated |
| C9(d) mixed-action end-point as a test | **yes** | K7 line and end point in the test table of `parts/gap.md`; VB-9 | - |
| C11 Hellmann-Feynman form of (ii) | **yes**, earlier and better | item 46 of `gap-brainstorm-max.md` L445; `gap-measured-vectors-max.md` L141, L277 ((SUM-RULE), with measured slopes 2.4 to 3.5); Identity KIN-5 (row 1076) in kinetic form | - |
| C12 symmetric family; no group-blind concavity | **partly** | Lemma SWAP and VB-4, VB-6 (row 1076), for the $2+2$ family; the path-tree family not found | corrected above (check 1079) |
| C13 (i) is free, the cost is in (ii); the missing input is a closing mechanism | **yes** | row 1072 C4, C5, C9 and 8.1 ("the road itself is easy to draw; what is missing is a rule that stops the property from being lost"); row 878 F5 | - |
| A11 a bridge is a habit | **yes** | row 1072 C-1 | - |
| A12 two comparable halves | **yes** in substance | row 1072 8.2 item 1 | - |
| A14 gap along the whole path is more than T | **yes** | BR-3 "blocked-stronger" (row 1072) | - |
| A4 Wilson must be reached | **partly** | row 1072 A2, B1; VB-14, VB-15 | - |
| A2 box quantifier | **yes** | row 1063 b6, c6 | - |

### 5.2 Where the earlier work is right and this run was wrong or weaker

1. **Stiff and floppy end-points** (rows 1072, 1076; credit: Claude Opus
   5.5 and Claude Fable 5.2 there). My C13 priced end-points only by the
   cost of (i). The lane's point is that the *side* decides what (ii) is: a
   sign from a stiff end-point, a bound on a decrease from a floppy one. I
   use it from here on.
2. **Block products** (E4, A30): corrected by Proposition CA-FAIL.
3. **N8b threshold**; **N19 setting** (Dobrushin-Shlosman as read by row
   1073 is for finite spin spaces); **C12** (direction).
4. **U(1) range** (A19): theorem grade only where a Villain theorem
   applies ($\beta\ge2^{14}$ in the lane's reading); belief grade in the
   window. Same as my A19, with the number.
5. **N4** ("open") was wrong; corrected from row 1104 (N4c). The lane had
   this since rows 1007, 1009, 1070.

### 5.3 What the fresh pass added, and what it only found again

**Added** (not found in the lane folder; PR branches not searched; all
argued, unchecked):
- the leaf lemma C2 in general form, with the periodic factor C2';
- the classification C6 of all corners with couplings in $\{0\}\cup(0,\infty)$
  by the 2-core, with the path trees as exact faces and the four-cycle and
  $K_4$-minus-an-edge faces named as unknown;
- the bound C7 (independent-plaquette patterns keep at most half of the
  plaquettes);
- the exact statement that a frozen star has rate 0 (C5a). Step 7 extends
  it to every pair of frozen planes that share a direction (C14).

**Found again:** reflection positivity off the diagonal; the star face and
its rate; the product of two-dimensional planes; the triangle face
(method 27); sheets at a frozen plane; the group, dimension, box-size and
mixed-action tests; the Hellmann-Feynman price; the continuity frame and the
missing closing estimate; "a bridge is a habit".

## Step 6. The blockage: discard tests and set-aside methods

Scope. This row is about end-points. So 6a lists every end-point, and every
way of proving a gap at an end-point, that the files of step 5 set aside or
stopped. It does not list the lane's other set-aside methods: row 1072 6a
(18 bridge methods) and row 998 6d re-judged those, and this run did not
read row 998. Each row was read first-hand in the file named, except where
"digest" is written.

### 6a. End-points and end-point proofs that were set aside or stopped

| # | Method (authors as the lane credits them) | Reason given | Where | Kind |
|---|---|---|---|---|
| 1 | Start at isotropic strong coupling (Osterwalder-Seiler) | the carry must read group and dimension; "the anchor is the better start" | row 1072 C-2, 3.3 | open premise (carry) |
| 2 | Star face $\beta_s=0$, continue in $\beta_s$ (idea 32 of row 859; row 962 A2) | "stops at (VAC-SUB)"; the engine "is lost in its present form" | `gap-constraints-max.md` L130, L288 (digest: seen by grep, file not read) | open premise |
| 3 | Triangle face $\beta_t=0$, path in $\beta_t$ (method 27; rows 988, 992) | needs three-dimensional mixing and (NOCRIT) | row 1072 6a #10 (digest) | open premise |
| 4 | Plane $\beta_M=0$ (idea 23 of `gap-brainstorm2-max.md`; VB-12) | group-blind start; carry is (NOCRIT) in $\beta_M$ | row 1076 VB-12 | open premise |
| 5 | Transverse-lattice point $(\beta,\beta,0)$ as a start (BR-9) | "dead for now: worse start than R_eps"; check 1074: "no supplied start estimate", not a refutation | row 1072 7.2 | open premise |
| 6 | Fundamental Higgs path (Fradkin-Shenker; VB-8) | group-blind start; half-plane Lee-Yang form false (LYP, LYP2) | row 1076 VB-8 | fails a test (one form) / open premise |
| 7 | Mixed action from $\beta_A=\infty$ (frozen $\mathbb Z_2$; VB-9) | the start reads only the centre; K7 line near the path | row 1076 VB-9 | open premise (ARGUED there) |
| 8 | Fifth direction of locked layers (VB-10) | contains the target at its end; no selective step | row 1076 VB-10 | circular |
| 9 | Geometry path, thin twisted torus (Tanizaki-Ünsal; VB-13) | found, not redone | row 1076 VB-13 | other |
| 10 | Other end-points: tail of cutoffs, a coupling below the window, anisotropic end-point (VB-14, VB-15) | stronger, or no vector | row 1076 | circular / other |
| 11 | Doubly flat corner $\beta_L=\beta_T=\infty$ (row 1053 6.8) | "not used"; carries no flux in the frozen planes; U(1) version massless | `gap-wall-vectors-max.md` L296-298 | other setting (judged for the flux device) |
| 12 | More freezing, $k=3$ flats (row 1053 L177) | three-dimensional O(4) layers order | `gap-wall-vectors-max.md` L177, L245 | fails a test |
| 13 | Block or finite-size criterion at the window (route RC; BR-4) | uniform form false (CA-FAIL); constant-coupling form needs a hand bound in the band | row 1072 6c, 7.2 | fails a test (uniform form) / needs a small number |
| 14 | Couplings on a sublattice (VB-11; GH2, P4) | test-bed and start data; no carry | row 1076 | open premise |
| 15 | Three dimensions first (VB-18) | no consumer for the target | row 1076 | other |
| 16 | Durhuus-Fröhlich layers | "$\beta_T$ acts as an external field on a sheet" | row 1072 6a #8 (digest of row 1053 L199) | other setting |
| 17 | Chessboard estimate in the transverse directions | the chessboard norm is a four-dimensional expectation | row 1072 6a #9 (digest) | circular |
| 18 | Face gap by bounded perturbation of the anchor | common interval is $\{0\}$ (15) | row 1077 4.1 | needs a small number (range $\{0\}$) |
| 19 | Face gap by the independent-sheet Ward step | fails at OpenAI (3.6): on-site term (9) | row 1077 3.2 | other setting |
| 20 | Face gap by association (Ginibre, FKG, amplitude association) | fails for a sheet in fields of several directions: (12), G1, G2, A1 | rows 1077, 1091, 1096 | other setting (step counterexamples at small coupling) |
| 21 | Face gap from one pinned square (FST-P), one sheet in a field (FST-F, FST-F1), tree cumulants (FST-T) | each is an open hypothesis | rows 1091, 1096 | open premise |
| 22 | Pei's transfer with pinning monotonicity | monotonicity fails in a field against the pole (P1) | row 1096 | other setting |
| 23 | PIN-U from OpenAI (3.61), from Ding-Huang-Yang, from wall monotonicity | (3.61) bounds a difference, PIN-U needs the sum; boundary class differs; Lemma W | rows 1096, 1099 | open premise / wrong quantity |
| 24 | EV by Section 3.11, by coarse orientations, by induction on $n$, by differentiation in the field, from free boundaries to all pins | each stops at a named step | row 1096 5.3; row 1099 step 6 | open premise / needs a small number (the last: needs $c/(2\Xi)>16\beta$) |
| 25 | Two-replica swap clusters (Proposition SW) | GUIDE run: swap clusters fill the torus at $\beta=2.3,2.5$ | row 1099 | unverified (a run) |
| 26 | Descent sign (MON-L) by operator order, frustration-freeness, convexity (KIN-1 to KIN-CVX) | each gives no sign for the gap; false for frozen $Q_8$ on a box | row 1076 6.1, 6.4 | wrong quantity / fails a test (class) |

### 6b. First principles on the blockage

What must an end-point tool do? It must supply a point of
$\overline{\mathfrak F}$ with a written gap proof, such that the carry from
it is a statement someone can attack. From the definitions there are two
kinds (step 5, 5.2 item 1). A floppy end-point has a larger rate than the
window; its carry must bound a decrease. A stiff end-point has a smaller
rate; its carry can be a sign. Which statements can serve at all? For a
floppy end-point: independence (C3) or a convergent expansion. For a stiff
one: a frozen plane orientation (step 7, C14, shows that this is forced
inside the Wilson cube). The least property a stiff end-point proof must
use: the non-abelian sheet gap (N4c), which U(1) lacks (N4).

**The blockage in one sentence:** every free end-point of the Wilson cube is
floppy, and every stiff one is a system of two-dimensional sheets that are
coupled by an on-site term which breaks each sheet's own symmetry.

### 6c. The tests, in their valid form, for end-point tools

Here a tool is "gap at the end-point $E$" plus "carry from $E$" $\Rightarrow$
T. The lane's test table (`parts/gap.md` L221-262, from row 998) was read
for this step. The rows that bear on end-points:

| Test (model M') | Class K | Exact T that fails in M' | How known | What a tool must use | Binds from |
|---|---|---|---|---|---|
| Compact U(1) | reflection-positive gauge models | gap at the isotropic point | THM for Villain at $\beta\ge2^{14}$ (lane, row 786, per row 998); BELIEF at window couplings | floppy end-points (C3 holds for U(1)): the carry must read the group. Stiff end-points: the end-point proof reads it (the sheet gap); then the carry's proof must use that datum | theorem grade only for path classes that reach $\beta\ge2^{14}$ |
| Five dimensions | same | gap at weak isotropic coupling | BELIEF (numerics) | no end-point of the cube reads the dimension: forests, the anchor and the doubly flat corner exist verbatim for $d=5$ (argued here). So the carry must read it | belief |
| Frozen $Q_8$, $2T$ | same | (MON-L) on a small box (KIN-7, PROVED in a limit there); singlet clustering on the frozen face (row 1077 5.3) | lane | a proof of a descent sign must use that the group is continuous | boxes; frozen limit |
| Slab device (Lemma SLAB, CA-FAIL) | any gauge group | mixing uniform over all pins | THM given Fröhlich-Simon-Spencer (threshold $1.0109<2.3$) | end-point proofs by block criteria must avoid pins that cut out three-dimensional slabs; on a face with one frozen plane, pins in $u$ cut out two-dimensional systems only | every window coupling |
| Short periodic side (this run's C9c; lane: row 1063 b6, c6) | SU(2) on boxes | T at $\beta_c(N_\tau)$ for a fixed side $N_\tau$ | BELIEF (numerics, N9b) | a box family with all sides long | $N_\tau\le10$ in the window |
| K7 line, $w_p$ (Proposition V) | positive-character weights | gap at one coupling | THM for $w_p$ (van Enter-Shlosman, per the lane); BELIEF for K7 | binds paths in the mixed-action plane (6a #7) | one point |
| Model 5.4 of row 1096 | spin models with coordinate reflections | EV | THM given Peierls | a proof of the face gap must use O(4) in the even sector | - |
| Adjacent frozen planes (this run, C14) | Wilson plane couplings | positive rate in the shared direction | argued (exact) | at most one frozen plane, or two opposite ones | all couplings |

A pass is no support. Are the tests enough? No test on file is a model in
the SU(2) class where a stiff face is gapped and the window is not. None is
believed to exist. So for sign carries the lane has constraints (U(1),
$d=5$, $Q_8$) and no refutation device; the same remark as point 5 of the
lane's table.

### 6d. Verdicts re-judged

| # | The verdict assumes | Valid? | What comes back |
|---|---|---|---|
| 1 | a floppy start; carry blind | valid as reported (as corrected by checks 1074, 1075) | - |
| 2 | the carry is the open part | valid as reported; not re-derived (row 962 not read) | - |
| 3 | $1+3$ split | valid in range: the start needs the open three-dimensional gap (N5) | - |
| 4 | carry in $\beta_M$ | valid. By C3 the start widens for free to a path tree (planes $L$, $T$ and one mixed orientation at any coupling); the carry is unchanged | nothing on the path of T |
| 5 | no start estimate | valid as corrected by check 1074. Step 7 (route F4) supplies an estimate for the far end $\beta_L=0$ of the same leg, not for $(\beta,\beta,0)$ | - |
| 6, 7, 8, 9, 10 | as stated there | valid as reported; not re-derived | - |
| 11 | judged for the flux device and marked "not used" | **moot for this row's question.** The remark is not a discard for a sign carry to T. By C14 the doubly flat corner is the only other stiff face of the Wilson cube. Its cost is the singlet-sector mixing (SING) of rows 1053, 1076 | it comes back as a named end-point (route S2), with the lane's own obstacle |
| 12 | one device ($k$-flats) | valid, and made exact: two frozen planes that share a direction give rate 0 in that direction (C14) | - |
| 13 | uniform over pins | valid (CA-FAIL) | - |
| 14, 15 | no carry; no consumer | valid | - |
| 16, 17 | as reported | valid as reported; not re-derived | - |
| 18 | norm perturbation | valid; sharp (check 1078) | - |
| 19, 20, 22 | steps of one proof | valid as step failures (checked by rows 1078, 1093, 1094, 1097, 1098); they refute no statement about the sheet | - |
| 21, 23, 24 | open hypotheses | valid: open, not refuted | - |
| 25 | a GUIDE run | valid only as a guide (check 1100) | - |
| 26 | class-level | valid; (MON-L) itself open | - |

No verdict of the lane on an end-point was found wrong or too strong.
One was found moot for this row's question (#11). The corrected filters of
this exercise are its own (step 5, 5.2).

## Step 7. Routes: generate, try to kill, rank

`proof-search-governance.md` was read before this step (target contract:
step 1; registry: 7.5). Passes are context-isolated passes by the one
writer; they are not independent. Literature: the record of step 2 and the
row 1104 reading; no new search was needed for the routes below except the
lane greps of step 5.

### 7.1 Pass A (drop "the stiff end-point is the lane's face"): all stiff faces of the Wilson cube

**C14 (stiff faces; argued, exact except the triangle case).** Take plane
couplings in $(0,\infty]$, none zero, free boundary. Let $F$ be the set of
frozen orientations ($\beta=\infty$).
(a) If $F$ contains two orientations $\mu\nu$, $\mu\rho$ that share the
direction $\mu$, and $\nu\rho\notin F$, then the $\nu\rho$-plaquette $A$ has
$\langle A;\tau_{te_\mu}A\rangle=\operatorname{Var}A>0$ for all $t$: the
rate in direction $\mu$ is 0.
(b) Every $F$ with $|F|\ge3$, and every $F$ of two orientations that share a
direction, falls under (a), except $F$ = a triangle $\{\mu\nu,\mu\rho,\nu\rho\}$,
which is the three-dimensional O(4) model per layer (C5b: ordered above
$1.0109$, THM given Fröhlich-Simon-Spencer; rate 0 for invariant observables:
BELIEF), and $F$ = all six (a trivial model).
(c) So the only frozen sets that can carry a positive rate in every
direction are: **one orientation** (the lane's face) and **two opposite
orientations** $\{12,34\}$ (the doubly flat corner of row 1053 6.8).
*Proof.* (a) Fix the gauge $U_\mu=1$ (free boundary in direction $\mu$).
Flatness of the $\mu\nu$-plaquettes gives $U_\nu(x)=U_\nu(x+e_\mu)$, and the
same for $U_\rho$. The $\nu\rho$-plaquette is a function of $U_\nu,U_\rho$
only, so it does not depend on $x_\mu$; it is gauge invariant, so this holds
in every gauge. Its coupling is finite, so its law has a density and it is
not constant. (b) A graph on four vertices with three edges has two edges
at a common vertex. Check each graph: for the star, path, four-cycle,
triangle with a pendant edge, $K_4$ minus an edge and their supersets below
$K_4$, some pair of frozen edges at a common vertex has its third side not
frozen; only the triangle has all three sides frozen. (c) What is left is
$|F|\le1$ and the two opposite edges. $\square$
Faces with some couplings zero add nothing stiff: a zero only removes
terms. The proved stiff points are then: one frozen plane with the two
sheet families decoupled ($\beta_{34}=0$: the anchor, given N4c), or with
direction 4 a leaf (C2: the three-dimensional face of VB-18 with free
chains attached; given N4c).

**Route S1.** The lane's face $(\infty,\beta,\beta)$. Found. Cost: the open
inputs of rows 1096, 1099.
**Route S2.** The doubly flat corner $(\infty,\beta,\infty)$ as end-point,
then two unfreezing descents. Found as a remark (row 1053 6.8). Cost: a
port of the two-dimensional mixing proof to a $\sigma$-model with target
$SU(2)^{V_T}/SU(2)$, including its singlet sector (the lane's (SING)).

### 7.2 Pass B (outside the lane's vocabulary: the topology of the plaquette complex)

Lens: the set $K$ of plaquettes with non-zero coupling is a 2-complex.
Object that changes: $K$. Invariant: its closed surfaces mod 2 (the second
homology with every local coefficient system), which are exactly the terms
of the character expansion. Toy: forests (no closed surface; C3). What
would falsify the lens: a complex without closed surfaces whose model is
not a product of independent plaquettes (none: C2 covers collapsible
complexes; for non-collapsible acyclic ones this run has no statement).
Returns:

- C6 (the corners by 2-core) and C7 (at most half of the plaquettes
  without closed surfaces). Done in step 3.
- **C15 (the closed surfaces of the mixed-only corner).** Let
  $A=\mathbb Z^2$ (directions 1,2) and $B=\mathbb Z^2$ (directions 3,4). A
  mixed plaquette is $e\times f$ with $e$ an edge of $A$ and $f$ an edge of
  $B$. A finite set $S$ of mixed plaquettes is closed mod 2 if and only if
  $S=\sum_{(P,Q)\in T}\partial P\otimes\partial Q$ for a finite set $T$ of
  pairs of unit squares ($P$ in $A$, $Q$ in $B$), and $T$ is unique. So
  closed mixed surfaces correspond one to one to finite sets of unit
  hypercubes. With $\varphi(P)=\{Q:(P,Q)\in T\}$,
  $$|S|=\sum_{P\sim P'}\operatorname{per}_B\big(\varphi(P)\,\triangle\,\varphi(P')\big),$$
  the sum over pairs of adjacent squares of $A$, per = number of boundary
  edges. Every non-empty closed mixed surface has at least 16 plaquettes;
  the surfaces with 16 are the mixed shells of single hypercubes, and each
  is a torus.
  *Proof.* Write $S$ as a 0-1 matrix $M[e,f]$ of finite support. Closure at
  the link $e\times\{b\}$ for all $b$ says that row $e$ is a cycle of $B$;
  closure at $\{a\}\times f$ says that column $f$ is a cycle of $A$. The
  matrices with all rows in a subspace $W$ and all columns in a subspace $V$
  form $V\otimes W$. The finite cycles of the square lattice have the basis
  $\{\partial P\}$ (a finite sum of square boundaries is the boundary of a
  finite region, non-zero unless empty; every finite cycle bounds the finite
  set of squares it winds around an odd number of times). So
  $\{\partial P\otimes\partial Q\}$ is a basis. For the area: the row of an
  edge $e$ between $P$ and $P'$ is $\partial_B(\varphi(P)+\varphi(P'))$. A
  non-zero column is a cycle of $A$, so at least 4 rows are non-zero, and
  each non-zero row is a cycle of $B$ with at least 4 edges. Equality forces
  one square on each side. In a hypercube every link lies in exactly two
  mixed plaquettes, and $16-32+16=0$. $\square$
- **Route F4: the mixed-only corner $W(\beta_{12}=\beta_{34}=0;\ \text{four
  mixed planes at }\beta)$**, in the lane's notation $(\beta_L,\beta_M,\beta_T)
  =(0,\beta,0)$. It is the four-cycle corner of C6. By C15 its character
  expansion is a two-dimensional contour model: a contour in $A$ carries a
  region of $B$ as its label, a unit of contour with label $g$ costs
  $c_{1/2}^{\operatorname{per}(g)}\le c_{1/2}^4$. At $\beta=2.5$:
  $c_{1/2}^4=0.066$, and with the connective constant $2.64$ of
  self-avoiding walks the activity per unit of contour is about $0.17$; the
  smallest polymer (a hypercube shell) has activity
  $\sum_{j\ge1/2}c_j^{16}\approx1.9\cdot10^{-5}$ (torus: weight
  $d_j^{0}c_j^{16}$). So a Peierls-type expansion is expected to converge
  with a wide margin at every $\beta$ of the window (guide estimate; the
  entropy bound is not written). If it does, the corner has the T-analog
  with rate close to $4(-\log c_{1/2})$, with **four of the six orientations
  at window coupling**, and it is not a product model. It is floppy and
  blind to group and dimension. Not found in the lane folder (patterns:
  "(0, beta, 0)", "beta_L = beta_T = 0", "mixed plaquettes only",
  "four-cycle"; the lane uses $\beta_L=0$ only as the end of the descent on
  small boxes, rows 1085, 1089, and on a sublattice, Lemma GH2-0).

### 7.3 Pass C (brief: argue that the bridge is misframed, and name the question that replaces it)

Return (reading; nothing here is checked):
1. The row asks which end-points could serve. Inside plane-dependent Wilson
   couplings the answer is now a finite list (C3, C6, C14, C15): floppy and
   free: forests (3 of 6 orientations), and, if the expansion of F4 is
   written, the mixed-only corner (4 of 6) with a layer around it; floppy
   and open: the triangle (three-dimensional gauge theory); stiff: one
   frozen plane, or two opposite frozen planes. Nothing else.
2. So "something other than sheets for the second half" has no positive
   answer among stiff Wilson end-points: both stiff families are sheet
   systems (the doubly flat corner is the sheets with the transverse
   plaquettes forced flat). The question is misframed if it looks for a
   third stiff face.
3. **The question that replaces it:** which of three things does the lane
   give up?
   (a) *The Wilson cube*: a stiffening that is not a plane coupling (matter,
   mixed action, geometry). The lane walked these (6a #6, #7, #9) and each
   start is blind to the group.
   (b) *The sign carry*: take a free floppy end-point and pay for a bound on
   a decrease (row 878's linear law; C11; (SUM-RULE)).
   (c) *The order "end-point first"*: BR-2 proves the face gap at
   $\beta_T=\beta$ before descending. The proved point is the anchor
   ($\beta_T=0$). A bridge from the anchor has two legs in either order;
   the order face-then-descent puts the sheet-in-field problem first. The
   other order (descent at $\beta_T=0$ by a sign, then $\beta_T$ from 0 to
   $\beta$) meets the sheets nowhere, but its second leg has no sign
   structure for the longitudinal rate (for the transverse rate it is the
   mirror image of BR-2's descent and wants the mirror face). Found in
   parts: BR-9 and check 1075 ("BR-3's first open statement in chain order
   is the beta_L leg at beta_T = 0"). No new route.
4. The bridge as a whole stays as row 1072 framed it: a continuity argument
   whose content is the closing estimate. This pass does not replace that.

### 7.4 Kill pass

| Route | Assumes T? | Contradicts a checked result? | Tried? | Fails a test (valid form)? | Terminal obligation vs T | Verdict |
|---|---|---|---|---|---|---|
| S1 face, then (MON-L) | no | no | yes (rows 1077-1100; 1081-1090) | (MON-L): false for frozen $Q_8$ on a box, so the proof must use a continuous group; GUIDE counterexamples off the window | face gap: not shown comparable; (MON-L): open | wounded (as the lane has it) |
| S2 doubly flat, then two descents | no | no | remark only (row 1053 6.8) | U(1): massless there (passes as a constraint) | (SING) for the $h$-model, then two signs, of which the first is for the wrong direction's rate (the $\beta_T$-descent is kinetic for the transverse transfer operator, the $\beta_L$-descent for the longitudinal one) | wounded twice: end-point open, and the two descents control different rates |
| F1 forest face + decrease law | no | no | yes (idea 32; row 962 A2; (SUM-RULE)) | carry blind to group and dimension is refuted at belief grade | linear law: stronger than T | blocked-stronger (found) |
| F4 mixed-only corner as end-point | no | no (row 1085's box values are at $\beta_M\ge9$) | not found in the lane folder | group-blind and dimension-blind start: allowed for an end-point; the carry must read both | the corner's gap: weaker than T, expected provable by hand; the carry from it: (NOCRIT) in $(\beta_L,\beta_T)$, stronger than T | **survives as an end-point; blocked-stronger as a bridge** |
| E4 block product | no | CA-FAIL refutes its uniform closing condition | yes (route RC) | slab device | - | dead in uniform form (found) |
| Pass C item 3(c), reverse order | no | no | parts (BR-9; check 1075) | - | leg 2 has no sign structure | no route |

### 7.5 Ranking and approach registry

Ranked by what the route would change, divided by the cost to find out.

| Rank | Route | Family (object; mechanism; terminal obligation) | Assumption challenged | What one must believe | Strength vs T | Kill verdict | Cost | First artifact | What it changes | Stop / reopen |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | C14 + C6 + C15 as the answer to the row | the cube of plane couplings; classification by frozen set and 2-core; none | A13, A16 | the proofs of C2, C14, C15 | not a route to T | - | one check row | written here (steps 3, 7) | an owner decision: stop looking for another stiff Wilson end-point; choose among 7.3 item 3 (a), (b), (c) | reopen if a check finds a frozen set or corner missed |
| 2 | F4 | mixed-only corner; Peierls contours with region labels; a convergent expansion at $c_{1/2}\le0.52$ | A13 ("independent pieces") | the entropy bound | weaker (an end-point) | survives as end-point | one proof row, by hand | step 8, attempt 2 | a proved gap at window-size coupling in a non-product model; the far end $\beta_L=0$ of the lane's leg $\beta_T=0$ in infinite volume; a floppy start with 4 of 6 | stop if the contour sum fails at $\beta=2.6$ |
| 3 | S2 | doubly flat corner; port of the O(4) mixing proof; (SING) | - | (SING) | unknown | wounded twice | large | none | a second stiff end-point; no gain over S1 on file | reopen if (SING) gets a mechanism |
| 4 | F1 | forest + linear law | A12 | row 878's law | stronger | blocked-stronger | as row 878 | none | nothing new | as row 878 |

Approach registry (this run; the lane's registry of rows 998, 1072, 1076
is not rewritten):

| Family | Object | Mechanism | Terminal obligation | Strength vs T | Status | Evidence | Reopen condition |
|---|---|---|---|---|---|---|---|
| floppy-exact | forest faces | independence (C2, C3) | a decrease law on the carry | stronger | blocked-stronger | C3, C4; lane idea 32 | a volume-free bound on the action excess (C11, KIN-5) |
| floppy-expansion | mixed-only corner F4 and a layer around it | contour expansion (C15) | entropy bound, then the same decrease law | end-point: weaker; bridge: stronger | provisional (end-point), blocked-stronger (bridge) | step 8 attempt 2 | - |
| stiff-one-plane | lane's face | sheets in fields; then a sign | PIN-2 or PIN-U, EV, long clusters; (MON-L) | unknown/comparable | active in the lane | rows 1077-1100 | - |
| stiff-two-planes | doubly flat corner | $\sigma$-model on $SU(2)^{V_T}/SU(2)$ | (SING); two signs for two different rates | unknown | blocked-local | row 1053 6.8; 7.4 | a singlet mechanism |
| frozen-adjacent | two frozen planes sharing a direction | - | - | - | retired | C14 (rate 0) | none |
| block criterion | block product E4 | Dobrushin-Shlosman | uniform mixing | false in uniform form | retired (uniform form) | CA-FAIL | a constant-coupling form with a hand bound |

Lenses considered and found empty for this row: operator algebras, number
theory, logic, K-theory, optimisation (one line each: no object in the
end-point question changes under them). Reframes used: finite carrier
versus limiting family (frozen faces are limits, C14); supplied model versus
target (A4); local pattern versus global structure (C15).

### 7.6 Pre-registration of the runs of step 8 (written before any run)

- **Run 1 (tries to refute C2 and C2').** Group $S_3$ (non-abelian, 6
  elements), class weight $f_\beta(g)=\exp(\beta\chi_{\rm std}(g)/2)$. One
  ladder with two rungs: variables $M_0,M_1,M_2,a_0,a_1,b_0,b_1$; plaquettes
  $P_k=M_ka_kM_{k+1}^{-1}b_k^{-1}$ with weights $f_{0.9},f_{1.7}$; $\Psi$ a
  fixed random positive table on $(a_0,a_1,b_0,b_1)$. Exhaustive sum over
  $6^7$ configurations. **Pass (not refuted):** the marginal of
  $(a,b)$ equals $\Psi/\sum\Psi$ and the joint law of $(P_0,P_1,a,b)$ equals
  $f f\Psi$ normalised, both to $10^{-12}$; and for the periodic ladder
  ($M_2=M_0$) the marginal weight of $(a,b)$ equals
  $\Psi\cdot\sum_j c_j(f_{0.9})c_j(f_{1.7})\chi_j(a_0a_1)\chi_j((b_0b_1)^{-1})$
  up to one constant, to $10^{-12}$. **Fail:** any larger deviation; then
  C2 or C2' is wrong as written.
- **Run 2 (tries to refute C15, and sizes the polymers of F4).** Box: $A$
  and $B$ each a $3\times3$ grid of sites (4 squares each), 144 mixed
  plaquettes, 216 links, 16 hypercubes. (i) Rank over $\mathbb F_2$ of the
  plaquette-to-link boundary map; **pass:** the kernel has dimension 16 and
  equals the span of the 16 hypercube shells; **fail:** otherwise (C15
  wrong). (ii) The exact histogram of $|S|$ over all $2^{16}$ closed
  surfaces in the box. Reading fixed now: C15's bound is refuted if any
  non-empty surface has fewer than 16 plaquettes or if the number with
  exactly 16 is not 16. (iii) $Z_{\rm box}(u)=\sum_Su^{|S|}$ at
  $u=0.479,0.507,0.520$ (the $j=\tfrac12$ level only). Reading fixed now:
  if $Z_{\rm box}-1>0.01$ at $u=0.520$, the claim "wide margin" of F4 is
  withdrawn; if $Z_{\rm box}-1<0.01$, it stands as a guide. The run says
  nothing on higher representations or on the entropy at large area.
Both runs are exact finite enumerations in pure Python, one serial job,
`nice 10`. They can refute or guide. They discharge nothing.

## Step 8. Real attempts

Budget used: about 15 minutes of the 2 hours for runs; the rest of the
step is hand work. Before each attempt the lane folder was searched (step 5
patterns; and for attempt 2 the patterns of route F4). No row holds C14 or
F4. `library/open-registry.md` was searched by `grep` only, not read.

### Attempt 1: the answer to the row inside the Wilson cube (C6 + C14)

Done in steps 3 and 7.1. Result, in one statement (**argued**, by Claude
Fable 5.2, not yet checked; the triangle case rests on a BELIEF):

> For plane-dependent Wilson couplings in $[0,\infty]^6$: (1) the corners
> with couplings in $\{0\}\cup(0,\infty)$ reduce, by exact integration of
> leaf orientations, to five cases: independent plaquettes (forests,
> solved), the three-dimensional gauge theory, the mixed-only corner, $K_4$
> minus an edge, the full model. (2) With no zero coupling, a positive rate
> in every direction allows only: no frozen plane, one frozen plane, or two
> opposite frozen planes.

On or off the path of T: off. It is the answer to "which end-points", not a
step towards T. It did not move the wall.

### Attempt 2: route F4, the mixed-only corner

**What is proved here (argued, unchecked):** C15, the structure of the
closed surfaces. **What is reduced to one exact statement:**

> **(F4-KP).** Let $\beta\le2.6$. Consider the polymer system whose polymers
> are the connected closed mixed surfaces $\gamma$ with a non-trivial SU(2)
> representation on each plaquette and an intertwiner at each link, with the
> activities $w(\gamma)$ of the character expansion of
> $W(\beta_{12}=\beta_{34}=0;\beta_{13}=\beta_{14}=\beta_{23}=\beta_{24}=\beta)$.
> Then there is $a>0$ with
> $\sup_p\sum_{\gamma\ni p}|w(\gamma)|\,e^{a|\gamma|}\le a$.

Given (F4-KP), the standard convergence theorem for polymer expansions
(Kotecký-Preiss; to be rebuilt in `library/` before any use, S4) gives a
unique limit state, and exponential clustering of gauge-invariant local
observables with a rate that does not depend on the volume. (F4-KP) is
**open**: the entropy bound for labelled surfaces is not written. It is not
T-equivalent: it concerns a different member of $\mathfrak F$.

**Why it should hold with margin (guide; hand numbers).** By C15 every
polymer has at least 16 plaquettes; the 16-plaquette polymers are tori with
activity $\sum_{j\ge1/2}c_j^{16}$ (a closed surface of genus $g$ with one
representation has weight $d_j^{2-2g}c_j^{|\gamma|}$): $7.7\cdot10^{-6}$,
$1.9\cdot10^{-5}$, $2.9\cdot10^{-5}$ at $\beta=2.3,2.5,2.6$. Four of them
contain a given plaquette. A product torus (loop of length $\ell$ in $A$)
$\times$ (loop of length $m$ in $B$) has $\ell m$ plaquettes; the number of
loops of length $\ell$ through an edge grows like $2.64^{\ell}$, and
$2.64\,c_{1/2}^4\le0.20$ in the window. Along a contour the label can change
only at a branch point (Kirchhoff rule: the labels at a vertex of $A$ add up
to zero), and each change costs further plaquettes.

**Run 2 (pre-registered in 7.6; result recorded as it came out).**
Script and output: `runs/gap-face-exercise-fable/run2_mixed_surfaces.py`,
`run2.out` (written in scratch; copied into the lane by the lead). Pure Python, exact, one serial job.
- (i) 144 plaquettes, 216 links, rank 128, kernel dimension **16**; the 16
  hypercube shells are closed and independent. **Pass: C15 is not refuted
  in this box.**
- (ii) Areas and counts of the $2^{16}$ closed surfaces: 0: 1; **16: 16**;
  24: 32; 30: 32; 32: 96; 34: 64; 36: 16; 38: 128; 40: 128; 42: 128; 44:
  384; 46: 256; 48: 696; largest 96. No non-empty surface below 16.
  **Pass.** (24 is a domino times a square; 30 is two hypercubes that share
  one mixed plaquette corner-wise: both checked by hand.)
- (iii) $Z_{\rm box}-1=1.24\cdot10^{-4},\ 3.08\cdot10^{-4},\ 4.62\cdot10^{-4}$
  at $u=0.479,0.507,0.520$; in each case within $1.2\%$ of the leading term
  $16u^{16}$. Below the pre-registered line $0.01$. **Reading as fixed
  before the run: the "wide margin" claim stands as a guide.**
What the run does not show: anything about large areas, about higher
representations, about the non-abelian link factors, or about infinite
volume. It is a guide. It proves nothing.

**Run 1 (pre-registered in 7.6).** `run1_leaf_s3.py`, `run1.out` in the same
folder. Exhaustive over $6^7$ configurations of the two-rung ladder for
$S_3$: largest deviation of the marginal $4.3\cdot10^{-18}$, of the joint
law $1.1\cdot10^{-19}$; periodic factor of C2': largest deviation
$1.1\cdot10^{-15}$. **Pass: C2 and C2' are not refuted.** The run does not
prove them; the proofs are in step 3.

**What F4 would change if (F4-KP) is proved.**
1. A member of $\mathfrak F$ with four of six orientations at window
   coupling, not a product, with a proved volume-uniform rate close to
   $4(-\log c_{1/2}(\beta))\approx2.7$. (C7 says independent-plaquette
   patterns stop at three of six.)
2. In the lane's family: the far end $\beta_L=0$ of the leg $\beta_T=0$, in
   infinite volume. The anchor $(\infty,\beta,0)$ is the other end (N4c). So
   that leg would have both ends proved, with rates about $2.7$ and of order
   $e^{-\pi\beta}$. The lane's box runs (rows 1085, 1089) could then be
   compared with exact end values. This is a consistency datum for the
   direction of (MON-L) at window $\beta_M$. It is not a proof of any sign.
3. It does **not** change (ii). The carry from the corner must raise
   $\beta_L$ and $\beta_T$ from 0 to $\beta$ and bound a decrease of the rate
   from about $2.7$ to about $0.7$: the same open law as for every floppy
   start.
On or off the path of T: off (an end-point). It did not move the wall.

### Attempt 3: is there a second stiff end-point with a cheaper proof? (S2)

Not attempted beyond the kill pass (7.4). Reason: the terminal obligation is
the lane's (SING), which row 1053 6.9 and row 1076 already hold as open,
and the two descents from the doubly flat corner control rates in two
different directions (7.4). Smallest test that would decide whether S2 is
worth a row: write the transfer operator of the $h$-model in a transverse
direction in the form of Lemma KIN and see whether the $\beta_T$-descent has
any consumer for the *longitudinal* rate. It waits on the lead (a queue
decision), not on an input.

### Summary of step 8

| Attempt | Result | Mark | On the path of T? | Moved the wall? |
|---|---|---|---|---|
| 1 | classification C6 + C14 | argued (triangle case: belief) | off | no |
| 2 | C15; (F4-KP) named; runs 1 and 2 pass | argued; open; guide | off | no |
| 3 | S2 not attempted; smallest test named | - | off | no |

## Step 9. Report

Written by Claude Fable 5.2 (Anthropic), effort high, laptop subagent, one
writer, no subagents. Only this file was written in the checkout. Nothing
was committed or pushed. Nothing here is checked by another model. No mass
gap is claimed.

### 9.1 The wall, in plain words (corrected)

We study a grid model of the strong force with a strength dial. We want to
prove that far-apart measurements become independent at a fixed exponential
rate, at the dial settings used in simulations. Proofs exist only for
altered versions of the model. The plan is a bridge from an altered version
to the real one. This exercise asked which altered versions can serve as
the start. The answer has two kinds. A "loose" start is one where the
measurements decouple faster than in the real model; such starts cost
nothing, but the bridge must then prove that the rate does not fall to
zero on the way. A "stiff" start is one where they decouple more slowly;
then the bridge only has to prove that the rate goes up, but the stiff
starts are themselves hard. When each of the six plane directions has its
own dial, the list of stiff starts is short: one plane frozen, or two
opposite planes frozen. Both are made of the same two-dimensional sheets.

### 9.2 What the exercise found

1. Most of the fresh pass found again what the lane has (rows 859, 962,
   1053, 1063, 1072, 1076): the solvable line with no spatial plaquettes,
   the product of two-dimensional planes, the need to read the group and the
   dimension in the carry, the box-size warning, the Hellmann-Feynman price.
   The lane's distinction between a start with a larger rate and one with a
   smaller rate was missing from the fresh pass and was taken over. (reading)
2. **Classification (argued, unchecked).** With plane couplings in
   $\{0\}\cup(0,\infty)$, exact integration of "leaf" orientations (Lemma
   C2) leaves five cases; the solved ones are the forests, with at most
   three of six orientations switched on (C3, C6), and no pattern of
   independent plaquettes keeps more than half of them (C7). With no zero
   coupling, two frozen planes that share a direction give rate 0 in that
   direction (C14, exact); a frozen triangle is an ordered three-dimensional
   magnet (belief for the rate); so the stiff faces are one frozen plane and
   two opposite frozen planes.
3. **One end-point not found in the lane folder (route F4):** the corner
   with only the four mixed planes switched on, $(\beta_L,\beta_M,\beta_T)=
   (0,\beta,0)$. Its closed surfaces are in one-to-one correspondence with
   finite sets of unit hypercubes (C15, argued); the smallest has 16
   plaquettes. A hand expansion is expected to converge at every window
   coupling (guide). Two exact enumeration runs, pre-registered, passed. The
   remaining statement is (F4-KP), open.
4. The owner's question, "something other than sheets for the second half":
   among stiff starts inside plane-dependent Wilson couplings, no (given
   C14). The doubly flat corner of row 1053 6.8 is the only other stiff
   face, and it is the same sheets with the transverse plaquettes forced
   flat.
5. Nothing in this run moves the wall. F4 and the classification are about
   end-points. The carry is untouched.

### 9.3 Filters corrected

- Of the lane: **none.** 26 set-aside end-points and end-point proofs were
  re-judged (6d). One verdict is moot for this row's question: the doubly
  flat corner was marked "not used" for the flux device; as an end-point for
  a sign carry it is not discarded, and it comes back as route S2 with the
  lane's own obstacle (SING).
- Of this run (corrected in place): "the two-dimensional O(4) gap is open"
  (false since the September 2026 preprints; N4c); the block-product
  end-point (its uniform closing condition is false by CA-FAIL); the
  three-dimensional O(4) threshold (1.0109, not 0.94); the symmetry of the
  path-tree family (rates change direction under the relabelling).

### 9.4 Routes worth doing (at most three)

1. **A check of the classification and of C15** (work item W1). Believe:
   nothing; it is a check. Cost: one check row. First test: C14(a) and the
   graph list of C14(b). It changes: whether the lane may stop looking for
   another stiff Wilson end-point.
2. **F4, the mixed-only corner** (work items W2, W3). Believe: the entropy
   bound (F4-KP). Cost: a reading row and one proof row by hand. First test:
   done (runs 1 and 2, guides). It changes: one more proved member of the
   family, with four of six orientations at window coupling, and both ends
   of the lane's leg $\beta_T=0$. It does not change the carry.
3. None further. The lane's own route S1 (rows 1096-1100) is not re-proposed
   here; this run adds nothing to it.

### 9.5 What not to do next

- Search for a third stiff face among plane-dependent Wilson couplings
  (C14, once checked).
- Freeze more planes (two adjacent frozen planes: rate 0).
- Treat forests, or the count of couplings already in place, as "closer" to
  the window (C7, C8, and the carry from every floppy start is the same open
  law).
- Open a row on the doubly flat corner before (SING) has a mechanism.
- Read the box runs of rows 1085-1090 as statements about the corner F4:
  their box has one transverse plaquette.

### 9.6 The exact price

Not sharpened beyond the lane's (`parts/gap.md` L264-275). What this run
adds is a necessary shape, not an equivalence (argued, given C14): a bridge
to T inside plane-dependent Wilson couplings whose carry is only a sign
must start on the face with one frozen plane or on the face with two
opposite frozen planes, with the other couplings at least $\beta$. So for
such bridges the end-point half is a statement about coupled
two-dimensional sheets, whatever the route.

### 9.7 Work items

**W1. Check request (first).** By a model that did not write this file;
another provider is preferred; a same-provider check is labelled as such.
Statements: C1, C2, C2', C3, C4, C5(a), C6, C7 (step 3); C14 (7.1); C15
(7.2); the conversion $\beta=4\beta_{\rm theirs}$ and the ranges of N1a
(step 2); the reduction "(F4-KP) gives the T-analog at the corner" (step 8).
Read: this file, steps 2, 3, 7.1, 7.2, 8. Test first: (1) in C2, the change
of variables when direction $\mu$ is periodic and $\nu$ is free; (2) in C4,
the step "an invariant function orthogonal to constants has support without
degree-1 sites" and $c_j\le c_{1/2}$; (3) in C14(a), the gauge fixing with
free boundary and the positive variance; in C14(b), each of the eleven
graphs on four vertices; (4) in C15, "rows in $W$ and columns in $V$ is
$V\otimes W$" for finite support, and the basis claim; (5) the rank count of
C7 on a torus; (6) search the open PR branches and `main` for C6, C7, C14,
C15 and for the corner $(0,\beta,0)$. Stop rule: each statement HOLDS, HOLDS
AFTER CORRECTION with the text, or FAILS with its first failing line.
Output: `library/gap-face-exercise-check-<model>.md`.

**W2. Reading row for F4** (the lane's rule: a reading on every new path).
Question: is the SU(2) lattice gauge model on $\mathbb Z^2\times\mathbb Z^2$
with only the mixed plaquettes (no plaquette inside either plane) in the
literature, under any name (transverse-lattice gauge theory at zero
longitudinal and transverse coupling; gauge theory on a product of graphs;
plaquette models with rows and columns closed)? Any convergent expansion or
solution? Any statement on the closed surfaces of a product of two graphs
(Künneth form)? Also: a clean statement of the Kotecký-Preiss criterion and
of "convergent polymer expansion gives exponential clustering" with proofs
that can be rebuilt. Open copies only, each download in a new empty folder,
no sign-in, never commit a paper. Output:
`library/prior/gap-mixed-corner-read-<model>.md`, one RESULT line.

**W3. Proof row for F4** (after W1 holds for C15 and W2 is in). Statement:
(F4-KP) of step 8 for $\beta\in[2.3,2.6]$, and from it the T-analog at the
corner with an explicit rate. Read: this file 7.2 and step 8; `parts/gap.md`
L221-262 (tests). Order of work: (1) write the character expansion on the
product complex, with the link integrals where four plaquettes meet; (2)
bound $|w(\gamma)|$ by $\prod_pc_{j_p}$ times an explicit link factor; (3)
count labelled surfaces through a plaquette with the height form of C15
(contours in one plane, region labels in the other, Kirchhoff rule at
branch points); (4) the sum by hand at $\beta=2.6$, with every constant
displayed; (5) the clustering theorem, rebuilt. Tests on any proof: compact
U(1) (the same expansion converges where $I_1/I_0$ is small enough; the
proof may be group-blind, that is allowed for an end-point); the box values
of `run2.out` at small area. Stop rule: a proof, a counterexample, or one
named step that failed in three written ways. No computer-assisted step.
Output: `library/gap-mixed-corner.md`.

**Not proposed, with reasons.** A row on the doubly flat corner (its first
open statement is the lane's (SING)). A row on forests as starts (found;
the carry is row 878's law). A numeric search for where the rate rises on
the leg $\beta_T=0$ (a guide that decides no step). A row on the corner
"$K_4$ minus an edge" (it contains the three-dimensional problem).

### 9.8 Appendix

The tables are in place above: inventory (step 2); conclusions C1-C13
(step 3); assumptions (step 4); comparison (5.1); set-aside methods, tests
and verdicts (6a, 6c, 6d); routes, kill pass, ranking and registry (7.4,
7.5); runs (7.6, step 8).

- *Assumptions most likely to be wrong:* A13 (closeness in couplings is the
  measure); A12 (two comparable halves); A26 (one phase in the open cube;
  a belief with no source checked here).
- *Assumptions most expensive to be wrong:* A25 (T is true); A27 (N4c, two
  unrefereed preprints that carry the anchor); A28 (the finite-temperature
  table, for the box quantifier).
- *Literature proofs worth translating:* the Kotecký-Preiss polymer
  criterion with the clustering consequence (for W3); Durhuus-Fröhlich
  Theorems 1.2 and 1.3 in the form of Cao-Nissim-Sheffield Theorem 2.3 (the
  slab $\sigma$-model; in $d=4$ its hypothesis fails above $1.0109$, so it
  does not reach the window).

### 9.9 Strong words, read against the run

- "Classification", "only", "exactly" (C6, C14): argued by hand, unchecked;
  C14's triangle case is a belief; C6 lists the graphs on four vertices
  (eleven; done by hand); the scope is couplings in $\{0\}$, $(0,\infty)$
  and $\{\infty\}$ per orientation, free boundary. Interior points of the
  cube are not classified.
- "Solved" (forests): for free boundary; in periodic boxes up to the factor
  of C2', analysed only when all sides are long.
- "Not found in the lane folder": by the `grep` patterns named, at
  `a4ebff848`; PR branches and `main` not searched. Never "new".
- "Expected to converge", "wide margin" (F4): a guide from hand numbers and
  one finite box at the $j=\tfrac12$ level. (F4-KP) is open.
- "No" as the answer to the owner's question: for stiff end-points inside
  plane-dependent Wilson couplings, given C14. It says nothing about other
  actions or about floppy starts.
- "Pass" for the runs: not refuted. A pass is no support beyond that.

### Credits

K. Osterwalder and E. Seiler; A. Migdal; D. Gross and E. Witten; B. Durhuus
and J. Fröhlich; S. Cao, R. Nissim and S. Sheffield; H. Shen, R. Zhu and
X. Zhu; J. Fingberg, U. Heller and F. Karsch; J. Fröhlich, B. Simon and
T. Spencer; J. Fröhlich and T. Spencer; A. Guth; C. Borgs and E. Seiler;
G. Bhanot and M. Creutz; M. Creutz; Y. Fu and H. B. Nielsen; T. Koma;
P. Orland; W. Bardeen, R. Pearson and E. Rabinovici; S. Chatterjee;
R. Dobrushin and S. Shlosman; D. Stroock and B. Zegarlinski; R. Kotecký and
D. Preiss; R. Peierls; C. Michael; the authors of the OpenAI Math preprints
on the two-dimensional O(n) and O(4) models; J. Ding, F. Huang and P. Yang;
Y. R. Pei; D. Bhattacharjee, U. Bhattacharya, J. M. Lockwood and
T. Romanov; T. Balaban, and E. Sussman and L. Alpoge (with Claude and Codex
as authors of their text), whose account the gap target serves. In this
lane: rows 859 and 962 (the line $\beta_s=0$), 1053 (the face, the splits,
the doubly flat corner; Claude Fable 5.2), 1063 (measured assumptions;
Claude Opus 5.5), 1072 (the bridge exercise; Claude Opus 5.5), 1076 (the
vectors, Lemma KIN, Lemma SWAP; Claude Fable 5.2), 1077 (gpt-6-astra),
1085-1090, 1091, 1096, 1099 (Claude Fable 5.2 and gpt-6-astra), the checks
1074, 1075, 1078, 1079, 1093, 1094, 1097, 1098, 1100, and the readings 1073
and 1104 (gpt-6-luna).

RESULT: Row 1103 (Claude Fable 5.2 high, laptop subagent; checked by no one; two exact enumeration runs, guides only): no bridge is proved, the wall does not move, and no mass gap is claimed. ARGUED by hand: Lemma C2 (a leaf orientation integrates out exactly, with the periodic factor C2'), C3/C4/C6 (forest faces are solved for every finite coupling, star rate 4(-log c_1/2); the corners reduce to five 2-cores), C7 (independent-plaquette patterns keep at most half of the plaquettes), C14 (two frozen planes that share a direction give rate 0, so the only stiff faces of the Wilson cube are one frozen plane and two opposite frozen planes; the frozen-triangle case rests on a belief), C15 (closed surfaces of the mixed-only corner correspond one to one to finite sets of unit hypercubes; at least 16 plaquettes). Answer to the row inside plane-dependent Wilson couplings: free end-points are floppy (forests; and the mixed-only corner (0, beta, 0), route F4, not found in the lane folder, with four of six orientations at window coupling, reduced to the open entropy statement (F4-KP), guide runs pass); stiff end-points are sheet systems only, so "something other than sheets" does not exist among them. Corrected: no filter of the lane (26 verdicts re-judged; the doubly flat corner comes back as a named end-point with the lane's obstacle (SING)); four errors of this run's own fresh pass, in place. Found again, with credit: most of the fresh pass (rows 859, 962, 1053, 1063, 1072, 1076). Open: (F4-KP); the carry from every end-point; the lane's PIN-2/PIN-U, EV and (MON-L). Not done as the row asked: the nine check files were read in part only.
