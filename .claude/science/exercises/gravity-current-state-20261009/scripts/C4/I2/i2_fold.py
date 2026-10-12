"""Lane RI / probe I2 (a): N-site cells of a nearest-neighbour chain = the fine lattice (spacing a/N), folded.

Units: coarse cell a = 1, c = 1 at small momentum.  Fine spacing b = 1/N.
Fine NN Klein-Gordon: w^2(K) = m^2 + 4 N^2 sin^2(K/(2N)),  K in (-pi N, pi N]  (K = lifted / tower momentum).
Coarse Bloch matrix of the N-site cell (dynamical matrix W(k), N x N):
   W = (m^2 + 2N^2) 1 - N^2 (S + S^dag),  S = cyclic shift with the boundary bond carrying e^{ik}.
Tower (empty lattice): E_n(k) = sqrt(m^2 + (k + 2 pi n)^2).

(1) folding identity: eig W(k) == {w^2(k + 2 pi n)} exactly (machine precision).
(2) C1 shift-closure residual  f(K) - K,  f = (1/2) d w^2/dK = N sin(K/N)  (band-resolved, on the lifted zone of each band).
(3) C3 boost anomaly symbol A(K) = u''(K) - 1,  u = w^2/2  ->  A = cos(K/N) - 1  (band-resolved).
    band-summed zone average  <sum_n A_n>/N  (exactly -1 for every N: sum rule, see i2_sumrule.py).
(4) loop-weighted anomaly in d = 1 and d = 3 (separable NN dispersion, boost along x):
      R_s(N) = sum_modes A_x(K) w^s / sum_modes w^s ,  s = 1 (zero-point energy), -1 (tadpole), -3, -5,
    and the absolute per-coarse-cell anomaly  sum_modes A_x w/2 / N^{d+1}  (natural size of a vacuum loop
    with cutoff ~ N/a).
"""
import numpy as np
np.set_printoptions(linewidth=160)
m = 1.0
out = []
def P(s=""):
    print(s, flush=True); out.append(s)

def Wcell(k, N):
    W = np.zeros((N, N), complex)
    for j in range(N):
        W[j, j] = m**2 + 2 * N**2
    for j in range(N - 1):
        W[j, j + 1] = W[j + 1, j] = -N**2
    W[N - 1, 0] += -N**2 * np.exp(1j * k)
    W[0, N - 1] += -N**2 * np.exp(-1j * k)
    return W

def w2fine(K, N):
    return m**2 + 4 * N**2 * np.sin(K / (2 * N))**2

P("=== (1) folding identity: N-site NN cell spectrum vs fine NN chain at K = k + 2 pi n ===")
for N in (2, 3, 4, 8, 16, 32):
    err = 0.0
    for k in np.linspace(-np.pi, np.pi, 41):
        ev = np.sort(np.linalg.eigvalsh(Wcell(k, N)))
        Ks = k + 2 * np.pi * np.arange(N)
        ref = np.sort(w2fine(Ks, N))
        err = max(err, np.max(np.abs(ev - ref)) / (4 * N**2))
    P(f"N={N:3d}: max |eig W(k) - w^2_fine(k+2pi n)| / bandwidth = {err:.1e}")
P("-> the N-site cell is the fine chain (spacing a/N) folded; bands touch exactly at the coarse faces/centre.")

P("\n=== (2) C1 shift-closure residual f(K)-K, f = N sin(K/N), band n covers |K - 2 pi n| <= pi ===")
P("   (target: tower f = K on every band; lowest band n=0 is |K|<=pi; truncation edge |K| = pi N)")
P("  N   band0 sup|f-K|   pi^3/(6N^2)   band1 sup   band2 sup   top band sup |f-K|   top/(pi N)   window|K|<=pi/4")
for N in (2, 4, 8, 16, 32, 64, 128, 256, 1024):
    def sup_band(n):
        K = 2 * np.pi * n + np.linspace(-np.pi, np.pi, 2001)
        K = K[np.abs(K) <= np.pi * N + 1e-12]
        return np.max(np.abs(N * np.sin(K / N) - K))
    top = (N - 1) // 2 if N % 2 else N // 2
    Kw = np.linspace(-np.pi / 4, np.pi / 4, 2001)
    w = np.max(np.abs(N * np.sin(Kw / N) - Kw))
    b1 = sup_band(1) if N > 2 else float('nan')
    b2 = sup_band(2) if N > 4 else float('nan')
    st = sup_band(top)
    P(f"{N:5d}  {sup_band(0):.4e}   {np.pi**3 / (6 * N**2):.4e}   {b1:.3e}   {b2:.3e}   {st:.4e}   {st / (np.pi * N):.4f}   {w:.3e}")
P("-> band n (n << N): sup|f-K| ~ ((2n+1) pi)^3/(6 N^2); edge band: |f-K| -> pi N (relative 1): the C1 face floor,")
P("   moved from the coarse face to the fine face (truncation edge).")

