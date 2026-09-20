#!/usr/bin/env python3
"""moving-kernel-with-vacancies, attempt 2 of 4: the lattice condition, proved - for the
two-valued menu, and not for the sphere.

Provenance: both prior attempts on this problem are BY ME, same model family, machine and running
worker, both finished within the hour: a3 (w-jonathonsmac4f50-jb416) derived the infrared bound
with the bond density rho_2 and hit a half-filling floor; a4 (w-jonathonsmac4f50-jb1d8) checked
the FKG lattice condition exhaustively on four small instances and removed the floor, listing as
its item 1 "prove the lattice condition for mu(A) proportional to z^|A| Z_A".  That is this
attempt.  I re-run neither route; I prove the statement a4 could only check, and then find where
the proof stops - which is exactly at the menu the unit actually asks about.

  P1  the site count is modular, the edge set supermodular            exact
  P2  the coupling vector: J(A n B) = J(A) ^ J(B) exactly             exact
  P3  Griffiths' second inequality, checked on every edge pair        exact
  P4  the assembled proof of the lattice condition
  P5  where it stops: the sphere menu is NOT covered
"""
import sys
from itertools import product
from fractions import Fraction as F

def ring(n):
    return [(i,) for i in range(n)], [((i,), ((i + 1) % n,)) for i in range(n)]

def torus2(L):
    sites = [(i, j) for i in range(L) for j in range(L)]
    bonds = []
    for (i, j) in sites:
        bonds.append(((i, j), ((i + 1) % L, j)))
        bonds.append(((i, j), (i, (j + 1) % L)))
    return sites, bonds

def E(A, bonds):
    A = set(A)
    return {e for e in bonds if e[0] in A and e[1] in A}

def ising(sites, bonds, ws):
    """Z and the correlations <sigma_e> and <sigma_e sigma_f> for edge variables sigma_e =
    sigma_x sigma_y, with per-edge weights ws[e] (a Fraction w_e = e^{J_e})."""
    idx = {x: n for n, x in enumerate(sites)}
    Z = F(0)
    se = {e: F(0) for e in bonds}
    sef = {(e, f): F(0) for e in bonds for f in bonds}
    for cfg in product([1, -1], repeat=len(sites)):
        wt = F(1)
        sig = {}
        for e in bonds:
            s = cfg[idx[e[0]]]*cfg[idx[e[1]]]
            sig[e] = s
            wt *= ws[e] if s == 1 else 1/ws[e]
        Z += wt
        for e in bonds:
            se[e] += wt*sig[e]
        for e in bonds:
            for f in bonds:
                sef[(e, f)] += wt*sig[e]*sig[f]
    return Z, {e: se[e]/Z for e in bonds}, {k: sef[k]/Z for k in sef}

