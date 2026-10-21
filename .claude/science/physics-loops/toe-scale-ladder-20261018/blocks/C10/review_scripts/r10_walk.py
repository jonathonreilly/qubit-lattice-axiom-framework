"""Reviewer's own construction of the C7 walk (from the parent note's G(b), Theorems 1-2), numpy and mpmath."""
import numpy as np, mpmath as mp, sympy as sp

def Gmat(b0, b1, b2, M=np):
    return [[1-3*b0**2, -2*b0*b1, b1**2-b0**2-b0*b2, -3*b1*(b0-b2)],
            [-2*b0*b1, b0**2-2*b1**2, b1*(b0-b2), b0*b2-b1**2+b2**2],
            [b1**2-b0**2-b0*b2, b1*(b0-b2), 2*b1**2-b2**2, 2*b1*b2],
            [-3*b1*(b0-b2), b0*b2-b1**2+b2**2, 2*b1*b2, 3*b2**2]]

def bpoints(dps=50):
    """b*, b_iso, b_gold as mpmath numbers. u* = smallest positive root of det G(11/30, sqrt u, 3/20) (own computation)."""
    mp.mp.dps = dps
    u = sp.Symbol('u'); B1 = sp.Symbol('B1')
    d = sp.Matrix(Gmat(sp.Rational(11, 30), B1, sp.Rational(3, 20), sp)).det()
    q = sp.Poly(sp.expand(d).subs(B1**2, u).subs(B1, sp.sqrt(u)), u)
    q = sp.Poly(sp.expand(sp.expand(d).subs(B1, sp.sqrt(u))), u)
    roots = [r for r in q.nroots(n=dps) if r.is_real and r > 0]
    us = min(roots)
    r5, r6, r15 = mp.sqrt(5), mp.sqrt(6), mp.sqrt(15)
    return {'bstar': (mp.mpf(11)/30, mp.sqrt(mp.mpf(str(us))), mp.mpf(3)/20),
            'iso': ((r6+2*r15)/27, (5*r6-2*r15)/27, (2*r15-2*r6)/27),
            'gold': ((9*r5-5)/38, (5*r5-7)/19, (71-29*r5)/38)}, us

t1 = np.array([[0, 1], [1, 0]], complex); t2 = np.array([[0, -1j], [1j, 0]]); t3 = np.diag([1., -1]).astype(complex); I2 = np.eye(2)
GAM = [np.kron(t1, I2), np.kron(t2, I2), np.kron(t3, t1), np.kron(t3, t2), np.kron(t3, t3)]

class Walk:
    """F rows: f = G phi0, h = 2x4 factor of G - f f^T, in a frame where e1 || W = H w (w = (0,1,2,1))."""
    def __init__(self, b, mpprec=False):
        self.b = b; self.mpprec = mpprec
        b0, b1, b2 = b
        G = mp.matrix(Gmat(*b, M=mp))
        phi0 = mp.matrix([1, 3, 3, 1])
        rf = G * phi0
        R = G - rf * rf.T
        E, Q = mp.eigsy(R)
        idx = sorted(range(4), key=lambda i: -E[i])[:2]
        H = mp.matrix(2, 4)
        for r, i in enumerate(idx):
            for j in range(4):
                H[r, j] = mp.sqrt(max(E[i], 0)) * Q[j, i]
        w = mp.matrix([0, 1, 2, 1]); W = H * w
        nW = mp.sqrt(W[0]**2 + W[1]**2)
        e1 = (W[0]/nW, W[1]/nW); e2 = (-e1[1], e1[0])
        Hr = mp.matrix(2, 4)
        for j in range(4):
            Hr[0, j] = e1[0]*H[0, j] + e1[1]*H[1, j]; Hr[1, j] = e2[0]*H[0, j] + e2[1]*H[1, j]
        self.rf, self.H, self.W = rf, Hr, Hr * w     # W = (|W|, 0) in this frame
        self.s = b0 + 2*b1 + b2
        self.rf_n = np.array([float(x) for x in rf]); self.H_n = np.array([[float(Hr[i, j]) for j in range(4)] for i in range(2)])
        self.b_n = [float(x) for x in b]; self.s_n = float(self.s)

    @staticmethod
    def phi(c, M=np):
        return [1, c[0]+c[1]+c[2], c[0]*c[1]+c[0]*c[2]+c[1]*c[2], c[0]*c[1]*c[2]]

    def comps(self, k, M=np):
        """(f0, h0 (2), g (3)) for the massless member."""
        if M is np:
            rf, H, (b0, b1, b2) = self.rf_n, self.H_n, self.b_n
            c = [np.cos(x) for x in k]; sn = [np.sin(x) for x in k]
        else:
            rf, H, (b0, b1, b2) = self.rf, self.H, self.b
            c = [mp.cos(x) for x in k]; sn = [mp.sin(x) for x in k]
        ph = self.phi(c)
        f = sum(rf[i]*ph[i] for i in range(4)); h = [sum(H[r, i]*ph[i] for i in range(4)) for r in range(2)]
        g = [sn[a]*(b0 + b1*(c[(a+1) % 3]+c[(a+2) % 3]) + b2*c[(a+1) % 3]*c[(a+2) % 3]) for a in range(3)]
        return f, h, g

    def U(self, k, theta=0.0, chi=0.0):
        """explicit 4x4 numpy matrix, massive member M U0 M, M = exp(i theta hhat.tau/2), hhat = (cos chi, sin chi) in W-frame."""
        f, h, g = self.comps(k)
        X = h[0]*GAM[0] + h[1]*GAM[1] + g[0]*GAM[2] + g[1]*GAM[3] + g[2]*GAM[4]
        U0 = f*np.eye(4) + 1j*X
        hh = np.cos(chi)*GAM[0] + np.sin(chi)*GAM[1]
        Mm = np.cos(theta/2)*np.eye(4) + 1j*np.sin(theta/2)*hh
        return Mm @ U0 @ Mm

GAMmp = [mp.matrix(G.tolist()) for G in GAM]

def Ump(walk, k, theta=0, chi=0):
    f, h, g = walk.comps(k, M=mp)
    X = h[0]*GAMmp[0] + h[1]*GAMmp[1] + g[0]*GAMmp[2] + g[1]*GAMmp[3] + g[2]*GAMmp[4]
    U0 = f*mp.eye(4) + mp.mpc(0, 1)*X
    hh = mp.cos(chi)*GAMmp[0] + mp.sin(chi)*GAMmp[1]
    Mm = mp.cos(mp.mpf(theta)/2)*mp.eye(4) + mp.mpc(0, 1)*mp.sin(mp.mpf(theta)/2)*hh
    return Mm*U0*Mm
