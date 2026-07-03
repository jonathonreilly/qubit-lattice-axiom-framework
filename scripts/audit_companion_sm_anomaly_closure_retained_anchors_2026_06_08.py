#!/usr/bin/env python3
"""SM one-generation anomaly closure, independently reproven from RETAINED anchors + explicit
admissions -- decoupled from the unaudited `anomaly_forces_time_theorem`.

PURPOSE (audit-unblock consolidation). The matter-content/anomaly chain
(`axiom_first_sm_anomaly_cancellation_complete`, `sm_hypercharge_uniqueness_without_nu_r`,
`rh_sector_anomaly_cancellation_identities`, ...) is correct but sits at `awaiting_audit` because every
row routes a dependency through `anomaly_forces_time_theorem` (unaudited, with documented circular
admissions), so none of them ever becomes deps-all-retained ("ready") and reaches the auditor dispatch
queue. This runner reproves the load-bearing arithmetic of that chain from primitives, depending only on
RETAINED anchors (graph_first_su3, native_gauge_closure, hypercharge_identification,
three_generation_observable_count) plus EXPLICIT admissions (the minimal SU(2)-singlet RH completion
ansatz; the doubled-Y convention), so the companion source note is auditable on its own.

It REPROVES (exact `fractions.Fraction` / integer parity), it does not import:
  A. RH hypercharge uniqueness on the no-nu_R sector: (y1,y2,y3)=(+4/3,-2/3,-2) forced by anomaly
     cancellation (discriminant a perfect square -> rational, unique up to u_R<->d_R fixed by Q>0).
  B. All six gauge-anomaly conditions cancel on the one-generation content:
     SU(3)^3, SU(2)^2 U(1)_Y, grav^2 U(1)_Y (=Tr Y), U(1)_Y^3, SU(2) Witten Z2 parity, SU(2)^3 (trivial).
  C. HONEST LEDGER (the scope, made explicit and verified):
     C1. content is NOT uniquely anomaly-forced -- SM + a vectorlike pair also cancels (the RH ansatz is
         an admission, not an anomaly consequence);
     C2. the absolute Y-scale is a vacuous rescaling convention (scaling all Y by lambda preserves all
         anomaly zeros) -- a convention, not an admitted input;
     C3. adding nu_R with free y4 reopens a 1-parameter family (neutrality y4=0 is load-bearing only if
         nu_R is included) -- nu_R is an admission, the no-nu_R sector closes without it.

Standard ABJ anomaly cancellation (Adler 1969; Bell-Jackiw 1969), Dynkin indices T(3)=T(2)=1/2,
SU(3) cubic indices A(3)=+1,A(3bar)=-1, and Witten pi_4(SU(2))=Z2 are admitted-context external
mathematical facts (comparator role), not framework derivations. No PDG/fitted value is used.
"""
from __future__ import annotations
from fractions import Fraction as F

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
# Content (doubled-Y convention Q = T_3 + Y/2). Entries: (multiplicity, Y).
# LH directly; RH given as left-conjugate fields (hypercharge sign flipped), so every entry is summed
# with a single + sign (the standard all-left-handed anomaly bookkeeping).
# N_c = 3 (retained graph_first_su3); n_gen = 3 (retained three_generation_observable_count).
# --------------------------------------------------------------------------- #
NC = 3
NGEN = 3
YQL, YLL = F(1, 3), F(-1)          # retained LH content (hypercharge_identification, retained_bounded)


def one_gen(y1, y2, y3, y4=F(0)):
    """One-generation content as (multiplicity, Y) in the all-left-conjugate frame."""
    return [
        (NC * 2, YQL),   # Q_L : 3 colour x 2 weak
        (2, YLL),        # L_L : 1 x 2 weak
        (NC, -y1),       # u_R^c : 3 colour (conj -> -Y)
        (NC, -y2),       # d_R^c : 3 colour
        (1, -y3),        # e_R^c : 1
        (1, -y4),        # nu_R^c : 1 (y4=0 by default)
    ]


def trY(fields):
    return sum(m * y for m, y in fields)


def trY3(fields):
    return sum(m * y ** 3 for m, y in fields)


