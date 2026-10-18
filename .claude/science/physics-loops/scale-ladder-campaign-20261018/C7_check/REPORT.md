# C7 check: emergent corner fermions (Γ-matrix model)

Provenance: a fresh-context checker of the same model family, so not an independent model family. All code is new: its own corner-graph geometry, oriented faces and Bloch builder (`k7_geom.py`), its own GF(2) solver, a different Cl(7) basis (YXX, XYZ, YYI, IZI, ZYZ, YXY, IXZ), its own bond labelling, a period-1 corner-sign-gauge symmetry solve in place of C7's L = 4 sign propagation, and the corner + λ Hamiltonian rebuilt from the repo runner definitions. The checker's file write was blocked; the supervisor saved this report from the hand-back.

**Result: all five claims hold. 35 PASS, 1 FAIL.** The FAIL is against one sentence in C7's claim 3, not a numerical failure.

| Runner | Result |
|---|---|
| `k7_A_gamma.py` | 13/0 |
| `k7_B_energetics.py` | 11/0 |
| `k7_C_psg_gap.py` | 6/1 |
| `k7_C2_isospectral.py` | probe |
| `k7_D_corner_flux.py` | 5/0 (a first 4/1 run was a mod-2π rounding bug in the checker's own comparison) |

## 1. Exact solvability: confirmed

- Jordan–Wigner check of the dictionary for all 36 label pairs.
- L = 2 (288 qubits): all 232 W_C commute with each other and with every bond term of H_M, H_M2 and H_R; the 1440 anticommuting edge pairs are exactly those sharing a corner.
- Closed surfaces (beyond C7): the face–edge incidence has a 42-dimensional left kernel; every relation gives ∏W = +1·I, matching W_C = (−1)^(n+1) ∏u.
- Cluster ED (triangle, square, tube, plaquette): qubit spectra equal free-Majorana levels in every sector.

## 2. Half-filling energetics: confirmed

| t2 | E(1c+11) | Runner-up | Margin |
|---|---|---|---|
| 0.2 | −11.417292 | 1c01 | 0.000837 |
| 0.5 | −11.957009 | 1c01 | 0.028757 |
| 1 | −13.818077 | 1c01 | 0.317584 |
| 2 | −19.999590 | 0c11 | 0.121948 |

- Margin identical on N_K = 6, 8, 12, 16, a half-shifted 9³ grid and a second gauge. Not a grid artefact.
- But physically fragile: O(t2⁴), since 1c11 and 1c01 differ only by the plaquette flux.
- 512 consistent uniform ±π/2 triangle assignments and 150 greedy period-1 descents per t2: nothing below 1c+11.

## 3. No O-fixed momentum, gapped: confirmed, one sentence overstated

- Exact sign-gauge solve for the 24 proper rotations: 1c+11 has C4⁴ = −1, commuting translations, no O-fixed momentum. Control 1011 has exactly two fixed momenta (k and k + (π,π,π)).
- Only 0c+01 and 1c+10 among chiral patterns with a period-1 gauge have fixed momenta, as C7 says.
- Gap: minimum one-body Δ = 0.988 near t2 = 0.8, on the 6-fold {0,π}³ star; the fermion excitation gap is 2Δ.
- **FAIL:** the spectral test E(Rk + πs_R) = E(k) cannot discriminate shift assignments. E(k + π(1,1,1)) = E(k) holds exactly (t2 → −t2 isospectrality; `k7_C2` finds no k-independent unitary or antiunitary implementing it). The alternative assignment s′_R = s_R + χ(R)(1,1,1) passes to 5e−15 and would give a nonempty fixed set. The empty-fixed-set claim rests on the exact symmetry solve only.
- Improper rotations are symmetries only combined with complex conjugation.

## 4. Corner-family fluxes: confirmed

λ term from `scripts/corner_fermion_projective_symmetry_group_class_and_site_shell_2026_10_17.py` and `scripts/corner_fermion_large_fermion_effective_theory_and_one_qubit_block_embedding_2026_10_17.py`. Wilson loops on all 232 faces after a random U(1) gauge, 6 values of λ, t2 ∈ {0.2, −0.3, 1}, θ = arctan λ: outward square π − 4θ, outward triangle π + 3θ, plaquette π, tube π − 2θ (on-site edges against the triangle orientation). Square = π forces λ = 0, so no member is gauge-equivalent to 1c+11. Pure-chiral limit: 1c±10.

The C6 §5.4 item is a completion, not a refutation: C6 gives the triangle shift correctly and omits the square and tube shifts.

## 5. Framing

Correct as a comparison of searched static sectors (no Lieb-type theorem). Say "lowest among the searched static sectors"; read "chiral" as spontaneous T- and mirror-breaking flux order with no implied protected boundary modes; do not cite the spectral test as independent confirmation.

## Corrections applied to `../C7_emergent_corner_fermions/FINDINGS.md`

1. Spectral test demoted. 2. C6 §5.4 recast as a completion, with orientation stated and the 1c±10 remark. 3. Δ is one-body; excitation gap 2Δ. 4. Wider searches added. 5. Fragility and framing tightened.
