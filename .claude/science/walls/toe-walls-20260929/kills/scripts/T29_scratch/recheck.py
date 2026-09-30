import sys, glob, math, numpy as np
sys.path.insert(0,'../../attacks/T29_scratch')
from ana import load, stat
R='../../attacks/T29_scratch/runs/'
# 1. drift / cut sensitivity of L=12 chains
tot={}
for cut in (0,100,300):
    ms=[];ws=[]
    for f in sorted(glob.glob(R+'hb_L12_*.txt')):
        P,_,_=load(f)
        if len(P)<cut+200: continue
        m,e,t=stat(P[cut:]); ms.append(m); ws.append(1/e**2)
    ms=np.array(ms); ws=np.array(ws)
    print('L12 cut',cut,'mean %.6f +/- %.6f'%((ms*ws).sum()/ws.sum(), 1/math.sqrt(ws.sum())), 'n chains',len(ms))
# 2. first/second half of each chain
for f in sorted(glob.glob(R+'hb_L12_*.txt'))+sorted(glob.glob(R+'hb_L16*.txt')):
    P,_,_=load(f); P=P[100:]; h=len(P)//2
    a=stat(P[:h]); b=stat(P[h:])
    print(f.split('/')[-1],'halves %.6f(%.6f) %.6f(%.6f)'%(a[0],a[1],b[0],b[1]))
# 3. simple fits on subsets
Pv={4:(0.5968678,9.4e-5),6:(0.5948652,3.66e-5),8:(0.5942582,2.32e-5),12:(0.5937200,1.95e-5),16:(0.5937963,7.1e-5)}
def fit(Ls,pw):
    x=np.array([L**-float(pw) for L in Ls]); y=np.array([Pv[L][0] for L in Ls]); s=np.array([Pv[L][1] for L in Ls])
    A=np.vstack([np.ones_like(x),x]).T/s[:,None]; b=y/s
    c,*_=np.linalg.lstsq(A,b,rcond=None); cov=np.linalg.inv(A.T@A); chi=float(((A@c-b)**2).sum())
    return c[0],math.sqrt(cov[0,0]),chi,len(Ls)-2
for Ls in ([8,12,16],[8,12],[12,16]):
    for pw in (4,3,2):
        if len(Ls)==2 and pw!=4: continue
        print('fit L=',Ls,'L^-%d'%pw,'P_inf=%.6f +/- %.6f chi2=%.1f dof=%d'%fit(Ls,pw))
# 4. all direct large-volume points (mine L=12,16 + repo 3) weighted mean
pts=[(0.593720,1.95e-5),(0.593796,7.1e-5),(0.593692,4.45e-5),(0.593671,3.26e-5),(0.593741,6.1e-5)]
w=np.array([1/e**2 for m,e in pts]); m=np.array([m for m,e in pts]); mean=(w*m).sum()/w.sum()
print('all large-volume pts mean %.6f +/- %.6f chi2 %.2f/4'%(mean,1/math.sqrt(w.sum()),(w*(m-mean)**2).sum()))
d=mean-0.5934; print('d=%.2e'%d)
# 5. hierarchy
Mpl=1.220890e19; ab=1/(4*math.pi)
v=lambda P: Mpl*(7/8)**0.25*(ab/P**0.25)**16
for P in (0.5934,0.59371,0.593725): print(P,v(P),100*(v(P)/246.2197-1))
