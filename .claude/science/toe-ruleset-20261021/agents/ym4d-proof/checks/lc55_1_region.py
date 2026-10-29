# lc55_1 — stripe configurations in the multiscale small-field region (criteria: lc55_1_criteria.md). Exact arithmetic.
# SU(2) element a*I + i(b s1 + c s2 + d s3) stored as (a,b,c,d) of Fractions.
from fractions import Fraction as F
from itertools import permutations, product
import sys, time
ONE=(F(1),F(0),F(0),F(0))
def qmul(p,q):
    a,b,c,d=p; e,f,g,h=q
    # (a+iu)(e+iv) = (ae-u.v) + i(av+eu-u x v)
    return (a*e-b*f-c*g-d*h,
            a*f+e*b-(c*h-d*g),
            a*g+e*c-(d*f-b*h),
            a*h+e*d-(b*g-c*f))
def qconj(p): return (p[0],-p[1],-p[2],-p[3])
def is_one(p): return p[0]==1 and p[1]==0 and p[2]==0 and p[3]==0
def G(tau,sgn):  # exp(i sgn*beta*s3), beta=2 arctan tau
    den=1+tau*tau
    return ((1-tau*tau)/den,F(0),F(0),sgn*2*tau/den)
def make_field(L,side,amap):
    # amap: function x0 -> quaternion for direction-1 (the "x_2" direction) links; all other links identity
    def U(z,nu):
        if nu==1: return amap(z[0]%side)
        return ONE
    return U
def step(U,z,nu,s,side):
    # transporter for one step from z to z+s e_nu
    if s==1:
        return U(z,nu), tuple((z[i]+(1 if i==nu else 0))%side for i in range(4))
    zz=tuple((z[i]-(1 if i==nu else 0))%side for i in range(4))
    return qconj(U(zz,nu)), zz
def path(U,z,target_coords,order,side,L):
    # complete-axial path from z, moving coordinate order[0] first, along the SHORTEST lattice displacement inside the block
    q=ONE; cur=list(z)
    for nu in order:
        disp=target_coords[nu]-cur[nu]
        s=1 if disp>0 else -1
        for _ in range(abs(disp)):
            m,nz=step(U,tuple(cur),nu,s,side)
            if not is_one(m): q=qmul(q,m)
            cur=list(nz)
    return q, tuple(cur)
def transporter(U,X,mu,y_off,order,L,side):
    # c_X = L X + h(1,1,1,1); y = L X + y_off; T = P^s(c_X->y) S_y P^s(c_Y->y+L e_mu)^dag
    h=(L-1)//2
    cX=tuple(L*X[i]+h for i in range(4)); y=tuple(L*X[i]+y_off[i] for i in range(4))
    cY=tuple(cX[i]+(L if i==mu else 0) for i in range(4)); yL=tuple(y[i]+(L if i==mu else 0) for i in range(4))
    p1,_=path(U,cX,y,order,side,L)
    q=p1; cur=y
    for _ in range(L):
        m,cur=step(U,cur,mu,1,side)
        if not is_one(m): q=qmul(q,m)
    p2,_=path(U,cY,yL,order,side,L)
    return qmul(q,qconj(p2))
def straight(U,X,mu,L,side):
    h=(L-1)//2; cur=tuple(L*X[i]+h for i in range(4)); q=ONE
    for _ in range(L):
        m,cur=step(U,cur,mu,1,side)
        if not is_one(m): q=qmul(q,m)
    return q
def center(U,X,mu,L,side):
    Ts=[]; offs=list(product(range(L),repeat=4))
    for order in permutations(range(4)):
        for yo in offs:
            Ts.append(transporter(U,X,mu,yo,list(order),L,side))
    n=len(Ts)
    Mbar=tuple(sum(T[k] for T in Ts)/n for k in range(4))
    return Ts,Mbar
def G1_link(U,X,mu,L,side):
    Ts,M=center(U,X,mu,L,side)
    a_ok=all(T[1]==0 and T[2]==0 for T in Ts)
    b_ok=(M[1]==0 and M[2]==0 and M[3]==0 and M[0]>0)
    S=straight(U,X,mu,L,side); c_ok=is_one(S)
    return a_ok,b_ok,c_ok,M
