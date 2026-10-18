from common import *
def Wcont(q):
    W = np.zeros((10, 4), complex)
    for i, (a, b) in enumerate(HC):
        for r in range(4): W[i, r] = 1j * (q[a] * (b == r) + q[b] * (a == r))
    return W
d = np.array([0.3, -0.5, 0.6, 0.55]); d /= np.linalg.norm(d)
for s in (0.1, 0.05, 0.025):
    q = s * d; W = strain_metric(Dc, q) @ Dc.gauge(q)[:, :4]; Wc = Wcont(q)
    lam = np.vdot(Wc.ravel(), W.ravel()) / np.vdot(Wc.ravel(), Wc.ravel())
    for sh in (0.0, 0.5):
        Wsh = Wc * np.exp(1j * sh * q.sum())
        lam2 = np.vdot(Wsh.ravel(), W.ravel()) / np.vdot(Wsh.ravel(), Wsh.ravel())
        print(f"s={s}: shift {sh} (phase e^(i q.u*{sh})): scale {lam2:.5f} rel misfit {np.linalg.norm(W - lam2*Wsh)/np.linalg.norm(W):.2e}")
    # per-column structure
    print("   W[:,0] / Wc[:,0] (nonzero):", np.round([W[i,0]/Wc[i,0] for i in range(10) if abs(Wc[i,0])>1e-12], 4))
