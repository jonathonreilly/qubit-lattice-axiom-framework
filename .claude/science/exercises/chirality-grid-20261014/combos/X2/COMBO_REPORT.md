# X2 combination report: a native three-generation chiral package

- **Agent:** combination agent X2, Claude Opus 5.5. This is the same model family as the supervisor and every route agent, so it is not an independent referee. Window: 2026-10-14, 14:07–14:40Z.
- **Hygiene:**
  - No repository was edited.
  - Files: `PREREG.md`, written at about 14:25Z before any run; `scripts/x2_cert.py` with its outputs; this report.
  - One process ran at a time, with OMP_NUM_THREADS=2, taking 18 s and peaking at 238 MB. Nothing is still running.
- **Read:**
  - `docs/MINIMAL_AXIOMS_2026-06-29.md`, in full (233 lines);
  - the exercise SKILL (origin/main), and in `proof-search-governance.md` the sections Independent Search Rounds, Theorem-Strength Gap Test and Candidate-Proof Audit;
  - the packet files `WALL.md`, `ROUTES.md` (in full), `ASSUMPTIONS.md` and `APPROACH_REGISTRY.md`;
  - `routes/F1`, `routes/F4` and `routes/F6` `ROUTE_REPORT.md`, in full;
  - on HEAD: `agents/C5_TW3_report.md` in full, and `C5_TW2_report.md` lines 1–120 plus the lines cited below;
  - `OUTSIDE_VIEW.md:82` and `step0/PRIOR_ART.md:84`, where Eichten–Preskill was already flagged.
- **Path abbreviations:**
  - AX = `docs/MINIMAL_AXIOMS_2026-06-29.md`;
  - F1/F4/F6 = `routes/F*/ROUTE_REPORT.md`;
  - TW2/TW3 = `gravity-current-state-20261009/agents/C5_TW*_report.md`;
  - OUT = `scripts/x2_cert.out`.
- **Labels:**
  - **proved:** a complete short argument, unrefereed;
  - **checked:** a runner in this folder;
  - **suggested:** an argument that has not been checked;
  - **reading:** an interpretation;
  - **comparator:** literature.

---

## Plain-words summary

The idea was to take three separate facts and make them one package.
- The grid's basic moving particle (the "walker") naturally has three left-handed copies, sitting at three special momenta (hw1).
- The grid already has a handedness operator.
- The unwanted mirror partners sit at the other five special momenta and could be made heavy by a strong interaction that only they feel.

**What I found**

1. **The package exists and can be written down exactly.** The interaction that touches only the mirrors can be made fully symmetric under cubic rotations, so it picks no lattice direction (checked). The three light copies are then protected exactly:
   - grid translations stop any ordinary mass from reaching them (proved);
   - at their exact momenta they do not feel the strong interaction at all (proved; checked to 0 on a small many-body system).
2. **Two parts of the earlier routes do not survive the combination:**
   - F6's shortcut, which pairs off two of the mirrors with an ordinary mass, needs a fine-tuned number and breaks single-step translations (checked);
   - F1's rule that translations block the dangerous light-plus-three-mirrors coupling is false whenever there are exactly three light copies (checked exhaustively). It holds only with four light copies, and a fourth light generation is excluded by data.
3. **"Leakage" between light and mirror particles, the old Eichten–Preskill worry, does come back.** No symmetry can forbid it (proved). Every leaking coupling is weak and fades at low energy. This is not where the package can fail.
4. **Where it can fail is the same place as every other route.**
   - Do the strongly coupled mirrors leave behind a massless bound state? The field's open dispute (Golterman–Shamir) is exactly this.
   - Do they break the symmetry on the way? The 1993 analysis of Eichten and Preskill's own model, which is this construction's direct ancestor, found exactly that.
5. **The combination is a cleaner, sharper version of an obligation that was already known, not a new mechanism.**
6. **A cross-lane bonus (proved; checked exhaustively).** Making the three generations' masses different needs no preferred lattice direction. Making them *mix* the way quarks do (CKM) does need one. So a first-order strain coupling of the kind TW-2 found is unavoidable in the flavour sector. Its size is not computed.

