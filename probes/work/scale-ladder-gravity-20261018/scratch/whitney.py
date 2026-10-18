"""Whitney forms of every degree on a periodic simplicial complex (Bloch), for Hodge Laplacians / Dirac-Kahler.

k-simplex classes: canonical vertex tuples sorted by (type, cell) after translating the first vertex to the
origin cell; orientation = that sorted order. Coboundary d_k: (k+1)-cochains from k-cochains with Bloch phases.
Mass matrices M_k: L^2 inner products of Whitney forms, summed over 4-simplices.
"""
import itertools, math, numpy as np

def canon(vs):
    vs = sorted(vs, key=lambda v: (v[1], v[0]))
    b0 = np.array(vs[0][0])
    key = tuple((t, tuple(np.subtract(b, b0))) for b, t in vs)
    return key, tuple(b0), vs

class Forms:
    def __init__(self, C):
        self.C = C
        self.cls = [dict() for _ in range(5)]      # degree k -> {key: index}
        for s in C.simp:
            for k in range(5):
                for sub in itertools.combinations(s, k + 1):
                    key, _, _ = canon(list(sub))
                    if key not in self.cls[k]: self.cls[k][key] = len(self.cls[k])
        self.n = [len(c) for c in self.cls]
        # coboundary terms: for each (k+1)-class tau (at anchor 0), faces = drop one vertex
        self.dterms = []
        for k in range(4):
            terms = []
            for key, ti in self.cls[k + 1].items():
                verts = [(b, t) for t, b in key]
                for j in range(len(verts)):
                    face = verts[:j] + verts[j + 1:]
                    fkey, fanc, fsorted = canon(face)
                    # sign: orientation of face as it appears in tau (order induced) vs canonical order
                    perm = [fsorted.index(v) for v in face]
                    sign = (-1) ** j * self._perm_sign(perm)
                    terms.append((ti, self.cls[k][fkey], np.array(fanc, float), sign))
            self.dterms.append(terms)
        # mass-matrix terms per 4-simplex
        self.mterms = [[] for _ in range(5)]
        for s in C.simp:
            P = np.array([C.pos(v) for v in s]); E = P[1:] - P[0]
            vol = abs(np.linalg.det(E)) / 24
            Einv = np.linalg.inv(E)
            grads = [-(Einv.sum(axis=1))] + [Einv[:, i] for i in range(4)]
            Gg = np.array([[gi @ C.g0inv @ gj for gj in grads] for gi in grads]) if hasattr(C, 'g0inv') else np.array([[gi @ gj for gj in grads] for gi in grads])
            Ill = vol * (np.ones((5, 5)) + np.eye(5)) / 30.0           # int lambda_a lambda_b
            for k in range(5):
                subs = list(itertools.combinations(range(5), k + 1))
                info = []
                for sub in subs:
                    vs = [s[i] for i in sub]; key, anc, srt = canon(vs)
                    perm = [srt.index(v) for v in vs]; sg = self._perm_sign(perm)
                    info.append((self.cls[k][key], np.array(anc, float), sg, sub))
                for (ca, aa, sa, A) in info:
                    for (cb, ab, sb, Bs) in info:
                        val = 0.0
                        for j, ia in enumerate(A):
                            Ar = [x for x in A if x != ia]
                            for l, ib in enumerate(Bs):
                                Br = [x for x in Bs if x != ib]
                                det = np.linalg.det(Gg[np.ix_(Ar, Br)]) if k > 0 else 1.0
                                val += (-1) ** (j + l) * Ill[ia, ib] * det
                        val *= math.factorial(k) ** 2 * sa * sb
                        if abs(val) > 1e-15: self.mterms[k].append((ca, cb, aa, ab, val))

    @staticmethod
    def _perm_sign(p):
        p = list(p); s = 1
        for i in range(len(p)):
            while p[i] != i:
                j = p[i]; p[i], p[j] = p[j], p[i]; s = -s
        return s

    def d(self, k, q):
        q = np.asarray(q, complex); D = np.zeros((self.n[k + 1], self.n[k]), complex)
        for ti, fi, fanc, sg in self.dterms[k]: D[ti, fi] += sg * np.exp(1j * q @ fanc)
        return D

    def M(self, k, q):
        q = np.asarray(q, complex); Mm = np.zeros((self.n[k], self.n[k]), complex)
        for ca, cb, aa, ab, v in self.mterms[k]:
            Mm[ca, cb] += v * np.exp(1j * q @ (ab - aa))
        return Mm

    def hodge(self, k, q):
        """stiffness K_k = d_k^dag M_{k+1} d_k + M_k d_{k-1} M_{k-1}^{-1} d_{k-1}^dag M_k (holomorphic: dag -> (-q)^T)."""
        q = np.asarray(q, complex); Mk = self.M(k, q); K = np.zeros_like(Mk)
        if k < 4:
            K += self.d(k, -q).T @ self.M(k + 1, q) @ self.d(k, q)
        if k > 0:
            Dm = self.d(k - 1, q); Dmm = self.d(k - 1, -q)
            K += Mk @ Dm @ np.linalg.solve(self.M(k - 1, q), Dmm.T @ Mk)
        return K, Mk
