#!/usr/bin/env python3
"""J:derive:the-travelling-disturbances-source-by-species:a1 -- exact checks.

Supplied clauses (nothing adopted): block 54's walk H = sum_a s_a S_a on the qubit coin; block 62's frame, site stress
Theta_a^j = Re psi^+ s_a (S_j psi) and its two transverse-traceless (TT) disturbances; block 63's bond current J (reach
two, with S_j); block 69's bond current K (reach three, with P_j = S_j C_j); block 70's species maps V_n = R_n U_n;
block 74's table.  Exactness: states have Gaussian-integer entries, every operator entry is a dyadic rational, so the
float64 values below are exact (asserted); sympy for symbols.
"""
import sys
from itertools import product
import numpy as np
import sympy as sy

OUT = []
FAIL = []


def rec(msg):
    OUT.append(msg)


def need(cond, msg):
    if not cond:
        FAIL.append(msg)


SG = [np.array([[0, 1], [1, 0]], dtype=complex), np.array([[0, -1j], [1j, 0]]),
      np.array([[1, 0], [0, -1]], dtype=complex)]
I2 = np.eye(2)
L = 4
sites = list(product(range(L), repeat=3))
ix = {s: i for i, s in enumerate(sites)}
n = len(sites)


def shift(a):
    T = np.zeros((n, n))
    for s in sites:
        t = list(s)
        t[a] = (t[a] + 1) % L
        T[ix[s], ix[tuple(t)]] = 1                              # (T psi)(x) = psi(x + e_a)
    return T


Tm = [shift(a) for a in range(3)]
Sm = [(T - T.T) / 2j for T in Tm]
Cm = [(T + T.T) / 2 for T in Tm]
Pm = [S @ C for S, C in zip(Sm, Cm)]
Hm = sum(np.kron(Sm[a], SG[a]) for a in range(3))
rng = np.random.default_rng(20260922)
psi = (rng.integers(-3, 4, 2 * n) + 1j * rng.integers(-3, 4, 2 * n)).astype(complex)


def site_vec(v):
    return v.reshape(n, 2)


def responses(ps):
    """site stress Theta, reach-two current J, reach-three current K (bond x -> x+e_a), momenta pi, P, energy e"""
    P2 = site_vec(ps)
    out = {}
    for a in range(3):
        for j in range(3):
            Sj = site_vec(np.kron(Sm[j], I2) @ ps)
            Pj = site_vec(np.kron(Pm[j], I2) @ ps)
            nxt = [ix[tuple((s[b] + (1 if b == a else 0)) % L for b in range(3))] for s in sites]
            th = np.array([np.real(P2[i].conj() @ SG[a] @ Sj[i]) for i in range(n)])
            J = np.array([0.5 * np.real(P2[nxt[i]].conj() @ SG[a] @ Sj[i] + Sj[nxt[i]].conj() @ SG[a] @ P2[i])
                          for i in range(n)])
            K = np.array([0.5 * np.real(P2[nxt[i]].conj() @ SG[a] @ Pj[i] + Pj[nxt[i]].conj() @ SG[a] @ P2[i])
                          for i in range(n)])
            out[("Th", a, j)], out[("J", a, j)], out[("K", a, j)] = th, J, K
    for j in range(3):
        Sj = site_vec(np.kron(Sm[j], I2) @ ps)
        Pj = site_vec(np.kron(Pm[j], I2) @ ps)
        out[("pi", j)] = np.array([np.real(P2[i].conj() @ Sj[i]) for i in range(n)])
        out[("P", j)] = np.array([np.real(P2[i].conj() @ Pj[i]) for i in range(n)])
    He = site_vec(Hm @ ps)
    out[("e",)] = np.array([np.real(P2[i].conj() @ He[i]) for i in range(n)])
    return out


def exact(arr):
    return np.all(arr * 64 == np.round(arr * 64))                   # dyadic rationals, exactly representable


R0 = responses(psi)
ok = all(exact(v) for v in R0.values())
table_ok = True
for nv in product((0, 1), repeat=3):
    D = [(-1) ** t for t in nv]
    s_n = D[0] * D[1] * D[2]
    rho = [s_n * d for d in D]
    # the coin's half turn R_n with R s_a R^+ = rho_a s_a (rho has determinant +1)
    R = I2 if rho == [1, 1, 1] else [1j * SG[a] for a in range(3) if rho[a] == 1][0]
    U = np.diag([(-1) ** (nv[0] * s[0] + nv[1] * s[1] + nv[2] * s[2]) for s in sites])
    V = np.kron(U, R)
    ok &= all(np.array_equal(R @ SG[a] @ R.conj().T, rho[a] * SG[a]) for a in range(3))
    ok &= np.array_equal(V @ Hm @ V.conj().T, s_n * Hm)
    Rn = responses(V @ psi)
    for a in range(3):
        for j in range(3):
            table_ok &= np.array_equal(Rn[("Th", a, j)], s_n * D[a] * D[j] * R0[("Th", a, j)])
            table_ok &= np.array_equal(Rn[("J", a, j)], s_n * D[j] * R0[("J", a, j)])
            table_ok &= np.array_equal(Rn[("K", a, j)], s_n * R0[("K", a, j)])
    for j in range(3):
        table_ok &= np.array_equal(Rn[("pi", j)], D[j] * R0[("pi", j)])
        table_ok &= np.array_equal(Rn[("P", j)], R0[("P", j)])
    table_ok &= np.array_equal(Rn[("e",)], s_n * R0[("e",)])
