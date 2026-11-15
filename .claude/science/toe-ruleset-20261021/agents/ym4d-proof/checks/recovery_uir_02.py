from fractions import Fraction as F
from datetime import datetime,timezone

print('UTC:',datetime.now(timezone.utc).isoformat())
def matmul(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),F()) for j in range(len(B[0]))] for i in range(len(A))]
def mv(A,x): return [sum((a*b for a,b in zip(row,x)),F()) for row in A]
def dot(x,y): return sum((a*b for a,b in zip(x,y)),F())
def inv(A):
    n=len(A); M=[row[:]+[F(i==j) for j in range(n)] for i,row in enumerate(A)]
    for j in range(n):
        pivot=next(i for i in range(j,n) if M[i][j])
        M[j],M[pivot]=M[pivot],M[j]
        d=M[j][j]; M[j]=[x/d for x in M[j]]
        for i in range(n):
            if i!=j:
                c=M[i][j]; M[i]=[a-c*b for a,b in zip(M[i],M[j])]
    return [row[n:] for row in M]
def polyadd(a,b): return [a[k]+b[k] for k in range(5)]
def polyscale(a,c): return [c*x for x in a]
def polymul(a,b): return [sum((a[i]*b[k-i] for i in range(k+1)),F()) for k in range(5)]
def polypow(a,n):
    q=[F(1)]+[F()]*4
    for _ in range(n): q=polymul(q,a)
    return q

tests=[]
def gate(name,x,detail=''):
    tests.append(x); print(name+': '+('PASS' if x else 'FAIL')+(' | '+detail if detail else ''))
for T in (3,4,7):
    H=[[F(5,2)*F(i==j)-F((i-j)%T==1)-F((j-i)%T==1) for j in range(T)] for i in range(T)]
    G=inv(H); r=F(1,2)
    GP=[[F(2,3)*(r**((i-j)%T)+r**(T-(i-j)%T))/(1-r**T) for j in range(T)] for i in range(T)]
    gate('P1 exact inverse=periodization T='+str(T),G==GP)
    identity=[[F(i==j) for j in range(T)] for i in range(T)]
    unperiodized=[[F(2,3)*r**min((i-j)%T,(j-i)%T) for j in range(T)] for i in range(T)]
    gate('P1 omitted-image control T='+str(T),matmul(H,unperiodized)!=identity)
    b=[F((i%3)-1, i+1) for i in range(T)]; b[0]=F(1)
    g=F(3,5); h=F(7,4)
    x1=mv(G,b)
    x2=mv(G,[-g*a*a/2 for a in x1])
    x3=mv(G,[-g*a*c-h*a*a*a/6 for a,c in zip(x1,x2)])
    xp=[[F(),a,c,d,F()] for a,c,d in zip(x1,x2,x3)]
    energy=[F()]*5
    for i in range(T):
        for j in range(T):
            energy=polyadd(energy,polyscale(polymul(xp[i],xp[j]),H[i][j]/2))
        linear=[F()]+xp[i][:-1]
        energy=polyadd(energy,polyscale(linear,-b[i]))
        energy=polyadd(energy,polyscale(polypow(xp[i],3),g/6))
        energy=polyadd(energy,polyscale(polypow(xp[i],4),h/24))
    third=g*sum((a**3 for a in x1),F())
    sq=[a*a for a in x1]
    fourth_direct=h*sum((a**4 for a in x1),F())
    exchange=3*g*g*dot(sq,mv(G,sq))
    gate('P2 cubic value-jet T='+str(T),6*energy[3]==third)
    gate('P2 quartic value-jet T='+str(T),24*energy[4]==fourth_direct-exchange)
    gate('P2 dropped-exchange control T='+str(T),24*energy[4]!=fourth_direct,
         'nonzero exchange='+str(exchange))
print('EXACT PREDICATES:',str(sum(tests))+'/'+str(len(tests)))
print('Scope: finite scalar matrix algebra and stationary polynomial jets only.')
print('No all-momentum, group-action, n-uniform, or Yang–Mills result is inferred from this runner.')
assert all(tests)
