import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import ast,collections,itertools,json,math,resource,signal,time,hashlib
from pathlib import Path
from fractions import Fraction
out=Path(__file__).resolve().parent
runtime=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
def guard():
    assert not (runtime/'STOP_REQUESTED.json').exists()
    assert time.time()<json.loads((runtime/'DEADLINE.json').read_text())['deadline_epoch']
guard();resource.setrlimit(resource.RLIMIT_CPU,(40,41));signal.alarm(90)
t0=time.monotonic();c0=time.process_time()
steps=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
add=lambda a,b:tuple(x+y for x,y in zip(a,b))
near=lambda a:[add(a,d) for d in steps]
zero=(0,0,0);ex=(1,0,0);ey=(0,1,0);ez=(0,0,1)
d2={add(a,b) for a in steps for b in steps}-{zero}
sources={}
def load_defs(path,names):
    raw=path.read_bytes();sources[str(path.relative_to(out.parent))]=hashlib.sha256(raw).hexdigest()
    tree=ast.parse(raw);body=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in names]
    assert {n.name for n in body}==set(names)
    exec(compile(ast.Module(body=body,type_ignores=[]),str(path),'exec'),globals())
load_defs(out.parent/'independent-fast-small-sector-check/check_words.py',['charge','state','step','physical'])
load_defs(out.parent/'finite-spin-fast-response-route/check_spin.py',
          ['weight','elementary','op','plus','gate','diagonal','local','flux'])
def hole(st):
    return next(x for x,q in st[0] if sum(x)%2==0 and q==0)
def dist(x,y):return sum(abs(a-b) for a,b in zip(x,y))
def occupied(st):return {x for x,q in st[0] if sum(x)%2 and q}
def V(st):
    h=hole(st);bs=occupied(st)
    if not set(near(h))<=bs or sum(dist(h,b)<=3 for b in bs)>9:return None
    for d in steps:
        b=add(h,d);c=add(b,d)
        if set(near(c))&bs=={b}:
            ans=step(step(st,h,b,'in'),c,b,'out');assert ans is not None
            return ans
    raise AssertionError('No clean axial row')
def Ocol(st):
    v=V(st)
    if v is not None:return {v:-1j}
    c=hole(st);shared=set(near(c))&occupied(st)
    if len(shared)!=1:return {}
    b=next(iter(shared));h=tuple(2*x-y for x,y in zip(b,c))
    mid=step(st,c,b,'in')
    if mid is None:return {}
    old=step(mid,h,b,'out')
    if old is not None and V(old)==st:return {old:1j}
    return {}
def O(v):
    result=collections.defaultdict(complex)
    for st,a in v.items():
        for x,b in Ocol(st).items():result[x]+=a*b
    return dict(result)
def addv(*terms):
    result=collections.defaultdict(complex)
    for coef,v in terms:
        for st,a in v.items():result[st]+=coef*a
    return {st:a for st,a in result.items() if abs(a)>1e-12}
def applyH(v,S):
    result=collections.defaultdict(complex)
    for st,a in v.items():
        for x,b in local(st,S).items():result[x]+=a*b
    return dict(result)
def loss(st,S):
    q,e=map(dict,st);h=hole(st)
    if S is None:return Fraction(2*sum(not charge(q,b) for b in near(h)))
    return sum((Fraction(2)-Fraction(2*e.get((h,b),0)**2,S*(S+1))
                for b in near(h) if not charge(q,b)),Fraction())
def applyG(v,S):return {st:a*float(loss(st,S)) for st,a in v.items()}
def project(v,S):return {st:a for st,a in v.items() if all(abs(e)<=S for _,e in st[1])}
def A(v,S,adj=False):return addv(((1j if adj else -1j),applyH(v,S)),(-.5,applyG(v,S)))
def T(v,S=None):
    r=addv((3,v),(-1,O(v)))
    return r if S is None else project(r,S)
def lyap(v,S,compressed):
    return addv((1,A(T(v,S if compressed else None),S,True)),
                (1,T(A(v,S),S if compressed else None)))