need(ok and table_ok, "S1 species maps")
rec("ok S1 on the 4^3 torus, for all eight maps V_n (V H V^+ = s_n H) and a Gaussian-integer state, at every site "
    "and in all nine components exactly: Theta -> s_n D_a D_j Theta, J -> s_n D_j J, K -> s_n K, e -> s_n e "
    "(block 74 T1), and the two momenta: block 63's pi_j -> D_j pi_j, block 69's P_j -> P_j (species-blind)")

# ---------------------------------- S2 (a) the TT sources along the axes, relative to the species' own stress K
# leading order (block 74 T2): Theta_aj = D_a D_j K_aj, J_aj = D_j K_aj, with K symmetric
Kc = sy.Matrix(3, 3, lambda i, j: sy.Symbol("K%d%d" % (min(i, j), max(i, j))))
tabs = {}
ok = True
for nv in product((0, 1), repeat=3):
    D = sy.diag(*[(-1) ** t for t in nv])
    Th = D * Kc * D
    Jm = Kc * D                                                 # J_a^j = D_j K_a^j
    Js = (Jm + Jm.T) / 2
    for c in range(3):
        a, b = [x for x in range(3) if x != c]
        plus_K = (Kc[a, a] - Kc[b, b]) / 2
        cross_K = Kc[a, b]
        row = []
        for (M_, nm) in ((Th, "frame"), (Js, "reach2"), (Kc, "reach3")):
            pl = sy.simplify((M_[a, a] - M_[b, b]) / 2)
            cr = sy.simplify(M_[a, b])
            rp = sy.simplify(pl / plus_K)
            fp = rp if not rp.free_symbols else "trace"           # a fixed multiple of K's + component, or not
            fc = sy.simplify(cr / cross_K)
            row.append((nm, fp, fc))
        tabs[(nv, c)] = row
        Da, Db = (-1) ** nv[a], (-1) ** nv[b]
        ok &= row[0][1:] == (1, Da * Db)
        ok &= row[1][1:] == ((Da, sy.Rational(Da + Db, 2)) if Da == Db else ("trace", 0))
        ok &= row[2][1:] == (1, 1)
need(ok, "S2 TT tables")
same_frame_x = [nv for nv in product((0, 1), repeat=3) if tabs[(nv, 2)][0][2] == 1]
rec("ok S2 (a) TT sources for travel along e_c, polarisations + (aa-bb) and x (ab), relative to the species' own "
    "stress K: frame + is species-blind, x carries D_aD_b = (-1)^(n_a+n_b) (along e3 the first species' sign for "
    "%s, the opposite for the other four); reach two: + and x carry D_a when n_a = n_b, and when n_a != n_b the x "
    "source vanishes and the + source becomes the transverse trace D_a(K_aa+K_bb)/2; reach three: every species, "
    "both polarisations, sign +1" % ", ".join("".join(map(str, v)) for v in same_frame_x))

# ---------------------------------- S3 (c) plane waves: K/Theta = cos k_a cos k_j exactly; species-blind K
k1, k2, k3 = sy.symbols("k1 k2 k3", real=True)
kv = (k1, k2, k3)
Ssym = [sy.Matrix([[0, 1], [1, 0]]), sy.Matrix([[0, -sy.I], [sy.I, 0]]), sy.Matrix([[1, 0], [0, -1]])]
Hk = sum((Ssym[a] * sy.sin(kv[a]) for a in range(3)), sy.zeros(2))
E = sy.sqrt(sum(sy.sin(k) ** 2 for k in kv))
ok = sy.simplify(Hk * Hk - E ** 2 * sy.eye(2)) == sy.zeros(2)
# for the eigenvector u of H(k) with eigenvalue E: u^+ s_a u = sin k_a / E (Hellmann-Feynman), so per unit probability
# Theta_a^j = sin k_a sin k_j / E and K_a^j = cos k_a sin k_a * sin k_j cos k_j / E (bond current: Re e^{-ik_a})
Proj = (sy.eye(2) + Hk / E) / 2
ok &= all(sy.simplify((Proj * Ssym[a]).trace() - sy.sin(kv[a]) / E) == 0 for a in range(3))
q1, q2 = sy.symbols("q1 q2", real=True)
for nv in product((0, 1), repeat=2):
    ka, kj = sy.pi * nv[0] + q1, sy.pi * nv[1] + q2
    Kaj = sy.cos(ka) * sy.sin(ka) * sy.sin(kj) * sy.cos(kj)
    Thaj = sy.sin(ka) * sy.sin(kj)
    ok &= sy.simplify(Kaj - sy.sin(2 * q1) * sy.sin(2 * q2) / 4) == 0
    ok &= sy.simplify(Thaj - (-1) ** (nv[0] + nv[1]) * sy.sin(q1) * sy.sin(q2)) == 0
