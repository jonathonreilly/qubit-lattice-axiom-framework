# Check: library/a41-avg.md (A4.1, change of averaging)

Checked line by line by Claude (Opus 5.5), 2026-11-08. One reading.
Note at branch `claude/ym4d-hard-route` head `41b3bad80`.

**Verdict: FIX.**

The ported steps and the elementary algebra check out. Every cited
source range says what the note says. No step is false.

The stopping supplier SC-HESS is not yet a precise lemma. It is also
stronger than A4.1 needs. Routes 1 and 2 stop on objections that do not
hit an operator-level comparison. A concrete fourth route exists. It is
Balaban's own method, and the note does not attempt it. The note should
add that route before it may claim stop (c).

Sources read: Y = `YM4_1400.tex` (scratchpad copy; line numbers match
the note). SA and I = `/Users/jonreilly/ym4d-lead/sa/YM4_sketch_500.tex`
and `theorem_0_complete_account_raw_I.tex`. The note's `/tmp` copies are
gone. I did not confirm the commit of the SA/I copies; every cited
line range matched its content.

## Findings

1. **Note 45; Y 2148–2156, 2169–2173; SA 3898–3906. CONFIRMED.**
   A4.1 text, its retention at general scope, and the SA obligation
   match.

2. **Note 47–48; SA 7065–7116, 7406–7424, 7798; I 24239–24338.
   CONFIRMED.** The mean is Federbush's mean of the coordinate-order
   paths. SA 1a.1.13 is a sketch with a geometric-series proof note at
   7798. I 24314–24338 is CMP 98 (92), the comb fundamental equality.

3. **Note 52; `b98p5.md` 2.5 (lines 423–435). CONFIRMED.** The comb row
   estimates (10)–(16) hold for the symmetrised prescription with the
   same enlarged constants. b98p5 says this is not an equality of the
   two curved maps.

4. **Note 90–106, eqs (1)–(2); Y 16661–16827. CONFIRMED.** Real
   reference, `T^{-1}Q^natural = Q_c A + C(A)`, `C'(0)=E`, and
   `H_A = H_c(1+C'(A)H_c)^{-1}T^{-1}` match. Repair (minor): line 100
   must state the condition `K_1 L epsilon <= 1/2` (Y 16792).

5. **Note 108–110; Y 16775–16800. CONFIRMED.** (Y 16784.) Transpose bounds use
   rows at levels `n-1, n, n+1`, weight sum `(L^3+2) xi_n^{-3}`. No depth
   factor.

6. **Note 113–125, eq (3); SA 11586–11598 (PX146–PX148). CONFIRMED.**
   `t_s = L^{s-j}`; the sum over `s<j` is below `1/(L-1)`. The product
   bound and the warning against levelwise constants are SA's.

7. **Note 127–139, eq (4); SA 11543–11547 (PX143–PX144); Y 3712.
   CONFIRMED.** Same contour in all four objects is Y 3712, verbatim in
   meaning.

8. **Note 141–145; Y 3991–4004, 34388–34460. CONFIRMED.** The tower
   axial gauge jumps by `O(L^j eta sup|A|)` across blocks (Y 4004).

9. **Note 147–162, eq (5); SA 11143–11254 (PX93–PX105). CONFIRMED.**
   `K_L`, the coarse Hessian formula, the outward factor (PX99) and the
   next-fibre multiplier `h_V^T J` and both GF derivatives (PX104) match.

10. **Note 166–169; Y 23838–23847. CONFIRMED.** Y says the physical
    constrained Hessian does not identify a separately defined
    `Delta'_pi[J]`.

11. **Note 244–253, eq (9). CONFIRMED.** `E_c+R = E_c(I+G_cR)` and
    congruence give (9). It needs `T_f` square and invertible.

12. **Note 266–273. CONFIRMED.** For `t` in `G^c`, `Ad(t)` preserves the
    bilinear trace form, so its bilinear transpose is its inverse.

13. **Note 280–289, eq (10); SA PX93. CONFIRMED** as algebra.
    **MISMATCH** as a stop. The surviving term `<S', D^2 Psi>` is a
    contraction of the multiplier with the constraint second jet. SA
    11612–11639 (PX153–PX154) bounds it by `C_L gamma_omega` in the mass
    norms, for each scheme separately. GW1 (2) works below a fixed current
    ceiling `j_*`. So this term is a small perturbation, not an obstruction.
    Route 1 shows only that the term does not cancel. Repair: say so, or
    show that the term is not small at the actual current ceiling.

14. **Note 293–303, eq (11); Y 4034. CONFIRMED.** Ported seam example;
    the note correctly does not count it as a counterexample.

15. **Note 307–327, eqs (12)–(13). CONFIRMED.** `Q_c(I+H_cE) = Q_c+E`
    gives `(Q_c+E)T_0 = Q_c` and `Q_m T_0 = T Q_c`. The kernels map
    bijectively. The norm bounds `(1-kappa)^{-1}` and `1+kappa` are right.

16. **Note 331–352, eq (14). CONFIRMED** as algebra. **UNCLEAR** as a
    stop. (14) shows a mean-critical field need not be comb-critical. An
    operator comparison at a common pair `(U,J)` with independent `J` does
    not need that. At a critical field, `omega = H^T j_U` for every right
    inverse `H`, since `j_U = Q^T omega` (SA PX93). So the multiplier is
    selected there. The note's objection applies to its fibre formulation
    only.

17. **Note 356–382, eq (15); `pi-admit.md` 459–495 (its eq (17)); Y
    29144–29212, 35771–35822. CONFIRMED.** Inner action versus PI's
    whole-action Hessian differ by `eta^{-2}||A||^2` at a flat slab. The
    stop at PI-ADMIT is correct. Minor: cite pi-admit's tag (17).

