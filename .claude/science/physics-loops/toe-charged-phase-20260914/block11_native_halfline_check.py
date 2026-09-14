"""Author falsifiers: actual native pulses, half-line clock and finite horizon."""
import numpy as np
from scipy import sparse as sp
from scipy.sparse.linalg import expm_multiply
from scipy.linalg import eigh_tridiagonal, expm
from scipy.special import jv, gammaincc
from math import pi, factorial, ceil, sinh, exp, log

I2=np.eye(2,dtype=complex)
X2=np.array([[0,1],[1,0]],complex)
Y2=np.array([[0,-1j],[1j,0]],complex)
Z2=np.diag([1.,-1.]).astype(complex)
low2=np.array([[0,1],[0,0]],complex)

def kron_list(xs):
    y=np.array([[1.]],complex)
    for x in xs:y=np.kron(y,x)
    return y

def native_fixture():
    names=['hv','hw','x','f','b0','b1','l0','l1'];D=256;I=np.eye(D,dtype=complex)
    def op(name,small):return kron_list([small if n==name else I2 for n in names])
    X={n:op(n,X2) for n in names};Z={n:op(n,Z2) for n in names}
    low={n:op(n,low2) for n in names};num={n:(I-Z[n])/2 for n in names}
    Y=op('x',Y2);q=num['f'];a=I-q;n=num['b1'];pp=(I+Y)/2;pm=(I-Y)/2;Pm=(I-Z['x'])/2
    K=q@(I+Y)+.5*I+num['b0']+2*num['b1'];Nh=num['hv']+num['hw']
    Efb=low['f']@low['b1'].conj().T+low['f'].conj().T@low['b1']
    Eh=low['hv']@low['hw'].conj().T+low['hv'].conj().T@low['hw']
    controls=[pp@n@(X['l0']-I),pp@n@(X['l1']-I),pp@Efb,pm@X['f'],a@(X['l1']-I),a@Pm@(X['l0']-I),a@Pm@(X['l1']-I),a@Eh,a]
    pulses=[]
    for j,G in enumerate(controls):
        if j in [0,1,4,5,6]:U=I+G
        elif j==8:U=I-2*G
        else:U=I-G@G-1j*G
        # Entries are Gaussian dyadic rationals exactly representable in binary64;
        # these finite products use no transcendental arithmetic.
        assert np.array_equal(G,G.conj().T)
        assert np.array_equal(U.conj().T@U,I)
        assert np.array_equal(U@K,K@U)
        assert np.array_equal(U@Nh,Nh@U)
        pulses.append(U)
    def idx(bits):return int(''.join(map(str,bits)),2)
    R=np.zeros((D,8),complex);V=np.zeros_like(R)
    pp2=(I2+Y2)/2;pm2=(I2-Y2)/2
    for x in range(2):
      for b0 in range(2):
       for b1 in range(2):
        c=4*x+2*b0+b1;R[idx([1,0,x,1,b0,b1,0,0]),c]=1
        # Separately assembled physical branch matrix elements, no pulse product.
        for z in range(2):
          label=[0,1] if z==0 else [1,0]
          V[idx([0,1,z,0,b0,b1,*label]),c]+=pm2[z,x]
          if b1==0:V[idx([0,1,z,0,b0,1,*label]),c]+=pp2[z,x]
        if b1==1:
          for y in range(2):V[idx([1,0,y,1,b0,b1,1,1]),c]+=pp2[y,x]
    prefixes=[I]
    for U in pulses:prefixes.append(U@prefixes[-1])
    assert np.array_equal(prefixes[-1]@R,V)
    assert np.array_equal(V.conj().T@V,np.eye(8))
    Kin=R.conj().T@K@R
    assert np.array_equal(K@V,V@Kin)
    # Deliberately phase-sensitive: all eight columns, not outcome norms alone.
    labels=[(I+Z['l0'])@(I+Z['l1'])/4,(I+Z['l0'])@(I-Z['l1'])/4,
            (I-Z['l0'])@(I+Z['l1'])/4,(I-Z['l0'])@(I-Z['l1'])/4]
    assert np.array_equal(sum(labels),I)
    for P in labels:assert np.array_equal(P@K,K@P)
    assert np.count_nonzero(labels[0]@V)==0
    return I,K,R,V,pulses,prefixes,labels

def native_exact_columns():
    I,K,R,V,Us,Ws,Ps=native_fixture()
    assert np.array_equal(R.conj().T@V,np.zeros((8,8)))
    # Choi overlap at t=0 is zero: exact interval-capture theorem is nonvacuous.
    print('NATIVE exact Gaussian-dyadic columns=8 K_spectrum=',np.unique(np.linalg.eigvalsh(K)).round(8).tolist())

