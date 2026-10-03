# A10 report: cycling partner pairs on Z³, one qubit per site

## 1. Question

Can a ticked step with one qubit per site on Z³ move records and give Dirac-like low-energy motion, if covariance is required only of the full cycle of sub-steps and not of each one? The example schedule cycles partner pairs x-even, x-odd, y-even, y-odd, z-even, z-odd. If so:
- Which group is the cycle covariant under?
- How many low-energy cones (doublers) does it have?
- How does it relate to staggered (Kogut–Susskind-type) structures?

## 2. Answer

**Conditional.**

**Motion: yes [EXACT].** Cycle the 2-site partial swap G(θ) = exp(−iθ·SWAP). These are the number-conserving 2-qubit gates that commute with any on-site rotation action and with reversing the bond. Under that cycle a record's possibilities move ballistically, and a record never moves more than one site per tick.
- A3 Step 10 is evaded, not violated: no single tick is covariant.
- In the one-record sector the plain cycle is exactly covariant under translations by 2 and all 24 rotations about cube centres.
- Unit translations hold up to relabelling which partner set comes first.

**Dirac-like motion: not from the plain cycle [EXACT].** Its one-record step factorizes into three independent 1D walks, U = W⊗W⊗W.
- At low energy it carries eight one-way movers locked to the body diagonals, not a cone.

**An isotropic cone needs the Kogut–Susskind sign pattern on the gates (a π flux on every plaquette).**
- With time-symmetric axis blocks the cone is isotropic at linear order [EXACT, CHECKED].
- It is one eightfold point: two 4-component Dirac cones, i.e. four Weyl nodes, two of each hand. ν₃ = 0 [EXACT]. This is the 3D Hamiltonian staggered count (a Dirac pair), not 8 tastes.

**What the signs cost:**
- Covariance holds only up to re-phasing the excited possibility site by site. That re-phasing is unavoidable [EXACT] and invisible to records started from record configurations [EXACT].
- They need the record-basis ("one possibility") reading.
- Translations survive only by 2.
- Odd rotations act only together with time reversal.
- Cycles with the C₃ symmetry carry an energy-linear branch split ∝ n_x n_y n_z [CHECKED]. Palindromic cycles remove that split but cannot keep C₃ [EXACT].

**Many-body:** every variant is a finite-depth, number-conserving circuit with index 1 [EXACT]. Once two records interact the axis blocks stop commuting, so the full rotation group survives only with odd rotations acting as time reversal [EXACT lemma, CHECKED].

**Admissibility:** the schedule-covariant reading of the axiom is a **named conditional** (S16).

## 3. Derivation

**Setup.**
- Layer L_{a,p} applies one gate to every pair (s, s+e_a) with s_a ≡ p (mod 2).
- Each gate is number-conserving: |00⟩→|00⟩, |11⟩→e^{iφ}|11⟩, one-record block u.
- Cycle: U = L_{z,o}L_{z,e}L_{y,o}L_{y,e}L_{x,o}L_{x,e} (x-even acts first).
- Unit cell: the 2×2×2 block, with in-cell label p ∈ {0,1}³ and cell momentum K. K = 2k, where k is the site momentum.

**S1. Gate family [EXACT].**
- The 2-qubit unitaries commuting with u⊗u for all u ∈ SU(2) are phase·exp(−iθ·SWAP).
- Under spin-½ soldering these are exactly the covariant gates, because the triplet stays irreducible under the binary octahedral group.
- They conserve number in every basis, so no possibility is privileged, and they are symmetric under bond reversal.
- Their one-record block, relative to |00⟩, is u(θ) = e^{iθ}(cos θ − i sin θ σ_x).

**S2. Why alternation is needed [EXACT, using A3 L1].**
- Each layer is a pair-mixing tick (L1 type (i)) and transports nothing across any cut.
- Two parities in sequence do transport. With full swaps, even-x content moves +2 per x-block and odd-x content moves −2: two counter-flowing lanes with zero net flow (index 1, consistent with D9 and D12).
- Direction is carried by the record's sublattice, not its content. So D24–D26 are evaded by the 2×2×2 cell, not contradicted. The cycle turns Step 10's "multi-site cell" option into the unit of covariance.

