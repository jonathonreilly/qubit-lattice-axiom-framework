"""Vectorised residual/Jacobian for the bilinear constraint system of c4d_quantum, plus helpers."""
import numpy as np
import scipy.sparse as sp
from c4d_common import pair, near_rhos
from c4d_monomial import com2


def compile_system(S, unit, spec):
    rows, I, J, C = [], [], [], []
    seen = set()
    nr = 0
    for c, terms in unit:
        key = ("u", c, tuple(sorted(terms)))
        if key in seen:
            continue
        seen.add(key)
        for i, j in terms:
            rows.append(nr); I.append(i); J.append(j)
        C.append(c); nr += 1
    for kind in ("W", "Wd"):
        for terms in spec[kind]:
            tt = tuple(sorted((i, j) for _, i, j in terms))
            key = ("s", tt)
            if key in seen:
                continue
            seen.add(key)
            for i, j in tt:
                rows.append(nr); I.append(i); J.append(j)
            C.append(0.0); nr += 1
    return dict(rows=np.array(rows), I=np.array(I), J=np.array(J), C=np.array(C, complex), nr=nr, n=S.nvar)


def moving_mask(S):
    mv = np.zeros(S.nvar, bool)
    mult = np.zeros(S.nvar)
    for k, (rho0, s, m) in enumerate(S.var_info):
        mv[k] = com2(s) != com2(pair((0, 0, 0), rho0))
        mult[k] = m
    return mv, mult


def make_fun(sysd, extra=None):
    rows, I, J, C, nr, n = sysd["rows"], sysd["I"], sysd["J"], sysd["C"], sysd["nr"], sysd["n"]

    def fun(z):
        x = z[:n] + 1j * z[n:]
        v = np.conj(x[I]) * x[J]
        r = C.copy()
        np.add.at(r, rows, v)
        out = [r.real, r.imag]
        if extra is not None:
            out.append(np.atleast_1d(extra[0](x)))
        return np.concatenate(out)

    def jac(z):
        x = z[:n] + 1j * z[n:]
        # d/da_I : x_J ; d/da_J : conj(x_I); d/db_I : -i x_J ; d/db_J : i conj(x_I)
        dA_I, dA_J = x[J], np.conj(x[I])
        dB_I, dB_J = -1j * x[J], 1j * np.conj(x[I])
        rr = np.concatenate([rows, rows, rows, rows])
        cc = np.concatenate([I, J, n + I, n + J])
        vv = np.concatenate([dA_I, dA_J, dB_I, dB_J])
        Jre = sp.coo_matrix((vv.real, (rr, cc)), shape=(nr, 2 * n))
        Jim = sp.coo_matrix((vv.imag, (rr, cc)), shape=(nr, 2 * n))
        blocks = [Jre, Jim]
        if extra is not None:
            g = extra[1](x)  # gradient wrt (a,b) as dense row
            blocks.append(sp.csr_matrix(g.reshape(1, -1)))
        return sp.vstack(blocks).tocsr()

    return fun, jac


def bloch(S, x, K):
    """13x13 (or d_r) Bloch matrix of W at pair-COM momentum K (anchor = lexmin site)."""
    rhos = near_rhos(S.r)
    pos = {rho: a for a, rho in enumerate(rhos)}
    M = np.zeros((len(rhos), len(rhos)), complex)
    for b, rho in enumerate(rhos):
        p = pair((0, 0, 0), rho)
        for s, i in S.column(p):
            a0, a1 = sorted(s)
            d = tuple(q - w for q, w in zip(a1, a0))
            from c4d_common import canon_rho
            c = canon_rho(d)
            anchor = a0 if c == d else a1
            M[pos[c], b] += x[i] * np.exp(-1j * np.dot(K, anchor))
    return M
