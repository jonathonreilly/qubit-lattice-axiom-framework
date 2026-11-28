# GUIDE: finite subgroups of SU(2) (Q_8, 2T), one sheet, two slice sites: class-function model of Lemma KIN.
import numpy as np, itertools
def qmul(p,q):
    a,b,c,d=p; e,f,g,h=q
    return np.array([a*e-b*f-c*g-d*h, a*f+b*e+c*h-d*g, a*g-b*h+c*e+d*f, a*h+b*g-c*f+d*e])
def group(name):
    els=[]
    for s in (1,-1):
        for k in range(4):
            v=np.zeros(4); v[k]=s; els.append(v)
    if name=="2T":
        for sg in itertools.product((0.5,-0.5),repeat=4): els.append(np.array(sg))
    return np.array(els)
def model(name):
    G=group(name); n=len(G)
    def find(v): return int(np.argmin(((G-v)**2).sum(1)))
    mul=np.array([[find(qmul(G[i],G[j])) for j in range(n)] for i in range(n)])
    inv=np.array([find(G[i]*np.array([1,-1,-1,-1])) for i in range(n)])
    x=G[:,0].copy()
    # conjugacy classes
    cls=-np.ones(n,int); nc=0
    for i in range(n):
        if cls[i]<0:
            for g in range(n): cls[mul[mul[g,i],inv[g]]]=nc
            nc+=1
    B=np.zeros((n,nc))
    for i in range(n): B[i,cls[i]]=1
    B/=np.sqrt(B.sum(0))                       # orthonormal class indicators (counting measure)
    def conv(b):
        if np.isinf(b): return np.eye(n)
        w=np.exp(b*(x-1)); w/=w.sum()
        return np.array([[w[mul[j,inv[i]]] for j in range(n)] for i in range(n)])
    def gap(bM,bL):
        CM=B.T@conv(bM)@B; CL=B.T@conv(bL)@B
        K=CM@CM@CL@CL; K=(K+K.T)/2
        E=np.diag(np.exp(0.5*bM*(B.T@(x[:,None]*B)).diagonal()-0.5*bM))
        T=E@K@E; ev=np.sort(np.linalg.eigvalsh((T+T.T)/2))[::-1]
        return np.log(ev[0]/ev[1])
    return gap,n,nc
for name in ("Q8","2T"):
    gap,n,nc=model(name)
    print(name,"order",n,"classes",nc)
    grid=np.exp(np.linspace(np.log(0.2),np.log(60),400))
    for bM in (1.0,2.0,2.4,3.0,4.0,6.0,8.0):
        f=gap(bM,np.inf); g=np.array([gap(bM,b) for b in grid]); k=(g-f).argmin()
        print("  bM=%.1f face=%.5f  min(gap-face)=%.4e at bL=%.2f"%(bM,f,(g-f)[k],grid[k]))
