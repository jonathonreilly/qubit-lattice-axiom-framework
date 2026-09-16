#!/usr/bin/env python3
"""Integer chain identities for the local filling used by the curl estimate.

No matrix determinant or continuum approximation enters these exact integer
checks. Random examples challenge orientations and support, not the general
chain-homotopy proof. Floating phases additionally test physical time units.
"""
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_FILES=[]
import collections,hashlib,itertools,json,math,time
from pathlib import Path
import numpy as np

def add(d,key,value):
    d[key]+=value
    if d[key]==0:del d[key]

def moved(x,a,n=1):
    y=list(x);y[a]+=n;return tuple(y)

def edge(a,x,sign=1):
    return (a,x) if sign>0 else (a,moved(x,a,-1))

def boundary(fill):
    out=collections.Counter()
    for (a,b,x),n in fill.items():
        for e,s in [((a,x),1),((b,moved(x,a)),1),((a,moved(x,b)),-1),((b,x),-1)]:add(out,e,n*s)
    return out

def fill_cycle(chain,root,order=(0,1,2,3)):
    current=chain.copy();fill=collections.Counter()
    for a in order:
        projected=collections.Counter()
        for (b,x),n in current.items():
            if a==b:continue
            lo=min(x[a],root[a]);hi=max(x[a],root[a]);direction=1 if x[a]>root[a] else -1
            orientation=1 if a<b else -1
            for z in range(lo,hi):
                u=list(x);u[a]=z
                add(fill,(min(a,b),max(a,b),tuple(u)),n*direction*orientation)
            y=list(x);y[a]=root[a];add(projected,(b,tuple(y)),n)
        current=projected
    assert not current
    return fill

def translate_edges(chain,shift):
    return collections.Counter({(a,tuple(xi+si for xi,si in zip(x,shift))):n for (a,x),n in chain.items()})

def translate_fill(fill,shift):
    return collections.Counter({(a,b,tuple(xi+si for xi,si in zip(x,shift))):n for (a,b,x),n in fill.items()})

def run():
    start=time.time();rng=np.random.default_rng(126734);rows=[]
    for trial in range(120):
        pairs=int(rng.integers(2,26));axes=rng.integers(0,4,size=pairs)
        steps=[(int(a),s) for a in axes for s in [1,-1]];rng.shuffle(steps)
        root=tuple(int(n) for n in rng.integers(-3,4,size=4));x=root;vertices=[x];chain=collections.Counter()
        ell=0;temporal=0
        for a,s in steps:
            add(chain,edge(a,x,s),s);x=moved(x,a,s);vertices.append(x)
            if a==0:temporal+=1
            else:ell+=1
        assert x==root
        fill=fill_cycle(chain,root)
        assert boundary(fill)==chain,(trial,'integer boundary mismatch')
        lower=np.min(vertices,axis=0);upper=np.max(vertices,axis=0)
        for a,b,u in fill:
            for v in [u,moved(u,a),moved(u,b),moved(moved(u,a),b)]:
                assert np.all(lower<=v) and np.all(np.array(v)<=upper),(trial,'fill left visited coordinate box')
        shift=(7,-4,3,-9)
        assert fill_cycle(translate_edges(chain,shift),tuple(x+s for x,s in zip(root,shift)))==translate_fill(fill,shift)
        spatial=sum(abs(n) for (a,b,x),n in fill.items() if a!=0)
        temp=sum(abs(n) for (a,b,x),n in fill.items() if a==0)
        assert spatial<=3*ell**2 and temp<=ell*temporal
        # With ascending contraction axes, every surviving edge has b>a;
        # replacing the orientation factor by+1 is then an equivalent
        # implementation, not a detected scientific error. Other permitted
        # spatial orders actually exercise the a>b orientation branch.
        for perm in itertools.permutations([1,2,3]):
            alternative=fill_cycle(chain,root,(0,)+perm)
            assert boundary(alternative)==chain,(trial,perm,'alternative-order integer boundary mismatch')
            asp=sum(abs(n) for (a,b,x),n in alternative.items() if a!=0)
            atmp=sum(abs(n) for (a,b,x),n in alternative.items() if a==0)
            assert asp<=3*ell**2 and atmp<=ell*temporal
        # Assign angles on every boundary edge of the fill, including edges
        # which cancel in the final loop; form each curl independently.
        all_edges=set(chain)
        for a,b,u in fill:
            all_edges.update([(a,u),(b,moved(u,a)),(a,moved(u,b)),(b,u)])
        angles={e:float(rng.normal()) for e in sorted(all_edges)}
        phase=sum(n*angles[e] for e,n in chain.items());phase_errors=[]
        images={p:int(rng.integers(-4,5)) for p in fill}
        for delta in [.1,.02,.003]:
            filled=0.;imaged=0.
            for (a,b,u),n in fill.items():
                curl=angles[a,u]+angles[b,moved(u,a)]-angles[a,moved(u,b)]-angles[b,u]
                time_factor=delta if a==0 else 1.
                physical=curl;filled+=n*time_factor*physical
                imaged+=n*time_factor*(physical+2*math.pi*images[a,b,u]/time_factor)
            assert abs(filled-phase)<2e-12
            assert abs(np.exp(1j*imaged)-np.exp(1j*phase))<2e-11
            assert spatial+delta*temp<=3*ell**2+ell*(delta*temporal)
            phase_errors.append(abs(filled-phase))
        rows.append({'trial':trial,'walk_steps':2*pairs,'spatial_steps':ell,'temporal_steps':temporal,'surviving_integer_edges':len(chain),'fill_plaquettes':len(fill),'spatial_fill_l1':spatial,'temporal_fill_l1':temp,'largest_phase_error':max(phase_errors)})
    print(json.dumps({'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'spatial_contraction_orders_per_cycle':6,'integer_cycles':rows,'seconds':time.time()-start},indent=2))

if __name__=='__main__':run()
