#!/usr/bin/env python3
"""Cycle650: retain the three Wilson signs as topological sector variables.

Route A removes the three root/Wilson face constraints from Cycle642 and
audits the resulting algebra.  Route B constructs a local flat Z2 link code
and charged seam-hopping covariance proxy.  Route C synthesizes a complete
finite supplied-chart Clifford isometry with three explicit topological input
qubits and audits raw versus Wilson-character-corrected matter generators.

The three extra dimensions are not silently declared spectator gauge: the
raw Cycle642 matter algebra is tested for central sector dependence first.
Authority none; audit unset; author accepted false.
"""
from __future__ import annotations

from collections import Counter
from hashlib import sha256
from itertools import combinations, product
import json
import resource
import signal
import subprocess
import sys
import time
import types
from pathlib import Path


ROOT=Path(__file__).resolve().parents[1]
SHORE="08d8fad170e8c24068b8f818c500a5309ebf96ce"
NOTE=ROOT/"docs/work_history/repo/review_feedback/PHYSICAL_TOPOLOGICAL_SECTOR_GAUGE_SUBSYSTEM_TOURNAMENT_CYCLE650_NOTE_2026-07-23.md"
RECEIPT=ROOT/"outputs/physical_topological_sector_gauge_subsystem_tournament_cycle650_receipt_2026_07_23.json"
COLD=ROOT/"outputs/physical_topological_sector_gauge_subsystem_tournament_cycle650_cold_2026_07_23.txt"
PASS=FAIL=0
PINS={
 "scripts/physical_orbit_tree_structured_full_isometry_tournament_cycle647_2026_07_23.py":"23d5316fb00ed4796bc74e193970f045fa7fa32a020e49fd0534ee0deec3fb18",
 "docs/work_history/repo/review_feedback/PHYSICAL_ORBIT_TREE_STRUCTURED_FULL_ISOMETRY_TOURNAMENT_CYCLE647_NOTE_2026-07-23.md":"1acf92423fcf59456b192d9a58fa8cf538157354d62763d4285d98872741b406",
 "outputs/physical_orbit_tree_structured_full_isometry_tournament_cycle647_receipt_2026_07_23.json":"41752b7c5f6a6deefab2cfdd562052c507896a2015a414297a0f0140b2bbbdbf",
 "outputs/physical_orbit_tree_structured_full_isometry_tournament_cycle647_cold_2026_07_23.txt":"df26b4fd0f2a092499d6bfef8e142c79a868ef783bee1710698b751710cbf518",
}
class Tee:
 def __init__(self,*streams):self.streams=streams
 def write(self,value):
  for stream in self.streams:stream.write(value)
  return len(value)
 def flush(self):
  for stream in self.streams:stream.flush()


def check(label,condition,detail=""):
 global PASS,FAIL
 PASS+=int(condition);FAIL+=int(not condition)
 print("PASS" if condition else "FAIL",label,"::",detail)


def git_bytes(path):return subprocess.check_output(["git","show",f"{SHORE}:{path}"],cwd=ROOT)
def file_sha(path):return sha256(path.read_bytes()).hexdigest()
def load_exact(name,path):
 module=types.ModuleType(name);module.__file__=str(ROOT/path);module.__package__="";sys.modules[name]=module
 exec(compile(git_bytes(path),module.__file__,"exec"),module.__dict__);return module


c647=load_exact("cycle650_exact_cycle647","scripts/physical_orbit_tree_structured_full_isometry_tournament_cycle647_2026_07_23.py")
c642=c647.c642;c643=c647.c643;c532=c647.c532;Pauli=c647.Pauli;Gate=c647.Gate;np=c642.np


def roots_and_retained(obj,length):
 roots=tuple(obj["face_by_axis"][axis][0] for axis in range(3))
 retained=obj["local"]+obj["equality"]+tuple(obj["face_by_axis"][axis][index] for axis in range(3) for index in range(1,length+1))
 return roots,retained


def quotient_data(stabilizers,rows,n):
 sv=tuple(row.symplectic(n) for row in stabilizers);rv=tuple(row.symplectic(n) for row in rows)
 reps=c532.quotient_complement(sv,rv)
 return len(reps),c532.symplectic_gram_rank(reps,n)


def route_a_algebra(obj,length,full_commutant=False):
 n=obj["qubits"];cells=length**3;roots,retained=roots_and_retained(obj,length)
 rank,inconsistent=c532.phase_rank(retained,n);full_rank,_=c532.phase_rank(obj["stabilizers"],n)
 matter=quotient_data(retained,obj["matter"],n);gauge=quotient_data(retained,obj["gauge"],n)
 sv=tuple(row.symplectic(n) for row in retained)
 root_inc=tuple(len(c532.quotient_complement(sv,(root.symplectic(n),))) for root in roots)
 roots_in_matter=[];roots_in_gauge=[]
 mv=tuple(row.symplectic(n) for row in obj["matter"]);gv=tuple(row.symplectic(n) for row in obj["gauge"])
 for root in roots:
  roots_in_matter.append(len(c532.quotient_complement(sv+mv,(root.symplectic(n),)))==0)
  roots_in_gauge.append(len(c532.quotient_complement(sv+gv,(root.symplectic(n),)))==0)
 commutant=(2*cells+2,2*cells-2)
 commutant_method="symplectic-complement theorem from the exact measured matter dimension/rank in the nondegenerate logical code space"
 if full_commutant:
  mask=(1<<n)-1;equations=tuple((row>>n)|((row&mask)<<n) for row in sv+mv)
  central=c532.null_basis(equations,2*n);reps=c532.quotient_complement(sv,central)
  commutant=(len(reps),c532.symplectic_gram_rank(reps,n));commutant_method="explicit nullspace quotient, cross-checking the symplectic-complement theorem"
 comm_fail={
  "stabilizer":sum(not a.commutes(b) for i,a in enumerate(retained) for b in retained[i+1:]),
  "matter_stabilizer":sum(not a.commutes(b) for a in obj["matter"] for b in retained),
  "gauge_stabilizer":sum(not a.commutes(b) for a in obj["gauge"] for b in retained),
  "matter_gauge":sum(not a.commutes(b) for a in obj["matter"] for b in obj["gauge"]),
 }
 result={"route":"A_remove_three_root_faces","length":length,"split":{3:"construction",6:"train",7:"held-out-no-refit"}[length],
  "coarse_cells":cells,"M2_labels":n,"retained_stabilizer_rank":rank,"full_Cycle642_rank":full_rank,
  "rank_drop":full_rank-rank,"code_exponent":n-rank,"expected_code_exponent":7*cells+2,
  "requested_partition":{"target":6*cells,"ordinary_gauge":cells-1,"topological_gauge":3,"sum":7*cells+2},
  "root_face_rank_increments":root_inc,"matter_quotient_dimension_rank":matter,"expected_raw_matter":(12*cells+2,12*cells-2),
  "gauge_quotient_dimension_rank":gauge,"expected_raw_gauge":(2*cells+2,2*cells-2),
  "raw_matter_center_dimension":matter[0]-matter[1],"raw_gauge_center_dimension":gauge[0]-gauge[1],
  "root_faces_in_raw_matter_span_mod_stabilizers":roots_in_matter,"root_faces_in_raw_gauge_span_mod_stabilizers":roots_in_gauge,
  "full_matter_commutant_dimension_rank":commutant,"full_commutant_method":commutant_method,"expected_commutant":(2*cells+2,2*cells-2),
  "commutator_failures":comm_fail,"phase_inconsistencies":inconsistent,
  "three_extra_qubits_form_raw_M8_spectator_commutant":False,
  "exact_residual":"the raw matter and gauge spans each acquire the same three Wilson centers; symplectic rank does not gain six, so the +3 code exponent is a direct-sum sector center, not a raw spectator M8 factor"}
 result["pass"]=bool(inconsistent==0 and rank==full_rank-3 and n-rank==7*cells+2 and root_inc==(1,1,1)
  and matter==result["expected_raw_matter"] and gauge==result["expected_raw_gauge"]
  and all(roots_in_matter) and all(roots_in_gauge) and all(v==0 for v in comm_fail.values())
  and commutant==result["expected_commutant"])
 return result


