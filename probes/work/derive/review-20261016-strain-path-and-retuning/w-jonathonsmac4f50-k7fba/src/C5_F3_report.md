# C5 F3 report: an O(t²) unitary dressing of the strained Dirac operator does move F1's additive-mass Hessian, and a small local dressing zeroes it

- **Worker:** Claude Opus 5.5 probe, the same model family as the supervisor and as F1. Unrefereed. Run 2026-10-13 from 13:13Z to 13:59Z.
- **Edits and downloads:** no repository file was edited; nothing was downloaded.
- **Memory:** every run used OMP_NUM_THREADS=2 and ran one at a time. Peak resident memory was 690 MB (`f3_sym`); all other runs were at or under 390 MB. No process of mine is still running.
- **Item:** `TESTS:9241-9259` (P = `.claude/science/exercises/gravity-current-state-20261009/`). The FIXED readings are at `:9255-9258` and the expectation at `:9259`.
- **Paths.**
  - `S/` = `scratchpad/C5/F3/scripts/`.
  - `S/f1_lib.py` is F1's library, copied unmodified (diff-checked).
  - `../arch/` holds unmodified copies of `dirac.py`, `sublum.py`, `dfam.py` and `zz.py` (from `P/scripts/C5/R18-5`) and of `r1934_lib.py` (from `P/scripts/C5/R19-34`).
  - `rF1` = `P/agents/C5_F1_report.md`, which is unrefereed (its referee is running).
  - `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`.
- **Read:**
  - `AX` in full;
  - `TESTS:9146-9280`;
  - `rF1` in full, with `f1_lib.py`, `f1_root.py`, `f1_validate2.py` and the `.out` files;
  - `C5_R19-34_referee_verdict.md` in full, and `C5_R19-34_report.md` by grep;
  - `C5_R19-30_report.md:1-80`, for W1 and for re-placement as a row-neutral freedom;
  - `r1934_lib.py:1-122`; `dirac.py:1-60`; `sublum.py`.
- **Labels:** proved (a complete short argument, unrefereed) / checked (numerics run here) / suggested / reading / comparator. RECALLED means from memory.

## 0. Plain words, and the reading

**The question.**
- F1 built the strained Dirac operator as D_t(k) = D(Φ_t(k)).
- Conjugating it by a smooth k-dependent unitary V_t = exp(i t² G(k)) keeps the band energies, the SF rows and UD, but it changes the gauge coupling at O(t²).
- Does that move F1's additive-mass E_g Hessian, +2.424e-2 e²?

**Answer: yes, strongly, and a small local dressing cancels it (checked).**

- **The Hessian is linear in the dressing (proved).** For G = a·G₀:

  Hess(a) = Hess_F1 + 2a·L[G₀]

  L is the first-order response of the one-loop additive mass of the *unstrained* root law to an infinitesimal conjugation. So the question is decided entirely at t = 0.
- **Only two generators can contribute in the item's class (proved; checked).** By range, they are:
  - G₁ = −Σ_j γ_j sin k_j, nearest-neighbour;
  - G₂ = −Σ_j γ_j sin k_j (cos k_l + cos k_m), next-nearest.
  - Every other generator in the class (hermitian, cubic covariant, trig, range ≤ NNN) is either odd under P, T or C, so its response vanishes by symmetry, or it commutes with H.
  - Each of G₁ and G₂ rotates the 4-vector (kinetic c, mass M) by a k-dependent angle 2ε|f(k)|. This keeps the energy E exactly and moves weight between the Wilson mass and the kinetic term.
- **The responses (checked; converged to 1e-10).**
  - L[G₁] = −0.858583 e²; L[G₂] = −1.502128 e² (R18-9 root).
  - L[G₁] = −0.858112 and L[G₂] = −1.502419 (0⁺ root).
  - Both are 35 to 62 times F1's Hessian.
- **The zero is reachable.** F1's Hessian vanishes at a* = +0.014116 for the nearest-neighbour G₁ (+0.00807 with G₂).
  - At a*, the dressing rotates (c, M) by at most 0.049·t² radians.
  - Checked directly: the full SF-strained law with the dressing switched on gives Hess = −1.2e-12 at a*. At a = 0 it reproduces F1's +2.4238554e-2 to all digits.
