"""Independent finite controls; imports no submitted code. Standard library only."""
from fractions import Fraction as Q
from itertools import product, combinations
import json, pathlib, hashlib, math
P=pathlib.Path('/private/tmp/review-drain-20260915/sol-max-astra-low-8158/packet')
O=pathlib.Path(__file__).parent
out={}
m=json.loads((P/'manifest.json').read_text())
out['source_identities']=[{'path':f['path'],'sha256':hashlib.sha256((P/f['path']).read_bytes()).hexdigest(),'hash_matches':hashlib.sha256((P/f['path']).read_bytes()).hexdigest()==f['sha256'],'size_matches':(P/f['path']).stat().st_size==f['bytes']} for f in m['files']]
def edge(a,b,t):
    return t[0] if a==b else t[1] if a//2==b//2 else t[2]
def mat(t):return [[edge(a,b,t) for b in range(6)] for a in range(6)]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(6)) for j in range(6)]for i in range(6)]
def tv(w,f):
    z=sum(w); zz=sum(x*y for x,y in zip(w,f))
    return sum(abs(Q(x,z)-Q(x*y,zz)) for x,y in zip(w,f))/2
# First recorded spin fixed to 0. Simultaneous menu transitivity makes all six slices equiprobable.
configs=[(0,)+v for v in product(range(6),repeat=3)]
def ringw(c,t):return math.prod(edge(c[i],c[(i+1)%4],t) for i in range(4))
tri={}
for t in ((3,1,2),(5,2,4),(2,1,2)):
    w=[ringw(c,t) for c in configs]
    f=[sum(edge(c[0],u,t)*edge(c[1],u,t) for u in range(6))for c in configs]
    tri[str(t)]=str(tv(w,f))
out['abstract_triangle_fixture_tv']=tri
# Independently derive edges from coordinates, never manually wire a lattice fixture.
def lattice_edges(coords):return [(i,j) for i,j in combinations(range(len(coords)),2) if sum(abs(a-b) for a,b in zip(coords[i],coords[j]))==1]
bottom=[(0,0,0),(1,0,0),(1,1,0),(0,1,0)]
cube=bottom+[(x,y,1) for x,y,z in bottom]
out['cube_edges_from_coordinates']=lattice_edges(cube)
t=(3,1,2); tops=list(product(range(6),repeat=4)); es=lattice_edges(cube)
f=[]
for c in configs:
    f.append(sum(math.prod(edge((c+u)[i],(c+u)[j],t) for i,j in es if j>=4) for u in tops))
out['cube_tv']=str(tv([ringw(c,t) for c in configs],f))
# A legal and smaller lattice witness, recorded opposite corners of one plaquette.
w=[(0,0,0),(1,1,0)]; e=[(1,0,0)]
es=lattice_edges(w+e)
f=[sum(math.prod(edge((0,b,u)[i],(0,b,u)[j],t) for i,j in es) for u in range(6))for b in range(6)]
out['legal_path_witness']={'W':w,'E':e,'edges':es,'factors_for_first_spin_zero':f,'tv':str(tv([1]*6,f))}
# Adjacent lattice sites have no common nearest neighbour, certified by neighbor intersections.
def nbr(x):
    return {tuple(a+(s if k==d else 0) for k,a in enumerate(x)) for d in range(3) for s in (-1,1)}
out['adjacent_common_neighbours']=sorted(nbr(bottom[0])&nbr(bottom[1]))
# Forest and a one-attachment cycle: internal geometry includes every induced bond.
pendcoords=bottom+[(-1,0,0),(-2,0,0),(2,1,0)]
pe=lattice_edges(pendcoords)
pf=[]
for c in configs:
    pf.append(sum(math.prod(edge((c+u)[i],(c+u)[j],(2,1,2)) for i,j in pe if j>=4) for u in product(range(6),repeat=3)))
