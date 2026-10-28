# c19 criteria (written BEFORE c19_gauge_taylor.py; session 8, 2026-10-27)

Purpose: test Lemma GT (gauge-invariant Taylor lemma, RTARGET §6) and its representation-theory input on explicit
SU(2) instances. A check tests instances, not the lemma's uniformity (PROOF.md session-2 caveat).

## Representation theory (exact, by enumeration of the 384 elements of B_4 = signed 4×4 permutation matrices)
- P1. Character norm of Λ²R⁴ under B_4: (1/384) Σ_g χ(g)² = 1 exactly (absolute irreducibility).
      Informational: the same norm over the rotation subgroup B_4 ∩ SO(4) (192 elements) is expected to be 2
      (self-dual ⊕ anti-self-dual), showing that reflections are needed.
- P2. The space of quadratic forms on su(2) ⊗ Λ²R⁴ invariant under B_4 and under 20 random Ad(SU(2)) elements has
      dimension exactly 1 (numerical rank of the averaged-projector, singular-value gap > 1e6).

## Lemma GT on explicit gauge-invariant functions of lattice SU(2) data
Background: radial-gauge su(2) field A_ν(x) = x^μ Ω_μν(x), Ω antisymmetric in μν, Ω(x) = Ω⁰ + Ω¹·x + Ω²·xx
(random anti-Hermitian coefficients, scaled so the derivatives are O(1)). F_μν(0) = 2Ω⁰_μν. Link transporters of
A^{(s)}(y) = sA(sy) along unit segments by a high-order product integrator (error well below s⁶ at the s used).
Region: all fine links/plaquettes with all sites in the box |x_μ| ≤ 1 (B_4- and ι-symmetric).
Test functions (all gauge invariant):
  F1 = Σ_p (1 - ½Re tr U_p)                                  (Wilson action of the region; = A_B)
  F2 = Σ_p (1 - ½Re tr U_p)² + Σ_{1×2 rectangles R} (1 - ½Re tr U_R) + Σ_{adjacent p,p'} (½Re tr U_p)(½Re tr U_p')
  F3 = Σ_{b ∈ star(0)} log[ I_1(2β|K_b|)/(β|K_b|) ],  K_b = staple sum of b (exact single-link Haar integral of
       exp(β ½Re tr(U K_b)), SU(2)); β = 1.3.
Controls (must show the property the lemma's hypothesis is there to exclude):
  C-a = F1 restricted to plaquettes in the (1,2) planes          (B_4 broken)
  C-b = F1 restricted to plaquettes with lower corner x_1 ≥ 0     (ι broken; also B_4 broken)
Backgrounds: ≥ 5 random ones, including an abelian (Cartan) one, one with F(0) self-dual, one anti-self-dual, and
generic ones.
Gauge-transformed copies: the same A transformed by a random smooth SU(2) gauge function (not radial).

Pass criteria (for F1, F2, F3 on every background):
- P3 (evenness). |f(s) - f(-s)| ≤ 1e-11·max(1, |f(s)|) for s ∈ {0.4, 0.2, 0.1}.
- P4 (no order s²). r(s) := (f(s) - f(0))/s⁴ has a finite limit: |r(s) - r(s/2)| / |r(s/2) - r(s/4)| ∈ [3, 5]
  for s = 0.2 (s² convergence), or both differences ≤ 1e-9·|r|.
- P5 (universality). c_F := Richardson limit of r(s)/Σ_{μ<ν}||F_μν(0)||²_HS agrees across all backgrounds to
  relative spread ≤ 1e-4.
- P6 (s⁶ remainder). R(s) := f(s) - f(0) - c_F s⁴ Σ||F_μν(0)||²: R(0.1)/R(0.05) ∈ [57.6, 70.4] (64 ± 10%), unless
  |R(0.05)| ≤ 1e-12 (then reported, not failed).
- P7 (gauge invariance). |f_gauge(s) - f_radial(s)| ≤ 1e-10 at s = 0.2.
- P8 (normalisation of F1). c_{F1} = n_B/(2N) = n_B/4 to relative 1e-6, n_B = number of region plaquettes per plane.
Controls:
- P9 (C-a must break universality). Relative spread of c across backgrounds > 10%.
- P10 (C-b must have an odd part). |f(s) - f(-s)| at s = 0.2 is > 1e-6 on some background, and its ratio between
  s = 0.2 and 0.1 is in [28.8, 35.2] (32 ± 10%, an s⁵ term) on that background.
Resource rules: one job, nice 10, OPENBLAS/OMP/MKL threads = 1, load < 8 and ≥ 25% free memory before start.
Result: PASS iff P1-P10 all pass. Any failure is reported as such, with no criterion edited after the run.

---
**[R78-fix] Disclosure (appended in session 9, 2026-10-27; the criteria above are unchanged).** REVIEW_S7_S8 (5) found,
from the session-8 transcript, that c19_gauge_taylor.py was edited at 12:38:38 UTC, before its first and only run
(12:38:51). The edit (i) removed a stray line, (ii) replaced sampled B_4 elements by the B_4 generators (three
adjacent transpositions and one reflection) in P2, and (iii) reduced the random Ad(SU(2)) elements in P2 from the
pre-registered 20 to 5. (iii) deviates from P2 as written above and was not disclosed in session 8. The reviewer judged
it mathematically harmless (5 generic elements generate a dense subgroup; the null-space gap is 6.6e14). The stored
output checks/c19_out.txt is from the edited script. The reflection-matters control requested by the review is c19b
(criteria in c19b_criteria.md, written before c19b_reflection_control.py).
