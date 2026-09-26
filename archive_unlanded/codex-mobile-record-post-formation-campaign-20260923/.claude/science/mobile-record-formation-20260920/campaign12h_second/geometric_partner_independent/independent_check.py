#!/usr/bin/env python3
"""Independent geometric-partner checks; no author implementation imports.

Abstract matchings use edge sets. Marked records store only permanent IDs and
rational Bloch vectors; partnerships are reconstructed by antipodality.
Exact marked fixtures are supported configurations, not positive-probability
singleton draws from the continuous birth law.
"""
import argparse
from collections import Counter, deque
from fractions import Fraction as F
import itertools as it
import json
from pathlib import Path
import sympy as s


def edge(a,b):return tuple(sorted((a,b)))


def all_matchings(n,edges):
    adjacent={x:set() for x in range(n)}
    for a,b in edges:adjacent[a].add(b);adjacent[b].add(a)
    result=[]
    def rec(free,chosen):
        if not free:result.append(frozenset(chosen));return
        x=min(free);rest=free-{x};rec(rest,chosen)
        for y in sorted(adjacent[x]&rest):rec(rest-{y},chosen+[edge(x,y)])
    rec(set(range(n)),[])
    return sorted(result,key=lambda m:(len(m),sorted(m)))


def partners(m):return {x:y for a,b in m for x,y in [(a,b),(b,a)]}


def channels(m,edges):
    occupied=set(partners(m));out=[]
    for a,b in sorted(edges):
        if a not in occupied and b not in occupied:
            out.append(('birth',(a,b),m|{(a,b)}))
    adjacent={x:set() for e in edges for x in e}
    for a,b in edges:adjacent[a].add(b);adjacent[b].add(a)
    for a,b in sorted(m):
        for first,middle in [(a,b),(b,a)]:
            for vacant in sorted(adjacent[middle]-occupied):
                out.append(('slide',(first,middle,vacant),(m-{(a,b)})|{edge(middle,vacant)}))
    return out


def augment(m,perfect,n):
    mp,pp=partners(m),partners(perfect)
    start=min(set(range(n))-set(mp));path=[start]
    while True:
        y=pp[path[-1]];assert y not in path;path.append(y)
        if y not in mp:break
        z=mp[y];assert z not in path;path.append(z)
    assert len(path)%2==0
    current=m;events=[]
    for j in range(0,len(path)-2,2):
        a,b,c=path[j:j+3]
        event=('slide',(c,b,a))
        target=(current-{edge(b,c)})|{edge(a,b)}
        assert any((kind,data)==event and dest==target for kind,data,dest in channels(current,GRAPH_EDGES))
        events.append(event);current=target
    a,b=path[-2:];assert a not in partners(current) and b not in partners(current)
    current=current|{edge(a,b)};events.append(('birth',(a,b)))
    assert len(current)==len(m)+1 and len(events)<=n//2
    return current,events


def inspect_graph(n,edges,name):
    global GRAPH_EDGES
    GRAPH_EDGES=set(edges)
    states=all_matchings(n,edges);full=[m for m in states if len(m)*2==n]
    assert full
    P=full[0];by_state=set(states);reverse={m:[] for m in states};counts=Counter()
    longest_prescribed=0
    for m in states:
        for kind,data,target in channels(m,edges):
            assert target in by_state;reverse[target].append(m);counts[kind]+=1
            if kind=='slide':
                assert any(k=='slide' and d==data[::-1] and t==m for k,d,t in channels(target,edges))
        current=m;length=0
        while len(current)*2<n:
            current,events=augment(current,P,n);length+=len(events)
        assert length<=n//2
        longest_prescribed=max(longest_prescribed,length)
    distance={m:0 for m in full};queue=deque(full)
    while queue:
        target=queue.popleft()
        for m in reverse[target]:
            if m not in distance:distance[m]=distance[target]+1;queue.append(m)
    assert len(distance)==len(states) and max(distance.values())<=n//2
    return {'name':name,'vertices':n,'edges':len(edges),'matchings':len(states),'full_matchings':len(full),
            'channels':dict(counts),'max_events_in_constructed_filling_path':longest_prescribed,
            'max_shortest_distance_to_full':max(distance.values())}


