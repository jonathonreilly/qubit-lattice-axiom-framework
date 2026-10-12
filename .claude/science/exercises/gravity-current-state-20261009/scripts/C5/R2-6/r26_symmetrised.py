"""R2-6 (d) side check: the symmetrised (commutative) variant k(+)_s q = (k(+)q + q(+)k)/2.
Not Snyder's star-product coproduct; tested only as a scope boundary for Lemma W-S.
 S1 is A/B (on-shell k(+)_s q = A k + B q) independent of k.q exactly (large a)?
 S2 is (+)_s associative?  If not, a 4-vector additive Ward charge Q(k)=kt(m)k cannot exist
    on 2->3 / 3->3 channels (Q would have to be a homomorphism).
 S3 does Q(k (+)_s q) = Q(k)+Q(q) hold for some kt(m)?  test kt(m) = c(m) fitted from A/B.
"""
import numpy as np
import importlib.util, sys
spec = importlib.util.spec_from_file_location("rc", "r26_composition_lib.py")
rc = importlib.util.module_from_spec(spec); spec.loader.exec_module(rc)
oplus, onshell, dot4 = rc.oplus, rc.onshell, rc.dot4


def sym(k, q, a):
    return 0.5 * (oplus(k, q, a) + oplus(q, k, a))


def AB(v, k, q):
    Mx = np.vstack([k, q]).T
    c, *_ = np.linalg.lstsq(Mx, v, rcond=None)
    return c


print("S1: A/B for (+)_s, m_k=1, m_q=0.6, at several a and k.q")
for a in [0.05, 0.3, 0.8]:
    rs = []
    for sp_ in [0.1, 0.6, 1.2, 2.0]:
        k = onshell(1.0, np.array([sp_, 0.0, 0.0]))
        q = onshell(0.6, np.array([-0.3, 0.4, 0.1]))
        c = AB(sym(k, q, a), k, q)
        rs.append(c[0] / c[1])
    print(f"  a={a}: A/B = {np.round(rs, 12)}  spread {max(rs)-min(rs):.2e}")
print("S2: associativity of (+)_s and of (+) (three on-shell momenta, masses 1, 0.6, 0.8)")
k = onshell(1.0, np.array([0.5, 0.1, 0.0]))
q = onshell(0.6, np.array([-0.3, 0.4, 0.1]))
r = onshell(0.8, np.array([0.1, -0.2, 0.6]))
for a in [0.2, 0.1, 0.05, 0.025]:
    d_s = np.linalg.norm(sym(sym(k, q, a), r, a) - sym(k, sym(q, r, a), a))
    d_o = np.linalg.norm(oplus(oplus(k, q, a), r, a) - oplus(k, oplus(q, r, a), a))
    print(f"  a={a:6.3f}: |(k+q)+r - k+(q+r)| sym = {d_s:.4e} (/a^2 = {d_s/a**2:.5f}); ordering law = {d_o:.4e} (/a^2 = {d_o/a**2:.5f})")
print("S3: is (+)_s a 2-body homomorphism to + in coordinates Q(k)=kt(m)k ?  (needed for n>=3 channels)")
print("    compute X(k)=sinh(am)/(am) k and N(k)=k/cosh-type candidates; report |Q(k(+)_s q) - Q(k) - Q(q)|")
for a in [0.2, 0.1, 0.05]:
    v = sym(k, q, a)
    mv = np.sqrt(-dot4(v, v))
    best = []
    for name, f in [("normal k", lambda m: 1.0), ("ambient sinh(am)/(am)", lambda m: np.sinh(a*m)/(a*m)),
                    ("projective tanh(am)/(am)", lambda m: np.tanh(a*m)/(a*m))]:
        Q = lambda kk, mm: f(mm) * kk
        res = np.linalg.norm(Q(v, mv) - Q(k, 1.0) - Q(q, 0.6))
        best.append(f"{name}: {res:.3e} (/a^2 {res/a**2:.4f})")
    print(f"  a={a}: " + "; ".join(best))
