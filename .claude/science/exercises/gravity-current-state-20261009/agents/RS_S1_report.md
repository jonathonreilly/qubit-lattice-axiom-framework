# Lane RS, probe S1: staggered fermions with contact interactions (Claude Opus 5.5; same family; not refereed)

**Reading against the FIXED lines: FAIL (bounded).** Both interaction classes, in d = 2 and 3, massive and massless, have no odd collision invariant at all, with or without slope. Matrix-valued (band/taste-resolved) one-body charges are included.
- **Proved** (same family, conditional; see 1e) for d = 2 at every m, and for d = 3 at m = 0.
- **Checked** (sampled finite-basis null spaces, singular gaps of order one) in all cases, including d = 3 with m > 0. That case has a taste-doublet multiplicity, which is where the proof does not reach.
- **The bound.** The result is a *necessary* condition at O(V): it covers conserved P analytic in V, empty-vacuum two-particle sector, number-conserving density–density laws as stated below. A FAIL needs a codex sol referee before it is recorded.

Scratch: `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/laneRS/S1/`. Every number below is in a `.out` file there.

## 0. Setting (stated lattice forms)

- **Free part.** h = Σ_{x,j} (i/2) η_j(x)(c†_x c_{x+j} − h.c.) + m Σ_x ε(x) n_x.
  - η_j(x) = (−1)^{x_1+…+x_{j−1}} and ε(x) = (−1)^{Σx}.
  - One complex component per site; spinless.
- **(a) Nearest-neighbour density–density.** V Σ_{x,j} n_x n_{x+j}, with kernel v_a(q) = 2V Σ_j cos q_j.
- **(b) Taste-invariant four-fermion contact.** U Σ_{all hypercubes y} Q_y², with Q_y = Σ_{x ∈ y+{0,1}^d} n_x.
  - This is the point-split taste-singlet density, squared. Summing over *all* hypercubes makes it invariant under every shift symmetry and every translation.
  - Its two-body kernel is K(r) = Π_j(2−|r_j|) for |r_j| ≤ 1, so v_b(q) = U Π_j (2 + 2cos q_j). The kernel vanishes at q_j = π, which suppresses taste-changing transfers.
  - The onsite term is one-body and is dropped (normal ordering).
- **In d = 1, (b) = 2×(a)** up to a chemical potential.

## 1. Analytic

### 1a. One-particle structure (proved, elementary; checked)

- **Symbol.** In full-zone momentum p, h maps c_p → c_{p+πζ_j} with weight −sin p_j (ζ_j = ones in slots < j), and mass maps c_p → c_{p+π(1,…,1)}.
- **Reduced zone.** On k ∈ T_π^d with 2^d components A ∈ {0,1}^d (p = k + πA):
  - h(k) = Σ_j sin k_j Γ_j + m Γ_ε, with Γ's mutually anticommuting and squaring to 1;
  - h² = ω² with ω(k) = sqrt(Σ sin² k_j + m²);
  - bands ±ω, each 2^{d−1}-fold degenerate (spin × taste).
- **Taste corners.** All 2^d full-zone corners πA fold onto k = 0. The taste shift p_i → π − p_i leaves ω invariant.
- **Check.** The Bloch vectors used are eigenvectors of the real-space h to 4e-15 (`s1_natural_P.out`).

### 1b. The natural momentum (proved)

- P_j = ½{J_j, h} has one-particle symbol ½ sin 2p_j · 1. It is scalar, π-periodic, and has slope +1 at every one of the 2^d corners, so it is taste-universal.
- In real space it is P_j = Σ_x (c†_x c_{x+2e_j} − h.c.)/(4i): half the antisymmetrized translation by 2.
- [h, P_j] = 0 exactly (cluster: 0.0).

### 1c. Necessary condition with matrix charges (proved, standard; same form as K3a/L2)

