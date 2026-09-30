"""Independent literal physical geometry and ordered-tensor sphere controls.
No author code is read or imported. This is finite control, not the proof.
"""
import itertools as it, math, json, time, resource, os
from fractions import Fraction as F
from pathlib import Path
start=time.process_time(); wall=time.monotonic()
runtime=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
assert not (runtime/'STOP_REQUESTED.json').exists()
assert time.time()<json.loads((runtime/'DEADLINE.json').read_text())['deadline_epoch']
# Exact ordered tensor entries avoid square-root occupation normalizations.
d=5
checks=0
for n in (2,3,5):
    states={}
    fixtures=[((n,0,0,0,0),1+2j),((0,n,0,0,0),2-1j),((0,0,n,0,0),-2+3j),((n-1,0,0,1,0),1-3j),((0,n-1,0,0,1),-1-2j),((1,0,n-1,0,0),3+1j)]
    for alpha,v in fixtures: states[alpha]=states.get(alpha,0)+v
    def counts(t): return tuple(t.count(i) for i in range(d))
    def psi(t): return states.get(counts(t),0)
    norm=sum(abs(psi(t))**2 for t in it.product(range(d),repeat=n))
    norm=int(round(norm))
    g1={(i,j):sum(psi((i,)+t)*psi((j,)+t).conjugate() for t in it.product(range(d),repeat=n-1)) for i in range(d) for j in range(d)}
    g2={(i,j,k,l):sum(psi((i,j)+t)*psi((k,l)+t).conjugate() for t in it.product(range(d),repeat=n-2)) for i,j,k,l in it.product(range(d),repeat=4)}
    coeff={a:math.factorial(n)//math.prod(math.factorial(x) for x in a)*v for a,v in states.items()}
    dimension=math.comb(n+d-1,d-1)
    def q(z): return (F(int(round(z.real))),F(int(round(z.imag))))
    for i,j,k,l in it.product(range(d),repeat=4):
        mr=F(0); mi=F(0)
        for alpha,va in coeff.items():
            minus=list(alpha); minus[k]+=1; minus[l]+=1
            for beta,vb in coeff.items():
                plus=list(beta); plus[i]+=1; plus[j]+=1
                if plus!=minus: continue
                moment=F(math.factorial(d-1)*math.prod(math.factorial(x) for x in plus),math.factorial(n+d+1))
                z=q(va*vb.conjugate())
                mr+=z[0]*moment;mi+=z[1]*moment
        # gamma uses ket indices first. Husimi <z^n,psi> hence v_alpha conj(v_beta)
        # and bar(z)^alpha z^beta; consistent ordered z_i z_j bar(z_k)bar(z_l).
        lhs=(mr*dimension*(n+d)*(n+d+1),mi*dimension*(n+d)*(n+d+1))
        sym=(g1[i,k]*(j==l)+g1[i,l]*(j==k)+g1[j,k]*(i==l)+g1[j,l]*(i==k))
        rhs=q(n*(n-1)*g2[i,j,k,l]+n*sym+norm*((i==k and j==l)+(i==l and j==k)))
        assert lhs==rhs,(n,i,j,k,l,lhs,rhs)
        checks+=1
# Literal occupation subsets: mixed bad clusters plus remote isolated pairs.
points=[(0,0,0),(2,0,0),(0,2,0),(0,0,2),(40,0,0),(42,0,0),(80,0,0),(81,1,0),(120,0,0),(121,-1,0),(0,50,0),(0,52,0)]
def graph(a,b):
    v=sorted(abs(a[i]-b[i]) for i in range(3))
    return v in ([0,0,2],[0,1,1])
def dist(a,b):return max(abs(a[i]-b[i]) for i in range(3))
def encode(s,R):
    pairs=tuple(sorted(tuple(sorted((a,b))) for a,b in it.combinations(s,2) if graph(a,b) and all(min(dist(x,a),dist(x,b))>R for x in s if x not in (a,b))))
    used={x for e in pairs for x in e}
    return pairs,tuple(sorted(set(s)-used))
enc_count=rem_count=env_count=0
for R in (14,17,20):
    seen=set()
    for mask in range(1<<len(points)):
        s=tuple(points[i] for i in range(len(points)) if mask>>i&1)
        pairs,env=encode(s,R);key=(pairs,env)
        assert key not in seen;seen.add(key)
        assert set(s)==set(env)|{x for e in pairs for x in e}
        if pairs and env:env_count+=1
        for e in pairs:
            reduced=tuple(x for x in s if x not in e)
            assert encode(reduced,R)==(tuple(x for x in pairs if x!=e),env)
            rem_count+=1
        enc_count+=1
# Guard energy counterexample from a union of endpoint neighborhoods,
# counting nearest-neighbor cuts directly with no cuboid-surface formula.
boundaries={}
for R in (2,5,14,20):
    forbidden=set()
    for center in ((0,0,0),(2,0,0),(-2,0,0)):
        for v in it.product(range(-R,R+1),repeat=3):
            forbidden.add(tuple(v[i]+center[i] for i in range(3)))
    count=0
    for x in forbidden:
        for j in range(3):
            for sign in (-1,1):
                y=list(x);y[j]+=sign
                count+=tuple(y) not in forbidden
    assert count==24*R*R+56*R+22
    boundaries[R]=count
result={'scope':'independent finite controls, not all-state proof','ordered_complex_Husimi_entries':checks,'physical_encodings':enc_count,'selected_removal_identities':rem_count,'mixed_selected_environment_inputs':env_count,'literal_guard_boundaries':boundaries,'cpu_seconds':time.process_time()-start,'wall_seconds':time.monotonic()-wall,'maxrss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
Path(__file__).with_name('RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
assert result['cpu_seconds']<30
assert result['maxrss_bytes']<150*1024**2
