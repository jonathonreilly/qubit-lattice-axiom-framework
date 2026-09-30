import glob
R=[]
for fn in sorted(glob.glob('outF/job_*.txt')):
    L=open(fn).read().strip().split('\n')
    f=L[0].split(); rs=L[1].split()
    R.append(dict(L=int(f[1]),beta=float(f[2]),z=float(f[3]),g=float(f[4]),c=float(f[5]),rho=float(f[6]),U=float(f[11]),rs=float(rs[1]),err=float(rs[2])))
def fam(beta,kind,L=12):
    out=[]
    for r in R:
        if r['L']!=L or abs(r['beta']-beta)>1e-9 or r['U']<0.6: continue
        one = abs(r['c']-1)<1e-4 and abs(r['g']-1)>1e-3
        neu = abs(r['g']-1)<1e-9
        if (kind=='N' and neu) or (kind=='O' and one): out.append((r['rho'],r['rs'],r['err'],r['z']))
    return sorted(out)
def interp(pts,x):
    for a,b in zip(pts,pts[1:]):
        if a[0]<=x<=b[0]: return a[1]+(b[1]-a[1])*(x-a[0])/(b[0]-a[0])
worst=0
for beta in (1.2,1.5):
    N=fam(beta,'N'); O=fam(beta,'O')
    for (rho,rs,err,z) in O:
        rn=interp(N,rho)
        if rn is None: continue
        rel=(rs-rn)/rn; worst=max(worst,abs(rel))
        print(f"beta={beta} rho={rho:.4f} (c=1,z={z}): rho_s(c=1)={rs:.4f}  rho_s(neutral, interpolated)={rn:.4f}  rel diff={rel*100:+.2f}%")
print("max |relative difference| = %.2f%%"%(worst*100))
print("neutral-scale rho_s range:",min(r['rs'] for r in R if abs(r['g']-1)<1e-9 and r['U']>0.6),max(r['rs'] for r in R if abs(r['g']-1)<1e-9 and r['U']>0.6))
