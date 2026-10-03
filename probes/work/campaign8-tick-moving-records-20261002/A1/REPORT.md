# Lane F report (agent A1): flow and index under I4

Scratch scripts are in `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A1/`. No git, no repo edits. Every run took under 60 s and under 120 MB, with `nice -n 10` and all four thread caps set to 1.

## 1. Question

Take I4: the shared possibilities flow, with one site's worth of possibilities per site. What kinds of net flow can a ticked, local, reversible step on Z^3 carry? Can a net flow be compatible with the axioms' covariance: translations plus the 24 proper cubic rotations, soldered so that a rotation turns the lattice and every site's domain together?

Sub-questions:
1. The exact classical flux law.
2. The quantum index.
3. Covariance of flows, including flows whose direction is set by each possibility's own content, and their behaviour under improper rotations.
4. Whether a many-body qubit step can send each qubit's up part one way and its down part the other.
5. What a record moving one site per tick requires of its surroundings.

## 2. Answer

**Conditional no.** Suppose a tick is a reversible local map of site contents with one site's worth per site: a bijection classically, or a quantum cellular automaton or one-excitation walk quantum mechanically.

- **What a net flow is.** It is a conserved, quantized vector: one integer per lattice direction per transverse site, or a power of 2 for qubits.
  - The same amount crosses every cut on every tick.
  - It cannot start or stop anywhere.
  - It cannot be produced by continuous change, or by any schedule of local updates.
  - **Grade:** EXACT. The quantum part uses GNVW as a comparator.
- **Covariance forbids it.** A 180° rotation about a perpendicular axis reverses this vector, so covariance forces it to zero (EXACT).
- **What covariance still allows: zero-net flow.**
  - Counter-passing: a swap in 1D, loops around plaquettes in 2D/3D.
  - Counter-flows whose direction is set by content. These need at least two independent movers per site, because one qubit's complementary parts cannot be sent to different places (EXACT).
- **If a mover's content is one qubit, soldered as spin-1/2:**
  - (a) **No long-range speed.** Every strictly local, reversible, exactly covariant one-excitation step has zero long-wavelength speed (EXACT, derived here). Cubic symmetry ties the slopes on the axis and body-diagonal lines in the ratio 1:√3, while strict locality makes both slopes integers.
  - (b) **The one surviving index is quasi-local only.** The only index compatible with covariance is the 3D winding ν_3, the net handedness at zero quasienergy, which is a mirror-odd pseudoscalar. The normalized content-set shift S/|S| carries |ν_3| = 2, but it is only quasi-local. Every strictly local walk has ν_3 = 0. **Grade:** EXACT, given a cited algebraic K-theory theorem.
  - (c) **Handedness.** Content-set flows tied to the qubit's content are handed (EXACT). Flows tied to direction slots are achiral.

## 3. Derivation

### 3.1 Classical flux (task 1)

Setting: f: Z → Z is a bijection with |f(x) − x| ≤ r. The item at x goes to f(x), and there is one item per site before and after.

**D1. Cut independence. EXACT.**
- Define J(c) = Σ_x ([f(x) > c] − [x > c]), the number of rightward minus leftward crossings of the cut between c and c+1. The sum is finite.
- For a window W = {a+1..b}, use [y>a] − [y>b] = χ_W(y). Then J(a) − J(b) = Σ_x (χ_W(f(x)) − χ_W(x)) = (items in W after) − (items in W before) = |W| − |W| = 0.
- Items that jump the whole window cancel automatically.

**D2. Additivity and values. EXACT.**
- J(f) = |L \ f⁻¹L| − |f⁻¹L \ L| for the half-line L = {x ≤ c}. This relative-index cocycle gives J(f∘g) = J(f) + J(g).
- J is an integer in [−r, r]. The shift by k has J = k.

**D3. No start or stop. EXACT.** If f is the identity on a half-line, or outside a finite set, then J = 0 everywhere. A nonzero net flow is therefore a conveyor through the whole line, every tick.

**D4. Classification. EXACT.**
- Every bounded-range bijection has the form f = T_J ∘ h₂ ∘ h₁, where h₁ and h₂ are layers of disjoint finite block permutations with block length L > 2(r+|J|).
- Proof: g = T₋J∘f has J = 0, so across each block boundary the right-crossers and left-crossers are equal in number. h₁ swaps them pairwise inside windows straddling the boundaries, which puts every item into its destination block. h₂ then permutes within blocks.

