"""(a) The letter D_b: frame, unitarity, affine action, covariance, W3 with refinement and SU(2) control."""
import time
from c12chk_lib import *

NP = NF = 0
def rep(ok, msg):
    global NP, NF
    NP += bool(ok); NF += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {msg}", flush=True)

rng = np.random.default_rng(12)
t0 = time.time()
FR = {}
for b in (1, -1):
    y, ns, s = t1_frame(DOUB[b]); FR[b] = y
    herm = all(np.allclose(y[i], y[i].conj().T) for i in range(3))
    alg = all(np.allclose(y[i] @ y[j], (i == j) * np.eye(2) + 1j * sum(EPS[i, j, k] * y[k] for k in range(3))) for i in range(3) for j in range(3))
    # unitary equivalence to Pauli: tau_i = V sigma_i V^dag
    w, V = np.linalg.eigh(y[2]); V = V[:, ::-1]                        # +1 first
    x01 = V.conj().T @ y[0] @ V; ph = np.conj(x01[0, 1]) / abs(x01[0, 1]); V = V @ np.diag([1, ph])  # first run used x01 not conj: spurious FAIL (checker bug)
    peq = all(np.allclose(V.conj().T @ y[i] @ V, PAULI[i]) for i in range(3))
    # compare with C11_check's saved frame (up to sign)
    t = np.load(os.path.join(HERE, '..', 'C11_check', 'tau_frames.npy'))[0 if b == 1 else 1]
    same = min(max(np.abs(y[i] - sg * t[i]).max() for i in range(3)) for sg in (1, -1))
    rep(ns == 1 and herm and alg and peq,
        f"a1 D{'+' if b>0 else '-'}: covariance-compatible T1 frame space (U_g T_l U_g^T = sum_j M_jl T_j) has dim {ns}; Hermitian, "
        f"tau_i tau_j = d_ij + i eps tau_k, unitarily equivalent to Pauli; agrees with C11_check frame to {same:.1e}")

# affine action: R^T(k*+q) + pi lam = k* + R^T q  (mod 2 pi), for all 24 and both fixed points
err = 0.0
for g in GRP:
    for c in (KST, -KST):
        for _ in range(5):
            q = rng.uniform(-np.pi, np.pi, 3)
            err = max(err, np.abs(wrapk(g['M'].T @ (c + q) + np.pi * g['lam'] - c - g['M'].T @ q)).max())
sinerr = max(np.abs(np.sin(g['M'].T @ q) - g['M'].T @ np.sin(q)).max() + abs(np.cos(g['M'].T @ q).sum() - np.cos(q).sum()) for g in GRP for q in rng.uniform(-9, 9, (20, 3)))
rep(err < 1e-12 and sinerr < 1e-12,
    f"a2 induced action is exactly q -> R^T q mod 2pi (affine shift absorbed because R^T k* + pi lam = k* mod 2pi), err {err:.1e}; "
    f"sin(R^T q) = R^T sin q and sum cos invariant (signed permutations), err {sinerr:.1e}")

K = rng.uniform(-np.pi, np.pi, (200, 3))
for b in (1, -1):
    f = make_Db(b, frame=FR[b]); U = f(K)
    uerr = np.abs(U @ np.conj(np.swapaxes(U, 1, 2)) - np.eye(12)).max()
    perr = np.abs(f(K + 2 * np.pi * rng.integers(-2, 3, (200, 3))) - U).max()
    cerr = 0.0
    for g in GRP:
        Kp = K @ g['M'] + np.pi * g['lam']      # rows: R^T k + pi lam
        cerr = max(cerr, np.abs(g['U'][None] @ f(Kp) @ g['U'].T[None] - U).max())
    # with the frame sign reversed / a wrongly oriented frame: still covariant (sign is a scalar); a non-T1 frame breaks it
    bad = make_Db(b, frame=np.array([FR[b][1], FR[b][0], FR[b][2]]))
    berr = max(np.abs(g['U'][None] @ bad(K @ g['M'] + np.pi * g['lam']) @ g['U'].T[None] - bad(K)).max() for g in GRP)
    rep(uerr < 1e-13 and perr < 1e-12 and cerr < 1e-12 and berr > 0.1,
        f"a3 D{'+' if b>0 else '-'}: unitary ({uerr:.1e}), 2pi-periodic ({perr:.1e}), A1-covariant under all 24 lifts ({cerr:.1e}); "
        f"negative control: swapping tau_x,tau_y breaks covariance ({berr:.2f})")

