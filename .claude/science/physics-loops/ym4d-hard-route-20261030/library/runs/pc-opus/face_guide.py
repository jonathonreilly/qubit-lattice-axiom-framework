# GUIDE only. Gaussian face-corner test, own implementation.
# Free links: base in B or C (no torus; exterior cochain = 0).
# Covariance of A_U, A_V = (C^T C)^+ restricted to quotient functionals,
# computed by CG on C^T C + D D^T (D = gradients at interior vertices).
import itertools, sys, math
def run(L, shift3=0):
    B=[(-L,L),(0,2*L),(-L,L),(-L,L)]
    C=[(0,2*L),(-L,L),(-L,L),(-L,L)]
    inbox=lambda x,R: all(R[i][0]<=x[i]<=R[i][1] for i in range(4))
    inS=lambda x: inbox(x,B) or inbox(x,C)
    def e(m): return tuple(1 if i==m else 0 for i in range(4))
    add=lambda x,y: tuple(a+b for a,b in zip(x,y))
    sub=lambda x,y: tuple(a-b for a,b in zip(x,y))
    rng=[range(-L-2,2*L+3)]*4
    sites=[x for x in itertools.product(*rng) if inS(x)]
    links={}
    for x in sites:
        for m in range(4): links[(x,m)]=len(links)
    n=len(links)
    # plaquettes touching S
    plaqs=set()
    for (x,m) in links:
        for nu in range(4):
            if nu==m: continue
            a,b=min(m,nu),max(m,nu)
            plaqs.add((x,a,b)); plaqs.add((sub(x,e(nu)),a,b))
    rows=[]
    for (x,a,b) in plaqs:
        r=[]
        for (y,mm,s) in [(x,a,1),(add(x,e(a)),b,1),(add(x,e(b)),a,-1),(x,b,-1)]:
            if (y,mm) in links: r.append((links[(y,mm)],s))
        if r: rows.append(r)
    # interior vertices: all 8 incident links free
    grads=[]
    for x in sites:
        inc=[((x,m),-1) for m in range(4)]+[((sub(x,e(m)),m),1) for m in range(4)]
        if all(k in links for k,_ in inc):
            grads.append([(links[k],s) for k,s in inc])
    def matvec(v):
        out=[0.0]*n
        for r in rows+grads:
            t=sum(s*v[i] for i,s in r)
            if t:
                for i,s in r: out[i]+=s*t
        return out
    def cg(bvec):
        x=[0.0]*n; r=bvec[:]; p=r[:]; rr=sum(t*t for t in r)
        for it in range(5000):
            Ap=matvec(p); al=rr/sum(a*b for a,b in zip(p,Ap))
            x=[a+al*b for a,b in zip(x,p)]; r=[a-al*b for a,b in zip(r,Ap)]
            rn=sum(t*t for t in r)
            if rn<1e-22: break
            p=[a+(rn/rr)*b for a,b in zip(r,p)]; rr=rn
        return x
    v=(0,0,-L+shift3,0)
    U=links[(sub(v,e(0)),0)]; V=links[(sub(v,e(1)),1)]
    e0=(sub(v,e(2)),2); print("e0 free?", e0 in links)
    bu=[0.0]*n; bu[U]=1; bv=[0.0]*n; bv[V]=1
    xu=cg(bu); xv=cg(bv)
    a=xu[U]; c=xu[V]; b=xv[V]
    corr=c/math.sqrt(a*b)
    print(f"L={L} links={n} a={a:.6f} b={b:.6f} c={c:.6f} t=a+b-2c={a+b-2*c:.6f} s={a+b+2*c:.6f} corr={corr:.6f} corr^2={corr*corr:.6f}")
run(1); run(2)
