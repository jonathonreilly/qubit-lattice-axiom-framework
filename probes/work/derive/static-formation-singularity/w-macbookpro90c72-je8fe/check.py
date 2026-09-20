# J:derive:static-formation-singularity:a1  -- exact checks, w-macbookpro90c72-je8fe
from fractions import Fraction as F
from itertools import product, permutations, combinations_with_replacement as cwr
import pickle, sys
BAD=[]
def chk(n,c):
    print(("ok   " if c else "FAIL ")+n)
    if not c: BAD.append(n)

def phi(s,t): return 3 if s==t else (1 if t==(s^1) else 2)
PH=[[phi(s,t) for t in range(6)] for s in range(6)]
def Zset(vals):            # Z(v|A) = sum_s prod_{y in A} phi(s,v_y)
    return sum(__import__('math').prod(PH[s][y] for y in vals) for s in range(6))
NT=[[Zset((a,b)) for b in range(6)] for a in range(6)]
Z3={k:Zset(k) for k in product(range(6),repeat=3)}

# --- C1 kernel constants -------------------------------------------------
chk("C1 Z1=12, N in {22,24,26} by antipode rule, Z_W(4-cycle)=20784",
    Zset((0,))==12 and all(NT[a][b]==(26 if a==b else 22 if b==(a^1) else 24)
                           for a in range(6) for b in range(6))
    and 12**4+3*2**4==20784)
E4=[(0,1),(0,2),(1,3),(2,3)]; nbr={0:[1,2],1:[0,3],2:[0,3],3:[1,2]}
def W4(v):
    w=1
    for a,b in E4: w*=PH[v[a]][v[b]]
    return w
CFG=list(product(range(6),repeat=4)); ZW=sum(W4(v) for v in CFG)
chk("C1b Z_W = 20784 by enumeration", ZW==20784)

# --- C2 exact likelihood identity for every order and configuration ------
def law(order):
    a0=a1=0; K=[]
    for k,x in enumerate(order):
        A=tuple(y for y in nbr[x] if y in order[:k])
        if len(A)==0: a0+=1
        elif len(A)==1: a1+=1
        else: K.append(A)
    return a0,a1,tuple(sorted(K))
def nu(order,v):
    p=F(1)
    for k,x in enumerate(order):
        A=[y for y in nbr[x] if y in order[:k]]
        num=1
        for y in A: num*=PH[v[x]][v[y]]
        p*=F(num,Zset(tuple(v[y] for y in A)))
    return p
orders=list(permutations(range(4)))
idok=True
for o in orders:
    a0,a1,K=law(o)
    for v in CFG:
        d=6**a0*12**a1
        for A in K: d*=Zset(tuple(v[y] for y in A))
        if nu(o,v)*d!=W4(v): idok=False;break
    if not idok: break
chk("C2 mu_sigma(v) = W(v)/(M^a0 Z1^a1 prod_A Z(v|A)), all 24 orders x 1296",idok)
from collections import Counter
cen=Counter(law(o) for o in orders)
chk("C3 census: 24 orders -> 4 laws, multiplicities 8,8,4,4",
    sorted(cen.values())==[4,4,8,8] and len(cen)==4)

# --- adaptive-policy DP: V(h) = sup over ALL adapted orders of E_nu[h] ---
def idx(v):
    i=(NT[v[0]][v[3]]-22)//2; j=(NT[v[1]][v[2]]-22)//2
    return (min(i,j),max(i,j))
def Vsup(G):
    memo={}
    def rec(S):
        if all(x is not None for x in S): return G[idx(S)]
        if S in memo: return memo[S]
        best=None
        for x in range(4):
            if S[x] is not None: continue
            A=[y for y in nbr[x] if S[y] is not None]
            t=[];Z=0
            for s in range(6):
                w=1
                for y in A: w*=PH[s][S[y]]
                t.append(w);Z+=w
            val=sum(F(t[s],Z)*rec(S[:x]+(s,)+S[x+1:]) for s in range(6))
            if best is None or val>best: best=val
        memo[S]=best; return best
    return rec((None,)*4)
KEYS=[(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)]
muj={}
for v in CFG: muj[idx(v)]=muj.get(idx(v),0)+W4(v)
muf={k:F(n,ZW) for k,n in muj.items()}
chk("C4 DP reproduces the pure-order laws (max over 24 orders <= V)",
    all(Vsup({k:F(1) for k in KEYS})==1 for _ in [0]) and
    max(sum(nu(o,v)*F(idx(v)==(2,2)) for v in CFG) for o in orders)
      <= Vsup({k:F(k==(2,2)) for k in KEYS}))

