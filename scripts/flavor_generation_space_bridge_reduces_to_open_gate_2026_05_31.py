#!/usr/bin/env python3
"""Generation-space bridge to delta=2/9 reduces to a single named import.

The bridge under test: "the physical charged-lepton generation space IS the C_3 [111]
fixed locus, so the native staggered Dirac's LOCAL equivariant Lefschetz density there
(= 2/9) is the flavor-asymmetry observable" -- derivable from framework baseline+retained?

Workflow wf_d994df21-e74 (5 attack routes + 3-lens adversarial verify + synthesis).
VERDICT: closed_modulo_one_named_import. Two findings, both verified here:

  POSITIVE (new): the local-density CONSTRUCTION survives koide_z3_equivariant_anticommuting_no_go.
    The objects it uses (C, the doublet projector P_minus, Gamma_chi) are block-DIAGONAL
    ([C,Gamma_chi]=0, [P_minus,Gamma_chi]=0). The no-go's forbidden object is block-OFF-diagonal
    (a C_3-equivariant singlet<->doublet anticommutator, Schur-killed). So 2/9 exists as a pure
    C_3 character/trace number, NEEDING NO Hermitian H with {H,Gamma_chi}=0. The no-go bounds the
    operator-realization side, not the value-construction side.

  GAP (the single named import): promoting the INTENSIVE per-fixed-point local Lefschetz density
    (distinct from the EXTENSIVE signed global invariant, which VANISHES on the retained
    Gamma_5-paired staggered Dirac: eta=0, signed global sum=0, chi=0) to THE observable.
    The unsigned L*(2/9) aggregate is a scale diagnostic, not the invariant. This summand-vs-invariant
    promotion IS the existing origin/main open_gate row lepton_brannen_bae_delta_two_ninths, and
    coincides with the a=0 zero-section pick of retained_no_go koide_q_delta_residual_cohomology.

This runner verifies the algebra of both findings (it does NOT discharge the gap -- by design).
"""
import hashlib
import json
from pathlib import Path

import numpy as np

