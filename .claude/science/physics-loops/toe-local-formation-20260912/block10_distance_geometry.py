"""Distance-Gram geometry copied from the prior nonlinear checker for full-force use."""
import itertools,json,time,hashlib,signal
from pathlib import Path
import mpmath as mp
AUDIT_TIMEOUT_SEC=180
mp.mp.dps=65;started=time.monotonic();checks=[]
def check(name,cond):
    if not cond:raise AssertionError(name)
    checks.append(name)
perms=list(itertools.permutations(range(4)))
sets=[tuple(v) for v in itertools.product((0,1),repeat=4) if any(v)]
zero=(0,0,0,0);full=(1,1,1,1)
triangles=[(zero,u,w) for w in sets for u in sets if u!=w and all(u[i]<=w[i] for i in range(4))]
assert len(triangles)==50
standard=[mp.matrix(4,1)]+[mp.eye(4)[:,j] for j in range(4)]

def area_sq(qa,qb,qc):return (2*(qa*qb+qa*qc+qb*qc)-qa*qa-qb*qb-qc*qc)/16

def simplex_data(vertices,q):
    lengths={(i,j):q(vertices[i],vertices[j]) for i,j in itertools.combinations(range(5),2)}
    def e(i,j):return 0 if i==j else lengths[tuple(sorted((i,j)))]
    G=mp.matrix(4)
    for i in range(1,5):
        for j in range(1,5):G[i-1,j-1]=(e(0,i)+e(0,j)-e(i,j))/2
    return G

def hinge_data(G,i,j):
    hinge=[a for a in range(5) if a not in (i,j)]
    u=standard[hinge[1]]-standard[hinge[0]];v=standard[hinge[2]]-standard[hinge[0]]
    legs=[standard[i]-standard[hinge[0]],standard[j]-standard[hinge[0]]]
    def dot(a,b):return (a.T*G*b)[0]
    D=mp.matrix([[dot(u,u),dot(u,v)],[dot(v,u),dot(v,v)]])
    inv=D**-1
    projections=[mp.matrix([dot(u,l),dot(v,l)]) for l in legs]
    def contracted(a,b):return dot(legs[a],legs[b])-(projections[a].T*inv*projections[b])[0]
    cosine=contracted(0,1)/mp.sqrt(contracted(0,0)*contracted(1,1))
    return mp.sqrt(mp.det(D))/2,mp.acos(cosine)

paths=[]
for perm in perms:
    vertices=[zero]
    for axis in perm:
        v=list(vertices[-1]);v[axis]=1;vertices.append(tuple(v))
    paths.append(vertices)

def cell_action(q):
    areas=mp.fsum(mp.sqrt(area_sq(q(v,u),q(u,w),q(v,w))) for v,u,w in triangles)
    angles=mp.mpf(0)
    for vertices in paths:
        G=simplex_data(vertices,q)
        for i,j in itertools.combinations(range(5),2):
            a,t=hinge_data(G,i,j);angles+=a*t
    return 2*mp.pi*areas-angles

def hyper_equation(q):
    deficits={u:2*mp.pi for u in sets if u!=full}
    for vertices in paths:
        G=simplex_data(vertices,q)
        for m in range(1,4):
            i,j=[v for v in (1,2,3) if v!=m]
            _,theta=hinge_data(G,i,j);deficits[vertices[m]]-=theta
    value=mp.mpf(0)
    for u,deficit in deficits.items():
        qa,qb,qc=q(zero,u),q(u,full),q(zero,full)
        area=mp.sqrt(area_sq(qa,qb,qc))
        value+=(qa+qb-qc)*deficit/(16*area)
    return value

def plane_q(n,epsilon,fields,xis,lambdas):
    L=len(fields)
    def q(v,w):
        step=[w[i]-v[i] for i in range(4)];a=(n+v[0])%L;b=(n+w[0])%L
        variation=(step[3]-sum(step[:3]))*(fields[a]+fields[b])
        variation+=2*sum(step[i]*(xis[i][b]-xis[i][a]) for i in range(4))
        variation+=lambdas[n] if sum(step)==4 else 0
        return mp.mpf(sum(step))+epsilon*variation
    return q

def cubic_target(fields,xis,lambdas):
    L=len(fields);value=mp.mpf(0)
    for n in range(L):
        j=(n+1)%L;g=fields[j]-fields[n];ds=[xis[i][j]-xis[i][n] for i in range(4)];la=lambdas[n]
        value+=(2*(fields[n]+fields[j])+ds[0])*g*g+la*la*sum(ds[1:])/4+la**3/8
    return value
