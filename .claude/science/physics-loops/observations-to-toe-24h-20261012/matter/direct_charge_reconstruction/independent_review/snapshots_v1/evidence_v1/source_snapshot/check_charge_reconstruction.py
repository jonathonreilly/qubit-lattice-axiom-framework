#!/usr/bin/env python3
"""Exact charge reconstruction and explicitly summary-level observations."""
from datetime import datetime, timezone
from fractions import Fraction as F
from itertools import combinations_with_replacement, product
from pathlib import Path
import hashlib
import json
import math
import sys

import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parent


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def charge_table(nc, h, eps):
    q, l = h*(1+2*eps)/nc, -h*(1+2*eps)
    return dict(Q=q, u=-q-h, d=-q+h, L=l, e=-l+h, n=-l-h, H=h)


def polynomial_derivation():
    nc, q, l, h = sp.symbols('N_c q l h', real=True)
    u, d, e, n = -q-h, -q+h, -l+h, -l-h
    color = 2*q+u+d
    weak = nc*q+l
    grav0 = sp.expand(2*nc*q+nc*(u+d)+2*l+e)
    cubic0 = sp.expand(2*nc*q**3+nc*(u**3+d**3)+2*l**3+e**3)
    assert color == 0 and sp.expand(grav0-(l+h)) == 0
    assert sp.expand(cubic0-((l+h)**3-6*h*h*weak)) == 0
    assert sp.expand(grav0+n) == 0
    assert sp.expand(cubic0+n**3+6*h*h*weak) == 0
    # Solve the linear equations rather than insert the familiar values.
    q0, l0 = sp.symbols('q0 l0', real=True)
    minimal = sp.solve([nc*q0+l0, l0+h], [q0, l0], dict=True)
    assert minimal == [{q0:h/nc, l0:-h}]
    eps = sp.symbols('epsilon', real=True)
    shifted = {q:h*(1+2*eps)/nc, l:-h*(1+2*eps)}
    assert sp.simplify(weak.subs(shifted)) == 0
    assert sp.simplify((2*n).subs(shifted)-4*h*eps) == 0
    assert sp.simplify((2*(l+h)).subs(shifted)+4*h*eps) == 0
    t = sp.symbols('t', real=True)
    flavors = [-h+t, -h-t, -h]
    assert sum(sp.expand(grav0.subs({nc:3,q:h/3,l:li})) for li in flavors) == 0
    assert sum(sp.expand(cubic0.subs({nc:3,q:h/3,l:li})) for li in flavors) == 0
    assert sum(3*h/3+li for li in flavors) == 0
    delta = sp.symbols('delta', real=True)
    physical = dict(up=sp.Rational(2,3)+eps/3, down=-sp.Rational(1,3)+eps/3,
                    electron=-1-eps, neutrino=-eps, proton=1+eps, neutron=eps, W=1)
    measured = {k:sp.factor((v/(1+eps)).subs(eps,delta/(1-delta))) for k,v in physical.items()}
    expected = dict(up=(2-delta)/3, down=(-1+2*delta)/3, electron=-1,
                    neutrino=-delta, proton=1, neutron=delta, W=1-delta)
    assert all(sp.simplify(measured[k]-expected[k]) == 0 for k in expected)
    assert sp.simplify(measured['proton']+measured['electron']-measured['neutrino']-measured['neutron']) == 0
    return dict(Yukawa={k:str(v) for k,v in dict(u=u,d=d,e=e,n=n).items()},
                anomalies_without_n=dict(color=str(color),weak=str(weak),gravity=str(grav0),
                                         cubic_factored='(l+h)^3-6*h^2*(N_c*q+l)'),
                anomalies_with_n=dict(gravity='0',cubic='-6*h^2*(N_c*q+l)'),
                minimal_solution={str(k):str(v) for k,v in minimal[0].items()},
                measured_electric_charges={k:str(v) for k,v in measured.items()},
                disconnected_flavor_counterexample=[str(x) for x in flavors],
                Majorana_charge='4*h*epsilon',Weinberg_charge='-4*h*epsilon')


