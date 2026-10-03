"""A41 d1: (1) closed-form family vs A34 c13's numerical null space (c13 reused by exec, its output suppressed);
(2) the pi-flux 24-band (2x2x2 KS cell) and 12-band (2x2x1) Bloch spectra equal 2*spec(H6) + 2*spec(-H6), resp.
spec(H6) + spec(-H6); (3) zero flux, theta = 0: H0 = sqrt2 B(k).S, the 8 triple points, slopes; (4) pi flux,
theta = 0: zero modes <=> det N(k) = 0 (a surface), kernel dimension, dispersion normal/tangent to the surface."""
import os, io, contextlib, signal, itertools
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[v] = "1"
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
C13 = os.path.join(HERE, "..", "A34", "c13_glued_link_hops.py")
ns = {"__file__": C13}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(open(C13).read(), "c13", "exec"), ns)
signal.alarm(38)
from common import *
rng = np.random.default_rng(41)

# (1) span check
vec = ns["vector"]                                          # 2 basis elements, each (3, 3, 3): M^(x), M^(y), M^(z)
def realvec(Ms): z = np.concatenate([m.reshape(-1) for m in Ms]); return np.concatenate([z.real, z.imag])
Bc = np.array([realvec(v) for v in vec]).T                   # 54 x 2
Bm = np.array([realvec(M_family(th)) for th in (0.0, np.pi / 2)]).T
def resid(A, B):                                            # max residual of B's columns projected on span(A)
    Q, _ = np.linalg.qr(A); return np.abs(B - Q @ (Q.T @ B)).max()
print(f"(1) closed form in c13's span: residual {resid(Bc, Bm):.1e}; c13's basis in the closed form's span: "
      f"residual {resid(Bm, Bc):.1e}; rank of closed form pair {np.linalg.matrix_rank(Bm)}")
sv = np.linalg.svd(M_family(0.3)[2], compute_uv=False)
print(f"    singular values of M^(z)(theta=0.3), t=1: {np.round(sv, 12)}; traces of M^(a): "
      f"{max(abs(np.trace(m)) for m in M_family(0.3)):.1e}")
# explicit gauge-free check: phase of the z-link hop in the spherical basis (m = +1 -> 0 and 0 -> -1 amplitudes)
th = 0.3; Mz = M_family(th)[2]
k1 = -(E3[0] + 1j * E3[1]) / np.sqrt(2); k0 = E3[2] + 0j; km = (E3[0] - 1j * E3[1]) / np.sqrt(2)
print(f"    M^(z): <0|M|+1> = {np.round(np.vdot(k0, Mz @ k1), 6)}, <-1|M|0> = {np.round(np.vdot(km, Mz @ k0), 6)}, "
      f"other matrix elements max {max(abs(np.vdot(p, Mz @ q)) for p in (k1, k0, km) for q in (k1, k0, km) if not ((p is k0 and q is k1) or (p is km and q is k0))):.1e}"
      f"  (theta = 0.3: amplitudes e^(-i theta), e^(+i theta) up to the basis sign)")

# (2) pi-flux reduction
worst24 = worst12 = 0.0; worstper = 0.0
for th in (0.0, 0.4, np.pi / 4, 1.2, np.pi / 2):
    M = M_family(th)
    for _ in range(40):
        k = rng.uniform(-np.pi, np.pi, 3)
        e6 = np.linalg.eigvalsh(H6(k, M))
        ref24 = np.sort(np.concatenate([e6, e6, -e6, -e6])); ref12 = np.sort(np.concatenate([e6, -e6]))
        worst24 = max(worst24, np.abs(np.linalg.eigvalsh(H24(k, M)) - ref24).max())
        worst12 = max(worst12, np.abs(np.linalg.eigvalsh(H12(k, M)) - ref12).max())
        for a in range(3):                                  # spec H6(k + pi e_a) = -spec H6(k)
            kk = k.copy(); kk[a] += np.pi
            worstper = max(worstper, np.abs(np.sort(np.linalg.eigvalsh(H6(kk, M))) - np.sort(-e6)).max())
