#!/usr/bin/env python3
"""Native finite-carrier registration kernel versus the unit-variance point.

Audit authority is set only by the independent audit lane. This source runner
does not set, predict, or apply an audit verdict.

K1: the selected-axis taste cube has an su(2) fiber, a residual base swap, a
joint commutant of dimension 10, and derived su(3) content 3+3+1+1.
K2: the native link carrier B(V) has four central isotypic sectors with
dimensions 36, 12, 12, and 4.
K3: full central resolution induces T_V(x) = (|chi_3(x)|^2 + 1)/2 =
1 + chi_8(x)/2, with w_8 = 1/16 and no other nontrivial spectral blocks.
K4: the identity readout floor has w_3 = w_3bar = 1/6 and w_8 = 1/16; native
registration removes exactly the 3 and 3bar coherence blocks.
K5: under the zero-sum minimal logarithm branch, the parameter-free native
second moment is not the unit value.
"""

from fractions import Fraction
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "NATIVE_CARRIER_REGISTRATION_KERNEL_RATE_VS_UNIT_VARIANCE_POINT_THEOREM_NOTE_2026-07-02.md"
DEPS = {
    "graph-first": ROOT / "docs" / "GRAPH_FIRST_SU3_INTEGRATION_NOTE.md",
    "rigidity": ROOT / "docs" / "G_BARE_RIGIDITY_THEOREM_NOTE.md",
    "controlled-copy": ROOT / "docs" / "RECORD_FORMATION_CONTROLLED_COPY_WRITE_ISOMETRY_THEOREM_NOTE_2026-06-18.md",
    "semigroup": ROOT / "docs" / "RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06.md",
}

SEED = 20260702
TWOPI = 2.0 * np.pi
PASS = 0
FAIL = 0


def check(label, ok, detail=""):
    global PASS, FAIL
    ok = bool(ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    if detail:
        print(f"       {detail}")
    PASS += int(ok)
    FAIL += int(not ok)


def flatten(text):
    return " ".join(text.split())


def comm(a, b):
    return a @ b - b @ a


def gell_mann():
    return [
        np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex),
        np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex),
        np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=complex),
        np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex),
        np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=complex),
        np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex),
        np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex),
        np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], dtype=complex) / np.sqrt(3.0),
    ]


def selected_axis_operators():
    x2 = np.zeros((8, 8), dtype=complex)
    tau = np.zeros((8, 8), dtype=complex)
    zdiag = np.zeros(8, dtype=complex)
    for v in range(8):
        b0 = v & 1
        b1 = (v >> 1) & 1
        b2 = (v >> 2) & 1
        x2[v ^ 4, v] = 1.0
        zdiag[v] = (-1.0) ** b2
        swapped = b1 + 2 * b0 + 4 * b2
        tau[swapped, v] = 1.0
    z2 = np.diag(zdiag)
    y2 = -1j * z2 @ x2
    return x2, y2, z2, tau


def base_swap():
    tau = np.zeros((4, 4), dtype=complex)
    for v in range(4):
        b0 = v & 1
        b1 = (v >> 1) & 1
        tau[b1 + 2 * b0, v] = 1.0
    return tau


def commutant_dimension(generators):
    n = generators[0].shape[0]
    ident = np.eye(n, dtype=complex)
    rows = []
    for mat in generators:
        rows.append(np.kron(ident, mat) - np.kron(mat.T, ident))
    constraints = np.vstack(rows)
    rank = np.linalg.matrix_rank(constraints, tol=1e-10)
    return n * n - int(rank)


def native_su3_generators():
    lam = gell_mann()
    t3 = [mat / 2.0 for mat in lam]
    e00 = np.array([1, 0, 0, 0], dtype=complex)
    e10 = np.array([0, 1, 0, 0], dtype=complex)
    e01 = np.array([0, 0, 1, 0], dtype=complex)
    e11 = np.array([0, 0, 0, 1], dtype=complex)
    usym = np.column_stack([e00, e11, (e01 + e10) / np.sqrt(2.0)])
    uanti = ((e01 - e10) / np.sqrt(2.0)).reshape(4, 1)
    tv = []
    for gen in t3:
        base = usym @ gen @ usym.conj().T
        tv.append(np.kron(np.eye(2, dtype=complex), base))
    return t3, tv, usym, uanti


