I found no allowed rule whose calmest state is a U(1) background with the walk's crossings. Ring terms alone never make the soldered background (equivalently the π-flux singlet) lowest. Adding a star-local face-diagonal term opens only a noise-level variational window, and on the 16-site cluster the exact ground state there sits about 0.25 per bond lower. The deformations that would give the hidden field a chance to act like light bring no energy gain.

This message is the full report. I did not write `SP/c8/A46/REPORT.md`, because my harness forbids subagent report files.

**Housekeeping**
- No git writes, no repo edits, no PRs.
- Scripts are in `SP/c8/A46/` and import `SP/c8/A44/a44lib.py`. Every run went through `run.sh` with the same gates as A44:
  - 1-minute load below 6 and free memory at least 25%; loads were 1.6–3.7 and free memory 32–40%;
  - the shared `NUMLOCK`; I waited about 25 s once while another lane held it; it was released after each run and is now free;
  - `nice -n 10`, the four BLAS caps at 1, and a Python alarm of at most 285 s.
- The longest run took 242 s and peak memory was 548 MB.
- Everything is in the Klein-dual (π-flux) frame of A44 unless stated; the coordinator's `verify_A44.py` passes for that map.

**Grades.** EXACT (proof or exact arithmetic), CHECKED (finite computation with stated tolerance or error bars), ARGUED (reasoning without proof), COMPARATOR (literature recalled from memory, not adopted). Every rule here is supplied, not adopted.

## 1. Question

1. Do covariant ring terms on the square faces make the projected π-flux singlet (the soldered background) beat the ordered competitors? Where in (J, K, ring strength), and how robustly?
2. Which covariant deformations break the mean-field gauge group SU(2) to U(1), and what do they cost or gain?
3. Is there a next-door or star-local covariant rule, one qubit per place, whose calmest state is a U(1) background with the walk's crossings as its half-pieces?

## 2. Answer, graded

**Q1. Ring exchange.**
- **The ring operator (EXACT; CHECKED to 0.0).**
  - On a face 1-2-3-4: P + P⁻¹ = ¼[(12)(34) + (14)(23) − (13)(24)] + ¼ Σ_{i<j}(ij) + ¼, with (ij) = σ_i·σ_j.
  - Its spectrum is −2 (×4), 0 (×6), +2 (×6). The ferromagnet takes the maximum +2. Néel gives 0 classically. The classical minimum is −½ (four spins at 90° steps in a plane).
  - The 4-site Heisenberg ground state has P = +1, not −1.
- **The soldered-covariant form (EXACT).** Replace each dot product by its Klein twist:
  - an edge along a becomes 2σ^aσ^a − σ·σ;
  - a face diagonal becomes 2σ^cσ^c − σ·σ, with c the face normal.

  Same coefficient R.
- **Reduction (EXACT).** For the symmetric states compared here (the π-flux singlet, the Néel-field family, the ferromagnet, the plaquette state), e_K′ = e_J′/3. So their energy per bond is J′_eff·e_J′ + R·ring, with J′_eff = J′ + K′/3, which equals (K − J)/3 in the original frame. The (J, K, R) map therefore collapses to ρ = R/J′_eff. The collinear family needs K′ = 0, which is the only place I used it.
- **Sign (CHECKED).** ⟨P + P⁻¹⟩ per face:

| State | 16-site exact | L = 4 | L = 6 | L = 8 |
|---|---|---|---|---|
| π-flux singlet (soldered background) | +0.2805 | +0.330(2) | +0.313(1) | +0.310(1) |
| 0-flux Fermi-sea singlet | −0.147 | — | — | — |
| ferromagnet | +2 | +2 | +2 | +2 |

  - So the π-flux singlet is favoured only by R < 0 in H = R(P + P⁻¹), and R < 0 favours the ferromagnet most of all.
  - Electron hopping generates R > 0 (COMPARATOR: Takahashi; MacDonald–Girvin–Yoshioka, 80t⁴/U³). That sign favours the 0-flux state instead (COMPARATOR: Motrunich, triangular lattice).
  - So "ring exchange favours π-flux states" holds only for R < 0 in this convention.