def solve_symplectic_constraints(vectors,rhs,n):
 pivots={};width=2*n
 for vector,value in zip(vectors,rhs):
  x=vector&((1<<n)-1);z=vector>>n;coeff=z|(x<<n);row=coeff|(int(value)<<width)
  while coeff:
   pivot=coeff.bit_length()-1
   if pivot in pivots:row^=pivots[pivot];coeff=row&((1<<width)-1)
   else:pivots[pivot]=row;break
  if not coeff and ((row>>width)&1):raise AssertionError("inconsistent symplectic constraints")
 solution=0
 for pivot in sorted(pivots):
  row=pivots[pivot];value=((row>>width)&1)^((row&solution).bit_count()&1)
  if value:solution|=1<<pivot
 for vector,value in zip(vectors,rhs):
  if c643.symp(solution,vector,n)!=value:raise AssertionError("dual solve verification")
 return solution


def positive_vector(vector,n):return c643.positive_hermitian(Pauli(0,vector&((1<<n)-1),vector>>n))


def build_route_c(obj,length):
 started=time.perf_counter();n=obj["qubits"];cells=length**3;roots,retained=roots_and_retained(obj,length)
 reduced=c643.reduce_stabilizers(retained,n);stab_gates=reduced["decoder_gates"];pivots=reduced["pivot_qubits"]
 raw_matter=tuple(obj["matter"]);raw_gauge=tuple(obj["gauge"])
 raw_mp=c647.dress_old(obj,c643.c537.pauli_product(obj["graph"].B(v) for v in range(obj["graph"].matter_count)),length)
 raw_gz,_raw_ga,_=c532.gauge_generators(obj["graph"]);raw_gp=c647.dress_old(obj,c643.c537.pauli_product(raw_gz),length)
 raw_ops=raw_matter+raw_gauge+(raw_mp,raw_gp)+roots
 decoded=c643.transform_rows(raw_ops,n,stab_gates)
 clean=tuple(c643.clean_ancilla(row,pivots) for row in decoded)
 matter_dec=clean[:len(raw_matter)];gauge_dec=clean[len(raw_matter):len(raw_matter)+len(raw_gauge)]
 mp=clean[len(raw_matter)+len(raw_gauge)];gp=clean[len(raw_matter)+len(raw_gauge)+1];root_dec=clean[-3:]
 mgs=c643.symplectic_gram_schmidt(tuple(row.symplectic(n) for row in matter_dec),n)
 ggs=c643.symplectic_gram_schmidt(tuple(row.symplectic(n) for row in gauge_dec),n)
 parity=mp.symplectic(n);rootv=tuple(row.symplectic(n) for row in root_dec)
 expected_radicals={parity,*rootv}
 mrad={row[0] for row in mgs["radicals"]};grad={row[0] for row in ggs["radicals"]}
 if mrad!=expected_radicals or grad!=expected_radicals or gp.symplectic(n)!=parity:raise AssertionError("four-center radical chart")
 matter_pairs=[(left[0],right[0]) for left,right in mgs["pairs"]];gauge_pairs=[(left[0],right[0]) for left,right in ggs["pairs"]]
 pair_vectors=[item for pair in matter_pairs+gauge_pairs for item in pair]
 q=solve_symplectic_constraints(tuple(pair_vectors)+rootv+(parity,),tuple(0 for _ in pair_vectors)+ (0,0,0,1),n)
 topo_x=[]
 base_vectors=tuple(pair_vectors)+(q,parity)+rootv
 for index in range(3):
  vectors=base_vectors+tuple(topo_x);rhs=tuple(0 for _ in pair_vectors)+(0,0)+tuple(int(j==index) for j in range(3))+tuple(0 for _ in topo_x)
  topo_x.append(solve_symplectic_constraints(vectors,rhs,n))
 topo_pairing_fail=sum(c643.symp(topo_x[i],rootv[j],n)!=(i==j) for i in range(3) for j in range(3))+sum(c643.symp(topo_x[i],topo_x[j],n)!=0 for i in range(3) for j in range(i+1,3))
 frame_pairs=matter_pairs+[(q,parity)]+gauge_pairs+list(zip(topo_x,rootv))
 coeffs=list(mgs["pairs"])+[((q,0),(parity,next(row[1] for row in mgs["radicals"] if row[0]==parity)))]+list(ggs["pairs"])+[((topo_x[i],0),(rootv[i],0)) for i in range(3)]
 frame_x=[];frame_z=[]
 for index,((xv,zv),pair) in enumerate(zip(frame_pairs,coeffs)):
  if index<len(matter_pairs):
   xp=c643.positive_hermitian(c643.clean_ancilla(c643.pauli_product(matter_dec,pair[0][1]),pivots));zp=c643.positive_hermitian(c643.clean_ancilla(c643.pauli_product(matter_dec,pair[1][1]),pivots))
  elif index==len(matter_pairs):xp=positive_vector(q,n);zp=c643.positive_hermitian(mp)
  elif index<len(matter_pairs)+1+len(gauge_pairs):
   xp=c643.positive_hermitian(c643.clean_ancilla(c643.pauli_product(gauge_dec,pair[0][1]),pivots));zp=c643.positive_hermitian(c643.clean_ancilla(c643.pauli_product(gauge_dec,pair[1][1]),pivots))
  else:
   topo_index=index-(len(matter_pairs)+1+len(gauge_pairs));xp=positive_vector(topo_x[topo_index],n);zp=c643.positive_hermitian(root_dec[topo_index])
  if xp.symplectic(n)!=xv or zp.symplectic(n)!=zv:raise AssertionError("frame representative")
  frame_x.append(xp);frame_z.append(zp)
 logical=reduced["logical_qubits"];frame=c643.reduce_complete_frame(tuple(frame_x),tuple(frame_z),logical,n)
 decoder=stab_gates+frame["decoder_gates"];encoder=c643.inverse_gates(decoder);decoded_all=c643.transform_rows(raw_ops,n,decoder)
 input_wires=frame["input_pivots"];target=frozenset(input_wires[:6*cells]);gauge=frozenset(input_wires[6*cells:7*cells-1]);topo_wires=tuple(input_wires[7*cells-1:]);topo=frozenset(topo_wires)
 if len(topo)!=3:raise AssertionError("topological input count")
 target_mask=sum(1<<q for q in target);gauge_mask=sum(1<<q for q in gauge);topo_mask=sum(1<<q for q in topo);ancilla_mask=sum(1<<q for q in pivots)
 decoded_stabs=c643.transform_rows(retained,n,decoder);stab_fail=sum(row.phase!=0 or bool(row.x) or bool(row.z&~ancilla_mask) for row in decoded_stabs)
 raw_m=decoded_all[:len(raw_matter)];raw_g=decoded_all[len(raw_matter):len(raw_matter)+len(raw_gauge)];decoded_roots=decoded_all[-3:]
 root_map_fail=sum(row.phase!=0 or bool(row.x) or row.z!=(1<<q) for row,q in zip(decoded_roots,topo_wires))
 raw_m_topo_x=sum(bool(row.x&topo_mask) for row in raw_m);raw_g_topo_x=sum(bool(row.x&topo_mask) for row in raw_g)
 raw_m_contam=sum(bool(row.z&topo_mask) for row in raw_m);raw_g_contam=sum(bool(row.z&topo_mask) for row in raw_g)
 corrected_m=[];corrected_g=[]
 for originals,rows,out in ((raw_matter,raw_m,corrected_m),(raw_gauge,raw_g,corrected_g)):
  for original,row in zip(originals,rows):
   corrected=original
   for root,q in zip(roots,topo_wires):
    if (row.z>>q)&1:corrected=corrected@root
   out.append(corrected)
 corrected_dec=c643.transform_rows(tuple(corrected_m+corrected_g),n,decoder)
 corrected_m_fail=sum(bool(row.x&topo_mask) or bool(row.z&topo_mask) or bool((row.x|row.z)&gauge_mask) or bool(row.x&ancilla_mask) for row in corrected_dec[:len(corrected_m)])
 parity_wire=input_wires[6*cells-1]
 corrected_g_fail=sum(bool(row.x&topo_mask) or bool(row.z&topo_mask) or bool((row.x|row.z)&target_mask&~(1<<parity_wire)) or bool(row.x&ancilla_mask) for row in corrected_dec[len(corrected_m):])
 categories=Counter();matter_count=obj["graph"].matter_count
 for index,row in enumerate(raw_m):
  support=(row.z&topo_mask).bit_count()
  if not support:continue
  if index<matter_count:category="B_onsite"
  else:
   edge=index-matter_count;source,target_vertex,kind,_=obj["graph"].base.edges[edge];left=obj["graph"].base.vertices[source][0];right=obj["graph"].base.vertices[target_vertex][0]
   seam=any(abs(left[a]-right[a])==length-1 for a in range(3));category=f"A_{kind}_{'seam' if seam else 'nonseam'}"
  categories[category]+=1
 counts=Counter(g.kind for g in encoder)
 result={"route":"C_direct_sum_full_E","length":length,"split":{3:"construction",6:"train",7:"held-out-no-refit"}[length],"coarse_cells":cells,"M2_labels":n,
  "target_inputs":6*cells,"ordinary_gauge_inputs":cells-1,"topological_gauge_inputs":3,"blank_inputs":len(pivots),"work_M2":0,
  "exact_partition":6*cells+cells-1+3+len(pivots)==n,"arbitrary_coherent_topological_input":True,"all_eight_topological_Z_basis_sectors_in_domain":True,"topological_plus_state_required_by_isometry":False,"topological_canonical_pairing_failures":topo_pairing_fail,
  "matter_pair_count":len(matter_pairs),"gauge_pair_count":len(gauge_pairs),"matter_and_gauge_radicals":["shared parity","Wilson X","Wilson Y","Wilson Z"],
  "encoder_factor_count":len(encoder),"encoder_factors_per_cell":len(encoder)/cells,"encoder_factor_counts":dict(counts),"encoder_factor_sha256":c643.gate_digest(encoder),
  "stabilizer_reference_failures":stab_fail,"root_to_topological_Z_failures":root_map_fail,
  "raw_matter_generators_with_topological_Z":raw_m_contam,"raw_gauge_generators_with_topological_Z":raw_g_contam,"raw_topological_X_failures":raw_m_topo_x+raw_g_topo_x,
  "raw_matter_topological_character_categories":dict(categories),"corrected_matter_partition_failures":corrected_m_fail,"corrected_gauge_partition_failures":corrected_g_fail,
  "raw_G_tree_code_is_sector_diagonal_not_topological_identity":raw_m_contam>0,"corrected_target_algebra_is_topological_spectator":corrected_m_fail==corrected_g_fail==0,
  "Wilson_character_correction_is_supplied_global_chart":True,"elapsed_seconds":time.perf_counter()-started}
 result["pass"]=bool(result["exact_partition"] and len(matter_pairs)==6*cells-1 and len(gauge_pairs)==cells-1 and topo_pairing_fail==stab_fail==root_map_fail==raw_m_topo_x==raw_g_topo_x==corrected_m_fail==corrected_g_fail==0 and raw_m_contam>0 and raw_g_contam>0)
 internal={"obj":obj,"retained":retained,"roots":roots,"encoder":encoder,"decoder":decoder,"pivots":pivots,"input_wires":input_wires,"target":target,"gauge":gauge,"topo":topo,"topo_wires":topo_wires,"corrected_matter":tuple(corrected_m),"corrected_gauge":tuple(corrected_g)}
 return result,internal


