lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-20T13:41Z

# gap-mini-solve-k-fable: attack on the four-dimensional SU(2) mass gap

Queue row 1201. Worker: Claude Fable 5.2, max effort, Mac mini worker 3, pinned at commit 20239923e.
This is research-stage working state. It grants no status and is not a public claim.

Labels used below: PROVED (every step written here or in a cited checked note), ARGUED (argument given, a step is not written out or not checked), GUIDE (numerics or heuristics, never a proof step), OPEN.

## 0. Plan (written first, before any reading of earlier attempts)

1. Repo search: read the RESULT lines of the earlier `gap-*` rows in FINISH.md, `parts/gap.md`, `library/open-core.md`, and the earlier `gap-mini-solve-*` notes, so that this run does not repeat an attack.
2. Choose one route that the earlier runs did not take, or the first unproved step of the best earlier route.
3. Attack it, one step per response, and append each step here.

## 1. Repo search (done 2026-11-20T02:10Z)

Read in full: `FINISH.md` L1-84 and L299-356 (rules), row 1201 (this item), rows 1188-1211 (the plain-brief rows a-f, their checks, the gpt-6.2-astra chain rows 1192, 1204, the two Argon rows and checks); `GOAL.md`; `parts/gap.md` L1-322 (state of attack, obligations, route registry, test table, price); `library/gap-crux-restate.md` Sections 1, 2 and 3.4 (DEF, candidates C1-C5, Theorem S). `library/open-core.md` holds the existence chain only; it has no entry for the gap lane (headings read, grep for N-phys empty).

Where the lane stands, in my words (GUIDE, a reading; every item is cited to its row in `parts/gap.md`):

- Engine (Theorem S, row 697, checked rows 698-699): on periodic tori, one inequality S(n; (2n)^3) < 1/5041 at one size gives a uniform gap on all larger cubes. It holds for every group. The whole open content is the seed at a physical size, uniformly in the cutoff: (W), equivalently (PHYS-SEED); in the later split, (N-phys) (centre-neutral excited trace at most 1/2 at aspect K = 512) plus the branch selection (BS), plus the continuum datum of the T0 chain.
- Every route on file ends at one order-one inequality in the band beta 2.3-2.6 that must be selective: false for compact U(1), for a product with a massless factor, for frozen Z_2 (periodic form), for a peaked weight w_p at its transition.
- Routes on file with their first failing step: contraction of the Casimir energy (RA), sign in beta (RB), one-scale number (RC), sector engines (RE), functional inequalities and log-Sobolev (RF, LC), hierarchical comparison (RG), the anisotropic bridge BR-2 with (SING), the pinned short step (T-pin), the Dobrushin-Shlosman hypothesis (DS-W), the slab extraction (A), ports of the posted 2D O(N) proofs (rows 1007-1050, 1188, 1193), aligned and Coulomb frames (route (ii)), vortex containers and Tomboulis-Kanazawa decimation, Lee-Yang and zero transport (Route Z), surface expansions with signs (method 35), swap criteria in law (method 34), the weak-coupling end and the electric strip (rows 1143-1175).
- The six plain-brief Fable rows a-f screened 12 + 17 + 10 + 7 + 5 candidate routes and found each on the map.

Consequence for this run: a seventh screening has no value. This run picks one mechanism and works on it.

## 2. Choice of attack (written 2026-11-20T02:20Z)

### 2.1 What a proof must contain (reading of the record; ARGUED there, cited)

1. The Jaffe-Witten gap clause reads one lattice premise, the neutral one-cube bound (N-phys), plus the continuum datum (row 1179 Theorem BP; row 1161; check 1183). The flux half (BS) is on the path of (W) only.
2. In pure gauge theory every stiffness, twist or frame mechanism on file acts on the flux half: the bracket of the posted 2D O(4) proof gives the charged half, and the neutral half there comes from association (row 1193, citing rows 1009, 1076-1086). The gauge port of association failed three ways (row 1084); the eight plaquette monomials have a sign pattern that no phase shift removes (row 1190 2.1).
3. So the missing object is a mechanism for neutral mixing at order-one coupling that reads the group. The record names it (SING) in two dimensions and (N-phys) in four.

### 2.2 Candidates generated in this run, each grepped before any work (rule 0a)

| # | Candidate | On file as | Verdict |
|---|---|---|---|
| 1 | Port of the 2D stiffness iteration with a colour frame | rows 1007-1050, 1188, 1193 (Propositions B, B', Theorem BH, Lemma PC, route (ii)) | found again |
| 2 | The time-independent gauge group as rigid group in temporal gauge | row 1016 QL1, HAM1; row 1190 item 2 | found again: its response is the static-charge (Polyakov) family, blind |
| 3 | Durhuus-Frohlich layers with the posted O(4) theorem | rows 712, 819, 825; method 36 (two-sided backgrounds order the layer at large b) | found again |
| 4 | Small-volume (toron) gap carried by a monotone step-scaling function | row 859 items 8, 36; rows 1143, 1008; route RA | found again: no step that excludes a zero of the step-scaling function |
| 5 | Hellmann-Feynman in beta with a bound on the action excess of the lightest state | row 859 item 46 and G8, (NOCRIT-HF); route RB | found again |
| 6 | Trace anomaly: scale derivative of D equals the finite-size plaquette shift | (MONO-Delta), `gap-phys-seed.md` L351; Proposition VIR; route RB | found again |
| 7 | Bakry-Emery on the orbit space (Singer's curvature) | method 31; rows 957, 968; Proposition G1 of row 1128 | found again |
| 8 | Three-dimensional compact U(1) (Gopfert and Mack) as a template or test | row 859 item 34; exercise 2 I20, (m2) | found again |
| 9 | Griffiths-type positivity for products of characters | (EP) false, Theorem EP-NO of row 754; method 35 | found again |
| 10 | A neutral soft mode needs a first-order-like structure; the Wilson axis is near a first-order end point | Proposition V, K7, (NO-1ST) of row 1109 | found again |
| 11 | The spacetime symmetry group of the box as the rigid non-abelian group: every glueball state except a scalar at rest is charged under it | sheared tori and Lemma SHIFT (row 962 A4, 7.4); rotated tori (row 963); "shape twists" in row 1190 item 3 (one line, "found again") | in part: the identities are on file; the question "does the bracket of this group give a gain" is not answered on file |

Candidate 11 is the only one with an unanswered question. Section 3 answers it.

A failed step of my own, kept as a negative result (ARGUED): I tried to get (MONO-Delta) for compact U(1) from Ginibre's inequality by "identifying periodic images". This is wrong. Identifying the sites of the kn-torus modulo n gives the n-torus at coupling k^4 beta, not at beta. So Ginibre compares different couplings and gives no sign for the finite-size plaquette shift. The record already holds that (MONO-Delta) fails for the ordered Ising model, which has Griffiths' inequalities (`gap-phys-seed.md` L367-373).

Status of this file: step 3 in progress.
