import pickle,numpy as np
rows=pickle.load(open('scan600.pkl','rb'))
EC=2*np.sqrt(3)
A=np.array([[r[0],r[1]-EC,r[2],r[3],r[4],r[5],r[6],r[7]] for r in rows])
for gcut in (0.3,):
    S=A[A[:,7]>gcut]
    bins=[0.02,0.04,0.06,0.08,0.12,0.2,0.3,0.5,1,2,5,10,20,80]
    for lo,hi in zip(bins[:-1],bins[1:]):
        s=S[(S[:,1]>=lo)&(S[:,1]<hi)]
        if len(s): print(f'delta in [{lo},{hi}) n={len(s)} max Wsum={s[:,4].max():.3f}  min={s[:,5].min():.3f}  g at max={s[np.argmax(s[:,4]),2]:.3f}')
