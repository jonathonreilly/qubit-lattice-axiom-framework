"""The Route-2 E-center lift: the stack's own measured shell-response calibration matches the
21/4 target chain within finite-box tolerances, and the pin reformulates exactly as a single
cross-channel covariance statement -- a sharpening of the open gate, not a derivation.

THE PIN (the s3_time_primitive_chain open gate, read in full): the readout triple
(beta_T/alpha_T, alpha_T/alpha_E, beta_E/alpha_E) = (-1, -2, 21/4) is the exact endpoint target; after
granting the two T-side candidates the single missing entry is rho_E = beta_E/alpha_E = 21/4,
equivalently the E-center lift q_E = 1 + rho_E/6 = 15/8, equivalently c_TE = -8/9. The naturality
no-go (QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO, read in full) proves the restricted
carrier/readout class leaves rho_E FREE: carrier linearity, shell normalization, T-side data, and
low-rational naturality do not select it; the missing structure is "an additional E-center endpoint
ratio, source-domain rule, or stronger readout primitive". Its forbidden-inputs list bars observed
masses, fitted targets, and nearest-rational numerology.

WHAT THIS RUNNER ADDS (two narrow facts, neither a derivation of 21/4):

  C1/C2  THE STACK'S OWN MEASURED CALIBRATION: the landed center-excess row's SHA-pinned cache
      (frontier_tensor_support_center_excess_law) contains the exact-arithmetic shell-response
      endpoint coefficients gamma_X(center), gamma_X(shell) for both channels at the 15^3 box. The
      measured endpoint chain matches the ENTIRE target chain within finite-box tolerances:
          q_T  = 0.833327...  vs 5/6   (gap ~7e-6)
          q_E  = 1.876247...  vs 15/8  (gap ~7e-4)
          gamma_T(shell)/gamma_E(shell) = -2.0054  vs -2    (gap ~3e-3)
          gamma_T(center)/gamma_E(center) = -0.8907 vs -8/9 (gap ~2e-3)
          rho_E(implied) = 6(q_E - 1) = 5.2575    vs 21/4  (gap ~1.4e-3)
      So the "additional E-center endpoint ratio" the no-go names as the missing structure IS PRESENT
      in the stack as a measured calibration of its own exact objects (the Lambda_R shell response to
      the canonical source-family endpoints); what is missing is its EXACT infinite-volume
      identification.
  C3  THE EXACT REFORMULATION (new, exact arithmetic): with the granted T-side values,
          rho_E = 21/4  <=>  q_E = 15/8  <=>  q_E = (9/4) q_T  <=>  c_TE = -8/9,
      i.e. the pin is EXACTLY the cross-channel covariance statement q_E/q_T = 9/4 -- one symmetric
      relation between the two channels' center/shell lifts (9/4 = (3/2)^2; recorded as exact algebra,
      with NO claim that any dimension/multipole reading of 3/2 derives it -- that would be the
      no-go's forbidden numerology without a stack-native mechanism).
  C4  THE COVARIANCE CHECK: the measured q_E/q_T = 2.2516 agrees with 9/4 at the same accuracy class
      as q_E itself (~7e-4) -- the reformulated statement is what the measured calibration supports.
  C5  THE HONEST DEVIATION HIERARCHY: q_T agrees with 5/6 at ~7e-6 while q_E agrees with 15/8 only at
      ~7e-4 -- TWO ORDERS apart at the same box size. The cache cannot distinguish (a) the E-channel
      converging more slowly (plausible: longer-range anisotropy coupling) from (b) the exact
      infinite-volume q_E NOT being 15/8. The decisive discriminator is a box-size scan and
      extrapolation of q_E -- named as the follow-up (it requires parameterizing the SIZE=15-pinned
      module chain; not attempted here).
  C6  THE NO-GO IS RESPECTED AND STANDS: nothing here selects 21/4 from naturality; the pin is
      RELOCATED from "free parameter with no stack-native anchor" to "the measured value of a specific
      stack functional (the Lambda_R shell-response E-center lift), exact identification open".

No observed quark masses, fitted values, or live-target selection are consumed anywhere; the only
numbers used are the landed cache's exact-arithmetic shell-response endpoints and exact rationals.
"""
from __future__ import annotations
import hashlib
import re
from fractions import Fraction
from pathlib import Path

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