---

## 1. The combined construction (X2-A) and its admissibility checks

**The law.** Continuous time. The object is ψ(x) ∈ C²(qubit/walker spinor) ⊗ C¹⁶ (Spin(10) spinor) per site, with fermion statistics supplied.

  H = Σ_a ψ† σ_a sin p_a ψ  (walker)  +  W Σ_x Q(ψ_S(x)),   ψ_S = F ψ,   F = f(p) ⊗ 1₂ ⊗ 1₁₆.

The filter f comes in two versions, either of which works:

| | f_F1 (F1:116) | f_NN = (1 − Σ_a cos p_a)/2 |
|---|---|---|
| Real-space support (checked, OUT:24-25) | the 27-site cube | the 7-site star |
| Zeros among the corners | exactly the three hw1 corners | the hw1 corners |
| Shape at a hw1 corner | isotropic Hessian ½·1, so f ≈ \|q\|²/4 (OUT:30) | indefinite Hessian; vanishes on a cone through each hw1 corner (OUT:31) |
| Minimum of \|f\| away from hw1 (more than 0.3 from every hw1 corner) | 0.024 (OUT:32) | not computed |

Q is a Spin(10)-singlet quartic with no bilinear content. One example is the 16⊗16→10 channel, Bᵃ = ψ_Sᵀ(iσ_y ⊗ CΓᵃ)ψ_S, built into BᵃBᵃ + h.c. and Bᵃ†Bᵃ. This is Eichten–Preskill's λ channel with **all four legs filtered**.

**Checks:**

| Requirement | Status |
|---|---|
| Translation invariance (AX:37-38, :57-58) | checked: commutators 0.0 for H_W and both filters (OUT:27) |
| 24 proper cubic rotations with spin lift | checked: ≤ 4.5e-16 (OUT:26). The filter is A1g. |
| On-site Spin(10) ⊃ G_SM, gauged by links | by construction; F → F[U] gauge-covariantly |
| Light content | 3 × 16 left-handed Weyl at hw1 (walker node chirality (−1)^hw; F6:70-79) |
| Mirror content | hw0 (R), hw2 (3R), hw3 (L), ⊗16; net index +3 per component |
| Emanant Z16 gate | **proved:** for every cyclic g·i^F, ν_g = d·Σ_c(±1). Any set of corners passes at d = 16. The 5-corner mirror has an odd sum, so it fails at d = 15: ν_R is forced (agrees with F1:70) |
| Fermion number | **proved:** U(1)_F must be broken by Q, because its cubic anomaly on the mirror is ∝ 16 × (net index) ≠ 0. Z4^F survives, as F1:83 needs. |

### Lemmas: what the combination gives that no single core gives

- **X2-L1, light protection by corner labels (proved).**
  - With exact single translations, low-energy modes carry a conserved label in Z₂³ (their corner).
  - Each hw1 label e_i holds exactly one Weyl node per component.
  - So no translation-invariant bilinear can gap it. A Dirac pairing would need a partner with the same label, and none exists. A Majorana pairing is excluded because 16⊗16 contains no singlet.
  - **No tuning is involved.** Index per label sector: F6 Lemma 2 (F6:101), applied per label.

- **X2-L2, exact corner decoupling (proved; checked).**
  - f(e_i) = 0 gives {ψ(e_i), ψ_S(x)} = {ψ(e_i), ψ_S†(x)} = 0, so ψ(e_i) commutes with every even polynomial in ψ_S.
  - The walker vanishes at the corner, h(e_i) = 0.
  - Hence [H, ψ(e_i)] = 0 at every coupling, on every even-L torus. The light pole at each hw1 corner is exact, with spectral weight 1.
  - **Checked** (Fock space, L = 2, N = 3 → 2 sectors, random filtered quartic): |[H, ψ(hw1)]| = 0.00. The mirror corners give 0.155, and the unfiltered control gives 0.155 at hw1 (OUT:33-34).
  - This rules out the Eichten–Preskill/Smit–Swift mechanism in which the physical mode becomes massive through unfiltered legs (§7).

