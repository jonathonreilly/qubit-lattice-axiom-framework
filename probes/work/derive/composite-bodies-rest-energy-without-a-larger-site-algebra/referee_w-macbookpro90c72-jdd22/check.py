#!/usr/bin/env python3
"""Independent referee for J:derive:composite-bodies-rest-energy-without-a-larger-site-algebra:a3.

Author w-jonathonsmac4f50-j8f94 (claude-opus-5-5). Referee w-macbookpro90c72-jdd22 (grok-4.6).
Own matrices and own quadrature. The author's check.py is not imported.
"""
import numpy as np
import sympy as sp
from scipy.sparse.linalg import expm_multiply

PASS = []


def record(tag, ok, text):
    PASS.append(bool(ok))
    print(f"{'PASS' if ok else 'FAIL'} {tag} {text}")


# ---------------------------------------------------------------- step 2: sector kinematics
K, q = sp.symbols("K q", real=True)
co = sp.simplify(sp.expand_trig(sp.sin(K / 2 + q) + sp.sin(K / 2 - q) - 2 * sp.sin(K / 2) * sp.cos(q)))
ct = sp.simplify(sp.expand_trig(sp.sin(K / 2 + q) - sp.sin(K / 2 - q) - 2 * sp.cos(K / 2) * sp.sin(q)))
kk = sp.symbols("k", real=True)
raw_D = sp.I / 2 * (sp.exp(-sp.I * kk) - sp.exp(sp.I * kk))
Dsym = sp.simplify(raw_D.rewrite(sp.sin) - sp.sin(kk))
record("S2", co == 0 and ct == 0 and Dsym == 0,
       "D has symbol sin k; co-moving kinetic energy is 2 sin(K/2) cos q; counter-moving is 2 cos(K/2) sin q")


# ---------------------------------------------------------------- step 3: residue lemma and contact dispersion
def lemma_quad(a, b, n=20001):
    t = np.linspace(0.0, 2 * np.pi, n)
    y = 1.0 / (a - 2 * b * np.cos(t))
    trap = np.trapezoid(y, t) / (2 * np.pi)
    return abs(trap - 1.0 / np.sqrt(a * a - 4 * b * b))


lem = max(lemma_quad(a, b) for a, b in ((3.0, 1.0), (5.0, -2.0), (2.5, 0.3), (7.0, -3.4), (4.0, -0.5)))
V, b = sp.symbols("V b", real=True)
ser_co = sp.series(V ** 2 + 4 * sp.sin(K / 2) ** 2, K, 0, 6).removeO()
ser_ct = sp.series(V ** 2 + 4 * sp.cos(K / 2) ** 2, K, 0, 4).removeO()
ser_ok = sp.simplify(ser_co - (V ** 2 + K ** 2 - K ** 4 / 12)) == 0
ser_ok = ser_ok and sp.simplify(ser_ct - (V ** 2 + 4 - K ** 2)) == 0
record("S3", lem < 1e-10 and ser_ok,
       f"residue lemma max trap error {lem:.1e}; co-moving E^2 = V^2 + K^2 - K^4/12; counter-moving E^2 = V^2 + 4 - K^2 at K=0")


def ring_contact(N, Vc, Kv, s1, s2):
    n = np.arange(N)
    k1 = 2 * np.pi * n / N
    eps = s1 * np.sin(k1) + s2 * np.sin(Kv - k1)
    return np.linalg.eigvalsh(np.diag(eps) + (Vc / N) * np.ones((N, N))).real


def pos_spectrum(N, Vc):
    """Position-space generator, basis (x1, x2, s1, s2), open periodic ring. Own index order."""
    dim = N * N * 4
    H = np.zeros((dim, dim), dtype=complex)
    sz = (1.0, -1.0)

    def idx(x1, x2, s1, s2):
        return ((x1 * N + x2) * 4 + s1 * 2 + s2)

    for x1 in range(N):
        for x2 in range(N):
            for s1 in range(2):
                for s2 in range(2):
                    i = idx(x1, x2, s1, s2)
                    for dx, amp in ((-1, 0.5j), (1, -0.5j)):
                        H[i, idx((x1 + dx) % N, x2, s1, s2)] += sz[s1] * amp
                        H[i, idx(x1, (x2 + dx) % N, s1, s2)] += sz[s2] * amp
                    if x1 == x2:
                        H[i, i] += Vc
    return np.linalg.eigvalsh(H).real


