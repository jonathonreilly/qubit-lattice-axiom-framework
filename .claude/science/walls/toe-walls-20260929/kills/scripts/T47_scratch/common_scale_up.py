"""T47 C5: up-sector comparators at a common scale (reuse of T46's own QCD runner, read-only import). Lane comparator: m_u(2GeV)/m_c(m_c) and m_c(m_c)/m_t(pole)."""
import sys
sys.dont_write_bytecode=True
sys.path.insert(0,'/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/walls/attacks/T46_scratch')
import numpy as np
from qcdrun import QCD
q=QCD()
MU2, MC, MT_POLE, MT_MSBAR = 2.16e-3, 1.273, 172.57, 162.5
print("lane comparators: r_uc = 2.16e-3/1.273 = %.4e ; r_ct = 1.273/172.57 = %.4e"%(MU2/MC, MC/MT_POLE))
print("mu[GeV]   m_u/m_c (common)   m_c/m_t(MSbar mt(mt)=162.5) (common)")
for mu in (1.273, 2.0, 4.18, 91.19, 162.5, 1000.):
    mu_run = q.mass(MU2, 2.0, mu); mc_run = q.mass(MC, 1.273, mu); mt_run = q.mass(MT_MSBAR, 162.5, mu)
    print(f"{mu:8.2f}   {mu_run/mc_run:.4e}        {mc_run/mt_run:.4e}   (m_c={mc_run:.3f})")
print("carrier CKM-only inversion at a_u=RPSR: r_uc=1.679e-3, r_ct=7.365e-3")
