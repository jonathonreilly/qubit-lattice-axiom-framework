## Lane F report: ticked steps and net chirality

All scripts are in `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A2/`. I did the derivation and every run myself, with no subagents.

### 1. Question

Suppose the change between records came in ticked steps:
- one unitary per tick;
- local with a strict light cone;
- translation-invariant;
- covariant under the 24 proper cubic rotations, acting on lattice and qubit together.

Can the single-particle step operator U(k) on the Brillouin 3-torus then have Weyl nodes (quasi-energy band touchings) with nonzero net chirality? And how does net chirality relate to W3 = (1/24π²)∫_{T³} Tr[(U⁻¹dU)³]?

### 2. Answer

**No. Grade: EXACT, within the class "translation-invariant, finite content per site, strictly finite range, reversible (unitary) single-particle step".**

- **What holds per quasi-energy.** At every quasi-energy ε, the net chirality of the touchings, plus the Chern numbers of any Fermi surfaces at ε, equals −W3 (sign is my convention). The 2-band case is EXACT; the general case is ARGUED.
- **Strict locality alone forces W3 = 0.** The proof is self-contained for every circuit built from "content-set shifts plus local mixing". For general strictly local steps it uses a standard theorem of algebraic K-theory.
- **So doubling persists at every quasi-energy, exactly as for continuous-time lattice Hamiltonians.**
- **Proper-cubic covariance plays no part in this.** It does two other things:
  - it forces the only other index a step can carry, the net flow ("conveyor"), to vanish;
  - for a 2-band step with spin-1/2 soldering, it pins band touchings at all 8 high-symmetry momenta.
- **Two relaxations do allow W3 ≠ 0, and both break a stated condition:**
  - (a) A reversible step with exponentially decaying tails (no strict light cone). I give a 2×2 example covariant under all 24 rotations, with W3 = −1 and a single Weyl node at k = 0. No continuous Hamiltonian can produce it within a tick.
  - (b) A strictly local but non-reversible map (point-gap winding).

### 3. Derivation

**Conventions.**
- U(k) = Σ_v A_v e^{ik·v}. Eigenvalue e^{−iε} defines quasi-energy ε.
- Node chirality χ := sign det(∂h_a/∂k_j), where near the node the step acts on the two touching bands as e^{−iε}e^{−ih(q)·σ}.
- W3 is the integral above, oriented by dk_x∧dk_y∧dk_z.

**D1. Algebraic setup. (EXACT)**
- With z_j = e^{ik_j}, a strictly local translation-invariant step is a matrix of Laurent polynomials over R = ℂ[z₁^±, z₂^±, z₃^±].
- Its inverse U† = Σ A_v† z^{−v} is also a Laurent polynomial. UU† = 1 holds on T³, so it holds identically.
- Hence U ∈ GL_n(R), and det U is a unit of R: det U = c·z^m.
- The same holds for any enlarged unit cell, so superlattice blocking changes nothing below.

**D2. Node–winding relation, 2 bands. (EXACT)**
- Assume det U has no winding; this is automatic under covariance (see D8). Then Ũ := e^{iφ}U ∈ SU(2) ≅ S³ is globally defined.
- Band touchings are exactly the points where Ũ = +1 ("in-phase") or Ũ = −1 ("anti-phase").
- The degree of Ũ can be counted over either regular value. Near Ũ = ±1, write Ũ ≈ ±e^{−ih·σ}. The chart orientation flips between the two hemispheres, and that flip cancels the sign from h = −b at −1.
- So both classes give the same sum: **Σ_{Ũ=+1} χ = Σ_{Ũ=−1} χ = −W3** in my conventions (sign CHECKED below).
- **This is how ticks differ from a continuous generator.** For a continuous generator H = h·σ, zeros of h net to zero (Poincaré–Hopf). On the quasi-energy circle there is no global "upper/lower band". Berry-flux bookkeeping then only forces the two classes to be equal, not zero, and W3 is their common value.

