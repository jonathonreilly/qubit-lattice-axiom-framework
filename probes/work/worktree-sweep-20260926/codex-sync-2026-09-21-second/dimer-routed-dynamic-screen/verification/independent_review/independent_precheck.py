#!/usr/bin/env python3
"""Independent finite controls; does not import author implementation or data."""
from pathlib import Path
from itertools import product, permutations
import json, math, random
import numpy as np
import sympy as sp
from scipy.linalg import expm

OUT = Path(__file__).resolve().parent
E = [tuple(s if j == i else 0 for j in range(3)) for i in range(3) for s in [1,-1]] + [(0,0,0)]*8
B = [(0,0,0)]*6 + list(product([-1,1], repeat=3))
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
T = [[[cross(E[a],B[b])[i]+cross(E[b],B[a])[i] for b in range(14)] for a in range(14)] for i in range(3)]

def rates_and_current():
    rows=[]
    for i in range(3):
        acc=np.zeros((14,14), dtype=np.int64); lo=100; hi=-100
        for l,a,b,r in product(range(14), repeat=4):
            h2=T[i][l][a]+T[i][a][r]-T[i][l][b]-T[i][b][r]
            lo=min(lo,h2); hi=max(hi,h2)
            num=22+5*h2
            assert 2<=num<=42
            reverse=T[i][l][b]+T[i][b][r]-T[i][l][a]-T[i][a][r]
            assert reverse == -h2 and num+(22+5*reverse)==44
            for color in (l,a,b,r):
                acc[a,color]+=num; acc[b,color]-=num
        # Product derivative of ACTUAL mean current at p_a=1/14.
        deriv=sp.Matrix(acc.tolist())/(40*14**3)
        target=sp.Matrix(T[i])/28
        assert deriv==target
        rows.append({'axis':i,'contexts':14**4,'h2_min':lo,'h2_max':hi,
                     'actual_current_derivative':'T_i/28 = A_i/2','rate_range':['1/20','21/20']})
    return rows

def uniformization():
    states=list(permutations(range(4))); pos={s:i for i,s in enumerate(states)}
    colors=(0,0,6,13)  # Four distinct conserved keys, including same-color keys.
    q=sp.zeros(24); i=1
    accepted_same_color_actions=0
    for eta in states:
        row=pos[eta]; hs=[]
        for u in range(4):
            l,a,b,r=[colors[eta[(u+j)%4]] for j in [-1,0,1,2]]
            h2=T[i][l][a]+T[i][a][r]-T[i][l][b]-T[i][b][r]
            hs.append(h2)
            rate=sp.Rational(22+5*h2,40)
            z=list(eta); v=(u+1)%4; z[u],z[v]=z[v],z[u]
            assert z!=list(eta)
            accepted_same_color_actions+=int(a==b)
            q[row,pos[tuple(z)]]+=rate; q[row,row]-=rate
        assert sum(hs)==0
    lam=sp.Rational(21,5) # Four channels, each ceiling 21/20.
    p=sp.eye(24)+q/lam
    assert all(x>=0 for x in p)
    assert all(sum(p.row(i))==1 for i in range(24))
    assert sp.ones(1,24)*q==sp.zeros(1,24)
    assert q!=q.T
    # Poisson mixture independently sums exact discrete uniformization matrix.
    t=.37; pp=np.array(p,dtype=float); qq=np.array(q,dtype=float)
    term=np.eye(24); mixture=np.zeros((24,24)); poisson=math.exp(-float(lam)*t)
    for k in range(80):
        mixture+=poisson*term
        term=term@pp; poisson*=float(lam)*t/(k+1)
    exact=expm(t*qq)
    err=float(np.max(np.abs(mixture-exact)))
    assert err<3e-15
    split=float(np.max(np.abs(expm(.11*qq)@expm(.26*qq)-exact)))
    assert split<3e-15
    return {'states':24,'channels_per_state':4,'ceiling_per_channel':'21/20',
            'total_uniformization_rate':'21/5','key_distinct_same_color_actions':accepted_same_color_actions,
            'nonreversible':True,'uniform_invariant':True,
            'poisson_mixture_max_error':err,'independent_interval_semigroup_error':split}

