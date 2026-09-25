#!/usr/bin/env python3
"""Disclosed author controls; auxiliary models, not observed photon data."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ['docs/LOCAL_BACKGROUND_AND_UNRESTRICTED_ORIGINAL_RECORD_COUNTS_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/ORIGINAL_FORMATION_RECORD_PHOTON_READOUT_AND_MICROSCOPIC_FINITE_BINS_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/WEAK_FIELD_WAVE_PACKETS_FROM_MOBILE_RECORD_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md']
from pathlib import Path
from itertools import product, combinations
import hashlib, json, time, math
import numpy as np
import scipy
from scipy import sparse
from scipy.linalg import eigh
from scipy.sparse.linalg import expm_multiply
from numpy.polynomial.legendre import leggauss
import sympy as sp
ROOT_CONTROL_SOURCES = [('local-record-background-personal/local_background_controls.py', 'abd959ce389ce71f15108abdffdc97a49f7ad3d2baf40c8d0bf58f087f2a8807'), ('unrestricted-record-count-personal/count_window_controls.py', '86243d8f649124e09e52de0061f2b6af23337640fe3a90d0d58d3ad298dcdc6d')]
RESULT_PATH = 'outputs/unrestricted_original_records_20260924/UNRESTRICTED_ORIGINAL_RECORD_RESULTS.json'

def diagonal_rotor_control():
    x,y,z=sp.symbols('x y z', integer=True)
    d=(x-y)**2+(y-z)**2
    difference=sp.expand(d.subs(x,x+1)-d)
    assert sp.diff(difference,z)==0
    rows=[]
    phase_time=.173
    for cutoff in (1,2,4,8):
        far=0.; near=0.; count=0
        for a,b,c in product(range(-cutoff,cutoff+1),repeat=3):
            if a==cutoff: continue
            f=lambda aa,bb,cc: (aa-bb)**2+(bb-cc)**2
            phase=lambda aa,bb,cc: np.exp(1j*phase_time*(f(aa+1,bb,cc)-f(aa,bb,cc)))
            if c<cutoff:
                far=max(far,abs(phase(a,b,c+1)-phase(a,b,c)));count+=1
            if b<cutoff:
                near=max(near,abs(phase(a,b+1,c)-phase(a,b,c)))
        expected=2*abs(np.sin(phase_time))
        assert far<1e-14 and abs(near-expected)<1e-13
        rows.append({'cutoff':cutoff,'valid_far_shift_columns':count,
                     'far_commutator_norm':far,'near_commutator_norm':near,
                     'near_exact_norm':expected})
    return {'diagonal':'(E1-E2)^2+(E2-E3)^2',
            'first_shift_energy_difference':str(difference),'rows':rows}

def local(n,index,op):
    result=sparse.csr_matrix([[1.]])
    for site in range(n):
        result=sparse.kron(result,op if site==index else sparse.eye(2),format='csr')
    return result

def hermitian_norm(a):
    residual=np.linalg.norm(a-a.conj().T,ord='fro')
    assert residual<1e-10
    return float(np.max(np.abs(np.linalg.eigvalsh((a+a.conj().T)/2))))

def chain_control(n,K,delta=.4,kappa=.07,t=.2):
    # Pair creation raises number by two; the exchange Hamiltonian preserves
    # number. This chain has no cubic Gauss law or first-pair Wilson effect.
    raise_op=sparse.csr_matrix([[0.,0.],[1.,0.]])
    create=[local(n,i,raise_op) for i in range(n)]
    number=[c@c.T for c in create]
    ident=sparse.eye(2**n,format='csr')
    diagonal=sum(number[i]@number[i+1] for i in range(n-1))
    hopping=sum(create[i]@create[i+1].T+create[i+1]@create[i].T for i in range(n-1))
    h=K*diagonal+delta*hopping
    jumps=[create[i]@create[i+1] for i in range(n-1)]
    loss=[j.T@j for j in jumps]
    dissipator=sum(sparse.kron(j.T,j.T,format='csr')-
        .5*sparse.kron(ident,q,format='csr')-
        .5*sparse.kron(q.T,ident,format='csr') for j,q in zip(jumps,loss))
    generator=1j*(sparse.kron(ident,h,format='csr')-
                   sparse.kron(h.T,ident,format='csr'))+kappa*dissipator
    o=number[0].toarray()
    eigenvalues,eigenvectors=eigh(h.toarray())
    def evolve(v):
        unitary=(eigenvectors*np.exp(-1j*v*eigenvalues))@eigenvectors.conj().T
        return unitary.conj().T@o@unitary
    full=expm_multiply(t*generator,o.ravel(order='F')).reshape(o.shape,order='F')
    difference=hermitian_norm(full-evolve(t))
    def integral(order):
        nodes,weights=leggauss(order)
        vals=[]
        for v in t*(nodes+1)/2:
            ov=evolve(v)
            norms=[hermitian_norm(j.T@ov@j-.5*(q@ov+ov@q))
                   for j,q in zip(jumps,loss)]
            vals.append(sum(norms))
        return kappa*t*float(np.dot(weights,vals))/2
    coarse,fine=integral(20),integral(32)
    quadrature_delta=abs(coarse-fine)
    # A numerical corroboration of Duhamel's norm inequality, not an
    # interval proof of the integral or of the rotor/locality theorem.
    assert difference<=fine+max(1e-10,3*quadrature_delta)
    assert difference<=2*kappa*(n-1)*t+1e-10
    return {'sites':n,'K':K,'delta':delta,'kappa':kappa,'time':t,
            'local_observable_full_vs_hamiltonian_norm':difference,
            'summed_disturbance_integral_20':coarse,
            'summed_disturbance_integral_32':fine,
            'quadrature_difference':quadrature_delta,
            'global_trivial_bound':2*kappa*(n-1)*t}

def overlap_square(h, b):
    """Integrate the square of |[0,h] intersect (t-b,t)| piecewise."""
    nodes, weights = np.polynomial.legendre.leggauss(3)
    cuts = sorted(set([0.0, h, b, h + b]))
    integral = 0.0
    for left, right in zip(cuts, cuts[1:]):
        for x, w in zip(nodes, weights):
            t = (left + right) / 2 + (right - left) * x / 2
            length = max(0.0, min(h, t) - max(0.0, t - b))
            integral += (right - left) * w * length * length / 2
    return integral

def poisson_moment_controls():
    rows = []
    for h, b in [(0.4, 0.3), (0.2, 0.7), (0.5, 0.5), (1.0, 0.02)]:
        exact = min(h, b) ** 2 * max(h, b) - min(h, b) ** 3 / 3
        quadrature = overlap_square(h, b)
        assert abs(exact - quadrature) < 1e-14
        assert exact <= h * b * b + 1e-14
        for rj, rl in [(0.02, 0.03), (2.0, 3.0), (20.0, 30.0)]:
            mu = rj * rl * h * b
            second = mu * mu + mu + rj * rl * rl * h * b * b + rj * rj * rl * exact
            upper = mu * mu + mu * (1 + (rj + rl) * b)
            assert second <= upper + 1e-10
            variance = second - mu * mu
            assert variance >= mu - 1e-12
            rows.append(dict(h=h, b=b, r_j=rj, r_l=rl, mean=mu,
                             overlap_square_exact=exact,
                             overlap_square_quadrature=quadrature,
                             second_moment=second, proposed_second_bound=upper,
                             variance=variance,
                             bernoulli_variance_formula=mu * (1 - mu)))
    assert any(r['bernoulli_variance_formula'] < 0 for r in rows)
    return rows

def bin_pair_bounds(times, labels, bins, interval, lag):
    """Closed bin hulls give conservative bounds; word order resolves zero lag."""
    left, right = interval
    step = 1.0 / bins
    lower = actual = upper = 0
    for first, second in combinations(range(len(times)), 2):
        if labels[first] != 'j' or labels[second] != 'l':
            continue
        s, t = times[first], times[second]
        actual += int(left <= s <= right and 0 < t - s <= lag)
        i = min(math.floor(s / step), bins - 1)
        k = min(math.floor(t / step), bins - 1)
        slo, shi = i * step, (i + 1) * step
        tlo, thi = k * step, (k + 1) * step
        # Given the stored order, actual lag is positive even within a bin.
        lag_max = thi - slo
        lag_min = max(0.0, tlo - shi)
        forced = slo >= left and shi <= right and lag_max <= lag
        permitted = shi >= left and slo <= right and lag_min <= lag
        lower += int(forced)
        upper += int(permitted)
    return lower, actual, upper

def register_window_controls():
    labels = ['other', 'j', 'other', 'l', 'j', 'l']
    points = [0.03, 0.11, 0.20, 0.29, 0.38, 0.50, 0.60, 0.71, 0.83, 0.97]
    interval, lag = (0.2, 0.6), 0.3
    cap = len(labels) * (len(labels) - 1) // 2
    rows = []
    for bins in [4, 8, 16, 32]:
        checked = ambiguity = exact = square_gap = max_count = 0
        example = None
        for length in range(len(labels) + 1):
            for times in combinations(points, length):
                lower, count, upper = bin_pair_bounds(times, labels[:length], bins,
                                                     interval, lag)
                assert 0 <= lower <= count <= upper <= cap
                assert upper * upper - lower * lower <= 2 * cap * (upper - lower)
                checked += 1
                ambiguity += upper - lower
                square_gap += upper * upper - lower * lower
                exact += int(lower == upper)
                max_count = max(max_count, count)
                if count > 1 and example is None:
                    example = dict(times=times, labels=labels[:length],
                                   lower=lower, actual=count, upper=upper)
        assert max_count > 1
        rows.append(dict(bins=bins, mesh=1 / bins, histories_checked=checked,
                         aggregate_bracket_gap=ambiguity,
                         aggregate_square_bracket_gap=square_gap,
                         exact_brackets=exact, maximum_actual_count=max_count,
                         multiple_count_example=example))
    # These nested partitions must improve the information on every history.
    monotone_checks = 0
    for length in range(len(labels) + 1):
        for times in combinations(points, length):
            bounds = [bin_pair_bounds(times, labels[:length], bins, interval, lag)
                      for bins in [4, 8, 16, 32]]
            assert all(a[0] <= b[0] and b[2] <= a[2]
                       for a, b in zip(bounds, bounds[1:]))
            monotone_checks += 1
    return dict(rows=rows, nested_partition_histories=monotone_checks,
                event_cap=len(labels), universal_pair_cap=cap,
                interval=interval, lag=lag)

def main():
    start=time.monotonic()
    result={
      "scope":"Disclosed author auxiliary controls; no full cubic simulation or empirical fit.",
      "diagonal_rotor":diagonal_rotor_control(),
      "chain_rows":[chain_control(n,K,t=t) for n in (3,4,5,6) for K in (0.,3.,30.) for t in (.2,.7)],
      "poisson_proposal_rows":poisson_moment_controls(),
      "finite_history_register":register_window_controls(),
      "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      "elapsed_seconds":time.monotonic()-start,
      "all_assertions_passed":True}
    p=Path(__file__).resolve().parents[1]/RESULT_PATH
    p.parent.mkdir(parents=True,exist_ok=True)
    data=json.dumps(result,indent=2,allow_nan=False)+"\n"
    p.write_text(data); print(data,end="")
    print("TOTAL: PASS=4 FAIL=0")

if __name__=="__main__":main()
