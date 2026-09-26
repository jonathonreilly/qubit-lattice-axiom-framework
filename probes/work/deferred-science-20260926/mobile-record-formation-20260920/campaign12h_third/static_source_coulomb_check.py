"""Static-source electrostatics and flat-connection controls.
Author checks for a specified compact rotor target, not a mobile-matter proof.
"""
from pathlib import Path
from datetime import datetime, timezone
from itertools import product
import json
import hashlib
import math
import numpy as np
import sympy as sp
from scipy.linalg import eigh_tridiagonal
from scipy.integrate import quad
from scipy.special import ive

HERE=Path(__file__).resolve().parent

def cubic(length, separation):
    shape=(length,)*3;volume=length**3
    # Canonical positive-axis edges; div E(x)=sum(E(x,a)-E(x-ea,a)).
    rho=np.zeros(shape);rho[(0,0,0)]=1;rho[(separation,0,0)]=-1
    modes=[2*np.pi*np.fft.fftfreq(length) for _ in range(3)]
    k=np.meshgrid(*modes,indexing="ij")
    lam=sum(4*np.sin(x/2)**2 for x in k)
    inv=np.zeros(shape);np.divide(1.,lam,out=inv,where=lam>0)
    potential=np.fft.ifftn(np.fft.fftn(rho)*inv).real
    longitudinal=np.stack([potential-np.roll(potential,-1,axis=a) for a in range(3)],axis=-1)
    div=sum(longitudinal[...,a]-np.roll(longitudinal[...,a],1,axis=a) for a in range(3))
    assert np.max(abs(div-rho))<1e-12
    # Integer reference path, with one unit on every edge from positive to negative charge.
    integer=np.zeros(shape+(3,))
    integer[:separation,0,0,0]=1
    intdiv=sum(integer[...,a]-np.roll(integer[...,a],1,axis=a) for a in range(3))
    assert np.array_equal(intdiv,rho)
    totals=integer.sum(axis=(0,1,2))
    harmonic=np.broadcast_to(totals/volume,integer.shape).copy()
    transverse=integer-longitudinal-harmonic
    tdiv=sum(transverse[...,a]-np.roll(transverse[...,a],1,axis=a) for a in range(3))
    assert np.max(abs(tdiv))<1e-12
    assert np.max(abs(transverse.sum(axis=(0,1,2))))<1e-12
    norms=[float(np.sum(z*z)) for z in (longitudinal,harmonic,transverse)]
    crosses=[float(np.sum(a*b)) for a,b in [(longitudinal,harmonic),(longitudinal,transverse),(harmonic,transverse)]]
    assert max(map(abs,crosses))<1e-12
    assert abs(sum(norms)-np.sum(integer*integer))<1e-12
    green=np.fft.ifftn(inv).real
    formula=2*(green[0,0,0]-green[separation,0,0])
    assert abs(formula-norms[0])<1e-12
    assert abs(norms[1]-separation**2/volume)<1e-12
    # Adding one plaquette changes only the transverse component and preserves
    # the transverse energy's affine-lattice description.
    loop=np.zeros_like(integer)
    loop[0,0,0,0]+=1;loop[1,0,0,1]+=1
    loop[0,1,0,0]-=1;loop[0,0,0,1]-=1
    assert np.max(abs(sum(loop[...,a]-np.roll(loop[...,a],1,axis=a) for a in range(3))))==0
    assert np.max(abs(loop.sum(axis=(0,1,2))))==0
    changed=integer+loop
    predicted=norms[0]+norms[1]+float(np.sum((transverse+loop)**2))
    assert abs(float(np.sum(changed*changed))-predicted)<1e-12
    return {"period":length,"separation":separation,"vertices":volume,
       "charge_laplacian_residual":float(np.max(abs(div-rho))),
       "integer_reference_norm_squared":float(np.sum(integer*integer)),
       "longitudinal_norm_squared":norms[0],"harmonic_norm_squared":norms[1],
       "transverse_reference_norm_squared":norms[2],
       "pair_Green_formula":float(formula),"orthogonality_errors":crosses,
       "harmonic_total_flux":totals.tolist(),
       "harmonic_warning":"Nonzero source dipole prevents assuming zero harmonic electric component in this sector."}

def exact_square():
    # One oriented C4 with source +1 at vertex0, -1 at vertex2.
    B=sp.Matrix([[1,0,0,-1],[-1,1,0,0],[0,-1,1,0],[0,0,-1,1]])
    rho=sp.Matrix([1,0,-1,0]);eref=sp.Matrix([1,1,0,0])
    lap=B*B.T
    phi=(lap+sp.ones(4)/4).inv()*rho
    el=B.T*phi;cyc=sp.ones(4,1)
    alpha=(cyc.T*eref)[0]/4
    assert B*eref==rho and B*el==rho and (cyc.T*el)[0]==0
    assert eref==el+alpha*cyc
    n=sp.symbols("n",integer=True)
    energy=sp.expand(((eref+n*cyc).T*(eref+n*cyc))[0])
    assert sp.expand(energy-(el.dot(el)+4*(n+alpha)**2))==0
    return {"incidence":[list(map(str,row)) for row in B.tolist()],
            "source":list(map(str,rho)),"reference":list(map(str,eref)),
            "longitudinal":list(map(str,el)),"electric_offset":str(el.dot(el)),
            "flat_connection_alpha":str(alpha),"exact_energy":str(energy),
            "decomposition":"||E||^2=1+4(n+1/2)^2; neutral loop has 4n^2.",
            "scope":"Exact affine Gauss decomposition on one loop; not a cubic photon model."}