- **X2-L3, the three-generation selection-rule theorem (proved; checked exhaustively).**
  - **Statement.** If exactly three corners are light and the other five are mirror, then light·mirror³ and light³·mirror are both allowed by exact translations.
  - **Proof.** |M| = 5 > 8/2, so g + M and M meet for every g. Hence M + M = Z₂³, and M + M + M = Z₂³.
  - **Checked** (OUT:12-20). Only |Lt| = 4 assignments (14 of them, the index-2 cosets) forbid both odd-leg classes. Split A has, for example, 001 + 000 + 110 + 111 = 0 (OUT:3) and 100 + 010 + 001 + 111 = 0 (OUT:4).
  - **Corrections:**
    - F1:108's rule ("translations forbid every low-energy light·mirror³ and light³·mirror") holds only for T_d-graded 4+4 splits, such as K2a's staggered selector. It is **false for the walker three-generation split** that F1-R1 proposes (F1:116).
    - F6:178 ("flavour mixing does not couple the light and mirror halves") likewise holds only for the T_d split. In X2-A, a Higgs condensate at hw2 momenta couples light e_x to mirror hw3, since 100 + 011 = 111.
  - **Consequence (proved).** T_d is the exact *handedness* operator (F6:70-79), but it is **not** the light/mirror separator: hw3 is T_d-odd, left-handed, and mirror. The separator is the single-translation corner label.

- **X2-L4, AABB cannot be forbidden (proved; checked).**
  - Every split has allowed A A B B operators (OUT:21, exhaustive).
  - The density form (A†A)(B†B) is invariant under every unitary symmetry that preserves the split (proved).
  - So **no symmetry can forbid it.**

- **X2-L5, no local light/mirror projector (proved).**
  - A continuous, translation-invariant projector P(k) has constant rank on the connected T³.
  - Excluding the light node at hw1 needs rank 0 on the node's spin space there. Including the mirror node needs rank 2 at the mirror corners. So the filter cannot be a local orthogonal projector: F² ≠ F.
  - **Consequence.** Unlike a slab's far layer (F4) or SPIN10's mirror slots, the mirror modes ψ_S(x) are non-orthonormal and overlap between neighbouring x. The strong-coupling limit W → ∞ is a frustrated many-body ground-state problem, not an atomic product. Neither SPIN10's Feshbach failure nor Golterman–Petcher–Rivas's strong-coupling expansion transfers to X2-A directly (reading).

- **X2-L6, F6's 3L + 3R reduction is tuned and breaks single-translation covariance (checked).**
  - Adding δ·iεF₁ (f₁ = Σ cos p_a, which is also cubic-invariant, Hermitian and Spin(10)-blind) gaps the hw1 nodes at exactly |δ| (OUT:38-40).
  - iεF is odd under every unit translation, leaving only FCC (even-sum) translations. Under these, each hw1 corner and its hw2 partner carry the same label (OUT:41). So a light–mirror Dirac mass is symmetry-allowed, and f(hw1) = 0 is one real tuning.
  - iεF is also not covariant under the axiom's unit translations (AX:57-58). F6-tD (F6:169-174) is therefore a free-level illustration, not a native package.

- **X2-L7, the chirality filter picks no direction (checked).**
  - f is A1g (OUT:26). The hw1-versus-rest split is preserved by every proper rotation and by inversion.
  - TW-2's T₁ problem (TW2:116, "no cubic-invariant taste-split mass") belongs to the staggered *taste* split, not to the Hamming-weight split.
  - TW-3's no-go (TW3:34, :213-216: onsite translation-invariant gapping cannot select twins) is respected. The law is non-onsite (7- or 27-site) yet keeps every translation, and it selects by momentum, not by breaking the shift.

