"""Blind independent spin-S coefficient, loss, and rotor controls.

No author large-spin source or output is read/imported. Electric words and
matter charges are assembled directly from Gauss on a single oriented square.
This small geometry checks algebra, not a torus or thermodynamic theorem.
"""
from pathlib import Path
from datetime import datetime, timezone
from itertools import product
import json
import math
import sys
import numpy as np
import sympy as s
from scipy.linalg import eigh

sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent


def square(spin):
    C=s.Integer(spin*(spin+1)); bg=(1,0,1,0)
    states=[]
    for q in product((-1,0,1),repeat=4):
        if sum(q)!=2:continue
        for last in range(-spin,spin+1):
            e=[];current=last
            for i in range(4):
                current += q[i]-bg[i];e.append(current)
            assert current==last
            if max(e)<=spin and min(e)>=-spin:
                states.append((q,tuple(e)))
    states.sort();index={x:i for i,x in enumerate(states)};D=len(states)
    hops=[s.zeros(D) for _ in range(4)]
    births=[{q:s.zeros(D) for q in (-1,1)} for _ in range(4)]
    def weight(m,delta):
        if not -spin<=m+delta<=spin:return s.Integer(0)
        return s.sqrt(1-s.Rational(m*(m+delta),C))
    for col,(q,e) in enumerate(states):
        for edge in range(4):
            x=edge;y=(edge+1)%4
            for source,dest,orientation in [(x,y,1),(y,x,-1)]:
                if q[source] and not q[dest]:
                    charge=q[source];delta=-orientation*charge;amplitude=weight(e[edge],delta)
                    if amplitude:
                        qq=list(q);qq[dest]=charge;qq[source]=0
                        ee=list(e);ee[edge]+=delta
                        target=(tuple(qq),tuple(ee));assert target in index
                        hops[edge][index[target],col]=amplitude
            if not q[x] and not q[y]:
                for charge in (-1,1):
                    amplitude=weight(e[edge],charge)
                    if amplitude:
                        qq=list(q);qq[x]=charge;qq[y]=-charge
                        ee=list(e);ee[edge]+=charge
                        target=(tuple(qq),tuple(ee));assert target in index
                        births[edge][charge][index[target],col]=amplitude
    h=-sum(hops,s.zeros(D));assert h==h.T
    nb=[sum(q[i]!=0 for i in (1,3)) for q,e in states]
    star=[sum(q[i]==-1 for i in (0,2))+sum(q[i]==1 for i in (1,3)) for q,e in states]
    count=[sum(z!=0 for z in q) for q,e in states]
    assert all(s.Rational(sum((e[i]-e[(i-1)%4])**2 for i in range(4)),2)==n for (q,e),n in zip(states,star))
    low=[i for i,(q,e) in enumerate(states) if q==bg]
    for js in births:
        assert all(all(j[i,k]==0 for i in range(D) for k in low) for j in js.values())
    return {'C':C,'states':states,'hops':hops,'h':h,'nb':nb,'star':star,'count':count,'births':births,'low':low}


def strings(a):return [[str(s.simplify(x)) for x in row] for row in a.tolist()]


def exact_coefficients(spin):
    m=square(spin);dim=len(m['states']);T=m['h'];P=m['low'];C=m['C'];answer={}
    expected2=s.zeros(len(P));expected4=s.zeros(len(P))
    levels=[m['states'][i][1][0] for i in P]
    assert sorted(levels)==list(range(-spin,spin+1))
    for i,e in enumerate(levels):
        ap=1-s.Rational(e*(e-1),C);am=1-s.Rational(e*(e+1),C)
        expected2[i,i]=-2*(ap+am)
        expected4[i,i]=2*ap**2+2*am**2+8*ap*am
        for j,f in enumerate(levels):
            if abs(f-e)==1:
                expected4[j,i]=-2*(1-s.Rational(e*f,C))**2
    for label,penalty in [('sublattice',m['nb']),('star',m['star'])]:
        inv=s.diag(*[s.Rational(1,k) if k else 0 for k in penalty])
        h2=-(T*inv*T).extract(P,P)
        metric=(T*inv*inv*T).extract(P,P)
        f4=-(T*inv*T*inv*T*inv*T).extract(P,P)
        h4=s.simplify(f4-(metric*h2+h2*metric)/2)
        assert s.simplify(h2-expected2)==s.zeros(len(P))
        assert s.simplify(h4-expected4)==s.zeros(len(P))
        assert metric==-h2
        answer[label]={'H2':strings(h2),'normalized_H4':strings(h4),'all_entries_match_weighted_path_formula':True}
    # Birth loss is not the spin-half vacancy projector.
    losses=[]
    for edge,js in enumerate(m['births']):
        total=js[1].T*js[1]+js[-1].T*js[-1]
        coherent=(js[1]+js[-1]).T*(js[1]+js[-1])
        expected=s.diag(*[2*(1-s.Rational(e[edge]**2,C)) if not q[edge] and not q[(edge+1)%4] else 0 for q,e in m['states']])
        assert s.simplify(total-expected)==s.zeros(dim)
        assert s.simplify(coherent-expected)==s.zeros(dim)
        values=sorted(set(expected.diagonal()))
        losses.append({'edge':edge,'loss_eigenvalues':list(map(str,values))})
    # A finite-circuit fourth-order gauge check: every first-order generator
    # is the grade inverse of one edge term; distinct products vanish on P.
    n=s.diag(*m['nb']);gates=[]
    for hop in m['hops']:
        gen=s.zeros(dim)
        for i in range(dim):
            for j in range(dim):
                gap=n[i,i]-n[j,j]
                if gap:gen[i,j]=-hop[i,j]/gap
        assert gen.T==-gen;gates.append(gen)
    checks=0
    for i,a in enumerate(gates):
        for b in gates[i+1:]:
            assert (a*b).extract(P,P)==s.zeros(len(P))
            assert (b*a).extract(P,P)==s.zeros(len(P));checks+=1
    return {'spin':spin,'dimension':dim,'initial_number_dimension':sum(n==2 for n in m['count']),
            'low_dimension':len(P),'low_electric_levels':levels,'coefficients':answer,
            'birth_loss_controls':losses,'first_order_distinct_edge_PP_products_zero':checks}


