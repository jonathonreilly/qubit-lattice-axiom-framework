# C10: burn-and-turn source tensor on the C7 two-qubit Dirac walk vs the C8 metric couplings

**Block:** C10 of `toe-scale-ladder-20261018` (cross-thread target (d)).
**Status:** Reviewed in a separate agent context (same model as the author); unaudited. Review: `REVIEW.md`; dispositions at the end.
**Runners:** `scripts/c10_exact.py` (sympy) and `scripts/c10_numeric.py` (numpy; explicit 4×4
matrices). `scripts/run_all.sh` writes `logs/c10_exact.log` (15/0), `logs/c10_numeric.log` (35/0)
and `logs/run_all.log`, which ends `TOTAL: PASS=50 FAIL=0`. The pre-registration, two debug runs
and the check revisions they caused are recorded in `WORKLOG.md`.

## Result

**Headline (attribution).** BT as defined selects nothing: the C7 walk is outside its domain. With
weak-value odds, BT's plane-wave tensor reduces to the dust tensor ε v v. Any rule whose mean step
equals v gives the same tensor, and the turn mechanics add nothing. The M1 agreement at massless
b_iso therefore tests a property of the walk, v = s⟨α⟩ through O(a²) iff β = 0, not a property of
the turn rule. The agreement also rests on four choices: the 1/s² rescaling (as given, nothing
agrees unless s = 1), the candidate set M1–M4, q = 0 plane waves, and fixing the constant at
continuum order. An energy-dependent factor ∝ sin ω/ω (not a constant) would tie M2.

