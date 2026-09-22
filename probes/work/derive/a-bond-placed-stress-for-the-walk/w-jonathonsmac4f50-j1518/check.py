"""a-bond-placed-stress-for-the-walk, attempt a3 (w-jonathonsmac4f50-j1518).  Exact: fractions, Gaussian rationals, sympy.

Walk (block 54, identity frame): H = sum_a sigma_a S_a, S_a = (T_a - T_a^dag)/(2i), (T_a psi)(x) = psi(x + e_a), i dpsi/dt = H psi.
Momentum density pi_j(x) = Re psi^dag(x)(S_j psi)(x).  Bond strain B_a^j(x) on the bond x -> x + e_a, coupled as a relabelling's
deformation (blocks 63, 64): H[B] = H + sum_aj sigma_a (1/2){C_a[B_a^j], S_j}, (C_a[v]f)(x) = (1/2)[v(x) f(x+e_a) + v(x-e_a) f(x-e_a)].
"""
import itertools
import random
from fractions import Fraction as F

import sympy as sp

RESULTS = []


def want(label, ok, detail=""):
    RESULTS.append((label, bool(ok)))
    print(("PASS " if ok else "FAIL ") + label + ((" :: " + str(detail)) if detail != "" else ""), flush=True)


class G:
    """Gaussian rational re + i im, exact."""
    __slots__ = ("re", "im")

    def __init__(self, re=0, im=0):
        self.re = F(re); self.im = F(im)

    def __add__(self, o):
        o = gg(o); return G(self.re + o.re, self.im + o.im)
    __radd__ = __add__

    def __sub__(self, o):
        o = gg(o); return G(self.re - o.re, self.im - o.im)

    def __rsub__(self, o):
        return gg(o) - self

    def __mul__(self, o):
        o = gg(o); return G(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)
    __rmul__ = __mul__

    def __neg__(self):
        return G(-self.re, -self.im)

    def conj(self):
        return G(self.re, -self.im)

    def __eq__(self, o):
        o = gg(o); return self.re == o.re and self.im == o.im

    def __hash__(self):
        return hash((self.re, self.im))

    def __repr__(self):
        return f"({self.re}{'+' if self.im >= 0 else '-'}{abs(self.im)}i)"


def gg(x):
    return x if isinstance(x, G) else G(x, 0)


I = G(0, 1)
MINUS_I_HALF = G(0, F(-1, 2))                                        # 1/(2i)


def sig(a, u):
    u0, u1 = u
    if a == 0: return (u1, u0)
    if a == 1: return (-I * u1, I * u0)
    return (u0, -u1)


def inner(u, v):
    return u[0].conj() * v[0] + u[1].conj() * v[1]


class Torus:
    def __init__(self, dims):
        self.dims = dims
        self.sites = list(itertools.product(*[range(d) for d in dims]))
        self.index = {x: n for n, x in enumerate(self.sites)}
        self.N = len(self.sites)

    def nb(self, n, a, k):
        x = list(self.sites[n]); x[a] = (x[a] + k) % self.dims[a]
        return self.index[tuple(x)]

    def shift(self, f, a, k=1):
        return [f[self.nb(n, a, k)] for n in range(self.N)]

    def S(self, f, j):
        fp, fm = self.shift(f, j, 1), self.shift(f, j, -1)
        return [((fp[n][0] - fm[n][0]) * MINUS_I_HALF, (fp[n][1] - fm[n][1]) * MINUS_I_HALF) for n in range(self.N)]

    def H(self, f):
        out = [(G(), G()) for _ in range(self.N)]
        for a in range(3):
            Sa = self.S(f, a)
            out = [(o[0] + s[0], o[1] + s[1]) for o, s in zip(out, (sig(a, v) for v in Sa))]
        return out

    def J(self, psi, a, j, phi=None):
        """bond current of pi_j on the bond x -> x + e_a (exact, a Fraction per site)."""
        if phi is None: phi = self.S(psi, j)
        psa, pha = self.shift(psi, a), self.shift(phi, a)
        return [F(1, 2) * (inner(psa[n], sig(a, phi[n])) + inner(pha[n], sig(a, psi[n]))).re for n in range(self.N)]

    def back(self, f, a):
        fm = self.shift(f, a, -1)
        return [f[n] - fm[n] for n in range(self.N)]

    def fwd(self, f, a):
        fp = self.shift(f, a, 1)
        return [fp[n] - f[n] for n in range(self.N)]


