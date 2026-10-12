"""R7-4 part 1: two free scalar species with different dispersions (c_s, m_s) on Z^3.
Checks, per species, the exact lattice identities the linear N-type lapse/shift coupling needs:
 (E)  dT00/dt = -div J_E  with J_E = c^2 P   (energy current = c^2 x pseudo-momentum)
 (M)  dP_j/dt = sum_i D_i T_ij with T SYMMETRIC (one value per ij face), 09-14 G-stencil placement
Then evaluates the linear-order observables with per-species couplings a_s:
 rest redshift, slow free-fall acceleration, light deflection -> gamma_s, and the EP/LPI conditions.
Conventions follow RN L1 (agents/RN_L1_report.md): P_j(x)=1/2(pi_x+pi_{x+e_j}) d_j phi(x).
"""
import numpy as np
rng = np.random.default_rng(7)
L = 6
def sh(f, j, s):  # f(x + s e_j)
    return np.roll(f, -s, axis=j)
def d(f, j):      # forward difference d_j f(x) = f(x+e_j)-f(x)
    return sh(f, j, 1) - f

def fields_and_rates(c, m):
    phi = rng.normal(size=(L, L, L)) * 3.0
    pi = rng.normal(size=(L, L, L)) * 3.0
    # H = sum 1/2 pi^2 + 1/2 m^2 phi^2 + 1/2 c^2 sum_j (d_j phi)^2
    lap = sum(sh(phi, j, 1) + sh(phi, j, -1) - 2 * phi for j in range(3))
    phidot = pi
    pidot = -m**2 * phi + c**2 * lap
    return phi, pi, phidot, pidot

def T00(phi, pi, c, m):
    g = sum(d(phi, j)**2 + sh(d(phi, j), j, -1)**2 for j in range(3))
    return 0.5 * pi**2 + 0.5 * m**2 * phi**2 + 0.25 * c**2 * g

def P(phi, pi, j):
    return 0.5 * (pi + sh(pi, j, 1)) * d(phi, j)

def Tstress(phi, pi, c, m):
    T = {}
    for j in range(3):
        others = [i for i in range(3) if i != j]
        T[(j, j)] = (0.5 * pi**2 - 0.5 * m**2 * phi**2
                     + 0.5 * c**2 * d(phi, j) * sh(d(phi, j), j, -1)
                     - 0.25 * c**2 * sum(d(phi, i)**2 + sh(d(phi, i), i, -1)**2 for i in others))
    for i in range(3):
        for j in range(i + 1, 3):
            T[(i, j)] = 0.25 * c**2 * (d(phi, i) + sh(d(phi, i), j, 1)) * (d(phi, j) + sh(d(phi, j), i, 1))
            T[(j, i)] = T[(i, j)]
    return T

def ddt(fun, phi, pi, phidot, pidot, eps=1e-6):
    # exact for quadratic forms via polarization: d/dt Q(phi,pi) = Q(phi+eps phidot, pi+eps pidot) - Q(phi-...) / 2eps
    return (fun(phi + eps * phidot, pi + eps * pidot) - fun(phi - eps * phidot, pi - eps * pidot)) / (2 * eps)

out = []
for (c, m) in [(1.0, 0.3), (1.3, 1.1), (0.7, 0.0)]:
    phi, pi, phidot, pidot = fields_and_rates(c, m)
    # (E): dT00/dt + div J_E = 0 with backward divergence of edge current c^2 P_j(x) on edge (x,x+e_j)
    dT = ddt(lambda a, b: T00(a, b, c, m), phi, pi, phidot, pidot)
    divJ = sum(c**2 * (P(phi, pi, j) - sh(P(phi, pi, j), j, -1)) for j in range(3))
    resE = np.max(np.abs(dT - divJ)) / np.max(np.abs(dT))
    # alternative: J_E = P (no c^2) fails unless c=1
    resE_wrong = np.max(np.abs(dT - sum((P(phi, pi, j) - sh(P(phi, pi, j), j, -1)) for j in range(3)))) / np.max(np.abs(dT))
    # (M): dP_j/dt = (G[T])_j with the 09-14 G stencil: T_jj(x+e_j)-T_jj(x) + sum_{i!=j}[T_ij(x)-T_ij(x-e_i)]
    T = Tstress(phi, pi, c, m)
    resM = 0.0
    for j in range(3):
        dP = ddt(lambda a, b: P(a, b, j), phi, pi, phidot, pidot)
        GT = sh(T[(j, j)], j, 1) - T[(j, j)] + sum(T[(i, j)] - sh(T[(i, j)], i, -1) for i in range(3) if i != j)
        resM = max(resM, np.max(np.abs(dP - GT)) / np.max(np.abs(dP)))
    out.append(f"species c={c} m={m}: rel. residual (E) J_E=c^2 P: {resE:.2e} ; (E) with J_E=P: {resE_wrong:.2e} ; (M) symmetric T: {resM:.2e}")

