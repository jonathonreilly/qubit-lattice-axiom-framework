"""Close (X6): rigorously certify the Basin-1 chamber-boundary preimage of the NuFit (s12^2,s13^2)
rectangle is contained in box B -- the single named external admission left under the P1 delta_CP forecast.

STRATEGY (the "outer-frame Krawczyk" the P1 note names): let S be a closed shell immediately surrounding
box B (S = (B grown by width w) minus B). If the interval image F(S) of the forward map
  F(m,delta) = (s12^2, s13^2)   on the chamber boundary q = sqrt(8/3) - delta
is DISJOINT from the NuFit rectangle over ALL of S (rigorous 200-bit interval arithmetic), then
F^{-1}(rect) has NO point in S, so the shell S separates the plane: the connected component of
F^{-1}(rect) containing the anchor (= Basin-1, inside B) cannot cross S, hence Basin-1 ⊂ B. QED.

This is a genuine TEST of (X6): PASS => the preimage is provably inside B (X6 closed, modulo the topological
lemma below); a persistent FAIL on a sub-box that bisection cannot clear would indicate the preimage
reaches ∂B (X6 in question). The competing Basin-0 (m~ -0.01) is far from B (delta-m ~ 0.7), so a thin
shell does not touch it -- the certificate concerns the Basin-1 component only, exactly as (X6) states.

Reuses the P1 runner's EXACT interval machinery (pmns_full_interval, interval_newton, projectors,
SQRT_8_3) at 200-bit mpmath precision -- no re-derivation of the chart or the observables.

Topological lemma (made explicit; checked for soundness, not by the runner): for a continuous F and a
closed shell S that fully encloses the open box int(B), if F(S) ∩ rect = empty then
F^{-1}(rect) ∩ S = empty; therefore F^{-1}(rect) is contained in int(B) ∪ (exterior of B∪S), and the
component meeting int(B) (Basin-1, which contains the anchor) is contained in int(B) ⊂ B.

Outputs: per-shell-strip certification counts; PASS=all shell sub-boxes certified disjoint from rect.
No PDG/NuFit value is derived; the rectangle and box B are the named comparison/admission objects of P1.
"""
from __future__ import annotations
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from mpmath import iv
import frontier_pmns_theta12_theta13_dcp_predictions_narrow as P1

SQRT_8_3 = P1.SQRT_8_3
pmns_full_interval = P1.pmns_full_interval

# Box B (m, delta) and the NuFit 3-sigma rectangle (s12^2, s13^2) -- the P1 note's objects.
B_M = (0.625, 0.750)
B_D = (0.902, 0.956)
RECT_S12 = (0.270, 0.341)
RECT_S13 = (0.02029, 0.02391)

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


def disjoint_from_rect(block):
    """True if the interval image box (s12^2, s13^2) is provably disjoint from the NuFit rectangle.
    Disjoint iff separated in at least one coordinate (upper < lo or lower > hi). The interval ENDPOINTS
    (mpmath mpf, the rigorous outer bounds) are compared directly -- no float() narrowing -- so the test
    is interval-rigorous (an image upper bound strictly below the rect lower bound rigorously certifies
    separation; round-to-nearest could spuriously narrow the bound)."""
    s12 = block["s_12sq"]; s13 = block["s_13sq"]
    if s12.b < RECT_S12[0] or s12.a > RECT_S12[1]:
        return True
    if s13.b < RECT_S13[0] or s13.a > RECT_S13[1]:
        return True
    return False


FAILS = []   # locations + reason of uncleared sub-boxes


def certify_box(m_lo, m_hi, d_lo, d_hi, depth, max_depth):
    """Return (n_certified, n_failed). A box is certified if its interval image is disjoint from rect,
    else bisect (longest side) until max_depth. pmns_full_interval==None (degenerate) is bisected too."""
    m_iv = iv.mpf([m_lo, m_hi]); d_iv = iv.mpf([d_lo, d_hi])
    q_iv = SQRT_8_3 - d_iv               # chamber boundary
    block = pmns_full_interval(m_iv, d_iv, q_iv)
    if block is not None and disjoint_from_rect(block):
        return 1, 0
    if depth >= max_depth:
        FAILS.append((m_lo, m_hi, d_lo, d_hi, "none" if block is None else "overlap"))
        return 0, 1
    # bisect longest side
    if (m_hi - m_lo) >= (d_hi - d_lo):
        mm = 0.5 * (m_lo + m_hi)
        a = certify_box(m_lo, mm, d_lo, d_hi, depth + 1, max_depth)
        b = certify_box(mm, m_hi, d_lo, d_hi, depth + 1, max_depth)
    else:
        dm = 0.5 * (d_lo + d_hi)
        a = certify_box(m_lo, m_hi, d_lo, dm, depth + 1, max_depth)
        b = certify_box(m_lo, m_hi, dm, d_hi, depth + 1, max_depth)
    return a[0] + b[0], a[1] + b[1]


