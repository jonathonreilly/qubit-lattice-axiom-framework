#!/usr/bin/env python3
"""the-sixteen-branches-and-the-ledger-with-a-staggered-mass a2 (w-jonathonsmac4f50-ja540).

Exact parts use integer-valued matrices (every entry a small Gaussian integer, so numpy arithmetic on them is exact)
or sympy; section N is floating point and labelled.
  E1 the maps with the staggered term: V_n (H + m eps) V_n = s_n H + m eps; Theta commutes with H + m eps;
     eps V_n (odd n) commutes; A_n = Theta V_n (odd n) no longer anticommutes; tau eps anticommutes (uniform field),
     and in a rate field sends the clocked massive walk to minus the walk in the translated field
  E2 the twin's energy density: e_z[tau eps psi] = - e_{z - e1}[psi], exact on random Gaussian-integer states
  E3 the chessboard of clocks with mass: phi H phi = H, m w eps = m(cosh a eps + sinh a); (H' - m sinh a)^2 = H^2 + (m cosh a)^2
  E4 the large-mass stiffness: the second-order sea energy -sum_bonds (w_x w_y/2)/(m(w_x + w_y)), expanded, has gradient
     coefficient +1/(8m) of (1/2) sum (u_x - u_y)^2
  N  kappa(m) on tori up to 32^3 by block diagonalisation (floating point, labelled)
"""
import sys
import numpy as np
import sympy as sp

FAILS = []
def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (("  [" + detail + "]") if detail else ""))
    if not ok: FAILS.append(name)

# ------------------------------------------------------------------ the walk on the 4^3 torus, scaled by 2i (integer entries)
L = 4; N = L**3
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], complex)
SIG = [sx, sy, sz]; I2 = np.eye(2)
def idx(x): return ((x[0] % L)*L + (x[1] % L))*L + (x[2] % L)
SITES = [(a, b, c) for a in range(L) for b in range(L) for c in range(L)]
E3 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
def hop(a, phi=None):
    """2i S_a with bond weights phi_x phi_y: (2i S_a psi)(x) = phi phi [psi(x+e_a) - psi(x-e_a)] (scaled)"""
    T = np.zeros((N, N), complex)
    for x in SITES:
        y = tuple(x[i] + E3[a][i] for i in range(3))
        f = 1 if phi is None else phi[idx(x)]*phi[idx(y)]
        T[idx(x), idx(y)] += f; T[idx(y), idx(x)] -= f
    return T
def walk(phi=None):          # 2i * phi H phi  (H = sum sigma_a S_a)
    return sum(np.kron(hop(a, phi), SIG[a]) for a in range(3))
eps_site = np.array([(-1)**sum(x) for x in SITES]); EPS = np.kron(np.diag(eps_site), I2)
def site_field(f): return np.kron(np.diag(f), I2)
m2i = 3                      # the mass, scaled: 2i * m eps -> use m = 3/(2i) * ... keep H' = walk + 2i m eps with m = 3
H2 = walk(); Hp = H2 + 2j*m2i*EPS    # 2i (H + m eps), m = 3
def eqz(A, B): return np.array_equal(A, B)
# species maps (block 70): U_n = (-1)^{n.x}, R_n = identity or sigma_c (c the axis rho_n keeps), s_n = det D_n
ok_even = ok_odd = ok_eps_odd = ok_A = True
for n in [(0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1), (1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1)]:
    Un = np.diag([(-1)**(n[0]*x[0] + n[1]*x[1] + n[2]*x[2]) for x in SITES])
    D = [(-1)**k for k in n]; s = int(np.prod(D)); rho = [s*d for d in D]
    keep = [i for i in range(3) if rho[i] == 1]
    Rn = I2 if len(keep) == 3 else SIG[keep[0]]
    V = np.kron(Un, Rn)
    VHV = V @ Hp @ V
    if s == 1: ok_even &= eqz(VHV, Hp)
    else:
        ok_odd &= eqz(VHV, -H2 + 2j*m2i*EPS)
        ok_eps_odd &= eqz(EPS @ V @ Hp @ V @ EPS, Hp)
        # A_n = Theta V_n, Theta = sigma_2 K: A H A^-1 = Theta (V H V) Theta^-1; Theta X Theta^-1 = S conj(X) S, S = 1 x sigma_2
        S2 = np.kron(np.eye(N), sy)
        AHA = S2 @ np.conj(VHV/(2j)) @ S2          # conjugate the unscaled operator (divide the 2i out first)
        ok_A &= not np.allclose(AHA, -Hp/(2j)) and np.allclose(AHA, (-H2 + 2j*m2i*EPS)/(2j))
check("E1.1 even species maps: V_n (H + m eps) V_n = H + m eps (m = 3, 4^3 torus, exact)", ok_even)
check("E1.2 odd species maps: V_n (H + m eps) V_n = -H + m eps; eps V_n commutes with H + m eps", ok_odd and ok_eps_odd)
S2 = np.kron(np.eye(N), sy)
check("E1.3 Theta = sigma_2 K commutes with H + m eps; the twin maps A_n = Theta V_n (odd n) send it to -H + m eps, not -(H + m eps)",
      np.allclose(S2 @ np.conj(Hp/(2j)) @ S2, Hp/(2j)) and ok_A)
