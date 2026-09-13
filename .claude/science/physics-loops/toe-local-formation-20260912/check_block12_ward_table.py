#!/usr/bin/env python3
"""Literal AP native one-particle table and small Fock Ward-source checks."""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
import hashlib
import itertools
import json
from pathlib import Path
import time
import numpy as np
import sympy as s
from check_block12_soft_diagnostic import car

HERE=Path(__file__).resolve().parent


def run():
    started=time.monotonic();checks=[]
    def exact(name,a,b):
        z=a-b
        assert all(s.simplify(x)==0 for x in z) if isinstance(z,s.MatrixBase) else s.simplify(z)==0,name
        checks.append({'name':name,'exact':True})
    L=8;points=list(itertools.product(range(L),repeat=3));ix={v:i for i,v in enumerate(points)};M=L**3
    K=np.zeros((M,M))
    for r in points:
        for axis in range(3):
            q=list(r);q[axis]=(q[axis]+1)%L
            sign=(-1)**sum(r[:axis])*(-1 if r[axis]==L-1 else 1)
            K[ix[r],ix[tuple(q)]]=sign;K[ix[tuple(q)],ix[r]]=-sign
    spectrum,U=np.linalg.eigh(1j*K);absfreq=np.abs(spectrum)
    inverse_abs=(U*(1/absfreq))@U.conj().T
    covariance=(K@inverse_abs).real
    radial=lambda r:float(np.mean(absfreq**r))
    moment=lambda n:radial(2*n)
    a=np.eye(M)[:,0]
    fixtures={'P':((1,0,0),(0,1,0)),'O':((1,0,0),(L-1,0,0))}
    errors={}
    for kind,neighbors in fixtures.items():
        d=np.zeros(M)
        for v in neighbors:d[ix[v]]=-K[0,ix[v]]
        w=6*np.linalg.solve(K,d)
        bank={('w',0):w};avec=a;dvec=d
        for n in range(4):
            bank[('a',n)]=avec;bank[('d',n)]=dvec
            avec=K@avec;dvec=K@dvec
        D=lambda n:2*moment(n) if kind=='P' else moment(n+1)/3
        F=lambda r:2*radial(r) if kind=='P' else radial(r+2)/3
        def table(f,g):
            typ,i=f;other,j=g
            if typ=='w' and other=='w':return (72*radial(-2) if kind=='P' else 12),0
            if other=='w':
                dot,kap=table(g,f);return dot,-kap
            if typ=='w':
                if other=='a':
                    if j%2==0:return 2*(-1)**(j//2)*moment(j//2),0
                    return 0,-2*(-1)**((j-1)//2)*radial(j)
                if j%2:return -6*(-1)**((j-1)//2)*D((j-1)//2),0
                return 0,-6*(-1)**(j//2)*F(j-1)
            if typ=='d' and other=='a':
                dot,kap=table(g,f);return dot,-kap
            m=i+j
            if typ==other:
                if m%2==0:return (-1)**(i+m//2)*(moment(m//2) if typ=='a' else D(m//2)),0
                return 0,(-1)**(i+(m+1)//2)*(radial(m) if typ=='a' else F(m))
            if m%2:return (-1)**(i+(m+1)//2)*moment((m+1)//2)/3,0
            return 0,(-1)**(i+m//2+1)*radial(m+1)/3
        rel=0
        for f,g in itertools.product(bank,repeat=2):
            expected=table(f,g);actual=(bank[f]@bank[g],bank[f]@covariance@bank[g])
            rel=max(rel,max(abs(x-y)/(1+abs(y)) for x,y in zip(actual,expected)))
        assert rel<2e-11,(kind,rel)
        errors[kind]=rel
        checks.append({'name':f'literal_native_{kind}_full_source_table','entries':len(bank)**2,'max_scaled_residual':rel})
    # A separate paired-mode Fock construction tests the vacuum-only identity.
    f=car(3);vac=s.eye(8)[:,0];g=f[0]+f[0].T
    aa=s.Rational(2);bb=s.Rational(3);c=s.Rational(1,3);ss=s.sqrt(2)/3
    fieldA=lambda v:sum((v[j]*(f[j]+f[j].T) for j in range(3)),s.zeros(8))
    fieldB=lambda v:sum((s.I*v[j]*(f[j].T-f[j]) for j in range(3)),s.zeros(8))
    vv=s.Matrix([c,ss,0]);d=-aa*fieldB(vv)
    H=aa*f[0].T*f[0]+bb*(f[1].T*f[1]+f[2].T*f[2])
    W=fieldA(s.Matrix([2,6*aa*ss/bb,0]));J=2*s.I*d;D=H+s.I*g*d;R=-D.inv()
    kd=fieldA(s.Matrix([-aa**2*c,-aa*bb*ss,0]))
    exact('small_Fock_native_Ward',W*D-D*W,-J)
    exact('small_Fock_two_source_identity',R*J*R*vac,R*W*vac-W*R*vac)
    exact('anticommutator_on_original_vacuum',(D*J+J*D)*vac,-2*kd*vac)
    assert any(s.simplify(x)!=0 for x in D*J+J*D+2*kd)
    checks.append({'name':'false_full_operator_anticommutator_rejected','rejected':True})
    p=(s.Rational(3),s.Rational(-1),s.Rational(1,8))
    poly=p[0]*s.eye(8)+p[1]*D+p[2]*D**2
    vhat=(W*poly-poly*W)*vac
    exact('local_linear_polynomial_trial',vhat,(-p[1]*J+2*p[2]*kd)*vac)
    exact('Ward_source_norm',(vac.T*W*W*vac)[0],(W*W)[0,0])
    exact('Ward_first_source_moment',(vac.T*W*D*W*vac)[0],(W*W)[0,0]*(vac.T*(D-H)*vac)[0]+(vac.T*W*J*vac)[0])
    return {'status':'passed','count':len(checks),'checks':checks,'seconds':time.monotonic()-started,
            'scope':'finite AP table test and synthetic paired CAR identity; no infinite native alpha or gap inference',
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'helper_sha256':hashlib.sha256((HERE/'check_block12_soft_diagnostic.py').read_bytes()).hexdigest(),
            'note_sha256':hashlib.sha256((HERE/'BLOCK12_DERIVATION.md').read_bytes()).hexdigest()}


if __name__=='__main__':
    result=run();(HERE/'BLOCK12_WARD_TABLE_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
