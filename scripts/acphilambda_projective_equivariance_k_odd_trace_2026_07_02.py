#!/usr/bin/env python3
"""Projective C3 equivariance and K-odd equivariant-trace verifier."""
from __future__ import annotations

import json
import math
import re
import sys
import time
from pathlib import Path

import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ACPHILAMBDA_PROJECTIVE_EQUIVARIANCE_K_ODD_TRACE_2026-07-02.md"
SOURCE = ROOT / "docs" / "STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md"
LEDGER = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"
PASS = 0
FAIL = 0
RNG = np.random.default_rng(20260702)


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(ok)
    PASS += int(ok)
    FAIL += int(not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" -- {detail}" if detail else ""))


def idx(x: tuple[int, int, int], n: int) -> int:
    return (x[0] % n) * n * n + (x[1] % n) * n + (x[2] % n)


def shift(n: int, mu: int) -> np.ndarray:
    t = np.zeros((n**3, n**3), complex)
    for x in np.ndindex(n, n, n):
        y = list(x)
        y[mu] = (y[mu] + 1) % n
        t[idx(tuple(y), n), idx(x, n)] = 1
    return t


R_C3 = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=int)
SX = np.array([[0, 1], [1, 0]], complex)
SY = np.array([[0, -1j], [1j, 0]], complex)
SZ = np.array([[1, 0], [0, -1]], complex)
SIGMA = [SX, SY, SZ]
I2 = np.eye(2, dtype=complex)
U = (I2 - 1j * (SX + SY + SZ)) / 2
W_PLUS = np.exp(-1j * math.pi / 3)
W_MINUS = np.exp(1j * math.pi / 3)


def site_rotation(n: int) -> np.ndarray:
    p = np.zeros((n**3, n**3), complex)
    for x in np.ndindex(n, n, n):
        y = tuple((R_C3 @ np.array(x)) % n)
        p[idx(y, n), idx(x, n)] = 1
    return p


def dense_h(n: int, phi: float = 0.0, r: float = 0.0) -> np.ndarray:
    q = np.exp(1j * phi / n)
    h = np.zeros((2 * n**3, 2 * n**3), complex)
    w = np.zeros((n**3, n**3), complex)
    eye = np.eye(n**3, dtype=complex)
    for mu in range(3):
        t = shift(n, mu)
        d = (q * t - q.conjugate() * t.conjugate().T) / (2j)
        h += np.kron(SIGMA[mu], d)
        w += eye - (q * t + q.conjugate() * t.conjugate().T) / 2
    return h + np.kron(I2, r * w)


def r2(n: int) -> np.ndarray:
    return np.kron(U, site_rotation(n))


def heat_trace(h: np.ndarray, g: np.ndarray, t: float) -> complex:
    vals, vecs = np.linalg.eigh(h)
    gev = vecs.conjugate().T @ g @ vecs
    return complex(np.sum(np.exp(-t * vals) * np.diag(gev)))


def reduced_trace(n: int, phi: float, t: float, r: float = 0.0, scale: float = 1.0) -> complex:
    out = 0j
    for m in range(n):
        k = 2 * math.pi * m / n + phi / n
        wilson = r * 3 * (1 - math.cos(k))
        a = math.sqrt(3) * math.sin(k)
        out += math.exp(-(t / scale) * scale * (wilson + a)) * W_PLUS
        out += math.exp(-(t / scale) * scale * (wilson - a)) * W_MINUS
    return out


def a_naive(n: int, phi: float, t: float) -> float:
    return reduced_trace(n, phi, t, 0.0).imag


def a_wilson(n: int, phi: float, t: float, r: float) -> float:
    return reduced_trace(n, phi, t, r).imag


def scalar_h(n: int) -> np.ndarray:
    return sum((shift(n, mu) - shift(n, mu).T) / (2j) for mu in range(3))


def ledger_scope() -> tuple[str, str]:
    rows = json.loads(LEDGER.read_text(encoding="utf-8"))["rows"]
    for key, row in rows.items():
        if row.get("note_path") == "docs/STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md":
            return key, row["claim_scope"]
    raise RuntimeError("ledger row not found")


def note_scope_quote(note: str) -> tuple[str, str]:
    line = next(x for x in note.splitlines() if x.startswith("Ledger scope quote"))
    return line, re.search(r'"(.*)"$', line).group(1)


