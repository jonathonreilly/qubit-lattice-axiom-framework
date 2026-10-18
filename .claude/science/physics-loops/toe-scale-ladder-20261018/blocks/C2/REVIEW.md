# C2 review (independent reviewer)

**Reviewed:** `NOTE.md` at commit 921a83728 (base main @ 584755767).
**Evidence:** `review_scripts/review_check.py` writes `review_scripts/review_check.log`, which ends `TOTAL: PASS=35 FAIL=0`. It runs in under a minute and needs only numpy, sympy and scipy. None of the author's scripts were imported or used as evidence.
**Provenance:** one reviewer agent, the session's configured model. The reviewer is a separate agent from the author, but nothing about independence is claimed beyond the different derivation routes listed below.

## Summary verdicts

| # | Claim | Verdict | Severity |
|---|---|---|---|
| 1a | One-loop fermion speed flow `d ln c_psi/dl = (e^2/6pi^2)[eta - 4/(1+eta)^2]` | **correct** (rederived in Coulomb gauge) | — |
| 1b | Photon speed flow and the `1/e^2` flow | **correct** | — |
| 1c | Linearised `d delta/dl = -(2alpha/3pi)(N_f+2) delta`, and `delta ∝ alpha^((N_f+2)/N_f)` | **correct** | — |
| 1d | 0.781 (`N_f=1`, `l=51`), 0.637 and 0.287 | **correct with fix** (scope the toy matter content) | minor |
| 1e | §0.5 "IR flow removes at most an O(1) factor" | **correct with fix** (state that it holds in the perturbative window) | minor |
| 1f | Agreement with Chadha–Nielsen and Isobe–Nagaosa | **unverified** (reviewer also has no source access) | info |
| 1g | "`c_gamma^2 c_psi` stationary to second order" | **correct with fix** (wording) | minor |
| 2 | T_tie group theory and its hypotheses | **correct with fix** (spell out the hypotheses; correct the count under the Lattice axiom's proper rotations) | minor |
| 3a | W2 meets the registered premises under reading K_m | **correct**, given the declared K_m reading | — |
| 3b | W1 | **correct as scoped**; the cited values were located on main but not recomputed | minor |
| 3c | Headline "kinetic isotropy ⇒ common cone retired as stated" | **correct with fix** (it is conditional on reading K_m) | moderate |

## 1. One-loop flow

### 1a. Fermion self-energy, rederived by a different route

The author works in the photon-frame Feynman gauge, with sympy shell integrals plus a numerical 4D quadrature. My derivation differs in the following ways.

- **Fermion frame.** I rescale `x' = x/c_psi` (with `A_0' = A_0`, `A_j' = c_psi A_j`, so `E' = c E`, `B' = c^2 B`, `d^4x' = d^4x/c^3`). The fermion then becomes Lorentz invariant with speed 1. The photon action becomes `(1/2e^2)[E'^2/eta + eta B'^2]` with `eta = c_gamma/c_psi`, so the problem reduces to a single-parameter function `f(eta)`.
- **Coulomb gauge.** I use the instantaneous `D_00 = e^2 eta/|k|^2` and the transverse `D_ij = e^2 eta (delta_ij - khat_i khat_j)/(k0^2 + eta^2 k^2)`.
- **Gamma algebra by hand.** The two contractions are `gamma0 qslash gamma0 = gamma0 q0 - gamma.q` and `sum_ij gamma_i qslash gamma_j (delta_ij - khat khat) = -2 gamma0 q0 - 2(khat.q) gamma.khat`. Both are checked with explicit matrices.
- **Effective action.** From `S_eff = -½<S_int^2>` I get `K_eff = i pslash - i ∫ gamma_mu qslash gamma_nu D_mu nu / q^2`, so that `d ln c_psi/dl = delta_s - delta_0`.
- **Log coefficients.** These are exact angular integrals over S^3. A homogeneous integrand of degree -4 has a log coefficient that does not depend on the cutoff shape. With `W = 1 + (eta^2-1) sin^2`, the integrals have closed forms `I1 = pi/(eta(eta+1))` and `I2 = (pi/2 - I1)/(eta^2-1)`, which I also cross-checked by quadrature.

Result: `f(eta) = (eta-1)(eta^2+3eta+4) / (6pi^2 (eta+1)^2)`. This is symbolically identical to the author's `[eta - 4/(1+eta)^2]/(6pi^2)`.

Three checks back this up:
- At `eta = 1`: `Z_0 = Z_s = e^2/8pi^2`, which is the standard `Z_2`, and the sign matches `Z_2 = 1 - (alpha/4pi) ln Lambda^2`. This anchors the sign convention on its own, without the author's `K - Sigma~`.
- At `eta → ∞`: `d ln c/dl → e^2 eta/(6pi^2) = 2alpha_C/(3pi)` with `alpha_C = e^2 c_gamma/(4pi c_psi)`. This is the standard Abrikosov–Beneslavskii / Goswami–Chakravarty result for 3D Dirac/Weyl fermions with instantaneous Coulomb interaction, `dv/dl = (2alpha/3pi) v`. I rely on memory for that literature result, but I know it well.
- The Feynman-gauge (author) and Coulomb-gauge (mine) results agree. This is a non-trivial gauge-independence check, because the two gauges differ by longitudinal terms that only feed `K(p)`.

### 1b. Vacuum polarisation

The same frame rescaling applied to the standard QED log `d(1/e^2)/dl = N_f/(6pi^2)` gives:
- `d eps/dl ∝ 1/c` and `d(1/mu)/dl ∝ c`;
- `d ln c_gamma/dl = (N_f e^2/12pi^2)(1/eta - eta)`;
- `d(1/e^2)/dl = N_f (eta + 1/eta)/(12pi^2)`.

All of these match the note. Physically, vacuum polarisation pulls `c_gamma` toward `c_psi`.

### 1c. Linearisation and the closed form

- Linearising gives `d delta/dl = -(N_f+2) e^2/(6pi^2) delta = -(2alpha/3pi)(N_f+2) delta`. This is verified symbolically.
- The author's drag decomposition also checks out: fermion drag `a = e^2/(3pi^2)` and photon drag `b = N_f e^2/(6pi^2)`.
- `d(d ln eta/dl)/d eta < 0` for every `N_f` (checked on (0.02, 50) for `N_f = 1, 3, 8`). It is also analytically obvious: every term is decreasing. So `eta = 1` is the unique, globally attractive fixed point.
- With `d alpha/dl = -(2N_f/3pi) alpha^2` at `eta = 1`, the ratio `d delta/d alpha = ((N_f+2)/N_f) delta/alpha` gives `delta ∝ alpha^((N_f+2)/N_f)`. Correct.

### 1d. Numbers

- **How α_UV is set.** It is not an independent input. It comes from `alpha_IR = alpha(m_e) = 1/137.036`, run up with Lorentz-limit one-loop running for `N_f` unit-charge species over the full `l`. This *is* declared, in the note's §5 "Residuals".
- **N_f = 1, l = 51.** `1/alpha_UV = 126.213`, and `(126.213/137.036)^3 = 0.78129`. Reproduced.
- **Other cases.** `N_f = 3` gives 0.6372 and `N_f = 8` gives 0.2868. Reproduced.
- **l values.** `ln(1.22e19 GeV/m_e) = 51.53`. Reproduced.
- **Nonlinear flow.** My own RK4 integration gives `eta_UV = 1.2 → eta_IR = 1.152478`, matching the table.
- **Fix (minor).** Say plainly in §0.4 that 0.781 belongs to the toy content: U(1) plus one unit-charge Dirac fermion, no thresholds, `alpha(m_e)` imposed at the IR end. The real charged spectrum, with thresholds and hypercharge embedding, would give a different O(1) number. The `N_f = 1` choice is mentioned only in the table header area; §0.4 should carry it too.

### 1e. The "at most O(1)" conclusion

- It holds only while one loop is valid all the way up.
- If `alpha_UV` were allowed to approach strong coupling, the suppression would be `≈ (alpha_IR/alpha_UV)^((N_f+2)/N_f)`. For `N_f = 1` that can go as low as about `(1/137)^3 ≈ 4e-7` at `alpha_UV ~ 1`. That is still about 8 orders short of 1e-15, so the conclusion survives.
- **Fix (minor).** Replace "at most an O(1) factor" with "an O(1) factor for the declared running; even at the edge of perturbativity (`alpha_UV ~ 1`) no more than about `alpha_IR^((N_f+2)/N_f)`". That strengthens the R3 obligation, and it fits the note's own disclaimer about strong coupling in §6.

### 1f. Literature

- **Chadha–Nielsen 1983** (NPB 217, 125): I recall that they find the Lorentz-invariant point IR-attractive at one loop for gauge plus fermion theories. **I cannot verify their coefficients.**
- **Isobe–Nagaosa 2012** (PRB 86, 165127): I recall that they treat 3+1D QED with `c ≠ v` and find that both flow to a common value. **I cannot verify their explicit equations or the "c^2 v almost unrenormalised" phrasing.** I had no network access to the papers either.
- The note correctly flags both as not cross-checked. Keep it that way.
- My derivation does confirm the structural fact quoted from Isobe–Nagaosa (see 1g).

### 1g. Wording

At `N_f = 1`, `d ln(c_gamma^2 c_psi)/dl = e^2 delta^2/(24pi^2) + O(delta^3)`. So `c_gamma^2 c_psi` is stationary at *first* order with an O(δ²) drift. "Stationary to second order" is ambiguous. **Fix:** write "invariant to first order in `eta - 1`".

## 2. T_tie

I counted the group theory independently by averaging over explicit elements. These are signed permutation matrices on R⁴, and on Λ²R⁴ the 6×6 matrices are built from the 2-minors.

| Group | Invariant rank-2 tensors | Invariant symmetric forms on Λ² |
|---|---|---|
| B4 (order 384) | 1 | 1 |
| Proper B4 | — | 2 (F², FF̃) |
| O_h × Z2(t) (order 96) | 2 | 2 |
| O × Z2(t) | — | 2 |
| **O only** (proper cubic, no time reflection) | **2** | **3** (E², B², E·B) |

The proof idea in the note is correct. B4 contains the 90° rotations that mix τ with space, and those force `delta_00 = delta_jj` and `E² ↔ B²`.

**Fix 2a (minor), the count under the Lattice axiom.** The Lattice axiom on main gives only *proper* cubic rotations (`MINIMAL_AXIOMS_2026-06-29.md`, lines 38 and 58), not O_h. Without time reflection the gauge count is 3, not 2: E·B (the θ-term) is also allowed. It carries no velocity, so W2's conclusion is unaffected. The sentence "Under spatial cubic symmetry times time reflection there are two" is true, but the note should say that time reflection or inversion is an *extra* assumption beyond the Lattice axiom.

**Fix 2b (minor), list the hypotheses that are actually used.**
- (i) B4 acts on the fermion through a Pin/spinor lift under which `gamma_mu` is a vector.
- (ii) No internal (taste or flavour) index transforms nontrivially under B4. Otherwise B4-invariant bilinears such as `sum_mu (gamma_mu ⊗ xi_mu) d_mu` exist, and their IR content needs a separate argument. This is relevant to staggered carriers like the one on main.
- (iii) A Euclidean local action exists on `Z^4`. Neither the Hamiltonian comparator nor the QCA walk provides one, which the note itself says.
- (iv) No spontaneous breaking, and an analytic small-momentum expansion.
- The "all orders" persistence is the standard symmetry argument, and the note rightly says it is not re-proved.
- `c = a/a_tau` is just the conversion of the lattice-unit value 1 into physical units.

## 3. Witnesses W1 and W2 against the premises on main

**The primitive text on main.** I read `docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md` on main myself. It says: "the matter kinetic normalization is space-time isotropic, `c_t = c_s`, equivalently the Euclidean regulator block `Z^3 x Z_tau` on which loops are computed is hypercubic-symmetric". The registry node in `axiom_premise_nodes.json` says "supplies only the kinetic form ratio". The quote from the strict-license note is accurate (`KINETIC_ISOTROPY_FROM_STRICT_LICENSE_..._2026-06-09.md`, line 277): "Matter sector only ... gauge-sector plaquette-coefficient anisotropy ... separate rows".

**W2.** My independent small-k pole checks confirm `c_gamma = sqrt(beta_s/beta_t) = 6/5` and `c_psi = 1/zeta_0 = 1`. W2 satisfies the premises under K_m and under the geometric reading (`a_tau = a`). It fails under K_full, as the note says.

**Fix 3c (moderate).**
- The primitive's own word "equivalently" means its author read "matter isotropy" and "regulator block hypercubic-symmetric" as the same statement. The phrase "regulator block on which loops are computed" can fairly be read as covering the gauge propagator used in those loops, which is K_full.
- So the headline "retired as stated" should read "**retired under reading K_m (the scope its support notes give it); under reading K_full it holds, via T_tie**".
- The note does record the ambiguity in §1. Only §0's closing line overstates it.
- Also, W2B satisfies K_m only for the *bare* matter action. At O(α) the matter form is driven anisotropic, as the note mentions (the Collins mechanism). That is fine, because the primitive concerns the regulator form, but §3 should say "bare" explicitly.

**Typo.** §0.2 ends with "The scale reference is dimensionless-free". This is garbled; it should read "carries no dimensionless content".

**W1.**
- I confirmed on main that `v = sqrt(UK) = 1.025` (Gaussian comparator note, 2026-10-01) and the walk value 0.9144 (two-qubit Dirac walk note, 2026-10-16) are both there. I did not recompute the walk.
- The note's own scoping is accurate and not overstated: the kinetic-isotropy primitive cannot be evaluated on these carriers, the clock conversion `rho` is a free declared input, and the site lies outside the Qubit axiom.
- The sampled-curve monotonicity is labelled numerical, which is correct.

## Net

The physics core is correct and confirmed by a different gauge and a different route: the two-velocity one-loop flow, its linearisation, the closed-form decay law and the quoted numbers. The T_tie group theory is right. The fixes are scoping and wording only:
- 1d: state the toy matter content in §0.4;
- 1e: add the perturbative-window bound;
- 1g: "first order" in place of "second order";
- 2a: the proper-O count is 3, and time reflection is an extra assumption;
- 2b: list the T_tie hypotheses explicitly;
- 3c: make the headline conditional on K_m, and fix the §0.2 typo.

Nothing here is incorrect.

## Correction confirmation

I read the whole corrected `NOTE.md`, including §9. The author's rerun ends `logs/run_all.log` with `TOTAL: PASS=49 FAIL=0`. The new O-only count check is at `logs/witness_os0_surface.log` line 8.

| Finding | Resolved? | Where it is fixed |
|---|---|---|
| 1d: toy matter content | yes | §0.4: U(1) plus one Dirac fermion, no thresholds, α(m_e) imposed at the IR end, and real spectrum gives a different O(1) number. |
| 1e: perturbative window | yes | §0.5. The bound α_IR³ ≈ 3.9e-7 (N_f = 1) is correct; I recomputed it. It is honestly labelled as the reviewer's estimate. |
| 1f: literature | yes | The literature coefficients are still marked "not cross-checked". |
| 1g: "invariant to first order" | yes | §5. The δ² drift coefficient e²/(24π²) matches my log. |
| 2a: proper-O count of 3 | yes | §0.1 and §2. Time reflection is marked as an extra assumption, and a runner check was added. |
| 2b: hypotheses | yes | §2 lists H0–H4, matching my list. |
| 3a/3b: "bare" matter action | yes | §0.2 and §3. |
| 3c: headline | yes | The title and the §0 closing line now say retired under K_m and holds under K_full. Which reading the primitive carries is left to owner or audit. |
| §0.2 typo | yes | Rewritten. |

**New defects:** none of substance. One cosmetic nit remains. The header still says "Unreviewed and unaudited", which contradicts the "Review: REVIEW.md" line; "independently reviewed; unaudited" would fix it. This does not block.

**Final verdict: READY.** The block is ready as worker output for audit. No audit status is implied.
