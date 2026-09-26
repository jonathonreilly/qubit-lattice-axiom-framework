#!/usr/bin/env python3
"""Pre-author finite controls for the stated preparation inequalities."""
from pathlib import Path
from itertools import permutations,product,combinations
from collections import deque,Counter
from fractions import Fraction as F
import json,math,random
import numpy as np
import sympy as sp
from scipy.linalg import expm

OUT=Path(__file__).resolve().parent

def swap(s,i,j):
    t=list(s);t[i],t[j]=t[j],t[i];return tuple(t)

def sector(values):return sorted(set(permutations(values)))

def laplacian(states,edges):
    index={s:i for i,s in enumerate(states)};l=sp.zeros(len(states))
    for a,s in enumerate(states):
        for u,v in edges:
            b=index[swap(s,u,v)]
            if b!=a:l[a,a]+=1;l[a,b]-=1
    return l

def psd_on_mean_zero(l,g):
    n=l.rows
    if n==1:return {'nontrivial_dimension':0,'minimum_LDL_pivot':None}
    basis=sp.zeros(n,n-1)
    for i in range(n-1):basis[i,i]=1;basis[n-1,i]=-1
    test=basis.T*(l-g*sp.eye(n))*basis
    lower,diag=test.LDLdecomposition(hermitian=False)
    assert lower*diag*lower.T==test
    assert all(diag[i,i]>0 for i in range(n-1))
    return {'nontrivial_dimension':n-1,'minimum_LDL_pivot':str(min(diag[i,i] for i in range(n-1)))}

