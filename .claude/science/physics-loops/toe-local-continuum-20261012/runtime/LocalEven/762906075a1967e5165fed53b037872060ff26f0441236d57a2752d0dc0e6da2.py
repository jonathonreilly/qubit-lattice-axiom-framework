#!/usr/bin/env python3
"""Polynomial integration versus lattice differences; exact-symbol spectral probes."""
import argparse, numpy as np
from fixtures import FIELDS, load_candidate, cell_coefficients, row, finish

def integrate_cells_gl(field,n,a,derivative=0):
    x,w=np.polynomial.legendre.leggauss(24)
    lo=np.maximum(a*n,field.support[0]); hi=np.minimum(a*(n+1),field.support[1])
    width=np.maximum(hi-lo,0)
    points=(lo+hi)[:,None]/2+width[:,None]*x[None,:]/2
    return width[:,None]/2*np.einsum('j,njk->nk',w,field.value(points,derivative))

def spectral_data(c,field,L,Nref,t,projector=False):
    k=np.rint(np.fft.fftfreq(Nref)*Nref).astype(int)
    q=2*np.pi*k/L
    b=np.sqrt(2*np.pi)/L*field.fourier(q)
    D=c.continuum_symbol(q,.8,1.3)
    M=c.positive(D) if projector else c.unitary(D,t)
    return k,q,np.einsum('nij,nj->ni',M,b)

def average_series(k,q,b,Nlat,L):
    a=L/Nlat
    weighted=b*(np.exp(1j*q*(-L/2+a/2))*np.sinc(q*a/(2*np.pi)))[:,None]
    aliased=np.zeros((Nlat,2),complex)
    np.add.at(aliased,k%Nlat,weighted)
    return np.sqrt(a)*Nlat*np.fft.ifft(aliased,axis=0)

