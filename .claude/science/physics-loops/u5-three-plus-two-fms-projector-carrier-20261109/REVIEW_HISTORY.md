# Review History

## 1. Author-Side Mutation Testing Record

Eleven load-bearing mutations were executed against [`scripts/frontier_u5_three_plus_two_fms_projector_carrier.py`](../../../../scripts/frontier_u5_three_plus_two_fms_projector_carrier.py); all eleven failed closed with `exit=1` (`AssertionError`):

| Mutation ID | Target Check Family | Mutation Applied | Result |
|---|---|---|---|
| `M1_su2_commutator_weight` | Theorem 1(2) state-$L^2$ equality | Changed commutator weight from $1/(16 r^4)$ to $1/(8 r^4)$ | Killed (`exit=1`, `AssertionError: Theorem 1(2) state-L^2 equality with zero radial-commutator cross term`) |
| `M2_u5_car_eigenvalue` | Theorem 2(2) 5-mode CAR identity | Changed eigenvalue factor from $6 - n$ to $5 - n$ in $C^2 = (6 - n)C$ | Killed (`exit=1`, `AssertionError: Theorem 2(2) 5-mode CAR sector n=1 (dim=5): C^2=5C, P_CAR^2=P_CAR, Tr(P_CAR)=1/5 I`) |
| `M3_so10_ja_reconstruction_sign` | Theorem 3(2) orthogonal reconstruction | Flipped sign of $((a - b)^2)/(ab)$ in $A - (a Q_6 + b Q_4)J_A$ | Killed (`exit=1`, `AssertionError: Theorem 3(2) exact factorizations of J_A^2 + I_10 and A - (a Q_6 + b Q_4) J_A through Q_6^2 - Q_6`) |
| `M4_z6_kernel_block_exponent` | Theorem 4(1) $\mathbb{Z}_6$ quotient kernel | Changed $z^{-2} = z^4$ to $z^2$ on the $SU(3)$ block of $\pi$ | Killed (`exit=1`, `AssertionError: Theorem 4(1) Z_6 kernel of pi: 6 distinct triples in SU(3)xSU(2)xU(1) all mapping to I_3 (+) I_2`) |
| `M5_link_determinant_fermion_sign` | Theorem 5(1) $\Lambda^5 \mathbb{C}^{10}$ determinant word | Flipped permutation sign in $U_\ell^{i_1,1}\cdots U_\ell^{i_5,5} = \operatorname{sgn}(i)D_{xy}$ | Killed (`exit=1`, `AssertionError: Theorem 5(1) U_ell^{i_1,j_1}...U_ell^{i_5,j_5} = eps(i) eps(j) D_{xy} across all 120 permutations and repeated indices`) |
| `M6_gauss_endpoint_charge` | Theorem 5(3) $\mathfrak{gl}(5)_x$ Gauss commutator | Changed endpoint eigenvalue from $2\delta_{ij}$ to $1\delta_{ij}$ in $[G_x^{ij}, \mathcal{O}_{xy}^{(10)}]$ | Killed (`exit=1`, `AssertionError: Theorem 5(3) [G_x^{ij}, O_{xy}^{(10)}] = 2 delta_{ij} O_{xy}^{(10)} for all 25 gl(5)_x generators`) |
| `M7_su5_quartic_32_ratio` | Theorem 6(2) fourth-moment ratio | Changed $3+2$ ratio from $7/30$ to $1/4$ | Killed (`exit=1`, `AssertionError: Theorem 6(2) exact fourth-moment ratios 7/30 < 1/4 < 1/2 < 13/20 across all four symmetry strata`) |
| `M8_higgs_gram_rank` | Theorem 7(1) $25 \times 25$ Higgs Gram matrix | Changed $\operatorname{rank}(\mathcal{M}^2)$ from $13$ to $12$ | Killed (`exit=1`, `AssertionError: Theorem 7(1) 25x25 Higgs Gram matrix M^2 spectrum`) |
| `M9_pinch_commutator_sign` | Theorem 7(3) noncommuting pinch identity | Changed anticommutator $D_A X + X D_A$ to commutator $D_A X - X D_A$ | Killed (`exit=1`, `AssertionError: Theorem 7(3) universal noncommuting pinch-commutator identity`) |
| `M10_coherent_su2_fms_defect` | Theorem 8(2) $K$-copy coherent $SU(2)$ defect | Changed $(K+1)/K^3$ to $(K+2)/K^3$ | Killed (`exit=1`, `AssertionError: Theorem 8(2) K=1 coherent SU(2) FMS defects`) |
| `M11_coherent_det_transport_defect` | Theorem 8(2) $K$-copy determinant transport defect | Changed $(3K+2)/K^3$ to $(3K+1)/K^3$ | Killed (`exit=1`, `AssertionError: Theorem 8(2) K=1 coherent determinant transport defect`) |

## 2. Independent Subagent Mathematical Review

An independent read-only referee subagent (`ebe84222-d51f-411e-8dc2-b4573909f63b`) was invoked across Milestone 01 (Theorems 1–5) and Milestone 02 (Theorems 6–8) to verify all theorem statements, equations and signs, the runner implementation, and conformance with `docs/ai_methodology/REVIEW_LOOP_PR_CONFORMANCE_SPEC.md`:

- **Mathematical verification:** Confirmed from first principles that all eight theorem statements, equations, coefficients, signs, dimensions, and all 43 runner checks are mathematically exact.
- **Proof and prose findings resolved:**
  1. Corrected a canceling double-sign step in the intermediate CAR manipulation of the proof of Theorem 2(2) ($c_j^\dagger c_j c_k = -\delta_{jk} c_j + c_k c_j^\dagger c_j \implies N c_k = c_k(N - I) \implies (5I - N)c_k = c_k(6I - N)$).
  2. Replaced a leftover scratch sentence in the proof of Theorem 5(2) with clean deductive sign-counting prose.
  3. Removed a duplicated `= \Psi_X^*` in the proof of Theorem 1(3), added `self-adjoint` to the spectral hypothesis of Theorem 2(3), and changed the unbound index in $\min_{k \in \{0,\dots,5\}} \mathcal{D}_{3+2}(A_{(k)}) = 0$.
- **Conformance and runner polish resolved:**
  1. Formatted provenance/context references (`docs/SU5_EMBEDDING_FROM_GRAPH_FIRST_SURFACE_THEOREM_NOTE_2026-05-07.md`, `docs/SU5_DECOMPOSITION_PROOF_WALK_LATTICE_INDEPENDENCE_BOUNDED_NOTE_2026-05-08.md`, cache, and loop pack) in backticks rather than markdown links per `REVIEW_LOOP_PR_CONFORMANCE_SPEC.md` §8 so `build_citation_graph.py` does not wire non-load-bearing provenance notes as upstream `deps`, and aligned the top-level note header with `REVIEW_LOOP_PR_CONFORMANCE_SPEC.md` §3.
  2. Added a nonzero trace-residual check (`h5_shifted = h5 + I_5`) to `theorem2_u5_projector_and_car_controls()`, aligned the sign comment in `theorem5_native_determinant_carrier_controls()`, and clarified the comment in `theorem8_transport_floor_and_coherent_scaling_controls()`.
