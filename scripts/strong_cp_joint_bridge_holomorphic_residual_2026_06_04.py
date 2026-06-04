#!/usr/bin/env python3
"""Strong-CP joint-basis bridge check.

The tested bridge does not force theta_bar = theta_QCD + arg det M to zero.
The finite checks separate gauge-side reflection from generation-side parity,
show that the tested generation density is odd under pure entrywise K but even
under reflection-composed P, and keep holomorphic/generation residual language
as an open lead rather than a proved multi-gate identification.

Verified structural facts:
 (1) theta_bar is the anomaly-INVARIANT: axial rotation M->e^{i alpha}M shifts arg det M by +n*alpha and
     (Fujikawa) theta_QCD by -n*alpha, so theta_bar is fixed; the Wilson gauge measure is alpha-invariant
     (anomaly-blind: the two reality conditions do not co-move).
 (2) Parity rule Theta(iQ)Theta^-1 = -i(R Q R): pure-K (R=I) makes the tested generation density
     G=i(C-C^2) ODD (conj(G)=-G), while reflection-composed P makes it EVEN
     (P conj(G) P = +G). Pure-K is UNAVAILABLE in the tested non-real-b class: conj(M)!=M.
 (3) Residual marker: pure-K would require changing the generation coupling
     class; this runner does not derive that structure.

Sets no audit status; independent audit lane owns status.
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

    # (1) theta_bar is anomaly-invariant in the paired-shift bookkeeping.
    a, b = 1.3, 0.5  # real b => M Hermitian, arg det M = 0
    M = a * I3 + b * (C + C.conj().T)
    alpha = 0.37
    Mrot = np.exp(1j * alpha) * M
    d_argdet = np.angle(np.linalg.det(Mrot)) - np.angle(np.linalg.det(M))
    theta_qcd = 1.1
    theta_bar_before = theta_qcd + np.angle(np.linalg.det(M))
    theta_bar_after = (theta_qcd - n * alpha) + np.angle(np.linalg.det(Mrot))   # Fujikawa shift
    passed.append(check(
        "(1) theta_bar anomaly-invariant bookkeeping: arg det M shifts by +n*alpha and theta_QCD by -n*alpha",
        abs(((d_argdet - n * alpha + np.pi) % (2 * np.pi)) - np.pi) < 1e-9
        and abs(((theta_bar_after - theta_bar_before + np.pi) % (2 * np.pi)) - np.pi) < 1e-9,
        f"d(arg det)={d_argdet:.4f}=n*alpha={n*alpha:.4f}; theta_bar fixed under paired shifts"))

    # (2) Parity rule on the CP-odd generation density G = i(C - C^2).
    G = 1j * (C - C.conj().T)
    # pure-K (entrywise conjugation, R=I): conj(G) = -G, so the tested density is odd.
    passed.append(check(
        "(2a) pure-K makes the tested density ODD: conj(i(C-C^2)) = -i(C-C^2)",
        np.allclose(G.conj(), -G)))
    # reflection-composed P: P conj(G) P = +G, so this parity does not force zero.
    passed.append(check(
        "(2b) reflection-composed P makes it EVEN: P conj(G) P = +G",
        np.allclose(P @ G.conj() @ P, G)))

    # pure-K is unavailable as a symmetry of M for non-real b in this Hermitian circulant class.
    bc = 0.5 + 0.4j
    Mc = a * I3 + bc * C + np.conj(bc) * C.conj().T
    passed.append(check(
        "(2c) pure-K unavailable for non-real b in this Hermitian circulant class; P maps b to conj(b)",
        not np.allclose(Mc.conj(), Mc) and np.allclose(P @ Mc @ P, a * I3 + np.conj(bc) * C + bc * C.conj().T)))

    # (3) Sector-disjoint antiunitaries: Theta_OS acts on a gauge factor (identity on generation),
    # P acts on the generation factor (identity on gauge) -> independent, spliced not forced.
    gauge = np.array([[0, 1.0], [1.0, 0]])  # a stand-in gauge-sector reflection on a 2-dim gauge factor
    Theta_OS = np.kron(gauge, I3)            # acts on gauge, identity on generation
    P_gen = np.kron(np.eye(2), P)            # acts on generation, identity on gauge
    passed.append(check(
        "(3) sector-disjoint: gauge reflection and generation parity act on different factors",
        np.allclose(Theta_OS @ P_gen, P_gen @ Theta_OS)
        and not np.allclose(Theta_OS, np.kron(np.eye(2), I3))
        and not np.allclose(P_gen, np.kron(np.eye(2), I3))))

    # Residual marker: restoring pure-K requires changing the coupling class or landing
    # on a real boundary; the current complex-b Hermitian class does not supply it.
    M_realsym = a * I3 + 0.5 * C + 0.5 * C.conj().T  # c=b real => conj(M)=M (pure-K available) ...
    passed.append(check(
        "(4) residual marker: pure-K is available only after changing the coupling class or landing on a real boundary",
        np.allclose(M_realsym.conj(), M_realsym) and not np.allclose(Mc.conj(), Mc),
        "current non-real-b Hermitian class needs the reflection-composed P relation"))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("FINDING: the tested joint-basis bridge does not force theta_bar to zero.")
    print("Gauge reflection and generation parity are sector-disjoint in this model;")
    print("the generation density is odd under pure K but even under reflection-composed P;")
    print("and theta_bar is invariant under the paired anomaly bookkeeping shifts.")
    print("A holomorphic/chiral generation structure remains an open residual lead,")
    print("not a theorem established by this runner. No audit status.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
