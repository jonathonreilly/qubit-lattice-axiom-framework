#!/usr/bin/env python3
"""Author checks: exact Gauss coordinates and fixed-volume spectral comparators.

No numerical sequence proves the form-limit theorem or a thermodynamic phase.
"""
from itertools import product, combinations
import json
import numpy as np
import sympy as sy
from sympy.matrices.normalforms import smith_normal_form
from scipy import sparse as sp
from scipy.sparse.linalg import eigsh
from scipy.linalg import eigh_tridiagonal
from scipy.special import hyp1f1, erf, erfc
from scipy.optimize import brentq

AUDIT_TIMEOUT_SEC = 90

passed = 0


def check(condition, label):
    global passed
    assert bool(condition), label
    passed += 1


def close(left, right, label, tol=2e-10):
    check(np.allclose(left, right, atol=tol, rtol=tol), label)


def box_complex(shape, periodic=False):
    vertices = list(product(*(range(n) for n in shape)))
    vi = {v: k for k, v in enumerate(vertices)}
    edges = []
    edge_id = {}
    def next_vertex(v, axis):
        w = list(v)
        w[axis] = (w[axis] + 1) % shape[axis]
        return tuple(w)
    for v in vertices:
        for axis in range(len(shape)):
            if periodic or v[axis] + 1 < shape[axis]:
                edge_id[v, axis] = len(edges)
                edges.append((vi[v], vi[next_vertex(v, axis)]))
    D = np.zeros((len(vertices), len(edges)), dtype=int)
    for j, (u, v) in enumerate(edges):
        D[u, j], D[v, j] = 1, -1
    faces = []
    for v in vertices:
        for i, j in combinations(range(len(shape)), 2):
            if periodic or (v[i]+1 < shape[i] and v[j]+1 < shape[j]):
                col = np.zeros(len(edges), dtype=int)
                for key, sign in [((v, i), 1), ((next_vertex(v, i), j), 1),
                                  ((next_vertex(v, j), i), -1), ((v, j), -1)]:
                    col[edge_id[key]] += sign
                faces.append(col)
    return D, np.array(faces).T, edges


def tree_coordinates(D, edges):
    V, E = D.shape
    parent = {0: None}
    tree = []
    queue = [0]
    for u in queue:
        for edge, (a, b) in enumerate(edges):
            v = b if a == u else a if b == u else None
            if v is not None and v not in parent:
                parent[v] = (u, edge)
                tree.append(edge)
                queue.append(v)
    R = np.zeros((E, V), dtype=int)
    for x in range(1, V):
        v = x
        while v:
            u, edge = parent[v]
            R[edge, x] = D[v, edge]
            v = u
    chords = [j for j in range(E) if j not in tree]
    C = np.eye(E, dtype=int)[:, chords] - R @ D[:, chords]
    return R, C, chords


