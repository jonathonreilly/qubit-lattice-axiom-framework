# C5 TW-1 report: can a twin be the antiparticle? (reduced/Majorana staggered halving, field by field)

- **Worker:** Claude Opus 5.5 probe, the same model family as the supervisor and every C5 worker. Unrefereed. Run 2026-10-14, 12:56Z to about 13:35Z.
- **Hygiene:** no repository file was edited. The only downloads were web pages read through the fetch tool; nothing was saved or executed. OMP_NUM_THREADS=2 and one process at a time.
  - Peak resident memory per run: `tw1_alg` 496 MB, `tw1_sigma` N = 64 427 MB, N = 48 242 MB, N ≤ 32 ≤ 160 MB, `tw1_count` negligible. The `tw1_alg` peak is just under the 0.5 GB cap.
  - No process of mine is still running. The `tw2_*` processes that are running belong to the TW-2 probe.
- **Item:** `TESTS:9611-9631`, which is `.claude/science/exercises/gravity-current-state-20261009/TESTS.md`. The shared setting is at `:9613-9617`, the FIXED readings at `:9626-9630`, and the expectation at `:9631`.
- **Paths.**
  - `S/` = `scratchpad/C5/TW1/scripts/`.
  - `P/` = `.claude/science/exercises/gravity-current-state-20261009/`.
  - `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`.
  - `main:` = a file read with `git show origin/main:<path>`.
- **Read:**
  - `AX`, in full;
  - `TESTS:9146-9658`, including NF-1 `:9448-9513` and its referee record `:9578-9585`;
  - `P/agents/C5_NF1_report.md` and `C5_NF1_referee_verdict.md`, both in full;
  - `P/agents/panel_F/SYNTHESIS.md`, in full;
  - `scripts/C5/NF1/` (nf1_alg, nf1_poslib, nf1_sigma8, nf1_pstag and their outputs).
  - **The coordinator's prior-art list:**
    - main:docs/CHIRALITY_GATE_IS_TWO_INDEPENDENT_GATES_…_2026-06-08.md
    - main:docs/CHIRAL_CONTENT_IS_THE_EPSILON_D_CHIRALITY_IMPORT_…_2026-06-08.md
    - main:docs/CHIRALITY_SEPARATE_FACTOR_DIRAC_MASS_ALGEBRA_SUPPORT_BOUNDED_NOTE_2026-06-08.md
    - main:docs/AXIOM_FIRST_SM_ANOMALY_CANCELLATION_COMPLETE_THEOREM_NOTE_2026-05-03.md
    - main:docs/A3_ROUTE3_ANOMALY_INFLOW_BOUNDED_OBSTRUCTION_NOTE_2026-05-08_r3.md
    - main:.claude/science/physics-loops/staggered-dirac-a1a2-realization-closure-20260710/{NO_GO_LEDGER,LITERATURE_BRIDGES}.md
    - main:docs/THE_GENERATION_COUNT_IS_THE_SPATIAL_DIMENSION_…_2026-09-03.md
  - **From a filename sweep** (`chiral|staggered|majorana|grassmann|kahler`, 751 hits):
    - COMPOSITE_SITES_GIVE_THE_CARVED_MAJORANAS_…_2026-09-24.md
    - A_RECORD_NATIVE_STAGGERED_MASS_GAP_…_2026-09-03.md (head)
    - NEUTRINO_MAJORANA_CURRENT_STACK_ZERO_LAW_NOTE.md and NEUTRINO_MAJORANA_NATIVE_GAUSSIAN_NO_GO_NOTE.md (heads)
    - FREE_FIELD_LATTICE_TO_CONTINUUM_GAUSSIAN_MEASURE_BOUNDED_NOTE_2026-05-30.md §3
- **Labels:**
  - proved: a complete short argument, unrefereed;
  - checked: numerics run here;
  - suggested;
  - reading;
  - comparator: literature, cited.
  - RECALLED marks something taken from memory.

## 0. Plain words, and the reading

