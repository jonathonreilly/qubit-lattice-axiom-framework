#!/usr/bin/env python3
"""Refuting pass, block 61 (floating point and symbolic; machinery disjoint from the exact runner's): tries to break each statement.

W1  the mode determinant derived afresh: the second-order Lagrangian written as a quadratic form in Fourier amplitudes and differentiated
    symbolically (the runner writes the matrix by hand); compared with the runner's formula in symmetric functions.
W2  real-space time evolution of the constrained lattice system on a 12^3 torus from a random start on the constraint surface (comparator's kinetic
    term): frequencies read from the time series of chosen Fourier components against the closed form; is the constraint kept?
W3  a search over kinetic terms (m_1, m_2) for one whose fast disturbance has the same speed in 200 random directions.
W4  equal hop energies along the three axes, brute-force static solve on a 9^3 box: is the response confined to columns, and how far does it reach?
W5  is the at-rest solution still 'alike' when the body sits off-centre, next to a wall?"""
import numpy as np
import sympy as sp

def symbolic_determinant():
    X,a,b,c,m1,m2 = sp.symbols("X a b c m1 m2", real=True)
    A1,A2,A3,U = sp.symbols("A1 A2 A3 U")
    T = m1*(A1**2+A2**2+A3**2) + m2*(A1*A2+A1*A3+A2*A3)
    # F_2 in Fourier space: D_k -> -kappa_k;  F_2 = 2U sum_j (Lap - D_j) A_j + 2 (A1 D3 A2 + A1 D2 A3 + A2 D1 A3)
    F2 = 2*U*(-(b+c)*A1 - (a+c)*A2 - (a+b)*A3) + 2*(-c*A1*A2 - b*A1*A3 - a*A2*A3)
    Q = X*T - F2
    v = (A1,A2,A3,U)
    H = sp.Matrix([[sp.diff(Q,p,q) for q in v] for p in v])
    s, sig, pi = a+b+c, a*b+a*c+b*c, a*b*c
    formula = -16*((2*m1-m2)*(m1*s**2-(m1+m2)*sig)*X**2 - 2*(m1*s**3-(2*m1+m2)*s*sig+3*(m1+m2)*pi)*X + 4*pi*s)
    return sp.expand(H.det()-formula) == 0

def closed_form(a,b,c):
    s, sig, pi = a+b+c, a*b+a*c+b*c, a*b*c
    if sig == 0: return []
    rho = pi/(s*sig)
    d = np.sqrt(max((1-rho)*(1-9*rho), 0.0))
    return sorted([s*((1-3*rho)-d)/2, s*((1-3*rho)+d)/2])

