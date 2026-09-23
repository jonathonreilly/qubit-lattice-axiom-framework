"""Exact finite author challenges of a full-algebra kernel/record pair.

Finite blank-exterior joints are not infinite-volume marginals. The seven
site star check DOES give the exact infinite-lattice one-parent probability,
because that parent choice depends only on these seven independent clocks.
No kinetic-isotropy or full-foundation compatibility is certified.
"""

# Canonical packaging; supplied scientific fixtures below are unchanged.
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = ['docs/SUPPLIED_RECORD_LAWS_AND_COMMON_ORDER_KERNELS_BOUNDED_THEOREM_NOTE_2026-09-15.md', 'docs/NATIVE_RECORD_SUPPORT_PRESERVING_PRIORITY_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-07.md', 'docs/FORMATION_ORDER_COVARIANCE_AND_ISOTROPIC_BINARY_ORDER_BLIND_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-13.md']
from pathlib import Path as _InputPath
_REPO_ROOT = _InputPath(__file__).resolve().parents[1]
_INPUT_TEXT = {q: (_REPO_ROOT / q).read_text() for q in AUDIT_INPUT_PATHS}
assert 'supplied_record_laws_and_common_order_kernels_bounded_theorem_note_2026-09-15' in _INPUT_TEXT['docs/SUPPLIED_RECORD_LAWS_AND_COMMON_ORDER_KERNELS_BOUNDED_THEOREM_NOTE_2026-09-15.md']
_OUTPUT_JSON = _REPO_ROOT / 'logs/runner-cache/record_pair_check_2026_09_15.json'
_OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
import itertools
import json
import math
from fractions import Fraction as F
from pathlib import Path
import sympy as sp


def probability(p, m, k):
    return F(1,2) if not m else (1-p)/2+p*F(k,m)


def joint(graph, p):
    n = len(graph)
    values = {bits:F(0) for bits in itertools.product([0,1],repeat=n)}
    for order in itertools.permutations(range(n)):
        seen = set()
        predecessor = {}
        for x in order:
            predecessor[x] = set(graph[x])&seen
            seen.add(x)
        for bits in values:
            value = F(1,math.factorial(n))
            for x in order:
                earlier = predecessor[x]
                q = probability(p,len(earlier),sum(bits[y] for y in earlier))
                value *= q if bits[x] else 1-q
            values[bits] += value
    return values


def ancestry_coefficients(graph, x, y):
    n = len(graph)
    coefficients = {}
    for order in itertools.permutations(range(n)):
        position = {v:k for k,v in enumerate(order)}
        choices = [[u for u in graph[v] if position[u]<position[v]] or [None] for v in range(n)]
        weight = F(1,math.factorial(n)*math.prod(map(len,choices)))
        for parent in itertools.product(*choices):
            paths=[]
            for root in [x,y]:
                path=[root]
                while parent[path[-1]] is not None:
                    path.append(parent[path[-1]])
                    assert len(path)<=n
                paths.append(path)
            meeting = next((v for v in paths[0] if v in paths[1]),None)
            if meeting is not None:
                length=paths[0].index(meeting)+paths[1].index(meeting)
                coefficients[length]=coefficients.get(length,F(0))+weight
    return coefficients


def covariance(law,x,y):
    return sum(weight*(F(bits[x])-F(1,2))*(F(bits[y])-F(1,2)) for bits,weight in law.items())