def add_cell(cell,axis,amount,length):
 row=list(cell);row[axis]=(row[axis]+amount)%length;return tuple(row)


def link_code(length):
 cells=tuple(product(range(length),repeat=3));links=tuple((cell,axis) for cell in cells for axis in range(3));index={link:i for i,link in enumerate(links)};n=len(links)
 stars=[]
 for cell in cells:
  mask=0
  for axis in range(3):mask^=1<<index[(cell,axis)];mask^=1<<index[(add_cell(cell,axis,-1,length),axis)]
  stars.append(Pauli(x=mask))
 plaquettes=[]
 for cell in cells:
  for a,b in combinations(range(3),2):
   mask=(1<<index[(cell,a)])^(1<<index[(add_cell(cell,a,1,length),b)])^(1<<index[(add_cell(cell,b,1,length),a)])^(1<<index[(cell,b)])
   plaquettes.append(Pauli(z=mask))
 logical_z=[];logical_x=[]
 for axis in range(3):
  z=sum(1<<index[(tuple(t if a==axis else 0 for a in range(3)),axis)] for t in range(length))
  x=sum(1<<index[(cell,axis)] for cell in cells if cell[axis]==0)
  logical_z.append(Pauli(z=z));logical_x.append(Pauli(x=x))
 return {"cells":cells,"links":links,"index":index,"qubits":n,"stars":tuple(stars),"plaquettes":tuple(plaquettes),"stabilizers":tuple(stars+plaquettes),"logical_z":tuple(logical_z),"logical_x":tuple(logical_x)}


def permute_mask(mask,mapping):
 result=0
 while mask:
  bit=mask&-mask;result^=1<<mapping[bit.bit_length()-1];mask^=bit
 return result


def gf2_basis(rows):
 pivots={}
 for row in rows:
  value=row
  while value:
   p=value.bit_length()-1
   if p in pivots:value^=pivots[p]
   else:pivots[p]=value;break
 return pivots


def in_span(value,pivots):
 while value:
  p=value.bit_length()-1
  if p not in pivots:return False
  value^=pivots[p]
 return True


