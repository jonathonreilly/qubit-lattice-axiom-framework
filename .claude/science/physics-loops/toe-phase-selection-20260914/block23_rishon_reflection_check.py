#!/usr/bin/env python3
"""Finite falsifiers for the endpoint reflection sector-bound proposal.

Exact finite cochains, endpoint shifts, projection predicates and dissemination
geometry. These checks do not execute the full many-body partition function,
prove the infinite-volume phase, or constitute independent review.
"""
import itertools as it
import json
import math
from collections import Counter

import numpy as np
import sympy as sp


def shift(v, axis, sign, L):
    out = list(v)
    out[axis] = (out[axis] + sign) % L
    return tuple(out)


def vertices(L):
    return list(it.product(range(L), repeat=3))


def principal(a):
    return (int(a) + 1) % 3 - 1


def curl_from_clock(a, L):
    b = {}
    for v in vertices(L):
        for i, j in it.combinations(range(3), 2):
            value = a[v, i] + a[shift(v, i, 1, L), j]
            value -= a[shift(v, j, 1, L), i] + a[v, j]
            b[v, i, j] = principal(value)
    return b


def dual_field(b, L):
    E = {}
    # The independent divergence/curl identity below challenges this sign
    # and the one-cell dual-base shift.
    for (v, i, j), value in b.items():
        k = next(x for x in range(3) if x not in (i, j))
        eps = -1 if (i, j, k) == (0, 2, 1) else 1
        E[shift(v, k, -1, L), k] = eps * value
    return E


def divergence(E, L):
    return {v: sum(E[v, i] - E[shift(v, i, -1, L), i] for i in range(3))
            for v in vertices(L)}


def d2(b, L):
    result = {}
    for v in vertices(L):
        result[v] = (b[shift(v, 0, 1, L), 1, 2] - b[v, 1, 2]
                     - b[shift(v, 1, 1, L), 0, 2] + b[v, 0, 2]
                     + b[shift(v, 2, 1, L), 0, 1] - b[v, 0, 1])
    return result


def endpoint_state(E, L):
    n = {}
    for (v, i), value in E.items():
        n[v, i, 1] = value + 1
        n[shift(v, i, 1, L), i, -1] = 1 - value
    return n


def physical_predicate(n, L):
    vs = vertices(L)
    for v in vs:
        if sum(n[v, i, s] for i in range(3) for s in (-1, 1)) % 3:
            return False
        for i in range(3):
            if n[v, i, 1] + n[shift(v, i, 1, L), i, -1] != 2:
                return False
    for i in range(3):
        if sum(n[v, i, 1] - 1 for v in vs if v[i] == 0) % 3:
            return False
    return True


def reflect_vertex(v, normal, L):
    out = list(v)
    out[normal] = L - 1 - out[normal]
    return tuple(out)


def reflected_hole(n, normal, L):
    return {(v, i, s): 2 - n[reflect_vertex(v, normal, L), i,
                               -s if i == normal else s]
            for v in vertices(L) for i in range(3) for s in (-1, 1)}


