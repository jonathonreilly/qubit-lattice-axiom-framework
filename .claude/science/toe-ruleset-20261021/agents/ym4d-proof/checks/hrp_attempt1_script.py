#!/usr/bin/env python3
"""Exact finite Wilson RP diagnostics. Standard library only; no random tests.

Read hrp_criteria.md and HRP.md for scope. Integers store Boltzmann weights
after configuration-independent positive rescaling. Matrices / Z are exact.
The 3D all-group cases have decoupled tx sheets; an additional Z2 case has
strictly positive couplings on EVERY plaquette of the 4x2x2 torus.
"""
import hashlib
import itertools as it
import json
import os
from pathlib import Path
import resource
import signal
import sys
import threading
import time
from fractions import Fraction as Q

START = time.monotonic()
ROOT = Path(__file__).resolve().parent
LIMIT = 1_000_000_000
STOP = threading.Event()
RESULTS = []
FAILURES = []


def peak_rss():
    n = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return n if sys.platform == 'darwin' else n * 1024


def monitor():
    while not STOP.wait(0.1):
        if peak_rss() > LIMIT or time.monotonic() - START >= 1190:
            os.write(2, b'RESOURCE LIMIT: RSS > 1GB or elapsed >=1190s\n')
            os._exit(3)


def alarm(signum, frame):
    raise RuntimeError('1190 second wall limit reached')


def require(ok, label):
    if not ok:
        raise AssertionError(label)


def mm(a, b):
    bt = list(zip(*b))
    return [[sum(x*y for x, y in zip(row, col)) for col in bt] for row in a]


def scale_cols(a, d):
    return [[v*d[j] for j, v in enumerate(row)] for row in a]


def psd_certificate(matrix):
    """Exact symmetric Schur complements; failure supplies a negative direction.

    A zero pivot with nonzero residual row has a 2x2 principal minor -b^2.
    With prior positive pivots, congruence transfers the negative direction.
    """
    n = len(matrix)
    if any(matrix[i][j] != matrix[j][i] for i in range(n) for j in range(i)):
        return {'psd': False, 'hermitian': False}
    a = [[Q(v) for v in row] for row in matrix]
    pivots = []
    for k in range(n):
        d = a[k][k]
        if d < 0:
            return {'psd': False, 'hermitian': True, 'negative_pivot': str(d),
                    'pivot_index': k, 'prior_pivots': pivots}
        if d == 0:
            j = next((j for j in range(k+1, n) if a[k][j]), None)
            if j is not None:
                return {'psd': False, 'hermitian': True,
                        'negative_minor': str(-a[k][j]**2), 'indices': [k, j]}
            pivots.append('0')
            continue
        pivots.append(str(d))
        active = [i for i in range(k+1, n) if a[i][k]]
        for ii, i in enumerate(active):
            for j in active[ii:]:
                v = a[i][j] - a[i][k]*a[j][k]/d
                a[i][j] = a[j][i] = v
    return {'psd': True, 'hermitian': True, 'pivots': pivots,
            'rank': sum(p != '0' for p in pivots)}


def save_gram(name, matrix, z, basis, extra=None, expect_psd=True):
    require(z > 0, name + ' positive normalization')
    cert = psd_certificate(matrix)
    record = {'name': name, 'matrix_numerator': matrix, 'denominator': z,
              'basis': basis, 'certificate': cert, 'extra': extra or {}}
    target = ROOT / ('hrp_' + name + '.json')
    target.write_text(json.dumps(record, indent=2) + '\n')
    print(name, 'dimension=', len(matrix), 'Z=', z,
          'PSD=', cert['psd'], 'Hermitian=', cert['hermitian'], flush=True)
    RESULTS.append({'name': name, 'psd': cert['psd'],
                    'hermitian': cert['hermitian'], 'file': target.name})
    if expect_psd:
        require(cert['psd'], name + ' expected PSD')
    return cert


