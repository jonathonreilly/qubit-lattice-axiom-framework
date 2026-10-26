import sympy as sp, itertools, time
c1,c2,c3,s1,s2,s3,C,Sn=sp.symbols('c1 c2 c3 s1 s2 s3 C Sn')
cs=[c1,c2,c3]; ss=[s1,s2,s3]
def red(x):
    x=sp.expand(x)
    # reduce s_j^2 -> 1-c_j^2 and Sn^2->1-C^2
    p=sp.Poly(x,s1,s2,s3,Sn)
    out=0
    for mon,co in p.terms():
        a,b,cc,d=mon
        t=co
        t*= (1-c1**2)**(a//2)*s1**(a%2)
        t*= (1-c2**2)**(b//2)*s2**(b%2)
        t*= (1-c3**2)**(cc//2)*s3**(cc%2)
        t*= (1-C**2)**(d//2)*Sn**(d%2)
        out+=t
    return sp.expand(out)
def mul(a,b):
    a0,av=a; b0,bv=b
    dot=sum(x*y for x,y in zip(av,bv))
    cr=[av[1]*bv[2]-av[2]*bv[1],av[2]*bv[0]-av[0]*bv[2],av[0]*bv[1]-av[1]*bv[0]]
    return (a0*b0-dot,[a0*bv[i]+b0*av[i]+cr[i] for i in range(3)])
def layer(j,sign,cosa,sina):
    n=[0,0,0]; n[j]=cs[j]; n[(j+1)%3]=sign*ss[j]
    return (cosa,[sina*x for x in n])
# full angle e: cos e=C^2-Sn^2, sin e=2 C Sn ; half angle: C,Sn
half=lambda j,sg: layer(j,sg,C,Sn)
full=lambda j,sg: layer(j,sg,C**2-Sn**2,2*C*Sn)
seq=[(0,-1),(0,1),(1,-1),(1,1),(2,-1),(2,1)]
t=time.time()
S=(sp.Integer(1),[0,0,0])
for (j,sg) in seq[:5]:
    S=mul(S,half(j,sg)); S=(red(S[0]),[red(x) for x in S[1]])
S=mul(S,full(*seq[5])); S=(red(S[0]),[red(x) for x in S[1]])
for (j,sg) in reversed(seq[:5]):
    S=mul(S,half(j,sg)); S=(red(S[0]),[red(x) for x in S[1]])
print(time.time()-t)
q0=S[0]
print('q0 terms',len(sp.Add.make_args(q0)))
import pickle
pickle.dump((q0,S[1]),open('S_pal.pkl','wb'))
print(sp.factor(q0))