**D5. Local schedules cannot make flow. EXACT.**
- A layer of disjoint finite moves has J = 0, so by D2 any finite composition of such layers has J = 0, however the layers are scheduled.
- Bearing on I1: *if* ticks are local, meaning neighbourhoods update on their own schedules through finite moves, *then* net flow is impossible. A conveyor needs one global step in which every cut is crossed at once.

**D6. Z^3. EXACT.**
- (a) For every finite region R, |R \ f⁻¹R| = |f⁻¹R \ R|. There are no sources and no sinks.
- (b) On Z×Z_L², or on a torus with tracked displacements, the flux through the plane x_a = c+½ is the same for every c (slab version of D1).
- (c) On infinite Z^3, the fluxes through a finite plane patch and through its normal translate differ only by a perimeter term, so flux densities are plane-independent.
- (d) A translation-covariant permutation of positions is a shift: f(x) = x + f(0).

**D7. Flow lines. EXACT.**
- A nearest-neighbour bijection splits into two kinds of orbit:
  - finite cycles, which are closed lattice loops of even length (Z^3 is bipartite): a swap has length 2, a plaquette loop has length 4;
  - bi-infinite chains.
- Flows never begin or end. In d ≥ 2, closed loops are localized circulations with zero net flux.

### 3.2 Quantum version (task 2)

The comparator statements here are not adopted; they are listed in the box below.

**D8. GNVW (comparator).**
- ind(α) is computed locally at any cut and is the same at every cut, for any quantum cellular automaton (QCA) on a chain, translation-invariant or not.
- It is multiplicative, and ind(right shift) = d.
- ind = 1 exactly for finite-depth circuits. For qubits, every QCA is a shift composed with a circuit.
- It is constant on continuous paths.
- With one qubit per site: ind ∈ {2^k : k ∈ Z}. At range 1: ind ∈ {½, 1, 2}.

**D9. Meaning for "possibilities flow". EXACT given D8.**
- log₂ ind is the net number of whole sites' worth of possibilities moved right across every cut per tick.
- Flow comes only in whole qubits. Half a qubit, i.e. one Majorana, needs a fermionic grading (index √2).
- A flowing tick is a rigid conveyor composed with local reshuffling that has zero net flow.
- Anything reached continuously from "no change" has ind = 1.

**D10. Localized motion has no flow. EXACT.** A QCA that is the identity outside a finite region is a unitary on that region, so ind = 1.

**D11. Per-direction flux in 3D. ARGUED.** A translation-invariant QCA on Z^3 has a per-direction flux j_a ∈ Z: compactify to Z×Z_L², where ind = 2^{j_a L²}.

### 3.3 Covariance (task 3)

**D12. Net flow is killed by covariance. EXACT.** The soldered 180° rotation about e_y reverses x, and acts on site domains by an on-site unitary.
- Classically: J_x = −J_x.
- Walks: the winding of det W along k_x equals minus itself.
- QCA: on-site unitaries leave the index unchanged and reflection inverts it, so ind_x = 1/ind_x.
- So J_x = 0, and likewise for every direction. Only the three axis C₂ rotations are needed.

**D13. Sum candidate. EXACT, and CHECKED.**
- S(k) = Σ_a(P_a⁺e^{−ik_a} + P_a⁻e^{ik_a}) = C − i s·σ, with C = Σ cos k_a and s = (sin k_a).
- It is covariant: the six terms P_v T_v are permuted by the rotations.
- But S†S = 3 + 2e₂(cos k) ∈ [1, 9], so no normalization constant makes S unitary.

**D14. Normalized sum S̃ = S/√(3+2e₂). EXACT, and CHECKED.**
- Exactly covariant and exactly unitary. Quasi-local: the square root never vanishes, so its Fourier tails decay exponentially. Not strictly local.
- Its nodes sit only at the eight time-reversal-invariant momenta (TRIM):

| Point | Count | W | Chirality | Note |
|---|---|---|---|---|
| Γ | 1 | +1 | +1 | isotropic speed 1/3 |
| X | 3 | +1 | −1 | |
| M | 3 | −1 | | |
| R | 1 | −1 | | |

