# Compare density-fluctuation (var N / V, column 8) at matched density, neutral vs c=1, from attacker's own raw outF rows.
import glob, math
R=[]
for fn in sorted(glob.glob('../../attacks/T80_scratch/outF/job_*.txt')):
    f=open(fn).read().split('\n')[0].split()
    R.append(dict(beta=float(f[2]),z=float(f[3]),g=float(f[4]),c=float(f[5]),rho=float(f[6]),var=float(f[7]),U=float(f[11])))
for b in (1.2,1.5):
    N=sorted([(r['rho'],r['var']) for r in R if abs(r['beta']-b)<1e-9 and abs(r['g']-1)<1e-9 and r['U']>0.6])
    # average duplicates
    d={}
    for r,v in N: d.setdefault(round(r,3),[]).append((r,v))
    N=sorted((sum(a for a,_ in v)/len(v),sum(x for _,x in v)/len(v)) for v in d.values())
    O=[(r['rho'],r['var'],r['z']) for r in R if abs(r['beta']-b)<1e-9 and abs(r['c']-1)<1e-4 and abs(r['g']-1)>1e-3 and r['U']>0.6]
    for rho,v,z in sorted(O):
        for (a,va),(bb,vb) in zip(N,N[1:]):
            if a<=rho<=bb:
                # interpolate log(var/(rho(1-rho))) linearly in rho -- ideal-gas-normalised
                fa=math.log(va/(a*(1-a))); fb=math.log(vb/(bb*(1-bb)))
                fr=fa+(fb-fa)*(rho-a)/(bb-a)
                vn=math.exp(fr)*rho*(1-rho)
                # also plain linear in log var
                la=math.log(va); lb=math.log(vb); vn2=math.exp(la+(lb-la)*(rho-a)/(bb-a))
                print(f"beta={b} rho={rho:.4f} z={z}: var(c=1)={v:.5f} neutral interp(ideal-normalised)={vn:.5f} ({(v/vn-1)*100:+.1f}%)  interp(log var)={vn2:.5f} ({(v/vn2-1)*100:+.1f}%)")
