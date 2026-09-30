"""T31 Test A: does u0 = <P>^(1/4) survive putting the formula's 16 tastes in the measure?
SU(3) Wilson gauge action + Ns staggered fields (4 tastes each), exact dense determinant, HMC.
Directions: 0 = time (antiperiodic for fermions), 1..3 space. Links U[mu, x0,x1,x2,x3, 3,3].
"""
import numpy as np, sys, time, json, os

os.environ.setdefault("OMP_NUM_THREADS", "1")

LT = int(os.environ.get("LT", 4)); LS = int(os.environ.get("LS", 4)); L = LS
N = LT * LS**3
DIMS = (LT, LS, LS, LS)
SHIFT = lambda f, mu, s=1: np.roll(f, -s, axis=mu)  # f(x + s*mu)

def dag(A):
    return np.conj(np.swapaxes(A, -1, -2))

def rand_su3(shape, rng, eps=None):
    """random SU(3) (Haar via QR) if eps None, else near-identity."""
    if eps is None:
        Z = rng.normal(size=shape + (3, 3)) + 1j * rng.normal(size=shape + (3, 3))
        Q, R = np.linalg.qr(Z)
        d = np.diagonal(R, axis1=-2, axis2=-1)
        Q = Q * (d / np.abs(d))[..., None, :]
        det = np.linalg.det(Q)
        Q[..., :, 0] = Q[..., :, 0] / det[..., None]
        return Q
    raise NotImplementedError

def herm_traceless(Y):
    H = 0.5 * (Y + dag(Y))
    tr = np.trace(H, axis1=-2, axis2=-1)
    return H - tr[..., None, None] * np.eye(3) / 3.0

def plaq_avg(U):
    s = 0.0
    cnt = 0
    for mu in range(4):
        for nu in range(mu + 1, 4):
            P = U[mu] @ SHIFT(U[nu], mu) @ dag(SHIFT(U[mu], nu)) @ dag(U[nu])
            s += np.real(np.trace(P, axis1=-2, axis2=-1)).sum() / 3.0
            cnt += N
    return s / cnt

def staples(U, mu):
    W = np.zeros_like(U[mu])
    for nu in range(4):
        if nu == mu:
            continue
        # forward: U_nu(x+mu) U_mu(x+nu)^dag U_nu(x)^dag
        W += SHIFT(U[nu], mu) @ dag(SHIFT(U[mu], nu)) @ dag(U[nu])
        # backward: U_nu(x+mu-nu)^dag U_mu(x-nu)^dag U_nu(x-nu)
        W += dag(SHIFT(SHIFT(U[nu], mu), nu, -1)) @ dag(SHIFT(U[mu], nu, -1)) @ SHIFT(U[nu], nu, -1)
    return W

def gauge_action(U, beta):
    return beta * 6 * N * (1.0 - plaq_avg(U))

def gauge_force(U, beta):
    F = np.empty_like(U)
    for mu in range(4):
        X = U[mu] @ staples(U, mu)
        Y = (beta / 3.0) * (X - dag(X)) / (2j)
        F[mu] = herm_traceless(Y)
    return F

# staggered phases eta_mu(x) including antiperiodic BC sign for the time link crossing the boundary
def make_eta():
    x = np.indices(DIMS)  # x[mu] arrays
    eta = np.ones((4,) + DIMS)
    eta[1] = (-1.0) ** (x[0])
    eta[2] = (-1.0) ** (x[0] + x[1])
    eta[3] = (-1.0) ** (x[0] + x[1] + x[2])
    bc = np.ones(DIMS)
    bc[LT - 1, :, :, :] = -1.0
    eta[0] = eta[0] * bc
    return eta
ETA = make_eta()
IDX = np.arange(N).reshape(DIMS)

def build_D(U):
    D = np.zeros((N, 3, N, 3), dtype=complex)
    for mu in range(4):
        s = IDX.ravel()
        t = SHIFT(IDX, mu).ravel()
        Um = U[mu].reshape(N, 3, 3)
        e = ETA[mu].ravel()[:, None, None]
        D[s, :, t, :] += 0.5 * e * Um
        D[t, :, s, :] += -0.5 * e * dag(Um)
    return D.reshape(3 * N, 3 * N)

def ferm_logdet(U, m):
    D = build_D(U) + m * np.eye(3 * N)
    sign, ld = np.linalg.slogdet(D)
    return sign, ld

