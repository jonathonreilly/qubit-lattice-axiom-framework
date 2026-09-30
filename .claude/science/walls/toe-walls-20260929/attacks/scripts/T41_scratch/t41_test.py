#!/usr/bin/env python3
"""T41 attack test: readout-blindness vs phase value; balanced vs index-carrying surface; native quark carrier.

Pre-registration is in PREREG.md (written before this script was run).
Reads (never writes) the repository checkout; imports two of its scripts read-only.
"""
import itertools
import json
import math
import os
import sys

sys.dont_write_bytecode = True
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

import warnings
import numpy as np
warnings.filterwarnings("ignore", category=RuntimeWarning)  # spurious FP flags from Accelerate slogdet; results cross-checked below

MAIN = ("/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--"
        "claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/"
        "scratchpad/main_wt")
sys.path.insert(0, os.path.join(MAIN, "scripts"))

rng = np.random.default_rng(20260929)
RES = {}
LOG = []


def log(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOG.append(s)


def wrap(x):
    return (x + math.pi) % (2 * math.pi) - math.pi


def phase_of(z):
    return float(np.angle(z))


# ---------------------------------------------------------------- S1
def build_K(L, seed):
    r = np.random.default_rng(seed)
    N = L ** 3
    idx = lambda x, y, z: ((x % L) * L + (y % L)) * L + (z % L)
    K = np.zeros((N, N))
    eps = np.zeros(N)
    for x in range(L):
        for y in range(L):
            for z in range(L):
                i = idx(x, y, z)
                eps[i] = (-1) ** (x + y + z)
                coords = (x, y, z)
                for mu in range(3):
                    eta = (-1) ** sum(coords[:mu])
                    s = r.choice([-1.0, 1.0])
                    nb = list(coords)
                    nb[mu] += 1
                    j = idx(*nb)
                    K[i, j] += 0.5 * eta * s
                    K[j, i] -= 0.5 * eta * s
    return K, eps


def rand_unitary(n):
    a = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    q, r = np.linalg.qr(a)
    return q * (np.diag(r) / np.abs(np.diag(r)))


def S1():
    log("=== S1: balanced additive surface (K real antisymmetric, eps grading, 4^3 torus) ===")
    L = 4
    K, eps = build_K(L, 7)
    N = L ** 3
    assert np.allclose(K, -K.T)
    assert np.allclose(np.diag(eps) @ K + K @ np.diag(eps), 0)
    assert eps.sum() == 0  # equal sublattices
    I3 = np.eye(3)
    absvals = np.array([0.7, 1.3, 2.1])
    U = rand_unitary(3)
    out = []
    for signs in itertools.product([1, -1], repeat=3):
        A = U @ np.diag(absvals * np.array(signs)) @ U.conj().T
        op = np.kron(K, I3) + np.kron(np.eye(N), A)
        sgn, ld = np.linalg.slogdet(op)
        ev = np.linalg.eigvals(op)
        ph_ev = phase_of(np.prod(ev / np.abs(ev)))
        ld_ev = float(np.sum(np.log(np.abs(ev))))
        assert abs(wrap(ph_ev - phase_of(sgn))) < 1e-8 and abs(ld_ev - ld) < 1e-8, "slogdet vs eigenvalue-product mismatch"
        out.append((signs, phase_of(sgn), ld, float(np.sign(np.linalg.det(A).real))))
    ph = max(abs(wrap(o[1])) for o in out)
    ldspread = max(o[2] for o in out) - min(o[2] for o in out)
    log(f"  Hermitian A, 8 sign patterns: max |arg det(K(x)1+1(x)A)| = {ph:.2e}; log|det| spread = {ldspread:.2e}")
    log(f"  arg det A takes values {sorted(set(round(phase_of(o[3]),3) for o in out))} across these patterns (det A sign +-)")
    # non-Hermitian
    Mnh = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    Mnh *= 0.8
    op = np.kron(K, I3) + np.kron(np.eye(N), Mnh)
    sgn, ld = np.linalg.slogdet(op)
    log(f"  (info) generic non-Hermitian complex A: arg det = {phase_of(sgn):+.4f} rad (expected != 0)")
    # eps phase
    m = 0.8
    vals = []
    for al in [0.0, 0.4, 1.1, 2.3]:
        op = K + m * np.diag(np.exp(1j * al * eps))
        sgn, ld = np.linalg.slogdet(op)
        vals.append((phase_of(sgn), ld))
    spread_ph = max(abs(wrap(v[0] - vals[0][0])) for v in vals)
    spread_ld = max(abs(v[1] - vals[0][1]) for v in vals)
    log(f"  eps-twisted mass det(K + m e^(i alpha eps)): phase spread = {spread_ph:.2e}, log|det| spread = {spread_ld:.2e}")
    RES["S1"] = dict(max_phase_hermitian=ph, logdet_spread_signs=ldspread,
                     eps_alpha_phase_spread=spread_ph, eps_alpha_logdet_spread=spread_ld,
                     nonherm_phase=phase_of(sgn))
    ok = ph < 1e-8 and ldspread < 1e-8 and spread_ph < 1e-8 and spread_ld < 1e-8
    RES["S1"]["pass"] = bool(ok)
    log("  S1", "PASS" if ok else "FAIL")


# ---------------------------------------------------------------- S2
def build_O(B, m):
    npl, nmi = B.shape
    f = m.shape[0]
    top = np.hstack([np.kron(np.eye(npl), m), np.kron(B, np.eye(f))])
    bot = np.hstack([-np.kron(B.conj().T, np.eye(f)), np.kron(np.eye(nmi), m.conj().T)])
    return np.vstack([top, bot])


def rand_cplx(n, m_):
    return rng.normal(size=(n, m_)) + 1j * rng.normal(size=(n, m_))


def predicted_logabs(B, m):
    npl, nmi = B.shape
    nu = npl - nmi
    s = np.linalg.svd(B, compute_uv=False)
    mm = m @ m.conj().T
    tot = abs(nu) * math.log(abs(np.linalg.det(m)))
    for si in s:
        tot += math.log(abs(np.linalg.det(mm + si ** 2 * np.eye(m.shape[0]))))
    return tot


def S2():
    log("=== S2: index-carrying chirality-graded surface, Yukawa form O = [[1(x)m, B(x)1],[-B^dag(x)1, 1(x)m^dag]] ===")
    sizes = [(6, 6), (7, 6), (8, 6), (6, 7), (6, 8), (5, 5), (9, 7), (4, 6)]
    maxerr_ph, maxerr_mag = 0.0, 0.0
    ncase = 0
    bal_max = 0.0
    for (npl, nmi) in sizes:
        nu = npl - nmi
        for rep in range(4):
            B = rand_cplx(npl, nmi)
            m = rand_cplx(3, 3)
            O = build_O(B, m)
            sgn, ld = np.linalg.slogdet(O)
            phi = phase_of(np.linalg.det(m))
            e_ph = abs(wrap(phase_of(sgn) - nu * phi))
            e_mag = abs(ld - predicted_logabs(B, m))
            maxerr_ph = max(maxerr_ph, e_ph)
            maxerr_mag = max(maxerr_mag, e_mag)
            if nu == 0:
                bal_max = max(bal_max, abs(wrap(phase_of(sgn))))
            ncase += 1
    log(f"  {ncase} random cases (nu in -2..2, generic complex 3x3 m): max |arg det O - nu*arg det m| = {maxerr_ph:.2e}; max |log|det O| - prediction| = {maxerr_mag:.2e}")
    log(f"  balanced nu = 0, generic complex m: max |arg det O| = {bal_max:.2e}")
    # Hermitian m with one negative eigenvalue
    U = rand_unitary(3)
    mh = U @ np.diag([-0.9, 1.4, 0.6]) @ U.conj().T
    ph_h = {}
    for (npl, nmi) in [(7, 6), (8, 6), (6, 6), (6, 7), (6, 8)]:
        B = rand_cplx(npl, nmi)
        sgn, ld = np.linalg.slogdet(build_O(B, mh))
        ph_h[npl - nmi] = phase_of(sgn)
    log("  Hermitian m with ONE negative eigenvalue (arg det m = pi): arg det O for nu=", {k: round(v, 6) for k, v in sorted(ph_h.items())})
    mp = U @ np.diag([0.9, 1.4, 0.6]) @ U.conj().T
    ph_p = {}
    for (npl, nmi) in [(7, 6), (8, 6), (6, 6), (6, 7), (6, 8)]:
        B = rand_cplx(npl, nmi)
        sgn, ld = np.linalg.slogdet(build_O(B, mp))
        ph_p[npl - nmi] = phase_of(sgn)
    log("  Hermitian POSITIVE m: arg det O for nu=", {k: round(v, 6) for k, v in sorted(ph_p.items())})
    ok = (maxerr_ph < 1e-8 and maxerr_mag < 1e-8 and bal_max < 1e-8
          and abs(abs(ph_h[1]) - math.pi) < 1e-8 and abs(ph_h[2]) < 1e-8 and abs(ph_h[0]) < 1e-8
          and all(abs(v) < 1e-8 for v in ph_p.values()))
    RES["S2"] = dict(ncase=ncase, max_phase_err=maxerr_ph, max_mag_err=maxerr_mag, balanced_max_phase=bal_max,
                     herm_neg_phase_by_nu={str(k): v for k, v in ph_h.items()},
                     herm_pos_phase_by_nu={str(k): v for k, v in ph_p.items()}, pass_=bool(ok))
    RES["S2"]["pass"] = bool(ok)
    log("  S2", "PASS" if ok else "FAIL")


# ---------------------------------------------------------------- S3
def S3():
    log("=== S3: T41-class readouts vs the weight phase, family m(phi) = diag(e^(i phi),1,1) m0 ===")
    m0h = rand_unitary(3)
    m0 = m0h @ np.diag([0.6, 1.1, 1.7]) @ m0h.conj().T  # Hermitian positive
    nus = [-2, -1, 0, 1, 2]
    Bs = {nu: rand_cplx(6 + max(nu, 0), 6 + max(-nu, 0)) for nu in nus}
    phis = np.linspace(-1.5, 1.5, 11)
    logabs = {nu: [] for nu in nus}
    ph = {nu: [] for nu in nus}
    for nu in nus:
        for phi in phis:
            m = np.diag([np.exp(1j * phi), 1, 1]) @ m0
            sgn, ld = np.linalg.slogdet(build_O(Bs[nu], m))
            logabs[nu].append(ld)
            ph[nu].append(phase_of(sgn))
    spread_abs = max(max(v) - min(v) for v in logabs.values())
    log(f"  class readout |det O| (K-even, block-multiplicative): max spread over phi in [-1.5,1.5], all nu: {spread_abs:.2e}")
    # k=0 character: exp(0) = 1 : trivially constant. k=1 character (what orbit constancy removes):
    f1_spread = max(float(np.max(np.abs(np.exp(1j * np.array(ph[nu]))[:, None] - np.exp(1j * np.array(ph[nu]))[None, :]))) for nu in nus)
    log(f"  (control) k=1 character exp(i arg det O) varies with phi: spread = {f1_spread:.3f}  (orbit constancy is what removes it)")
    # actual phase = nu*phi
    err = max(abs(wrap(ph[nu][i] - nu * phis[i])) for nu in nus for i in range(len(phis)))
    log(f"  weight phase arg det O = nu*phi confirmed: max err {err:.2e}")
    # toy topological sum with exact sector phases
    chi = 1.5
    p = {nu: math.exp(-nu ** 2 / (2 * chi)) for nu in nus}
    phi0 = 0.3
    i0 = int(np.argmin(abs(phis - phi0)))
    phi_used = phis[i0]
    Zs = sum(p[nu] * np.exp(1j * ph[nu][i0]) for nu in nus)
    Z0 = sum(p[nu] for nu in nus)
    nu_mean = sum(nu * p[nu] * np.exp(1j * ph[nu][i0]) for nu in nus) / Zs
    log(f"  toy sum over nu in -2..2 with Gaussian p_nu (NOT framework content), phi = {phi_used:.3f}: "
        f"Z(phi)/Z(0) = {Zs.real/Z0:.4f} (imag {Zs.imag/Z0:.1e}); Im<nu>_phi = {nu_mean.imag:.4f}")
    ok = spread_abs < 1e-9 and abs(Zs.real / Z0 - 1) > 1e-3 and abs(nu_mean.imag) > 1e-3 and err < 1e-8
    RES["S3"] = dict(readout_abs_spread=spread_abs, k1_char_spread=float(f1_spread), phase_err=err,
                     Z_ratio=float(Zs.real / Z0), Im_nu=float(nu_mean.imag), phi_used=float(phi_used))
    RES["S3"]["pass"] = bool(ok)
    log("  S3", "PASS" if ok else "FAIL")


# ---------------------------------------------------------------- S4
def jark_signed(v):
    return float(np.imag(v[0, 1] * v[1, 2] * np.conj(v[0, 2]) * np.conj(v[1, 1])))


def ckm(Mu, Md):
    eu, Uu = np.linalg.eigh(Mu @ Mu.conj().T)
    ed, Ud = np.linalg.eigh(Md @ Md.conj().T)
    V = Uu.conj().T @ Ud
    return np.sqrt(np.abs(eu)), np.sqrt(np.abs(ed)), V


def S4():
    log("=== S4: native quark carrier (Hermitian Schur-NNI + complex 1-3), note's solved point ===")
    import frontier_quark_cp_carrier_completion as qc
    from frontier_quark_mass_ratio_full_solve import (C12_D, C12_U, C23_D, C23_U, R_DB, R_SB, V_CB_ATLAS,
                                                       V_UB_ATLAS, V_US_ATLAS, J_ATLAS)
    r_uc, r_ct = 1.688494e-3, 7.400356e-3
    xi_u, xi_d = complex(0.340735, -0.063203), complex(0.078186, 0.108371)
    m_u, m_c, m_t = r_uc * r_ct, r_ct, 1.0
    m_d, m_s, m_b = R_DB, R_SB, 1.0
    c13u = C12_U * C23_U * math.sqrt(m_u / m_t) + xi_u
    c13d = C12_D * C23_D * math.sqrt(m_d / m_b) + xi_d
    Mu = qc.build_nni_with_complex_13(m_u, m_c, m_t, C12_U, C23_U, c13u)
    Md = qc.build_nni_with_complex_13(m_d, m_s, m_b, C12_D, C23_D, c13d)
    mu_s, md_s, V = ckm(Mu, Md)
    vus, vcb, vub = abs(V[0, 1]), abs(V[1, 2]), abs(V[0, 2])
    J = abs(jark_signed(V))
    log(f"  reproduced: |V_us|={vus:.6f} (atlas {V_US_ATLAS:.6f}), |V_cb|={vcb:.6f} ({V_CB_ATLAS:.6f}), "
        f"|V_ub|={vub:.6f} ({V_UB_ATLAS:.6f}), J={J:.4e} ({J_ATLAS:.4e})")
    NOTE = dict(vus=0.227270122, vcb=0.042179824, vub=0.003917067, J=3.313653e-5)  # docs/QUARK_CP_CARRIER_COMPLETION_NOTE_2026-04-18.md
    rep_ok = (abs(vus / NOTE["vus"] - 1) < 5e-3 and abs(vcb / NOTE["vcb"] - 1) < 5e-3
              and abs(vub / NOTE["vub"] - 1) < 5e-3 and abs(J / NOTE["J"] - 1) < 5e-3)
    log(f"  vs the NOTE's reported numbers (the preregistered comparator): rel. diffs "
        f"{vus/NOTE['vus']-1:+.1e}, {vcb/NOTE['vcb']-1:+.1e}, {vub/NOTE['vub']-1:+.1e}, {J/NOTE['J']-1:+.1e}")
    # minimal Schur-NNI (no xi): eigenvalue signs
    c13u0 = C12_U * C23_U * math.sqrt(m_u / m_t)
    c13d0 = C12_D * C23_D * math.sqrt(m_d / m_b)
    Mu0 = qc.build_nni_with_complex_13(m_u, m_c, m_t, C12_U, C23_U, c13u0)
    Md0 = qc.build_nni_with_complex_13(m_d, m_s, m_b, C12_D, C23_D, c13d0)
    e_u0, e_d0 = np.linalg.eigvalsh(Mu0), np.linalg.eigvalsh(Md0)
    log(f"  minimal Schur-NNI (xi=0): eig(M_u) = {e_u0}; eig(M_d) = {e_d0}")
    log(f"  2x2 (1,2) principal minor det: M_u {Mu[0,0].real*Mu[1,1].real-abs(Mu[0,1])**2:+.3e} (c12_u={C12_U}), M_d {Md[0,0].real*Md[1,1].real-abs(Md[0,1])**2:+.3e} (c12_d={C12_D})")
    RES_extra = dict(min_schur_neg_u=int((e_u0 < 0).sum()), min_schur_neg_d=int((e_d0 < 0).sum()))
    ev_u, W_u = np.linalg.eigh(Mu)
    ev_d, W_d = np.linalg.eigh(Md)
    log(f"  native eigenvalues of M_u: {ev_u}; of M_d: {ev_d}")
    nneg_u, nneg_d = int((ev_u < 0).sum()), int((ev_d < 0).sum())
    dphase = abs(wrap(phase_of(np.linalg.det(Mu) * np.linalg.det(Md))))
    log(f"  negative eigenvalues: M_u {nneg_u}, M_d {nneg_d}; native |arg det(M_u M_d)| = {dphase:.2e}")
    base = dict(mu=mu_s, md=md_s, absV=np.abs(V), J=jark_signed(V))
    maxd = 0.0
    counts = {0: 0, 1: 0}
    for su in itertools.product([1, -1], repeat=3):
        for sd in itertools.product([1, -1], repeat=3):
            Mu2 = W_u @ np.diag(ev_u * np.array(su)) @ W_u.conj().T
            Md2 = W_d @ np.diag(ev_d * np.array(sd)) @ W_d.conj().T
            a, b, V2 = ckm(Mu2, Md2)
            d = max(np.max(np.abs(a - base["mu"])) / np.max(base["mu"]),
                    np.max(np.abs(b - base["md"])) / np.max(base["md"]),
                    np.max(np.abs(np.abs(V2) - base["absV"])),
                    abs(abs(jark_signed(V2)) - abs(base["J"])) / abs(base["J"]))
            maxd = max(maxd, d)
            ph = abs(wrap(phase_of(np.linalg.det(Mu2) * np.linalg.det(Md2))))
            counts[0 if ph < 1e-6 else 1] += 1
    log(f"  64 eigenvalue-sign patterns: max change in (masses, |V|, |J|) = {maxd:.2e}; arg det(M_u M_d) = 0 for {counts[0]}, = pi for {counts[1]}")
    ok = rep_ok and maxd < 1e-8 and counts[0] == 32 and counts[1] == 32
    RES["S4"] = dict(min_schur_neg_u=RES_extra["min_schur_neg_u"], min_schur_neg_d=RES_extra["min_schur_neg_d"], vus=vus, vcb=vcb, vub=vub, J=J, reproduced=bool(rep_ok), nneg_u=nneg_u, nneg_d=nneg_d,
                     native_det_phase=dphase, max_obs_change_under_sign_flips=float(maxd),
                     count_phase0=counts[0], count_phase_pi=counts[1])
    RES["S4"]["pass"] = bool(ok)
    log("  S4", "PASS" if ok else "FAIL")
    return Mu, Md


# ---------------------------------------------------------------- S5
def cycle_phase(M):
    return phase_of(M[0, 1] * M[1, 2] * M[2, 0])


def perm_parity(p):
    inv = sum(1 for i in range(3) for j in range(i + 1, 3) if p[i] > p[j])
    return inv % 2


def k_is_gauge(M, tol=1e-9):
    """True iff conj(M) is gauge-equivalent (permutation + diagonal rephasing) to M."""
    Phi = cycle_phase(M)
    if min(abs(Phi), abs(abs(Phi) - math.pi)) < 1e-9:
        return True, "cycle phase in {0,pi}"
    for p in itertools.permutations(range(3)):
        if perm_parity(p) == 1:
            P = np.eye(3)[list(p)]
            Mp = P @ M @ P.T
            if np.allclose(np.abs(Mp), np.abs(M), atol=tol * max(1, np.abs(M).max())):
                return True, f"odd permutation {p} preserves diag and |off-diag|"
    return False, "no odd permutation preserves (diag, |off-diag|) and cycle phase not in {0,pi}"


def S5(Mu, Md):
    log("=== S5: K-orbit indexing, lepton circulant vs quark carrier ===")
    a, b, delta = 1.0, 0.3, 2.0 / 9.0
    C = np.roll(np.eye(3), 1, axis=0)
    H = a * np.eye(3) + b * np.exp(1j * delta) * C + b * np.exp(-1j * delta) * C.T
    g, why = k_is_gauge(H)
    log(f"  lepton Brannen circulant (delta=2/9): cycle phase {cycle_phase(H):+.4f}; K gauge relabeling? {g} ({why})")
    gu, wu = k_is_gauge(Mu)
    gd, wd = k_is_gauge(Md)
    log(f"  quark M_u: cycle phase {cycle_phase(Mu):+.4f}; K gauge relabeling? {gu} ({wu})")
    log(f"  quark M_d: cycle phase {cycle_phase(Md):+.4f}; K gauge relabeling? {gd} ({wd})")
    _, _, V = ckm(Mu, Md)
    _, _, Vc = ckm(Mu.conj(), Md.conj())
    J1, J2 = jark_signed(V), jark_signed(Vc)
    log(f"  signed J: original {J1:+.4e}; after (M_u,M_d)->(M_u*,M_d*): {J2:+.4e} (ratio {J2/J1:+.4f})")
    ok = g and (not gu) and (not gd) and abs(J2 + J1) < 1e-9 * abs(J1) + 1e-15
    RES["S5"] = dict(lepton_K_gauge=bool(g), quark_u_K_gauge=bool(gu), quark_d_K_gauge=bool(gd),
                     J_orig=J1, J_conj=J2, cycle_phase_lepton=cycle_phase(H),
                     cycle_phase_u=cycle_phase(Mu), cycle_phase_d=cycle_phase(Md))
    RES["S5"]["pass"] = bool(ok)
    log("  S5", "PASS" if ok else "FAIL")


if __name__ == "__main__":
    S1()
    S2()
    S3()
    Mu, Md = S4()
    S5(Mu, Md)
    allp = all(RES[k]["pass"] for k in ["S1", "S2", "S3", "S4"])
    RES["decision"] = "S1-S4 PASS -> MISFRAMED reading supported" if allp else "at least one of S1-S4 FAILED"
    log("=== decision:", RES["decision"], "| S5 pass:", RES["S5"]["pass"])
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "results.json"), "w") as f:
        json.dump(RES, f, indent=2, default=float)
    with open(os.path.join(here, "results.txt"), "w") as f:
        f.write("\n".join(LOG) + "\n")
