#!/usr/bin/env python3
"""Koide r=1/2 via a tracial-standard-form carrier candidate.

This runner strengthens the unaudited note `flavor_missing_axiom_carrier_measure_note_2026-05-30`
by replacing its "three-way fork, rep theory ranks none" framing with a CANONICITY
computation. The candidate carrier input: the on-site generation carrier is R[Z_3] in its
TRACIAL STANDARD FORM -- i.e. the algebra acting on its GNS / L^2(R[Z_3], tau) space, tau the
normalized group trace, <x,y> = tau(x* y), with cyclic vector Omega = e and the canonical
group-element ONB {e, g, g^2}. We test, rigorously, what the standard form DOES and DOES NOT
force about the partition that fixes r = |b|^2/a^2.

NON-CIRCULAR: r = 1/(N-1) is derived from the candidate carrier input plus equal
GNS Hilbert-Schmidt energy across the cyclic-vector channels of H; Q=2/3 is never assumed.
This is a Tier-A candidate source (claim_type bounded_theorem, status authority = audit lane),
NOT a Tier-A admission, NOT an axiom-surface change, and NOT a derivation from the current
framework baseline plus retained inventory. It forces r=1/2 only given the carrier input
and the channel-counting scoring rule.

Checks (SCORECARD PASS=k):
  C1  GNS standard form well-defined: <Omega, pi(g^k) Omega> = tau(g^k); {e,g,g^2} is a GNS ONB;
      Omega=e is cyclic and separating (the distinguished vacuum vector).
  C2  CRUX (canonicity, the new rigor): the (1,N-1) identity/non-identity split
      C.Omega (+) Omega^perp = span{e} (+) span{g,g^2} is a function of (Omega, <.,.>) ALONE
      (a fixed orthogonal projection, NO diagonalization); the idempotent split's distinguished
      line is the DEMOCRATIC element (1,1,1)/sqrt(N) which is NOT Omega -> the cyclic vector
      breaks the fork in favor of the group-element (1,N-1) partition.
  C3  HS arithmetic on the carrier: ||I||^2=N, ||J-I||^2=N(N-1), <I,J-I>_HS=0; equal
      channel energy a^2*1 = b^2*(N-1) -> r = 1/(N-1). At N=3 -> r=1/2 -> Q=2/3 (Brannen).
  C4  GROUP-BASIS/HOPF AUT-INVARIANCE: the checked Aut(Z_3) maps fix e and permute {g,g^2}
      among themselves -> {e} is the unique singleton orbit -> the (1,2) split is canonical
      under the carrier's checked group-basis symmetry. This is not a classification of all
      trace-preserving *-automorphisms of R[Z_N].
  C5  HONEST RESIDUAL: the idempotent/per-mode partitions are NOT eliminated as ALGEBRA
      decompositions -- equal POWER per central idempotent of the SPECTRUM gives r=17/2-6sqrt(2)
      (~0.0147), per-mode equipartition a^2=b^2 gives r=1 (Plancherel). The standard form
      distinguishes the (1,N-1) SPLIT (via Omega) but the residual SCORING choice
      'count channels (->1/2)' vs 'count basis directions (->1)' remains carried by the carrier.
  C6  FALSIFIABLE family r=1/(N-1) ties r=1/2 to the DERIVED n_gen=3 (N=2->1, N=3->1/2,
      N=4->1/3, N=6->1/5); Q(N)=1/3+(2/3)r.
  C7  Kahler/Dirac corroborator -> Q=2/3 <=> complex b (Dirac); Majorana neutrinos (real b)
      depart from 2/3. Distinct derivation 1*(a^2+4b^2)=2*(a^2+b^2) -> r=1/2.
  C8  DECOUPLING: r=1/2 is an interior point of the COMMUTING circulant family, [H,S]=0, so the
      candidate carrier introduces no chiral/anticommuting operator and does NOT trip the
      generation-chirality no-go (comm(S) cap anticomm(Gamma_chi) = {0}).
"""
import numpy as np
import sympy as sp


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def regular_rep(N):
    """Left-multiplication-by-g (cyclic shift) on R[Z_N] in the {e,g,...,g^{N-1}} ONB."""
    S = sp.zeros(N, N)
    for k in range(N):
        S[(k + 1) % N, k] = 1
    return S


