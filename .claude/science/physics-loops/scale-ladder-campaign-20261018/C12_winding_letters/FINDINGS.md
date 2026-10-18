# C12 findings: W₃ ≠ 0 is allowed in the declared class; an explicit quasi-local letter gives a single isotropic Weyl node with no doubler; finite range forces W₃ = 0

Provenance: a worker of the same model family. **Unchecked.** Saved by the supervisor from the hand-back (the worker's file write was blocked). `c12_runner.py` sections 0–2 copy the wt-lanes C11 model build verbatim, with nothing imported. **TOTAL: PASS=35 FAIL=0** (462 s, ≤ 3 threads). Scratch is in the session scratchpad `c12/` (`d6.py`, `d6probe.py`, `cert.py`).

**Supervisor's prior-art note (unchecked recollection).** Evading fermion doubling by giving up strict locality is the classic Nielsen–Ninomiya loophole: SLAC-type non-local derivatives evade it. For Floquet unitaries the net chirality equals W₃ (Bessho–Sato) and can be nonzero for smooth maps. So the C12 construction is the Floquet analogue of that loophole, now O-covariant in this model. Whether S6 (finite range ⇒ W₃ = 0) is known in the quantum-walk/QCA literature was not checked.

## Question

The class is C¹ translation-invariant unitaries U(k) on C¹² with U_R U(Rᵀk+πλ_R) U_Rᵀ = χ(g)U(k), χ ∈ {A1, A2}.
1. Is W₃ ≠ 0 allowed by symmetry?
2. If so, can a letter with W₃ ≠ 0 be built?
3. Does such a letter let a step evade the doubling obstruction?

## Symmetry analysis

- **S1 (exact): O covariance does not constrain W₃.** Each k ↦ Rᵀk+πλ_R is a rotation about k*, with det = +1. Conjugating by U_R, the projective sign and the character χ all leave W₃ unchanged.
- **S2 (exact): sign rules.** W₃(Uᵀ) = W₃(U⁻¹) = W₃(U(−k)) = −W₃(U), and W₃(U*) = W₃(U(Rᵀk)) = +W₃(U).
- **S3: I·K.**
  - The hopping family has an I·K-type real signed inversion W with W² = −1 (2 sign solutions).
  - I·K is not part of the declared class, and the letters do not share one I·K type:
    - S, S², A0 and D± are "Θ-even" (W U* Wᵀ = U);
    - exp(iθR_L) and exp(iθH_on) are "Θ-odd" (W U* Wᵀ = U⁻¹);
    - R_L and Rt are both.
  - If every letter is Θ-odd, then W₃ = 0 for every word (exact). Θ-even imposes nothing.
- **S4 (exact): O_h would force W₃ = 0.** S is covariant up to a phase under all 24 improper lifts, and improper covariance acting unitarily would force W₃ = 0. The declared class is O only.
- **S5 (exact): the 1D windings of det U vanish**, since they form an O-invariant vector. W₃ is the only K¹(T³) datum left.
- **S6 (new; exact given standard algebraic K-theory, recalled, not re-verified): finite range forces W₃ = 0**, in any dimension and with no symmetry.
  - Statement: if U(k) has Laurent-polynomial entries and an inverse of the same kind, then W₃(U) = 0.
  - Proof sketch:
    1. K₁(C[Z³]) = C^× ⊕ Z³ (Bass–Heller–Swan/Quillen; Quillen–Suslin–Swan for K₀).
    2. So SK₁ = 0, and U ⊕ 1 = diag(det U, 1, …)·(product of elementaries).
    3. Each elementary e_ij(f) is homotopic to 1 through e_ij(tf).
    4. Hence W₃(U) = W₃(diag(det U, 1, …)) = 0.
  - Also exact: W₃ = 0 for any T exp(−i∫H(k,t)dt) with H continuous, including exp(iH).
  - Novelty not checked.
- **Verdict.**
  - W₃ ≠ 0 is allowed in the declared class.
  - Θ-odd I·K, O_h, or finite range would each force W₃ = 0.

## Construction

D_b(k) = 1 − P_b + n̂₄(q)P_b + i Σ_i n̂_i(q) D_b τ_i^{(b)} D_b†, with q = k − k*, n = (sin q, m + Σ cos q), n̂ = n/|n| and m = 2. Any m ∈ (1,3) gives the same class.

- **Covariant** (exact given F1, F3, F4): D_b is k-independent and O-invariant, τ is the T1 frame, and sin(Rᵀq) = Rᵀ sin q for signed permutations. Covariance error 6e−16; unitarity, periodicity and the analytic derivative were also checked.
- **Analytic:** |n| ≥ 1 at m = 2.
- **Θ-even.**
- **Exponentially local, not finite range** (as S6 requires).
- **W₃ = ±1 exactly.** τ is unitarily equivalent to the Pauli triple, and n̂ = −e₄ has the single regular preimage q = (π,π,π).
  - The numerical W₃ is 0.96571 (N = 8), 0.9998587 (N = 16) and 0.99999945 (N = 24), identical to the SU(2) Pauli control.
  - W₃ = 0 at m = 4.
  - Additivity checks: W₃(D₊D₋) = 2, W₃(D₊D₊⁻¹) = 0, W₃(A0D₊A0) = 1, W₃(D₊S) = 1.
- **Not parameter-free:** m is a parameter, though the topology is constant on (1,3).

## Consequences

- **Q1 (exact, plus numerics): the one-letter step D_b reaches E = π only at −k*.**
  - The complement of D_b is frozen at 1, and e^{±iθ} = −1 only at q = (π,π,π) ≡ −k*.
  - The node is an isolated 2-fold D_b level, so by the C11 lemma it is an untilted isotropic cone, with speed 1/(3−m) = 1 and FHS charge −1.
  - **So the B20 criterion is met: a single Weyl node, no doubler.**
  - D₊D₋ at E = π is 4-fold at −k*, with equal speeds and the same chirality (charge −2).
- **Q2 (exact two-band argument, plus numerics): the Bessho–Sato-type bookkeeping holds in this example.**
  - The same block has 7 nodes in its E = 0 gap, with net lower-band charge −1, equal to the π node's −1.
  - Their speeds are 1/5, 1/3 and 1, so E = 0 fails the one-speed criterion.
- **Q3: steps with S fail.**
  - **Screen:** 342 cyclic word classes of length ≤ 3 in {D±^{±1}, S^{±1,±2}, R_L, Rt, A0, C± = 1−2P_{D±}}, giving 758 (word, E) pairs.
    - Θ-even words have D± levels at E ∈ {0, π} only.
    - 115 were clean on 12³, and 10 were "one-speed clean" at N = 20.
  - **Mid-run correction.**
    - D₊S⁴ and D₋S⁻⁴ (speed |1 + 4√2/3| = 2.8856, matching C11 additivity) looked clean at N = 20. On a 40³ grid they reach E = π at generic points with multiplicity 2–4.
    - **At E ∈ {0, π} the det-sign Fermi-surface test cannot see Kramers-paired crossings. Do not use it there for Θ-even words.**
    - The inverse words were not tested at 40³.
    - Words with R_L or Rt and S have 6- or 12-fold levels at +k* with many speeds.
  - **Result:** the only passing steps found are D_b^{±1} and D₊^{±1}D₋^{±1}. The step D_b alone is exact.
- **Q4 (grid evidence only): robustness.** In exp(iεH₁)·D₊·exp(iεH₂) with generic O-symmetric H and ε = 0.15, the node moves to E′ but stays a single isotropic one-speed cone of charge −1, reached nowhere else on the grid (4/4 samples). No certificate.
- **Bottom line.**
  - In the declared C¹ class, the doubling obstruction for one-speed steps is **false**: D_b is a counterexample.
  - For finite-range letters, exp(iH) letters, or any continuous-time-generated step, W₃ = 0 is exact (S6), and the obstruction rests only on Bessho–Sato.
  - So the obstruction is a **locality** statement, not a symmetry statement.

## Status

- **Exact:**
  - S1–S5;
  - S6, given the cited K-theory;
  - D_b covariance and |W₃| = 1, given F1, F3, F4;
  - Q1's single node;
  - Q2's two-band bookkeeping.
- **Numerical:** W₃ integrals, speeds, FHS charges, the screen, Q4 and the 40³ correction.
- **Conditional:** net chirality = W₃ for general steps (Bessho–Sato).
- **Weak runner lines:** D5 (records only that the classification ran) and C1 (an ad hoc 0.35 threshold; illustration).
- **Not claimed:** physical identification; admissibility of quasi-local, non-finite-range letters as QCA steps; novelty of S6.

## Open

1. **A premise decision for the owner: must letters be finite range?** If yes, S6 makes W₃ = 0 exact for every step. If quasi-local letters are allowed, the obstruction fails (D_b).
2. A rigorous certificate for the Q4 perturbed steps.
3. Θ-even finite-range words at E ∈ {0, π}: where the compensating Kramers point nodes are forced to sit.
4. Independent re-derivation of S6; a check of D_b on a different build.
