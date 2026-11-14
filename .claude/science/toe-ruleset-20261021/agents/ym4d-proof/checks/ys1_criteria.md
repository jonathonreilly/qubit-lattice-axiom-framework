# ys1 criteria — written 2026-10-28 14:54 UTC, BEFORE `ys1_funnel.py` exists

Pre-registered PASS/FAIL verdicts for the YSUP session-25 check battery. **No constant appearing below is
derived in this session.** The only numbers quoted are (a) powers of L and of n_i, (b) closed forms quoted
from other files, and (c) four exact rationals produced by REVIEW_BFT_A_S8 (a *prior* session) and rebuilt
in TENTQ (also prior to this file): φ_1 = −1/54, φ_2 = −17/13122, φ_2/φ_1 = 17/243, ψ_u = −65/26244, for the
**unnormalised** u = d*δ_p (ψ_u for u/8), p the (0,1)-plaquette at c_X + (1,0,0,0), k = 2.

Environment, committed in advance: exact arithmetic only (`fractions.Fraction` and Python ints), plain
`python3 -I`, `nice -n 10`, `OMP_NUM_THREADS=OPENBLAS_NUM_THREADS=MKL_NUM_THREADS=VECLIB_MAXIMUM_THREADS=1`,
`PYTHONDONTWRITEBYTECODE=1`, no numpy, no BLAS, single thread, **no numeric lock** (DRIVE_BRIEF rule 6
exempts exact rational arithmetic). d = 4, L = 3, roots at off(l) = (L^l − 1)/2 + L^l·Z^d.

## The two objects under test

- **LI_i** ("block-averaged axial line integral"): (Q_str^{(0→i)}v)(ℓ) at the level-i link ℓ nearest p, with
  (Q_str v)(Y,m) = L^{−d}Σ_{r∈[0,L)^d}Σ_{j<L}v_m(LY + r + je_m) as quoted from BFT_B §27.1.
- **BA_i** ("full normalised block average"): n_i^{−d}Σ_{|z−p|_∞≤(n_i−1)/2}v(z), n_i = L^i.

## The test field

`v^+(b) := L^{−3·j(|b − p|_∞)}`, `j(s) := min{ j ≥ 0 : L^j ≥ 1 + s }` — the exact L-adic **lower** staircase
of the admissible profile (1 + |b − p|_∞)^{−3} of BFT_A §38.7. Pre-registered properties, to be verified by
the script as **A0** (FAIL the whole battery if either fails):
- (A0a) v^+(b) ≤ (1 + |b − p|_∞)^{−3} ≤ L^3·v^+(b) for every b in the test range — so v^+ is admissible with
  C_0 = 1 and brackets the true profile within the **constant** L^3, i.e. every *ratio* computed from v^+
  equals the corresponding ratio of the true profile up to that constant and every *power* is exact;
- (A0b) v^+ is exactly L-scale-covariant: v^+(s) = L^{−3}·(the staircase at s/L) on the staircase steps.
**Scope limitation, stated in advance:** v^+ is a positive scalar profile, not co-closed and not a response
field. It is used **only** to measure the power of n_i in LI_i and BA_i (target Y2). No statement about
Y^p_{*,0} itself is to be read off A4.

## Checks and pre-registered verdicts

**A1 (rebuild of the outside numbers).** Re-implement the axial weights of h_i and Q_str from the
definitions quoted above and in YSUP §1.0, then compute, at k = 2 with c_X = (4,4,4,4) and p the
(0,1)-plaquette at c_X + (1,0,0,0): φ_1 := h_0(u)(Y_1), φ_2 := h_1(Q_str u)(Y_2), ψ_u := (φ_1 + φ_2)/8.
- **PASS** iff φ_1 = −1/54, φ_2 = −17/13122, φ_2/φ_1 = 17/243 and ψ_u = −65/26244, **all four exactly**.
- **FAIL** otherwise. A FAIL voids every analytic statement in YSUP that uses the funnel weights.
*Tested against:* an independent prior computation in another file and another session.
*Power:* **HIGHEST against an outside number.**

