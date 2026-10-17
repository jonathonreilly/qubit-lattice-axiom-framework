#!/usr/bin/env python3
"""Exact finite algebra discriminator for nonorthogonal isometry errors.

This is not a scattering fit or a test of the infinite-time theorem.  It
checks why orthogonal input/output columns do not justify taking the maximum
individual error when the interaction mixes old-energy channels.
"""
from pathlib import Path
import hashlib
import json
import platform
import resource
import sys
import time

resource.setrlimit(resource.RLIMIT_CPU,(10,10))
import sympy as sp

start=time.monotonic()
I=sp.eye(2)
K=sp.diag(1,3)
P=sp.Matrix([[1,1],[1,1]])/2
z=sp.Rational(3,5)+sp.I*sp.Rational(4,5)
U=I+(z-1)*P
E=U-I
gram=sp.simplify(E.conjugate().T*E)
comm=K*P-P*K
assert sp.simplify(U.conjugate().T*U)==I
assert comm!=sp.zeros(2)
assert gram==sp.Matrix([[sp.Rational(2,5),sp.Rational(2,5)],
                        [sp.Rational(2,5),sp.Rational(2,5)]])
eig=gram.eigenvals()
assert eig=={sp.Integer(0):1,sp.Rational(4,5):1}
assert max(eig)>max(gram[0,0],gram[1,1])
assert max(eig)==gram.trace()
result={
    'scope':'Exact two-dimensional algebra only; no scattering or hardware certificate',
    'K':str(K),'projector':str(P),'chosen_unit_phase':str(z),
    'K_projector_commutator':str(comm),'U_is_unitary':True,
    'error_Gram':str(gram),
    'each_column_error_squared':str(gram[0,0]),
    'operator_error_squared':str(max(eig)),
    'naive_max_column_bound_rejected':bool(max(eig)>max(gram[0,0],gram[1,1])),
    'sum_of_column_squares_is_sharp':bool(max(eig)==gram.trace()),
    'runtime':{'executable':sys.executable,'python':sys.version,
               'sympy':sp.__version__,'platform':platform.platform(),
               'largest_matrix_dimension':2,'cpu_seconds_cap':10,
               'elapsed_seconds_after_import':time.monotonic()-start},
    'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
print(json.dumps(result,indent=2))
