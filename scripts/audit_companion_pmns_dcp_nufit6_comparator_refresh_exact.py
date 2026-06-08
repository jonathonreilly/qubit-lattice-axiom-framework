r"""
Audit companion - PMNS delta_CP forecast under NuFit-6: its experimental STANDING degrades from favorable (NuFit-5.3)
to disfavored-but-allowed (NuFit-6.0), and the theta_23 upper-octant prediction now flips with the SK-atmospheric
choice. The predicted band is INPUT-STABLE (the inputs it consumes barely moved) but is NOT re-certified here.

WHY THIS NOTE: the standing PMNS delta_CP / theta_23 forecast notes (PMNS_THETA12_THETA13_DCP_PREDICTIONS_2026-05-17
and the theta_23 cascade Cycles 5a/6a/7) are anchored on NuFit-5.3 (X3/X3'), under which delta_CP was T2K-driven
toward ~230-270 deg, making the framework band [251.86, 270] deg look like a tight 7.3% sub-region match. NuFit-6.0
(2024, arXiv:2410.05380) moved the normal-ordering best fit to 177 deg (no-SK) / 212 deg (with-SK), CP-conserving
within ~1 sigma. (NuFit-6.1, Nov 2025, nu-fit.org node/309, is the latest version and is qualitatively the same for
this purpose: NO consistent with CP conservation within 1 sigma, theta_23 octant still ambiguous; v6.0 2024 is used
here as the precise comparator.) This runner re-assesses the forecast against NuFit-6.0 as the current comparator.

KEY STRUCTURAL POINT (reproven below): the forecast CONSUMES (s_12^2, s_13^2) as inputs (the NuFit rectangle X3) and
produces delta_CP as the forced output; it does NOT consume the measured delta_CP. So whether the PREDICTED band moves
is governed by whether the (s_12^2, s_13^2) INPUT rectangle moved 5.3 -> 6.0 -- and it barely did. So the band as a
function of those inputs is EXPECTED stable; the comparison target (measured delta_CP) is what moved.

COMPUTED (exact / interval-free arithmetic):
 (A) INPUT STABILITY (NOT a re-certification): the NuFit-6.0 NO (s_12^2, s_13^2) rectangle (both no-SK and with-SK)
     shifts from the NuFit-5.3 rectangle by about 7% of its 3-sigma width AND lies inside the region the chamber box B
     maps onto (s_12^2 in [0.008, 0.97], s_13^2 in [0.0005, 0.121]; landed runner Part 4 coverage). CAVEAT: the landed
     box-Krawczyk certificate covers only the sub-boxes whose image overlaps the NuFit-5.3 rectangle, NOT all of box B;
     this note does NOT re-run the certificate over the 6.0 rectangle. So the band is taken AS the landed
     [251.86, 270] for the standing assessment; a rigorous re-certification over the 6.0 rectangle is left to a future
     iteration. The small input shift makes a large band shift unlikely, but that is an expectation, not a certificate.
 (B) delta_CP STANDING: the band [251.86, 270] is WITHIN the NuFit-6.0 NO 3-sigma range for BOTH no-SK [96, 422] and
     with-SK [124, 364] (NOT excluded), but the NuFit-6.0 best fit (177 / 212) lies OUTSIDE the band (disfavored).
     Contrast NuFit-5.3 (favored ~230-270, band looked like a match). The "~1.5-2 sigma" figure below is a CRUDE
     asymmetric-error yardstick (band-edge minus best-fit over the 1-sigma error), NOT a likelihood significance: the
     NO delta_CP likelihood is strongly non-Gaussian/wrapped (3-sigma reaches 422 deg) and NO is consistent with CP
     conservation within 1 sigma.
 (C) theta_23 OCTANT: the framework predicts s_23^2 > 0.5 (upper). NuFit-6.0 NO gives 0.561 (no-SK, UPPER, agrees) vs
     0.470 (with-SK, LOWER, disagrees) -> the octant confirmation is now SK-dependent, not clean.

Reprove-and-cite: the standing arithmetic (rectangle shift vs width; 6.0 rectangle inside box-B image region;
band-within-3-sigma; best-fit-outside-band; octant test) is reproven here from the numbers. NuFit-5.3 and NuFit-6.0
(arXiv:2410.05380) values are COMPARATORS (named external admissions for the labeling step), never derivation inputs;
the framework's predicted band [251.86, 270] is the landed theorem content (runner frontier_pmns_..._narrow.py, 61/61),
inherited AS STATED here, not re-derived and not re-certified. No value is fit. This is a comparator refresh + honest
standing update, NOT a no-go and NOT a new prediction.
"""

R = []
def chk(label, ok):
    R.append((label, bool(ok)))

