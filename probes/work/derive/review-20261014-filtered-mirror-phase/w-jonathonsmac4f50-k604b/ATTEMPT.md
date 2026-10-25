# J:derive:review-20261014-filtered-mirror-phase:a1 — attempt

Worker: Claude Sonnet 5.5, 2026-10-25. Same family as the source authors; unrefereed. Verdict: PARTIAL. The route stops at step 19.

## Plain-words summary

The sources propose a strong four-fermion interaction that acts only on "filtered" fields, so the three wanted (light) fermion families never feel it while the unwanted mirror partners might be gapped by it. I did four things.

1. I recovered the interaction exactly. It is the repo's Spin(10) pair operator, with a factor 2 (steps 5-6). The source's own "many-body check" never used it: it used a random generic filtered quartic with no 16-component index (step 4).
2. I checked, with the real 16-index tensors, that the light modes commute exactly with every operator built from the filtered field (steps 8-9). I also showed that this exactness is only the statement that the light corner modes do not appear in the Hamiltonian at all, so it says nothing by itself about the light spectrum near the corner (step 10).
3. I proved that any filter with an exact zero has overlapping, non-orthogonal filtered modes, with a quantitative bound (step 11). For the nearest-neighbour star filter the aggregate overlap squared is exactly 3/2 (step 12). So there is no independent-site limit and no controlled strong-coupling bound from the usual argument.
4. I found an exact counterexample to a unique symmetric ground state for one member of the interaction family. The number-conserving member Σ B†B always has a zero-energy, maximal-spin multiplet that is not a singlet (step 13). The source never says which member it means (step 7). Whether the member with the number-violating term (the only one that breaks U(1)_F as the source requires) has a unique symmetric gapped ground state is unresolved (step 19).

Nothing here shows that a symmetric gapped mirror phase without composites exists.

## Setting and premises

