"""TOR-1 torus crossing geometry for W-matched point-orbit witnesses (shared by kernel and search)."""
import numpy as np
from tor1_lib import *
from lat2d import cells_Lx4, duffy_tet, wrap
DELTA = 0.6


def plane_nodes(off, n):
    Phi = wrap(off.sum()); assert abs(Phi) < 1e-9, 'pool not W-matched'
    P = []; W = []
    for c in cells_Lx4(Phi, DELTA, 'hard'):
        p, w = duffy_tet(c, n); P.append(p); W.append(w)
    d = np.concatenate(P); w = np.concatenate(W)
    ph = np.zeros((len(w), 4)); ph[:, 1] = d[:, 0] - off[0]; ph[:, 2] = ph[:, 1] + d[:, 1] - off[1]; ph[:, 3] = ph[:, 2] + d[:, 2] - off[2]
    return ph, w


def entry_fields(S, ua, ub, n, nw):
    """all node link vectors (P, nl) and weights; lat2d conventions: Lambda+ = ua (slices 1..T), Lambda- = mirror of ub."""
    Lt = S.Lt; T = Lt // 2; A0 = np.zeros(S.nl)
    for t in range(1, T + 1):
        for x in range(4):
            A0[S.key[('x', x, t % Lt)]] = ua['x'][t - 1, x]; A0[S.key[('x', x, (1 - t) % Lt)]] = ub['x'][t - 1, x]
    for t in range(1, T):
        for x in range(4):
            A0[S.key[('t', x, t)]] = ua['t'][t - 1, x]; A0[S.key[('t', x, (-t) % Lt)]] = -ub['t'][t - 1, x]
    offA = ub['x'][0] - ua['x'][0]; offB = ua['x'][T - 1] - ub['x'][T - 1]
    pA, wA = plane_nodes(offA, n); pB, wB = plane_nodes(offB, n)
    chi0 = 2 * np.pi * np.arange(nw) / nw; wc = np.full(nw, 2 * np.pi / nw)
    iA, iB, iC = [a.ravel() for a in np.meshgrid(np.arange(len(wA)), np.arange(len(wB)), np.arange(nw), indexing='ij')]
    A = np.repeat(A0[None], len(iA), 0)
    for x in range(4):
        A[:, S.key[('t', x, 0)]] = pA[iA, x]
        A[:, S.key[('t', x, T)]] = chi0[iC] + pB[iB, x]
    return A, wA[iA] * wB[iB] * wc[iC]


def entry_log(S, ua, ub, n, nw, fn_logs, CH=128):
    A, w = entry_fields(S, ua, ub, n, nw)
    l = np.concatenate([fn_logs(A[c:c + CH]) for c in range(0, len(A), CH)])
    lm = l.real.max(); return lm + np.log(np.sum(w * np.exp(l - lm)) + 0j), A
