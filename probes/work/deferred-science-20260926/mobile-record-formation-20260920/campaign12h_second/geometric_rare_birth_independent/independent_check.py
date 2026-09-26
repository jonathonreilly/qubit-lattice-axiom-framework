#!/usr/bin/env python3
"""Independent pre-author comparison controls for geometric rare births.

Only the previously sealed independent matching primitives are imported.
No author rare-birth code/results are read. No file outside --out is written.
"""
import sys
sys.dont_write_bytecode=True
import argparse
from collections import Counter,deque
import hashlib
import importlib.util
import itertools as it
import json
from pathlib import Path
import sympy as s

HERE=Path(__file__).resolve().parent
PRIMITIVES=HERE.parent/'geometric_partner_independent/independent_check.py'
assert hashlib.sha256(PRIMITIVES.read_bytes()).hexdigest()=='1b6c73b87789df05d5cafc03beff72ed7973ddfc22c3b0327128c0476bfd4c8f'
spec=importlib.util.spec_from_file_location('own_prior_matching_primitives',PRIMITIVES)
own=importlib.util.module_from_spec(spec);spec.loader.exec_module(own)
edge=own.edge

def adjacency(n,edges):
    out={i:set() for i in range(n)}
    for a,b in edges:out[a].add(b);out[b].add(a)
    return out

def connected(n,edges):
    adj=adjacency(n,edges);seen={0};todo=[0]
    while todo:
        for x in adj[todo.pop()]-seen:seen.add(x);todo.append(x)
    return len(seen)==n

def slide(m,a,b,c,edges):
    assert edge(a,b) in m and edge(b,c) in edges and c not in own.partners(m)
    target=(m-{edge(a,b)})|{edge(b,c)}
    assert len(target)==len(m) and len(own.partners(target))==2*len(target)
    assert (target-{edge(b,c)})|{edge(a,b)}==m
    return target

def vacancy_path(m,side,targets,adj):
    partners=own.partners(m);vacancies=side-set(partners);assert len(vacancies)==1
    vacancy=next(iter(vacancies));parent={vacancy:None};todo=deque([vacancy]);end=None
    while todo:
        x=todo.popleft()
        if x in targets:end=x;break
        for r in sorted(adj[x]):
            if r in partners:
                y=partners[r]
                if y not in parent:parent[y]=(x,r);todo.append(y)
    if end is None:return None
    path=[]
    while parent[end] is not None:
        x,r=parent[end];path.append((x,r,end));end=x
    return path[::-1]

def execute_path(m,path,edges):
    for a,r,b in path:m=slide(m,b,r,a,edges)
    return m

def transform(m,target,L,R,edges,adj):
    original=m;events=0;cycle_lengths=[]
    for side in (L,R):
        desired=side-set(own.partners(target));assert len(desired)==1
        path=vacancy_path(m,side,desired,adj);assert path is not None
        opposite=(R if side==L else L)-set(own.partners(m))
        m=execute_path(m,path,edges);events+=len(path)
        assert ((R if side==L else L)-set(own.partners(m)))==opposite
    while m!=target:
        difference=m^target;diffadj=adjacency(len(L)+len(R),difference)
        start=min(x for e in difference for x in e);vertices={start};todo=[start]
        while todo:
            for x in diffadj[todo.pop()]-vertices:vertices.add(x);todo.append(x)
        assert all(len(diffadj[x])==2 for x in vertices)
        cycle_edges={e for e in difference if set(e)<=vertices};assert len(cycle_edges)==len(vertices)
        old=m;old_vacancies=set(range(len(L)+len(R)))-set(own.partners(m))
        path=vacancy_path(m,L,L&vertices,adj);assert path is not None and len(path)>0
        for a,r,b in path[:-1]:assert not ({a,r,b}&vertices)
        external,entering_r,entry=path[-1]
        assert external not in vertices and entering_r in vertices and entry in vertices
        m=execute_path(m,path,edges);events+=len(path);hole=entry;tp=own.partners(target)
        around=0
        while tp[hole]!=entering_r:
            r=tp[hole];next_hole=own.partners(m)[r]
            assert r in vertices and next_hole in vertices
            m=slide(m,next_hole,r,hole,edges);hole=next_hole;around+=1;events+=1
            assert around<len(vertices)
        assert own.partners(m)[entering_r]==external
        m=slide(m,external,entering_r,hole,edges);events+=1
        for a,r,b in reversed(path[:-1]):m=slide(m,a,r,b,edges);events+=1
        expected=(old-(old&cycle_edges))|(target&cycle_edges)
        assert m==expected
        assert set(range(len(L)+len(R)))-set(own.partners(m))==old_vacancies
        cycle_lengths.append({'cycle_vertices':len(vertices),'approach_slides':len(path),'around_slides':around+1})
    assert m==target and len(original)==len(target)
    return events,cycle_lengths

