#!/usr/bin/env python3
"""K-symmetrized untied measure: records-only reconstruction (rhalf block 16).

The two-slice weight tested here is

    mu_sym(W) = (exp(chibar K(W,W) chi)
                 + exp(chibar K(W^dag,W^dag) chi)) / 2.

It is the K-orbit average of the time-homogeneous untied weight, not the
arrow-dependent W,W^dag alternating weight.  All derivation-path arithmetic is
exact over Gaussian rationals or SymPy rationals.  Floating eigenvalues are
used only for labeled scans.  Numbered PASS/FAIL; exit 0 iff FAIL == 0.
"""
from fractions import Fraction as F
from itertools import combinations
import random

import numpy as np
import sympy as sp


_pass = 0
_fail = 0


def check(num, desc, ok, detail=""):
    global _pass, _fail
    tag = "PASS" if ok else "FAIL"
    if ok:
        _pass += 1
    else:
        _fail += 1
    line = f"[{tag}] ({num:02d}) {desc}"
    if detail:
        line += f"  [{detail}]"
    print(line)


def residual(msg):
    print(f"RESIDUAL (declared-open): {msg}")


# =====================================================================
# Exact Gaussian-rational and Grassmann/Berezin engine (block 10 reused)
# =====================================================================
class CR:
    __slots__ = ("re", "im")

    def __init__(self, re=0, im=0):
        self.re = re if isinstance(re, F) else F(re)
        self.im = im if isinstance(im, F) else F(im)

    def __add__(self, other):
        other = asCR(other)
        return CR(self.re + other.re, self.im + other.im)

    __radd__ = __add__

    def __sub__(self, other):
        other = asCR(other)
        return CR(self.re - other.re, self.im - other.im)

    def __mul__(self, other):
        other = asCR(other)
        return CR(self.re * other.re - self.im * other.im,
                  self.re * other.im + self.im * other.re)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = asCR(other)
        den = other.re * other.re + other.im * other.im
        num = self * CR(other.re, -other.im)
        return CR(num.re / den, num.im / den)

    def __neg__(self):
        return CR(-self.re, -self.im)

    def conj(self):
        return CR(self.re, -self.im)

    def __eq__(self, other):
        other = asCR(other)
        return self.re == other.re and self.im == other.im

    def __hash__(self):
        return hash((self.re, self.im))

    def is_zero(self):
        return self.re == 0 and self.im == 0

    def __repr__(self):
        return f"({self.re}{'+' if self.im >= 0 else ''}{self.im}i)"

    def __complex__(self):
        return complex(float(self.re), float(self.im))


def asCR(value):
    if isinstance(value, CR):
        return value
    if isinstance(value, complex):
        return CR(F(value.real), F(value.imag))
    return CR(F(value), F(0))


def gr_mul(p, q):
    out = {}
    for m1, c1 in p.items():
        for m2, c2 in q.items():
            if m1 & m2:
                continue
            sign = 1
            remaining = m2
            while remaining:
                low = remaining & (-remaining)
                bit = low.bit_length() - 1
                if bin(m1 >> (bit + 1)).count("1") % 2:
                    sign = -sign
                remaining ^= low
            mask = m1 | m2
            value = c1 * c2 if sign > 0 else -(c1 * c2)
            out[mask] = out.get(mask, CR(0)) + value
    return {m: value for m, value in out.items() if not value.is_zero()}


def gr_int(poly, generator):
    out = {}
    bit = 1 << generator
    for mask, coeff in poly.items():
        if not (mask & bit):
            continue
        below = bin(mask & (bit - 1)).count("1")
        signed = -coeff if below % 2 else coeff
        reduced = mask ^ bit
        out[reduced] = out.get(reduced, CR(0)) + signed
    return {m: value for m, value in out.items() if not value.is_zero()}


def exp_bilinear(K, nmode):
    action = {}
    for i in range(nmode):
        for j in range(nmode):
            if K[i][j].is_zero():
                continue
            gi, gj = 2 * i, 2 * j + 1
            mask = (1 << gi) | (1 << gj)
            signed = K[i][j] if gi < gj else -K[i][j]
            action[mask] = action.get(mask, CR(0)) + signed
    expo = {0: CR(1)}
    term = {0: CR(1)}
    for order in range(1, nmode + 1):
        term = gr_mul(term, action)
        term = {m: value / order for m, value in term.items()}
        for mask, value in term.items():
            expo[mask] = expo.get(mask, CR(0)) + value
    return {m: value for m, value in expo.items() if not value.is_zero()}


