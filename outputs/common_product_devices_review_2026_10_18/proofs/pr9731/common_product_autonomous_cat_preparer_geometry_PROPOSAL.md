# Explicit cubic placement of the standalone cat-preparer network

New source-exposed author construction requiring distinct review. This closes the combined cubic nearest-neighbor placement left open in d4e708: A1 is one physical qubit with six distinct neighbors, all ten paired cables have equal lengths within each gap, and all four infinite external rays are disjoint. The layout is deliberately large and not optimized. It does not close the complete packet, finite endpoint-seed preparation, or receiving-gadget handoff interfaces.

The exact coordinate manifest COORDINATES.json is part of this construction. Its axis_aligned_corners lists specify every cable: between consecutive corners include every integer point on the straight coordinate segment, counting a common corner once. All blocks and signs inside each translated writer/core/splitter are those of d4e708 and its pinned local sources. The deterministic validator expands all such paths before checking them. No long-range interaction is installed along a corner-to-corner jump; it denotes an entire ordinary nearest-neighbor cable.

## 1. The shared A1 writer and final core

Set A1=(0,0,0). Put the core endpoint heads at

    I0=(-1,-1,0), O0=(1,-1,0),
    I1=(1,1,0), O1=(-1,1,0).

The four mediator heads are the square-edge midpoints(0,-1,0),(1,0,0),(0,1,0),(-1,0,0). Each connects to its two adjacent endpoint heads and to A1 with the original programmed mediator block. The straight/cross coefficient assignments retain the labels of76b5, so the core comparator remains C_0=X_path,C_1=I_path. Endpoint on-sites and repeated vacancy repairs are retained without change. The program has not been copied.

Use the literal writer93445 with its target at its local origin, and map every local coordinate by

    (x,y,z) -> (z,y,x).

This is an isometry of the cubic graph, allowing a reflection. It preserves every length and installed sign. Call the resulting branch1 stage1 writer w11. Its two terminal heads are(0,0,1) and(0,0,-1), both adjacent to the SAME A1. Its port origins are w11.in=(0,8,0) and w11.out=(1,8,1). Its two arms are explicitly the images of

    arm0: (1,0,0),(2,0,0),(2,1,0),(1,1,0),
                                      (1,2,0),...,(1,8,0),
    arm1: (-1,0,0),(-1,1,0),...,(-1,8,0),
                                      (-1,8,1),(0,8,1).

The four writer-junction bonds connect those arm ends to the two writer ports. Both positive phase-cell repairs stay on the transformed arm1 edges corresponding to local y=2--3 and5--6. The target contacts remain j n_T(I+X_A1). All24 writer heads are distinct from the eight core heads and A1. For example the writer's near-origin excursions are at z=+-1 or2, while the core is in z=0; the only transformed writer heads in z=0 lie at y=8, away from the core.

Thus the six installed neighbors of A1 are EXACTLY

    (+-1,0,0), (0,+-1,0), (0,0,+-1).

The first four are core mediators and the final two are writer terminals. There is no geometric degree obstruction, no duplicate target, no unlisted interaction through a seventh neighbor and no claim that degree counting alone proves the placement. The displayed coordinates and the full validation below establish it.

## 2. Other writers and splitter

For the seven remaining writers retain the literal local orientation and translate by(x0,0,0):

| Writer | Stage/branch | x0 | Target |
| --- | --- | ---: | --- |
| w10 | 1/0 | 100 | scalar specialization, no target qubit |
| w20 | 2/0 | 200 | scalar specialization |
| w21 | 2/1 | 300 | A2=(300,0,0) |
| w30 | 3/0 | 400 | scalar specialization |
| w31 | 3/1 | 500 | A3=(500,0,0) |
| w40 | 4/0 | 600 | scalar specialization |
| w41 | 4/1 | 700 | A4=(700,0,0) |

Every scalar branch has terminal onsite2j n_T instead of a target contact; an unused target coordinate is NOT a physical dummy qubit. Each translated input port is(x0,8,0) and output is(x0+1,8,1). Their respective first escape paths are along y from8 to20 at(x0,y,0), and along x from x0+1 to x0+20 at(x,8,1). These paths do not meet internal writer heads. The shared writer w11 uses its input y escape from(0,8,0) to(0,20,0); its output rises directly in+z from(1,8,1).