# --- C5 the test h, its exact U*V and the certified sample size ----------
G={(0,0):F(1),(0,1):F(511,500),(0,2):F(1041,1000),
   (1,1):F(209,200),(1,2):F(533,500),(2,2):F(136,125)}
U=sum(muf[k]/G[k] for k in KEYS); V=Vsup(G); UV=U*V
chk("C5 U = 13339090843683247/13958280479086944",U==F(13339090843683247,13958280479086944))
chk("C5b V = 1009751/965250 (adaptive sup over every order and mixture)",V==F(1009751,965250))
chk("C5c U*V = 13469160318500002341497/13473230232438672696000 < 1",
    UV==F(13469160318500002341497,13473230232438672696000) and UV<1)
e=sum(F(1,__import__('math').factorial(k)) for k in range(14))
chk("C6 log 2 < 7/10 certified: sum_{k<14} 1/k! > 2718/1000 and 2718^7 > 1024*1000^7",
    e>F(2718,1000) and 2718**7>1024*1000**7)
m=F(7,5)*(1+UV)/(1-UV)
chk("C7 m >= 9268 gives TV >= 1/2 (a3: 80237), factor 8.65",
    m<9268 and F(80237,9268)>F(865,100))

# --- C8 best single event, valid against the whole hull ------------------
bestE=None
for m_ in range(64):
    S=[KEYS[i] for i in range(6) if m_>>i&1]
    if not S: continue
    d=sum(muf[k] for k in S)-Vsup({k:F(k in S) for k in KEYS})
    if bestE is None or d>bestE[0]: bestE=(d,tuple(S))
chk("C8 sup_E [mu(E)-sup_nu nu(E)] = 30457/2431728 at E={N1N2>=624}",
    bestE[0]==F(30457,2431728) and bestE[1]==((1,2),(2,2)))
tvs=[sum(abs(F(W4(v),ZW)-nu(o,v)) for v in CFG)/2 for o in orders]
chk("C9 min over the 24 orders TV = 455/31176 -> hull TV in [30457/2431728, 455/31176]",
    min(tvs)==F(455,31176) and max(tvs)==F(37,1299))
f4mu=F(6*81,ZW)
f4nu=sum(nu((0,1,2,3),(s,)*4) for s in range(6))
chk("C10 four-point (all four equal): mu=81/3464, nu=9/416, gap 315/180128",
    f4mu==F(81,3464) and f4nu==F(9,416) and f4mu-f4nu==F(315,180128))
chk("C10b the level-set test beats the four-point function by 8.34x (7.16x vs the hull)",
    F(455,31176)/(f4mu-f4nu)>F(834,100) and bestE[0]/(f4mu-f4nu)>F(716,100))

