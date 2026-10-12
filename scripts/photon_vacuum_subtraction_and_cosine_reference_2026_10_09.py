#!/usr/bin/env python3
"""Author checks of the complete vacuum-subtracted quartic photon coefficient.

No repository or empirical data is read by this runner; its cache binds the
paired source note as a declared input. Exact finite Fock dictionaries use unnormalized
occupation monomials and their factorial inner product; Fourier checks float.
This does not test the compact Hamiltonian or establish an all-volume remainder.
"""
import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['OMP_NUM_THREADS'] = '1'
os.environ['MKL_NUM_THREADS'] = '1'
from fractions import Fraction as F
from itertools import product
import math
import sys
import time

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ("docs/PHOTON_VACUUM_SUBTRACTION_AND_COSINE_REFERENCE_BOUNDED_THEOREM_NOTE_2026-10-09.md",)

started = time.monotonic()
passed = 0


def check(label, condition, detail=''):
    global passed
    if not condition:
        raise AssertionError(label + ': ' + str(detail))
    passed += 1
    print('PASS', label, detail, flush=True)


def add(*vectors):
    out = {}
    for vec in vectors:
        for n, x in vec.items():
            out[n] = out.get(n, F(0)) + x
    return {n: x for n, x in out.items() if x}


def scale(vec, x):
    return {n: x*y for n, y in vec.items() if x*y}


def inner(a, b):
    return sum((x*b.get(n, 0)*math.prod(math.factorial(i) for i in n)
                for n, x in a.items()), F(0))


def create(vec, j):
    out = {}
    for n, x in vec.items():
        m = list(n)
        m[j] += 1
        out[tuple(m)] = x
    return out


def annihilate(vec, j):
    out = {}
    for n, x in vec.items():
        if n[j]:
            m = list(n)
            m[j] -= 1
            out[tuple(m)] = x*n[j]
    return out


def apply_field(vec, row):
    return add(*(scale(add(create(vec, j), annihilate(vec, j)), v)
                 for j, v in enumerate(row) if v))


def potential(vec, rows, power, coefficient):
    out = {}
    for row in rows:
        v = vec
        for _ in range(power):
            v = apply_field(v, row)
        out = add(out, scale(v, coefficient))
    return out


def resolve(vec, frequencies, offset):
    out = {}
    for n, x in vec.items():
        den = sum((w*i for w, i in zip(frequencies, n)), F(0)) + offset
        assert den > 0, (n, den)
        out[n] = x/den
    return out


def exact_family(copies):
    # Constant variance, exact diagonal harmonic Gram matrix, two degeneracies.
    # The frequencies lie below three times their minimum, avoiding resonances.
    hadamard = [(1, 1, 1, 1), (1, -1, 1, -1),
                (1, 1, -1, -1), (1, -1, -1, 1)]
    root_half_w = [F(1, 2), F(1, 2), F(3, 4), F(3, 4)]
    w = [2*x*x for x in root_half_w]*copies
    rows = []
    for block in range(copies):
        for signs in hadamard:
            row = [F(0)]*len(w)
            row[4*block:4*block+4] = [s*x/2 for s, x in zip(signs, root_half_w)]
            rows.append(row)
    c = sum((v*v for v in rows[0]), F(0))
    vacuum = {(0,)*len(w): F(1)}
    basis = [create(vacuum, j) for j in range(len(w))]
    v4 = lambda vec: potential(vec, rows, 4, -F(1, 24))
    v6 = lambda vec: potential(vec, rows, 6, F(1, 720))
    v4vac = v4(vacuum)
    mean4 = inner(vacuum, v4vac)
    mean6 = inner(vacuum, v6(vacuum))
    v0 = add(v4vac, scale(vacuum, -mean4))
    vacuum_form = inner(v0, resolve(v0, w, F(0)))
    c3, s, u = {}, {}, {}
    for j in range(4):
        applied = v4(basis[j])
        u[j] = {n: x for n, x in applied.items() if sum(n) != 1}
        s[j] = create(v0, j)
        c3[j] = add(u[j], scale(s[j], -1))
        assert all(sum(n) == 3 for n in c3[j])
    largest_error = F(0)
    spectator_error = F(0)
    matrices = []
    cross_values = []
    control_omit_cross = False
    control_omit_plus = False
    control_no_vacuum_subtraction = False
    for pair in [(0, 1), (2, 3)]:
        mat = []
        for i in pair:
            row = []
            for j in pair:
                delta = int(i == j)
                km = inner(c3[i], resolve(c3[j], w, -w[j]))
                kp = inner(c3[i], resolve(c3[j], w, w[j]))
                direct6 = inner(basis[i], v6(basis[j])) - mean6*delta
                direct_r = inner(u[i], resolve(u[j], w, -w[j]))
                direct = direct6 - direct_r + vacuum_form*delta
                predicted = -c*c*w[j]*delta/32 - km - kp
                cross = inner(s[i], resolve(c3[j], w, -w[j]))
                spectator = inner(s[i], resolve(s[j], w, -w[j])) - vacuum_form*delta
                spectator_error = max(spectator_error, abs(direct6-c*c*w[j]*delta/16),
                                      abs(cross-c*c*w[j]*delta/32),
                                      abs(spectator-c*c*w[j]*delta/32-kp))
                assert direct6 == c*c*w[j]*delta/16
                assert cross == c*c*w[j]*delta/32
                assert spectator == c*c*w[j]*delta/32 + kp
                assert direct == predicted
                largest_error = max(largest_error, abs(direct-predicted))
                row.append(str(direct))
                if i == j:
                    cross_values.append(str(cross))
                    control_omit_cross |= direct != predicted+2*cross
                    control_omit_plus |= direct != predicted+kp
                    control_no_vacuum_subtraction |= direct != direct6-direct_r
            mat.append(row)
        matrices.append(mat)
    check('exact_full_gap_identity_copies_'+str(copies), largest_error == 0,
          {'c': str(c), 'vacuum_resolvent': str(vacuum_form), 'gap_matrices': matrices})
    check('exact_spectator_and_cross_copies_'+str(copies), spectator_error == 0,
          'cross diagonal '+str(cross_values))
    check('missing_interference_control_copies_'+str(copies), control_omit_cross)
    check('missing_exchange_plus_control_copies_'+str(copies), control_omit_plus)
    check('missing_vacuum_subtraction_control_copies_'+str(copies), control_no_vacuum_subtraction)
    return vacuum_form, matrices


