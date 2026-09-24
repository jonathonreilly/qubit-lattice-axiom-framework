"""Full-H4 first/second moments for each normalized selected-output matter word.

The weak-field normalization supplies a different rescaled field packet,
not a division of a flat zero vector. Only this independent primitive module
is reused. Values below are flat-fiber coefficients of rotor h, not heat.
"""
from pathlib import Path
from hashlib import sha256
from itertools import combinations
from fractions import Fraction
from collections import defaultdict
import json
import time
import primitive_dynamics_control as p


def one(side,sigma):
    vertices,index,aset,neighbors,edges,edge_id,axes=p.graph(side)
    def vertex(x):return index[tuple(t%side for t in x)]
    a,d,h,c,e,b,v1,v2,v3=map(vertex,[(0,0,0),(1,1,0),(2,2,0),(1,0,0),
        (0,1,0),(-1,0,0),(0,-1,0),(0,0,1),(0,0,-1)])
    word=[int(i in set(aset)) for i in range(len(vertices))]
    word[d]=word[h]=-1;word[a]=sigma;word[b]=-sigma
    for x in (c,e,v1,v2,v3):word[x]=1
    flow=()
    for ed,k in [(edge_id[d,c],-1),(edge_id[a,e],-1),(edge_id[a,b],sigma)]:
        flow=p.shifted(flow,ed,k)
    initial={(tuple(word),flow):1}
    common,paths=p.flow_from_paths([(d,v1),(h,v2),(h,v3)],vertices,aset,neighbors,edges,edge_id)
    p.gauss_check(initial,common,vertices,aset,edges)
    pairs=[(x,y)for x,y in combinations(aset,2)if set(neighbors[x])&set(neighbors[y])]
    hv,paths_count=p.h4_action(initial,pairs,neighbors,edge_id)
    gauss=p.gauss_check(hv,common,vertices,aset,edges)
    moments={}
    for keep in (True,False):
        v=p.flat_group(initial,axes,keep);w=p.flat_group(hv,axes,keep)
        mean=2*p.scalar(v,w);second=2*p.scalar(w,w)
        moments['harmonic_averaged'if keep else'all_angles_zero']={
            'mean_H4':p.fraction(mean),'second_H4':p.fraction(second),
            'variance_H4':p.fraction(second-mean*mean),'groups':len(w)}
    # Positive Gram mean from only outward hops, separately from inward H4 action.
    gram=Fraction(0)
    for x,y in pairs:
        sv=defaultdict(int)
        for w1,e1,k1 in p.outward(tuple(word),x,neighbors,edge_id):
            for w2,e2,k2 in p.outward(w1,y,neighbors,edge_id):
                sv[w2,p.shifted(p.shifted(flow,e1,k1),e2,k2)]+=1
        group=p.flat_group(sv,axes,True)
        gram+=2*p.scalar(group,group)
    assert p.fraction(-2*gram)==moments['harmonic_averaged']['mean_H4']
    single_hop_count=sum(1 for x in aset for _ in p.outward(tuple(word),x,neighbors,edge_id))
    assert single_hop_count==len(edges)-36
    return {'side':side,'sigma':sigma,'matter_records':sum(q!=0 for q in word),
            'matter_deviations':p.describe_word(tuple(word),vertices,aset),
            'H4_four_hop_paths':paths_count,'H4_Laurent_terms':len(hv),
            'all_H4_terms_Gauss_checked':gauss,'flat_moments':moments,
            'sum_positive_Gram_norms':p.fraction(gram),
            'M_rotor_mean_exact_for_any_field_in_this_matter_word':single_hop_count}


def main():
    start=time.perf_counter();here=Path(__file__).resolve().parent
    rows=[one(side,sigma)for side in (6,8)for sigma in (-1,1)]
    print(json.dumps({'scope':__doc__,'rows':rows,
        'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'primitive_source_sha256':sha256((here/'primitive_dynamics_control.py').read_bytes()).hexdigest(),
        'elapsed_seconds':time.perf_counter()-start},indent=2))


if __name__=='__main__':main()