def geometry_checks():
    rng = np.random.default_rng(140913)
    records = []
    for shape in [(2, 2), (2, 2, 2), (3, 2, 2), (3, 3, 2)]:
        D, F, edges = box_complex(shape)
        R, C, chords = tree_coordinates(D, edges)
        V, E = D.shape
        c = E-V+1
        Z = F[chords, :]
        target = np.eye(V, dtype=int)
        target[0, :] -= 1
        close(D @ R, target, 'integer rooted right inverse')
        close(D @ C, 0, 'exact divergence-free cycle basis')
        close(C[chords, :], np.eye(c), 'chord identity')
        close(D @ F, 0, 'boundary of boundary')
        close(C @ Z, F, 'integer plaquette coordinates')
        smith = smith_normal_form(sy.Matrix(Z), domain=sy.ZZ)
        check([abs(smith[j, j]) for j in range(c)] == [1]*c,
              'primitive integer generation, not just real rank')
        we = np.linspace(.7, 1.9, E)
        wb = np.linspace(.8, 1.7, F.shape[1])
        K = C.T @ (we[:, None]*C)
        A = (Z*wb) @ Z.T
        av, au = np.linalg.eigh(A)
        root_A = (au*np.sqrt(av)) @ au.T
        spectrum = np.linalg.eigvalsh(root_A @ K @ root_A)
        curl = (np.sqrt(we)[:, None]*F)*np.sqrt(wb)
        direct = np.linalg.eigvalsh(curl @ curl.T)
        close(spectrum, direct[-c:], 'weighted oscillator versus direct curl spectrum')
        for repeat in range(6):
            rho = rng.integers(-2, 3, V)
            rho[0] -= rho.sum()
            n = rng.integers(-3, 4, c)
            field = R @ rho + C @ n
            close(D @ field, rho, 'affine integer physical field')
            close(field[chords], n, 'coordinate inverse')
            longitudinal = (D.T @ (np.linalg.pinv((D/we) @ D.T) @ rho))/we
            transverse = field-longitudinal
            close(D @ transverse, 0, 'weighted transverse divergence')
            close(C.T @ (we*longitudinal), 0, 'weighted orthogonality')
            close(np.dot(field*we, field), np.dot(transverse*we, transverse)
                  + np.dot(rho, np.linalg.pinv((D/we) @ D.T) @ rho),
                  'exact Coulomb energy splitting')
            for edge in range(E):
                delta = np.eye(E, dtype=int)[:, edge]
                close(delta-R @ D[:, edge], C @ delta[chords],
                      'tree/chord charged hop displacement')
        records.append(dict(shape=shape, cycle_rank=c, primitive=True))
    D, F, _ = box_complex((2, 2, 2))
    vals = np.linalg.eigvalsh(F @ F.T)
    close(vals[-5:], [4, 4, 4, 6, 6], 'open cube exact squared frequencies')
    close(.5*np.sqrt(vals[-5:]).sum(), 3+np.sqrt(6), 'open cube zero-point energy')
    D, F, _ = box_complex((3, 3, 3), periodic=True)
    check(np.linalg.matrix_rank(F) == D.shape[1]-D.shape[0]+1-3,
          'periodic three harmonic directions remain')
    D, _, edges = box_complex((2, 2))
    rho = np.array([1, -1, 0, 0])
    EL = D.T @ np.linalg.pinv(D @ D.T) @ rho
    check(np.max(np.abs(EL-np.round(EL))) > .1,
          'longitudinal field is not an independent integer link assignment')
    print('GEOMETRY', json.dumps(records))


states = [sum(1 << i for i in pair) for pair in combinations(range(4), 2)]
fi = {state: j for j, state in enumerate(states)}
eta = np.array([0, 1, 0, 1])
ons = np.array([.17, -.31, .26, -.12])
hops = [1., .7, 1.2, .9]
E0 = []
for state in states:
    rho = np.array([(state >> j) & 1 for j in range(4)])-eta
    E0.append(np.array([rho[0], rho[0]+rho[1], sum(rho[:3]), 0]))


def move(state, x, y):
    if not (state >> y & 1) or state >> x & 1:
        return None
    sign = (-1)**((state & ((1 << y)-1)).bit_count())
    lower = state ^ (1 << y)
    sign *= (-1)**((lower & ((1 << x)-1)).bit_count())
    return lower | (1 << x), sign


def free_matrix():
    H = np.diag([sum(ons[j] for j in range(4) if state >> j & 1) for state in states])
    for f, state in enumerate(states):
        for edge, hop in enumerate(hops):
            result = move(state, edge, (edge+1) % 4)
            if result is not None:
                target, sign = result
                H[fi[target], f] += hop*sign
                H[f, fi[target]] += hop*sign
    return H


def reduced_matrix(g, S):
    free = free_matrix()
    basis = [(f, n) for f in range(6)
             for n in range(-S-int(min(E0[f])), S-int(max(E0[f]))+1)]
    ix = {label: j for j, label in enumerate(basis)}
    H = sp.lil_matrix((len(basis), len(basis)))
    for col, (f, n) in enumerate(basis):
        H[col, col] = (.5*g*g*np.dot(E0[f]+n, E0[f]+n)
                         + 1/g**2 + free[f, f])
        if (f, n+1) in ix:
            row = ix[f, n+1]
            H[row, col] += -1/(2*g*g)
            H[col, row] += -1/(2*g*g)
        for edge, hop in enumerate(hops):
            result = move(states[f], edge, (edge+1) % 4)
            if result is not None:
                target, sign = result
                label = (fi[target], n+(edge == 3))
                if label in ix:
                    row = ix[label]
                    H[row, col] += hop*sign
                    H[col, row] += hop*sign
    return H.tocsr(), basis


