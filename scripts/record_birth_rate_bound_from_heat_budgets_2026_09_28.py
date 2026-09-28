#!/usr/bin/env python3
"""Birth-rate bound: how often can a sharp one-site record be born, given the heat budgets of matter and of empty space?

Pre-registered by the second panel's strategy lens (2026-09-28, recorded in
the viability map). Arithmetic only; the observational inputs are reference
inputs, not framework content.

Inputs:
- Framework (the record-cost note, T4(g) and T4): the cheapest sharp
  site-local record in the walker sea costs 1.19 hop energies (a particle
  placed at one site); a sharp lock of one site costs 2.39.
- Bridge (supplied, as in the member note): a hop costs hbar c / a.
- Spacings: a = 1e-19 m (an illustrative coarse spacing) and a = l_P.
- Heat budgets (reference inputs): Earth's mean internal heat production,
  about 7e-12 W/kg (radiogenic plus secular cooling, of order 1e-11 W/kg);
  the cosmic energy density today, about 6e-10 J/m^3 (critical density times
  c^2), over the Hubble time, about 4.4e17 s.
- For comparison (reference only): collapse-model localisation rates, GRW
  lambda = 1e-16 per nucleon per second, 6e26 nucleons per kg.

Pre-registered criterion: sharp births "survive" only if the budgets allow at
least one birth per kg per second in matter (placement: next to existing
records) AND at least one per cubic metre per Hubble time in empty space
(placement: anywhere). Prediction: fails.

Checks:
A. In matter: allowed births per kg per second at both spacings (< 1: fails).
B. In empty space: allowed births per cubic metre per second, and per lattice
   site per Hubble time (far below 1).
C. Against collapse-model rates: GRW-rate sharp births would heat matter by
   many orders of magnitude more than Earth's budget, at both spacings.
D. Soft births survive only as coarse, macroscopic records: the record-cost
   note's T6(b) cost of a Gaussian record of width R and resolution sigma is
   0.415 R/sigma^2 hop energies. At collapse-model rates and GRW's width
   (1e-7 m), Earth's budget requires sigma >= 3e13 units of content at
   a = 1e-19 m (blind to single particles, but fine for a macroscopic pointer,
   whose positions differ by ~1e23 units) and sigma >= 2e29 at the Planck
   spacing (too coarse even for a pointer).

Prints one line per check, the N5 resolution lines and `TOTAL: PASS=N FAIL=M`.
"""
import math

AUDIT_TIMEOUT_SEC = 900

PASS = FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}", flush=True)


HBAR_C = 1.973269804e-7      # eV m
EV = 1.602176634e-19         # J
L_P = 1.616255e-35           # m
COST_PARTICLE, COST_LOCK = 1.19, 2.39   # hop energies (record-cost note)
EARTH_HEAT = 7e-12           # W/kg (reference input)
RHO_COSMIC = 6e-10           # J/m^3 (reference input)
T_HUBBLE = 4.4e17            # s (reference input)
GRW_RATE = 1e-16 * 6e26      # localisations per kg per s (reference only)

rows = {}
for label, a in (("a = 1e-19 m", 1e-19), ("a = l_P", L_P)):
    hop_J = HBAR_C / a * EV
    birth_J = COST_PARTICLE * hop_J
    rows[label] = dict(hop_eV=HBAR_C / a, birth_J=birth_J,
                       matter=EARTH_HEAT / birth_J,
                       space=RHO_COSMIC / (birth_J * T_HUBBLE),
                       per_site=RHO_COSMIC / birth_J * a ** 3,
                       grw_heat=GRW_RATE * birth_J)

check("A: in ordinary matter, the heat budget allows far fewer than one sharp site-local birth per kg per second at either spacing (the pre-registered test fails)",
      all(r["matter"] < 1 for r in rows.values()),
      "; ".join(f"{k}: hop {r['hop_eV']:.2e} eV, birth {r['birth_J']:.2e} J, allowed {r['matter']:.1e} per kg per s" for k, r in rows.items()))
check("B: in empty space, the cosmic energy budget allows at most a tiny birth rate: per lattice site, far below one birth in the age of the universe",
      all(r["per_site"] < 1e-20 for r in rows.values()),
      "; ".join(f"{k}: {r['space']:.1e} per m^3 per s, {r['per_site']:.1e} per site over a Hubble time" for k, r in rows.items()))
check("C: sharp births at collapse-model rates would out-heat Earth's budget by many orders of magnitude at either spacing",
      all(r["grw_heat"] / EARTH_HEAT > 1e10 for r in rows.values()),
      "; ".join(f"{k}: {r['grw_heat']:.1e} W/kg, {r['grw_heat'] / EARTH_HEAT:.0e} times Earth's" for k, r in rows.items()))

R_GRW = 1e-7  # m, collapse-model localisation width (reference only)
soft = {}
for label, a in (("a = 1e-19 m", 1e-19), ("a = l_P", L_P)):
    hop_J = HBAR_C / a * EV
    allowed_cost_hops = EARTH_HEAT / GRW_RATE / hop_J     # hop energies per birth allowed at GRW rates
    R_sites = R_GRW / a
    soft[label] = (allowed_cost_hops, R_sites, math.sqrt(0.415 * R_sites / allowed_cost_hops))
check("D: soft births survive only as coarse records: at collapse-model rates and width 1e-7 m the heat budget allows single-particle resolution at neither spacing; "
      "macroscopic records (differences of ~1e23 units) survive at a = 1e-19 m, not at the Planck spacing",
      all(v[2] > 1e10 for v in soft.values()) and soft["a = 1e-19 m"][2] < 1e23 < soft["a = l_P"][2],
      "; ".join(f"{k}: allowed cost {v[0]:.1e} hops per birth, width {v[1]:.1e} sites, minimal resolution sigma {v[2]:.1e}" for k, v in soft.items()))

print("per_element: checked and not executed - arithmetic on the record-cost note's per-record costs; no operator is built here.")
print("per_site: the cost per site-local birth is taken from the record-cost note (1.19 hop energies), not recomputed here.")
print("per_mode: checked and not executed - no mode sums; the sea costs come from the record-cost note's zone integrals.")
print("per_block: checked and not executed - no finite block; budgets are per kilogram and per cubic metre (reference inputs).")
print("lattice_wide: rates are bounded for whole bodies (per kg) and for empty space (per m^3, per site per Hubble time), at two spacings.")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