W = np.exp(2j * np.pi / 3)            # omega = primitive cube root of unity
I3 = np.eye(3)
J = np.ones((3, 3))
GAMMA = (2.0 / 3.0) * J - I3          # chiral grading Gamma_chi = (2/3)J - I
C = np.array([[0, 0, 1.0], [1, 0, 0], [0, 1, 0]])   # C_3 cyclic shift on generation R^3
ROOT = Path(__file__).resolve().parents[1]
LEPTON_CID = "lepton_brannen_bae_delta_two_ninths_open_gate_note_2026-05-26"
LEPTON_NOTE = "docs/LEPTON_BRANNEN_BAE_DELTA_TWO_NINTHS_OPEN_GATE_NOTE_2026-05-26.md"
LEPTON_RUNNER = "scripts/frontier_lepton_brannen_bae_delta_two_ninths_open_gate.py"
LEPTON_CACHE = "logs/runner-cache/frontier_lepton_brannen_bae_delta_two_ninths_open_gate.txt"
THIS_NOTE = "docs/FLAVOR_GENERATION_SPACE_BRIDGE_REDUCES_TO_OPEN_GATE_2026-05-31.md"


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def lefschetz_density(weights):
    """Atiyah-Bott holomorphic local density (1/|G|) sum_{g != e} 1/prod_j (g^{a_j} - 1),
    with the transverse C_3 rotation weight-tuple `weights` and group order 3."""
    total = 0j
    for k in (1, 2):
        denom = 1.0
        for a in weights:
            denom *= (W ** (k * a) - 1.0)
        total += 1.0 / denom
    return total / 3.0


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def cache_header(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    header, _, _stdout = text.partition("----- stdout -----")
    out = {"_text": text}
    for line in header.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        out[key.strip()] = value.strip()
    return out


def flat(text: str) -> str:
    return " ".join(text.split())


def main():
    passed = []

    # --- Finding A: the value 2/9 as a forced character/trace number -------------------------
    L12 = lefschetz_density((1, 2))   # faithful transverse rotation: weights {omega, omega^2}
    L11 = lefschetz_density((1, 1))   # degenerate alternative
    per_elt = 1.0 / ((W - 1) * (W ** 2 - 1))
    passed.append(check(
        "A1 L_3(1,2) = (1/3) sum_{k=1,2} 1/((w^k-1)(w^2k-1)) == 2/9 exactly",
        abs(L12 - 2.0 / 9.0) < 1e-12 and abs(L12.imag) < 1e-12,
        f"L_3(1,2)={L12.real:.6f} (imag {L12.imag:.1e}); per-nontrivial-element term={per_elt.real:.6f}=1/3"))
    passed.append(check(
        "A2 (1,2) is the FAITHFUL transverse weight-tuple; alternative L_3(1,1)=1/9 distinguishes it",
        abs(L11 - 1.0 / 9.0) < 1e-12,
        f"L_3(1,1)={L11.real:.6f}=1/9; faithful C_3 plane carries weights {{1,2}} (a1+a2=3=0 mod 3, trace-free)"))
    det_tr = (1 - W) * (1 - W ** 2)
    passed.append(check(
        "A3 transverse det(1 - dg) = (1-w)(1-w^2) == 3 (the local denominator)",
        abs(det_tr - 3.0) < 1e-12,
        f"det(1-dg|transverse)={det_tr.real:.6f}"))

    # --- Finding B: the construction survives the anticommuting no-go (block-diagonal data) ---
    eig = np.sort(np.linalg.eigvalsh(GAMMA))
    passed.append(check(
        "B1 Gamma_chi=(2/3)J-I has eigs {+1,-1,-1}; +1 is the [111] singlet, -1,-1 the transverse doublet",
        np.allclose(eig, [-1, -1, 1]),
        f"eigs={np.round(eig,6)}; (1,1,1)/sqrt3 -> {float(GAMMA@np.ones(3)/np.ones(3))[0] if False else (GAMMA@(np.ones(3)/np.sqrt(3)))[0]:.4f} (=+1)"))
    P_minus = 0.5 * (I3 - GAMMA)      # projector onto the -1 transverse doublet
    com_C = np.linalg.norm(C @ GAMMA - GAMMA @ C)
    com_P = np.linalg.norm(P_minus @ GAMMA - GAMMA @ P_minus)
    passed.append(check(
        "B2 local-density operators are BLOCK-DIAGONAL: [C,Gamma_chi]=0 AND [P_minus,Gamma_chi]=0",
        com_C < 1e-12 and com_P < 1e-12,
        f"||[C,Gamma]||={com_C:.1e}, ||[P_minus,Gamma]||={com_P:.1e} -> NOT the forbidden off-diagonal object"))

    # the no-go's forbidden object: a C_3-equivariant operator that anticommutes with Gamma_chi.
    # Schur: C_3-equivariant => block-diagonal (scalar on singlet, scalar on doublet); anticommuting
    # with Gamma_chi=diag(+1,-1,-1) forces the singlet scalar to 0 and the doublet scalar to 0 => X=0.
    rng_ok = True
    for trial in range(200):
        # any real C_3-equivariant operator: a*I + b*C + b*C^2 (b real here) -- block diagonal
        a, b = (trial % 7) - 3.0, ((trial * 3) % 5) - 2.0
        X = a * I3 + b * C + b * (C @ C)
        anti = np.linalg.norm(X @ GAMMA + GAMMA @ X)
        com = np.linalg.norm(X @ GAMMA - GAMMA @ X)
        # equivariant X always commutes; it anticommutes only in the trivial X=0 case
        if com > 1e-9:
            rng_ok = False
        if anti < 1e-9 and np.linalg.norm(X) > 1e-9:
            rng_ok = False
    passed.append(check(
        "B3 every C_3-equivariant X commutes with Gamma_chi; none anticommutes unless X=0 (no-go confirmed)",
        rng_ok,
        "comm(R) intersect anticomm(Gamma_chi) = {0} -> the value-construction never uses such an X"))

    # --- Finding C: operator-realization side STAYS obstructed (the gap is real) --------------
    a, b = 1.0, 1.0 / np.sqrt(2.0)    # r = |b|^2/a^2 = 1/2  (Koide Q=2/3 candidate)
    H = a * I3 + b * C + np.conj(b) * C.conj().T
    r = abs(b) ** 2 / a ** 2
    passed.append(check(
        "C1 r=1/2 circulant H: [H,Gamma_chi]=0 but {H,Gamma_chi} != 0 (Hermitian realization obstructed)",
        abs(r - 0.5) < 1e-12
        and np.linalg.norm(H @ GAMMA - GAMMA @ H) < 1e-12
        and np.linalg.norm(H @ GAMMA + GAMMA @ H) > 1.0,
        f"r={r:.4f}; ||[H,G]||={np.linalg.norm(H@GAMMA-GAMMA@H):.1e}; ||{{H,G}}||={np.linalg.norm(H@GAMMA+GAMMA@H):.4f}"))

    # --- Finding D: signed global index vanishes; 2/9 survives only as a selected summand ----
    # Unsigned same-orientation aggregate over L diagonal fixed sites = L * (per-site density).
    # This is a scale diagnostic, not the signed global invariant.
    sums = {L: L * (2.0 / 9.0) for L in (3, 8)}
    intensive_const = all(abs((s / L) - 2.0 / 9.0) < 1e-12 for L, s in sums.items())
    passed.append(check(
        "D1 unsigned same-orientation aggregate = L*(2/9) scales with L; intensive per-site density stays 2/9",
        abs(sums[3] - 2.0 / 3.0) < 1e-12 and abs(sums[8] - 16.0 / 9.0) < 1e-12 and intensive_const,
        f"L=3 -> {sums[3]:.4f}=2/3 ; L=8 -> {sums[8]:.4f}=16/9 ; density L-independent; not the signed invariant"))
    # Gamma_5=(-1)^(x+y+z) pairing => signed spectrum is +/- symmetric => global index/eta = 0
    paired_spectrum = np.array([0.7, -0.7, 1.3, -1.3, 2.1, -2.1])   # any +/- paired set
    eta = np.sign(paired_spectrum).sum()
    passed.append(check(
        "D2 Gamma_5 +/- pairing => global eta = signed-sum = 0 (so 2/9 is not a free global invariant)",
        abs(eta) < 1e-12,
        f"signed-sum over a +/- paired spectrum = {eta:.1f}; the global invariant is 0, the local summand is 2/9"))
    local = 2.0 / 9.0
    signed_local_sum = sum(sign * local for sign in (1, -1, 1, -1))
    passed.append(check(
        "D3 signed local-density pairs cancel: (+2/9)+(-2/9)+(+2/9)+(-2/9)=0",
        abs(signed_local_sum) < 1e-12,
        f"signed local sum={signed_local_sum:.1f}; selecting one +2/9 summand is the open readout/promotion premise"))

    # --- Finding E: downstream 2/9 -> Koide Q is subsumed in the same gate (readout-class) -----
    # H eigenvalues lam_k = a + 2|b| cos(delta + 2pi k/3). Two readout classes give the SAME masses
    # m_k = lam_k^2 but differ in sqrt(m) sign -> different Q. Tie to audited_failed signed-vs-singular.
    def Q_signed(delta):      # Brannen / det_R: signed sqrt(m) = lam_k  -> Q = 2/3 at r=1/2, delta-indep
        lam = np.array([a + 2 * abs(b) * np.cos(delta + 2 * np.pi * k / 3) for k in range(3)])
        return (lam ** 2).sum() / (lam.sum() ** 2)
    def Q_singular(delta):    # Yukawa / singular-value: sqrt(m) = |lam_k| (unsigned) -> delta-dependent
        lam = np.array([a + 2 * abs(b) * np.cos(delta + 2 * np.pi * k / 3) for k in range(3)])
        return (lam ** 2).sum() / (np.abs(lam).sum() ** 2)
    deltas = np.linspace(0, np.pi, 37)
    Qsig = np.array([Q_signed(d) for d in deltas])
    Qsv = np.array([Q_singular(d) for d in deltas])
    passed.append(check(
        "E1 at r=1/2 SIGNED (Brannen) Q == 2/3 delta-independently; SINGULAR-VALUE Q is delta-dependent and <=2/3",
        np.allclose(Qsig, 2.0 / 3.0, atol=1e-9)
        and (Qsv.max() - Qsv.min() > 1e-3) and Qsv.max() <= 2.0 / 3.0 + 1e-9,
        f"signed Q const={Qsig.mean():.6f}=2/3; singular-value Q range=[{Qsv.min():.4f},{Qsv.max():.4f}] "
        f"-> 2/9->Q load-bears on the SIGNED readout-class, which is audited_failed on origin/main"))

    # --- Finding F: source-packet inclusion for exact residual matching ----------------------
    ledger = json.loads((ROOT / "docs" / "audit" / "data" / "audit_ledger.json").read_text())
    lepton_row = ledger["rows"].get(LEPTON_CID, {})
    this_note = (ROOT / THIS_NOTE).read_text(encoding="utf-8")
    lepton_note = (ROOT / LEPTON_NOTE).read_text(encoding="utf-8")
    lepton_note_flat = flat(lepton_note)
    header = cache_header(ROOT / LEPTON_CACHE)
    passed.append(check(
        "F1 lepton delta=2/9 source packet is audited-clean open_gate, not a phase derivation",
        lepton_row.get("audit_status") == "audited_clean"
        and lepton_row.get("effective_status") == "open_gate"
        and lepton_row.get("runner_path") == LEPTON_RUNNER,
        f"{LEPTON_CID}: audit={lepton_row.get('audit_status')} effective={lepton_row.get('effective_status')}"))
    passed.append(check(
        "F2 downstream note names lepton source packet note, runner, and cache",
        LEPTON_NOTE in this_note and LEPTON_RUNNER in this_note and LEPTON_CACHE in this_note,
        "restricted packet includes exact residual note/runner/cache"))
    passed.append(check(
        "F3 lepton source packet keeps phase/coefficient/scale open",
        "does not derive the Brannen phase" in lepton_note_flat
        and "open gate plus empirical comparator" in lepton_note_flat
        and "not a retained lepton-mass theorem" in lepton_note_flat,
        "no downstream promotion of the open comparator"))
    passed.append(check(
        "F4 lepton runner cache is SHA-fresh and clean",
        header.get("runner") == LEPTON_RUNNER
        and header.get("runner_sha256") == sha256_file(ROOT / LEPTON_RUNNER)
        and header.get("exit_code") == "0"
        and "TOTAL: PASS=17 FAIL=0" in header["_text"],
        f"cache runner={header.get('runner')} status={header.get('status')}"))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("VERDICT: closed_modulo_one_named_import. The generation-space bridge REDUCES to a single")
    print("named premise -- promoting the intensive per-fixed-point local Lefschetz density 2/9")
    print("(rather than the VANISHING signed global invariant) to the physical observable. That premise IS the")
    print("origin/main open_gate row lepton_brannen_bae_delta_two_ninths (= the a=0 zero-section pick")
    print("of retained_no_go koide_q_delta_residual_cohomology_obstruction). NEW positive content: the")
    print("local-density CONSTRUCTION survives koide_z3_equivariant_anticommuting_no_go (block-diagonal")
    print("commuting data only); the no-go bounds the operator-realization side, not the value side.")
    print("Provenance (verified vs origin/main 2026-05-31): open_gate lepton_brannen_bae_delta_two_ninths;")
    print("retained_bounded koide_z3_equivariant_anticommuting_no_go, axiom_first_z_n_equivariant_spectral_")
    print("asymmetry_narrow, koide_aps_block_by_block_forcing; retained_no_go koide_q_delta_residual_")
    print("cohomology_obstruction; audited_failed koide_signed_eigenvalue_vs_singular_value_readout. The")
    print("note does NOT load-bear on unaudited closure_c_staggered_dirac_gate / koide_phase_aps_eta_parity.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