Put the splitter at

    split.I0=(1000,0,0), split.I1=(1001,1,0),
    split.O0=(1001,0,0), split.O1=(1000,1,0).

Install its four signed unit-square bonds and four positive vacancy repairs exactly as in d4e708. All these module vertices and four targets are pairwise distinct, except the intentional A1 role shared between w11 and the core. There are204 module heads and four target qubits, totaling208 before cable interiors.

## 3. Complete cables and external rays

Connect the ten port pairs listed below. The manifest provides all corner coordinates; heights and edge lengths are summarized here. Within each stage gap the two lengths agree exactly, even though the height differs.

| Gap | Branch0 connection / height | Branch1 connection / height | Common length L_a |
| --- | --- | --- | ---: |
| 1 | split.O0 -> w10.in /10000 | split.O1 -> w11.in /9952 | 20935 |
| 2 | w10.out -> w20.in /20000 | w11.out -> w21.in /19900 | 40122 |
| 3 | w20.out -> w30.in /30000 | w21.out -> w31.in /29999 | 60222 |
| 4 | w30.out -> w40.in /40000 | w31.out -> w41.in /39999 | 80222 |
| 5 | w40.out -> core.I0 /50000 | w41.out -> core.I1 /49952 | 100648 |

Each cable first follows its stated short module escape, then rises vertically at a unique(x,y) post to its assigned height, follows its manifest planar path there, descends at the other post, and reverses the other short escape to reach its endpoint. The core and splitter ports use zero-length short escapes. Every cable edge carries an ordinary Q_j block. No new program/data qubit is used by a cable.

For reproducibility the manifest's planar paths were selected by deterministic breadth-first search in the rectangle[-20,1030]x[-20,40], avoiding every other post coordinate. Neighbor order is(+x,+y,-x,-y). At a gap, branch0 height is10000 times the gap number. Branch1 height is set to equalize total cable lengths, including escape lengths and differing post heights. The parity difference is even in every case. When equal heights would result, one two-edge planar detour is inserted into branch1 and its height reduced by one. The detour's vertices avoid the planar path and all posts. The stored corners, not an arbitrary choice of a new BFS path, define the frozen construction.

The four remaining external rays are

    split.I0+(0,0,n), split.I1+(0,0,n),
    core.O0+(0,0,n), core.O1+(0,0,n), n=1,2,... .

Their origins are already module heads. Their(x,y) coordinates are distinct. Every finite module/cable vertex on one of these four vertical lines has z at or below its origin; this was checked against the complete finite vertex set. It follows analytically that the entire infinite continuations, not just sampled prefixes, miss the finite construction. They also miss one another because their(x,y) coordinates differ. Radial coordinate n starts at each respective origin, so the geometric bends in internal cables do not change the external plane-wave convention.

Every internal horizontal cable lies at a distinct height above all modules. Its planar route avoids the posts of all other cables and external rays. Thus it cannot intersect their vertical legs. Short escape paths are disjoint from modules except at their own port endpoints and from all other escapes. The explicit expansion verifies these facts rather than inferring them merely from a schematic projection. Incidental nearest-neighbor adjacencies between vertices carry NO interaction unless a module edge or cable/ray edge is listed. Absence of such unwanted couplings remains the supplied-block premise.

## 4. Phase, counts, cap and exact inherited scope

The cable lengths sum to302149. Therefore d4e708's exact ideal common forward/reverse scalar is

    z^(90+sum L_a)=z^302239.

The ordered full-fiber ideal word remains C_A1 W4 W3 W2 W1 H_path, sending |0,0000> to |1>cat+. All paired stages have exactly equal cable phases. The physical common vacancy scalar remains8b+36(sqrt(2)-1)j, since cable bending adds only ordinary Q_j blocks and no extra vacancy repair. Geometric placement introduces no independently fitted branch phase.

Each L_a-edge cable adds L_a-1 interior heads; there are two cables per gap. Hence the finite module/cable section has

    208+2 sum_a(L_a-1)=604496 qubits,
    304+2 sum_a L_a=604602 positive listed blocks.

These counts exclude the four external infinite rays and any future finite emitter/cap system. The geometry is a large FIXED component independent of a future error parameter; it is not a practical size claim or optimized layout. The validator confirms the finite vertex count including all four target qubits. Onsite repairs are counted by the inherited module inventory rather than miscounted as edges.