if __name__ == "__main__":
    print("[W1] determinant from the quadratic form by symbolic differentiation equals the runner's formula:", symbolic_determinant())

    print("\n[W2] real-space evolution, 12^3 torus, comparator's kinetic term (K = wbar = 1), leapfrog, dt = 0.02, 6000 steps:")
    L = 12; rng = np.random.default_rng(7)
    def d2(f, ax): return np.roll(f,1,ax) + np.roll(f,-1,ax) - 2*f
    kap = [4*np.sin(np.pi*np.fft.fftfreq(L)*1.0)**2 for _ in range(3)]
    KA, KB, KC = np.meshgrid(kap[0], kap[1], kap[2], indexing="ij")
    Sj = [KB+KC, KA+KC, KA+KB]                                           # Fourier symbol of -(Lap - D_j)
    def constraint(lam): return sum(d2(lam[j], ax) for j in range(3) for ax in range(3) if ax != j)
    def accel(lam):
        """lam_p'' + lam_q'' = (D_p + D_q) u + D_q lam_p + D_p lam_q  for each j;  u from the requirement that the constraint's second rate of change vanishes."""
        def R(u):
            out = []
            for j in range(3):
                p, q = [ax for ax in range(3) if ax != j]
                out.append(d2(u,p) + d2(u,q) + d2(lam[p],q) + d2(lam[q],p))
            return out
        def acc_from(Rv): return [(Rv[1]+Rv[2]-Rv[0])/2, (Rv[0]+Rv[2]-Rv[1])/2, (Rv[0]+Rv[1]-Rv[2])/2]
        a0 = acc_from(R(np.zeros_like(lam[0])))
        c0 = np.fft.fftn(constraint(a0))
        # response of the constraint of the acceleration to u, in Fourier space (linear, diagonal): compute symbol by probing with the symbols
        # acc_j(u) = (R_p + R_q - R_j)/2 with R_j(u) = -(s_j) u  ->  acc_j = (s_j - s_p - s_q)/2 u ; constraint symbol: sum_j (-S_j) acc_j
        sym = sum(-Sj[j]*((Sj[j] - Sj[(j+1)%3] - Sj[(j+2)%3])/2) for j in range(3))
        with np.errstate(divide="ignore", invalid="ignore"):
            uh = np.where(np.abs(sym) > 1e-12, -c0/sym, 0.0)
        u = np.real(np.fft.ifftn(uh))
        return acc_from(R(u)), u
    # random start projected onto the constraint surface, mode by mode
    lam = [rng.standard_normal((L,L,L)) for _ in range(3)]
    lh = [np.fft.fftn(f) for f in lam]
    norm = sum(S**2 for S in Sj)
    dot = sum(Sj[j]*lh[j] for j in range(3))
    with np.errstate(divide="ignore", invalid="ignore"):
        lh = [lh[j] - np.where(norm > 1e-12, Sj[j]*dot/norm, 0.0) for j in range(3)]
    lam = [np.real(np.fft.ifftn(h)) for h in lh]
    vel = [np.zeros((L,L,L)) for _ in range(3)]
    dt = 0.02; steps = 6000
    probes = {(1,1,0): [], (1,1,1): [], (1,2,3): [], (2,0,1): []}
    acc, u = accel(lam)
    for n in range(steps):
        vel = [vel[j] + 0.5*dt*acc[j] for j in range(3)]
        lam = [lam[j] + dt*vel[j] for j in range(3)]
        acc, u = accel(lam)
        vel = [vel[j] + 0.5*dt*acc[j] for j in range(3)]
        h0 = np.fft.fftn(lam[0])
        for kk in probes: probes[kk].append(h0[kk])
    print(f"     constraint after the run: max |sum_j (Lap - D_j) lam_j| = {np.abs(constraint(lam)).max():.2e}  (start: {0.0:.1e})")
    for kk, series in probes.items():
        series = np.array(series); spec = np.abs(np.fft.rfft(series.real*np.hanning(len(series))))
        freqs = 2*np.pi*np.fft.rfftfreq(len(series), dt)
        peaks = [i for i in range(2, len(spec)-1) if spec[i] > spec[i-1] and spec[i] > spec[i+1] and spec[i] > 0.05*spec[2:].max()]
        a, b, c = (4*np.sin(np.pi*np.array(kk)/L)**2)
        pred = [np.sqrt(x) for x in closed_form(a,b,c) if x > 1e-9]
        print(f"     k = 2pi/12 x {kk}: spectral peaks at omega = {[round(float(freqs[i]),3) for i in peaks]};  closed form {[round(float(p),3) for p in pred]}")

    print("\n[W3] search for a kinetic term whose fast disturbance is direction-free (spread of v over 200 random directions, long wavelength):")
    dirs = rng.standard_normal((200,3)); dirs /= np.linalg.norm(dirs, axis=1)[:,None]
    def spread(m):
        m1, m2 = m
        vs = []
        for n in dirs:
            a, b, c = (0.05*n)**2
            s, sig, pi = a+b+c, a*b+a*c+b*c, a*b*c
            co = [(2*m1-m2)*(m1*s**2-(m1+m2)*sig), -2*(m1*s**3-(2*m1+m2)*s*sig+3*(m1+m2)*pi), 4*pi*s]
            r = np.roots(co) if abs(co[0]) > 1e-30 else np.array([-co[2]/co[1]])
            r = r[np.abs(r.imag) < 1e-9].real
            if len(r) == 0: return 1e3
            vs.append(np.max(r)/s)
        vs = np.array(vs); return vs.std()/abs(vs.mean())
    best = (1e9, None)
    for m1 in np.linspace(-3, 3, 25):
        for m2 in np.linspace(-3, 3, 25):
            if abs(m1) + abs(m2) < 1e-9: continue
            sp_ = spread((m1, m2))
            if sp_ < best[0]: best = (sp_, (m1, m2))
    print(f"     smallest relative spread on a 25 x 25 grid of (m_1, m_2): {best[0]:.3f} at {tuple(round(float(v),2) for v in best[1])}  (the comparator's term: {spread((0.0,-2.0)):.3f})")

    print("\n[W4] equal hop energies 1/3 along the three axes at the centre of an 11^3 box (9^3 interior), brute-force solve of all 4 x 729 equations:")
    n = 9; N = n**3; I = np.eye(n); Ld = -2*np.eye(n)+np.eye(n,k=1)+np.eye(n,k=-1)
    D = [np.kron(np.kron(Ld,I),I), np.kron(np.kron(I,Ld),I), np.kron(np.kron(I,I),Ld)]; Z = np.zeros((N,N))
    A = np.block([[Z, D[2], D[1], D[1]+D[2]],[D[2], Z, D[0], D[0]+D[2]],[D[1], D[0], Z, D[0]+D[1]],[D[1]+D[2], D[0]+D[2], D[0]+D[1], Z]])
    idx = lambda s: (s[0]*n+s[1])*n+s[2]; c = n//2
    rhs = np.zeros(4*N)
    for j in range(3): rhs[j*N + idx((c,c,c))] = (1/3)/2
    sol = np.linalg.solve(A, rhs); l = [sol[j*N:(j+1)*N] for j in range(3)]; u = sol[3*N:]
    a1 = l[0] + u
    on_cols = max(abs(a1[idx(s)]) for s in [(c,c,z) for z in range(n)] + [(c,y,c) for y in range(n)])
    plane = max(abs(a1[idx((x,y,z))]) for x in (c-1,c,c+1) for y in range(n) for z in range(n))
    elsewhere = max(abs(a1[idx((x,y,z))]) for x in range(n) for y in range(n) for z in range(n) if abs(x-c) > 1)
    print(f"     lam_1 + u: largest value on the two columns through the source {on_cols:.4f}; on the three planes x = c-1, c, c+1: {plane:.4f}; anywhere else: {elsewhere:.1e}")
    print(f"     at the wall end of a column: {a1[idx((c,c,0))]:+.4f}  (K = 1)")

    print("\n[W5] a body at rest next to a wall (7^3 interior, body at (0,3,5)): max |lam_1 - lam_2|, |lam_1 - lam_3|, |lam_1 + u|:")
    n = 7; N = n**3; I = np.eye(n); Ld = -2*np.eye(n)+np.eye(n,k=1)+np.eye(n,k=-1)
    D = [np.kron(np.kron(Ld,I),I), np.kron(np.kron(I,Ld),I), np.kron(np.kron(I,I),Ld)]; Z = np.zeros((N,N))
    A = np.block([[Z, D[2], D[1], D[1]+D[2]],[D[2], Z, D[0], D[0]+D[2]],[D[1], D[0], Z, D[0]+D[1]],[D[1]+D[2], D[0]+D[2], D[0]+D[1], Z]])
    idx = lambda s: (s[0]*n+s[1])*n+s[2]
    rhs = np.zeros(4*N); rhs[3*N + idx((0,3,5))] = -0.5
    sol = np.linalg.solve(A, rhs); l = [sol[j*N:(j+1)*N] for j in range(3)]; u = sol[3*N:]
    print(f"     {np.abs(l[0]-l[1]).max():.1e}, {np.abs(l[0]-l[2]).max():.1e}, {np.abs(l[0]+u).max():.1e}")
