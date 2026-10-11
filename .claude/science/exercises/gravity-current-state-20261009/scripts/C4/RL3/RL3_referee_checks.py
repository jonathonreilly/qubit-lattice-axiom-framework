"""Independent arithmetic and finite-toy checks for the RL3 referee report.

This does not import the worker's Python modules.  It uses only the stored H
arrays for the reported window integrals.  The Poisson check is a separate
one-hop toy calculation of the thinning/chaos identity.
"""

import math

import numpy as np
from scipy.special import gammaln


COEFFICIENTS = np.array([1.3, -0.8, 0.5, -0.2])


def f_derivative(order, volume):
    """d^order/dvolume^order of exp(-volume) sum C_j volume^j/j!."""
    total = 0.0
    for j, coefficient in enumerate(COEFFICIENTS):
        for q in range(min(order, j) + 1):
            falling = math.factorial(j) / math.factorial(j - q)
            total += (
                math.comb(order, q)
                * (-1.0) ** (order - q)
                * coefficient
                * falling
                * volume ** (j - q)
                / math.factorial(j)
            )
    return math.exp(-volume) * total


def g_value(n, epsilon):
    """Sum C_j Binom(n,j;epsilon), evaluated in log form."""
    total = 0.0
    for j, coefficient in enumerate(COEFFICIENTS):
        if n >= j:
            log_probability = (
                gammaln(n + 1)
                - gammaln(j + 1)
                - gammaln(n - j + 1)
                + j * math.log(epsilon)
                + (n - j) * math.log1p(-epsilon)
            )
            total += coefficient * math.exp(log_probability)
    return total


def poisson_variance(epsilon, volume):
    mean = volume / epsilon
    nmax = int(mean + 14.0 * math.sqrt(mean + 1.0) + 100.0)
    ns = np.arange(nmax + 1)
    log_probabilities = -mean + ns * math.log(mean) - gammaln(ns + 1)
    probabilities = np.exp(log_probabilities)
    values = np.array([g_value(int(n), epsilon) for n in ns])
    expectation = np.sum(probabilities * values)
    variance = np.sum(probabilities * (values - expectation) ** 2)
    return expectation, variance


def chaos_variance(epsilon, volume, kmax=200):
    terms = []
    for k in range(1, kmax + 1):
        term = epsilon**k * volume**k / math.factorial(k) * f_derivative(k, volume) ** 2
        terms.append(term)
        if k > 20 and term < 1e-18 * max(sum(terms), 1e-300):
            break
    return sum(terms), len(terms)


def check_one_hop_chaos():
    # General p-thinning does not have nonnegative p-independent Taylor
    # coefficients: for F=1[N=0], Var F=e^(-pV)-e^(-2pV), whose p^2
    # coefficient is -3V^2/2.  The following checks the special tuned
    # binomial-smearing identity used by RL3, not a generic thinning theorem.
    volume = 0.73
    print("one-hop thinning/chaos identity, volume=0.73")
    print("  generic-thinning counterexample p^2 coefficient for 1[N=0] = %.8f" % (-1.5 * volume**2))
    for epsilon in (0.8, 0.3, 0.07, 0.01):
        expectation, direct_variance = poisson_variance(epsilon, volume)
        series_variance, terms = chaos_variance(epsilon, volume)
        expected_mean = f_derivative(0, volume)
        print(
            "  eps=%g mean_error=%+.3e variance_direct=%.12e "
            "variance_series=%.12e relative_error=%.3e terms=%d"
            % (
                epsilon,
                expectation - expected_mean,
                direct_variance,
                series_variance,
                abs(series_variance - direct_variance) / direct_variance,
                terms,
            )
        )


def integrate_trapezoid(x, y, mask=None):
    if mask is None:
        mask = np.ones_like(x, dtype=bool)
    return np.trapezoid(np.where(mask, y, 0.0), x)


def check_constants():
    print("stored-H quadrature")
    for operator in range(3):
        data = np.load("rl3_H_op%d.npz" % operator)
        tau, response = data["taus"], data["H"]
        integrand = tau * response**2
        full = integrate_trapezoid(tau, integrand)
        for label, mask in (
            ("absH>=0.3", np.abs(response) >= 0.3),
            ("tau<=0.6", tau <= 0.6),
        ):
            window = integrate_trapezoid(tau, integrand, mask)
            print(
                "  op%d %-10s I=%.8f c_low=sqrt(pi I)=%.8f"
                % (operator, label, window, math.sqrt(math.pi * window))
            )
        print("  op%d full       I=%.8f c_star=sqrt(4 pi I)=%.8f" % (operator, full, math.sqrt(4.0 * math.pi * full)))


def check_translation():
    planck_length = 1.616255e-35
    distance = 3.0857e25
    source_size = 1.2e4
    locality_bar = 1e-19
    proper_time = math.sqrt(2.0 * distance * source_size + source_size**2)
    epsilon = (planck_length / locality_bar) ** 4
    dimensionless_exponent = math.sqrt(epsilon) * proper_time / locality_bar
    threshold = 2.0 / dimensionless_exponent
    print("translation arithmetic")
    print(
        "  tau=%.12e epsilon=%.12e sqrt(eps)*tau/lk=%.12f c_fail=%.12f"
        % (proper_time, epsilon, dimensionless_exponent, threshold)
    )
    for constant in (0.7171, 1.1759, 1.5214, 2.7317, 3.2526):
        sd_efolds = 0.5 * constant * dimensionless_exponent
        needed = (0.5 * constant * planck_length**2 * proper_time) ** (1.0 / 3.0)
        print("  c=%.4f sd_efolds=%.6f lk_needed=%.12e" % (constant, sd_efolds, needed))


if __name__ == "__main__":
    check_one_hop_chaos()
    check_constants()
    check_translation()
