"""K5: if the circulant ratio r = 2|b|/a were sector-blind (as HIER-2 proved for exponents), every sector
would carry Q = 2/3 (r = sqrt2).  Best Chebyshev fit of each sector with r = sqrt2, delta and mu free."""
import numpy as np
SETS = {"MZ": dict(u=(1.38e-3, 0.638, 172.1), d=(2.82e-3, 0.057, 2.86), e=(0.4866e-3, 0.10272, 1.7462)),
        "LOW": dict(u=(2.16e-3, 1.27, 172.69), d=(4.67e-3, 0.0934, 4.18), e=(0.51099895e-3, 0.1056583755, 1.77686))}
dl = np.linspace(0, np.pi / 3, 200001)
k = np.arange(3)[None, :]
roots = 1 + np.sqrt(2) * np.cos(dl[:, None] + 2 * np.pi * k / 3)
ok = (roots > 0).all(1)
lm = np.sort(np.log(roots[ok] ** 2), 1); dd = dl[ok]
for s, data in SETS.items():
    out = []
    for f, m in data.items():
        y = np.log(np.array(m))
        dev = 0.5 * np.ptp(y[None, :] - lm, 1)
        i = dev.argmin()
        out.append(f"{f}: x{np.exp(dev[i]):.2f} at delta={dd[i]:.4f}")
    print(s, " | ".join(out))
print("x3 tolerance: pass iff factor <= 3")
