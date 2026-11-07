# CN1. A common light cone by interaction: outline and rung 1

## 0. Status

**FINISH: FROZEN 2026-11-07 after pass 3 (CN1_REFEREE.md); the referee's edits E1-E5 and E8 are applied.** Frozen means: the proved results below are not reopened; open statements are worked in their own files and enter by a dated amendment. The item enters `LZ1.md` as its Amendment 4. The lead (Claude Opus 5.5, laptop) checked that the edits are in the text; that is a text check, not a second referee. The results below concern specified mathematical flows, not a derived framework dynamics or an empirical prediction. No reading or axiom is adopted.

**Proved, conditional on the displayed equations.** Theorem 1 gives global alignment for the positive-coefficient star flow. Theorem 2 gives the exact equal-charge pair exponent. Theorem 3 gives a conditional robustness result under explicit smallness and remainder bounds. Proposition 4 gives a persistent-source counterexample. Proposition 5 gives the free continuum current threshold. Lemma 6 gives off-site vanishing of the *undressed* charged correlator in a locally invariant state. Lemma 7 gives the photon coefficients conditional on the imported one-loop vacuum-polarisation input. These were author-side checks; `CN1_REFEREE.md` reports a referee re-derivation, not audited status.

**GAP.** The proposed spectral functional has domain and identification defects (§2); the referee proposes a repair and closes local access under T1 and the R0 level-0 bound, with a proviso at coarse levels. A fixed-window bound does not establish CN1-T; transferring a rate requires the uniformity and denominator conditions in §2. The general-coefficient versions of the perturbation claims need the stated local regularity and the correct weighting exponent (§5). A gauge-fixed charged propagator is not the undressed invariant-state correlator; H1 is an observable/zoom mismatch, not a proof that a gauge-fixed calculation fails. Continuous time is not established by the zoom. The absolute assertion that a faster threshold remains visible under interaction is unproved. These defects do not establish that a common cone is impossible.

**Open by name.** CN1-T, CN1-T(r), R1-MOD, R1″-MOD, R1′, R1-OBS beyond the free continuum, R2 with R2-a (H-TICK), R2-b (H-TRANSFER, including alias control), R2-c, R3 (H-NA), R-P (H-RATE), H-FIN, H-PHOTON, H-THR, H-CONV (the content of R1-MOD). Framework inputs: GA1-P-5 (plaquette class), GA1-5-Φ as a cone (T1), VC1, ZM1-I1[INV], R-CS, MT1-S[R-CS], Y2-W, GA2, BK1, CH1, and the graviton bridge (GR2). H3, H4, H6 and H7 are open framework inputs. No full R1 model has been shown to satisfy the flow and observable bridges.

**Provenance.** Distilled from `CN1_OUTLINE.md`, SHA-256 `db536699debc9effeaae029e9e5e3d351a06f5639116b61d56b2afb56cab09da`; context: `prior/CN1.md`, `TOE_ASSEMBLY.md`, `LZ1.md`, `LZ1I.md`, `ZM1I1A.md`, `LW1.md`. Pass 1 reports its source revisions and search in the outline; those historical claims are not refreshed here. Model requested for this pass: gpt-6.1-terra; actual model, effort and session id: see run log. Pass 3 referee: `CN1_REFEREE.md`; its closures are unrefereed.

**Editing provenance.** Codex gpt-6.1-terra, effort high, codex-cli 0.165.0; session id `01a1b6e3-3876-7972-81a8-f35447722c2b`.

## 1. Definitions inferred by the distiller

1. A **star flow** is the ODE (OL) in §4, viewed as an ODE independently of its QED interpretation. `n` is finite, `n_a>0`, `q_a≠0`, `W=Σ n_a q_a²`, and initial speeds and coupling are positive. Replacing the displayed `P,R,S` by positive locally Lipschitz functions gives the general star flow.
2. `m,M` are the minimum and maximum of all `v_a` and `c`; `D=M−m`, `B=[m(0),M(0)]`, `τ=∫G dℓ`. At consensus `P∞=P(c∞,c∞)` and `S∞=S(c∞)`. A pair exponent is `α=q²P∞/(W S∞)`. For (OL), `α=2q²/W`.
3. A **zoom trajectory** here means the sequence of invariant-algebra systems and ZM1-INV maps described in `TOE_ASSEMBLY.md` §3.6, with block factor `L≥2`, one coarse tick per `L` fine ticks and the separately open class-(a), `p=2` comparison. The map does not supply charged-field maps. A D1 state, physical subspace and admissible tick are as in `LZ1.md` §1 and `LZ1I.md` §1. A band and Clifford speed are as in `LZ1I.md` §1; `LZ1-SC` counts the specified nonstationary band images.
4. A **photon band** is proposed to mean an R-Φ flux-carrying band with a Clifford cone. R-Φ itself is a proposed reading; see `GA1_5.md`. This definition does not construct a photon.
5. For a local invariant `A`, let `ξ_A=π(A)Ω−ω(A)Ω` and let `μ_A` be its joint spectral measure for the commuting tick and spatial translations. For `0<κ≤1`, `W(κ)={|λ|≤κ, 0<|K|≤κ}`, using the local coordinates at the origin of the Brillouin torus. Call `A` light when `μ_A(W(κ))>0`. Let `ss(μ_A)` be the complement of the largest open set where the measure has a smooth Lebesgue density. Define `E_A(κ)` as the closure of `|λ|/|K|` over `ss(μ_A)∩W(κ)`. For the named family of all light local invariant observables, set `S_k(κ)=⋃_A E_A(κ)` and `Δ_k=(sup S_k−inf S_k)/inf S_k` only when the set is nonempty, bounded above, and bounded away from zero. These definitions are proposed CN1-OBS, not consequences of ZM1-INV.
6. In §5, `ρ=(ρ_a,ρ_0,ρ_G)` is continuous in flow time and locally Lipschitz in state, uniformly on compact time intervals, so the usual local ODE theorem applies. `𝓡(K,f,f₁₂)` means the three bounds (R-i)–(R-iii) there. `f,f₁₂` are nonnegative continuous functions. The forcing in (R-iii) is a signed function `g₁₂` bounded by `f₁₂`.
7. A **threshold** below is a singular-support threshold in definition 5, not necessarily an isolated particle pole. A gauge-invariant undressed two-point function, a gauge-fixed propagator, a Wilson-line-dressed correlator and an invariant current correlator are distinct objects.

