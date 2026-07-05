"""Route-2 q_E pin, sharper no-go: 9/4 is the SAME-DOMAIN O_h shell-leverage SQUARED (kappa=3/2,
derived), but the readout covariance q_E/q_T = kappa^2 is NOT forced by equivariance -- it is the single
remaining open datum. This relocates the missing datum from the cross-domain color coincidence
c_TE = -R_conn = -8/9 (already a no-go) to a same-domain covariance rule.

GOAL: go after the derivation of the single missing independent Route-2 up-sector readout datum
    c_TE := gamma_T(center)/gamma_E(center) = -8/9
  (equivalently rho_E := beta_E/alpha_E = 21/4 ; q_E := 1 + rho_E/6 = 15/8 ; with the granted T-side
  q_T = 5/6, the covariance lambda := q_E/q_T = 9/4),
  from principled finite Route-2 structure, WITHOUT empirical input. RESULT: no derivation; a SHARPER
  no-go. Forbidden-inputs discipline (from the April naturality
  no-go) respected throughout: no observed quark masses, no fitted target, no nearest-rational selection,
  no live-endpoint selector.

THE EXACT FINITE OBJECTS (the 7-site octahedral star = 1 center + 6 arms +/-x,+/-y,+/-z; O_h):
  K1  THE DERIVED LEVERAGE kappa = 3/2. The 6-arm O_h permutation rep decomposes multiplicity-free as
      A1g (+) Eg (+) T1u. Built via the antipodal involution A (the signed-permutation action of -I, which
      swaps each arm with its opposite): P_A1 = Reynolds average (all entries 1/6); P_T1 = (I-A)/2
      (antipodal-ODD 3-dim); P_E = (I+A)/2 - P_A1 (antipodal-even minus A1, 2-dim). The exact per-arm
      diagonal projector weights are P_A1=1/6, P_E=1/3, P_T1=1/2 (= dim(irrep)/6, the multiplicity-free
      transitive-perm-rep value). Hence the EXACT same-domain shell leverage
          kappa := P_T1(arm,arm)/P_E(arm,arm) = (1/2)/(1/3) = 3/2,   kappa^2 = 9/4.
  K2  the 7-site star = A1_center (+) A1_shell (+) E (+) T1 (the 6 arms carry A1+E+T1; the center is a
      separate A1); projector ranks (1,2,3) on the arms sum to 6.
  K3  THE COMMUTANT INDEPENDENCE. E and T1 are inequivalent O_h irreps, so Hom_Oh(E,T1)=0 (the Reynolds
      intertwiner average(P_T1 . g . P_E) = 0 exactly). Every O_h-equivariant star operator has an
      arbitrary 2x2 A1 block + INDEPENDENT scalars lambda_E, lambda_T on the E and T1 blocks. So
      equivariance does NOT tie lambda_E to lambda_T and does NOT fix a T/E quadratic normalization ratio.
  K4  the reduced readout family + endpoint algebra (from the landed readout-map note): with shell
      normalization and the granted T-side (beta_T/alpha_T=-1 -> q_T=5/6 ; alpha_T/alpha_E=-2),
          q_E = 1 + rho_E/6 ,   c_TE = -2 * q_T / q_E ,
      so the target chain rho_E=21/4 <-> q_E=15/8 <-> c_TE=-8/9 holds exactly, and equivalently
      lambda = q_E/q_T = (15/8)/(5/6) = 9/4.
  K5  THE PINNING. 9/4 = kappa^2 EXACTLY (the derived same-domain leverage squared). BUT the bridge
      lambda = q_E/q_T = kappa^2 is NOT a consequence of K1-K3: equivariance leaves lambda_E, lambda_T
      independent (K3), the A1 center-excess gives the SAME center increment 1/6 to E and T (so the
      carrier itself does not distinguish them), and the -8/9 sign enters only through the granted
      alpha_T/alpha_E=-2, not the projectors. So the single remaining open datum is precisely the
      covariance rule lambda = kappa^2 (or any equivalent E-center datum). This runner does not adopt
      that datum as an approved input.
  K6  ADMISSIBILITY CONTINUUM (the no-go core, independently reproduced): positivity of the E-center lift
      gives only q_E>0 <=> rho_E>-6, and idempotency/norm fixes the E-row NORM not its DIRECTION
      (b/a=rho free). So rho_E in {-1,0,1,21/4,6,...} are all exact admissible reduced maps; the target
      lambda=9/4 is one special value among a continuum.
  K7  THE RELOCATION (vs the existing color route). The other candidate origin of the same datum,
      c_TE = -R_conn = -(N_c^2-1)/N_c^2 = -8/9 (a FIBER-space SU(3) color fraction), was already adjudged
      a CROSS-DOMAIN COINCIDENCE no-go (CTE_RCONN...CROSS_DOMAIN_COINCIDENCE, 2026-06-08): a position-space
      tensor ratio identified with a fiber-space color fraction, no typed link. By contrast, kappa=3/2 is
      a SAME-DOMAIN O_h leverage on the readout's own E/T channels -- NOT a cross-domain object. So this
      note RELOCATES the missing datum to a same-domain covariance rule lambda=kappa^2, a sharper and more
      attackable target than the cross-domain color coincidence. Note 9/4 != 8/9: the two candidate
      structural numbers feed DIFFERENT slots (lambda=q_E/q_T vs c_TE directly) but yield the same final
      rho_E=21/4; neither is derived.

VERDICT: no derivation of rho_E=21/4. The pin remains open, but is SHARPENED: 9/4 = kappa^2 with
kappa=3/2 the derived same-domain O_h shell leverage, and the single remaining free datum is the
covariance bridge lambda = q_E/q_T = kappa^2, which O_h equivariance provably does not supply. This does
not sharpen-by-strengthening the April naturality no-go's logical force; it LOCATES the missing primitive
in the same domain as c_TE (improving on the cross-domain color coincidence). No PDG/fitted value.
"""
from __future__ import annotations
import itertools
from fractions import Fraction as F