def amplitudes(M,t,J=1.):
    if t==0:
        out=np.zeros(M,complex);out[0]=1;return out
    n=np.arange(M)
    return np.exp(-2j*J*t)*(1j)**n*(jv(n,2*J*t)+jv(n+2,2*J*t))

def scalar_clock(M,t,J=1.):
    ev,Q=eigh_tridiagonal(np.full(M,2*J),np.full(M-1,-J))
    return Q@(np.exp(-1j*t*ev)*Q[0])

def halfline_integrals_and_tail():
    from scipy.integrate import quad
    # Compare spectral sine integral, Bessel recurrence, and finite path spectrum.
    largest=0.
    for t in [.01,.5,2.,6.,18.,40.]:
        a=amplitudes(160,t);b=scalar_clock(160,t)
        largest=max(largest,np.linalg.norm(a-b));assert np.linalg.norm(a-b)<3e-13
        n=np.arange(160);r=np.exp(-2j*t)*(1j)**n*(n+1)/t*jv(n+1,2*t)
        assert np.max(abs(a-r))<3e-14
        for k in [0,1,4,8,12]:
            fun=lambda q:2/pi*np.sin(q)*np.sin((k+1)*q)*np.exp(-2j*t*(1-np.cos(q)))
            z=quad(lambda q:fun(q).real,0,pi,epsabs=1e-11)[0]+1j*quad(lambda q:fun(q).imag,0,pi,epsabs=1e-11)[0]
            assert abs(z-a[k])<3e-12
    for L in [1,2,9,17]:
        C=L*(L+1)*(2*L+1)/6
        for t in np.geomspace(.05,1e4,48):
            eta=np.vdot(amplitudes(L,t),amplitudes(L,t)).real
            assert eta<=min(1,C/t**2)+1e-13
            if t>=max(L,72/pi**2):assert eta<=32*C/(pi*pi*t**3)+1e-13
        E=sum(m*m for m in range(2,L+1,2));O=sum(m*m for m in range(1,L+1,2))
        # Asymptotic formula is tested only at genuinely late times for fixed L.
        errors=[]
        for t in [1e4,1e5,1e6]:
            phi=2*t-pi/4;eta=np.sum(abs(amplitudes(L,t))**2)
            prediction=(E*np.cos(phi)**2+O*np.sin(phi)**2)/pi
            errors.append(abs(t**3*eta-prediction))
            assert errors[-1] < 3*L**5/t
    print('HALFLINE sine/Bessel/finite-spectrum max_vector_residual=',largest,'L9_parity_sums=',[120,165])

def positive_full_bonds():
    # Full TWO-clock-qubit extension, including 00 and 11, actual 256 native states.
    I,K,R,V,Us,Ws,Ps=native_fixture();z=np.zeros_like(I)
    maxres=0.
    for U in Us+[I]:
        # Clock order 00,01,10,11; |01><10| multiplies U.
        B=np.block([[z,z,z,z],[z,I,-U,z],[z,-U.conj().T,I,z],[z,z,z,2*I]])
        assert np.array_equal(B,B.conj().T)
        assert np.array_equal(B@B,2*B)  # spectrum subset {0,2}, hence PSD.
        Kfull=np.kron(np.eye(4),K)
        assert np.array_equal(B@Kfull,Kfull@B)
        maxres=max(maxres,np.max(abs(B@B-2*B)))
    print('POSITIVE full_bond_dimension=1024 actual_gate_bonds=9 polynomial_residual=',maxres)

def direct_native_joint():
    I,K,R,V,Us,Ws,Ps=native_fixture();M=40;D=256
    # Build oriented hopping from actual U, without using D Hpath D†.
    blocks=[[None for _ in range(M)] for _ in range(M)]
    for n in range(M):
        blocks[n][n]=sp.csr_matrix(K+2*I)
        if n<M-1:
            U=Us[n] if n<len(Us) else I
            blocks[n+1][n]=sp.csr_matrix(-U)
            blocks[n][n+1]=sp.csr_matrix(-U.conj().T)
    H=sp.bmat(blocks,format='csr');R0=np.zeros((M*D,8),complex);R0[:D]=R
    Kfull=sp.kron(sp.eye(M),sp.csr_matrix(K),format='csr')
    comm=H@Kfull-Kfull@H;assert comm.nnz==0 or np.max(abs(comm.data))==0
    maxres=0.
    for t in [.15,2.5,9.,18.]:
        a=scalar_clock(M,t);free=expm(-1j*t*K)
        expected=np.vstack([a[n]*(free@Ws[min(n,9)]@R) for n in range(M)])
        actual=expm_multiply(-1j*t*H,R0,traceA=-1j*t*H.diagonal().sum())
        residual=np.max(abs(actual-expected));maxres=max(maxres,residual)
        assert residual<3e-12
        eta=np.sum(abs(a[:9])**2);p=1-eta
        if p>1e-9:
            target=np.vstack([np.zeros_like(V) if n<9 else a[n]/np.sqrt(p)*(free@V) for n in range(M)])
            # Full input/reference Choi norm and overlap, not just a selected state.
            overlap=np.trace(target.conj().T@actual)/8
            assert abs(overlap-np.sqrt(p))<3e-12
        # Completed-tail cutoff must remain gate9; early completion is not allowed.
        if t==2.5:assert eta>.99
    print('JOINT direct_sparse_dimension=',M*D,'columns=8 max_entry_residual=',maxres)

