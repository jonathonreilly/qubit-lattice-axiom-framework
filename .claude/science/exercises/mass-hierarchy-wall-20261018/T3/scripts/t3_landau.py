"""T-LANDAU: Eg Landau coefficients of GEN-2 rod generations from the one-loop fermion determinant (= HS mean field).
usage: python3 t3_landau.py A N|W [M]   (channel A, naive or Wilson; M = half-axis BZ points)
       python3 t3_landau.py B [MB]       (channel B, Yukawa/mass)
See ../PREREG.md. Phi = rho (cos t, sin t); e_i = rho * ehat_i(t), ehat = sqrt(2/3) cos(t - 2 pi i/3)."""
import sys, time, numpy as np
T0 = time.time()
TH = np.linspace(0, np.pi / 3, 121)                       # fundamental domain; 0 and pi/3 are tetragonal
def ehat(t):
    t = np.asarray(t)[..., None]
    return np.sqrt(2 / 3) * np.cos(t - 2 * np.pi * np.arange(3) / 3)
def fourier(V):                                            # V[..., 121] on [0, pi/3]; even, period 2pi/3
    w = np.full(TH.size, 1.0); w[0] = w[-1] = 0.5; w /= (TH.size - 1)
    out = {}
    for n in (0, 1, 2, 3):
        c = np.cos(3 * n * TH)
        out[n] = (V * c * w).sum(-1) * (1 if n == 0 else 2)
    return out
def ang_min(Vt):
    """exact angular minimum on [0, pi/3]: index argmin + parabolic refinement -> t* (rad)."""
    i = int(np.argmin(Vt))
    if i in (0, TH.size - 1):
        return TH[i]
    y0, y1, y2 = Vt[i - 1], Vt[i], Vt[i + 1]
    den = y0 - 2 * y1 + y2
    d = 0.5 * (y0 - y2) / den if den > 0 else 0.0
    return TH[i] + d * (TH[1] - TH[0])
def classify(t):
    return 'D2h' if (np.degrees(t) >= 0.5 and np.degrees(np.pi / 3 - t) >= 0.5) else 'TET'
def hull_realised(s, E):
    """indices on the lower convex hull of (s,E) with negative left slope (realisable for some G>0)."""
    pts = []
    for k in range(len(s)):
        while len(pts) >= 2:
            i, j = pts[-2], pts[-1]
            if (E[j] - E[i]) * (s[k] - s[i]) >= (E[k] - E[i]) * (s[j] - s[i]):
                pts.pop()
            else:
                break
        pts.append(k)
    out = []
    for m in range(1, len(pts)):
        i, j = pts[m - 1], pts[m]
        if (E[j] - E[i]) / (s[j] - s[i]) < 0:
            out.append(j)
    return out
def fib_sphere(n):
    i = np.arange(n) + 0.5
    z = 1 - 2 * i / n; r = np.sqrt(1 - z * z); ph = np.pi * (1 + 5 ** 0.5) * i
    return np.stack([r * np.cos(ph), r * np.sin(ph), z], 1)

# ---------------- channel A ----------------
def bz_axis(M):
    k = (np.arange(M) + 0.5) * np.pi / M                     # half axis; sin^2 and 1-cos even in k
    K = np.stack(np.meshgrid(k, k, k, indexing='ij'), 0).reshape(3, -1)
    return np.sin(K) ** 2, 1 - np.cos(K)
def velocities(eta, lam, rho, t):
    """v[..., a, i] for rods a, directions i."""
    e = ehat(t) * np.asarray(rho)[..., None]               # [..., 3]
    v0 = np.ones((3, 3)) + (eta - 1) * np.eye(3)
    l1, l2, l3 = lam
    v = v0 + l1 * e[..., None, :] + l2 * e[..., :, None] + l3 * np.eye(3) * e[..., :, None]
    return v
