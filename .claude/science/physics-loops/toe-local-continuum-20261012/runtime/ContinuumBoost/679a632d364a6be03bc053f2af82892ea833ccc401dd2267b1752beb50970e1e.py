#!/usr/bin/env python3
"""Exact finite algebra for the local continuum boost; no domain certification."""
import argparse
import itertools
import json
import platform
import sympy as sp

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--variant', choices=['baseline', 'wrong_spin', 'opposite_polarization'], default='baseline')
    args = ap.parse_args()
    I = sp.I
    eye = sp.eye(2)
    sx = sp.Matrix([[0,1],[1,0]])
    sy = sp.Matrix([[0,-I],[I,0]])
    sz = sp.diag(1,-1)
    z, m, v = sp.symbols('z m v', positive=True)
    k, energy = sp.symbols('k energy', real=True)
    ch = (z+1/z)/2
    sh = (z-1/z)/2
    c = sp.expand(ch**2+sh**2)
    s = sp.expand(2*ch*sh)
    spin_sign = 1 if args.variant == 'wrong_spin' else -1
    spin = ch*eye+spin_sign*sh*sx
    spin_inverse = ch*eye-spin_sign*sh*sx
    lorentz = sp.Matrix([[c,s/v],[v*s,c]])
    d = lambda q: -v*q*sx-m*sy
    q_new = k*c+energy*s/v
    energy_new = energy*c+v*k*s
    checks = []

    def zero(name, expression):
        matrix = expression if isinstance(expression, sp.MatrixBase) else sp.Matrix([[expression]])
        simplified = matrix.applyfunc(sp.simplify)
        passed = simplified == sp.zeros(*simplified.shape)
        checks.append({'name': name, 'pass': bool(passed), 'residual': [[str(x) for x in simplified.row(j)] for j in range(simplified.rows)]})

    zero('lorentz_determinant', lorentz.det()-1)
    zero('spin_inverse', spin*spin_inverse-eye)
    zero('pde_time_coefficient', spin*(c*eye+s*sx)-spin_inverse)
    zero('pde_space_coefficient', spin*(s*eye+c*sx)-spin_inverse*sx)
    zero('pde_complete_mass_cancellation', spin*(c*eye+s*sx)*sy-sy*spin)
    zero('flux_matrix', spin.T*spin-(c*eye-s*sx))
    zero('plane_wave_intertwiner', (d(q_new)-energy_new*eye)*spin-spin_inverse*(d(k)-energy*eye))
    zero('mass_shell_preservation', energy_new**2-v**2*q_new**2-(energy**2-v**2*k**2))

    theta = sp.symbols('theta', real=True)
    r = sp.diag(sp.exp(I*theta/2),sp.exp(-I*theta/2))
    eplus = sp.Matrix([1,-I])/sp.sqrt(2)
    eminus = sp.conjugate(eplus)
    uplus, uminus = r*eplus, r*eminus
    zero('parallel_positive_frame', (uplus.conjugate().T*sp.diff(uplus,theta))[0])
    zero('parallel_negative_frame', (uminus.conjugate().T*sp.diff(uminus,theta))[0])
    zero('frame_real_structure_reflects_momentum', uminus-sp.conjugate(uplus.subs(theta,-theta)))
    zero('frame_derivative_anticommutator', (-sy)*(r.conjugate().T*sp.diff(r,theta))+(r.conjugate().T*sp.diff(r,theta))*(-sy))
    q = sp.symbols('q', real=True)
    eq = sp.sqrt(m*m+v*v*q*q)
    rational = sp.Matrix([(-v*q+I*m)/eq,1])/sp.sqrt(2)
    zero('rational_eigenvector', d(q)*rational-eq*rational)
    zero('rational_berry_connection', (I*eq*rational.conjugate().T*sp.diff(rational,q))[0]+m*v/(2*eq))
    zero('real_conjugation_correct', sp.conjugate(d(-q))+d(q))
    wrong_real = (sp.conjugate(d(q))+d(q)).applyfunc(sp.simplify)

    n = 3
    gammas = []
    for site in range(n):
        for local in [sx,sy]:
            factors = [sz if j<site else (local if j==site else eye) for j in range(n)]
            gammas.append(sp.kronecker_product(*factors))
    identity = sp.eye(2**n)
    vacuum = sp.zeros(2**n,1)
    vacuum[0] = 1
    car = sp.zeros(2**n)
    for j, g in enumerate(gammas):
        for k2, h in enumerate(gammas):
            car += (g*h+h*g-(2*identity if j==k2 else sp.zeros(2**n))).applyfunc(lambda x: sp.conjugate(x)*x)
    zero('jordan_wigner_car', car)
    p0 = (eye-sy)/2
    if args.variant == 'opposite_polarization':
        p0 = eye-p0
    polarization = sp.diag(*([p0]*n))
    observed_covariance = sp.Matrix(2*n,2*n,lambda j,k2: (vacuum.T*gammas[j]*gammas[k2]*vacuum)[0])
    zero('vacuum_covariance_sign_and_factor', observed_covariance-2*polarization)
    zero('polarization_is_projection', polarization*polarization-polarization)
    zero('polarization_real_complement', polarization+sp.conjugate(polarization)-sp.eye(2*n))
    even_vectors, odd_vectors = [], []
    for length in range(2*n+1):
        for subset in itertools.combinations(range(2*n),length):
            vec = vacuum
            for j in reversed(subset):
                vec = gammas[j]*vec
            (even_vectors if length%2==0 else odd_vectors).append(vec)
    even_rank = sp.Matrix.hstack(*even_vectors).rank()
    odd_rank = sp.Matrix.hstack(*odd_vectors).rank()
    full_rank = sp.Matrix.hstack(*even_vectors,*odd_vectors).rank()
    checks.append({'name':'even_vacuum_sector_not_full_fock', 'pass':even_rank==4 and odd_rank==4 and full_rank==8,
                   'even_rank':even_rank,'odd_rank':odd_rank,'full_rank':full_rank})
    zero('disjoint_even_products_commute', (gammas[0]*gammas[1])*(gammas[4]*gammas[5])-(gammas[4]*gammas[5])*(gammas[0]*gammas[1]))
    result = {'variant':args.variant, 'python':platform.python_version(), 'sympy':sp.__version__,
              'scope':'Exact finite algebra only. No proof of infinite-dimensional domains or local-net closure.',
              'checks':checks,
              'real_structure_wrong_pointwise_conjugation_residual':[[str(x) for x in wrong_real.row(j)] for j in range(2)],
              'weak_survivors':[c['name'] for c in checks if c['pass']] if args.variant!='baseline' else [],
              'all_checks_passed':all(c['pass'] for c in checks)}
    print(json.dumps(result,indent=2))
    return 0 if result['all_checks_passed'] else 1

if __name__ == '__main__':
    raise SystemExit(main())