# Framework predicted band (landed theorem content; runner frontier_pmns_theta12_theta13_dcp_predictions_narrow.py 61/61)
BAND = (251.86, 270.00)          # interval certificate (PDG convention, deg)
BAND_FLOAT = (257.57, 268.82)    # tighter floating-point image
ANCHOR = 260.88                  # PDG-central anchor, sin(delta_CP) = -0.987

# Comparator rectangles on (s_12^2, s_13^2): NuFit-5.3 (used in the landed note, X3) vs NuFit-6.0 NO (arXiv:2410.05380)
RECT_53     = {'s12': (0.270, 0.341),  's13': (0.02029, 0.02391)}
RECT_60_NOSK= {'s12': (0.275, 0.345),  's13': (0.02023, 0.02376)}
RECT_60_SK  = {'s12': (0.275, 0.345),  's13': (0.02030, 0.02388)}
# Region the chamber box B maps onto (landed runner Part 4 broad-sweep coverage result)
BOXB_IMAGE  = {'s12': (0.008, 0.97),   's13': (0.0005, 0.121)}

def width(iv):  return iv[1] - iv[0]
def maxshift(a, b):  return max(abs(a[0]-b[0]), abs(a[1]-b[1]))
def contains(outer, inner):  return outer[0] <= inner[0] and inner[1] <= outer[1]

# ---------------------------------------------------------------------------------------------------
# (A) INPUT STABILITY under the 5.3 -> 6.0 comparator refresh (NOT a re-certification of the band)
# ---------------------------------------------------------------------------------------------------
# (A1) the consumed (s_12^2, s_13^2) inputs barely moved: shift about 7% of the 3-sigma width
for lab, rect in [('noSK', RECT_60_NOSK), ('SK', RECT_60_SK)]:
    sh12 = maxshift(RECT_53['s12'], rect['s12']) / width(RECT_53['s12'])
    sh13 = maxshift(RECT_53['s13'], rect['s13']) / width(RECT_53['s13'])
    chk(f"(A1-{lab}) consumed inputs barely moved 5.3->6.0: s_12^2 shift {sh12*100:.1f}% and s_13^2 shift "
        f"{sh13*100:.1f}% of their 3-sigma widths (s_12^2 ~7.0%, both <= ~10%)",
        sh12 <= 0.075 and sh13 <= 0.075)

# (A2) the NuFit-6.0 rectangle lies inside the region box B maps onto (landed Part-4 coverage)
for lab, rect in [('noSK', RECT_60_NOSK), ('SK', RECT_60_SK)]:
    chk(f"(A2-{lab}) NuFit-6.0 NO (s_12^2,s_13^2) rectangle lies inside the chamber box-B image region "
        f"[0.008,0.97]x[0.0005,0.121] (landed Part 4) -> the 6.0 inputs are in the forecast's covered domain",
        contains(BOXB_IMAGE['s12'], rect['s12']) and contains(BOXB_IMAGE['s13'], rect['s13']))

# (A3) HONEST CAVEAT (not a certificate): the landed box-Krawczyk certificate covers only the sub-boxes whose IMAGE
#      OVERLAPS the NuFit-5.3 rectangle (5404 overlapping, 996 skipped), NOT all of box B. This note does NOT re-run
#      the certificate over the 6.0 rectangle. So the band is taken AS the landed [251.86, 270] for the standing
#      assessment; band-stability under the ~7% input shift is an EXPECTATION, not a re-certified result.
band_recertified_here = False    # explicitly: the box-Krawczyk over the 6.0 rectangle is NOT re-run in this note
chk("(A3) [HONEST CAVEAT, not a certificate] band-stability under the ~7% input shift is EXPECTED but is NOT "
    "re-certified here: the landed certificate covers only NuFit-5.3-image-overlap sub-boxes (5404 of 6400; 996 "
    "skipped), not all of box B; a rigorous re-run over the 6.0 rectangle is left to a future iteration",
    band_recertified_here is False)

# ---------------------------------------------------------------------------------------------------
# (B) delta_CP STANDING vs NuFit-6.0 NO measured (comparator only)
# ---------------------------------------------------------------------------------------------------
# NuFit-6.0 NO delta_CP: best fit and 3-sigma range
DCP_60 = {'noSK': (177.0, (96.0, 422.0)), 'SK': (212.0, (124.0, 364.0))}
for lab, (bf, three_sig) in DCP_60.items():
    within3 = three_sig[0] <= BAND[0] and BAND[1] <= three_sig[1]
    bf_in_band = BAND[0] <= bf <= BAND[1]
    chk(f"(B-{lab}) band [251.86,270] is WITHIN the NuFit-6.0 NO 3-sigma range [{three_sig[0]},{three_sig[1]}] "
        f"(NOT excluded) but the best fit {bf} deg lies OUTSIDE the band (disfavored, not a match)",
        within3 and not bf_in_band)