Read in full: `docs/MINIMAL_AXIOMS_2026-06-29.md` (233 lines) and `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (130 lines), on origin/main a77a3449c91a. Also read: the four named source reports in full, the source scripts `scripts/X2/x2_cert.py` and `scripts/K1/b1_meanfield_10channel.py` at the frozen commit, and `docs/SPIN10_SYMMETRIC_ATOMIC_GAPS_…_NOTE_2026-09-14.md` on main lines 1-140.

- **ASSUMED P1 (supplied carrier).** Per site, 2 spin slots × 16 of Spin(10), i.e. 32 complex fermion modes (X2 report :212). This exceeds the one-site algebra M_2(C) (AX:47-49). It is the source's own priced comparator, not an axiom consequence. I do not enlarge any primitive. All statements below are about this supplied model.
- **ASSUMED P2 (supplied dynamics).** H = H_W + W Σ_x Q(ψ_S(x)), with H_W = Σ ψ†σ·sin p ψ, continuous time and fermion statistics. AX:114-123 says Admissibility chooses no Hamiltonian, so this is downstream supplier content. No registered primitive (scale reference, kinetic isotropy, realized state) is used.
- **ASSUMED P3 (filter).** ψ_S = (f(p)⊗1₂⊗1₁₆)ψ, with f_NN = (1−Σcos p_a)/2 (7-site star) or f_F1 (27-site cube; X2 :64-66). Interaction range is 2 for the star filter. This is wider than the nearest-neighbour adjacency of AX:37-38 and AX:57-58, which is the source's own price P-X2-4 (:215).
- **Premise-text note.** The task text says Admissibility supplies no probability distribution. Current main says it names one, determined by nearest-neighbour conditions, but does not specify its form or values (AX:63-73, :114-123). Nothing below uses it either way.

## Steps

1. **CHECKED.** The four named objects hash to the task's values at commit dd7d358c6f6b0fd049b46962970397dbdc7d2e1f (`git show`, and check.py section A on the copies in `src/`). See RECOVERY_STATUS.json.

2. **READING.** Where the quartic lives in the sources. The source names it only in prose: B^a = ψ_Sᵀ(iσ_y⊗CΓ^a)ψ_S, "built into BᵃBᵃ + h.c. and Bᵃ†Bᵃ" (X2 :68). Its coefficients and the relative weight of the two forms are not given.

3. **READING.** The source scripts relevant to this task are `x2_cert.py` and `b1_meanfield_10channel.py`. K1's mean-field and overlap scripts use only the filter f(p), never the 16-index tensor.

4. **CHECKED by reading the source script (mismatch).** The "many-body check on a small system" (X2 :94, :264) is `x2_cert.py:136-180`. Its Fock space has 16 modes (8 corners × 2 spin), with no Spin(10) index. The quartic is `randV`: random complex coefficients on bond-local products of the four filtered legs. It tests only the sectors N=3→2. The source's own wording is "random filtered quartic" (X2 :94). So the report's "Q is a Spin(10)-singlet quartic" and the check are never combined in code. The check is a valid instance of step 8, not a test of the Spin(10) quartic.

5. **CHECKED (check.py B, C).** Recovered encoding.
   - With the SPIN10 note's Clifford conventions (γ_{2k+1} = I^k⊗X⊗Z^{4−k}, γ_{2k+2} = I^k⊗Y⊗Z^{4−k}, C = Y⊗X⊗Y⊗X⊗Y, + chirality block) I rebuilt the 16, the 45 generators t_ab (Σt² = 45/4), and the ten symmetric 16×16 monomial matrices M_a = (CΓ_a)|₊.
   - The identity t_abᵀM_c + M_ct_ab = i(δ_acM_b − δ_bcM_a) holds exactly for all 450 cases.
   - Ω = Σ_a B_aB_a has 240 nonzero ordered coefficients, with +8 at (u₀,u₁,v₁₄,v₁₅). Both match the main note's numbers (SPIN10 note :81-84).
   - X2's B^a equals exactly 2 × the main note's B_a, with u, v the two walker spin slots. The mode count is 2 × 16 = 32, the note's q = 32.

6. **PROVED (from step 5's identity) and CHECKED.** Σ_c B_cB_c, Σ_c B_c†B_c and Σ_c B_c†B_c† are Spin(10) singlets. Derivation: [T_ab,B_c] = −i(δ_acB_b − δ_bcB_a), so the induced vector rotation is real antisymmetric and the sums cancel. Each B_a is also a singlet under the spin SU(2), since σᵀε + εσ = 0. Hence Q commutes with S_± and with rotations' spin lift.

7. **PROVED (trivial) / READING.** The quartic is a family Q(a,λ) = aΣB†B + λΣ(BB+B†B†). The source never fixes a and λ. The members are physically different:
   - λ = 0 conserves fermion number, contrary to X2's requirement that U(1)_F be broken to Z₄ (X2 :80).
   - λ ≠ 0 is indefinite.
   - The main note's exact gapped atom (SPIN10 note :93) is neither. It adds a 32-body projector ΔQ_proj, a Casimir term, and a number-window projector Π_mid. The pure quartic is not that atom. This is a source gap, and it is where the next worker must start.

8. **PROVED (short).** Let ψ_m be the annihilator of any mode m, and let f(m) = 0. Then ψ_m anticommutes with every ψ_S(x,s,α) and every ψ_S†(x,s,α). Therefore B_a(x) and B_a(x)† commute with ψ_m, and so does every word in them, for every a, λ and W. Since h(m) = σ·sin p = 0 at a corner, [H_W,ψ_m] = 0 as well. So [H,ψ_m] = 0, and the same holds for ψ_m†, on every even-L torus.

9. **CHECKED (check.py D, E).** The lemma of step 8 on the actual tensors.
   - D: on the 3D L=2 carrier (256 modes), the coefficient matrices K_a(x) = g_xg_xᵀ⊗ε⊗M_a, for all 8 sites × 10 a (both filters), have exactly zero rows and columns at all 96 hw1 modes and nonzero rows at the mirror modes. The unfiltered control has nonzero light rows.
   - E: in a genuine CAR engine with the actual M_a (64 modes: one light corner, one mirror corner, two spin slots, 16 flavours; random N ≤ 2 states including the vacuum component), H = Σ_{x,a}(B†B + ½BB + ½B†B†) gives max|[H,ψ_light]| = 0 exactly on 5 light modes. The mirror modes give a commutator of at least 128, and the unfiltered control also gives at least 128.
   - New relative to the sources: the real tensors; not new: the mechanism (X2-L2).

10. **PROVED (trivial) + READING.** Step 8 says the 96 light corner modes do not appear in H at all (the L=2-torus counting: 3 corners × 2 × 16). So "the light pole is exact with weight 1" (X2 :90-95) is the statement that a measure-zero set of momenta decouples.
    - Near the corner the vertex is f ~ |q|²/4 (f_F1) or a cone (f_NN; indefinite Hessian, X2 :66).
    - That the physical light spectrum remains massless then depends on the mirror sector staying weakly interacting at low energy, i.e. on no massless composite near e_i. That is exactly the Golterman-Shamir question (X2 :173-177).
    - Also, the zero of F[U] is exact only on the trivial gauge background (P-X2-5, X2 :216). I did not check the gauged case.
    - So step 8 supports "no Eichten-Preskill mixing through unfiltered legs" and nothing about composites. That is the scope it carries.

11. **PROVED.** Let f be a trigonometric polynomial with f(p₀) = 0. Put K(r) = Σ_y a(y)a(y+r), so K̂ = |f|². Then K̂(p₀) = 0 gives K(0) = −Σ_{r≠0}K(r)e^{ip₀r} ≤ Σ_{r≠0}|K(r)| ≤ √(N_r Σ_{r≠0}K(r)²), where N_r is the number of nonzero r in the support. Hence the aggregate overlap squared Σ_{r≠0}K²/K(0)² ≥ 1/N_r > 0. In particular ψ_S(x) and ψ_S(y) cannot be orthonormal for all x ≠ y. This holds for every filter with an exact decoupling zero, so a lattice of independent sites is unavailable for every such filter, not only for the two tested. (X2-L5 and K1 B2/B3 gave the same conclusion for the two filters; the lemma and bound are new but elementary.)

12. **CHECKED (check.py F; exact Fractions).**
    - f_NN: K(0) = 5/8, max_{r≠0}|K|/K(0) = 2/5, support 25 sites, aggregate² = Σ_{r≠0}K²/K(0)² = 3/2 exactly. K1's FFT value 1.2247 is √(3/2).
    - f_F1: support 125, max neighbour 0.1850, aggregate 0.6338, matching K1's values.
    - The A1g nearest-neighbour-star filters a + bΣcos p_a vanish at (π,0,0) iff a = −b, so f_NN is the unique such filter up to scale.
    - A numerical search over range-1 A1g filters with the hw1 zeros finds aggregate² as low as 0.3032 (aggregate 0.551; not a certified global minimum), against 0.4017 for f_F1. The optimised filter has no extra zeros on a 31³ grid.
    - So lowering the overlap by changing the range-1 filter does not give an atomic limit (suggested for the whole class; the proven bound is only 1/124).

13. **PROVED + CHECKED (check.py G).** For the number-conserving member Q_+ = Σ_{x,a}B_a(x)†B_a(x) ≥ 0:
    - Take any N ≤ 16 of the u-type modes filled and no v. Every ψ_S(x,↓) annihilates it, so B_a(x) kills it and Q_+ = 0.
    - Q_+ commutes with S_± (step 6), so the whole multiplet S_-^k|Ψ⟩, k = 0..N (spin N/2, dimension N+1), is annihilated. I checked this on the 32-mode atom with the actual M_a for N = 1..16 and for [S_±,B_a] = 0; the lattice version is the same argument, since ψ_S acts only on position and flavour-independent labels.
    - Since Q_+ ≥ 0, this is the minimum. The ground space in every sector N ≥ 1 therefore has dimension ≥ N+1 and contains spin non-singlets (N > 16 follows by particle-hole). It is not a unique symmetric state.
    - Scope: this member only, the quartic alone, i.e. W → ∞ at fixed N. Adding H_W changes the problem, and ker Q_+ ∩ (symmetric states) is not computed.

14. **PROVED + CHECKED.** Also B_a†|all u filled⟩ = 0 (the creation of u is blocked), so for any member including λ ≠ 0 the all-u-filled state (N = 16) and its S = 8 multiplet are exact zero-energy eigenstates. For λ ≠ 0 whether 0 is the lowest eigenvalue is not decided: Q is indefinite there and negative-energy mixing of |0⟩ with N = 4 is expected.

15. **CHECKED (reproduction only).**
    - The BdG spectrum of the walker with singlet pairing is E = ±√(|sin k|² + φ²), each doubly degenerate (sympy, exact). This is the formula behind K1's mean-field B1.
    - The onset ratios I[1]/I[f] are 3.244 (f_F1) and 0.873 (f_NN), as K1 found.
    - The 10 contains no G_SM singlet. So a 10-vector condensate breaks G_SM at the lattice scale. The intermediate symmetry-breaking danger is retained, not removed. Mean field cannot produce a symmetric gapped phase, as K1 noted (KILL_REPORT :172).

16. **READING.** Absence of anomaly versus a symmetric gapped phase. K1 shows every mixed class vanishes at 16 per corner, so symmetry cannot forbid a gapped mirror (K1 :51, :128-130). That is a necessary condition for symmetric gapping, not existence. It also gives no protection to the light 3×16 (K1 :152-153). Steps 11 and 13 show that existence is a dynamical question about a specific operator family whose strong-coupling limit is not atomic. No 't Hooft matching forces massless mirror composites, but nothing excludes them either.

17. **ASSUMED + CHECKED illustration.** Right-handed-neutrino necessity.
    - The mod-16 argument (F1 :63-83; K1 :136-143) binds only gapping that keeps the corner nodes pinned and uses the stated translation, rotation, fermion-parity and Spin(10)/G_SM contract.
    - Illustration (check.py F): walker plus an on-site chemical potential m = 2 keeps every shift and the number, and is gapped by moving the bands off the Fermi level (max|sin p| = √3).
    - So "ν_R forced" is conditional on the node-preserving contract, as the task states. I add no new classification result.

18. **READING.** Slab and protected zero. X1 argues that a successful symmetric slab implies the F4-L2 protected-zero condition (X1 :84-93, :156-163) and concedes it is not a new mechanism. The converse is not shown. I found no converse and no counterexample. X2-L2k (X2 :138-141) is a proof skeleton with named open steps. I did not advance it.

19. **FIRST UNRESOLVED STEP.** For the member with the number-violating term (step 7), at some W and in 3D: a unique, symmetric (translations, proper rotations with spin lift, Spin(10), Z₄^F), gapped ground state of H_W + W Σ_x Q(ψ_S(x)) with no 10-vector condensate and no massless composite. Steps 11-13 show that the atomic strong-coupling route is unavailable and that the λ = 0 member fails. The step is blocked-equivalent to Golterman-Shamir condition (3) plus no intermediate symmetry breaking (X2 :179-185).

## What is new relative to the sources

- **New:** the explicit recovery map with checked normalisation (steps 5-6). The coefficient-level and CAR-level light-mode check on the real tensors, with the source mismatch (steps 4, 9). The scope of exactness (step 10). The lemma that every exactly-zero filter has non-orthogonal filtered modes, with its bound, and the exact value 3/2 (steps 11-12). The Q_+ and all-u-state multiplets (steps 13-14).
- **Not new:** the mechanism of X2-L2, K1's overlap numbers (reproduced), K1's mean-field ratios (reproduced), the anomaly arithmetic (not re-run).

## Overlap with open PRs

Open PRs #9994, #10004 and #10035 (candidate-laws, 2026-10-21/22) treat a cube-filtered mirror term on SU(4) toys and Karsten-Wilczek bands, with sign-free CT-INT diagnostics that they themselves call inconclusive at L ≤ 6. They are not Spin(10) and not the walker carrier. I read only their summaries via `gh pr view`, not their notes, so any further overlap is unchecked.

## Files

- `ATTEMPT.md` (this file)
- `check.py` (runtime about 36 s, peak memory about 118 MB; output saved as `run.out`)
- `RECOVERY_STATUS.json`
- `src/` (verbatim copies of the four named objects and of `x2_cert.py`, `x2_cert.out`, `b1_meanfield_10channel.py`/`.out`)
