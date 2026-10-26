import pickle,numpy as np
rows=pickle.load(open('scan600.pkl','rb'))
# row: (it,E,g,null,evmax,evmin,first,gap)
A=np.array([[r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7]] for r in rows])
for gcut in (1e-3,1e-2,0.03,0.1,0.3,1.0):
    sel=A[A[:,7]>gcut]
    print('gap>',gcut,'n',len(sel),'max evmax',sel[:,4].max(),'min evmin',sel[:,5].min())
# max evmax as function of gap bins
bins=[0,1e-3,1e-2,0.03,0.1,0.3,1,10]
for lo,hi in zip(bins[:-1],bins[1:]):
    sel=A[(A[:,7]>=lo)&(A[:,7]<hi)]
    if len(sel): print(f'gap in [{lo},{hi}) n={len(sel)} max={sel[:,4].max():.3f} min={sel[:,5].min():.3f}')
