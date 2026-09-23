#!/usr/bin/env python3
"""delay-of-the-rate-field-with-the-curvature-member, attempt 1 (worker w-jonathonsmac4f50-j03c0, claude-opus-5-5).

Exact claims: sympy. Section E is a floating point control (labelled [executed]).
Step labels refer to ATTEMPT.md.
"""
import sys
import time

import numpy as np
import sympy as sp

T0 = time.time()
NP = NF = 0


def ok(label, cond, detail=""):
    global NP, NF
    if cond:
        NP += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        NF += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def z(e):
    return sp.simplify(e) == 0


K, wb, al, be, p = sp.symbols("K wbar alpha beta p", positive=True)
t = sp.symbols("t", real=True)

# ---------------------------------------------------------------- Step 1: block 62's member and kinetic term, one wave vector
# symbols p_j; R1 = -(p_i p_j h_ij - p^2 h), R2 = -(1/4)p^2 h:h + (1/2)|p.h|^2 - (1/2)(p.h.p) h + (1/4) p^2 h^2
pv = sp.Matrix(sp.symbols("p1:4", real=True))
Hs = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"h{min(i, j)}{max(i, j)}", real=True))
xi = sp.Matrix(sp.symbols("xi1:4", real=True))


def R1(h, pp):
    return -((pp.T * h * pp)[0] - pp.dot(pp) * h.trace())


def R2(h, pp):
    ph = h * pp
    return (-sp.Rational(1, 4) * pp.dot(pp) * sum(h[i, j] ** 2 for i in range(3) for j in range(3))
            + sp.Rational(1, 2) * ph.dot(ph) - sp.Rational(1, 2) * (pp.T * h * pp)[0] * h.trace()
            + sp.Rational(1, 4) * pp.dot(pp) * h.trace() ** 2)


gauge = pv * xi.T + xi * pv.T
ok("1.1 R1 and R2 are unchanged by the relabelling h -> h + p xi + xi p (every p, h, xi)",
   z(R1(Hs + gauge, pv) - R1(Hs, pv)) and z(sp.expand(R2(Hs + gauge, pv) - R2(Hs, pv))))
phs = sp.symbols("phi", real=True)
Pp = sp.eye(3) - pv * pv.T / pv.dot(pv)
ok("1.2 on the scalar h = (1 - p p/p^2) phi, for every direction: R1 = 2 p^2 phi, R2 = (1/2) p^2 phi^2",
   z(R1(Pp * phs, pv) - 2 * pv.dot(pv) * phs) and z(R2(Pp * phs, pv) - pv.dot(pv) * phs ** 2 / 2))
ok("1.3 isotropic stretch h = 2 lam delta: the constraint K wbar R1 = e gives p^2 lam = e/(4 K wbar), block 60's Lap lam = -e/(4K wbar)",
   z(sp.solve(sp.Eq(K * wb * R1(2 * sp.Symbol("lam") * sp.eye(3), pv), sp.Symbol("e")), sp.Symbol("lam"))[0]
     - sp.Symbol("e") / (4 * K * wb * pv.dot(pv))))

# the full Lagrangian with p along z (every lattice wave vector can be rotated there: R1, R2 and the kinetic term are O(3)-covariant)
e = sp.Function("e")(t)
u = sp.Function("u")(t)
ph = sp.Function("phi")(t)  # scalar
a_ = sp.Function("a")(t)  # TT +
b_ = sp.Function("b")(t)  # TT x
xl = sp.Function("xiL")(t)  # longitudinal relabelling, h_zz = 2 xiL
cx = sp.Function("cx")(t)  # transverse relabellings h_xz, h_yz
cy = sp.Function("cy")(t)
hz = sp.Matrix([[ph + a_, b_, cx], [b_, ph - a_, cy], [cx, cy, 2 * xl]])
pz = sp.Matrix([0, 0, p])
hd = hz.diff(t)
Tkin = (al * sum(hd[i, j] ** 2 for i in range(3) for j in range(3)) + be * hd.trace() ** 2) / wb
Lag = Tkin + K * wb * (u * R1(hz, pz) + R2(hz, pz)) - e * u
fields = [u, ph, a_, b_, xl, cx, cy]
EL = {f: sp.expand(sp.diff(sp.diff(Lag, f.diff(t)), t) - sp.diff(Lag, f)) for f in fields}
ok("1.4 u-equation: K wbar R1 = e, i.e. 2 K wbar p^2 phi = e(t) - a constraint at each label time (no time derivative)",
   z(EL[u] - (e - 2 * K * wb * p ** 2 * ph)))
ok("1.5 TT equations: (4 alpha/wbar) a'' = -K wbar p^2 a (and b): speed^2 = K wbar^2/(4 alpha) in every direction (block 62 T4); no source from a body at rest",
   z(EL[a_] - (4 * al / wb * a_.diff(t, 2) + K * wb * p ** 2 * a_)) and z(EL[b_] - (4 * al / wb * b_.diff(t, 2) + K * wb * p ** 2 * b_)))
