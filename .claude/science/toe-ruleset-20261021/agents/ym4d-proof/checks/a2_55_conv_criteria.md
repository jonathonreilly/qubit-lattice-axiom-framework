# a2_55_conv — pre-registered criteria (written before the script exists)

Written: see the UTC stamp in ALIGN2_55.md §1.11 (criteria file created before `a2_55_conv.py`).
Purpose: exact checks of the two algebraic identities behind Lemma CONV-P (ALIGN2_55 §1.4): Step 1 (the split of the
left-trivialised gauge generator) and Step 3 (the G_0-slot charge = point charges + divergence of w_A, first order in ȳ).
Arithmetic: python Fractions / ints only; no floats in any verdict.

## Part I — Step 1 identity, in a nilpotent Lie algebra (universal formal identity, finite exactly)
Algebra: strictly upper-triangular 6×6 rational matrices (ad nilpotent; exp, log are finite polynomials).
For random rational X, a, c (seeded), compute K := d/dt|_{t=0} log(e^{ta} e^{X} e^{−tc}) EXACTLY (log and exp as finite series in
nilpotent matrices; the t-derivative extracted as the coefficient of t of a polynomial in t computed with t as a formal variable,
i.e. matrices with polynomial-in-t entries truncated at degree 1).
- **I1 PASS iff** K == ψ_−(ad_X)a − ψ_+(ad_X)c, with ψ_∓ the Bernoulli series (exact rational coefficients, truncated beyond the
  nilpotency order), for 3 seeds.
- **I2 PASS iff** K − (a − c) == −[X, (a+c)/2] − ½Φ(ad_X)(c − a), Φ(z) = 2Σ_{n≥1}B_{2n}z^{2n}/(2n)!, for the same 3 seeds.
- **Controls (each must FIRE, i.e. the stated equality must FAIL for at least one seed):**
  CI1 ψ_− and ψ_+ swapped in I1; CI2 Φ dropped in I2 (K − (a − c) == −[X, (a+c)/2]); CI3 sign of the commutator flipped in I2.

## Part II — Step 3 decomposition, su(2) ≅ (R³, ×), d = 4 torus of side 3 (81 sites, 324 links, 486 plaquettes)
Random rational G(P) ∈ R³ on plaquettes, y(b) ∈ R³ on links, λ(z) ∈ R³ on sites (seeded). Orientation convention of ALIGN2_55 §1.4:
P = (z; μ<ν), ∂P = b1 + b2 − b3 − b4. λ̄(b) := (λ(tail) + λ(head))/2, dλ(b) := λ(head) − λ(tail), dy(P) := Σ_{b∈∂P} ε_b y(b).
LHS := Σ_P Σ_{b∈∂P} ε_b G(P)·(y(b) × λ̄(b))   (the first-order part of ⟨G, d(K′λ)⟩ up to the overall sign −).
RHS := Σ_P G(P)·(dy(P) × λ(z_P)) + Σ_{b′} W(b′)·dλ(b′), with W built from the coefficient table of §1.4 Step 3
(b1: ½ from b1's term and 1 from b2's term; b2: ½; b3: ½; b4: ½ from b4's term and 1 from b3's term), W(b′) := Σ c·ε_b (G(P) × y(b)).
- **II1 PASS iff** LHS == RHS exactly, for 3 seeds.
- **II2 PASS iff** the total coefficient mass Σ|c| received by every link equals 2(d − 1) = 6 exactly, and every site is the base of exactly
  d(d − 1)/2 = 6 plaquettes.
- **Controls (each must FIRE):** CII1 RHS without the W term; CII2 b1's own coefficient ½ replaced by 1; CII3 orientation sign of b3 flipped
  in the RHS's W only.

## What this check cannot decide (stated in advance)
No norm bound, no routing cost, no k- or T-uniformity, no s-slot (Step 4), nothing about the Φ remainder's size beyond the formal identity, and
nothing about su(N) beyond the universal formula (Part I) and su(2) (Part II). OVERALL PASS iff I1, I2, II1, II2 PASS and all six controls FIRE.
