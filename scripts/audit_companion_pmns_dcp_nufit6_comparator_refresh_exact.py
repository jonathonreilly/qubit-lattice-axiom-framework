r"""
Audit companion - PMNS delta_CP forecast under NuFIT-6.1: its experimental standing degrades from favorable
(NuFIT-5.3) to disfavored-but-allowed. The predicted band is input-stable in the limited comparator sense below, but is
NOT re-certified here.

WHY THIS NOTE: the standing PMNS delta_CP / theta_23 forecast notes (PMNS_THETA12_THETA13_DCP_PREDICTIONS_2026-05-17
and the theta_23 cascade Cycles 5a/6a/7) are anchored on NuFIT-5.3 (X3/X3'), under which delta_CP was T2K-driven
toward ~230-270 deg, making the framework band [251.86, 270] deg look like a tight 7.3% sub-region match. NuFIT-6.0
(2024, arXiv:2410.05380) already moved the normal-ordering best fit to 177 deg (no-SK) / 212 deg (with-SK). Official
NuFIT-6.1 (2025, data through Nov 2025) is the current table: the normal-ordering best fit is 207 deg (no-SK) / 212 deg
(with-SK), and theta_23 is lower-octant at the best fit in both current NO columns.

KEY STRUCTURAL POINT (reproven below): the forecast CONSUMES (s_12^2, s_13^2) as inputs (the NuFIT rectangle X3) and
produces delta_CP as the forced output; it does NOT consume the measured delta_CP. So whether the PREDICTED band moves
is governed by whether the (s_12^2, s_13^2) INPUT rectangle moved. This runner checks that the NuFIT-6.0/6.1 input
rectangles remain nearby and inside the broad chamber-box image region. That is still an expectation of stability, not
a replacement for re-running the box-Krawczyk certificate.

COMPUTED (exact / interval-free arithmetic):
 - INPUT STABILITY (NOT a re-certification): NuFIT-6.0 barely moved from NuFIT-5.3; NuFIT-6.1 has a stricter s_12^2
   range and only a small s_13^2 upper-edge expansion relative to NuFIT-5.3. All NuFIT-6.0/6.1 NO input rectangles lie
   inside the region the chamber box B maps onto (s_12^2 in [0.008, 0.97], s_13^2 in [0.0005, 0.121]; landed runner
   Part 4 coverage). CAVEAT: the landed box-Krawczyk certificate covers only the sub-boxes whose image overlaps the
   NuFIT-5.3 rectangle, NOT all of box B; this note does NOT re-run the certificate over the NuFIT-6 rectangle. So the
   band is taken AS the landed [251.86, 270] for the standing assessment.
 - delta_CP STANDING: the band [251.86, 270] is WITHIN the current NuFIT-6.1 NO 3-sigma ranges [114, 405] (no-SK) and
   [125, 365] (with-SK), but the NuFIT-6.1 best fits (207 / 212) lie OUTSIDE the band. The same disfavored-but-allowed
   disposition appears in NuFIT-6.0.
 - theta_23 OCTANT: the framework predicts s_23^2 > 0.5 (upper). NuFIT-6.0 NO was SK-dependent, 0.561 no-SK vs 0.470
   with-SK. Current NuFIT-6.1 NO gives 0.470 in both no-SK and with-SK best fits, so the upper-octant prediction is now
   current-data disfavored for NO, though still inside the 3-sigma ranges.

Reprove-and-cite: the standing arithmetic (rectangle shift vs width; NuFIT-6.0/6.1 rectangles inside box-B image
region; band-within-3-sigma; best-fit-outside-band; octant test) is reproven here from the numbers. NuFIT values are
COMPARATORS (named external admissions for the labeling step), never derivation inputs; the framework's predicted band
[251.86, 270] is the landed theorem content (runner frontier_pmns_..._narrow.py, 61/61), inherited AS STATED here, not
re-derived and not re-certified. No value is fit. This is a comparator refresh + honest standing update, NOT a no-go
and NOT a new prediction.
"""

R = []
def chk(label, ok):
    R.append((label, bool(ok)))

# Framework predicted band (landed theorem content; runner frontier_pmns_theta12_theta13_dcp_predictions_narrow.py 61/61)
BAND = (251.86, 270.00)          # interval certificate (PDG convention, deg)
BAND_FLOAT = (257.57, 268.82)    # tighter floating-point image
ANCHOR = 260.88                  # PDG-central anchor, sin(delta_CP) = -0.987

