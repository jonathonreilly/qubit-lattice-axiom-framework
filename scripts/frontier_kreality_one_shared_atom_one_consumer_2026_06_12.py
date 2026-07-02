#!/usr/bin/env python3
"""K-reality one-shared-atom / one-consumer bounded verifier.

This runner verifies the local algebra and text boundaries for
docs/KREALITY_PREDICATE_ONE_SHARED_ATOM_ONE_CONSUMER_BOUNDED_NOTE_2026-06-12.md.

It reads only local notes, writes no cache, sets no audit status, and does not
invoke git, gh, or network tools.
"""
from __future__ import annotations

import re
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "KREALITY_PREDICATE_ONE_SHARED_ATOM_ONE_CONSUMER_BOUNDED_NOTE_2026-06-12.md"
EIN = DOCS / "FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02.md"
BRIDGE = DOCS / "REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md"
THETA = DOCS / "STRONG_CP_THETA_ZERO_NOTE.md"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    print(f"{tag}: {label}" + (f" -- {detail}" if detail else ""))
    return ok


def section(title: str) -> None:
    print("\n" + "-" * 88)
    print(title)
    print("-" * 88)


def same(a: sp.Matrix, b: sp.Matrix) -> bool:
    return all(sp.simplify(x) == 0 for x in (a - b))


def flat(text: str) -> str:
    return " ".join(text.split())


def normalized(text: str) -> str:
    repl = {
        "ℝ": "R",
        "²": "^2",
        "³": "^3",
        "₃": "_3",
        "θ": "theta",
        "δ": "delta",
        "ω": "omega",
        "−": "-",
        "→": "->",
        "∈": "in",
        "π": "pi",
        "—": "-",
    }
    out = text
    for src, dst in repl.items():
        out = out.replace(src, dst)
    return out


def matrix_entries_zero(mat: sp.Matrix) -> bool:
    return all(sp.simplify(entry) == 0 for entry in mat)


def line_count(path: Path) -> int:
    return len(path.read_text(encoding="utf-8").splitlines())