def main():
    p=argparse.ArgumentParser(); p.add_argument('candidate');p.add_argument('output');p.add_argument('--mode',choices=['cells','spectral'],required=True);args=p.parse_args()
    c=load_candidate(args.candidate);rows=[];measurements=[]
    m,v=.8,1.3
    if args.mode=='cells':
        for fi,f in enumerate(FIELDS):
            norms=[f.norm(j) for j in range(3)]
            for a in [.4,.2,.1,.05,.025]:
                n=np.arange(int(np.floor(f.support[0]/a))-3,int(np.ceil(f.support[1]/a))+3)
                cf=cell_coefficients(c,f,n,a)
                ref=integrate_cells_gl(f,n,a)
                rows.append(row(f'cell_primitive_f{fi}_a{a}',np.linalg.norm(f.integral(a*n,a*(n+1))-ref),0))
                rows.append(row(f'contraction_f{fi}_a{a}',np.linalg.norm(cf),norms[0]))
                # Literal L6 interpolation is independently normalized by 1/sqrt(a).
                step_norm=np.sqrt(a*np.sum(np.abs(cf/np.sqrt(a))**2))
                rows.append(row(f'isometry_f{fi}_a{a}',abs(step_norm-np.linalg.norm(cf)),0))
                constant_cell=np.sqrt(a)*np.array([.37,-.82])
                back=c.cell_factor(a)*a*(constant_cell/np.sqrt(a))
                rows.append(row(f'cell_right_inverse_f{fi}_a{a}',np.linalg.norm(back-constant_cell),0))
                g,J=c.couplings(a,m,v)
                lhs=(c.open_kernel(len(n),g,J)@cf.reshape(-1)).reshape(-1,2)
                df=integrate_cells_gl(f,n,a,1)
                rhs=c.cell_factor(a)*c.continuum_position(ref,df,m,v)
                error=np.linalg.norm(lhs-rhs)
                delta=a/2*(m*norms[1]+v*norms[2])
                rows.append(row(f'consistency_f{fi}_a{a}',error,delta))
                measurements.append({'field':fi,'a':a,'norms':norms,'cell_norm':float(np.linalg.norm(cf)),'consistency_error':float(error),'delta':delta,'ratio':float(error/delta)})
    else:
        L=32.; spectral=[]
        for fi,f in enumerate(FIELDS[:2]):
            norm,norm1,norm2=[f.norm(j) for j in range(3)]
            for t in [-.37,.43]:
                prior={}
                for Nref in [8192,16384]:
                    k,q,b=spectral_data(c,f,L,Nref,t)
                    x=-L/2+L*np.arange(Nref)/Nref
                    values=Nref*np.fft.ifft(b*np.exp(-1j*q*L/2)[:,None],axis=0)
                    outside=(x < f.support[0]-v*abs(t)) | (x > f.support[1]+v*abs(t))
                    outside_norm=float(np.sqrt(L/Nref*np.sum(np.abs(values[outside])**2)))
                    series_norm=float(np.sqrt(L*np.sum(np.abs(b)**2)))
                    rows.append(row(f'continuum_norm_f{fi}_t{t}_N{Nref}',abs(series_norm-norm),0,2e-8))
                    rows.append(row(f'causal_exterior_f{fi}_t{t}_N{Nref}',outside_norm,0,2e-8))
                    for a in [.4,.2,.1,.05,.025]:
                        Nlat=round(L/a); n=np.arange(-Nlat//2,Nlat//2)
                        cf=cell_coefficients(c,f,n,a)
                        qa=2*np.pi*np.fft.fftfreq(Nlat,d=a)
                        Da=c.discrete_symbol(qa,a,m,v)
                        ua=np.fft.ifft(np.einsum('nij,nj->ni',c.unitary(Da,t),np.fft.fft(cf,axis=0)),axis=0)
                        continuum_cells=average_series(k,q,b,Nlat,L)
                        delta=a/2*(m*norm1+v*norm2)
                        eps=a*norm1+abs(t)*delta
                        norm_error_squared=np.linalg.norm(ua)**2+norm**2-2*np.vdot(ua,continuum_cells).real
                        error=float(np.sqrt(max(0,norm_error_squared)))
                        rows.append(row(f'dynamics_f{fi}_t{t}_a{a}_N{Nref}',error,eps,2e-8))
                        cell_error=float(np.linalg.norm(ua-continuum_cells))
                        rows.append(row(f'duhamel_f{fi}_t{t}_a{a}_N{Nref}',cell_error,abs(t)*delta,2e-8))
                        if a in prior:
                            rows.append(row(f'reference_refinement_f{fi}_t{t}_a{a}',np.linalg.norm(continuum_cells-prior[a]),0,2e-8))
                        prior[a]=continuum_cells
                        spectral.append({'field':fi,'time':t,'a':a,'Nref':Nref,'embedded_error':error,'bound':eps,'cell_error':cell_error,'duhamel_bound':abs(t)*delta,'series_norm':series_norm,'outside_norm':outside_norm})
        # The same resolvent proof also applies on this periodic circle; this is
        # a periodic diagnostic and is not relabeled an infinite-line projector.
        for fi,f in enumerate(FIELDS[:2]):
            k,q,b=spectral_data(c,f,L,16384,0,projector=True)
            for a in [.4,.2,.1,.05,.025]:
                Nlat=round(L/a);n=np.arange(-Nlat//2,Nlat//2)
                cf=cell_coefficients(c,f,n,a)
                qa=2*np.pi*np.fft.fftfreq(Nlat,d=a)
                pc=np.fft.ifft(np.einsum('nij,nj->ni',c.positive(c.discrete_symbol(qa,a,m,v)),np.fft.fft(cf,axis=0)),axis=0)
                cp=average_series(k,q,b,Nlat,L)
                bound=a/2*(m*f.norm(1)+v*f.norm(2))/(2*m)
                error=float(np.linalg.norm(pc-cp))
                rows.append(row(f'periodic_projector_f{fi}_a{a}',error,bound,2e-8))
                measurements.append({'field':fi,'a':a,'projector_intertwining_error':error,'bound':bound,'circle_length':L})
        measurements.extend(spectral)
    finish({'mode':args.mode,'rows':rows,'measurements':measurements,'limits':'Floating diagnostics; spectral checks use a periodic box and finite Fourier cutoffs; exact line theorems are analytic.'},args.output)

if __name__=='__main__':main()