def representation_traces():
    I, r3 = sp.I, sp.sqrt(3)
    lambdas = [sp.Matrix(x) for x in [
        [[0,1,0],[1,0,0],[0,0,0]], [[0,-I,0],[I,0,0],[0,0,0]],
        [[1,0,0],[0,-1,0],[0,0,0]], [[0,0,1],[0,0,0],[1,0,0]],
        [[0,0,-I],[0,0,0],[I,0,0]], [[0,0,0],[0,0,1],[0,1,0]],
        [[0,0,0],[0,0,-I],[0,I,0]], [[1/r3,0,0],[0,1/r3,0],[0,0,-2/r3]]]]
    tc = [x/2 for x in lambdas]
    tw = [sp.Matrix([[0,1],[1,0]])/2,sp.Matrix([[0,-I],[I,0]])/2,sp.diag(1,-1)/2]
    zero1, zero2, zero3 = sp.zeros(1),sp.zeros(2),sp.zeros(3)
    generators = [sp.diag(sp.kronecker_product(t,sp.eye(2)),-t.T,-t.T,zero2,zero1,zero1) for t in tc]
    generators += [sp.diag(sp.kronecker_product(sp.eye(3),t),zero3,zero3,t,zero1,zero1) for t in tw]
    q, h = sp.symbols('q h', real=True)
    charges = [q]*6+[-q-h]*3+[-q+h]*3+[-3*q]*2+[3*q+h,3*q-h]
    generators += [sp.diag(*charges)]
    assert all(g.shape == (16,16) and g == g.conjugate().T for g in generators)
    products = {(j,k):generators[j]*generators[k]+generators[k]*generators[j]
                for j in range(12) for k in range(j,12)}
    rows = []
    for i,j,k in combinations_with_replacement(range(12),3):
        a,b = generators[i],products[j,k]
        value = sp.expand(sum(a[r,s]*b[s,r] for r in range(16) for s in range(16) if a[r,s]!=0 and b[s,r]!=0))
        assert value == 0
        rows.append(dict(indices=[i,j,k],trace=str(value)))
    assert len(rows) == 364
    gravity = [str(sp.trace(g)) for g in generators]
    assert all(v == '0' for v in gravity)
    missing_n_gravity = sp.factor(sum(charges[:-1]))
    missing_n_cubic = sp.factor(sum(x**3 for x in charges[:-1]))
    assert sp.expand(missing_n_gravity+(3*q-h)) == 0
    assert sp.expand(missing_n_cubic+(3*q-h)**3) == 0
    # Wrongly make u^c a fundamental: a direct nonzero SU(3)^3 counterfactual.
    t=tc[-1]
    wrong=sp.diag(sp.kronecker_product(t,sp.eye(2)),t,-t.T,zero2,zero1,zero1)
    wrong_trace=sp.simplify(2*sp.trace(wrong**3))
    assert wrong_trace != 0
    return dict(basis='8 Gell-Mann/2,3 Pauli/2,Y; all LH; Q ordered color x weak',
                symmetric_cubic_rows=rows,gravity_traces=gravity,
                missing_n_gravity=str(missing_n_gravity),missing_n_cubic=str(missing_n_cubic),
                wrong_u_color_cubic_trace=str(wrong_trace),ordinary_SU2_doublets_per_generation=4,
                additional_global_anomaly_classification=False)


def rational_controls():
    rows=[]
    for nc,h,eps in product([3,5,7],[F(1,2),F(1),F(3,2)],[F(-1,10),F(0),F(1,100),F(2,3),F(2)]):
        c=charge_table(nc,h,eps); q,u,d,l,e,n=[c[k] for k in ['Q','u','d','L','e','n']]
        values=[2*q+u+d,nc*q+l,2*nc*q+nc*(u+d)+2*l+e+n,
                2*nc*q**3+nc*(u**3+d**3)+2*l**3+e**3+n**3]
        assert all(v==0 for v in values) and (nc+1)%2==0
        assert q+h+u == q-h+d == l-h+e == l+h+n == 0
        rows.append(dict(Nc=nc,h=str(h),epsilon=str(eps),charges={k:str(v) for k,v in c.items()},anomalies=[str(v) for v in values]))
    return rows


