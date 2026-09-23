#!/usr/bin/env python3
"""Finite challenges to sampled magnetic events and excursions, not a phase or chessboard proof.

Geometry is reconstructed from oriented endpoints. The compact single-face
heat equation is evaluated independently in Fourier and finite-difference
bases. Neither finite-dimensional calculation is the full spatial model.
"""
AUDIT_TIMEOUT_SEC = 120
AUDIT_MEMORY_MB = 512
AUDIT_INPUT_PATHS = ['docs/COMPACT_ROTOR_SAMPLED_MAGNETIC_EVENT_BOUNDED_THEOREM_NOTE_2026-09-16.md', 'docs/COMPACT_ROTOR_MAGNETIC_EXCURSION_BOUNDED_THEOREM_NOTE_2026-09-16.md']
EXPECTED_INPUT_SHA256 = {'docs/COMPACT_ROTOR_SAMPLED_MAGNETIC_EVENT_BOUNDED_THEOREM_NOTE_2026-09-16.md': 'aa61782c652fb722b65832dceed9b309e63a8bdae67cb6045830a2a974eb8ccc', 'docs/COMPACT_ROTOR_MAGNETIC_EXCURSION_BOUNDED_THEOREM_NOTE_2026-09-16.md': 'c68e64839af884757499eb5223a479f7ad32aba3f339198fc2e2b5845816db7e'}

# Numerical fixtures remain defined below. Declared proof inputs and this
# source are hash-bound; JSON diagnostics alone are not audit verdicts.

from collections import Counter
from itertools import combinations, product
from pathlib import Path
import hashlib
import json
import math
import time

import numpy as np
from scipy.integrate import quad
from scipy.linalg import eigh_tridiagonal
from scipy.sparse import diags
from scipy.sparse.linalg import expm_multiply


def shift(x, i, amount, L):
    y = list(x)
    y[i] = (y[i] + amount) % L
    return tuple(y)


def face(x, i, j, L):
    return {(x, i): 1, (shift(x, i, 1, L), j): 1,
            (shift(x, j, 1, L), i): -1, (x, j): -1}


def signature(f):
    return tuple(sorted(f.items()))


def mapped_face(corners, L):
    ans = Counter()
    for x, y in zip(corners, corners[1:] + corners[:1]):
        delta = [(y[i] - x[i]) % L for i in range(3)]
        nz = [i for i, a in enumerate(delta) if a]
        assert len(nz) == 1, (x, y, delta)
        i = nz[0]
        if delta[i] == 1:
            ans[(x, i)] += 1
        else:
            assert delta[i] == L - 1
            ans[(y, i)] -= 1
    return dict(ans)