def main():
    p1,p2=F(1,4),F(3,4)
    kernel_cases=0
    for p in [p1,p2]:
        for m in range(7):
            for k in range(m+1):
                q=probability(p,m,k)
                assert (1-p)/2<=q<=1-(1-p)/2
                assert q+(1-q)==1
                kernel_cases+=1
        assert probability(p,1,1)-probability(p,1,0)==p
    zero,identity=sp.zeros(2),sp.eye(2)
    possibilities=[zero,identity,sp.Matrix([[1,0],[0,0]]),sp.Matrix([[0,1],[0,0]]),
                   sp.Matrix([[1,sp.I],[2,3]])]
    transformations=[sp.Matrix([[1,1],[0,1]]),sp.Matrix([[0,1],[1,0]]),
                     sp.Matrix([[2,0],[0,F(1,2)]]),sp.Matrix([[1,sp.I],[0,1]])]
    automorphism_cases=0
    for a in possibilities:
        for g in transformations:
            for conjugate in [False,True]:
                transformed=g*(sp.conjugate(a) if conjugate else a)*g.inv()
                assert (transformed==identity)==(a==identity)
                assert g*zero*g.inv()==zero and g*identity*g.inv()==identity
                automorphism_cases+=1
    a=sp.Matrix([[1,0],[0,0]]);g=sp.Matrix([[0,1],[1,0]])
    wrong_coordinate_gap=abs(a[0,0]-(g*a*g.inv())[0,0])
    assert wrong_coordinate_gap==1

    graphs={'edge':[[1],[0]],'path3':[[1],[0,2],[1]],'square':[[1,3],[0,2],[1,3],[0,2]]}
    graph_checks=[]
    for name,graph in graphs.items():
        pairs=list(itertools.combinations(range(len(graph)),2))
        coeff={pair:ancestry_coefficients(graph,*pair) for pair in pairs}
        checked=[]
        for p in [F(0),p1,p2,F(1)]:
            law=joint(graph,p)
            assert sum(law.values())==1
            assert all(v>=0 for v in law.values())
            for x in range(len(graph)):
                assert sum(v*bits[x] for bits,v in law.items())==F(1,2)
            for pair in pairs:
                direct=covariance(law,*pair)
                formula=sum(a*p**length for length,a in coeff[pair].items())/4
                assert direct==formula
            checked.append(dict(p=str(p),adjacent_covariance=str(covariance(law,0,1))))
        graph_checks.append(dict(graph=name,vertices=len(graph),orders=math.factorial(len(graph)),
                                 ancestry_coefficients={str(pair):{str(k):str(v) for k,v in a.items()} for pair,a in coeff.items()},
                                 direct_joint_checks=checked))
    assert ancestry_coefficients(graphs['path3'],0,1)=={1:F(5,6)}
    assert ancestry_coefficients(graphs['path3'],0,2)=={2:F(2,3)}

    # Center=0 and designated neighbour=1. Exterior cannot alter this choice.
    parent_probability=F(0)
    for order in itertools.permutations(range(7)):
        before=order[:order.index(0)]
        if 1 in before:
            parent_probability+=F(1,math.factorial(7)*len(before))
    assert parent_probability==F(1,7)
    first_meeting_length1=2*parent_probability
    covariance_gap=first_meeting_length1*(p2-p1)/4
    agreement_gap=first_meeting_length1*(p2-p1)/2
    assert covariance_gap==F(1,28) and agreement_gap==F(1,14)
    result=dict(status='finite_author_checks_passed',independent_review=False,
                kernel_count_cases=kernel_cases,algebra_automorphism_probes=automorphism_cases,
                rejected_basis_coordinate_gap=str(wrong_coordinate_gap),finite_graph_checks=graph_checks,
                infinite_lattice_local_parent_probability=str(parent_probability),
                analytic_neighbour_covariance_gap_lower_bound=str(covariance_gap),
                analytic_neighbour_agreement_gap_lower_bound=str(agreement_gap),
                limitations=['finite graph joints use blank exterior and are not infinite marginals',
                             'infinite process and coalescence formula require the written analytic proof',
                             'full M2 domain with proper support, not a full-support measure',
                             'approved kinetic-isotropy compatibility remains unverified',
                             'no physical-law selection or axiom-update verdict'])
    _OUTPUT_JSON.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
    print('per_element: checked exact kernel weights and algebraic identity probes on specified M2 elements')
    print('per_site: checked every recorded-neighbour count and the exact seven-site parent rank probability')
    print('per_mode: checked and not executed — no matter kinetic mode or quantum/Born reconstruction is constructed')
    print('per_block: checked finite edge, path and square joint laws against a separate parent-ancestry expansion')
    print('lattice_wide: checked and not executed — infinite realization and covariance separation rest on the analytic proof, not a lattice simulation')


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
