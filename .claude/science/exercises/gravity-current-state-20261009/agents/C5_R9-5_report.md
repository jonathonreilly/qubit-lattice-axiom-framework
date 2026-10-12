# C5 R9-5 report: box-confined Poincaré on a qubit lattice (⊗M₂), with honest sector accounting

**Author.** Claude Opus 5.5 probe (same family as the supervisor and every C5 worker). Unrefereed. 2026-10-12, 16:39Z to about 17:10Z. No repository file edited.
**Scratch.** `S/` = `.../scratchpad/C5/R9-5/`. Scripts and outputs in `S/scripts/` (all OMP_NUM_THREADS=2, each < 3 min):
- `r95_common.py` (the dispersion, the dimer lattice, the translation-covariant string paths);
- `r95_signed_ed.{py,out}` (full signed spin-operator check of the fermion dictionary);
- `r95_jet_bound.{py,out}` (explicit tail constants by exact derivative jets; the norm certificate);
- `r95_tails.{py,out}` (coefficients, envelope; its spectral C_8 is roundoff-dominated and is **superseded** by `r95_jet_bound`);
- `r95_visons_R12_L40.out` (from `r95_visons.py 12 40`), `r95_visons_conv.{py,out}`, `r95_tmatrix16.{py,out}` (vison sectors of the actual law);
- `r95_z3_graph.{py,out}` (d = 3 feasibility).

**Read.** `docs/MINIMAL_AXIOMS_2026-06-29.md` in full (cited AX); `TESTS.md` C5 method (2302–2319), R6-1 setting (3030–3070), R7-1 pre-registration (3240–3256), referee results 3285–3345, 3396–3441, 3541–3573, Round 9 (3575–3791; R9-5 at 3742–3765); `agents/C5_S8_synthesis.md` §4 item 8, §5, P26/P30 rows (229, 233); `SUMMARY.md` §§21–23; `agents/C5_R7-3_report.md` + `C5_R7-3_referee_verdict.md`; `C5_R7-1_report.md` + verdict; `C5_R6-1_referee_verdict.md`; `C5_R8-2_report.md` §3 + verdict; packet scripts `scripts/C5/R7-3/*`, `scripts/C5/R7-1/r71_box_poincare_free.py`.
**Labels.** proved / checked (numerics here) / suggested / reading / comparator / RECALLED (literature from memory, not verified here). "Web-verified" = abstract fetched this session.

---

## 0. In plain words