def regular_bipartite_controls():
    summary=Counter();total_near=0
    for K in range(1,5):
        L=set(range(K));R=set(range(K,2*K))
        for degree in range(1,K+1):
            choices=list(it.combinations(range(K),degree))
            for rows in it.product(choices,repeat=K):
                if any(sum(j in row for row in rows)!=degree for j in range(K)):continue
                edges={edge(i,K+j) for i,row in enumerate(rows) for j in row}
                if not connected(2*K,edges):continue
                adj=adjacency(2*K,edges);summary[(K,degree)]+=1
                for side in (L,R):
                    ordered=sorted(side)
                    for mask in range(1,(1<<K)-1):
                        subset={ordered[j] for j in range(K) if mask>>j&1}
                        assert len(set().union(*(adj[x] for x in subset)))>len(subset)
                near=[m for m in own.all_matchings(2*K,edges) if len(m)==K-1]
                total_near+=len(near);state_set=set(near)
                for m in near:
                    for side in (L,R):
                        for x in side:
                            path=vacancy_path(m,side,{x},adj);assert path is not None
                            result=execute_path(m,path,edges)
                            assert side-set(own.partners(result))=={x}
                seen={near[0]};todo=[near[0]]
                while todo:
                    for kind,data,m in own.channels(todo.pop(),edges):
                        if kind=='slide' and m not in seen:seen.add(m);todo.append(m)
                assert seen==state_set
    assert sum(summary.values())==106
    return {'connected_regular_bipartite_labeled_graphs':sum(summary.values()),
            'by_half_size_and_degree':{str(k):v for k,v in sorted(summary.items())},
            'total_near_perfect_states_checked':total_near}

def excursion_controls():
    cases=[];winding_example=None
    fixtures=[]
    for K in (3,4):
        cycle={edge(i,K+i) for i in range(K)}|{edge((i+1)%K,K+i) for i in range(K)}
        fixtures.append((K,cycle,f'cycle_{2*K}'))
        fixtures.append((K,{edge(i,K+j) for i in range(K) for j in range(K)},f'complete_K{K}_{K}'))
    coords=list(it.product((0,1),repeat=3));left=[x for x in coords if sum(x)%2==0];right=[x for x in coords if sum(x)%2==1]
    index={x:i for i,x in enumerate(left+right)}
    cube={edge(index[x],index[y]) for x in left for y in right if sum(abs(a-b) for a,b in zip(x,y))==1}
    fixtures.append((4,cube,'cube'))
    for K,edges,name in fixtures:
        near=[m for m in own.all_matchings(2*K,edges) if len(m)==K-1]
        L=set(range(K));R=set(range(K,2*K));adj=adjacency(2*K,edges)
        excursions=0;max_events=0;max_approach=0
        for m,target in it.product(near,repeat=2):
            count,cycles=transform(m,target,L,R,edges,adj)
            excursions+=len(cycles);max_events=max(max_events,count)
            max_approach=max([max_approach]+[x['approach_slides'] for x in cycles])
        cases.append({'graph':name,'near_states':len(near),'ordered_pairs_transformed':len(near)**2,
                      'cycle_excursions':excursions,'max_total_slides':max_events,'max_approach_slides':max_approach})
    assert sum(x['cycle_excursions'] for x in cases)>0
    return cases