## 2. Target and its domain

**CN1-T, proposed and open.** Take `L_cube`, `L5-U[m]` or `L5-O[S_+]`, an admissible update with plaquette layer, a VC1 vacuum and a ZM1-INV zoom trajectory with class (a), `p=2`. Assume (T1) a photon band of positive speed at each level, with its node at `K = 0`, and (T2) every other light band or continuum is generated by nonzero Gauss-charged species in the proposed R-CS^str sense; charged pairs are allowed, and light neutral bound species are excluded. With the family in definition 5, the intended conclusion is
\[
\lim_{\kappa\downarrow0}\limsup_{k\to\infty}\Delta_k(\kappa)=0.
\]
**CN1-T(r), proposed and open.** There are `C, γ, κ₀ > 0` with `Δ_k(κ) ≤ C(1+k)^{−γ} + Cκ` for all `κ ∈ (0, κ₀]` and all `k`, where `C` and `γ` do not depend on `κ`. A term linear in `κ` needs `C^{1,1}` regularity at the nodes; `C¹` gives only `o(1)`.

**GAP 2.1: definition.** Neither the hypotheses nor the definition guarantee that `S_k(κ)` is nonempty, has positive infimum, or is bounded. The window clips a cone: if `v>1`, its portion with `|K|>κ/v` lies outside `W(κ)`. A local operator can have multiple spectral components, and an abstract band need not be created with nonzero local spectral weight. A `C¹` Clifford node alone gives `λ=±v|K|+o(|K|)`, not necessarily an `O(|K|²)` remainder. Specify local spectral access, the domain of `Δ`, and sufficient regularity before using the asserted band-to-threshold estimate. The absolute-value window also requires a specified Floquet branch and control of folded branches.

**Referee repair CN1-T′ (proposed, not adopted).** (referee closure, CN1_REFEREE.md) Keep the law, update, vacuum, zoom, T1 and T2; in T1 the photon band has its node at `K = 0`. For local `A ∈ 𝔄_k^G`, let `ξ_A^s` be the projection of `ξ_A` onto `ker(Ũ_k − 1)^⊥`, and `μ_A^s` its joint spectral measure. Define `E_A(κ)` and `S_k(κ)` as in definition 5 with `μ_A^s` in place of `μ_A`. *Conclusion:* for every `ε > 0` there are `κ₀ > 0` and `k₀` such that for all `κ ∈ (0, κ₀]` and `k ≥ k₀` there is `s > 0` with `∅ ≠ S_k(κ) ⊂ [s, (1+ε)s]`.

- Where `Δ_k(κ)` is defined, `S_k(κ) ⊂ [s,(1+ε)s]` for some `s > 0` exactly when `Δ_k(κ) ≤ ε`. So CN1-T′ is CN1-T on its domain. Outside the domain it is false instead of undefined, which is the right answer for a light stationary or quadratic mode.
- Four tests. (1) P: it restates CN1's own target and fixes no other part's target. (2) P: closed. (3) P: the projection drops only tick-fixed weight, which the owner's LZ1-SC already records as "a separate static class, which LZ1 does not constrain" (`TOE_ASSEMBLY.md` line 229). (4) P: each change has its own reason (domain, static weight, node in the window); no constant is added.

**Nonemptiness from T1 (referee closure, CN1_REFEREE.md).** Under T1 (photon band in `H_phys`, node at `K = 0`, `c_k > 0`), `S_k(κ) ≠ ∅` for every `κ ∈ (0,1]`. *Proof.* (i) Local invariants are norm dense in `𝔄^G`: if local `A_n → A ∈ 𝔄^G`, average `A_n` over the compact gauge group of the finitely many sites it touches; the average is local, invariant and within `‖A − A_n‖` of `A`. So `{π(A)Ω : A local invariant}` is dense in `H_phys = closure π(𝔄^G)Ω`. (ii) The band eigenphases are `±c_k|K| + o(|K|)`, so for some `δ > 0` the band image `X` over `0 < |K| ≤ δ` has joint spectrum inside `W(κ)`. `X` is a nonzero closed subspace of `H_phys`, invariant under the tick and translations, and orthogonal to `Ω`: `V(K)` has no eigenvalue `1` for `0 < |K| ≤ δ`, so `X ⊂ ker(Ũ−1)^⊥`, while `Ω` is tick-fixed. By density some local invariant `A` has `P_Xξ_A ≠ 0`. (iii) The band part of `μ_A^s` lives on the graph of the eigenphases, a Lebesgue-null set; every point of its support therefore lies in `ss(μ_A^s)`. So `E_A(κ) ≠ ∅`. □ The same argument gives **local spectral access** for any band in `H_phys ∩ ker(Ũ−1)^⊥` with a node at `0`; it is used for R0 below.

