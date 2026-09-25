"""Independent combinatorial formula versus primitive two-hop Gram certificate.

This uses destination eligibility and branch-overlap cases, never charge-word
hop propagation.  It also writes an exact plaquette/two-plaquette description
of every nonconstant defect character.
"""
from collections import defaultdict, Counter
from itertools import combinations
from pathlib import Path
from hashlib import sha256
import json
import time
import magnetic_increment_control as primitive


def clean(d): return {k:v for k,v in d.items() if v}
def negate(f): return tuple((e,-k) for e,k in f)
def canonical(f): return min(f,negate(f))


def formula(side):
    vertices,index,aa,neighbors,edges,eid,axes=primitive.graph(side)
    def v(x):return index[tuple(t%side for t in x)]
    a,d,h,c,e,v1,v2,v3=map(v,[(0,0,0),(1,1,0),(2,2,0),(1,0,0),
                                (0,1,0),(0,-1,0),(0,0,1),(0,0,-1)])
    q={x:(-1 if x in (d,h) else 1) for x in aa}
    nc={x:set(n) for x,n in neighbors.items()}
    pairs={(x,y) for x in aa for y in aa if x<y and nc[x]&nc[y]}
    occs=({c,v1,v2,v3},{e,v1,v2,v3})
    diag=defaultdict(int);cross=defaultdict(int)
    plaquettes={}
    central_paths=0
    for x,y in sorted(pairs):
        common=sorted(nc[x]&nc[y])
        # Empty diagonal minus prepared diagonal; two branches each have
        # coefficient -1, whereas the empty word has coefficient -2.
        diag[()]+=2*(36-len(common))
        for occ in occs:
            ex=nc[x]-occ;ey=nc[y]-occ
            diag[()]-=len(ex)*len(ey)-len(ex&ey)
        for s,t in combinations(common,2):
            f=()
            for edge,k in [((x,s),1),((y,s),-1),((y,t),1),((x,t),-1)]:
                f=primitive.add(f,eid[edge],k)
            plaquettes[canonical(f)]=[vertices[x],vertices[s],vertices[y],vertices[t]]
            # Missing same-branch exchange paths give +2 per blocked branch.
            coefficient=2
            for occ in occs:
                if q[x]==q[y] and s not in occ and t not in occ:coefficient-=1
            diag[f]+=coefficient;diag[negate(f)]+=coefficient
        # Cross-branch final B set is fixed: {c,e,t,v1,v2,v3}.
        for t in (nc[x]|nc[y])-set((c,e,v1,v2,v3)):
            def amplitudes(destination,string):
                terms=[]
                for source,other in ((x,y),(y,x)):
                    if q[source]==1 and destination in nc[source] and t in nc[other]:
                        f=((eid[d,string],-1),)
                        f=primitive.add(f,eid[source,destination],-1)
                        f=primitive.add(f,eid[other,t],-q[other])
                        terms.append((q[other],f,source))
                return terms
            left=amplitudes(e,c);right=amplitudes(c,e)
            for ql,fl,sl in left:
                for qr,fr,sr in right:
                    if ql==qr:
                        f=primitive.difference(fr,fl)
                        cross[f]+=1;cross[negate(f)]+=1
                        if sl==sr:central_paths+=1
    diag=clean(diag);cross=clean(cross)
    defect=defaultdict(int,diag)
    for f,k in cross.items():defect[f]+=k
    defect=clean(defect)
    ps=list(plaquettes)
    decomposition=[]
    for f,k in sorted(defect.items()):
        if not f or f!=canonical(f):continue
        if f in plaquettes:
            surface=[{"plaquette_flow":f,"sign":1}]
        else:
            surface=None
            for p in ps:
                for sign in (-1,1):
                    rem=f
                    for ed,power in p:rem=primitive.add(rem,ed,-sign*power)
                    if canonical(rem) in plaquettes:
                        surface=[{"plaquette_flow":p,"sign":sign},
                                 {"plaquette_flow":canonical(rem),"sign":1 if rem==canonical(rem) else -1}]
                        break
                if surface:break
            assert surface is not None
        recombined=()
        for term in surface:
            for ed,power in term['plaquette_flow']:
                recombined=primitive.add(recombined,ed,term['sign']*power)
        assert recombined==f
        decomposition.append({"flow":f,"cos_coefficient":2*k,"plaquette_surface":surface})
    exact_compare=None
    file=Path(__file__).parent/f'LAURENT_DATA_L{side}.json'
    if file.exists():
        data=json.loads(file.read_text())
        actual={tuple(map(tuple,r['flow'])):r['coefficient'] for r in data['haar_defect_polynomial']}
        assert defect==actual
        exact_compare=True
    summary={"side":side,"constant":defect[()],"flat_defect":sum(defect.values()),
             "cosine_count":len(decomposition),"cross_same_source_paths":central_paths,
             "cross_cosine_histogram":dict(Counter(2*k for f,k in cross.items() if f==canonical(f))),
             "diagonal_missing_cosine_histogram":dict(Counter(2*k for f,k in diag.items() if f and f==canonical(f))),
             "surface_weight_sum":sum(t['cos_coefficient']*len(t['plaquette_surface'])**2 for t in decomposition),
             "full_primitive_coefficientwise_comparison":exact_compare,
             "harmonic_signatures_all_zero":all(not any(primitive.signature(f,axes)) for f in defect)}
    assert summary['harmonic_signatures_all_zero']
    return summary,decomposition


def main():
    started=time.perf_counter();base=Path(__file__).parent;rows=[]
    for side in (6,8,10):
        summary,terms=formula(side)
        outfile=base/f'SURFACE_DECOMPOSITION_L{side}.json'
        outfile.write_text(json.dumps(terms,indent=2)+'\n')
        rows.append({**summary,'surface_certificate_sha256':sha256(outfile.read_bytes()).hexdigest()})
    print(json.dumps({'rows':rows,'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
                      'elapsed_seconds':time.perf_counter()-started},indent=2))


if __name__=='__main__':main()