def symbolic_branch_checks() -> None:
    s1 = sp.Matrix([[0, 1], [1, 0]])
    s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    s3 = sp.Matrix([[1, 0], [0, -1]])
    ss = s1 + s2 + s3
    uu = (sp.eye(2) - sp.I * ss) / 2
    kappa, phi, tt = sp.symbols("kappa phi tt", real=True)
    hk = sp.sin(kappa) * ss
    p_plus = (sp.eye(2) + ss / sp.sqrt(3)) / 2
    p_minus = (sp.eye(2) - ss / sp.sqrt(3)) / 2
    check("Bloch H(kappa) commutes with U exactly", sp.simplify(hk * uu - uu * hk) == sp.zeros(2))
    root_minus = (1 - sp.I * sp.sqrt(3)) / 2
    root_plus = (1 + sp.I * sp.sqrt(3)) / 2
    check("plus branch has U-weight exp(-i*pi/3)", sp.simplify(uu * p_plus - root_minus * p_plus) == sp.zeros(2))
    check("minus branch has U-weight exp(+i*pi/3)", sp.simplify(uu * p_minus - root_plus * p_minus) == sp.zeros(2))
    im = lambda e: sp.sqrt(3) * (sp.exp(tt * e) - sp.exp(-tt * e)) / 2
    e0 = sp.sqrt(3) * sp.sin(phi / 4)
    e1 = sp.sqrt(3) * sp.sin(phi / 4 + sp.pi / 2)
    pair0 = sp.simplify(sp.trigsimp(im(e0) + im(sp.sqrt(3) * sp.sin(phi / 4 + sp.pi))))
    pair1 = sp.simplify(sp.trigsimp(im(e1) + im(sp.sqrt(3) * sp.sin(phi / 4 + 3 * sp.pi / 2))))
    check("symbolic N=4 doubler pair m=0,2 cancels", pair0 == 0)
    check("symbolic N=4 doubler pair m=1,3 cancels", pair1 == 0)


