**Check of LW2_REFEREE.md closures RC-T3b, RC-G3b, RC-G3c, RC-4.2, RC-7.1, RC-I1g.** One check by Codex gpt-6-astra at low effort, read-only, on the laptop, 2026-11-08T23:07:45Z. Template `~/toe-lap/tmpl/check_lw2rc.txt`. Its final message follows unchanged.

The six conclusions survive in the stated cube-face and chain-layer settings, with the repairs below. **RC-G3c does not handle nonzero θ without cube-face factorization.** Both kernel proofs establish the needed sup-norm convergence, but omit an explicit reality argument.

Read-only check. No files changed. No git commands ran. I checked the requested closure text and its cited premises, including GB1ISO’s factorization and kernel bounds. I did not assess other reviewers’ verdicts.

**1. RC-T3b**

| Step | Status | Check |
|---|---|---|
| 1. Choose four plaquettes through one link. | CORRECT | On `Z³`, each has a link absent from the other three. |
| 2. Form the quaternion Gram entries. | CORRECT | The entries are polynomial multipliers in finitely many link algebras. No discontinuous multiplier is needed. |
| 3. Establish gauge invariance. | CORRECT | All based holonomies undergo the same conjugation. Quaternion inner products are preserved. |
| 4. Set the Gram determinant to zero. | CORRECT | Five vectors in `R⁴` have a singular Gram matrix, pointwise. |
| 5. Use independent link parities. | CORRECT | Each chosen parity negates exactly one holonomy. It is itself gauge invariant. |
| 6. Apply a character. | CORRECT | Conjugation invariance forces every off-diagonal Gram entry to have character value zero. Diagonal entries have value one. |
| 7. Obtain the contradiction. | CORRECT | Multiplicativity gives `0 = det I₅ = 1`. The argument works in either stated region-algebra convention. |

VERDICT RC-T3b: holds

**2. RC-G3b**

The first eight rows check section 3.1, which RC-G3c also uses.

| Step | Status | Check |
|---|---|---|
| 1. Reduce to one cube. | CORRECT | GB1QL’s cube-face family partitions links into disjoint twelve-link sets. This also factorizes its finite-register R-IA transfer. |
| 2. F1: flux decomposition. | CORRECT | The Casimir eigenvalues and the lower bound on `Q_L` are correct. |
| 3. F2: potential bounds and flux range. | CORRECT | Both potentials have norm at most 24. Each plaquette uses each participating link once. Zero extension does not enlarge the flux range. |
| 4. F3: low-flux comparison. | CORRECT | GB1QL Lemma 4.7 supplies the stated bound. Other factors in the plaquette do not alter the flux of the link being compared. |
| 5. F4: weighted norm. | CORRECT | The Peter–Weyl evaluation bound gives sup-norm control. Cauchy–Schwarz gives `d_L⁶`. The neighbour count gives the stated, generous constant `24·6¹²`. |
| 6. F5: smoothing. | CORRECT | Cauchy–Schwarz gives `k_{2uτ}(e)⁶`. The heat-trace growth is of the stated order. |
| 7. F6: reproducing vectors. | CORRECT | Their evaluation identity and norm follow from the projection kernel. |
| 8. F7: positive targets. | CORRECT | The local bound follows directly from the multiplication factors. The exact bound follows from GB1ISO’s heat-kernel comparison. |
| 9. Section 3.2, step 1: telescope powers. | CORRECT | `B(U)` is a scalar. No commutativity between link operators is assumed. |
| 10. Step 2: cancel low flux. | CORRECT | Testing against `P_{≤M−1}` puts the multiplied test function inside the reproducing space. This justifies the cancellation. |
| 11. Step 3: damp high flux. | CORRECT | After `i−1` insertions, initial flux at least `M` remains at least `M−i+1`. The heat factor gives the displayed bound. |
| 12. Step 4: sum the errors. | CORRECT | With `M = ⌊s^{1/20}⌋`, the low-flux term is `O(s⁻¹)`. Heat damping and the factorial tail beat `d_s⁶ = O(s¹⁸)`. Thus `sup_U ‖r_U‖ → 0`. |
| 13. Step 5: convert vector convergence to kernel convergence. | CORRECT | The `a_U` have uniformly bounded norms. Cauchy–Schwarz bounds the kernel error by `2C sup‖r_U‖ + sup‖r_U‖²`, plus the heat-truncation error. This proves uniform convergence in both kernel variables. |
| 14. Infer strict positivity. | INCOMPLETE | Reality is not stated. A small complex error around a positive kernel is insufficient. Repair: the `P_μ` preserve real functions. The traces of products of quaternion basis matrices are real. Distinct-link coefficients commute. Hence `B̃`, the heat operator and the R-IA transfer preserve real functions. Their continuous kernels are real. The claimed lower bound then follows. |
| 15. Obtain a box-independent threshold. | CORRECT | After step 14, choose the threshold using one cube’s error and positive minimum. Every cube has the same bounds. Products and gauge averages preserve positivity. |
| 16. Obtain probability lifts and total-variation convergence. | CORRECT | For fixed box and fixed `N_t`, finite products of uniformly convergent kernels converge uniformly. Their positive normalizations converge too. This is not volume-uniform convergence. |