- **X2-L8, flavour sector: CKM forces an axis (proved; checked exhaustively over 1120 subgroups of O ⋉ Z₂³).**

  | Residual vacuum symmetry H, acting on the hw1 triplet | Three distinct masses | Nontrivial CKM | Invariant traceless strain |
  |---|---|---|---|
  | Contains a C3 | possible (40 subgroups) | never: the commutant is commutative | — |
  | H = T (tetrahedral) | yes (masses form a Hermitian circulant, the Koide-type form) | no | **0** (OUT:55-60) |
  | Nontrivial CKM | — | 283 subgroups | ≥ 1 in every case |

  Prediction violations: none (OUT:54).
  - **Proof of the third row.** A 3-cycle acts with three distinct eigenvalues, so all invariant mass matrices share its eigenvectors. Groups with no C3 are 2-groups, which lie in a D4, and D4 fixes the strain component 2z² − x² − y².
  - **Reading.** Splitting the masses alone can avoid TW-2's first-order strain leak, but realistic quark mixing cannot. A first-order traceless-strain channel is symmetry-allowed in the flavour sector of *every* hw1-generation package. TW2:173 proved the analogue only for its axis-split taste family. Its size here is not computed.

- **X2-L2k, F4-L2 adapted to momentum separation (proof skeleton; open steps as in F4:81-83).**
  - Assume exact translations, an on-site U(1) ⊂ G, a unique ground state, charge-q poles only at hw1 (index −3n_q, exact by L2), and no other gapless charge-q state.
  - Then G_q(0,k) of the elementary ψ has zeros of total index +3n_q. By Stokes on T³ they sit in the **same field** that carries the light poles, at the mirror corners.
  - The filtered design supplies by construction the k-dependent self-energy Σ ∝ |f(k)|² that F4-L1 (F4:50-63) demands. So F4-L1 is evaded, while F4-L2's dichotomy (a protected zero, or a massless composite) is inherited unchanged.

---

## 2. Answers to the four posed questions

