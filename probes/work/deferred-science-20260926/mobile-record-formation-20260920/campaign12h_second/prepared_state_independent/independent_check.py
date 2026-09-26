#!/usr/bin/env python3
"""Independent pre-author-checker controls for smooth finite-mode preparation.

Includes exact Gaussian algebra, a complete two-A-record count sector, and
an exact convolution of the full 15-label N=4 product law. No author imports.
"""
import argparse
from collections import Counter, defaultdict, deque
from fractions import Fraction as F
import itertools as it
import json
from pathlib import Path
import sympy as s


def categorical():
    rho_a,rho_b = s.Rational(3,8),s.Rational(1,4)
    labels = [(s.zeros(3,1),s.zeros(3,1),1-rho_a-rho_b)]
    for i,sign in it.product(range(3),(-1,1)):
        e=s.zeros(3,1);e[i]=sign
        labels.append((e,s.zeros(3,1),rho_a/6))
    for signs in it.product((-1,1),repeat=3):
        labels.append((s.zeros(3,1),s.Matrix(signs),rho_b/8))
    mean=s.zeros(6,1);cov=s.zeros(6);cross=s.zeros(6,8)
    for e,b,p in labels:
        v=e/s.sqrt(rho_a/3);v=v.col_join(b/s.sqrt(rho_b))
        other=s.Matrix([int(e!=s.zeros(3,1)),int(b!=s.zeros(3,1)),
                        e[0]**2-e[1]**2,e[1]**2-e[2]**2,
                        b[0]*b[1],b[0]*b[2],b[1]*b[2],b[0]*b[1]*b[2]])
        mean+=p*v;cov+=p*v*v.T;cross+=p*v*other.T
    assert mean==s.zeros(6,1) and cov==s.eye(6) and cross==s.zeros(6,8)
    return {'rho_A':str(rho_a),'rho_B':str(rho_b),'labels':len(labels),
            'normalized_vector_covariance':'I_6','spectator_cross_covariance':'zero 6 by 8',
            'product_centered_charge_variances':{'e':str(rho_a/2),'b':str(3*rho_b/2)}}


def gaussian_algebra():
    lam=s.symbols('lambda',nonnegative=True)
    c,t=s.symbols('c t',real=True)
    z=s.symbols('z')
    k=2*s.pi*s.Matrix([1,2,2]);r=6*s.pi
    C=s.Matrix([[0,-k[2],k[1]],[k[2],0,-k[0]],[-k[1],k[0],0]])
    pl=k*k.T/r**2;pt=s.eye(3)-pl;zero=s.zeros(3)
    G=s.I*c*(zero.row_join(C)).col_join((-C).row_join(zero))
    sigma=pt+pl/(1+lam);cov=s.diag(sigma,sigma)
    assert G+s.conjugate(G.T)==s.zeros(6)
    assert (G*cov-cov*G).applyfunc(s.simplify)==s.zeros(6)
    assert s.factor((z*s.eye(6)-G).det())==z**2*(z**2+r**2*c**2)**2
    cosine=pl+s.cos(c*r*t)*pt
    sine=s.I*s.sin(c*r*t)*C/r
    U=cosine.row_join(sine).col_join((-sine).row_join(cosine))
    assert (s.diff(U,t)-G*U).applyfunc(s.simplify)==s.zeros(6)
    assert U.subs(t,0)==s.eye(6)
    assert (U*cov*s.conjugate(U.T)-cov).applyfunc(s.trigsimp)==s.zeros(6)
    assert ((U*cov)[:3,3:]-sine).applyfunc(s.simplify)==s.zeros(3)
    assert s.factor(cov.det())==(1+lam)**-2
    q,a=s.symbols('q a',positive=True)
    integral0=s.integrate(s.exp(-a*q),(q,0,s.oo))
    integral1=s.integrate(q*s.exp(-a*q),(q,0,s.oo))
    assert integral0==1/a and integral1==1/a**2
    cases=[]
    for m,l in [(1,0),(1,1),(2,3),(3,s.Rational(1,2))]:
        l=s.sympify(l)
        normal=(1+l)**(-2*m)
        expectation=s.Rational(2*m)/(1+l)
        entropy=2*m*(s.log(1+l)-l/(1+l))
        if l==0:assert entropy==0
        cases.append({'m':m,'lambda':str(l),'Z':str(normal),'E_Q':str(expectation),'H':str(entropy)})
    return {'K':'2*pi*(1,2,2)','anti_Hermitian':True,'stationary_covariance_commutator':0,
            'characteristic_polynomial':str(s.factor((z*s.eye(6)-G).det())),
            'upper_cross_block':'i sin(c |K| t) C_K/|K|','covariance_determinant_per_mode':'(1+lambda)^(-2)',
            'Gaussian_cases':cases,'Lipschitz_constant':'sqrt(2*lambda/e), zero at lambda=0'}