1. **For charged particles the answer is no.**
   - NF-1's twin carries exactly the same charges as the original.
   - An antiparticle carries the opposite charges, and each Dirac twin already contains its own antiparticle.
   - With continuous time, a one-mode-per-site field can be cut in half while keeping the gauge charges exact only if the particle's charge representation is *real*. A real representation is one where particle and antiparticle carry the same kind of charge (proved by Schur's lemma, §3a).
   - Every quark and charged lepton fails this, because of hypercharge and colour.
   - SU(2) doublets also fail, contrary to the expectation. Their representation is "pseudo-real", and a pseudo-real field can only be cut in half in pairs. A pair halved is just one ordinary field again, so nothing is gained (checked).
2. **For neutral particles the answer is yes.**
   - A field with no gauge charge (a right-handed neutrino) or in a real representation can be halved. One "reduced" staggered field is then exactly one Dirac fermion, whose second taste *is* its antiparticle.
   - The strain zero survives the halving. The two protecting symmetries (renamed Θ_M and P_stag) still hold, and the self-energy is zero to ≤ 6e-18 at every strain (checked).
   - Two controls, each breaking one symmetry, bring the mass back: 2.4e-2 and 2.9e-2 e²C_F, with strain Hessians of about −1e-3 to −1e-2 (checked).
3. **What a halved field cannot do.**
   - It has no lattice-symmetric mass term. All six possible mass terms are forbidden by Θ_M or by P_stag, and none is cubic-invariant (checked).
   - So a halved ν_R stays massless unless something breaks a symmetry or interactions gap it (TW-3).
4. **Grouping the SM.**
   - Under the full SM gauge group, no grouping of 1–4 generations (with or without ν_R) fits staggered fields without leftovers. Adding one mirror generation per generation works only for an even number of generations (2 + 2 mirror, 4 + 4 mirror), and then the "halved" form is identical to the unhalved one (checked; proved).
   - Factor by factor:
     - under SU(3) alone, or SU(2) alone, one generation with ν_R fits exactly: the twins are absorbed by conjugate partners already present, and the singlets are halved;
     - U(1)_Y blocks it;
     - so does SU(3)×SU(2) together.
5. **Worker reading: HALVE-PARTIAL** (§4), with corrections to the expectation.
   - SU(2) doublets are not halved. They pass only factor by factor, by pairing.
   - U(1)_Y is the blocking factor.
   - The full SM needs named extra content: mirror families, and an even family count.
   - The only genuine halving is for real-representation (neutral) fields.

## 1. Class, hypotheses and choices

- **Arena.**
  - Z³ × ℝ (continuous time), Hamiltonian Fock space with a CAR algebra on each site.
  - The staggered law h = Σ_j η_j(x) S_j, with symbol s = SymS(0.909103708) and r = 0 (`TESTS:9614`).
  - The registered SF strain, the separable flow of E² = Σ s².
  - Psym links (`TESTS:9615`).
- **Reduction (definition used).** A *halving* is a local, gauge-covariant sub-system that keeps half of the Majorana operators at every site and is closed under the dynamics.
- **Gauge content.** I use the SM group G_SM = SU(3)×SU(2)×U(1)_Y in the left-handed Weyl frame. I also report the unbroken SU(3)×U(1)_em, the vector-like content that the C5 root actually builds (U(1) photon plus C_F).
- **Strain checks.** These use a real-representation stand-in gauge group: SO(3) links in position space, and an SO(N)-vector group factor C_F at one loop. No SM field is in a real non-singlet representation, so this is the only way to test the strain zero on a *charged* reduced field.
- **Not computed:**
  - two loops;
  - Yukawa and Higgs couplings of a reduced ν_R;
  - chiral electroweak vertices (absent on both edges, as in NF-1);
  - non-uniform strain;
  - the multiplicative channel of the reduced field;
  - observational limits on mirror families.

## 2. Prior art (counted once)

- **NF-1 and its referee.**
  - The 2-Dirac taste count, Θ and P_stag, and Σ(0,0) = 0 (`C5_NF1_report.md:115-153,202-210`; `C5_NF1_referee_verdict.md:5-13`).
  - U(1)_ε is absent with continuous time (NF-1 L2, `:124-127`). The same fact kills the 4D even/odd reduction here (§3a).
  - T2, tastes as generations (`:218-229`). This reappears below as the SU(3)×U(1)_em "2 gen" match.
