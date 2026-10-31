# r55b_dip — criteria (written BEFORE any r55b script exists)

Reviewer: claude-opus-5-5 (REVIEW55_BFTB). Written 2026-10-28 ≈22:45 UTC. No script `checks/r55b_*.py` exists
at the time of writing. Exact arithmetic only: Python `fractions.Fraction` and ints, no numpy, no BLAS, no floats
in any verdict. Single thread. Independent construction (no code copied from bb9b/bb10/bb11).

## Purpose
Decide, in the lane's own abelian model class, two algebraic claims that bear on BFT_B §35.2 (Lemma SPLIT) and
§35.7 (Proposition COF-res's "(CO-fun) as stated is FALSE"):

(I) **Root-dipole identity.** For a level-(k-1) plain current j = q·path_b, where path_b is the straight level-(k-1)
path from the root c_X to the root c_{X+e_μ} (b = (X, μ) a level-k link), there is a level-(k-1) 2-form G supported in
B(X) ∪ B(X+e_μ) such that, as linear functionals on chains with x_k = 0,
   ⟨path_b, x_{k-1}⟩ = (Q_{k-1}x_{k-1})(b) + ⟨G, d x_{k-1}⟩ = r_{k-1}(x)(b) + ⟨G, d x_{k-1}⟩,
i.e. the root-charged plain current q·path_b is the SAME source as (residual source s_{k-1} = qδ_b, divergence-form
source G_{k-1} = qG). (Derived by hand in REVIEW55_BFTB; this check tests the algebra, not any analytic bound.)

(II) **Lemma SPLIT pointwise.** The composite divergence D(S) = Σ_l ev^{(0→l)T}d*S_l of a TOP residual source
s_{k-1} is the nonzero root-supported function ev^{(0→k)T}d*s_{k-1}, not 0; a lower residual source s_l (l < k-1) has
D = 0 pointwise; and a source with D(S) = 0 pointwise can have plain-current part with D(S^j) ≠ 0.

## Model
d = 2, L = 3, k = 2, coarse side T = 3 (level sides 27, 9, 3), roots = block centres (level-(l+1) site X ↔ level-l site
3X + (1,1)), block B(X) = 3X + {0,1,2}². Linearised root map with ONE fixed axial order (coordinate 0 then 1):
(Q A)(X, μ) = 3^{-2} Σ_{y∈B(X)} ∫_{T_y} A,  T_y = a(c_X→y) · S_y · a(c_{X+e_μ}→y+3e_μ)^{-1},
a(·→·) the axial path (first coordinate 0, then 1), S_y the straight 3-link path y → y + 3e_μ.
d on functions: (dλ)(z, μ) = λ(z+e_μ) − λ(z); on 1-forms (d = 2, one plaquette per site):
(dA)(z) = A(z,0) + A(z+e_0,1) − A(z+e_1,0) − A(z,1); d* = transpose in the standard pairing.
T = 3 is chosen so that B(X) ∪ B(X+e_μ) (a 6×3 box at level 1) does not wrap the level-1 torus (side 9).

## Tests (each PASS/FAIL fixed now)
- **D1 (construction sanity, could fail):** root covariance Q_1 dλ = d ev λ exactly, for all level-2 links and 5 random
  level-1 functions λ (entries random integers in [−5, 5]). FAIL if any entry differs. [Also run for Q_0 at level 0→1
  with 3 random level-0 λ.]
- **D2 (identity (I), the core):** for b = (X, μ) with X = (1,1), μ = 0 and μ = 1: v := path_b − Q_1^Tδ_b. PASS requires
  ALL of: (a) d*v = 0 exactly; (b) every link carrying v ≠ 0 has both endpoints in B(X) ∪ B(X+e_μ); (c) the exact
  linear system d*G = v, with G restricted to plaquettes having all four corners in B(X) ∪ B(X+e_μ), is solvable
  (exact Gaussian elimination over ℚ); (d) for 20 random level-1 1-forms x (integers in [−5, 5]):
  ⟨path_b, x⟩ = (Q_1x)(b) + ⟨G, dx⟩ exactly. FAIL if any of (a)-(d) fails.
- **D3 (non-vacuity of D2):** v ≠ 0, G ≠ 0, and ev^{(1→2)T}-placed divergence of path_b is nonzero (the source q·path_b
  has D ≠ 0 at the two level-2 roots: it is in the composite-co-closed class (cc) but NOT in (CC-0)). FAIL if any is 0.
- **D4 (control, must fire):** with G replaced by 0, the identity of D2 (d) fails for at least one of the 20 random x.
  If the control does NOT fire (identity holds with G = 0), D2 is declared vacuous and the identity's content unsupported.
- **D5 (Lemma SPLIT, top slot):** for s_1 := δ_b (level-2 link b, X = (1,1), μ = 0): the chain-source coefficient on x_1
  is S_1 = Q_1^Ts_1 (x_2 = data, fixed), S_0 = 0. PASS requires: d*(Q_1^Tδ_b) (level-1 function) is NONZERO, is supported
  on level-2 roots (as level-1 sites), has total 0, and equals ev^{(1→2)T}d*δ_b exactly. (A PASS refutes the pointwise
  "D(S^s) = 0" of BFT_B §35.2 for the top residual slot.)
- **D6 (Lemma SPLIT, lower slot, control of D5):** for 3 random level-1 1-forms s_0: S_0 = Q_0^Ts_0, S_1 = −s_0, and
  D(S) = d*S_0 + ev^{(0→1)T}d*S_1 must be 0 at every level-0 site exactly. PASS if 0; FAIL otherwise.
- **D7 (Lemma SPLIT's "(CC-0) for S ⇒ (CC-0) for S^j"):** S := (s_1 = δ_b) + (j_1 = −path_b). PASS (i.e. the
  counterexample is exhibited) iff D(S) = 0 at every level-0 site AND D(S^j) ≠ 0 at some level-0 site.
- **D8 (D7's source is a pure divergence-form source):** for 20 random level-1 x with x_2 = 0:
  ⟨δ_b, r_1(x)⟩ − ⟨path_b, x_1⟩ = −⟨G, dx_1⟩ exactly (G from D2). PASS/FAIL accordingly.

## Verdict rule
ALL of D1-D3, D5-D8 PASS and D4 FIRES ⇒ "identity (I) and claim (II) hold in the model (algebra only)".
Any FAIL is reported as a FAIL and the corresponding review finding is downgraded to NOT-VERIFIED; no criterion is
retuned after a run; a rerun after a code fix must be a new file with the fix stated in its header.

## Scope limitation (stated before running)
d = 2, k = 2, abelian, one axial order (the lane's S4′ averages 24 orders in d = 4; the identity uses only that every
contour runs root to root inside B(X) ∪ B(X+e_μ), which holds for every order). The check tests algebra only; the
analytic step "the (s, G) response is bounded k-, T-uniformly" is lane A's Corollary LIN0 / Theorem GU (quoted, not
checked here).

---

# r55b_num — criteria for the exact-rational number checks (written before the script)

- **N1 (K_f, BFT_B §29.3 / §27.2):** x := 3^{−9/4}; decide by x⁴ = 3^{−9} with rational endpoints: PASS iff
  8.737 ≤ 8/(1 − x) ≤ 8.74. Also report whether the printed intermediate "3^{−2.25} = 0.08434" lies in a rational
  interval containing x (expected NOT: true x ∈ [0.08442, 0.08443]); this is recorded, not a FAIL of K_f.
- **N2 (C_C base, §35.4):** 1 + 8·(27/26) = 121/13 ≤ 9.31 exactly. PASS/FAIL.
- **N3 (ΓT-op (d) constant, §25.1 (d) / §36.2):** 2M_n/n = 4(4n + 1)/n ≤ 20 for n = 3^k, k = 1..12, exactly; and the
  1D-Green identity behind Lemma N1G: for the cycle Z_M, g(t) := (t − M/2)²/(2M) satisfies −Δg = δ_0 − 1/M exactly and
  2(g(0) − g(M/2)) = M/4, for M = 4, 6, 8, 10, 12, 50. PASS/FAIL.