TAU = np.zeros((N, N))
for x in SITES: TAU[idx((x[0] + 1, x[1], x[2])), idx(x)] = 1      # (tau psi)(x + e1) = psi(x)
TAUc = np.kron(TAU, I2)
check("E1.4 tau eps (translation by e1 after the site sign) anticommutes with H + m eps in a uniform field",
      eqz(TAUc @ EPS @ Hp @ EPS @ TAUc.T, -Hp))
rng = np.random.default_rng(3); phi = rng.integers(1, 4, N)
Hw = walk(phi) + 2j*m2i*EPS @ site_field(phi**2)                    # 2i(phi H phi + m w eps), w = phi^2
phi_t = TAU @ phi                                                   # the translated field (tau phi)(x + e1) = phi(x)
Hw_t = walk(phi_t) + 2j*m2i*EPS @ site_field(phi_t**2)
check("E1.5 in a rate field: tau eps (phi H phi + m w eps) eps tau^-1 = -(phi' H phi' + m w' eps), phi' = tau phi (exact, integer phi)",
      eqz(TAUc @ EPS @ Hw @ EPS @ TAUc.T, -Hw_t))
# no on-site map can anticommute when m != 0: an on-site X commutes with eps; X H X^-1 moves one step, eps none
check("E1.6 every on-site operator commutes with eps (block-diagonal in the site basis), and H has no on-site part",
      all(np.allclose(H2[2*i:2*i+2, 2*i:2*i+2], 0) for i in range(N)))

# ------------------------------------------------------------------ E2 the twin's energy density
ok_e = True
for trial in range(5):
    psi = rng.integers(-3, 4, 2*N) + 1j*rng.integers(-3, 4, 2*N)
    chi = TAUc @ EPS @ psi
    Hpsi = Hp @ psi; Hchi = Hp @ chi
    e_psi = np.array([np.real(np.vdot(psi[2*i:2*i+2], Hpsi[2*i:2*i+2]/(2j))) for i in range(N)])
    e_chi = np.array([np.real(np.vdot(chi[2*i:2*i+2], Hchi[2*i:2*i+2]/(2j))) for i in range(N)])
    for x in SITES:
        ok_e &= abs(e_chi[idx((x[0] + 1, x[1], x[2]))] + e_psi[idx(x)]) < 1e-9
check("E2 twin's energy density e_{z+e1}[tau eps psi] = -e_z[psi] at every site (5 random Gaussian-integer states)", ok_e)

# ------------------------------------------------------------------ E3 the chessboard of clocks with a mass
a, m = sp.symbols('a m', real=True)
cb_ok = sp.simplify((m*sp.exp(a)*1 - (m*sp.cosh(a)*1 + m*sp.sinh(a))).rewrite(sp.exp)) == 0 and sp.simplify((m*sp.exp(-a)*(-1) - (m*sp.cosh(a)*(-1) + m*sp.sinh(a))).rewrite(sp.exp)) == 0
phi_cb = np.where(eps_site == 1, 2.0, 0.5)                           # phi = 2^eps: every bond product is 1
check("E3.1 chessboard phi = c^eps: phi H phi = H exactly (c = 2), and m w eps = m (cosh a eps + sinh a) with w = e^(a eps)",
      eqz(walk(phi_cb), H2) and cb_ok)
mc, ms = 17/8*3, 15/8*3                                               # c = 2: w = 4 on even, 1/4 on odd; m = 3
Hc = H2 + 2j*mc*EPS
lhs = (Hc/(2j))@(Hc/(2j)); rhs = (H2/(2j))@(H2/(2j)) + mc**2*np.eye(2*N)
check("E3.2 (H + m cosh a eps)^2 = H^2 + m^2 cosh^2 a, so the spectrum is m sinh a +- sqrt(E^2 + m^2 cosh^2 a) (c = 2, m = 3)",
      np.allclose(lhs, rhs))
x = sp.symbols('x', positive=True)
Es = sp.symbols('E', real=True)
E_sea = m*sp.sinh(a) - sp.sqrt(Es**2 + m**2*sp.cosh(a)**2)           # per negative state
check("E3.3 the chessboard mode is not stationary: d/da E_sea at a = 0 is +m per negative state (N m in total)",
      sp.simplify(sp.diff(E_sea, a).subs(a, 0) - m) == 0)

