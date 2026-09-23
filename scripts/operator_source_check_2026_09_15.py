"""Finite matrix/cycle identities and exact Fourier-mode source checks.

The matrix phase inputs are exact rationals from the separately constructed
free cubical complex. Source checks use periodic single modes (real and
imaginary parts are real tests), not an asserted compact-source scaling proof.
"""

# Canonical packaging; supplied scientific fixtures below are unchanged.
AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ['docs/SIGNED_FOREST_FIXED_ORDER_REMAINDERS_AND_RESTRICTED_LOOP_SUMS_BOUNDED_THEOREM_NOTE_2026-09-15.md']
from pathlib import Path as _InputPath
_REPO_ROOT = _InputPath(__file__).resolve().parents[1]
_INPUT_TEXT = {q: (_REPO_ROOT / q).read_text() for q in AUDIT_INPUT_PATHS}
assert 'signed_forest_fixed_order_remainders_and_restricted_loop_sums_bounded_theorem_note_2026-09-15' in _INPUT_TEXT['docs/SIGNED_FOREST_FIXED_ORDER_REMAINDERS_AND_RESTRICTED_LOOP_SUMS_BOUNDED_THEOREM_NOTE_2026-09-15.md']
_OUTPUT_JSON = _REPO_ROOT / 'logs/runner-cache/operator_source_check_2026_09_15.json'
_OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
import itertools
import json
import math
from pathlib import Path

import mpmath as mp
import numpy as np


def cycles():
    rng = np.random.default_rng(531809)
    rows = []
    for shape in [(2,2), (3,4), (5,6)]:
        T = rng.normal(size=shape)
        T *= .3/np.linalg.norm(T,2)
        A, B = T.T@T, T@T.T
        tr4 = np.trace(A@A)
        direct = sum(T[j,i]*T[j,k]*T[l,k]*T[l,i]
                     for i,k in itertools.permutations(range(shape[1]),2)
                     for j,l in itertools.permutations(range(shape[0]),2))
        formula = tr4-np.sum(np.diag(A)**2)-np.sum(np.diag(B)**2)+np.sum(T**4)
        assert abs(direct-formula)<2e-16
        assert abs(direct)<=tr4+1e-16
        eigen = np.linalg.eigvalsh(A)
        closed = np.sum(eigen-np.log1p(eigen))
        partial = sum((-1)**r*np.trace(np.linalg.matrix_power(A,r))/r
                      for r in range(2,20))
        assert abs(closed-partial)<1e-16
        tail_majorant = np.trace(A)*.3**2/(2*(1-.3**2))
        assert abs(closed)<=tail_majorant
        rows.append(dict(shape=shape, distinct_cycle=direct, trace_four=tr4,
                         logdet_sum=closed, majorant=tail_majorant))

    mp.mp.dps=70
    raw=[mp.mpf(3256681)/4643045, -mp.mpf(211582)/4643045,
         mp.mpf(496)/3905, mp.mpf(63)/3905]
    # Electric index first in the source receipt; transpose to m-by-e matrix.
    T=np.array([float(mp.sin(6*mp.pi*x)) for x in raw]).reshape(2,2).T
    distinct = 4*np.prod(T)
    assert distinct < -.3
    trace = np.trace((T.T@T)@(T.T@T))
    assert trace > 0 and abs(distinct)<=trace
    # Reject the incorrect claim that removing repeated labels preserves sign.
    negative_control = distinct < 0 < trace

    x=mp.mpf(4096)
    M2=32*1562500*mp.exp(-x/64)/(1-100608*mp.exp(-x/64))
    M6=2*1562500*4**6*mp.exp(-x/64)/(1-25755648*mp.exp(-x/64))
    rho=x*M2+x**3*M6/6
    assert rho<mp.mpf('3e-8')
    return dict(matrix_rows=rows, compatible_distinct_cycle=distinct,
                compatible_unrestricted_trace=trace,
                repeated_label_positivity_negative_control=bool(negative_control),
                half_measure_rho_upper=str(rho), orientation_included_upper=str(2*rho))


