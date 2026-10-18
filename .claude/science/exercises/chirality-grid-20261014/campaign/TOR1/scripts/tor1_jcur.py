"""TOR-1 F10: Luscher's measure current j_l = L_{e_l} of the construction's basis (Theorem 5.1 object), its anomalous Ward
identity, and its locality (response to one source link vs torus distance).  usage: python3 tor1_jcur.py Lx Lt model nfield seed"""
import sys, time
import numpy as np
from tor1_lib import *
Lx, Lt, model, nf, seed = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], int(sys.argv[4]), int(sys.argv[5])
S = Torus(Lx, Lt); rng = np.random.default_rng(seed); t0 = time.time(); eps, dlt = 1e-4, 1e-3
Ns = int(sys.argv[6]) if len(sys.argv) > 6 else 8; WARD_ONLY = len(sys.argv) > 7
M = TorusMeasure(S, model, Ns=Ns, sk=-1, ntor=96, nloop=512, ngam=256); M.ntor1 = 24; M.use_spline()
mid = np.array([(l[4] + 0.5, l[5]) if l[2] == 'x' else (l[4], l[5] + 0.5) for l in S.L])
def td(a, b):
    dx = abs(a[0] - b[0]); dt = abs(a[1] - b[1]); return min(dx, Lx - dx) + min(dt, Lt - dt)


def construct(th):
    """bases V_f and phase alpha at the ACTUAL fields th (ray from U[w] to th itself; no canonicalisation)."""
    F, Q, AT, w = S.decompose(th); assert np.all(Q == 0)
    Aw = w[:, 0:1] * S.Ux[None] + w[:, 1:2] * S.Ut[None]; Ap = th - Aw
    V0, _ = M.toron_basis(w); r = M.ray(Ap, w, V0, Ns, True)
    alpha = (-w[:, 1] * (M.Gam_t(w[:, 0]) - M.gam[0]) / (2 * np.pi)) + M.sk * np.sum(Ap * r['kbb'], 1)
    return r['V'], alpha, r['Abar']


def current(th):
    """j_l at field th (1D), all links, by central differences of the basis and of alpha."""
    E = np.eye(S.nl) * eps; pts = np.concatenate([th + E, th - E], 0); Vs = {}; al = []
    CHK = 32 if S.N <= 64 else 4
    for c in range(0, len(pts), CHK):
        V, a, _ = construct(pts[c:c + CHK]); al.append(a)
        for kf, v in V.items(): Vs.setdefault(kf, []).append(v)
    al = np.concatenate(al); j = -(al[:S.nl] - al[S.nl:]) / (2 * eps)
    for (e, c, m) in M.model:
        V = np.concatenate(Vs[(e, c)]); Vp, Vm = V[:S.nl], V[S.nl:]
        sg, ld = np.linalg.slogdet(np.conj(np.swapaxes(Vm, 1, 2)) @ Vp)
        j = j - m * np.angle(sg) / (2 * eps)
    return j


print(f"# TOR-1 measure current Lx={Lx} Lt={Lt} model={model} eps={eps} dlt={dlt} Ns={Ns}", flush=True)
for f in range(nf):
    while True:   # random admissible canonical field, then a small random gauge transformation (actual field non-canonical)
        th = rng.normal(0, 0.12, S.nl) + rng.uniform(0, 2*np.pi) * S.Ux + rng.uniform(0, 2*np.pi) * S.Ut
        Fr = (th @ S.Pm.T + np.pi) % (2*np.pi) - np.pi
        if np.abs(Fr).max() < 0.5 and abs(round(Fr.sum()/(2*np.pi))) == 0: break
    _, _, AT, w = S.decompose(th[None]); th = S.canon(AT, w)[0]
    th = S.gauge(th[None], rng.uniform(-0.05, 0.05, (1, S.ns)))[0]
    j = current(th)
    _, _, Ab = construct(th[None])
    # anomaly at the field itself: q_tot(x) from the ray end; Abar is the ray average, so recompute q_tot at s = 1
    q = np.zeros(S.ns)
    for e in M.charges:
        wv, Vv = np.linalg.eigh(S.H(e * th[None])); q += M.coef[e] * q_of(S, wv, Vv)[0]
    for trial in range(3):
        om = rng.normal(0, 1, S.ns); dom = om[S.frm] - om[S.to]
        print(f"field {f} Ward: sum_l (d omega)_l j_l = {dom @ j:+.10e}; sum_x omega q_tot = {om @ q:+.10e}; ratio {(dom @ j)/(om @ q):+.8f}", flush=True)
    for l0 in (() if WARD_ONLY else (S.key[('x', 1, 2)], S.key[('t', 2, 1)])):
        jp = current(th + dlt * np.eye(S.nl)[l0]); jm = current(th - dlt * np.eye(S.nl)[l0]); R = (jp - jm) / (2 * dlt)
        ds = np.array([td(mid[l0], mid[l]) for l in range(S.nl)])
        prof = [(dv, np.abs(R[ds == dv]).max()) for dv in np.unique(ds)]
        X = np.array([p[0] for p in prof if p[0] >= 1]); Y = np.log(np.array([p[1] for p in prof if p[0] >= 1]))
        A = np.vstack([X, np.ones_like(X)]).T; c, *_ = np.linalg.lstsq(A, Y, rcond=None); r = Y - A @ c
        se = np.sqrt((r @ r) / max(len(X) - 2, 1) * np.linalg.inv(A.T @ A)[0, 0])
        print(f"field {f} source {S.L[l0][2]}{S.L[l0][4:6]}: |dj/dtheta| vs d: " + " ".join(f"{dv:.1f}:{p:.2e}" for dv, p in prof)
              + f" | fit rate {-c[0]:.3f} +- {se:.3f} [{time.time()-t0:.0f}s]", flush=True)
