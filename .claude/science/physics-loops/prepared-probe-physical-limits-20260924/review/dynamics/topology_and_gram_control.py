"""Bounded extra checks of the independent primitive calculation, not root code."""
from pathlib import Path
from hashlib import sha256
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
import json
import time
import primitive_dynamics_control as p


def gram_mean(side):
    vertices,index,aset,neighbors,edges,edge_id,axes = p.graph(side)
    def vertex(x): return index[tuple(t%side for t in x)]
    d,h,c,e,v1,v2,v3 = map(vertex,[(1,1,0),(2,2,0),(1,0,0),(0,1,0),
                                 (0,-1,0),(0,0,1),(0,0,-1)])
    word = [int(i in set(aset)) for i in range(len(vertices))]
    word[d]=word[h]=-1;word[v1]=word[v2]=word[v3]=1
    wc=word.copy();wc[c]=1
    we=word.copy();we[e]=1
    vector={(tuple(wc),((edge_id[d,c],-1),)):1,
            (tuple(we),((edge_id[d,e],-1),)):-1}
    norm_sum=Fraction(0); pair_count=0
    for a,q in combinations(aset,2):
        if not(set(neighbors[a]) & set(neighbors[q])): continue
        pair_count+=1
        output=defaultdict(int)
        for (w,f),coefficient in vector.items():
            for w1,e1,k1 in p.outward(w,a,neighbors,edge_id):
                for w2,e2,k2 in p.outward(w1,q,neighbors,edge_id):
                    flow=p.shifted(p.shifted(f,e1,k1),e2,k2)
                    output[w2,flow]+=coefficient
        groups=p.flat_group(output,axes,True)
        norm_sum+=p.scalar(groups,groups)
    return {"side":side,"pairs":pair_count,"sum_norm_S_squared":p.fraction(norm_sum),
            "minus_two_Gram_sum":p.fraction(-2*norm_sum),
            "method":"Two outward hops and positive norms, no inward hops or H4-action routine."}


def compact_witness(witness):
    terms=[]
    for term in witness["Laurent_terms"]:
        terms.append({"coefficient":term["coefficient"],
                      "shifts":[(tuple(s["edge"][0]),tuple(s["edge"][1]),s["power"])
                                for s in term["electric_shift"]]})
    assert sum(t["coefficient"] for t in terms)==witness["group_coefficient_before_dividing_sqrt2"]
    return {**{k:v for k,v in witness.items() if k!="Laurent_terms"},"terms":terms}


def main():
    here=Path(__file__).resolve().parent
    start=time.perf_counter()
    original=json.loads((here/"PRIMITIVE_DYNAMICS_RESULTS.json").read_text())
    six=original["rows"][0]
    eight=p.control(8)
    rows=[]
    for row in (six,eight):
        gram=gram_mean(row["side"])
        assert gram["minus_two_Gram_sum"]==row["flat_moments"]["harmonic_averaged"]["mean_H4"]
        compact={k:v for k,v in row.items() if k!="selected_birth_rows"}
        compact["Gram_cross_check"]=gram
        births=[]
        for b in row["selected_birth_rows"]:
            births.append({**{k:v for k,v in b.items() if k!="witness"},
                           "witness":compact_witness(b["witness"])})
        compact["selected_birth_rows"]=births
        variance=row["flat_moments"]["harmonic_averaged"]["variance_H4"]["numerator"]
        for b in births:
            gamma=b["gamma_harmonic_averaged"]["numerator"]
            assert 0<gamma<=25*variance
        rows.append(compact)
    result={"scope":"Side-eight topology extension and direct positive-Gram mean cross-checks on sides six/eight. Reuses only this independent packet's primitive helpers, not author code. All original side-six logs retained.",
            "rows":rows,"source_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),
            "primitive_source_sha256":sha256((here/"primitive_dynamics_control.py").read_bytes()).hexdigest(),
            "side_six_result_sha256":sha256((here/"PRIMITIVE_DYNAMICS_RESULTS.json").read_bytes()).hexdigest(),
            "elapsed_seconds":time.perf_counter()-start}
    print(json.dumps(result,indent=2))


if __name__=="__main__":main()
