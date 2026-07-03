#!/usr/bin/env python3
"""Record density slows the local information front: an exactly-solved 1D toy
that BUILDS the named-not-built step "position-dependent record density ->
position-dependent front speed v(x) -> optical-metric potential Phi(x)".

WHAT THIS IS. The emergent-metric conformal-class note (2026-06-06) states:
"A position-dependent record-density (varying v_LR) would curve the conformal
class -- the seed of an emergent curved geometry / gravity. That extension is
beyond this note (the homogeneous free case gives the Minkowski conformal
class)" and lists the curving step as "named, not built". The weak-field map
note (PR #3385) calls the same step its M1 posit ("record-density n(x) ->
varying local front speed v_LR(x) -> curved effective metric"), an unaudited
posit. This runner builds that single step as an honest TOY: a minimal,
exactly-diagonalized model in which sites carrying records measurably slow the
local front, giving v_eff(x) and hence an optical-metric potential
Phi(x) = (v_eff(x)^2 - v_bare^2) / (2 v_bare^2).

THE TOY MODEL (one supplied dynamics, no fitted value, lattice units t=1):
  - a single particle hopping on an open 1D chain (one axis of the Lattice
    axiom's Z^3), H_chain = -t sum_x (|x+1><x| + h.c.);
  - a RECORD SITE x carries a frozen environment qubit (no self-Hamiltonian in
    the ancilla sector) coupled by the excitation-conserving registration
    coupling g (sigma+_a c_x + c_x^dag sigma-_a): the site's occupation
    amplitude is registered into the frozen qubit. In the one-excitation
    sector this is EXACTLY a quadratic "dangling-mode" model (checked, S1.1),
    so everything is exact diagonalization / transfer matrices -- no Monte
    Carlo anywhere (the pointer-contrast channel sum is an exact enumeration).
  - record DENSITY n: fraction of sites carrying record couplings (periodic
    dilution n = 1/m), or, for smooth profiles, coupling weight
    g(x)^2 = g0^2 n(x) (the two implementations agree at weak coupling, S2.5).

HEADLINE (verified by two independent methods + controls):
  v_eff(n) DECREASES monotonically with record density n -- frequency domain
  (exact Bloch dispersion / closed form / transfer-matrix scattering phases)
  AND time domain (exact wave-packet arrival, exact propagator light cone)
  agree. The slowing mechanism is exact and quantified: amplitude dwells in
  the record modes while being registered (delay = ancilla-dwell minus a
  small refraction advance, S3.7). A smooth record-density bump n(x) then
  defines v_eff(x) and the optical-metric potential Phi(x) <= 0, and the
  exact packet arrival matches the optical-metric (eikonal) time integral.

HONEST BOUNDARIES (see the companion note):
  - The chain hopping and the registration coupling are SUPPLIED toy dynamics
    (the axioms supply no dynamics; record-production dynamics is explicitly
    outside the Record axiom). The toy builds the n(x) -> v(x) -> Phi(x) LINK,
    not the axioms -> metric derivation.
  - The toy fixes only the DIMENSIONLESS cone field v_eff(x)/v_bare (the
    conformal class). The absolute scale (clock rate) is the supplied time
    unit of the toy Hamiltonian -- the clock-rate no-go boundary is
    respected and DEMONSTRATED (S4.3: rescaling the supplied clock leaves
    Phi(x) invariant and rescales every absolute speed).
  - Class-dependence finding: a projective pointer-copy record coupling
    (g n_x sigma^x_a, exactly decomposed into +/-g potential channels)
    ATTENUATES the front with almost no delay; the registration coupling
    DELAYS with almost no attenuation (S3.5). "Records slow the front" is a
    property of the registration class built here, not of every conceivable
    record coupling -- reported honestly.
  - Lieb-Robinson is cited as standard literature context only; the front
    statement used here (max group velocity = the free-model front speed) is
    reproven in-model via the exact propagator light cone (S3.3).

Sets no audit status.
"""
from __future__ import annotations

import numpy as np
import sympy as sp
import itertools

PASS = 0
FAIL = 0


def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"  [{tag}] {label}" + (f"  --  {detail}" if detail else ""))
    return bool(ok)


def section(t):
    print("\n" + "-" * 88 + "\n" + t + "\n" + "-" * 88)


# ============================================================ shared machinery
T_HOP = 1.0                       # lattice units
K0 = 2 * np.pi / 5                # carrier quasimomentum (avoids low-order zone folds)
E0 = -2 * T_HOP * np.cos(K0)      # = -(sqrt(5)-1)/2, exact below
V_BARE = 2 * T_HOP * np.sin(K0)   # bare group velocity at the carrier
G_REC = 0.4                       # headline registration coupling


def chain_H(L):
    H = np.zeros((L, L))
    for x in range(L - 1):
        H[x, x + 1] = -T_HOP
        H[x + 1, x] = -T_HOP
    return H


def dressed_H(L, g_site):
    """Chain + one frozen record mode per site with g_site[x] != 0."""
    rec = [x for x in range(L) if g_site[x] != 0.0]
    dim = L + len(rec)
    H = np.zeros((dim, dim))
    H[:L, :L] = chain_H(L)
    for i, s in enumerate(rec):
        H[s, L + i] = g_site[s]
        H[L + i, s] = g_site[s]
    return H, dim, rec


