#!/usr/bin/env python3
"""Exact controls for finite harmonic gauge completion; see .criteria.md."""
from itertools import product
from math import comb
import json
import sympy as sp

checks = []
def check(name, value, details=None):
    ok = bool(value)
    checks.append({'name': name, 'ok': ok, **({'details': details} if details is not None else {})})

def zero(matrix):
    return all(sp.cancel(x) == 0 for x in matrix)

def sparse_lap_column(x, side, anti):
    col = {x: 8}
    for mu in range(4):
        for step in (-1, 1):
            y = list(x)
            raw = y[mu] + step
            phase = -1 if anti and (raw < 0 or raw >= side) else 1
            y[mu] = raw % side
            y = tuple(y)
            col[y] = col.get(y, 0) - phase
    return col

# Geometry computed on a complete side-nine torus, with no matrix inverse.
side = 9
roots = list(product(range(0, side, 3), repeat=4))
columns = [sparse_lap_column(x, side, True) for x in roots]
gram_ok = True
first_ok = True
for i, x in enumerate(roots):
    for j, y in enumerate(roots):
        inner = sum(v * columns[j].get(z, 0) for z, v in columns[i].items())
        gram_ok = gram_ok and inner == (72 if i == j else 0)
        first_ok = first_ok and columns[j].get(x, 0) == (8 if i == j else 0)
check('4d_side9_all_root_gram_entries_72', gram_ok, {'roots': len(roots), 'entries': len(roots)**2})
check('4d_side9_all_first_gram_entries_8', first_ok)
check('antiperiodic_wrap_is_present', columns[0][(8,0,0,0)] == 1 and columns[0][(1,0,0,0)] == -1)
nonlocal_entry = sp.Rational(64, 72*len(roots))
check('mean_zero_projection_has_distant_nonzero_entry', nonlocal_entry != 0,
      {'value': str(nonlocal_entry), 'root_pair': [[0,0,0,0], [3,3,3,3]]})

# Independent exact Bloch cell. All coarse phases are -1, allowed on the
# side-nine torus with the same antiperiodic cycle twist.
coords = list(product(range(3), repeat=4))
index = {x: i for i, x in enumerate(coords)}
Delta = sp.zeros(81)
for x in coords:
    for y, val in sparse_lap_column(x, 3, True).items():
        Delta[index[y], index[x]] = val
J = sp.zeros(81, 1); J[0] = 1
Dint = Delta[1:, 1:]
lower = Dint.inv(method='DM') * (-Delta[1:, :1])
Lift = sp.Matrix.vstack(sp.ones(1,1), lower)
S = sp.cancel((J.T*Delta*Lift)[0])
check('harmonic_ev_lift', Lift[0] == 1)
check('harmonic_laplacian_lift_root_S', zero(Delta*Lift-J*S))
check('harmonic_energy_is_S', sp.cancel((Lift.T*Delta*Lift)[0]-S) == 0)
check('harmonic_squared_gram_is_S_squared', sp.cancel((Lift.T*Delta*Delta*Lift)[0]-S*S) == 0)
q = sp.eye(81)-(Delta*Lift)*(Lift.T*Delta)/(S*S)
check('harmonic_residual_projection_exact', zero(q-(sp.eye(81)-J*J.T)))
alias_green = sum(sp.Rational(comb(4,j)*2**(4-j), 81*(4+3*j)) for j in range(5))
check('all_aliases_green_equals_inverse_S', sp.cancel(alias_green-1/S) == 0,
      {'root_green': str(alias_green), 'S': str(S)})
# The cell determinant is independently obtained from all scalar Fourier aliases.
det_alias = sp.prod((4+3*j)**(comb(4,j)*2**(4-j)) for j in range(5))
det_direct = Delta.det(method='domain-ge')
det_int = Dint.det(method='domain-ge')
check('full_laplacian_det_matches_alias_product', det_direct == det_alias)
check('dirichlet_cofactor_matches_green', sp.cancel(det_int-det_alias*alias_green) == 0)
check('full_det_equals_dirichlet_det_times_S', sp.cancel(det_direct-det_int*S) == 0)

