#!/usr/bin/env python3
"""Disclosed author reference and primitive controls; no empirical fit."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/ORIGINAL_RECORD_CALIBRATION_AND_PREPARED_MATTER_PROBE_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/WEAK_FIELD_WAVE_PACKETS_FROM_MOBILE_RECORD_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/ORIGINAL_FORMATION_RECORD_PHOTON_READOUT_AND_MICROSCOPIC_FINITE_BINS_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/LOCAL_BACKGROUND_AND_UNRESTRICTED_ORIGINAL_RECORD_COUNTS_BOUNDED_THEOREM_NOTE_2026-09-24.md')
from collections import Counter, deque, defaultdict
from fractions import Fraction
from itertools import product
from pathlib import Path
from math import factorial, pi, sqrt
import contextlib, io, hashlib, json, math, time
import numpy as np
from scipy.special import eval_genlaguerre, eval_hermite
from scipy.linalg import expm
ROOT_CONTROL_SOURCES = [('record-observable-calibration-personal/observable_calibration_controls.py', 'f6a4fe09dbb8c2ec88197db4868466b3c3f5531b63cc0c56bf3909c6da56eec8'), ('prepared-matter-probe-personal/prepared_probe_controls.py', '27da3c4fdff89c16e4c15c96e41296f2ae51964c6048b727c07c2b55cba9683c')]
RESULT_PATH = 'outputs/prepared_original_record_probe_20260924/PREPARED_ORIGINAL_RECORD_PROBE_RESULTS.json'

def displacement_element(m, n, z):
    lower, upper = min(m, n), max(m, n)
    return (np.exp(-z*z/2) * sqrt(factorial(lower)/factorial(upper))
            * (1j*z)**(upper-lower) * eval_genlaguerre(lower, upper-lower, z*z))

def characteristic(state, d, g, t, frequencies):
    result = 0j
    for m, cm in state.items():
        for n, cn in state.items():
            phase = np.exp(1j*np.dot(frequencies, np.subtract(m, n))*t)
            factors = np.prod([displacement_element(mm, nn, g*dd)
                               for mm, nn, dd in zip(m, n, d)])
            result += cm.conjugate()*cn*phase*factors
    return result

def quadrature_characteristic(state, d, g, t, frequencies, order):
    q, w = np.polynomial.hermite.hermgauss(order)
    q1, q2 = np.meshgrid(q, q, indexing='ij')
    weight = np.outer(w, w)/pi
    wave = np.zeros((order, order), dtype=complex)
    for n, cn in state.items():
        polynomial = (eval_hermite(n[0], q1)*eval_hermite(n[1], q2)
                      / sqrt(2**sum(n)*factorial(n[0])*factorial(n[1])))
        wave += cn*np.exp(-1j*np.dot(frequencies, n)*t)*polynomial
    norm = np.sum(weight*abs(wave)**2)
    assert abs(norm-1) < 2e-14
    return np.sum(weight*abs(wave)**2*np.exp(1j*g*sqrt(2)*(d[0]*q1+d[1]*q2)))

def lower(state, mode):
    output = {}
    for n, cn in state.items():
        if n[mode]:
            m = list(n); m[mode] -= 1; m = tuple(m)
            output[m] = output.get(m, 0j)+sqrt(n[mode])*cn
    return output

def inner(left, right):
    return sum(c.conjugate()*right.get(n, 0j) for n, c in left.items())

def moment_data(state, d, t, frequencies):
    lowered = [lower(state, r) for r in range(2)]
    normal = anomalous = 0j
    for r in range(2):
        for s in range(2):
            normal += d[r]*d[s]*np.exp(1j*(frequencies[r]-frequencies[s])*t)*inner(lowered[r], lowered[s])
            anomalous += d[r]*d[s]*np.exp(-1j*(frequencies[r]+frequencies[s])*t)*inner(state, lower(lowered[s], r))
    assert abs(normal.imag) < 1e-13
    return float(normal.real), anomalous

def primitive_control():
    side=6
    vertices=list(product(range(side),repeat=3))
    is_a=lambda v:sum(v)%2==0
    def neighbors(v):
        for axis in range(3):
            for sign in (-1,1):
                w=list(v);w[axis]=(w[axis]+sign)%side;yield tuple(w)
    def edge(x,y):
        return (x,y) if is_a(x) else (y,x)
    def key(flow):
        return tuple(sorted((a,b,int(v)) for (a,b),v in flow.items() if v))
    def divergence(flow):
        out=Counter()
        for (x,y),v in flow.items():out[x]+=v;out[y]-=v
        return {x:v for x,v in out.items() if v}
    def path(start,end):
        before={start:None};q=deque([start])
        while end not in before:
            x=q.popleft()
            for y in neighbors(x):
                if y not in before:before[y]=x;q.append(y)
        route=[end]
        while route[-1]!=start:route.append(before[route[-1]])
        return route[::-1]
    a=(0,0,0);d=(1,1,0);h=(2,2,0)
    c=(1,0,0);e=(0,1,0);b=(5,0,0)
    fixed=[(0,5,0),(0,0,1),(0,0,5)]
    common=Counter();routes=[]
    for start,end in [(d,fixed[0]),(h,fixed[1]),(h,fixed[2])]:
        route=path(start,end);routes.append(route)
        for x,y in zip(route,route[1:]):common[edge(x,y)]+=(-1 if is_a(x) else 1)
    expected={d:-1,h:-2,**{v:1 for v in fixed}}
    assert divergence(common)==expected
    loop=Counter({(a,c):1,(d,c):-1,(d,e):1,(a,e):-1})
    baseline={v:1 for v in vertices if is_a(v)}
    def gauss(charges,flow):
        delta={v:charges.get(v,0)-baseline.get(v,0) for v in vertices}
        delta={v:q for v,q in delta.items() if q}
        assert divergence(flow)==delta
    rows=[];outputs_by_sign={}
    for sigma in (-1,1):
        outputs=[]
        for occupied,empty,phase in [(c,e,1),(e,c,-1)]:
            initial=baseline.copy();initial[d]=initial[h]=-1
            for v in fixed+[occupied]:initial[v]=1
            incoming=common.copy();incoming[d,occupied]-=1
            gauss(initial,incoming)
            retained=[];blocked_birth=0
            for destination in neighbors(a):
                if initial.get(destination,0):continue
                after=initial.copy();charge=after.pop(a);after[destination]=charge
                flow=incoming.copy();flow[a,destination]-=charge
                if after.get(b,0):blocked_birth+=1;continue
                assert not after.get(a,0)
                after[a]=sigma;after[b]=-sigma;flow[a,b]+=sigma
                gauss(after,flow)
                retained.append((tuple(sorted(after.items())),key(flow),phase))
            assert len(retained)==1 and blocked_birth==1
            outputs+=retained
            for winding in range(-2,3):
                shifted=incoming.copy()
                for link,value in loop.items():shifted[link]+=winding*value
                gauss(initial,shifted)
            rows.append(dict(sigma=sigma,initial_occupied_variable=occupied,
                             initial_records=len(initial),output_records=len(dict(retained[0][0])),
                             retained_paths=1,outward_to_birth_site_rejected=1,
                             physical_flux_cases_checked=5))
        assert outputs[0][0]==outputs[1][0]
        coefficients=Counter()
        for left,right in product(outputs,repeat=2):
            fleft=Counter({(x,y):v for x,y,v in left[1]})
            fright=Counter({(x,y):v for x,y,v in right[1]})
            diff=Counter(fright)
            for link,value in fleft.items():diff[link]-=value
            coefficients[key(diff)]+=Fraction(left[2]*right[2],2)
        negative=Counter({link:-value for link,value in loop.items()})
        assert coefficients==Counter({():Fraction(1),key(loop):Fraction(-1,2),key(negative):Fraction(-1,2)})
        outputs_by_sign[str(sigma)]=dict(identity='1',cycle='-1/2',inverse_cycle='-1/2',
                                       dephased_identity='1',dephased_cycle='0')
    return dict(scope='Exact original selected primitive on the side-six cubic graph; no full Hamiltonian propagation.',
                common_flow=key(common),common_flow_paths=routes,rows=rows,
                effects=outputs_by_sign,gauss_checks='both charged branches and every listed loop flux satisfy div E=q-1_A')

def timing_probability(g,b,one,order):
    q,w=np.polynomial.hermite.hermgauss(order)
    dark=np.array([1.,-1.])/math.sqrt(2)
    h=np.diag([1.,-1.])/(g*g)
    values=[]
    for x in q:
        angle=math.sqrt(2)*g*x
        jump=np.array([np.exp(.5j*angle),np.exp(-.5j*angle)])
        loss=np.outer(jump.conj(),jump)
        final=expm(b*(-1j*h-.5*loss))@dark
        probability=1-float(np.vdot(final,final).real)
        values.append(probability*(2*x*x if one else 1.))
    return float(np.dot(w,values)/math.sqrt(math.pi))

def timing_control():
    rows=[];max_refinement=0.
    for g in (.4,.2,.1,.05,.025):
        for exponent in (3.5,2.):
            b=g**exponent
            vals=[]
            for one in (False,True):
                coarse=timing_probability(g,b,one,24)
                fine=timing_probability(g,b,one,32)
                max_refinement=max(max_refinement,abs(coarse-fine)/(b*g*g))
                assert abs(coarse-fine)<2e-13
                vals.append(fine)
            assert vals[1]>vals[0]
            rows.append(dict(g=g,window_exponent=exponent,window=b,
                             vacuum_probability=vals[0],one_probability=vals[1],
                             vacuum_over_b_g2=vals[0]/(b*g*g),
                             one_over_b_g2=vals[1]/(b*g*g),
                             excess_over_b_g2=(vals[1]-vals[0])/(b*g*g)))
    small=rows[-2]
    assert abs(small['vacuum_over_b_g2']-.5)<.025
    assert abs(small['excess_over_b_g2']-1)<.003
    assert rows[-1]['vacuum_over_b_g2']>100
    return dict(scope='Separate two coherent input states and one absorbing state at each Gaussian angle. '
                      'kappa=tau=1, matter splitting g^-2, one selected jump and its full loss. '
                      'No cubic electric term, Gauss constraint, other original channels or microscopic limit in this timing toy.',
                rows=rows,maximum_scaled_quadrature_refinement=max_refinement,
                no_uniform_optimal_window_claim=True)

def calibration_control_group():
    start = time.perf_counter()
    # A three-row curl-like test matrix, not an actual periodic cubic curl.
    curl = np.array([[1/sqrt(2), 1], [1/sqrt(2), -1], [0, sqrt(2)]])
    lambdas = np.array([1., 4.]); frequencies = np.sqrt(lambdas)
    assert np.max(abs(curl.T@curl-np.diag(lambdas))) < 1e-14
    drows = curl/np.sqrt(2*np.sqrt(lambdas))[None, :]
    assert np.max(abs(drows.T@drows-np.diag(np.sqrt(lambdas)/2))) < 1e-14
    states = {
        'one_in_first': {(1, 0): 1.+0j},
        'one_two_mode_superposition': {(1, 0): 1/sqrt(2)+0j, (0, 1): 1j/sqrt(2)},
        'vacuum_plus_two': {(0, 0): sqrt(.9)+0j, (2, 0): sqrt(.1)+0j},
        'vacuum_minus_two': {(0, 0): sqrt(.9)+0j, (2, 0): -sqrt(.1)+0j},
    }
    rows = []; average_rows = []; max_quad = 0.; max_refinement = 0.
    for name, state in states.items():
        assert abs(inner(state, state)-1) < 1e-14
        energy = sum(abs(c)**2*np.dot(frequencies, n) for n, c in state.items())
        eta = np.array([inner(state, lower(lower(state, r), r)) for r in range(2)])
        for t in (0., .4, 1.1):
            leading = np.array([2*(n+a.real) for n, a in
                                (moment_data(state, d, t, frequencies) for d in drows)])
            sum_formula = energy+np.sum(frequencies*(eta*np.exp(-2j*frequencies*t)).real)
            assert abs(sum(leading)-sum_formula) < 1e-13
            for g in (.2, .1, .05):
                exact = []; errors = []
                for d in drows:
                    val = characteristic(state, d, g, t, frequencies)
                    quad = quadrature_characteristic(state, d, g, t, frequencies, 20)
                    fine = quadrature_characteristic(state, d, g, t, frequencies, 28)
                    max_quad = max(max_quad, abs(val-fine))
                    max_refinement = max(max_refinement, abs(quad-fine))
                    assert abs(val-fine) < 2e-13 and abs(quad-fine) < 2e-13
                    vacuum = np.exp(-g*g*np.dot(d, d)/2)
                    exact.append(float(2*(vacuum-val.real)/(g*g)))
                residual = np.array(exact)-leading
                rows.append(dict(state=name, t=t, g=g, energy=float(energy),
                                 deficit_over_g_squared=exact,
                                 leading_quadratic_response=leading.tolist(),
                                 maximum_scaled_remainder=float(max(abs(residual))/(g*g))))
        for window in (.3, 2., 20.):
            exact_average = float(energy+np.sum(frequencies*(eta*np.exp(-1j*frequencies*window)).real
                                               *np.sinc(frequencies*window/pi)))
            bound = float(sum(abs(eta))/window)
            assert abs(exact_average-energy) <= bound+1e-14
            average_rows.append(dict(state=name, time_window=window,
                                     averaged_leading_response=exact_average,
                                     excitation_energy=float(energy), oscillatory_bound=bound))
    phase = dict(p=.1, same_occupation=.2,
                 plus=.2+sqrt(.18), minus=.2-sqrt(.18))
    assert phase['plus'] > 0 and phase['minus'] < 0
    benchmark = dict(source='Brouri et al quant-ph/0007032v1 equations1-2 and Fig3 caption',
                     signal_fraction=.34, corrected_g2_zero=0.,
                     corresponding_raw_normalized_coincidence=1-.34**2,
                     poisson_reference_bin_counts=5780*5990*1e-9*11450,
                     scope='Printed-parameter arithmetic only, not digitized data or a model fit.')
    assert .84 < benchmark['corresponding_raw_normalized_coincidence'] < 1
    output = dict(scope='Finite two-mode harmonic reference and printed benchmark arithmetic; '
                       'no original cubic dynamics, full detector simulation, empirical fit or universal no-go.',
                  response_rows=rows, time_average_rows=average_rows,
                  same_energy_phase_example=phase, empirical_normalization_check=benchmark,
                  maximum_characteristic_quadrature_error=float(max_quad),
                  maximum_quadrature_refinement_error=float(max_refinement),
                  elapsed_seconds=time.perf_counter()-start)
    print(json.dumps(output, indent=2, allow_nan=False))
    print('per_element: finite reference characteristic elements checked against independent quadrature.')
    print('per_site: checked and not executed — no physical single-site detector dynamics is simulated.')
    print('per_mode: finite occupation and equal-energy phase-sensitive reference examples are exercised.')
    print('per_block: a two-mode, three-probe harmonic block checks anomalous and ordinary second moments.')
    print('lattice_wide: checked and not executed — the full cubic curl identity is analytic, not simulated here.')

def main():
    start=time.perf_counter()
    buffer=io.StringIO()
    with contextlib.redirect_stdout(buffer):calibration_control_group()
    raw=buffer.getvalue();calibration,end=json.JSONDecoder().raw_decode(raw)
    certificates=raw[end:].strip().splitlines()
    assert len(certificates)==5
    result={"scope":"Disclosed author controls; separate harmonic, original primitive and auxiliary timing scopes.",
            "calibration":calibration,"calibration_certificates":certificates,
            "prepared_primitive":primitive_control(),"separate_timing":timing_control(),
            "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "elapsed_seconds":time.perf_counter()-start,"all_assertions_passed":True}
    p=Path(__file__).resolve().parents[1]/RESULT_PATH;p.parent.mkdir(parents=True,exist_ok=True)
    data=json.dumps(result,indent=2,allow_nan=False)+"\n";p.write_text(data);print(data,end="")
    print("TOTAL_PASS: 3")

if __name__=="__main__":main()
