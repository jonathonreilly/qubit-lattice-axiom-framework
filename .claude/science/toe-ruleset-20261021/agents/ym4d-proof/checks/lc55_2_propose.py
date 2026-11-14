# lc55_2 PROPOSAL generator (floats/numpy). NOT a verdict: it only proposes directions, rounded to rationals and written to
# lc55_2_proposals.txt; every verdict is computed exactly by lc55_2_certify.py (plain python fractions).
import numpy as np, math
s=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.array([[1,0],[0,-1]],complex)]
I2=np.eye(2,dtype=complex)
def G(a): return np.cos(a)*I2+1j*np.sin(a)*s[2]
def Ad(Um,X):
    M=sum(X[i]*s[i] for i in range(3)); N=Um@M@np.linalg.inv(Um)
    return np.array([0.5*np.trace(N@s[i]).real for i in range(3)])
def pattern(P,beta):
    h=(P-1)//2; a=[0.0]*P; a[h-1]=beta; a[h+1]=-beta; return a
def plaq_hess_add(H,mats,var):
    def F(k,der):
        (key,inv,B)=mats[k]
        if der is None: return np.linalg.inv(B) if inv else B
        if der[0]=='d1':
            i=der[1]; return (-1j*s[i])@np.linalg.inv(B) if inv else B@(1j*s[i])
        i,j=der[1],der[2]; M=-(s[i]@s[j]+s[j]@s[i])/2
        return M@np.linalg.inv(B) if inv else B@M
    for ka in range(4):
        va=var(mats[ka][0])
        if va is None: continue
        for kb in range(4):
            vb=var(mats[kb][0])
            if vb is None: continue
            for i in range(3):
                for j in range(3):
                    prod=I2
                    for k in range(4):
                        if ka==kb==k: d=('d2',i,j)
                        elif k==ka: d=('d1',i)
                        elif k==kb: d=('d1',j)
                        else: d=None
                        prod=prod@F(k,d)
                    H[3*va+i,3*vb+j]+=-0.5*np.trace(prod).real
def cyl(n,P,beta):
    a=pattern(P,beta); A=lambda x: a[x%P]
    D=3*(2*n-1); H=np.zeros((D,D))
    def var(key):
        kind,x=key
        if kind==1: return x
        return n+x-1 if 1<=x<=n-1 else None
    for x in range(n):
        mats=[((1,x),False,I2),((2,x+1),False,G(A(x+1))),((1,x),True,I2),((2,x),True,G(A(x)))]
        plaq_hess_add(H,mats,var)
    B=np.zeros((D,3*n))
    for p in range(3*n):
        e=np.zeros(3*n); e[p]=1
        w1=np.zeros((n,3)); w2=np.zeros((n+1,3)); w1[0]=e[0:3]
        for x in range(1,n): w2[x]=e[3*x:3*x+3]
        for x in range(1,n): w1[x]=w1[x-1]-(Ad(G(A(x)),w2[x])-w2[x])
        v=np.zeros(D)
        for x in range(n): v[3*x:3*x+3]=w1[x]
        for x in range(1,n): v[3*(n+x-1):3*(n+x-1)+3]=w2[x]
        B[:,p]=v
    Q,_=np.linalg.qr(B); ev,U=np.linalg.eigh(Q.T@H@Q); v=Q@U[:,0]
    p=np.linalg.lstsq(B,v,rcond=None)[0]
    return ev[0],p
def box(n,P,beta):
    a=pattern(P,beta); A=lambda x: a[x%P]
    bnd=lambda z: z[0] in (0,n) or z[1] in (0,n)
    links=[]
    for x1 in range(n+1):
        for x2 in range(n+1):
            for mu in (1,2):
                y=(x1+(mu==1),x2+(mu==2))
                if y[0]>n or y[1]>n: continue
                if bnd((x1,x2)) and bnd(y): continue
                links.append(((x1,x2),mu))
    idx={l:i for i,l in enumerate(links)}
    def U(x,mu): return G(A(x[0])) if mu==2 else I2
    D=3*len(links); H=np.zeros((D,D))
    var=lambda key: idx.get(key)
    for x1 in range(n):
        for x2 in range(n):
            x=(x1,x2)
            mats=[((x,1),False,U(x,1)),(((x1+1,x2),2),False,U((x1+1,x2),2)),(((x1,x2+1),1),True,U((x1,x2+1),1)),((x,2),True,U(x,2))]
            plaq_hess_add(H,mats,var)
    cols=[]
    for x1 in range(1,n):
        for x2 in range(1,n):
            for c in range(3):
                v=np.zeros(D)
                for (l,i0) in idx.items():
                    (y,mu)=l; z=(y[0]+(mu==1),y[1]+(mu==2))
                    if y==(x1,x2):
                        Bm=U(*l); M=np.linalg.inv(Bm)@s[c]@Bm
                        for i in range(3): v[3*i0+i]+=0.5*np.trace(M@s[i]).real
                    if z==(x1,x2): v[3*i0+c]-=1
                cols.append(v)
    V=np.array(cols).T
    Qv,_=np.linalg.qr(V); Pm=np.eye(D)-Qv@Qv.T; w,Uu=np.linalg.eigh(Pm); Bh=Uu[:,w>0.5]
    ev,Y=np.linalg.eigh(Bh.T@H@Bh); v=Bh@Y[:,0]
    return ev[0],v,links
def rat(x,den=10**6): return '%d/%d'%(int(round(x*den)),den)
out=open('lc55_2_proposals.txt','w')
for (tau_num,tau_den,n) in [(1,10,9),(1,10,60),(1,50,9),(1,50,240)]:
    tau=tau_num/tau_den; beta=2*math.atan(tau)
    e,p=cyl(n,3,beta); p=p/np.max(np.abs(p))
    out.write('CYL tau=%d/%d n=%d float_lowest=%.6e params %s\n'%(tau_num,tau_den,n,e,' '.join(rat(x) for x in p)))
    print('cyl',tau_num,tau_den,n,e,flush=True)
tau=0.1; beta=2*math.atan(tau); n=12
e,v,links=box(n,3,beta); v=v/np.max(np.abs(v))
out.write('BOX tau=1/10 n=12 float_lowest=%.6e links %s\n'%(e,' '.join('%d,%d,%d'%(l[0][0],l[0][1],l[1]) for l in links)))
out.write('BOXVEC %s\n'%(' '.join(rat(x) for x in v)))
print('box',e,flush=True)
out.close()