**GAP 2.2: rate and bridge.** A bound at one fixed `κ₀` alone gives at most `limsup_k Δ_k(κ₀)≤Cκ₀`; it does not imply the double limit. A sufficient replacement is a bound uniform for all sufficiently small `κ`, with constants independent of `κ`, plus existence of the functional. R1-OBS asks for distances `O(κ+G_k)` from *each* running speed uniformly in `κ`, but does not by itself supply a positive relative denominator. It therefore does not by itself transfer the sharper pair exponent to `Δ_k`; even `G_k=O(1/k)` can dominate an exponent greater than one. Further bounds are required.

**GAP 2.3: thresholds.** A single free current has the threshold in Proposition 5, but arbitrary invariant bilinears or all local observables need not have exactly that singular set. Interactions may broaden, remove, shift or create singularities; no theorem here proves that a faster species remains visible. The statement that all neutral bound-state photon couplings are irrelevant is also an unproved generalization. T2 is a restriction, not a proof of neutral-sector behavior.

## 3. Ladder and prior results

**R0, already proved elsewhere within its hypotheses.** `LZ1I.md` Theorems 7–9 construct two exactly decoupled neutral bands with unequal speeds. Theorem 10′ transfers their speeds to `(M/L′)v₁,(M/L′)v₂` under its explicit band comparison; for `M=L′` the split remains. RC-Z and 10′ are referee closures labelled unrefereed in that source. **GAP:** the lower bound on the proposed `Δ_k` additionally needs the local spectral access and estimates of §2. **R0 access (referee closure, CN1_REFEREE.md).** The band vectors are `u_x^j = π(E^x_{j0})Ω` with `E^x_{j0}` local and gauge invariant (`LZ1I.md` line 80). They are orthogonal to the tick-fixed `Ω`, so `ω(E^x_{j0}) = 0` and `ξ_A = u_x^j` for `A = E^x_{j0}`. Each fibre of `u_x^j` has norm one, so `μ_A` puts positive mass on the band graph over every ball `0 < |K| ≤ δ`; by the nonemptiness proof above those points lie in the singular support. Hence `E_{A_j}(κ)` is nonempty and lies within `ε(κ) → 0` of `v_j`. So `S_0(κ)` meets small neighbourhoods of both `v₁` and `v₂`. If `v₁ < v₂`, `ε < (v₂−v₁)/v₁` and `κ` is small, no `s` gives `S_0(κ) ⊂ [s,(1+ε)s]`. At every level that carries both bands in the same way, CN1-T′'s inclusion fails. **At levels `k ≥ 1`.** Theorem 10′ gives coarse zero branches near `±Mw_j(θ/L′)`, with `Mw_j(θ/L′) = (Mv_j/L′)|θ| + O(|θ|^3)`, only "along every ray of" a closed cone `Γ` of directions (`LZ1I.md` line 156). One direction is enough. Access at a coarse level follows if the coarse list vectors of Theorem 10′ lie in the coarse `H_phys`; they do when they are made from coarse invariant operators, the only ones ZM1-INV maps. Proof: `H_phys` is invariant under the spectral projections of `(Ũ, T)`, so the spectral projection `E` onto the part of a coarse branch graph inside `W(κ)` is nonzero on `H_phys`; density gives a local invariant `A` with `Eξ_A ≠ 0`; the graph is Lebesgue-null, so the points it charges lie in `ss(μ_A)`. With only `C^1` the error term is `ε(κ)`, not `Cκ`. This counterexample does not cover every charged or interacting sector.

**R1.** M1 is 3+1-dimensional massless Dirac matter of multiplicities `n_a`, charges `q_a`, speeds `v_a`, coupled to one Maxwell field of speed `c`; `G=e²/ε` and `ℓ=log(Λ/scale)`. Theorems 1–3 establish only the displayed ODE consequences. **R1-MOD** asks for an exact scale integration in a lattice regularization whose interpolated coefficients obey (OL+ρ) with the §5 bounds uniformly at all scales, with (Sm) at the starting scale and `f + f₁₂ ≤ Ke^{−βℓ}`. **R1-OBS** asks to identify invariant spectral thresholds with those coefficients to `O(κ+G_k)`, with a constant independent of `κ`, including access to each speed. Both are open. Their truth, plus the additional §2 conditions, would be needed for a model-level cone conclusion.

**R2, open.** For the framework gauge layer, obtain (R2-a) the continuum one-loop coefficients from tick loops, (R2-b) transfer of continuum thresholds across class-(a) zooms, and (R2-c) a decaying cell-scale forcing. Required inputs include a Clifford photon GA1-5-Φ, R-CS, ZM1-I1[INV], Y2-W, VC1 and a specified plaquette class. A finite offset at the initial scale is initial data; a source at every scale needs its own bound.

