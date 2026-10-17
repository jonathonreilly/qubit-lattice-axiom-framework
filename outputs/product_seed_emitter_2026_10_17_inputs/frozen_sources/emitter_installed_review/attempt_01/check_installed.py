#!/usr/bin/env python3
"""Independent exact noncommuting-tail and conservative-bound checks.

No author code is imported or executed. The small model contains one open
and one closed channel, noncommuting real contact matrices, and complex loop
bonds. Its direct finite outgoing problem is the source of the comparisons.
The physical interval bounds are independently enclosed by looser rational
ceilings; no momentum sampling is used as an interval certificate.
"""
import json
import resource
import sys
import time
from fractions import Fraction as F
from pathlib import Path

resource.setrlimit(resource.RLIMIT_CPU, (45, 45))
START = time.monotonic()
import sympy as s
ROOT = Path(__file__).resolve().parent

def simp(x):
    return s.cancel(s.expand_complex(x))

def cleaned(m):
    return m.applyfunc(simp)

def exact_zero(m):
    return cleaned(m) == s.zeros(*m.shape)

def serial(m):
    return [[str(simp(m[i,j])) for j in range(m.cols)] for i in range(m.rows)]

def first_nonzero(m):
    for i in range(m.rows):
        for j in range(m.cols):
            x = simp(m[i,j])
            if x != 0:
                return {"row": i, "column": j, "value": str(x)}
    raise AssertionError("Discriminator did not distinguish the wrong expression")

def rat(x):
    return {"exact": str(x), "approximate_display": float(x)}

R = s.Rational
ii = s.I
eye = s.eye(2)
J = s.Integer(1)
z = (3+4*ii)/5
q = R(1,7)
phase = (5+12*ii)/13
coupling = R(1,13)
E0toy = R(1,7)
energy = R(4,5)
bulk = s.diag(0,R(208,35))
Q = s.diag(z,q)
A = (J*(Q-Q.inv())).inv()
assert exact_zero((energy-2*J)*eye-bulk+J*(Q+Q.inv()))
V0 = s.Matrix([[R(1,3),R(1,5)],[R(1,5),-R(2,7)]])
V1 = s.Matrix([[R(1,4),-R(1,6)],[-R(1,6),R(2,9)]])
assert not exact_zero(V0*bulk-bulk*V0)
assert not exact_zero(V1*bulk-bulk*V1)
L = 3
last = 5
size = 2*(last+1)

# Direct finite matrix with exact outgoing/decaying Robin boundary at last.
clock = s.zeros(size)
for n in range(last+1):
    clock[2*n:2*n+2,2*n:2*n+2] = (energy-2*J)*eye-bulk
    if n < last:
        clock[2*n:2*n+2,2*n+2:2*n+4] = J*eye
        clock[2*n+2:2*n+4,2*n:2*n+2] = J*eye
clock[:2,:2] -= V0
clock[2:4,2:4] -= V1
clock[-2:,-2:] += J*Q
green = cleaned(clock.inv(method="DM"))
assert exact_zero(clock*green-s.eye(size))

small = s.zeros(4)
small[:2,:2] = (energy-2*J)*eye-bulk-V0
small[:2,2:] = J*eye
small[2:,:2] = J*eye
small[2:,2:] = -J*Q.inv()-V1
small_inv = cleaned(small.inv(method="DM"))
T = cleaned(small_inv[2:,2:]-A)
assert not exact_zero(T*Q-Q*T)

# Check every pair in the sampled finite tail against a separately inverted
# complete outgoing operator. No commutativity of T and Q is available.
gluing_pairs = []
for n in range(2,last+1):
    for m in range(2,last+1):
        prediction = A*Q**abs(n-m)+Q**(n-1)*T*Q**(m-1)
        assert exact_zero(green[2*n:2*n+2,2*m:2*m+2]-prediction)
        gluing_pairs.append([n,m])
wrong_order = A*Q**2+T*Q**4
wrong_order_residual = green[4:6,8:10]-wrong_order  # n=2,m=4

V = s.zeros(size,2)
V[2*L:2*L+2,:] = eye
V[2*(L+2):2*(L+2)+2,:] = -phase*eye
X = Q**(L-1)*(eye-s.conjugate(phase)*Q**2)
Y = Q**(L-1)*(eye-phase*Q**2)
sigma_direct = cleaned(V.H*green*V)
sigma_free = cleaned(A*(2*eye-(phase+s.conjugate(phase))*Q**2))
assert exact_zero(sigma_direct-(sigma_free+X*T*Y))
wrong_sigma_residual = sigma_direct-(sigma_free+Y*T*X)

