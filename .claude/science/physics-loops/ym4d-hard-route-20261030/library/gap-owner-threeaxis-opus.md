lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T00:27Z

# gap-owner-threeaxis-opus: multi-direction plaquette blocks and the SU(2) mass gap

Row 1273 of FINISH.md. Started 2026-11-20T12:27Z (date -u) at commit 49bbe938f on branch claude/ym4d-hard-route.
Worker: Claude Opus 5.5, max effort, Mac mini worker 2. Research-stage working state; no claim of status.

Labels: PROVED (written argument, checkable by hand), ARGUED (argument with a named gap), GUIDE (heuristic or numeric guide, never a proof step), OPEN.

## Step 0. Save protocol

File created first, per the row. Sections are appended one step at a time.

## Step 1. Repo search (rule 0a) and plan

Read for this step, at 49bbe938f: `GOAL.md` in full; `FINISH.md` L1-84, L299-351, row 1273 (this item) and the
RESULT parts of rows 930-934, 1011, 1141, 1188, 1200, 1201, 1228, 1249, 1256, 1260; `parts/gap.md` L1-104;
`library/gap-mini-neutral-fable.md` L55-135 ((N-phys) and what is on file about it).

Grep of `library/*.md`, `parts/*.md` and `FINISH.md` for the owner's idea and its neighbours (several wordings:
multi-direction, several directions, different axes, non-commuting rotation/twist, Fact T, three-axis, femto,
Luscher, van Baal, commutator potential, quartic valley). `library/open-core.md` has no line on rotations, twists
or commutators of blocks. Matches, each read at the cited lines:

| On file | Where | What it says | Bearing on this item |
|---|---|---|---|
| Fact T | `gap-crux-restate.md` L53; `gap-crux-exercise4-max.md` L210, L283 | -1 is the group commutator of i sigma_1 and i sigma_2; the single-plane central twist has classical cost zero for SU(2) | the commutator of two perpendicular half-turns is central: flux half only. Q_8 shares it (check of row 1003, L251-305), so it is not selective for the flux half |
| Crossed twists, torons | rows 930-938; row 1200 Lemma M (`gap-mini-solve-j-fable.md`) | minimum action in the crossed-twist sector; abelian family A_perp(L) = 2 L^4 (1 - cos(pi/L^2)) | a commutator held at a central value: flux half |
| OpenAI O(n) annulus engine | `gap-direction3-max.md` L190-197 (row 1007 B(2)) | "an additive gradient of non-commuting rotations is gauge equivalent to a commutator field"; commutators of plane waves on frequency shells add coherently to the twist while costs add incoherently | this is the owner's idea in 2D, for a twist (flux-type) quantity |
| Port of that engine | row 1046 Lemma TAN; row 1188 Lemma PC (`gap-mini-solve-a-fable.md`); row 1228 Prop P5 | identity holds on the pin space; cost of a commutator profile on a 3D slice is at least lambda^2 eta^2 N; plate twists squeeze under tiling | the commutator-as-twist mechanism has no 4D gain |
| Rigid symmetries | row 1016 Lemma CEN+ (`gap-pinned-cell-gauge-check-astra.md` L52-96 corrects CEN) | every trace-preserving family of single-link maps is a gauge transformation times a closed Z_2 field | block rotations that preserve the weight are gauge times central |
| Box symmetry group | row 1201 (`gap-mini-solve-k-fable.md`) | spatial rotations as a rigid non-abelian group; no stiffness | the spatial reading of the dream |
| Several directions kill association | `gap-face-stability.md` L308; `gap-face-exercise-fable.md` L934 | OpenAI's (3.6) and the Ginibre step fail for a sheet with pins of several directions | multi-direction pins are an obstruction for the neutral half by association |
| K_3 commutator frustration | row 1241 (`gap-mini-solve-y-opus.md`) | at Gaussian order K_3 is massless; the commutator frustration is cubic, not a decay mechanism | one neutral commutator route closed |
| Small-volume neutral gap | row 998 I33 (`gap-crux-exercise3-max.md` L218); row 1003 item 14; `gap-brainstorm-max.md` idea 36; `gap-council-rg-fable.md` L209; `gap-council-conf-fable.md` L159 | Luscher (1983), van Baal: in a small periodic box the zero-flux gap is about 4.1167 g^(2/3)/L; held as BELIEF; "z tends to 0 at small L" | the commutator potential of the constant modes is the neutral-half mechanism at small volume; it is on file only as a recalled belief, not as a lattice lemma |

Not found on file: (i) a literal multi-direction block with its gauge-invariant content worked out; (ii) the
question whether non-central commutators act inside the neutral sector; (iii) a hand proof that the commutator
potential of the constant modes, and not the twist, is what U(1) lacks in the neutral half.

**Plan (at most eight steps).**
1. This search (done).
2. Literal model: what a multi-direction block (MDB) is on the lattice; which of its data are gauge invariant
   (junction invariants). Elementary lemmas, PROVED or killed.
3. The commutator question as operators on the transfer-matrix space: do MDB operators and their commutators
   act inside the neutral sector, and how does that differ from the centre twists? PROVED or killed.
4. The commutator question as energy: the commutator (quartic) energy of an MDB, its dichotomy (central
   commutator = flux sector; non-central = curvature), its scaling with block size, and the fact tests (U(1),
   frozen Q_8 and 2T, products with a free photon).
5. The neutral mechanism at one block: a hand-provable reduced (Simon-type) lemma that the commutator potential
   gives a discrete spectrum and a gap on the neutral constant modes; what it does and does not give on the
   lattice.
6. Tiling: can a tiling of MDBs carry the one-block mechanism to the size that (N-phys) needs? Attack it as a
   real proof; name the first failing step.
7. Two further distinct attacks on that failing step, if the first fails.
8. Verdict and RESULT line.

**Moves (rule 0):** (N-phys), the neutral half of the gap clause (rows 1161, 1179, 1180). If the MDB commutators
give a selective neutral engine that crosses the band, (N-phys) moves; if they provably act only at small volume or
reduce to the block RG through the band, that closes the owner's idea as a route and says why.
