#!/usr/bin/env python3
"""Supervisor control, block 61 (floating point; NOT the exact runner): three lengths per site under the curvature member, second order.

Fields on sites: u (log rate) and lam_1, lam_2, lam_3 (log lengths along the three axes).  K = wbar = 1.
   F_2 = 2 u.[(D2+D3) lam_1 + (D1+D3) lam_2 + (D1+D2) lam_3]  -  2 [grad_3 lam_1.grad_3 lam_2 + grad_2 lam_1.grad_2 lam_3 + grad_1 lam_2.grad_1 lam_3]
   T_2 = M1 sum_i (dlam_i/dt)^2 + M2 sum_{i<m} (dlam_i/dt)(dlam_m/dt),    comparator: M1 = 0, M2 = -2.
D_i the second difference along axis i, grad_i the forward difference.
[W1] static, held walls, a body at rest: brute-force solve of the 4N linear equations; are the three lengths alike and equal to -u?  is the matrix non-singular?
[W2] static, a localised hop energy along axis 1 only: the response of lam_2 + u along the column in direction 3 through the source (a tent to the walls?), box sizes 7, 11, 15.
[W3] torus: frequencies from the 4x4 mode matrix at lattice wave vectors against the closed form  v = [(1 - 3 rho) +- sqrt((1 - rho)(1 - 9 rho))]/2,
     rho = abc/((a+b+c)(ab+ac+bc)), a = 4 sin^2(k_1/2) etc.;  and a direct time integration of the constrained system for one wave vector.
[W4] other kinetic terms (M1, M2): ratio of the fast mode's speed^2 on a body diagonal to that in a coordinate plane."""
import numpy as np
import itertools

def lap1(n):
    A = -2*np.eye(n) + np.eye(n, k=1) + np.eye(n, k=-1)
    return A

def box_ops(n):
    """Second differences along each axis on the n^3 interior with zero walls, as Kronecker products."""
    I = np.eye(n); L = lap1(n)
    return [np.kron(np.kron(L, I), I), np.kron(np.kron(I, L), I), np.kron(np.kron(I, I), L)]

def static_matrix(n):
    D = box_ops(n); N = n**3; Z = np.zeros((N, N))
    # unknowns (lam1, lam2, lam3, u); rows: dF/dlam_1, dF/dlam_2, dF/dlam_3, dF/du   (each divided by 2)
    rows = [[Z, D[2], D[1], D[1]+D[2]],
            [D[2], Z, D[0], D[0]+D[2]],
            [D[1], D[0], Z, D[0]+D[1]],
            [D[1]+D[2], D[0]+D[2], D[0]+D[1], Z]]
    return np.block(rows), D