# Assemble the whole attached graph before eliminating any tail coordinates.
whole = s.zeros(size+2)
whole[:size,:size] = clock
whole[:size,size:] = -coupling*V
whole[size:,:size] = -coupling*V.H
whole[size:,size:] = (energy-E0toy)*eye-bulk
keep = list(range(4))+list(range(size,size+2))
remove = list(range(4,size))
direct_aug = cleaned(whole.extract(keep,keep)
    -whole.extract(keep,remove)*whole.extract(remove,remove).inv(method="DM")
    *whole.extract(remove,keep))
aug = s.zeros(6)
aug[:4,:4] = small
aug[2:4,4:6] = -coupling*Y
aug[4:6,2:4] = -coupling*X
aug[4:6,4:6] = (energy-E0toy)*eye-bulk-coupling**2*(sigma_free-X*A*Y)
assert exact_zero(direct_aug-aug)
de_direct = cleaned(direct_aug[4:,4:]
    -direct_aug[4:,:4]*small_inv*direct_aug[:4,4:])
assert exact_zero(de_direct-((energy-E0toy)*eye-bulk-coupling**2*sigma_direct))
wrong_aug = aug.copy()
wrong_aug[4:6,2:4] *= -1

# Actual unit-incoming stationary solve at the last site, distinct from a
# proposed reflection formula. The incoming Robin defect fixes its RHS.
rhs = s.zeros(size,1)
rhs[-2,0] = J*(z-z**-1)*z**(-last)
background = cleaned(green*rhs)
rbg = simp((background[-2,0]-z**(-last))/z**last)
assert simp(rbg*s.conjugate(rbg)-1) == 0
assert simp(T[0,0]-A[0,0]*z*z*rbg) == 0
rhs_all = s.zeros(size+2,1)
rhs_all[:size,:] = rhs
solution = cleaned(whole.inv(method="DM")*rhs_all)
drive = cleaned(V.H*background)
ye = cleaned(coupling*de_direct.inv(method="DM")*drive)
assert exact_zero(solution[-2:,:]-ye)
assert exact_zero(solution[:size,:]-(background+coupling*green*V*ye))
raug = simp((solution[-4,0]-z**(-last))/z**last)
assert simp(raug*s.conjugate(raug)-1) == 0
dtail = A*(Q**2-phase*eye)+Q**(L+1)*T*Y
brow = z**(-L-2)*dtail[0,:]
assert simp(raug-rbg-coupling*(brow*ye)[0]) == 0
gp = z**(-L)*(1-phase*z**-2)
gm = z**L*(1-phase*z**2)
assert simp(brow[0]-A[0,0]*(gp+rbg*gm)) == 0
assert simp(drive[0]-s.conjugate(gm)-rbg*s.conjugate(gp)) == 0
assert drive[1] != 0 and ye[1] != 0

# Scalar reference spectral density, obtained from the two-contact kernel.
kernel = A[0,0]*s.Matrix([[1,z*z],[z*z,1]])
vlocal = s.Matrix([1,-phase])
sf = simp((vlocal.H*kernel*vlocal)[0])
df = simp(energy-E0toy-coupling**2*sf)
speed = J*(z-z**-1)/ii
aa = simp(gp*s.conjugate(gp))
bb = simp(gm*s.conjugate(gm))
jump_dk_times_pi = simp(-s.im(1/df)*speed)
weights_dk_times_pi = simp(coupling**2*(aa+bb)/(2*df*s.conjugate(df)))
assert simp(jump_dk_times_pi-weights_dk_times_pi) == 0
wrong_density = simp(-s.im(1/df)-weights_dk_times_pi)
assert wrong_density != 0

# Full operator overlap requires the whole two-column Hermitian matrix.
seed = s.eye(4)[:,:2]
rot = s.Matrix([[R(3,5),R(4,5)],[-R(4,5),R(3,5)]])
unitary = ((5+12*ii)/13)*rot
packet = s.zeros(4,2)
packet[:2,:] = R(12,13)*unitary
packet[2:,:] = R(5,13)*eye
assert exact_zero(packet.H*packet-eye)
overlap = cleaned(seed.H*packet)
error_gram = cleaned((seed-packet).H*(seed-packet))
assert exact_zero(error_gram-(2*eye-overlap-overlap.H))
error_eigenvalues = sorted(error_gram.eigenvals().keys())
diagonal_only = error_gram[0,0]
assert error_eigenvalues[-1] > diagonal_only
off = s.Matrix([[0,R(3,1000)+ii*R(4,1000)],
                [R(5,2000)-ii*R(12,2000),0]])