def structure_constants(t3):
    f = np.zeros((8, 8, 8), dtype=float)
    for a in range(8):
        for b in range(8):
            cab = comm(t3[a], t3[b])
            for c in range(8):
                f[a, b, c] = float((-2j * np.trace(cab @ t3[c])).real)
    return f


def matrix_exp_i_hermitian(h):
    vals, vecs = np.linalg.eigh(h)
    return (vecs * np.exp(1j * vals)) @ vecs.conj().T


def lift_to_native_v(u3, usym, uanti):
    panti = uanti @ uanti.conj().T
    base = usym @ u3 @ usym.conj().T + panti
    return np.kron(np.eye(2, dtype=complex), base)


def projector_checks(label, p, tol=1e-10):
    check(f"{label} is Hermitian", np.linalg.norm(p - p.conj().T) < tol, f"norm={np.linalg.norm(p - p.conj().T):.3e}")
    check(f"{label} is idempotent", np.linalg.norm(p @ p - p) < tol, f"norm={np.linalg.norm(p @ p - p):.3e}")


def weyl_grid(m, complex_coefficients=False):
    t = -np.pi + TWOPI * (np.arange(m, dtype=float) + 0.5) / m
    t1, t2 = np.meshgrid(t, t, indexing="ij")
    d12 = t1 - t2
    d13 = 2.0 * t1 + t2
    d23 = t1 + 2.0 * t2
    haar = (64.0 / 6.0) * np.sin(d12 / 2.0) ** 2 * np.sin(d13 / 2.0) ** 2 * np.sin(d23 / 2.0) ** 2
    abs_chi3_sq = 3.0 + 2.0 * np.cos(d12) + 2.0 * np.cos(d13) + 2.0 * np.cos(d23)
    re_chi3 = np.cos(t1) + np.cos(t2) + np.cos(t1 + t2)
    tv = (abs_chi3_sq + 1.0) / 2.0
    tid = (abs_chi3_sq + 1.0 + 2.0 * re_chi3) / 2.0

    th30 = -(t1 + t2)
    s2min = np.full_like(t1, np.inf)
    for a in (-1, 0, 1):
        for b in (-1, 0, 1):
            candidate = (t1 + TWOPI * a) ** 2 + (t2 + TWOPI * b) ** 2 + (th30 - TWOPI * (a + b)) ** 2
            s2min = np.minimum(s2min, candidate)
    principal_th3 = ((th30 + np.pi) % TWOPI) - np.pi
    s2naive = t1 * t1 + t2 * t2 + principal_th3 * principal_th3

    out = {
        "haar_mean": float(np.mean(haar)),
        "tv_mean": float(np.mean(haar * tv)),
        "tid_mean": float(np.mean(haar * tid)),
        "tv_min": float(np.min(tv)),
        "m2_total": float(np.mean(haar * tv * s2min) / 4.0),
        "m2_floor": float(np.mean(haar * tid * s2min) / 4.0),
        "m2_naive": float(np.mean(haar * tv * s2naive) / 4.0),
        "pi_identity": float(np.mean(haar * abs_chi3_sq * s2naive)),
    }
    out["increment"] = out["m2_total"] - out["m2_floor"]

    if complex_coefficients:
        chi3 = np.exp(1j * t1) + np.exp(1j * t2) + np.exp(-1j * (t1 + t2))
        chi8 = abs_chi3_sq - 1.0
        out["identity_form_error"] = float(np.max(np.abs(tv - (1.0 + chi8 / 2.0))))
        out["w8_tv"] = np.mean(haar * tv * np.conj(chi8)) / 8.0
        out["w3_tv"] = np.mean(haar * tv * np.conj(chi3)) / 3.0
        out["w3_tid"] = np.mean(haar * tid * np.conj(chi3)) / 3.0
        out["w8_tid"] = np.mean(haar * tid * np.conj(chi8)) / 8.0
        # Triplet-only carrier: registration kernel via the sector-sum formula
        # (single sector, m = 2), identity-readout kernel via its own
        # independently computed grid normalizer <|chi_3|^2>. The equality gate
        # discriminates: it fails if the normalizer deviates from 1.
        t3_reg = (4.0 * abs_chi3_sq) / 4.0
        chi3_norm = float(np.mean(haar * abs_chi3_sq)) / float(np.mean(haar))
        t3_id = (4.0 * abs_chi3_sq) / (4.0 * chi3_norm)
        out["t3_reg_id_error"] = float(np.max(np.abs(t3_reg - t3_id)))
    return out