def last_birth_matrix(n,edges,beta,weights=None,conservative_weights=None,kappa=1):
    all_states=own.all_matchings(n,edges);K=n//2
    near=[m for m in all_states if len(m)==K-1];full=[m for m in all_states if len(m)==K]
    ind={m:i for i,m in enumerate(near)};fi={m:i for i,m in enumerate(full)}
    S=s.zeros(len(near));A=s.zeros(len(near),len(full))
    for m,i in ind.items():
        for kind,data,target in own.channels(m,edges):
            if kind=='birth':A[i,fi[target]]+=(weights or {}).get(edge(*data),1)
            else:
                rate=kappa*(conservative_weights or {}).get(target,1)
                S[i,ind[target]]+=rate;S[i,i]-=rate
    h=A*s.ones(len(full),1)
    P=(beta*s.diag(*h)-S).inv(method='DM')*beta*A
    P=P.applyfunc(s.factor)
    assert (P*s.ones(len(full),1)-s.ones(len(near),1)).applyfunc(s.simplify)==s.zeros(len(near),1)
    return near,full,S,A,P

def exact_last_birth_and_countercontrols():
    b=s.symbols('b',positive=True);cycle4={(0,1),(1,2),(2,3),(0,3)}
    near,full,S,A,P=last_birth_matrix(4,cycle4,b)
    target=next(i for i,m in enumerate(full) if (0,1) in m)
    start=near.index(frozenset({(0,1)}));value=P[start,target]
    assert s.simplify(value-(b+2)/(b+4))==0
    assert P.applyfunc(lambda x:s.limit(x,b,0))==s.ones(len(near),len(full))/2
    cycle6={edge(i,(i+1)%6) for i in range(6)}
    n6,f6,S6,A6,P6=last_birth_matrix(6,cycle6,b)
    assert S6==S6.T and P6.applyfunc(lambda x:s.limit(x,b,0))==s.ones(len(n6),len(f6))/len(f6)
    assert list(s.ones(1,len(n6))*A6)==[3,3]
    asymmetric_weights={frozenset({(0,1)}):2}
    na,fa,Sa,Aa,Pa=last_birth_matrix(4,cycle4,b,conservative_weights=asymmetric_weights)
    biased=[s.limit(x,b,0) for x in Pa[0,:]]
    assert biased[fa.index(full[target])]==s.Rational(3,5)
    nw,fw,Sw,Aw,Pw=last_birth_matrix(4,cycle4,b,weights={(0,1):2})
    weighted=[s.limit(x,b,0) for x in Pw[0,:]]
    assert weighted[fw.index(full[target])]==s.Rational(3,5)
    n0,f0,S0,A0,P0=last_birth_matrix(4,cycle4,b,kappa=0)
    assert P0[start,target]==1
    disconnected=cycle4|{(a+4,c+4) for a,c in cycle4}
    nd,fd,Sd,Ad,Pd=last_birth_matrix(8,disconnected,b)
    state=frozenset({(0,1),(2,3),(4,5)})
    limit=[s.limit(x,b,0) for x in Pd[nd.index(state),:]]
    assert sorted(limit)==[0,0,s.Rational(1,2),s.Rational(1,2)]
    tv=sum(abs(x-s.Rational(1,len(fd))) for x in limit)/2;assert tv==s.Rational(1,2)
    # Without regularity, the claimed fixed-opposite-vacancy reachability can fail.
    path4={(0,1),(1,2),(2,3)};m=frozenset({(2,3)})
    assert vacancy_path(m,{0,2},{2},adjacency(4,path4)) is None
    # A positive stopping time can destroy stationarity even for a symmetric chain.
    flip=s.Matrix([[-2,2],[2,-2]]);pi=s.Matrix([[s.Rational(1,2),s.Rational(1,2)]])
    assert pi*flip==s.zeros(1,2)
    assert (-flip.extract([1],[1])).inv()*flip.extract([1],[0])==s.ones(1,1)
    return {'cycle4_from_preserved_edge_probability':str(value),'cycle4_rare_limit':'1/2 from every near-perfect state',
            'cycle6_near_states':len(n6),'cycle6_rare_limit':'uniform on two full matchings from all nine near-perfect states',
            'countercontrols':{'nonregular_path4':'L vacancy 0 cannot reach 2 with R vacancy 1 fixed when only (2,3) is matched.',
              'disconnected_two_cycles':{'rare_probabilities':list(map(str,limit)),'tv_from_uniform':str(tv)},
              'asymmetric_extra_conservative_channels':{'rare_probabilities':list(map(str,biased)),'favored_full_probability':'3/5'},
              'unequal_birth_edge_rates':{'rare_probabilities':list(map(str,weighted)),'favored_full_probability':'3/5'},
              'zero_slide_rate':'A near-perfect C4 state completes its unique full extension with probability 1 for every positive b.',
              'already_full_start':'First-full law is its initial point mass.',
              'fixed_ratio_b_over_kappa':'For b/kappa=1 the preserved-edge probability stays 3/5; sending both rates to zero does not give 1/2.',
              'state_dependent_post_filling_observation':'The symmetric two-full-state chain sampled on first return/hit to state 0 after a positive departure time is delta_0, TV 1/2 from its uniform invariant law.'}}