# (B-contrast) under NuFit-5.3 the band sat near the T2K-favored upper region (~230-270): a favorable match.
dcp_53_band = (120.0, 369.0)   # NuFit-5.3 NO 3-sigma delta_CP band (X3'), centered ~230, T2K-driven toward ~270
chk("(B-contrast) under NuFit-5.3 the band sat inside [120,369] near the T2K-favored ~230-270 region "
    "(a favorable 7.3% sub-region match); under NuFit-6.0 the best fit moved to 177/212 -> standing DEGRADED "
    "from favorable to disfavored-but-allowed",
    BAND[0] >= dcp_53_band[0] and BAND[1] <= dcp_53_band[1])

# ---------------------------------------------------------------------------------------------------
# (C) theta_23 OCTANT: framework predicts s_23^2 > 0.5 (upper); NuFit-6.0 is SK-dependent
# ---------------------------------------------------------------------------------------------------
S23_60 = {'noSK': 0.561, 'SK': 0.470}
chk("(C1) framework predicts s_23^2 > 0.5 (upper octant); NuFit-6.0 no-SK = 0.561 -> UPPER (agrees)",
    S23_60['noSK'] > 0.5)
chk("(C2) NuFit-6.0 with-SK = 0.470 -> LOWER (disagrees) => the octant confirmation is now SK-DEPENDENT, "
    "not a clean prediction",
    S23_60['SK'] < 0.5 and (S23_60['noSK'] > 0.5) != (S23_60['SK'] > 0.5))

# ---------------------------------------------------------------------------------------------------
# (D) HONEST STANDING + falsifiability
# ---------------------------------------------------------------------------------------------------
# The forecast is robust/invariant as a prediction, but current data (NuFit-6.0) lean against it; DUNE/Hyper-K
# (~2031-32) sit at maximal-CP sensitivity (band at 270 = -90 deg) and will decisively confirm-or-exclude the band.
band_at_max_cp = abs(BAND[1] - 270.0) < 1e-6   # band upper edge = 270 = -90 deg = maximal CP, peak DUNE/HK sensitivity
chk("(D) the band's upper edge is 270 = -90 deg (maximal CP), exactly where DUNE/Hyper-K (~2031-32) have peak "
    "sensitivity (no insensitive-region escape hatch) -> decisively testable, but NuFit-6.0 currently leans AGAINST it",
    band_at_max_cp)

# ---------------------------------------------------------------------------------------------------
P = sum(1 for _, o in R if o)
Fa = sum(1 for _, o in R if not o)
for l, o in R:
    print(("PASS" if o else "FAIL"), "-", l)
print("\n%d PASS, %d FAIL" % (P, Fa))
if Fa:
    raise SystemExit(1)
print("""
RE-ASSESSMENT (PMNS delta_CP forecast under NuFit-6.0):
 - INPUT-STABLE FORECAST (not re-certified): the forecast consumes (s_12^2, s_13^2) and produces delta_CP; those
   inputs shifted by only ~7% of their width 5.3 -> 6.0 and remain inside the chamber box-B image region, so a large
   band shift is unlikely. CAVEAT: this note does NOT re-run the box-Krawczyk certificate over the 6.0 rectangle (the
   landed certificate covers only NuFit-5.3-image-overlap sub-boxes), so the band is taken AS the landed [251.86, 270].
 - DEGRADED STANDING: under NuFit-5.3 (T2K-driven, ~230-270 favored) the band looked like a tight 7.3% match; under
   NuFit-6.0 (best fit 177 no-SK / 212 with-SK, CP-conserving within ~1 sigma) the band is WITHIN 3-sigma (not
   excluded) but the best fit lies OUTSIDE it -> a forward bet current data DISFAVOR. (The "~1.5 sigma SK to ~2 sigma
   no-SK" is only a crude asymmetric-error yardstick, NOT a likelihood significance: the NO delta_CP likelihood is
   strongly non-Gaussian/wrapped and NO is consistent with CP conservation within 1 sigma.)
 - theta_23 OCTANT now SK-DEPENDENT: framework predicts upper (s_23^2 > 0.5); NuFit-6.0 gives 0.561 (no-SK, agrees)
   vs 0.470 (with-SK, disagrees). No longer a clean confirmation.
 - DUNE / Hyper-K (~2031-32) decisively test the band (it sits at maximal CP, peak sensitivity). The honest framing
   is "a sharp forward bet current data lean against, decisively testable by ~2031" -- NOT the stale NuFit-5.3
   "tight match". NuFit-6.0 is a comparator only; the band is the landed forecast taken as stated (not re-certified).
""")