def geometry():
    rows = []
    for L in (4, 6, 8):
        vertices = list(product(range(L), repeat=3))
        N = L**3
        lookup = {}
        all_faces = []
        for ij in combinations(range(3), 2):
            for x in vertices:
                f = face(x, *ij, L)
                lookup[signature(f)] = (x, ij, 1)
                lookup[signature({e: -v for e, v in f.items()})] = (x, ij, -1)
                all_faces.append((x, ij, f))
        assert len(lookup) == 6*N
        for i, j in combinations(range(3), 2):
            k = next(r for r in range(3) if r not in (i, j))
            for b in (0, 1):
                corners = []
                for a, d in ((0, 0), (1, 0), (1, 1), (0, 1)):
                    c = [0, 0, 0]
                    c[i], c[j], c[k] = a, d, b
                    corners.append(tuple(c))
                seen, signs = Counter(), Counter()
                for x in vertices:
                    transformed = [tuple((x[r] + (c[r] if x[r] % 2 == 0
                                                  else 1-c[r])) % L
                                         for r in range(3)) for c in corners]
                    anchor, ij, sign = lookup[signature(mapped_face(transformed, L))]
                    assert ij == (i, j)
                    assert anchor[k] % 2 == b
                    seen[anchor] += 1
                    signs[sign] += 1
                assert len(seen) == N//2
                assert set(seen.values()) == {2}
                packed = [x for x in seen if (x[i]+x[j]) % 2 == 0]
                edges = Counter(e for x in packed for e in face(x, i, j, L))
                assert len(packed) == N//4
                assert max(edges.values()) == 1
                rows.append(dict(L=L, orientation=[i,j], normal_face=b,
                                 distinct_faces=len(seen), multiplicity=2,
                                 independent_faces=len(packed), signs=dict(signs)))
        # No face crosses a vertex reflection plane into both open halves.
        for r in range(3):
            for plane in range(L):
                boundary_count = 0
                for x, ij, f in all_faces:
                    support = set()
                    for (y, axis) in f:
                        support.add(y)
                        support.add(shift(y, axis, 1, L))
                    d = {(y[r]-plane) % L for y in support}
                    positive = any(0 < a < L//2 for a in d)
                    negative = any(L//2 < a < L for a in d)
                    assert not (positive and negative)
                    if not positive and not negative:
                        boundary_count += 1
                    # Pull back the reflected actual endpoints and check C.
                    reflected = Counter()
                    for (y, axis), sign in f.items():
                        z = shift(y, axis, 1, L)
                        ry, rz = list(y), list(z)
                        ry[r], rz[r] = (2*plane-y[r]) % L, (2*plane-z[r]) % L
                        ry, rz = tuple(ry), tuple(rz)
                        if (rz[axis]-ry[axis]) % L == 1:
                            reflected[(ry,axis)] += sign
                        else:
                            reflected[(rz,axis)] -= sign
                    assert signature(dict(reflected)) in lookup
                assert boundary_count == 2*L*L
    time_rows = []
    for M in (2,4,6,8,10):
        for b in (0,1):
            seen = Counter((n+(b if n % 2 == 0 else 1-b)) % M for n in range(M))
            assert len(seen) == M//2 and set(seen.values()) == {2}
            assert all(n % 2 == b for n in seen)
            time_rows.append(dict(M=M, base_endpoint=b, distinct_times=len(seen),
                                  endpoint_multiplicity=2, whole_intervals=M))
    return dict(spatial=rows, temporal=time_rows)


def trial_and_parameters():
    v = 1/3 - 2/math.pi**2
    C0 = 3*math.pi**2/16 + 12*v
    trials = []
    for g in (0.01, 0.2, 1.0):
        a = math.sqrt(2)*g
        f = lambda x: math.sqrt(2*math.pi/a)*math.cos(math.pi*x/(2*a))
        df = lambda x: -math.sqrt(2*math.pi/a)*math.pi/(2*a)*math.sin(math.pi*x/(2*a))
        norm = quad(lambda x: f(x)**2/(2*math.pi), -a, a, epsabs=1e-11)[0]
        derivative = quad(lambda x: df(x)**2/(2*math.pi), -a, a, epsabs=1e-10)[0]
        variance = quad(lambda x: x*x*f(x)**2/(2*math.pi), -a, a, epsabs=1e-12)[0]
        assert abs(norm-1) < 1e-12
        assert abs(derivative/(math.pi**2/(4*a*a))-1) < 1e-12
        assert abs(variance/(a*a*v)-1) < 1e-12
        # Exact product-state mean cosine uses independent one-link transforms.
        cosine = quad(lambda x: math.cos(x)*f(x)**2/(2*math.pi), -a,a,epsabs=1e-12)[0]
        energy_per_vertex = 3*g*g*derivative/2 + 3*(1-cosine**4)/(g*g)
        assert energy_per_vertex <= C0+2e-10
        trials.append(dict(g=g, norm=norm, derivative=derivative, variance=variance,
                           exact_product_energy_per_vertex=energy_per_vertex, bound=C0))
    alpha = math.pi/3
    c = 1-math.cos(alpha/2)
    T = alpha/(16*math.sqrt(2*c))
    rows = []
    for g in (.1,.05,.02,.015,.01,.008):
        sample = min(0, math.log(17)/8 + C0*T - 2*T*c/(8*g*g))
        excursion = min(0, math.log(17)/4 + C0*T - T*c/(4*g*g))
        pe = min(1,6*math.exp(excursion/6))
        assert excursion >= sample
        rows.append(dict(g=g, log_epsilon_sample=sample, log_epsilon_excursion=excursion,
                         epsilon_excursion=math.exp(excursion), p_excursion=pe,
                         degree_squared_times_p=64*pe))
    selected = next(x for x in rows if x['g'] == .01)
    assert selected['degree_squared_times_p'] < .41
    # Threshold follows by solving the explicit logarithmic inequality, not a sweep.
    g_sufficient = math.sqrt((T*c/24)/(math.log(384)+math.log(17)/24+C0*T/6))
    assert .01 < g_sufficient < .011
    return dict(trial_integrals=trials, C0=C0, alpha=alpha, T=T,
                sampled_rate=2*T*c, excursion_rate=T*c,
                sufficient_g_strictly_below=g_sufficient, rows=rows)


def fourier_survival(g, tau, theta, cutoff):
    n = np.arange(-cutoff,cutoff+1)
    diag = 2*g*g*n*n + 1/(g*g)
    off = np.full(2*cutoff,-.5/(g*g))
    vals, vecs = eigh_tridiagonal(diag,off)
    coeff = vecs @ (np.exp(-tau*vals)*vecs[cutoff,:])
    return float(np.dot(np.cos(theta*n),coeff))


def difference_survival(g,tau,n):
    # Positive nearest-neighbor approximation to the circle diffusion.
    h = 2*math.pi/n
    theta = np.arange(n)*h
    rate = 2*g*g/(h*h)  # F=sum of FOUR link angles, diffusivity 2g^2.
    H = diags([np.full(n-1,-rate),2*rate+(1-np.cos(theta))/(g*g),
               np.full(n-1,-rate)],[-1,0,1],format='lil')
    H[0,n-1] = H[n-1,0] = -rate
    ans = expm_multiply(-tau*H.tocsr(),np.ones(n))
    assert np.min(ans) >= -1e-12 and np.max(ans) <= 1+1e-12
    return float(ans[n//6])


def rotor_checks():
    # This is the exact one-face compact rotor after reducing its free
    # diffusion to the sum of four independent circle Brownian angles.
    # No sampled Brownian trajectories or full-lattice numerical claim.
    alpha = math.pi/3
    T = alpha/(16*math.sqrt(2*(1-math.cos(alpha/2))))
    tau = 2*T
    rows = []
    for g in (.25,.15,.1,.08):
        f48 = fourier_survival(g,tau,alpha,48)
        f64 = fourier_survival(g,tau,alpha,64)
        assert abs(f48-f64) < 1e-10
        fd = [difference_survival(g,tau,n) for n in (384,768,1536)]
        assert abs(fd[-1]-f64) < 2e-5
        assert abs(fd[-1]-f64) <= abs(fd[0]-f64)+1e-12
        q = min(1, math.exp(-tau*(1-math.cos(alpha/2))/(g*g))
                   +16*math.exp(-alpha*alpha/(128*g*g*tau)))
        assert -1e-11 <= f64 <= q+1e-11
        rows.append(dict(g=g,tau=tau,start_flux=alpha,Fourier48=f48,Fourier64=f64,
                         FD_meshes=[384,768,1536],FD_values=fd,Brownian_upper_bound=q,
                         FD_relative_difference=abs(fd[-1]-f64)/abs(f64)))
    # Formula-sensitive negative control: a one-link diffusivity silently
    # substituted for a four-link face must be detectably different.
    g=.25
    wrong = fourier_survival(g/math.sqrt(2),tau/2,alpha,48)
    correct = fourier_survival(g,tau,alpha,48)
    assert abs(wrong-correct) > 1e-5
    return dict(one_face_rows=rows,
                wrong_diffusivity_control=dict(correct=correct,wrong=wrong),
                limitations='Finite Fourier and positive mesh checks are not rigorous tail enclosures or full-volume phase evidence.')


def main():
    started = time.monotonic()
    ans = dict(scope=__doc__,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               geometry=geometry(),parameters=trial_and_parameters(),rotor=rotor_checks())
    ans['elapsed_seconds']=time.monotonic()-started
    ans['status']='PERSONAL_CHECKS_COMPLETED'
    _emit(ans)




def _check_inputs():
    root = Path(__file__).resolve().parents[1]
    for name in AUDIT_INPUT_PATHS:
        if hashlib.sha256((root / name).read_bytes()).hexdigest() != EXPECTED_INPUT_SHA256[name]:
            raise RuntimeError("input identity mismatch: " + name)

def _emit(report):
    report["input_sha256"] = dict(EXPECTED_INPUT_SHA256)
    report["completed_diagnostic_families"] = 3
    report["total_unit"] = "completed diagnostic families, not dynamic assertions"
    report["static_source_assert_statements"] = 27
    output = Path(__file__).resolve().parents[1] / "logs" / "runner-cache" / (Path(__file__).stem + ".json")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))
    print("TOTAL: PASS=3 FAIL=0")
    print('per_element: all original oriented faces, trial integrals and compact one-face heat comparisons.')
    print('per_site: periodic geometry L=4,6,8 and all original reflection planes.')
    print('per_mode: Fourier cutoffs48/64 and finite-difference meshes384/768/1536; no rigorous tail enclosure.')
    print('per_block: sampled and excursion parameter constants at the original fixed couplings.')
    print('lattice_wide: checked and not executed — full lattice ground law and infinite-volume theorem are analytic, not numerically sampled.')

if __name__ == '__main__':
    _check_inputs()
    main()