**D3. General n bands. (ARGUED, careful sketch)**
- Pick a quasi-energy ε hit only at isolated type-I nodes. Cut out small balls around them. On the complement, U = e^{−iH_ε} with a continuous branch-cut log.
- The transgression identity ∂_s Tr(U_s⁻¹dU_s)³ = 3 d Tr(U_s⁻¹∂_sU_s (U_s⁻¹dU_s)²), applied to U_s = e^{−isH_ε}, turns ∫Tr(U⁻¹dU)³ into a sum of boundary terms.
- Near each node, H_ε → ε + 2πP₋(q̂). Each boundary term is then the winding of e^{−2πisP₋} on S¹×S², which is ±Ch(P₋) = ±χ.
- Result: Σ_{nodes at ε} χ = −W3. If Fermi surfaces sit at ε, add their Chern numbers (the tick analog of "Fermi-surface Chern numbers sum to zero").

**D4. A continuous generator forces W3 = 0. (EXACT)**
- Suppose U(k) = T exp(−i∫₀¹H(k,s)ds) with H continuous on T³×[0,1]. The partial evolutions U_t connect 1 to U, so W3 = 0. This includes time-dependent and quasi-local generators.
- Suppose U has a quasi-energy gap anywhere. A continuous log then exists, so W3 = 0.
- So **W3 ≠ 0 means: no quasi-energy gap anywhere, and no Hamiltonian generation within the tick.**

**D5. Shift-and-mix circuits have W3 = 0. (EXACT, self-contained)**
- W3 is additive under pointwise products. This follows from the Polyakov–Wiegmann identity: Tr((fg)⁻¹d(fg))³ = Tr(f⁻¹df)³ + Tr(g⁻¹dg)³ − 3d Tr(f⁻¹df ∧ dg g⁻¹).
- A factor depending on k through a single coordinate has A = f⁻¹df ∝ dk_j, so A∧A = 0 and W3 = 0.
- Every layer of the circuits in question is a product of such factors:
  - a content-set shift (each content moves by its own vector v_α) is diag(e^{ik·v_α}) = D_x(k_x)D_y(k_y)D_z(k_z);
  - a translation-invariant layer of disjoint local gates is D(k)†·G·D(k), with D diagonal and G constant.
- Hence **any depth, any internal dimension, any layer pattern gives W3 = 0**. This answers "look for a step built from content-set shifts plus local mixing with W3 ≠ 0": no such step exists, at any range.

**D6. Every strictly local step has W3 = 0. (EXACT, via a standard theorem)**
- SK₁(R) = 0. This follows from the fundamental theorem of K-theory for regular rings, K₁(A[t^±]) = K₁(A) ⊕ K₀(A), together with K₀(ℂ[z₁^±, z₂^±]) = ℤ (Quillen–Suslin–Swan). By induction K₁(R) is generated by the units c, z₁, z₂, z₃.
- So U·diag(c⁻¹z^{−m}, 1, …) ⊕ 1_p is a product of elementary matrices e_ij(f).
- The family e_ij(tf), t ∈ [0,1], is a homotopy to 1 through GL-valued maps.
- Tr(g⁻¹dg)³ is closed on GL_N(ℂ), so W3 is invariant under that homotopy and stable under adding identity blocks; the abelian factor contributes 0. Hence W3[U] = 0.
- These K-theory results are standard mathematics used as a lemma, not physics content. The topological analog (top Bott class present in K¹(T³) = ℤ⁴, absent algebraically) is what makes polynomial steps different from smooth ones.

**D7. Corollaries. (EXACT)**
- Strictly local reversible ticks keep the per-quasi-energy balance of D3 at zero: doubling persists.
- A sequence of different ticks U_T⋯U₁ still has W3 = 0 (by additivity).
- If some step Q has W3 ≠ 0, every strictly local unitary U′ satisfies max_k ‖U′(k) − Q(k)‖ = 2, the largest possible distance. Otherwise U′Q⁻¹ never has eigenvalue −1, has a continuous log, and W3 would match. So a chirality-carrying step cannot even be approximated uniformly by ticked strictly local ones.