class Group:
    def __init__(self, name):
        self.name = name
        self.q = {'Z2': 2, 'Z3': 3, 'Q8': 8}[name]
        if name != 'Q8':
            self.mul = [[(a+b) % self.q for b in range(self.q)]
                        for a in range(self.q)]
        else:
            def mult(a, b):
                u, sa = divmod(a, 2)
                v, sb = divmod(b, 2)
                s = sa ^ sb
                if u == 0:
                    w = v
                elif v == 0:
                    w = u
                elif u == v:
                    w, s = 0, s ^ 1
                else:
                    w = 6-u-v
                    if (u, v) not in [(1, 2), (2, 3), (3, 1)]:
                        s ^= 1
                return 2*w+s
            self.mul = [[mult(a, b) for b in range(8)] for a in range(8)]
        self.inv = [next(b for b in range(self.q) if self.mul[a][b] == 0)
                    for a in range(self.q)]
        require(all(self.mul[self.mul[a][b]][c] == self.mul[a][self.mul[b][c]]
                    for a, b, c in it.product(range(self.q), repeat=3)),
                name + ' associativity')
        classes = []
        for a in range(self.q):
            c = sorted({self.mul[self.mul[h][a]][self.inv[h]] for h in range(self.q)})
            if c not in classes:
                classes.append(c)
        self.classes = classes
        self.cls = {a: i for i, c in enumerate(classes) for a in c}
        if name == 'Q8':
            mats = [[[1, 0], [0, 1]], [[1j, 0], [0, -1j]],
                    [[0, 1], [-1, 0]], [[0, 1j], [1j, 0]]]
            rep = [[[(-1 if s else 1)*v for v in row] for row in mats[u]]
                   for u in range(4) for s in range(2)]
            require(all(mm(rep[a], rep[b]) == rep[self.mul[a][b]]
                        for a, b in it.product(range(8), repeat=2)), 'Q8 representation')
            require(all(m[0][0]*m[1][1]-m[0][1]*m[1][0] == 1 for m in rep),
                    'Q8 determinant')
            require(all(mm(m, [list(map(complex.conjugate, col))
                               for col in zip(*[[complex(v) for v in r] for r in m])])
                        == [[1, 0], [0, 1]] for m in rep), 'Q8 unitarity')
            require([(m[0][0]+m[1][1]).real/2 for m in rep]
                    == [1, -1, 0, 0, 0, 0, 0, 0], 'Q8 trace')
        print('GROUP', name, 'order', self.q, 'classes', classes, flush=True)

    def product(self, seq):
        v = 0
        for x in seq:
            v = self.mul[v][x]
        return v

    def weights(self, k):
        # beta = k log 2 (Z2,Q8), beta = 2 k log 2 (Z3).
        if not k:
            return [1]*self.q
        m = abs(k)
        if self.name == 'Z2':
            w = [2**(2*m), 1]
        elif self.name == 'Z3':
            w = [2**(3*m), 1, 1]
        else:
            w = [2**(2*m), 1] + [2**m]*6
        if k < 0:
            top = max(w)
            w = [top//v for v in w]
        return w


def profiles(reflection, offset=0):
    if reflection == 'link':
        return [[1+offset, 2], [2, 1], [2, 2+offset], [2, 1]]
    return [[1+offset, 2], [2, 1], [2, 1], [1+offset, 2]]


def cylinder_transfer(group, ks):
    q, mul, inv = group.q, group.mul, group.inv
    w0, w1 = [group.weights(k) for k in ks]
    t = [[0]*q for _ in range(q)]
    # Spatial tree gauge in each length-2 slice: A=(1,g), B=(1,h).
    # Sum ALL temporal links c0,c1, including the fourth periodic step.
    for g, h, c0, c1 in it.product(range(q), repeat=4):
        p0 = mul[c0][inv[c1]]
        p1 = group.product((c1, h, inv[c0], inv[g]))
        t[g][h] += w0[p0]*w1[p1]
    return t


def torus_gram(group, reflection, prof):
    ts = [cylinder_transfer(group, ks) for ks in prof]
    nc = len(group.classes)
    degree = 2 if reflection == 'link' else 3
    basis = list(it.product(range(nc), repeat=degree))
    ids = {b: i for i, b in enumerate(basis)}
    gram = [[0]*len(basis) for _ in basis]
    for g0, g1, g2, g3 in it.product(range(group.q), repeat=4):
        c0, c1, c2, c3 = [group.cls[g] for g in (g0, g1, g2, g3)]
        if reflection == 'link':
            neg, pos = (c0, c3), (c1, c2)
        else:
            neg, pos = (c0, c3, c2), (c0, c1, c2)
        gram[ids[neg]][ids[pos]] += ts[0][g0][g1]*ts[1][g1][g2]*ts[2][g2][g3]*ts[3][g3][g0]
    return gram, sum(map(sum, gram)), basis


def lattice(extents):
    verts = list(it.product(*(range(n) for n in extents)))
    edges = [(v, d) for v in verts for d in range(len(extents))]
    edgeid = {e: i for i, e in enumerate(edges)}
    def step(v, d):
        w = list(v); w[d] = (w[d]+1) % extents[d]; return tuple(w)
    faces = []
    for v in verts:
        for mu, nu in it.combinations(range(len(extents)), 2):
            faces.append((v, mu, nu, [(edgeid[v, mu], 1),
                         (edgeid[step(v, mu), nu], 1),
                         (edgeid[step(v, nu), mu], -1), (edgeid[v, nu], -1)]))
    return verts, edges, faces, step


def direct_z2_torus(group, reflection, prof, expected, z_expected):
    _, edges, faces, _ = lattice((4, 2))
    ids = {e: i for i, e in enumerate(edges)}
    basis = list(it.product(range(2), repeat=2 if reflection == 'link' else 3))
    index = {b: i for i, b in enumerate(basis)}
    gmat = [[0]*len(basis) for _ in basis]
    ws = [group.weights(prof[v[0]][v[1]]) for v, _, _, _ in faces]
    for bits in range(1 << len(edges)):
        weight = 1
        for (_, _, _, boundary), w in zip(faces, ws):
            flux = 0
            for e, _ in boundary:
                flux ^= (bits >> e) & 1
            weight *= w[flux]
        c = [((bits >> ids[((t, 0), 1)]) ^ (bits >> ids[((t, 1), 1)])) & 1
             for t in range(4)]
        if reflection == 'link':
            neg, pos = (c[0], c[3]), (c[1], c[2])
        else:
            neg, pos = (c[0], c[3], c[2]), (c[0], c[1], c[2])
        gmat[index[neg]][index[pos]] += weight
    z = sum(map(sum, gmat))
    require(all(gmat[i][j]*z_expected == expected[i][j]*z
                for i in range(len(basis)) for j in range(len(basis))),
            'direct enumeration versus transfer ' + reflection)
    save_gram('direct_Z2_4x2_' + reflection, gmat, z, basis,
              {'original_link_configurations': 1 << len(edges), 'transfer_agreement': True})


def tree_free_edges(vertices, endpoints):
    parent = {v: v for v in vertices}
    def find(v):
        while parent[v] != v:
            v = parent[v]
        return v
    free, tree = [], []
    for i, (v, w) in enumerate(endpoints):
        a, b = find(v), find(w)
        if a == b:
            free.append(i)
        else:
            parent[a] = b; tree.append(i)
    require(len(tree) == len(vertices)-1, 'connected tree gauge')
    return free, tree


def full_3d_z2(group, reflection):
    vs, edges, faces, step = lattice((2, 2))
    vi = {v: i for i, v in enumerate(vs)}
    free, tree = tree_free_edges(vs, [(v, step(v, d)) for v, d in edges])
    states = []
    for bits in it.product(range(2), repeat=len(free)):
        a = [0]*len(edges)
        for e, bit in zip(free, bits): a[e] = bit
        states.append(a)
    n = len(states)
    ds, ks = [], []
    dprofile = [1, 1, 2, 2] if reflection == 'link' else [1, 2, 3, 2]
    kprofile = [1, 2, 3, 2] if reflection == 'link' else [1, 2, 2, 1]
    for t in range(4):
        dvals = []
        for a in states:
            w = 1
            for fnum, (_, _, _, bd) in enumerate(faces):
                flux = 0
                for e, _ in bd: flux ^= a[e]
                w *= group.weights(dprofile[t] + fnum % 2)[flux]
            dvals.append(w)
        ds.append(dvals)
        table = [[0]*n for _ in range(n)]
        weights = [group.weights(kprofile[t]+e % 2) for e in range(len(edges))]
        for i, a in enumerate(states):
            for j, b in enumerate(states):
                val = 0
                for h in it.product(range(2), repeat=len(vs)):
                    w = 1
                    for e, (v, d) in enumerate(edges):
                        flux = h[vi[v]] ^ b[e] ^ h[vi[step(v, d)]] ^ a[e]
                        w *= weights[e][flux]
                    val += w
                table[i][j] = val
        ks.append(table)
    if reflection == 'link':
        tail = mm(mm(scale_cols(ks[1], ds[2]), scale_cols(ks[2], ds[3])), ks[3])
        gram = [[ds[0][i]*ds[1][j]*ks[0][i][j]*tail[j][i]
                 for j in range(n)] for i in range(n)]
    else:
        left = mm(scale_cols(list(map(list, zip(*ks[0]))), ds[0]),
                  list(map(list, zip(*ks[3]))))
        right = mm(scale_cols(ks[1], ds[2]), ks[2])
        gram = [[ds[3][i]*ds[1][j]*left[j][i]*right[j][i]
                 for j in range(n)] for i in range(n)]
    save_gram('full_Z2_4x2x2_' + reflection, gram, sum(map(sum, gram)), states,
              {'all_48_plaquette_couplings_strictly_positive': True,
               'spatial_tree_edges': tree, 'observable': 'indicator of tree-gauged slice at t=1',
               'spatial_weight_profile': dprofile, 'temporal_weight_profile': kprofile})


def subfaces(lower, axes, dim):
    for varying in it.combinations(axes, dim):
        fixed = [a for a in axes if a not in varying]
        for signs in it.product((0, 1), repeat=len(fixed)):
            v = list(lower)
            for a, s in zip(fixed, signs): v[a] += s*(1 if a == 4 else 2)
            yield tuple(v), tuple(varying)


def vertices_of(cell):
    return [v for v, _ in subfaces(cell[0], cell[1], 0)]


def reflect_cell(cell, mu):
    lower, axes = cell; v = list(lower)
    v[mu] = -v[mu] - (2 if mu in axes else 0)
    return tuple(v), axes


def sphere_geometry(radius_num, radius_den):
    # a=1, chart coordinates stored doubled, exactly as G_a=Z^4+(1/2)^4.
    bound = radius_num // radius_den + 1
    cubes = []
    for k in it.product(range(-bound, bound+1), repeat=4):
        if sum((2*abs(x)+1)**2 for x in k)*radius_den**2 <= 4*radius_num**2:
            cubes.append(tuple(2*x-1 for x in k)+(0,))
    boundary_count = {}
    for low in cubes:
        for face in subfaces(low, (0, 1, 2, 3), 3):
            boundary_count[face] = boundary_count.get(face, 0)+1
    boundary = [c for c, n in boundary_count.items() if n == 1]
    cells = {}
    for low in cubes:
        k = 1+sum((x+1)**2 for x in low[:4])
        for sheet in (0, 1): cells[(low[:4]+(sheet,), (0, 1, 2, 3))] = k
    for low, axes in boundary:
        centre = [low[a]+(1 if a in axes else 0) for a in range(4)]
        cells[(low, axes+(4,))] = 1+sum(x*x for x in centre)
    edges, faces = set(), {}
    for (low, axes), k in cells.items():
        edges.update(subfaces(low, axes, 1))
        for f in subfaces(low, axes, 2): faces[f] = faces.get(f, 0)+k
    report = {'R_over_a': str(Q(radius_num, radius_den)), 'D_cubes': len(cubes),
              'boundary_3cells': len(boundary), 'K_4cells': len(cells),
              'edges': len(edges), 'plaquettes': len(faces), 'reflections': []}
    for mu in range(4):
        require(all(reflect_cell(e, mu) in edges for e in edges), 'sphere edge automorphism')
        require(all(cells.get(reflect_cell(c, mu)) == k for c, k in cells.items()),
                'sphere radial cell weights')
        require(all(faces.get(reflect_cell(f, mu)) == k for f, k in faces.items()),
                'sphere plaquette weights')
        crossing = []
        for f in faces:
            vals = [v[mu] for v in vertices_of(f)]
            if min(vals) < 0 < max(vals):
                crossing.append(f)
                require(reflect_cell(f, mu) == f, 'crossing face invariant')
                require(mu in f[1] and f[0][mu] == -1, 'crossing face square split')
                # A square with mu as one axis has one tangential edge in each
                # half and two reflected crossing edges. Reflection exchanges
                # those tangential edges and reverses the boundary cycle.
                tangent = next(a for a in f[1] if a != mu)
                poslow = list(f[0]); poslow[mu] = 1
                posedge = (tuple(poslow), (tangent,))
                require(posedge in edges and reflect_cell(posedge, mu) in edges,
                        'positive path and reflected path present')
        crosslinks = [e for e in edges if e[1] == (mu,) and e[0][mu] == -1]
        endpoints = [v for e in crosslinks for v in vertices_of(e)]
        require(len(endpoints) == len(set(endpoints)), 'sphere crossing links matching')
        require(all(not (e[1] == (4,) and min(v[mu] for v in vertices_of(e)) < 0 <
                         max(v[mu] for v in vertices_of(e))) for e in edges),
                'seam links do not cross coordinate plane')
        report['reflections'].append({'mu': mu, 'crossing_plaquettes': len(crossing),
                                      'crossing_prism_plaquettes': sum(4 in f[1] for f in crossing),
                                      'crossing_links': len(crosslinks)})
    print('SPHERE GEOMETRY', json.dumps(report), flush=True)
    return faces, report


def face_boundary(face, edgeid):
    low, (mu, nu) = face
    vm = list(low); vm[mu] += 1 if mu == 4 else 2
    vn = list(low); vn[nu] += 1 if nu == 4 else 2
    return [(edgeid[(low, (mu,))], 1), (edgeid[(tuple(vm), (nu,))], 1),
            (edgeid[(tuple(vn), (mu,))], -1), (edgeid[(low, (nu,))], -1)]


def prism_model(group, sphere_faces):
    # Boundary square of the central 4-cube, extruded across the seam.
    cube = ((-1, -1, 1, 1, 0), (0, 1, 4))
    verts = vertices_of(cube)
    edges = sorted(subfaces(*cube, 1))
    faces = sorted(subfaces(*cube, 2))
    require(all(f in sphere_faces for f in faces), 'prism faces belong to K_a')
    edgeid = {e: i for i, e in enumerate(edges)}
    endpoints = [vertices_of(e) for e in edges]
    free, tree = tree_free_edges(verts, endpoints)
    bd = [face_boundary(f, edgeid) for f in faces]
    weights = [group.weights(sphere_faces[f]) for f in faces]
    pos = next(i for i, f in enumerate(faces) if 0 not in f[1] and f[0][0] == 1)
    neg = faces.index(reflect_cell(faces[pos], 0))
    n = len(group.classes)
    gram = [[0]*n for _ in range(n)]
    for assignment in it.product(range(group.q), repeat=len(free)):
        links = [0]*len(edges)
        for e, g in zip(free, assignment): links[e] = g
        hol = [group.product(links[e] if sign == 1 else group.inv[links[e]]
                             for e, sign in boundary) for boundary in bd]
        w = 1
        for vals, h in zip(weights, hol): w *= vals[h]
        gram[group.cls[hol[neg]]][group.cls[hol[pos]]] += w
    save_gram('prism_' + group.name, gram, sum(map(sum, gram)), group.classes,
              {'subcomplex': cube, 'edges': edges, 'faces': faces,
               'effective_coupling_k': [sphere_faces[f] for f in faces],
               'tree_edges': tree, 'free_edges': free,
               'enumerated_gauge_fixed_assignments': group.q**len(free),
               'scope': 'six-face prism model, not enumeration of entire K_a'})


def controls(group):
    # All controls fixed in this script before its first run.
    prof = [[1, 1] for _ in range(4)]; prof[0][0] = -1
    mat, z, basis = torus_gram(group, 'link', prof)
    cert = save_gram('control_negative_beta', mat, z, basis, {'profile': prof}, False)
    detected = cert['hermitian'] and not cert['psd']
    print('NEGATIVE CONTROL negative_beta:', 'DETECTED negative eigenvalue' if detected else 'FAILED', flush=True)
    if not detected: FAILURES.append('negative_beta: no certified negative eigenvalue')

    prof = [[1, 1] for _ in range(4)]; prof[1][0] = 2
    mat, z, basis = torus_gram(group, 'link', prof)
    cert = save_gram('control_asymmetric_coupling', mat, z, basis, {'profile': prof}, False)
    herm = [[mat[i][j]+mat[j][i] for j in range(len(mat))] for i in range(len(mat))]
    hc = save_gram('control_asymmetric_coupling_hermitian_part', herm, 2*z, basis, {}, False)
    # Non-Hermiticity is already an RP failure, but is not a negative-eigenvalue
    # certificate for the original nonsymmetric matrix.
    if not cert['hermitian']:
        FAILURES.append('asymmetric_coupling: raw Gram non-Hermitian; requested negative eigenvalue not certified')
    elif cert['psd']:
        FAILURES.append('asymmetric_coupling: no negative eigenvalue')
    print('NEGATIVE CONTROL asymmetric_coupling: raw Hermitian=', cert['hermitian'],
          'Hermitian-part negative=', not hc['psd'], flush=True)

    # Independent Wilson-loop fluxes a+,b+,a-,b- in Z2, each Haar-uniform.
    # One added crossing closed walk has holonomy a+ b- (connector traversed
    # in both directions). Its reflected walk a- b+ is absent.
    bnames = ['1', 'a', 'b', 'ab']
    mat = [[0]*4 for _ in range(4)]; z = 0
    for ap, bp, am, bm in it.product((1, -1), repeat=4):
        w = 4 if ap*bm == 1 else 1
        fp, fm = (1, ap, bp, ap*bp), (1, am, bm, am*bm)
        z += w
        for i, x in enumerate(fm):
            for j, y in enumerate(fp): mat[i][j] += w*x*y
    save_gram('control_asymmetric_cell', mat, z, bnames,
              {'interaction': 'one closed crossing walk with holonomy a+ b-'}, False)
    herm = [[mat[i][j]+mat[j][i] for j in range(4)] for i in range(4)]
    hc = save_gram('control_asymmetric_cell_hermitian_part', herm, 2*z, bnames, {}, False)
    require(not hc['psd'], 'asymmetric cell Hermitian part has negative eigenvalue')
    # Raw matrix is diag(1,0,0,0) plus one off-diagonal nilpotent entry:
    # eigenvalues 1,0,0,0; H has eigenvalues 1,+3/10,-3/10,0.
    require(mat == [[z, 0, 0, 0], [0, 0, 0, 0], [0, 3*z//5, 0, 0], [0, 0, 0, 0]],
            'asymmetric cell exact raw spectrum certificate')
    FAILURES.append('asymmetric_cell: raw eigenvalues 1,0,0,0; Hermitian part has -3/10')
    print('NEGATIVE CONTROL asymmetric_cell: raw negative-eigenvalue criterion FAILED; H eigenvalue -3/10', flush=True)


def main():
    require(os.getpriority(os.PRIO_PROCESS, 0) >= 10, 'nice level >=10')
    for key in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
        require(os.environ.get(key) == '1', key + '=1')
    require((ROOT.parents[5] / '.locks_hrp_numeric').is_dir(), 'numeric lock held')
    criteria_sha = hashlib.sha256((ROOT/'hrp_criteria.md').read_bytes()).hexdigest()
    require(criteria_sha == '3e00f5ec5bbc32522636004aa72628c45884fe3762573c047e1105593ea82173',
            'pre-registered criteria unchanged')
    print('START', time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
          'criteria_sha256', criteria_sha, 'script_sha256',
          hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), flush=True)
    groups = [Group(name) for name in ('Z2', 'Z3', 'Q8')]
    for g in groups:
        for reflection in ('link', 'site'):
            prof = profiles(reflection)
            mat, z, basis = torus_gram(g, reflection, prof)
            save_gram(g.name+'_4x2_'+reflection, mat, z, basis, {'profile': prof})
            other, zo, _ = torus_gram(g, reflection, profiles(reflection, 1))
            require(psd_certificate(other)['psd'], 'second sheet PSD')
            save_gram(g.name+'_4x2x2_sheets_'+reflection, mat, z, basis,
                      {'tx_profile_y0': prof, 'tx_profile_y1': profiles(reflection, 1),
                       'ty_xy_couplings': 0, 'second_sheet_Z': zo,
                       'observable': 'same holonomy-class basis on y=0; other sheet cancels exactly'})
            zero, zz, zb = torus_gram(g, reflection, [[0, 0] for _ in range(4)])
            save_gram(g.name+'_zero_'+reflection, zero, zz, zb)
            if g.name == 'Z2': direct_z2_torus(g, reflection, prof, mat, z)
    for reflection in ('link', 'site'): full_3d_z2(groups[0], reflection)
    faces, report1 = sphere_geometry(11, 10)
    _, report2 = sphere_geometry(23, 10)
    (ROOT/'hrp_sphere_geometry.json').write_text(json.dumps([report1, report2], indent=2)+'\n')
    for g in groups: prism_model(g, faces)
    controls(groups[0])
    report = {'checks': RESULTS, 'negative_control_criterion_failures': FAILURES,
              'elapsed_seconds': time.monotonic()-START, 'peak_rss_bytes': peak_rss(),
              'theorem_status': 'finite diagnostics only; independent review pending'}
    (ROOT/'hrp_summary.json').write_text(json.dumps(report, indent=2)+'\n')
    print('POSITIVE MATRICES:', sum(r['psd'] for r in RESULTS if not r['name'].startswith('control')),
          'NEGATIVE CONTROL CRITERION FAILURES:', len(FAILURES), flush=True)
    for fail in FAILURES: print('REPORTED CONTROL FAILURE:', fail, flush=True)
    print('RESOURCE elapsed_seconds=', report['elapsed_seconds'],
          'peak_rss_bytes=', report['peak_rss_bytes'], flush=True)
    # Exit 2 distinguishes recorded control-criterion failures from crashes.
    return 2 if FAILURES else 0


if __name__ == '__main__':
    signal.signal(signal.SIGALRM, alarm)
    signal.alarm(1190)
    worker = threading.Thread(target=monitor, daemon=True)
    worker.start()
    try:
        status = main()
    finally:
        STOP.set(); worker.join(timeout=1); signal.alarm(0)
    sys.exit(status)