def graph_controls():
    possible=list(it.combinations(range(4),2));small=[]
    for mask in range(1<<len(possible)):
        edges={e for j,e in enumerate(possible) if mask&(1<<j)}
        if any(len(m)==2 for m in all_matchings(4,edges)):
            small.append(inspect_graph(4,edges,f'four_vertex_mask_{mask}'))
    assert len(small)==37
    cube_vertices=list(it.product(range(2),repeat=3))
    cube={edge(i,j) for i,x in enumerate(cube_vertices) for j,y in enumerate(cube_vertices)
          if i<j and sum(abs(a-b) for a,b in zip(x,y))==1}
    prism={edge(i,(i+1)%3) for i in range(3)}|{edge(i+3,(i+1)%3+3) for i in range(3)}|{(i,i+3) for i in range(3)}
    triangle_leaves={(0,1),(1,2),(0,2),(0,3),(1,4),(2,5)}
    ladder={(i,i+1) for i in range(4)}|{(i+5,i+6) for i in range(4)}|{(i,i+5) for i in range(5)}
    fixtures=[(6,set(it.combinations(range(6),2)),'complete_K6'),
              (6,{(i,j) for i in range(3) for j in range(3,6)},'complete_bipartite_K3_3'),
              (6,prism,'triangular_prism'),(6,triangle_leaves,'triangle_with_three_leaves'),
              (10,{edge(i,(i+1)%10) for i in range(10)},'cycle_10'),(10,ladder,'ladder_2_by_5'),
              (8,cube,'reflecting_cube'),(8,{(0,1)}|{edge(i,2+(i-1)%6) for i in range(2,8)},'edge_plus_cycle_6')]
    return {'all_labeled_four_vertex_graphs_with_perfect_matching':small,
            'additional_graphs':[inspect_graph(*row) for row in fixtures]}


def finite_generator_controls():
    beta,kappa=s.symbols('beta kappa',positive=True)
    def matrix(n,edges):
        states=all_matchings(n,edges);ind={m:i for i,m in enumerate(states)};L=s.zeros(len(states))
        rewards=s.zeros(len(states),n)
        for m,i in ind.items():
            for kind,data,target in channels(m,edges):
                rate=beta if kind=='birth' else kappa
                L[i,ind[target]]+=rate
                if kind=='birth':
                    for x in data:rewards[i,x]+=beta
            L[i,i]=-sum(L[i,j] for j in range(len(states)) if j!=i)
        return states,L,rewards
    states,L,rewards=matrix(4,{(0,1),(1,2),(2,3)})
    transient=[i for i,m in enumerate(states) if len(m)<2];full=[i for i,m in enumerate(states) if len(m)==2]
    Q=L.extract(transient,transient);means=(-Q).inv()*s.ones(len(transient),1)
    absorption=(-Q).inv()*L.extract(transient,full)*s.ones(len(full),1)
    assert (absorption-s.ones(len(transient),1)).applyfunc(s.simplify)==s.zeros(len(transient),1)
    empty=transient.index(states.index(frozenset()))
    mean=s.factor(means[empty]);assert s.simplify(mean-11/(6*beta)-1/(6*kappa))==0
    local=(-Q).inv()*rewards.extract(transient,range(4))
    local_empty=[s.simplify(x) for x in local[empty,:]]
    assert local_empty==[s.Rational(5,6),s.Rational(7,6),s.Rational(7,6),s.Rational(5,6)]
    trap=states.index(frozenset({(1,2)}));remaining=[i for i in transient if i!=trap]
    zero=L.subs(kappa,0);h=(-zero.extract(remaining,remaining)).inv()*zero.extract(remaining,full)*s.ones(len(full),1)
    assert h[remaining.index(states.index(frozenset()))]==s.Rational(2,3)
    cycle_states,cycle_L,cycle_rewards=matrix(4,{(0,1),(1,2),(2,3),(0,3)})
    tr=[i for i,m in enumerate(cycle_states) if len(m)<2]
    birth_counts=(-cycle_L.extract(tr,tr)).inv()*cycle_rewards.extract(tr,range(4))
    row=birth_counts[tr.index(cycle_states.index(frozenset())),:]
    assert row.applyfunc(s.simplify)==s.ones(1,4)
    no_perfect=all_matchings(3,{(0,1),(1,2)})
    assert max(map(len,no_perfect))==1
    return {'path4':{'mean_filling_time_from_empty':str(mean),'full_packing_probability_positive_kappa':'1',
                     'full_packing_probability_kappa_zero':'2/3','expected_site_birth_counts':list(map(str,local_empty))},
            'cycle4':{'expected_site_birth_counts':['1']*4},
            'no_perfect_matching_countercontrol':{'graph':'path3','max_records':2,'vertices':3}}