Npos, Vpos = 6, -0.8
full = np.sort(pos_spectrum(Npos, Vpos))
blocks = []
for m in range(Npos):
    Kv = 2 * np.pi * m / Npos
    for s1 in (1, -1):
        for s2 in (1, -1):
            blocks.append(ring_contact(Npos, Vpos, Kv, s1, s2))
blocks = np.sort(np.concatenate(blocks))
spec_err = np.max(np.abs(full - blocks))
form_err = 0.0
for m in range(0, 48):
    Kv = 2 * np.pi * m / 48
    e_co = ring_contact(48, -1.3, Kv, 1, 1)[0]
    e_ct = ring_contact(48, -1.3, Kv, 1, -1)[0]
    form_err = max(form_err,
                   abs(e_co + np.sqrt(1.3 ** 2 + 4 * np.sin(Kv / 2) ** 2)),
                   abs(e_ct + np.sqrt(1.3 ** 2 + 4 * np.cos(Kv / 2) ** 2)))
record("S4", spec_err < 1e-8 and form_err < 1e-8,
       f"6-ring position spectrum matches K-blocks to {spec_err:.1e}; 48-ring closed forms to {form_err:.1e}")


# ---------------------------------------------------------------- step 5: nearest neighbour, quadratic only
def ring_nn(N, Vn, Kv):
    n = np.arange(N)
    k1 = 2 * np.pi * n / N
    qq = k1 - Kv / 2
    eps = np.sin(k1) + np.sin(Kv - k1)  # co-moving
    U = (Vn / N) * 2 * np.cos(qq[:, None] - qq[None, :])
    ev = np.linalg.eigvalsh(np.diag(eps) + U).real
    return np.sort(ev)


bb, Ee, Vn = sp.symbols("b E V_n", real=True)
qv = sp.symbols("qv", real=True)
avg = lambda f: sp.integrate(f, (qv, 0, 2 * sp.pi)) / (2 * sp.pi)
ch_cos = sp.simplify(avg(2 * sp.cos(qv) ** 2 * (1 + 2 * bb * sp.cos(qv) / Ee + 4 * bb ** 2 * sp.cos(qv) ** 2 / Ee ** 2)) / Ee)
ch_sin = sp.simplify(avg(2 * sp.sin(qv) ** 2 * (1 + 2 * bb * sp.cos(qv) / Ee + 4 * bb ** 2 * sp.cos(qv) ** 2 / Ee ** 2)) / Ee)
ch_ok = sp.simplify(ch_cos - (1 + 3 * bb ** 2 / Ee ** 2) / Ee) == 0
ch_ok = ch_ok and sp.simplify(ch_sin - (1 + bb ** 2 / Ee ** 2) / Ee) == 0
curv_nn = []
for Vnv in (-0.7, -2.5):
    E0 = ring_nn(80, Vnv, 0.0)
    Kv = 2 * np.pi / 80
    E1 = ring_nn(80, Vnv, Kv)
    # two bound channels sit at Vn when K=0; curvature of E^2
    curv_nn.append([(E1[i] ** 2 - E0[i] ** 2) / Kv ** 2 for i in (0, 1)])
# O(K^4): compare E^2 with Vn^2 + 6 sin^2(K/2) at a moderate K
Kv_m = 1.2
Em = ring_nn(96, -1.5, Kv_m)
exactish = 1.5 ** 2 + 6 * np.sin(Kv_m / 2) ** 2
nn_deviation = abs(Em[0] ** 2 - exactish)
nn_ok = ch_ok and all(abs(c[0] - 1.5) < 0.02 and abs(c[1] - 0.5) < 0.02 for c in curv_nn)
record("S5", nn_ok,
       "channel conditions to O(b^2) give c^2 = 3/2 and 1/2; "
       + "; ".join(f"V_n curv {c[0]:.4f},{c[1]:.4f}" for c in curv_nn)
       + f"; at K=1.2, |E^2 - (V_n^2 + 6 sin^2(K/2))| = {nn_deviation:.4f} (not an all-K identity)")