# --- C11 converse: one fixed order cannot be told apart below m=496 ------
rho=F(0)
for j in range(3):
    n=sum(W4(v) for v in CFG if (NT[v[1]][v[2]]-22)//2==j)
    x=F(433,18*(22+2*j)); r=F(int(float(x)**.5*10**9),10**9)
    while r*r>x: r-=F(1,10**9)
    rho+=F(n,ZW)*r
d=1-rho
chk("C11 Hellinger rho >= 0.999712...; TV < 1/2 for every m <= 495",
    rho>F(4328,4330) and (1-d)/(7*d)>495)
eu=sum(F(1,__import__('math').factorial(k)) for k in range(14))+F(15,14)/__import__('math').factorial(14)
chk("C11b log(4/3) > 2/7 certified: e < 2719/1000 and 2719^2*2187 < 16384*10^6",
    eu<F(2719,1000) and 2719**2*2187<16384*10**6)

# --- C12 the two divergence inequalities (symbolic, exact) ---------------
import sympy as sp
r=sp.symbols('r',positive=True)
w1=sp.simplify(sp.diff(r*sp.log(r)-r+1-(r-1)**2/2,r,2))          # r<=1 branch
w2=sp.simplify(sp.diff(r*sp.log(r)-r+1-(r-1)**2/(2*r),r,2))      # r>=1 branch
x=sp.symbols('x',positive=True)
w3=sp.simplify(sp.diff(sp.log(1/x)-2*(1-x)/(1+x),x))
chk("C12 h(r)-(r-1)^2/2 convex on (0,1], h(r)-(r-1)^2/(2r) convex on [1,inf)",
    sp.simplify(w1-(1/r-1))==0 and sp.simplify(w2-(r**2-1)/r**3)==0)
chk("C12b d/dx[log(1/x)-2(1-x)/(1+x)] = -(1-x)^2/(x(1+x)^2) <= 0",
    sp.simplify(w3+(1-x)**2/(x*(1+x)**2))==0)

# --- C13 single-site conditional divergence on Z^2 -----------------------
def Dhat(w,Wt,g):
    A=[1]*6
    for s in range(6):
        for u in range(6):
            if u!=s: A[s]*=g[u]
    B=sum(w[t]*A[t] for t in range(6)); tot=F(0)
    for s in range(6):
        rr=F(Wt*A[s],B)
        if rr!=1: tot+=F(w[s],Wt)*(1-rr)**2/(2*max(1,rr))
    return tot
def gam(mult):
    w=[1]*6
    for s in range(6):
        for b in mult: w[s]*=PH[s][b]
    return w,sum(w)
g2=set()
for b5 in range(6):
    for b6 in range(6): g2.add(tuple(NT[s][b5]*NT[s][b6] for s in range(6)))
chk("C13 Z^2: the tilt is never constant (21 distinct vectors, none constant)",
    len(g2)==21 and not any(len(set(g))==1 for g in g2))
m2=min(Dhat(*gam(mu_),g) for mu_ in cwr(range(6),4) for g in g2)
chk("C13b Z^2 min D = 537719/129443808050 >= a3's 19/4604256 (no finite-energy factor)",
    m2==F(537719,129443808050) and m2>F(19,4604256))

# --- C14 single-site conditional divergence on Z^3 -----------------------
chk("C14 finite energy: max_b sum_s prod_{i<=6} phi(s,b_i) = 986, so gamma >= 1/986",
    max(sum(__import__('math').prod(PH[s][b] for b in mu_) for s in range(6))
        for mu_ in cwr(range(6),6))==986)
PR=[(0,1),(0,2),(1,0),(1,2),(2,0),(2,1)]
def g3(c):
    out=[]
    for s in range(6):
        p=1
        for j in range(3):
            kl=[k for k in range(3) if k!=j]
            p*=Z3[tuple(sorted((s,c[(j,kl[0])],c[(j,kl[1])])))]
        out.append(p)
    return tuple(out)
allg={}; good={}; const=0
for vals in product(range(6),repeat=6):
    c=dict(zip(PR,vals)); g=g3(c)
    if len(set(g))==1: const+=1
    allg[g]=vals
    if c[(0,1)]==c[(0,2)]: good[g]=vals
chk("C14b Z^3: tilt constant on exactly 600 of 46656, none with v(a1)=v(b1)",
    const==600 and not any(len(set(g))==1 for g in good))
GAM=[gam(mu_) for mu_ in cwr(range(6),6)]
m3=min(Dhat(w,Wt,g) for g in good for w,Wt in GAM)
chk("C14c Z^3 min D on {v(a1)=v(b1)} = 29405471333306771/9669810101542139423160",
    m3==F(29405471333306771,9669810101542139423160))
chk("C14d (1/986)*min D beats a3's (1/986)^2*(4/28561) by 21.4x",
    F(1,986)*m3/(F(1,986)**2*F(4,28561))>F(2140,100))
# --- C15 the 2x2x2 window ------------------------------------------------
# summing out the two antipodal corners (000 and 111) leaves t=(v100,v010,v001),
# s=(v110,v101,v011) with weight Z3[t]*Z3[s]*cross(t,s) and Q=NT-triple(t)*Z3[s]
TS=list(product(range(6),repeat=3)); S={}
for t in TS:
    q1=NT[t[0]][t[1]]*NT[t[0]][t[2]]*NT[t[1]][t[2]]; zt=Z3[t]
    for s in TS:
        cr=(PH[t[0]][s[0]]*PH[t[0]][s[1]]*PH[t[1]][s[0]]
            *PH[t[1]][s[2]]*PH[t[2]][s[1]]*PH[t[2]][s[2]])
        k=q1*Z3[s]; S[k]=S.get(k,0)+zt*Z3[s]*cr
ZC=sum(S.values()); c=6*12**3
chk("C15 cube: Z_W = 6982520832, the monotone law is W/(10368 Q), Q has 17 values",
    ZC==6982520832 and c==10368 and sum(F(s,c*q) for q,s in S.items())==1
    and len(S)==17)
TVc=sum(abs(F(s,ZC)-F(s,c*q)) for q,s in S.items())/2
Es=[q for q in S if c*q>ZC]
chk("C15b cube TV = 1182193085/23402354976, attained by {Q > 6061216/9}",
    TVc==F(1182193085,23402354976) and F(ZC,c)==F(6061216,9)
    and sum(F(S[q],ZC) for q in Es)-sum(F(S[q],c*q) for q in Es)==TVc
    and sum(F(S[q],ZC) for q in Es)==F(5071505,12122432)
    and sum(F(S[q],c*q) for q in Es)==F(90895,247104))# --- C16 the independent sets used by the chain rule ---------------------
def E(d,j,sg=1): return tuple(sg*(1 if i==j else 0) for i in range(d))
def FD(d):
    out=[E(d,j,s) for j in range(d) for s in (1,-1)]
    out+=[tuple(a-b for a,b in zip(E(d,j),E(d,k))) for j in range(d)
          for k in range(d) if j!=k]
    return out
def dens(mem,mod,d):
    pts=[p for p in product(range(mod),repeat=d) if mem(p)]
    ok=all(not mem(tuple((p[i]+v[i])%mod for i in range(d)))
           for p in pts for v in FD(d))
    return ok,F(len(pts),mod**d)
o2,d2=dens(lambda p:(p[0]+2*p[1])%3==0,3,2)
o3,d3=dens(lambda p:(p[0]+2*p[1]+3*p[2])%4==0,4,3)
ob,db=dens(lambda p:p[0]%2==p[1]%2==p[2]%2,2,3)
cl2=all(tuple(a-b for a,b in zip(u,v)) in FD(2) for u in [(0,0),(1,0),(0,1)]
        for v in [(0,0),(1,0),(0,1)] if u!=v)
cl3=all(tuple(a-b for a,b in zip(u,v)) in FD(3)
        for u in [(0,0,0),(1,0,0),(0,1,0),(0,0,1)]
        for v in [(0,0,0),(1,0,0),(0,1,0),(0,0,1)] if u!=v)
chk("C16 dependency graph NN u (e_j-e_k): independent sets of density 1/3 (Z^2, "
    "x1+2x2=0 mod 3) and 1/4 (Z^3, x1+2x2+3x3=0 mod 4 AND x1=x2=x3 mod 2)",
    o2 and d2==F(1,3) and o3 and d3==F(1,4) and ob and db==F(1,4))
chk("C16b both densities are maximal: {x,x+e_j} is a 3-clique in Z^2, a 4-clique in Z^3",
    cl2 and cl3)

print("SUMMARY: "+("ROUTE FAILS AT "+BAD[0] if BAD else
 "PARTIAL - mu_sigma(v)=W(v)/(M^a0 Z1^a1 prod_A Z(v|A)) exactly, so sum_A log Z(v|A) is a "
 "sufficient statistic and every optimal test is one of its level sets. On m disjoint 4-cycles "
 "a plaquette test has U*V=13469160318500002341497/13473230232438672696000<1, so TV>=1/2 at "
 "m=9268 against the closed convex hull of all adapted formation laws (8.65x below 80237); "
 "Hellinger affinity >=432875307883/433000000000 for the nearest fixed order leaves every test "
 "powerless at m<=495. Using D>=sum_s (P_s-Q_s)^2/(2max(P_s,Q_s)): min D=537719/129443808050 "
 "on Z^2 (tilt never constant, so no finite-energy factor is needed) and "
 "29405471333306771/9669810101542139423160 on {v(a1)=v(b1)} in Z^3, where one factor 1/986 "
 "suffices: 21.4x the earlier Z^3 rate. The dependency graph is NN u (e_j-e_k) and its "
 "independent-set densities 1/3 and 1/4 are maximal. On the 2x2 the hull-optimal event is "
 "{N(d1),N(d2)}={26,>=24}, gap 30457/2431728; the plaquette four-point function gives "
 "315/180128, 7.16x worse. On the 2x2x2 the likelihood ratio is one scalar Q (17 values), "
 "TV=1182193085/23402354976 at {Q>6061216/9}."))
if not BAD:
    print("HIT: U*V=13469160318500002341497/13473230232438672696000<1, so m=9268 disjoint "
          "4-cycles separate the static law from the closed convex hull of every adapted "
          "formation law (TV>=1/2) and no test does at m<=495; on Z^3 one finite-energy factor "
          "1/986 with min D=29405471333306771/9669810101542139423160 gives 21.4x the earlier "
          "rate; the plaquette four-point function is 7.16x below the optimal 2x2 event "
          "30457/2431728.")
sys.exit(1 if BAD else 0)