1. **The burn-and-turn (BT) rule is not defined on the C7 walk.** BT assumes the shift-coin form
   U(k) = diag(e^{−ik·d}) C: each component label carries one hop vector d, which need not have unit
   length (BT's own eight-direction walk uses √3 body diagonals), and the walk moves one link per
   tick. Equivalently, A_n = Π_n C with orthogonal Π_n: the ranks sum to 4 and A_nA_m† = 0. The
   C7 walk has 27 nonzero hop matrices A_n on the 27-point cell, with total rank 92 and overlapping
   ranges. The basis-free overlap max‖A_nA_m†‖₂ is 0.23–0.25, θ-independent (reviewer). The 0.16–0.23
   in my log is a basis-dependent max-element measure. No choice of internal basis brings the walk to
   this form (exact hop decomposition; all three points, massless and massive). The reviewer adds a
   basis-free certificate: ‖[U(k)U(0)†, U(k′)U(0)†]‖ ≈ 1.9 ≠ 0. **Untested:** whether U factors into
   shift-coin sub-ticks. That would be a different tick, outside BT as defined. So "BT exactly as defined"
   has no value here. All later statements use one of two **declared extensions**. Each one
   reduces to BT's Born odds on BT's own walks (checked on BT's 1D and six-direction walks).
   - **E-K (which-hop odds)** P_n = ‖A_n u‖². These are real, non-negative and sum to 1. Their
     mean step is **not** the group velocity. |m| ≈ 0.12–0.16 against |v| ≈ 0.9 (massless). The
     relative deviation is at least 0.63 at every point, for every vector in the band. So
     T^{BT,K} = ε m m disagrees with every coupling **at continuum order**.
   - **E-W (weak-value odds)** w_n = e^{iω}e^{−ik·n}⟨u|A_n|u⟩. These sum to 1 and their mean is
     exactly v. They are **complex and partly negative** (|Im w| up to 0.62, Re w down to −0.68),
     so BT's flows 2εw w′/ρ are not flows. The algebra still gives T^{BT,W} = ε v v exactly.
     Everything below concerns this continuation, that is, the "dust" tensor ε v v.
2. **Exact closed forms** (proved; E2, E3, E4). On the upper band, ⟨α_i⟩ = g_i/|x| for every vector
   of the degenerate band. With D = −∇f = v sin ω, the plane-wave stress tensors are:

   T^{BT,W} = ω D D / sin²ω, T^{M1} = ω g g / sin²ω, T^{M2} = (sin ω/ω) T^{M1},
   T^{M3} = s·sym(g, sin k)/sin ω, T^{M4} = sym(D, sin k)/sin ω.

   **D − λ s g = sin k_a [E₁(x_b + x_c) + E₂ x_b x_c]** (componentwise; x = 1 − cos k), with
   λ = cos θ − sin θ (ĥ·W)/s² and E₁ = −3β cos θ + O(θ). Here β = −s(b₀ − b₁ − 2b₂)/3 is **exactly
   C7's k⁴ cubic-anisotropy coefficient**. Physically, the group velocity equals s times the
   expectation of the Dirac velocity operator α up to a term proportional to β.
3. **Comparison** (registered criteria; "shape" means up to one constant fixed at continuum order):

| | continuum order, as given | continuum order, shape | O(a²), shape (generic direction) |
|---|---|---|---|
| b\*, massless | none (T^BT = s²T^X, s² = 0.836) | all four agree | **none**. M1 mismatch 3β n₁²(n₂²+n₃²)…, β = 0.0403 |
| b_iso, massless | none (s² = 2/3) | all four agree | **M1 only** (next mismatch O(a⁴), coefficient C = (10√10 − 32)/27) |
| b_gold, massless | all four agree (s = 1) | all four agree | **none**. M1 mismatch ∝ β = 7/6 − √5/2 |
| massive, Wilson-aligned (b\*, b_iso) | none | none: O(a) mismatch for all | none |
| massive, maximal twist / b_gold | none (s ≠ 1); all (b_gold) | all | none at the registered constant s² |

   Exact special cases: for k on a lattice axis, T^{BT,W} = s² T^{M1} exactly for every b. At b_iso
   along (111), M3 and M4 also agree through O(a²); only the generic direction (123) separates them.
   In a *secondary, labelled* comparison the constant is allowed to depend on the mass, λ²s².
   Then at b_iso M1 agrees through O(a²) for massive members too (residual O(a³) when
   Wilson-aligned, O(a⁴) at maximal twist). M2–M4 still mismatch at O(a²) or O(a).
4. **Clock** (target 3): **fails, and the failure is not caused by C7's O(a²) anisotropy.** At rest
   the E-K turn action is θ(⟨|n|²⟩_K − |m_K|²), with ⟨|n|²⟩_K = 0.539 (b\*), 0.519 (b_iso) and
   0.640 (b_gold), band- and θ-independent. The E-K rest mean step is not zero (|m_K| ≤ 0.048, a
   spurious rest drift). So action/θ = 0.537 (b\*), 0.518–0.520 (b_iso) and 0.638–0.640 (b_gold). The E-W action is θ(3s² − 3iĥ·W) exactly (E6). Both differ from
   m²/ε = θ at k = 0. From k = 0 to |k| = 0.2 both actions **rise** while m²/ε falls, so the
   rule is not a clock even up to normalisation. The direction dependence of the action at
   |k| = 0.2 is only 5×10⁻⁵–6×10⁻⁴ relative, smallest at b_iso, where β = 0. That is consistent with
   the anisotropy being a sub-leading effect on top of an O(1) failure. As in BT's six-direction case,
   the cause is that the steps' |n|² (here n ∈ {−1,0,1}³, with |n|² from 0 to 3) is unrelated to the
   light speed s.
5. **Coupling** (target 4): BT as defined selects nothing. The plane-wave dust tensor, which equals
   the E-W continuation of BT, agrees with M1 through O(a²) iff β = 0, that is, at massless b_iso,
   at shape level. This does not depend on the turn rule. If M1 is adopted, C8 gives
   c_G^iso(M1, b_iso) = 6.63451×10⁻³ and a/l_P = 0.5775 √N_f (with C8's caveats: anisotropic TT stiffness of 55% at b_iso, the q⁰
   sector, the conformal channel not computed). No new fitting was done. At b\* (c_G = 7.36673×10⁻³)
   nothing is selected.

**Outcome (with scope).**
- *As defined:* BT is inapplicable (domain).
- *E-K extension:* incompatibility at continuum order.
- *E-W continuation, constant as given:* incompatibility at s ≠ 1, non-selection at b_gold
  (continuum order), incompatibility at O(a²).
- *E-W, shape:* non-selection at continuum order. M1 is the only coupling that agrees at O(a²),
  and only at massless b_iso. This is a walk-kinematic match (v = s⟨α⟩), not a selection by the
  turn rule; incompatibility at O(a²) at b\* and b_gold and, at the registered constant, for massive
  members.

## 0. Premises

- C7 P1–P3: two-qubit site (outside the one-qubit axiom; parked owner fork 4, not adopted), the
  Clifford walk family, and the scaling θ = m a. The points b\*, b_iso and b_gold. Mass direction
  χ = 0 (Wilson-aligned) or π/2 (maximal twist). At b_gold W = 0, and χ is a frame label only.
- C8 P4 and its variants M1–M4, each taken as defined in C8 §1. The tree-level stress tensor is
  T^X_ij = −2 ∂⟨u|δH_X|u⟩/∂h_ij at q = 0, with δH = −½h_ij V_ij. This is the same normalisation as a
  dust particle, for which T = E v v/c².
- BT rule (other thread): supplied exchange flow, per-turn stress and ε = band frequency. The
  extensions E-K and E-W are **my declared choices**, not derived.
- Lattice units a = τ = 1. The factor s² in "as given" is unit-invariant: both tensors are energies.
  It reflects that BT measures steps against the lattice cone (1 site/tick), while the metric
  couplings see the Dirac light speed s.

## 1. Domain test (exact certificate)

U(k) = Σ_n e^{−ik·n}A_n with n ∈ {−1,0,1}³. A_n comes from an exact 27-point DFT (U has degree ≤ 1
per axis). The reconstruction, unitarity and Σ A_n†A_n = 1 hold to 2×10⁻¹⁵. The shift-coin form
needs A_n = Π_n C, with orthogonal projectors Π_n: at most 4 nonzero hops, ranks summing to 4, and
A_nA_m† = 0. The C7 walk has 27 nonzero hops (rank sum 92). This holds for all three points and θ.

## 2. The BT identity is algebra

E1 (sympy, arbitrary complex weights, arbitrary step vectors) gives burns + turns = ε m m and
turn action = ε(⟨|d|²⟩ − m·m). So on any walk the BT tensor is ε m m, and the only physics is
whether m = v. E-W gives m = v by first-order perturbation of the eigenphase; E-K does not.

## 3. Exact stress tensors and the β identity

- **E2.** Π = (1 − X/|x|)/2 is the upper band, and ΠΓ_AΠ = −(x_A/|x|)Π. Hence ⟨α_i⟩ = g_i/|x| =
  g_i/sin ω for every band vector, and the coupling tensors are band-independent.
- **E3 (massless, all b).** D₁ − s g₁ = sin k₁[−3β(x₂ + x₃) + C x₂x₃], with
  C = −3b₀b₁ + 2b₀b₂ − 3b₁² + 7b₁b₂ + 5b₂².
- **E4 (massive).** g is mass-independent (MΓ_{3,4,5}M = Γ_{3,4,5}). f_θ = cos θ f₀ − sin θ ĥ·h₀.
  The displayed identity holds with E₁ = −3β cos θ + sin θ(c₂ + c₃ − (ĥ·W)(b₁ + b₂)/s) and
  E₂ = C cos θ − sin θ(c₃ − (ĥ·W)b₂/s), where (c₀..c₃) = ĥ·(h rows of F). This is checked against
  eigenphase finite differences of the explicit 4×4 matrix to 2×10⁻¹⁰.
- **Named points.** b\*: β = 0.040299, C = 0.093899. b_iso: β = 0 and
  C = (10√10 − 32)/27 = −0.013971. b_gold: β = 7/6 − √5/2 and C = (583 − 259√5)/38.
  At b_iso the h row orthogonal to W is ∝ (−1,1,−1,1), so ĥ⊥·h₀ = −c x₁x₂x₃ = O(k⁶) (E5f + numeric).
- **E5b–E5e.** These are the exact κ⁴ mismatch polynomials of M1–M4 against T^{BT,W}/s². All vanish
  at continuum order. The M1 mismatch is 3β·(polynomial in n), for example the xx entry is
  3β n₁²(n₂² + n₃²). M2–M4 are nonzero at all three points along (1,2,3). M3 and M4 vanish at b_iso
  along (111).

## 4. Numerical scaling (k = κn, θ = κμ, κ = 0.08 → 0.01)

The fitted slopes of the relative mismatch were:
- 2.000 for M1 off-axis at b\* and b_gold;
- 3.94–4.06 for M1 at b_iso;
- 2.000 for M2–M4 along (123);
- 1.00–1.03 for every coupling, massive and Wilson-aligned;
- 2.00 for every coupling at maximal twist.

The as-given continuum deviation equals 1 − s² to 2×10⁻³ (0.1638 and 0.3333), and 0 at b_gold.

## 5. Claim types

| claim | type |
|---|---|
| C7 walk outside BT's domain | exact certificate (finite DFT, rank/overlap) |
| E-K, E-W are extensions reducing to BT odds on BT walks | declared construction, plus a numerical check |
| BT = ε m m for any weights; ⟨α⟩ = g/sin ω; D − λsg identity; β-proportional M1 mismatch | proved (exact sympy, all b, θ, ĥ) |
| E-W weights complex, E-K mean ≠ v | numerical (finite sets of points and band vectors) |
| table §Result 3 | exact leading coefficients (massless), plus numerical slopes (massive) |
| clock failure at rest (E6 exact for E-W; E-K numerical), rising trend | exact / numerical |
| relation of clock direction dependence to β | numerical observation, not a theorem |
| c_G, a/l_P | quoted from C8, not recomputed |

## 6. Load-bearing step for independent check

The identity **D − λ s g = sin k_a[E₁(x_b + x_c) + E₂ x_b x_c] with E₁|_{θ=0} = −3β**, together
with **⟨α_i⟩ = g_i/sin ω** on the band. The M1 match at b_iso (a walk property, not a turn-rule selection) rests on these two facts. A
reviewer should re-derive v·sin ω from the walk by a different route (for example from the
eigenvalue of the explicit U at a generic k with exact arithmetic), and should check that β is C7's
anisotropy coefficient. Second item: whether E-W (complex weights) may count as "applying BT" at all.
I classify it as a continuation, not the rule.

## 7. Novelty

Ehrenfest-type relations v = c⟨α⟩ hold in the continuum. As far as I know (from memory, not
searched), the lattice statement (massless members, generic direction) "the group velocity equals s⟨α⟩ through O(a²) iff the k⁴ cubic
anisotropy vanishes" for this family is new. It is specific to the C7/parent family.

## Review dispositions (REVIEW.md)

| item | verdict | disposition |
|---|---|---|
| 1a domain stated as "unit-length" | correct with fix | **applied**: shift-coin form with arbitrary hop vectors; sub-tick factorisation listed as untested |
| 1c overlap 0.16–0.23 basis-dependent | correct with fix | **applied**: basis-free 0.23–0.25 quoted; the reviewer's commutator certificate cited |
| 2, 3, 4a, 4b extensions, identities, comparison numbers | correct (independent 50-digit eigen-route) | none needed |
| 4c "selects M1 at b_iso" attributed to BT | correct with fix (moderate) | **applied**: headline, Result 5 and Outcome reworded. The match is a dust-tensor/walk property (v = s⟨α⟩); it rests on the 1/s² rescaling, the M1–M4 set and q = 0; c_G is quoted only "if M1 is adopted" |
| 5 clock rest formula | correct with fix (minor) | **applied**: action = θ(⟨\|n\|²⟩ − \|m\|²), \|m_K\| ≤ 0.048, b\* value 0.537 |

Logs and runners are unchanged. The runner message "≤ 4 unit-length hops" in `logs/c10_numeric.log`
is superseded by the condition stated above. Its pass/fail outcome does not depend on the unit length.
