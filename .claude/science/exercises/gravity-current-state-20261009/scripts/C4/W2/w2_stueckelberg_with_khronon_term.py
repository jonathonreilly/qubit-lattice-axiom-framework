"""W2 part 2b: add the gauge-invariant BPS 'acceleration' term  alpha*Mp2*(grad(Phi + pi_dot))^2
(the healthy-extension term of Hora\v{c}ava-Blas-Pujolas-Sibiryakov; invariant since d Phi = eps_dot,
d pi = -eps) to GR + the anomaly's Wess-Zumino term from w2_stueckelberg_scalar.py, and redo the
spectrum and Krein signature.  Question: can a natural-size induced acceleration term cure the
ghost found with alpha = 0?"""
import sympy as sp, numpy as np
w, k = sp.symbols('omega k', positive=True)
a, M, al = sp.symbols('a M_p2 alpha', real=True)
# Fourier quadratic form (fields Phi, Psi, pi, zeta), gauge B = E = 0, copied from the .out of part 2
Mq = sp.Matrix([[0, -M*k**2/2, 0, -a*k**2/4],
                [-M*k**2/2, M*(k**2 - 3*w**2)/2, 0, 0],
                [0, 0, -a*k**2/4, -sp.I*a*k**2*w/4],
                [-a*k**2/4, 0, sp.I*a*k**2*w/4, 0]])
# acceleration term alpha*M*(d_x(Phi + pi_dot))^2 -> v^dag A v with u = Phi_h + (-i w) pi_h:
# period average of (Re(i k u e))^2 = k^2 |u|^2 / 2 ;  v^dag M v convention = (1/4)*(...)*2 -> k^2/2 |u|^2 * (1/2)?
# use the same convention as part 2: term c*D1 f_a * D2 f_b contributes M[ib,ia] += c s1 conj(s2)/4 and transpose
s_Phi = sp.I*k; s_pi = sp.I*k*(-sp.I*w)
facs = {0: s_Phi, 2: s_pi}
A = sp.zeros(4, 4)
for ia, s1 in facs.items():
    for ib, s2 in facs.items():
        A[ib, ia] += al*M*s1*sp.conjugate(s2)/4
        A[ia, ib] += al*M*sp.conjugate(s1)*s2/4
Mt = sp.simplify(Mq + A)
det = sp.factor(sp.simplify(Mt.det()))
print("det =", det)
W2 = sp.symbols('W2')
roots = sp.solve(sp.Eq(sp.simplify(det.subs(w, sp.sqrt(W2))), 0), W2)
print("omega^2 roots:", [sp.simplify(r) for r in roots])
P1, P2, P3, P4 = Mt[:2, :2], Mt[:2, 2:], Mt[2:, :2], Mt[2:, 2:]
S = sp.simplify(P4 - P3*P1.inv()*P2)
Sf = sp.lambdify((w, k, a, M, al), S, 'numpy'); dSf = sp.lambdify((w, k, a, M, al), sp.diff(S, w), 'numpy')
for alv in (0.0, 1e-3, 0.1, 1.0):
    for av in (+1e-2, -1e-2):
        line = []
        for kv in (0.05, 0.3, 1.0, 5.0):
            rts = [complex(r.subs({k: kv, a: av, M: 1.0, al: alv})) for r in roots]
            for r in rts:
                if abs(r.imag) > 1e-12 or r.real <= 0:
                    line.append(f"k={kv}: w2={r.real:+.3e} TACHYON"); continue
                wv = np.sqrt(r.real)
                Sv = np.array(Sf(wv, kv, av, 1.0, alv), dtype=complex)
                ev, evec = np.linalg.eigh(Sv); v = evec[:, np.argmin(abs(ev))]
                E = wv*np.real(v.conj() @ np.array(dSf(wv, kv, av, 1.0, alv), dtype=complex) @ v)
                line.append(f"k={kv}: w2={r.real:+.3e} {'healthy' if E > 0 else 'GHOST'}")
        print(f"alpha={alv:g} a={av:+g}: " + " | ".join(line))