def V_A(eta, lam, rho, t, S, C, wilson):
    rho, t = np.broadcast_arrays(np.asarray(rho, float), np.asarray(t, float))
    shp = rho.shape; rho = rho.ravel(); t = t.ravel()
    out = np.empty(rho.size)
    for c0 in range(0, rho.size, 100):
        v = velocities(eta, lam, rho[c0:c0 + 100], t[c0:c0 + 100])     # [P,3,3]
        P = v.shape[0]
        E2 = (v.reshape(P * 3, 3) ** 2) @ S
        if wilson:
            E2 = E2 + (v.reshape(P * 3, 3) @ C) ** 2
        out[c0:c0 + 100] = -np.sqrt(E2).mean(-1).reshape(P, 3).sum(-1)
    return out.reshape(shp)
def rho_edge_A(eta, lam, vmin):
    v0 = np.ones((3, 3)) + (eta - 1) * np.eye(3)
    tt = np.linspace(0, 2 * np.pi, 721)
    dv = velocities(eta, lam, np.ones_like(tt), tt) - v0     # per unit rho
    m = dv.min(0)                                             # most negative over the circle
    with np.errstate(divide='ignore'):
        r = np.where(m < 0, (v0 - vmin) / (-m), np.inf)
    return min(1.5, r.min())

def run_coupling_A(eta, lam, S, C, wilson, nr=40):
    vmin = 0.05 * min(1, eta)
    re = rho_edge_A(eta, lam, vmin)
    rr = re * np.linspace(1 / nr, 1, nr)
    V = V_A(eta, lam, rr[:, None], TH[None, :], S, C, wilson)
    V00 = V_A(eta, lam, np.array([0.0]), np.array([0.0]), S, C, wilson)[0]
    tstar = np.array([ang_min(V[k]) for k in range(nr)])
    Emin = V.min(1)
    s = np.concatenate([[0.0], rr ** 2]); E = np.concatenate([[V00], Emin])
    real = [j - 1 for j in hull_realised(s, E)]
    # Landau coefficients
    rf = np.geomspace(0.02, min(0.25, 0.5 * re), 10)
    Vf = V_A(eta, lam, rf[:, None], TH[None, :], S, C, wilson)
    F = fourier(Vf)
    b = np.polyfit(rf ** 2, F[1] / rf ** 3, 2)[::-1]          # b3, b5, b7
    c = np.polyfit(rf ** 2, F[2] / rf ** 6, 2)[::-1]          # c6, c8, c10
    q = np.polyfit(rf ** 2, F[0], 3)[::-1]                    # const, a2, q4, q6
    Fm = fourier(V)
    return dict(re=re, rr=rr, tstar=tstar, real=real, b=b, c=c, q=q, V3=Fm[1], V6=Fm[2], V9=Fm[3])

def lv_cost(eta, lam):
    tt = np.linspace(0, 2 * np.pi, 361)
    v0 = np.ones((3, 3)) + (eta - 1) * np.eye(3)
    dv = velocities(eta, lam, np.ones_like(tt), tt) - v0
    return np.abs(dv).max(), np.abs(lam[0])                  # per unit rho: max rod speed shift; universal part

