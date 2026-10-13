"""R18-6: "does N's gravitational-energy source contain a vacuum part that (S) must also subtract?"  Both arenas.

C1  C-box: one-point vacuum stress of ANY cubic-symmetric lattice sector (the supplied graviton included) is
    rho n n + p h (O_h leaves only delta_ij invariant).  Numerical check on cubic and (control) tetragonal dispersions.
C2  C-box: per harmonic mode in its ground state <kinetic> = <potential>, so an Isaacson-type t^00 ~ <hdot^2> equals the
    Hamiltonian zero-point density (virial).  So e0 (if H contains the graviton sector) removes exactly the energy part of
    <t_LL>_0, and (d-i) receives its enthalpy part W_g, whatever its value.
A1  Set A: a boost- and rotation-invariant symmetric tensor is proportional to eta  ->  W_vac = 0 for the matter vacuum.
A2  Set A: O(G) gravitational field energy sourced by matter vacuum fluctuations through the frame-tied record gain:
    ~ (l_P/l)^2 hbar c / l^4 (order of magnitude; suggested).
A3  Set A: record-noise constraint-channel energy |u1| = hbar I_F/(32 pi^(3/2) l^3 tau), I_F = 21/32 (vR15-2:17),
    strict tau = l/c and drag-ceiling tau_c = 1.49e-3 m / c; in units of rho_Lambda (RECALLED 5.3e-10 J/m^3).
A4  Set A: a scalar subtraction C g cannot remove a stress with p != -rho or with time dependence (elementary).
A5  Set A: static smearing defect of the O(G^2) source outside a body: F s - s ~ (l^2/2) lap s, s ~ r^-4 -> 6 l^2/r^2.
A6  Set A: under N, a non-diluting noise energy in an expanding background needs an injection 3H(rho_n+p_n) in tau.
"""
import numpy as np
import sympy as sp

print("=== C1: one-point stress isotropy on the cubic lattice ===")
L = 48
k = 2*np.pi*(np.arange(L) + 0.5)/L - np.pi
KX, KY, KZ = np.meshgrid(k, k, k, indexing='ij')
def tensor(om2_fn, m2=0.01, h=1e-5):
    om = np.sqrt(om2_fn(KX, KY, KZ) + m2)
    # group-velocity "kinetic stress" density <v_i k_j / ... > stand-in: S_ij = < d_i om d_j om / om >
    d = []
    for i in range(3):
        sh = [KX, KY, KZ]
        shp = [s.copy() for s in sh]; shm = [s.copy() for s in sh]
        shp[i] = shp[i] + h; shm[i] = shm[i] - h
        d.append((np.sqrt(om2_fn(*shp) + m2) - np.sqrt(om2_fn(*shm) + m2))/(2*h))
    S = np.array([[np.mean(d[i]*d[j]/om) for j in range(3)] for i in range(3)])
    return S
cubic_nn = lambda x, y, z: 4*(np.sin(x/2)**2 + np.sin(y/2)**2 + np.sin(z/2)**2)
cubic_zz = lambda x, y, z: (np.sin(x)**2 + np.sin(y)**2 + np.sin(z)**2) + 0.3*(np.sin(x)**2*np.sin(y)**2 + np.sin(y)**2*np.sin(z)**2 + np.sin(z)**2*np.sin(x)**2)
tetrag = lambda x, y, z: 4*(np.sin(x/2)**2 + np.sin(y/2)**2 + 1.7*np.sin(z/2)**2)
for name, fn in (("cubic NN", cubic_nn), ("cubic + quartic cross terms", cubic_zz), ("CONTROL tetragonal (c-axis x1.7)", tetrag)):
    S = tensor(fn)
    iso = np.trace(S)/3
    aniso = np.max(np.abs(S - iso*np.eye(3)))/abs(iso)
    print(f"C1 {name:34s} diag = {np.diag(S).round(6)}  max|S - (trS/3) 1|/|trS/3| = {aniso:.2e}")
print("C1 => any cubic-covariant sector's one-point stress is (rho, p) in the site frame: split -V g + W h exists; (S) takes V's")
print("     ground-state part (if the sector is in H), (d-i) takes W.  [proved by O_h: Sym^2(T1u) = A1g + Eg + T2g; checked]")

print("\n=== C2: virial per mode (ground state of a harmonic mode, frequency w) ===")
w, hb = sp.symbols('omega hbar', positive=True)
# ground state of H = p^2/2 + w^2 q^2/2: <p^2> = hb w/2, <q^2> = hb/(2w)
kin = sp.Rational(1, 2)*hb*w/2; pot = sp.Rational(1, 2)*w**2*hb/(2*w)
print("C2 <kin> =", kin, " <pot> =", sp.simplify(pot), " equal:", sp.simplify(kin - pot) == 0,
      " -> 2<kin> (Isaacson-type <qdot^2>) = <H> =", sp.simplify(kin + pot))

