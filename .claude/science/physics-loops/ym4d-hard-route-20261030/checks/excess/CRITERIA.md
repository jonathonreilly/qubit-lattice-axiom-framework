# Registered criteria, item `excess`, written before any run

Statement frozen at d9d4496f1. SU(2), d = 4 unless stated, comb map of `checks/gate_ex/ex_core.py`. These runs test steps of a proof; a pass does not prove a bound.

Notation. chi_y^{mu nu}(z) := L^-6 tau(z_mu - y_mu) tau(z_nu - y_nu) 1[z_rho, z_sigma in block], tau the discrete tent. m_y := chi-average of fine plaquette angles in a gauge at y. Var_y its variance. r_y := theta'_y - L^2 m_y. n_y := fine energy on the region read by the coarse plaquette at y.

- **T0 (kernels).** sum_z chi_y = 1 and sum_y chi_y(z) = L^-4 to 1e-12. Overlap mass of tents = (1 - L^-2)/4 exactly.
- **T1 (abelian identity).** Abelian field, any closed F, angles below pi/2: E_0 - E_1 = sum L^4 Var, relative error below 1e-10.
- **T2 (remainder is second order).** Non-abelian random field, amplitude t: max |r_y| / max n_y bounded as t -> 0, ratio at t and t/2 within a factor 1.5, and max |r_y| / t^2 stable. FAIL if max |r_y| scales as t^1 (a missed linear term).
- **T3 (Bianchi).** On any field of flux f: sum_cube |B|^2 <= C f^2 E with C stable as t -> 0. And I^grad <= 3 P + C f E with C below 50 on: random smooth, wave, const-plus-wave, charged constant flux plus wave. FAIL if I^grad / P exceeds 3 by more than the f E allowance, on any field.
- **T4 (sharpness).** Abelian plane wave p = (1,1,1,0), a = e_4, small momentum: T / P -> 2.
- **T5 (excess against gradient, any field in the fibre).** For random fine U: E_0 - E_1 >= c I^grad(MU) - C f E with c = (1 - L^-2)/96 and C free of the field, at L = 3. FAIL on a violation with C above 100.
- **T6 (charged field at small flux, minimiser).** Constant abelian flux of non-zero second Chern number on a torus of N' >= 8 parents, plus a smooth non-abelian perturbation, flux at most 0.15. True fibre minimiser. e >= c_1 I^grad - C f E with the same c_1. Record the charge from the plaquette sum at both levels: PASS needs the charge to agree with the integer to 2 percent.
