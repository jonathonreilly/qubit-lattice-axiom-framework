*(Saved by the coordinator from the agent's final message.)*

# A38 report: patterned calm backgrounds and light-like ripples

**Paths.** SP = `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad`.
- Library: `SP/c8/A38/lib38.py`.
- Scripts: `t1_strict_class.py`, `t2_magnons_pair.py`, `t3_star_family.py`, `t4a_rigidity.py`, `t4b_records.py`, `t5_family_spectra_records.py`, `t6_isotropy.py`, `t7_isotropic_point.py`, `t8_isotropy_with_nn.py`, `t9_clifford.py`.
- Each script has `out_*.txt` and `time_*.txt` files; runner `run.sh`.
- No git, no repo edits, no review or audit lanes.

**Grades.** EXACT, CHECKED, ARGUED, SUPPLIED, COMPARATOR. All models are supplied toys. "Magnon" means a single flip over a calm product state, treated at harmonic order.

## 1. Question

Take a period-2 product texture (one direction m_r per site of the 2×2×2 cell). It may break translations down to 2Z³. Each of the 24 glued turns must map it to one of its own translates.
- Is it exactly calm under a homogeneous glued law: the pair terms Jσ·σ + Kσ^aσ^a + D(DM), optionally with star-local three-spin terms?
- Do its single ripples then see π on every face and form light-like cones at zero cost, with no sign pattern on the law?

## 2. Answer

**No π twist, for the whole class (EXACT). A partly light-like point appears only with star terms and tuning (CHECKED).**

1. **The class has exactly one member (EXACT).** The state-level condition admits one texture up to translation. I call it H8: m^a(r) = (−1)^{r_a}/√3, so the 8 sites carry the 8 body diagonals, one each.
   - The uniform vacuum of A31 fails the condition.
   - A25's role layout cannot be a product texture: vertex and cube places would need a direction kept by all 24 turns.
2. **Its only calm pair law is J(σ·σ + σ^aσ^a), i.e. K = J, D = 0 (EXACT).**
3. **The face twist is ±2π/3 under every glued covariant law, never π (EXACT, symmetry argument; CHECKED).** This holds at any range and body number, whenever nearest-neighbour hops are nonzero. The sign alternates with the parity of the face's corner.
   - Reason: each bond is swapped end-for-end by a half-turn of the background, which pins each hop's phase.
   - A33's parity route does not apply. No half-turn about a face diagonal fixes a site of H8.
4. **With the pair law, ripples form zero-cost nodal lines, not cones (CHECKED).**
   - The lines run along the body diagonals.
   - Dispersion is linear across a line and flat along it.
5. **With star terms there is a partly light-like point, at a price (CHECKED).**
   - The star-local glued terms that keep H8 calm form a 24-dimensional family.
   - Every member has an 8-fold level at the zone corner.
   - Tuning that level to zero cost, then making it isotropic, gives two linear branches of 2 modes each, E = ±1.938|q| in every direction. The other 4 modes at that point are heavy (quadratic).
   - Two heavy zero-cost modes always sit at zone centre.
   - **What is supplied:** the 1-of-8 state texture, three-spin or longer-range in-star terms, and tuned coefficients. No sign pattern is supplied.

## 3. Derivation

**D1. The strict class is H8 (EXACT; CHECKED t1).**
- The turns act on the 8 cell sites through coordinate permutations. A direction m(r₀) must be fixed by the stabilizer of r₀.
- Among subgroups of O, only cyclic ones fix a direction. Orbit sizes 1–6 need non-cyclic stabilizers (T, D3, D4, or C4 leaving a 2-orbit), so the 8 sites form one orbit with stabilizer C3.
- So every m(r) is a body diagonal and all 8 appear.
- Exhaustive check over 8! = 40,320 bijections: exactly 8 pass, the translates of H8.
- Controls: the uniform state, Néel along (111) and a random texture all fail.
- The exact site stabilizer is C3, of order 3. Face-diagonal half-turns fixing a site: 0 of 48.

**D2. Calm pair laws (EXACT, by hand and t1).**
- On a converging x-bond, from (1,1,1) to (−1,1,1), the double-flip amplitude is −2J/3 + 2K/3 + 2iD/√3. It vanishes only at K = J, D = 0.
- Single flips vanish automatically because of the C3 site symmetry. Here the local field is in fact 0.
- Diverging bonds are related by time reversal combined with a (1,1,1) shift.
- t1 singular values are 5.657, 4.619 and 0, giving the null vector (1,1,0).
- Background energy is E₀ = 0.

**D3. Four-sublattice (Klein-type) relabelling (EXACT).**
- Rotating each site by a half-turn about its axis a(r) gives the map s(r) = ((−1)^{y+z}, (−1)^{x+z}, (−1)^{x+y}).
- It sends the law (J, K) to (−J, 2J + K), and maps H8 to Néel order along (111) (t1).
- Hence the patterned calm families at special ratios:
  - K = −2J: the relabelled uniform ferromagnet, for every n. It has 4 directions, fails D1, and gives one quadratic band.
  - K = −3J: Néel along (111) (t1: (0.316, −0.949, 0)). It has the same ripples as H8 and fails D1.
- A general calm search with the D1 condition dropped was not run (open).

**D4. Ripples under the pair law (CHECKED t2; EXACT through D3).**
- In the relabelled frame this is a two-sublattice problem with f(k) ∝ e^{iπ/3}cos k_x + e^{−iπ/3}cos k_y − cos k_z.
- Its zeros lie on cos k_x = cos k_y = cos k_z, which are lines.
- Hops have magnitude 2J and on-site cost 0. Wilson loops have |W| = 16 and phase ±2π/3.
- The spectrum is symmetric about 0 (to 7e-15).
- Transverse slope 1.448, equal in both transverse directions; slope 0 along the line.
- At the zone corner all 8 levels are 0, with slopes 4.0 along (100), 2.83 along (110) and 0 along (111).
- At zone centre there are 2 heavy zero modes. For the pair law their classical origin is EXACT: the relabelled Néel family has energy Σ_a(3n_a² − 1) = 0 for every n.

**D5. Face-twist rigidity (EXACT argument; CHECKED t3, t4a, t8).**
- The half-turn about (0,1,1) through (½,0,0) maps H8 to itself and swaps the ends of bond (0, e_x). The same holds mod 2 for every bond of its orbit.
- So for any law commuting with it, t_yx = φ·conj(t_yx). Each hop is e^{iθ_b}λ_b with λ_b real and θ_b fixed by the background alone.
- The two parallel bonds of a face are both converging or both diverging.
- So W = λ_a²λ_b²e^{iΘ}, with Θ = ±2π/3 by corner parity.
- Checks:
  - Random covariant laws, calm or not, always show ±2/3 π.
  - Over the calm family the nearest-neighbour block has rank 1 (singular value 9.80, then 0), with phase π/6 mod π.
  - A targeted search for π on all faces is stuck at residual 4.9.

**D6. The star-local calm family (CHECKED t1, t3–t9).**
- Glued covariant terms counted by shape:

| Shape | Count |
|---|---|
| NN pair | 3 |
| Pair at distance √2 | 4 |
| Pair at distance 2 | 3 |
| Three-spin L | 12 |
| Three-spin straight | 2 |
| Three-spin octant | 11 |
| Three-spin (x−a, x+b, x+a) | 12 |
| **Total** | **47** |

- Of these, a 24-dimensional subspace keeps H8 calm. A34's chiral term T alone does not: its triple-flip amplitude is 2.18.
- The one-flip map from the family has rank 5:

| Entry | Rank |
|---|---|
| On-site | 1 |
| Nearest neighbour | 1 |
| Distance √2 | 2 |
| Distance 2 | 2 |

- On-site costs are equal on all 8 sites automatically, since all sites form one orbit. This contrasts with A34 c7, where four roles need three tunings.
- H(R) ∝ I for every member (3.5e-15), so the corner level is 8-fold.
- Members with the corner level at zero:
  - generic ones are anisotropic, with slopes ranging 0.18–6.2;
  - the zero-cost points on a 21³ grid are only zone centre and the corners.
- The isotropic optimum (t6/t7):
  - slopes −1.938 (×2), 0 (×4), +1.938 (×2) over 200 directions, with a spread of 3e-13;
  - the 4 middle modes have curvature 0.53–0.80;
  - it has no pair part, and its nearest-neighbour hop is 0.028, against slopes of 1.94;
  - it nearly splits into two fcc sublattices, each giving (−v, 0, 0, +v).
- Things not found:
  - isotropy with the nearest-neighbour hop held at ≥ 0.25 of the slope scale (best spread 5.7–8.4%);
  - a full 8-mode Dirac cone, i.e. Clifford velocities (12 starts, only a degenerate point).
- This narrows A31 D4. "An isotropic cone needs π per face" holds for nearest-neighbour-only ripple hopping, not with in-star longer hops at a symmetry-enforced 8-fold point.

**D7. Records (CHECKED t5; exact difference method).**
- Under the pair law:

| Record content | Calm? |
|---|---|
| +m (the background's own direction) | Yes (0) |
| −m | No (2.83) |
| +z | No (1.23) |
| Another body diagonal | No (1.89) |

- A scan over the sphere finds the minimum at m itself.
- In the star family, an 8-dimensional subfamily stays calm next to a −m record. It has no pair part.
- Record clusters were not tested.
- A covariant quiet formation weight exists: 1 − P, with P the projector onto the 8 translate star states, rank 8 out of 128 (EXACT).

**D8. Readability (EXACT arithmetic).**
- If a record's content is the local body diagonal, one record fixes the translate relative to any other placed structure.
- With axis menus, one-site odds are (1 ± 1/√3)/2 = 0.789 or 0.211, so the translate shows at first order.
- This is a state-level pattern, so readability is expected, unlike A31's law-level KS.

## 4. Checks

- **Run conditions.** All runs used `nice -n 10`, the four thread caps at 1, a 55 s alarm and a load gate at 6. Loads were 1.9–3.9. Peak memory was 210 MB.
- **Superseded runs.** `t4` hit the alarm with no output; it was split into `t4a`/`t4b`. `t4a` was partly cut off and superseded by `t5`. `t4b`'s box-limited record count (3) is superseded by `t5`'s exact difference method (8).
- **Tolerances.** Zero means ≤ 1e-12. The optimizations (t3, t6, t8, t9) are searches, so their negatives are CHECKED, not EXACT.
- **Not run:**
  - the general patterned calm search without the D1 condition;
  - the dimension of the isotropic set;
  - the size of one-to-two-flip leakage;
  - record clusters.

## 5. Real-physics match (comparators, not adopted)

- **H8** is a triple-q, hedgehog-like texture. COMPARATOR: Berry phases in non-coplanar magnets, i.e. spin chirality acting as an emergent field.
- **D3** mirrors the four-sublattice duality of the Kitaev–Heisenberg model. COMPARATOR: Chaloupka–Khaliullin.
- **Ripple spectra:**
  - nodal-line magnons (COMPARATOR: Mook–Henk–Mertig);
  - multifold, including 8-fold, points at corners of non-symmorphic groups (COMPARATOR: Bradlyn et al. 2016);
  - non-collinear magnon decay, which makes "single ripples" a harmonic-order notion here (COMPARATOR: Zhitomirsky–Chernyshev).
- **Falsifiers.**
  - A glued covariant law giving π on the faces over H8 would contradict D5.
  - In the tuned point, heavy partners sit beside the light-like branch at the same energy. A light sector with no heavy companion at that energy would not match it.

## 6. Open edges

1. A general calm search over all period-2 textures with the turn condition relaxed, including laws with a hidden symmetry.
2. The dimension and stability of the isotropic set, and whether the 4 heavy modes can be removed.
3. The cause of the 8-fold corner level and the zone-centre zero modes when star terms are present.
4. Size of the one-to-two-flip leakage.
5. Record clusters in the 8-dimensional subfamily that stays calm next to −m records.
6. How H8 combines with F6.

**Owner decisions.**
- Whether three-spin or longer-range in-star terms are allowed (A34 C56).
- Whether tuned homogeneous coefficients count as "pattern-free".
- Whether records may hold only the background's own direction.
- Whether a 1-of-8 texture in which all places are alike is acceptable next to F6.

## 7. Plain-language summary

I looked for a calm, patterned empty background in which neighbouring sub-grids point different ways, under a rule that treats every spot and turn alike. If the pattern must look the same after any turn of the grid, apart from a shift, there is exactly one such background: the 8 spots of each small cube point to the cube's 8 corners. One simple rule keeps it calm. Ripples on it get a twist on every square face, but it is always a third of a turn, never the half turn that light-like motion needs, and no rule of this kind can change that (proved). With the simple rule, the ripples form lines of zero-cost motion rather than cones. With richer three-spot rules and carefully chosen strengths, some ripples move the same speed in every direction at zero cost, but heavy, slow ripples sit at the same spot and energy. So no sign pattern needs painting on, but the background, extra kinds of rule terms, and finely set numbers are all put in by hand, and the result is only partly light-like.

---

## ERRATA from review round 8 (A34/REVIEW4.md), added by the coordinator

- D5 'under EVERY glued covariant law': on nearest-neighbour faces, whenever nearest-neighbour hops are nonzero; loops through longer hops are not covered (C133).
- D6 'narrows A31 D4': CHECKED; the isotropic point has 2+2 linear modes plus 4 heavy ones, and H8 is not the ground state there (C133).
- D7 'others do not': under the pair law; an 8-dimensional star subfamily also keeps −m records calm (C133).
- NEW (A34 c11, EXACT): H8 is not the ground state of its calm pair law, for either sign (27 of 64 one-flip states below on 4³), nor at any zero-cost linear touching (A39 positivity lemma). So A38's light-like offers fall under A39 escape (a) (C116).
- The parity route cannot be set up on H8 (no half-turn fixes a site); A38 did not test the route, it showed the route needs a non-pointing background (C117).