if __name__ == "__main__":
    n = 5; N = n**3
    A, D = static_matrix(n)
    idx = lambda s: (s[0]*n + s[1])*n + s[2]
    c = (n//2,)*3
    print(f"[W1] box {n+2}^3, held walls: smallest singular value of the static matrix = {np.linalg.svd(A, compute_uv=False).min():.4f} (non-singular: the static solution is unique)")
    rhs = np.zeros(4*N); e = 0.3; rhs[3*N + idx(c)] = -e/2          # dF/du = -e  ->  2 sum (...) lam = -e
    sol = np.linalg.solve(A, rhs); l1, l2, l3, u = (sol[i*N:(i+1)*N] for i in range(4))
    print(f"     body at rest of energy {e}: max |lam_1 - lam_2| = {np.abs(l1-l2).max():.1e}, max |lam_1 - lam_3| = {np.abs(l1-l3).max():.1e}, max |lam_1 + u| = {np.abs(l1+u).max():.1e};  u at the body {u[idx(c)]:.6f}")
    Dtot = D[0]+D[1]+D[2]; lam_iso = np.linalg.solve(Dtot, -e/4*np.eye(N)[idx(c)])
    print(f"     block 60's isotropic law 4 Lap lam = -e gives lam at the body {lam_iso[idx(c)]:.6f} against {l1[idx(c)]:.6f}")

    print("\n[W2] a localised hop energy tau = 1 along axis 1 only, at the centre; a_2 = lam_2 + u along the column in direction 3 through the source, and one site off that column:")
    for n in (5, 9, 13):
        N = n**3; A, D = static_matrix(n); idx = lambda s: (s[0]*n + s[1])*n + s[2]; c = n//2
        rhs = np.zeros(4*N); rhs[idx((c,c,c))] = 0.5                 # dF/dlam_1 = tau_1 -> [D3 (lam2+u) + D2 (lam3+u)] = tau/2
        sol = np.linalg.solve(A, rhs); l1, l2, l3, u = (sol[i*N:(i+1)*N] for i in range(4))
        col = [l2[idx((c,c,z))] + u[idx((c,c,z))] for z in range(n)]
        off = l2[idx((c,c+1,c))] + u[idx((c,c+1,c))]
        print(f"   box {n+2}^3: a_2 along the column = {np.array(col).round(4)};  one site off the column: {off:.1e};  height at the source {col[c]:.4f} against -(n+1)/16 = {-(n+1)/16:.4f}")
    print("   (a tent reaching the walls, its height growing with the box: the response to hop energy along one axis is not a field that falls off)")

    print("\n[W3] torus modes, comparator's kinetic term: omega^2/(a+b+c) from the 4x4 mode matrix against the closed form in rho:")
    def speeds(k, M1=0.0, M2=-2.0):
        a, b, c = (4*np.sin(np.array(k)/2)**2)
        s = a+b+c
        Kin = np.array([[2*M1, M2, M2],[M2, 2*M1, M2],[M2, M2, 2*M1]])
        Pot = -2*np.array([[0, c, b],[c, 0, a],[b, a, 0]])             # gradient energy's Hessian: -2 (c l1 l2 + b l1 l3 + a l2 l3)
        con = np.array([b+c, a+c, a+b])
        # constrained problem: omega^2 Kin x = Pot x + con mu, con.x = 0 -> project onto the plane con.x = 0
        Q = np.linalg.svd(con.reshape(1,3))[2][1:].T                 # 3x2 basis of the plane
        Kp, Pp = Q.T@Kin@Q, Q.T@Pot@Q
        w2 = np.linalg.eigvals(np.linalg.solve(Kp, Pp))
        return np.sort(w2.real)/s, np.abs(w2.imag).max()
    L = 24
    for kk in ((1,2,0),(3,5,0),(1,1,1),(2,2,2),(1,2,3),(2,5,7),(1,1,6)):
        k = 2*np.pi*np.array(kk)/L
        v, im = speeds(k)
        a, b, c = 4*np.sin(k/2)**2; rho = a*b*c/((a+b+c)*(a*b+a*c+b*c))
        cf = sorted([((1-3*rho) - np.sqrt((1-rho)*(1-9*rho)))/2, ((1-3*rho) + np.sqrt((1-rho)*(1-9*rho)))/2])
        print(f"   k = 2pi/{L} x {kk}: speeds^2 = {v.round(6)} (imag {im:.0e});  closed form {np.round(cf, 6)};  rho = {rho:.5f}")
    print("   (coordinate planes: 1 and 0;  body diagonal: 1/3 twice;  in between, two speeds that depend on direction at every wavelength)")

    # direct time integration of the constrained system at one wave vector (amplitudes of a single Fourier mode)
    k = 2*np.pi*np.array((1,2,3))/L; a, b, c = 4*np.sin(k/2)**2; s = a+b+c
    Kin = np.array([[0,-2,-2],[-2,0,-2],[-2,-2,0.0]]); Pot = -2*np.array([[0, c, b],[c, 0, a],[b, a, 0]]); con = np.array([b+c, a+c, a+b])
    Q = np.linalg.svd(con.reshape(1,3))[2][1:].T
    Kp, Pp = Q.T@Kin@Q, Q.T@Pot@Q
    w2, vecs = np.linalg.eig(np.linalg.solve(Kp, Pp))
    y = vecs[:,0].real.copy(); yd = np.zeros(2); dt = 0.002; acc = lambda y: -np.linalg.solve(Kp, Pp)@y
    zero_cross = []; t = 0.0; prev = y[0]
    for step in range(400000):
        yd += 0.5*dt*acc(y); y += dt*yd; yd += 0.5*dt*acc(y); t += dt
        if prev > 0 >= y[0] or prev < 0 <= y[0]: zero_cross.append(t)
        prev = y[0]
        if len(zero_cross) >= 5: break
    period = 2*(zero_cross[-1]-zero_cross[0])/(len(zero_cross)-1)
    print(f"   time integration, mode 0 at k = (1,2,3): omega^2 = {(2*np.pi/period)**2:.6f} against {w2[0].real:.6f}")

    print("\n[W4] other kinetic terms (M1, M2): fast speed^2 on the body diagonal over that in a coordinate plane, long wavelength:")
    for M1, M2 in ((0,-2),(1,-2),(1,0),(1,1),(2,-1),(-1,-3)):
        try:
            vd, imd = speeds(2*np.pi*np.array((1,1,1))/96, M1, M2); vp, imp = speeds(2*np.pi*np.array((1,1,0))/96, M1, M2)
            print(f"   (M1, M2) = ({M1}, {M2}): body diagonal {vd.round(4)}, coordinate plane {vp.round(4)}")
        except np.linalg.LinAlgError:
            print(f"   (M1, M2) = ({M1}, {M2}): singular kinetic form on the constraint plane")
