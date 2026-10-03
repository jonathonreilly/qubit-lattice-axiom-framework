*(Saved by the coordinator from the agent's final message; the agent's sandbox blocked it from writing REPORT.md.)*

# A33 report: can the calm empty background supply the π-flux pattern that light-like matter needs?

**Paths.** SP = `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad`. All scripts and outputs are in `SP/c8/A33/`.

**Housekeeping.** No git, no repo edits, no review or audit lanes. I did not write a REPORT.md file because my harness forbids subagent report files; this message is the report.

**Reused code (cited).** A20's `grp.py` (the 24 soldered turns, `label_map`) and `pauli.py` (exact Pauli strings with phases). `p2lib.py` loads them by path, because A20's `grp.py` clashes with the stdlib module `grp`. The single-defect mobility test re-implements A31 `c5`'s F₂ rank test (`p2_tests.mobile_moves`).

**Grades.** EXACT (proof or exact F₂/Pauli arithmetic), CHECKED (numerics in a stated toy), ARGUED, SUPPLIED, COMPARATOR (literature from memory, never adopted). All models are supplied toys.

## 1. Question

Is there a vacuum Ω on Z³ (one qubit per site, ordinary tensor product) with four properties?
1. **Calm under a pattern-free law.** Ω is an exact eigenstate of a homogeneous, soldered-covariant, short-range (preferably frustration-free) law.
2. **Pattern at state level only.** Ω may keep only 2Z³ of the translations, giving 8 translates like F6.
3. **Mobile excitations.** A single defect can be moved by local operators.
4. **Vacuum-supplied π flux.** The movers' plaquette commutator is −1, so the excitations get a light-like cone.

Method: exact F₂ (stabilizer) searches.

## 2. Answer

**No, inside every class searched, and for a structural reason that is EXACT and covers far more than the searches.**

- **Theorem C (EXACT).** Take any pure stabilizer vacuum on Z³, of any period and any number of qubits per cell, whose local checks are independent: as many check orbits per unit cell as qubits. Then no superselected excitation, single defect or composite, can move in three independent directions. At best it moves in a plane.
  - This class includes every translation-invariant vacuum with one qubit per site.
  - It also includes every period-2 vacuum with one check per site, or one per fine cube, at any range.
  - Moving in 3D needs more checks than qubits, tied by local relations. That is a gauge-type structure (Gauss law plus a Bianchi-type identity), like the toric code.
- **Theorem A (EXACT).** In a translation-invariant vacuum covariant under the 12 tetrahedral or 24 cubic turns, a single defect cannot move at all, by any vector, at any degree. This extends A31 D14 from the star and face states to A20's whole module and beyond.
- **Period-2 searches (EXACT for the stated finite classes; §3).** Two classes were searched:
  - one role-dependent check per site, at radii |d|² ≤ 2, 3, 4 (77,665 commuting, exactly covariant candidates at |d|² ≤ 4);
  - up to two checks per role, so redundant checks are allowed, at |d|² ≤ 2 and 3.

  No pure covariant vacuum in either class has a single defect that moves in 3D. Every candidate that did have 3D-mobile defects carries an exact impurity certificate: its checks leave a local qubit free. No pure vacuum with redundant checks exists in the second class at all.
- **What the vacuum can supply (EXACT, positive).** It can supply π flux, but only to excitations that move in planes.
  - In a covariant, pure period-2 "layer" vacuum, a single defect moves in planes, and its elementary loop equals exactly one check. With the uniform covariant law sign s_E = −1 it sees π through every square plaquette. That gives 2D Dirac cones inside layers and no velocity along the normal.
  - In the translation-invariant star vacuum with S = −1, an 8-defect planar composite sees π per triangle. That only flips the hop sign: one band, no cone.
- **New open route (EXACT symmetry statement; realization OPEN).** Theorem S assumed matter carries trivial site quantum numbers.
  - For any non-fractionalized excitation with one state per site, the flux through a plaquette is |t|²|t′|²·p(x)p(c). Here p is the excitation's parity under the half-turn about the plaquette diagonal, at the two corners x, c that the half-turn fixes.
  - In a period-2 vacuum, π on every face is symmetry-allowed if the parities differ between vertex/face and between edge/cube roles. So a state-level pattern is not excluded from supplying the KS pattern.
