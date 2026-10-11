#!/usr/bin/env python3
"""Finite controls for the projected-band canonical-current construction.

Four complete frozen control programs run in isolated namespaces. Their finite
operator algebra, exact budgets and floating examples support the proof note;
no continuum theorem or long-time relaxation is inferred from a grid. The
only source-file read is integrity metadata, not a scientific calculation.
Requires NumPy, SciPy and SymPy; no author helper is imported at runtime.
"""
from hashlib import sha256
from pathlib import Path
from time import perf_counter

AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = [
    'docs/EXCLUDED_WALK_PROJECTED_FREE_BAND_CANONICAL_CURRENT_BOUNDED_THEOREM_NOTE_2026-10-11.md',
    'docs/EXCLUDED_WALK_LOW_ENERGY_ENERGY_CURRENT_BOUNDED_THEOREM_NOTE_2026-10-11.md',
]
_started = perf_counter()


def _run_block(label, source):
    print('BEGIN', label, 'embedded_source_sha256='+sha256(source.encode()).hexdigest(), flush=True)
    # The original source's __file__ metadata now identifies this combined
    # runner. The four mathematical global namespaces never overlap.
    namespace = {'__name__': '__main__', '__file__': __file__}
    exec(compile(source, __file__+'::'+label, 'exec'), namespace)
    print('END', label, flush=True)

