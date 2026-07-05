"""Route-2 q_E pin, follow-on no-go: the covariance bridge lambda = q_E/q_T = kappa^2 = 9/4 is NOT forced
even by a genuinely QUADRATIC O_h-invariant functional -- it remains an OPEN READOUT DATUM (a free
direction in the readout plane). This strengthens the sharper no-go by closing the live
Sym^2 / "quadratic-forces-the-square" mechanism.

CONTEXT. The s3_time_primitive_chain open gate's single missing Route-2 up-sector readout datum is
    c_TE := gamma_T(center)/gamma_E(center) = -8/9
  (equivalently rho_E := beta_E/alpha_E = 21/4 ; q_E := 1 + rho_E/6 = 15/8 ; with the granted T-side
  q_T = 5/6, the covariance lambda := q_E/q_T = 9/4). The standalone positive theorem derives
  the same-domain O_h shell leverage kappa = dim(T1)/dim(E) = 3/2 on the 7-site octahedral star, so the
  VALUE 9/4 = kappa^2 is structurally present; the sharper no-go showed O_h equivariance does
  NOT supply the BRIDGE lambda = kappa^2 (Hom_Oh(E,T1)=0; the A1 center-excess gives the SAME 1/6 increment
  to E and T; positivity leaves the rho_E > -6 continuum). The remaining live derivation hope was that the
  bright observable being QUADRATIC in the metric could make the per-channel response scale as the SQUARE
  of the projector weight. This runner CLOSES that hope and records two corroborating facts.

  This runner records the narrowed route-exercise output; the verdict is that the datum remains open.
  Forbidden-inputs discipline (from the April naturality no-go) respected throughout: no observed quark
  masses, no fitted target, no nearest-rational selection, no live-endpoint selector. The rationals
  5/6, 15/8, -2, -8/9, 9/4, 21/4 appear ONLY as comparison targets.

REPROVEN FROM #3844 (self-contained, so this note does not hard-depend on #3844 landing):
  K1  kappa = 3/2 derived. 6-arm O_h perm rep = A1g (+) Eg (+) T1u multiplicity-free; per-arm projector
      weights (1/6, 1/3, 1/2) = dim/6 (via the antipodal involution A = rho(-I)); kappa = P_T1/P_E = 3/2.
  K3  commutant independence: Hom_Oh(E,T1) = 0 (Reynolds intertwiner = 0).
  K4  endpoint algebra: q_T=5/6, q_E=15/8, lambda=9/4, c_TE=-8/9 exact (granted T-side + readout map).
  K5  the pinning: 9/4 = kappa^2 exactly, but the bridge is not a consequence of K1/K3.

THE NEW CLOSURES (this note's contribution):
  Q1  THE QUADRATIC-ROUTE KILL (Schur). Sym^2(perm6) contains the trivial rep EXACTLY 3 times. Since
      A1g, Eg, T1u are each multiplicity-1, by Schur a general O_h-invariant quadratic form is
          a * ||.||_A1 + b * ||.||_E + c * ||.||_T1   with a, b, c FREE,
      i.e. there are exactly 3 independent invariant quadratic forms and the E:T1 weight ratio b:c is a
      FREE reduced-matrix-element ratio. So even a genuinely quadratic O_h-invariant functional does NOT
      force the covariance to kappa^2; 9/4 is one point on a continuum. (Lambda^2(perm6) trivial mult = 0;
      trivial-in-perm6 = 1 are reported as sanity checks.)
  Q2  THE INVERSE-SQUARE CHARACTERIZATION. lambda = kappa^2 holds iff the per-channel lift scales as the
      INVERSE SQUARE of the channel's OWN per-arm projector weight, q_X ~ w_X^{-2}: (w_E/w_T1)^{-2} = 9/4
      exactly. The most common quadratic/bilinear constructions carry ONE power of the leverage --
      (w_E/w_T1)^{-1} = 3/2 = kappa (not kappa^2), and the Sym^2-diagonal scaling ~ w_X^{+2} gives
      (w_E/w_T1)^{+2} = 4/9 (not 9/4, and on the wrong channel). No named functional produces an
      inverse-square-of-projector-weight center lift. This is the sharpest statement of the gap.
  Q3  THE RATIO BOX-INSTABILITY (recomputed here from the linked box-scan cache; the cited
      q_E(N), q_T(N) are box-scan outputs, the ratio lambda(N) and the spreads are recomputed). lambda(N)
      = q_E(N)/q_T(N) is the LEAST box-stable of the three quantities -- spread(lambda) >> spread(q_E) >>
      spread(q_T) -- and lambda equals 9/4 ONLY at the pinning box N=15. So the "dynamics cancels in the
      ratio" reframing fails: the dynamics AMPLIFIES in the ratio; #3835's no-go is strengthened, not
      reframed away. (Corroboration, not the load-bearing kill, which is Q1.)

VERDICT: open_readout_datum. rho_E = beta_E/alpha_E is a FREE DIRECTION in the (shell, center-excess)
readout plane; equivariance (K3), the channel-blind carrier (K5), positivity, and now the quadratic
invariant (Q1) all leave it free. 21/4 is moreover a nearest-rational over-idealization of a non-rational
live number (box-size scan cache q_E(N=15)=1.876246 -> live rho_E = 6*(q_E-1) ~ 5.26 vs the exact 5.25). This
does NOT prove impossibility over arbitrary
future nonlinear observables (N7); it closes the quadratic-invariant route as a theorem.
"""
from __future__ import annotations
from fractions import Fraction as F
import itertools
import numpy as np
import numpy.linalg as la

