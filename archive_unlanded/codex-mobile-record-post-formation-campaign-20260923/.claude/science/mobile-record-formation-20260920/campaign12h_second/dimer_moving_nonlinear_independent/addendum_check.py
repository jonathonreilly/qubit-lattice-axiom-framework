#!/usr/bin/env python3
"""Independent even-cube comparison and entropy/empirical rate controls."""
from pathlib import Path
from collections import Counter
from fractions import Fraction as F
import datetime,hashlib,itertools,json,math
import numpy as np
import sympy as s
import independent_check as own

HERE=Path(__file__).resolve().parent
def edge(a,b):return tuple(sorted((tuple(a),tuple(b))))
def path(a,b):
    current=list(a);answer=[tuple(current)]
    for i in range(3):
        step=1 if b[i]>current[i] else -1
        while current[i]!=b[i]:current[i]+=step;answer.append(tuple(current))
    return answer

def path_counts():
    rows=[]
    for L in (2,4,6):
        sites=list(itertools.product(range(L),repeat=3));loads=Counter()
        for a in sites:
            for b in sites:
                pp=path(a,b)
                for x,y in zip(pp,pp[1:]):loads[edge(x,y)]+=1
        for (x,y),load in loads.items():
            i=next(i for i in range(3) if x[i]!=y[i]);cut=min(x[i],y[i])+1
            assert load==2*cut*(L-cut)*L**2
        assert max(loads.values())<=L**4/2
        rows.append({'even_L':L,'ordered_pairs':len(sites)**2,'physical_edges':len(loads),
                     'maximum_path_load':max(loads.values()),'L4_over_2':L**4//2})
    return rows

def owner_word_comparison():
    N,L=48,4;M=own.Matching(N);M.make_rough(L,attempts=140,seed=418)
    origin=np.array([1,0,1]);sites=[tuple(origin+r) for r in itertools.product(range(L),repeat=3)]
    representatives={}
    for x in sorted(sites):representatives.setdefault(M.owner(x),x)
    owners=sorted(representatives,key=representatives.get);m=len(owners);ix={u:i for i,u in enumerate(owners)}
    physical_representatives={}
    for x in sites:
        for i in range(3):
            y=list(x);y[i]+=1;y=tuple(y)
            if y not in representatives.values() and y not in sites:continue
            if y not in sites:continue
            u,v=M.owner(x),M.owner(y)
            if u!=v:physical_representatives.setdefault(edge(u,v),set()).add(edge(x,y))
    assert max(map(len,physical_representatives.values()))<=2
    load=Counter();word_uses=Counter();weighted=Counter();max_word=0
    for a,b in itertools.combinations(owners,2):
        pp=path(representatives[a],representatives[b]);raw=[M.owner(x) for x in pp]
        simple=[];position={}
        for u in raw:
            if u in position:
                at=position[u]
                for old in simple[at+1:]:del position[old]
                simple=simple[:at+1]
            else:position[u]=len(simple);simple.append(u)
        assert simple[0]==a and simple[-1]==b and len(simple)<=len(pp)
        edges=[edge(x,y) for x,y in zip(simple,simple[1:])]
        assert len(edges)==len(set(edges)) and all(e in physical_representatives for e in edges)
        word=edges+edges[-2::-1];max_word=max(max_word,len(word));assert len(word)<=6*L
        values=list(range(m));expected=values.copy();expected[ix[a]],expected[ix[b]]=expected[ix[b]],expected[ix[a]]
        for x,y in word:values[ix[x]],values[ix[y]]=values[ix[y]],values[ix[x]]
        assert values==expected
        for e in edges:load[e]+=1
        for e in word:word_uses[e]+=1;weighted[e]+=len(word)
    assert max(load.values())<=L**4 and max(word_uses.values())<=2*L**4
    assert max(weighted.values())<=12*L**5
    assert m>=L**3/2
    return {'N':N,'even_L':L,'origin':origin.tolist(),'owners':m,'fixture_flips':M.flips,
            'matching_sha256':M.fixture_hash(),'endpoint_words_checked':m*(m-1)//2,
            'max_physical_representatives_per_simple_edge':max(map(len,physical_representatives.values())),
            'max_contracted_path_load':max(load.values()),'max_word_uses':max(word_uses.values()),
            'max_word_length':max_word,'exact_comparison_load':max(weighted.values()),
            'claimed_upper_comparison_coefficient':12*L**5,
            'scope':'All selected owner endpoint transpositions checked on an irregular embedded even cube; no simulated mixing or eigenvalue fit.'}

def rate_algebra():
    k=s.symbols('k',integer=True,positive=True)
    gap=s.factor(2/k-(2*(k-2)/(k*(k-1))+2/k**2))
    assert gap==2/(k**2*(k-1))
    a=s.symbols('a');exponent=s.solve(s.Eq(-a,(5*a-1)/2),a)[0];assert exponent==s.Rational(1,7)
    exponents=[-exponent,(5*exponent-1)/2,exponent-1,2*exponent-2,-1]
    assert exponents==[-s.Rational(1,7),-s.Rational(1,7),-s.Rational(6,7),-s.Rational(12,7),-1]
    rows=[]
    for L in (16,18,32,64):
        N=L**7;assert N>10*L
        scaled=F(2)+F(1,L**5)+F(1,L**11)+F(1,L**6)
        assert 2<scaled<3
        rows.append({'even_L':L,'formal_N_equals_L7':N,'N1over7_times_error_envelope':str(scaled),
                     'scope':'Arithmetic check only; no claim of sampling such volumes.'})
    return {'complete_permutation_induction_slack':str(gap),'block_balance_exponent':str(exponent),
            'five_error_exponents':[str(x) for x in exponents],'gap_lower_bound':'1/(48 L^2)',
            'rate_rows':rows,'time_supremum_exponent':'(1/7)*(2/3)=2/21'}

def empirical_controls():
    K=6;prob=[F(1,10),F(2,7),F(1,2),F(3,5),F(4,5),F(9,10)]
    phi=[F(-1),F(3,5),F(1,3),F(-2,3),F(0),F(4,5)];B=1
    atoms=[]
    for binary in itertools.product((0,1),repeat=K):
        mass=math.prod(prob[i] if x else 1-prob[i] for i,x in enumerate(binary))
        W=sum(phi[i]*(binary[i]-prob[i]) for i in range(K))/K
        Y=K*W*W/(B*B);atoms.append((mass,W,Y))
    assert sum(x[0] for x in atoms)==1
    mgf=sum(float(mass)*math.exp(float(Y)) for mass,W,Y in atoms)
    assert mgf<=3
    # An arbitrary correlated tilt tests the entropy inequality, not just its product special case.
    tilted=np.array([float(mass)*math.exp(4*float(Y)) for mass,W,Y in atoms]);tilted/=tilted.sum()
    H=float(sum(mu*math.log(mu/float(mass)) for mu,(mass,W,Y) in zip(tilted,atoms)))
    lhs=float(sum(mu*float(W*W) for mu,(mass,W,Y) in zip(tilted,atoms)))
    rhs=(H+math.log(3))*B*B/K
    assert lhs<=rhs
    # Wrong strengthening of the Hoeffding factor fails on six fair variables with weights one.
    fair_tail=F(2,2**K);good=2*math.exp(-2*K*.5**2);wrong=2*math.exp(-8*K*.5**2)
    assert float(fair_tail)<=good and float(fair_tail)>wrong
    # Time-supremum distinction: random uniform location of a periodic unit-Lipschitz triangular bump.
    x,d=s.symbols('x d',positive=True);moment=s.integrate(2*(d-x)**2,(x,0,d));assert moment==2*d**3/3
    bumps=[]
    for width in (F(1,8),F(1,16),F(1,32)):
        fixed=F(2,3)*width**3;sup=width**2
        bumps.append({'width':str(width),'each_fixed_time_second_moment':str(fixed),
                      'expected_time_supremum_square':str(sup),'sup_to_fixed_ratio':str(sup/fixed)})
    return {'signed_weight_product_mgf':mgf,'bound':3,'correlated_tilt_entropy':H,'correlated_tilt_E_W2':lhs,
            'entropy_upper_bound_E_W2':rhs,'wrong_Hoeffding_factor_countercontrol':{'actual_tail':str(fair_tail),'correct_bound':good,'incorrect_eightK_bound':wrong},
            'time_supremum_countercontrols':bumps,
            'scope':'The triangular-bump example tests what fixed-time/Lipschitz information alone implies; it is not the record process or a counterexample to the stated r^(2/3) bound.'}

def main():
    result={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'boundary':'Quantitative addendum controls independently assembled after base pre-seal, before all new author code/results.'}
    for name,fn in [('even_cube_path_counts',path_counts),('contracted_endpoint_words',owner_word_comparison),
                    ('gap_and_rate_algebra',rate_algebra),('empirical_and_time_mesh',empirical_controls)]:
        result[name]=fn();print(name+' complete',flush=True)
    result['checker_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    with (HERE/'ADDENDUM_RESULTS.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
    print('all independent addendum groups complete',flush=True)

if __name__=='__main__':main()