# ---------------------------------------------------------------- step 6: 3D contact, own 4x4 inverses
SX = np.array([[0, 1], [1, 0]], complex)
SY = np.array([[0, -1j], [1j, 0]], complex)
SZ = np.array([[1, 0], [0, -1]], complex)
I2 = np.eye(2, dtype=complex)
SIG = (SX, SY, SZ)


def G3(E, K, N):
    k = 2 * np.pi * np.arange(N) / N
    grid = np.stack(np.meshgrid(k, k, k, indexing="ij"), axis=-1).reshape(-1, 3)
    h1 = np.sin(grid)
    h2 = np.sin(np.asarray(K, float) - grid)
    A = np.zeros((len(grid), 4, 4), dtype=complex)
    for a in range(3):
        A += h1[:, a, None, None] * np.kron(SIG[a], I2)
        A += h2[:, a, None, None] * np.kron(I2, SIG[a])
    M = E * np.eye(4) - A
    return np.linalg.inv(M).sum(axis=0) / len(grid)


def bound3(V, K, N):
    # most negative eigenvalue of G equals 1/V
    k = 2 * np.pi * np.arange(N) / N
    # continuum lower edge at this K: min over k of -|h(k)| - |h(K-k)|
    grid = np.stack(np.meshgrid(k, k, k, indexing="ij"), axis=-1).reshape(-1, 3)
    edge = (-np.linalg.norm(np.sin(grid), axis=1) - np.linalg.norm(np.sin(np.asarray(K, float) - grid), axis=1)).min()

    def f(E):
        return np.linalg.eigvalsh(G3(E, K, N)).real.min() - 1.0 / V

    lo, hi = -40.0, edge - 1e-6
    if f(lo) <= 0 or f(hi) >= 0:
        raise RuntimeError(f"bisection not bracketed at K={K}, f(lo)={f(lo)}, f(hi)={f(hi)}, edge={edge}")
    for _ in range(50):
        mid = 0.5 * (lo + hi)
        if f(mid) > 0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi), edge


def ed3_lowest(N, K, V):
    k = 2 * np.pi * np.arange(N) / N
    grid = np.stack(np.meshgrid(k, k, k, indexing="ij"), axis=-1).reshape(-1, 3)
    n = len(grid)
    H = np.zeros((4 * n, 4 * n), dtype=complex)
    for i, kv in enumerate(grid):
        A = np.zeros((4, 4), dtype=complex)
        h1, h2 = np.sin(kv), np.sin(np.asarray(K, float) - kv)
        for a in range(3):
            A += h1[a] * np.kron(SIG[a], I2) + h2[a] * np.kron(I2, SIG[a])
        H[4 * i:4 * i + 4, 4 * i:4 * i + 4] = A
    H += (V / n) * np.kron(np.ones((n, n)), np.eye(4))
    return np.linalg.eigvalsh(H).real[0]


ed_gap = []
for Kv in ((0.0, 0.0, 0.0), (np.pi / 2, 0.0, 0.0)):
    e_sec, _ = bound3(-5.0, Kv, 4)
    e_ed = ed3_lowest(4, Kv, -5.0)
    ed_gap.append(abs(e_sec - e_ed))
E0_12, edge0 = bound3(-5.0, (0.0, 0.0, 0.0), 12)
dk = 2 * np.pi / 12
curv3 = []
for direc in ((1, 0, 0), (1, 1, 0), (1, 1, 1)):
    dK = dk * np.array(direc, float)
    E1, _ = bound3(-5.0, dK, 12)
    curv3.append((E1 ** 2 - E0_12 ** 2) / np.dot(dK, dK))
