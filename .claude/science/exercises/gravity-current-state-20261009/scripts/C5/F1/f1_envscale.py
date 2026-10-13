"""F1 (c)/(d): convert the SF Hessians to F2's universal coefficient mu_rho = |m_g^2|/rho (eV^2 m^3/kg) and read them against F2's table
(F2_report.md sec. 2; worker, unrefereed).  F2's placeholder: mu_rho = 1.012e-21 for R19-34's c_h = -0.040475 (f2_common.out:1);
mu_rho is linear in |c_h| (same mapping), c_h = 4 Hess_t.  Sign: c_h > 0 with <psibar psi> > 0 (R19-34's convention) = MASSIVE (branch M)."""
import numpy as np
base_mu, base_c = 1.012e-21, 0.040475
rows = {'SF B1 R18-9 root': 2.42401e-2, 'SF B2 (flow at m=0)': 2.4261092e-2, 'SF B1 0+ root': 2.4534992e-2,
        'K1 control (both on photon flow)': -2.2676313e-3, 'H-cov R19-34 (control)': -0.040475/4}
bounds = [('Earth crossing GW170817 (row 1, checked, both signs)', 1.5e-29), ('detector on ground (row 2, ~1e-29)', 1e-29),
          ('binary pulsar (row 8, suggested, M)', 2.0e-43), ('PTA Local Bubble (row 7, suggested, M)', 8e-24),
          ('Galaxy+IGM LVK column (row 5, checked arith.)', 2.7e-19)]
for lab, Ht in rows.items():
    c = 4*Ht; mu = base_mu*abs(c)/base_c
    sign = 'M (massive)' if c > 0 else 'T (tachyonic)'
    print('%-34s Hess_t %+.4e  c_h %+.4e  mu_rho %.3e  computed-sign branch %s  |m_g|(5500 kg/m^3) = %.2e eV'
          % (lab, Ht, c, mu, sign, np.sqrt(mu*5500)))
    for bl, b in bounds:
        print('      %-48s bound %.1e : ratio %.2e %s' % (bl, b, mu/b, 'EXCEEDS' if mu > b else 'passes'))
    print('      hot era: branch M -> no observational bound (F2 row 10); branch T: N ~ 2.0e9*sqrt(|c|/0.040475) = %.1e e-folds vs N_max 66-95 (F2 row 9)'
          % (2.0e9*np.sqrt(abs(c)/base_c)))
