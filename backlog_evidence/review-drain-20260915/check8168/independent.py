from fractions import Fraction as Q
from itertools import product
from random import Random
from collections import deque
import json,hashlib,pathlib
# Independent menu encoding: antipodes differ in the low bit; axes are integer pairs.
def probabilities(triple,p,q,r):
    weights=[]
    for v in range(6):
        w=1
        for z in triple:w*=p if v==z else q if v//2==z//2 else r
        weights.append(w)
    return [Q(w,sum(weights)) for w in weights]
triples=[z for z in product(range(6),repeat=3) if z.count(0)>=2]
assert len(triples)==16 # 216 candidates, only 16 meet the majority condition
thresholds=[]
for q,r,p0 in [(1,2,285718),(1,1,142861),(2,4,571436),(1,3,428576)]:
    values=[max(1-probabilities(z,p,q,r)[0] for z in triples) for p in [p0-1,p0]]
    assert values[0]>Q(7,10**6)>=values[1]
    thresholds.append({'q':q,'r':r,'p0':p0,'epsilon_predecessor':str(values[0]),'epsilon_at':str(values[1])})
# Direct occupancy-slot sum, independently generates certificate products without recurrence helper.
t=Q(91,1000);s=Q(1000,107653)
cert={'D':Q(3290957526219,10**12),'U':Q(514547476033,25*10**10),'F':Q(943741493637,25*10**10)}
def slots(arrival):
    types=['D']*3+['U']*3+['F']*6
    if arrival:types.remove({'D':'U','U':'D','F':'F'}[arrival])
    total=Q(0)
    for occupied in product((0,1),repeat=len(types)):
        if sum(on for ty,on in zip(types,occupied) if ty=='D')+(arrival=='U')>1:continue
        weight=Q(1)
        for ty,on in zip(types,occupied):
            if on:weight*=cert[ty]*(s if ty=='F' else t)
        total+=weight
    return total
slacks={k:cert[k]-slots(k) for k in cert};R=slots(None)
assert all(v>0 for v in slacks.values()) and R<Q(391,100) and t**3*s==Q(7,10**6)
# Independent spanning identity on arbitrary finite cluster trees. Unique point labels allow
# several edges to meet at one point. Charge assignments are arbitrary triples summing to zero.
rng=Random(8168);tested=0
for trial in range(800):
    n=rng.randrange(1,16);edges=[(v,rng.randrange(v)) for v in range(1,n)]
    adj={i:[] for i in range(n)}
    for u,v in edges:adj[u].append(v);adj[v].append(u)
    terms=[rng.randrange(n) for _ in range(3)]
    keep=set(range(n))
    while True:
        leaves={v for v in keep if sum(w in keep for w in adj[v])<=1 and v not in terms}
        if not leaves:break
        keep-=leaves
    pts={v:[(v,j) for j in range(3)] for v in keep}
    meet={}
    for u,v in edges:
        if u in keep and v in keep:meet[u,v]=rng.choice(pts[u]);meet[v,u]=rng.choice(pts[v])
    poles=[rng.choice(pts[v]) for v in terms]
    charges={}
    for v in keep:
        for pt in pts[v]:
            a,b=rng.randrange(-9,10),rng.randrange(-9,10);charges[pt]=(a,b,-a-b)
    # Each terminal-rooted orientation gives all pole assignments by walking toward that terminal.
    total=0
    assigned={v:[] for v in keep}
    for k,target in enumerate(terms):
        parent={target:None};todo=[target]
        for v in todo:
            for w in adj[v]:
                if w in keep and w not in parent:parent[w]=v;todo.append(w)
        for v in keep:
            pt=poles[k] if v==target else meet[v,parent[v]]
            assigned[v].append(pt);total+=charges[pt][k]
        for u,v in edges:
            if u not in keep or v not in keep:continue
            # fork pole chooses the endpoint on the terminal side of that edge
            a,b=(u,v) if parent[u]==v else (v,u)
            total+=charges[meet[b,a]][k]
    assert total==sum(charges[poles[k]][k] for k in range(3))
    for v in keep:
        required={poles[k] for k in range(3) if terms[k]==v}|{meet[v,w] for w in adj[v] if w in keep}
        assert required<=set(assigned[v])
    tested+=1
# Independent exact exhaustive finite-cone law, no explainer used.
pts=[(i,j,k) for i in range(3) for j in range(3-i) for k in range(3-i-j)]
by_weight=[0]*11
for bits in product((0,1),repeat=10):
    noise=dict(zip(pts,bits));state={}
    for z in sorted(pts,key=sum,reverse=True):
        parents=[tuple(z[j]+(j==i) for j in range(3)) for i in range(3)]
        state[z]=noise[z] or sum(state.get(w,0) for w in parents)>=2
    if state[(0,0,0)]:by_weight[sum(bits)]+=1
assert sum(by_weight)==932
for eps in [Q(0),Q(1,10**8),Q(7,10**6)]:
    density=sum(c*eps**k*(1-eps)**(10-k) for k,c in enumerate(by_weight))
    assert density<=Q(391,100)*eps
out={'status':'PASS','kernel_majority_triples':len(triples),'thresholds':thresholds,'slot_certificate_slacks':{k:str(v) for k,v in slacks.items()},'root_weight':str(R),'spanning_instances':tested,'finite_cone_success_by_noise_count':by_weight,'scope':'Independent finite controls and exact certificate, not full primary run or infinite-volume computational proof.'}
print(json.dumps(out,indent=2))
