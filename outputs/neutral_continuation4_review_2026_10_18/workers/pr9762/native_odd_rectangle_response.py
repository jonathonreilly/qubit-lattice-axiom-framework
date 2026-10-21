import sys as _sys
if _sys.flags.optimize: raise RuntimeError("Optimized Python disables scientific helper assertions")
_sys.stdout.reconfigure(line_buffering=True)
_sys.stderr.reconfigure(line_buffering=True)
_groups=set(); _calls=0
def _check(label, condition):
 global _calls
 _calls+=1
 if not bool(condition):
  print('[FAIL]',label,flush=True)
  print(f'TOTAL: PASS={len(_groups)} FAIL=1',flush=True)
  raise AssertionError(label)
 if label not in _groups:
  _groups.add(label);print('[PASS]',label,flush=True)
"""Source-exposed column model controls; no native 80/120-spin diagonalization."""
from pathlib import Path
import numpy as np, json
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import eigsh
from fractions import Fraction as F

def model(Nx, Ny):
    N = Nx * Ny
    idx = lambda x, y: x % Nx * Ny + y % Ny
    rows = [sum((1 << idx(x, y) for y in range(Ny))) for x in range(Nx)]
    cols = [sum((1 << idx(x, y) for x in range(Nx))) for y in range(Ny)]

    def mul(a, b):
        x, z, p = a
        y, w, q = b
        return (x ^ y, z ^ w, p * q * (-1) ** (z & y).bit_count())
    gens = [(rows[0], 0, 1)] + [(rows[0] ^ rows[x], 0, 1) for x in range(1, Nx)] + [(cols[0] ^ cols[y], cols[0] ^ cols[y], 1) for y in range(1, Ny)]
    piv = {}
    zs = []
    for g in gens:
        while g[0]:
            b = g[0].bit_length() - 1
            if b in piv:
                g = mul(piv[b], g)
            else:
                piv[b] = g
                break
        else:
            zs.append((g[1], int(g[2] == -1)))
    rr = {}
    for mask, rhs in zs + [(1 << b, 0) for b in piv]:
        while mask:
            b = mask.bit_length() - 1
            if b in rr:
                mask ^= rr[b][0]
                rhs ^= rr[b][1]
            else:
                rr[b] = (mask, rhs)
                break
        else:
            _check('P9762:native_odd_rectangle_response:C001', rhs == 0)
    free = [i for i in range(N) if i not in rr]

    def solve(v):
        s = sum(((v >> j & 1) << b for j, b in enumerate(free)))
        for b in sorted(rr):
            mask, rhs = rr[b]
            if (s & mask).bit_count() & 1 ^ rhs:
                s ^= 1 << b
        return s
    basis = [solve(i) for i in range(1 << len(free))]
    D = len(basis)

    def reduce(s):
        phase = 1
        for b in sorted(piv, reverse=True):
            if s >> b & 1:
                x, z, p = piv[b]
                phase *= p * (-1) ** (s & z).bit_count()
                s ^= x
        return (sum(((s >> b & 1) << j for j, b in enumerate(free))), phase)
    Hx = []
    Hy = []
    P = []
    for x in range(Nx):
        for y in range(Ny):
            m = 1 << idx(x, y) | 1 << idx(x + 1, y)
            Hx.append((m, 0, -1))
            m = 1 << idx(x, y) | 1 << idx(x, y + 1)
            Hy.append((m, m, 1))
            m = sum((1 << idx(x + i, y + j) for i, j in [(0, 0), (1, 0), (0, 1), (1, 1)]))
            P.append((0, m, -1))

    def matrix(terms):
        rr = []
        cc = []
        vv = []
        for col, s in enumerate(basis):
            for x, z, p in terms:
                row, phase = reduce(s ^ x)
                rr.append(row)
                cc.append(col)
                vv.append(p * (-1) ** (s & z).bit_count() * phase)
        A = coo_matrix((vv, (rr, cc)), shape=(D, D)).tocsr()
        _check('P9762:native_odd_rectangle_response:C002', (A - A.T).nnz == 0)
        return A
    for term in Hx + Hy + P:
        for gen in gens:
            _check('P9762:native_odd_rectangle_response:C003', ((term[0] & gen[1]).bit_count() + (term[1] & gen[0]).bit_count()) % 2 == 0)
    X, Y, Z = map(matrix, [Hx, Hy, P])
    return (X, Y, Z, D)