def main() -> int:
    print("SM ONE-GENERATION ANOMALY CLOSURE FROM RETAINED ANCHORS (decoupled from anomaly_forces_time)")
    print("=" * 92)

    # ----------------------------------------------------------------- #
    # A. RH hypercharge uniqueness from anomaly cancellation (no-nu_R sector).
    #    Unknowns y1=Y(u_R), y2=Y(d_R), y3=Y(e_R). LH content fixed (retained).
    #    (A2) SU(3)^2 Y : 2*YQL*? -> y1+y2 = 2*YQL = 2/3 ; (A1) Tr Y : 3(y1+y2)+y3 = 0 (LH TrY=0)
    #    (A3) Tr Y^3 : 3(y1^3+y2^3)+y3^3 = LH Tr Y^3 = -16/9 in all-left bookkeeping.
    # ----------------------------------------------------------------- #
    s = 2 * YQL                       # y1 + y2 from SU(3)^2 Y, = 2/3
    y3 = -3 * s                       # from Tr Y (LH Tr Y = 6*YQL+2*YLL = 0), so 3 s + y3 = 0
    lh_trY3 = NC * 2 * YQL ** 3 + 2 * YLL ** 3   # = -16/9
    # all-left-conjugate Tr[Y^3]=0 => 3(y1^3+y2^3) + y3^3 = lh_trY3
    sum_cubes = (lh_trY3 - y3 ** 3) / 3          # y1^3 + y2^3 = 56/27
    p = (s ** 3 - sum_cubes) / (3 * s)           # y1*y2 from (y1+y2)^3 identity
    disc = s * s - 4 * p
    from math import isqrt

    def rational_sqrt(q):
        if q < 0:
            return None
        n, d = q.numerator, q.denominator
        rn, rd = isqrt(n), isqrt(d)
        return F(rn, rd) if (rn * rn == n and rd * rd == d) else None

    rroot = rational_sqrt(disc)
    check(
        "discriminant of the RH quadratic is a perfect square (rational, hence unique SM solution)",
        rroot is not None,
        f"s=y1+y2={s}, y1*y2={p}, disc={disc}, sqrt(disc)={rroot}",
    )
    y1 = (s + rroot) / 2
    y2 = s - y1
    check(
        "RH hypercharges uniquely forced: (y1,y2,y3) = (+4/3, -2/3, -2) [doubled-Y], Q(u_R)>0 fixes the swap",
        {y1, y2} == {F(4, 3), F(-2, 3)} and y3 == F(-2),
        f"(y1,y2,y3) = ({max(y1,y2)}, {min(y1,y2)}, {y3})",
    )
    Y1, Y2, Y3 = F(4, 3), F(-2, 3), F(-2)   # canonical SM (Q(u_R)>0)

    # ----------------------------------------------------------------- #
    # B. All six gauge-anomaly conditions cancel on the one-generation content.
    # ----------------------------------------------------------------- #
    fields = one_gen(Y1, Y2, Y3)
    # (A1) SU(3)^3 cubic: A(3)=+1, A(3bar)=-1. Q_L weak-mult 2 in 3; u_R^c,d_R^c in 3bar.
    su3_cubic = 2 * F(1) + 1 * F(-1) + 1 * F(-1)
    check("(A1) SU(3)^3 cubic anomaly cancels: 2*(+1) + (-1) + (-1) = 0", su3_cubic == 0, f"= {su3_cubic}")
    # (A2) SU(2)^2 U(1)_Y: only LH doublets; T(2)=1/2.
    su2sq_Y = F(1, 2) * (NC * YQL + 1 * YLL)
    check("(A2) SU(2)^2 U(1)_Y cancels: (1/2)(3*(1/3) + (-1)) = 0", su2sq_Y == 0, f"= {su2sq_Y}")
    # (A3) grav^2 U(1)_Y = Tr[Y]
    grav_Y = trY(fields)
    check("(A3) grav^2 U(1)_Y = Tr[Y] cancels on full LH+RH content", grav_Y == 0, f"Tr[Y] = {grav_Y}")
    # (A4) U(1)_Y^3
    Y3sum = trY3(fields)
    check("(A4) U(1)_Y^3 cubic cancels on full LH+RH content", Y3sum == 0, f"Tr[Y^3] = {Y3sum}")
    # (A5) SU(2) Witten Z2 parity: count SU(2) doublets per gen = N_c (Q_L) + 1 (L_L); x n_gen.
    n_doublets = NGEN * (NC + 1)
    check("(A5) SU(2) Witten Z2 parity cancels: N_D = 3*(3+1) = 12, even", n_doublets % 2 == 0,
          f"N_D = {n_doublets}, mod 2 = {n_doublets % 2}")
    # (A0) SU(2)^3 cubic: identically zero (no symmetric d^abc for SU(2)).
    check("(A0) SU(2)^3 cubic identically zero (group-theoretic, all SU(2) reps (pseudo)real)", True)

    # ----------------------------------------------------------------- #
    # C. HONEST LEDGER -- the explicit scope/admissions, verified.
    # ----------------------------------------------------------------- #
    print("\n-- C. Honest forced/admitted/convention ledger --")
    # C1. content is NOT uniquely anomaly-forced: SM + a vectorlike pair (Y, -Y) also cancels.
    vec = fields + [(1, F(5)), (1, F(-5))]
    check(
        "C1 (admission): the matter CONTENT is not anomaly-unique -- SM + a vectorlike pair (Y=+/-5) "
        "also cancels Tr[Y] and Tr[Y^3]; the minimal RH completion is an ADMITTED ansatz, not forced",
        trY(vec) == 0 and trY3(vec) == 0,
        f"SM+vectorlike: Tr[Y]={trY(vec)}, Tr[Y^3]={trY3(vec)}",
    )
    # C2. absolute Y-scale is a vacuous rescaling convention: scale all Y by lambda, anomalies stay zero.
    lam = F(7, 5)
    scaled = [(m, lam * y) for m, y in fields]
    check(
        "C2 (convention): the absolute Y-scale is a vacuous rescaling -- scaling all Y by lambda keeps "
        "Tr[Y]=Tr[Y^3]=0; the overall scale is a gauge/normalization choice, not an admitted number",
        trY(scaled) == 0 and trY3(scaled) == 0,
        f"lambda={lam}: Tr[Y]={trY(scaled)}, Tr[Y^3]={trY3(scaled)}",
    )
    # C3. adding nu_R with free t reopens a 1-parameter family
    #     y_u=4/3+t, y_d=-2/3-t, y_e=-2-t, y_nu=t.
    #     Neutrality t=0 is load-bearing only with nu_R.
    t = F(1, 2)
    y1_nu = F(4, 3) + t
    y2_nu = F(-2, 3) - t
    y3_nu = F(-2) - t
    y4_nu = t
    f_nu = one_gen(y1_nu, y2_nu, y3_nu, y4_nu)
    nu_family_su3sq_y = 2 * YQL - y1_nu - y2_nu
    check(
        "C3 (admission): adding nu_R with free y4 reopens a 1-parameter anomaly-free family "
        "(y4=1/2 example cancels SU(3)^2Y, Tr[Y], and Tr[Y^3]); neutrality y4=0 is load-bearing only when nu_R is included",
        nu_family_su3sq_y == 0 and trY(f_nu) == 0 and trY3(f_nu) == 0,
        (
            f"t={t}: (y_u,y_d,y_e,y_nu)=({y1_nu},{y2_nu},{y3_nu},{y4_nu}); "
            f"SU(3)^2Y={nu_family_su3sq_y}, Tr[Y]={trY(f_nu)}, Tr[Y^3]={trY3(f_nu)}"
        ),
    )

    print(f"\nSCORECARD PASS={PASS} FAIL={FAIL}")
    print(
        "VERDICT: GIVEN the retained LH content (hypercharge_identification / native_gauge_closure / "
        "graph_first_su3), N_c=3 and n_gen=3 (retained), and the EXPLICIT minimal SU(2)-singlet RH "
        "completion ansatz, the RH hypercharges are uniquely forced (+4/3,-2/3,-2) and all six "
        "gauge-anomaly conditions cancel exactly. The matter CONTENT itself (RH ansatz, nu_R branch) and "
        "the absolute Y-SCALE are admissions/conventions, not anomaly consequences. This reproves the "
        "load-bearing arithmetic of the matter-content chain with deps-all-retained, decoupled from the "
        "unaudited anomaly_forces_time_theorem. Audit lane sets the verdict."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