def rand_state(T, rng, amp=3):
    return [(G(rng.randint(-amp, amp), rng.randint(-amp, amp)), G(rng.randint(-amp, amp), rng.randint(-amp, amp))) for _ in range(T.N)]


rng = random.Random(20260922)

# ================================================================== (a) the local conservation law, every state
T = Torus((3, 4, 5))
psi = rand_state(T, rng)
dpsi = [(-I * v[0], -I * v[1]) for v in T.H(psi)]                         # dpsi/dt = -i H psi
ok = True
for j in range(3):
    phi = T.S(psi, j); dphi = T.S(dpsi, j)
    pidot = [(inner(dpsi[n], phi[n]) + inner(psi[n], dphi[n])).re for n in range(T.N)]
    Js = [T.J(psi, a, j, phi) for a in range(3)]
    div = [sum(T.back(Js[a], a)[n] for a in range(3)) for n in range(T.N)]
    ok = ok and all(pidot[n] + div[n] == 0 for n in range(T.N))
# second-neighbour dependence: J_1^2(x) changes when psi(x + e_1 + e_2) changes
x0 = T.index[(0, 0, 0)]; y = T.index[(1, 1, 0)]
psi2 = list(psi); psi2[y] = (psi[y][0] + 1, psi[y][1])
reach = T.J(psi, 0, 1)[x0] != T.J(psi2, 0, 1)[x0]
want("A1 for EVERY state (random Gaussian-integer amplitudes, 3x4x5 torus): d(pi_j)/dt(x) + sum_a [J_a^j(x) - J_a^j(x - e_a)] = 0 at all "
     "60 sites for j = 1,2,3, with J_a^j(x -> x+e_a) = (1/2) Re[psi^dag(x+e_a) sigma_a (S_j psi)(x) + (S_j psi)^dag(x+e_a) sigma_a psi(x)]; "
     "J_1^2(x) depends on psi(x + e_1 + e_2), a second neighbour", ok and reach)

# ================================================================== (b) the coupling whose response is J; uniform strains
T4 = Torus((4, 4, 4))
psi = rand_state(T4, rng)
phi_rand = rand_state(T4, rng)


def C_apply(T, a, v, f):
    fp, fm = T.shift(f, a, 1), T.shift(f, a, -1)
    vm = T.shift(v, a, -1)
    return [((v[n] * fp[n][0] + vm[n] * fm[n][0]) * F(1, 2), (v[n] * fp[n][1] + vm[n] * fm[n][1]) * F(1, 2)) for n in range(T.N)]


def D_apply(T, a, j, v, f):
    """sigma_a (1/2){C_a[v], S_j} f"""
    t1 = C_apply(T, a, v, T.S(f, j))
    t2 = T.S(C_apply(T, a, v, f), j)
    return [sig(a, ((u[0] + w[0]) * F(1, 2), (u[1] + w[1]) * F(1, 2))) for u, w in zip(t1, t2)]


def expval(T, f, g):
    return sum((inner(f[n], g[n]) for n in range(T.N)), G())


ok = True; herm = True
for a in range(3):
    for j in range(3):
        Jaj = T4.J(psi, a, j)
        for n0 in range(T4.N):
            v = [F(int(n == n0)) for n in range(T4.N)]
            ev = expval(T4, psi, D_apply(T4, a, j, v, psi))
            ok = ok and ev.im == 0 and ev.re == Jaj[n0]
        vr = [F(rng.randint(-3, 3)) for _ in range(T4.N)]
        herm = herm and expval(T4, phi_rand, D_apply(T4, a, j, vr, psi)) == expval(T4, psi, D_apply(T4, a, j, vr, phi_rand)).conj()