print("\n=== A1: Lorentz-invariant symmetric tensor ===")
T = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f"T{min(i,j)}{max(i,j)}"))
eta = sp.diag(-1, 1, 1, 1)
gens = []
for i in (1, 2, 3):   # boost generators K_i (acting on vectors)
    K = sp.zeros(4); K[0, i] = 1; K[i, 0] = 1; gens.append(K)
for (i, j) in ((1, 2), (2, 3), (1, 3)):
    J = sp.zeros(4); J[i, j] = -1; J[j, i] = 1; gens.append(J)
# invariance of T^{mu nu}: G T + T G^T = 0 for each generator
eqs = []
for Gm in gens:
    eqs += list(Gm*T + T*Gm.T)
sol = sp.solve(eqs, list(set(T)), dict=True)
Tsol = T.subs(sol[0])
print("A1 invariant T^{mu nu} =", Tsol.tolist())
rho = sp.Symbol('rho')
print("A1 => T^{mu nu} = c eta^{mu nu}: rho = -c... check T + T00*eta == 0:", sp.simplify(Tsol + Tsol[0, 0]*eta) == sp.zeros(4, 4),
      " -> W = rho + p = 0 for a Poincare-invariant vacuum (set A matter).")

print("\n=== A2 / A3: set-A vacuum-sourced and record-noise field energies (units of rho_Lambda) ===")
hbar = 1.0546e-34; c = 2.998e8; lP = 1.616e-35; rhoL = 5.3e-10   # rho_Lambda RECALLED (J/m^3)
IF = 21/32; tc = 1.49e-3/c
for l in (4e-10, 3e-8, 5e-8, 2.5e-7, 1e-6, 5e-6):
    a2 = (lP/l)**2*hbar*c/l**4/rhoL
    u_strict = hbar*IF/(32*np.pi**1.5*l**3*(l/c))/rhoL
    u_tc = hbar*IF/(32*np.pi**1.5*l**3*tc)/rhoL
    print(f"l = {l:7.1e} m:  A2 (l_P/l)^2 hbar c/l^4 = {a2:8.1e}   A3 |u1| strict = {u_strict:8.1e}   |u1| tau_c ceiling = {u_tc:8.1e}")
print("A3 reproduces R15-2's 1.2x at 5e-6 m and ~1e12x at 4e-10 m (tau_c ceiling) [C5_R15-2_report.md:26; vR15-2:17].")

print("\n=== A4: what a scalar subtraction can remove ===")
C_, rn, pn = sp.symbols('C rho_n p_n', real=True)
# residual after subtracting -C g from a site/CMB-frame stress (rho_n, p_n): (rho_n - C, p_n + C)
print("A4 residual (rho_n - C, p_n + C) vanishes iff C = rho_n and p_n = -rho_n:", sp.solve([rn - C_, pn + C_], [C_, pn]))
print("A4 TT noise p = rho/3 -> W_n = 4 rho_n/3 left over; S/V static field stress p = u/3 (R16-14:241, suggested) -> W_n = 4u/3.")
print("   E1 TT noise grows with age (eps ln t, R11-5/R13-6) -> not a constant at all.  (S) cannot subtract either.")

print("\n=== A5: static filter defect on the O(G^2) source outside a body ===")
r_ = sp.symbols('r', positive=True); l_ = sp.symbols('ell', positive=True)
s = r_**-4
lap = sp.diff(r_**2*sp.diff(s, r_), r_)/r_**2
rel = sp.simplify((l_**2/2)*lap/s)
print("A5 (l^2/2) lap(r^-4) / r^-4 =", rel)
for (name, rr) in (("R_sun", 6.96e8), ("Mercury orbit", 5.79e10), ("1 AU", 1.496e11)):
    print(f"A5 l = 5e-6 m at {name}: {float(rel.subs({l_: 5e-6, r_: rr})):.1e}")
print("A5 dynamic part 6(tau_c w/R)^2 = 4.2e-29 on the U^2 term (R16-14 out:104; vR16-14 item 4) - not recomputed.")

print("\n=== A6: under N, a non-diluting noise energy in expansion ===")
H0 = 2.27e-18
print("A6 Bianchi under N needs d(rho_n)/dt + 3H(rho_n + p_n) = (injection in tau).  For constant rho_n, p_n = rho_n/3:")
print(f"   injection = 4 H rho_n;  at rho_n = rho_Lambda: {4*H0*rhoL:.1e} W/m^3 must come from a conserved partner (meters) inside tau.")
