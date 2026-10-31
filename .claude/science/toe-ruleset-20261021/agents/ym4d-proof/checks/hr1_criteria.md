# checks/hr1_criteria.md — pre-registered criteria for the (HESS-rel) currency test

Written **2026-10-28 21:44:36 UTC**, after `HESSREL.md` §H0 (PRE-STATED) and **before any script exists**
(`checks/hr1_flat.py` does not exist at the time of writing). Contains **no constant derived in this
session**. Verdicts below are binding; a failed gate is reported as a FAIL.

## What is being tested, and why it can decide

`NBG_A.md` §A4.3's **(HESS-rel)** asserts a bound of the form

> `‖Hess𝔉_k(Z(V)) − Hess𝔉_k(1)‖_{𝔐→Y} ≤ C f_k ‖Hess𝔉_k(1)‖_{𝔐→Y}`,  `C = C(N, L, κ_±)`,

i.e. the Hessian difference is controlled by the background **curvature** `f_k`. The leading term of that
difference, in the level-0 Wilson block, is `d_Z^*d_Z − d^*d` (the Hessian of `S_W(U_0)` at `U_0 = e^{x}Z_0`;
`𝔉_k` defined at PROOF.md l.6605, its quadratic part at PROOF.md l.6613).

A bound by `f_k` must be **exactly zero** when `f_k` is **exactly zero**. There exist backgrounds with
`f ≡ 0` and `Z ≠ 1`: the pure gauges `Z(b) = G(y)G(y')^{−1}` of Lemma CONJ (BFT_B.md l.4517). So the test
is decidable by exact arithmetic and could come out either way.

## Objects (all pre-session definitions)

- `d_Z` on 0-forms: `(d_Zλ)(b) = Ad_{Z(b)}λ(y') − λ(y)` for `b = (y → y')` — BFT_B.md l.4521.
- `d_Z` on 1-forms, plaquette `p` at `z`, directions `μ < ν`, far corner `c = z + e_μ + e_ν`:
  `(d_Zu)(p) = u(z,μ) + Ad_{Z(z,μ)}u(z+e_μ,ν) − Ad_{Z(z,ν)}u(z+e_ν,μ) − u(z,ν)` — the expansion used in
  BFT_B.md l.4535's proof.
- `U_1 := Ad_{Z(z,μ)}Ad_{Z(z+e_μ,ν)}`, `U_2 := Ad_{Z(z,ν)}Ad_{Z(z+e_ν,μ)}` — BFT_B.md l.4533.
- Exactness defect **B1**: `(d_Zd_Zλ)(p) = (U_1 − U_2)λ(c)` — BFT_B.md (41.1), l.4534.
- Root-covariance defect **B2**: `(Row_l(Y,μ) − Ad_{Z_{l+1}(Y,μ)})lam_{l+1}(Y + e_μ)` — BFT_B.md (41.3), l.4543.
- `d^*` is the transpose of `d` in the `Ad`-invariant inner product (BFT_B.md l.4536 uses
  `d_Z^*d_Z^* = (d_Zd_Z)^T`).

## Setting (fixed before the script)

A periodic `T × T` lattice, `T = 8`, structure group `SU(2)` acting on `g = R³` through `Ad` (so all
matrices are real `3 × 3`). Chain gauge `G(y) := g^{y_1}` with `Ad_g = R`, `R` the integer matrix of the
quarter-turn about the 3-axis, `R = [[0,−1,0],[1,0,0],[0,0,1]]`; `g^8 = 1`, so `G` is periodic for `8 | T`.
Background: `Z(y,1) := G(y)G(y+e_1)^{−1}`, `Z(y,2) := G(y)G(y+e_2)^{−1}`. All arithmetic is **exact
integer** arithmetic (entries of `R` and `R^{−1}` are in `{0, ±1}`). No floating point. No BLAS. No lock.

## Gates