def delta_exact(st,S,centers=None):
    q,e=map(dict,st);z=Fraction()
    for (a,b),m in e.items():
        if centers is not None and a not in centers:continue
        if charge(q,a) and not charge(q,b) and gate(q,a):
            z+=(Fraction(1) if abs(m)>S or abs(m-charge(q,a))>S
                else Fraction(m*(m-charge(q,a)),S*(S+1)))
    return z
def DH(v,S):
    hs=applyH(v,S);hr=applyH(v,None)
    diag={st:a*float(diagonal(st,S)) for st,a in v.items()}
    return addv((1,hs),(-1,diag),(-1,hr))
def DG(v,S):return addv((1,applyG(v,S)),(-1,applyG(v,None)))
def Del(v,S):return {st:a*float(diagonal(st,S)) for st,a in v.items()}
def error(v,S):
    return addv((-3,DG(v,S)),(-1j,DH(O(v),S)),(1j,O(DH(v,S))),
                (-1j,Del(O(v),S)),(1j,O(Del(v,S))),
                (.5,DG(O(v),S)),(.5,O(DG(v,S))))
base=((),());c=(1,1,0);d=(1,0,1);extra=(2,0,1)
for aa,bb,kind,sg in [(c,ex,'out',0),(c,ey,'birth',1),(d,ez,'out',0),
    (d,extra,'birth',1),(zero,(0,-1,0),'out',0),(zero,(-1,0,0),'birth',1),
    (zero,(0,0,-1),'out',0)]:
    base=step(base,aa,bb,kind,sg);assert base is not None
rows=[];gauss=0;max_error=0.;boundary=0;distant_nonzero=0
for S in (1,2,5):
    for local_center,local_flux in [(zero,-1),(zero,0),(zero,1),((-2,0,0),-S)]:
        st0=flux(base,local_center,local_flux)
        if any(abs(e)>S for _,e in st0[1]):continue
        target0=V(st0);assert target0 is not None
        reference_delta=delta_exact(target0,S)-delta_exact(st0,S)
        for distant_flux in (0,S):
            guard();st=flux(st0,(30,0,0),distant_flux);target=V(st)
            gauss+=physical({st:1,target:1})
            h=hole(st);c1=hole(target)
            centers={h,c1}|{add(h,z) for z in d2}|{add(c1,z) for z in d2}
            assert len(centers)<=38
            full_diff=delta_exact(target,S)-delta_exact(st,S)
            local_diff=delta_exact(target,S,centers)-delta_exact(st,S,centers)
            assert full_diff==local_diff==reference_delta
            if distant_flux:
                assert delta_exact(st,S)>delta_exact(st0,S);distant_nonzero+=1
            if any(abs(e)>S for _,e in target[1]):boundary+=1
            vec={st:1.};left=lyap(vec,S,True)
            right=project(addv((1,lyap(vec,None,False)),(1,error(vec,S))),S)
            keys=set(left)|set(right)
            err=max((abs(left.get(x,0)-right.get(x,0)) for x in keys),default=0.)
            scale=1+max((abs(z) for v in (left,right) for z in v.values()),default=0.)
            assert err<=1e-10*scale
            gauss+=physical({x:1 for x in keys});max_error=max(max_error,err)
            assert all(all(abs(e)<=S for _,e in x[1]) for x in left)
            rows.append({'S':S,'local_center':local_center,'local_flux':local_flux,'remote_flux':distant_flux,
                'Delta_commutator_rational':str(full_diff),'compensation_centers':len(centers),
                'compressed_column_size':len(keys),'max_error':err,
                'selected_rotor_output_in_spin':not any(abs(e)>S for _,e in target[1])})
result={'scope':'exact diagonal-locality and floating compressed multiplier algebra; not all-field theorem',
    'rows':rows,'Gauss_words':gauss,'actual_boundary_blocked_selected_paths':boundary,
    'nonzero_distant_compensation_cases':distant_nonzero,'max_compression_error':max_error,
    'reused_definition_sources':sources,'cpu_seconds':time.process_time()-c0,
    'wall_seconds':time.monotonic()-t0,'rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
assert result['cpu_seconds']<40 and result['rss_bytes']<150*1024**2
(out/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result));assert boundary>0 and distant_nonzero>0
print('TOTAL: PASS=2 FAIL=0')
