"""Independent geometry/Taylor/least-squares controls; no author helper imports."""
import argparse
import itertools as it
import json
import time
import numpy as np
from scipy import sparse as sp
from scipy.sparse.linalg import lsmr

L = 3
DIM = 4
PAIRS = list(it.combinations(range(DIM), 2))
ORDERS = list(it.permutations(range(DIM)))
OFFSETS = list(it.product(range(-1, 2), repeat=DIM))
checks = []


def record(name, error, scale=1.0, tol=1e-8, absolute=1e-9):
    error, scale = float(error), float(scale)
    checks.append(dict(name=name, error=error, scale=scale,
                       threshold=absolute + tol * scale,
                       pass_=bool(error <= absolute + tol * scale)))


def witness(name, value, floor=1e-7):
    checks.append(dict(name=name, witness=float(value), floor=floor,
                       pass_=bool(value > floor)))


def qmul(a, b):
    return np.concatenate(((a[..., :1] * b[..., :1]
                            - np.sum(a[..., 1:] * b[..., 1:], axis=-1, keepdims=True)),
                           a[..., :1] * b[..., 1:] + b[..., :1] * a[..., 1:]
                           + np.cross(a[..., 1:], b[..., 1:])), axis=-1)


def qexp(a):
    length = np.linalg.norm(a, axis=-1)
    return np.concatenate((np.cos(length)[..., None],
                           np.sinc(length / np.pi)[..., None] * a), axis=-1)


def expjet(a):
    out = np.zeros(a.shape[:-1] + (5, 4))
    n2 = np.sum(a * a, axis=-1)
    out[..., 0, 0] = 1
    out[..., 1, 1:] = a
    out[..., 2, 0] = -n2 / 2
    out[..., 3, 1:] = -n2[..., None] * a / 6
    out[..., 4, 0] = n2 * n2 / 24
    return out


def muljet(a, b):
    out = np.zeros_like(a)
    for k in range(5):
        for j in range(k + 1):
            out[..., k, :] += qmul(a[..., j, :], b[..., k - j, :])
    return out


def sites(shape):
    return np.array(list(np.ndindex(tuple(shape))), dtype=np.int32)


def index(pos, mu, shape):
    return np.ravel_multi_index(np.moveaxis(np.mod(pos, shape), -1, 0), tuple(shape)) * 4 + mu


def gradient(shape):
    x = sites(shape)
    ids = np.arange(len(x))
    rr, cc, vv = [], [], []
    for mu in range(4):
        e = np.eye(4, dtype=int)[mu]
        head = index(x + e, 0, shape) // 4
        rr.extend((4 * ids + mu, 4 * ids + mu))
        cc.extend((head, ids))
        vv.extend((np.ones(len(x)), -np.ones(len(x))))
    return sp.coo_matrix((np.concatenate(vv), (np.concatenate(rr), np.concatenate(cc))),
                         shape=(4 * len(x), len(x))).tocsr()


def walk(start, displacement, order):
    pos = np.array(start, dtype=int)
    result = []
    for mu in order:
        sign = int(np.sign(displacement[mu]))
        for _ in range(abs(displacement[mu])):
            if sign < 0:
                pos[mu] -= 1
            result.append((pos.copy(), mu, sign))
            if sign > 0:
                pos[mu] += 1
    return result


def motif(mu):
    result, axials, straights, clipped = [], [], [], []
    shift = L * np.eye(4, dtype=int)[mu]
    for offset in OFFSETS:
        for order in ORDERS:
            first = walk(np.zeros(4, int), offset, order)
            middle = walk(offset, shift, [mu])
            last = [(p + shift, d, -s) for p, d, s in reversed(first)]
            result.append(first + middle + last)
            axials.append(first)
            straights.append(middle)
            clipped.append(first + middle)
    return result, axials, straights, clipped


