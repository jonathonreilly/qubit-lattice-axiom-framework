"""Exact hopping-path reconstruction on actual side-six periodic cubic tori."""
from pathlib import Path
from itertools import product, combinations
from collections import Counter
from hashlib import sha256
from datetime import datetime, timezone
import json

HERE=Path(__file__).resolve().parent


def check(d,side,seed):
    vertices=list(product(range(side),repeat=d)); vi={x:i for i,x in enumerate(vertices)}
    volume=len(vertices); apart=[i for i,x in enumerate(vertices) if sum(x)%2==0]
    bpart=[i for i in range(volume) if i not in set(apart)]
    oc0=sum(1<<i for i in apart)
    def shift(x,a,sign=1): return tuple((x[k]+sign*(k==a))%side for k in range(d))
    neighbors=[[] for _ in vertices]
    for i,x in enumerate(vertices):
        for a in range(d):
            neighbors[i].append((vi[shift(x,a)],d*i+a,1))
            j=vi[shift(x,a,-1)]; neighbors[i].append((j,d*j+a,-1))
    bits=0
    for i,x in enumerate(vertices):
        for a in range(d):
            bit=1 if seed=='uniform' else int(sum(x[k] for k in range(d) if k!=a)%2==0)
            bits|=bit<<(d*i+a)
    def moves(state,sources):
        field,occupied=state
        for x in sources:
            if not (occupied>>x)&1: continue
            for y,e,direction in neighbors[x]:
                if (occupied>>y)&1: continue
                if ((field>>e)&1)!=(direction==1): continue
                yield field^(1<<e),occupied^(1<<x)^(1<<y)
    v1=Counter(moves((bits,oc0),apart))
    degree=d*volume//2
    assert sum(v1.values())==degree and all(z==1 for z in v1.values())
    v2=Counter()
    for state,weight in v1.items():
        for target in moves(state,apart):v2[target]+=weight
    assert all(z==2 for z in v2.values())
    v3=Counter()
    for state,weight in v2.items():
        for target in moves(state,bpart):v3[target]+=weight
    v4=Counter()
    for state,weight in v3.items():
        for field,occ in moves(state,bpart):
            assert occ==oc0;v4[field]+=weight
    expected={bits:degree*degree-degree*(2*d-1)}
    flippable=[]
    for i,x in enumerate(vertices):
        for a,b in combinations(range(d),2):
            raised=(d*i+a,d*vi[shift(x,a)]+b)
            lowered=(d*vi[shift(x,b)]+a,d*i+b)
            pattern=tuple((bits>>e)&1 for e in raised+lowered)
            if pattern in [(0,0,1,1),(1,1,0,0)]:
                out=bits
                for e in raised+lowered:out^=1<<e
                expected[out]=expected.get(out,0)+2
                flippable.append([i,a,b])
    assert all(weight%2==0 for weight in v4.values())
    excursion={field:weight//2 for field,weight in v4.items()}
    assert excursion==expected
    return {'d':d,'side':side,'volume':volume,'seed':seed,'initial_field_hex':hex(bits),
            'one_hop_count':degree,'two_hop_states':len(v2),'three_hop_states':len(v3),
            'four_hop_low_output_states':len(v4),'flippable_plaquettes':len(flippable),
            'second_order_constant':-degree,'fourth_order_unfolded_diagonal':-excursion[bits],
            'fourth_order_folded_diagonal':degree*degree,'fourth_order_total_diagonal':degree*(2*d-1),
            'every_ring_matrix_element':-2,'all_paths_and_low_outputs_exhaustively_checked_to_order_four':True,
            'complete_state_space_enumeration':False}


if __name__=='__main__':
    out={'created_utc':datetime.now(timezone.utc).isoformat(),'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
         'results':[check(2,6,'uniform'),check(2,6,'staggered'),check(3,6,'staggered')],
         'normalization':'Coefficients multiply t^2/Delta and t^4/Delta^3. The middle two-record-on-B denominator is 2 Delta; folded term is included.',
         'scope':'All order-four hopping paths from the chosen exact ice words on the actual period-six tori; the proof for arbitrary ice fields is separate.'}
    txt=json.dumps(out,indent=2)+'\n';(HERE/'FOURTH_ORDER_RESULTS.json').write_text(txt);print(txt,end='')