assert exact_zero(off.H*off-s.diag(R(169,4000000),R(25,1000000)))
aligned = s.Matrix([[1,1]])
assert (aligned*aligned.H)[0] == 2

# Independent rounded rational enclosures. These do not read author output.
j = F("0.030021107107032")
center_q = F("4.510351185997098")
cs = (center_q**2-1)/(center_q**2+1)
sn = 2*center_q/(center_q**2+1)
sin2 = 2*cs*sn
k = F(1,10**12)
width = F(1,10**6)
v = F(1,40)
gap = F(9,50)
r = F(1,7)
assert cs*cs+sn*sn == 1
assert 2*j*(sn-width)>v and 2*k<2*j*(1-cs)
eta = F(131,10**8)  # 1.31e-6
delta = F(52,10**11)  # 5.2e-10
wc = F(58,10**9)  # 5.8e-8
assert width/(sin2-width)<eta
assert (1+r*r)*r**11<delta
assert 16*(1+r*r)*r**10<wc
assert sin2>F(3,4)
gamma = F(977,50)  # 19.54
assert (2*sin2-2*width)**2/(4*j)>gamma
Sclosed = 2*(1+r*r)/gap+delta*delta*206
assert gap-k*k*Sclosed>F(1,6)
pq,qp = 2*width*206*delta, delta*206*2
xi = F(263,10**8)  # 2.63e-6
assert 2*eta+k*k*pq*6*qp/gamma < xi
assert gamma*(1-xi)>19
de_bound = (1+k*k*pq*6)*(1+k*k*qp*6)/(19*k*k)+6
aug_bound = (1+166*k*2)*(1+166*k*2*width)/(18*k*k)
assert de_bound<1/(18*k*k) and aug_bound<1/(17*k*k)
eta_profile = F(3941,10**9)
assert (eta+k*k*pq*6*wc/F(3,2)+xi)/(1-xi)<eta_profile
off_bound = F(35,10**20)
assert 6*k*wc+6*k*k*delta*206*2*(1+eta_profile)<off_bound
mass_bound = F(13,10**9)
h = width/2
assert 2*k*k/(v*h)**2+(h/(F(3,4)-h))**2 < mass_bound
seed_sq_bound = 2*(mass_bound+eta_profile+off_bound)
assert seed_sq_bound < F(3,1000)**2
eps_closed = (6*k*k*206*delta*wc
    +6*k*k*delta**2*206**2*2*(1+eta_profile)*4*j/F(3,2))
phase_bound = 2*eta+2*(1+eta)*eta_profile+eps_closed+4*eta**2
assert phase_bound<F(11,10**6)
assert F(176,10**15)+702*width+F(11,10**6)<F(714,10**6)

assert 2*j/(1-r*r)<F(62,1000)
assert 166**2*F(62,1000)<1710
assert 2*j/v**2<100 and 2*j/gap**2<100
sigma_prime = 560+24*206*2+(2*width)*2000*2+(2*width)*206*24
assert sigma_prime<11000
assert 2*j+11000*k*k<F(61,1000)
diag_prime = 2*j+k*k*(560+24*40*2+2*width*100*2+2*width*40*24)
assert max(F(62,1000),diag_prime)+24*k<F(63,1000)
assert k*(3*F(61,1000)/(18*k*k)**2+30/(18*k*k))<k**-3
wc_prime = ((700*(1+r*r)+32*r/F(24))*r**10
            +16*10*(1+r*r)*r**9/F(24))
assert 26+700*2*width+(12*2*width+2)+wc_prime<30
assert 1/(1-r*r)<F(1011,1000)**2
assert (1+r*r)/(1-r*r)**3<F(21,20)**2
K0 = 332+2*492+12*(492+492)+492*F(1011,1000)
K1 = (7404+492+2*21468+12*(16000+13*492+21468)
      +14580*F(1011,1000)+492*F(1,24)*F(21,20))
