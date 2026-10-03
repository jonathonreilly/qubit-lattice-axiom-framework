*(Saved by the coordinator from the agent's final message; the agent's harness forbade writing REPORT.md.)*

# A40 report: one pattern of kinds of places?

**Files and rules.** Let SP = `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad`. Scripts, outputs and run statistics are in `SP/c8/A40/`:
- `run.sh`
- `k1_kinds_patterns.py`
- `k2_star_form.py`, which loads A25's `stag2.py` by path
- `k3_layouts.py`
- `k4_matter_loops.py`

No git, no repo edits, no PRs, no review or audit lanes.

**Grades.**
- EXACT: proof, or exact arithmetic or enumeration over a stated finite class.
- CHECKED: numerics with a stated tolerance.
- ARGUED: reasoning without proof.
- SUPPLIED: a premise put in by hand.
- COMPARATOR: literature recalled from memory, never adopted.

Every model is a supplied toy, every rule is a named conditional, and nothing here is proposed as adopted.

**Conventions.**
- The layout label is s = 0. A site y has class r = y mod 2 and a role from A25 S7:
  - V (weight 0);
  - E_a (weight 1, axis a);
  - F_a (weight 2, normal a);
  - C (weight 3).
- A "star" is a site plus its 6 neighbours.
- Distances are Manhattan distances on Z³.

---

## 1. Question

Can one 1-of-8 pattern of kinds of places serve everything?
- **Field places** carry light and gravity and never record.
- **Matter places** can record, have a calm vacuum and carry matter.
- **Buffer places** are optional.

The pattern has to fit:
- state-level covariance under the 24 site-centred turns;
- A25's field layout;
- A31 D10;
- A39 escape (e);
- matter's own twist (A31 Theorem S, A33, A38);
- A26's lapse and frame couplings.

The brief also asks for the payload per place, the couplings across kinds, and a verdict for the owner.

## 2. Answer (short, graded)

**Conditional yes, but only in a "shared places" form. The clean three-disjoint-kinds form fails.**

1. **The kinds pattern is the field's own label (EXACT; CHECKED k1).**
   - A period-2 kinds pattern that moves together with A25's layout under all 24 site-centred turns must be a function of the role (V, E, F, C).
   - That is 81 of the 3⁸ = 6561 three-kind patterns.
   - So a kinds pattern adds no new label beyond F6. It is the same 1-of-8 choice.

2. **Gravity needs only half the roles (EXACT; CHECKED k2).**
   - A25's own (h,π) form keeps all field content on V and F places.
   - Every potential term depends on the h's around one E or C place and never on that place itself. I call these "hollow-star" terms.
   - E and C places therefore carry nothing.
   - A25's curl-split form, which uses neighbour pairs only, needs all four roles. A34 C61's collision ("every place carries field") holds for that pair form only.
   - The star form frees half the places, at the price of terms spanning three or more places of a star (decision 22).

