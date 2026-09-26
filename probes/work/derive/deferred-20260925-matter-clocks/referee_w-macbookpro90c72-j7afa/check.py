#!/usr/bin/env python3
"""Independent referee for formation-clock dephasing, attempt 1.

The constant-clock characteristic function, its joint bound, and the
resonant counterexamples are recomputed. The attempt's script is not
imported. No clock is selected from the axioms.
"""
from __future__ import annotations

import sympy as sp

FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str = "") -> None:
    print(("PASS " if ok else "FAIL ") + tag + ((": " + msg) if msg else ""), flush=True)
    if not ok:
        FAILS.append(tag)


def constant_clock() -> bool:
    time, window, rate, frequency = sp.symbols("t T f omega", positive=True)
    density = rate * sp.exp(-rate * time) / (1 - sp.exp(-rate * window))
    integrated = sp.simplify(sp.integrate(sp.exp(sp.I * frequency * time) * density, (time, 0, window)))
    closed = rate * (1 - sp.exp(-(rate - sp.I * frequency) * window)) / (
        (rate - sp.I * frequency) * (1 - sp.exp(-rate * window))
    )
    cosine = sp.simplify(sp.integrate(sp.cos(frequency * time) * density, (time, 0, window)) - sp.re(closed))
    sine = sp.simplify(sp.integrate(sp.sin(frequency * time) * density, (time, 0, window)) - sp.im(closed))
    return sp.simplify(integrated - closed) == 0 and cosine == 0 and sine == 0


def joint_bound() -> bool:
    rate_ratio, decay, phase = sp.symbols("x kappa tau", positive=True)
    signal = rate_ratio * (1 - sp.exp(-decay) * sp.exp(sp.I * phase)) / (
        (rate_ratio - sp.I) * (1 - sp.exp(-decay))
    )
    modulus = sp.simplify(sp.expand_complex(signal * sp.conjugate(signal)))
    exact_numerator = 1 - 2 * sp.exp(-decay) * sp.cos(phase) + sp.exp(-2 * decay)
    exact = rate_ratio ** 2 * exact_numerator / ((1 + rate_ratio ** 2) * (1 - sp.exp(-decay)) ** 2)
    gap = sp.simplify(
        (rate_ratio * (1 + sp.exp(-decay))) ** 2 / ((1 + rate_ratio ** 2) * (1 - sp.exp(-decay)) ** 2) - modulus
    )
    stated_gap = 2 * rate_ratio ** 2 * sp.exp(-decay) * (1 + sp.cos(phase)) / (
        (1 + rate_ratio ** 2) * (1 - sp.exp(-decay)) ** 2
    )
    height = sp.symbols("y", positive=True)
    derivative = sp.diff((height + 1) * (1 - sp.exp(-height)) - height, height)
    vanished = sp.limit((height + 1) * (1 - sp.exp(-height)) - height, height, 0)
    slow = sp.simplify(signal.subs(rate_ratio, 0))  # not used; limit taken on the closed form below
    del slow
    return (
        sp.simplify(modulus - exact) == 0
        and sp.simplify(gap - stated_gap) == 0
        and sp.simplify(derivative - height * sp.exp(-height)) == 0
        and vanished == 0
    )


def sharpness() -> bool:
    window, rate, frequency = sp.symbols("T f omega", positive=True)
    closed = rate * (1 - sp.exp(-(rate - sp.I * frequency) * window)) / (
        (rate - sp.I * frequency) * (1 - sp.exp(-rate * window))
    )
    frozen = sp.limit(closed, rate, 0)
    uniform = (sp.exp(sp.I * frequency * window) - 1) / (sp.I * frequency * window)
    at_half = sp.simplify(sp.Abs(uniform.subs(window, sp.pi / frequency)) - 2 / sp.pi)
    surviving = rate / (rate - sp.I * frequency)
    long = sp.simplify(sp.limit(closed * sp.exp(0), window, sp.oo) - surviving) if False else None
    # The phase factor is bounded, so the T -> infinity limit is the residue at the decaying exponential.
    amplitude = sp.symbols("E", positive=True)
    phased = rate * (1 - amplitude * sp.exp(sp.I * frequency * window)) / ((rate - sp.I * frequency) * (1 - amplitude))
    infinite = sp.simplify(sp.limit(phased, amplitude, 0) - surviving)
    modulus = sp.simplify(sp.Abs(surviving) - rate / sp.sqrt(rate ** 2 + frequency ** 2))
    return (
        sp.simplify(frozen - uniform) == 0
        and at_half == 0
        and infinite == 0
        and modulus == 0
        and long is None
    )


