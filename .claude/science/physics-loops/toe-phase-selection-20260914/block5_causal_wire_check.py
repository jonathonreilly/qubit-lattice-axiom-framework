#!/usr/bin/env python3
"""Vertex-disjoint periodic wires for a supplied bounded-degree type DAG.

The first geometry is an independently checked unit-point immersion. A scale
and local detours remove all foreign crossings. The final geometry is checked
by exact inclusive segment intersections, without expanding millions of copies.
No native law, rate or program selection is inferred from an embedding.
"""
from collections import Counter, defaultdict
from hashlib import sha256
from itertools import product
import json
from pathlib import Path

from block4_periodic_routing_check import Compiler, Edge, add


SCALE=10


def axis(a,b):
    axes=[i for i in range(3) if a[i]!=b[i]]
    assert len(axes)==1,(a,b)
    return axes[0]


def simplify(points):
    out=[]
    for p in points:
        if out and out[-1]==p:
            continue
        if len(out)>=2:
            i=axis(out[-2],out[-1])
            j=axis(out[-1],p)
            if i==j and (out[-1][i]-out[-2][i])*(p[i]-out[-1][i])>0:
                out[-1]=p
                continue
        out.append(p)
    return out


def quotient_segments(points,periods,wire):
    """Split lifted inclusive segments at periodic seams, retaining endpoint 0.

    A segment through coordinate L includes the quotient vertex zero, even
    if its final lifted endpoint is exactly L. Singleton seam pieces matter.
    """
    out=[]
    for a,b in zip(points,points[1:]):
        i=axis(a,b)
        lower,upper=sorted((a[i],b[i]))
        size=periods[i]
        fixed=tuple(a[j]%periods[j] for j in range(3))
        first=lower//size
        last=upper//size
        for slab in range(first,last+1):
            lo=max(lower,slab*size)-slab*size
            hi=min(upper,(slab+1)*size-1)-slab*size
            if lo<=hi:
                out.append((i,fixed,lo,hi,wire))
    return out


def intersection_check(segments,homes,endpoints,controls):
    """Exact integer segment comparisons, independent of route generation.

    Foreign wires may meet only at their common true gate endpoint. The
    generator separately proves/tests simplicity of each lifted wire; this
    check also rejects any positive-length self-overlap.
    """
    buckets=defaultdict(list)
    counts=Counter()
    def permit(a,b,p,overlap_length=0):
        if overlap_length:
            raise AssertionError(('positive segment overlap',a,b,p,overlap_length))
        if a[4]==b[4]:
            # Turning vertices occur in two consecutive segments of a wire.
            # A later independent per-wire point/segment test controls repeats.
            counts['same_wire_turn']+=1
            return
        assert p in homes and p in endpoints[a[4]] and p in endpoints[b[4]],('foreign wire collision',a,b,p)
        counts['shared_gate']+=1
    for seg in segments:
        i,f,lo,hi,_=seg
        key=(i,tuple(f[j] for j in range(3) if j!=i))
        buckets[key].append(seg)
    for group in buckets.values():
        group.sort(key=lambda z:z[2])
        active=[]
        for b in group:
            active=[a for a in active if a[3]>=b[2]]
            for a in active:
                lower=max(a[2],b[2]);upper=min(a[3],b[3])
                p=list(a[1]);p[a[0]]=lower
                permit(a,b,tuple(p),upper-lower)
            active.append(b)
    for i,j in ((0,1),(0,2),(1,2)):
        k=3-i-j
        left=defaultdict(list);right=defaultdict(list)
        for seg in segments:
            if seg[0]==i:
                left[seg[1][k]].append(seg)
            elif seg[0]==j:
                right[seg[1][k]].append(seg)
        for level,aa in left.items():
            for a in aa:
                for b in right.get(level,()):
                    if a[2]<=b[1][i]<=a[3] and b[2]<=a[1][j]<=b[3]:
                        p=list(a[1]);p[i]=b[1][i]
                        permit(a,b,tuple(p))
    # Controls are not wire vertices or homes. Point query uses the same
    # exact interval representation, not a sampled distance test.
    for p in controls:
        assert p not in homes
        for i in range(3):
            key=(i,tuple(p[j] for j in range(3) if j!=i))
            assert all(not lo<=p[i]<=hi for _,_,lo,hi,_ in buckets.get(key,())),('control collision',p)
    return dict(counts)


