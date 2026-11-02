# b4b55_1 — pre-registered criteria (written 2026-10-29 ≈04:22Z, BEFORE any b4b55 script exists)

Owner: BFT4B55.md (Opus 5.5 worker, claude-opus-5-5). Target: the exact algebra of **Lemma AVG** (BFT4B55 §3):
on a gauge-invariant domain, Haar-averaging each polymer over the gauges at the endpoints of its support links gives
(i) the same total, (ii) locally gauge-invariant pieces, (iii) pieces that still depend only on their support, (iv) no
larger sup norm. Plus one hand-derived exact average, so the check is not only a restatement.

## Model (finite, exact)
- Gauge group G = S_3 (non-abelian), elements = permutations of {0,1,2} as tuples; composition (p∘q)(i) = p(q(i));
  permutation matrix M(q)[r][c] = 1 iff q(c) = r (so M(p∘q) = M(p)M(q)); χ(q) := tr M(q) = number of fixed points.
  Haar measure = uniform measure; all averages are exact Fractions. No floats anywhere.
- Lattice: 2D periodic 3×3 (9 sites, 18 links (s, μ) from s to s + e_μ, 9 plaquettes). Gauge action
  (U^g)(s, μ) = g(s) ∘ U(s, μ) ∘ g(s + e_μ)^{-1}. Plaquette at s: U_p = U(s,0)∘U(s+e0,1)∘U(s+e1,0)^{-1}∘U(s,1)^{-1}.
- Gauge-invariant total: E(U) := Σ_p [χ(U_p) + 2χ(U_p∘U_p)].
- Non-invariant local decomposition (Tset := plaquettes at (0,0), (1,1), (2,2)):
  - h(q) := M(q)[0][0] + 2M(q)[1][0] + 3M(q)[2][1];  h2(q) := M(q)[2][0] + M(q)[0][2];
  - for p at s: P_p := U(s,0)∘U(s+e0,1)∘U(s+e1,0)^{-1} (open 3-link path), C_p := U(s,1)^{-1}, T_p := M(P_p)[0][1]·M(C_p)[1][0];
  - plaquette polymer {p}: R({p}) := χ(U_p) + 2χ(U_p²) + h(bottom) + h(left) − h(top) − h(right) + [p ∈ Tset]·T_p
    − [p − e0 ∈ Tset]·h2(U_right(p)); support Ω({p}) := the 4 links of p;
  - domino polymer D_q (q ∈ Tset) = {q, q + e0}: R(D_q) := −T_q + h2(U_right(q+e0)); declared support Ω(D_q) := the 7 links of
    the two plaquettes (6 sites; it reads only 5 of them — the declared support is deliberately larger);
  - Σ_p R({p}) + Σ_q R(D_q) = E exactly (h terms cancel link by link; T and h2 terms cancel between {p} and D_q).
- R̄(X)(U) := average of R(X)(U^g) over g ∈ G^{S(Ω(X))}, S(Ω(X)) := endpoints of the links of Ω(X).

## Hand-derived prediction (BFT4B55 §8, derived before this file; must be confirmed by brute force)
- avg over both endpoint gauges of any single matrix entry M(aUb^{-1})[r][c] is 1/3; so avg h = 2, avg h2 = 2/3;
- avg of T_p over the gauges at s and s + e1 is **χ(U_p)/9** (count 4·fix(P_p∘C_p) of 36 pairs; P_p∘C_p = U_p);
- hence **R̄({p}) = χ(U_p) + 2χ(U_p²) + [p ∈ Tset]·χ(U_p)/9 − [p − e0 ∈ Tset]·(2/3)** (the h-constants 2 + 2 − 2 − 2 = 0) and
  **R̄(D_q) = −χ(U_q)/9 + 2/3**.

## Configurations and gauges (fixed in advance)
A: all links = identity. C: identity except U((0,0),0) = the transposition (0 1). R1, R2, R3: uniformly random links from
random.Random(seed) with seeds 101, 202, 303 (random only selects group elements; no floats). Gauges: two random gauges per
configuration from random.Random(seed + 7) and random.Random(seed + 11) (A and C use seeds 1, 2).

## Gates (all must PASS)
- **P0 (input identity):** Σ_X R(X)(U) = E(U) exactly, for A, C, R1-R3.
- **P1 (AVG (c)):** Σ_X R̄(X)(U) = E(U) exactly, for A, C, R1-R3.
- **P2 (AVG (b)):** R̄(X)(U^g) = R̄(X)(U) for every polymer X, every configuration, both gauges.
- **P3 (AVG (a), locality):** R̄(X)(U′) = R̄(X)(U) where U′ differs from U on one link outside Ω(X) (the first link in a fixed
  ordering outside Ω(X), replaced by its composition with (0 1 2)), every X, every configuration.
- **P4 (prediction):** R̄(X)(U) equals the hand-derived formula above for every X and configuration.
- **P5 (non-triviality):** (a) some R(X)(U^g) ≠ R(X)(U) among the tested (X, U, g) — the input pieces are genuinely not
  invariant; (b) for p = (0,0) ∈ Tset, R̄({p}) − χ(U_p) − 2χ(U_p²) differs between A and C — averaging produced a non-constant
  invariant correction beyond the invariant part put in by hand.
- **P6 (AVG (a), bound):** over all 6⁴ = 1296 configurations of the 4 links of p = (0,0): max|R̄({p})| ≤ max|R({p})|.

## Controls (each must FIRE, i.e. make the named gate FAIL; the overall verdict requires every control to fire)
- **K1:** average a Tset plaquette polymer over its support sites **minus the site s + e1** → P2 must fail for some (U, g).
- **K2:** drop the term −h(top) from R({p}) for p at (1,0) → P0 must fail for some configuration.
- **K3:** average over **constant** gauges only (g(s) = c for all s in S(Ω(X))) → P2 must fail for some (X, U, g) with a
  non-constant g.
- **K4:** replace χ(U_p)/9 by χ(U_p)/8 in P4's formula → P4 must fail for some (X, U).

## OVERALL
PASS iff P0-P6 all pass and K1-K4 all fire. Anything else is FAIL, reported as such.

## What this check can and cannot decide (stated in advance)
- **Can decide:** that Lemma AVG's averaging set (all endpoints of the support links) is the right one, that the identity,
  invariance and locality hold exactly in a non-abelian instance with genuinely non-invariant multi-link pieces whose averages
  are non-constant, and that my hand computation of those averages is right. A wrong averaging set, a missing Haar
  normalisation, or a wrong orientation convention would make P1/P2/P4 fail; the controls show the gates can fail.
- **Cannot decide:** holomorphy, complex domains, the continuous group SU(N), sup bounds on non-compact complex domains, any
  property of BFT-4's actual pieces, k- or T-uniformity, and — above all — **the consumer trace of Theorem T0 (BFT4B55 §2,
  §4-§5), which is a reading of the ledger, not a computation**. A PASS is evidence for Lemma AVG's algebra only.