def main_A(wilson, M):
    S, C = bz_axis(M)
    lams = fib_sphere(120); etas = [1 / 3, 1 / 2, 1.0, 2.0, 3.0]
    tag = 'A-W' if wilson else 'A-N'
    print(f'=== channel {tag}, BZ midpoint {2*M}^3 (half-axis {M}), 120 coupling directions x 5 eta ===')
    rows = []
    for eta in etas:
        for li, lam in enumerate(lams):
            R = run_coupling_A(eta, lam, S, C, wilson)
            cls_all = [classify(t) for t in R['tstar']]
            cls_real = [(R['rr'][j], classify(R['tstar'][j]), j == len(R['rr']) - 1) for j in R['real']]
            # K criterion (sixth-order truncation) vs exact at each rho of the main grid
            kpred = ['D2h' if (R['V6'][k] > 0 and abs(R['V3'][k]) < 4 * R['V6'][k]) else 'TET' for k in range(len(R['rr']))]
            agree = np.mean([kp == ca for kp, ca in zip(kpred, cls_all)])
            rows.append(dict(eta=eta, li=li, lam=lam, R=R, cls_all=cls_all, cls_real=cls_real, kagree=agree))
        print(f'  eta={eta:.3g} done t={time.time()-T0:.0f}s'); sys.stdout.flush()
    # summaries
    for eta in etas:
        sub = [r for r in rows if r['eta'] == eta]
        nD_any = sum('D2h' in r['cls_all'] for r in sub)
        nD_real = sum(any(c == 'D2h' and not edge for _, c, edge in r['cls_real']) for r in sub)
        nD_edge = sum(any(c == 'D2h' and edge for _, c, edge in r['cls_real']) for r in sub)
        nreal = sum(len(r['cls_real']) > 0 for r in sub)
        b3 = np.array([r['R']['b'][0] for r in sub]); c6 = np.array([r['R']['c'][0] for r in sub])
        print(f'eta={eta:.3g}: directions with ANY rho giving D2h angular min: {nD_any}/120; '
              f'with a REALISED interior D2h vacuum: {nD_real}/120; D2h only at edge: {nD_edge}; ordered at all: {nreal}/120')
        print(f'     b3: frac>0 {np.mean(b3>0):.2f}, median |b3| {np.median(np.abs(b3)):.3g};  c6: frac>0 {np.mean(c6>0):.2f}, '
              f'median |c6| {np.median(np.abs(c6)):.3g};  K-criterion agreement with exact (all rho) {np.mean([r["kagree"] for r in sub]):.3f}')
    print('\n--- D2h realised vacua (interior), details ---')
    det = []
    for r in rows:
        Dl = [(rho, edge) for rho, c, edge in r['cls_real'] if c == 'D2h']
        if Dl:
            R = r['R']
            js = [j for j in R['real'] if classify(R['tstar'][j]) == 'D2h']
            ts = [np.degrees(R['tstar'][j]) for j in js]
            lv = lv_cost(r['eta'], r['lam'])
            print(f"eta={r['eta']:.3g} lam=({r['lam'][0]:+.2f},{r['lam'][1]:+.2f},{r['lam'][2]:+.2f}) rho_edge={R['re']:.3f} "
                  f"D2h realised rho={np.round([d[0] for d in Dl],3).tolist()} edge={[d[1] for d in Dl]} t*={np.round(ts,1).tolist()} deg "
                  f"b3={R['b'][0]:+.3g} c6={R['c'][0]:+.3g} 4c6rho^3/|b3| at first={4*R['c'][0]*Dl[0][0]**3/abs(R['b'][0]):.2f} "
                  f"LV per unit rho: rod {lv[0]:.2f}, universal {lv[1]:.2f}")
            det.append(dict(eta=r['eta'], lam=r['lam'], rho=[d[0] for d in Dl], edge=[d[1] for d in Dl], t=ts))
    print('\n--- per-direction Landau coefficient table (eta=1 and eta=2, first 12 directions) ---')
    for r in rows:
        if r['eta'] in (1.0, 2.0) and r['li'] < 12:
            R = r['R']
            print(f"eta={r['eta']:.3g} lam=({r['lam'][0]:+.2f},{r['lam'][1]:+.2f},{r['lam'][2]:+.2f}) a2={R['q'][1]:+.4g} q4={R['q'][2]:+.4g} "
                  f"b3={R['b'][0]:+.4g} c6={R['c'][0]:+.4g} rho_edge={R['re']:.3f} realised rho={np.round(R['rr'][R['real']],3).tolist()} "
                  f"classes={[c for _,c,_ in r['cls_real']]}")
    np.save(f'../t3_{tag}_details.npy', np.array(det, dtype=object), allow_pickle=True)
    return rows

# ---------------- channel B ----------------
def multiset_S(M):
    k = (np.arange(M) + 0.5) * np.pi / M; s = np.sin(k) ** 2
    Ss, W = [], []
    for i in range(M):
        for j in range(i, M):
            kk = np.arange(j, M)
            mult = np.where(i == j, np.where(kk == j, 1, 3), np.where(kk == j, 3, 6))
            Ss.append(s[i] + s[j] + s[kk]); W.append(mult)
    Ss = np.concatenate(Ss); W = np.concatenate(W).astype(float)
    return Ss, W / W.sum()
