# Axiom-First Fermionic Stefan-Boltzmann — the `T⁴` Law with Finite `g_eff` for Every Realized-Class Kinetic Kernel with Point-Like Linear-Cone Zero Set (Narrow Theorem)

**Date:** 2026-05-26 (re-scoped 2026-06-11; see §0)
**Claim type:** bounded_theorem
**Claim scope:** On the `Z³` one-qubit single-ladder one-particle
hopping surface supplied by the current minimal axiom memo and the
retained tensor-product Fock/translation bridge, for **every** kinetic kernel in the realized class —
finite-range, sublattice-periodic, Hermitian hopping with analytic
Bloch band family `{E_b(p)}` on the Brillouin torus — **whose massless
set is point-like with linear cones** (hypothesis (Z): the zero set
`Z(h) = {(p_j, b) : E_b(p_j) = 0}` is finite and nonempty, and each vanishing branch
satisfies `|E_b(p_j + q)| = |V_jb q| + O(|q|²)` with invertible real
`3×3` matrices `V_jb`), the half-filled free-Fermi thermal energy
density per site obeys, as `T → 0`,
`u(T) = g_eff · (7/8)(π²/30) · T⁴ + O(T⁵)` with
`g_eff = Σ_(j,b) |det V_jb|⁻¹ ∈ (0, ∞)` — the **cone-weighted massless
species count** (equal to the bare zero-branch count when the cone
matrices are unimodular; equal to `N₀/c³` for `N₀` isotropic cones of
speed `c`). Equivalently: `g_eff(T) := u(T)/[(7/8)(π²/30)T⁴]` has a
finite `T → 0` plateau — "the massless species density is finite" in
the retained Stefan-Boltzmann bridge row's own per-dof currency —
**conditionally on the kernel-geometry hypothesis (Z)**, which is
stated explicitly and is demonstrably load-bearing in both clauses
(an extended-zero-surface kernel gives `g_eff ∝ T⁻²`, Sommerfeld; a
point-like-but-quadratic zero gives `g_eff ∝ T^(−3/2)`). The error
control is explicit at the stated order: off-cone modes contribute
`O(e^(−Δ/T))`, the cone-window replacement costs `O(T⁵)` absolute
(`O(T)` relative), with constants depending only on the kernel's cone
data `(V_jb, C_j, r_j)`, gap `Δ`, band number, and bandwidth. This
note **neither assumes nor derives `phi = -1`**: the quantifier runs
over the kernel class; both licensed branch symbols appear only as
computed witnesses classified by their zero-set geometry.
**Status authority:** independent audit lane only. This source note
does not set or predict an audit outcome; audit verdict and effective
status are set only by the independent audit lane.
**Primary runner:** [`scripts/frontier_axiom_first_fermionic_stefan_boltzmann_narrow.py`](../scripts/frontier_axiom_first_fermionic_stefan_boltzmann_narrow.py)
(`TOTAL: PASS=20 FAIL=0`, deterministic, runtime well under one
minute)
**Runner cache:** [`logs/runner-cache/frontier_axiom_first_fermionic_stefan_boltzmann_narrow.txt`](../logs/runner-cache/frontier_axiom_first_fermionic_stefan_boltzmann_narrow.txt)
**Authority role:** source-note proposal. If retained, this row
supplies, conditionally on (Z), the clause "the massless species
density is finite" of the realized kinetic kernel — in the retained
SB bridge row's per-dof currency — for any downstream consumer that
separately certifies the kernel geometry. It changes no existing
row's status and performs no selection itself.

## 0. Changelog

- **2026-05-26.** First version: fermionic Stefan-Boltzmann
  `u_F(T) = (7π²/60) T⁴` per Dirac species on a **supplied** continuum
  dispersion `ω = c|k|` imported from the emergent-Lorentz row, with
  KMS/spin-statistics rows cited as load-bearing upstreams.
