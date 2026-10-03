Everything I need is in hand. The checks gave:

- Strict covariance fails in 2D: phase 0 never matches, 0/40.
- Every moved site is adjacent to a record (maximum distance 1).
- The small-island orbits circle clockwise.

All runs took under 2 s with peak RSS at most 172 MB. Here is the report.

# Lane report (agent A11): one-way flow along the walls of recorded regions

Scratch scripts are in `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A11/`. No git, no repo edits, no subagents. Every run used `nice -n 10`, all four thread caps set to 1, and a 60 s alarm. Each took under 2 s, with peak RSS at most 172 MB.

## 1. Question

Can a ticked, strictly local, reversible step act as the identity on bulk possibilities while carrying one-way flow along the walls of recorded regions? The step is required to be:
- a short cycle of nearest-neighbour pair transfers;
- one qubit per site;
- covariant over the cycle under proper rotations, up to cyclic relabelling of sub-steps;
- possibly handed.

A transfer into a locked (recorded) site does not happen. If such a step exists, the owner's "possibilities push one way" conveyor would live exactly on the surfaces of recorded regions and nowhere in open space.

Tasks: 2D construction and flow index; covariance and handedness; 3D; many-body index; interpretation.

## 2. Answer

**Conditional: yes in a supplied 2D toy, no on Z³ under the axioms' 24 rotations.**

**2D (supplied square-lattice toy), under the named reading SC.** Yes. **EXACT, and CHECKED.**
- A handed cycle of four sub-steps of full nearest-neighbour transfers (on a two-sublattice pattern, directions +x, +y, −x, −y) is exactly the identity on every site not next to a record.
- Around every recorded region, of any shape or size, including a single isolated record, it carries the open sites' content one way. That is exactly one qubit per cycle across any cut from the region to infinity, at two sites per cycle along a straight wall, clockwise for the right-handed schedule. The mirror schedule is the inverse cycle and reverses the flow.
- The amount is fixed by a bulk count: each open plaquette is circled by exactly one item per cycle. No local modification smaller than the region can change it.
- Covariance holds only up to cyclic relabelling of sub-steps. Strictly, the cycle is not covariant.

**3D (Z³, 24 proper rotations about sites).** No, under SC. **EXACT.**
- SC forces every sub-step to be invariant under the 180° face rotations about every site, because these are commutators of the rotation group. No nearest-neighbour pairing survives that, so the cycle contains no transfers at all.
- Under a weaker reading that only asks the flow pattern to be covariant, two exact results apply:
  - a lattice Ampère law gives every periodic facet of a record region the surface current K = M×n̂, where M is the bulk loop-area vector;
  - covariance forces M = 0, so no periodic facet and no straight axis hinge carries net one-way flow.
- Surface conveyors in 3D appear only when the law supplies a direction. I checked this with a layered cycle and a body-diagonal cycle. The axioms' rotation covariance excludes such a direction.
- Hinges between inequivalent low-symmetry facets remain OPEN.

## 3. Derivation

**Notation.**
- A *transfer* on a pair swaps the two sites' entire content (M₂(C) each), so it carries a site's shared possibilities, with their links, along with it.
- A *sub-step* is a set of disjoint pairs, transferred at once.
- *Lock rule:* a pair containing a locked site is skipped and acts as the identity on both sites.
- *Full cycle* U: the composition of the sub-steps. For transfer cycles, U is the permutation of site contents P_π, where π is a permutation of sites (EXACT).

### 3.1 The 2D cycle

**D1. Construction; bulk identity. EXACT.**
- A sites are those with x+y even. Sub-step j pairs each A site a with a+d_j, where d = (+x, +y, −x, −y). Each sub-step is a perfect matching.
- Content starting on an A site moves +x, −y, −x, +y. Content starting on a B site moves −x, +y, +x, −y. Both are clockwise unit-plaquette loops that return home.
- So U = 1 on the open grid, on the whole many-body algebra.
- Every plaquette is circled by exactly one item per cycle, clockwise. So the bulk winding count is μ_bulk = −1 (counterclockwise positive).

**D2. Straight wall. EXACT.**
- Take the locked region y ≤ −1. Row-0 A items have sub-steps 2 and 4 skipped (partner locked), and sub-steps 1 and 3 each move +x. They advance two sites per cycle.
- Row-0 B items and all of y ≥ 1 never pair with a locked site, so they keep their bulk loops.
- Result: one qubit crosses every cut across the wall per cycle, eastward. With the open side below the wall instead, the flow runs westward.

