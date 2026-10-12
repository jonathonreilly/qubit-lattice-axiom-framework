import numpy as np, time
from d2_common import *
N=1024
k=TWO_PI*np.arange(N//2+1)/N
for kind in ['SLAC','KG','TB']:
    E=eps_band(kind,k)
    r=face_measures(k,E)
    print(kind,[ (round(d,4), round(s,4), round(p,3)) for d,_,s,p in r[:5]])
    for w in [np.pi/4,np.pi/2,np.pi]:
        print('  fit',w, slac_fit(k,E,w))
t=time.time()
r=dressed_band_1d('TB',1024,1.5,0.2,0.5,sc=True)
print('time',time.time()-t,r['it'],r['res'], r['Z'][[0,-1]], r['gap'][[0,-1]])
print([ (round(d,4), round(s,5), round(p,3)) for d,_,s,p in face_measures(r['k'],r['E'])])