- **Map with ring only (CHECKED, variational).**
  - Competitors: the π-flux singlet against the projected Néel-field family, the ferromagnet (exact at K′ = 0), Néel product and spin-wave energies, and the plaquette product.
  - On the ring side the soldered background is never lowest at L = 4, 6 or 8. An ordered family member wins for ρ > −1.22 and the ferromagnet for ρ < −1.22. For R ≥ 0 it loses more: its ring energy rises, while Néel's spin-wave energy does not change with R at harmonic order (EXACT).
  - At the closest point, ρ ≈ −1.22, it sits 0.025, 0.060 and 0.072 per bond above at L = 4, 6 and 8. The gap grows with size, so this is robust.
  - 16-site exact:
    - the window closes once m = 0.1 is included (to within 0.0007);
    - the π-flux overlap with the exact ground state rises from 0.72 (R = 0) to 0.80 (R = −0.5), then falls to 0.71 (R = −1.3);
    - the exact ground state stays 0.21–0.32 per bond lower.
- **Ring plus the star-local face-diagonal term (CHECKED, but at the noise level).**
  - The added term is the Klein dual of J₂, which is j Σ_fd (2σ^cσ^c − σ·σ) in the original frame.
  - Dual-frame face-diagonal correlation at L = 8: π-flux +0.393; Néel family m = 0.05/0.1/0.2: +0.44/+0.51/+0.63.
  - At K′ = 0, i.e. original (J, K) = (−1, 2) plus j and R:
    - at L = 6 the π-flux singlet is lowest for j ∈ [0.2, 0.45], R ∈ [−1.4, −0.05], with margins up to 0.007;
    - at L = 8 (Néel side; collinear family from L = 6, so a mixed-size comparison) the window shrinks to j ∈ [0.25, 0.43], R ∈ [−1.4, −0.55], with margins at most 0.0023 per bond. That is within the statistical errors of ±0.002–0.004.
  - The runners-up are the weakly ordered members (Néel m = 0.05, collinear m = 0.1). So the variational optimum sits at zero or near-zero order, and clearly ordered states lose.
  - 16-site exact at window points: the π-flux is the best tested state, but the exact ground state is 0.25–0.27 per bond lower and the overlap is 0.50–0.74.