**A2 (kernel support, sup, ℓ¹ — against closed forms).** Build K_i := (Q_str^{(0→i)})^T h_i^Tδ_X explicitly
for i = 0, 1 and by streaming for i = 2, on a **disjoint code path** from A1 (transpose, not forward).
- **PASS** iff all three hold for every i tested: (a) every nonzero K_i(b) has both endpoints of b inside
  the level-(i+1) block of c_X (Lemma FT (i)'s "paths stay inside the block", BFT_B §29.2); (b)
  max_b|K_i(b)| ≤ L^{i(1−d)}; (c) Σ_b|K_i(b)| = L^i·L^{−d}Σ_{y∈B}|y − c_X|_1, the closed form of
  Lemma FT (i) composed with the ℓ¹ gain L of one Q_str^T step.
- **FAIL** if any clause fails. A FAIL of (b) or (c) voids the analytic level-i bound of target Y2.
*Tested against:* two closed forms quoted from BFT_B §29.2, neither produced here.
*Power:* **MEDIUM-HIGH.** A wrong Q_str^T, a wrong off(l), or a wrong block convention fails it.

**A3 (the two paths agree).** ⟨K_0, u⟩ and ⟨K_1, u⟩ against A1's φ_1 and φ_2.
- **PASS** iff both agree exactly. **FAIL** otherwise.
*Power:* **MEDIUM-HIGH.** The forward and transpose paths share no code; neither is the other's transpose
by construction.

**A4 (THE DISCRIMINATING CHECK: the power of n_i in the averaging).** Compute LI_i and BA_i on v^+ exactly
for i = 0, 1, 2, 3, and the ratios r^{LI}_i := LI_{i+1}/LI_i, r^{BA}_i := BA_{i+1}/BA_i. For each ratio put
ρ := −log_L r. Pre-registered, mutually exclusive bands, applied **separately** to LI and to BA:
- **verdict (V-2)** if every ρ in the family lies in **[1.5, 2.5)** — the averaging gains n_i^{−2};
- **verdict (V-3)** if every ρ lies in **[2.5, 3.5)** — the averaging gains n_i^{−3};
- **verdict (V-other)** if any ρ lies outside [1.5, 3.5), or the family straddles the two bands: the
  criteria are then declared **inadequate** and the analytic claim is reported as unsupported.
Pre-registered expectation (YSUP §1.2, YS-F1): **LI → (V-2)** and **BA → (V-3)**. This check decides the
brief's question and **can come out either way**; if LI lands in (V-3) the averaging beats the core by one
more power than expected and the verdict of this session reverses.
*Power:* **HIGH, and it is the check the session's conclusion turns on.*
*Independent construction it is tested against:* BA_i, computed from the same data by a different operator —
so the instrument is shown to be able to read **both** bands (see A8).

**A5 (TGAUGE identity — an outside formula with no free parameter).** By Proposition TGAUGE (TENTQ §2.7,
proven there and not re-judged here), Φ_k(dμ)(X) = A^{(0→k)}μ(X) − μ(c_X). With μ = δ_{c_X} this predicts
**Φ_k(dδ_{c_X})(X) = L^{−dk} − 1** exactly.
- **PASS** iff the pipeline returns exactly L^{−dk} − 1 at k = 1 and k = 2. **FAIL** otherwise.
*Power:* **HIGH against an outside formula.* A wrong root offset, a wrong level count, a wrong block
convention or a telescoping error each fail it, and the predicted value is not a constant of this session.

**A6 (the k-uniform lower bound).** At k = 3, c_X = (13,13,13,13), p the (0,1)-plaquette at c_X + (1,0,0,0):
compute φ_1, φ_2, φ_3 exactly, and the tail bound 𝔗 := ‖u‖_1·Σ_{i≥3}L^{i(1−d)} = ‖u‖_1·L^{3(1−d)}/(1 − L^{1−d}).
- **PASS** iff (a) φ_1 and φ_2 at k = 3 equal φ_1/8 and φ_2/8 of A1 (the admissible normalisation) exactly —
  level/translation covariance; and (b) |φ_1 + φ_2 + φ_3| > 10·𝔗, so that no tail can cancel the head.
- **FAIL** if either fails; (b) failing means no k-uniform lower bound is established and YS-F3 occurs.
*Power:* **HIGH for (a)** (a wrong off(3) fails it); **MEDIUM-HIGH for (b)**.

**A7 (DESIGNED-FAIL CONTROL — the battery must be able to fail).** Re-run A1's computation with exactly one
deliberate error: off(l) := 0 (block **corner** instead of block centre), everything else untouched.
- **PASS of the control** iff the control **FAILS A1's verdict**, i.e. returns φ_1 ≠ −1/54.
- If the control reproduces −1/54, then **A1 cannot fail**, and every analytic statement in YSUP resting on
  A1-A3 is to be reported as unsupported.
*Power:* this check **is** the power measurement.

**A8 (DESIGNED CONTRAST — the band test must be able to read both answers).** A4 is accepted as
discriminating only if LI and BA land in **different** bands. If both land in the same band, A4 is reported
as non-discriminating regardless of which band that is.

## What this battery cannot test, stated in advance

1. **Nothing here is nonabelian.** h_i, Q_str, ev and d act componentwise on su(N) in an orthonormal basis at
   the trivial background (BFT_B §24.0, §16.1 (f)), so a scalar model is a *complete* test of these
   identities; it is **vacuous** for any statement at a nontrivial background, and none is made.
2. **No response field is computed.** v^+ is a profile stand-in and u = ⅛d*δ_p is a source. Whether
   Y^p_{*,0} actually has the |z|^{−3} core is a **named input** (BFT_A §38.7, Theorem YH's 𝒩 ≍ n) and is
   not tested here.
3. **No level-count statement.** k ≤ 3; a factor k cannot be measured at k ≤ 3, and nothing here is evidence
   about the upstream factor k that REVIEW_BFT_B_S9_S10 RS10-1 establishes.
4. **λ^E is not computed.** Any statement about the box-dipole face (YS-F5) is analytic, not checked, and
   will be labelled ARGUED.
