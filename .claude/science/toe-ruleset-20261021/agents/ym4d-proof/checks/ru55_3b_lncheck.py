# ru55_3b: corrected log-enclosure sanity check (criteria: checks/ru55_3b_criteria.md, written first).
import os, importlib.util
from fractions import Fraction as F
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("ru55_3_u1", os.path.join(HERE, "ru55_3_u1.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
l10 = m.ln_enc(10)
l2 = m.ln_enc(2)
l54 = m.ln_enc(F(5, 4))
W10 = (F(2302585092994045684017, 10 ** 21), F(2302585092994045684018, 10 ** 21))
W2 = (F(693147180559945309417, 10 ** 21), F(693147180559945309418, 10 ** 21))
L1 = W10[0] <= l10[0] and l10[1] <= W10[1] and (l10[1] - l10[0]) < F(1, 10 ** 30)
alt = (3 * l2[0] + l54[0], 3 * l2[1] + l54[1])
ov = (max(alt[0], l10[0]), min(alt[1], l10[1]))
L2 = ov[0] <= ov[1] and (ov[1] - ov[0]) < F(1, 10 ** 30)
L3 = W2[0] <= l2[0] and l2[1] <= W2[1]
sh = (l10[0] + F(1, 10 ** 20), l10[1] + F(1, 10 ** 20))
L4 = W10[0] <= sh[0] and sh[1] <= W10[1]
print(f"L1 ln10 enclosure inside [..684017, ..684018] and width<1e-30: {L1} (width {float(l10[1] - l10[0]):.1e})")
print(f"L2 3ln2+ln(5/4) overlaps ln10 enclosure, overlap width<1e-30: {L2}")
print(f"L3 ln2 enclosure inside [..309417, ..309418]: {L3}")
print(f"L4 (designed FAIL) shifted enclosure inside the window: {L4} -> {'FAILS (as designed)' if not L4 else 'CONTROL DOES NOT FIRE'}")
print(f"VERDICT: {'log enclosures CERTIFIED; ru55_3 verdicts stand with K4 replaced by L1-L4' if (L1 and L2 and L3 and not L4) else 'NOT certified'}")
