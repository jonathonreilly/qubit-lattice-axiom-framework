**A56 report: cube-interface gains are additive on faces, but the L adds an edge contact the estimate left out**

## 1. Verdict

- **Face interfaces add up almost exactly, slightly better than additive (EXACT).** Three cubes in a line gain 4–5% more than two separate face interfaces, under both rules. Faces show no monogamy.
- **The L gains much more than face-additive (EXACT).** δ_L is −0.127 under B4_inner and −0.162 under B4_r4. The reason is that the L's two arm cubes share an edge, and they couple through the 011 bonds across it. The face-only estimate never credited that contact. On its own, an edge pair gains 0.67 (inner) or 0.75 (r4), which is 3.7–4.4 times a face. Inside the L, monogamy cuts that gain by about 80%.
- **The near-tie stays open (ARGUED).** The −1.722 estimate is uncontrolled rather than simply optimistic. Cube-cluster increments do not converge at three cubes.

## 2. Table (total energies, J_NN = 1; per-site values in parentheses)

| | B4_inner | B4_r4 |
|---|---|---|
| E_cube | −13.236749 (−1.654594) | −13.269320 (−1.658665) |
| E(2×2×4), A53 check | −26.653080 (−1.665817) | −26.710645 (−1.669415) |
| Δ (face) | −0.179581 | −0.172005 |
| E_add = 3E_cube + 2Δ | −40.069410 | −40.151970 |
| **E_line** (2×2×6) | **−40.085114** (−1.670213) | **−40.168353** (−1.673681) |
| **δ_line** | **−0.015704** | **−0.016383** |
| **E_L** | **−40.196883** (−1.674870) | **−40.314397** (−1.679767) |
| **δ_L** | **−0.127473** | **−0.162427** |
| Δ_edge (two cubes sharing an edge) | −0.666518 | −0.749491 |
| δ_L − Δ_edge (genuine three-cube part) | +0.539045 | +0.587064 |

- **Other pairs.** The corner pair gives Δ = −0.0006 (inner) and −0.00001 (r4). Two cubes one cube apart give Δ = 0 exactly, because no rule term reaches a component of 3. So δ_line is a purely three-cube effect.
- **Other three-cube shapes (B4_inner only, EXACT, pass 1).** These give the genuine three-cube increment δ3:

| Shape | Contacts | δ3 | Per site |
|---|---|---|---|
| tri_eee | three cubes, pairwise edge-sharing | +0.464 | −1.71857 |
| bent | face + edge | −0.026 | |
| fek | face + edge + corner | +0.009 | |
| ee90 | two edge contacts at 90° | −0.081 | |
| ee120 | two edge contacts at 120° | +0.009 | |
| ee180 | two edge contacts in a line | −0.057 | |

## 3. Implication for the near-tie (ARGUED)

- **Faces alone.** Crediting the line correction (3 lines per cube) moves the A53 estimate from −1.72194 to −1.72783 (inner, against the parton's −1.72681). Under r4 it moves from −1.72317 to −1.72931 (against −1.72841). Both land about 0.001 below the parton. On faces alone, the estimate was slightly pessimistic, not optimistic.
- **The edge channel decides it, and it does not settle.**
  - Each cube has 6 edge contacts. Crediting them alongside faces at pair level gives −2.222 per site.
  - In the L, the edge bonds close frustrated triangles with the corner cube's nearest-neighbour bonds. The arm-to-arm ⟨σ·σ⟩ is −0.51, against −1.12 for an isolated edge pair. That is where the monogamy sits.
  - Adding all eight three-cube shapes (inner) adds +8.63 per cube, which gives −1.143 per site. That is above even the bare cube product (−1.6546).
  - The face-connected truncation (3 lines + 12 L's per cube) gives −1.919 (inner) and −1.973 (r4). But it counts each edge contact twice; the 4-cube 2×2 square would correct that, and at 32 sites it is beyond this machine.
  - These truncations swing by 0.1–1 per site. That is 20–200 times the 0.005 margin.
- **Consequence.** No cube-increment count fixes the crystal's energy to the precision the near-tie needs. One pointer: the edge-rich 24-site open block tri_eee sits at −1.7186 per site, within 0.008 of the parton despite its open boundaries.
- **What could settle it.** A variational dressed-cube state that carries edge (011) correlations (A53's open edge 1). Contact-resolved 4-cube increments would also help, but need more memory than this machine has.

## 4. Checks (CHECKED)

- **A53 reproduced.** E_cube and E(2×2×4) match A53 to every printed digit under both rules.
- **Restricted rule.**
  - Pairs match an independent class enumeration exactly. The four-spin sets match the 10³-torus operator restricted to each block exactly.
  - Under inner, the line has 180 pairs and 88 four-spin sets, and the L has 216 and 100. Under r4 the counts are 132/88 and 136/100.
  - The L has 12 four-spin sets spanning three cubes. No set splits 2+2, so the cube-product energy equals 3E_cube to 1e−13.
- **Kernel.** My table kernel agrees with A53's `_matvec_gen` to 1e−12 at 24 sites, and runs at 0.9–1.1 s per matvec against A53's 2.1 s.
- **Lanczos.**
  - The start vector is the cube product plus 0.3 times a random singlet. Both are exact S = 0 states, so the Krylov space stays in S = 0.
  - The four main blocks ran two passes, with every α reproduced in pass 2. Their true residuals are 4–8×10⁻⁸, Σ⟨σ·σ⟩ ≤ 3×10⁻¹², and overlap with the cube product is 0.75–0.80.
  - The six extra shapes ran pass 1 only, with residual estimates below 10⁻⁷.
  - The 16-site Lanczos reproduces the eigsh values.
- **Runtime and memory.**

| Run | Runtime | Peak memory |
|---|---|---|
| chk56 ×2 | 15–18 s | 228–250 MB |
| line blocks | 183–207 s | 202 MB |
| L blocks | 232–268 s (inner L split over two calls) | 203 MB |
| extra shapes ×6 | 43–82 s | ≤222 MB |

  - I ran one job at a time at load 2.1–4.0 with 32–41% memory free. Nothing was SKIPPED.
  - I made no repo edits, git writes or PRs, and ran no audit or review lanes.

## 5. Plain summary

Three cubes in a row gain slightly more than two separate cube joins, so face contacts add up fine. Three cubes in an L gain much more, because the two arm cubes also touch along an edge, a contact the old estimate ignored. That edge contact is strong alone, but crowding by neighbouring cubes mostly cancels it, and the bookkeeping does not settle at three cubes. The parton against cube-crystal near-tie stays open.

Files are in `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A56/`:
- `NOTES.md`
- `a56lib.py`
- `chk56.py`
- `lz56.py`
- the `out_*.txt` run logs