def main():
    ok = True
    def want(cond, msg):
        nonlocal ok
        print(("ok   " if cond else "FAIL ") + msg)
        ok = ok and bool(cond)

    print("P1  the two set functions in mu(A) = z^|A| Z_A")
    print("     mu(A) = z^|A| Z_A, so log mu = |A| log z + log Z_A.  The site count is MODULAR:")
    print("       |A u B| + |A n B| = |A| + |B|   exactly, so the fugacity contributes nothing to")
    print("     the lattice condition either way.  The edge set is SUPERMODULAR:")
    print("       E(A) u E(B) is contained in E(A u B), and E(A) n E(B) = E(A n B),")
    print("     the second because an edge with both ends in A and both ends in B has both ends")
    print("     in A n B.  Checked by enumeration:")
    for (nm, (ss, bb)) in [("ring of 6", ring(6)), ("3x3 torus", torus2(3))]:
        N = len(ss)
        badc = bade = badi = 0
        for ma in range(1 << N):
            A = {ss[i] for i in range(N) if ma >> i & 1}
            for mb in range(1 << N):
                B = {ss[i] for i in range(N) if mb >> i & 1}
                if len(A | B) + len(A & B) != len(A) + len(B):
                    badc += 1
                if not (E(A, bb) | E(B, bb)) <= E(A | B, bb):
                    bade += 1
                if E(A, bb) & E(B, bb) != E(A & B, bb):
                    badi += 1
        want(badc == 0 and bade == 0 and badi == 0,
             f"     {nm}: over all {(1 << N)**2} ordered pairs - {badc} count failures, "
             f"{bade} union failures, {badi} intersection failures")
    ss, bb = ring(4)
    A = {(0,), (1,)}; B = {(2,), (3,)}
    want(E(A | B, bb) > (E(A, bb) | E(B, bb)),
         f"     and the union can be STRICT: on a ring of 4, E(A u B) has "
         f"{len(E(A | B, bb))} edges against {len(E(A, bb) | E(B, bb))} in E(A) u E(B)")

    print("\nP2  the coupling vector")
    print("     Write J(A)_e = beta if e is inside A and 0 otherwise, so that Z_A is the Ising")
    print("     partition function at couplings J(A), times 2 for every site outside A.  Then P1")
    print("     says exactly")
    print("       J(A n B) = J(A) ^ J(B)        (componentwise minimum), and")
    print("       J(A u B) >= J(A) v J(B)       (componentwise maximum), sometimes strictly.")
    for (nm, (ss2, bb2)) in [("ring of 6", ring(6)), ("3x3 torus", torus2(3))]:
        N = len(ss2)
        bad = 0
        for ma in range(1 << N):
            A = {ss2[i] for i in range(N) if ma >> i & 1}
            for mb in range(1 << N):
                B = {ss2[i] for i in range(N) if mb >> i & 1}
                ea, eb = E(A, bb2), E(B, bb2)
                if E(A & B, bb2) != (ea & eb) or not (ea | eb) <= E(A | B, bb2):
                    bad += 1
        want(bad == 0, f"     {nm}: both hold over all {(1 << N)**2} ordered pairs ({bad} failures)")

    print("\nP3  Griffiths' second inequality, on this model, checked exactly")
    print("     ASSUMED as a theorem for the ferromagnetic Ising model: for J >= 0,")
    print("       d^2 log Z / dJ_e dJ_f  =  <sigma_e sigma_f> - <sigma_e><sigma_f>  >=  0,")
    print("     i.e. log Z is SUPERMODULAR in the coupling vector, and dlog Z/dJ_e = <sigma_e>")
    print("     >= 0 makes it increasing.  Verified here on every ordered pair of edges:")
    for (nm, (ss3, bb3), wv) in [("ring of 5", ring(5), F(2)),
                                 ("ring of 6", ring(6), F(3)),
                                 ("2x2 torus", torus2(2), F(2))]:
        ws = {e: wv for e in bb3}
        Z, se, sef = ising(ss3, bb3, ws)
        neg = [(e, f) for e in bb3 for f in bb3 if sef[(e, f)] - se[e]*se[f] < 0]
        negm = [e for e in bb3 if se[e] < 0]
        want(not neg and not negm,
             f"     {nm} at w = {wv}: all {len(bb3)**2} pairs have "
             f"<s_e s_f> - <s_e><s_f> >= 0, and all {len(bb3)} have <s_e> >= 0")
    print("     (the 2x2 torus has doubled bonds; it is included because the doubling is exactly")
    print("     the degenerate case where a naive proof would be tempted to divide by zero)")

    print("\nP4  the lattice condition, assembled")
    print("     log mu(A) = |A| log z + log Z_A, and Z_A = 2^{N - |A|} Zising(J(A)).  Then")
    print("       log mu(A u B) + log mu(A n B)")
    print("         = (|A u B| + |A n B|) log z + (2N - |A| - |B|) log 2")
    print("           + log Zising(J(A u B)) + log Zising(J(A n B))       [P1: counts are modular]")
    print("         >= ... + log Zising(J(A) v J(B)) + log Zising(J(A) ^ J(B))")
    print("                                                    [P2 and Zising increasing in J]")
    print("         >= ... + log Zising(J(A)) + log Zising(J(B))         [P3: supermodularity]")
    print("         = log mu(A) + log mu(B).")
    print("     So mu is log-supermodular: the FKG lattice condition HOLDS, for every graph and")
    print("     every z > 0 and beta >= 0.  a4 checked this on four instances; it is a theorem.")
    print("     Re-verified on one instance not in a4's list:")
    ss4, bb4 = ring(5)
    z, w = F(3, 2), F(2)
    N = len(ss4)
    mu = {}
    for ma in range(1 << N):
        A = {ss4[i] for i in range(N) if ma >> i & 1}
        lst = sorted(A)
        idx = {x: n for n, x in enumerate(lst)}
        tot = F(0)
        for cfg in product([1, -1], repeat=len(lst)):
            wt = F(1)
            for e in E(A, bb4):
                wt *= w if cfg[idx[e[0]]] == cfg[idx[e[1]]] else 1/w
            tot += wt
        mu[ma] = (z**len(A))*tot
    bad = sum(1 for a in range(1 << N) for b in range(1 << N)
              if mu[a | b]*mu[a & b] < mu[a]*mu[b])
    want(bad == 0, f"     ring of 5, z = {z}, w = {w}: {(1 << N)**2} ordered pairs, {bad} failures")

    print("\nP5  where the proof stops - and it stops at the menu the unit asks about")
    print("     Step P3 is Griffiths' SECOND inequality.  It is a theorem for the Ising model -")
    print("     the two-valued menu of block 36's runner - and for a few other single-site")
    print("     measures, but it is NOT available in general for vector spins: for the O(3)")
    print("     model, which is the SPHERE menu this unit is about, the second Griffiths")
    print("     inequality is not known and is believed false in general.  Everything else in P4")
    print("     is menu-independent: P1 and P2 are pure set combinatorics, and the monotonicity")
    print("     of Z in the couplings holds for any ferromagnetic menu.  So:")
    print("       two-valued menu:  rho_2 >= rho^2 is a THEOREM (modulo GKS-II and FKG);")
    print("       sphere menu:      rho_2 >= rho^2 rests on a4's numerical evidence alone,")
    print("                         and the one missing ingredient is named.")
    print("     How far past Ising does the GKS-II step survive?  Checked for a q-state menu")
    print("     (weight w if the two contents agree, 1 if they differ), with the centred edge")
    print("     variable sigma_e = 1[agree] - 1/q, on a ring of 5:")
    for q in (2, 3, 4, 6):
        ss5, bb5 = ring(5)
        idx5 = {x: n for n, x in enumerate(ss5)}
        wv = F(2)
        Z5 = F(0); se5 = {e: F(0) for e in bb5}
        sef5 = {(e, f): F(0) for e in bb5 for f in bb5}
        for cfg in product(range(q), repeat=len(ss5)):
            wt = F(1); sig = {}
            for e in bb5:
                ag = cfg[idx5[e[0]]] == cfg[idx5[e[1]]]
                sig[e] = (1 if ag else 0) - F(1, q)
                wt *= wv if ag else 1
            Z5 += wt
            for e in bb5:
                se5[e] += wt*sig[e]
                for f in bb5:
                    sef5[(e, f)] += wt*sig[e]*sig[f]
        neg = [(e, f) for e in bb5 for f in bb5
               if sef5[(e, f)]/Z5 - (se5[e]/Z5)*(se5[f]/Z5) < 0]
        want(not neg,
             f"       q = {q}: all {len(bb5)**2} edge pairs have non-negative covariance "
             f"({len(neg)} negative)")
    print("     So the inequality itself survives every finite menu tested - which says the")
    print("     obstruction for the sphere is about the CONTINUUM limit and the absence of a")
    print("     proof there, not about a counterexample at small q.  That is the honest state:")
    print("     a4's headline extends to the unit's own menu only")
    print("       if a GKS-II analogue holds for the sphere, which is a real open question and")
    print("       not a gap in the bookkeeping.")

    print()
    if ok:
        print("SUMMARY: PARTIAL - the FKG lattice condition for the occupation marginal "
              "mu(A) = z^|A| Z_A of the law with vacancies is PROVED for the two-valued menu, "
              "modulo Griffiths' second inequality: the site count is modular and the edge set "
              "supermodular with E(A n B) = E(A) n E(B) and E(A) u E(B) contained in E(A u B) "
              "(both verified over all ordered pairs of subsets of a ring of 6 and a 3x3 torus), "
              "so the coupling vectors satisfy J(A n B) = J(A) ^ J(B) and J(A u B) >= J(A) v "
              "J(B); since log Z is increasing and supermodular in the couplings - the latter "
              "being GKS-II, checked here on every ordered pair of edges of three small graphs - "
              "log mu is supermodular, which upgrades attempt a4's four exhaustive instance "
              "checks to a theorem for every graph, every z > 0 and every beta >= 0; but GKS-II "
              "is an Ising theorem and is not available for O(3) spins, so for the SPHERE menu "
              "that this unit is actually about, rho_2 >= rho^2 still rests on a4's numerics")
        print("HIT: the lattice condition behind rho_2 >= rho^2 factors into three pieces - "
              "modularity of the site count, supermodularity of the edge set with E(A n B) = "
              "E(A) n E(B) exactly, and supermodularity of log Z in the couplings - of which only "
              "the third carries any physics, and it is exactly Griffiths' second inequality; "
              "this proves attempt a4's checked hypothesis for the two-valued menu at every "
              "graph, fugacity and coupling, and simultaneously locates the obstruction for the "
              "sphere menu the unit asks about, where GKS-II is not available for vector spins - "
              "so the half-filling floor is provably removable for the two-valued menu and only "
              "numerically removable for the sphere")
        return 0
    print("SUMMARY: ROUTE FAILS AT one of the checks above")
    return 1

if __name__ == "__main__":
    sys.exit(main())
