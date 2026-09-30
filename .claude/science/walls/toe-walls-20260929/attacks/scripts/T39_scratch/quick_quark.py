import numpy as np
def dial(m):
    s=np.sqrt(np.array(sorted(m)))
    a=s.sum()/3
    Q=sum(np.array(m))/s.sum()**2
    r=(3*Q-1)/2
    x=(s/a-1)/(2*np.sqrt(r))
    d=np.arccos(np.clip(x.max(),-1,1))   # heaviest ~ cos(delta)
    return Q,r,d
# masses at mu = M_Z (MS-bar, Xing-Zhang-Zhou-like), GeV
sets={
 'MZ up':[1.24e-3,0.624,171.7],
 'MZ down':[2.69e-3,0.0535,2.86],
 'PDG mixed up (2GeV u,c(mc),t pole)':[2.16e-3,1.27,172.5],
 'PDG mixed down':[4.67e-3,0.093,4.18],
 'lepton':[0.5109989461e-3,0.1056583745,1.77686],
}
for k,m in sets.items():
    print(k, dial(m))
