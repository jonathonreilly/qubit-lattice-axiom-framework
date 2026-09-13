#!/usr/bin/env python3
"""Literal-edge and finite-Fock checks of the analytical transport argument."""
from __future__ import annotations
AUDIT_TIMEOUT_SEC = 180
import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[key]="1"
import hashlib
import itertools
import json
from pathlib import Path
import time
import numpy as np
from scipy.linalg import expm
from scipy.special import gammainc
import sympy as s

HERE=Path(__file__).resolve().parents[1]


def run():
    start=time.monotonic();checks=[]
    def close(name,a,b,tol=3e-12):
        err=float(np.max(np.abs(np.asarray(a)-np.asarray(b))))
        assert err<tol,(name,err)
        checks.append({"name":name,"max_residual":err})
    def exact(name,expr):
        assert s.simplify(expr)==0,(name,expr)
        checks.append({"name":name,"exact":True})

    kx,ky,kz=s.symbols('kx ky kz',real=True)
    h0=s.Matrix([[2*s.cos(kx)+2*s.cos(kz),1+s.exp(-2*s.I*ky)],
                 [1+s.exp(2*s.I*ky),2*s.cos(kz)]])
    phase=s.diag(1,s.exp(s.I*ky));internal=s.diag(0,1)
    h=s.Matrix([[2*s.cos(kx)+2*s.cos(kz),2*s.cos(ky)],
                [2*s.cos(ky),2*s.cos(kz)]])
    for i,j in itertools.product(range(2),repeat=2):
        exact(f"physical_Bloch_phase_{i}{j}",(phase.conjugate().T*h0*phase-h)[i,j].rewrite(s.exp))
        physical_y=h0.diff(ky)+s.I*(h0*internal-internal*h0)
        exact(f"physical_y_current_{i}{j}",(phase.conjugate().T*physical_y*phase-h.diff(ky))[i,j].rewrite(s.exp))
    wrong=phase.conjugate().T*h0.diff(ky)*phase-h.diff(ky)
    assert s.simplify(wrong[0,1].subs(ky,s.pi/4))!=0
    checks.append({"name":"omitted_internal_position_changes_current_operator","rejected":True})
    lam=s.symbols('lam')
    center=s.cos(kx)+2*s.cos(kz)
    exact("characteristic_polynomial",(h-lam*s.eye(2)).det()-((lam-center)**2-s.cos(kx)**2-4*s.cos(ky)**2))
    exact("patch_modes_per_vertex",(s.pi**3/54)/(4*s.pi**3)/2-s.Rational(1,432))

    # The current-window tolerance must preserve half the weakest x current.
    epsilon=s.Rational(1,8192);error_bound=2*epsilon
    half_bounds=(s.sqrt(3)/6912,s.Rational(1,3456),s.sqrt(3)/1728)
    assert all(s.simplify(bound**2-error_bound**2)>0 for bound in half_bounds)
    checks.append({"name":"exact_all_direction_half_current_margin","epsilon":str(epsilon)})
    old_error=2*s.Rational(1,6912)
    assert s.simplify(half_bounds[0]**2-old_error**2)<0
    checks.append({"name":"old_tolerance_fails_claimed_half_x_margin","rejected":True})

    # Full periodic hopping matrix from literal graph edges, no Bloch construction.
    shape=(6,8,6)
    points=list(itertools.product(*(range(n) for n in shape)))
    index={v:i for i,v in enumerate(points)};M=len(points)
    matrix=np.zeros((M,M),complex)
    currents=[np.zeros_like(matrix) for _ in range(3)]
    for v,i in index.items():
        for axis in range(3):
            if axis==0 and v[1]%2:continue
            w=list(v);w[axis]=(w[axis]+1)%shape[axis];j=index[tuple(w)]
            matrix[i,j]+=1;matrix[j,i]+=1
            currents[axis][i,j]+=1j;currents[axis][j,i]-=1j
    momenta=itertools.product(2*np.pi*np.arange(shape[0])/shape[0],
                             2*np.pi*np.arange(shape[1]//2)/shape[1],
                             2*np.pi*np.arange(shape[2])/shape[2])
    expected=[];C=np.eye(M,dtype=complex)/4
    for x,y,z in momenta:
        hh=np.array([[2*np.cos(x)+2*np.cos(z),2*np.cos(y)],
                     [2*np.cos(y),2*np.cos(z)]])
        values,vectors=np.linalg.eigh(hh);expected.extend(values)
        for band in range(2):
            vector=np.array([np.exp(1j*(x*v[0]+y*v[1]+z*v[2]))*vectors[v[1]%2,band]
                             for v in points])/np.sqrt(M/2)
            close(f"literal_mode_{len(expected)}_{band}",matrix@vector,values[band]*vector)
            if band==1 and np.pi/3-1e-12<=x<=2*np.pi/3+1e-12 and np.pi/6-1e-12<=y<=np.pi/3+1e-12 and np.pi/3-1e-12<=z<=2*np.pi/3+1e-12:
                C+=.5*np.outer(vector,vector.conj())
                D=np.sqrt(np.cos(x)**2+4*np.cos(y)**2)
                velocity=(-np.sin(x)*(1+np.cos(x)/D),-4*np.cos(y)*np.sin(y)/D,-2*np.sin(z))
                for axis in range(3):
                    close(f"literal_current_{x}_{y}_{z}_{axis}",np.vdot(vector,currents[axis]@vector),velocity[axis])
    close("entire_literal_spectrum",np.linalg.eigvalsh(matrix),np.sort(expected))
    close("stationary_finite_comparator",matrix@C,C@matrix)
    assert np.linalg.eigvalsh(C).min()>.25-1e-12
    assert np.linalg.eigvalsh(C).max()<.75+1e-12
    checks.append({"name":"comparator_covariance_between_quarter_and_three_quarters","passed":True})

    # Full 64-state occupation sum gives even-parity covariance, not a Gaussian assumption.
    nu=np.array([.25,1/3,.4,.6,2/3,.75]);weights=[];masks=[]
    for mask in range(64):
        bits=np.array([(mask>>j)&1 for j in range(6)])
        weights.append(np.prod(np.where(bits,nu,1-nu)));masks.append(bits)
    weights=np.array(weights);masks=np.array(masks)
    allowed=masks.sum(axis=1)%2==0
    probability=weights[allowed].sum()
    actual=(weights[allowed,None]*masks[allowed]).sum(axis=0)/probability
    r=np.prod(1-2*nu)
    expected_even=nu-2*nu*(1-nu)*np.array([np.prod(np.delete(1-2*nu,j)) for j in range(6)])
    close("even_parity_probability",probability,(1+r)/2)
    close("explicit_even_covariance",actual,expected_even)
    assert np.max(np.abs(actual-nu))<=2**(-6)/(1-2**(-6))
    checks.append({"name":"even_parity_operator_bound","actual_error":float(np.max(np.abs(actual-nu)))})
    assert abs(np.dot(weights[allowed],masks[allowed,0])-actual[0])>.05
    checks.append({"name":"missing_parity_normalization_rejected","rejected":True})

    # An open 4x4x4 compression inside the literal periodic comparator.
    inside=[index[(x,y,z)] for x in range(1,5) for y in range(2,6) for z in range(1,5)]
    hf=matrix[np.ix_(inside,inside)];Cf=C[np.ix_(inside,inside)]
    v=index[(2,3,2)];w=index[(2,3,3)];iv=inside.index(v);iw=inside.index(w)
    for endpoint in (v,w):
        full=np.eye(M,dtype=complex)[:,endpoint]
        finite=np.eye(len(inside),dtype=complex)[:,inside.index(endpoint)]
        for n in range(2):
            embedded=np.zeros(M,complex);embedded[inside]=finite
            close(f"boundary_path_powers_{endpoint}_{n}",full,embedded)
            full=matrix@full;finite=hf@finite
        embedded=np.zeros(M,complex);embedded[inside]=finite
        assert np.max(np.abs(full-embedded))>=1
    checks.append({"name":"boundary_first_omitted_power_is_nonzero","rejected_shortcut":True})
    boundary_results=[]
    for duration in (.01,.02,.04):
        Uf=expm(-1j*duration*hf);evolved=Uf@Cf@Uf.conj().T
        a=6*duration;tail=np.exp(a)*gammainc(2,a)
        actual_error=abs(evolved[iv,iw]-C[v,w])
        assert actual_error<=4*tail
        boundary_results.append({"duration":duration,"actual_covariance_error":float(actual_error),"derived_bound":float(4*tail)})
    checks.append({"name":"finite_boundary_evolution_bound","results":boundary_results})
    for a,d in ((.24,2),(1.,6),(10.,55)):
        tail=np.exp(a)*gammainc(d,a)
        assert tail<=2*(np.e*a/d)**d
    checks.append({"name":"factorial_tail_bound","passed":True})
    return {"status":"passed","count":len(checks),"checks":checks,"seconds":time.monotonic()-start,
            "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "note_sha256":hashlib.sha256((HERE/'docs/NATIVE_GROWING_FORMATION_CURRENT_BOUNDED_THEOREM_NOTE_2026-09-13.md').read_bytes()).hexdigest(),
            "scope":"same-author finite comparators; no numerical integral defines the transport theorem"}