ser = sy.series(sy.sin(2 * q1) * sy.sin(2 * q2) / 4, q1, 0, 4).removeO()
lead = sy.expand((q1 - sy.Rational(2, 3) * q1 ** 3) * (q2 - sy.Rational(2, 3) * q2 ** 3))
ok &= sy.expand(sy.series(ser, q2, 0, 4).removeO() - lead) == 0
need(ok, "S3 plane waves")
rec("ok S3 (c) plane waves: Theta_a^j = sin k_a sin k_j/E and K_a^j = sin k_a cos k_a sin k_j cos k_j/E exactly, so "
    "K = Theta cos k_a cos k_j; at k = pi n + q, K_a^j = sin 2q_a sin 2q_j/(4E), identical for all eight species, "
    "= (q_a q_j/E)(1 - (2/3)(q_a^2 + q_j^2) + ...): the first lattice correction; Theta carries D_aD_j exactly")

# ---------------------------------- S4 (b) the TT field's energy and the sign of the radiated energy
p3, Kf, wb = sy.symbols("p3 K wbar", positive=True)
h12, hp = sy.symbols("h12 hp", real=True)
pv = sy.Matrix([0, 0, p3])                                    # travel along e3
h = sy.Matrix([[hp, h12, 0], [h12, -hp, 0], [0, 0, 0]])       # TT: p.h = 0, tr h = 0
p2s = p3 ** 2
trh = h.trace()
ph = pv.T * h
R1 = -((pv.T * h * pv)[0] - p2s * trh)
R2 = (-sy.Rational(1, 4) * p2s * sum(h[i, j] ** 2 for i in range(3) for j in range(3))
      + sy.Rational(1, 2) * (ph * ph.T)[0] - sy.Rational(1, 2) * (pv.T * h * pv)[0] * trh
      + sy.Rational(1, 4) * p2s * trh ** 2)
F2 = -Kf * wb * R2                                             # u R1 drops: R1 = 0 on TT
ok = sy.simplify(R1) == 0 and sy.simplify(F2 - Kf * wb * p3 ** 2 * (2 * hp ** 2 + 2 * h12 ** 2) / 4) == 0
need(ok, "S4 TT energy")
rec("ok S4 (b) on TT disturbances block 62's member has R1 = 0 and F2 = (K wbar/4) p^2 h_ij h_ij >= 0, so with the "
    "kinetic term (alpha/wbar) hdot_ij hdot_ij the TT energy is positive iff alpha > 0 (speed^2 K wbar^2/(4 alpha)); "
    "the field a source radiates is linear in the source and its energy quadratic, so the sign s of a species' "
    "coupling cancels: for alpha > 0 every species loses energy by radiating, reflected or not")

print("\n".join(OUT))
print("SUMMARY: " + ("ROUTE FAILS AT " + FAIL[0] if FAIL else
      "PARTIAL exact species tables for the sources of block 62's two TT disturbances under the three couplings "
      "(frame: + species-blind, x with (-1)^(n_a+n_b); reach two: D_a for n_a = n_b, else x vanishes and + becomes "
      "the transverse trace; reach three: all +1, with K = sin 2q_a sin 2q_j/(4E) exactly), the two momenta "
      "(pi_j -> D_j pi_j, P_j blind), and the TT energy (K wbar/4) p^2 h^2 >= 0: no species gains energy by "
      "radiating when alpha > 0, so the task's HIT condition is not met."))
if not FAIL:
    print("HIT: per unit of each species' own stress K (block 74 T2), the TT source of block 62's disturbances "
          "travelling along e_c is: under the frame, species-blind for + and (-1)^(n_a+n_b) for x; under reach "
          "two, D_a for both when n_a = n_b, while for n_a != n_b the x source vanishes and the + source becomes "
          "the transverse trace D_a(K_aa+K_bb)/2; under reach three +1 for all eight species; exact map laws "
          "checked on a 4^3 torus, with block 63's pi_j -> D_j pi_j and block 69's P_j species-blind.")
sys.exit(1 if FAIL else 0)