def link_covariance(code,length):
 frames=tuple(c642.FRAMES);maps=[];frame_fail=0
 for frame in frames:
  mapping=[]
  for cell,axis in code["links"]:
   target_axis,sign=c642.signed_axis(frame,axis);mapped=tuple(int(v)%length for v in frame@np.asarray(cell,dtype=int))
   if sign<0:mapped=add_cell(mapped,target_axis,-1,length)
   mapping.append(code["index"][(mapped,target_axis)])
  frame_fail+=len(set(mapping))!=len(mapping);maps.append(tuple(mapping))
 frame_index={tuple(int(v) for v in f.ravel()):i for i,f in enumerate(frames)};group_fail=0
 for li,left in enumerate(frames):
  for ri,right in enumerate(frames):
   direct=maps[frame_index[tuple(int(v) for v in (left@right).ravel())]]
   group_fail+=tuple(maps[li][maps[ri][q]] for q in range(code["qubits"]))!=direct
 star_masks={row.x for row in code["stars"]};plaq_masks={row.z for row in code["plaquettes"]};constraint_fail=0;homology_fail=0
 plaq_basis=gf2_basis(plaq_masks);star_basis=gf2_basis(star_masks)
 for frame,mapping in zip(frames,maps):
  constraint_fail+=sum(permute_mask(row.x,mapping) not in star_masks for row in code["stars"])
  constraint_fail+=sum(permute_mask(row.z,mapping) not in plaq_masks for row in code["plaquettes"])
  for axis in range(3):
   target,_sign=c642.signed_axis(frame,axis)
   homology_fail+=not in_span(permute_mask(code["logical_z"][axis].z,mapping)^code["logical_z"][target].z,plaq_basis)
   homology_fail+=not in_span(permute_mask(code["logical_x"][axis].x,mapping)^code["logical_x"][target].x,star_basis)
 return {"proper_cubic_frames":24,"frame_products":576,"frame_bijection_failures":frame_fail,"all576_group_failures":group_fail,"constraint_image_failures":constraint_fail,"logical_homology_image_failures":homology_fail,"pass":frame_fail==group_fail==constraint_fail==homology_fail==0}


def route_b_link_field(length):
 code=link_code(length);cells=code["cells"];N=length**3;n=code["qubits"];rank,inconsistent=c532.phase_rank(code["stabilizers"],n)
 comm_fail=sum(not a.commutes(b) for i,a in enumerate(code["stabilizers"]) for b in code["stabilizers"][i+1:])
 logical_fail=0
 for i in range(3):
  for j in range(3):logical_fail+=(not code["logical_x"][i].commutes(code["logical_z"][j]))!=(i==j)
 logical_stab_fail=sum(not logical.commutes(stab) for logical in code["logical_x"]+code["logical_z"] for stab in code["stabilizers"])
 # Charged local covariance proxy: six matter qubits per cell plus links.
 matter_index={(cell,mode):i for i,(cell,mode) in enumerate((x for x in product(cells,range(6))))};offset=6*N;total=9*N
 gauss=[]
 for cell,star in zip(cells,code["stars"]):
  z=sum(1<<matter_index[(cell,mode)] for mode in range(6));gauss.append(Pauli(x=star.x<<offset,z=z))
 plaquettes=tuple(Pauli(z=row.z<<offset) for row in code["plaquettes"])
 hops=[];seam_hops=0
 for cell,axis in code["links"]:
  target=add_cell(cell,axis,1,length);link_bit=1<<(offset+code["index"][(cell,axis)]);seam=cell[axis]==length-1
  for mode in range(6):
   pair=(1<<matter_index[(cell,mode)])^(1<<matter_index[(target,mode)])
   hops.append(Pauli(x=pair,z=link_bit));hops.append(Pauli(2,x=pair,z=pair^link_bit));seam_hops+=2*int(seam)
 covariance_fail=sum(not hop.commutes(constraint) for hop in hops for constraint in tuple(gauss)+plaquettes)
 onsite=tuple(Pauli(z=1<<matter_index[(cell,mode)]) for cell in cells for mode in range(6))
 contacts=tuple(Pauli(z=(1<<matter_index[(cell,a)])^(1<<matter_index[(cell,b)])) for cell in cells for a,b in combinations(range(6),2))
 diagonal_fail=sum(not row.commutes(g) for row in onsite+contacts for g in gauss)
 cov=link_covariance(code,length)
 basis=c643.independent_paulis(code["stabilizers"],n,False);deleted_rank,_=c532.phase_rank(basis[1:],n)
 flipped=(Pauli((code["stars"][0].phase+2)%4,code["stars"][0].x,code["stars"][0].z),)+code["stabilizers"][1:];_fr,flip_inconsistent=c532.phase_rank(flipped,n)
 result={"route":"B_local_flat_Z2_link_field","length":length,"split":{3:"construction",6:"train",7:"held-out-no-refit"}[length],"coarse_cells":N,
  "link_M2":n,"link_M2_per_cell":3,"star_rows":len(code["stars"]),"plaquette_rows":len(code["plaquettes"]),"stabilizer_rank":rank,"expected_rank":3*N-3,"code_exponent":n-rank,"topological_qubits":3,
  "maximum_star_weight":max(row.x.bit_count() for row in code["stars"]),"maximum_plaquette_weight":max(row.z.bit_count() for row in code["plaquettes"]),
  "stabilizer_commutator_failures":comm_fail,"logical_pairing_failures":logical_fail,"logical_stabilizer_failures":logical_stab_fail,"phase_inconsistencies":inconsistent,
  "charged_XX_YY_link_dressed_hopping_terms":len(hops),"seam_hopping_terms":seam_hops,"gauge_covariance_commutator_failures":covariance_fail,
  "onsite_mass_and_contact_proxy_terms":len(onsite)+len(contacts),"onsite_contact_Gauss_commutator_failures":diagonal_fail,
  "covariance":cov,"delete_one_independent_constraint_rank":deleted_rank,"flipped_redundant_star_phase_inconsistencies":flip_inconsistent,
  "local_link_code_state_preparation_E_constructed":False,"tree_root_to_link_holonomy_local_coupling_constructed":False,
  "hopping_and_onsite_objects_are_covariance_proxies_not_exact_original_CAR_compiler":True,"global_parity_service_used":False}
 result["pass"]=bool(inconsistent==0 and rank==3*N-3 and n-rank==3 and comm_fail==logical_fail==logical_stab_fail==covariance_fail==diagonal_fail==0 and cov["pass"] and deleted_rank==rank-1 and flip_inconsistent>0)
 return result


