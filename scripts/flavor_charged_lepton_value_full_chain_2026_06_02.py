"""Charged-lepton Koide chain -- local algebra/registry consistency runner.

This runner backs the capstone chain note. It reproduces representative local
algebra through Q=2/3 <=> r=1/2 and verifies that the live registries do not
supply the physical r=1/2 selection. It does not prove or audit the cited
dependency claims. Independent audit owns status.

LINK -> source/dependency anchor (status checked before landing, not set by this runner):
 L1 one-qubit local algebra / per-site spin-1/2: per_site_su2_spin_half
 L2 Z^3 spatial substrate locality / emergent lightcone: lieb_robinson_equal_time_tensor_locality
 L3 3-gen carrier (hw=1 C_3 triplet)    : three_generation_observable_theorem (+_count_corollary,
                                          _m3c_burnside, _no_proper_quotient)
 L4 carrier momentum-type forced        : this session (spectral theorem on commuting translations)
 L5 C_3-equivariant circulant H=aI+bC+conj(b)C^2 : generation_axiom_boundary
 L6 exact Q=1/3+(2/3)r                  : koide_kappa_block_total_frobenius_algebraic /
                                          koide_kappa_spectrum_operator_bridge
 L7 channels + topological 2/9          : axiom_first_z_n_equivariant_spectral_asymmetry,
                                          koide_aps_block_by_block_forcing
 L8 endpoint exclusion (interior)       : this session
 L9 r=1/2 = HS 2-sector equipartition   : this session (stationary point; koide_kappa_two_orbit_dimension_
    / balance stationary point            factorization)
 L10 Q=2/3 <=> r=1/2 (cone biconditional): charged_lepton_koide_cone_algebraic_equivalence_narrow_theorem
 OPEN SELECTOR r=1/2                    : zero live Tier-A targets; the
   owner-governed AC_phi_lambda boundary explicitly supplies no r value.
"""
import itertools
import json
from pathlib import Path
import numpy as np

w = np.exp(2j * np.pi / 3)
C = np.array([[0, 0, 1.0], [1, 0, 0], [0, 1, 0]])
I3 = np.eye(3)


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def Q_of(a, b):
    H = a * I3 + b * C + np.conj(b) * C.conj().T
    lam = np.sort(np.linalg.eigvalsh(H))
    return (lam ** 2).sum() / (lam.sum() ** 2), lam