def half_label(n, normal, L):
    left = {v for v in vertices(L) if v[normal] < L // 2}
    for v in left:
        if sum(n[v, i, s] for i in range(3) for s in (-1, 1)) % 3:
            return None
        for i in range(3):
            w = shift(v, i, 1, L)
            if w in left and n[v, i, 1] + n[w, i, -1] != 2:
                return None
    cross = sorted((v, i, s) for v in left for i in range(3) for s in (-1, 1)
                   if shift(v, i, s, L) not in left)
    normal_flux = sum(n[v, normal, 1] - 1 for v in left
                      if v[normal] == L // 2 - 1) % 3
    if normal_flux:
        return None
    tangential = tuple(sum(n[v, j, 1] - 1 for v in left if v[j] == 0) % 3
                       for j in range(3) if j != normal)
    return tuple(n[key] for key in cross), tangential


def cone_projection_predicate(n, normal, L):
    a = half_label(n, normal, L)
    b = half_label(reflected_hole(n, normal, L), normal, L)
    return a is not None and a == b


def field_projection_checks():
    rng = np.random.default_rng(2026091505)
    L = 4
    vs = vertices(L)
    rows = []
    nonzero_partial_fluxes = 0
    for trial in range(24):
        a = {(v, i): int(rng.integers(3)) for v in vs for i in range(3)}
        b = curl_from_clock(a, L)
        E = dual_field(b, L)
        assert divergence(E, L) == d2(b, L)
        assert all(q % 3 == 0 for q in divergence(E, L).values())
        n = endpoint_state(E, L)
        assert physical_predicate(n, L)
        for normal in range(3):
            assert cone_projection_predicate(n, normal, L)
            label = half_label(n, normal, L)
            nonzero_partial_fluxes += any(label[1])
        for axis in range(3):
            # Add one nontrivial mod-three winding cycle, retaining mod-three
            # Gauss after taking the principal representative again.
            changed = dict(E)
            for v in vs:
                if all(v[j] == 0 for j in range(3) if j != axis):
                    changed[v, axis] = principal(changed[v, axis] + 1)
            nn = endpoint_state(changed, L)
            assert all(q % 3 == 0 for q in divergence(changed, L).values())
            assert not physical_predicate(nn, L)
            for normal in range(3):
                assert not cone_projection_predicate(nn, normal, L)
        # A deformation of endpoint occupation preserves the local mod-three
        # register but violates hard link matching. It must not pass the cone.
        bad = dict(n)
        v = (1, 0, 0)
        for i in range(3):
            bad[v, i, 1] = (bad[v, i, 1] + 1) % 3
        assert not physical_predicate(bad, L)
        for normal in range(3):
            assert not cone_projection_predicate(bad, normal, L)
        rows.append({'trial': trial,
                     'charge_mass': sum(abs(q // 3) for q in divergence(E, L).values())})
    assert nonzero_partial_fluxes > 0
    isolated_cross_controls = 0
    for normal in range(3):
        tangent = (normal + 1) % 3
        E = {(v,i):0 for v in vs for i in range(3)}
        base = [0,0,0]; base[normal]=1; base[tangent]=1
        v0=tuple(base)
        v1=shift(v0,normal,1,L)
        v3=shift(v0,tangent,1,L)
        E[v0,normal]=1;E[v1,tangent]=1
        E[v3,normal]=-1;E[v0,tangent]=-1
        n=endpoint_state(E,L)
        assert physical_predicate(n,L)
        # Particle-hole on the right half preserves every internal link
        # constraint and local mod-three register. This fixture's partial
        # tangential periods vanish. Only cross-link matching is broken.
        broken={key:(2-value if key[0][normal]>=L//2 else value)
                for key,value in n.items()}
        a=half_label(broken,normal,L)
        b=half_label(reflected_hole(broken,normal,L),normal,L)
        assert a is not None and b is not None
        assert a[1] == b[1] == (0,0)
        assert a[0] != b[0]
        assert not physical_predicate(broken,L)
        assert not cone_projection_predicate(broken,normal,L)
        isolated_cross_controls += 1
    return {'L': L, 'actual_clock_fields': len(rows),
            'nonzero_winding_controls': 3 * len(rows),
            'broken_endpoint_controls': len(rows), 'reflection_normals': 3,
            'nonzero_tangential_half_flux_instances': nonzero_partial_fluxes,
            'isolated_cross_link_matching_controls':isolated_cross_controls,
            'scope': 'exact diagonal projection equivalence on the listed finite fixtures',
            'field_rows': rows}


def port(v, w, L):
    for i in range(3):
        for s in (-1, 1):
            if shift(v, i, s, L) == w:
                return v, i, s
    raise AssertionError('non-neighbor corner')


def ring_word(cycle, L):
    ans = {}
    for j, v in enumerate(cycle):
        ans[port(v, cycle[(j + 1) % 4], L)] = 1
        ans[port(v, cycle[(j - 1) % 4], L)] = -1
    assert len(ans) == 8
    return ans


def theta_word(word, normal, L):
    return {(reflect_vertex(v, normal, L), i, -s if i == normal else s): -power
            for (v, i, s), power in word.items()}


def apply_word(n, word):
    ans = dict(n)
    for key, power in word.items():
        ans[key] += power
        if not 0 <= ans[key] <= 2:
            return None
    return ans


def ring_and_reflection_checks():
    L = 4
    cases = []
    for normal in range(3):
        for tangent in range(3):
            if tangent == normal:
                continue
            base = [0, 0, 0]; base[normal] = L // 2 - 1
            v0 = tuple(base)
            v1 = shift(v0, normal, 1, L)
            v2 = shift(v1, tangent, 1, L)
            v3 = shift(v0, tangent, 1, L)
            cycle = (v0, v1, v2, v3)
            word = ring_word(cycle, L)
            left = {key: power for key, power in word.items()
                    if key[0][normal] < L // 2}
            right = {key: power for key, power in word.items() if key not in left}
            assert len(left) == len(right) == 4
            assert theta_word(left, normal, L) == right
            assert theta_word(theta_word(left, normal, L), normal, L) == left
            edges = []
            shifts = []
            for j, v in enumerate(cycle):
                w = cycle[(j + 1) % 4]
                lo, hi = sorted((v, w))
                edges.append((lo, hi))
                shifts.append(1 if (lo, hi) == (v, w) else -1)
            checked = 0
            for es in it.product((-1, 0, 1), repeat=4):
                n = {}
                for (v, w), e in zip(edges, es):
                    n[port(v, w, L)] = e + 1
                    n[port(w, v, L)] = 1 - e
                for power in (1, -1, 2, -2):
                    target = tuple(e + power*s for e, s in zip(es, shifts))
                    expected = all(-1 <= e <= 1 for e in target)
                    got = apply_word(n, {key: power*v for key, v in word.items()})
                    assert (got is not None) == expected
                    if expected:
                        for (v, w), e in zip(edges, target):
                            assert got[port(v, w, L)] == e + 1
                            assert got[port(w, v, L)] == 1 - e
                    checked += 1
            cases.append({'normal': normal, 'tangent': tangent,
                          'physical_endpoint_transition_checks': checked})
    # A one-link exact matrix compression separately checks unit amplitudes.
    R = sp.Matrix([[0, 0, 0], [1, 0, 0], [0, 1, 0]])
    embedding = sp.zeros(9, 3)
    for e in (-1, 0, 1):
        embedding[3*(e+1)+(1-e), e+1] = 1
    assert embedding.T * sp.kronecker_product(R, R.T) * embedding == R
    assert embedding.T * embedding == sp.eye(3)
    # The center-two constraint has an exact cone decomposition. Moving its
    # center to one fails reflection positivity on an explicit diagonal test.
    f = [1, -1, 1]
    correct = sum(f[a]*f[2-b] for a in range(3) for b in range(3) if a+b == 2)
    incorrect = sum(f[a]*f[2-b] for a in range(3) for b in range(3) if a+b == 1)
    assert correct == 3 and incorrect == -2
    return {'crossing_ring_cases': cases, 'one_link_isometry': 'exact symbolic equality',
            'correct_link_projector_reflection_form': correct,
            'wrong_link_sum_one_reflection_form': incorrect}


def disseminate(labels, axis, ell, L):
    # Keep [ell-L/2,ell-1] modulo L and reflect in ell-1/2.
    keep = {(ell - L//2 + j) % L for j in range(L//2)}
    out = {}
    for v in vertices(L):
        if v[axis] in keep:
            out[v] = labels[v]
        else:
            w = list(v); w[axis] = (2*ell-1-v[axis]) % L
            out[v] = labels[tuple(w)]
    return out


def dissemination_and_checkerboards():
    rng = np.random.default_rng(91723)
    cases = []
    for L in (4, 8):
        vs = vertices(L)
        for trial in range(8):
            labels = {v: int(rng.integers(-2, 3)) for v in vs}
            initial = labels[(0, 0, 0)]
            lengths = [1, 1, 1]
            steps = 0
            for axis in range(3):
                ell = 1
                while ell < L:
                    old = dict(labels)
                    labels = disseminate(old, axis, ell, L)
                    # The opposite dissemination supplies the other half.
                    other = disseminate(old, axis, ell + L//2, L)
                    assert Counter(labels.values()) + Counter(other.values()) == Counter({k: 2*v for k,v in Counter(old.values()).items()})
                    lengths[axis] = 2 * ell
                    assert all(labels[v] == initial for v in it.product(*(range(x) for x in lengths)))
                    ell *= 2; steps += 1
            assert set(labels.values()) == {initial}
            cases.append({'L': L, 'trial': trial, 'doublings': steps})
        for k in (-2, -1, 0, 1, 2):
            E = {}
            for v in vs:
                parity = (-1) ** sum(v)
                for axis in range(3):
                    if k == 0:
                        val = 0
                    elif abs(k) == 2:
                        val = (k//2) * parity
                    else:
                        selected = int(v[axis] % 2 == 0)
                        val = -k * parity * (selected - 1)
                    E[v, axis] = val
            q = divergence(E, L)
            assert q == {v: 3*k*((-1)**sum(v)) for v in vs}
            n = endpoint_state(E, L)
            assert physical_predicate(n, L)
            assert all(cone_projection_predicate(n, normal, L) for normal in range(3))
    return {'doubling_cases': cases, 'physical_checkerboard_fixtures': 10,
            'scope': 'geometry and feasibility; no many-body partition sum executed'}


def local_spectral_constant():
    h = sp.symbols('h', real=True)
    z = sp.symbols('z')
    tri = sp.Matrix([[0, 1, h], [1, 0, 1], [h, 1, 0]])
    assert sp.expand(tri.charpoly(z).as_expr() - (z+h)*(z*z-h*z-2)) == 0
    states = list(it.product((-1, 0, 1), repeat=4))
    idx = {e:i for i,e in enumerate(states)}
    B = np.zeros((81,81), dtype=float)
    for col,e in enumerate(states):
        target = tuple(e[i]+(1,1,-1,-1)[i] for i in range(4))
        if target in idx:
            B[idx[target],col] = 1
    rows = []
    for h0 in (0, 1/7, 0.5, 1):
        matrix = B+B.T+h0*(B@B+(B.T@B.T))
        exact = (h0+math.sqrt(h0*h0+8))/2
        actual = max(abs(np.linalg.eigvalsh(matrix)))
        assert abs(actual-exact) < 1e-12
        rows.append({'h':h0,'rho':actual})
    return {'symbolic_characteristic_polynomial':'(z+h)(z^2-hz-2)',
            'full_four_link_matrices':rows}


def rank_mod_three(matrix):
    a = np.asarray(matrix, dtype=np.int64).copy() % 3
    row = 0
    for col in range(a.shape[1]):
        candidates = np.flatnonzero(a[row:, col])
        if not len(candidates):
            continue
        pivot = row + int(candidates[0])
        a[[row, pivot]] = a[[pivot, row]]
        a[row] = (a[row] * (1 if a[row, col] == 1 else 2)) % 3
        for j in range(a.shape[0]):
            if j != row and a[j, col]:
                a[j] = (a[j] - a[j, col]*a[row]) % 3
        row += 1
        if row == a.shape[0]:
            break
    return row


def cohomology_and_wrap_checks():
    L = 4
    vs = vertices(L)
    edges = [(v,i) for v in vs for i in range(3)]
    faces = [(v,i,j) for v in vs for i,j in it.combinations(range(3),2)]
    empty_a = {e:0 for e in edges}
    empty_b = {f:0 for f in faces}
    F = np.zeros((len(faces),len(edges)),dtype=np.int64)
    for j,e in enumerate(edges):
        a = dict(empty_a); a[e]=1
        b = curl_from_clock(a,L)
        F[:,j] = [b[f] for f in faces]
    D = np.zeros((len(vs),len(faces)),dtype=np.int64)
    periods = np.zeros((3,len(faces)),dtype=np.int64)
    for j,f in enumerate(faces):
        b = dict(empty_b); b[f]=1
        db = d2(b,L)
        D[:,j] = [db[v] for v in vs]
        E = dual_field(b,L)
        for i in range(3):
            periods[i,j] = sum(E[v,i] for v in vs if v[i]==0)
    C = np.vstack((D,periods))
    assert not np.any((C @ F) % 3)
    ranks = [rank_mod_three(x) for x in (F,D,C)]
    assert ranks == [126,63,66]
    assert ranks[0]+ranks[2]==len(faces)
    local_counts = Counter((sum(ns)-6)//3 for ns in it.product(range(3),repeat=6)
                           if sum(ns)%3==0)
    assert local_counts == {-2:1,-1:50,0:141,1:50,2:1}
    assert sum(local_counts.values())==243

    rng = np.random.default_rng(231944)
    inputs = [{e:int(rng.integers(3)) for e in edges} for _ in range(12)]
    hist = Counter()
    for trial,a in enumerate(inputs):
        chosen = edges[trial*7:trial*7+12]
        for e in chosen:
            star = F[:,edges.index(e)]
            assert np.count_nonzero(star)==4
            v,i = e
            other = [j for j in range(3) if j!=i]
            incident = set()
            for bits in it.product((0,-1),repeat=2):
                z=v
                for j,bit in zip(other,bits):
                    z=shift(z,j,bit,L)
                incident.add(z)
            assert len(incident)==4
            for sigma in (-1,1):
                b = curl_from_clock(a,L)
                aa=dict(a);aa[e]=(aa[e]+sigma)%3
                bb=curl_from_clock(aa,L)
                before=np.array([b[f] for f in faces])
                after=np.array([bb[f] for f in faces])
                numerator=after-before-sigma*star
                assert not np.any(numerator%3)
                mismatch=numerator//3
                norm=int(mismatch@mismatch)
                hist[norm]+=1
                qb,qa=d2(b,L),d2(bb,L)
                same=qb==qa
                assert same == (norm in (0,4))
                if norm==0:
                    assert np.array_equal(after-before,sigma*star)
                elif norm==4:
                    assert np.array_equal(after-before,-2*sigma*star)
                else:
                    assert any(qb[c] or qa[c] for c in incident)
                assert all(qb[c]==qa[c] for c in vs if c not in incident)
    # Force both clean neutral transitions, including the complete wrap.
    for e in edges[:3]:
        star=F[:,edges.index(e)]
        a=dict(empty_a);a[e]=1
        b=curl_from_clock(a,L)
        a[e]=2
        bb=curl_from_clock(a,L)
        before=np.array([b[f] for f in faces]);after=np.array([bb[f] for f in faces])
        assert not np.any(D@before) and not np.any(D@after)
        assert np.array_equal(after-before,-2*star)
    return {'L':L,'rank_curl_mod3':ranks[0],'rank_divergence_mod3':ranks[1],
            'rank_closure_plus_three_periods_mod3':ranks[2],
            'physical_field_dimension_mod3':126,
            'local_vertex_charge_multiplicities':dict(sorted(local_counts.items())),
            'original_clock_mismatch_histogram':dict(sorted(hist.items())),
            'forced_neutral_full_wraps':3,
            'scope':'finite cohomology equality and original-clock transition identities'}


def finite_reflection_functional():
    R=np.array([[0,0,0],[1,0,0],[0,1,0]],dtype=complex)
    d=np.diag([1,0,1]).astype(complex)/4
    I=np.eye(3)
    P=np.diag([int(i==j) for i in range(3) for j in range(3)])
    rng=np.random.default_rng(23519)
    rows=[]
    for beta in (0.1,0.7,2):
        for h in (0,0.3,1):
            H=np.kron(d,I)+np.kron(I,d)-np.kron(R,R)-np.kron(R.T,R.T)
            H-=h*(np.kron(R@R,R@R)+np.kron(R.T@R.T,R.T@R.T))
            assert np.max(np.abs(H@P-P@H))<1e-14
            es,us=np.linalg.eigh(H)
            density=P@((us*np.exp(-beta*es))@us.conj().T)
            def inner(F,G):
                return np.trace(density@np.kron(F,G.conj()))
            minimum=math.inf
            for _ in range(12):
                F=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3))
                G=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3))
                ff,gg,fg=inner(F,F),inner(G,G),inner(F,G)
                assert abs(ff.imag)<1e-10 and abs(gg.imag)<1e-10
                assert ff.real>=-1e-10 and gg.real>=-1e-10
                assert abs(fg)**2<=ff.real*gg.real+1e-9
                minimum=min(minimum,ff.real,gg.real)
            rows.append({'beta':beta,'h':h,'minimum_sampled_reflection_form':minimum})
    # Wrong sign of the crossing hopping yields a negative reflection form,
    # exposing the sign dependence independently of the cone predicate.
    wrong=np.kron(R,R)+np.kron(R.T,R.T)
    es,us=np.linalg.eigh(wrong)
    density=P@((us*np.exp(-es))@us.conj().T)
    F=np.zeros((3,3),dtype=complex);F[0,1]=1
    negative=float(np.trace(density@np.kron(F,F.conj())).real)
    assert negative < -0.1
    return {'projected_two_factor_models':rows,'wrong_hopping_sign_reflection_form':negative,
            'scope':'nine-dimensional finite matrix probes of the reflection functional and Cauchy-Schwarz'}


def run():
    print(json.dumps({'status':'finite author checks; reflection/sector proof and independent review separate',
                      'endpoint_rings':ring_and_reflection_checks(),
                      'physical_projection':field_projection_checks(),
                      'dissemination':dissemination_and_checkerboards(),
                      'local_norm':local_spectral_constant(),
                      'cohomology_and_original_clock':cohomology_and_wrap_checks(),
                      'finite_reflection_functional':finite_reflection_functional()}, indent=2))


if __name__ == '__main__':
    run()