print(f"(2) pi flux, 200 random (k, theta): |spec H24 - (2 H6 + 2(-H6))| max {worst24:.1e}; "
      f"|spec H12 - (H6 + (-H6))| max {worst12:.1e}; |spec H6(k+pi e_a) + spec H6(k)| max {worstper:.1e}")
P = np.zeros((3, 8, 8))
for a in range(3):
    for i, s in enumerate(CELL8):
        s2 = list(s); s2[a] = (s2[a] + 1) % 2; P[a, i, CELL8.index(tuple(s2))] = eta(a, s)
ac = max(np.abs(P[a] @ P[b] + P[b] @ P[a] - 2 * (a == b) * np.eye(8)).max() for a in range(3) for b in range(3))
print(f"    KS cell matrices P_a: max |{{P_a,P_b}} - 2 delta_ab| = {ac:.0f}; symmetric: {all(np.allclose(p, p.T) for p in P)}; "
      f"Tr(P_x P_y P_z) = {np.trace(P[0] @ P[1] @ P[2]):.0f}")

# (3) zero flux, theta = 0
M0 = M_family(0.0)
def Bvec(k):
    c, s = np.cos(k), np.sin(k); return np.array([c[2] + s[1], c[0] + s[2], c[1] + s[0]])
w = 0.0
for _ in range(200):
    k = rng.uniform(-np.pi, np.pi, 3)
    w = max(w, np.abs(H0(k, M0) - np.sqrt(2) * sum(Bvec(k)[i] * SP1[i] for i in range(3))).max())
G = grid(36); E = np.linalg.eigvalsh(H0(G, M0))
print(f"(3) zero flux, theta=0: |H0 - sqrt2 B.S| max {w:.1e} (200 random k); middle band max |E| on 36^3 grid "
      f"{np.abs(E[:, 1]).max():.1e}; band edges {E[:, 0].min():.6f} .. {E[:, 2].max():.6f} (2 sqrt3 = {2*np.sqrt(3):.6f})")