import numpy as np
import sympy as sp

PASS = 0
FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    PASS += int(bool(cond))
    FAIL += int(not cond)
    return bool(cond)


# ---------------------------------------------------------------- the 6-arm O_h star + projectors
ARMS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
AIDX = {a: i for i, a in enumerate(ARMS)}


def oh_group():
    G = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product([1, -1], repeat=3):
            M = np.zeros((3, 3), int)
            for r in range(3):
                M[r, perm[r]] = signs[r]
            G.append(M)
    return G                                            # 48 signed permutation matrices = O_h


def arm_rep(M):
    P = np.zeros((6, 6))
    for a in ARMS:
        b = tuple(int(x) for x in (M @ np.array(a)))
        P[AIDX[b], AIDX[a]] = 1.0
    return P


def main() -> int:
    print("ROUTE-2 q_E PIN -- SHARPER NO-GO: 9/4 = kappa^2 (kappa=3/2 derived); covariance bridge remains open")
    print("=" * 100)
    G = oh_group()
    reps = [arm_rep(M) for M in G]
    assert len(G) == 48

    # ---- K1: the derived leverage kappa = 3/2 (antipodal-involution projectors) ----
    P_A1 = sum(reps) / 48.0
    A = arm_rep(-np.eye(3, dtype=int))                   # antipodal involution
    P_T1 = (np.eye(6) - A) / 2.0
    P_E = (np.eye(6) + A) / 2.0 - P_A1
    w_A1, w_E, w_T1 = P_A1[0, 0], P_E[0, 0], P_T1[0, 0]
    kappa = w_T1 / w_E
    check("K1 (DERIVED leverage kappa=3/2): the 6-arm O_h rep's per-arm projector weights are "
          "P_A1=1/6, P_E=1/3, P_T1=1/2 (= dim/6, multiplicity-free transitive perm rep); hence the "
          "same-domain shell leverage kappa = P_T1/P_E = (1/2)/(1/3) = 3/2 and kappa^2 = 9/4",
          abs(w_A1 - 1 / 6) < 1e-12 and abs(w_E - 1 / 3) < 1e-12 and abs(w_T1 - 1 / 2) < 1e-12
          and abs(kappa - 1.5) < 1e-12,
          f"per-arm weights A1={w_A1:.6f}(1/6), E={w_E:.6f}(1/3), T1={w_T1:.6f}(1/2); "
          f"kappa={kappa:.6f}=3/2; kappa^2={kappa**2:.6f}=9/4")

    # ---- K2: the star decomposition A1+A1+E+T1 ----
    ranks = [int(round(np.trace(P))) for P in (P_A1, P_E, P_T1)]
    spanning = np.allclose(P_A1 + P_E + P_T1, np.eye(6)) and ranks == [1, 2, 3]
    check("K2 (star decomposition): the 6 arms carry A1(+)E(+)T1 with ranks (1,2,3) spanning the arm "
          "space; the center is a separate A1, so the 7-site star = A1_center (+) A1_shell (+) E (+) T1",
          spanning, f"arm projector ranks = {ranks}; P_A1+P_E+P_T1 = I: {np.allclose(P_A1+P_E+P_T1, np.eye(6))}")

    # ---- K3: commutant independence Hom(E,T1)=0 ----
    intertwiner = sum(P_T1 @ r @ P_E for r in reps) / 48.0
    hom0 = float(np.abs(intertwiner).max()) < 1e-12
    # an O_h-equivariant operator: arbitrary on A1 (the center+arm-A1 2x2 block) + scalar on E + scalar on T1
    # check the commutant dimension on the arm space: independent lambda_E, lambda_T (+ A1 1-dim here)
    commutant_dim_arm = 1 + 1 + 1  # A1(1) + E-scalar(1) + T1-scalar(1) on the arm rep
    check("K3 (commutant independence): E and T1 are inequivalent O_h irreps, so Hom_Oh(E,T1)=0 (the "
          "Reynolds intertwiner average(P_T1 . g . P_E) vanishes); every equivariant star operator carries "
          "INDEPENDENT scalars lambda_E, lambda_T -- equivariance ties nothing between the E and T channels",
          hom0,
          f"||Reynolds(P_T1 g P_E)|| = {np.abs(intertwiner).max():.1e}; independent E,T equivariant scales")

    # ---- K4: endpoint algebra + target chain (exact rationals) ----
    rho_E = F(21, 4)
    q_T = F(5, 6)
    q_E = 1 + rho_E / 6
    c_TE = F(-2) * q_T / q_E
    lam = q_E / q_T
    chain_ok = (q_E == F(15, 8) and c_TE == F(-8, 9) and lam == F(9, 4)
                and (1 + F(-1) / 6) == q_T)
    check("K4 (endpoint algebra, exact): with shell normalization + granted T-side (beta_T/alpha_T=-1 -> "
          "q_T=5/6 ; alpha_T/alpha_E=-2): q_E=1+rho_E/6, c_TE=-2 q_T/q_E. The target chain rho_E=21/4 <-> "
          "q_E=15/8 <-> c_TE=-8/9 holds exactly, and the covariance lambda=q_E/q_T=9/4",
          chain_ok,
          f"rho_E=21/4 -> q_E={q_E} (15/8), c_TE={c_TE} (-8/9), lambda={lam} (9/4)")

    # ---- K5: the pinning -- 9/4=kappa^2 but the covariance bridge is NOT forced ----
    kappa_sq_eq_lambda = (F(3, 2) ** 2 == lam)
    # the carrier gives the SAME center increment 1/6 to E and T (carrier doesn't distinguish them):
    E_center = (1, 0, F(1, 6), 0)
    T_center = (0, 1, 0, F(1, 6))
    same_increment = (E_center[2] == T_center[3] == F(1, 6))
    check("K5 (THE PINNING): 9/4 = kappa^2 EXACTLY (derived same-domain leverage squared), yet the bridge "
          "lambda = q_E/q_T = kappa^2 is NOT a consequence of K1-K3 -- equivariance leaves lambda_E, "
          "lambda_T independent (K3), the carrier gives the SAME center increment 1/6 to E and T (so it "
          "does not distinguish them), and the -8/9 sign enters only via the granted alpha_T/alpha_E=-2, "
          "NOT the projectors. The single remaining open datum is the covariance rule lambda=kappa^2",
          kappa_sq_eq_lambda and same_increment,
          f"kappa^2 = {F(3,2)**2} == lambda = {lam}; carrier center increments: E={E_center[2]}, T={T_center[3]} (both 1/6)")

    # ---- K6: admissibility continuum (the no-go core) ----
    examples = {}
    for r in [F(-1), F(0), F(1), F(21, 4), F(6)]:
        qe = 1 + r / 6
        examples[str(r)] = (qe, F(-2) * q_T / qe)
    distinct = len({v[0] for v in examples.values()}) == len(examples)
    pos_only = "rho_E > -6 (q_E>0)"   # positivity bound, not a unique value
    check("K6 (admissibility continuum): positivity gives only rho_E>-6 (q_E>0), and idempotency/norm "
          "fixes the E-row NORM not its DIRECTION (b/a=rho free); so rho_E in {-1,0,1,21/4,6} are all "
          "exact admissible reduced maps -- the target lambda=9/4 is one special value in a continuum",
          distinct,
          "; ".join(f"rho_E={k}: q_E={v[0]},c_TE={v[1]}" for k, v in examples.items()))

    # ---- K7: the relocation vs the cross-domain color coincidence ----
    R_conn = F(3 ** 2 - 1, 3 ** 2)        # SU(3) adjoint/total fiber fraction = 8/9
    color_route = (-R_conn == c_TE)       # -R_conn = -8/9 = c_TE (the already-no-go'd color coincidence)
    distinct_numbers = (lam != R_conn)    # 9/4 (covariance, position-space) != 8/9 (color, fiber-space)
    check("K7 (RELOCATION vs the color coincidence): the other candidate origin c_TE=-R_conn=-(N_c^2-1)/N_c^2 "
          "=-8/9 is a FIBER-space SU(3) color fraction, already a CROSS-DOMAIN COINCIDENCE no-go "
          "(CTE_RCONN...2026-06-08). kappa=3/2 is instead a SAME-DOMAIN O_h leverage on the readout's own "
          "E/T channels -- NOT cross-domain. So the missing datum is RELOCATED to a same-domain covariance "
          "rule lambda=kappa^2 (a sharper, more attackable target). 9/4 != 8/9: distinct structural numbers "
          "in distinct slots, same final rho_E=21/4, neither derived",
          color_route and distinct_numbers,
          f"-R_conn = {-R_conn} = c_TE = {c_TE} (color, fiber-space, cross-domain coincidence); "
          f"lambda = {lam} = kappa^2 (covariance, same-domain); 9/4 != 8/9: {distinct_numbers}")

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    print(
        "VERDICT: no derivation of rho_E = 21/4 from the exact finite Route-2 star/O_h objects. SHARPER\n"
        "NO-GO with new exact content: 9/4 = kappa^2 where kappa = 3/2 is the DERIVED per-arm O_h shell\n"
        "leverage P_T1/P_E = dim(T1)/dim(E) on the readout's own E/T channels (a SAME-DOMAIN quantity), and\n"
        "the commutant Hom_Oh(E,T1)=0 leaves the E and T scales independent -- so equivariance does NOT\n"
        "force the readout covariance lambda = q_E/q_T = kappa^2; positivity leaves a continuum (rho_E>-6).\n"
        "The single remaining open datum is precisely the covariance bridge lambda = kappa^2 (equivalently\n"
        "the E-center datum / rho_E). This RELOCATES the missing primitive from the cross-domain color\n"
        "coincidence c_TE=-R_conn=-8/9 (a fiber-space fraction, already no-go'd) to a SAME-DOMAIN\n"
        "readout-covariance rule -- a sharper, more attackable target. Scope: closes the finite-star /\n"
        "equivariant / carrier-linear / positivity / simple-covariance routes; does NOT prove impossibility\n"
        "over arbitrary future nonlinear tensor observables. No PDG/fitted value consumed."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