**R3, open.** Extend to all relevant charged species, including nonabelian sectors, their breaking or confinement and the remaining photon. It depends on R2, GA2, BK1 and CH1. Neutral sectors and gravitons need separate bridges. **R-P, open:** obtain `Δ_k≤C L^(−βk)` for `β>0`; the marginal two-species example below does not give this rate.

**Hard steps.** H-CONV is uniform all-scale control of R1-MOD. R1′ is reduced QED as an intermediate test; R1″ gives the photon a mass and has `N=log(Λ/m_γ)` marginal scales. R1″-MOD asks for bounds uniform in `N`; its finite-scale consequence also requires uniform initial data, smallness and constants in Theorem 3. H-THR is identification of thresholds beyond free theory. H-PHOTON asks for a framework flux band with a Clifford cone; `GA15PHI.md` reports a one-way flux band, not such a cone. H-TRANSFER asks to extend RC-Z beyond isolated branches; its simplest test is a free cube-tick pair continuum. H-TICK asks for tick loop coefficients, first with a Gaussian photon. H-NA asks for nonabelian drag and its termination at breaking or confinement. H-FIN asks for finite matching when a species becomes massive. H-RATE asks for a power in physical scale, first at a controlled interacting fixed point. These are research plans, not established results.

**Overlap.** Constant positive two-sector exchange attraction is already in `docs/EMERGENT_LORENTZ_VELOCITY_RG_EXCHANGE_MATRIX_EXACT_SUPPORT_NOTE_2026-06-18.md`, conditional and unaudited. The shared-speed nonlinear truncated ODE, linear multi-cone star flow, and decaying-forcing discussion are already in `docs/SPATIAL_LATTICE_GAUGE_FERMION_LOGARITHMS_AND_METRIC_ATTRACTION_LIMITS_BOUNDED_THEOREM_NOTE_2026-09-14.md` (conditional-support, unaudited). Theorems 1–3 extend the displayed ODE statements as specified, not their physical status. `LZ1I.md` Theorems 11–12 already give the integrated-drag criterion and marginal-versus-power distinction. `CH1_5UQ.md` Theorem 2.2 and `LZ1.md` Corollary 2.3 give prior forms of Lemma 6 (the latter for local odd operators). The digest `prior/CN1.md` also records the B4 symmetry route, Hall-response limitation, supplied free matching, gravity routes and withdrawn proxy claims; none supplies R1-MOD or the observable bridge.

## 4. One-loop flow and alignment

The coefficient functions, imported as conditional one-loop input, are
\[
\begin{aligned}
v_a'&=Gq_a^2P(v_a,c)(c-v_a),& c'&=G\sum_b n_bq_b^2R(v_b,c)(v_b-c),\\
G'&=-G^2\sum_b n_bq_b^2S(v_b),\\
P(v,c)&={4v^2+3vc+c^2\over6\pi^2c(v+c)^2},&R(v,c)&={v+c\over12\pi^2cv},&S(v)&={1\over6\pi^2v}.
\end{aligned}\tag{OL}
\]
The first coefficient is the Peierls-note fermion speed logarithm cited in §3. It is an effective two-point-action coefficient, not an exact charged particle pole. The coefficient extraction and Ward identity are inputs, not established by the ODE.

**Lemma 7 (conditional photon lines).** Assume the Lorentz-invariant one-loop coefficient for one Dirac species is `(q²e²/6π²)·(E²−B²)/2`, with the stated charge normalization and regulator permitting the logarithmic change of variables. A species of speed `v` contributes `(q²e²/6π²)·(E²/v−vB²)/2`. If the vertex charge is fixed in this convention by the Ward identity, the last two lines of (OL) follow.

*Proof.* Set `y=x/v` and `Ã_j=vA_j`. Then `Ẽ=vE`, `B̃=v²B`, and `d³y=v^(−3)d³x`. Transform the imported speed-one term. Thus `ε′=Σ n_bq_b²e²/(6π²v_b)` and `(μ⁻¹)′=Σ n_bq_b²e²v_b/(6π²)`. Differentiate `c²=μ⁻¹/ε` and `G=e²/ε`; this gives the displayed `R,S`. Regulator independence and the Ward identity are not proved by this rescaling. □

**Theorem 1 (R1-A).** For the general star flow with positive locally Lipschitz `P,R,S`, there is a unique global solution. All speeds remain in `B`; `m` increases and `M` decreases. Define
\[
p_-=\min_a q_a^2\min_{B^2}P,\quad R_+=W\max_{B^2}R,\quad S_-=W\min_B S,\quad S_+=W\max_B S.
\]
Then
\[
{G_0\over1+G_0S_+\ell}\le G(\ell)\le {G_0\over1+G_0S_-\ell},\quad
D(\ell)\le {D(0)\over1-\eta}(1+G_0S_+\ell)^{-\gamma},
\]
where `s₀=1/(4R₊)`, `η=(1−e^(−p₋s₀))/4`, `γ=|log(1−η)|/(s₀S₊)>0`. All speeds converge to one positive limit.

*Proof.* At a maximizing matter speed its derivative is nonpositive; at a maximizing photon speed every term is nonpositive. The max-of-finitely-many Dini derivative rule makes `M` nonincreasing; the corresponding minimum rule makes `m` nondecreasing. Positivity and `(1/G)′=Σ n_bq_b²S(v_b)` give the coupling bounds. These bounds keep the solution in a compact subset of the positive domain on every finite interval, so local existence extends globally.