def geometric(k,R):
    return sum(np.exp(1j*k*x) for x in range(R))


def sources():
    rows=[]
    for L in [32,64,128,256]:
        a=2*math.pi/L
        k=a*np.array([1.,2.,1.,1.])
        d=np.exp(1j*k)-1
        lap=float(np.sum(abs(d)**2))
        # h_12=a^2 exp(ik.x). Exact finite-difference exterior symbols.
        ue=a*a*np.array([-d[1].conjugate(),d[0].conjugate()])/lap
        um=a*a*np.array([d[2],d[3]])/lap
        ph=a*a*(abs(d[0])**2+abs(d[1])**2)/lap
        qh=a*a*(abs(d[2])**2+abs(d[3])**2)/lap
        max_u=max(abs(ue).max(),abs(um).max())
        max_grad=max_u*max(abs(d))
        assert max_u<=2*a and max_grad<=4*a*a
        row=dict(L=L,a=a,potential_over_a=float(max_u/a),
                 gradient_over_a2=float(max_grad/(a*a)),rectangles=[])
        for R in [1,2,4,L//4]:
            # Electric plaquette rectangle in directions 1,2. Its boundary
            # is the oriented bottom/right/top/left current, mass 4R.
            boundary=(ue[0]*(1-np.exp(1j*k[1]*R))*geometric(k[0],R)
                      +ue[1]*(np.exp(1j*k[0]*R)-1)*geometric(k[1],R))
            fill=ph*geometric(k[0],R)*geometric(k[1],R)
            assert abs(boundary-fill)<2e-14
            # Magnetic fill has orientation 1,2, and varies across 3,4.
            # q=B n has the dual rectangular boundary, also mass 4R.
            dual_boundary=(um[0]*(np.exp(-1j*k[2])-1)*geometric(k[2],R)*geometric(k[3],R)
                           +um[1]*(np.exp(-1j*k[3])-1)*geometric(k[2],R)*geometric(k[3],R))
            dual_fill=qh*geometric(k[2],R)*geometric(k[3],R)
            assert abs(dual_boundary-dual_fill)<2e-14
            mass=4*R
            bound=16*min(a*mass,a*a*mass*mass)
            assert abs(fill)<=bound and abs(dual_fill)<=bound
            row['rectangles'].append(dict(R=R,mass=mass,electric_pair_abs=float(abs(fill)),
                                           magnetic_pair_abs=float(abs(dual_fill)),bound=bound))
        # A single edge is not closed: its mode response is O(a), not O(a^2).
        row['nonclosed_edge_over_a2']=float(abs(ue[0])/(a*a))
        rows.append(row)
    assert rows[-1]['nonclosed_edge_over_a2']>7*rows[0]['nonclosed_edge_over_a2']
    return rows


def main():
    out=dict(status='finite_cycle_and_source_checks_passed',cycles=cycles(),sources=sources(),
             scope='Matrix identities and periodic Fourier-mode diagnostics; '
                   'no interacting cumulants, infinite-volume proof, or independent review.')
    _OUTPUT_JSON.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'cycles':out['cycles'],
                      'source_scales':[(r['L'],r['potential_over_a'],r['gradient_over_a2'],
                                        r['nonclosed_edge_over_a2']) for r in out['sources']]},indent=2))


if __name__=='__main__':
    main()

if __name__ == '__main__':
    print('TOTAL: PASS=1 FAIL=0')
    print('Completed family: complete finite companion program; individual checks and diagnostics remain in structured JSON')
    print('per_element: finite cochain, signed phase, partition and derivative fixtures')
    print('per_site: finite source-support configurations only')
    print('per_mode: finite matrix/operator directions; no all-order or infinite-kernel execution')
    print('per_block: one complete companion family; imported helpers are shared implementation, not independent evidence')
    print('lattice_wide: analytical claims and infinite/iterated limits checked in written proof, not executed here')
