#!/usr/bin/env python3
"""Disclosed primitive word and separate initial-balance controls.
The public rerun reuses both sources; it is not a new independent check.
"""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ['docs/INITIAL_CUBE_ENERGY_LAYER_AND_EXACT_BAND_BALANCE_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ACTUAL_CUBE_BIRTH_ENERGY_ON_THE_FAST_TIME_SCALE_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/FULL_ORIGINAL_CUBE_ENSEMBLE_ENERGY_AND_RARE_MATTER_FIELD_DENSITY_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/ORDINARY_MICROSCOPIC_CUBE_ENERGY_AFTER_THE_BIRTH_LAYER_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/SHARP_ACTUAL_ROTOR_CUBE_ENERGY_TAIL_BOUNDED_THEOREM_NOTE_2026-09-24.md']
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
import hashlib,json,time
import numpy as np
from numpy.polynomial.legendre import leggauss
A=(0,3,5,6);B=(1,2,4,7)
EDGES=tuple((a,b) for a in A for b in B if a^b in (1,2,4))
OMEGA=(tuple(1 if v in A else 0 for v in range(8)),(0,)*12)
RESULT_PATH='outputs/initial_cube_energy_balance_20260924/INITIAL_CUBE_ENERGY_BALANCE_RESULTS.json'
INDEPENDENT_SOURCE_SHA='c839ffaed8da4e2b8830807695e16b4aac2ec8944139288eec7df1fe2bf7c5fc'
ROOT_SOURCE_SHA='b86de88159b5593cb16c749edf2966499670a838a562b4de2857a9a2bf956d65'

def legal(word):
    q, electric = word
    div = [0] * 8
    for value, (a, b) in zip(electric, EDGES):
        div[a] += value
        div[b] -= value
    assert all(div[v] == q[v] - int(v in A) for v in range(8))
    assert sum(q) == 4 and all(x in (-1, 0, 1) for x in q)


def combine(*terms):
    out = defaultdict(Fraction)
    for factor, vector in terms:
        for word, coefficient in vector.items():
            out[word] += factor * coefficient
    return {word: c for word, c in out.items() if c}


def hop(vector, inward=False, center=None):
    out = defaultdict(Fraction)
    for (charges, electric), coefficient in vector.items():
        for index, (a, b) in enumerate(EDGES):
            if center is not None and a != center:
                continue
            src, dst = (b, a) if inward else (a, b)
            if not charges[src] or charges[dst]:
                continue
            q, fields = list(charges), list(electric)
            sign = q[src]
            q[src], q[dst] = 0, sign
            fields[index] += sign if inward else -sign
            word = tuple(q), tuple(fields)
            legal(word)
            out[word] += coefficient
    return dict(out)


def mark(vector, edge, signs):
    a, b = EDGES[edge]
    out = defaultdict(Fraction)
    for (charges, electric), coefficient in vector.items():
        if charges[a] or charges[b]:
            continue
        for sign in signs:
            q, fields = list(charges), list(electric)
            q[a], q[b] = sign, -sign
            fields[edge] += sign
            word = tuple(q), tuple(fields)
            legal(word)
            out[word] += coefficient
    return dict(out)


def norm2(vector):
    return sum((c * c for c in vector.values()), Fraction())


def primitive_words():
    initial = {OMEGA: Fraction(1)}
    f = hop(initial)
    f2 = hop(f)
    rows, totals = [], {}
    assert norm2(f) == 12 and norm2(f2) == 168
    for instrument, cases in [('resolved', [('plus', (1,)), ('minus', (-1,))]),
                              ('coherent', [('coherent', (1, -1))])]:
        total_b = total_r = total_c = Fraction()
        for edge, (a, b) in enumerate(EDGES):
            for name, signs in cases:
                beta = mark(f, edge, signs)
                remainder = combine((Fraction(1, 2), mark(f2, edge, signs)), (-1, hop(beta)))
                local = combine((-1, hop(beta, center=a)))
                assert remainder == local
                g = combine((1, hop(hop(remainder, inward=True))), (-1, hop(hop(remainder), inward=True)))
                loss_r = sum(norm2(mark(remainder, k, (s,))) for k in range(12) for s in (1, -1))
                loss_g = sum(norm2(mark(g, k, (s,))) for k in range(12) for s in (1, -1))
                nb, nr = norm2(beta), norm2(remainder)
                assert (nb, nr) == {'plus': (2, 4), 'minus': (2, 2), 'coherent': (4, 6)}[name]
                assert loss_r == 0 and loss_g == 24 * nr
                wrong = combine((1, mark(f2, edge, signs)), (-1, hop(beta)))
                mutation_error = norm2(combine((1, wrong), (-1, remainder)))
                assert mutation_error > 0
                total_b += nb
                total_r += nr
                total_c += loss_g
                rows.append({'edge': [a, b], 'mark': name, 'b': int(nb), 'r': int(nr),
                             'initial_loss_form': int(loss_r), 'loss_after_G': int(loss_g),
                             'wrong_half_factor_squared_residual': int(mutation_error)})
        assert (total_b, total_r, total_c) == (48, 72, 1728)
        totals[instrument] = {'sum_b': int(total_b), 'sum_r': int(total_r), 'sum_loss_after_G': int(total_c)}
    return {'F_Omega_norm_squared': 12, 'F_squared_Omega_norm_squared': 168,
            'initial_rotor_energy_over_delta': -84, 'rows': rows, 'totals': totals,
            'scope': 'New exact integer/rational rotor word calculation at zero field; no finite-spin dynamics or joint-limit simulation.'}


