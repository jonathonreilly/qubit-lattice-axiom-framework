#!/usr/bin/env python3
"""Checks of the second-order flux formula and of the spin coefficient.

PRE-STATED criteria.
 M1. Scalar, d=2: for D_theta^* D_theta + tau^2 on an N x N torus with flux theta = 2 pi m / N^2 per plaquette, the per-site
     log det has theta^2 coefficient  c2 = int dQ/(2 pi)^2 D(T), T = Qhat^2 + tau^2, with
     D(T) = P/(16 T^2) - Ptilde/(12 T^3), P = 2 (T11 T22 - T12^2), Ptilde = T1^2 T22 - 2 T1 T2 T12 + T2^2 T11.
     Fit the coefficient from m = 1,2,3 (theta^2, theta^4, constant, Richardson). PASS if agreement within 0.5 percent, at tau = 1, 0.5.
 M2. Spin: on the d=3, N=9 torus of hard-core--mapped_onshell_flux.py the lowest eigenvalue of K_f in the charged sector at theta = 2 phi
     is within 15 percent of -theta, the lowest level of -D^2 - 2F. PASS or FAIL as stated.
 M4. Lemma 3.8 (matrix form, h_0 diagonal and not scalar) on an explicit Hermitian twisted symbol, d=2, N=24: even part of the theta^2 coefficient from
     m = +-1,+-2,+-3 against the formula, within 1 percent.
 M3. Invariance of the combination -log|det G| - log|det(D_1^* G^-1 D_1)| under Q -> Q^o = Q - D_1 Phi, with Phi the covariant
     contour average, tolerance 1e-8. If Q^o is not constructed exactly the check reports the residual.
RSS guard 2 GB.
"""
import math, itertools, sys, resource, importlib.util, os
import numpy as np

def rss_guard():
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform == 'darwin':
        r /= 1024
    if r > 2_000_000:
        raise SystemExit("RSS above 2 GB")

def Dsym(tau, n=400):
    Q = (np.arange(n)+0.5)*2*np.pi/n-np.pi
    q1, q2 = np.meshgrid(Q, Q, indexing='ij')
    T = 2*(1-np.cos(q1))+2*(1-np.cos(q2))+tau**2
    T1 = 2*np.sin(q1); T2 = 2*np.sin(q2); T11 = 2*np.cos(q1); T22 = 2*np.cos(q2); T12 = 0*q1
    P = 2*(T11*T22-T12**2)
    Pt = T1**2*T22-2*T1*T2*T12+T2**2*T11
    return np.mean(P/(16*T**2)-Pt/(12*T**3))

def logdet_flux(N, m, tau):
    th = 2*math.pi*m/N**2
    # Landau gauge A_2 = th x_1, wrap in direction 1 with -th N x_2; blocks in q_2 not used because the wrap couples them: dense
    ns = N*N
    A = np.zeros((ns,ns),dtype=complex)
    idx = lambda x,y: (x%N)*N+(y%N)
    for x in range(N):
        for y in range(N):
            i = idx(x,y)
            A[i,i] += 4+tau**2
            # direction 2
            j = idx(x,y+1); ph = np.exp(1j*th*x)
            A[i,j] -= ph; A[j,i] -= np.conj(ph)
            # direction 1
            j = idx(x+1,y); ph = np.exp(-1j*th*N*y) if x == N-1 else 1.0
            A[i,j] -= ph; A[j,i] -= np.conj(ph)
    s, l = np.linalg.slogdet(A)
    return l/ns

def m1(N=48):
    res = []
    for tau in (1.0, 0.5):
        vals = [logdet_flux(N, m, tau) for m in (0,1,2,3)]
        th = [2*math.pi*m/N**2 for m in (1,2,3)]
        d = [vals[i+1]-vals[0] for i in range(3)]
        # fit d = c th^2 + e th^4 + f th^6
        X = np.array([[t**2, t**4, t**6] for t in th])
        c = np.linalg.solve(X, np.array(d))[0]
        res.append((tau, c, Dsym(tau)))
        rss_guard()
    return res

