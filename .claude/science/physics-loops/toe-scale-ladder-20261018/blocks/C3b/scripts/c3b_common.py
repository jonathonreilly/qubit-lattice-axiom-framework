"""C3b common utilities: torus lattices, record formation, ancestry depth, correlations.

All randomness is passed in explicitly (numpy Generator) so runs are reproducible.
Conventions follow C3 sec.1: a site sees exactly the neighbours with STRICTLY smaller clock.
"""
import numpy as np
import numba as nb

PASS = 0
FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
        print(f"PASS  {name}  {detail}")
    else:
        FAIL += 1
        print(f"FAIL  {name}  {detail}")


def total():
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")


def nbr_table(shape):
    """Nearest-neighbour table on a periodic box of given shape; returns (N, 2d) int64."""
    d = len(shape)
    N = int(np.prod(shape))
    idx = np.arange(N).reshape(shape)
    cols = []
    for ax in range(d):
        cols.append(np.roll(idx, -1, axis=ax).ravel())
        cols.append(np.roll(idx, +1, axis=ax).ravel())
    return np.stack(cols, axis=1).astype(np.int64)


@nb.njit(cache=True)
def depth_and_record(T, nbr, u_choice, u_noise, delta):
    """Process sites in increasing T.  Rule (q=2, colours +-1):
       - with prob delta (u_noise<delta): uniform random colour (u_choice<0.5 -> +1);
       - else: majority of strictly-earlier neighbours' colours; tie or no earlier neighbour -> uniform random.
       Also returns L(x) = length of the longest strictly decreasing nn path starting at x (C3 sec.1).
       Ties T_x == T_y: the neighbour is NOT seen (strict convention)."""
    N = T.shape[0]
    order = np.argsort(T, kind='mergesort')
    sig = np.zeros(N, np.int8)
    L = np.zeros(N, np.int64)
    for k in range(N):
        x = order[k]
        s = 0
        cnt = 0
        best = -1
        for j in range(nbr.shape[1]):
            y = nbr[x, j]
            if T[y] < T[x]:
                s += sig[y]
                cnt += 1
                if L[y] > best:
                    best = L[y]
        L[x] = best + 1
        if u_noise[x] < delta or cnt == 0 or s == 0:
            sig[x] = 1 if u_choice[x] < 0.5 else -1
        else:
            sig[x] = 1 if s > 0 else -1
    return sig, L


def axis_corr(field, rmax):
    """Connected two-point function averaged over axes and sites (periodic):
       C(r) = <f_x f_{x+r e_i}> - <f>^2 , r=0..rmax.  Returns array (rmax+1,)."""
    f = field.astype(np.float64)
    m = f.mean()
    out = np.zeros(rmax + 1)
    d = f.ndim
    for r in range(rmax + 1):
        acc = 0.0
        for ax in range(d):
            acc += (f * np.roll(f, -r, axis=ax)).mean()
        out[r] = acc / d - m * m
    return out


def mean_se(a, axis=0):
    a = np.asarray(a, float)
    n = a.shape[axis]
    return a.mean(axis=axis), a.std(axis=axis, ddof=1) / np.sqrt(n)


def corr_length_second_moment(C, rmax):
    """xi from C(r) along axes: xi^2 = sum r^2 C / (2 sum C) over r<=rmax (1D-axis estimator).
       Only used as a scale; reported together with raw C(r)."""
    r = np.arange(len(C))[:rmax + 1]
    c = C[:rmax + 1]
    w = np.concatenate([[1.0], 2 * np.ones(len(r) - 1)])
    num = (w * r ** 2 * c).sum()
    den = (w * c).sum()
    return np.sqrt(max(num, 0) / (2 * den)) if den > 0 else np.nan


def fit_loglog(x, y, yerr):
    """Weighted least squares of log y on log x; returns slope, slope_se."""
    lx = np.log(x)
    ly = np.log(y)
    w = (y / yerr) ** 2
    W = w.sum()
    xb = (w * lx).sum() / W
    yb = (w * ly).sum() / W
    sxx = (w * (lx - xb) ** 2).sum()
    slope = (w * (lx - xb) * (ly - yb)).sum() / sxx
    se = np.sqrt(1.0 / sxx)
    # inflate by reduced chi2 if > 1
    resid = ly - (yb + slope * (lx - xb))
    dof = max(len(x) - 2, 1)
    chi2 = (w * resid ** 2).sum() / dof
    if chi2 > 1:
        se *= np.sqrt(chi2)
    return slope, se, chi2
