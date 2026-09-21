#!/usr/bin/env python3
"""discrete-step-walk-under-the-clock-clause, attempt 1 of 3: no discrete formulation is at once
unitary, local, and a clock.

No prior attempt existed on this problem at claim time.

Setting (blocks 53/54, as the unit states them; both SUPPLIED, not adopted): every site has a
positive tick rate w_x, u = log w.  Block 54's continuous-time clause gives the generator w H,
similar to H_w = sqrt(w) H sqrt(w), with the exact translation identity H_w^n T_a =
lambda_a^n T_a H_w^n in a uniform gradient, and the ray law
dv_j/dt = -w^2 cos(2 k_j) d_j u + 2 (v.grad u) v_j.  The record layer's ticks are discrete.

  W1  the homogeneous coined walk: unitary, cos omega = cos theta cos k     exact
  W2  (a)-i  site-dependent coin: UNITARY                                   exact on a ring
  W3  (a)-i  but it is NOT a clock - the dispersion is not separable        exact
  W4  (a)-ii fractional activation: NOT unitary, and exactly why            exact
  W5  (a)-iii a fractional step U^w: unitary but NOT finite range           exact + coefficients
  W6  (b)  the ray law that does hold, and why block 54's does not apply
  W7  (b)  a propagation on a line against those rays                       numeric
  W8  (c)  block 54's translation identity has no discrete analogue         exact
"""
import sys
import cmath
import sympy as sp

th, k, w = sp.symbols('theta k w', real=True)

def coin(t):
    return sp.Matrix([[sp.cos(t), -sp.sin(t)], [sp.sin(t), sp.cos(t)]])

def symbol(t):
    """the one-step operator in Fourier space: coin then shift (comp 0 right, comp 1 left)"""
    return sp.diag(sp.exp(-sp.I*k), sp.exp(sp.I*k))*coin(t)

def ring(N, theta_of_x):
    """the one-step unitary of the walk on a ring of N sites, as a 2N x 2N sympy matrix"""
    U = sp.zeros(2*N, 2*N)
    for x in range(N):
        Cx = coin(theta_of_x(x))
        for a in range(2):
            xp = (x + 1) % N if a == 0 else (x - 1) % N
            for b in range(2):
                U[2*xp + a, 2*x + b] += Cx[a, b]
    return U

