import numpy as np, itertools, time
sg=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]],complex)]
def basis_V(j):
    """unitary V with V^dag sigma_j V = X, V^dag sigma_{j+1} V = Y  (columns = a_j,b_j)"""
    X=sg[j];Y=sg[(j+1)%3]
    sx,sy=sg[0],sg[1]
    for sgn in itertools.product([1,-1],repeat=3):
        V=(np.eye(2)+1j*sum(s*m for s,m in zip(sgn,sg)))/2
        for pre in (np.eye(2),):
            pass
        # search over the 24 cubic rotations incl. identity: V from products
    # brute force: eigen-decompose
    # find V by requiring V^dag X V = sx, V^dag Y V = sy: V = columns from joint solution
    # construct via rotation taking (X,Y,Z)->(sx,sy,sz): use quaternion from matching
    Z=-1j*X@Y
    # V maps standard basis: V sx V^dag = X, V sy V^dag = Y, V sz V^dag = Z
    # V = (1/(2 c)) (I + X sx + Y sy + Z sz)  [up to normalisation]
    M=np.eye(2)+X@sx+Y@sy+Z@sg[2]
    V=M/np.sqrt(np.trace(M.conj().T@M).real/2)
    assert np.allclose(V.conj().T@V,np.eye(2)),(j,)
    assert np.allclose(V@sx@V.conj().T,X) and np.allclose(V@sy@V.conj().T,Y)
    return V
Vs=[basis_V(j) for j in range(3)]
def apply_layer(psi,j,kind,alpha_cos,alpha_sin):
    """psi shape (nx,ny,nz,2) standard basis. alpha arrays shape (nx,ny,nz) = bond (x,x+e_j)."""
    V=Vs[j]
    phi=np.einsum('ab,xyzb->xyza',V.conj().T,psi)  # components (a,b)
    a=phi[...,0];b=phi[...,1]
    if kind=='A':   # pairs (a,x),(b,x+e)
        bs=np.roll(b,-1,axis=j)
        an=alpha_cos*a-1j*alpha_sin*bs
        bsn=alpha_cos*bs-1j*alpha_sin*a
        bn=np.roll(bsn,1,axis=j)
    else:           # pairs (b,x),(a,x+e)
        as_=np.roll(a,-1,axis=j)
        bn=alpha_cos*b-1j*alpha_sin*as_
        asn=alpha_cos*as_-1j*alpha_sin*b
        an=np.roll(asn,1,axis=j)
    phi2=np.stack([an,bn],axis=-1)
    return np.einsum('ab,xyzb->xyza',V,phi2)
SEQ=[(0,'A'),(0,'B'),(1,'A'),(1,'B'),(2,'A'),(2,'B')]
def make_tick(w,eps0,order='pal'):
    """w: array (nx,ny,nz) site clock. bond angle eps0*sqrt(w(x)w(x+e_j))"""
    ang=[eps0*np.sqrt(w*np.roll(w,-1,axis=j)) for j in range(3)]
    cs=[(np.cos(a),np.sin(a)) for a in ang]
    ch=[(np.cos(a/2),np.sin(a/2)) for a in ang]
    def tick(psi):
        if order=='pal':
            for (j,kd) in SEQ[:5]:
                psi=apply_layer(psi,j,kd,*ch[j])
            psi=apply_layer(psi,SEQ[5][0],SEQ[5][1],*cs[SEQ[5][0]])
            for (j,kd) in reversed(SEQ[:5]):
                psi=apply_layer(psi,j,kd,*ch[j])
        else:  # plain: L1 first ... L6 last
            for (j,kd) in SEQ:
                psi=apply_layer(psi,j,kd,*cs[j])
        return psi
    return tick
def symbol(k,eps,order='pal'):
    """2x2 symbol in the standard basis for uniform angle eps at wave vector k (psi=e^{ik.x} u)."""
    I2=np.eye(2)
    def lay(j,kind,a):
        X=sg[j];Y=sg[(j+1)%3]
        g=np.cos(k[j])*X-np.sin(k[j])*Y if kind=='A' else np.cos(k[j])*X+np.sin(k[j])*Y
        return np.cos(a)*I2-1j*np.sin(a)*g
    if order=='pal':
        S=I2
        for (j,kd) in SEQ[:5]: S=S@lay(j,kd,eps/2)
        S=S@lay(SEQ[5][0],SEQ[5][1],eps)
        for (j,kd) in reversed(SEQ[:5]): S=S@lay(j,kd,eps/2)
    else:
        S=I2
        for (j,kd) in SEQ: S=lay(j,kd,eps)@S
    return S