def phi_laplace(s,T):
    return 1/s-2/(T*s*s)+2*(-np.expm1(-s*T))/(T*T*s*s*s)


def mean(eps,t,a,b,lam,delta):
    return delta*a/(b-lam*eps*eps)*np.exp(-lam*t)*(-np.expm1(-(b/eps**2-lam)*t))


def controls():
    # Trace-one classical three-state Markov chain: q -> high with rate
    # a eps^2, q -> terminal with rate lam-a eps^2, high -> terminal at
    # b/eps^2. Energies are (0,delta eps^-4,0), initially q=1.
    a=.21;b=1.8;lam=.4;delta=1.3;T=1.4
    evalues=[.2,.1,.05,.025,.0125]
    initial=[];physical=[];distribution=[]
    nodes,weights=leggauss(160)
    impulse=delta*a/b
    limit_integral=impulse*(1-lam*phi_laplace(lam,T))
    for eps in evalues:
        assert lam-a*eps**2>0
        for tau in [0.,.2,1.,3.,10.]:
            t=eps**2*tau;m=mean(eps,t,a,b,lam,delta)
            high=m*eps**4/delta;q=np.exp(-lam*t);terminal=1-q-high
            assert min(q,high,terminal)>-1e-14
            target=impulse*(-np.expm1(-b*tau))
            initial.append(dict(epsilon=eps,tau=tau,mean=m,profile=target,
                                eps4_variance=delta*m-eps**4*m*m,
                                variance_profile=delta*target,probabilities=[q,high,terminal]))
        for t in [.2,.7,1.4]:
            m=mean(eps,t,a,b,lam,delta)
            gain=delta*a/eps**2*np.exp(-lam*t);loss=b/eps**2*m
            deriv=delta*a/(b-lam*eps**2)*(-lam*np.exp(-lam*t)+b/eps**2*np.exp(-b*t/eps**2))
            assert abs((gain-loss)-deriv)<2e-10
            physical.append(dict(epsilon=eps,t=t,mean=m,
                                 mean_limit=impulse*np.exp(-lam*t),
                                 eps2_gain=eps**2*gain,eps2_loss=eps**2*loss,
                                 common_scaled_flow=delta*a*np.exp(-lam*t),
                                 net_power=deriv,regular_power_limit=-lam*impulse*np.exp(-lam*t)))
        # Test phi(t)=(1-t/T)^2, zero after T; C1 at T. Its integral
        # against power has a short positive term and a regular negative term.
        exact=delta*a/(b-lam*eps**2)*(-lam*phi_laplace(lam,T)+b/eps**2*phi_laplace(b/eps**2,T))
        cap=min(T/eps**2,40/b)
        tau=(nodes+1)*cap/2
        fast_quad=b*cap/2*np.dot(weights,(1-eps**2*tau/T)**2*np.exp(-b*tau))
        checked=delta*a/(b-lam*eps**2)*(fast_quad-lam*phi_laplace(lam,T))
        assert abs(exact-checked)<2e-13
        distribution.append(dict(epsilon=eps,test_integral=exact,
                                 limit_including_initial_impulse=limit_integral,
                                 omitted_impulse_mutant_limit=limit_integral-impulse,
                                 fast_age_quadrature_error=abs(exact-checked)))
    # An exact band-loss term need not be nonnegative when the density has
    # interband coherence, even though Gamma itself is positive.
    Hband=np.diag([0.,2.]);Gamma=np.array([[1.,.6],[.6,1.]])
    A=(Hband@Gamma+Gamma@Hband)/2
    values,vectors=np.linalg.eigh(A);psi=vectors[:,0]
    negative=float(np.vdot(psi,A@psi).real)
    assert negative<0 and np.linalg.eigvalsh(Gamma).min()>0
    return {'parameters':dict(a=a,b=b,lam=lam,delta=delta,T=T),
            'initial_profile_rows':initial,'physical_flow_rows':physical,
            'distribution_rows':distribution,'impulse':impulse,
            'loss_sign_control':{'Hband':Hband.tolist(),'Gamma':Gamma.tolist(),
                                 'state':psi.tolist(),'band_loss':negative,
                                 'exact_smallest_eigenvalue':1-np.sqrt(1+.6**2)},
            'scope':'Separate trace-one three-state Markov injection/depletion model and a two-band algebra control. No actual cube dynamics, large-spin convergence proof, physical reservoir, or independent reconstruction. The omitted-impulse mutant is an actually evaluated wrong limiting expression, not a modified microscopic evolution.'}


def main():
    start=time.monotonic()
    result={'primitive_words':primitive_words(),'cascade':controls(),
            'elapsed_seconds':time.monotonic()-start,
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'provenance':{'reused_independent_primitive':INDEPENDENT_SOURCE_SHA,'reused_root_cascade':ROOT_SOURCE_SHA}}
    p=Path(__file__).resolve().parents[1]/RESULT_PATH;p.parent.mkdir(parents=True,exist_ok=True)
    text=json.dumps(result,indent=2)+'\n';p.write_text(text);print(text,end='',flush=True)
    print('TOTAL: PASS=2 FAIL=0',flush=True)

if __name__=='__main__':main()