q4 = np.pi / 4
cands = [np.array(p) * q4 for p in itertools.product((-3, -1, 1, 3), repeat=3)]
nodes = [k for k in cands if np.linalg.norm(Bvec(k)) < 1e-12]
dirs = rng.normal(size=(300, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
print(f"    nodes B(k)=0 among the 64 points with odd multiples of pi/4: {len(nodes)}")
def Jac(k, f, h=1e-6):
    return np.array([(f(k + h * E3[j]) - f(k - h * E3[j])) / (2 * h) for j in range(3)]).T
for k in nodes:
    J = Jac(k, Bvec); svs = np.sqrt(2) * np.linalg.svd(J, compute_uv=False)
    sl = []
    for q in (1e-3, 1e-5):
        sl.append(np.array([np.linalg.eigvalsh(H0(k + q * d, M0)) / q for d in dirs]))
    fast = np.linalg.svd(J)[2][0]
    print(f"    node k/(pi/4) = {np.round(k / q4).astype(int)}: chirality sign det J = {int(np.sign(np.linalg.det(J))):+d}; "
          f"slopes sqrt2*sv(J) = {np.round(svs, 6)}; fast axis ~ {np.round(fast / np.abs(fast).max(), 3)}; "
          f"300 dirs, q=1e-5: lower band slope {sl[1][:,0].min():.4f}..{sl[1][:,0].max():.4f}, "
          f"middle {np.abs(sl[1][:,1]).max():.1e}, upper {sl[1][:,2].min():.4f}..{sl[1][:,2].max():.4f}; "
          f"q=1e-3 vs 1e-5 max diff {np.abs(sl[0]-sl[1]).max():.1e}")
# no other zeros of B: minimize |B| from a grid
Bn = np.linalg.norm(np.stack([np.cos(G[:, 2]) + np.sin(G[:, 1]), np.cos(G[:, 0]) + np.sin(G[:, 2]),
                              np.cos(G[:, 1]) + np.sin(G[:, 0])], 1), axis=1)
far = np.full(len(G), np.inf)
for nd in nodes:
    far = np.minimum(far, np.linalg.norm(((G - nd + np.pi) % (2 * np.pi)) - np.pi, axis=1))
print(f"    on the 36^3 grid, min |B| at distance > 0.3 from the 8 nodes: {Bn[far > 0.3].min():.3f} (> 0: no other nodes)")

# (4) pi flux, theta = 0
def Nmat(k):
    c, s = np.cos(k), np.sin(k)
    return np.array([[0, c[0], s[0]], [s[1], 0, c[1]], [c[2], s[2], 0]])   # rows n_x, n_y, n_z
wr = 0.0; wsv = 0.0
for _ in range(200):
    k = rng.uniform(-np.pi, np.pi, 3); N = Nmat(k)
    wr = max(wr, np.abs(H6(k, M0) - np.sqrt(2) * sum(N[a, i] * np.kron(SIG[a], SP1[i]) for a in range(3) for i in range(3))).max())
    U, lam, Vt = np.linalg.svd(N); lam = lam * np.array([1, 1, np.sign(np.linalg.det(N))])
    ref = np.linalg.eigvalsh(np.sqrt(2) * sum(lam[i] * np.kron(SIG[i], SP1[i]) for i in range(3)))
    wsv = max(wsv, np.abs(np.linalg.eigvalsh(H6(k, M0)) - ref).max())
    detf = np.cos(k).prod() + np.sin(k).prod()
    assert abs(np.linalg.det(N) - detf) < 1e-12
print(f"(4) pi flux, theta=0: |H6 - sqrt2 sum N_ai sigma_a S^i| max {wr:.1e}; spectrum = that of "
      f"sqrt2 sum_i lam_i sigma_i S^i (lam = signed singular values of N) to {wsv:.1e}; det N = cxcycz + sxsysz (checked)")
detg = np.cos(G).prod(1) + np.sin(G).prod(1)
print(f"    det N on the 36^3 grid: min {detg.min():.3f}, max {detg.max():.3f} -> changes sign: zero set is a surface")
# points on the surface: solve det N = 0 along random lines; kernel dimension and dispersion
from scipy.optimize import brentq
res = []
for _ in range(400):
    k = rng.uniform(-np.pi, np.pi, 3); d = rng.normal(size=3); d /= np.linalg.norm(d)
    f = lambda s: np.cos(k + s * d).prod() + np.sin(k + s * d).prod()
    ss = np.linspace(-1, 1, 41); fv = [f(s) for s in ss]
    for i in range(40):
        if fv[i] * fv[i + 1] < 0:
            s0 = brentq(f, ss[i], ss[i + 1], xtol=1e-14); k0 = k + s0 * d
            e = np.sort(np.abs(np.linalg.eigvalsh(H6(k0, M0))))
            gN = Jac(k0, lambda kk: np.array([np.cos(kk).prod() + np.sin(kk).prod()]))[0]
            nrm = gN / np.linalg.norm(gN); t1 = np.cross(nrm, rng.normal(size=3)); t1 /= np.linalg.norm(t1)
            q = 1e-5
            en = np.linalg.eigvalsh(H6(k0 + q * nrm, M0)); et = np.linalg.eigvalsh(H6(k0 + q * t1, M0))
            zn = en[np.argsort(np.abs(en))[:2]] / q; zt = et[np.argsort(np.abs(et))[:2]] / q
            lam = np.linalg.svd(Nmat(k0), compute_uv=False)
            res.append((e[0], e[1], e[2], zn[0], zn[1], np.abs(zt).max(), lam[2], np.linalg.norm(gN) * 2 * np.sqrt(2) / (lam[0] ** 2 + lam[1] ** 2) * lam[0] * lam[1] / (lam[0] * lam[1])))
            break
res = np.array(res)
print(f"    {len(res)} surface points: two smallest |E| of H6 max {res[:,0].max():.1e}, {res[:,1].max():.1e}; third smallest min {res[:,2].min():.3f}")
print(f"    zero modes' slopes along the surface normal: both same sign in {np.mean(np.sign(res[:,3]) == np.sign(res[:,4])):.2f} of points, "
      f"|slope| range {np.abs(res[:,3:5]).min():.3f}..{np.abs(res[:,3:5]).max():.3f}; first-order formula 2sqrt2|grad detN|/(l1^2+l2^2) "
      f"matches to {np.abs(np.abs(res[:,3]) - res[:,7]).max():.1e}; slope along a tangent max {res[:,5].max():.1e}")
