# Lane RC, probe C2: strong-coupling candidates for an exactly conserved energy current

**Who and when.** Claude Opus 5.5 at xhigh (same family as the supervisor). Ran 2026-10-11, 15:44Z to about 16:05Z. Nothing here has been refereed, and no repository file was edited.

**Where things are.** Scratch folder: `.../scratchpad/laneRC/C2/`.
- `pauli_ti.py`: exact Pauli-string algebra for translation-invariant operators on infinite 2D lattices.
- `c2_models.py`: the model densities.
- `c2_algebra.py` → `c2_algebra.out`: [H, J_E] and the improvement search.
- `c2_ed.py` → `c2_ed.out`: full ED Drude ratios.
- `c2_kitaev_majorana.py`, `c2_kitaev_dilute.py`, `c2_kitaev_window.py` → `.out`: Kitaev, all flux sectors.
- `c2_majorana_bipartite3d.py` → `.out`: 2D square and 3D cubic static-Z2 Majorana models, plus the current-formula cross-check.
- `c2_controls.py` → `c2_controls.out` and `c2_ed_xxzstack.out`: integrable controls.

**Labels.**
- **proved:** a complete argument within the stated class.
- **checked:** computed here.
- **suggested:** argued, not computed.
- **reading:** an interpretation.
- **comparator:** literature. V means verified in a fetched abstract or search summary; M means from memory, unverified.

---

## 0. Bottom line

**Worker reading for C2: FAIL (bounded to the candidates examined), with two items flagged for the referee (§6).**

No interacting candidate examined in d ≥ 2 has an exactly conserved total energy current. The candidates fall into three groups:
1. **Commuting-local-term models** (toric code, quantum doubles, string nets, X-cube and other stabilizer fracton codes, Xu–Moore at h = 0).
   - J_E ≡ 0 identically, and every energy density is separately conserved, so energy cannot move in any state (proved).
   - The only conserved current in the improvement class is 0.
   - The one-particle symbol is 0. It cannot equal E∇E with nonzero slope.
   - Category (i), useless for gravity.
2. **Kitaev-type models** (free Majoranas in a static Z2 gauge field on a bipartite lattice: honeycomb, and the 3D variants by the same lemma).
   - J_E is conserved exactly in the translation-invariant flux sector, with symbol exactly E∇E there.
   - **In every flux sector whose Majorana spectrum is non-degenerate, the conserved part of J_E is exactly zero** (proved: a chiral-symmetry lemma; checked to 1e-14).
   - At T = ∞ the all-sector Drude ratio is about 1e-30 for L = 8–24. At any finite flux density, which is the case at every T > 0, the low-frequency weight goes to zero, with a Drude-like peak of width ∝ flux density (checked, L ≤ 40).
   - Category (ii), sector-restricted. Inside a sector the model is also non-interacting.
3. **Generic interacting 2D models**: TFIM at h = 1 and 3, the XX model (hard-core bosons), the compass model, Xu–Moore at h = 1, toric code + field, Kitaev + [111] field.
   - [H, J_E] ≠ 0 exactly (operator algebra).
   - The patch improvement search leaves 66–100 % of the residual.
   - The ED Drude ratio at β = 0 falls with N.
   - For TFIM, XY/XYZ (which includes XX) and compass, published theorems exclude every nontrivial local conserved quantity. Combined with a parity step (§3), they exclude any conserved local improved current (comparator plus proved reduction).

**Supervisor expectation**: "the Kitaev honeycomb conserves the current only within flux sectors, and at T > 0 flux scattering spoils it. No candidate passes." **Confirmed.**
- It is sharpened: in non-degenerate sectors the conserved part is exactly zero, not merely degraded.

---

## 1. Two general facts (proved)

**Setup.**
- H = Σ_x h_x, and J = J_E^x = (i/2) Σ_{x,y} (r_y − r_x)[h_x, h_y], with each Pauli term of H taken as its own energy density, placed at its centroid.
- Redefining the density, h_x → h_x + div b_x (any local choice), changes the total current by i[H, B], with B = Σ_x b_x. Curl terms sum to zero on the torus.
- The searched space is therefore J' = J + i[H, B], with B a translation-invariant sum of local operators. This is the RN L3 referee's "up to divergence-free improvements", applied to the total.

