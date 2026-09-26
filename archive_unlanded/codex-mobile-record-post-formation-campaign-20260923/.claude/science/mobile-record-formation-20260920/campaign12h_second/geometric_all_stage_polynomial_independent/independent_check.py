#!/usr/bin/env python3
"""Independent padded-graph, killed-operator and coupling controls.

No author module, result or fixture is imported. Output stays beside this
script; an existing result is not overwritten.
"""
from pathlib import Path
from itertools import combinations,product
from collections import Counter,defaultdict
from fractions import Fraction as F
import json,math
import numpy as np
import sympy as sp

OUT=Path(__file__).resolve().parent

def edge(a,b):return tuple(sorted((a,b)))
def matching(edges):return tuple(sorted(edges))

def enumerate_rank(left,right,edges,rank):
    neighbor={u:sorted(v if u==w else w for w,v in edges if u in (w,v)) for u in left}
    answer=[]
    def visit(i,used,chosen):
        if len(chosen)==rank:answer.append(matching(chosen));return
        if i==len(left) or len(chosen)+len(left)-i<rank:return
        u=left[i];visit(i+1,used,chosen)
        for v in neighbor[u]:
            if v not in used:visit(i+1,used|{v},chosen+[edge(u,v)])
    visit(0,set(),[])
    assert len(answer)==len(set(answer))
    return sorted(answer)

def slides(M,edges):
    partner={x:y for a,b in M for x,y in [(a,b),(b,a)]}
    out=set()
    for a,b in edges:
        if (a in partner)==(b in partner):continue
        free,covered=(a,b) if a not in partner else (b,a)
        old=edge(covered,partner[covered]);new=edge(free,covered)
        out.add(matching(set(M)-{old}|{new}))
    return out

def graph_laplacian(states,outgoing):
    index={M:i for i,M in enumerate(states)};edges=set()
    for i,M in enumerate(states):
        for T in outgoing(M):
            assert T in index
            assert M in outgoing(T)
            if i!=index[T]:edges.add(tuple(sorted((i,index[T]))))
    L=np.zeros((len(states),len(states)),dtype=np.int64)
    for a,b in edges:L[a,a]+=1;L[b,b]+=1;L[a,b]-=1;L[b,a]-=1
    seen={0};todo=[0]
    while todo:
        i=todo.pop()
        for j in np.flatnonzero(L[i]<0):
            if int(j) not in seen:seen.add(int(j));todo.append(int(j))
    return L,sorted(edges),len(seen)==len(states)

def original_cases():
    return [
        ('path4',2,[(0,2),(1,2),(1,3)]),
        ('path6',3,[(0,3),(1,3),(1,4),(2,4),(2,5)]),
        ('cycle6',3,[(0,3),(1,3),(1,4),(2,4),(2,5),(0,5)]),
        ('bridged_squares8',4,[*(product([0,1],[4,5])),*(product([2,3],[6,7])),(1,6)]),
        ('complete_bipartite4',4,list(product(range(4),range(4,8))))]