- **The two Dirac flavours of a 3D KS field** were already on main: main:docs/A_RECORD_NATIVE_STAGGERED_MASS_GAP_…_2026-09-03.md, claim scope T4 ("two Dirac flavors, fourfold spin/flavor bands").
- **Main's chirality lane** (CHIRALITY_GATE_…, CHIRAL_CONTENT_…, CHIRALITY_SEPARATE_FACTOR_…).
  - ε, the qubit pseudoscalar and generation handedness are distinct data. The ε grading supplies a grading, not a chiral gauging selection (CHIRAL_CONTENT_…:39-42).
  - TW-1 is consistent with this. The reduction uses ε (through Θ_M) only as a protecting symmetry, and does not touch chirality or gauging.
- **Main's anomaly note** includes ν_R in the retained content (main:docs/AXIOM_FIRST_SM_ANOMALY_CANCELLATION_COMPLETE_THEOREM_NOTE_2026-05-03.md:6,26). That is why ν_R counts as an SM field for the reading.
- **Main's generation lane** (main:docs/THE_GENERATION_COUNT_IS_THE_SPATIAL_DIMENSION_…_2026-09-03.md §1-2).
  - It splits the 8 corners by Hamming weight (1+3+3+1) with the Wilson/K0 operator M_W = dI − H_K0/2. That is a different decomposition of the same 8 corners from NF-1's 4 ⊗ 2.
  - **New here (proved; checked `tw1_alg.out:21`):** M_W is real symmetric, so its quadratic form on a Majorana field is a constant. The hw-splitting operator therefore does not exist on a reduced field, and that reading has no carrier there.
- **Main's neutrino-Majorana lane.**
  - μ_current = 0 by exact fermion-number U(1) (main:docs/NEUTRINO_MAJORANA_CURRENT_STACK_ZERO_LAW_NOTE.md:24,34).
  - A reduced field has no fermion-number U(1). Instead, Θ_M, P_stag and cubic symmetry forbid every gap-opening Majorana bilinear (§3a). So the reduced route does not supply a ν_R Majorana mass either (suggested; count with that lane).
- **Staggered-Dirac a1a2 packet.**
  - NO_GO_LEDGER: the minimal axioms do not select a staggered kinetic law (`NO_GO_LEDGER.md:7-12`). TW-1, like NF-1, *supplies* the staggered edge; nothing here selects it.
  - LITERATURE_BRIDGES: no literature is load-bearing (`:3-9`).
- **Carved-Majorana notes** (main:docs/COMPOSITE_SITES_…_2026-09-24.md:23-34). These are a different construction: Majoranas from spins, with a bare-bilinear projection obstruction. They are not used here.
- **Comparators (literature):**
  - **Reduced staggered fermions:** C. van den Doel and J. Smit, *Nucl. Phys. B* 228 (1983) 122.
  - **4D Euclidean reduced action:** ψ̄ on one parity, ψ on the other, ψ̄ relabelled as ψᵀ. For SU(2) fundamentals, pseudoreality makes the measure positive; it gives 2 continuum Dirac fermions in place of 4 (S. Catterall and N. Butt, *Phys. Rev. D* 99, 014505 (2019), arXiv:1810.00853).
  - **Reduced staggered fields with four-fermion gapping:** Catterall, arXiv:1510.04153 (3D, SO(4)); Butt, Catterall and Schaich, *Phys. Rev. D* 98, 114514 (2018), arXiv:1810.06117.
  - **Reduced Kähler–Dirac fields with mirror fermions** gapped by 't Hooft-consistent Yukawas, whose light sector is Pati–Salam: Catterall, *SciPost Phys.* 16, 108 (2024), arXiv:2311.02487; also arXiv:2010.02290.
  - **Reality of SM and GUT representations:** R. Slansky, *Phys. Rep.* 79 (1981) 1 (RECALLED; standard).

## 3. Results

### 3(a) The reduced field in continuous time, and its count

**R1. When a halving exists (proved; checked).**
- Each site carries complex fermions χ^a_x in the gauge representation R (complex dimension d), which is 2d Majoranas transforming in the realification R_ℝ.
- Gauge transformations act independently at each site. So a gauge-covariant local halving must keep, at every site, a G-invariant real subspace of R_ℝ of real dimension d.
- For irreducible R this exists iff R is **real** (Frobenius–Schur +1):
  - complex and pseudo-real R_ℝ are irreducible over ℝ (Schur);
  - for real R, R_ℝ = R₀ ⊕ iR₀.
