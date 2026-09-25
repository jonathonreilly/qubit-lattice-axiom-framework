"""Exact electric quadratic-form checks and coefficient-count accounting."""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction
from itertools import combinations
import json
import magnetic_increment_control as p


def control(side):
    base=Path(__file__).parent;file=base/f'LAURENT_DATA_L{side}.json'
    data=json.loads(file.read_text())
    vertices,index,aa,n,edges,eid,axes=p.graph(side);aa=set(aa)
    def v(x):return index[tuple(t%side for t in x)]
    a,d,h,c,e,v1,v2,v3=map(v,[(0,0,0),(1,1,0),(2,2,0),(1,0,0),
                                (0,1,0),(0,-1,0),(0,0,1),(0,0,-1)])
    qbase=[int(i in aa) for i in range(len(vertices))]
    qbase[d]=qbase[h]=-1;qbase[v1]=qbase[v2]=qbase[v3]=1
    words=[]
    for dest in (c,e):word=qbase.copy();word[dest]=1;words.append(word)
    pairs=[(x,y) for x,y in combinations(sorted(aa),2) if set(n[x])&set(n[y])]
    pairset=set(pairs);b_neighbors={bv:{av for av,bb in edges if bb==bv} for bv in (c,e,v1,v2,v3)}
    scalar_rows=[]
    for occ in ({c,v1,v2,v3},{e,v1,v2,v3}):
        m={x:len(set(n[x])&occ) for x in aa}
        linear_count=sum(6*(m[x]+m[y]) for x,y in pairs)
        product_count=sum(m[x]*m[y] for x,y in pairs)
        common_count=sum(len(set(n[x])&set(n[y])&occ) for x,y in pairs)
        pair_counts=[]
        for u,vv in combinations(sorted(occ),2):
            count=sum(x!=y and tuple(sorted((x,y))) in pairset
                      for x in b_neighbors[u] for y in b_neighbors[vv])
            pair_counts.append({'B_pair':[vertices[u],vertices[vv]],'ordered_A_neighbor_overlap_count':count})
        assert product_count==60+sum(row['ordered_A_neighbor_overlap_count'] for row in pair_counts)
        scalar_rows.append({'sum_6_mx_plus_my':linear_count,'sum_mx_my':product_count,
                            'sum_occupied_common_neighbors':common_count,
                            'constant_defect':linear_count-product_count-common_count,
                            'occupied_B_pair_counts':pair_counts})
    assert sum(r['constant_defect'] for r in scalar_rows)==data['summary']['defect_constant']
    w=[Fraction(*q) for q in data['electric_mask']]
    ell=[Fraction(*q) for q in data['electric_linear']]
    const=Fraction(*data['electric_constant'])
    fields=[{}]
    terms=data['defect_cosines']
    for sample in (1,2,3):
        f=()
        for i,t in enumerate(terms):
            coefficient=((i+2)*sample)%5-2
            for ed,k in t['flow']:f=p.add(f,ed,coefficient*k)
        fields.append(dict(f))
    rows=[]
    for field in fields:
        assert not any(p.divergence(tuple(field.items()),edges,len(vertices)))
        direct=[]
        for word,branch in zip(words,data['electric_branches']):
            shift=dict(branch['flow']);value=0
            for ed,(av,bv) in enumerate(edges):
                if word[bv]==0:
                    ee=field.get(ed,0)+shift.get(ed,0)
                    value+=ee*(ee-word[av])
            assert value>=0;direct.append(value)
        target=Fraction(sum(direct),2)
        quadratic=sum(w[i]*field.get(i,0)**2+ell[i]*field.get(i,0) for i in range(len(edges)))+const
        assert target==quadratic
        rows.append({'reference_field_nonzero_edges':len(field),'direct_branch_D_values':direct,
                     'averaged_D':[target.numerator,target.denominator],
                     'quadratic_form_exact_equal':True})
    # Exact central plaquette's own four links carry missing electric weight
    # 1/2, because its B vertices c,e are each occupied in one branch.
    central=next(t for t in terms if t['cos_coefficient']==170)
    assert all(w[ed]==Fraction(1,2) for ed,k in central['flow'])
    return {'side':side,'constant_count_rows':scalar_rows,'electric_rows':rows,
            'central_plaquette_electric_mask_exact':[1,2],
            'input_data_sha256':sha256(file.read_bytes()).hexdigest()}


if __name__=='__main__':
    print(json.dumps({'rows':[control(6),control(8)],
                     'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest()},indent=2))