**D8. Flow and covariance. (EXACT)**
- For n ≥ 2, homotopy classes of maps T³ → U(n) are labelled by (m, W3) ∈ ℤ⁴, where m is the vector of det windings (the "conveyor" flow). This is standard topology.
- det U(Rk) = det U(k), so m transforms as a vector. The 180° rotations force m = 0.
- A covariant strictly local step is therefore null-homotopic. Topologically it is indistinguishable from a step generated by a continuous (quasi-local, not star-local) Hamiltonian.
- **Consequence for the clause's word "continuously":** in this single-particle setting it sets aside no chirality-carrying index that strict locality plus covariance had not already excluded. Campaign 7's flagged sentence ("continuity sets aside index-carrying discrete steps, which bear on chirality") should be narrowed accordingly. In 3D, the index that discrete steps add is net flow, which covariance excludes; the chirality index is excluded by strict locality alone.

**D9. Readings of "one qubit per site". (EXACT)**
- **(a) The qubit's two possibilities as empty/occupied, with the step conserving the number of occupied sites.** The one-excitation sector is a scalar walk with |u(k)| = 1. Then u is a unit of R, so u = c·z^m: a rigid conveyor. Covariance forces m = 0, so **nothing moves**: the excitation only gains a phase.
- **(b) One fermion mode per site with pairing (2 Majoranas).** The 2×2 step O(k) satisfies O(−k)* = O(k).
  - Complex conjugation leaves W3 unchanged; k → −k flips it. So W3 = 0 for every such step, even a quasi-local one.
  - Nodes pair as (k, ε, χ) ↔ (−k, −ε, −χ).
- **(c) A walker carrying the qubit, or more content per site.** W3 = 0 by D6.

**D10. 2-band steps with spin-1/2 soldering.**
- (EXACT) Every high-symmetry point (Γ, X, M, R) has a stabilizer whose spin-1/2 lift acts irreducibly. By Schur's lemma, U ∝ 1 there: touchings are pinned at all 8 such points. At Γ and R the node is isotropic, h = λq.
- (EXACT) A single-layer covariant 2-band step with nearest-neighbour hops only is constant:
  - the e^{2ik_z} coefficient forces A_{e_z} = αP_↑;
  - the e^{i(k_x−k_y)} coefficient then equals (|α|²/2)·1, so α = 0.
  - The same holds with an extra rotation-invariant two-level label.
- (ARGUED; CHECKED on 3 maps) Parity rule: W3 ≡ n₋ mod 2, where n₋ counts the high-symmetry points with Ũ = −1, weighting Γ and R by 1 and the X and M classes by 3. Off-symmetry nodes come in even-size orbits with equal chirality. Hence a strictly local covariant 2-band step needs even n₋.

**D11. Reflections. (EXACT)**
- W3 is a pseudoscalar: the mirror image of a step has −W3. Reflection covariance would force W3 = 0.
- The axioms ask only for proper rotations, and those allow W3 ≠ 0 (E3 below, covariant under all 24). For strictly local steps the point is moot (D6).

**D12. Relaxations that permit W3 ≠ 0. (EXACT for the examples)**
- **E3: quasi-local, reversible.** U = (d₄ + i d·σ)/|d|, with d = (sin k_x, sin k_y, sin k_z) and d₄ = 2 − Σcos k_j. W3 = −1, covariant under all 24 rotations with spin-1/2 soldering. Its hopping amplitudes decay exponentially (it is real-analytic). By D4 and D6 it is neither Hamiltonian-generated nor strictly local.
- **E4: strictly local, not reversible.** M = i d₄ + d·σ. Here M⁻¹ is not strictly local, and W3 = +1. The obstruction in D6 is specifically that the step and its inverse are both strictly local.

### 4. Checks

Every run used `nice -n 10`, the four thread caps set to 1, and a 60 s alarm (numpy 2.4.4, scipy 1.17.1). Wall times were 0.2 to 45 s.

**Memory cap breach.** `run5d_gn.py` peaked at **510 MB for about 8 s**, over the 300 MB cap; I underestimated its Jacobian temporaries. `run2_E3.py` peaked at 301 MB. All other runs stayed at or below 270 MB.

**Core code.** The W3 integrand of a strictly local unitary is a trig polynomial of degree ≤ 6r per axis, so the grid mean is exact once N > 6r.

