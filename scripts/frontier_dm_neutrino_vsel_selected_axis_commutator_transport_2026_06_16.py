#!/usr/bin/env python3
"""Selected-axis commutator transport for the DM-neutrino V_sel curvature.

This runner checks a bounded support bridge for the ADM-3 blocker in
DM_NEUTRINO_SCHUR_SUPPRESSION_NAMED_ADMISSIONS_BOUNDED_THEOREM_NOTE_2026-06-07.

The existing no-go says pure even trace invariants of the Dirac Higgs family
M(phi)=sum_i phi_i Gamma_i are radial because M(phi)^2=|phi|^2 I.  This
runner does not reopen that route.  It checks a narrower curvature-only
transport: once a weak axis Gamma_1 is already selected, the graph-trace
normalized Clifford commutator norm

    V_axis(phi) = 8 * tau_D([Gamma_1, M(phi)]^dag [Gamma_1, M(phi)])

has transverse Hessian diag(0,64,64) at e_1, matching the graph-shift
selector curvature packet and hence m_perp=32.  The factor 8 is the source
graph/taste trace dimension from the retained graph-shift selector surface.

The result is support only.  It does not derive the selected-axis physical
functional, the weak coupling g, the physical readout j=g/sqrt(2), or the
full graph-shift potential.
"""

from __future__ import annotations

from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "DM_NEUTRINO_VSEL_SELECTED_AXIS_COMMUTATOR_TRANSPORT_BOUNDED_THEOREM_NOTE_2026-06-16.md"
)
PARENT = ROOT / "docs" / (
    "DM_NEUTRINO_SCHUR_SUPPRESSION_NAMED_ADMISSIONS_BOUNDED_THEOREM_NOTE_2026-06-07.md"
)
NO_GO = ROOT / "docs" / (
    "DM_NEUTRINO_VSEL_CURVATURE_TASTE_TO_DIRAC_TRANSPORT_OBSTRUCTION_NO_GO_NOTE_2026-06-07.md"
)

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    print(f"{tag}: {name}")
    if detail:
        print(f"      {detail}")


def mat_eq(a: sp.Matrix, b: sp.Matrix) -> bool:
    return sp.simplify(a - b) == sp.zeros(*a.shape)


def kron_all(parts: list[sp.Matrix]) -> sp.Matrix:
    out = parts[0]
    for part in parts[1:]:
        out = sp.kronecker_product(out, part)
    return out


def hessian_at(expr: sp.Expr, vars_: tuple[sp.Symbol, ...], point: dict[sp.Symbol, int]) -> sp.Matrix:
    return sp.simplify(sp.hessian(expr, vars_).subs(point))


