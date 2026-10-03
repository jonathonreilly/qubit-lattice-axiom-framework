"""A25: limiting gauge directions at a degenerate momentum K for a collocated generator symbol D(k) (6x3).
S_K = span of all limits of Im D(k) as k -> K.  Every direction counts (special approach directions included),
so each approach contributes an orthonormal basis and the union dimension is counted with an ABSOLUTE
threshold on the singular values of the stacked bases (a direction seen in a single approach gives sv ~ 1).
Necessary condition for no zero-frequency transverse mode at K (see A25 report): dim S_K <= 4."""
import itertools
import numpy as np

_r = np.random.default_rng(3)
LAT_DIRS = [np.array(v, float) for v in itertools.product((-1, 0, 1), repeat=3) if any(v)]
NEAR = [d + 0.05 * _r.normal(size=3) for d in LAT_DIRS]          # generic directions close to special ones
RAND = list(_r.normal(size=(30, 3)))
DIRS = [d / np.linalg.norm(d) for d in LAT_DIRS + NEAR + RAND]


def span_sv(D, K, eps=1e-4, rank_tol=1e-11, dirs=None):
    bases = []
    for q in (DIRS if dirs is None else dirs):
        u, s, vh = np.linalg.svd(D(K + eps * q))
        if s[0] == 0:
            continue
        r = int(np.sum(s > rank_tol * s[0]))
        bases.append(u[:, :r])
    if not bases:
        return np.zeros(6)
    return np.linalg.svd(np.hstack(bases), compute_uv=False)


def span_dim(D, K, thr=0.05, **kw):
    return int(np.sum(span_sv(D, K, **kw) > thr))
