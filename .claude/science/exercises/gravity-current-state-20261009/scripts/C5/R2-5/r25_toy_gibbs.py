"""R2-5 check 2: 1+1 Euclidean, time-reflection-symmetric Gibbs toy with a low-record boundary.

Sites (x, t), x in Z_L (periodic), t = 0..T.  s in {0 blank, 1 locked}.
Row t = 0 is fixed blank (the low-record boundary); the top row T is free (no future boundary).
Weight  = exp(h * #locked)  *  ex^(# spatial disagreements)  *  et^(# temporal disagreements).
  isotropic (whole-law square-lattice symmetry, the 1+1 analogue of B4+): ex = et = eps
  anisotropic (a law-level preferred axis):  ex = 1 (no spatial coupling), et = eps
No oriented coupling anywhere: every weight is invariant under t -> -t.
Exact transfer matrices over 2^L row states.  Outputs per t: record density m(t), formation
f(t) = E#(0->1)/L, un-formation u(t) = E#(1->0)/L between t and t+1.
Also: P(no un-formation anywhere in the box), bulk u at t = T/2, the arrow length t90 (time by
which 90% of the net formation over [0, T/2] has occurred), the transfer-matrix correlation
length xi = 1/ln(l0/l1), and two controls: blank boundary at the top instead (reversed arrow)
and blank at both ends (no arrow: f(t) = u(T-1-t)).
"""
import itertools
import numpy as np

def build(L, h, ex, et):
    S = np.array(list(itertools.product((0, 1), repeat=L)), dtype=int)
    nloc = S.sum(1)
    dw = (S != np.roll(S, 1, axis=1)).sum(1)
    R = np.exp(h * nloc) * ex ** dw
    ham = (S[:, None, :] != S[None, :, :]).sum(2)
    W = et ** ham
    up = (S[:, None, :] == 1) & (S[None, :, :] == 0)   # site locked at t, blank at t+1
    dn = (S[:, None, :] == 0) & (S[None, :, :] == 1)
    U = up.sum(2)   # number of un-formations in the step
    F = dn.sum(2)   # number of formations in the step
    return S, nloc, R, W, U, F

def profile(L, h, ex, et, T, top_blank=False, bottom_blank=True, noU=False):
    S, nloc, R, W, U, F = build(L, h, ex, et)
    n = len(S)
    Wm = W * (U == 0) if noU else W
    # row weights for rows 1..T-1 are R; boundary rows are fixed blank (index 0) if requested
    Rrow = [None] * (T + 1)
    for t in range(T + 1):
        r = R.copy()
        if (t == 0 and bottom_blank) or (t == T and top_blank):
            r = np.zeros(n); r[0] = 1.0
        Rrow[t] = r
    # forward
    alpha = [None] * (T + 1); logZf = 0.0
    a = Rrow[0].copy(); s = a.sum(); a /= s; logs = [np.log(s)]
    alpha[0] = a
    for t in range(1, T + 1):
        a = (alpha[t - 1] @ Wm) * Rrow[t]
        s = a.sum(); a = a / s; logs.append(np.log(s)); alpha[t] = a
    logZ = sum(logs)
    beta = [None] * (T + 1)
    b = np.ones(n); beta[T] = b
    for t in range(T - 1, -1, -1):
        b = Wm @ (Rrow[t + 1] * beta[t + 1]); b = b / b.sum(); beta[t] = b
    m = np.zeros(T + 1); f = np.zeros(T); u = np.zeros(T)
    for t in range(T + 1):
        p = alpha[t] * beta[t]; p /= p.sum(); m[t] = (p @ nloc) / L
    for t in range(T):
        P = alpha[t][:, None] * Wm * (Rrow[t + 1] * beta[t + 1])[None, :]
        P /= P.sum()
        f[t] = (P * F).sum() / L; u[t] = (P * U).sum() / L
    return m, f, u, logZ

def corr_length(L, h, ex, et):
    S, nloc, R, W, U, F = build(L, h, ex, et)
    D = np.sqrt(R)
    M = D[:, None] * W * D[None, :]
    lam = np.linalg.eigvalsh(M)
    lam = np.sort(np.abs(lam))[::-1]
    return 1.0 / np.log(lam[0] / lam[1]), lam[0], lam[1]

def t90(f, u):
    half = len(f) // 2
    net = np.cumsum(f[:half] - u[:half])
    tot = net[-1]
    if tot <= 0:
        return float('nan')
    return int(np.argmax(net >= 0.9 * tot)) + 1