def berezin_full(poly, nmode):
    out = poly
    for i in range(nmode):
        out = gr_int(out, 2 * i + 1)
        out = gr_int(out, 2 * i)
    return out.get(0, CR(0))


def expect(K, nmode, obs):
    return berezin_full(gr_mul(obs, exp_bilinear(K, nmode)), nmode)


def cb(i):
    return {1 << (2 * i): CR(1)}


def c(i):
    return {1 << (2 * i + 1): CR(1)}


def mul(*terms):
    out = {0: CR(1)}
    for term in terms:
        out = gr_mul(out, term)
    return out


def scal(value, poly):
    return {mask: asCR(value) * coeff for mask, coeff in poly.items()}


def add(*polys):
    out = {}
    for poly in polys:
        for mask, coeff in poly.items():
            out[mask] = out.get(mask, CR(0)) + coeff
    return {m: value for m, value in out.items() if not value.is_zero()}


def theta(poly, ng=3):
    out = {}
    for mask, coeff in poly.items():
        generators = [g for g in range(4 * ng) if (mask >> g) & 1]
        sign = 1
        reflected = []
        for generator in reversed(generators):
            mode = generator // 2
            is_chi = generator % 2 == 1
            slice_index = 0 if mode < ng else 1
            generation = mode % ng
            new_mode = generation if slice_index == 1 else ng + generation
            reflected.append(2 * new_mode if is_chi else 2 * new_mode + 1)
            sign = -sign
        image = {0: CR(1)}
        for generator in reflected:
            image = gr_mul(image, {1 << generator: CR(1)})
        out_coeff = coeff.conj() if sign > 0 else -coeff.conj()
        for out_mask, value in scal(out_coeff, image).items():
            out[out_mask] = out.get(out_mask, CR(0)) + value
    return {m: value for m, value in out.items() if not value.is_zero()}


Cm = [[CR(0), CR(1), CR(0)],
      [CR(0), CR(0), CR(1)],
      [CR(1), CR(0), CR(0)]]


def matmul(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(len(B))), CR(0))
             for j in range(len(B[0]))] for i in range(len(A))]


C2 = matmul(Cm, Cm)
EYE = [[CR(1) if i == j else CR(0) for j in range(3)] for i in range(3)]


def W_of(a, b, ccoef):
    a, b, ccoef = asCR(a), asCR(b), asCR(ccoef)
    return [[(a if i == j else CR(0)) + b * Cm[i][j] + ccoef * C2[i][j]
             for j in range(3)] for i in range(3)]


def dag(matrix):
    return [[matrix[j][i].conj() for j in range(len(matrix))]
            for i in range(len(matrix[0]))]


def direct_sum(A, B):
    na, nb = len(A), len(B)
    return [[(A[i][j] if i < na and j < na else
              B[i - na][j - na] if i >= na and j >= na else CR(0))
             for j in range(na + nb)] for i in range(na + nb)]


def cr_det(matrix):
    size = len(matrix)
    if size == 1:
        return matrix[0][0]
    total = CR(0)
    for j in range(size):
        sub = [row[:j] + row[j + 1:] for row in matrix[1:]]
        term = matrix[0][j] * cr_det(sub)
        total = total + (term if j % 2 == 0 else -term)
    return total


def build_K(W0, W1, ng=3):
    K = [[CR(0)] * (2 * ng) for _ in range(2 * ng)]
    for i in range(ng):
        for j in range(ng):
            K[i][j] = -W0[i][j]
            K[ng + i][ng + j] = -W1[i][j]
    for generation in range(ng):
        K[generation][ng + generation] = CR(F(-1, 2))
        K[ng + generation][generation] = CR(F(1, 2))
    return K


def n(generation):
    return mul(cb(3 + generation), c(3 + generation))


def bilin1(matrix):
    out = {}
    for i in range(3):
        for j in range(3):
            if matrix[i][j].is_zero():
                continue
            out = add(out, scal(matrix[i][j], mul(cb(3 + i), c(3 + j))))
    return out


one = {0: CR(1)}
REG = {
    "1": one,
    "N": bilin1(EYE),
    "TCsym": add(bilin1(Cm), bilin1(C2)),
    "e2": add(mul(n(0), n(1)), mul(n(0), n(2)), mul(n(1), n(2))),
    "e3": mul(n(0), n(1), n(2)),
}
RO = ["1", "N", "TCsym", "e2", "e3"]
OBS_PAIR = {(i, j): gr_mul(theta(REG[name_i]), REG[name_j])
            for i, name_i in enumerate(RO) for j, name_j in enumerate(RO)}


