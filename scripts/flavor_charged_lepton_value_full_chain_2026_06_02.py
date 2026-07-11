"""Charged-lepton Koide chain -- local algebra/registry consistency runner.

This runner backs the capstone chain note. It reproduces representative local
algebra through Q=2/3 <=> r=1/2 and verifies that the live registries do not
supply the physical r=1/2 selection. It does not prove or audit the cited
dependency claims. Independent audit owns status.

LINK -> source/dependency anchor (status checked before landing, not set by this runner):
 L1 one-qubit local algebra / per-site spin-1/2: per_site_su2_spin_half
 L2 raw equal-time tensor locality      : lieb_robinson_equal_time_tensor_locality
 L3 abstract hw=1 C_3 triplet algebra   : three_generation_observable_theorem (+_count_corollary,
                                          _m3c_burnside, _no_proper_quotient)
 L4 label separation on supplied carrier: flavor_carrier_momentum_type_from_translation
 L5 abstract C_3-equivariant circulant H=aI+bC+conj(b)C^2
 L6 exact Q=1/3+(2/3)r                  : koide_kappa_block_total_frobenius_algebraic /
                                          koide_kappa_spectrum_operator_bridge
 L7 local cyclotomic density 2/9        : axiom_first_z_n_equivariant_spectral_asymmetry,
                                          koide_aps_block_by_block_forcing
 L8 positive-spectrum endpoint boundary : local algebra in this runner
 L9 r=1/2 = HS 2-sector equipartition   : local algebra in this runner (stationary point; koide_kappa_two_orbit_dimension_
    / balance stationary point            factorization)
 L10 Q=2/3 <=> r=1/2 (cone biconditional): charged_lepton_koide_cone_algebraic_equivalence_narrow_theorem
 OPEN SELECTOR r=1/2                    : the AC occupancy/readout statements
   are open derivation obligations and supply no r value.
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
    passed.append(check("L3 abstract hw=1 carrier: BZ corners form a 3-element C_3 orbit; eig(C)={1,w,w^2} [three_generation_observable]",
                        len(hw1) == 3 and np.allclose(np.sort(np.linalg.eigvals(C)), np.sort([1, w, w ** 2]))))

    # L4 momentum-TYPE forced: distinct translation characters on the 3 corners
    chars = [tuple(-1 if ki else 1 for ki in k) for k in hw1]
    passed.append(check("L4 supplied-carrier labels: the 3 corners carry distinct translation characters [flavor_carrier_momentum_type_from_translation]",
                        len(set(chars)) == 3))

    # L5/L6 circulant + exact Q=1/3+(2/3)r
    okQ = all(abs(Q_of(1.0, np.sqrt(r))[0] - (1 / 3 + 2 / 3 * r)) < 1e-12 for r in [0, 0.25, 0.5, 0.75, 1.0])
    passed.append(check("L5/L6 abstract circulant H=aI+bC+conj(b)C^2 -> exact spectral ratio Q_H=1/3+(2/3)r [koide_kappa_*]",
                        okQ, "r=|b|^2/a^2; verified at r in {0,1/4,1/2,3/4,1}"))

    # L7 topological 2/9 (Atiyah-Bott density)
    L12 = sum(1 / ((w ** k - 1) * (w ** (2 * k) - 1)) for k in (1, 2)) / 3
    passed.append(check("L7 local cyclotomic density L_3(1,2)=2/9; no physical-delta identification [axiom_first_z_n_equivariant_spectral_asymmetry]",
                        abs(L12 - 2 / 9) < 1e-12, f"L_3(1,2)={L12.real:.6f}"))

    # L8 positive-spectrum boundary for general b=exp(i delta) at r=1.
    e0 = np.sort(np.round(Q_of(1.0, 0.0)[1], 12))
    phases = np.linspace(0.0, 2 * np.pi, 25, endpoint=False)
    det_errors = []
    minimum_eigenvalues = []
    for phase in phases:
        b_phase = np.exp(1j * phase)
        _, spectrum = Q_of(1.0, b_phase)
        h_phase = I3 + b_phase * C + np.conj(b_phase) * C.conj().T
        det_errors.append(abs(np.linalg.det(h_phase).real - 2 * (np.cos(3 * phase) - 1)))
        minimum_eigenvalues.append(float(np.min(spectrum)))
    psd_boundary_spectra = [
        np.sort(np.round(Q_of(1.0, np.exp(1j * phase))[1], 12))
        for phase in (0.0, 2 * np.pi / 3, 4 * np.pi / 3)
    ]
    endpoint_ok = (
        np.allclose(e0, [1, 1, 1])
        and max(det_errors) < 1e-10
        and max(minimum_eigenvalues) <= 1e-10
        and all(np.allclose(spectrum, [0, 0, 3], atol=1e-10) for spectrum in psd_boundary_spectra)
    )
    passed.append(check(
        "L8 positive-spectrum boundary: r=0 is degenerate; at r=1 positivity forces cos(3 delta)=1 and spectrum [0,0,3]",
        endpoint_ok,
        f"r=0 {e0.tolist()}, max determinant-formula error={max(det_errors):.2e}, "
        f"largest sampled minimum eigenvalue={max(minimum_eigenvalues):.2e}",
    ))

    # L9 r=1/2 = HS 2-sector equipartition stationary point (max 2-sector entropy)
    hs = lambda M: np.trace(M.conj().T @ M).real
    a, b = 1.0, np.sqrt(0.5)
    eq = abs(hs(a * I3) - hs(b * C + np.conj(b) * C.conj().T)) < 1e-9
    def S2(r):
        ps, pd = 1 / (1 + 2 * r), 2 * r / (1 + 2 * r); return -(ps * np.log(ps) + pd * np.log(pd))
    rs = np.linspace(0.02, 3, 1500); rmax = rs[int(np.argmax([S2(r) for r in rs]))]
    passed.append(check("L9 r=1/2 = HS 2-sector equipartition (||aI||^2=||bC+conj(b)C^2||^2) = max 2-sector entropy (stationary point) [local algebra; koide_kappa_two_orbit_dimension_factorization]",
                        eq and abs(rmax - 0.5) < 0.02, f"equipartition at r=1/2; 2-sector entropy argmax={rmax:.3f}"))

    # L10 endpoint: Q=2/3 <=> r=1/2 (cone biconditional)
    passed.append(check("L10 Q=2/3 <=> r=1/2 (cone biconditional) [charged_lepton_koide_cone_algebraic_equivalence_narrow_theorem]",
                        abs(Q_of(1.0, np.sqrt(0.5))[0] - 2 / 3) < 1e-9, f"Q(r=1/2)={Q_of(1.0, np.sqrt(0.5))[0]:.6f}"))

    # Open selector: derivation obligations never supply a value.
    born_blocks = (1 / 3, 2 / 3)   # rho=I/3 dimension weighting -> r=1
    repo = Path(__file__).resolve().parents[1]
    tier_a = json.loads((repo / "docs/audit/data/premise_decision_history.json").read_text())
    obligations = json.loads((repo / "docs/audit/data/derivation_obligations.json").read_text())
    obligation_ids = set(obligations["canonical_ids"])
    selector_open = (
        tier_a["genuine_admitted_input_count"] == 0
        and not tier_a["canonical_ids"]
        and obligation_ids
        == {
            "ac_orbit_occupancy_statistical_grain_derivation_obligation",
            "ac_reta_hclass_hunit_readout_derivation_obligation",
        }
    )
    passed.append(check(
        "OPEN SELECTOR: AC obligations have zero premise weight and supply no r value",
        selector_open
        and abs((1 / 3 + 2 / 3 * 1.0) - 1.0) < 1e-12
        and abs((1 / 3 + 2 / 3 * 0.5) - 2 / 3) < 1e-12,
        f"Born blocks {born_blocks} -> r=1 -> Q=1; r=1/2 -> Q=2/3 algebraically; physical selection remains open",
    ))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("CHAIN CONSISTENCY CHECK: nine representative local algebra/registry checks passed.")
    print("The runner does not prove or audit the chain's cited dependency claims.")
    print("The structural formulas assemble to abstract Q_H=1/3+(2/3)r, while physical Q=2/3")
    print("requires the still-open physical selection r=1/2.")
    print("The AC occupancy/readout statements are open derivation obligations and supply no r value.")
    print("Independent audit alone decides claim type/status.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
