# fl55_4 criteria — uniqueness of the marginal cubic jet (Ward transport), exact (written before any fl55_4 script)

Owner: FLOW55.md (worker claude-opus-5-5). Script: checks/fl55_4.py, written AFTER this file. Plain python 3 with
`fractions.Fraction` (exact Gauss-Jordan rank) and sympy only for polynomial bookkeeping; no numpy, no floats in any verdict.
nice 10. Output: checks/fl55_4_out.txt, checks/fl55_4_err.txt.

## Objects
d = 4. A degree-1 cubic symbol is T_{μνρ}(p, q) := Σ_σ(α_{μνρσ}p_σ + β_{μνρσ}q_σ) (512 rational unknowns), with the third leg
momentum r := −p − q. Legs: 1 = (μ, p), 2 = (ν, q), 3 = (ρ, r).
- **(H) hypercubic covariance.** For each generator g of the hyperoctahedral group B_4 (signed permutations; generators:
  the transposition of axes 1, 2; the cycle 1→2→3→4→1; the reflection of axis 1), with (gp)_μ := Σ_ν g_{μν}p_ν:
  T_{μνρ}(gp, gq) = Σ_{μ′ν′ρ′}g_{μμ′}g_{νν′}g_{ρρ′}T_{μ′ν′ρ′}(p, q) identically in (p, q).
- **(S−) Bose antisymmetry (f-type colour) / (S+) Bose symmetry (d-type colour).** Under the transposition of legs 1, 2:
  T_{νμρ}(q, p) = ∓T_{μνρ}(p, q); under the transposition of legs 1, 3: T_{ρνμ}(r, q) = ∓T_{μνρ}(p, q) (r = −p − q),
  identically in (p, q). (Upper sign: (S−).)
- **(W0) homogeneous transversality on leg 1.** Σ_μ p_μT_{μνρ}(p, q) ≡ 0 as a polynomial in (p, q).
- The Yang-Mills vertex V^{YM}_{μνρ}(p, q) := δ_μν(p − q)_ρ + δ_νρ(q − r)_μ + δ_ρμ(r − p)_ν.

## Verdict lines
- **J1 (f-type uniqueness).** dim{T : (H), (S−), (W0)} = 0. PASS iff the exact rank gives 0.
- **J2 (d-type vanishing).** dim{T : (H), (S+), (W0)} = 0. PASS iff 0.
- **J3 (particular solution).** V^{YM} satisfies (H) and (S−), and the inhomogeneous Ward identity
  Σ_μ p_μV^{YM}_{μνρ}(p, q) = (r²δ_νρ − r_νr_ρ) − (q²δ_νρ − q_νq_ρ) identically. PASS iff exact.
  [Correction logged 2026-10-29 ~00:50 UTC, BEFORE any fl55_4 script existed: the first version of this line had the two
  brackets in the opposite order. Hand check at p = e_1, q = e_2, ν = ρ = 3: Σ_μp_μV^{YM}_{μ33} = δ_33(q − r)·p = 1, and
  r² − q² = 2 − 1 = 1, so the order written now is the one that holds for this V^{YM}. The verdict concerns the identity
  up to this convention-dependent overall sign; uniqueness (J1) does not depend on it.]
- **J-c1 (designed FAIL control).** Without (W0): dim{T : (H), (S−)} ≥ 1 (V^{YM} is a nonzero element). The control fires iff
  that dimension is ≥ 1; then J1's constraint (W0) is shown to be the one doing the work. If it is 0, J1 is INVALID.
- **J-c2 (designed FAIL control).** V^{YM} violates (W0) (Σ_μp_μV^{YM}_{μνρ} ≢ 0). Must fire.
- **J4 (informational, no verdict).** Print dim{(H), (S−)} and dim{(H), (S+)} (the numbers of independent hypercubic,
  Bose-(anti)symmetric degree-1 cubic structures).

## Overall
PASS iff J1, J2, J3 PASS and both controls fire. Run once; output kept unaltered.