- **Calmness (EXACT).** Calm period-2 vacua exist: every pure one-check-per-site vacuum at |d|² ≤ 2 has covariant sign choices with a homogeneous, frustration-free, covariant law. One of them (#87) is star-local and passes the quiet test, but its defects are immobile.

## 3. Derivation and search

### 3.1 Theorems

**Theorem C (EXACT).** Setup:
- Γ ≅ Z³ is the translation lattice of Ω (Z³ or 2Z³), and R = F₂[y₁^±, y₂^±, y₃^±].
- There are t qubits per Γ-cell. The checks are the Γ-translates of t local Paulis, assembled into σ: R^t → R^{2t}; the syndrome map is ε = σ^†λ.
- Purity means M = M^⊥, i.e. ker ε = im σ. With t generators of a rank-t module, σ is injective, so M is free.

Proof:
1. The sequence 0 → R^t → R^{2t} → R^t → C → 0 is exact, so the charge module C has projective dimension ≤ 2.
2. At every maximal ideal m, Auslander–Buchsbaum gives depth C_m ≥ 3 − 2 = 1. So C has no nonzero finite-length submodule.
3. If a nonzero class s (a pattern not creatable locally) could move by a rank-3 set of vectors, then (1 + y_i^n)s = 0 for i = 1, 2, 3. Then R·s would be a quotient of R/(y_i^n − 1), which has finite length. Contradiction.
4. So the move set has rank ≤ 2. Moves that change check type are covered by pigeonhole over the finitely many types.

**Theorem A (EXACT).** For a translation-invariant vacuum with one qubit per site:
- The stabilizer module is principal, Ru with u = (a, b) coprime (a reflexive rank-1 module over a UFD is free).
- A soldered 3-fold turn forces the label sum u(1,1,1) = 0, so a single defect is never creatable locally.
- Theorem C (or Krull's height theorem) bounds its move lattice Λ to rank ≤ 2.
- Covariance makes Λ invariant under T or O, which act irreducibly on Q³. So Λ = 0.
- The same argument holds for cube-centred checks.

**Unmixedness (EXACT).** (a, b) is a regular sequence, so R/(a, b) has no embedded points. Hence even composites move at most in planes.

**Additional exact facts.**
- **No covariant one-site stabilizer (EXACT).** Vertex and cube sites: the 24 turns would generate all three σ's. Edge and face sites: the quarter turn swaps σ^b and σ^c, and the perpendicular half-turn flips σ^axis. This gives a cheap impurity test.
- **Edge lemma (EXACT, by hand).** At an edge-role site, two face-centred 4-site flux checks that are quarter-turn images of each other share only that site. They commute only if both use σ^axis, the same label as the vertex stars there. So a covariant "toric code on edge roles" leaves the edge qubits single-label, i.e. a classical code. This is the mechanism behind every impure-but-mobile candidate. Example: #75 at |d|² ≤ 2, where vertex defects move by one-site Z movers but the plaquette loops are free local qubits.
- **Linear translations for local excitations (EXACT).** Locally creatable excitations in a Γ-invariant vacuum carry linear Γ-translations, so they get no projective plaquette phase on Γ.
- **Parity formula (EXACT).**
  - Setup: a turn g fixes corners x and c of a plaquette, the law is invariant, and g|y⟩ = p(y)|gy⟩.
  - Result: Φ = |t(x,a)|²|t(a,c)|²·p(x)p(c).
  - For the period-2 role layout, π on every fine face holds exactly when p_V ≠ p_F and p_E ≠ p_C, under each face's diagonal half-turn. Theorem S is the case p ≡ 1.

### 3.2 Searches (all exact for the stated class)

**Translation-invariant class (`a1`).**
- Site-centred, O, |d|² ≤ 6: 127 shapes, 45 pure covariant states.
- Cube-centred, |y−c|² ≤ 6.75: 63 shapes, 0 pure.
- Tetrahedral only, |d|² ≤ 3: 15 shapes, 15 pure.
- All 60 pure states: single defect not creatable and 0 movable displacements on L = 4, 6, 8, as Theorem A says.
- Quiet test: only the star and its tetrahedral twists have a check inside one star. The other 44 O-covariant states have maximally mixed star marginals, so no formation weight can annihilate them.

**One check per site, period 2 (P2-A).** Roles are vertex, cube, edge (axis) and face (normal), with site groups O, O, D₄, D₄.

| Class | Candidates (commuting, exact sign) | Outcome |
|---|---|---|
| \|d\|² ≤ 2 | 157 (3 translation-invariant) | 129 certified impure, including all 12 with movers on L = 4, 6, 8. 28 pure-looking, all immobile on Z³. |
| \|d\|² ≤ 3 | 697 | 633 impure, including all 36 mobile. 64 pure-looking, all immobile. |
| \|d\|² ≤ 4 | 77,665 | see breakdown below |

Breakdown at |d|² ≤ 4:
- 70,769 have a one-site logical.
- 472 are certified in a 3³ box, 260 in a 5³ box and 168 in 6³/7³ boxes. These 168 include all 160 with explicit rank-3 Z³ movers (face 96, edge 24, vertex 24, cube 12, cube+vertex 4).
- 5,912 are immobile on L = 6, 8 or 10.
- 60 are planons with explicit in-plane movers and no certificate.
- 24 have no move shorter than 8: on L = 16 they move only by half-torus vectors (fractal-like torus behaviour).

**Redundant checks (W class).** Up to 2 checks per role, |d|² ≤ 2: 452 combinations. 444 are impure; the other 8 have exactly 8 checks per cell, so they are free modules, and they are immobile. At |d|² ≤ 3: 5,392 combinations, 5,376 impure, 16 with 8 checks per cell, all immobile.

### 3.3 Flux (EXACT, exact Pauli algebra)

- **Layer vacuum (`a20`).** Shapes (1,1,1,1) at |d|² ≤ 4. It decouples into pure pieces: stars on the vertex and cube sublattices, and planar twisted stars in sublattice layers.
  - The edge defect hops by 4 sites in-plane with one-site movers.
  - Its loop W equals the single edge check at the plaquette centre, with c = +1, so the loop phase is s_E.
- **Star planon (`a22`, `a23`).** The parallelogram loop is two stars (phase +1). The triangle loop is one star (phase S).

### 3.4 Calm (`a18`, `a19`)

- **Site-centred projector law.** The site-centred projector ∏(1 − s g_o)/2 over the 8 translate checks is nonzero for 2 or 4 of the 16 covariant sign choices, in all 28 pure-looking states at |d|² ≤ 2 (EXACT).
- **#87.** Ordinary star at vertex, cube and edge sites; σ^c on all six arms at face sites with normal c.
  - With s = (1,1,1,1) its law is star-local, and it passes the quiet test at every role.
  - The same law also has the translation-invariant star as a ground state (EXACT), so the law does not pick out the pattern.
- **General lemma (EXACT).** If a ball holds at least 4 independent checks of every translate, then the dimension count 8·2^(|B|−4) < 2^|B| gives a nonzero covariant P_{W⊥}. So a covariant frustration-free law exists at some range for every pure period-2 vacuum.
- **Records (EXACT for translation-invariant covariant vacua).** Records all along one fixed axis see uniform odds on any finite set, because t·a = 0 forces t = 0.
- **Records in #87 (ARGUED).** z-records on the six arms of a face site with normal z have a fixed product, so they would tell the translates apart.

## 4. Checks

| Script | What it does | Key numbers |
|---|---|---|
| `a0_libtest` | library self-test | invariant-shape dimensions 1, 2, 2, 3, 5, 7 by shell; star and face exactly invariant |
| `a1_ti_class` | translation-invariant class | 45 / 0 / 15 pure states; 0 moves on L = 4, 6, 8; star k(L) = 4L, face k(L) = 16L − 24 |
| `a2*` (`a2d` is the fast solver) | P2-A searches | 697 → 157; 2745 → 697; 77,665 at \|d\|² ≤ 4 in 2.0 s |
| `a3`–`a7` | P2-A screen and classification | as in §3.2 |
| `a8`, `a11`, `a13`, `a14`, `a16`, `a17` | \|d\|² ≤ 4 pipeline | as in §3.2 |
| `a10_mover` | explicit Z³ mover search | validated: layer move (0,4,0) found, (4,0,0) correctly rejected; one-site movers for #75 |
| `a15`, `a12` | #1048 inspection and move sets | 3D-mobile face defect; certified impure in a 6³ box; k(16)/N = 0.165 (extensive) |
| `a21_wyckoff` | redundant-check class | as in §3.2 |
| `a18`–`a23` | calm, flux, composites | as in §3.3 and §3.4 |

**Run conditions.** Every run went through `run.sh`: `nice -n 10`, all four thread caps at 1, a 55 s alarm, and a load gate at 6 (four runs were skipped at load 6.6–7.1 and rerun). Every run took ≤ 52.3 s and used ≤ 58 MB.

**Lessons, recorded honestly.**
- `a2b` at |d|² ≤ 4 hit the alarm; it was superseded by `a2d`.
- `a10` had a false-positive bug (a defect check not touching the box was dropped). It is fixed; negatives were unaffected.
- 5³ boxes missed impurity for radius-2 shapes, so the |d|² ≤ 4 candidates were re-certified with 6³/7³ boxes (`a16`).
- "Pure-looking" means no certificate in boxes up to 4³ (|d|² ≤ 3) or 7³ (|d|² ≤ 4). That is CHECKED, not proved.

**Exactness logic.** Immobility on any even torus larger than the checks implies immobility on Z³, because a Z³ mover wraps to a torus mover. Movers found inside a box on Z³ are exact. Impurity certificates are anticommuting pairs inside a box, each commuting with every Z³ check.

## 5. Real-physics match (comparators flagged)

- **Theorem C** matches the known lore that 3D mobile point charges need gauge structure. COMPARATOR: 3D toric code, with 4 checks on 3 qubits per cell and one cube relation per cell. COMPARATOR: Haah 2013 polynomial formalism; I did not check whether Theorem C is stated there.
- **Excitation types seen** match fracton models:
  - immobile defects, lineon dipoles and planons (COMPARATOR: X-cube, Vijay–Haah–Fu);
  - layer anyons (COMPARATOR: Wen plaquette model);
  - half-torus mobility on tori of side 2^k (COMPARATOR: fractal codes, Yoshida 2013).
- **The π flux** found is the toric-code background-charge mechanism (COMPARATOR: Wen's projective symmetry groups). The parity escape echoes symmetry fractionalization and staggered fermion symmetry (COMPARATOR: Kogut–Susskind, Kluberg-Stern et al.).
- **Falsifiers.**
  - A pure covariant vacuum with independent checks and a 3D-mobile charge would contradict Theorem C. It is excluded by proof.
  - A pure covariant vacuum with redundant checks and π-flux charges would answer this lane yes.

## 6. Open edges

1. **Redundant-check covariant vacua beyond W(|d|² ≤ 3, ≤ 2 checks per role):** larger radii, checks centred on bonds, cube centres or plaquettes, or period 4Z³. Theorem C says this is where 3D mobility must live.
2. **The parity route (most promising).** A calm vacuum such as #87, plus local excitations that are pseudoscalar (A₂) at vertex and cube sites and diagonal-even at edge and face sites, plus a calm, covariant, translation-invariant hop law. Then compute the 8-band spectrum, and check whether bond-type magnitudes |t_VE|, |t_EF|, |t_FC| gap or split the KS cone.
3. **The 24 fractal-like states:** decide whether they move by vectors in 8Z³, via an algebraic charge-module computation.
4. **Exact purity proofs** for the 60 planar and 64 + 28 pure-looking states.
5. **Non-stabilizer calm vacua.**
6. **Explicit construction of calm projected hop laws.**

**Owner decisions.**
- Whether matter may carry role-dependent site quantum numbers in a 1-of-8 state pattern (this would also reopen sharing with F6).
- Whether a uniform law sign such as s_E = −1 is acceptable as a homogeneous choice.

## 7. Plain-language summary

I tested whether calm empty space could, by its own arrangement, give moving disturbances the twist they need to travel like light, without that twist being written into the rule. The test used a large family of tidy, exactly solvable arrangements, all treating every site and every turn of the grid alike. In every tidy arrangement where each site carries one independent condition, a lone disturbance can never travel in all three directions. At best it slides within flat sheets, and that is proved, not just searched.

Inside those sheets the empty space really can supply the twist. A uniform choice of sign in the rule makes a disturbance circling any small square pick up the needed half-turn, but this only gives sheet-bound motion, never light-like motion in all directions. To move freely in three directions, the background would need more conditions than sites, linked to each other the way electric charge and magnetic field are linked. None of the tidy, turn-respecting versions of that I could build stayed fully settled. Some quiet backgrounds with an 8-fold pattern do exist; their disturbances cannot move.

The open hope is a different mechanism: an ordinary local ripple that behaves differently on the different sub-grids of an 8-fold patterned background. The grid's symmetries no longer forbid such a ripple from feeling the twist everywhere, but nobody has built one yet.