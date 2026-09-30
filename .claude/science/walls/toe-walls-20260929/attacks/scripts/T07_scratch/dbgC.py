import numpy as np
exec(open('testC_scaling.py').read().split("P0 = wave(0.0)")[0])
P0 = (np.abs(wave(0.0))**2).sum(1)
m=4; q=2*np.pi*m/L
rho0 = P0*(1+0.5*np.cos(q*x)); rho0/=rho0.sum()
ts,R = evolve(rho0, 30.0, nt=7)
for i,t in enumerate(ts):
    P=(np.abs(wave(t))**2).sum(1)
    f=np.where(P>1e-12, R[i]/np.maximum(P,1e-300), np.nan)
    print('t',t,'D',kl(R[i],P))
    if i in (0,3,6):
        sel=[j for j in range(L) if P[j]>1e-3*P.max()]
        print('  sites',sel[0],sel[-1])
        print('  f at sites step 4:', np.round([f[j] for j in sel[::4]],3))
        print('  P mass right half:', P[80:].sum(), ' rho mass right half', R[i][80:].sum())