def main() -> int:
    print("=" * 88)
    print("DM-neutrino V_sel selected-axis commutator transport")
    print("=" * 88)

    phi1, phi2, phi3 = sp.symbols("phi1 phi2 phi3", real=True)
    phi = (phi1, phi2, phi3)
    e1 = {phi1: 1, phi2: 0, phi3: 0}

    I2 = sp.eye(2)
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])

    print("\n[1] Retained graph-shift selector surface")
    shifts = [
        kron_all([sx, I2, I2]),
        kron_all([I2, sx, I2]),
        kron_all([I2, I2, sx]),
    ]
    H = sum((phi[i] * shifts[i] for i in range(3)), sp.zeros(8))
    tr_h2 = sp.simplify(sp.trace(H * H))
    tr_h4 = sp.simplify(sp.trace(H * H * H * H))
    v_graph = sp.expand(tr_h4 - sp.Rational(1, 8) * tr_h2**2)
    target_graph = 32 * (phi1**2 * phi2**2 + phi1**2 * phi3**2 + phi2**2 * phi3**2)
    graph_hess = hessian_at(v_graph, phi, e1)
    check("graph shifts are commuting involutions", all(mat_eq(s * s, sp.eye(8)) for s in shifts)
          and all(mat_eq(shifts[i] * shifts[j], shifts[j] * shifts[i]) for i in range(3) for j in range(3)))
    check("V_graph = Tr H^4 - (1/8)(Tr H^2)^2 = 32 sum phi_i^2 phi_j^2",
          sp.simplify(v_graph - target_graph) == 0,
          f"V_graph={v_graph}")
    check("graph Hessian at e1 is diag(0,64,64); m_perp=32",
          graph_hess == sp.diag(0, 64, 64),
          f"Hess={graph_hess}")

    print("\n[2] Pure Dirac even-trace route remains blocked")
    # 4x4 Euclidean Clifford triple, tensored by I4 to match the C^16 Dirac
    # carrier dimension used in the local neutrino bridge.
    g4 = [
        sp.kronecker_product(sx, I2),
        sp.kronecker_product(sz, sx),
        sp.kronecker_product(sz, sz),
    ]
    I4 = sp.eye(4)
    gammas = [sp.kronecker_product(g, I4) for g in g4]
    d_dirac = gammas[0].shape[0]
    M = sum((phi[i] * gammas[i] for i in range(3)), sp.zeros(d_dirac))
    norm2 = phi1**2 + phi2**2 + phi3**2
    check("Gamma_i are Hermitian Clifford involutions on C^16",
          all(mat_eq(g.conjugate().T, g) and mat_eq(g * g, sp.eye(d_dirac)) for g in gammas)
          and all(mat_eq(gammas[i] * gammas[j] + gammas[j] * gammas[i], sp.zeros(d_dirac))
                  for i in range(3) for j in range(i + 1, 3)))
    check("M(phi)^2 = |phi|^2 I",
          mat_eq(M * M, norm2 * sp.eye(d_dirac)))
    pure_even = sp.expand(sp.trace(M * M * M * M) - sp.Rational(1, 8) * sp.trace(M * M) ** 2)
    pure_hess = hessian_at(pure_even, phi, e1)
    check("pure even trace invariant is radial, as in the retained no-go",
          sp.simplify(pure_even - (d_dirac * (1 - sp.Rational(d_dirac, 8)) * norm2**2)) == 0,
          f"pure_even={pure_even}")
    check("pure even trace Hessian does not match graph selector curvature",
          pure_hess != graph_hess,
          f"pure Hessian={pure_hess}, graph Hessian={graph_hess}")

    print("\n[3] Selected-axis commutator curvature bridge")
    comm = gammas[0] * M - M * gammas[0]
    comm_norm_tau = sp.simplify(sp.trace(comm.conjugate().T * comm) / d_dirac)
    v_axis = sp.expand(8 * comm_norm_tau)
    axis_hess = hessian_at(v_axis, phi, e1)
    check("normalized selected-axis commutator norm tau([G1,M]^dag [G1,M]) = 4(phi2^2+phi3^2)",
          sp.simplify(comm_norm_tau - 4 * (phi2**2 + phi3**2)) == 0,
          f"tau={comm_norm_tau}")
    check("graph-trace-normalized V_axis = 8*tau = 32(phi2^2+phi3^2)",
          sp.simplify(v_axis - 32 * (phi2**2 + phi3**2)) == 0,
          f"V_axis={v_axis}")
    check("selected-axis commutator Hessian at e1 matches graph Hessian exactly",
          axis_hess == graph_hess,
          f"axis Hessian={axis_hess}")
    check("therefore selected-axis commutator curvature gives m_perp=32",
          axis_hess[1, 1] / 2 == 32 and axis_hess[2, 2] / 2 == 32)

    print("\n[4] Boundary and teeth")
    v_axis_no_graph_factor = comm_norm_tau
    no_factor_hess = hessian_at(v_axis_no_graph_factor, phi, e1)
    check("without graph trace factor 8, curvature is not m_perp=32",
          no_factor_hess[1, 1] / 2 != 32,
          f"no-factor Hessian={no_factor_hess}")
    comm_norms = []
    for a in range(3):
        ca = gammas[a] * M - M * gammas[a]
        comm_norms.append(sp.trace(ca.conjugate().T * ca) / d_dirac)
    unselected_average = sp.expand(8 * sum(comm_norms) / 3)
    avg_hess = hessian_at(unselected_average, phi, e1)
    check("averaging over axes removes the selector and fails the graph Hessian",
          avg_hess != graph_hess,
          f"axis-averaged Hessian={avg_hess}")
    check("curvature bridge is not a full potential equality",
          sp.simplify(v_axis - v_graph) != 0,
          f"V_axis - V_graph = {sp.expand(v_axis - v_graph)}")

    print("\n[5] Source firewalls")
    note = NOTE.read_text(encoding="utf-8")
    parent = PARENT.read_text(encoding="utf-8")
    no_go = NO_GO.read_text(encoding="utf-8")
    flat_note = " ".join(note.split())
    flat_note_lower = flat_note.lower()
    flat_parent = " ".join(parent.split())
    check("note declares bounded support and independent audit authority",
          "**Claim type:** bounded_theorem / bounded support" in note
          and "independent audit lane only" in note)
    check("note states pure even-trace no-go is not reopened",
          "does not reopen the pure-even-trace route" in flat_note_lower
          and "selected-axis commutator norm" in flat_note)
    check("note leaves ADM-1, ADM-2, and full physical identification open",
          "ADM-1" in note and "ADM-2" in note and "full graph-shift-to-Dirac-Higgs identification" in flat_note)
    check("parent note cites this support bridge without status promotion",
          "2026-06-16 selected-axis commutator transport support" in parent
          and "No retained-grade proposal or status promotion is made by this wire-up" in parent)
    check("no-go source remains present and scoped to pure even invariants",
          "native even invariant" in no_go and "rotationally invariant" in no_go)
    check("no audit ledger or queue edit is claimed by the note",
          "does not edit audit-owned ledger, queue, registry, or publication-status surfaces" in flat_note)
    check("runner output total is expected by note",
          "TOTAL: PASS=21 FAIL=0" in note)

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
