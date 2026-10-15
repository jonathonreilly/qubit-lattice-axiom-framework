"""CLS-1 step 5: arithmetic of (iii) against bounds over the f range, from the proxy coefficients.
Coefficient sizes: eps*a = g' f a. Range: f a in [0.026, 1] (g f a = 0.33, g <= 4 pi). Central g' = g -> eps*a = 0.33 for all f.
Bracket: g' in [0.1, 1] (independent of g) -> eps*a = g' f a.
Proxy facts used (cls1_light.out): a-type split = 3 eps (A1 at +2eps, E at -eps); c-type spread = 2 eta (P-c) and ~kappa^2 (P-d);
model-A light gap = Delta * sigma_light (= Delta*kappa for E)."""
import numpy as np
def P(*a): print(*a)
MPL = 1.22e19; GUT = 2e16
A3_ICECUBE = 2.9e-24      # GeV, |Re,Im a(3)_mutau| 99% CL, IceCube Nat. Phys. 14 (2018) 961, arXiv:1709.03434 Table 1 (fetched via ar5iv)
C4_ICECUBE = 3.9e-28      # dimensionless, |Re,Im c(4)_mutau| 99% CL, same table (fetched)
C4_QUARK = 1e-22          # OBS-3 as-printed D44 d row (u row 3e-23)
NU_MASS = 1e-9            # GeV, generous upper scale for any G_SM-symmetric light mass (neutrino mass scale ~ eV; recalled)
fa = np.array([0.026, 0.05, 0.1, 0.33, 1.0])
for lab, invA in [("1/a = M_Pl", MPL), ("1/a = 2e16 GeV", GUT)]:
    P(f"--- {lab} ---")
    for gp_lab, eps in [("g'=g (eps a = 0.33)", np.full_like(fa, 0.33)), ("g'=1", fa), ("g'=0.1", 0.1 * fa)]:
        a_split = 3 * eps * invA
        c_spread = 2 * eps
        k2 = eps ** 2
        gapA = eps * invA
        P(f"  {gp_lab:22s} f a = {fa}")
        P(f"     a-type split 3eps/a [GeV]       {a_split}   / IceCube a(3) = {a_split / A3_ICECUBE}")
        P(f"     c-type spread 2eta              {c_spread}   / IceCube c(4) = {c_spread / C4_ICECUBE}   / quark row = {c_spread / C4_QUARK}")
        P(f"     c-type spread kappa^2 (P-d)     {k2}   / IceCube c(4) = {k2 / C4_ICECUBE}")
        P(f"     model-A light gap Delta*kappa/a {gapA} GeV / 1e-9 GeV = {gapA / NU_MASS}")
    P(f"  tuning to pass (coefficient needed / central 0.33):")
    P(f"     a-type eps a <= {A3_ICECUBE / 3 / invA:.2e}  -> tuning {A3_ICECUBE / 3 / invA / 0.33:.1e}")
    P(f"     c-type eta   <= {C4_ICECUBE / 2:.2e}  -> tuning {C4_ICECUBE / 2 / 0.33:.1e}  (quark rows only: {C4_QUARK / 2 / 0.33:.1e})")
    P(f"     c-type kappa <= {np.sqrt(C4_ICECUBE):.2e} -> tuning {np.sqrt(C4_ICECUBE) / 0.33:.1e}  (or cancel by the dim-4 counterterms)")
    P(f"     model-A: kappa <= {NU_MASS / invA:.1e} -> tuning {NU_MASS / invA / 0.33:.1e}")
# proton-decay contact estimate (suggested): C = W (2 kappa)^4 a^2 vs ~6e-32 GeV^-2 (Lambda ~ 4e15 GeV for tau(p->e+pi0) > 2.4e34 yr; recalled)
for lab, invA in [("M_Pl", MPL), ("2e16", GUT)]:
    C = (2 * 0.33) ** 4 / invA ** 2
    P(f"proton-decay contact (W=1, kappa=0.33, 1/a={lab}): C = {C:.2e} GeV^-2 vs ~6e-32 -> margin {6e-32 / C:.1e}")
