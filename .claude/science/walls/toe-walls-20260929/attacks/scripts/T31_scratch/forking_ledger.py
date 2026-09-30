"""T31 Test B: forking-paths ledger for v = M * pref * alpha^N (pre-registered family in PREREG.md).
p_LEE(tau) = measure of log-targets in [50,1000] GeV lying within +/-tau of SOME family member (N free 1..40).
"""
import math, itertools, json
import os
P = float(os.environ.get('PLAQ', 0.5934))
u0 = P ** 0.25
ab = 1 / (4 * math.pi)
COUP = {"alpha_bare": ab, "alpha_LM": ab / u0, "alpha_s=ab/u0^2": ab / u0**2, "ab/u0^4": ab / u0**4}
MPL = {"M_Pl=1.2209e19": 1.2209e19, "M_red=2.435e18": 2.435e18}

def A(Lt):
    s = sum(1 / (3 + math.sin((2 * n + 1) * math.pi / Lt) ** 2) for n in range(Lt))
    return s / (2 * Lt * u0**2)
A2 = A(2)
ENDP = {2: A2 / A(2), 4: A2 / A(4), 6: A2 / A(6), 8: A2 / A(8), "inf": math.sqrt(3) / 2}
PREF = {}
for k, r in ENDP.items():
    PREF[f"Lt={k},root4"] = r ** 0.25
    PREF[f"Lt={k},root16"] = r ** (1 / 16)
TARGET_FACTORS = {"v=246.22": 1.0, "v/sqrt2": math.sqrt(2)}  # member value compared to target*: member*c = target

def members(pref_keys, coup_keys, mpl_keys, tgt_keys):
    out = []
    for pk, ck, mk, tk in itertools.product(pref_keys, coup_keys, mpl_keys, tgt_keys):
        out.append((pk, ck, mk, tk))
    return out

def value(mem, N):
    pk, ck, mk, tk = mem
    return MPL[mk] * PREF[pk] * COUP[ck] ** N * TARGET_FACTORS[tk]

def plee(mems, tau, lo=50.0, hi=1000.0, Nmax=40):
    ivs = []
    for mem in mems:
        for N in range(1, Nmax + 1):
            lv = math.log(value(mem, N))
            ivs.append((lv - tau, lv + tau))
    a, b = math.log(lo), math.log(hi)
    ivs = [(max(x, a), min(y, b)) for x, y in ivs if y > a and x < b]
    ivs.sort()
    tot = 0.0; cur_s = None; cur_e = None
    for x, y in ivs:
        if cur_e is None or x > cur_e:
            if cur_e is not None:
                tot += cur_e - cur_s
            cur_s, cur_e = x, y
        else:
            cur_e = max(cur_e, y)
    if cur_e is not None:
        tot += cur_e - cur_s
    return tot / (b - a)

F160 = members(PREF.keys(), COUP.keys(), MPL.keys(), TARGET_FACTORS.keys())
FMIN = members([k for k in PREF if k.endswith("root4")], ["alpha_bare", "alpha_LM"], ["M_Pl=1.2209e19"], ["v=246.22"])
# a third, "as published" family: only the endpoint choice and the exponent are free (the lane's own discrete axis)
FLANE = members([k for k in PREF if k.endswith("root4")], ["alpha_LM"], ["M_Pl=1.2209e19"], ["v=246.22"])
print("family sizes:", len(F160), len(FMIN), len(FLANE))
res = {"P": P, "sizes": [len(F160), len(FMIN), len(FLANE)], "plee": {}}
for tau in (0.00026, 0.002, 0.004, 0.005, 0.01):
    row = [plee(F, tau) for F in (F160, FMIN, FLANE)]
    res["plee"][str(tau)] = row
    print(f"tau=+/-{tau*100:.3f}%   p_LEE F160={row[0]:.4f}  Fmin={row[1]:.4f}  Flane={row[2]:.4f}")

# which members hit the actual target 246.22 (with target factor 1 => member value directly, or /sqrt2 => 174.10)
print("\nMembers hitting the real target, any N (|dev| <= 1%):")
hits = []
for mem in F160:
    for N in range(1, 41):
        v = value(mem, N)  # member value * c, to be compared with 246.22
        dev = v / 246.22 - 1
        if abs(dev) <= 0.01:
            hits.append((abs(dev), mem, N, v))
hits.sort()
for d, mem, N, v in hits[:12]:
    print(f"  dev={100*(v/246.22-1):+.3f}%  N={N:2d}  {mem}  v={v:.3f}")
res["n_hits_1pct"] = len(hits)
res["hits_within"] = {str(t): sum(1 for h in hits if h[0] <= t) for t in (0.00026, 0.002, 0.004, 0.005, 0.01)}
print("hit counts within tau:", res["hits_within"])
# with the unquenched-plaquette sensitivity: a shift dP moves the natural member by -4 dP/P
json.dump(res, open(f"forking_ledger_result_P{P}.json", "w"), indent=1)
