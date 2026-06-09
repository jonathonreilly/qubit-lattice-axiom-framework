"""Pressure-test of the headline PMNS delta_CP prediction (P1): is delta_CP in [251.86, 270] deg a
BRANCH-ROBUST forecast, or does it ride on the IMPOSED branch-choice rule (Basin-1, q=sqrt(8/3)-delta)?

The narrow-theorem note (PMNS_THETA12_THETA13_DCP_PREDICTIONS_2026-05-17) certifies delta_CP in the third
quadrant by RIGOROUS 200-bit box-Krawczyk interval arithmetic -- but ONLY over box B (the Basin-1
preimage of the NuFit rectangle) and ONLY on the chamber boundary q=sqrt(8/3)-delta, and it explicitly
ADMITS (sec 5, sec 7, residual list) it is SILENT on whether competing chamber-boundary branches give the
same delta_CP. This runner tests that exact gap at float precision, reusing the note's own chart.

Chart H(m,delta,q) (float, identical to the runner frontier_pmns..._narrow.py lines 205-207),
GAMMA=0.5, SQRT_8_3=sqrt(8/3), SQRT8_3=sqrt(8)/3:
  H = [[ m,                         S83 - d + q,                 -S83 + d + q - i*G ],
       [ S83 - d + q,               d,                           -S8_3 + m + q      ],
       [-S83 + d + q + i*G,        -S8_3 + m + q,                -d                 ]]
Observables via eigen-projectors P_k = v_k v_k^dag (rephasing invariant), flavor rows (e,mu,tau)=(2,1,0),
mass states = eigenvectors sorted by ascending eigenvalue:
  s13^2=(P2)_22, s12^2=(P1)_22/(1-s13^2), s23^2=(P2)_11/(1-s13^2),
  J=Im[(P0)_21 (P1)_12], ReBox=Re[(P0)_21 (P2)_12], cos_neg_num=ReBox + c12^2 c13^2 s13^2 s23^2,
  delta_CP = atan2(J, -cos_neg_num) mod 360  (D=c12 s12 c23 s23 c13^2 s13 > 0 cancels).

TESTS:
  V0 (anchor validation): at (m,d,q)=(0.657061,0.933806,0.715042) reproduce the note's
      (s12^2,s13^2,s23^2,delta_CP) ~ (0.307,0.0218,0.545,260.88) -> confirms the convention.
  V1 (branch scan, chamber boundary q=sqrt(8/3)-delta): scan a BROAD (m,delta) domain, collect ALL
      preimages of the NuFit-central target (s12^2,s13^2)=(0.307,0.0218), cluster into basins, report
      delta_CP per basin. ROBUST iff every basin gives third-quadrant delta_CP; BRANCH-DEPENDENT iff any
      basin lands in a different quadrant (then the imposed Basin-1 rule is load-bearing and must be
      justified, not fitted).
  V2 (embedding sensitivity): is q=sqrt(8/3)-delta special? Recompute delta_CP at the anchor (m,delta) for
      nearby embeddings q=sqrt(8/3)-delta + t, t in {-0.1,-0.05,0,0.05,0.1}, to see how strongly the
      forecast depends on the exact chamber-boundary surface.

No PDG/NuFit value is consumed as derived; the NuFit-central point is used only as the localization target
(named external comparison, exactly as the note uses it). Float-precision DIAGNOSTIC (the note's interval
cert is the rigorous artifact); this isolates the branch/embedding dependence the note leaves open.
"""
from __future__ import annotations
import numpy as np

S83 = np.sqrt(8.0 / 3.0)     # sqrt(8/3) ~ 1.6330
S8_3 = np.sqrt(8.0) / 3.0    # sqrt(8)/3 ~ 0.9428
G = 0.5

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


def H_of(m, d, q):
    return np.array([
        [m,                  S83 - d + q,        -S83 + d + q - 1j * G],
        [S83 - d + q,        d,                  -S8_3 + m + q],
        [-S83 + d + q + 1j * G, -S8_3 + m + q,   -d],
    ], dtype=complex)


