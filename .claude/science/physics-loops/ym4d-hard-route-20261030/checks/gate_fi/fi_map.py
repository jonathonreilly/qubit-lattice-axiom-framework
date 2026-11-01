#!/usr/bin/env python3
"""Map D3 of hard-core--independent Text 5.1, 5.4, written from the text, in torch, differentiable.

Box: axes 0, 1 have 2L sites, axes 2, 3 have L. Four blocks (a, b), a, b in {0, 1}. Coarse plaquette in the (0, 1) plane.
W = M(00->10, axis 0) M(10->11, axis 1) M(01->11, axis 0)^-1 M(00->01, axis 1)^-1. Paths multiply left to right.

Cost is O(L^4) per block direction: a mean over one coordinate of phi(s) seg(s -> t) factors as [mean_s phi(s) P(s)^-1] P(t),
with P the transport from coordinate 0 along the line. So all of x, orders and z are done by transfer steps and no path is enumerated.
"""
import itertools
import numpy as np
import torch

torch.set_num_threads(1)
torch.set_default_dtype(torch.float64)
AXES = (0, 1, 2, 3)


def qmul(a, b):
    a0, a1, a2, a3 = a.unbind(-1)
    b0, b1, b2, b3 = b.unbind(-1)
    return torch.stack((a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3, a0 * b1 + a1 * b0 + a2 * b3 - a3 * b2,
                        a0 * b2 - a1 * b3 + a2 * b0 + a3 * b1, a0 * b3 + a1 * b2 - a2 * b1 + a3 * b0), -1)


def qconj(a):
    return a * a.new_tensor([1.0, -1.0, -1.0, -1.0])


def shape_box(L):
    return (2 * L, 2 * L, L, L)


def flat_links(L):
    """Quaternion links on the box, one tensor per axis, axis dimension one shorter."""
    out = []
    for mu in AXES:
        s = list(shape_box(L))
        s[mu] -= 1
        q = torch.zeros(*s, 4)
        q[..., 0] = 1.0
        out.append(q)
    return out


def block_slices(L, a, b):
    return (slice(a * L, (a + 1) * L), slice(b * L, (b + 1) * L), slice(0, L), slice(0, L))


def block_links(U, L, a, b):
    """Links inside block (a, b), axis mu tensors of shape L except L - 1 at mu."""
    out = []
    bs = block_slices(L, a, b)
    for mu in AXES:
        s = list(bs)
        s[mu] = slice(bs[mu].start, bs[mu].stop - 1)
        out.append(U[mu][tuple(s)])
    return out


def line_transport(Ub, mu, L):
    """P[..., i, ...] = transport from coordinate 0 to i along axis mu, dimension mu of size L."""
    u = Ub[mu].movedim(mu, 0)
    p = [torch.zeros_like(u[0])]
    p[0][..., 0] = 1.0
    for i in range(L - 1):
        p.append(qmul(p[-1], u[i]))
    return torch.stack(p, 0).movedim(0, mu)


def transfer(phi, P, mu):
    """(E_mu phi)(t) = mean_s phi(s) seg(s -> t), at every t."""
    inner = qmul(phi, qconj(P)).mean(dim=mu, keepdim=True)
    return qmul(inner, P)


def star_field(P, x0, L):
    """S(x) = mean over axial orders of the path x0 -> x, by a recursion on subsets of axes."""
    def take(T, keep):
        idx = tuple(slice(None) if i in keep else slice(x0[i], x0[i] + 1) for i in AXES) + (Ellipsis,)
        return T[idx]
    G = {(): torch.tensor([1.0, 0.0, 0.0, 0.0]).reshape(1, 1, 1, 1, 4)}
    for r in range(1, 5):
        for A in itertools.combinations(AXES, r):
            tot = 0.0
            for a in A:
                rest = tuple(i for i in A if i != a)
                Pa = take(P[a], A)
                Pa0 = Pa.index_select(a, torch.tensor([x0[a]]))
                tot = tot + qmul(qmul(G[rest], qconj(Pa0)), Pa)
            G[A] = tot / r
    return G[AXES]


def psi_face(S, P, mu, face):
    """Psi^mu(z) without star, z on the face z_mu = face: mean over x and transverse orders, then along mu."""
    tr = [i for i in AXES if i != mu]
    tot = 0.0
    first = {a: transfer(S, P[a], a) for a in tr}
    for a in tr:
        b, c = [i for i in tr if i != a]
        ab = transfer(first[a], P[b], b)
        ac = transfer(first[a], P[c], c)
        tot = tot + transfer(ab, P[c], c) + transfer(ac, P[b], b)
    phi = tot / 6.0
    inner = qmul(phi, qconj(P[mu])).mean(dim=mu, keepdim=True)
    Pf = P[mu].index_select(mu, torch.tensor([face]))
    m = qmul(inner, Pf).squeeze(mu)
    r = m.norm(dim=-1, keepdim=True)
    return m / r.clamp_min(1e-300), r


def plaquette_f(U, L):
    """Dict (al, be) -> f_p on the box, with al < be, f = |U_p - 1| in R^4."""
    out = {}
    for al, be in itertools.combinations(AXES, 2):
        u1 = U[al].narrow(be, 0, U[al].shape[be] - 1)
        u2 = U[be].narrow(al, 1, U[be].shape[al] - 1)
        u3 = U[al].narrow(be, 1, U[al].shape[be] - 1)
        u4 = U[be].narrow(al, 0, U[be].shape[al] - 1)
        g = qmul(qmul(u1, u2), qmul(qconj(u3), qconj(u4)))
        d = g - g.new_tensor([1.0, 0.0, 0.0, 0.0])
        out[(al, be)] = (d * d).sum(-1)
    return out