def symbolic_cube_absorption():
    b=s.symbols('b',positive=True);vertices=list(it.product((0,1),repeat=3));index={x:i for i,x in enumerate(vertices)}
    edges={edge(i,j) for i,x in enumerate(vertices) for j,y in enumerate(vertices) if i<j and sum(abs(a-c) for a,c in zip(x,y))==1}
    states=own.all_matchings(8,edges)
    automorphisms=[]
    for perm in it.permutations(range(3)):
        for bits in it.product((0,1),repeat=3):
            automorphisms.append({i:index[tuple(x[perm[j]]^bits[j] for j in range(3))] for i,x in enumerate(vertices)})
    def representative(m):return min(tuple(sorted(edge(T[a],T[c]) for a,c in m)) for T in automorphisms)
    rep={m:representative(m) for m in states};orbits=sorted(set(rep.values()));oi={r:i for i,r in enumerate(orbits)}
    def columnar(m):return len(m)==4 and len({next(j for j in range(3) if vertices[a][j]!=vertices[c][j]) for a,c in m})==1
    full=[i for i,m in enumerate(orbits) if len(m)==4];transient=[i for i,m in enumerate(orbits) if len(m)<4]
    rows={};L=s.zeros(len(orbits))
    for m in states:
        row=[0]*len(orbits);i=oi[rep[m]]
        for kind,data,target in own.channels(m,edges):
            rate=b if kind=='birth' else 1
            row[oi[rep[target]]]+=rate;row[i]-=rate
        if i in rows:assert row==rows[i]
        else:rows[i]=row
    for i,row in rows.items():
        for j,x in enumerate(row):L[i,j]=x
    boundary=s.Matrix([int(columnar(orbits[i])) for i in full])
    solution=(-L.extract(transient,transient)).inv(method='DM')*L.extract(transient,full)*boundary
    solution=solution.applyfunc(s.factor)
    values={i:x for i,x in zip(transient,solution)}|{i:x for i,x in zip(full,boundary)}
    for m in states:
        if len(m)==4:continue
        residual=sum((b if kind=='birth' else 1)*(values[oi[rep[target]]]-values[oi[rep[m]]])
                     for kind,data,target in own.channels(m,edges))
        assert s.factor(residual)==0
    answer=s.factor(values[oi[()]]);claimed=(6*b**3+77*b**2+308*b+308)/(7*(b+6)*(3*b**2+19*b+22))
    assert s.factor(answer-claimed)==0
    assert s.limit(answer,b,0)==s.Rational(1,3) and s.limit(answer,b,s.oo)==s.Rational(2,7)
    assert answer.subs(b,1)==s.Rational(699,2156)
    return {'matching_states':len(states),'verified_automorphism_quotient_states':len(orbits),
            'unlumped_harmonic_residuals_checked':sum(len(m)<4 for m in states),
            'columnar_probability_from_empty':str(answer),'at_b_1':str(answer.subs(b,1)),
            'slow_limit':str(s.limit(answer,b,0)),'fast_limit':str(s.limit(answer,b,s.oo)),
            'difference_from_uniform':str(s.factor(answer-s.Rational(1,3)))}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,required=True);args=parser.parse_args()
    result={}
    for name,fn in [('regular_graphs',regular_bipartite_controls),('explicit_cycle_excursions',excursion_controls),
                    ('exact_last_birth_and_countercontrols',exact_last_birth_and_countercontrols),('symbolic_cube_absorption',symbolic_cube_absorption)]:
        result[name]=fn();print(json.dumps({name:result[name]},indent=2),flush=True)
    args.out.write_text(json.dumps(result,indent=2)+'\n');print('PASS: independent reconstruction completed.',flush=True)