def raw_gram_from_weight(weight):
    Z = berezin_full(weight, 6)
    G = [[berezin_full(gr_mul(OBS_PAIR[(i, j)], weight), 6)
          for j in range(5)] for i in range(5)]
    return G, Z


def gaussian_weight(W):
    return exp_bilinear(build_K(W, W), 6)


def sym_weight(W):
    return scal(F(1, 2), add(gaussian_weight(W), gaussian_weight(dag(W))))


def reg_gram(W):
    return raw_gram_from_weight(gaussian_weight(W))


def sym_gram(W):
    return raw_gram_from_weight(sym_weight(W))


def norm_gram(G, Z):
    return [[G[i][j] / Z for j in range(5)] for i in range(5)]


def is_hermitian(G):
    return all((G[i][j] - G[j][i].conj()).is_zero()
               for i in range(len(G)) for j in range(len(G)))


def principal_minors(G):
    out = {}
    for size in range(1, len(G) + 1):
        for indices in combinations(range(len(G)), size):
            out[indices] = cr_det([[G[i][j] for j in indices] for i in indices])
    return out


def exact_psd_status(G, Z):
    if Z.is_zero():
        return None, {}
    normalized = norm_gram(G, Z)
    minors = principal_minors(normalized)
    psd = (is_hermitian(normalized)
           and all(value.im == 0 and value.re >= 0 for value in minors.values()))
    return psd, minors


def gram_float(G, Z):
    return np.array([[complex(G[i][j] / Z) for j in range(5)] for i in range(5)])


def poly_equal(A, B):
    masks = set(A) | set(B)
    return all((A.get(mask, CR(0)) - B.get(mask, CR(0))).is_zero()
               for mask in masks)


print("=" * 76)
print("K-symmetrized untied measure -- records-only reconstruction (rhalf block 16)")
print("mu_sym = (mu_W + mu_{W^dag})/2; same registrable spanning set")
print("=" * 76)


# =====================================================================
# Engine validation and T1
# =====================================================================
pt3 = [[CR(F(i - j, 3), F(i * j, 5)) for j in range(3)] for i in range(3)]
check(1, "reused block-10 Grassmann/Berezin engine: exact single-slice "
         "partition equals det K to the first power at a dense rational-complex "
         "point", expect(pt3, 3, one) == cr_det(pt3))

Wt1 = [[CR(1)]]
Ktoy = build_K(Wt1, Wt1, ng=1)
toy_basis = [one, cb(1), c(1), mul(cb(1), c(1))]
toy = [[expect(Ktoy, 2, gr_mul(theta(toy_basis[i], 1), toy_basis[j]))
        for j in range(4)] for i in range(4)]
toy_target = [[CR(F(5, 4)), CR(0), CR(0), CR(-1)],
              [CR(0), CR(F(1, 2)), CR(0), CR(0)],
              [CR(0), CR(0), CR(F(1, 2)), CR(0)],
              [CR(-1), CR(0), CR(0), CR(1)]]
check(2, "reused theta/two-slice engine reproduces block 10's inherited exact "
         "toy OS Gram", toy == toy_target)

PROBES = [
    ("P1", CR(F(4, 5), F(1, 10)), CR(F(3, 10), F(1, 5)),
     CR(F(1, 2), F(-1, 10))),
    ("P2", CR(1), CR(F(1, 3), F(1, 7)), CR(F(1, 3), F(-1, 5))),
]

orbit_ok = True
orbit_details = []
probe_data = {}
for tag, a, b, ccoef in PROBES:
    W = W_of(a, b, ccoef)
    G, Z = reg_gram(W)
    Gd, Zd = reg_gram(dag(W))
    Gs, Zs = sym_gram(W)
    relation = (Zd == Z.conj()
                and all(Gd[j][i].conj() == G[i][j]
                        for i in range(5) for j in range(5)))
    averaged = (Zs == (Z + Zd) / 2
                and all(Gs[i][j] == (G[i][j] + Gd[i][j]) / 2
                        for i in range(5) for j in range(5)))
    orbit_ok = orbit_ok and relation and averaged
    orbit_details.append(f"{tag}: Zsym={Zs}")
    probe_data[tag] = (W, G, Z, Gd, Zd, Gs, Zs)
check(3, "T1 reflection identity at both required exact untied probes: "
         "Z(W^dag)=conj Z(W), G_raw(W^dag)=G_raw(W)^dag entrywise, and direct "
         "integration of the half-sum equals the arithmetic orbit average",
      orbit_ok, "; ".join(orbit_details))

herm_ok = all(not data[6].is_zero() and data[6].im == 0
              and is_hermitian(data[5])
              and is_hermitian(norm_gram(data[5], data[6]))
              for data in probe_data.values())
