"""Small exact independent controls; no author assembly is imported.

The general theorem is the analytic argument in REPORT.md, not finite samples.
Run with OMP_NUM_THREADS=OPENBLAS_NUM_THREADS=MKL_NUM_THREADS=1.
"""
import json
import resource
import time
from pathlib import Path

t0 = time.perf_counter()
import sympy as s

I = s.I
eye = s.eye(2)
sigma = [s.Matrix([[0, 1], [1, 0]]),
         s.Matrix([[0, -I], [I, 0]]), s.diag(1, -1)]


def hermitian(prefix):
    a, b, c, d = s.symbols(prefix + '0:4', real=True)
    return s.Matrix([[a, c + I*d], [c - I*d, b]])


def real_hessian(M):
    C, D = M.applyfunc(s.re), M.applyfunc(s.im)
    return C.row_join(-D).col_join(D.row_join(C))


def zero(M):
    return all(s.expand(x) == 0 for x in M)


# psi=(q+i p)/sqrt(2), with q,p real. An arbitrary Hermitian Z
# corresponds to {q,q}={p,p}=Im Z and {q,p}=Re Z.
A, B, Z = [hermitian(p) for p in ['a', 'b', 'z']]
ZR, ZI = Z.applyfunc(s.re), Z.applyfunc(s.im)
Jreal = ZI.row_join(ZR).col_join((-ZR).row_join(ZI))
HA, HB = real_hessian(A), real_hessian(B)
target = -I * (A*Z*B - B*Z*A)
assert zero(HA*Jreal*HB - HB*Jreal*HA - real_hessian(target))
assert zero(Jreal + Jreal.T)
# A deliberately misplaced Z is genuinely different, not a harmless convention.
bad_ordering_detected = not zero(target + I*Z*(A*B-B*A))
assert bad_ordering_detected


def conv(A, B):
    ans = {}
    for a, m in A.items():
        for b, n in B.items():
            ans[a+b] = ans.get(a+b, s.zeros(2)) + m*n
    return clean(ans)


def clean(A):
    return {a: m.applyfunc(s.expand) for a, m in A.items() if not zero(m)}


def plus(*terms):
    out = {}
    for scale, A in terms:
        for a, m in A.items():
            out[a] = out.get(a, s.zeros(2)) + scale*m
    return clean(out)


def derivative(A):
    return clean({a: I*a*m for a, m in A.items()})


def affine_bracket_row(F, H, row):
    """Literal i(F E_x-E_x F), where E_x(a,b)=(a+b)H_(b-a)/2."""
    out = {}
    for a, f in F.items():
        mid = row + a
        for b, h in H.items():
            col = mid + b
            out[col-row] = out.get(col-row, s.zeros(2)) + I*f*h*s.Rational(mid+col, 2)
    for a, h in H.items():
        mid = row + a
        for b, f in F.items():
            col = mid + b
            out[col-row] = out.get(col-row, s.zeros(2)) - I*h*f*s.Rational(row+mid, 2)
    return clean(out)


def equal(A, B):
    return not plus((1, A), (-1, B))


# A legitimate transverse-gapped symbol slice of the source:
# sin(k_2)=3/5, sin(k_3)=4/5. No finite-volume affine coordinate is used.
H = {-1: I*sigma[0]/2, 0: s.Rational(3, 5)*sigma[1]+s.Rational(4, 5)*sigma[2],
     1: -I*sigma[0]/2}
P = {-2: I*eye/4, 2: -I*eye/4}
a = {-1: eye/2, 0: 2*eye, 1: eye/2}
b = {-2: eye/3, 0: -eye, 2: eye/3}
Zcomm = plus((1, a), (1, conv(b, H)))
F = conv(P, Zcomm)
assert equal(conv(F, H), conv(H, F))
rhs = plus((s.Rational(1, 2), conv(derivative(F), H)),
           (s.Rational(1, 2), conv(H, derivative(F))))
for row in [-7, 0, 11]:
    assert equal(affine_bracket_row(F, H, row), rhs)
assert s.trace(derivative(F).get(0, s.zeros(2))) == 0

# For a noncommuting Z the general affine row retains its expected x term.
Zn = {0: eye, 1: sigma[1]/2, -1: sigma[1]/2}
Fn = conv(P, Zn)
uniform = plus((I, conv(Fn, H)), (-I, conv(H, Fn)))
assert uniform
q0 = affine_bracket_row(Fn, H, 0)
for row in [-7, 11]:
    assert equal(affine_bracket_row(Fn, H, row), plus((1, q0), (row, uniform)))

# Fully symbolic trace step: invertible H, no positivity of Z required.
h1, h2, h3, u1, v1, w1, z1 = s.symbols('h1 h2 h3 u1 v1 w1 z1', real=True)
Hs = h1*sigma[0] + h2*sigma[1] + h3*sigma[2]
Q = s.Matrix([[u1, w1+I*z1], [w1-I*z1, v1]])
omega2 = h1*h1+h2*h2+h3*h3
assert zero(Hs*Hs-omega2*eye)
trace_check = s.trace(((Q*Hs+Hs*Q)/2)*Hs) - omega2*s.trace(Q)
assert s.expand(trace_check) == 0

# U(1) monomial counting through degree three, independent of spatial support.
# A charge-q coefficient with a psi and b psi* factors has a-b=q.
min_degree = {}
for charge in [0, 1, 2]:
    degrees = [a+b for a in range(4) for b in range(4) if a+b <= 3 and a-b == charge]
    min_degree[str(charge)] = min(degrees)
assert min_degree == {'0': 0, '1': 1, '2': 2}
neutral_nonconstant = min(a+b for a in range(4) for b in range(4)
                          if a+b and a+b <= 3 and a-b == 0)
assert neutral_nonconstant == 2

result = {
    'generic_real_Poisson_Hermitian_quadratic_identity': True,
    'incorrect_Z_ordering_detected': bad_ordering_detected,
    'commuting_matrix_symbol_affine_rows': [-7, 0, 11],
    'commuting_F_radius': max(abs(a) for a in F),
    'affine_result_radius': max(abs(a) for a in rhs),
    'noncommuting_uniform_x_term_retained': True,
    'generic_inverse_H_trace_identity': True,
    'charge_min_degrees': min_degree,
    'neutral_nonconstant_min_degree': neutral_nonconstant,
    'author_code_imported': False,
    'elapsed_seconds': time.perf_counter()-t0,
    'maxrss_bytes': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
}
out = Path(__file__).parent
(out/'results.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