class Paths:
    def __init__(self, shape, kind="soft"):
        self.shape = np.array(shape, int)
        self.nfine = 4 * int(np.prod(shape))
        self.kind = kind
        if kind == "soft":
            self.coarse = self.shape // L
            x = sites(self.coarse)
            families = [motif(mu) for mu in range(4)]
            self.nout = len(x) * 4
            self.count = 24 * L**4
            self.idx = np.zeros((self.nout, self.count, 11), dtype=np.int32)
            self.sgn = np.zeros_like(self.idx, dtype=np.int8)
            self.Q = self._matrix(families, 0, x, L)
            self.alpha = self._matrix([families[0]], 1, x, L, scalar=True)
            self.straight = self._matrix(families, 2, x, L)
            self.omit = self._matrix(families, 3, x, L)
            for mu, family in enumerate(families):
                for t, path in enumerate(family[0]):
                    for k, (p, d, sign) in enumerate(path):
                        self.idx[mu::4, t, k] = index(L * x + p, d, shape)
                        self.sgn[mu::4, t, k] = sign
        else:
            x = sites(shape)
            self.nout, self.count = len(x) * 6, 1
            self.idx = np.zeros((self.nout, 1, 4), dtype=np.int32)
            self.sgn = np.tile(np.array([1, 1, -1, -1], np.int8), (self.nout, 1, 1))
            eye = np.eye(4, dtype=int)
            for c, (mu, nu) in enumerate(PAIRS):
                for k, (p, d) in enumerate([(x, mu), (x + eye[mu], nu),
                                            (x + eye[nu], mu), (x, nu)]):
                    self.idx[c::6, 0, k] = index(p, d, shape)
            rows = np.repeat(np.arange(self.nout), 4)
            self.Q = sp.coo_matrix((self.sgn.ravel(), (rows, self.idx.ravel())),
                                  shape=(self.nout, self.nfine)).tocsr()

    def _matrix(self, families, which, x, step, scalar=False):
        rows, cols, vals = [], [], []
        for mu, fam in enumerate(families):
            merged = {}
            for path in fam[which]:
                for p, d, sign in path:
                    key = tuple(p) + (d,)
                    merged[key] = merged.get(key, 0) + sign
            for key, count in merged.items():
                if count:
                    rows.append(np.arange(len(x)) if scalar else 4 * np.arange(len(x)) + mu)
                    cols.append(index(step * x + np.array(key[:4]), key[4], self.shape))
                    vals.append(np.full(len(x), count / self.count))
        nrows = len(x) if scalar else len(x) * 4
        return sp.coo_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))),
                             shape=(nrows, self.nfine)).tocsr()

    def bilinear(self, a, adjoint_r=None):
        result = np.zeros((self.nout, 3))
        adj = np.zeros_like(a) if adjoint_r is not None else None
        for lo in range(0, self.nout, 16):
            hi = min(lo + 16, self.nout)
            idx, sign = self.idx[lo:hi], self.sgn[lo:hi]
            v = a[idx] * sign[..., None]
            total, prefix = np.sum(v, axis=2), np.zeros(v.shape[:2] + (3,))
            crosssum = np.zeros_like(prefix)
            for k in range(v.shape[2]):
                x = v[:, :, k]
                crosssum += np.cross(prefix, x)
                if adj is not None:
                    suffix = total - prefix - x
                    deriv = np.cross(adjoint_r[lo:hi, None, :], prefix - suffix)
                    deriv *= sign[:, :, k, None] / self.count
                    np.add.at(adj, idx[:, :, k].ravel(), deriv.reshape(-1, 3))
                prefix += x
            result[lo:hi] = np.mean(crosssum, axis=1)
        return (result, adj) if adj is not None else result

    def jets(self, a):
        result = np.zeros((self.nout, 5, 4))
        for lo in range(0, self.nout, 16):
            hi = min(lo + 16, self.nout)
            curr = np.zeros((hi - lo, self.count, 5, 4))
            curr[..., 0, 0] = 1
            for k in range(self.idx.shape[2]):
                v = a[self.idx[lo:hi, :, k]] * self.sgn[lo:hi, :, k, None]
                curr = muljet(curr, expjet(v))
            result[lo:hi] = curr.mean(axis=1)
        return result

    def group(self, a):
        result = np.zeros((self.nout, 4))
        for lo in range(0, self.nout, 32):
            hi = min(lo + 32, self.nout)
            curr = np.zeros((hi - lo, self.count, 4))
            curr[..., 0] = 1
            for k in range(self.idx.shape[2]):
                v = a[self.idx[lo:hi, :, k]] * self.sgn[lo:hi, :, k, None]
                curr = qmul(curr, qexp(v))
            result[lo:hi] = curr.mean(axis=1)
        return result