def certify_strip(name, m_lo, m_hi, d_lo, d_hi, n_long, n_short, max_depth=10):
    """Tile a shell strip into n_long x n_short cells and certify each."""
    tot_c = tot_f = 0
    span_m = m_hi - m_lo
    span_d = d_hi - d_lo
    # tile finely along the longer extent
    if span_m >= span_d:
        nx, ny = n_long, n_short
    else:
        nx, ny = n_short, n_long
    for i in range(nx):
        for j in range(ny):
            ml = m_lo + span_m * i / nx
            mh = m_lo + span_m * (i + 1) / nx
            dl = d_lo + span_d * j / ny
            dh = d_lo + span_d * (j + 1) / ny
            c, f = certify_box(ml, mh, dl, dh, 0, max_depth)
            tot_c += c; tot_f += f
    print(f"    strip {name:7s}: cells {nx}x{ny}  certified={tot_c}  failed={tot_f}")
    return tot_c, tot_f


def main() -> int:
    iv.prec = 200
    print("Closing (X6): outer-frame interval certificate that Basin-1 preimage of the NuFit rect ⊂ B")
    print("=" * 92)

    # anchor sanity: the anchor maps into the rect ON THE CHAMBER BOUNDARY (the same map F that S1
    # certifies on the shell). Use q = sqrt(8/3) - delta (NOT the 3D-pin q_+=0.715), so S0 sanity-checks
    # exactly the boundary map F that the topological lemma's anchoring premise relies on.
    m_star, d_star = iv.mpf("0.657061342210"), iv.mpf("0.933806343759")
    anchor = pmns_full_interval(m_star, d_star, SQRT_8_3 - d_star)
    a12, a13 = float(anchor["s_12sq"].mid), float(anchor["s_13sq"].mid)
    check("S0 (anchor in rect, on the chamber boundary): the PDG-central preimage maps into the NuFit "
          "rectangle under the SAME boundary map F that S1 certifies (q = sqrt(8/3) - delta) -> the anchor "
          "genuinely lies in F^{-1}(rect), so the topological lemma's anchoring premise holds and B is the "
          "right localization box",
          RECT_S12[0] <= a12 <= RECT_S12[1] and RECT_S13[0] <= a13 <= RECT_S13[1],
          f"on-boundary anchor image s12^2={a12:.5f} in {RECT_S12}, s13^2={a13:.5f} in {RECT_S13}")

    # shell width and tiling
    W = 0.03
    mlo, mhi = B_M[0] - W, B_M[1] + W
    dlo, dhi = B_D[0] - W, B_D[1] + W
    NL, NS = 90, 16    # cells along long / short extent of each strip
    print(f"\n  outer frame: shell of width W={W} around B=[{B_M[0]},{B_M[1]}]x[{B_D[0]},{B_D[1]}]"
          f"  (chamber boundary q=sqrt(8/3)-delta), tiling ~{NL}x{NS}/strip, bisection depth<=10")
    tc = tf = 0
    for nm, args in [
        ("bottom", (mlo, mhi, dlo, B_D[0])),
        ("top",    (mlo, mhi, B_D[1], dhi)),
        ("left",   (mlo, B_M[0], dlo, dhi)),
        ("right",  (B_M[1], mhi, dlo, dhi)),
    ]:
        c, f = certify_strip(nm, *args, NL, NS, max_depth=16)
        tc += c; tf += f
    if FAILS:
        print(f"  uncleared boxes ({len(FAILS)}): showing up to 6")
        for (ml, mh, dl, dh, why) in FAILS[:6]:
            print(f"    m=[{ml:.5f},{mh:.5f}] delta=[{dl:.5f},{dh:.5f}] reason={why}")
        nover = sum(1 for x in FAILS if x[4] == "overlap"); nnone = sum(1 for x in FAILS if x[4] == "none")
        print(f"    failure types: overlap(blow-up)={nover}, interval-Newton-none={nnone}")

    check("S1 (outer-frame containment): EVERY shell sub-box's interval image (s12^2,s13^2) is DISJOINT from "
          "the NuFit rectangle -> F^{-1}(rect) has no point in the shell -> the Basin-1 component (containing "
          "the anchor in B) cannot cross the shell -> Basin-1 preimage ⊂ B. (X6) is CLOSED by interval "
          "certificate (modulo the explicit topological separation lemma).",
          tf == 0,
          f"shell sub-boxes: certified-disjoint={tc}, uncleared={tf}")

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    if tf == 0:
        print("VERDICT: (X6) preimage-localization is CLOSED -- the outer-frame interval certificate proves the\n"
              "Basin-1 chamber-boundary preimage of the entire NuFit rectangle is contained in box B, upgrading\n"
              "(X6) from a multistart-fsolve named admission to a 200-bit-rigorous containment. Closing (X6)\n"
              "RELOCATES (does not eliminate) the forecast's conditionality. The P1 delta_CP forecast then rests\n"
              "on: (i) the chart H(m,delta,q) + the chamber-boundary surface q=sqrt(8/3)-delta; (ii) the\n"
              "measured-theta23 filter distinguishing Basin-1 from the disjoint Basin-0 (m~-0.01, J flips sign,\n"
              "delta_CP~105 deg, predicted s23^2~0.71), as stated in the branch-robustness note; and (iii) the\n"
              "named-external NuFit input bands. (X6) itself is no longer an open preimage-localization admission.")
    else:
        print(f"VERDICT: {tf} shell sub-box(es) could not be cleared by bisection -- either interval blow-up\n"
              "(try finer tiling / deeper bisection) or the preimage genuinely reaches the shell (X6 in\n"
              "question on those boxes). Reports the location for follow-up; (X6) NOT closed as stated.")
    print(f"runner_check_breakdown = {{A: {PASS}, B: 0, C: 0, D: 0, total_pass: {PASS}}}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