- **Mechanism.**
  - Structural (proved): minimal coupling does not commute with a k-dependent conjugation. The dressed law equals a field redefinition of F1's law **plus** a gauge-covariant Pauli/clover-type operator (∝ F_jl and E_j). Like the clover term for Wilson fermions (comparator, RECALLED), that operator moves the critical mass.
  - Numerical (checked): 98.5% of L[G₁] comes from the dressing's change of the mass function (−2ε f·c), 80% of it through the tadpole. About half of that change sits inside the box, where the root has no Wilson term at all.
- **What the dressing leaves alone (proved):** the band energies at every t (all SF free rows); UD and every first-order vertex, so W1; the Ward identity; ξ-independence; locality.
- **What else it changes:** a strain-dependent Pauli magnetic-moment term in the IR. With the Planck-spacing mapping this is δa ~ 4a*t²(mℓ_P) ≈ 2e-42 for electrons at t ~ 1e-9. Suggested; unobservable.

**Branch on the item's wording.**
- The item writes D′ = V D V† and also says this "leaves the spectrum unchanged" and acts as the field redefinition ψ → Vψ (`TESTS:9244,9259`).
- Those two descriptions agree only when V commutes with γ₀, or when the conjugation acts on the Hamiltonian H = γ₀D (D-H: H → VHV†, equivalently D → γ₀Vγ₀·D·V†).
- For the generators that matter (G₁, G₂ anticommute with γ₀), the literal V D V† makes the band Hamiltonian non-hermitian at O(ε): its eigenvalues acquire imaginary parts of 5.4e-3 at ε = 1e-2 (checked). So it violates the item's own premise.
- **D-H (the class that satisfies the premise):** DRESS-SHIFTS.
- **Literal formula, restricted to V that keep the spectrum ([V, γ₀] = 0):** every admissible nontrivial generator is P-, T- or C-odd, up to range 2. So DRESS-INVARIANT there (proved by symmetry; checked to ≤ 7e-15).

