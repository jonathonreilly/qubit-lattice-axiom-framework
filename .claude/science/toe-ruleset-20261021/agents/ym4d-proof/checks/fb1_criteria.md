# fb1 — pre-registered criteria for FACEB.md (target T55-G)

Written **2026-10-28T21:20:47Z**, AFTER FACEB.md §1 (PRE-STATED, 21:17:09Z) and **BEFORE any script**.
No constant below was derived in this session. Every number quoted is from a prior file with its file:line.

## What fb1 tests, and why these clauses

The one identity on which my §5 escapes (i)/(ii)/(iv) all turn is `d∘d = 0` on the lattice cochain
complex, in the two forms the lane uses it: (a) an **exact** 1-form pairs to zero against a **co-exact**
1-form; (b) a co-exact 1-form is **co-closed**. fb1 verifies those two forms, verifies them on the
**actual witness** `u = d*δ_p` of YSUP.md §2.3 (ii) rather than on a generic field, and checks that the
gate can tell the difference between a divergence-form slot and a generic one. fb1 also reproduces the
decade arithmetic of §6 at two precisions.

fb1 is **exact integer / exact rational arithmetic in plain python**, no BLAS, no numpy, no machine-wide
lock (session-25 brief rule 6). Lattice: periodic `Z_N^4`, `N = 4` (256 sites, 1024 links, 1536
plaquettes). Conventions, fixed here before the script exists:

- `(dφ)(z,μ) = φ(z+e_μ) − φ(z)` on 0-forms;
- `(dA)(z,μ,ν) = A(z,μ) + A(z+e_μ,ν) − A(z+e_ν,μ) − A(z,ν)` on 1-forms, `μ < ν`;
- `δ` is the **transpose** of `d` for the counting inner products, computed in the script by transposing
  the incidence lists and not by writing a second formula — so a sign error in `d` cannot be cancelled by
  a matching sign error in `δ`.

## Clauses and pre-registered verdicts

| id | clause | PASS | FAIL | could it have failed? |
|---|---|---|---|---|
| **A1** | `d∘d = 0` on 0-forms: `d(dφ) = 0` at every plaquette, for 5 pseudo-random integer 0-forms `φ` and for `φ = δ_z` at 3 sites | every component exactly `0` | any nonzero component | **MEDIUM-HIGH.** A wrong plaquette orientation, a wrong periodic wrap or a wrong `e_μ` offset each break it. |
| **A2** | the **source-leg** statement: `⟨dφ, δW⟩ = 0` for 5 pseudo-random 0-forms `φ` and 5 pseudo-random integer 2-forms `W` (25 pairs) | all 25 exactly `0` | any nonzero | **MEDIUM-HIGH.** Independent of A1 in code path: it uses the transposed incidence lists, not `d∘d`. |
| **A3** | the **response-leg** statement on the actual witness: with `u := δ(1_p)` for the plaquette `p = (0; 0,1)` (YSUP.md §2.3 (ii)'s `u = ⅛d*δ_p` up to the factor `1/8` = `1/(2d)`), `⟨dμ, u⟩ = 0` for 5 pseudo-random 0-forms `μ` and for `μ = δ_z` at 5 sites | all 10 exactly `0` | any nonzero | **MEDIUM.** It is A2 at a delta `W`, but on the specific witness the sharpness claim uses. |
| **A4** | **non-vacuity of A3** (defect 3: a clause that passes because its object is zero decides nothing): `u ≠ 0`, `δu = 0` (co-closed), and `du ≠ 0` (it carries curvature) | all three hold | any fails | **HIGH as a guard.** If `u` were `0`, or co-exact-trivial, A3 would be vacuous and I would have to say so. |
| **A5** | **discriminating power of the gate**: with a *generic* 1-form `j` in place of `δW`, `⟨dφ, j⟩ ≠ 0` for at least 4 of 5 pseudo-random pairs | at least 4 nonzero | fewer | **This clause exists to show A2 is not a tautology about the pairing.** |
| **A6** | **DESIGNED-FAIL CONTROL.** Corrupt the complex: flip the sign of exactly one entry of the 1-form→2-form incidence (one `(plaquette, link)` pair). Re-run A1, A2, A3. The control **must FAIL them**. | A1/A2/A3 all produce at least one nonzero under the corruption | the corruption changes nothing | **This is the control. I report it as having FAILED, and if it does not fail, A1-A3 are not evidence and I say so.** |
| **A7** | **price arithmetic**, exact and at two precisions (50 and 100 significant digits): `P(k) := (2k−3)·log₁₀3`; the `k` solving `P(k) = −log₁₀(DX′)` with `DX′ = 2.456·10⁻¹⁵²` (REVIEW_SF_S7.md l.203, `C_Ω = 1`); the `k` solving `P(k) = −log₁₀(ε₁)` with `ε₁ = 6.7·10⁻⁴⁰` (RLARGE l.72, the headline value quoted in ARS_FIX.md l.271); and `P(k)` at `k ∈ {10, 42, 160, 183, 356}` | the two precisions agree to `< 10⁻³⁰` in every row | any row disagreeing above that | **LOW as mathematics, MEDIUM as bookkeeping** — it is a guard against a precision artefact in a figure that will be quoted. |

## Pre-registered scope limitations of fb1 (stated before the script, so they cannot be retrofitted)

1. fb1 touches **no funnel**: it does not rebuild `Φ_k`, `h_i`, `Q_str` or any of YSUP's rationals. Every
   funnel number used in FACEB.md is **quoted** from YSUP.md / TENTQ.md / REVIEW_BFT_A_S8 with its
   file:line and is **not** re-verified here. Any claim of mine that depends on a funnel value is
   therefore CONDITIONAL on those files, and FACEB.md labels it so.
2. fb1 is **abelian, trivial background, `m = 0`, `d = 4`, `N = 4` periodic**. It is a check on the
   cochain complex, not on the RG.
3. fb1 decides **nothing** about whether `Φ_k(Y^p_{*,0})` is `Θ(1)`. That is the profile input, it is not
   tested here, and FACEB.md's sharpness section is written to say exactly that.
4. A7 uses an identification between the 𝔐-ball radius `η` of BFT_A.md l.2809 and the quantities `DX′`
   and `ε₁` bound. **That identification is NOT established anywhere I have read**, and FACEB.md §6 states
   it as an assumption with that warning attached; A7 verifies only the arithmetic, never the
   identification.

## Process

`FACEB.md` §1 (21:17:09Z) → this file (21:20:47Z) → `checks/fb1_bianchi.py` → `checks/fb1_out.txt`.
Any FAIL is reported as a FAIL with output kept byte-unaltered; a re-run goes under a new id with these
criteria untouched; any probe added after seeing a result is labelled post-hoc.
