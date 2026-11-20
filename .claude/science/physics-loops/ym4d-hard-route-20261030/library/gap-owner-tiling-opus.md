lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T02:14Z

# gap-owner-tiling-opus (FINISH row 1285): the owner's multi-direction idea, the tiling question

Row: 1285 of FINISH.md, branch claude/ym4d-hard-route pinned at ff38f286f. Worker: Claude Opus 5.5 (max), Mac mini
Claude worker 1. Labels: PROVED, ARGUED, GUIDE, OPEN as the row asks. Sibling row 1286 (gpt-6.2-astra, same question)
is `library/gap-owner-tiling-astra62.md`; it is read only after my own Section 3 is written, and cited where used.

## Status log

- 2026-11-20T14:14Z (date -u): file created; reading FINISH rules, `parts/gap.md`, rows 1273 and 1279.
- 2026-11-20T14:21Z (date -u): Section 1 written (inputs, registry grep, plan).

## 1. Inputs, repo search, plan

Read at ff38f286f, before any attack: `FINISH.md` rule sections (L52-73, L320-350) and rows 1273, 1279, 1285;
`GOAL.md` in full; `parts/gap.md` L8-104 (state of attack, lead rules); `library/gap-mini-neutral-fable.md`
L30-60 (the exact (N-phys) statement, row 1161 / row 1179 wording); row 1273's file
`library/gap-owner-threeaxis-opus.md` in full; check 1279 `library/gap-threeaxis-check-astra.md` L55-123 (the
Hamiltonian, tiling and verdict sections). **Provenance of independence:** the sibling row 1286
(`library/gap-owner-tiling-astra62.md`, gpt-6.2-astra, same question, committed at my pin) was read at its outline
and its RESULT line (L209) only, before I chose my attacks, so that I do not repeat it. Its ground: reduced-model
arrays of N^3 periodic-block oscillators (independent, exactly constrained, finite and infinite spring stiffness,
tree sewing with dynamical frames giving a singlet gap asymptotic to kappa_r g^(2/3)/(N l), cyclic adjoint sewing
with at least 3N^3 soft neutral plaquette excitations), and a Wilson trace estimate (its (7)) for straight segment
transports, with the unselected links and the fine fluctuations left OPEN. Everything below is my own unless a
row is cited.

**Consumer (the "couplings the lane needs").** (N-phys) (row 1161 L146-148, wording of row 1179, quoted in
`gap-mini-neutral-fable.md` L39-49): one admissible physical side L and j_0 such that for every j >= j_0, with
n_j = L/a_j, 4 | n_j, some integer u_j in [3, n_j/K] gives s_j(u_j; n_j) <= 1/2, where s is the centre-neutral
excited thermal sum of the periodic cube in vacuum units and K = 512. GUIDE size (same file 2.4): m L of order
1.1 x 10^4. Equivalent and sufficient forms of the older wall (W) (z^-(L) > 256 D_0 + 30 at one L in the window)
are listed in `parts/gap.md` L13-35.

**Registry grep** (counts of files among `library/*.md`, `library/prior/*.md`, `parts/*.md` that contain the
term, case-insensitive, at ff38f286f): tiling 80, tiled 15, Knabe 33, "finite-size criterion" 37,
local-to-global 15, Garland 0, trickle 2, Yarotsky 1, Michalakis 13, Gosset 18, Stroock 42, Zegarlinski 25,
"block dynamics" 10, Martinelli 36, 4.1167 6, g^(2/3) 12, "2 pi/L" 7, "photon gap" 1, stiffness 128, spring 43,
Nedelko 1, "domain model" 2, Copenhagen 1, "intermediate volume" 0, sphaleron 2, Koller 18, "van Baal" 48.
So finite-size (local-to-global) criteria and the small-volume literature are heavily on file; each statement
below that touches them cites the hit it rests on (Section 2 lists the hits read).

**Plan (provisional; one step per response, appended at once).**
1. This section.
2. The tiling question as a carry statement: which carry theorems are on file (lane engine, (N-phys) consumer,
   Knabe / Martinelli / Dobrushin-Shlosman forms), what each needs from one block, and what a multi-direction
   block supplies (Lemma S: z = kappa g(l)^(2/3)). Read the registry hits first.
3. Value test (fact test with the free photon): is the single-block neutral gap of SU(2) selective at all?
   Lattice photon spectrum by hand.
4. Attack on the carry itself in the Wilson setting: the stiffness that the Wilson action puts between blocks,
   and what it does to the one-block mechanism.
5. A second, distinct attack on the first failing step of 4 (local-to-global criterion with a boundary-uniform
   block input).
6. Verdict and RESULT line.