- |ν_3| = 2 (degree count; the numeric value is +2.0000). This is a net handedness of two units at quasienergy 0.

**D15. Ordered products W_zW_yW_x, all six orders. EXACT, and CHECKED.**
- Unitary and strictly local. They move along body diagonals, and equal the published BCC Weyl walk (comparator).
- Their symmetry inside the soldered O is exactly {E, C₂x, C₂y, C₂z}.
- They fail the 3-fold rotation because the coefficients are rank one, A_v ∝ |s_z⟩⟨s_x|, and no unitary can realize C₃ on them.
- ν_3 = 0: four of the eight nodes at W = +1 lie off the TRIM and compensate.

**D16. Nearest-neighbour no-go, with flavours. EXACT.**
- Coin = spin-½ ⊗ Cⁿ, with O acting on the spin only. Covariance forces A₀ = 1⊗M₀ and A_{±a} = 1⊗B ± σ_a⊗C.
- The e^{2ik_a} coefficient of W†W gives B†B = C†C and C†B = B†C.
- The e^{i(k_a+k_b)} coefficient gives 2·1⊗B†B = 0. So B = C = 0 and nothing moves.

**D17. Support |v|_∞ ≤ 1 (27 vectors, including face and body diagonals). EXACT.**
- The general covariant form has 7 complex parameters: f − iΣ_a s_a h_a σ_a.
- The odd parts of WW† force a common phase.
- The remaining identity f² + Σ(1−c_a²)h_a² ≡ 1 has only the trivial solutions (sympy: 10 coefficient equations, solutions A = ±1 and everything else 0).

**D18. Line-integrality obstruction. EXACT, derived here.** Let W be any finite-range, unitary, translation-covariant one-excitation walk with a spin-½ coin, covariant under the 24 soldered rotations. Normalize W(0) = 1; Schur makes W(0) scalar.
- (i) Covariance kills the scalar linear term. Schur on the vector representation makes the vector part isotropic, and unitarity makes it real: W = 1 − i v k·σ + O(k²).
- (ii) C₄ₓ fixes every point of the line (t,0,0). So W ∈ span{1, σ_x}, its eigenvalues are unimodular trigonometric polynomials, and those are monomials: W = e^{−iptσ_x} with p ∈ Z, and p = v.
- (iii) C₃ fixes every point of the line (t,t,t). So W = e^{−ip′tσ·d̂} with p′ ∈ Z, and matching the linear term gives p′ = √3·v.
- (iv) √3 is irrational, so v = 0.

Consequences:
- The same argument at R gives zero speed there too.
- At X and M, √2-integrality on face-diagonal lines kills the transverse slopes, so no full Weyl crossing sits at any TRIM.
- With inert flavours (coin C²⊗Cⁿ), the signed speeds at Γ sum to zero: tr Y ∈ Z and √3·tr Y ∈ Z.
- Corollary: if all Weyl movers at Γ share one speed, there are as many of one hand as of the other.

**D19. Ranges 2 and 3. CHECKED (search only, not a proof of absence).**
- A randomized least-squares search over the full covariant parameter space finds only near-unitary approximants.
  - At range 2, the best point is a genuine stationary point with residual² 2.2e-10 and |Jᵀr| = 4.5e-16.
  - At range 3, the residual² is 1.2e-16 and still slowly decreasing.
- These approximants have a non-linear axis phase. The slope is about 1.124 at t = 0.3, isotropic with the diagonal to 0.4%, sitting between the integer constraints. They look like truncations of quasi-local walks, which is what D18 predicts.
- Range-2 searches with the exact line conditions imposed all have strictly positive minima: axis branch m = 0, 1, 2 give 5.0e-5, 1.3e-7, 5.5e-3; the zero-speed branch gives ≥ 6.8e-5.

**D20. ν_3 = 0 for every strictly local walk on Z^3, any coin, covariant or not. EXACT, conditional on a cited theorem.**
- det W is a unit of C[z^±], so it equals c·z^m. Write W = W′·diag(det W, 1, …); the diagonal factor has ν_3 = 0.
- W′ lies in SL_N of the Laurent polynomial ring in z₁^±, z₂^±, z₃^±. That group equals E_N (Suslin; comparator).
- Elementary matrices are null-homotopic through invertible matrices, and ν_3 is homotopy-invariant and additive. So ν_3(W) = 0.
- Without the cited theorem, the same conclusion is EXACT for finite circuits and for continuously generated steps, by direct homotopy.
- For two bands, ν_3 is the net chirality of the nodes at quasienergy 0. So strictly local steps have balanced hands at every quasienergy: a discrete-time doubling statement.

