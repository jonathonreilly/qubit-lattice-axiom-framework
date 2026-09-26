#!/usr/bin/env python3
"""Independent exact algebra and finite initial-current controls; no author imports."""
from __future__ import annotations
import hashlib
import itertools
import json
from pathlib import Path
import platform
import time
import numpy as np
import sympy as s

HERE = Path(__file__).resolve().parent
R = s.Rational
GAMMA, K0 = R(2, 3), R(5, 2)
axes = list(s.eye(3).columnspace())
zero = s.zeros(3, 1)
es, bs, labels = [], [], []
for i in range(3):
    for sign in (1, -1):
        es.append(sign * axes[i]); bs.append(zero.copy())
        labels.append(f"A{i + 1}{'+' if sign > 0 else '-'}")
for b in itertools.product((-1, 1), repeat=3):
    es.append(zero.copy()); bs.append(s.Matrix(b)); labels.append(f"B{b}")
e, b = s.Matrix.hstack(*es).T, s.Matrix.hstack(*bs).T
pairs = [(0, 1), (0, 2), (1, 2)]
feature_names = ["D1", "D2", "D3", "X1", "X2", "X3", "Y1", "Y2", "Y3", "Z12", "Z13", "Z23", "w"]
T = s.Matrix([[1] * 14] +
    [[es[a][i] ** 2 for a in range(14)] for i in range(3)] +
    [[es[a][i] for a in range(14)] for i in range(3)] +
    [[bs[a][i] for a in range(14)] for i in range(3)] +
    [[bs[a][i] * bs[a][j] for a in range(14)] for i, j in pairs] +
    [[bs[a][0] * bs[a][1] * bs[a][2] for a in range(14)]])
Ti = T.inv()
Btan = s.Matrix.vstack(s.eye(13), -s.ones(1, 13))

def zero_matrix(m):
    return all(s.expand(v) == 0 for v in m)

def kernel(n):
    return s.Matrix(14, 14, lambda a, c: n.dot(es[a].cross(bs[c]) + es[c].cross(bs[a])))

def flux(p, gamma=GAMMA):
    X, Y = e.T * p, b.T * p
    return s.Matrix.vstack(*[(gamma * p[a] * (es[a].cross(Y) + X.cross(bs[a]) - 2 * X.cross(Y))).T for a in range(14)])

def ambient_jac(p, n, gamma=GAMMA):
    K = kernel(n); v = K * p; M = (p.T * v)[0]
    return gamma * (s.diag(*[v[i] - M for i in range(14)]) + s.diag(*p) * K - 2 * p * v.T)

def moment_jac(p, n, gamma=GAMMA):
    return T[1:, :] * ambient_jac(p, n, gamma) * Ti[:, 1:]

def crossmat(n):
    return s.Matrix([[0, -n[2], n[1]], [n[2], 0, -n[0]], [-n[1], n[0], 0]])

def rest(D, Z=(0, 0, 0), w=0):
    return Ti * s.Matrix([1, *D, 0, 0, 0, 0, 0, 0, *Z, w])

def current(pl, pu, pw, pr, n, gamma=GAMMA, k0=K0):
    S = gamma * kernel(n) / 2
    sv = S * (pl + pr)
    muu, muw = (pu.T * sv)[0], (pw.T * sv)[0]
    return k0 * (pu - pw) / 2 + ((pu + pw).multiply_elementwise(sv) - pu * muw - pw * muu) / 4

