# s2 criteria (lane F session 2). Written BEFORE any s2 script exists. Not edited after the script exists.

Purpose: numerical sanity checks of the session-2 items of SF.md (§6 pre-statements). Not proofs. Post hoc diagnostics, if any,
are labelled as such in the output and do not change these criteria.

## A. Lemma LOC-s + Corollary CE-exp-𝒞 (strictly local H) on a d = 1 toy
Model: ring of 24 sites, n = 1 (Z_y real), Z_y i.i.d. uniform on [-p, p], p = 1.3. Kernel 𝒞(b, y) = 0.7·e^{-0.9·dist(b,y)}
(circular distance; every entry non-zero: NOT finite range). X = sites {0, 1}; base set B = sites at distance ≤ 2 from X (the
X^+ analogue; 6 sites... computed by the script); far set F = the 12 sites nearest to B outside B (the other far sites are frozen
at s = 0, i.e. Z = 0 there, in the model, so the far set is exactly 12 sites; disclosed model choice). δ(y) := distance from y to X.
μ := 0.45. Activity H(A) := exp(A_0) + A_0·A_1² (entire). Φ(Z) := H(𝒞Z). Pieces F_S := Σ_{T⊂S}(-1)^{|S∖T|}Φ(1_{B∪T}·Z), S ⊂ F
(fast Möbius transform over 2^12 subsets). 20 random Z samples (seed 2).
- A1 PASS iff for every sample |Σ_SF_S - Φ(1_{B∪F}·Z)| ≤ 1e-11·max(1, |Φ|).
- A2 PASS iff for 200 random (sample, S) pairs, re-drawing Z outside B ∪ S (inside F) changes F_S by ≤ 1e-12·max(1, max|F_S|).
- A3 PASS iff for every sample and every S: |F_S| ≤ h·Π_{y∈S}e^{-μδ(y)} with h := e^{R_0} + R_0R_1², R_b := pΣ_{y∈B∪F}|𝒞(b, y)|λ_y,
  λ_y := 1 (y ∈ B), 1 + e^{μδ(y)} (y ∈ F). (The sup of |H| over the polydisc reached is ≤ h by the triangle inequality.)
- A4 (non-vacuity) PASS iff the maximum over samples and S ≠ ∅ of the ratio in A3 is ≥ 1e-4, and some |S| ≥ 3 has ratio ≥ 1e-8.

## B. Lemma HULL and the distance relation in d = 4
Torus of 7⁴ CE cubes, M = 2 (fine torus 14⁴). 200 random trials: X = a random polymer of 1-3 cubes built by random *-adjacent
growth; S = 1-4 random sites outside ∪X^+. Y := X^+ ∪ {cubes whose closed cube meets the segment from the centre of q(y) to the
centre of the lexicographically first ℓ^∞-nearest cube of X^+ (in the torus lift realising the distance)}.
- B1 PASS iff in every trial Y is *-connected and contains q(y) for every y ∈ S.
- B2 PASS iff in every trial the explicit length of the constructed tree's added parts, Σ_y(Euclidean segment length + 1), is
  ≤ Σ_y(2n(y, X) + 1).
- B3 PASS iff in every trial δ(y, X) > M·n(y, X) and n(y, X) ≥ 1 for every y ∈ S (δ by brute force over the sites of ∪X).

## C. Constants of Theorem CE-exp
κ_0 = 16 log 12800; κ_c := 3κ_0 + 4; κ' = κ_c + 16 log 2.
- C1 (record) κ', 273κ' + 1296w_8, w_8 = Σ_{n≥1}(2n+1)⁴e^{-8n}. PASS iff w_8 ≤ 0.03.
- C2 With μ = m_1 = 4.83e-11 (N5-w0, PROOF l.5404 as quoted in SF §3.3 (V7)), M_min := the least integer M with
  μM ≥ 3κ' + 4 log M + 8. PASS iff at M = M_min the directly summed W (log-domain) is ≤ w_8 and M_min < 2.646e15 (SF-V (V7)'s
  value). Record M_min.

## D. Lemma SF-J' and the D_N coverage (Haar samples, QR of complex Ginibre with phase fix, det normalised to 1; seed 3)
4·10⁴ samples each for N = 3, 4; 10⁴ for N = 2, 5.
- D1 PASS iff the SU(3) fraction with principal log traceless and no eigenvalue -1 lies in [0.96, 0.99].
- D2 PASS iff the SU(4) fraction lies in [0.93, 0.965].
- D3 PASS iff for every sample (N = 2, 3, 4, 5) the number of angle windows [c, c + 2π) whose representative sum is 0 is
  exactly 1 (distinct eigenvalues), checked by scanning c over the sorted angles.

## E. Lemma BS (base set), SU(2) and SU(3)
10⁴ random real plaquettes: links U_i = exp(small random su(N)) with ||1 - U_p|| ≤ 0.2 (rejection), Z_i real su(N) with
||Z_i|| ≤ s = 0.01.
- E1 PASS iff ||1 - U'_p|| ≤ ||1 - U_p|| + 4(e^s - 1) in every sample (U'_p the plaquette of the U_ie^{Z_i}).
- E2 PASS iff 4(e^{0.01} - 1) ≤ 4.05·0.01.

OVERALL PASS iff every PASS/FAIL criterion above passes. Runtime target < 5 min; numeric lock, nice 10, BLAS threads 1.