def geometry():
    n=8; coords=list(product(range(n),repeat=3)); loc={x:i for i,x in enumerate(coords)}
    dirs=[tuple(s if j==i else 0 for j in range(3)) for i in range(3) for s in [1,-1]]
    def shift(x,d): return tuple((x[j]+d[j])%n for j in range(3))
    black=[x for x in coords if sum(x)%2==0]
    rows=[]
    for name in ['winding','irregular']:
        partner={}
        for x in black if name=='winding' else [x for x in coords if x[0]%2==0]:
            y=shift(x,(1,0,0)); partner[x]=y; partner[y]=x
        accepted=0
        if name=='irregular':
            rng=random.Random(531921)
            for _ in range(8*n**3):
                x=coords[rng.randrange(n**3)]; i,j=rng.sample(range(3),2)
                e=dirs[2*i]; f=dirs[2*j]
                a,b,c,d=x,shift(x,e),shift(shift(x,e),f),shift(x,f)
                if partner[a]==b and partner[d]==c:
                    pairs=[(a,d),(b,c)]
                elif partner[a]==d and partner[b]==c:
                    pairs=[(a,b),(d,c)]
                else: continue
                for v,w in pairs: partner[v]=w;partner[w]=v
                accepted+=1
            assert accepted>0
        assert len(partner)==n**3 and all(partner[partner[x]]==x for x in coords)
        blackid={x:i for i,x in enumerate(black)}
        total=0; minimum=n**3; mult={}
        for delta in dirs:
            q=[blackid[partner[shift(x,delta)]] for x in black]
            assert sorted(q)==list(range(len(black)))
            seen=set()
            for u in range(len(black)):
                if u not in seen:
                    cycle=[];v=u
                    while v not in seen: seen.add(v);cycle.append(v);v=q[v]
                    assert v==u
                    if len(cycle)>1: minimum=min(minimum,len(cycle)); assert len(cycle)>=4
                v=q[u]
                if u==v: continue
                total+=1; key=tuple(sorted((u,v)));mult[key]=mult.get(key,0)+1
                l=q.index(u);r=q[v];assert len({l,u,v,r})==4
                for x,y in [(black[u],black[v]),(partner[black[u]],partner[black[v]])]:
                    assert sum(min((x[j]-y[j])%n,(y[j]-x[j])%n) for j in range(3))==2
        assert total==5*len(black)
        rows.append({'name':name,'N':n,'pairs':len(black),'channels':total,
                     'distinct_unordered_pair_edges':len(mult),'max_channel_multiplicity':max(mult.values()),
                     'minimum_nontrivial_cycle':minimum,'fixture_accepted_plaquettes':accepted})
    return rows

def fourier():
    root=sp.sqrt(7)
    m=sp.Matrix([[root*E[a][i] for a in range(14)] for i in range(3)]+
                [[root*B[a][i]/2 for a in range(14)] for i in range(3)])
    cov=sp.eye(14)/14-sp.ones(14)/196
    assert m*cov*m.T==sp.eye(6)
    c=sp.Rational(2,7); checks=[]
    for k in [(1,0,0),(0,1,0),(0,0,1),(1,2,3)]:
        a=sum((sp.Matrix(T[i])*sp.Rational(k[i],14) for i in range(3)),sp.zeros(14))
        cx=sp.Matrix([[0,-k[2],k[1]],[k[2],0,-k[0]],[-k[1],k[0],0]])
        d=sp.zeros(6);d[:3,3:]=sp.I*c*cx;d[3:,:3]=-sp.I*c*cx
        assert m*(-sp.I*a)==d*m
        assert d.conjugate().T == -d
        checks.append({'Q_without_2pi':k,'exact_full_current_to_six_field_identity':True})
    khat=sp.Matrix([[0,0,0],[0,0,-1],[0,1,0]])
    pl=sp.diag(1,0,0);pt=sp.eye(3)-pl
    angles=[0,sp.pi/4,sp.pi/2,3*sp.pi/4,sp.pi]
    for theta in angles:
        z=pl+sp.cos(theta)*pt;u=sp.zeros(6)
        u[:3,:3]=z;u[3:,3:]=z;u[:3,3:]=sp.I*sp.sin(theta)*khat;u[3:,:3]=-sp.I*sp.sin(theta)*khat
        assert sp.simplify(u*u.conjugate().T)==sp.eye(6)
        signed=sp.trace((-sp.I*khat.T)*u[:3,3:]+(sp.I*khat.T)*u[3:,:3])/4
        assert sp.simplify(signed-sp.sin(theta))==0
        assert sp.simplify(sp.trace(pt*u[:3,:3]+pt*u[3:,3:])/4-sp.cos(theta))==0
        assert sp.trace(pl*u[:3,:3]+pl*u[3:,3:])/2==1
    return {'normalized_initial_covariance':'I_6','speed':'2/7','current_checks':checks,
            'cross_blocks':'U_EB=+i sin(theta) C_hat; U_BE=-i sin(theta) C_hat',
            'time_phases':['0','pi/4','pi/2','3pi/4','pi'],
            'unitarity_autocorrelation_and_cross_contraction_checks':5}

if __name__=='__main__':
    ans={'scope':'Pre-author finite controls only; no production data read.',
         'rates_and_current':rates_and_current(),'uniformization':uniformization(),
         'geometry':geometry(),'fourier':fourier()}
    (OUT/'PRE_CHECK_RESULTS.json').write_text(json.dumps(ans,indent=2)+'\n')
    print(json.dumps(ans,indent=2))