want("B1 H[B] = H + sum_aj sigma_a (1/2){C_a[B_a^j], S_j} is hermitian (random bond fields, random pairs of states) and "
     "d<H[B]>/dB_a^j(x) = J_a^j(x -> x + e_a) exactly at all 64 sites of the 4^3 torus for all nine (a, j), for a random state", ok and herm)

# uniform strain: operator against symbol on the 4^3 torus (e^{ik}, sin k, cos k in {0, +-1, +-i})
Bu = [[F(1, 2), F(-1, 3), F(2, 5)], [F(1, 7), F(-2, 3), F(1, 4)], [F(3, 5), F(0), F(-1, 6)]]
unit = {0: G(1), 1: G(0, 1), 2: G(-1), 3: G(0, -1)}                          # e^{i pi n/2}
ok = True
for nk in itertools.product(range(4), repeat=3):
    s = [F(unit[n].im) for n in nk]; c = [F(unit[n].re) for n in nk]
    V = [s[a] + c[a] * sum(Bu[a][j] * s[j] for j in range(3)) for a in range(3)]
    for chi in ((G(1), G(0)), (G(0), G(1))):
        wave = [tuple(unit[sum(nk[d] * x[d] for d in range(3)) % 4] * chi[t] for t in range(2)) for x in T4.sites]
        out = T4.H(wave)
        for a in range(3):
            for j in range(3):
                v = [Bu[a][j]] * T4.N
                dd = D_apply(T4, a, j, v, wave)
                out = [(o[0] + d[0], o[1] + d[1]) for o, d in zip(out, dd)]
        Hk = [G(), G()]
        for a in range(3):
            sa = sig(a, chi)
            Hk = [Hk[0] + sa[0] * V[a], Hk[1] + sa[1] * V[a]]
        ok = ok and all(out[n][t] == Hk[t] * unit[sum(nk[d] * T4.sites[n][d] for d in range(3)) % 4] for n in range(T4.N) for t in range(2))
k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
ks = (k1, k2, k3)
Bs = sp.Matrix(3, 3, lambda a, j: sp.Symbol(f"B{a + 1}{j + 1}", real=True))
s_ = [sp.sin(k) for k in ks]; c_ = [sp.cos(k) for k in ks]
Vs = [s_[a] + c_[a] * sum(Bs[a, j] * s_[j] for j in range(3)) for a in range(3)]
px = sp.Matrix([[0, 1], [1, 0]]); py = sp.Matrix([[0, -sp.I], [sp.I, 0]]); pz = sp.Matrix([[1, 0], [0, -1]])
Hk_s = Vs[0] * px + Vs[1] * py + Vs[2] * pz
sq_ok = sp.simplify(Hk_s * Hk_s - sum(v ** 2 for v in Vs) * sp.eye(2)) == sp.zeros(2, 2)
V2 = sum(v ** 2 for v in Vs)
flip_ok = True
for a in range(3):
    flipped = V2.subs(ks[a], sp.pi - ks[a], simultaneous=True)
    flip_ok = flip_ok and sp.expand(sp.expand_trig(V2 - flipped - 4 * s_[a] * c_[a] * sum(Bs[a, j] * s_[j] for j in range(3)))) == 0
# block 62's site frame for contrast: H(k) = sum_j (E^j.sigma) s_j, H^2 depends on s only
want("B2 for a uniform strain H[B](k) = sum_a sigma_a (s_a + c_a (B s)_a) (s = sin k, c = cos k; checked against the operator on all 64 "
     "plane waves of the 4^3 torus, both coins) and H[B]^2 = |V|^2 exactly; the reflection k_a -> pi - k_a keeps s and flips c_a, and "
     "|V|^2 changes by exactly 4 s_a c_a (B s)_a: so H[B]^2 is a function of sin k alone (a metric form g^ij s_i s_j, block 62 T1) ONLY "
     "for B = 0 - the bond coupling trades block 62's exact metric for exact conservation", ok and sq_ok and flip_ok)

