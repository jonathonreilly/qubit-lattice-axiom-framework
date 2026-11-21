# GUIDE only: checks hand calculations on binary polyhedral subgroups of SU(2).
import itertools, math
from fractions import Fraction
def qmul(a,b):
    a0,a1,a2,a3=a; b0,b1,b2,b3=b
    return (a0*b0-a1*b1-a2*b2-a3*b3, a0*b1+a1*b0+a2*b3-a3*b2, a0*b2-a1*b3+a2*b0+a3*b1, a0*b3+a1*b2-a2*b1+a3*b0)
def qinv(a): return (a[0],-a[1],-a[2],-a[3])
def key(q): return tuple(round(x,9)+0.0 for x in q)
def close(gens):
    G={key((1.0,0,0,0)):(1.0,0.0,0.0,0.0)}
    frontier=list(G.values())
    while frontier:
        new=[]
        for g in frontier:
            for h in gens:
                p=qmul(g,h); k=key(p)
                if k not in G: G[k]=p; new.append(p)
        frontier=new
    return list(G.values())
phi=(1+5**0.5)/2
Q8=close([(0,1.0,0,0),(0,0,1.0,0)])
T2=close([(0,1.0,0,0),(0,0,1.0,0),(0.5,0.5,0.5,0.5)])
O2=close([(0,1.0,0,0),(0,0,1.0,0),(0.5,0.5,0.5,0.5),(2**-0.5,2**-0.5,0,0)])
I2=close([(0.5,0.5,0.5,0.5),(phi/2,0.5,1/(2*phi),0)])
groups={'Q8':Q8,'2T':T2,'2O':O2,'2I':I2}
catalan=[1,1,2,5,14,42,132]
print('orders',{k:len(v) for k,v in groups.items()})
for name,G in groups.items():
    row=[]
    for k in range(1,7):
        m=sum(g[0]**(2*k) for g in G)/len(G)
        su2=catalan[k]/4**k
        row.append((2*k, round(m*4**k,6), catalan[k], 'same' if abs(m-su2)<1e-9 else 'DIFF'))
    first=[r[0] for r in row if r[3]=='DIFF']
    print(name,'first differing degree of E[x^2k]:',first[0] if first else None,'| 4^k*E[x^2k]:',[r[1] for r in row])
# commutator subgroups
for name,G in groups.items():
    comms=[qmul(qmul(a,b),qmul(qinv(a),qinv(b))) for a in G for b in G]
    H=close(list({key(c):c for c in comms}.values()))
    # average commutator as quaternion (fundamental rep acts by left mult): E[[A,B]] should be (1/4,0,0,0)
    avg=[sum(c[i] for c in comms)/len(comms) for i in range(4)]
    print(name,'|[G,G]|=',len(H),'E[[A,B]] =',[round(x,6) for x in avg])
# Q8 pair filter on spin 1: t'=(cosh b-1)/(cosh b+3); compare formula
def adj(q):
    # rotation matrix of q acting on imaginary quaternions
    w,x,y,z=q
    return [[1-2*(y*y+z*z),2*(x*y-w*z),2*(x*z+w*y)],[2*(x*y+w*z),1-2*(x*x+z*z),2*(y*z-w*x)],[2*(x*z-w*y),2*(y*z+w*x),1-2*(x*x+y*y)]]
for b in (0.5,1.0,1.15,2.0):
    Z=sum(math.exp(b*g[0]) for g in Q8)
    M=[[sum(math.exp(b*g[0])*adj(g)[i][j] for g in Q8)/Z for j in range(3)] for i in range(3)]
    print('Q8 beta',b,'spin-1 filter diag',[round(M[i][i],6) for i in range(3)],'formula',round((math.cosh(b)-1)/(math.cosh(b)+3),6))
# Bessel I_n by series
def I(n,x): return sum((x/2)**(2*m+n)/(math.factorial(m)*math.factorial(m+n)) for m in range(60))
b=2.0
print('beta=2: r_1/2=I2/I1',round(I(2,b)/I(1,b),5),' r_3/2=I4/I1',round(I(4,b)/I(1,b),6),' r_5/2=I6/I1',round(I(6,b)/I(1,b),7),' r_11/2=I12/I1',I(12,b)/I(1,b))
for name,G in groups.items():
    Z=sum(math.exp(b*g[0]) for g in G); r=sum(math.exp(b*g[0])*g[0] for g in G)/Z
    print(name,'beta=2 fundamental filter r^G_1/2 =',round(r,5))
# Q8 one-link covariance sup: F along (1,1,0,0)/sqrt2 * f, direction u=(1,-1,0,0)/sqrt2
for f in (0,1,5,20,50):
    c=f/2**0.5
    ws=[math.exp(f*(g[0]+g[1])/2**0.5) for g in Q8]; Z=sum(ws)
    mu=sum(w*(g[0]-g[1])/2**0.5 for w,g in zip(ws,Q8))/Z
    var=sum(w*((g[0]-g[1])/2**0.5)**2 for w,g in zip(ws,Q8))/Z-mu**2
    print('Q8 |F|=',f,'variance along u =',round(var,6))
import resource; print('maxrss MB',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
