"""Exact small charged-ring checks; no cubic or thermodynamic phase solve."""
from pathlib import Path
import itertools
import json
import numpy as np
import sympy as sp
from scipy.linalg import eigh

HERE = Path(__file__).resolve().parent
MASKS = [m for m in range(16) if m.bit_count() == 2]
ETA = np.array([0, 1, 0, 1])
OMEGA = 2**(-.25)
FLOOR = -2*np.sqrt(2)


def charge(mask):
    return np.array([(mask >> j) & 1 for j in range(4)])-ETA


def offset(mask):
    return np.r_[np.cumsum(charge(mask))[:3], 0]


def hop(mask, create, destroy):
    if not((mask >> destroy) & 1) or (mask >> create) & 1:
        return None
    sign = (-1)**((mask & ((1 << destroy)-1)).bit_count())
    middle = mask ^ (1 << destroy)
    sign *= (-1)**((middle & ((1 << create)-1)).bit_count())
    return middle | (1 << create), sign


def reduced(g, cut, omit_offsets=False):
    basis = [(mask, n) for mask in MASKS for n in range(-cut, cut+1)
             if max(abs(n+offset(mask))) <= cut]
    lookup = {v: i for i, v in enumerate(basis)}
    h = np.zeros((len(basis), len(basis)))
    fields = np.array([n+offset(mask) for mask, n in basis])
    for col, (mask, n) in enumerate(basis):
        h[col, col] = 2*g*g*n*n if omit_offsets else g*g*(fields[col] @ fields[col])/2
        for link in range(4):
            result = hop(mask, link, (link+1) % 4)
            if result:
                target, sign = result
                key = (target, n+int(link == 3))
                if key in lookup:
                    row = lookup[key]; h[row, col] += sign; h[col, row] += sign
    return h, basis, fields


def direct_full(g, cut):
    # Literal ambient 16-dimensional CAR, followed by all-field Gauss projection.
    operators = []
    for j in range(4):
        c = np.zeros((16, 16))
        for mask in range(16):
            occ = [(mask >> k) & 1 for k in range(4)]
            if occ[j]:c[mask-(1 << j), mask] = (-1)**sum(occ[:j])
        operators.append(c)
    hops = [operators[j].T @ operators[(j+1) % 4] for j in range(4)]
    basis = [(f, e) for f in MASKS
             for e in itertools.product(range(-cut, cut+1), repeat=4)
             if np.array_equal(np.array(e)-np.roll(e, 1), charge(f))]
    lookup = {b: i for i, b in enumerate(basis)}
    h = np.zeros((len(basis), len(basis)))
    for col, (mask, et) in enumerate(basis):
        e = np.array(et); h[col, col] = g*g*(e @ e)/2
        for j, op in enumerate(hops):
            for sign in [-1, 1]:
                matrix = op if sign == 1 else op.T
                ep = e.copy(); ep[j] += sign
                if max(abs(ep)) > cut:continue
                for target in np.flatnonzero(matrix[:, mask]):
                    h[lookup[(int(target), tuple(ep))], col] += matrix[target, mask]
    return h, basis


def symbolic_frame():
    pos = {m: i for i, m in enumerate(MASKS)}
    forward = sp.zeros(6); forward_z = sp.zeros(6)
    z = sp.symbols('z', nonzero=True)
    for col, mask in enumerate(MASKS):
        for j in range(4):
            result = hop(mask, j, (j+1) % 4)
            if result:
                target, sign = result; row = pos[target]
                forward[row, col] += sign*(-1 if j == 3 else 1)
                forward_z[row, col] += sign*(-z**4 if j == 3 else 1)
    offsets = [list(map(int, offset(m))) for m in MASKS]
    a = sp.diag(*[sp.Rational(sum(e), 4) for e in offsets])
    c = sp.diag(*[sum(sp.Rational(v*v, 2) for v in e)-2*sp.Rational(sum(e), 4)**2 for e in offsets])
    u_frame = sp.diag(*[z**(-4*a[j, j]) for j in range(6)])
    hm = forward_z+forward_z.T.subs(z, 1/z)
    transformed = (u_frame.inv()*hm*u_frame).applyfunc(sp.simplify)
    assert transformed == z*forward+forward.T/z
    assert forward*forward.T == forward.T*forward
    u = sp.Matrix([sp.sqrt(2)/4, -sp.Rational(1, 2), sp.sqrt(2)/4,
                   sp.sqrt(2)/4, -sp.Rational(1, 2), sp.sqrt(2)/4])
    assert (forward*u+sp.sqrt(2)*u).applyfunc(sp.simplify) == sp.zeros(6, 1)
    scalar = sp.simplify((u.T*c*u)[0]); assert scalar == sp.Rational(5, 16)
    mean_a = sp.simplify((u.T*a*u)[0])
    ordinary_metric = sp.simplify(2*((u.T*a*a*u)[0]-mean_a**2))
    assert ordinary_metric == sp.Rational(3, 16)
    ann = sp.zeros(12)
    for j in range(1, 12):ann[j-1, j] = sp.sqrt(j)
    omega = 2**(-sp.Rational(1, 4))
    xi = sp.sqrt(2/omega)*(ann+ann.T)
    xi4 = xi**4
    c2 = [sp.simplify(scalar-sp.sqrt(2)*xi4[j, j]/3072) for j in range(4)]
    assert c2 == [sp.Rational(v, 128) for v in [39, 35, 27, 15]]
    return dict(offsets=offsets, A=[str(a[j, j]) for j in range(6)],
                C=[str(c[j, j]) for j in range(6)], C_ground=str(scalar),
                ordinary_derivative_term_if_offsets_deleted=str(ordinary_metric),
                exact_c2=[str(v) for v in c2],
                frame_identity='U^-1 H(pi+delta) U=z F+z^-1 F^T, [F,F^T]=0')