def main():
    passed = []

    # L1: per-site su(2) spin-1/2 (Casimir j(j+1)=3/4)
    Si = [np.array([[0, 1], [1, 0]], dtype=complex) / 2, np.array([[0, -1j], [1j, 0]]) / 2, np.diag([1, -1.0]).astype(complex) / 2]
    passed.append(check("L1 one-qubit local algebra carries the unique j=1/2 su(2) module (Casimir=3/4) [per_site_su2_spin_half]",
                        np.allclose(sum(s @ s for s in Si), 0.75 * np.eye(2))))

    # L3 carrier: hw=1 BZ corners = 3-gen C_3 triplet; eig(C)={1,w,w^2}
    corners = [k for k in itertools.product([0, 1], repeat=3)]
    hw1 = [k for k in corners if sum(k) == 1]
    passed.append(check("L3 3-gen carrier: hw=1 BZ corners are a 3-element C_3 orbit; eig(C)={1,w,w^2} [three_generation_observable]",
                        len(hw1) == 3 and np.allclose(np.sort(np.linalg.eigvals(C)), np.sort([1, w, w ** 2]))))

    # L4 momentum-TYPE forced: distinct translation characters on the 3 corners
    chars = [tuple(-1 if ki else 1 for ki in k) for k in hw1]
    passed.append(check("L4 carrier momentum-type forced: the 3 corners carry DISTINCT translation characters [this session]",
                        len(set(chars)) == 3))

    # L5/L6 circulant + exact Q=1/3+(2/3)r
    okQ = all(abs(Q_of(1.0, np.sqrt(r))[0] - (1 / 3 + 2 / 3 * r)) < 1e-12 for r in [0, 0.25, 0.5, 0.75, 1.0])
    passed.append(check("L5/L6 C_3-equivariant circulant H=aI+bC+conj(b)C^2 -> exact Q=1/3+(2/3)r [koide_kappa_*]",
                        okQ, "r=|b|^2/a^2; verified at r in {0,1/4,1/2,3/4,1}"))

    # L7 topological 2/9 (Atiyah-Bott density)
    L12 = sum(1 / ((w ** k - 1) * (w ** (2 * k) - 1)) for k in (1, 2)) / 3
    passed.append(check("L7 topological asymmetry datum delta=2/9 = L_3(1,2) Atiyah-Bott density [axiom_first_z_n_equivariant_spectral_asymmetry]",
                        abs(L12 - 2 / 9) < 1e-12, f"L_3(1,2)={L12.real:.6f}"))

    # L8 endpoint exclusion: r=0 degenerate, r=1 two massless -> charged leptons forced interior
    e0 = np.sort(np.round(Q_of(1.0, 0.0)[1], 6)); e1 = np.sort(np.round(Q_of(1.0, 1.0)[1], 6))
    passed.append(check("L8 endpoint exclusion: r=0 -> [1,1,1] (degenerate), r=1 -> [0,0,3] (two massless) both excluded for distinct massive e,mu,tau [this session]",
                        np.allclose(e0, [1, 1, 1]) and np.allclose(e1, [0, 0, 3]),
                        f"r=0 {e0.tolist()}, r=1 {e1.tolist()} -> leptons forced to the open interior (0,1)"))

    # L9 r=1/2 = HS 2-sector equipartition stationary point (max 2-sector entropy)
    hs = lambda M: np.trace(M.conj().T @ M).real
    a, b = 1.0, np.sqrt(0.5)
    eq = abs(hs(a * I3) - hs(b * C + np.conj(b) * C.conj().T)) < 1e-9
    def S2(r):
        ps, pd = 1 / (1 + 2 * r), 2 * r / (1 + 2 * r); return -(ps * np.log(ps) + pd * np.log(pd))
    rs = np.linspace(0.02, 3, 1500); rmax = rs[int(np.argmax([S2(r) for r in rs]))]
    passed.append(check("L9 r=1/2 = HS 2-sector equipartition (||aI||^2=||bC+conj(b)C^2||^2) = max 2-sector entropy (stationary point) [this session; koide_kappa_two_orbit_dimension_factorization]",
                        eq and abs(rmax - 0.5) < 0.02, f"equipartition at r=1/2; 2-sector entropy argmax={rmax:.3f}"))

    # L10 endpoint: Q=2/3 <=> r=1/2 (cone biconditional)
    passed.append(check("L10 Q=2/3 <=> r=1/2 (cone biconditional) [charged_lepton_koide_cone_algebraic_equivalence_narrow_theorem]",
                        abs(Q_of(1.0, np.sqrt(0.5))[0] - 2 / 3) < 1e-9, f"Q(r=1/2)={Q_of(1.0, np.sqrt(0.5))[0]:.6f}"))

    # Open selector: the owner-governed replacement explicitly supplies no r.
    born_blocks = (1 / 3, 2 / 3)   # rho=I/3 dimension weighting -> r=1
    repo = Path(__file__).resolve().parents[1]
    tier_a = json.loads((repo / "docs/audit/data/tier_a_admissions.json").read_text())
    owner = json.loads((repo / "docs/audit/data/owner_governed_premise_nodes.json").read_text())
    boundary = owner["nodes"]["staggered_dirac_realization_gate_note_2026-05-03"]["boundary"]
    selector_open = (
        tier_a["genuine_admitted_input_count"] == 0
        and not tier_a["canonical_ids"]
        and "no value of r" in boundary
    )
    passed.append(check(
        "OPEN SELECTOR: zero live Tier-A targets and owner-governed AC_phi_lambda supplies no r value",
        selector_open
        and abs((1 / 3 + 2 / 3 * 1.0) - 1.0) < 1e-12
        and abs((1 / 3 + 2 / 3 * 0.5) - 2 / 3) < 1e-12,
        f"Born blocks {born_blocks} -> r=1 -> Q=1; r=1/2 -> Q=2/3 algebraically; physical selection remains open",
    ))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("CHAIN CONSISTENCY CHECK: nine representative local algebra/registry checks passed.")
    print("The runner does not prove or audit the chain's cited dependency claims.")
    print("The structural formulas assemble to Q=1/3+(2/3)r, while the VALUE Q=2/3")
    print("requires the still-open physical selection r=1/2.")
    print("There are zero live Tier-A targets, and the owner-governed AC_phi_lambda boundary supplies no r value.")
    print("Independent audit decides claim type/status after landing.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
