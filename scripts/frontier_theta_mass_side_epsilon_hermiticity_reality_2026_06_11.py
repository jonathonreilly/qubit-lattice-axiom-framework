#!/usr/bin/env python3
"""Strong-CP mass side: epsilon-Hermiticity reality on the realization.

Companion runner for
    docs/THETA_MASS_SIDE_EPSILON_HERMITICITY_REALITY_BRIDGE_DISCHARGE_BOUNDED_THEOREM_NOTE_2026-06-11.md

Target (the named open of THETA_P2_K_CPT_DETERMINANT_CHARACTER_PHASE_
ERASURE_BOUNDED_NOTE_2026-06-10): the determinant-readout bridge -- show
that the physical arg det(M) contribution to theta_bar is exhausted by
the registrable determinant class, with no phase-sensitive
non-multiplicative or action-level datum remaining at the matter level.

This runner discharges that bridge AT THE BILINEAR MATTER LEVEL on the
staggered realization, by an exact mechanism:

  A. The matter measure's entire partition-level output is the FIRST
     power of one determinant (explicit Grassmann expansion, no
     determinant identity assumed): at the bilinear level there IS no
     non-multiplicative matter datum -- the only matter phase object is
     arg det.

  B. The exact reality identity: for any matrix M with eps M eps = M+
     (eps the staggered parity, eps^2 = 1),
         det M = det(eps M eps) = det(M+) = conj(det M),
     so det M is REAL.  Verified as a matrix-identity chain and then
     established for the realization: the gauge-dressed staggered
     operator D(U) satisfies eps D(U) eps = -D(U) = D(U)+ for EVERY
     unitary link configuration (any gauge group; verified for U(1),
     SU(2), and SU(3) seeded backgrounds), and the enumerated
     epsilon-graded K-real
     bilinear classes -- real site-diagonal taste/generation channels
     (the hw-mixing eps and eps_mu channels included) plus anti-
     Hermitian h.c.-paired one-link taste channels -- preserve the
     identity.

  C. Therefore det(D(U) + A) is REAL for every gauge background in
     those enumerated epsilon-graded K-real bilinear classes: the
     mass-side strong-CP phase collapses to the sign bit {0, pi}
     IDENTICALLY on that surface -- not as a selected-surface condition
     but as a theorem of the realization, conditional on the K-reality
     of the coupling (the same C_3 K-real structure as the AC_phi_lambda
     reading selection).

  D. Localization of the failure modes (the K-reality boundary, both
     directions): a complex site-diagonal coupling (K-reality violated)
     and a Hermitian one-link coupling (epsilon-grading pairing
     violated) each break the identity and produce a nonzero
     determinant phase (computed) -- in this bilinear channel
     classification, the mass-side phase enters through epsilon-graded
     K-reality violation.

  E. Consequence and sign bookkeeping: theta_bar = theta_gauge +
     arg det(matter); on this surface arg det(matter) is 0 or pi; in
     the tested diagonal-dominant K-real family the sign is + (det >
     0); sign excursions within the family are reported honestly.  The
     residual admitted content of theta(b) is: the K-reality premise
     (shared with AC_phi_lambda) + the discrete orientation bit.

PASS/FAIL per check; RESIDUAL (declared-open) lines mark load-bearing
premises at point of use.  Final line: TOTAL: PASS=<n> FAIL=<m>
Deterministic: all randomness from seeded numpy Generators.
"""

import pathlib
import re
import warnings

import numpy as np
import sympy as sp

L = 4
N = L ** 3
TOL = 1e-9

_pass = 0
_fail = 0


def check(num, desc, ok, detail=""):
    global _pass, _fail
    tag = "PASS" if ok else "FAIL"
    if ok:
        _pass += 1
    else:
        _fail += 1
    line = f"[{tag}] ({num:02d}) {desc}"
    if detail:
        line += f"  [{detail}]"
    print(line)


def residual(msg):
    print(f"RESIDUAL (declared-open): {msg}")


DOCS = pathlib.Path(__file__).resolve().parent.parent / "docs"


def doc_text(name):
    raw = (DOCS / name).read_text(encoding="utf-8")
    raw = re.sub(r"^\s*>\s?", "", raw, flags=re.M)
    return " ".join(raw.split())


def idx(x1, x2, x3):
    return (x1 % L) + L * ((x2 % L) + L * (x3 % L))


def sites():
    for x3 in range(L):
        for x2 in range(L):
            for x1 in range(L):
                yield (x1, x2, x3)


SITES = list(sites())
EMU = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]