def source_coefficients():
    L = 5
    p = {0: F(1)}
    d = {0: F(0)}
    for S in range(1, 1 << L):
        val = sum((p[S ^ 1 << j] for j in range(L) if S >> j & 1))
        der = sum((d[S ^ 1 << j] for j in range(L) if S >> j & 1))
        if S != (1 << L) - 1:
            w1 = sum(((S >> j ^ S >> j + 1) & 1 for j in range(L - 1)))
            w2 = sum(((S >> j ^ S >> j + 2) & 1 for j in range(L - 2)))
            den = 4 * w1
            der = der / den + val * 4 * w2 / den ** 2
            val /= den
        p[S] = val
        d[S] = der
    ratio = d[31] / p[31]
    K = F(0)
    Kp = F(0)
    for j in range(L):
        n1 = int(j > 0) + int(j < L - 1)
        n2 = int(j > 1) + int(j < L - 2)
        delta = 2 * n1
        kj = F(1, 2 * delta ** 3)
        K += kj
        Kp += 6 * F(n2, delta) * kj
    _check('P9762:native_odd_rectangle_response:C004', p[31] == F(1, 16) and ratio == F(9, 2) and (K == F(19, 128)) and (Kp / K == F(54, 19)))
    return dict(t=str(p[31]), t_log_source=str(ratio), K=str(K), K_log_source=str(Kp / K), rectangle_amplitude=str(F(3, 361) * (ratio - Kp / K)))

def open_path_coefficients():
    for n in range(2, 10):
        for c in [1, 2]:
            v = {0: F(1)}
            for S in range(1, 1 << n):
                a = sum((v[S ^ 1 << j] for j in range(n) if S >> j & 1))
                if S != (1 << n) - 1:
                    w = sum(((S >> j ^ S >> j + 1) & 1 for j in range(n - 1)))
                    a /= 2 * c * w
                v[S] = a
            _check('P9762:native_odd_rectangle_response:C005', v[(1 << n) - 1] == F(1, c ** (n - 1)))
    t = F(1, 16)
    K = F(19, 128)
    a = F(5, 2) * t ** 3 / K ** 2
    b = 4 * t * t / K
    _check('P9762:native_odd_rectangle_response:C006', a == F(10, 361) and b == F(2, 19) and (a * F(63, 38) == F(315, 6859)))
    _check('P9762:native_odd_rectangle_response:C007', 2 * F(189, 13718) ** 2 / F(3, 19) == F(11907, 4952198))
    return dict(open_row=str(a), open_column=str(b), open_source=str(a * F(63, 38)), periodic_line_static=str(F(11907, 4952198)))

def main():
    result = dict(status='bounded-support', coefficients=source_coefficients(), open_coefficients=open_path_coefficients(), square=[], rectangle=[], scope='Exact coefficient/source arithmetic and column-model spectral controls, not native80/120-site diagonalization or observational tests')
    for Nx, Ny, label, ts in [(4, 4, 'square', [0.1, 0.05, 0.02, 0.01, 0.005]), (4, 6, 'rectangle', [0.2, 0.1, 0.05, 0.02, 0.01])]:
        X, Y, Z, D = model(Nx, Ny)
        _check('P9762:native_odd_rectangle_response:C008', D == (512 if label == 'square' else 32768))
        for t in ts:
            H = Z + t * (X + Y)
            E, V = eigsh(H, k=2, which='SA', tol=1e-13, ncv=28, v0=np.random.default_rng(1752).normal(size=D))
            order = np.argsort(E)
            E = E[order]
            V = V[:, order]
            g = V[:, 0]
            v = V[:, 1]
            if label == 'square':
                tau = t * t / 2
                gap_pred = 8 * np.sqrt(2) * tau
                source = t * (X - Y)
                weight_pred = 128 * tau * tau
            else:
                a = 3 * t ** 3 / 4
                b = 3 * t * t
                gap_pred = 2 * np.hypot(a, b)
                source = 4.5 * t * (X + Y) + 54 / 19 * Z
                weight_pred = (a * b * (63 / 38) / np.hypot(a, b)) ** 2
            weight = float((v @ (source @ g)) ** 2)
            res = float(max(np.linalg.norm(H @ g - E[0] * g), np.linalg.norm(H @ v - E[1] * v)))
            _check('P9762:native_odd_rectangle_response:C009', res < 1e-09)
            row = dict(t=t, dim=D, gap=float(E[1] - E[0]), gap_ratio=float((E[1] - E[0]) / gap_pred), source_weight=weight, weight_ratio=float(weight / weight_pred), plaquette_weight=float((v @ (Z @ g)) ** 2), residual=res)
            _check('P9762:native_odd_rectangle_response:C010', row['gap'] > 0 and np.isfinite(list(row.values())).all())
            if label == 'square':
                _check('P9762:native_odd_rectangle_response:C011', row['plaquette_weight'] < 1e-16)
            result[label].append(row)
        _check('P9762:native_odd_rectangle_response:C012', [r['t'] for r in result[label]] == ts and len(result[label]) == 5)
        _check('P9762:native_odd_rectangle_response:C013', abs(result[label][-1]['gap_ratio'] - 1) < 0.001 and abs(result[label][-1]['weight_ratio'] - 1) < 0.002)
    p = Path(__file__).resolve().parents[1] / 'outputs/native_odd_rectangle_response/result.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result))
if __name__ == '__main__':
    main()

print('Assertion evaluations:',_calls,'; PASS counts distinct primary assertion groups; helper assertions are additional uncounted checks.',flush=True)
from pathlib import Path as _Path
import json as _json
(_Path(__file__).resolve().parents[1]/'assertion-groups.json').write_text(_json.dumps({'groups':sorted(_groups),'evaluations':_calls})+'\n')
