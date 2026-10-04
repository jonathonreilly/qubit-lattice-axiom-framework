I ran lane A52 to the end (about 2 hours of the 2.5-hour box). One run went over the memory guide, and I've flagged it in section 5. The derivations are in `SP/c8/A52/NOTES.md`; I did not write a separate REPORT.md.

# A52 report: record-conditioned fermionic hops for light's charges

## 1. Verdict
- **Escape (a) works (EXACT; CHECKED).** Let every corner place hold a record whose locked possibility points along a body diagonal. Then an explicit hop rule exists with all of these properties:
  - Gauss's law stays exact;
  - the law is covariant under all 24 turns and the translations, as a function of the records;
  - the Levin–Wen phase is −1 on all 20 junction triples at every corner.
  
  This holds on the uniform background and on any mixture of body-diagonal records. Axis records give no fermions in any class I tested.
- **The pattern changes nothing measurable (EXACT).** Any two record backgrounds give unitarily equivalent laws. A fixed set of controlled-sign gates on each corner's six links maps one law onto the other. The records carry only the bookkeeping that exact turns demand.
- **The real price is in the law.**
  - The light ring term must be dressed as well (EXACT). It then depends on its four corner records and reaches farther.
  - In empty space the dressed ring is equivalent to the bare one by a diagonal sign change. Light's spectrum and its field correlations are unchanged (CHECKED on small tori).
  - In the π-flux sector the charges are Dirac fermions, doubled in the Kawamoto–Smit way.

## 2. Question
Can a pattern held in records cut the turn symmetry at the corners while the law stays fully covariant, so that light's link charges become fermions under exact turns (Q3)? If so, what matter results, and what does it cost?

## 3. Answers

### Q1. The construction (EXACT; census and searches CHECKED)
**Records.**
- Each corner place records the state |f_v⟩, whose Bloch vector lies along a body diagonal f_v ∈ {(±1,±1,±1)/√3}.
- Under a turn g, the content becomes R_g f.
- Corners carry no covariant charge operator, so nothing else uses these places.

**The dressing rule T_f.** Let R_f be the right-handed 120° turn about f. At a corner, the hop along leg δ carries the field factor E (σ^axis) of leg δ′ exactly when one of these holds:
- f·δ > 0 > f·δ′ ("an out-hop carries all three in-legs");
- f·δ and f·δ′ have the same sign, and δ′ = R_f δ.

For example, at f₀ = (1,1,1): the +x hop carries −x, −y, −z and +y; the −x hop carries only −y.

**The hop.** On the link ℓ between corners v and w = v + 2δ:
- t_ℓ = raise_out_v(ℓ) · ∏_{T_{f_v}(δ,δ′)} E_{v+δ′} · ∏_{T_{f_w}(−δ,δ″)} E_{w+δ″}.
- The reverse hop is t_ℓ†.
- The hop acts on the link and on both corner stars, so it reaches two steps. It depends on the two end records.

**Why it works.**
- T_f is a tournament: of each pair of hops, exactly one carries the other's field factor. So all 15 pairs at a corner anticommute, and θ = −1 on all 20 triples. Transitivity is not needed.
- Covariance is manifest, because R_{gf} = g R_f g⁻¹.