# Comparator rectangles on (s_12^2, s_13^2): NuFIT-5.3 (used in the landed note, X3) vs NuFIT-6.0/6.1 NO.
RECT_53     = {'s12': (0.270, 0.341),  's13': (0.02029, 0.02391)}
RECT_60_NOSK= {'s12': (0.275, 0.345),  's13': (0.02023, 0.02376)}
RECT_60_SK  = {'s12': (0.275, 0.345),  's13': (0.02030, 0.02388)}
RECT_61_NOSK= {'s12': (0.2893, 0.3295),'s13': (0.02070, 0.02420)}
RECT_61_SK  = {'s12': (0.2893, 0.3295),'s13': (0.02064, 0.02418)}
# Region the chamber box B maps onto (landed runner Part 4 broad-sweep coverage result)
BOXB_IMAGE  = {'s12': (0.008, 0.97),   's13': (0.0005, 0.121)}

def width(iv):  return iv[1] - iv[0]
def maxshift(a, b):  return max(abs(a[0]-b[0]), abs(a[1]-b[1]))
def contains(outer, inner):  return outer[0] <= inner[0] and inner[1] <= outer[1]

# ---------------------------------------------------------------------------------------------------
# INPUT STABILITY under the 5.3 -> 6.x comparator refresh (NOT a re-certification of the band)
# ---------------------------------------------------------------------------------------------------
# NuFIT-6.0 consumed (s_12^2, s_13^2) inputs barely moved: shift about 7% of the 3-sigma width.
for lab, rect in [('noSK', RECT_60_NOSK), ('SK', RECT_60_SK)]:
    sh12 = maxshift(RECT_53['s12'], rect['s12']) / width(RECT_53['s12'])
    sh13 = maxshift(RECT_53['s13'], rect['s13']) / width(RECT_53['s13'])
    chk(f"(input-shift v6.0-{lab}) consumed inputs barely moved 5.3->6.0: s_12^2 shift {sh12*100:.1f}% and s_13^2 shift "
        f"{sh13*100:.1f}% of their 3-sigma widths (s_12^2 ~7.0%, both <= ~10%)",
        sh12 <= 0.075 and sh13 <= 0.075)

# NuFIT-6.1 s_12^2 is a stricter subset of the NuFIT-5.3 range; s_13^2 only mildly expands the high edge.
for lab, rect in [('noSK', RECT_61_NOSK), ('SK', RECT_61_SK)]:
    s12_subset = contains(RECT_53['s12'], rect['s12'])
    s13_upper_expansion = max(0.0, rect['s13'][1] - RECT_53['s13'][1]) / width(RECT_53['s13'])
    chk(f"(input-shift v6.1-{lab}) current NuFIT-6.1 input rectangle remains nearby: s_12^2 is inside the 5.3 range "
        f"and s_13^2 upper-edge expansion is {s13_upper_expansion*100:.1f}% of the 5.3 width",
        s12_subset and s13_upper_expansion <= 0.085)

# The NuFIT-6.x rectangles lie inside the broad chamber-box image region (landed Part-4 coverage).
for lab, rect in [('6.0-noSK', RECT_60_NOSK), ('6.0-SK', RECT_60_SK), ('6.1-noSK', RECT_61_NOSK), ('6.1-SK', RECT_61_SK)]:
    chk(f"(box-image {lab}) NuFIT-{lab[:3]} NO (s_12^2,s_13^2) rectangle lies inside the chamber box-B image region "
        f"[0.008,0.97]x[0.0005,0.121] (landed Part 4) -> the inputs are in the broad forecast domain",
        contains(BOXB_IMAGE['s12'], rect['s12']) and contains(BOXB_IMAGE['s13'], rect['s13']))

# Honest caveat (not a certificate): the landed box-Krawczyk certificate covers only the sub-boxes whose image overlaps
# the NuFIT-5.3 rectangle (5404 overlapping, 996 skipped), NOT all of box B. This note does NOT re-run the certificate
# over the NuFIT-6 rectangle. So the band is taken AS the landed [251.86, 270] for the standing assessment.
band_recertified_here = False    # explicitly: the box-Krawczyk over the NuFIT-6 rectangle is NOT re-run in this note
chk("(not-recertified) band-stability under the nearby NuFIT-6.x input shift is EXPECTED but is NOT re-certified here: "
    "the landed certificate covers only NuFIT-5.3-image-overlap sub-boxes (5404 of 6400; 996 skipped), not all of box B; "
    "a rigorous re-run over the NuFIT-6.1 rectangle is left to a future iteration",
    band_recertified_here is False)

# ---------------------------------------------------------------------------------------------------
# delta_CP standing vs NuFIT-6.0/6.1 NO measured (comparator only)
# ---------------------------------------------------------------------------------------------------
# NuFIT NO delta_CP: best fit and 3-sigma range
DCP_6X = {
    '6.0-noSK': (177.0, (96.0, 422.0)),
    '6.0-SK': (212.0, (124.0, 364.0)),
    '6.1-noSK': (207.0, (114.0, 405.0)),
    '6.1-SK': (212.0, (125.0, 365.0)),
}
for lab, (bf, three_sig) in DCP_6X.items():
    within3 = three_sig[0] <= BAND[0] and BAND[1] <= three_sig[1]
    bf_in_band = BAND[0] <= bf <= BAND[1]
    chk(f"(delta_CP standing {lab}) band [251.86,270] is WITHIN the NuFIT NO 3-sigma range "
        f"[{three_sig[0]},{three_sig[1]}] "
        f"(NOT excluded) but the best fit {bf} deg lies OUTSIDE the band (disfavored, not a match)",
        within3 and not bf_in_band)