E0_8, _ = bound3(-8.0, (0.0, 0.0, 0.0), 12)
E1_8, _ = bound3(-8.0, (dk, 0.0, 0.0), 12)
curv8 = (E1_8 ** 2 - E0_8 ** 2) / dk ** 2
below = E0_12 < edge0 - 1e-3
sign_ok = all(c < -0.5 for c in curv3) and curv8 < -0.5
spread = max(curv3) - min(curv3)
record("S6", max(ed_gap) < 1e-8 and below and sign_ok and spread < 0.05,
       f"4^3 secular vs ED {max(ed_gap):.1e}; V=-5 E(0)={E0_12:.4f} edge={edge0:.4f}; "
       f"(E^2-E0^2)/K^2 on 12^3 = {', '.join(f'{c:.3f}' for c in curv3)}; V=-8 axis {curv8:.3f}")


# ---------------------------------------------------------------- step 7: timed identity
def chain(N, g, Vc, timed, s1, s2, kind):
    x = np.arange(N)
    w = np.exp(g * (x - N // 2))
    D = np.zeros((N, N), dtype=complex)
    for i in range(1, N):
        D[i, i - 1] = 0.5j
    for i in range(N - 1):
        D[i, i + 1] = -0.5j
    sw = np.sqrt(w)
    Dw = sw[:, None] * D * sw[None, :]
    I = np.eye(N)
    H = s1 * np.kron(Dw, I) + s2 * np.kron(I, Dw)
    for x1 in range(N):
        partners = [x1] if kind == "contact" else [x1 - 1, x1 + 1]
        for x2 in partners:
            if 0 <= x2 < N:
                i = x1 * N + x2
                if timed:
                    wt = w[x1] if kind == "contact" else np.sqrt(w[x1] * w[x2])
                else:
                    wt = 1.0
                H[i, i] += Vc * wt
    return H, w


ident = {}
Nid, gid = 10, 0.25
for kind in ("contact", "nn"):
    for timed in (True, False):
        H, w = chain(Nid, gid, -1.2, timed, 1, -1, kind)
        T = np.zeros((Nid * Nid, Nid * Nid), dtype=complex)
        for x1 in range(1, Nid):
            for x2 in range(1, Nid):
                T[x1 * Nid + x2, (x1 - 1) * Nid + (x2 - 1)] = 1.0
        lam = np.exp(gid)
        M = H @ T - lam * T @ H
        inner = [x1 * Nid + x2 for x1 in range(3, Nid - 3) for x2 in range(3, Nid - 3)]
        ident[(kind, timed)] = np.abs(M[np.ix_(inner, inner)]).max()
id_ok = ident[("contact", True)] < 1e-9 and ident[("nn", True)] < 1e-9
id_ok = id_ok and ident[("contact", False)] > 0.05 and ident[("nn", False)] > 0.05
record("S7", id_ok, "interior commutator " + ", ".join(
    f"{k[0]}/{'timed' if k[1] else 'untimed'} {v:.1e}" for k, v in ident.items()))


# ---------------------------------------------------------------- step 8: at-rest curvature and a short propagation
eps = sp.symbols("eps", real=True)
# closed forms
Eco = -sp.sqrt(V ** 2 + 4 * sp.sin(K / 2) ** 2)
Ect = -sp.sqrt(V ** 2 + 4 * sp.cos(K / 2) ** 2)
dco = sp.simplify(sp.diff(Eco ** 2 / 2, K, 2).subs(K, 0))
dct = sp.simplify(sp.diff(Ect ** 2 / 2, K, 2).subs(K, 0))
# nn quadratic: E^2 = Vn^2 + c2 K^2, second derivative of E^2/2 is c2
record("S8a", sp.simplify(dco - 1) == 0 and sp.simplify(dct + 1) == 0,
       f"d^2(E^2/2) at K=0 is {dco} (co-moving, a=-g) and {dct} (counter-moving, a=+g)")


def accel(H, psi, g, tmax=12.0, n=7):
    N = int(np.sqrt(len(psi)))
    x = np.arange(N)
    Xc = 0.5 * (np.repeat(x, N) + np.tile(x, N)) - N / 2
    ts = np.linspace(0.0, tmax, n)
    Xs = []
    for t in ts:
        ph = psi if t == 0 else expm_multiply(-1j * H * t, psi)
        p = np.abs(ph) ** 2
        Xs.append(np.real(np.dot(p, Xc) / p.sum()))
    return np.polyfit(ts, Xs, 2)[0] * 2 / g


def packet(N, sigma, rel):
    x = np.arange(N)
    X1, X2 = np.repeat(x, N), np.tile(x, N)
    Xc = 0.5 * (X1 + X2) - N / 2.0
    psi = np.exp(-Xc ** 2 / (4 * sigma ** 2)) * rel(X1 - X2)
    psi = psi / np.linalg.norm(psi)
    return psi


Nrun, grun, sig = 72, 0.008, 8.0
# counter-moving relative bound state at K=0, V=-1: phi(q) = 1/(E - 2 sin q)
Mq = 256
qg = 2 * np.pi * np.arange(Mq) / Mq
Ect0 = -np.sqrt(1.0 + 4.0)
phi_r = np.fft.ifft(1.0 / (Ect0 - 2 * np.sin(qg))) * Mq

runs = []
H, _ = chain(Nrun, grun, -1.0, True, 1, 1, "contact")
a_co = accel(H, packet(Nrun, sig, lambda r: (r == 0).astype(float)), grun)
runs.append(("co-moving timed", a_co, -1.0))
H, _ = chain(Nrun, grun, -1.0, False, 1, 1, "contact")
a_un = accel(H, packet(Nrun, sig, lambda r: (r == 0).astype(float)), grun)
runs.append(("co-moving untimed", a_un, 0.0))
H, _ = chain(Nrun, grun, -1.0, True, 1, -1, "contact")
a_ct = accel(H, packet(Nrun, sig, lambda r: phi_r[np.asarray(r) % Mq]), grun)
runs.append(("counter-moving timed", a_ct, 1.0))
H, _ = chain(Nrun, grun, -2.0, True, 1, 1, "nn")
a_even = accel(H, packet(Nrun, sig, lambda r: (np.abs(r) == 1).astype(float)), grun)
runs.append(("nn even timed", a_even, -1.5))
# The 72-site packet is shorter than the attempt's 130-site run, so the co-moving
# residual is several hundredths. The sign and the channel, not a 1% fit, are the check.
prop_ok = abs(a_co + 1) < 0.15 and abs(a_un) < 0.08 and abs(a_ct - 1) < 0.15 and abs(a_even + 1.5) < 0.2
record("S8b", prop_ok, "executed a/g " + "; ".join(f"{n} {a:+.3f} (rest {rest:+.1f})" for n, a, rest in runs))

print(f"TOTAL: PASS={sum(PASS)} FAIL={len(PASS) - sum(PASS)}")
if all(PASS):
    print("SUMMARY: confirmed — 1D contact dispersions are exact (co-moving c=1, counter-moving band minimum), "
          "nearest-neighbour c^2 is 3/2 and 1/2 at quadratic order only, the 3D contact ground pair is a band minimum, "
          "and a timed degree-one interaction obeys H T = λ T H so the at-rest acceleration is -d^2(E^2/2) g "
          "(−g, +g, −3g/2, 0 untimed); the §1 all-K formula E^2 = V_n^2 + 6 sin^2(K/2) is only the O(K^2) statement of step 5")
    print("HIT: confirmed - the a3 claim survives: binding supplies a rest energy M=|V| inside M_2(C) per walker for the "
          "1D co-moving contact pair (E^2 = V^2 + 4 sin^2(K/2), c=1), the timed two-walker generator scales as "
          "H_w T_a = λ_a T_a H_w, and free fall is not universal (counter-moving and 3D contact ground pairs fall up; "
          "an untimed contact pair at rest does not fall)")
else:
    bad = [i for i, ok in enumerate(PASS, start=1) if not ok]
    print(f"SUMMARY: fails at step {bad[0]} - independent checks {bad} did not reproduce the attempt")
