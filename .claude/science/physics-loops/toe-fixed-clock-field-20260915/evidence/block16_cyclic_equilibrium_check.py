"""Personal finite fixtures for Block16; no phase or infinite-limit computation.

Four oriented edges i -> i+1, two opposite-charge CAR modes per vertex.
The generic theorem is cubic; this fixture intentionally is not cubic.
"""
from __future__ import annotations
import json
import math
from pathlib import Path
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import eigsh

HERE = Path(__file__).resolve().parent
CE = 4 / np.pi**2
K_E, K_B, T, PHI, U = .605, .4, .18, .23, .7
B_TOTAL = K_B + 16*T


def charges(mask):
    return np.array([((mask >> (2*i)) & 1) - ((mask >> (2*i+1)) & 1)
                     for i in range(4)], dtype=int)


def representative(x, n):
    s = n//2
    return (x+s) % n - s


def reduced_basis(cut, cyclic):
    n = 2*cut+1
    basis = []
    for mask in range(256):
        q = charges(mask)
        if (sum(q) % n if cyclic else sum(q)) != 0:
            continue
        for seed in range(-cut, cut+1):
            e = [seed+int(v) for v in np.cumsum(q)[:3]] + [seed]
            if cyclic:
                e = [representative(v, n) for v in e]
            if max(map(abs, e)) <= cut:
                basis.append((mask, tuple(e)))
    return basis


def fermion_hop(mask, create, destroy):
    if not (mask >> destroy) & 1 or (mask >> create) & 1:
        return None
    sign = (-1)**((mask & ((1 << destroy)-1)).bit_count())
    middle = mask ^ (1 << destroy)
    sign *= (-1)**((middle & ((1 << create)-1)).bit_count())
    return middle | (1 << create), sign


def matrix(cut, cyclic, basis=None):
    n = 2*cut+1
    if basis is None:
        basis = reduced_basis(cut, cyclic)
    lookup = {x: i for i, x in enumerate(basis)}
    rows, cols, vals = [], [], []
    electric, aliases = [], []
    for col, (mask, et) in enumerate(basis):
        e = np.array(et)
        e2 = float(e @ e)
        electric.append(e2)
        q = charges(mask)
        gauss = e-np.roll(e, 1)-q
        assert np.all(gauss % n == 0) if cyclic else np.all(gauss == 0)
        aliases.append(gauss != 0)
        ev = K_E*np.sum(e**2*np.sinc(e/n)**2) if cyclic else K_E*e2
        rows.append(col); cols.append(col)
        vals.append(ev + K_B + U*float(q @ q)/2)
        # Forward plaquette, then adjoint; hard-cut boundary retains K_B I.
        ep = e+1
        if cyclic:
            ep = np.array([representative(x, n) for x in ep])
        if max(abs(ep)) <= cut:
            row = lookup[(mask, tuple(ep))]
            rows.extend([row, col]); cols.extend([col, row])
            vals.extend([-K_B/2, -K_B/2])
        for link in range(4):
            for species, charge in [(0, 1), (1, -1)]:
                result = fermion_hop(mask, 2*link+species,
                                     2*((link+1) % 4)+species)
                if result is None:
                    continue
                new_mask, sign = result
                eh = e.copy(); eh[link] += charge
                if cyclic:
                    eh[link] = representative(eh[link], n)
                if max(abs(eh)) > cut:
                    continue
                row = lookup[(new_mask, tuple(eh))]
                value = T*np.exp(1j*charge*PHI)*sign
                rows.extend([row, col]); cols.extend([col, row])
                vals.extend([value, value.conjugate()])
    h = coo_matrix((vals, (rows, cols)), shape=(len(basis), len(basis)),
                   dtype=complex).tocsr()
    assert np.max(np.abs((h-h.getH()).data), initial=0) < 1e-13
    return h, basis, np.array(electric), np.array(aliases)


