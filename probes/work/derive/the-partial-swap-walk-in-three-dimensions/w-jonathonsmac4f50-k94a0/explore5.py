import sympy as sp, pickle, time
c1,c2,c3,s1,s2,s3,C,Sn=sp.symbols('c1 c2 c3 s1 s2 s3 C Sn')
e=sp.symbols('e',positive=True)
cs=[c1,c2,c3]; ss=[s1,s2,s3]
def mul(a,b):
    a0,av=a; b0,bv=b
    dot=sum(x*y for x,y in zip(av,bv))
    cr=[av[1]*bv[2]-av[2]*bv[1],av[2]*bv[0]-av[0]*bv[2],av[0]*bv[1]-av[1]*bv[0]]
    return (a0*b0-dot,[a0*bv[i]+b0*av[i]+cr[i] for i in range(3)])
def layer(j,sign,a):
    n=[0,0,0]; n[j]=cs[j]; n[(j+1)%3]=sign*ss[j]
    return (sp.cos(a),[sp.sin(a)*x for x in n])
seq=[(0,-1),(0,1),(1,-1),(1,1),(2,-1),(2,1)]
def serq(S,n=4):
    q0=sp.series(S[0],e,0,n+1).removeO()
    qv=[sp.series(x,e,0,n+1).removeO() for x in S[1]]
    return q0,qv
# plain product P = L6 L5 ... L1  (L1 applied first)
S=(sp.Integer(1),[0,0,0])
for (j,sg) in seq:
    S=mul(layer(j,sg,e),S)
q0,qv=serq(S,3)
q0=sp.expand(q0); qv=[sp.expand(x) for x in qv]
for n in range(0,4):
    print('plain order',n,'q0',sp.factor(q0.coeff(e,n)),' q',[sp.factor(x.coeff(e,n)) for x in qv])