**S3. One-record factorization [EXACT; CHECKED 2e-15].**
- If a bond's gate depends only on its axis and parity, then L_{x,p} = w_p⊊1⊗1, and likewise for y and z.
- Layers of different axes therefore commute.
- For every ordering of the six layers, U = W_x⊗W_y⊗W_z with W = w_o w_e.

**S4. The 1D walk [EXACT].**
- w_e = e^{iθ_e}exp(−iθ_eσ_x) and w_o(K) = e^{iθ_o}exp(−iθ_o(cos K σ_x + sin K σ_y)).
- Dispersion: cos ω = cos θ_e cos θ_o − sin θ_e sin θ_o cos K.
- At K = π, W(π) = e^{i(θ_e+θ_o)}exp(i(θ_o−θ_e)σ_x), so the gap is 2|θ_e−θ_o|.
- Massless iff θ_e ≡ θ_o (mod π). That is exactly the condition for a unit translation to act as a schedule relabelling.
- The massless point is a linear crossing at k = ±π/2. Its maximum group velocity is sin θ cells per W, i.e. 2 sin θ sites.
- Each line carries one 2-component Dirac mover with no doubler: the 2-site cell absorbs it.

**S5. Plain 3D bands [EXACT; CHECKED].**
- Eigenphases are Σ_a s_a ω(K_a), with s ∈ {±}³.
- For uniform θ, U(K*) = e^{6iθ}·1 at K* = (π,π,π), which is site momentum k = (±π/2)³.
- Near K* the bands are eight planar sheets, Ω = sin θ (s·q): eight one-way movers along the body diagonals, at 2√3 sin θ sites per cycle.
- The zero-quasienergy set is made of surfaces (four planes through K*), not points.
- The velocity matrices commute, so no choice of angles gives an isotropic cone.

**S6. Plain one-record covariance [EXACT; CHECKED 3e-16].**
- Rotations about a cube centre (½,½,½)+2Z³ preserve every layer type. These are site rotations composed with odd translations, i.e. rotations combined with sublattice shifts.
- All 24 are exact symmetries, together with translations by 2Z³. The group is (2Z)³⋊O, an index-8 subgroup of the lattice group.
- T_x U T_x⁻¹ = L_{x,e} U L_{x,e}⁻¹, which is the same cycle started one sub-step later.

**S7. Many-body: the schedule-word lemma [EXACT; CHECKED].**
- With two or more records, the axis blocks X, Y, Z do not commute: ‖[X,Y]v‖/‖v‖ = 0.35 in the 2-record sector, θ = 0.6, on a 4³ torus.
- A lattice symmetry permutes the layers. It is a symmetry "up to relabelling" iff it maps the cyclic word to a rotation of itself (unitary) or to a rotation of the reversed word (antiunitary: with symmetric layers U^T is the reversed product, i.e. time reversal).
- Lemma part 1: the symmetries realized unitarily embed in a cyclic group. So:
  - the full S₃ image of O is never realized unitarily;
  - a palindromic word can never carry C₃;
  - at most a Z₂×Z₂ of the 8 translation parity classes can survive, even allowing reversal. Interacting records therefore always distinguish some sublattices.
- Lemma part 2: for the word XYZ:
  - (2Z)³⋊T is realized as relabellings, where T is the 12-element tetrahedral group and C₃ shifts the schedule by 2 sub-steps;
  - C₄ and the 180° turns about face diagonals map U to a relabelled T₁₁₁U^T T₁₁₁⁻¹ (CHECKED 5e-16), and to no relabelling of U itself (CHECKED, residual 0.35);
  - after one cycle, 2-record odds differ from the C₄-rotated odds by at least 0.009 (CHECKED);
  - no unit translation survives.
- At θ = π/2 (the pure conveyor) the many-body blocks are permutations and do commute.

**S8. An isotropic cone needs position-dependent signs [EXACT; CHECKED].**
- Ω = ±v|q| at linear order needs anticommuting velocity matrices. S3 gives commuting ones.
- The Kogut–Susskind signs are η_x = 1, η_y = (−1)^{s_x}, η_z = (−1)^{s_x+s_y}. The gate on a bond with η = −1 is Z G Z.
- Closed form, with factor order (z, y, x) (CHECKED 1e-15):
  - U(K) = ∏ e^{iθ}exp(−iθD_{a,p}(K));
  - D_{x,e} = X_x and D_{x,o} = cos K_x X_x + sin K_x Y_x;
  - y-layers carry a Z_x string; z-layers carry Z_xZ_y.