def evolve_packet(H, dim, L, x0, sigx, times, x_det, k0=K0):
    """Exact spectral evolution of a Gaussian packet; returns P_past_det(t),
    A_ancilla(t)."""
    w, V = np.linalg.eigh(H)
    xs = np.arange(L)
    psi0 = np.zeros(dim, dtype=complex)
    psi0[:L] = np.exp(-((xs - x0) ** 2) / (4.0 * sigx**2) + 1j * k0 * xs)
    psi0 /= np.linalg.norm(psi0)
    c = V.conj().T @ psi0
    P, A = [], []
    for tt in times:
        psi = V @ (np.exp(-1j * w * tt) * c)
        P.append(float(np.sum(np.abs(psi[x_det:L]) ** 2)))
        A.append(float(np.sum(np.abs(psi[L:]) ** 2)))
    return np.array(P), np.array(A)


def first_half_crossing(times, P):
    """Arrival time = first crossing of half the transmitted plateau (max over
    the window; window chosen to end before any boundary bounce)."""
    Pmax = float(P.max())
    half = Pmax / 2.0
    i = int(np.argmax(P >= half))
    t_arr = times[i - 1] + (half - P[i - 1]) / (P[i] - P[i - 1]) * (times[i] - times[i - 1])
    return float(t_arr), Pmax


def bloch_vg_at_E(E_target, g, m, nk=8001):
    """Hellmann-Feynman group velocity |dE/dK| of the Bloch band nearest
    E_target for the periodic medium with one record mode every m sites."""
    dim = m + 1
    ks = np.linspace(1e-9, np.pi / m - 1e-9, nk)
    best = None
    for K in ks:
        H = np.zeros((dim, dim), dtype=complex)
        dH = np.zeros((dim, dim), dtype=complex)
        for j in range(m - 1):
            H[j, j + 1] += -T_HOP
            H[j + 1, j] += -T_HOP
        H[m - 1, 0] += -T_HOP * np.exp(1j * K * m)
        H[0, m - 1] += -T_HOP * np.exp(-1j * K * m)
        dH[m - 1, 0] += -T_HOP * 1j * m * np.exp(1j * K * m)
        dH[0, m - 1] += T_HOP * 1j * m * np.exp(-1j * K * m)
        H[0, m] += g
        H[m, 0] += g
        w, v = np.linalg.eigh(H)
        for i, wi in enumerate(w):
            if best is None or abs(wi - E_target) < abs(best[0] - E_target):
                vel = abs(float(np.real(v[:, i].conj() @ dH @ v[:, i])))
                best = (float(wi), vel)
    return best


def bloch_vfront(g, m, nk=4001):
    """Front speed of the periodic medium: max |dE/dK| over all bands and K."""
    dim = m + 1
    ks = np.linspace(1e-9, np.pi / m - 1e-9, nk)
    vmax = 0.0
    for K in ks:
        H = np.zeros((dim, dim), dtype=complex)
        dH = np.zeros((dim, dim), dtype=complex)
        for j in range(m - 1):
            H[j, j + 1] += -T_HOP
            H[j + 1, j] += -T_HOP
        H[m - 1, 0] += -T_HOP * np.exp(1j * K * m)
        H[0, m - 1] += -T_HOP * np.exp(-1j * K * m)
        dH[m - 1, 0] += -T_HOP * 1j * m * np.exp(1j * K * m)
        dH[0, m - 1] += T_HOP * 1j * m * np.exp(-1j * K * m)
        H[0, m] += g
        H[m, 0] += g
        w, v = np.linalg.eigh(H)
        for i in range(dim):
            vel = abs(float(np.real(v[:, i].conj() @ dH @ v[:, i])))
            vmax = max(vmax, vel)
    return vmax


def v_med_closed(E, g):
    """Exact n=1 medium group velocity at energy E (derived symbolically in
    S1): eps(E) = E - g^2/E, v = v_k(eps) / (1 + g^2/E^2)."""
    eps = E - g**2 / E
    if abs(eps) >= 2 * T_HOP:
        return 0.0
    kp = np.arccos(-eps / (2 * T_HOP))
    return 2 * T_HOP * np.sin(kp) / (1 + g**2 / E**2)


def transfer_wigner_delay(E, g, W, dE=1e-6):
    """Exact transfer-matrix scattering phase derivative (Wigner delay,
    relative to the bare chain) through a slab of W consecutive record sites,
    with the frozen record mode eliminated exactly: eps_eff(E) = g^2/E."""
    def phase(EE, eps=None):
        k = np.arccos(-EE / (2 * T_HOP))
        if eps is None:
            eps = g**2 / EE
        M = np.eye(2, dtype=complex)
        # recursion -t(psi_{x+1}+psi_{x-1}) + eps psi_x = E psi_x
        #   =>  psi_{x+1} = ((eps - E)/t) psi_x - psi_{x-1}
        Mx = np.array([[(eps - EE) / T_HOP, -1.0], [1.0, 0.0]], dtype=complex)
        for _ in range(W):
            M = Mx @ M
        z = np.exp(1j * k)
        # psi_x = z^x + r z^-x (x<=0 side), tau z^x (x>=W side); M maps
        # (psi_0, psi_-1) -> (psi_W, psi_{W-1}).  NOTE: with this ansatz a bare
        # slab (eps=0) gives tau = 1 exactly, so arg(tau) is the EXTRA phase
        # relative to the bare chain and d arg(tau)/dE is the delay RELATIVE to
        # the bare chain over the same W sites.
        a, b, c, d = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
        # solve the 2x2 linear system:
        #   a (1+r) + b (z^-1 + r z) = tau z^W
        #   c (1+r) + d (z^-1 + r z) = tau z^(W-1)
        Mat = np.array([[a + b * z, -z**W], [c + d * z, -z ** (W - 1)]], dtype=complex)
        rhs = -np.array([a + b / z, c + d / z], dtype=complex)
        r_, tau_ = np.linalg.solve(Mat, rhs)
        return np.angle(tau_), abs(tau_)
    # construction sanity (checked, not asserted): a bare slab transmits with
    # tau = 1 exactly in this ansatz
    ph0, a0 = phase(E, eps=0.0)
    assert abs(a0 - 1.0) < 1e-10 and abs(ph0) < 1e-10, "bare-slab tau != 1"
    ph_p, _ = phase(E + dE)
    ph_m, _ = phase(E - dE)
    _, absT = phase(E)
    ph_un = np.unwrap([ph_m, ph_p])
    return (ph_un[1] - ph_un[0]) / (2 * dE), absT


