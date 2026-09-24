#!/usr/bin/env python3
"""Exact residue-polynomial coefficients of the finite-spin Jacobi matrix."""
from fractions import Fraction
import importlib.util
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location("core",HERE/"core_derivation.py")
core=importlib.util.module_from_spec(spec); spec.loader.exec_module(core)
nodes=core.walk_nodes(100)
dtab=json.loads((HERE/"D_RESIDUE_POLYNOMIALS.json").read_text())

def x_pair(paths):
    assert len(paths)==1,paths
    m1,a1,m2,a2=paths[0][3]
    return (m1*(m1+a1),m2*(m2+a2))

def edge_x(n):
    return x_pair([p for p in core.two_hop_paths(nodes[n]) if p[0]==nodes[n+1]])

def returns_x(n):
    paths=[p for p in core.two_hop_paths(nodes[n]) if p[0]==nodes[n]]
    assert len(paths)==2,paths
    out=[]
    for p in paths:
        pair=x_pair([p])
        assert pair[0]==pair[1],(n,pair)
        out.append(pair[0])
    return tuple(out)

def fit(vals):
    y0,y1,y2=vals
    A=Fraction(y2-2*y1+y0,2)
    B=Fraction(y1-y0)-A
    return (A,B,Fraction(y0))

def value(p,k):
    return p[0]*k*k+p[1]*k+p[2]

rows=[]
for r in range(15):
    e_samples=[edge_x(r+15*k) for k in (0,1,2)]
    e_polys=[fit([z[j] for z in e_samples]) for j in (0,1)]
    d_samples=[returns_x(r+15*k) for k in (0,1,2)]
    d_polys=[fit([z[j] for z in d_samples]) for j in (0,1)]
    for k in (-1,3):
        assert edge_x(r+15*k)==tuple(value(p,k) for p in e_polys),(r,k,"edge")
        assert returns_x(r+15*k)==tuple(value(p,k) for p in d_polys),(r,k,"diag")
    assert all(p[0]==9 for p in e_polys+d_polys)
    dtabrow=dtab["rows"][r]
    D_edge=tuple(Fraction(x) for x in dtabrow["right"]["quadratic_k2_k_const"])
    D_diag=tuple(Fraction(x) for x in dtabrow["diag"]["quadratic_k2_k_const"])
    assert tuple((e_polys[0][j]+e_polys[1][j])/2 for j in range(3))==D_edge
    assert tuple(d_polys[0][j]+d_polys[1][j] for j in range(3))==D_diag
    rows.append({"residue":r,
        "edge_x1_k2_k_const":[str(x) for x in e_polys[0]],
        "edge_x2_k2_k_const":[str(x) for x in e_polys[1]],
        "return_x1_k2_k_const":[str(x) for x in d_polys[0]],
        "return_x2_k2_k_const":[str(x) for x in d_polys[1]]})

out={
 "status":"exact legal-hop path polynomials; all 15 residue classes checked at k=-1,0,1,2,3",
 "coordinate":"n=15k+r; one P-state per integer n in this connected component",
 "finite_spin_matrix":"M_S=-H2,S is tridiagonal on I_S=[-5S,5S-4]",
 "entry_form":"M_S[n,n+1]=sqrt((1-x1/C)(1-x2/C)); M_S[n,n]=2-(y1+y2)/C, with C=S(S+1)",
 "boundary":"an outward edge has a factor x_i=C and therefore vanishes",
 "generator_identity":"G_S=C H2,S+H4,S=M_S^2-C M_S because the two-A-vacancy block is zero",
 "rows":rows,
 "scope":"integer S, supplied five-record one-vacancy sector; identities are conditional on the #8831 model"
}
(HERE/"FINITE_SPIN_JACOBI_COEFFICIENTS.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