- Checked by real commutants (`tw1_alg.out:31-35`):

| representation | real commutant | halving |
|---|---|---|
| SU(2) doublet | dim 4 (quaternions) | none |
| SU(3) triplet | ℂ | none |
| U(1) charge 1 | ℂ | none |
| SO(3) triplet | M₂(ℝ), rank-3 projector | exists |
| two SU(2) doublets | — | exists, giving one complex doublet: no gain |

- This holds for any sublattice pattern, including keeping ξ₁ on even sites and ξ₂ on odd sites.

**R2. The reduced law (proved; checked).**
- The root's odd symbol makes h purely imaginary, h = iB with B real antisymmetric. This holds at t = 0 and under SF strain, and with real SO(3) link matrices on straight and Psym paths (`tw1_alg.out:24-29`).
- Then Σ χ†hχ = (i/2)(ξ₁ᵀBξ₁ + ξ₂ᵀBξ₂) + const (Fock identity, 4.4e-16, `:22`).
- Control: a charged, complex h mixes the two copies (`:23`).
- **The reduced field** is H_M = (i/2) Σ ξ_x B_xy ξ_y, with one Majorana per site per real component.

**Count (proved by counting).**
- At K = 0 the 8 corner modes are real (−πn ≡ πn).
- One reduced field in a real R₀ is 8 real corner components = 2 Weyl = **1 Dirac = 2 Majorana in R₀**. That is half of NF-1's 2 Dirac. The second taste is the charge conjugate of the first.

**Correction to the pre-registration** (`TESTS:9620`: "real or pseudo-real").
- Pseudo-real does not reduce in continuous time. With SU(2) links, (iσ₂)K anticommutes with h[U] and squares to −1 (`:30`). That is a symplectic structure: a Majorana condition needs pairs.
- The 4D reduced fermions that *do* work for SU(2) (Catterall–Butt, comparator) use the even/odd decoupling of a discrete-time action. The on-site χ̄∂_τχ of continuous time couples χ̄_e to χ_e. This is the same fact that kills U(1)_ε (NF-1 L2) (proved).
- Even there the reduced field is 2 Dirac in R (comparator), the same as the unreduced continuous-time field. So moving to discrete time would buy nothing for complex or pseudo-real fields (suggested).

**Majorana-legal bilinears** (`tw1_alg.out:15-21`, proved; checked).
- Of the 28 hermitian antisymmetric constant 8×8 bilinears, Θ_M allows 16 and P_stag (at K = 0) allows 12. **None is allowed by both.**
- Two familiar terms are absent from any Majorana field, because both are real symmetric and their quadratic forms are constants: the staggered mass Γ_ε and the Wilson M_W.
- There are 6 gap-opening masses:
  - iΓ_εJ_a, which are Θ_M-odd;
  - iG₅J_a, which are P_stag-odd.
  - Here G₅ = Γ_εΓ₁Γ₂Γ₃, and J_a = Z_iZ_j is a product of two shift symmetries at K = 0 (`:9-14`).
- iΓ_εJ₁₂ is a local two-link operator iε(S₁S₂ − (S₁S₂)ᵀ)/2, with reduced-zone symbol cos(K₁+K₂)·iΓ_εJ₁₂ (`:36-42`).
- **Cubic symmetry.** Both mass triplets rotate as cubic vectors (`:47-61`). No combination is cubic-invariant (`:62`). The only 2 cubic-invariant Majorana-legal bilinears are not gap-opening, and both are P_stag-odd (`:63-65`).
- Hence **a single reduced field has no lattice-symmetric bilinear mass** (checked for the K = 0 part).

### 3(b) Reality type per field (comparator; tabulated in `tw1_count.out:1-10`)

| field (LH Weyl) | SU(3) | SU(2) | U(1)_Y | G_SM |
|---|---|---|---|---|
| Q (3,2,1/6) | complex | pseudo-real | complex | complex |
| u^c (3̄,1,−2/3) | complex | real | complex | complex |
| d^c (3̄,1,1/3) | complex | real | complex | complex |
| L (1,2,−1/2) | real | pseudo-real | complex | complex |
| e^c (1,1,1) | real | real | complex | complex |
| ν^c (1,1,0) | real | real | real | **real** |