18. **Note 384–386. CONFIRMED in part.** The three routes are distinct.
    Route 3 fails where stated. Routes 1 and 2 stop on objections listed
    in findings 13 and 16, not on a failed estimate.

19. **Note 171–232, SC-HESS (6)–(8). MISMATCH: under-specified.**
    `E_c^J` is "the corresponding specified comb current precision" whose
    "restriction and current completion must be the required ones". It is
    not defined. The gauge-row part of `T_f` is not constructed. Line 200
    says verifying `T_f` is itself part of the missing comparison. So (8)
    is a template, not a lemma that fails three routes. Repair: define
    `E_c^J` as GW1 (2)'s `Delta_a - K_J` at the same `(U,J)` and the same
    whole action, or replace SC-HESS by finding 21's statement.

20. **SC-HESS versus A4.1. MISMATCH: stronger than needed.** A4.1 (Y
    2148–2156) asks for a uniform intertwiner with its coarse gauge
    factor, and for the transferred objects to obey A1–A3. It does not ask
    for a congruence of two gauge-fixed fibre charts. Y 16858–16863 states
    the remaining step as a comparison of fine quadratic forms with Y
    (mb:comb-fine-operator). Y 4025 states Balaban's form: for real
    `U_0`, `Ad(t)` cancels from `Q^* a Q`, and the forms defining `G'`,
    `R`, `G_k`, `H_k` differ by local forms of relative size `C alpha_0`.
    Neither uses a fibre chart `T_f` or a flat-form match. SC-HESS adds
    these.

21. **Concrete route not attempted. Route 4: saddle perturbation on the
    fixed fine space.** This is Balaban's method (CMP 95/96 perturbation
    of `G` by small local forms; Y 4025) in Y 29049–29212's saddle form.
    State it as follows.

    Fix an admitted pair `(U,J)` of GW1, `U = e^{i eta A} U_0`, `U_0`
    real, `|A|_{(-1)} <= r`, `|J|_{(-3)} <= j_*`. Use PI's whole action
    and boundary convention for both schemes. For `s` in `{m,c}` let the
    saddle operator on `X + Y + Z` be

        S_s = [[K_L^s, K_s^T, Gam_s^T], [K_s, 0, 0], [Gam_s, 0, 0]],

    with `K_L^s = Delta^W_U - <omega_s, D^2 q_s>`, `omega_s = H_s^T J`,
    `K_s` the straightened rows and `Gam_s = R_0 R_s D_U^T` the gauge rows,
    each built with one contour type in all four objects (Y 3712). The
    intertwiner is `diag(I_X, T, T')`: identity on fine fields, the row
    transport `T` and the site transport `T'` of Y (mb:mean-comb-comparison).
    These are the coarse gauge factors. Claim: the defect

        D = diag(I, T^{-1}, T'^{-1}) S_m diag(I, T^{-T}, T'^{-T}) - S_c

    has norm at most `C(L epsilon + kappa_F alpha_0 + j_*)` from the energy
    product space to its dual, and the same bound in GW1 3.1's algebra with
    complete carriers. The row part is Y (mb:mean-comb-moments) and
    (mb:nonlinear-row-bounds). The current part is PX154 for each scheme.
    No depth factor enters, by finding 6. A Neumann series about the
    comb saddle inverse gives the mean saddle inverse, lift and multiplier
    with the same bounds up to a factor two. Constraints transfer by (2)
    and (13). Kernels transfer by (13). At a critical field the multiplier
    is the physical one (finding 16).

    Inputs this route still needs, each to be checked, not assumed:
    (a) the comb saddle inverse in GW1's algebra, including the multiplier
    blocks; Y 23849–23915 assembles it from `G_1^J`, `H_1^J`, `q_{1,J}`.
    (b) bounds for `E` and `E'` at complex references on GW1's whole
    domain; Y 16848–16852 warns this differs from complex increments at a
    real reference. (c) a comparison of the gauge projections `R_m` and
    `R_c` from `E'`. (d) the outward-row datum coordinates `Xi` and the
    endpoint node factor (Y 16823–16846) on both sides.
    None of (a)–(d) is shown false by Routes 1–3.

22. **Route 5, also not attempted: no comparison at all.** b98p5 2.5 gives
    the row estimates for the mean with the comb constants. Y 4007–4024
    says Balaban's averaging lemmas use only six contour axioms that both
    schemes meet, and that at `U=1` the two straightened linear parts agree
    after the translation `e_j`. If PI/GW/GW1 use only these row estimates
    and the flat limit, they run natively on mean rows. Then A4.1 is not
    needed by those consumers. Check: whether `out-pi.md` Lemma 4.4 and
    line 666 ("read the straight average directly on corner blocks") use
    comb geometry beyond the translation.

23. **Note 18 and 28. UNCLEAR, minor.** The task did not request
    `prior/a41-avg.md`. The `/tmp` source copies cited are absent now.

## Repairs required for ADVANCE

R1. Add Route 4 (finding 21), written out, and run it to closure or to
    the first of inputs (a)–(d) that fails three distinct ways.
R2. Check Route 5 (finding 22) against `out-pi.md` §4.
R3. If SC-HESS is kept, define `E_c^J` and the gauge part of `T_f`
    (finding 19), and say it is a sufficient form stronger than A4.1
    (finding 20).
R4. Recast the stops of Routes 1 and 2 (findings 13, 16): they show
    non-cancellation and non-transfer of criticality, not a failed bound.
R5. Minor: state `K_1 L epsilon <= 1/2` at line 100; cite pi-admit (17).
