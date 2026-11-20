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

Status of this file: step 2 (choice of attack) in progress. Nothing below this line is proved yet.
