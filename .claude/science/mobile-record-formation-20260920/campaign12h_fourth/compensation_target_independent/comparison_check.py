#!/usr/bin/env python3
"""Compare only the authorized general-compensation theorem and sealed PRE."""
from pathlib import Path
import sys
sys.dont_write_bytecode=True
import hashlib,json
import sympy as sp
from finite_blocks import exact_blocks,ingredients
HERE=Path(__file__).resolve().parent;AUTHOR=HERE.parent/'local_compensation_author'
PRE_HASH='0504a3fc90cca1b0f9b7bab3a1aa346b11e0889bc25abf55bd65966965375a46'
SEAL_HASH='630f063e8fd546c844dba720943198070c49573d9de1c3870531ec40791e373f'
NOTE_HASH='9bc691a07fd70c1a813852aa0cac55832065b3c95cf3d50e5528845f6613e0b0'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def authenticate(path,expected):
 assert sha(path)==expected;s=json.loads(path.read_text());counts={}
 for group in ['sources','artifacts']:
  for item in s[group]:
   p=Path(item['path']);assert len(p.read_bytes())==item['bytes'] and sha(p)==item['sha256']
  counts[group]=len(s[group])
 return s,counts
pre,pre_counts=authenticate(HERE/'PRE_COMPARISON_SEAL.json',PRE_HASH)
seal,author_counts=authenticate(AUTHOR/'GENERAL_TARGET_AUTHOR_SEAL.json',SEAL_HASH)
note_path=AUTHOR/'BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET.md';assert sha(note_path)==NOTE_HASH
note=note_path.read_text();quote='All displayed operators are self-adjoint.'
assert note.count(quote)==1
line=next(i for i,s in enumerate(note.splitlines(),1) if quote in s)
# Literal author Eq. (2), evaluated on the frozen independent finite model.
W,N,T,C,jumps=exact_blocks();ix,qx,A,Z,M,C0,C1,K2,K4,B=ingredients(W,T,C,jumps)
H2_author=C0-M
H4_author=M*M-(M*C0+C0*M)/2+A.H*C1*A-Z.H*Z/2
B_author=[-j.extract(ix,[i for i in range(W.rows) if W[i,i]==1])*A for j in jumps]
assert H2_author==K2 and H4_author==K4 and B_author==B
assert H2_author.H==H2_author and H4_author.H==H4_author
saved=json.loads((HERE/'BLOCK_RESULTS.json').read_text())
def matrix(rows):return sp.Matrix([[sp.Rational(v) for v in row] for row in rows])
assert H2_author==matrix(saved['K2']) and H4_author==matrix(saved['K4'])
assert B_author==[matrix(rows) for rows in saved['leading_effective_jumps']]
# Exact countercontrol to the blanket sentence, from author Eq. (6).
graph4=M*M-M*C0+A.H*C1*A-Z.H*Z/2
anti=graph4-graph4.H;anti_squared=sp.trace(anti.H*anti)
assert anti_squared==202 and graph4!=graph4.H
jump_anti_squared=[]
for b in B_author:
 D=b-b.H;jump_anti_squared.append(str(sp.trace(D.H*D)))
assert all(sp.Rational(v)>0 for v in jump_anti_squared)
# Read the recorded density controls, but do not rerun already checked dynamics.
density=json.loads((HERE/'DENSITY_RESULTS.json').read_text())
assert density['maximum_trace_error_over_epsilon']<4
print(json.dumps({'PRE_sha256':PRE_HASH,'PRE_bindings_unchanged':pre_counts,
 'author_seal_sha256':SEAL_HASH,'author_bindings_verified':author_counts,
 'author_note_sha256':NOTE_HASH,'author_equation_2_matches_exact_independent_coefficients_and_jumps':True,
 'both_canonical_Hamiltonian_coefficients_self_adjoint':True,
 'finding':{'id':'F1','type':'Narrow overbroad self-adjointness sentence; equations and theorem unchanged.',
 'line':line,'quote':quote,'raw_graph_fourth_antihermitian_frobenius_squared':str(anti_squared),
 'formation_jump_antihermitian_frobenius_squared':jump_anti_squared,
 'requested_replacement':'Both Hamiltonian coefficients H2^C and H4^C are self-adjoint.'},
 'comparison_limits':{'full_author_note_read':True,'other_author_files_read':False,
 'new_scientific_execution':'Exact coefficient identity and sentence countercontrol only; no repeated propagation.',
 'stronger_PRE_diagonal_discrepancy_bound':'O(epsilon^2), versus the sufficient author O(epsilon); not a discrepancy.',
 'excluded_scope':'No particular local compensation construction or physical completion was read or checked.'}},indent=2))