def padded_case(name,K,E,j,layers):
    E=sorted(map(lambda e:edge(*e),E));k=j+1;h=K-k;f0=math.factorial(h)**2
    dl=list(range(2*K,2*K+h));dr=list(range(2*K+h,2*K+2*h))
    left=list(range(K))+dl;right=list(range(K,2*K))+dr
    HE=sorted(set(E)|{edge(x,y) for x in dl for y in range(K,2*K)}|
              {edge(x,y) for x in dr for y in range(K)})
    mh=len(HE);assert mh==len(E)+2*h*K
    full=enumerate_rank(left,right,HE,K+h);near=enumerate_rank(left,right,HE,K+h-1)
    states=near+full;index={M:i for i,M in enumerate(states)}
    projection={M:matching(e for e in M if max(e)<2*K) for M in states}
    fibers=Counter();goodfib=Counter();badstates=[]
    for M in states:
        P=projection[M];covered={x for e in M for x in e}
        if M in index and len(M)==K+h:kind='perfect'
        else:
            holes=[x for x in left+right if x not in covered]
            assert len(holes)==2 and sum(x in left for x in holes)==1
            original=sum(x<2*K for x in holes)
            kind={2:'original_original',1:'mixed',0:'dummy_dummy'}[original]
        fibers[(P,kind)]+=1
        if len(P)<=k:goodfib[P]+=1
        else:badstates.append(M)
    for P in layers[j]:assert fibers[P,'original_original']==(h+1)**2*f0
    for P in layers[k]:
        assert fibers[P,'perfect']==f0 and fibers[P,'mixed']==2*h*f0
    for U in layers[k+1] if k<K else []:assert fibers[U,'dummy_dummy']==f0
    assert len(near)==f0*((h+1)**2*len(layers[j])+2*h*len(layers[k])+(len(layers[k+1]) if k<K else 0))
    R=F(len(layers[K-1]),len(layers[K]));rh=F(len(near),len(full))
    exactrh=(h+1)**2*F(len(layers[j]),len(layers[k]))+2*h+F(len(layers[k+1]) if k<K else 0,len(layers[k]))
    upper=(h+1)*R+2*h+F(len(E),k+1)
    assert rh==exactrh<=upper

    def hout(M):
        out=slides(M,HE)
        if len(M)==K+h:out={matching(set(M)-{e}) for e in M}
        else:
            occupied={x for e in M for x in e}
            out|={matching(set(M)|{e}) for e in HE if not set(e)&occupied}
        return out
    transitions=set();degree=[];badexit=Counter();signatures=defaultdict(set)
    for M in states:
        dest=hout(M);degree.append(len(dest));assert len(dest)<=mh
        signature=Counter(projection[T] for T in dest if projection[T]!=projection[M])
        if len(projection[M])<=k:signatures[projection[M]].add(tuple(sorted(signature.items())))
        for T in dest:
            assert T in index and M in hout(T)
            transitions.add(tuple(sorted((index[M],index[T]))))
            P,U=projection[M],projection[T]
            if len(P)==k+1:
                if len(U)==k+1:assert P==U
                else:
                    assert len(U)==k and set(U)<set(P)
                    badexit[P,U]+=1
    for U in layers[k+1] if k<K else []:
        for e in U:assert badexit[U,matching(set(U)-{e})]==2*f0
    B=layers[j]+layers[k];bi={M:i for i,M in enumerate(B)};nb=len(B);scale=k+1
    bedges=[]
    for a,b in combinations(range(nb),2):
        x,y=set(B[a]),set(B[b]);different=x^y
        if (len(x)==len(y) and len(different)==2) or (len(x)!=len(y) and len(different)==1):bedges.append((a,b))
    LB=np.zeros((nb,nb),dtype=np.int64)
    for a,b in bedges:LB[a,a]+=1;LB[b,b]+=1;LB[a,b]-=1;LB[b,a]-=1
    table=np.zeros((len(states),nb),dtype=np.int64)
    for i,M in enumerate(states):
        P=projection[M]
        if len(P)<=k:table[i,bi[P]]=scale
        else:
            for e in P:table[i,bi[matching(set(P)-{e})]]=1
    assert np.all(table.sum(axis=1)==scale)
    energy=np.zeros((nb,nb),dtype=np.int64)
    for a,b in transitions:
        va=table[a]-table[b];support=np.flatnonzero(va)
        energy[np.ix_(support,support)]+=np.outer(va[support],va[support])
        P,U=projection[states[a]],projection[states[b]]
        if len(P)<=k and len(U)<=k and P!=U:assert LB[bi[P],bi[U]]==-1
    minimum=(2*h+1)*f0;maximum=(h+1)**2*f0
    assert min(goodfib.values())==minimum and max(goodfib.values())==maximum
    deficit=minimum*mh*(h+2)*scale**2*LB-energy
    assert np.all(deficit.sum(axis=1)==0)
    assert np.max(deficit-np.diag(np.diag(deficit)))<=0
    # Exact nonnegative conductances prove this finite matrix inequality for
    # every real/complex g, not only the random quadratic vectors below.
    ratios=[F(int(-energy[a,b]),minimum*mh*(h+2)*scale**2) for a,b in bedges]
    rng=np.random.default_rng(633521+K*20+j);variance_checks=0
    for g in [*np.eye(nb,dtype=np.int64),*rng.integers(-4,5,size=(8,nb))]:
        values=table@g;total=len(states)
        lhs=nb*(total*sum(int(x)**2 for x in values)-sum(map(int,values))**2)
        rhs=minimum*total*scale**2*(nb*sum(int(x)**2 for x in g)-sum(map(int,g))**2)
        assert lhs>=rhs;variance_checks+=1
    S,sedges,connected=graph_laplacian(layers[j],lambda M:slides(M,E));assert connected
    gS=float(np.linalg.eigvalsh(S.astype(float))[1]);gB=float(np.linalg.eigvalsh(LB.astype(float))[1])
    Cj=1+(2*K-2)*(len(E)+len(E)**2)*(k-1)*(k+1+2*len(E))
    assert gS+1e-12>=gB/Cj
    hatgap=None
    if len(states)<=150:
        HL=np.zeros((len(states),len(states)),dtype=np.int64)
        for a,b in transitions:HL[a,a]+=1;HL[b,b]+=1;HL[a,b]-=1;HL[b,a]-=1
        hatgap=float(np.linalg.eigvalsh(HL.astype(float))[1])
        assert hatgap+1e-12>=float(1/(256*mh*rh**4))
        assert gB+1e-12>=hatgap/(mh*(h+2))
    return dict(graph=name,K=K,rank=j,h=h,original_counts=list(map(len,layers)),
        padded_edges=mh,full_states=len(full),near_states=len(near),bad_states=len(badstates),
        f0=f0,good_fiber_minimum=minimum,good_fiber_maximum=maximum,
        R_hat=str(rh),U_j=str(upper),augmented_undirected_transitions=len(transitions),
        maximum_augmented_degree=max(degree),exact_bad_parent_exit_count=2*f0 if h else 0,
        nonlumpable_good_projection_fibers=sum(len(x)>1 for x in signatures.values()),
        maximum_exact_compressed_energy_ratio=str(max(ratios)),
        exact_energy_deficit_is_nonnegative_conductance_Laplacian=True,
        exact_variance_vector_controls=variance_checks,numerical_slide_gap=gS,
        numerical_auxiliary_gap=gB,numerical_padded_gap=hatgap,comparison_Cj=Cj)

