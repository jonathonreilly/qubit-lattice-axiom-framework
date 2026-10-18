# C7 findings: corner fermions as emergent partons of a Kitaev-type Γ-matrix model

Provenance: a worker of the same model family. Checked by a fresh-context same-family agent (`../C7_check/REPORT.md`, 35 PASS, 1 FAIL against one overstated sentence); corrections from that check are applied below.

| Runner | Result |
|---|---|
| `c7_A_gamma_model_exact_solvability.py` | 18/0 (~10 min) |
| `c7_B_majorana_flux_energetics.py` | 5/0 |
| `c7_B2_extra_sector_search.py` | 1/0 |
| `c7_C_selected_sector_spectrum_psg.py` | 10/0 |

Shared code is in `c7_common.py`.

**Answer.** A translation-invariant Γ-matrix model on the fine cubic lattice exists and is exactly solvable. Its partons hop on the corner graph in a static Z2 field. At its natural filling (Majorana half filling), the lowest of the searched static sectors has π on every 4-cycle, with chiral (±π/2) triangles. That sector is not the corner model: it is a gapped Z2 spin liquid with spontaneous T- and mirror-breaking flux order, no O-fixed momentum and no nodes. "Chiral" here means the ±π/2 triangle fluxes; no protected boundary modes are implied (3D class D has no strong invariant; weak invariants were not computed). At the corner model's filling ν = 1, the family picks other sectors, as in C6.

## 1. Construction (a supplied model; the standard Kitaev / Γ recipe)

- **Site.** 3 qubits per corner, 36 qubits per site. Cl(7) Γ matrices (8×8). The corner graph is 6-regular, so 8 dimensions is the minimum for one Γ per bond end.
- **Bond labels** depend only on the corner type and the relative edge, so the model is translation invariant.
- **Dictionary.** G^a = i b^a c, G⁷ = i d c, and u_e = i b^α b^β.
- **Three Hamiltonians:**
  - H_M, Majorana hopping with spectator d;
  - H_M2, a complex parton with imaginary hopping;
  - H_R, real parton hopping (C6's problem).

  A chemical potential and λ terms keep the model solvable.
- **Exact checks:**
  - A0: the dictionary in an explicit Jordan–Wigner representation.
  - A1: on L = 2, 288 qubits, all 232 W_C commute with each other and with every bond term; the cuboctahedron product is +1.
  - A2: on five clusters, the qubit spectra equal the free-fermion spectra in every sector.

## 2. Flux selection at Majorana half filling (numerical)

- **Allowed fluxes.** Odd triangles must carry ±π/2, so the corner pattern (π everywhere) is not available. There are 16 distinct uniform patterns.
- **Uniform winner:** 1c+11 (square = plaquette = tube = π, chiral triangles) at every tested t2. The order is stable at N_K = 6, 8, 10 (check: also 12, 16, a half-shifted 9³ grid and a second gauge; the t2 = 0.2 margin is unchanged).
- **Fragility.** The t2 = 0.2 margin is O(t2⁴): 1c11 and 1c01 differ only by the 4-link plaquette flux. A small extra term (for example the untried Γ⁷ further-neighbour terms) could reorder the top two. Neither is the corner model.
- **Wider searches (check).** All 512 consistent translation-invariant ±π/2 triangle assignments with uniform 4-cycle bits, and 150 greedy period-1 descents per t2, found nothing below 1c+11.

  | t2 | E per site | Runner-up | Margin |
  |---|---|---|---|
  | 0.2 | −11.417 | 1c+01 | 0.0008 |
  | 0.5 | — | — | 0.029 |
  | 1 | — | — | 0.318 |
  | 2 | — | 0c+11 | 0.122 |

- **Stability.**
  - All 288 period-2 single flips raise the energy.
  - L = 4 flips cost 0.012–0.38.
  - Greedy, random and kick searches never went below 1c+11.
- **H_R (real hopping).** This reproduces C6: at ν = 1 the corner pattern ranks 15th–16th, and at μ = 0 it ranks 4th.
- **H_M2 at ν = 1.** 1c+11 ranks 13th–14th.

## 3. The selected sector compared with the corner model

- **Gauge.** It has a period-1 gauge: 12 bands with exact fine translations. All bands are 2-fold.
- **Gap.** Fully gapped, with one-body gap Δ = 1.0–3.1 over t2 = 0.05–3 and no nodes (check: minimum 0.988 near t2 = 0.8). The fermion excitation gap of H_M is 2Δ. The gap minimum is a 6-fold star at {0, π}³ points.
- **PSG (exact, GF(2), L = 4).** C4⁴ = −1 and the translations commute, but no momentum is O-fixed. The check confirmed this by an independent exact sign-gauge solve for all 24 rotations. The spectral test E(Rk + πs_R) = E(k) (7e−15) is not independent evidence: E(k + π(1,1,1)) = E(k) holds exactly (the t2 → −t2 isospectrality, not a symmetry), so the alternative shift assignment s_R + χ(R)(1,1,1) passes it too and would give a nonempty fixed set. The control 1011 has the fixed pair. Among chiral patterns only 0c+01 and 1c+10 have O-fixed momenta; 1c+10 ranks 4th and 8th.
- **No member of the corner family is gauge-equivalent (exact).** For t1 = −1 and chiral λ, the fluxes are:
  - outward square π − 4 arctan λ;
  - tube π − 2 arctan λ (orientation with its two on-site edges against the triangle orientation);
  - outward triangle π + 3 arctan λ;
  - plaquette π.

  Reversing a face flips the sign of the shift. Each on-site amplitude is u(1 + iλσ), contributing ±arctan λ per on-site edge. Square = π forces λ = 0, and then the triangle is π, not ±π/2. In the pure-chiral limit (|λ| → ∞) the pattern is 1c±10, which has O-fixed momenta but is still not 1c+11.

  **Completion of the C6 note §5.4 (an omission, not an error):** it gave the triangle shift correctly but not the square and tube shifts. Labels such as "1011" are u-convention labels, not gauge-invariant fluxes, once λ ≠ 0.
- **T breaking.** The two chiralities are degenerate, so T is broken spontaneously (Yao–Kivelson).

## What would have to change

- 1c+10 (tube = 0) winning at half filling. Γ⁷ further-neighbour terms are untried.
- At the corner model's own filling, the energetics is negative (C6).
- Triangles cannot be π for Majorana hopping.

## Status

- **Exact:**
  - the Γ algebra and dictionary;
  - flux commutation and the closed-surface relation;
  - the cluster spectra;
  - the PSG on L = 4 (and the check's period-1 sign-gauge solve);
  - the corner-family flux formulas;
  - the conjugate degeneracy and the period-1 gauge.
- **Numerical:** all energetics, the gap scan and the location of the gap minimum.

## Caveats

- Not a ground-state proof: only static sectors were compared, uniform and period-2, with greedy searches. No Lieb theorem applies. The result matches the loop-length heuristic.
- Torus projection was not modelled.
- Only |t1| = 1 with scanned t2.
- The 36-qubit site is supplied local structure relative to rung 0.
- No literature search was run.

## Prior art

- Kitaev 2006; Yao–Kivelson 2007.
- Wu–Arovas–Hung 2009; Yao–Zhang–Kivelson 2009; Ryu 2009; Mandal–Surendran 2009; Yao–Lee 2011.
- O'Brien–Hermanns–Trebst 2016; Chulliparambil et al. 2020.
- Lieb 1994; Macris–Nachtergaele; Pedrocchi–Chesi–Loss 2011.
