"""Extract the local second-order hyperdiagonal equation from first geometry variations."""
import itertools,json,time,hashlib
from pathlib import Path
import sympy as s
start=time.monotonic();A,B,lam=s.symbols('A B lambda',real=True)
f=s.symbols('f0:8',real=True)
d=s.symbols('d0:4',real=True)
xi=[s.symbols('xi'+str(i)+'_0:8',real=True) for i in range(4)]
def index(v):return 4*v[0]+2*v[1]+v[2]
pairs=list(itertools.combinations(range(5),2))
normals=[s.Matrix([-1,0,0,0]),s.Matrix([1,-1,0,0]),s.Matrix([0,1,-1,0]),s.Matrix([0,0,1,-1]),s.Matrix([0,0,0,1])]

def phi(v):return f[4*v[0]+2*v[1]+v[2]]

def edge(v,w):
    step=[w[i]-v[i] for i in range(4)]
    scalar=(step[3]-sum(step[:3]))*(phi(v)+phi(w))
    # An affine static displacement xi(v)=v_0*d. Its difference is step_0*d.
    gauge=2*sum(step[i]*(xi[i][index(w)]-xi[i][index(v)]) for i in range(4))
    return scalar+gauge+(lam if sum(step)==4 else 0)

value=0;terms=[]
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
    for m in range(1,4):
        i,j=[v for v in (1,2,3) if v!=m];ni,nj=normals[i],normals[j]
        aa,bb,cc=ni.dot(ni),ni.dot(nj),nj.dot(nj)
        W=(ni.T*H*nj)[0]-bb*((ni.T*H*ni)[0]/aa+(nj.T*H*nj)[0]/cc)/2
        c=e(0,4)-e(0,m)-e(m,4)
        term=s.expand(-c*W/(8*m*(4-m)))
        value+=term;terms.append(dict(perm=perm,split=m,term=str(term)))
value=s.factor(value)
print('expanded terms:',len(s.Add.make_args(s.expand(value))))
print('field-only:',s.factor(value.subs({x:0 for row in xi for x in row})))
print('zero-hyper field/gauge:',s.factor(value.subs(lam,0)))
out=dict(expression=str(value),terms=terms,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),elapsed_sec=time.monotonic()-start,scope='first coefficient extraction, not a proof of nonlinear existence or global failure')
Path(__file__).with_name('BLOCK10_GENERAL_GAUGE_COEFFICIENT.json').write_text(json.dumps(out,indent=2)+'\n')