# BEGIN VERBATIM excluded_walk_long_time/long_time_checks.py
_run_block('block_1_long_time_checks', r'''"""Author finite controls of the zero-mode/leakage proof, not continuum numerics.

Inputs are literal exact fields below. Each process has a 90-second harness
timeout. No repository or earlier author runner is imported.
"""
from pathlib import Path
from hashlib import sha256
import json
import numpy as np
import sympy as s

CHECK_TIMEOUT_SECONDS=90
checks=0
def check(value,label):
    global checks
    assert bool(value),label
    checks+=1
def zm(M):return all(s.simplify(x)==0 for x in M)
def norm2(x):return s.simplify((x.H*x)[0])

# Actual singlet/Pauli matrices, before using a scalar radial representation.
pauli=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
singlet=s.Matrix([0,1,-1,0])/s.sqrt(2)
triplet=[s.kronecker_product(p,s.eye(2))*singlet for p in pauli]
coin_basis=s.Matrix.hstack(singlet,*triplet)
check(zm(coin_basis.H*coin_basis-s.eye(4)),'orthonormal actual singlet/triplet basis')
sx=s.symbols('s0:3',real=True)
spinH=sum((sx[j]*(s.kronecker_product(pauli[j],s.eye(2))-s.kronecker_product(s.eye(2),pauli[j])) for j in range(3)),s.zeros(4))
cart=s.zeros(4)
for j in range(3):cart[0,j+1]=cart[j+1,0]=2*sx[j]
check(zm(coin_basis.H*spinH*coin_basis-cart),'exact zero-K longitudinal block')

# Nine antipodal pairs, represented with even singlet/odd triplet parity.
# This rational cubically symmetric measure tests algebra; it is NOT torus
# quadrature or an approximation used to claim the continuum scaling.
radii=[s.Rational(1,8),s.Rational(1,3),s.Rational(2,3)]
nodes=[(r,j) for r in radii for j in range(3)]
N=len(nodes);dim=4*N
H0=s.zeros(dim);R=s.zeros(dim);eps2=s.zeros(dim)
c=s.zeros(dim,1);inverse_c=s.zeros(dim,1)
v=s.zeros(dim,1);va=[s.zeros(dim,1) for _ in range(3)]
for p,(r,j) in enumerate(nodes):
    at=4*p;c[at]=s.Rational(1,3)
    H0[at,at+j+1]=H0[at+j+1,at]=2*r
    R[at,at]=R[at+j+1,at+j+1]=1
    inverse_c[at+j+1]=c[at]/(2*r)
    v[at+j+1]=r/3;va[j][at+j+1]=r/3
    for k in range(4):eps2[at+k,at+k]=r*r
I0=sum(1/(4*r*r) for r,j in nodes)/N
zeta=inverse_c/s.sqrt(I0)
C=c*c.H;P=s.eye(dim)-C
H=P*H0*P
check(norm2(c)==1,'normalized finite contact measure')
check(zm(H0*inverse_c-c),'reduced inverse contact coefficient')
check(norm2(inverse_c)==I0 and norm2(zeta)==1,'inverse norm uses averaged measure')
check((c.H*zeta)[0]==0 and zm((s.eye(dim)-R)*zeta),'physical and free-flat orthogonality')
check(zm(H*zeta),'actual compression has extra zero vector')
check(H0.rank()==2*N and H.rank()==2*N-2,'actual kernel dimension increase beyond the flat band')
physical_kernel=s.eye(dim)-R+zeta*zeta.H
check(zm(physical_kernel*c),'auxiliary contact zero mode excluded from physical kernel')
check(zm(H*physical_kernel) and zm(physical_kernel**2-physical_kernel),'physical zero-space projector')
check(s.trace(physical_kernel)==2*N+1,'free-flat plus one physical zero dimension')

# Exact free spectral projection onto the high radial value, so the cutoff
# below genuinely lies below the initial band. No asymptotic claim uses this
# discrete fixture's radial values or zero spectral gap.
Gamma=s.zeros(dim)
for p,(r,j) in enumerate(nodes):
    if r==radii[-1]:
        e=s.zeros(dim,1);e[4*p]=e[4*p+j+1]=1/s.sqrt(2)
        Gamma+=e*e.H
check(zm(Gamma**2-Gamma) and zm(H0*Gamma-s.Rational(4,3)*Gamma),'actual positive-band projector')
w=norm2(Gamma*zeta);phi=Gamma*zeta/s.sqrt(w)
beta=s.simplify((c.H*phi)[0]);normal=s.sqrt(1-beta**2)
chi=P*phi/normal;A=s.sqrt(w)/normal
check(norm2(chi)==1 and (c.H*chi)[0]==0,'normalized immediate contact projection')
check(s.simplify((zeta.H*chi)[0]-A)==0,'retained threshold amplitude after projection')
check(zm(physical_kernel*chi-A*zeta),'complete physical zero projection of prepared band state')

# Cutoff inverse: compare an actual H application with the claimed residual.
cut=s.Rational(1,4)
F=[];G=[];formal=[]
for p,(r,j) in enumerate(nodes):
    F.append(s.simplify(chi[4*p]/c[4*p]))
    G.append(s.simplify(chi[4*p+j+1]/c[4*p]))
    formal.append(s.simplify(G[-1]/(2*r)-A/(4*s.sqrt(I0)*r*r)))
check(s.simplify(sum(formal)/N)==0,'formal inverse has zero integrable mean')
mean_cut=s.simplify(sum(f for f,(r,j) in zip(formal,nodes) if r>=cut)/N)
xi=s.zeros(dim,1);residual=s.zeros(dim,1)
for p,((r,j),f) in enumerate(zip(nodes,formal)):
    f_cut=(f if r>=cut else 0)-mean_cut
    xi[4*p]=c[4*p]*f_cut
    xi[4*p+j+1]=c[4*p]*F[p]/(2*r)
    residual[4*p+j+1]=c[4*p]*((A/(2*s.sqrt(I0)*r) if r<cut else 0)-2*r*mean_cut)
check(s.simplify((c.H*xi)[0])==0,'cutoff inverse restores the excluded singlet mean')
check(zm(H*xi-(chi-A*zeta)-residual),'cutoff inverse actual residual identity')

# Actual canonical-current coefficient and its cancellation, with no assigned
# expectation values replacing matrices. Coordinate points are cubic symmetric.
L=[]
for a in range(3):
    free=s.eye(dim)
    for p,(r,j) in enumerate(nodes):
        if a==j:
            for k in range(4):free[4*p+k,4*p+k]-=2*r*r
    correction=va[a]*v.H+v*va[a].H
    current=P*free*P+correction
    L.append(current)
    free_centered=s.simplify((zeta.H*(free-s.eye(dim))*zeta)[0])
    contact=s.simplify((zeta.H*correction*zeta)[0])
    check(s.simplify(free_centered+1/(6*I0))==0,'free threshold current deviation coefficient')
    check(s.simplify(contact-1/(6*I0))==0,'canonical correction cancels threshold deviation')
    check(s.simplify((zeta.H*current*zeta)[0]-1)==0,'canonical centered threshold current is zero')
sum_center=sum(L,s.zeros(dim))-3*P
check(zm(P*R*sum_center*R*P+H**2/2),'conserved canonical trace from squared compression')

# Floating actual finite-time averaging via spectral decomposition. This
# checks the averaging/cutoff identity, not a continuum time-evolution proof.
Hn=np.array(H,dtype=complex);xin=np.array(xi,dtype=complex).ravel()
chin=np.array(chi,dtype=complex).ravel();zn=np.array(zeta,dtype=complex).ravel()
rn=np.array(residual,dtype=complex).ravel();An=float(A)
ev,U=np.linalg.eigh(Hn)
floating=[]
for time in [3.4,20.0,50.0]:
    multiplier=np.exp(-1j*ev*time/2)*np.sinc(ev*time/(2*np.pi))
    mean=U@(multiplier*(U.conj().T@chin))
    actual=float(np.linalg.norm(mean-An*zn))
    bound=2*np.linalg.norm(xin)/time+np.linalg.norm(rn)
    check(actual<=bound+1e-12,'actual finite-time averaging residual bound')
    lhs=U@(multiplier*(U.conj().T@(Hn@xin)))
    rhs=1j*(U@(np.exp(-1j*ev*time)*(U.conj().T@xin))-xin)/time
    check(np.linalg.norm(lhs-rhs)<1e-12,'averaging identity sign from actual unitary')
    floating.append({'T':time,'actual_mean_error':actual,'cutoff_bound':float(bound)})

# Rational certificate for the deliberately conservative lambda<=10^-12
# range in L22. sqrt(12)<4, pi<4, sqrt(23)>4; exponents are bounded at
# the largest lambda, so no floating log-power comparison proves the range.
error_bound=s.Rational(42,5000)+s.Rational(24,10**10)+s.Rational(32,10**12)+s.Rational(4,10**15)
check(error_bound<s.Rational(9,1000)<s.Rational(1,108),'exact finite leakage range certificate')
check(s.Rational(23,324)*s.Rational(1,9)/4==s.Rational(23,11664),'leakage lower coefficient with pi squared separate')

print('Exact finite field: pairs =',N,'I0 =',I0,'free kernel =',dim-H0.rank(),'physical compressed kernel =',s.trace(physical_kernel))
print('Exact packet: band weight =',w,'contact loss =',s.simplify(beta**2),'physical zero weight =',s.simplify(A**2))
print('Canonical coefficients: free =',-1/(6*I0),'correction =',1/(6*I0))
print('Floating averaging controls:',json.dumps(floating,sort_keys=True))
print('Conservative range certificate:',error_bound,'< 9/1000 < 1/108')
print('Scope: exact finite operator/field algebra and floating averaging controls; no finite-grid inference of continuum threshold density, isolated zero mode, or current relaxation.')
print('TOTAL: PASS='+str(checks)+' FAIL=0')
print('Source SHA256:',sha256(Path(__file__).read_bytes()).hexdigest())
''')
# END VERBATIM excluded_walk_long_time/long_time_checks.py

