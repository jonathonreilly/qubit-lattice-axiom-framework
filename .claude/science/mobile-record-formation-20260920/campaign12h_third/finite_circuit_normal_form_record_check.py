#!/usr/bin/env python3
"""Term-by-term finite circuit version of the local normal-form recursion.

The nine-state sector verifies exact algebra, including ordering effects.
The finite-depth coloring and volume-uniform constants are proved separately.
"""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import time
import mpmath as mp
import sympy as sp
import local_normal_form_record_check as algebra

OUT = Path(__file__).resolve().parent
ORDER = 12


def main():
    begin = time.monotonic()
    dep = hashlib.sha256((OUT/'local_normal_form_record_check.py').read_bytes()).hexdigest()
    assert dep == '9507de54429615ccc0256da4965f9a4e093787797d635e53c751d3279028d3ec'
    basis, hop, nb, count, jumps, _ = algebra.source.square_model((1,0,1,0),allow_birth=True)
    dim = len(basis)
    edge_hops = [sp.zeros(dim) for _ in range(4)]
    for i,(m,b) in enumerate(basis):
        for j,(mm,bb) in enumerate(basis):
            if hop[i,j]:
                edges = [e for e in range(4) if b[e] != bb[e]]
                assert len(edges) == 1
                edge_hops[edges[0]][i,j] = hop[i,j]
    assert sum(edge_hops,sp.zeros(dim)) == hop
    mp.mp.dps = 90
    rows = []
    for model in ['B_occupancy','homogeneous_star_onsite_extension']:
        pieces = []
        nmat = sp.zeros(dim)
        for x in range(4):
            if model == 'B_occupancy':
                nx = sp.diag(*[int(x%2==1 and m[x] != 0) for m,b in basis])
            else:
                nx = sp.diag(*[int(m[x] == (-1 if x%2==0 else 1)) for m,b in basis])
            nmat += nx
            if any(nx):
                series = [sp.zeros(dim) for _ in range(ORDER+2)]
                series[0] = nx
                pieces.append({'label':'onsite_'+str(x),'series':series})
        for e,h in enumerate(edge_hops):
            series = [sp.zeros(dim) for _ in range(ORDER+2)]
            series[1] = h
            pieces.append({'label':'hop_'+str(e),'series':series})
        gate_rows = []
        for power in range(1,ORDER+1):
            gates = []
            # Freeze every order-r generator before applying any order-r gate.
            for piece in pieces:
                coefficient = piece['series'][power]
                assert coefficient == coefficient.T
                gen = sp.zeros(dim)
                for i in range(dim):
                    for j in range(dim):
                        grade = nmat[i,i]-nmat[j,j]
                        if grade:
                            gen[i,j] = coefficient[i,j]/grade
                assert gen == -gen.T
                if any(gen):
                    gates.append((piece['label'],gen))
            for label,gen in gates:
                for piece in pieces:
                    piece['series'] = algebra.formal_conjugate(piece['series'],gen,power,ORDER+1)
                gate_rows.append({'order':power,'origin':label,'generator':algebra.serialize(gen)})
            total = sum((piece['series'][power] for piece in pieces),sp.zeros(dim))
            assert algebra.comm(nmat,total) == sp.zeros(dim)
            if power%2:
                assert total == sp.zeros(dim)
            print(json.dumps({'model':model,'order':power,'nonzero_gates':len(gates)}),flush=True)
        total_series = [sum((piece['series'][k] for piece in pieces),sp.zeros(dim)) for k in range(ORDER+2)]
        assert total_series[0] == nmat
        for k in range(1,ORDER+1):
            assert algebra.comm(nmat,total_series[k]) == sp.zeros(dim)
            if k%2:
                assert total_series[k] == sp.zeros(dim)
        p = [i for i in range(dim) if nmat[i,i] == 0]
        assert len(p) == 2
        assert total_series[2].extract(p,p) == -2*sp.eye(2)
        assert total_series[4].extract(p,p) == sp.Matrix([[2,-2],[-2,2]])
        leading_sq = sum(v*v for v in total_series[ORDER+1])
        assert leading_sq > 0
        leading = mp.sqrt(mp.mpf(int(leading_sq.p))/int(leading_sq.q))
        proj = sp.diag(*[int(i in p) for i in range(dim)])
        field = sp.diag(*[sp.Rational(2*b[0]-1,2) for m,b in basis])
        num = sp.diag(*count)
        for row in gate_rows:
            gen = sp.Matrix(row['generator'])
            assert algebra.comm(num,gen) == sp.zeros(dim)
        numeric = []
        for estr in ['0.006','0.012','0.024']:
            eps = mp.mpf(estr)
            y = mp.eye(dim)
            for row in gate_rows:
                y = mp.expm(eps**row['order']*algebra.as_mp(sp.Matrix(row['generator'])))*y
            actual = y*(algebra.as_mp(nmat)+eps*algebra.as_mp(hop))*y.T
            truncated = sum((eps**k*algebra.as_mp(a) for k,a in enumerate(total_series[:ORDER+1])),mp.zeros(dim))
            res = algebra.frob(actual-truncated)
            ratio = res/(leading*eps**(ORDER+1))
            assert mp.mpf('0.7') < ratio < mp.mpf('1.3')
            birth = max(algebra.frob(y*algebra.as_mp(j)*y.T*algebra.as_mp(proj)) for j in jumps)
            field_change = algebra.frob(y*algebra.as_mp(field)*y.T-algebra.as_mp(field))
            assert birth < 10*eps and field_change < 10*eps
            numeric.append({'epsilon':estr,'residual_Frobenius':mp.nstr(res,30),
                            'residual_over_exact_first_omitted_term':mp.nstr(ratio,30),
                            'dressed_birth_amplitude_over_epsilon':mp.nstr(birth/eps,30),
                            'local_field_change_over_epsilon':mp.nstr(field_change/eps,30)})
        rows.append({'model':model,'order':ORDER,'dimension':dim,'number_of_pieces':len(pieces),
                     'number_of_nonzero_gates':len(gate_rows),'gates':gate_rows,
                     'normal_coefficients':[algebra.serialize(a) for a in total_series[:ORDER+1]],
                     'first_omitted_coefficient':algebra.serialize(total_series[ORDER+1]),
                     'first_omitted_Frobenius_squared_exact':str(leading_sq),
                     'all_prescribed_commutators_and_parity_checks_exact':True,
                     'numerical_controls':numeric})
    result = {'status':'PASS','algebra_dependency_sha256':dep,'checks':rows,
              'elapsed_seconds':time.monotonic()-begin,
              'scope':'Exact term-ordered normal-form algebra and numerical remainder on a complete finite sector; the lattice locality proof is separate.'}
    (OUT/'FINITE_CIRCUIT_NORMAL_FORM_RECORD_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'PASS','elapsed_seconds':result['elapsed_seconds']}),flush=True)


if __name__ == '__main__':
    main()