- **Yes, the free box law lives on plain qubits — in one sector.** Take one qubit per site of Z², wired as Kitaev's brick wall. Replace Kitaev's three nearest-neighbour terms by a long, rapidly decaying sum of Kitaev "strings" whose coefficients are R7-1's box dispersion. In the sector with no vortices (every plaquette operator W_p = +1), the qubits behave *exactly* as one free fermion per dimer whose energy is √(m² + k²) inside the box. R7-1's exact Poincaré algebra then holds there at every particle number, with ordinary (ungraded) qubit composition.
- **I checked the hard part with all signs kept.** On 12- and 16-qubit flakes, the spin operators reproduce the free-fermion algebra and spectra to 1e-13 (the R7-3 referee's gap: phases had been dropped there).
- **The tails are certified.** Each string is a Pauli product of weight ≤ 2|r|₁ + 2. With explicit derivative bounds on the coefficients, the interaction norm is finite for every polynomial weight, with numbers (e.g. 21.54, 304.8, 7754 for weights (1+d)⁰, (1+d)¹, (1+d)²).
- **What lives in the other sectors.** Vortex ("vison") sectors. The law never creates or moves visons, so they are perfectly static: a flat band, frozen in the lattice frame. A box particle passing a vison pair scatters sideways strongly (|t| ≈ 1.7), so in those sectors there is no exact momentum, hence no Poincaré algebra.
- **A surprise: this law prefers visons.** Without help, inserting visons *lowers* the energy (about −0.0076 per vison in lattice units). So the law needs an extra plaquette term −Δ_v Σ W_p with Δ_v > 0.0038 to make the vortex-free sector the ground sector. Δ_v is free, so the vison gap can be put anywhere up to the cutoff; it is not forced low.
- **The price.** Ordinary qubit composition is kept (so P26(c)'s graded composition is not used). Instead the law pays:
  - exactness only in a dynamically invariant sector that one local σ^z leaves;
  - a gauge constraint (every term must commute with every W_p);
  - the plaquette term;
  - loss of full grid symmetry: only half the translations and no site-centred rotation (structural for this kind of construction);
  - the inherited R7-1/R8-2 scope (free only, local-domain boosts, doublers or gapped edge, super-polynomial non-exponential tails).
- **Worker reading: PASS (with scope).** The registered expectation was INCONCLUSIVE.

---

## 1. Hypotheses and classes (stated before titles)

- **H-spin.** ⊗_{Λ} M₂(C), Λ = Z² (d = 3 in §4.7), ungraded tensor product, one qubit per site. Continuous time (Z^d × ℝ), as R7-1.
- **H-law.** H_spin is a (super-polynomially) quasi-local sum of Pauli strings, Σ_X Φ(X), with ‖Φ‖_F = sup_x Σ_{X∋x} ‖Φ(X)‖ F(diam X) < ∞ for stated F.
- **H-sector.** "Flux-free sector" = the joint +1 eigenspace of all plaquette loop operators W_p (each the ordered product of the six Kitaev bond operators around a hexagon, starting at an A site). In infinite volume: the W_p = +1 subspace of the vacuum (toric-code-type) superselection sector (even fermion number), together with that of the ε sector (odd fermion number; RECALLED identification, Kitaev 2006).
- **H-box.** R7-1's free box law exactly: s(k) = ρk + (1−ρ)sin k, ε̃ = √(m² + s(k₁)² + s(k₂)²), Gevrey-2 plateau, b = 2.0, b₂ = 3.1, m = 0.3 (`scripts/C5/R7-1/r71_box_poincare_free.py:22-49`), now on the dimer lattice.
- **Excluded (as pre-registered, `TESTS:3747-3750`):** interactions beyond R7-1's free law; gravity. Also not addressed: pair creation, gauge fields, finite temperature, Route B constructions beyond comparator level.

## 2. Prior art (each counted once)

- **R7-3** (`TESTS:3543-3548`; `C5_R7-3_referee_verdict.md:5-35`): the Kitaev brick wall with spin strings, flux-free exact momentum; Lemma S confirmed (`:5-9`); the two gaps this item closes — phases dropped in the Pauli runner (`:25`), and vison scattering computed for the bare H_K rather than the actual law (`:27`). Also: "sector-only does not meet R7-3's clause" (`:31`). R9-5's clause expressly allows a stated invariant sector (`TESTS:3761`).
- **R6-1** (`TESTS:3316-3329`; `C5_R6-1_referee_verdict.md:17`): CAR witness outside ⊗M₂; locality-preserving 2D bosonization needs gauge qubits and constraints.
- **R7-1** (`TESTS:3398-3407`; `C5_R7-1_referee_verdict.md:273-275`): P1, the free box algebra at every N on C_c^∞(int B^N); used here unchanged.
- **R8-2** (`TESTS:3552-3553`; `C5_R8-2_referee_verdict.md:49-58`): literal profile has 2^d − 1 mass-m corner valleys; gapped edge ceiling √(m²+b²).
- **In-repo Kitaev/BKSF notes (counted once, not used as premises):** `docs/DYNAMICS_CLAUSE_RECORDS_CARVE_EXACTLY_SOLVABLE_THREE_DIMENSIONAL_KITAEV_NETWORKS_..._2026-09-24.md` (3D Kitaev networks carved in Z³), `docs/DYNAMICS_CLAUSE_RECORDS_CARVE_KITAEV_MODELS_AT_THE_COMPASS_POINT_..._2026-09-24.md:52-54` (in that model the least-energy translation-invariant flux sector is π-flux, not zero flux — the same phenomenon as §4.4(c) here), `docs/BRAVYI_KITAEV_SUPERFAST_PI_FLUX_SIGN_CLASS_FINITE_CUBIC_GRAPH_..._2026-09-02.md` (BKSF face-transport sign class on cubic graphs).
- **Literature.** Kitaev, cond-mat/0506438 (web-verified by R7-3; counted once). CKR 1711.00515 and Chen–Xu 2201.05153 (web-verified by R7-3; counted once). Bravyi–Kitaev, quant-ph/0003137 "Fermionic quantum computation" (web-verified this session: local fermionic gates on bounded-degree graphs simulated at constant qubit overhead). Wu–Arovas–Hung, 0811.1380 (web-verified: 4×4 Γ-matrix Kitaev generalization on a *decorated* square lattice; 4-dim sites). RECALLED, not verified: Lieb's flux theorem; Pedrocchi–Chesi–Loss projection rule; Yao–Zhang–Kivelson square-lattice Γ model; Gevrey-class Fourier decay exp(−c|r|^{1/s}).

---

## 3. The law (Route A), explicit

**Geometry** (`r95_common.py:1-12`). Brick wall in Z² as R7-3: z bond (X,Y)–(X,Y+1) iff X+Y even; x bond A(X,Y)–B(X+1,Y); y bond A(X,Y)–B(X−1,Y); A = (X+Y even). Unit cell = z-dimer n = (n₁,n₂): A at (n₁+n₂, n₁−n₂), B one step up. Dimer Bravais vectors e₁ = (1,1), e₂ = (1,−1) are orthogonal and of equal length, so the dimer-coordinate Euclidean metric is the Z² metric (×2): the box law's rotations are rotations of the physical plane.

**Strings.** K_e = σ^α_iσ^α_j on a bond e of type α. For each displacement r a fixed, translation-covariant monotone path γ_r from A_R to B_{R+r} (and AA, BB paths) built from pairs of bond moves (`r95_common.py:_pairs, path`); length ℓ(r) = 2·pairs + 1 ≤ 2|r|₁ + 1 (checked against the constructor, `r95_tails.out:3`). S_γ = ordered product of the K_e along γ: a Pauli string of weight ℓ+1, norm 1.

**The Hamiltonian.**

  H_spin = −½ Σ_R Σ_{r∈Z²} M(r) S_{γ_r}(A_R → B_{R+r})  −  Δ_v Σ_p W_p,

with M(r) the real, even Fourier coefficients of ε̃ on the dimer lattice (M(0) = 1.735523; ε̃ = √(m²+k²) on the closed box to 8.9e-16; `r95_tails.out:1-2`). The r = 0 term is −½M(0)σ^zσ^z on each dimer (ferro-z, as Kitaev's A_z phase). Δ_v is the plaquette coefficient (range-6 term); §4.4 shows it is needed (Δ_v > 0.0038).

**The generators.** P_j, K_j, J of R7-1 are dΓ of one-body operators; their spin images are Φ(h) below (AA, BB and AB strings with the same kernels as R7-1, K and J with linear weights).

---

## 4. Results

### 4.1 Dictionary Theorem D — proved (standard Kitaev algebra); checked with all signs

- **Statement.** In Kitaev's representation σ^α_j = i b^α_j c_j with uniform gauge u_{AB} = +1, every ordered bond-operator string along a path of n bonds equals (−i)^n ∏u · c_start c_end. On a bipartite trivalent graph, a path A→B (n odd) has ∏u = (−1)^{(n−1)/2}, so S(A→B) = −i c_A c_B for *every* path; A→A and B→B paths give S = c c′; every closed ordered loop equals +1. Hence the flux-free sector is W_p = +1 and, with d_R = (c_{A,R} + i c_{B,R})/2,
  - d_R†d_R = (1 − S(A_R→B_R))/2,
  - d_R†d_{R′} = ¼[S(A_R→A_{R′}) + S(B_R→B_{R′}) − S(A_R→B_{R′}) − S(A_{R′}→B_R)] (R ≠ R′).

  Define Φ(h) = Σ h_{RR′}·(this dictionary). Then on the flux-free sector Φ(h) = dΓ(h) for every one-body h.
- **The law.** Because M is even, the AA/BB parts cancel in Φ(M) on the sector, so H_spin (Δ_v term aside) = Σ_{RR′} M(R′−R) d_R†d_{R′} − N M(0)/2 = Σ_k ε̃(k) d_k†d_k − const. The vacuum is the d-empty state (all dimers σ^zσ^z = +1, all W_p = +1); it is unique because ε̃ ≥ m > 0.
- **Checked** (`r95_signed_ed.out`; full Pauli phases kept; open flakes of 2×3, 3×2 dimers = 12 qubits, and 2×4 = 16 qubits):
  - W_p Hermitian, involutive, commuting: 0.0; [Φ(h), W_p] = 0.0 exactly, for the box law and for random complex Hermitian h.
  - Lie homomorphism on the sector, P([Φ(a),Φ(b)] − Φ([a,b]))P: max 9.7e-16 and 1.5e-15 (12 qubits; scale |Φ| ≈ 4); random-vector residual 5.4e-15 (16 qubits).
  - Spectrum of Φ(h) on the W_p = +1 sector = the full Fock spectrum of h (both parities) × uniform multiplicity 16 (the open-boundary b-Majoranas): max deviation 9.8e-14 (box law), 4.0e-14 (random complex Hermitian).
  - The law as written equals Φ(M) − N M(0)/2 on the sector: 8.6e-14 (12 qubits), 1.1e-15 (16 qubits, random vectors); ground energy 0 = Fock vacuum (16 qubits, eigsh).
- This closes the R7-3 referee's "phases dropped / signed isomorphism not checked" gap (`C5_R7-3_referee_verdict.md:25`) for this law.

### 4.2 The free box Poincaré algebra on the flux-free sector at every particle number — proved; checked

- **Claim.** On 𝒟_B^spin = flux-free states whose d-fermion wavefunctions are finite-particle and C_c^∞ in int(B)^N, the spin operators Φ(ε̃), Φ(s), Φ(½{ε̃, X}), Φ(J) satisfy R7-1's undeformed Poincaré relations exactly, with R7-1's rapidity budget η* = asinh(b/m_⊥) − |θ| and leakage bound 2‖1_E ψ‖.
- **Proof.** Theorem D gives Φ = dΓ on the sector; every Φ(h) preserves the sector (it commutes with all W_p); R7-1's P1 (`C5_R7-1_referee_verdict.md:41-48,70-77`) is a statement about dΓ of one-body operators on that domain. ∎
- **Particle numbers.** Even N: in the vacuum superselection sector. Odd N: in the ε sector (a single fermion needs a semi-infinite string in infinite volume; RECALLED identification). On finite open flakes both parities are present in the flux-free sector (checked: the full Fock spectrum appears, §4.1).
- **Checked.** The homomorphism identity (§4.1) for arbitrary complex one-body operators transfers every one-body bracket, including R7-1's (`scripts/C5/R7-1/r71_box_poincare_free.out` (C), residuals ≤ 1.3e-11 inside the box; counted once, not rerun).

### 4.3 Norm-certified tails — proved; constants checked

- **Bound (proved, elementary).** Each site lies on at most ℓ(r)+1 translates of γ_r, and ‖S‖ = 1, so

  ‖Φ‖_F ≤ Σ_r ½|M(r)| (ℓ(r)+1) F(ℓ(r)),  ℓ(r) ≤ 2|r|₁ + 1.

  Integration by parts on T² gives |M(r)| ≤ C_p/|r|_∞^p, with C_p = max_j (2π)^{-2}∫|∂_j^p ε̃|. ε̃ ∈ C^∞(T²), since m > 0 and s is C^∞ (`C5_R7-1_referee_verdict.md:131-137` for the class). So ‖Φ‖_{F_n} < ∞ for F_n(d) = (1+d)^n and every n: super-polynomial quasi-locality.
- **Not exponential (inherited, proved in R7-1).** ε̃² cannot be real-analytic (`C5_R7-1_report.md:130-131`, counted once).
- **Explicit constants (checked; floating point, not interval arithmetic; `r95_jet_bound.out`).** C_p for p = 2…40 come from exact Taylor-jet arithmetic through the formula, with no Fourier data, so no roundoff × r^p. C₀ = 1.735523 = M(0). The envelope min_p C_p ρ^{−p} bounds the FFT shell maxima at every checked ρ: 3.3e-3 vs 5.5e-4 (ρ = 16), 1.5e-6 vs 2.8e-7 (64), 2.7e-12 vs 1.2e-12 (256). Certified totals (finite part |r|_∞ ≤ 512 plus tail bound):

| weight F(d) | ‖Φ‖_F ≤ | of which tail bound |
|---|---|---|
| 1 | 21.543 | 1.1e-8 |
| (1+d) | 304.79 | 2.4e-5 |
| (1+d)² | 7754.1 | 5.3e-2 |
| (1+d)⁴ | 2.00e7 | 2.6e5 |
| (1+d)⁸ | 6.9e18 | 6.9e18 (tail-dominated) |

- **Finite-range envelope** (`r95_tails.out:7-8`): shell maxima 2.1e-2, 5.5e-4, 2.0e-5, 2.8e-7, 1.9e-9, 1.2e-12 at ρ = 8, 16, 32, 64, 128, 256. A stretched-exponential fit gives β = 0.39 over 16–256 (finite-range evidence; Gevrey-2 theory β = ½ RECALLED).
- `r95_tails.out`'s "C_8 = 4.7e17" and its tail bounds are roundoff-dominated (spectral derivative of FFT data), and are superseded by the jet constants (C_8 = 4.93e8).

### 4.4 The complementary (vison) sectors — computed for the actual law

**(a) Static, never generated — proved.** Every term of H_spin, and every generator Φ(h), is a product of Kitaev bond operators. Each bond operator commutes with every W_p (Kitaev; checked: [Φ(h), W_p] = 0.0 in §4.1). So all flux sectors are exactly invariant: visons have zero hopping (an exactly flat band at every vison momentum), and no term of the law connects sectors. Sector-connecting local operators exist: a single σ^z_j flips the two W_p sharing j's z bond (R7-3, `TESTS:3544`; counted once). But they are not generated by the dynamics.

**(b) Energies — checked, converged in the hopping truncation** (`r95_visons_conv.out`; the fermion part is the vacuum shift −½Σσ(M_ab(F)) + ½Σσ(M_ab(0)), with truncation |r|_∞ ≤ RMAX on an L×L dimer torus; lattice units, m = 0.3, b = 2):

| RMAX / L | local pair (one σ^z) | pair at D = 12 | single vison ≈ ½(D=12) | π-flux, per plaquette | π-flux gap |
|---|---|---|---|---|---|
| 12 / 40 | −0.00965 | −0.01496 | −0.0075 | −0.000359 | 0.528 |
| 16 / 48 | −0.00974 | −0.01519 | −0.0076 | −0.000359 | 0.526 |
| 24 / 64 | −0.00975 | −0.01522 | −0.0076 | −0.000359 | 0.525 |
| 32 / 80 | −0.00976 | −0.01523 | −0.0076 | −0.000359 | 0.525 |

- The pair energy saturates by D ≈ 6 (−0.01495 at D = 6, `r95_visons_R12_L40.out`), so the vison–vison interaction is short-ranged.
- No fermion level lies below the flux-free gap in any tested vison sector (RMAX = 32: lowest levels 0.29889 (local pair) and 0.29972 (D = 12) against the flux-free gap 0.29865 of the same truncated law; finite-L statement).
- The total energy of a sector with n_v visons includes +2Δ_v n_v from the plaquette term.

**(c) Ground-sector selection needs the plaquette term — checked (tested configurations).**
- At Δ_v = 0 every tested vison configuration lies *below* the flux-free sector. Lieb-type flux selection (RECALLED; proved for nearest-neighbour honeycomb) does not extend to this long-range law. The in-repo compass-point note finds the same kind of non-zero-flux preference for its model (counted once).
- With Δ_v > 0.0038, the flux-free sector is lowest among all tested configurations: single vison 2Δ_v − 0.0076; local pair 4Δ_v − 0.0098; π-flux 2Δ_v − 0.00036 per plaquette.
- General stability over *all* flux configurations is suggested, not proved: a trace-norm bound grows with the gauge string length, not the vison number.
- **The vison threshold is then a free parameter:** E_pair = 4Δ_v − 0.0098. It can be placed at or above the cutoff. It need not set a low edge-like threshold below R8-2's doublers (mass m) or gapped edge (≤ √(m²+b²)).

**(d) Parity — checked.** sign det M_ab(F)/det M_ab(0) shows that the local-pair sector's vacuum has the opposite fermion parity to the flux-free vacuum, and the D = 12 sector's has the same. One flipped u (from one σ^z) with flipped c-parity is the physical combination (projection rule, RECALLED), so one σ^z creates the vison pair without a fermion. This is consistent with the toric-code picture (RECALLED).
- The "no zero crossing" line in `r95_visons_R12_L40.out` comes from an 11-point scan too coarse to see the crossing, and is superseded by the determinant sign.

**(e) Non-Poincaré: box particles scatter sideways off a static pair — checked; with Lemma S, proved consequence.**
- Exact one-fermion on-shell T-matrix of the *actual* law's sign-flip perturbation (not the bare H_K; this closes `C5_R7-3_referee_verdict.md:27`), with an infinite-volume Green function by BZ quadrature (`r95_visons_R12_L40.out`, `r95_tmatrix16.out`).
- Box momentum k = (0.50, 0.20), E = 0.6164, all outputs exactly on shell:

| out-momentum | RMAX=12 (Nk 1024, η .005) | RMAX=16 (η .005) | Born |
|---|---|---|---|
| rotated 90° | 1.830 | 1.827 | 0.057 |
| backward | 1.773 | 1.781 | 0.052 |
| mirror (k₂,k₁) | 1.708 | 1.698 | 0.062 |
| rotated 45° | 1.702 | — | 0.063 |

  - Stable to ≤ 0.5% over Nk 512/1024, η 0.02–0.005 and RMAX 12/16.
  - Second momentum k = (1.2, −0.7) at RMAX 16: rotated 0.93, backward 1.57, mirror 1.51.
  - The amplitude is non-perturbative (Born ≈ 0.06). The flipped dimer reverses the largest coupling, M(0).
- The defect (a vison pair at position R) is a translation-covariant, scalar, flat-band defect with p-independent dynamics and a nonzero non-forward kernel. So Lemma S (refereed, `C5_R7-3_referee_verdict.md:5-9`) excludes any bounded additive momentum lift in that sector. Hence no exact additive P, and no box Poincaré algebra, there.
- The vison sectors are therefore a non-Poincaré, lattice-frame-fixed sector: exactly flat, so E(p) = const. Unlike R7-1's decoupled edge, they *do* couple to box matter (Aharonov–Bohm-type scattering).

**(f) Robustness (suggested).** Any generic local term not built from bond operators (e.g. h σ^z) connects sectors. Visons would then become mobile at O(h²/Δ_vis), and the flux-free sector would no longer be invariant. The box algebra would then be exact only at h = 0; violations are expected at O((h/Δ_vis)²). Not computed.

### 4.5 Why the covariance loss is structural for this route — proved (elementary), with scope

- **Lemma C1.** A Kitaev-solvable graph (trivalent, every vertex with one bond of each colour) cannot have one site per primitive cell. If site R's α-bond goes to R + v_α, the α-bond at R + v_α must return to R, so 2v_α = 0. Hence ≥ 2 sites per cell, and qubit-level covariance is under an index-≥2 translation subgroup.
- **Lemma C2.** Using 3 of the 4 Z² directions at a site cannot be invariant under the site-centred C4 that the Lattice axiom names (`AX:37-41`). So no site-centred proper rotation is a symmetry of any trivalent-subgraph law.
- **Lemma C3.** One Majorana per site on a Bravais lattice gives h(k) = iÂ(k) odd in k, hence h(0) = 0, so the band is gapless. A *massive* box law therefore needs ≥ 2 Majoranas per cell.
- **What survives.** The string law is covariant under the dimer translations (index 2; the paths are translation-covariant by construction). The brick-wall *bond pattern* also has a glide (X,Y) → (X+1,−Y) combined with the on-site unitary exchanging σ^x and σ^y (it maps x-bonds to y-bonds). Whether the full string law is glide-covariant depends on choosing glide-covariant paths: it is automatic on the flux-free sector (path independence), but not checked in the vison sectors.
- **Comparator.** Γ-matrix models restore more covariance with 4-dim sites (Wu–Arovas–Hung, web-verified: decorated square lattice). This is a price on Qubit's M₂(C) (`AX:47`), not taken.

### 4.6 Route B (BKSF / CKR) — comparator and suggested, not built

- Bravyi–Kitaev superfast and CKR put one qubit on each edge of the fermion lattice Z². Edge midpoints of Z² form a rotated square (medial) lattice, so this is again one qubit per site of a square lattice. Translation by one medial step exchanges vertex- and face-centred plaquettes (fermion sites ↔ constraint sites), so covariance is again index 2 (suggested).
- The constraint sector is the flux/Gauss-violating sector. If the law commutes with the constraints, it is static, as in §4.4(a). Lemma S applies once a non-forward amplitude is computed; that is not done here for BKSF/CKR.
- The in-repo BKSF note fixes a π-flux sign class for BKSF face transport on cubic graphs (counted once). In that encoding the "flux-free" sector for the fermion hopping is a stated sign class, which must be matched when porting §3.
- Route A is the realized construction; Route B is expected to give the same sector structure (suggested).

### 4.7 d = 3 — feasibility checked; algebra by the same proof; vison loops not computed

- `r95_z3_graph.out`: A(X,Y,Z) with X+Y+Z even. Bonds are x → B(X+(−1)^Y, Y, Z), y → B(X, Y+1, Z) and z → B(X, Y, Z+1). Every site of Z³ is used once, with one bond of each colour. The graph is connected on an 8³ torus with winding rank 3, i.e. three-dimensional.
- The all-(+1) choice splits into 2D sheets (rank 2), and the (−1)^{Y+Z}-type choice into 8-site clusters.
- Theorem D's proof uses only bipartiteness and trivalence, so the flux-free dictionary and §4.2 carry over to the fcc dimer lattice, with the box law written in its Bravais coordinates (proved by the same argument; no 3D numerics).
- In 3D, flux sectors are closed flux loops whose energy grows with length (suggested; not computed). Lemmas C1–C2 apply (cubic site-centred rotations fail).

---

## 5. Prices (named, not adopted) — probe (d)

1. **Sector restriction.** Exact box Poincaré holds only on the flux-free sector. It is dynamically invariant but not superselected: one σ^z leaves it (`C5_R7-3_referee_verdict.md:31`, counted once). In vison sectors exact momentum fails (§4.4e).
2. **A constraint on the law.** Every term must commute with all W_p (be built from Kitaev bond operators): a local Z₂ gauge-invariance condition on the dynamics. [Reading] Dynamics is outside the axiom texts (`AX:116-130`), so this is a law choice needing registration or derivation, not an axiom-text change. S8's question whether it reads as an "Admissibility-type rule" (`C5_S8_synthesis.md:233`) remains a reading: Admissibility's text is about a probability distribution (`AX:57-60`), not a Hamiltonian constraint.
3. **A plaquette term with a threshold.** Δ_v > 0.0038 (lattice units, this profile; tested configurations) is needed for the flux-free sector to be the ground sector.
4. **Covariance.** Only index-2 translations plus a glide, and no site-centred proper rotations (Lemmas C1–C2). This conflicts with Lattice/Admissibility covariance (`AX:37-41,57-58`) if the dynamics law is required to share it [reading]. It is structural for one-qubit-per-site Kitaev-type routes. The emergent law is exactly rotation-covariant on the box (J closes).
5. **Tails.** Super-polynomial, non-exponential (inherited necessity; now norm-certified).
6. **The fermion is an emergent gauge-charged excitation.** Odd-N states sit in a nontrivial superselection sector (RECALLED ε identification), and the fermion braids nontrivially with visons.
7. **Inherited scope.** R7-1 (free; local-domain, not integrated covariance) and R8-2: on the dimer BZ the literal profile has 3 extra mass-m corner valleys, or use the gapped edge with ceiling √(m²+b²). Both are unchanged by the qubit encoding.
8. **The Qubit-text question P26(c).** This route uses the plain ⊗M₂ composition (`AX:47` plus the campaign reading `TESTS:3039`). So P26(c)'s *graded composition* is not paid; it is traded for prices 1–4 and 6. Whether the axiom text (which states no cross-site composition, `C5_S8_synthesis.md:229`) prefers either is the owner question this probe does not settle (`TESTS:3765`).

---

## 6. Against the FIXED readings (`TESTS:3760-3763`)

- **PASS** requires:
  - **an explicit quasi-local ⊗M₂ law:** H_spin of §3 — met;
  - **tails certified:** §4.3, proof plus explicit F_n-norm bounds — met, with constants checked in floating point, not interval arithmetic;
  - **a stated invariant sector carrying the exact free box Poincaré algebra at every particle number:** the flux-free sector, §4.1–4.2 — met (proved; dictionary checked with full signs to 1e-13); odd N in the ε sector;
  - **the complementary sectors' gap and dynamics computed:** §4.4 — met (static, exactly flat; energies converged; threshold; parity; non-forward scattering of box particles with Lemma S);
  - **the price named:** §5 — met;
  - **checked:** yes.
- **Worker reading: PASS (with scope), referee required.** The scope must travel with it:
  - the flux-free invariant sector only;
  - free matter only;
  - the plaquette threshold, checked only on tested configurations;
  - reduced lattice covariance;
  - d = 2 realized, d = 3 by the same proof without numerics;
  - Route B comparator only.
- **FAIL** is unavailable: §3 is an explicit counterexample to a no-go on the flux-free sector class.
- **If the referee requires stability of the flux-free ground sector over all flux configurations** (not just those tested), the reading drops to INCONCLUSIVE. I flag this as the weakest clause.

## 7. Strong-word check and what is not established

- "Exact" means operator identities on the flux-free sector (proved), checked to ≤ 1e-13 on 12–16-qubit flakes.
- "Certified" means a proof of finiteness for every polynomial weight, plus floating-point constants.
- "Static" and "never generated" are exact operator commutation statements.
- **Not established:**
  - all-configuration ground-sector stability;
  - interacting laws (an R7-3-type V_spin or the BT pair law) on the sector: the dictionary transfers any even fermion operator, but the R7-1/R8-1 interacting algebras are not re-checked here;
  - the robustness (h/Δ_vis)² estimate;
  - Route B's amplitude and sign class;
  - d = 3 vison loops;
  - anything about gravity (excluded), pair creation or gauge fields.
- **For the referee, check in order:**
  1. Theorem D's sign bookkeeping, against `r95_signed_ed.py`'s full-phase operators;
  2. the counting bound ‖Φ‖_F ≤ Σ½|M|(ℓ+1)F(ℓ) and the jet constants;
  3. the vison energies' sign and convergence, and whether Δ_v > 0.0038 suffices beyond the tested configurations;
  4. that the T-matrix uses the actual law's sign flips (`r95_tmatrix16.py`) and that Lemma S's hypotheses hold for the vison-pair defect;
  5. whether the sector reading meets `TESTS:3761`'s "stated invariant sector".
