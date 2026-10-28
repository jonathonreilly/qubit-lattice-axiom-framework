# cc55 — criteria (written BEFORE any cc55 script exists)

Worker: claude-opus-5-5 (COFUN_CC.md). Written 2026-10-28 ≈23:20 UTC. No `checks/cc55_*.py` exists at the time of
writing. Exact arithmetic only: Python `fractions.Fraction` and ints; no numpy, no BLAS, no floats in any verdict;
single thread; `python3 -I`. Independent construction: no code copied or imported from r55t, r55b, bb9, bb10, bb11, cf1.

## Purpose (algebra only)
Test, in the lane's abelian model class, the exact identities that COFUN_CC.md's assembly of (CO-fun) on class (cc)
uses. Nothing here measures k-uniformity or any analytic constant (Theorem COF, BL-4, Proposition W are quoted inputs).

## Model
d = 2, L = 3, roots = block centres (level-(i+1) site X <-> level-i site 3X + (1,1)), block B(X) = 3X + {0,1,2}^2.
Level i torus side N_i = T·3^{k-i}. (dλ)(z,μ) = λ(z+e_μ) − λ(z); (d*j)(z) = Σ_μ [j(z−e_μ,μ) − j(z,μ)];
(dA)(z) = A(z,0) + A(z+e_0,1) − A(z+e_1,0) − A(z,1); d* on 2-forms = transpose. ev λ(X) = λ(3X+(1,1)); ev^T = placement.
Straight average (Q_str A)(X,μ) = 3^{-2} Σ_{y∈B(X)} Σ_{t<3} A(y+te_μ, μ).
Root map for a fixed coordinate order σ ∈ {(0,1),(1,0)}: (Q^σ A)(X,μ) = 3^{-2} Σ_{y∈B(X)} ∫_{T^σ_y} A,
T^σ_y = P^σ(c_X→y) · S_y · P^σ(c_{X+e_μ}→y+3e_μ)^{-1} (axial paths, coordinates moved in the order σ; S_y the straight
leg). The lane's operator (LINEAR_PACKAGE §1.2) is the ORDER-AVERAGED Q^avg := ½(Q^{01} + Q^{10}); h^σ(A)(X) :=
3^{-2}Σ_y ∫_{P^σ(c_X→y)} A, h^avg := ½(h^{01} + h^{10}). Chain energy E_src (BFT_A §7.1) with κ_l := l + 1 (distinct),
r_l(x) := Q x_l − x_{l+1}, x_k := B_k. Linear source functional L_S(x) := Σ_l[⟨G_l, dx_l⟩ + ⟨j_l, x_l⟩ + ⟨s_l, r_l(x)⟩]
(x_k = 0). Chain coefficients S_l := d*G_l + j_l + Q^T s_l − s_{l−1}. D(S) := Σ_{l<k} ev^{(0→l)T} d*S_l (pointwise).
π_l(j) := 3^{(d−1)(k−l)} max|j| = 3^{k−l} max|j| (the d = 2 analogue of L^{3(k−l)}).
Block flux Φ_l: level-l 1-form → level-k 1-form, Φ_l j(X,μ) := Σ of j over the level-l μ-links that leave the level-k
block of X through its upper μ-face. Root charges q := R_k(D(S)) (the level-k function with ev^{(0→k)T}q = D(S)).
Flux candidate b(S) := Σ_{l<k} Φ_l(j_l) + s_{k−1}. Decomposed source S' := (G_l; j'_l; s'_l) with j'_l = j_l (l < k−1),
j'_{k−1} := j_{k−1} − Q^T Σ_l Φ_l(j_l), s'_l = s_l (l ≤ k−2), s'_{k−1} := 0.

Random (cc) sources: integer-coefficient sums (seeded `random.Random`, seeds 5501.. fixed in the script) of
(g1) divergence-form slots G_l (random 2-forms, entries in [−3,3]); (g2) residual slots s_l at EVERY level incl. the
top (entries in [−3,3]); (g3) (CC-0) non-level-wise pairs: j_l = straight level-l path between adjacent level-(l+1)
roots, j_{l+1} = −(the corresponding single level-(l+1) link); (g4) root-charged plain currents: straight level-l
paths between adjacent level-k roots; (g5) co-closed plain currents d*(random 2-form) in the j slot. All operators
built with Q^avg unless a test says otherwise.

## Part A — no solve. Configurations (k, T) = (2, 3) and (3, 2).
- **A1 (sanity, can fail):** Q^σ d = d ev and Q^σ = Q_str − d∘h^σ exactly, σ ∈ {01, 10, avg}, on 3 random λ / A per level.
- **A2 (FLUX identity):** for 3 random level-l 1-forms j per l < k: d*_k Φ_l j = blocksum_l(d*_l j) exactly, and
  max|Φ_l j| ≤ 3^{k−l} max|j|. PASS iff all hold.
