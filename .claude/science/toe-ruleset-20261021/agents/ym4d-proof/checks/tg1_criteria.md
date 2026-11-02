# checks/tg1_criteria.md — pre-registered criteria for TGAUGE_PRICE.md, written 2026-10-28 15:31 UTC

**Written BEFORE `checks/tg1_price.py` exists.** Contains **no constant derived in this drive session**:
the only constants appearing below are L = 3, d, k, n = L^k, T, the combinatorial 2d and 2^d of cited
lemmas, and the four rationals of REVIEW_BFT_A_S8 §S8-7 (−1/432, −17/104976, 17/243, −65/26244), which are
an **outside** prior computation from another file and another session, quoted as a reference target and
not derived here.

Exact `fractions.Fraction` / Python ints throughout. Plain `python3 -I`, `nice -n 10`,
`OMP_NUM_THREADS=OPENBLAS_NUM_THREADS=MKL_NUM_THREADS=1`, no numpy, no BLAS, single thread, **no numeric
lock** (DRIVE_BRIEF rule 6 exempts exact rational arithmetic). Target: under 5 minutes and under 500 MB.

## Models

| id | d | k | T | level-0 torus side | what it is for |
|---|---|---|---|---|---|
| **P1** | 2 | 2 | 3 | 27 | all clauses on a full torus |
| **P2** | 2 | 3 | 2 | 54 | the level scaling of clause E (l = 0, 1, 2) |
| **P3** | 4 | 1 | 2 | 6 | all clauses in d = 4 on a full torus |
| **P4** | 4 | 2 | 2 | 18 | clauses A, B, C, D, E and the S8-7 rebuild in d = 4 at k = 2 |

Sources and fields are **pseudo-random** from a fixed linear congruential generator, and **sparse** (a fixed
small number of seeded sites per level), so nothing is tuned to the answer. The root-charge distribution D
is built as a **neutral** (total 0) distribution on the level-k roots, placed so that at least one root with
D ≠ 0 lies in a level-k block meeting the support of the test field x_0 — otherwise the residue would be 0
and every clause would pass vacuously. **Clause Z below tests exactly that non-vacuity.**

## Clauses, with PASS/FAIL fixed in advance

**Z (non-vacuity gate; must be checked first).** The residue 𝒯 := n²Σ_X D(c_X)·Φ_k(x_0)(c_X) is **nonzero**
and the constructed μ is **not** identically zero, in every model. **FAIL if 𝒯 = 0 or μ ≡ 0 in any model**,
in which case every other clause of that model is vacuous and must be reported as vacuous, not as a PASS.

**A (TGAUGE rebuild).** For pseudo-random μ and pseudo-random x_0, at **every** level-k site X of the torus:
Φ_k(x_0 + dμ)(X) − Φ_k(x_0)(X) = A^{(0→k)}μ(X) − μ(c_X), where
A^{(0→k)}μ(X) = L^{−dk}Σ_{s∈[0,L^k)^d}μ(L^kX + s).
**PASS iff exact equality at every X in every model.** FAIL otherwise.
*Tested against:* Proposition TGAUGE (TENTQ §2.7), an outside formula proven in a file this lane did not
write, via two disjoint code paths (forward funnel h_i∘Q_str chain vs plain block average).

**B (the construction).** Two explicit μ are built from a prescribed level-k target ν(X) := −Φ_k(x_0)(c_X):
- **μ_flat**: on each level-k block, the constant (1 − L^{−dk})^{−1}·ν(X) at every fine site of the block
  except its centre c_X, and 0 at c_X;
- **μ_pt**: L^{dk}·ν(X) at the single fine site c_X + e_0 and 0 elsewhere.
**PASS iff, for both μ and every level-k site X: (i) μ(c_X) = 0; (ii) A^{(0→k)}μ(X) = ν(X) exactly;
(iii) Φ_k(x_0 + dμ)(c_X) = 0 exactly.** FAIL if any clause fails for either μ.
*Power:* clause (iii) is an independent consequence of A, computed through the funnel and not through the
block average, so an error in either chain breaks it.

**C (THE PRICE — the decisive clause).** With Ĉ_def := Σ_{i<k}(Q_str^{(0→i)})^T h_i^T R_{i+1}(D) the
regrouping defect of Lemma DF-cc (ii) (†) and 𝒯 as in Z:
- **C1:** n²⟨Ĉ_def, x_0⟩ = 𝒯 exactly — i.e. Proposition COF-res's identity;
- **C2:** n²⟨Ĉ_def, dμ⟩ = −𝒯 exactly, for **both** μ_flat and μ_pt.
**PASS iff both hold exactly in every model.** A FAIL of C2 reverses the session's verdict.
*Tested against:* two disjoint code paths — the left sides run R_{i+1}, h_i^T, (Q_str)^T and d; the right
side runs the forward funnel h_i∘Q_str and the root sum. Neither calls the other and neither is the other's
transpose by construction. C1 is additionally tested against an **outside formula** (BFT_B §35.7).
*Pre-registered reading:* C2 holding for both μ means the exact price of the gauge is **μ-independent** and
equal to the residue removed; C2 failing for one μ and not the other means the price depends on μ and the
verdict must be decided by the optimum instead.