# BEGIN VERBATIM excluded_walk_degenerate/degenerate_checks.py
_run_block('block_2_degenerate_checks', r'''#!/usr/bin/env python3
"""Author controls for the gapless zero-space derivation; no continuum proof by grid.

Literal inputs; no network or repository writes. Exact SymPy algebra is separated
from floating finite-dimensional evolution and unvalidated torus quadrature.
Intended outer process timeout: 120 seconds. Python >=3.10, NumPy/SciPy/SymPy.
"""
import json
import platform
import time

import numpy as np
import scipy
from scipy.linalg import expm
import sympy as sp

START = time.monotonic()
COUNT = 0
ii = sp.I


def check(label, condition):
    global COUNT
    if not condition:
        raise AssertionError(label)
    COUNT += 1
    print(f"PASS {label}", flush=True)


def exact(label, left, right):
    delta = left - right
    if isinstance(delta, sp.MatrixBase):
        good = all(sp.simplify(x) == 0 for x in delta)
    else:
        good = sp.simplify(delta) == 0
    check(label, good)


def cross(x):
    return sp.Matrix([[0, -x[2], x[1]], [x[2], 0, -x[0]], [-x[1], x[0], 0]])


def farray(x):
    return np.array(x.evalf(17).tolist(), dtype=complex)


print(json.dumps({"python": platform.python_version(), "numpy": np.__version__,
                  "scipy": scipy.__version__, "sympy": sp.__version__,
                  "timeout_seconds": 120, "inputs": "literal, deterministic"}))

# Independent Pauli construction fixes the first derivative sign.
pauli = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -ii], [ii, 0]]),
         sp.diag(1, -1)]
spin_c = sp.Matrix([0, 1, -1, 0]) / sp.sqrt(2)
trip = [sp.kronecker_product(x, sp.eye(2)) * spin_c for x in pauli]
ST = sp.Matrix.hstack(spin_c, *trip)
exact("spin basis unitary", ST.H * ST, sp.eye(4))
d = sp.Matrix(sp.symbols("d_1 d_2 d_3", real=True))
raw_B = sp.zeros(4)
for j in range(3):
    raw_B += d[j] * (sp.kronecker_product(pauli[j], sp.eye(2))
                     + sp.kronecker_product(sp.eye(2), pauli[j])) / 2
FIRST_DERIVATIVE_SIGN = 1
expected_B = sp.diag(sp.zeros(1), FIRST_DERIVATIVE_SIGN * ii * cross(d))
exact("Pauli derivative cross sign", ST.H * raw_B * ST, expected_B)
s = sp.Matrix(sp.symbols("s_1 s_2 s_3", real=True))
e2 = (s.T * s)[0]
transverse = sp.eye(3) - s * s.T / e2
PROJECT_BOTH_SIDES = True
candidate_D = (transverse * cross(d) * transverse if PROJECT_BOTH_SIDES else cross(d))
exact("transverse projected cross identity", candidate_D, (d.dot(s) / e2) * cross(s))

# Six positive representatives and their implicit antipodes. The reduced
# pair coordinate has an even singlet and odd triplet. Actual sin/cos pairs
# are rational; the equal probability of each antipodal pair is 1/6.
R = sp.Rational
bases = [(sp.Matrix([R(3, 5), 0, 0]), sp.Matrix([R(4, 5), 1, 1])),
         (sp.Matrix([R(3, 5), R(5, 13), 0]), sp.Matrix([R(4, 5), R(12, 13), 1]))]
fixture = []
for sv, cv in bases:
    for shift in range(3):
        fixture.append((sp.Matrix([sv[(j - shift) % 3] for j in range(3)]),
                        sp.Matrix([cv[(j - shift) % 3] for j in range(3)])))
m = len(fixture)
dim = 4 * m
I0 = sum(1 / (4 * sv.dot(sv)) for sv, _ in fixture) / m
c = sp.zeros(dim, 1)
zeta = sp.zeros(dim, 1)
v = sp.zeros(dim, 1)
va = [sp.zeros(dim, 1) for _ in range(3)]
Hfree = sp.zeros(dim)
F = sp.zeros(dim)
B = sp.zeros(dim)
E2 = sp.zeros(dim)
kap = sp.Matrix([1, 1, 1])
for p, (sv, cv) in enumerate(fixture):
    off = 4 * p
    eps2 = sv.dot(sv)
    c[off] = 1 / sp.sqrt(m)
    Hfree[off, off + 1:off + 4] = 2 * sv.T
    Hfree[off + 1:off + 4, off] = 2 * sv
    F[off + 1:off + 4, off + 1:off + 4] = sp.eye(3) - sv * sv.T / eps2
    zeta[off + 1:off + 4, 0] = sv / (2 * eps2 * sp.sqrt(m * I0))
    v[off + 1:off + 4, 0] = sv / sp.sqrt(m)
    for a in range(3):
        va[a][off + 1 + a] = sv[a] / sp.sqrt(m)
    B[off + 1:off + 4, off + 1:off + 4] = ii * cross(kap.multiply_elementwise(cv))
    E2[off:off + 4, off:off + 4] = eps2 * sp.eye(4)
C = c * c.H
P = sp.eye(dim) - C
Hstar = P * Hfree * P
INCLUDE_DRESSING = True
Pi = F + (zeta * zeta.H if INCLUDE_DRESSING else sp.zeros(dim))
exact("dressing normalization", (zeta.H * zeta)[0], 1)
exact("physical zero projector", Pi * Pi, Pi)
exact("physical zero annihilation", Hstar * Pi, sp.zeros(dim))
check("entire physical zero dimension", Pi.rank() == dim - Hstar.rank() - 1 == 13)
exact("physical zero excludes contact", Pi * c, sp.zeros(dim, 1))
A = Pi * B * Pi
g = F * B * zeta
exact("dressing self coupling zero", (zeta.H * B * zeta)[0], 0)
KEEP_G = True
A_blocks = F * B * F + (g * zeta.H + zeta * g.H if KEEP_G else sp.zeros(dim))
exact("full effective generator includes g", A, A_blocks)
g_reference = sp.zeros(dim, 1)
for p, (sv, cv) in enumerate(fixture):
    dv = kap.multiply_elementwise(cv)
    g_reference[4*p + 1:4*p + 4, 0] = ii * dv.cross(sv) / (2 * sv.dot(sv) * sp.sqrt(m * I0))
exact("actual transverse dressing source", g, g_reference)
check("nonzero dressing source", sp.simplify((g.H * g)[0]) > 0)
exact("effective generator self adjoint", A.H, A)

Ls = []
Js = []
KEEP_PLACEMENT_CORRECTION = True
for a in range(3):
    ma = sp.diag(*[1 - 2 * sv[a]**2 for sv, _ in fixture for _spin in range(4)])
    placement = va[a] * v.H + v * va[a].H
    La = P * ma * P + (placement if KEEP_PLACEMENT_CORRECTION else sp.zeros(dim))
    Ja = Pi * La * Pi
    ra = F * va[a] / (2 * sp.sqrt(I0))
    block = F * ma * F + ra * zeta.H + zeta * ra.H + zeta * zeta.H
    exact(f"canonical block including cross {a}", Ja, block)
    exact(f"canonical dressing cancellation {a}", (zeta.H * La * zeta)[0], 1)
    Ls.append(La)
    Js.append(Ja)
exact("full zero space trace identity", sum(Js, sp.zeros(dim)) - 3 * Pi, -2 * F * E2 * F)
gamma2 = sp.simplify((g.H * E2 * g)[0])
for a in range(3):
    comm = A * Js[a] - Js[a] * A
    exact(f"cyclic first derivative zero {a}", (ii * zeta.H * comm * zeta)[0], 0)
    curvature = -(zeta.H * (A * comm - comm * A) * zeta)[0]
    exact(f"cyclic current second derivative {a}", curvature, -4 * gamma2 / 3)
print("EXACT_FIXTURE", json.dumps({"positive_pairs": m, "dimension": dim,
      "physical_zero_dimension": Pi.rank(), "I0": str(I0), "gamma_squared": str(gamma2)}))

# Numerical finite-dimensional controls: these do not prove a gapless continuum
# limit. They check the cutoff corrector algebra and the actual exponentials.
Hn, Bn, An, Pin, Fn = map(farray, [Hstar, B, A, Pi, F])
cn, zn = farray(c).ravel(), farray(zeta).ravel()
Pn = farray(P)
vn = farray(v).ravel()
van = [farray(x).ravel() for x in va]
Jn = [farray(x) for x in Js]
eig, U = np.linalg.eigh(Hn)
positive = np.abs(eig[np.abs(eig) > 1e-9])
cut = float(np.median(positive))
sel = np.abs(eig) > cut
Q = (U[:, sel] * 1.0) @ U[:, sel].conj().T
inv_cut = (U[:, sel] / eig[sel]) @ U[:, sel].conj().T
Low = np.eye(dim) - Pin - np.outer(cn, cn.conj()) - Q
tau, lam = 0.37, 0.031
vt = expm(-1j * tau * An) @ zn
CORRECTOR_SIGN = -1
y = CORRECTOR_SIGN * inv_cut @ Bn @ vt
yp = -1j * CORRECTOR_SIGN * inv_cut @ Bn @ An @ vt
residual = 1j * (-1j * An @ vt + lam * yp) - (Hn / lam + Bn) @ (vt + lam * y)
reference_residual = -Low @ Bn @ vt + lam * (1j * yp - Bn @ y)
check("cutoff corrector residual sign", np.linalg.norm(residual - reference_residual) < 2e-12)


def supplied_at(lam):
    K = lam * np.ones(3)
    symbol = np.zeros((dim, dim), dtype=complex)
    for p, (sv, cv) in enumerate(fixture):
        sf, cf = np.array(sv, float).ravel(), np.array(cv, float).ravel()
        aa = 2 * np.cos(K / 2) * sf
        dd = 2 * np.sin(K / 2) * cf
        off = 4 * p
        symbol[off, off+1:off+4] = aa
        symbol[off+1:off+4, off] = aa
        symbol[off+1:off+4, off+1:off+4] = farray(ii * cross(sp.Matrix(dd)))
    h = sum((2 * np.cos(K[j] / 2) * van[j] for j in range(3)), np.zeros(dim, complex))
    currents = []
    for a in range(3):
        CURRENT_HPRIME_SIGN = -1
        hp = CURRENT_HPRIME_SIGN * np.sin(K[a] / 2) * van[a]
        diag = np.array([np.sin(K[a]) * (1 - 2 * float(sv[a])**2)
                         for sv, _ in fixture for _spin in range(4)])
        currents.append(Pn @ np.diag(diag) @ Pn - np.outer(hp, h.conj()) - np.outer(h, hp.conj()))
    return Pn @ symbol @ Pn, currents


tau = 0.29
target = expm(-1j * tau * An) @ zn
trans = Fn @ target
trace_target = 1 - 2 * float(np.real(trans.conj() @ farray(E2) @ trans)) / 3
for a in range(3):
    check(f"actual effective cyclic current {a}", abs(np.vdot(target, Jn[a] @ target) - trace_target) < 3e-13)
check("strict effective dressing current response", trace_target < 1 - 1e-4)
rows = []
for lam in [0.04, 0.02, 0.01, 0.005]:
    Hl, Jl = supplied_at(lam)
    b = np.sqrt(3)
    rem = np.linalg.norm((Hl - Hn) / lam - Bn, 2)
    rem_bound = lam * b*b / 4 + lam*lam*b**3 / 24
    check(f"bounded generator expansion lambda={lam}", rem <= rem_bound + 1e-12)
    actual = expm(-1j * tau * Hl / lam) @ zn
    err = np.linalg.norm(actual - target)
    eps = float(np.min(positive) / 2)
    bound = (2 * lam * b + 2 * tau * lam * b*b) / eps + tau * rem_bound
    check(f"finite evolution cutoff bound lambda={lam}", err <= bound + 1e-12)
    current_remainder_bound = lam*lam*((1/6 + np.sqrt(3)/24) + 3/8)
    for a in range(3):
        check(f"actual canonical expansion lambda={lam} axis={a}",
              np.linalg.norm(Jl[a]/lam-farray(Ls[a]), 2) <= current_remainder_bound+1e-12)
    curerr = max(abs(np.vdot(actual, Jl[a] @ actual) / lam - np.vdot(target, Jn[a] @ target)) for a in range(3))
    rows.append({"lambda": lam, "state_error": float(err), "scaled_current_error": float(curerr)})
check("finite evolution tends to effective example", rows[-1]["state_error"] < 0.003)
check("finite canonical current tends to block example", rows[-1]["scaled_current_error"] < 0.003)
print("FLOATING_FINITE_EVOLUTION", json.dumps(rows))

# Actual local cone matrix, rather than assigned oscillation constants.
CONE_STREAMING = 2
M = sp.Matrix([[0, -ii, 0], [ii, 0, CONE_STREAMING], [0, CONE_STREAMING, 0]])
exact("cone matrix cubic polynomial", M**3, 5 * M)
ey = sp.Matrix([1, 0, 0])
at_half_period = (sp.eye(3) - 2 * M**2 / 5) * ey
exact("cone limiting state", at_half_period, sp.Matrix([R(3, 5), 0, -R(4, 5)*ii]))
exact("cone nonuniform squared separation", ((at_half_period-ey).H * (at_half_period-ey))[0], R(4, 5))
actual_cone = expm(-1j * np.pi / np.sqrt(5) * farray(M)) @ np.array([1, 0, 0], complex)
check("actual cone exponential", np.linalg.norm(actual_cone-farray(at_half_period).ravel()) < 1e-14)
eta = R(1, 100)
# pi<4 and 2<sqrt(5)<5/2 give a rational lower margin.
check("cone packet separation rational margin", R(4, 5) - 16*eta > R(1, 2))

# These grid values are floating quadrature illustrations, not error bars for
# the continuum integrals. The analytic integral inequalities are in the note.
qrows = []
for ngrid in [16, 24, 32]:
    axis = -np.pi + (np.arange(ngrid) + 0.5) * (2*np.pi/ngrid)
    q = np.stack(np.meshgrid(axis, axis, axis, indexing="ij"), axis=-1).reshape(-1, 3)
    ss, cc = np.sin(q), np.cos(q)
    ee = np.sum(ss*ss, axis=1)
    Igrid = np.mean(1/(4*ee))
    nn = ss/np.sqrt(ee[:, None])
    numerator = np.sum(cc*cc, axis=1)-np.sum(cc*nn, axis=1)**2
    gamgrid = np.mean(numerator)/(4*Igrid)
    qrows.append({"grid": ngrid, "I0_quadrature": float(Igrid), "gamma2_kappa111_quadrature": float(gamgrid)})
    check(f"quadrature symmetry and analytic bracket n={ngrid}",
          3/(12*Igrid)-1e-12 <= gamgrid <= 3/(8*Igrid)+1e-12)
print("UNVALIDATED_TORUS_QUADRATURE", json.dumps(qrows))
print(json.dumps({"checks": COUNT, "elapsed_seconds": time.monotonic()-START,
                  "scope": "author controls; no independent review or continuum proof by discretization"}))
''')
# END VERBATIM excluded_walk_degenerate/degenerate_checks.py

