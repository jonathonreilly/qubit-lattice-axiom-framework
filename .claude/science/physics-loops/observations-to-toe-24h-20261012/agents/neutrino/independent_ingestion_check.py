#!/usr/bin/env python3
"""Independent standard-library arithmetic and finite-difference controls.

This does not import the primary implementation. It checks input aggregation,
ratio uncertainty gradients, response normalization and the bad-kernel eigenvalue.
It does not add an experimental uncertainty model or statistical significance.
"""
from decimal import Decimal
import json
import math
from pathlib import Path

RUNTIME = Path("/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012/neutrino")
INPUTS = RUNTIME / "inputs"


def rows(name, max_columns=None):
    return [[Decimal(v) for v in line.split()[:max_columns]] for line in (INPUTS/name).read_text().splitlines()
            if line.strip() and not line.lstrip().startswith("#")]


def contrast(values):
    fl, fh, fr, nl, nh, nr = values
    return (fh/nh-fl/nl)*(nl+nh+nr)/(fl+fh+fr)


def main():
    result = json.loads((RUNTIME/"results.json").read_text())
    spectrum = [rows(f"DayaBay_IBDPromptSpectrum_EH{h}_3158days.txt", 6) for h in (1,2,3)]
    background = [rows(f"DayaBay_BackgroundSpectrum_EH{h}_3158days.txt") for h in (1,2,3)]
    masks = []
    for condition in (lambda a,b:a>=2 and b<=4, lambda a,b:a>=6 and b<=8,
                      lambda a,b:a>=2 and b<=8 and not(a>=2 and b<=4) and not(a>=6 and b<=8)):
        masks.append([i for i,row in enumerate(spectrum[0]) if condition(float(row[0]),float(row[1]))])
    total_candidates = sum(row[col] for hall in spectrum for row in hall for col in (3,4,5))
    assert float(total_candidates) == result["shape_audit"]["all_candidate_count_sum"]
    errors, value_errors = [], []
    for p, period in enumerate(("6AD","8AD","7AD")):
        groups, variances = [], []
        for halls in ((2,), (0,1)):
            for mask in masks:
                observed = sum(spectrum[h][i][3+p] for h in halls for i in mask)
                bkg = sum(background[h][26*p+i][3] for h in halls for i in mask)
                groups.append(float(observed-bkg)); variances.append(float(observed))
        value = contrast(groups)
        finite_variance = 0.
        for j in range(6):
            step = groups[j]*1e-5
            plus, minus = groups.copy(), groups.copy()
            plus[j] += step; minus[j] -= step
            derivative = (contrast(plus)-contrast(minus))/(2*step)
            finite_variance += derivative*derivative*variances[j]
        expected = result["shape_audit"]["periods"][period]["EH3_over_pooled_near"]
        value_errors.append(abs(value-expected["high_minus_low"]))
        errors.append(abs(math.sqrt(finite_variance)/expected["diagonal_count_proxy_error"]-1))
    matrix = rows("DayaBay_DetectorModel_Etrue_to_Eprompt.txt")
    matrix_total = sum(sum(row) for row in matrix)
    columns = [sum(row[j] for row in matrix) for j in range(len(matrix[0]))]
    assert abs(float(matrix_total)-result["response_audit"]["total"]) < 1e-14
    assert abs(float(max(columns))-result["response_audit"]["column_sum_max"]) < 1e-14
    assert max(value_errors) < 1e-13 and max(errors) < 1e-7
    a,b = math.exp(-.1),math.exp(-.9)
    independent_min_eigenvalue = (2+b-math.sqrt(b*b+8*a*a))/2
    expected_eigenvalue = result["channel_controls"]["invalid_pairwise_rate_counterexample"]["kernel_eigenvalues_at_L_0p1"][0]
    assert abs(independent_min_eigenvalue-expected_eigenvalue) < 1e-14
    print("INDEPENDENT CONTROL: decimal candidate sum =", total_candidates)
    print("INDEPENDENT CONTROL: decimal response total =", matrix_total)
    print("INDEPENDENT CONTROL: decimal largest column sum =", max(columns))
    print("INDEPENDENT CONTROL: grouped-statistic maximum central discrepancy =", max(value_errors))
    print("INDEPENDENT CONTROL: finite-difference proxy-error maximum relative discrepancy =", max(errors))
    print("INDEPENDENT CONTROL: closed-form bad-kernel eigenvalue =", independent_min_eigenvalue)
    print("All independent control assertions passed; no experimental significance computed.")


if __name__ == "__main__":
    main()
