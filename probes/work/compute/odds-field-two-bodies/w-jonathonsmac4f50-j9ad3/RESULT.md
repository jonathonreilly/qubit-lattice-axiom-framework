# Two bodies in the self-consistent odds field — run 1

Worker `w-jonathonsmac4f50-j9ad3`, model `claude-opus-5-5`. Blocks 41 and 42 were written by the same model family (Claude).

The run uses the full nonlinear six-outcome map on the torus of side 41 as the task specifies. Iteration is Anderson-accelerated on log-odds, to tolerance `10⁻¹²`. The run took 6175 s under heavy machine load.

`E = −Σ_{unformed x} log(Z_x/Z_void)` is a **declared bookkeeping quantity**, not an energy of the axioms. The pair interaction is `E_int = E(A+B) − E(A) − E(B)`.

## Exact: the first-order pair form

From block 42 T4(b) (checked in sympy for six neighbours):

`(1/6) Σ_s Π_y (1 + 3λ₁ m_y·e(s)) = 1 + 3λ₁² Σ_{y<y'} m_y·m_{y'} + O(m³)`

It has no first-order term. For two sources this gives the cross term

`E_int⁽¹⁾ = −3λ₁² Σ_x [M_A·M_B − Σ_y m_A(y)·m_B(y)]`,

where `M` is the sum over a site's six neighbours. This is evaluated from the two single-body fields, so the comparator has no free parameter.

## (2.95,1,2): 6λ₁ = 0.979, range 2.79

**Sign.** For every side (1, 2, 3) and every d from 6 to 16:
- **equal contents:** negative;
- **opposite contents:** positive;
- **orthogonal contents:** positive and second order. The first-order term vanishes identically (`~10⁻¹⁴`).

The orthogonal term is up to 0.74 of the equal-content magnitude at side 3, d = 6. It decays much faster, reaching `10⁻⁵` of its d = 6 value by d = 16 at side 1.

**Decay with separation.** For one record each, E_int(d)/E_int(6) is:

| d | E_int | G | G² | G*G |
|---|---|---|---|---|
| 8 | 0.535 | 0.365 | 0.133 | 0.488 |
| 10 | 0.274 | 0.143 | 0.020 | 0.239 |
| 12 | 0.139 | 0.058 | 0.003 | 0.117 |
| 14 | 0.070 | 0.025 | 0.0006 | 0.058 |
| 16 | 0.036 | 0.011 | 0.0001 | 0.029 |

- The rms of the log-ratio after the best constant is 0.068 for `G*G`, 0.41 for `G` and 1.95 for `G²`.
- The pair energy decays like the convolution of the two screened fields. That is `e^{−md}` without the `1/d`, which is what the first-order pair form predicts. It is not `G`, and not `G²`.
- E_int over the first-order pair form runs 0.80, 0.86, 0.90, 0.92, 0.93, 0.94 over d = 6..16. It approaches 1 at large d, and nonlinearity reduces it near.

**Side dependence at d = 12.** E_int(side)/E_int(1) is 1, 6.98, 20.2. The record count² is 1, 64, 729, so the interaction is nowhere near count².

It is capacity²:
- The far-lean ratios printed (squared: 1, 5.14, 10.8) were measured 8 steps beyond each cube's back face.
- That point lies 0.5 and 1 site further from the cube's centre for sides 2 and 3.
- With range 2.79 that offset alone costs `e^{2·0.5/2.79} = 1.43` and `e^{2/2.79} = 2.05`.
- Corrected, capacity² is 7.4 and 22, against 6.98 and 20.2 measured.

## (3,1,2): massless surface, on the torus

**What is measured.**
- The single-record `E` is −59.2, against −1.25 at (2.95,1,2).
- E_int is positive for equal, opposite and orthogonal contents at every d.
- It is nearly independent of d: equal contents with one record each give 29.9 → 24.8 from d = 6 to d = 16.
- It has the wrong sign against the first-order form for equal contents: the ratio is −0.26.

**Why.** This is the torus's neutral uniform mode. Each body polarises the whole torus, as in the companion computation `odds-field-massless-far-field` (tori there are image-dominated too).

**Wording in the printed summary.** The phrase "equal of both signs" for (3,1,2) means only "not all negative". In fact every equal-content value at (3,1,2) is positive.

**What would read the pair law on the massless surface.** Boxes with uniform odds held on the boundary, as the far-field computation uses. This is not done here.

## Summary

At (2.95,1,2), which is screened:
- equal contents attract in this bookkeeping and opposite contents repel;
- orthogonal contents interact only at second order;
- the interaction decays as `G*G`;
- it scales with capacity squared, not with record count.

At (3,1,2) the torus zero mode dominates, and the pair law cannot be read on a torus. The task stated no expectation, so there is no HIT.
