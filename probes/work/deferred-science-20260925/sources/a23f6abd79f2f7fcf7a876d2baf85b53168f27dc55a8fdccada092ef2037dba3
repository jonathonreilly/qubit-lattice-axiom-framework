"""Read-only global geometric enumeration and rational saved-result review."""
from pathlib import Path
from itertools import product,combinations
from fractions import Fraction as F
import hashlib,json

P=Path(__file__).resolve().parent
read=[P/'local_support_controls.py',P/'SOURCE_PINS.json',P/'WORKING_DERIVATION.md',
      *[P/'attempt01'/n for n in ['source.py','WORKING_BEFORE_CONTROL.md','EXECUTION.json','stdout.json','stderr.txt']]]
def ident(p):
    s=p.stat();return [hashlib.sha256(p.read_bytes()).hexdigest(),s.st_size,s.st_mtime_ns,s.st_ctime_ns,s.st_mode,s.st_ino]
before={str(p):ident(p) for p in read}
data=json.loads((P/'attempt01/stdout.json').read_text())
assert before[str(P/'local_support_controls.py')][0]==data['program_sha256']
assert (P/'attempt01/source.py').read_bytes()==(P/'local_support_controls.py').read_bytes()
assert not (P/'attempt01/stderr.txt').read_bytes()
assert json.loads((P/'attempt01/EXECUTION.json').read_text())['exit_code']==0
for pin in json.loads((P/'SOURCE_PINS.json').read_text())['sources']:
    assert hashlib.sha256(Path(pin['path']).read_bytes()).hexdigest()==pin['sha256']

def tuples(v):return tuple(tuples(x) for x in v) if isinstance(v,list) else v
rows=[]
offsets=[]
for i in range(3):
    for s in (-2,2):
        v=[0]*3;v[i]=s;offsets.append(tuple(v))
for i,j in combinations(range(3),2):
    for s,t in product((-1,1),repeat=2):
        v=[0]*3;v[i]=s;v[j]=t;offsets.append(tuple(v))
assert len(set(offsets))==18
for graph in data['graphs']:
    L=graph['L'];A=[x for x in product(range(L),repeat=3) if sum(x)%2==0]
    stars={};edges=[]
    for a in A:
        members={('s',*a)}
        for i,s in product(range(3),(-1,1)):
            b=list(a);b[i]=(b[i]+s)%L;b=tuple(b)
            members.update([('s',*b),('e',*a,*b)]);edges.append((a,b))
        assert len(members)==13;stars[a]=members
    pairs=set()
    for a in A:
        for off in offsets:
            c=tuple((a[i]+off[i])%L for i in range(3))
            assert c!=a;pairs.add(tuple(sorted((a,c))))
    assert len(pairs)==(15*L**3//4 if L==4 else 9*L**3//2)
    for label,saved in graph['sets'].items():
        S=set(tuples(saved['S']));X1=set(tuples(saved['X1']));X2=set(tuples(saved['X2']))
        expected_G=set();expected_G2=set();built=set(S)
        for a,st in stars.items():
            if st&S:expected_G.add(('f',a));built.update(st)
            if st&X2:expected_G2.add(('f',a))
        for a,c in pairs:
            st=stars[a]|stars[c]
            if st&S:expected_G.add(('h',a,c));built.update(st)
            if st&X2:expected_G2.add(('h',a,c))
        assert built==X1 and expected_G==set(tuples(saved['groups']))
        assert expected_G2==set(tuples(saved['halo_groups']))
        extended=set(X1)
        for a,b in edges:
            term={('s',*a),('s',*b),('e',*a,*b)}
            if term&X1:extended.update(term)
        assert extended==X2
        for gs,key,coeff in [(expected_G,'counts','J_coefficients'),(expected_G2,'halo_counts','J_halo_coefficients')]:
            counts={'formation':sum(g[0]=='f' for g in gs),'magnetic':sum(g[0]=='h' for g in gs)}
            assert counts==saved[key] and saved[coeff]==[5184*counts['magnetic'],600*counts['formation']]
        assert len(X1)<=4651*len(S) and len(X2)<=88369*len(S)
    for label,f,g,b in [('AA','A','A',4),('BB','B','B',1),('AB','A','B',2)]:
        d=graph['sets'][f if f==g else 'AB'];p=d['J_coefficients'];q=d['J_halo_coefficients']
        z=graph['sets'][f]['J_coefficients'];w=graph['sets'][g]['J_coefficients']
        vals=[F(b)*(F(p[0]*q[0],2)+z[0]*w[0]),F(b)*(F(p[0]*q[1]+p[1]*q[0],2)+z[0]*w[1]+z[1]*w[0]),F(b)*(F(p[1]*q[1],2)+z[1]*w[1])]
        assert vals==list(map(F,graph['M'][label]))
    assert list(map(F,graph['means_in_kappa']))==[-60,60]
    assert [[F(v) for v in r] for r in graph['covariance_in_kappa']]==[[120,-20],[-20,120]]
    ex=graph['illustrative_delta_kappa_equal_one'];t=F(ex['max_time_for_bound_one_over_sixty'])
    ab=sum(map(F,graph['M']['AB']));bb=sum(map(F,graph['M']['BB']))
    assert 120-t*bb==F(ex['denominator'])>0
    assert t*(ab+bb/6)/(120-t*bb)==F(ex['ratio_error_bound'])<=F(1,60)
    rows.append(dict(L=L,global_magnetic_pairs=len(pairs),global_electric_terms=len(edges),
        local_sets={k:dict(X1=len(v['X1']),X2=len(v['X2']),counts=v['counts'],halo_counts=v['halo_counts']) for k,v in graph['sets'].items()},
        exact_bound_window=ex))
assert before=={str(p):ident(p) for p in read}
print(json.dumps(dict(status='All stored support sets, local group lists, global completeness and bound arithmetic checked.',
    mode='Read only, no primary imports/execution; different full-graph offset enumeration at all six sides.',
    observed_files=len(read),byte_and_stat_preservation=True,graphs=rows),indent=2))
