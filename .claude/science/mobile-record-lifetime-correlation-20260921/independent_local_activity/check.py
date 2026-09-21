#!/usr/bin/env python3
"""Exact finite checks for vacancy drift, repeated births, and tagged hops."""
from fractions import Fraction as F
from itertools import product
from math import prod
from pathlib import Path
import json


def solve(matrix,rhs):
    """Small exact Gaussian elimination, with multiple right-hand sides."""
    n=len(matrix);q=len(rhs[0])
    aug=[list(map(F,row))+list(map(F,rhs[i])) for i,row in enumerate(matrix)]
    for col in range(n):
        pivot=next(i for i in range(col,n) if aug[i][col])
        aug[col],aug[pivot]=aug[pivot],aug[col]
        divisor=aug[col][col]
        aug[col]=[x/divisor for x in aug[col]]
        for i in range(n):
            if i!=col and aug[i][col]:
                factor=aug[i][col]
                aug[i]=[a-factor*b for a,b in zip(aug[i],aug[col])]
    return [row[n:n+q] for row in aug]


def construct(n,edges,W,epsilon,kappa):
    adj=[[] for _ in range(n)]
    for x,y in edges:
        adj[x].append(y);adj[y].append(x)
    states=list(product(range(-1,6),repeat=n));index={s:i for i,s in enumerate(states)}
    weights=[prod(W[s[x]][s[y]] for x,y in edges if s[x]>=0 and s[y]>=0) for s in states]
    rows=[];rewards=[];birth_channels=[]
    for i,s in enumerate(states):
        row={};birth=[F(0)]*n;depart=[F(0)]*n;arrive=[F(0)]*n;channels=[]
        for x,y in edges:
            if (s[x]<0)!=(s[y]<0):
                t=list(s);t[x],t[y]=t[y],t[x];j=index[tuple(t)]
                rate=kappa*weights[j]/(weights[i]+weights[j])
                row[j]=row.get(j,F(0))+rate
                source,dest=(x,y) if s[x]>=0 else (y,x)
                depart[source]+=rate;arrive[dest]+=rate
        for x in range(n):
            if s[x]<0:
                for a in range(6):
                    t=list(s);t[x]=a;j=index[tuple(t)]
                    rate=epsilon*prod(W[a][s[y]] for y in adj[x] if s[y]>=0)
                    row[j]=row.get(j,F(0))+rate
                    birth[x]+=rate;channels.append((x,j,rate))
        row[i]=-sum(row.values())
        assert sum(row.values())==0
        rows.append(row);rewards.append((birth,depart,arrive));birth_channels.append(channels)
    return states,index,rows,rewards,birth_channels,adj


def drift_checks(name,W,n=3):
    edges=[(x,(x+1)%n) for x in range(n)];epsilon=F(1,7);kappa=F(2,3)
    states,index,rows,rewards,channels,adj=construct(n,edges,W,epsilon,kappa)
    z=max(map(len,adj));lo=min(F(1),min(map(min,W)));hi=max(F(1),max(map(max,W)))
    alpha=6*epsilon*lo**z;beta=6*epsilon*hi**z
    for i,s in enumerate(states):
        vacancy=[F(a<0) for a in s]
        birth,depart,arrive=rewards[i]
        for x in range(n):
            direct=sum(rate*(F(states[j][x]<0)-vacancy[x]) for j,rate in rows[i].items())
            assert direct==depart[x]-arrive[x]-birth[x]
            assert alpha*vacancy[x]<=birth[x]<=beta*vacancy[x]
            assert depart[x]<=kappa*sum(vacancy[y] for y in adj[x])
            assert arrive[x]<=z*kappa*vacancy[x]
        global_drift=sum(rate*(sum(a<0 for a in states[j])-sum(vacancy))
                         for j,rate in rows[i].items())
        assert global_drift==-sum(birth)
    # Correlated translation-invariant laws, including non-reflection-symmetric
    # ordered content orbits. No independence of occupied contents is assumed.
    orbits=[]
    seeds=([(-1,-1,-1),(-1,-1,0),(-1,0,1),(-1,0,2),(0,1,2)] if n==3
           else [(-1,-1,-1,-1),(-1,-1,0,1),(-1,0,1,2),(0,1,2,3)])
    for seed in seeds:
        orbit={seed[k:]+seed[:k] for k in range(n)}
        size=len(orbit)
        v=sum(F(s[0]<0) for s in orbit)/size
        birth=sum(rewards[index[s]][0][0] for s in orbit)/size
        depart=sum(rewards[index[s]][1][0] for s in orbit)/size
        arrive=sum(rewards[index[s]][2][0] for s in orbit)/size
        assert depart==arrive
        assert alpha*v<=birth<=beta*v
        edge_flux=F(0)
        for s in orbit:
            if (s[0]<0)!=(s[1]<0):
                t=list(s);t[0],t[1]=t[1],t[0]
                rate=rows[index[s]][index[tuple(t)]]
                edge_flux+=rate*(F(s[1]<0)-F(s[0]<0))/size
        if n==4 and seed==(-1,0,1,2):
            assert edge_flux!=0
        orbits.append({'seed':seed,'vacancy_density':str(v),'birth_rate_at_origin':str(birth),
                       'departure_rate':str(depart),'arrival_rate':str(arrive),
                       'vacancy_density_derivative':str(-birth),
                       'individual_edge_vacancy_flux':str(edge_flux)})
    return {'name':name,'states':len(states),'alpha':str(alpha),'beta':str(beta),'orbits':orbits}


