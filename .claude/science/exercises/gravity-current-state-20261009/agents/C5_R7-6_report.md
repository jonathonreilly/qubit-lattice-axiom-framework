# C5 R7-6 report: three bodies in box-confined Poincaré (can the interacting algebra close beyond two bodies on a lattice?)

**Author.** Claude Opus 5.5 probe. Same family as the supervisor and as the R7-1 worker, whose unrefereed P2 is the main input. Unrefereed. Ran 2026-10-12, 15:17Z to about 15:55Z. No repository file was edited.

**Scratch.** `S/` = `.../scratchpad/C5/R7-6/`. Scripts and outputs are in `S/scripts/`:
- `r76_threebody_naive.py`: d = 1, the three-fermion sector of R7-1's law, on the ring's own momentum grid.
- Its outputs `r76_threebody_naive_fermi_lam{-2.5,-3.0,-4.0}_kap0.25.out`.
- `r76_fit.{py,out}`.
- `r76_fock_crosscheck.{py,out}`: an independent second-quantized Slater-determinant build.
- `r76_packing_range.{py,out}`: the range of the BT packing operator B_a on the fixed-P fibre (d = 1).
- `S/scripts/discarded/` holds two early runs. Their plateau or box was too small: c < 1 or a truncated g lay on the trimer's support. They are kept only for the record and used nowhere.

