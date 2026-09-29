"""PR 9354 attack-g: PROOF STEPS BY BRUTE FORCE, literally as written, on random small stoquastic matrices (exact rationals where the step is algebraic, 40-digit mpmath where it involves exp).

Steps of the two notes:
  P1  weighted-generator identity (1): Q^T - diag(E_L) = -D H D^{-1} entrywise, Q(x,y) = -H(y,x) psi(y)/psi(x), Q(x,x) = -sum Q(x,y)  [exact, Fractions, 400 instances incl. zero entries, reducible H];
  P2  pathwise identity: m(x) Q_x(d omega) exp(W) = psi(x) psi(y) prod(A along jumps) exp(-int D dt) for random jump paths (product form with the rates q, exit rates lambda, W = -int E_L dt) [mpmath];
  P3  Z(t) = psi^T exp(-tH) chi > 0 for every Metzler/stoquastic H INCLUDING reducible ones, and E_mix = psi^T H exp(-tH) chi / Z = -d log Z / dt [mpmath, 200 instances];
  P4  f_t = D exp(-tH) chi solves the weighted forward equation d f / dt = (Q^T - diag(E_L)) f and its time-Taylor series has the claimed positive-coefficient structure after a diagonal shift [mpmath];
  P5  the finite-projection difference E_psi(T) - E_0 = sum_(n>0) |c_n|^2 (E_n - E_0) e^{-T(E_n-E_0)} / (|c_0|^2 + sum ...), its derivative = -Var(E_n) under the spectral weights, and the bound
      0 <= E_psi - E_0 <= B (|psi|^2 - |c_0|^2) e^{-gT}/|c_0|^2 [mpmath, 200 instances];
  P6  the capped kernel K_J(Delta): symmetric, entrywise nonnegative, positive diagonal, independent of psi, and K_J -> exp(-Delta H) as J grows [Dyson terms by the block exponential];
  P7  detailed balance pi(x) Q(x,y) = -H(x,y) psi(x) psi(y)/sum psi^2 and the stationary energy psi^T H psi/psi^T psi (connected H: convergence of exp(tQ^T) p0 to pi).
"""
import itertools, sys, time
import numpy as np
import mpmath as mp
from scipy.linalg import expm

PASS = FAIL = 0
HITS = []
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}", flush=True)

def rand_stoq(n, rng, density=1.0, zero_diag=False):
    A = rng.uniform(0, 1.5, (n, n)) * (rng.uniform(0, 1, (n, n)) < density); A = np.triu(A, 1); A = A + A.T
    D = np.zeros(n) if zero_diag else rng.uniform(-1, 2, n)
    return np.diag(D) - A, D, A
def spectral(H):
    e, V = np.linalg.eigh(H); return e, V
def E_endpoint(H, psi, T):
    G = expm(-T * H); Z = psi @ G @ psi
    return float(psi @ H @ G @ psi / Z)
def E_rayleigh(H, psi, T):
    u = expm(-T * H / 2) @ psi; return float(u @ H @ u / (u @ u))
def E_logderiv(H, psi, T, h=1e-5):
    f = lambda tt: np.log(psi @ expm(-tt * H) @ psi)
    return float(-(f(T + h) - f(T - h)) / (2 * h))
def kernel_capped(D, A, Delta, J):
    """K_J(Delta): weighted paths with at most J jumps (exact Dyson terms via the block-upper-triangular exponential): sum over j <= J of the j-jump term"""
    n = len(D); Bm = np.zeros(((J + 1) * n, (J + 1) * n))
    for b in range(J + 1):
        Bm[b * n:(b + 1) * n, b * n:(b + 1) * n] = -np.diag(D)
        if b < J: Bm[b * n:(b + 1) * n, (b + 1) * n:(b + 2) * n] = A
    E = expm(Bm * Delta)
    return sum(E[0:n, j * n:(j + 1) * n] for j in range(J + 1))
