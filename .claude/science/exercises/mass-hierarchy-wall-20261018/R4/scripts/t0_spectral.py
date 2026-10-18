"""T0: largest ratio of nonzero lattice spectral values at high-symmetry momenta."""
import itertools
import numpy as np
from common import MZ, SECTORS

ks = [0.0, np.pi / 3, np.pi / 2, 2 * np.pi / 3, np.pi]


def spectra(dim):
    vals = {"naive": set(), "wilson": set(), "laplacian": set(), "walker": set()}
    for k in itertools.product(ks, repeat=dim):
        k = np.array(k)
        s2 = np.sum(np.sin(k) ** 2)
        w = np.sum(1 - np.cos(k))
        vals["naive"].add(round(np.sqrt(s2), 12))
        vals["wilson"].add(round(np.sqrt(s2 + w ** 2), 12))
        vals["laplacian"].add(round(2 * w, 12))
        c = np.prod(np.cos(k))
        om = np.arccos(np.clip(c, -1, 1))
        vals["walker"].add(round(min(om, np.pi - om), 12))  # quasi-energy distance to nearest node
    return vals


for dim in (3, 4):
    v = spectra(dim)
    for name, s in v.items():
        nz = sorted(x for x in s if x > 1e-9)
        print(f"dim={dim} {name:10s} nonzero values={len(nz):3d} max/min ratio={nz[-1]/nz[0]:.3f}")

# cubic-group integers: orbit sizes of {0,1}^3,{0,1}^4, O class sizes, |O|,|O_h|, irrep dims
ints = [1, 3, 4, 6, 8, 16, 24, 48, 2]
print("cubic-group integers max/min =", max(ints) / min(ints))
print()
for key in SECTORS:
    m = MZ[key]
    print(f"needed in-sector ratios {key}: m3/m2={m[2]/m[1]:.1f} m3/m1={m[2]/m[0]:.3g}")
print("Wilson corner staircase (hw=1,2,3): ratios 2, 3 (main: WILSON_BZ_CORNER_HAMMING_STAIRCASE)")