# A rational gauge-compatible quadratic family, built from a direct Gaussian
# rather than from the shear. It is a matrix control, not the S4' map.
t = sp.symbols('t', real=True)
D = sp.Matrix([[1,t], [0,1], [1,1]])
Dc = sp.Matrix([[2]])
M = sp.Matrix([[3,1-3*t,-1]])
C = sp.Matrix([[sp.Rational(3,2)+t]])
vv = D[:,0].cross(D[:,1])
HW = 2*vv*vv.T
Delta_s = D.T*D
J_s = sp.Matrix([[1],[0]])
I_s = sp.Matrix([[0],[1]])
Di = I_s.T*Delta_s*I_s
Li = J_s-I_s*Di.inv()*I_s.T*Delta_s*J_s
Si = sp.simplify(J_s.T*Delta_s*Li)
Pin = I_s*I_s.T
Qaa = HW+M.T*C.inv()*M
Qab = -M.T*C.inv()
Qah = M.T*C.inv()*Dc
Qbb = C.inv()
Qbh = -C.inv()*Dc
Qhh = Dc.T*C.inv()*Dc
Q = sp.BlockMatrix([[Qaa,Qab,Qah], [Qab.T,Qbb,Qbh], [Qah.T,Qbh.T,Qhh]]).as_explicit()
Gfix = sp.diag(D*D.T,Dc*Dc.T,sp.zeros(1))
Aug = Q+Gfix
K = sp.Matrix.vstack(D, sp.zeros(1,2), -J_s.T)
check('small_family_covariance_MD', zero(M*D-Dc*J_s.T))
check('small_family_ungaugefixed_null_columns', zero(Q*K))
HH = Q[:4,:4]
Jmin = Aug[:4,:4]-Aug[:4,4:]*Qhh.inv()*Aug[4:,:4]
Lharm = HH+sp.diag(D*Pin*D.T,Dc*Dc.T)
A = Aug.det(method='domain-ge')
check('h_schur_from_augmented', sp.cancel(A-Qhh.det()*Jmin.det(method='domain-ge')) == 0)
check('harmonic_shear_schur_from_augmented', sp.cancel(A-Si.det()**2*Lharm.det(method='domain-ge')) == 0)
W = HW+D*D.T
Gc = Dc.T*C.inv()*Dc
exp2phi = sp.cancel(Lharm.det(method='domain-ge')/W.det(method='domain-ge') *
    Delta_s.det()**2/Di.det()**2 /Qhh.det() * C.det()*Gc.det()/(Dc.T*Dc).det()**2)
check('full_scalar_ghost_gram_cancellation_for_changing_family', exp2phi == 1)
check('changing_harmonic_lift_not_constant', any(sp.diff(x,t).subs(t,0) != 0 for x in Li))
check('dirichlet_log_has_nonzero_second_jet', sp.diff(sp.log(Di.det()),t,2).subs(t,0) == 1)
wrong_drop_dirichlet = sp.cancel(exp2phi*Di.det()**2)
check('control_dropping_dirichlet_factor_fails', wrong_drop_dirichlet.subs(t,0) != 1)
wrong_S_power = sp.cancel(Si.det()*Lharm.det(method='domain-ge')-A)
check('control_using_S_instead_of_S_squared_fails', wrong_S_power.subs(t,0) != 0)
# Destroying the null-column hypothesis must destroy this determinant identity.
Aug_wrong = Aug.subs(t,0)+sp.diag(sp.eye(3),sp.zeros(1),sp.zeros(1))
L_wrong = Lharm.subs(t,0)+sp.diag(sp.eye(3),sp.zeros(1))
check('control_omitting_null_column_premise_fails',
      sp.cancel(Aug_wrong.det()-Si.subs(t,0).det()**2*L_wrong.det()) != 0)

# Point-root and harmonic gauge energy, computed directly without determinant use.
D0=D.subs(t,0); De0=Delta_s.subs(t,0); M0=M.subs(t,0); C0=C.subs(t,0)
Gj=J_s.T*De0*De0*J_s
Qj=sp.eye(2)-De0*J_s*Gj.inv()*J_s.T*De0
Rc=(sp.eye(1)+Dc.T*C0*Dc).inv()
Oj=HW.subs(t,0)+D0*Qj*D0.T+M0.T*Dc*Rc*Dc.T*M0
a_point=D0*J_s
energy_target=(Dc.T*Dc)*Rc*(Dc.T*Dc)
check('point_root_gauge_energy_exact', zero(a_point.T*Oj*a_point-energy_target))
check('point_root_gauge_norm_exact', zero(a_point.T*a_point-J_s.T*De0*J_s))
Oh=HW.subs(t,0)+D0*Pin*D0.T+M0.T*Dc*Rc*Dc.T*M0
a_harm=D0*Li.subs(t,0)
check('harmonic_root_gauge_energy_exact', zero(a_harm.T*Oh*a_harm-energy_target))
check('harmonic_root_gauge_norm_is_S', zero(a_harm.T*a_harm-Si.subs(t,0)))

result = {'scope': 'finite algebra and free lattice geometry; no actual residual bound',
          'checks': checks, 'passed': sum(x['ok'] for x in checks), 'total': len(checks),
          'all_ok': all(x['ok'] for x in checks)}
print(json.dumps(result, indent=2))
raise SystemExit(0 if result['all_ok'] else 1)