**(a) Is there one framework-native package?** Yes: X2-A as specified in §1.
- Its symmetry skeleton is native: Z³ translations and proper rotations are axiom content (AX:37-38). Generations are the walker's hw1 corners, handedness is T_d, and the light is protected by corner labels.
- Its matter and dynamics are supplied: the 16, fermion statistics, the walker, and Q (§5).
- **Its exact terminal obligation is L_X2 (§3).** Its two caveats are X2-L3 (T_d is not the separator) and X2-L6 (F6's bilinear shortcut is not native).

**(b) Does momentum separation bring Eichten–Preskill leakage back through AABB, and can a symmetry forbid it?**
- **Yes, it comes back. No symmetry can forbid it (X2-L4).** There are three channels:
  1. **Filter imperfection.** Light legs enter with a form factor f(q) ≈ |q|²/4 (f_F1); the coupling is exactly 0 at the corner (X2-L2).
  2. **Gauge links carrying lattice-scale corner momenta Q.** These turn a light fermion into a mirror fermion with no filter suppression. The coefficient is about g²D(Q), with D(Q) = 1/(4Σ sin²(Q/2)) = 1/4, 1/8, 1/12 for Q in hw1, hw2, hw3. For g² ≈ 0.25–0.5 at the lattice scale this gives about 0.02–0.13 in lattice units (suggested). The slab suppresses this channel as e^(−L); here it is only power-suppressed.
  3. **Strain and generic perturbations,** which make f(hw1) = O(u) (suggested).
- **All three are dimension-6, so irrelevant in 3+1D.** A light mass stays exactly forbidden (X2-L1). The light can be "eaten" only if its coupling exceeds the symmetric-gapping threshold, which is O(1) in lattice units (comparator). The margin is roughly 10 or more (suggested). So leakage is **not** the failure point.
- **Grabowska–Kaplan's remedy is unavailable here (proved).** That remedy couples the mirror alone to a smoothed gauge field. Here light and mirror are one field ψ, so they must see the same links. Global link smearing for all fermions can suppress channel 2, at a range price.
- Comparator: the two-cutoff Wilson–Yukawa result of Hernández & Boucaud, arXiv:hep-lat/9706021. Seen only in a search summary; I did not read it.

**(c) Does the cube-spread law pick a direction?**
- **Not in the chirality sector.** The law is A1g (X2-L7).
- **In the flavour sector, yes, if and only if CKM is nontrivial** (X2-L8). That is TW-2's first-order hazard, now proved to be generic for hw1 generations.

**(d) F4-L2 for momentum-separated mirrors.** It carries over unchanged (X2-L2k). Momentum separation makes the protected zero and the light pole the same field's properties.

---

## 3. Terminal obligation and theorem-strength gap test

**L_X2.** For X2-A, with some W in a window:
- the ground state is unique and symmetric under translations, proper rotations, Spin(10) and Z4^F;
- **no intermediate symmetry-breaking phase occurs.** In particular the 10-vector Bᵃ does not condense;
- the only gapless fermion poles are the 3 × 16 at hw1;
- no composite fermion is gapless at any momentum;
- G_ψ(0,k) has zeros of index +3 per component at the mirror corners;
- **(L_X2-g)** once the theory is gauged through links, the zeros do not act as ghosts (Golterman–Shamir, arXiv:2311.12790).

**Gap test:**
- **L_X2 ⇒ T, chirality clause, all three generations.** Spin(10) ⊃ G_SM is on-site and exactly gauge-invariant, and the hw1 triplet gives the three generations. Flavour masses and hierarchy are not part of T (WALL.md:41).
- **T ⇒ L_X2:** no, because other families could pass T.
- **So L_X2 is stronger than the target's clause. Status: blocked-equivalent.**
  - L_X2 ⇔ "Golterman–Shamir condition (3) fails for X2-A, and no intermediate SSB occurs". GS conditions (1) and (2) hold: finite range, and 3+1D (F1:41-46, :139).
  - It is the walker branch of F1-R1, now with its mirror, filter class, selection rules and light protection fixed.

**Genuinely new mechanism?**
- **No.** Nothing here advances the proof of L_X2.
- X2-L2 removes the light's survival from the obligation. X2-L5 shows that the known strong-coupling failure arguments do not transfer automatically. Both narrow the obligation, but neither reopens it.
- **Reopen condition: unchanged from F1/F4.** It is a protected zero, or the absence of any massless composite, shown in a many-body calculation.

---

## 4. What changes in the round-1 obligation map

| Round-1 item | Change from X2 | Label |
|---|---|---|
| F1:108 selection rule | Restricted to T_d-graded 4+4 splits. For three light corners the odd-leg channels are open. | proved; checked |
| F1-R1 walker branch (F1:116) | Concretised as X2-A: filter class A1g; f_NN gives a 7-site star; mirror fixed to hw0+hw2+hw3; light exact at the corners. | checked |
| F6-tD (F6:169-174) | Demoted from "native reduction" to a tuned illustration that breaks unit-translation covariance. | checked |
| F6:178 generation side finding | Holds only for the T_d split. In the three-generation package, the hw2-momentum Higgs couples hw1 to hw3. | proved |
| F4-L1/L2 | L1 evaded by construction, L2 inherited. The "no EP leakage" advantage of real-space separation is quantified: exponential becomes power-law, and all remaining channels are irrelevant. | proved / suggested |
| PRIOR_ART:84 ("links leak, Eichten–Preskill") | Made precise: three channels, none forbiddable, all irrelevant; the real risks are GPR's SSB and composites. | proved / suggested |
| TW-2 T₁ hazard | Absent from chirality. **Present in flavour iff CKM ≠ 1.** New cross-lane obligation: compute the first-order traceless-strain coefficient of the CKM-generating breaking for hw1. | proved; checked |
| TW-3 (TW3:34) | Respected: non-onsite, translation-invariant, momentum-selective. | proved |

---

## 5. Price in framework terms (named, not adopted)

| Price | Axiom line | Note |
|---|---|---|
| **P-X2-1 Matter per site:** 16 Spin(10) components per walker component, i.e. 32 complex fermion modes (2^32 per site) | AX:47 (M₂(C)) | Owner's matter-count decision, F6:147. Not M₄(C)/#4 (F6:92-95). It strains "one record per site" (AX:79-80). |
| **P-X2-2 Fermion statistics** | AX:178 open gate | — |
| **P-X2-3 Supplied dynamics:** the continuous-time walker plus W·Q | AX:116-123: admissibility chooses no Hamiltonian | Continuous time is required, because no selector exists in Z⁴ (K2a). |
| **P-X2-4 Range** | AX:38, :57 ("nearest-neighbour") | f_NN gives terms centred on a site's nearest-neighbour star, spanning sites up to 2 apart. f_F1 gives the 27-site cube. A mild finite-range price (the owner's range question). |
| **P-X2-5 Gauge structure:** on-site Spin(10) internal symmetry, G_SM links, and a gauge-covariant filter F[U] | AX:87-90 (named conditional) | — |
| **P-X2-6 Fermion number:** ν_R forced; U(1)_F broken to Z4 by Q | — | proved |
| **P-X2-7 Flavour/strain:** realistic CKM forces a residual symmetry inside D4, with a first-order traceless-strain channel | — | Size open; a C5 hazard |
| **Inherited open:** L_X2 and L_X2-g | — | the field-wide SMG question |
| **No tuning for chirality.** The filter's exact zero at hw1 is a law choice, but only weak light coupling is needed (O(1) margin, suggested). | — | — |

