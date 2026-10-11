"""Independent arithmetic checks for the C4/RL2 referee.

This deliberately does not import rl2_core.  The operator moments, c2 values,
bare-ladder constants, fit sensitivities, and physical translation are
recomputed from the supplied local .npy artifact and closed-form Gaussian
integrals.
"""

from pathlib import Path
import math
import re

import numpy as np
from scipy.optimize import curve_fit
from scipy.special import digamma, gamma, gammaln


ROOT = Path(__file__).resolve().parent
A = math.pi / 24.0


def gaussian_moment(power):
    """Integral_0^inf s**power exp(-A*s**2) ds."""
    return 0.5 * A ** (-(power + 1.0) / 2.0) * gamma((power + 1.0) / 2.0)


def gaussian_log_moment(power):
    """Integral_0^inf s**power log(s) exp(-A*s**2) ds."""
    base = gaussian_moment(power)
    return 0.5 * base * (digamma((power + 1.0) / 2.0) - math.log(A))


def linear_functional(coeffs, power, with_log=False):
    total = 0.0
    for n, coeff in enumerate(coeffs):
        moment = gaussian_log_moment(power + 2 * n) if with_log else gaussian_moment(power + 2 * n)
        total += coeff * A**n / math.factorial(n) * moment
    return total


def ft0(coeffs):
    return math.pi / 2.0 * linear_functional(coeffs, 1, with_log=True)


def c2(coeffs):
    return -math.pi / 16.0 * linear_functional(coeffs, 2, with_log=True)


def bare_i1(coeffs):
    """Integral_0^inf u f(u**2)^2 du, evaluated term by term."""
    total = 0.0
    for i, ci in enumerate(coeffs):
        for j, cj in enumerate(coeffs):
            n = i + j
            integral = 0.25 * (2 * A) ** (-(n + 0.5)) * gamma(n + 0.5)
            total += ci * cj * A**n / (math.factorial(i) * math.factorial(j)) * integral
    return total


def parse_mean(mode):
    values = {op: {} for op in range(3)}
    for suffix in ("", "_smallp", "_tinyp"):
        text = (ROOT / f"rl2_A_{mode}{suffix}.out").read_text()
        for block in re.split(r"\n  p=", text)[1:]:
            p = float(block.split()[0])
            for op, value in re.findall(r"op(\d):.*?ratio/sqrt\(Delta\)=([\d.]+)", block):
                values[int(op)][p] = float(value)
    return values


def fit_three_models(p, m):
    fits = []
    fits.append(curve_fit(lambda x, m0, aa, bb: m0 + aa * np.sqrt(x) + bb * x, p, m)[0][0])
    fits.append(
        curve_fit(
            lambda x, m0, aa, alpha: m0 + aa * x**alpha,
            p,
            m,
            p0=[1.0, 1.0, 0.6],
            maxfev=20000,
        )[0][0]
    )
    fits.append(
        curve_fit(lambda x, m0, aa, bb: m0 + aa * np.sqrt(x) + bb * x * np.log(x), p, m)[0][0]
    )
    return np.asarray(fits)


def fit_sensitivity():
    print("\nMean-intercept sensitivity (three free-intercept ansatzes):")
    for mode in ("mid", "quarter"):
        data = parse_mean(mode)
        for op in range(3):
            p = np.asarray(sorted(data[op]))
            m = np.asarray([data[op][x] for x in p])
            tiny = fit_three_models(p[:4], m[:4])
            resolved = fit_three_models(p[2:6], m[2:6])
            print(
                f"  {mode:7s} op{op}: with p>=2.5e-4 {tiny} (mean {tiny.mean():.6f}); "
                f"with p>=1e-3 {resolved} (mean {resolved.mean():.6f})"
            )


def mc_slopes():
    print("\nRe-fitted fixed-source Monte Carlo slopes:")
    for op, eps, pred in (
        (0, 1.0, 2.488),
        (0, 0.5, 1.470),
        (0, 0.25, 0.868),
        (0, 0.125, 0.536),
        (1, 0.25, 0.904),
        (2, 0.25, 0.945),
    ):
        text = (ROOT / f"rl2_B_op{op}_eps{eps:g}.out").read_text()
        rows = re.findall(r"T=\s*([\d.]+).*?phi: mean=[-+.\deE]+ \+- [\d.eE+-]+ sd=([\d.eE+-]+)", text)
        t = np.asarray([float(row[0]) for row in rows])
        sd = np.asarray([float(row[1]) for row in rows])
        s4 = np.polyfit(t[-4:], np.log(sd[-4:]), 1)[0]
        s3 = np.polyfit(t[-3:], np.log(sd[-3:]), 1)[0]
        print(f"  op{op} eps={eps:g}: slopes {s4:.6f}, {s3:.6f}; ratios {s4/pred:.4f}, {s3/pred:.4f}")


def translation():
    lp = 1.616255e-35
    distance = 3.0857e25
    print("\nPhysical translation (k=2.84):")
    for label, extent in (("1.23e4", 1.23e4), ("3e6", 3e6), ("3e10", 3e10)):
        tau = math.sqrt(2 * distance * extent + extent**2)
        efolds = 2.84 * lp**2 * tau / (2 * 1e-19**3)
        needed = (2.84 * lp**2 * tau / 2) ** (1.0 / 3.0)
        print(f"  s={label} m: tau={tau:.9e}, n19={efolds:.9e}, lk={needed:.9e}")
    eps = (lp / 1e-19) ** 4
    alpha = 0.5 + math.log(1 / 323.0) / math.log(eps)
    print(f"  epsilon={eps:.9e}; alpha needed for a factor 323={alpha:.9f}")


def main():
    raw = np.load(ROOT / "RL1_F4b_stable_L6.npy")[:3]
    print("Closed-form operator checks from the local coefficient artifact:")
    for op, coeffs in enumerate(raw):
        normalization = 1.0 / ft0(coeffs)
        coeffs = coeffs * normalization
        moments = [linear_functional(coeffs, power) for power in range(4)]
        cc = c2(coeffs)
        ii = bare_i1(coeffs)
        print(
            f"  op{op}: renorm={normalization:.10f}; M0..M3={moments}; "
            f"c2={cc:.9f}; W={1/(2*math.pi*cc):.9f}; I1={ii:.9f}; k={math.sqrt(4*math.pi*ii):.9f}"
        )
    fit_sensitivity()
    mc_slopes()
    translation()


if __name__ == "__main__":
    main()