# ================================================================== (c) the member placed to match: block 62's member translated
p1, p2, p3 = sp.symbols("p1 p2 p3", real=True)
P = (p1, p2, p3)
xi = sp.symbols("xi1 xi2 xi3", real=True)
hs = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"h{min(i, j) + 1}{max(i, j) + 1}", real=True))
psq = sum(x ** 2 for x in P)


def R1(h):
    return -(sum(P[i] * P[j] * h[i, j] for i in range(3) for j in range(3)) - psq * sum(h[i, i] for i in range(3)))


def R2(h):
    tr = sum(h[i, i] for i in range(3))
    return (-sp.Rational(1, 4) * psq * sum(h[i, j] ** 2 for i in range(3) for j in range(3))
            + sp.Rational(1, 2) * sum(sum(P[i] * h[i, j] for i in range(3)) ** 2 for j in range(3))
            - sp.Rational(1, 2) * sum(P[i] * h[i, j] * P[j] for i in range(3) for j in range(3)) * tr
            + sp.Rational(1, 4) * psq * tr ** 2)


dh = sp.Matrix(3, 3, lambda i, j: P[i] * xi[j] + P[j] * xi[i])
inv62 = sp.expand(R1(hs + dh) - R1(hs)) == 0 and sp.expand(R2(hs + dh) - R2(hs)) == 0
# corner placement: h_ij(x) = -(B_i^j(x) + B_j^i(x)), relabelling dh_ij = -(D_i xi_j + D_j xi_i), D_i = e^{ik_i} - 1.
# With h'_ij = e^{-i(k_i+k_j)/2} h_ij and eta_j = e^{-ik_j/2} xi_j:  e^{-i(k_i+k_j)/2}(D_i xi_j + D_j xi_i) = i (p_i eta_j + p_j eta_i).
ok_ph = True
for i in range(3):
    for j in range(3):
        lhs = sp.exp(-sp.I * (ks[i] + ks[j]) / 2) * ((sp.exp(sp.I * ks[i]) - 1) * xi[j] + (sp.exp(sp.I * ks[j]) - 1) * xi[i])
        rhs = sp.I * (2 * sp.sin(ks[i] / 2) * sp.exp(-sp.I * ks[j] / 2) * xi[j] + 2 * sp.sin(ks[j] / 2) * sp.exp(-sp.I * ks[i] / 2) * xi[i])
        ok_ph = ok_ph and sp.simplify(sp.expand((lhs - rhs).rewrite(sp.exp))) == 0
# real space: R_1 in the corner placement, R_1'(x) = sum_ij (D_i^- D_j^- h_ij)(x) - sum_m Lap_m sum_i h_ii(x - e_i), of a pure relabelling
T5 = Torus((5, 4, 3))
xir = [[F(rng.randint(-9, 9)) for _ in range(T5.N)] for _ in range(3)]
hcorner = {}
for i in range(3):
    for j in range(3):
        hcorner[(i, j)] = [-(T5.fwd(xir[j], i)[n] + T5.fwd(xir[i], j)[n]) for n in range(T5.N)]
term1 = [F(0)] * T5.N
for i in range(3):
    for j in range(3):
        t = T5.back(T5.back(hcorner[(i, j)], j), i)
        term1 = [u + w for u, w in zip(term1, t)]
trace_shift = [F(0)] * T5.N
for i in range(3):
    t = T5.shift(hcorner[(i, i)], i, -1)
    trace_shift = [u + w for u, w in zip(trace_shift, t)]
lap = [F(0)] * T5.N
for m in range(3):
    fp, fm = T5.shift(trace_shift, m, 1), T5.shift(trace_shift, m, -1)
    lap = [u + fp[n] - 2 * trace_shift[n] + fm[n] for n, u in enumerate(lap)]