def s2min_from_principal_phases(phases):
    best = np.full(phases.shape[0], np.inf, dtype=float)
    for a in (-1, 0, 1):
        for b in (-1, 0, 1):
            for c in (-1, 0, 1):
                shifted = phases + TWOPI * np.array([a, b, c], dtype=float)
                zero_sum = np.abs(np.sum(shifted, axis=1)) < 1e-6
                s2 = np.sum(shifted * shifted, axis=1)
                best = np.where(zero_sum & (s2 < best), s2, best)
    if np.any(~np.isfinite(best)):
        for a in (-2, -1, 0, 1, 2):
            for b in (-2, -1, 0, 1, 2):
                for c in (-2, -1, 0, 1, 2):
                    shifted = phases + TWOPI * np.array([a, b, c], dtype=float)
                    zero_sum = np.abs(np.sum(shifted, axis=1)) < 1e-6
                    s2 = np.sum(shifted * shifted, axis=1)
                    best = np.where(zero_sum & (s2 < best), s2, best)
    return best


def monte_carlo_total_m2(target):
    rng = np.random.default_rng(SEED)
    total = 0.0
    samples = 500000
    batch = 100000
    done = 0
    while done < samples:
        n = min(batch, samples - done)
        z = rng.normal(size=(n, 3, 3)) + 1j * rng.normal(size=(n, 3, 3))
        q, r = np.linalg.qr(z)
        diag = np.diagonal(r, axis1=1, axis2=2)
        phase = diag / np.abs(diag)
        q = q / phase[:, None, :]
        det = np.linalg.det(q)
        cube = np.exp(np.log(det) / 3.0)
        q = q / cube[:, None, None]
        eig = np.linalg.eigvals(q)
        phases = np.angle(eig)
        s2 = s2min_from_principal_phases(phases)
        chi3 = np.trace(q, axis1=1, axis2=2)
        tv = (np.abs(chi3) ** 2 + 1.0) / 2.0
        total += float(np.sum(tv * s2))
        done += n
    estimate = total / samples / 4.0
    check(
        "D7 Monte Carlo cross-check agrees with Weyl-grid total",
        abs(estimate - target) < 2e-2,
        f"MC/4={estimate:.9f}, grid={target:.9f}, diff={estimate - target:.3e}",
    )
    return estimate


def require_contains(label, haystack, needle):
    check(label, needle in haystack, f"needle={needle!r}" if needle not in haystack else "")


def section_a():
    print("SECTION A -- native taste-cube structure")
    x2, y2, z2, tau = selected_axis_operators()
    ident8 = np.eye(8, dtype=complex)
    check(
        "A1 selected-axis involutions square to identity",
        max(np.linalg.norm(x2 @ x2 - ident8), np.linalg.norm(y2 @ y2 - ident8), np.linalg.norm(z2 @ z2 - ident8)) < 1e-12,
    )
    check(
        "A1 selected-axis su(2) commutators close cyclically",
        max(
            np.linalg.norm(comm(x2, y2) - 2j * z2),
            np.linalg.norm(comm(y2, z2) - 2j * x2),
            np.linalg.norm(comm(z2, x2) - 2j * y2),
        )
        < 1e-12,
    )
    check(
        "A2 residual base swap commutes with selected-axis X2 and Z2",
        max(np.linalg.norm(comm(tau, x2)), np.linalg.norm(comm(tau, z2))) < 1e-12,
    )
    joint_dim = commutant_dimension([x2, z2, tau])
    weak_dim = commutant_dimension([x2, z2])
    check("A3 joint commutant of X2, Z2, tau has dimension 10", joint_dim == 10, f"dim={joint_dim}")
    check("A3 rejector: commutant of X2, Z2 alone has dimension 16", weak_dim == 16, f"dim={weak_dim}")

    evals = np.linalg.eigvalsh(base_swap())
    plus = int(np.sum(evals > 0.5))
    minus = int(np.sum(evals < -0.5))
    check("A4 base swap splits C^4 into dimensions 3 and 1", plus == 3 and minus == 1, f"plus={plus}, minus={minus}")

    t3, tv, usym, uanti = native_su3_generators()
    f = structure_constants(t3)
    max_close = 0.0
    for a in range(8):
        for b in range(8):
            target = np.zeros((8, 8), dtype=complex)
            for c in range(8):
                target = target + 1j * f[a, b, c] * tv[c]
            max_close = max(max_close, np.linalg.norm(comm(tv[a], tv[b]) - target))
    check("A5 embedded generators close with the 3x3-computed su(3) constants", max_close < 1e-12, f"max={max_close:.3e}")
    spot = max(
        np.linalg.norm(comm(tv[0], tv[1]) - 1j * sum(f[0, 1, c] * tv[c] for c in range(8))),
        np.linalg.norm(comm(tv[3], tv[4]) - 1j * sum(f[3, 4, c] * tv[c] for c in range(8))),
        np.linalg.norm(comm(tv[5], tv[6]) - 1j * sum(f[5, 6, c] * tv[c] for c in range(8))),
    )
    check("A5 spot commutators use the same computed structure constants", spot < 1e-12, f"max={spot:.3e}")
    casimir = sum(gen @ gen for gen in tv)
    cevals = np.linalg.eigvalsh(casimir)
    count_fund = int(np.sum(np.abs(cevals - 4.0 / 3.0) < 1e-10))
    count_singlet = int(np.sum(np.abs(cevals) < 1e-10))
    check("A5 Casimir spectrum is 4/3 x6 and 0 x2", count_fund == 6 and count_singlet == 2, f"4/3={count_fund}, 0={count_singlet}")
    max_native_comm = max(np.linalg.norm(comm(gen, op)) for gen in tv for op in (x2, z2, tau))
    check("A6 derived su(3) generators commute with X2, Z2, and tau", max_native_comm < 1e-12, f"max={max_native_comm:.3e}")
    return t3, tv, usym, uanti, casimir