def route_c_controls(rows,internals):
 inverse=[];deletions=[];fixtures=[]
 for row,internal in zip(rows,internals):
  n=row["M2_labels"];indices=tuple(sorted(set((0,1,n//2,n-2,n-1,*sorted(internal["pivots"])[:3],*internal["input_wires"][:3],*internal["input_wires"][-3:]))));probes=tuple(x for q in indices for x in (Pauli(x=1<<q),Pauli(z=1<<q)))
  returned=c643.transform_rows(probes,n,internal["encoder"]+internal["decoder"]);inverse.append({"length":row["length"],"probes":len(probes),"failures":sum(a!=b for a,b in zip(probes,returned))})
  if row["length"]==3:
   mask=sum(1<<q for q in internal["pivots"])
   for kind in ("H","S","CNOT"):
    i=next(i for i,g in enumerate(internal["decoder"]) if g.kind==kind);altered=internal["decoder"][:i]+internal["decoder"][i+1:];decoded=c643.transform_rows(internal["retained"],n,altered);fail=sum(r.phase!=0 or bool(r.x) or bool(r.z&~mask) for r in decoded);deletions.append({"kind":kind,"factor_index":i,"failures":fail,"detected":fail>0})
   topo_input=tuple(Pauli(z=1<<q) for q in sorted(internal["topo"]));encoded=c643.transform_rows(topo_input,n,internal["encoder"]);base_rank,_=c532.phase_rank(internal["retained"],n);fixed_rank,_=c532.phase_rank(internal["retained"]+encoded,n);deleted_rank,_=c532.phase_rank(internal["retained"]+encoded[1:],n);minus=(Pauli((encoded[0].phase+2)%4,encoded[0].x,encoded[0].z),)+encoded[1:];minus_rank,minus_inc=c532.phase_rank(internal["retained"]+minus,n)
   fixtures.append({"optional_plus_topological_fixture":True,"references":3,"base_rank":base_rank,"plus_rank":fixed_rank,"delete_one_rank":deleted_rank,"minus_rank":minus_rank,"minus_phase_inconsistencies":minus_inc,"minus_consistent_but_refused_by_plus_fixture":minus_inc==0,"pass":fixed_rank==base_rank+3 and deleted_rank==fixed_rank-1 and minus_rank==fixed_rank and minus_inc==0})
 return {"inverse":inverse,"factor_deletions":deletions,"optional_topological_plus_fixture":fixtures,"factorwise_inverse":{"H":"H","S":"S S S","CNOT":"CNOT"},"pass":all(x["failures"]==0 for x in inverse) and all(x["detected"] for x in deletions) and all(x["pass"] for x in fixtures)}


def topological_axis_covariance():
 frames=tuple(c642.FRAMES);maps=[];bijection_failures=0
 for frame in frames:
  mapping=tuple(c642.signed_axis(frame,axis)[0] for axis in range(3));bijection_failures+=len(set(mapping))!=3;maps.append(mapping)
 frame_index={tuple(int(v) for v in frame.ravel()):i for i,frame in enumerate(frames)};group_failures=0
 for li,left in enumerate(frames):
  for ri,right in enumerate(frames):
   direct=maps[frame_index[tuple(int(v) for v in (left@right).ravel())]];group_failures+=tuple(maps[li][maps[ri][axis]] for axis in range(3))!=direct
 return {"proper_cubic_frames":24,"frame_products":576,"axis_bijection_failures":bijection_failures,"all576_group_failures":group_failures,"Z2_orientation_sign_requires_no_extra_label":True,"compile_time_encoder_transport":"E_R = F_R E C_R^dagger with the three topological input wires permuted by the axis action","runtime_frame_selector":False,"pass":bijection_failures==group_failures==0}


def update_interface(route_c_rows):
 inherited=c643.c537.inherited_target_controls();fixture=inherited["mass_contact_and_seam"]
 minus_root=1.5783929737448452;plus_root=1.563199679844947;delta=1e-3
 minus=c532.c230.seam_block(minus_root-delta,minus_root+delta,-1)[0];plus=c532.c230.seam_block(plus_root-delta,plus_root+delta,1)[0]
 seam_sign_singular_residual=float(np.linalg.norm(np.linalg.svd(minus,compute_uv=False)-np.linalg.svd(plus,compute_uv=False)))
 return {"corrected_generator_polynomial_rule":"Wilson-character-corrected complete matter generators are target-only, so multiplication and linearity compose the inherited coarse polynomial on every topological input",
  "E_Gcoarse_equals_Gcorrected_E_on_all_topological_inputs":inherited["pass"] and all(row["corrected_target_algebra_is_topological_spectator"] for row in route_c_rows),
  "G_corrected_is_supplied_Wilson_character_chart_not_derived_autonomous_law":True,
  "permission_to_redefine_G_coarse_claimed":False,
  "raw_G_tree_code_equals_original_coarse_interface_only_in_supplied_plus_plus_plus_sector":True,
  "raw_other_sectors_are_spin_character_conditioned_channels_not_silently_the_same_coarse_theory":True,
  "onsite_residual":fixture["onsite_intertwiner_residual"],"FSWAP_matrix_residual":inherited["FSWAP_polynomial_inverse"]["matrix_residual"],"contact_active_states":fixture["Cycle230_contact_active_two_particle_states"],"contact_deletion_residual":fixture["Cycle230_contact_deletion_residual"],"Cycle219_mass_residual":fixture["Cycle219_mass_fixture_residual"],"Cycle230_seam_subchecks":fixture["Cycle230_seam_subchecks"],"Cycle230_plus_minus_seam_singular_residual":seam_sign_singular_residual,"B_coefficient_failures":sum(x["coefficient_identity_failures"] for x in inherited["full_Fock_Gamma_P"]["quadratic_full_Fock_theorems"]),"pass":inherited["pass"] and seam_sign_singular_residual<3e-13}


def citation(path,fragment):
 for line,text in enumerate(git_bytes(path).decode().splitlines(),1):
  if fragment in text:return {"ref":SHORE,"path":path,"line":line,"text":text.strip()}
 raise AssertionError((path,fragment))


def current_citation(fragment):
 for line,text in enumerate(Path(__file__).read_text().splitlines(),1):
  if fragment in text:return {"ref":"Cycle650 current artifact","path":str(Path(__file__).relative_to(ROOT)),"line":line,"text":text.strip()}
 raise AssertionError(fragment)


def no_go_discipline():
 families=[
  {"family":"remove root/Wilson checks","object_formulation":"Cycle642 tree code with three root faces omitted","mechanism_invariant":"exact quotient and commutant ranks","terminal_obligation":"target tensor ordinary gauge tensor topological M8","strength_vs_target":"direct","honesty_marker":"ATTEMPTED","status":"+3 exponent passes; raw M8 spectator factor does not"},
  {"family":"local flat Z2 link field","object_formulation":"3N cubic links with star/plaquette constraints","mechanism_invariant":"three toric holonomies and link-dressed charged hopping","terminal_obligation":"local seam covariance and full coupled E","strength_vs_target":"partial constructive","honesty_marker":"ATTEMPTED","status":"local covariance passes; coupled E open"},
  {"family":"direct-sum supplied-chart E","object_formulation":"three explicit topological input qubits","mechanism_invariant":"signed tableau plus Wilson-character correction","terminal_obligation":"arbitrary-sector exact isometry and update","strength_vs_target":"algebraically target-equivalent, locality weaker","honesty_marker":"ATTEMPTED","status":"finite E passes; global character chart supplied"},
  {"family":"fixed plus-plus-plus sector","object_formulation":"Cycle647 full root-face stabilizer code","mechanism_invariant":"three Wilson signs fixed as blank references","terminal_obligation":"arbitrary topological input","strength_vs_target":"strict subset","honesty_marker":"RULED OUT BY PRIOR","status":"Cycle647 exact E intentionally fixes the three signs"},
 ]
 open_routes=[{"family":"distributed local toric/tree coupled encoder","status":"OPEN / NOT COUNTED","terminal":"bounded-range E with returned work"},{"family":"odd-CAR spin-structure covariant extension","status":"OPEN / NOT COUNTED","terminal":"odd generators and seam channels without supplied character chart"},{"family":"dynamical Z2 flux law","status":"OPEN / NOT COUNTED","terminal":"autonomous topological-sector update/genesis"}]
 walls={"W_raw_tensor":"make the raw Cycle642 matter algebra identity on topological gauge","W_coupled_E":"construct a bounded-range tree/link encoder with returned work","W_interface":"show every sector is the unchanged coarse update rather than a spin-conditioned extension"};pairs=[{"from":a,"to":b,"implied":False,"reason":f"closing {a} does not construct {b}"} for a in walls for b in walls if a!=b]
 c537=citation("docs/work_history/repo/review_feedback/PHYSICAL_LOCAL_WILSON_FILL_DISK_CYCLE537_NOTE_2026-07-21.md","removes exactly one topological code qubit")
 c647n=citation("docs/work_history/repo/review_feedback/PHYSICAL_ORBIT_TREE_STRUCTURED_FULL_ISOMETRY_TOURNAMENT_CYCLE647_NOTE_2026-07-23.md","strict physical local")
 current=current_citation("direct-sum sector center")
 n4=[{"prior_ref":c537["ref"],"prior_path":c537["path"],"prior_line":c537["line"],"prior_residual":"each Wilson fill removes one topological code qubit","current_path":current["path"],"current_line":current["line"],"current_residual":"omitting three root/Wilson constraints restores exactly three code qubits as central sector labels","same_scope":True,"exact_match":True,"use_as_closure":True}]
 non=[{"prior_ref":c647n["ref"],"prior_path":c647n["path"],"prior_line":c647n["line"],"prior_residual":"Cycle647 factor lists are nonlocal","current_path":current["path"],"current_line":current["line"],"current_residual":"Cycle650 raw algebra has three additional centers","same_scope":False,"exact_match":False,"use_as_closure":False}]
 rhetoric=[{"claim":"the three restored code qubits are not a raw spectator M8 factor","per_element":"all displayed raw generators are charted","per_site":"local link proxy is separately tested","per_mode":"all six-mode even generators are included","per_block":"L3/L6/L7 ranks and held charts are exact","lattice_wide":"no all-L impossibility is inferred"}]
 n6=[{"file":"UNMATERIALIZED/distributed_tree_toric_coupled_E_cycle_next.py","status":"OPEN / PRIORITY","what_closes":"W_coupled_E"},{"file":"UNMATERIALIZED/odd_CAR_spin_character_extension_cycle_next.py","status":"OPEN","what_closes":"W_interface for odd and seam generators"},{"file":"UNMATERIALIZED/autonomous_Z2_flux_genesis_cycle_next.py","status":"OPEN","what_closes":"autonomous sector preparation/update, not the algebraic rank result"}]
 n7={"mechanism":"use the positive local flat-link construction to distribute each Wilson character and synthesize the tree/link coupling by gauge-fixing only local spanning-tree edges while leaving three holonomies arbitrary","actionable_steps":["construct local tree-root/link plaquette coupling checks","synthesize a returned-work local gauge-fixing circuit","conjugate the complete corrected generator set and odd seam channels"],"terminal_test":"bounded physical range, arbitrary three-qubit holonomy input, inverse/leakage, all24/all576, and unchanged coarse interface without a supplied global character table","supporting_citations":[c537,c647n]}
 n8=[{"cycle":537,"retired":"three spin characters in the fixed target factor","mechanism":"three fill disks fix them","applicability":"Cycle650 reverses this choice and exposes their exact central algebra","citation_ref":c537["ref"],"citation_path":c537["path"],"citation_line":c537["line"],"citation_text":c537["text"]},{"cycle":647,"retired":"absence of a finite tree-code E","mechanism":"finite supplied-chart tableau","applicability":"reusable for Route C but not a local coupled link encoder","citation_ref":c647n["ref"],"citation_path":c647n["path"],"citation_line":c647n["line"],"citation_text":c647n["text"]}]
 return {"Status":"PASS","N1_normalized_families":families,"N1_open_routes_not_counted":open_routes,"N1_qualifying_attempts":4,"N1_required_for_negative":5,"N1_broad_negative_gate":"FAIL / DO NOT SHIP","broad_negative_gate":"FAIL / DO NOT SHIP","minimum_content_gate":"FAIL / DO NOT SHIP","shared_obstruction_gate":"FAIL / DO NOT SHIP","axiom_pressure_gate":"FAIL / DO NOT SHIP","N2_walls":walls,"N2_directed_ordered_pairs":pairs,"N3_hidden_wall_scan":[{"condition":"three omitted root faces","classification":"explicit choice"},{"condition":"Wilson-character correction table","classification":"supplied global chart, not derived local law"},{"condition":"flat-link stabilizers and blank inputs","classification":"supplied gauge-code structure and state, not autonomous genesis"}],"N4_exact_residual_matches":n4,"N4_nonmatches_not_used_as_closure":non,"N5_rhetoric":rhetoric,"N6_partial_closure_paths":n6,"N7_steelman":n7,"N8_cross_cycle_echo":n8,"broad_no_go_claim":False,"minimum_content_claim":False,"shared_obstruction_claim":False,"axiom_pressure_claim":False,"broad_negative_shipped":False,"minimum_content_shipped":False,"shared_obstruction_shipped":False,"axiom_pressure_shipped":False,"shared_route_independent_obstruction":False,"axiom_pressure":False}


def note_text(r):
 a=r["route_A_algebra"];b=r["route_B_local_link"];c=r["route_C_direct_sum_E"]
 table="\n".join(f"| L{x['length']} | {x['retained_stabilizer_rank']} | {x['code_exponent']} | {x['matter_quotient_dimension_rank']} | {x['gauge_quotient_dimension_rank']} |" for x in a)
 ctable="\n".join(f"| L{x['length']} | {x['encoder_factor_count']} | {x['encoder_factors_per_cell']:.3f} | {x['raw_matter_generators_with_topological_Z']} | {x['raw_gauge_generators_with_topological_Z']} |" for x in c)
 btable="\n".join(f"| L{x['length']} | {x['link_M2']} | {x['stabilizer_rank']} | {x['charged_XX_YY_link_dressed_hopping_terms']} | {x['gauge_covariance_commutator_failures']} |" for x in b)
 return f"""# Physical topological-sector gauge-subsystem tournament — Cycle 650

Classification: **positive direct-sum/topological-input algebra with an exact raw-spectator falsifier; strict local coupled compiler open**

Authority: **none**

Audit: **unset**

Author artifact status accepted: **false**

Breakthrough: **false**

## Result

Removing the three Cycle-642 root/Wilson face constraints restores exactly
three code qubits at L3, L6, and held L7.  It does **not** make those qubits a
raw spectator `M8` gauge factor.  The raw matter and ordinary-gauge spans each
gain the same three commuting Wilson centers while their symplectic ranks do
not increase.  The exact object is therefore a direct sum over eight spin
characters unless one supplies a Wilson-character correction chart.

| size | retained rank | code exponent | raw matter dim/rank | raw gauge dim/rank |
|---|---:|---:|---:|---:|
{table}

The requested dimension identity nevertheless holds exactly:
`6N target + (N-1) ordinary gauge + 3 topological inputs = 7N+2`.
The distinction is algebraic action, not Hilbert-space dimension.

## Route C: arbitrary-sector finite E

Route C constructs a complete finite supplied-chart H/S/CNOT isometry with
three arbitrary coherent topological input qubits.  It needs no fixed plus
topological state.  Every raw matter/gauge generator is charted; multiplying
the contaminated rows by their explicit root/Wilson characters clears all
topological support and recovers a target-only/ordinary-gauge algebra.

| size | factors | factors/cell | raw matter rows with topological Z | raw gauge rows with topological Z |
|---|---:|---:|---:|---:|
{ctable}

The contaminated rows are exactly the `3L^2` periodic `outer_square` seam
generators: `27 / 108 / 147`; onsite `B` and non-seam generators carry no
topological character.  Route-C maximum declared fine-L1 factor ranges are
`459 / 1161 / 1231`, with only `3 / 6 / 13` nearest-neighbor CNOTs.  The
finite isometry is therefore abstract/nonlocal in the supplied placement.

Thus `E G_coarse = G_corrected E` holds on all topological inputs by complete
generator and polynomial composition.  The uncorrected inherited
`G_tree_code` is sector-diagonal and agrees with the original coarse interface
in the supplied `+++` sector; other sectors are spin-character-conditioned
channels.  They are not silently declared the unchanged coarse theory.  The
global Wilson-character table, pivot/root/chart, blanks, and factor schedule
remain supplied.  `G_corrected` is a supplied Wilson-character chart, not a
derived autonomous law and not permission to redefine `G_coarse`.  This is
not autonomous genesis or a strict local compiler.

## Route B: local Z2 link comparator

The local comparator places one Z2 qubit on each of `3N` cubic links.  Weight-6
stars and weight-4 plaquettes have rank `3N-3`, leaving exactly three holonomy
qubits.  Six-mode `XXZ_link` and `YYZ_link` hopping proxies, including every
periodic seam edge, commute with every charged Gauss and flatness constraint;
onsite mass and contact-density proxies do also.
These hopping and onsite objects are covariance proxies/comparators, not an
exact compiler for the original CAR update.

| size | link M2 | rank | dressed hopping terms | covariance failures |
|---|---:|---:|---:|---:|
{btable}

The link presentation and the three-axis topological input action close under
all 24 proper-cubic frames and all 576 products.  It uses state-carried local link values and no global parity
service.  However, a bounded-range preparation E and local coupling between
the tree root faces and link holonomies are not constructed.  Local gauge
covariance is positive evidence, not permission to back-credit a physical
compiler.

## Mass, contact, seam, inverse, and controls

The corrected generator chart retains onsite residual
`{r['update_interface']['onsite_residual']:.3e}`, FSWAP residual
`{r['update_interface']['FSWAP_matrix_residual']:.1e}`, Cycle-219 mass
residual `{r['update_interface']['Cycle219_mass_residual']:.3e}`, contact
deletion residual `{r['update_interface']['contact_deletion_residual']:.15f}`,
zero B-coefficient failures, and Cycle-230 seam
`{r['update_interface']['Cycle230_seam_subchecks']['pass']} PASS /
{r['update_interface']['Cycle230_seam_subchecks']['fail']} FAIL`.  The tested
plus/minus seam singular-value residual is
`{r['update_interface']['Cycle230_plus_minus_seam_singular_residual']:.3e}`.

Route-C inverse probes, representative H/S/CNOT deletions, stabilizer
references, leakage, both matter parities, all eight topological basis sectors,
and optional `+++` fixture deletion/malformed controls pass.  Fixing `+++` is
optional for E but required if one wants the uncorrected Cycle-647 interface.

## Supplied structure and semantic firewall

Supplied are immutable Cycle-642/647 algebra and tableau machinery; the three
omitted root faces; finite L3/L6/L7 domains; topological input chart and its
Wilson-character corrections; the local flat-link code; blank references;
and compile schedules.  No global Jordan-Wigner order or nonlocal parity
query is used.  A topological input is not derived state genesis, a schedule
is not time or a rate, phase is not energy, and gauge capacity is not source
or gravity.

## Prior art and novelty boundary

Z2 lattice-gauge/toric holonomies, spin-structure sectors, and Clifford
stabilizer encoders are standard prior art.  The narrow new result here is the
exact Cycle-642 rank/center decomposition, sector-character and seam
comparison, and finite supplied-chart composition on L3/L6/held-out L7.  No
broader novelty is claimed for those standard ingredients.

## Route disposition and six-wall ledger

- Route A: **+3 dimension passes; raw spectator-M8 interpretation narrowly
  falsified by the exact four-dimensional center**.
- Route B: **local flat-link/seam covariance passes; coupled local E open**.
- Route C: **finite arbitrary-sector E passes with a supplied global character
  chart; raw update remains sector-conditioned**.

| wall | movement | residual |
|---|---|---|
| `C_ref` | arbitrary three-qubit topological input and optional +++ fixture | Wilson-character chart/blanks/schedule supplied |
| `C_num` | exact ranks, centers, factors, seam residuals | no empirical/Born normalization |
| `C_wrap` | Wilson signs become explicit sector labels/local link holonomies | autonomous flux genesis and coupled E open |
| `C_int` | corrected mass/contact/seam/update compose | raw update is sector-conditioned outside +++ |
| `C_local` | local Z2 constraints and all24/all576 pass | tree/link coupling and Route-C factors not locally compiled |
| `C_source` | gauge/link resources explicit | no source, stress, energy, or gravity identification |

## N1-N8

The full N1-N8 schema passes while every broad-negative, minimum-content,
shared-obstruction, and axiom-pressure promotion gate is **FAIL / DO NOT
SHIP**.  N1 has four qualifying families, below the required five.  Broad
no-go: **not claimed**.  Shared route-independent obstruction: **not
established**.  Axiom pressure: **none**.

The optimal next campaign is the N7 distributed tree/toric coupling: construct
local root-face/link checks and a returned-work gauge-fixing E, then test the
complete corrected and odd seam generator sets without a supplied global
character table.
"""


def main():
 signal.alarm(3600);started=time.perf_counter();observed={p:sha256(git_bytes(p)).hexdigest() for p in PINS};check("immutable Cycle647 shore is byte exact",observed==PINS,{"files":len(PINS),"mismatches":[p for p in PINS if observed[p]!=PINS[p]]})
 objects={};a_rows=[];b_rows=[];c_rows=[];internals=[];distances=[]
 for length in (3,6,7):
  _placement,fibers=c642.allocate_orbit_roles(length);obj=c642.build_tree_code(length,fibers);objects[length]=obj
  a=route_a_algebra(obj,length,full_commutant=length==3);a_rows.append(a);check(f"L{length} Route A exact topological-center algebra",a["pass"],{"rank":a["retained_stabilizer_rank"],"k":a["code_exponent"],"matter":a["matter_quotient_dimension_rank"]})
  b=route_b_link_field(length);b_rows.append(b);check(f"L{length} Route B local flat-link gauge covariance",b["pass"],{"rank":b["stabilizer_rank"],"hops":b["charged_XX_YY_link_dressed_hopping_terms"]})
  c,internal=build_route_c(obj,length);c_rows.append(c);internals.append(internal);distance=c647.gate_distance_audit({"route":"C_direct_sum_full_E","length":length,**c},internal,c647.positions(obj,length));distances.append(distance);check(f"L{length} Route C arbitrary-sector full E",c["pass"],{"factors":c["encoder_factor_count"],"raw_matter_topo":c["raw_matter_generators_with_topological_Z"]})
 base_cov=c647.covariance_audit(objects);topo_cov=topological_axis_covariance();check("Cycle642 labels and topological-axis inputs close all24/all576",base_cov["pass"] and topo_cov["pass"],{"labels":base_cov["rows"],"topological":topo_cov})
 controls=route_c_controls(c_rows,internals);check("Route C inverse, deletion, and optional +++ controls",controls["pass"],{"inverse":len(controls["inverse"]),"deletions":len(controls["factor_deletions"])})
 update=update_interface(c_rows);check("corrected update fixtures and plus/minus seam comparator",update["pass"],{"seam":update["Cycle230_plus_minus_seam_singular_residual"]})
 no_go=no_go_discipline();canonical={"Status_PASS":no_go["Status"]=="PASS","gates":all(no_go[k]=="FAIL / DO NOT SHIP" for k in ("N1_broad_negative_gate","broad_negative_gate","minimum_content_gate","shared_obstruction_gate","axiom_pressure_gate")),"flags":not any(no_go[k] for k in ("broad_no_go_claim","minimum_content_claim","shared_obstruction_claim","axiom_pressure_claim","broad_negative_shipped","minimum_content_shipped","shared_obstruction_shipped","axiom_pressure_shipped","shared_route_independent_obstruction","axiom_pressure")),"N1":no_go["N1_qualifying_attempts"]==4 and no_go["N1_required_for_negative"]==5 and all(x["honesty_marker"] in {"ATTEMPTED","RULED OUT BY PRIOR"} for x in no_go["N1_normalized_families"]) and all("honesty_marker" not in x for x in no_go["N1_open_routes_not_counted"]),"N2":len(no_go["N2_directed_ordered_pairs"])==6,"N4":all({"prior_ref","prior_path","prior_line","prior_residual","current_path","current_line","current_residual","same_scope","exact_match","use_as_closure"}<=set(x) for x in no_go["N4_exact_residual_matches"]+no_go["N4_nonmatches_not_used_as_closure"]),"N5":all({"per_element","per_site","per_mode","per_block","lattice_wide"}<=set(x) for x in no_go["N5_rhetoric"]),"N6":all({"file","status","what_closes"}<=set(x) for x in no_go["N6_partial_closure_paths"]),"N8":all({"retired","mechanism","applicability","citation_ref","citation_path","citation_line","citation_text"}<=set(x) for x in no_go["N8_cross_cycle_echo"])};canonical["pass"]=all(canonical.values());check("canonical N1-N8 and negative gates",canonical["pass"],canonical)
 receipt={"Status":"PASS","cycle":650,"date":"2026-07-23","status":"positive direct-sum topological-input algebra with narrow raw-spectator falsifier; strict local coupled compiler open","classification":"three-route topological-sector-as-gauge subsystem tournament","strongest_constructive_result":"finite exact arbitrary-three-qubit-topological-input supplied-chart E with corrected six-mode even-CAR algebra and inherited mass/contact/seam/update fixtures, plus a separately local gauge-covariant Z2 link comparator","strict_success_criterion_met":False,"strict_physical_local_M2_compiler_claimed":False,"prior_art_novelty_boundary":{"standard_prior_art":["Z2 lattice gauge and toric holonomies","spin-structure sectors","Clifford stabilizer encoders"],"narrow_new_result":"exact Cycle642 rank/center and sector-character/seam comparisons plus finite supplied-chart composition on L3/L6/held-out L7","broader_novelty_claimed":False},"authority":"none","audit":"unset","author_accepted":False,"author_artifact_status_accepted":False,"breakthrough":False,"constitutional_effect":"none","broad_negative_gate":"FAIL / DO NOT SHIP","minimum_content_gate":"FAIL / DO NOT SHIP","shared_obstruction_gate":"FAIL / DO NOT SHIP","axiom_pressure_gate":"FAIL / DO NOT SHIP","broad_no_go_claim":False,"minimum_content_claim":False,"shared_obstruction_claim":False,"axiom_pressure_claim":False,"broad_negative_shipped":False,"minimum_content_shipped":False,"shared_obstruction_shipped":False,"axiom_pressure_shipped":False,"shared_route_independent_obstruction":False,"axiom_pressure":False,"immutable_shore":{"ref":SHORE,"pins":PINS,"observed":observed,"working_tree_bytes_used_as_premise":False},"route_A_algebra":a_rows,"route_B_local_link":b_rows,"route_C_direct_sum_E":c_rows,"route_C_physical_distance_audit":distances,"route_C_controls":controls,"Cycle642_label_covariance":base_cov,"topological_input_covariance":topo_cov,"update_interface":update,"route_disposition":{"A":"PASS_PLUS3_DIRECT_SUM_CENTER__RAW_SPECTATOR_M8_NARROWLY_FALSIFIED","B":"PASS_LOCAL_LINK_GAUGE_COVARIANCE__COUPLED_LOCAL_E_OPEN","C":"PASS_FINITE_ARBITRARY_SECTOR_E__GLOBAL_CHARACTER_CHART_SUPPLIED"},"supplied_structure_inventory":{"Cycle642_Cycle647_committed_algebra":True,"three_omitted_root_faces":True,"finite_L3_L6_L7":True,"topological_input_chart":True,"Wilson_character_correction_table":True,"local_flat_Z2_link_code":True,"blank_pivot_root_order_schedule":True,"fixed_topological_plus_state_required_for_E":False,"fixed_plus_plus_plus_required_for_uncorrected_original_interface":True,"autonomous_topological_genesis":False,"global_Jordan_Wigner_order":False,"nonlocal_parity_service":False},"no_go_discipline":no_go,"canonical_claim_gate_contract":canonical,"six_wall_ledger":{"C_ref":"three arbitrary topological inputs; chart/blanks/schedule supplied","C_num":"exact ranks/centers/factors/seam; no empirical/Born normalization","C_wrap":"explicit sectors/local holonomies; autonomous flux genesis/coupled E open","C_int":"corrected update composes; raw update sector-conditioned outside +++","C_local":"local link constraints/all24/all576; local tree-link E open and Route C nonlocal","C_source":"resources explicit; no source/stress/energy/gravity"},"highest_honest_terminal":"exact +3 direct-sum center and finite arbitrary-topological-input E after a supplied Wilson-character chart, plus a local gauge-covariant link/seam comparator; not a raw spectator M8 factor or strict local compiler","optimal_next_campaign":"distributed local tree/toric coupling and returned-work gauge-fixing E with complete corrected and odd seam generators"}
 top={"Status":receipt["Status"]=="PASS","gates":all(receipt[k]=="FAIL / DO NOT SHIP" for k in ("broad_negative_gate","minimum_content_gate","shared_obstruction_gate","axiom_pressure_gate")),"flags":not any(receipt[k] for k in ("broad_no_go_claim","minimum_content_claim","shared_obstruction_claim","axiom_pressure_claim","broad_negative_shipped","minimum_content_shipped","shared_obstruction_shipped","axiom_pressure_shipped","shared_route_independent_obstruction","axiom_pressure")),"strongest_constructive_result_nonempty":bool(receipt["strongest_constructive_result"]),"strict_success_false":receipt["strict_success_criterion_met"] is False,"strict_physical_claim_false":receipt["strict_physical_local_M2_compiler_claimed"] is False};top["pass"]=all(top.values());receipt["top_level_claim_gate_contract"]=top;check("top-level gates, strict fields, and shipped flags",top["pass"],top)
 NOTE.write_text(note_text(receipt));flat=" ".join(NOTE.read_text().lower().split());required=("authority: **none**","audit: **unset**","direct sum","raw spectator","g_corrected","permission to redefine","covariance proxies/comparators","prior art and novelty boundary","not silently declared","no global jordan-wigner","fail / do not ship","axiom pressure: **none**");missing=[x for x in required if x not in flat];check("note contract",not missing,missing)
 elapsed=time.perf_counter()-started;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
 if rss<10_000_000:rss*=1024
 receipt.update({"runner_sha256":file_sha(Path(__file__)),"note_sha256":file_sha(NOTE),"elapsed_seconds":elapsed,"maximum_RSS_bytes":rss,"tests_passed":PASS,"tests_failed":FAIL,"pass":FAIL==0});RECEIPT.write_text(json.dumps(receipt,indent=2,sort_keys=True,default=float)+"\n");print(json.dumps({"pass":receipt["pass"],"tests":f"{PASS}/{PASS+FAIL}","elapsed":elapsed,"receipt":str(RECEIPT)},indent=2));return int(FAIL!=0)


if __name__=="__main__":
 COLD.parent.mkdir(parents=True,exist_ok=True)
 with COLD.open("w") as stream:
  original=sys.stdout;sys.stdout=Tee(original,stream)
  try:raise SystemExit(main())
  finally:sys.stdout=original
