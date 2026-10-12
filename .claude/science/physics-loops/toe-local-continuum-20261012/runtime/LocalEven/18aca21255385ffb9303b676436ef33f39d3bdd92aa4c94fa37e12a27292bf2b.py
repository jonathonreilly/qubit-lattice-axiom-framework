#!/usr/bin/env python3
"""Whole-line Fourier integrals versus infinite lattice Brillouin-zone integrals."""
import argparse, numpy as np
from scipy.integrate import quad_vec
from fixtures import FIELDS, load_candidate, cell_coefficients, row, finish, complex_pair

def continuum_form(c,f,g,t,Q):
    def integrand(q):
        D=c.continuum_symbol(q,.8,1.3)
        return 2*np.vdot(f.fourier(q),c.positive(D)@c.unitary(D,t)@g.fourier(q))
    value,error=quad_vec(integrand,-Q,Q,epsabs=2e-11,epsrel=2e-11,limit=1500)
    tail=2*Q**(-4)*f.norm(2)*g.norm(2)
    return value,float(error),tail

def lattice_form(c,f,g,t,a,M):
    lo=int(np.floor(min(f.support[0],g.support[0])/a))-2
    hi=int(np.ceil(max(f.support[1],g.support[1])/a))+2
    n=np.arange(lo,hi)
    fs=cell_coefficients(c,f,n,a);gs=cell_coefficients(c,g,n,a)
    F=np.zeros((M,2),complex);G=np.zeros((M,2),complex)
    F[n%M]=fs;G[n%M]=gs
    F=np.fft.fft(F,axis=0);G=np.fft.fft(G,axis=0)
    q=2*np.pi*np.fft.fftfreq(M,d=a)
    D=c.discrete_symbol(q,a,.8,1.3)
    result=np.einsum('nij,njk,nk->ni',c.positive(D),c.unitary(D,t),G)
    return 2*np.sum(F.conj()*result)/M

def main():
    p=argparse.ArgumentParser();p.add_argument('candidate');p.add_argument('output');args=p.parse_args()
    c=load_candidate(args.candidate);rows=[];transforms=[];integrals=[];measurements=[]
    f,g=FIELDS[:2]
    for fi,field in enumerate([f,g]):
        for q in [-17.,-.3,0.,2.7,23.]:
            actual,error=quad_vec(lambda x:np.exp(-1j*q*x)*field.value(x)/np.sqrt(2*np.pi),*field.support,epsabs=2e-13,epsrel=2e-13)
            candidate=field.fourier(q)
            difference=float(np.linalg.norm(actual-candidate))
            rows.append(row(f'fourier_transform_f{fi}_q{q}',difference,0))
            transforms.append({'field':fi,'q':q,'difference':difference,'quadrature_estimate':float(error)})
    for t in [0.,.43]:
        results=[]
        for Q in [40.,80.,160.]:
            value,error,tail=continuum_form(c,f,g,t,Q)
            results.append((value,error,tail))
            integrals.append({'time':t,'cutoff':Q,'value':complex_pair(value),'quadrature_estimate':error,'analytic_tail_envelope':tail})
        for i in [1,2]:
            rows.append(row(f'continuum_cutoff_refinement_t{t}_i{i}',abs(results[i][0]-results[i-1][0]),results[i][2]+results[i-1][2],results[i][1]+results[i-1][1]))
        value,error,tail=results[-1]
        for a in [.4,.2,.1,.05,.025]:
            coarse=lattice_form(c,f,g,t,a,4096);fine=lattice_form(c,f,g,t,a,8192)
            mesh=float(abs(fine-coarse))
            rows.append(row(f'BZ_quadrature_refinement_t{t}_a{a}',mesh,0,2e-10))
            delta=a/2*(.8*g.norm(1)+1.3*g.norm(2))
            eta=a*g.norm(1)+delta/(2*.8)
            bound=2*f.norm()*(abs(t)*delta+eta)
            discrepancy=float(abs(fine-value))
            slack=tail+error+mesh+2e-10
            rows.append(row(f'two_point_bound_t{t}_a{a}',discrepancy,bound,slack))
            measurements.append({'time':t,'a':a,'lattice':complex_pair(fine),'continuum':complex_pair(value),'difference':discrepancy,'analytic_bound':bound,'BZ_mesh_difference':mesh,'continuum_tail_envelope':tail,'continuum_quadrature_estimate':error})
    finish({'rows':rows,'transform_checks':transforms,'continuum_integrals':integrals,'two_point_comparisons':measurements,'limits':'Adaptive and trapezoid quadrature are floating diagnostics, not certified intervals; the tail envelope is analytic.'},args.output)

if __name__=='__main__':main()