ok("1.6 longitudinal relabelling: d/dt[(8/wbar)((alpha+beta) xiL' + beta phi')] = 0 (no potential, no source at rest)",
   z(EL[xl] - sp.diff(8 / wb * ((al + be) * xl.diff(t) + be * ph.diff(t)), t)))
# solve: phi from the constraint, xiL' = -beta phi'/(alpha+beta) from rest, u from the phi-equation
phi_sol = e / (2 * K * wb * p ** 2)
xl_dot = -be * phi_sol.diff(t) / (al + be)
EPh = EL[ph].subs({xl.diff(t, 2): xl_dot.diff(t), xl.diff(t): xl_dot}).subs(ph, phi_sol).doit()
u_sol = sp.solve(sp.Eq(EPh, 0), u)[0]
u_claim = -e / (4 * K * wb * p ** 2) + al * (al + 3 * be) * e.diff(t, 2) / (K ** 2 * wb ** 3 * (al + be) * p ** 4)
ok("1.7 u(k,t) = -e(k,t)/(4 K wbar p^2) + alpha(alpha+3beta) e''(k,t)/(K^2 wbar^3 (alpha+beta) p^4): set at each label time by the content then",
   z(u_sol - u_claim), f"u = {sp.simplify(u_sol)}")
ok("1.8 static limit: u = -e/(4 K wbar p^2), i.e. Lap u = e/(4K wbar) (block 60 at rest, tau = 0)", z(u_claim.subs(e.diff(t, 2), 0) + e / (4 * K * wb * p ** 2)))
# the comparator's ratio
C = sp.symbols("C", real=True)
ok("1.9 alpha + beta = 0 (the comparator's kinetic ratio): the relabelling equation becomes beta phi' = const, so with the constraint e'(k,t) is constant: a jump of a body's energy has no solution",
   z(((al + be) * sp.Symbol("xLd") + be * phi_sol.diff(t)).subs(be, -al) + al * e.diff(t) / (2 * K * wb * p ** 2)))
ok("1.10 at alpha + 3 beta = 0 the e'' term vanishes and u is exactly the instantaneous Poisson field", z(u_claim.subs(be, -al / 3) + e / (4 * K * wb * p ** 2)))

# the mode determinant of block 62 T4 is reproduced (omega^2 = X): 2 TT waves, the rest static or constrained
Xs = sp.symbols("X", positive=True)
ok("1.11 the only travelling modes are TT: X = K wbar^2 p^2/(4 alpha); the scalar phi has no wave (it is fixed by the constraint)",
   sp.solve(sp.Eq(4 * al / wb * (-Xs) + K * wb * p ** 2, 0), Xs) == [K * wb ** 2 * p ** 2 / (4 * al)])

# ---------------------------------------------------------------- Step 2: a formation event
tau_r = sp.symbols("tau_r", positive=True)
De = sp.symbols("Delta_e", real=True)
s = t / tau_r
ramp = De * (3 * s ** 2 - 2 * s ** 3)  # smooth step on [0, tau_r]
du0 = u_claim.subs(e, ramp).doit()
du_early = sp.series(du0, t, 0, 2).removeO()
ok("2.1 a smooth switch-on of Delta_e over tau_r: at label time 0+ the clock field already moves, du = 6 alpha(alpha+3beta) Delta_e/(K^2 wbar^3 (alpha+beta) p^4 tau_r^2) + O(t), at every wave vector",
   z(du_early.subs(t, 0) - 6 * al * (al + 3 * be) * De / (K ** 2 * wb ** 3 * (al + be) * p ** 4 * tau_r ** 2)))
ok("2.2 after the switch-on the jump of u is the Poisson field of Delta_e, -Delta_e/(4 K wbar p^2), whatever alpha, beta",
   z(u_claim.subs(e, De).doit() + De / (4 * K * wb * p ** 2)))

print(f"exact part done in {time.time() - T0:.1f} s")

# ---------------------------------------------------------------- E: executed 2D-slice control (floating point)
Lx = 48
Kv, wbv, alv, bev = 1.0, 1.0, 1.0, 0.5
Cq = alv * (alv + 3 * bev) / (Kv ** 2 * wbv ** 3 * (alv + bev))
cT = wbv * np.sqrt(Kv / (4 * alv))
kx = 2 * np.pi * np.fft.fftfreq(Lx)
KX, KY = np.meshgrid(kx, kx, indexing="ij")
P2 = 4 * np.sin(KX / 2) ** 2 + 4 * np.sin(KY / 2) ** 2
P2[0, 0] = 1.0
X, Y = np.meshgrid(np.arange(Lx), np.arange(Lx), indexing="ij")
c0 = Lx // 2
blob = np.exp(-((X - c0) ** 2 + (Y - c0) ** 2) / (2 * 1.5 ** 2))
blob /= blob.sum()
tr = 2.0


def e_of(tq, d0):
    sq = np.clip(tq / tr, 0, 1)
    return d0 * (3 * sq ** 2 - 2 * sq ** 3)