# BEGIN VERBATIM two_scale_band_current/root_two_scale_controls.py
_run_block('block_3_root_two_scale_controls', r'''#!/usr/bin/env python3
"""Exact finite controls for B5, B8, B12 and the packet margins.

This is author evidence for the two-scale theorem. It proves no gapless
limit by a finite fixture and supplies no quantitative delta onset.
Literal data, no network or author-helper imports. Requires SymPy.
"""
import json
import platform
import time
import sympy as s

start = time.monotonic()
R, I = s.Rational, s.I


def exact(label, lhs, rhs):
    delta = lhs-rhs
    terms = list(delta) if isinstance(delta, s.MatrixBase) else [delta]
    assert all(s.simplify(x) == 0 for x in terms), label
    print("EXACT", label, flush=True)


print(json.dumps({"python": platform.python_version(), "sympy": s.__version__,
                  "scope": "author exact finite controls; no continuum quadrature"}))
pauli = [s.Matrix([[0, 1], [1, 0]]), s.Matrix([[0, -I], [I, 0]]), s.diag(1, -1)]
singlet = s.Matrix([0, 1, -1, 0])/s.sqrt(2)
left = [s.kronecker_product(p, s.eye(2)) for p in pauli]
right = [s.kronecker_product(s.eye(2), p) for p in pauli]
ST = s.Matrix.hstack(singlet, *(p*singlet for p in left))
kap = [R(2, 3), -R(1, 5), R(4, 7)]
fixture = [([R(3, 5), 0, 0], [R(4, 5), 1, 1], R(1, 2)),
           ([0, R(5, 13), 0], [1, R(12, 13), 1], R(1, 3)),
           ([0, 0, R(7, 25)], [1, 1, R(24, 25)], R(1, 6))]
dim = 4*len(fixture)
H0, B, F, E2 = (s.zeros(dim) for _ in range(4))
c, v, zeta = (s.zeros(dim, 1) for _ in range(3))
va = [s.zeros(dim, 1) for _ in range(3)]
I0 = sum(prob/(4*sum(x*x for x in sv)) for sv, cv, prob in fixture)
for j, (sv, cv, prob) in enumerate(fixture):
    off = 4*j
    sv = s.Matrix(sv)
    eps2 = sv.dot(sv)
    c[off] = s.sqrt(prob)
    v[off+1:off+4, 0] = s.sqrt(prob)*sv
    zeta[off+1:off+4, 0] = s.sqrt(prob)*sv/(2*eps2*s.sqrt(I0))
    for a in range(3):
        va[a][off+1+a] = s.sqrt(prob)*sv[a]
    raw_H = sum((sv[a]*(left[a]-right[a]) for a in range(3)), s.zeros(4))
    raw_B = sum((kap[a]*cv[a]*(left[a]+right[a])/2 for a in range(3)), s.zeros(4))
    H0[off:off+4, off:off+4] = ST.H*raw_H*ST
    B[off:off+4, off:off+4] = ST.H*raw_B*ST
    F[off+1:off+4, off+1:off+4] = s.eye(3)-sv*sv.T/eps2
    E2[off:off+4, off:off+4] = eps2*s.eye(4)
P = s.eye(dim)-c*c.H
H = P*H0*P
Pi = F+zeta*zeta.H
Q = P-Pi
exact("physical zero projector", Pi*Pi, Pi)
exact("physical zero excludes auxiliary singlet", Pi*c, s.zeros(dim, 1))
exact("physical zero annihilation", H*Pi, s.zeros(dim))
exact("nonzero subspace projection", Q*Q, Q)
assert Q.rank() == 4
exact("nonzero derivative lands in transverse zero space", B*Q, F*B*Q)
exact("nonzero derivative has no diagonal block", Q*B*Q, s.zeros(dim))
assert B*Q != s.zeros(dim)

L = []
PLACEMENT_FACTOR = 1
for a in range(3):
    ma = s.diag(*[1-2*sv[a]**2 for sv, cv, prob in fixture for _ in range(4)])
    L.append(P*ma*P+PLACEMENT_FACTOR*(va[a]*v.H+v*va[a].H))
TRANSVERSE_TRACE_FACTOR = 2
exact("full physical canonical trace identity", sum(L, s.zeros(dim)),
      3*P-H*H/2-TRANSVERSE_TRACE_FACTOR*E2*F)
assert E2*F != s.zeros(dim)
exact("full trace restricted to nonzero spectrum", Q*sum(L, s.zeros(dim))*Q,
      3*Q-H*H/2)

# The inverse is harmless in this finite fixture; the continuum proof cuts
# it off at sigma and carries the missing low spectral mass explicitly.
Hinv = Q*(H+Pi+c*c.H).inv()*Q
exact("finite nonzero inverse", H*Hinv, Q)
delta = s.symbols("delta", positive=True)
HIGH_CORRECTOR_SIGN = 1
y = HIGH_CORRECTOR_SIGN*B*Hinv*Q
vprime = -I*H*Q/delta
yprime = HIGH_CORRECTOR_SIGN*B*Hinv*vprime
residual = I*(vprime+delta*yprime)-(H/delta+B)*(Q+delta*y)
exact("high-spectrum corrector residual", residual, -delta*B*y)
exact("high-spectrum corrector is a physical zero vector", H*y, s.zeros(dim))
assert y != s.zeros(dim)
print("NONCUBIC_FIXTURE", json.dumps({"pair_probabilities": ["1/2", "1/3", "1/6"],
      "I0_fixture": str(I0), "physical_dimension": dim-1,
      "zero_dimension": Pi.rank(), "nonzero_dimension": Q.rank(),
      "continuum_integral_values": False}))

# Exact sign margins and one global contact normalization.
A2 = s.symbols("A2", positive=True)
radius = A2/777600
delta_over_lambda = A2/44236800
exact("momentum-envelope error budget", 9*radius, A2/86400)
exact("actual-band preparation error budget", 512*delta_over_lambda, A2/86400)
exact("surviving three-component current drift",
      -A2/21600+9*radius+512*delta_over_lambda, -A2/43200)
lam = s.symbols("lambda", positive=True)
exact("explicit band lower coefficient", (-A2/43200).subs(A2, lam/(9*s.pi**2)),
      -lam/(388800*s.pi**2))
free_weights = [R(1, 7), R(2, 7), R(4, 7)]
survival = [R(9, 10), R(4, 5), R(3, 4)]
norm2 = sum(w*n for w, n in zip(free_weights, survival))
GLOBAL_RENORMALIZATION = True
physical_weights = [w*n/(norm2 if GLOBAL_RENORMALIZATION else 1)
                    for w, n in zip(free_weights, survival)]
exact("single global projection normalization", sum(physical_weights), 1)
assert physical_weights != free_weights
fiber_drifts = [-A2/43200, -A2/21600, -A2/14400]
total = s.simplify(sum(w*d for w, d in zip(physical_weights, fiber_drifts)))
assert s.simplify(total/A2) <= -R(1, 43200)
print("EXACT positive global weights preserve the common current bound")
print(json.dumps({"elapsed_seconds": time.monotonic()-start,
                  "limits": "No continuum spectral-mass bound, delta(lambda) rate, or all-state relaxation theorem is computed."}))
''')
# END VERBATIM two_scale_band_current/root_two_scale_controls.py

