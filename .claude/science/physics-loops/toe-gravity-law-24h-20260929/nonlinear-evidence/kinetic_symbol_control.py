#!/usr/bin/env python3
"""Exact matrix-symbol controls; general proof is in KINETIC_PAIRING_ESCAPE.md."""
import json
import hashlib
from pathlib import Path
import sympy as s
from axial_cc import budget
HERE=Path(__file__).resolve().parent

def main():
    budget();z=s.symbols('z',nonzero=True);I=s.eye(2);J=s.Matrix([[0,1],[-1,0]])
    sharp=lambda M:M.subs(z,1/z).T
    clean=lambda M:M.applyfunc(s.cancel)
    b=z+1/z-2;d=(z-1/z)/2
    E=s.Matrix([[1,b],[0,1]]);F=clean(E*sharp(E));Finv=clean(F.inv())
    Q=d*I+b*J;D=clean(Q*Finv)
    A=clean(z*F.diff(z)/2+s.Matrix([[b,1],[1,-b]]))
    assert clean(F-sharp(F))==s.zeros(2)
    assert clean(D*F+F*sharp(D))==s.zeros(2)
    assert clean(A-sharp(A)-z*F.diff(z))==s.zeros(2)
    assert clean(D.subs(z,1))==s.zeros(2)
    assert clean(D.diff(z).subs(z,1))==I
    # B=XF+A; moving X right gives the displayed affine residual.
    residual=clean(z*D.diff(z)*F+D*A+A*sharp(D)-F)
    reduced=clean(residual*Finv)
    expected=clean(z*D.diff(z)+D*A*Finv-A*Finv*D-I)
    assert clean(reduced-expected)==s.zeros(2)
    trace=s.cancel(s.trace(reduced));trace_expected=s.cancel(z*s.diff(s.trace(D),z)-2)
    assert s.cancel(trace-trace_expected)==0
    const=s.expand(trace).coeff(z,0)
    assert const==-2
    eps=s.symbols('eps',nonnegative=True)
    scalarF=(1+eps*(2-z-1/z))*I;scalarD=d*I;scalarA=z*scalarF.diff(z)/2
    scalar_res=clean(z*scalarD.diff(z)*scalarF+scalarD*scalarA+scalarA*sharp(scalarD)-scalarF)
    assert clean(scalar_res-((z+1/z)/2-1)*scalarF)==s.zeros(2)
    assert clean(z*(s.log(z)*I).diff(z)-I)==s.zeros(2)
    out={'noncommuting_matrix_fixture':{'F':str(F),'D':str(D),'A':str(A),
        'uniform_residual_zero':True,'affine_reduction_identity':True,
        'trace_residual':str(trace),'constant_Laurent_coefficient':str(const)},
        'scalar_higher_gradient_fixture':{'residual':str(scalar_res),
        'unit_circle_factor':'cos(k)-1','small_k_leading':'-k^2/2'},
        'formal_logarithm_control':'Solves derivative condition on a branch; fails finite Laurent/single-valued locality hypothesis.',
        'zero_F_control':'Both original matrix equations become zero; invertible TT kinetic hypothesis is load-bearing.',
        'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'scope':'Exact algebra controls, not proof of TT reduction or full nonlinear closure.'}
    (HERE/'kinetic_symbol_results.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

if __name__=='__main__':main()
