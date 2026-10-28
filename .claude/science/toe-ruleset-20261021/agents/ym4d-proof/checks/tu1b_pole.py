#!/usr/bin/env python3
"""tu1b_pole.py -- repair run for criterion tu1b-D only (see checks/tu1b_criteria.md).
Imports the UNALTERED tu1_twisted.py and re-runs the pole ladder over six decades."""
from fractions import Fraction as Fr
import os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tu1_twisted as T

def main():
    corr, unco = [], []
    print("eps        max|b| corrected     max|b| uncorrected   residual(corrected)")
    for j in range(1, 7):
        e = Fr(1, 10 ** j)
        zz = (Fr(1) + e, Fr(5, 4), Fr(3, 7), Fr(7, 5))
        on = T.run_instance("on", 3, 4, zz, random.Random(777), quiet=True)
        off = T.run_instance("off", 3, 4, zz, random.Random(777), use_b1=False, quiet=True)
        corr.append(float(on["maxb"])); unco.append(float(off["maxb"]))
        print(f"1e-{j}    {corr[-1]:18.6g} {unco[-1]:20.6g} {on['bad']:12d}")
    ratios = [unco[i + 1] / unco[i] for i in range(len(unco) - 1)]
    print("\nsuccessive ratios (uncorrected):", " ".join(f"{r:.4f}" for r in ratios))
    vary = max(corr) / min(corr)
    print(f"corrected variation over six decades = {vary:.6g}")
    ok = all(r >= 9.0 for r in ratios) and ratios[-1] >= 9.9 and vary < 10
    print(f"tu1b-D : {'PASS' if ok else 'FAIL'}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