def eta_ks(x, mu):
    if mu == 0:
        return 1
    if mu == 1:
        return (-1) ** (x[0] % 2)
    return (-1) ** ((x[0] + x[1]) % 2)


def eps_site(x):
    return (-1) ** (sum(x) % 2)


print("=" * 72)
print("Strong-CP mass side: epsilon-Hermiticity reality on the realization")
print("box: Z^3 torus, L =", L,
      "; gauge groups tested: U(1), SU(2), SU(3)")
print("=" * 72)

# ===================== A. the measure leg (first power) ================
print("\n--- A. the matter partition datum is one determinant (reproven)")


def gr_mul(p, q):
    out = {}
    for m1, c1 in p.items():
        for m2, c2 in q.items():
            if m1 & m2:
                continue
            sign = 1
            gg = m2
            while gg:
                low = gg & (-gg)
                bit = low.bit_length() - 1
                if bin(m1 >> (bit + 1)).count("1") % 2:
                    sign = -sign
                gg ^= low
            m = m1 | m2
            out[m] = out.get(m, 0) + sign * c1 * c2
    return {m: c for m, c in out.items() if c != 0}


def gr_int(p, g):
    out = {}
    bit = 1 << g
    for m, c in p.items():
        if not (m & bit):
            continue
        below = bin(m & (bit - 1)).count("1")
        sign = -1 if below % 2 else 1
        m2 = m ^ bit
        out[m2] = out.get(m2, 0) + sign * c
    return {m: c for m, c in out.items() if c != 0}


def berezin_partition(K, n):
    action = {}
    for i in range(n):
        for j in range(n):
            if K[i][j] == 0:
                continue
            gi, gj = 2 * i, 2 * j + 1
            m = (1 << gi) | (1 << gj)
            sign = 1 if gi < gj else -1
            action[m] = action.get(m, 0) + sign * K[i][j]
    expo = {0: 1}
    term = {0: 1}
    for k in range(1, n + 1):
        term = gr_mul(term, action)
        term = {m: c / k for m, c in term.items() if c != 0}
        for m, c in term.items():
            expo[m] = expo.get(m, 0) + c
    out = expo
    for i in range(n):
        out = gr_int(out, 2 * i)
        out = gr_int(out, 2 * i + 1)
    return out.get(0, 0)


K3 = [[sp.Symbol(f"k{i}{j}") for j in range(3)] for i in range(3)]
Z3 = berezin_partition(K3, 3)
ok = sp.simplify(Z3 - sp.det(sp.Matrix(K3))) == 0
check(1, "explicit Grassmann expansion (no determinant identity "
         "assumed): the one-pair-per-site matter measure yields Z = "
         "det K to the FIRST power -- at the bilinear level the only "
         "matter-level phase object is arg det (no non-multiplicative "
         "matter datum exists)", ok)
residual("the matter-statistics clause (single Grassmann pair per "
         "site) is consumed at the gate-note grade; beyond-bilinear / "
         "interacting matter terms are outside this discharge and are "
         "the named residual of the bridge at that level.")

# ===================== B. the reality identity =========================
print("\n--- B. the exact identity: eps M eps = M+  =>  det M real")

rng = np.random.default_rng(20260611)
Mrand = rng.normal(size=(6, 6)) + 1j * rng.normal(size=(6, 6))
ok = (abs(np.linalg.det(Mrand.conj().T)
          - np.conj(np.linalg.det(Mrand))) < 1e-9
      and abs(np.linalg.det(np.diag([1, -1, 1, -1, 1, -1]) @ Mrand
                            @ np.diag([1, -1, 1, -1, 1, -1]))
              - np.linalg.det(Mrand)) < 1e-9)
check(2, "matrix-identity chain verified on a generic complex matrix: "
         "det(M+) = conj(det M) and det(eps M eps) = det M; hence "
         "eps M eps = M+ forces det M real", ok)

EPSD = np.diag([float(eps_site(x)) for x in SITES])


def build_D_gauge(links, cdim):
    """Gauge-dressed staggered operator; links[(x,mu)] is cdim x cdim
    unitary.  Color-blocked: site-major kron structure."""
    Dg = np.zeros((N * cdim, N * cdim), dtype=complex)
    for x in SITES:
        for mu, e in enumerate(EMU):
            xp = tuple((x[k] + e[k]) % L for k in range(3))
            U = links[(x, mu)]
            i, j = idx(*x), idx(*xp)
            Dg[i * cdim:(i + 1) * cdim, j * cdim:(j + 1) * cdim] += (
                0.5 * eta_ks(x, mu) * U)
            Dg[j * cdim:(j + 1) * cdim, i * cdim:(i + 1) * cdim] -= (
                0.5 * eta_ks(x, mu) * U.conj().T)
    return Dg