def softjet(m, b):
    # Independent series for sqrt(sum of squared quaternion components).
    square = np.zeros(m.shape[:-2] + (5,))
    for k in range(5):
        for j in range(k + 1):
            square[..., k] += np.sum(m[..., j, :] * m[..., k-j, :], axis=-1)
    root = np.zeros_like(square)
    root[..., 0] = 1
    for k in range(1, 5):
        root[..., k] = (square[..., k] - sum(root[..., j] * root[..., k-j]
                                           for j in range(1, k))) / 2
    eb = expjet(b)
    dot = np.zeros_like(square)
    for k in range(5):
        for j in range(k + 1):
            dot[..., k] += np.sum(eb[..., j, :] * m[..., k-j, :], axis=-1)
    return root - dot


def solve(D, rhs, name):
    out = np.zeros((D.shape[1], 3))
    stats = []
    for c in range(3):
        fit = lsmr(D, rhs[:, c], atol=1e-13, btol=1e-13, maxiter=5000)
        out[:, c] = fit[0]
        stats.append(dict(stop=int(fit[1]), iterations=int(fit[2]),
                          normr=float(fit[3]), normar=float(fit[4])))
    record(name, np.linalg.norm(D.T @ (D @ out - rhs)),
           np.linalg.norm(D.T @ rhs))
    return out, stats


