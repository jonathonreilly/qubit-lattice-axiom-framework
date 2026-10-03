"""Coordinator check of A9 3.2(d): does a menu set by the site's OWN possibilities signal, while a menu set by a
RECORDED NEIGHBOUR does not?  Three qubits: x (forming site), y (x's neighbour), b (distant). b's menu choice c in {Z, X}
is the distant 'setting'. We compute the exact distribution of x's record content (a direction +-m) averaged over b's
outcome, for each c, and report the total-variation difference between c = Z and c = X.
 own rule  : x's menu axis = direction of x's own Bloch vector (conditional on everything already recorded).
 field rule: y records first with a fixed z menu; x's menu axis = direction of y's content (a recorded neighbour)."""
import numpy as np, itertools
rng = np.random.default_rng(5)
I2 = np.eye(2); X = np.array([[0,1],[1,0]],complex); Y = np.array([[0,-1j],[1j,0]]); Z = np.diag([1.,-1.]).astype(complex)
def op(o, k):     # qubit order (x, y, b)
    mats = [I2, I2, I2]; mats[k] = o
    return np.kron(np.kron(mats[0], mats[1]), mats[2])
def proj(axis, s, k):
    return 0.5 * (np.eye(8) + s * (axis[0]*op(X,k) + axis[1]*op(Y,k) + axis[2]*op(Z,k)))
def bloch(psi, k):
    return np.array([np.vdot(psi, op(P, k) @ psi).real for P in (X, Y, Z)])
def x_content_dist(psi, c, rule):
    axis_b = np.array([0,0,1.]) if c == "Z" else np.array([1.,0,0])
    dist = {}
    for sb in (1, -1):
        v = proj(axis_b, sb, 2) @ psi; pb = np.vdot(v, v).real
        if pb < 1e-14: continue
        v = v / np.sqrt(pb)
        branches = [(pb, v, None)]
        if rule == "field":           # y records first in a fixed z menu; x's menu = y's content
            new = []
            for (p, w, _) in branches:
                for sy in (1, -1):
                    u = proj(np.array([0,0,1.]), sy, 1) @ w; py = np.vdot(u, u).real
                    if py > 1e-14: new.append((p * py, u / np.sqrt(py), sy * np.array([0,0,1.])))
            branches = new
        for (p, w, ycont) in branches:
            if rule == "own":
                r = bloch(w, 0); nr = np.linalg.norm(r)
                m = r / nr if nr > 1e-12 else np.array([0,0,1.])
            else:
                m = ycont
            for sx in (1, -1):
                u = proj(m, sx, 0) @ w; px = np.vdot(u, u).real
                key = tuple(np.round(sx * m, 6))
                dist[key] = dist.get(key, 0.0) + p * px
    return dist
def tv(d1, d2):
    keys = set(d1) | set(d2)
    return 0.5 * sum(abs(d1.get(k, 0) - d2.get(k, 0)) for k in keys)
worst = {"own": 0.0, "field": 0.0}
for trial in range(400):
    psi = rng.normal(size=8) + 1j * rng.normal(size=8); psi /= np.linalg.norm(psi)
    if trial == 0:     # singlet between x and b, y in |0>
        psi = np.zeros(8, complex); psi[0b001] = 1/np.sqrt(2); psi[0b100] = -1/np.sqrt(2)
    for rule in ("own", "field"):
        d = tv(x_content_dist(psi, "Z", rule), x_content_dist(psi, "X", rule))
        worst[rule] = max(worst[rule], d)
        if trial == 0: print("x-b singlet: rule %-5s  TV(x's record content | b menu Z vs X) = %.4f" % (rule, d))
print("400 random 3-qubit states: max TV  own rule = %.4f   field rule (recorded-neighbour menu) = %.2e" % (worst["own"], worst["field"]))