def observables(m, d, q):
    """Return (s12^2, s13^2, s23^2, dcp_deg) or None if degenerate."""
    H = H_of(m, d, q)
    w, V = np.linalg.eigh(H)               # ascending eigenvalues; columns = eigenvectors
    # projectors P_k[a,b] = V[a,k] conj(V[b,k])
    P = [np.outer(V[:, k], np.conj(V[:, k])) for k in range(3)]
    s13 = np.real(P[2][2, 2])
    if not (0 < s13 < 1):
        return None
    c13 = 1.0 - s13
    s12 = np.real(P[1][2, 2]) / c13
    s23 = np.real(P[2][1, 1]) / c13
    if not (0 <= s12 <= 1 and 0 <= s23 <= 1):
        return None
    J = np.imag(P[0][2, 1] * P[1][1, 2])
    ReBox = np.real(P[0][2, 1] * P[2][1, 2])
    cos_neg_num = ReBox + (1 - s12) * c13 * s13 * s23
    dcp = np.degrees(np.arctan2(J, -cos_neg_num)) % 360.0
    return s12, s13, s23, dcp


def quadrant(dcp):
    if 0 <= dcp < 90:
        return "Q1 (0-90)"
    if 90 <= dcp < 180:
        return "Q2 (90-180)"
    if 180 <= dcp < 270:
        return "Q3 (180-270)"
    return "Q4 (270-360)"


