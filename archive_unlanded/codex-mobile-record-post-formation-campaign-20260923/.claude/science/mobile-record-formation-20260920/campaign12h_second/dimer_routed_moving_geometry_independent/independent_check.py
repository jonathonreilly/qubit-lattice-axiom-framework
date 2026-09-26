#!/usr/bin/env python3
"""Independent moving-geometry controls; no author code/data imports."""
from pathlib import Path
from itertools import product,permutations,combinations
from collections import Counter
import json,math,random
import numpy as np
import sympy as sp
from scipy.linalg import expm

OUT=Path(__file__).resolve().parent

def two_rewards_operator(q,a,b):
    n=len(q);h=np.zeros((6*n,6*n))
    for j in range(6):h[j*n:(j+1)*n,j*n:(j+1)*n]=q
    def block(i,j,value):h[i*n:(i+1)*n,j*n:(j+1)*n]=np.diag(value)
    block(0,1,a);block(0,2,b);block(1,3,2*a);block(1,4,b);block(2,4,a);block(2,5,2*b)
    return h

def kick(m,a,b):
    p,u,v,uu,uv,vv=m.copy()
    return np.array([p,u+p*a,v+p*b,uu+2*u*a+p*a*a,
                     uv+u*b+v*a+p*a*b,vv+2*v*b+p*b*b])

def one_reward_operator(q,f):
    n=len(q);h=np.zeros((3*n,3*n))
    for j in range(3):h[j*n:(j+1)*n,j*n:(j+1)*n]=q
    h[:n,n:2*n]=np.diag(f);h[n:2*n,2*n:]=np.diag(2*f)
    return h

def switched_energy():
    n=4;q1=sp.zeros(n);q2=sp.zeros(n)
    for i in range(n):q1[i,(i+1)%n]+=2;q1[i,(i-1)%n]+=sp.Rational(1,2)
    for a,b,r in [(0,1,sp.Rational(1,2)),(1,2,sp.Rational(3,2)),(2,3,sp.Rational(5,4)),(3,0,sp.Rational(3,4)),(0,2,sp.Rational(2,3))]:
        q2[a,b]+=r;q2[b,a]+=r
    for a,b in [(0,2),(2,3),(3,0)]:q2[a,b]+=sp.Rational(2,5)
    for q in [q1,q2]:
        for i in range(n):q[i,i]=-sum(q[i,j] for j in range(n) if j!=i)
        assert q*sp.ones(n,1)==sp.zeros(n,1) and sp.ones(1,n)*q==sp.zeros(1,n)
        assert q!=q.T
    assert q1*q2!=q2*q1
    qs=[q1,q2,2*q1];fs=[sp.Matrix([3,-1,0,-2]),sp.Matrix([-1,2,-3,2]),sp.Matrix([0,1,-2,1])]
    specs=[]
    for q,F in zip(qs,fs):
        lap=-(q+q.T)/2;f=(lap+sp.ones(n)/n).inv()*F
        assert lap*f==F and sum(f)==0
        energy=(F.T*f)[0]/n
        specs.append((np.array(q,dtype=float),np.array(F,dtype=float).ravel(),np.array(f,dtype=float).ravel(),energy))
    perms=[]
    for image in [[2,1,0,3],[0,3,2,1]]:
        p=np.zeros((n,n));p[np.arange(n),image]=1;perms.append(p)
    rows=[]
    for count in [1,2,9,37]:
        dt=.6/count;m=np.zeros((6,n));m[0]=1/n;integral=np.zeros((3,n));integral[0]=1/n
        density=np.eye(n)[0];energy=0.;unitary_error=0.
        for j in range(count):
            q,F,f,hminus=specs[j%3];energy+=dt*float(hminus)
            m=kick(m,-f,f)
            m=(m.ravel()@expm(dt*two_rewards_operator(q,-q@f,-q.T@f))).reshape(6,n)
            m=kick(m,f,-f)
            integral=(integral.ravel()@expm(dt*one_reward_operator(q,F))).reshape(3,n)
            density=density@expm(dt*q)
            assert np.max(abs(m[0]-1/n))<5e-15
            if j+1<count:
                p=perms[j%2];m=m@p;integral=integral@p
                before=np.mean((n*density-1)**2);density=density@p
                unitary_error=max(unitary_error,abs(np.mean((n*density-1)**2)-before))
        plus,minus,cross=m[3].sum(),m[5].sum(),m[4].sum()
        reward_second=integral[2].sum();paired=(plus+2*cross+minus)/4
        expected_martingale_second=2*energy
        assert abs(plus-expected_martingale_second)<3e-12
        assert abs(minus-expected_martingale_second)<3e-12
        assert abs(paired-reward_second)<3e-12
        assert reward_second<=2*energy+3e-12 and abs(integral[1].sum())<3e-13
        # This rational lower bound follows from minimum symmetric rate >=1/2
        # and a connected four-vertex graph of diameter <=3.
        g=1/60
        assert np.mean((n*density-1)**2)<=3*math.exp(-2*g*.6)+1e-12
        rows.append({'constant_geometry_intervals':count,'total_time':.6,
                     'integral_second_moment':float(reward_second),'energy_bound':2*energy,
                     'forward_martingale_second':float(plus),'backward_martingale_second':float(minus),
                     'expected_each_martingale_second':expected_martingale_second,
                     'forward_backward_pairing_error':float(abs(paired-reward_second)),
                     'nonstationary_density_permutation_norm_error':float(unitary_error)})
    # The estimate needs stationary COLOR entrance, not stationary geometry.
    q=np.array([[-.01,.01],[1.,-1.]])
    F=np.array([-.01,1.]);start=np.array([0.,1.,0.,0.,0.,0.])
    moment=start@expm(.5*one_reward_operator(q,F));second=float(moment[4:].sum())
    false_bound=1/101
    assert second>false_bound
    return {'noncommuting_generators':True,'exact_interval_Hminus_norms':[str(x[3]) for x in specs],
            'rows':rows,'excluded_nonstationary_color_countercontrol':{'initial_state':1,
            'stationary_law':['100/101','1/101'],'time':.5,'actual_integral_second':second,
            'incorrect_stationary_energy_bound':false_bound}}

