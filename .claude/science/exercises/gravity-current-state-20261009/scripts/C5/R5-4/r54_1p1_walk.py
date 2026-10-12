"""C5 R5-4 (2): 1+1 analogue of LRL timelike-link laws (an analogue only, not L7).

Lattice L = diag(sqrt k, 1) Z^2, Q(n) = -k n0^2 + n1^2 (anisotropic over Q), Gamma = SO+(Q,Z) = <g>,
g = [[2,1],[3,2]] for k = 3 (eta0 = arccosh 2), g = [[8,3],[21,8]] for k = 7 (eta0 = arccosh 8).
Links (x, d_n), d_n = g^n e0 (one future-timelike orbit, trivial stabilizer). A plane wave e^{i q.x} on the
future shell H_m^+: q = (-sqrt(k) m cosh th, m sinh th) in dual lattice coords, so q.d_n = -sqrt(k) m cosh(th - n eta0).
Covariance reduces every translation- and Gamma-covariant banded link law to a recurrence in n whose
coefficients depend on the phases phi_n = q.(g^n a) (a fixed lattice vectors).

(a) phase identity q.d_n = -sqrt(k) m cosh(th - n eta0) (exact integer d_n, 60 digits).
(b) two-term scalar law c0 f_n + (c1 e^{i q.g^n a} + c2 e^{i q.g^n b}) f_{n+1} = 0:
    forward and backward growth exponents of |f_n| along shell points vs Jensen's value
    chi = log|c0| - log max(|c1|,|c2|); two-sided decay needs chi_+ < 0 and chi_- < 0, but chi_- = -chi_+.
(c) coined unitary link walk (W psi)_n = e^{-i phi_n}[P+ C psi_{n-1} + P- C psi_{n+1}], C = rotation(zeta):
    eigenvalue-1 (law phi = W phi) <=> SU(1,1) transfer T_n = (1/c)[[e^{-i phi_n}, -s], [-s, e^{i phi_n}]].
    An l^2 solution at (m, th) <=> the +infinity-decaying and -infinity-decaying directions coincide.
    Both directions lie on the invariant circle |z| = 1 of CP^1, so the mismatch is a real angle.
    An exact covariant mass shell at m needs mismatch = 0 for a.e. th in a fundamental interval [0, eta0).
"""
import mpmath as mp, sys
mp.mp.dps = 80
def setup(k):
    if k == 3: g = ((2, 1), (3, 2))
    elif k == 7: g = ((8, 3), (21, 8))
    a0 = g[0][0]; return g, mp.acosh(a0)
def mul(g, v): return (g[0][0]*v[0] + g[0][1]*v[1], g[1][0]*v[0] + g[1][1]*v[1])
def inv(g): return ((g[1][1], -g[0][1]), (-g[1][0], g[0][0]))
def orbit(g, v, N):
    """dict n -> g^n v, exact integers, |n| <= N"""
    out = {0: v}; w = v
    for n in range(1, N+1): w = mul(g, w); out[n] = w
    w = v; gi = inv(g)
    for n in range(1, N+1): w = mul(gi, w); out[-n] = w
    return out
def qvec(k, m, th): return (-mp.sqrt(k)*m*mp.cosh(th), m*mp.sinh(th))
def dot(q, v): return q[0]*v[0] + q[1]*v[1]

def part_a(k):
    g, eta = setup(k); D = orbit(g, (1, 0), 25)
    worst = 0
    for m in (mp.mpf('0.3'), mp.mpf('1.7')):
        for th in (mp.mpf('0.2'), mp.mpf('-1.1')):
            q = qvec(k, m, th)
            for n in (-25, -7, 0, 3, 25):
                exact = -mp.sqrt(k)*m*mp.cosh(th - n*eta)
                worst = max(worst, abs(dot(q, D[n]) - exact)/abs(exact))
    print(f"(a) k={k}: max rel. error of q.d_n = -sqrt(k) m cosh(th - n eta0) over test points: {mp.nstr(worst, 3)}")

def part_b(k, N=60):
    g, eta = setup(k)
    a, b = (0, 1), (1, 1)
    A, Bv = orbit(g, a, N+1), orbit(g, b, N+1)
    c0, c1, c2 = mp.mpf(1), mp.mpf('0.9'), mp.mpf('0.5')
    chi = mp.log(abs(c0)) - mp.log(max(abs(c1), abs(c2)))
    print(f"(b) k={k}, two-term law c0={c0}, c1={c1}, c2={c2}, a={a}, b={b}; Jensen chi = {mp.nstr(chi, 5)}")
    for m, th in ((0.4, 0.1), (0.4, 0.9), (1.3, 0.37), (2.5, 1.2)):
        q = qvec(k, mp.mpf(m), mp.mpf(th))
        def r(n):  # |f_{n+1}/f_n|
            return abs(c0)/abs(c1*mp.expjpi(dot(q, A[n])/mp.pi) + c2*mp.expjpi(dot(q, Bv[n])/mp.pi))
        fwd = sum(mp.log(r(n)) for n in range(0, N))/N            # (1/N) log|f_N/f_0|
        bwd = -sum(mp.log(r(n)) for n in range(-N, 0))/N          # (1/N) log|f_{-N}/f_0|
        print(f"    m={m}, th={th}: chi_+ (forward) = {mp.nstr(fwd, 4)}, chi_- (backward) = {mp.nstr(bwd, 4)}, chi_+ + chi_- = {mp.nstr(fwd+bwd, 3)}")