R1corner = [u - w for u, w in zip(term1, lap)]
want("C1 THE REWRITE: with displacements xi on sites and the strain on its bond (h_ij(x) = -(B_i^j(x) + B_j^i(x)) from the site's forward "
     "bonds), a relabelling moves h by forward differences, -(d_i xi_j + d_j xi_i), and translating h_ij by (e_i + e_j)/2 and xi_j by "
     "e_j/2 turns that into block 62's i(p_i eta_j + p_j eta_i): the member is block 62's R_1, R_2 of the translated h, SAME symbols "
     "p_j = 2 sin(k_j/2), relabelling invariance exact (symbolic for R_1, R_2; R_1 of a random integer relabelling zero at all 60 sites "
     "of the 5x4x3 torus in real space)", inv62 and ok_ph and all(v == 0 for v in R1corner))

# ================================================================== (c) the decision: the symmetric part, an exact witness
chiA = (G(1), G(1)); chiB = (G(1), G(0, 1))                               # +1 eigenvectors of sigma_x and sigma_y
psiW = [(unit[x[0] % 4] * chiA[0] + unit[x[1] % 4] * chiB[0], unit[x[0] % 4] * chiA[1] + unit[x[1] % 4] * chiB[1]) for x in T4.sites]
stat = T4.H(psiW) == psiW
Jw = {(a, j): T4.J(psiW, a, j) for a in range(3) for j in range(3)}
cons = all(sum(T4.back(Jw[(a, j)], a)[n] for a in range(3)) == 0 for j in range(3) for n in range(T4.N))
trans = {j: [sum(T4.back(Jw[(j, a)], a)[n] for a in range(3)) for n in range(T4.N)] for j in range(3)}
vals = sorted({v for j in range(3) for v in trans[j]})
symdiv_nonzero = any(v != 0 for j in range(3) for v in trans[j])
want("C2 THE DECISION, EXACT WITNESS: psi = e^{i pi x1/2}(1,1) + e^{i pi x2/2}(1,i) on the 4^3 torus has H psi = psi exactly; its bond "
     "current is conserved at every site (sum_a back_a J_a^j = 0), but the transposed divergence sum_a back_a J_j^a takes the values "
     f"{[str(v) for v in vals]}: the corner-placed symmetric source J_(aj) = (J_a^j + J_j^a)/2, whose divergence the member's "
     "condition needs, has divergence (1/2) x that, not zero", stat and cons and symdiv_nonzero)

# pairing form of the obstruction on the witness: P_sym = sum J_(aj) d_a xi_j = -P_rot, P_rot = (1/2) sum tau_aj d_a xi_j, tau = J - J^T
ok = True; seen_nonzero = False
for trial in range(5):
    xiw = [[F(rng.randint(-5, 5)) for _ in range(T4.N)] for _ in range(3)]
    dxi = {(a, j): T4.fwd(xiw[j], a) for a in range(3) for j in range(3)}
    Pfull = sum(Jw[(a, j)][n] * dxi[(a, j)][n] for a in range(3) for j in range(3) for n in range(T4.N))
    Psym = sum((Jw[(a, j)][n] + Jw[(j, a)][n]) / 2 * dxi[(a, j)][n] for a in range(3) for j in range(3) for n in range(T4.N))
    Prot = sum((Jw[(a, j)][n] - Jw[(j, a)][n]) / 2 * dxi[(a, j)][n] for a in range(3) for j in range(3) for n in range(T4.N))
    ok = ok and Pfull == 0 and Psym == -Prot
    seen_nonzero = seen_nonzero or Psym != 0
want("C3 the obstruction is the torque: on the witness, for random integer relabellings xi, sum_x,a,j J_a^j d_a xi_j = 0 (conservation) "
     "while the symmetric pairing sum J_(aj) d_a xi_j equals MINUS the torque pairing (1/2) sum (J_a^j - J_j^a) d_a xi_j and is not zero",
     ok and seen_nonzero)

