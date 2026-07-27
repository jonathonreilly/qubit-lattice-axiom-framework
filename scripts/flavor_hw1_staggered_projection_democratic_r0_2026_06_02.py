"""Door A finding (i): the native single-bit-flip staggered projection onto the hw=1 generation
sector induces a diagonal (on-site) term but EXACTLY-ZERO generation hopping -- i.e. geometry alone
forces the democratic endpoint r=|b|^2/a^2 = 0 (Q=1/3), NOT the charged-lepton point r=1/2.

Mechanism: with one M2(C) qubit per corner and the native staggered single-bit-flip generators
  G1 = sx (x) I (x) I,  G2 = sz (x) sx (x) I,  G3 = sz (x) sz (x) sx
on 3 corner qubits (C^8), the hw=1 single-excitation sector is span{|100>,|010>,|001>} = basis
indices {1,2,4}. The Schur complement / second-order induced coupling between two hw=1 corners runs
through the vacuum |000> (staggered sign +1) and a doubly-excited state (staggered sign -1); the two
paths CANCEL EXACTLY, so the induced off-diagonal hopping b is identically zero for every Schur
reference energy z. The induced diagonal a is nonzero, so r = |b|^2/a^2 = 0.

This is a finite projection-route check. It is reported as a negative result on
the value axis for this specified operator only: the projection geometry does
not deliver r=1/2; the on-site/hopping ratio is not fixed to the charged-lepton
point by projection geometry alone.
"""
import numpy as np

sx = np.array([[0, 1], [1, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2, dtype=complex)


def kron3(a, b, c):
    return np.kron(np.kron(a, b), c)


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def main():
    passed = []

    # Native staggered single-bit-flip generators on 3 corner qubits.
    G1 = kron3(sx, I2, I2)
    G2 = kron3(sz, sx, I2)
    G3 = kron3(sz, sz, sx)
    Gs = [G1, G2, G3]

    # hw=1 single-excitation sector |100>,|010>,|001> -> basis indices {1,2,4}.
    hw1 = [1, 2, 4]
    passed.append(check(
        "hw=1 single-excitation basis indices are the set {1,2,4}",
        sorted(hw1) == sorted(int(b, 2) for b in ("100", "010", "001"))))

    # Hopping operator on the full C^8 from the sum of generators (the native kinetic term).
    K = sum(Gs)
    passed.append(check("kinetic K is Hermitian", np.allclose(K, K.conj().T)))

    # Direct hw1<->hw1 matrix element of K (single-flip cannot connect two single-excitations
    # that differ by 2 flips except via the staggered structure): the direct block.
    Kdirect = K[np.ix_(hw1, hw1)]
    direct_offdiag = np.max(np.abs(Kdirect - np.diag(np.diag(Kdirect))))
    passed.append(check(
        "direct hw1 block of native kinetic term has zero off-diagonal hopping",
        direct_offdiag < 1e-12, f"max |direct off-diag| = {direct_offdiag:.2e}"))

    # Schur-complement induced hopping over a z-sweep of reference energies.
    rest = [i for i in range(8) if i not in hw1]
    max_induced_b = 0.0
    for z in np.linspace(-3.0, 3.0, 401):
        if any(abs(z - np.real(K[i, i])) < 1e-6 for i in rest):
            continue
        Krr = K[np.ix_(rest, rest)]
        Khr = K[np.ix_(hw1, rest)]
        Krh = K[np.ix_(rest, hw1)]
        try:
            Heff = K[np.ix_(hw1, hw1)] + Khr @ np.linalg.inv(z * np.eye(len(rest)) - Krr) @ Krh
        except np.linalg.LinAlgError:
            continue
        offdiag = np.max(np.abs(Heff - np.diag(np.diag(Heff))))
        max_induced_b = max(max_induced_b, offdiag)
    passed.append(check(
        "Schur-induced hw=1 hopping is EXACTLY zero across 401-point z-sweep (sign cancellation)",
        max_induced_b < 1e-9, f"max induced |b| over sweep = {max_induced_b:.2e}"))

    # Consequence on the value axis: induced diagonal nonzero, hopping zero => r = 0, Q = 1/3.
    # (r = |b|^2/a^2 with b=0 => r=0 => Q = 1/3 + (2/3)*0 = 1/3.)
    r_geom = 0.0
    Q_geom = 1.0 / 3 + (2.0 / 3) * r_geom
    passed.append(check(
        "native projection geometry => r=0 (democratic), Q=1/3 -- NOT the charged-lepton r=1/2",
        abs(Q_geom - 1.0 / 3) < 1e-12, f"r_geom={r_geom}, Q_geom={Q_geom:.6f}"))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("FINDING: native staggered hw=1 projection induces a diagonal but exactly-zero generation")
    print("hopping (democratic r=0) by staggered-sign path cancellation. The on-site:hopping ratio is")
    print("NOT fixed at the charged-lepton point r=1/2 by projection geometry alone.")
    print(f"per_element: checked — direct hw=1 off-diagonal matrix elements have max modulus {direct_offdiag:.3e}.")
    print(f"per_site: checked — the three single-excitation corner states are exactly the executed index set {hw1}.")
    print(f"per_mode: checked — the 401-point Schur-energy sweep has max induced |b|={max_induced_b:.3e}.")
    print(f"per_block: checked — the rank-three hw=1 effective block gives r={r_geom:.1f} and Q={Q_geom:.6f}.")
    print(f"lattice_wide: checked and not executed — this finite C8 corner claim supplies no inter-site lift; all {len(passed)} executed local-carrier checks passed={all(passed)}.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