def ferm_force_unit(U, m):
    """returns Fdet[mu,x] with d ln det /d delta = tr(eps * Y), Y herm-traceless part; plus ln det."""
    D = build_D(U) + m * np.eye(3 * N)
    G = np.linalg.inv(D).reshape(N, 3, N, 3)
    F = np.empty_like(U)
    for mu in range(4):
        s = IDX.ravel()
        t = SHIFT(IDX, mu).ravel()
        A = G[t, :, s, :]      # [n,b,a] = G_{(z+mu,b),(z,a)}
        B = G[s, :, t, :]      # [n,b,a] = G_{(z,b),(z+mu,a)}
        Um = U[mu].reshape(N, 3, 3)
        e = ETA[mu].ravel()[:, None, None]
        Y = 0.5 * e * 1j * (Um @ A + B @ dag(Um))
        F[mu] = herm_traceless(Y).reshape(DIMS + (3, 3))
    return F

def total_force(U, beta, Ns, m):
    F = gauge_force(U, beta)
    if Ns > 0:
        F = F - Ns * ferm_force_unit(U, m)   # dS_f = -Ns dlndet
    return F

def action(U, beta, Ns, m):
    S = gauge_action(U, beta)
    if Ns > 0:
        sign, ld = ferm_logdet(U, m)
        S -= Ns * ld
    return S

def expmi(P, dt):
    w, V = np.linalg.eigh(P)
    return (V * np.exp(1j * dt * w)[..., None, :]) @ dag(V)

def random_mom(rng):
    # P = sum_a p_a T_a, tr T_a T_b = delta_ab, p ~ N(0,1): H hermitian gaussian traceless with <tr P^2> = 8
    Z = rng.normal(size=(4,) + DIMS + (3, 3)) + 1j * rng.normal(size=(4,) + DIMS + (3, 3))
    H = (Z + dag(Z)) / 2.0
    # component variance: for hermitian H=(Z+Z^dag)/2 with iid complex N(0,2): diag var 1, offdiag re/im var 1/2 each -> tr H^2 sums right
    return herm_traceless(H)

def kinetic(P):
    return 0.5 * np.real(np.trace(P @ P, axis1=-2, axis2=-1)).sum()

def leapfrog(U, P, beta, Ns, m, nsteps, dt):
    F = total_force(U, beta, Ns, m)
    P = P - 0.5 * dt * F
    for i in range(nsteps):
        U = expmi(P, dt) @ U if False else np.einsum('...ij,...jk->...ik', expmi(P, dt), U)
        F = total_force(U, beta, Ns, m)
        P = P - (dt if i < nsteps - 1 else 0.5 * dt) * F
    return U, P

def reunit(U):
    # Gram-Schmidt on rows then fix det
    a = U[..., 0, :]
    a = a / np.linalg.norm(a, axis=-1, keepdims=True)
    b = U[..., 1, :] - np.sum(np.conj(a) * U[..., 1, :], axis=-1, keepdims=True) * a
    b = b / np.linalg.norm(b, axis=-1, keepdims=True)
    c = np.conj(np.cross(a, b))
    return np.stack([a, b, c], axis=-2)

def run(beta, Ns, m, ntraj, ntherm, nsteps, dt, seed, cold=False, verbose=True):
    rng = np.random.default_rng(seed)
    if cold:
        U = np.broadcast_to(np.eye(3, dtype=complex), (4,) + DIMS + (3, 3)).copy()
    else:
        U = rand_su3((4,) + DIMS, rng)
    S = action(U, beta, Ns, m)
    plaqs = []; acc = 0; dHs = []
    t0 = time.time()
    for it in range(ntraj + ntherm):
        P = random_mom(rng)
        H0 = kinetic(P) + S
        U1, P1 = leapfrog(U, P, beta, Ns, m, nsteps, dt)
        U1 = reunit(U1)
        S1 = action(U1, beta, Ns, m)
        H1 = kinetic(P1) + S1
        dH = H1 - H0
        if rng.random() < np.exp(-dH):
            U, S = U1, S1; a = 1
        else:
            a = 0
        acc += a; dHs.append(dH)
        pl = plaq_avg(U)
        if it >= ntherm:
            plaqs.append(pl)
        if verbose and (it % 20 == 0 or it == ntraj + ntherm - 1):
            print(f"it {it:4d} P={pl:.5f} dH={dH:+.3f} acc={acc/(it+1):.2f} t={time.time()-t0:.0f}s", flush=True)
    return np.array(plaqs), acc / (ntraj + ntherm), np.array(dHs)

def jack_err(x, nb=10):
    x = np.asarray(x)
    n = len(x) // nb * nb
    blocks = x[:n].reshape(nb, -1).mean(axis=1)
    return blocks.mean(), blocks.std(ddof=1) / np.sqrt(nb)

