from pathlib import Path
import gzip,json
import mpmath as mp
import sympy as s

HERE=Path(__file__).resolve().parent
PACK=HERE.parent.parent
source=gzip.decompress((HERE/'check_block05_fock.py.gz').read_bytes()).decode()
prefix=source.split('    results=[]')[0]
namespace={'__file__':str(PACK/'check_block05_fock.py')}
exec(compile(prefix+'    return ox,bonds,totaln\n',str(PACK/'check_block05_fock.py'),'exec'),namespace)
ox,bonds,totaln=namespace['run']()
sector=[i for i in range(64) if i.bit_count()==3]
la=next(iter(ox[0].free_symbols))
mp.mp.dps=45
def number(z):
    re,im=s.re(z),s.im(z)
    rn,rd=re.as_numer_denom()
    an,ad=im.as_numer_denom()
    return mp.mpc(mp.mpf(int(rn))/int(rd),mp.mpf(int(an))/int(ad))
def matrix(o):
    return mp.matrix([[number(z) for z in row] for row in o.extract(sector,sector).tolist()])
op=[matrix(o.subs(la,-20)) for o in ox]
bs=[matrix(b) for b in bonds]
zero=mp.zeros(20)
h=sum(op,zero)+sum(bs,zero)
values,vectors=mp.eighe(h)
ground=vectors[:,0]
direction=[1,-2,1]
deriv=sum((direction[x]*op[x] for x in range(3)),zero)+sum(((direction[x]+direction[x+1])*bs[x]/2 for x in range(2)),zero)
kato=-2*sum(abs((vectors[:,i].H*deriv*ground)[0])**2/(values[i]-values[0]) for i in range(1,20))
contact=sum((-(direction[x]-direction[x+1])**2*bs[x]/4 for x in range(2)),zero)
prediction={'A':kato,'C':kato+mp.re((ground.H*contact*ground)[0])}
def energy(t,kind):
    N=[1+t*x for x in direction]
    factors=[(N[x]+N[x+1])/2 if kind=='A' else mp.sqrt(N[x]*N[x+1]) for x in range(2)]
    hn=sum((N[x]*op[x] for x in range(3)),zero)+sum((factors[x]*bs[x] for x in range(2)),zero)
    return mp.eighe(hn,eigvals_only=True)[0]
rows=[]
for kind in('A','C'):
    for step in(map(mp.mpf,['.001','.0005','.00025'])):
        e={n:energy(n*step,kind) for n in(-2,-1,0,1,2)}
        second=(-e[2]+16*e[1]-30*e[0]+16*e[-1]-e[-2])/(12*step**2)
        rows.append(dict(kind=kind,step=str(step),second=str(second),prediction=str(prediction[kind]),
                         residual=str(second-prediction[kind])))
result={'gap':str(values[1]-values[0]),'precision_digits':mp.mp.dps,'rows':rows,
        'scope':'Convergence diagnosis of the preserved failed finite-difference fixture; not a new physics proof.'}
(HERE/'CONVERGENCE.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