def random_su3(rng_):
    """Haar-style SU(3) sample by QR projection of a complex Gaussian."""
    z = rng_.normal(size=(3, 3)) + 1j * rng_.normal(size=(3, 3))
    q, r = np.linalg.qr(z)
    phases = np.diag(r)
    phases = np.where(np.abs(phases) > 0, phases / np.abs(phases), 1.0)
    q = q @ np.diag(np.conj(phases))
    q[:, 0] /= np.linalg.det(q)
    return q


def validate_link(U, cdim):
    if not np.allclose(U.conj().T @ U, np.eye(cdim), atol=1e-10):
        raise ValueError("generated link is not unitary")
    if cdim in (2, 3) and abs(np.linalg.det(U) - 1.0) > 1e-10:
        raise ValueError(f"generated SU({cdim}) link has det != 1")


def random_links(rng_, cdim):
    links = {}
    for x in SITES:
        for mu in range(3):
            if cdim == 1:
                U = np.array([[np.exp(2j * np.pi * rng_.random())]])
            elif cdim == 2:
                q = rng_.normal(size=4)
                q = q / np.linalg.norm(q)
                U = np.array(
                    [[q[0] + 1j * q[3], q[2] + 1j * q[1]],
                     [-q[2] + 1j * q[1], q[0] - 1j * q[3]]])
            elif cdim == 3:
                U = random_su3(rng_)
            else:
                raise ValueError(f"unsupported color dimension: {cdim}")
            validate_link(U, cdim)
            links[(x, mu)] = U
    return links


def det_phase_sign(M):
    """Return det(M)/|det(M)| via slogdet, avoiding large-matrix overflow."""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        sign, _ = np.linalg.slogdet(M)
    return sign


backgrounds = []
for seed in (1, 2, 3):
    r1 = np.random.default_rng(1000 + seed)
    backgrounds.append(("U(1)", 1, build_D_gauge(random_links(r1, 1), 1)))
for seed in (1, 2):
    r2 = np.random.default_rng(2000 + seed)
    backgrounds.append(("SU(2)", 2, build_D_gauge(random_links(r2, 2), 2)))
for seed in (1, 2):
    r3 = np.random.default_rng(3000 + seed)
    backgrounds.append(("SU(3)", 3, build_D_gauge(random_links(r3, 3), 3)))

ok = True
for (gname, cdim, Dg) in backgrounds:
    E = np.kron(EPSD, np.eye(cdim))
    if not (np.allclose(Dg.conj().T, -Dg, atol=1e-10)
            and np.allclose(E @ Dg @ E, -Dg, atol=1e-10)):
        ok = False
check(3, "for EVERY tested unitary background (3x U(1), 2x SU(2), "
         "2x SU(3)): the "
         "gauge-dressed staggered operator is anti-Hermitian and "
         "eps-odd, so eps D(U) eps = -D(U) = D(U)+ -- the identity "
         "premise holds for the kinetic operator on any gauge "
         "background", ok)

# ===================== C. the K-real coupling classes ==================
print("\n--- C. eps-graded K-real channels preserve reality, any background")

EPSMU_D = [np.diag([float((-1) ** (x[mu] % 2)) for x in SITES])
           for mu in range(3)]


def site_diag_channels(m0, m1, c):
    A = m0 * np.eye(N) + m1 * EPSD
    for mu in range(3):
        A = A + c[mu] * EPSMU_D[mu]
    return A


def one_link_taste(links, cdim, w):
    """Anti-Hermitian h.c.-paired one-link taste channel (kinetic
    class): w * sum_x eps_mu-weighted (U hop - U+ hop back)."""
    A = np.zeros((N * cdim, N * cdim), dtype=complex)
    for x in SITES:
        mu = 0
        e = EMU[mu]
        xp = tuple((x[k] + e[k]) % L for k in range(3))
        U = links[(x, mu)]
        i, j = idx(*x), idx(*xp)
        wloc = w * ((-1) ** (x[1] % 2))          # taste-vector dressing
        A[i * cdim:(i + 1) * cdim, j * cdim:(j + 1) * cdim] += wloc * U
        A[j * cdim:(j + 1) * cdim, i * cdim:(i + 1) * cdim] -= (
            wloc * U.conj().T)
    return A


params = [(0.9, 0.20, (0.10, -0.07, 0.05)),
          (0.7, -0.15, (0.04, 0.11, -0.08)),
          (1.1, 0.35, (-0.12, 0.06, 0.09))]