**D21. Continuous-time generator. EXACT.** H_W = Σ sin k_a σ_a is covariant, with eight nodes whose chiralities sum to 0. exp(−iλH_W) has ν_3 = 0.

**D22. Improper rotations. EXACT.**
- If inversion acts on M₂(C) by an automorphism commuting with the soldered O action, Schur makes that action trivial. The Bloch vector is then axial, and helicity is a pseudoscalar.
- ν_3 flips under orientation reversal, so an O_h-covariant walk has ν_3 = 0.
- Spin-locked content-set flows are therefore handed. Direction-slot flows (coin = permutation representation on the 6 directions) are achiral.
- A spin⊗slot walk W_θ = D(k)·exp(iθΣ_v σ·v⊗|v⟩⟨v|)·(1⊗Grover) is strictly local, unitary and O-covariant. Its mirror image is W_{−θ}, so it is handed (CHECKED). ν_3 = 0.
- An anti-automorphism action (time-reversal-like) would make the content polar instead. That is a named conditional, not chosen here.

**D23. Lock-and-move channel. EXACT.** This is an I3-type analog, not adopted.
- Kraus operators K_v = 3^{−½}P_v⊗T_v over the six axis possibilities satisfy Σ K_v†K_v = 1, and are permuted by the rotations. So the channel is exactly covariant.
- The odds are ⟨P_v⟩/3; an uninfluenced site gives 1/6 each, matching Q4.
- It is irreversible: a forming record locks one of six non-orthogonal possibilities.
- That six-possibility menu is a choice the axioms do not fix (named conditional).

### 3.4 Many-body (task 4)

**D24. EXACT.** In any QCA, α(1−P) = 1 − α(P) has the same support as α(P). The up and down parts of one qubit cannot go to different places.

**D25. EXACT.** Classically, "↑ moves +1, ↓ moves −1" is not a map into one-item-per-site configurations. With ↓ at x−1 and ↑ at x+1, site x receives nothing.

**D26. EXACT.** With one mode per site, an excitation has no internal content. Its walk is a unimodular scalar, i.e. a pure shift, and covariance makes that shift zero.

**D27. EXACT given D8; CHECKED.**
- **Minimal structure:** two independent movers per site (M₂⊗M₂). This gives net index 2·½ = 1, zero net flow, and a two-layer circuit.
- **Full covariance:** at least 6 direction slots plus vacuum for an achiral flow (consistent with the archived 2026-07-14 audit), or spin ⊗ slots for a handed one.
- A spin doublet alone falls back under D16–D18.

**D28. EXACT; the index value is a comparator.**
- With a graded (fermionic) product, one qubit is two Majorana halves. A Majorana counterflow (γ₁→x+1, γ₂→x−1) is a fermionic QCA with index √2·(1/√2) = 1. So in this encoding one site *can* split into two counter-movers.
- But the grading operator is ∝ σ·n for some axis n. The soldered rotations preserve it only for the stabilizer of that line (D₄), and C₄ about n mixes γ₁ with γ₂. The split is not covariant.

**D29. EXACT.** D12 applies to every qubit QCA.

### 3.5 Counter-passing (task 5)

**D30. EXACT.** If a tick is the identity outside a finite region, then in that tick every plane is crossed equally often in each direction. If the tick equals a global shift T_v far away, apply this to T₋v∘tick.

**D31. EXACT.** In 1D at range 1, finite cycles on a path graph have length 2. A record moves relative to its surroundings only by swapping with a neighbour.

**D32. EXACT.** In Z^3 with nearest-neighbour moves, localized motion consists of closed even loops; the minimal ones are swaps and plaquette 4-cycles. The record's counter-crossing partner can sit elsewhere on the plane, so "flow rather than swap" exists as circulation.