def killed_controls(cases):
    rows=[]
    for name,K,E in cases[:4]:
        layers=[enumerate_rank(list(range(K)),list(range(K,2*K)),E,j) for j in range(K+1)]
        for j in range(1,K):
            states=layers[j];n=len(states);L,_,connected=graph_laplacian(states,lambda M:slides(M,E));assert connected
            h=[sum(not ({x for e in M for x in e}&set(e)) for e in E) for M in states]
            p=F(sum(h),n);assert p==F((j+1)*len(layers[j+1]),n)>0
            # Elementary safe gap for a connected unit-rate graph, proved in
            # the report; the actual small-matrix gap is checked separately.
            g=F(1,n*n);m=len(E)
            for beta in [F(1,11),F(1),F(7)]:
                D=sp.Matrix(L)+sp.diag(*[sp.Rational(beta*x) for x in h])
                means=D.inv()*sp.ones(n,1)
                assert all(x>0 for x in means)
                C=2/(beta*p)+(1+2*m/p)/g
                eigenvalue=float(np.linalg.eigvalsh(np.array(D,dtype=float))[0])
                assert eigenvalue+1e-12>=float(1/C)
                uniform=(1+.5*math.log(n))*float(C)
                assert max(map(float,means))<=uniform
                rows.append(dict(graph=name,rank=j,beta=str(beta),states=n,hazard_min=min(h),hazard_max=max(h),
                    exact_p=str(p),exact_conservative_gap=str(g),exact_inverse_eigenvalue_bound=str(C),
                    exact_maximum_mean=str(max(means)),displayed_uniform_mean_bound=uniform,
                    numerical_minimum_killed_eigenvalue=eigenvalue))
    a,b,H=sp.symbols('a b H',positive=True)
    D=sp.Matrix([[a,-a],[-a,a+b*H]]);mean=D.inv()*sp.ones(2,1)
    assert sp.simplify(mean[0]-(2/(b*H)+1/a))==0
    assert sp.simplify(mean[1]-2/(b*H))==0
    return dict(actual_layer_rows=rows,two_state_zero_hazard_countercontrol=[str(x) for x in mean],
        interpretation='Mean is unbounded as the conservative rate tends to zero at fixed average hazard; a uniform gap cannot be omitted. Inversions are exact rational; eigenvalue and logarithmic comparisons are floating.')