- **2026-06-11.** **Quantifier re-scope (the load-bearing change).**
  The old quantifier bound a supplied dispersion/inventory: it said
  nothing about kernels at all, so it could never supply a finiteness
  requirement on the realized kernel's massless set, and its
  load-bearing import of the emergent-Lorentz row (whose isotropy core
  is derived ON the staggered dispersion) made it unusable by any
  flux-selection consumer (RP circularity class). The theorem is
  restated with the quantifier on the **realized kernel class** and
  the linear-cone zero-set geometry as the **explicit hypothesis (Z)**
  — a condition on the kernel, not an import. The emergent-Lorentz,
  KMS, spin-statistics, spectrum-condition, and anomaly-3+1 rows are
  demoted from load-bearing citations to plain-text context (the
  Fermi factor now enters as the declared probe currency matching the
  retained bridge row, boundary B-1). The runner is rebuilt to compute
  the load-bearing content: mode sums on explicit realized-class
  kernels (positive leg: isotropic and anisotropic point-cone kernels
  plateau at the predicted cone-weighted count; falsification legs:
  extended-zero-surface and quadratic-point-zero kernels violate the
  `T⁴` law at the predicted divergence rates), with `[A]–[D]` tags and
  declared residuals. Motivation (context only, NOT an authority):
  the P-FLUX finite-species-density no-go of 2026-06-10 names exactly
  this promotion — an SB row whose quantifier binds the realized
  kernel — as the single most natural future supplier of its boundary
  B-Z2 (its N6); this note is written to be that row, conditionally
  on (Z), without itself consuming or deciding any branch fact.
  The 2026-05-26 continuum results are preserved as Corollary FSB-C
  (specialization to a supplied isotropic dispersion), so downstream
  citations of the per-Dirac-species law and the `7/8` per-dof ratio
  are unaffected.

## Repair Note

**2026-07-10.** The audit's notes for re-audit were:

> scope_too_broad: Require Z(h) to be nonempty or replace
> g_eff in (0,infinity) by g_eff in [0,infinity), and restrict FSB-X to the
> explicit witnesses or add hypotheses globally controlling every zero
> component; then re-audit.

The chosen arms are the NONEMPTY arm for hypothesis (Z), preserving
the existing `g_eff ∈ (0, ∞)` claim surface, and the
RESTRICT-TO-WITNESSES arm for FSB-X. No computational content changed;
the runner gains an empty-set discriminator and note-surface pins.

## 1. Question and method

**Question.** The retained Stefan-Boltzmann bridge row normalizes
fermionic thermal energy density per **supplied** relativistic degree
of freedom as `(7/8)(π²/30)T⁴`; it binds "a relativistic, effectively
massless thermal degree of freedom" and explicitly does not derive
the inventory. What does the **realized kinetic kernel** supply to
that bookkeeping? Concretely: for which kernels in the licensed
realized class does the low-`T` thermal energy density obey the `T⁴`
law at all, and when it does, what finite number multiplies the
bridge coefficient?

**Method.** State the kernel-geometry condition explicitly
(hypothesis (Z)) and prove the `T⁴` law with an explicit error order
for the whole class at once, by classical analysis: split the
Brillouin torus into cone windows and a gapped remainder, replace
each cone window by its tangent cone with a quadratic-error Lipschitz
bound on the Fermi integrand, and evaluate the tangent-cone integral
in closed form via the retained bridge row's Fermi-Dirac integral
identity. Then **compute** the load-bearing content both ways:
realized-class kernels satisfying (Z) plateau at the predicted
cone-weighted count (including an anisotropic witness certifying the
`|det V|⁻¹` weighting), and kernels violating either clause of (Z)
violate the `T⁴` law at the predicted rates. Circularity discipline
throughout: no flux value, branch label, species inventory, or
dispersion import enters the statement or the proof; `phi = -1` is
neither assumed nor derived.

## 2. Setup and definitions

