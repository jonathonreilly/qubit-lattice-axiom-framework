"""Independent exact Laurent compression of the supplied charged J_- input.

Graph, charge hops and string convention are reconstructed from the admitted
parents.  The elementary graph/outward/flow conventions agree with this
checker's previously sealed primitive_dynamics_control.py; no author builder
or author result is imported.  New computation uses only the two-outward-hop
Gram identity, not the author's or the previous four-hop implementation.
"""
from collections import defaultdict, deque, Counter
from itertools import product, combinations
from pathlib import Path
from hashlib import sha256
from fractions import Fraction
import json
import time


def graph(side):
    vertices = list(product(range(side), repeat=3))
    index = {x: i for i, x in enumerate(vertices)}
    aa = [i for i, x in enumerate(vertices) if sum(x) % 2 == 0]
    neighbors, edges, axes = {}, [], []
    for a in aa:
        neighbors[a] = []
        for mu in range(3):
            for sign in (-1, 1):
                y = list(vertices[a]); y[mu] = (y[mu] + sign) % side
                b = index[tuple(y)]; neighbors[a].append(b)
                edges.append((a, b))
                axis = [0, 0, 0]; axis[mu] = sign; axes.append(tuple(axis))
    return vertices, index, aa, neighbors, edges, {e:i for i,e in enumerate(edges)}, axes


def add(flow, edge, power):
    out = dict(flow); out[edge] = out.get(edge, 0) + power
    if not out[edge]: del out[edge]
    return tuple(sorted(out.items()))


def difference(right, left):
    out = right
    for e, k in left: out = add(out, e, -k)
    return out


def outward(word, a, neighbors, edge_id):
    if word[a]:
        for b in neighbors[a]:
            if word[b] == 0:
                out = list(word); out[a] = 0; out[b] = word[a]
                yield tuple(out), edge_id[a,b], -word[a]


def two_hops(initial, a, c, neighbors, edge_id):
    out = defaultdict(lambda: defaultdict(int))
    for word, flow, coefficient in initial:
        for w1,e1,k1 in outward(word,a,neighbors,edge_id):
            for w2,e2,k2 in outward(w1,c,neighbors,edge_id):
                f = add(add(flow,e1,k1),e2,k2)
                out[w2][f] += coefficient
    return out


def gram_polynomial(out, factor):
    poly = defaultdict(int)
    for terms in out.values():
        terms = [(f,c) for f,c in terms.items() if c]
        for left,cl in terms:
            for right,cr in terms:
                poly[difference(right,left)] += factor*cl*cr
    return {f:c for f,c in poly.items() if c}


def signature(flow, axes):
    return tuple(sum(k*axes[e][mu] for e,k in flow) for mu in range(3))


def divergence(flow, edges, nv):
    out = [0]*nv
    for e,k in flow:
        a,b = edges[e]; out[a] += k; out[b] -= k
    return out


def common_flow(pairs, vertices, aa, edges, edge_id):
    adjacent = [[] for _ in vertices]
    for a,b in edges: adjacent[a].append(b); adjacent[b].append(a)
    aa = set(aa); flow = (); paths = []
    for source,sink in pairs:
        queue = deque([source]); prev = {source:None}
        while sink not in prev:
            x = queue.popleft()
            for y in sorted(adjacent[x]):
                if y not in prev: prev[y]=x; queue.append(y)
        path = [sink]
        while path[-1] != source: path.append(prev[path[-1]])
        path.reverse(); paths.append([vertices[v] for v in path])
        for x,y in zip(path,path[1:]):
            edge,power = ((x,y),-1) if x in aa else ((y,x),1)
            flow = add(flow,edge_id[edge],power)
    return flow,paths


def qjson(x):
    x = Fraction(x)
    return [x.numerator,x.denominator]


def encode_poly(poly):
    return [{"flow":f,"coefficient":c} for f,c in sorted(poly.items())]