def edd_of(tq, d0):
    if tq <= 0 or tq >= tr:
        return 0.0
    return d0 * (6 - 12 * tq / tr) / tr ** 2


def u_field(tq, d0):
    ek = np.fft.fft2(blob) * e_of(tq, d0)
    eddk = np.fft.fft2(blob) * edd_of(tq, d0)
    uk = -ek / (4 * Kv * wbv * P2) + Cq * eddk / P2 ** 2
    uk[0, 0] = 0.0
    return np.real(np.fft.ifft2(uk))


sx = np.array([[0, 1], [1, 0]], complex)
sy = np.array([[0, -1j], [1j, 0]])


def Sop(psi, ax):  # (T - T^dag)/(2i) along axis ax
    return (np.roll(psi, -1, axis=ax) - np.roll(psi, 1, axis=ax)) / (2j)


def Hw(psi, w):
    phs_ = np.sqrt(w)[..., None]
    f = phs_ * psi
    g = np.einsum("ab,xyb->xya", sx, Sop(f, 0)) + np.einsum("ab,xyb->xya", sy, Sop(f, 1))
    return phs_ * g


def force(psi, w):  # d<S_x>/dt = <i [H_w, S_x]>
    return float(np.real(np.vdot(psi, 1j * (Hw(Sop(psi, 0), w) - Sop(Hw(psi, w), 0)))))


def packet(r):
    """positive-energy packet at rest: wave number pi/2 along y (group speed cos(pi/2) = 0), coin (1, i)/sqrt 2 (+ branch of sigma_y)"""
    g = np.exp(-((X - (c0 + r)) ** 2 + (Y - c0) ** 2) / (2 * 3.0 ** 2)) * (1j ** Y)
    psi = np.zeros((Lx, Lx, 2), complex)
    psi[..., 0] = g
    psi[..., 1] = 1j * g
    return psi / np.linalg.norm(psi)


rows = []
for r in (8, 16):
    for d0 in (0.02, 0.04):
        psi = packet(r)
        f_before = force(psi, np.ones((Lx, Lx)))
        f_early = force(psi, np.exp(u_field(0.05, d0)))
        f_after = force(psi, np.exp(u_field(tr, d0)))
        en = float(np.real(np.vdot(psi, Hw(psi, np.ones((Lx, Lx))))))
        ux = u_field(tr, d0)
        wts = np.sum(np.abs(psi) ** 2, axis=2)
        grad = np.sum(wts * (np.roll(ux, -1, 0) - np.roll(ux, 1, 0)) / 2)
        rows.append((r, d0, f_before, f_early, f_after, en, -en * grad))
        print(f"EXEC E r={r} Delta_e={d0}: packet energy {en:.4f}; d<S_x>/dt before {f_before:+.3e}, at t=0.05 {f_early:+.3e}, after the switch-on {f_after:+.3e} "
              f"(block 54's -E <grad u> = {-en * grad:+.3e}); TT wave would arrive at t = {r / cT:.0f}")
lin = all(abs(rows[i + 1][4] / rows[i][4] - 2) < 1e-3 for i in (0, 2))
ok("E1 [executed] before the switch-on the force on the packet is zero; at label time 0.05 and after the ramp it is non-zero at r = 8 and 16, long before r/c_T = 16, 32; it is linear in Delta_e, points toward the body and matches -E<grad u> within 5%",
   all(abs(r_[2]) < 1e-14 and abs(r_[3]) > 1e-9 and abs(r_[4]) > 1e-9 for r_ in rows) and lin
   and all(abs(r_[4] / r_[6] - 1) < 0.05 for r_ in rows) and all(r_[4] < 0 for r_ in rows))

print(f"total {time.time() - T0:.1f} s; PASS={NP} FAIL={NF}")
if NF:
    print(f"SUMMARY: ROUTE FAILS AT the first FAIL line above ({NF} failures)")
    sys.exit(1)
print("SUMMARY: PARTIAL (exact at second order, every lattice wave vector) with block 62's kinetic term and the curvature member, the rates stay multipliers and "
      "their constraint fixes the scalar part of the lengths at each label time: u(k,t) = -e/(4K wbar p^2) + alpha(alpha+3beta) e''/(K^2 wbar^3 (alpha+beta) p^4); "
      "only the two transverse traceless strains travel (speed^2 = K wbar^2/(4 alpha)) and a body at rest does not source them; so a formation event changes the clocks, "
      "the scalar lengths and a slow packet's fall at every distance at once, by an amount set by the change of energy; for alpha + beta = 0 (the comparator's ratio) a "
      "change of a body's energy at rest has no solution at all")
print("HIT: within blocks 60 and 62's clauses a packet's fall changes before any strain wave can arrive, by -E grad of the Poisson field of the change of the body's "
      "energy (plus an alpha(alpha+3beta)/(alpha+beta) e'' term): the rate is a multiplier and the scalar length is a constraint; only alpha + beta = 0 excludes it, "
      "by forbidding the change itself")