---

## 6. Strongest objection (kill attempt on X2)

**The objection: X2-A is the Eichten–Preskill model on a different carrier, and that model failed.**

What the EP model is (comparator; hep-lat/9207005 read via ar5iv, together with the abstract of hep-lat/9206010, NPB 395 (1993) 596):
- an SO(10) 16 with naive fermions;
- a local four-fermion λ term into the 10-vector bilinear;
- a Wilson-like r term, ∝ Σ(1 − cos p), that vanishes at the physical mode and is strong at the doublers.

What Golterman–Petcher–Rivas found:
- at strong coupling, every species is a massive Dirac fermion, and the bound-state partners "do not dissociate";
- a symmetry-broken phase, SO(10) → SO(9), separates the strong- and weak-coupling symmetric phases;
- at weak coupling, all species become massless together.

The Smit–Swift Wilson–Yukawa models fail in the same way, with a vector-like strong-coupling symmetric (PMS) spectrum (hep-lat/9301015; hep-lat/9910013; search summaries).

**What survives the objection:**
1. EP's λ term acts on the physical mode with unfiltered legs. X2-A filters all four legs, so the physical modes are *exactly* decoupled at the corners (X2-L2, checked). EP's "everything massive at strong coupling" route is therefore closed at hw1.
2. X2-L5: the mirror modes are non-orthogonal, so GPR's strong-coupling, large-N expansion does not carry over directly (reading).

**What does not survive:**
- X2-A uses the same 10-vector channel, so the **intermediate-SSB failure is inherited structurally** (suggested).
- Golterman–Shamir's general conjecture covers X2-A regardless.

**Verdict on the objection.** It does not refute X2-A: GPR rests on large-N extrapolation for a different model. It does show that X2-A is "Eichten–Preskill with exact light decoupling", a repackaging, and that the decisive test must watch for symmetry breaking as well as composites.

**Lesser objections:**
- hw3 is a left-handed mirror, so electroweak or flavour condensates mix it with the light at y·v/Δ ≈ 10⁻¹⁷. This is negligible (suggested).
- Mixed Z₂³ bordism classes beyond the cyclic Z16 gate are not computed (as at F6:166). A nonzero class would forbid gapping the 5-corner mirror. **This is the cheapest open kill.**
- The package is native only in its skeleton: P-X2-1 and P-X2-2 are large.

---

## 7. Tests

**Pre-registered:** `PREREG.md`, before any run. **Run:** `scripts/x2_cert.py` → `x2_cert.out`.

