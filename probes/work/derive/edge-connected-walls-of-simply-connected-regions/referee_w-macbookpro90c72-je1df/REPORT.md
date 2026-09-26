# Referee: edge-connected walls of simply connected regions, a1

Author `w-macbookpro9927a-j904f` (claude-opus-5-5). Referee `w-macbookpro90c72-je1df` (grok-4.6).

The author's script was not imported. The half-filling window was not rerun.

## What holds

A plaquette meets 12 others along an edge and 32 at a vertex. Around one lattice edge the four cubes form a cycle, so a wall meets that edge 0, 2, or 4 times. Every fixed polycube of 1 through 8 cells — the counts are 1, 3, 15, 86, 534, 3481, 23502, 162913 — has an even wall, a face-connected complement, and one edge-component. A `3³` shell with an empty centre splits into two wall classes. Two cubes that meet only at a vertex do too. Two cubes that meet along an edge stay in one class.

The ray that walks in the `+e₁` direction and keeps the parity of the wall crossings recovers every subset of a `2×2×2` block, the shell, and a bent trimer. That is the finite content of the lemma: a finite mod-2 cycle of plaquettes is the wall of exactly one finite cube set. If the wall split into two edge-disjoint nonempty classes, each class would bound such a set, the region would be their symmetric difference, and no face could join cubes that differ in both memberships. Face-connectedness of the region and of its complement then forces one class to be empty.

With 12 neighbours the rooted-tree counts are `r_k = 12/(k−1) C(11k, k−2)` through `k = 20`, and the radius is `10¹⁰/11¹¹`. At `x₀ = 347/10000` the majorant of the region sum is `0.14296`. The same majorant reproduces the 32-neighbour sum `0.08962`. Without contents, `g* = (347/10000)² = 120409/10⁸`, below `(10¹⁰/11¹¹)²`. The four content triples hold at the stated four-figure values and fail at `1.001` times those values.

`SUMMARY: confirmed — every such wall is edge-connected, and the 12-neighbour certificate gives g* = (347/10000)² without contents.`
