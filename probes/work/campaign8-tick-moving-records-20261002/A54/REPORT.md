# A54 report: is the sign χ local?

## 1. Verdict
- **χ is not local.** No bounded-range CZ/S/Z circuit maps light's bare ring onto A52's dressed ring, even on the charge-free sector. This holds with Gauss-law corrections allowed, for any record background and any range. This part is EXACT. For circuits of any kind it is ARGUED. The obstruction is the charges' exchange sign: a local χ would give bare rings local fermionic hops dressed only by charge parities, and those cannot exist in two or more dimensions. In 1D they do (a local Jordan–Wigner string), and quasi-1D tori do admit a local χ.
- **What χ needs instead is a global ordering of the corners**, a Jordan–Wigner string (EXACT construction, CHECKED). An equivalent alternative is a membrane potential σ whose boundary is the field lines. Given either one, χ can be written down explicitly. It turns A52's fermionic hops into Jordan–Wigner hops on bare rings; those stay fermionic but carry strings as long as the torus.
- **So the price is real.** For light alone the dressing is a relabeling of the charge-free operators that keeps local operators local, but it is not a circuit, so light in empty space behaves identically either way. Once charges are in the law, no local relabeling removes the dressing. For Q3, the sign of K decides the flux (EXACT, Z₂ form); K < 0 gives π flux and Dirac charges.

## 2. Question
Is the diagonal sign χ with R̃_p = χR_pχ (charge-free sector) a local relabeling? The answer decides whether "light's loop rule must be dressed" is a real price of fermionic charges under exact turns (owner reading Q3). The record background is treated as a supplied option; owner decision 29 is open.

## 3. Answers

