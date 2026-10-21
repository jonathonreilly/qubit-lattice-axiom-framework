"""Explicit complete scalar E8 basis. No source Krylov construction."""
import sys,json
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parent))
from neutral_kink_core import band,bits,pairs,h

def basis(L,m,states):
 lookup={x:i for i,x in enumerate(states)};powers=[8**j for j in range(L)];q=2*np.pi*m/L;cols=[];labels=[];zeros=[]
 for kind in ['edge','diagonal']:
  for ell in range(1,L//2+1):
   if kind=='diagonal' and ell%2:continue
   vec=np.zeros(len(states),complex)
   for a,b in pairs:
    if (abs(h[b,a])>0)!=(kind=='edge'):continue
    for a,b in [(a,b),(b,a)]:
     amp=h[b,a]**ell if kind=='edge' else 1
     for start in range(L):
      ds=[a]*L
      for j in range(ell):ds[(start+j)%L]=b
      st=sum(x*p for x,p in zip(ds,powers))
      vec[lookup[st]]+=amp*np.exp(1j*q*(start+(ell-1)/2))
   norm=np.linalg.norm(vec)
   if ell==L//2 and m%2:
    assert norm<2e-12,(L,m,kind,ell,norm);zeros.append([kind,ell]);continue
   assert norm>1
   cols.append(vec/norm);labels.append([kind,ell])
 return np.array(cols).T,labels,zeros

def symmetry_maps(L,states):
 lookup={x:i for i,x in enumerate(states)};powers=[8**j for j in range(L)]
 square=[];reflection=[];sign=[]
 for b in range(8):
  bs=[(b>>(2-j))&1 for j in range(3)];bs+=[sum(bs)%2];new=[0]*4
  for x in range(2):
   for y in range(2):new[2*y+1-x]=bs[2*x+y]
  square.append(sum(new[j]<<(2-j) for j in range(3)))
  reflection.append((bs[2]<<2)|(bs[3]<<1)|bs[0]);sign.append(-1 if sum(bs) in (0,4) else 1)
 maps=[]
 for gen in range(6):
  dest=[];ph=[]
  for st in states:
   ds=[st//p%8 for p in powers];sg=1
   if gen==0:new=[x^6 for x in ds]
   elif gen==1:new=[x^1 for x in ds]
   elif gen==2:new=[x^5 for x in ds];sg=(-1)**sum(1+(x&5).bit_count() for x in ds)
   elif gen==3:new=[square[x] for x in ds];sg=int(np.prod([sign[x] for x in ds]))
   elif gen==4:new=[reflection[x] for x in ds]
   else:new=ds[1:]+ds[:1]
   dest.append(lookup[sum(x*p for x,p in zip(new,powers))]);ph.append(sg)
  maps.append((np.array(dest),np.array(ph)))
 return maps

def run():
 rows=[]
 for L in [4,6,8,10,12,16]:
  H1,H2,H3,states,source=band(L,third=True)
  maps=symmetry_maps(L,states)
  for m in range(L):
   U,labels,zeros=basis(L,m,states)
   expected=L//2-m%2+L//4-int(L%4==0 and m%2==1)
   assert U.shape[1]==expected
   gram=np.max(abs(U.conj().T@U-np.eye(expected)))
   mats=[U.conj().T@(H@U) for H in [H1,H2,H3]]
   leak=[np.linalg.norm(H@U-U@M) for H,M in zip([H1,H2,H3],mats)]
   assert max(leak+[gram])<2e-11,(L,m,leak,gram)
   symerr=[]
   for gen,(dst,ph) in enumerate(maps):
    transformed=np.zeros_like(U);transformed[dst]=ph[:,None]*U
    phase=np.exp(2j*np.pi*m/L) if gen==5 else 1
    symerr.append(float(np.linalg.norm(transformed-phase*U)))
   assert max(symerr)<2e-11,(L,m,symerr)
   nb=sum(x[0]=='edge' for x in labels);A=np.zeros((expected,expected));t=2*np.cos(np.pi*m/L)
   for j in range(nb-1):A[j,j+1]=A[j+1,j]=t*(np.sqrt(2) if labels[j+1][1]==L//2 else 1)
   e1=np.max(abs(mats[0]-A));assert e1<2e-12,(L,m,e1)
   rows.append(dict(L=L,m=m,dimension=expected,orthogonality_error=float(gram),closure_errors=[float(x) for x in leak],K1_formula_error=float(e1),terminal_exclusions=zeros,symmetry_errors=symerr))
  print(L,'passed all momenta',flush=True)
 return rows
if __name__=='__main__':
 rows=run();Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2))