def neg(v):return tuple(-x for x in v)
def ntag(t):return (F(2*t,1+t*t),F(1-t*t,1+t*t),F(0))
def adjacent(x,y):return sum(abs(a-b) for a,b in zip(x,y))==1


def marked_matching(records):
    assert len({identity for identity,n in records.values()})==len(records)
    tags={n:x for x,(_,n) in records.items()};assert len(tags)==len(records)
    out=set()
    for x,(identity,n) in records.items():
        assert sum(a*a for a in n)==1
        y=tags.get(neg(n));assert y is not None and adjacent(x,y)
        out.add(edge(x,y))
    return frozenset(out)


def fixture_birth(records,a,b,t):
    assert a not in records and b not in records and adjacent(a,b)
    out=dict(records);identity=max([v[0] for v in records.values()]+[0])+1
    out[a]=(identity,ntag(t));out[b]=(identity+1,neg(ntag(t)))
    return out


def slide(records,a,b,c):
    assert a in records and b in records and c not in records
    assert adjacent(a,b) and adjacent(b,c) and records[a][1]==neg(records[b][1])
    out=dict(records);out.pop(a);out.pop(b);out[b]=records[a];out[c]=records[b]
    return out


def permanence(old,new):
    old_by_id={identity:(x,n) for x,(identity,n) in old.items()}
    new_by_id={identity:(x,n) for x,(identity,n) in new.items()}
    assert old_by_id.keys()<=new_by_id.keys()
    moved=[]
    for identity,(x,n) in old_by_id.items():
        y,content=new_by_id[identity];assert n==content
        if x!=y:assert adjacent(x,y);moved.append([identity,x,y])
    return moved


def marked_controls():
    origin=(0,0,0);x=(1,0,0);xx=(2,0,0);left=(-1,0,0);turn=(2,1,0)
    initial=fixture_birth({},origin,x,1);after=slide(initial,origin,x,xx)
    assert slide(after,xx,x,origin)==initial
    first_motion=permanence(initial,after);assert len(first_motion)==2
    reborn=fixture_birth(after,left,origin,2);turned=slide(reborn,x,xx,turn)
    assert len(permanence(reborn,turned))==2
    for state in [initial,after,reborn,turned]:marked_matching(state)
    assert len(turned)==4 and initial[origin][0] in {i for i,n in turned.values()}
    square=[(0,0,0),(1,0,0),(1,1,0),(0,1,0)]
    base=fixture_birth({},square[0],square[1],1);base=fixture_birth(base,square[2],square[3],2)
    def rotate(state,sign):return {square[(j+sign)%4]:state[square[j]] for j in range(4)}
    cw,ccw=rotate(base,1),rotate(base,-1)
    assert cw!=ccw and marked_matching(cw)==marked_matching(ccw)!=marked_matching(base)
    assert rotate(cw,-1)==rotate(ccw,1)==base
    assert len(permanence(base,cw))==len(permanence(base,ccw))==4
    # The earlier reflecting-cube three-direction cage now has a turning escape.
    cage={}
    for t,(a,b) in enumerate([((1,0,0),(1,1,0)),((0,1,0),(0,1,1)),((0,0,1),(1,0,1))],1):
        cage=fixture_birth(cage,a,b,t)
    escaped=slide(cage,(1,1,0),(1,0,0),(0,0,0));full=fixture_birth(escaped,(1,1,0),(1,1,1),4)
    assert len(permanence(cage,escaped))==2 and len(full)==8
    marked_matching(full)
    def axes(state):return dict(Counter(next(j for j in range(3) if a[j]!=b[j]) for a,b in marked_matching(state)))
    assert axes(cage)=={0:1,1:1,2:1} and axes(escaped)=={0:2,2:1} and axes(full)=={0:2,2:2}
    return {'site_reuse':{'site':origin,'births_at_site':2,'old_records_preserved':True,'first_slide':first_motion},
            'plaquette':{'distinct_marked_channels':2,'same_geometric_target':True,'projected_rate':'2 nu','both_exact_inverses':True},
            'reflecting_cube_turn':{'records_before_after':[6,8],'old_records_moved_before_birth':2,
                                    'axis_counts':[axes(cage),axes(escaped),axes(full)]}}