**D33. EXACT; the "relabeling" reading is ARGUED.**
- A global conveyor preserves every relative position, so it moves everything together.
- Since sites are distinguished by lattice structure alone, it amounts to relabeling.
- A covariant classical rule leaves the record-free vacuum fixed: by D6(d) it acts as a shift, and by D12 that shift is zero.

**D34. EXACT.** The four plaquettes containing a directed edge form one orbit under the edge's C₄ stabilizer. A covariant law gives each the same odds, and the realized step picks one (I3-like).

**D35. EXACT.**
- One pinned record blocks both adjacent cuts. At range 1 in 1D, that makes J = 0 everywhere.
- Quantum: a range-1 QCA that fixes the record site's whole algebra splits into half-line QCAs, so ind = 1.
- On Z×Z_L², a pinned record caps the flux of every plane at N_⊥−1, giving a stall line upstream and downstream (relevant to I5).

**D36. EXACT for the index; ARGUED for the reading.** Index 1 means right-moving operator content balances left-moving content. The balancing piece can be a different kind of content, e.g. phase information in a CNOT-type exchange.

> **Comparators (not adopted)**
> - Gross–Nesme–Vogts–Werner, CMP 310 (2012)
> - Ranard–Walter–Witteveen, AHP (2022)
> - Fidkowski–Po–Potter–Vishwanath (2019): fermionic QCA index
> - Freedman–Hastings (2020); Haah (2021+): higher-dimensional QCA
> - D'Ariano–Perinotti (2014); D'Ariano–Erba–Perinotti (2017): isotropic s=2 walks select the BCC lattice
> - Nielsen–Ninomiya (1981)
> - Ginsparg–Wilson/overlap fermions
> - Suslin (1977): SL_n = E_n over Laurent polynomial rings, n ≥ 3; stable form via Bass–Heller–Swan plus stability
> - Archived repo context, not authoritative and not checked against origin/main: `archive/notes/docs/work_history/repo/review_feedback/CUBIC_SPLIT_STEP_QW_QCA_PRIMARY_SOURCE_UNIQUENESS_AUDIT_2026-07-14.md`. It is consistent with D15 and D27.

## 4. Checks

**Classical flux** (`flux_classical.py`): exact integer arithmetic.
- 1D: 200 random bounded-range bijections on Z₉₆, maximum displacement 11. The flux is identical at all 96 cuts and equals the shift.
- 3D: 60 random nearest-neighbour bijections on Z₈³ built from plaquette loops, swaps and a shift. Plane flux is equal on all 8 planes in each direction and equals v_a·L². 600 random boxes have zero net outflow.

**Walk covariance** (`walk_covariance.py`): 24 rotations, 40 random k, tolerance 1e-10.
- S: covariant under 24/24. S†S = 9 at Γ and 3 at (π/2)³; maximum defect 7.9.
- All six ordered products: unitary to 6e-16, symmetric under exactly 4 rotations (identity and C₂ about x, y, z).
- H_W: covariant under 24/24. Chiralities [1,−1,−1,1,−1,1,1,−1], sum 0.

**Exact range-1 family** (`rho1_exact.py`): 10 equations, real solutions only A = ±1.

**Covariant walk searches** (`covariant_walk_search.py`, `polish_rho2.py`, `tau_scan_rho2.py`, `gauss_newton_rho2.py`, `warm_rho3.py`, `polish_rho3.py`, `gn_trunc_rho3.py`, `analyze_rho3.py`, `axis_branch_search.py`, `axis_warm_rho3.py`, `zero_speed_branch.py`):
- "Solution" threshold: residual² < 1e-20. None was found.
- Range 1 minima: 4e-4 to 5e-3.
- Range 2: best stationary point 2.16e-10. Branch minima as in D19.
- Range 3: 1.2e-16, off-grid unitarity defect 3.5e-8, approximant only. With the axis integrality (m = 1) imposed, 2.2e-15; the conflict is on the diagonal, as D18 says.

**GNVW Choi check** (`gnvw_choi.py`): 10-qubit ring, log₂ ind = [I(A′:B) − I(A:B′)]/2.

| Step | log₂ ind |
|---|---|
| Right shift | +1.0000000000 |
| Left shift | −1.0000000000 |
| 1-layer circuit | 0 |
| 2-layer circuit | 0 |
| Shift ∘ random 1-layer circuit | ±1 |
| Two-slot counter-conveyor | 0 |