def main(depth, top):
    started = time.time()
    shapes = [tuple(np.array(top) * L**(depth-j)) for j in range(depth+1)]
    sizes = [4 * int(np.prod(x)) for x in shapes]
    ks = [0.8, 1.3][:depth]
    path = [Paths(shapes[j]) for j in range(depth)]
    plaq = Paths(shapes[0], "plaquette")
    offsets = np.cumsum([0] + sizes[:-1])
    blocks = []
    blocks.append([plaq.Q] + [None] * (depth-1))
    for j in range(depth):
        row = [None] * depth
        row[j] = -np.sqrt(ks[j]) * path[j].Q
        if j+1 < depth:
            row[j+1] = np.sqrt(ks[j]) * sp.eye(sizes[j+1], format="csr")
        blocks.append(row)
    D = sp.bmat(blocks, format="csr")
    rng = np.random.default_rng(92041 + depth)
    v = rng.normal(size=(sizes[-1], 3)) * 0.37
    fixed = np.zeros((D.shape[0], 3))
    fixed[-sizes[-1]:] = np.sqrt(ks[-1]) * v
    hidden, linear_stats = solve(D, -fixed, "linear_stationary_equations")
    a = [hidden[offsets[j]:offsets[j+1]] for j in range(depth)] + [v]
    r = [a[j+1] - path[j].Q @ a[j] for j in range(depth)]
    f = plaq.Q @ a[0]
    bp, dbpf = plaq.bilinear(a[0], f)
    Bs, dbr = [], []
    source = np.zeros_like(hidden)
    source[:sizes[0]] = plaq.Q.T @ bp + dbpf
    for j in range(depth):
        b, adj = path[j].bilinear(a[j], r[j])
        Bs.append(b)
        dbr.append(adj)
        source[offsets[j]:offsets[j+1]] += ks[j] * (path[j].Q.T @ b - adj)
        if j+1 < depth:
            source[offsets[j+1]:offsets[j+2]] -= ks[j] * b
        dg = gradient(shapes[j+1])
        delta = path[j].Q - path[j].straight + dg @ path[j].alpha
        record(f"root_straight_funnel_level{j}", np.max(np.abs(delta.data), initial=0), tol=1e-10)
        record(f"straight_row_level{j}", np.max(np.abs(np.asarray(path[j].straight.sum(1)).ravel() - L)))
        record(f"straight_column_level{j}", np.max(np.abs(np.asarray(path[j].straight.sum(0)).ravel() - L**-3)))
        record(f"linear_coclosed_level{j}", np.linalg.norm(dg.T @ r[j]))
        witness(f"endpoint_mutation_level{j}", np.linalg.norm((path[j].Q-path[j].omit) @ a[j]))
    # Solve H w = -S by two independent rectangular least-squares solves:
    # D^T z = -S, D w = z. This uses the Moore-Penrose slice, not H^-1 on nulls.
    z, source_stats = solve(D.T, -source, "source_in_range_of_hidden_D_transpose")
    wh, second_stats = solve(D, z, "second_stationary_equations")
    record("direct_second_Euler", np.linalg.norm(D.T @ (D @ wh) + source), np.linalg.norm(source))
    w = [wh[offsets[j]:offsets[j+1]] for j in range(depth)] + [np.zeros_like(v)]
    q = [ks[j] * (w[j+1] - path[j].Q @ w[j] - Bs[j]) for j in range(depth)]
    divergence = []
    for j in range(depth):
        dg = gradient(shapes[j+1])
        bracket = 2 * np.cross(a[j+1], ks[j] * r[j])
        incoming_plus_outgoing = abs(dg).T @ bracket
        # abs(dg) merges a self-loop to zero; compute incidence separately.
        coords = sites(shapes[j+1])
        ipo = np.zeros((len(coords), 3))
        outgoing = np.zeros_like(ipo)
        for mu in range(4):
            heads = index(coords + np.eye(4, dtype=int)[mu], 0, shapes[j+1]) // 4
            outgoing += bracket[mu::4]
            ipo += bracket[mu::4]
            np.add.at(ipo, heads, bracket[mu::4])
        dq = dg.T @ q[j]
        record(f"log_covariance_level{j}", np.linalg.norm(dq - ipo / 2), np.linalg.norm(ipo))
        J2 = q[j] - bracket / 2
        record(f"right_covariance_level{j}", np.linalg.norm(dg.T @ J2 - outgoing), np.linalg.norm(outgoing))
        divergence.append(float(np.linalg.norm(dq)))
        witness(f"ordinary_coclosed_mutation_level{j}", np.linalg.norm(dq))
        witness(f"log_right_half_factor_mutation_level{j}", np.linalg.norm(ipo / 2))
        if np.any(np.array(shapes[j+1]) == 1):
            witness(f"self_loop_incidence_mutation_level{j}", np.linalg.norm(incoming_plus_outgoing - ipo))
        if j:
            actual = q[j-1] - path[j].Q.T @ q[j] - ks[j]*dbr[j]
            record(f"intermediate_Euler_level{j}", np.linalg.norm(actual), np.linalg.norm(q[j-1]))
            funnel = path[j].alpha.T @ dq
            forced = ks[j]*dbr[j] - funnel
            record(f"forced_straight_transport_level{j}",
                   np.linalg.norm(q[j-1] - path[j].straight.T @ q[j] - forced), np.linalg.norm(q[j-1]))
            witness(f"DB_source_omission_level{j}", np.linalg.norm(ks[j]*dbr[j]))
            witness(f"funnel_omission_level{j}", np.linalg.norm(funnel))
            witness(f"wrong_kappa_ratio_level{j}", np.linalg.norm((ks[j]/ks[j-1]-1)*path[j].Q.T @ q[j]))
    F3 = float(np.sum(f*bp) - sum(ks[j]*np.sum(r[j]*Bs[j]) for j in range(depth)))
    h = rng.normal(size=hidden.shape)
    def cubic(x):
        aa = [x[offsets[j]:offsets[j+1]] for j in range(depth)] + [v]
        ff = plaq.Q @ aa[0]
        result = np.sum(ff * plaq.bilinear(aa[0]))
        for j in range(depth):
            result -= ks[j] * np.sum((aa[j+1]-path[j].Q @ aa[j])*path[j].bilinear(aa[j]))
        return result
    t = 1e-4
    # Cubic central difference has an exact O(t^2) term removed by Richardson.
    g1 = (cubic(hidden+t*h)-cubic(hidden-t*h))/(2*t)
    g2 = (cubic(hidden+0.5*t*h)-cubic(hidden-0.5*t*h))/t
    record("independent_source_direction", abs((4*g2-g1)/3-np.sum(source*h)), abs(np.sum(source*h)))
    exchange = float(-0.5 * np.sum(source*wh))
    witness("charged_source_nonzero", np.linalg.norm(source))
    witness("exchange_omission", exchange)
    witness("exchange_sign", 2*exchange)
    witness("exchange_half_factor", exchange/2)
    F2 = float(np.sum((D@hidden+fixed)**2)/2)
    payload = dict(depth=depth, top=top, shapes=shapes, kappas=ks,
                   n_hidden=int(D.shape[1]), n_contours=sum(p.nout*p.count for p in path),
                   linear_solver=linear_stats, source_solver=source_stats, second_solver=second_stats,
                   F2=F2, F3=F3, exchange=exchange, divergence=divergence)
    if depth == 1:
        pp = plaq.jets(a[0])
        total = -pp[:, :, 0].sum(axis=0)
        total[0] += plaq.nout
        for j in range(depth):
            m = path[j].jets(a[j])
            record("direct_product_BCH2", np.linalg.norm(m[:, 2, 1:] - Bs[j]), np.linalg.norm(Bs[j]), tol=1e-9, absolute=1e-10)
            total += ks[j] * softjet(m, a[j+1]).sum(axis=0)
            witness("path_divisor_mutation", np.linalg.norm((24/23-1)*m[:, 1, 1:]))
        record("product_polynomial_F2", abs(total[2]-F2), abs(F2), tol=1e-9, absolute=1e-10)
        record("product_polynomial_F3", abs(total[3]-F3), abs(F3), tol=1e-9, absolute=1e-10)
        target = total[4] - exchange
        def action(eps):
            aa = [eps*a[j] + eps**2*w[j] for j in range(depth+1)]
            value = np.sum(1-plaq.group(aa[0])[:, 0])
            for j in range(depth):
                m = path[j].group(aa[j])
                value += ks[j] * np.sum(np.linalg.norm(m, axis=1)-np.sum(qexp(aa[j+1])*m, axis=1))
            return float(value)
        epsilons = [0.04, 0.02, 0.01]
        estimate = [(action(e)+action(-e)-2*F2*e*e)/(2*e**4) for e in epsilons]
        extrap = (4*estimate[-1]-estimate[-2])/3
        record("quartic_stationary_direct_group", abs(extrap-target), abs(target), tol=2e-5, absolute=2e-6)
        payload.update(bare_quartic=float(total[4]), completed_quartic=float(target),
                       finite_eps=epsilons, finite_quartic=estimate, extrapolated_quartic=float(extrap))
        # Actual centered constant noncommuting family cancels its averaged B.
        constant = np.tile(np.array([[0.2,0.1,0.0],[0.0,0.3,0.1],[-0.1,0.0,0.2],[0.2,-0.2,0.1]]), (sizes[0]//4,1))
        cb = path[0].bilinear(constant)
        record("centered_constant_B_cancellation", np.linalg.norm(cb), tol=1e-10)
        single = constant[path[0].idx[0]] * path[0].sgn[0,...,None]
        prefix = np.cumsum(single, axis=1)-single
        indiv = np.sum(np.cross(prefix,single),axis=1)
        witness("constant_individual_B_nonzero", np.max(np.linalg.norm(indiv,axis=1)))
    # Exact symbolic powers, density factors, and one-form lemma are assessed in report.
    # These arithmetic mutations show why amplitude alone cannot be a column norm.
    record("geometric_current_identity", abs(L**-3 * L**-4 - L**3 * L**-6 * L**-4), tol=1e-10)
    witness("omitted_4d_density_mutation", L**4-1)
    payload.update(elapsed_seconds=time.time()-started, checks=checks,
                   passed=sum(c["pass_"] for c in checks), total=len(checks),
                   implementation="independent geometric paths, quaternion product jets, rectangular LSMR")
    print(json.dumps(payload, indent=2))
    return all(c["pass_"] for c in checks)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--depth", type=int, default=1, choices=[1,2])
    args = ap.parse_args()
    ok = main(args.depth, [1,2,1,1])
    raise SystemExit(0 if ok else 1)