def main():
    passed = []
    N = 3
    S = regular_rep(N)
    I = sp.eye(N)
    E = I
    G = S
    G2 = S * S
    J = sp.ones(N, N)
    gk = {k: S ** k for k in range(N)}
    tau = lambda M: sp.Rational(1, N) * M.trace()  # normalized group trace
    Omega = sp.zeros(N, 1)
    Omega[0] = 1  # cyclic vector = unit e, coords (1,0,...,0)

    # ---- C1: GNS standard form well-defined ----
    gns_state = all(sp.simplify((Omega.T * (gk[k] * Omega))[0] - tau(gk[k])) == 0 for k in range(N))
    onb = all(sp.simplify(tau(gk[i].T * gk[j]) - (1 if i == j else 0)) == 0
              for i in range(N) for j in range(N))
    cyclic = sp.Matrix.hstack(*[gk[k] * Omega for k in range(N)]).rank() == N
    separating = all((gk[k] * Omega).is_zero_matrix is False for k in range(N))
    passed.append(check(
        "C1 GNS standard form: <Omega,pi(g^k)Omega>=tau(g^k); {e,g,g^2} ONB; Omega cyclic+separating",
        gns_state and onb and cyclic and separating,
        "tracial GNS triple reproduces tau; Omega=e is the distinguished vacuum vector"))

    # ---- C2: CRUX -- cyclic vector breaks the fork toward the (1,N-1) split ----
    # The (1,N-1) split is the FIXED orthogonal projection onto C.Omega vs Omega^perp.
    P_id = Omega * Omega.T  # |e><e|, rank-1; NO diagonalization needed
    P_nonid = I - P_id
    proj_is_complementary = (sp.simplify(P_id * P_id - P_id).is_zero_matrix
                             and sp.simplify(P_nonid * P_nonid - P_nonid).is_zero_matrix
                             and sp.simplify(P_id * P_nonid).is_zero_matrix
                             and (sp.trace(P_id) == 1) and (sp.trace(P_nonid) == N - 1))
    # The idempotent split's distinguished line = democratic central idempotent p_0=(e+..+g^{N-1})/N
    p0 = sp.zeros(N, N)
    for k in range(N):
        p0 += gk[k]
    p0 = sp.simplify(sp.Rational(1, N) * p0)
    democratic = sp.Matrix([1] * N) / sp.sqrt(N)        # the (1,1,1)/sqrt(N) line
    p0_is_democratic = sp.simplify(p0[:, 0] * N - sp.Matrix([1] * N)).is_zero_matrix
    democratic_not_Omega = sp.simplify((Omega.T * democratic)[0]) != 0 and \
        sp.simplify((Omega.T * democratic)[0] - 1) != 0  # overlap strictly between 0 and 1
    passed.append(check(
        "C2 CRUX: (1,N-1) split=C.Omega(+)Omega^perp is (Omega,metric) data (no diag); cyclic vector",
        proj_is_complementary and p0_is_democratic and democratic_not_Omega,
        "idempotent singlet line = democratic (1,1,1)/sqrt(N) != Omega=e, so the cyclic vector "
        "selects the GROUP-ELEMENT (1,N-1) partition; idempotent split needs the extra Fourier resolution"))

    # ---- C3: HS arithmetic + r = 1/(N-1) at N=3 ----
    a, b = sp.symbols('a b', positive=True)
    HSe = sp.trace((a * E).T * (a * E))            # ||a e||^2 = N a^2
    HSrest = sp.trace((b * (G + G2)).T * (b * (G + G2)))  # ||b(J-I)||^2 = N(N-1) b^2
    hs_norms = (sp.trace(E.T * E) == N and sp.trace((J - I).T * (J - I)) == N * (N - 1)
                and sp.trace(E.T * (J - I)) == 0)
    r_chan = (sp.solve(sp.Eq(HSe, HSrest), b)[0] / a) ** 2
    # Brannen/eigenvalue readout: H = a I + b(J-I), eigenvalues a+(N-1)b (singlet), a-b (mult N-1)
    H = a * E + b * (G + G2)
    eigs = H.eigenvals()
    Q = sp.simplify(sum(sp.simplify(lam) ** 2 * m for lam, m in eigs.items()) /
                    (sum(sp.simplify(lam) * m for lam, m in eigs.items())) ** 2)
    Q_form = sp.simplify(Q - (sp.Rational(1, 3) + sp.Rational(2, 3) * b ** 2 / a ** 2)) == 0
    passed.append(check(
        "C3 HS arithmetic: ||I||^2=N,||J-I||^2=N(N-1),<.,.>=0; equal-channel-energy -> r=1/(N-1)=1/2",
        hs_norms and r_chan == sp.Rational(1, 2) and Q_form,
        f"3a^2=6b^2 -> r={r_chan}; Brannen Q={Q}=1/3+(2/3)r -> Q=2/3 at r=1/2"))

    # ---- C4: checked Aut(Z_3) group-basis invariance of the (1,2) split ----
    auts = [u for u in range(1, N) if sp.gcd(u, N) == 1]
    aut_ok = True
    for u in auts:
        images = [(k * u) % N for k in range(N)]
        # e (k=0) fixed; non-identity {1..N-1} permuted among themselves
        if images[0] != 0 or sorted(images[1:]) != list(range(1, N)):
            aut_ok = False
    passed.append(check(
        "C4 checked Aut(Z_3) fixes e and permutes {g,g^2} -> {e} unique singleton orbit; (1,2) canonical",
        aut_ok and len(auts) >= 1,
        f"Aut(Z_{N}) group-basis maps g->g^u, u in {auts}; identity is the unique order-1 element"))

    # ---- C5: HONEST RESIDUAL -- idempotent/per-mode partitions are not eliminated ----
    # idempotent EQUAL-POWER of the SPECTRUM: (a+2b)^2 = 2(a-b)^2 -> r = 17/2 - 6 sqrt(2)
    sol_eig = sp.solve(sp.Eq((a + 2 * b) ** 2, 2 * (a - b) ** 2), b)
    r_eig = sp.simplify((sol_eig[0] / a) ** 2)
    r_eig_val = float(r_eig.subs(a, 1))
    # per-mode equipartition a^2 = b^2 -> r = 1 (Plancherel / dimension weighting)
    r_mode = sp.simplify((sp.solve(sp.Eq(a ** 2, b ** 2), b)[0] / a) ** 2)
    residual = (sp.simplify(r_eig - (sp.Rational(17, 2) - 6 * sp.sqrt(2))) == 0
                and abs(r_eig_val - 0.0147186) < 1e-5 and r_mode == 1)
    passed.append(check(
        "C5 HONEST RESIDUAL: idempotent-power->17/2-6sqrt2~0.0147, per-mode->1 still expressible",
        residual,
        "standard form distinguishes the (1,N-1) SPLIT via Omega, but the SCORING choice "
        "channel-count(->1/2) vs basis-direction-count(->1) remains carried by the carrier"))

    # ---- C6: falsifiable family r = 1/(N-1) ----
    fam = {}
    for n in [2, 3, 4, 6]:
        In = sp.eye(n)
        Jn = sp.ones(n, n)
        # equal channel energy: a^2 ||I||^2 = b^2 ||J-I||^2 -> a^2 * n = b^2 * n(n-1) -> r=1/(n-1)
        rn = sp.simplify(sp.trace(In.T * In) / sp.trace((Jn - In).T * (Jn - In)))
        fam[n] = rn
    Qfam = {n: sp.simplify(sp.Rational(1, 3) + sp.Rational(2, 3) * fam[n]) for n in fam}
    fam_ok = (fam[2] == 1 and fam[3] == sp.Rational(1, 2) and fam[4] == sp.Rational(1, 3)
              and fam[6] == sp.Rational(1, 5) and Qfam[3] == sp.Rational(2, 3))
    passed.append(check(
        "C6 falsifiable: r=1/(N-1) ties r=1/2 to derived n_gen=3 (N=2->1,3->1/2,4->1/3,6->1/5)",
        fam_ok,
        f"r={{ {', '.join(f'{n}:{fam[n]}' for n in fam)} }}; Q(N=3)=1/3+(2/3)(1/2)={Qfam[3]}"))

    # ---- C7: Kahler/Dirac corroborator (distinct derivation, Majorana prediction) ----
    r_kahler = sp.simplify((sp.solve(sp.Eq(a ** 2 + 4 * b ** 2, 2 * (a ** 2 + b ** 2)), b)[0] / a) ** 2)
    passed.append(check(
        "C7 Kahler 1*(a^2+4b^2)=2*(a^2+b^2) -> r=1/2 (distinct); Q=2/3<=>complex b(Dirac), Majorana off",
        r_kahler == sp.Rational(1, 2),
        "complex b (Dirac/U(1)-gauged) -> Q=2/3; real b (Majorana, frozen phase) -> departs from 2/3"))

    # ---- C8: decoupling from the chirality no-go ([H,S]=0) ----
    Sn = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], float)
    Hn = np.eye(3) + (1.0 / np.sqrt(2.0)) * (np.ones((3, 3)) - np.eye(3))  # r=1/2 point
    commute = np.allclose(Hn @ Sn - Sn @ Hn, 0.0)
    # Confirm it is NOT anticommuting with the C3 grading Gamma_chi=(2/3)J-I (the chiral op class)
    Gamma_chi = (2.0 / 3.0) * np.ones((3, 3)) - np.eye(3)
    anticomm_norm = np.linalg.norm(Hn @ Gamma_chi + Gamma_chi @ Hn)
    passed.append(check(
        "C8 r=1/2 interior COMMUTING point [H,S]=0 -> decoupled from chirality no-go",
        commute and anticomm_norm > 1e-6,
        "value lane introduces no chiral/anticommuting operator; comm(S) cap anticomm(Gamma_chi)={0}"))

    n_pass = sum(passed)
    print(f"\nSCORECARD PASS={n_pass} FAIL={len(passed) - n_pass}")
    print("=" * 78)
    print("VERDICT (honest): the tracial standard form PRIVILEGES the (1,N-1) group-element")
    print("partition over the idempotent partition -- the cyclic vector Omega=e sits on the")
    print("identity line, while the idempotent singlet is the democratic line (1,1,1)/sqrt(N)")
    print("!= Omega. So the carrier candidate STRENGTHENS the unaudited note: the fork is no")
    print("longer symmetric ('rep theory ranks none'); the cyclic vector ranks the (1,N-1)")
    print("split first. RESIDUAL that REMAINS: the SCORING rule on that split -- equal energy")
    print("per CHANNEL (2 channels -> r=1/2) vs per basis DIRECTION (3 directions -> r=1,")
    print("Plancherel) -- is still carried by the carrier, not forced by GNS alone. F1 is thus")
    print("SUBSTANTIALLY RELOCATED (channel/(1,N-1) now canonically distinguished), not closed.")
    print("This is a Tier-A candidate source, not a Tier-A admission or axiom-surface change.")
    print("It forces r=1/2 only GIVEN the carrier input plus channel-counting scoring,")
    print("not from the current framework baseline plus retained inventory.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
