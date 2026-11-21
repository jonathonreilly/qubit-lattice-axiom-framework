# Guide run for FINISH 1099. Pure Python. One serial job. Guides only.
import math, random, sys
random.seed(1099)
def rand_s3():
    while True:
        v=[random.gauss(0,1) for _ in range(4)]
        n=math.sqrt(sum(x*x for x in v))
        if n>1e-9: return [x/n for x in v]
def nbrs(i,L):
    x,y=i%L,i//L
    return (((x+1)%L)+y*L, ((x-1)%L)+y*L, x+((y+1)%L)*L, x+((y-1)%L)*L)
def wolff(s,L,beta,NB):
    n=rand_s3(); i0=random.randrange(L*L)
    proj=[sum(a*b for a,b in zip(s[i],n)) for i in range(L*L)]
    inc=[False]*(L*L); inc[i0]=True; st=[i0]; cl=[i0]
    while st:
        i=st.pop(); pi=proj[i]
        for j in NB[i]:
            if not inc[j]:
                t=pi*proj[j]
                if t>0 and random.random()<1-math.exp(-2*beta*t):
                    inc[j]=True; st.append(j); cl.append(j)
    for i in cl:
        p=proj[i]; si=s[i]
        s[i]=[si[k]-2*p*n[k] for k in range(4)]
    return len(cl)
def clusters(L,NB,bondp):
    # bondp(i,j) -> open probability; returns labels
    lab=[-1]*(L*L); c=0
    # sample bonds once (right and up edges)
    op={}
    for i in range(L*L):
        for j in (NB[i][0],NB[i][2]):
            op[(i,j)]=random.random()<bondp(i,j)
    def isopen(i,j):
        return op[(i,j)] if (i,j) in op else op[(j,i)]
    sizes=[]
    for i in range(L*L):
        if lab[i]<0:
            lab[i]=c; st=[i]; sz=1
            while st:
                a=st.pop()
                for b in NB[a]:
                    if lab[b]<0 and isopen(a,b):
                        lab[b]=c; st.append(b); sz+=1
            sizes.append(sz); c+=1
    nb=sum(op.values())/len(op)
    return lab,sizes,nb
def run(L,beta,ntherm,nmeas,gap):
    NB=[nbrs(i,L) for i in range(L*L)]
    A=[rand_s3() for _ in range(L*L)]; B=[rand_s3() for _ in range(L*L)]
    for _ in range(ntherm):
        wolff(A,L,beta,NB); wolff(B,L,beta,NB)
    res={'sw':[0,0,0],'sg':[0,0,0]}; en=0.0
    for m in range(nmeas):
        for _ in range(gap):
            wolff(A,L,beta,NB); wolff(B,L,beta,NB)
        d=[[ (A[i][k]-B[i][k])/2 for k in range(4)] for i in range(L*L)]
        def psw(i,j):
            t=sum(d[i][k]*d[j][k] for k in range(4))
            return 1-math.exp(-4*beta*t) if t>0 else 0.0
        def psg(i,j):
            t=A[i][0]*A[j][0]
            return 1-math.exp(-2*beta*t) if t>0 else 0.0
        for key,f in (('sw',psw),('sg',psg)):
            lab,sizes,nb=clusters(L,NB,f)
            far=sum(1 for i in range(L*L) if lab[i]==lab[(i%L+L//2)%L+(i//L)*L])/(L*L)
            res[key][0]+=nb; res[key][1]+=max(sizes)/(L*L); res[key][2]+=far
        en+=sum(sum(A[i][k]*A[NB[i][0]][k] for k in range(4)) for i in range(L*L))/(L*L)
    out={k:[x/nmeas for x in v] for k,v in res.items()}
    print("L=%d beta=%.2f energy/bond=%.4f"%(L,beta,en/nmeas))
    print("  swap clusters: bond density %.3f, largest/vol %.3f, P(x<->x+L/2) %.3f"%tuple(out['sw']))
    print("  sign clusters (one replica, first coordinate): bond density %.3f, largest/vol %.3f, P(x<->x+L/2) %.4f"%tuple(out['sg']))
    sys.stdout.flush()
# wall quadrature: <|s|> under weight rho*ds (uniform S^3) and under sinh(kappa*rho)ds
def quad(f,n=20000):
    h=1.0/n; return sum(f((i+0.5)*h) for i in range(n))*h
for kappa in (0.5,2.5):
    u=quad(lambda s: s*math.sqrt(1-s*s))/quad(lambda s: math.sqrt(1-s*s))
    w=quad(lambda s: s*math.sinh(kappa*math.sqrt(1-s*s)))/quad(lambda s: math.sinh(kappa*math.sqrt(1-s*s)))
    print("wall check kappa=%.1f: <|s|> uniform %.4f, with transverse field %.4f"%(kappa,u,w))
for L,beta in ((24,2.5),(48,2.5),(48,2.3)):
    run(L,beta,ntherm=600 if L<40 else 1500,nmeas=12,gap=25 if L<40 else 60)