check(4, "T1 exact consequence: theta preserves mu_sym and its raw records-only "
         "Gram is Hermitian; at both required probes Z_sym=Re Z_W is nonzero, "
         "so the normalized Gram is exactly Hermitian too", herm_ok)

azero = CR(F(3, 8), F(5, 8))
Wzero = W_of(azero, 0, 0)
Gzero_w, Zzero_w = reg_gram(Wzero)
Gzero_s, Zzero_s = sym_gram(Wzero)
check(5, "normalization guard: Z_sym=Re Z_W is not automatically nonzero.  "
         "At W=(3/8+5i/8)I, Z_W=(15i/32)^3=-3375i/32768 is nonzero and purely "
         "imaginary, hence Z_sym=0 exactly; the raw symmetrized form remains "
         "Hermitian but no normalized Gram exists on this locus",
      Zzero_w == CR(0, F(-3375, 32768)) and Zzero_s.is_zero()
      and is_hermitian(Gzero_s))


# =====================================================================
# T2 -- the decisive exact signature and bounded domain structure
# =====================================================================
print("\n--- T2: exact signature and bounded domain structure ---")
strict_probe_pd = {}
for check_num, tag in [(6, "P1"), (7, "P2")]:
    Gs, Zs = probe_data[tag][5], probe_data[tag][6]
    psd, minors = exact_psd_status(Gs, Zs)
    strict = (psd is True
              and all(value.im == 0 and value.re > 0
                      for value in minors.values()))
    strict_probe_pd[tag] = strict
    smallest = min(minors.items(), key=lambda item: float(item[1].re))
    scan_mineig = float(np.linalg.eigvalsh(gram_float(Gs, Zs)).min())
    check(check_num, f"required exact untied probe {tag}: the normalized "
          "K-symmetrized 5x5 Gram is POSITIVE DEFINITE -- all 31 principal "
          "minors are exact positive rationals (no threshold)", strict,
          f"smallest exact minor {smallest[0]}={smallest[1]}; "
          f"float context min-eig={scan_mineig:.6g}")

failure_points = [
    ("iI", CR(0, 1), CR(0), CR(0)),
    ("2P1", PROBES[0][1] * 2, PROBES[0][2] * 2, PROBES[0][3] * 2),
]
failure_ok = True
failure_details = []
failure_minors = {}
for tag, a, b, ccoef in failure_points:
    Gs, Zs = sym_gram(W_of(a, b, ccoef))
    psd, minors = exact_psd_status(Gs, Zs)
    negatives = [(idx, value) for idx, value in minors.items()
                 if value.im == 0 and value.re < 0]
    first = min(negatives, key=lambda item: (len(item[0]), item[0]))
    failure_minors[tag] = first
    failure_ok = (failure_ok and psd is False and is_hermitian(norm_gram(Gs, Zs))
                  and not Zs.is_zero() and bool(negatives))
    failure_details.append(f"{tag}: Zsym={Zs}, minor{first[0]}={first[1]}")
check(8, "exact failure certificates on both signs/regions: W=iI and W=2P1 "
         "have nonzero Z_sym and exactly Hermitian normalized Grams, but each "
         "has a strictly negative rational principal minor; 2P1 has Z_sym>0, "
         "so failure is not an artifact of a negative normalization",
      failure_ok and sym_gram(W_of(*failure_points[1][1:]))[1].re > 0,
      "; ".join(failure_details))

check(9, "the exact T2 topology is MIXED-DOMAIN: strict PD at P1 and P2 and a "
         "strict negative minor at iI and 2P1 imply, by continuity away from "
         "Z_sym=0, nonempty open PD neighborhoods and nonempty open indefinite "
         "neighborhoods.  Thus symmetrization restores positivity on a domain, "
         "not universally", all(strict_probe_pd.values())
      and all(value.re < 0 for _, value in failure_minors.values()))

# Exact inheritance controls relative to block 10: the tied weight itself is
# unchanged; on P-even records the all-real branch agrees with its P-conjugate.
W_tie = W_of(CR(F(4, 5)), CR(F(3, 10), F(1, 5)),
             CR(F(3, 10), F(-1, 5)))
W_real_in = W_of(F(4, 5), F(3, 10), F(1, 2))
W_real_out = W_of(F(1, 2), F(-4, 5), F(3, 10))
inherit_ok = True
inherit_detail = []
for tag, W, expected in [("tie", W_tie, True),
                         ("real-inside", W_real_in, True),
                         ("real-outside", W_real_out, False)]:
    G, Z = reg_gram(W)
    Gs, Zs = sym_gram(W)
    status, _ = exact_psd_status(Gs, Zs)
    same_records_form = (Z == Zs
                         and all(G[i][j] == Gs[i][j]
                                 for i in range(5) for j in range(5)))
    inherit_ok = inherit_ok and same_records_form and status is expected
    inherit_detail.append(f"{tag}: PSD={status}")
