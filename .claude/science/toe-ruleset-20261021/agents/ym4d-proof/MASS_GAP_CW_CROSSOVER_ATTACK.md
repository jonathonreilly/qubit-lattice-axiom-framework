# Mass-gap CW crossover attack (conditional-support; closes no MG row)

Author checkpoint, 1 November 2026; editorial restatement (statement form, status labels, isolation of computer-assisted
steps) on the same date. **The four-dimensional continuum existence and physical mass-gap target remains open; CW remains
open.** This unit continues [MASS_GAP_CROSSOVER_REDUCTION.md](MASS_GAP_CROSSOVER_REDUCTION.md) (cited below as RED).
The editorial pass changed no mathematical content. Gaps found during it are listed in §6 as open items; they were not fixed.

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: conditional-support
independent_review: pending
MG_rows_closed: []
```

**Summary of content (each item is restated below with hypotheses and status).**
(a) Proposition S: single-link Dobrushin uniqueness for SU(2) Wilson in d = 4 at β < 1/9, **conditional on Open Lemma OL-S1**
(a one-variable Bessel-function inequality for which only computer-assisted evidence exists). (b) Computed observation O-KP: a
simple Kotecký–Preiss bound does not reach β = 1/32. (c) A finite-block criterion CW_ℓ (Definition 1.4), an openness statement
(Lemma 1.7, proof not written), and Theorem H′, which is Theorem H of RED with CW replaced by CW′. (d) Monte Carlo runs, moved
to Appendix N, **not used in any proof**. No MG row changes status.

## 0. Conventions

**Status labels.** Every numbered statement carries one of:
* **[proved here]**: a complete argument is given in this note (independent review still pending for the whole note);
* **[cited: ref]**: taken from the literature at the exact reference given; the reference list is in RED §References;
* **[open]** / **Open Lemma**: a precise statement that is *not* proved here. Every computer-assisted step is isolated as an
  Open Lemma or as a Computed observation; no proved statement rests on a computation;
* **Conjecture**: a statement believed true, no proof, not used;
* **Computed observation**: a number produced by a script in [checks/cw/](checks/cw/README.md); not a theorem, not used in
  any proof;
* **Remark / Heuristic**: explanation only; no claim of proof.

**Model.** RED §1 at N = 2: Λ a periodic hypercubic lattice in d = 4, link variables U_e ∈ SU(2), Wilson weight
exp{(β/2) Σ_p Tr U_p}, β = 4/g_0², equivalently S = β Σ_p (1 − ½ Tr U_p). Identify SU(2) with the unit quaternions
S³ ⊂ R⁴, with ⟨·,·⟩ the Euclidean inner product on R⁴ (so ½ Tr(U V^†) = ⟨u, v⟩). Pinned input: this branch on top of
`f76f6c649cff`.

**Literature used and its role.** Dobrushin (1968) and Föllmer (1982) for the single-site uniqueness theorem and covariance
estimate; Dobrushin–Shlosman (1985) for block criteria (Open Lemma OL-DS: the form needed here is not verified against the
original); Martinelli–Olivieri (1994), used only to note that it does *not* apply; Osterwalder–Seiler (1978); Bałaban
(CMP 1984–89); Kotecký–Preiss (1986). Exact references: RED §References.

---

## 1. Definitions and the block criterion CW_ℓ

**Definition 1.1 (link specification).** A *gauge-invariant link specification* γ on Z⁴ is a family of probability kernels
γ_V(dU_V | ξ), indexed by finite link sets V, with ξ ∈ SU(2)^{E∖V} the boundary configuration, which is consistent, invariant
under lattice translations, and invariant under gauge transformations. The Wilson specification γ^W_β has
γ_V(dU_V | ξ) ∝ exp{(β/2) Σ_{p ∩ V ≠ ∅} Tr U_p} Π_{e∈V} dU_e. Write μ_V^ξ := γ_V(· | ξ).

**Definition 1.2 (Dobrushin interdependence matrix).** For links i ≠ j set
C_ij := sup { ‖μ_{{i}}^ξ − μ_{{i}}^{ξ'}‖_TV : ξ, ξ' agree off j }, with ‖·‖_TV the total-variation distance, and
q(γ) := sup_i Σ_{j≠i} C_ij. *Dobrushin's condition* is q(γ) < 1.

**Definition 1.3 (block coefficient).** For a finite link set V, a link y ∉ V sharing a plaquette with V, and a distance d
on probability measures on SU(2) (TV or a Wasserstein distance), set
k_{V,y}(γ) := Σ_{x∈V} sup { d(μ_V^ξ|_x, μ_V^{ξ'}|_x) : ξ, ξ' agree off y },
and α_V(γ) := |V|^{-1} Σ_y k_{V,y}(γ). (For |V| = 1 and d = TV, α_{{i}} = Σ_j C_ij.)

**Definition 1.4 (CW_ℓ).** CW_ℓ(γ) holds if there is a link set V of diameter ≤ ℓ that satisfies Remark 1.6(1)(i), or is
measured as in Remark 1.6(1)(ii), with α_V(γ) < 1.

**Definition 1.5 (CW′ and landing).** Stated inside Theorem H′, §4. "Landing" means the closeness clause
‖γ_{a,Λ} − γ_0‖_V ≤ δ(η, V) of CW′.

**Remark 1.6 (gauge-theory complications; explanation, no claim).**
1. *Gauge triviality of marginals.* If V contains all 8 links at a site s, then μ_V^ξ is invariant under gauge
   transformations at s, so the link marginals at s are Haar for every ξ and k_{V,y} is trivially small there. That is a
   false signal. Either (i) restrict to link sets V with no interior site (every site of V has a link outside V; single links
   and slabs of plaquettes qualify), or (ii) replace one-link marginals by laws of gauge-invariant local functions in V
   (plaquettes, small Wilson loops), i.e. work on the quotient by the gauge group of the interior sites. The output is then
   decay of truncated correlations of gauge-invariant observables, which is what RED Lemma A2 uses.
2. *Boundary changes as gauge moves.* Changing a boundary link y = (s_out, s_in) with s_in a site of V acts on
   gauge-invariant functions of V like a gauge rotation at s_in applied to the other outer links at s_in (at most 7 in
   d = 4). So k_{V,y} measures the response of V to a rotation of a face, not only to a single-link perturbation. Parallel
   outer links enter through staples only; their effect in TV is O(β) at strong coupling and O(1) in general (Heuristic).
3. *Scope test, not a no-go.* A valid CW_ℓ verification must not hold for compact U(1) Wilson theory in d = 4 at weak
   coupling, which has a proved massless phase (Guth 1980; Fröhlich–Spencer 1982; RED Remark 5.4). The single-link condition
   is consistent with this, because it holds only at strong coupling for any group.
4. *Martinelli–Olivieri.* Their finite-size mixing criteria (CMP 161 (1994)) are for finite single-spin spaces. I know of no
   extension to Lie-group spins and do not cite MO for gauge theories (flag C9).
5. *Doob contraction.* [MASS_GAP_LOCAL_BLOCK_ASTRA.md](MASS_GAP_LOCAL_BLOCK_ASTRA.md) uses a Doob-kernel contraction
   r(β) = β/(1−Q), Q = 12β + β²/(1−14β), r ≤ 18/359 at β ≤ 1/32: a block criterion of the same family.

**Remark 1.6a (checkability; Heuristic).** α_V(γ) is a supremum over a compact set of boundary conditions of differences of
finite-dimensional integrals over SU(2)^{|V|}. In principle it can be bounded to any accuracy by interval branch-and-bound,
at a cost that grows like (grid size)^{#boundary links}. Only |V| = 1 is done (Prop. S below, conditional on OL-S1).
Monte Carlo estimates of α_V would be heuristic only.

**Lemma 1.7 (openness of the block criterion) [stated; proof not written — open item OI-3].** Fix V. α_V(γ) depends
continuously on the interaction restricted to V ∪ ∂V, in the sup norm of log-densities. Hence for each η > 0 there is
δ(η, V) > 0 such that α_V(γ_0) ≤ 1 − 2η and ‖γ − γ_0‖_V ≤ δ(η, V) imply α_V(γ) < 1 − η.
*Status.* The source text justifies this by "TV distances are 1-Lipschitz in the log-density sup norm up to a factor
e^{2‖δ‖} − 1". That inequality is not derived in the note, and the norm ‖·‖_V is not defined precisely. Recorded as OI-3.

**Open Lemma OL-DS (block criterion ⇒ uniqueness and decay, for the specifications needed here) [open; source to be checked].**
*Statement needed.* If a gauge-invariant link specification γ (finite range, or with exponentially decaying interactions)
satisfies α_V(γ) ≤ 1 − η for some finite V as in Definition 1.4, then γ has a unique Gibbs measure, and truncated correlations
of bounded gauge-invariant local observables decay exponentially in distance with a rate depending only on (η, V), uniformly
in finite periodic volumes.
*Status.* Dobrushin–Shlosman, "Constructive criterion for the uniqueness of Gibbs field" (1985), proves uniqueness under
finite-volume conditions C_V for translation-invariant potentials; exponential decay is associated with the companion paper
"Completely analytical Gibbs fields" (same volume, p. 371 ff.). Whether either covers compact continuous single-spin spaces,
gauge-invariant (quotient) observables, and exponentially decaying interactions, and in which distance, has **not** been
checked against the originals. Until it is, OL-DS is open (open item OI-5). For |V| = 1 the classical Dobrushin theorem
(Theorem 2.0) is used instead and OL-DS is not needed.

---

## 2. Single-link Dobrushin for SU(2), d = 4 (Proposition S)

Scripts: [checks/cw/var_certificate.py](checks/cw/var_certificate.py) (evidence for OL-S1 only) and
[checks/cw/rigorous_bounds.py](checks/cw/rigorous_bounds.py) (computed observations only).

**Theorem 2.0 (Dobrushin uniqueness and covariance decay) [cited: Dobrushin, Theory Probab. Appl. 13 (1968) 197–224;
Föllmer, J. Funct. Anal. 46 (1982) 387–395; textbook form: Georgii, *Gibbs Measures and Phase Transitions* (1988), Ch. 8].**
For a specification on a countable set of sites with standard Borel single-spin spaces, q(γ) < 1 implies that there is at most
one Gibbs measure, and covariances of local functions decay exponentially in the graph distance generated by the matrix
(C_ij), with rate −log q. The same estimate holds for the finite-volume periodic measures.
*Status note (open item OI-6).* The exact theorem numbers and the precise form of the covariance bound used below,
|Cov(F, τ_n G)| ≤ C_{F,G} q^{n−c}/(1−q), including the constant c and its passage from link-graph distance to time distance,
are not pinned to a specific statement in these sources in this pass.

**Lemma 2.1 (geometry) [proved here].** In Z⁴ each link lies in exactly 6 plaquettes, the set of links sharing a plaquette
with a given link has 18 elements, and two distinct links share at most one plaquette.
*Proof.* A link in direction μ lies in 2 plaquettes for each of the 3 directions ν ≠ μ; each plaquette contributes 3 other
links, and the 18 links so obtained are distinct; two links determine at most one plaquette. ∎

**Lemma 2.2 (conditional law of one link) [proved here].** Under γ^W_β, the conditional law of U_i given the other links is
the probability measure on S³ with density ∝ exp⟨u, a⟩ with respect to normalized surface measure, where a = β Σ_{p∋i} s_p and
s_p ∈ S³ is the (quaternion of the) staple of plaquette p. Hence |a| ≤ 6β, and changing one neighbour U_j changes exactly one
staple, so |δa| ≤ 2β.

**Lemma 2.3 (KL bound for an exponential family) [proved here; standard].** For the family μ_a(du) ∝ exp⟨u, a⟩ du on S³,
with log-partition A(a) and covariance Cov_a = ∇²A(a),
KL(μ_a ‖ μ_{a'}) ≤ ½ sup_{w ∈ [a, a']} λ_max(Cov_w) · |a − a'|².
*Proof.* KL(μ_a‖μ_{a'}) = A(a') − A(a) − ⟨∇A(a), a' − a⟩; Taylor's theorem with the mean-value form of the remainder. ∎

**Lemma 2.4 (transverse variance) [proved here].** Write w = κŵ with κ = |w|, and t = ⟨u, ŵ⟩. Then Cov_w is diagonal in the
decomposition R ŵ ⊕ ŵ^⊥, with eigenvalue Var_∥(κ) := Var_w(t) on R ŵ and eigenvalue Var_⊥(κ) := (1 − E_κ t²)/3 on ŵ^⊥ (multiplicity 3),
and Var_⊥(κ) ≤ 1/4 for all κ ≥ 0.
*Proof.* Rotational symmetry about ŵ gives the diagonal form and mean zero for the transverse coordinates, whose squares sum to
1 − t². The law of t has density ∝ √(1−t²) e^{κt} on [−1, 1]. By symmetry E_κ t² = E_0[t² cosh κt]/E_0[cosh κt], and
t² and cosh κt are both nondecreasing in |t|, so Chebyshev's association inequality gives E_κ t² ≥ E_0 t² = 1/4. ∎

**Lemma 2.5 (parallel variance identity) [proved here; standard Bessel identities].** With R(κ) := I₂(κ)/I₁(κ),
E_κ t = R(κ) and Var_∥(κ) = R′(κ) = 1 − R(κ)² − 3R(κ)/κ for κ > 0, and lim_{κ→0} Var_∥(κ) = 1/4.
*Proof.* ∫_{−1}^{1} √(1−t²) e^{κt} dt = π I₁(κ)/κ, so E_κ t = d/dκ log(I₁(κ)/κ) = R(κ) by I₁′ = I₂ + I₁/κ; then
Var_∥ = R′ = 1 − R² − 3R/κ by I₂′ = I₁ − 2I₂/κ. The limit is E_0 t² = 1/4. ∎
(The identity was also cross-checked numerically against quadrature to 2.6e-31; that check is not part of the proof.)

**Open Lemma OL-S1 (parallel variance bound) [open; computer-assisted evidence only].**
For every κ ∈ (0, 2/3]:  Var_∥(κ) = 1 − R(κ)² − 3R(κ)/κ ≤ 1/4,  where R = I₂/I₁.
*Why this range.* Proposition S needs λ_max(Cov_w) ≤ 1/4 for |w| ≤ 6β with β < 1/9, i.e. κ < 2/3.
*What is proved toward it [proved here].* (i) Small κ: Var_∥ is even and real-analytic in κ, with Var_∥(0) = 1/4 and
Var_∥″(0) = κ₄(0) = E_0 t⁴ − 3(E_0 t²)² = 1/8 − 3/16 = −1/16; the fourth derivative is the sixth cumulant κ₆ of t under the tilted
law, and |κ₆| ≤ 1082 (the sum of the absolute coefficients of κ₆ in terms of raw moments, all of which lie in [−1, 1]). Taylor's
theorem gives Var_∥(κ) ≤ 1/4 − κ²/32 + 1082 κ⁴/24, which is ≤ 1/4 for κ ≤ κ₀ := (24/(32·1082))^{1/2} ≈ 0.02633.
(ii) Reduction to finitely many inequalities: R is increasing (R′ = Var_∥ > 0) and nonnegative, so for 0 < lo ≤ κ ≤ hi,
Var_∥(κ) ≤ 1 − R(lo)² − 3R(lo)/hi. Hence OL-S1 on [κ₀, 2/3] follows from finitely many inequalities
1 − R(lo_m)² − 3R(lo_m)/hi_m ≤ 1/4 over any finite cover of [κ₀, 2/3] by cells [lo_m, hi_m] on which they hold.
*What is open.* A pen-and-paper verification of those finitely many inequalities, or any other analytic proof of OL-S1 on
[κ₀, 2/3]. **Computer-assisted evidence (not a proof in this note):** `var_certificate.py` evaluates the cell inequalities with
arb ball arithmetic on 29,602 cells covering [0.999κ₀, 1.2] and reports a maximum cell upper bound of 0.249991 < 1/4
(`checks/cw/data/var_certificate_out.txt`). The computation covers (0, 1.2], more than the range needed. It has not been
independently re-run or reviewed.

**Proposition S (SU(2), d = 4; conditional on OL-S1) [proved here modulo OL-S1 and Theorem 2.0; independent review pending].**
Assume OL-S1. Then for 0 < β < 1/9 the Wilson specification γ^W_β satisfies C_ij ≤ β/2 for every pair of neighbouring links
and q(γ^W_β) ≤ 9β < 1. In particular CW_1(γ^W_β) holds with d = TV.
*Proof.* By Lemma 2.2, C_ij ≤ sup ‖μ_a − μ_{a'}‖_TV over |a|, |a'| ≤ 6β, |a − a'| ≤ 2β; the segment [a, a'] lies in the ball of
radius 6β < 2/3. By Lemmas 2.4–2.5 and OL-S1, λ_max(Cov_w) ≤ 1/4 on that ball. Lemma 2.3 gives KL ≤ ½ · ¼ · (2β)² = β²/2,
and Pinsker's inequality gives TV ≤ (KL/2)^{1/2} = β/2. Lemma 2.1 gives 18 neighbours, so q ≤ 18 · β/2 = 9β. ∎

**Corollary S′ (lattice gap at strong coupling; conditional) [conditional on OL-S1, Theorem 2.0 in the form noted in OI-6,
RED H1 and RED Lemma A2].** For 0 < β < 1/9 the infinite-volume Gibbs state is unique, truncated correlations of bounded local
gauge-invariant observables decay at rate ≥ −log(9β) per lattice step uniformly in the periodic volume, and
spec(H_a) ⊂ {0} ∪ [−a^{−1} log(9β), ∞), ker H_a = span{Ω_a}.
*Status.* This would replace β_sc = 1/32 by 1/9 in RED H4 for SU(2) (with a weaker mass than the Doob bound at very small β:
−log(18/359) ≈ 2.99 at β = 1/32 versus −log(9/32) ≈ 1.27). It depends on OL-S1 and on OI-6.

**Remark 2.6 (closed-form evaluations of −log(9β); arithmetic only).**

| β | q = 9β | −log(9β) |
|---|---|---|
| 1/32 | 0.281 | 1.27 |
| 0.05 | 0.450 | 0.80 |
| 0.08 | 0.720 | 0.33 |
| 0.10 | 0.900 | 0.105 |

**Conjecture S♯ (sharp single-link threshold) [conjecture; not used].** Let M(K) := sup_{0≤κ≤K, |e|=1} E|⟨u, e⟩ − E⟨u, e⟩| under
μ_{κŵ} (mean absolute deviation). Then the path bound C_ij ≤ β·M(6β) holds, and sup_{κ≥0} M is attained at κ = 0 with
M(0) = 4/(3π), which would give single-link Dobrushin for β < β_D = π/24 = 3π/72 ≈ 0.1309.
*Computed observation O-MAD (not a proof).* A grid over κ ∈ [0, 0.8] (step 0.01) and angle steps π/80, with an added
Lipschitz margin 0.049 based on Lipschitz constants "≤ 2" that are not derived in the note (open item OI-8), gives M ≤ 0.4737,
hence β_D ≥ 0.1173. This is not interval-certified and is not used. The path bound C_ij ≤ β·M(6β) itself is also stated
without proof in the source (OI-8).

**Remark 2.7 (comparison; no new claim).** MASS_GAP_LOCAL_BLOCK_ASTRA's 18β row bound gives β < 1/18 and its Doob contraction
gives β ≤ 1/32. Conditional on OL-S1, Prop. S extends the SU(2) strong-coupling range by a factor 32/9 ≈ 3.6 in β (from
g² ≥ 128 to g² > 36).

**Remark 2.8 (normalization of character coefficients) [proved here; standard].** c_j(β) := ∫ e^{β cos θ} χ_j(U) dU =
2(2j+1) I_{2j+1}(β)/β, so a_j := c_j/(d_j c_0) = I_{2j+1}(β)/I_1(β), d_j = 2j+1. (Numerical cross-check against Haar quadrature at
β ∈ {0.1, 0.5, 1, 2.3}, j ≤ 2, max discrepancy 2.0e-31: computed observation, not used.)

---

## 3. Computed observations (not theorems; not used in any proof)

**Computed observation O-KP (Kotecký–Preiss thresholds for the character expansion).** Setup: polymers are link-connected
plaquette sets X with |w(X)| ≤ ε^{|X|}, ε(β) = Σ_{j≥½} d_j² a_j(β); activities vanish unless every link is covered at least
twice, so |X| ≥ 6; the plaquette-graph degree is Δ = 20. The sufficient condition 6 Σ_{n≥6} D^{n−1}(ε e^a)^n ≤ a/4 was evaluated
with arb, including the tail bound I_ν(x) ≤ (x/2)^ν e^{x²/4}/Γ(ν+1) [proved: termwise from the series]. The counting constant D
and the form of the condition are not derived in the note (open item OI-7).

| counting bound | β_KP | a | ε(β_KP) |
|---|---|---|---|
| D = 4Δ = 80 (claimed self-contained; derivation not written) | 0.00776 | 0.120 | 0.00778 |
| D = eΔ (standard lattice-animal bound, not re-proved) | 0.01088 | 0.124 | 0.0109 |

*Remark.* Both values are below 1/32. This says only that this particular sufficient condition fails above them; it is not a
statement that the cluster expansion diverges.

**Computed observation O-τ (MDTN truncation tails).** MDTN = monomer–dimer tensor-network basis (Chandrasekharan–Siew–
Bhattacharya, Phys. Rev. D 111 (2025) 114502, arXiv:2502.14175), used with the ASQR truncation j_max = ½. Define
τ_J(β) := Σ_{j>J} d_j² a_j(β). *Elementary fact [proved here]:* since |χ_j| ≤ d_j, τ_J(β) bounds the sup-norm error, relative to
c_0, of truncating the plaquette Boltzmann weight's character expansion at spin J. Values (upper ends of arb balls of the
partial sums over 2j ≤ 79; **no bound on the omitted tail 2j ≥ 80 is included**, so these are computed values, not
certified bounds; open item OI-1):

| β | J=½ | J=1 | J=3/2 | J=2 | J=3 | J=4 | J=6 |
|---|---|---|---|---|---|---|---|
| 0.5 | 1.03e-1 | 1.11e-2 | 8.5e-4 | 5.0e-5 | 9.8e-8 | 1.1e-10 | 3.3e-17 |
| 1.0 | 0.444 | 9.1e-2 | 1.4e-2 | 1.6e-3 | 1.2e-5 | 5.2e-8 | 2.6e-13 |
| 2.0 | 1.91 | 0.709 | 0.199 | 4.4e-2 | 1.3e-3 | 2.1e-5 | 1.6e-9 |
| 2.3 | 2.55 | 1.05 | 0.332 | 8.4e-2 | 3.2e-3 | 6.8e-5 | 9.1e-9 |
| 3.0 | 4.35 | 2.16 | 0.846 | 0.269 | 1.65e-2 | 5.9e-4 | 2.2e-7 |
| 4.0 | 7.56 | 4.48 | 2.16 | 0.864 | 8.7e-2 | 5.2e-3 | 5.8e-6 |

(The script also gives τ_½(1.5) ≈ 1.05 and τ_½(2.5) ≈ 3.02.)
*Remark.* τ_½(β) > 1 for β ≳ 1.5 means only that **this** error bound gives no control of the j_max = ½ truncation there; it is
not a proof that the truncation fails. Reaching τ_J < 10⁻² at β ≈ 2–3 needs J ≈ 3–6, i.e. local link dimension
Σ_{j≤J} (2j+1)² = 140 (J = 3) to 819 (J = 6). *Heuristic:* MDTN is suited to strong-coupling (H4-type) statements, not to CW.
Author-side local MDTN notes (a strong-coupling Hamiltonian gap lemma and small exact diagonalizations) are not committed to
this repository and are not relied on. No MDTN material was found on main or in PRs #10114 or #10132 (for #10114 only the
first 1000 changed files were searchable through the API).

**Remark 3.1 (window; Heuristic).** The gap between the proved strong-coupling range (β < 1/9, conditional on OL-S1) and
Bałaban's weak-coupling range β_Bal = 4/ḡ² (ḡ not explicit) is unquantified; Appendix N places the physical crossover near
β ≈ 2–2.3, so the window spans at least a factor ~20 in β.

---

## 4. Theorem H′ (conditional)

**Theorem H′ [conditional; proof outline = proof of RED Theorem H with step B3 replaced; independent review pending].**
Let N = 2 (the statement is formulated for SU(N), but the verification half below is only available for N = 2), d = 4. Assume
RED H1–H6, MG2, Open Lemma OL-DS, Lemma 1.7, and

> **CW′.** There exist a finite link set V of diameter ℓ, a margin η > 0, a reference specification γ_0 with
> α_V(γ_0) ≤ 1 − 2η (*verification half*), and a fixed number n_* of RG steps after k_1(a), such that, uniformly in the volume
> and in a, the effective theory at scale ℓ_* = L_b^{n_*} ℓ_1, written as a gauge-invariant link specification γ_{a,Λ},
> satisfies ‖γ_{a,Λ} − γ_0‖_V ≤ δ(η, V) (*landing half*; δ from Lemma 1.7), so that α_V(γ_{a,Λ}) < 1 − η. In addition, the RG
> map transports decay of effective gauge-invariant correlations back to the original observables with sources, without loss
> of rate (MG2).

Then the conclusion of RED Theorem H holds with μ_* > 0 depending only on (η, V) through OL-DS.
*Status note (open item OI-4).* The source stated "μ_* ≥ −log(1 − η)/(cℓ) in units of ℓ_*" with the constant c undefined; the
explicit rate depends on the form of OL-DS and is left open.

**Remark 4.1 (what changed relative to Theorem H; explanation).** CW is replaced by a finite-dimensional strict inequality on one
block (verification half) plus a landing statement. For |V| = 1 the verification half holds for γ_0 = Wilson at β_0 < 1/9,
conditional on OL-S1 (Prop. S). Then CW′ asks that the effective action at scale ℓ_* be δ-close to strong-coupling Wilson.

**Circularity and validity flags (extend C1–C5 of RED §6; Remarks).**
* **C6 (effective action, not Wilson).** CW_ℓ must be verified for γ_{a,Λ}, the Bałaban effective action, which has large-field
  regions, auxiliary/background fields and non-local, exponentially decaying polymers. It is not a finite-range link
  specification, so OL-DS must cover exponentially decaying interactions. Wilson-action numerics do not verify it.
* **C7 (no use of the conclusion).** The landing bound must come from RG estimates (Bałaban-type small-field control continued
  past ḡ, or another RG argument). It must not use decay of correlations of the effective theory, which CW_ℓ is meant to produce.
* **C8 (the real gap).** Bałaban's control ends at g ≤ ḡ. Prop. S starts at g² > 36 (conditional on OL-S1). Landing near
  strong-coupling Wilson requires carrying the effective coupling from ḡ to g² ≈ 36 with controlled remainders. That is the
  non-perturbative part, and nothing here supplies it.
* **C9 (MO not available).** Martinelli–Olivieri finite-size criteria cannot be cited for SU(N) spins without a new extension.

---

## 5. Open statements (consolidated)

| Name | Statement | Status | Used by |
|---|---|---|---|
| OL-S1 | Var_∥(κ) ≤ 1/4 for κ ∈ (0, 2/3] | Open Lemma; proved for κ ≤ κ₀ ≈ 0.0263; computer-assisted evidence on (0, 1.2] | Prop. S, Cor. S′, Theorem H′ (via γ_0 = Wilson) |
| OL-DS | Block criterion ⇒ uniqueness + uniform decay for gauge-invariant, possibly exponentially decaying specifications | Open Lemma (DS 1985 to be checked) | Theorem H′ |
| Lemma 1.7 | Openness of {α_V < 1 − η} | Stated; proof not written (OI-3) | Theorem H′ |
| CW′ landing | ‖γ_{a,Λ} − γ_0‖_V ≤ δ(η, V) uniformly | Open (C8); the core problem | Theorem H′ |
| CW | RED §3 | Open | RED Theorem H |
| Conjecture S♯ | MAD supremum at κ = 0; β_D = π/24 | Conjecture; O-MAD only | nothing |
| (extension) | Rigorous block criterion with |V| > 1 for SU(2) Wilson | Open | would push Prop. S beyond 1/9 |
| (extension) | Prop. S for SU(3) | Not attempted; constants and neighbour count must be redone | — |

## 6. Open items recorded in the editorial pass (not fixed)

* **OI-1.** τ_J values were previously described as a "certified tail". The script sums 2j ≤ 79 with ball arithmetic and
  adds no bound for the omitted terms; they are computed values. No theorem depends on them.
* **OI-2.** `checks/cw/data/rigorous_bounds_out.txt` section (2a) prints "certified … False" and then, unconditionally, a line
  "certified Dobrushin: q(β) = 9β". The second line is not supported by that section; the certificate claim (now only evidence
  for OL-S1) comes from `var_certificate.py`. The script output was left unchanged.
* **OI-3.** Lemma 1.7: Lipschitz factor and norm ‖·‖_V not defined/derived.
* **OI-4.** Theorem H′ rate constant c undefined in the source.
* **OI-5.** OL-DS: form of the Dobrushin–Shlosman theorem (distance, continuous spins, decay statement and which of the two 1985
  papers proves it) not checked against the originals.
* **OI-6.** Theorem 2.0: exact theorem numbers and constants of the covariance estimate, and the passage from link-graph distance
  to time distance used in Corollary S′, not pinned.
* **OI-7.** O-KP: the counting constant D = 4Δ and the form of the KP sufficient condition are not derived.
* **OI-8.** Conjecture S♯ / O-MAD: the path bound C_ij ≤ β·M(6β) and the Lipschitz constants "≤ 2" are not derived.

## Appendix N. Numerical evidence (not used in any proof)

Wilson action, not the Bałaban effective action (flag C4 of RED). Code: `checks/cw/su2_mc.py` (Kennedy–Pendleton heat-bath plus
3 overrelaxation sweeps, checkerboard). Scan: `checks/cw/run_scan.sh` (150 thermalization + 500 measurement sweeps, 40 runs).
Analysis: `checks/cw/analyze_mc.py` → `checks/cw/data/mc_summary.{txt,json}`, `checks/cw/data/sc_wc_compare.txt`. Raw per-run
JSON (~6.7 MB) is not committed. Compute: 30.9 min user + 3.1 min sys CPU, about 10 min wall on 8 cores. Errors are jackknife
with 20 bins.

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

Observations (evidence only):
* **Smoothness.** ⟨P⟩(β) is smooth. Hot and cold starts agree at β = 2.2, 2.3, 2.5 (0.56903(38) vs 0.56867(23); 0.60223(35) vs
  0.60271(36); 0.65235(21) vs 0.65239(20)). dP/dβ peaks at about 0.33–0.38 for β ≈ 2.1–2.3 and does not grow from L = 4 → 6 → 8
  (peak values 0.46(4), 0.37(3), 0.38(3)), consistent with a crossover rather than a bulk transition at these volumes.
* **Strong-coupling comparison.** ⟨P⟩ ≈ u holds to 0.06% at β = 0.5 and 1.3% at β = 1, then fails (5% at 1.5, 16% at 2.0). The
  Creutz ratio tracks −log u up to β ≈ 1.25 and then drops below it. Weak-coupling check: (1−P)·4β/3 falls toward 1 (1.07 at
  β = 4), consistent with ⟨1−P⟩ ≈ 3/(4β).
* **Correlation-length proxy.** The Creutz ratio falls by about 12× between β = 1 and 4. The 0⁺⁺ effective mass is too noisy to
  be informative and is not used. Polyakov |⟨P_L⟩| stays at the finite-volume noise level (≈ 0.018 on 8⁴) up to β ≈ 2.3, then
  rises (finite-temperature crossover for N_t = 8, not a bulk effect).
* **Heuristic reading.** Nothing singular is visible for β ∈ [0.11, ~2], but leading-order strong-coupling agreement is lost near
  β ≈ 1.

Caveats: small volumes, modest statistics, Wilson action only (C4). Integrated autocorrelation times were not measured
separately; 20 jackknife bins of 25 sweeps partly account for them.

## Not claimed

No MG row is closed. CW and CW′ are open. Proposition S is conditional on Open Lemma OL-S1 and needs independent review; it
changes the H4 threshold for SU(2) only once OL-S1 is proved and the note is reviewed. No computation in this note or in
[checks/cw/](checks/cw/README.md) supports a proved statement. Monte Carlo results are evidence about the Wilson action only.
