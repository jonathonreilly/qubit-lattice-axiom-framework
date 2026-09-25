#!/usr/bin/env python3
"""Independent four-hop control of the colored/Gauss and occupancy reduction.

This program does not import the occupation builder. It reads that program's
saved integer rows only to compare independently enumerated primitive paths.
"""
from collections import Counter
from itertools import combinations,product
from pathlib import Path
import hashlib,json,time
import numpy as np

HERE=Path(__file__).resolve().parent


def make_graph(L):
    V=tuple(product(range(L),repeat=3))
    AA=tuple(v for v in V if sum(v)%2==0)
    BB=tuple(v for v in V if sum(v)%2==1)
    neighbors={}
    for v in V:
        neighbors[v]=tuple(w for w in V if sum(
            min((a-b)%L,(b-a)%L) for a,b in zip(v,w))==1)
    pairs=tuple((u,v) for u,v in combinations(AA,2)
                if set(neighbors[u]).intersection(neighbors[v]))
    return V,AA,BB,neighbors,pairs


def step(q,flow,a,b,outward):
    # Every edge is oriented from A to B. The dictionaries hold exact integers.
    source,destination=(a,b) if outward else (b,a)
    assert source in q and destination not in q
    result=q.copy();charge=result.pop(source);result[destination]=charge
    flux=flow.copy();edge=(a,b)
    flux[edge]+=(-charge if outward else charge)
    if not flux[edge]:del flux[edge]
    return result,flux


def gauss_delta(initial,final,flow):
    residual=Counter(final)
    residual.subtract(initial)
    for (a,b),k in flow.items():
        residual[a]-=k;residual[b]+=k
    assert all(v==0 for v in residual.values())


def primitive_row(AA,BB,neighbors,pairs,J,minus,all_gauss=False):
    initial={v:1 for v in AA+J};initial[minus]=-1
    colored=Counter();paths=0;gauss_checked=0
    for u,v in pairs:
        local_checked=False
        for p in neighbors[u]:
            if p in initial:continue
            q1,f1=step(initial,Counter(),u,p,True)
            for q in neighbors[v]:
                if q in q1:continue
                q2,f2=step(q1,f1,v,q,True)
                for r in neighbors[v]:
                    if r not in q2:continue
                    q3,f3=step(q2,f2,v,r,False)
                    for s in neighbors[u]:
                        if s not in q3:continue
                        q4,f4=step(q3,f3,u,s,False)
                        assert all(a in q4 for a in AA)
                        JJ=tuple(b for b in BB if b in q4)
                        mm=tuple(x for x,c in q4.items() if c==-1)
                        assert len(JJ)==2 and len(mm)==1 and sum(q4.values())==len(AA)
                        colored[(JJ,mm[0])]+=1;paths+=1
                        if all_gauss or not local_checked:
                            gauss_delta(initial,q4,f4)
                            gauss_checked+=1;local_checked=True
    coarse=Counter()
    for (J,m),weight in colored.items():coarse[J]+=weight
    return colored,coarse,paths,gauss_checked


def resolved_mark(AA,BB,neighbors):
    a=AA[0];b=neighbors[a][0];initial={v:1 for v in AA}
    rows=[]
    for sigma in (-1,1):
        born=[]
        for z in neighbors[a]:
            if z==b:continue
            q,flow=step(initial,Counter(),a,z,True)
            assert a not in q and b not in q
            q[a]=sigma;q[b]=-sigma;flow[(a,b)]+=sigma
            gauss_delta(initial,q,flow)
            J=tuple(x for x in BB if x in q)
            minus=next(x for x,c in q.items() if c==-1)
            born.append(dict(occupied_B=J,minus=minus,
                electric_change=[dict(A=e[0],B=e[1],value=k) for e,k in sorted(flow.items())],amplitude=1))
        assert len({(tuple(map(tuple,r['occupied_B'])),tuple(r['minus'])) for r in born})==len(neighbors[a])-1
        rows.append(dict(a=a,b=b,sigma=sigma,squared_norm=len(born),branches=born,
                         all_Gauss_residuals_zero=True,flat_coefficients_positive=True))
    return rows