**Census (A45's GF(2) system).**
- Fermion-consistent stabilizers:
  - C3 (body diagonal);
  - D3 (the diagonal's line, without its sign), only if some hops carry Gauss-parity factors;
  - C2′ (face diagonal), only with Gauss-parity factors;
  - trivial (generic direction).
- Not consistent: O, T, C4 and D4 (axis), D2 and C2z. Every one of these contains an axis half-turn, which is lemma F's mechanism.
- Exactly 32 tournaments are C3-invariant, and none is transitive. The rule above is one of them. All 32 transport to the 8 diagonals with 0 conflicts.

**Axis records** (CHECKED by continuous search adapted from A50, 25 starts each):
- C4 with link factors only: four T-junctions stay at +1 (best residual 5.29).
- C4 or D4 with a free corner qubit: no scalar solution (best residuals 4.52 and 5.66).
- Control: under C3, 12/12 starts reach −1 on all 20 junctions.

**The ring term must be dressed (Lemma R, EXACT for any finitely supported field-factor dressing).**
- Suppose every bare ring term commutes with every hop on other links.
- Then each hop's dressing equals its own link plus Gauss parities, because compact-support cohomology of Z³ vanishes in degrees 1 and 2. Such a hop is a boson.
- So fermionic charges force the dressed ring R̃_p = L_p + L_p†, where L_p is the product of the four hops around p: the bare ring flip times six off-loop field factors.
- Example, the xy plaquette (0,0,0)–(2,0,0)–(2,2,0)–(0,2,0) at f₀: factors on legs (0,0,0)+z; (2,0,0)±z; (2,2,0)−z; (0,2,0)+y and −x.

### Q2. Verification (CHECKED)
**Symbolic Pauli arithmetic on coarse tori 3³ and 4³** (all 32 rules; uniform and random backgrounds):
- Hops anticommute exactly when their links share a corner (0 violations).
- 1280/1280 junctions are −1.
- Each hop flips the Gauss parity exactly at its two ends.
- Covariance with the records turned too: 0/9792 mismatches, covering 24 turns about a corner, 24 about a cube centre, and the translations.

**Dense checks with true U(1) operators and exact SU(2) lifts.**
- Corner star (6 qubits):
  - covariance residual 1.3e-15 over 24 turns × 8 records × 6 hops;
  - the phases are ±1 and ±i; link rotations exp(iφE/2) remove them (ARGUED; stabilizer argument);
  - ‖[G_v, t] − t‖ = 0;
  - 960/960 junction phases are −1, residual 0.
- One coarse cube (12 qubits), 24 turns about its centre with the 8 records turned:
  - hop and loop residuals ≤ 1.1e-15;
  - corner junctions 8/8 = −1.

**Closed loops** (Z₂ form, exact phases):
- S_p² = 1.
- S_p commutes with every hop, every Gauss parity and every other S_q.
- The product over each cube's six faces is +1, and so is the product over whole torus planes.
- This is the Bravyi–Kitaev superfast algebra (COMPARATOR).

**Exact free-fermion test** (one cube, Z₂ form):
- In the 2- and 4-charge sectors, the encoded hopping Σ(i/2)A_ℓ(B_v − B_w) has exactly the union, over the 32 flux classes, of free-fermion spectra (deviations 2.0e-14 and 4.8e-14).
- It differs from hard-core bosons by 0.68 and 0.64.
- The S_p = +1 sector equals zero-flux fermions (3.6e-15). The S_p = −1 sector equals π flux through every face (2.5e-15).

### Q3. What matter results
**Zero flux:** one band, −2t Σcos k (coarse spacing a). It has no nodes, and an isotropic mass 1/(2ta²) at the bottom. It is not Dirac.

**π flux:**
- The bands are |E| = 2t√(Σcos²k) (CHECKED to 5.8e-15).
- There are two four-fold nodes per magnetic zone, with isotropic cone speed 2ta in all five directions tried.
- This is Kawamoto–Smit doubling: two four-component Dirac fermions, equivalently four Weyl nodes, two of each hand. The charges are electron-like, but doubled.
- Grades: EXACT in the Z₂ reduction, where fluxes are conserved; ARGUED (static flux, mean field) for spin-½ U(1) links.

**Which sector:** the sign of the dressed ring coupling decides (ARGUED). Light itself is indifferent to that sign. On the cubic lattice a diagonal period-2 sign pattern removes it (EXACT).

**Different f (EXACT): equivalent at every wavelength, not just long ones.**
- For two rules T and T′ at a corner, the disagreement pattern q_jk is symmetric. So V = ∏_{q=1} CZ_jk (in the field basis) maps every hop and loop of T onto those of T′.
- CHECKED:
  - 0/1152 mismatches for random pairs of backgrounds and rules on 4³;
  - dense residual 0;
  - identical cube spectra for 4 rules × 11 backgrounds.
- Corollary: the law on a uniform background is exactly invariant under "soldered turn, then that CZ pattern", which is an exact group action. A48 classified on-site relabelings only, so this two-place relabeling lies outside its classification.

### Q4. The price, in plain terms
**Records.**
- One at every corner place (1 place in 8), each locking one of 8 diagonal directions. Any mixture works.
- A corner without such a record has no fermionic rule, so its hop menu would be empty.

**Symmetry.**
- A uniform background keeps 3 of the 24 turns about each corner, plus the 2-step shifts. A mixture keeps none.
- Neither difference is observable (Q3).

**The gate.**
- Corners are never next-door neighbours, and the links between them must never record, because they carry light.
- So "records form only next to records" must be counted on the corner grid (reach 2, decision 22), or the background is supplied.
- A turn-respecting law cannot pick a diagonal, so the first record's axis must be supplied. Later corners could copy an axis from a recorded corner, with equal odds for f and −f.
- Once the background exists, empty space stays quiet. All dressings are field factors, so the charge-free sector is preserved and charge-gated weights never fire (EXACT, as in A45 §3.2).

**Light.**
- The ring term gains six field factors. It depends on four records and reaches √5 from its face place, instead of 1.
- It is covariant as a function of the records.
- In empty space it equals the bare ring up to a diagonal sign χ, with 0 sign inconsistencies on:
  - 2×2×2 (864 states, complete);
  - 2×2×3 (34,080 states, complete);
  - 2×2×4 (capped at 250,000 states).
- χ is expected to be non-local, because the bosonic- and fermionic-charge Coulomb phases differ (COMPARATOR: Wang–Senthil). I did not test this.
- **So does the ring term still respect every turn?** Exactly, only as a function of the records. On the background it keeps C3 plus the CZ-modified turns. In empty space its spectrum is that of the fully covariant bare ring.

**Hops** reach two steps from their link place (decision 22).

### Q5. Controls (CHECKED)
- **No records** (O-covariant dressings): the census is inconsistent, and 20 dense samples give +1 on every junction. This reproduces lemma F.
- **Extensions that break covariance:**
  - The Bravyi–Kitaev total order has 16 transport conflicts: the stabilizer assigns it 3 different rules.
  - Forcing C3 covariance by summing its images leaves 10/20 junctions non-scalar (residual up to 4).
  - Using one fixed rule for every record gives covariance residual 1.000.
  - Holding the records fixed while turning gives 4032/4608 mismatches.
- **Bare hops** give hard-core boson spectra (2.7e-14), not fermion spectra (0.68 apart).
- **Bare ring** anticommutes with off-loop hops at every plaquette (486 pairs on 3³).

## 4. Methods
- A45's GF(2) system (via `a48lib.link_system`), and enumeration of all 2¹⁵ tournaments.
- Symbolic Pauli strings with exact phases on coarse tori.
- Product-operator and dense numerics with exact SU(2) lifts.
- Sector diagonalization on one cube.
- Breadth-first sign-consistency search over ice states.
- A50's Levenberg–Marquardt search, with groups C4z, D4z and C3 added.
- Bloch bands.

## 5. Checks
All runs used `run_small.sh` (load 2.7–4.7, free memory 32–38%). Memory is in MiB.

| Script | Wall | Peak | Key numbers |
|---|---|---|---|
| c1_census | 0.25 s | 35 | census table; 32 C3 rules; control: 16 conflicts |
| c2_symbolic 3 / 4 | 0.50 / 2.60 s | 34 | 0 violations; 540/540 and 1280/1280 junctions −1; 0/9792 mismatches; cube and plane relations +1 |
| c3_dense | 1.32 s | 35 | residuals ≤ 1.3e-15; 960/960 junctions −1; controls |
| c3b_cube_spectrum | 3.24 s | 250 | fermion and boson matches; zero-flux and π-flux sectors |
| c4_ring_equiv | 41.7 s | 48 | 0/1152 mismatches; 0 sign inconsistencies |
| c5_bands | 7.30 s | 51 | formula to 5.8e-15; cone speed 2.0 in all directions |
| c6_axis_search (5 runs) | 2.5–22.4 s | 73–76 | C3 reaches −1; C4 and D4 do not |
| c7_explicit | 0.18 s | 28 | explicit rule = transported rule; covariant |

**Memory overshoot:** the first full-precision c3b run took 7.95 s and about 490 MB, which is over the 300 MB guide. The lean rerun peaked at 232 MB; the run in the table (with the π-flux check added) peaked at 250 MiB.

**Fixes on the way:** one crashed c3b run (it asked for a 3-charge sector, which is empty, since charges come in pairs), one crashed c6 run (empty array), and one c3 orientation bug, which showed residual 1 until I compared against the adjoint hop for reversed links.

## 6. Open edges
1. Whether χ is local, and whether it stays consistent on larger tori (the 2×2×4 run was capped).
2. The photon itself is still not established; the dressed ring inherits the bare ring's status.
3. Charges coupled to dynamical spin-½ light (flux selection, dressing, confinement) were treated only at mean field.
4. Formation of the corner background is not modelled: the seed, and copying an axis across a two-step gap under Q7. This needs an owner reading.
5. Face and cube places used as helper qubits might keep the ring term bare. Not explored.
6. Line-only (D3) and face-diagonal records need Gauss-parity factors. Not built out.
7. Doubling is unchanged: two Dirac tastes, net handedness zero.
8. The "turn plus two-place relabeling" reading is a new looser reading. Whether it counts is the owner's call.

## 7. Plain-language summary
I tested whether directions locked into records at the grid's corner places can make light's charges behave like electrons while the rule still respects every turn. They can. Each corner records one of the eight cube diagonals. How a charge's jump is dressed then depends on that diagonal, and turning everything together, records included, leaves the rule unchanged. Every exchange test gives the electron sign. There are two surprises. First, the stored directions change nothing measurable, because any two choices are related by a fixed relabeling. Second, light's own loop rule must be dressed too, though in empty space it behaves exactly as before. With the right sign on light's loop rule, the charges move like massless electrons, doubled as usual on a grid.

Everything is in `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A52/`:
- NOTES.md
- a52lib.py
- c1_census.py
- c2_symbolic.py
- c3_dense.py
- c3b_cube_spectrum.py
- c4_ring_equiv.py
- c5_bands.py
- c6_axis_search.py
- c7_explicit.py
- an out_*.txt and time_*.txt file for each run