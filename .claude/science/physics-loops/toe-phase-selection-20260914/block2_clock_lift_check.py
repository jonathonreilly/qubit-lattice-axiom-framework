#!/usr/bin/env python3
"""Lift the sparse cubic path to original Z3 link coordinates and verify it."""
from pathlib import Path
import importlib.util,json
import numpy as np

PACK=Path(__file__).resolve().parent

def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    out=importlib.util.module_from_spec(spec);spec.loader.exec_module(out);return out

def solve_mod_three(A,b):
    M=np.column_stack([A,b]).copy()%3
    row=0;pivots=[]
    for col in range(A.shape[1]):
        nz=np.flatnonzero(M[row:,col])
        if not len(nz):continue
        pivot=row+int(nz[0]);M[[row,pivot]]=M[[pivot,row]]
        M[row]=(M[row]*int(M[row,col]))%3 # inverse(1)=1, inverse(2)=2
        factors=M[:,col].copy();factors[row]=0
        M=(M-factors[:,None]*M[row][None,:])%3
        pivots.append(col);row+=1
        if row==M.shape[0]:break
    assert not np.any((np.all(M[:,:-1]==0,axis=1))&(M[:,-1]!=0))
    x=np.zeros(A.shape[1],dtype=int)
    for r,c in enumerate(pivots):x[c]=M[r,-1]
    assert np.all((A@x-b)%3==0)
    return (x+1)%3-1

def main():
    cells=module('cells',PACK/'block1_projection_sector_check.py')
    sparse_path=module('path',PACK/'block2_cubic_path_exact_check.py')
    levels,_,F,D=cells.box_complex((5,5,5))
    b=np.array([sparse_path.INITIAL.get(face,0) for face in levels[2]],dtype=int)
    assert np.all((D@b)%3==0)
    a=solve_mod_three(F,b);initial=a.copy()
    assert np.array_equal((F@a+1)%3-1,b)
    base_charge=D@b//3;moves=[]
    for sign,edges in ((1,sparse_path.EDGES),(-1,list(reversed(sparse_path.EDGES)))):
        for axis,anchor in edges:
            l=levels[1].index(((axis,),anchor));f=F[:,l]
            direct=sparse_path.curl_of_edge(axis,anchor)
            assert np.array_equal(f,np.array([direct.get(face,0) for face in levels[2]]))
            a[l]=(a[l]+sign+1)%3-1
            new=(F@a+1)%3-1
            assert np.array_equal(new,b+sign*f)
            assert np.array_equal(D@new//3,base_charge)
            moves.append({'edge':[axis,anchor],'sign':sign,'integer_wrap_count':0})
            b=new
    assert np.array_equal(a,initial)
    result={'box':[5,5,5],'original_clock_edges':[(levels[1][i],int(v)) for i,v in enumerate(initial) if v],
            'edge_word_nonzero_count':int(np.count_nonzero(initial)),
            'all_fourteen_steps_have_no_face_wrap':True,'closed_original_clock_path':True,
            'charge_pattern':[(levels[3][i],int(v)) for i,v in enumerate(base_charge) if v],
            'moves':moves,'sparse_and_dense_incidence_match':True}
    (PACK/'BLOCK2_CLOCK_LIFT_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('original_clock_edges','moves')},indent=2))

if __name__=='__main__':main()