**D3. Islands. CHECKED (s = 1–6); straight portions EXACT by D2.**
- Around an s×s record block, exactly 2s+1 items move. They form one orbit that goes once around clockwise in 2s+1 cycles.
- For the 4×4 block, the orbit visits the adjacent open sites in angular order, one ring position per cycle (CHECKED).
- A single record carries a 3-site orbit: (0,−1)→(−1,1)→(1,0).
- **Light cone (EXACT).** An item's partner at each sub-step is the site it moves to, so its path stays inside its own plaquette. An item whose plaquette has no locked corner follows its bulk loop exactly. Hence every moved site is within Chebyshev distance 1 of a record. CHECKED: maximum distance 1 over 40 random patterns.

**D4. Loop-linking identity. EXACT, any schedule, any locks, any dimension.**
- Setting: a finite cut S (a curve in 2D, a surface in 3D) whose boundary avoids all item paths.
- Identity: Σₓ c_S(x→π(x)) = −Σₓ link(Lₓ, ∂S).
  - c_S counts the signed crossings of the straight move.
  - Lₓ is item x's actual path, closed by the straight segment back.
- Proof:
  - Each transfer moves two items in opposite directions across the same bond, so path crossings cancel gate by gate (a finite sum).
  - Path minus straight segment is a closed loop, whose crossing number with S is its linking number with ∂S.

**D5. The circulation around every record region is set by the bulk. EXACT; CHECKED.**
- Definitions, for a point P on no path:
  - ρ(P): full-cycle rotation number, the sum over items of the straight-chord angle x→π(x) around P, in turns.
  - μ(P) = Σₓ wind(Lₓ, P).
  - ρ_A(P): the rotation number computed from the items' actual sub-step paths.
- By D4, ρ_A(P) is the same at every such point, equal to μ_bulk = −1. Hence ρ(P) = μ_bulk − μ(P).
- **Record sites.** At a record site with no closed loop around it, μ = 0 and ρ = −1: one qubit per cycle, clockwise. This is EXACT for record sites deeper than two sites. It is CHECKED at every record site of 9 patterns, including isolated single records:
  - L-shape, plus, staircase;
  - a shell with a cavity and an inner island;
  - two islands;
  - random rectangles;
  - random sites at densities 0.08, 0.25, 0.5.

  All gave (ρ_A, ρ, μ) = (−1, −1, 0).
- **Open plaquette centres** give only (−1, 0, −1), meaning their own loop with no net flow, or (−1, −1, 0) where records enclose them.
- **Nesting.** A cavity's boundary circulates the other way, and the enclosing shell's outer boundary circulates like an island. The shell + cavity + island pattern gave orbit lengths 9, 23 and 33.
- **Robustness. EXACT.** Composing with any local transfer circuit whose reach is smaller than the region's inradius cannot change ρ at deep record points. A single record's 3-cycle is not protected in this sense.

**D6. Consistency with A1. EXACT.** Each island orbit crosses any full line twice, once each way. So the net flow through every full line is zero, consistent with A1 D10, D12 and D30. What exists is circulation (A1 D32), not a net conveyor.

### 3.2 Hand and covariance (2D)

**D7. Handed. EXACT; CHECKED.**
- The mirror x→−x maps (+x, +y, −x, −y) to (−x, +y, +x, −y). That is a cyclic shift of the reversed schedule, i.e. the inverse cycle U⁻¹, and not a cyclic shift of the schedule itself.
- In the mirror cycle, μ_bulk = +1 and every region circulates counterclockwise. 4×4 island: ρ = +1 at all four phases, rays −1.