def two_site_absorption(epsilon,kappa):
    W=[[F(1)]*6 for _ in range(6)]
    states,index,rows,rewards,channels,adj=construct(2,[(0,1)],W,epsilon,kappa)
    transient=[i for i,s in enumerate(states) if -1 in s]
    position={i:j for j,i in enumerate(transient)}
    matrix=[[-rows[i].get(j,F(0)) for j in transient] for i in transient]
    rhs=[]
    for i in transient:
        birth,depart,arrive=rewards[i]
        rhs.append([birth[0],birth[1],depart[0],arrive[0],sum(depart)])
    values=solve(matrix,rhs)
    start=position[index[(-1,-1)]]
    b0,b1,d0,a0,hops=values[start]
    assert b0==b1==1
    assert hops==kappa/(12*epsilon)
    assert d0==a0==hops/2
    # Birth-count factorial moment gives the probability of two births at site 0.
    rhs2=[]
    for i in transient:
        value=2*sum(rate*values[position[j]][0]
                    for x,j,rate in channels[i] if x==0 and j in position)
        rhs2.append([value])
    second=solve(matrix,rhs2)[start][0]
    repeated_birth_probability=second/2
    assert repeated_birth_probability==kappa/(4*(6*epsilon+kappa))
    # Until the second birth, all hops are by the first record.
    first_tag_hops=sum(values[position[index[(a,-1)]]][4] for a in range(6))/6
    assert first_tag_hops==kappa/(12*epsilon)
    origin_zero_tag_batch=first_tag_hops/2
    assert origin_zero_tag_batch==d0
    # W=1 closes the vacancy generator pointwise, not only at this initial law.
    for i,s in enumerate(states):
        for x in range(2):
            actual=sum(rate*(F(states[j][x]<0)-F(s[x]<0)) for j,rate in rows[i].items())
            expected=kappa*F(1,2)*(F(s[1-x]<0)-F(s[x]<0))-6*epsilon*F(s[x]<0)
            assert actual==expected
    geometric_ratio=(kappa/2)/(6*epsilon+kappa/2)
    assert (1-geometric_ratio)*geometric_ratio/(1-geometric_ratio**2)/2==repeated_birth_probability
    return {'epsilon':str(epsilon),'kappa':str(kappa),'transient_states':len(transient),
            'expected_births_per_site':str(b0),'expected_site_departures':str(d0),
            'expected_site_arrivals':str(a0),'expected_incident_hops':str(hops),
            'probability_two_births_at_one_site':str(repeated_birth_probability),
            'expected_first_record_lifetime_hops':str(first_tag_hops),
            'expected_lifetime_hops_all_records_originating_at_one_site':str(origin_zero_tag_batch),
            'tag_hop_geometric_continuation_probability':str(geometric_ratio)}


def main():
    axes=[[F(3,2) if a==b else F(1,2) if (a^1)==b else F(1)
           for b in range(6)] for a in range(6)]
    v=[2,-1,-1,0,0,0]
    general=[[1+F(v[a]*v[b],10) for b in range(6)] for a in range(6)]
    drift=[drift_checks('six_axis_cycle3',axes),drift_checks('general_positive_cycle3',general),
           drift_checks('general_positive_cycle4',general,n=4)]
    absorption=[two_site_absorption(e,k) for e,k in [(F(1,7),F(2,3)),(F(1),F(3)),(F(2),F(0))]]
    result={'status':'all exact checks passed','drift_checks':drift,'two_site_checks':absorption,
            'outside_hypotheses_epsilon_zero':{
                'initial_law':'one record, uniform position on a two-site periodic graph with one bond',
                'vacancy_density':'1/2 at all times',
                'successful_hop_rate':'kappa/2 at all times',
                'conclusion':'for kappa>0 the record and both sites have infinitely many hops'},
            'new_primary_calculations_read':False}
    text=json.dumps(result,indent=2)+'\n'
    (Path(__file__).parent/'RESULTS.json').write_text(text)
    print(text,end='')


if __name__=='__main__':
    main()