**Surface.** The `Z³` one-qubit single-ladder one-particle hopping
surface: [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies the per-site
one-qubit operator algebra, and the retained tensor-product fermion
bridge supplies the finite periodic Fock/translation extension with
local ladder operators.
A **realized-class
kinetic kernel** is a finite-range Hermitian hopping matrix `h` on
this surface, periodic under a full-rank sublattice `Λ ⊆ Z³` with
unit cell of `n_c` sites, hence with an analytic Hermitian Bloch
symbol `H(p)` (`n_c × n_c`, trigonometric-polynomial entries) on the
reduced Brillouin torus `T*_Λ` and continuous band family
`{E_b(p)}_(b=1..n_c)`.

**Probe (the currency; boundary B-1).** The half-filled free-Fermi
thermal energy density per site,

```text
u(T) := Σ_b ∫_(T*_Λ) d³p/(2π)³ |E_b(p)| n_F(|E_b(p)|/T),
n_F(x) = 1/(eˣ + 1),
```

the thermodynamic limit of `(1/L³) Σ_modes |E| n_F(|E|/T)` on `L³`
volumes (`Λ`-compatible `L`). On the retained Fock surface this is
the standard particle-hole-symmetric (chemical potential 0) reading:
each single fermionic mode of energy `|E|` has two states,
`Z_mode = 1 + e^(−|E|/T)`, mean excitation energy
`|E| n_F(|E|/T)`; negative-energy modes count through holes. This is
the same integrand as the retained SB bridge row and the same probe
as the P-FLUX note's F-3 certificate. It is a hypothesis-
satisfiability currency: thermal equilibrium of the realized dynamics
is NOT derived here.

**The per-dof object.**
`g_eff(T) := u(T) / [(7/8)(π²/30) T⁴]` — the retained bridge row's
per-dof normalization as denominator.

**Hypothesis (Z) (point-like linear-cone zero set).** The massless
set `Z(h) = {(p_j, b) : E_b(p_j) = 0}` is finite and nonempty, and for each
`(p_j, b) ∈ Z(h)` there are an invertible real `3×3` matrix `V_jb`,
a radius `r_j > 0`, and a constant `C_j < ∞` with

```text
| |E_b(p_j + q)| − |V_jb q| |  ≤  C_j |q|²    for |q| ≤ r_j.
```

(No isotropy is required; `|V_jb q|` is the Euclidean norm of
`V_jb q`. Because the bands are continuous on a compact torus,
finiteness of `Z(h)` plus the local cone bounds already imply a
uniform gap `Δ > 0` off the cone neighborhoods; no separate gap
hypothesis is needed.)

(2026-07-10 scope repair: nonemptiness is load-bearing for
`g_eff ∈ (0, ∞)`. The empty-`Z(h)` fully gapped case is excluded from
FSB-K's claim surface: there `u(T) = O(e^{-Δ/T})` and
`g_eff(T) → 0`, so the `T⁴` normalization is not the natural currency
and no FSB-K claim is made.)

## 3. Statements

### 3.1 Theorem FSB-K (the `T⁴` law on the realized kernel class)

**For every realized-class kinetic kernel `h` satisfying hypothesis
(Z), with**

```text
g_eff  :=  Σ_((j,b) ∈ Z(h)) |det V_jb|⁻¹  ∈  (0, ∞),
```

**there are constants `C < ∞`, `T₀ > 0` (depending only on the cone
data `(V_jb, C_j, r_j)`, the off-cone gap `Δ`, the band number `n_c`,
and the bandwidth `max|E_b|`) such that**

```text
u(T)  =  g_eff · (7/8)(π²/30) · T⁴  +  R(T),
|R(T)| ≤ C T⁵   for 0 < T ≤ T₀.
```

**In particular `g_eff(T) → g_eff`, the cone-weighted massless
species count: `g_eff = N₀` when all `|det V_jb| = 1`, and
`g_eff = N₀/c³` for `N₀` isotropic cones of speed `c`.** ∎ (§4;
runner checks 1–11.)

### 3.2 Corollary FSB-CL (the conditional finiteness clause)

**For any realized-class kernel satisfying (Z), the clause
"`g_eff(T)` is bounded as `T → 0`" holds, with limit the cone-
weighted massless species count — i.e. the massless species density
is finite, stated in the retained SB bridge row's own per-dof
currency.** This row supplies that clause **conditionally on (Z)**:
whether a given realized kernel satisfies (Z) is a separate,
external, computable kernel-geometry fact, not certified here
(boundary B-3). ∎

### 3.3 Proposition FSB-X (both clauses of (Z) are load-bearing on explicit witness kernels; certificate grade)

(a) **Extended zero set.** For the explicit extended-zero witness
kernel (§4.6; runner checks 12–13), `u(T) ≍ T²` (Sommerfeld), so
`g_eff(T) ≍ T⁻²` diverges — the `T⁴` law fails structurally.
(b) **Point-like but quadratic.** For the explicit isolated
quadratic-point witness kernel (runner checks 14–15),
`u(T) ≍ T^(5/2)` and `g_eff(T) ≍ T^(−3/2)` diverges — point-likeness
alone is insufficient; the linear-cone clause is load-bearing
separately. FSB-X is certificate + sketch grade, not the theorem-grade
core (boundary B-5). No sufficient-condition claim is made for kernels
with additional uncontrolled zero components: a flatter additional
component (`|E| ≍ |q|^α`, `α > 2`) dominates the low-`T` asymptotics
(`u ≍ T^{1+3/α}`), so the two-sided rates above are witness-specific;
only the per-witness divergence of `g_eff(T)` is certified.
(2026-07-10 scope repair.) ∎

### 3.4 Corollary FSB-C (continuum specialization; the 2026-05-26 content, preserved)

Specializing FSB-K's tangent-cone integral to a supplied isotropic
dispersion `ω = c|k|` with 4 internal degrees of freedom (one Dirac
species: 4 conical branches with `V = c·1`, `|det V| = c³`):

```text
u_F(T) = 4 · (7/8)(π²/30) T⁴/c³ = (7π²/60) T⁴/c³
       = (7π²/60) T⁴ in natural units (per Dirac species),
```

and per single degree of freedom
`u_F/u_B = η(4)/ζ(4) = 1 − 2^(1−4) = 7/8` against the bosonic
`(π²/30)T⁴` — the `Γ(4)η(4) = 7π⁴/120` Fermi-Dirac integral identity
of the retained bridge row. The `7/8` is the alternating-Dirichlet
(APBC/odd-Matsubara) partial-sum factor `1 − 2^(1−s)` at `s = 4`;
the consistency of this factor with the retained Riemann-Dirichlet
anchor and the `g_* = 28 + (7/8)·90 = 427/4` supplied-inventory
arithmetic is unchanged from the first version. ∎ (Runner checks
1–3.)

## 4. Proof of FSB-K

### 4.1 Step 0 (mode sum to band integral)

On a `Λ`-compatible `L³` volume the `L³` one-particle modes organize
as `n_c` bands over the `(L³/n_c)`-point reduced grid; per-site
averaging gives `(1/L³) Σ_modes = Σ_b` (reduced-grid average)
`× vol(T*_Λ)/(2π)³`-normalized Riemann sums. The summand
`|E_b(p)| n_F(|E_b(p)|/T)` is continuous on the compact torus, so
the thermodynamic limit exists and equals the band integral in §2
with the uniform measure `d³p/(2π)³`. (Finite-`L` rates are certified
numerically, boundary B-2.)

### 4.2 Step 1 (gapped remainder)

Shrink each `r_j` so that `C_j r_j ≤ s_j/2` with `s_j` the smallest
singular value of `V_jb`. Group the zero pairs `(p_j,b)` by distinct
momentum point. Balls centered at distinct zero momenta may be taken
disjoint; when several bands vanish at the same momentum, their branch
contributions are summed inside the same ball. No disjointness between band
labels at a shared momentum is assumed. Off the union of these balls, every band obeys
`|E_b| ≥ Δ > 0` (compactness, §2), and `x n_F(x/T) ≤ x e^(−x/T)` is
decreasing in `x ≥ Δ ≥ T`, so the off-cone contribution is at most
`n_c · max|E_b| · e^(−Δ/T) = O(e^(−Δ/T))`, super-polynomially small.

### 4.3 Step 2 (cone-window replacement, the `O(T⁵)` bound)

Let `φ_T(x) := x n_F(x/T)`. Then
`φ_T′(x) = n_F(x/T) + (x/T) n_F′(x/T)` satisfies
`|φ_T′(x)| ≤ 2 e^(−x/(2T))` (since `n_F(y) ≤ e^(−y)` and
`y|n_F′(y)| ≤ y e^(−y) ≤ e^(−y/2)`). On `B_j`, the choice of `r_j`
gives `|E_b(p_j+q)| ≥ |V_jb q| − C_j|q|² ≥ |V_jb q|/2`, so

```text
| φ_T(|E_b(p_j+q)|) − φ_T(|V_jb q|) |
   ≤  C_j |q|² · 2 e^(−|V_jb q|/(4T))
   ≤  2 C_j |q|² e^(−s_j |q|/(4T)),
```

and integrating over `B_j`:

```text
∫ d³q |q|² e^(−s_j|q|/(4T)) ≤ (4T/s_j)⁵ ∫ d³x |x|² e^(−|x|)
                            = (4T/s_j)⁵ · 4π Γ(5),
```

an `O(T⁵)` absolute error per cone branch.

### 4.4 Step 3 (extending the tangent cone to `R³`)

`∫_(|q|>r_j) φ_T(|V_jb q|) d³q ≤ ∫_(|q|>r_j) |V_jb q| e^(−s_j|q|/T) d³q
= O(e^(−s_j r_j/(2T)))`, again super-polynomially small.

### 4.5 Step 4 (the tangent-cone integral in closed form)

Substituting `u = V_jb q` (`d³q = d³u/|det V_jb|`) and going to
spherical coordinates:

```text
∫_(R³) d³q/(2π)³ |V_jb q| n_F(|V_jb q|/T)
   = |det V_jb|⁻¹ (1/(2π²)) ∫₀^∞ k³ n_F(k/T) dk
   = |det V_jb|⁻¹ (1/(2π²)) T⁴ Γ(4) η(4)
   = |det V_jb|⁻¹ (7/8)(π²/30) T⁴,
```

where `Γ(4)η(4) = 7π⁴/120` is the retained bridge row's Fermi-Dirac
integral identity `I_F` (consumed, not re-derived), and
`(1/(2π²)) · 7π⁴/120 = 7π²/240 = (7/8)(π²/30)` exactly. Summing over
the finitely many `(j, b) ∈ Z(h)` and collecting the Step-1/2/3
errors proves FSB-K with `|R(T)| ≤ C T⁵`. ∎

### 4.6 FSB-X sketches (certificate grade)

(a) In a tubular neighborhood of a regular codim-1 zero surface,
`|E| = |∇E| · dist + O(dist²)` with `|∇E| ∈ [a, A]`, `a > 0`; the
coarea formula gives
`u(T) ⊇ (Area/(2π)³) ∫₀ φ_T(a t) dt ≍ (T²/a²) Γ(2) η(2)`-scale terms,
so `u ≍ T²` (`η(2) = π²/12`; the Sommerfeld law) and
`g_eff ≍ T⁻²`. (b) For an isolated quadratic zero, `|E| ≍ |q|²`
rescales as `q = √T x`, giving `u ≍ T^(3/2) · T = T^(5/2)` and
`g_eff ≍ T^(−3/2)`. Both rates are computed on explicit kernels in
the runner; no theorem-grade claim is made beyond the computed
certificates (boundary B-5).

## 5. Boundaries (stated up front)

| ID | Boundary | Where it bites |
|---|---|---|
| B-1 | `u(T)` is the half-filled free-Fermi probe in the retained SB bridge row's own integrand (hypothesis-satisfiability currency); thermal equilibrium / KMS structure of the realized dynamics is NOT derived here — the axiom-first KMS and spin-statistics rows are context, not load-bearing | §2, runner residual after check 15 |
| B-2 | The theorem is stated at the thermodynamic limit; finite-`L` mode-sum convergence is certified numerically at the stated grids (`L = 64` vs `128`, `< 1%`), not proven with explicit constants | §4.1, check 8 |
| B-3 | Hypothesis (Z) is a CONDITION: this row verifies it for its explicit runner witnesses only and does NOT certify it for the realized kernel; which kernel is realized (the P-FLUX bit) is neither assumed nor derived — any selection requires external, separately computed kernel-geometry certificates plus this row's promotion, composed by a downstream consumer | §3.2, checks 6, 17–18 |
| B-4 | Error order: relative `O(T)` (absolute `O(T⁵)`) is what is proven; the measured order on the odd-symbol witnesses is faster (their cone corrections are `O(q³)`); constants are not optimized | §4.3, checks 6, 11 |
| B-5 | Proposition FSB-X (the falsification legs) is computed-certificate + sketch grade, not theorem grade; it establishes only that (Z) is load-bearing | §3.3, §4.6, checks 12–15 |

## 6. Cited authorities (one hop, with license statements)

Load-bearing (markdown links):

1. [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) —
   axiom premise node. License used: Lattice (`Z³`, translations, NN
   cubic adjacency) and Quantum (per-site qubit) for the kernel-class
   constructions. No dynamics drawn.
2. [`TENSOR_PRODUCT_TRANSLATION_FERMION_OPERATOR_BRIDGE_NARROW_THEOREM_NOTE_2026-05-25.md`](TENSOR_PRODUCT_TRANSLATION_FERMION_OPERATOR_BRIDGE_NARROW_THEOREM_NOTE_2026-05-25.md)
   — retained. License used: the finite periodic Fock surface on
   which the per-mode `Z_mode = 1 + e^(−|E|/T)` half-filled reading
   of the probe lives.
3. [`GSTAR_THERMAL_SEVEN_EIGHTHS_STEFAN_BOLTZMANN_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md`](GSTAR_THERMAL_SEVEN_EIGHTHS_STEFAN_BOLTZMANN_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md)
   — retained-grade currency-setting row. License used: the
   Fermi-Dirac integral identity `I_F = Γ(4)η(4) = 7π⁴/120` and the
   per-dof normalization `(7/8)(π²/30)T⁴` (Step 4 of the proof and
   the `g_eff` denominator). Composition: that row owns the integral
   arithmetic for a SUPPLIED inventory ("a relativistic, effectively
   massless thermal degree of freedom"; "does not derive the Standard
   Model particle inventory"); this row binds the kernel class and
   derives WHICH count a (Z)-satisfying realized spectrum supplies.
   Disjoint roles; no duplication, no contradiction.
4. [`HIERARCHY_SEVEN_EIGHTHS_RIEMANN_DIRICHLET_DIMENSIONAL_ANCHOR_NARROW_THEOREM_NOTE_2026-05-10.md`](HIERARCHY_SEVEN_EIGHTHS_RIEMANN_DIRICHLET_DIMENSIONAL_ANCHOR_NARROW_THEOREM_NOTE_2026-05-10.md)
   — retained. License used: the algebraic identity
   `η(4)/ζ(4) = 1 − 2^(1−4) = 7/8` (Corollary FSB-C's
   identification only).

Plain-text pointers (NOT load-bearing; the 2026-06-11 demotions are
the circularity-discipline fix):

- `EMERGENT_LORENTZ_INVARIANCE_NOTE.md` and
  `LORENTZ_KERNEL_POSITIVE_CLOSURE_NOTE.md` — the first version
  imported the linear dispersion from here. Demoted: the emergent-
  Lorentz isotropy core is derived ON the staggered dispersion, so a
  load-bearing import would put this row in the RP circularity class
  for any flux-selection consumer. The linear-cone geometry is now
  hypothesis (Z), stated of the kernel.
- `AXIOM_FIRST_KMS_CONDITION_THEOREM_NOTE_2026-05-01.md`,
  `AXIOM_FIRST_SPIN_STATISTICS_THEOREM_NOTE_2026-04-29.md`,
  `AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29.md`,
  `ANOMALY_FORCES_TIME_THEOREM.md` — all unaudited; demoted to
  context. The Fermi factor enters as the declared probe currency
  (B-1) matching the retained bridge row, not as a derived
  equilibrium statement.
- `AXIOM_FIRST_STEFAN_BOLTZMANN_THEOREM_NOTE_2026-05-01.md` — the
  bosonic counterpart (context for the `7/8` comparison in FSB-C).
- `P_FLUX_FINITE_SPECIES_DENSITY_FROM_DETERMINANT_MATSUBARA_SURFACE_NARROW_NO_GO_NOTE_2026-06-10.md`
  — **motivation only, not an authority**: its N6 names this
  promotion (an SB row binding the realized kernel) as the most
  natural supplier of its boundary B-Z2, and its F-3 certificate is
  reproduced independently by this note's runner on this runner's own
  constructions. Nothing from that note is load-bearing here.
- `SM_RELATIVISTIC_DOF_COUNT_IMPORT_NOTE_2026-05-17.md`,
  `G_STAR_SM_CONTENT_AT_LEPTOGENESIS_FROM_SUPPLIED_THERMAL_INVENTORY_BOUNDED_THEOREM_NOTE_2026-05-28.md`
  — the supplied-inventory `g_*` convention this row's currency
  matches (context).

Forbidden imports: no PDG values, no lattice-MC values, no fitted
coefficients, no species names, no flux or branch input, no new
axioms.

## 7. What the runner computes

[`scripts/frontier_axiom_first_fermionic_stefan_boltzmann_narrow.py`](../scripts/frontier_axiom_first_fermionic_stefan_boltzmann_narrow.py)
— deterministic, no network, no randomness; numpy + sympy + mpmath;
runtime well under one minute. 20 checks in five sections:

- **[A]** (4 checks) the exact currency: `η/ζ` arithmetic (symbolic),
  the Fermi-Dirac integral `Γ(4)η(4) = 7π⁴/120` and `I_F/I_B = 7/8`
  (40-digit), the per-dof normalization
  `(1/2π²) I_F = 7π²/240 = (7/8)(π²/30)` (exact + 40-digit radial),
  and the cone-reduction Jacobian
  `∫ d³q/(2π)³ |Vq| n_F = |det V|⁻¹ (7/8)(π²/30) T⁴` certified by
  direct 3D midpoint quadrature at the anisotropic `V = diag(2,2,4)`.
- **[B]** (7 checks) the positive leg: eigensolver tie of the symbol
  witnesses to explicit lattice kernels at `L = 8` (Kawamoto-Smit
  phases and scalar NN — the witnesses ARE realized-class spectra);
  computed zero-set classification (point counts `8, 8` vs the
  unboundedly growing surface trace vs the single quadratic point;
  cone-expansion order at a zero); the W1 plateau
  `g_eff(0.05) = 0.979 ≈ 1 = 8/2³` with T-halving ratio `≈ 0.95`;
  finite-size Cauchy control (`L = 64` vs `128`, `1.4 × 10⁻³`); the
  ANISOTROPIC W2 plateau at `8/16 = 1/2` (the `|det V|⁻¹` weighting);
  the gapped-band null (`< 10⁻³` share); the measured low-T error
  order (monotone, halving ratio `≤ 0.55`).
- **[C]** (4 checks) the falsification legs: the extended-zero-
  surface kernel diverges `g_eff = 323, 81, 20.4, 5.0` with ratios
  `≈ 4` (`T⁻²`, reproducing F-3 independently) and plateaus in
  Sommerfeld currency `u/T² ≈ 0.233`; the quadratic point zero
  diverges with ratios `≈ 2.8` (`T^(−3/2)`); single-clause selection
  consistency (the (CL) clause holds on exactly the (Z)-satisfying
  witnesses).
- **[D]** (3 checks) composition with the retained bridge (textual
  hypotheses + ledger status + exact `7/240` coefficient match,
  disjoint roles); circularity discipline on this note's own file
  (no load-bearing emergent-Lorentz/KMS links; the declared
  branch-blindness sentence present); branch-blindness of the
  computation (both branch symbols through the same code path,
  separated only by computed geometry).
- **[E]** (2 checks) the 2026-07-10 scope repair: an explicitly gapped
  empty-zero-set kernel has decreasing `u(T)/T⁴ → 0` on three
  decreasing temperatures, and note-surface pins require the
  nonempty-(Z), explicit-witness FSB-X, witness-specific, dated repair,
  and Repair Note wording.

Four `RESIDUAL (declared-open): ...` lines mark boundaries B-1, B-2,
B-3, B-5 where they are load-bearing (B-4 is recorded inside check
11's message).

Runner check classes per the audit rubric: checks 1–15 and 18–19 are
class (A) (exact symbolic arithmetic and algebraic/spectral/
quadrature computations on constructed finite objects); checks 16–17
and 20 conjoin class (B) components (cross-note or source-note text/
ledger verification) with class (A) arithmetic where applicable.

## 8. What this does NOT close

- **The P-FLUX bit.** `phi = -1` is neither assumed nor derived. This
  row, even if retained, supplies the finiteness clause only
  **conditionally on hypothesis (Z)**; selecting a branch requires a
  downstream consumer to compose it with separately computed,
  separately audited kernel-geometry certificates for the realized
  kernel (which branch satisfies (Z) is exactly the kind of fact the
  P-FLUX notes compute; none of it is consumed here).
- Thermal equilibrium / KMS structure of the realized dynamics (B-1).
- Finite-`L` convergence constants (B-2); optimized error constants
  (B-4).
- Theorem-grade necessity of (Z) (FSB-X stays certificate grade,
  B-5).
- The Standard Model inventory, `g_*` content, and everything the
  retained bridge row already declares out of scope — unchanged and
  not duplicated here.
- No existing row's status is changed.

## 9. Command

```bash
python3 scripts/frontier_axiom_first_fermionic_stefan_boltzmann_narrow.py
```

Expected output (deterministic): 20 numbered `[PASS]` lines in
sections `[A]`/`[B]`/`[C]`/`[D]`/`[E]` as described in §7, including
`g_eff(T) at L=128 = 0.979, 1.026, 1.144, 1.508 at T=0.05..0.4`,
`W2 ... g_eff = 0.472, 0.507 ... plateau at sum |det V|^-1 = 8/16 =
1/2`, `g_eff = 323, 81, 20.4, 5.0 ... T-halving ratios 3.97, 3.99`,
`u/T^2 = 0.232, 0.234, 0.235, 0.232`, `ratios 2.78, 2.72 ~ 2^1.5`;
four `RESIDUAL (declared-open): ...` lines; then exactly:

```text
TOTAL: PASS=20 FAIL=0
```

followed by the VERDICT block stating the conditional `T⁴` law with
finite `g_eff = Σ|det V|⁻¹` on the (Z)-satisfying realized class, the
two falsification rates, and that `phi = -1` is neither assumed nor
derived. Exit code 0 iff `FAIL=0`.

## 10. Honest status

```yaml
claim_type_author_hint: bounded_theorem
claim_scope: "On the Z^3 one-qubit single-ladder one-particle hopping surface supplied by the current minimal axiom memo and the retained tensor-product Fock/translation bridge: for every realized-class kinetic kernel (finite-range, sublattice-periodic, Hermitian hopping with analytic Bloch bands) satisfying hypothesis (Z) — the massless set is a finite nonempty set of points with linear cones, |E_b(p_j+q)| = |V_jb q| + O(|q|^2), V_jb invertible — the half-filled free-Fermi thermal energy density per site obeys u(T) = g_eff (7/8)(pi^2/30) T^4 + O(T^5) as T -> 0, with g_eff = sum |det V_jb|^{-1} finite = the cone-weighted massless species count; equivalently g_eff(T) = u(T)/[(7/8)(pi^2/30)T^4] has a finite plateau (the massless species density is finite, in the retained SB bridge row's per-dof currency), conditionally on (Z). Error control: off-cone O(e^{-Delta/T}), cone-window O(T^5) absolute / O(T) relative, constants explicit in the kernel's cone data, gap, band number, bandwidth. The hypothesis is demonstrably load-bearing on the explicit witness kernels in both clauses (computed certificates: the extended-zero witness gives g_eff ~ T^-2 Sommerfeld; the quadratic-point witness gives g_eff ~ T^-3/2); no sufficient-condition claim is made for kernels with additional uncontrolled zero components. Bounded by: the probe currency (free-Fermi half-filled integrand, equilibrium not derived); thermodynamic-limit statement with numerically certified finite-L control; (Z) verified only for the runner's witnesses, never for 'the realized kernel'; FSB-X at certificate grade. Branch-blind: phi = -1 is neither assumed nor derived, and no flux, branch, or inventory input is consumed. Continuum specialization preserved: u_F = (7 pi^2/60) T^4 per Dirac species; u_F/u_B = 7/8 per dof."
upstream_dependencies:
  - minimal_axioms
  - tensor_product_translation_fermion_operator_bridge_narrow_theorem_note_2026-05-25
  - gstar_thermal_seven_eighths_stefan_boltzmann_bridge_narrow_theorem_note_2026-06-06
  - hierarchy_seven_eighths_riemann_dirichlet_dimensional_anchor_narrow_theorem_note_2026-05-10
admitted_context_inputs: []
source_sets_audit_outcome: false
```

This note **neither assumes nor derives `phi = -1`**. The statement
is about kernel classes and is branch-blind on its face: hypothesis
(Z) is a geometric condition any kernel either satisfies or violates,
the runner's witnesses include both licensed branch symbols processed
identically and classified only by their computed zero-set geometry,
and the conditional supplier role (Corollary FSB-CL) becomes a
selection only if a downstream consumer composes a retained promotion
of this row with external branch-geometry certificates — neither of
which this note performs or predicts.
