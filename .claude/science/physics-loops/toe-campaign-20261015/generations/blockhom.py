import numpy as np
from scipy.linalg import null_space, expm
import coinrep as CR
B = np.load('blockreps.npy')
def spin(j):
    Jx, Jy, Jz = CR.spin_mats(j); return expm(-1j*np.pi/2*Jz), expm(-1j*np.pi/2*Jx)
RZ = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]); RX = np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
Bs = np.array([[1, 1], [-1, 1], [0, -2]]) @ np.diag([1/np.sqrt(2), 1/np.sqrt(6)])
irr = {'A1': (np.eye(1), np.eye(1)), 'E': (Bs.T @ np.abs(RZ) @ Bs, Bs.T @ np.abs(RX) @ Bs),
       'T1': spin(1.0), 'E1/2': spin(0.5), 'H': spin(1.5)}
def hom(Db, Dx):
    (bz, bx), (xz, xx) = Db, Dx; n, m = bz.shape[0], xz.shape[0]
    M = np.vstack([np.kron(np.eye(m), bz) - np.kron(xz.T, np.eye(n)), np.kron(np.eye(m), bx) - np.kron(xx.T, np.eye(n))])
    return null_space(M).shape[1]
for i, (DZ, DX) in enumerate(B):
    out = {}
    for name, (xz, xx) in irr.items():
        for sz in (1, -1, 1j, -1j):
            for sx in (1, -1, 1j, -1j):
                h = hom((DZ.astype(complex), DX.astype(complex)), (sz * xz, sx * xx))
                if h: out[f'{name}[{sz},{sx}]'] = h
    print('block', i, out)