**F1 (uniqueness and finite-size invariance).**
- In the Hilbert–Schmidt inner product, ker ad_H ⊥ range ad_H. So J + range(ad_H) contains at most one conserved element, and it is the time average J̄, the orthogonal projection of J onto the commutant of H.
- Hence:
  - (a) if a conserved local J' = J + i[H, B] exists, then J' = J̄ on every torus large enough to hold the supports;
  - (b) the T = ∞ Drude ratio r(N) := ‖J̄‖²/‖J‖² then equals ‖j'‖²/‖j‖², the ratio of the HS norms per cell of the two local densities. **This is independent of N.**
- **A decaying r(N) therefore excludes every conserved local improvement, J' = 0 included, whose support fits the clusters.** This tests all local B, not only a chosen span.
- The "ratio of ensemble sums" form used throughout is r = Σ_{E_n=E_m} p_n|J_nm|² / Σ_{n,m} p_n|J_nm|².
- Also: if [H, [H, B]] = 0 then (E_n − E_m)²B_nm = 0, so [H, B] = 0. So no improvement can turn a zero current into a conserved nonzero one.

**F2 (commuting local terms).** If [h_x, h_y] = 0 for all x and y:
- every h_x is conserved, so the energy profile ⟨h_x(t)⟩ is frozen in every state;
- J_E ≡ 0, and by F1 the only conserved current in the class is 0. The Drude weight is 0;
- the elementary excitations are immobile. The exactly solvable spectrum is flat in k, so E∇E = 0;
- this covers the toric code, Kitaev quantum doubles, Levin–Wen string nets, X-cube, Haah's code, and classical Ising in a parallel field.

Checked: the toric-code and Xu–Moore (h = 0) J_E densities come out identically empty (`c2_algebra.out`).

---

## 2. Kitaev-type models (honeycomb; 3D variants)

**Setup.**
- H = Σ J_a σ^a σ^a → (i/4) cᵀA_s c in flux sector s, with A_s real antisymmetric and bipartite.
- The term-wise current maps to the single-particle matrix **B_s = [A_s², X] = A_s² ∘ D**, where D_ij is the x-displacement.
  - proved: [A, XA + AX] = [A², X];
  - checked: it agrees with the explicit term-by-term construction to residual 0.
- J_E commutes with the bond terms' flux operators, so it is flux-diagonal.

**K1. Zero-flux (translation-invariant) sector: conserved exactly (proved, checked).**
- In k-space A_0²(k) = −|f(k)|² · 1, so B_0(k) = −i∂_k|f|² · 1 = 2E∂_kE · 1, which commutes with A_0(k).
- **The symbol is exactly E∇E.** Note that this is the symbol of a free (non-interacting) band.
- Checked: ‖[A, B]‖ = 0 and r = 1 for L = 4–40.

**K2. Chiral lemma (proved).**
- Let S = diag(±1) by sublattice. Then SAS = −A and SBS = B, because B is a product of two inter-sublattice matrices. Also B is real.
- For an eigenvector v of iA with eigenvalue λ ≠ 0, Sv and v* both have eigenvalue −λ. If that eigenvalue is non-degenerate, Sv ∝ v*.
- Then ⟨v|iB|v⟩ = ⟨Sv|iB|Sv⟩ = ⟨v*|iB|v*⟩ = −⟨v|iB|v⟩ = 0.
- So **J̄_s = 0 exactly in every sector with a non-degenerate spectrum**, at every Majorana temperature.
- Checked: max|⟨v|iB|v⟩| / ‖B‖ ≤ 3e-14 on honeycomb, square and cubic lattices with random signs (`c2_majorana_bipartite3d.out`).
- The lemma uses only bipartiteness and nearest-neighbour hopping, so it covers the 3D Kitaev variants (hyperhoneycomb, hyperoctagon) and the Γ-matrix models without a field. For those 3D lattices this is suggested; the check was done on cubic random-sign hopping.

**K3. All sectors at T = ∞ (checked).** Random gauge configurations sample the flux sectors uniformly.

