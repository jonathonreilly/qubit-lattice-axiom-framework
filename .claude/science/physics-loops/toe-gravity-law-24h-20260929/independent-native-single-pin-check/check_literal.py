"""Independent exact Q(sqrt(2),sqrt(3)) occupation-creation controls."""
import datetime, fractions, hashlib, itertools, json, os, pathlib, resource, signal, time

START=time.perf_counter(); CPU=time.process_time()
ROOT=pathlib.Path(__file__).resolve().parent
RUN=pathlib.Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
deadline=json.loads((RUN/'DEADLINE.json').read_text())['deadline_epoch']
assert time.time()<deadline and not (RUN/'STOP_REQUESTED.json').exists()
assert all(os.environ.get(k)=='1' for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'))
resource.setrlimit(resource.RLIMIT_CPU,(30,30)); signal.alarm(120)
F=fractions.Fraction

class S:
    # Coefficients in basis 1,sqrt(2),sqrt(3),sqrt(6).
    def __init__(self,c=0):
        self.c=tuple(c) if isinstance(c,(tuple,list)) else (F(c),F(0),F(0),F(0))
    def __add__(self,v):
        v=v if isinstance(v,S) else S(v)
        return S(tuple(a+b for a,b in zip(self.c,v.c)))
    __radd__=__add__
    def __neg__(self):return S(tuple(-a for a in self.c))
    def __sub__(self,v):return self+-v
    def __mul__(self,v):
        v=v if isinstance(v,S) else S(v); out=[F(0)]*4
        for i,a in enumerate(self.c):
            if a:
                for j,b in enumerate(v.c):
                    if b:out[i^j]+=a*b*(2 if i&j&1 else 1)*(3 if i&j&2 else 1)
        return S(out)
    __rmul__=__mul__
    def __eq__(self,v):return self.c==(v.c if isinstance(v,S) else S(v).c)
    def serial(self):return [str(a) for a in self.c]

Z=S(); H2=S((F(0),F(1,2),F(0),F(0))); H6=S((F(0),F(0),F(0),F(1,6)))
unit=[tuple(int(i==j) for i in range(3)) for j in range(3)]
add=lambda x,y:tuple(a+b for a,b in zip(x,y))
scale=lambda c,x:tuple(c*a for a in x)
O=(0,0,0)
disps=[scale(2,e) for e in unit]
for i,j in itertools.combinations(range(3),2):
    for r in (1,-1):disps.append(add(unit[i],scale(r,unit[j])))
U=[[H2,H6,Z,Z,Z],[-H2,H6,Z,Z,Z],[Z,-2*H6,Z,Z,Z]]
for plane in range(3):
    for r in (1,-1):
        row=[Z]*5; row[plane+2]=-r*H2; U.append(row)
assert all(sum(U[d][a]*U[d][b] for d in range(9))==int(a==b) for a in range(5) for b in range(5))

def oriented(edge):
    x,y=sorted(edge); delta=tuple(b-a for a,b in zip(x,y))
    if delta in disps:return x,disps.index(delta)
    delta=tuple(-a for a in delta)
    if delta in disps:return y,disps.index(delta)
    return None

# Derive the centered-to-forward map from literal endpoints.
centered=[]
for i in range(3):centered.append((unit[i],scale(-1,unit[i]),1))
for i,j in itertools.combinations(range(3),2):
    for s,t in itertools.product((1,-1),repeat=2):
        centered.append((scale(s,unit[i]),scale(t,unit[j]),s*t))
counts=[0]*9; translations=[]
for x,y,sgn in centered:
    anchor,d=oriented((x,y)); counts[d]+=1
    assert set((x,y))==set((anchor,add(anchor,disps[d])))
    translations.append({'anchor':anchor,'type':d,'sign':sgn})
assert counts==[1]*3+[2]*6

# Raw real symmetric basis: off-diagonal basis has HS norm squared two.
bases=[[(i,i)] for i in range(5)]+[[(i,j),(j,i)] for i,j in itertools.combinations(range(5),2)]

def phi(Sites,basis):
    if len(Sites)!=4:return Z
    sites=sorted(Sites); ans=Z
    for selected in itertools.combinations(range(4),2):
        e=[sites[i] for i in selected]; f=[sites[i] for i in range(4) if i not in selected]
        re,rf=oriented(e),oriented(f)
        if re is None or rf is None:continue
        ans+=sum(U[re[1]][a]*U[rf[1]][b] for a,b in basis)
    return H2*ans

far=(10,11,12); images=[]; far_checks=0; pins=0
for basis in bases:
    image=[]
    for residual in disps:
        eta={O,residual}
        for d,disp in enumerate(disps):
            removed={far,add(far,disp)}
            actual=phi(eta|removed,basis)
            j=disps.index(residual)
            expected=2*H2*sum(U[d][a]*U[j][b] for a,b in basis)
            assert actual==expected
            image.append(actual); far_checks+=1
            # Literal hard-core extraction is zero if any endpoint remains occupied.
            pinned={O,disp}; output=Z if pinned&eta else phi(eta|pinned,basis)
            assert output==0; pins+=1
    images.append(image)
for i,j in itertools.product(range(15),repeat=2):
    gram=sum(a*b for a,b in zip(images[i],images[j]))
    expected=2*len(bases[i]) if i==j else 0
    assert gram==expected

out={'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
     'scalar_field':'exact Q(sqrt(2),sqrt(3))','forward_multiplicities':counts,
     'centered_translations':translations,'literal_far_creation_checks':far_checks,
     'literal_hard_core_pin_checks':pins,'full_channel_image_gram_entries_checked':225,
     'channel_image_gram_diagonal':[2]*5+[4]*10,
     'complex_extension':'real full Gram equality implies Hermitian norm equality for arbitrary complex symmetric A',
     'cpu_seconds':time.process_time()-CPU,'wall_seconds':time.perf_counter()-START,
     'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
     'finished_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
(ROOT/'literal_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