def compress(side):
    vertices,index,aa,neighbors,edges,edge_id,axes = graph(side)
    def v(x): return index[tuple(t%side for t in x)]
    a,d,h,c,e,b,v1,v2,v3 = map(v,[(0,0,0),(1,1,0),(2,2,0),(1,0,0),
                                   (0,1,0),(-1,0,0),(0,-1,0),(0,0,1),(0,0,-1)])
    base = [int(i in set(aa)) for i in range(len(vertices))]
    word = base.copy(); word[d]=word[h]=-1
    word[v1]=word[v2]=word[v3]=1
    wc=word.copy(); wc[c]=1; we=word.copy(); we[e]=1
    initial = [(tuple(wc),((edge_id[d,c],-1),),1),
               (tuple(we),((edge_id[d,e],-1),),-1)]
    common,paths = common_flow([(d,v1),(h,v2),(h,v3)],vertices,aa,edges,edge_id)
    pairset = set()
    b_neighbors = defaultdict(list)
    for av,bv in edges: b_neighbors[bv].append(av)
    for avs in b_neighbors.values(): pairset.update(combinations(sorted(avs),2))
    prepared,empty,changed = defaultdict(int),defaultdict(int),[]
    for x,y in sorted(pairset):
        pp = gram_polynomial(two_hops(initial,x,y,neighbors,edge_id),-1)
        pe = gram_polynomial(two_hops([(tuple(base),(),1)],x,y,neighbors,edge_id),-2)
        for f,k in pp.items(): prepared[f]+=k
        for f,k in pe.items(): empty[f]+=k
        diff = {f:pp.get(f,0)-pe.get(f,0) for f in set(pp)|set(pe)}
        diff = {f:k for f,k in diff.items() if k}
        if diff: changed.append({"A_pair":[vertices[x],vertices[y]],"terms":encode_poly(diff)})
    prepared={f:k for f,k in prepared.items() if k}
    empty={f:k for f,k in empty.items() if k}
    defect={f:prepared.get(f,0)-empty.get(f,0) for f in set(prepared)|set(empty)}
    defect={f:k for f,k in defect.items() if k}
    assert all(not any(divergence(f,edges,len(vertices))) for f in set(prepared)|set(empty))
    assert all(prepared.get(tuple((e,-k) for e,k in f),0)==c0 for f,c0 in prepared.items())
    haar_defect={f:k for f,k in defect.items() if not any(signature(f,axes))}
    killed={f:k for f,k in defect.items() if any(signature(f,axes))}
    electric=[]
    for word,branch,_ in initial:
        flow=common
        for ed,k in branch: flow=add(flow,ed,k)
        div=divergence(flow,edges,len(vertices))
        assert all(div[i]==word[i]-base[i] for i in range(len(vertices)))
        fd=dict(flow)
        mask=[int(word[bv]==0) for av,bv in edges]
        linear=[mask[ed]*(2*fd.get(ed,0)-word[av]) for ed,(av,bv) in enumerate(edges)]
        constant=sum(mask[ed]*(fd.get(ed,0)**2-word[av]*fd.get(ed,0)) for ed,(av,bv) in enumerate(edges))
        electric.append({"mask":mask,"linear":linear,"constant":constant,"flow":flow})
    mask=[Fraction(electric[0]["mask"][i]+electric[1]["mask"][i],2) for i in range(len(edges))]
    linear=[Fraction(electric[0]["linear"][i]+electric[1]["linear"][i],2) for i in range(len(edges))]
    constant=Fraction(electric[0]["constant"]+electric[1]["constant"],2)
    cos_terms=[]
    for f,k in haar_defect.items():
        if f and f<tuple((ed,-pw) for ed,pw in f): cos_terms.append({"flow":f,"cos_coefficient":2*k})
    # A1: two charges have changed sign; two outward hops retain their full
    # signed phases.  No empty-sector Wilson formula was used for prepared.
    result={"side":side,"vertices":len(vertices),"edges":len(edges),"A_sites":len(aa),
        "overlapping_pairs":len(pairset),"changed_pairs":len(changed),
        "gauss_and_Hermiticity_exact":True,"all_flows_divergence_free_exact":True,
        "empty_constant":empty[()],"empty_flat":sum(empty.values()),
        "prepared_haar_flat":sum(k for f,k in prepared.items() if not any(signature(f,axes))),
        "defect_constant":defect.get((),0),"defect_haar_flat":sum(haar_defect.values()),
        "defect_all_angle_flat":sum(defect.values()),"haar_killed_term_count":len(killed),
        "haar_killed_coefficient_sum":sum(killed.values()),
        "haar_defect_Laurent_term_count":len(haar_defect),
        "cosine_histogram":dict(Counter((str((sum(abs(k) for _,k in t["flow"]),t["cos_coefficient"]))) for t in cos_terms)),
        "haar_defect_coefficient_L1":sum(abs(k) for k in haar_defect.values()),
        "electric_mask_histogram":dict(Counter(str(x) for x in mask)),
        "electric_constant":qjson(constant),"common_paths":paths}
    data={"summary":result,"vertices":vertices,"edges":edges,"signed_axes":axes,
          "prepared_polynomial":encode_poly(prepared),"empty_polynomial":encode_poly(empty),
          "haar_defect_polynomial":encode_poly(haar_defect),"haar_killed_polynomial":encode_poly(killed),
          "defect_cosines":sorted(cos_terms,key=lambda r:r["flow"]),"changed_pairs":changed,
          "electric_branches":electric,"electric_mask":list(map(qjson,mask)),
          "electric_linear":list(map(qjson,linear)),"electric_constant":qjson(constant)}
    return data


def main():
    start=time.perf_counter(); rows=[]
    base=Path(__file__).resolve().parent
    for side in (6,8):
        data=compress(side)
        path=base/f"LAURENT_DATA_L{side}.json"
        path.write_text(json.dumps(data,indent=2)+"\n")
        rows.append({**data["summary"],"data_sha256":sha256(path.read_bytes()).hexdigest()})
    print(json.dumps({"method":"exact integer two-hop Gram enumeration, with exact harmonic-character rejection",
        "rows":rows,"source_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),
        "elapsed_seconds":time.perf_counter()-start},indent=2))


if __name__=="__main__":main()