# ================================================================== (c) plane-wave closed form, every wavelength
kA = (1, 0, 0); kB = (0, 1, 0)                                            # the witness's pair, in units of pi/2
def M_of(chi_p, chi, a):
    return inner(chi_p, sig(a, chi))
sA = [F(unit[n].im) for n in kA]; sB = [F(unit[n].im) for n in kB]
Aa = [(unit[kA[a] % 4] + unit[(-kB[a]) % 4]) * F(1, 2) for a in range(3)]          # A_a = (e^{ik_a} + e^{-ik'_a})/2
Ma = [M_of(chiB, chiA, a) for a in range(3)]
qv = [(kA[a] - kB[a]) % 4 for a in range(3)]
ok = True
for j in range(3):
    for a in range(3):
        # J(x) - J_A - J_B = Re[(s_j + s'_j) A_a M_a e^{iq.x}]
        JA = T4.J([(unit[x[0] % 4] * chiA[0], unit[x[0] % 4] * chiA[1]) for x in T4.sites], a, j)
        JB = T4.J([(unit[x[1] % 4] * chiB[0], unit[x[1] % 4] * chiB[1]) for x in T4.sites], a, j)
        coef = (sA[j] + sB[j]) * Aa[a] * Ma[a]
        ok = ok and all(Jw[(a, j)][n] - JA[n] - JB[n] == (coef * unit[sum(qv[d] * T4.sites[n][d] for d in range(3)) % 4]).re for n in range(T4.N))
    cT = Aa[j] * Ma[j] * sum(((1 - unit[(-qv[a]) % 4]) * (sA[a] + sB[a]) for a in range(3)), G())
    ok = ok and all(trans[j][n] == (cT * unit[sum(qv[d] * T4.sites[n][d] for d in range(3)) % 4]).re for n in range(T4.N))
kb = sp.symbols("kb1 kb2 kb3", real=True); qs = sp.symbols("q1 q2 q3", real=True)
kk = [kb[a] + qs[a] / 2 for a in range(3)]; kp = [kb[a] - qs[a] / 2 for a in range(3)]
lhs = sp.Rational(1, 2) * sum((1 - sp.exp(-sp.I * qs[a])) * (sp.sin(kk[a]) + sp.sin(kp[a])) for a in range(3))
mid = sp.I * sum(sp.exp(-sp.I * qs[a] / 2) * sp.sin(qs[a]) * sp.sin(kb[a]) for a in range(3))
third = sp.I * (sum(sp.sin(qs[a]) * sp.sin(kb[a]) * (sp.cos(qs[a] / 2) - sp.cos(kb[a]) - sp.I * sp.sin(qs[a] / 2)) for a in range(3))
                + sp.Rational(1, 2) * sum(sp.sin(kk[a]) ** 2 - sp.sin(kp[a]) ** 2 for a in range(3)))
tri = sp.simplify(sp.expand((lhs - mid).rewrite(sp.exp))) == 0 and sp.simplify(sp.expand((mid - third).rewrite(sp.exp))) == 0
want("C4 PLANE WAVES, EVERY WAVELENGTH: for psi = chi e^{ik.x} + chi' e^{ik'.x}, J_a^j(x) = const + Re[(s_j + s'_j) A_a M_a e^{iq.x}] with "
     "q = k - k', A_a = (e^{ik_a} + e^{-ik'_a})/2, M_a = chi'^dag sigma_a chi (checked on the witness at every site, all nine (a, j)), so "
     "sum_a back_a J_j^a = Re[e^{iq.x} A_j M_j sum_a (1 - e^{-iq_a})(s_a + s'_a)] = Re[2i e^{iq.x} A_j M_j sum_a e^{-iq_a/2} sin q_a sin kbar_a], "
     "and for equal energies (|s| = |s'|) the sum equals sum_a sin q_a sin kbar_a [cos(q_a/2) - cos kbar_a - i sin(q_a/2)]: third order in "
     "the wave numbers (leading Re[e^{iq.x} A_j M_j sum_a q_a^2 kbar_a]), the order of block 62's site defect, not zero in general", ok and tri)

