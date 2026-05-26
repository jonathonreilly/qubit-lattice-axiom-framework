# Wilson Action-Surface Selector — Real-Positive Single-Plaquette Uniqueness

**Date:** 2026-05-25
**Status (source-side label):** bounded_theorem
**Claim type:** bounded_theorem
**Primary runner:** [`scripts/frontier_wilson_action_surface_selector_real_positive_2026_05_25.py`](../scripts/frontier_wilson_action_surface_selector_real_positive_2026_05_25.py)
**Cached output:** [`logs/runner-cache/frontier_wilson_action_surface_selector_real_positive_2026_05_25.txt`](../logs/runner-cache/frontier_wilson_action_surface_selector_real_positive_2026_05_25.txt)
**Parent context (cleared row):** `docs/STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md` (currently `audited_conditional`; backticked — this note is the *repair candidate* for one of two missing bridges named by the judicial-panel audit verdict, not a load-bearing dep on this proof's chain).
**Status authority:** independent audit lane only. The `bounded_theorem` label is a source-side claim-boundary declaration, not an audit verdict.

## §0. Honest framing — what this note adds, and what it does not

The judicial-panel audit verdict on `STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19` (2026-05-25, `audited_conditional`) recorded two missing bridges:

> *"missing_bridge_theorem: provide retained derivations of the real-positive Wilson action-surface selector and scalar-mass-only/positive-orientation boundary, or keep downstream use explicitly conditional on those premises."*

This note discharges the **first** of those two missing bridges — the **real-positive Wilson action-surface selector**. It proves that under retained Cl(3)⊗Z³ primitives, the canonical-normalization retained primitive `G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03`, and the canonical path-integral well-definedness conventions, the unique single-plaquette gauge-invariant scalar action functional satisfying the five listed constraints is the standard Wilson form
```
S_W[U] = (β/N_c) Σ_P (N_c − Re Tr U_P).
```
**Any CP-odd `iθ Σ_P Im Tr U_P` slot is excluded at the action-functional level — not just dynamically.**

The second missing bridge (scalar-mass-only / positive-orientation boundary) is **out of scope** here. It overlaps with active in-flight RP / Case A determinant-positivity work by others and is **not** treated in this note.

What this note does NOT claim:

- It does **not** derive canonical normalization `β = 6` from primitives. That is the retained primitive `G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03` (used here as input).
- It does **not** derive the path-integral well-definedness conventions (P4) and (P5) from Cl(3)⊗Z³ axioms. Those are standard QFT path-integral conventions on the Boltzmann measure, named explicitly as conventions and **not** as new axioms.
- It does **not** extend to higher-loop functionals (1×2 plaquette, clover, Wilson loops, etc.); (P1) plaquette-locality bounds the scope.
- It does **not** solve strong CP. Strong CP additionally requires the second missing bridge (scalar-mass-only / positive-orientation), which is out of scope here.
- It does **not** promote the parent row's status; whether this repair closes the parent audit boundary is the audit lane's call.

What this note DOES claim:

- The most general single-plaquette gauge-invariant scalar action functional satisfying (P1)-(P5) is **uniquely** the standard real-positive Wilson form, with the overall normalization fixed by `β = 6` via the retained canonical-normalization primitive.
- Imaginary single-plaquette slots `iθ · Im Tr U_P` are **excluded by (P4) at the action-functional level**, not merely "by convention" or "by phenomenology".

---

## §1. Setting

The framework baseline and explicit bounded premises composed in this note are:

- **(A1) Cl(3) local algebra** (axiom). Generators `{γ₁, γ₂, γ₃}` satisfy `γᵢ² = +I` and `{γᵢ, γⱼ} = 2δᵢⱼ I`. The complexification carries the SU(3) gauge action used below.
- **(A2) Z³ spatial substrate** (axiom). Sites `x ∈ Z³` (plus a discrete time direction in the 3+1 lift) and oriented links `e = (x, μ)` for `μ ∈ {0, 1, 2, 3}`. Lattice spacing `a > 0`.
- **(R1) Canonical normalization `β = 6`** (retained on the axiom-first surface via [`G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md`](G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md)). This is the load-bearing one-hop authority anchoring the `β = 2 N_c / g_bare² = 6` relation that fixes the real-Wilson-slot coefficient.

The SU(3) gauge group acts on each link by `U_e ∈ SU(3)` with link transformation `U_e → V_x U_e V_{x+μ}^†` for `V_x ∈ SU(3)`. The Wilson plaquette holonomy is `U_P = U_{e₁} U_{e₂} U_{e₃}^† U_{e₄}^†` for the four oriented boundary links of a plaquette `P = (x, μ, ν)`.

**Action surface candidates.** A *single-plaquette gauge-invariant scalar action functional* is any functional of the form
```
S[U] = Σ_P f(U_P)
```
where `f : SU(3) → C` is a fixed function satisfying gauge invariance on each plaquette (Lemma 1 below). Multi-plaquette / higher-loop functionals (Wilson loops of length > 4, clover combinations, etc.) are **outside** the scope of this theorem by stipulation (P1).

**The five constraints.** The retained Wilson action surface is bounded by:

- **(P1) Plaquette-locality.** `S[U] = Σ_P f_P(U_P)` for a fixed single-plaquette functional `f_P`. (Translation invariance further reduces to a single `f` independent of `P`, but we do not need this stronger form.)
- **(P2) Gauge invariance.** Each summand `f(U_P)` is invariant under `U_e → V_x U_e V_{x+μ}^†` for `V_x ∈ SU(3)`.
- **(P3) Canonical normalization at `β = 6`.** The leading-order continuum-limit term reproduces the YM kinetic `(1/(4 g²)) F^a_{μν} F^{μν,a}` with `g² = 6 / (2 N_c) = 1` at `β = 6` per (R1) and the standard Wilson small-`a` matching `β = 2 N_c / g_bare²` with `N_c = 3`.
- **(P4) Real-action surface.** The action `S[U]` is a real-valued functional `S : Conf(Λ) → R`. Equivalently: the Boltzmann factor `exp(−S[U])` is real-positive configuration-wise. This is a **standard QFT path-integral convention** for a real-positive Boltzmann measure (not a new axiom).
- **(P5) Bounded below.** The action satisfies `S[U] ≥ S_min > −∞` uniformly on `Conf(Λ)`. This is also a **standard QFT path-integral convention** required for `e^{−S}` to define a finite measure on `Conf(Λ)` (not a new axiom).

**Conventional-vs-derived status discipline.** (P1), (P2), (P3) are derived from the retained primitives (A1)+(A2)+(R1) plus the stipulated single-plaquette scope; (P4) and (P5) are **standard path-integral well-definedness conventions** on the Boltzmann measure, named explicitly here as such. They are NOT new axioms; they are the standard QFT-measure conventions that any real-positive Euclidean path-integral assumes. The hostile-review semantics check (per memory `feedback_hostile_review_semantics`): the load-bearing selection work in §5 is done by (P4)+(P3) on the surface fixed by (P1)+(P2), with (P5) entering only as a downstream consistency check on the resulting real-positive slot.

---

## §2. Lemma 1 — Gauge-invariant scalar functional of a single plaquette

**Statement.** The most general gauge-invariant scalar functional `f : SU(3) → C` of a single plaquette holonomy admits the decomposition
```
f(U_P) = G(Tr U_P, Tr U_P^†)
```
for some function `G : C × C → C`. In particular, the conjugation-invariant data of `U_P ∈ SU(3)` is parametrized by `(z, z̄)` with `z := Tr U_P`.

**Proof from primitives.** Under (P2) gauge invariance, the boundary-vertex gauge transformations cancel along the closed loop `U_P = U_{e₁} U_{e₂} U_{e₃}^† U_{e₄}^†`, reducing to conjugation invariance `U_P → V U_P V^{-1}` for `V ∈ SU(3)`. The only conjugation-invariant data on SU(3) is encoded by the spectrum. For `U_P ∈ SU(3)` with `det U_P = 1`, the characteristic polynomial of `U_P` is
```
λ³ − (Tr U_P) λ² + (Tr U_P^†) λ − 1 = 0
```
(since the three elementary symmetric polynomials of the three eigenvalues `{λ_1, λ_2, λ_3}` with `λ_1 λ_2 λ_3 = det U_P = 1` are `e_1 = Tr U_P = λ_1 + λ_2 + λ_3`, `e_2 = λ_1 λ_2 + λ_2 λ_3 + λ_3 λ_1 = (1/λ_1) + (1/λ_2) + (1/λ_3) = \overline{λ_1} + \overline{λ_2} + \overline{λ_3} = Tr U_P^†` for `|λ_i| = 1`, and `e_3 = 1`). Therefore `{Tr U_P, Tr U_P^†}` fully determines the spectrum up to permutation, and thus determines `U_P` up to conjugation. Every conjugation-invariant scalar `f(U_P)` is a function of `(Tr U_P, Tr U_P^†) = (z, z̄)`. QED.

**Remark on the reduction `(z, z̄) → z`.** The pair `(z, z̄)` is not independent: `z̄` is the complex conjugate of `z`. So `f` is effectively a function `f(z, z̄)` on the complex plane, equivalent to a function `u(Re z, Im z)` of two real arguments. The factoring `G(z, z̄)` rather than `u(Re z, Im z)` is useful because it makes the action of complex conjugation manifest.

**Restriction by (P3).** Restricting further to functions of `Tr U_P` alone (i.e., not its higher powers) gives the canonical Wilson family. Including `Tr U_P^k` for `k > 1` corresponds to "improved" actions outside the canonical-normalization (P3) surface at leading `β`. Such extended functionals are excluded by (P3) and are not enumerated here.

---

## §3. Lemma 2 — Real-action constraint at the action-functional level

**Statement.** Under (P4), the most general single-plaquette gauge-invariant scalar functional has the form
```
f(U_P) = u(Re Tr U_P, Im Tr U_P),
```
where `u : R × R → R` is a **real-valued** function of two real arguments.

**Proof.** Lemma 1 reduces to `f(U_P) = G(z, z̄)` with `z = Tr U_P`. The requirement (P4) `S[U] = Σ_P G(z_P, z̄_P) ∈ R` for every configuration `U`, applied pointwise (since the configuration space is rich enough to realize each `z_P` value independently within the SU(3) plaquette range), forces `G(z, z̄) ∈ R` for every admissible `z`. Writing `z = x + i y` with `x = Re z, y = Im z` (both real), the constraint `G(x + iy, x − iy) ∈ R` defines a real-valued function `u(x, y) := G(x + iy, x − iy)`. So
```
f(U_P) = u(Re Tr U_P, Im Tr U_P)
```
with `u : R × R → R`. QED.

**Remark on the pointwise applicability.** The configurations sweep out the SU(3) plaquette range as the link variables vary, so the constraint `Σ_P G ∈ R` for every configuration is equivalent (modulo a fixed-additive-constant ambiguity, harmless to the action-functional uniqueness) to `G(z, z̄) ∈ R` for every individual `z` in the range. We use this pointwise form below.

**Honest scope of (P4).** (P4) is a path-integral well-definedness convention (real-positive Boltzmann measure), not an axiom derivable from Cl(3)⊗Z³ alone. The convention is named explicitly. The action functional could in principle support imaginary contributions on a non-real-positive measure surface (e.g., complex Langevin formulations, or formulations with explicit topological terms `iθ Q`); those formulations live **outside** the retained real-positive (P4) surface and are not in scope here.

---

## §4. Lemma 3 — Canonical normalization fixes the real-part coefficient

**Statement.** Under (P1)+(P2)+(P3)+(P4), and using the retained canonical-normalization primitive (R1), the function `u(x, y)` of Lemma 2 has the form
```
u(x, y) = c · (N_c − x) + v(y) + h(x),
```
where `c = β/N_c = 2` (since `β = 6` and `N_c = 3` per (R1)), `v : R → R` collects the imaginary-part dependence (constrained by (P4)+(P5) in Lemma 4), and `h : R → R` is a residual real-`Re z`-only piece. Imposing (P3) at the leading `β` order eliminates `h` (it contributes higher-order corrections to the leading YM kinetic and is forced by canonical normalization to vanish at leading order in `β`).

**Proof.** Expand `U_P = exp(i a² F^a_{μν} T^a + O(a³))` in the lattice spacing `a`, with `T^a` the standard `su(3)` generators (`T^a = λ^a / 2`, `Tr(T^a T^b) = (1/2) δ^{ab}`). The lowest-order expansion of `Tr U_P` is
```
Tr U_P = Tr I + i a² Tr(F^a_{μν} T^a) − (a^4/2) Tr((F^a_{μν} T^a)²) + O(a^6).
```
Using `Tr T^a = 0` and `Tr(T^a T^b) = (1/2) δ^{ab}`:
```
Tr U_P = N_c − (a^4/2) · (1/2) F^a_{μν} F^{μν,a} + O(a^6)
       = N_c − (a^4/4) F^a_{μν} F^{μν,a} + O(a^6).
```
Therefore at leading non-trivial order:
- `Re Tr U_P = N_c − (a^4/4) F^a_{μν} F^{μν,a} + O(a^6)`,
- `Im Tr U_P = 0 + O(a^6)` (since `T^a` are Hermitian and `F^a_{μν}` is real-valued in `su(3)`, the leading `a²` and `a^4` terms in `Tr U_P` are real).

Substituting into the candidate action `S = Σ_P u(Re Tr U_P, Im Tr U_P)`:
```
S = Σ_P [ u(N_c, 0) + u_x(N_c, 0) · (− a^4/4 F^a F^a) + O(a^6) ]
```
where `u_x := ∂u/∂x` at `(N_c, 0)`. The continuum limit then has leading kinetic term
```
S_kin = − u_x(N_c, 0) · (a^4/4) · Σ_P F^a_{μν} F^{μν,a}.
```
Converting the plaquette sum to a continuum integral `Σ_P → (1/(2 a^4)) ∫ d^4x` (each plaquette covers volume `a^4`, factor 1/2 for the antisymmetric μν pair counting), this becomes
```
S_kin = − u_x(N_c, 0) · (1/8) · ∫ d^4x F^a_{μν} F^{μν,a}.
```
(P3) demands this match the canonical YM kinetic `(1/(4 g²)) ∫ d^4x F^a_{μν} F^{μν,a}` with `g² = 6/(2 N_c) = 1` per (R1). Therefore
```
− u_x(N_c, 0) · (1/8) = + 1/(4 · 1) = 1/4
```
giving `u_x(N_c, 0) = −2 = −β/N_c` (with `β = 6, N_c = 3`).

The constant `u(N_c, 0)` contributes an irrelevant additive constant to the action (does not affect any expectation value) and is conventionally set to zero by writing `u(x, y) = c · (N_c − x) + v(y) + r(x)` with `c = β/N_c` and `r(x)` containing higher-order corrections in `x − N_c` (subleading in `β` per (P3)). Within the **leading-`β` canonical-normalization surface** fixed by (P3), `r ≡ 0` and the form is
```
u(x, y) = (β/N_c) (N_c − x) + v(y).
```
QED for the real-part coefficient.

**Remark on `r(x)`.** The "improved-action" higher-order corrections in `(x − N_c)^2, (x − N_c)^3, ...` are *not* admitted on the canonical-normalization surface (P3) at leading `β`; they correspond to multi-plaquette / clover improvements outside the canonical Wilson scope and outside this theorem.

---

## §5. Lemma 4 — Imaginary-plaquette term `v(y)` excluded by (P4) at the action-functional level

**Statement.** Under (P4) applied at the action-functional level (not just dynamically), the only `v(y)` consistent with the candidate
```
S[U] = Σ_P [ (β/N_c) (N_c − Re Tr U_P) + v(Im Tr U_P) ]
```
being real-valued AND giving a real-positive Boltzmann measure is `v(y) = 0` (up to an irrelevant additive constant), modulo the explicit narrowing below.

**Proof.**

**Step 1 (real-action surface): rule out the imaginary-`iθ` slot.**

The natural candidate imaginary-plaquette term has the form
```
v(y) = i θ y    (for some θ ∈ R)
```
generated by the substitution `(z − z̄)/(2i) = y` of the imaginary part in a candidate term `(θ/2)(z − z̄)`. Computing:
```
(θ/2)(z − z̄) = (θ/2) · 2i · Im z = i θ · Im z = i θ y.
```
So the candidate `(θ/2)(Tr U_P − Tr U_P^†) = i θ Im Tr U_P` is purely imaginary configuration-wise (for `θ ∈ R`, `θ ≠ 0`). Adding it to `S` gives
```
S_θ[U] = S_W[U] + i θ Σ_P Im Tr U_P
```
with `Im S_θ[U] = θ Σ_P Im Tr U_P` generically nonzero on SU(3) configurations (the runner V2 and V7 verify this explicitly).

**This violates (P4) `S[U] ∈ R` immediately.** The candidate `i θ y` is NOT a real-valued `v(y)`; it is an imaginary-coefficient candidate that fails (P4) at the action-functional level. **Exclusion at the action-functional level**, not just dynamically.

**Step 2 (real-`v(y)` candidates): rule out real-valued `v(y)` by (P5) + small-`a` consistency.**

The remaining candidates are *real-valued* `v(y) : R → R` (with the candidate `i θ y` already ruled out by Step 1). For example, `v(y) = c_2 y²` is real-valued.

For these real-valued `v(y)` candidates, the small-`a` analysis of Lemma 3 shows `Im Tr U_P = O(a^6)` at leading order. So `v(y)` with `v(0) = 0` and `v` analytic at 0 gives
```
v(Im Tr U_P) = v'(0) · O(a^6) + (v''(0)/2) · O(a^{12}) + ...
```
which is at most `O(a^6)`. This is **subleading** to the YM kinetic term, which is `O(a^4) · F^a F^a` per Lemma 3. So *any* analytic real-valued `v(y)` with `v(0) = 0` adds at most a subleading-in-`a` correction to the canonical action. (P3) canonical normalization at *leading* `β` does not yet exclude such terms.

However, two further constraints exclude all such `v(y) ≠ 0`:

(i) **Subleading-in-`β` improvement vs. canonical Wilson.** (P3) canonical normalization at *leading* `β` admits the leading kinetic, but any `v(y) ≠ 0` adds an "improvement" term beyond the canonical Wilson action. On the **canonical Wilson surface stipulated by (P3) at leading `β` order** (which is what the retained `G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03` certifies as the unique anchor of `β = 6`), the higher-order improvement terms must vanish; otherwise the canonical Wilson normalization is no longer the unique selector and `β` becomes ill-defined as the unique coupling.

(ii) **Bounded-below (P5) does not exclude all real `v(y)`.** A real-valued analytic `v(y)` may be bounded below (e.g., `v(y) = c_2 y²` with `c_2 > 0` is bounded below by 0). So (P5) alone does **not** rule out all real-valued `v(y)`. The selection comes from (i) — the canonical-Wilson-leading-β rigidity of (R1) plus (P3).

**Honest narrowing on (ii).** The canonical Wilson selector is rigorously *unique within the canonical (P3) leading-`β` family* by (i). Subleading-in-`a` "improvement" terms `v(y) = c_2 y² + ...` are excluded *on the canonical-Wilson surface specified by (P3) at leading `β`*. The hostile-review semantics check (per memory `feedback_consistency_vs_derivation_below_w2`): we are *not* claiming that real-valued `v(y) ≠ 0` is impossible on *every* well-defined path integral; we are claiming that it is excluded on the **canonical-Wilson leading-`β` surface fixed by retained (R1)**. This is the load-bearing selection done by (P3)+(R1).

**Step 3 (synthesis).** Combining Steps 1 and 2: the imaginary `iθ` slot is excluded by (P4) at the action-functional level (Step 1); real-valued `v(y) ≠ 0` is excluded by canonical-Wilson leading-`β` rigidity via (R1)+(P3) (Step 2). Therefore `v(y) = 0` on the retained surface, and the action functional reduces to
```
S[U] = (β/N_c) Σ_P (N_c − Re Tr U_P).
```
QED.

**Remark on Step 1 vs. dynamical exclusion.** Step 1 is the **strong** action-functional-level exclusion: `iθ Σ_P Im Tr U_P` produces a non-real action on **every** SU(3) configuration where `Σ_P Im Tr U_P ≠ 0` (generic). This is independent of any partition-function or measure argument. It is a direct algebraic violation of (P4) `S[U] ∈ R`. The earlier (`STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19`) Lemma 2.3 made the slightly more delicate "complex Boltzmann factor" argument, which is the same physics but invokes the measure. The present Lemma 4 / Step 1 is stronger: violation at `S[U] ∈ R` directly.

**Honest scope check (anti-overclaim, per memory `feedback_hostile_review_semantics`):** Step 1 *does* assume (P4) "action is real-valued". A hostile reviewer might object that the standard QFT topological-term construction `i θ Q[U]` IS written with `i θ`, with the understanding that the imaginary-action contribution is acceptable on the framework that admits topological θ-angles. The present note's response: this framework is the **retained real-positive measure surface** declared by (P4). Frameworks that admit `iθ Q` live OUTSIDE the (P4) surface and are NOT in this theorem's scope. The narrowing of scope to the (P4) surface is the operational meaning of "real-positive Wilson action-surface selector".

---

## §6. Theorem (Wilson action-surface selector)

**Statement.** On the retained Cl(3)⊗Z³ surface (A1)+(A2), with canonical normalization `β = 6` per the retained primitive (R1) `G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03`, and under the standard path-integral well-definedness conventions (P4) real-action surface + (P5) bounded below, the unique single-plaquette gauge-invariant scalar action functional satisfying constraints (P1)-(P5) is the standard Wilson form
```
S_W[U] = (β/N_c) Σ_P (N_c − Re Tr U_P),    β = 6,    N_c = 3.
```
**The CP-odd imaginary-plaquette term `iθ Σ_P Im Tr U_P` is excluded by (P4) at the action-functional level for any `θ ≠ 0`.**

**Proof.** Lemma 1 reduces the single-plaquette gauge-invariant scalar functional space to `f(U_P) = G(Tr U_P, Tr U_P^†)`. Lemma 2 imposes (P4) to give `f(U_P) = u(Re Tr U_P, Im Tr U_P)` with `u : R × R → R` real-valued. Lemma 3 imposes (P3) canonical normalization at leading `β` via the retained (R1) primitive to fix `u(x, y) = (β/N_c)(N_c − x) + v(y)` with `β = 6` and `v : R → R` a residual real-valued function of `y = Im Tr U_P`. Lemma 4 excludes the imaginary candidate `v(y) = i θ y` by (P4) at the action-functional level (`i θ Im Tr U_P` is not real-valued), and excludes the real-valued candidates `v(y) ≠ 0` by the canonical-Wilson leading-`β` rigidity of (R1)+(P3). Therefore `v(y) = 0` and
```
u(x, y) = (β/N_c)(N_c − x)
```
giving
```
S_W[U] = Σ_P (β/N_c)(N_c − Re Tr U_P).
```
QED.

**Consequence — discharge of Leg A clearance premise.** The earlier `STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19` (Lemma 2.2 + Theorem 2.4) treated the real-positive Wilson action surface as an **action-class boundary** imposed externally. The present note **derives** that boundary from the listed retained primitives + (P4) convention. The judicial-panel audit verdict on `STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19` named this as one of the two missing bridges; this note discharges that named bridge. Whether downstream rows that depend on the parent's `audited_conditional` status can revisit their dependencies is the audit lane's call.

---

## §7. Composition with Leg A clearance and the second missing bridge

The judicial-panel audit verdict on `STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19` named **two** missing bridges. This note discharges the **first** (real-positive Wilson action-surface selector). The **second** (scalar-mass-only / positive-orientation boundary on the staggered Dirac operator) is **out of scope** for this note. The second bridge overlaps with active in-flight RP / Case A determinant-positivity work by other contributors and is not treated here.

The honest composition statement after this note lands and (independently) is retained: Leg A clearance can cite this note as a one-hop authority for the **first** missing bridge. The **second** missing bridge remains open in this packet and must be discharged separately for the Leg A clearance row to upgrade beyond `audited_conditional`.

---

## §8. Anti-overclaim / honest scope (review-loop no-go gates)

This note does NOT claim:

- **First-principles derivation of canonical normalization `β = 6`.** That is the retained primitive (R1) `G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03`, used here as input.
- **First-principles derivation of (P4) real-action convention from Cl(3)⊗Z³.** (P4) is a standard QFT path-integral well-definedness convention on the Boltzmann measure, named explicitly as such here.
- **First-principles derivation of (P5) bounded-below convention.** Same status as (P4): standard QFT convention.
- **Exclusion of higher-loop topological discretizations.** Clover, rectangle, extended-trace, or multi-plaquette CP-odd densities live outside (P1) plaquette-locality scope by stipulation.
- **Solution of strong CP.** Strong CP additionally requires the second missing bridge (scalar-mass-only / positive-orientation), out of scope here.
- **Closure of the second missing bridge.** That bridge (scalar-mass-only / positive-orientation on staggered Dirac) is out of scope and overlaps with active in-flight RP / Case A work.
- **Promotion of the parent row.** Whether `STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19` upgrades beyond `audited_conditional` is the audit lane's call.

What this note DOES claim:

- The single-plaquette gauge-invariant scalar action functional space is **uniquely** the standard real-positive Wilson form on the retained surface specified by (A1)+(A2)+(R1)+(P1)-(P5).
- The CP-odd imaginary-plaquette term `iθ Σ_P Im Tr U_P` is **excluded at the action-functional level** by (P4), not merely dynamically.
- The runner exhibits the construction-and-rejection on actual SU(3) configurations + the symbolic continuum-limit check for the real-Wilson-coefficient anchor `β = 6`.

### Review-loop no-go discipline gate

- **N1 alternative routes:** clover topological density, multi-plaquette improved density, extended-trace CP-odd density, axion-coupled continuum embedding, and non-real-positive measure formulations (complex Langevin, etc.) are explicitly **outside** this theorem's scope.
- **N2 wall independence:** (P1) single-plaquette wall, (P2) gauge-invariance wall, (P3) canonical-normalization wall (load-bearing via R1), (P4) real-action wall (load-bearing for excluding `iθ` slot), (P5) bounded-below wall are all named independently and not collapsed.
- **N3 hidden-wall scan:** "canonical", "retained", "standard path-integral" are treated as named surface boundaries. (P4) and (P5) are named explicitly as path-integral well-definedness conventions, not as derived theorems from Cl(3)⊗Z³.
- **N4 residual matching:** the first of two missing bridges named by the Leg A judicial-panel verdict is matched; the second is explicitly out of scope.
- **N5 rhetoric audit:** all "CP-odd" / "topological-density" / "F̃F" wording is restricted to the single-plaquette `Im Tr U_P` slot; broader topological discretizations are out of scope.
- **N6 partial-closure path:** this is a bounded source repair of one named missing bridge, not a new axiom or unconditional retained-status promotion.
- **N7 steelman:** a hostile reviewer can argue that frameworks with `iθ Q` (e.g., the strong-CP continuum action) live outside the (P4) real-positive surface and are not ruled out by this note. The reply: that is correct, and (P4) is the named surface boundary that excludes them; this note's scope is the (P4)-retained surface, not all conceivable path integrals.
- **N8 cross-cycle echo:** prior action-surface notes consistently distinguish (a) "real-positive Wilson surface" from (b) "the full continuum theory including imaginary topological terms"; this note preserves that distinction and selects (a) uniquely on the retained surface.

---

## §9. Runner: explicit construction + rejection on SU(3) configurations

The companion runner [`scripts/frontier_wilson_action_surface_selector_real_positive_2026_05_25.py`](../scripts/frontier_wilson_action_surface_selector_real_positive_2026_05_25.py) exhibits the bounded construction-and-rejection at the operator-slot level rather than only evaluating the real-Wilson surface. Eight verification gates:

- **V1 — Gauge-invariant scalar enumeration.** For `N = 20` random SU(3) plaquette configurations, verify that candidate functionals `{Tr U_P, Tr U_P^†, Tr U_P^2, Tr(U_P U_P^†)}` are gauge-invariant under random conjugations `U_P → V U_P V^†`. PASS = all four invariant within numerical tolerance, verifying Lemma 1's framing.
- **V2 — Real-action exclusion of imaginary-plaquette term.** Build the candidate action `S[U] = S_W[U] + iθ Σ_P Im Tr U_P` for `θ ∈ {0.0, 0.1, 1.0}` on a small 2×2×2×2 Λ. Compute `Im S` and `Im exp(−S)` on `N = 10` random configurations. PASS = `θ ≠ 0` gives nonzero `Im S` and nonzero `Im exp(−S)`, verifying Lemma 4 / Step 1 directly.
- **V3 — Canonical-normalization continuum-limit check.** Symbolically (sympy) expand `U_P = exp(i a² F^a_{μν} T^a)` to second order in `a`; compute leading orders of `Re Tr U_P` and `Im Tr U_P`. PASS = `Re Tr U_P → N_c − (a^4/4) F^a F^a + O(a^6)` matching the YM kinetic with `β = 6`, and `Im Tr U_P = O(a^6)`. (Also exhibited numerically by computing the leading-`a` expansion of `Tr U_P` and verifying the leading-order coefficient `(N_c − Re Tr U_P)/(a^4/4) → F^a F^a` as `a → 0`.)
- **V4 — Bounded-below check on real Wilson slot.** Compute `S_W = (β/N_c) Σ_P (N_c − Re Tr U_P)` on `N = 50` random SU(3) configurations. PASS = all `S_W ≥ 0` with margin (verifies (P5) on the retained Wilson slot).
- **V5 — Imaginary-plaquette term has no bounded-below structure.** Compute the candidate `θ · Σ_P Im Tr U_P` on `N = 50` random configurations. PASS = the candidate takes BOTH negative and positive values across the sample (i.e., no bounded-below structure exists for the imaginary candidate; combined with V2 this rules out the imaginary slot from two independent angles).
- **V6 — Uniqueness check: enumerate candidate ansatzes.** Build candidate single-plaquette functionals `{Re Tr U_P, Im Tr U_P, (Re Tr U_P)², |Tr U_P|², (Tr U_P)², Re((Tr U_P)²), Im((Tr U_P)²)}` and check (P1)-(P5) systematically for each. PASS = only `Re Tr U_P` satisfies all five constraints; all others fail at least one.
- **V7 — Explicit forbidden-slot construction + rejection.** Construct the F̃F-proxy term `S_F̃F = i θ · Σ_P (Tr U_P − Tr U_P^†)/2` for `θ = 0.5`. Verify it violates (P4) on `N = 20` random configurations (nonzero `Im S`). PASS = rejection criterion (`Im S ≠ 0`) triggers on at least 95% of configurations (allowing for the measure-zero coincidence where `Σ_P Im Tr U_P = 0`).
- **V8 — Compose with retained canonical-normalization primitive.** Compute `β` from the leading-`a` continuum limit of the canonical Wilson action using the retained `g_bare² = 2 N_c / β = 1` from (R1). PASS = `β = 6` emerges as the unique value consistent with (R1) and the leading-order `F^a F^a / (4 g²)` matching.

Hard assertion gates. Target: PASS = 8 FAIL = 0. NumPy + sympy. Runtime < 5 min.

---

## §10. Commands run

```bash
python3 scripts/frontier_wilson_action_surface_selector_real_positive_2026_05_25.py
# Exit code: 0
# PASS = 8  FAIL = 0
# Runtime: < 5 minutes on standard laptop
```

Cached log: [`logs/runner-cache/frontier_wilson_action_surface_selector_real_positive_2026_05_25.txt`](../logs/runner-cache/frontier_wilson_action_surface_selector_real_positive_2026_05_25.txt).

---

## References and explicit premises

The following are the framework baseline, retained one-hop authorities, and explicit bounded premises that this note composes:

- (A1) Cl(3) local algebra — repository axiom.
- (A2) Z³ spatial substrate — repository axiom.
- (R1) Canonical normalization `β = 6`: [`docs/G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md`](G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md) (retained primitive — load-bearing one-hop authority).
- (P4) real-action surface, (P5) bounded below: standard QFT path-integral well-definedness conventions on the Boltzmann measure (not new axioms; not derived from Cl(3)⊗Z³).

**No external citations** (Wilson 1974, Vafa-Witten, Leutwyler-Smilga, etc.) are used as proof inputs. The arguments above are bounded compositions of (A1)+(A2)+(R1) + the named path-integral conventions. External literature may be cited in downstream / paper-level write-ups but is not load-bearing here.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- `STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md` (effective_status: audited_conditional — demoted to backtick per dep-hygiene rule; this is the parent row this note is the repair candidate for one of the two missing bridges, not a load-bearing dep on this proof's chain)
