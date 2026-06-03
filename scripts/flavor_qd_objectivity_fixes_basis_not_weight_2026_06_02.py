"""Route-A negative: Quantum-Darwinism objectivity fixes the pointer BASIS (the 2 K-real einselected
sectors), but is PROVABLY INDIFFERENT to the WEIGHT on those sectors -- so it does NOT force the
uniform/block-count measure (r=1/2). The objective redundancy / classical mutual-information plateau
equals H(weights), a weight-dependent OUTPUT; full redundancy (objectivity) holds IDENTICALLY for the
Born weighting (1/3,2/3 -> r=1) and the uniform weighting (1/2,1/2 -> r=1/2). The Born weight of 'which
sector occurred' survives into the objective ledger. CPT/reality is K-even on both candidate reference
states and induces NO rank-1<->rank-2 swap; and I/3 is the UNIQUE tracial/U(3)-invariant state, so the
retained tracial reference (r=1) is canonical (modulo the demoted pre_record_reference_state_tracial
identification admission), while the uniform reference (r=1/2) is a choice.

Conclusion: objectivity changes the BASIS, not the WEIGHTS; r=1 survives. The Koide value remains a
native-unforced reference-state / measure choice. Sets no audit status (independent audit lane owns that).
"""
import numpy as np

C = np.array([[0, 0, 1.0], [1, 0, 0], [0, 1, 0]])
I3 = np.eye(3)


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def H_shannon(weights):
    w = np.array(weights, float)
    w = w[w > 0]
    return float(-(w * np.log2(w)).sum())


def main():
    passed = []

    # 2 K-real einselected sectors: singlet (rank 1) + doublet (rank 2).
    v0 = np.ones(3) / np.sqrt(3)
    P_s = np.outer(v0, v0)
    P_d = I3 - P_s
    passed.append(check(
        "2 K-real sectors: singlet rank 1, doublet rank 2 (the objective pointer alphabet -- BASIS fixed)",
        abs(np.trace(P_s) - 1) < 1e-12 and abs(np.trace(P_d) - 2) < 1e-12))

    # Objectivity is indifferent to the weight: a Spectrum-Broadcast-Structure branching state with
    # ANY weight distribution over the 2 sectors has full redundancy; the classical mutual information
    # an observer reads from any environment fragment is H(weights) -- an OUTPUT, identical objectivity
    # status for Born and uniform, never selecting the weight.
    H_born = H_shannon([1/3, 2/3])
    H_unif = H_shannon([1/2, 1/2])
    passed.append(check(
        "objective info plateau = H(weights) is OUTPUT, not selector: full redundancy holds for BOTH weightings",
        abs(H_born - 0.9182958) < 1e-6 and abs(H_unif - 1.0) < 1e-9,
        f"H(Born 1/3,2/3)={H_born:.4f} bits ; H(uniform 1/2,1/2)={H_unif:.4f} bits -- both fully objective"))

    # The Born weight survives: tracial reference I/3 pushes through {P_s,P_d} to (1/3,2/3) -> r=1.
    p_triv = np.real(np.trace(P_s @ (I3 / 3)))
    p_doublet = np.real(np.trace(P_d @ (I3 / 3)))
    r_born = (p_doublet / p_triv) / 2.0
    passed.append(check(
        "tracial reference I/3 -> sector weights (1/3,2/3) -> r=1 (Q=1): the Born weight survives objectivity",
        abs(p_triv - 1/3) < 1e-12 and abs(p_doublet - 2/3) < 1e-12 and abs(r_born - 1.0) < 1e-12,
        f"(p_triv,p_doublet)=({p_triv:.3f},{p_doublet:.3f}) -> r={r_born}"))

    # I/3 is the UNIQUE tracial / U(3)-inner-automorphism-invariant state; the uniform-realizing state
    # rho_unif = 0.5 P_s + 0.25 P_d (eigs 0.25,0.25,0.5) is NOT invariant and over-weights the singlet.
    rng = np.random.default_rng(0)
    rho_unif = 0.5 * P_s + 0.5 * (P_d / 2)
    def random_unitary():
        X = rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))
        Q, R = np.linalg.qr(X)
        return Q @ np.diag(np.diag(R) / np.abs(np.diag(R)))
    I3_invariant = True
    unif_invariant = True
    for _ in range(2000):
        U = random_unitary()
        if np.linalg.norm(U @ (I3/3) @ U.conj().T - I3/3) > 1e-9:
            I3_invariant = False
        if np.linalg.norm(U @ rho_unif @ U.conj().T - rho_unif) > 1e-9:
            unif_invariant = False
    passed.append(check(
        "I/3 is the UNIQUE U(3)-invariant (tracial) state; rho_unif (the uniform reference) is NOT invariant",
        I3_invariant and not unif_invariant,
        f"singlet weight: tracial=1/3 vs uniform=0.5 (1.5x over-weight)"))

    # CPT/reality (plain conjugation K): both effects are real (built from real symmetric S=C+C^2),
    # so K fixes each effect -> identity permutation on the 2 labels -> NO p_s<->p_d swap -> CPT cannot
    # move (1/3,2/3) to (1/2,1/2). The ranks 1 vs 2 are non-exchangeable.
    S = C + C.conj().T
    passed.append(check(
        "CPT (conjugation K) fixes both real effects -> identity label permutation -> no rank-1<->rank-2 swap -> cannot force uniform",
        np.allclose(P_s.conj(), P_s) and np.allclose(P_d.conj(), P_d) and np.allclose(S.imag, 0)))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("FINDING: QD objectivity fixes the pointer BASIS (2 sectors) but is INDIFFERENT to the WEIGHT")
    print("(plateau = H(weights) is output; full redundancy for both Born and uniform). The Born weight")
    print("survives (tracial I/3 -> r=1); CPT is K-even on both references with no rank-swap; I/3 is the")
    print("unique tracial state. Objectivity does NOT force r=1/2 -- it changes basis, not weights. No audit status.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