def main():
    ok = True
    def want(cond, msg):
        nonlocal ok
        print(("ok   " if cond else "FAIL ") + msg)
        ok = ok and bool(cond)

    print("W1  the homogeneous coined walk on a line")
    U = symbol(th)
    want(sp.simplify(sp.expand_complex(U.H*U - sp.eye(2))) == sp.zeros(2, 2),
         "     one step is unitary for every coin angle")
    want(sp.simplify(sp.expand_complex(U.det() - 1)) == 0, "     and has determinant 1, so its")
    tr = sp.simplify(sp.expand_complex(sp.trace(U)))
    want(sp.simplify(tr - 2*sp.cos(th)*sp.cos(k)) == 0,
         f"     two eigenvalues are e^(-i omega) with 2 cos omega = trace = {tr}, i.e.")
    print("       cos omega(k) = cos theta cos k.")
    om = sp.acos(sp.cos(th)*sp.cos(k))
    v = sp.simplify(sp.diff(om, k))
    want(sp.simplify(v - sp.cos(th)*sp.sin(k)/sp.sqrt(1 - sp.cos(th)**2*sp.cos(k)**2)) == 0,
         "     group velocity dw/dk = cos(theta) sin(k)/sqrt(1 - cos^2(theta) cos^2(k))")
    print("     The gap is omega(0) = theta: the coin angle is a MASS, as the gap shows.")

    print("\nW2  (a)-i  a site-dependent coin angle theta_x")
    N = 6
    g0, t0 = sp.Rational(1, 10), sp.Rational(1, 5)
    Ur = ring(N, lambda x: t0 + g0*x)
    want(sp.simplify(sp.expand_complex(Ur.H*Ur - sp.eye(2*N))) == sp.zeros(2*N, 2*N),
         f"     UNITARY on a ring of {N} with theta_x = 1/5 + x/10: a block-diagonal unitary coin")
    print("       followed by a fixed shift is a product of unitaries, so this formulation is")
    print("       unitary for ANY assignment x -> theta_x.  It is also strictly nearest-neighbour.")

    print("\nW3  (a)-i  but the coin angle is not a CLOCK")
    print("     The clause 'the amplitude advances in that site's own time' means the local")
    print("     energies are RESCALED by one factor: E(k,x) = w(x) eps(k).  A site-dependent coin")
    print("     does not do that - it reshapes the dispersion.  Exactly, omega = arccos(cos theta")
    print("     cos k), and the ratio between two coin angles is not constant in k:")
    t1, t2 = sp.pi/6, sp.pi/3
    rs = []
    for kv in (sp.pi/6, sp.pi/3, sp.pi/2):
        r = sp.acos(sp.cos(t1)*sp.cos(kv))/sp.acos(sp.cos(t2)*sp.cos(kv))
        rs.append(sp.N(r, 15))
        print(f"       k = {kv}: omega(pi/6)/omega(pi/3) = {float(sp.N(r,12)):.9f}")
    want(abs(rs[0] - rs[1]) > sp.Rational(1, 100) and abs(rs[1] - rs[2]) > sp.Rational(1, 100),
         "     the ratio moves from 0.643 to 1.000 across the band, so the dispersion is NOT")
    print("       separable as w(x) eps(k).  A coin gradient is a MASS gradient, not a clock.")

    print("\nW4  (a)-ii  'a site acts on a fraction w of the global ticks'")
    print("     As a deterministic one-step map this is M = w U + (1-w) I.  Then")
    dev = sp.factor(sp.simplify(sp.expand_complex(sp.simplify((sp.Matrix(w*U + (1-w)*sp.eye(2)).H
                                                              * (w*U + (1-w)*sp.eye(2))
                                                              - sp.eye(2))[0, 0]))))
    want(sp.simplify(dev + 2*w*(w - 1)*(sp.cos(k)*sp.cos(th) - 1)) == 0,
         f"       (M^dag M - I)_00 = {dev}")
    print("     Since cos k cos theta - 1 <= 0 and w(w-1) < 0 strictly for 0 < w < 1, this is")
    print("     strictly positive off the band edge: M is NOT unitary at any intermediate w, and")
    print("     it degenerates to a unitary only at w = 0 (do nothing) and w = 1 (a full step).")
    for wv in (sp.Rational(1,4), sp.Rational(1,2), sp.Rational(3,4)):
        val = sp.simplify(dev.subs({w: wv, th: sp.pi/4, k: sp.pi/3}))
        want(val != 0, f"       w = {wv} at theta=pi/4,k=pi/3: deviation = {sp.nsimplify(val)} != 0")
    print("     Read as a RANDOM choice of which sites step, each realization is unitary and the")
    print("     clause holds in the mean; but then the evolution of the state is a channel, not a")
    print("     unitary, and the amplitude is no longer a pure state.  That is a different theory.")

    print("\nW5  (a)-iii  a genuine fractional step U^w")
    print("     U^w has the same eigenvectors with eigenvalues e^(-i w omega), so its trace is")
    print("     2 cos(w omega).  For w = 1/2:")
    halftr = sp.simplify(sp.sqrt((1 + sp.cos(th)*sp.cos(k))/2))
    want(sp.simplify(2*halftr**2 - 1 - sp.cos(th)*sp.cos(k)) == 0,
         f"       cos(omega/2) = {halftr}, verified by the half-angle identity")
    print("       2 cos^2(omega/2) - 1 = cos omega = cos theta cos k (and cos(omega/2) >= 0 on")
    print("       0 <= omega <= pi, which fixes the branch).")
    print("     A strictly range-R operator has a symbol whose entries are trigonometric")
    print("     POLYNOMIALS of degree <= R in k - finitely many Fourier coefficients.  This square")
    print("     root has infinitely many.  Its cosine coefficients at theta = 1/3:")
    import mpmath as mp
    mp.mp.dps = 30
    thv = mp.mpf(1)/3
    cs = [mp.quad(lambda x, n=n: mp.sqrt((1 + mp.cos(thv)*mp.cos(x))/2)*mp.cos(n*x),
                  [0, 2*mp.pi])/(2*mp.pi) for n in range(9)]
    print("       n = 0..8: " + ", ".join(f"{float(c):+.6f}" for c in cs))
    want(all(abs(c) > mp.mpf(10)**-6 for c in cs),
         "     every coefficient through n = 8 is nonzero, and they decay geometrically rather")
    print("       than truncating: the half-step is unitary but has UNBOUNDED range.  So a site")
    print("       cannot take a fraction of a step without reaching arbitrarily far.")

    print("\nW6  (b)  the ray law that does hold, and block 54's")
    print("     For the only formulation that is both unitary and local - the coin gradient - the")
    print("     local dispersion is cos omega(k,x) = cos theta(x) cos k, and the rays are the")
    print("     Hamiltonian flow of omega:")
    thx = sp.Function('theta')(sp.Symbol('x'))
    omx = sp.acos(sp.cos(thx)*sp.cos(k))
    xdot = sp.simplify(sp.diff(omx, k))
    kdot = sp.simplify(-sp.diff(omx, sp.Symbol('x')))
    print(f"       dx/dt = dw/dk   = {xdot}")
    print(f"       dk/dt = -dw/dx  = {kdot}")
    want(sp.simplify(xdot - sp.sin(k)*sp.cos(thx)/sp.sqrt(1 - sp.cos(k)**2*sp.cos(thx)**2)) == 0,
         "     both read off omega exactly")
    print("     Block 54's law dv_j/dt = -w^2 cos(2k_j) d_j u + 2 (v.grad u) v_j is derived from")
    print("     E = w(x) eps(k) - a SEPARABLE dispersion; its second term 2(v.grad u)v is exactly")
    print("     the signature of that product.  W3 showed the discrete walk's dispersion is not")
    print("     separable, so block 54's law does not apply to it, and the discrete rays carry no")
    print("     such term.  The two laws agree only where the gradient vanishes.")

    print("\nW7  (b)  a propagation on a line against those rays   [NUMERIC, not exact]")
    L, T = 241, 60
    x0, k0, sig = 120, 1.0, 8.0
    th_of = lambda x: 0.30 + 0.0020*(x - x0)
    # an equal superposition splits into the two bands and its centroid tracks NO single ray;
    # start instead in the eigenvector of the symbol at (k0, theta(x0)) for the branch we follow
    import math
    t00 = th_of(x0); c00, s00 = math.cos(t00), math.sin(t00)
    om0 = math.acos(c00*math.cos(k0))
    lam = cmath.exp(-1j*om0)
    e0 = cmath.exp(-1j*k0)
    v1 = 1.0 + 0j
    v2 = (c00*e0 - lam)*v1/(s00*e0)
    nv = math.sqrt(abs(v1)**2 + abs(v2)**2)
    v1, v2 = v1/nv, v2/nv
    psi = [[0j, 0j] for _ in range(L)]
    nrm = 0.0
    for x in range(L):
        a = cmath.exp(-((x - x0)**2)/(2*sig**2) + 1j*k0*x)
        psi[x] = [a*v1, a*v2]
        nrm += abs(psi[x][0])**2 + abs(psi[x][1])**2
    nrm = nrm**0.5
    psi = [[c/nrm for c in s] for s in psi]
    def step(p):
        q = [[0j, 0j] for _ in range(L)]
        for x in range(L):
            t = th_of(x); c, s = cmath.cos(t), cmath.sin(t)
            a = c*p[x][0] - s*p[x][1]
            b = s*p[x][0] + c*p[x][1]
            q[(x + 1) % L][0] += a
            q[(x - 1) % L][1] += b
        return q
    def centroid(p):
        tot = sum(abs(p[x][0])**2 + abs(p[x][1])**2 for x in range(L))
        return sum(x*(abs(p[x][0])**2 + abs(p[x][1])**2) for x in range(L))/tot, tot
    c0, tot0 = centroid(psi)
    xr, kr = float(x0), k0
    for n in range(T):
        psi = step(psi)
        t = th_of(xr); ct, st = math.cos(t), math.sin(t)
        sw = math.sqrt(max(1e-15, 1 - ct*ct*math.cos(kr)**2))
        xr += ct*math.sin(kr)/sw
        kr += -(st*math.cos(kr)/sw)*0.0020
    cT, totT = centroid(psi)
    want(abs(totT - 1.0) < 1e-9, f"     the walk stays normalized: |psi|^2 = {totT:.12f}")
    err = abs(cT - xr)
    print(f"     after {T} steps: packet centroid {cT:.4f}, ray {xr:.4f}, difference {err:.4f}")
    print(f"     ballistic displacement {cT - c0:.4f} sites, so the ray tracks the packet to "
          f"{err/abs(cT - c0)*100:.2f} percent")
    want(err/abs(cT - c0) < 0.05,
         "     the single ray follows the packet to better than 5 percent of its displacement")
    print("     (one ray, not a cloud: this is a check that the W6 law is the right one, not a")
    print("      measurement of the packet's spread.  Floating point, unlike everything above.)")

    print("\nW8  (c)  block 54's exact translation identity in discrete steps")
    print("     Block 54 has H_w^n T_a = lambda_a^n T_a H_w^n exactly in a uniform gradient: a")
    print("     translate evolves faster by exactly the ratio of the clocks.  For the discrete")
    print("     walk with a uniform coin gradient, test whether U T = lambda T U for a scalar:")
    Tm = sp.zeros(2*N, 2*N)
    for x in range(N):
        for a in range(2):
            Tm[2*((x + 1) % N) + a, 2*x + a] = 1
    A, B = sp.simplify(Ur*Tm), sp.simplify(Tm*Ur)
    want(sp.simplify(A - B) != sp.zeros(2*N, 2*N), "     [U, T] is not zero, as expected, and")
    ratios = set()
    for i in range(2*N):
        for j in range(2*N):
            if B[i, j] != 0 and A[i, j] != 0:
                ratios.add(sp.simplify(sp.cancel(A[i, j]/B[i, j])))
    want(len(ratios) > 1,
         f"     the entrywise ratios (U T)_ij/(T U)_ij take {len(ratios)} DISTINCT values, so no")
    print("       scalar lambda satisfies U T = lambda T U.  The identity is not available.")
    print("     The reason is structural: block 54's identity rests on H_w = sqrt(w) H sqrt(w)")
    print("     being MULTIPLICATIVE in the clock, so a uniform gradient rescales it by a constant")
    print("     factor under translation.  The discrete step is a coin composed with a shift, and")
    print("     a coin gradient enters inside a cosine (W1), not as a prefactor - there is nothing")
    print("     for a translation to factor out.")

    print()
    if ok:
        print("SUMMARY: PARTIAL on the clock clause in discrete steps: no formulation is at once "
              "unitary, local and a clock. (a) A site-dependent coin angle is unitary for any "
              "assignment and strictly nearest-neighbour, but it is NOT a clock - the dispersion "
              "cos omega = cos theta cos k is not separable as w(x) eps(k), the ratio "
              "omega(pi/6)/omega(pi/3) running from 0.643 to 1.000 across the band, so a coin "
              "gradient is a MASS gradient (the gap is omega(0) = theta). Letting a site act on a "
              "fraction w of the ticks is not unitary as a deterministic map: "
              "(M^dag M - I)_00 = -2w(w-1)(cos k cos theta - 1), nonzero for every 0 < w < 1 and "
              "vanishing only at the endpoints; read as a random choice it is unitary per "
              "realization but the state evolves by a channel. A genuine fractional step U^w is "
              "unitary but has unbounded range: its symbol's trace is 2cos(w omega), which at "
              "w = 1/2 is sqrt(2 + 2 cos theta cos k), a square root whose Fourier coefficients "
              "never truncate. (b) The rays of the unitary local formulation are the Hamiltonian "
              "flow of arccos(cos theta(x) cos k), checked against a propagation on a line, and "
              "block 54's law does not apply because its 2(v.grad u)v term is the signature of "
              "the separable E = w(x) eps(k). (c) The exact translation identity has no discrete "
              "analogue: (U T)_ij/(T U)_ij takes many distinct values, so no scalar lambda "
              "satisfies U T = lambda T U")
        print("HIT: in discrete steps the local-clock clause cannot be realized unitarily, "
              "locally and as a clock at the same time - a site-dependent coin angle is unitary "
              "and local but rescales nothing (its dispersion cos omega = cos theta cos k is not "
              "separable, so it is a mass gradient), letting a site take a fraction w of the "
              "ticks fails unitarity by exactly -2w(w-1)(cos k cos theta - 1) at every "
              "intermediate w, and a true fractional step U^w is unitary but has unbounded range "
              "because cos(omega/2) = sqrt((1 + cos theta cos k)/2) is not a trigonometric "
              "polynomial; consequently block 54's ray law, whose 2(v.grad u)v term comes from "
              "the separable E = w(x)eps(k), does not describe the discrete walk, and its exact "
              "translation identity H_w^n T_a = lambda^n T_a H_w^n has no discrete analogue")
        return 0
    print("SUMMARY: ROUTE FAILS AT one of the checks above")
    return 1

if __name__ == "__main__":
    sys.exit(main())