The identification with the compressed transfer is correctly rejected. This proof treats the actual finite-register R-IA transfer.

VERDICT RC-G3b: holds with stated repairs

**3. RC-G3c**

| Step | Status | Check |
|---|---|---|
| 1. Adopt the one-cube setting. | CORRECT | Section 3.1 applies to the specified cube-face R-SUM Hamiltonian. It does not apply to an arbitrary overlapping plaquette Hamiltonian. |
| 2. Extend the finite-register Hamiltonian. | CORRECT | `Ĥ = H_s ⊕ τA` because both `A` and `Π` preserve flux and `B̃ = ΠB̃Π`. |
| 3. Remove the complementary heat kernel. | CORRECT | Telescoping the twelve heat factors gives the stated bound on `h_s`. It tends to zero uniformly. |
| 4. Step 1(a): weighted Dyson bound. | CORRECT | Heat contracts the weighted norm. Each potential insertion costs at most `c`. |
| 5. Step 1(b): smoothing. | CORRECT | A largest heat interval has length at least `w/(n+1)`. Half can supply smoothing. Weighted bounds on its left and Hilbert-space bounds on its right give the displayed summable series. |
| 6. Step 1(c): high-flux damping. | CORRECT | For `n < L/2`, the inserted flux projections keep every heat interval above flux `L/2`. Reserving half the largest interval for smoothing leaves at least `w/2` for damping. The remaining Dyson tail tends to zero uniformly on the stated time interval. |
| 7. Step 2: kernel vectors. | CORRECT | Smoothing makes evaluation bounded. The semigroup identity gives the Riesz-vector factorization. Applying step 1(c) to that factorization gives the weighted tail bound. |
| 8. Step 3: Duhamel identity. | ERROR | The sign is wrong. For `ΔB = B̃−B`, the identity is `e^{−a₀Ĥ}−e^{−a₀H} = −θ∫₀^{a₀} e^{−(a₀−u)Ĥ}ΔB e^{−uH}du`. Change both displayed integral signs accordingly. All subsequent absolute-value estimates survive. |
| 9. Step 3: kernel interpretation and endpoints. | INCOMPLETE | The Riesz vectors are defined for positive time. At the integration endpoints they need not exist in `L²`. State the kernel formula for `0<u<a₀`; endpoints have measure zero. Step 4 supplies the uniform integrable bound. For continuity, step 1(c) approximates each positive-time evaluation map uniformly by finite-flux output maps. The resulting Riesz vectors are norm-continuous. |
| 10. Step 4(i): low flux. | CORRECT | Flux range permits the projection on the left. F3 and the two low-flux evaluation bounds give the stated `96δ_s(M)e^{2c|θ|a₀}d_{M+1}^{12}`. |
| 11. Step 4(ii): late-time high flux. | CORRECT | The right kernel vector has at least half the total time available. Its weighted tail is small. The left semigroup is bounded in that same norm. |
| 12. Step 4(iii): early-time high flux. | CORRECT | Self-adjointness moves the potential difference to the long-time vector. The flux projections are valid. This avoids any short-time bound on the other Riesz vector. |
| 13. Step 4: choose the cutoff. | CORRECT | With `M = ⌊s^{1/40}⌋`, the low-flux term is `O(s^{38/40−2})`. The weighted tail also vanishes. Thus the kernel difference tends to zero in sup norm. |
| 14. Step 5: strict positivity. | INCOMPLETE | Add the reality argument from RC-G3b. Then the uniform error, including `h_s`, can be made smaller than half the exact cube kernel’s positive minimum. |
| 15. Step 5: box independence and lifts. | CORRECT | For the cube-face family, one threshold works for every cube. Full kernels are products. Gauge averaging preserves positivity. Total-variation convergence follows for fixed box and `N_t`. |
| 16. Claimed coverage without cube-face factorization. | INCOMPLETE | No such extension is proved. Without factorization, the twelve-link constants and cube minimum no longer control the full transfer. A fixed-box adaptation would have volume-dependent constants. A box-independent threshold needs a further argument. |

The repaired proof establishes the norm needed for positivity. It does not rely on trace-norm convergence alone. GB1E Theorem 8.1 remains compatible: its obstruction concerns sufficiently small steps at fixed register.

VERDICT RC-G3c: holds with stated repairs

**4. RC-4.2**

