"""Probe: does relaxing "nearest-neighbor" to "local" actually buy chirality?

The reset proposal claims that replacing Admissibility's strict
nearest-neighbor coupling with decay removes the Nielsen-Ninomiya hypothesis,
and that this is the whole cost of the chirality unlock.

That claim has a sharp test. In two dimensions:

  (a) a strictly nearest-neighbor operator that exactly anticommutes with
      gamma5 must carry 2^d species (doubling);
  (b) a strictly nearest-neighbor operator with one species must break the
      chiral relation;
  (c) an operator that is NOT strictly nearest-neighbor, but decays
      exponentially, can have one species AND an exact Ginsparg-Wilson chiral
      relation.

If (a) and (b) hold and (c) fails, the proposed one-word change buys nothing.
If all three hold, the change is exactly the hypothesis being paid for.

Species counts and decay rates are measured, not assumed.
"""

import numpy as np

RESULTS = []
L = 24                      # lattice extent per direction
TOL = 1e-9

G1 = np.array([[0, 1], [1, 0]], dtype=complex)
G2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
G5 = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2, dtype=complex)


def check(label, ok, detail=""):
    RESULTS.append((label, bool(ok), detail))


def momenta():
    k = 2.0 * np.pi * np.arange(L) / L
    return [(p1, p2) for p1 in k for p2 in k]


def d_naive(p1, p2):
    return 1j * (G1 * np.sin(p1) + G2 * np.sin(p2))


def d_wilson(p1, p2, mass=0.0, r=1.0):
    kin = 1j * (G1 * np.sin(p1) + G2 * np.sin(p2))
    w = mass + r * ((1 - np.cos(p1)) + (1 - np.cos(p2)))
    return kin + w * I2


def d_overlap(p1, p2, m0=-1.0):
    """D = 1 + gamma5 sign(gamma5 D_wilson(m0)), the standard overlap form."""
    dw = d_wilson(p1, p2, mass=m0)
    hw = G5 @ dw
    hw = 0.5 * (hw + hw.conj().T)          # symmetrize away round-off
    vals, vecs = np.linalg.eigh(hw)
    sign_hw = vecs @ np.diag(np.sign(vals)) @ vecs.conj().T
    return I2 + G5 @ sign_hw


def count_species(op):
    """Number of Brillouin-zone momenta where the operator degenerates."""
    zeros = []
    for p1, p2 in momenta():
        s = np.linalg.svd(op(p1, p2), compute_uv=False)
        if s.min() < 1e-8:
            zeros.append((round(p1, 6), round(p2, 6)))
    return zeros


def chiral_defect(op):
    """max |{gamma5, D}| over the zone: zero means exact chiral symmetry."""
    worst = 0.0
    for p1, p2 in momenta():
        D = op(p1, p2)
        worst = max(worst, float(np.abs(G5 @ D + D @ G5).max()))
    return worst


def gw_defect(op):
    """max |gamma5 D + D gamma5 - D gamma5 D|: zero means the GW relation."""
    worst = 0.0
    for p1, p2 in momenta():
        D = op(p1, p2)
        resid = G5 @ D + D @ G5 - D @ G5 @ D
        worst = max(worst, float(np.abs(resid).max()))
    return worst


def position_profile(op):
    """Fourier transform back to position space; return max |D(x)| by |x|_1."""
    field = np.zeros((L, L, 2, 2), dtype=complex)
    k = 2.0 * np.pi * np.arange(L) / L
    for a, p1 in enumerate(k):
        for b, p2 in enumerate(k):
            field[a, b] = op(p1, p2)
    pos = np.fft.ifft2(field, axes=(0, 1))
    prof = {}
    for x in range(L):
        for y in range(L):
            r = min(x, L - x) + min(y, L - y)
            prof[r] = max(prof.get(r, 0.0), float(np.abs(pos[x, y]).max()))
    return prof


def support_radius(prof, floor=1e-12):
    return max(r for r, v in prof.items() if v > floor)


def main():
    # (a) strictly nearest-neighbour + exact chiral symmetry -> doubling
    naive_zeros = count_species(d_naive)
    naive_chiral = chiral_defect(d_naive)
    naive_prof = position_profile(d_naive)
    naive_reach = support_radius(naive_prof)
    check("naive operator is strictly nearest-neighbour",
          naive_reach == 1, f"position-space support radius = {naive_reach}")
    check("naive operator has exact chiral symmetry",
          naive_chiral < TOL, f"max |{{g5, D}}| = {naive_chiral:.2e}")
    check("Nielsen-Ninomiya (a): strict locality + chirality forces doubling",
          len(naive_zeros) == 2 ** 2,
          f"measured species = {len(naive_zeros)} at {sorted(naive_zeros)}, "
          f"expected 2^d for d=2")

    # (b) strictly nearest-neighbour + one species -> chiral symmetry broken
    wilson_zeros = count_species(lambda a, b: d_wilson(a, b, mass=0.0))
    wilson_chiral = chiral_defect(lambda a, b: d_wilson(a, b, mass=0.0))
    wilson_reach = support_radius(position_profile(lambda a, b: d_wilson(a, b, mass=0.0)))
    check("Wilson operator is strictly nearest-neighbour",
          wilson_reach == 1, f"position-space support radius = {wilson_reach}")
    check("Nielsen-Ninomiya (b): strict locality + one species breaks chirality",
          len(wilson_zeros) == 1 and wilson_chiral > 0.1,
          f"species = {len(wilson_zeros)}, max |{{g5, D}}| = {wilson_chiral:.4f}")

    # (c) exponentially local escapes the trade
    ov_zeros = count_species(d_overlap)
    ov_gw = gw_defect(d_overlap)
    ov_chiral = chiral_defect(d_overlap)
    prof = position_profile(d_overlap)
    ov_reach = support_radius(prof)

    check("overlap operator has exactly one species",
          len(ov_zeros) == 1, f"species = {len(ov_zeros)} at {sorted(ov_zeros)}")
    check("overlap operator satisfies the Ginsparg-Wilson relation exactly",
          ov_gw < 1e-10, f"max |g5 D + D g5 - D g5 D| = {ov_gw:.2e}")
    check("overlap operator does NOT have naive chiral symmetry (as expected)",
          ov_chiral > 0.1, f"max |{{g5, D}}| = {ov_chiral:.4f}")

    # the load-bearing measurement: not compact, but exponentially decaying
    check("overlap operator is NOT strictly nearest-neighbour",
          ov_reach > 1, f"position-space support radius = {ov_reach} (vs 1 for naive/Wilson)")

    rs = sorted(r for r in prof if 1 <= r <= L // 2 and prof[r] > 1e-13)
    vals = np.array([prof[r] for r in rs])
    slope, intercept = np.polyfit(np.array(rs, float), np.log(vals), 1)
    resid = np.log(vals) - (slope * np.array(rs, float) + intercept)
    r2 = 1.0 - float(np.var(resid) / np.var(np.log(vals)))
    check("overlap operator decays exponentially, so it is local in the drafted sense",
          slope < -0.5 and r2 > 0.9,
          f"fitted decay exp(-{-slope:.3f} * |x|_1), R^2 = {r2:.4f}, "
          f"amplitude falls {vals[0]/vals[-1]:.2e} across |x|_1 = {rs[0]}..{rs[-1]}")

    passed = sum(1 for _l, ok, _d in RESULTS if ok)
    failed = len(RESULTS) - passed
    for label, ok, detail in RESULTS:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" ({detail})" if detail else ""))
    print("=" * 76)
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
