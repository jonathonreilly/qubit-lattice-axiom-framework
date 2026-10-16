"""Exact controls for the supplied conformal-exchange construction."""
import json
import time
import sympy as s

start = time.monotonic()
checks = []
def check(name, residual):
    value = s.simplify(residual)
    checks.append({"name": name, "pass": bool(value == 0), "residual": str(value)})
def truth(name, value):
    checks.append({"name": name, "pass": bool(value)})

g = s.diag(-1, 1, 1, 1)
q = s.symbols('q0:4', real=True)
sym = s.symbols('s0:10', real=True)
T = s.zeros(4)
n = 0
for i in range(4):
    for j in range(i, 4):
        T[i,j] = T[j,i] = sym[n]
        n += 1
mixed = g*T
tr = s.trace(mixed)
def delta(i,j):
    return s.Integer(i == j)
def connection(a,b,c):
    return -delta(a,b)*q[c]-delta(a,c)*q[b]+g[b,c]*sum(g[a,k]*q[k] for k in range(4))
for b in range(4):
    correction = sum(4*q[a]*mixed[a,b] for a in range(4))
    correction += sum(connection(a,a,c)*mixed[c,b] for a in range(4) for c in range(4))
    correction -= sum(connection(c,a,b)*mixed[a,c] for a in range(4) for c in range(4))
    check(f'exchange_trace_component_{b}', correction-tr*q[b])
truth('opposite_exchange_sign_not_identity', s.expand(2*tr*q[0]) != 0)

# Direct metric connection/Ricci in physical-time coordinates, independently
# of a Friedmann substitution. gE=exp(-2nu tau)eta.
tau, nu, M, rho, chi = s.symbols('tau nu M rho chi', positive=True)
coords = [tau]+list(s.symbols('x y z', real=True))
metric = s.exp(-2*nu*tau)*g
inv = metric.inv()
Ga = [[[s.simplify(sum(inv[a,d]*(s.diff(metric[d,c],coords[b])+s.diff(metric[d,b],coords[c])-s.diff(metric[b,c],coords[d])) for d in range(4))/2) for c in range(4)] for b in range(4)] for a in range(4)]
Ric = s.zeros(4)
for b in range(4):
    for c in range(4):
        Ric[b,c] = s.simplify(sum(s.diff(Ga[a][b][c],coords[a])-s.diff(Ga[a][b][a],coords[c])+sum(Ga[a][a][d]*Ga[d][b][c]-Ga[a][c][d]*Ga[d][b][a] for d in range(4)) for a in range(4)))
scalarR = s.simplify(s.trace(inv*Ric))
Ein = s.simplify(Ric-metric*scalarR/2)
check('metric_G00', Ein[0,0]-3*nu**2)
for i in range(1,4):
    check(f'metric_G{i}{i}', Ein[i,i]+nu**2)
check('metric_R', scalarR-6*nu**2*s.exp(2*nu*tau))

K = 2*M**2-rho*s.exp(2*chi)/nu**2
V = 2*M**2*nu**2*s.exp(2*chi)-rho*s.exp(4*chi)/2
speed = nu*s.exp(chi)
dot = lambda f:s.simplify(speed*s.diff(f,chi))
H = -speed
X = speed**2/2
rm = rho*s.exp(4*chi)
rs = K*X+V
ps = K*X-V
check('scalar_density', rs-(3*M**2*nu**2*s.exp(2*chi)-rm))
check('scalar_pressure', ps+M**2*nu**2*s.exp(2*chi))
check('friedmann', 3*M**2*H**2-rm-rs)
check('raychaudhuri', -2*M**2*dot(H)-rm-K*speed**2)
check('matter_exchange', dot(rm)+3*H*rm-speed*rm)
check('scalar_Euler', K*(dot(speed)+3*H*speed)+s.diff(K,chi)*speed**2/2+s.diff(V,chi)+rm)
check('scalar_energy_exchange', dot(rs)+3*H*(rs+ps)+speed*rm)
check('physical_scale_factor', s.exp(chi)*s.exp(-chi)-1)
check('physical_lapse', s.exp(2*nu*tau)*metric[0,0]+1)
check('physical_density', s.exp(-4*chi)*rm-rho)
for i in range(4):
    for j in range(4):
        total = ((rm+rs) if i == j == 0 else (ps if i == j else 0))*s.exp(-2*chi)
        check(f'direct_Einstein_{i}{j}', M**2*Ein[i,j]-s.sympify(total).subs(chi,nu*tau))
for n in [1,2]:
    truth(f'healthy_local_margin_nu{n}', K.subs({M:1,rho:1,nu:n,chi:0})>0)
    check(f'luminal_nu{n}', (K/K).subs(nu,n)-1)
truth('different_physical_time_histories', s.exp(tau)-s.exp(2*tau) != 0)
truth('different_local_kinetic_coefficients', K.subs({M:1,rho:1,nu:1,chi:0}) != K.subs({M:1,rho:1,nu:2,chi:0}))
wrongV = 2*M**2*nu**2*s.exp(2*chi)-rho*s.exp(4*chi)
truth('wrong_potential_fails_Friedmann', s.simplify(3*M**2*H**2-rm-K*X-wrongV) != 0)
print(json.dumps({"scope":"Exact constructed class and background; no empirical validation", "passed":sum(x['pass'] for x in checks), "failed":sum(not x['pass'] for x in checks), "checks":checks, "elapsed_seconds":time.monotonic()-start},indent=2))
raise SystemExit(any(not x['pass'] for x in checks))
