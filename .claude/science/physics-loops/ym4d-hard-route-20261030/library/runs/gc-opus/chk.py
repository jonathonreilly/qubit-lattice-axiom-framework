import math, random
random.seed(1)
def haar():
    v=[random.gauss(0,1) for _ in range(4)]; n=math.sqrt(sum(t*t for t in v)); return [t/n for t in v]
# quaternion a+bi+cj+dk <-> SU(2); x(W)=(1/2)tr W = real part
def mul(p,q):
    a1,b1,c1,d1=p;a2,b2,c2,d2=q
    return [a1*a2-b1*b2-c1*c2-d1*d2,a1*b2+b1*a2+c1*d2-d1*c2,a1*c2-b1*d2+c1*a2+d1*b2,a1*d2+b1*c2-c1*b2+d1*a2]
def inv(p): return [p[0],-p[1],-p[2],-p[3]]
R=haar();S=haar();M=200000;s=0.0
for _ in range(M):
    k=haar(); ki=inv(k); s+=mul(R,ki)[0]*mul(S,ki)[0]
print("Haar identity MC", s/M, "predicted", mul(R,inv(S))[0]/4)
# ball volume: (2/pi) int_0^d sin^2 vs d^3/24
for d in [0.1,0.5,1.0]:
    vol=(2/math.pi)*(d/2-math.sin(2*d)/4); print("delta",d,"vol",vol,"d^3/24",d**3/24, vol>=d**3/24)
c=8+(2/3)*math.log(24)
f=lambda b:(math.log(b)+c)/b
for target,name in [(1.0,"nontrivial"),(79/80,"mu>1/80"),(159/160,"mu>1/160")]:
    b=1.0
    while f(b)>=target: b+=0.01
    print(name,"from beta ~",round(b,2))
print("const",c)