def graph_controls():
    rows=[]
    for mask in range(512):
        edges=[(a,b+3) for a in range(3) for b in range(3) if mask&(1<<(3*a+b))]
        matrix=[]; adjacency=[set() for _ in range(6)]
        for a,b in edges:
            row=[0]*6;row[a]=-1;row[b]=1;matrix.append(row)
            adjacency[a].add(b);adjacency[b].add(a)
        remaining=set(range(6));components=[]
        while remaining:
            start=min(remaining);stack=[start];seen=set()
            while stack:
                a=stack.pop()
                if a not in seen:
                    seen.add(a);stack.extend(adjacency[a]-seen)
            remaining-=seen;components.append(sorted(seen))
        rank=sp.Matrix(matrix).rank() if matrix else 0
        assert rank == 6-len(components)
        rows.append(dict(mask=mask,edge_count=len(edges),components=components,rank=rank,connected=len(components)==1))
    return dict(rows=rows,connected_support_count=sum(x['connected'] for x in rows),
                any_claim_all_supports_unitary=False)


def global_controls():
    triality=dict(Q=1,u=-1,d=-1,L=0,e=0,n=0,H=0)
    weak=dict(Q=1,u=0,d=0,L=1,e=0,n=0,H=1)
    rows=[]
    for k in range(-12,25):
        eps=F(k,6);c=charge_table(3,F(1,2),eps);z={key:6*v for key,v in c.items()}
        integer=all(v.denominator==1 for v in z.values())
        allowed={'product':integer,
                 'Z2':integer and all((z[key]+weak[key])%2==0 for key in z),
                 'Z3':integer and all((z[key]-triality[key])%3==0 for key in z),
                 'Z6':integer and all((z[key]+2*triality[key]+3*weak[key])%6==0 for key in z)}
        predicted={'product':(2*eps).denominator==1,'Z2':eps.denominator==1,
                   'Z3':(2*eps/3).denominator==1,'Z6':(eps/3).denominator==1}
        assert allowed == predicted
        rows.append(dict(epsilon=str(eps),weights={key:str(v) for key,v in z.items()},allowed=allowed))
    variable=[]
    for k in [3,6,12,22]:
        D=10**k;eps=F(1,D);c=charge_table(3,F(1,2),eps)
        denominator=math.lcm(*(v.denominator for v in c.values()))
        weights={key:int(v*denominator) for key,v in c.items()}
        assert denominator==D and weights['n']==1 and math.gcd(*weights.values())==1
        assert weights['H']==D//2
        variable.append(dict(k=k,epsilon=str(eps),primitive_unit=str(F(1,denominator)),
                             primitive_weights=weights,delta=str(eps/(1+eps)),fixed_H_weight_3=False))
    return dict(fixed_lattice_rows=rows,variable_primitive_lattice_examples=variable,
                positive_near_standard_gap_product='1/3',positive_near_standard_gap_Z6='3/4',
                global_form_observed=False)