- **Embeddings:** SU(5) 5̄ and 10 are complex. SO(10) 16 is complex (a Spin(10) spinor, 10 ≡ 2 mod 8). Pati–Salam (4,2,1) and (4̄,1,2) are complex. 16 ⊕ 16̄ is real.
- **Under the unbroken SU(3)×U(1)_em:** ν_L and ν^c are real (neutral); every charged fermion is complex.

### 3(c) The strain zero on the reduced field (proved; checked)

**Symmetries.**
- **Θ_M** is antiunitary: ξ → εξ together with K. With real links it acts as E → −E on the gauge field.
- **P_stag** is ξ(x) → ε_x ξ(−x), with the link lift O^P_j(x) = O_j(−x−e_j)ᵀ.
- Both hold with random SO(3) links at t = 0 and 0.3: εBε = −B to 0, and P h P^T = h[O^P] to 3e-16 (`tw1_alg.out:26-29`).

**Theorem.** NF-1's argument carries over: Θ_M forces Σ_M(0,0) to anticommute with Γ_ε, and P_stag forces it to commute. So Σ_M(0,0) = 0 at every uniform strain and every perturbative order.
- This carries the NF-1 referee's caveats: the link lift must be inversion-covariant, and the regulator must respect the symmetries (`C5_NF1_referee_verdict.md:7`).

**One loop.**
- A complex field in a real representation is two decoupled Majorana copies (R2). So per copy Σ_M = C_F(R₀) × NF-1's U(1) Σ with e = 1 (proved).
- This is evaluated with NF-1's direct 8×8 evaluator, copied unchanged, on full-BZ midpoint grids N = 24, 32, 48 and 64.
- Folding covariance and Majorana-legality of every law used are checked to ≤ 3e-15 (`tw1_sigma_N64.out:2-4`).

| case | quantity | N = 32 / 48 / 64 | source |
|---|---|---|---|
| **A, reduced law**, E_g t ∈ {0, ±0.1, 0.2} | max \|Σ(0)\|, all 64 entries | ≤ 6.2e-18 at every N | `tw1_sigma_N{24,32,48,64}.out:7-10` |
| A | Majorana-illegal symmetric part (consistency) | ≤ 6e-18 | same |
| **B control**, Θ_M broken, P_stag kept: r_c cos(k₁+k₂)Σsin²k·iΓ_εJ₁₂ | δm(0) (iΓ_εJ₁₂ channel), r_c = 0.1 / 0.3 | +2.3558e-2, +2.3573e-2, **+2.3578e-2** / +7.0493e-2, +7.0539e-2, **+7.0554e-2** | `_N64.out:18,25` |
| B | Hess_t (d = 0.05), r_c = 0.1 / 0.3 | −2.08e-3, −4.10e-3, −3.16e-3 / −6.32e-3, −1.24e-2, −9.58e-3 | `_N32/48/64.out` |
| **C control**, P_stag broken, Θ_M kept: r_c cos k₃ Σsin²k·iG₅J₁₂ | δm(0) (iG₅J₁₂), r_c = 0.1 / 0.3 | +2.8831e-2, +2.8847e-2, **+2.8852e-2** / +8.6119e-2, +8.6166e-2, **+8.6181e-2** | `_N64.out:33,40` |
| C | Hess_t (d = 0.05), r_c = 0.1 / 0.3 | −0.84e-3, −3.80e-3, −2.38e-3 / −3.77e-3, −1.26e-2, −8.37e-3 | same |

- All units are per e²C_F.
- The control masses are converged to 4 digits.
- The control Hessians are **not converged** on midpoint grids. They are negative and ≥ 8e-4 in magnitude at every grid.
- **New relative to NF-1:** each symmetry alone is needed. Breaking only P_stag (control C) also re-admits a mass. NF-1's controls broke Θ only.

### 3(d) Groupings (proved by counting; tabulated in `tw1_count.out:11-51`)

**Building blocks.**
- A complex field in R gives 2R + 2R̄ (LH Weyl).
- A reduced field in a real R₀ gives 2R₀.
- So content matches with no leftovers iff:
  - complex R has mult(R) = mult(R̄), and even;
  - pseudo-real R has mult ≡ 0 mod 4;
  - real R has even mult.