# ================================================================== (c) no re-weighting of the transposed current repairs it
coins = {(0, 1): (G(1), G(1)), (0, -1): (G(1), G(-1)), (1, 1): (G(1), G(0, 1)), (1, -1): (G(1), G(0, -1)), (2, 1): (G(1), G(0)), (2, -1): (G(0), G(1))}
shell = []
for nk in itertools.product(range(4), repeat=3):
    s = [unit[n].im for n in nk]
    if sum(v * v for v in s) == 1:
        a0 = next(a for a in range(3) if s[a] != 0)
        shell.append((nk, [F(v) for v in s], coins[(a0, int(s[a0]))]))
qfix = (0, 3, 1); jfix = 0
rows = []
for (nk, s, chi) in shell:
    for (nk2, s2, chi2) in shell:
        if tuple((nk[d] - nk2[d]) % 4 for d in range(3)) != qfix: continue
        A_j = (unit[nk[jfix] % 4] + unit[(-nk2[jfix]) % 4]) * F(1, 2)
        if A_j * inner(chi2, sig(jfix, chi)) == 0: continue
        rows.append([s[a] + s2[a] for a in (1, 2)])
rank = sp.Matrix(rows).rank() if rows else 0
want("C5 NO RE-WEIGHTING HELPS: on the 4^3 torus at energy 1 and q = (0, 3pi/2, pi/2), j = 1, every pair (k, k - q) of the energy shell "
     "with A_j M_j != 0 forces sum_a beta_a (s_a + s'_a) = 0 on the weights beta_a = (1 - e^{-iq_a}) pi_a(q) of ANY translation-invariant "
     "operator applied to the transposed current; these pairs' vectors have rank 2 on the two components with q_a != 0, so only "
     "pi = 0 works: the symmetric part cannot be placed so as to be divergence-free", rank == 2, f"{len(rows)} pairs, rank {rank}")

# ================================================================== (d) what absorbs it
ok = True
for trial in range(3):
    xis = [[F(rng.randint(-9, 9)) for _ in range(T5.N)] for _ in range(3)]
    Bd = {(a, j): T5.fwd(xis[j], a) for a in range(3) for j in range(3)}
    for a in range(3):
        for b in range(3):
            for j in range(3):
                curl = [u - w for u, w in zip(T5.fwd(Bd[(b, j)], a), T5.fwd(Bd[(a, j)], b))]
                ok = ok and all(v == 0 for v in curl)
want("D1 a member of the FULL nine-component bond strain built from the plaquette curls F_ab^j = d_a B_b^j - d_b B_a^j (block 64) is "
     "unchanged by every relabelling (curls of d_a xi_j vanish identically; random integer xi on the 5x4x3 torus), so its solvability "
     "condition is sum J_a^j d_a xi_j = 0, which A1 gives exactly on stationary states: the torque is absorbed by the three rotational "
     "components of the bond strain as field variables, sourced by tau = J - J^T", ok)

# block 65's coin rotation: H[theta] = H + (1/2) sum_j {(theta x e_j).sigma, S_j} + (1/2) sum_a C_a[d_a theta_a]; its response
EPS = {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1, (0, 2, 1): -1, (2, 1, 0): -1, (1, 0, 2): -1}


def coin_rot_response(T, psi, c, n0):
    """<psi| dH[theta]/dtheta_c(x0) |psi> at theta = 0."""
    delta = [F(int(n == n0)) for n in range(T.N)]
    acc = G()
    for j in range(3):
        for b in range(3):
            e = EPS.get((b, c, j), 0)                                   # (e_c x e_j)_b = eps_bcj
            if e == 0: continue
            Sj = T.S(psi, j)
            t1 = [sig(b, (delta[n] * Sj[n][0], delta[n] * Sj[n][1])) for n in range(T.N)]
            dpsi_ = [sig(b, (delta[n] * psi[n][0], delta[n] * psi[n][1])) for n in range(T.N)]
            t2 = T.S(dpsi_, j)
            acc = acc + expval(T, psi, [((u[0] + w[0]) * F(e, 2), (u[1] + w[1]) * F(e, 2)) for u, w in zip(t1, t2)])
    twist = T.fwd(delta, c)                                             # d_c theta_c
    acc = acc + expval(T, psi, [(u[0] * F(1, 2), u[1] * F(1, 2)) for u in C_apply(T, c, twist, psi)])
    return acc