def observation_map():
    source=json.loads((ROOT/'OBSERVATION_INPUTS.json').read_text())
    y,sy=float(source['neutron']['mean_in_1e_minus21']),float(source['neutron']['reported_uncertainty_in_1e_minus21'])
    s,ss=float(source['molecule']['mean_in_1e_minus21']),float(source['molecule']['reported_uncertainty_in_1e_minus21'])
    Z,A=source['molecule']['Z_nominal'],source['molecule']['A_nominal'];N=A-Z
    a=N/A
    prediction=a*y; prediction_sigma=a*sy
    residual=s-prediction; combined_sigma=math.sqrt(ss*ss+prediction_sigma**2)
    pull=residual/combined_sigma
    denom=1/sy**2+a*a/ss**2
    fitted=(y/sy**2+a*s/ss**2)/denom
    fit_sigma=denom**(-.5)
    chi2=((y-fitted)/sy)**2+((s-a*fitted)/ss)**2
    assert abs(chi2-pull*pull)<1e-14
    M=np.array([[-N/Z,A/Z],[1.,0.],[-A/Z,A/Z]])
    means=M@np.array([y,s]);covariance=M@np.diag([sy*sy,ss*ss])@M.T
    assert abs(means[0]-means[1]-means[2])<1e-14
    assert abs(covariance[0,0]+covariance[1,1]-2*covariance[0,1]-covariance[2,2])<1e-13
    assert np.linalg.matrix_rank(covariance)==2
    polarity=source['molecule']['polarity_means_in_1e_minus21']
    half_sum=(float(polarity[0]['mean'])+float(polarity[1]['mean']))/2
    half_diff=(float(polarity[0]['mean'])-float(polarity[1]['mean']))/2
    half_sigma=math.hypot(float(polarity[0]['uncertainty']),float(polarity[1]['uncertainty']))/2
    assert abs(half_sum-s)<1e-14
    delta_exact=F(source['neutron']['mean_in_1e_minus21'])/10**21
    epsilon_exact=delta_exact/(1-delta_exact)
    # The two possible baseline assumptions have different molecular responses.
    assert F(N,A) != 1
    return dict(units='All means/sigmas in this section are multiples of1e-21; covariance in(1e-21)^2.',
                calibration_only=dict(delta=y,reported_sigma=sy,delta_exact=str(delta_exact),epsilon_exact=str(epsilon_exact),input='neutron'),
                exposed_development_transfer=dict(design_coefficient=str(F(N,A)),predicted_s=prediction,
                    predicted_sigma=prediction_sigma,observed_s=s,reported_observed_sigma=ss,residual=residual,
                    independent_Gaussian_combined_sigma=combined_sigma,standardized_residual=pull,blind=False,refit=False),
                optional_joint_summary_refit=dict(delta=fitted,sigma=fit_sigma,chi2=chi2,summary_degrees_of_freedom=1,
                    calibration_inputs=['neutron','SF6'],independent_test=False,p_value_reported=False),
                general_two_parameter_inversion=dict(order=['x=(qp+qe)/e','y=qn/e','qnu/e=x-y'],
                    means=means.tolist(),covariance=covariance.tolist(),sigmas=np.sqrt(np.diag(covariance)).tolist(),
                    anomaly_family_imposed=False,neutrino_neutrality_imposed=False),
                polarity_check=dict(half_sum=half_sum,half_difference_nuisance=half_diff,unrounded_independent_sigma=half_sigma,
                    published_rounded_sigma=ss,unconstrained_even_offset_degenerate_with_s=True),
                source_scope=source['scope'])


def main():
    names=['PROTOCOL.md','DIRECT_CHARGE_RECONSTRUCTION.md','OBSERVATION_INPUTS.json','check_charge_reconstruction.py']
    out=dict(created_utc=datetime.now(timezone.utc).isoformat(),source_sha256={n:sha(ROOT/n) for n in names},
             derivation=polynomial_derivation(),representation=representation_traces(),rational_rows=rational_controls(),
             mixing_graphs=graph_controls(),global_lattices=global_controls(),observations=observation_map())
    out['summary']=dict(cubic_generator_triples=len(out['representation']['symmetric_cubic_rows']),
        rational_charge_cases=len(out['rational_rows']),mixing_graphs=len(out['mixing_graphs']['rows']),
        connected_supports=out['mixing_graphs']['connected_support_count'],global_grid_cases=len(out['global_lattices']['fixed_lattice_rows']),
        compact_small_charge_examples=len(out['global_lattices']['variable_primitive_lattice_examples']),
        transfer_prediction_in_1e_minus21=out['observations']['exposed_development_transfer']['predicted_s'],
        transfer_standardized_residual=out['observations']['exposed_development_transfer']['standardized_residual'],
        blind_empirical_test=False)
    dest=Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/'evidence_v1/RESULTS.json'
    dest.parent.mkdir(exist_ok=True);assert not dest.exists(),'Preserve every execution; use a new version path.'
    dest.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n');print(json.dumps(out['summary'],sort_keys=True))


if __name__=='__main__':
    main()