3. **No fully separated layout works (EXACT for the 270 stated combinations; CHECKED k3).** The combinations are:
   - gravity in either A25 form;
   - light either in link form with charged matter on its Gauss-law role, or non-gauge light (A39's toy);
   - matter places kept apart from field places, place by place (D10).

   Within these, none lets charged matter feel the lapse. Matter always lands on the corner role opposite the lapse, at distance 3, and no star holds both.

   With non-gauge light, two separated layouts exist: gravity on V and F, matter on E, light on C, plus its twin. But their matter is neutral, and lapse and shear can enter only as separate first-order terms. The only stars holding both a V and an F are E-centred, and they hold no second matter place (EXACT).

4. **The layout that meets the couplings (EXACT; k3).** The two combinations with the fewest shared places are S1 and its twin (V↔C, E↔F). S1 is:

   | Role | Job in S1 |
   |---|---|
   | V | matter, plus gravity's stretch parts (h_ii, π_ii), plus the lapse |
   | E | light's links, with the Gauss law at V |
   | F | gravity's shear parts (h_ij, π_ij) |
   | C | no job |

   Each matter hop sits in one E-centred star. That star also holds both ends' lapse, h_aa at both ends, the four relevant shear components, and the link.

5. **Payload (EXACT, given A25's content).**
   - More room per place is unavoidable for A25's gravity in every assignment, because a canonical pair has no finite-dimensional representation.
   - The pattern only decides where the extra room goes: 4 of 8 places in the star form, 8 of 8 in the pair form.
   - Light fits one qubit per link place (COMPARATOR: spin-1/2 quantum links).
   - Neutral matter fits one qubit. A turn-glued U(1) charge on a corner place needs at least two qubits (EXACT).

6. **Records (EXACT).**
   - In S1, D10 survives only factor by factor: a record at V locks a possibility of V's matter factor, never its gravity factor.
   - In every layout with gravity on a checkerboard, no two matter places are nearest neighbours. So:
     - records cannot step to a nearest neighbour; steps go two sites;
     - A28's "form only next to a record" gate at reach 1 would forbid every record;
     - Q7's "recorded neighbours" can act only at reach 2, through a light place.

7. **Couplings (EXACT).** The weight F = N̂_V ⊗ F_matter ⊗ 1_light, all at the same V place:
   - is quiet on the calm matter vacuum;
   - is blind to light, as A39 (e) needs;
   - redshifts record clocks, as A31 K4(c) needs;
   - never locks the lapse;
   - is linear in the state, so it does not signal.

   A39's strict F_matter ⊗ 1_field, blind to gravity as well, would stop record clocks from redshifting (EXACT).

8. **The twist (EXACT; CHECKED k4).**
   - With matter on a single role, every square of matter's lattice has a kept half-turn that fixes two same-role corners. So neither painted signs nor A33's parities can give π there (generalized Theorem S).
   - But in S1 matter's hops carry light's link, and light's vacuum can hold π through every square.
   - That configuration is kept by all 24 turns, up to a gauge change. Explicit gauges were found for all 24.
   - It needs one uniform sign on light's square term, not a pattern (ARGUED; COMPARATOR: π-flux quantum spin ice).

9. **Verdict.** S1 is a coherent single supplied 1-of-8 choice (ARGUED overall; the pieces are EXACT as graded).
   - It bundles decisions 13, 17, 21, 22, 24 and A39's light-invisible-to-records choice.
   - Its costs are:
     - more room at V and F;
     - a factor-wise reading of Record;
     - one idle place in 8;
     - matter number exactly conserved;
     - records stepping two sites at a time;
     - for a one-place mass, a staggered pattern that is not a role function (EXACT).

## 3. Derivation

### 3.1 Which kinds patterns are allowed (Q1, covariance)

- **K1 (EXACT).**
  - A proper turn about site c acts on classes as r ↦ P(r − c) + c (mod 2), where P is the turn's permutation part.
  - "Moves with the layout" means: the image of the kinds pattern is its translate by the same vector that moves A25's layout.
  - Turns about V keep the layout exactly (A25 S9), so the kinds pattern K must be invariant under them.
  - Their orbits on the 8 classes are {V}, {E_x, E_y, E_z}, {F_x, F_y, F_z} and {C}. So K is a function of role.
  - Conversely, every role function moves with the layout (A25 S9.2).
  - CHECKED (k1, exhaustive):
    - 81 of 6561 move with the layout, and all 81 are role functions.
    - 297 patterns are covariant on their own. Each is a role function of some translate s′. For example, "E_x only" is "V only" for s′ = (1,0,0), but it does not move with s = 0.
    - A layered pattern fails.
- **K2 (EXACT/ARGUED).**
  - Coarser patterns (checkerboard, uniform) are special role functions (EXACT).
  - Period-4 patterns are supplied structure beyond F6 (ARGUED). One appears below in T8.

### 3.2 Where gravity's content sits

- **G1 (EXACT; CHECKED k2 on A25's builder, side 8).** In A25's (h,π) form on the parity-role lattice:
  - all h and π components sit on even classes: V has 3 diagonal pairs, each F_a has 1 off-diagonal pair;
  - each curl component sits on an odd place and depends only on h at its 6 neighbours (maximum distance 1; zero inputs from the place itself);
  - V(h) = ¼ Σ C:Cᵀ equals the sum over odd places y of terms supported on star(y) minus y (reconstruction error 0.0 over 256 centres);
  - the kinetic term is on-site.

  So H_field = (on-site kinetic terms on even places) + (hollow-star potential terms centred on odd places). It is star-local, with content on V and F only.
- **G2 (EXACT, from A25's S3 identities).** In continuous time (the record-tick shape's smooth change), the star form keeps A25's properties:
  - Dᵀπ is conserved, because 𝒱D = 0;
  - R h is conserved on the momentum surface, because R𝓜 = −Div·Dᵀ;
  - tensor modes have ω = |ŝ| (z = 1), with no doubler (ŝ = 0 only at k = 0).

  As a tick, its P-layer is a product of commuting hollow-star gates (A25 S7's "Manhattan reach 2").
- **G3 (EXACT).**
  - The pair-local curl-split form stores C on E and C, so all 8 classes carry content.
  - The twin form is (h,π) on the translate s + 111: content on E and C, lapse at C.
- **G4 (EXACT; k2 role table).**
  - The lapse (Hamiltonian row) sits at V (A25 S1). The shear component h_ab sits at F_c.
  - V–F distance is 2, and V–C distance is 3.
  - The only stars holding both a V and an F are E-centred. An E star holds 2 V's and 4 F's and no other E or C.

### 3.3 Homes for light and matter

- **L1 (EXACT, role geometry).** Places that can serve as links along their own axis between two Gauss-law places are:
  - E_a, between two V's along a;
  - F_a, between two C's along a.

  V and C have no axis. So link-form light has two options:
  - content on E, Gauss law in V-stars (6 E's each), square terms in F-stars (4 E's each), all star-local;
  - or the twin: content on F, Gauss law at C, square terms at E.
- **L2 (COMPARATOR, plus ARGUED).**
  - Spin-1/2 quantum links (one qubit per link) carry an emergent photon with z = 1 away from the Rokhsar–Kivelson point (quantum spin ice and quantum link models). That literature is recalled from memory and not verified for the cubic lattice.
  - On edge places, σ^axis is the covariant label (A33's edge lemma; A34 c7), which fits gluing (ARGUED).
- **M1 (ARGUED, physics).** Charged matter must sit on light's Gauss role. A gauge-covariant hop V–E–V′ fits in E's star.
- **M2 (EXACT, representation theory; A34 c7).**
  - On one qubit at a V or C place, the 24 turns leave only multiples of 1 invariant (A1 + T1).
  - Gauss's law with glued links needs a turn-invariant charge at V.
  - So a glued U(1) charge on a corner place needs at least two qubits. A1 appears twice in (A1+T1)⊗², as 1 and σ₁·σ₂; for example, a charge projector onto the singlet.

### 3.4 Enumeration of kinds assignments (one kind per role)

There are 81 assignments of {V, E, F, C} to {Field, Matter, Buffer}.
- **Gravity fits (EXACT)** only if Field contains {V,F} or {E,C} (star form), or all four (pair form). That is 17 assignments.
  - The other 64 break A25's need for field places.
- **All-Field (1 assignment):** no matter places, and D10 forbids every record (C61).
- **6 assignments** have gravity's half as Field and no Matter.
- **The remaining 10** split into 5 primal and 5 twins:

| (E, C) kinds, with V, F = Field | Light | Charged? | Lapse reach | Lapse + shear in one star | Matter twist (k4) | What breaks |
|---|---|---|---|---|---|---|
| Matter, Matter | must share F with gravity (twin link; Gauss at C) | yes (C) | no for C (distance 3) | no | E squares forced; C coarse squares forced | light shares gravity's places; lapse |
| Matter, Field | twin link on F (shares) or non-gauge on C | no | yes, split first order | no | squares forced; kept signs uniform → nodal lines (T4) | charge; all-orders coupling; no cones |
| Matter, Buffer | must share F with gravity (Gauss at C is a buffer) | no | yes, split first order | no | as above | charge; light shares |
| Field, Matter | link on E (own places); Gauss at V is a field place | no | no (C–V distance 3) | no | coarse squares forced (T3) | charge; lapse; twist |
| Buffer, Matter | twin link on F shares; Gauss at C | yes | no | no | coarse squares forced | light shares; lapse; twist |

**Result (EXACT within these forms).** Every one-kind-per-role assignment breaks at least one of:
- charged matter;
- lapse reach;
- light on its own places;
- a matter twist kept by the layout.

k3 (1) confirms this: 0 of 270 combinations meet place-wise D10 + charge + lapse reach.

### 3.5 Shared places: layout S1

**Which combinations pass.** When a place may carry gravity and matter together, with records locking only the matter factor, k3 (4) finds 8 combinations meeting all of:
- charge;
- lapse and shear in one star with each hop;
- light on its own places.

The two with the fewest shared roles are S1 and its twin. The other six add matter to E (sharing light's places) or to F.

**Couplings in S1.** For an x-hop V(0,0,0)–V(2,0,0), the E(1,0,0) star holds (EXACT; k2):
- both lapses and h_xx at both ends;
- h_xy at F(1,±1,0);
- h_xz at F(1,0,±1);
- the link.

**The idle place C.**
- Under any gate that needs a record in the star, C never records, because its star holds only F places (EXACT).
- Without such a gate, C needs a zero weight (SUPPLIED).

**Matter's lattice.** Matter lives on the V places, 2Z³ + s: a coarse cubic lattice of spacing 2.

**Consequences for records (EXACT).**
- V's six neighbours are all light places. So:
  - no record ever has a recorded nearest neighbour;
  - a one-grid-space step (I2) would land on a light place, so the swap and claim steps (SW, CL) must act at reach 2, through E;
  - A28's reach-1 gate would forbid every record.
- A39 (e) keeps voids quiet without the gate, because F_matter annihilates the calm matter vacuum.
- No region can ever be fully recorded: E, F and C never record, so light and gravity run through any cluster of records. This changes the I5 black-hole picture (C61 (ii)).

### 3.6 Payload (Q2)

| Role in S1 | Content | Grade |
|---|---|---|
| V | h_ii, π_ii: 3 canonical pairs (6 reals) | EXACT (A25) |
| V | dynamical lapse: +1 pair | ARGUED (A31 K4(b)) |
| V | matter: ≥ 2 qubits if glued-charged, 1 if neutral | EXACT (M2) |
| E | light link: 1 qubit (spin-1/2 link) | COMPARATOR; a compact rotor in KS's original form |
| E | shift vector, if dynamical: +1 pair, where A25 puts ξ | ARGUED |
| F | h_ij, π_ij: 1 pair | EXACT |
| C | nothing; its qubit is idle | EXACT |
| all | an 8-valued role label (A25 open edge 1), unless the domain itself differs by role | ARGUED |

- **More room is unavoidable (EXACT).** tr[h, π] = 0 ≠ i·dim, so no finite domain holds A25's field. More room is needed at 4 of 8 places (star form) or 8 of 8 (pair form), in every assignment.
- **If every site keeps the same domain (ARGUED).** "No site is privileged" read as "same domain everywhere" means every place carries the union: at least 4 pairs, 3 qubits and the label, with the pattern deciding which parts act.

### 3.7 Couplings across kinds (Q3)

**The change.**
- Matter to gravity: lapse × (matter terms) on-site at V; frame and shear on hops inside E stars (§3.5).
- Matter to light: the gauge-covariant hop ψ†_V U_E ψ_V′.
- Light reaches records only through matter it is absorbed by, as A39 (e) requires.

**Weight W1 = N̂_V ⊗ F_matter(V) ⊗ 1_rest (EXACT).**
1. It is quiet: (N̂ ⊗ F_m)(Ω_f ⊗ |0_m⟩) = 0 whenever F_m|0_m⟩ = 0.
2. It is blind to light.
3. Record clocks redshift with N̂ (A31 K4(c)).
4. It weights the lapse but never locks it. Each event cuts the lapse's possibilities slightly (A31 K3(d), ARGUED).
5. It is linear in the state, so it does not signal (A23 D1, A26 D12).

**Strict A39 form.** With F_m ⊗ 1_field, blind to gravity as well, the formation chance does not depend on the gravity factor at all. Records would then not redshift (EXACT, by linearity).

**Q7, menus set by the conditions including recorded neighbours (EXACT).**
- Matter places have no matter nearest neighbour: in all checkerboard layouts (k3 (5)) and in S1.
- Dependence on recorded matter is possible only through weights centred on a light place, acting on the two matter factors at its ends and as 1 on the link. That is star-local and blind to light (EXACT construction).
- Lock odds, taken from V's own part after the update, still vary with unrecorded neighbours through the change (ARGUED, as in A39 (e)).

**Matter number.** Gauge-covariant hops conserve charge. A39 (e) also needs no pair-creating terms; that cost stands.

### 3.8 The twist (Q4)

- **T1, generalized Theorem S (EXACT).** Take matter on any union of roles, any hop set, and a loop ℓ. Let g, an element of the layout's group O ⋉ 2Z³, reverse ℓ and fix two of its sites x and c, with no bond fixed.
  - (a) With exactly-kept real signs, the bonds pair up and the sign product is +1.
  - (b) With A33's parity route, the flux sign is p(x)p(c). If x and c have the same role, they differ by a 2Z³ translation along g's axis, which commutes with g. So p(x) = p(c), and the product is forced to +1.
  - (c) If g fixes one site and one bond, as for every triangle, the fixed bond's sign is free.
- **T2 (EXACT; CHECKED k4).**
  - A Z³ unit square needs three roles: V, E, E, F or E, F, F, C. So unit squares exist on matter's lattice only if matter covers at least 7 of 8 places, which overlaps gravity in every layout.
  - Control: on all of Z³ with unit hops, 54 of 54 squares are of the parity type. This is consistent with Theorem S and A33.
- **T3 (EXACT; CHECKED k4).**
  - Matter on one role (V or C): 12 of 12 coarse squares are forced to +1 by both mechanisms.
  - Matter on E (or F) with the shortest hops: 18 of 18 squares forced, 19 of 19 triangles free.
  - With longer hops, 66 squares become free, but 12 stay forced.
- **T4 (EXACT).** E-only matter with exactly-kept signs:
  - the 12 E–E bonds per cell form one orbit, so the kept signs are uniform;
  - the Bloch form is H(k) = 4t(vvᵀ − diag(v_a²)), with v_a = cos k_a;
  - H vanishes on the lines where two cosines are zero;
  - the result is nodal lines, not point cones (compare A38's pair-law nodal lines).
- **T5 (EXACT; CHECKED k4).** Light-supplied flux:
  - With matter on V and hops carrying light's link, the twist matter feels is light's square holonomy W.
  - "W = −1 on every coarse square" is a uniform, gauge-invariant assignment, so every turn and translation keeps it.
  - On Z³, two link configurations with equal holonomies differ by a gauge change.
  - k4 check, on a 4³ coarse torus:
    - the KS signs give W = −1 on all squares;
    - each of the 24 turns gives W = −1 everywhere, with an explicit consistent gauge function.
  - Theorem S does not apply here. Its premise is a fixed sign pattern with no gauge freedom (A31 D5's glued case). Here the freedom is the Gauss-law gauge group of matter plus light, which acts trivially on physical states (ARGUED).
- **T6 (COMPARATOR).** In quantum spin ice, the sign of the square (ring) term selects a 0-flux or a π-flux vacuum (Lee–Onoda–Balents 2012, from memory). So the twist becomes one uniform law sign on light's square term (A33's "uniform minus sign" choice, moved to light), not a pattern.
- **T7 (EXACT, KS counting).** The single-particle problem is KS on the coarse lattice: two tastes in 3D and net chirality 0, unchanged.
- **T8 (EXACT).** A one-place staggered mass on the coarse lattice has period 4 on Z³. It is not a role function, so it would be a further supplied label (1 of 2) unless the mass arises some other way. A31 D7 found no clean glued mass.
- **T9 (ARGUED).** Over an empty, quiet matter vacuum, the lower Dirac branch is made of real one-particle states with no sea. A39's loopholes (a) and (a′) still bear on matter.

### 3.9 Verdict (Q5)

- **Coherent single choice?** Yes, in the S1 form (ARGUED): one role pattern, the same label as F6, with the law using role labels, as A25's law already does. It is not coherent with place-wise D10 and charged, lapse-coupled matter (EXACT within the stated forms).
- **Decisions it bundles.**
  - **13:** F6 plus more room, now only at V and F; a dynamical lapse at V.
  - **21:** "gravity's places never record" becomes factor-wise.
  - **22:** the star form needs hollow-star terms; with pairs only, every place carries gravity.
  - **17:** matter's painted pattern is replaced by light's uniform π vacuum.
  - **24:** an 8-fold matter background is not needed.
  - **A39 (e):** F = N̂ ⊗ F_m ⊗ 1_light, with exact matter-number conservation.
  - It also touches decision 4 (A28's gate), 8 and 27 (two-site steps), 16 (the calm axis on V's matter factor), 20 (light never recorded directly) and I5 (no fully recorded region).
- **Costs against the axioms.**
  - **"No site is privileged":** a state-level 1-of-8 pattern, the same one as F6. One place in 8 is idle; that is still a role function, so no extra label (ARGUED).
  - **One qubit per site:** broken at V and F, unavoidably for A25's field (EXACT). V also needs at least 2 matter qubits for a glued charge (EXACT). E and C keep one qubit.
  - **Record:** "locks exactly one admissible local possibility" must be read factor-wise. That is a wording decision.
  - **Q7:** dependence on recorded neighbours works only at reach 2.
  - **Matter:** number exactly conserved, a coarse lattice, and a coarse mass pattern if a one-place mass is used.

## 4. Checks

Every run went through `run.sh`: `nice -n 10`, all four thread caps at 1, a 28 s alarm, and a load gate below 6. Loads at run time were 2.0–5.4.

| Script | Result | Time, peak memory |
|---|---|---|
| `k1_kinds_patterns` | 6561 patterns. 297 covariant alone, all role functions of some translate. 81 move with the layout, all role functions. Layered control fails. | 3.8 s, 15 MB |
| `k2_star_form` (A25 builder, side 8) | (h,π) only on even places, C only on odd. Curl inputs within distance 1, none from the centre. Star sum minus 𝒱 = 0.0 over 256 centres, support within distance 1, centre unused. 𝒱 couples distances {0, 2}. Kinetic on-site. Role-distance and star tables. | 0.3 s, 57 MB |
| `k3_layouts` (270 combinations) | (1) place-wise D10 + charge + lapse: 0. (2) D10 + charge: 4, all with light sharing gravity's places and lapse out of reach. (3) D10 + split lapse/shear: 2, neutral matter. (3b) one-star coupling: 0. (4) shared: 8, minimal ones S1 and twin. (5) adjacent matter on checkerboard layouts: none. | 5.2 s, 17 MB |
| `k4_matter_loops` | Loop classification table (§3.8). KS on the 4³ coarse torus: all squares −1. All 24 turns give gauge-equivalent patterns with explicit gauges. | 1.4 s, 29 MB |

**Superseded runs.**
- `k3`'s first star test limited star centres to [−2,2] and wrongly failed hops at the box edge.
- After fixing that, one version hit the 28 s alarm and was rewritten with a cached common-star test.
- One intermediate version labelled a "same star" column that actually ran the split test. The final version runs both tests and labels them correctly.

Tolerance: zeros are exact (integer or dyadic arithmetic). k2's 0.0 is a floating-point zero on dyadic entries.

## 5. Open edges

1. **Light's vacuum.** Confirm a z = 1 Coulomb phase with a π-flux background for spin-1/2 links on the cubic lattice under glued couplings. This is COMPARATOR only so far.
2. **Charged hop.** Write the glued gauge-covariant hop for a two-qubit turn-scalar charge at V, and check it under all 24 turns.
3. **Cross shear.** On the coarse lattice, A26's in-cell sandwich becomes a reach-4 operator. A star-local, cell-free shear on F places is still open (A31 open edge 2; here F holds the shear).
4. **Mass.** A matter mass without the period-4 pattern of T8.
5. **Lower branch.** The lower-branch and sea issue (T9) under A39 (e).
6. **Shift vector.** If it is dynamical, it sits at E and shares light's places.
7. **Finer patterns.** Period-4 kinds patterns were not enumerated.
8. **Collective gravity.** A collective one-qubit gravity (decision 13's alternative) would change the payload answer.
9. **Owner decisions.** Each item below is framed for the owner; none is adopted.
   - Accept S1's shared V places, with records locking only the matter factor?
   - Accept hollow-star terms?
   - Accept a uniform sign on light's square term?
   - Accept records stepping two sites at a time?
   - Accept one idle place in eight?

## 6. Plain-language summary

The grid's places can be sorted into kinds using the same 8-way pattern that gravity already needs, so no new pattern is added. Gravity needs only half the places if its rule may use small groups of places, not just pairs. But no arrangement keeps every kind on its own places and still lets charged matter feel gravity's slowing of time. The arrangement that works puts matter on the same places as gravity's stretch parts, with records fixing only matter's share of each place. Light sits on the places between them, and one place in eight has no job. Light's own calm state can then give matter the half-turn twist it needs, with nothing painted on. The price: places that hold more than one site's worth, records that move two places at a time and never touch light or gravity, and matter that never appears out of empty space.