print('Python', sys.version.split()[0], flush=True)
reference = None
base_vac = None
for copies in (1, 2, 3):
    vac, matrices = exact_family(copies)
    if reference is None:
        reference, base_vac = matrices, vac
    else:
        check('exact_extensive_cancellation_copies_'+str(copies),
              vac == copies*base_vac and matrices == reference,
              'vacuum term grows exactly; the complete gap coefficient stays fixed')

# Direct single oscillator, with omega=1/2 and B=(a+a^dag)/2.
w = [F(1, 2)]
rows = [[F(1, 2)]]
vac = {(0,): F(1)}
one = {(1,): F(1)}
v4 = lambda v: potential(v, rows, 4, -F(1, 24))
v6 = lambda v: potential(v, rows, 6, F(1, 720))
def second(vec, energy):
    a = v4(vec)
    a = {n: x for n, x in a.items() if sum((w[i]*n[i] for i in range(len(w))), F(0)) != energy}
    return inner(vec, v6(vec))-inner(a, resolve(a, w, -energy))
single_gap = second(one, w[0])-second(vac, F(0))
check('single_oscillator_complete_g4', single_gap == -F(1, 512), str(single_gap))

import numpy as np
print('NumPy', np.__version__, flush=True)
for L in (3, 4):
    pts = list(product(range(L), repeat=3))
    N = L**3
    zero = (0, 0, 0)
    wf = {p: math.sqrt(sum(abs(np.exp(2j*np.pi*p[i]/L)-1)**2 for i in range(3))) for p in pts}
    c = sum(wf.values())/(3*N)
    fs = {}
    for p in pts:
        if p == zero:
            continue
        d = np.exp(2j*np.pi*np.array(p)/L)-1
        omega = wf[p]
        pol = []
        for z in np.eye(3, dtype=complex):
            z = z-d*np.vdot(d, z)/(omega*omega)
            for e in pol:
                z = z-e*np.vdot(e, z)
            norm = np.linalg.norm(z)
            if norm > 1e-9:
                pol.append(z/norm)
            if len(pol) == 2:
                break
        curl = np.zeros((3, 3), dtype=complex)
        for o, (i, j) in enumerate([(0, 1), (0, 2), (1, 2)]):
            curl[o, j] = d[i]
            curl[o, i] = -d[j]
        fs[p] = curl@np.column_stack(pol)/math.sqrt(2*omega)
    gram_error = max(np.linalg.norm(z.conj().T@z-wf[p]*np.eye(2)/2) for p,z in fs.items())
    covariance = sum((np.sum(np.abs(z)**2, axis=1) for z in fs.values()))/N
    check("fourier_reference_gram_L"+str(L), gram_error < 2e-12
          and np.max(np.abs(covariance-c)) < 2e-12,
          {"gram_residual": float(gram_error), "plaquette_variance": covariance.tolist()})
    for k in [(1, 0, 0), (1, 1, 0), (1, 1, 1)]:
        omega = wf[k]
        minus = np.zeros((2, 2), dtype=complex)
        plus = np.zeros((2, 2), dtype=complex)
        occupation_amplitudes = {}
        for p, q in product(fs, repeat=2):
            r = tuple((k[i]-p[i]-q[i]) % L for i in range(3))
            if r == zero:
                continue
            energy = wf[p]+wf[q]+wf[r]
            assert energy-omega > 0
            for a, b, cc in product(range(2), repeat=3):
                tensor = fs[k].T@(fs[p][:, a].conj()*fs[q][:, b].conj()*fs[r][:, cc].conj())/N
                occupation = tuple(sorted(((p, a), (q, b), (r, cc))))
                occupation_amplitudes.setdefault(occupation, np.zeros(2, dtype=complex))
                occupation_amplitudes[occupation] -= tensor/6
                outer = np.outer(tensor.conj(), tensor)/6
                minus += outer/(energy-omega)
                plus += outer/(energy+omega)
        # Independent Bose contraction: combine ordered vertices into actual
        # occupation monomials, then use their factorial inner products.
        direct_minus = np.zeros((2, 2), dtype=complex)
        direct_plus = np.zeros((2, 2), dtype=complex)
        for occupation, amplitude in occupation_amplitudes.items():
            multiplicity = math.prod(math.factorial(occupation.count(mode)) for mode in set(occupation))
            energy = sum(wf[mode[0]] for mode in occupation)
            gram = multiplicity*np.outer(amplitude.conj(), amplitude)
            direct_minus += gram/(energy-omega)
            direct_plus += gram/(energy+omega)
        fock_error = max(np.linalg.norm(direct_minus-minus), np.linalg.norm(direct_plus-plus))
        check('fourier_to_occupation_resolvent_L'+str(L)+'_k'+str(k),
              fock_error < 1e-11*omega,
              {'residual': float(fock_error), 'occupation_monomials': len(occupation_amplitudes)})
        gap4 = -c*c*omega*np.eye(2)/32-minus-plus
        em = np.linalg.eigvalsh(minus)/omega
        ep = np.linalg.eigvalsh(plus)/omega
        eg = np.linalg.eigvalsh(gap4)/omega
        tag = 'L'+str(L)+'_k'+str(k)
        check('fourier_positive_forms_'+tag, em[0] >= -1e-13 and ep[0] >= -1e-13,
              {'Kminus/omega': em.tolist(), 'Kplus/omega': ep.tolist()})
        check('fourier_uniform_gap_coefficient_'+tag,
              em[-1] <= 1+1e-12 and ep[-1] <= 1/3+1e-12
              and eg[0] >= -65/48-1e-12 and eg[-1] <= -c*c/32+1e-12,
              {'c': c, 'D4/omega': eg.tolist()})