def run(L,reference):
    V,AA,BB,neighbors,pairs=make_graph(L)
    saved={tuple(map(tuple,row['occupied_B'])):row for row in reference['saved_occupation_rows']}
    bsets=list(combinations(BB,2))
    if L==2:
        initial_words=[(J,m) for J in bsets for m in AA+J]
    else:
        initial_words=[(J,m) for J in saved for m in (AA[0],)+J]
    full_words=[(J,m) for J in bsets for m in AA+J] if L==2 else []
    number={word:i for i,word in enumerate(full_words)}
    matrix=np.zeros((len(full_words),len(full_words)),dtype=np.int64) if L==2 else None
    checked=[];total_paths=0;gauss_count=0
    # On the cube all occupancy rows have the same permutation-invariant form;
    # compute their exact primitive rows and compare the one saved representative.
    for J,minus in initial_words:
        colored,coarse,paths,ng=primitive_row(AA,BB,neighbors,pairs,J,minus,all_gauss=(L==2))
        total_paths+=paths;gauss_count+=ng
        reference_row=saved.get(J)
        if reference_row:
            expected={tuple(map(tuple,e['occupied_B'])):e['value'] for e in reference_row['entries']}
            assert dict(coarse)==expected
        if L==2:
            for dest,weight in colored.items():matrix[number[(J,minus)],number[dest]]=weight
            assert paths==49
        raw=json.dumps([dict(occupied_B=k,value=v) for k,v in sorted(coarse.items())],sort_keys=True).encode()
        checked.append(dict(occupied_B=J,minus=minus,primitive_paths=paths,
            colored_destinations=len(colored),occupation_destinations=len(coarse),
            directly_compared_to_saved_row=reference_row is not None,
            occupation_row_sha256=hashlib.sha256(raw).hexdigest(),
            complete_occupation_row=[dict(occupied_B=k,value=v) for k,v in sorted(coarse.items())]))
    result=dict(L=L,vertex_count=len(V),degree=len(neighbors[AA[0]]),
        initial_colored_words=len(initial_words),direct_reference_rows=sum(x['directly_compared_to_saved_row'] for x in checked),
        total_primitive_paths=total_paths,exact_Gauss_path_checks=gauss_count,
        all_reference_rows_agree=True,rows=checked,resolved_birth_checks=resolved_mark(AA,BB,neighbors))
    if L==2:
        assert np.array_equal(matrix,matrix.T)
        assert (matrix.sum(axis=1)==49).all()
        result.update(full_colored_matrix=matrix.tolist(),full_colored_matrix_symmetric=True,
            exact_positive_constant_eigenvector=True,exact_Perron_value=49,
            floating_top_eigenvalue_diagnostic=float(np.linalg.eigvalsh(matrix)[-1]))
    return result


if __name__=='__main__':
    tic=time.perf_counter();source=HERE/'OCCUPATION_SPECTRUM_RESULTS.json'
    previous=json.loads(source.read_text())
    references={r['L']:r for r in previous['rows']}
    rows=[run(L,references[L]) for L in (2,4)]
    data=dict(scope=__doc__,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        comparison_data_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),rows=rows,
        elapsed_seconds=time.perf_counter()-tic,no_author_code=True,
        limitations='Primitive flat magnetic paths and Gauss changes only; no finite-g spectral simulation')
    with (HERE/'PRIMITIVE_COLORED_RESULTS.json').open('x') as out:json.dump(data,out,indent=2);out.write('\n')
    print(json.dumps({**{k:v for k,v in data.items() if k!='rows'},
        'rows':[{k:v for k,v in r.items() if k not in ('rows','full_colored_matrix')} for r in rows]},indent=2))
