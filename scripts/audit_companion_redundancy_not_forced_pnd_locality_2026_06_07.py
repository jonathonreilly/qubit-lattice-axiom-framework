#!/usr/bin/env python3
"""Redundancy (local observability) is NOT forced by {durability/PND + Z^3-locality + leading-range}
-- a NO-GO that CONFIRMS and QUANTIFIES the landed open-gate note.

PROVENANCE OF THIS RUNNER. A first version of this script claimed the OPPOSITE -- that redundant
broadcast is the GENERIC outcome of leading-range pointer-non-demolition record-formation, so "local
observability" would be a free corollary. An adversarial review (6 lenses) + the owner found that
verdict was produced by a METHODOLOGICALLY BROKEN genericity test: (i) it sampled only the range-2 ray
H = th*(Z_S X_1 + Z_S X_2), structurally excluding the range-3 joint term from the "generic" PND family,
and (ii) it scored "recoverability > 1e-6", which is NOT the quantum-Darwinism plateau (the plateau
requires each fragment to reach the information deficit (1-delta)*H_S, delta ~ 0.1). This script is the
CORRECTED test, and it reports the honest -- inverted -- result.

HONEST RESULT.
  (A) The redundant broadcast (R_delta = N, every disjoint fragment reaches (1-delta)*H_S) EXISTS, but
      only at a FINE-TUNED point: the pure single-site-sum monitoring Sum_k Z_S (x) X_k AT the CNOT time
      g t = pi/4. At g t = pi/6 the SAME coupling gives Holevo chi = 0.811 < 0.9*H_S per fragment, so
      R_delta = 0. The broadcast is fine-tuned in BOTH the coupling form and the time.
  (B) A GENUINELY generic pointer-non-demolition coupling H = c0 Z_S X_1 + c1 Z_S X_2 + c2 Z_S X_1 X_2
      (random Gaussian c) gives R_delta = N in ~0/300 samples (delta=0.1). Generic PND is non-redundant.
      The range-2 monitoring being present does NOT rescue redundancy: H = 0.5(Z_S X_1 + Z_S X_2)
      + Z_S X_1 X_2 has the range-2 term present yet yields R_delta = 0.
  (C) Therefore PND ([H, Z_S]=0, sourced cleanly from the Record axiom's DURABILITY via the Heisenberg
      necessity leg -- redundancy-free) + Z^3-locality + leading-range do NOT force redundancy. The
      premise that does -- a pure sum of INDEPENDENT single-site monitorings (conditional independence /
      multiplicity) -- IS local observability restated; it is a measure-zero condition, not a corollary.

This CONFIRMS docs/DARWINISM_BRIDGE_RESIDUAL_LOCAL_OBSERVABILITY_OPEN_GATE_NOTE_2026-06-05.md (local
observability is a NAMED OPEN PREMISE not supplied by {Lattice, Quantum, Record}) and quantifies it
(measure-zero in the PND coupling space). It also SHARPENS/CORRECTS
docs/RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md item 1
("[H,Pi_S]=0 => R_delta=n"): that holds only for the single-site-SUM coupling, NOT for a general PND
coupling -- Z_S X_1 X_2 is a pointer-non-demolition counterexample with R_delta=1.

Standard quantum Darwinism (Zurek; Brandao-Piani-Horodecki) is reproven here (Holevo information deficit,
redundancy R_delta), not imported; no PDG/fitted value is used. No framework code.
"""
from __future__ import annotations
from functools import reduce
import numpy as np

PASS = 0
FAIL = 0


