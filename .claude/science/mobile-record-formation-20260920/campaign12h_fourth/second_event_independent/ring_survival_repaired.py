"""Independent exact block clock and complete-matrix time controls."""
from pathlib import Path
import cmath, json, math
import numpy as np
import sympy as sp
from scipy.linalg import expm, solve_continuous_lyapunov
from operators import ring_operators, first_outputs
D=Path(__file__).resolve().parent


def two_level(omega,kappa,t):
    w=cmath.sqrt(kappa*kappa-omega*omega)
    f=t if abs(w)<1e-13 else cmath.sinh(w*t)/w
    a=cmath.cosh(w*t)-kappa*f
    return math.exp(-2*kappa*t)*(abs(a)**2+omega*omega*abs(f)**2)


def formula(theta,eta,delta,kappa,t,coherent):
    answer=.5*math.exp(-4*kappa*t)
    for j in range(6):
        alpha=(4*theta+2*math.pi*j)/6
        b=(1+math.cos(theta-alpha))/6 if coherent else 1/6
        for sign in (-1,1):
            s2=max(0.,4+sign*4*math.cos(alpha/2))
            answer+=b*.25*two_level((eta-4*delta)*math.sqrt(s2),kappa,t)
    return answer


# Solve the exact two-state integrated no-event equation with symbolic input.
k,g=sp.symbols('k g',positive=True,real=True)
K=sp.Matrix([[-2*k,sp.I*g],[sp.I*g,0]])
mean=sp.Matrix([[1/(2*k),-sp.I/(2*g)],[sp.I/(2*g),1/(2*k)+k/g**2]])
assert sp.simplify(K.conjugate().T*mean+mean*K)==-sp.eye(2)

rows=[]
for theta in (0.,.217,math.pi/4,.901,math.pi/2):
    basis,H2,H4,G,_,_=ring_operators(4,theta)
    for eta in (2.8,7.,31.,157.):
        delta=.7;kappa=.9
        K0=-1j*(eta*H2+delta*H4)-kappa*G/2
        for t in (0.,.13,.81,2.1):
            U=expm(t*K0)
            for coherent,a in zip((False,True),first_outputs(4,basis)):
                observed=float(np.linalg.norm(U@a)**2)
                predicted=formula(theta,eta,delta,kappa,t,coherent)
                assert abs(observed-predicted)<2e-11,(theta,eta,t,coherent,observed,predicted)
                rows.append({'theta':theta,'eta':eta,'delta':delta,'kappa':kappa,
                             'time':t,'coherent_first_mark':coherent,
                             'complete_matrix_survival':observed,'block_formula':predicted,
                             'absolute_error':abs(observed-predicted)})

# Fixed normalizable angle densities, midpoint quadrature as numerical controls
# only. The proof of the limit is dominated convergence, not these grids.
quad=[]
angles=2*math.pi*(np.arange(4001)+.5)/4001
for field,density in [('one_flux',np.ones(len(angles))),
                      ('neighbor_flux_coherence',1+np.cos(angles))]:
    for eta in (20.,80.,320.):
        for coherent in (False,True):
            for t in (.2,1.):
                values=np.array([formula(x,eta,.7,.9,t,coherent) for x in angles])
                observed=float(np.mean(density*values))
                limiting=.5*math.exp(-3.6*t)+.5*math.exp(-1.8*t)
                quad.append({'initial_field':field,'eta':eta,'time':t,'coherent':coherent,
                             'quadrature_survival':observed,'limiting_survival':limiting,
                             'error':abs(observed-limiting)})

exception=[]
for theta in (0.,math.pi/2,math.pi,3*math.pi/2):
    for coherent in (False,True):
        b=(1+math.cos(theta))/6 if coherent else 1/6
        weight=.5+b/4
        exception.append({'theta':theta,'coherent':coherent,
                          'fast_limit_exp_minus_4k_t_weight':weight,
                          'fast_limit_exp_minus_2k_t_weight':1-weight})

out={'exact_two_level_mean_operator':str(mean),
     'exact_mean_from_lossy_initial_coordinate':'1/(2*kappa) for omega != 0; 1/(4*kappa) for omega = 0',
     'complete_matrix_controls':rows,'fixed_density_numerical_quadrature':quad,
     'exceptional_nonphysical_sharp_fibers':exception,
     'fixed_input_limit':'(exp(-4*kappa*t)+exp(-2*kappa*t))/2',
     'scope':'The numerical quadratures are controls only; exceptional sharp fibers are not normalizable rotor states. No author source read.'}
(D/'RING_SURVIVAL_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
