# Mass-gap CW crossover attack (conditional-support; closes no MG row)

Author checkpoint, 1 November 2026. **The four-dimensional continuum existence and physical mass-gap target remains open; CW
remains open.** This unit continues [MASS_GAP_CROSSOVER_REDUCTION.md](MASS_GAP_CROSSOVER_REDUCTION.md). It (a) states a new
strong-coupling proposition, Prop. S: single-link Dobrushin uniqueness for SU(2) Wilson in d = 4 at β < 1/9, with an
interval-certified variance input. Prop. S **needs independent review**. (b) It shows that a simple Kotecký–Preiss bound does *not*
beat the existing 1/32. (c) It gives a finite-block criterion CW_ℓ that is an open (perturbation-stable) condition, and restates
Theorem H as Theorem H′, with CW replaced by CW′: "the Balaban flow lands near a verified specification". (d) It reports small Monte
Carlo runs, which are **evidence only**. No MG row changes status.

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: conditional-support
independent_review: pending
MG_rows_closed: []
```

Every number below comes from a script in [checks/cw/](checks/cw/README.md), with outputs in `checks/cw/data/`. Conventions are those of
MASS_GAP_CROSSOVER_REDUCTION §1 at N = 2: weight exp{(β/2) Σ_p Tr U_p}, β = 4/g_0², equivalently S = β Σ_p (1 − ½Tr U_p).
Pinned input: this branch on top of `f76f6c649cff`.

Literature is used only as follows: Dobrushin–Shlosman (1985, constructive uniqueness criterion), Martinelli–Olivieri (1994,
finite-size mixing conditions), Osterwalder–Seiler (Ann. Phys. 110 (1978) 440: RP, strong-coupling cluster expansion), Bałaban
(CMP 1984–89: RG in finite volume), Kotecký–Preiss (CMP 103 (1986) 491: polymer convergence criterion; Borgs for related
cluster-expansion technology). **The continuous-spin form of the DS condition used in Part 1 must be checked against the 1985 original
before any producer relies on it.**

---

## 0. MDTN finding (what "the MDTN truncation" is, and what it can do for CW)

* MDTN = Monomer–Dimer Tensor-Network basis (Chandrasekharan–Siew–Bhattacharya, arXiv:2502.14175, Phys. Rev. D 111, 114502 (2025)),
  used with the ASQR truncation: SU(2) irreps {0, ½} only, i.e. j_max = ½. Author-side local exploration notes (a strong-coupling
  Hamiltonian gap lemma and small exact-diagonalization runs) are **not committed** to this repository and are not relied on here.
  No MDTN material was found on main or in PRs #10114 or #10132 (for #10114, only the first 1000 changed files were searchable through
  the API).
* What those local notes indicate (not relied on): a volume-uniform Hamiltonian gap in the strong-coupling, electric-dominated regime,
  and that the j_max = ½ gap is a truncation artefact at weak coupling.
* **Quantified here** ([checks/cw/rigorous_bounds.py](checks/cw/rigorous_bounds.py), part 4): the sup-norm error, relative to c_0, of truncating the plaquette Boltzmann
  weight's character expansion at spin J is τ_J(β) = Σ_{j>J} (2j+1)² a_j(β), a_j = I_{2j+1}(β)/I_1(β):

| β | J=½ | J=1 | J=3/2 | J=2 | J=3 | J=4 | J=6 |
|---|---|---|---|---|---|---|---|
| 0.5 | 1.03e-1 | 1.11e-2 | 8.5e-4 | 5.0e-5 | 9.8e-8 | 1.1e-10 | 3.3e-17 |
| 1.0 | 0.444 | 9.1e-2 | 1.4e-2 | 1.6e-3 | 1.2e-5 | 5.2e-8 | 2.6e-13 |
| 2.0 | 1.91 | 0.709 | 0.199 | 4.4e-2 | 1.3e-3 | 2.1e-5 | 1.6e-9 |
| 2.3 | 2.55 | 1.05 | 0.332 | 8.4e-2 | 3.2e-3 | 6.8e-5 | 9.1e-9 |
| 3.0 | 4.35 | 2.16 | 0.846 | 0.269 | 1.65e-2 | 5.9e-4 | 2.2e-7 |
| 4.0 | 7.56 | 4.48 | 2.16 | 0.864 | 8.7e-2 | 5.2e-3 | 5.8e-6 |

  Conclusion: **the j_max = ½ (ASQR/MDTN) truncation is not a controlled approximation anywhere in the crossover window** (τ_½ > 1 for
  β ≳ 1.5). A truncated transfer matrix with an *arb-certified tail* is only usable with J ≈ 3–6 at β ≈ 2–3, i.e. local link dimension
  Σ_{j≤J}(2j+1)² = 140 (J=3) to 819 (J=6). That rules out exact diagonalization of anything but a few links. MDTN is useful for H4-type
  strong-coupling statements, **not** for CW. Series matching via truncated transfer matrices would need certified j_max ≥ 3 blocks.

---

## Part 1. A checkable finite-volume criterion CW_ℓ(β)

**Setting.** Links are the spins; single-spin space SU(2) (compact, not finite). A specification is given by the action; for a finite link
set V and boundary condition ξ, μ_V^ξ is the conditional law on SU(2)^V.

**Dobrushin–Shlosman-type condition (C_V).** For a finite V and a link y ∉ V adjacent to V (shares a plaquette), set
  k_{V,y} = Σ_{x∈V} sup_{ξ = ξ' off y} d(μ_V^ξ|_x, μ_V^{ξ'}|_x),
with d a suitable distance between one-site marginals (TV, or a Wasserstein distance). The DS-type condition is Σ_{y} k_{V,y} < |V|.
DS 1985 show conditions of this type imply uniqueness and exponential decay of correlations. The precise form of their condition, which
distance they use, and whether it covers compact continuous spins with finite-range interactions must be checked against the original
paper before it goes in a PR. |V| = 1 is the classical Dobrushin condition; that case is done rigorously in Part 2.

**Gauge-theory complications (explicit).**
1. *Gauge triviality of marginals.* If V contains all 8 links at some site s, then μ_V^ξ is invariant under gauge transformations at s, and
   the link marginals at s are Haar whatever ξ is, so k_{V,y} is trivially small there. That is a false signal. Fix: either (i) restrict to
   link sets V with no interior site (every site of V has a link outside V; single links and "slabs of plaquettes" qualify), or (ii) replace
   one-site marginals by laws of **gauge-invariant** local functions (plaquettes or small Wilson loops in V), i.e. work on the quotient by the
   gauge group of the interior sites. The output of (C_V) is then decay of truncated correlations for gauge-invariant observables, which is
   all A2 needs.
2. *Boundary changes as gauge moves.* Changing a boundary link y = (s_out, s_in) with s_in a site of V is, on gauge-invariant functions of
   V, the same as a gauge rotation at s_in applied to the other outer links at s_in (at most 7 in d = 4). So k_{V,y} is controlled by how V
   responds to a *rotation of a face*, not just a single-link perturbation. Parallel (non-crossing) outer links enter through staples only.
   Their TV effect is O(β) at strong coupling and O(1) in general.
3. *No-go sanity check.* Any valid CW_ℓ must **fail** for compact U(1) Wilson theory in d = 4 at weak coupling (massless phase; see MASS_GAP_CROSSOVER_REDUCTION §5 item 4), and must use non-abelian structure (MASS_GAP_CROSSOVER_REDUCTION §5 item 4). The single-link condition passes this check trivially because it
   only holds at strong coupling for any group.
4. *Martinelli–Olivieri.* Their finite-size criteria (1994) are for finite single-spin spaces. As far as I know, no extension to Lie-group
   spins exists in the literature. Do not cite MO for gauge theories without such an extension.
5. *Doob/contraction alternative.* [MASS_GAP_LOCAL_BLOCK_ASTRA.md](MASS_GAP_LOCAL_BLOCK_ASTRA.md) uses a Doob-kernel contraction (r(β) = β/(1−Q), Q = 12β + β²/(1−14β), r ≤ 18/359 at β ≤ 1/32).
   That is a block criterion of the same family.

**Definition (CW_ℓ(β)).** For a translation-invariant, finite-range (or exponentially decaying) gauge-invariant link specification γ,
CW_ℓ(γ) holds if there is a link set V of diameter ≤ ℓ, satisfying 1(i) or measured as in 1(ii), with
  α_V(γ) := |V|^{-1} Σ_y k_{V,y}(γ) < 1.

**Checkability.** α_V is a supremum over a compact set of boundary conditions of differences of finite-dimensional integrals over
SU(2)^{|V|}. It is computable to any accuracy by interval branch-and-bound, but the cost grows like (grid)^{#boundary links}. Realistically
only |V| = 1 (done below) and perhaps |V| ≤ 3 with heavy symmetry reduction are feasible. Monte Carlo estimates of α_V are heuristic only.

**Stability (the useful structural fact).** α_V(γ) depends continuously on the interaction restricted to V ∪ ∂V (TV distances are
1-Lipschitz in the log-density sup norm up to a factor e^{2‖δ‖}−1). Hence **{γ : α_V(γ) < 1 − η} is open**: if γ_0 is verified with
margin η and ‖γ − γ_0‖ ≤ δ(η, V), then CW_ℓ(γ) holds. This is what lets an RG output that is *close* to a verified action inherit the
criterion.

---

## Part 2. Rigorous strong coupling: Dobrushin beats 1/32, KP does not

Scripts: [checks/cw/rigorous_bounds.py](checks/cw/rigorous_bounds.py) (output `checks/cw/data/rigorous_bounds_out.txt`, `.json`) and [checks/cw/var_certificate.py](checks/cw/var_certificate.py) (output `checks/cw/data/var_certificate_out.txt`, `.json`).

**2.0 Normalization check.** c_j(β) = ∫ e^{β cos θ} χ_j dU = 2(2j+1) I_{2j+1}(β)/β, so a_j = c_j/(d_j c_0) = I_{2j+1}/I_1. Checked against
direct Haar (Weyl-measure) quadrature at β ∈ {0.1, 0.5, 1, 2.3}, j ≤ 2. Max discrepancy: 2.0e-31. Example: a_½(0.5) = 0.123718.

**2.1 Single-link Dobrushin.** In d = 4 each link lies in 6 plaquettes and has 18 neighbours; two distinct links share at most one plaquette.
Writing U_i as a unit quaternion u ∈ S³, the conditional density is ∝ exp(β⟨u, a⟩), with a = sum of 6 unit staple vectors, so |a| ≤ 6β.
Changing a neighbour U_j moves exactly one staple: |δa| ≤ 2β.

*Certified route (interval arithmetic).* This is an exponential family on S³ with log-partition A. Then KL(μ_a‖μ_{a'}) ≤ ½ sup λ_max(Cov_w)·|δ|².
By symmetry, Cov_w is diagonal in (ŵ, ŵ^⊥):
* Var_⊥ = (1 − E t²)/3 ≤ 1/4, since E_κ t² ≥ E_0 t² = 1/4. This is the Chebyshev association inequality: t² and cosh κt both increase in |t|.
* Var_∥(κ) = R′ = 1 − R² − 3R/κ, with R = I₂/I₁. The identity was checked against quadrature to 2.6e-31. Var_∥ < 1/4 is **certified with arb**
  on κ ∈ (0, 1.2], using 29,602 cells: the small-κ Taylor bound with |κ₆| ≤ 1082 covers κ ≤ 0.0263, and monotone-R cell bounds cover the
  rest. The maximum cell upper bound is 0.249991.

Hence KL ≤ β²/2. Pinsker gives TV ≤ β/2, so C_ij ≤ β/2 and

  **q(β) = Σ_j C_ij ≤ 9β < 1 for β < 1/9 (certified; uses 6β ≤ 1.2).**

*Validated-numerics route (sharper, not interval-certified).* The path bound C_ij ≤ β·M(6β), with M(K) = sup_{κ≤K, e} MAD of ⟨u,e⟩ under the
tilted law. This reduces exactly to a 1-D integral (S³ → 2-plane projection is uniform on the disk). Grid over κ ∈ [0, 0.8] in steps of 0.01,
and φ in steps of π/80, with Lipschitz margin 0.049 (constants ≤ 2 in κ and in φ). The maximum is at κ = 0 with value 4/(3π) = 0.42441.
Result: M ≤ 0.4737, so **β_D ≥ 0.1173 (validated)**. If the supremum really is at κ = 0, as the grid indicates, then β_D = 3π/72 = 0.1309.

*Consequences.* For SU(2) Wilson in d = 4, every β < 1/9 gives uniqueness of the infinite-volume Gibbs state and |Cov(F, τ_n G)| ≤
C_{F,G} q^{n−c}/(1−q), uniformly in the torus size. With RP (H1) and A2, this gives the volume-uniform lattice gap **m_lat ≥ −log(9β)**:

| β | q_cert = 9β | m_lat ≥ (cert) | q_valid | m_lat ≥ (valid) |
|---|---|---|---|---|
| 1/32 | 0.281 | 1.27 | 0.266 | 1.32 |
| 0.05 | 0.450 | 0.80 | 0.426 | 0.85 |
| 0.08 | 0.720 | 0.33 | 0.682 | 0.38 |
| 0.10 | 0.900 | 0.105 | 0.853 | 0.16 |

Compared with what exists: MASS_GAP_LOCAL_BLOCK_ASTRA's 18β row bound gives β < 1/18, and its Doob contraction gives β ≤ 1/32 with the stronger mass bound
−log(18/359) ≈ 2.99 at 1/32. **The new result extends the strong-coupling range by a factor 32/9 ≈ 3.6 in β (author-side, review pending)** (from g² ≥ 128 down
to g² > 36). It is weaker in mass at very small β.

**2.2 Kotecký–Preiss for the character expansion (honest negative).** Polymers are link-connected plaquette sets X with |w(X)| ≤ ε^{|X|},
ε = Σ_{j≥½} d_j² a_j. The activity is zero unless every link is covered at least twice, so |X| ≥ 6. The plaquette-graph degree is Δ = 20. The KP condition
6 Σ_{n≥6} D^{n−1}(εe^a)^n ≤ a/4 was checked with arb, including a rigorous Bessel tail I_ν(x) ≤ (x/2)^ν e^{x²/4}/Γ(ν+1).

| counting bound | β_KP | a | ε(β_KP) |
|---|---|---|---|
| self-contained D = 4Δ = 80 | 0.00776 | 0.120 | 0.00778 |
| standard lattice-animal D = eΔ (not re-proved here) | 0.01088 | 0.124 | 0.0109 |

**Both are below 1/32.** A naive KP character expansion does not improve the strong-coupling threshold. Dobrushin does. Window
(qualitative): **[β_D, β_Bal)** with β_D ∈ [1/9, ≈0.131] and β_Bal = 4/ḡ², where Balaban's ḡ is not explicit. On the numerics below, the
physics crossover sits near β ≈ 2–2.3 (g² ≈ 1.7–2). So the window spans at least a factor ~20 in β, and the new bound narrows it only
modestly.

---

## Part 3. Monte Carlo evidence (EVIDENCE ONLY; Wilson action, not the Balaban effective action; flag C4)

Code: `checks/cw/su2_mc.py` (Kennedy–Pendleton heat-bath + 3 overrelaxation sweeps, checkerboard). Scan: `checks/cw/run_scan.sh` (150 therm + 500 meas
sweeps, 40 runs). Analysis: `checks/cw/analyze_mc.py` → `checks/cw/data/mc_summary.{txt,json}`, `checks/cw/data/sc_wc_compare.txt`. Raw per-run JSON (~6.7 MB) is not committed. Compute used: 30.9 min user +
3.1 min sys CPU, about 10 min wall on 8 cores. That is slightly over the ~30 CPU-min target. Errors are jackknife with 20 bins.

Selected 8⁴ results (cold start):

| β | ⟨P⟩ | u = I₂/I₁ | (P−u)/u | dP/dβ = N_p Var P | Creutz χ(2,2) | −log u |
|---|---|---|---|---|---|---|
| 0.5 | 0.12380(12) | 0.12372 | 0.0006 | 0.24(2) | noisy | 2.09 |
| 1.0 | 0.24325(14) | 0.24019 | 0.013 | 0.22(2) | 1.46(4) | 1.43 |
| 1.5 | 0.36242(20) | 0.34414 | 0.053 | 0.24(1) | 1.000(9) | 1.07 |
| 2.0 | 0.50070(30) | 0.43313 | 0.156 | 0.32(2) | 0.598(2) | 0.84 |
| 2.2 | 0.56867(23) | 0.46448 | 0.224 | 0.33(3) | 0.407(1) | 0.77 |
| 2.3 | 0.60271(36) | 0.47928 | 0.258 | 0.33(2) | 0.316(1) | 0.74 |
| 2.5 | 0.65239(20) | 0.50720 | 0.286 | 0.21(2) | 0.211(1) | 0.68 |
| 3.0 | 0.72333(10) | 0.56792 | 0.274 | 0.11(1) | 0.132(0) | 0.57 |
| 4.0 | 0.79960(8) | 0.65805 | 0.215 | 0.052(2) | 0.080(0) | 0.42 |

Observations (evidence, not proof):
* **Smoothness.** ⟨P⟩(β) is smooth. Hot and cold starts agree at β = 2.2, 2.3, 2.5 (0.56903(38) vs 0.56867(23); 0.60223(35) vs 0.60271(36);
  0.65235(21) vs 0.65239(20)), so there is no hysteresis. dP/dβ peaks at about 0.33–0.38 for β ≈ 2.1–2.3 and does **not** grow from L = 4 → 6 → 8
  (peak values 0.46(4), 0.37(3), 0.38(3)). That pattern fits a crossover and does not fit a bulk transition at these volumes.
* **Strong-coupling series matching.** Leading-order ⟨P⟩ ≈ u holds to 0.06% at β = 0.5 and 1.3% at β = 1, then fails fast (5% at 1.5, 16% at 2.0).
  The Creutz ratio tracks the leading strong-coupling string tension −log u up to β ≈ 1.25 and then drops below it. Weak-coupling check: (1−P)·4β/3
  falls toward 1 (1.07 at β = 4), consistent with ⟨1−P⟩ ≈ 3/(4β).
* **Correlation-length proxy.** The Creutz ratio falls smoothly by about 12× between β = 1 and 4. The 0⁺⁺ effective mass from time-slice plaquette
  correlators is **too noisy to be informative** at this statistics (errors comparable to the values). It is reported in the JSON but not used.
  Polyakov |⟨P_L⟩| stays at the finite-volume noise level (≈ 0.018 on 8⁴) up to β ≈ 2.3 and then rises. That is the finite-T deconfinement
  crossover for N_t = 8, not a bulk effect.
* **What this says about CW.** In the window β ∈ [0.11, ~2] nothing singular is visible, but leading-order strong-coupling control is lost
  already near β ≈ 1. Any rigorous route must either push a block criterion to β ~ 2, or start Balaban's flow from β_Bal down to there.

Caveats: small volumes and modest statistics. The scan used the Wilson action, while CW concerns the effective action (C4). Integrated autocorrelation
times were not measured separately; binning in 20 jackknife bins of 25 sweeps partly accounts for them.

---

## Part 4. Refined conditional theorem

**Proposition S (author-side proof, independent review pending; SU(2), d = 4).** For 0 < β < 1/9, the Wilson Gibbs specification satisfies CW_1 (single-link Dobrushin, q ≤ 9β).
Consequently the infinite-volume state is unique, truncated correlations of local observables decay at rate ≥ −log(9β) per lattice step,
uniformly in the torus, and (with H1, A2) spec(H_a) ⊂ {0} ∪ [−a^{−1} log(9β), ∞). This replaces β_sc = 1/32 by 1/9 in H4 for SU(2) (with a weaker
mass at tiny β). Rigour: the variance bound is arb-certified ([checks/cw/var_certificate.py](checks/cw/var_certificate.py)). The remaining steps are elementary (Pinsker, the KL Hessian
bound, the Dobrushin uniqueness theorem). The decay-to-gap step is MASS_GAP_TARGET §2 (step A2 of MASS_GAP_CROSSOVER_REDUCTION). *This needs independent review before it goes in a PR.*

**Theorem H′ (conditional).** Assume H1–H6 for SU(N), d = 4, and

> **CW′.** There exist a finite link set V (diameter ℓ), a margin η > 0, a reference specification γ_0 with α_V(γ_0) ≤ 1 − 2η, and a fixed
> number n_* of further RG steps after k_1(a), such that, **uniformly in the volume and in a**, the effective theory at scale ℓ_* = L_b^{n_*} ℓ_1,
> written as a gauge-invariant link specification γ_{a,Λ}, satisfies ‖γ_{a,Λ} − γ_0‖_V ≤ δ(η, V). Hence α_V(γ_{a,Λ}) < 1 − η, i.e. CW_ℓ holds.
> In addition, the RG map transports decay of the effective gauge-invariant correlations back to the original observables with sources,
> without loss of rate.

Then the conclusion of Theorem H holds, with μ_* ≥ −log(1 − η)/(c ℓ) in units of ℓ_*.

*What changed relative to H:* CW ("some clustering estimate in the window") is replaced by a **finite-dimensional, open condition** on one block
(CW_ℓ) plus a **landing statement** (the flow ends δ-close to a verified specification). The verification half is computable in principle
(Part 1), and for |V| = 1 it is done up to β < 1/9 (Prop. S). For example, with γ_0 = Wilson at β_0 < 1/9, CW′ asks that the effective
action at scale ℓ_* be δ-close to strong-coupling Wilson.

**Circularity and validity flags (extend C1–C5 of MASS_GAP_CROSSOVER_REDUCTION §6).**
* **C6 (effective action, not Wilson).** CW_ℓ must be verified for γ_{a,Λ}, the Balaban effective action. That action has large-field regions,
  auxiliary/background fields, and non-local but exponentially decaying polymers. It is not a finite-range link specification, so (C_V) in a
  form valid for exponentially decaying interactions is needed. Wilson-action numerics (Part 3) do **not** verify it.
* **C7 (no use of the conclusion).** The landing bound ‖γ_{a,Λ} − γ_0‖ ≤ δ must come from RG estimates (Balaban-type small-field control
  continued past ḡ, or a computer-assisted RG step). It must **not** use decay of correlations of the effective theory, which is what CW_ℓ is
  meant to produce.
* **C8 (the real gap).** Balaban's control ends at g ≤ ḡ (weak coupling). Prop. S starts at g² > 36. Landing near *strong-coupling Wilson*
  would require the RG to carry the effective coupling from ḡ up to g² ≈ 36 with controlled remainders. That is exactly the non-perturbative
  part, and nothing here supplies it. Choosing a better γ_0 (larger-block CW_ℓ verified at β ~ 1–2) would shorten the gap, but block
  verification there is computationally out of reach on present methods (Part 1, checkability; τ_J table in §0).
* **C9 (MO not available).** Martinelli–Olivieri finite-size criteria cannot be cited for SU(N) spins without a new extension.

## Part 5. What remains open
1. CW′'s landing statement (C8). This is still the Clay-level core.
2. Rigorous DS (C_V) for |V| > 1 for SU(2) Wilson, which would push Prop. S beyond 1/9. The sharper single-link value 0.131 also needs an
   interval proof that the MAD supremum is at κ = 0.
3. The DS theorem in a form covering compact Lie-group spins and exponentially decaying gauge-invariant interactions (C6).
4. Prop. S for SU(3): the same method applies, but the variance/Lipschitz constants and the neighbour count must be redone. Not computed here.

Files: [checks/cw/](checks/cw/README.md) (scripts, outputs, reproduction notes).

## Not claimed

No MG row is closed. CW is open. Prop. S is author-side and needs independent review; it changes the H4 threshold for SU(2)
only once reviewed. Monte Carlo results are evidence about the Wilson action only.