def twisted_pendulum():
    # H_alpha = (g^2/2)(n+alpha)^2 + (1/g^2)(1-cos A).
    # In scaled semiclassical units h=g^2, the barrier is 2(1-cos A).
    rows=[]
    for g in (1.2,1.,.85,.7,.6):
        gs=[]
        for cutoff in (32,48):
            n=np.arange(-cutoff,cutoff+1)
            values=[]
            for alpha in (0.,.25,.5):
                diag=.5*g*g*(n+alpha)**2+1/(g*g)
                off=np.full(len(n)-1,-.5/(g*g))
                ev,vec=eigh_tridiagonal(diag,off,select="i",select_range=(0,0))
                residual=np.linalg.norm(diag*vec[:,0]+np.r_[off*vec[1:,0],0]+np.r_[0,off*vec[:-1,0]]-ev[0]*vec[:,0])
                values.append((float(ev[0]),float(residual),float(vec[0,0]**2+vec[-1,0]**2)))
            gs.append(values)
        disagreement=max(abs(a[0]-b[0]) for a,b in zip(*gs))
        assert disagreement<5e-12
        spreads=[v[0]-gs[1][0][0] for v in gs[1]]
        assert min(spreads)>-5e-13
        rows.append({"g":g,"h":g*g,"ground_energies_at_alpha_0_quarter_half":[v[0] for v in gs[1]],
             "twist_energy_differences":spreads,"max_cutoff_disagreement":disagreement,
             "max_eigenpair_residual":max(v[1] for v in gs[1]),
             "max_endpoint_probability":max(v[2] for v in gs[1]),
             "leading_instanton_exponential_for_orientation_only":math.exp(-8/(g*g))})
    assert rows[-1]["twist_energy_differences"][-1]<rows[0]["twist_energy_differences"][-1]*1e-6
    return {"rows":rows,"scope":"Numerical fixed-box flat-connection sensitivity, not a certified exponential bound; the proof is analytic."}

def axis_green(n):
    # G(n,0,0)=integral_0^infinity exp(-6t) I_n(2t) I_0(2t)^2 dt.
    # t=s^2, s=u/(1-u) gives a smooth large-t tail on [0,1].
    def f(u):
        if u==1.:return 2/(4*math.pi)**1.5
        if u==0.:return 0.
        s=u/(1-u);t=s*s
        return 2*s/(1-u)**2*ive(n,2*t)*ive(0,2*t)**2
    value,error=quad(f,0,1,epsabs=1e-12,epsrel=1e-11,limit=400)
    assert np.isfinite(value) and error<1e-10
    return value,error

def greens():
    rows=[]
    for n in (0,1,2,4,8,16,32,64):
        value,error=axis_green(n)
        row={"axis_distance":n,"infinite_lattice_G":value,"quadrature_error_estimate":error}
        if n:
            row["four_pi_r_times_G"]=4*math.pi*n*value
            row["r_squared_relative_correction"]=n*n*(4*math.pi*n*value-1)
        rows.append(row)
    # Discrete Poisson at the source supplies an independent normalization.
    residual=6*(rows[0]["infinite_lattice_G"]-rows[1]["infinite_lattice_G"])-1
    assert abs(residual)<1e-10
    assert abs(rows[-1]["four_pi_r_times_G"]-1)<1e-3
    return {"rows":rows,"source_Poisson_normalization_residual":residual,
            "scope":"Quadrature with estimated errors; analytic Fourier proof establishes the asymptotic, not these samples."}

def main():
    b=Path(__file__).read_bytes()
    r={"created_utc":datetime.now(timezone.utc).isoformat(),
       "source":{"path":str(Path(__file__).resolve()),"bytes":len(b),"sha256":hashlib.sha256(b).hexdigest()},
       "cubic_affine_controls":[cubic(L,r) for L,r in [(6,1),(6,2),(8,3),(12,4)]],
       "exact_square":exact_square(),"twisted_pendulum":twisted_pendulum(),
       "lattice_Green_controls":greens(),
       "status":"Author static-source target-rotor controls passed; mobile charged-record matching not established."}
    (HERE/"STATIC_SOURCE_COULOMB_RESULTS.json").write_text(json.dumps(r,indent=2)+"\n")
    print(json.dumps(r,indent=2))
if __name__=="__main__":main()