def section_b(t3, tv, usym, uanti, casimir):
    print("SECTION B -- link carrier sectors")
    ident8 = np.eye(8, dtype=complex)
    p3 = (3.0 / 4.0) * casimir
    p1 = ident8 - p3
    vals, vecs = np.linalg.eigh(casimir)
    mask = vals > 0.5
    p3_eigh = vecs[:, mask] @ vecs[:, mask].conj().T
    check("B0 rational Casimir projector equals spectral projector", np.linalg.norm(p3 - p3_eigh) < 1e-10, f"norm={np.linalg.norm(p3 - p3_eigh):.3e}")
    projector_checks("B0 P3", p3)
    projector_checks("B0 P1", p1)

    sectors = []
    labels = []
    for name_i, pi in (("3", p3), ("1", p1)):
        for name_j, pj in (("3", p3), ("1", p1)):
            sectors.append(np.kron(pi, pj.T))
            labels.append(name_i + name_j)
    ident64 = np.eye(64, dtype=complex)
    max_projector_error = max(np.linalg.norm(p @ p - p) + np.linalg.norm(p - p.conj().T) for p in sectors)
    max_orth = 0.0
    for i in range(4):
        for j in range(4):
            if i != j:
                max_orth = max(max_orth, np.linalg.norm(sectors[i] @ sectors[j]))
    traces = [int(round(np.trace(p).real)) for p in sectors]
    check("B1 sector projectors are orthogonal projectors", max_projector_error < 1e-10 and max_orth < 1e-10, f"proj={max_projector_error:.3e}, orth={max_orth:.3e}")
    check("B1 sector projectors sum to I_64", np.linalg.norm(sum(sectors) - ident64) < 1e-10, f"norm={np.linalg.norm(sum(sectors) - ident64):.3e}")
    check("B1 sector traces are 36, 12, 12, 4", traces == [36, 12, 12, 4], f"{labels}={traces}")

    max_lr_comm = 0.0
    for gen in tv:
        left = np.kron(gen, ident8)
        right = np.kron(ident8, gen.T)
        for p in sectors:
            max_lr_comm = max(max_lr_comm, np.linalg.norm(comm(p, left)), np.linalg.norm(comm(p, right)))
    check("B2 sectors commute with left and right su(3) action generators", max_lr_comm < 1e-10, f"max={max_lr_comm:.3e}")

    rng = np.random.default_rng(SEED)
    max_overlap_error = 0.0
    for _ in range(6):
        coeff_u = rng.uniform(-1.0, 1.0, size=8)
        coeff_w = rng.uniform(-1.0, 1.0, size=8)
        hu = sum(coeff_u[a] * t3[a] for a in range(8))
        hw = sum(coeff_w[a] * t3[a] for a in range(8))
        u3 = matrix_exp_i_hermitian(hu)
        w3 = matrix_exp_i_hermitian(hw)
        ru = lift_to_native_v(u3, usym, uanti)
        rw = lift_to_native_v(w3, usym, uanti)
        vu = ru.reshape(-1)
        vw = rw.reshape(-1)
        rel_eigs = np.linalg.eigvals(u3.conj().T @ w3)
        chi = {"3": np.sum(rel_eigs), "1": 1.0 + 0j}
        mult = {"3": 2.0, "1": 2.0}
        for idx, p in enumerate(sectors):
            left_label = labels[idx][0]
            right_label = labels[idx][1]
            observed = np.vdot(vu, p @ vw)
            expected = (mult[left_label] * chi[left_label]) if left_label == right_label else 0.0
            max_overlap_error = max(max_overlap_error, abs(observed - expected))
    check("B3 constructed overlaps match the closed character formula", max_overlap_error < 1e-8, f"max={max_overlap_error:.3e}")


