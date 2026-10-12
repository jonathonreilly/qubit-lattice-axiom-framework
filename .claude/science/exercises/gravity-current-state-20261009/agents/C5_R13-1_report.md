# C5 R13-1 report: the electron–photon split, with momentum in the superalgebra on the box

**Author.** Claude Opus 5.5 probe, the same model family as the supervisor and every C5 worker. Unrefereed. Written 2026-10-12, 20:13Z to about 21:00Z. No repository file was edited.

**Scratch.** `S/` = `.../scratchpad/C5/R13-1/`. Scripts and outputs are in `S/scripts/`. Every run takes under 15 s with `OMP_NUM_THREADS=2`.
- `r131_photon_sqed.{py,out}`: the one-loop photon coefficient in minimal N=1 box SQED, from the Dirac loop plus 2 selectron loops, with a moment-formula check on the literal edge.
- `r131_electron_sqed.{py,out}` (m = 0.2), `_m0.1.out`, `_m0.05.out`: the full one-loop c_e − c_γ.
- `r131_checks.{py,out}`: the mass-split residual; the product-rule defect; an on-shell 2→2 process with ΔP ≠ 0; the doubler-free photino; the per-mode algebra.
- `r131_partner_crosscheck.{py,out}`: the 4×4 partner-loop code checked against R10-5's refereed 8×8 logic.
- `r85_box_qed_copy.py`: an unmodified copy of R8-5's refereed runner (photon P_E/P_M and the electron's photon loop).

**Read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`, in full (`AX`).
- `TESTS.md`: the C5 method (`:2302-2320`); Round 13 (`:4560-4694`), with R13-1 at `:4578-4596`; prior-art lines `:871`, `:1168-1180`, `:1213-1216`, `:1850`.
- `SUMMARY.md` §§21–25 (`:534-675`).
- `agents/C5_S14_synthesis.md`, §§1–3 in full.
- R12-3: the report, `C5_R12-3_referee.md` and the verdict.
- R10-5: the report (§§0–3.5), `C5_R10-5_referee.md` and the verdict.
- R10-1: the report (§§1–3.7) and the verdict.
- R8-5: the report, in full, and the verdict.
- `C4_F2_referee.md:30-58`.
- Scripts `scripts/C5/R8-5/r85_box_qed.py`, `R10-1/r101_pairing.py`, `R10-5/r105_partner_loop.py`.

**Labels.**
- **proved**: complete under the stated hypotheses.
- **checked**: numerics here.
- **suggested**: argued, not proved.
- **reading**: an interpretation.
- **comparator**: literature. V = verified this session; R = recalled.

**Paths.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`. `vR12-3` abbreviates `P/agents/C5_R12-3_referee_verdict.md`, and likewise for other rounds.

---

## 0. In plain words

1. **(a) At the free level the algebra exists, but it does not force one light cone.**
   - A spinor supercharge with {Q, Q̄} = 2σ^μP_μ can be built on the whole Brillouin zone (D2), mode by mode. Here P is the "symbol momentum" Σ p(k)N(k) (proved).
   - The algebra works for any p(k) per species. So the algebra alone does not force a common p.
   - A common p on the box *is* forced once P is required to generate lattice translations on box states, or to be conserved by a vertex on D1 (proved). That condition is an identification, not a consequence of the algebra.
   - Even then, the algebra forces the light cone only for massless (short) multiplets: E = |p| exactly, so c = 1.
   - For massive multiplets it gives only a positivity bound, E ≥ |p|, i.e. c_e ≥ (1 − m²/b²)^{1/2}. An electron faster than light is allowed (proved, with an explicit counterexample).
   - The expectation "a common p(k) is forced" is therefore refuted as stated, and holds only in this narrower sense.
2. **(b) With interactions the algebra cannot close on the whole zone.**
   - If Q is conserved, the Jacobi identity forces P to be conserved.
   - A Ward-forced photon couples to every charged mode (R8-5 Lemma C). A one-body P = Σ p(k)N(k) with p(k) = k on the box is then conserved only if p is affine on the whole circle, which is impossible for a periodic p (proved; this is Lemma R and the Kato–Sakamoto–So obstruction in operator form).
   - The defect is explicit: [P_i, H] = Σ_vertices Δ_i × vertex, with Δ_i(k, q) = p_i(k+q) − p_i(k) − p_i(q). It vanishes exactly on D1, the box-additive domain.
   - At tree level the algebra closes on D1. At O(e²) the normal-ordering terms of {Q⁽¹⁾, Q̄⁽¹⁾} are sums over the whole zone. That is where the loops leave D1.
   - A dressed P is also blocked at O(e²): an on-shell 2→2 process with ΔP ≠ 0 and order-one charge overlaps exists (checked example). Class-wide this is suggested.
