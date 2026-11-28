import math, random
random.seed(1)
# 1. threshold
print("tanh(log(1651/1650)/2)*3301 =", math.tanh(math.log(1651/1650)/2)*3301)
# 2. two-level excess ratios
for k in (1,13):
    v=math.exp(-k); print("kappa",k,"excess",2*v/(1+v*v),"vs 1/1650",1/1650)
# 3. chord TV bound maximum
for R in (1.5,4.0,50.0):
    best=max(((R*m-1)*(1-m)/((R-1)*m),m) for m in [1/R+i*(1-1/R)/20000 for i in range(1,20000)])
    print("R",R,"max",best[0],"at m",best[1],"formula",(math.sqrt(R)-1)/(math.sqrt(R)+1),"m*",1/math.sqrt(R))
# 4. tangential covariance of e^{H.x} on S^3: (1/3)E sin^2 r times (1+H)
def tang(H,n=200000):
    num=den=0.0
    for i in range(1,n):
        r=math.pi*i/n; w=math.sin(r)**2*math.exp(-H*(1-math.cos(r)))
        den+=w; num+=w*math.sin(r)**2
    return num/den/3
for H in (0.0,1.0,10.0,100.0,1000.0):
    t=tang(H); print("H",H,"tangential var",t,"times (1+H)",t*(1+H))
# 5. commutator identity
def qmul(a,b):
    a0,a1,a2,a3=a; b0,b1,b2,b3=b
    return (a0*b0-a1*b1-a2*b2-a3*b3, a0*b1+a1*b0+a2*b3-a3*b2, a0*b2-a1*b3+a2*b0+a3*b1, a0*b3+a1*b2-a2*b1+a3*b0)
def conj(a): return (a[0],-a[1],-a[2],-a[3])
def unit_imag():
    v=[random.gauss(0,1) for _ in range(3)]; s=math.sqrt(sum(x*x for x in v)); return [x/s for x in v]
err=0
for _ in range(2000):
    ti,tj=random.uniform(0,math.pi),random.uniform(0,math.pi); ni,nj=unit_imag(),unit_imag()
    qi=(math.cos(ti),*[math.sin(ti)*x for x in ni]); qj=(math.cos(tj),*[math.sin(tj)*x for x in nj])
    c=qmul(qmul(qi,qj),qmul(conj(qi),conj(qj)))
    cr=[ni[1]*nj[2]-ni[2]*nj[1],ni[2]*nj[0]-ni[0]*nj[2],ni[0]*nj[1]-ni[1]*nj[0]]
    pred=2*math.sin(ti)**2*math.sin(tj)**2*sum(x*x for x in cr)
    err=max(err,abs((1-c[0])-pred))
print("commutator identity max error",err)
# 6. harmonic minorant minimum on |x|<=r/2, 0<=y<=r/2 (r=1)
r=1.0
mv=min(math.cos(math.pi*x/(2*r))*math.sinh(math.pi*(r-y)/(2*r))/math.sinh(math.pi/2) for x in [i/200-0.5 for i in range(201)] for y in [j/400 for j in range(201)])
print("min v",mv)
# 7. McDiarmid exponent: P(|S|>E/2)<=2exp(-2(3N/2)^2/(N*24^2))
print("McDiarmid exponent per N",2*(1.5)**2/(24**2))
