# f6c: evaluate amendment A1 of checks/f6_criteria.md (POST-HOC, labelled) on the STORED f6 values.
# Reads only checks/f6_out.txt; no f6 algebra is re-run.
import math, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
txt = open(os.path.join(HERE, "f6_out.txt")).read()

def ccov_closed(L2):
    return -(L2**2 - 1)**2 / (576.0 * L2**4 * (L2**2 + 1))

vals = {}  # (ell, kc) -> dict
for line in txt.splitlines():
    m = re.match(r"\s*l=(\d+):\s*(.*)", line)
    if not m:
        continue
    ell = int(m.group(1))
    for blk in m.group(2).split(";"):
        mk = re.search(r"kc=([\d.]+): it c=([-\d.]+) cM=([-\d.]+) cK=([-\d.]+) ccov=([-\d.]+) \| single c=([-\d.]+) "
                       r"cM=([-\d.]+) cK=([-\d.]+)", blk)
        if mk:
            kc = float(mk.group(1))
            vals[(ell, kc)] = dict(itK=float(mk.group(4)), ccov=float(mk.group(5)), sK=float(mk.group(8)))

W = 48 * math.pi**2
ells = (9, 15)
kcs = sorted({k for (_, k) in vals})
assert len(vals) == 6, vals
print("f6c: amendment A1 (POST-HOC) of checks/f6_criteria.md, on stored f6_out.txt values")
dev = max(abs(vals[(l, k)]["ccov"] - ccov_closed(l / 3)) for l in ells for k in kcs)
for l in ells:
    print(f"   ell={l}: c^cov_closed={ccov_closed(l/3):.6e}; stored c^cov={vals[(l, kcs[0])]['ccov']:.8f}")
print(f"[A1-cov] {'PASS' if dev <= 1e-8 else 'FAIL'} :: max |c^cov_f6 - c^cov_closed| = {dev:.2e} (<= 1e-8)")

def slope(a, b):
    return (b - a) / math.log(15 / 9) * W

okG = okH = True
for k in kcs:
    rK = [vals[(l, k)]["itK"] - ccov_closed(l / 3) for l in ells]
    rD = [vals[(l, k)]["itK"] - vals[(l, k)]["sK"] - ccov_closed(l / 3) for l in ells]
    sG, sH = slope(*rK), slope(*rD)
    okG &= abs(sG) <= 0.005
    okH &= abs(sH) <= 0.005
    print(f"   kc={k}: r^K(9)={rK[0]:+.3e} r^K(15)={rK[1]:+.3e} slope x48pi^2 {sG:+.5f}; "
          f"r^D(9)={rD[0]:+.3e} r^D(15)={rD[1]:+.3e} slope x48pi^2 {sH:+.5f}")
print(f"[A1-G] {'PASS' if okG else 'FAIL'} :: |s_rK(9,15)| x 48pi^2 <= 0.005 for each kc")
print(f"[A1-H] {'PASS' if okH else 'FAIL'} :: |s_rD(9,15)| x 48pi^2 <= 0.005 for each kc")
print("[A1-G'] NOT EVALUATED :: ell = 21 not run (not planned)")
# rounding of the 8-decimal printout: each stored value +-5e-9; r^D uses two stored values (+-1e-8), so a slope is
# uncertain by <= 2*1e-8/log(15/9)*48pi^2
print(f"   (printout rounding bound on any slope above: {2*1e-8/math.log(15/9)*W:.1e})")