**3D winding** (`winding3.py`): 48³ midpoint grid.

| Walk | ν_3 |
|---|---|
| S̃ = S/\|S\| | +2.0000 |
| W_zW_yW_x | 0.0000 |
| exp(−1.3i·H_W) | 0.0000 |

**Handed slot walk** (`handed_slot_walk.py`):
- Unitarity defect 2e-15; covariance defect 1e-15 over 24 rotations × 20 k.
- The inversion image differs from W_θ (4.46) and equals W_{−θ} (2e-16).
- At θ = 0 it is achiral (1e-16).

**Not run (too big):** `zero_speed_branch.py 4 5 61` (range 4, roughly 400 MB, several minutes).

## 5. Real-physics match

- **No preferred drift.** Covariant ticks cannot carry net flow, which matches the absence of any preferred vacuum direction (toy-level, ARGUED).
- **Chirality.** Real light matter moves with helicity locked to motion, and the weak sector is net-chiral. This toy gives three results:
  1. A strictly local, exactly covariant tick with one qubit of content per mover has no long-wavelength speed (D18), so a lone Weyl mover at long wavelength is excluded under those conditions.
  2. Strictly local walks of any kind keep hands balanced at every quasienergy (D20). This is a discrete-time analog of Nielsen–Ninomiya.
  3. Quasi-local covariant ticks *can* be net-handed (S̃), analogous to how overlap-type operators evade doubling.
- **Implication for the chirality lane.** It needs one of: per-tick quasi-locality beyond a strict reading of I2, boundaries or defects, or interacting many-body structure. This is the same wall lattice field theory meets.
- **Falsifiers:**
  - A strictly local, exactly O-covariant spin-½ walk with axis winding p and diagonal winding p′ ≠ √3·p would falsify D18. Any candidate is a one-line check.
  - A strictly local walk with ν_3 ≠ 0 would falsify D20 (and the cited K-theory theorem).
  - A bounded-range bijection whose flux depends on the cut would falsify D1.

## 6. Open edges and next steps

1. Does any nontrivial strictly local covariant spin-½ walk exist? By D18 it would have zero speed at every TRIM. Next: the higher-order analysis at Γ, or a Gröbner computation at range 2 with the line conditions imposed.
2. **Owner decision point.** S̃ breaks "at most one grid space per tick" only by exponentially small tails.
   - If ticks may have faint reach, a covariant handed index is available.
   - If not, one-excitation ticks carry no index of any kind under covariance (D12 + D20).
3. Exactly covariant, non-circuit 3D many-body QCAs on qubits (Haah-type classes, tied to chiral boundary theories): is there one? It could carry handedness without single-particle ν_3.
4. Finite record sets cannot induce net flow (D10, D30). Infinite polarized record structures might select a flow direction through a covariant state-dependent rule (ARGUED). Worth a toy.
5. Check the lock-and-move channel (D23) against "records are permanent" and against Q7 menus.
6. The quantum pinned-record case where only the record projector, not the whole site algebra, is fixed.
7. D28 (a graded product breaks soldered O to D₄ at each site) should be cross-checked against the repo's graded-product lane; not verified here.
8. Campaign 7's flag can be sharpened:
   - Flux-type indices are excluded by covariance itself (D12), and also by continuity.
   - The chirality index ν_3 survives covariance, but is excluded by continuity *and* by strict locality (D20). Only quasi-local discrete steps carry it.

## 7. Plain-language summary

If the possibilities on the grid drifted, the drift would have to be the same across every cut at every tick: it could not start or stop anywhere, could not be switched on gradually, and could not be built from local moves taken in turns. Any such drift points one way, and turning the grid around reverses it, so the grid's turning symmetry rules out a standing drift. What remains is give-and-take: whenever something crosses a line one way, something else crosses it the other way in the same tick, either as a swap along a line or as a small loop around a square in space. One site's possibilities cannot be split so that one part goes one way and the opposite part goes the other; that needs at least two separate movers per site. Even then, if each mover carries only one site's worth of content to set its direction, a rule with strictly limited reach that treats all directions alike cannot make it travel steadily over long distances, nor tip the overall balance between left-handed and right-handed movers; that tipping becomes possible only if each tick has a faint reach beyond its near neighbours.