def direct_projected_n3():
    # Independent full electric enumeration and literal 256-dimensional CAR.
    from itertools import product
    n, cut = 3, 1
    basis = [(mask, e) for mask in range(256)
             for e in product(range(-1, 2), repeat=4)
             if np.all((np.array(e)-np.roll(e, 1)-charges(mask)) % 3 == 0)]
    lookup = {x: i for i, x in enumerate(basis)}
    annihilators = []
    for mode in range(8):
        c = np.zeros((256, 256))
        for mask in range(256):
            occ = [(mask >> j) & 1 for j in range(8)]
            if occ[mode]:
                c[mask-(1 << mode), mask] = (-1)**sum(occ[:mode])
        annihilators.append(c)
    for i in range(8):
        for j in range(8):
            anti = annihilators[i] @ annihilators[j].T
            anti += annihilators[j].T @ annihilators[i]
            assert np.max(abs(anti-(np.eye(256) if i == j else 0))) == 0
    h = np.zeros((len(basis), len(basis)), dtype=complex)
    hop = {(i, s): annihilators[2*i+s].T @
           annihilators[2*((i+1) % 4)+s] for i in range(4) for s in range(2)}
    for col, (mask, et) in enumerate(basis):
        q, e = charges(mask), np.array(et)
        h[col, col] += K_E*sum(e**2*np.sinc(e/3)**2)+K_B+U*(q @ q)/2
        for sign in [-1, 1]:
            ep = tuple((e+sign+1) % 3-1)
            h[lookup[(mask, ep)], col] -= K_B/2
        for i in range(4):
            for s, charge in [(0, 1), (1, -1)]:
                for sign in [-1, 1]:
                    op = hop[i, s] if sign == 1 else hop[i, s].T
                    eh = e.copy(); eh[i] = (eh[i]+sign*charge+1) % 3-1
                    for new_mask in np.flatnonzero(op[:, mask]):
                        h[lookup[(int(new_mask), tuple(eh))], col] += (
                            T*np.exp(1j*sign*charge*PHI)*op[new_mask, mask])
    return h, basis


def theta_bound(q):
    return 1+math.sqrt(math.pi/q)