**D8. Covariant only up to cyclic relabelling. EXACT; CHECKED.**
- A 90° rotation about any site maps the cycle to its shift by one sub-step. An odd translation swaps the sublattices and shifts it by two.
- So R U_J R⁻¹ = V U_{RJ} V⁻¹, with V the leading sub-steps. CHECKED as an exact permutation equality on 40 random lock patterns.
- The unshifted phase never matches (0/40). The four phase-shifted cycles never pairwise commute (0/40), so a 16-step symmetrised composite is not strictly covariant either.
- **Named conditional reading SC (schedule covariance), not adopted:** "A ticked step made of sub-steps counts as covariant if every lattice symmetry maps the cycle onto the same cycle started at another sub-step."
- **Why the relabelling is forced:**
  - (a) EXACT. A layer of disjoint gates invariant under all unit translations has single-site blocks only. A block containing x and x+e would be invariant under translation by e, hence infinite. So strictly covariant transfer layers do nothing.
  - (b) EXACT, given the RLBL winding (comparator). With one qubit per site and a strictly translation-invariant drive, the one-excitation step has one band, whose winding is zero, so there is no one-way edge. The two-sublattice schedule is what allows the flow.
- **Relabelling preserves every flux. EXACT.** For σ′ = vσv⁻¹ with σ the identity outside a bounded set B, ρ(σ′) = ρ(σ) + Σ_{x∈B}[φ(σx) − φ(x)] = ρ(σ). Here φ(x) is the angle of the move x→v(x).

### 3.3 Many-body: index along a closed boundary

**D9. Definition and value.**
- Let C be the set of open sites that U moves around one record region. By D3, U = W_C ⊗ (identity elsewhere), and the bulk is exactly the identity (EXACT).
- Arrange C as a ring in angular order and group it into blocks at least as long as W_C's reach along the ring.
- **ind_C** := the GNVW index of W_C, computed locally at any cut of the ring.
  - It is cut-independent and unchanged by composing with any finite-depth circuit whose reach is much shorter than the ring (GNVW, comparator).
  - It is protected only for rings much longer than the reach.
- For transfer cycles, log₂ ind_C = net qubits crossing a cut per cycle. This is EXACT by counting, given GNVW: a permutation splits as a shift times block permutations (A1 D4).
- Values: log₂ ind_C = −1 (counterclockwise positive) for every record region with a deep point; the bulk index is 1.
- **Anomaly. EXACT.** The whole U is a depth-4 circuit, yet W_C is not a circuit on C, because a ring circuit has zero rotation number. Each island's channel is compensated at infinity. In a finite world, it is compensated by the opposite channel on the outer boundary: for any finite swap circuit on an annulus, the total rotation is zero.
- **One excitation.** It follows its orbit. The edge step is a cyclic shift, so its quasi-energy winds once, one way, as the ring momentum winds once (EXACT). Each sub-step is smoothly generated, since SWAP = exp(iπ(1−SWAP)/2). So what the flow needs is the ordered schedule, not discreteness itself (EXACT).

### 3.4 3D

**D10. No transfers under SC with the 24 rotations. EXACT.**
- The phase-shift map φ: G → Z_p is a homomorphism (G = translations plus rotations about sites; p = the period of the sub-step sequence).
- The face C₂ rotations and the C₃ rotations lie in [O,O], the 12-element group T (CHECKED by enumeration), so φ vanishes on them about every site.
- Each sub-step therefore equals its own image under the face C₂ about every site s. Its finest product decomposition is then invariant.
- A pair {s, s+e} is mapped by the C₂ about an axis perpendicular to e onto {s, s−e}. Disjointness then forces s to be unpaired.
- More generally, a finite cluster invariant under C₂ about each of its own points is invariant under a nonzero translation, hence infinite.
- So every sub-step is on-site: no transfers and no flow. This holds for any gate type and any handedness.
- In 2D the argument fails because C₄ is not a commutator, which is consistent with the 2D construction.

**D11. Lattice Ampère law in 3D. EXACT; CHECKED.**
- Setting: any bulk-identity transfer cycle, with M = the mean loop-area vector ½Σ r×dr per site.
- Statement: the net current on every periodic record facet with integer normal n is K = M×n̂. Equivalently, the flux through r_t = c over one torus period is L(M×n)_t.
- Proof sketch:
  - Apply D4 with ∂S split into a curve inside the record (no loops) and a curve in the open bulk.
  - The bulk linking count per length is independent of where that curve lies, because moving it sweeps no π-moves. So it equals its average, M·τ̂.
- CHECKED: exact integer match on 12 slabs. The normals were (1,0,0), (0,1,0), (0,0,1), and the low-symmetry (1,0,2), (1,2,3), (2,−1,1), for both cycles of D13.

