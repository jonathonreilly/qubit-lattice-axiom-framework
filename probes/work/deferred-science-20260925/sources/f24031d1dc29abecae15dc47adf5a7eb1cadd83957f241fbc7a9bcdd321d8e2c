"""Independent finite-word H4 and B_j H4 on the supplied Gauss-dressed probe.

No author builder, numerical Hamiltonian propagation, or root runner is used.
All path coefficients and flat-fiber moment sums are integers/rationals.
"""
from collections import defaultdict, deque
from fractions import Fraction
from itertools import product, combinations
from pathlib import Path
from hashlib import sha256
import json
import time


def graph(side):
    vertices = list(product(range(side), repeat=3))
    index = {x:i for i,x in enumerate(vertices)}
    aset = [i for i,x in enumerate(vertices) if sum(x)%2 == 0]
    neighbors = {}
    edges = []
    signed_axes = []
    for a in aset:
        x = vertices[a]
        neighbors[a] = []
        for axis in range(3):
            for sign in (-1,1):
                y = list(x); y[axis] = (y[axis]+sign)%side
                b = index[tuple(y)]
                neighbors[a].append(b)
                edges.append((a,b))
                unit = [0,0,0]; unit[axis] = sign
                signed_axes.append(tuple(unit))
    edge_id = {edge:i for i,edge in enumerate(edges)}
    return vertices,index,aset,neighbors,edges,edge_id,signed_axes


def shifted(flow, edge, amount):
    result = dict(flow)
    result[edge] = result.get(edge,0)+amount
    if result[edge] == 0: del result[edge]
    return tuple(sorted(result.items()))


def put(word, a, qa, b, qb):
    result = list(word); result[a] = qa; result[b] = qb
    return tuple(result)


def outward(word, a, neighbors, edge_id):
    q = word[a]
    if q:
        for b in neighbors[a]:
            if word[b] == 0:
                yield put(word,a,0,b,q),edge_id[a,b],-q


def inward(word, a, neighbors, edge_id):
    if word[a] == 0:
        for b in neighbors[a]:
            q = word[b]
            if q:
                yield put(word,a,q,b,0),edge_id[a,b],q


def h4_action(vector, pairs, neighbors, edge_id):
    result = defaultdict(int)
    paths = 0
    for (word,flow), coefficient in vector.items():
        for a,d in pairs:
            for w1,e1,k1 in outward(word,a,neighbors,edge_id):
                f1 = shifted(flow,e1,k1)
                for w2,e2,k2 in outward(w1,d,neighbors,edge_id):
                    f2 = shifted(f1,e2,k2)
                    for w3,e3,k3 in inward(w2,d,neighbors,edge_id):
                        f3 = shifted(f2,e3,k3)
                        for w4,e4,k4 in inward(w3,a,neighbors,edge_id):
                            result[w4,shifted(f3,e4,k4)] -= 2*coefficient
                            paths += 1
    return {k:v for k,v in result.items() if v},paths


def birth(vector, a, b, sigma, neighbors, edge_id):
    result = defaultdict(int)
    for (word,flow), coefficient in vector.items():
        for w,e,k in outward(word,a,neighbors,edge_id):
            if w[a] == 0 and w[b] == 0:
                out = put(w,a,sigma,b,-sigma)
                newflow = shifted(shifted(flow,e,k),edge_id[a,b],sigma)
                result[out,newflow] += coefficient
    return {k:v for k,v in result.items() if v}


def harmonic_signature(flow, axes):
    return tuple(sum(k*axes[e][d] for e,k in flow) for d in range(3))


def flat_group(vector, axes, keep_harmonic):
    result = defaultdict(int)
    for (word,flow), coefficient in vector.items():
        signature = harmonic_signature(flow,axes) if keep_harmonic else ()
        result[word,signature] += coefficient
    return {k:v for k,v in result.items() if v}


def scalar(left,right):
    return Fraction(sum(c*right.get(k,0) for k,c in left.items()),2)


def flow_from_paths(sources_sinks, vertices, aset, neighbors, edges, edge_id):
    adjacent = [[] for _ in vertices]
    for a,b in edges:
        adjacent[a].append(b); adjacent[b].append(a)
    aa = set(aset)
    flow = ()
    paths = []
    for source,sink in sources_sinks:
        queue = deque([source]); previous = {source:None}
        while sink not in previous:
            x = queue.popleft()
            for y in sorted(adjacent[x]):
                if y not in previous:
                    previous[y] = x;queue.append(y)
        path = [sink]
        while path[-1] != source: path.append(previous[path[-1]])
        path.reverse();paths.append([vertices[x] for x in path])
        for x,y in zip(path,path[1:]):
            edge,sign = ((x,y),-1) if x in aa else ((y,x),1)
            flow = shifted(flow,edge_id[edge],sign)
    return flow,paths


