# MC-D: does s = m2/rho^2 depend on (z,c) only through rho?  Neutral (g=1) vs c=1 families, L=12, sphere.
import math
def load(fn):
    R=[]
    for line in open(fn):
        f=line.split()
        if len(f)<14 or f[0]!='s': continue
        R.append(dict(L=int(f[1]),beta=float(f[2]),z=float(f[3]),g=float(f[4]),c=float(f[5]),rho=float(f[6]),m2=float(f[9]),U=float(f[11]),cold=int(f[13])))
    return R
R=load('results_DE.csv')+load('results_A1.csv')
def fam(beta,kind):
    out=[]
    for r in R:
        if r['L']!=12 or abs(r['beta']-beta)>1e-9 or r['cold']!=0: continue
        is_one = abs(r['c']-1)<1e-4 and abs(r['g']-1)>1e-3
        is_neu = abs(r['g']-1)<1e-9
        if (kind=='N' and is_neu) or (kind=='O' and is_one):
            if r['U']>0.6:   # ordered only
                out.append((r['rho'],r['m2']/r['rho']**2,r['z']))
    return sorted(set(out))
def interp(pts,x):
    for (x0,y0,_),(x1,y1,_) in zip(pts,pts[1:]):
        if x0<=x<=x1: return y0+(y1-y0)*(x-x0)/(x1-x0)
    return None
for beta in (1.2,1.5):
    N=fam(beta,'N'); O=fam(beta,'O')
    print(f"beta={beta}: neutral ordered (rho, s, z):",[(round(a,4),round(b,4),z) for a,b,z in N])
    print(f"          c=1     ordered (rho, s, z):",[(round(a,4),round(b,4),z) for a,b,z in O])
    worst=0
    for (rho,s,z) in O:
        sN=interp(N,rho)
        if sN is not None:
            print(f"   at rho={rho:.4f} (c=1, z={z}): s_O={s:.4f}  s_N(interp)={sN:.4f}  diff={s-sN:+.4f}")
            worst=max(worst,abs(s-sN))
    print("   max |s_O - s_N| over matched points:",round(worst,4))
    # pre-registered points rho=0.90, 0.95
    for rho in (0.90,0.95):
        a=interp(N,rho); b=interp(O,rho)
        print(f"   pre-registered rho={rho}: s_N={a}, s_O={b}", "(c=1 family has no ordered state there)" if b is None else f"diff={b-a:+.4f}")
