"""R11-1 Lemma M check: for V = p p'^T + p' p^T - delta (p.p' + m^2) and the 4D de Donder P,
V.P.V = 2 p^2 p'^2 - 4 m^2 (p.p' + m^2)  for ANY complex 4-vectors; on shell (p.p = -m^2): = -2 m^2 [(p+p')^2 + 3 m^2]."""
import numpy as np
rng = np.random.default_rng(7); worst = 0; worst_on = 0
for _ in range(1000):
    m = rng.uniform(0.01, 2)
    p = rng.normal(size=4) + 1j * rng.normal(size=4); pp = rng.normal(size=4) + 1j * rng.normal(size=4)
    def vpv(p, pp):
        Q = p @ pp + m * m
        V = np.outer(p, pp) + np.outer(pp, p) - Q * np.eye(4)
        return np.sum(V * V) - 0.5 * np.trace(V) ** 2, Q
    v, Q = vpv(p, pp)
    worst = max(worst, abs(v - (2 * (p @ p) * (pp @ pp) - 4 * m * m * Q)) / abs(v))
    # on shell: p = (i E, s) with E^2 = m^2 + s.s  (Euclidean continuation)
    s = rng.normal(size=3); E = np.sqrt(m * m + s @ s); pon = np.array([1j * E, *s])
    v2, _ = vpv(pon, pp)
    worst_on = max(worst_on, abs(v2 + 2 * m * m * ((pon + pp) @ (pon + pp) + 3 * m * m)) / abs(v2))
print('VPV identity, random complex vectors: max rel err %.1e ; on-shell form -2m^2[(p+p\')^2+3m^2]: max rel err %.1e' % (worst, worst_on))
