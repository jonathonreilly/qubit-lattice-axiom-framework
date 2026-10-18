"""Shared model loader for the C20 independent checks: reuses only the supplied model definitions
(build_model + the seeded X, M construction copied from the runner's main), nothing else."""
import os, sys, itertools
import numpy as np
REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), *(['..'] * 5)))
sys.path.insert(0, os.path.join(REPO, 'scripts'))
import corner_fermion_interaction_channels_and_qubit_build_2026_10_18 as R


def load():
    Mdl = R.build_model()
    nV = Mdl['nV']; sym = Mdl['sym']; loc0 = Mdl['loc0']
    rng = np.random.default_rng(0)
    nbr = [Mdl['C']['VID'][(tuple(x % Mdl['L'] for x in d), c)] for d in [(0, 0, 0)] + list(Mdl['DIRS']) for c in Mdl['CORN']]
    seeds = []
    for trial in range(6):
        A = np.zeros((nV, nV))
        for i in loc0:
            for j in nbr:
                v, w = Mdl['VERTS'][i][0], Mdl['VERTS'][j][0]
                if i != j and sum(abs(Mdl['dmod'](y - x)) for x, y in zip(v, w)) <= 1: A[i, j] = rng.normal()
        A = A - A.T
        seeds.append(sym(1j * A, inversion=True))
    xv = np.random.default_rng(11).normal(size=6); xv /= np.linalg.norm(xv)
    X = np.tensordot(xv, np.array(seeds), 1); X /= np.abs(X).max()
    A_ = np.random.default_rng(42).normal(size=(12, 12)); A_ = A_ - A_.T
    S = np.zeros((nV, nV), complex); S[np.ix_(loc0, loc0)] = 1j * A_
    Mm = sym(S, Qmom=True, a2=True); Mm = (Mm + Mm.conj().T) / 2; Mm /= np.abs(Mm).max()
    return Mdl, X, Mm, seeds


def bloch_fn(bl):
    shs = np.array(list(bl.keys()), float); Ms = np.array(list(bl.values()))
    def Hk(K):  # K: (n,3)
        ph = np.exp(1j * K @ shs.T)          # (n, nsh)
        return np.einsum('ns,sij->nij', ph, Ms)
    return Hk
