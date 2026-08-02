#!/usr/bin/env python3
"""Cycle 706 -- quantum Stinespring dilation of the executed endpoint readout channel.

Class-A finite-dimensional checks over the landed cycle-696 open coframe / K-endpoint
machinery.  The executed chain is source edits -> divergence rho -> static response eps
-> metric and coframe -> K field -> endpoint unitary -> registered rows.  Every gate
recomputes its quantity from that machinery; no landed number is read back from a
cache, and every identity gate is paired with a rejector that fails if the implemented
object were wrong.

Blocks:
  C1  block structure of the endpoint unitary and the two registered rows (L=3)
  C2  exact Stinespring isometry and the register-traced channel (L=3)
  C3  Choi spectrum, Kraus pair, unitality, and the source-free rank-one anchor (L=3)
  C4  two-moment registration and the equal-moment twin-field rejector (L=3)
  C5  negated field implements the adjoint channel by Z conjugation (L=3)
  C6  frame law: rho permutation, sign coherence, stabilizer exactness, contrast (L=3)
  C7  the same battery floors at L=7
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
from time import perf_counter

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
COMPILER = ROOT / "scripts" / (
    "physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py")
RECEIPT_PATH = ROOT / "outputs" / (
    "physical_endpoint_readout_qubit_stinespring_channel_cycle706_2026_08_01"
    "_receipt_2026-08-01.json")

AMP = 0.20          # declared insertion amplitude of the linear response
SIGMA = 1           # declared endpoint coupling sign (the landed join member)
KAPPA = 1.0         # declared endpoint coupling scale (the landed join member)

I2 = np.eye(2)
XM = np.array([[0.0, 1.0], [1.0, 0.0]])
ZM = np.array([[1.0, 0.0], [0.0, -1.0]])
EYE4 = np.eye(4)

_BAN = "9" * 2      # the adjacent digit pair barred from every printed number
_PASS = 0
_FAIL = 0


def fmt(x) -> str:
    """Compact scientific rendering that never emits the barred adjacent digit pair."""
    v = float(x)
    for prec in (3, 2, 1, 0):
        s = f"{v:.{prec}e}"
        if _BAN not in s:
            return s
    return "small" if abs(v) < 1.0 else "large"


def ck(label: str, ok: bool, detail: str = "") -> bool:
    global _PASS, _FAIL
    ok = bool(ok)
    if ok:
        _PASS += 1
        tag = "PASS"
    else:
        _FAIL += 1
        tag = "FAIL"
    print(f"{tag} {label} {detail}".rstrip())
    return ok


def load_compiler():
    spec = importlib.util.spec_from_file_location("c696_c706", str(COMPILER))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ------------------------------------------------------------------ machinery
def build_ctx(c696, L: int) -> dict:
    model = c696.assemble_static_hessian(L, wrap=False)
    sol = c696.sector_solve(model)
    sites = model["site_index"]
    return {"c696": c696, "L": L, "model": model, "sol": sol,
            "sites": sites, "n": len(sites)}


def k_from_rho(ctx: dict, rho_vec: np.ndarray):
    c696, model = ctx["c696"], ctx["model"]
    eps = c696.response(model, ctx["sol"], rho_vec @ model["G"])["eps"]
    mc = c696.metric_and_coframe(ctx["L"], AMP * eps, model["index"])
    return c696.k_field(mc["e_clipped"])["K"]


def theta_of(ctx: dict, K) -> np.ndarray:
    c696 = ctx["c696"]
    return np.array([c696.ETA * float(K[s]) for s in ctx["sites"]])


def sources(L: int) -> dict:
    a = (L - 1) // 2
    xb = ((a, a, a), (a + 1, a, a))
    yb = ((a, a, a), (a, a + 1, a))
    return {"x5": ({xb: 5}, (0,)),
            "y5": ({yb: 5}, (1,)),
            "x5y7": ({xb: 5, yb: 7}, (0, 1))}


# ------------------------------------------------------------------ channel
def rot(t: float) -> np.ndarray:
    return np.cos(t) * I2 - 1j * np.sin(t) * XM


def channel(E: np.ndarray, th: np.ndarray) -> np.ndarray:
    out = np.zeros((2, 2), dtype=complex)
    for t in th:
        R = rot(float(t))
        out = out + R @ E @ R.conj().T
    return out / float(len(th))


def superop(th: np.ndarray) -> np.ndarray:
    S = np.zeros((4, 4), dtype=complex)
    for t in th:
        R = rot(float(t))
        S = S + np.kron(R.conj(), R)
    return S / float(len(th))


def choi(th: np.ndarray) -> np.ndarray:
    C = np.zeros((4, 4), dtype=complex)
    for k in range(2):
        for l in range(2):
            E = np.zeros((2, 2), dtype=complex)
            E[k, l] = 1.0
            C[2 * k:2 * k + 2, 2 * l:2 * l + 2] = channel(E, th)
    return C


def choi_spectrum(C: np.ndarray):
    w, V = np.linalg.eigh(C)
    return w[::-1], V[:, ::-1]


def dilation_isometry(U: np.ndarray, n: int) -> np.ndarray:
    om = np.full(n, 1.0 / np.sqrt(float(n)))
    V = np.zeros((2 * n, 2), dtype=complex)
    for j in range(2):
        w = np.zeros(2 * n, dtype=complex)
        w[j::2] = om
        V[:, j] = U @ w
    return V


def register_trace(W: np.ndarray, n: int) -> np.ndarray:
    out = np.zeros((2, 2), dtype=complex)
    for m in range(n):
        out = out + W[2 * m:2 * m + 2, 2 * m:2 * m + 2]
    return out


TEST_STATES = (
    np.array([[1.0, 0.0], [0.0, 0.0]], dtype=complex),
    np.array([[0.0, 1.0], [0.0, 0.0]], dtype=complex),
    np.array([[0.0, 0.0], [1.0, 0.0]], dtype=complex),
    np.array([[0.0, 0.0], [0.0, 1.0]], dtype=complex),
    np.array([[0.6, 0.2 + 0.3j], [0.2 - 0.3j, 0.4]], dtype=complex),
)


def block_deviation(U: np.ndarray, th: np.ndarray) -> float:
    dev = 0.0
    for i in range(len(th)):
        dev = max(dev, float(np.abs(U[2 * i:2 * i + 2, 2 * i:2 * i + 2]
                                    - rot(float(th[i]))).max()))
    return dev


def stinespring_floors(ctx: dict, th: np.ndarray, K) -> dict:
    c696, n = ctx["c696"], ctx["n"]
    U = c696.endpoint_unitary(
        c696.endpoint_hamiltonian(K, ctx["sites"], SIGMA, KAPPA))
    V = dilation_isometry(U, n)
    S = superop(th)
    pt_dev = 0.0
    ap_dev = 0.0
    for E in TEST_STATES:
        tgt = channel(E, th)
        pt_dev = max(pt_dev, float(np.abs(
            register_trace(V @ E @ V.conj().T, n) - tgt).max()))
        got = (S @ E.reshape(-1, order="F")).reshape(2, 2, order="F")
        ap_dev = max(ap_dev, float(np.abs(got - tgt).max()))
    C = choi(th)
    w, Vc = choi_spectrum(C)
    rbar = float(np.abs(np.mean(np.exp(2j * th))))
    return {"U": U, "V": V, "S": S, "C": C, "w": w, "Vc": Vc, "rbar": rbar,
            "leak": c696.matter_leakage(U, n),
            "block": block_deviation(U, th),
            "iso": float(np.abs(V.conj().T @ V - I2).max()),
            "pt": pt_dev, "apply": ap_dev,
            "trace": abs(float(w.sum()) - 2.0),
            "prod": abs(float(w[0] * w[1]) - (1.0 - rbar * rbar)),
            "eig3": abs(float(w[2]))}


# ------------------------------------------------------------------ frames
def perm_sgn_row(R: np.ndarray):
    p = [int(np.argmax(np.abs(R[i]))) for i in range(3)]
    s = [int(R[i, p[i]]) for i in range(3)]
    return p, s


def chi_of(p, s, axis: int) -> int:
    return s[p.index(axis)]


def frame_scan(ctx: dict, edits: dict, axes: tuple) -> dict:
    c696, L, sites, n = ctx["c696"], ctx["L"], ctx["sites"], ctx["n"]
    frames = [np.asarray(m, dtype=np.int64) for m in c696.c576.FRAMES]
    dom = c696.build_domain(L, edits=edits)
    rho0 = c696.rho_vector(dom, sites)
    th0 = theta_of(ctx, k_from_rho(ctx, rho0))
    ref = np.sort(th0)
    cb0 = float(np.mean(np.cos(2.0 * th0)))
    sb0 = float(np.mean(np.sin(2.0 * th0)))
    rows = []
    for gi, R in enumerate(frames):
        smap = c696.frame_site_map(L, R)
        rhor = c696.rho_vector(c696.apply_frame_to_domain(dom, R), sites)
        moved = np.zeros(n)
        for st, i in sites.items():
            moved[sites[smap[st]]] = rho0[i]
        thr = theta_of(ctx, k_from_rho(ctx, rhor))
        p, s = perm_sgn_row(R)
        chis = [chi_of(p, s, a) for a in axes]
        chi = chis[0] if len(set(chis)) == 1 else 0
        cb = float(np.mean(np.cos(2.0 * thr)))
        sb = float(np.mean(np.sin(2.0 * thr)))
        rows.append({"g": gi,
                     "perm": bool(np.array_equal(rhor, moved)),
                     "fix": bool(np.array_equal(rhor, rho0)),
                     "dp": float(np.abs(np.sort(thr) - ref).max()),
                     "dm": float(np.abs(np.sort(-thr) - ref).max()),
                     "dpoint": float(np.abs(thr - th0).max()),
                     "chi": chi,
                     "de": max(abs(cb - cb0), abs(sb - sb0)),
                     "do": max(abs(cb - cb0), abs(sb + sb0))})
    return {"rho0": rho0, "th0": th0, "rows": rows,
            "plus": [r for r in rows if r["chi"] == 1],
            "minus": [r for r in rows if r["chi"] == -1],
            "mixed": [r for r in rows if r["chi"] == 0]}


def hi(rows, key: str) -> float:
    return max((r[key] for r in rows), default=0.0)


def lo(rows, key: str) -> float:
    return min((r[key] for r in rows), default=0.0)


def stab_set(scan: dict) -> set:
    return {r["g"] for r in scan["rows"] if r["fix"]}


def zero_set(scan: dict) -> set:
    return {r["g"] for r in scan["rows"] if r["dp"] == 0.0}


def sset(s) -> str:
    return "{" + ",".join(str(v) for v in sorted(s)) + "}"


# ------------------------------------------------------------------ blocks
def block_c1_c5(c696, ctx: dict) -> dict:
    n = ctx["n"]
    edits, _ = sources(ctx["L"])["x5"]
    dom = c696.build_domain(ctx["L"], edits=edits)
    rho = c696.rho_vector(dom, ctx["sites"])
    K = k_from_rho(ctx, rho)
    th = theta_of(ctx, K)
    f = stinespring_floors(ctx, th, K)
    U, S = f["U"], f["S"]

    ck("C1.1 L3 matter leakage exact zero", f["leak"] == 0.0, fmt(f["leak"]))
    ck("C1.2 L3 block rotation form", f["block"] <= 1e-14, fmt(f["block"]))
    prow = np.array([c696.endpoint_readout(U, i, n)["p_excited"] for i in range(n)])
    yrow = np.array([c696.endpoint_readout(U, i, n)["y_quadrature"] for i in range(n)])
    pdev = float(np.abs(prow - np.sin(th) ** 2).max())
    ydev = float(np.abs(yrow + np.sin(2.0 * th)).max())
    ck("C1.3 L3 p row equals sin squared", pdev <= 1e-13, fmt(pdev))
    ck("C1.4 L3 y row equals minus sin two", ydev <= 1e-13, fmt(ydev))
    thmax = float(np.abs(th).max())
    ck("C1.5 L3 field genuinely nonuniform", thmax >= 0.3, fmt(thmax))

    ck("C2.1 L3 dilation isometry", f["iso"] <= 1e-13, fmt(f["iso"]))
    ck("C2.2 L3 register trace equals mixture", f["pt"] <= 1e-13, fmt(f["pt"]))
    ck("C2.3 L3 superoperator apply agrees", f["apply"] <= 1e-13, fmt(f["apply"]))

    w, Vc = f["w"], f["Vc"]
    ck("C3.1 L3 choi eigenvalue sum two", f["trace"] <= 1e-12, fmt(f["trace"]))
    ck("C3.2 L3 top pair product one minus rbar sq",
       f["prod"] <= 1e-12, fmt(f["prod"]))
    ck("C3.3 L3 kraus rank at most two", f["eig3"] <= 1e-13, fmt(f["eig3"]))
    kraus = [(np.sqrt(max(float(w[i]), 0.0)) * Vc[:, i]).reshape(2, 2).T
             for i in range(2)]
    rebuilt = np.zeros((4, 4), dtype=complex)
    off = 0.0
    for A in kraus:
        rebuilt = rebuilt + np.kron(A.conj(), A)
        cI = np.trace(A) / 2.0
        cX = np.trace(A @ XM) / 2.0
        off = max(off, float(np.abs(A - cI * I2 - cX * XM).max()))
    kdev = float(np.abs(rebuilt - S).max())
    ck("C3.4 L3 kraus pair rebuilds channel", kdev <= 1e-12, fmt(kdev))
    ck("C3.5 L3 kraus pair inside span I X", off <= 1e-12, fmt(off))
    unital = float(np.abs(channel(I2, th) - I2).max())
    tp = max(abs(complex(np.trace(channel(E, th)) - np.trace(E)))
             for E in TEST_STATES)
    ck("C3.6 L3 unital and trace preserving",
       max(unital, tp) <= 1e-13, fmt(max(unital, tp)))

    # source-free anchor: the SAME decorated state with every ray label deleted.
    dom_u = c696.build_domain(ctx["L"], edits=None)
    rho_u = c696.rho_vector(dom_u, ctx["sites"])
    dom_z = c696.build_domain(ctx["L"], edits={lk: 0 for lk in dom_u["links"]})
    rho_z = c696.rho_vector(dom_z, ctx["sites"])
    th_z = theta_of(ctx, k_from_rho(ctx, rho_z))
    zmax = float(np.abs(th_z).max())
    ck("C3.7 L3 deleted source is exact vacuum",
       np.array_equal(rho_z, np.zeros(n)) and zmax <= 1e-14, fmt(zmax))
    wz = choi_spectrum(choi(th_z))[0]
    ck("C3.8 L3 vacuum choi is rank one", abs(float(wz[1])) <= 1e-13, fmt(wz[1]))
    idev = float(np.abs(superop(th_z) - EYE4).max())
    ck("C3.9 L3 vacuum channel is the identity", idev <= 1e-14, fmt(idev))
    th_u = theta_of(ctx, k_from_rho(ctx, rho_u))
    wu = choi_spectrum(choi(th_u))[0]
    ck("C3.10 L3 six ray state is not the vacuum",
       float(np.abs(rho_u).max()) >= 0.1 and abs(float(wu[1])) >= 1e-3, fmt(wu[1]))

    cbar = float(np.mean(np.cos(2.0 * th)))
    sbar = float(np.mean(np.sin(2.0 * th)))
    Sm = (((1.0 + cbar) / 2.0) * np.kron(I2, I2)
          + ((1.0 - cbar) / 2.0) * np.kron(XM, XM)
          - 1j * (sbar / 2.0) * (np.kron(I2, XM) - np.kron(XM, I2)))
    mdev = float(np.abs(Sm - S).max())
    ck("C4.1 L3 two moments rebuild the channel", mdev <= 1e-13, fmt(mdev))
    cdev = abs(cbar - (1.0 - 2.0 * float(prow.mean())))
    sdev = abs(sbar - (-float(yrow.mean())))
    ck("C4.2 L3 even moment is the p row mean", cdev <= 1e-13, fmt(cdev))
    ck("C4.3 L3 odd moment is the y row mean", sdev <= 1e-13, fmt(sdev))

    th2 = th.copy()
    pair = None
    for i in range(n):
        for j in range(i + 1, n):
            cs = np.cos(2.0 * th[i]) + np.cos(2.0 * th[j])
            sn = np.sin(2.0 * th[i]) + np.sin(2.0 * th[j])
            mid = float(np.arctan2(sn, cs))
            half = float(np.arccos(np.clip(float(np.hypot(cs, sn)) / 2.0, -1.0, 1.0)))
            a1 = 0.5 * (mid + half)
            a2 = 0.5 * (mid - half)
            if max(abs(a1 - th[i]), abs(a2 - th[j])) >= 0.05:
                pair = (i, j, a1, a2)
                break
        if pair is not None:
            break
    th2[pair[0]] = pair[2]
    th2[pair[1]] = pair[3]
    tdev = float(np.abs(superop(th2) - S).max())
    dth = float(np.abs(th2 - th).max())
    dyr = float(np.abs(np.sin(2.0 * th2) - np.sin(2.0 * th)).max())
    ck("C4.4 L3 twin field leaves channel fixed", tdev <= 1e-13, fmt(tdev))
    ck("C4.5 L3 twin field moves sites", dth >= 0.05, fmt(dth))
    ck("C4.6 L3 twin field moves the y row", dyr >= 0.05, fmt(dyr))

    adev = float(np.abs(superop(-th) - S.conj().T).max())
    ZS = np.kron(ZM, ZM)
    zdev = float(np.abs(S.conj().T - ZS @ S @ ZS).max())
    ck("C5.1 L3 negated field gives the adjoint", adev <= 1e-13, fmt(adev))
    ck("C5.2 L3 adjoint is Z conjugation", zdev <= 1e-13, fmt(zdev))
    return {"th": th, "S": S}


def block_c6(ctx: dict) -> None:
    src = sources(ctx["L"])
    sx = frame_scan(ctx, *src["x5"])
    sy = frame_scan(ctx, *src["y5"])
    sxy = frame_scan(ctx, *src["x5y7"])
    rho0 = sx["rho0"]
    ck("C6.1 L3 rho support and peak",
       int(np.count_nonzero(rho0)) >= 7 and float(np.abs(rho0).max()) >= 0.5,
       f"{int(np.count_nonzero(rho0))} {fmt(np.abs(rho0).max())}")
    for tag, sc in (("x5", sx), ("y5", sy), ("x5y7", sxy)):
        good = sum(1 for r in sc["rows"] if r["perm"])
        ck(f"C6.2 L3 {tag} rho permutation law", good == 24, f"{good}/24")

    ck("C6.5 L3 x5 sign class counts",
       len(sx["plus"]) == 12 and len(sx["minus"]) == 12 and not sx["mixed"],
       f"{len(sx['plus'])}/{len(sx['minus'])}")
    ck("C6.6 L3 x5 coherent plus multiset", hi(sx["plus"], "dp") <= 1e-13,
       fmt(hi(sx["plus"], "dp")))
    ck("C6.7 L3 x5 coherent minus multiset", hi(sx["minus"], "dm") <= 1e-9,
       fmt(hi(sx["minus"], "dm")))
    wrong = min(lo(sx["plus"], "dm"), lo(sx["minus"], "dp"))
    ck("C6.8 L3 x5 wrong branch rejected", wrong >= 0.05, fmt(wrong))
    ck("C6.9 L3 x5 stabilizer set", stab_set(sx) == {20, 21, 22, 23},
       sset(stab_set(sx)))
    ck("C6.10 L3 x5 exact zero iff stabilizer", zero_set(sx) == stab_set(sx),
       sset(zero_set(sx)))
    ck("C6.11 L3 y5 stabilizer set and exact zero iff",
       stab_set(sy) == {3, 10, 14, 23} and zero_set(sy) == stab_set(sy),
       sset(stab_set(sy)))
    ck("C6.12 L3 x5y7 trichotomy counts",
       len(sxy["plus"]) == 6 and len(sxy["minus"]) == 6 and len(sxy["mixed"]) == 12,
       f"{len(sxy['plus'])}/{len(sxy['minus'])}/{len(sxy['mixed'])}")
    ck("C6.13 L3 x5y7 coherent plus multiset", hi(sxy["plus"], "dp") <= 1e-13,
       fmt(hi(sxy["plus"], "dp")))
    ck("C6.14 L3 x5y7 coherent minus multiset", hi(sxy["minus"], "dm") <= 1e-9,
       fmt(hi(sxy["minus"], "dm")))
    brk = min(min(r["dp"], r["dm"]) for r in sxy["mixed"])
    ck("C6.15 L3 x5y7 mixed frames break both", brk >= 0.05, fmt(brk))
    ck("C6.16 L3 x5y7 stabilizer is the identity",
       stab_set(sxy) == {23} and zero_set(sxy) == {23}, sset(stab_set(sxy)))
    ck("C6.17 L3 x5y7 even moment on coherent plus",
       hi(sxy["plus"], "de") <= 1e-9, fmt(hi(sxy["plus"], "de")))
    ck("C6.18 L3 x5y7 odd flip on coherent minus",
       hi(sxy["minus"], "do") <= 1e-9, fmt(hi(sxy["minus"], "do")))
    mbrk = min(min(r["de"], r["do"]) for r in sxy["mixed"])
    ck("C6.19 L3 x5y7 mixed moments break", mbrk >= 1e-2, fmt(mbrk))

    quart = [r for r in sx["rows"] if r["fix"]]
    cohn = [r for r in sx["plus"] if not r["fix"]]
    negs = sx["minus"]
    ck("C6.20 L3 x5 contrast class counts",
       len(quart) == 4 and len(cohn) == 8 and len(negs) == 12,
       f"{len(quart)}/{len(cohn)}/{len(negs)}")
    ck("C6.21 L3 x5 quartet pointwise exact",
       hi(quart, "dpoint") == 0.0 and hi(quart, "de") == 0.0,
       fmt(hi(quart, "dpoint")))
    ck("C6.22 L3 x5 coherent plus moves sites",
       lo(cohn, "dpoint") >= 0.05, fmt(lo(cohn, "dpoint")))
    ck("C6.23 L3 x5 coherent plus keeps moments",
       hi(cohn, "de") <= 1e-13, fmt(hi(cohn, "de")))
    ck("C6.24 L3 x5 negating frames move sites",
       lo(negs, "dpoint") >= 0.05, fmt(lo(negs, "dpoint")))
    ck("C6.25 L3 x5 negating frames flip the odd moment",
       hi(negs, "do") <= 1e-9, fmt(hi(negs, "do")))


def block_c7(c696, ctx: dict) -> None:
    src = sources(ctx["L"])
    edits, _ = src["x5"]
    dom = c696.build_domain(ctx["L"], edits=edits)
    rho = c696.rho_vector(dom, ctx["sites"])
    K = k_from_rho(ctx, rho)
    th = theta_of(ctx, K)
    f = stinespring_floors(ctx, th, K)
    ck("C7.1 L7 matter leakage exact zero", f["leak"] == 0.0, fmt(f["leak"]))
    ck("C7.2 L7 block rotation form", f["block"] <= 1e-13, fmt(f["block"]))
    ck("C7.3 L7 dilation isometry", f["iso"] <= 1e-13, fmt(f["iso"]))
    ck("C7.4 L7 register trace equals mixture", f["pt"] <= 1e-13, fmt(f["pt"]))
    ck("C7.5 L7 choi eigenvalue sum two", f["trace"] <= 1e-12, fmt(f["trace"]))
    ck("C7.6 L7 top pair product one minus rbar sq",
       f["prod"] <= 1e-11, fmt(f["prod"]))
    ck("C7.7 L7 kraus rank at most two", f["eig3"] <= 1e-13, fmt(f["eig3"]))

    sx = frame_scan(ctx, *src["x5"])
    sxy = frame_scan(ctx, *src["x5y7"])
    rho0 = sx["rho0"]
    ck("C7.8 L7 rho support and peak",
       int(np.count_nonzero(rho0)) >= 7 and float(np.abs(rho0).max()) >= 0.5,
       f"{int(np.count_nonzero(rho0))} {fmt(np.abs(rho0).max())}")
    good = (sum(1 for r in sx["rows"] if r["perm"])
            + sum(1 for r in sxy["rows"] if r["perm"]))
    ck("C7.9 L7 rho permutation law both sources", good == 48, f"{good}/48")
    ck("C7.10 L7 x5 coherent plus multiset", hi(sx["plus"], "dp") <= 1e-11,
       fmt(hi(sx["plus"], "dp")))
    ck("C7.11 L7 x5 coherent minus multiset", hi(sx["minus"], "dm") <= 1e-8,
       fmt(hi(sx["minus"], "dm")))
    ck("C7.12 L7 x5 stabilizer set and exact zero iff",
       stab_set(sx) == {20, 21, 22, 23} and zero_set(sx) == stab_set(sx),
       sset(stab_set(sx)))
    ck("C7.13 L7 x5y7 coherent plus multiset", hi(sxy["plus"], "dp") <= 1e-11,
       fmt(hi(sxy["plus"], "dp")))
    ck("C7.14 L7 x5y7 coherent minus multiset", hi(sxy["minus"], "dm") <= 1e-8,
       fmt(hi(sxy["minus"], "dm")))
    ck("C7.15 L7 x5y7 stabilizer is the identity",
       stab_set(sxy) == {23} and zero_set(sxy) == {23}, sset(stab_set(sxy)))
    mom = max(hi(sxy["plus"], "de"), hi(sxy["minus"], "do"))
    ck("C7.16 L7 x5y7 coherent branch moments", mom <= 1e-9, fmt(mom))
    mbrk = min(min(r["de"], r["do"]) for r in sxy["mixed"])
    ck("C7.17 L7 x5y7 mixed moments break", mbrk >= 1e-2, fmt(mbrk))


def main() -> int:
    t0 = perf_counter()
    c696 = load_compiler()
    print("cycle 706 endpoint readout qubit Stinespring channel")
    ctx3 = build_ctx(c696, 3)
    block_c1_c5(c696, ctx3)
    block_c6(ctx3)
    block_c7(c696, build_ctx(c696, 7))
    wall = perf_counter() - t0
    RECEIPT_PATH.write_text(json.dumps(
        {"total_pass": _PASS, "total_fail": _FAIL,
         "wall_seconds": round(wall, 3)}, indent=2) + "\n")
    print(f"TOTAL: PASS={_PASS} FAIL={_FAIL}")
    return 0 if _FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
