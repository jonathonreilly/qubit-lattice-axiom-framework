#!/usr/bin/env python3
"""Exact local cut factorization of all 1D physical field words."""
from collections import Counter,defaultdict
from pathlib import Path
import hashlib,json,time

import one_dimensional_record_field_transport_check as transport

OUT=Path(__file__).resolve().parent

def fib(n):
    a,b=0,1
    for _ in range(n):a,b=b,a+b
    return a

def check(length):
    m=length//2;groups=defaultdict(list)
    for word in range(1<<length):
        q=transport.matter(word,length)
        if all(v in (0,1,-1) for v in q):
            groups[tuple(x for x,v in enumerate(q) if v==-1)].append((word,q))
    assert sum(map(len,groups.values()))==3**m
    rows=[];hist=Counter();hops_checked=0
    for anchors,states in groups.items():
        if not anchors:
            assert len(states)==fib(length-1)+fib(length+1)
            continue
        intervals=[];gaps=[];ones=set();zeros=set()
        for i,a in enumerate(anchors):
            b=anchors[(i+1)%len(anchors)]
            gap=((b-a)%length)//2 if len(anchors)>1 else m
            assert gap>=2;gaps.append(gap)
            intervals.append([(a+j)%length for j in range(2,2*gap-2)])
            ones.update(((a-1)%length,a));zeros.update(((a-2)%length,(a+1)%length))
        assert not ones&zeros
        free=set().union(*map(set,intervals))
        assert len(free)+len(ones)+len(zeros)==length
        dimension=1
        for gap in gaps:dimension*=fib(2*gap-2)
        assert len(states)==dimension
        hist[(len(anchors),tuple(sorted(gaps)),dimension)]+=1
        for word,q in states:
            eta=[((word>>e)&1) if e%2==0 else 1-((word>>e)&1) for e in range(length)]
            assert all(eta[e]==1 for e in ones) and all(eta[e]==0 for e in zeros)
            assert all(not (eta[a] and eta[b]) for seq in intervals for a,b in zip(seq,seq[1:]))
            nb=sum(q[x]!=0 for x in range(1,length,2))
            assert nb==m-sum(eta[e] for e in free)
            actual=set()
            for e in range(length):
                x,y=e,(e+1)%length;bit=(word>>e)&1
                if (q[x]==1 and q[y]==0 and bit==1) or (q[x]==0 and q[y]==1 and bit==0):actual.add(e)
            predicted={e for e in free if eta[(e-1)%length]==eta[(e+1)%length]==0}
            assert actual==predicted;hops_checked+=len(actual)
        if len(rows)<6:
            rows.append({'minus_positions':anchors,'B_site_gaps':gaps,
                         'open_PXP_block_lengths':[len(seq) for seq in intervals],
                         'tensor_product_dimension':dimension})
    return {'length':length,'physical_dimension':3**m,'minus_pattern_sectors':len(groups),
            'nonempty_minus_pattern_sectors':len(groups)-1,'all_exact_factorizations':True,
            'directed_hops_in_cut_sectors_checked':hops_checked,'examples':rows,
            'sector_classes':[{'minus_count':key[0],'sorted_B_gaps':key[1],'dimension':key[2],'patterns':count}
                              for key,count in sorted(hist.items())]}

def main():
    start=time.monotonic();dep=hashlib.sha256((OUT/'one_dimensional_record_field_transport_check.py').read_bytes()).hexdigest()
    assert dep=='9c0f787bb5b64238145c0647076e88b1011571f5539bcb7a4ed60d4d62234b27'
    result={'status':'PASS','dependency_sha256':dep,'all_physical_word_controls':[check(n) for n in (6,8,10,12,14)],
            'runtime_seconds':time.monotonic()-start,'scope':'One-dimensional supplied Gauss sector only; fixed minus records cut the closed Hamiltonian exactly, and births can create further cuts. No 3D fragmentation inference.'}
    text=json.dumps(result,indent=2)+'\n';(OUT/'ONE_DIMENSIONAL_RECORD_CUT_FACTORIZATION_RESULTS.json').write_text(text);print(text,end='')

if __name__=='__main__':main()