# BEGIN VERBATIM quantitative_band_current/quantitative_controls.py
_run_block('block_4_quantitative_controls', r'''"""Separate author controls for quantitative weak-momentum band-current onset.

Exact rational parameter budgets and cutoff identities; floating matrices for
pointwise effective orbits, the longitudinal complement and spectral correctors.
The finite fixture is not an infinite torus quadrature or an independent review.
"""
from fractions import Fraction as F
from math import sqrt
import numpy as np

# Exact budget certificate, with 0<lambda<=1/16, sigma=2^-40 lambda^(3/2),
# delta=2^-68 lambda^2, and A>=sqrt(lambda)/12.
eta=F(108,2**28)+F(17,2**23)+F(96,2**40)+F(3,80*2**68)
assert eta<F(1,200000)
assert F(9,2**68)<F(1,345600)             # delta/A^2
assert F(144,2**68)<F(1,44236800)          # delta/(A^2 lambda)
assert F(1,2**42)<F(5,8)                  # sigma/lambda <= a/2
assert F(1,2**68*16)<F(1,32)              # delta/lambda
assert F(4,200000)+F(2,200000**2)+F(8,345600)<F(1,21600)
assert -F(1,21600)+2*F(1,86400)==-F(1,43200)
assert 9*777600==6998400 and 9*43200==388800
assert F(43,5)<=9 and F(807,50)<=17 and F(133,40)<=4 and F(2,15)<=F(1,5)
assert F(4)+F(47,12)<8
print('Exact parameter budget e_perp/A upper bound:',eta,'< 1/200000')
print('Exact current, preparation, support, cutoff-domain and global-drift constant margins verified.')

# Three antipodal pairs, represented in their even-singlet/odd-triplet sectors.
# Each representative is an actual axis sine/cosine point. Choose positive
# weights with sum one and I0 exactly one so the dressing coefficients are rational.
eps=[F(3,5),F(5,13),F(1)]
qcos=[F(4,5),F(12,13),F(0)]
w3=F(1,4)
w1=(F(1)-w3/(4*eps[2]**2)-(1-w3)/(4*eps[1]**2))/(F(1)/(4*eps[0]**2)-F(1)/(4*eps[1]**2))
weights=[w1,1-w1-w3,w3]
assert all(x>0 for x in weights) and sum(weights)==1
assert sum(w/(4*e*e) for w,e in zip(weights,eps))==1
for e,c in zip(eps,qcos):assert e*e+c*c==1

# Exact pure-longitudinal fixture orthogonal to zeta. The cutoff removes one
# atom and has nonzero mean; forgetting the mean would fail this identity.
f=[F(1),-weights[0]*eps[1]/(weights[1]*eps[0]),F(0)]
assert sum(w*x/(2*e) for w,x,e in zip(weights,f,eps))==0
r=F(1,2);m=sum(w*x/(2*e) for w,x,e in zip(weights,f,eps) if e>=r)
xi=[(x/(2*e) if e>=r else F(0))-m for x,e in zip(f,eps)]
res=[2*e*y-x for e,y,x in zip(eps,xi,f)]
assert m!=0 and sum(w*y for w,y in zip(weights,xi))==0
assert res==[-(x if e<r else 0)-2*e*m for x,e in zip(f,eps)]
assert sum(w*y*y for w,y in zip(weights,xi))<=sum(w*(x/(2*e))**2 for w,x,e in zip(weights,f,eps) if e>=r)
print('Exact longitudinal cutoff: I0=1, nonzero removed mean',m,'and complete residual identity verified.')

N=12;c=np.zeros(N,complex);zeta=np.zeros(N,complex);H0=np.zeros((N,N),complex)
Fflat=np.zeros((N,N),complex);B=np.zeros((N,N),complex);kap=np.array([1.,2.,-1.]);b=np.linalg.norm(kap)

def cross(d):
    x,y,z=d;return np.array([[0,-z,y],[z,0,-x],[-y,x,0]],complex)

for i,(wi,ei,ci) in enumerate(zip(weights,eps,qcos)):
    weight=float(wi);epsilon=float(ei);normal=np.eye(3)[i]
    c[4*i]=sqrt(weight);zeta[4*i+1:4*i+4]=sqrt(weight)*normal/(2*epsilon)
    H0[4*i,4*i+1:4*i+4]=2*epsilon*normal;H0[4*i+1:4*i+4,4*i]=2*epsilon*normal
    Fflat[4*i+1:4*i+4,4*i+1:4*i+4]=np.eye(3)-np.outer(normal,normal)
    cq=np.ones(3);cq[i]=float(ci)
    B[4*i+1:4*i+4,4*i+1:4*i+4]=1j*cross(kap*cq)
P=np.eye(N)-np.outer(c,c.conj());Hstar=P@H0@P
Pi=Fflat+np.outer(zeta,zeta.conj());Q=P-Pi;A=Pi@B@Pi
assert np.linalg.norm(zeta)==1
assert np.linalg.norm(Hstar@zeta)<1e-14 and np.linalg.norm(Pi@Pi-Pi)<1e-14
assert np.linalg.norm(Q@B@Q)<1e-14 and np.linalg.norm(B@Q-Fflat@B@Q)<1e-14


def evolve(H,t,v):
    e,U=np.linalg.eigh(H);return U@(np.exp(-1j*t*e)*(U.conj().T@v))

es,Vs=np.linalg.eigh(Hstar);positive=sorted(set(round(abs(x),8) for x in es if abs(x)>1e-8))
sigma=(positive[0]+positive[-1])/2
mask=(np.abs(es)>1e-8)&(np.abs(es)<=sigma)
Es=Vs[:,mask]@Vs[:,mask].conj().T
assert 0<np.count_nonzero(mask)<np.count_nonzero(np.abs(es)>1e-8)
max_cut_mean=0.
for tau in (-.2,-.05,0.,.05,.2):
    orbit=evolve(A,tau,zeta);u=Fflat@orbit;alpha=np.vdot(zeta,orbit);y=Q@B@orbit
    assert abs(alpha)<=1+1e-13 and np.linalg.norm(Fflat@y)<1e-13 and abs(np.vdot(zeta,y))<1e-13
    fs=[]
    for i,(wi,ei) in enumerate(zip(weights,eps)):
        ui=u[4*i+1:4*i+4]/sqrt(float(wi));normal=np.eye(3)[i]
        assert np.linalg.norm(ui)<=abs(tau)*b/(2*float(ei))+1e-13
        fi=np.dot(normal,y[4*i+1:4*i+4])/sqrt(float(wi));fs.append(fi)
        assert abs(fi)<=b*b*abs(tau)/float(ei)+1e-13
    mean=sum(float(wi)*fi/(2*float(ei)) for wi,fi,ei in zip(weights,fs,eps) if ei>=r)
    max_cut_mean=max(max_cut_mean,abs(mean))
    cut=np.zeros(N,complex)
    for i,(wi,fi,ei) in enumerate(zip(weights,fs,eps)):
        cut[4*i]=sqrt(float(wi))*((fi/(2*float(ei)) if ei>=r else 0)-mean)
    residual=Hstar@cut-y;formula=np.zeros(N,complex)
    for i,(wi,fi,ei) in enumerate(zip(weights,fs,eps)):
        formula[4*i+1+i]=sqrt(float(wi))*(-(fi if ei<r else 0)-2*float(ei)*mean)
    assert np.linalg.norm(residual-formula)<1e-13
    assert np.linalg.norm(Es@y)<=np.linalg.norm(residual)+sigma*np.linalg.norm(cut)+1e-13
assert max_cut_mean>1e-4
print('Five actual effective orbits: pointwise bound, pure-longitudinal Q B orbit, cutoff mean and nontrivial spectral-cutoff inequality verified.')

# Corrector identities and finite estimates tested without replacing Hstar's
# complement by a pointwise uncompressed inverse.
Hinv=Vs@np.diag([1/x if abs(x)>sigma else 0 for x in es])@Vs.conj().T
v=evolve(A,.13,zeta);vprime=-1j*A@v;y=-Hinv@B@v;yprime=-Hinv@B@vprime
delta=.017;w=v+delta*y
lhs=1j*(vprime+delta*yprime)-(Hstar/delta+B)@w
rhs=-Es@B@v+delta*(1j*yprime-B@y)
assert np.linalg.norm(lhs-rhs)<1e-12
x=Vs[:,np.argmax(es)];v=evolve(Hstar,.13/delta,x);y=B@Hinv@v
assert np.linalg.norm(Hstar@y)<1e-13
vprime=-1j*Hstar@v/delta;yprime=B@Hinv@vprime
lhs=1j*(vprime+delta*yprime)-(Hstar/delta+B)@(v+delta*y)
assert np.linalg.norm(lhs+delta*B@y)<1e-12
print('Both zero-space and complementary high-spectral corrector residuals reconstructed from matrices.')

# Full-space trace identity: a fixture need not be cubically invariant for it.
V=np.zeros(N,complex);va=[];Ls=[];eps2=np.zeros((N,N),complex)
for a in range(3):
    vj=np.zeros(N,complex);mult=np.zeros((N,N),complex)
    for i,(wi,ei) in enumerate(zip(weights,eps)):
        sj=float(ei) if a==i else 0.
        vj[4*i+1+a]=sqrt(float(wi))*sj
        mult[4*i:4*i+4,4*i:4*i+4]=(1-2*sj*sj)*np.eye(4)
        eps2[4*i:4*i+4,4*i:4*i+4]=float(ei)**2*np.eye(4)
    va.append(vj);V+=vj;Ls.append(P@mult@P)
for a in range(3):Ls[a]+=np.outer(va[a],V.conj())+np.outer(V,va[a].conj())
assert np.linalg.norm(sum(Ls)-(3*P-Hstar@Hstar/2-2*eps2@Fflat))<1e-13
print('Full physical-space current trace identity verified; no rotational equality of components assumed for this non-cubic fixture.')
print('Controls complete. Floating finite matrices do not prove the torus cone integral bounds or the infinite-dimensional evolution estimate.')
''')
# END VERBATIM quantitative_band_current/quantitative_controls.py

print('Complete finite controls; no independent audit or continuum proof is inferred.')
print('Runner SHA256:', sha256(Path(__file__).read_bytes()).hexdigest())
print('Elapsed seconds:', format(perf_counter()-_started, '.6f'))
