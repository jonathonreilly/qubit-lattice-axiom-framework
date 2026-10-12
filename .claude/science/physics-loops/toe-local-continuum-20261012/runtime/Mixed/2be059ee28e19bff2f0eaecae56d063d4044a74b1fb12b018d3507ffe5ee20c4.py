"""Literal Pauli even words and state moments, independent coefficient oracle."""
import numpy as np
from scipy.linalg import eigh, expm
from reporting import arguments,Book

def kron(ms):
    result=np.ones((1,1),complex)
    for matrix in ms:result=np.kron(result,matrix)
    return result

def literal(L,R,a,m,v):
    size=R-L+1;I=np.eye(2,dtype=complex)
    X=np.array([[0,1],[1,0]],complex);Y=np.array([[0,-1j],[1j,0]],complex);Z=np.diag([1.,-1.])
    site=lambda P,k:kron([P if j==k else I for j in range(size)])
    xs=[site(X,k) for k in range(size)];ys=[site(Y,k) for k in range(size)]
    zs=[site(Z,k) for k in range(size)]
    J=(np.sqrt(m*m+4*v*v/a**2)-m)/4;g=J+m/2
    H=np.zeros((2**size,2**size),complex);Q=H.copy()
    for k,n in enumerate(range(L,R)):
        density=-J*xs[k]@xs[k+1]-g/2*(zs[k]+zs[k+1])
        H+=density;Q+=a*n*density
    gammas=[];string=np.eye(2**size,dtype=complex)
    for k in range(size):
        gammas.extend([string@xs[k],string@ys[k]]);string=string@zs[k]
    return H,Q,gammas

def spin_shift(size,n):
    out=np.zeros((2**size,2**size),complex)
    for col in range(2**size):
        bits=[(col>>(size-1-j))&1 for j in range(size)]
        new=[bits[(j-n)%size] for j in range(size)]
        row=sum(b<<(size-1-j) for j,b in enumerate(new));out[row,col]=1
    return out

def field(gammas,z):
    return sum((coefficient*g for coefficient,g in zip(z,gammas)),np.zeros_like(gammas[0]))

def actual_unitary(word,H,Q,a,size):
    U=np.eye(2**size,dtype=complex)
    for kind,p in word:
        if kind=='t':factor=expm(1j*p*H)
        elif kind=='b':factor=expm(-1j*p*Q)
        elif kind=='x':factor=spin_shift(size,int(np.floor(p/a)))
        U=U@factor
    return U

def main():
    args,c=arguments();b=Book('literal_spin_mixed_words',args)
    a=.37;m=.8;v=1.3;L=-3;R=2;indices=np.arange(L,R+1);size=len(indices)
    H,Q,gammas=literal(L,R,a,m,v);D,B=c.matrices(indices,a,m,v,finite_open=True)
    D=D.toarray();B=B.toarray();dim=len(H)
    # i times row coefficients of i[H,gamma] equals the Hermitian D.
    for name,spin,one in [('time',H,D),('boost',Q,B)]:
        rows=[]
        for gamma in gammas:
            deriv=1j*(spin@gamma-gamma@spin)
            rows.append([1j*np.trace(g@deriv)/dim for g in gammas])
        b.check('literal_generator_'+name,np.linalg.norm(one-np.asarray(rows)),5e-10)
    values,vectors=eigh(H);vac=vectors[:,0]
    eigen,frame=eigh(D);P=frame[:,eigen>0]@frame[:,eigen>0].conj().T
    for i in range(2*size):
        for j in range(i+1,2*size):
            actual=np.vdot(vac,gammas[i]@gammas[j]@vac)
            b.check('ground_covariance',abs(actual-c.pair(np.eye(2*size)[i],np.eye(2*size)[j],P)),5e-10,i=i,j=j)
    base=np.array([[1,.2,.3,-.1],[.1,1,-.2,.4],[.6,-.3,1,.2],
                   [-.2,.8,.3,1],[1,-.4,.1,.7],[.2,.5,-.8,.6]],float)
    fs=[]
    for row in base:
        f=np.zeros(2*size);f[4:8]=row/np.linalg.norm(row);fs.append(f)
    for sign in [-1.,1.]:
        words=[ [('b',sign*.19),('t',.17),('x',a)],
                [('t',-.23),('b',sign*-.14),('x',-a)],
                [('b',sign*-.11),('t',.13),('b',sign*.08),('x',0.)] ]
        actuals=[];zs=[]
        for k,word in enumerate(words):
            U=actual_unitary(word,H,Q,a,size)
            obs=field(gammas,fs[2*k])@field(gammas,fs[2*k+1])
            actuals.append(U@obs@U.conj().T)
            for f in fs[2*k:2*k+2]:
                z,lost=c.lattice_word(f,word,a,D,B);zs.append(z)
                b.check('coefficient_norm_weak',abs(np.linalg.norm(z)-np.linalg.norm(f)),5e-10,sign=sign,block=k)
                b.check('initial_translation_no_wrap',max(lost,default=0.),5e-10,sign=sign,block=k)
            pred=field(gammas,zs[-2])@field(gammas,zs[-1])
            b.check('actual_even_mixed_word',np.linalg.norm(actuals[-1]-pred),5e-10,sign=sign,block=k)
        upper=np.zeros((6,6),complex)
        for i in range(6):
            for j in range(i+1,6):upper[i,j]=c.pair(zs[i],zs[j],P)
        actual=np.eye(dim,dtype=complex)
        for count,obs in enumerate(actuals,1):
            actual=actual@obs;moment=np.vdot(vac,actual@vac)
            proposed=c.pfaffian(upper[:2*count,:2*count])
            b.check('ordered_even_joint_moment',abs(moment-proposed),5e-10,sign=sign,degree=2*count,
                    actual=[float(moment.real),float(moment.imag)],candidate=[float(proposed.real),float(proposed.imag)])
        # Nonzero imaginary pair witness is essential to real-only discrimination.
        b.check('complex_pair_witness',max(0,.05-np.max(np.abs(upper.imag))),0,sign=sign,
                largest_imaginary=float(np.max(np.abs(upper.imag))))
    b.finish('Literal finite spin H/Q and cyclic site permutation provide disjoint arithmetic. Only initially interior even observables are translated, as rightmost factors, so no wrapped odd JW assertion is used. The finite H ground state is a finite-volume oracle, not the infinite chosen state. Real-only covariance can fail the witness and complex moments while norms still pass. All auxiliary odd matrices are grouped into actual even observables.')

if __name__=='__main__':main()
