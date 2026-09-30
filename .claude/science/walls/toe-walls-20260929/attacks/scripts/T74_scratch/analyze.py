import numpy as np, re
# M2 torus data (m=0 and m=1): L -> eta by orientation (from m2_results_L12_16.txt, m2_L20_*.txt, and L=8 run)
d0 = {8:(0.193,0.21248,0.22519), 12:(0.1951,0.21515,0.22806), 16:(0.19578,0.21609,0.22924), 20:(0.1961,0.21652,0.2298)}
d1 = {8:(0.16451,0.18349,0.19613), 12:(0.16469,0.18404,0.18681+0.00000), 16:(0.1647,0.18413,0.19696), 20:(0.1647,0.18415,0.19699)}
d1[12] = (0.16469,0.18404,0.19681)
def extrap(d, col):
    Ls = np.array(sorted(d)); y = np.array([d[L][col] for L in Ls])
    A = np.vstack([np.ones_like(Ls,dtype=float), 1.0/Ls**2]).T
    # fit on L>=12
    sel = Ls>=12
    c,_,_,_ = np.linalg.lstsq(A[sel], y[sel], rcond=None)
    return c[0]
names = ["(100)","(110)","(111)"]
for tag,d in (("m=0",d0),("m=1",d1)):
    e = [extrap(d,i) for i in range(3)]
    print(tag, "L->inf (a+b/L^2, L>=12):", {n:round(x,4) for n,x in zip(names,e)},
          " (110)/(100)=%.3f (111)/(100)=%.3f max/min=%.3f" % (e[1]/e[0], e[2]/e[0], max(e)/min(e)),
          " g_thermo=1/(4 eta):", [round(1/(4*x),3) for x in e])
# mass scan
rows=[]
for line in open("m1_mass_scan.txt"):
    mm = re.match(r"m=([\d.]+) .* eta100=([\d.]+)", line)
    if mm: rows.append((float(mm.group(1)), float(mm.group(2))))
rows = np.array(rows)
m, eta = rows[:,0], rows[:,1]
print("mass scan (100):"); 
for a,b in rows: print("  m=%.2f eta=%.5f" % (a,b))
print("  max eta over m: %.5f at m=0 ; crosses 1/6 near m=%.2f ; never reaches 1/4 (max=%.5f)" % (eta.max(), np.interp(1/6, eta[::-1], m[::-1]), eta.max()))
# universal log-mass term: eta(m)-eta(0) = a m^2 + b m^2 ln m ; continuum prediction b = N_D/(12 pi) * (1/c^2) with N_D=2, c=2 (M=m/2): 2/(12 pi)/4
sel = (m>0)&(m<=0.5)
X = np.vstack([m[sel]**2, m[sel]**2*np.log(m[sel])]).T
y = eta[sel]-eta[m==0][0]
coef,_,_,_ = np.linalg.lstsq(X,y,rcond=None)
print("fit on m<=0.5: a=%.4f b=%.4f ; continuum prediction b = N_D/(12 pi c^2) = %.4f (N_D=2 four-comp Dirac, c=2)" % (coef[0], coef[1], 2/(12*np.pi*4)))
