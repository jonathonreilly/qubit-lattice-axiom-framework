Reviewer model: claude-opus-5-5

# HINT55 — the non-free witness H_int: specification, comparator theorem, and reduction to layer-1 inputs

Worker file (Opus 5.5, worker not reviewer; the binding rules of REVIEW_BRIEF_55 apply). Writes only this file and
`checks/hi55_*`. No git. Labels: **PROVEN** (complete argument written here), **CONDITIONAL** (on named inputs, each
listed with owner file and owner's status), **ARGUED** (reasoned, hole named), **OPEN**, **[m]** (literature from
memory, not re-read), **IMPORTED** (standard result used without re-derivation, named). Statuses quoted from other files
are those files' labels, not re-verified here unless this file says so.

## PRE-STATED — 2026-10-28 23:45:27 UTC

*Honest provenance.* Before this text I read REVIEW_BRIEF_55, PANEL_P1 (all), PANEL_P3 (all), PANEL_P2 §8 and the
S0-S4 lemma statement, PANEL_P4 §2.2 and §9.1, PLAN_S26 §4/§6/§9, HANDOFF (head), FLOW §0 and §7-§13 (Theorems
F-flow, F-tune), and EXISTENCE §0 (status block and §0 table), §10.1 (X-NTAF, X-NTAF-AF, X-WIL), §13.4 (Lemma CBE,
Theorem CB), §13.6 statements of LAP^S and H-Bal-3T^S, §16.2 (Theorem SIG-FREE, Corollary SEP), §19 (all), §20.1-§20.2,
§20.4, §21.3 (consumer list). Exploratory reasoning about the witness preceded this text and was not written down; no
derivation, criteria file or script of this file existed before this time stamp.

**Question.** Specify a witness W for H_int (PANEL_P1 §3 item 4): a continuous finite-moment functional of local,
gauge-invariant, noise-free observables, vanishing (or sign-definite) on a named class of free theories including
mixtures, with |W(ω_{a,R})| ≥ c > 0 at fixed renormalized coupling uniformly in volume; and reduce that lower bound to
named layer-1 inputs.

**Targets.**
- **T1 (specification and test of the scale-variation candidate).** Fix the observable (gradient-flowed energy density
  f(t) := t²ω(E(t)); smeared plaquette energies as the alternative), the comparator classes, and W. Test, each
  separately, whether W_GF := f(t₂) − f(t₁) vanishes or has a fixed sign on: (i) canonical massless free abelian gauge
  fields (N² − 1 copies, any couplings, any gauge fixing); (ii) their mixtures; (iii) massive and generalized free
  fields; (iv) Euclidean representatives of free theories that differ only by contact terms (same OS reconstruction);
  (v) soft-variable realizations (auxiliary noise). Say what "free comparator" must mean for SU(N) and whether
  normalisation choices can fake a t-variation.