def run(L, h, eps, T, iso=True):
    ex = eps if iso else 1.0
    et = eps
    m, f, u, logZ = profile(L, h, ex, et, T)
    _, _, _, logZnoU = profile(L, h, ex, et, T, noU=True)
    pnoU = np.exp(logZnoU - logZ)
    xi, l0, l1 = corr_length(L, h, ex, et)
    half = T // 2
    return dict(m_half=m[half], f_half=f[half], u_half=u[half], t90=t90(f, u), pnoU=pnoU, xi=xi,
                f1=f[0], u1=u[0])

def controls(L, h, eps, T):
    m1, f1, u1, _ = profile(L, h, eps, eps, T)                       # blank bottom
    m2, f2, u2, _ = profile(L, h, eps, eps, T, top_blank=True, bottom_blank=False)  # blank top
    m3, f3, u3, _ = profile(L, h, eps, eps, T, top_blank=True, bottom_blank=True)   # both blank
    print(f"  controls L={L} h={h} eps={eps} T={T}:")
    print(f"    blank bottom: f(0..3) = {np.round(f1[:4],5)}, u(0..3) = {np.round(u1[:4],5)}")
    print(f"    blank top   : f(T-4..T-1) = {np.round(f2[-4:],5)}, u(T-4..T-1) = {np.round(u2[-4:],5)}  (mirror: u_top(T-1-t) = f_bottom(t)?)")
    mir = np.max(np.abs(u2[::-1][:T//2] - f1[:T//2])) if True else 0
    print(f"    max |u_top(T-1-t) - f_bottom(t)| over t<T/2 = {mir:.2e} (should be ~0 up to free-boundary effects)")
    sym = np.max(np.abs(f3 - u3[::-1]))
    print(f"    both blank  : max |f(t) - u(T-1-t)| = {sym:.2e} (exact time symmetry -> 0); total net formation over box = {(f3-u3).sum():.2e}")

if __name__ == "__main__":
    np.set_printoptions(linewidth=160)
    T = 80
    print("== isotropic (whole-law square symmetry) ==")
    print(" L    h      eps   | m(T/2)   f(T/2)     u(T/2)     u/f   | t90 | xi_t   | P(no un-formation in box) | f(0) u(0)")
    for L in (6, 8):
        for eps in (0.6, 0.4142, 0.3, 0.1, 0.01):
            for h in (0.01, 0.1, 1.0, 3.0):
                r = run(L, h, eps, T, iso=True)
                ratio = r['u_half'] / r['f_half'] if r['f_half'] > 0 else float('nan')
                print(f" {L:2d} {h:6.2f} {eps:7.4f} | {r['m_half']:.4f} {r['f_half']:.3e} {r['u_half']:.3e} {ratio:5.3f} | {r['t90']:3} | {r['xi']:7.3f} | {r['pnoU']:.3e} | {r['f1']:.3e} {r['u1']:.3e}")
    print("== anisotropic (no spatial coupling: a law-level preferred axis), single column L=1 ==")
    print(" h        eps_t    | m(T/2)   f(T/2)     u(T/2)     | t90 | xi_t      | P(no un-formation) | predicted: arrow ~1/h, u ~ eps^2/h")
    T2 = 400
    for h, eps in ((0.05, 1e-3), (0.02, 1e-4), (0.01, 1e-5), (0.05, 0.2)):
        r = run(1, h, eps, T2, iso=False)
        print(f" {h:7.3f} {eps:9.1e} | {r['m_half']:.4f} {r['f_half']:.3e} {r['u_half']:.3e} | {r['t90']:3} | {r['xi']:9.3f} | {r['pnoU']:.4e} | {1/h:6.1f} {eps**2/h:.2e}")
    print("== L-dependence, isotropic, small field near coexistence (does the arrow lengthen with space?) ==")
    for eps in (0.3, 0.1):
        for h in (0.01, 0.1):
            row = []
            for L in (2, 4, 6, 8, 10):
                r = run(L, h, eps, 120, iso=True)
                row.append((L, r['t90'], round(r['xi'], 2), f"{r['u_half']:.1e}"))
            print(f"  eps={eps} h={h}: (L, t90, xi, u_bulk) = {row}")
    print("== controls (arrow comes only from the boundary) ==")
    controls(6, 0.1, 0.3, 60)
    controls(6, 1.0, 0.1, 60)