```python
def w3_from(U, dU, Uinv):                 # U:(M,n,n), dU:(3,M,n,n) on an N^3 grid
    A = [Uinv @ dU[j] for j in range(3)]
    f = np.einsum("mij,mji->m", A[0], A[1] @ A[2] - A[2] @ A[1])
    return np.pi * f.mean()               # = (1/24pi^2) Int Tr(U^-1 dU)^3
# 2-band nodes: U = u0 - i b.sigma, b_a = (i/2) Tr(sigma_a U); Newton on b=0 from a 24^3 grid
# chi = u0 * sign det(db_a/dk_j)
E1: U = expm(-i kx sx) @ expm(-i ky sy) @ expm(-i kz sz)
E3: U = (d4*1 + 1j*d.sigma)/|d|;   E4: M = 1j*d4*1 + d.sigma
E2 (12x12, content = direction v in {±e_j} x spin): U = S(k) @ G @ expm(-i*beta*Hel),
    S = diag(e^{ik.v}) (x) 1_2,  G = (2|s><s|-1) (x) 1_2,  Hel = sum_v |v><v| (x) v.sigma   (beta = 0.7)
covariance: max|U(Rk) - D(R)U(k)D(R)^+| < 1e-10 at 40 random k, D = P(R) (x) spin-1/2 lift
```

**Results.**

| Step | Strictly local | Covariant: proper / improper | W3 | Nodes and net χ |
|---|---|---|---|---|
| E1, 2×2 | yes | 4/24 / – | ≤ 1.2e-15 for N = 8–24 | 16 nodes. In-phase: 4 at points with all k_j ∈ {0, π} (χ = +1) and 4 at (±π/2)³ (χ = −1), net 0. Anti-phase: same pattern, net 0. |
| E2, 12×12 (≤ 1 site per tick, chiral) | yes | 24/24 / 0/24 | ~1e-17 (one and two layers) | not analysed |
| E3, 2×2 | no (tails) | 24/24 / 0/24 (mirror maps U → U†) | −1.0023, −1.00014, −1.00000055, −1.0000000021, −1.0000000000 for N = 12, 16, 24, 32, 48 | single anti-phase node at Γ (χ = +1); 7 in-phase nodes at X, M, R summing to +1 |
| E3 mirror | no | – | +1.00000000 | net −1 / −1 |
| E4, 2×2 | yes, but not unitary | – | +1.00000000 (N ≥ 32) | – |

- **Sign convention:** net χ = −W3 in all three cases.
- **Additivity:** W3[E3·E1] = −1, W3[E3²] = −2, W3[E3·mirror] = 0.
- **E3 hopping decay:** largest ‖A_v‖ at graph distance r = 0, 4, 8, 12 is 1.0, 8.8e-3, 5.4e-4, 2.7e-5 (roughly e^{−0.8 per site}).

**Adversarial search for a strictly local 2×2 unitary with W3 ≠ 0** (`run5*`). I minimized F = Σ‖UU† − 1‖² on the exact (4r+2)³ grid.
- **Range r = 1, random seeds (Levenberg–Marquardt with analytic Jacobian):**
  - 9 seeds reached exact unitarity (defect ≤ 3e-14); **all have W3 = 0.0000**.
  - One seed stalled at defect 6.5e-3 with W3 = −1; the rest stayed far from unitary.
- **Range r = 1, seeded at truncated E3:** stuck at F = 3.6704e-2 with W3 = −1.
- **Range r = 2, seeded:** F fell slowly from 4.8e-8 (1e4 evaluations) to 5.0e-9 (1.1e5), 3.84e-9 (2.2e5) and 3.37e-9 (3.2e5). Sup defect 4.7e-6; W3 stayed −1. A second-order polish converged linearly, not quadratically.
- **Range r = 3, seeded:** F = 3.6e-8 with W3 = −1 after the evaluation budget.
- **Status: CHECKED, consistent with the theorem but not decisive.** At r = 2 the numerics cannot certify a positive defect floor; the theorem implies one.

**Search for covariant 2×2 strictly local steps** (`run6`, spin-1/2 soldering):
- r = 1 (20 seeds) and r = 2 (17 seeds): **no nontrivial exact solution**. Exact solutions were constants only.
- Best nontrivial near-solutions at r = 2: F = 4.1e-5 with W3 = +2 (n₋ = 6), and F = 1.4e-4 with W3 = −3 (n₋ = 5). Both match the parity rule; E3 does too (n₋ = 1, W3 = −1).

