"""Selective post-seal reconstruction, without executing author runners.

The complete stored rational series are checked by multiplying the power
series of gate matrices and their inverses, not by the author's commutator
recursion. The finite physical sector is the earlier independent builder.
This is finite algebra and source authentication, not numerical proof of a
uniform-volume bound. No primary or PRE artifact is written.
"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
from itertools import product
import importlib.util
import json
import math
import sys
import sympy as sp
import numpy as np

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
BASE = HERE.parent


def identity(path):
    path = Path(path).resolve(); raw = path.read_bytes()
    return {'path': str(path), 'bytes': len(raw), 'sha256': sha256(raw).hexdigest()}


def verify(rows):
    for row in rows:
        actual = identity(row['path'])
        assert actual == row, (row, actual)


def matrix(a):
    return sp.Matrix([[sp.Rational(x) for x in row] for row in a])


def poly_multiply(a, b, order):
    out = [sp.zeros(a[0].rows) for _ in range(order+1)]
    for i, aa in enumerate(a):
        if not any(aa):
            continue
        for j, bb in enumerate(b[:order+1-i]):
            if any(bb):
                out[i+j] += aa*bb
    return out


def gate_series(s, power, order):
    out = [sp.zeros(s.rows) for _ in range(order+1)]
    term = sp.eye(s.rows)
    for k in range(order//power+1):
        out[k*power] = term
        term = term*s/(k+1)
    return out


def direct_series(n, hop, gates, order):
    u = [sp.eye(n.rows)]+[sp.zeros(n.rows) for _ in range(order)]
    for power, gen in gates:
        u = poly_multiply(gate_series(gen, power, order), u, order)
    inverse = [a.T for a in u]
    unit = poly_multiply(u, inverse, order)
    assert unit[0] == sp.eye(n.rows) and all(a == sp.zeros(n.rows) for a in unit[1:])
    h = [n, hop]+[sp.zeros(n.rows) for _ in range(order-1)]
    return poly_multiply(poly_multiply(u, h, order), inverse, order)


def sector_and_author_series():
    path = BASE/'hardcore_live_density_independent/finite_sector_check.py'
    assert identity(path)['sha256'] == 'c1e6142e632ae77c14fee1b76079c8cba0f2e9c73cf1fed2e40f84f0a3893122'
    spec = importlib.util.spec_from_file_location('own_prior_builder', path)
    own = importlib.util.module_from_spec(spec); spec.loader.exec_module(own)
    model = own.build(4, [(i, (i+1)%4) for i in range(4)], {0, 2}, 0)
    global_result = json.loads((BASE/'LOCAL_NORMAL_FORM_RECORD_RESULTS.json').read_text())
    circuit_result = json.loads((BASE/'FINITE_CIRCUIT_NORMAL_FORM_RECORD_RESULTS.json').read_text())
    author_basis = global_result['basis']
    own_basis = [(tuple(q), tuple((word >> e)&1 for e in range(4)))
                 for q, word in zip(model['charges'], model['states'])]
    permutation = [own_basis.index((tuple(q), tuple(bits))) for q, bits in author_basis]
    assert len(set(permutation)) == 9 and len(model['states']) == 9
    hop = -sum(model['hop'], sp.zeros(9)).extract(permutation, permutation)
    number = sp.diag(*[sum(x != 0 for x in q) for q, bits in author_basis])
    rows = []
    for kind, source_rows in [('global', global_result['checks']), ('circuit', circuit_result['checks'])]:
        for row in source_rows:
            name = row['model']
            n = sp.diag(*[sum(q[x] != 0 for x in (1,3)) if name == 'B_occupancy'
                         else sum(q[x] == -1 for x in (0,2))+sum(q[x] == 1 for x in (1,3))
                         for q,bits in author_basis])
            order = row['order']
            if kind == 'global':
                exact = row['exact_formal_matrices']
                gates = [(r, matrix(a)) for r,a in enumerate(exact['generators'],1)]
                normal = list(map(matrix, exact['normal_coefficients']))
                omitted = matrix(exact['first_omitted_coefficient'])
                omitted_squared = sp.Rational(exact['first_omitted_Frobenius_squared_exact'])
            else:
                gates = [(g['order'], matrix(g['generator'])) for g in row['gates']]
                normal = list(map(matrix, row['normal_coefficients']))
                omitted = matrix(row['first_omitted_coefficient'])
                omitted_squared = sp.Rational(row['first_omitted_Frobenius_squared_exact'])
            for r,g in gates:
                assert g.T == -g and number*g == g*number
                parity = sp.diag(*[(-1)**int(n[i,i]) for i in range(9)])
                assert parity*g*parity == (-1)**r*g
            reconstructed = direct_series(n, hop, gates, order+1)
            assert reconstructed[:order+1] == normal
            assert reconstructed[order+1] == omitted
            assert sum(x*x for x in omitted) == omitted_squared
            low = [i for i in range(9) if n[i,i] == 0]
            for r,a in enumerate(normal):
                assert a == a.T and n*a == a*n
                if r%2:
                    assert not any(a)
            assert normal[2].extract(low,low) == -2*sp.eye(2)
            assert normal[4].extract(low,low) == sp.Matrix([[2,-2],[-2,2]])
            summary = {'kind':kind, 'penalty':name, 'order':order,
                       'gate_count_including_zero':len(gates), 'all_stored_coefficients_recomposed':True,
                       'exact_first_omitted_frobenius_squared':str(omitted_squared),
                       'first_omitted_frobenius':str(sp.N(sp.sqrt(omitted_squared),22)),
                       'all_gate_parities_and_number_commutators_verified':True}
            if kind == 'circuit':
                first = [g for r,g in gates if r == 1]
                noncommuting = sum(any(a*b-b*a) for i,a in enumerate(first) for b in first[i+1:])
                summary['noncommuting_first_order_gate_pairs'] = noncommuting
                assert noncommuting > 0
            # Every numeric output row is read and its recorded ratios checked.
            numeric_checks = []
            for nr in row['numerical_controls']:
                eps = sp.Rational(nr['epsilon'])
                residual = sp.Float(nr['residual_Frobenius'],35)
                ratio_key = 'residual_over_exact_leading_term' if kind == 'global' else 'residual_over_exact_first_omitted_term'
                derived = sp.N(residual/(sp.sqrt(omitted_squared)*eps**(order+1)),35)
                recorded = sp.Float(nr[ratio_key],35)
                assert abs(derived-recorded) < sp.Float('1e-27')
                assert 0 < sp.Float(nr['dressed_birth_amplitude_over_epsilon']) < 10
                assert 0 < sp.Float(nr['local_field_change_over_epsilon']) < 10
                numeric_checks.append({'epsilon':str(eps),'stored_ratio_recomputed':str(sp.N(derived,20))})
            summary['numeric_table_arithmetic'] = numeric_checks
            rows.append(summary)
            print(json.dumps({'completed_series':summary}),flush=True)
    return {'own_to_author_basis_permutation':permutation,'rows':rows,
            'scope':'All stored rational matrices are independently recomposed. Numerical high-precision exponentials are authenticated and their table arithmetic checked, not rerun.'}


def source_bound_and_onsite_control():
    # The full dissipator can be first order even when the jump count is second order.
    s = sp.symbols('s',real=True,positive=True)
    c = sp.sqrt(1-s*s)
    p = sp.diag(1,0,0)
    b = sp.Matrix([[0,0,0],[0,0,0],[s,c,0]])
    jump = b*p*b.T
    loss = b.T*b
    dissipator = sp.simplify(jump-(loss*p+p*loss)/2)
    assert sp.trace(jump) == s*s
    assert dissipator[:2,:2].det() == -s*s*(1-s*s)/4
    # Two-by-two block eigenvalues (-s^2 +/- s)/2, plus eigenvalue s^2.
    eigs = [(-s*s-s)/2,(-s*s+s)/2,s*s]
    char = sp.symbols('lambda')
    assert sp.simplify(dissipator.charpoly(char).as_expr()-sp.prod(char-e for e in eigs)) == 0
    checks = []
    for numerator,denominator in [(1,3),(1,11),(1,101)]:
        z = sp.Rational(numerator,denominator)
        numeric = np.array(dissipator.subs(s,z),float)
        trace_norm = float(np.linalg.svd(numeric,compute_uv=False).sum())
        assert abs(trace_norm-float(z+z*z)) < 1e-14
        checks.append({'BP_norm':str(z),'jump_trace':str(z*z),'full_dissipator_trace_norm':str(z+z*z)})
    # Identity holds on all fixed-charge configurations, without field enumeration.
    onsite_rows = []
    for volume in (4,6):
        A = set(range(0,volume,2)); passed = 0
        for q in product((-1,0,1),repeat=volume):
            if sum(q) != volume//2:
                continue
            half_square = sum(sp.Rational((q[x]-int(x in A))**2,2) for x in range(volume))
            projector_sum = sum(q[x] == (-1 if x in A else 1) for x in range(volume))
            assert half_square == projector_sum
            if projector_sum == 0:
                assert q == tuple(1 if x in A else 0 for x in range(volume))
            passed += 1
        onsite_rows.append({'volume':volume,'fixed_charge_words':passed,'integer_penalty_identity':True,'unique_zero_pattern':True})
    return {'dissipator_matrix':[[str(x) for x in row] for row in dissipator.tolist()],
            'exact_trace_norm_for_0_s_1':'s+s^2','exact_jump_trace':'s^2','controls':checks,
            'scope':'The O(epsilon) trace-source estimate is sharp as a general bound; a jump-probability-only O(epsilon^2) source estimate is false.',
            'onsite_integer_extension_checks':onsite_rows}


def clipped_cone_and_scales():
    # Finite-torus controls cross the wrap scale; the accompanying proof uses
    # #B(r)<=C(1+r)^d, so constants do not depend on these samples.
    rows=[]
    for periods in [(6,6),(6,10),(6,6,6),(6,8,10)]:
        distances = [sum(min(x,L-x) for x,L in zip(site,periods)) for site in product(*(range(L) for L in periods))]
        d=len(periods)
        for eps in (.01,.2):
            for vt in (0.,2.,20.,100.):
                actual = sum(min(eps,math.exp(min(0.,vt-r))) for r in distances)
                scale = eps*(1+vt+abs(math.log(eps)))**d
                rows.append({'periods':periods,'epsilon':eps,'vT':vt,'clipped_sum':actual,'ratio_to_claimed_scale':actual/scale})
                assert actual/scale < 20
    exponents=[]
    for d in (2,3,4):
        n=2*d+6
        rem=n+1-4-2*d
        birth=2*d+1-2*d
        assert (rem,birth)==(3,1)
        exponents.append({'dimension':d,'normal_form_order':n,'remainder_after_cone_power':rem,'birth_after_cone_power':birth})
    return {'finite_torus_controls':rows,'max_observed_ratio':max(x['ratio_to_claimed_scale'] for x in rows),'scaling_powers':exponents}


def main():
    author_seal=BASE/'UNIFORM_LOCAL_RING_AUTHOR_SEAL.json'
    pre=HERE/'PRE_COMPARISON_SEAL.json'
    assert identity(author_seal)['sha256']=='4b52f52f820ed5efbe01b18d47c0166018f0c421cd507fb55f171d893f8a7ce5'
    assert identity(pre)['sha256']=='928e25108e5482c4a8d555323e55cda2a6f3b0a5b9cbdcf4e0c1b2550e84fd6b'
    a=json.loads(author_seal.read_text()); p=json.loads(pre.read_text())
    verify(a['artifacts']); verify(p['sources']+p['artifacts'])
    contexts=json.loads((BASE/'UNIFORM_LOCAL_RING_SOURCE_CONTEXT.json').read_text())
    checked_context=[]
    for row in contexts['dependencies']:
        if Path(row['path']).name=='BALLISTIC_FIELD_SIGNALS_FROM_RECORD_FORMATION.md':
            continue  # expressly outside this assignment; do not open it
        verify([row]); checked_context.append(row)
    result={'created_utc':datetime.now(timezone.utc).isoformat(),'status':'PASS',
            'authentication':{'author_artifacts':17,'preserved_PRE_bindings':24,'prior_context_dependencies':checked_context,
                              'unread_context_reference':'BALLISTIC_FIELD_SIGNALS_FROM_RECORD_FORMATION.md is neither opened nor imported.'},
            'stored_series_check':sector_and_author_series(),
            'full_dissipator_and_onsite_control':source_bound_and_onsite_control(),
            'clipped_cone_and_scaling':clipped_cone_and_scales(),
            'limits':['No author runner executed; stored exact matrices independently recomposed.',
                      'Finite controls do not prove locality, uniform constants, or a thermodynamic field phase.',
                      'PRE and all primary sources are unchanged.']}
    (HERE/'COMPARISON_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)


if __name__=='__main__':
    main()
