"""Exact finite algebra challenges of the general-alphabet proof.
The standard-Borel and null-set arguments are analytic, not finite tests.
"""

# Canonical packaging; supplied scientific fixtures below are unchanged.
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = ['docs/SUPPLIED_RECORD_LAWS_AND_COMMON_ORDER_KERNELS_BOUNDED_THEOREM_NOTE_2026-09-15.md', 'docs/NATIVE_RECORD_SUPPORT_PRESERVING_PRIORITY_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-07.md', 'docs/FORMATION_ORDER_COVARIANCE_AND_ISOTROPIC_BINARY_ORDER_BLIND_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-13.md', 'scripts/record_pair_check_2026_09_15.py']
from pathlib import Path as _InputPath
_REPO_ROOT = _InputPath(__file__).resolve().parents[1]
_INPUT_TEXT = {q: (_REPO_ROOT / q).read_text() for q in AUDIT_INPUT_PATHS}
assert 'supplied_record_laws_and_common_order_kernels_bounded_theorem_note_2026-09-15' in _INPUT_TEXT['docs/SUPPLIED_RECORD_LAWS_AND_COMMON_ORDER_KERNELS_BOUNDED_THEOREM_NOTE_2026-09-15.md']
_OUTPUT_JSON = _REPO_ROOT / 'logs/runner-cache/general_order_check_2026_09_15.json'
_OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
import itertools
import json
from pathlib import Path
import sympy as s
from record_pair_check_2026_09_15 import joint
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
    _OUTPUT_JSON.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
    print('per_element: checked an exact positive nonsymmetric stochastic matrix whose square is the independent kernel')
    print('per_site: checked two-site detailed balance failure and reversible square-projection controls')
    print('per_mode: checked and not executed — no kinetic or quantum mode is identified by this conditional theorem')
    print('per_block: checked exact path-three mixtures and a direction-sensitive two-port order-independent escape')
    print('lattice_wide: checked and not executed — general Borel and supported-profile statements rely on the analytic proof')


if __name__=='__main__':
    main()

if __name__ == '__main__':
    print('TOTAL: PASS=1 FAIL=0')
    print('Completed family: complete finite companion program; individual checks and diagnostics remain in structured JSON')
    print('per_element: exact finite alphabet and matrix-record identities')
    print('per_site: finite partial-record and order fixtures')
    print('per_mode: not executed: no spectral or Fourier calculation is claimed')
    print('per_block: one complete companion family; imported helpers are shared implementation, not independent evidence')
    print('lattice_wide: analytical claims and infinite/iterated limits checked in written proof, not executed here')