def main():
    print("=" * 88)
    print("RECORD DENSITY SLOWS THE LOCAL FRONT -> OPTICAL METRIC: EXACT 1D TOY")
    print("=" * 88)
    print(f"lattice units t=1; carrier K0=2*pi/5, E0={E0:+.6f}, v_bare={V_BARE:.6f}; "
          f"headline g={G_REC}")

    # ================================================================== S1
    section("S1: the model and the exact bridge (symbolic derivations, not assertions)")

    # --- S1.1 frozen record QUBIT == dangling mode in the one-excitation sector
    Lq, rec_q = 5, [1, 3]
    # full spin construction: chain sites are hardcore (qubit) sites, ancilla
    # qubits attached at rec_q; build the FULL 2^(L+R) Hamiltonian and project
    # onto the one-excitation sector.
    nq = Lq + len(rec_q)
    dimF = 2**nq
    # explicit qubit ops in basis |0>,|1>
    sminus = np.array([[0.0, 1.0], [0.0, 0.0]])   # lowers |1> -> |0>
    splus = sminus.T

    def op_at(op, j):
        out = np.array([[1.0]])
        for i in range(nq):
            out = np.kron(out, op if i == j else np.eye(2))
        return out

    Hfull = np.zeros((dimF, dimF))
    for x in range(Lq - 1):
        Hfull += -T_HOP * (op_at(splus, x + 1) @ op_at(sminus, x)
                           + op_at(splus, x) @ op_at(sminus, x + 1))
    for i, s in enumerate(rec_q):
        a = Lq + i
        Hfull += G_REC * (op_at(splus, a) @ op_at(sminus, s)
                          + op_at(splus, s) @ op_at(sminus, a))
    # number operator
    Nop = sum(op_at(np.diag([0.0, 1.0]), j) for j in range(nq))
    occ = np.diag(Nop)
    sec = np.where(np.isclose(occ, 1.0))[0]
    Hsec = Hfull[np.ix_(sec, sec)]
    g_site = np.zeros(Lq)
    for s in rec_q:
        g_site[s] = G_REC
    Hquad, dq, _ = dressed_H(Lq, g_site)
    ev1 = np.sort(np.linalg.eigvalsh(Hsec))
    ev2 = np.sort(np.linalg.eigvalsh(Hquad))
    check("S1.1 record = site state registered into a FROZEN environment qubit "
          "(no self-Hamiltonian): the one-excitation sector of the full 2^7 qubit model "
          "IS the quadratic dangling-mode model (spectra equal)",
          ev1.shape == ev2.shape and np.max(np.abs(ev1 - ev2)) < 1e-12,
          f"max|dE|={np.max(np.abs(ev1 - ev2)):.2e}")

    # --- S1.2 exact elimination of the frozen mode: eps_eff(E) = g^2/E
    Es, ks = sp.symbols("E k")
    ts, gs = sp.symbols("t g", positive=True)
    psi0_s, d_s = sp.symbols("psi0 d")
    elim = sp.solve(sp.Eq(Es * d_s, gs * psi0_s), d_s)[0]
    eps_eff = sp.simplify(gs * elim / psi0_s)   # coupling g*d back onto the site
    check("S1.2 frozen record mode eliminated exactly: energy-dependent on-site "
          "weight eps_eff(E) = g^2/E (sympy)",
          sp.simplify(eps_eff - gs**2 / Es) == 0, f"eps_eff={eps_eff}")

    # --- S1.3 single-record transmission amplitude DERIVED + unitarity
    r_s, tau_s = sp.symbols("r tau")
    E_k = -2 * ts * sp.cos(ks)
    psi = lambda x: sp.exp(sp.I * ks * x) + r_s * sp.exp(-sp.I * ks * x) if x < 0 \
        else tau_s * sp.exp(sp.I * ks * x)
    cont = sp.Eq(1 + r_s, tau_s)                                   # psi_0 two ways
    schr0 = sp.Eq(-ts * (psi(-1) + tau_s * sp.exp(sp.I * ks)) + (gs**2 / E_k) * tau_s,
                  E_k * tau_s)
    sol = sp.solve([cont, schr0], [r_s, tau_s], dict=True)[0]
    tau_expr = sp.simplify(sol[tau_s])
    tau_target = 1 / (1 + sp.I * gs**2 / (2 * ts * E_k * sp.sin(ks)))
    diff_simpl = sp.simplify(tau_expr - tau_target)
    if diff_simpl != 0:
        # robust numeric confirmation on a grid of exact substitutions
        diff_simpl = max(abs(complex((tau_expr - tau_target).subs(
            [(ts, 1), (gs, sp.Rational(2, 5)), (ks, sp.pi * sp.Rational(p, q))]).evalf()))
            for p, q in [(2, 5), (1, 3), (3, 7), (5, 11)])
        ok_tau = diff_simpl < 1e-12
    else:
        ok_tau = True
    check("S1.3a single-record transmission DERIVED from the lattice Schroedinger "
          "matching: tau(E) = 1/(1 + i g^2/(2 t E sin k)) with E = -2t cos k (sympy)",
          ok_tau, f"residual={diff_simpl}")
    uni = (sp.Abs(tau_expr.subs([(ts, 1), (gs, sp.Rational(2, 5))])) ** 2
           + sp.Abs(sol[r_s].subs([(ts, 1), (gs, sp.Rational(2, 5))])) ** 2 - 1)
    uni_num = complex(uni.subs(ks, sp.pi * sp.Rational(2, 5)).evalf())
    check("S1.3b unitarity |tau|^2 + |r|^2 = 1 at the carrier (exact evaluation)",
          abs(uni_num) < 1e-12, f"residual={abs(uni_num):.2e}")

    # --- S1.4 Wigner delay: exact sign structure
    # phi(E) = -arctan(g^2 / (2 t f(E))) with f(E) = E sin k = E sqrt(1-E^2/4t^2),
    # so  dphi/dE = [2 t g^2 / (4 t^2 f^2 + g^4)] * f'(E):  sign(tau_W) = sign(f').
    fE = Es * sp.sqrt(1 - Es**2 / (4 * ts**2))
    phiE = -sp.atan(gs**2 / (2 * ts * fE))
    ratio = sp.simplify(sp.diff(phiE, Es) / sp.diff(fE, Es))
    ratio_target = 2 * ts * gs**2 / (4 * ts**2 * fE**2 + gs**4)
    sign_boundary = sp.solve(sp.Eq(sp.diff(fE, Es), 0), Es)
    def tauW_num(E, g):
        dE = 1e-7
        def ph(EE):
            k = np.arccos(-EE / 2.0)
            return np.angle(1.0 / (1.0 + 1j * g**2 / (2.0 * EE * np.sin(k))))
        return (ph(E + dE) - ph(E - dE)) / (2 * dE)
    tw0 = tauW_num(E0, G_REC)
    inner = np.concatenate([np.linspace(-1.35, -0.15, 30), np.linspace(0.15, 1.35, 30)])
    inner_pos = all(tauW_num(E, G_REC) > 0 for E in inner)
    edge_neg = tauW_num(-1.9, G_REC) < 0 and tauW_num(1.9, G_REC) < 0
    check("S1.4 per-record Wigner delay, exact sign structure (sympy): tau_W = "
          "[2tg^2/(4t^2 f^2 + g^4)] f'(E) with f = E sin k, so tau_W > 0 exactly on the "
          "INNER band |E| < sqrt(2) t (this includes the carrier and every fast mode) "
          "and < 0 only in the slow band-edge skin |E| > sqrt(2) t -- verified at the "
          "carrier, on inner-band grids both sides of the antiresonance, and at E=-1.9, "
          "+1.9 (the honest band-edge advance; the FRONT statement S2.3 is "
          "carrier-independent)",
          sp.simplify(ratio - ratio_target) == 0
          and sorted(sp.simplify(s) for s in sign_boundary)[0] == -sp.sqrt(2) * ts
          and tw0 > 0 and inner_pos and edge_neg,
          f"tau_W(E0)={tw0:.6f}; sign flips at E=+/-sqrt(2)t")

    # --- S1.5 pointer-energy antiresonance (full-record opacity limit)
    tau_E = 1 / (1 + sp.I * gs**2 / (2 * ts * Es * sp.sqrt(1 - Es**2 / (4 * ts**2))))
    lim0 = sp.limit(tau_E.subs([(ts, 1), (gs, sp.Rational(2, 5))]), Es, 0)
    check("S1.5 antiresonance: tau(E -> 0) = 0 (sympy limit) -- at the frozen "
          "pointer energy a single record is perfectly opaque (the full-record/gap limit)",
          sp.simplify(lim0) == 0, f"limit={lim0}")

    # --- S1.6 n=1 medium: exact dispersion and gap (sympy)
    # Bloch: E psi = -2t cos(k) psi + g^2/E psi  =>  eps(k) = E - g^2/E
    eps_of_E = Es - gs**2 / Es
    gap = 2 * (sp.sqrt(ts**2 + gs**2) - ts)
    # band edges: E satisfies E - g^2/E = +/- 2t ; E_+ band bottom at eps=-2t:
    Eb = sp.symbols("Eb")
    edges = sp.solve(sp.Eq(Eb - gs**2 / Eb, -2 * ts), Eb)
    Ep_min = sp.simplify([e for e in edges if sp.simplify(e.subs([(ts, 1), (gs, 1)])) > 0][0])
    Em_max_edges = sp.solve(sp.Eq(Eb - gs**2 / Eb, 2 * ts), Eb)
    Em_max = sp.simplify([e for e in Em_max_edges
                          if sp.simplify(e.subs([(ts, 1), (gs, 1)])) < 0][0])
    gap_derived = sp.simplify(Ep_min - Em_max)
    check("S1.6 n=1 medium exact inverse dispersion eps(E) = E - g^2/E (sympy Bloch "
          "elimination); spectral GAP around the pointer energy = 2(sqrt(t^2+g^2)-t), "
          "which closes as g -> 0",
          sp.simplify(gap_derived - gap) == 0
          and sp.limit(gap, gs, 0) == 0,
          f"gap={sp.simplify(gap_derived)}")

    # --- S1.7 closed-form medium group velocity (implicit differentiation)
    # v_med = dE/dk = (deps/dk) / (deps/dE) = v_k(eps) / (1 + g^2/E^2)
    deps_dE = sp.diff(eps_of_E, Es)
    check("S1.7 closed-form medium group velocity v_med(E) = v_k(eps(E)) / (1 + g^2/E^2) "
          "(deps/dE = 1 + g^2/E^2, sympy)",
          sp.simplify(deps_dE - (1 + gs**2 / Es**2)) == 0,
          f"v_med(E0,g={G_REC}) = {v_med_closed(E0, G_REC):.6f} vs v_bare {V_BARE:.6f}")

    # ================================================================== S2
    section("S2: deliverable (a) -- v_eff(n) DECREASES monotonically with record "
            "density (frequency domain)")

    ns = [(8, 0.125), (4, 0.25), (2, 0.5), (1, 1.0)]
    vg = {}
    for m, n in ns:
        Eb_, v_ = bloch_vg_at_E(E0, G_REC, m)
        vg[n] = v_
        print(f"    n={n:5.3f}: Bloch band E={Eb_:+.6f}  v_g(E0)={v_:.6f}")
    seq = [V_BARE] + [vg[n] for _, n in ns]
    check("S2.1 carrier group velocity v_g(E0; n) strictly decreasing in record "
          "density n in {0, 1/8, 1/4, 1/2, 1} (exact Bloch + Hellmann-Feynman)",
          all(seq[i] > seq[i + 1] for i in range(len(seq) - 1)),
          " > ".join(f"{v:.4f}" for v in seq))
    check("S2.2 n=1 Bloch velocity matches the S1.7 closed form",
          abs(vg[1.0] - v_med_closed(E0, G_REC)) < 1e-3,
          f"|diff|={abs(vg[1.0] - v_med_closed(E0, G_REC)):.2e}")

    vF = {}
    for m, n in ns:
        vF[n] = bloch_vfront(G_REC, m)
        print(f"    n={n:5.3f}: front speed v_F = {vF[n]:.6f}")
    seqF = [2 * T_HOP] + [vF[n] for _, n in ns]
    check("S2.3 FRONT speed v_F(n) = max_k |dE/dk| (the in-model information front, "
          "v_LR analogue) strictly decreasing in n and < 2t for every n > 0",
          all(seqF[i] > seqF[i + 1] for i in range(len(seqF) - 1)),
          " > ".join(f"{v:.4f}" for v in seqF))
    v_tiny = bloch_vfront(1e-4, 1)
    check("S2.4 limit n*g^2 -> 0 restores the bare front: v_F(g=1e-4, n=1) = 2t "
          "within 1e-3 (no records, no slowing)",
          abs(v_tiny - 2 * T_HOP) < 1e-3, f"v_F={v_tiny:.6f}")

    g_weak = 0.15
    _, v_dil = bloch_vg_at_E(E0, g_weak, 2)
    v_uni = v_med_closed(E0, g_weak / np.sqrt(2.0))
    shift_dil = V_BARE - v_dil
    shift_uni = V_BARE - v_uni
    check("S2.5 'density' is well-defined: dilution (every 2nd site, g0) and uniform "
          "weighting (every site, g0/sqrt(2), i.e. g^2 halved) give the SAME velocity "
          "shift at weak coupling within 5%",
          abs(shift_dil - shift_uni) < 0.05 * shift_uni,
          f"shift_dilute={shift_dil:.5f} shift_uniform={shift_uni:.5f}")

    # transfer-matrix route (independent of Bloch): per-site delay extracted as
    # the least-squares slope of the exact slab Wigner delay tau_W(W) over
    # W = 200..400 (the slope averages out the Fabry-Perot interface
    # oscillation, which is W-periodic and does not grow per site)
    Ws = np.arange(200, 401)
    tws = np.array([transfer_wigner_delay(E0, G_REC, int(W))[0] for W in Ws])
    Amat = np.vstack([Ws.astype(float), np.ones(len(Ws))]).T
    per_site_tm, _ = np.linalg.lstsq(Amat, tws, rcond=None)[0]
    per_site_pred = 1.0 / v_med_closed(E0, G_REC) - 1.0 / V_BARE
    _, absT_B = transfer_wigner_delay(E0, G_REC, 120)
    check("S2.6 transfer-matrix scattering phase (independent frequency-domain route, "
          "no Bloch input): bulk per-record-site group delay = least-squares slope of "
          "the exact slab Wigner delay over W=200..400 equals 1/v_med - 1/v_bare "
          "within 0.5%",
          abs(per_site_tm - per_site_pred) < 0.005 * per_site_pred,
          f"TM slope={per_site_tm:.6f} closed-form={per_site_pred:.6f} "
          f"|T|_120={absT_B:.4f}")

    tw_g1 = tauW_num(E0, 0.1)
    tw_g2 = tauW_num(E0, 0.2)
    ratio_g = tw_g2 / tw_g1
    seq_rich = []
    for gg in [0.2, 0.1, 0.05, 0.025]:
        seq_rich.append((2 * T_HOP - bloch_vfront(gg, 1, nk=20001)) / gg)
    rich = [2 * seq_rich[i + 1] - seq_rich[i] for i in range(len(seq_rich) - 1)]
    check("S2.7 controlled coupling scaling: per-record delay tau_W proportional to g^2 "
          "(tau_W(0.2)/tau_W(0.1) = 4 within 3%) and the n=1 front-speed law "
          "v_F = 2t - sqrt(2) g + O(g^2) (Richardson of (2t-v_F)/g -> sqrt(2) within 1e-3)",
          abs(ratio_g - 4.0) < 0.12 and abs(rich[-1] - np.sqrt(2.0)) < 1e-3,
          f"ratio={ratio_g:.4f}; Richardson={rich[-1]:.6f} vs sqrt2={np.sqrt(2):.6f}")

    # ================================================================== S3
    section("S3: deliverable (c) + the independent TIME-DOMAIN method and controls")

    # --- uniform slabs W=120, 240 embedded in bare leads
    L = 1000
    x0, sigx = 140, 22
    x_det = 720
    times = np.arange(0.0, 392.0, 0.5)
    Pb, _ = evolve_packet(chain_H(L), L, L, x0, sigx, times, x_det)
    tb, plat_b = first_half_crossing(times, Pb)

    def slab_run(W):
        g_site = np.zeros(L)
        g_site[350:350 + W] = G_REC
        H, dim, _ = dressed_H(L, g_site)
        P, A = evolve_packet(H, dim, L, x0, sigx, times, x_det)
        t_arr, plat = first_half_crossing(times, P)
        return t_arr, plat, A

    t120, plat120, A120 = slab_run(120)
    t240, plat240, A240 = slab_run(240)
    pred120 = 120 * per_site_pred
    pred240 = 240 * per_site_pred
    print(f"    bare arrival {tb:.2f} (plateau {plat_b:.4f}); W=120 delay "
          f"{t120 - tb:.2f} (pred {pred120:.2f}, plateau {plat120:.4f}); W=240 delay "
          f"{t240 - tb:.2f} (pred {pred240:.2f}, plateau {plat240:.4f})")
    check("S3.1 exact wave-packet arrival through a W=120 record slab: measured delay "
          "matches the frequency-domain prediction W (1/v_med - 1/v_bare) within 5% "
          "(two INDEPENDENT methods agree)",
          abs((t120 - tb) - pred120) < 0.05 * pred120,
          f"delay={t120 - tb:.2f} pred={pred120:.2f} "
          f"ratio={(t120 - tb) / pred120:.4f}")
    per_site_wp = ((t240 - tb) - (t120 - tb)) / 120.0
    check("S3.2 two-width subtraction (W=240 minus W=120) cancels the O(1) boundary "
          "terms: per-site time-domain delay matches the closed form within 3%",
          abs(per_site_wp - per_site_pred) < 0.03 * per_site_pred,
          f"wp={per_site_wp:.6f} closed-form={per_site_pred:.6f}")

    # --- propagator light cone (in-model v_LR statement)
    def cone_radius(Lc, with_records, tt, thr2=1e-6):
        xc = Lc // 2
        if with_records:
            g_site = np.full(Lc, G_REC)
            H, dim, _ = dressed_H(Lc, g_site)
        else:
            H, dim = chain_H(Lc), Lc
        w, V = np.linalg.eigh(H)
        src = np.zeros(dim, dtype=complex)
        src[xc] = 1.0
        c = V.conj().T @ src
        psi = V @ (np.exp(-1j * w * tt) * c)
        d = np.abs(psi[:Lc]) ** 2
        idx = np.where(d > thr2)[0]
        return max(abs(int(idx[0]) - xc), abs(int(idx[-1]) - xc))

    rb1, rb2 = cone_radius(600, False, 60.0), cone_radius(600, False, 120.0)
    rr1, rr2 = cone_radius(600, True, 60.0), cone_radius(600, True, 120.0)
    slope_b = (rb2 - rb1) / 60.0
    slope_r = (rr2 - rr1) / 60.0
    check("S3.3 in-model information front (exact one-particle propagator light cone, "
          "|G(x,t)|^2 > 1e-6 threshold): cone slope ratio records/bare matches the Bloch "
          "front-speed ratio v_F(1)/2t within 2% (absolute slopes within 5%) -- the "
          "Lieb-Robinson-style statement reproven in-model, not imported",
          abs(slope_r / slope_b - vF[1.0] / (2 * T_HOP)) < 0.02
          and abs(slope_b - 2 * T_HOP) < 0.05 * 2 * T_HOP
          and abs(slope_r - vF[1.0]) < 0.05 * vF[1.0],
          f"slopes: bare {slope_b:.4f} (2t), records {slope_r:.4f} (vF={vF[1.0]:.4f})")

    # --- gauge invariance
    rng = np.random.default_rng(7)
    Lg = 500
    g_site = np.zeros(Lg)
    g_site[200:280] = G_REC
    Hg, dimg, _ = dressed_H(Lg, g_site)
    phases = rng.uniform(0, 2 * np.pi, dimg)
    U = np.exp(1j * phases)
    Hg2 = (U[:, None] * Hg) * np.conj(U)[None, :]
    wg, Vg = np.linalg.eigh(Hg)
    wg2, Vg2 = np.linalg.eigh(Hg2)
    xs = np.arange(Lg)
    psi0 = np.zeros(dimg, dtype=complex)
    psi0[:Lg] = np.exp(-((xs - 120) ** 2) / (4 * 20.0**2) + 1j * K0 * xs)
    psi0 /= np.linalg.norm(psi0)
    dmax = 0.0
    for tt in [120.0, 200.0]:
        p1 = np.abs(Vg @ (np.exp(-1j * wg * tt) * (Vg.conj().T @ psi0))) ** 2
        p2 = np.abs(Vg2 @ (np.exp(-1j * wg2 * tt) * (Vg2.conj().T @ (U * psi0)))) ** 2
        dmax = max(dmax, float(np.max(np.abs(p1 - p2))))
    check("S3.4 the delay is physical, not convention: under arbitrary local phase "
          "redefinitions (random U(1) frame on every site AND every record mode) all "
          "densities/arrival observables are unchanged to machine precision",
          dmax < 1e-12, f"max density diff={dmax:.2e}")

    # --- registration class vs projective pointer class (exact enumeration)
    Lc = 320
    rec_sites = list(range(140, 164, 3))
    x0c, sigc, detc = 60, 18, 220
    tgrid = np.arange(0.0, 132.0, 0.5)
    Hb_c = chain_H(Lc)
    tb_c, plat_bc = first_half_crossing(tgrid, evolve_packet(Hb_c, Lc, Lc, x0c, sigc,
                                                             tgrid, detc)[0])
    Pacc = np.zeros(len(tgrid))
    for signs in itertools.product([1, -1], repeat=len(rec_sites)):
        Hch = Hb_c.copy()
        for s, sg in zip(rec_sites, signs):
            Hch[s, s] = sg * G_REC
        Pacc += evolve_packet(Hch, Lc, Lc, x0c, sigc, tgrid, detc)[0]
    Pacc /= 2.0 ** len(rec_sites)
    tp_c, plat_pc = first_half_crossing(tgrid, Pacc)
    g_site = np.zeros(Lc)
    for s in rec_sites:
        g_site[s] = G_REC
    Hd_c, dimd, _ = dressed_H(Lc, g_site)
    td_c, plat_dc = first_half_crossing(tgrid, evolve_packet(Hd_c, dimd, Lc, x0c, sigc,
                                                             tgrid, detc)[0])
    print(f"    pointer copy (g n sigma^x, exact 2^8-channel enumeration): delay "
          f"{tp_c - tb_c:+.3f}, plateau {plat_pc:.4f}")
    print(f"    amplitude registration (frozen-mode copy): delay {td_c - tb_c:+.3f}, "
          f"plateau {plat_dc:.4f}")
    check("S3.5 class-dependence control (honest): the projective pointer-copy record "
          "(g n_x sigma^x_a; exact +/-g channel enumeration, no sampling) ATTENUATES "
          "(plateau < 0.8) with small delay, while the amplitude-registration record "
          "DELAYS (> 5x the pointer delay) with little attenuation (plateau > 0.95): "
          "the slowing is a property of the registration class this toy builds",
          (plat_pc < 0.8) and (plat_dc > 0.95) and (td_c - tb_c) > 5 * (tp_c - tb_c),
          f"delays {td_c - tb_c:.3f} vs {tp_c - tb_c:.3f}; plateaus {plat_dc:.3f} vs "
          f"{plat_pc:.3f}")

    # --- full-record opacity at the pointer energy (time domain)
    La = 700
    g_site = np.zeros(La)
    g_site[300:400] = G_REC
    Ha, dima, _ = dressed_H(La, g_site)
    ta_grid = np.arange(0.0, 262.0, 1.0)
    P_anti, _ = evolve_packet(Ha, dima, La, 150, 25, ta_grid, 450, k0=np.pi / 2)
    P_anti_bare, _ = evolve_packet(chain_H(La), La, La, 150, 25, ta_grid, 450,
                                   k0=np.pi / 2)
    check("S3.6 full-record limit: a packet AT the pointer energy (k0=pi/2, E=0, the "
          "S1.5 antiresonance / S1.6 gap) is blocked: transmitted weight < 1e-3 while "
          "the bare chain transmits > 0.9 -- records at full back-action close the cone "
          "(v_eff -> 0 / gap), the other end of the dial from S2.4",
          float(P_anti.max()) < 1e-3 and float(P_anti_bare.max()) > 0.9,
          f"records {float(P_anti.max()):.2e} vs bare {float(P_anti_bare.max()):.4f}")

    # --- mechanism accounting: delay = ancilla dwell - refraction advance
    f_anc = G_REC**2 / E0**2
    epsm = E0 - G_REC**2 / E0
    kp = np.arccos(-epsm / (2 * T_HOP))
    v_kp = 2 * T_HOP * np.sin(kp)
    dwell_pred = 240 * f_anc / v_kp
    refr_pred = 240 * (1.0 / v_kp - 1.0 / V_BARE)
    trapz = getattr(np, "trapezoid", None) or np.trapz
    dwell_meas = float(trapz(A240, times))
    check("S3.7 the MECHANISM, quantified: measured time-integrated record-mode "
          "occupation (W=240 slab) equals the closed-form registration dwell "
          "W f/v_k' (f = g^2/E^2) within 10%, and delay = dwell + refraction "
          "(W(1/v_k'-1/v_bare) < 0) holds within 10%: the front is slow because "
          "amplitude DWELLS in the record modes while being registered",
          abs(dwell_meas - dwell_pred) < 0.10 * dwell_pred
          and abs((t240 - tb) - (dwell_pred + refr_pred)) < 0.10 * (dwell_pred + refr_pred),
          f"dwell meas={dwell_meas:.2f} pred={dwell_pred:.2f}; "
          f"dwell+refr={dwell_pred + refr_pred:.2f} vs delay={t240 - tb:.2f}")

    # --- windowed imprint
    iA = int(np.searchsorted(times, 330.0))
    A_late1, A_late2 = float(A240[iA]), float(A240[-1])
    check("S3.8 windowed imprint (honest): after the packet exits, a nonzero record-mode "
          "occupation REMAINS in the slab (> 5e-4) and persists to the end of the window "
          "(>= half its t=330 value; the slow residual leak of a unitary toy is reported, "
          "not hidden)",
          A_late1 > 5e-4 and A_late2 >= 0.5 * A_late1,
          f"A(330)={A_late1:.2e} A(391.5)={A_late2:.2e}")

    # ================================================================== S4
    section("S4: deliverable (b) -- the optical-metric map for a smooth record-density "
            "profile (and the clock-rate no-go boundary)")

    Lp = 1400
    xsp = np.arange(Lp)
    xc_p, sig_p, g0_p = 700.0, 60.0, 0.45
    nprof = np.exp(-((xsp - xc_p) ** 2) / (2 * sig_p**2))
    nprof[nprof < 1e-4] = 0.0
    gprof = g0_p * np.sqrt(nprof)
    v_x = np.array([v_med_closed(E0, gx) if gx > 0 else V_BARE for gx in gprof])
    Phi_x = (v_x**2 - V_BARE**2) / (2 * V_BARE**2)
    print("    record-density bump n(x) = exp(-(x-700)^2 / (2*60^2)), g(x)^2 = g0^2 n(x), "
          f"g0={g0_p}")
    print("    x:      " + "".join(f"{x:>9d}" for x in [400, 550, 640, 700, 760, 850, 1000]))
    print("    n(x):   " + "".join(f"{nprof[x]:>9.4f}" for x in [400, 550, 640, 700, 760, 850, 1000]))
    print("    v_eff:  " + "".join(f"{v_x[x]:>9.4f}" for x in [400, 550, 640, 700, 760, 850, 1000]))
    print("    Phi(x): " + "".join(f"{Phi_x[x]:>9.4f}" for x in [400, 550, 640, 700, 760, 850, 1000]))
    order_ok = all((nprof[a] > nprof[b]) == (Phi_x[a] < Phi_x[b])
                   for a, b in [(700, 760), (760, 850), (850, 1000), (700, 550), (640, 400)])
    check("S4.1 the optical-metric map EXHIBITED: Phi(x) = (v_eff(x)^2 - v_bare^2) / "
          "(2 v_bare^2) <= 0 everywhere, = 0 outside the record support, minimum at the "
          "density peak, and pointwise ordered: MORE record density <=> LOWER Phi "
          "(ds^2 = -(1 + 2 Phi(x)) (v_bare dt)^2 + dx^2, null cone dx/dt = v_eff(x))",
          np.all(Phi_x <= 1e-15) and abs(Phi_x[0]) < 1e-15
          and int(np.argmin(Phi_x)) == int(xc_p) and order_ok,
          f"Phi_min={Phi_x.min():.4f} at x={int(np.argmin(Phi_x))}")

    times_p = np.arange(0.0, 542.0, 1.0)
    Hp, dimp, _ = dressed_H(Lp, gprof)
    Pp, Ap = evolve_packet(Hp, dimp, Lp, 250, 30, times_p, 1050)
    Ppb, _ = evolve_packet(chain_H(Lp), Lp, Lp, 250, 30, times_p, 1050)
    tp_arr, plat_p = first_half_crossing(times_p, Pp)
    tpb_arr, plat_pb = first_half_crossing(times_p, Ppb)
    delay_eik = float(np.sum(1.0 / v_x - 1.0 / V_BARE))
    check("S4.2 null-geodesic (eikonal) time of the optical metric matches the exact "
          "packet: measured delay through the smooth profile = sum_x (1/v_eff(x) - "
          "1/v_bare) within 6% -- propagation follows ds^2 = 0 of the exhibited metric",
          abs((tp_arr - tpb_arr) - delay_eik) < 0.06 * delay_eik,
          f"measured={tp_arr - tpb_arr:.2f} eikonal={delay_eik:.2f} "
          f"plateau={plat_p:.4f}")

    lam = 1.7
    v_x_scaled = lam * v_x          # H -> lam H rescales every speed exactly
    v_bare_scaled = lam * V_BARE
    Phi_scaled = (v_x_scaled**2 - v_bare_scaled**2) / (2 * v_bare_scaled**2)
    check("S4.3 the clock-rate no-go boundary RESPECTED and demonstrated: rescaling the "
          "supplied clock unit (H -> 1.7 H) rescales every absolute speed by 1.7 but "
          "leaves Phi(x) (the dimensionless cone-slope field = the conformal-class "
          "datum) invariant to machine precision: the toy fixes the conformal class "
          "ONLY; the absolute scale remains the supplied clock unit (the "
          "clock-rate no-go boundary, cited in the note)",
          float(np.max(np.abs(Phi_scaled - Phi_x))) < 1e-14
          and abs(v_x_scaled[int(xc_p)] / v_x[int(xc_p)] - lam) < 1e-12,
          f"max|dPhi|={float(np.max(np.abs(Phi_scaled - Phi_x))):.2e}")

    # ================================================================== verdict
    print("\n" + "=" * 88)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    print("""
VERDICT: the named-not-built step is BUILT, as a toy, and the posit SURVIVES in the
registration class: in an exactly-solved 1D chain where a record site is a site whose
occupation amplitude is registered into a frozen environment qubit, the local front
speed v_eff strictly DECREASES with record density n -- monotonically across
n in {0, 1/8, 1/4, 1/2, 1} -- verified by two independent methods (exact Bloch/
transfer-matrix frequency domain; exact wave-packet and propagator-cone time domain)
that agree to within a few percent, with the per-record Wigner delay positive across
the inner band |E| < sqrt(2) t (sign structure at the band edges verified exactly;
the front-speed statement is carrier-independent). The mechanism: registration
dwell, quantified exactly. A smooth record-density
bump n(x) yields the explicit optical-metric potential Phi(x) = (v_eff^2 - v_bare^2)/
(2 v_bare^2) <= 0 whose eikonal (null-geodesic) time matches the exact packet arrival.
Controls: gauge-invariant; n -> 0 and g -> 0 restore the bare cone; at the pointer
energy full records close the cone (gap/antiresonance); the supplied-clock rescaling
leaves Phi(x) invariant (conformal class only -- the clock-rate no-go boundary is
respected, the scale is NOT derived). Honest class finding: a projective pointer-copy
record attenuates instead of delaying -- the slowing built here is a property of the
amplitude-registration coupling class, reported as such. This is a TOY: the hopping
and registration couplings are supplied model dynamics; nothing here derives the
metric from the axioms, fixes the conformal/clock normalization, or touches Einstein
dynamics. Sets no audit status.""")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
