#!/usr/bin/env python3
"""Exact cube formation dynamics and bounded numerical response diagnostics.

All integer rotor words are explicit. Discovery stops only at exact closure
or an explicitly reported resource ceiling, never at a field cutoff.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import hashlib
import json

A = tuple(v for v in range(8) if v.bit_count() % 2 == 0)
B = tuple(v for v in range(8) if v not in A)
EDGES = tuple((a, b) for a in A for b in B if (a ^ b) in (1, 2, 4))
EI = {edge: i for i, edge in enumerate(EDGES)}
NB = {v: tuple(w for w in range(8) if (v ^ w) in (1, 2, 4)) for v in range(8)}
PAIRS = tuple((a, c) for a, c in combinations(A, 2) if set(NB[a]) & set(NB[c]))
MARKS = tuple((a, b, sig) for a, b in EDGES for sig in (-1, 1))
OMEGA = (tuple(int(v in A) for v in range(8)), (0,) * len(EDGES))


def clean(x):
    return {k: v for k, v in x.items() if v}


def gauss(s):
    q, e = s
    div = [0] * 8
    for (a, b), x in zip(EDGES, e):
        div[a] += x
        div[b] -= x
    return tuple(div) == tuple(q[v] - int(v in A) for v in range(8))


def make(q, e):
    s = tuple(q), tuple(e)
    assert gauss(s), s
    return s


def D(s):
    q, e = s
    assert all(q[a] for a in A)
    ans = sum(x * (x - q[a]) for (a, b), x in zip(EDGES, e) if q[b] == 0)
    assert ans >= 0 and ans % 2 == 0
    return ans


@lru_cache(None)
def outward(s, a):
    q, e = s
    if q[a] == 0:
        return ()
    out = []
    for b in NB[a]:
        if q[b] == 0:
            qq, ee = list(q), list(e)
            qq[a], qq[b] = 0, q[a]
            ee[EI[a, b]] -= q[a]
            out.append(make(qq, ee))
    return tuple(out)


@lru_cache(None)
def inward(s, a):
    q, e = s
    if q[a]:
        return ()
    out = []
    for b in NB[a]:
        if q[b]:
            qq, ee = list(q), list(e)
            qq[a], qq[b] = q[b], 0
            ee[EI[a, b]] += q[b]
            out.append(make(qq, ee))
    return tuple(out)


def born(s, mark, adjoint=False):
    a, b, sig = mark
    q, e = s
    if adjoint:
        if q[a] != sig or q[b] != -sig:
            return ()
        qq, ee = list(q), list(e)
        qq[a] = qq[b] = 0
        ee[EI[a, b]] -= sig
    else:
        if q[a] or q[b]:
            return ()
        qq, ee = list(q), list(e)
        qq[a], qq[b] = sig, -sig
        ee[EI[a, b]] += sig
    return (make(qq, ee),)


@lru_cache(None)
def jump(s, mark):
    out = Counter()
    for t in outward(s, mark[0]):
        out.update(born(t, mark))
    return clean(out)


@lru_cache(None)
def jump_adj(s, mark):
    out = Counter()
    for t in born(s, mark, True):
        out.update(inward(t, mark[0]))
    return clean(out)


@lru_cache(None)
def h4(s):
    out = Counter()
    for a, c in PAIRS:
        for t in outward(s, a):
            for u in outward(t, c):
                for v in inward(u, c):
                    for w in inward(v, a):
                        out[w] -= 2
    return clean(out)


@lru_cache(None)
def loss(s):
    out = Counter()
    for mark in MARKS:
        for t, j in jump(s, mark).items():
            for u, k in jump_adj(t, mark).items():
                out[u] += j * k
    return clean(out)


def shifted(s, z):
    return make(s[0], [e + x for e, x in zip(s[1], z)])


def loops():
    out = []
    for fixed in (1, 2, 4):
        u, v = [x for x in (1, 2, 4) if x != fixed]
        for base in (0, fixed):
            verts = [base, base ^ u, base ^ u ^ v, base ^ v, base]
            z = [0] * len(EDGES)
            for x, y in zip(verts, verts[1:]):
                a, b = (x, y) if x in A else (y, x)
                z[EI[a, b]] += 1 if x in A else -1
            out.append(tuple(z))
    assert len(set(out)) == 6
    return tuple(out)


def component(seeds, ceiling):
    todo = deque(sorted(seeds))
    seen = set(todo)
    processed = 0
    while todo:
        s = todo.popleft()
        assert D(s) == 0
        for op in (h4, loss):
            for t in op(s):
                if D(t) == 0 and t not in seen:
                    seen.add(t)
                    todo.append(t)
                    if len(seen) > ceiling:
                        return sorted(seen), False, processed
        processed += 1
    return sorted(seen), True, processed


def matrix_rows(basis, op):
    ix = {s: i for i, s in enumerate(basis)}
    rows, outside = [], []
    for j, s in enumerate(basis):
        for t, coeff in op(s).items():
            if D(t) == 0:
                assert t in ix
                rows.append([ix[t], j, coeff])
            else:
                outside.append([j, list(t[0]), list(t[1]), D(t), coeff])
    d = {(i, j): v for i, j, v in rows}
    assert all(d.get((j, i)) == v for (i, j), v in d.items())
    return sorted(rows), outside


AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    'docs/CUBE_FORMATION_MATTER_FLUX_DYNAMICS_AND_STRONG_ELECTRIC_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-26.md',
    'docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md',
    'docs/LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md',
    'scripts/cube_formation_incidence_2026_09_26.py',
)
import cube_formation_incidence_2026_09_26 as independent


def exact_construction():
    assert gauss(OMEGA) and D(OMEGA)==0
    first={str(m):jump(OMEGA,m) for m in MARKS}
    assert all(sum(v*v for v in x.values())==2 for x in first.values())
    assert loss(OMEGA)=={OMEGA:48}
    assert h4(OMEGA)[OMEGA]==-84
    assert sorted(h4(OMEGA).values())==[-84]+[-2]*12
    assert all(D(s)==4 for s in h4(OMEGA) if s!=OMEGA)
    seeds=set().union(*(x.keys() for x in first.values()))
    assert all(D(s)==0 for s in seeds)
    basis,closed,processed=component(seeds,10000)
    assert closed, 'Resource guard: closure unestablished'
    hrows,hout=matrix_rows(basis,h4); grows,gout=matrix_rows(basis,loss)
    ix={s:i for i,s in enumerate(basis)}
    istates,ih,ig,ij=independent.reconstruct()
    assert istates==set(basis)
    assert {(ix[s],ix[t]):v for (s,t),v in ih.items()}=={(i,j):v for i,j,v in hrows}
    assert {(ix[s],ix[t]):v for (s,t),v in ig.items()}=={(i,j):v for i,j,v in grows}
    terminal=sorted({t for s in basis for m in MARKS for t in jump(s,m)})
    ti={t:i for i,t in enumerate(terminal)}
    jrows=[]
    for j,s in enumerate(basis):
        for m in MARKS:
            for t,v in jump(s,m).items():
                assert ij[m,t][s]==v
                jrows.append([*m,ti[t],j,v])
    assert {(m,t,s):v for (m,t),row in ij.items() for s,v in row.items()}=={
        ((a,b,sig),terminal[i],basis[j]):v for a,b,sig,i,j,v in jrows}
    for t in terminal:
        assert all(t[0]) and D(t)==0 and not h4(t) and not loss(t)
    assert len(seeds)==36 and len(basis)==252 and len(terminal)==816
    assert max(abs(e) for q,es in basis for e in es)==1
    assert max(abs(e) for q,es in terminal for e in es)==2
    assert sum(i!=j for i,j,v in hrows)==2232
    assert all(i==j or (basis[i][0]!=basis[j][0] and basis[i][1]!=basis[j][1]) for i,j,v in hrows)
    assert all(v==-14 for i,j,v in hrows if i==j)
    assert all(v==8 for i,j,v in grows if i==j)
    print('Exact primitive paths agree with independently derived full incidence matrices and jumps.')
    print('Coordinate closure:',len(basis),'first seeds:',len(seeds),'terminal:',len(terminal))
    print('Projected H/G entries:',len(hrows),len(grows),'unprojected nonzero-D paths retained:',len(hout),len(gout))
    # A short complete path, followed by an exact H^3 coefficient check.
    start=min(ix[s] for s in first[str((0,1,-1))])
    adj={i:[] for i in range(len(basis))}
    hd={(i,j):v for i,j,v in hrows}
    for i,j,v in hrows:
        if i!=j:adj[j].append(i)
    todo=deque([start]);prev={start:None};target=None
    while todo:
        j=todo.popleft()
        if j!=start and basis[j][0]==basis[start][0]:target=j;break
        for i in sorted(adj[j]):
            if i not in prev:prev[i]=j;todo.append(i)
    assert target is not None
    path=[];current=target
    while current is not None:path.append(current);current=prev[current]
    path.reverse()
    assert len(path)==4
    coeff=[hd[y,x] for x,y in zip(path,path[1:])]
    z=tuple(b-a for a,b in zip(basis[path[0]][1],basis[path[-1]][1]))
    assert sum(bool(e) for e in z)==4 and all(abs(e)<=1 for e in z)
    assert gauss((tuple(int(v in A) for v in range(8)),z))
    power={start:1}
    for _ in range(3):
        out=Counter()
        for j,v in power.items():
            for i in range(len(basis)):
                if (i,j) in hd:out[i]+=hd[i,j]*v
        power=clean(out)
    assert coeff==[-2,-2,-2] and power[target]==-8
    print('Loop-return witness:',json.dumps({'states':[basis[i] for i in path],'coefficients':coeff,'delta_E':z,'H_cubed_entry':power[target]}))
    d={'edges':EDGES,'loops':loops(),'basis':basis,'terminal':terminal,'H4':hrows,
       'Gamma_over_kappa':grows,'jumps':jrows,
       'first_outputs':{k:[[ix[s],v] for s,v in x.items()] for k,x in first.items()}}
    print('Exact reconstructed payload sha256:',hashlib.sha256(json.dumps(d,sort_keys=True,separators=(',',':')).encode()).hexdigest())
    return d

import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import expm


def matrix(rows, n):
    a = np.zeros((n, n), dtype=np.int64)
    for i, j, v in rows:
        a[i, j] = v
    return a


def sine_quarter(n):
    return (0, 1, 0, -1)[int(n) % 4]


def calculate(d):
    basis, terminal = d['basis'], d['terminal']
    n, m = len(basis), len(terminal)
    h = matrix(d['H4'], n)
    gamma = matrix(d['Gamma_over_kappa'], n)
    # Supplied ratio, fixed before the test; magnetic time u=delta*t.
    r = 1.0
    generator = -1j * h - r * gamma / 2
    edge = (0, 1)
    z = np.array(d['loops'][0], dtype=np.int64)
    observables = {
        'survival': (np.ones(n), np.zeros(m)),
        'charge_at_0': (np.array([q[0] for q, e in basis]), np.array([q[0] for q, e in terminal])),
        'occupancy_at_7': (np.array([abs(q[7]) for q, e in basis]), np.ones(m)),
        'sine_electric_circulation': (np.array([sine_quarter(z @ e) for q, e in basis]),
                                      np.array([sine_quarter(z @ e) for q, e in terminal])),
    }
    jumps = {}
    for a, b, sig, i, j, amp in d['jumps']:
        mark = (a, b, sig)
        if mark not in jumps:
            jumps[mark] = np.zeros((m, n), dtype=np.int64)
        jumps[mark][i, j] += amp
    # Diagonal terminal observables make opposite newborn signs orthogonal;
    # check actual coherent and resolved recycling adjoints rather than assume.
    qops = []
    for name, (ob, ot) in observables.items():
        qo = sum(j.T @ (ot[:, None] * j) for j in jumps.values())
        coherent = [jumps[a, b, -1] + jumps[a, b, 1] for a, b in d['edges']]
        qc = sum(j.T @ (ot[:, None] * j) for j in coherent)
        assert np.array_equal(qo, qc)
        qops.append(qo)
    ob = np.array([v[0] for v in observables.values()])
    qops = np.array(qops)
    outcomes = {}
    for convention in ('resolved_minus', 'resolved_plus', 'coherent'):
        v = np.zeros(n, dtype=np.int64)
        signs = (-1, 1) if convention == 'coherent' else ((-1,) if convention.endswith('minus') else (1,))
        for sig in signs:
            for i, amp in d['first_outputs'][str((*edge, sig))]:
                v[i] += amp
        norm = int(v @ v)
        psi0 = v.astype(complex) / np.sqrt(norm)
        o = observables['sine_electric_circulation'][0].astype(np.int64)
        phi0 = o * psi0
        # Exact integer numerators for unitary curvature and impulse slope.
        h_v = h @ v
        h2_v = h @ h_v
        exact = {}
        for name, (ov, _) in observables.items():
            ov = ov.astype(np.int64)
            curvature = int(2 * (h_v @ (ov * h_v)) - 2 * ((ov * v) @ h2_v))
            impulse = int(sum(v[i] * h[i, j] * (ov[i] - ov[j])**2 * v[j]
                              for i in np.flatnonzero(v) for j in np.flatnonzero(v)))
            exact[name] = {'unitary_second_derivative_numerator': curvature,
                           'impulse_initial_slope_numerator': impulse, 'denominator': norm}

        def rhs(u, y):
            psi, phi = y[:n], y[n:2*n]
            terminal_rates = r * np.einsum('i,aij,j->a', psi.conj(), qops, psi, optimize=True)
            response_rate = 2*r*np.imag(psi.conj() @ qops[-1] @ phi)
            return np.concatenate((generator @ psi, generator @ phi, terminal_rates, [response_rate]))

        y0 = np.concatenate((psi0, phi0, np.zeros(len(observables)+1)))
        times = np.array([0, .01, .05, .1, .25, .5, 1.0])
        sol = solve_ivp(rhs, (0, times[-1]), y0, t_eval=times, rtol=2e-11, atol=2e-13,
                        method='DOP853')
        assert sol.success
        rows = []
        for u, y in zip(sol.t, sol.y.T):
            psi, phi = y[:n], y[n:2*n]
            vals = np.einsum('i,ai,i->a', psi.conj(), ob, psi).real + y[2*n:2*n+len(observables)].real
            resp = 2*np.imag(psi.conj() @ (o*phi)) + y[-1].real
            rows.append({'magnetic_time': float(u), **dict(zip(observables, map(float, vals))),
                         'bounded_electric_impulse_response': float(resp)})
        direct = expm(generator * times[-1]) @ psi0
        error = float(np.linalg.norm(direct-sol.y[:n, -1]))
        assert error < 1e-9
        # Full trace equals survival + all terminal probability; directly integrate
        # its analytic derivative -<Gamma> + sum ||B psi||^2 = 0.
        assert np.array_equal(sum(j.T @ j for j in jumps.values()), gamma)
        outcomes[convention] = {'norm_squared': norm, 'exact_initial_moments': exact,
                               'time_rows': rows, 'exponential_crosscheck_error': error,
                               'ode_function_evaluations': sol.nfev}
    return {'status': 'primary_numerical_diagnostic_of_exact_projected_generator',
            'kappa_over_delta_supplied': r, 'first_edge': edge, 'electric_loop': z.tolist(),
            'full_trace_identity_exact': True,
            'H_Gamma_commutator_max_abs': int(np.max(np.abs(h @ gamma-gamma @ h))),
            'outcomes': outcomes}


if __name__ == '__main__':
    result=calculate(exact_construction())
    ex=result['outcomes']
    expected={'resolved_minus':0,'resolved_plus':-24,'coherent':-12}
    for name,target in expected.items():
        x=ex[name]['exact_initial_moments']['sine_electric_circulation']
        assert x['impulse_initial_slope_numerator']==target*x['denominator']
    assert result['electric_loop']==[0,1,-1,0,0,0,0,0,0,-1,1,0]
    assert result['H_Gamma_commutator_max_abs']>0
    print(json.dumps(result,indent=2))
    print('Verification complete: exact finite supplied-model identities; numerical projected dynamics only. Strong-electric error bounds are proved in the note, not certified by this numerical run.')
