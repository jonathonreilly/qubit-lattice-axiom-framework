# c19b criteria (written BEFORE c19b_reflection_control.py; session 9, 2026-10-27)

Purpose (REVIEW_S7_S8 (5), binding fix 9): a control that is invariant under the rotation subgroup B_4 ∩ SO(4) (which
contains ι = -1) and under gauge transformations, but ODD under reflections. Lemma GT's hypothesis (ii) asks for all of
B_4; without the reflections, Λ²R⁴ splits into self-dual and anti-self-dual parts (c19 P1: norm 2), and a second
invariant (ε^{μνρσ} tr Φ_μν Φ_ρσ) is allowed (failure mode R4-F2). The control must show this failure mode is real, so
that c19's agreement c_SD = c_ASD is evidence that the reflection hypothesis is load-bearing, not automatic.

Setting: as c19 (same backgrounds generator, transporter integrator, box |x_μ| ≤ 1, SU(2)), imported from
c19_gauge_taylor.py.
Control function (gauge invariant: every factor is a loop based at the site 0):
  C_μν := (1/4) Σ_{4 clover leaves at 0 in the (μ,ν) plane} (W - W^†)/2,  leaves = based loops [μ,ν,-μ,-ν], [ν,-μ,-ν,μ],
          [-μ,-ν,μ,ν], [-ν,μ,ν,-μ];
  Q_ε := Σ_{μ,ν,ρ,σ} ε^{μνρσ} (-½) Re tr(C_μν C_ρσ).
Combined function: G := F1 + Q_ε (F1 = c19's Wilson sum over the box), to show universality of c fails.
Normalisation: r(s) := (f(s) - f(0))/s⁴, c := Richardson limit of r(s)/Σ_{μ<ν}||F_μν(0)||²_HS (as c19).
Backgrounds: c19's make_background with kinds abelian, sd, asd, generic, generic (5), from c19's seeded generator.
Reflection R = diag(-1,1,1,1): (R·A)(x) := R A(R^{-1}x) (the data action under which GT's (ii) is stated).

Criteria:
- Q1 (gauge invariance holds). |Q_ε(gauge-transformed) - Q_ε(radial)| ≤ 1e-10 at s = 0.2 on every background.
- Q2 (ι-evenness holds). |Q_ε(s) - Q_ε(-s)| ≤ 1e-11·max(1,|Q_ε(s)|) for s ∈ {0.4, 0.2, 0.1}, every background.
- Q3 (order s² vanishes). As c19 P4, for Q_ε, every background with |r(0.1)| > 1e-8.
- Q4 (reflection oddness). |Q_ε(R·A; s) + Q_ε(A; s)| ≤ 1e-10 at s = 0.2, and |Q_ε(A; 0.2)| > 1e-6, on the generic
  backgrounds.
- Q5 (the control's point: SD vs ASD differ). c(Q_ε) on the sd and asd backgrounds differ by more than 10% of
  max(|c_sd|, |c_asd|), and max(|c_sd|, |c_asd|) > 1e-6. (Informational: expected c_sd ≈ -c_asd, c_abelian = 0 if the
  abelian F(0) has zero ε·F·F.)
- Q6 (universality of G fails). The relative spread of c(G) across the 5 backgrounds is > 10%.
Resource rules: one job, nice 10, OPENBLAS/OMP/MKL threads = 1, load < 8 and ≥ 25% free memory before start.
Result: PASS iff Q1-Q6 all pass. Any failure is reported as such; no criterion is edited after the run.