def birth_and_projector_controls():
    theta,phi=s.symbols('theta phi',real=True)
    n=s.Matrix([s.sin(theta)*s.cos(phi),s.sin(theta)*s.sin(phi),s.cos(theta)])
    integrate=lambda f:s.simplify(s.integrate(s.integrate(f*s.sin(theta),(phi,0,2*s.pi)),(theta,0,s.pi))/(4*s.pi))
    assert integrate(1)==1 and all(integrate(n[j])==0 for j in range(3))
    assert all(integrate(n[i]*n[j])==(s.Rational(1,3) if i==j else 0) for i in range(3) for j in range(3))
    directions=[tuple(sign if k==i else 0 for k in range(3)) for i,sign in it.product(range(3),(-1,1))]
    eps=F(3,5);subsets=[]
    for mask in range(1,64):
        D=[d for j,d in enumerate(directions) if mask&(1<<j)];r=len(D)
        avg=tuple(sum(d[j] for d in D)/F(r) for j in range(3))
        assert sum(abs(z) for z in avg)<=1
        subsets.append({'mask':mask,'r':r,'conditional_mean_n':[str(eps*a/3) for a in avg]})
    rotations=[]
    for perm,signs in it.product(it.permutations(range(3)),it.product((-1,1),repeat=3)):
        R=s.zeros(3)
        for j in range(3):R[j,perm[j]]=signs[j]
        if R.det()==1:rotations.append(R)
    assert len(rotations)==24
    pauli=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
    for t in range(1,7):
        tag=s.Matrix([s.Rational(x.numerator,x.denominator) for x in ntag(t)])
        P=(s.eye(2)+sum((tag[j]*pauli[j] for j in range(3)),s.zeros(2)))/2
        assert (P*P-P).applyfunc(s.simplify)==s.zeros(2) and s.trace(P)==1 and P.conjugate().T==P
        assert (P*(s.eye(2)-P)).applyfunc(s.simplify)==s.zeros(2)
        for R in rotations:
            assert (R*tag).dot(R*tag)==1
            for d in directions:
                d=s.Matrix(d)
                assert (R*tag).dot(R*d)==tag.dot(d)
                assert (-tag).dot(-d)==tag.dot(d)
    pz=s.diag(1,0);minus_z=s.diag(0,1);px=s.Matrix([[1,1],[1,1]])/2
    overlap=s.trace(s.kronecker_product(pz,minus_z)*s.kronecker_product(pz,px))
    assert overlap==s.Rational(1,2)
    return {'spherical_integrals':'E n=0; E n_i n_j=delta_ij/3','vacant_neighbor_subsets':subsets,
            'proper_cubic_rotations':24,'exact_pure_projector_fixtures':6,
            'density_lower_bound':'(1-|epsilon|)/(4*pi)>0','site_hazard':'beta*r_x',
            'empty_neighbor_conditional_rule':'unused because site hazard is zero',
            'local_quantum_recognition_countercontrol':{'antipodal_input':'P_z tensor P_-z','nonpartner_input':'P_z tensor P_x','overlap_trace':str(overlap),'consequence':'No perfect deterministic discrimination of these unknown physical-input alternatives without extra information.'}}


def run():return {'birth_and_projectors':birth_and_projector_controls(),'marked_moves':marked_controls(),
                  'finite_graphs':graph_controls(),'finite_generators':finite_generator_controls()}


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,required=True);args=parser.parse_args()
    result=run();args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='birth_and_projectors'},indent=2))
    print(json.dumps({k:v for k,v in result['birth_and_projectors'].items() if k!='vacant_neighbor_subsets'},indent=2))
    print('PASS: independent local/marked, all-graph augmentation and finite-generator controls.')
