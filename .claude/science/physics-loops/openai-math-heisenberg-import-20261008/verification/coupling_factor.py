"""Exact finite controls for the supplied ferromagnet theorem dictionary.

The infinite-volume theorem is an accepted external Lean-covered import.
This runner checks our new finite algebra and normalization; it does not
claim to construct a KMS state numerically or reverify the external library.
All decisive calculations below are exact SymPy matrix/symbolic arithmetic.
No external scientific files are read and no receipts are written.
"""
import itertools
import json

import sympy as s

AUDIT_TIMEOUT_SEC = 120


def exact_controls():
    X = s.Matrix([[0, 1], [1, 0]])
    Y = s.Matrix([[0, -s.I], [s.I, 0]])
    Z = s.diag(1, -1)
    pauli = [X, Y, Z]
    # Directly construct the formal model's ell=1 matrix units/levels.
    plus = s.Matrix([[0, 0], [1, 0]])
    minus = plus.H
    external_spin = [(plus + minus)/2, (plus - minus)/(2*s.I),
                     s.diag(-s.Rational(1, 2), s.Rational(1, 2))]
    basis_flip = X
    assert all(basis_flip*A*basis_flip.H == B/2
               for A, B in zip(external_spin, pauli))
    assert external_spin[2] != Z/2  # direct basis identification has wrong sign
    u2 = s.kronecker_product(basis_flip, basis_flip)
    h0 = -sum((s.kronecker_product(A, A) for A in external_spin), s.zeros(4))
    bond = sum((s.kronecker_product(A, A) for A in pauli), s.zeros(4))
    J = s.symbols('J', negative=True)
    kappa = -2*J
    hj = J*bond
    assert hj == kappa*u2*h0*u2.H
    assert hj != (-J)*u2*h0*u2.H
    assert hj != (4*J)*u2*h0*u2.H

    # All matrix units: the finite generator intertwines with time factor kappa.
    for i, j in itertools.product(range(4), repeat=2):
        A = s.zeros(4)
        A[i, j] = 1
        image = u2*A*u2.H
        assert s.simplify(hj*image-image*hj-kappa*u2*(h0*A-A*h0)*u2.H) == s.zeros(4)
    ell = s.Integer(1)
    assert 2*(ell/8) == s.Rational(1, 4)
    beta, beta0 = s.symbols('beta beta0', positive=True)
    beta_ext = kappa*beta
    assert s.simplify(beta_ext.subs(beta, beta0/kappa)-beta0) == 0
    # Positive kappa maps every closed strip coordinate into the required strip.
    for kap in [s.Rational(1, 3), s.Integer(2), s.Rational(7, 2)]:
        for b in [s.Rational(1, 5), s.Integer(3)]:
            for fraction in [s.Integer(0), s.Rational(1, 3), s.Integer(1)]:
                assert 0 <= kap*(b*fraction) <= kap*b

    # Independent geometric and bond-action constructions of a one-flip sector.
    L = 3
    sites = list(itertools.product(range(L), repeat=3))
    index = {x: i for i, x in enumerate(sites)}
    bonds = set()
    for x in sites:
        for axis in range(3):
            y = list(x)
            y[axis] = (y[axis]+1) % L
            bonds.add(tuple(sorted((index[x], index[tuple(y)]))))
    N = len(sites)
    direct = s.zeros(N)
    for down in range(N):
        for a, b in sorted(bonds):
            col = 2*int(down == a)+int(down == b)
            for row in range(4):
                coefficient = bond[row, col]
                if coefficient == 0:
                    continue
                output = {down}-{a, b}
                if row//2:
                    output.add(a)
                if row % 2:
                    output.add(b)
                assert len(output) == 1
                direct[next(iter(output)), down] += coefficient
    excitation_in_J_units = direct-len(bonds)*s.eye(N)
    laplacian = s.zeros(N)
    for x in sites:
        a = index[x]
        for axis in range(3):
            for sign in [-1, 1]:
                y = list(x)
                y[axis] = (y[axis]+sign) % L
                b = index[tuple(y)]
                laplacian[a, a] += 1
                laplacian[a, b] -= 1
    assert excitation_in_J_units == -2*laplacian
    assert excitation_in_J_units != -laplacian

    k = s.symbols('k', real=True)
    energy_axis = -4*J*(1-s.cos(k))
    D = s.diff(energy_axis, k, 2).subs(k, 0)/2
    quartic = s.diff(energy_axis, k, 4).subs(k, 0)/s.factorial(4)
    assert D == -2*J == kappa/2
    assert quartic == -D/12
    a = s.symbols('a', positive=True)
    i0 = s.integrate(s.exp(-a*k*k), (k, -s.oo, s.oo))
    i4 = s.integrate(k**4*s.exp(-a*k*k), (k, -s.oo, s.oo))
    assert s.simplify(i4/i0) == 3/(4*a*a)
    assert s.simplify(3*a*i4/(12*i0)) == 3/(16*a)
    return {
        'sympy_version': s.__version__,
        'exact_import': 'OAI.Heisenberg.spontaneous_magnetization at d=3, ell=1',
        'external_basis_spin_z': str(external_spin[2]),
        'basis_flip': str(basis_flip),
        'external_coupling_kappa': str(kappa),
        'magnetization_lower_bound_pauli': '1/4',
        'beta_threshold': 'beta0/(-4*J), J<0',
        'all_16_bond_generator_matrix_units_match': True,
        'torus_sites': N,
        'torus_unordered_bonds': len(bonds),
        'one_flip_identity': 'H-E_all_up = -2*J*graph_Laplacian',
        'dispersion_quadratic': str(D),
        'dispersion_quartic_axis': str(quartic),
        'normalized_Gaussian_fourth_moment': str(s.simplify(i4/i0)),
        'relative_three_axis_first_correction': str(s.simplify(3*a*i4/(12*i0))),
        'many_body_asymptotic': 'Separately paper-premised; not proved by these finite checks',
        'external_Lean_local_rebuild': 'not run; accepted provider theorem at pinned scope',
    }


if __name__ == '__main__':
    print(json.dumps(exact_controls(), indent=2))
    print('PASS basis, coupling, magnetization and finite generator dictionary')
    print('PASS exact direct one-spin-flip operator versus geometric Laplacian')
    print('PASS dispersion Taylor coefficients and Gaussian integral identities')
    print('per_element: all one-site matrices and16 bond matrix units are exact.')
    print('per_site: the supplied translation-covariant dictionary is proved in the note.')
    print('per_mode: exact dispersion normalization; no thermal many-body remainder is computed.')
    print('per_block: all729 entries of the27-state one-flip block are compared.')
    print('lattice_wide: the KMS/order claim uses the matched external theorem and written scaling proof.')
    print('TOTAL: PASS=3 FAIL=0')