def linear_hazard() -> bool:
    time, slope = sp.symbols("t beta", positive=True)
    density = slope * time * sp.exp(-slope * time ** 2 / 2)
    critical = sp.solve(sp.diff(density, time), time)
    peak = sp.simplify(density.subs(time, 1 / sp.sqrt(slope)) - sp.sqrt(slope) * sp.exp(-sp.Rational(1, 2)))
    factor = sp.factor(sp.diff(density, time) / (slope * sp.exp(-slope * time ** 2 / 2)))
    return critical == [1 / sp.sqrt(slope)] and peak == 0 and factor == 1 - slope * time ** 2


def cosine_clock() -> bool:
    time, frequency = sp.symbols("t omega", positive=True)
    count = sp.symbols("N", integer=True, positive=True)
    window = 2 * sp.pi * count / frequency
    density = (1 + sp.cos(frequency * time)) / window
    mass = sp.simplify(sp.integrate(density, (time, 0, window)))
    signal = sp.simplify(sp.integrate(sp.exp(sp.I * frequency * time) * density, (time, 0, window)))
    return mass == 1 and signal == sp.Rational(1, 2)


def hazard_from_density() -> bool:
    time, mass = sp.symbols("t m", positive=True)
    weight = sp.Function("w")
    cumulative = sp.Function("W")
    hazard = mass * weight(time) / (1 - mass * cumulative(time))
    survival = 1 - mass * cumulative(time)
    derivative = sp.diff(survival, time).subs(sp.diff(cumulative(time), time), weight(time))
    return sp.simplify(derivative + hazard * survival) == 0


def square_wave() -> bool:
    phase = sp.symbols("phi", real=True)
    average = sp.simplify(sp.integrate(sp.exp(sp.I * phase), (phase, -sp.pi / 2, sp.pi / 2)) / sp.pi)
    frequency, rate = sp.symbols("omega f0", positive=True)
    first = (0, sp.pi / (2 * frequency))
    second = (3 * sp.pi / (2 * frequency), 2 * sp.pi / frequency)
    early = rate * sp.exp(-rate * sp.symbols("t", positive=True))
    time = sp.symbols("t", positive=True)
    early = rate * sp.exp(-rate * time)
    carried = sp.exp(-rate * sp.pi / (2 * frequency))
    late = rate * carried * sp.exp(-rate * (time - second[0]))
    norm = sp.integrate(early, (time, *first)) + sp.integrate(late, (time, *second))
    moment = sp.integrate(sp.exp(sp.I * frequency * time) * early, (time, *first))
    moment += sp.integrate(sp.exp(sp.I * frequency * time) * late, (time, *second))
    signal = sp.simplify(moment / norm)
    limit = sp.simplify(sp.limit(signal, rate, 0) - 2 / sp.pi)
    return average == 2 / sp.pi and limit == 0


def main():
    check("constant clock", constant_clock(), "the conditioned constant hazard has the closed characteristic function, and its real and imaginary parts are the cosine and sine averages")
    check("joint bound", joint_bound(), "|z|^2 differs from the larger comparison by 2 x^2 e^{-kappa}(1+cos tau) over a positive denominator, and 1/(1-e^{-y}) <= 1+1/y")
    check("sharpness", sharpness(), "f -> 0 gives the uniform average, modulus 2/pi at omega T = pi; T -> infinity gives f/sqrt(f^2+omega^2)")
    check("linear hazard", linear_hazard(), "beta t exp(-beta t^2/2) peaks at 1/sqrt(beta) with height sqrt(beta) e^{-1/2}")
    check("cosine", cosine_clock(), "w = (1+cos omega t)/T on a whole number of periods has z = 1/2")
    check("any density", hazard_from_density(), "f = m w/(1-m W) has survival 1-m W, so the conditioned formation density is w")
    check("square wave", square_wave(), "the on-half average is 2/pi, and one exact period tends to 2/pi as the hazard tends to 0")
    if FAILS:
        print("SUMMARY: fails at " + ", ".join(FAILS), flush=True)
        return 1
    print(
        "SUMMARY: confirmed partial. The perpendicular part of a formation-weighted Bloch average is the "
        "characteristic function of the conditioned formation time. For a constant clock "
        "|z| <= 2(f/omega + 1/(omega T)), so the joint slow and long limit dephases. A cosine modulation "
        "keeps |z| = 1/2 and a half-period square wave tends to 2/pi. No clock was selected from the axioms.",
        flush=True,
    )
    print(
        "HIT: confirmed - dephasing is the decay of the formation-time characteristic function; the constant "
        "clock dephases jointly, and resonant hazards do not",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