**hr1-D (precondition).** Every plaquette holonomy of `Z` equals the identity exactly, i.e. `U_1 = U_2` at
every `p`, so `f = 0` exactly on this configuration.
- **PASS** if `U_1 − U_2 = 0` at every plaquette (exact integer equality).
- **FAIL** otherwise — and then hr1-A and hr1-B are void and are not reported as evidence.

**hr1-A (the currency gate; this is the decider).** Compute the exact integer matrix
`E := d_Z^*d_Z − d^*d` on `R³`-valued functions on the torus.
- **PASS (route survives):** `E = 0` exactly. Then (HESS-rel) is not refuted by zero curvature and the
  route continues to TL3.
- **FAIL (route refuted at this step):** `E ≠ 0`. Reported as: **(HESS-rel) as stated in `NBG_A.md` §A4.3
  is FALSE**, because the right-hand side is `C·0·‖Hess𝔉_k(1)‖ = 0` while the left-hand side is `> 0` in
  every norm. A witness must be exhibited: an explicit `λ` with `‖Eλ‖² / ‖λ‖²` an exact positive rational.
- *Pre-registered expectation:* **FAIL** (failure mode **HR-F1** of `HESSREL.md` §H0.5). Recording the
  expectation does not change the verdict rule: if `E = 0` the gate PASSES and HR-F1 does not occur.

**hr1-B (the extension gate).** On the **same** configuration compute (i) the B1 defect `(U_1 − U_2)` at
every plaquette and (ii) the B2 defect `Row(Y,μ) − Ad_{Z(Y,μ)}` for the straight row of length `L = 2`
along direction `μ` (the one-step straight-row comparison of (41.3)).
- **PASS (the two defects do control the difference):** at least one of the two defects is non-zero
  whenever `E ≠ 0`.
- **FAIL (the extension from two defects to the whole difference does not hold):** both defects are
  exactly `0` while `E ≠ 0`. Reported as: **BFT_B §41.2 (c)'s bound, which bounds exactly these two
  defects, cannot bound `Hess𝔉_k(Z) − Hess𝔉_k(1)`, because the two defects vanish on a configuration
  where the difference does not.**
- *Pre-registered expectation:* **FAIL**.

## Designed-FAIL controls (Defect 3). Each must behave as stated or the corresponding gate is withdrawn.

**hr1-C1 (constant gauge; control for hr1-A).** Rerun the identical code with `G ≡ 1` (so `Z ≡ 1`).
- The control **fires** (behaves as a control should) iff `E = 0` exactly.
- If `E ≠ 0` here, the hr1-A verdict is an artefact of my own arithmetic and is **withdrawn**.

**hr1-C2 (abelian; control for hr1-A).** Rerun the identical code with the adjoint action replaced by the
`1 × 1` identity (the abelian case, where `Ad ≡ 1`).
- The control **fires** iff `E = 0` exactly. This is the abelian control that BFT_B.md l.4538's bb11 **C1**
  runs for the B1 defect; it certifies that what hr1-A detects is **nonabelian** content.
- If `E ≠ 0` here, hr1-A is withdrawn.

**hr1-C3 (positive control for hr1-B).** Rerun with a **curved** background: the same `Z` but with the
single link `Z(0, 2)` replaced by `R` (which destroys flatness at the plaquettes touching that link).
- The control **fires** iff the B1 defect `(U_1 − U_2)` is **non-zero** at at least one plaquette.
- If the B1 defect is `0` here too, then hr1-B's "both defects are zero" is a blind test (my B1 code never
  sees anything) and hr1-B is **withdrawn**.