| Step | Status | Check |
|---|---|---|
| 1. Infer support from the vacuum test vector. | INCOMPLETE | The stated explanation needs normal ordering and number conservation. A monomial containing an annihilator need not kill the vacuum: `cc†|vac⟩ = |vac⟩`. Repair: normal-order the local operator and use `[N,X]=X`. Its vacuum image then has exactly one matter particle, located inside its supporting cube. |
| 2. Cancel the link layers in `XΦ`. | CORRECT | Matter gates fix empty matter. The creation operator commutes with link-only layers. Their adjoints cancel, leaving `M_e* M_o* d†Φ`. |
| 3. Use one-particle evolution. | CORRECT | On this sector the operator-valued matrix exponential is exact. It does not treat link entries as commuting numbers. |
| 4. Write the two selected amplitudes. | CORRECT | Each even cube meets the first odd cube at only one corner. Thus there is only the displayed intermediate corner for each selected output site. |
| 5. Show nonzero derivatives. | CORRECT | On `H₀`, `y₀=1`. A column of `U_s` or its adjoint acting on the constant vector is nonzero for every `s≥1`. |
| 6. Exclude countable exceptional sets. | CORRECT | A nonzero scalar component of each vector-valued entire function has isolated zeros. The two-stage choice of exceptional sets is valid. |
| 7. Exclude every unit cube. | CORRECT | Both selected amplitudes are nonzero. Their sites differ by `2e₁`, so no unit cube contains both. |
| 8. State the generic parameter conclusion. | CORRECT | The analytic zero sets are measurable. Their countable fibres give a null exceptional set. The invertible change to `(ε,μ)` preserves nullity. This does not prove the draft’s stronger one-parameter wording. |

VERDICT RC-4.2: holds with stated repairs

**5. RC-7.1**

| Step | Status | Check |
|---|---|---|
| 1. Reduce the determinant operator. | CORRECT | At total rishon number five, it connects only the two fully occupied endpoint states, with magnitude `5! = 120`. |
| 2. Exponentiate the two-state block. | CORRECT | The displayed formula follows from `(D+D*)² = 120²P`. |
| 3. Conjugate by `U(5)_x`. | CORRECT | `P` is fixed. `D` gains the determinant phase, and `D*` gains its conjugate. |
| 4. Determine the commuting subgroup. | CORRECT | The two off-diagonal matrix units are independent. Commutation is equivalent to `sin(120κ)(e^{iα}−1)=0`. |
| 5. Include the other gates. | CORRECT | The original gates already commute with `U(5)_x`. The determinant gate therefore restricts this subgroup to `SU(5)_x` exactly at the stated nonexceptional angles. |
| 6. Retain parts (b) and (c). | CORRECT | With the group read as `SU(5)`, `−I₅` is excluded and the five-fermion determinant is invariant. Neither assertion depends on κ. |
| 7. Limit the maximality claim. | CORRECT | The proof identifies the commuting subgroup inside the supplied `U(5)` action. It does not classify arbitrary external unitaries. The closure explicitly preserves this limit. |

VERDICT RC-7.1: holds

**6. RC-I1g**

| Step | Status | Check |
|---|---|---|
| 1. Preserve the oriented sector. | CORRECT | Each end gate preserves its end number. Hence the product preserves `σ^→`. |
| 2. Apply Schur’s lemma. | CORRECT | On a fixed star sector, the layer commutes with diagonal `U(5)`. It therefore acts as `⊕λ 1⊗c_λ`, with unitary `c_λ`. |
| 3. Find a nonzero traceless commuting generator. | CORRECT | I2 supplies multiplicity `d≥2`. A scalar `c` permits any traceless generator. Otherwise two spectral projections give the displayed nonzero traceless choice. Normalization is possible. |
| 4. Preserve the state. | CORRECT | The normalized isotypic projection is invariant under `1⊗c`. Matter gates fix empty matter. Electric and swap layers retain their previous invariance. |
| 5. Extend the empty-matter reduction. | CORRECT | The added layer is link-only. The reduction uses the ordered product of all link layers and remains valid. |
| 6. Fix `A_v(a)` under the chain layer. | CORRECT | `c*a c=a`. Gates on other stars act on other end factors. Number preservation makes them commute with the sector projections too. |
| 7. Transport through swaps. | ERROR | As a global operator identity, “the swap carries `A_v` to `A_v′`” is too strong. On an unequal-type pair the swap is identity. Repair: assert the transport only on the support of the chosen product state, or as equality of GNS vectors. Every occupied star there has the selected type, so transport holds. |
| 8. Keep the same generator after transport. | CORRECT | The translation identification preserves orientation and intertwines identical end gates. Thus the transported generator commutes with the transported chain action. |
| 9. Recover the band. | CORRECT | With step 7 repaired, tracelessness and normalization give orthonormal vectors. Their shift is unchanged, so the fibre remains `e^{−iK·(1,1,1)}`. |
| 10. Compile the chain gates. | CORRECT | Each gate is an even operator on one link end. It fits within the NN-a edge support. |

This closes the band claim for the stated identical, number-preserving end gates. It does not cover arbitrary internal updates.

VERDICT RC-I1g: holds with stated repairs