def load_onshell():
    here = os.path.dirname(os.path.abspath(__file__))
    spec = importlib.util.spec_from_file_location('onshell', os.path.join(here, 'hard-core--mapped_onshell_flux.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def m2m3():
    o = load_onshell()
    lat, conf, _ = o.run(1)
    H, D = o.charged_ops(lat, conf)
    K = H+D@D.conj().T
    ev = np.linalg.eigvalsh((K+K.conj().T)/2)
    theta = 2*lat.phi
    Nc, Ac = o.coarse_data(lat, conf)
    D1 = o.coarse_D(lat, Nc, Ac)
    Q = o.Q_charged(lat, conf)
    # contour average Phi: covariant, base at the block centre
    N = lat.N; d = o.d; L = o.L
    A = lat.A
    Phi = np.zeros((Nc**d, d*N**d),dtype=complex)
    for yc in itertools.product(range(Nc),repeat=d):
        y = tuple(L*v for v in yc)
        row = 0
        for v in yc:
            row = row*Nc+v
        for x in o.block:
            G = o.axial_contours(y,x)
            for g in G:
                wt = 1.0/(len(o.block)*len(G))
                phase = 0.0
                for a,b in zip(g[:-1],g[1:]):
                    diff = [b[i]-a[i] for i in range(d)]
                    m_ = [i for i in range(d) if diff[i]!=0][0]
                    if diff[m_]==1:
                        Phi[row, lat.bidx(a,m_)] += wt*np.exp(2j*phase)
                        phase += A(a,m_)
                    else:
                        phase -= A(b,m_)
                        Phi[row, lat.bidx(b,m_)] += -wt*np.exp(2j*phase)
    Qo = Q-D1@Phi
    Kinv = np.linalg.inv(K)
    def combo(QQ):
        G = QQ@Kinv@QQ.conj().T
        Ginv = np.linalg.inv(G)
        return -np.linalg.slogdet(G)[1]-np.linalg.slogdet(D1.conj().T@Ginv@D1)[1]
    rss_guard()
    # size of the contour part remaining in Qo at this flux
    return ev[:4], theta, combo(Q), combo(Qo), np.abs(Q).max(), np.abs(Qo).max(), np.linalg.norm(Q), np.linalg.norm(Qo)


def twisted_matrix(N, theta, taus):
    """Dense matrix of the operator with kernel exp(i (theta/2) x^y) tau(x-y) on the N x N torus with flux theta per plaquette,
    in the periodic Landau gauge. taus: dict {(z1,z2): 2x2 complex array}. Unwrapped phase: exp(i (theta/2)[x^y + y1 y2 - x1 x2]) with
    x, y unwrapped; folding y1 -> y1 - N n1 , y2 -> y2 - N n2 uses the magnetic boundary condition of the Landau gauge."""
    n = 2*N*N
    A = np.zeros((n,n),dtype=complex)
    for x1 in range(N):
        for x2 in range(N):
            for (z1,z2),t in taus.items():
                y1 = x1-z1; y2 = x2-z2
                ph = (theta/2)*(x1*y2-x2*y1+y1*y2-x1*x2)
                f1 = y1 % N; f2 = y2 % N
                n1 = (y1-f1)//N
                # T(x1+N,x2;y1+N,y2) = exp(-i theta N (x2-y2)) T(x;y), so the boundary condition preserved by T is
                # psi(y1+N n1, y2) = exp(-i theta N n1 y2) psi(y1,y2); y2 periodic
                ph2 = -theta*N*n1*f2
                i = (x1*N+x2)*2; j = (f1*N+f2)*2
                A[i:i+2,j:j+2] += t*np.exp(1j*(ph+ph2))
    return A

def m4(N=24):
    """Lemma 3.8 on a random symbol with diagonal, non-scalar, positive h_0."""
    rng = np.random.default_rng(7)
    I = np.eye(2,dtype=complex)
    # h_0 diag: a + sum b_i 2(1-cos Q_i), different per component
    def lap(c1,c2,a):
        t = {}
        t[(0,0)] = a+2*c1+2*c2
        t[(1,0)] = -c1; t[(-1,0)] = -c1; t[(0,1)] = -c2; t[(0,-1)] = -c2
        return t
    t11 = lap(1.0,0.7,0.9); t22 = lap(0.6,1.3,1.1)
    tau0 = {}
    for k,v in t11.items():
        tau0.setdefault(k,np.zeros((2,2),dtype=complex))[0,0] += v
    for k,v in t22.items():
        tau0.setdefault(k,np.zeros((2,2),dtype=complex))[1,1] += v
    # h_1: Hermitian, off-diagonal i u + hopping, diagonal hopping
    tau1 = {}
    def add(d,k,i,j,v):
        d.setdefault(k,np.zeros((2,2),dtype=complex))[i,j] += v
    add(tau1,(0,0),0,1,-1.0j); add(tau1,(0,0),1,0,+1.0j)         # spin-like
    add(tau1,(1,0),0,1,0.2); add(tau1,(-1,0),1,0,0.2)            # h_1,12(z)=conj h_1,21(-z)
    add(tau1,(1,1),0,0,0.15); add(tau1,(-1,-1),0,0,0.15)
    tau2 = {}
    add(tau2,(0,0),0,0,0.5); add(tau2,(0,0),1,1,-0.3); add(tau2,(0,1),1,1,0.1); add(tau2,(0,-1),1,1,0.1)
    def op(th):
        taus = {}
        for d,c in ((tau0,1.0),(tau1,th),(tau2,th*th)):
            for k,v in d.items():
                taus.setdefault(k,np.zeros((2,2),dtype=complex))
                taus[k] = taus[k]+c*v
        return twisted_matrix(N,th,taus)
    vals = {}
    for m in (-3,-2,-1,1,2,3,0):
        th = 2*math.pi*m/N**2
        A = op(th)
        if m == 2:
            herm = np.abs(A-A.conj().T).max()
        s,l = np.linalg.slogdet(A)
        vals[m] = l/(N*N)
        rss_guard()
    th1 = 2*math.pi/N**2
    d = [ (vals[m]+vals[-m])/2-vals[0] for m in (1,2,3)]
    X = np.array([[(m*th1)**2,(m*th1)**4,(m*th1)**6] for m in (1,2,3)])
    fit = np.linalg.solve(X,np.array(d))[0]
    # formula on a fine grid
    n = 512
    Q = (np.arange(n)+0.5)*2*np.pi/n-np.pi
    q1,q2 = np.meshgrid(Q,Q,indexing='ij')
    def sym(d):
        out = np.zeros((2,2)+q1.shape,dtype=complex)
        for (z1,z2),t in d.items():
            ph = np.exp(-1j*(q1*z1+q2*z2))
            for i in range(2):
                for j in range(2):
                    out[i,j] += t[i,j]*ph
        return out
    h0 = sym(tau0); h1 = sym(tau1); h2 = sym(tau2)
    def Dfun(c1,c2,a):
        T = a+2*c1*(1-np.cos(q1))+2*c2*(1-np.cos(q2))
        T1 = 2*c1*np.sin(q1); T2 = 2*c2*np.sin(q2); T11 = 2*c1*np.cos(q1); T22 = 2*c2*np.cos(q2)
        P = 2*(T11*T22); Pt = T1**2*T22+T2**2*T11
        return P/(16*T**2)-Pt/(12*T**3), T
    D1,T1_ = Dfun(1.0,0.7,0.9); D2,T2_ = Dfun(0.6,1.3,1.1)
    dens = (h2[0,0].real/T1_+h2[1,1].real/T2_)+D1+D2-0.5*(np.abs(h1[0,0])**2/(T1_*T1_)+np.abs(h1[1,1])**2/(T2_*T2_)+2*np.abs(h1[0,1])**2/(T1_*T2_))
    # the theta^1 coefficient must vanish in the even part; report the formula value
    return fit, dens.mean(), herm

if __name__ == '__main__':
    ok = True
    for tau, c, s in m1():
        rel = abs(c-s)/abs(s)
        print(f"M1 tau={tau}: fitted {c:.8f}  formula {s:.8f}  rel {rel:.2e}")
        ok = ok and rel < 5e-3
    ev, theta, a, b, q1, q2, n1, n2 = m2m3()
    print("M2 lowest eigenvalues", ev, " -theta =", -theta, " ratio", ev[0]/(-theta))
    ok = ok and abs(ev[0]/(-theta)-1) < 0.15
    print("M3 combination with Q, with Q^o, difference:", a, b, a-b)
    print("   max |Q|, |Q^o|, norm Q, norm Q^o:", q1, q2, n1, n2)
    ok = ok and abs(a-b) < 1e-8
    fit, form, herm = m4()
    rel = abs(fit-form)/abs(form)
    print(f"M4 matrix formula, diagonal non-scalar h0: fitted {fit:.8f}  formula {form:.8f}  rel {rel:.2e}  hermiticity defect {herm:.1e}")
    ok = ok and rel < 1e-2 and herm < 1e-10
    print("PASS" if ok else "FAIL")
