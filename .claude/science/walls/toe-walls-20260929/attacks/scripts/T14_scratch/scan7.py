import numpy as np, json
from yukawa_chunked import run_chunked as run
rows=[]
print("slope d gap/d eps at eps=1 (per g^2, tree speeds 1, 16 naive species), central diff h=0.01; also fermion-only and scalar-only slopes")
for (m,mu) in [(1.0,1.0),(0.7,0.7),(0.5,0.5),(0.35,0.35),(0.25,0.25),(1.0,0.3),(0.3,1.0),(0.5,0.2),(0.2,0.5)]:
    N=48 if min(m,mu)>=0.35 else 64
    h=0.01
    rp=run(N,N,1+h,m,mu); rm=run(N,N,1-h,m,mu)
    sg=(rp['gap']-rm['gap'])/(2*h); sp=(rp['a_psi']-rm['a_psi'])/(2*h); sf=(rp['a_phi']-rm['a_phi'])/(2*h)
    print(f"m={m:4.2f} mu={mu:4.2f} N={N}: slope gap={sg: .5f}   psi part={sp: .5f}   phi part={sf: .5f}   |slope| x g^2(1/137)={abs(sg)*0.0917:.2e}")
    rows.append(dict(m=m,mu=mu,N=N,slope=float(sg),slope_psi=float(sp),slope_phi=float(sf)))
json.dump(rows,open('scan7.json','w'),indent=1)