def finite_horizon_and_recurrence():
    L=9;eps=.01;T0=max(L,72/pi**2,(128*285/(pi*pi*eps))**(1/3));T=100.;mu=1.
    M=ceil((2*T*sinh(mu)+log(16/((1-exp(-mu))*eps)))/mu)
    em=4*exp(-mu*M+2*T*sinh(mu))/(1-exp(-mu))
    assert 2*32*285/(pi*pi*T0**3)+2*em<=eps*(1+1e-12)
    # Nontrivial finite-size error tested where visible, and its Chebyshev bound.
    rows=[]
    for M1,t in [(18,4.),(30,8.),(48,16.),(70,25.)]:
        N=max(256,4*M1);af=scalar_clock(M1,t);ai=amplitudes(N,t)
        embedded=np.zeros(N,complex);embedded[:M1]=af
        err=np.linalg.norm(embedded-ai)
        mu1=np.arccosh(M1/(2*t))
        bound=4*np.exp(-mu1*M1+2*t*np.sinh(mu1))/(1-np.exp(-mu1))
        # Direct absolute Bessel tail is a separate route to the same norm bound.
        tail=4*np.sum(abs(jv(np.arange(M1,4*N),2*t)))
        assert err<=tail+5e-13 and tail<=bound+5e-13
        rows.append([M1,t,float(err),float(bound)])
    # The previous engineered finite clock arrives exactly then reverses.
    g=pi/2;j=np.arange(17)
    ev,Q=eigh_tridiagonal(np.zeros(18),g*np.sqrt((j+1)*(17-j)))
    a1=Q@(np.exp(-1j*ev)*Q[0]);a2=Q@(np.exp(-2j*ev)*Q[0])
    assert abs(abs(a1[17])-1)<1e-13 and abs(abs(a2[0])-1)<1e-13
    assert np.sum(abs(a2[:9])**2)>1-1e-12
    print('HORIZON epsilon=.01 J=1 T0=',T0,'T=100 M=',M,'certified_error=',2*32*285/(pi*pi*T0**3)+2*em,'finite_rows=',rows)

def absorbing_clock_and_instrument():
    I,K,R,V,Us,Ws,Ps=native_fixture();L=9;gamma=1.3
    G=np.zeros((L+1,L+1))
    for j in range(L):G[j,j]=-gamma;G[j+1,j]=gamma
    for t in [.1,1.,5.,10.,30.]:
        p=expm(t*G)[:,0];analytic=np.array([exp(-gamma*t)*(gamma*t)**j/factorial(j) for j in range(L)]+[0.])
        analytic[-1]=1-analytic[:-1].sum()
        assert np.max(abs(p-analytic))<3e-14
        assert abs(p[:-1].sum()-gammaincc(L,gamma*t))<3e-14
        assert p[-1]<1  # finite t in tested range, no finite completion certainty.
    # Split final jumps conserve K as an observable on the full native carrier.
    E=sum((P@Us[-1]).conj().T@K@(P@Us[-1]) for P in Ps)
    assert np.array_equal(E,K)
    psi=np.array([1,1j,-.2,.7j,.3,-.4j,.6,.1j],complex);psi/=np.linalg.norm(psi)
    out=V@psi;rho=np.outer(out,out.conj());dephased=sum(P@rho@P for P in Ps)
    assert np.linalg.norm(rho-dephased)>0.1
    assert abs(np.trace(K@rho)-np.trace(K@dephased))<1e-14
    assert abs(np.trace(dephased)-1)<1e-14
    # Exact stationary labels in this explicitly supplied absorbing generator.
    for P in Ps:
        assert np.array_equal(P@K,K@P)
    print('ABSORBING Erlang/master_equation matched; coherent_vs_dephased_difference=',np.linalg.norm(rho-dephased))

if __name__=='__main__':
    for f in [native_exact_columns,halfline_integrals_and_tail,positive_full_bonds,direct_native_joint,finite_horizon_and_recurrence,absorbing_clock_and_instrument]:
        f();print('PASS',f.__name__,flush=True)