- **T2 (reduction).** State exactly which layer-1 statements imply |W| ≥ c > 0 uniformly in cutoff and volume, as a
  CONDITIONAL theorem with every input named (owner file, owner's status), and say which inputs are new.
- **T3 (prove now).** Prove the comparator-side statements; compute the leading-order YM value; state the size of the
  error term the YM side may have.
- **T4 (existence lane).** For Lemma DIFF, LO-D, (WC), NT-red, NT-pol, (H-sig^S)/SIG-FREE, SPEC-red(^ms), NG-red/NG-ax,
  X-NTAF(^S): reusable or not, and which part of the bar each fails.

**What counts as a refutation (written before deriving).**
- Of "W vanishes on class X": one explicit state in X (or a mixture) with W ≠ 0. Of "W has the sign opposite to YM on
  X": one explicit state in X with W of the YM sign. Either found is reported as such, and the class or witness is then
  repaired, not silently narrowed.
- Of the reduction (T2): an input that is H_int restated — a lower bound on a quantity that already separates YM from
  the comparator class — or an implication whose proof uses an unlisted estimate. Of "uniform in volume": any constant
  that depends on the torus side.
- Of a check: a gate that could not have failed. Every check below gets a designed-FAIL control.
- Checks use exact rational arithmetic in plain Python (`fractions`), with rigorous rational enclosures for exp/log
  where needed; criteria files precede scripts.

---

# Derivations (written after PRE-STATED and after checks/hi55_{a,b,c}_criteria.md; before any hi55 script)

**Symbol table for this file (collisions with the lane are deliberate-avoided and stated).**
- R = physical box (torus) side, as in PANEL_P1's ω_{a,R}. **R_F := FLOW's additive constant "R = 2R_0"** of (F_R)
  (FLOW §7, Theorem F-flow) — renamed here because FLOW's R is not a box size.
- L = blocking factor; level k = after k RG steps, k = 0 bare, k = K unit lattice (FLOW §0); m := K − k ≥ 0 (levels below
  the unit lattice, = EXISTENCE's "resolution m"); u_k := 1/g_k² along the tuned sequence (FLOW Def F-g).
- t = continuum flow time (physical units, unit lattice = 1); t^{(m)} := c_t L^{−2m}, c_t > 0 fixed.
- E(t,x) = −½tr(G_μνG_μν)(t,x) = ¼G^a_μνG^a_μν (tr T^aT^b = −½δ^{ab}); 𝓔(t,x) := t²E(t,x); f_ω(t) := ω(𝓔(t,0)).
- ŝ, h(u) := uŝ(u), ρ (Källén–Lehmann measure), P (contact polynomial), J(σ) := ∫_0^∞v²e^{−2v}(v+σ)^{−1}dv.
- (TS) constants c₋, C₊, exponent ϑ ∈ [0,1) (not the lane's θ). U_±(m) := g^{−2} + β_±m log L ± R_F (F-tune's bounds).
- N² − 1 written out (the lane's n is a level count).

## 1. Specification

### 1.1 The observable (noise-free, geometric normalisation)
On the lattice aZ⁴ ∩ (torus of side R) the variables are the **bare** links U_b ∈ SU(N) of the Wilson measure — the
level-0 variables of the soft chain, never the soft variables U_k, k ≥ 1. The Wilson flow V(τ) (τ = t/a²) solves
dV_b/dτ = −(∂_bS_geo(V))V_b, V(0) = U, with S_geo the Wilson action **without** the factor β (geometric normalisation,
U = e^{aA}); E_lat(t,x) is a fixed (plaquette or clover) lattice energy density of V(t/a²) normalised so that it tends to
¼G^aG^a on smooth fields [m: Lüscher's construction]. 𝓔(t,x) := t²E_lat(t,x). Properties used: gauge invariant,
≥ 0, hypercubic covariant, a fixed functional of U for each t (no coupling, no level, no kernel parameter enters its
definition), quasi-local at scale √t. The same statements are made for the alternative **block** observable
Ψ_m := ‖log V^{(m)}_p‖²_HS, V^{(m)}_p a plaquette of the **deterministic** S4c block field at resolution m,
V^{(m)} := A^{K−m}(U) (EXISTENCE ES4 and X-S4c: continuous, local, gauge covariant; level k = K − m) — bounded, strictly
local, noise-free.

### 1.2 The algebra on which "free" is decided
Let 𝔈 be the commutative algebra generated by symbols 𝓔(t,x), t > 0, x ∈ R⁴. A theory gives a state on 𝔈 by
**realising** the symbols: Yang–Mills by the (lattice approximants of the) nonabelian flow above; an abelian comparator
by 𝓔(t,x) := (t²/4)Σ_aΣ_{μν}[(K_t ∗ F^a_μν)(x)]², K_t the heat kernel, F^a (a = 1, …, N² − 1) abelian field strengths
(the abelian flow of the field strength is exactly K_t∗, independent of the gauge-flow parameter). "ω is free relative
to a class 𝒳" means: the law of the energy-density field 𝓔 under ω is its law under some member of 𝒳 (or of a mixture).
This is the identification that makes "Yang–Mills is N² − 1 free photons" a statement that could be true or false; it
is the g → 0 contraction su(N) → R^{N²−1}. Only one-point functions f(t) enter the witness.

### 1.3 Comparator classes
Fix Fourier convention f̂(p) = ∫e^{−ipx}f(x)dx and put, for p ∈ R⁴,
  T^I_{μν,ρσ}(p) := p_μp_ρδ_νσ − p_μp_σδ_νρ − p_νp_ρδ_μσ + p_νp_σδ_μρ.
An **abelian field-strength state** is a law (any law — Gaussian or not) of N² − 1 antisymmetric-tensor-valued
generalised random fields F^a on R⁴, invariant under translations and O(4), with finite second moments on Schwartz test
functions and summed two-point function
  Σ_a E[F^a_μν(x)F^a_ρσ(y)] = ∫ e^{ip(x−y)} T^I_{μν,ρσ}(p) ŝ(p²) d⁴p/(2π)⁴,          (1.1)
with ŝ ≥ 0 (positivity of the two-point function forces ŝ ≥ 0, since T^I(p) is positive semidefinite, Lemma TR).
- **𝔊₀**: ŝ(u) = ∫_{[0,∞)}dρ(m²)/(u + m²) + P(u), ρ ≥ 0 with ∫dρ(m²)/(1 + m²) < ∞, P a real polynomial, ŝ ≥ 0.
- **𝔊₁** (one Källén–Lehmann subtraction): ŝ(u) = ∫dρ(m²)[1/(u + m²) − 1/(1 + m²)] + P(u), ρ ≥ 0 with
  ∫dρ/(1 + m²) = ∞ and ∫dρ/(1 + m²)² < ∞, P polynomial, ŝ ≥ 0.
- **𝔊 := 𝔊₀ ∪ 𝔊₁.** **𝔉₀** ⊂ 𝔊₀: the canonical massless free fields — centred Gaussian, ŝ(u) = (Σ_ae_a²)/u (N² − 1
  Maxwell fields with arbitrary, possibly colour-dependent, couplings e_a² ≥ 0; any gauge fixing, Lemma TR (iii)).
  **𝔉_free**: the centred Gaussian members of 𝔊 = every free (generalised free) abelian gauge field with at most one
  Källén–Lehmann subtraction — massless, massive (Proca), superpositions — **and every Euclidean representative of each
  that differs by point-supported (polynomial) contact terms.**
- **𝔖**: states on 𝔈 that are scale invariant, ω(𝓔(λ²t, λx)) = ω(𝓔(t,x)) for all λ > 0.
- **conv(𝒳)**: mixtures ∫μ_α dν(α), ν a probability measure on a measurable family in 𝒳.
- *Remarks.* (i) Two members of 𝔊₀ with the same ρ and different P have identical reflection-positivity forms for the
  linear field (P contributes only point-supported terms, which vanish on pairs of test functions supported in opposite
  open half-spaces), hence the same OS reconstruction of the linear field: **𝔊 contains, with each free theory, its
  whole family of OS-equivalent Euclidean representatives with polynomial contact terms.** (ii) By the Källén–Lehmann
  theorem for the field strength [IMPORTED, not re-derived here: RP + O(4) + Bianchi ⇒ (1.1) with ŝ a K-times-subtracted
  Stieltjes function plus a polynomial], 𝔊 contains the energy-density sector of **every** reflection-positive abelian
  theory (free or interacting) needing K ≤ 1 subtraction. Only (ii) uses this import; everything PROVEN below is for the
  explicitly defined class 𝔊.

### 1.4 The witness
  W_GF(ω; t₁, t₂) := f_ω(t₂) − f_ω(t₁),  0 < t₁ < t₂     (affine in ω; two local one-point functions).
  **(AF-W)**  f_ω(t₀) > liminf_{t→0} f_ω(t)  (the right side finite)  — "the gradient-flow coupling at a finite scale
  exceeds its ultraviolet value": vanishing bare charge.
**H_int, as specified here.** There are a fixed physical t₀ = t^{(m₀)}, a constant c_W > 0 and m₁ ≥ m₀ such that, for
every m ≥ m₁, uniformly in the lattice spacing (all K ≥ m + d₀) and in the box:
  W_m(ω_{a,R}) := W_GF(ω_{a,R}; t^{(m)}, t^{(m₀)}) ≥ c_W.                                          (1.2)
This is a countable family of affine finite-moment inequalities of PANEL_P2's S4 type. In any limit state it gives
(AF-W) (Theorem H-RED below), and (AF-W) excludes conv(𝔊 ∪ 𝔖) (Theorem SEP). Proposition CT shows that **no finite
subfamily of (1.2) can exclude the OS-equivalent representatives of the free massless field**: the UV end of the family
is essential, not decorative.

## 2. Comparator side (all PROVEN unless labelled)

### 2.1 Lemma TR (tensor identities). PROVEN (hand; exact check hi55_a A1, A2)
(i) T^I_{μν,ρσ}(p) = Σ_λ v^λ_{μν}(p)v^λ_{ρσ}(p) with v^λ_{μν}(p) := p_μδ_νλ − p_νδ_μλ; hence T^I(p) is positive
semidefinite on antisymmetric tensors. (ii) Σ_{μ,ν}T^I_{μν,μν}(p) = 2(d − 1)p² = 6p² (d = 4). (iii) If A has covariance
e²D(p), D_μν := (δ_μν − (1 − ξ)p_μp_ν/p²)/p², ξ ≥ 0, then F = dA has two-point function e²T^I(p)/p², independent of ξ.
*Proof.* (i) Expand Σ_λ(p_μδ_νλ − p_νδ_μλ)(p_ρδ_σλ − p_σδ_ρλ): the four products give the four terms of T^I. (ii) The
four terms traced give d p² − p² − p² + d p². (iii) F_μν(p) = i(p_μA_ν − p_νA_μ), so ⟨F_μνF*_ρσ⟩ = p_μp_ρD_νσ − p_μp_σD_νρ
− p_νp_ρD_μσ + p_νp_σD_μρ; the p_μp_ν/p² part of D contributes ±p_μp_νp_ρp_σ/p⁴ with signs + − − +, which cancel. ∎

### 2.2 The formula for f, and the canonical free value. PROVEN
For a state satisfying (1.1), the heat kernel being Schwartz and even, E[(K_t∗F^a_μν)(0)(K_t∗F^a_μν)(0)] is the
two-point function paired with K_t ⊗ K_t, and K_t∗K_t = K_{2t} has symbol e^{−2tp²}. With Lemma TR (ii) and
d⁴p/(2π)⁴ = u du/(16π²) (u = p²):
  f(t) = (t²/4)·6∫e^{−2tp²}p²ŝ(p²)d⁴p/(2π)⁴ = (3t²/32π²)∫_0^∞u²e^{−2tu}ŝ(u)du = (3/32π²)∫_0^∞ v e^{−2v} h(v/t) dv,   (2.1)
the last form by u = v/t, with h(u) := uŝ(u) ≥ 0 (Tonelli: all integrands ≥ 0). For 𝔉₀, h ≡ Σ_ae_a² and
∫_0^∞ve^{−2v}dv = 1/4, so **f ≡ 3Σ_ae_a²/(128π²)**: W_GF = 0 for every member of 𝔉₀ and (affinity) every mixture of
members at different couplings. With e_a² = g² this is the Yang–Mills tree-level value (§3.1).

### 2.3 Lemma SI (scale invariance kills the witness). PROVEN
If ω ∈ 𝔖 then f_ω(λ²t) = f_ω(t) for all λ, t: f_ω is constant, every W_GF vanishes and (AF-W) fails. 𝔖 is convex.
Members: 𝔉₀ (F_λ(x) := λ²F(λx) has the law of F because e²T^I(p)/p² is homogeneous of degree 0; and
(K_t∗F_λ)(x) = λ²(K_{λ²t}∗F)(λx), from K_t(x − z/λ) = λ⁴K_{λ²t}(λx − z), so 𝓔[F_λ](t,x) = 𝓔[F](λ²t, λx)).
*ARGUED (formal, not needed below):* the nonabelian flow of a centred Gaussian connection with covariance homogeneous
of degree −2 (Feynman, Landau, any covariant gauge) is scale covariant — B_λ(t,x) := λB(λ²t, λx) solves
∂_tB = D_νG_νμ if B does — so such "Gaussian-connection" realisations, if they exist for rough data, lie in 𝔖 too. They
are not free quantum field theories (not reflection positive in covariant gauges); they are listed only because
EXISTENCE §20.4 (Lemma PO) shows they defeat odd witnesses. They do not defeat this one.

### 2.4 Theorem KLM (Källén–Lehmann monotonicity for every self-similar quadratic smearing). PROVEN
Let φ^{(1)}, …, φ^{(r)} be antisymmetric-tensor-valued Schwartz functions, not all zero, φ^{(i)}_s(x) := s^{−2}φ^{(i)}(x/s)
(s > 0), and F(φ) := ½Σ_{μν}∫F_μν φ_μν. For a state satisfying (1.1) put Q(s) := Σ_iΣ_aE[F^a(φ^{(i)}_s)²] ∈ [0, ∞]. Then
  Q(s) = ∫_{R⁴} w(v) h(|v|²/s²) d⁴v,  w(v) := Σ_i \overline{φ̂^{(i)}(v)}·T^I(v)·φ̂^{(i)}(v)/(4(2π)⁴|v|²) ≥ 0.
Hence **if h is non-decreasing on (0, ∞), s ↦ Q(s) is non-increasing**, and constant if h is constant.
*Proof.* φ̂_s(p) = s²φ̂(sp). By (1.1), E[F(φ_s)²] = ¼∫s⁴\overline{φ̂(sp)}T^I(p)φ̂(sp)ŝ(p²)d⁴p/(2π)⁴. Substitute v = sp
(d⁴p = s^{−4}d⁴v, T^I(v/s) = s^{−2}T^I(v)): the integrand becomes \overline{φ̂(v)}T^I(v)φ̂(v)·s^{−2}ŝ(v²/s²) =
[\overline{φ̂}T^Iφ̂/|v|²]·h(v²/s²). w ≥ 0 by Lemma TR (i). If s < s′ then v²/s² > v²/s′², so h(v²/s²) ≥ h(v²/s′²) pointwise,
and integrate (values in [0, ∞]). ∎
*Applications.* (a) 𝓔(t,0) is of this form with s = √t: tK_t(y) = s^{−2}K_1(y/s), one φ per component (μν). So f is
non-increasing in t whenever h is non-decreasing. (b) The linearised (abelian) block flux squared Σ_a(φ^a_s)² of a
self-similar block kernel is of this form (§4.4). (c) **When is h non-decreasing?** If ŝ = ∫dρ/(u + m²) + p₀ with p₀ ≥ 0:
h(u) = ∫dρ(m²)u/(u + m²) + p₀u, each term non-decreasing. This is the **screening** property: h(u) is the effective
charge at momentum √u (Källén's 0 ≤ Z₃ ≤ 1 in flow-time form [m]); f(t) = (3/32π²)∫ve^{−2v}h(v/t)dv is that charge
averaged at scale u ≍ 1/t. **Asymptotic freedom (f increasing in t) is anti-screening, which a positive spectral weight
for a gauge-invariant field strength forbids**; Yang–Mills escapes because F^a is not gauge invariant and E is not the
square of a reflection-positive field.

### 2.5 Proposition CT (contact terms fake the scale variation; no finite family of W's suffices). PROVEN
For ε_c > 0, e² > 0 let μ_{ε_c} be the centred Gaussian field strength (1.1) with ŝ(u) = e²(1/u − ε_c + ε_c²u).
(i) ŝ(u) − e²ε_c = e²(1 − ε_cu)²/u ≥ 0, so ŝ ≥ e²ε_c > 0 and μ_{ε_c} exists (Bochner–Minlos), is O(4) invariant and
satisfies Bianchi (its covariance is T^I times a scalar). (ii) μ_{ε_c} ∈ 𝔊₀ with ρ = e²δ_0, P(u) = e²(−ε_c + ε_c²u), and
by Remark 1.3 (i) its linear field has exactly the reflection form, hence the OS reconstruction, of the free massless
field μ_0 ∈ 𝔉₀ (Gaussian RP follows from RP of the covariance [STANDARD; e.g. the Wick-exponential argument written in
PANEL_P3 §2]). (iii) From (2.1) with ∫_0^∞u^ke^{−2tu}du = k!/(2t)^{k+1}:
  f_{ε_c}(t) = (3e²/32π²)[1/4 − ε_c/(4t) + 3ε_c²/(8t²)],  f′_{ε_c}(t) = (3e²ε_c/128π²t²)(1 − 3ε_c/t).
So f_{ε_c} is strictly increasing on (3ε_c, ∞): **W_GF(μ_{ε_c}; t₁, t₂) > 0 for all 3ε_c < t₁ < t₂**, and it is made
arbitrarily large by scaling e². Given any finite set of flow times, choose ε_c below a third of the smallest: every
member of a finite family (1.2) is positive on this OS-equivalent representative of the free massless field.
(iv) f_{ε_c}(t) → ∞ as t → 0. (Exact arithmetic: hi55_a A3.) ∎
**Verdict on the candidate as posed in the brief.** "t²⟨E(t)⟩ is t-independent in every free theory and every mixture"
is **true for the canonical representatives (𝔉₀ and all of 𝔖)**, **false as a sign statement for massive and generalised
free fields** (they have W < 0, the opposite sign to Yang–Mills: harmless), and **false for OS-equivalent Euclidean
representatives with contact terms** (any sign, including the Yang–Mills one): refutation of "W_GF alone excludes free
theories up to OS equivalence", repaired by (1.2)'s UV family via Lemma UV-D and Theorem SEP.

### 2.6 Lemma UV-D (dichotomy on 𝔊). PROVEN
For μ ∈ 𝔊 exactly one holds: (a) ŝ = ∫dρ/(u + m²) + p₀ with p₀ ≥ 0 (a member of 𝔊₀ with deg P ≤ 0); then f_μ is
non-increasing on (0, ∞) and f_μ(t) ↑ 3ρ([0,∞))/(128π²) + ∞·1[p₀ > 0] as t ↓ 0; (b) otherwise f_μ(t) → +∞ as t → 0.
Consequently **liminf_{t→0} f_μ(t) < ∞ implies: p₀ = 0, ρ is finite, f_μ is non-increasing, and
f_μ(t) ≤ f_μ(0+) = 3ρ([0,∞))/(128π²) for every t.**
*Proof.* *𝔊₀.* ∫dρ/(u + m²) → 0 as u → ∞ (dominated by 1/(1 + m²) for u ≥ 1). If deg P ≤ 0, ŝ ≥ 0 at large u forces
p₀ ≥ 0; then KLM (c) gives monotonicity, and (2.1) with Tonelli gives f(t) = (3/32π²)[∫dρ(m²)J(tm²) + p₀/(4t)], where
J(σ) := ∫_0^∞v²e^{−2v}/(v + σ)dv is decreasing with J(0) = 1/4; monotone convergence gives the limit. If deg P = d ≥ 1,
its leading coefficient p_d > 0 (else ŝ → −∞), so ŝ(u) ≥ (p_d/2)u^d for u ≥ U₀, and since ŝ ≥ 0 everywhere,
f(t) ≥ (3t²/32π²)(p_d/2)∫_{U₀}^∞u^{d+2}e^{−2tu}du ≥ (3t²/32π²)(p_d/2)[(d+2)!/(2t)^{d+3} − U₀^{d+3}/(d+3)] → ∞.
*𝔊₁.* S₁(u) := ∫dρ(m²)(1 − u)/((u + m²)(1 + m²)) is finite for u > 0 (|integrand| ≤ |1 − u|/(min(u,1)(1 + m²)²)).
For u ≥ 1 the integrand is ≤ 0 and decreasing in u (∂_u[(1 − u)/(u + m²)] = −(1 + m²)/(u + m²)²) with limit −1/(1 + m²),
so by monotone convergence S₁(u) → −∫dρ/(1 + m²) = −∞; and S₁(u)/u → 0 (integrand of S₁/u dominated by 1/(1 + m²)² for
u ≥ 1). Then ŝ = S₁ + P ≥ 0 forces deg P = d ≥ 1 with p_d > 0 and ŝ(u) ≥ (p_d/2)u^d for large u; conclude as above. ∎
*Not covered (ARGUED):* K ≥ 2 subtractions; the same mechanism (S_K = o(u^K), so a polynomial must dominate and f → ∞)
should apply, but it is not written out.

### 2.7 Theorem SEP (separation, including mixtures). PROVEN
Let μ̄ = ∫μ_αdν(α) be a mixture of members of 𝔊 ∪ 𝔖 with f_μ̄(t) = ∫f_{μ_α}(t)dν(α) ∈ [0, ∞]. If
ℓ := liminf_{t→0}f_μ̄(t) < ∞, then **f_μ̄(t₀) ≤ ℓ for every t₀ > 0**. Hence a state satisfying (AF-W) is not in
conv(𝔊 ∪ 𝔖).
*Proof.* Take t_n ↓ 0 with f_μ̄(t_n) → ℓ. Fatou (f_α ≥ 0): ∫liminf_nf_{μ_α}(t_n)dν ≤ ℓ < ∞, so for ν-a.e. α,
liminf_nf_{μ_α}(t_n) < ∞. For such α ∈ 𝔊, Lemma UV-D puts μ_α in case (a) with f non-increasing; for α ∈ 𝔖, f is
constant. In both cases f_{μ_α}(t₀) ≤ f_{μ_α}(t_n) whenever t_n ≤ t₀. Integrating, f_μ̄(t₀) ≤ f_μ̄(t_n) for all large n,
so f_μ̄(t₀) ≤ ℓ. ∎
**Corollary SEP-1.** If ω satisfies (AF-W), the law of its energy-density field is not that of: any free abelian gauge
theory with N² − 1 components (massless at any couplings, massive, generalised free with ≤ 1 subtraction), any
OS-equivalent Euclidean representative of one with polynomial contact terms, any non-Gaussian state with such a
two-point function (e.g. Gaussian plus independent point-supported noise), any scale-invariant state, or any mixture
of these; and, given the imported Källén–Lehmann theorem, not that of any reflection-positive abelian theory with ≤ 1
subtraction, interacting or not.
**Corollary SEP-2 (one affine witness, canonical classes).** Every μ ∈ conv(𝔊₀^{≤0} ∪ 𝔖), 𝔊₀^{≤0} := {deg P ≤ 0}, has
W_GF(μ; t₁, t₂) ≤ 0 for all t₁ < t₂ with f_μ(t₁) < ∞ (KLM + affinity). So a single W_GF > 0 already excludes every
canonical free and generalised-free field and every mixture; only contact terms of degree ≥ 1 and subtracted spectral
measures need the UV family.
**Corollary SEP-3 (survives averaging).** In the continuum, 𝓔(t,0) is a scalar at the origin, so for a rotation average
ω̄ = ∫ω∘α_g dg over SO(4) (or a translation average of a translation-invariant state) f_ω̄ = f_ω: (AF-W) and (1.2) are
preserved by PANEL_P1/P3's averaging routes — the "shared affine witness" PANEL_P1 §3 asks for.

### 2.8 Normalisation, gauge, lattice and soft noise: what can and cannot fake the variation
- **(N1) Constant normalisations cannot.** Rescaling F^a ↦ λ_aF^a (colour-dependent allowed) maps 𝔊 into 𝔊 and 𝔖
  into 𝔖; a constant factor in 𝓔 rescales f and preserves (AF-W). PROVEN (immediate).
- **(N2) Scale-dependent normalisations can.** 𝓔̃(t) := n(t)𝓔(t) with non-constant n turns the constant f of 𝔉₀ into
  a varying one (e.g. dividing by a running coupling, or the level-dependent normalisations below). The witness must
  apply one fixed functional of the bare field at every t; the flow time is the only parameter varied. PROVEN
  (immediate).
- **(N3) Gauge fixing cannot:** E is gauge invariant; for comparators Lemma TR (iii).
- **(N4) Lattice artifacts:** on the free lattice Maxwell field, τ²⟨E_lat(τ)⟩ = (3/2)·τ²(e^{−4τ}I_0(4τ))⁴ (§7, hi55_c),
  which approaches 3/(128π²)(1 + 1/(8τ) + O(τ^{−2})) from above (screening sign) at τ = t/a² ≳ 1; the artifact is
  O(a²/t) and enters (1.2) only through the depth margin d₀. Informational.
- **(N5) Soft variables do fake it — proven by the existence lane itself.** EXISTENCE Corollary SEP (a) (§16.2): in the
  free Gaussian soft chain with (F)-type kernel couplings, the **soft** block plaquette obeys a two-sided logarithmic
  running in m, while the fine field is free. Mechanism, re-derived here in one line (linear chain): the soft flux at
  level m is (deterministic flux) + Σ_k(averaged noise ζ_k), the noise of level k having variance ∝ g_k²/κ (EXISTENCE
  LAP^S: "properties of the kernel … no information about the Wilson measure"), and g_k runs by (F). So **witnesses
  built from soft variables U_k, k ≥ 1, do not meet the bar as such**: a free fine field with the lane's kind of kernel
  satisfies the conclusions of X-NTAF^S (Cor. SEP (a), fine coupling the finest term of a running sequence), (H-sig^S)
  (SIG-FREE (ii), constant fine coupling) and SPEC-red(^ms) (EXISTENCE [RX10-fix 7]: "free gluons meet the same bound");
  for NG-red/NG-ax see §6 (ARGUED). PROVEN for the first three by the cited results (read;
  constants not re-checked) and the mechanism re-derived above. *(In-place edit, see §9.3.)*
- **Lemma BARE (bare witnesses are scheme-independent). PROVEN.** The chain's joint density is
  Z^{−1}e^{−S_0(U_0)}Π_{k<K}K_k(U_{k+1}, U_k) with ∫K_k(V, U)dV = 1 (EXISTENCE Lemma MK; §13.5). Integrating U_K, U_{K−1},
  …, U_1 in turn leaves the Wilson density of U_0. So for every function O(U_0), E_{P_K}[O] is the Wilson expectation,
  whatever the kernels, κ or the kernel couplings: a bare-field witness cannot be produced or removed by the soft scheme.

### 2.9 What "free comparator" must mean for SU(N)
The free limit of SU(N) Yang–Mills is N² − 1 Maxwell fields (the contraction su(N) → R^{N²−1}), observed through the same
energy density. The witness needs no gauge, no calibration of "the" free coupling (all e_a² are allowed, colour by
colour), and no normalisation convention for the gauge field beyond (N1)-(N2). Three things are **not** comparators:
(i) "Gaussian connections" observed through nonabelian holonomies or the nonabelian flow — gauge dependent, not
reflection positive in covariant gauges; when scale invariant they lie in 𝔖 anyway (§2.3); (ii) any free fine field
seen through soft variables (N5); (iii) torus zero-mode/toron sectors (not local R⁴ theories). The named class is
𝔊 ∪ 𝔖 and mixtures; it is larger than "the" free theory in every direction the panels asked about (mixtures,
massive/generalised free, contact representatives, abelian interactions).

## 3. Yang–Mills side at leading order, and the size of error the reduction tolerates

### 3.1 The tree-level coefficient. PROVEN (free-field computation; hi55_a A4)
With A = gA_c (A_c canonically normalised) the O(g²) term of f in Yang–Mills is the free value of §2.2 with e_a² = g²
for each of the N² − 1 colours (at this order only the Gaussian part of the measure and the linear part of the flow
enter):  f(t) = A_∞g² + O(g⁴),  **A_∞ := 3(N² − 1)/(128π²)**  (= (t²/4)·6·(16π²)^{−1}·∫_0^∞ue^{−2tu}du·(N² − 1)).
In FLOW's normalisation u = β_Wilson = 2N/g_std², so A_∞g_std² = 3(N² − 1)·2N/(128π²u).

### 3.2 The leading running. ARGUED / IMPORTED (renormalised perturbation theory; not a constructive statement)
[m: Lüscher, JHEP 1008:071 (2010)] f(t) = A_∞ḡ²(q)[1 + k₁ḡ²(q) + O(ḡ⁴)] with q = (8t)^{−1/2} and ḡ the MS-bar coupling;
dḡ²/d ln t = b₀ḡ⁴ + O(ḡ⁶), b₀ = 11N/(48π²) (FLOW L4b, IMPORTED-AND-REVERIFIED there). Since f depends on t only through
ḡ(q) (dimensionless, q ∝ t^{−1/2}), k₁ is t-independent and cancels at this order:
  W_GF(t₁, t₂) = A_∞b₀ ḡ⁴ log(t₂/t₁) + O(ḡ⁶log²(t₂/t₁)) = (33N(N² − 1)/(6144π⁴)) ḡ⁴ log(t₂/t₁) + …,  ḡ = ḡ((8t₁)^{−1/2}),
positive (SU(2): 3.31·10⁻⁴ ḡ⁴log(t₂/t₁); SU(3): 1.32·10⁻³ ḡ⁴log(t₂/t₁); hand arithmetic). It is the anti-screening sign
that Theorem KLM forbids for every comparator in 𝔊₀^{≤0}. And f(t) → 0 as t → 0 (ḡ → 0): the vanishing bare charge of
(AF-W), which Lemma UV-D forbids for every comparator in 𝔊.

### 3.3 What error the Yang–Mills side may have
Two routes, both proven in §4:
- **Crude route (Theorem H-RED; sufficient for H_int).** Only two-sided comparability with the RG coupling,
  c₋g_k² ≤ f ≤ C₊g_k^{2−2ϑ}, with **arbitrary** constants 0 < c₋ ≤ C₊ and ϑ ∈ [0,1), plus the sign of the flow (β₋ > 0).
  No error term has to be small, no perturbative coefficient enters except that sign, and k₁, b₁, the scheme conversion
  and the non-perturbative "condensate" contribution ≍ t²Λ⁴ are all irrelevant. The price is the scale separation:
  t^{(m₀)}/t^{(m₁)} = L^{2(m₁ − m₀)} with m₁ from (4.1), astronomically large when C₊/c₋ is (e.g. with X-NTAF's δ_* ≈ 10⁻³⁴
  type constants) but a fixed number.
- **Sharp route (Theorem H-RED-sharp; moderate separation).** If f(t_k) = A/(u_k + O(1)) with one k-independent A, i.e.
  |A/f(t_k) − u_k| ≤ C_sch (a bounded additive error in 1/g², equivalently an O(g⁴) error in f with bounded, not small,
  coefficient), then a single W_GF at separation L^{2Δ₀}, Δ₀ the least Δ with β₋Δ log L > R_F + 2C_sch, is positive. This
  alone does not exclude contact-term representatives (Proposition CT); it excludes conv(𝔊₀^{≤0} ∪ 𝔖) (Corollary SEP-2).

## 4. Reduction of H_int to named layer-1 inputs

### 4.1 Theorem H-RED (vanishing-charge form). PROVEN implication; CONDITIONAL on the inputs named
*Setting.* F-tune's tuned sequence at renormalised coupling g ∈ (0, g₁] (FLOW §8):
  (F-tune)  U₋(m) ≤ u_{K−m} ≤ U₊(m) and u_{K−m} − u_{K−m₀} ≥ β₋(m − m₀)log L − R_F  (0 ≤ m₀ ≤ m ≤ K),  β₋ > 0,
with γ, g₁, β_±, R_F independent of K and of the torus (FLOW §8 step 5). Owner: FLOW Theorems F-flow, F-tune —
PROVEN-HERE there given (UNIV-1L) [OPEN], (SF-g), (RLF-δ), (SF-cont), (SF-∞); "CONFIRMED conditional" per EXISTENCE
§21.3 row B. Not re-verified here.
*Inputs* (each for all K ≥ m + d₀ and all torus sides ≥ R₀; d₀, R₀ fixed):
- **(TS-low)** at one m₀: f_{a,R}(t^{(m₀)}) ≥ c₋/u_{K−m₀}.
- **(TS-up)** for every m ≥ m₀: f_{a,R}(t^{(m)}) ≤ C₊u_{K−m}^{ϑ−1}, some ϑ ∈ [0,1).
- **(MOM-E)** sup ω_{a,R}(𝓔(t^{(m₀)},0)²) ≤ M₂.
- **(CONV-E)** along PANEL_P1's H_reg subsequence (a_j, R_j) the laws of 𝓔(t^{(m)},0), m ≥ m₀, converge weakly.
WLOG C₊ ≥ c₋ and U₊(m₀) ≥ 1. Let x := U₊(m₀) and let m₁ ≥ m₀ be the least integer with
  (x + β₋(m₁ − m₀)log L − R_F)^{1−ϑ} ≥ 2C₊x/c₋.                                                         (4.1)
*Conclusion.* For every m ≥ m₁, every K ≥ m + d₀ and every torus side ≥ R₀:
  W_m(ω_{a,R}) = f_{a,R}(t^{(m₀)}) − f_{a,R}(t^{(m)}) ≥ c_W := c₋/(2U₊(m₀)) > 0,                        (4.2)
i.e. (1.2) holds with constants independent of the cutoff and the volume, at the fixed renormalised coupling g. Every
limit point ω along (a_j, R_j) has f_ω(t^{(m₀)}) ≥ c₋/U₊(m₀), W_m(ω) ≥ c_W for all m ≥ m₁, and
f_ω(t^{(m)}) ≤ C₊(U₋(m₀) + a_m)^{ϑ−1} → 0 (a_m defined in the proof); so ω satisfies (AF-W) and, by Theorem SEP,
**ω ∉ conv(𝔊 ∪ 𝔖)**.
*Proof.* Put y := u_{K−m₀} ∈ [U₋(m₀), x] and a_m := β₋(m − m₀)log L − R_F. By (4.1), C₊ ≥ c₋ and x ≥ 1 one has
(x + a_{m₁})^{1−ϑ} ≥ 2x > x, so a_{m₁} > 0, and a_m ≥ a_{m₁} for m ≥ m₁. By (F-tune), u_{K−m} ≥ y + a_m > 0; since ϑ − 1 < 0,
(TS-up) gives f(t^{(m)}) ≤ C₊(y + a_m)^{ϑ−1}. The function ψ_a(z) := (z + a)^{1−ϑ}/z (a > 0) is decreasing on z > 0
(ψ_a′(z) = −(z + a)^{−ϑ}(ϑz + a)/z² < 0) and (z + a)^{1−ϑ} is increasing in a, so ψ_{a_m}(y) ≥ ψ_{a_{m₁}}(x) ≥ 2C₊/c₋, i.e.
C₊(y + a_m)^{ϑ−1} ≤ c₋/(2y). With (TS-low), f(t^{(m)}) ≤ c₋/(2y) ≤ f(t^{(m₀)})/2, so W_m ≥ f(t^{(m₀)})/2 ≥ c₋/(2y) ≥ c_W.
*Limits.* For the nonnegative continuous function 𝓔 and weak convergence, ω(𝓔) ≤ liminf_jω_j(𝓔) (portmanteau): the
upper bounds pass, in the K-uniform form f(t^{(m)}) ≤ C₊(U₋(m₀) + a_m)^{ϑ−1} (use y ≥ U₋(m₀)). At t^{(m₀)}, (MOM-E)
gives uniform integrability, so ω_j(𝓔) → ω(𝓔) (𝓔 ∧ M is bounded continuous and 0 ≤ ω_j(𝓔) − ω_j(𝓔 ∧ M) ≤ M₂/M); hence
f_ω(t^{(m₀)}) ≥ c₋/x and W_m(ω) ≥ lim_jf_j(t^{(m₀)}) − liminf_jf_j(t^{(m)}) = limsup_jW_m(ω_j) ≥ c_W. Since a_m → ∞,
liminf_{t→0}f_ω(t) = 0 < c₋/x ≤ f_ω(t^{(m₀)}): (AF-W). ∎
(Arithmetic of (4.1)-(4.2) on worst-case data, with the threshold computed at y and the K-uniform form at x following
from the monotonicity of ψ proved above: hi55_b B1, with a designed-FAIL control showing m₁ is sharp.)

### 4.2 Theorem H-RED-sharp (one affine witness at moderate separation). PROVEN implication
*Inputs.* (F-flow) two-sided between levels j < n: β₋(n − j)log L − R_F ≤ u_j − u_n ≤ β₊(n − j)log L + R_F; and
**(SCH_u)** at k ∈ {j, n}: |A_sch/f(t_k) − u_k| ≤ C_sch with one constant A_sch > 0 and u_k − C_sch > 0.
*Conclusion.* If Δ := n − j satisfies β₋Δ log L > R_F + 2C_sch, then
  W_GF(t_j, t_n) = f(t_n) − f(t_j) ≥ A_sch(β₋Δ log L − R_F − 2C_sch)/((u_j + C_sch)(u_n + C_sch)) > 0.
*Proof.* v_k := A_sch/f(t_k) ∈ [u_k − C_sch, u_k + C_sch]; W = A_sch(v_j − v_n)/(v_jv_n), v_j − v_n ≥ (u_j − C_sch) −
(u_n + C_sch) ≥ β₋Δ log L − R_F − 2C_sch > 0, and v_jv_n ≤ (u_j + C_sch)(u_n + C_sch). ∎ (hi55_b B2 with a designed-FAIL
control at Δ₀ − 1.) (SCH_u) at all fine levels implies (TS) with c₋ = A_sch/2, C₊ = 2A_sch, ϑ = 0 when u_k ≥ 2C_sch.

### 4.3 Two auxiliary lemmas used in the branch reductions. PROVEN
**Lemma EV.** For U ∈ SU(N) with eigenphases θ_j ∈ (−π, π] and ‖log U‖²_HS := Σθ_j²:
  (2/(π²N))‖log U‖²_HS ≤ 1 − N^{−1}Re tr U ≤ ‖log U‖²_HS/(2N).
*Proof.* 1 − cos θ = 2sin²(θ/2), and (2/π)|x| ≤ |sin x| ≤ |x| on |x| ≤ π/2 (Jordan). Sum over j and divide by N. ∎
So any two-sided bound on ω(1 − P_{p,m}) is a two-sided bound on ω(Ψ_m) with constants changed by 2N and π²N/2.
**Lemma NA-lin (noise adds variance; linear chain).** Suppose the chain is generated forward as A_{k+1} = 𝒜A_k + ζ_k with
𝒜 linear and ζ_k centred, square integrable and independent of (A_0, ζ_0, …, ζ_{k−1}), A_0 having any law with finite
second moments. Then for every linear functional φ of the level-m field,
  E[φ(A_m)²] = E[φ(𝒜^mA_0)²] + Σ_{k<m}E[φ(𝒜^{m−1−k}ζ_k)²] ≥ E[φ(𝒜^mA_0)²].
*Proof.* A_m = 𝒜^mA_0 + Σ_{k<m}𝒜^{m−1−k}ζ_k; cross terms vanish by independence and centring. ∎
*Reading.* The deterministic (noise-free) block flux is dominated by the soft one, and the difference is a known
function of the kernel. This is the linear model of (NOISE-ADD) below; it also exhibits exactly the noise term that
makes soft witnesses fake (§2.8 (N5)).

### 4.4 The inputs, by branch (owner's labels; "NEW" = stated by no file read)
**Branch D — deterministic S4c block observable Ψ_m (bounded, strictly local, noise-free).** EXISTENCE §10.1 already
proves (conditionally) exactly (TS) for 1 − P_{p,m}:
  (δ_*/2)/(1/g² + β′m log L) ≤ ω(1 − P_{p,m}) ≤ φ(G_m),  G_m = (1/g² + βm log L)^{−1/2}   (Theorem X-NTAF),
uniformly in K and in the volume, for every limit point. With Lemma EV this is (TS-low) at every m and (TS-up) for every
ϑ > 0 (φ(G) = G²(p(G)²/(2N) + 2) with p a power of log(1/G), ≤ C_ϑG^{2−2ϑ}). (MOM) and (CONV) are automatic (bounded
continuous block generators; X-ALG). So in Branch D:
  **H_int ⇐ H-Bal-1 + H-loc-LF + H-sg** (EXISTENCE: X-NTAF ⇐ LAP-1 ⇐ [Theorem LF⇒3L] H-Bal-1 + H-loc-LF; upper half + H-sg)
  **+ (S4c-lin)** + Theorems H-RED, SEP (this file),
where **(S4c-lin)** [ARGUED here, not proven]: the linearisation of A^{K−m} at the trivial field, read at resolution m,
converges as the depth K − m → ∞ to a fixed self-similar smearing, so that the abelian realisation Ψ^{ab}_m := Σ_a(φ^a_m)²
of Ψ_m is a family of the form of Theorem KLM (with w ≢ 0 at large |v|, which Lemma UV-D's divergence step needs; true
for any nonzero compactly supported kernel since φ̂ is entire). Status of the three hypotheses: H-Bal-1 is Balaban's
coupling flow (SU(2); EXISTENCE: "proof deferred and unseen", IMPORTED-NOT-YET-REVERIFIED); H-loc-LF and H-sg are
EXISTENCE's HYPOTHESIS-NEW for the deterministic S4c variables (§11). **They are hard-scheme statements; the lane's soft
RG does not supply them.** I have not re-verified X-NTAF, LAP-1 or LF⇒3L; this item is CONDITIONAL on them as written.

**Branch S — the lane's soft RG; observable Ψ_m of the bare field (or 𝓔).**
| Input of H-RED | Route | Owner / status |
|---|---|---|
| (F-tune) | FLOW Theorems F-flow, F-tune | PROVEN-HERE there given (UNIV-1L) [OPEN], (SF-g), (RLF-δ), (SF-cont), (SF-∞); only β₋ > 0 and R_F < ∞ are used here |
| (TS-up) | soft upper half H-Bal-3T^S: ω(1 − P^S_{p,m}) ≤ φ(g^S_m) [EXISTENCE §13.6 ⇐ (RLF-3^dis), (PLD^mod_dis), (F)] + Lemma EV + **(NOISE-ADD)**: ω(Ψ_m) ≤ C_NA ω(‖log U_{K−m}(p)‖²_HS) + C′_NA g_{K−m}^{2−2ϑ} (deterministic A^{K−m}(U_0) against the soft U_{K−m} at the same level) + **(KER-fwd)**: the soft kernel is "deterministic average times noise independent of the past" | (RLF-3^dis), (PLD^mod_dis): HYPOTHESIS-NEW (EXISTENCE §13.4, §13.6); (NOISE-ADD): **NEW**, PROVEN only in the linear chain (Lemma NA-lin); (KER-fwd): **NEW**, a property of PROOF's S4′/D4-norm kernel to be checked (I have not checked it; if the kernel's centre is a non-unitary average, the noise is not independent of the past and Lemma NA-lin applies only after linearisation) |
| (TS-low) at one m₀ | **(ANTI-♭)**: ω(Ψ_{m₀}) ≥ c♭/u_{K−m₀} (Ψ_{m₀} built from A^{K−m₀}(U_0)), a one-point, one-scale lower bound for a noise-free block. Not obtainable from soft bounds: LAP^S is "kernel only" and EXISTENCE Corollary SEP (a) shows soft lower bounds hold for a free fine field. Routes: (α) Branch D's LAP-1 ⇐ H-loc-LF for S4c variables; (β) noise subtraction: by Lemma NA-lin, E[Ψ_det] = E[Ψ_soft] − 𝒩_m with 𝒩_m the exactly known noise term, and in the Gaussian part of the level effective action (EXISTENCE Lemma NT-G: the free soft chain at coupling g_j) E^G[Ψ_soft] − 𝒩_m = g_j²w_fine > 0; so (ANTI-♭) ⇐ **(W-AF2_r)**: a Gaussian comparison of the one-point soft block variance at one level to relative accuracy r < w_fine/(2(w_fine + w_noise)) [a fixed-r version of EXISTENCE's W-AF2 = H-corr], + nonlinear (NOISE-ADD), + large fields at that level of probability o(1) [(O3)/(LF-loc)] | **OPEN, NEW**; consumes (I_j^E)′′ items (a3-q), (a4), (a5) with relative accuracy r (not o(1)) |
| (MOM-E), (CONV-E) | automatic for Ψ (bounded); for 𝓔: part of H_reg plus **(FLOW-BLK)**: two-sided comparison of f(t^{(m)}) with ω(Ψ_m) with bounded constants; or **(SRC)**: transport of the bare flowed observable through every level below k(t) — EXISTENCE §19.5: "(I_k^E)′′ with an observable source … not stated by layer 1" | **OPEN, NEW** |

*Consequence for the work plan (ARGUED).* The soft scheme pays for "no auxiliary noise in the witness" with two new
inputs, (NOISE-ADD) and (ANTI-♭), which a hard (deterministic-averaging) scheme gets from its own block law. This is a
concrete datum for PLAN_S26 Step 3 ("decision 4, re-priced"): under decision 4 the non-free witness costs a noise
comparison that Balaban's scheme does not.

### 4.5 What the reduction does not need
No infrared input: no decay, clustering, uniqueness, gap, or control of scales coarser than t₀ beyond volume-uniform
one-point bounds. No two-point lower bound (unlike (WC), (H-sig^♭), SPEC-red). No small remainder (crude route). No
perturbative coefficient except the sign of the one-loop β coefficient, through β₋ > 0. No reflection positivity of the
Yang–Mills state (RP enters only as the defining property of the comparators), no rotation invariance, no
non-Gaussianity. Is any input H_int restated? (TS-low) is satisfied by every nontrivial comparator and only excludes
the trivial theory F ≡ 0. (TS-up) for any finite set of m is satisfied by free comparators with small e². What separates
is (TS-up) along infinitely many levels together with u_{K−m} → ∞ (β₋ > 0): the energy density in units of t^{−2}
tends to 0 in the ultraviolet — the vanishing bare charge, i.e. asymptotic freedom of an observable — which no
nontrivial member of 𝔊 has (Lemma UV-D). These are an upper bound and a flow statement, both standard UV-stability
content; neither is a lower bound on a separating quantity. The separating mechanism is proven here (Theorem SEP).

*Kernel check for (KER-fwd) (done after writing the table; recorded here, not edited into it).* PROOF.md, locating
string `K(V, U) := Π_c k_c` (L5 [S9]): k_c := exp(−(κ/g²)[1 − N^{−1}Re tr(V_c^{−1}M̄_c(U))])/𝒩(M̄_c(U)), with M̄_c(U) the
**mean over contours** of SU(N) transports — not unitary in general. Writing M̄_c = W_cP_c (polar form), the conditional
law of ζ := W_c^{−1}V_c has density ∝ exp((κ/(g²N))Re tr(ζ^{−1}P_c)), which depends on U through P_c. So **(KER-fwd)
fails exactly for the lane's kernel**: the noise is independent of the past only to leading order in small fields
(P_c = 1 − O(curvature²)). Lemma NA-lin therefore supplies (NOISE-ADD) only after linearisation; the correction is a
named part of the nonlinear (NOISE-ADD).

## 5. A second witness: the odd cubic W₃ (specified; YM side OPEN)
O₃(t,x) := t³·tr(G_μν[G_νρ, G_ρμ])(t,x) (summed; dimensionless; gauge invariant; C-even: under G ↦ −G^T,
tr(X[Y,Z]) ↦ −tr(X^T[Y^T,Z^T]) = tr(X[Y,Z]); P-even: each index occurs twice). Abelian realisation (tr T^a[T^b,T^c] =
−½f^{abc}): O₃^{ab} := −(t³/2)f^{abc}G^a_μνG^b_νρG^c_ρμ, G^a = K_t∗F^a. W₃(ω) := ω(O₃(t,0)).
- **Lemma W3-0. PROVEN.** For every law of (F^a) invariant under F ↦ −F — every centred Gaussian of any covariance (all of
  𝔉_free, every contact representative of any polynomial degree, every subtraction) and every C-invariant abelian theory —
  E[O₃^{ab}] = 0 (O₃^{ab} is cubic); hence W₃ = 0 on every mixture of such laws. No UV family is needed.
- **Limits.** (i) Point-supported *non-Gaussian* noise added independently (all its cumulants on the diagonal) leaves the
  separated-point Schwinger functions, hence the OS reconstruction, unchanged, but a nonzero diagonal third cumulant of
  f^{abc} type can make W₃ ≠ 0: W₃ is not robust under OS equivalence for non-Gaussian representatives (ARGUED; no
  O(4)-invariant Bianchi example constructed here). (ii) The Yang–Mills value is W₃ = c₃g⁴ + O(g⁶) with c₃ a tree-level
  two-loop flowed integral (three-gluon vertex plus flow and commutator nonlinearities). **c₃ is not computed here
  (OPEN).** EXISTENCE §21.2 reports a nonzero tree-level value 0.012827·N(N² − 1) for its lattice corner analogue (float
  sums, box-converged; not re-verified here) — suggestive only. (iii) Its reduction needs a **small** remainder,
  |W₃ − c₃g⁴| ≤ |c₃|g⁴/2 (cf. EXISTENCE (CE-cond^3) with (N2): 2r ≤ |c(t₀)|/8), strictly stronger than (TS).
- **Verdict (ARGUED).** W₃ is a useful second witness (it excludes every Gaussian abelian law without UV input), but its
  Yang–Mills side is harder than W_GF's. Recommend W_GF in the vanishing-charge form (1.2) as the H_int witness.

## 6. The existence lane against the bar (T4)
Located by string in `$E/EXISTENCE.md`; statuses are the lane's, re-derivations noted where done.
| Item | What it gives (as stated) | Meets the H_int bar? | Reusable? |
|---|---|---|---|
| Lemma DIFF (§19.1, `Lemma DIFF (the second difference is an RP form`) | C_F(0) − 2C_F(h) + C_F(2h) = OS norm of [D_h], blind to vacuum degeneracy | **No.** Excludes the vacuum-only theory, not a free one: the free massless field has a strictly positive value (PANEL_P1 §4 PROVEN; LO-D *is* that value). I re-derived (i)-(ii): D_h ∈ 𝔄_+, Cov(θD^*, D) = C(0) − 2C(h) + C(2h) ≥ 0 by RP, spectral form by [τ_aG] = e^{−aH}[G]. | As an OS-space tool only |
| Lemma LO-D (§19.2) | order-g⁴ Gaussian second difference > 0 | **No:** it is the free two-gluon value | The positivity computation pattern |
| (WC), Theorem NT-red (§17.3) | two-point lower bound on a fixed hypercubic torus, g ≤ g_W(𝕋) | **No:** a physically small box (EXISTENCE [RX8-fix 9]); not volume-uniform; a non-vacuum bound, not a non-free one | No |
| Theorem NT-pol, Cor. NT-pol^OS (§18) | O(1) Polyakov/toron correlation | **No:** tiny-torus zero modes (PANEL_P3 §5 names this case) | No |
| (H-sig^S), Theorem SIG-FREE, Prop. SIG-RED (§16) | dim H^S_ω > 1 for soft variables | **No:** soft variables; and dim H > 1 excludes vacuum-only, not free (SIG-FREE (ii): the free soft chain has it) | **Corollary SEP (a)** is reusable: it is the lane's own proof that soft one-point running is faked by kernel noise (§2.8 N5) |
| (H-sig^♭) (§16.4) | noise-free cross-plane two-point lower bound | **No:** non-vacuum, not non-free | Its noise-free framing is right; the needed lower bound is the much weaker one-point (ANTI-♭) |
| Theorems SPEC-red, SPEC-red^ms (§19.4, §20.2) | σ_F((0,∞)) ≥ u_+^{−2}A_*/2 for a soft block plaquette, given (CE-cond)/(CE-cond^ms), (MOM_4), (LF-loc) | **No:** non-vacuum weight; Gaussian limits not excluded (EXISTENCE [RX10-fix 7] says so); soft variables | **Yes, the architecture:** Lemma MK, Lemma MIX-cond, Theorem CB → (LF-loc), (MOM_4), tower property — the right tools for (TS-up), (ANTI-♭), (NOISE-ADD) |
| Theorems NG-red, NG-ax; Lemmas NG-wit, PO, AX (§20.4, §21.2) | an f^{abc}-odd corner one-point function, separated from sign-symmetric / axial-Gaussian laws | **Partly.** Affine (mixture-robust) and local, but built from soft variables: Lemma PO gives ¾N(N² − 1)σ⁴ ≠ 0 for i.i.d. Gaussian links, so the kernel noise (σ² ∝ g²/κ) can feed the witness at the signal's order g⁴ — a free fine field plus the lane's kernel is not in NG-ax's null class (ARGUED; not computed for the actual kernel). Its null class is gauge-defined, not "free theories" | Lemma REC (linear recursion across levels) and the odd-witness idea → W₃ (§5) with noise-free observables and the abelian null class |
| **Theorem X-NTAF, Cor. X-NTAF-AF** (§10.1, deterministic S4c branch) | (δ_*/2)/(1/g² + β′m log L) ≤ ω(1 − P_{p,m}) ≤ φ(G_m) → 0, uniformly in K and volume | **Yes, in substance.** Noise-free, local, bounded, volume-uniform. With Lemma EV it is (TS) for Ψ_m; with Theorems H-RED and SEP it gives H_int against conv(𝔊 ∪ 𝔖). Its own stated reach ("excludes massless free fields with canonical scaling and power-law approach") undersells it: KLM/UV-D make it exclude every free and every RP abelian comparator (≤ 1 subtraction) and all mixtures | **Yes** — CONDITIONAL on H-Bal-1, H-loc-LF, H-sg (hard-scheme hypotheses for S4c variables) and (S4c-lin); X-NTAF, LAP-1 and LF⇒3L not re-verified here |
| X-NTAF^S, LAP^S, H-Bal-3T^S (§13.6) | soft analogue | Lower half **No** (LAP^S "kernel only"; Cor. SEP (a)); upper half is genuine dynamics | Upper half → (TS-up) via (NOISE-ADD) |
| Theorem CB, Lemma CBE (§13.4) | volume-uniform local large-field bounds from disseminated ones (RP chessboard) | (tool) | **Yes**, also for the deterministic S4c variables (EXISTENCE notes the proof transfers with X-RP) |
| §21.3 consumer list | layer-1 interface names and owners' statuses | (tool) | **Yes** (used in §4.4) |
**Summary of T4.** Every non-triviality conclusion of the existence lane's soft branch (sessions 4-12) is either a
vacuum-only exclusion or a soft-variable statement, and fails the bar. The deterministic branch's X-NTAF (session 2),
which the lane stopped developing when it moved to soft variables, is the one result that already has the right form;
what it lacked was the comparator theorem (§2), now supplied.

**Codex review used.** CODEX_REVIEW_P4.md (read as on disk; it ends mid-sentence at "Proving a transparently tuned
version of that normaliz", so its last section is unfinished) says: "Non-freeness is not a closed property", a witness
must be "separated by a positive amount from its calibrated free Yang–Mills comparator, uniformly in both cutoff and
radius", and "A nonzero formal running coupling is not such a witness". **I agree with all three.** This file meets
them as follows: (1.2) is a closed condition (each W_m is continuous under (MOM)/(CONV)) separated by c_W from a class
that contains every calibration (all couplings, colour by colour); and the running enters only through constructive
inputs ((F-tune) and (TS)), never through a formal β-function.

## 7. Checks (criteria before scripts; plain Python Fractions; nice 10; single thread; no lock needed: ≤ 0.2 s each)
- **hi55_a** (`checks/hi55_a_criteria.md` 23:46:54 UTC, `hi55_a_comparator.py` 23:58:47, `hi55_a_out.txt`,
  `hi55_a_time.txt`; run 2026-10-28 23:58:56 UTC): **A1, A2, A3(a)-(e), A4 PASS; controls A1-F (all 25 momenta fail the flipped identity), A2-F
  (p²ΣD_μμ ∈ {3, 10/3, 4, 13/2, 13}), A3-F (ε_c = 0 gives W = 0 exactly) behave as registered.** A3(c) values
  F₁(8) − F₁(4) = 7/512 etc.; A3(d) F₁(1) − F₁(1/2) = −7/8 (the sign is not automatic); A4 = 3/128. Load-bearing for
  Lemma TR and Proposition CT.
- **hi55_b** (`hi55_b_criteria.md` 23:47:07 UTC, `hi55_b_reduction.py` 23:59:19, `hi55_b_out.txt`, `hi55_b_time.txt`;
  run 23:59:28 UTC): **B1 PASS** (300 parameter sets, ratios C₊/c₋ up to ~10⁶, ϑ (`theta` in the script) ∈ {0, ½}, m = m₁ … m₁ + 40, 0 violations);
  **B1-F behaves** (100/100 zero-slack sets fail at m₁ − 1: m₁ is sharp, the gate can fail); **B2 PASS** (900 checks,
  0 violations, the adversarial corner is the minimum every time); **B2-F behaves** (270/270 sets give W ≤ 0 at Δ₀ − 1).
  Load-bearing for the arithmetic of Theorems H-RED and H-RED-sharp (not for any YM input).
- **hi55_c** (`hi55_c_criteria.md` 23:47:29 UTC after a wording edit, before the script existed; `hi55_c_latfree.py`
  23:59:53, `hi55_c_out.txt`, `hi55_c_time.txt`; run 23:59:56 UTC): **C1, C2, C3 PASS (informational).** F_lat(1) = 1.836105·10⁻³ >
  F_lat(2) > … > F_lat(64) = 1.586245·10⁻³ (continuum 1/(64π²) = 1.583·10⁻³); increasing at τ ≤ 1/8; 64π²F_lat − 1 =
  3.929·10⁻³ and 1.959·10⁻³ at τ = 32, 64 (≈ 1/(8τ)). Not load-bearing.
- *Could the gates fail?* A1/A2 compute from definitions (A1-F shows a wrong formula fails); A3(c)/(d) test signs in both
  directions; B1/B2 use worst-case data with sharpness controls; C1/C2 test opposite monotonicity in two regimes.

## 8. Summary
### 8.1 Claims of this file
| # | Claim (locating string) | Label |
|---|---|---|
| 1 | Specification of 𝓔, 𝔈, 𝔊₀, 𝔊₁, 𝔉₀, 𝔉_free, 𝔖, W_GF, (AF-W), (1.2) (§1) | definition |
| 2 | Lemma TR (Gram form, trace 6p², ξ-independence) | PROVEN (+hi55_a) |
| 3 | f ≡ 3Σe_a²/(128π²) on 𝔉₀; W_GF = 0 on 𝔉₀ and its mixtures (§2.2) | PROVEN |
| 4 | Lemma SI: W_GF = 0 on 𝔖 (convex) | PROVEN; Gaussian-connection examples ARGUED |
| 5 | Theorem KLM (screening ⇒ non-increasing, any self-similar quadratic smearing) | PROVEN |
| 6 | Proposition CT (contact representatives of the free field have W_GF > 0; no finite family suffices) | PROVEN (+hi55_a) — refutes the naive "W_GF vanishes on every free theory" up to OS equivalence |
| 7 | Lemma UV-D (dichotomy on 𝔊₀ ∪ 𝔊₁) | PROVEN; K ≥ 2 subtractions ARGUED |
| 8 | Theorem SEP, Cor. SEP-1, SEP-2, SEP-3 | PROVEN |
| 9 | 𝔊 contains every RP abelian theory with ≤ 1 subtraction | CONDITIONAL on the imported Källén–Lehmann theorem |
| 10 | (N1)-(N3); Lemma BARE; (N5) soft witnesses faked by noise | PROVEN (N5 rests on EXISTENCE Cor. SEP (a), read; mechanism re-derived) |
| 11 | A_∞ = 3(N² − 1)/(128π²) | free-field value PROVEN (+hi55_a A4); its identification as Yang–Mills' O(g²) coefficient is standard perturbation theory (§9.2), not used by H-RED/SEP |
| 12 | W_GF = A_∞b₀ḡ⁴log(t₂/t₁) + O(ḡ⁶ log²) | ARGUED/IMPORTED (perturbative) |
| 13 | Theorems H-RED and H-RED′ (§9.1) | PROVEN implications (+hi55_b B1 for H-RED's arithmetic; H-RED′ is a one-line inequality); CONDITIONAL on (F-tune), (TS)/(TS′), (MOM-E), (CONV-E) |
| 14 | Theorem H-RED-sharp | PROVEN implication (+hi55_b B2) |
| 15 | Lemma EV; Lemma NA-lin | PROVEN |
| 16 | Branch D: H_int ⇐ H-Bal-1 + H-loc-LF + H-sg + (S4c-lin), via X-NTAF = (TS′) and H-RED′ | CONDITIONAL (X-NTAF not re-verified; (S4c-lin) ARGUED) |
| 17 | Branch S: new inputs (NOISE-ADD), (ANTI-♭)/(W-AF2_r), (FLOW-BLK)/(SRC) | OPEN, NEW |
| 18 | (KER-fwd) fails exactly for PROOF's kernel (`K(V, U) := Π_c k_c`) | PROVEN (direct reading of the kernel formula) |
| 19 | Lemma W3-0; W₃'s limits; c₃ | PROVEN; limit (i) ARGUED; c₃ OPEN |
| 20 | Lattice free comparator has the screening sign at τ ≥ 1 | informational (hi55_c) |
| 21 | Existence-lane verdicts (§6) | as tabulated; X-NTAF reusable (conditional), soft-branch non-triviality results fail the bar |

### 8.2 The reduction in one paragraph
H_int, specified as the uniform family (1.2) of affine finite-moment witnesses W_m = f(t^{(m₀)}) − f(t^{(m)}) of the
noise-free flowed energy density (or S4c block energy), holds in every limit state **if** (i) the coupling flow has the
asymptotically free sign with bounded error, β₋ > 0 and R_F < ∞ (FLOW F-tune, conditional on (UNIV-1L), (SF-g), (RLF-δ),
(SF-cont), (SF-∞)); (ii) the observable is two-sided comparable to the running coupling, c₋g_k² ≤ f(t_k) ≤ C₊g_k^{2−2ϑ},
with arbitrary constants, at one scale (lower) and at all finer scales (upper), uniformly in cutoff and volume; and
(iii) moment and convergence conditions that are part of H_reg (automatic for bounded block observables). The limit then
has vanishing bare charge, f(t) → 0 as t → 0 with f(t₀) > 0, and Theorem SEP (PROVEN) shows that no free abelian theory —
massless at any couplings, massive, generalised free, any OS-equivalent Euclidean representative with polynomial contact
terms — no scale-invariant state, no reflection-positive abelian theory (≤ 1 subtraction; KL imported), and no mixture of
these has that property. In the deterministic (hard-averaging) branch, (ii) is the existence lane's X-NTAF under H-Bal-1,
H-loc-LF, H-sg. In the soft branch, (ii)'s upper half needs a noise comparison (NOISE-ADD) on top of H-Bal-3T^S, and its
lower half needs a one-point, one-scale noise-free anti-concentration bound (ANTI-♭) that no soft-variable statement can
supply. No infrared input, no two-point bound and no small perturbative remainder is needed.

### 8.3 What this changes for PROOF.md and HANDOFF (recommendations to the lead; not edits)
1. H_int now has a precise specification ((1.2), §1) and a PROVEN comparator theorem (§2); the "invariant running-coupling
   property" PANEL_P3 §5 asked for exists in the form (AF-W). It should replace "non-triviality" items that are
   vacuum-only exclusions.
2. The single affine witness W_GF is **not** enough against OS-equivalent contact representatives (Proposition CT); the
   UV family is required. Any plan that tries to prove non-freeness at one or finitely many scales should be told so.
3. The existence lane's soft-branch non-triviality results (SIG-FREE/(H-sig^S), SPEC-red(^ms), (WC_∞^(sp)), NT-red,
   NT-pol, NG-red/NG-ax as stated) do not meet the H_int bar; X-NTAF (deterministic branch) does, conditionally.
4. For PLAN_S26 Step 3 (decision 4 re-priced): under the soft scheme the witness costs two inputs the hard scheme does
   not — (NOISE-ADD) and (ANTI-♭) — and the lane's kernel does not have independent multiplicative noise (§4.4 kernel
   check), so (NOISE-ADD) is genuinely nonlinear.
5. Smallest next artifacts: (a) (ANTI-♭) at one level via route (β) — a fixed-accuracy Gaussian comparison of one soft
   block variance (W-AF2_r); (b) nonlinear (NOISE-ADD) with the actual kernel; (c) (S4c-lin) (convergence of the
   linearised S4c tower), which is a linear-algebra statement.

## 9. Addenda (written after §8, 2026-10-29 ~00:05 UTC; appended, not edited into the sections they qualify)

### 9.1 Theorem H-RED′ (hypotheses in F-tune's K-uniform form). PROVEN implication
X-NTAF (Branch D) states its bounds with the flow's *bounds* in place of u_{K−m}, so §4.4's "this is (TS-low) at every m
and (TS-up)" should read "(TS′)". Define
  **(TS-low′)** f_{a,R}(t^{(m₀)}) ≥ c₋/U₊(m₀);   **(TS-up′)** f_{a,R}(t^{(m)}) ≤ C₊U₋(m)^{ϑ−1} for all m ≥ m₀,
uniformly as in §4.1, with U_±(m) = g^{−2} + β_±m log L ± R_F and U₋(m₀) > 0. (TS) implies (TS′) because
u_{K−m} ∈ [U₋(m), U₊(m)]. Let m₁′ ≥ m₀ be the least integer with U₋(m₁′)^{1−ϑ} ≥ 2C₊U₊(m₀)/c₋ (it exists: U₋(m) → ∞ since
β₋ > 0). Then for m ≥ m₁′: f(t^{(m)}) ≤ C₊U₋(m)^{ϑ−1} ≤ c₋/(2U₊(m₀)) ≤ f(t^{(m₀)})/2, so W_m ≥ c₋/(2U₊(m₀)) = c_W; the
limit statements and (AF-W) follow exactly as in §4.1 (only (MOM-E) at t^{(m₀)} and (CONV-E) are used). ∎ The threshold
m₁′ ≥ m₁ (it uses U₋(m) rather than u_{K−m₀} + a_m), so H-RED′ trades a larger separation for hypotheses that need no
knowledge of the actual u_{K−m}. With Lemma EV, X-NTAF supplies (TS′) for Ψ_m with c₋ = Nδ_*, U₊ from H-Bal-1's upper
bound, and C₊ = (π²N/2)C_ϑ.

### 9.2 Precision on §3.1's label
PROVEN there: the free-field value f = 3Σ_ae_a²/(128π²). That this is the O(g²) coefficient of Yang–Mills' f is the
standard tree-level statement of perturbation theory (only the Gaussian measure and the linear flow contribute at that
order) — IMPORTED/standard, not a constructive statement, and not used by Theorems H-RED/H-RED′/SEP.

### 9.3 Edit log (in-place changes made to earlier sections, for the reviewer)
1. §4.1, before any script ran (~23:56 UTC): the conclusion first said every limit point has "f_ω(t^{(m)}) ≤ c_W for all
   m ≥ m₁"; that does not follow (the lattice bound is c₋/(2y), y K-dependent). Replaced by the K-uniform bound
   f_ω(t^{(m)}) ≤ C₊(U₋(m₀) + a_m)^{ϑ−1} → 0 and the limsup argument for W_m(ω) ≥ c_W; the *Limits* paragraph was
   rewritten accordingly.
2. §4.5, same time: the "H_int restated?" paragraph was sharpened (it first said only the combination of (TS-up) at
   infinitely many levels with β₋ > 0 separates; it now also says (TS-low) excludes only F ≡ 0).
3. §2.8 (N4), ~00:01 UTC: a cross-reference "§8" corrected to "§7".
4. §2.8 (N5), ~00:02 UTC: "every witness built from soft variables fails the bar" weakened to the three cases actually
   proven by citation (X-NTAF^S, (H-sig^S), SPEC-red(^ms)), with the fine-coupling choice of each cited free model
   stated, and NG-red/NG-ax left ARGUED.
5. checks/hi55_c_criteria.md: one sentence reworded (definition of F_lat) before the script existed (file mtime
   23:47:29 UTC; script 23:59:53 UTC).
6. §7 and §8.1, ~00:08 UTC: §7's local file times replaced by the UTC mtimes, the script's `theta` named as ϑ; §8.1
   rows 11, 13, 16 refined to cite §9.1-§9.2 (H-RED′, the label of A_∞). No verdict changed.
7. §1.1, §4.4, ~00:12 UTC: Ψ_m was first called the plaquette of the "m-fold" S4c block field, inconsistent with
   m := K − k; corrected to resolution m, V^{(m)} = A^{K−m}(U) (EXISTENCE ES4), and the Branch-S rows and (S4c-lin) were
   re-indexed to match. No statement changed beyond the indexing.
No check verdict, number or threshold was changed after its output existed; items 4 and 6 narrowed or re-labelled
claims that do not rest on any check.

### 9.4 How (1.2) meets each clause of the bar (PANEL_P1 §3 item 4; PANEL_P2 S4; PANEL_P3 §5; CODEX_REVIEW_P4)
| Clause | Where met |
|---|---|
| specified, continuous, finite-moment | each W_m is a difference of two one-point functions of 𝓔 (or Ψ_m); continuous under (MOM-E)/(CONV-E), automatic for the bounded Ψ_m |
| vanishes on a named class of free theories | W_m = 0 on 𝔖 ⊃ conv(𝔉₀) (Lemma SI, §2.2); W_m ≤ 0 on conv(𝔊₀^{≤0} ∪ 𝔖) (Cor. SEP-2); the family excludes conv(𝔊 ∪ 𝔖) (Theorem SEP) |
| mixtures | affine witness + Fatou (Theorem SEP); no clustering used |
| composites of a Gaussian (Y = X² − 1) | irrelevant: the witness is a one-point function of the composite, compared with the same composite of every comparator, not a cumulant |
| bounded away from zero at fixed renormalised coupling, uniformly in volume | Theorem H-RED / H-RED′ (CONDITIONAL on (F-tune), (TS)/(TS′), (MOM-E), (CONV-E)); constants independent of K and the torus |
| local | Ψ_m strictly local (S4c); 𝓔 quasi-local at scale √t; the separating end of the family is the ultraviolet one |
| survives the OS quotient | one-point functions are OS data ⟨Ω, [·]⟩; the separation holds over whole OS-equivalence classes (Remark 1.3 (i), Proposition CT, Cor. SEP-1) |
| no auxiliary soft noise | bare-field observables only; Lemma BARE (kernel-independent); §2.8 (N5) shows why soft observables fail |
| survives averaging (rank-3 routes) | Cor. SEP-3 |
| non-freeness is not a closed property (CODEX_REVIEW_P4) | (1.2) is a closed condition separated by c_W from a class containing every calibration |

### 9.5 Branch S dependency chain down to layer-1 clauses (from EXISTENCE §21.3 rows B-C; owners' statuses, not re-verified)
- **(F-tune)** ⇐ FLOW F-flow/F-tune ⇐ (UNIV-1L) [⇐ Theorem UNIV ⇐ (U-IR) **OPEN**, (U-loc)] + (SF-g) + (RLF-δ)_k + (SF-cont)
  + (SF-∞). Used only through β₋ > 0 and R_F < ∞.
- **(TS-up)** ⇐ H-Bal-3T^S [EXISTENCE §13.6] ⇐ (RLF-3^dis) [⇐ RLARGE (RLF-3) per history in (H-w) form + HIST-sum + (RLF-1),
  (RLF-4), K8 normalisation; (H-w) **OPEN**] + (PLD^mod_dis) [HYPOTHESIS-NEW, only its free analogue proven] + (F);
  then **(NOISE-ADD)** [NEW; linear case = Lemma NA-lin; nonlinear case needs the polar factor P_c of the kernel centre,
  §4.4 kernel check].
- **(TS-low)** ⇐ **(ANTI-♭)** [NEW] ⇐ (route β) **(W-AF2_r)** [NEW: one soft block variance at one level within relative
  accuracy r of its Gaussian (Lemma NT-G) value], which consumes (I_j^E)′′ items (a3-q), (a4), (a5) [HYPOTHESIS [P];
  (a5-G♯) ⇐ **BFT-5** + (G♯-patch) — the B-NA wall; (a5-U) ⇐ **BFT-0**] and large fields of probability o(1) at that level
  [(O3): branch (i) PROVEN, (ii) ⇐ (SG^fl)_k, (iii) ⇐ CLS-sf ⇐ (AE) **OPEN**], plus nonlinear (NOISE-ADD).
- **(MOM-E), (CONV-E)**: automatic for the bounded Ψ_m; for 𝓔, H_reg plus (FLOW-BLK) or (SRC).
So the BFT clauses enter H_int only through (TS-low)'s route β, at **one** level and at a **fixed** relative accuracy r —
not through any all-scale or small-remainder statement. A route avoiding BFT-5 for (TS-low) would be route α (an
H-loc-LF-type local density bound for the S4c variables of the Wilson measure).

### 9.6 The error size of §3.3 in continuum-perturbation-theory language. PROVEN (elementary)
If |f(t) − A_∞ḡ²(t)| ≤ Cḡ⁴(t) for every t in a window with Cḡ² ≤ A_∞/2, put v := A_∞/f. Then f = A_∞ḡ²(1 + δ) with
|δ| ≤ (C/A_∞)ḡ² ≤ ½, so |v − 1/ḡ²| = (1/ḡ²)|δ|/(1 + δ) ≤ 2C/A_∞ =: C_sch, and the argument of Theorem H-RED-sharp gives
W_GF(t₁, t₂) > 0 as soon as 1/ḡ²(t₁) − 1/ḡ²(t₂) > 4C/A_∞; at one loop (d(1/ḡ²)/d ln t = −b₀) this is
log(t₂/t₁) > 4C/(A_∞b₀). So an O(ḡ⁴) remainder with **any finite** coefficient C is tolerated at a separation fixed by C;
it need not be small. (Illustration only, [m]: with C ≈ A_∞k₁ and Lüscher's k₁ ≈ 1.1 for SU(3), log(t₂/t₁) ≳ 4k₁/b₀ ≈ 63.
If the remainder is a smooth function of ḡ alone, as in perturbation theory, it cancels at this order and no such
separation is needed; the bound above is for an arbitrary bounded remainder.)
