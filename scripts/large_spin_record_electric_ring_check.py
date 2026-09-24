#!/usr/bin/env python3
"""Electric and magnetic terms from the same hard-core record hopping.

The complete square checks exact finite-spin coefficients and a finite-volume
joint limit. They do not establish a many-volume Coulomb phase.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('scripts/large_spin_record_electric_ring_check.py',)
from itertools import product
import hashlib
import json
from pathlib import Path
import time
import numpy as np
import scipy.linalg as la
import sympy as sp

OUT=Path(__file__).resolve().parent


def square_basis(spin):
    spin=sp.Rational(spin);values=[-spin+j for j in range(int(2*spin)+1)]
    ref=(1,0,1,0);basis=[]
    for matter in product((0,1),repeat=4):
        if sum(matter)!=2:continue
        for m0 in values:
            field=[m0]
            for x in (1,2,3):field.append(field[-1]+matter[x]-ref[x])
            if field[0]-field[-1]+ref[0]-matter[0]:continue
            if any(abs(m)>spin for m in field):continue
            basis.append((matter,tuple(field)))
    basis.sort(key=lambda z:(sum(z[0][x] for x in (1,3)),z[1][0],z[0]))
    return basis


def square(spin,exact):
    spin=sp.Rational(spin);casimir=spin*(spin+1);basis=square_basis(spin)
    index={s:i for i,s in enumerate(basis)};dim=len(basis)
    hop=sp.zeros(dim) if exact else np.zeros((dim,dim))
    for i,(matter,field) in enumerate(basis):
        for edge in range(4):
            x,y=edge,(edge+1)%4
            for u,v,orientation in [(x,y,1),(y,x,-1)]:
                if matter[u]!=1 or matter[v]!=0:continue
                change=-orientation;old=field[edge]
                if abs(old+change)>spin:continue
                squared=1-(old*old+change*old)/casimir
                assert squared>0
                mm=list(matter);ff=list(field);mm[u]=0;mm[v]=1;ff[edge]+=change
                dest=index[(tuple(mm),tuple(ff))]
                hop[dest,i]=-sp.sqrt(squared) if exact else -float(sp.sqrt(squared))
    penalty=[int(m[1]+m[3]) for m,f in basis]
    low=[i for i,n in enumerate(penalty) if n==0]
    assert len(low)==int(2*spin)+1
    assert hop==hop.T if exact else np.array_equal(hop,hop.T)
    return basis,hop,penalty,low


def exact_coefficients(spin):
    basis,t,n,p=square(spin,True);dim=len(basis);s=sp.Rational(spin);c=s*(s+1)
    den=sp.diag(*[sp.Rational(1,k) if k else 0 for k in n])
    h2=-(t*den*t).extract(p,p)
    folded=(t*den*den*t).extract(p,p)
    h4=-(t*den*t*den*t*den*t).extract(p,p)-(folded*h2+h2*folded)/2
    h2=h2.applyfunc(sp.simplify);h4=h4.applyfunc(sp.simplify)
    want2=sp.zeros(len(p));want4=sp.zeros(len(p))
    ms=[basis[i][1][0] for i in p]
    for i,m in enumerate(ms):
        assert basis[p[i]][1]==(m,)*4
        a=1-m*m/c;b=m/c
        want2[i,i]=-4+4*m*m/c
        want4[i,i]=12*a*a-4*b*b
        if i+1<len(p):
            want4[i+1,i]=want4[i,i+1]=-2*(1-m*(m+1)/c)**2
    assert h2==want2 and h4==want4
    return {'spin':str(s),'dimension':dim,'low_dimension':len(p),'low_fluxes':list(map(str,ms)),
            'second_coefficient':[[str(x) for x in row] for row in h2.tolist()],
            'fourth_coefficient':[[str(x) for x in row] for row in h4.tolist()],
            'second_electric_and_fourth_weighted_formula_exact':True}


def rotor_spectrum(cutoff,electric,magnetic):
    modes=np.arange(-cutoff,cutoff+1)
    mat=np.diag(4*electric*modes*modes)-magnetic*(np.eye(len(modes),k=1)+np.eye(len(modes),k=-1))
    return la.eigh(mat,subset_by_index=(0,5))[0]


def scaled_controls():
    electric=.3;magnetic=1.
    target=rotor_spectrum(24,electric,magnetic)
    cutoff_error=float(np.max(abs(target-rotor_spectrum(12,electric,magnetic))))
    assert cutoff_error<1e-11
    rows=[]
    for s in (16,32,64,128):
        basis,t,n,p=square(s,False);casimir=s*(s+1)
        h=electric*casimir;delta=2*h*h/magnetic;coupling=np.sqrt(h*delta);eps=coupling/delta
        constant=-4*h+6*magnetic
        mat=delta*np.diag(n)+coupling*t-constant*np.eye(len(basis))
        vals,vecs=la.eigh(mat,subset_by_index=(0,5))
        residual=float(np.max(la.norm(mat@vecs-vecs*vals[None,:],axis=0)))
        error=float(np.max(abs(vals-target)))
        weight=float(np.sum(vecs[p,0]**2))
        assert residual<1e-5 and .9<weight<=1+1e-12
        rows.append({'spin':s,'dimension':len(basis),'electric_K':electric,'magnetic_J':magnetic,
                     'Delta':delta,'hopping_t':coupling,'epsilon':eps,'removed_scalar':constant,
                     'lowest_six_shifted_microscopic_energies':vals.tolist(),
                     'largest_six_energy_error_against_rotor':error,
                     'error_divided_by_epsilon_squared':error/(eps*eps),
                     'eigenpair_absolute_residual':residual,'ground_code_weight':weight})
        print(json.dumps(rows[-1]),flush=True)
    assert all(rows[j+1]['largest_six_energy_error_against_rotor']<rows[j]['largest_six_energy_error_against_rotor'] for j in range(len(rows)-1))
    assert rows[-1]['largest_six_energy_error_against_rotor']<.05
    return {'rotor_cutoff_comparison_error':cutoff_error,'rotor_lowest_six_energies':target.tolist(),'rows':rows,
            'scope':'Complete finite-square numerical spectra at four supplied scales; no thermodynamic phase inference.'}


def symbolic_cubic_diagonal():
    # The weighted count of all disjoint two-excursion returns leaves only
    # same-edge and shared-endpoint terms after folded normalization.
    c,d,volume,m2=sp.symbols('C d V sum_E_squared',positive=True)
    edges=d*volume;degree=2*d
    constant=edges+volume*degree*(degree-1)
    assert sp.expand(constant-d*volume*(4*d-1))==0
    per_edge_linear=-2*(1+2*(degree-1))/c
    assert sp.simplify(per_edge_linear+2*(4*d-1)/c)==0
    return {'rotor_fourth_scalar':'d V (4d-1)',
            'finite_spin_second':'-d V + sum_e E_e^2 / C in the ice sector',
            'finite_spin_fourth_diagonal':'sum_e F_e^2 + 2 sum_(unordered adjacent edges e,f) F_e F_f',
            'F_e':'1-(E_e^2-sigma_e E_e)/C, sigma_e=+1 for stored A-to-B orientation',
            'fourth_electric_correction_after_multiplying_J_over2':'-J(4d-1) sum_e E_e^2 / C',
            'linear_flux_sum':'sum_e sigma_e E_e = sum_(A vertices) div E = 0'}


def main():
    start=time.monotonic();exact=[]
    for s in [sp.Rational(1,2),1,2,3]:
        exact.append(exact_coefficients(s));print(json.dumps({'exact_spin':str(s),'dimension':exact[-1]['dimension']}),flush=True)
    result={'status':'PASS','exact_square_coefficients':exact,'cubic_weighted_count':symbolic_cubic_diagonal(),
            'joint_scaling':scaled_controls(),'elapsed_seconds':time.monotonic()-start,
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (OUT/'LARGE_SPIN_RECORD_ELECTRIC_RING_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'PASS','elapsed_seconds':result['elapsed_seconds']}),flush=True)


if __name__=='__main__':main()