def constants_and_coupling():
    constants=[]
    for K in [256,257,500,2048,32768]:
        m=6*K;R=F(K*K,6)
        for j in sorted({1,2,K//2,K-2,K-1}):
            k=j+1;h=K-k;mh=m+2*h*K
            U=(h+1)*R+2*h+F(m,k+1)
            Cj=1+(2*K-2)*(m+m*m)*(k-1)*(k+1+2*m)
            denominator=256*mh*mh*(h+2)*U**4*Cj
            assert mh<=4*K*K and U<=K**3 and Cj<=2**11*K**5
            assert denominator<=2**23*K**22
        delta=F(3,32*K**3)
        assert 2*delta/(1-2*delta)<=F(3,13*K**3)
        assert 2*K*delta==F(3,16*K*K)
        constants.append(dict(K=K,maximum_schedule_delta=str(delta),mean_relative_bound=str(F(3,13*K**3))))
    # Exact finite-law analogue of the proof coupling. State 8 is partial;
    # the other eight states are two full geometries with two binary colors.
    q=F(1,10);alpha=F(1,8);geometry=[F(1,3),F(2,3)];pi=[F(1,4)]*4
    colored=[(1-alpha)*p+alpha*(i==0) for i,p in enumerate(pi)]
    mu=[(1-q)*geometry[g]*colored[c] for g in range(2) for c in range(4)]+[q]
    ref=[((1-q)*geometry[g]+q*(g==0))*pi[c] for g in range(2) for c in range(4)]+[F(0)]
    tv=sum(abs(a-b) for a,b in zip(mu,ref))/2
    assert tv<=q+alpha and sum(mu)==sum(ref)==1
    # A common future Markov kernel; the partial state subsequently fills.
    # Exact resolvent kernel is enough to control the TV data-processing step.
    Q=sp.zeros(9)
    for g in range(2):
        for c in range(4):
            i=4*g+c;Q[i,4*(1-g)+c]+=1
            if c in [1,2]:Q[i,4*g+(3-c)]+=2
    for c in range(4):Q[8,c]+=sp.Rational(1,4)
    for i in range(9):Q[i,i]=-sum(Q[i,j] for j in range(9) if j!=i)
    P=(sp.eye(9)-Q).inv();assert P*sp.ones(9,1)==sp.ones(9,1)
    after=(sp.Matrix(1,9,mu)-sp.Matrix(1,9,ref))*P
    aftertv=sum(abs(x) for x in after)/2;assert aftertv<=sp.Rational(tv)
    sector=[F(0),F(1,2),F(1,2),F(0)]
    sector_tv=sum(abs(x-y) for x,y in zip(sector,pi))/2;assert sector_tv==F(1,2)
    return dict(cubic_exact_arithmetic=constants,law_coupling=dict(bad_mass=str(q),good_color_mixture_weight=str(alpha),
        unconditioned_total_variation=str(tv),upper_bound=str(q+alpha),future_total_variation=str(aftertv)),
        fixed_count_countercontrol_tv=str(sector_tv),
        scope='The reference coupling is on the geometry/color projection. Extra immutable keys need not mix. Fixed count conditioning differs permanently from the multinomial mixture.')

def main():
    target=OUT/'INDEPENDENT_RESULTS.json';assert not target.exists(),'Preserve the sealed output; reproduce in a copied directory.'
    cases=original_cases();rows=[]
    for name,K,E in cases:
        layers=[enumerate_rank(list(range(K)),list(range(K,2*K)),E,j) for j in range(K+1)]
        assert layers[K]
        for j in range(1,K):
            row=padded_case(name,K,E,j,layers);rows.append(row)
            print(json.dumps({x:row[x] for x in ['graph','rank','h','full_states','near_states','maximum_exact_compressed_energy_ratio']}),flush=True)
    killed=killed_controls(cases);print('Exact killed controls completed',flush=True)
    composition=constants_and_coupling();print('Constants and unconditioned finite-law coupling completed',flush=True)
    target.write_text(json.dumps(dict(padded_cases=rows,killed_operator=killed,composition=composition,
        scope='Independent before author all-stage-polynomial controls/results. Exact enumeration and compressed forms distinguished from numerical spectral corroboration. No production replay.'),indent=2)+'\n')

if __name__=='__main__':main()