def massmat(m0, mJ, mu1, mu2, rho, t):
    e = ehat(t) * np.asarray(rho)[..., None]
    J = np.ones((3, 3)); I = np.eye(3)
    off = np.zeros(e.shape[:-1] + (3, 3))
    off[..., 1, 2] = off[..., 2, 1] = e[..., 0]; off[..., 0, 2] = off[..., 2, 0] = e[..., 1]; off[..., 0, 1] = off[..., 1, 0] = e[..., 2]
    D = e[..., :, None] * I
    return m0 * I + mJ * (J - I) + mu1 * D + mu2 * off
def V_B(pars, rho, t, Ss, W):
    rho, t = np.broadcast_arrays(np.asarray(rho, float), np.asarray(t, float))
    shp = rho.shape
    Mm = massmat(*pars, rho.ravel(), t.ravel())
    ev = np.linalg.eigvalsh(Mm).ravel() ** 2
    out = np.empty(ev.size)
    for c0 in range(0, ev.size, 200):
        out[c0:c0 + 200] = -(np.sqrt(Ss[None, :] + ev[c0:c0 + 200, None]) * W).sum(-1)
    return out.reshape(-1, 3).sum(-1).reshape(shp)
def main_B(MB):
    Ss, W = multiset_S(MB)
    print(f'=== channel B (Yukawa/mass), BZ half-axis {MB} ({Ss.size} weighted S values) ===')
    phis = np.linspace(0, 2 * np.pi, 24, endpoint=False)
    tot = 0; nD = 0; nDreal = 0
    for m0 in (0.02, 0.2):
        for xJ in (0.0, 0.5, -0.5):
            line = []
            for ph in phis:
                pars = (m0, xJ * m0, np.cos(ph), np.sin(ph))
                rr = np.linspace(1.0 / 40, 1.0, 40)
                V = V_B(pars, rr[:, None], TH[None, :], Ss, W)
                V00 = V_B(pars, np.array([0.0]), np.array([0.0]), Ss, W)[0]
                ts = np.array([ang_min(V[k]) for k in range(40)])
                real = [j - 1 for j in hull_realised(np.concatenate([[0], rr ** 2]), np.concatenate([[V00], V.min(1)]))]
                rf = np.geomspace(0.01, 0.1, 8)
                F = fourier(V_B(pars, rf[:, None], TH[None, :], Ss, W))
                b3 = np.polyfit(rf ** 2, F[1] / rf ** 3, 2)[-1]; c6 = np.polyfit(rf ** 2, F[2] / rf ** 6, 2)[-1]
                cls = [classify(ts[j]) for j in range(40)]
                creal = [(rr[j], classify(ts[j]), j == 39) for j in real]
                tot += 1; nD += ('D2h' in cls); nDreal += any(c == 'D2h' and not e for _, c, e in creal)
                line.append((np.degrees(ph), b3, c6, [f'{r:.2f}:{c}{"(edge)" if e else ""}' for r, c, e in creal],
                             [round(float(np.degrees(ts[j])), 1) for j in real]))
            print(f'm0={m0} mJ/m0={xJ:+.1f}:')
            for ph, b3, c6, cr, tsr in line:
                print(f'   (mu1,mu2) at {ph:5.1f} deg: b3={b3:+.3g} c6={c6:+.3g} realised {cr} t*={tsr}')
            sys.stdout.flush()
    print(f'channel B: couplings with any-rho D2h angular min {nD}/{tot}; with realised interior D2h vacuum {nDreal}/{tot}')

if __name__ == '__main__':
    if sys.argv[1] == 'A':
        main_A(sys.argv[2] == 'W', int(sys.argv[3]) if len(sys.argv) > 3 else 16)
    elif sys.argv[1] == 'B':
        main_B(int(sys.argv[2]) if len(sys.argv) > 2 else 48)
    print(f'total time {time.time()-T0:.0f}s')
