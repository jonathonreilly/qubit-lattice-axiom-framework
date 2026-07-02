#!/usr/bin/env python3
"""W91 (reviewer-authored, codex unavailable) — the c_(0,0) lower bound for H_det.

H_det (Route B value side of the native discrete SU(3) half-line gap theorem)
needs a uniform analytic LOWER bound on c_(0,0)(beta), the denominator of
r_(p,q) = c_(p,q)/c_(0,0). W89 established the need and that positivity alone
gives no uniform constant (beta^(3/2) e^(-beta) c_(0,0) decreases). This note
DERIVES the lower bound.

c_(0,0)(beta) is the SINGLET coefficient of the Wilson single-plaquette
Boltzmann weight: by character orthogonality (normalized Haar measure,
integral dU = 1),

    c_(0,0)(beta) = E_Haar[ exp( (beta/3) Re Tr U ) ],  U in SU(3).

Re Tr U attains its UNIQUE maximum N_c = 3 at U = I (a strict, non-degenerate
maximum: near U = exp(iX), X in su(3) (8 real dims), Re Tr U = 3 - (1/2)|X|^2
+ O(|X|^4)). A Haar small-ball lower bound at U = I then gives

    c_(0,0)(beta) >= C_lower * e^beta * beta^(-(N_c^2-1)/2),
                  = C_lower * e^beta * beta^(-4)   for SU(3),

with C_lower > 0 a fixed small-ball constant (the SU(3) small-ball Haar
constant times e^-4 12^4 / 2). The power -(N_c^2-1)/2 = -4 is the
group-dimension Gaussian normalization. The witnessed prefactor
C = lim c_(0,0) beta^4 e^(-beta) ~ 14.85 is a numerical scale check, not the
load-bearing source of the analytic lower-bound constant.

DERIVATION OF THE LOWER BOUND (the Haar small-ball argument):
  c_(0,0) = E_Haar[exp((beta/3) Re Tr U)]
          >= exp((beta/3)(3 - eps)) * P_Haar(Re Tr U >= 3 - eps)   (restrict)
          = e^beta * e^(-beta eps/3) * P(eps).
  The event {Re Tr U >= 3 - eps} is {|X|^2 <= 2 eps + O(eps^2)} near U=I, an
  8-dimensional ball; its Haar measure P(eps) ~ c_8 eps^(8/2) = c_8 eps^4 as
  eps -> 0 (c_8 > 0 a fixed SU(3) Haar geometric constant). Choosing
  eps = 12/beta (so e^(-beta eps/3) = e^-4):
    c_(0,0) >= e^beta * e^-4 * (c_8/2) (12/beta)^4
            = [(c_8/2) e^-4 12^4] * e^beta * beta^(-4),
  for beta >= beta_0 (where the small-ball asymptotic holds with the 1/2 safety
  factor). This is the claimed lower bound; C_lower = (c_8/2) e^-4 12^4 > 0.

The runner (a) independently CHECKS the identification c_(0,0) = Haar average by
Monte Carlo at small beta, (b) witnesses the asymptotic form e^beta beta^(-4)
(c_(0,0) beta^4 e^(-beta) -> C ~ 14.85, power -4 = -(N_c^2-1)/2), and (c)
checks that a fixed grid constant C_GRID=8 holds on the sampled large-beta grid.
Nothing is fitted; C_GRID is not the analytic lower-bound constant.
"""
import importlib.util
import math
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_SRC = os.path.join(
    _HERE, "frontier_gauge_vacuum_plaquette_tensor_transfer_perron_solve.py"
)
_spec = importlib.util.spec_from_file_location("se_perron", _SRC)
se = importlib.util.module_from_spec(_spec)
sys.modules["se_perron"] = se
_spec.loader.exec_module(se)

N_C = 3
POWER = (N_C ** 2 - 1) / 2.0  # = 4 for SU(3); the group-dimension Gaussian power
C_GRID = 8.0  # non-load-bearing finite-grid witness (< witnessed C ~ 14.85)

PASS = 0
FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"{tag}: {name}")
    if detail:
        print(f"      {detail}")


def c00(beta, mode):
    return se.wilson_character_coefficient(0, 0, mode, beta / 3.0)


def haar_su3(rng):
    """A Haar-random SU(3) matrix (QR of complex Gaussian, det normalized)."""
    z = (rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))) / math.sqrt(2.0)
    q, r = np.linalg.qr(z)
    d = np.diagonal(r)
    ph = d / np.abs(d)
    q = q * ph  # fix QR phase ambiguity -> Haar on U(3)
    q = q / (np.linalg.det(q) ** (1.0 / 3.0))  # project to SU(3)
    return q