**Read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`, in full.
- `TESTS.md`: lines 2302–2440 (C5 method and round 1), 3240–3395 (rounds 6–7, including R7-6 at :3387–3394).
- `SUMMARY.md` §17 (:355–494).
- `agents/C4_M1_referee.md`, `agents/C4_B1_referee.md`, `agents/C4_I1_referee.md` (grep).
- `agents/C5_R6-1_report.md` and `agents/C5_R6-1_referee_verdict.md`.
- The R7-1 report and scripts (`.../C5/R7-1/R7-1_report.md`; `r71_bt_twobody.py` reused).

**Labels.**
- **proved:** argued here in full.
- **checked:** numerics here.
- **suggested:** argued, not proved.
- **reading:** an interpretation.
- **comparator:** someone else's result, used for comparison.
- **RECALLED:** literature from memory, not verified here.
- **VERIFIED-CITE:** the bibliographic fact was confirmed on the web; the content was not re-derived.

---

## 0. In plain words

1. **Adding up pair interactions does not work, and no choice of boost can rescue it (checked, d = 1).**
   - Put three particles on R7-1's lattice law, so the Hamiltonian is the free part plus R7-1's exact two-body Bakamjian–Thomas (BT) pair term for each pair.
   - The three fermions then bind into a trimer, but the trimer's rest mass √(E² − P²) depends on its momentum: 0.734266 at rest, 0.733714 at P = 0.105, 0.732137 at P = 0.209. These values are converged in the ring size to about 1e-6.
   - Its dispersion fits E² ≈ M₀² + (1 − δ)P² with δ ≈ 0.074 at low P. The trimer moves on a light cone about 4% slower than its own constituents, which are exact in the same law (R7-1).
   - Any exact Poincaré algebra with this H and the lattice momentum would keep the trimer's mass the same at every momentum. So **no boost operator of any form** closes the algebra for the pairwise Hamiltonian.
   - Three-body terms are therefore forced into H itself, not only into K. This sharpens R7-1 §4.3, which only showed that the pairwise *boost* fails.
2. **The lattice adds nothing new to the three-body problem.**
   - Inside the momentum box, the lattice three-body problem *is* the continuum relativistic three-body problem: same operators, same algebra (Lemma L3, proved).
   - The lattice adds one constraint: the spatial momentum must stay the kinematic lattice momentum, because e^{iP} must be the lattice shift. This forces the "instant form" of relativistic dynamics (Lemma IF, proved).
   - It rules out the cheap 1+1 escapes in which pair interactions simply add up: the light-front form (proved here) and the Ruijsenaars–Schneider model (RECALLED). In both, the momentum depends on the interaction.
3. **The standard continuum cure fits inside the box (proved in part; RECALLED in part).**
   - First, the BT three-body law. Its mass operator turns out to be exactly the pairwise law's Hamiltonian at total momentum zero, carried to other momenta by free boosts (Proposition BT0, proved). It closes the algebra exactly. The three-body correction it adds is +5.5e-4 to +8.2e-3 in energy over 0.10 ≤ P ≤ 0.50 (checked).
   - Its generators do not separate into independent clusters (RECALLED). The mechanism is argued, and its key operator's long reach is checked.
   - Sokolov's "packing" unitaries repair that (Sokolov 1977/78; Coester–Polyzou 1982; VERIFIED-CITE).
   - Every ingredient preserves compact momentum support. So the packed law transplants to the lattice box with an exact algebra (proved, given the BT algebra and Lemma L3).
   - Cluster separability holds by Sokolov's and Coester–Polyzou's theorem (RECALLED), whose short-range hypothesis our C^∞ compact form factors meet (suggested).
4. **What is not done.**
   - The packed three-body law was **not checked numerically as a whole**. Its packing operators are momentum-space reparametrizations that need off-grid interpolation.
   - Its basic building block was checked on its own (d = 1).
     - The BT packing operator for one pair is exactly 1 at zero total momentum (to 5e-13).
     - It falls off steeply as that pair separates: 5.1e-4, 2.2e-5 and 4.7e-7 at separations 80, 160 and 320. The local power steepens from 4.5 to 5.6, consistent with exp(−0.8√r), the same smoothness class as the form factor. This is a fit over one decade, not a proof.
     - It stays of order one as the third particle recedes: 0.14, 0.28 and 0.86 at distances 0, 20 and 80. That long reach is exactly what makes the BT generators fail to separate, and what Sokolov's packing has to undo.
   - That its three-body terms have faster-than-power tails is **suggested, not proved**. This is the one place a hidden power-law tail could sit (§4.3, T-risk). The packing operators are non-analytic functions of the pair's full spectrum, and a threshold non-smoothness there could produce power-law tails.
5. **Against the FIXED readings: INCONCLUSIVE** (worker reading), **leaning PASS**.
   - Existence: the algebra is proved exact, cluster separability rests on a cited theorem, and the box transplant is proved.
   - PASS needs "checked", and the tails are open.
   - A FAIL is not available: the construction exists in the continuum and transplants. The only no-go found covers the pairwise class, which the item does not restrict to.

---

## 1. Hypotheses and classes (stated before any title)

- **H-lat.** As R7-1 (`R7-1_report.md:31-33`): one complex fermion mode per site of Z^d, with a graded tensor product, and time continuous (Z^d × ℝ).
  - Numerics are in d = 1.
  - The ⊗M₂ (ungraded) version inherits R6-1's open status (`C5_R6-1_referee_verdict.md:3,17`).
- **H-box.** A frame-fixed box in lattice momentum. Box states have C^∞ momentum wavefunctions with compact support in a stated region R inside the box.
- **H-gen.**
  - The Poincaré relations [H,P] = 0, [K,P] = iH, [K,H] = iP are required as operator identities on a common invariant domain of box states, as in R7-1.
  - For Theorem N, we additionally assume K generates a local flow that keeps compactly supported box packets in the domain for small rapidity. R7-1's P1 and P2 have this property (`R7-1_report.md:105-108,171-175`).
- **H-P.** e^{iP} = T, the lattice shift, on the box sector, with ‖P − Q‖ < π there. Here Q is R6-1's additive sawtooth momentum. This is the reading "the Poincaré translation by one spacing is the lattice translation" (Lattice axiom, `MINIMAL_AXIOMS:37-41`).
- **H-CS (cluster separability, Coester–Polyzou sense; RECALLED).**
  - For each partition a = (ij)(k), translating the cluster k away to distance D makes the generators converge strongly on box states to the tensor-product generators of (ij) ⊗ (k).
  - As all three separate, they converge to the free generators.
  - The weaker property, a cluster-separable S-matrix, is named separately wherever it is the only one available.
- **Excluded outside realizations, and not addressed:**
  - pair creation and loops (R7-5's subject);
  - gauge fields;
  - N ≥ 4 at the level of a single second-quantized law (§5);
  - the local (non-affine) lapse algebra;
  - set B (Z⁴);
  - ⊗M₂ ungraded composition.

## 2. Prior art (each item counted once)

- **R7-1 P2 (unrefereed).**
  - Two-body BT box law with an exact algebra on 𝒟₂ (`R7-1_report.md:133-161`).
  - N ≥ 3 is open (`:163-167`): the pairwise boost's cross terms [K_W,12, W₂₃] "do not cancel".
  - "Box confinement neither helps nor hurts this problem" (`:167`). Lemma L3 below makes that precise.
- **R7-1 Lemma L** (one-body generators on int B equal the continuum ones; `:87-94`). Its rapidity budget and leakage (`:169-190`) carry over unchanged.
- **B1 referee.**
  - Theorem S: the boost is forced to be a first moment under regular affine-lapse smearing.
  - Theorem U: no closure on bounded exponentiating sectors.
  - "patchwise DSR remains possible" (`C4_B1_referee.md:11,21`).
- **M1.** A globally isolated composite band has averaged anomaly −βI. It does not exclude "non-first-moment generators … unbounded continuum finite-N sectors" (`C4_M1_referee.md:15`).
  - The trimer here exists only on a P-plateau, so it is not globally isolated, as for R7-1's dimer (`R7-1_report.md:161`).
- **R6-1 referee.** The CAR witness is sound but outside ⊗M₂ (`C5_R6-1_referee_verdict.md:3,33`). That scope is inherited here.
- **Literature.**
  - Bakamjian–Thomas (1953): instant-form mass-operator construction (RECALLED).
  - Coester (1965): the three-body BT S-matrix is cluster separable, but the BT generators are not (RECALLED).
  - Sokolov, *Dokl. Akad. Nauk SSSR* 233, 575 (1977) and *Teor. Mat. Fiz.* 36, 193 (1978): packing operators (VERIFIED-CITE, through the citation list of Coester–Polyzou's later review, arXiv nucl-th/0102050).
  - Coester and Polyzou, *Phys. Rev. D* 26, 1348 (1982): an explicit N-particle construction satisfying cluster separability. Their abstract states that the N-body interaction strength falls rapidly with N (VERIFIED-CITE, via the search summary of the Iowa repository record; full text not read).
  - Keister–Polyzou review (Adv. Nucl. Phys. 20, 1991) (RECALLED).
  - Reichelt–Schweiger–Klink, arXiv 1711.04555: a review stating that BT runs into cluster separability as soon as more than two particles interact (VERIFIED-CITE, abstract only).
  - Ruijsenaars–Schneider (1986) (RECALLED, comparator only).

---

## 3. What the lattice adds to the three-body problem

### Lemma L3 (transplant) — proved, elementary

- **Setting.**
  - Let 𝒮 be a continuum (1+1 or d+1) N-body system whose generators (H, P, K) are built from the one-body generators, and from operators that act at fixed total P with momentum kernels supported in a compact set.
  - Suppose 𝒮 has a compact region R in momentum space with |legs| < b_int < π/2 such that 𝒟_R = C_c^∞(int R) is invariant under H and K.
- **Claim.**
  - The lattice law H_lat = H₀^lat + (the same interaction kernels, multiplied by smooth cutoffs equal to 1 on R) coincides with 𝒮's H on 𝒟_R.
  - K_lat = K₀^lat + (the same) coincides with 𝒮's K there.
  - So every algebraic identity of 𝒮 holds on 𝒟_R.
- **Proof.**
  - Lemma L (`R7-1_report.md:87-94`): the one-body lattice generators act on C_c^∞(int B) as the continuum ones, including the first-order K₀.
  - The interaction pieces are equal on R by construction.
  - No umklapp, because pair legs are < π/2, so Q = Σq̂(k_i) is additive (R6-1's two-line argument, `agents/C5_R6-1_report.md:93-96`).
  - Note: for three legs only the *pair* legs need |k| < π/2. Q is real-valued and additive, not reduced mod 2π.
- **Converse.** Every lattice box law of this kind *is* a continuum law on R. Lattice-specific obstructions can therefore come only from (i) the forced form of dynamics (Lemma IF) or (ii) the existence of a compact invariant R inside the box (Lemma R).

### Lemma IF (instant form is forced) — proved, given H-P

- **First step.** e^{iP} = T = e^{iQ} on the box sector, and ‖P − Q‖ < π. On each spectral subspace {T = e^{ik}}, P has spectrum in k + 2πℤ, and so exactly {k}. Hence P = Q, which is kinematic.
- **Second step.** In 1+1 dimensions the kinematic subgroup must contain P. It cannot contain K as well: [K, P] = iH would make H kinematic, and the law free. So H and K are both dynamical: the instant form.
- **Consequences.**
  - **Light-front form is excluded.** In 1+1 it has kinematic {P⁺, K} and a single dynamical P⁻. Its algebra is linear in P⁻: [K, P^±] = ±iP^±, [P⁺, P⁻] = 0. So P⁻ = P₀⁻ + Σ_{ij} (M_ij² − M_{0,ij}²)/P⁺_ij closes **exactly, with pair terms only, for every N, and clusters** (proved; three lines). But its P = (P⁺ − P⁻)/2 is dynamical, so e^{iP} ≠ T. Excluded.
  - **The Ruijsenaars–Schneider N-body systems** (RECALLED) have a kinematic K and a dynamical P. Excluded for the same reason.
  - The lattice therefore removes exactly the forms in which 1+1 pair interactions would simply add up (reading).

### Lemma R (compact invariant region) — proved for the pairwise and BT laws; suggested for the packed law

- **Pairwise law.**
  - W_ij maps (k_i, k_j, k_k) to (k_i′, k_j′, k_k), with k_i′ and k_j′ inside the interaction box.
  - So the leg box {|k_i| < b_int} is invariant: exact, and used in the numerics. The script's leg box equals the interaction box, 1.0.
- **BT law (Proposition BT0 below).**
  - H_BT(P) = Λ_P sqrt(M_BT² + P²) Λ_P†, where Λ_P is the free-boost change of variables from rest-frame to lab momenta.
  - If R₀ is invariant under M_BT = H_pair(P = 0) (for example, the P = 0 leg box of size ℓ₀ ≥ 0.7 for κ = 0.25 and m = 0.3), then ∪_{|P|≤Π} Λ_P(R₀) is compact and invariant under H_BT and K_BT = ½{H_BT, X₀}.
  - X₀ = i∂_P at fixed rest-frame variables, so it preserves supports.
  - The lattice parameters must put this region inside the box. With physical m ≪ 1 that costs nothing (reading).
- **Packed law.**
  - The packing unitaries B_a (§4.3) are, fibre by fibre in P, smooth reparametrizations of a compact set of relative momenta, with pair masses in [M_b, M₀(κ)]. They map compact sets to compact sets.
  - A compact invariant region for B = T exp(i∫ΣĜ_a) is argued from boundedness of the flows. Suggested.

---

## 4. Results

### 4.1 Theorem N (the pairwise box law admits no Poincaré representation in the three-body sector) — proved, given the check; checked (d = 1)

**Statement.**
- H_pair = H₀ + W₁₂ + W₂₃ + W₃₁ is R7-1's law in the three-fermion sector. Each W_ij is R7-1's exact two-body BT term at fixed third momentum.
- For the parameters below, H_pair has a bound trimer whose √(E² − P²) depends on P, on a plateau where every pair term is exactly R7-1's BT operator.
- Hence there is **no** self-adjoint K of any form (first moment or not, with or without many-body terms) satisfying H-gen with this H and P = Q.

**Proof of the implication.**
- On the domain, [K, H² − P²] = H[K,H] + [K,H]H − P[K,P] − [K,P]P = 0.
- So the local boost flow preserves the M²-spectral measure of a packet while carrying it to boosted momenta.
- In each P-fibre, μ(P)² = E₀(P)² − P² is the bottom of the M² spectrum, because E₀ is the lowest H eigenvalue and P is fixed.
- The check below gives μ(0.209) < μ(0). Boost a trimer packet at P ≈ 0.209 back to P ≈ 0, with rapidity about 0.28; all legs stay below 0.6, inside the box. It arrives with M² ≈ μ(0.209)², which is below the bottom of the P ≈ 0 spectrum. That is a contradiction.

**Parameters (checked; `r76_threebody_naive.py`).**
- m = 0.3; ε = √(m² + s(k)²) with s(k) = k for |k| ≤ 2.6.
- g odd and C^∞, supported in |q| < κ = 0.25.
- λ = −3 (also −2.5 and −4).
- Pair plateau c(P₁₂) = 1 for |P₁₂| ≤ 0.8, with the cut at 1.0.
- Interaction legs < 1.0. At |P₁₂| = 1.0 and |q| = κ the largest leg is 0.906 < 1.0, so g is never truncated.
- Leg box 1.0, which is exactly invariant.
- Exact antisymmetric three-fermion sector on the ring's own grid (no interpolation). Hermiticity holds to 2e-16.
- **Independent cross-check** (`r76_fock_crosscheck.out`). The law was built a second time as ½ΣW a†a†aa on Slater determinants with explicit fermionic signs. It reproduces script 1's E₀ to ≤ 7e-16 at L = 90 and 120, for P = 0, 0.209 and 0.419.

**The pair sector.**
- Dimer M_b = 0.515280 at L = 300; 2m = 0.6.
- The dimer's own dispersion is exactly relativistic in this law (R7-1 checked it to 1.2e-10, `r71_bt_twobody.out`).
- The 2+1 threshold is √((M_b+m)² + P²).

**The trimer** (λ = −3; P is the same lattice point at every L):

| P | L = 180 | L = 240 | L = 300 |
|---|---|---|---|
| 0 | 0.734256054 | 0.734265439 | 0.734266071 |
| 0.10472 | 0.733704558 | 0.733714587 | 0.733713866 |
| 0.20944 | 0.732122877 | 0.732136463 | 0.732136727 |
| M(0) − M(0.10472) | 5.515e-4 | 5.509e-4 | 5.522e-4 |
| M(0) − M(0.20944) | 2.133e-3 | 2.129e-3 | 2.129e-3 |

- The trimer is bound by 0.081 below the 2+1 threshold.
- Its weight on configurations with any |P_ij| > 0.8 (the c < 1 shell) is exactly 0 for P ≤ 0.40, and ≤ 3e-15 at P ≈ 0.50.
- The drift is converged in L: L = 180–300 agree to about 1e-6. For comparison, R7-1's two-body invariant-mass error in the same law is 7.5e-7 at L = 300 (`r71_bt_twobody.out`). So the drift is 700–2800 times that floor.
- It is quadratic in P: the ratio at 2P is 3.86.
- **Fit (`r76_fit.out`).** E² = M₀² + (1 − δ)P², with δ = 0.0739 at P = 0.105, 0.0680 at 0.293, and 0.0576 at 0.503. So the trimer's limiting speed √(1 − δ) ≈ 0.962 sits about 4% below c = 1 at low P (checked; reading of "cone").
- **Coupling dependence (L = 240, spread over 0 ≤ P ≤ 0.50).** 7.3e-3 at λ = −2.5, 9.8e-3 at λ = −3, 1.65e-2 at λ = −4 (checked). Its exact power in λ was not fitted: the trimer does not exist at weak coupling.

**Scope.**
- One coupling family, R7-1's W, d = 1, fermions.
- That *every* pairwise-additive instant-form law fails is the standard expectation (Foldy-type and Coester–Polyzou statements, RECALLED), not proved here.
- The trimer test does not use K at all, so it is independent of the boost ansatz.

### 4.2 Proposition BT0 (the BT three-body box law) — proved; numbers checked

- **Definition.**
  - For a = (ij)(k), let U_a = U_ij ⊗ U_k, with generators H_a = H_ij + ε_k and K_a = K_ij + κ_k. This is R7-1's two-body law plus a free spectator.
  - B_a is the unitary that commutes with P, maps the a-centre X_a = ½{H_a⁻¹, K_a} to the free centre X₀, and identifies internal labels.
  - M_(a) = B_a M_a B_a†.
  - M_BT = M₀ + Σ_a (M_(a) − M₀); H_BT = √(M_BT² + P²); K_BT = ½{H_BT, X₀}.
- **Algebra (BT, RECALLED; algebraic, in 1+1).** [X₀, P] = i, M_BT commutes with P and X₀, and so the 1+1 algebra holds:
  - [K,P] = ½{H,[X,P]} = iH;
  - [K,H] = ½{H,[X,H]} = ½{H, iP/H} = iP.
- **BT0 claim.** Take c(P_ij) = 1 on the P = 0 region used. In 1+1 dimensions B_a acts as the identity on the P = 0 fibre. There the a-frame and the free frame are both the rest frame, q₃^(a) = k₃ = q₃^(0), and the pair-internal variable is common. Hence M_(a)|_{P=0} = H_a|_{P=0}, and
  - **M_BT = H_pair|_{P=0}, transported to every P by free boosts.**
- **Consequences.**
  - (i) The BT trimer mass equals the pairwise trimer's rest energy, 0.7342661 at L = 300, at every P.
  - (ii) The three-body term the BT law adds is H_BT − H_pair. It vanishes at P = 0. On the trimer it is E_BT − E_pair = +5.5e-4, 2.0e-3, 3.7e-3, 6.0e-3 and 8.2e-3 at P = 0.105, 0.209, 0.293, 0.398 and 0.503 (checked, `r76_fit.out`).
  - (iii) The region is box-supported (Lemma R).
- **Cluster status.**
  - The three-body BT S-matrix is cluster separable (Coester 1965, RECALLED).
  - The generators are not (RECALLED). The mechanism:
    - On "dimer(12) ⊗ particle 3", B_a reparametrizes the spectator's momentum by an amount that depends on the pair's mass. In position space it moves the far particle by a distance proportional to its separation.
    - **B_a's long reach is checked**: ‖(B_a − 1)ψ‖ stays at 0.28–0.86 as the spectator recedes to x = 20–320 (`r76_packing_range.out`, rows B).
    - So H_BT − H_a = B_aH_aB_a† − H_a keeps a non-decaying, dilation-type piece (argued from that check; H_BT − H_a itself was not computed).
  - **Hence the BT law is exact but not quasi-local.** Its three-body term has non-decaying tails. It fails the item's "faster-than-power tails" as well as generator-level separability (suggested).

### 4.3 Construction S (packed box law) — algebra proved; cluster separability RECALLED and argued; tails suggested; not checked

- **Packing (Sokolov; Coester–Polyzou; RECALLED in form).**
  - Let Ĝ_a(s), for s ∈ [0,1], generate the interpolation B_a(s). This is the B_a built with pair mass M₀ + s(M_ij − M₀).
  - Set B = T exp(i∫₀¹ Σ_a Ĝ_a(s) ds), an ordered exponential that is permutation-symmetric, so it is compatible with fermions.
  - If Ĝ_b and Ĝ_c → 0, then B → B_a.
  - Define H = B† H_BT B, K = B† K_BT B, P = Q.
- **Exact algebra — proved.** H is a unitary conjugate of the BT generators by an operator commuting with P. On the box domain, Lemma L3 applies.
- **Cluster separability — RECALLED (Sokolov; Coester–Polyzou) plus argued for this class.**
  - In cluster limit a: B_b and B_c → 1, and M_(b), M_(c) → M₀. Then H → B_a† B_a H_a B_a† B_a = H_a, and likewise for K.
  - The needed strong limits require short-range pair interactions. Our form factors are C^∞ with compact support in q, so the pair factors decay faster than any power in the pair separation (as `R7-1_report.md:152`).
  - The dilation factors grow at most linearly in the spectator distance and move a far particle by an O(1) factor of its distance, never closer.
  - So the mixed terms decay faster than any power (suggested).
- **What the three-body term is.**
  - H₃ := H − H_pair = [B†H₀B − H₀ − Σ_a(B_a†H₀B_a − H₀)] + Σ_a[B†(H_(a)BT − H₀)B − B_a†(H_(a)BT − H₀)B_a] + B† C_BT B.
  - C_BT is the connected part of the BT functional calculus: products like V_a G V_b with resolvents at negative spectral parameter.
  - Every term contains at least two different pair factors, or C_BT. The single-pair dilations cancel exactly, because B_a = e^{iG_a} for pair a alone.
- **T-risk (the one gap).**
  - That every surviving term is uniformly bounded by C_N (1 + spread)^{−N}, rather than merely tending to 0 strongly, is **suggested, not proved**.
  - Strong convergence alone allows power-law tails. For example, a smeared dilation ∫ w(λ) U_λ dλ applied to a packet at distance D has norm ~ (σ/D)^{1/2}.
  - Whether the box law is quasi-local, with faster-than-power tails, rests on this.
  - **Building block checked (`r76_packing_range.out`; d = 1, P = 0.4; pair λ = −3, κ = 0.25).** The setup and results:
    - Pair grid dq = 0.004; spectator grid 601 points; test packets are Gaussians, including near threshold.
    - (C) B_a = 1 at P = 0, to 5.5e-13.
    - (A) With the pair separated by r and the spectator at the pair, ‖(B_a − 1)ψ‖ = 0.14, 0.11, 0.032, 5.1e-4, 2.2e-5 and 4.7e-7 at r = 0, 20, 40, 80, 160 and 320. That fits exp(−c√r) with c ≈ 0.7–0.85, the Gevrey-2 class of the sstep form factor. This is far above the packet's own Gaussian tail (e^{−46} at r = 160), so it measures the operator, not the packet.
    - (B) With the pair together and the spectator at distance x, ‖(B_a − 1)ψ‖ = 0.14, 0.28, 0.86 and 0.63 at x = 0, 20, 80 and 320. B_a acts at long range in the spectator coordinate, as expected.
    - So the ingredient Sokolov's argument needs (B_b → 1 as the b-pair separates) falls off faster than a fixed power over r = 80–320 in this instance (a fit, not a proof). The threshold risk below is not seen there.
    - This checks one operator. It does not check H₃.
  - **A concrete way the T-risk could happen (suggested; partly tested above).**
    - B_a = Σ_μ ∫dq |q⟩⟨q|χ_μ⟩⟨χ_μ| ⊗ (R_{M₀(q)}⁻¹R_μ). Here R_μ is the change of variables from k₃ to q₃, the spectator's momentum in the rest frame of (cluster of mass μ) + spectator. This is the standard identification, and the one under which BT0 holds.
    - So B_a is an operator-valued function of M_ij that also integrates over the pair's continuum spectrum. Its decay in the pair separation is set by the smoothness in μ of the scattering data, including at the threshold μ = 2m.
    - R7-1's Lemma Sm avoided threshold singularities by writing √(M²+P²) − √(M₀²+P²) as a resolvent integral at negative spectral parameter (`R7-1_report.md:148-153`). That trick does not carry over directly: a reparametrization R_μ does not continue to complex μ as a bounded operator.
    - If the threshold behaviour is only finitely smooth, B_a − 1, and with it H₃, could have power-law tails in the pair separation.
    - Script 4 checks only the pair-separation decay of B_a, which came out super-polynomial. The mixed terms in H₃ were not computed. They are the first thing to settle.
- **Boost form.**
  - K = ½{H, X} with X = B†X₀B, a dressed centre that tends to X_a in each cluster limit.
  - Whether K is a first moment of a quasi-local density (B1 Theorem S's form) is not addressed. It plausibly holds up to quasi-local terms if H₃ is quasi-local (suggested).
- **Numerical check.** None for Construction S. B_a acts along curves of constant rest-frame spectator momentum, which are not grid lines of the ring. A faithful check needs spectral interpolation on a two-dimensional fibre with oscillatory e^{−ik₃D} test states. It did not fit the time. It is the cheapest next step (§9).

---

## 5. What fails or stays open (quantified where possible)

1. **Pairwise H.** Fails rep-independently (checked, §4.1). The size of the needed three-body energy is 5e-4 to 8e-3 at 0.1 ≤ P ≤ 0.5 on the trimer, for the λ = −3 law.
2. **BT H.** Exact, but its three-body term is long-ranged (dilation-type). Generator separability fails; the S-matrix clusters for N = 3 (RECALLED).
3. **Packed H.**
   - Exact (proved) and separable (RECALLED and argued).
   - The tails are the open item (T-risk).
   - Not checked numerically.
4. **N ≥ 4 in one second-quantized law.**
   - The three-body term acts on every triple in the N ≥ 4 sectors. Closure then needs four-body packing terms, and so on: a tower of n-body terms.
   - Coester–Polyzou state that the N-body strength decreases rapidly with N (VERIFIED-CITE, abstract level).
   - Whether the lattice law, with all orders included, stays finite per site and quasi-local is OPEN.
5. **Inherited unchanged from R7-1 §5:**
   - the rapidity budget and leakage;
   - the inert edge sector carrying the −1 anomaly;
   - loops and pair creation (R7-5);
   - gauge fields;
   - the local lapse.

## 6. Reading against the FIXED readings (`TESTS.md:3391-3394`)

- **PASS — not met as registered.** The clauses run as follows:
  - "explicit three-body box law": met in recipe form. Construction S is explicit up to the spectral calculus of the pair mass operators.
  - "exact algebra": proved.
  - "cluster separability": RECALLED theorem plus argument.
  - "checked": not met.
  - "faster-than-power tails" (the item's construction clause, `TESTS.md:3389`): suggested only.
- **FAIL — not available.**
  - No no-go was found for the item's class. The continuum construction exists and transplants (Lemma L3).
  - The only proved-and-checked negative, Theorem N, covers the *pairwise* class, which the item does not restrict to. It is recorded as a bounded negative for that class.
- **INCONCLUSIVE — worker reading, leaning PASS.**
  - The registered question "can the interacting algebra close beyond two bodies on a lattice?" is answered **yes in the algebra**, at the price of three-body terms in H.
  - Generator-level separability holds by the cited theorem.
  - It is **open in quasi-locality** (T-risk) and **unchecked numerically**.
- **Bounded negative to record (checked; worker reading).** In d = 1, R7-1's pairwise BT box law has a trimer with δ ≈ 0.074, so no boost of any form exists for it. Three-body terms in H are forced.

## 7. Strong-word check

- **"No boost of any form"** (Theorem N) assumes H-gen's local flow on trimer packets. Without integrability or a local flow, the algebra on a domain alone does not formally force μ(P) to be constant.
- **"Exact"** means operator identities on 𝒟_R for the stated region, as in R7-1. On the full Fock space the relations fail at the box edge.
- **"Converged"** means the L = 180–300 values agree to about 1e-6 on the same lattice P. This is a finite-L statement.
- **"Forced three-body terms"** is checked for R7-1's W only, at λ ∈ {−2.5, −3, −4}. It is not a theorem about every pairwise law.
- **"Instant form forced"** depends on the reading e^{iP} = T and ‖P − Q‖ < π (H-P).
- **"Light-front pairwise closure for every N"** is proved only as the algebra, plus strong limits under short-range V. Not run.
- **Cluster separability of Construction S** rests on Sokolov and Coester–Polyzou (RECALLED for content; citations verified). Not re-proved here; not checked.
- **Nothing here gives a graviton**, a local stress tensor for interacting three-body matter, or loop control.

## 8. Price (named, not adopted)

- **Everything R7-1's price already names** (`R7-1_report.md:274`):
  - non-quasi-analytic form factors;
  - a frame-fixed box;
  - an inert edge sector;
  - form-factor, not point-local, interactions.
- **Plus:**
  - a tower of many-body interaction terms (three-body at least; n-body for N ≥ n in one law) generated by packing operators;
  - these terms are "connected" by construction, but their quasi-locality is unproved;
  - instant-form kinematics is forced by the lattice translation, so the cheap 1+1 pairwise forms (light-front, Ruijsenaars–Schneider) are unavailable.
- **No new axiom text.** Admissibility does not fix the dynamics (`MINIMAL_AXIOMS:114-125`). The graded-composition question stays as R6-1 left it (`C5_R6-1_referee_verdict.md:17`).

## 9. For the referee

Check, in order:

1. **Theorem N's numerics.**
   - Rerun `python3 r76_threebody_naive.py sym=fermi lam=-3 kap=0.25 pi1=0.8 pi2=1.0 Ls=180,240,300` (about 10 s).
   - Confirm three things: the shell weight is 0 on the plateau; every leg on supp g stays below the interaction box; the drift is L-independent.
   - `r76_fock_crosscheck.py` gives an independent second-quantized build. It agrees to 7e-16.
2. **The implication from a non-constant μ(P) to "no K".** Check it under H-gen's local-flow hypothesis.
3. **Proposition BT0.** Check that B_a = 1 on the P = 0 fibre, and so M_BT = H_pair(0).
4. **Lemma IF**, including the spectral step P = Q.
5. **The T-risk.** Do the packed three-body terms have faster-than-power kernels?
   - The cheapest decisive numeric is the two-pair distinguishable version (12 and 23 interacting) at fixed P on a spectral grid. Compute ‖(H − H_a)T_Dψ‖ against D for the packed law, and the non-decay for BT.
6. **The reading.** If a recalled-and-cited separability theorem plus a proved transplant is judged to meet "checked", the strongest reading would be PASS. The tails would stay suggested, and N ≥ 4 open.