def direct_matrix(g, S):
    # Independent full four-link enumeration and direct CAR matrices.
    D = np.eye(4, dtype=int)-np.roll(np.eye(4, dtype=int), 1, axis=0)
    annihilators = []
    for j in range(4):
        op = np.zeros((16, 16))
        for f in range(16):
            if f >> j & 1:
                op[f ^ (1 << j), f] = (-1)**sum((f >> k) & 1 for k in range(j))
        annihilators.append(op)
    basis = []
    for f, state in enumerate(states):
        rho = np.array([(state >> j) & 1 for j in range(4)])-eta
        for field in product(range(-S, S+1), repeat=4):
            if np.array_equal(D @ field, rho):
                basis.append((f, field))
    ix = {label: j for j, label in enumerate(basis)}
    H = np.zeros((len(basis), len(basis)))
    for col, (f, field) in enumerate(basis):
        H[col, col] = .5*g*g*np.dot(field, field)+1/g**2
        H[col, col] += sum(ons[j] for j in range(4) if states[f] >> j & 1)
        raised = tuple(e+1 for e in field)
        if (f, raised) in ix:
            row = ix[f, raised]
            H[row, col] += -1/(2*g*g)
            H[col, row] += -1/(2*g*g)
        for edge, hop in enumerate(hops):
            op = annihilators[edge].T @ annihilators[(edge+1) % 4]
            field2 = list(field)
            field2[edge] += 1
            for ff, state2 in enumerate(states):
                value = hop*op[state2, states[f]]
                if value and (ff, tuple(field2)) in ix:
                    row = ix[ff, tuple(field2)]
                    H[row, col] += value
                    H[col, row] += value
    return H, basis


def box_energy(s):
    fun = lambda E: hyp1f1((1-E)/4, .5, 2*s*s)
    for hi in np.linspace(1.00001, 1+np.pi*np.pi/(2*s*s)+2*s*s, 200):
        if fun(hi) < 0:
            return brentq(fun, 1., hi, xtol=1e-13)
    raise AssertionError('first box eigenvalue bracket')


def pure(g, S, step=1):
    n = np.arange(-S, S+1)
    off = -np.ones(len(n)-step)/(2*g*g)
    H = sp.diags(2*g*g*n*n+1/(g*g), format='csr')
    H += sp.diags([off, off], [-step, step], format='csr')
    return np.sort(eigsh(H, k=4, which='SA', return_eigenvectors=False, tol=1e-11))