**Q2. SU(2) → U(1).**
- **Which deformations (EXACT; CHECKED with `igg2.py`).**
  - All nearest-neighbour covariant hops keep η-SU(2) (shown in A44).
  - The covariant same-sublattice hops break it to the charge U(1) (defect 2.00 for all six cases): face-diagonal t₂ + iλ₂σ·d̂, and axis-pair (x, x+2e_a) t₃ + iλ₃σ^a.
  - Nearest-neighbour covariant triplet pairing (d along the bond; the Klein dual of singlet pairing) should give U(1) if collinear in gauge space, and Z₂ with non-collinear combinations (ARGUED; COMPARATOR: Wen's projective symmetry groups). I did not compute its energy; the Pfaffian route was not cheap within the time box.
- **Whether the walk's crossings survive (EXACT, k-space).**
  - λ₂ and λ₃ vanish at all eight nodes, since sin(k·d) = 0 there.
  - t₃ shifts all nodes equally (by 6t₃), which the filling level absorbs.
  - t₂ splits them: Γ and R move up by 12t₂, X and M down by 4t₂, giving small pockets.
  - So λ₂, λ₃ and t₃ break SU(2) to U(1) while keeping the crossings. Γ and R stay round; X and M may split speeds (A43).
- **Energy (CHECKED, L = 6; EXACT symmetry).**
  - The energy is even in t₂ and λ₂: the η-rotation flips their sign and leaves the projected state unchanged.
  - Under the window rule (j = 0.35, R = −1.0), relative to the undeformed state:

| Deformation | Energy change per bond |
|---|---|
| t₂ = 0.15 | +0.002 ± 0.005 |
| λ₂ = 0.15 | +0.002 ± 0.005 |
| λ₂ = 0.3 | +0.014 ± 0.005 |

  - So U(1) gains nothing and costs at larger amplitude.
  - At L = 4 and on the 16-site cluster, t₂ leaves the occupied space unchanged (a finite-size degeneracy).

**Q3. Verdict.**
- No evidence for such a rule:
  - next-door rules alone: no (A44);
  - adding face ring terms: no, robustly;
  - adding the star-local face-diagonal term plus ring: a variational candidate region where the SU(2) background ties the weakly ordered states within noise. That is not evidence of a calmest state: the 16-site exact ground state is about 0.25 per bond lower, the ring term is face-local rather than star-local, and nothing energetically selects U(1).
- A real case would need:
  - a stronger competitor set (other flux and Z₂ liquids, valence-bond orders, spirals), larger L and improved wavefunctions;
  - a term that rewards same-sublattice spinon hopping, so that U(1) is selected.
- COMPARATOR: the known 3D U(1) phases with emergent photons have gapped bosonic charges, not Weyl spinons. Examples are pyrochlore quantum ice (Hermele–Fisher–Balents) and bosonic ring models on cubic lattices (Motrunich–Senthil).

## 3. Methods

- **Mean field.** The soldered-frame hop matrix (with deformations) is rotated by V = ⊕V_x into the dual frame. The Néel field is m(−1)^{|x|}σᶻ; the collinear field is m(−1)^{x1+x2}σᶻ.
- **VMC.** Single flips plus bond pair flips (exchange only for S^z-conserving states), with O(N²) estimators. The ring estimator is ψ(Pc)/ψ(c) + ψ(P⁻¹c)/ψ(c), computed as a determinant over the changed sites.
- **Exact cluster.** The ring term is built as sparse permutation matrices on the 16-site cubic cluster; Lanczos with tol 1e-8.
- **Harmonic-order statement (EXACT).** Around Néel the ring energy starts at fourth order, because each overlap ⟨m|−m⟩ is O(δ).

## 4. Checks (all in `SP/c8/A46/`; outputs `out_*`/`log_*`, timing `time_*`)

| Run | Runtime | Result |
|---|---|---|
| `ring_check.py` | 3 s | Identity exact, after a coefficient fix (first run used ⅛ in place of ¼; superseded) |
| `vmc_ring.py` on the 16-site cluster | 3 s | VMC agrees with exact within 1σ (ring 0.284(7) vs 0.2805; m = 0.3: 0.239 vs 0.242; m = 1: 0.108 vs 0.105) |
| `vmc_def.py` on the 16-site cluster | 3 s | λ₂ = 0.2 and 0.4 agree with `ed16_def.py` within 1σ |
| `vmc_ring.py` at L = 4 / 6 / 8 | 28 / 93 / 241 s | Ring-only family; first and second halves agree; inverse drift at most 5e-11 |
| `vmc_j2r.py` at L = 6 (Néel, collinear) and L = 8 (Néel) | 111 / 93 / 242 s | Face-diagonal correlations; same convergence checks |
| `vmc_def.py` at L = 4 / 6 | 26 / 86 s | Deformation energies |
| `ed16_ring.py` (two runs), `ed16_j2r.py`, `ed16_def.py` | 2–9 s, ≤ 548 MB | Exact cluster numbers |
| `map_ring.py`, `map_j2r.py`, `igg2.py` | ≤ 0.1 s | Maps and gauge check |

**Flagged.**
- `map_ring`'s 16-site line used coarse VMC m values and showed a spurious window; exact m = 0.1 closes it.
- Two output files were overwritten by later runs with the same runner tag. The full outputs are kept in `log_j6.txt` and `log_d6.txt`.
- The staggered-moment diagnostic is meaningless for the collinear family.

## 5. Open edges

1. Collinear family and other orders at L = 8. The L = 8 window is within noise.
2. Z₂ and pairing states via Pfaffians, other flux patterns, valence-bond and plaquette orders.
3. Lanczos-step or backflow-improved energies to close the 0.25-per-bond gap to the exact 16-site ground state.
4. Whether any star-local term rewards same-sublattice spinon hopping enough to select U(1).
5. K′ ≠ 0 for the collinear family.

## 6. Plain-language summary

Adding the four-spin "ring" terms the grid allows does not make the entangled two-part background the calmest state. The sign of ring term that helps it helps a fully aligned state even more, and before that takes over, ordered magnet-like states still win. When a star-local next-nearest term is added as well, the background ties the best ordered states within our measurement noise in a small range of rules, but an exact small-system calculation shows something else lies well below all of them. Its hidden field is, at this level, the non-abelian kind; turning it into a light-like U(1) one needs extra hopping terms that cost a little energy rather than saving any. So I found no rule that clearly makes this background, with its light-like hidden field and the walk's crossings for its half-pieces, the calmest state.