In `τ` time, suppose at the start of a window the photon is in the lower half of the speed interval, of width `D₀`. It moves by at most `R₊D₀s₀=D₀/4`; hence it stays below `K=M₀−D₀/4`. A matter speed above `K` has `(v−K)′≤−p₋(v−K)` and cannot cross upward through `K`. Its initial excess is at most `D₀/4`, so at the end every speed is at most `M₀−ηD₀`. If the photon starts in the upper half, the symmetric lower-barrier argument raises the minimum by at least `ηD₀`. Thus each window contracts the spread by `1−η`. Iteration and `τ≥S₊⁻¹ log(1+G₀S₊ℓ)` give the bound. The nested intervals have vanishing width, hence a common limit. □

For (OL), explicit bounds include `P≥1/(6π²M(0))`, `R≤1/(6π²m(0))`, and `1/(6π²M(0))≤S≤1/(6π²m(0))` on `B`.

**Theorem 2 (R1-B).** Under Theorem 1, assume `P` is `C²` near the diagonal, `S` is `C¹` near `c∞`, `q₁²=q₂²=q²` and `Δ(0)=v₁(0)−v₂(0)≠0`. Then
\[
|\Delta(\ell)|=(C+o(1))(1+\ell)^{-q^2P_\infty/(WS_\infty)},\qquad C>0.
\]
For (OL) the exponent is `2q²/W`; with exactly two unit-charge Dirac species it is `1`.

*Proof.* Let `F(v,c)=P(v,c)(c−v)` and `Λ=−∫₀¹∂_vF(v₂+tΔ,c)dt`. Then `Δ′=−Gq²ΛΔ`, so `Δ` never vanishes. Theorem 1 and smoothness give `Λ=P∞+O(D)` and `Σ n_bq_b²S(v_b)=WS∞+O(D)`. Since `G=O((1+ℓ)⁻¹)` and `D=O((1+ℓ)⁻γ)`, `∫G|Λ−P∞|<∞`. Integration of `(1/G)′` shows `G−[WS∞(1+ℓ)]⁻¹` is integrable. Hence `∫G=(WS∞)⁻¹log(1+ℓ)+constant+o(1)`. Substitute into the exact exponential solution. □

For `ℓ=k log L`, this pair difference is a power of `k`, not `O(L^(−βk))` for any `β>0`. This is an ODE statement; identifying it with a spectral `Δ_k` requires R1-OBS. For unequal charges the linear star eigenvalues are in the Peierls note; no nonlinear sharp rate is claimed here. In the linearized star flow (C2), the nonzero decay rates per unit `∫κ` are `2q_a²` for each charge class with at least two members and one root of `Σ_b n_bq_b²/(2q_b² − μ) = −1` in each gap between consecutive distinct values `2q_b²` and above the largest; all are at least `2q_min²` (referee linear-spectrum remark, CN1_REFEREE.md).

**Consistency checks, conditional on imported source conventions.** (C1) With all `v_a=v` and all `q_a²=1` (so `W=Σ n_a`), `r=v/c`, `g=G/c`, the equations become `r′=−g(r−1)H_W(r)/(12π²)`, `g′=−Wg²(r+1/r)/(12π²)`, `(log c)′=Wg(r²−1)/(12π²r)`, `H_W=2(4r²+3r+1)/(r+1)²+W(r+1)`, matching the cited shared-speed flow. (C2) Near consensus, with `v_a=c∞(1+f_a)`, `c=c∞(1+h)`, `κ=G/(6π²c∞)`, the leading equations are `f_a′=2q_a²κ(h−f_a)`, `h′=κΣ n_bq_b²(f_b−h)`, `κ′=−Wκ²`. (C3) The outline's contraction of Kostelecký–Lane–Pickering's one-loop tensors gives a relative exponent `3` for one unit-charge species, matching the single-species star mode; tensor conventions and the outside source were not independently checked in this pass. (C4) For one unit-charge species, `(log(c²v))′=Gv(c−v)²/[6π²c²(c+v)²]`, so it is invariant to first order near consensus, consistent with the cited Isobe–Nagaosa approximation. This is not an exact invariant.

## 5. Remainders and a counterexample

Let (OL+ρ) add `ρ_a,ρ₀,ρ_G` to the three lines of (OL). For `K≥0`, class `𝓡(K,f,f₁₂)` has
\[
\begin{array}{ll}
\text{(R-i)}& |\rho_a|,|\rho_0|\le KG^2D+f(\ell),\quad \int_0^\infty f<\infty,\\
\text{(R-ii)}& |\rho_G|\le KG^3,\\
\text{(R-iii)}& \rho_1-\rho_2=-G^2\vartheta\Delta+g_{12},\quad |\vartheta|\le K,\quad |g_{12}|\le f_{12},\quad \int_0^\infty f_{12}(1+\ell)^{2q^2/W}d\ell<\infty.
\end{array}
\]
In (R-iii), `q₁²=q₂²=q²`. Exchange symmetry together with a uniform `O(G²)` Lipschitz bound in the two exchanged speed coordinates gives the homogeneous difference form; symmetry alone does not give the bound.

