"""Finite local checks for integer-wall normal form, not a uniform proof by numerics."""
from pathlib import Path
import json,numpy as np
from neutral_rung_model import h,Ds,kron
from neutral_kink_core import band
I=np.eye(8)
z=np.array([np.diag(d) for d in Ds]).T
colors=np.array([[i//64,(i//8)%8,i%8] for i in range(512)])
N=sum((4-np.sum(z[colors[:,j]]*z[colors[:,(j+1)%3]],axis=1))/4 for j in range(3))
V=kron(h,I,I)+kron(I,h,I)+kron(I,I,h)
delta=N[:,None]-N[None,:];mask=delta!=0
S=np.divide(V,4*delta,out=np.zeros_like(V),where=mask)
P=lambda A:np.where(mask,0,A)
D1=P(V);D2=P(S@V-V@S)/2
cancel=np.max(np.abs(S*(4*N[None,:]-4*N[:,None])+V-D1))
H1,H2,states,source=band(3)
# Native band encoding uses little-endian base8, but all-rung sum is reversal invariant.
err=np.max(np.abs(D2[np.ix_(states,states)]+1.5*np.eye(len(states))-H2.toarray()))
assert cancel<1e-14 and err<1e-14
# A single central term uses only the two touching bonds, no periodic outer bond needed.
Nc=sum((4-np.sum(z[colors[:,j]]*z[colors[:,j+1]],axis=1))/4 for j in range(2))
Vc=kron(I,h,I);dc=Nc[:,None]-Nc[None,:]
Sc=np.divide(Vc,4*dc,out=np.zeros_like(Vc),where=dc!=0)
assert np.max(np.abs(Sc+Sc.T))<1e-14
# Filter the local second-order commutator term; it separately conserves global N.
dc2=np.where(dc==0,(Sc@Vc-Vc@Sc)/2,0)
uniform=[i for i,c in enumerate(colors) if c[0]==c[1]==c[2]]
vals=np.diag(dc2)[uniform]
assert np.ptp(vals)<1e-14
ann=np.max(np.abs((dc2-vals[0]*np.eye(512))[:,uniform]))
assert ann<1e-14
out=dict(cancellation_error=float(cancel),K2_match_error=float(err),central_generator_norm=float(np.linalg.norm(Sc,2)),central_vacuum_constant=float(vals[0]),uniform_annihilation_error=float(ann),scope='Finite algebra checks; no native pole, state selection or uniform remainder inferred from finite matrices')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