def physical_spectra():
    rows = []
    for g in [.16, .08, .04, .02, .01]:
        cut = int(np.ceil(5/np.sqrt(g)))+2
        h, basis, fields = reduced(g, cut)
        es, vs = eigh(h, subset_by_index=(0, 3))
        residual = float(max(np.linalg.norm(h @ vs[:, j]-es[j]*vs[:, j]) for j in range(4)))
        assert residual < 2e-11
        c2 = np.array([39, 35, 27, 15])/128
        expansion = FLOOR+OMEGA*(np.arange(4)+.5)*g+c2*g*g
        scaled_remainder = (es-expansion)/g**3
        assert max(abs(scaled_remainder)) < 1
        psi = vs[:, 0]; lookup = {b: i for i, b in enumerate(basis)}
        shifted = np.zeros_like(psi)
        for col, (mask, n) in enumerate(basis):
            if (mask, n+1) in lookup:shifted[lookup[(mask, n+1)]] = psi[col]
        loop = float(np.dot(psi, shifted))
        electric = g*(psi**2 @ (fields**2))
        rows.append(dict(g=g, cutoff=cut, dimension=len(basis), energies=es.tolist(),
                         residual=residual, two_term_c2=((es-FLOOR-OMEGA*(np.arange(4)+.5)*g)/g**2).tolist(),
                         remainder_over_g3=scaled_remainder.tolist(),
                         gap_over_g=float((es[1]-es[0])/g),
                         gap_g2_coefficient=float((es[1]-es[0]-OMEGA*g)/g**2),
                         loop_expectation=loop, loop_scaled=(1+loop)/g,
                         electric_scaled_per_link=electric.tolist()))
    assert abs(rows[-1]['loop_scaled']-1/OMEGA) < .02
    assert max(abs(np.array(rows[-1]['electric_scaled_per_link'])-OMEGA/8)) < .005
    return rows


def main():
    exact = symbolic_frame()
    comparisons = []
    for cut in [1, 2]:
        h, b, _ = reduced(.25, cut)
        hd, bd = direct_full(.25, cut); lookup = {v: i for i, v in enumerate(bd)}
        perm = [lookup[(f, tuple(n+offset(f)))] for f, n in b]
        error = float(np.max(abs(h-hd[np.ix_(perm, perm)])))
        assert error == 0
        comparisons.append(dict(cutoff=cut, dimension=len(b), matrix_error=error))
    cutoff = []
    for g in [1e-2, 1e-3, 1e-4, 1e-5]:
        cut = int(np.ceil(g**(-.25)))
        h, _, _ = reduced(g, cut)
        e = float(eigh(h, subset_by_index=(0, 0), eigvals_only=True)[0])
        bound = np.sqrt(2)/8*(1-np.cos(np.pi/(2*cut+2)))
        assert e-FLOOR >= bound-1e-12
        cutoff.append(dict(g=g, cutoff=cut, scaled_payload=cut*np.sqrt(g),
                           ground_excess=e-FLOOR, exact_lower_bound=bound,
                           excess_over_g=(e-FLOOR)/g))
    adverse = []
    for g in [.08, .04, .02, .01]:
        cut = int(np.ceil(5/np.sqrt(g)))+2
        h, _, _ = reduced(g, cut, omit_offsets=True)
        e = float(eigh(h, subset_by_index=(0, 0), eigvals_only=True)[0])
        adverse.append(dict(g=g, ground_energy=e,
                            c2_estimate=(e-FLOOR-OMEGA*g/2)/g**2,
                            wrong_model_coefficient=23/128,
                            actual_model_coefficient=39/128))
    assert abs(adverse[-1]['c2_estimate']-23/128) < .001
    assert abs(adverse[-1]['c2_estimate']-39/128) > .1
    result = dict(status='personal_checks_pass_no_independent_audit',
                  symbolic=exact, independent_physical_matrices=comparisons,
                  physical_spectra=physical_spectra(), insufficient_cutoff=cutoff,
                  omitted_offsets_adverse=adverse,
                  limits=['Four-site global holonomy mode, not a bulk photon.',
                          'Finite large cutoffs are checks, not exact infinite matrices.',
                          'O(g^3) is established by the quasimode proof, not curve fitting.',
                          'No three-dimensional charged phase or axiom selection.'])
    out = json.dumps(result, indent=2)
    (HERE/'block19_charged_ring_check.json').write_text(out+'\n')
    print(out)


if __name__ == '__main__':main()