**Theorem 3 (R1-C, corrected domain).** Use the displayed (OL) coefficients and suppose the bounds above hold along the solution. Put `B′=[m(0)/2,2M(0)]`, `S′=W/(12π²M(0))`, `a=4KG₀/S′`, `F=∫f`. Assume
\[
KG_0\le S'/2,\qquad {a\over2}e^a(D(0)+2F)+F\le m(0)/2.\tag{Sm}
\]
If `f≡0` or `f(ℓ)≤K e^(−βℓ)` for some `β>0`, the solution is global, remains in `B′`, has `D=O((1+ℓ)^(−γ′))` for some `γ′>0`, and every speed converges to the same positive limit. Under the same hypothesis on `f` and (R-iii), with `α=2q²/W`, `(1+ℓ)^α Δ` converges to a finite constant. If `g₁₂=0` and `Δ(0)≠0`, this constant is nonzero; otherwise it may vanish. In all cases `|Δ|=O((1+ℓ)^(−α))`.

*Proof.* In `B′`, `Σ n_bq_b²S(v_b)≥S′`. As long as `KG≤S′/2`, `(1/G)′≥S′/2`, so `G≤G₀/(1+G₀S′ℓ/2)` and `∫G²≤2G₀/S′`; the condition propagates. Dini estimates give `D⁺M≤KG²D+f` and `D₊m≥−KG²D−f`. Grönwall yields `D≤e^a(D(0)+2F)`, and the maximum can rise and minimum fall by at most `(a/2)e^a(D(0)+2F)+F`. Hence the solution stays in `[m(0)/2,M(0)+m(0)/2]⊂B′`, and global continuation follows. The equality case is covered by continuation in a slightly larger positive box, using the uniform bound just obtained.

In `τ` time, compare on each fixed-length window with the homogeneous star system. Its speed vector field is uniformly Lipschitz on `B′`, so variation of constants bounds the extra displacement by a constant times `∫window(KGD+f/G)dτ = ∫window(KG²D+f)dℓ`. The homogeneous barrier proof in Theorem 1, with the uniform constants on `B′`, then gives, for late windows, `D_{j+1}≤(1−η′/2)D_j+C∫window f dℓ`: `G→0`, and the homogeneous contraction absorbs the `KG²D` contribution. For exponential `f`, window start times grow at least exponentially in `j`, since `τ≤C log(1+ℓ)`; the forcing terms are supergeometrically summable. Iteration gives exponential decay in `j`, hence a power in `ℓ`, using `τ≥c log(1+ℓ)`. The same holds for zero forcing. The total upward variation of `M` and downward variation of `m` are finite because `∫(KG²D+f)<∞`; their common limiting width is zero, so the speeds converge.

For the pair, `Δ′=−(Gq²Λ+G²ϑ)Δ+g₁₂`. The proof of Theorem 2 applies: the `G²ϑ` integral is finite, and the `ρ_G` correction contributes at most `O(log(1+ℓ))` to `1/G`, which does not spoil integrability of `G−[WS∞(1+ℓ)]⁻¹`. The fundamental solution is therefore `(C_Ψ+o(1))(1+ℓ)^(−α)` with `C_Ψ>0`. Variation of constants and the weighted `f₁₂` integral give the stated limit; for `g₁₂=0`, its sign and nonzero value follow from `Δ(0)≠0`. □

**GAP 5.1.** The outline presents the contraction of the perturbed system as immediate from its barrier proof; it does not show the stability estimate for the vector field or the constants. The proof above supplies the finite-window comparison but leaves the estimates conditional on uniform local Lipschitz bounds in the compact box and on the stated regularity of `ρ`. For general `P,R,S`, replace the weighting exponent `2q²/W` in (R-iii) by `α=q²P∞/(WS∞)` and assume the regularity in Theorem 2; `S′` and (Sm) must also be replaced by the actual positive lower bound. The theorem does not cover arbitrary integrable `f` with a power rate.

**Convergence for integrable forcing (referee closure, CN1_REFEREE.md).** Under (Sm) and any continuous `f ≥ 0` with `∫f < ∞`, the solution is global, stays in `B'`, and all speeds converge to one limit; no rate is claimed. Proof: the estimates in the proof and the finite-window comparison give `D_{j+1} ≤ (1−η'/2)D_j + ε_j` for `j ≥ j₁`, with `ε_j = C∫_window f` and `Σε_j < ∞`. Then `D_j ≤ (1−η'/2)^{j−j₁}D_{j₁} + Σ_{i=j₁}^{j}(1−η'/2)^{j−i}ε_i → 0`, because `ε_i → 0`. Inside a window `D ≤ D_j + 2∫_window(KG^2D+f)`, so `D(ℓ) → 0`. `M − ∫₀^ℓ(KG^2D+f)` is nonincreasing and bounded below, so `M` converges; likewise `m`. Their limits agree.

**Proposition 4 (R1-D).** Let `Δ′=−Gq²Λ(ℓ)Δ+σG`, with `σ≠0`, `G>0`, `∫₀∞G=∞`, and continuous `Λ→P∞>0`. Then `Δ→σ/(q²P∞)`.

*Proof.* In time `τ=∫G`, put `y=Δ−σ/(q²P∞)`. Then `dy/dτ=−q²Λy+σ(1−Λ/P∞)`. For sufficiently late time `Λ≥P∞/2`. The variation-of-constants estimate first sends the initial contribution to zero, then bounds the remaining term by a constant times `sup_{s≥τ₀}|Λ(s)−P∞|`, which tends to zero as `τ₀→∞`. □