- **Setup.** Write P = P0 + V P1 + … (a regular family analytic in V). The O(V) equation is [h, P1] + [H_int, P0] = 0.
- **Taking on-shell elements.** Take two-particle matrix elements between free states of equal energy. The empty-vacuum N = 2 sector is exactly invariant by number conservation. For a bounded P1 kernel, [h, P1] vanishes on shell.
- **Two consequences:**
  - P0's one-body part F(k) commutes with h(k), so F = F_+ ⊕ F_−, with F_± arbitrary 2^{d−1}×2^{d−1} matrix functions on D_±(k);
  - for every on-shell process (k1 σ1, k2 σ2) → (k3 σ3, k4 σ4) with k1+k2 ≡ k3+k4 (mod π) and Σσω conserved:
    (F3⊗1 + 1⊗F4) W = W (F1⊗1 + 1⊗F2).
- **What W is.** W is the antisymmetrized vertex between the degenerate band spaces, with the true form factors: W_d = Σ_{A's} U3*U4*U1U2 v(k3−k1+π(A3−A1)), restricted by A4 = A1⊕A2⊕A3, minus the exchange term.
  - Zero-amplitude channels give 0 = 0 rows automatically.
  - In this formulation only the diagonal blocks of F enter.
- **Hole branches.** Over the Dirac sea, e-e, h-h and e-h scattering are these same first-quantized processes between the ± bands, so both branches are included. Quasi-particle symbols differ from F only at O(V), through the Hartree–Fock term, so the O(V⁰) slope is unaffected.
- **Parity.** Inversion (c_x → ε(x)c_{−x}) is a symmetry of h and of both interactions. So every invariant splits into odd and even invariants. The slope term k_j·1 is odd, so searching the odd sector suffices.
- **Non-number-conserving P.** Averaging over the exact U(1) keeps the neutral part, and with it the one-particle action (referee L2, Finding 1).
- **Scope.** This is a necessary condition only (referee L2, Finding 1). It does not cover singular resonance-supported P1 kernels or charges non-analytic in V.

### 1d. Kinematics: only band-number-conserving channels are open (proved)

- ω is subadditive on the torus: |sin(a+b)| ≤ |sin a| + |sin b|, then Minkowski, then sqrt(x²+m²) is subadditive in x.
- A band-changing 2↔2 process (e.g. ++→+−) would need ω(k1+k2−k4) = ω1+ω2+ω4. That is impossible for m > 0. For m = 0 it is possible only on a measure-zero collinear set.
- **So the open channels are** ++→++, −−→−−, and +−→+− (both orderings): 6 of 16. The sampler hits exactly these 6 (`channels hit 6/16`; the deliberate band-changing sampling found 0).
- **By-product (even, irrelevant to momentum).** The band numbers N_± are Born invariants. Π_+ = (1+h/ω)/2 is exponentially local for m > 0.
  - It is not a trigonometric polynomial. That explains the third, exponentially decaying even singular value at m = 0.5 (0.42 → 0.25 → 0.058 → 0.0145 at R = 1, 4, 6, 8 in d = 2).
  - At m = 0 the decay is slow, because Π_+ is non-analytic at the cone.

### 1e. Reduction to the scalar problem, and the result

**(i) Symmetry averaging (proved; group structure checked).**
- The shift symmetries S_μ: c_x → ξ_μ(x) c_{x+μ}, with ξ_μ(x) = (−1)^{Σ_{ν>μ} x_ν}, commute with h at m = 0. At m ≠ 0 they map m → −m, so only the products S_μS_ν survive.
- Both interactions are invariant, because n_x → n_{x+μ}. The shifts preserve k.
- Averaging any collision invariant over the restricted group gives an invariant with the same averaged slope, since the slope s·1 is conjugation-invariant.

**(ii) Irreducibility on D_+(k), at generic k** (`s1_shift_schur.out`):

| Case | Commutant | Consequence |
|---|---|---|
| d = 2, m = 0 | dim 1 (irreducible) | F̄ is a scalar g(k) |
| d = 2, m > 0 | dim 2, commutative (two 1-dim Z-sectors from S1S2) | scalar g^a, g^b |
| d = 3, m = 0 | dim 2, commutative (two inequivalent irreps) | scalar per sector |
| d = 3, m > 0 | dim 4, non-commutative | a 2-dim irrep (spin) × multiplicity 2 (taste doublet); F̄ = 1 ⊗ f(k) with f a 2×2 taste matrix, so no scalar reduction |

**(iii) Scalar problem = the L2 lattice-KG problem, exactly (proved).**
- With k′ = 2k, ω² = m² + Σ sin²(k′_j/2) is the nearest-neighbour lattice Klein–Gordon band, and (mod π) conservation becomes (mod 2π) conservation.
- **Irreducible case (d = 2, m = 0).** The ++ channel is exactly the problem the L2 referee settled (Spohn: only aω + c for m > 0, d ≥ 2).
- **Sector cases (d = 2, m > 0; d = 3, m = 0).** The sector labels carry k-dependent phases (e.g. S1S2 → ±c·e^{i(k1+k2)}). So the sector-diagonal functions form one scalar function on a double-cover torus (argued). That function has the same KG-type band and conservation on the cover. Spohn's local functional-equation step gives aω + b·k + c on the cover, and periodicity on the cover kills b.
- **Either way,** the scalar function is aω + c. Its gradient at k = 0 is zero, so the slope is zero, which contradicts a nonzero universal slope.

**(iv) Conditions on the proof** (same family, unrefereed):
- Spohn's hypotheses for this band (recalled, as the L2 referee relied on them);
- the same-sector ++ amplitude is not identically zero:
  - **checked** for d = 2, m = 0.5, both interactions: with cover labels ±i, both sectors are nonzero on 800/800 sampled ++ processes (`s1_sector_amp.out`);
  - for d = 2, m = 0 the full W ≠ 0 on 100% of processes;
  - for d = 3, m = 0 it is argued only;
- for m = 0, the cone point k = 0 is excluded from Spohn's regular set (argued).

**(v) Status by case.**
- d = 2 (every m) and d = 3, m = 0: no local or exponentially quasi-local momentum with nonzero taste-universal slope (**proved** under (iv)).
- d = 3, m > 0: **checked only** (section 2).

**(vi) Special branches (proved).**
- The e-h flat branch (k,+),(−k,−) → (q,+),(−q,−) at K = 0, E = 0 constrains only even parts: an odd F with F_+ = F_− gives 0 = 0.
- Sampling also deliberately covered total reduced momentum K = (π/2,…), the analogue of the 1D K = π branch, and K = (π/2, 0, …).

### 1f. Discrete Z2 taste charges vs. additive momentum (proved)

- **Exact interacting symmetries:**
  - translations by 2, giving crystal momentum mod π (group-valued, e^{2iK_j});
  - the shift group (m = 0) or its even subgroup (m ≠ 0). Modulo translations it is finite, and its eigenvalues are multiplicative Z2/Z4-type taste labels.
- These are exact. They are not additive densities with a slope: their logarithms are not local, so they cannot feed the shift constraint.
- The additive version, the per-sector number N_a − N_b, is not expected to be conserved, because aa → bb is symmetry-allowed (only the product of labels is conserved). This was **not checked directly**: its projector contains Π_+, so it would sit among the slowly decaying even singular values, not in the exact null space {N, H0}. It is even, so it is irrelevant to momentum anyway.
- This matches the supervisor's "Z2 taste charges, not additive momentum".

## 2. Numerics: sampled finite-basis null spaces (checked)

**Method** (`s1_matrix_collision.py`, `s1_run*.py`):
- **Basis.** Every one-body operator invariant under translation by 2 with |r|_∞ ≤ R: O_{B,r} = Σ_x e^{iπB·x} c†_x c_{x+r}. These are full 2^d×2^d matrix symbols, covering every taste and band structure.
- **Parity.** The basis is split by inversion (c_x → ε(x) c_{−x}, a symmetry of h and of both interactions), and the odd sector is searched.
- **Quotient.** The basis is quotiented by the kernel of F ↦ (diagonal blocks). This covers every F commuting with h, and also every exp-local C(F) = (F + hFh/ω²)/2 at m > 0.
- **Linear algebra.** Collision rows are D⁴ per process (D = 2^{d−1}), solved by TSQR then SVD.
- **Tolerance.** Nullity counts sv < 1e-8 (absolute) + 1e-9·sv_max (relative), which addresses the L2 referee's relative-only problem.
- **Sampling.** Processes are random on-shell processes in all open channels, plus deliberate K = 0, K = (π/2,…) and K = (π/2,0,…) branches. Energy residuals are ≤ 2.4e-15.
- **Vertex check.** W was checked against a direct real-space sum to ≤ 4.4e-15 (`s1_vertex_check.out`).

**Results.** "Ratio" is the smallest nonzero sv divided by sv_max.

| Case | R range | Odd nullity | Ratio at largest R | Smallest odd sv vs R | Even nullity |
|---|---|---|---|---|---|
| d=2 nn m=0.5 | 1–8 | **0** | 0.27 | 7.47, 7.40 (R=6, 8): flat | 2 (N, H0) |
| d=2 nn m=0 | 1–8 | **0** | 0.27 | 7.48, 6.94: flat | 2 |
| d=2 cube m=0.5 | 1–8 | **0** | 0.29 | 19.8, 19.2: flat | 2 |
| d=2 cube m=0 | 1–8 | **0** | 0.30 | 19.9, 19.2: flat | 2 |
| d=2 nn m=0.5, fresh seed 99 | 8 | **0** | 0.27 | — | 2 |
| d=3 nn m=0.5 | 1–4 | **0** | 0.17 (R=4) | 19.7, 19.8, 17.4, 17.9 | 2 (R ≤ 4) |
| d=3 cube m=0.5 | 1–3; R=4 odd (seed 55) | **0** | 0.19 (R=3), 0.17 (R=4) | 108, 118, 101, 104 | 2 (R ≤ 3) |
| d=3 cube m=0 | 1–3 | **0** | 0.20 | 103, 106, 99 | 2 |
| d=3 nn m=0 | 1–4 | **0** | 0.14 (R=4) | 19.3, 18.0, 17.3, 14.3 | 2 (R ≤ 3) |
| d=3 nn m=0.5, fresh seed 44 | 1–3 | **0** | 0.20 | 19.6, 19.6, 17.2 | 2 |

- The matrix (taste-doublet) case d = 3, m > 0 is covered here, and here only.
- **Smallest odd sv vs R:** it stays flat as R grows. That suggests a uniform ℓ² floor, i.e. no quasi-local odd invariant either. This is a trend, not a bound.
- **Even nullity:** exactly 2 everywhere (number and free energy), with null singular values ≤ 2.5e-12 against sv_max of 10–500. This is the positive control that the code finds true invariants with the absolute tolerance.

**Controls:**
- **Free (v ≡ 0):** every odd symbol passes (nullity 32 of 32, d = 2, R = 2).
- **1D massless.** This is the XXZ chain under Jordan–Wigner, so it is integrable.
  - Odd nullity is 1, 2, 4, 8 at R = 2, 4, 8, 16: the expected extra invariants, found with the absolute tolerance.
  - 89% of sampled reduced-zone resonances have W = 0 exactly (full-zone momentum conservation). The matrix formulation drops them automatically.
- **1D massive** (staggered field, non-integrable): odd nullity 0 at every R (R ≤ 16), ratio ≥ 0.12.
- **The natural P_x = ½ sin 2k_x directly** (`s1_natural_P.out`):
  - every nonzero-amplitude process violates it;
  - W-weighted rms defect is 0.49–0.59 on generic processes;
  - on ee→ee with in-states |k| < 0.35, the defect is 0.012–0.021 (an O(k³) lattice effect), and still 99–100% of processes violate it.

## 3. Exact cluster check (checked; `s1_cluster_ed.out`)

**Setup.**
- 2D PBC clusters; dense ED in the N-particle sector.
- Lx = 6 is required: on Lx = 4, ½ sin 2p ≡ 0 on the allowed momenta.
- P = P_x natural, as in 1b.

**Results:**
- ||[H, P]||_op is exactly linear in V: 0.612·V for nn, N = 2; 1.061·V for N = 3; 4.42·V for cube, N = 3 on 6×4. It is 0.0 at V = 0.
- **The O(V) on-shell part ||Π_E[H_int, P]Π_E||** (degenerate free levels; no dressing P1, local or not, can cancel it):
  - zero on 6×4, where the grid is too coarse to give resonances;
  - **0.204 (op), with Frobenius 1.28 of 5.20, on 6×6 with N = 2, m = 0.5.**
- **HS distance from P to the commutant of H (the nearest exactly conserved operator), as V → 0:**

| Cluster | dist / ‖P‖ as V → 0 |
|---|---|
| 6×6, N=2, nn, m=0.5 | **0.677** (V = 1e-3 … 0.05) |
| 6×4, N=3, nn, m=0.5 | 0.50–0.53 |
| 6×4, N=3, nn, m=0 | 0.37 |
| 6×4, N=3, cube, m=0.5 | 0.52 |
| 6×4, N=2 | → 0 linearly (finite-size: no resonances) |
| Control: free energy H0, every case | → 0 linearly (e.g. 1.85e-4 at V = 1e-3) |

- **Reading.** On clusters with resonances, the natural momentum is not adiabatically connected to any conserved operator. On 6×6 this is first order; on 6×4 with N = 3 it is higher order.
- **Limitation.** A finite cluster cannot exclude every local P. This check is supporting evidence, not the decisive leg.

## 4. Stress, first class, G, γ

Not applicable: no passer.

## Against the registered expectation

- **Expected FAIL (bounded) for S1: confirmed.**
- **Refinements:**
  - Matrix charges add **no** odd invariant at all in the tested range, not even on degenerate submanifolds. The degenerate e-h K = 0 branch constrains only even parts.
  - The scalar part is **exactly** the L2 lattice-KG problem under k′ = 2k.
  - Kinematics close every band-changing channel.
  - The only non-scalar residue is the d = 3 massive taste doublet. It is closed numerically, not analytically.
- **The price is unchanged:** "non-local momentum, or an exact lattice momentum not in the axioms".

## Labels and strong words

- **Proved (same family, unrefereed):**
  - 1a, 1b, 1c (necessary only), 1d, and the exact symmetries in 1f;
  - the exact KG mapping, 1e(iii);
  - the scalar reduction and FAIL for d = 2 (all m) and d = 3, m = 0, conditional on 1e(iv).
- **Checked:**
  - the null spaces (sampled, finite basis, R ≤ 8 in d = 2, R ≤ 4 in d = 3), with singular-gap ratios 0.14–0.31;
  - the shift-group commutant dimensions;
  - the same-sector amplitudes for d = 2, m = 0.5;
  - the vertex against real space;
  - the 1D and free controls;
  - the cluster ED numbers.
- **Argued:** the m = 0 cone exclusion in Spohn's argument; the double-cover labelling of sectors; that the same-sector amplitude is generically nonzero for d = 3, m = 0 (checked for d = 2, m = 0.5).
- **Suggested:**
  - a uniform odd floor, from the flat smallest sv;
  - exact-in-V statements: the exact T(E) has finite-rank form factors and is nonzero wherever W is, for small V. Not computed.
- **Not covered:**
  - non-perturbative V;
  - charges with zero one-particle action;
  - gauge-mediated interactions (S2);
  - non-number-conserving or higher-body-leading interactions;
  - an analytic proof for d = 3, m > 0;
  - range beyond R = 8 (d = 2) or 4 (d = 3) except via the d = 2 and d = 3, m = 0 proof;
  - the referee-flagged regularity of the C¹ step (the L2 repair applies).
- **Strong words used:**
  - "exact" only for operator identities, and for the KG mapping, which is an identity;
  - "proved" only with its stated conditions;
  - "no invariant" for numerics always means "in the sampled finite basis".