def main():
    # (a) IDENTIFICATION CHECK: c_00(beta) == E_Haar[exp((beta/3) Re Tr U)] at small beta.
    rng = np.random.default_rng(20260612)
    for beta in (6.0, 9.0):
        mc = np.mean(
            [
                math.exp((beta / 3.0) * np.trace(haar_su3(rng)).real)
                for _ in range(400000)
            ]
        )
        exact = c00(beta, 60)
        rel = abs(mc - exact) / exact
        check(
            f"identification c_00 = E_Haar[exp((beta/3)Re Tr U)] at beta={beta:.0f}",
            rel < 0.03,
            f"MC={mc:.5f} vs machinery c_00={exact:.5f} (rel {rel:.4f})",
        )

    # (b) ASYMPTOTIC FORM: c_00 beta^POWER e^(-beta) -> C ~ 14.85 (=> c_00 ~ C e^beta beta^-4).
    print("beta   c_00*beta^POWER*e^-beta  (-> C)")
    Cs = []
    for beta in (48, 96, 192, 384):
        mode = int(0.8 * beta) + 30
        lnc = math.log(c00(beta, mode))
        val = math.exp(lnc + POWER * math.log(beta) - beta)
        Cs.append(val)
        print(f"{beta:>5}   {val:>14.5f}")
    # power check: the scaled quantity converges (monotone, levelling) to C in [14, 16]
    check(
        f"c_00 ~ C e^beta beta^(-POWER), POWER = (N_c^2-1)/2 = {POWER:g}",
        all(14.0 < c < 16.0 for c in Cs)
        and all(Cs[i + 1] > Cs[i] for i in range(len(Cs) - 1))
        and (Cs[-1] - Cs[-2]) < (Cs[1] - Cs[0]),
        f"C estimates {[round(c, 3) for c in Cs]} converging upward to ~14.9",
    )
    # power is exactly -(N_c^2-1)/2: per-octave power -> POWER (using scaled-quantity flatness)
    powers = []
    for beta in (48, 96, 192, 384):
        mode = int(0.8 * beta) + 30
        powers.append(math.log(beta ** 1.5 * math.exp(-beta) * c00(beta, mode)))
    # slope of ln(beta^1.5 e^-b c00) vs ln beta -> -(POWER-1.5) = -5/2
    xs = [math.log(b) for b in (48, 96, 192, 384)]
    slope = np.polyfit(xs, powers, 1)[0]
    check(
        "measured power of beta^1.5 e^-beta c_00 is ~ -5/2 (=> c_00 power -4)",
        abs(slope + 2.5) < 0.05,
        f"slope = {slope:.4f} (target -2.5); c_00 power = {slope - 1.5:.3f} ~ -4",
    )

    # (c) Non-load-bearing finite-grid witness for the lower-bound scale.
    ok = True
    margins = []
    for beta in (48, 96, 192, 384):
        mode = int(0.8 * beta) + 30
        lnc = math.log(c00(beta, mode))
        ln_bound = math.log(C_GRID) + beta - POWER * math.log(beta)
        margins.append(lnc - ln_bound)  # > 0 means c_00 >= bound
        ok = ok and (lnc > ln_bound)
    check(
        f"grid witness c_00 >= C_grid e^beta beta^(-{POWER:g}) holds on sampled betas (C_grid={C_GRID:g})",
        ok,
        f"ln(c_00) - ln(grid bound) = {[round(m, 4) for m in margins]} (all > 0; finite-grid witness)",
    )
    check(
        "anti-fab: C_grid is a fixed finite-grid witness BELOW the observed asymptotic scale, not fitted",
        C_GRID < min(Cs),
        f"C_grid={C_GRID:g} < witnessed C~{min(Cs):.2f}; analytic C_lower remains the small-ball constant",
    )
    # FALSIFIER: wrong group-dimension power breaks the asymptotic form.
    wrong = math.exp(math.log(c00(192, 184)) + 3.0 * math.log(192) - 192)  # power 3 not 4
    check(
        "falsifier: wrong power (3 not (N_c^2-1)/2=4) does NOT give a stable O(1) constant",
        not (1.0 < wrong < 100.0) or wrong > 1e3,
        f"with power 3, scaled quantity = {wrong:.3e} (drifts; the correct power is 4)",
    )

    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