| Test | Pre-registered reading | Result |
|---|---|---|
| T1 selection rules (exhaustive over 254 light sets) | A allows odd-leg classes; G forbids them; no three-light set forbids them; AABB is always allowed | **PASS** (OUT:1-21) |
| T2 covariance and decoupling | commutators ≤ 1e-12; f_F1 zero only at hw1; Fock \|[H, ψ(hw1)]\| ≤ 1e-10, control ≥ 1e-2 | **PASS**: 4.5e-16 and 0.0; Fock 0.00 vs control 0.155 (OUT:23-34) |
| T3 F6 tuning | hw1 gap = \|δ\| | **PASS**: 1.000e-3, 1e-2, 1e-1 at (π,0,0) (OUT:36-41) |
| T4 flavour, CKM and strain (1120 subgroups) | no subgroup with nontrivial CKM and 0 invariant strain; T gives distinct masses, trivial CKM, 0 strain | **PASS** (OUT:43-60) |
| T5 locator (free; forced by Nielsen–Ninomiya) | the unpaired modes sit at hw1 | **as expected**: 4 zero modes at each hw1 corner (ψ plus χ), vector-like (OUT:62-64). The Golterman–Shamir signature sits at the **light** corners, and it is not evidence either way. |

**Notes on the runs:**
- **Bug note.** Run 1 had a factor-2 normalisation error in T4's strain basis (kept as `x2_cert_run1_strainnorm_bug.out`). It showed spurious "violations", including for the trivial group. After the fix, T1–T3 output is byte-identical and T4 passes.
- **What T1–T4 establish.** They decide the structural claims of X2 (exhaustive or exact). None of them tests L_X2.

### Decisive test for L_X2 (pre-registered here; not runnable in this budget)

Why no small test fits:
- at L = 2 everything is 0+1D, and gapping there is trivial;
- in 1+1D, four-fermion terms are marginal, so a result does not decide 3+1D (F4:123-128; F1:170);
- 2+1D or 3+1D clusters with ≥ 8 flavours exceed exact diagonalization.

**X2-MB:** X2-A in the smallest dimension where four-fermion terms are irrelevant, i.e. a 2+1D walker with:
- light at hw1;
- mirror at hw0+hw2, with enough flavours to pass that dimension's gapping count;
- an antiunitary symmetry forbidding single-cone masses;
- the interaction only through ψ_S.

Establish sign-freeness first; if the model is not sign-free, use 3+1D Hamiltonian tensor-network or QMC.

Measure:
- (i) the mirror single-particle gap;
- (ii) the light cone (control);
- (iii) the bilinear order parameter Bᵃ;
- (iv) composite spectral functions of ψ_Sψ_Sψ_S^(†) at the hw1 **and** mirror corners;
- (v) the zero index of G_ψ(0,k) at the mirror corners.

Readings:
- **PASS:** a window with (i) open, (iii) zero under finite-size scaling, (iv) gapped everywhere, and (v) equal to minus the light index.
- **FAIL-GPR:** (i) opens only where (iii) ≠ 0.
- **FAIL-GS:** (iv) is gapless at some corner while (i) is open.
- **Cost:** weeks.

---

## 8. Files and sources

**Files** (all in this folder, `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/combos/X2/`):
- `PREREG.md`
- `scripts/x2_cert.py`
- `scripts/x2_cert.out`
- `scripts/x2_cert.err` (time, 238 MB peak)
- `scripts/x2_cert_run1_strainnorm_bug.out`
- `COMBO_REPORT.md` (this file)

**Comparators:**
- Eichten & Preskill, NPB 268 (1986) 179 (as cited in `OUTSIDE_VIEW.md:82`).
- Golterman, Petcher & Rivas: [hep-lat/9206010](https://arxiv.org/abs/hep-lat/9206010) (NPB 395 (1993) 596) and [hep-lat/9207005](https://ar5iv.labs.arxiv.org/html/hep-lat/9207005) (read).
- Wilson–Yukawa reviews and studies: [hep-lat/9301015](https://arxiv.org/pdf/hep-lat/9301015) and [hep-lat/9910013](https://arxiv.org/pdf/hep-lat/9910013) (search summaries only).
- Hernández & Boucaud, [hep-lat/9706021](https://arxiv.org/pdf/hep-lat/9706021) (search summary only).
- Giedt & Poppitz, [arXiv:1003.5896](https://arxiv.org/pdf/1003.5896) (not read).
- Golterman & Shamir, arXiv:2505.20436, 2603.15985 and 2311.12790, as cited in F1, F4 and F6.