def cyclic_checks(n):
    h, basis, e2, alias = matrix(n//2, True)
    energies, vecs = np.linalg.eigh(h.toarray())
    ground = vecs[:, 0]
    p_ground = abs(ground)**2
    ground_moment = float(p_ground @ e2)
    ground_bound = B_TOTAL/(CE*K_E)
    assert ground_moment <= ground_bound+1e-10
    e_fields = np.array([e for _, e in basis])
    # A physical, non-Hermitian unitary plaquette shift.
    lookup = {x: i for i, x in enumerate(basis)}
    a = np.zeros(h.shape, complex)
    for col, (mask, e) in enumerate(basis):
        a[lookup[(mask, tuple(representative(x+1, n) for x in e))], col] = 1
    w = vecs.conj().T @ a @ vecs
    gaps = energies[None, :]-energies[:, None]  # row low n, column high m
    rows = []
    for beta in [.5, 1.5, 5., 15.]:
        p = np.exp(-beta*(energies-energies[0])); p /= sum(p)
        diagonal = abs(vecs)**2 @ p
        moment = float(diagonal @ e2)
        entropy = float(-np.dot(p[p > 0], np.log(p[p > 0])))
        log_ref_upper = 8*np.log(2)+4*np.log(theta_bound(beta*CE*K_E/2))
        entropy_rhs = beta*CE*K_E*moment/2+log_ref_upper
        bound = 2/(CE*K_E)*(B_TOTAL+log_ref_upper/beta)
        assert entropy <= entropy_rhs+1e-10 and moment <= bound+1e-10
        alias_p = diagonal @ alias
        local_second = diagonal @ (e_fields**2)
        alias_rhs = 3*(local_second+np.roll(local_second, 1)+1)/n**2
        assert np.all(alias_p <= alias_rhs+1e-11)
        # W_nm has A going from m to n, so a positive gap E_m-E_n
        # contributes negative-energy A weight p_m |W_nm|^2.
        positive = gaps > 1e-10
        neg_weight = p[None, :]*abs(w)**2
        adj_positive = p[:, None]*abs(w)**2
        expected = np.exp(-beta*gaps[positive])*adj_positive[positive]
        balance_error = float(np.max(abs(neg_weight[positive]-expected), initial=0))
        assert balance_error < 1e-12
        epsilon = .4
        neg_mass = float(np.sum(neg_weight[gaps >= epsilon]))
        neg_bound = math.exp(-beta*epsilon)  # ||A||=1
        assert neg_mass <= neg_bound+1e-11
        rows.append(dict(beta=beta, electric_square=moment,
                         electric_square_bound=bound, entropy=entropy,
                         entropy_bound=entropy_rhs,
                         any_integer_alias_probability=float(diagonal @ np.any(alias, axis=1)),
                         maximal_vertex_alias_probability=float(max(alias_p)),
                         minimal_vertex_alias_bound=float(min(alias_rhs)),
                         detailed_balance_max_error=balance_error,
                         negative_energy_mass=neg_mass, negative_energy_bound=neg_bound))
    return dict(N=n, dimension=len(basis), ground_energy=float(energies[0]),
                ground_electric_square=ground_moment, ground_bound=ground_bound,
                alias_basis_states=int(sum(np.any(alias, axis=1))), thermal=rows)


def main():
    coercivity = []
    for n in [3, 5, 7, 17, 101, 1001]:
        es = np.arange(1, n//2+1)
        ratio = np.sinc(es/n)**2
        assert min(ratio) >= CE-1e-15 and max(ratio) <= 1+1e-15
        coercivity.append(dict(N=n, minimum_ratio=float(min(ratio))))
    independent, direct_basis = direct_projected_n3()
    reduced, reduced_b, _, _ = matrix(1, True)
    direct_index = {x: i for i, x in enumerate(direct_basis)}
    perm = [direct_index[x] for x in reduced_b]
    independent_error = float(np.max(abs(independent[np.ix_(perm, perm)]-reduced.toarray())))
    assert independent_error < 1e-13
    thermal = [cyclic_checks(n) for n in [3, 5, 7]]
    ground = []
    rng = np.random.default_rng(16160915)
    for cyclic, cuts in [(False, [2, 4, 8, 12]), (True, [4, 6, 8, 12, 16])]:
        for cut in cuts:
            h, basis, e2, alias = matrix(cut, cyclic)
            # A constant start can exclude a symmetry sector exactly. Use a
            # deterministic generic complex start; no sector restriction.
            start = rng.normal(size=len(basis))+1j*rng.normal(size=len(basis))
            energy, vectors = eigsh(h, k=1, which='SA', tol=1e-12, v0=start)
            psi = vectors[:, 0]
            residual = float(np.linalg.norm(h @ psi-energy[0]*psi))
            assert residual < 1e-9
            ground.append(dict(regulator='cyclic' if cyclic else 'hard_integer',
                               cut=cut, N=2*cut+1, dimension=len(basis),
                               ground_energy=float(energy[0]), residual=residual,
                               electric_square=float(abs(psi)**2 @ e2),
                               alias_probability=float(abs(psi)**2 @ np.any(alias, axis=1))))
    result = dict(status='personal_finite_checks_pass_no_phase_or_independent_audit',
                  model='four-edge charged cycle, two conjugate CAR modes per vertex',
                  constants=dict(cE=CE, kE=K_E, kB=K_B, hop=T, phase=PHI,
                                 repulsion=U, B_total=B_TOTAL),
                  independent_projected_matrix_error=independent_error,
                  coercivity=coercivity, thermal=thermal, ground_comparisons=ground,
                  limits=['Noncubic finite fixtures do not prove cubic thermodynamic claims.',
                          'Hard cutoff 12 is a finite comparator, not an exact infinite rotor.',
                          'The analytic proof, not eigenvalue convergence plots, establishes existence.',
                          'No positive estimator for arbitrary observables was checked.'])
    output = json.dumps(result, indent=2)
    (HERE/'block16_cyclic_equilibrium_check.json').write_text(output+'\n')
    print(output)


if __name__ == '__main__':
    main()
