"""Exact integer action of the original pair-form H4 at zero link angles.

This reuses disclosed root23 pair-action machinery for new definite output words.
It is a finite matter-fiber coefficient computation, not rotor propagation.
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
    initial_before=[(common_plus|bits[v],minus) for v in (c,e)]
    # Actual selected output of the first branch: old plus at a hops to e,
    # then the original pair has sign sigma at a and -sigma at b.
    initial=[]
    for sigma in (-1,1):
        p,n=initial_before[0]
        p=(p^bits[a])|bits[e]
        if sigma==1:p|=bits[a];n|=bits[b]
        else:n|=bits[a];p|=bits[b]
        assert (p|n).bit_count()==len(A)+6 and p.bit_count()-n.bit_count()==len(A)
        initial.append((p,n))
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
    rows=[]
    for sigma,q,out,count in zip((-1,1),initial,actions,active_counts):
        mean=out.get(q,0);second=sum(v*v for v in out.values())
        rows.append({'sigma':sigma,'mean_H4':mean,'mean_minus_empty':mean-base_scalar,
                     'variance_H4':second-mean*mean,'nonzero_output_words':sum(v!=0 for v in out.values()),
                     'active_pair_count':count,'record_number':(q[0]|q[1]).bit_count()})
    return {'side':side,'vertices':len(vertices),'overlap_pairs':len(pairs),
            'all_B_empty_flat_scalar':base_scalar,'selected_output_matter_rows':rows}


if __name__=='__main__':
    start=time.perf_counter()
    rows=[control(s) for s in (16,)]
    print(json.dumps({'scope':__doc__,'rows':rows,'elapsed_seconds':time.perf_counter()-start},indent=2))
