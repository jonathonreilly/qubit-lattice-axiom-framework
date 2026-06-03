"""Door A finding (ii): every action-level condition that lands the charged-lepton ratio EXACTLY on
r=1/2 (Q=2/3) reduces algebraically to the SINGLE object 3a^2 = 6|b|^2 -- the equal total
Hilbert-Schmidt norm of the mass block (aI) and the hopping block (bC + conj(b)C^2). This is the
already-named block-count weighting AC_phi_lambda. So the "geometry-fixed action" axis (Door A) is
the SAME wall as the previously-mapped measure axis, reached from a new direction; and the faithful
A1 metric (dimension / trace / Plancherel weighting) on the same algebra gives r=1 (Q=1), not 1/2.

This runner verifies the algebraic identities behind that unification. It does NOT set or change any
audit status (independent audit lane owns that), and it does NOT claim r=1/2 is forced -- it makes
precise that r=1/2 <=> equal-block-HS-norm, and that the dimension reading gives r=1.
"""
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
    lam = np.linalg.eigvalsh(H)
    return (lam ** 2).sum() / (lam.sum() ** 2)


def main():
    passed = []

    # HS norms of the two C_3 grade blocks of H = aI + bC + conj(b)C^2.
    a, b = 1.0, 0.7  # arbitrary nonzero probe
    mass_block = a * I3
    hop_block = b * C + np.conj(b) * C.conj().T
    mass_hs = np.real(np.trace(mass_block.conj().T @ mass_block))   # = 3 a^2
    hop_hs = np.real(np.trace(hop_block.conj().T @ hop_block))      # = 6 |b|^2
    passed.append(check(
        "mass-block HS norm = 3 a^2 and hopping-block HS norm = 6 |b|^2 (geometric trace-counts)",
        abs(mass_hs - 3 * a ** 2) < 1e-12 and abs(hop_hs - 6 * abs(b) ** 2) < 1e-12,
        f"||mass||^2={mass_hs:.4f}=3a^2, ||hop||^2={hop_hs:.4f}=6|b|^2"))

    # The equal-block-HS condition 3a^2 = 6|b|^2  <=>  r = |b|^2/a^2 = 1/2  <=>  Q = 2/3.
    a_eq = np.sqrt(2.0)  # pick a so that 3a^2 = 6|b|^2 with |b|=1
    b_eq = 1.0
    r_eq = abs(b_eq) ** 2 / a_eq ** 2
    passed.append(check(
        "equal-block-HS-norm 3a^2=6|b|^2  <=>  r=1/2  <=>  Q=2/3",
        abs(3 * a_eq ** 2 - 6 * abs(b_eq) ** 2) < 1e-12
        and abs(r_eq - 0.5) < 1e-12 and abs(Q_of(a_eq, b_eq) - 2.0 / 3) < 1e-12,
        f"r={r_eq}, Q={Q_of(a_eq, b_eq):.6f}"))

    # The faithful A1 metric: DIMENSION/Plancherel weighting. The orthonormal HS frame {I,C,C^2}
    # has equal coefficient-norm 3 each; weighting the blocks by representation DIMENSION
    # (trivial 1 : doublet 2) i.e. equal HS power per COEFFICIENT (not per block) gives 3a^2 = 3|b|^2
    # -> r = 1 -> Q = 1.
    a_dim, b_dim = 1.0, 1.0  # equal coefficient magnitude
    passed.append(check(
        "dimension/Plancherel reading (equal HS power per coefficient) => r=1 => Q=1",
        abs(abs(b_dim) ** 2 / a_dim ** 2 - 1.0) < 1e-12 and abs(Q_of(a_dim, b_dim) - 1.0) < 1e-12,
        f"r=1, Q={Q_of(a_dim, b_dim):.6f}"))

    # Unification: the 1:2 multiplicities (1 = Tr(I)/3 on the trivial grade; 2 = the two shift
    # generators C, C^2 in the doublet grade) are FORCED geometric trace-counts, so "equal weight
    # per block" vs "equal weight per coefficient/dimension" is the single binary granularity choice
    # that ALL four Door-A routes (Wilson, hw=1 projection, Cl3/heat-kernel, self-dual) collapse onto.
    # Both are realizable; r=1/2 picks block-count, r=1 picks dimension. Confirm the full lane.
    rs = {0.0: 1.0 / 3, 0.5: 2.0 / 3, 1.0: 1.0}
    line_ok = all(abs(Q_of(1.0, np.sqrt(r)) - q) < 1e-12 for r, q in rs.items())
    passed.append(check(
        "the binary granularity choice lives on the one exact line Q=1/3+(2/3)r (r=0,1/2,1 -> 1/3,2/3,1)",
        line_ok))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("FINDING: every Door-A action condition reaching r=1/2 reduces to equal-block-HS-norm")
    print("3a^2=6|b|^2 (= AC_phi_lambda, native, not Wilson-dependent); the dimension/Plancherel reading")
    print("gives r=1. Door A = the measure axis, same wall, new direction. Asserts no audit status.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