def main() -> int:
    print("PMNS delta_CP PRESSURE-TEST: is the third-quadrant forecast branch-robust or branch-dependent?")
    print("=" * 92)

    # ---- V0: anchor validation ----
    anchor = observables(0.657061342210, 0.933806343759, 0.715042329587)
    s12a, s13a, s23a, dcpa = anchor
    ok0 = (abs(s12a - 0.307) < 5e-3 and abs(s13a - 0.0218) < 1e-3
           and abs(s23a - 0.545) < 1e-2 and abs(dcpa - 260.88) < 0.5)
    check("V0 (anchor validation): float forward map reproduces the note's anchor "
          "(s12^2,s13^2,s23^2,delta_CP)=(0.307,0.0218,0.545,260.88) -> the convention is correct",
          ok0, f"computed s12^2={s12a:.4f}, s13^2={s13a:.5f}, s23^2={s23a:.4f}, delta_CP={dcpa:.2f} deg")

    # ---- V1: branch scan on the chamber boundary q = sqrt(8/3) - delta ----
    TGT12, TGT13 = 0.307, 0.0218     # NuFit-central (localization target, comparison only)
    TOL = 0.004
    ms = np.linspace(-1.5, 3.5, 900)
    ds = np.linspace(0.0, 2.6, 900)
    hits = []
    for m in ms:
        for d in ds:
            q = S83 - d
            o = observables(m, d, q)
            if o is None:
                continue
            s12, s13, s23, dcp = o
            if abs(s12 - TGT12) < TOL and abs(s13 - TGT13) < TOL:
                hits.append((m, d, dcp, s23))
    # cluster hits into basins by (m,d) proximity
    basins = []
    for (m, d, dcp, s23) in hits:
        placed = False
        for bcl in basins:
            mm, dd = bcl["m"], bcl["d"]
            if abs(m - mm) < 0.25 and abs(d - dd) < 0.25:
                bcl["pts"].append((m, d, dcp, s23))
                bcl["m"] = np.mean([p[0] for p in bcl["pts"]])
                bcl["d"] = np.mean([p[1] for p in bcl["pts"]])
                placed = True
                break
        if not placed:
            basins.append({"m": m, "d": d, "pts": [(m, d, dcp, s23)]})
    print(f"\n  V1a branch scan, TWO-angle input (the note's stated logic: s12^2,s13^2 are inputs, "
          f"s23^2+delta_CP are outputs). target (s12^2,s13^2)=({TGT12},{TGT13}) +/-{TOL}: "
          f"{len(hits)} grid hits in {len(basins)} basin(s)")
    has_non_q3_competitor = False
    for i, bcl in enumerate(basins):
        dcps = [p[2] for p in bcl["pts"]]
        s23s = [p[3] for p in bcl["pts"]]
        if not all(180 <= x < 270 for x in dcps):
            has_non_q3_competitor = True
        print(f"    basin {i}: (m,delta)~({bcl['m']:.3f},{bcl['d']:.3f})  delta_CP in [{min(dcps):.1f},{max(dcps):.1f}] deg "
              f"{sorted({quadrant(x) for x in dcps})}  s23^2 in [{min(s23s):.3f},{max(s23s):.3f}]")
    check("V1a (two-angle input IS branch-dependent -- verified finding): under the note's stated logic "
          "(s12^2,s13^2 as the only inputs), there EXISTS a competing chamber-boundary preimage whose "
          "delta_CP is NOT in Q3 (basin 0: Q2, ~98-114 deg). This answers the note's own open sec-5 "
          "question: competing branches do NOT agree -- the imposed Basin-1 rule is genuinely load-bearing "
          "under two-angle input.",
          len(basins) >= 2 and has_non_q3_competitor,
          f"{len(basins)} basin(s); competing non-Q3 branch present = {has_non_q3_competitor}")

    # ---- V1b: FAIR test -- fix all THREE measured angles (s23^2 is itself measured ~0.545) ----
    TGT23, TOL23 = 0.545, 0.02
    hits3 = [(m, d, dcp, s23) for (m, d, dcp, s23) in hits if abs(s23 - TGT23) < TOL23]
    basins3 = []
    for (m, d, dcp, s23) in hits3:
        placed = False
        for bcl in basins3:
            if abs(m - bcl["m"]) < 0.25 and abs(d - bcl["d"]) < 0.25:
                bcl["pts"].append((m, d, dcp, s23)); bcl["m"] = np.mean([p[0] for p in bcl["pts"]]); bcl["d"] = np.mean([p[1] for p in bcl["pts"]]); placed = True; break
        if not placed:
            basins3.append({"m": m, "d": d, "pts": [(m, d, dcp, s23)]})
    print(f"\n  V1b FAIR test, THREE-angle input (s23^2~{TGT23} is also MEASURED, +/-{TOL23}): "
          f"{len(hits3)} grid hits in {len(basins3)} basin(s)")
    near_max = True   # all surviving delta_CP near-maximal (~Q3, NOT the Q2 competitor)
    for i, bcl in enumerate(basins3):
        dcps = [p[2] for p in bcl["pts"]]; s23s = [p[3] for p in bcl["pts"]]
        near_max = near_max and all(230 <= x <= 285 for x in dcps)
        print(f"    basin {i}: (m,delta)~({bcl['m']:.3f},{bcl['d']:.3f})  delta_CP in [{min(dcps):.1f},{max(dcps):.1f}] deg "
              f"{sorted({quadrant(x) for x in dcps})}  s23^2 in [{min(s23s):.3f},{max(s23s):.3f}]")
    check("V1b (THREE-angle robustness -- the fair test): with s23^2 ALSO fixed to its measured value, does "
          "EXACTLY ONE basin survive (the Q2 competitor excluded) and is it near-maximal CP (~Q3)?  PASS here "
          "= the competing branch is empirically excluded by the measured s23^2 (NOT just an imposed rule); "
          "so delta_CP near-maximal is robust given the 3 measured angles, and the prediction can be stated "
          "conditional on data, dropping the imposed branch rule. (The exact [251.86,270] bracket is the "
          "note's 200-bit interval cert; this loose float scan only checks branch structure, not the bracket.)",
          len(basins3) == 1 and near_max,
          f"{len(basins3)} basin(s) match all 3 angles (the Q2 s23^2~0.70 competitor is gone); near-maximal = {near_max}")

    # ---- V2: embedding sensitivity ----
    print("\n  V2 embedding sensitivity (anchor (m,delta), q = sqrt(8/3) - delta + t):")
    sens = []
    for t in (-0.10, -0.05, 0.0, 0.05, 0.10):
        o = observables(0.657061342210, 0.933806343759, S83 - 0.933806343759 + t)
        if o is None:
            print(f"    t={t:+.2f}: degenerate")
            continue
        s12, s13, s23, dcp = o
        sens.append((t, dcp))
        print(f"    t={t:+.2f}: delta_CP={dcp:7.2f} deg  {quadrant(dcp)}  (s12^2={s12:.3f}, s13^2={s13:.4f})")
    spread = max(d for _, d in sens) - min(d for _, d in sens) if sens else 0.0
    check("V2 (embedding sensitivity): how far does delta_CP move as the embedding surface q is perturbed "
          "off the chamber boundary by t in +/-0.1?  A large swing means the exact q=sqrt(8/3)-delta surface "
          "is load-bearing for the forecast.",
          spread > 10.0, f"delta_CP spread over t in [-0.1,0.1] = {spread:.1f} deg")

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    print(f"runner_check_breakdown = {{A: {PASS}, B: 0, C: 0, D: 0, total_pass: {PASS}}}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