# ---------------- linear-order observables (analytic formulas, evaluated) -----------------
# Coupling: H = H_N + sum_s H_s + n (S/kappa + sum_s a_s T00^s) + N_j(-(J/kappa) G_j + sum_s a_s c_s^2 P^s_j) + sum_s c'_s h_ij T^s_ij
# Shift-constraint preservation per separately conserved species: c'_s = -kappa a_s c_s^2 / J.
# Static field of a dust source (RN L1 convention, h_ij = 2 psi delta_ij): psi = kappa a_S T00/(4 qhat^2), n = -2 g kappa psi.
# One quantum of species s with momentum k: <sum T_ij> = f_i v_j, f = sin k, v = c_s^2 sin k / omega_s.
# delta omega_s = a_s n omega_s + 2 c'_s psi f.v  =>  delta omega_s / omega_s = a_s n [1 + (c_s^2/(J g)) f.v/omega_s]
def response(cs, ms, a_s, Jg, k):
    k = np.asarray(k, float)
    w2 = ms**2 + cs**2 * np.sum(4 * np.sin(k / 2)**2)
    w = np.sqrt(w2)
    f = np.sin(k); v = cs**2 * np.sin(k) / w
    return a_s * (1 + (cs**2 / Jg) * np.dot(f, v) / w)   # delta omega/omega in units of n
out.append("")
out.append("Linear observables (units: n = lapse perturbation of the source's field):")
for Jg in [1.0, 1.21]:
    for (cs, ms, a_s) in [(1.0, 0.3, 1.0), (1.3, 1.1, 1.0), (1.0, 1.1, 1.0), (1.0, 1.1, 0.8)]:
        kray = [1e-3, 0, 0]
        ray = response(cs, 0.0, a_s, Jg, kray)        # massless ray of this species' band
        rest = response(cs, ms, a_s, Jg, [0, 0, 0])
        accel = a_s * cs**2                              # slow free fall: x'' = -a_s c_s^2 grad n
        # gamma_s: (ray deflection)/(Newtonian deflection at v=c_s) = (1+gamma_s)/... ; Newtonian deflection at v=c_s ~ a_s grad n
        gamma = ray / a_s - 1
        out.append(f" c_g^2=Jg={Jg}: species (c={cs}, m={ms}, a={a_s}): rest redshift dω/ω = {rest:.6f} n ; free-fall accel = {accel:.4f} (-grad n) ; ray dω/ω = {ray:.6f} n ; gamma_s = {gamma:.6f} (c_s^2/c_g^2 = {cs**2/Jg:.6f})")
out.append("")
out.append("EP (free-fall) needs a_A c_A^2 = a_B c_B^2 ; LPI (redshift) needs a_A = a_B ; gamma = 1 needs c_s = c_g.")
eta = (1.3**2 - 1.0**2) / 1.0
out.append(f"Example Eotvos parameter for c_A=1, c_B=1.3, a_A=a_B: eta = {eta:.3f}")
# anisotropy of the ray response at finite k (lattice correction), same c
for kdir in [[1, 0, 0], [1, 1, 0], [1, 1, 1]]:
    kk = 0.05 * np.array(kdir) / np.linalg.norm(kdir)
    out.append(f" ray response at |k|=0.05 dir {kdir}: gamma_eff-1 = {response(1.0, 0.0, 1.0, 1.0, kk) - 2:.3e}")
print("\n".join(out))