- D's of different axes anticommute (CHECKED 8e-16).
- In the Trotter limit, θΣD has spectrum ±2θ√(Σcos²(K_a/2)), each fourfold. That is the 3D Hamiltonian staggered (π-flux) spectrum (CHECKED 6e-15).

**S9. The Floquet cone at K* [EXACT; CHECKED].**
- Each axis block equals e^{2iθ}·1 at K*, because D_{a,o}(K*) = −D_{a,e}. So U(K*) = e^{6iθ}·1 and the linear term is a sum over blocks.
- **Block in order even, odd:** H₁ = sin θ Σ_a q_a(cos θ A_a + sin θ Z_a), where A_a = ∂D_{a,o}/∂K_a at K*.
  - The A_a anticommute; the Z_a commute and anticommute only with their own A_a.
  - Result: an anisotropic, split cone. At θ = π/4 the body-diagonal slopes are ±1.155, ±0.577 ×2 and 0 ×2.
- **Time-symmetric block (even at θ/2, odd at θ, even at θ/2):** H₁ = sin θ Σ q_a A_a, so H₁² = sin²θ q².
  - This block equals the order even, odd, odd, even with one gate angle on every tick.
  - Result: an isotropic fourfold cone at speed sin θ cells = 2 sin θ sites per cycle.
  - Checked over 205 directions at θ = π/8, π/4 and 3π/8: every slope equals sin θ.

**S10. Cone count and chirality [EXACT for the linear theory; CHECKED].**
- χ = iA_xA_yA_z commutes with H₁. Each χ-sector holds two Weyl nodes of one hand: 2 left + 2 right, i.e. two Dirac cones.
- The eight components are the eight corners k = (±π/2)³.
- The Chern number of the lower four bands on a cube around K* is 0.0000.
- ν₃ = 0 for every cycle [EXACT]: each layer contracts to 1 as θ→0, so no Suslin argument is needed. Numerically |ν₃| < 1e-6 for 8 cycles, with the normalization calibrated to −1 on a degree-one map.
- The plain sheets have no point nodes at all.
- Node census for the signed time-symmetric cycle:
  - for θ ≤ 0.7, quasienergy 0 occurs only at K* and the π-gap is open;
  - by θ ≈ 0.8, Floquet wrap-around adds zero- and π-states elsewhere.
- The signed even-then-odd cycle at θ = π/4 has touchings along the body-diagonal lines.

**S11. Masses [EXACT at K*; CHECKED].**
- Two kinds of mass are available:
  - unequal even/odd angles, B_a = D_{a,e};
  - a sublattice phase, ε = (−1)^{s_x+s_y+s_z}.
- Both anticommute with every A_a and with each other: 7 mutually anticommuting 8×8 matrices.
- So each gaps all eight bands equally (CHECKED: ±0.08, each fourfold). Every available mass hits both Dirac copies equally.
- Masslessness needs one gate for every pair. It is not protected by the surviving symmetry.

**S12. Order effects beyond linear order [CHECKED].**
- C₃-symmetric time-symmetric cycle (9 layers): the upper cone splits 2+2 as δΩ = ±sin²θ|q|²n_xn_yn_z.
  - The ratio is constant over 40 random directions (sd ≤ 3e-6).
  - ξ = sin²θ at θ = 0.1, 0.2, 0.4 and π/4.
  - Same class as A5 T6.4.
- Palindrome XYZZYX (18 layers):
  - no split (< 5e-7);
  - fourfold degenerate at every K;
  - velocity anisotropy 0.4% at q = 0.45;
  - but its symmetry, up to relabelling and re-phasing, is only 8 of the 24 rotations: the dihedral group about the middle axis, as the lemma requires.