# W3 refinement
print("   W3 refinement (midpoint grid, central differences h=1e-5):")
res = {}
for N in (8, 16, 24, 32):
    a = W3(make_Db(1, frame=FR[1]), N); bm = W3(make_Db(-1, frame=FR[-1]), N); c = W3(pauli_ctrl(center=KST), N)
    res[N] = (a, bm, c); print(f"   N={N:2d}: W3(D+)={a.real:+.8f}  W3(D-)={bm.real:+.8f}  W3(SU2 ctrl)={c.real:+.8f}  imag<={max(abs(a.imag),abs(bm.imag)):.0e}  ({time.time()-t0:.0f}s)", flush=True)
a, bm, c = res[32]
rep(abs(abs(a.real) - 1) < 1e-6 and abs(a - bm) < 1e-8 and abs(a - c) < 1e-6,
    f"a4 |W3(D_b)| = 1 with grid convergence 8->32, equal to the 2x2 SU(2) degree-one control (N=32 err {abs(abs(a.real)-1):.1e})")
# m scan and products
ms = {m: W3(make_Db(1, m=m, frame=FR[1]), 64 if m in (1.2, 2.8) else 24).real for m in (1.2, 2.0, 2.8, 3.5, 4.0, 0.5, -2.0)}  # first run used N=24 for all: m=1.2,2.8 unconverged (gap m-1, 3-m = 0.2)
print("   W3(D+) vs m (N=24; N=64 for m=1.2,2.8):", {k: round(v, 5) for k, v in ms.items()})
rep(all(abs(ms[m] - ms[2.0]) < 1e-2 for m in (1.2, 2.8)) and abs(ms[3.5]) < 1e-2 and abs(ms[4.0]) < 1e-3,
    "a5 W3 constant on m in (1,3) and 0 for m > 3 (N=64 for m=1.2, 2.8; tol 1e-2). Not claimed by C12 but seen: m=0.5 gives -2, m=-2 gives +1 (Wilson-type pattern)")
D1 = make_Db(1, frame=FR[1]); Dm = make_Db(-1, frame=FR[-1]); D1i = make_Db(1, frame=FR[1], inv=True)
prods = {'D+D-': W3(word([D1, Dm]), 24), 'D+D+^-1': W3(word([D1, D1i]), 24),
         'A0 D+ A0^-1': W3(word([lambda K: np.broadcast_to(A0, (len(np.atleast_2d(K)), 12, 12)), D1,
                                 lambda K: np.broadcast_to(np.linalg.inv(A0), (len(np.atleast_2d(K)), 12, 12))]), 24),
         'D+ S': W3(word([D1, S_batch]), 24), 'D+^-1': W3(D1i, 24)}
print("   products (N=24):", {k: round(v.real, 6) for k, v in prods.items()})
w = res[32][0].real
rep(abs(prods['D+D-'] - 2 * w) < 1e-3 and abs(prods['D+D+^-1']) < 1e-9 and abs(prods['A0 D+ A0^-1'] - w) < 1e-3
    and abs(prods['D+ S'] - w) < 1e-3 and abs(prods['D+^-1'] + w) < 1e-3, "a6 additivity: D+D- = 2w, D+D+^-1 = 0, conjugation = w, D+S = w, inverse = -w")
print(f"TOTAL PASS={NP} FAIL={NF} ({time.time()-t0:.0f}s)")
