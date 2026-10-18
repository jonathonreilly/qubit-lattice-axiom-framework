# C7 review: massive continuum limit of the 3D two-qubit Dirac walk

**Reviewer provenance.** Claude Code subagent, model `claude-opus-5-5` (Opus 5.5). This
context did not write C7. It may share a model family with the author, so treat the
review as *independent-code, not independent-lineage*. The reasoning-effort setting
was not visible to the reviewer.
**Read:** NOTE.md, WORKLOG.md, scripts/c7_exact.py, scripts/c7_numeric.py, logs/*,
the parent note `docs/TWO_QUBIT_SITE_UNFREEZES_..._2026-10-16.md` (Theorem 7 and the
claim scope), and `omega2_series` together with the b_iso sextic check in
`scripts/two_qubit_cubic_dirac_tick_2026_10_16.py`.
**Reviewer evidence** (one core, nice 10, each run under 2 min):
- `review_scripts/r1_exact.py` writes `review_scripts/r1_exact.log` and ends with **TOTAL: PASS=18 FAIL=0** (sympy).
- `review_scripts/r2_numeric.py` writes `review_scripts/r2_numeric.log` and ends with **TOTAL: PASS=37 FAIL=0** (numpy/mpmath).

The independent routes differ from the author's in these ways:
- **Walk construction.** The reviewer builds the walk from G(b) by SVD and a Householder
  alignment. The author uses eigh and QR.
- **Generator.** The reviewer takes the generator from eigenphases on a QR-orthonormalised
  eigenbasis. The author uses a Schur log.
- **O(a) term.** The reviewer derives it by a direct matrix-log series
  log(1+E) = E − E²/2 + E³/3 of M U₀ M. That route does not use the O(3)-rotation identity
  or the ω/sin ω prefactor.
- **|W|.** The reviewer derives |W| from the axis doubler and unitarity, not from the
  Gram quadratic form.
- **Sextic coefficients.** The reviewer obtains them by an 80-digit polynomial fit, with no
  lower-order terms subtracted.

## Verdicts

| # | Claim | Verdict | Severity |
|---|---|---|---|
| 1 | Theorem B O(a) term (a/2)\|p\|² W·τ, signs α = −τ₃σ, β = −ĥ·τ, \|W\| = s√(1−s²); twist dichotomy | **correct** | none |
| 2a | Lemma V: extrema of f, so min ω and min(π−ω), sit at TRIMs; global dispersion bound; doubler separation bounds | **correct** | none |
| 2b | Lemma V item 1: "every node of every member lies at a TRIM" | **correct with fix** | minor |
| 3 | Theorem C (strong convergence, rate, items 3–5) | **correct with fix** (labelling and quantifiers) | minor |
| 4 | Parent runner defect: 8/45 → 4/45; x(s) → s²(4s⁴−5s²+2)/360; 1/243 → 1/1215 | **correct** (the parent is in error) | moderate, for the parent |
| 5 | Lorentz coefficients β = +0.0403/0/0.0486; speeds 0.914/0.816/1; axis vs diagonal quartics; −(s²/3)m²p² | **correct** | none |

### 1. O(a) term and twist dichotomy: correct

**Independent derivation** (r1, part B). U₀ is fixed through O(a²) by three inputs:
- φ(ak) = φ₀ − (a²|p|²/2)w + O(a⁴), checked;
- Cφ₀ = 0;
- O(k²) unitarity, which forces Gφ₀·w = s².

These give U₀ = (1 − s²a²p²/2) + i(−(a²p²/2)W·τ + s a τ₃σ·p). Take M = e^{iamτ₁/2} to
O(a²) and expand log(MU₀M) directly. The result is
H_a = sα·p + mβ + (a/2)|p|² W·τ + O(a²), with α = −τ₃σ and β = −τ₁ = −ĥ·τ. This is exact
symbolic equality at O(a⁰) and O(a¹). Every sign matches the note.

**|W| by a different route.** φ(X) = φ₀ − 2w exactly, so h(X) = −2W. At X we have g = 0
and f_X = 1 − 2s². Unitarity then gives |W|² = (1 − f_X²)/4 = s²(1 − s²). This also proves
the "pinned to the axis-doubler gap" remark. It was cross-checked as a polynomial
identity in G(b).

**Twist dichotomy.** The square (H_D + (a/2)p²W·τ)² equals
[E² − a m|W|cos χ p² + a²|W|²p⁴/4]·1 (exact). At maximal twist, Γ⊥ = τ₂ anticommutes with
α and β. βΓ⊥ is anti-Hermitian, squares to −1 and commutes with α. The rotation
exp((φ/2)βΓ⊥) maps mβ + εΓ⊥ to √(m²+ε²)β exactly. For cos χ ≠ 0 the eigenvalue shift is
−a m|W|cos χ p²/(2E) (exact).

**Numerical confirmation** (r2). A Richardson extraction of the O(a) coefficient of the
true log H_a equals +(1/2)|p|²W·τ at relative error ≤ 2e-6. This holds at b* and b_iso
for χ = 0, 1, π/2. The eigenphase matching distance of U^n against e^{−itH_D} scales as
a^1.01 at χ = 0 and a^2.00 at χ = π/2. That distance is a lower bound for *every*
unitary identification, so the irremovability claim is confirmed.

### 2a. Lemma V and doubler bounds: correct

f = row·φ(c) is multilinear (r1). An affine function on each coordinate line reaches its
max and min over the box at vertices, and the vertices are the 8 TRIMs including Γ.

**The dispersion-bound proof is sound.** D(x) is multilinear in x_a = 1 − c_a ∈ [0,2], with
D(0) = 0 because f(Γ) = cos θ. By the definition of c_θ, D ≥ 0 at every other vertex, so
D ≥ 0 on the whole box.

**Corollaries check out.** |k_a| ≥ π/2 gives 1 − cos k_a ≥ 1, hence ω ≥ arccos(1 − c_θ).
Using 1 − cos x ≥ 2x²/π², the bound E ≤ Λ gives |p| ≤ (π/2)√((Λ²−m²)/c_θ)(1 + O(a²)).

**Other items check out.**
- The S³ bi-invariance bound |ω_K(θ) − θ_K| ≤ θ holds: d(MUM, U) ≤ 2 d(M, 1) = θ.
- The Gaussian tail 3 erfc(√2κΣ/a) is right: σ_p = 1/(2Σ).
- U_θ(X) = −U_θ(0) at b_gold holds (r2, err 3e-15).

**Independent numbers** (r2):
- The TRIM angles at b*, b_iso and b_gold match the table to 1e-3.
- c₀ = 0.2644, 0.3184 and 0.2956 are reproduced.
- On a 33³ grid, max f and min f equal their TRIM values, and the off-Γ gap bound holds.

### 2b. "Every node of every member lies at a TRIM": correct with fix

Multilinearity proves that the *extremal values* are attained at vertices, not that they
are attained *only* there. Suppose f = 1 at a non-vertex point. Then f is constant along
each coordinate line through the point's interior coordinates. So at least two TRIMs that
differ in one coordinate are both nodes of the same type, and the whole edge between them
is nodal.

**Fix.** Add the hypothesis: "provided no two TRIMs adjacent on the cube (differing in one
k_a) are both ω = 0, or both ω = π, nodes. Otherwise the nodal set contains the edge
between them." All three named points satisfy this:
- at b*, b_iso and b_gold only Γ has f = 1;
- at b_gold the f = −1 set is the three X points, and these pairwise differ in two
  coordinates.

So every concrete statement in §2 and §5 stands. Only the "every member" generality
needs the caveat. A moving member (s ≠ 0) cannot have f = 1 at both Γ and X, but
pairs such as M–R are not excluded by the note.

### 3. Theorem C: correct with fix

**Item 1 (strong convergence) is correct as proved.** The fibrewise bound is
a‖H_a‖ + t‖H_a − H_D‖ → 0 for fixed p. The supremum over t ∈ [0,T] is taken inside the
integral and dominated by 4, and P_a → 1. None of this uses the value of C₃.

**Theorem B remainder.** The existence of C₃ and κ₀ with
‖R_a‖ ≤ C₃a²(|p|+m)³ on a(|p|+m) ≤ κ₀ is proved. a·H is jointly real-analytic in
(k, θ) = a(p, m). Its degree-2 part is exactly (k²/2)W·τ: there is no θ² or θk term,
because sin θ·f₀ = θ + O(3) and g is θ-independent. Homogeneity then gives the a²(|p|+m)³
form, uniformly in m.

**Fixes:**
- **(i)** Items 2–4 are proved only as "there exist C₃, κ₀ > 0 such that…". The quoted
  C₃ ≈ 0.042, 0.033 and 0.051 are maxima over 120 sampled momenta with |p| ≤ 2, m = 1,
  a ≤ 0.04, that is, a(P+m) ≤ 0.12. They are *lower estimates of the sup on that
  sample*, not bounds, and κ₀ has no value at all. State this explicitly next to the
  inequality in item 2. The §10 table is already close to this, but the inequality in
  §4 reads as if quantified. Severity: minor.
- **(ii)** Item 5 cites Bauer–Fike. For unitary matrices the clean statement is the
  matching-distance bound (Bhatia–Davis). In either form the lower bound
  |e^{−itE_a} − e^{−itE}| holds only away from the aliasing set where e^{−itE_a} comes
  near e^{+itE}, that is, where sin(tE) ≈ 0. Add "for t with |sin tE| bounded away from 0
  (in particular, in sup over t ∈ [0,T])". Severity: low.
- **(iii)** Item 4's identification V_a(p) is a different, p-dependent map, with
  ‖V_a − 1‖ = O(ap²/m), and the rate is not uniform as m → 0. The note already says
  this. No change is needed beyond keeping "O(a) removable *by a p-dependent
  identification*" wherever item 4 is summarised. The bare error stays O(a), at slope
  1.00 in the author's log.

### 4. Parent runner defect: correct; the parent is wrong

**The coefficient.** arccos(1−u)² = 2u + u²/3 + **4/45**·u³ + O(u⁴) (r1, sympy series).
The parent's 8/45 is the y⁶ coefficient of arcsin(y)², quoted without the rescaling
arccos(1−u)² = 4 arcsin²(√(u/2)) (r1).

**The k⁶ correction.** The u³ term contributes to k⁶ only through (s²k²/2)³, which is
isotropic. The shift in x is (4/45)(s²/2)³ = s²·4s⁴/360. So
x = s²(8s⁴−5s²+2)/360 becomes s²(4s⁴−5s²+2)/360. At s² = 2/3, x goes from 1/243 to
1/1215 (exact). y = −s²/360 and z are unchanged.

**Independent confirmation** (r2, 80 digits). A 6-term polynomial fit in k² of arccos²(f)
at b_iso was made along (1,0,0), (1,1,0) and (1,1,1), with no assumed lower terms
subtracted. It gives k² = 2/3 and k⁴ = −1/54. The k⁶ coefficient matches the corrected
formula (1/1215 − N₄/540 + zP₂₂₂) to better than 1e-20 and misses the parent's by more
than 1e-3. The three directions determine x, y and z, so the corrected sextic is fully
confirmed, and so is the parent's y and z.

**Why the parent's check passes.** Both its target and its series carry 8/45.

**Fix in the parent (on main, not done here):**
- set the coefficient to `4 * uu ** 3 / 45` in `omega2_series`;
- change the target to `sp.Rational(1, 1215)`;
- in Theorem 7 of the parent note, replace `8 s^4` with `4 s^4`;
- add the b_iso value 1/1215 if it is stated anywhere.

The parent's "independent check B5" should be re-read to see whether it actually checked
x. The parent text says only that it agreed on y.

### 5. Lorentz-violation data: correct

From r2, using Richardson in k² on the massless ω²:

| point | β | quartic coefficient along the axis | along the body diagonal |
|---|---|---|---|
| b* | 0.04030 | −0.01142 | −0.03828 |
| b_iso | 0.00000 | −0.01852 = −1/54 | −0.01852 |
| b_gold | 0.04863 = 7/6 − √5/2 | −0.0000 | −0.03242 |

- **Speeds:** s = 0.9144, 0.8165 and 1.0000.
- **New massive term:** the θ²k² coefficient of ω² at b* is −0.2787, against −s²/3 = −0.2787.

All values match the note.

## Items not independently checked
- The Weyl-index signs (det J_K) and the degree-zero sum.
- Lemma P and the Poincaré-defect slopes in §7.
- The literature characterisations in §8, which the author read as abstracts only.

None of these is load-bearing for claims 1–5.

## Requested edits to NOTE.md (author to apply)
1. §2 Lemma V item 1: add the adjacency hypothesis from 2b.
2. §4 item 2: state that "C₃, κ₀ exist" is proved, while the C₃ values are sampled lower
   estimates and κ₀ is unquantified.
3. §4 item 5: replace Bauer–Fike with the unitary matching-distance bound, and add the
   non-aliasing qualifier.
4. §9: leave as is. It is confirmed. Optionally note the arcsin² origin of the 8/45.