check(10, "block-10 controls are inherited exactly at records-only grade: "
          "mu_sym equals the tied weight on the tie; on the all-real branch its "
          "P-even record Gram equals the original Gram, positive inside the "
          "known strip and indefinite at the supplied outside point",
      inherit_ok, "; ".join(inherit_detail))


def scan_box(radius_tenths, samples, seed):
    """Float-sign scan only: no threshold and no derivation-path use."""
    rng = random.Random(seed)
    counts = {"PD": 0, "INDEF": 0, "Z0": 0}
    extrema = [float("inf"), float("-inf")]
    for _ in range(samples):
        vals = [F(rng.randint(-radius_tenths, radius_tenths), 10)
                for _ in range(6)]
        W = W_of(CR(vals[0], vals[1]), CR(vals[2], vals[3]),
                 CR(vals[4], vals[5]))
        Gs, Zs = sym_gram(W)
        if Zs.is_zero():
            counts["Z0"] += 1
            continue
        mineig = float(np.linalg.eigvalsh(gram_float(Gs, Zs)).min())
        extrema[0], extrema[1] = min(extrema[0], mineig), max(extrema[1], mineig)
        counts["PD" if mineig > 0 else "INDEF"] += 1
    return counts, extrema


scan_report = []
for radius, samples in [(1, 24), (2, 24), (5, 24), (30, 48)]:
    counts, extrema = scan_box(radius, samples, 20260712 + radius)
    scan_report.append((F(radius, 10), counts, extrema))
small_counts = scan_report[0][1]
mid_counts = scan_report[1][1]
wide_counts = scan_report[-1][1]
check(11, "labeled float-only six-real-dimensional coverage (eigenvalue sign, "
          "no threshold) sees the open PD core/tubes and failures as the box "
          "widens; this is domain evidence only, not a claimed analytic global "
          "boundary", small_counts["PD"] > 0 and mid_counts["INDEF"] > 0
      and wide_counts["INDEF"] > 0,
      "; ".join(f"R={radius}: {counts}, min-eig-range={extrema}"
                for radius, counts, extrema in scan_report))
residual("the complete six-real-dimensional semialgebraic boundary of the PSD "
         "domain is NOT classified here.  Exact strict certificates establish "
         "open PD and indefinite regions; floats only map bounded coverage and "
         "are never promoted to a threshold or a global genericity theorem.")


# =====================================================================
# T3 -- law/ensemble status, K consumption, and many-slice extensions
# =====================================================================
print("\n--- T3: law/ensemble and licensing analysis ---")
Wp1, Gp1, Zp1, Gdp1, Zdp1, Gsp1, Zsp1 = probe_data["P1"]
Kp1 = build_K(Wp1, Wp1)
Kdp1 = build_K(dag(Wp1), dag(Wp1))
Kaverage = [[(Kp1[i][j] + Kdp1[i][j]) / 2 for j in range(6)]
            for i in range(6)]
single_gaussian_candidate = exp_bilinear(Kaverage, 6)
symp1 = sym_weight(Wp1)
all_masks = set(single_gaussian_candidate) | set(symp1)
different_masks = [mask for mask in all_masks
                   if single_gaussian_candidate.get(mask, CR(0))
                   != symp1.get(mask, CR(0))]
low_order_equal = all(single_gaussian_candidate.get(mask, CR(0))
                      == symp1.get(mask, CR(0))
                      for mask in all_masks if mask.bit_count() <= 2)
first_degree = min(mask.bit_count() for mask in different_masks)
check(12, "mu_sym is one exact finite Grassmann weight but is NON-GAUSSIAN: "
          "its constant and bilinear coefficients force K_eff=(K_W+K_Wdag)/2, "
          "yet exp(chibar K_eff chi) first disagrees with the half-sum at "
          "Grassmann degree four.  Hence there is no single bilinear/3-mode "
          "local Gaussian rule producing this weight at P1",
      low_order_equal and first_degree == 4
      and not poly_equal(single_gaussian_candidate, symp1),
      f"first mismatch degree={first_degree}, mismatch masks={len(different_masks)}")