def mismatch(k, m, th, zeta, N, D, nc=0):
    """angle between the +inf-decaying and -inf-decaying directions at v_0 (on the circle |z|=1)."""
    c, s = mp.cos(zeta), mp.sin(zeta)
    q = qvec(k, m, th)
    def T(n):
        ph = dot(q, D[n]); e = mp.expjpi(-ph/mp.pi)
        return mp.matrix([[e/c, -s/c], [-s/c, mp.conj(e)/c]])
    Mp = mp.eye(2)
    for n in range(nc, nc+N): Mp = T(n)*Mp           # v_{nc+N} = Mp v_nc
    Mm = mp.eye(2)
    for n in range(1, N+1): Mm = mp.inverse(T(nc-n))*Mm   # v_{nc-N} = Mm v_nc
    def decaying(M):
        U, S, V = mp.svd_c(M)
        v = V.H[:, 1] if S[1] < S[0] else V.H[:, 0]   # right singular vector of smallest singular value
        return v, min(S[0], S[1])
    up, sp = decaying(Mp); um, sm = decaying(Mm)
    zp, zm = up[1]/up[0], um[1]/um[0]
    ang = mp.arg(zp/zm)
    lyap = -mp.log(sp)/N
    return ang, abs(zp), abs(zm), lyap

def part_c(k, zeta, ms, ngrid=240, N=24):
    g, eta = setup(k)
    D = orbit(g, (1, 0), N+2)
    print(f"(c) k={k}, eta0={mp.nstr(eta,6)}, coin angle zeta={zeta}, truncation N={N}, theta grid {ngrid} on [0, eta0)")
    for m in ms:
        angs = []; lyaps = []; rad = []
        for i in range(ngrid):
            th = eta*i/ngrid
            a, rp, rm, ly = mismatch(k, mp.mpf(m), th, mp.mpf(zeta), N, D)
            angs.append(float(a)); lyaps.append(float(ly)); rad.append(max(abs(float(rp)-1), abs(float(rm)-1)))
        sc = sum(1 for i in range(ngrid) if angs[i]*angs[(i+1) % ngrid] < 0 and abs(angs[i]-angs[(i+1) % ngrid]) < 3.0)
        fr = [sum(1 for a in angs if abs(a) < e)/ngrid for e in (0.3, 0.1, 0.03, 0.01)]
        print(f"    m={m}: Lyapunov (per step) min/mean = {min(lyaps):.3f}/{sum(lyaps)/len(lyaps):.3f}; max ||z|-1| = {max(rad):.1e}; "
              f"zero crossings of mismatch in [0,eta0): {sc}; fraction |mismatch|<eps for eps=0.3,0.1,0.03,0.01: "
              + ", ".join(f"{x:.3f}" for x in fr) + f"; min |mismatch| = {min(abs(a) for a in angs):.2e}, max = {max(abs(a) for a in angs):.2f}")
    # covariance check: th and th + eta0 give the same mismatch up to truncation (window shift by one site)
    D2 = orbit(g, (1, 0), N+4)
    a1 = mismatch(k, mp.mpf(ms[0]), mp.mpf('0.3'), mp.mpf(zeta), N, D2, 0)[0]
    a2 = mismatch(k, mp.mpf(ms[0]), mp.mpf('0.3') + eta, mp.mpf(zeta), N, D2, 1)[0]
    print(f"    Gamma check (evaluated at the shifted site): mismatch(th=0.3, site 0) = {mp.nstr(a1, 12)}, mismatch(th=0.3+eta0, site 1) = {mp.nstr(a2, 12)}, diff = {mp.nstr(abs(a1-a2), 3)}")

if __name__ == "__main__":
    for k in (3, 7): part_a(k)
    part_b(3); part_b(7)
    part_c(3, 0.6, (0.2, 0.5, 1.0))
    part_c(3, 1.2, (0.5,))
    part_c(7, 0.6, (0.2, 0.5))
    # truncation stability: same m, finer grid and larger N
    part_c(3, 0.6, (0.5,), ngrid=600, N=34)