def immutable_square():
    tested=0;projections=Counter()
    horizontal={frozenset((0,1)),frozenset((2,3))};vertical={frozenset((1,2)),frozenset((3,0))}
    for state in permutations(range(4)):
        pair_edges={frozenset((state.index(0),state.index(1))),frozenset((state.index(2),state.index(3)))}
        if pair_edges not in [horizontal,vertical]:continue
        for black in [(0,2),(1,3)]:
            initial=tuple(state[x]//2 for x in black);changes=[]
            for direction in [-1,1]:
                after=tuple(state[(x-direction)%4] for x in range(4))
                assert sorted(after)==[0,1,2,3]
                for record in range(4):assert (after.index(record)-state.index(record))%4==direction%4
                new_edges={frozenset((after.index(0),after.index(1))),frozenset((after.index(2),after.index(3)))}
                assert new_edges==(vertical if pair_edges==horizontal else horizontal)
                final=tuple(after[x]//2 for x in black)
                assert final in [initial,initial[::-1]]
                changes.append(final==initial[::-1]);tested+=1
                projections['swap' if final==initial[::-1] else 'identity']+=1
                inverse=tuple(after[(x+direction)%4] for x in range(4));assert inverse==state
            assert sorted(changes)==[False,True]
    return {'record_orientation_parity_and_sense_cases':tested,'projection_counts':dict(projections),
            'inverse_immutable_rotation_exact':True,'geometry_flip_rate':'2 nu','color_swap_drift_rate':'nu'}

def matching_and_forms():
    n=8;xyz=list(product(range(n),repeat=3));index={x:i for i,x in enumerate(xyz)}
    black=[x for x in xyz if sum(x)%2==0];k=len(black)
    def move(x,axis,sign=1):return tuple((x[j]+(sign if j==axis else 0))%n for j in range(3))
    k0=sp.Rational(5,4);nu=sp.Rational(7,9);rows=[]
    for kind in ['winding','columnar','irregular']:
        partner={};starts=black if kind=='winding' else [x for x in xyz if x[0]%2==0]
        for x in starts:y=move(x,0);partner[x]=y;partner[y]=x
        if kind=='irregular':
            rng=random.Random(381107)
            for _ in range(8*n**3):
                a=rng.choice(xyz);i,j=rng.sample(range(3),2);b=move(a,i);d=move(a,j);c=move(b,j)
                if partner[a]==b and partner[d]==c:pairs=[(a,d),(b,c)]
                elif partner[a]==d and partner[b]==c:pairs=[(a,b),(d,c)]
                else:continue
                for x,y in pairs:partner[x]=y;partner[y]=x
        owner={}
        for u,x in enumerate(black):owner[x]=u;owner[partner[x]]=u
        routed=Counter()
        for x in black:
            for axis in range(3):
                for sign in [-1,1]:
                    a,b=owner[x],owner[move(x,axis,sign)]
                    if a!=b:routed[tuple(sorted((a,b)))]+=1
        assert sum(routed.values())==5*k
        flips=Counter()
        for a in xyz:
            for i,j in combinations(range(3),2):
                b=move(a,i);d=move(a,j);c=move(b,j)
                if not ((partner[a]==b and partner[d]==c) or (partner[a]==d and partner[b]==c)):continue
                corners=[a,b,c,d];opposite=[x for x in corners if sum(x)%2==0]
                edge=tuple(sorted(owner[x] for x in opposite));assert len(set(edge))==2
                flips[edge]+=1
        assert all(m==1 for m in flips.values())
        for edge in flips:assert routed[edge]>=1 and nu<=2*nu/k0*(k0*routed[edge]/2)
        ls=np.zeros((k,k));lk=np.zeros((k,k))
        for edges,lap,scale in [(routed,ls,float(k0)/2),(flips,lk,float(nu))]:
            for (a,b),m in edges.items():
                r=m*scale;lap[a,a]+=r;lap[b,b]+=r;lap[a,b]-=r;lap[b,a]-=r
        Q=2*np.pi*np.array([1,2,3]);F=np.exp(-1j*np.array(black)@Q/n)/np.sqrt(k)
        drift=-lk@F;poisson=np.linalg.solve(ls+np.ones((k,k))/k,drift)
        norm=float(np.vdot(drift,poisson).real/k);energy=float(np.vdot(F,lk@F).real/k)
        bound=2*float(nu/k0)*energy
        assert norm>=-1e-18 and norm<=bound+max(1e-19,abs(bound)*1e-11)
        rows.append({'matching':kind,'N':n,'flippable_squares':sum(flips.values()),
                     'maximum_squares_per_black_pair':max(flips.values(),default=0),
                     'minimum_routed_multiplicity_on_flip_edges':min((routed[e] for e in flips),default=0),
                     'exact_edgewise_form_comparison':True,'one_marker_Hminus_squared':norm,
                     'one_marker_D_K':energy,'displayed_Hminus_upper_bound':bound})
    return rows

def gauss_fourier():
    rows=[];maximum=0.;divmax=0.;cases=0
    for n in [8,10]:
        v=n**3
        for base in [(0,0,0),(n-1,n-1,n-1)]:
            parity=(-1)**sum(base)
            for i,j in combinations(range(3),2):
                ei=np.eye(3)[i];ej=np.eye(3)[j];x=np.array(base,dtype=float)
                for mode in [(1,0,0),(0,1,0),(0,0,1),(1,2,3)]:
                    q=2*np.pi*np.array(mode);k=q/n;center=x+(ei+ej)/2
                    for orientation in [-1,1]:
                        # Assemble signed outgoing links individually. The
                        # formula is then checked against their actual phases.
                        links=[(i,x,-parity),(i,x+ej,parity),(j,x,parity),(j,x+ei,-parity)]
                        actual=np.zeros(3,dtype=complex)
                        for axis,origin,value in links:
                            actual[axis]+=orientation*value*np.exp(-1j*k@(origin+np.eye(3)[axis]/2))/math.sqrt(v)
                        expected=orientation*2j*parity*np.exp(-1j*k@center)*(-np.sin(k[j]/2)*ei+np.sin(k[i]/2)*ej)/math.sqrt(v)
                        error=float(max(abs(actual-expected)));maximum=max(maximum,error)
                        divergence=abs(np.sin(k/2)@actual);divmax=max(divmax,float(divergence))
                        assert error<2e-15 and divergence<2e-15
                        norm=float(np.vdot(actual,actual).real)
                        assert norm<=float(q@q)/(n*n*v)+1e-16
                        cases+=1
        rows.append({'N':n,'local_increment_cases':cases-(rows[-1]['cumulative_cases'] if rows else 0),'cumulative_cases':cases})
    # One flippable face embedded in a torus, with all other geometry held fixed:
    # the two-state reversible identity checks the factors 2 nu and 2 t D.
    nu=.7;delta2=.013
    reversibility=[]
    for t in [.01,.3,2.]:
        actual=.5*delta2*(1-math.exp(-4*nu*t));energy=nu*delta2
        assert actual<=2*t*energy
        reversibility.append({'time':t,'stationary_increment_second':actual,'twice_time_D':2*t*energy})
    return {'increment_cases':cases,'maximum_component_formula_error':maximum,'maximum_symbolic_divergence_error':divmax,
            'per_size':rows,'two_state_reversible_boundary_control':reversibility}

if __name__=='__main__':
    energy=switched_energy();print('switched forward/backward and entrance countercontrol done',flush=True)
    square=immutable_square();print('immutable square projections done',flush=True)
    forms=matching_and_forms();print('full matching form comparison done',flush=True)
    gauss=gauss_fourier();print('Gauss Fourier and reversible boundary done',flush=True)
    result={'scope':'Pre-author independent controls; exact permutation/form identities and separately numerical finite moment/Fourier evaluations.',
            'switched_energy':energy,'immutable_square':square,'matching_form_comparison':forms,'gauss_fourier':gauss}
    (OUT/'INDEPENDENT_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'history_cases':len(energy['rows']),'rotation_cases':square['record_orientation_parity_and_sense_cases'],
                      'matching_cases':len(forms),'Fourier_increment_cases':gauss['increment_cases']},indent=2))