def rule_base(f2, L, a, b, eps, s_rule):
    """x_0 in block coordinates. f2 are numpy squared plaquette values on the box."""
    o = (L - 1) // 2
    y = (o, o, o, o)
    bs = block_slices(L, a, b)
    s = np.zeros((L,) * 4)
    any_rough = False
    for (al, be), v in f2.items():
        sl = list(bs)
        sl[al] = slice(bs[al].start, bs[al].stop - 1)
        sl[be] = slice(bs[be].start, bs[be].stop - 1)
        g = np.sqrt(v[tuple(sl)])
        g = np.where(g > eps, g, 0.0)
        if not g.any():
            continue
        any_rough = True
        ga, de = [i for i in AXES if i not in (al, be)]
        C = g.sum(axis=(al, be))  # shape L x L in (ga, de)
        add = C + (C.sum(axis=1, keepdims=True) + C.sum(axis=0, keepdims=True)) / L
        sh = [1, 1, 1, 1]
        sh[ga] = L
        sh[de] = L
        s = s + add.reshape(sh)
    if not any_rough or s[y] <= s_rule:
        return y
    return tuple(int(i) for i in np.unravel_index(np.argmin(np.round(s, 12).ravel()), s.shape))


def coarse_W(U, L, bases):
    """bases: dict (a, b) -> x_0 in block coordinates. Returns W, min |m| over all means, and pieces."""
    P, S = {}, {}
    for ab in ((0, 0), (1, 0), (0, 1), (1, 1)):
        Ub = block_links(U, L, *ab)
        P[ab] = [line_transport(Ub, mu, L) for mu in AXES]
        S[ab] = star_field(P[ab], bases[ab], L)
    rmin = []

    def coarse(y, yp, mu):
        pa, ra = psi_face(S[y], P[y], mu, L - 1)
        pb, rb = psi_face(S[yp], P[yp], mu, 0)
        sl = [slice(None)] * 4
        sl[0] = slice(y[0] * L, (y[0] + 1) * L)
        sl[1] = slice(y[1] * L, (y[1] + 1) * L)
        sl[mu] = L * (y[mu] + 1) - 1
        u = U[mu][tuple(sl)]
        m = qmul(qmul(pa, u), qconj(pb)).mean(dim=(0, 1, 2))
        r = m.norm()
        rmin.extend((ra.min(), rb.min(), r))
        return m / r.clamp_min(1e-300)

    A = coarse((0, 0), (1, 0), 0)
    B = coarse((1, 0), (1, 1), 1)
    C = coarse((0, 1), (1, 1), 0)
    D = coarse((0, 0), (0, 1), 1)
    W = qmul(qmul(A, B), qmul(qconj(C), qconj(D)))
    return W, min(float(r) for r in rmin)


def xi_bar(U, L, ab, x0):
    """|Xi_bar(x')| on the block, up to the order convention of pi: mean over x of S(x) R(x -> x')."""
    Ub = block_links(U, L, *ab)
    P = [line_transport(Ub, mu, L) for mu in AXES]
    S = star_field(P, x0, L)
    tot = 0.0
    for p in itertools.permutations(AXES):
        g = S
        for a in p:
            g = transfer(g, P[a], a)
        tot = tot + g
    return (tot / 24.0).norm(dim=-1)


def splits(f, L, eps):
    """f: flat numpy array of f_p. Returns (A_rhs, C_rhs, threshold t): RHS at irr = rough, and min RHS over threshold splits."""
    o = np.sort(f)
    c1 = np.concatenate(([0.0], np.cumsum(o)))
    c2 = np.concatenate(([0.0], np.cumsum(o * o)))
    kmax = int(np.searchsorted(o, eps, side="right"))
    val = (c1[-1] - c1[: kmax + 1]) / L ** 2 + np.sqrt(c2[: kmax + 1])
    k = int(np.argmin(val))
    t = o[k - 1] if k > 0 else -1.0
    return float(val[kmax]), float(val[k]), float(t)


def evaluate(U, L, eps, s_rule, base="rule"):
    """Exact score of a field, with no smoothing and no gradient."""
    with torch.no_grad():
        f2t = plaquette_f(U, L)
        f2 = {k: v.numpy() for k, v in f2t.items()}
        bases = {}
        o = (L - 1) // 2
        for ab in ((0, 0), (1, 0), (0, 1), (1, 1)):
            bases[ab] = (o, o, o, o) if base == "fixed" else rule_base(f2, L, *ab, eps, s_rule)
        W, r = coarse_W(U, L, bases)
        w1 = float((W - W.new_tensor([1.0, 0, 0, 0])).norm())
        f = np.sqrt(np.concatenate([v.ravel() for v in f2.values()]))
        ra, rc, t = splits(f, L, eps)
    return dict(w1=w1, rhs_a=ra, rhs_c=rc, ratio_a=w1 / ra if ra > 1e-9 else 0.0, ratio_c=w1 / rc if rc > 1e-9 else 0.0,
                min_m=r, bases=bases, thr=t, l1=float(f.sum()), nrough=int((f > eps).sum()))
