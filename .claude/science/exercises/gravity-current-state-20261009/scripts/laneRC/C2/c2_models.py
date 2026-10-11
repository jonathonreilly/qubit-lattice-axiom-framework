"""C2 models: densities of H for 2D spin models (square, honeycomb, toric code edges)."""
import numpy as np
from pauli_ti import Lat, canon
X, Y, Z = 1, 2, 3
s3 = np.sqrt(3.0)

def dens(terms):
    D = {}
    for c, s in terms:
        cs, _ = canon(tuple(sorted(s)))
        D[cs] = D.get(cs, 0) + c
    return D

SQ = Lat((1, 0), (0, 1), [(0, 0)])
def tfim(h=3.0, J=1.0):
    return SQ, dens([(-J, [((0,0,0),Z), ((1,0,0),Z)]), (-J, [((0,0,0),Z), ((0,1,0),Z)]), (-h, [((0,0,0),X)])])
def tfim_long(h=3.0, g=0.5, J=1.0):
    return SQ, dens([(-J, [((0,0,0),Z), ((1,0,0),Z)]), (-J, [((0,0,0),Z), ((0,1,0),Z)]), (-h, [((0,0,0),X)]), (-g, [((0,0,0),Z)])])
def xx2d():
    t = []
    for d in [(1,0,0),(0,1,0)]:
        for p in [X, Y]:
            t.append((1.0, [((0,0,0),p), (d,p)]))
    return SQ, dens(t)
def xxz2d(Delta=0.5):
    t = []
    for d in [(1,0,0),(0,1,0)]:
        for p, c in [(X,1.0),(Y,1.0),(Z,Delta)]:
            t.append((c, [((0,0,0),p), (d,p)]))
    return SQ, dens(t)
def compass():
    return SQ, dens([(1.0, [((0,0,0),X), ((1,0,0),X)]), (1.0, [((0,0,0),Z), ((0,1,0),Z)])])
def xx_chains():   # decoupled XX chains along x: integrable control
    return SQ, dens([(1.0, [((0,0,0),X), ((1,0,0),X)]), (1.0, [((0,0,0),Y), ((1,0,0),Y)])])
def plaquette_ising(h=1.0):  # Xu-Moore: -sum ZZZZ - h sum X
    return SQ, dens([(-1.0, [((0,0,0),Z), ((1,0,0),Z), ((0,1,0),Z), ((1,1,0),Z)]), (-h, [((0,0,0),X)])])

# toric code: k=0 horizontal edge at (x+1/2,y), k=1 vertical edge at (x,y+1/2)
TC = Lat((1, 0), (0, 1), [(0.5, 0), (0, 0.5)])
def toric(hz=0.0, hx=0.0):
    t = [(-1.0, [((0,0,0),X), ((-1,0,0),X), ((0,0,1),X), ((0,-1,1),X)]),
         (-1.0, [((0,0,0),Z), ((0,1,0),Z), ((0,0,1),Z), ((1,0,1),Z)])]
    if hz: t += [(-hz, [((0,0,0),Z)]), (-hz, [((0,0,1),Z)])]
    if hx: t += [(-hx, [((0,0,0),X)]), (-hx, [((0,0,1),X)])]
    return TC, dens(t)

HC = Lat((1, 0), (0.5, s3/2), [(0, 0), (0, 1/s3)])
def kitaev(Jx=1.0, Jy=1.0, Jz=1.0, hfield=0.0, JH=0.0):
    t = [(Jz, [((0,0,0),Z), ((0,0,1),Z)]),
         (Jx, [((0,0,0),X), ((1,-1,1),X)]),
         (Jy, [((0,0,0),Y), ((0,-1,1),Y)])]
    if JH:
        for bsite in [(0,0,1), (1,-1,1), (0,-1,1)]:
            for p in [X, Y, Z]:
                t.append((JH, [((0,0,0),p), (bsite,p)]))
    if hfield:
        for k in [0, 1]:
            for p in [X, Y, Z]:
                t.append((hfield/np.sqrt(3), [((0,0,k),p)]))
    return HC, dens(t)