- **A3 (construction sanity):** each random S has D(S) supported on the level-k roots with total 0, and q ≠ 0.
  FAIL if any S is not (cc) or every q vanishes (vacuous).
- **A4 (root charges are the divergence of the explicit flux):** for 4 random (cc) sources per configuration:
  d*b(S) = q exactly, and max|b(S)| ≤ c(S) := Σ_{l<k} π_l(j_l) + max|s_{k−1}|. PASS iff all hold.
- **A5 (decomposition as an identity of functionals):** for each S of A4 and 8 random chains x (x_k = 0, entries in
  [−4,4]): L_S(x) = L_{S'}(x) + ⟨b(S), r_{k−1}(x)⟩ exactly.
- **A6 (S' is (CC-0) and Lemma SPLIT holds for it pointwise):** D(S') = 0, D(S'^j) = 0, D(S'^s) = 0, D(S'^G) = 0 at every
  level-0 site.
- **A7 (X-T7 defect, independent code):** for s_{k−1} random alone: D = ev^{(0→k)T} d*s_{k−1} pointwise, nonzero,
  root-supported, total 0. (A PASS confirms that Lemma SPLIT's "D(S^s) = 0" fails for the top slot.)
- **A8 (top residual source = datum shift, Lemma TS in functional form):** for b of A4 and 8 random chains x:
  [E_src(x; top residual source b, B_k = 0) − E(x; B_k = b/κ_{k−1}, no source)] is the same for all 8 x and equals
  −||b||²/(2κ_{k−1}).
- **A9 (self-flux identity, every chain):** for 8 random chains x with x_k = 0: D(Hx) = κ_{k−1} ev^{(0→k)T} d*r_{k−1}(x)
  pointwise, where (Hx)_0 = d*dx_0 + κ_0 Q^T r_0, (Hx)_l = κ_l Q^T r_l − κ_{l−1} r_{l−1}.
- **Controls (each must FIRE, i.e. the stated identity must FAIL):**
  C1: b with Φ_0 omitted: d*b ≠ q for at least one S. C2: A5 with j'_{k−1} built with Q^{01 T} while the chain uses
  Q^avg: identity fails for some (S, x). C3: A8 with κ_{k−2} in place of κ_{k−1}: differences not constant.
  C4: A9 with κ_0 in place of κ_{k−1}: fails. C5: A4's bound with the max|s_{k−1}| term dropped, on the source
  s_{k−1} = δ_b alone: fails.

## Part B — exact solve, (k, T) = (1, 3) (level-0 9×9, 162 links; level 1 3×3)
Gauge: x_0 := 0 on the axial tree (order 01 from the root) of each level-1 block (72 links), 90 unknowns; solve the
reduced normal equations exactly; then check the FULL gradient vanishes.
- **B1 (sanity):** for 3 random (cc) sources with q ≠ 0 (generators g1, g2 incl. the top slot s_0, g4, g5): the solved
  x satisfies Hx = S on all 162 links (with x_1 = 0). FAIL if any residual ≠ 0.
- **B2 (self-flux at critical points):** κ_0 d*r_0(x) = q exactly, q ≠ 0.
- **B3 (additivity of the decomposition):** with x' the response to S' and y the source-free minimiser with datum
  b/κ_0: dx_0 = dx'_0 + dy_0 at every plaquette, and r_0(x) = r_0(x') + r_0(y) + b/κ_0 at every level-1 link.
- **B4 (data map is h-independent):** for 2 random data B_1 and for B_1 = b/κ_0: the minimisers for the chains built
  with Q^avg, Q^{01}, Q^{10} have identical dx_0 (every plaquette) and identical r_0 (every level-1 link).
  Non-vacuity control C6 (must FIRE): the three energies differ as functions (E differs at some random x for some pair),
  and the gauge-fixed minimisers' x_0 differ for some pair.
- **B5 (designed contrast, informational, NOT a verdict on any claim):** for a root-charged plain-current source, the
  responses with chain Q^avg and chain Q^{01} (same source functional) differ in dx_0 somewhere. Expected: differ. If they
  agree, it is reported and no claim of COFUN_CC rests on B5.

## Verdict rule
ALL of A1-A9, B1-B4 PASS and C1-C6 FIRE ⇒ "the algebra used by COFUN_CC holds in the model". Any FAIL is reported as a
FAIL and the claim resting on it is downgraded; no criterion is retuned after a run; a rerun after a code fix is a new
file with the fix stated in its header.

## Scope limitation (stated before running)
d = 2, k ≤ 3, abelian, L = 3; orders averaged over the 2 orders of d = 2 (the lane averages 24 in d = 4). Algebra only:
k-, T-uniformity of Theorem COF, BL-4, Proposition W and Corollary FP is quoted, not tested. Part B has k = 1 only (the
cascade is trivial there); the cascade identities at k = 2, 3 are tested in no-solve form (A5, A6, A9).