real_ok = True
signs = set()
max_imag = 0.0
for (gname, cdim, Dg) in backgrounds:
    E = np.kron(EPSD, np.eye(cdim))
    for (m0, m1, c) in params:
        A = np.kron(site_diag_channels(m0, m1, c), np.eye(cdim))
        Mfull = Dg + A
        if not np.allclose(E @ Mfull @ E, Mfull.conj().T, atol=1e-10):
            real_ok = False
        phase_sign = det_phase_sign(Mfull)
        rel_imag = abs(phase_sign.imag)
        max_imag = max(max_imag, rel_imag)
        if rel_imag > 1e-8:
            real_ok = False
        signs.add(int(np.sign(phase_sign.real)))
check(4, "REAL site-diagonal taste/generation channels (m0*I + m1*eps "
         "+ c_mu*eps_mu -- the hw-mixing channel classes): "
         "eps(D(U)+A)eps = (D(U)+A)+ holds exactly and det(D(U)+A) is "
         "REAL for every tested background x parameter point (21 "
         "combinations)", real_ok,
      f"max |Im det|/|det| = {max_imag:.1e}; signs seen: {sorted(signs)}")

ol_ok = True
one_link_backgrounds = [backgrounds[0], backgrounds[3], backgrounds[5]]
for (gname, cdim, Dg) in one_link_backgrounds:
    E = np.kron(EPSD, np.eye(cdim))
    r3 = np.random.default_rng(3000)
    links = random_links(r3, cdim)
    A1 = one_link_taste(links, cdim, 0.17)
    A0 = np.kron(site_diag_channels(0.8, 0.1, (0.05, 0.0, 0.0)),
                 np.eye(cdim))
    Mfull = Dg + A0 + A1
    if not (np.allclose(A1.conj().T, -A1, atol=1e-10)
            and np.allclose(E @ A1 @ E, -A1, atol=1e-10)
            and np.allclose(E @ Mfull @ E, Mfull.conj().T, atol=1e-10)):
        ol_ok = False
    phase_sign = det_phase_sign(Mfull)
    if abs(phase_sign.imag) > 1e-8:
        ol_ok = False
check(5, "anti-Hermitian h.c.-paired one-link taste channels (the "
         "tested gauge-covariant kinetic-class dressing) are eps-odd "
         "anti-Hermitian, preserve the identity, and keep det REAL on "
         "representative U(1), SU(2), and SU(3) backgrounds", ol_ok)

# epsilon-graded K-reality, stated as the exact classification
m0s, m1s = sp.symbols("m0 m1", real=True)
zc = sp.Symbol("zc")                       # complex diagonal coefficient
ok = True
# even part (site-diagonal): eps A eps = +A, so identity needs A+ = A,
# i.e. real coefficients; odd part (one-link): eps A eps = -A, so the
# identity needs A+ = -A (anti-Hermitian).  Verify both directions on
# 2x2 toy blocks exactly.
Aeven = sp.diag(m0s + m1s, m0s - m1s)
ok = ok and (Aeven.conjugate().T - Aeven == sp.zeros(2))
Aeven_bad = sp.diag(zc, zc)
ok = ok and not (sp.simplify(Aeven_bad.conjugate().T - Aeven_bad)
                 == sp.zeros(2))
w_s = sp.Symbol("w", real=True)
Aodd = sp.Matrix([[0, w_s], [-w_s, 0]])
ok = ok and (Aodd.conjugate().T + Aodd == sp.zeros(2))
check(6, "the exact classification (epsilon-graded K-reality): "
         "eps-EVEN channels must be Hermitian-real (real coefficients) "
         "and eps-ODD channels must be anti-Hermitian for the identity "
         "eps(D+A)eps = (D+A)+ to hold -- the realization form of the "
         "K-reality premise, verified in both directions on exact "
         "blocks", ok)
residual("the K-reality of the physical generation coupling is "
         "CONSUMED, not derived: it is the same C_3 K-real structure "
         "as the AC_phi_lambda reading selection (custody selector i; "
         "the cross-admission identification of the structured "
         "admission note). This discharge is conditional on it.")

# ===================== D. failure modes localized ======================
print("\n--- D. the K-reality boundary: both violation classes phase")

phase_c = 0.0
for (gname, cdim, Dg) in backgrounds[:2]:
    A = np.kron(site_diag_channels(0.9, 0.2, (0.1, -0.07, 0.05))
                + (0.11 + 0.23j) * EPSD, np.eye(cdim))
    phase_sign = det_phase_sign(Dg + A)
    phase_c = max(phase_c, abs(np.angle(phase_sign)) % np.pi)