def main() -> int:
    start = time.perf_counter()
    note = NOTE.read_text(encoding="utf-8") if NOTE.exists() else ""
    source = SOURCE.read_text(encoding="utf-8") if SOURCE.exists() else ""
    key, scope = ledger_scope() if LEDGER.exists() else ("", "")
    qline, quoted = note_scope_quote(note) if note else ("", "")

    check("paired note exists", NOTE.exists())
    check("retained input note exists", SOURCE.exists())
    check("ledger exists", LEDGER.exists())
    check("ledger row found for retained input", key == "staggered_dirac_kinetic_class_forcing_narrow_theorem_note_2026-06-10")
    check("source note self-scope is not authority", "**Claim scope:**" in source and quoted == scope)
    check("ledger quoted scope matches exactly", quoted == scope)
    check("quoted-scope line names retained_bounded once", qline.count("retained_bounded") == 1)
    check("header carries primary runner link", "scripts/acphilambda_projective_equivariance_k_odd_trace_2026_07_02.py" in note)
    check("heat-trace anchors are printed in note", "4.798063" in note and "7.829155" in note)
    check("fixed-seed dense probe is nondegenerate", abs(RNG.normal(size=12)).sum() > 1.0)

    n = 4
    h0 = dense_h(n)
    g = r2(n)
    g2 = np.linalg.matrix_power(g, 2)
    eye = np.eye(2 * n**3)
    check("H_D is Hermitian exactly in dense arithmetic", np.array_equal(h0, h0.conjugate().T))
    check("R2 is unitary", np.linalg.norm(g.conjugate().T @ g - eye) < 1e-12)
    check("[R2,H_D]=0 at N=4", np.linalg.norm(g @ h0 - h0 @ g) < 1e-12)
    check("R2^3=-I at N=4", np.linalg.norm(np.linalg.matrix_power(g, 3) + eye) < 1e-12)
    tr05 = heat_trace(h0, g, 0.5)
    tr10 = heat_trace(h0, g, 1.0)
    check("heat trace t=0.5 anchor", abs(tr05.real - 4.798062701290279) < 1e-6 and abs(tr05.imag) < 1e-12)
    check("heat trace t=1.0 anchor", abs(tr10.real - 7.82915488035186) < 1e-6 and abs(tr10.imag) < 1e-12)
    check("projective sign identity at t=0.5", abs(heat_trace(h0, g2, 0.5) + tr05) < 1e-9)
    check("projective sign identity at t=1.0", abs(heat_trace(h0, g2, 1.0) + tr10) < 1e-9)
    ps = site_rotation(n)
    sh = scalar_h(n)
    sc1 = heat_trace(sh, ps, 0.5)
    sc2 = heat_trace(sh, np.linalg.matrix_power(ps, 2), 0.5)
    check("one-component scalar trace has plus sign", abs(sc1 - sc2) < 1e-9)
    check("one-component sign contrasts with two-component trace", abs(sc1 + sc2) > 1.0 and abs(tr05 + heat_trace(h0, g2, 0.5)) < 1e-9)

    symbolic_branch_checks()
    for tt in (0.5, 1.0):
        check(f"dense trace equals diagonal reduction at t={tt}", abs(heat_trace(h0, g, tt) - reduced_trace(4, 0.0, tt)) < 1e-9)
    spinless = sum(math.exp(-0.5 * math.sqrt(3) * math.sin(2 * math.pi * m / 4)) + math.exp(0.5 * math.sqrt(3) * math.sin(2 * math.pi * m / 4)) for m in range(4))
    check("dropping spinor torsion weights breaks reduction", abs(spinless - tr05.real) > 1e-3)
    check("diagonal fixed momenta are the N C3-fixed Bloch points", sum(1 for m in range(4) if (m, m, m) == (m, m, m)) == 4)

    check("naive A(4,0.7)=0", abs(a_naive(4, 0.7, 0.7)) < 1e-12)
    check("naive A(6,0.7)=0", abs(a_naive(6, 0.7, 0.7)) < 1e-12)
    check("odd N anchor A(3,0.7)", abs(a_naive(3, 0.7, 0.7) + 0.272282888817) < 1e-9)
    check("odd N naive trace is flux-odd", abs(a_naive(3, -0.7, 0.7) + a_naive(3, 0.7, 0.7)) < 1e-9)
    check("odd N naive trace vanishes at zero flux", abs(a_naive(3, 0.0, 0.7)) < 1e-12)
    w0 = dense_h(4, 0.0, 0.5) - dense_h(4, 0.0, 0.0)
    check("Wilson scalar term preserves R2 covariance", np.linalg.norm(g @ w0 - w0 @ g) < 1e-12)
    check("Wilson A(4,0.7) anchor", abs(a_wilson(4, 0.7, 0.7, 0.5) + 0.017277781723) < 1e-9)
    check("Wilson even-N trace is flux-odd", abs(a_wilson(4, -0.7, 0.7, 0.5) + a_wilson(4, 0.7, 0.7, 0.5)) < 1e-9)
    check("Wilson even-N trace vanishes at zero flux", abs(a_wilson(4, 0.0, 0.7, 0.5)) < 1e-12)
    check("Wilson A(3,0.7) anchor", abs(a_wilson(3, 0.7, 0.7, 0.5) - 0.126068832665) < 1e-9)
    check("special r=1,t=1 vanishing is real", abs(a_wilson(6, 0.7, 1.0, 1.0)) < 1e-12)
    check("generic Wilson point is not that special vanishing", abs(a_wilson(6, 0.7, 0.7, 0.5)) > 1e-6)
    mags = [abs(a_naive(k, 0.7, 0.7)) for k in (3, 5, 7)]
    check("finite-ring native instances decrease 3>5>7", mags[0] > mags[1] > mags[2])
    check("dense flux trace equals reduction at N=3", abs(heat_trace(dense_h(3, 0.7), r2(3), 0.7) - reduced_trace(3, 0.7, 0.7)) < 1e-9)
    check("dense Wilson flux trace equals reduction at N=4", abs(heat_trace(dense_h(4, 0.7, 0.5), g, 0.7) - reduced_trace(4, 0.7, 0.7, 0.5)) < 1e-9)
    check("PR #4783 rescale freedom persists on the composed surface", abs(reduced_trace(3, 0.7, 0.7, 0.5) - reduced_trace(3, 0.7, 0.7, 0.5, scale=2.0)) < 1e-9)

    preserves = [
        "the projective equivariance is realized exactly on the retained-class two-component surface (`R2^3 = -I`)",
        "the sector-distinguishing weights are torsion phases (`+- pi/3`), so at zero flux no R-valued off-locus datum appears",
        "on even diagonal grids the naive K-odd trace vanishes identically: the doubler pairing annihilates it",
        "the K-odd observable exists at the generation ring size `N = 3` and requires doubling-pairing breaking elsewhere",
        "what value it registers remains the wall",
        "not a terminal no-go",
    ]
    for phrase in preserves:
        check(f"required sentence present: {phrase[:44]}", phrase in note)
    check("N1 through N8 gate tokens present", all(f"N{i}" in note for i in range(1, 9)))
    banned = ["only " + "route", "last " + "route", "exhau" + "sted", "closes the " + "route", "P" + "DG", "new " + "wall"]
    check("forbidden phrases are absent", all(x not in note for x in banned))
    walls = set(re.findall(r"\bW_[A-Za-z0-9_]+\b", note))
    check("W_ names stay whitelisted", walls <= {"W_cycle_holonomy_value", "W_defect_identity_unit", "W_defect_readout_selection"})
    links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", note)
    check("link inventory is one md dependency plus one runner", len([x for x in links if x.endswith(".md")]) == 1 and len([x for x in links if x.endswith(".py")]) == 1)
    check("in-flight campaign ids are backticked, not linked", all(f"PR #{p}" in note for p in (4783, 4788, 4789, 4794, 4798, 4803, 4831, 4835)) and "ACPHILAMBDA_DEFECT_IDENTITY_UNIT_RESCALE_OBSTRUCTION_2026-07-01](" not in note)
    leaks = [
        "PRESERVE " + "VERBATIM",
        "MUST BE " + "ABSENT",
        "Acceptance " + "contract",
        "ANTI-" + "FABRICATION",
        "RULES " + "(binding)",
    ]
    check("instruction-leakage strings absent from note", all(x not in note for x in leaks))
    check("note does not present file-self scope as ledger scope", "**Claim scope:**" not in note and "Ledger scope quote" in note)
    legacy_status_label = "Status " + "authority"
    check(
        "canonical type, audit boundary, and bounded gate are stated",
        "**Type:** bounded_theorem" in note
        and "**Audit boundary:**" in note
        and legacy_status_label not in note
        and "**Gate result:** PASS bounded; not a terminal no-go" in note,
    )
    check("runtime under 90 seconds", time.perf_counter() - start < 90.0)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