def section_c():
    print("SECTION C -- exact Weyl-grid kernel identities")
    c = weyl_grid(800, complex_coefficients=True)
    one_sixteenth = Fraction(1, 16)
    one_sixth = Fraction(1, 6)
    check("C0 Haar density averages to 1 on the centered M=800 grid", abs(c["haar_mean"] - 1.0) < 1e-9, f"mean={c['haar_mean']:.12f}")
    check("C1 T_V forms agree: (|chi_3|^2+1)/2 equals 1 + chi_8/2", c["identity_form_error"] < 1e-12, f"max={c['identity_form_error']:.3e}")
    check("C2 native registration density normalizes to 1", abs(c["tv_mean"] - 1.0) < 1e-9, f"mean={c['tv_mean']:.12f}")
    check("C2 identity-readout density normalizes to 1", abs(c["tid_mean"] - 1.0) < 1e-9, f"mean={c['tid_mean']:.12f}")
    check("C3 native registration density is bounded below by 1/2", c["tv_min"] >= 0.5 - 1e-9, f"min={c['tv_min']:.12f}")
    check("C4 w_8(T_V) equals 1/16", abs(c["w8_tv"].real - float(one_sixteenth)) < 1e-9, f"w8={c['w8_tv'].real:.12f}")
    check("C4 w_3(T_V) vanishes", abs(c["w3_tv"]) < 1e-9, f"w3={c['w3_tv']:.3e}")
    check("C4 w_3(T_id) equals 1/6", abs(c["w3_tid"].real - float(one_sixth)) < 1e-9, f"w3={c['w3_tid'].real:.12f}")
    check("C4 w_8(T_id) equals 1/16", abs(c["w8_tid"].real - float(one_sixteenth)) < 1e-9, f"w8={c['w8_tid'].real:.12f}")
    max_imag = max(abs(c["w8_tv"].imag), abs(c["w3_tv"].imag), abs(c["w3_tid"].imag), abs(c["w8_tid"].imag))
    check("C5 sampled spectral coefficients have negligible imaginary parts", max_imag < 1e-9, f"max_imag={max_imag:.3e}")
    return c


def section_d(c):
    print("SECTION D -- parameter-free numbers")
    d = weyl_grid(1600, complex_coefficients=False)
    check("D0 M=800 and M=1600 total moments agree", abs(c["m2_total"] - d["m2_total"]) < 1e-9, f"M800={c['m2_total']:.12f}, M1600={d['m2_total']:.12f}")
    check("D0 M=800 and M=1600 floor moments agree", abs(c["m2_floor"] - d["m2_floor"]) < 1e-9, f"M800={c['m2_floor']:.12f}, M1600={d['m2_floor']:.12f}")
    check("D0 M=800 and M=1600 increments agree", abs(c["increment"] - d["increment"]) < 1e-9, f"M800={c['increment']:.12f}, M1600={d['increment']:.12f}")
    check("D0 M=800 and M=1600 naive moments agree", abs(c["m2_naive"] - d["m2_naive"]) < 1e-9, f"M800={c['m2_naive']:.12f}, M1600={d['m2_naive']:.12f}")
    check("D0 M=800 and M=1600 pi-squared identities agree", abs(c["pi_identity"] - d["pi_identity"]) < 1e-9, f"M800={c['pi_identity']:.12f}, M1600={d['pi_identity']:.12f}")

    check("D1 m^2(T_V) equals the external anchor", abs(c["m2_total"] - 2.440631) < 2e-4, f"{c['m2_total']:.9f}")
    check("D2 m^2(T_id) equals the external anchor", abs(c["m2_floor"] - 1.835061) < 2e-4, f"{c['m2_floor']:.9f}")
    check("D3 registration-attributable increment equals the external anchor", abs(c["increment"] - 0.605570) < 2e-4, f"{c['increment']:.9f}")
    check("D4 naive-branch native moment equals the sensitivity anchor", abs(c["m2_naive"] - 2.411846) < 2e-4, f"{c['m2_naive']:.9f}")
    check("D5 naive-branch |chi_3|^2 identity equals pi^2", abs(c["pi_identity"] - np.pi * np.pi) < 5e-6, f"observed={c['pi_identity']:.12f}, pi^2={np.pi * np.pi:.12f}")
    check("D6 total moment is more than one unit above the unit point", c["m2_total"] > 2.0 and abs(c["m2_total"] - 1.0) > 1.0, f"m2_total={c['m2_total']:.9f}")
    check("D6 readout floor is above 1.5", c["m2_floor"] > 1.5, f"m2_floor={c['m2_floor']:.9f}")
    check("D6 registration-attributable increment is below 0.7", c["increment"] < 0.7, f"increment={c['increment']:.9f}")
    tau_native = c["m2_total"] / 2.0
    beta_map = 3.0 / tau_native
    print(f"       tau_native={tau_native:.9f}; beta_map={beta_map:.9f}")
    monte_carlo_total_m2(c["m2_total"])
    return tau_native, beta_map


