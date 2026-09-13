"""Extract the complete cubic cell action on a plane-symmetric static family."""
import itertools,json,time,hashlib
from pathlib import Path
import sympy as s
start=time.monotonic();f0,f1,lam=s.symbols('f0 f1 lambda',real=True);ds=s.symbols('d0:4',real=True)
pairs=list(itertools.combinations(range(5),2))
normals=[s.Matrix([-1,0,0,0]),s.Matrix([1,-1,0,0]),s.Matrix([0,1,-1,0]),s.Matrix([0,0,1,-1]),s.Matrix([0,0,0,1])]
def phi(v):return f1 if v[0] else f0
def edge(v,w):
    step=[w[i]-v[i] for i in range(4)]
    return (step[3]-sum(step[:3]))*(phi(v)+phi(w))+2*step[0]*sum(step[i]*ds[i] for i in range(4))+(lam if sum(step)==4 else 0)
value=0
for perm in itertools.permutations(range(4)):
    vertices=[(0,0,0,0)]
    for axis in perm:
        v=list(vertices[-1]);v[axis]=1;vertices.append(tuple(v))
    q={(i,j):edge(vertices[i],vertices[j]) for i,j in pairs}
    def e(i,j):return 0 if i==j else q[tuple(sorted((i,j)))]
    H=s.zeros(4)
    for a in range(1,5):
        H[a-1,a-1]=e(a-1,a)
        for b in range(a+1,5):H[a-1,b-1]=H[b-1,a-1]=(e(a,b-1)+e(a-1,b)-e(a,b)-e(a-1,b-1))/2
    H2=(H*H).applyfunc(s.expand)
    local=0
    for i,j in pairs:
        ni,nj=normals[i],normals[j];a,b,c=ni.dot(ni),ni.dot(nj),nj.dot(nj);D=a*c-b*b
        N=ni.row_join(nj);P=s.eye(4)-N*(N.T*N).inv()*N.T
        u=(ni.T*H*ni)[0]/a;v=(nj.T*H*nj)[0]/c
        U=(ni.T*H2*ni)[0]/a;V=(nj.T*H2*nj)[0]/c
        B=(ni.T*H*nj)[0];B2=(ni.T*H2*nj)[0]
        s1=(u+v)/2;s2=3*(u*u+v*v)/8+u*v/4-(U+V)/2
        W=B-b*s1;Z=-b*s2+B*s1-B2;t=s.trace(P*H)
        cA=t*t/8-s.trace(P*H*P*H)/4
        local+=t*Z/12-t*b*W*W/(24*D)+cA*W/3
    value+=s.expand(local)
value=s.factor(value)
print(value)
out=dict(expression=str(value),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),elapsed_sec=time.monotonic()-start,scope='first extraction of a derived rational cubic identity, not nonlinear existence')
Path(__file__).with_name('BLOCK10_CUBIC_FIRST.json').write_text(json.dumps(out,indent=2)+'\n')
