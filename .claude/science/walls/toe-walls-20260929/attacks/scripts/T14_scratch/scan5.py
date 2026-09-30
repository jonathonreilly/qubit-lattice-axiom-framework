import numpy as np, json, time
from yukawa_chunked import run_chunked as run
print("== P5: attraction rate at hypercubic eps=1: detune scalar tree speed to 1+eta (lam=1/(1+eta)^2), c_psi=1 ==")
rows=[]
def kappa(m,mu,N,eta=0.01):
    rp=run(N,N,1.0,m,mu,1.0,1/(1+eta)**2)
    rm=run(N,N,1.0,m,mu,1.0,1/(1-eta)**2)
    dpsi=(rp['a_psi']-rm['a_psi'])/(2*eta)      # d a_psi / d eta   (psi log-speed shift per g^2)
    dphi=(rp['a_phi']-rm['a_phi'])/(2*eta)      # d a_phi / d eta
    return dpsi,dphi,rp,rm
for m in (1.0,0.7,0.5,0.35,0.25,0.18):
    mu=m
    for N in ((32,48) if m>=0.35 else (48,64)):
        t0=time.time(); dpsi,dphi,rp,rm=kappa(m,mu,N)
        kap_psi=dpsi; kap_phi=-dphi   # attractive if both >0
        print(f"m=mu={m:4.2f} N={N}  kappa_psi={kap_psi: .5f} kappa_phi(16sp)={kap_phi: .5f}  kappa_phi(4fl)={kap_phi/4: .5f}  total(4fl)={kap_psi+kap_phi/4: .5f}  a_psi(eta=+)={rp['a_psi']:.5f} ({time.time()-t0:.0f}s)",flush=True)
        rows.append(dict(m=m,mu=mu,N=N,kap_psi=float(kap_psi),kap_phi16=float(kap_phi),total4=float(kap_psi+kap_phi/4)))
json.dump(rows,open('scan5.json','w'),indent=1)