This is a counterexample to replacing the vanishing-at-consensus structure by an unrestricted `O(G)` source. It does not prove that a framework tick produces such a source.

**Full-flow extensions (referee closure, CN1_REFEREE.md).** **(R1-D-a) Robust form.** If `σ ≠ 0`, `∫₀^∞G = ∞` and `|Λ| ≤ Λ̄` along the solution, then `liminf|Δ| ≥ |σ|/(q^2Λ̄)`. Proof: take `σ > 0` and `b = σ/(q^2Λ̄)`. In `τ` time, wherever `|Δ| < b − δ`, `dΔ/dτ ≥ σ − q^2Λ̄|Δ| > q^2Λ̄δ`. So `Δ` crosses the band `|Δ| < b − δ` upward in finite `τ` and never re-enters it from above. Hence eventually `|Δ| ≥ b − δ`; let `δ → 0`. **(R1-D-b) Explicit full flow.** Fix `(v₁*, v₂*, c*)` positive with `q₁^2 = q₂^2` and `v₁* ≠ v₂*`. Put `ρ_a = Gσ_a`, `ρ₀ = Gσ₀`, `ρ_G = 0`, with `σ_a = −q_a^2P(v_a*,c*)(c*−v_a*)` and `σ₀ = −Σ_b n_bq_b^2R(v_b*,c*)(v_b*−c*)`. Then the speeds stay at `(v*, c*)` for all `ℓ`, `G` solves `G' = −G^2Σ_b n_bq_b^2S(v_b*)`, and `Δ ≡ v₁* − v₂* ≠ 0`. The source is `O(G)` and violates (R-i). So the vanishing-at-consensus structure of `𝓡` cannot be replaced by an `O(G)` bound. As noted above, neither closure shows that a tick produces such a source.

## 6. The free threshold and local gauge invariance

**Proposition 5 (R1-OBS₀).** For a free massless continuum Dirac field of speed `v>0` in the positive-energy vacuum, the unsmeared current-density spectral distribution at nonzero momentum has the form
\[
\rho^{00}(\lambda,K)=C_v|K|^2\,\mathbf1_{\lambda\ge v|K|},\qquad C_v>0,
\]
up to the choice of Fourier normalization. Its singular-support speed set in `W(κ)` is `{v}`. This statement concerns the distributional local current; smearing can remove threshold weight if its Fourier transform vanishes there.

*Proof.* At speed one, Lorentz covariance and current conservation make the tensor spectral density `(q^μq^ν−q²g^{μν})ρ₁(q²)`. The free massless two-particle phase-space integral gives `ρ₁=C₁ θ(q⁰)θ(q²)`, `C₁>0`: scale invariance fixes the power and the nonzero current matrix element gives positivity. Thus the `00` component is `C₁|K|²` above the forward cone and zero below. The change `y=x/v` sends momentum to `vK`, with a positive normalization factor. At every nonzero `K` on `λ=v|K|`, the jump is nonzero, while the density is smooth on either side. The window contains points of that cone arbitrarily close to the origin for every finite `v>0`; the ratio there is `v`. □

**GAP 6.1.** The outline uses covariance and dimensional analysis alone to assert `C₁>0`. Those facts do not exclude a zero current spectral density; the nonzero free pair matrix element is an additional check. Proposition 5 does not establish R1-OBS at nonzero coupling or on a tick. Local fields in continuum QFT are distributions, so a rigorous algebraic version needs the smearing and spectral-access conditions of §2.

**Free-continuum positivity (referee closure, CN1_REFEREE.md).** Sketch: `ρ^{00}` is the spectral density of a vector, so it is a positive measure. It is the two-particle phase-space integral of `|⟨p,s;p',s'|j⁰(0)|Ω⟩|²`. For a massless Dirac field the right-handed part of this amplitude is the overlap of the `σ·p̂ = +1` and `σ·p̂' = −1` spinors; its square is `(1 − p̂·p̂')/2`, which is positive for non-parallel momenta. A positive continuous integrand on an open set gives `C₁ > 0`. The other parts of GAP 6.1 stay open: nonzero coupling, the tick (H-TRANSFER) and smeared local observables.

**Lemma 6 (already proved in `ZM1.md`, Lemma R-GI, in the corresponding fine-level form; see also `CH1_5UQ.md` Theorem 2.2 and `LZ1.md` Corollary 2.3 for local odd operators).** Let `ω` be invariant under every local gauge rotation `U_x(θ)=e^{iθG_x}` and let `α` commute with these rotations. If `ψ_x` has charge `−1` at `x` and zero charge at other sites, and similarly `ψ_y` at `y≠x`, where charge `−1` means `U_x(θ)ψ_xU_x(θ)^* = e^{−iθ}ψ_x`, then `ω(ψ_x^*α^n(ψ_y))=0` for every integer `n`.

*Proof.* Under conjugation by `U_x(θ)`, the first factor gains `e^{iθ}`, while `α^n(ψ_y)` is invariant. Invariance of `ω` makes the correlator equal to `e^{iθ}` times itself for all `θ`, so it vanishes. □

**GAP 6.2 (H1).** The lemma applies to the undressed correlator in an invariant state. A gauge-fixed propagator is a different object and need not obey this vanishing. The correct conclusion is that a gauge-fixed coefficient has no supplied identification with a ZM1-INV observable; R1-OBS or another bridge is needed. `LZ1.md` Theorem 2.2 proves flatness only for its specified odd local-band reading, and states: "flatness in it does not settle charged sectors or infraparticles". ZM1-INV does not map charged fields; it does not prove their physical absence.

