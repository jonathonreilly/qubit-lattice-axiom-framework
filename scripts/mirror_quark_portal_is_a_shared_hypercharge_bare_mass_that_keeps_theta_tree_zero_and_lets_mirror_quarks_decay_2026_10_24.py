AUDIT_INPUT_PATHS = ('docs/MIRROR_QUARK_PORTAL_IS_A_SHARED_HYPERCHARGE_BARE_MASS_THAT_KEEPS_THETA_TREE_ZERO_AND_LETS_MIRROR_QUARKS_DECAY_BOUNDED_THEOREM_NOTE_2026-10-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""mirror-quark-portal: can a P_slab-symmetric light-mirror quark portal exist in the BCS shape?

Supplied-model checks (exact group theory + mass-matrix toys + supplied-number estimates).
Self-contained (numpy, scipy, fractions). Seeded. Prints PASS/FAIL lines, ends with TOTAL.
"""
AUDIT_TIMEOUT_SEC = 120

import time
from fractions import Fraction as Fr
import numpy as np
from scipy.special import i0, i1

T0 = time.time()
rng = np.random.default_rng(20261024)
NP = 0
NF = 0


def check(tag, ok, msg):
    global NP, NF
    if ok:
        NP += 1
    else:
        NF += 1
    print(f"{'PASS' if ok else 'FAIL'} {tag}: {msg}")


# ---------------------------------------------------------------- fields
# name: (triality, dL, dR', Y, Y', chirality); light 16 on near wall, mirror on far wall
h = Fr(1, 2)
F = {
    "qL": (1, 2, 1, Fr(1, 6), 0, "L"), "uR": (1, 1, 1, Fr(2, 3), 0, "R"), "dR": (1, 1, 1, Fr(-1, 3), 0, "R"),
    "lL": (0, 2, 1, Fr(-1, 2), 0, "L"), "eR": (0, 1, 1, Fr(-1), 0, "R"),
    "q'R": (1, 1, 2, 0, Fr(1, 6), "R"), "u'L": (1, 1, 1, 0, Fr(2, 3), "L"), "d'L": (1, 1, 1, 0, Fr(-1, 3), "L"),
    "l'R": (0, 1, 2, 0, Fr(-1, 2), "R"), "e'L": (0, 1, 1, 0, Fr(-1), "L"),
}
LR_cross = [("qL", "q'R"), ("u'L", "uR"), ("u'L", "dR"), ("d'L", "uR"), ("d'L", "dR")]


def bil(a, b):  # psi_a-bar_L psi_b_R
    fa, fb = F[a], F[b]
    return (fa[1], fa[2], fb[1], fb[2], -fa[3] + fb[3], -fa[4] + fb[4])


def in_half_Z(x):
    return (2 * Fr(x)).denominator == 1


print("== A. Portal operators (separate U(1)_Y x U(1)'_Y, then shared Y) ==")
bad = [(a, b) for a, b in LR_cross if in_half_Z(bil(a, b)[4]) and in_half_Z(bil(a, b)[5])]
ys = ", ".join(f"{a}-bar {b}:({bil(a,b)[4]},{bil(a,b)[5]})" for a, b in LR_cross)
check("A1 [T]", not bad, f"separate Y: every cross quark bilinear has (Y,Y') off Z/2 -> no H^a H'^b neutraliser. {ys}")


# SU(2)xSU(2)' content of H^a Hdag^b H'^c H'dag^d (bosonic, one doublet each): Sym^a x Sym^b
# contains spin j iff |a-b|/2 <= j <= (a+b)/2 and (a+b)/2 - j integer. Singlet needs a = b -> Y_H = 0.
def scalar_monomials(jL, jR, Yneed, maxdeg=6):
    hits = []
    for a in range(maxdeg + 1):
        for b in range(maxdeg + 1 - a):
            for c in range(maxdeg + 1 - a - b):
                for d in range(maxdeg + 1 - a - b - c):
                    okL = abs(a - b) <= 2 * jL <= a + b and ((a + b) - 2 * jL) % 2 == 0
                    okR = abs(c - d) <= 2 * jR <= c + d and ((c + d) - 2 * jR) % 2 == 0
                    Y = Fr(a - b, 2) + Fr(c - d, 2)
                    if okL and okR and Y == Yneed:
                        hits.append(a + b + c + d)
    return min(hits) if hits else None


rows = []
for a, b in LR_cross:
    dL1, dR1, dL2, dR2, Y, Yp = bil(a, b)
    Ysh = Y + Yp  # shared hypercharge
    jL = 0 if dL1 * dL2 == 1 else Fr(1, 2)
    jR = 0 if dR1 * dR2 == 1 else Fr(1, 2)
    nmin = scalar_monomials(jL, jR, -Ysh)
    rows.append((a, b, Ysh, None if nmin is None else 3 + nmin))
dims = {f"{a}-bar {b}": d for a, b, _, d in rows}
ok = dims["u'L-bar uR"] == 3 and dims["d'L-bar dR"] == 3 and dims["qL-bar q'R"] == 5 \
    and dims["u'L-bar dR"] is None and dims["d'L-bar uR"] is None
check("A2 [T]", ok, "shared Y: lowest dimension " + ", ".join(f"{k}={v}" for k, v in dims.items())
      + " (None = forbidden to all orders in H,H'); u'L-bar uR, d'L-bar dR are bare masses C")
print("   -> renormalizable mass matrix is block lower-triangular: M = [[A, 0],[C, D]], B (qL-bar q'R) from dim-5")


# exact-charge invariant I = (Q + triality/3) mod 1 on the electric-charge components
def comps(name, shared):
    t, dL, dR, Y, Yp, _ = F[name]
    out = []
    for T3 in ([h, -h] if dL == 2 else [0]):
        for T3p in ([h, -h] if dR == 2 else [0]):
            if shared:
                out.append((T3 + T3p + Y + Yp,))
            else:
                out.append((T3 + Y, T3p + Yp))
    return t, out


def inv(name, shared):
    t, cs = comps(name, shared)
    return sorted({((c[0] + Fr(t, 3)) % 1, (c[-1] + Fr(t, 3)) % 1 if not shared else 0) for c in cs})


sep = {n: inv(n, False) for n in F}
shr = {n: inv(n, True) for n in F}
light_zero = all(v == [(0, 0)] or all(x[0] == 0 for x in v) for k, v in sep.items() if "'" not in k)
mirrorq = sorted({x[0] for k in ["q'R", "u'L", "d'L"] for x in sep[k]})
check("A3 [T]", light_zero and mirrorq == [Fr(1, 3)] and all(x[0] == 0 for v in shr.values() for x in v),
      f"I=(Q+t/3) mod 1: light & mirror leptons 0; mirror quarks {mirrorq} with Q,Q' separate -> lightest "
      "I!=0 state absolutely stable for ANY added field; with shared Y (Q=T3+T3'+Y) I=0 for all")

print("== B. theta_tree and light J with the portal C ==")


def haar(n):
    z = (rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))) / np.sqrt(2)
    q, r = np.linalg.qr(z)
    return q * (np.diag(r) / abs(np.diag(r)))


def cg(n, s=1.0):
    return s * (rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))) / np.sqrt(2)


def herm(n):
    x = cg(n)
    return (x + x.conj().T) / 2


def blocks(Yu, Yd, v, vp, al, be, Cu, Cd, Bu=None, Bd=None):
    hu, hp = v * np.exp(1j * al), vp * np.exp(1j * be)
    Au, Du = Yu * np.conj(hu), Yu.conj().T * hp
    Ad, Dd = Yd * hu, Yd.conj().T * np.conj(hp)
    Z = np.zeros((3, 3))
    Mu = np.block([[Au, Z if Bu is None else Bu], [Cu, Du]])
    Md = np.block([[Ad, Z if Bd is None else Bd], [Cd, Dd]])
    return Mu, Md


mx = 0.0
for k in range(300):
    Yu, Yd = cg(3), cg(3)
    vp = 10 ** rng.uniform(1, 4)
    herm_case = k % 2 == 0
    Cu = herm(3) * 10 ** rng.uniform(-3, 2) if herm_case else cg(3, 10 ** rng.uniform(-3, 2))
    Cd = herm(3) * 10 ** rng.uniform(-3, 2) if herm_case else cg(3, 10 ** rng.uniform(-3, 2))
    Mu, Md = blocks(Yu, Yd, 1.0, vp, rng.uniform(0, 6.3), rng.uniform(0, 6.3), Cu, Cd)
    s1, l1 = np.linalg.slogdet(Mu)
    s2, l2 = np.linalg.slogdet(Md)
    mx = max(mx, abs(np.angle(s1 * s2)))
check("B1 [T]", mx < 1e-12, f"det(MuMd)>0 for block-triangular M, Hermitian AND generic C, any VEV phase: "
      f"max|theta_tree|={mx:.1e} (300 samples, v'/v in [1e1,1e4])")

def light_ckm(Mu, Md):
    out = []
    for M in (Mu, Md):
        U, s, Vh = np.linalg.svd(M)
        idx = np.argsort(s)[:3]
        out.append((U[:3, idx], s[idx]))
    (Uu, su), (Ud, sd) = out
    return Uu.conj().T @ Ud, su, sd


Js, dev = [], 0.0
for k in range(200):
    Yu, Yd = cg(3), cg(3)
    vp = 1e4
    Mu, Md = blocks(Yu, Yd, 1.0, vp, rng.uniform(0, 6.3), rng.uniform(0, 6.3), 1e-2 * herm(3), 1e-2 * herm(3))
    V, su, sd = light_ckm(Mu, Md)
    Js.append(abs(np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1]))))
    su0 = np.sort(np.linalg.svd(Yu, compute_uv=False))
    dev = max(dev, np.max(abs(su - su0) / su0))
check("B3 [F]", np.median(Js) > 1e-2 and dev < 1e-4,
      f"light J free: median |J|={np.median(Js):.1e}; light masses = sv(Y) v to max rel {dev:.1e} (C<<yv')")

print("== C. Leak from dim-5 B and the BBN lifetime: the window for C ==")
v, LAM = 246.0, 2.4e18           # supplied
mu_q = np.array([2.16e-3, 1.27, 172.7])
md_q = np.array([4.67e-3, 0.0934, 4.18])  # supplied PDG, running ignored
yu, yd = np.sqrt(2) * mu_q / v, np.sqrt(2) * md_q / v


def leak(mu, vp, n=200, Bsc=None):
    th = []
    for _ in range(n):
        Yu = haar(3) @ np.diag(yu) @ haar(3).conj().T
        Yd = haar(3) @ np.diag(yd) @ haar(3).conj().T
        tot = 0.0
        for Y, conjh in ((Yu, True), (Yd, False)):
            a, b = rng.uniform(0, 6.3, 2)
            A = Y * (v / np.sqrt(2)) * np.exp(-1j * a)
            D = Y.conj().T * (vp / np.sqrt(2)) * np.exp(1j * b)
            Hm = herm(3)
            C = mu * Hm / np.max(abs(np.linalg.eigvalsh(Hm)))
            c = cg(3)
            B = c / np.linalg.norm(c, 2) * (v * vp / (2 * LAM) if Bsc is None else Bsc)
            X = np.linalg.solve(D, C @ np.linalg.solve(A, B))
            tot += np.angle(np.linalg.det(np.eye(3) - X))
        th.append(abs(tot))
    return np.median(th)


l1, l10 = leak(1.0, 1e9), leak(10.0, 1e9)
l10b = leak(10.0, 1e11)
cmax = 1e-10 / (l10 / 10.0)
cest = 1e-10 * yu[0] ** 2 * LAM
check("C1 [F]", 5 < l10 / l1 < 20 and 0.3 < l10b / l10 < 3,
      f"theta_leak linear in C, v'-independent: median {l1:.1e}(C=1), {l10:.1e}(C=10 GeV), {l10b:.1e}(v'=1e11); "
      f"theta<1e-10 needs C<{cmax:.2g} GeV for |c|=1 (worst-direction estimate y_u^2 Lam 1e-10 = {cest:.2g}; "
      f"median/estimate ratio {cmax/cest:.0f})")
lbd = leak(0.1, 1e9, Bsc=1.0)
check("C1b [F]", lbd > 1e-6, f"contrast: a condensed bi-doublet B = 1 GeV (C=0.1 GeV, v'=1e9) leaks median "
      f"|theta|={lbd:.1e} >> 1e-10 -> the SU(2) inter-wall link must stay disordered")

hbar = 6.582e-25
lines, okw = [], True
for vp in (1e8, 1e9, 1e10, 1e11):
    mup = mu_q[0] * vp / v
    cmin = vp * np.sqrt(16 * np.pi * hbar / (1.0 * mup))
    chi = min(cmax, 0.1 * mup)
    okw &= cmin < chi
    lines.append(f"v'={vp:.0e}: m_u'={mup:.1e}, C in [{cmin:.0e},{chi:.0e}] GeV")
check("C2 [E]", okw, "tau(u'->u h,Z,dW) = 16 pi hbar (v'/C)^2/m_u' < 1 s; window non-empty: " + "; ".join(lines))

print("== D. Electroweak breaking and FCNC (gauge toy SU(2) x SU(2)' x U(1)_shared) ==")
g, g1 = 0.65, 0.45
sig = [np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.diag([1.0, -1.0])]


def gen_H(Y, which):
    T = [s / 2 if (which == 0 and i < 3) or (which == 1 and i >= 3) else np.zeros((2, 2))
         for i, s in enumerate(sig + sig)]
    return T + [Y * np.eye(2)]


def gauge_mass(vv, vpp, k=0.0):
    gs = [g] * 6 + [g1]
    fields = [(gen_H(0.5, 0), np.array([0, vv / np.sqrt(2)])), (gen_H(0.5, 1), np.array([0, vpp / np.sqrt(2)]))]
    if k:
        TL = [np.kron(s / 2, np.eye(2)) for s in sig]
        TR = [np.kron(np.eye(2), -s.T / 2) for s in sig]
        fields.append((TL + TR + [np.zeros((4, 4))], np.array([k, 0, 0, k]) / np.sqrt(2)))
    M2 = np.zeros((7, 7))
    for T, p in fields:
        for a in range(7):
            for b in range(7):
                M2[a, b] += gs[a] * gs[b] * np.real(p.conj() @ (T[a] @ T[b] + T[b] @ T[a]) @ p)
    return M2


M2 = gauge_mass(1.0, 1e3)
w, U = np.linalg.eigh(M2)
mixWW = abs(M2[0, 3]) + abs(M2[0, 4]) + abs(M2[1, 3])
mW2 = M2[0, 0]
geff2 = 1 / (1 / g ** 2 + 1 / g1 ** 2)
rho = []
for vp in (1e2, 1e3):
    ww = np.linalg.eigvalsh(gauge_mass(1.0, vp))
    rho.append(abs(mW2 / (ww[3] * g ** 2 / (g ** 2 + geff2)) - 1))
M2k = gauge_mass(1.0, 1e3, k=0.3)
mixk = abs(M2k[0, 3]) + abs(M2k[1, 4])
check("D1 [T]", mixWW == 0 and abs(mW2 - g ** 2 / 4) < 1e-12 and np.sum(w < 1e-9) == 1
      and 50 < rho[0] / rho[1] < 200 and mixk > 1e-3,
      f"no bi-doublet VEV: W_L-W' mixing {mixWW:.0e}, M_W^2=g^2v^2/4 exact, 1 photon, rho-1={rho[0]:.1e},"
      f"{rho[1]:.1e} at v'/v=1e2,1e3 (~(v/v')^2); bi-doublet VEV 0.3v gives W_L-W' mixing {mixk:.2f} (problem returns)")

# Z couplings of quark Weyls in the toy; light-light off-diagonal after diagonalising M_u
iz = np.argsort(w)[3]
Zv = U[:, iz]


def zc(T3, T3p, Y):
    return g * T3 * Zv[2] + g * T3p * Zv[5] + g1 * Y * Zv[6]


zL = np.diag([zc(.5, 0, 1 / 6)] * 3 + [zc(0, 0, 2 / 3)] * 3)
zR = np.diag([zc(0, 0, 2 / 3)] * 3 + [zc(0, .5, 1 / 6)] * 3)
worst = 0.0
for _ in range(50):
    Yu = cg(3)
    Mu, _ = blocks(Yu, Yu, 1.0, 1e4, 0.3, 1.1, 1e-2 * herm(3), 1e-2 * herm(3))
    Uu, s, Vh = np.linalg.svd(Mu)
    idx = np.argsort(s)[:3]
    for mat, R in ((zL, Uu[:, idx]), (zR, Vh.conj().T[:, idx])):
        G = R.conj().T @ mat @ R
        worst = max(worst, np.max(abs(G - np.diag(np.diag(G)))) / g)
zdiag = (abs(zL[0, 0]) / g, abs(zL[3, 3]) / g, abs(zR[0, 0]) / g, abs(zR[3, 3]) / g)
check("D2 [F]", worst < 1e-10 and min(zdiag) > 1e-2, f"tree Z FCNC among light quarks (v'/v=1e4, C=1e-2 v): max off-diag/g = {worst:.1e} (diag "
      f"{zdiag[0]:.2f},{zdiag[1]:.2f},{zdiag[2]:.3f},{zdiag[3]:.3f}); "
      "uR and u'L share all charges, u'R differs only via Z-Z' mixing")

print("== E. Slab reading: the portal is the wall-overlap term dressed by the inter-wall link chain ==")
a, Ls = 0.4, 16
th = rng.uniform(0, 2 * np.pi, Ls - 1)
K0 = a * np.eye(Ls) - np.diag(np.ones(Ls - 1), 1)
Kt = a * np.eye(Ls) - np.diag(np.exp(1j * th), 1)
m0 = 1 / np.linalg.inv(K0)[0, -1]
mt = 1 / np.linalg.inv(Kt)[0, -1]
check("E1 [T]", abs(abs(m0) - a ** Ls) < 1e-20 and abs(mt / m0 - np.exp(-1j * th.sum())) < 1e-10,
      f"near-far effective mass = (1-m)^Ls x prod(link)^-1 exactly: |m|={abs(m0):.2e}, phase = Wilson line")
N = 4000
Phi_dis = np.mean(np.exp(1j * rng.uniform(0, 2 * np.pi, (N, Ls - 1)).sum(1)))
kap = 20.0
u = i1(kap) / i0(kap)
q = np.array([haar(2) for _ in range(800)])
P2 = q[:, :, :]
for _ in range(Ls - 2):
    P2 = np.einsum('nij,njk->nik', P2, np.array([haar(2) for _ in range(800)]))
Phi2 = np.linalg.norm(P2.mean(0)) / np.sqrt(2)
check("E2 [F]", abs(Phi_dis) < 0.05 and Phi2 < 0.1 and u ** (Ls - 1) > 0.5,
      f"disordered U(1) chain <Phi>={abs(Phi_dis):.3f}, Haar SU(2) chain <Phi_2>={Phi2:.3f} -> C=B=0 (X1 as stated, "
      f"wall-local D3); ordered U(1) (kappa=20) <Phi>=u^(Ls-1)={u**(Ls-1):.2f} -> C!=0 with B=0")
cmin8 = 1e8 * np.sqrt(16 * np.pi * hbar / (mu_q[0] * 1e8 / v))
Lhi = np.log(cmin8 / LAM) / np.log(a)
Llo = np.log(cmax / LAM) / np.log(a)
check("E3 [E]", Llo > 5, f"C = (1-m)^Ls x cutoff in window needs Ls in [{Llo:.0f},{Lhi:.0f}] at 1-m=0.4 "
      "(tension with wall-local D2 Ls<~5 for flat colour; Ls=5 gives C~1e16 GeV, excluded)")

print(f"runtime {time.time() - T0:.2f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
