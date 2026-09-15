"""Finite challenges to Block17, with explicit boundary and alias retention."""
from __future__ import annotations
import importlib.util
import itertools
import json
from pathlib import Path
import numpy as np
from scipy.linalg import eigh, eigh_tridiagonal
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import eigsh
from scipy.special import mathieu_a

HERE = Path(__file__).resolve().parent
RNG = np.random.default_rng(17160915)


def one_continuum(ell, modes=80, levels=5):
    m = np.arange(-modes, modes+1)
    kinetic = 2*np.pi**2*m**2/ell**2
    diag = kinetic+ell**2/np.pi**2
    off = np.full(len(m)-1, -ell**2/(2*np.pi**2))
    es, vs = eigh_tridiagonal(diag, off, select='i', select_range=(0, levels-1))
    return es, vs, kinetic


def one_finite(g, n, levels=5):
    # Electric basis retains the corner wrap. All n states are physical.
    ns = np.arange(-(n//2), n//2+1)
    potential = 2*(g*n)**2/np.pi**2*np.sin(np.pi*ns/n)**2
    h = np.diag(potential+1/g**2)
    for j in range(n):
        h[(j+1) % n, j] -= .5/g**2
        h[j, (j+1) % n] -= .5/g**2
    es, vs = eigh(h, subset_by_index=(0, levels-1))
    return es, vs, potential


def two_geometry():
    vertices = [(x, y) for y in range(2) for x in range(3)]
    edges = [(0, 1), (1, 2), (3, 4), (4, 5), (0, 3), (1, 4), (2, 5)]
    d = np.zeros((6, 7), int)
    for j, (a, b) in enumerate(edges):
        d[a, j] = 1; d[b, j] = -1
    f = np.array([[1, 0], [0, 1], [-1, 0], [0, -1],
                  [-1, 0], [1, -1], [0, 1]])
    tree, chords = [0, 1, 4, 5, 6], [2, 3]
    r = np.zeros((7, 6), int)
    r[np.ix_(tree, range(1, 6))] = np.rint(np.linalg.inv(d[np.ix_(range(1, 6), tree)])).astype(int)
    c = np.eye(7, dtype=int)[:, chords]-r @ d[:, chords]
    z = f[chords, :]
    assert np.array_equal(d @ r, np.eye(6, dtype=int)-np.eye(6, dtype=int)[:, [0]] @ np.ones((1, 6), int))
    assert np.array_equal(d @ c, np.zeros((6, 2), int))
    assert np.array_equal(c[chords], np.eye(2, dtype=int))
    assert np.array_equal(c @ z, f)
    assert abs(round(np.linalg.det(z))) == 1
    return d, f, r, c, z


def rep(x, n):
    return (np.asarray(x)+n//2) % n-n//2


def gauss_coordinate_checks():
    d, f, r, c, z = two_geometry()
    rows = []
    for n in [3, 5, 9, 15]:
        coords = list(itertools.product(range(-(n//2), n//2+1), repeat=2))
        for charge in [np.zeros(6, int), np.array([1, 0, -1, 0, 0, 0]),
                       np.array([0, 1, 0, 0, -1, 0])]:
            fields = [tuple(rep(r @ charge+c @ v, n)) for v in coords]
            assert len(set(fields)) == n*n
            assert all(np.all((d @ e-charge) % n == 0) for e in fields)
            if n == 3:
                brute = {e for e in itertools.product(range(-1, 2), repeat=7)
                         if np.all((d @ e-charge) % 3 == 0)}
                assert set(fields) == brute
        fields = np.array([rep(c @ v, n) for v in coords])
        aliases = np.any(fields @ d.T != 0, axis=1)
        expected = (n//2)*(n//2+1)
        assert sum(aliases) == expected
        # Every link marginal of the uniform divergence-free state is uniform.
        for j in range(7):
            assert np.array_equal(np.bincount(fields[:, j]+n//2, minlength=n), np.full(n, n))
        rows.append(dict(N=n, dimension=n*n, alias_count=int(sum(aliases)),
                         alias_probability=float(np.mean(aliases)),
                         exact_expected=expected/n**2, composite_N=(n in [9, 15])))
    return rows


def two_finite(g, n):
    d, _, _, c, z = two_geometry()
    coords = list(itertools.product(range(n), repeat=2))
    idx = {q: j for j, q in enumerate(coords)}
    fields = np.array([rep(c @ q, n) for q in coords])
    electric = (g*n)**2/(2*np.pi**2)*np.sum(np.sin(np.pi*fields/n)**2, axis=1)
    rr, cc, vv = list(range(n*n)), list(range(n*n)), list(electric+2/g**2)
    for col, q in enumerate(coords):
        for zp in z.T:
            for sign in [-1, 1]:
                row = idx[tuple((np.array(q)+sign*zp) % n)]
                rr.append(row); cc.append(col); vv.append(-.5/g**2)
    h = coo_matrix((vv, (rr, cc)), shape=(n*n, n*n)).tocsr()
    # The nearly degenerate first excited cluster stalled a three-vector
    # Lanczos solve. Keep all three levels and the original residual gate,
    # using direct Hermitian diagonalization at these finite dimensions.
    es, vs = eigh(h.toarray(), subset_by_index=(0, 2))
    order = np.argsort(es); es, vs = es[order], vs[:, order]
    psi = vs[:, 0]
    residual = float(np.linalg.norm(h @ psi-es[0]*psi))
    assert residual < 2e-8
    alias = np.any(fields @ d.T != 0, axis=1)
    uniform = np.ones(n*n)/n
    if np.dot(uniform, psi) < 0:
        psi = -psi
    return dict(N=n, g=g, ell=g*n, energies=es.tolist(), residual=residual,
                alias_probability=float(abs(psi)**2 @ alias),
                uniform_alias_probability=float(np.mean(alias)),
                distance_to_uniform=float(np.linalg.norm(psi-uniform)),
                electric_energy=float(abs(psi)**2 @ electric),
                magnetic_energy=float(es[0]-abs(psi)**2 @ electric))


def charged_cycle_checks():
    # Use the previously independently checked exact CAR/full Gauss matrix,
    # then independently build its free-link matter comparator here.
    spec = importlib.util.spec_from_file_location('block16', HERE/'block16_cyclic_equilibrium_check.py')
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    m.T, m.PHI, m.U = .12, .19, .17
    masks = [f for f in range(256) if sum(m.charges(f)) == 0]
    pos = {f: i for i, f in enumerate(masks)}
    hm = np.zeros((len(masks), len(masks)), complex)
    for col, mask in enumerate(masks):
        q = m.charges(mask); hm[col, col] = m.U*(q @ q)/2
        for link in range(4):
            for species, charge in [(0, 1), (1, -1)]:
                result = m.fermion_hop(mask, 2*link+species,
                                      2*((link+1) % 4)+species)
                if result:
                    target, sign = result
                    row = pos[target]; value = m.T*np.exp(1j*charge*m.PHI)*sign
                    hm[row, col] += value; hm[col, row] += value.conjugate()
    matter_es = np.linalg.eigvalsh(hm)
    m.K_E = m.K_B = 0
    h_matter, basis, _, _ = m.matrix(2, True)
    p = np.zeros((len(basis), len(masks)), complex)
    for row, (mask, _) in enumerate(basis):
        p[row, pos[mask]] = 1/np.sqrt(5)
    uniform_reduction_error = float(np.max(abs(h_matter @ p-p @ hm)))
    assert uniform_reduction_error < 1e-13
    rows = []
    for ell in [2., 4.]:
        osc, _, _ = one_continuum(ell)
        target = sorted(a+b for a in osc for b in matter_es)[:4]
        for n in [9, 17, 33]:
            g = ell/n
            m.K_E, m.K_B = g*g/2, 1/(g*g)
            h, basis, _, _ = m.matrix(n//2, True)
            start = RNG.normal(size=len(basis))+1j*RNG.normal(size=len(basis))
            es, vs = eigsh(h, k=4, which='SA', tol=1e-11, v0=start)
            order = np.argsort(es); es, vs = es[order], vs[:, order]
            psi = vs[:, 0]
            residual = float(np.linalg.norm(h @ psi-es[0]*psi))
            assert residual < 1e-8
            lookup = {b: i for i, b in enumerate(basis)}
            plaquette = np.zeros_like(psi)
            for col, (mask, e) in enumerate(basis):
                plaquette[lookup[(mask, tuple(m.representative(x+1, n) for x in e))]] = psi[col]
            deficit = float(1-np.vdot(psi, plaquette).real)
            bound = g*g*(ell*ell/np.pi**2+16*m.T)
            assert deficit <= bound+1e-10
            rows.append(dict(ell=ell, N=n, dimension=len(basis), energies=es.tolist(),
                             continuum_targets=target, maximum_level_error=float(max(abs(es-target))),
                             residual=residual, plaquette_deficit=deficit,
                             deficit_bound=bound))
    return dict(uniform_matter_reduction_error=uniform_reduction_error,
                matter_dimension=len(masks), matter_low_energies=matter_es[:5].tolist(),
                note='u Q^2 remains in the finite matter comparator; not a free-fermion substitution',
                spectra=rows)


def main():
    continuum = []
    for ell in [.5, 1., 2., 4., 8., 16.]:
        es, vs, kinetic = one_continuum(ell)
        es2, _, _ = one_continuum(ell, modes=120)
        special = ell**2/np.pi**2+np.pi**2/(2*ell**2)*mathieu_a(0, -ell**4/np.pi**4)
        error = abs(es[0]-special)
        refinement = float(max(abs(es-es2)))
        assert error < 2e-9 and refinement < 2e-8
        assert 0 < es[0] < 1
        continuum.append(dict(ell=ell, energies=es.tolist(), mathieu_ground=float(special),
                              mathieu_error=float(error), refinement_error=refinement,
                              magnetic_energy=float(abs(vs[:, 0])**2 @ kinetic),
                              gaussian_energy_error_scaled=float((1-es[0])*ell**2)))
    fixed_ell = []
    for ell in [1., 3., 6.]:
        target, _, _ = one_continuum(ell)
        for n in [31, 61, 121]:
            es, _, _ = one_finite(ell/n, n)
            fixed_ell.append(dict(ell=ell, N=n, energies=es.tolist(),
                                  maximum_level_error=float(max(abs(es-target)))))
    infinite_ell = []
    for n in [31, 61, 121, 241]:
        g = 1/np.sqrt(n)
        es, _, _ = one_finite(g, n)
        infinite_ell.append(dict(N=n, g=g, ell=g*n, energies=es.tolist(),
                                 oscillator_targets=[1, 3, 5, 7, 9]))
    vanishing_ell = []
    for n in [9, 17, 33]:
        g = n**(-1.5)
        es, _, _ = one_finite(g, n)
        ell = g*n
        vanishing_ell.append(dict(N=n, g=g, ell=ell, energies=es.tolist(),
                                  ground_over_ell_squared=float(es[0]/ell**2),
                                  first_gap_times_ell_squared=float((es[1]-es[0])*ell**2)))
    two = [two_finite(ell/n, n) for ell in [.5, 2., 5.] for n in [9, 17, 33]]
    result = dict(status='personal_finite_checks_no_phase_or_independent_audit',
                  exact_gauss=gauss_coordinate_checks(), continuum_one_plaquette=continuum,
                  fixed_ell_one_plaquette=fixed_ell, infinite_ell_one_plaquette=infinite_ell,
                  vanishing_ell_one_plaquette=vanishing_ell,
                  two_plaquette_ground_states=two, charged_cycle=charged_cycle_checks(),
                  limits=['No thermodynamic photon or matter phase was computed.',
                          'Fourier truncation refinement is a numerical check, not an interval proof.',
                          'Fixed-ell, infinite-ell and vanishing-ell are distinct limits.',
                          'Uniform-flow alias probability is exact; phase claims do not follow.'])
    output = json.dumps(result, indent=2)
    (HERE/'block17_cyclic_scaling_check.json').write_text(output+'\n')
    print(output)


if __name__ == '__main__':
    main()