**S13. The signs and covariance [EXACT; CHECKED].**
- (a) Symmetries map the pattern to Z-re-phased copies. Checked: 12/12 even-permutation rotations hold with dressing plus relabelling, 0/12 odd ones (residual 0.72), and unit translation fails even with dressing (residual 0.12).
- (b) The re-phasing is unavoidable. The cube-centred T group acts freely and transitively on the 12 cube edges, and on the faces with 2 edges of each orientation. So every T-invariant sign or U(1) phase pattern has zero flux through the cube faces, while anticommuting A_a need flux π there. The flux-π requirement is exact for signs and argued for general U(1) phases.
- (c) Odds of record histories that start from record configurations are unchanged by the re-phasing, because Z commutes with every record projector. Snapshots with shared possibilities do need it.
- (d) Under spin-½ soldering, Z G Z is not covariant.

**S14. Many-body legitimacy [EXACT].**
- Finite depth: 6, 9 or 18 layers of disjoint-pair gates. This is a local reversible change with index 1 on every axis.
- Number is conserved for any |11⟩ phase, so interacting versions keep it.
- Jammed (fully recorded) regions are frozen up to phase, consistent with I5.
- Per tick, pairs are closed:
  - a record moves at most one site, to its current partner (I2);
  - the move odds come from the pair block (I3);
  - two records never compete for one site.

**S15. Motion and speed [CHECKED].**
- Under R3 (uncut possibilities guide the record), a single-site start spreads ballistically. ⟨r²⟩/t² tends to:
  - 3.52 (plain, θ = π/4);
  - 1.38 (signed, π/4);
  - 0.135 (signed, θ = 0.3).
- Pure-sheet packets of the plain cycle move along a diagonal whatever their momentum direction: |cos(v,n)| = 0.93 for a generic n, |v| = 1.94 against 2√3 sin θ = 1.96.
- Signed packets move parallel to their momentum (|cos| ≥ 0.998).
- Smooth possibility spreads with no modulation sit at a band edge and move slowly.
- Under R1 (a cut every tick) motion is diffusive: ⟨x²⟩/n = 0.94 at θ = 0.6 and 2.00 at π/4. The exception is θ = π/2, a deterministic conveyor at 2 sites per cycle per axis.

**S16. Reading of Admissibility [ARGUED → NAMED CONDITIONAL].**
- No single object meets both literal clauses together with motion:
  - a tick that is nearest-neighbour, homogeneous and covariant is trivial (Step 10);
  - the cycle is covariant but reaches 2–3 sites per axis.
- **Schedule-covariant reading:** the rule is the periodic schedule; nearest-neighbour holds per tick; each symmetry maps the phase-τ tick rule to the phase-r_g(τ) rule.
  - Equivalently, the film has screw symmetries: a rotation combined with a shift of the tick count.
  - Once records interact, odd rotations must also be allowed to reverse the schedule.
- Choices it introduces, none fixed by the supplied structure:
  - **N1** a global schedule phase, with phase-locked clocks (a mismatch is a defect) [ARGUED];
  - **N2** the schedule word (the xyz vs xzy handedness, time-symmetric blocks, palindrome or not);
  - **N3** one gate angle for every pair;
  - **N4** the sign pattern, with covariance up to re-phasing;
  - **N5** a sublattice labelling in the many-body sector.
- Q3's "glued to rotations" weakens to "glued up to the schedule phase".
- I2 needs ticks = sub-steps.
- A record law that forms records only at cycle boundaries picks up a cycle-scale anisotropy unless formation is allowed at every tick [ARGUED].

## 4. Checks

All runs were in `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A10/`, with `nice -n 10`, the four thread caps set to 1, and a 60 s alarm. Each took under 7 s; peak memory was 277 MB.