P("\n=== (3) C3 boost anomaly A(K) = cos(K/N) - 1, band-resolved ===")
P("  N   max|A| band0   (pi/N)^2/2    max|A| band1   A at edge   <A> over all N bands (zone average)")
for N in (2, 4, 8, 16, 32, 64, 128, 256, 1024):
    K0 = np.linspace(-np.pi, np.pi, 4001)
    a0 = np.max(np.abs(np.cos(K0 / N) - 1))
    K1 = np.linspace(np.pi, 3 * np.pi, 4001)
    a1 = np.max(np.abs(np.cos(K1 / N) - 1)) if N > 2 else float('nan')
    # zone average over all bands = average over the fine zone K in (-pi N, pi N]
    Kz = (np.arange(200 * N) + 0.5) / (200 * N) * 2 * np.pi * N - np.pi * N
    avg = np.mean(np.cos(Kz / N) - 1)
    P(f"{N:5d}  {a0:.4e}   {(np.pi / N)**2 / 2:.4e}   {a1:.4e}   {np.cos(np.pi) - 1:+.1f}   {avg:+.6f}")
P("improved fine stencils (range r_m): A(K) ~ -c_r (K/N)^{2 r_m}, edge values exact -2,-8/3,-16/5,-128/35,-256/63 (C3 referee);")
P("zone average stays -1 for every r_m and every N.")
cn = [1.0, 1 / 12, 1 / 90, 1 / 560, 1 / 3150]
def u_imp(x, rm):  # fine units x = K/N
    s2 = (2 * np.sin(x / 2))**2
    return 0.5 * sum(cn[j] * s2**(j + 1) for j in range(rm))
def upp_imp(x, rm, h=1e-4):
    return (u_imp(x + h, rm) - 2 * u_imp(x, rm) + u_imp(x - h, rm)) / h**2
P("  r_m   max|A| band0 for N = 4, 16, 64            A(edge)   zone-avg")
for rm in (1, 2, 3, 4):
    row = []
    for N in (4, 16, 64):
        x = np.linspace(-np.pi, np.pi, 2001) / N
        row.append(np.max(np.abs(upp_imp(x, rm) - 1)))
    xz = (np.arange(4000) + 0.5) / 4000 * 2 * np.pi - np.pi
    P(f"  {rm}    {row[0]:.3e} {row[1]:.3e} {row[2]:.3e}     {upp_imp(np.pi - 1e-3, rm) - 1:+.4f}   {np.mean(upp_imp(xz, rm) - 1):+.4f}")

P("\n=== (4) loop-weighted anomaly, d = 1 and d = 3 (separable NN fine lattice, boost along x) ===")
P("   R_s(N) = sum A_x w^s / sum w^s over all modes of the fine zone (= all N^d bands x coarse zone)")
P("   abs = sum_modes A_x w/2 per coarse cell, divided by N^(d+1) (natural size of a cutoff-N vacuum loop)")
for d in (1, 3):
    P(f"  d = {d}")
    P("     N     R_1       R_-1      R_-3      R_-5      abs/N^(d+1)")
    for N in ((4, 8, 16, 32, 64, 128, 256) if d == 1 else (2, 4, 8, 16, 32, 64)):
        # graded quadrature on the fine zone (all bands x coarse zone), x = K/N = pi t^3, t in (-1,1)
        G = 4000 if d == 1 else 110
        t = (np.arange(G) + 0.5) / G * 2 - 1
        x = np.pi * t**3; jw = 3 * np.pi * t**2 * (2 / G)          # dx weights
        g = N * x; gw = N * jw                                       # K and dK
        if d == 1:
            w2 = w2fine(g, N); Ax = np.cos(g / N) - 1; Wt = gw
        else:
            sx = 4 * N**2 * np.sin(g / (2 * N))**2
            w2 = m**2 + sx[:, None, None] + sx[None, :, None] + sx[None, None, :]
            Ax = np.broadcast_to((np.cos(g / N) - 1)[:, None, None], w2.shape)
            Wt = gw[:, None, None] * gw[None, :, None] * gw[None, None, :]
        wt_cells = 1.0 / (2 * np.pi)**d          # integral dK/(2pi) per coarse cell
        w = np.sqrt(w2)
        R = [np.sum(Wt * Ax * w**s) / np.sum(Wt * w**s) for s in (1, -1, -3, -5)]
        ab = np.sum(Wt * Ax * w / 2) * wt_cells / N**(d + 1)
        P(f"   {N:4d}   {R[0]:+.4f}   {R[1]:+.4f}   {R[2]:+.4f}   {R[3]:+.4f}   {ab:+.4f}")
P("-> UV-dominated loop weights (zero-point energy, tadpole) carry an N-independent O(1) relative anomaly;")
P("   the marginal weight s = -d falls only like 1/ln N; IR-dominated weights (s < -d) fall like a power of N.")
P("   The absolute vacuum anomaly per coarse cell grows like N^(d+1) (abs/N^(d+1) -> constant).")
open('i2_fold.out', 'w').write('\n'.join(out) + '\n')