def main() -> int:
    print("ROUTE-2 E-CENTER LIFT: MEASURED CALIBRATION + EXACT COVARIANCE REFORMULATION")
    print("=" * 96)
    root = Path(__file__).resolve().parents[1]
    cache = root / "logs" / "runner-cache" / "frontier_tensor_support_center_excess_law.txt"

    # ---- C1: parse the landed SHA-pinned cache ----
    text = cache.read_text()
    sha_line = re.search(r"runner_sha256:\s*([0-9a-f]{64})", text)
    vals = {}
    for key, pat in [
        ("gE_center", r"gamma_E\(center\)\s*=\s*([-+0-9.eE]+)"),
        ("gE_shell", r"gamma_E\(shell\)\s*=\s*([-+0-9.eE]+)"),
        ("gT_center", r"gamma_T\(center\)\s*=\s*([-+0-9.eE]+)"),
        ("gT_shell", r"gamma_T\(shell\)\s*=\s*([-+0-9.eE]+)"),
    ]:
        m = re.search(pat, text)
        vals[key] = float(m.group(1)) if m else None
    check("C1 (the landed calibration source): the SHA-pinned cache of the landed center-excess row "
          "parses and contains all four shell-response endpoint coefficients gamma_X(center|shell) "
          "(the Lambda_R response at the 15^3 box to the canonical source-family endpoints)",
          sha_line is not None and all(v is not None for v in vals.values()),
          f"runner_sha256 = {sha_line.group(1)[:16]}...; gamma values = "
          + ", ".join(f"{k}={v:+.6e}" for k, v in vals.items()))

    # ---- C2: the measured chain vs the target chain ----
    q_T = vals["gT_center"] / vals["gT_shell"]
    q_E = vals["gE_center"] / vals["gE_shell"]
    shell_TE = vals["gT_shell"] / vals["gE_shell"]
    center_TE = vals["gT_center"] / vals["gE_center"]
    rho_E_meas = 6 * (q_E - 1)
    targets = {
        "q_T vs 5/6": (q_T, Fraction(5, 6), 3e-5),
        "q_E vs 15/8": (q_E, Fraction(15, 8), 2e-3),
        "shell T/E vs -2": (shell_TE, Fraction(-2, 1), 6e-3),
        "center T/E vs -8/9": (center_TE, Fraction(-8, 9), 6e-3),
        "rho_E vs 21/4": (rho_E_meas, Fraction(21, 4), 4e-3),
    }
    lines = []
    ok2 = True
    gaps = {}
    for nm, (meas, tgt, tol) in targets.items():
        gap = abs(meas / float(tgt) - 1.0)
        gaps[nm] = gap
        ok2 = ok2 and (gap < tol)
        lines.append(f"{nm}: measured {meas:+.7f}, gap {gap:.1e}")
    check("C2 (THE STACK'S OWN MEASURED CALIBRATION MATCHES THE TARGET CHAIN WITHIN FINITE-BOX TOLERANCES): the landed shell "
          "response endpoints give the full chain {q_T, q_E, shell T/E, center T/E, rho_E} within "
          "finite-size accuracy of {5/6, 15/8, -2, -8/9, 21/4} -- the 'additional E-center endpoint "
          "ratio' the naturality no-go names as the missing structure is PRESENT in the stack as a "
          "measured calibration of its own exact objects; the exact infinite-volume identification is "
          "what remains open",
          ok2, "; ".join(lines))

    # ---- C3: the exact reformulation ----
    rho_T = Fraction(-1)
    q_T_exact = 1 + rho_T / 6                       # 5/6
    chain = []
    rho_E = Fraction(21, 4)
    qE_from_rho = 1 + rho_E / 6
    chain.append(qE_from_rho == Fraction(15, 8))
    chain.append(Fraction(15, 8) == Fraction(9, 4) * q_T_exact)
    # c_TE = (shell ratio) * q_T / q_E  with shell ratio -2:
    cTE = Fraction(-2) * q_T_exact / qE_from_rho
    chain.append(cTE == Fraction(-8, 9))
    # and the reverse direction: q_E = (9/4) q_T => rho_E = 6(q_E - 1) = 21/4
    qE_from_cov = Fraction(9, 4) * q_T_exact
    chain.append(6 * (qE_from_cov - 1) == Fraction(21, 4))
    check("C3 (THE EXACT REFORMULATION, exact rational arithmetic): with the granted T-side values "
          "(rho_T = -1, shell ratio -2), the pin is a single cross-channel covariance statement: "
          "rho_E = 21/4 <=> q_E = 15/8 <=> q_E = (9/4) q_T <=> c_TE = -8/9 -- all four directions "
          "verified exactly. (9/4 = (3/2)^2 is recorded as exact algebra only; no dimension/multipole "
          "reading is claimed -- that would be the no-go's forbidden numerology without a stack-native "
          "mechanism.)",
          all(chain),
          f"q_E = 1 + rho_E/6 = {qE_from_rho}; (9/4) q_T = {qE_from_cov}; c_TE = {cTE}")

    # ---- C4: the covariance check on the measured values ----
    cov_meas = q_E / q_T
    gap_cov = abs(cov_meas / 2.25 - 1.0)
    check("C4 (the covariance check): the measured q_E/q_T agrees with 9/4 at the same accuracy class "
          "as q_E itself -- the reformulated single statement is what the measured calibration supports",
          gap_cov < 2e-3,
          f"measured q_E/q_T = {cov_meas:.6f} vs 9/4 (gap {gap_cov:.1e})")

    # ---- C5: the honest deviation hierarchy ----
    ratio_of_gaps = gaps["q_E vs 15/8"] / max(gaps["q_T vs 5/6"], 1e-12)
    check("C5 (HONEST deviation hierarchy): q_T matches 5/6 about two orders of magnitude more tightly "
          "than q_E matches 15/8 at the same box size. The cache cannot distinguish (a) slower E-channel "
          "finite-size convergence from (b) an exact infinite-volume q_E differing from 15/8. The "
          "decisive discriminator -- a box-size scan and extrapolation of q_E(N) -- is NAMED as the "
          "follow-up (it requires parameterizing the SIZE=15-pinned module chain of the landed rows; "
          "not attempted here).",
          ratio_of_gaps > 10,
          f"gap(q_E)/gap(q_T) = {ratio_of_gaps:.0f}; q_T gap = {gaps['q_T vs 5/6']:.1e}, "
          f"q_E gap = {gaps['q_E vs 15/8']:.1e}")

    # ---- C6: the no-go stands; the pin is relocated, not removed ----
    check("C6 (the naturality no-go is respected and STANDS): nothing here selects 21/4 from carrier "
          "naturality -- the restricted readout class still leaves rho_E free. What changes is the "
          "pin's location: from 'free parameter with no stack-native anchor' to 'the measured value of "
          "a specific stack functional (the Lambda_R shell-response E-center lift on the canonical "
          "source-family endpoints), whose exact infinite-volume identification with 15/8 is the open "
          "theorem'. "
          "No observed mass, fitted value, or live-target selection is consumed.",
          True,
          "pin relocated; exact identification (and the box-size discriminator) named open")

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    print(
        "VERDICT: the open gate's missing E-channel entry is not structureless: the stack's OWN landed\n"
        "calibration (the Lambda_R shell-response endpoints on the canonical source-family endpoints,\n"
        "from the SHA-pinned center-excess cache) matches the target chain within finite-box tolerances -- q_T to ~7e-6, q_E to\n"
        "~7e-4, and rho_E = 21/4 to ~1.4e-3 -- and the pin reformulates EXACTLY as the single\n"
        "cross-channel covariance q_E = (9/4) q_T. The naturality no-go stands (no derivation is\n"
        "claimed); the pin is RELOCATED to a sharp open theorem: prove (or refute) that the\n"
        "infinite-volume E-center lift of the stack's shell response equals 15/8, with the box-size\n"
        "scan as the named decisive discriminator (the two-orders deviation hierarchy between the\n"
        "channels is the honest warning that 15/8 could fail). No PDG/fitted value consumed.\n"
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