def full_cosine_one_mode(g, cutoff):
    # Finite normal-ordered even polynomial, with the exact cosine coefficients.
    # No series remainder is inferred from this floating convergence diagnostic.
    v, omega, c = 0.5, 0.5, 0.25
    y = g*g*c
    r = math.exp(-y/2)
    t = math.expm1(-y/2)/2
    h = {2: t*v*v}
    connected = {}
    for m in range(4, cutoff+1, 2):
        coefficient = r*(-1)**(m//2+1)*g**(m-2)/math.factorial(m)
        h[m] = coefficient*v**m
        connected[m-1] = m*coefficient*v**m
    spectator = {m+1: z for m, z in h.items()}
    u = {n: spectator.get(n, 0)+connected.get(n, 0)
         for n in set(spectator) | set(connected)}
    vac = sum(math.factorial(m)*z*z/(m*omega) for m, z in h.items())
    direct = sum(math.factorial(n)*z*z/((n-1)*omega) for n, z in u.items())-vac
    km = sum(math.factorial(n)*z*z/((n-1)*omega) for n, z in connected.items())
    kp = sum(math.factorial(n)*z*z/((n+1)*omega) for n, z in connected.items())
    cross = sum(math.factorial(n)*spectator.get(n, 0)*z/((n-1)*omega)
                for n, z in connected.items())
    x2 = -t*r*y*omega/8
    higher = cross-x2
    formula = t*t*omega/2+km+kp+2*cross
    # Taylor remainder bound avoids subtracting nearly equal cosh terms.
    cross_tail_bound = math.exp(-y)*omega*y**3*math.cosh(y)/192
    assert abs(direct-formula) < 1e-16
    assert -cross_tail_bound-1e-18 <= higher <= 1e-18
    return direct/omega, higher/omega


for g in (0.125, 0.25, 0.5):
    s10, x10 = full_cosine_one_mode(g, 10)
    s14, x14 = full_cosine_one_mode(g, 14)
    check('full_cosine_one_mode_cancellation_g'+str(g), abs(s10-s14) < 1e-14,
          {'Sg/omega_cutoff10': s10, 'Sg/omega_cutoff14': s14,
           'higher_cross/omega': x14,
           'scope': 'normal-ordered truncation diagnostic, not a compact-spectrum test'})

print('elapsed_sec', format(time.monotonic()-started, '.4f'), flush=True)
print('TOTAL: PASS='+str(passed)+' FAIL=0', flush=True)

print("per_element: exact occupation coefficients and factorial inner products were evaluated.")
print("per_site: Fourier plaquette variances and harmonic Gram normalization were checked on L=3,4.")
print("per_mode: two-polarization forms were sampled at six nonzero lattice momenta.")
print("per_block: one, two and three independent oscillator blocks tested extensive vacuum cancellation.")
print("lattice_wide: finite Fourier boxes were executed; uniform-volume and full-series results are analytic proofs.")
