import re, numpy as np
rows={}
for line in open('ladder_xx_probe0_signed.out'):
    m=re.search(r'N=\s*(\d+) qT=([+-][\d.]+) sTE=([+-][\d.]+) rhoE=([+-][\d.]+) qE=([+-][\d.]+)',line)
    if m: rows[int(m.group(1))]=tuple(float(m.group(i)) for i in range(2,6))
# frob has N=121
for line in open('ladder_frob_probe0.out'):
    m=re.search(r'N=\s*(\d+) qT=([+-][\d.]+) sTE=([+-][\d.]+) rhoE=([+-][\d.]+) qE=([+-][\d.]+)',line)
    if m and int(m.group(1))==121:
        v=tuple(float(m.group(i)) for i in range(2,6)); rows[121]=(-v[0],v[1],-v[2]+ (0), -v[3])  # sign convention: frob has |.|; use smooth-equivalent sign
Ns=[n for n in sorted(rows) if n>=61]
print("N used", Ns)
names=['q_T','s_TE','rho_E','q_E']
# rho_E and qE for N=121 from frob: reconstruct smooth values = |orig| relation: rho=6(qE-1), qE positive
rows[121]=(0.98187,0.97043,6*(1.08575-1),1.08575)
for i,n in enumerate(names):
    y=np.array([rows[N][i] for N in Ns]); x=1.0/np.array(Ns,float)
    A=np.vstack([np.ones_like(x),x]).T
    c1=np.linalg.lstsq(A,y,rcond=None)[0]
    A2=np.vstack([np.ones_like(x),x,x**2]).T
    c2=np.linalg.lstsq(A2,y,rcond=None)[0]
    print(f"{n:6s} N=61..121: 1/N fit -> {c1[0]:+.4f}   1/N+1/N^2 fit -> {c2[0]:+.4f}   last value {y[-1]:+.4f}")
for tgt,name,val in [(5/6,'q_T',None),(-2,'s_TE',None),(21/4,'rho_E',None)]:
    pass
print("targets: q_T=5/6=0.8333, s_TE=-2, rho_E=21/4=5.25 (q_E=15/8=1.875); b_T/a_T=6(q_T-1) target -1")
