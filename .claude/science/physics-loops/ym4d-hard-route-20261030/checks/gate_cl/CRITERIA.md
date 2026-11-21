# gate_cl: registered criteria (written before any run), pin bad958abb

Target: `library/one-step-closure.md` Sections 4, 10; `library/sector-values.md` Prop DS, (SRC), (LIFT-I), (COMP).

What a run can show: a power of L, or growth with level, against a claimed bound is a counterexample in trend. A pass proves no bound.

## K1: the kernel of Section 4 at U = 1 (abelian, d = 4)
K(y, x') := level-k bond angle of the minimal lift of a unit parent bond x', fine = level k (one level) and, for L = 3, fine two levels
below (composite). Landau gauge, H-hat(q) = s(q) o lambda-hat(p) / |q-hat|^2, lambda coarse-transverse. Gauge in the note is weighted Landau;
here Landau, with x' restricted to Chebyshev distance <= R parent cells of y (the note cuts its omega at R_* ~ log L, so R is held fixed).
 S_row := sup_y sum_{x'} |K(y, x')|,  S_col := sup_{x'} sum_y |K(y, x')|.
Note's claim: S_row <= C_1 (log L)^{1/2} / L, S_col <= C_1 L^3. Closure reads kappa_n := S_col S_row^(n-1) <= 1/8 at n = 5, 6 for L >= L_0.
Validity: V1 curl of Q_path H equals curl of the unit bond to 1e-6 relative. V2 dense constrained minimiser on N' = 2, L = 3 agrees with
the Fourier lift in plaquette angles to 1e-6.
PASS: local power of L S_row and of S_col / L^3 between the two largest L is <= 0.25 (room for logs).
FAIL: above that: the top coefficient has a power of L the note does not carry.
Limits fixed in advance: U = 1 only. Says nothing at a background. Landau, not weighted Landau: a log of size is not resolved.

## K2: (COMP)(ii) in SU(2), two levels, reanalysis of `checks/gate_ex/y_2_3_*.json` (logged before this gate)
R_m := a_m / (s_m^2 (a_top + f_top E_top)), s_m = 3^-m, a_m := I_grad at level k - m, from those logs. I_top := a_top + f_top E_top bounds the
cubic energy from above, so R_m is low by at most the share of that term.
PASS: R_m <= 25 for all runs at f_top <= 0.11 (abelian sup is C(4, 3, n) = 16.96, 16.01, 16.00, cap 1.5 times that).
FAIL: above. Limits: k = 2, N' = 2, L = 3, fields not chosen for this test, two data points in m.

## K1 follow-up (added after the first K1 run, not registered in advance)
First run: at R = 1 the two largest L are L = 9 (N' = 6) and L = 11 (N' = 4), local power 0.27, above the registered 0.25: a registered FAIL on unequal tori.
Follow-up: N' = 4 at L = 5, 7, 9, 11, 13, one torus, R = 1, 2. The same cap 0.25, read on the two largest L. Reported in full either way.