def symbolic_bulk():
    # z=2d incident edges; each edge meets 2(z-1) other edges.
    E,eta,C,d=s.symbols('E eta C d',real=True);q=E**2-eta*E
    return {'initial_hop_weight_squared':'a_e=1-(E_e^2-eta_e E_e)/C',
            'Gauss_linear_cancellation':'sum_e eta_e E_e=sum_{x in A} div E_x=0',
            'H2':'-(t^2/Delta)dV+(t^2/(Delta C))sum_e E_e^2',
            'diagonal_H4_dimensionless':'sum_e a_e^2+2 sum_{unordered distinct edges sharing a vertex} a_e a_f',
            'constant_H4_at_unit_weights':'dV(4d-1)',
            'diagonal_H4_minus_constant_on_ice':'-2(4d-1)sum_e E_e^2/C + [sum_e q_e^2+2 sum_adjacent q_e q_f]/C^2',
            'offdiagonal_H4_dimensionless':'-2 sum_p(W_{p,S}+W_{p,S}^dagger)',
            'scaling':'epsilon^2 C=J/(2g); Delta=J/(2epsilon^4); t=epsilon Delta',
            'uniform_shift_error_bound':'||(U_infinity-U_S)rho^(1/2)||_2 <= C^(-1) <[E(E+1)]^2>^(1/2)',
            'boundary_countercontrol':'U_S|S>=0 but U_infinity|S>=|S+1>; operator norm error >=1.'}


def rotor_control():
    # One loop's exact low-space Hamiltonian: all four fields have the same m.
    # This independently tests sign, factors, and the finite-S diagonal term.
    g=2.;J=1.;cutoff=24
    levels=np.arange(-cutoff,cutoff+1,dtype=float)
    rotor=np.diag(4*g*levels**2)-J*(np.eye(2*cutoff+1,k=1)+np.eye(2*cutoff+1,k=-1))
    re,rv=eigh(rotor)
    initial=np.zeros(len(levels));initial[cutoff]=1
    rows=[]
    for spin in [1,2,4,8,16]:
        C=spin*(spin+1);x=np.arange(-spin,spin+1,dtype=float)
        diag4=12-24*x*x/C+(12*x**4-4*x*x)/C**2
        ham=np.diag(4*g*x*x+J*(diag4-12)/2)
        for i,m in enumerate(x[:-1]):
            ham[i,i+1]=ham[i+1,i]=-J*(1-m*(m+1)/C)**2
        ev,vec=eigh(ham);psi0=np.zeros(len(x));psi0[spin]=1
        for time in [.2,.7,1.3]:
            ps=vec@(np.exp(-1j*time*ev)*(vec.T@psi0))
            pr=rv@(np.exp(-1j*time*re)*(rv.T@initial))
            embedded=np.zeros(len(levels),complex);embedded[cutoff-spin:cutoff+spin+1]=ps
            distance=np.linalg.norm(embedded-pr)
            rows.append({'spin':spin,'C':C,'time':time,'vector_difference':float(distance),
                         'C_times_difference':float(C*distance),'spin_zero_flux_probability':float(abs(ps[spin])**2),
                         'rotor_zero_flux_probability':float(abs(pr[cutoff])**2),
                         'rotor_probability_at_cutoff':float(abs(pr[0])**2+abs(pr[-1])**2)})
    assert max(r['rotor_probability_at_cutoff'] for r in rows)<1e-20
    return {'g':g,'J':J,'rotor_cutoff':cutoff,'rows':rows,
            'scope':'Finite cutoff numerical corroboration; domain and local uniformity require the report proof, not small tail values alone.'}


def moment_bound():
    # A bound needed for fourth moments under a unit shift.
    m=s.symbols('m',integer=True)
    numerator=1+(m+1)**2;denominator=1+m*m
    difference=s.expand(3*denominator-numerator)
    assert difference==2*m*m-2*m+1
    # 2(m-1/2)^2+1/2>0 proves this for every real m, hence every integer.
    ratios=[(1+(n+1)**2)/(1+n*n) for n in range(-100,101)]
    assert max(ratios)<3 and min(ratios)>1/3
    return {'polynomial_certificate':str(difference),'positive_form':'2(m-1/2)^2+1/2',
            'fourth_moment_weight':'F(E)=(1+E^2)^2',
            'weighted_shift_commutator_bound':'||F^(-1/2)[W_p,F]F^(-1/2)|| <= 3 when p meets the edge',
            'Gronwall_rate':'12 J (d-1)', 'sample_max_ratio':max(ratios)}


def main():
    result={'created_utc':datetime.now(timezone.utc).isoformat(),'status':'PASS',
            'exact_square_controls':[exact_coefficients(S) for S in (1,2,3)],
            'bulk_formulas':symbolic_bulk(),'moment_control':moment_bound(),'rotor_control':rotor_control(),
            'source_boundary':'Only neutral specification and previously sealed spin-half/uniform-local dependencies used; no new author large-spin sources.'}
    (HERE/'FINITE_SPIN_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)


if __name__=='__main__':main()