## 7. Mechanism hypotheses and open attacks

The Chadha–Nielsen paper's text was not fetched in pass 1. The following are the outline's working hypotheses for later one-loop formulations, not a verified list of the original paper's assumptions.

| Name | Hypothesis or issue | Framework standing |
|---|---|---|
| H1 | Charged two-point-action speed is a meaningful flow variable | **GAP:** a gauge-fixed variable lacks the invariant-observable/zoom identification; Lemma 6 does not disprove a gauge-fixed propagator. |
| H2 | Continuous-time scale and light modes | A zoom level may be labelled `ℓ=k log L`; this does not establish continuous-time dynamics. `LZ1I.md` Theorem 10′ has specific band hypotheses and treats folding; it is not a general spectral transfer theorem. |
| H3 | Massless photon at all scales | Open: H-PHOTON and plaquette data. |
| H4 | Massless charged matter and divergent accumulated drag | Open: R-CS, MT1-S[R-CS], and the drag integral. `LZ1I.md` Theorem 11 gives the criterion only for its assumed flow. |
| H5 | Every light species carries the common gauge charge | Fails for the specified neutral bands of `LZ1I.md` Theorems 7–9 (in `H_phys`, line 80; mutually decoupled in the tick, line 194); T2 excludes them. Whether those bands couple to a gauge field is not established. |
| H6 | Small coupling and controlled higher orders | Open: Y2-W and R1-MOD. |
| H7 | No persistent marginal Lorentz-violating source | Open; Proposition 4 shows the consequence of such a source in its stated ODE. |

**R1-MOD attacks.** Pass 1 records: (1) the Giuliani–Mastropietro–Porta all-orders route stops at summing the orders; it also concerns reduced QED. (2) Integrating a Gaussian massless photon leaves a marginal long-range current kernel; the required scale-gap summability is not established. (3) Ward identities and exchange symmetry do not by themselves give the `O(G²)` size estimate; symmetry alone supplies at most a vanishing structure under suitable hypotheses. (4) At large `N`, leading fermion speeds remain fixed and the drag is `1/N`; convergence of that expansion is not established. R1″-MOD asks for the photon-mass version with `K,β` uniform in the number of scales. These are failed attacks as recorded, not impossibility theorems. For R1-OBS beyond free coupling the same attacks leave respectively the sum, kernel bound and threshold location open. The free cube tick is the first H-TRANSFER test.

## 8. Proposed readings and downstream scope

The outline's four checks ask whether a reading (1) fixes a part's target, (2) is closed rather than open-ended, (3) settles downstream physics by premise, and (4) adds unneeded structure. P means pass, C conditional, F fail. These are **pass-1 check results**, with the referee’s correction to R-PH test 1; they are not adoption or an independent validation of the readings. The gaps in §2 qualify CN1-OBS.

| Reading | Proposed content | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| CN1-OBS | invariant local spectral singular-support sets and mismatch, definition 5 | P | P | P | C |
| R-PH | R-Φ flux band plus Clifford cone | C | P | P | P |
| R-SCALE | identify `ℓ=k log L` for one coarse tick per `L` ticks | P | P | P | P |
| R-THR | charged species speed is the threshold of its own invariant current | P | C | C | P |
| T2 as an LZ1 reading | restrict all of LZ1's common-cone clause to charged species | F | P | F | P |

CN1-OBS does not state alignment; CN1-T′ proposes a domain repair and closes spectral access under T1. R-PH adds a cone requirement without constructing it. Its test 1 is conditional: as T1 of CN1-T it fixes no target, but as a meaning of "photon" for GA1 it would fix GA1's target. R-SCALE is a comparison convention, not a proof of a continuous RG. R-THR needs separately identifiable currents and compatibility with R-CS^str. T2 is used only as a conditional target hypothesis; the outline does not propose it as a reading of all LZ1.

If the photon's eigenphases near `K=0` all have one sign, `V` is not `C¹` at the node, so the photon has no Clifford cone in the sense of `LZ1I.md` line 23. CN1-OBS needs only `|λ|=c|K|+o(|K|)`; a T1 stated that way is the referee's proposed repair. Whether the VC1 vacuum has such one-signed photon eigenphases is open.

LZ1 needs a common speed for all of its stated species and `p≥2`, beyond the logarithmic pair result. ZM1 needs continuum threshold transfer, not just band transfer. GA1 needs an identified photon cone. MT1-S and R-CS need an invariant or dressed charged-sector prescription. ST1 still needs its own reconstruction and reflection-positivity inputs; GA2 needs anisotropy control; GR2 needs the tensor modes tied to the same speed. CN1-T alone supplies none of these bridges.

**Literature and search provenance.** Pass 1 records searches and references in `CN1_OUTLINE.md` §1, including Chadha–Nielsen, Kostelecký–Lane–Pickering, Isobe–Nagaosa, Anber–Donoghue, Giuliani–Mastropietro–Porta, Buchholz, and possible fixed-point routes. It reports no convergent 3+1-dimensional construction found; this is a search result, not a literature-wide no-go. The prior digest records repository evidence and its scope. Outside papers and historical branch versions were not independently fetched in this distillation; imported physics coefficients remain conditional.