psi_r = rand_state(T4, rng)
Hpsi = T4.H(psi_r)
ok = True
for c in range(3):
    for n0 in range(T4.N):
        r = coin_rot_response(T4, psi_r, c, n0)
        half_dspin = (I * inner(Hpsi[n0], sig(c, psi_r[n0]))).re        # (1/2) d(psi^dag sigma_c psi)/dt = Re[i (H psi)^dag sigma_c psi]
        ok = ok and r.im == 0 and r.re == half_dspin
zero_on_witness = all(coin_rot_response(T4, psiW, c, n0) == 0 for c in range(3) for n0 in range(T4.N))
torque_nonzero = any(Jw[(a, j)][n] != Jw[(j, a)][n] for a in range(3) for j in range(3) for n in range(T4.N))
want("D2 block 65's law for the rotation of the COIN axes (frame rotation at every site plus the scalar hop weighted by the twist) has "
     "response d<H[theta]>/dtheta_c(x) = (1/2) d(psi^dag sigma_c psi)(x)/dt for every state (exact, all 192 site-axis pairs, a random state), "
     "hence zero at every site of the witness, whose bond torque J_a^j - J_j^a is not zero: a coin-rotation variable adds nothing to the "
     "static sources, so it cannot absorb the torque; what absorbs it is a rotation of the BONDS coupled as a relabelling's deformation (D1)",
     ok and zero_on_witness and torque_nonzero)

npass = sum(1 for _, o in RESULTS if o)
nfail = len(RESULTS) - npass
print(f"TOTAL: PASS={npass} FAIL={nfail}")
if nfail == 0:
    print("SUMMARY: ROUTE FAILS AT (c) for a metric member: the bond current J_a^j is conserved exactly and is the exact response of the "
          "second-neighbour bond coupling H[B], whose uniform H[B]^2 is a metric form only for B = 0; block 62's member rewritten for "
          "the bond placement is block 62's own member translated (same symbols p_j, exact relabelling invariance, forward differences), "
          "and its solvability condition becomes the divergence of the symmetric part, which equals minus half the divergence of the "
          "bond torque J_a^j - J_j^a and is NOT zero on stationary states (exact witness on the 4^3 torus; closed form for every pair of "
          "plane waves, third order in the wave numbers; no translation-invariant re-weighting of the transposed current repairs it at the "
          "witness wave vector q = (0, 3pi/2, pi/2) of the 4^3 torus); a coin-rotation law (block 65) cannot absorb it, its response being "
          "zero on stationary states; a member of the full "
          "nine-component strain (curls) absorbs it, with the three rotations as field variables sourced by the torque")
    print("HIT: with the bond-placed strain (block 64's coupling, exact response J), block 62's metric member is exactly relabelling-"
          "invariant after translating h_ij by (e_i + e_j)/2, but its static condition fails on stationary states of the walk: it asks "
          "sum_a back_a J_(aj) = 0, which by exact conservation equals -(1/2) sum_a back_a (J_a^j - J_j^a); psi = e^{i pi x1/2}(1,1) + "
          "e^{i pi x2/2}(1,i) on 4^3 (H psi = psi) has transposed divergence sum_a back_a J_j^a = +-2 at sites; for any plane-wave pair of equal energy the transposed divergence is Re[2i e^{iq.x} A_j M_j sum_a sin q_a sin kbar_a (cos(q_a/2) - "
          "cos kbar_a - i sin(q_a/2))], and at q = (0, 3pi/2, pi/2) on 4^3 no translation-invariant re-weighting of the transposed current "
          "removes it")