**Worker reading: DRESS-SHIFTS.**
- Range: the whole real line. The Hessian is affine and unbounded in the dressing coefficient; for |a| ≤ 1 with G₁ alone it spans [−1.69, +1.74] e².
- The zero is reachable with the nearest-neighbour generator at a* = +0.0141. It is a one-number tuning per strain channel, per loop order and per root, and it is priced below (P-F3a, named, not adopted).
- To pass F2's Earth row, a must be tuned to |a/a* − 1| ≤ 6e-9.
- **Consequence for F1 (reading, for F1's referee).** F1's "no tuning knob inside SF" (`rF1:47`) holds only for its U = 1 lift (`rF1:135`). The O(t²) dressing is a knob with the same status as R19-34's κ*. F1's SF-HAZARD is then generic but not unconditional: a tuned codimension-1 set of dressings zeroes the one-loop channel. P-R19-34a remains the cheaper cover.

## 1. Setting, branches and hypotheses (stated before titling)

- **Law:** F1's branch B1 (`rF1:113-133`; `S/f1_lib.py`).
  - R18-9 root D1(0.909103708, 0.555604226); the 0⁺ root D1(0.915438682, 0.568280847);
  - photon Gph(2.9435);
  - SF flows Φ_t (Dirac at m_flow = 0.01; photon with its own separable flow);
  - Psym axis-ordered generalized links;
  - Feynman gauge; external P = 0; critical m = 0 fixed at t = 0.
  - SF units t, with Hess_h = 4·Hess_t.
- **Dressing (`TESTS:9246-9249`):** V_t(k) = exp(i t² a G(k)). G is a hermitian 4×4 trig polynomial in the Dirac algebra, cubic covariant, with Fourier support on the stencil S19 = {0, ±e_j, ±e_j ± e_l} (up to next-nearest neighbour). S27 (adding the cube corners) and S33 (adding ±2e_j) are run as extensions.
  - G is evaluated at the unflowed k. Evaluating it at Φ_t(k) differs at O(t³), which cannot enter the Hessian.
- **Conventions (`f1_validate2.py:19-20`):**
  - g₀ = σ₁⊗1, g_j = σ₂⊗σ_j (Euclidean, hermitian);
  - F1's D = i g·c + M;
  - H = g₀D = α·c + βM, with α_j = i g₀ g_j and β = g₀;
  - Σ_j = −(i/2)ε_jkl α_kα_l.
- **Branches.**
  - **D-H, main:** H → VHV†. This is spectrum-preserving for every unitary V, and it is the field redefinition ψ → Vψ, ψ† → ψ†V†, which keeps the ∂_τ term.
  - **D-L, literal:** D → VDV† on F1's D. It preserves the band energies for every D only when [V, g₀] = 0, and there it coincides with D-H (proved). With [V, g₀] ≠ 0, H′ = g₀VDV† = V†HV† is not hermitian. Checked: for G₁ at ε = 1e-2, the eigenvalues acquire |Im| = 5.4e-3 (`f3_lit.out`, section (1)). The premise excludes this case.
  - **Roots:** R18-9 and 0⁺. Flow mass B1 / B2 enters only through Hess_F1, because L is a t = 0 quantity (proved).
- **Excluded:**
  - two loops;
  - the T₂g channel. Its O(t²) dressing would need its own coefficient: one per quadratic strain invariant (suggested);
  - the multiplicative channel;
  - the O(t²) change of the photon's own one-loop strain response, which the Pauli remainder also touches (not computed);
  - non-axis path families (that is F4's item).

## 2. Proofs

**Lemma 1 (reduction; proved).**
- H′_t = V_t H_t V_t† = H_t + i t² a [G, H₀] + O(t³), because H_t = H₀ + O(t).
- Psym vertices and seagulls are linear in the corner values of the operator. The one-loop δm is a smooth functional of (H, vertices, seagulls, photon symbols).
- So δm[H′_t] = δm_F1(t) + t² a L[G] + O(t³), with L[G] = d/dε δm[H₀ + iε[G, H₀]] at t = 0.
- Both sides are even in t: the C₂ rotation about [110] maps h → −h (`rF1:147`), and G is cubic covariant while t² is even.
- Hence **Hess(a) = Hess_F1 + 2aL[G]**, exactly at this order. The dressing is the same in H-cov units (t² = 4h²), so Hess_h(a) = 4Hess_F1 + 8aL.
- Checked in full: `f3_tcheck_156.out:3-5` builds the strained and dressed law at finite t with F1's flows.
  - a = 0 gives +2.4238554e-2 (= `f1_root_conv.out:2`).
  - a = a* gives −1.2e-12.
  - a = −0.05 gives +0.11009685, against the prediction +0.11009685 (diff 7e-12).

**Lemma 2 (symmetry selection; proved; inputs checked).**
- The undressed root H(k) is invariant under the cubic rotations, P (β·), T (U_T K, with U_T U_T* = −1) and C (U_C K) (`f3_sym.out:2-7`, ≤ 7e-16).
- The dressed law is symmetric under g iff G = g·G, where:
  - (P·G)(k) = βG(−k)β;
  - (T·G)(k) = −U_T G(−k)* U_T†;
  - (C·G)(k) = −U_C G(−k)* U_C†.
- The minus sign comes from the antiunitary flipping i in exp(iεG).
- Psym and Gph are covariant under each g, and the β-component of Σ(0) is g-invariant. So L[g·G] = L[G], and L vanishes on every g-odd generator.
- Checked: every symmetry-odd generator tried gives |L| ≤ 7e-15, while the symmetric ones give O(1) (`f3_mat_N16.out:12-25`).

**Lemma 3 (the admissible class; checked by exact linear algebra on sampled values, `f3_sym.out`).**

| stencil | cubic-covariant generators (nontrivial) | fully symmetric, nontrivial | literal branch ([G, β] = 0), nontrivial and symmetric |
|---|---|---|---|
| S19 (≤ NNN) | 20 (17) | **2 = span{G₁, G₂}** | **0** (its 7 nontrivial members are P/T/C-odd) |
| S27 | 28 (24) | 3 (adds G₃ = −Σγ_j sin k_j cos k_l cos k_m) | 0 |
| S33 | 36 (31) | 4 (adds G₄ = −Σγ_j sin 2k_j) | 0 |

- The literal-branch representatives are β, βΣcos, βΣcos·cos (P+T−), βΣ·sin, βΣ·sin(c + c) (P−T−C+), and Σ·sin, Σ·sin(c + c) (P−T−C−).
- They span the 7-dim space (rank 7, `f3_lit.out`).
- A random element of that span has L = 0 at N = 16 and at N = 24 (`f3_lit.out`, last two lines).

**Lemma 4 (structure of the symmetric dressing; proved; checked).**
- For G_f = Σ_j iβα_j f_j = −Σ_j γ_j f_j, with f odd and T₁u:
  - i[G_f, H] = 2(α·f M − β f·c);
  - so V = exp(iεG_f) rotates (c, M) in the (f̂, M) plane by θ = 2ε|f|, and c⊥ is fixed.
- The dressed operator stays in Dirac form, so F1's reduced formula (`f1_lib.py:17-18`) applies exactly.
- Checked:
  - against expm, to 2.7e-15; E is preserved to 4.4e-15 (`f3_mat_N16.out:2-3`);
  - the reduced formula against an independent explicit 4×4-matrix one-loop computation, which does the Q₀ integral by spectral decomposition: equal to 3.5e-17, undressed and dressed (`:6-8`);
  - the dressed integrand is even in each q_j, so F1's octant quadrature is valid: octant against full zone to 3e-17 (`f3_even.out`).
- G_f(0) = 0, so D′(0) = 0. M′ = M cos θ − (f̂·c) sin θ is even. Psym telescoping holds for any corner values. Therefore F1's Ward-identity and ξ-independence proofs (`rF1:185-190`) carry over verbatim (proved).

**Lemma 5 (why the field-redefinition argument fails; proved).**
- Let G_A be the Psym coupling of G and U_A = 1 + iεG_A. Substituting ψ′ = U_Aψ into the dressed law gives F1's law plus

  Δ_A = iε{([G, H])_A − [G_A, H_A]} + iε[D_τ, G_A]

  with a fermion Jacobian that affects δm only at O(e⁴).
- (i) The exact redefinition leaves the additive mass unchanged at one loop. Its extra terms carry Γ_tree(0) = 0 on at least one side at the critical point, and U(0) = 1 because G_f(0) = 0. So the shift is **not** an off-shell artefact of Σ(0); the second half of `TESTS:9259` does not apply.
- (ii) Δ_A ≠ 0. Take the pair −γ_y sin k_y in G₁ and α_x s(k_x) in H.
  - Psym's x-vertex of their product weights sin k_y at ½[sin 0 + sin q_y].
  - The product rule (what [G_A, H_A] uses) puts it at the leg ends.
  - The difference is −½{γ_y, α_x} sin q_y s(q_x)/d_x = −iβγ_xγ_y sin q_y s(q_x)/d_x. That is a βΣ_z (q_xq_y)-type, i.e. B_z, Pauli vertex.
  - The time term gives ε Σ_j V_j[G](q₀a_j − d_j a₀), an E_j-dipole coupling.
- Both vanish as q → 0, so the Ward identity, the rows and the gauge parameter are untouched. But the loop integrates over the whole zone, so they enter Σ(0).
- (iii) Continuum check (suggested; Pauli identity RECALLED). With G = −γ·p, the dressed law has −2εβπ², while the redefined law has −2εβ(γ·π)² = −2εβ(π² ± eΣ·B). The remainder is a magnetic moment 2εe.

## 3. Results (checked)

**L per generator, per e², per unit ε** (`f3_resp_main.out`, `f3_resp_root0.out`; central differences ±1e-3 and ±2e-3 with Richardson):

| root | grid (nodes) | L[G₁] (NN) | L[G₂] (NNN) | L[G₃] (S27) | L[G₄] (S33) |
|---|---|---|---|---|---|
| R18-9 | 156 | −0.858582973 | −1.502128368 | −0.711968053 | −0.846559902 |
| R18-9 | 240 | −0.858582973 | −1.502128368 | −0.711968053 | −0.846559902 |
| R18-9 | 344 | **−0.858582973** | **−1.502128368** | −0.711968053 | −0.846559902 |
| 0⁺ | 240 / 344 | −0.858112335 | −1.502419329 | — | — |

- The undressed dm₀ = +0.041858390, F1's value (`rF1:200`).
- Grid changes move L by ≤ 2e-10; the d-versus-2d spread is 3e-6 before Richardson.

**Structural split of L[G₁], 156 nodes** (`f3_resp_parts.out`, `f3_split.out`):
- tadpole −0.6829, exchange −0.1756;
- mass part (δM = −2εf·c): −0.8458, of which −0.4356 inside the box |k_j| ≤ b and −0.4102 outside;
- kinetic part (δc = 2εfM): −0.0128.
- So the dressing acts mainly as an added Wilson-like scalar term, ≈ −2εk² in the IR box, and its seagull dominates.
- G₂: tadpole −1.3659, exchange −0.1362.

**Zero and range** (`f3_astar.out`):

| branch (Hess_F1) | a* with G₁ | a* with G₂ | max rotation at a*, per t² |
|---|---|---|---|
| B1 R18-9 (+2.424011e-2, `f1_root_conv2.out:3`) | **+0.0141164** | +0.0080686 | ≤ 0.049 (G₁) |
| B2 R18-9 (+2.426109e-2, `f1_branches.out:4`) | +0.0141286 | +0.0080756 | ≤ 0.049 |
| 0⁺ root (+2.453499e-2, `f1_branches.out:5`) | +0.0142959 | +0.0081652 | ≤ 0.050 |

- At NNN the zero set is the line a₁L₁ + a₂L₂ = −Hess_F1/2, which has codimension 1.
- For |a| ≤ 1 (G₁): Hess ∈ [−1.693, +1.741] e². For |a₁|, |a₂| ≤ 1: [−4.70, +4.75] e².
- A dressing with a > a* flips the sign to F1's tachyonic branch.
- H-cov units: Hess_h(a) = +0.0970 − 6.869a.

## 4. Probe (c): cost of the zero, and what it changes

**Cost.**
- One real number per strain channel (E_g here; T₂g needs its own, not computed), per root, per loop order. Two loops would re-tune it.
- Precision: to pass F2's Earth-crossing row, which F1 exceeds by 1.62e8 (`f1_envscale.out:2`), |a/a* − 1| ≤ 6.2e-9.
- The generator is nearest-neighbour and smooth, so the dressed operator stays C^∞ with super-polynomial hopping tails (proved: V is entire in G).

**What it changes.**

| item | status |
|---|---|
| band energies at every t, hence all SF free rows (`rF1:181-182`) | unchanged (proved: unitary conjugation) |
| UD, first-order vertices, W1 (the linearized stress Ward identity of the UD kernels, `C5_R19-30_report.md:52,72`) | unchanged (proved: V_t = 1 + O(t²)) |
| F1's Ward identity, ξ-independence, locality | preserved (Lemma 4) |
| the unstrained law, critical mass and R19-34 numbers | unchanged (V₀ = 1) |
| additive-mass E_g Hessian | moved by 2aL (checked) |
| IR: strain-dependent Pauli moment ~ 2a t² e·βΣ·B | δa ~ 4a*t²(mℓ_P): 2.4e-42 for electrons at t ~ 1e-9; 2.4e-66 at t ~ 1e-21; 8e-37 for the top quark (suggested; Planck spacing as in the R19-34 mapping; `f3_astar.out`) |
| one-loop photon strain response at O(t²) and the T₂g and multiplicative channels | not computed |

- Nothing observed is changed except the targeted channel (suggested, on the rows above).

## 5. Against the FIXED readings (`TESTS:9255-9258`), literal first

| reading | status |
|---|---|
| **DRESS-INVARIANT** | **Not met on D-H**: L[G₁] = −0.8586 and L[G₂] = −1.5021, converged to 1e-10 and confirmed by the full finite-t law. **Met on the literal sub-branch** (V commuting with γ₀, the only literal V that keep the spectrum): all admissible nontrivial generators are P/T/C-odd up to S33 (proved; ≤ 7e-15 checked) |
| **DRESS-SHIFTS** | **Met (D-H).** Range: all of ℝ (affine, unbounded); [−1.69, +1.74] e² for \|a\| ≤ 1. Zero reachable with the NN generator at a* = +0.0141 (B1). It is a tuning, priced as P-F3a |
| OPEN | Not met. The law was built and both branches were computed. The branch split comes from the item's own wording, and its premise ("spectrum unchanged", "ψ → Vψ") selects D-H |

**Worker reading: DRESS-SHIFTS** (D-H), with the literal [V, γ₀] = 0 sub-branch DRESS-INVARIANT.

## 6. Against the expectation (`TESTS:9259`)

- **"DRESS-INVARIANT … field redefinition … cannot change the pole mass":** not borne out on D-H.
  - The redefinition must be gauge-covariantized.
  - Psym coupling does not commute with a k-dependent conjugation, so the dressed law equals the redefined law plus a Pauli/clover-type remainder (Lemma 5).
  - Comparator (RECALLED; no numbers quoted): for Wilson–clover fermions the one-loop critical mass depends on c_SW.
- **"Possibly DRESS-SHIFTS for the off-shell Σ(0), but not the physical mass":** not borne out.
  - At P = 0 and the critical point, the β-part of Σ(0) is the pole datum, and the exact redefinition leaves it fixed (Lemma 5(i)).
  - The shift is a change of law, not an off-shell artefact.
- **Borne out on the literal [V, γ₀] = 0 sub-branch**, by symmetry rather than by the field-redefinition argument.

## 7. Prices (named, not adopted)

- **P-F3a: O(t²) Dirac dressing tuned to the critical point.**
  - V_t = exp(i t² a* G₁), with a* = +0.0141164 (R18-9 B1) chosen so the one-loop additive-mass E_g Hessian vanishes.
  - Cost: 1 number per channel per order per root, at tuning precision 6e-9.
  - Gate: `AX:89-90` ("a choice not fixed by the supplied structure remains a named conditional").
  - Compare **P-R19-34a** (`rF1:291`; `C5_R19-34_report.md:177`): 0 numbers, a clause, exact at all orders. It covers the channel whatever the dressing (proved: it resets δm on every strained law), so it dominates P-F3a (reading).
- **No axiom text changes.**

## 8. Strong words

- **"Proved"** (short, unrefereed): Lemmas 1, 2, 4, 5(i)-(ii); the D-L/D-H relation; the "unchanged" rows of §4.
- **"Checked":** every number in §3-§4 and the Lemma 3 dimensions (numerical rank with tolerance 1e-8 on 48 random k).
- **"Every admissible dressing" (literal branch):** stencils up to S33 only; beyond that, the symmetric γ₀-commuting class (e.g. Σ·g with g ∈ T₁g, range ≥ (2,1,1)) was not examined.
- **Not claimed:**
  - two loops;
  - T₂g;
  - the photon's O(t²) strain response under the dressing;
  - any principle that fixes a;
  - that the dressing is physically preferred. It is a freedom left open by the registered texts (`rF1:135`).

## 9. Files (`S/` = `scratchpad/C5/F3/scripts/`)

- `f3_dirac.py`: Dirac algebra, the spin representation, and U_T and U_C.
- `f3_lib.py`: the general Dirac-form one-loop mass on F1's formula, the dressing rotation, and the dressed and strained operator built on F1's flows.
- `f3_sym.py` → `.out`: symmetries of H and the generator-space enumeration (S19, S27, S33).
- `f3_mat.py` → `f3_mat_N16.out`: the expm check, the matrix-versus-reduced check, and L for 14 generators.
- `f3_resp.py` → `f3_even.out`, `f3_resp_main.out`, `f3_resp_root0.out`, `f3_resp_parts.out`: evenness, converged L, the 0⁺ root, and the parts.
- `f3_split.py` → `.out`: the mass/kinetic and inside/outside split.
- `f3_tcheck.py` → `f3_tcheck_156.out`: the full finite-t dressed law (Lemma 1 check; zero at a*).
- `f3_lit.py` → `.out`: the literal branch (non-hermiticity; span; random element).
- `f3_astar.py` → `.out`: a*, the range, the tuning precision and the IR estimate.
- `*.err`: /usr/bin/time memory records.
- `f1_lib.py`: F1's library, unmodified.
