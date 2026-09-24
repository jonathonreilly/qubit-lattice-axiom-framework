
AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('scripts/limit_controls.py', 'scripts/mobile_ring_cube_operators_20260924.py', 'scripts/ring_survival_repaired.py')
from pathlib import Path
import ast,cmath,json,math
import numpy as np
from scipy.linalg import solve_continuous_lyapunov
from mobile_ring_cube_operators_20260924 import ring_operators,first_outputs
D=Path(__file__).resolve().parent
# Import only the local already executed formula definitions; do not rerun
# the source's top-level output writes.
p=D/'ring_survival_repaired.py';ns={'cmath':cmath,'math':math}
tree=ast.parse(p.read_text())
exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,ast.FunctionDef)],type_ignores=[]),str(p),'exec'),ns)
formula=ns['formula']
means=[]
for theta in (.193,.631,1.19):
    basis,H2,H4,G,_,_=ring_operators(4,theta)
    for eta in (1.,13.,71.):
        delta=.7;kappa=.9
        K=-1j*(eta*H2+delta*H4)-kappa*G/2
        X=solve_continuous_lyapunov(K.conj().T,-np.eye(len(basis)))
        residual=float(np.max(abs(K.conj().T@X+X@K+np.eye(len(basis)))))
        assert residual<3e-10
        for coherent,a in zip((False,True),first_outputs(4,basis)):
            value=float(np.vdot(a,X@a).real)
            assert abs(value-3/(8*kappa))<3e-10
            means.append({'theta':theta,'eta':eta,'coherent':coherent,'mean':value,
                          'formula':3/(8*kappa),'Lyapunov_residual':residual})

packets=[]
t=.8;delta=.7;kappa=.9
for eta in (40.,160.,640.):
    # An actual normalized L2 angle packet: g_eta is constant on
    # [-eta^-2,eta^-2], zero elsewhere. Each midpoint has equal mass.
    width=eta**-2
    theta=width*(2*(np.arange(401)+.5)/401-1)
    for coherent in (False,True):
        survival=float(np.mean([formula(x,eta,delta,kappa,t,coherent) for x in theta]))
        w=7/12 if coherent else 13/24
        exceptional=w*math.exp(-4*kappa*t)+(1-w)*math.exp(-2*kappa*t)
        fixed=.5*math.exp(-4*kappa*t)+.5*math.exp(-2*kappa*t)
        packets.append({'eta':eta,'packet_halfwidth':width,'coherent':coherent,
                        'time':t,'quadrature_survival':survival,
                        'exceptional_limit':exceptional,'fixed_input_limit':fixed})

out={'complete_matrix_mean_controls':means,'shrinking_normalizable_packet_controls':packets,
     'scope':'Mean controls use the complete independent 36-dimensional generator; packet quadrature corroborates the analytic countercontrol to uniformity over eta-dependent initial states.'}
(D/'LIMIT_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