def spectral_checks():
    g, S = .1, 8
    n = np.arange(-S, S+1)
    kinetic = np.diag(np.full(len(n), 1/g**2))
    kinetic += np.diag(np.full(len(n)-1, -1/(2*g*g)), 1)
    kinetic += np.diag(np.full(len(n)-1, -1/(2*g*g)), -1)
    v = np.random.default_rng(148).normal(size=len(n))
    close(v @ kinetic @ v, np.sum(np.diff(np.r_[0., v, 0.])**2)/(2*g*g),
          'compressed magnetic form retains two zero-extension boundary terms')
    dirichlet = kinetic + np.diag(2*g*g*n*n)
    reflecting = dirichlet.copy()
    reflecting[0, 0] -= 1/(2*g*g)
    reflecting[-1, -1] -= 1/(2*g*g)
    check(np.linalg.eigvalsh(dirichlet)[0]-np.linalg.eigvalsh(reflecting)[0] > .2,
          'dropping the magnetic identity at endpoints changes the vacuum')
    for S in [1, 2]:
        reduced, rb = reduced_matrix(.37, S)
        direct, db = direct_matrix(.37, S)
        lookup = {label: j for j, label in enumerate(db)}
        check(all((f, tuple(E0[f]+n)) in lookup for f, n in rb),
              'every reduced label lies in the direct physical cutoff domain')
        order = [lookup[f, tuple(E0[f]+n)] for f, n in rb]
        check(len(db) == len(rb), 'direct Gauss enumeration is onto affine domain')
        close(reduced.toarray(), direct[np.ix_(order, order)],
              'full direct CAR/link Hamiltonian equals reduced charged Hamiltonian')
        check(len(rb) < 6*(2*S+1), 'charged finite cutoff is not a product domain')
    free = np.linalg.eigvalsh(free_matrix())
    records = []
    for s in [1., 2., 3.]:
        reference = box_energy(s)
        # Independent continuum central difference (Dirichlet), no hypergeometric coefficients.
        count = 2200
        h = 2*s/(count+1)
        x = -s+h*np.arange(1, count+1)
        fd = eigh_tridiagonal(1/h**2+2*x*x, -np.ones(count-1)/(2*h*h),
                              select='i', select_range=(0, 0))[0][0]
        close(fd, reference, 'independent continuum box reference', tol=5e-6)
        check(reference > 1, 'finite interval vacuum differs from full Gaussian')
        errors = []
        for S in [20, 40, 80]:
            g = s/(S+1)
            gauge = pure(g, S)[0]
            H, _ = reduced_matrix(g, S)
            charged = np.sort(eigsh(H, k=4, which='SA', return_eigenvectors=False, tol=1e-11))
            errors.append(abs(charged[0]-(reference+free[0])))
            records.append(dict(s=s, S=S, gauge=float(gauge), charged=float(charged[0]),
                                box_ground=reference, charged_target=float(reference+free[0])))
        check(errors[2] < errors[1] < errors[0], 'sampled charged fixed-boundary convergence')
        check(errors[-1] < .008, 'sampled charged boundary target accuracy')
        if s >= 2:
            lower = 2*erfc(np.sqrt(2)*s)
            upper = np.sqrt(2/np.pi)/erf(np.sqrt(2))*np.exp(-2*(s-1)**2)
            check(lower <= reference-1 <= upper, 'analytic Gaussian energy-tail bounds')
    targets = np.sort(np.array([1+2*n+v for n in range(4) for v in free]))[:4]
    full = []
    for g in [.2, .1, .05]:
        S = int(np.ceil(np.log(1/g)/g))
        H, _ = reduced_matrix(g, S)
        values = np.sort(eigsh(H, k=4, which='SA', return_eigenvectors=False, tol=1e-11))
        full.append(dict(g=g, S=S, eigenvalues=values.tolist(), error=float(max(abs(values-targets)))))
    check(full[-1]['error'] < .005, 'first four additive oscillator/free-matter levels')
    check(full[-1]['error'] < full[0]['error'], 'sampled growing-cutoff spectral improvement')
    doubles = []
    for g in [.2, .1, .05]:
        values = pure(g, int(np.ceil((3+np.log(1/g))/g)), step=2)
        doubles.append(values.tolist())
    close(doubles[-1][:2], [2, 2], 'nonprimitive doubled ground cluster', tol=.002)
    check(doubles[-1][1]-doubles[-1][0] < 1e-7, 'two flux parity copies persist')
    # Symbolic ODE recurrence independently substituted through x^10.
    x, energy = sy.symbols('x energy')
    coeff = sy.Integer(1)
    series = coeff
    for n in range(6):
        coeff = coeff*(4*n-(energy-1))/((n+1)*(2*n+1))
        series += coeff*x**(2*n+2)
    residual = sy.expand(sy.diff(series, x, 2)-4*x*sy.diff(series, x)+2*(energy-1)*series)
    for degree in range(0, 12, 2):
        check(sy.factor(residual.coeff(x, degree)) == 0, 'box ODE exact recurrence')
    print('SPECTRAL', json.dumps(dict(free=free.tolist(), fixed_boundary=records,
                                   full_space=full, additive_targets=targets.tolist(),
                                   doubled_flux_copies=doubles)))
    for label, message in [
        ('per_element', 'weighted electric projection and integer link-hop increments checked; no selected coupling'),
        ('per_site', 'direct CAR matrices and exact charge neutrality checked in the four-site fixture'),
        ('per_mode', 'one-plaquette oscillator spectra, finite-boundary vacuum and doubled parity copies checked'),
        ('per_block', 'open cubical integer homology and exact charged Hamiltonian equivalence checked'),
        ('lattice_wide', 'fixed finite contractible graph proof supplied; periodic harmonic directions exhibited; growing-volume phase unproved')]:
        print(label+': '+message)



if __name__ == '__main__':
    geometry_checks()
    spectral_checks()
    print(f'TOTAL: PASS={passed} FAIL=0')