3. **(c) One loop: c_e − c_γ is not zero, and N=1 partners barely move it.**
   - Setting: minimal N=1 box SQED (electron = R8-5's BQ law, 2 matched selectrons, R8-5's photon, a matched doubler-free Majorana photino; Yukawa √2e).
   - Result: Δ = (δc_e − δc_γ)·16π²/e² lies between **−12.2 and −24.9 on the gapped edge** and **−16.3 and −55.1 on the literal edge**, over 4 box shapes (m = 0.05, N = 128; IR- and N-stable).
   - That is c_e − c_γ ≈ −7e-3 to −3e-2, the same size as R8-5 without partners (−11 to −22 on these shapes).
   - **Literal edge, photon coefficient (proved and checked).** The supersymmetric pairing cancels exactly the A-moments, the part Theorem N\* targets. What is left is the Dirac velocity-norm moment, δc_γ = ⟨(S′(k_x)² − 1)S′(k_y)²/(4E³)⟩. Since S′ − 1 = ∂_qΔ(k, 0), this is literally an edge moment of the product-rule defect. It changes sign between shapes, so a tuned zero of the photon coefficient exists. Δ stays negative in all 24 laws computed.
   - **The sign is diagnostic (proved).** An exact algebra on box states would force c_γ = 1 and c_e ≥ c_γ − O(m²/b²). The computed values violate both, by O(e²/16π²). So minimal box SQED is not supersymmetric with momentum at one loop, even on box one-particle states.
4. **(d) No photon doubler is forced in the spinor class (spectral level).**
   - A Majorana–Wilson photino with E_λ(q) = ω(q) exactly, matched to R8-5's doubler-free photon, exists. It vanishes only at q = 0 (checked to 3e-15).
   - R10-5's Chern ±2 obstruction does not apply: the photino operator is not the curl, and fermion number is not conserved (the escape the R12-3 referee named, `vR12-3:3`).
   - A quasi-local field-level Q for this vector multiplet is **not constructed** (open).
5. **Against the FIXED readings: INCONCLUSIVE, leaning FAIL** (worker reading).
   - No PASS: the split is nonzero.
   - No class FAIL: no doubler is forced, and "no untuned choice removes the split" is not proved, because the off-D1 Yukawa and selectron gauging are free functions.
   - Bounded results offered to the referee: Theorem B (no exact spinor algebra on D2 in 𝒢₀); Corollary BPS (what an exact algebra would force, and that one-loop minimal box SQED violates it); Lemma LIT (the literal-edge photon coefficient equals the defect moment).
   - The upside registered in the expectation does not occur. N=1 pairing is the A-moment cancellation that N\* allows, but the Dirac a-moment and mixing moments have no bosonic counterpart in a 4-component multiplet.

---

## 1. Hypotheses and classes (stated before any title)