**hr1-C4 (positive control for hr1-A's witness).** The witness `λ` exhibited for hr1-A must also satisfy
`‖(d^*d)λ‖² > 0`, so that the exhibited ratio is not a comparison against a zero operator.
- The control **fires** iff `‖(d^*d)λ‖² > 0`.

## What this check does NOT decide (stated now, so it is not claimed later)

1. It does not decide whether a **repaired** statement (comparison against a flat chain of nontrivial
   holonomy, or against a conjugated flat Hessian) is true. That is argued in `HESSREL.md`, not checked.
2. It says nothing about the **soft** blocks of `Hess𝔉_k`; it tests only the level-0 Wilson block, which
   suffices to refute a bound on the whole difference but not to size it.
3. It says nothing about whether `Z(V)` for a given `V` in the class *is* a pure gauge under the lane's
   gauge-fixing conventions. The refutation is of (HESS-rel) **as quantified in §A4.3** ("for every `k`,
   every torus and every `V` of the class", with no representative named); the separate argument that the
   same failure occurs for the lane's own lift `Z^off` is made in `HESSREL.md` from SF's BNA-F4 and
   Corollary CL-iv's frame-locality, **not** from this check.

---

## AMENDMENT, 2026-10-28 21:53:48 UTC — a defect in MY OWN criteria, disclosed, with the corrected gate

**The defect.** Gate **hr1-A** above says "Compute the exact integer matrix `E := d_Z^*d_Z − d^*d` on
`R³`-valued **functions** on the torus". That is `d_Z` acting on **0-forms**, i.e. the Faddeev-Popov /
chain-gauge block (the operator of BFT_B.md l.4578, Lemma FR-price step 4, where `λ` is a 0-form). The
**Wilson block of `Hess𝔉_k`** is `d_Z^*d_Z` with `d_Z` acting on **1-forms** (`½‖dB_0‖²` of PROOF.md
l.6613, `B_0` a level-0 1-form). **So hr1-A as pre-registered tested an adjacent operator, not the one
named in (HESS-rel).** The script `checks/hr1_flat.py` and its output `checks/hr1_out.txt` were already
run when this was noticed; **they are kept unaltered and are NOT rerun**, and their verdicts stand for
the operator they actually tested (which is a real lane object — §41.4 step 4's normal operator).

**Status of the original gates after this amendment.** hr1-A and hr1-B remain valid **as evidence about
the Faddeev-Popov block and about the two defects B1/B2** (B1 and B2 were computed from the plaquette
data directly and are unaffected by the 0-form/1-form distinction; hr1-C1/C2/C3/C4 likewise stand). They
are **not** by themselves evidence about the Wilson Hessian block, and nothing in `HESSREL.md` may claim
they are.

**Corrected gates, pre-registered now, before `checks/hr1_wilson.py` is written (it does not exist at the
time of writing). These are POST-HOC relative to the first run and are labelled post-hoc wherever they
are reported.**

- `d_Z` on 1-forms: `(d_Zu)(p) = u(z,μ) + Ad_{Z(z,μ)}u(z+e_μ,ν) − Ad_{Z(z,ν)}u(z+e_ν,μ) − u(z,ν)`
  (the same convention as above), `p` the plaquette at `z` with `μ < ν`; `d^*` the transpose.
- **hr1-A′ (the Wilson-block currency gate).** `E_W := d_Z^*d_Z − d^*d` on **1-forms**, on the same exactly
  flat nonabelian pure-gauge configuration.
  - **PASS (route survives):** `E_W = 0` exactly.
  - **FAIL (route refuted):** `E_W ≠ 0`, with an exhibited witness `u` and exact integers `‖E_Wu‖²`,
    `‖(d^*d)u‖²`.
- **hr1-A″ (the gauge-fixed block).** `E_H := (d_Z^*d_Z + d_Zd_Z^*) − (d^*d + dd^*)` on 1-forms — the shape
  of the Hessian with a Feynman fixing. Same PASS/FAIL rule.
- **Controls, same rules as before and each must behave as stated or the corresponding gate is withdrawn:**
  **hr1-C1′** constant gauge ⟹ `E_W = E_H = 0` (control fires iff both are `0`);
  **hr1-C2′** abelian ⟹ `E_W = E_H = 0` (control fires iff both are `0`);
  **hr1-C4′** the exhibited witness must satisfy `‖(d^*d)u‖² > 0`.
- **hr1-D′** the flatness precondition is re-checked by the new script independently.