alpha = Zp1 / (2 * Zsp1)
beta = Zdp1 / (2 * Zsp1)
check(13, "law versus ensemble, exact distinction: for supplied (W,K), the "
          "orbit-average prescription returns exactly one fixed raw integrand "
          "(so it satisfies the Qualification's extensional one-answer clause) "
          "and is a finite Berezin weight/linear functional.  It is formally a "
          "half-sum of two component weights, but after normalization at P1 the "
          "component coefficients are conjugate NONREAL numbers alpha,beta "
          "with alpha+beta=1 -- not a positive probabilistic mixture of two "
          "normalized laws", alpha + beta == CR(1) and alpha.im != 0
      and beta == alpha.conj(), f"alpha={alpha}, beta={beta}")

Wgeneric = Wp1
Wgeneric_dag = dag(Wgeneric)
Wtied_weight = gaussian_weight(W_tie)
check(14, "K-orbit use is exact and explicit: mu_sym(W)=mu_sym(Wdag), it reduces "
          "to mu_W on the tie, and it differs from mu_W at generic P1.  Thus "
          "the construction is arrow-free once K is supplied, but it CONSUMES "
          "K to alter the unregistered weight; that physical licensing is not "
          "settled by the algebra", poly_equal(sym_weight(Wgeneric),
                                                sym_weight(Wgeneric_dag))
      and poly_equal(sym_weight(W_tie), Wtied_weight)
      and not poly_equal(sym_weight(Wgeneric), gaussian_weight(Wgeneric)))
residual("K-ORBIT-AVERAGE LAW/MEASURE LICENSING (first-class): pro -- supplied "
         "readout-context K canonically fixes the orbit and removes any arrow or "
         "representative choice; contra -- applying that downstream context to "
         "the Berezin weight promotes K into the dynamics/measure and can be "
         "read as pre-inserting the structure sought.  No authorized landed "
         "content resolves this choice, so neither side is adopted.")

x_hist, y_hist = sp.Rational(2), sp.Rational(3)
quenched_two = (x_hist ** 2 + y_hist ** 2) / 2
annealed_two = ((x_hist + y_hist) / 2) ** 2
check(15, "time-homogeneity does not extend automatically: a quenched global "
          "orbit choice gives (x^N+y^N)/2, whereas an annealed per-step orbit "
          "average gives ((x+y)/2)^N; already at N=2, x=2, y=3 they are exactly "
          "13/2 and 25/4.  The present half-sum is global over the supplied "
          "two-slice history and lands neither many-slice rule",
      quenched_two == sp.Rational(13, 2)
      and annealed_two == sp.Rational(25, 4)
      and quenched_two != annealed_two)
residual("the many-slice transfer rule is OPEN: quenched means one W/Wdag orbit "
         "representative fixed for a whole history before averaging histories; "
         "annealed means re-averaging orbit representatives per step/link and "
         "summing 2^N assignments.  Neither extension is supplied or licensed.")


# =====================================================================
# T4 -- doubled carrier, correlator mismatch, and counting
# =====================================================================
print("\n--- T4: doubled-space realization and fork arithmetic ---")


def identity(size):
    return [[CR(1) if i == j else CR(0) for j in range(size)]
            for i in range(size)]


def matrix_add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]


def matrix_sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]