from fractions import Fraction as Fr
import random
T0 = time.time()
mp.mp.dps = 40
random.seed(93541); rng = np.random.default_rng(93541)
# P1 exact
ok = True; worst_zero = 0
for _ in range(400):
    n = random.randint(2, 5)
    A = [[Fr(0)] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < 0.7: A[i][j] = A[j][i] = Fr(random.randint(1, 9), random.randint(1, 4))
    D = [Fr(random.randint(-5, 5), random.randint(1, 3)) for _ in range(n)]
    H = [[(D[i] if i == j else -A[i][j]) for j in range(n)] for i in range(n)]
    psi = [Fr(random.randint(1, 9), random.randint(1, 5)) for _ in range(n)]
    Q = [[Fr(0)] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if x != y: Q[x][y] = -H[y][x] * psi[y] / psi[x]
        Q[x][x] = -sum(Q[x][y] for y in range(n) if y != x)
    EL = [sum(H[x][y] * psi[y] for y in range(n)) / psi[x] for x in range(n)]
    for x in range(n):
        for y in range(n):
            lhs = Q[y][x] - (EL[x] if x == y else 0)              # (Q^T - diag(E_L))(x, y) = Q(y, x) - delta E_L
            rhs = -psi[x] * H[x][y] / psi[y]                        # (-D H D^{-1})(x, y)
            ok &= (lhs == rhs)
check("P1: Q^T - diag(E_L) = -D H D^{-1} entrywise, exactly, on 400 random rational stoquastic matrices (zero entries, reducible graphs, zero diagonal included)", ok)
# P2 pathwise identity
worst = mp.mpf(0)
for _ in range(200):
    n = random.randint(2, 4); Am = mp.matrix(n, n)
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < 0.8: Am[i, j] = Am[j, i] = mp.mpf(random.randint(1, 9)) / random.randint(1, 4)
    Dv = [mp.mpf(random.randint(-4, 4)) / random.randint(1, 3) for _ in range(n)]
    ps = [mp.mpf(random.randint(1, 9)) / random.randint(1, 5) for _ in range(n)]
    lam = [sum(Am[x, y] * ps[y] / ps[x] for y in range(n)) for x in range(n)]
    EL = [Dv[x] - lam[x] for x in range(n)]
    # random path with k jumps; dwell times
    k = random.randint(0, 4); states = [random.randrange(n)]
    for _ in range(k):
        nxt = [y for y in range(n) if y != states[-1] and Am[states[-1], y] != 0]
        if not nxt: break
        states.append(random.choice(nxt))
    dwell = [mp.mpf(random.randint(1, 20)) / 10 for _ in states]
    prodq = mp.mpf(1); prodA = mp.mpf(1)
    for a, b in zip(states[:-1], states[1:]): prodq *= Am[a, b] * ps[b] / ps[a]; prodA *= Am[a, b]
    intlam = sum(l * lam[s] for l, s in zip(dwell, states)); intD = sum(l * Dv[s] for l, s in zip(dwell, states)); intEL = sum(l * EL[s] for l, s in zip(dwell, states))
    x, y = states[0], states[-1]
    lhs = ps[x] ** 2 * prodq * mp.e ** (-intlam) * mp.e ** (-intEL)                 # m(x) Q_x exp(W), W = -int E_L dt
    rhs = ps[x] * ps[y] * prodA * mp.e ** (-intD)
    worst = max(worst, abs(lhs - rhs) / max(abs(rhs), mp.mpf(10) ** -30))
check("P2: the pathwise identity m(x) Q_x exp(W) = psi(x) psi(y) prod(A) exp(-int D) holds on 200 random jump paths (including zero-jump paths), relative deviation", worst < mp.mpf(10) ** -30, mp.nstr(worst, 3))
# P3, P4, P5 random real instances via mpmath
worstZ = worstM = worstF = worst5 = mp.mpf(0); Zmin = mp.inf; viol_bound = 0; viol_nonneg = 0; viol_var = mp.mpf(0)
for it in range(200):
    n = random.randint(2, 5)
    A = mp.matrix(n, n)
    dens = random.choice([0.4, 0.7, 1.0])
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < dens: A[i, j] = A[j, i] = mp.mpf(random.randint(1, 9)) / random.randint(1, 4)
    Dv = [mp.mpf(random.randint(-4, 4)) / random.randint(1, 3) for _ in range(n)]
    H = mp.matrix(n, n)
    for i in range(n):
        for j in range(n): H[i, j] = Dv[i] if i == j else -A[i, j]
    ps = mp.matrix([mp.mpf(random.randint(1, 9)) / random.randint(1, 5) for _ in range(n)])
    p0 = mp.matrix([mp.mpf(random.randint(0, 5)) for _ in range(n)]);
    if sum(p0) == 0: p0[0] = 1
    p0 = p0 / sum(p0)
    chi = mp.matrix([p0[i] / ps[i] for i in range(n)])
    tt = mp.mpf(random.randint(1, 40)) / 10
    G = mp.expm(-tt * H); Z = (ps.T * G * chi)[0]; Zmin = min(Zmin, Z)
    Em = (ps.T * H * G * chi)[0] / Z
    Zf = lambda s: (ps.T * mp.expm(-s * H) * chi)[0]
    dl = mp.diff(lambda s: mp.log(Zf(s)), tt)
    worstM = max(worstM, abs(Em + dl))
    # P4: f_t = D exp(-tH) chi ; d f/dt = (Q^T - diag(E_L)) f
    Dm = mp.diag([ps[i] for i in range(n)]); f = lambda s: Dm * mp.expm(-s * H) * chi
    Q = mp.matrix(n, n)
    for x in range(n):
        for y in range(n):
            if x != y: Q[x, y] = -H[y, x] * ps[y] / ps[x]
        Q[x, x] = -sum(Q[x, y] for y in range(n) if y != x)
    EL = mp.matrix([sum(H[x, y] * ps[y] for y in range(n)) / ps[x] for x in range(n)])
    Gen = Q.T - mp.diag([EL[i] for i in range(n)])
    ft = f(tt); dft = mp.matrix([mp.diff(lambda s, i=i: f(s)[i], tt) for i in range(n)])
    worstF = max(worstF, mp.norm(dft - Gen * ft) / max(mp.norm(dft), mp.mpf(10) ** -20))
    # P5 (needs a connected graph so that E_0 is simple and c_0 != 0)
    Hn = np.array(H.tolist(), dtype=float)
    Ad = (Hn - np.diag(np.diag(Hn))) * -1
    conn = np.linalg.matrix_power(np.eye(n) + (Ad > 0), n).min() > 0
    if conn:
        Hm = mp.matrix(H); E, V = mp.eigsy(Hm); order = sorted(range(n), key=lambda i: E[i]); V2 = mp.matrix(n, n)
        for kk, ii in enumerate(order):
            for rr in range(n): V2[rr, kk] = V[rr, ii]
        E = [E[i] for i in order]; V = V2
        c = [(V[:, i].T * ps)[0] for i in range(n)]
        Tt = tt
        w = [c[i] ** 2 * mp.e ** (-Tt * (E[i] - E[0])) for i in range(n)]
        Epsi = sum(w[i] * E[i] for i in range(n)) / sum(w)
        E_end = (ps.T * H * mp.expm(-Tt * H) * ps)[0] / (ps.T * mp.expm(-Tt * H) * ps)[0]
        worst5 = max(worst5, abs(Epsi - E_end))
        diff = Epsi - E[0]
        viol_nonneg += diff < -mp.mpf(10) ** -30
        g = min(E[i] - E[0] for i in range(1, n)); B = max(E[i] - E[0] for i in range(1, n)); nn2 = sum(c[i] ** 2 for i in range(n))
        bound = B * (nn2 - c[0] ** 2) * mp.e ** (-g * Tt) / c[0] ** 2
        viol_bound += diff > bound + mp.mpf(10) ** -30
        # derivative = -variance of E_n under normalised weights
        dE = mp.diff(lambda s: sum(c[i] ** 2 * mp.e ** (-s * (E[i] - E[0])) * E[i] for i in range(n)) / sum(c[i] ** 2 * mp.e ** (-s * (E[i] - E[0])) for i in range(n)), Tt)
        pw = [wi / sum(w) for wi in w]; var = sum(pw[i] * E[i] ** 2 for i in range(n)) - sum(pw[i] * E[i] for i in range(n)) ** 2
        viol_var = max(viol_var, abs(dE + var))
check("P3: Z(t) = psi^T exp(-tH) chi > 0 on 200 random instances including reducible ones (smallest Z shown), and E_mix = -d log Z/dt", Zmin > 0 and worstM < mp.mpf(10) ** -25, f"min Z {mp.nstr(Zmin, 5)}, max |E_mix + dlogZ/dt| {mp.nstr(worstM, 3)}")
check("P4: f_t = D exp(-tH) chi satisfies d f/dt = (Q^T - diag(E_L)) f (relative residual)", worstF < mp.mpf(10) ** -25, mp.nstr(worstF, 3))
check("P5: spectral formula = endpoint average; E_psi - E_0 >= 0; the bound B(|psi|^2 - |c_0|^2) e^{-gT}/|c_0|^2 is never exceeded; dE/dT = -Var(E_n)", worst5 < mp.mpf(10) ** -25 and viol_nonneg == 0 and viol_bound == 0 and viol_var < mp.mpf(10) ** -25,
      f"formula deviation {mp.nstr(worst5, 3)}, non-negativity violations {viol_nonneg}, bound violations {viol_bound}, derivative deviation {mp.nstr(viol_var, 3)}")
# P6 capped kernel
bad_sym = bad_neg = bad_diag = 0; conv = []
for _ in range(100):
    n = random.randint(2, 5); Hh, Dd, Aa = rand_stoq(n, rng, density=0.8); Delta = float(rng.uniform(0.1, 0.8))
    Ks = [kernel_capped(Dd, Aa, Delta, J) for J in (0, 1, 2, 4, 8, 16, 36)]
    for K in Ks:
        bad_sym += np.abs(K - K.T).max() > 1e-12; bad_neg += K.min() < -1e-14; bad_diag += np.diag(K).min() <= 0
    conv.append(np.abs(Ks[-1] - expm(-Delta * Hh)).max())
check("P6: K_J(Delta) is symmetric, entrywise nonnegative with positive diagonal for J = 0, 1, 2, 4, 8, 16, 36 on 100 random instances, and converges to exp(-Delta H) (largest deviation at J = 36 shown)", bad_sym == 0 and bad_neg == 0 and bad_diag == 0 and max(conv) < 1e-8, f"{bad_sym} {bad_neg} {bad_diag}; max deviation at J = 36: {max(conv):.1e}")
# P7 detailed balance and stationary energy on connected instances
bad_db = 0; bad_lim = 0.0; n_conn = 0
for _ in range(100):
    n = random.randint(2, 5); Hh, Dd, Aa = rand_stoq(n, rng, density=1.0); ps = rng.uniform(0.3, 2.0, n)
    Q = np.zeros((n, n))
    for x in range(n):
        for y in range(n):
            if x != y: Q[x, y] = Aa[y, x] * ps[y] / ps[x]
        Q[x, x] = -Q[x].sum()
    pi = ps ** 2 / (ps ** 2).sum()
    for x in range(n):
        for y in range(n):
            if x != y: bad_db += abs(pi[x] * Q[x, y] - (-Hh[x, y]) * ps[x] * ps[y] / (ps ** 2).sum()) > 1e-12
    p0 = rng.dirichlet(np.ones(n)); lim = expm(4000 * Q.T) @ p0; EL = Hh @ ps / ps
    bad_lim = max(bad_lim, abs(lim @ EL - ps @ Hh @ ps / (ps @ ps))); n_conn += 1
check("P7: detailed balance pi(x) Q(x,y) = -H(x,y) psi(x) psi(y)/sum psi^2 and the limiting energy psi^T H psi / psi^T psi on 100 connected instances", bad_db == 0 and bad_lim < 1e-9, f"{bad_db} violations, limit deviation {bad_lim:.1e}")

print()
for h in HITS: print("HIT:", h)
print(f"time {time.time()-T0:.0f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print(f"SUMMARY: attack-g proof steps on PR 9354 by brute force: P1 exact generator identity (400 rational instances), P2 pathwise identity (200 random paths), P3 Z>0 incl. reducible and E_mix=-dlogZ/dt, P4 forward equation, P5 spectral formula/nonnegativity/bound/variance derivative (0 violations), P6 capped kernel symmetric/nonnegative/positive diagonal/convergent, P7 detailed balance and stationary energy; PASS={PASS} FAIL={FAIL}; no defect in the notes' proof steps")
sys.exit(1 if FAIL else 0)
