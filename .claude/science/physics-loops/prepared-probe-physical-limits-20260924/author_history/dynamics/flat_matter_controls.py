"""Exact integer action of the original pair-form H4 at zero link angles.

This is a finite matter-fiber coefficient computation, not rotor propagation.
H4=-2 sum S_ac^* S_ac. Full hard-core signs, occupied B sites and all local
overlapping pairs are retained. Scalar far pairs are evaluated analytically.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from pathlib import Path
import hashlib,json,time


def control(side):
    vertices=list(product(range(side),repeat=3));index={v:i for i,v in enumerate(vertices)}
    bits=[1<<i for i in range(len(vertices))]
    A=[i for i,v in enumerate(vertices) if sum(v)%2==0]
    def near(i):
        v=vertices[i];out=[]
        for k in range(3):
            for s in (-1,1):
                w=list(v);w[k]=(w[k]+s)%side;out.append(index[tuple(w)])
        return out
    adj={i:near(i) for i in range(len(vertices))}
    mask=sum(bits[i] for i in A)
    def location(v):return index[tuple(x%side for x in v)]
    a,d,h,c,e,b=map(location,[(0,0,0),(1,1,0),(2,2,0),(1,0,0),(0,1,0),(-1,0,0)])
    fixed=list(map(location,[(0,-1,0),(0,0,1),(0,0,-1)]))
    minus=bits[d]|bits[h]
    common_plus=(mask^minus)|sum(bits[i] for i in fixed)
    initial=[(common_plus|bits[v],minus) for v in (c,e)]
    pairs=set()
    for x in A:
        for y in adj[x]:
            for z in adj[y]:
                if x<z:pairs.add((x,z))
    pairs=sorted(pairs)
    def hop(state,src,dst):
        p,n=state
        if not ((p|n)&bits[src]) or (p|n)&bits[dst]:return None
        if p&bits[src]:return p^bits[src]^bits[dst],n
        return p,n^bits[src]^bits[dst]
    def step(vector,src,dests,inward=False):
        out=defaultdict(int)
        for q,w in vector.items():
            for v in dests:
                r=hop(q,v,src) if inward else hop(q,src,v)
                if r is not None:out[r]+=w
        return dict(out)
    def pair_action(q,x,z):
        first=step({q:1},x,adj[x]);forward=step(first,z,adj[z])
        back=step(forward,z,adj[z],True);out=step(back,x,adj[x],True)
        assert out.get(q,0)==sum(w*w for w in forward.values())
        return out
    base_scalar=0
    for x,z in pairs:
        r=len(set(adj[x])&set(adj[z]));base_scalar-=2*(36+r*(r-2))
    actions=[];active_counts=[]
    for q in initial:
        result=defaultdict(int);active=0
        for x,z in pairs:
            neighborhood=set(adj[x])|set(adj[z])
            if not any((q[0]|q[1])&bits[v] for v in neighborhood) and not (q[1]&(bits[x]|bits[z])):
                r=len(set(adj[x])&set(adj[z]));result[q]+=-2*(36+r*(r-2))
            else:
                active+=1
                for f,value in pair_action(q,x,z).items():result[f]+=-2*value
        actions.append(dict(result));active_counts.append(active)
    assert actions[0].get(initial[1],0)==actions[1].get(initial[0],0)
    w=defaultdict(int)
    for sign,out in zip((1,-1),actions):
        for q,c0 in out.items():w[q]+=sign*c0
    w={q:c0 for q,c0 in w.items() if c0}
    mean=Fraction(w.get(initial[0],0)-w.get(initial[1],0),2)
    square=Fraction(sum(c0*c0 for c0 in w.values()),2)
    variance=square-mean*mean
    def mark(vector,sigma):
        moved=step(vector,a,adj[a]);out=defaultdict(int)
        for (p,n),value in moved.items():
            if (p|n)&(bits[a]|bits[b]):continue
            if sigma==1:r=(p|bits[a],n|bits[b])
            else:r=(p|bits[b],n|bits[a])
            out[r]+=value
        return {q:c0 for q,c0 in out.items() if c0}
    assert not mark({initial[0]:1,initial[1]:-1},1)
    leak={}
    for sigma in (-1,1):
        bw=mark(w,sigma)
        leak[str(sigma)]={'norm_squared':str(Fraction(sum(x*x for x in bw.values()),2)),
                          'output_words':len(bw)}
    shifted=dict(w)
    shifted[initial[0]]=shifted.get(initial[0],0)-base_scalar
    shifted[initial[1]]=shifted.get(initial[1],0)+base_scalar
    shifted={q:c0 for q,c0 in shifted.items() if c0}
    def describe(q):
        p,n=q
        return {'A_minus':[vertices[i] for i in A if n&bits[i]],
                'B_occupied':[[vertices[i],1 if p&bits[i] else -1]
                              for i in range(len(vertices)) if not mask&bits[i] and (p|n)&bits[i]]}
    certificate=[dict(describe(q),amplitude=c0) for q,c0 in sorted(shifted.items())]
    path=Path(__file__).with_name(f'FLAT_ACTION_SIDE_{side}.json')
    path.write_text(json.dumps(certificate,indent=2)+'\n')
    return {'side':side,'vertices':len(vertices),'overlap_pairs':len(pairs),
            'active_pair_counts':active_counts,'all_B_empty_flat_scalar':base_scalar,
            'mean_H4':str(mean),'mean_minus_background':str(mean-base_scalar),
            'variance_H4':str(variance),'selected_mark_leakage':leak,
            'shifted_action_words':len(shifted),'action_certificate_sha256':hashlib.sha256(path.read_bytes()).hexdigest()}


if __name__=='__main__':
    start=time.perf_counter()
    rows=[control(s) for s in (6,16)]
    print(json.dumps({'scope':__doc__,'rows':rows,'elapsed_seconds':time.perf_counter()-start},indent=2))