**Lemma (proved).** Any real representation that contains a complex F also contains F̄. Hence every G_SM-exact reduced form needs mirror content. For F ⊕ F̄ the reduced field in F_ℝ *is* the complex field in F (realification), so there is no halving gain.

| gauge group | content | result |
|---|---|---|
| **G_SM** | 1, 2, 3 or 4 generations, with or without ν_R | **fails**: Q, u^c, d^c, L, e^c have no conjugate partners |
| G_SM | n gen + ν_R + n mirror gen | **matches only for even n** (2+2 yes; 1+1 and 3+3 no) |
| SU(3)×SU(2) | any of the above | fails ((3,2) complex; L doublet count) |
| **SU(3) alone** | 1 gen + ν_R (and 2, 3, 4 gen + ν_R) | **matches**: triplets 2 vs antitriplets 2; singlets 4 → 2 reduced fields |
| SU(3) alone | no ν_R | fails (odd singlet count: 3 per gen, 9 for 3 gen) |
| **SU(2) alone** | 1 gen + ν_R (and 2, 3, 4) | **matches**: 4 doublets → 1 complex field; 8 singlets → 4 reduced fields |
| SU(2) alone | no ν_R | fails (7 singlets per gen, 21 for 3 gen) |
| **U(1)_Y alone** | any | **fails** (Y = 1/6 has 6 copies per gen and Y = −1/6 has none) |
| SU(3)×U(1)_em (root's vector content) | 2 gen + 2 ν_R | matches (NF-1's T2, counted once) |
| SU(3)×U(1)_em | 1 or 3 gen | fails (odd) |
| SU(3)×U(1)_em, neutral sector | ν_L, ν^c | 2 per gen → 1 reduced field per gen (genuine halving); 1.5 per gen without ν_R |
| SO(10), Pati–Salam | 16; (4,2,1) ⊕ (4̄,1,2) | complex: no reduced form without 16̄. This matches Catterall's 4D route, which adds mirrors and gaps them by interactions (comparator) |

## 4. Against the FIXED readings (`TESTS:9626-9630`), literal first

| reading | clause | status |
|---|---|---|
| HALVE-WORKS | a reduced gauge-invariant form for the full SM content, with the strain zero kept | **no.** No charged SM fermion admits a reduced form under G_SM (R1, §3d) |
| **HALVE-PARTIAL** | "works for some factors only (name which)" | **met.** Factor by factor, SU(3) alone and SU(2) alone match one generation with ν_R (pairing plus halved singlets). U(1)_Y fails for every charged field, and SU(3)×SU(2) jointly fails on Q. The *halving proper* acts only on real representations: factor-singlets, and under G_SM only ν^c |
| | "or needs an embedding/extra content (name it)" | **met.** SO(10) and Pati–Salam do not help (16 is complex). The extra content needed is **one mirror family per family plus an even family count**: over the SM's 3, that means 4 gen + 4 mirror gen with ν_R. In that case the reduced form equals the complex form (no count gain) |
| HALVE-FAILS | "no SM field admits it" | **no.** ν^c admits it, and ν_R is retained SM content on main (anomaly note `:6,26`). True only for the minimal SM without ν_R |
| | "or the reduction destroys the strain zero" | **no.** Θ_M and P_stag survive; Σ_M(0,0) ≤ 6e-18; controls B and C are nonzero |
| OPEN | otherwise | not met |

- **Worker reading: HALVE-PARTIAL.** The strain zero is kept wherever the reduced form exists.
- **Flagged for the referee:**
  1. If "works for some factors" is held to mean that the *halving proper* acts on a non-singlet of some factor, the first disjunct fails. No SM fermion sits in a real non-singlet representation. The reading would then rest on the second disjunct (mirror content) alone, where the reduced form exists but gives no halving gain.
  2. If ν_R is excluded from "SM fields", HALVE-FAILS's first clause holds literally.

## 5. Against the expectation (`TESTS:9631`)