# ------------------------------------------------------------------ E4 the large-mass stiffness
ux, uy, mm = sp.symbols('u_x u_y m', positive=True)
wx, wy = sp.exp(ux), sp.exp(uy)
f = -(wx*wy/2)/(mm*(wx + wy))                                        # second-order energy of one bond (coin trace 1/2)
ser = sp.series(sp.series(f, ux, 0, 3).removeO(), uy, 0, 3).removeO()
quad = sp.expand(sum(t for t in sp.Add.make_args(sp.expand(ser)) if sp.Poly(t, ux, uy).total_degree() == 2))
d = sp.symbols('d')
# write the quadratic part as A (u_x^2 + u_y^2) + B (u_x - u_y)^2 and read B
Acoef, Bcoef = sp.symbols('A B')
sol = sp.solve(sp.Poly(sp.expand(quad - (Acoef*(ux**2 + uy**2) + Bcoef*(ux - uy)**2)), ux, uy).coeffs(), [Acoef, Bcoef])
check("E4.1 hop trace: tr(sigma_a/(2i) (sigma_a/(2i))^dagger) = 1/2", sp.simplify(sp.trace(sp.Matrix([[0, 1], [1, 0]])**2)/4) == sp.Rational(1, 2))
check("E4.2 second-order sea energy per bond: gradient term +(1/(16m))(u_x - u_y)^2, i.e. kappa = 1/(8m) + O(m^-3)",
      sp.simplify(sol[Bcoef] - 1/(16*mm)) == 0, f"B = {sol[Bcoef]}, A = {sol[Acoef]}")

# ------------------------------------------------------------------ N  kappa(m), floating point, labelled
def sea_energy(Lx, mv, u):
    ph = np.exp(u/2); w = ph**2
    Sx = np.zeros((Lx, Lx), complex)
    for xx in range(Lx):
        Sx[xx, (xx + 1) % Lx] += ph[xx]*ph[(xx + 1) % Lx]/(2j); Sx[(xx + 1) % Lx, xx] += -ph[xx]*ph[(xx + 1) % Lx]/(2j)
    Hx = np.kron(Sx, sx); W = np.diag(w); stag = np.diag([(-1)**xx for xx in range(Lx)])
    Mm = np.kron(mv*W@stag, I2); E = 0.0; ks = 2*np.pi*np.arange(Lx)/Lx; seen = set()
    for iy in range(Lx):
        for iz in range(Lx):
            key = (iy, iz); partner = ((iy + Lx//2) % Lx, (iz + Lx//2) % Lx)
            if key in seen or partner in seen: continue
            seen.add(key); seen.add(partner)
            T = np.kron(W, np.sin(ks[iy])*sy + np.sin(ks[iz])*sz)
            ev = np.linalg.eigvalsh(np.block([[Hx + T, Mm], [Mm, Hx - T]])); E += ev[ev < 0].sum()
    return E
def kappa(Lx, mv, n=1, e=0.04):
    xx = np.arange(Lx); c = np.cos(2*np.pi*n*xx/Lx); E0 = sea_energy(Lx, mv, 0*c)
    d1 = (sea_energy(Lx, mv, e*c) + sea_energy(Lx, mv, -e*c) - 2*E0)/(2*Lx**3*e**2)
    d2 = (sea_energy(Lx, mv, 2*e*c) + sea_energy(Lx, mv, -2*e*c) - 2*E0)/(2*Lx**3*(2*e)**2)
    Pq = (4*d1 - d2)/3; q2 = 2*(1 - np.cos(2*np.pi*n/Lx))
    return (Pq - E0/Lx**3/4)/(q2/4), E0/Lx**3
MS = [0, 0.25, 0.5, 1, 1.5, 2, 3, 4, 6, 8]
rows = {}
for Lx in (8, 16, 24):
    rows[Lx] = [kappa(Lx, mv) for mv in MS]
print("   NUMERICAL kappa(m) (mode n = 1 along e1; c0 = E_sea/N):")
for Lx in rows:
    print("   L=%2d " % Lx + " ".join("m=%-4g k=%.5f" % (mv, r[0]) for mv, r in zip(MS, rows[Lx])))
k24 = [r[0] for r in rows[24]]
check("N1 NUMERICAL: kappa(m) > 0 at every m in {0,...,8} and L in {8,16,24}: no sign change",
      all(r[0] > 0 for L_ in rows for r in rows[L_]))
check("N2 NUMERICAL: at L = 24 kappa decreases with m from m = 0.25 on, and kappa * 8m -> 1 (0.987 at m = 8)",
      all(k24[i] > k24[i + 1] for i in range(1, len(MS) - 1)) and abs(k24[-1]*8*8 - 0.987) < 0.005)
check("N3 NUMERICAL: block 77 W3 reproduced at L = 8 (kappa = 0.088/0.090/0.076 at m = 0, 1/2, 1)",
      [round(r[0], 3) for r in rows[8][:3:2]] == [0.088, 0.090] and round(rows[8][3][0], 3) == 0.076)

print()
if FAILS:
    print("SUMMARY: ROUTE FAILS AT " + FAILS[0]); sys.exit(1)
print("SUMMARY: PARTIAL exact: with the staggered mass the even species maps survive, the odd ones survive as eps V_n, and "
      "no on-site map makes twins; tau eps (one-site translation after the site sign) anticommutes with the massive walk and "
      "carries a solution in rate field w to a twin in the translated field with energy density -e_{z-e1}; the chessboard of "
      "clocks is NOT invisible with a mass (m w eps = m cosh a eps + m sinh a; E_sea(a) = N m sinh a - sum sqrt(E^2 + m^2 cosh^2 a), "
      "first variation N m); kappa(m) = 1/(8m) + O(m^-3) exactly at large m and (floating) positive on 0..8: no sign change")