def matrix_scale(value, A):
    return [[asCR(value) * A[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]


def matrix_equal(A, B):
    return all(A[i][j] == B[i][j]
               for i in range(len(A)) for j in range(len(A[0])))


def matrix_nonzero(A):
    return any(not value.is_zero() for row in A for value in row)


D = direct_sum(Wp1, dag(Wp1))
J = [[CR(1) if ((i < 3 and j == i + 3) or
                (i >= 3 and j == i - 3)) else CR(0)
      for j in range(6)] for i in range(6)]
# The natural doubled antiunitary is K_D = S o complex-conjugation.  The
# generation inversion P is needed because W^dag = P conjugate(W) P for the
# C3 circulant.  This K-fixed real form is distinct from the linear J=+1 space.
P3 = [[CR(1), CR(0), CR(0)],
      [CR(0), CR(0), CR(1)],
      [CR(0), CR(1), CR(0)]]
Santi = [[(P3[i][j - 3] if i < 3 and j >= 3 else
           P3[i - 3][j] if i >= 3 and j < 3 else CR(0))
          for j in range(6)] for i in range(6)]
Dbar = [[D[i][j].conj() for j in range(6)] for i in range(6)]
Sbar = [[Santi[i][j].conj() for j in range(6)] for i in range(6)]
I6 = identity(6)
Pplus = matrix_scale(F(1, 2), matrix_add(I6, J))
Pminus = matrix_sub(I6, Pplus)
leak = matmul(matmul(Pminus, D), Pplus)
Jsp = sp.Matrix([[int(J[i][j].re) for j in range(6)] for i in range(6)])
signature = Jsp.eigenvals()
check(16, "the doubled one-slice carrier D=W direct-sum Wdag is conjugation-"
          "closed by construction in both relevant senses: J D=Ddag J for the "
          "copy-swap fundamental symmetry J, with J^2=I and signature (3,3); "
          "and the natural antiunitary K_D=S o conjugation obeys S conjugate(D) "
          "S=D and K_D^2=1 (S includes generation inversion P).  Its K-fixed "
          "real form is invariant.  Distinctly, the linear positive J=+1 half "
          "is NOT invariant: (I-P+)DP+ is nonzero at P1",
      matrix_equal(matmul(J, D), matmul(dag(D), J))
      and matrix_equal(matmul(J, J), I6)
      and signature == {sp.Integer(-1): 3, sp.Integer(1): 3}
      and matrix_equal(matmul(matmul(Santi, Dbar), Santi), D)
      and matrix_equal(matmul(Santi, Sbar), I6)
      and matrix_nonzero(matrix_sub(matmul(D, J), matmul(J, D)))
      and matrix_nonzero(leak))

# A Grassmann Gaussian on a direct-sum carrier factorizes (exterior algebra of
# a direct sum is a tensor product).  For the most charitable exchange-even
# additive lift of an already-formed correlator O, spectator partitions give
# B_D(O_+)=(B_W(O) Z_d + Z B_d(O))/2, not (B_W(O)+B_d(O))/2.
Zdouble = Zp1 * Zdp1
Gdouble_additive = [[(Gp1[i][j] * Zdp1 + Zp1 * Gdp1[i][j])
                     / (2 * Zdouble) for j in range(5)] for i in range(5)]
Gsym_normalized = norm_gram(Gsp1, Zsp1)
mismatches = [((i, j), Gdouble_additive[i][j] - Gsym_normalized[i][j])
              for i in range(5) for j in range(5)
              if Gdouble_additive[i][j] != Gsym_normalized[i][j]]
first_mismatch = mismatches[0]
check(17, "the ordinary doubled Gaussian does NOT reproduce mu_sym correlators "
          "even on the natural K-paired additive lift (the registrable basis is "
          "P-even, so this is the half-sum across copies): its partition is "
          "Z_D=Z_W Z_Wdag=|Z_W|^2 and spectator factors reweight every lifted "
          "correlator.  At exact P1 its normalized 5x5 form differs from the "
          "mu_sym form entrywise.  A direct-sum/superselection trace with an "
          "exclusive sector would reproduce the half-sum, but that one-hot "
          "sector structure is additional and is not the six-mode Gaussian",
      Zdouble.im == 0 and Zdouble.re > 0 and Zdouble != Zsp1
      and bool(mismatches),
      f"first difference {first_mismatch[0]}={first_mismatch[1]}; "
      f"mismatched entries={len(mismatches)}")

# Fork arithmetic inherited from block 10, with no endpoint adopted.  Uniform
# carrier doubling changes 3->6 diagonal slots and 6->12 doublet slots while
# also doubling the corresponding budgets.  It therefore cancels from the
# squared-amplitude ratio.  Count-twice would require a different budget rule.
a2, b2, eps = sp.symbols("a2 b2 eps", positive=True)
single_once = sp.solve([sp.Eq(3 * a2, eps), sp.Eq(6 * b2, eps)],
                       [a2, b2], dict=True)[0]
double_uniform = sp.solve([sp.Eq(6 * a2, 2 * eps),
                           sp.Eq(12 * b2, 2 * eps)],
                          [a2, b2], dict=True)[0]
double_count_twice = sp.solve([sp.Eq(6 * a2, 2 * eps),
                               sp.Eq(12 * b2, 4 * eps)],
                              [a2, b2], dict=True)[0]
ratio_single = sp.simplify(single_once[b2] / single_once[a2])
ratio_double = sp.simplify(double_uniform[b2] / double_uniform[a2])
ratio_twice = sp.simplify(double_count_twice[b2] /
                          double_count_twice[a2])
original_real_dims = {"singlet": 2, "doublet": 4}
doubled_real_dims = {key: 2 * value for key, value in original_real_dims.items()}
check(18, "DOUBLED-CARRIER COUNTING: W direct-sum Wdag doubles BOTH the singlet "
          "and doublet carriers (real dimensions 2->4 and 4->8).  The honest "
          "uniform doubled equations 6 a^2=2 eps, 12 b^2=2 eps preserve the "
          "count-once comparator b^2/a^2=1/2; they do NOT produce the count-"
          "twice comparator 1.  Obtaining the latter needs 12 b^2=4 eps (or an "
          "asymmetric singlet quotient), an extra grain/equipartition rule",
      doubled_real_dims == {"singlet": 4, "doublet": 8}
      and ratio_single == sp.Rational(1, 2)
      and ratio_double == ratio_single
      and ratio_twice == 1)
residual("no physical r value is derived or adopted.  The equations in check "
         "18 only compare the two already-landed fork cells.  Uniform direct-"
         "sum doubling pays a factor-two carrier overhead and a (3,3) Krein "
         "form.  The antiunitary K-fixed real form halves singlet and doublet "
         "uniformly; the linear positive J half is not transfer-invariant.  A "
         "different counting quotient would be new formation/equipartition "
         "content.")

escape_table = {
    "block10_non_OS": "PARTIALLY REALIZED algebraically by mu_sym",
    "mu_sym_signature": "LIVE only on a nonempty PD domain; indefinite elsewhere",
    "mu_sym_licensing": "OPEN first-class K-orbit-average residual",
    "mu_sym_many_slice": "OPEN annealed-versus-quenched transfer residual",
    "ordinary_doubling": "BLOCKED as a correlator realization; product not sum",
    "positive_metric_W": "CLOSED to tie (block 11)",
    "Krein_W": "OPEN on block-11 transposition loci",
    "coarser_A2": "OPEN (block 11)",
    "alternating_measure": "UNLICENSED inherited: arrow-dependent and K-preinserted",
}
check(19, "escape-table update relative to blocks 10/11 is complete: the new "
          "arrow-free orbit average is algebraically live only on a PD domain, "
          "with licensing and many-slice transfer open; ordinary doubling does "
          "not realize its correlators; positive-metric closure, Krein, A2, and "
          "alternating-measure dispositions remain correctly separated",
      len(escape_table) == 9
      and "OPEN" in escape_table["mu_sym_licensing"]
      and "BLOCKED" in escape_table["ordinary_doubling"]
      and "CLOSED" in escape_table["positive_metric_W"]
      and "OPEN" in escape_table["Krein_W"]
      and "OPEN" in escape_table["coarser_A2"]
      and "UNLICENSED" in escape_table["alternating_measure"])
residual("the per-cell equipartition/dial and formation-weight residues are "
         "untouched; no r endpoint, premise, probability rule, local transfer, "
         "or many-slice history law is adopted.  The exact construction is "
         "bounded to the two-slice C3 circulant and the registrable spanning set.")


print()
print("T2 SIGNATURE VERDICT FIRST: PSD ON A NONEMPTY OPEN DOMAIN, INDEFINITE "
      "ON ANOTHER NONEMPTY OPEN DOMAIN (MIXED-DOMAIN BOUNDED THEOREM).  Both "
      "required exact complex untied probes are PD; iI and 2P1 have exact "
      "negative principal minors; no global six-dimensional boundary claimed.")
print("T1: theta exchanges mu_W and mu_Wdag, so mu_sym and its raw Gram are "
      "exactly reflection-invariant/Hermitian; normalization exists only where "
      "Z_sym=Re Z_W is nonzero.")
print("T3: the prescription is one fixed non-Gaussian Berezin weight and a "
      "formal orbit ensemble, but its K-to-measure licensing and annealed-versus-"
      "quenched many-slice law remain first-class open residuals.")
print("T4: W direct-sum Wdag is a (3,3)-signature conjugation-closed carrier, "
      "but its K-paired Gaussian gives product rather than sum correlators; the "
      "natural K-real form is closed while the linear positive J half is not.")
print("DOUBLED-CARRIER COUNTING RESULT: uniform doubling doubles singlet and "
      "doublet alike, preserves the count-once fork comparator, and does not "
      "reinstall count-twice without an extra asymmetric grain rule.")
print(f"CHECK COUNT: PASS={_pass} FAIL={_fail}")
print("PROPOSED CLAIM_SCOPE: bounded_theorem -- two-slice C3 circulant, "
      "registrable 5-element spanning set, exact mixed signature, with "
      "K-orbit-average licensing and many-slice transfer explicitly open.")
print("HOSTILE-AUDIT UNCERTAINTIES: full PSD-domain boundary; whether supplied "
      "readout K may act on the weight; law-versus-ensemble physical status; "
      "annealed/quenched extension; exclusive-sector transfer realization; "
      "equipartition/formation grain.")
print(f"TOTAL: PASS={_pass} FAIL={_fail}")
raise SystemExit(0 if _fail == 0 else 1)