out['pendant_forest']={'edges':pe,'unique_factors':sorted(set(pf)),'tv':str(tv([ringw(c,(2,1,2)) for c in configs],pf))}
cc=[(0,0,0),(1,0,0),(2,0,0),(2,1,0),(1,1,0)]
ce=lattice_edges(cc)
cf=[sum(math.prod(edge((b,)+u if False else ((b,)+u)[i],((b,)+u)[j],t) for i,j in ce)for u in product(range(6),repeat=4))for b in range(6)]
out['one_attachment_cycle']={'edges':ce,'factors':cf}
# Orthogonal projectors, independent matrix construction via dot products of signed axes.
vecs=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
p0=[[Q(1,6)]*6 for _ in range(6)]
po=[[Q(sum(a*b for a,b in zip(v,w)),2)for w in vecs]for v in vecs]
pe=[[Q(i==j)-p0[i][j]-po[i][j] for j in range(6)]for i in range(6)]
spec=[]
for t in ((3,1,2),(5,2,4),(2,1,2),(1,3,2),(1,1,3),(2,2,2)):
    A=mat(t); power=[[int(i==j) for j in range(6)]for i in range(6)]
    for n in range(1,6):
        power=mm(power,A)
        z,o,e=t[0]+t[1]+4*t[2],t[0]-t[1],t[0]+t[1]-2*t[2]
        assert all(power[i][j]==z**n*p0[i][j]+o**n*po[i][j]+e**n*pe[i][j]for i in range(6)for j in range(6))
    spec.append({'pqr':t,'powers_1_through_5':'pass'})
out['spectral_checks']=spec
# Constant-rule counterexample to the unqualified iff.
out['constant_rule_bridge']={'pqr':[2,2,2],'factors':[24]*6,'tv':'0','touches_two':True}
# Marginal two-site law on a three-site chain induces nonlocal record dependence.
f=[sum(edge(0,u,(3,1,2))*edge(b,u,(3,1,2))for u in range(6))for b in range(6)]
out['R2_record_only_conditional_on_distant_record']=[str(Q(v,sum(f)))for v in f]
# Averaging preserves expectation inequalities but not arbitrary statements like independence.
prod1=[Q(9,16),Q(3,16),Q(3,16),Q(1,16)]
prod2=list(reversed(prod1));mix=[(a+b)/2 for a,b in zip(prod1,prod2)]
out['mixture_nonclosure_control']={'component_determinants':[str(prod1[0]*prod1[3]-prod1[1]*prod1[2]),str(prod2[0]*prod2[3]-prod2[1]*prod2[2])],'mixture':list(map(str,mix)),'mixture_determinant':str(mix[0]*mix[3]-mix[1]*mix[2])}
# Sphere integral: convergent exact coefficient series checked against independent Simpson quadrature.
def sphere_series(beta,t):
    a=beta*beta*(2+2*t)
    return 4*math.pi*sum(a**n/math.factorial(2*n+1) for n in range(40))
def simpson(beta,t,N=4000):
    z=beta*math.sqrt(2+2*t); h=2/N
    return 2*math.pi*h/3*sum((1 if k in (0,N) else 4 if k%2 else 2)*math.exp(z*(-1+k*h))for k in range(N+1))
out['sphere_controls']=[{'t':t,'series':sphere_series(1.3,t),'quadrature':simpson(1.3,t),'abs_error':abs(sphere_series(1.3,t)-simpson(1.3,t))}for t in (-1,0,.5,1)]
cid=next(f['path'] for f in m['files'] if f['path'].startswith('docs/ADMISSIBILITY_RULE_UNRECORDED'))
source=(P/cid).read_text();import re
out['changed_note_markdown_links']=re.findall(r'\]\(([^)]+)\)',source)
g=json.loads((P/'docs/audit/data/citation_graph_manifest.json').read_text())
out['submitted_graph_node']=g['nodes'][cid[5:-3].lower()]
(O/'checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='source_identities'},indent=2))