ok = phase_c > 1e-3
check(7, "violation class 1 (K-reality broken): a COMPLEX site-"
         "diagonal coefficient produces a nonzero determinant phase "
         "(computed)", ok, f"max |phase| mod pi = {phase_c:.3f}")

phase_h = 0.0
for (gname, cdim, Dg) in backgrounds[:2]:
    E = np.kron(EPSD, np.eye(cdim))
    r4 = np.random.default_rng(4000)
    links = random_links(r4, cdim)
    A1 = one_link_taste(links, cdim, 0.17)
    Aherm = 1j * A1                         # Hermitian one-link (eps-odd)
    A0 = np.kron(site_diag_channels(0.8, 0.1, (0.05, 0.0, 0.0)),
                 np.eye(cdim))
    Mfull = Dg + A0 + Aherm
    broke = not np.allclose(E @ Mfull @ E, Mfull.conj().T, atol=1e-10)
    phase_sign = det_phase_sign(Mfull)
    if broke:
        phase_h = max(phase_h, abs(np.angle(phase_sign)) % np.pi)
ok = phase_h > 1e-3
check(8, "violation class 2 (epsilon-grading pairing broken): a "
         "HERMITIAN one-link coupling breaks the identity and produces "
         "a nonzero determinant phase (computed) -- in this bilinear "
         "channel classification, the mass-side phase enters through "
         "epsilon-graded K-reality violation", ok,
      f"max |phase| mod pi = {phase_h:.3f}")

# ===================== E. consequence + interfaces =====================
print("\n--- E. consequence: theta(b) collapses to K-reality + one bit")

ok = (signs == {1})
check(9, "sign bookkeeping in the tested diagonal-dominant K-real "
         "family: det(D(U)+A) > 0 throughout (arg det = 0, not pi); "
         "the orientation bit did not excurse in the tested family "
         "(family-bounded statement, not a theorem of all couplings)",
      ok, f"signs seen: {sorted(signs)}")

bridge = doc_text("THETA_P2_K_CPT_DETERMINANT_CHARACTER_PHASE_ERASURE"
                  "_BOUNDED_NOTE_2026-06-10.md")
struct = doc_text("STRONG_CP_THETA_BAR_STRUCTURED_ADMISSION_2026-06-04.md")
ok = ("a later retained bridge must show that the physical "
      "`arg det(M_u M_d)` contribution" in bridge
      and "exhausted by this determinant-class registrable readout"
      in bridge
      and "gauge-side and mass-side" in struct.lower()
      or ("gauge-side" in struct and "mass-side" in struct))
check(10, "interface pins: the 06-10 note's named-open bridge sentence "
          "and the structured admission's gauge/mass split are present "
          "in the live notes; this block supplies the bilinear-matter-"
          "level half of the named bridge (the measure output IS the "
          "determinant, and it is real on the K-real section for every "
          "gauge background)", ok)
residual("NOT discharged and explicitly out of scope: the gauge-side "
         "residual theta_gauge (winding/multi-plaquette account) is "
         "untouched; beyond-bilinear matter terms; the rotation-"
         "channel coupling's gauge-covariant dressing (not "
         "constructed); and the discrete orientation bit itself. The "
         "theta(b) admitted content after this block is: the K-reality "
         "premise (shared with AC_phi_lambda) + the orientation bit, "
         "at the bilinear matter level.")
residual("gauge-group generality: the identity chain det M = "
         "det(eps M eps) = det(M+) = conj(det M) is exact for any "
         "matrix satisfying the premise, and the premise was verified "
         "on U(1), SU(2), and SU(3) seeded backgrounds; the exact "
         "argument is still the epsilon-Hermiticity premise, not a "
         "gauge-group-specific numerical fit.")

print()
print(f"TOTAL: PASS={_pass} FAIL={_fail}")
print("VERDICT: at the bilinear matter level the determinant-readout "
      "bridge discharges on the staggered realization: the matter "
      "measure's only phase object is arg det (first-power Berezin, "
      "reproven), and eps-Hermiticity makes det(D(U)+A) REAL for every "
      "tested gauge background in the enumerated epsilon-graded K-real "
      "bilinear classes (site-diagonal hw-mixing classes and anti-"
      "Hermitian one-link taste classes), with both violation classes "
      "computed to phase. "
      "The mass-side strong-CP admission reduces, at this level, to "
      "the K-reality premise (shared with AC_phi_lambda) plus the "
      "discrete orientation bit. Nothing is retired; no audit status "
      "is set.")
raise SystemExit(0 if _fail == 0 else 1)
