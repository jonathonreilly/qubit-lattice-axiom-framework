"""Independent literal dictionary paths and support controls; no author imports."""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from pathlib import Path
import json, resource, time

started = time.monotonic()
out = Path(__file__).resolve().parent
steps = [tuple(s if j == i else 0 for j in range(3)) for i in range(3) for s in (-1, 1)]
origin = (0, 0, 0)
other = (1, 1, 0)
def add(x, y): return tuple(a+b for a,b in zip(x,y))
def dist(x, y=origin): return sum(abs(a-b) for a,b in zip(x,y))
def neighbors(x): return {add(x,s) for s in steps}
def pack(charges, fields):
    return (tuple(sorted((x,q) for x,q in charges.items() if q)),
            tuple(sorted((e,k) for e,k in fields.items() if k)))
def hop_one(word, a, backward=False):
    charges, fields = map(dict, word)
    if bool(charges.get(a,0)) == backward: return []
    result = []
    for b in neighbors(a):
        if bool(charges.get(b,0)) != backward: continue
        q = charges[b] if backward else charges[a]
        c, e = charges.copy(), fields.copy()
        c[a], c[b] = (q,0) if backward else (0,q)
        e[(a,b)] = e.get((a,b),0) + (q if backward else -q)
        result.append(pack(c,e))
    return result
def linear(words, operation):
    result = defaultdict(int)
    for word, coefficient in words.items():
        for target, multiplier in operation(word): result[target] += coefficient*multiplier
    return {w:c for w,c in result.items() if c}
def hop(words, a, backward=False):
    return linear(words, lambda w: [(v,1) for v in hop_one(w,a,backward)])
def magnetic(words):
    # Direct S^* S, with the order reversed from the author's commuting F order.
    for a, back in [(other,False),(origin,False),(origin,True),(other,True)]:
        words=hop(words,a,back)
    return {w:-2*c for w,c in words.items()}
mark_edge=(1,0,0)
def creation(w, sign):
    charges, fields = map(dict,w)
    if charges.get(origin,0) or charges.get(mark_edge,0): return []
    charges[origin],charges[mark_edge]=sign,-sign
    fields[(origin,mark_edge)]=fields.get((origin,mark_edge),0)+sign
    return [(pack(charges,fields),1)]
def mark(words, sign):
    return linear(hop(words,origin),lambda w:creation(w,sign))
def difference(a,b):
    return {w:a.get(w,0)-b.get(w,0) for w in a.keys()|b.keys() if a.get(w,0)!=b.get(w,0)}
def electric(word):
    charges,fields=map(dict,word)
    return sum(k*(k-charges.get(a,0)) for (a,b),k in fields.items() if not charges.get(b,0))
def omega(n=0):
    b,d=(1,0,0),(0,1,0)
    return pack({origin:1,other:1},{(origin,b):n,(other,b):-n,(other,d):n,(origin,d):-n})

vac=omega()
v=magnetic({vac:1})
assert sorted(v.values())==[-68,-2,-2]
comm=[]
vectors=[]
for sign in (-1,1):
    w=difference(magnetic(mark({vac:1},sign)),mark(magnetic({vac:1}),sign))
    vectors.append(w)
    comm.append([sign,len(w),sum(c*c for c in w.values())])
assert comm==[[-1,140,16984],[1,75,10808]]
coh={w:sum(v.get(w,0) for v in vectors) for w in vectors[0].keys()|vectors[1].keys()}
assert len(coh)==215 and sum(c*c for c in coh.values())==27792
electric_controls=[]
for n in (-7,-1,0,2,11):
    w=omega(n); image=magnetic({w:1})
    norm2=sum(((electric(u)-electric(w))*c)**2 for u,c in image.items())
    assert electric(w)==4*n*n and norm2==512*n*n+128
    electric_controls.append([n,norm2])

# Enumerate endpoints by distances, not the author's displacement set.
even4={x for x in product(range(-4,5),repeat=3) if dist(x)<=4 and sum(x)%2==0}
even10={x for x in product(range(-10,11),repeat=3) if dist(x)<=10 and sum(x)%2==0}
pair_steps={x for x in product(range(-2,3),repeat=3) if dist(x)==2}
kept={frozenset((a,add(a,d))) for a in even4 for d in pair_steps}
S=neighbors(origin)|{origin}
for pair in kept:
    for a in pair: S.update({a}|neighbors(a))
gate=S.copy()
for x in S: gate.update(neighbors(x))
candidate_pairs={frozenset((a,add(a,d))) for a in even10 for d in pair_steps}
boundary=set()
bare=neighbors(origin)|{origin}
for pair in candidate_pairs-kept:
    support=set(pair)
    for a in pair: support.update(neighbors(a))
    if support & gate:
        boundary.add(pair)
        assert not support & bare
assert (len(even4),len(kept),len(gate),len(boundary))==(85,1038,833,4284)
assert max(dist(x) for x in gate)==8

# Every omitted electric edge is disjoint from S, but it may meet gate.
# It can then touch only diagonal h_loc terms, and commutes with the bare U.
omitted_touching_gate=0
for a in even10:
    for b in neighbors(a):
        if not ({a,b}&S) and ({a,b}&gate):
            omitted_touching_gate+=1
            assert not ({a,b}&bare)
assert omitted_touching_gate>0

# Exact incidence bounds before/after the product field compression.
f_bounds=[(6-o)*(o+1) for o in range(7)]
b_bounds=[(5-o)*(o+1) for o in range(6)]
gamma_bounds=[2*(5-o)*(6-o)*(o+1) for o in range(6)]
assert max(f_bounds)==12 and max(b_bounds)==9 and max(gamma_bounds)==80
assert 90*(4*9**2+2)*288==8449920

# A two-link boundary fixture distinguishes product projection from radial
# projection and keeps the loss as the square of the compressed original jump.
R=2
box={(x,y) for x in range(-R,R+1) for y in range(-R,R+1)}
radial={w for w in box if sum(map(abs,w))<=R}
assert (R,R) in box-radial
def shift(w):return w[0]+1,w[1]-1
for w in box:
    full_loss=1
    actual_loss=int(shift(w) in box)
    if w==(R,0): assert full_loss!=actual_loss
for n in range(3):
    w=(0,0)
    for j in range(n):
        w=shift(w)
        if 2*n<=R: assert w in radial and w in box

result={'commutator_words':comm,'coherent_norm_squared':sum(c*c for c in coh.values()),
        'electric_controls':electric_controls,'geometry':[len(even4),len(kept),len(gate),len(boundary)],
        'omitted_electric_edges_touching_gate':omitted_touching_gate,
        'center_loss_bounds':gamma_bounds,'box_boundary_loss_mutation_detected':True,
        'runtime_seconds':time.monotonic()-started,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        'scope':'Exact finite source-word and geometry controls; analytic proof carries all-volume and process statements.'}
(out/'results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