def gauss_check(vector, common, vertices, aset, edges):
    aa = set(aset)
    common_div = [0]*len(vertices)
    for e,k in common:
        a,b = edges[e];common_div[a]+=k;common_div[b]-=k
    for (word,flow) in vector:
        divergence = common_div.copy()
        for e,k in flow:
            a,b = edges[e];divergence[a]+=k;divergence[b]-=k
        assert all(divergence[i] == q-int(i in aa) for i,q in enumerate(word))
    return len(vector)


def describe_word(word, vertices, aset):
    aa = set(aset)
    return [{"site":vertices[i],"charge":q} for i,q in enumerate(word) if q!=int(i in aa)]


def fraction(value):
    return {"numerator":value.numerator,"denominator":value.denominator}


def control(side):
    vertices,index,aset,neighbors,edges,edge_id,axes = graph(side)
    def vertex(x): return index[tuple(t%side for t in x)]
    a,d,h,c,e,b,v1,v2,v3 = map(vertex,[(0,0,0),(1,1,0),(2,2,0),(1,0,0),
                                    (0,1,0),(-1,0,0),(0,-1,0),(0,0,1),(0,0,-1)])
    word = [int(i in set(aset)) for i in range(len(vertices))]
    word[d] = word[h] = -1
    word[v1] = word[v2] = word[v3] = 1
    wc = word.copy();wc[c] = 1
    we = word.copy();we[e] = 1
    initial = {(tuple(wc),((edge_id[d,c],-1),)):1,
               (tuple(we),((edge_id[d,e],-1),)):-1}
    common,common_paths = flow_from_paths([(d,v1),(h,v2),(h,v3)],vertices,aset,neighbors,edges,edge_id)
    pairs = [(x,y) for x,y in combinations(aset,2) if set(neighbors[x]) & set(neighbors[y])]
    hvec,path_count = h4_action(initial,pairs,neighbors,edge_id)
    gauss_initial = gauss_check(initial,common,vertices,aset,edges)
    gauss_hvec = gauss_check(hvec,common,vertices,aset,edges)
    moments = {}
    for preserve in (True,False):
        vin = flat_group(initial,axes,preserve)
        hv = flat_group(hvec,axes,preserve)
        mean = scalar(vin,hv)
        second = scalar(hv,hv)
        moments["harmonic_averaged" if preserve else "all_angles_zero"] = {
            "norm_squared":fraction(scalar(vin,vin)),"mean_H4":fraction(mean),
            "second_H4":fraction(second),"variance_H4":fraction(second-mean*mean),
            "nonzero_matter_fiber_groups":len(hv)}
    sigma_rows = []
    for sigma in (-1,1):
        bv = birth(initial,a,b,sigma,neighbors,edge_id)
        bhv = birth(hvec,a,b,sigma,neighbors,edge_id)
        assert not flat_group(bv,axes,True)
        gauss_bhv = gauss_check(bhv,common,vertices,aset,edges)
        grouped = flat_group(bhv,axes,True)
        gamma = scalar(grouped,grouped)
        group_plain = flat_group(bhv,axes,False)
        gamma_plain = scalar(group_plain,group_plain)
        assert gamma > 0
        witness_key = max(grouped,key=lambda k:abs(grouped[k]))
        witness_word,witness_signature = witness_key
        terms = [{"coefficient":coef,"electric_shift":[{"edge":[vertices[edges[ed][0]],vertices[edges[ed][1]]],"power":k} for ed,k in flow]}
                 for (ww,flow),coef in bhv.items() if ww == witness_word and harmonic_signature(flow,axes) == witness_signature]
        sigma_rows.append({"sigma":sigma,"initial_birth_Laurent_terms":len(bv),
            "initial_flat_fiber_birth_norm_squared":fraction(Fraction(0)),
            "BH4_Laurent_terms":len(bhv),"BH4_nonzero_flat_fiber_groups":len(grouped),
            "all_BH4_terms_Gauss_checked":gauss_bhv,
            "gamma_harmonic_averaged":fraction(gamma),"gamma_all_angles_zero":fraction(gamma_plain),
            "witness":{"matter_deviations":describe_word(witness_word,vertices,aset),
                        "harmonic_signature_without_common_flow":witness_signature,
                        "group_coefficient_before_dividing_sqrt2":grouped[witness_key],
                        "Laurent_terms":terms}})
    return {"side":side,"vertices":len(vertices),"A_sites":len(aset),"edges":len(edges),
        "overlapping_A_pairs":len(pairs),"H4_four_hop_paths":path_count,
        "H4_Laurent_terms":len(hvec),"initial_Gauss_terms_checked":gauss_initial,
        "H4_Gauss_terms_checked":gauss_hvec,"common_flow_paths":common_paths,
        "flat_moments":moments,"selected_birth_rows":sigma_rows}


def main():
    start = time.perf_counter()
    result = {"scope":"Exact one-H4-action and subsequent original resolved B_j action on the supplied two-branch charged preparation. Harmonic-fiber averaging precedes any comparison to all-zero link angles. Finite graph, no time propagation or microscopic energy computation.",
              "rows":[control(6)],"code_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),
              "elapsed_seconds":time.perf_counter()-start}
    print(json.dumps(result,indent=2))


if __name__ == "__main__": main()