assert K0<20000 and K1<10**6
assert 31+(1+20000*k)/k<2*10**12
assert 2700+10**6+(1+20000*k)/k**3<2*10**36
assert 700+21468+492/k**2<1000/k**2
assert 26/(19*k)+2*F(61,1000)/(19**2*k**3)<1/k**3
assert 2*width<F(1,500)**2
assert F(12,5)*F(99,100)>2
assert 1/k+width/k**3<2*10**30
assert F(720,19)+160*F(61,1000)/(19**2*k**2)<1/k**2
assert 2+4/k**2<5/k**2
F0,F1=F(1,500),F(2*10**30)
assert F1+F(5,2)*F0<3*10**30
assert F1+(5/k**2+F(5,2))*F0<3*10**30
Dj=F1*2*10**12+F0*2*10**36+F(5,2)*F0*2*10**12
assert Dj<5*10**42 and 2*Dj**2<(8*10**42)**2
onset=10**72
root_floor=27*10**34
assert root_floor**2<3*v*onset
escape=F(6*10**30,root_floor)+F(8*10**42)/(F(12,5)*v*onset)
joint=F(3,1000)+F(714,10**6)+escape
assert joint<F(4,1000)
assert F(3*10**30,root_floor)<F(1,2)
M=5*10**73
distance=M-12-1
horizon_margin=distance-19*(2*onset)*F(6,5)-9
assert horizon_margin>0
assert joint+F(1,1000)<F(5,1000)
assert 2*k/(v*width)==F(1,12500)

result = {
    "scope": "New exact model and independent conservative inequalities; no author-code replay or physical momentum sampling",
    "small_model": {
        "internal_dimension": 2, "open_channels": 1, "closed_channels": 1,
        "L": L, "last_retained_clock": last, "largest_matrix_dimension": size+2,
        "J": str(J), "z": str(z), "q": str(q), "phase": str(phase),
        "coupling": str(coupling), "emitter_energy": str(E0toy),
        "energy": str(energy), "B": serial(bulk), "V0": serial(V0), "V1": serial(V1),
        "commutator_T_Q_nonzero": first_nonzero(T*Q-Q*T),
        "tail_pairs_exactly_checked": gluing_pairs,
        "direct_augmented_matching": serial(direct_aug),
        "direct_emitter_schur": serial(de_direct),
        "background_reflection": str(rbg), "augmented_reflection": str(raug),
        "full_closed_emitter_coordinate": str(ye[1]),
        "green_jump_and_matching_identities": "exact",
        "full_augmented_flux": "exact unit modulus",
        "wrong_tail_order": first_nonzero(wrong_order_residual),
        "wrong_X_Y_order": first_nonzero(wrong_sigma_residual),
        "wrong_augmented_lower_sign": first_nonzero(direct_aug-wrong_aug),
    },
    "reference_measure": {
        "jump_times_velocity_equals_sum_dk_weights": str(jump_dk_times_pi),
        "omitted_velocity_residual": str(wrong_density),
        "global_mass_reason": "normalized seed spectral measure of a bounded selfadjoint full-line Hamiltonian; analytically reviewed, not inferred from this point",
    },
    "complete_overlap_discriminators": {
        "rectangular_isometry_shape": [4,2],
        "seed_overlap_matrix": serial(overlap),
        "exact_error_gram": serial(error_gram),
        "exact_squared_operator_error": str(error_eigenvalues[-1]),
        "incorrect_diagonal_only_ceiling": str(diagonal_only),
        "off_diagonal_matrix_gram": serial(off.H*off),
        "aligned_column_squared_operator_norm": 2,
        "aligned_maximum_individual_column_squared_norm": 1,
    },
    "independent_uniform_enclosures": {
        "eta": rat(eta), "delta": rat(delta), "closed_drive": rat(wc),
        "gamma_lower": rat(gamma), "xi": rat(xi),
        "profile_relative_error": rat(eta_profile), "off_overlap": rat(off_bound),
        "reference_mass_loss": rat(mass_bound),
        "seed_squared_error": rat(seed_sq_bound),
        "reflection_correction": rat(phase_bound),
        "K0_expression": rat(K0), "K1_expression": rat(K1),
        "Dj": rat(Dj), "escape": rat(escape), "all_future_error": rat(joint),
        "finite_horizon_exponent_margin": str(horizon_margin),
        "point_spectrum_operator_ceiling": "1/12500",
        "headline_bounds_recovered": {
            "seed": "3/1000", "phase": "714/1000000",
            "all_future": "4/1000", "finite_horizon": "5/1000",
        },
    },
    "runtime": {"python": sys.version, "sympy": s.__version__,
                "elapsed_seconds": time.monotonic()-START, "maximum_matrix_dimension": size+2},
    "limits": [
        "The small exact model checks conventions and noncommuting identities, not the physical interval",
        "The interval certificate follows analytic norm inequalities with inherited ladder constants",
        "No new physical point-state certificate, optimizer, wavepacket quadrature or large-clock evolution",
        "Reviewer authored earlier stationary ladder and reviewed earlier generic packet proof; source-exposed same model",
    ],
}
print(json.dumps(result,indent=2))