**D (the invariance that forces it).** An explicitly constructed composite-co-closed single-slot source
S_{k−1} = j with D(S) = ev^{(0→k−1)T}d*j **supported on the level-k roots** (a two-root dipole), and
C(j) := (Q_str^{(0→k−1)})^T j − Σ_{i<k−1}(Q_str^{(0→i)})^T h_i^T ev^{(i+1→k−1)T}(d*j) its full push-down
(Proposition RF transposed). **PASS iff all three hold exactly:**
- **D1:** d*C(j) = D(S) (Lemma DF-cc (i)), as level-0 functions, at every site;
- **D2:** D(S) is supported on the level-k roots and Σ_z D(S)(z) = 0;
- **D3:** ⟨C(j), dμ⟩ = 0 for both μ_flat and μ_pt, exactly — equivalently ⟨d*C(j), μ⟩ = 0.
FAIL if any fails. (For k = 1 the inner sum is empty and D is reported as degenerate, not as a PASS.)
*Power:* D1 tests the whole (Q^{(0→l)})^T chain against a closed statement from another file; D3 is the
structural fact that makes the price equal, and the control F below shows it can fail.

**E (the estimator ratio; the isoperimetric clause).** For each μ and each l < k compute exactly
ρ_est(l) := ‖d(A^{(0→l)}μ)‖_1 / [(n/L^l)^{d−1}·osc_1(ν)], osc_1(ν) := max over μ-adjacent level-k root
pairs of |ν(X) − ν(X′)|. **PASS iff: (i) ρ_est(l) ≥ 1 for every l and both μ; (ii) ρ_est(l) ≤ 2d for every
l for μ_flat; (iii) ρ_est(l) ≥ L^{k−l} for every l for μ_pt.** FAIL if any clause is violated at any l.
*Reading fixed in advance:* (i) is the claim that no μ beats the stated total-variation lower bound; (ii)
that μ_flat attains it up to the absolute constant of Lemma TENT-TV; (iii) that μ_pt is worse by exactly a
power of the block side. A FAIL of (i) would refute the lower-bound lemma; a FAIL of (ii) would mean the
flat construction is not optimal.

**F (DESIGNED-FAIL CONTROL 1 — a μ outside Λ_*).** Re-run D3 and C2 with
μ_root := Σ_X (1 − L^{−dk})^{−1}·(−ν(X))·δ_{c_X}, which satisfies TGAUGE's hypothesis but violates
μ(c_X) = 0, so it is **not** an admissible composite gauge shift.
**The control is a PASS of the control iff D3 FAILS for μ_root (⟨C(j), dμ_root⟩ ≠ 0).** If D3 still returns
0, clause D has no discriminating power over the Λ_* constraint and that must be stated.

**G (DESIGNED-FAIL CONTROL 2 — a corrupted block convention).** Re-run clause A with the block average
computed at the wrong root offset (off(k) := 0 in place of (L^k − 1)/2).
**The control is a PASS of the control iff A then FAILS.** If A still passes, the pipeline has no power over
the root/block convention and that must be stated.

**H (reference rebuild).** In model P4 (d = 4, k = 2) recompute, for u := ⅛d*δ_p with p the (0,1)-plaquette
at c_X + (1,0,0,0): φ_1, φ_2, φ_2/φ_1 and Φ_2(u) = φ_1 + φ_2.
**PASS iff all four equal the outside values −1/432, −17/104976, 17/243, −65/26244 exactly.**
*Power:* HIGHEST against a number this lane did not produce; any error in the axial weights, the root
offsets, Q_str, the plaquette convention or the normalisation fails it.

## Scope limitations, stated in advance

1. **No response field is computed.** x_0 is a pseudo-random sparse stand-in and u is the explicit witness
   field; neither is Y^p_{*,0}. Every statement about Y^p_{*,0} inherits the profile input as a named
   hypothesis.
2. **Nothing nonabelian, nothing at a background, nothing at m > 0 or θ > 0.** The scalar model is complete
   for the identities tested (all operators act componentwise on su(N) at the trivial background) and would
   be vacuous for a background statement; none is made.
3. **k ≤ 3, T ≤ 3.** A level count cannot be measured here and none is claimed. Clause E's scaling in l is
   measured at k = 3 in d = 2 only.
4. **The residual terms ⟨·, r_m(Y^p)⟩ of Theorem COF step (c) are not computed.** They are not inert under
   the shift, and any change in them is additional cost; this is a one-sided limitation.
5. **No claim about (NC-Γ)'s k-uniformity** (RS10-1 stands), and (NEUT-box) is not used.