| Lattice | L | r |
|---|---|---|
| honeycomb | 8–24 | 5e-30 to 4e-29 |
| 2D square | 6–20 | about 1e-30 |
| 3D cubic | 6–10 | about 1e-30 |

- One degenerate 3D L = 4 sample gave r = 0.03.
- Small-cluster spin ED (N = 8, 10, 12) gives r = 0.375, 0.0625, 0.118. These are dominated by degenerate sectors.
- **By F1, no local conserved improvement with support inside a 24×24 honeycomb torus exists** (proved from checked numbers).

**K4. Finite flux density, i.e. any T > 0 (checked).** The flux density is about e^{−Δ/T} > 0.
- **Exact degeneracy ratio** (`c2_kitaev_dilute.out`):
  - at q = 0.02 (flux density about 0.04), r = 0.54, 0.27, 0.065, 0.036, 0.011 and 0.0072 for L = 8 to 40;
  - at q = 0.005 (flux density about 0.01), r goes from 0.88 to 0.08.
  - This tracks the probability that a sample is flux-free or symmetric.
- **Order-of-limits-safe check:** the weight below frequency δ, r_δ, at L large compared with 1/spacing (`c2_kitaev_window.out`).
  - At q = 0.02, L = 32: r_δ = 0.86, 0.74, 0.56, 0.36, 0.21 and 0.10 for δ = 0.4 down to 0.0125. **It is linear in δ** at small δ, i.e. a Lorentzian peak of width Γ ≈ 0.1. **D = 0.**
  - At q = 0.1 (L = 16–32): r_δ = 0.089, 0.043 and 0.019 for δ = 0.05, 0.025 and 0.0125. The values do not change with L at fixed δ, so they are converged, and the width is Γ ≈ 0.5.
  - At q = 0.005 (L = 40): r_δ = 0.60 at δ = 0.0125, still falling, with Γ ≈ 0.02–0.03.
  - So Γ ∝ q ∝ flux density.
- Reading: heat transport at low T is diffusive with κ ∝ 1/Γ ∝ e^{+Δ/T}, which is large but finite. It is not ballistic.
- Comparator, V (abstract): Metavitsiadis, Pidatella and Brenig, PRB 96, 205121 (2017), arXiv:1707.03836. The thermally activated Z2 flux acts as emergent disorder, and the system is "a dissipative heat conductor".
- Comparator, V (search summary only): the Kitaev ladder, PRB 96, 041115 (2017), has no ballistic channel.

**K5. Operator level (checked).**
- ‖[H, J]‖ / (‖H‖‖J‖) = 1.155 per cell on the infinite lattice. ED agrees after rescaling by √N.
- A patch search over 690 strings on 4-site patches does not reduce it at all (residual 1.000).
- With a [111] field h = 0.1 the ratio is 1.162, and the residual is 0.997.

**K6. On qubits on Z³ (suggested).**
- A Kitaev-type solution needs each site's bond operators to be distinct anticommuting Paulis. With one qubit per site that allows coordination ≤ 3.
- A cubic-covariant nearest-neighbour rule on Z³ has coordination 6, so it cannot be of Kitaev type without grouping sites or using 4-dimensional sites (Γ-matrix models), and that breaks the Qubit or covariance structure.
- Even if it were available, it is category (ii).

---

## 3. Generic interacting 2D models

### Operator algebra (checked; infinite lattice; `c2_algebra.out`)

The table gives ρ = ‖[H, J^x]‖ / (‖H‖‖J‖), with HS norms per cell, and the improvement residual min‖[H, J + i[H, B]]‖ / ‖[H, J]‖. B runs over all strings on a 2×2 plaquette and 3-site lines, about 300 strings (465–690 for two-sublattice lattices).

| Model | ρ | Residual |
|---|---|---|
| 2D TFIM, h = 3 | 0.853 | 0.665 |
| 2D XX (hard-core bosons) | 2.83 | 0.919 |
| 2D compass | 2.83 | 0.707 |
| Xu–Moore, h = 1 | 2.83 | 0.692 |
| toric code + h_z = 0.3 | 0.575 | 0.999 |
| Kitaev | 1.155 | 1.000 |
| Kitaev + [111] h = 0.1 | 1.162 | 0.997 |
| controls: XX chains, Kitaev J_z = 0 (chains), stacked XXZ Δ = 0.5 | **0** | — |