def conditional_coupling():
    rows=[]
    for k in range(2,6):
        ss=list(permutations(range(k)));n=len(ss)
        for i in range(k):
            def f(s):return sum((j+1)*s[j]**2 for j in range(k))+7*int(s[0]<s[-1])
            values={s:f(s) for s in ss}
            means=[sum(F(values[s]) for s in ss if s[i]==a)/(n//k) for a in range(k)]
            mean=sum(means)/k;var=sum((a-mean)**2 for a in means)/k
            energy=sum(F((values[swap(s,i,j)]-values[s])**2,2*n)
                       for s in ss for j in range(k) if j!=i)
            assert var<=energy/k
            # This special f depends only on sigma(i), making the coefficient
            # 1/K in the conditional-mean inequality exact.
            indicator={s:int(s[i]==0) for s in ss}
            indenergy=sum(F((indicator[swap(s,i,j)]-indicator[s])**2,2*n)
                          for s in ss for j in range(k) if j!=i)
            indvar=F(k-1,k*k)
            assert indvar==indenergy/k and indvar>indenergy/(k+1)
        all_l=laplacian(ss,list(combinations(range(k),2)))
        # The larger K=5 control above checks the conditional inequality; keep
        # exact matrix certificates bounded to the 24-state K=4 case.
        cert=psd_on_mean_zero(all_l,sp.Rational(k,2)) if k<=4 else None
        rows.append({'K':k,'distinct_label_states':n,'positions_checked':k,
                     'conditional_indicator_ratio':'1/'+str(k),'complete_bound_certificate':cert})
    return rows

def paths(k,edges):
    adjacency=[[] for _ in range(k)]
    for a,b in edges:adjacency[a].append(b);adjacency[b].append(a)
    result={}
    for start in range(k):
        parent={start:None};queue=deque([start])
        while queue:
            x=queue.popleft()
            for y in adjacency[x]:
                if y not in parent:parent[y]=x;queue.append(y)
        assert len(parent)==k
        for end in range(start+1,k):
            path=[end]
            while path[-1]!=start:path.append(parent[path[-1]])
            result[start,end]=path[::-1]
    return result

def graph_comparison():
    choices=[('path4',4,[(0,1),(1,2),(2,3)],(0,1,2,3)),
             ('star4',4,[(0,1),(0,2),(0,3)],(0,0,1,2)),
             ('diamond4',4,[(0,1),(0,2),(1,2),(1,3),(2,3)],(0,0,1,1)),
             ('triangle_with_bridge_tail5',5,[(0,1),(1,2),(2,0),(2,3),(3,4)],(0,0,0,1,2)),
             ('cycle5',5,[(i,(i+1)%5) for i in range(5)],(0,0,0,1,2))]
    rows=[]
    for name,k,edges,colors in choices:
        route=paths(k,edges);diam=max(len(v)-1 for v in route.values());usage=Counter();checks=0
        for (a,b),path in route.items():
            forward=list(zip(path[:-1],path[1:]));word=forward+forward[-2::-1]
            assert len(word)==2*len(path)-3 and len(word)<=2*diam-1
            occurrences=Counter(tuple(sorted(e)) for e in word)
            assert max(occurrences.values())<=2;usage.update(occurrences)
            for s in permutations(range(k)):
                actual=s
                for x,y in word:actual=swap(actual,x,y)
                assert actual==swap(s,a,b);checks+=1
        assert max(usage.values())<=k*(k-1)
        ss=sector(colors);l=laplacian(ss,edges)
        gap=sp.Rational(1,2*(2*diam-1)*(k-1));cert=psd_on_mean_zero(l,gap)
        rows.append({'graph':name,'K':k,'diameter':diam,'color_sector_size':len(ss),
                     'immutable_label_word_checks':checks,'max_reference_edge_occurrences':max(usage.values()),
                     'displayed_unit_rate_gap_lower_bound':str(gap),'exact_certificate':cert})
    # Missing connectedness is consequential: homogeneous components cannot
    # move their colors to the other component.
    ss=sector((0,0,1,1));l=laplacian(ss,[(0,1),(2,3)])
    idx=ss.index((0,0,1,1));assert l.row(idx)==sp.zeros(1,len(ss))
    return rows,{'disconnected_absorbing_state':(0,0,1,1),'sector_size':6,
                 'TV_from_uniform_for_all_times':'5/6'}

def contracted_geometry():
    n=8;xyz=list(product(range(n),repeat=3));black=[x for x in xyz if sum(x)%2==0];k=len(black)
    def move(x,i,sign=1):return tuple((x[j]+(sign if i==j else 0))%n for j in range(3))
    rows=[]
    for name in ['winding','columnar','irregular']:
        partner={};initial=black if name=='winding' else [x for x in xyz if x[0]%2==0]
        for x in initial:y=move(x,0);partner[x]=y;partner[y]=x
        accepted=0
        if name=='irregular':
            rng=random.Random(602117)
            for _ in range(8*n**3):
                a=rng.choice(xyz);i,j=rng.sample(range(3),2);b=move(a,i);d=move(a,j);c=move(b,j)
                if partner[a]==b and partner[d]==c:pairs=[(a,d),(b,c)]
                elif partner[a]==d and partner[b]==c:pairs=[(a,b),(d,c)]
                else:continue
                for x,y in pairs:partner[x]=y;partner[y]=x
                accepted+=1
        owner={}
        for i,x in enumerate(black):owner[x]=i;owner[partner[x]]=i
        edges=set()
        # Contract original physical NN edges directly, rather than deriving H
        # from an author's routing array.
        for x in xyz:
            for axis in range(3):
                a,b=owner[x],owner[move(x,axis)]
                if a!=b:edges.add(tuple(sorted((a,b))))
        route=paths(k,sorted(edges));diam=max(len(p)-1 for p in route.values())
        assert diam<=3*n//2
        rows.append({'matching':name,'N':n,'K':k,'simple_contracted_edges':len(edges),
                     'exact_contracted_diameter':diam,'physical_diameter_bound':3*n//2,
                     'accepted_fixture_flips':accepted})
    return rows

def nonreversible():
    e=[tuple(s if j==i else 0 for j in range(3)) for i in range(3) for s in [1,-1]]+[(0,0,0)]*8
    b=[(0,0,0)]*6+list(product([-1,1],repeat=3))
    def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
    def tensor(a,c):return cross(e[a],b[c])[2]+cross(e[c],b[a])[2]
    states=sector((0,2,6,11));idx={s:i for i,s in enumerate(states)};q=sp.zeros(len(states))
    k0=sp.Rational(5,4);gamma=sp.Rational(3,4)
    for i,s in enumerate(states):
        hsum=0
        for u in range(4):
            l,a,c,r=[s[(u+v)%4] for v in [-1,0,1,2]]
            h2=tensor(l,a)+tensor(a,r)-tensor(l,c)-tensor(c,r);hsum+=h2
            rate=k0/2+gamma*h2/8;assert rate>0
            j=idx[swap(s,u,(u+1)%4)];q[i,j]+=rate;q[i,i]-=rate
        assert hsum==0
    assert q!=q.T and q*sp.ones(len(states),1)==sp.zeros(len(states),1)
    assert sp.ones(1,len(states))*q==sp.zeros(1,len(states))
    unit=laplacian(states,[(0,1),(1,2),(2,3),(3,0)])
    s=(q+q.T)/2;assert -s==k0*unit/2
    gap=k0/sp.Integer(4*(2*2-1)*(4-1));cert=psd_on_mean_zero(-s,gap)
    f=sp.Matrix([2*i-23 for i in range(24)])
    derivative=2*(f.T*q.T*f)[0]/24
    assert derivative==2*(f.T*s*f)[0]/24
    samples=[]
    for time in [.1,1.,4.,20.,100.]:
        law=expm(np.array(q,dtype=float)*time)[0];centered=24*law-1
        l2=float(np.mean(centered**2));tv=float(np.sum(abs(law-1/24))/2)
        l2_bound=23*math.exp(-2*float(gap)*time);tv_bound=math.sqrt(23)/2*math.exp(-float(gap)*time)
        assert l2<=l2_bound+1e-12 and tv<=tv_bound+1e-12
        samples.append({'time':time,'centered_density_L2_squared':l2,'displayed_L2_bound':l2_bound,
                        'TV':tv,'displayed_TV_bound':tv_bound})
    return {'states':24,'k0':str(k0),'gamma':str(gamma),'nonreversible':True,
            'symmetric_part_exactly_k0_over_2_graph_swaps':True,'comparison_gap':str(gap),
            'exact_LDL_certificate':cert,'density_energy_derivative':str(derivative),'samples':samples}

def probability_transfer():
    k=3;ss=list(product(range(14),repeat=k));groups={}
    for s in ss:
        counts=tuple(s.count(a) for a in range(14));groups.setdefault(counts,[]).append(s)
    total=F(0)
    for counts,states in groups.items():
        size=math.factorial(k)
        for c in counts:size//=math.factorial(c)
        assert size==len(states)
        monomial=math.prod(F(a+1,105)**c for a,c in enumerate(counts))
        sector_mass=size*monomial;total+=sector_mass
        for s in states:assert sector_mass/size==math.prod(F(a+1,105) for a in s)
    assert total==1
    # Counts are Binomial(2,1/2), but their correlation with M prevents the
    # claimed JOINT product law despite the correct unconditioned color law.
    actual={(0,(0,0)):F(1,4),(0,(1,1)):F(1,4),(1,(0,1)):F(1,4),(1,(1,0)):F(1,4)}
    tv=sum(abs(actual.get((m,s),F(0))-F(1,8)) for m in [0,1] for s in product([0,1],repeat=2))/2
    assert tv==F(1,2)
    schedule=[]
    for n in [8,16,32,64,128]:
        pairs=n**3//2;g=sp.Rational(1,4*(3*n-1)*(pairs-1));eps=sp.Rational(1,n**4)
        bracket=sp.Rational(pairs,2)*sp.log(14)-sp.log(2)-sp.log(eps)
        prep=bracket/g
        assert sp.expand(-sp.log(2)+sp.Rational(pairs,2)*sp.log(14)-g*prep-sp.log(eps))==0
        assert pairs*eps==sp.Rational(1,2*n)
        schedule.append({'N':n,'K':pairs,'g_N_at_k0_1':str(g),'epsilon_N':str(eps),
                         'K_times_epsilon_N':str(pairs*eps),'exact_log_TV_bound_equals_log_epsilon':True})
    return {'fourteen_label_K3_states':len(ss),'multinomial_sectors':len(groups),
            'all_sector_mixture_weights_equal_product_exactly':True,
            'missing_count_geometry_independence_counterexample_TV':str(tv),
            'wrong_counts_counterexample':'All-one-color sector stays there; TV from iid p is 1-p_a^K.',
            'schedule':schedule,'TV_only_countercontrol':'Two-point laws differing by epsilon and a [0,K] test can differ in expectation by K epsilon; epsilon=o(1) alone is insufficient.'}

if __name__=='__main__':
    cc=conditional_coupling();print('conditional coupling/complete transpositions done',flush=True)
    graphs,counter=graph_comparison();print('graph path/Dirichlet comparisons done',flush=True)
    geo=contracted_geometry();print('contracted torus controls done',flush=True)
    nr=nonreversible();print('nonreversible contraction done',flush=True)
    p=probability_transfer();print('sector mixture and schedule done',flush=True)
    result={'scope':'Independent before any new author checker/results; exact arithmetic except explicitly numeric semigroup evaluations.',
            'conditional_coupling':cc,'connected_graphs':graphs,'disconnected_countercontrol':counter,
            'contracted_geometry':geo,'nonreversible':nr,'probability_transfer':p}
    (OUT/'INDEPENDENT_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'graphs':len(graphs),'nonreversible_states':nr['states'],
                      'joint_law_countercontrol_TV':p['missing_count_geometry_independence_counterexample_TV']},indent=2))