def plaquette_values(U,side):
    vals=set()
    for z in product(range(side),repeat=4):
        for mu in range(4):
            for nu in range(mu+1,4):
                a,z1=step(U,z,mu,1,side); b,z2=step(U,z1,nu,1,side); c,z3=step(U,z2,mu,-1,side); d,_=step(U,z3,nu,-1,side)
                P=qmul(qmul(qmul(a,b),c),d)
                vals.add(2-2*P[0])
    return sorted(vals)
def run_G1(L,tau,pattern_name,amap_vals):
    side=2*L
    amap=lambda x0: amap_vals[x0%len(amap_vals)]
    U=make_field(L,side,amap)
    allok=True; rec=[]
    for mu in range(4):
        X0=(0,0,0,0); X1=(1,1,0,1)
        a0,b0,c0,M0=G1_link(U,X0,mu,L,side)
        a1,b1,c1,M1=G1_link(U,X1,mu,L,side)
        d_ok=(M0==M1)
        ok=a0 and b0 and c0 and a1 and b1 and c1 and d_ok
        allok=allok and ok
        rec.append((mu,a0,b0,c0,a1,b1,c1,d_ok,M0))
    return allok,rec,plaquette_values(U,side)
t0=time.time()
print('lc55_1 start',flush=True)
results={}
for L in (3,5):
    for tau in (F(1,10),F(1,1000)):
        h=(L-1)//2
        vals=[ONE]*L; vals[h-1]=G(tau,1); vals[h+1]=G(tau,-1)
        ok,rec,pv=run_G1(L,tau,'centred',vals)
        results[(L,tau)]=ok
        print('G1 L=%d tau=%s centred-antisymmetric: %s'%(L,tau,'PASS' if ok else 'FAIL'),flush=True)
        for r in rec:
            mu,a0,b0,c0,a1,b1,c1,d_ok,M0=r
            print('   mu=%d torus(a)=%s,%s real+(b)=%s,%s straight=1(c)=%s,%s transl(d)=%s r_c=%s'%(mu,a0,a1,b0,b1,c0,c1,d_ok,M0[0]),flush=True)
        print('   record: set of 2-trU_p over level-0 plaquettes =',[str(v) for v in pv],flush=True)
        print('   elapsed %.1fs'%(time.time()-t0),flush=True)
G1=all(results.values())
print('G1 overall:', 'PASS' if G1 else 'FAIL',flush=True)
# Control C1a: L=3, pattern (beta,0,0)
tau=F(1,10)
vals=[G(tau,1),ONE,ONE]
ok,rec,pv=run_G1(3,tau,'C1a',vals)
print('C1a (pattern (beta,0,0)): G1 predicate =',ok,'-> control', 'FIRED' if not ok else 'DID NOT FIRE',flush=True)
for r in rec:
    print('   mu=%d (b)=%s M=%s'%(r[0],r[2],[str(x) for x in r[8]]),flush=True)
# Control C1b: L=3, period-2 pattern on side-6 torus
L=3; side=6
amap=lambda x0: G(tau,1) if x0%2==1 else ONE
U=make_field(L,side,amap)
Ms={}
allb=True
for X in product(range(2),repeat=4):
    for mu in range(4):
        Ts,M=center(U,X,mu,L,side); Ms[(X,mu)]=M
        if not (M[1]==0 and M[2]==0 and M[3]==0 and M[0]>0): allb=False
def norm2(M): return sum(x*x for x in M)
nontriv=0
for X in product(range(2),repeat=4):
    for mu in range(4):
        for nu in range(mu+1,4):
            Xm=tuple((X[i]+(1 if i==mu else 0))%2 for i in range(4)); Xn=tuple((X[i]+(1 if i==nu else 0))%2 for i in range(4))
            A=Ms[(X,mu)]; B=Ms[(Xm,nu)]; C=Ms[(Xn,mu)]; D=Ms[(X,nu)]
            P=qmul(qmul(qmul(A,B),qconj(C)),qconj(D))
            re=P[0]; prodn2=norm2(A)*norm2(B)*norm2(C)*norm2(D)
            # 2 - tr V_P > 0  <=>  re < sqrt(prodn2)  (V_P = P/sqrt(prodn2))
            if re<=0 or re*re<prodn2: nontriv+=1
print('C1b (period 2, L=3): all centres positive scalars =',allb,'; coarse plaquettes with 2-trV_P>0:',nontriv,'-> control','FIRED' if (not allb and nontriv>0) else 'DID NOT FIRE',flush=True)
print('lc55_1 done, %.1fs'%(time.time()-t0),flush=True)