The interacting integrable control (stacked XXZ) gives exactly 0. That validates the algebra code against Zotos–Naef–Prelovšek.

### ED, β = 0 Drude ratio r(N)

Clusters are N = 8, 9, 10, 12 (square) and N = 8, 10, 12 (two-sublattice). Source: `c2_ed.out`.

| Model | r(N) |
|---|---|
| TFIM, h = 3 | 0.251, 0.209, 0.096, 0.092 |
| TFIM, h = 1 | 0.183, 0.114, 0.041, 0.033 |
| XX | 0.303, 0.285, 0.165, 0.118 |
| compass | 0.203, 0.250, 0.142, 0.079 |
| Xu–Moore, h = 1 | 0.354, 0.196, 0.102, 0.054 |
| toric code + field | 0.307, 0.200, 0.137 |
| Kitaev + field | 0.000, 0.032, 0.012 |
| controls | 1.000 at every N and β |

- By F1, r(N) is not constant, so no conserved local improvement with support fitting these clusters (about 3×3) exists.
- The finite-β columns are dominated by low-lying degeneracies at these sizes and are not used.

### Theorems (comparator, V at abstract or search-summary level)

- **Shiraishi and Tasaki, arXiv:2412.18504.** S = ½ XY and XYZ models on hypercubic lattices with d ≥ 2, arbitrary field, X and Y couplings nonzero: no nontrivial local conserved quantities. This includes XX. The authors suggest that Ising in a parallel field is the only standard model in d ≥ 2 that has them.
- **Chiba, arXiv:2412.18903, PRB 111, 195130 (2025).** Ising with transverse and longitudinal fields, d ≥ 2: no local conserved quantity other than H. "Local" here allows support up to half the system in one direction.
- **Futami and Tasaki, arXiv:2502.10791, J. Math. Phys. (2025).** The square-lattice compass model: none except H.
- **Futami.** The same for the Hubbard model in d ≥ 2 (search summary; arXiv number not verified).

**Reduction (proved).** These models are symmetric under x-reflection R, and R J R = −J.
1. Suppose J' = J + i[H, B] is conserved.
2. Then the R-odd part J + i[H, (B − RBR)/2] is also conserved and local.
3. The theorems leave only H and the trivial charges (magnetization where present), and all of these are R-even. So that part is 0.
4. That means J = −i[H, B_odd], so J̄ = 0 on every torus that fits the support.
5. This contradicts r(N) > 0 in ED, and in any case it would mean D = 0.

So **for TFIM, XY/XYZ/XX and compass in d ≥ 2, no conserved local improved current exists**, within the theorems' locality class. This is proved via the comparator. Quasi-local improvements are not covered: the theorems are for local quantities, and quasi-local versions are listed as open.

---

## 4. Other classes (suggested or comparator)

- **Free-fermion-solvable spin models.**
  - Kitaev and its JW form (Feng–Zhang–Xiang, PRL 98, 087204 (2007), M).
  - Exact 2D bosonization (Chen–Kapustin–Radičević, Ann. Phys. 393, 234 (2018), M).
  - Line-graph "free fermions in disguise" (Chapman–Flammia, Quantum 4, 278 (2020), M).

  Where a Z2 gauge constraint is needed, constraint-violating sectors are static defects. In the full qubit space that gives K2/K4 (suggested). Where no gauge sectors arise, the model is non-interacting, so it does not meet "interacting" (reading). None was found on Z² or Z³ with genuinely 2D or 3D hopping and no gauge sectors (search not done).
- **Integrable interacting lattice models in d ≥ 2 with factorized scattering.** None is known (M). Zamolodchikov tetrahedron solutions give 3D classical or 2+1 circuit models, not local Hermitian Hamiltonians with ballistic transport (M).
- **Dual-unitary or Floquet circuits.** These have no conserved energy and break the continuous-time requirement. Excluded.
- **Disorder-LIOM (MBL) systems.** They break translation covariance and are insulating (D = 0). MBL in d ≥ 2 is contested by the avalanche argument (De Roeck–Huveneers, PRB 95, 155129 (2017), M). Excluded.
- **Classical momentum-conserving anharmonic lattices.** They show anomalous, not ballistic, heat transport in 2D (κ ~ log L; Lepri–Livi–Politi, Phys. Rep. 377, 1 (2003), M). Their momentum is a field-shift charge of continuous displacements, which is not available with qubits (reading).

