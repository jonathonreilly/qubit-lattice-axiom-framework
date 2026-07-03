#!/usr/bin/env python3
import sys
from pathlib import Path

import numpy as np


PASS = 0
FAIL = 0
BUILD_CACHE = {}
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/THETA_SUPPLIER_FLAVORED_GRADING_SPECTRAL_FLOW_REGISTERS_WINDING_2D_NARROW_THEOREM_NOTE_2026-07-02.md"


def report(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    suffix = " -- " + detail if detail else ""
    print(f"{status}: {name}{suffix}")


def herm(A):
    return 0.5 * (A + A.conj().T)


def norm(A):
    return float(np.linalg.norm(A))


def anticom(A, B):
    return A @ B + B @ A


def comm(A, B):
    return A @ B - B @ A


def _build_parts(L, Q, gauge_seed=None, deform_seed=None, deform_amp=0.05):
    N = L * L

    def idx(x1, x2):
        return (x1 % L) + L * (x2 % L)

    phi = 2.0 * np.pi * Q / (L * L)
    U1 = np.ones((L, L), dtype=complex)
    U2 = np.ones((L, L), dtype=complex)
    for x1 in range(L):
        for x2 in range(L):
            U2[x1, x2] = np.exp(1j * phi * x1)
            if x1 == L - 1:
                U1[x1, x2] = np.exp(-1j * phi * L * x2)
    if deform_seed is not None:
        rng = np.random.default_rng(deform_seed)
        U1 = U1 * np.exp(1j * deform_amp * rng.standard_normal((L, L)))
        U2 = U2 * np.exp(1j * deform_amp * rng.standard_normal((L, L)))
    if gauge_seed is not None:
        rng = np.random.default_rng(gauge_seed)
        g = np.exp(1j * rng.uniform(0, 2 * np.pi, (L, L)))
        for x1 in range(L):
            for x2 in range(L):
                U1[x1, x2] = g[x1, x2] * U1[x1, x2] * np.conj(g[(x1 + 1) % L, x2])
                U2[x1, x2] = g[x1, x2] * U2[x1, x2] * np.conj(g[x1, (x2 + 1) % L])
    tot = 0.0
    for x1 in range(L):
        for x2 in range(L):
            p = U1[x1, x2] * U2[(x1 + 1) % L, x2] * np.conj(U1[x1, (x2 + 1) % L]) * np.conj(U2[x1, x2])
            tot += np.angle(p)
    T1 = np.zeros((N, N), dtype=complex)
    T2 = np.zeros((N, N), dtype=complex)
    eta2 = np.zeros(N)
    eps = np.zeros(N)
    sx2 = np.zeros(N)
    for x1 in range(L):
        for x2 in range(L):
            i = idx(x1, x2)
            T1[i, idx(x1 + 1, x2)] = U1[x1, x2]
            T2[i, idx(x1, x2 + 1)] = U2[x1, x2]
            eta2[i] = (-1.0) ** x1
            eps[i] = (-1.0) ** (x1 + x2)
            sx2[i] = (-1.0) ** x2
    E = np.diag(eps)
    Eta2 = np.diag(eta2)
    Sx2 = np.diag(sx2)
    D = 0.5 * (T1 - T1.conj().T) + 0.5 * Eta2 @ (T2 - T2.conj().T)
    C1 = 0.5 * (T1 + T1.conj().T)
    C2 = 0.5 * (T2 + T2.conj().T)
    S = 0.5 * (C1 @ C2 + C2 @ C1)
    Gf = 1j * Eta2 @ S
    Gw = 1j * Sx2 @ S
    return {
        "D": D,
        "E": E,
        "Gf": Gf,
        "Gw": Gw,
        "S": S,
        "tot": tot,
        "Eta2": Eta2,
        "C1": C1,
        "C2": C2,
    }


def build(L, Q, gauge_seed=None, deform_seed=None, deform_amp=0.05):
    parts = _build_parts(L, Q, gauge_seed, deform_seed, deform_amp)
    return parts["D"], parts["E"], parts["Gf"], parts["Gw"], parts["S"], parts["tot"]


def parts_for(L, Q, gauge_seed=None, deform_seed=None, deform_amp=0.05):
    key = (L, Q, gauge_seed, deform_seed, deform_amp)
    if key not in BUILD_CACHE:
        parts = _build_parts(L, Q, gauge_seed, deform_seed, deform_amp)
        BUILD_CACHE[key] = parts
        label = f"L={L} Q={Q}"
        if gauge_seed is not None:
            label += f" gauge_seed={gauge_seed}"
        if deform_seed is not None:
            label += f" deform_seed={deform_seed} amp={deform_amp}"
        target = 2.0 * np.pi * Q
        err = abs(parts["tot"] - target)
        report("flux self-check " + label, err < 1e-9, f"tot={parts['tot']:.15g} target={target:.15g} err={err:.3e}")
    return BUILD_CACHE[key]


def nneg(H):
    ev = np.linalg.eigvalsh(0.5 * (H + H.conj().T))
    gap = np.min(np.abs(ev))
    if gap <= 1e-10:
        raise ValueError("ambiguous zero eigenvalue, gap=%.2e" % gap)
    return int(np.sum(ev < 0))


def flow_plateau(D, E, G, ms):
    return [nneg(E @ D - m * G) - nneg(E @ D + m * G) for m in ms]


def safe_flow(D, E, G, ms):
    try:
        return flow_plateau(D, E, G, ms), None
    except ValueError as exc:
        return None, str(exc)


def heat_trace_eps(D, E, t):
    A = herm(-D @ D)
    vals, vecs = np.linalg.eigh(A)
    weighted_eps = np.sum(np.conj(vecs) * (E @ vecs), axis=0)
    return np.sum(weighted_eps * np.exp(-t * vals))


def main():
    ms = [0.1, 0.2, 0.3, 0.4, 0.5]
    ms_deform = [0.05, 0.1, 0.2, 0.3, 0.4, 0.5]
    note = NOTE.read_text(encoding="utf-8")
    report(
        "note declares bounded_theorem metadata",
        "**Type:** bounded_theorem" in note and "**Claim type:** bounded_theorem" in note,
    )
    report(
        "note declares bounded 2D scope",
        "**Scope boundary:**" in note
        and "Finite even-L 2D U(1) staggered surfaces" in note
        and "no 4D carrier" in note
        and "no SU(3) extension" in note
        and "no continuum limit" in note,
    )
    report(
        "note leaves audit verdicts to independent lane",
        "**Audit boundary:** Independent audit lane only" in note
        and "audit_status" in note
        and "effective_status" in note
        and "pipeline/auditor-owned" in note,
    )

    free8 = parts_for(8, 0)
    q1_8 = parts_for(8, 1)

    for label, parts in [("L=8 Q=0", free8), ("L=8 Q=1", q1_8)]:
        D = parts["D"]
        E = parts["E"]
        anti_h = norm(D + D.conj().T)
        eps_anti = norm(anticom(E, D))
        report(f"D anti-Hermitian and eps anticommutes with D {label}", anti_h < 1e-13 and eps_anti < 1e-13, f"||D+D^dag||={anti_h:.3e} ||{{eps,D}}||={eps_anti:.3e}")

    for label, parts in [("L=8 Q=0", free8), ("L=8 Q=1", q1_8)]:
        E = parts["E"]
        Gf = parts["Gf"]
        Gw = parts["Gw"]
        vals = {
            "Gf herm": norm(Gf - Gf.conj().T),
            "Gw herm": norm(Gw - Gw.conj().T),
            "[eps,Gf]": norm(comm(E, Gf)),
            "[eps,Gw]": norm(comm(E, Gw)),
        }
        ok = all(v < 1e-13 for v in vals.values())
        detail = " ".join(f"{k}={v:.3e}" for k, v in vals.items())
        report(f"Gamma_f/Gamma_w Hermitian and eps-commuting {label}", ok, detail)

    Eta2 = q1_8["Eta2"]
    C1 = q1_8["C1"]
    C2 = q1_8["C2"]
    S = q1_8["S"]
    forced_vals = {
        "eta2 C1 + C1 eta2": norm(Eta2 @ C1 + C1 @ Eta2),
        "eta2 C2 - C2 eta2": norm(Eta2 @ C2 - C2 @ Eta2),
        "eta2 S + S eta2": norm(Eta2 @ S + S @ Eta2),
    }
    report(
        "forced-i identities",
        all(v < 1e-13 for v in forced_vals.values()),
        " ".join(f"{k}={v:.3e}" for k, v in forced_vals.items()),
    )

    Ge = 1j * q1_8["E"] @ q1_8["S"]
    ge_nonherm = norm(Ge - Ge.conj().T)
    report("rejector gate Ge non-Hermitian", ge_nonherm > 1.0, f"||Ge-Ge^dag||={ge_nonherm:.6f}")

    ev = np.sort(np.linalg.eigvalsh(herm(free8["Gf"])))
    expected = np.sort(np.array([np.cos(2.0 * np.pi * n1 / 8) * np.cos(2.0 * np.pi * n2 / 8) for n1 in range(8) for n2 in range(8)]))
    maxdev = float(np.max(np.abs(ev - expected)))
    report("free-field spectrum of Gamma_f L=8", maxdev < 1e-12, f"maxdev={maxdev:.3e}")

    free_gf_ac = norm(anticom(free8["Gf"], free8["D"]))
    free_gw_ac = norm(anticom(free8["Gw"], free8["D"]))
    report("dressing discriminator free field L=8", free_gf_ac < 1e-12 and free_gw_ac > 1.0, f"||{{Gamma_f,D}}||={free_gf_ac:.6f} ||{{Gamma_w,D}}||={free_gw_ac:.6f}")

    conj_vals = []
    D = q1_8["D"]
    E = q1_8["E"]
    Gf = q1_8["Gf"]
    for m in [0.2, 0.5]:
        H_plus = E @ D - m * Gf
        H_minus = E @ D + m * Gf
        conj_vals.append(norm(E @ H_plus @ E + H_minus))
    report("conjugation antisymmetry", all(v < 1e-13 for v in conj_vals), " ".join(f"m={m}: {v:.3e}" for m, v in zip([0.2, 0.5], conj_vals)))

    for L in [8, 12]:
        for Q in [-2, -1, 0, 1, 2]:
            parts = parts_for(L, Q)
            D = parts["D"]
            E = parts["E"]
            Gf = parts["Gf"]
            Gw = parts["Gw"]
            if Q in [0, 1, 2]:
                ac = norm(anticom(Gf, D))
                print(f"MEASURED: gauged ||{{Gamma_f,D}}||_F L={L} Q={Q} = {ac:.6f}")

            flows, err = safe_flow(D, E, Gf, ms)
            target = [-2 * Q] * len(ms)
            report(f"registration Gamma_f L={L} Q={Q}", err is None and flows == target, f"flows={flows if err is None else err} target={target}")

            flows_eps, err_eps = safe_flow(D, E, E, ms)
            report(f"blind control eps L={L} Q={Q}", err_eps is None and flows_eps == [0] * len(ms), f"flows={flows_eps if err_eps is None else err_eps}")

            flows_gw, err_gw = safe_flow(D, E, Gw, ms)
            report(f"blind control Gamma_w L={L} Q={Q}", err_gw is None and flows_gw == [0] * len(ms), f"flows={flows_gw if err_gw is None else err_gw}")

    gauge = parts_for(8, 1, gauge_seed=7)
    gf_gauge, err_gf_gauge = safe_flow(gauge["D"], gauge["E"], gauge["Gf"], ms)
    eps_gauge, err_eps_gauge = safe_flow(gauge["D"], gauge["E"], gauge["E"], ms)
    report(
        "gauge covariance seed 7 L=8 Q=1",
        err_gf_gauge is None and err_eps_gauge is None and gf_gauge == [-2] * len(ms) and eps_gauge == [0] * len(ms),
        f"flow(Gamma_f)={gf_gauge if err_gf_gauge is None else err_gf_gauge} flow(eps)={eps_gauge if err_eps_gauge is None else err_eps_gauge}",
    )

    for Q in [1, 2]:
        deform = parts_for(8, Q, deform_seed=11, deform_amp=0.05)
        gf_deform, err_gf_deform = safe_flow(deform["D"], deform["E"], deform["Gf"], ms_deform)
        eps_deform, err_eps_deform = safe_flow(deform["D"], deform["E"], deform["E"], ms_deform)
        report(
            f"deformation invariance seed 11 L=8 Q={Q}",
            err_gf_deform is None and err_eps_deform is None and gf_deform == [-2 * Q] * len(ms_deform) and eps_deform == [0] * len(ms_deform),
            f"flow(Gamma_f)={gf_deform if err_gf_deform is None else err_gf_deform} flow(eps)={eps_deform if err_eps_deform is None else err_eps_deform}",
        )

    S = q1_8["S"]
    D = q1_8["D"]
    E = q1_8["E"]
    s_herm = norm(S - S.conj().T)
    try:
        s_flows = flow_plateau(D, E, S, ms)
        clean = s_flows == [-2] * len(ms)
        ok = s_herm < 1e-13 and not clean
        detail = f"REJECTED (ambiguous zero mode / no quantized flow); ||S-S^dag||={s_herm:.3e} flows={s_flows}"
    except ValueError as exc:
        ok = s_herm < 1e-13
        detail = f"REJECTED (ambiguous zero mode / no quantized flow); ||S-S^dag||={s_herm:.3e} error={exc}"
    report("undressed-S rejection", ok, detail)

    heat_abs = []
    for Q in [0, 1, 2]:
        parts = parts_for(8, Q)
        for t in [0.5, 1.0]:
            val = heat_trace_eps(parts["D"], parts["E"], t)
            heat_abs.append(abs(val))
            print(f"MEASURED: heat trace L=8 Q={Q} t={t:.1f} value={val.real:.3e}{val.imag:+.3e}j abs={abs(val):.3e}")
    report("heat-trace control", max(heat_abs) < 1e-10, f"max_abs={max(heat_abs):.3e}")

    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        sys.exit(1)


if __name__ == "__main__":
    main()
