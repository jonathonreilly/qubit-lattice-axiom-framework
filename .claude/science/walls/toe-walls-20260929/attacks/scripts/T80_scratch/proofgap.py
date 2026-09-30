# MC-C: for the MC-observed (beta, rho) at c = c0 (sphere, L=12, ordered), what c would block 126's sufficient criterion need?
import math
G3=0.7581  # 3G(0)
rows=[]
for line in open('results_A1.csv'):
    f=line.split()
    if len(f)<14 or f[0]!='s' or int(f[1])!=12: continue
    beta,z,g,c,rho,U=float(f[2]),float(f[3]),float(f[4]),float(f[5]),float(f[6]),float(f[11])
    if abs(g-1)<1e-9 and U>0.6: rows.append((z,beta,rho))
print("sphere, neutral scale, ordered by MC (L=12).  proof needs (beta - gamma(c)) rho > 3G(0)=%.4f"%G3)
print(" z    beta   rho    proof reaches?   c*/c0   ln(c*/c0)=glue the proof needs")
for z,beta,rho in sorted(rows):
    gm=beta-G3/rho
    if gm<=0: print(f"{z:4g} {beta:5.2f} {rho:6.3f}   no (beta*rho={beta*rho:.3f} <= 3G(0))"); continue
    cs=gm/math.sinh(gm); c0=beta/math.sinh(beta)
    print(f"{z:4g} {beta:5.2f} {rho:6.3f}   only for c>=c*     {cs/c0:6.3f}   {math.log(cs/c0):6.3f}")