### Q1. Is χ local?
**Theorem L (EXACT; derivation in NOTES §1).**
- Z₂ setup: hops t_l = X_l Z^{d_l}, where d is the link-to-link matrix of field factors.
- A52's tournaments give d + dᵀ = DᵀD, with D the boundary map from links to corners (CHECKED: 0 violations on every torus).
- A quadratic χ acts as χX^xχ = ±X^x Z^{Bx}, with B symmetric. The demand is (B + d)∂p ∈ im Dᵀ (products of Gauss operators) for every plaquette p.
- On Z³ with finite-range B, cohomology steps (H₁ = H₂ = H¹_c = H²_c = 0) turn this demand into local hops X_l G_{c_l}, dressed only by charge parities, that anticommute exactly when they share one corner.
- **Lemma G:** such hops do not exist in d ≥ 2. Path independence, plus detours around balls, forces s(u,w) = α_u + α_w for far corners. Pairing the paths u→w and u→v then gives 0 = 1.
- Scope: ±1- and ±i-valued χ, any range, any records (only d + dᵀ = DᵀD is used), Gauss corrections, and A45's y-gauge variants. The translation-invariant version requires A + Ā = 1 over Laurent polynomials, which is impossible.
- **Byproduct (a repair to A52's Lemma R):** its last step ("own link plus Gauss parities means boson") needs Lemma G. A single far Gauss factor can flip one junction: t₁ = X_{l1}G_{x2} gives θ(1,2,3) = −1. Lemma G shows a local family cannot make every junction −1.

**GF(2) scans (CHECKED).** The weakest local system is ⟨∂q, (B+d)∂p⟩ = 0.

| Torus | Smallest solvable range² (fine units) |
|---|---|
| 2³ | 2 |
| 3³ | 8 |
| 4³, 4×4×6, 4×4×8 | 14 |
| 3×3×5, 4×4×5 | 20 |
| 5³ | none up to 26 |
| 6³ | none at 8, 14 or 16 |
| 2×2×L, L = 3…8 | 2–4 for every L (the 1D escape) |

- **Translation-invariant B on 4³:** no solution at any range, up to the full torus.
- **Random records:** same thresholds and ranks. A52's Lemma V absorbs any background once range² ≥ 4.
- **Z₄ χ (S gates):** no help.
- **Record-free core** (charge-parity-dressed fermions), smallest admitted range² in doubled units:
  - 1D: 1 for every L;
  - 2D, L = 3…8: 9, 13, 25, 37, 49, 65, which is about half the torus;
  - 3D, L = 3, 4, 5: 13, 29, 41.
- **Controls:**
  - Translation-invariant bosonic hops (local CZ-conjugated) are detected exactly at range² 4 and not at 2.
  - Fermionic hops with an extra local CZ give the fermionic pattern unchanged.

**The non-local χ (EXACT construction, CHECKED).**
- Construction: order the corners and set K[u,w] = [pos u < pos w]; let Λ be the sublattice parity. Then M = Dᵀ(Kᵀ+Λ)D and B = M + d, which is symmetric with zero diagonal and satisfies B∂p = d∂p. The linear part comes from the phases of S_p.
- Result: χX^{∂p}χ = S_p as exact Pauli strings in every sector. Mismatches are 0 on 2³, 2×2×4, 4³ (uniform and random records) and 6³.
- Uniqueness: χ is unique up to sign on each homology sector, so the non-locality belongs to the function itself, not to this construction.
- Match with A52: it equals A52's breadth-first-search χ up to one global sign on every torus tried.
- Reach grows with the torus: CZ on 108 / 2,400 / 14,694 pairs, farthest pair at range² 12 / 36 / 76 (2³ / 4³ / 6³).
- Membrane form: Γ = D₂ᵀ d D₂ is local and alternating, so χ = (−1)^{σᵀUσ+λσ} for any σ with ∂σ = n. χ is local in σ but not in n.

**General circuits (ARGUED; COMPARATOR).** A finite-depth χ of any kind would carry the ground state of the Z₂ gauge theory with bosonic charges to the one with fermionic charges. These are distinct 3+1D topological orders (Levin–Wen; Lan–Kong–Wen). The U(1) analog is E_bM_b versus E_fM_b (Wang–Senthil).

**Spin-½ U(1) version.**
- The same χ works (EXACT): on ice states the dressed flip has exactly the Z₂ matrix element. CHECKED: 0 failing edges on the ice graph; complete on 2³ (864 states), capped on 2×2×4, 4³ and 6³.
- Locality on ice states, where the constraints are weaker (CHECKED, sampled): random walks on 4³ find no local Q at range² 4, 8 or 12; the sample is solvable from 16, the same threshold as Z₂.
- Controls: bosonic-conjugated signs are solvable from 4; 2×2×8 is solvable at 2.

### Q2. Consistency check (EXACT identity; CHECKED)
- χt_lχ = ±X_l ∏_{v∈J(l)} G_v, where J(l) is the order interval between the two ends of l. This is the Jordan–Wigner hop.
- Statistics are unchanged:
  - 0 violations of the pair rule (anticommute exactly when one corner is shared);
  - the commutation matrix is identical to that of A52's hops;
  - θ = −1 at every junction;
  - 0 anticommutations with bare rings. By contrast, A52's own hops anticommute with bare rings, which is their control.
- String lengths in corners:

| Torus | Mean | Max |
|---|---|---|
| 2³ | 2.3 | 5 |
| 4³ | 10.5 | 49 |
| 6³ | 23.9 | 181 |

- So bare rings plus fermionic charges require non-local strings, consistent with Q1.

### Q3. Flux sector (EXACT in the Z₂ form)
- **Flux is conserved.** S_p commutes with every hop, every Gauss parity and every other S_q.
- **One cube** (charge-free sector, dimension 32):
  - K = +1 gives a unique ground state with all S_p = +1;
  - K = −1 gives a unique ground state with all S_p = −1;
  - the gap is 4|K|, for both uniform and random records.
- **Tori:** both uniform sectors are consistent with every relation on 2³, 2×2×3, 4³ and 3×4×4. On 3³ the π-flux sector violates 9 relations, so it is frustrated on planes with an odd number of plaquettes.
- **Light alone is indifferent to the sign of K:** a diagonal Z^η flips every S_p and multiplies hop l by (−1)^{η_l}, so the charges can tell K from −K.
- **Conclusion:** with A52's identification (S_p = +1 is zero flux, S_p = −1 is π flux), the sign of K decides:
  - K > 0 gives a Schrödinger band;
  - K < 0 gives Kawamoto–Smit Dirac charges, doubled.
- For spin-½ light the same conclusion holds at mean field (ARGUED).

### Q4. Helper places (EXACT core; ARGUED conclusion)
- Setup: hops X_l G_{c_l} ⊗ h_l with finite-range helper Pauli operators, and a bare ring.
- **Trivial helper loops:** if the helper loop products H_p are trivial, the same far-pair argument applies, because the helper commutation form is alternating. Then there are no fermions (EXACT).
- **Non-trivial helper loops:** each H_p is a conserved loop operator that the charges feel. Unless a helper loop rule fixes it, empty space has an extensive flux degeneracy.
- So helpers keep light's ring bare only by moving a dressed loop rule onto the helpers.
- **σ on face qubits:** placing σ there with the local constraint n = ∂σ makes χ a local CZ circuit. But each charge then ends a string of violated constraints, which confines it unless the string carries no tension (ARGUED).

## 4. Methods
- Symbolic Pauli strings with exact phases (A52 library).
- Incremental GF(2) elimination with spatially ordered unknowns.
- Translation-orbit reduction.
- Relation bookkeeping for the commuting operators S_p and G_v.
- Exact diagonalization in the 32-dimensional sector.
- Breadth-first search and random walks on the ice graph.
- A cohomological derivation (Theorem L, Lemma G).

## 5. Checks
Every job ran through `run_small.sh` with an alarm of at most 118 s. Load was 3.0–4.7 and free memory 33–38%.

| Script | Wall | Peak (MiB) | Key numbers |
|---|---|---|---|
| c1_local_scan (2³–6³, 2×2×L, 3×3×L, 4×4×L; Z₄; controls) | 0.1–8.5 s | 33–148 | thresholds above |
| c1b_ti_scan 4 (fermion / boson) | 0.2 / 0.1 s | 34 | none at any range / exactly 4 |
| c2_gauss_core in 1D / 2D / 3D | 0.1 / 0.6 / 4.6 s | 28 / 34 / 185 | 1D local; 2D and 3D grow with L |
| c3_jw_chi (2³, 2×2×4, 4³ ×2, 6³) | 0.2–5.0 s | 34–37 | 0 mismatches; 0 failing ice edges |
| c4_ice_local (2³; 4³; boson control; 2×2×8) | 0.6–62 s | 34–42 | 4³: none below 16 |
| c5_flux | 0.13 s | 35 | sign(K) decides; 3³ frustrated |

**Two incidents:**
- One c4 run (40 walkers × 4000 steps) was stopped by the alarm after range² 4 and 8, both unsolvable; I reduced it to 10 walkers × 3000 steps.
- The first c5 version peaked at 302.7 MB (the guide is 300 MB) because it built full 4096² arrays. The rebuilt sector-only version gives identical numbers at 35 MiB.

A first, shallow ice sample (6,000 states near the starting state) wrongly looked solvable at range² 4; the random walks replaced it.

## 6. Open edges
1. An EXACT version for non-Clifford diagonal χ (for example CCZ) and for general circuits; this needs a nonlinear form of Lemma G.
2. An EXACT proof for the spin-½ ice manifold, which allows extra on-loop factors.
3. Whether the relabeling of the charge-free operators is a nontrivial QCA in the formal sense (COMPARATOR: Haah–Fidkowski–Hastings).
4. The flux choice at finite charge density, where K competes with the charges' kinetic energy (Lieb-type).
5. An explicit face-helper model with its own loop rule, and whether its strings confine.
6. On odd tori, the ±1 construction needs S gates or a per-sector treatment.

## 7. Plain-language summary
A52 found that making light's charges behave like electrons forces light's loop rule to carry extra sign factors. It also found a sign change that seemed to undo them. I asked whether that sign change is local. It is not. Undoing the factors needs a single thread running through every corner of the grid, so it reaches across the whole space. If it were local, the charges would turn back into ordinary particles, which is impossible in three dimensions; in one dimension it does work. In empty space, light behaves identically either way. With charges present, the extra factors are a real cost. The sign of light's loop coupling decides whether the charges see no flux or the flux that makes them Dirac particles.

Everything is in `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A54/`:
- NOTES.md
- a54lib.py
- c1_local_scan.py
- c1b_ti_scan.py
- c2_gauss_core.py
- c3_jw_chi.py
- c4_ice_local.py
- c5_flux.py
- out_*.txt and time_*.txt for each run