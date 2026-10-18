"""M3: level-time relaxation under the landed kernel at beta=0.5561. Integrated autocorrelation time of |M_level|^2 (Sokal window c=6),
and the exponential time from the decay of the autocorrelation function; z from log-log slopes between sizes."""
import numpy as np, glob, re
def acf(x):
    x=x-x.mean(); n=len(x); f=np.fft.rfft(x,2*n); a=np.fft.irfft(f*np.conj(f))[:n]; return a/a[0]
res=[]
for f in sorted(glob.glob('data/m3_L*.bin'),key=lambda s:int(re.findall(r'L(\d+)',s)[0])):
    L=int(re.findall(r'L(\d+)',f)[0]); log=open(f[:-4]+'.log').read()
    if 'watchdog' not in log: continue
    w=np.fromfile(f).reshape(-1,2); x=w[:,0]
    a=acf(x); tau=0.5
    for t in range(1,len(a)):
        tau+=a[t]
        if t>=6*tau: break
    # exponential time: fit log a(t) on window where a in (0.05, 0.5)
    idx=np.where((a>0.05)&(a<0.5))[0]; idx=idx[idx<idx.min()+int(3*tau)+5] if len(idx) else idx
    texp=-1/np.polyfit(idx,np.log(a[idx]),1)[0] if len(idx)>3 else np.nan
    n=len(x); err=tau*np.sqrt(2*(2*t+1)/n)
    res.append((L,tau,err,texp)); print(f'L={L:2d} ticks={n} tau_int(|M|^2)={tau:.1f}({err:.1f}) ticks  tau_exp~{texp:.1f}')
res=np.array(res)
for i in range(len(res)-1):
    L1,t1,e1,x1=res[i]; L2,t2,e2,x2=res[i+1]
    print(f'z_eff({int(L1)},{int(L2)}): int {np.log(t2/t1)/np.log(L2/L1):.2f}  exp {np.log(x2/x1)/np.log(L2/L1):.2f}')