| Script | What it checks | Result |
|---|---|---|
| `cyc.py`, `vcyc.py` | Bloch layer builders, ν₃ integral | n/a |
| `t1_plain.py` | Factorization U = W⊗W⊗W, all 6 axis orders | 2.0e-15 |
| | 1D dispersion law | 7.8e-16 |
| | Gap at K = π | 2\|θ_e−θ_o\| |
| | Sheet slopes at K* | sin θ(s·n) to 9e-11 |
| | Max 1D group velocity | sin θ |
| `t2_signed.py` | Anticommutation of D's | 7.8e-16 |
| | Kogut–Susskind spectrum in the Trotter limit | 5.8e-15 |
| | Even-then-odd cone shape | split, anisotropic |
| `t3_cones.py` | Isotropy of the time-symmetric signed cone, 205 directions | exact |
| | ν₃ for 8 cycles | 0 (6 decimals); calibration −1 |
| `t4_nodes.py`, `t4b_zero.py`, `t4c_split.py` | Node census | as in S10 |
| | Chern number of lower four bands at K* | 0.0000 |
| | Branch split δΩ | ξ = sin²θ, n_xn_yn_z law |
| | Palindrome split | absent |
| `t5_sym.py` | Bloch symmetry search: 24 rotations × relabellings × 128 sign dressings, plus unit translation | as in S6 and S13 |
| `t6_mb.py` | 1- and 2-record sectors on a 4³ torus | as in S7 |
| `t7_real.py`, `t7b_packets.py` | Real-space runs match Bloch form | 6e-15 |
| | Single-site spread, band-projected packets | as in S15; packet speed magnitudes are not resolved on the coarse 32-cell grid, so speed claims rest on band slopes |
| `t8_vel.py` | Finite-q cone velocities | time-symmetric: mean isotropic to 0.3%, split ∝ q; palindrome: split 0, anisotropy 0.4% |
| `t9_deg.py` | Degeneracy at generic K | plain: none; time-symmetric signed: 2-fold; signed palindrome: 4-fold |
| `t10_pal.py` | Palindrome symmetry (8/24 rotations), spectrum invariant under all 24, clean for φ ≤ 0.45 | as stated |
| `t11_misc.py` | Closed form | 1e-15 |
| | Mass gaps all bands equally | ±0.08, fourfold |
| | R1 is diffusive | as in S15 |

`big_two_record.py` is **not run**. It is the 2-record sector on an 8³ torus (dimension 130,816) for bound states and for how C₄ breaking depends on θ.

## 5. Real-physics match

- **Doubling.** The signed cycle gives a Dirac pair (2 left + 2 right) with ν₃ = 0. Net-handed matter cannot come from any one-qubit-per-site cycle of this kind, consistent with A1 D20. Comparator, not adopted: this is the 3D Hamiltonian staggered count (Kogut–Susskind 1975; Susskind 1977) and Nielsen–Ninomiya doubling (1981).
- **1D comparator.** The 1D brickwork of partial swaps is the integrable XXX Trotterization (Destri–de Vega 1987; Vanicat–Zadnik–Prosen 2018).
- **Dispersion.** C₃-symmetric cycles have δv/v ∝ sin θ·(qa)·n_xn_yn_z. That is energy-linear and cubic-anisotropic, the class of A5 T6.4. For photon-like content at a Planck-scale tick, the bounds in A5 T6.5 effectively exclude it unless it is suppressed. Palindromic cycles leave only quadratic departures.
- **Frame.** The covariant cell singles out the lattice rest frame (A5 T6.1).
- **What would falsify these results:**
  - a strictly local one-qubit-per-site cycle with ν₃ ≠ 0, or a lone Weyl node;
  - a T-invariant phase pattern with flux π through the cube faces;
  - an observed energy-linear cubic splitting would favour the C₃-symmetric class, and its absence at E/E_Pl sensitivity disfavours that class.

## 6. Open edges and next steps

1. Masses that gap only one of the two Dirac copies (all masses tried here hit both equally).
2. Order effects at q³ in the palindrome; whether some C₃-symmetric word that is not a palindrome cancels the q² split.
3. Two-record bound states and how C₄ breaking grows with θ (`big_two_record.py`).
4. Locally clocked schedules: phase-locking and defects (I1 local ticks).
5. Spin-½-covariant variants using bond-direction spin gates. These lose number conservation.
6. When records form relative to the schedule (every tick vs cycle boundaries), with the A3 Step 11 joint rule applied on the cycle.

## 7. Plain-language summary

If each tick pairs every site with one neighbour, and the pairing keeps changing (east–west twice, then north–south twice, then up–down twice), a record can move one site per tick, even though each site holds only one possibility. No single tick treats all directions alike. A whole round of ticks does, once you allow for which tick you call the first. With plain pairings, a moving record drifts along the corner-to-corner diagonals of small cubes, so its motion is lopsided rather than the same in every direction. If each pairing also carries a fixed pattern of plus and minus signs, the shared possibilities carry ripples that travel at one speed in every direction, like light. But they always come as two copies with equal left- and right-handed parts. The price is a supplied clock that says which pairing acts now, plus a sign pattern that a rotation reproduces only after re-labelling the signs of the shared possibilities.