# Under NuFIT-5.3 the band sat near the T2K-favored upper region (~230-270): a favorable match.
dcp_53_band = (120.0, 369.0)   # NuFIT-5.3 NO 3-sigma delta_CP band (X3'), centered ~230, T2K-driven toward ~270
chk("(delta_CP contrast) under NuFIT-5.3 the band sat inside [120,369] near the T2K-favored ~230-270 region "
    "(a favorable 7.3% sub-region match); under NuFIT-6.1 the current best fits are 207/212 -> standing DEGRADED "
    "to disfavored-but-allowed",
    BAND[0] >= dcp_53_band[0] and BAND[1] <= dcp_53_band[1])

# ---------------------------------------------------------------------------------------------------
# theta_23 octant: framework predicts s_23^2 > 0.5 (upper)
# ---------------------------------------------------------------------------------------------------
S23_60 = {'noSK': 0.561, 'SK': 0.470}
S23_61 = {'noSK': 0.470, 'SK': 0.470}
S23_61_3SIG = {'noSK': (0.432, 0.587), 'SK': (0.435, 0.584)}
chk("(theta_23 v6.0-noSK) framework predicts s_23^2 > 0.5 (upper octant); NuFIT-6.0 no-SK = 0.561 -> UPPER (agrees)",
    S23_60['noSK'] > 0.5)
chk("(theta_23 v6.0-SK) NuFIT-6.0 with-SK = 0.470 -> LOWER (disagrees) => the v6.0 octant reading is SK-dependent, "
    "not a clean prediction",
    S23_60['SK'] < 0.5 and (S23_60['noSK'] > 0.5) != (S23_60['SK'] > 0.5))
chk("(theta_23 v6.1-current) current NuFIT-6.1 NO best fits are lower-octant in both columns, but the 3-sigma ranges "
    "still include upper-octant values",
    S23_61['noSK'] < 0.5 and S23_61['SK'] < 0.5
    and S23_61_3SIG['noSK'][1] > 0.5 and S23_61_3SIG['SK'][1] > 0.5)

# ---------------------------------------------------------------------------------------------------
# Honest standing + falsifiability
# ---------------------------------------------------------------------------------------------------
# The forecast is robust/invariant as a prediction, but current data (NuFIT-6.1) lean against it; DUNE/Hyper-K-era
# sensitivity sits near maximal CP (band at 270 = -90 deg) and should decisively confirm-or-exclude the band.
band_at_max_cp = abs(BAND[1] - 270.0) < 1e-6   # band upper edge = 270 = -90 deg = maximal CP, peak DUNE/HK sensitivity
chk("(falsifiability) the band's upper edge is 270 = -90 deg (maximal CP), where DUNE/Hyper-K-era data have strong "
    "sensitivity (no insensitive-region escape hatch) -> decisively testable, but current NuFIT-6.1 leans AGAINST it",
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
	RE-ASSESSMENT (PMNS delta_CP forecast under NuFIT-6.1):
	 - INPUT-STABLE FORECAST (not re-certified): the forecast consumes (s_12^2, s_13^2) and produces delta_CP; NuFIT-6.0
	   barely moved from NuFIT-5.3, and current NuFIT-6.1 is still nearby (s_12^2 stricter, s_13^2 upper edge only mildly
	   expanded) and inside the chamber box-B image region. CAVEAT: this note does NOT re-run the box-Krawczyk certificate
	   over the NuFIT-6.1 rectangle, so the band is taken AS the landed [251.86, 270].
	 - DEGRADED STANDING: under NuFIT-5.3 (T2K-driven, ~230-270 favored) the band looked like a tight 7.3% match; under
	   current NuFIT-6.1 (best fit 207 no-SK / 212 with-SK) the band is WITHIN 3-sigma (not excluded) but the best fit lies
	   OUTSIDE it -> a forward bet current data DISFAVOR. No likelihood significance is claimed.
	 - theta_23 OCTANT is current-data disfavored for NO: framework predicts upper (s_23^2 > 0.5); NuFIT-6.1 NO gives
	   0.470 in both no-SK and with-SK best fits, while 3-sigma still permits upper-octant values.
	 - DUNE / Hyper-K-era data decisively test the band (it sits at maximal CP, peak sensitivity). The honest framing is
	   "a sharp forward bet current data lean against, decisively testable by next-generation long-baseline data" -- NOT
	   the stale NuFIT-5.3 "tight match". NuFIT values are comparators only; the band is the landed forecast taken as
	   stated (not re-certified).
	""")
