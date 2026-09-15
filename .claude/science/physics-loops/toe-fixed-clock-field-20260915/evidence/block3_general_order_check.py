"""Exact finite algebra challenges of the general-alphabet proof.
The standard-Borel and null-set arguments are analytic, not finite tests.
"""
import itertools
import json
from pathlib import Path
import sympy as s
from block3_record_pair_check import joint
from fractions import Fraction as F


def main():
    one=s.ones(3,1);pi=s.ones(3,3)/3
    u=s.Matrix([1,-1,0]);v=s.Matrix([1,1,-2])
    k=pi+u*v.T/12
    assert k*one==one and one.T*k==one.T
    assert k*k==pi and k!=pi and k!=k.T
    assert min(k)>0
    weighted_difference=k-k.T
    assert weighted_difference[0,1]==s.Rational(1,6)
    reversible=[]
    for lam in [s.Rational(-1,4),s.Rational(0),s.Rational(1,4),s.Rational(3,4)]:
        a=pi+lam*(s.eye(3)-pi)
        assert a==a.T and a*one==one and min(a)>=0
        residual=a*a-pi
        assert residual==lam**2*(s.eye(3)-pi)
        reversible.append(dict(lam=str(lam),square_projection_residual_squared_norm=str(s.trace(residual.T*residual))))
    graph=[[1],[0,2],[1]]
    pair=[]
    for p in [F(1,4),F(3,4)]:
        law=joint(graph,p)
        endpoint=sum(weight*F(bits[0])*F(bits[2]) for bits,weight in law.items())
        assert endpoint-F(1,4)==p*p/6
        pair.append(dict(copy_probability=str(p),mixture_endpoint_covariance=str(endpoint-F(1,4))))
    labels=list(itertools.product([0,1],repeat=2))
    pp=F(1,2)
    def bit_cond(out,neighbor):
        return (1-pp)/2+pp*int(out==neighbor)
    port_reference={}
    for conf in itertools.product(labels,repeat=3):
        port_reference[conf]=F(1,64)
        for x in range(2):
            port_reference[conf]*=1+pp*(2*conf[x][1]-1)*(2*conf[x+1][0]-1)
    assert sum(port_reference.values())==1
    port_checks=0
    for order in itertools.permutations(range(3)):
        for conf,reference in port_reference.items():
            seen=set();actual=F(1)
            for x in order:
                actual*=bit_cond(conf[x][0],conf[x-1][1]) if x-1 in seen else F(1,2)
                actual*=bit_cond(conf[x][1],conf[x+1][0]) if x+1 in seen else F(1,2)
                seen.add(x)
            assert actual==reference
            reflected=tuple((r,l) for l,r in reversed(conf))
            assert reference==port_reference[reflected]
            port_checks+=1
    assert bit_cond(1,1)!=bit_cond(1,0)
    result=dict(status='finite_author_checks_passed',independent_review=False,
                nonreversible_positive_matrix=[[str(x) for x in row] for row in k.tolist()],
                exact_square_is_independent=True,two_site_reversibility_defect=str(weighted_difference[0,1]),
                reversible_controls=reversible,priority_mixture_controls=pair,
                direction_sensitive_order_blind_checks=port_checks,
                limitations=['standard-Borel generalization uses written Markov-operator proof',
                             'null-set exception and Feller upgrade are not numerically certified',
                             'two-port escape is a supplied path model, not a cubic full-domain embedding',
                             'no order-independent physical-law or full-foundation conclusion'])
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
    print('per_element: checked an exact positive nonsymmetric stochastic matrix whose square is the independent kernel')
    print('per_site: checked two-site detailed balance failure and reversible square-projection controls')
    print('per_mode: checked and not executed — no kinetic or quantum mode is identified by this conditional theorem')
    print('per_block: checked exact path-three mixtures and a direction-sensitive two-port order-independent escape')
    print('lattice_wide: checked and not executed — general Borel and supported-profile statements rely on the analytic proof')


if __name__=='__main__':
    main()