def two_record_sector():
    n=4;vertices=list(it.product(range(n),repeat=3))
    states=list(it.combinations(range(n**3),2));index={x:i for i,x in enumerate(states)}
    neighbors=[]
    for x in vertices:
        row=[]
        for j,sign in it.product(range(3),(-1,1)):
            y=tuple((x[k]+(sign if k==j else 0))%n for k in range(3))
            row.append(vertices.index(y))
        neighbors.append(row)
    # rho_A=3/8 -> V*(rho_A/3)=8. First-axis-shell M, lambda=4 log 2.
    q=[];g=[];log2g=[];adj=[]
    for a,b in states:
        delta=(vertices[a][0]-vertices[b][0])%4
        value=F(1,2) if delta==0 else F(0) if delta==2 else F(1,4)
        q.append(value);power=4*value;assert power.denominator==1
        g.append(F(1,2**power.numerator));log2g.append(-power.numerator)
        targets=[]
        for old,fixed in [(a,b),(b,a)]:
            for new in neighbors[old]:
                if new!=fixed:targets.append(index[tuple(sorted((fixed,new)))])
        adj.append(targets)
    seen={0};queue=deque([0])
    while queue:
        for j in adj[queue.popleft()]:
            if j not in seen:seen.add(j);queue.append(j)
    assert len(seen)==len(states)==2016
    for i,targets in enumerate(adj):
        for j in targets:assert i in adj[j]
    Lg=[sum((g[j]-g[i] for j in targets),F(0)) for i,targets in enumerate(adj)]
    assert sum(Lg)==0
    norm=sum(g);assert norm==1144
    adjacent=index[tuple(sorted([vertices.index((0,0,0)),vertices.index((1,0,0))]))]
    opposite=index[tuple(sorted([vertices.index((0,0,0)),vertices.index((2,0,0))]))]
    assert q[adjacent]==F(1,4) and q[opposite]==0 and Lg[adjacent]==1
    assert Lg[opposite]==-2
    entropy_derivative=sum((Lg[i]*log2g[i] for i in range(len(states))),F(0))/norm
    assert entropy_derivative<0
    return {'N':n,'state_count':len(states),'context_drive':'zero throughout this sector because b=0',
            'rates':'unit symmetric exchange floor','lambda':'4 log 2','M':'three positive first-axis-shell representatives',
            'Q_histogram':{str(k):v for k,v in sorted(Counter(q).items())},'conditional_Z':str(norm/len(states)),
            'adjacent_Q':str(q[adjacent]),'opposite_Q':str(q[opposite]),
            'adjacent_probability_derivative':str(Lg[adjacent]/norm),
            'entropy_derivative_coefficient_of_log2':str(entropy_derivative),
            'microscopic_prepared_conditional_law_stationary':False}


def extra_shell_countercontrol():
    n=5;a=s.Rational(1,8)
    def q(dx):return s.simplify(sum(2+2*s.cos(2*s.pi*j*dx/n) for j in (1,2))/(n**3*a))
    q0,q1,q2=[q(j) for j in (0,1,2)]
    assert q1==q2==s.Rational(24,125) and q0==s.Rational(64,125)
    modes=[tuple(j if axis==i else 0 for axis in range(3)) for i in range(3) for j in (1,2)]
    residues={tuple(a%n for a in m) for m in modes}
    assert len(residues)==6 and residues.isdisjoint({tuple(-a%n for a in m) for m in modes})
    for perm,signs in it.product(it.permutations(range(3)),it.product((-1,1),repeat=3)):
        for m in modes:
            transformed=tuple(signs[j]*m[perm[j]] for j in range(3))
            assert transformed in modes or tuple(-x for x in transformed) in modes
    return {'N':5,'M':modes,'mode_aliases_or_self_conjugates':False,'closed_under_proper_cubic_rotations_up_to_sign':True,
            'two_plus_x_records_distance_one_Q':str(q1),'distance_two_Q':str(q2),
            'separation_y_one_Q':str(q0),
            'finding':'Extra second axis harmonics exactly cancel the stated distance-one/distance-two witness. The law remains nonstationary by the other separation; restrict that particular witness to the first-axis-shell choice, or to sufficiently large N at fixed M.'}