PASS = 0
FAIL = 0


def check(label, cond, got=""):
    global PASS, FAIL
    ok = bool(cond)
    PASS += ok
    FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f"\n       {got}" if got else ""))
    return ok


# ---------------------------------------------------------------------------
# The 48 O_h signed-permutation matrices on R^3 and their action on the 6 arms.
# ---------------------------------------------------------------------------
def oh_signed_perms():
    mats = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            M = np.zeros((3, 3), dtype=int)
            for i in range(3):
                M[i, perm[i]] = signs[i]
            mats.append(M)
    return mats


ARMS = [np.array(v) for v in
        [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]]
NEG = {0: 1, 1: 0, 2: 3, 3: 2, 4: 5, 5: 4}


def arm_index(v):
    for k, a in enumerate(ARMS):
        if np.array_equal(v, a):
            return k
    raise ValueError(v)


def perm_of(M):
    return [arm_index(M @ ARMS[k]) for k in range(6)]


def perm_matrix(M):
    P = np.zeros((6, 6))
    p = perm_of(M)
    for k in range(6):
        P[p[k], k] = 1
    return P


def chi_perm(M):                       # permutation character = number of fixed arms
    p = perm_of(M)
    return sum(1 for k in range(6) if p[k] == k)


def main() -> int:
    print("Route-2 q_E covariance bridge: quadratic-route closure (Schur) -- follow-on no-go")
    print("=" * 96)
    G = oh_signed_perms()
    assert len(G) == 48
    order = len(G)

    # --- isotypic projectors via the antipodal involution A = rho(-I) ---------
    Reyn = sum(perm_matrix(M) for M in G) / order            # P_A1 (Reynolds avg)
    A = np.zeros((6, 6))
    for k in range(6):
        A[NEG[k], k] = 1
    P_A1 = Reyn
    P_T1 = (np.eye(6) - A) / 2                                # antipodal-odd  -> T1u
    P_E = (np.eye(6) + A) / 2 - P_A1                          # antipodal-even - A1 -> Eg

    # ---- K1: kappa = 3/2 derived --------------------------------------------
    print("\n-- Reproven from the sharper covariance no-go --")
    ranks = tuple(int(round(np.trace(X))) for X in (P_A1, P_E, P_T1))
    check("K1a ranks (A1g,Eg,T1u) = (1,2,3); multiplicity-free A1g(+)Eg(+)T1u",
          ranks == (1, 2, 3), f"ranks = {ranks}")
    wA1, wE, wT1 = (F(X[0, 0]).limit_denominator() for X in (P_A1, P_E, P_T1))
    check("K1b per-arm projector weights = (1/6, 1/3, 1/2) = dim/6",
          (wA1, wE, wT1) == (F(1, 6), F(1, 3), F(1, 2)), f"(w_A1,w_E,w_T1) = {(wA1, wE, wT1)}")
    kappa = wT1 / wE
    check("K1c kappa = P_T1/P_E = 3/2 ; kappa^2 = 9/4",
          kappa == F(3, 2) and kappa ** 2 == F(9, 4), f"kappa = {kappa}, kappa^2 = {kappa**2}")

    # ---- K3: Hom_Oh(E,T1) = 0 -----------------------------------------------
    rng = np.random.default_rng(0)
    X = rng.standard_normal((6, 6))
    inter = sum(perm_matrix(M) @ X @ perm_matrix(M).T for M in G) / order
    cross = P_T1 @ inter @ P_E
    check("K3  Hom_Oh(E,T1) = 0 (Reynolds intertwiner vanishes -> independent E,T1 scales)",
          la.norm(cross) < 1e-12, f"||P_T1 . <g X g^-1> . P_E|| = {la.norm(cross):.2e}")

    # ---- K4: endpoint algebra (granted T-side + readout map) ----------------
    def q(rho):
        return 1 + F(rho) / 6
    rho_T, rho_E = F(-1), F(21, 4)
    qT, qE = q(rho_T), q(rho_E)
    lam = qE / qT
    cTE = -2 * qT / qE
    check("K4  endpoint: q_T=5/6, q_E=15/8, lambda=q_E/q_T=9/4, c_TE=-2 q_T/q_E=-8/9",
          (qT, qE, lam, cTE) == (F(5, 6), F(15, 8), F(9, 4), F(-8, 9)),
          f"q_T={qT}, q_E={qE}, lambda={lam}, c_TE={cTE}")

    # ---- K5: the pinning 9/4 = kappa^2 (value present; bridge not a consequence)
    check("K5  the pinning: 9/4 = kappa^2 exactly (value present; bridge tested in Q1/Q2)",
          lam == kappa ** 2, f"lambda = {lam} = kappa^2 = {kappa**2}")

    # ---- Q1: THE QUADRATIC-ROUTE KILL (Schur) -------------------------------
    print("\n-- New closures (this note) --")
    # trivial mult in Sym^2(V) = (1/|G|) sum_g [chi(g)^2 + chi(g^2)] / 2
    sym2 = sum(F(chi_perm(M) ** 2 + chi_perm(M @ M), 2) for M in G) / order
    lam2 = sum(F(chi_perm(M) ** 2 - chi_perm(M @ M), 2) for M in G) / order
    trivV = F(sum(chi_perm(M) for M in G), order)
    check("Q1  Sym^2(perm6) trivial mult = 3  ==>  3 FREE invariant quadratics (Schur): E:T1 ratio FREE, "
          "so even a quadratic functional does NOT force lambda = kappa^2",
          sym2 == 3, f"mult_triv[Sym^2(perm6)] = {sym2}")
    check("Q1-sanity  Lambda^2(perm6) trivial mult = 0 ; trivial-in-perm6 = 1 (multiplicity-free)",
          lam2 == 0 and trivV == 1, f"mult_triv[Lambda^2] = {lam2}, mult_triv[V] = {trivV}")

    # ---- Q2: THE INVERSE-SQUARE CHARACTERIZATION ----------------------------
    r = wE / wT1                                             # = 2/3 (E weight / T1 weight)
    check("Q2  lambda = kappa^2  <=>  q_X ~ w_X^{-2}: (w_E/w_T1)^{-2} = 9/4 (the bridge); "
          "(w_E/w_T1)^{-1} = 3/2 = kappa (one power, not the square); (w_E/w_T1)^{+2} = 4/9 (wrong)",
          r ** -2 == F(9, 4) and r ** -1 == F(3, 2) and r ** 2 == F(4, 9),
          f"(w_E/w_T1)^-2 = {r**-2}, ^-1 = {r**-1}, ^+2 = {r**2}")

    # ---- Q3: THE RATIO BOX-INSTABILITY (recomputed from the linked box-size scan cache)
    # cited inputs (box-scan cache outputs); the ratio + spreads are recomputed here.
    N3835 = [13, 15, 17, 19, 21, 25]
    qT_N = [0.87009, 0.83333, -0.19680, -0.81228, -1.31647, -2.08540]
    qE_N = [-0.03887, 1.87625, -5.83700, -7.45520, -8.67461, -10.37720]
    lam_N = [e / t for e, t in zip(qE_N, qT_N)]
    spread = lambda a: max(a) - min(a)
    s_lam, s_qE, s_qT = spread(lam_N), spread(qE_N), spread(qT_N)
    at15 = abs(lam_N[N3835.index(15)] - 2.25)
    bulk_min = min(abs(lam_N[i] - 2.25) for i, n in enumerate(N3835) if n != 15)
    check("Q3a lambda(N) is the LEAST box-stable: spread(lambda) >> spread(q_E) >> spread(q_T)",
          s_lam > s_qE > s_qT,
          f"spread(lambda)={s_lam:.2f}, spread(q_E)={s_qE:.2f}, spread(q_T)={s_qT:.2f}")
    check("Q3b lambda = 9/4 ONLY at the pinning box N=15 (bulk boxes are far from 9/4)",
          at15 < 0.01 and bulk_min > 1.0,
          f"|lambda(15)-9/4|={at15:.4f}; min bulk |lambda-9/4|={bulk_min:.2f}; "
          f"lambda(N)={[round(x,2) for x in lam_N]}")

    print("\n" + "=" * 96)
    print(f"PASS={PASS} FAIL={FAIL}")
    print(
        "\nVERDICT: open_readout_datum. The VALUE 9/4 = kappa^2 is a same-domain O_h theorem output\n"
        "(K1), but the BRIDGE lambda = q_E/q_T = kappa^2 is forced by NOTHING named: equivariance leaves\n"
        "E,T1 scales independent (K3), the carrier is channel-blind (K5), and now (Q1) even a quadratic\n"
        "O_h-invariant functional has a FREE E:T1 ratio by Schur -- kappa^2 is one point on a continuum.\n"
        "The gap is exactly q_X ~ w_X^{-2} (Q2), realized by no named functional; the live box-scan ratio\n"
        "is the LEAST box-stable quantity (Q3). rho_E = beta_E/alpha_E is a FREE DIRECTION in the readout\n"
        "plane: an open supplied datum, not adopted here. (Does NOT prove impossibility over future nonlinear observables.)"
    )
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