def run_case(name,edges,stages,cover_multiplier=(1,1,1),expected_registry=None):
    compiler=Compiler([1]*len(stages),edges)
    # At most four horizontal ports; distinct first directions remove the
    # two-lanes-per-direction shared terminal in the scalar immersion.
    assert max(compiler.ports.values())<=3
    compiler.ports={key:2*p for key,p in compiler.ports.items()}
    for e in edges:
        assert stages[e.left]<stages[e.right]
    p=compiler.period
    cover=tuple(p*a for a in cover_multiplier)
    periods=tuple(SCALE*compiler.side*a for a in cover)
    homes={compiler.quotient(compiler.home(n,h),cover)
           for n in product(*(range(a) for a in cover)) for h in range(len(stages))}
    paths=[]
    occupancy=defaultdict(list)
    for n in product(*(range(a) for a in cover)):
        for e in range(len(edges)):
            lifted=compiler.route(n,e)
            quotient=[compiler.quotient(x,cover) for x in lifted]
            assert len(set(quotient))==len(quotient)
            wire=len(paths)
            paths.append((n,e,lifted,quotient))
            for j,x in enumerate(quotient[1:-1],1):
                assert x not in homes
                occupancy[x].append((wire,j))
    detours=defaultdict(set)
    crossing_types=Counter()
    for point,entries in occupancy.items():
        assert len(entries)<=2
        if len(entries)==1:
            continue
        vertical=[]
        for wire,j in entries:
            path=paths[wire][2]
            axes=(axis(path[j-1],path[j]),axis(path[j],path[j+1]))
            if axes==(2,2):
                assert path[j+1][2]-path[j][2]==path[j][2]-path[j-1][2]
                vertical.append((wire,j))
            else:
                assert 2 not in axes,('crossing is not horizontal/vertical',point,entries,axes)
                crossing_types[str(axes)]+=1
        assert len(vertical)==1,('crossing lacks a unique vertical strand',point,entries)
        detours[vertical[0][0]].add(vertical[0][1])
    scaled_homes={tuple(SCALE*x for x in h) for h in homes}
    controls={tuple((x-(1 if i==2 else 0))%periods[i] for i,x in enumerate(h)) for h in scaled_homes}
    endpoints={}
    segments=[]
    lengths=[]
    digest=sha256()
    final_routes=[]
    registry={}
    for wire,(n,e,path,quotient) in enumerate(paths):
        points=[]
        for j,x in enumerate(path):
            center=tuple(SCALE*a for a in x)
            if j not in detours[wire]:
                points.append(center)
                continue
            dz=path[j+1][2]-x[2]
            before=add(center,(0,0,-2*dz));after=add(center,(0,0,2*dz))
            points.extend((before,add(before,(1,0,0)),add(before,(1,1,0)),
                           add(after,(1,1,0)),add(after,(1,0,0)),after))
        points=simplify(points)
        key=(e,compiler.color(n))
        relative=tuple(tuple(x-SCALE*compiler.side*n[i] for i,x in enumerate(v)) for v in points)
        if key in registry:
            assert registry[key]==relative,'A repeated coarse color changes the detour pattern'
        registry[key]=relative
        if expected_registry is not None:
            assert expected_registry[key]==relative,'A larger cover changes the causal local role map'
        length=sum(abs(a[axis(a,b)]-b[axis(a,b)]) for a,b in zip(points,points[1:]))
        assert length==SCALE*(len(path)-1)+4*len(detours[wire])
        lengths.append(length)
        ep={tuple(x%periods[i] for i,x in enumerate(points[0])),
            tuple(x%periods[i] for i,x in enumerate(points[-1]))}
        assert len(ep)==2 and ep<=scaled_homes
        endpoints[wire]=ep
        own_segments=quotient_segments(points,periods,wire)
        # A per-wire multiplicity count of all inclusive segment intersections
        # equals the number of turn vertices. A periodic seam split adds no
        # duplicated zero/L vertex, because integer slabs use L-1 then zero.
        own_turns=0
        for a_i,a in enumerate(own_segments):
            for b in own_segments[a_i+1:]:
                if a[0]==b[0]:
                    other=[j for j in range(3) if j!=a[0]]
                    if all(a[1][j]==b[1][j] for j in other):
                        lo=max(a[2],b[2]);hi=min(a[3],b[3])
                        assert lo>hi,('self collinear overlap',wire,a,b)
                else:
                    i,j=a[0],b[0];k=3-i-j
                    if a[1][k]==b[1][k] and a[2]<=b[1][i]<=a[3] and b[2]<=a[1][j]<=b[3]:
                        own_turns+=1
        assert own_turns==len(points)-2,('nonconsecutive self intersection',wire,own_turns,len(points)-2)
        segments.extend(own_segments)
        final_routes.append(points)
        digest.update(repr((n,e,points)).encode())
    checked=intersection_check(segments,scaled_homes,endpoints,controls)
    # Assign strict causal levels to every gate and internal unit vertex.
    # These rational levels need not be encoded as floating point or clocks.
    for wire,(n,e,path,quotient) in enumerate(paths):
        assert stages[edges[e].right]-stages[edges[e].left]>=1
        # Level along edge j is s_left+(s_right-s_left)j/length.
        assert lengths[wire]>0
    result=dict(name=name,coarse_cover=cover,coarse_period=p,coarse_side=compiler.side,
                final_physical_periods=periods,wires=len(paths),gate_sites=len(scaled_homes),
                controls=len(controls),crossings_removed=sum(map(len,detours.values())),
                original_crossing_types=dict(crossing_types),
                maximum_original_internal_load=max(map(len,occupancy.values())),
                final_interval_pieces=len(segments),maximum_path_edges=max(lengths),
                hidden_copy_sites=sum(length-1 for length in lengths),
                exact_final_intersection_counts=checked,vertex_disjoint_foreign_wires=True,
                coordinate_sha256=digest.hexdigest(),
                cover_independent_role_map=(expected_registry is not None),
                scope='Supplied periodic type DAG, one complex payload per gate/copy, controls supplied; no autonomous program or state selection')
    print(json.dumps(result,indent=2),flush=True)
    return result,registry


def main():
    standard=[Edge(0,0,2,0,(1,0,0)),Edge(1,0,2,0,(0,1,0)),Edge(2,0,3,0,(0,0,1))]
    negative=[Edge(0,0,2,0,(-1,0,-1)),Edge(1,0,2,0,(0,-1,0)),Edge(2,0,3,0,(1,1,1))]
    base,registry=run_case('three-axis sum DAG',standard,[0,0,1,2])
    negative_row,_=run_case('negative-displacement DAG',negative,[0,0,1,2])
    doubled,_=run_case('doubled first axis',standard,[0,0,1,2],(2,1,1),registry)
    rows=[base,negative_row,doubled]
    Path(__file__).with_name('BLOCK5_CAUSAL_WIRE_CHECK.json').write_text(json.dumps(rows,indent=2)+'\n')


if __name__=='__main__':
    main()
