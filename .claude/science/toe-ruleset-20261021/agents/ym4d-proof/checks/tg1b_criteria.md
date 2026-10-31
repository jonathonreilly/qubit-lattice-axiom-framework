# checks/tg1b_criteria.md — repair round, written 2026-10-28 ~15:35 UTC

*(Timestamp correction, disclosed rather than silently fixed: this header was first typed as "15:40 UTC",
which is wrong — that is later than the run. `tg1_price.py` ran at 15:33:16 UTC, this file was written after
that and before `tg1b_ledger.py` ran at 15:36:14 UTC, so the true time is ≈ 15:35 UTC and the required
ordering — criteria written **before** the script — is intact and verifiable from the two run clocks.)*

**`checks/tg1_criteria.md` is NOT amended and `checks/tg1_price.py`, `tg1_out.txt`, `tg1_err.txt` are kept
unaltered with their FAILs.** This is a **new id** with its own criteria, written **before**
`checks/tg1b_ledger.py` exists.

## The three tg1 FAILs this round repairs, declared before any new number is produced

1. **Z/P1, Z/P3, Z/P4 FAIL** (𝒯 = 0 for the "generic" field). Cause: `tg1_price.py` placed the root charge
   at the two level-k roots X0, X1 **without** checking that Φ_k(x0) ≠ 0 there, which the tg1 criteria had
   required in words ("placed so that at least one root with D ≠ 0 lies in a level-k block meeting the
   support of the test field x_0"). The script did not implement its own criterion. Consequence, as the tg1
   criteria pre-registered: **every generic-field clause of P1, P3 and P4 is VACUOUS, not a PASS** — in
   particular C1, C2 and F there. The non-vacuous tg1 results are P2's generic field and all four models'
   one-block field.
2. **F/P1, F/P4 FAIL** — consequential on 1 (μ_root's value at the charged roots is proportional to ν there,
   which was 0).
3. **E-ii-flat FAILS in all four models** (ρ_est(l) > 2d). The criterion was **wrong**, and only "≤" with a
   k-dependent factor is derivable. **Derived analytically here, before the script, and independently of
   tg1's output:** for a ν supported on a single level-k box X, μ_flat = s·ν on the block minus its centre
   with s := (1 − L^{−dk})^{−1}, so A^{(0→l)}μ_flat equals s·ν on every level-l site of the block except the
   one containing c_X, where it is s·ν(1 − L^{−dl}). Its level-l total variation is therefore
   **2d(n/L^l)^{d−1}·s|ν| across the 2d block faces, plus 2d·L^{−dl}·s|ν| across the root hole**, so with
   osc_1(ν) = |ν|:
   **ρ_est(l) = 2d·(1 − L^{−dk})^{−1}·(1 + L^{−l}·n^{1−d}) exactly**, which exceeds 2d by a factor that
   tends to 1 as k → ∞ and is never more than 2d·(1 + L^{−l}n^{1−d})/(1 − L^{−dk}).
   For μ_pt = L^{dk}ν·δ_{c_X+e_0}: A^{(0→l)}μ_pt = L^{d(k−l)}ν at one level-l site and 0 elsewhere, so
   **ρ_est(l) = 2d·L^{k−l} exactly**.

## What tg1b adds beyond the repair: the ledger is closed on ONE source

tg1 computed the regrouping defect Ĉ_def from a root charge D chosen independently of the clause-D source
j, so its clause C2 measured only ⟨Ĉ_def, dμ⟩ — **part** of ΔM, not ΔM. tg1b uses **one** source throughout:
j a level-(k−1) current whose composite divergence D(S) is a two-root dipole on the level-k roots; then
- **C(j)** := (Q_str^{(0→k−1)})^T j − Σ_{i<k−1}(Q_str^{(0→i)})^T h_i^T ev^{(i+1→k−1)T}(d*j)  (Proposition RF transposed),
- **Ĉ_def** := Σ_{i<k}(Q_str^{(0→i)})^T h_i^T R_{i+1}(D(S))  (the Lemma DF-cc (ii) defect),
- **Ĉ** := C(j) + Ĉ_def = Σ_l(Q_str^{(0→l)})^T ĵ_l  (identity (†)),
- **P** := n²⟨C(j), x_0⟩ (the whole of Theorem COF step (c)'s first term, the gauge-invariant quantity),
- **M** := n²⟨Ĉ, x_0⟩ (the regrouped main term that Theorem COF estimates),
- **𝒯** := n²Σ_X D(S)(c_X)·Φ_k(x_0)(c_X) (Proposition COF-res's residue).

## Clauses, PASS/FAIL fixed in advance

Models: **Q1** (d = 2, k = 2, T = 3), **Q2** (d = 2, k = 3, T = 2), **Q3** (d = 4, k = 2, T = 2). Fields:
`one-block` (support inside the level-k block carrying the + charge) and `mixed` (that, plus generic sparse
pseudo-random links elsewhere). Exact Fractions, plain `python3 -I`, `nice -n 10`, one thread, no numpy/BLAS,
no numeric lock.

**B0 (non-vacuity).** 𝒯 ≠ 0, D(S) ≠ 0, μ_flat ≠ 0, μ_pt ≠ 0, in **every** model and **both** fields.
**FAIL if any is zero**, and then every clause of that model/field is vacuous.

**B1 (the closed ledger).** PASS iff all five hold **exactly** in every model and both fields:
(i) d*C(j) = D(S); (ii) D(S) is supported on the level-k roots and sums to 0;
(iii) **M = P + 𝒯**; (iv) for μ ∈ {μ_flat, μ_pt}: **ΔP := n²⟨C(j), dμ⟩ = 0**;
(v) for μ ∈ {μ_flat, μ_pt}: **ΔM := n²⟨Ĉ, dμ⟩ = −𝒯**, i.e. **ρ := |ΔM|/|𝒯| = 1**.
*Tested against:* Lemma DF-cc (i) and (†) and Proposition COF-res, three closed statements from another
file; and two disjoint code paths for 𝒯 (forward funnel + root sum) versus ΔM (R_{i+1}, h^T, Q_str^T, d).
*Reading fixed in advance:* (v) with (iv) is the verdict **EQUAL**, exactly and μ-independently. If (v)
fails for one μ and holds for the other, the price depends on μ and the verdict is decided by the optimum.

**B2 (DESIGNED-FAIL CONTROL 1 — the price of an inadmissible μ).** With
μ_root := −s·ν(X)·δ_{c_X} summed over X (TGAUGE-admissible, **not** in Λ_*):
**the control FIRES (= PASS of the control) iff BOTH ΔP ≠ 0 AND ρ_root := |ΔM|/|𝒯| ≠ 1.**
If ρ_root = 1 as well, then clause B1 (v) does not distinguish admissible from inadmissible shifts and has
no power over the Λ_* constraint; I will say so.

**B3 (the estimator, repaired).** For the `one-block` field: PASS iff
(i) ρ_est(l) = 2d·(1 − L^{−dk})^{−1}·(1 + L^{−l}·n^{1−d}) **exactly** for μ_flat at every l < k;
(ii) ρ_est(l) = 2d·L^{k−l} **exactly** for μ_pt at every l < k;
(iii) ρ_tv(l) := ‖d(A^{(0→l)}μ_flat)‖_1 / ‖d(ev^{(0→l)}I_χν)‖_1 satisfies 1 ≤ ρ_tv(l) ≤ 2 and is
**decreasing in k** at fixed l (compare Q1 against Q2 at l = 0, 1).
FAIL if any clause fails. *Note:* the closed forms in (i)-(ii) are derived analytically above, before the
script; that they also match tg1's printed numbers is **disclosed and post-hoc**.

**B4 (TP-F6, the SOURCE-DISAGREES clause).** For pseudo-random μ and every 0 ≤ l < k:
(i) **Q_str^{(0→l)}(dμ) = d(A^{(0→l)}μ)** exactly, at every level-l link;
(ii) **Q_str^{(0→l)}(dμ) ≠ d(ev^{(0→l)}μ)** for at least one l ≥ 1 and at least one link.
PASS iff both. *If (ii) fails, TENTQ §2.7's displayed chain is right and my TP-F6 is wrong, and I will say
so.* Clause (ii) is skipped at l = 0, where A^{(0→0)} = ev^{(0→0)} = id and the two agree trivially.

**B5 (DESIGNED-FAIL CONTROL 2 — a corrupted straight average).** Replace the straight average's
longitudinal multiplicity table t ↦ L − |t − (L−1)| by the flat table t ↦ 1, and assert the kernel mass
Σ_t mult(t) = L² before use. **The control FIRES iff the mass assertion rejects the corrupted table AND
clause B4 (i) then FAILS.** If B4 (i) still passes under the corruption, the pipeline is insensitive to the
one feature the straight average turns on and I will say so.

## Scope limitations (unchanged from tg1_criteria.md, restated)

1. No response field: x_0 is a pseudo-random stand-in, not Y^p_{*,0}.
2. Nothing nonabelian, nothing at a background, nothing at m > 0 or θ > 0.
3. k ≤ 3; no level count is measured and none is claimed.
4. The ⟨·, r_m(Y^p)⟩ residual terms of Theorem COF step (c) are **not** computed; any change in them is
   additional cost, so this limitation is one-sided (it can only move the verdict towards WORSE).
5. No claim about (NC-Γ)'s k-uniformity; (NEUT-box) is not used.
