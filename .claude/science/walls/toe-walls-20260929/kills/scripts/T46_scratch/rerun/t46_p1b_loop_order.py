"""T46 P1b: transport factor m_s(2 GeV)/m_s(m_b) by loop order; explains 18.6% (here) vs 14-15% (lane)."""
import numpy as np
from qcdrun import QCD
V=0.103303816122/np.sqrt(6); Rp=V**1.2
for L in (1,2,3,4):
    q=QCD(loops=L)
    T=0.0934/q.mass(0.0934,2.0,4.18)
    Rc=q.mass(0.0934,2.0,4.18)/4.18
    print(f"loops={L}: alpha_s(2)={q.alpha_s(2.0):.4f} alpha_s(mb)={q.alpha_s(4.18):.4f}  T={T:.4f}  R_common={Rc:.6f}  R_pred/R_common-1={100*(Rp/Rc-1):+.1f}%")
# one-loop formula with the lane's alpha_s values
print("lane July inputs (0.2965,0.2265): T =", (0.2965/0.2265)**(12/25))
print("PDG-style literal 93.4/81.0 =", 93.4/81.0, " (lane's 81.0 is not reproduced by 2-4 loop running from 93.4)")
