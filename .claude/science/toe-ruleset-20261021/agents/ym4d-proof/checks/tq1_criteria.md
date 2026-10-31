# checks/tq1_criteria.md — pre-registered criteria for check tq1 (TENTQ session 25)

Written 2026-10-28 14:1x UTC, **after** TENTQ.md §1 (PRE-STATED) and **before** `checks/tq1_charge.py`
exists. Every constant quoted below comes from a **previous** session and is named with its source; no
constant derived in this session appears here. All arithmetic exact (`fractions.Fraction`), plain python,
single thread, no numpy/BLAS, no numeric lock (per DRIVE_BRIEF rule 6: exact rational arithmetic needs none).

## Conventions fixed before the run (all from previous sessions)

- L = 3. Level-l roots at off(l) + L^l·Z^d with off(l) := (L^l - 1)/2 (BFT_B §15.0 "roots at block
  centres"; the same convention as `checks/ba8_fun.py` / scratch `revA8/rev8_psi.py`, where off(2) = 4).
- σ_5(t) := 1 - p(t), p(t) := 10t³ - 15t⁴ + 6t⁵ on [0, 1], σ_5 := 0 for t ≥ 1 (BFT_B §16.1 (b)).
- χ^5_X(w) := Π_ν σ_5(|w_ν - c_{X,ν}|_per / n), n := L^k (BFT_B §24.0, §16.1 (b)).
- d* convention: (d*v)(z) = Σ_μ[v(z - e_μ, μ) - v(z, μ)], so (d*df)(z) = 2d·f(z) - Σ_{±μ}f(z ± e_μ)
  (BFT_A §23.1, quoted in BFT_A §38.3).
- D(S) := d*S_0 + Σ_{1≤l≤k-1} ev^{(0→l)T} d*S_l (BFT_B §27.1).
- Q_X(S) := ⟨χ^5_X, D(S)⟩ (BFT_B §36.5 (ii)).
- Φ_k(v)(X) := Σ_{i<k} ev^{(i+1→k)} h_i(Q_str^{(0→i)}v)(X), with h_i the 24-order axial-average funnel
  weight and Q_str the straight block average (BFT_A §36.0 "Funnel functions"; the h and Q_str
  implementations of `revA8/rev8_psi.py`, themselves re-implemented there from `checks/c26_led.py` and
  `checks/ba5_y.py`).
- A^{(0→k)}μ(X) := L^{-4k} Σ_{s ∈ [0, L^k)^d} μ(L^k X + s), the iterated block average (BL-2 (b)'s
  straight average applied to 0-forms; the identity Q_str∘d = d∘A is the transpose statement of BL-2 (c)).

## Checks and their pre-registered verdicts

**Models.** M1: d = 2, L = 3, k = 2 (n = 9), torus of 3 coarse cells per direction (side 27), source slots
S_0, S_1 pseudo-random Fractions on the whole torus. M2: d = 4, L = 3, k = 2 (n = 9), torus of 3 coarse
cells per direction (side 27), source slots **sparse** (a few links each) so that the full-torus sums stay
cheap. M3: d = 4, L = 3, k = 2, a pseudo-random level-0 0-form μ on a box large enough for Φ_2 to read it.

| id | statement tested | PASS iff | FAIL iff |
|---|---|---|---|
| **A1** | Σ_X Q_X(S) = 0, M1 and M2 | the Fraction is **exactly** 0 in both models | any nonzero value |
| **A2** | Q_X(S) = Σ_{l=0}^{k-1} ⟨d(ev^{(0→l)}χ^5_X), S_l⟩ for **every** X, M1 and M2 | exact equality for every X in both models | any X with a nonzero difference |
| **A3** | Σ over level-l links of \|d(ev^{(0→l)}χ^5_X)\| = **2d(n/L^l)^{d-1}** for every 0 ≤ l ≤ k (the exact total variation of BFT_B §25.1 (f), post-proof correction (1)) | exact equality at every l in M1 and M2 | any l where it differs |
| **A4** | Σ_X χ^5_X ≡ 1 and ⟨χ^5_X⟩ = n^d (BFT_B §16.1 (b), §25.1 (f)'s "the second is n/s") | both exact, every site / every X | either fails anywhere |
| **A5** | n²Σ_X Q_X(S)·Φ(c_X) = n²Σ_l ⟨d(ev^{(0→l)}Ψ), S_l⟩ with Ψ := Σ_X Φ(X)χ^5_X, for a **pseudo-random** level-k function Φ (no response solve), M1 and M2 | exact equality in both models | any difference |
| **A6** | **Φ_k(x_0 + dμ)(X) - Φ_k(x_0)(X) = A^{(0→k)}μ(X) - μ(c_X)**, M3, pseudo-random μ and pseudo-random x_0 | exact equality | any difference |
| **A7** | rebuild of REVIEW_BFT_A_S8 S8-7's exact tent values for u := ⅛ d*δ_p, p the (0,1)-plaquette at c_X + (1,0,0,0), k = 2: φ_1 = **-1/432**, φ_2 = **-17/104976**, φ_2/φ_1 = **17/243**, ψ_u = **-65/26244** | all four **exactly** equal to the quoted values | any mismatch |
| **A8** | *informational, no verdict.* max_X\|Φ_k(u)(c_X)\| and the one-coarse-step difference max_X,μ\|Φ_k(u)(c_{X+e_μ}) - Φ_k(u)(c_X)\| for the A7 source u, and their ratio | — | — |

## Pre-registered failure-mode mapping (to TENTQ.md §1.2)

- A1 FAIL ⟹ **TQ-F1 occurs**.
- A2 FAIL ⟹ the summation-by-parts form of T2 is wrong; **T2 (a) is refuted** and nothing in T3 stands.
- A3 FAIL ⟹ the exact total variation quoted from BFT_B §25.1 (f) does not hold in my conventions; then every
  constant in T2/T3 is suspect and must be recomputed, and the discrepancy is reported as a defect against
  §25.1 (f) **or** against my conventions, with both possibilities named.
- A5 FAIL ⟹ the tent-interpolation reduction of T3 is wrong; **T3 collapses**.
- A6 FAIL ⟹ the tent-gauge proposition of this session is wrong; the representative-dependence half of T3's
  conclusion must be withdrawn.
- A7 FAIL ⟹ either my h/Q_str rebuild or REVIEW_BFT_A_S8 S8-7 is wrong; in that case **no** number from S8-7
  is used anywhere in TENTQ.md and the discrepancy is reported as the session's main finding.
- A8 is informational and feeds only a COMPUTED statement; it is **not** permitted to change any verdict.

## Scope limitations, stated before the run

1. k = 2 only. At k = 2 there are two funnel levels (i = 0, 1), so A6's telescoping is tested with two terms;
   a FAIL at k = 3 would not be detected. A1-A5 are conventions-and-adjointness identities and are
   k-insensitive in form, but that is an expectation, not a test.
2. M1 is d = 2, which is not the physical dimension; it is used only where the identity is dimension-generic
   (A1-A5). A3's right-hand side carries d explicitly and is checked in **both** d = 2 and d = 4.
3. No response field is computed anywhere: Φ in A5 is pseudo-random and in A7/A8 is evaluated on an explicit
   compactly supported **source** field, never on Y^p. Nothing in tq1 measures the response, so no verdict
   of this session may claim anything about Y^p's own field.
4. No box-Neumann solve is performed, so nothing here tests Lemma ΓT-op (a)'s A^X_w fields; the pin
   cancellation of target T4 is argued algebraically from §25.1 (a) and is **not** checked numerically.