def section_e(c):
    print("SECTION E -- Schur contrast")
    check("E1 triplet-only registration and identity kernels agree", c["t3_reg_id_error"] < 1e-12, f"max={c['t3_reg_id_error']:.3e}")
    check(
        "E1 native 3+1 carrier differs by exactly the killed w_3 block",
        abs((c["w3_tid"] - c["w3_tv"]).real - float(Fraction(1, 6))) < 1e-9,
        f"w3_id={c['w3_tid'].real:.12f}, w3_reg={c['w3_tv'].real:.12f}",
    )


def section_f():
    print("SECTION F -- source-boundary guards")
    paths = [NOTE] + list(DEPS.values())
    check("F0 note and four dependency notes exist", all(path.exists() for path in paths), ", ".join(str(path) for path in paths if not path.exists()))
    dep_text = {name: flatten(path.read_text(encoding="utf-8")) for name, path in DEPS.items()}
    require_contains("F1 graph-first dependency marker is present", dep_text["graph-first"], "the joint commutant has dimension `10`")
    require_contains("F1 rigidity dependency marker is present", dep_text["rigidity"], "no independent scalar-normalization freedom")
    require_contains("F1 controlled-copy dependency marker is present", dep_text["controlled-copy"], "projective record-write isometry")
    require_contains("F1 semigroup dependency marker is present", dep_text["semigroup"], "continuous Markov semigroups live on the probability/ensemble")

    note_text = NOTE.read_text(encoding="utf-8")
    flat_note = flatten(note_text)
    markers = [
        "independent audit lane only",
        "parameter-free",
        "zero-sum",
        "does not derive that a record step occurs",
        "not a citation-graph dependency",
        "does not claim:",
        "an audit verdict or any effective-status promotion",
        "refutes the single named route",
        "readout floor",
        "registration-attributable",
        "load-bearing for registration dynamics",
        "1 + chi_8(x)/2",
        "w_8 = 1/16",
    ]
    for marker in markers:
        require_contains(f"F2 note preserve marker: {marker}", flat_note, marker)

    canonical = [
        "**Claim type:** bounded_theorem",
        "**Claim scope:** parameter-free native finite-carrier full-resolution",
        "**Status authority:** independent audit lane only.",
    ]
    for marker in canonical:
        require_contains(f"F2 canonical source metadata: {marker}", flat_note, marker)

    runner_text = Path(__file__).read_text(encoding="utf-8")
    combined = (note_text + "\n" + runner_text).lower()
    forbidden = [
        "**audit " + "status:**",
        "**status:** " + "pass",
        "audit_" + "status:",
        "effective_" + "status:",
        "only " + "route",
        "ex" + "hausted",
        "closes " + "the route",
    ]
    bad = [needle for needle in forbidden if needle in combined]
    check("F3 note and runner avoid forbidden status and closure phrases", not bad, ", ".join(bad))


def main():
    print("NATIVE FINITE-CARRIER REGISTRATION KERNEL RATE VS UNIT-VARIANCE POINT")
    print("=" * 72)
    t3, tv, usym, uanti, casimir = section_a()
    section_b(t3, tv, usym, uanti, casimir)
    c = section_c()
    section_d(c)
    section_e(c)
    section_f()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
