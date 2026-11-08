#!/usr/bin/env python3
"""Exact residue geometry supporting the vertex-output candidate; no physics selection."""
from itertools import permutations, product
from collections import Counter
from pathlib import Path
from hashlib import sha256
import argparse, json, resource, signal, time


def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--free-all-unused',action='store_true'); args=parser.parse_args()
    resource.setrlimit(resource.RLIMIT_CPU,(30,30)); signal.alarm(35)
    start=time.monotonic(); phases=list(product(range(5),repeat=3))
    def distance(x,p):return sum(a!=b for a,b in zip(x,p))
    def kind(x,p):
        d=distance(x,p)
        return 'active' if d==1 else ('output' if d==0 or args.free_all_unused else 'frozen')
    def edge(q,i,sign):
        return [tuple((q[j]+(sign*k if j==i else 0))%5 for j in range(3)) for k in range(1,5)]
    counts=Counter(); witness_counts=Counter()
    for p in phases:
        classes=Counter(kind(x,p) for x in phases)
        assert classes['active']==12
        assert classes['output']>=1
        for q in phases:
            if p==q:continue
            witnesses=[(i,sign) for i in range(3) for sign in (-1,1) if all(kind(x,p)=='frozen' for x in edge(q,i,sign))]
            assert witnesses, ('origin detector lost fixed-zero witness',p,q)
            counts[distance(p,q)]+=1; witness_counts[len(witnesses)]+=1
    rotations=[]
    for perm in permutations(range(3)):
        parity=(-1)**sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
        for signs in product((-1,1),repeat=3):
            if parity*signs[0]*signs[1]*signs[2]==1:rotations.append((perm,signs))
    covariance_checks=0
    for perm,signs in rotations:
        def rot(x):return tuple((signs[i]*x[perm[i]])%5 for i in range(3))
        for p in phases:
            for x in phases:
                assert kind(rot(x),rot(p))==kind(x,p)
                covariance_checks+=1
    # A concrete failed enlargement, not an inference from absence of witnesses:
    # p=(0,0,0), q=(1,1,1) have disjoint active site sets. If all other sites
    # are unrestricted, the tensor product of both sets of link-code factors
    # is nonzero and lies in both enlarged sectors.
    p=(0,0,0);q=(1,1,1)
    active_p={x for x in phases if distance(x,p)==1};active_q={x for x in phases if distance(x,q)==1}
    assert active_p.isdisjoint(active_q)
    print(json.dumps({'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'phase_pairs_by_coordinate_difference':dict(counts),'pairs_by_number_of_fixed_zero_edge_witnesses':dict(witness_counts),'rotations':len(rotations),'covariance_checks':covariance_checks,'qubits_per_cell':dict(Counter(kind(x,p) for x in phases)),'free_all_unused_common_sector_witness':{'p':p,'q':q,'disjoint_active_sets':True},'elapsed_seconds':time.monotonic()-start,'max_rss':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'scope':'finite residue geometry; operator completeness and arbitrary-n proof require the hand argument'},indent=2))

if __name__=='__main__':main()