All interactions in this construction are nearest-neighbor or onsite, with real positive blocks from the original splitter/writer/core specifications. The shared target load is4(D1-2b)+4j, other target loads4j; cable interiors have4j, and module port loads include exactly one external cable/ray bond. Thus the d4e708 sufficient cap choice D1=Lambda/16, zeta<=1/4, eta<=1/8, j=eta^2 zeta D1 remains valid, along with its required stationary smallness6max(33d,13eta^2+5zeta)<1. No long-range primitive, entangled ancillary input or copied target has been added to solve the geometric problem.

The inherited stationary feedback proof is still conditional on its separate check. Placement changes neither the number of six stages nor ideal nilpotence of the ordered internal propagation; it only instantiates its cable phases. In particular the composition must still act on all16 target channels, because A1 is changed by its writer and later controls the core. Geometry does not justify a classical-program decomposition.

## 5. Deterministic verification and limits

The authored standard-library validator validate.py was executed successfully. It constructs the exact local modules and all target contacts, generates and fully expands ten cables, and asserts:

- every installed two-site edge has Manhattan length one;
- module and target sites are distinct, except the one deliberately reused A1 identity;
- every cable is simple and its interior avoids every module, target and other cable;
- all five paired lengths agree;
- A1's neighbor set is exactly the six directions displayed above;
- the maximum installed geometric degree, including the four external first edges, is six;
- no vertex lies above an external ray origin on its line, proving the infinite-ray condition;
- the finite vertex count equals198+2sum L_a.

The output RESULT.json records the successful assertions and numeric summary. COORDINATES.json retains every module/target site, port, cable corner list and local installed edge, so another checker can reconstruct the graph without using the search algorithm. The validation is geometry and bookkeeping only. It does not validate scattering coefficients, packet completeness, preparation success, timing or a physical implementation of selective couplings. It is this author's deterministic check, not an independent review.

Open work is now the modified network's full normalized packet/internal derivatives and actual finite product-endpoint seed/cut transfer. Neither is obtained from the coordinate check or by reusing970a unchanged. Large cable lengths affect derivative and timing constants and must be paid. A separate receiving-gadget attachment remains unresolved: the prepared targets here have no permanently coupled ZZ penalty or receiving data interactions. No handoff, capture, reset or permanent halt is asserted.

## 6. Frozen evidence and exposure

All new files are under N/common_product_autonomous_cat_preparer_geometry, with N=/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934.

- validate.py SHA25608c24b6d0f3bdc738c76946608ce13338825b2c869cedc4c7dd3b51a126bdceb.
- COORDINATES.json SHA256f8b3c4579e82abd999ebacd403b0fd040d101d37b8f43301c287ff247bcaecc5.
- RESULT.json SHA2564a136378609119999a12b41ac97e31d2cc284dd5261da5bab10bc619e1ffdd2a.

The parent stationary source common_product_autonomous_cat_preparer/PROPOSAL.mdd4e708583626102d5f09d6f98c56e25fadb36895fdb437d07b69c0e345ef96af was authored, fully read and frozen immediately before this task. Its standalone scope and complete source identities are unchanged. The writer93445d7d52e32859c980f0a0ebc6024238bedc7571d09e145ab1b128d8292f56 was completely reread there; the arm and junction coordinates used here are exactly that source's isometric images. Core76b5fd9bdf7a1609dfbc981211a508991a6a24c53686e26f28907210007e1b01 and60bc91b6ad085a722b3805de1d1b0d93a9cabcf77b1c3f5a74e43045354c3182 retain their full relevant geometry/operator reads and the scoped checks identified in d4e708.

ROOT requested closing the actual six-neighbor A1 geometry and equal paired routing, rather than assuming a generic embedding. This author chose the reflected writer, explicit translations, escape posts, layered cables and deterministic validation after that exposure. This is source-exposed same-model author continuation. A distinct review should inspect the actual path manifest, all shared-site identities, source-to-module indexing/sign inheritance, infinite rays, edge/block distinction, counts and common phase before accepting this geometry interface.

Only this proposal and its expressly authorized coordinate validator/outputs were created. No scientific dynamics simulation, numerical sweep, delegation, old source/W/Git/checkpoint/axiom/editable-prompt/model change or publication occurred. Failed abstract geometry assumptions were not promoted to a universal obstruction; they were replaced here by an explicit placement, while the genuinely separate finite preparation obligations remain open.