---

## 5. Against the FIXED readings

| Candidate | [H, J_E] | Conserved improvement in searched or all-local space? | Drude (scaling) | Category |
|---|---|---|---|---|
| toric code, quantum doubles, string nets, X-cube, Haah, Xu–Moore h = 0 | J_E ≡ 0 | only 0 (F1, F2) | 0 | (i) trivial, immobile |
| Kitaev honeycomb (± field), 3D Kitaev/Γ variants | ≠ 0 (1.16) | none, any local B with support < 24 (F1 + K3) | 0 at T = ∞; at T > 0 peak width ∝ flux density | (ii) sector-only (zero-flux, free) |
| TFIM, XX/XY/XYZ, compass (2D) | ≠ 0 | none: theorem + parity (§3) | r(N) ↓ | fail |
| Xu–Moore h = 1, toric code + field | ≠ 0 | none in ~300–465 patch strings; r(N) ↓ (supports ≲ 3×3) | r(N) ↓ | fail (weaker) |

**C2 worker reading: FAIL (bounded to these candidates).**

---

## 6. Flags for the referee (stated so the readings are not quietly bent)

1. **Literal FAIL wording.** The FAIL text says every candidate has [H, J_E] ≠ 0. For the commuting-projector class [H, J_E] = 0 holds only vacuously, because J_E ≡ 0 with D = 0. The brief itself classes these as (i), useless, and they cannot meet PASS's Drude clause. I count them as non-passing, not as a counterexample to FAIL.
2. **A PASS-shaped degenerate example.**
   - Stacked interacting XXZ chains on Z²: x-bonds only, Δ = 0.5.
   - J^x is exactly conserved (checked: ρ = 0; ED r = 1 at N = 8–12 and all β).
   - J^y ≡ 0.
   - D_xx > 0 (Zotos–Naef–Prelovšek, comparator).
   - This meets the PASS sentence literally except that it is not d ≥ 2 in any physical sense.
   - **I do not count it, for three reasons:**
     - (a) it is not covariant under the proper cubic rotations of the lane-RG class and the Lattice/Admissibility memo;
     - (b) E is independent of k_y, so nothing moves along y;
     - (c) one vertical coupling g = 0.2 destroys conservation (ρ = 0.82).
   - **Proved:** with one qubit per site, a translation- and rotation-covariant rule cannot hold mutually commuting non-classical chains along every axis. A chain term that uses two non-commuting Paulis at a site leaves only scalars in that site's commutant, so a crossing chain must interact with it or be trivial there. This is proved for term-wise commuting chain families.
   - If the referee reads PASS without covariance, this example decides it, and it is gravitationally irrelevant.
3. **What is not closed.**
   - Quasi-local improvements in the Xu–Moore and field-perturbed models beyond the patch and cluster sizes.
   - 3D generic models (no 3D ED was done here).
   - Exotic constructions that were not examined.

   RG's open corner (dressed walls at strong coupling) is not excluded as a class. It is only not realized in any candidate examined.

## 7. Strong words checked

- **"Exactly zero" (K2)** is a finite-size identity for non-degenerate spectra. The checks are at 1e-14 to 1e-30.
- **"No local improvement" (Kitaev)** holds for supports fitting the L = 24 torus, from F1. It is not a statement about quasi-local B with long tails.
- **"Theorem-excluded"** depends on the cited papers' hypotheses: nonzero couplings, hypercubic lattices, and their locality definition. I read abstracts and search summaries, not the proofs.
- **"D = 0 at T > 0" for Kitaev** is checked numerically for flux densities of 0.01–0.04 at L ≤ 40 on a Majorana-temperature proxy. It agrees with the literature, but no proof is given.
- **ED sizes are small (N ≤ 12).** The ED claims are used only through F1, which needs no extrapolation.