**D12. What weaker readings leave. EXACT for periodic facets and axis hinges.**
- The weaker reading: R U_J R⁻¹ = V U_{RJ} V⁻¹ with V a local transfer circuit.
- Fluxes are invariant under conjugation (D8). So:
  - on axis faces, C₄ about the normal forces K = 0, hence M×x̂ = M×ŷ = 0, so M = 0, so K = 0 on every periodic facet (D11);
  - on axis hinges, C₂ about n₁+n₂ reverses the hinge direction, so the hinge flux is 0.
- Hinges between inequivalent facets have no stabilizer and stay OPEN. Corner circulations are allowed but localized, with no index.
- In 3D a circulation is an axial vector, which proper rotations act on. So "proper rotations only" does not shelter it, unlike A2's pseudoscalar W₃.

**D13. With a supplied direction. CHECKED; covariance EXACT.**

*Layered z cycle* (D1 in every z-layer):
- Covariant up to relabelling under C₄z (shift 1) and translations (odd translation: shift 2). No phase works for C₄x.
- M = −ẑ.
- Side faces carry one item per cycle per layer, clockwise seen from +z (K = n̂×ẑ). The ±z faces carry nothing.
- 6-layer cube: half-plane flux −6.

*Body-diagonal cycle:* (x, y, −z, −x, y, z, −x, −y, z, x, −y, −z), a closed self-avoiding 12-step loop:
- C₃ about (111) gives shift 4; odd translation gives shift 6. No phase works for C₂z or C₄z.
- M = (2,2,2).
- Every face carries K = M×n̂. For example, face +x carries +2 along y and −2 along z per unit length.
- Cube s = 6: half-plane fluxes 16 = 2×(6+2). The +2 is a loop-size correction at the hinges.

> **Comparators (not adopted).**
> - Rudner–Lindner–Berg–Levin, PRX 3, 031005 (2013): anomalous Floquet edge states; bulk winding equals edge count.
> - Po–Fidkowski–Morimoto–Potter–Vishwanath, PRX 6, 041070 (2016): chiral unitary index; the SWAP model, which is D1 in essence.
> - Gross–Nesme–Vogts–Werner, CMP 310 (2012): GNVW index.
> - Mutual-information form log₂ ind = ½[I(a_in:b_out) − I(b_in:a_out)]: recalled from the matrix-product-unitary literature, not re-checked against the source; validated here on known cases.
> - Textbook magnetization (bound) current K = M×n̂.
> - Background only, not checked and not imported: the repo lane "zero-field records bind chiral Majorana bands, weak Chern 1". A weak (layer) index is also a directional quantity whose direction comes from the record arrangement, not the law. Whether there is a real link is OPEN.

## 4. Checks

All are permutation bookkeeping with exact integer comparison, except angle sums (float, matched to integers within 1e-9; reported rounded to 1e-6).

- **`check2d.py`** (with `cyc2d.py`):
  - Bulk identity on an L=16 torus: True (4 phases × 2 hands).
  - Wall band: row 4, A items, +2 (8 items); row 15, B items, −2 (8 items).
  - Islands s = 1–6 on L = 24: moved = 2s+1; one orbit; path winding −1.000000000; ρ = −1; rays in all 4 directions = +1 (s ≥ 2).
  - 4×4 island: all phases ρ = −1; mirror ρ = +1.
  - Covariance: R gives shift 1 and T gives shift 2 exactly (40 patterns); commuting phases 0/40.
- **`check2d_b.py`:** L = 64 torus, patterns inside a radius-9 disc, summation radius 29. Results as in D5. Chords subtending more than 0.9π were skipped, at plaquette centres only (1–52 per pattern).
  - Note: a first run on L = 40 gave non-integers because orbits straddled the summation radius under minimal-image wrap. Fixed by enlarging the torus.
- **`check2d_c.py`:** 90° image matches phase 1 in 40/40 and phase 0 in 0/40; maximum moved distance 1; 1×1 and 2×2 orbits as in D3.
- **`gnvw.py`** (peak 172 MB):
  - Ring n = 10, k = 3: identity 0; right shift +1; left shift −1; depth-2 random brickwork 0 (error below 1e-10); layer∘shift∘layer +1.
  - 4×4 island edge orbit (9 sites, each item −1 ring position per cycle): log₂ ind = −1 at all 9 cuts, both bare and dressed with random layers.