**Should be run (not run, over budget):** `python3 run6_cov2x2.py 3 40` and `… 4 40`, to probe nontrivial covariant 2-band steps at range 3–4. Expect minutes.

### 5. Real-physics match

- **What it implies.** If records formed only at ticks (I1) and the change between them were reversible with a strict one-site reach (I2), then the free-particle content keeps lattice fermion doubling at every quasi-energy, the same obstacle lattice gauge theory faces. To match observed single-handed fermions, ticks alone are not enough. Some other ingredient is needed; each candidate is open:
  - interactions;
  - boundaries or defects, such as edges of recorded regions;
  - the separate-factor chirality constructions.
- **What would falsify it.** An explicit translation-invariant, strictly local, reversible step on Z³ with a single uncompensated Weyl node at some quasi-energy. That would contradict D6, and with it established algebraic K-theory.
- **Scope relative to the landed no-go.** The landed chirality no-go forbids only the hybrid identification γ_CL = Γ_χ. This result is independent of it: it neither extends nor relies on that no-go, and it is itself confined to the class stated in §2.

**Comparators (not adopted; recalled, not re-checked):**
- Higashikawa, Nakagawa & Ueda (PRL 2019, "Floquet chiral magnetic effect") and Bessho & Sato (PRL 2021, "Nielsen–Ninomiya theorem with bulk topology") relate Floquet Weyl chirality to a bulk winding of the Floquet operator, consistent with D2–D3. I have not checked whether any of their examples are strictly local; D6 says none can be.
- Chen–Mazaheri–Seidel–Tang (2014), Dubail–Read (2015) and Read (2017) use the K₀ version of D6 to show strictly local flat Chern bands are impossible.
- Known lattice escapes from doubling give up strict locality for exponential locality. Examples are overlap/Ginsparg–Wilson operators; I recall a no-go for ultralocal Ginsparg–Wilson operators (Horváth 1998), which parallels D6.
- D'Ariano–Perinotti's 3D Weyl QCA, as I recall its form, is a product of single-direction factors, hence W3 = 0 by D5.

### 6. Open edges and next steps

1. **Interacting steps.** Single-particle W3 does not exist there. Whether an interacting, strictly local, reversible step with on-site U(1) can carry a 3+1D chiral anomaly is OPEN. Nontrivial 3D interacting steps exist in the literature (comparator), but their relation to chirality is unknown here.
2. **Anomaly reading (ARGUED).** W3 plays the role of the anomaly coefficient for tick dynamics. In 1+1D the flow survives strict locality because it is carried by a unit z^m; in 3+1D the chirality class has no polynomial representative.
3. **Record backgrounds (I5, local ticks).** These break translation, so D6 does not apply directly. Define a real-space W3 and test whether record patterns can bind chiral modes. Net flow along record lines is not excluded once covariance is locally broken.
4. **Non-reversible pieces.** Evolution conditioned on no record forming is non-unitary. Strictly local non-unitary maps can carry point-gap winding (E4). Whether anything Weyl-like follows is OPEN, and I doubt it in the standard sense (ARGUED).
5. **Quasi-energy vs energy, and which quasi-energy matters.** Ticks have only quasi-energy. In E3 the single node sits at quasi-energy π, and a global −1 per tick moves it to 0. A global phase per tick is invisible at fixed particle number, so the "physical" quasi-energy is not fixed by the step. It would have to come from many-body filling or record conditions (OPEN).
6. **Next runs.** The covariant 2-band search at range 3–4. A proof or counterexample for the parity rule with degenerate touchings.

### 7. Plain-language summary

If the change between records happened in ticks, and nothing could travel more than one site per tick, could the moving possibilities carry a built-in twist (a handedness) without an opposite-twisted partner? They cannot: with a strict one-site reach and reversible ticks, every twist comes paired with an opposite twist, exactly as with smooth change. An unpartnered twist appears only if each tick leaks a tiny amount past the next site, or if the tick cannot be undone, and both break the rules assumed here. The rotation rule is not what causes the pairing; it separately forbids a steady one-way drift through the grid. So ticks by themselves do not give the grid a handedness; that would have to come from how records form, from interactions, or from the edges of recorded regions.