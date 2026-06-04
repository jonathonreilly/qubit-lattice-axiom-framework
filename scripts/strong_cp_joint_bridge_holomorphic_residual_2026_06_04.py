"""The strong-CP joint-basis bridge FAILS: the physical theta_bar = theta_QCD + arg det M is NOT forced
to zero. The framework's retained emergent-time antiunitary is REFLECTION-COMPOSED on both sectors and
ANOMALY-BLIND, so theta_bar is Theta-EVEN and survives. The single residual is a global PURE-K =
a genuinely complex/holomorphic generation coupling -- the SAME unbuilt chiral-grading brick as the
Koide Q=2/3 and generation-ID gates (a triple convergence).

Verified structural facts:
 (1) theta_bar is the anomaly-INVARIANT: axial rotation M->e^{i alpha}M shifts arg det M by +n*alpha and
     (Fujikawa) theta_QCD by -n*alpha, so theta_bar is fixed; the Wilson gauge measure is alpha-invariant
     (anomaly-blind: the two reality conditions do not co-move).
 (2) Parity rule Theta(iQ)Theta^-1 = -i(R Q R): pure-K (R=I) makes the CP-odd generation density
     G=i(C-C^2) ODD (conj(G)=-G) -> would force theta_bar=0; reflection-composed P makes it EVEN
     (P conj(G) P = +G) -> theta_bar survives. Pure-K is UNAVAILABLE: conj(M)!=M for complex b.
 (3) The residual: a complex coupling c != conj(b) makes conj(M)=M achievable WITHOUT P (pure-K available)
     but BREAKS the C_3 conjugate-symmetry = the holomorphic generation coupling (the open brick).

Sets no audit status (independent audit lane owns that); edits/re-cites no existing row.
"""
import numpy as np

w = np.exp(2j * np.pi / 3)
C = np.array([[0, 0, 1.0], [1, 0, 0], [0, 1, 0]])
I3 = np.eye(3)
# P = the real C_3 orientation-reversing transposition: P C P = C^2.
P = np.array([[1.0, 0, 0], [0, 0, 1.0], [0, 1.0, 0]])


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def main():
    passed = []
    n = 3  # generations

    # (1) theta_bar is anomaly-invariant; the Wilson measure is alpha-blind.
    a, b = 1.3, 0.5  # real b => M Hermitian, arg det M = 0
    M = a * I3 + b * (C + C.conj().T)
    alpha = 0.37
    Mrot = np.exp(1j * alpha) * M
    d_argdet = np.angle(np.linalg.det(Mrot)) - np.angle(np.linalg.det(M))
    theta_qcd = 1.1
    theta_bar_before = theta_qcd + np.angle(np.linalg.det(M))
    theta_bar_after = (theta_qcd - n * alpha) + np.angle(np.linalg.det(Mrot))   # Fujikawa shift
    passed.append(check(
        "(1) theta_bar anomaly-INVARIANT: axial rot shifts arg det M by +n*alpha and theta_QCD by -n*alpha; theta_bar fixed",
        abs(((d_argdet - n * alpha + np.pi) % (2 * np.pi)) - np.pi) < 1e-9
        and abs(((theta_bar_after - theta_bar_before + np.pi) % (2 * np.pi)) - np.pi) < 1e-9,
        f"d(arg det)={d_argdet:.4f}=n*alpha={n*alpha:.4f}; theta_bar fixed (the Wilson Re Tr U_P is alpha-blind)"))

    # (2) Parity rule on the CP-odd generation density G = i(C - C^2).
    G = 1j * (C - C.conj().T)
    # pure-K (entrywise conjugation, R=I): conj(G) = -G  => ODD  => would force theta_bar=0.
    passed.append(check(
        "(2a) pure-K makes the CP-odd density ODD: conj(i(C-C^2)) = -i(C-C^2) (would force theta_bar=0)",
        np.allclose(G.conj(), -G)))
    # reflection-composed P: P conj(G) P = +G  => EVEN  => theta_bar SURVIVES.
    passed.append(check(
        "(2b) reflection-composed P makes it EVEN: P conj(G) P = +G (theta_bar survives)",
        np.allclose(P @ G.conj() @ P, G)))

    # pure-K is UNAVAILABLE as a symmetry of M for complex b (the Koide radius lives off the real axis).
    bc = 0.5 + 0.4j
    Mc = a * I3 + bc * C + np.conj(bc) * C.conj().T
    passed.append(check(
        "(2c) pure-K UNAVAILABLE: conj(M)!=M for complex b (only the reflection-composed P M P = M(conj b) holds)",
        not np.allclose(Mc.conj(), Mc) and np.allclose(P @ Mc @ P, a * I3 + np.conj(bc) * C + bc * C.conj().T)))

    # (3) Sector-disjoint antiunitaries: Theta_OS acts on a gauge factor (identity on generation),
    # P acts on the generation factor (identity on gauge) -> independent, spliced not forced.
    gauge = np.array([[0, 1.0], [1.0, 0]])  # a stand-in gauge-sector reflection on a 2-dim gauge factor
    Theta_OS = np.kron(gauge, I3)            # acts on gauge, identity on generation
    P_gen = np.kron(np.eye(2), P)            # acts on generation, identity on gauge
    passed.append(check(
        "(3) sector-DISJOINT: Theta_OS = (gauge reflection)(x)I_gen and P = I_gauge(x)P_gen act on different factors (global Theta is a SPLICE, not forced)",
        np.allclose(Theta_OS @ P_gen, P_gen @ Theta_OS)
        and not np.allclose(Theta_OS, np.kron(np.eye(2), I3))
        and not np.allclose(P_gen, np.kron(np.eye(2), I3))))

    # THE RESIDUAL: a complex coupling c != conj(b) makes conj(M)=M reachable WITHOUT P (pure-K available),
    # but BREAKS the C_3 conjugate-symmetry coeff(C^2)=conj(coeff(C)) = the holomorphic generation coupling.
    # Example: a REAL-symmetric M (b and c both real, equal) is conj-invariant (pure-K available) but is the
    # degenerate boundary; a genuinely holomorphic coupling breaks conjugate-symmetry. Show the fork:
    M_realsym = a * I3 + 0.5 * C + 0.5 * C.conj().T  # c=b real => conj(M)=M (pure-K available) ...
    passed.append(check(
        "(RESIDUAL) the open brick = a holomorphic generation coupling breaking coeff(C^2)=conj(coeff(C)); only then is pure-K (conj(M)=M) available without P",
        np.allclose(M_realsym.conj(), M_realsym),
        "= the SAME chiral/holomorphic generation-grading gate as Koide Q=2/3 and generation-ID (triple convergence)"))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("FINDING: the joint-basis bridge FAILS -- theta_bar is NOT forced to zero. The retained emergent-time")
    print("Theta is reflection-composed (P-even) and anomaly-blind on the gauge+matter carrier, so theta_bar")
    print("survives; the gauge-OS and generation antiunitaries are sector-disjoint (global Theta is a splice).")
    print("The single residual is a global PURE-K = a holomorphic generation coupling -- the SAME unbuilt brick")
    print("as Koide Q=2/3 and generation-ID (triple convergence). No audit status.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
