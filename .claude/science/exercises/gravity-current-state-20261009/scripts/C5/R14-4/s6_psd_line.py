# R14-4 s6: the near-axis PSD line of s5 (TT1=TT2=1, VEC=S=0, c2=c3/2-1/4).  Scan c3; for each member report
# global PSD over 3005 directions, the worst-direction third soft stiffness lambda_3, and the max rank.
import numpy as np
from s4_families_and_margin import stats
rows=[]
for c3 in np.linspace(-4,5,37):
    c2=c3/2-0.25; c=np.array([1,c2,c3,-2-c2,0.5-c3,0.0]); mn,l3,rk=stats(c); rows.append((c3,mn,l3,rk))
    print("c3=%6.3f c2=%6.3f  min eig=%+.3e  max_dir lambda_3=%.4f  max rank=%d"%(c3,c2,mn,l3,rk))
psd=[r for r in rows if r[1]>-1e-9]
if psd: print("PSD members on the line: c3 in [%.3f, %.3f]; min over them of max_dir lambda_3 = %.4f"%(min(r[0] for r in psd),max(r[0] for r in psd),min(r[2] for r in psd)))