- **"HALVE-PARTIAL": borne out, with the content of the "partial" changed.**
  - "**SU(2) doublets yes**": **no.** Pseudo-real fields cannot be halved in continuous time (R1; `tw1_alg.out:30-31,35`). Doublets pass only factor-wise, by pairing: 4 doublets per generation form one complex field.
  - "**U(1)_Y and colour triplets no**": U(1)_Y yes, it blocks. Colour triplets pass factor-wise (SU(3) alone matches by pairing) but fail jointly with SU(2) or U(1)_Y.
  - "**unless paired with its mirror**": the mirror is necessary (Lemma) but not sufficient. An even family count is also needed, and the reduced form then equals the unreduced one.
- **Not anticipated:**
  - The pre-registration's "real or pseudo-real" premise is wrong for continuous time. The 4D reduced fermions rely on discrete-time even/odd decoupling.
  - A reduced field has no lattice-symmetric bilinear mass at all: 6 candidates, each Θ_M- or P_stag-odd, and all cubic vectors.
  - Main's Wilson/K0 hw-splitting operator vanishes identically on a reduced field.
  - Both symmetries are separately necessary (control C).

## 6. Strong words

- **"Proved"** (short, unrefereed): R1; R2; the count; the Lemma; the reality table (standard group theory); the theorem in §3(c) under NF-1's caveats; the one-loop group-factor identity; the M_W and Γ_ε vanishing on Majorana fields; the continuous-time obstruction to the 4D even/odd reduction.
- **"Checked":** every number in `tw1_alg.out`, `tw1_sigma_N*.out` and `tw1_count.out`.
- **"Every strain":** uniform strain only.
- **"Every order":** perturbative, with a symmetry-respecting regulator and lift.
- **The strain test of a charged reduced field** uses an SO(N) stand-in. No SM field is in a real non-singlet representation.
- **Not claimed:**
  - two loops;
  - the reduced field's multiplicative channel;
  - Yukawa/Higgs couplings of a reduced ν_R;
  - that mirror families are observationally allowed;
  - that interactions can gap mirrors symmetrically (TW-3);
  - chiral electroweak couplings;
  - non-uniform strain;
  - convergence of the control Hessians.

## 7. Prices (named, not adopted; no axiom text changes)

- **P-TW1a: mirror families with an even family count.** SM + ν_R ⊕ one mirror family per family, with 4 + 4 families over the SM's 3.
  - All charges are exact and the strain zero is kept.
  - It requires the mirrors to be gapped without Θ_M- or P_stag-breaking bilinears. That is SMG; it goes to TW-3 and the chirality exercise.
  - Mirror and 4th-family observational status is not computed. LHC vector-like and 4th-generation limits are RECALLED as constraining.
  - It overlaps NF-1's P-NF1a, the T2 content: count once.
- **P-TW1b: reduced (Majorana) staggered fields for real-representation content only.**
  - This is ν_R under G_SM; under the root's present vector-like group it is also ν_L.
  - It halves the count and keeps the strain zero.
  - Needs: a 4th sterile Weyl if 3 ν_R are to be paired; and no symmetric bilinear mass, so a mass must come from interactions or from explicit Θ_M/P_stag/cubic breaking, which reopens the channel (controls B and C).
- **No arena price helps.** Discrete staggered time (the 4D reduced route) leaves complex and pseudo-real fields at 2 Dirac per field (comparator; suggested).

## 8. Files (`S/`)

- `tw1_alg.py` → `tw1_alg.out` / `.time`: reduced-zone algebra, the J's from the shift symmetries, Majorana-legal bilinears, the Fock identity, SO(3) and SU(2) position-space checks, commutants, locality of the J-mass, and cubic rotations.
- `tw1_sigma.py` → `tw1_sigma_N{24,32,48,64}.out` / `.time`: one-loop Σ_M(0,0) for the reduced law and controls B and C. The sigma8 function is copied from `scripts/C5/NF1/nf1_sigma8.py`.
- `tw1_count.py` → `tw1_count.out`: reality types and the grouping and count matching.
- Copies, with imports repointed to `../flat` only: `f1_lib.py`, `f3_lib.py`, `f3_dirac.py`, `nf1_poslib.py`, `nf1_gammas.npy`, `nf1_dict.npy`; and `../flat/*.py` from NF-1.
- `../prior/`: prior-art notes from origin/main, saved for reading.