- **H-lat.** Z³ × ℝ, Hamiltonian, continuous time; translations and proper cubic rotations (`AX:37-41`). Free fields plus Ward-forced Peierls gauge coupling, and one loop where stated.
- **Box symbols.** A per-axis odd periodic C^∞ symbol p_j(k) = S(k_j), with S = ρk + (1 − ρ)sin k; ρ = 1 on |k| ≤ b₁ and 0 on |k| ≥ b₂ (R8-5's S, `P/agents/C5_R8-5_report.md:126-131`).
  - Wilson mass M(k) = m + Σ_j W(k_j), with W = r(1 − ρ)(1 − cos k).
  - **Literal edge:** r = 0, which leaves doublers at mass m.
  - **Gapped edge:** r = 1.
  - B = the open box; D1 = all external and internal momenta, and their sums, in B without folding; D2 = the full zone.
- **Class 𝒮𝒫 (untwisted spinor SUSY with momentum).**
  - Spinor charges Q_α with {Q_α, Q̄_β̇} = 2σ^μ_{αβ̇}P_μ, P₀ = H, [Q, P_μ] = 0, on a positive-norm Fock or Hilbert space.
  - P_i is one-body and band-scalar: P_i = Σ_s Σ_k p_{s,i}(k)N_s(k), with p_s continuous and periodic (Theorem B), or a perturbative dressing of it (§3.2(iii)).
  - Matter multiplets are realized as 4-component Dirac h_e = Σ S(k_j)α_j + βM(k) (R8-5's BQ law), with matched selectrons ε = E_e.
  - The vector multiplet is a Ward-forced photon plus a Majorana photino.
- **Minimal box SQED (for (c)).**
  - Electron: BQ.
  - Selectrons φ_L, φ_R: complex, with ε² = E_e², gauged in the D1-supersymmetric factorized form K_A = Σ_j S_j(A)² + M(A)², all factors Peierls.
  - Photon: R8-5's, ω² = Σ_j d(q_j)².
  - Photino: Majorana, 4-component form h_λ = Σ_j S_γ(q_j)α_j + βW_λ(q), with W_λ² = Σ_j[d(q_j)² − S_γ(q_j)²], so E_λ = ω exactly.
  - Yukawa: √2e[φ_L* λ̄P_Lψ + φ_R* λ̄P_Rψ] + h.c., momentum-independent on the whole zone. This is the D1 value; off D1 it is a choice.
  - Feynman gauge for the photon loop, with photon mass λ = m. The D-term does not enter at this order.
- **Excluded outside realizations, named before any title:**
  - twisted or nilpotent-scalar Q (R12-3, R12-6);
  - class 𝒮 (R10-5);
  - non-scalar or non-one-body momentum operators beyond perturbative dressing;
  - non-C¹ (SLAC) symbols and infinite-flavour or non-local constructions (the KSS escapes, `P/agents/C4_F2_referee.md:46`);
  - compact links; Euclidean Z⁴; nonabelian groups;
  - two loops;
  - soft breaking, except the mass-split residual;
  - the selectron gauging and Yukawa form factors off D1, other than the stated choice.

## 2. Prior art (each counted once)

- **Kato–Sakamoto–So, the Leibniz no-go.**
  - Cited at `TESTS.md:871`: "not a blanket theorem that no lattice momentum exists".
  - `:1213-1216`: P_tot generates central differences; KSS is an analogy, not the proof.
  - `:1850`: SUSY cancellation is broken at g²/16π² by KSS.
  - `C4_I2_report.md:238`: the infinite-flavour escape is N → ∞.
  - Theorem B below is this obstruction, made precise for the superalgebra's P.
- **RC C1 Lemma R** (`TESTS.md:1172-1177`): the C¹ invariants of normal collisions are λE + b·k + c, and "closure forbids umklapp". Theorem B is its operator, off-shell version for one-body P. The on-shell §3.2(iii) is its direct use.
- **C4 F2 referee** (`P/agents/C4_F2_referee.md:46`): without P_i, GNP is merely unavailable, not refuted; KSS has escapes.
- **C4 P1** (`C4_P1_report.md:180,205`): a nilpotent H = {Q, Q†} is allowed.
- **R8-5** (CWC): the BQ law, the vertex and Lemma C/Theorem B; the BQ split −11 to −71 (`vR8-5:3-13`). Its runner is reused unmodified.
- **R10-1** (CWC): Theorem D (Dirac = a, A, c₁, c₂ moments), Theorem T′ (scalar), Theorem P (8-component Clifford-flat pairing) (`vR10-1:5-9`), and the localization lemma (a sketch, `vR10-1:15`). Lemma LIT below is Theorems D and T′ specialized to the N=1 content.
- **R10-5** (CWC, FAIL bounded to 𝒮): Lemma PD; §3.4 (N=1 nilpotent charges square to H + n̂·P); and the partner-loop spectral formula, confirmed by the referee (`P/agents/C5_R10-5_referee.md:38-40`), which is reused here.
- **R12-3** (CWC, INCONCLUSIVE): Theorem L is non-protection by a single Nicolai Q; GNP needs the full supercharge–translation algebra (`vR12-3:9`).
- **R11-1 Theorem N\*** (as quoted in `C5_S14_synthesis.md:58-60`): aggregate boson and fermion A-measures must cancel per observable.
- **R8-2/R9-2/R11-4:** box-to-box momentum conservation, with off-box sources (`TESTS.md:4040-4041,4428`). The defect operator in §3.2 is the field-theory form of those off-box sources.
- **Comparators.**
  - **GNP, hep-ph/0404271 (V: abstract and HTML).** They keep the supercharge–translation subalgebra unmodified. Dimension 3 is forbidden by exact SUSY. Dimension 4 is possible only through a derivative superpotential of gauge singlets or a W^αW^β term between two U(1)s, so it is absent in the MSSM. Soft breaking regenerates operators suppressed by m_soft/M. Berger–Kostelecký's deformed algebra is removable by a coordinate change.
  - Dondi–Nicolai 1977 and Bergner et al. on SLAC-derivative SUSY (R, not used).
  - Sugino hep-lat/0311021 (V via `vR12-3:3`): doublers removed without conserved fermion number.

## 3. Results

### 3.1 (a) Free level

- **Lemma F (free algebra on D2). Proved.**
  - Statement. Take free species with one-particle energies E_s(k) and any continuous periodic p_s: T³ → ℝ³. A spinor Q_α with {Q_α, Q̄_β̇} = 2σ^μP_μ, P₀ = H₀ and P_i = Σ p_{s,i}N_s exists on the free Fock space iff at each k the one-particle levels group into Clifford representations with E ≥ |p_s(k)|.
    - E > |p|: long, 2 bosons + 2 fermions.
    - E = |p|: short, 1 + 1.
  - Proof.
    1. Q_α = Σ_k q_α(k), where q_α(k) is the per-mode Clifford representation of 2(E − σ·p(k)) ≥ 0.
    2. Operators at different k anticommute.
    3. Positivity of {Q, Q†} gives the "only if".
  - Every free identity used is an identity in commuting c-numbers (p_j(k), M(k)) at fixed k. No product rule enters, which is why the free level is unobstructed.
  - Checked per mode (`r131_checks.out` (4)):
    - box electron: eig 2(E − σ·p) = (0.026, 1.52);
    - edge electron: (2.69, 5.37);
    - zone corner: (4.2, 4.2).
    All are long and positive.
- **Corollary F1 (no common p from the algebra). Proved.**
  - Lemma F holds for p_γ = λk on the photon and p_e = k on the electron, with λ ≠ 1. The algebra is exact and c_γ = λ.
  - So the algebra alone does not tie species together. This mirrors Theorem L (`vR12-3:9`), now for the spinor class.
- **Corollary F2 (common p from translations). Proved.**
  - Suppose e^{ia·P} = T_a on box one-particle states for all a ∈ Z³. Then p_s(k) − k ∈ 2πZ³ on B, and continuity with p_s(0) = 0 gives p_s = k on B for every species.
  - The same follows if a one-body P is conserved by a cubic vertex on an open subset of D1. Then p_s(k+q) = p_{s′}(k) + p_{s″}(q) there, and Cauchy's equation makes every p affine with a common slope.
  - Off B, nothing forces commonality.
- **Corollary F3 (what the algebra does to the cone). Proved.**
  - With p = k on B, every species has E_s(k) ≥ |k| on B.
  - **Massless short multiplets** have E = |k| exactly, so c = 1.
  - **Massive multiplets** satisfy E_s² = k² + M_s(k)², where M_s² := E_s² − k² ≥ 0 is otherwise free. So c_s² = 1 + ∂_{k²}M_s², bounded only by c_s² ≥ 1 − m_s²/b².
  - Counterexample to "one cone by algebra" for matter: M(k) = (m² + δ|S(k)|²)^{1/2} with δ > 0. This is smooth on T³ for m > 0, gives c_e = (1+δ)^{1/2}, and keeps the free algebra exact.
  - **Reading (comparator GNP):** a lattice-scale-natural superpotential symbol M(k) = m + O(k²) gives δc² = O(m·w), suppressed by m. That is GNP's dimension-5 structure, imposed by locality and naturalness, not by the algebra.

### 3.2 (b) Interactions: closure domain and defect operator

- **(i) The defect operator. Proved, by direct commutation.**
  - For each cubic vertex Σ_{k,q} X(k,q) a_{s″}(q) ψ_s†(k+q) ψ_{s′}(k), with lattice momentum conserved mod 2π:

    [P_i, H⁽¹⁾] = Σ_{k,q} Δ_i(k,q) X(k,q) a(q)ψ†(k+q)ψ(k),  Δ_i = p_{s,i}(k+q) − p_{s′,i}(k) − p_{s″,i}(q),

    with p evaluated at the folded momentum. The same holds for the Peierls photon vertex (fermion and selectron) and for the Yukawa (with Δ = p_e(k) − p_φ(k−q) − p_λ(q)). For the quartic seagull and D-term, the analogous four-point Δ appears.
  - Δ ≡ 0 on D1, because S is linear there and nothing folds.
  - Checked for S1 (`r131_checks.out` (2)): Δ ≤ 6e-17 with k, q, k+q in the box; −2.9e-5, −0.25, −0.37 and −0.40 off it. Δ(0, q) = 0 trivially, because S(0) = 0.
- **(ii) Theorem B (no exact spinor algebra on D2 with Ward-forced coupling). Proved.**
  - **Hypotheses.** 𝒮𝒫 with one-body band-scalar P; a Peierls photon in class 𝒢₀ (`vR8-5:3`); and p_e = k on B.
  - **Claim.** No Q in 𝒮𝒫 is conserved in the interacting theory at O(e).
  - **Proof.**
    1. Jacobi: [{Q_α, Q̄_β̇}, H] = 0 gives σ^μ_{αβ̇}[P_μ, H] = 0. The σ^μ span the 2×2 Hermitian matrices, so [P_i, H] = 0.
    2. At O(e) this requires Δ_i(k,q)V(k+q,k) = 0 for all k and q.
    3. Take q along x and the current along y. The Peierls vertex is exactly ∂_yh(k) = S′(k_y)α_y + W′(k_y)β, independent of k_x and q (`P/agents/C5_R10-1_report.md:73`). It is nonzero for every k_x when |k_y| < b₁.
    4. Hence S(k_x + q) − S(k_x) = p_γ,x(q) for all k_x on the circle and all small q.
    5. Differentiating gives S′ constant on the circle. A periodic S then has S′ ≡ 0, contradicting S = k on B. ∎
  - **Scope.**
    - This is Lemma R (`TESTS.md:1172`) and KSS in operator form. The new step is Jacobi plus Lemma C's whole-zone vertex.
    - It does not cover non-local or infinite-flavour P, or P that is not band-scalar.
- **(iii) Dressed P. Suggested; example checked.**
  - Solving [P, H] = 0 order by order needs the commutator [P⁽⁰⁾, H_int] to vanish between H₀-degenerate states. At O(e²) that means the on-shell 2→2 amplitude times ΔP must vanish.
  - Example (`r131_checks.out` (2)), BQ S1 gapped, m = 0.1:
    - k₁ = (0.95, 0.5, 0) and k₂ = (0.6, −0.5, 0), both in the box;
    - on shell to 2e-16 into k₃ = (1.275, 0.445, 0), which is off the box, and k₄ = (0.275, −0.445, 0);
    - ΔP_x = −0.030 (−0.003 and −0.101 at neighbouring points);
    - charge-vertex singular values 0.99 and 0.99.
  - The Born amplitude is generically nonzero, so no dressed P exists generically.
- **(iv) Closure domain.**
  - Tree level: {Q, Q̄} − 2σ^μP_μ has vanishing matrix elements between Fock states whose momenta and partial sums lie in D1. The rules there are continuum SQED's (R8-5 in-box rules, `P/agents/C5_R8-5_report.md:137-138`).
  - At O(e²), normal ordering of {Q⁽¹⁾, Q̄⁽¹⁾} produces quadratic operators with an internal sum over the whole zone. These terms are not D1-closed even between box states. This is exactly the one-loop self-energy (reading; the operator is not written out here).
- **(v) Corollary BPS (what exactness would force). Proved under the stated hypotheses.**
  - Hypotheses: Q in 𝒮𝒫 conserved on the interacting theory; P eigenvalue k on box one-particle states; minimal content; C₄ about the cubic axes.
  - **Photon.** For q along an axis, the photon multiplet (±1, ±½) cannot form a long representation. A long representation has both bosons at one J_z, and +1 ≢ −1 (mod 4). So E_γ = |P| exactly, and by cubic isotropy of the dimension-4 term, c_γ = 1.
  - **Electron.** E_e ≥ |k| for all box k, so c_e ≥ (1 − m²/b²)^{1/2}.
  - Hence c_e − c_γ ≥ −O(m²/b²). Even an exact algebra would *not* give c_e = c_γ; it forbids only the "electron slower" sign. The other sign needs GNP's field-theory structure.

### 3.3 (c) One loop in minimal N=1 box SQED. Checked; Lemma LIT proved

- **Method.**
  - δc_γ: the electron loop, from R8-5's `photon()`, unmodified, plus 2 selectron loops. For the selectrons, P_E = ⟨Γ(k,k)²/(16ε⁵)⟩ and P_M = [χ(0) − χ(q)]/q².
    - **Subtraction named:** the Ward/f-sum subtraction χ_yy(0) from the same grid. It is exact because the factorized seagull is q-independent.
    - The vertex is Γ = 2S(k_y)S′(k_y) + W′(k_y)[M(k) + M(k+q)].
    - Richardson extrapolation over q = 2πs/N.
  - δc_e: the photon loop, from R8-5's `fermion()` (Feynman gauge, λ = m), plus the selectron–photino loop. The latter uses R10-5's refereed spectral formula (normal plus Z graph, `P/agents/C5_R10-5_referee.md:38`), adapted to 4×4.
  - **Adaptation check** (`r131_partner_crosscheck.out`): on the common case (W = 0, photino on the electron curve) it equals R10-5's 8×8 logic to 2e-13.
  - Additional check: axis-x equals axis-y to all printed digits.
- **Lemma LIT (literal edge, photon). Proved; checked.**
  - With r = 0: c₁ = c₂ = 0 in R10-1 Theorem D, so δc_γ(Dirac) = ⟨a x²/(4E³)⟩ − ⟨AX²/(4E⁵)⟩.
  - The scalar band u = S² is separable, so Theorem T′ gives δc_γ(selectron) = ⟨AX²/(8ε⁵)⟩ with ε = E.
  - The sum for 1 Dirac + 2 selectrons is δc_γ = ⟨(S′(k_x)² − 1)S′(k_y)²/(4E³)⟩, with a = (∂_qΔ)(∂_qΔ + 2) and ∂_qΔ(k, 0) = S′(k) − 1.
  - The A-moments cancel exactly. What remains is an edge moment of the product-rule defect.
  - a ≢ 0 for any C¹ periodic S with W = 0, because S′ must vanish somewhere, where a = −1.
  - Checked (`r131_photon_sqed.out`), direct versus moment at N = 96, m = 0.2:
    - S1: −3.954 vs −3.956;
    - S3: +40.589 vs +40.594;
    - S5: −6.009 vs −6.007;
    - S7: +3.492 vs +3.492.
  - The sign varies across shapes, so a one-shape tuning zeroes it.
- **Gapped edge (r = 1).** Shared β gives mixing moments, and the selectron band is non-separable. Wilson no-box control: −0.395. N=1 4-component matter cannot be Clifford-flat, which needs at least 6 anticommuting mass/velocity matrices beyond m, i.e. 8 components. So R10-1 Theorem P is unavailable (proved by counting; the 4×4 Hermitian Clifford maximum is 5).
- **Result** (m = 0.05, N = 128; units e²/16π²; `r131_electron_sqed_m0.05.out`):

| shape (b₁, b₂) | edge | δc_γ (e + 2ẽ) | δc_e photon loop | δc_e ẽ–λ̃ loop | δc_e | **Δ = δc_e − δc_γ** |
|---|---|---|---|---|---|---|
| S1 (1, 2) | literal | −4.31 | −10.28 | −10.28 | −20.57 | **−16.25** |
| S1 | gapped | +1.15 | −10.62 | −1.67 | −12.29 | **−13.44** |
| S3 (2, 3) | literal | +42.62 | −7.13 | −5.36 | −12.48 | **−55.10** |
| S3 | gapped | +16.73 | −6.55 | −1.64 | −8.18 | **−24.91** |
| S5 (0.5, 1.5) | literal | −6.46 | −11.79 | −11.72 | −23.51 | **−17.04** |
| S5 | gapped | −0.09 | −13.36 | −1.57 | −14.93 | **−14.84** |
| S7 (1, 3) | literal | +3.58 | −8.63 | −7.66 | −16.29 | **−19.87** |
| S7 | gapped | +2.08 | −8.33 | −1.76 | −10.08 | **−12.17** |

- **Stability.**
  - N = 64 → 96 at m = 0.2: |change| ≤ 0.15.
  - m = 0.2 → 0.1 → 0.05: Δ moves by at most 4%. For example, S3 gapped: −23.2, −24.3, −24.9; S1 gapped: −13.09, −13.32, −13.44.
  - Errors are grid and extrapolation spread, not a controlled bound.
- **Comparison.** R8-5's BQ without partners gives Δ = −12.97, −21.70, −14.83, −11.03 on S1, S3, S5, S7 (`P/agents/C5_R8-5_report.md:229-235`, at m = 0.025). On the gapped edge, N=1 partners change Δ by −0.01 (S5) to −3.2 (S3). The reused legs reproduce R8-5: δc_e photon loop −10.62/−6.55/−13.36/−8.33 here vs −10.61/−6.54/−13.33/−8.31 there.
- **Physical size.** e²/16π² = 5.807e-4 (`C5_R8-5_report.md:259`), so c_e − c_γ ≈ −7.1e-3 (S7 gapped) to −3.2e-2 (S3 literal). That is about 3e16 to 1.2e17 times the 2.66e-19 photon-decay bound (`C5_R8-5_report.md:261`). The sign is c_γ > c_e in every case, as in R8-5 and F2.
- **Against Corollary BPS.** Computed δc_γ ∈ [−6.5, +42.6] ≠ 0, and δc_e ∈ [−23.5, −8.2], i.e. c_e < c_γ by far more than m². Both violate what an exact algebra would force. This confirms Theorem B quantitatively: the one-loop theory is not supersymmetric with momentum, even on box states.
- **Mass-split residual** (soft ε² = E² + Δm², both loops; m = 0.1, N = 96; `r131_checks.out` (1)):
  - ∂Δ/∂(Δm²) ≈ +0.4 (S1) and +1.0 (S3) on the gapped edge, lattice units. These are poorly resolved; the noise is about 0.01 in Δ.
  - On the literal edge: +6.9 and +65 (the doublers have mass m).
  - At a = ℓ_P and Δm = 1 TeV, Δm²a² ≈ 7e-33, so the residual is negligible next to Δ itself.
- **Is it zero, or a defect moment?** It is not zero in any of the 24 laws (8 laws × 3 masses). On the literal edge, the photon leg is exactly a defect moment (Lemma LIT). The electron legs are edge-supported only by R10-1's localization sketch (`vR10-1:15`); I did not derive them as defect moments.

### 3.4 (d) Doublers

- **The vector multiplet of 𝒮𝒫 can be doubler-free at the spectral level. Checked.**
  - Photon: R8-5's, ω² = Σd(q_j)², with zeros only at 0 (`vR8-5:5`).
  - Photino: Majorana, h_λ = α·S_γ + βW_λ, with W_λ² = Σ(d² − S_γ²) ≥ 0 because 2 sin(q/2) ≥ sin q.
  - |E_λ² − ω²| ≤ 3.6e-15 on the grid; the 4×4 eigenvalues equal ω to 3.1e-15. S_γ(π) = 0 and W_λ(π,0,0) = 2, so the zone corners are gapped (`r131_checks.out` (3)).
  - **A smooth variant (suggested).** Take W_λ = Σ_j w(q_j) and give the photon the gauge-invariant factor f(q) = (|S_γ|² + W_λ²)/Σd_j², which equals 1 near 0. Its kernel is f(|D̂|²1 − D̂D̂†). This avoids the square root.
- **Why R10-5's Chern ±2 does not bite (suggested).**
  - In 𝒮 the photino operator is the curl. Here it is a Weyl block with a Majorana mass: no conserved fermion number, so there is no Nielsen–Ninomiya pairing (Sugino's escape, `vR12-3:3`).
  - At q = 0 the bundles balance: c₁(photon ±1) = ±2 = c₁(photino ±½) + c₁(spinor index ±½) = ±1 ± 1. So there is no Chern obstruction to the intertwiner there.
- **Open.** A quasi-local field-level Q_α for this multiplet. The per-mode intertwiners exist (Lemma F), but I did not build a smooth global symbol.
  - The naive continuum transcription Q ∝ σ·(Π + iB)λ, with lattice curls, gives a photon "momentum" built from D̂_j e^{−iq_j/2}, which is antiperiodic (suggested). It needs a separate Majorana/Wilson piece in Q.
  - So "no doubler is forced" holds at the spectrum level only.

### 3.5 (e) Per-site content and prices (named, not adopted)

- **P-site.** Electron, 4 CAR; selectrons, 2 complex = 4 real CCR; photon, 3 non-compact CCR links (1 gauge); photino, 2 CAR (Majorana; U(1)_R broken by W_λ).
  - Total about 7 CCR + 6 CAR per site, against the Qubit fibre M₂(ℂ) (`AX:47`): infinite-dimensional bosons and graded composition (O3 Prop. 3).
  - This is the cheapest SUSY content tried (BF: 7 + 7 gauge only; R10-5: 16 + 16 charged).
- **P-dyn.** H = P₀ in a superalgebra is dynamics, which Admissibility does not supply (`AX:116-130`).
- **P-mom.** The algebra's P is a symbol momentum. It equals lattice momentum only on box states, and it is not conserved off D1 (Theorem B). Making it exact needs non-local or infinite-flavour structure, i.e. the KSS escapes, or set A's continuum.
- **P-match.** A selectron degenerate with the electron (R comparator: excluded). Soft splitting adds only O(Δm²a²) here (§3.3), but the matched split is already nonzero.
- **P48 stands** (`C5_S14_synthesis.md:179`). The e–γ counterterm (about 1e-16 to 1e-17) remains a tuning in the untwisted spinor class too. R13-1 prices the loophole that P48 left unpriced: momentum in the algebra closes only on D1, and loops leave D1.

## 4. Against the FIXED readings (`TESTS.md:4593-4595`)

**Worker reading: INCONCLUSIVE, leaning FAIL.** Same family; the referee is required for every no-go below.

- **PASS: not met.**
  - The free spinor Q is exact on D2 at tree level (order e⁰).
  - With interactions, closure holds on D1 at tree level only. At O(e) it fails on D2 (Theorem B), and at O(e²) the normal-ordering terms leave D1.
  - The Ward identity holds (R8-5's).
  - The photon is doubler-free at the spectral level, but the field-level Q of the vector multiplet is not built.
  - One-loop c_e − c_γ is nonzero in every computed law: −12.2 to −55.1 e²/16π².
  - The residual under a mass split is O(Δm²a²) and is stated.
- **FAIL: not met as registered.**
  - (i) No photon doubler is forced (§3.4).
  - (ii) The split is a nonzero edge quantity: proved to be a defect moment for the literal photon leg, and edge-supported only by R10-1's sketch for the electron legs. "No untuned choice removes it" is **not** proved. The Yukawa form factor and the selectron gauging off D1 are free functions not fixed by D1-SUSY, and the photon leg changes sign across shapes. A tuned zero of Δ is plausible. I found none: Δ < 0 in 24 of 24 laws.
- **Bounded results offered to the referee:**
  - Theorem B: no conserved Q in 𝒮𝒫 with one-body band-scalar P, in 𝒢₀.
  - Corollary BPS: an exact algebra on box states would give c_γ = 1 and c_e ≥ c_γ − O(m²/b²). One-loop minimal box SQED violates both.
  - Lemma LIT: the literal-edge photon coefficient equals ⟨(∂_qΔ)(∂_qΔ + 2)S′_y²/(4E³)⟩.
  - Corollary F1/F3: the algebra alone forces neither a common p nor c_e = c_γ.
- **The record, if confirmed.**

  > "Momentum can be put into a lattice superalgebra only as the box symbol, and only on box-additive states. With Ward-forced gauge coupling it is not conserved off the box, so no spinor supercharge is exact on the zone. Even an exact one would force only c_γ = 1 and c_e ≥ c_γ. In minimal N=1 box SQED the one-loop split stays at −12 to −55 e²/16π², the sign the algebra would forbid. On the literal edge the photon leg is exactly a moment of the product-rule defect. The electron–photon split remains unremoved and unprotected in the untwisted spinor class."

- **Expectation check.**
  - (a) "a common p(k) is forced" is right only via translation identification, not by the algebra.
  - (b)–(c) INCONCLUSIVE leaning FAIL: as expected.
  - The upside, N\* cancelling the defect moment, did not occur. N=1 pairing removes the A-moments but not the Dirac a-moment or mixing moments.

## 5. Strong-word check

- **"Exact":**
  - the free per-mode algebra (an identity);
  - Δ ≡ 0 on D1 (checked to 6e-17);
  - E_λ = ω (checked to 3.6e-15);
  - the in-box rules and Ward identity (R8-5, refereed).
- **"Proved":**
  - Lemma F and Corollaries F1–F3;
  - the defect commutator;
  - Theorem B (one-body band-scalar P only);
  - Corollary BPS (under exactness, C₄ and minimal content);
  - Lemma LIT;
  - the Clifford-count statement that 4 components are not flat.
- **"Suggested":**
  - the dressed-P obstruction class-wide;
  - the smooth photino variant;
  - the absence of a Chern obstruction for the spinor intertwiner;
  - the edge support of the electron legs (via R10-1's sketch);
  - GNP-type suppression from naturalness (reading).
- **"Checked":** every table number.
  - The partner loop is checked against R10-5's refereed logic on a common case, not independently of that formula.
  - Selectron loops are checked against Theorem T′ on the literal edge only. The gapped factorized-gauging vertex is checked only by the Ward subtraction and N-convergence.
- **"Not zero":** in the 8 laws × 3 masses computed. No sign theorem is claimed.
- **Not claimed:**
  - any statement for twisted, Nicolai, non-local or infinite-flavour supercharges;
  - two loops;
  - a field-level Q for the Majorana–Wilson vector multiplet;
  - that Δ < 0 holds class-wide.

## 6. For the referee

1. **Theorem B.** The Jacobi step; the use of R10-1's exact transverse vertex ∂_yh (independent of k_x and q) to get S′ constant on the whole k_x circle; the band-scalar hypothesis on P.
2. **Corollary BPS.** Whether C₄ about the axes suffices to keep the photon multiplet short, and whether cubic isotropy then fixes the dimension-4 c_γ.
3. **Lemma LIT.** The specialization of R10-1 Theorems D and T′ (c₁ = c₂ = 0 when W = 0; u′ = 2X).
4. **The factorized selectron gauging.** The vertex Γ and the q-independence of the seagull.
5. **The 4×4 partner adaptation** (`r131_electron_sqed.py:41-79`). The Majorana photino propagator in ⟨λλ̄⟩ form; y = √2e per selectron; averaging over the 2 positive states.
6. **The off-D1 choices.** Whether "no untuned choice removes" can be proved for any natural restriction on the Yukawa form factor.

**Downloads:** none. Web: arXiv abstract and HTML of hep-ph/0404271, read via WebFetch, as text only.
