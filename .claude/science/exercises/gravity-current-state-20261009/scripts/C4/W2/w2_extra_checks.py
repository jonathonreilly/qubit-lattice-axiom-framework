"""W2 extra checks (rerun of the inline checks in the session):
(1) exact vacuum identity e_c + p_c = 1/2 <d/dq_c (sin q_c w)>_zone = 0, and its thermal deviation;
(2) null vector of the scalar-sector form at the extra-mode root: u = Phi + pi_dot vanishes there
    (why the BPS acceleration term alpha*(grad u)^2 cannot change the mode), Psi = -(a/2Mp2) zeta
    (the conformal mode is excited: Boulware-Deser-type mechanism);
(3) the vacuum-branch scale |mu| = sqrt(4 pi G |a_vac|) for ell = ell_P."""
import numpy as np, sympy as sp
q = 2*np.pi*(np.arange(96)+0.5)/96 - np.pi
qx, qy, qz = np.meshgrid(q, q, q, indexing='ij')
w = np.sqrt(0.25 + 2*(3 - np.cos(qx) - np.cos(qy) - np.cos(qz)))
print("(1) vacuum: <(cos q_c w + sin^2 q_c / w)/2> =", np.mean(0.5*(np.cos(qx)*w + np.sin(qx)**2/w)), "(exact 0: total q-derivative)")
for T in (0.1, 1.0):
    n = 1/np.expm1(w/T); dn = -n*(n+1)/T
    print(f"    thermal T={T}: e_c + p_c (normal-ordered) = {np.mean(n*(np.cos(qx)*w + np.sin(qx)**2/w)):+.4e}  = -<sin^2 q_c n'(w)> = {np.mean(-np.sin(qx)**2*dn):+.4e}")
w_, k_ = sp.symbols('omega k', positive=True); a, M = sp.symbols('a M', real=True)
Mq = sp.Matrix([[0, -M*k_**2/2, 0, -a*k_**2/4],[-M*k_**2/2, M*(k_**2 - 3*w_**2)/2, 0, 0],[0, 0, -a*k_**2/4, -sp.I*a*k_**2*w_/4],[-a*k_**2/4, 0, sp.I*a*k_**2*w_/4, 0]])
root = a*k_**2/(3*a - 2*M*k_**2)
v = sp.simplify(Mq.subs(w_, sp.sqrt(root)).nullspace()[0])
print("(2) null vector (Phi, Psi, pi, zeta) at the root:", list(v))
print("    u = Phi + pi_dot  ->  Phi_h - i w pi_h =", sp.simplify(v[0] - sp.I*sp.sqrt(root)*v[2]))
for name, aval in [("m=0", -1.303802), ("m=1", -1.399127)]:
    mu2 = 4*np.pi*abs(aval)
    print(f"(3) vacuum branch {name}: a_vac = -(rho+p) = {aval}; |mu| = {np.sqrt(mu2):.3f}/ell; gapless-ghost window k < sqrt(3)|mu| = {np.sqrt(3*mu2):.2f}/ell > pi (whole zone)")
