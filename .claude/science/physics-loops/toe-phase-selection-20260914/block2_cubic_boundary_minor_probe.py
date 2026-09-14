#!/usr/bin/env python3
"""Bounded search for an induced signed-cycle minor of the actual cubic F.

A non-unimodular submatrix would test whether an event-allocation proof can
rely on total unimodularity of F. It does not test sector energies.
"""
from pathlib import Path
import importlib.util,json,time
import numpy as np
import sympy as sp

pack=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('cells',pack/'block1_projection_sector_check.py')
cells=importlib.util.module_from_spec(spec);spec.loader.exec_module(cells)

def main():
    levels,_,F,D=cells.box_complex((3,3,3))
    adjacency=[[] for _ in range(F.shape[1])]
    for p,row in enumerate(F):
        edges=np.flatnonzero(row)
        for e in edges:
            for other in edges:
                if other!=e:adjacency[e].append((int(other),p,int(-row[e]*row[other])))
    rng=np.random.default_rng(20260914);found=None;start=time.monotonic();attempt=0
    for attempt in range(100000):
        root=int(rng.integers(F.shape[1]));path=[root];faces=[];sign=1
        for _ in range(18):
            options=[a for a in adjacency[path[-1]] if a[1] not in faces and (a[0] not in path or a[0]==root)]
            if not options:break
            nxt,p,w=options[int(rng.integers(len(options)))]
            if nxt==root:
                if len(path)>2 and sign*w==-1:
                    rows=faces+[p];M=F[np.ix_(rows,path)]
                    if np.all(np.count_nonzero(M,axis=1)==2) and np.all(np.count_nonzero(M,axis=0)==2):
                        determinant=int(sp.Matrix(M).det());assert abs(determinant)==2
                        found={'rows':rows,'columns':path,'minor':M.tolist(),'determinant':determinant,
                               'faces':[levels[2][i] for i in rows],'edges':[levels[1][i] for i in path]}
                break
            path.append(nxt);faces.append(p);sign*=w
        if found:break
    out={'scope':'induced signed-cycle minor of 3x3x3 cubic edge-to-face coboundary',
         'elapsed_seconds':time.monotonic()-start,'attempts':attempt+1,'found':found}
    (pack/'BLOCK2_CUBIC_BOUNDARY_MINOR_PROBE.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
