"""T46 P4: the taste-staircase NNI down texture (c_23=0.9738) puts theta23^d ~ c*sqrt(m_s/m_b); can the up sector cancel it to |V_cb|?"""
import numpy as np
from qcdrun import QCD
q = QCD()
V_ATLAS = 0.103303816122/np.sqrt(6)
for label, Rsb, mu in (("threshold-local (lane) m_s(2)/m_b(m_b)", 0.0934/4.18, None),
                       ("RG-common", q.mass(0.0934,2.0,4.18)/4.18, None)):
    print(label, "R_sb =", round(Rsb,6))
    th_d = 0.9738*np.sqrt(Rsb)
    # up sector: m_c/m_t on its own natural surfaces
    for lab2, Rct in (("m_c(m_t)/m_t(m_t)", q.mass(1.27,1.27,163.0)/163.0),
                      ("m_c(m_c)/m_t(m_t)", 1.27/163.0),
                      ("lane comparator m_c(m_c)/m_t(m_t)~", 1.27/172.5)):
        th_u = 1.0*np.sqrt(Rct)   # c_u = 1
        print(f"   theta23^d = {th_d:.4f} ;  up: {lab2}={Rct:.5f} -> theta23^u(c_u=1) = {th_u:.4f} ;"
              f" min |V_cb| = {th_d-th_u:.4f} (phase 0) ; c_u needed for V_cb=atlas: {(th_d-V_ATLAS)/np.sqrt(Rct):.2f}")