def check(name: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    PASS += int(bool(cond))
    FAIL += int(not cond)
    return bool(cond)


# --------------------------------------------------------------------------- #
# Exact dense-qubit machinery (numpy complex128). Site 0 = system S; pointer Z_S.
# --------------------------------------------------------------------------- #
I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
KET0 = np.array([1, 0], dtype=complex)
KET1 = np.array([0, 1], dtype=complex)
DELTA = 0.1  # standard quantum-Darwinism information deficit


def vket(*vecs):
    return reduce(np.kron, vecs)


def single(P, site, n):
    return reduce(np.kron, [P if i == site else I2 for i in range(n)])


def partial_trace(rho, keep, n):
    keep = sorted(keep)
    t = rho.reshape([2] * n + [2] * n)
    offset = 0
    for q in [i for i in range(n) if i not in keep]:
        a = q - offset
        b = (n - offset) + (q - offset)
        t = np.trace(t, axis1=a, axis2=b)
        offset += 1
    k = len(keep)
    return t.reshape(2 ** k, 2 ** k)


def vn_entropy(rho):
    w = np.linalg.eigvalsh(rho)
    w = w[w > 1e-12]
    return float(-np.sum(w * np.log2(w)))


def trace_distance(a, b):
    return 0.5 * float(np.sum(np.abs(np.linalg.eigvalsh(a - b))))


def pointer_conditional(psi, frag, n):
    """Reduced states of `frag` conditioned on Z_S = +1 / -1, plus the pointer priors."""
    Pp = single((I2 + Z) / 2, 0, n)
    Pm = single((I2 - Z) / 2, 0, n)
    vp, vm = Pp @ psi, Pm @ psi
    pp, pm = float(np.real(vp.conj() @ vp)), float(np.real(vm.conj() @ vm))
    rp = (partial_trace(np.outer(vp, vp.conj()) / pp, frag, n) if pp > 1e-12
          else np.eye(2 ** len(frag), dtype=complex) / 2 ** len(frag))
    rm = (partial_trace(np.outer(vm, vm.conj()) / pm, frag, n) if pm > 1e-12
          else np.eye(2 ** len(frag), dtype=complex) / 2 ** len(frag))
    return rp, rm, pp, pm


def pointer_entropy(psi, n):
    _, _, pp, pm = pointer_conditional(psi, [1], n)
    return -sum(p * np.log2(p) for p in (pp, pm) if p > 1e-12)


def holevo_pointer(psi, frag, n):
    """Holevo (accessible classical) information about the pointer Z_S available in `frag`."""
    rp, rm, pp, pm = pointer_conditional(psi, frag, n)
    rho = pp * rp + pm * rm
    return vn_entropy(rho) - (pp * vn_entropy(rp) + pm * vn_entropy(rm))


def records(psi, frag, n, HS, delta=DELTA):
    """QD record criterion: the fragment reaches the (1-delta) information deficit of the pointer."""
    return holevo_pointer(psi, frag, n) >= (1.0 - delta) * HS - 1e-9


def R_delta(psi, env, n, HS, delta=DELTA):
    """Redundancy: number of DISJOINT single-site fragments that each carry the (1-delta) record."""
    return sum(1 for e in env if records(psi, [e], n, HS, delta))


def evolve(H, psi0, t):
    w, V = np.linalg.eigh(H)
    return (V @ np.diag(np.exp(-1j * w * t)) @ V.conj().T) @ psi0


def main() -> int:
    print("REDUNDANCY IS NOT FORCED BY {DURABILITY/PND + Z^3-LOCALITY + LEADING-RANGE}  (NO-GO)")
    print("=" * 82)
    np.random.seed(0)

    # ----------------------------------------------------------------- #
    # B0. The crux that DOES survive: recoverable pointer info (Holevo) != quantum mutual information.
    # ----------------------------------------------------------------- #
    print("\n-- B0. recoverable pointer info = Holevo deficit, NOT quantum mutual information --")
    n3 = 3
    psi_aw = (vket(KET0, KET0, KET0) + vket(KET0, KET1, KET1)
              + vket(KET1, KET0, KET1) + vket(KET1, KET1, KET0)) / 2.0  # Z_S Z_1 Z_2 = +1
    rho_aw = np.outer(psi_aw, psi_aw.conj())
    I_S1 = (vn_entropy(partial_trace(rho_aw, [0], n3)) + vn_entropy(partial_trace(rho_aw, [1], n3))
            - vn_entropy(partial_trace(rho_aw, [0, 1], n3)))
    chi1 = holevo_pointer(psi_aw, [1], n3)
    check(
        "anti-witness Z_S Z_1 Z_2=+1: fragment {1} has FULL quantum mutual info I(S:1)=1 bit yet ZERO "
        "Holevo pointer info (chi=0) -> mutual information is the WRONG QD measure (this refinement holds)",
        abs(I_S1 - 1.0) < 1e-9 and chi1 < 1e-9,
        f"I(S:1)={I_S1:.3f} bit, Holevo chi({{1}})={chi1:.1e}",
    )

    # ----------------------------------------------------------------- #
    # A. The redundant broadcast EXISTS but is FINE-TUNED (coupling form AND time).
    # ----------------------------------------------------------------- #
    print("\n-- A. The R_delta=N broadcast exists only at a fine-tuned coupling form AND time --")
    N = 4
    n = N + 1
    env = list(range(1, n))
    psi0 = vket(*([(KET0 + KET1) / np.sqrt(2)] + [KET0] * N))
    H_sum = sum(single(Z, 0, n) @ single(X, k, n) for k in env)  # pure single-site-sum monitoring
    HS = pointer_entropy(psi0, n)
    psi_cnot = evolve(H_sum, psi0, np.pi / 4)     # CNOT point g t = pi/4
    psi_pi6 = evolve(H_sum, psi0, np.pi / 6)       # off the fine-tuned point
    chi_cnot = holevo_pointer(psi_cnot, [1], n)
    chi_pi6 = holevo_pointer(psi_pi6, [1], n)
    td_pi6 = trace_distance(*pointer_conditional(psi_pi6, [1], n)[:2])
    check(
        f"at the CNOT point (g t = pi/4) the pure single-site-sum coupling gives R_delta = N = {N} "
        f"(every fragment reaches the (1-delta) deficit) -- the broadcast EXISTS here",
        R_delta(psi_cnot, env, n, HS) == N and abs(chi_cnot - HS) < 1e-9,
        f"R_delta={R_delta(psi_cnot, env, n, HS)}, per-fragment Holevo chi={chi_cnot:.3f} = H_S={HS:.3f}",
    )
    check(
        "but at g t = pi/6 the SAME coupling gives per-fragment Holevo chi = 0.811 < 0.9*H_S, trace "
        "distance 0.866 -> R_delta = 0: the broadcast is FINE-TUNED in time, not robust",
        R_delta(psi_pi6, env, n, HS) == 0 and abs(chi_pi6 - 0.811) < 5e-3 and abs(td_pi6 - 0.866) < 5e-3,
        f"R_delta={R_delta(psi_pi6, env, n, HS)}, Holevo chi={chi_pi6:.3f}, trace distance={td_pi6:.3f}",
    )

    # ----------------------------------------------------------------- #
    # B. CORRECTED genericity: a generic PND coupling is non-redundant.
    # ----------------------------------------------------------------- #
    print("\n-- B. CORRECTED genericity over the full PND family H = c0 Z_S X_1 + c1 Z_S X_2 + c2 Z_S X_1 X_2 --")
    ZX1 = single(Z, 0, n3) @ single(X, 1, n3)
    ZX2 = single(Z, 0, n3) @ single(X, 2, n3)
    ZX1X2 = single(Z, 0, n3) @ single(X, 1, n3) @ single(X, 2, n3)
    psi0_3 = vket((KET0 + KET1) / np.sqrt(2), KET0, KET0)
    HS3 = pointer_entropy(psi0_3, n3)
    for tlabel, tval in [("t=1", 1.0), ("t=pi/4", np.pi / 4)]:
        hits = 0
        M = 300
        for _ in range(M):
            c = np.random.randn(3)
            H = c[0] * ZX1 + c[1] * ZX2 + c[2] * ZX1X2
            psi = evolve(H, psi0_3, tval)
            if R_delta(psi, [1, 2], n3, HS3) == 2:
                hits += 1
        check(
            f"generic PND coupling [{tlabel}]: R_delta = 2 (both single fragments reach the (1-delta) "
            f"deficit) in only {hits}/{M} samples -> generic PND is NOT redundant. "
            "Redundant broadcast is measure-zero, NOT the generic outcome",
            hits / M < 0.05,
            f"redundant in {hits}/{M} = {100*hits/M:.1f}% of generic PND couplings",
        )
    # the range-2 term being PRESENT does not rescue redundancy
    H_mix = 0.5 * ZX1 + 0.5 * ZX2 + 1.0 * ZX1X2
    psi_mix = evolve(H_mix, psi0_3, np.pi / 4)
    check(
        "concrete counterexample: H = 0.5(Z_S X_1 + Z_S X_2) + Z_S X_1 X_2 has the range-2 monitoring "
        "PRESENT (coeff 0.5) yet gives R_delta = 0 -> 'leading range present' does NOT force redundancy; "
        "a higher-range admixture destroys it",
        R_delta(psi_mix, [1, 2], n3, HS3) == 0,
        f"R_delta={R_delta(psi_mix, [1, 2], n3, HS3)}; Holevo chi({{1}})={holevo_pointer(psi_mix,[1],n3):.3f} < {(1-DELTA)*HS3:.3f}",
    )

    # ----------------------------------------------------------------- #
    # C. PND alone does not force redundancy (sharpens RECORD_FORMATION item 1).
    # ----------------------------------------------------------------- #
    print("\n-- C. PND alone does NOT force redundancy: a higher-range PND coupling gives R_delta=0 --")
    check(
        "Z_S X_1 X_2 is pointer-non-demolition ([H, Z_S]=0) yet R_delta=0 for disjoint single-site fragments -> RECORD_FORMATION item 1's "
        "'[H,Pi_S]=0 => R_delta=n' holds only for the single-site-SUM coupling, not for general PND",
        np.allclose(ZX1X2 @ single(Z, 0, n3) - single(Z, 0, n3) @ ZX1X2, 0)
        and R_delta(evolve(ZX1X2, psi0_3, np.pi / 4), [1, 2], n3, HS3) <= 0,
        f"||[Z_S X_1 X_2, Z_S]||={np.linalg.norm(ZX1X2 @ single(Z,0,n3) - single(Z,0,n3) @ ZX1X2):.1e}, "
        f"single-site R_delta={R_delta(evolve(ZX1X2, psi0_3, np.pi/4), [1,2], n3, HS3)}",
    )

    print(f"\nSCORECARD PASS={PASS} FAIL={FAIL}")
    print(
        "VERDICT (NO-GO): redundant broadcast / local observability is NOT forced by {durability/PND "
        "(clean, redundancy-free) + Z^3-locality + leading-range}. It exists only at a measure-zero, "
        "fine-tuned set (pure single-site-sum monitoring at the CNOT time); a generic pointer-non-"
        "demolition coupling is non-redundant. The premise that does force it -- a pure sum of "
        "independent single-site monitorings (conditional independence / multiplicity) -- IS local "
        "observability restated. This CONFIRMS + QUANTIFIES the landed open-gate note: local "
        "observability is a NAMED OPEN PREMISE not supplied by the axioms. Audit lane sets the verdict."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