- **`check3d.py`:**
  - Bulk identity: True (both cycles); M = (0,0,−1) and (2,2,2), with zero spread over items.
  - Covariance phases as in D13.
  - [O,O]: 12 elements (traces: three −1, eight 0, one 3); every axis vector is reversed by some element.
  - Bug note: a first run put the cut planes through lattice sites (cube side even), giving −3 instead of −6. Fixed with generic offsets; the reported values are after the fix.
- **`check3d_b.py`:** 12 slabs, all exact matches with L(M×n)_t. For example, the C3 cycle with n = (1,2,3), L = 48 gave (96, −192, 96).
- **Not run (a suggested next toy):** a search for a cycle that is weakly covariant, has M = 0, and carries nonzero flux on a (102)/(001) hinge. Plan: random 3D transfer schedules with a 2×2×2 cell, symmetrised over O at the flux level, measuring hinge flux on a record wedge. Expect minutes; above budget.

## 5. Real-physics match

- **2D.** The toy reproduces anomalous Floquet behaviour (comparator): a bulk that does nothing and one-way channels on boundaries, here bound to frozen (recorded) regions. As an ANALOG: if records behaved like this, one-way edge transport (quantum-Hall-like edges, but for qubit content, not fermions) would appear around every recorded region with no field supplied, and its orientation would come from the law's handedness.
- **3D.** The surface flow is exactly Ampère's magnetization current K = M×n̂ (D11): the bulk loops act like molecular current loops, and records act like holes in a magnetized medium. That is an exact lattice identity; the physical identification is analog only.
  - Real 3D chiral surface currents need an axial vector (a field or a magnetization). The axioms' rotation covariance forbids one in the law, so this mechanism cannot supply chiral surface channels bound to records without an imported direction.
  - It does not produce Weyl-type chirality. A2's W₃ = 0 is untouched in the covariant setting.
- **What would falsify these results:**
  - a 3D cycle of local disjoint-gate layers that is SC-covariant under the 24 rotations and moves anything (contradicts D10);
  - a weakly covariant cycle with nonzero current on an axis facet (contradicts D12);
  - a 2D bulk-identity cycle in which a large record region's circulation differs from μ_bulk (contradicts D5).

## 6. Open edges and next steps

1. **Low-symmetry hinges and corners in 3D** under the weak reading. Symmetry does not exclude them, and a handed law could orient them. Run the toy described in §4.
2. **Local ticks (I1).** Regions running the cycle at different phases conflict on boundary pairs, and no rule for phase walls is fixed. Whether phase walls carry channels is OPEN.
3. **Moving records (I2/I3).** The conveyor should follow the wall, and formation odds next to a conveyor are not analysed.
4. **A time-independent, covariant, star-local generator** (Campaign 7 sentence 2). Whether record walls bind one-way channels without a schedule is OPEN. The schedule-based mechanism here needs an ordered phase.
5. **Non-swap gates** (partial transfers, gates with phases): the bulk is no longer the identity, and robustness under the index definition is open.
6. **Readings for the owner to choose between:**
   - SC: workable in 2D, empty in 3D;
   - the weak index-level reading;
   - a reading that also allows reversal (U ↦ U⁻¹). That one would formally admit the layered cycle, but it equates a conveyor with its reverse, so it cannot protect one-way flow.

## 7. Plain-language summary

Picture a rule where, in each tick, every open site trades its possibilities with a neighbour in four set moves that go around a little square. Out in open grid, everything ends each tick exactly where it started. Next to a recorded site, the trades that would touch the record simply do not happen, so the possibilities beside it are carried around the recorded region, always the same way round and one site's worth per tick, while nothing moves anywhere else. On a flat grid this works for every shape of recorded region, including a single record, and the mirror-image rule turns the flow the other way. On the real three-dimensional grid it fails, because the rule must look the same after every turn of the grid: that leaves no trading at all in rules of this kind, and even looser versions cancel the flow on every flat face of a recorded region. A one-way flow around recorded regions in three dimensions would need the rule itself to carry a built-in direction, and the axioms do not supply one.

**Files** (all in the A11 scratch directory): `cyc2d.py`, `check2d.py`, `check2d_b.py`, `check2d_c.py`, `gnvw.py`, `cyc3d.py`, `check3d.py`, `check3d_b.py`, `run.sh`.