def main():
    started = time.time()
    out = {"label_order": labels, "moment_order": feature_names,
           "versions": {"python": platform.python_version(), "numpy": np.__version__, "sympy": s.__version__},
           "scope": "Independently assembled algebra/current controls. No author checker, result, simulation, or finite-time hydrodynamic argument used."}
    assert T.det() != 0 and T * Ti == s.eye(14)
    m = s.Matrix(s.symbols("m0:13")); p_inverse = Ti * s.Matrix([1, *m])
    for i in range(3):
        assert p_inverse[2*i] == (m[i] + m[3+i]) / 2
        assert p_inverse[2*i+1] == (m[i] - m[3+i]) / 2
    for a in range(6, 14):
        expected = (1 - sum(m[:3]) + sum(bs[a][i] * m[6+i] for i in range(3)) +
                    sum(bs[a][i] * bs[a][j] * m[9+k] for k, (i, j) in enumerate(pairs)) +
                    s.prod(bs[a]) * m[12]) / 8
        assert s.expand(p_inverse[a] - expected) == 0
    p = s.Matrix(s.symbols("p0:14"))
    X, Y = e.T * p, b.T * p
    D = [sum(p[a] * es[a][i] ** 2 for a in range(14)) for i in range(3)]
    Z = [sum(p[a] * bs[a][i] * bs[a][j] for a in range(14)) for i, j in pairs]
    w = sum(p[a] * s.prod(bs[a]) for a in range(14))
    MB = b.T * s.diag(*p) * b
    XY = X.cross(Y)
    rows = [GAMMA * (X[i] * axes[i].cross(Y) - 2 * D[i] * XY) for i in range(3)]
    rows += [GAMMA * (D[i] * axes[i].cross(Y) - 2 * X[i] * XY) for i in range(3)]
    rows += [GAMMA * (X.cross(MB * axes[i]) - 2 * Y[i] * XY) for i in range(3)]
    for z, (i, j) in zip(Z, pairs):
        k = next(k for k in range(3) if k not in (i, j))
        rows.append(GAMMA * (X.cross(Y[j] * axes[i] + Y[i] * axes[j] + w * axes[k]) - 2 * z * XY))
    rows.append(GAMMA * (X.cross(s.Matrix([Z[2], Z[1], Z[0]])) - 2 * w * XY))
    assert zero_matrix(T[1:, :] * flux(p) - s.Matrix.vstack(*[v.T for v in rows]))
    # Mass one matters in the species-total identity.
    p0 = s.Matrix([R(i, 105) for i in range(1, 15)])
    assert zero_matrix(s.ones(1, 14) * flux(p0))
    out["moment_algebra"] = {"feature_matrix_determinant": str(T.det()), "symbolic_component_identities": 39,
                             "inverse": "Exact 14-label Walsh/axis inverse verified", "mass_total_flux": [0, 0, 0]}

    # Tangent entropy Hessian and explicit entropy-flux derivative, including a false-control.
    n = s.Matrix([1, 2, -1]); K = kernel(n); v = K * p0; M = (p0.T * v)[0]
    A = ambient_jac(p0, n); Hr = Btan.T * s.diag(*[1/x for x in p0]) * Btan
    Ar = A[:13, :] * Btan
    assert A * Btan == Btan * Ar
    assert zero_matrix(Hr * Ar - Ar.T * Hr)
    z = s.eye(14)[:, 0] - s.eye(14)[:, 7]
    logp = p0.applyfunc(s.log); eta = (p0.T * logp)[0]
    target = ((logp + s.ones(14, 1)).T * A * z)[0]
    dq = GAMMA * (((logp + s.ones(14, 1)).multiply_elementwise(v - M * s.ones(14, 1)) +
                    K * p0.multiply_elementwise(logp) - (2 * eta + 1) * v).T * z)[0]
    assert s.expand(dq - target) == 0
    omitted_term_error = s.expand(GAMMA * (v.T * z)[0])
    assert omitted_term_error != 0
    out["entropy"] = {"tangent_dimension": 13, "symmetrizer_symmetry_exact": True,
        "positive_metric_reason": "B^T diag(1/p) B, B full rank and p positive",
        "direction": list(n), "entropy_derivative_residual": "0",
        "omitting_minus_M_over_2_derivative_error": str(omitted_term_error)}

    # Rest optics, complete thirteen-field Jacobian, and weighted-divergence countercontrol.
    anis = rest([R(1, 5), R(1, 6), R(1, 7)], [R(1, 50), -R(1, 70), R(1, 40)], R(1, 100))
    assert min(anis) > 0
    optrows = []
    for direction in [*axes, s.Matrix([1, 2, 2]) / 3]:
        Am = moment_jac(anis, direction)
        Dmat = s.diag(*list((T * anis)[1:4])); MB = b.T * s.diag(*anis) * b
        expected6 = s.BlockMatrix([[s.zeros(3), -GAMMA * Dmat * crossmat(direction)],
                                  [GAMMA * MB * crossmat(direction), s.zeros(3)]]).as_explicit()
        assert Am[3:9, 3:9] == expected6
        assert zero_matrix(Am[3:9, :3]) and zero_matrix(Am[3:9, 9:])
        H6 = s.diag(*[1 / Dmat[i, i] for i in range(3)]).row_join(s.zeros(3))
        H6 = H6.col_join(s.zeros(3).row_join(MB.inv()))
        assert zero_matrix(H6 * expected6 - expected6.T * H6)
        assert Am.rank() == 4
        optrows.append({"direction": [str(x) for x in direction], "full_jacobian_rank": Am.rank(),
                        "closed_vector_block": True})
    gamma = s.symbols("gamma", nonzero=True, real=True)
    d2, d3, rb, z23 = s.symbols("d2 d3 rb z23", positive=True)
    square = gamma**2 * s.Matrix([[d2 * rb, -d2 * z23], [-d3 * z23, d3 * rb]])
    disc = s.expand(square.trace() ** 2 - 4 * square.det())
    assert s.factor(disc - gamma**4 * (rb**2 * (d2-d3)**2 + 4*d2*d3*z23**2)) == 0
    specific = rest([R(1, 7)] * 3, [0, 0, R(1, 14)])
    speeds = []
    for direction in axes:
        A6 = moment_jac(specific, direction, 1)[3:9, 3:9]
        ev = (A6**2).eigenvals()
        speeds.append({str(k): val for k, val in ev.items()})
    assert speeds[0] == {R(1, 14).__str__(): 2, R(9, 98).__str__(): 2, "0": 2}
    assert speeds[1] == {R(4, 49).__str__(): 4, "0": 2} and speeds[2] == speeds[1]
    w0 = rest([R(1, 7)] * 3); w1 = rest([R(1, 7)] * 3, w=R(1, 14))
    assert min(w1) > 0
    assert moment_jac(w0, axes[0])[3:9, 3:9] == moment_jac(w1, axes[0])[3:9, 3:9]
    assert moment_jac(w0, axes[0]) != moment_jac(w1, axes[0])
    rot = s.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, -1]])
    assert rot.det() == 1
    assert s.prod(rot * bs[6]) == -s.prod(bs[6])
    assert zero_matrix(moment_jac(w1, axes[0], 0))
    nn, yy = s.Matrix([1, 1, 0]), axes[2]
    drift = s.diag(R(1, 5), R(1, 6), R(1, 7)) * nn.cross(yy)
    assert nn.dot(drift) == R(1, 30)
    assert nn.dot(s.diag(5, 6, 7) * drift) == 0
    out["rest_optics"] = {"general_rest_tests": optrows, "axis_specific_squared_speeds_gamma_1": speeds,
        "axis_discriminant": str(disc), "w_changes_full_jacobian_not_vector_block": True,
        "proper_rotation_flips_w": True, "gamma_zero_all_modes_static": True,
        "unweighted_divergence_countercontrol": "1/30", "weighted_divergence_countercontrol": "0"}

    # Four independent nonidentical integer-weight laws; enumerate all 14^4 quadruples.
    weights = [list(range(1, 15)), list(range(14, 0, -1)),
               [2 + (5*a) % 17 for a in range(14)], [3 + (7*a) % 19 for a in range(14)]]
    laws = [s.Matrix([R(x, sum(wt)) for x in wt]) for wt in weights]
    enumeration = []
    directions = [v for i in range(3) for v in (axes[i], -axes[i]) if v != axes[0]]
    for direction in directions:
        Ki = [[int(v) for v in row] for row in kernel(direction).tolist()]
        accum = [0] * 14; hmin, hmax = 99, -99
        for l, a, c, r in itertools.product(range(14), repeat=4):
            hk = Ki[l][a] + Ki[a][r] - Ki[l][c] - Ki[c][r]
            hmin, hmax = min(hmin, hk), max(hmax, hk)
            weight = weights[0][l] * weights[1][a] * weights[2][c] * weights[3][r] * (15 + hk)
            accum[a] += weight; accum[c] -= weight
        denominator = 12 * s.prod(sum(wt) for wt in weights)
        brute = s.Matrix([R(x, denominator) for x in accum])
        exact = current(*laws, direction)
        assert brute == exact and sum(brute) == 0
        assert current(p0, p0, p0, p0, direction) == flux(p0) * direction / 2
        enumeration.append({"direction": list(direction), "quadruples": 14**4, "h_over_gamma_half_range": [hmin, hmax],
                            "current": [str(x) for x in brute]})
    # First stencil correction from a linear local profile, checked as a polynomial in h.
    h = s.symbols("h"); z = (s.eye(14)[:, 2] - s.eye(14)[:, 11]) / 19
    direction = -axes[1]
    Jh = current(p0-h*z, p0, p0+h*z, p0+2*h*z, direction)
    derivative = Jh.diff(h).subs(h, 0)
    expected = ambient_jac(p0, direction) * z / 4 - K0 * z / 2
    assert derivative == expected
    route_tensor = sum(((delta - axes[0]) * delta.T for delta in directions), s.zeros(3)) / 2
    second_tensor = sum(((delta - axes[0]) * (delta - axes[0]).T for delta in directions), s.zeros(3))
    assert route_tensor == s.eye(3) and second_tensor == s.diag(8, 2, 2)
    out["four_context_enumeration"] = enumeration
    out["initial_taylor_exact"] = {"current_first_derivative_identity": "d_h J|0 = DF_delta(p)z/4 - k0*z/2",
        "tensor_half_sum_a_delta": route_tensor.tolist(), "sum_a_a_transpose": second_tensor.tolist(),
        "gamma_zero_fourier_symbol": "k0 sum_nonfixed_delta [cos(Q.a_delta/N)-1]",
        "gamma_zero_diffusive_limit_N2": "-k0*(4 Q1^2 + Q2^2 + Q3^2)"}

    # A fixed positive C-infinity profile, analytic spatial derivatives, independent finite differences.
    en, bn = np.asarray(e, float), np.asarray(b, float)
    Kn = [np.asarray(kernel(axes[i]), float) for i in range(3)]
    direction_arrays = [np.asarray(x, float).ravel() for x in directions]
    profile_features = [en[:, 0], bn[:, 1], en[:, 1], bn[:, 0]*bn[:, 2], np.sum(en**2, axis=1)-3/7]
    specs = [(.20, (1,0,0), False), (.15, (1,0,1), True), (.10, (0,1,0), False),
             (.07, (0,0,1), True), (.10, (1,-1,0), False)]
    def profile(x):
        pval = np.ones(14); dp = np.zeros((14, 3))
        for f, (amp, kval, cosine) in zip(profile_features, specs):
            kv = np.array(kval); phase = 2*np.pi*np.dot(kv, x)
            value, deriv = (np.cos(phase), -np.sin(phase)) if cosine else (np.sin(phase), np.cos(phase))
            pval += amp*f*value
            dp += amp*np.outer(f, 2*np.pi*kv)*deriv
        return pval/14, dp/14
    def jf(x, delta, N):
        a = delta - np.array([1., 0., 0.]); step = a/N
        pl, pu, pw, pr = [profile(x + k*step)[0] for k in (-1, 0, 1, 2)]
        S = float(GAMMA)/2*sum(delta[i]*Kn[i] for i in range(3)); sv = S@(pl+pr)
        return float(K0)/2*(pu-pw)+((pu+pw)*sv-pu*np.dot(pw,sv)-pw*np.dot(pu,sv))/4
    points = [np.array(x, float)/8 for x in [(0,0,0),(2,1,3),(4,2,2),(3,3,2)]]
    seq = []
    for N in (8,16,32,64,128,256):
        resids = []; scaled = []
        for x in points:
            assert int(round(N*sum(x))) % 2 == 0
            pv, dp = profile(x)
            assert min(pv) > 0 and abs(sum(pv)-1) < 2e-15
            div = np.zeros(14)
            for i in range(3):
                v = Kn[i]@pv; M = pv@v
                Ai = float(GAMMA)*(np.diag(v-M)+np.diag(pv)@Kn[i]-2*np.outer(pv,v))
                div += Ai@dp[:,i]
            drift = np.zeros(14)
            for delta in direction_arrays:
                a = delta - np.array([1.,0.,0.])
                drift += jf(x-a/N,delta,N)-jf(x,delta,N)
            resids.append(float(np.linalg.norm(N*drift+div)))
            scaled.append(float(np.linalg.norm(N*drift)))
        seq.append({"N": N, "max_residual_four_points": max(resids), "N_times_max_residual": N*max(resids),
                    "max_scaled_drift": max(scaled), "per_point_residuals": resids})
    assert seq[-1]["max_residual_four_points"] < seq[0]["max_residual_four_points"]/15
    assert max(row["N_times_max_residual"] for row in seq) < 50
    out["profile_control"] = {"fixed_black_points_denominator_8": [list(x) for x in points],
        "profile_formula": "(1 + .20 e1 sin(2pi x1) + .15 b2 cos(2pi(x1+x3)) + .10 e2 sin(2pi x2) + .07 b1b3 cos(2pi x3) + .10(1_A-3/7)sin(2pi(x1-x2)))/14",
        "all_space_positive_lower_bound": (1-.20-.15-.10-.07-.10*4/7)/14,
        "scope": "Four selected black anchors; numerical corroboration, not uniform-profile proof", "rows": seq}
    out["elapsed_seconds"] = time.time()-started
    out["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    def encode(x):
        if isinstance(x, s.Integer): return int(x)
        if isinstance(x, s.Basic): return str(x)
        if isinstance(x, np.generic): return x.item()
        raise TypeError(type(x).__name__)
    result = HERE/"INDEPENDENT_RESULTS.json"
    with result.open("x") as f: json.dump(out, f, indent=2, default=encode); f.write("\n")
    print(json.dumps({"status":"passed", "groups":list(out.keys()), "elapsed_seconds":out["elapsed_seconds"]}, default=encode))

if __name__ == "__main__": main()