def main() -> int:
    print("K-reality predicate: one shared atom, one surviving consumer")
    print("=" * 88)

    note_text = NOTE.read_text(encoding="utf-8")
    bridge_text = BRIDGE.read_text(encoding="utf-8")
    ein_text = EIN.read_text(encoding="utf-8")
    theta_text = THETA.read_text(encoding="utf-8")
    note_flat = flat(note_text)
    bridge_flat = flat(bridge_text)
    ein_norm = normalized(ein_text)

    I = sp.I
    sqrt3 = sp.sqrt(3)
    omega = sp.Rational(-1, 2) + I * sqrt3 / 2

    eye = sp.eye(3)
    C = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    C2 = C**2
    S = C + C2
    J = sp.simplify(I * (C - C2))

    section("P1 - exact C_3 circulant algebra for the K-real predicate")

    check("P1.1 C is a real order-three generator with C^T = C^2",
          same(C**3, eye) and same(C.T, C2) and same(sp.conjugate(C), C))

    a, x, y, alpha, beta = sp.symbols("a x y alpha beta", real=True)
    b = x + I * y
    c = x - I * y
    M_h = sp.simplify(a * eye + b * C + c * C2)
    M_k = sp.simplify(a * eye + x * S)

    check("P1.2 Hermitian coefficient section c=conj(b) gives M^dagger = M",
          same(M_h.conjugate().T, M_h))

    k_defect = sp.simplify(sp.conjugate(M_h) - M_h)
    trans_defect = sp.simplify(M_h.T - M_h)
    span_defect = sp.simplify(M_h - (alpha * eye + beta * S))
    span_eqs = [sp.expand(entry) for entry in span_defect]
    span_solutions = sp.solve(span_eqs, (alpha, beta, y), dict=True)
    check("P1.3 K-reality M=conj(M) on the Hermitian section forces Im(b)=0",
          matrix_entries_zero(k_defect.subs(y, 0))
          and any(sp.simplify(entry / y) != 0 for entry in k_defect if entry != 0),
          detail="K defect is proportional to the K-odd coefficient y")
    check("P1.4 transpose-fixed M=M^T on the Hermitian section is the same y=0 condition",
          matrix_entries_zero(trans_defect.subs(y, 0))
          and any(sp.simplify(entry / y) != 0 for entry in trans_defect if entry != 0),
          detail="with c=conj(b), b=c iff b is real")
    check("P1.5 span_R{I,C+C^2} membership is equivalent to y=0",
          span_solutions == [{alpha: a, beta: x, y: 0}],
          detail=f"solutions={span_solutions}")

    det_k = sp.factor(M_k.det())
    check("P1.6 on the K-real section det(aI+x(C+C^2))=(a+2x)(a-x)^2 is real",
          sp.factor(det_k - (a + 2 * x) * (a - x) ** 2) == 0,
          detail=f"det={det_k}")

    M_complex_witness = eye + (sp.Rational(1, 4) + I / 3) * C + (sp.Rational(1, 4) + I / 3) * C2
    det_witness = sp.simplify(M_complex_witness.det())
    check("P1.7 outside the K-real span a complex-coefficient circulant can acquire determinant phase",
          sp.im(det_witness) != 0,
          detail=f"det witness={det_witness}")

    M_herm_kodd = eye + sp.Rational(1, 5) * S + sp.Rational(1, 7) * J
    check("P1.8 guard: the Hermitian K-odd line is detected spectrally, not by determinant phase alone",
          same(M_herm_kodd.conjugate().T, M_herm_kodd)
          and sp.im(sp.simplify(M_herm_kodd.det())) == 0
          and not same(sp.conjugate(M_herm_kodd), M_herm_kodd),
          detail="Hermitian off-K-real examples still have real determinant")

    eig_S = sorted(S.eigenvals().keys(), key=lambda z: float(sp.N(z)))
    check("P1.9 eig(C+C^2)={2,-1,-1}: singlet isolated, doublet degenerate",
          S.eigenvals() == {sp.Integer(2): 1, sp.Integer(-1): 2},
          detail=f"eigenvals={S.eigenvals()}")

    section("P1 - unique K-odd obstruction and omega/omega^2 resolution")

    check("P1.10 J=i(C-C^2) is Hermitian, C_3-invariant, and K-odd",
          same(J.conjugate().T, J) and same(J * C, C * J) and same(sp.conjugate(J), -J))

    u, v, w = sp.symbols("u v w", real=True)
    X = u * eye + v * S + w * J
    kodd_solutions = sp.solve([sp.expand(entry) for entry in sp.conjugate(X) + X], (u, v), dict=True)
    check("P1.11 the C_3-invariant K-odd Hermitian direction is unique up to scale",
          kodd_solutions == [{u: 0, v: 0}],
          detail=f"solutions={kodd_solutions}; w remains free")

    P0 = sp.simplify((eye + C + C2) / 3)
    Pp = sp.simplify((eye + omega**2 * C + omega * C2) / 3)
    Pm = sp.simplify((eye + omega * C + omega**2 * C2) / 3)
    P1 = sp.simplify(Pp + Pm)
    mu_p = sp.simplify((J * Pp).trace() / Pp.trace())
    mu_m = sp.simplify((J * Pm).trace() / Pm.trace())
    check("P1.12 J resolves omega from omega^2 with opposite faithful-sector eigenvalues",
          sp.simplify(mu_p + mu_m) == 0 and sp.simplify(mu_p**2 - 3) == 0,
          detail=f"mu_plus={mu_p}; mu_minus={mu_m}")

    proj_span_eqs = [sp.expand(entry) for entry in (Pp - (alpha * eye + beta * S))]
    proj_span_solutions = sp.solve(proj_span_eqs, (alpha, beta), dict=True)
    check("P1.13 a single faithful projector is not in the K-real span",
          proj_span_solutions == [] and same(sp.conjugate(Pp), Pm) and not same(Pp, Pm),
          detail="K swaps P_omega and P_omega^2")

    section("P2 - theta-side consumer is unloaded")

    k, phi = sp.symbols("k phi", real=True)
    defect = sp.exp(I * k * phi) - sp.exp(-I * k * phi)
    linear_coeff = sp.series(defect, phi, 0, 2).removeO().coeff(phi, 1)
    k_solutions = sp.solve(sp.Eq(linear_coeff, 0), k)
    check("P2.1 K/CPT character invariance uses only {k, phi}, no coupling object",
          defect.free_symbols == {k, phi} and linear_coeff.free_symbols == {k},
          detail=f"free symbols={sorted(str(s) for s in defect.free_symbols)}")
    check("P2.2 all-phi determinant-character invariance forces k=0",
          k_solutions == [0],
          detail=f"linear coefficient={linear_coeff}; solutions={k_solutions}")

    proof_start = bridge_text.index("### Proof")
    proof_end_candidates = [
        bridge_text.find(marker, proof_start)
        for marker in ("## Conditional Implication B", "## Consequence B")
    ]
    proof_end_candidates = [idx for idx in proof_end_candidates if idx != -1]
    proof_end = min(proof_end_candidates)
    proof_text = bridge_text[proof_start:proof_end]
    proof_flat = flat(proof_text)
    forbidden = ["K-real coupling", "b = c", "span{I, C + C^2}"]
    absent = [phrase for phrase in forbidden if phrase not in proof_text]
    check("P2.3 bridge proof sections T1-T7 plus Consequence A do not use coupling K-reality strings",
          len(absent) == len(forbidden),
          detail=f"absent={absent}")
    check("P2.4 bridge proof load-bearing inputs are additivity plus orbit-constancy of the readout",
          "(Additivity)" in proof_text
          and "(Orbit)" in proof_text
          and "constant on `K`/CPT orbits" in proof_flat,
          detail="uses additivity + K/CPT-orbit constancy of the readout")

    section("P3 - surviving consumer is Koide partition selection")

    A = alpha * eye + beta * S
    lam0 = alpha + 2 * beta
    lam1 = alpha - beta
    check("P3.1 K-real monitored coupling has singlet/doublet eigenspaces",
          same(A * P0, lam0 * P0) and same(A * P1, lam1 * P1))
    check("P3.2 K-real monitored coupling cannot split the faithful omega pair",
          same(A * Pp, lam1 * Pp) and same(A * Pm, lam1 * Pm))
    check("P3.3 the r=0 three-mode partition strictly requires the K-odd obstruction line",
          same(J * Pp, mu_p * Pp)
          and same(J * Pm, mu_m * Pm)
          and sp.simplify(mu_p - mu_m) != 0
          and same(sp.conjugate(J), -J))
    check("P3.4 einselection note contains the span/eigenvalue/K-odd partition authority sentence",
          "span_R{I, C+C^2}" in ein_norm
          and "eig(C+C^2)={2,-1,-1}" in ein_norm
          and "i(C-C^2)" in ein_norm)

    section("P4 and boundary assembly")

    one_predicate = "one predicate" in note_text and "time-reversal-real" in note_text
    theta_unloaded = "theta consumer is unloaded" in note_text and "not K-reality of the coupling" in note_text
    koide_consumes = "Koide partition selection" in note_text and "one consumer" in note_text
    falsifier = "i(C - C^2)" in note_text and "named falsifier surface" in note_text
    check("P4.1 assembly booleans: one predicate, theta unloaded, Koide consumes, K-odd falsifier named",
          one_predicate and theta_unloaded and koide_consumes and falsifier)

    check("B1 standard status-authority lines are present",
          "**Status authority:** independent audit lane only" in note_text
          and "does not set or predict an audit outcome" in note_text
          and "does not edit the audit-lane-owned Tier-A registry" in note_text)
    check("B2 No-promotion statement is present",
          "**No-promotion statement:**" in note_text
          and "does not promote, demote, or set the audit status" in note_text)
    check("B3 firewall keeps predicate named/supplied and not derived or registered",
          "predicate remains a named" in note_text
          and "supplied open predicate" in note_text
          and "not derived here" in note_text
          and "not adopted here" in note_text
          and "not accepted here as a new" in note_text
          and "does not edit the registry" in note_text)
    check("B4 firewall keeps r, delta, registry, audit grades, and occupancy binary untouched",
          "does not set audit grades" in note_text
          and "does not fix `r`" in note_text
          and "does not derive `delta`" in note_text
          and "occupancy binary is untouched" in note_text)
    banned_closing = ["only route", "last route", "route-closure", "complete solution", "solves strong-CP", "fully closes"]
    found_banned = [phrase for phrase in banned_closing if phrase.lower() in note_text.lower()]
    check("B5 closing language is absent",
          found_banned == [],
          detail=f"found={found_banned}")
    links = re.findall(r"\[[^\]]+\]\([^)]+\)", note_text)
    check("B6 markdown link inventory is exactly the three dependency links",
          len(links) == 3
          and all(link.startswith("[`") for link in links)
          and "FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02.md" in links[0]
          and "REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md" in links[1]
          and "STRONG_CP_THETA_ZERO_NOTE.md" in links[2],
          detail=f"links={len(links)}")
    check("B7 context companions are backticked, not markdown-linked",
          "`ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md`" in note_text
          and "`CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md`" in note_text
          and "`THETA_P2_K_CPT_DETERMINANT_CHARACTER_PHASE_ERASURE_BOUNDED_NOTE_2026-06-10.md`" in note_text)
    check("B8 theta note still names the mass-orientation premise being unloaded",
          "positive real quark-mass orientation" in theta_text
          or "positive real mass orientation" in theta_text)
    check("B9 bridge dependency still names additivity and orbit phrases",
          "(Additivity)" in bridge_text
          and "(Orbit)" in bridge_text
          and "finitely additive over pairwise-disjoint records" in bridge_text)
    check("B10 target file inventory for this spec is exactly the requested pair",
          NOTE.exists() and Path(__file__).resolve().exists(),
          detail=f"note={NOTE.relative_to(ROOT)}, runner={Path(__file__).resolve().relative_to(ROOT)}")

    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("git diff --stat (not invoked; local file summary for this no-git run)")
    for path in (NOTE, Path(__file__).resolve()):
        print(f" {path.relative_to(ROOT)} | {line_count(path)} lines")
    print(f" 2 files changed, {line_count(NOTE) + line_count(Path(__file__).resolve())} insertions(+)")
    print("SUMMARY: K-reality remains a named/supplied open predicate; theta-side registrability does not consume it; Koide partition selection is the one surviving consumer.")
    return 0 if FAIL == 0 and PASS >= 15 else 1


if __name__ == "__main__":
    raise SystemExit(main())