def full_product_convolution():
    # For N=4, M={2*pi e_x}, the real and imaginary Fourier sums each contain
    # 32 independent sites. The +/- phase is absorbed by the symmetric tag law.
    # The projected single-site (e_x,b_x) increments have probabilities
    # (0,0):10/16, (+/-1,0):1/16 each, (0,+/-1):2/16 each.
    increments=[((0,0),10),((1,0),1),((-1,0),1),((0,1),2),((0,-1),2)]
    distributions={0:{(0,0):1}}
    for count in range(1,33):
        out=defaultdict(int)
        for (a,b),multiplicity in distributions[count-1].items():
            for (da,db),weight in increments:
                out[a+da,b+db]+=weight*multiplicity
        assert sum(out.values())==16**count
        distributions[count]=dict(out)
    def expectation(count,shift=(0,0),moment=False):
        total=F(0)
        for (a,b),weight in distributions[count].items():
            power=2*(a+shift[0])**2+(b+shift[1])**2
            term=F(weight,2**power)
            if moment:term*=F(power,16)
            total+=term
        return total/16**count
    Zr=expectation(32);Z=Zr*Zr
    EQr=expectation(32,moment=True)/Zr;EQ=2*EQr
    shifts=[(0,0),(1,0),(-1,0),(0,1),(0,-1)]
    ratios={shift:expectation(31,shift)/Zr for shift in shifts}
    marginal={'vacancy':F(3,8)*ratios[0,0]}
    for axis,sign in it.product(range(3),(-1,1)):
        marginal[f'A{axis}:{sign}']=F(1,16)*ratios[(sign,0) if axis==0 else (0,0)]
    for signs in it.product((-1,1),repeat=3):
        marginal[f'B{signs}']=F(1,32)*ratios[0,signs[0]]
    assert sum(marginal.values())==1
    reference={'vacancy':F(3,8),**{f'A{i}:{a}':F(1,16) for i,a in it.product(range(3),(-1,1))},
               **{f'B{z}':F(1,32) for z in it.product((-1,1),repeat=3)}}
    tv=sum(abs(marginal[k]-reference[k]) for k in marginal)/2
    assert tv>0
    assert ratios[1,0]==ratios[-1,0] and ratios[0,1]==ratios[0,-1]
    # Two opposite-x neighbors have opposite Fourier phases. The other 30
    # variables remain independent. Exactly sum their two marked increments.
    pair_cache={}
    cross_a=cross_b=F(0)
    for d,wd in increments:
        for e,we in increments:
            offset=(e[0]-d[0],e[1]-d[1])
            if offset not in pair_cache:pair_cache[offset]=expectation(30,offset)/Zr
            probability=F(wd*we,16**2)*pair_cache[offset]
            cross_a+=probability*d[0]*e[0]
            cross_b+=probability*d[1]*e[1]
    eax2=2*marginal['A0:1'];eay2=2*marginal['A1:1']
    b2=sum(v for k,v in marginal.items() if k.startswith('B'))
    charge_e=(2*eax2-2*cross_a+4*eay2)/4
    charge_b=(6*b2-2*cross_b)/4
    assert charge_e>0 and charge_b>0
    precision=50
    sym=lambda q:s.Rational(q.numerator,q.denominator)
    lam=16*s.log(2)
    entropy=-s.log(sym(Z))-lam*sym(EQ)
    gaussian_Z=(1+lam)**-2
    gaussian_H=2*(s.log(1+lam)-lam/(1+lam))
    return {'method':'Exact integer-coefficient convolution of all 64 independent 15-label sites, via the sufficient (e_x,b_x) statistics; no sampling.',
            'N':4,'M':'one mode 2*pi e_x','rho_A':'3/8','rho_B':'1/4','lambda':'16 log 2',
            'real_group_sites':32,'real_group_lattice_states':len(distributions[32]),
            'Z_exact':str(Z),'E_mu_Q_exact':str(EQ),'one_site_TV_exact':str(tv),
            'finite_N_values':{'Z':str(s.N(sym(Z),precision)),'E_Q':str(s.N(sym(EQ),precision)),
                               'H':str(s.N(entropy,precision)),'one_site_TV':str(s.N(sym(tv),precision)),
                               'E_D_e_squared':str(s.N(sym(charge_e),precision)),
                               'E_D_b_squared':str(s.N(sym(charge_b),precision))},
            'Gaussian_limit_values_at_same_lambda':{'Z':str(s.N(gaussian_Z,precision)),'H':str(s.N(gaussian_H,precision))},
            'finite_N_equal_to_Gaussian_claim':False,'one_site_vector_means':'exactly zero by the checked +/- ratios',
            'charge_squared_exact':{'e':str(charge_e),'b':str(charge_b)}}


def run():
    return {'categorical':categorical(),'Gaussian_and_propagator':gaussian_algebra(),
            'finite_sector_nonstationarity':two_record_sector(),
            'larger_mode_set_countercontrol':extra_shell_countercontrol(),
            'full_product_exact_control':full_product_convolution()}


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,required=True);args=parser.parse_args()
    result=run();args.out.write_text(json.dumps(result,indent=2)+'\n')
    # Full exact rationals are saved in JSON; avoid obscuring the substantive log.
    printed=dict(result);printed['full_product_exact_control']={k:v for k,v in result['full_product_exact_control'].items()
        if k not in ('Z_exact','E_mu_Q_exact','one_site_TV_exact','charge_squared_exact')}
    print(json.dumps(printed,indent=2))
    print('PASS: independent Gaussian, sector and exact-product controls. One finite-volume witness-scope counterexample retained.')