def tau_int(x, W=None):
    x = np.asarray(x) - np.mean(x)
    n = len(x)
    var = np.dot(x, x) / n
    tau = 0.5
    for t in range(1, n // 4):
        c = np.dot(x[:-t], x[t:]) / (n - t) / var
        tau += c
        if W is None and t > 5 * tau:
            break
    return tau

def check_force(seed=1):
    rng = np.random.default_rng(seed)
    U = rand_su3((4,) + DIMS, rng)
    beta, Ns, m = 6.0, 2, 0.1
    F = total_force(U, beta, Ns, m)
    # finite difference on a few random links with random Hermitian traceless eps
    worst = 0.0
    for trial in range(6):
        mu = rng.integers(4); x = tuple(rng.integers(L, size=4))
        Z = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
        eps = herm_traceless(Z)
        h = 1e-5
        vals = []
        for sgn in (+1, -1):
            U2 = U.copy()
            w, V = np.linalg.eigh(eps)
            R = (V * np.exp(1j * sgn * h * w)) @ dag(V)
            U2[(mu,) + x] = R @ U[(mu,) + x]
            vals.append(action(U2, beta, Ns, m))
        fd = (vals[0] - vals[1]) / (2 * h)
        an = np.real(np.trace(eps @ F[(mu,) + x]))
        rel = abs(fd - an) / max(abs(fd), 1e-8)
        worst = max(worst, rel)
        print(f"  link {mu}{x}: fd={fd:+.6f} analytic={an:+.6f} rel={rel:.2e}")
    return worst

if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "check":
        print("force check (gauge+fermion, Ns=2,m=0.1):")
        w = check_force()
        print("worst rel err", w)
        # gauge only
        rng = np.random.default_rng(3)
        U = rand_su3((4,) + DIMS, rng)
        F = total_force(U, 6.0, 0, 0.1)
        mu, x = 2, (1, 2, 3, 0)
        eps = herm_traceless(rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)))
        h = 1e-5; vals = []
        for sgn in (+1, -1):
            U2 = U.copy(); w_, V = np.linalg.eigh(eps)
            U2[(mu,) + x] = ((V * np.exp(1j * sgn * h * w_)) @ dag(V)) @ U[(mu,) + x]
            vals.append(action(U2, 6.0, 0, 0.1))
        print("gauge-only fd", (vals[0] - vals[1]) / (2 * h), "an", np.real(np.trace(eps @ F[(mu,) + x])))
        # sign/reality of det, and timing
        t = time.time(); s, ld = ferm_logdet(U, 0.1); print("logdet sign", s, "ld", ld, "t", time.time() - t)
        t = time.time(); ferm_force_unit(U, 0.1); print("force t", time.time() - t)
        # energy conservation with small dt
        P = random_mom(rng)
        for dt, ns in ((0.02, 10), (0.01, 20)):
            H0 = kinetic(P) + action(U, 6.0, 2, 0.1)
            U1, P1 = leapfrog(U, P, 6.0, 2, 0.1, ns, dt)
            H1 = kinetic(P1) + action(U1, 6.0, 2, 0.1)
            print(f"dt={dt} n={ns} dH={H1-H0:+.4e}")
    elif mode == "run":
        Ns = int(sys.argv[2]); m = float(sys.argv[3]); ntraj = int(sys.argv[4]); ntherm = int(sys.argv[5])
        nsteps = int(sys.argv[6]); dt = float(sys.argv[7]); seed = int(sys.argv[8])
        cold = len(sys.argv) > 9 and sys.argv[9] == "cold"
        pl, acc, dHs = run(6.0, Ns, m, ntraj, ntherm, nsteps, dt, seed, cold=cold)
        mean, err = jack_err(pl)
        out = dict(Ns=Ns, m=m, L=L, beta=6.0, ntraj=ntraj, ntherm=ntherm, nsteps=nsteps, dt=dt, seed=seed,
                   P_mean=mean, P_err_jack10=err, acc=acc, mean_abs_dH=float(np.mean(np.abs(dHs))),
                   tau_int=float(tau_int(pl)), plaq_series=pl.tolist())
        fn = f"resgeo_LT{LT}_LS{LS}_Ns{Ns}_m{m}_s{seed}.json"
        json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), fn), "w"))
        print(f"RESULT Ns={Ns} m={m} P={mean:.5f} +/- {err:.5f} acc={acc:.2f} |dH|={np.mean(np.abs(dHs)):.3f} tau={out['tau_int']:.1f}")
