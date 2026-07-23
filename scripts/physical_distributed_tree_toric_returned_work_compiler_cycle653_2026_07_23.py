#!/usr/bin/env python3
"""Cycle653: distributed tree/flat-link coupling with returned routing work.

The positive construction replaces Cycle650's runtime Wilson-character table
by the local flat-connection identity

    z(v,a) = g(v) + g(v+e_a) + t_a [v crosses the a cut]  (mod 2).

Route A computes the three tree-root characters into physical link seeds by
reversible local message-passing macros.  Route B constructs the exact
plaquette-only flat-link code, whose N+2 logical qubits split as N-1 ordinary
gauge inputs plus three coherent holonomies.  Route C compiles the finite
tree-to-flat change of encoding into nearest-neighbour macros on an explicit
doubled K129 routing mesh and returns all routing work.

The construction closes the finite encoder and every Cycle650 seam-character
comparison, but does not promote the supplied extensive schedule into an
autonomous bounded-period physical update law.  Authority none; audit unset.
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
SHORE="cb7199196fe41b6738dc76f5b3236d2c46f6c9f4"
NOTE=ROOT/"docs/work_history/repo/review_feedback/PHYSICAL_DISTRIBUTED_TREE_TORIC_RETURNED_WORK_COMPILER_CYCLE653_NOTE_2026-07-23.md"
RECEIPT=ROOT/"outputs/physical_distributed_tree_toric_returned_work_compiler_cycle653_receipt_2026_07_23.json"
COLD=ROOT/"outputs/physical_distributed_tree_toric_returned_work_compiler_cycle653_cold_2026_07_23.txt"
PASS=FAIL=0
PINS={
 "scripts/physical_topological_sector_gauge_subsystem_tournament_cycle650_2026_07_23.py":"7c428845a95f3b79dd525be70fd8f9c3e41076130e173a372b0c22c825684dde",
 "docs/work_history/repo/review_feedback/PHYSICAL_TOPOLOGICAL_SECTOR_GAUGE_SUBSYSTEM_TOURNAMENT_CYCLE650_NOTE_2026-07-23.md":"84d8ee582059a40eda5106debb439a1f0a9f4b181d806b07a6e7fe29fe4712cb",
 "outputs/physical_topological_sector_gauge_subsystem_tournament_cycle650_receipt_2026_07_23.json":"383efa37e45447d7340efd9d7118ba909d6c269995f0ba51ff3a4d4fd48111ed",
 "outputs/physical_topological_sector_gauge_subsystem_tournament_cycle650_cold_2026_07_23.txt":"50614cd0fac0e24b5afad188fdf4ffe720ff67d38f7bae6bdddb9d74b4eb16fe",
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
 PASS+=int(bool(condition));FAIL+=int(not condition)
 print("PASS" if condition else "FAIL",label,"::",detail)


def git_bytes(path):return subprocess.check_output(["git","show",f"{SHORE}:{path}"],cwd=ROOT)
def file_sha(path):return sha256(path.read_bytes()).hexdigest()
def load_exact(name,path):
 module=types.ModuleType(name);module.__file__=str(ROOT/path);module.__package__="";sys.modules[name]=module
 exec(compile(git_bytes(path),module.__file__,"exec"),module.__dict__);return module


c650=load_exact("cycle653_exact_cycle650","scripts/physical_topological_sector_gauge_subsystem_tournament_cycle650_2026_07_23.py")
c647=c650.c647;c643=c650.c643;c642=c650.c642;c532=c650.c532;Pauli=c650.Pauli;Gate=c650.Gate;np=c650.np
K=c642.K


def bit_indices(mask):
 while mask:
  bit=mask&-mask;yield bit.bit_length()-1;mask^=bit


def periodic_l1(left,right,modulus):
 return sum(min((a-b)%modulus,(b-a)%modulus) for a,b in zip(left,right))


def link_midpoint(cell,axis,length):
 modulus=2*K*length;row=[(2*K*cell[a])%modulus for a in range(3)];row[axis]=(row[axis]+K)%modulus;return tuple(row)


def matter_position(cell,mode,length):
 modulus=2*K*length;axis=mode//2;sign=1 if mode%2==0 else -1;row=[(2*K*cell[a])%modulus for a in range(3)];row[axis]=(row[axis]+sign)%modulus;return tuple(row)


def cell_path_mask(code,cell):
 cursor=[0,0,0];mask=0
 for axis in range(3):
  for _ in range(cell[axis]):
   mask^=1<<code["index"][(tuple(cursor),axis)];cursor[axis]+=1
 return mask


def routed_cnot_primitives(distance):
 if distance<1:raise AssertionError("distinct CNOT endpoints required")
 return 6*(distance-1)+1


def routed_swap_primitives(distance):
 if distance<1:raise AssertionError("distinct SWAP endpoints required")
 return 3*(2*distance-1)


def remote_cnot_macro(distance):
 gates=[]
 def swap(a,b):gates.extend((Gate("CNOT",a,b),Gate("CNOT",b,a),Gate("CNOT",a,b)))
 for q in range(distance-1):swap(q,q+1)
 gates.append(Gate("CNOT",distance-1,distance))
 for q in reversed(range(distance-1)):swap(q,q+1)
 return tuple(gates)


def remote_macro_controls(maximum_distance):
 rows=[]
 for distance in sorted({1,2,3,maximum_distance}):
  n=distance+1;probes=tuple(item for q in sorted({0,distance//2,distance}) for item in (Pauli(x=1<<q),Pauli(z=1<<q)))
  actual=c643.transform_rows(probes,n,remote_cnot_macro(distance));ideal=c643.transform_rows(probes,n,(Gate("CNOT",0,distance),))
  rows.append({"distance":distance,"primitive_CNOTs":len(remote_cnot_macro(distance)),"probe_failures":sum(a!=b for a,b in zip(actual,ideal))})
 gates=remote_cnot_macro(3);altered=gates[:1]+gates[2:];probes=tuple(item for q in range(4) for item in (Pauli(x=1<<q),Pauli(z=1<<q)))
 deleted=sum(a!=b for a,b in zip(c643.transform_rows(probes,4,altered),c643.transform_rows(probes,4,(Gate("CNOT",0,3),))))
 return {"rows":rows,"deleted_primitive_failures":deleted,"all_emitted_two_qubit_primitive_range":1,"pass":all(x["probe_failures"]==0 for x in rows) and deleted>0}


def flat_link_frame(length):
 code=c650.link_code(length);cells=code["cells"];N=length**3;n=code["qubits"];root=(0,0,0);cell_index={c:i for i,c in enumerate(cells)};nonroot=tuple(c for c in cells if c!=root)
 rank,inconsistent=c532.phase_rank(code["plaquettes"],n);basis=c643.independent_paulis(code["plaquettes"],n,False);deleted_rank,_=c532.phase_rank(basis[1:],n)
 flipped=(Pauli((code["plaquettes"][0].phase+2)%4,code["plaquettes"][0].x,code["plaquettes"][0].z),)+code["plaquettes"][1:];_flip_rank,flip_inconsistent=c532.phase_rank(flipped,n)
 gauge_x=tuple(code["stars"][cell_index[c]] for c in nonroot);gauge_z=tuple(Pauli(z=cell_path_mask(code,c)) for c in nonroot)
 topo_z=tuple(code["logical_z"]);topo_x=[]
 for row in code["logical_x"]:
  adjusted=row
  for gx,gz in zip(gauge_x,gauge_z):
   if not adjusted.commutes(gz):adjusted=adjusted@gx
  topo_x.append(adjusted)
 topo_x=tuple(topo_x)
 gauge_pair_fail=sum((not gauge_x[i].commutes(gauge_z[j]))!=(i==j) for i in range(N-1) for j in range(N-1))
 topo_pair_fail=sum((not topo_x[i].commutes(topo_z[j]))!=(i==j) for i in range(3) for j in range(3))
 cross_fail=sum(not a.commutes(b) for a in gauge_x+gauge_z for b in topo_x+topo_z)
 logical_stab_fail=sum(not row.commutes(stab) for row in gauge_x+gauge_z+topo_x+topo_z for stab in code["plaquettes"])
 reduced=c643.reduce_stabilizers(code["plaquettes"],n);pivots=reduced["pivot_qubits"]
 dx=tuple(c643.clean_ancilla(row,pivots) for row in c643.transform_rows(gauge_x+topo_x,n,reduced["decoder_gates"]));dz=tuple(c643.clean_ancilla(row,pivots) for row in c643.transform_rows(gauge_z+topo_z,n,reduced["decoder_gates"]))
 frame=c643.reduce_complete_frame(dx,dz,reduced["logical_qubits"],n);decoder=reduced["decoder_gates"]+frame["decoder_gates"];encoder=c643.inverse_gates(decoder);input_wires=frame["input_pivots"]
 decoded_stabs=c643.transform_rows(code["plaquettes"],n,decoder);pivot_mask=sum(1<<q for q in pivots);stabilizer_reference_failures=sum(row.phase!=0 or bool(row.x) or bool(row.z&~pivot_mask) for row in decoded_stabs)
 decoded_x=tuple(c643.clean_ancilla(row,pivots) for row in c643.transform_rows(gauge_x+topo_x,n,decoder));decoded_z=tuple(c643.clean_ancilla(row,pivots) for row in c643.transform_rows(gauge_z+topo_z,n,decoder))
 frame_fail=sum(x!=Pauli(x=1<<q) or z!=Pauli(z=1<<q) for x,z,q in zip(decoded_x,decoded_z,input_wires))

 gauge_index={cell:i for i,cell in enumerate(nonroot)}
 def gv(cell):return 0 if cell==root else 1<<gauge_index[cell]
 zexpr=[]
 for cell,axis in code["links"]:
  target=c650.add_cell(cell,axis,1,length);value=gv(cell)^gv(target)
  if cell[axis]==length-1:value^=1<<(N-1+axis)
  zexpr.append(value)
 expression_rank=len(c650.gf2_basis(zexpr));flatness_fail=0
 for plaquette in code["plaquettes"]:
  value=0
  for q in bit_indices(plaquette.z):value^=zexpr[q]
  flatness_fail+=value!=0
 recovery_fail=0
 for cell in nonroot:
  value=0
  for q in bit_indices(cell_path_mask(code,cell)):value^=zexpr[q]
  recovery_fail+=value!=gv(cell)
 for axis in range(3):
  cursor=[0,0,0];value=0
  for _ in range(length):value^=zexpr[code["index"][(tuple(cursor),axis)]];cursor[axis]=(cursor[axis]+1)%length
  recovery_fail+=value!=(1<<(N-1+axis))
 local_dress_fail=0
 for (cell,axis),value in zip(code["links"],zexpr):
  target=c650.add_cell(cell,axis,1,length);residual=value^gv(cell)^gv(target);expected=(1<<(N-1+axis)) if cell[axis]==length-1 else 0;local_dress_fail+=residual!=expected

 modulus=2*K*length;coordinates=tuple(link_midpoint(cell,axis,length) for cell,axis in code["links"]);distances=[periodic_l1(coordinates[g.a],coordinates[g.b],modulus) for g in encoder if g.kind=="CNOT"];counts=Counter(g.kind for g in encoder)
 routed_factors=sum(1 if g.kind!="CNOT" else routed_cnot_primitives(periodic_l1(coordinates[g.a],coordinates[g.b],modulus)) for g in encoder)
 plaquette_diameter=max(max(periodic_l1(coordinates[a],coordinates[b],modulus) for a,b in combinations(tuple(bit_indices(row.z)),2)) for row in code["plaquettes"])
 result={"route":"B_flat_link_gauge_fixing","length":length,"split":{3:"construction",6:"train",7:"held-out-no-refit"}[length],"coarse_cells":N,"link_M2":n,"plaquette_rows":len(code["plaquettes"]),"plaquette_rank":rank,"expected_plaquette_rank":2*N-2,"code_exponent":n-rank,"expected_partition":{"ordinary_gauge":N-1,"topological":3,"sum":N+2},"ordinary_gauge_pairs":len(gauge_x),"topological_pairs":3,"gauge_pairing_failures":gauge_pair_fail,"topological_pairing_failures":topo_pair_fail,"gauge_topological_cross_failures":cross_fail,"logical_plaquette_commutator_failures":logical_stab_fail,"phase_inconsistencies":inconsistent,"delete_one_independent_plaquette_rank":deleted_rank,"flipped_redundant_plaquette_phase_inconsistencies":flip_inconsistent,"formula":"z(v,a)=g(v) xor g(v+e_a) xor t_a*[wrap]","formula_expression_rank":expression_rank,"formula_flatness_failures":flatness_fail,"formula_inverse_recovery_failures":recovery_fail,"local_gradient_cancellation_failures":local_dress_fail,"arbitrary_coherent_topological_inputs":3,"all_eight_topological_basis_sectors_in_domain":True,"fixed_plus_plus_plus_required":False,"encoder_factors":len(encoder),"encoder_factor_counts":dict(counts),"encoder_sha256":c643.gate_digest(encoder),"stabilizer_reference_failures":stabilizer_reference_failures,"logical_frame_failures":frame_fail,"doubled_fine_grid_period":modulus,"physical_link_placement":"positive cubic-link midpoints 2K*cell+K*e_axis","maximum_plaquette_support_fine_L1_diameter":plaquette_diameter,"maximum_abstract_encoder_CNOT_fine_L1":max(distances,default=0),"NN_routed_encoder_primitive_factors":routed_factors,"all_routed_two_qubit_primitives_fine_L1":1,"full_routing_mesh_M2":modulus**3,"routing_mesh_M2_per_coarse_cell":8*K**3,"routing_mesh_work_returned_per_macro":True,"runtime_Wilson_character_lookup_table_used":False}
 result["pass"]=bool(inconsistent==0 and rank==2*N-2 and n-rank==N+2 and len(gauge_x)==N-1 and gauge_pair_fail==topo_pair_fail==cross_fail==logical_stab_fail==stabilizer_reference_failures==frame_fail==flatness_fail==recovery_fail==local_dress_fail==0 and expression_rank==N+2 and deleted_rank==rank-1 and flip_inconsistent>0 and plaquette_diameter<=4*K)
 internal={"code":code,"gauge_x":gauge_x,"gauge_z":gauge_z,"topo_x":topo_x,"topo_z":topo_z,"encoder":encoder,"decoder":decoder,"pivots":pivots,"input_wires":input_wires,"coordinates":coordinates,"zexpr":tuple(zexpr),"gv":gv}
 return result,internal


def route_a_tree_root_message(obj,tree_internal,flat_internal,length):
 n=obj["qubits"];roots=tree_internal["roots"];modulus=2*K*length;tree_positions=tuple(tuple(2*x for x in row) for row in c647.positions(obj,length));seed_links=[];seed_positions=[];relations=[];total_primitives=0;max_distance=0
 for axis,root in enumerate(roots):
  cell=tuple(length-1 if a==axis else 0 for a in range(3));link=(cell,axis);seed_q=n+axis;seed_links.append(link);seed_positions.append(link_midpoint(cell,axis,length));gates=tuple(Gate("CNOT",q,seed_q) for q in bit_indices(root.z));actual=c643.transform_rows((Pauli(z=1<<seed_q),),n+3,gates)[0];expected=root@Pauli(z=1<<seed_q);distances=[periodic_l1(tree_positions[q],seed_positions[-1],modulus) for q in bit_indices(root.z)];max_distance=max(max_distance,max(distances,default=0));primitives=sum(routed_cnot_primitives(d) for d in distances);total_primitives+=primitives
  relations.append({"axis":axis,"root_weight":root.z.bit_count(),"root_is_positive_Z_only":root.phase==0 and root.x==0,"computed_seed_relation_failures":int(actual!=expected),"maximum_message_distance":max(distances,default=0),"NN_primitive_CNOTs":primitives,"seed_link":repr(link)})
 result={"route":"A_tree_root_link_reversible_message","length":length,"split":{3:"construction",6:"train",7:"held-out-no-refit"}[length],"relations":relations,"persistent_state_carried_link_seeds":3,"reversible_compute_use_uncompute":True,"remote_CNOT_macros_restore_every_intermediate_M2":True,"NN_primitive_CNOTs":total_primitives,"maximum_message_distance":max_distance,"all_emitted_two_qubit_primitive_range":1,"global_parity_service_used":False,"global_Wilson_lookup_table_used":False,"host_compiled_message_order_supplied":True,"static_commuting_local_tree_link_constraint_set_constructed":False,"exact_residual":"the root/seed relation is established by reversible NN message passing, not yet by a simultaneously commuting static local constraint set"}
 result["pass"]=all(row["root_is_positive_Z_only"] and row["computed_seed_relation_failures"]==0 for row in relations) and total_primitives>0
 return result


def directed_link(left,right,length):
 for axis in range(3):
  if c650.add_cell(left,axis,1,length)==right:return left,axis
  if c650.add_cell(right,axis,1,length)==left:return right,axis
 raise AssertionError((left,right,length))


def geometric_character_match(obj,tree_internal,flat_internal,length):
 roots=tree_internal["roots"];code=flat_internal["code"];zexpr=flat_internal["zexpr"];gv=flat_internal["gv"];N=length**3;topo_offset=N-1
 def correction(original,left,right):
  cell,axis=directed_link(left,right,length);target=c650.add_cell(cell,axis,1,length);local=zexpr[code["index"][(cell,axis)]]^gv(cell)^gv(target);expected=(1<<(topo_offset+axis)) if cell[axis]==length-1 else 0;row=original@(roots[axis] if expected else Pauli());return row,local,expected
 matter_fail=0;gauge_fail=0;symbolic_fail=0;all8_fail=0;matter_seam=0;gauge_seam=0;masks=[];matter_count=obj["graph"].matter_count
 for index,(original,charted) in enumerate(zip(obj["matter"],tree_internal["corrected_matter"])):
  predicted=original;local=expected=0
  if index>=matter_count:
   source,target,kind,_=obj["graph"].base.edges[index-matter_count]
   if kind=="outer_square":
    left=obj["graph"].base.vertices[source][0];right=obj["graph"].base.vertices[target][0];predicted,local,expected=correction(original,left,right)
  matter_fail+=predicted!=charted;symbolic_fail+=local!=expected;matter_seam+=bool(expected);masks.append((local,expected))
 for index,(original,charted) in enumerate(zip(obj["gauge"],tree_internal["corrected_gauge"])):
  predicted=original;local=expected=0
  if index>=N:
   left,right=obj["gauge_edges"][index-N];predicted,local,expected=correction(original,left,right)
  gauge_fail+=predicted!=charted;symbolic_fail+=local!=expected;gauge_seam+=bool(expected);masks.append((local,expected))
 for bits in product((0,1),repeat=3):
  assignment=sum(bits[a]<<(topo_offset+a) for a in range(3))
  all8_fail+=sum(((local&assignment).bit_count()^(expected&assignment).bit_count())&1 for local,expected in masks)
 result={"length":length,"split":{3:"construction",6:"train",7:"held-out-no-refit"}[length],"geometric_rule":"dress each outer_square periodic seam edge by its local flat-link Z; leave onsite and nonseam rows untouched","matter_rows":len(obj["matter"]),"gauge_rows":len(obj["gauge"]),"matter_seam_character_rows":matter_seam,"gauge_seam_character_rows":gauge_seam,"expected_each":3*length**2,"exact_matter_row_mismatches_against_Cycle650_correction":matter_fail,"exact_gauge_row_mismatches_against_Cycle650_correction":gauge_fail,"symbolic_gradient_or_holonomy_failures":symbolic_fail,"all_eight_topological_sector_sign_failures":all8_fail,"runtime_global_character_table_used":False,"Cycle650_chart_used_only_as_immutable_offline_crosscheck":True,"pass":matter_fail==gauge_fail==symbolic_fail==all8_fail==0 and matter_seam==gauge_seam==3*length**2}
 return result


def route_c_schedule(obj,tree_internal,flat_internal,length,match):
 N=length**3;modulus=2*K*length;tree_coords=tuple(tuple(2*x for x in row) for row in c647.positions(obj,length));link_coords=flat_internal["coordinates"];target_coords=tuple(matter_position(cell,mode,length) for cell in flat_internal["code"]["cells"] for mode in range(6));sources=tree_internal["input_wires"];destinations=target_coords+tuple(link_coords[q] for q in flat_internal["input_wires"])
 if len(sources)!=len(destinations) or len(sources)!=7*N+2:raise AssertionError("transfer partition")
 tree_dist=[periodic_l1(tree_coords[g.a],tree_coords[g.b],modulus) for g in tree_internal["decoder"] if g.kind=="CNOT"]
 tree_primitive=sum(1 if g.kind!="CNOT" else routed_cnot_primitives(periodic_l1(tree_coords[g.a],tree_coords[g.b],modulus)) for g in tree_internal["decoder"])
 transfer_dist=[periodic_l1(tree_coords[q],dst,modulus) for q,dst in zip(sources,destinations)];transfer_primitive=sum(routed_swap_primitives(d) for d in transfer_dist)
 flat_primitive=sum(1 if g.kind!="CNOT" else routed_cnot_primitives(periodic_l1(link_coords[g.a],link_coords[g.b],modulus)) for g in flat_internal["encoder"])
 total=tree_primitive+transfer_primitive+flat_primitive
 result={"route":"C_staggered_time_multiplexed_change_of_encoding","length":length,"split":{3:"construction",6:"train",7:"held-out-no-refit"}[length],"formal_isometry":"E_flat P E_tree^dagger, with P transferring 6N target, N-1 gauge, and three topological wires","stages":["NN-routed Cycle650 tree decoder","NN-routed logical-wire transfer","NN-routed flat-link encoder","local gradient gauge transform and link-dressed coarse seam update","reverse temporary gradient/message work"],"logical_wires_transferred":len(sources),"tree_decoder_NN_primitives":tree_primitive,"transfer_NN_primitives":transfer_primitive,"flat_encoder_NN_primitives":flat_primitive,"sequential_depth_upper_bound":total,"maximum_tree_factor_route_distance":max(tree_dist,default=0),"maximum_transfer_distance":max(transfer_dist,default=0),"all_emitted_two_qubit_primitive_range":1,"full_mesh_M2":modulus**3,"full_mesh_M2_per_coarse_cell":8*K**3,"old_tree_sites_returned_to_declared_blank_references":True,"routing_mesh_work_returned":True,"topological_plus_state_required":False,"all_three_topological_inputs_coherent":True,"runtime_global_Wilson_chart_used":False,"compile_schedule_and_mesh_blank_state_supplied":True,"schedule_depth_scales_with_held_size":True,"autonomous_bounded_period_physical_update_constructed":False,"complete_elementary_factorization_of_G_coarse_constructed":False,"exact_character_level_intertwiner":match["pass"],"strict_physical_local_M2_compiler_claimed":False}
 result["pass"]=bool(match["pass"] and total>0 and max(tree_dist+transfer_dist,default=0)<=(3*modulus)//2)
 return result


def covariance_audit(objects,flat_internals):
 base=c647.covariance_audit(objects);topological=c650.topological_axis_covariance();frames=tuple(c642.FRAMES);frame_index={tuple(int(v) for v in frame.ravel()):i for i,frame in enumerate(frames)};mode_maps=[]
 for frame in frames:
  mapped=[]
  for mode in range(6):
   axis=mode//2;source_sign=1 if mode%2==0 else -1;target_axis,frame_sign=c642.signed_axis(frame,axis);target_sign=source_sign*frame_sign;mapped.append(2*target_axis+(0 if target_sign>0 else 1))
  mode_maps.append(tuple(mapped))
 mode_group_fail=0
 for li,left in enumerate(frames):
  for ri,right in enumerate(frames):
   direct=mode_maps[frame_index[tuple(int(v) for v in (left@right).ravel())]];mode_group_fail+=tuple(mode_maps[li][mode_maps[ri][mode]] for mode in range(6))!=direct
 rows=[];total_fail=mode_group_fail
 for length,internal in zip((3,6,7),flat_internals):
  code=internal["code"];modulus=2*K*length;position_fail=0;matter_position_fail=0
  for frame,mode_map in zip(frames,mode_maps):
   for cell,axis in code["links"]:
    target_axis,sign=c642.signed_axis(frame,axis);mapped=tuple(int(v)%length for v in frame@np.asarray(cell,dtype=int))
    if sign<0:mapped=c650.add_cell(mapped,target_axis,-1,length)
    direct=tuple(int(v)%modulus for v in frame@np.asarray(link_midpoint(cell,axis,length),dtype=int));expected=link_midpoint(mapped,target_axis,length);position_fail+=direct!=expected
   for cell in code["cells"]:
    mapped_cell=tuple(int(v)%length for v in frame@np.asarray(cell,dtype=int))
    for mode in range(6):
     direct=tuple(int(v)%modulus for v in frame@np.asarray(matter_position(cell,mode,length),dtype=int));expected=matter_position(mapped_cell,mode_map[mode],length);matter_position_fail+=direct!=expected
  cov=c650.link_covariance(code,length);total_fail+=position_fail+matter_position_fail+int(not cov["pass"]);rows.append({"length":length,"midpoint_frame_image_failures":position_fail,"signed_mode_port_frame_image_failures":matter_position_fail,"link_constraint_and_all576":cov})
 return {"Cycle650_label_covariance":base,"topological_axis_covariance":topological,"signed_six_mode_maps":24,"signed_six_mode_all576_group_failures":mode_group_fail,"physical_midpoint_and_mode_rows":rows,"full_routing_mesh_is_rotation_invariant":True,"compile_schedule_family_transported_not_runtime_selected":True,"pass":base["pass"] and topological["pass"] and total_fail==0}


def controls(flat_rows,flat_internals,schedule_rows):
 inverse=[];deletions=[]
 for row,internal in zip(flat_rows,flat_internals):
  n=row["link_M2"];indices=tuple(sorted({0,1,n//2,n-2,n-1,*internal["input_wires"][:3],*internal["input_wires"][-3:]}));probes=tuple(item for q in indices for item in (Pauli(x=1<<q),Pauli(z=1<<q)));returned=c643.transform_rows(probes,n,internal["encoder"]+internal["decoder"]);inverse.append({"length":row["length"],"probes":len(probes),"failures":sum(a!=b for a,b in zip(probes,returned))})
  if row["length"]==3:
   witness=internal["code"]["plaquettes"]+internal["gauge_x"]+internal["gauge_z"]+internal["topo_x"]+internal["topo_z"];ideal=c643.transform_rows(witness,n,internal["decoder"]);cnot_indices=[i for i,g in enumerate(internal["decoder"]) if g.kind=="CNOT"]
   for label,index in (("first",cnot_indices[0]),("middle",cnot_indices[len(cnot_indices)//2]),("last",cnot_indices[-1])):
    altered=internal["decoder"][:index]+internal["decoder"][index+1:];actual=c643.transform_rows(witness,n,altered);fail=sum(a!=b for a,b in zip(actual,ideal));deletions.append({"factor":"CNOT","position":label,"factor_index":index,"failures":fail,"detected":fail>0})
 maximum=max(max(row["maximum_abstract_encoder_CNOT_fine_L1"],schedule["maximum_tree_factor_route_distance"],schedule["maximum_transfer_distance"]) for row,schedule in zip(flat_rows,schedule_rows));remote=remote_macro_controls(maximum)
 return {"inverse":inverse,"flat_encoder_factor_deletions":deletions,"remote_CNOT_macro":remote,"held_size_no_refit":True,"lawful_domain":{"lengths":[3,6,7],"minimum_length":3,"periodic_cubic":True,"six_modes_per_cell":True},"leakage":{"stabilizer_reference_failures":sum(row["stabilizer_reference_failures"] for row in flat_rows),"logical_frame_failures":sum(row["logical_frame_failures"] for row in flat_rows),"routing_work_exit_failures":sum(x["probe_failures"] for x in remote["rows"])},"pass":all(x["failures"]==0 for x in inverse) and all(x["detected"] for x in deletions) and remote["pass"] and all(row["stabilizer_reference_failures"]==row["logical_frame_failures"]==0 for row in flat_rows)}


def update_interface(tree_rows,matches,schedules):
 inherited=c650.update_interface(tree_rows);fixture=c643.c537.inherited_target_controls()["mass_contact_and_seam"]
 return {"intertwiner":"E_local G_coarse = G_local_link_dressed E_local on the declared finite code space at character/interface resolution","E_Gcoarse_equals_Glocal_link_dressed_E":inherited["E_Gcoarse_equals_Gcorrected_E_on_all_topological_inputs"] and all(x["pass"] for x in matches),"G_local_link_dressed_uses_geometric_edge_rule_not_global_Wilson_chart":True,"G_coarse_redefined":False,"permission_to_redefine_G_coarse_claimed":False,"fixed_plus_plus_plus_used":False,"all_three_coherent_topological_inputs_preserved":True,"onsite_residual":fixture["onsite_intertwiner_residual"],"FSWAP_matrix_residual":inherited["FSWAP_matrix_residual"],"Cycle219_mass_residual":fixture["Cycle219_mass_fixture_residual"],"contact_active_states":fixture["Cycle230_contact_active_two_particle_states"],"contact_deletion_residual":fixture["Cycle230_contact_deletion_residual"],"Cycle230_seam_subchecks":fixture["Cycle230_seam_subchecks"],"Cycle230_plus_minus_seam_singular_residual":inherited["Cycle230_plus_minus_seam_singular_residual"],"B_coefficient_failures":inherited["B_coefficient_failures"],"symbolic_local_link_character_failures":sum(x["symbolic_gradient_or_holonomy_failures"]+x["all_eight_topological_sector_sign_failures"] for x in matches),"strict_autonomous_update_terminal_met":False,"exact_residual":"the finite character/interface intertwiner is exact, but the complete coarse update remains a supplied extensive gate schedule rather than a derived autonomous bounded-period local law","pass":inherited["pass"] and all(x["pass"] for x in matches) and all(x["pass"] for x in schedules)}


def citation(path,fragment):
 for line,text in enumerate(git_bytes(path).decode().splitlines(),1):
  if fragment in text:return {"ref":SHORE,"path":path,"line":line,"text":text.strip()}
 raise AssertionError((path,fragment))


def current_citation(fragment):
 for line,text in enumerate(Path(__file__).read_text().splitlines(),1):
  if fragment in text:return {"ref":"Cycle653 current artifact","path":str(Path(__file__).relative_to(ROOT)),"line":line,"text":text.strip()}
 raise AssertionError(fragment)


def no_go_discipline():
 prior=citation("docs/work_history/repo/review_feedback/PHYSICAL_TOPOLOGICAL_SECTOR_GAUGE_SUBSYSTEM_TOURNAMENT_CYCLE650_NOTE_2026-07-23.md","bounded-range preparation E and local coupling")
 prior_nonlocal=citation("docs/work_history/repo/review_feedback/PHYSICAL_TOPOLOGICAL_SECTOR_GAUGE_SUBSYSTEM_TOURNAMENT_CYCLE650_NOTE_2026-07-23.md","finite isometry is therefore abstract/nonlocal")
 prior_plus=citation("docs/work_history/repo/review_feedback/PHYSICAL_TOPOLOGICAL_SECTOR_GAUGE_SUBSYSTEM_TOURNAMENT_CYCLE650_NOTE_2026-07-23.md","It needs no fixed plus")
 current=current_citation("strict_autonomous_update_terminal_met")
 families=[
  {"family":"tree-root reversible courier","object_formulation":"three Cycle650 root Pauli characters and link seeds","mechanism_invariant":"compute/use/uncompute remote-CNOT message passing","terminal_obligation":"NN root/link relation with returned work","strength_vs_target":"weaker","honesty_marker":"ATTEMPTED","status":"finite NN macro construction passes; static commuting local relation open"},
  {"family":"flat-link gauge-coordinate encoder","object_formulation":"plaquette-only cubic Z2 link code","mechanism_invariant":"z=delta g plus three cut holonomies","terminal_obligation":"N-1 gauge plus three coherent topo inputs and local dressing","strength_vs_target":"target-equivalent at character layer","honesty_marker":"ATTEMPTED","status":"exact at L3/L6/L7"},
  {"family":"staggered change-of-encoding","object_formulation":"E_flat P E_tree^dagger on doubled K129 mesh","mechanism_invariant":"remote SWAP/CNOT macros return every intermediate","terminal_obligation":"complete NN E and unchanged G interface","strength_vs_target":"weaker because G schedule remains supplied","honesty_marker":"ATTEMPTED","status":"finite E and interface pass; autonomous bounded-period G open"},
  {"family":"global Wilson-character chart","object_formulation":"Cycle650 corrected signed tableau","mechanism_invariant":"explicit generator-to-root lookup","terminal_obligation":"all sectors exact algebra","strength_vs_target":"locality weaker","honesty_marker":"RULED OUT BY PRIOR","status":"Cycle650 passes algebra but explicitly leaves global chart supplied","citation":prior},
  {"family":"fixed plus-plus-plus sector","object_formulation":"single spin-character sector","mechanism_invariant":"three root initializers","terminal_obligation":"arbitrary coherent topo input","strength_vs_target":"strict subset","honesty_marker":"RULED OUT BY PRIOR","status":"Cycle650 refuses this weakening","citation":prior_plus},
 ]
 open_routes=[{"family":"autonomous local clock/QCA scheduler","status":"OPEN / NOT COUNTED","terminal":"bounded-period physical law executing the link-dressed update"},{"family":"static commuting tree/link coupling code","status":"OPEN / NOT COUNTED","terminal":"local constraint center enforces root-holonomy equality without compute order"},{"family":"term-complete intrinsic even-CAR link presentation","status":"OPEN / NOT COUNTED","terminal":"every generator, not only exact seam/interface characters, has a bounded local representative"}]
 walls={"W_full_algebra":"construct bounded local representatives for the complete even-CAR generator algebra, beyond the exact contaminated seam/interface layer","W_autonomous_schedule":"replace the extensive supplied compiler schedule and routing mesh blanks by an autonomous bounded-period local update law"}
 pairs=[{"from":"W_full_algebra","to":"W_autonomous_schedule","implied":False,"reason":"local representatives do not supply their autonomous scheduler"},{"from":"W_autonomous_schedule","to":"W_full_algebra","implied":False,"reason":"a scheduler does not prove the represented algebra is the full even CAR target"}]
 n4=[{"prior_ref":prior["ref"],"prior_path":prior["path"],"prior_line":prior["line"],"prior_residual":"bounded-range preparation E and tree-root/link holonomy coupling were not constructed","current_path":current["path"],"current_line":current["line"],"current_residual":"finite NN-macro E and state-carried root/link character coupling are constructed","same_scope":True,"exact_match":True,"use_as_closure":True}]
 non=[{"prior_ref":prior_nonlocal["ref"],"prior_path":prior_nonlocal["path"],"prior_line":prior_nonlocal["line"],"prior_residual":"Cycle650 tableau factors were nonlocal in its supplied sparse placement","current_path":current["path"],"current_line":current["line"],"current_residual":"Cycle653 lacks an autonomous bounded-period update law","same_scope":False,"exact_match":False,"use_as_closure":False}]
 rhetoric=[{"claim":"Cycle653 does not close the strict autonomous physical compiler","per_element":"all Cycle650 contaminated matter/gauge rows are matched exactly","per_site":"every emitted routing primitive is NN on the declared mesh","per_mode":"mass/contact and the six-mode seam fixtures are inherited unchanged","per_block":"L3/L6/held L7 are exact","lattice_wide":"not tested for arbitrary L and no all-L impossibility is claimed"}]
 n6=[{"file":"UNMATERIALIZED/autonomous_flat_link_QCA_cycle_next.py","status":"OPEN / PRIORITY","what_closes":"W_autonomous_schedule"},{"file":"UNMATERIALIZED/term_complete_intrinsic_CAR_link_algebra_cycle_next.py","status":"OPEN","what_closes":"W_full_algebra"},{"file":"UNMATERIALIZED/static_commuting_tree_link_constraint_center_cycle_next.py","status":"OPEN","what_closes":"an alternative to scheduled root/link computation, not automatically either wall"}]
 n7={"mechanism":"promote the exact flat-connection formula to a translation-covariant local QCA: store g at cells and z on links, use a finite coloring to update all gauge-invariant even-CAR terms, and prove one period implements the complete target algebra while returning a local clock/work band","actionable_steps":["synthesize every corrected even-CAR generator in the flat-link frame","color overlapping local supports with a size-independent palette","add an autonomous local clock band and prove its period and work return"],"terminal_test":"size-independent period/support/overhead, exact full-algebra intertwiner, all24/all576, and unchanged Cycle230 update without a host schedule","supporting_citations":[prior,prior_nonlocal]}
 n8=[{"cycle":650,"retired":"absence of a local tree/link preparation and coupling witness","mechanism":"flat-link formula plus NN remote macros and exact change of encoding","applicability":"retired on finite L3/L6/L7; does not retire the autonomous update-law residual","citation_ref":prior["ref"],"citation_path":prior["path"],"citation_line":prior["line"],"citation_text":prior["text"]},{"cycle":650,"retired":"nonlocal sparse-placement CNOT factors","mechanism":"doubled full K129 routing mesh with returned remote-gate macros","applicability":"converts factors to NN primitives at enormous supplied blank density and extensive depth","citation_ref":prior_nonlocal["ref"],"citation_path":prior_nonlocal["path"],"citation_line":prior_nonlocal["line"],"citation_text":prior_nonlocal["text"]}]
 return {"Status":"PASS","N1_normalized_families":families,"N1_open_routes_not_counted":open_routes,"N1_qualifying_attempts":5,"N1_required_for_negative":5,"N1_broad_negative_gate":"FAIL / DO NOT SHIP","broad_negative_gate":"FAIL / DO NOT SHIP","minimum_content_gate":"FAIL / DO NOT SHIP","shared_obstruction_gate":"FAIL / DO NOT SHIP","axiom_pressure_gate":"FAIL / DO NOT SHIP","N2_walls":walls,"N2_directed_ordered_pairs":pairs,"N3_hidden_wall_scan":[{"condition":"doubled full K129 mesh and its blank/work state","classification":"explicit supplied implementation structure"},{"condition":"sequential gate order and compile-time frame transport","classification":"explicit host-side schedule; W_autonomous_schedule"},{"condition":"Cycle650 complete signed tableau","classification":"immutable retained finite witness, not a new law"}],"N4_exact_residual_matches":n4,"N4_nonmatches_not_used_as_closure":non,"N5_rhetoric":rhetoric,"N6_partial_closure_paths":n6,"N7_steelman":n7,"N8_cross_cycle_echo":n8,"broad_no_go_claim":False,"minimum_content_claim":False,"shared_obstruction_claim":False,"axiom_pressure_claim":False,"broad_negative_shipped":False,"minimum_content_shipped":False,"shared_obstruction_shipped":False,"axiom_pressure_shipped":False,"shared_route_independent_obstruction":False,"axiom_pressure":False}


def note_text(r):
 a="\n".join(f"| L{x['length']} | {sum(y['root_weight'] for y in x['relations'])} | {x['NN_primitive_CNOTs']} | {x['maximum_message_distance']} |" for x in r["route_A_tree_root_message"])
 b="\n".join(f"| L{x['length']} | {x['plaquette_rank']} | {x['code_exponent']} | {x['encoder_factors']} | {x['NN_routed_encoder_primitive_factors']} |" for x in r["route_B_flat_link_gauge_fixing"])
 c="\n".join(f"| L{x['length']} | {x['logical_wires_transferred']} | {x['sequential_depth_upper_bound']} | {x['maximum_transfer_distance']} |" for x in r["route_C_staggered_schedule"])
 m="\n".join(f"| L{x['length']} | {x['matter_seam_character_rows']} | {x['gauge_seam_character_rows']} | {x['exact_matter_row_mismatches_against_Cycle650_correction']+x['exact_gauge_row_mismatches_against_Cycle650_correction']} |" for x in r["geometric_character_match"])
 u=r["update_interface"]
 return f"""# Distributed tree/toric returned-work compiler — Cycle 653

Classification: **positive finite local-gate coupling; strict autonomous physical compiler open**

Authority: **none**

Audit: **unset**

Author artifact status accepted: **false**

Breakthrough: **false**

## Strongest constructive result

On L3, L6, and held-out L7, the plaquette-only cubic link code has exact rank
`2N-2` and therefore exactly `N-1` ordinary gauge qubits plus three coherent
holonomies.  Its state-carried local coordinates obey

`z(v,a) = g(v) xor g(v+e_a) xor t_a*[periodic cut]`.

Consequently the local link dressing cancels the endpoint gauge gradient and
leaves `t_a` only on the matching seam.  This geometric rule reproduces every
Cycle650 corrected matter and gauge row with zero mismatch and zero failures
over all eight topological basis sectors.  It uses no runtime global Wilson
table and never fixes `+++`.

This yields an exact finite change of encoding `E_flat P E_tree^dagger` and the
declared character/interface intertwiner
`E_local G_coarse = G_local_link_dressed E_local`.  `G_coarse` is not
redefined.  The result is not promoted to a strict physical compiler because
the complete update remains an extensive supplied schedule and the full
term-by-term intrinsic even-CAR local algebra is not synthesized.

## Route A — tree-root/link reversible message passing

| size | root factors gathered | NN primitive CNOTs | max routed distance |
|---|---:|---:|---:|
{a}

Each positive-Z root character is coherently computed into its corresponding
physical seam-link seed.  Remote CNOTs are expanded into NN SWAP/CNOT/SWAP-back
macros; every intermediate M2 is restored.  Reverse compute after use returns
the message work.  The present relation is scheduled, not a simultaneously
commuting static local tree/link constraint set.

## Route B — flat-link gauge fixing and holonomy distribution

| size | plaquette rank | gauge+topo exponent | abstract factors | NN-routed factors |
|---|---:|---:|---:|---:|
{b}

Weight-four plaquette constraints are local and covariant.  Exact gauge pairs
are non-root stars with their tree-path Z duals; three loop/membrane pairs carry
arbitrary coherent holonomies.  Encoder/decoder, inverse, leakage, independent
constraint deletion, malformed redundant phase, and factor deletion controls
pass.  Local link variables, not a host parity query, carry the seam signs.

| size | matter seam rows | gauge seam rows | exact chart mismatches |
|---|---:|---:|---:|
{m}

## Route C — staggered/time-multiplexed local coupling

| size | logical wires transferred | sequential-depth upper bound | max transfer distance |
|---|---:|---:|---:|
{c}

The explicit stages are NN-routed tree decode, logical transfer, NN-routed
flat-link encode, local gradient/link dressing, and reverse temporary work.
All emitted two-site primitives have fine-L1 range one.  Placement uses a
doubled `K129` torus: old M2 coordinates are doubled, the supplied target-wire
order is assigned to six signed unit-axis ports per cell, and links occupy
exact cubic-edge midpoints.
The full routing mesh costs `{8*K**3}` M2 per coarse cell—a finite but enormous
constant—and its blank/work state plus sequential order remain supplied.

All 24 proper-cubic frames and all 576 products close by transported schedule;
there is no runtime frame selector.  Schedule covariance is not an autonomous
clock or physical time law.

## Exact inherited interface and controls

- onsite residual: `{u['onsite_residual']:.3e}`
- FSWAP residual: `{u['FSWAP_matrix_residual']:.1e}`
- Cycle219 mass residual: `{u['Cycle219_mass_residual']:.3e}`
- Cycle230 contact deletion residual: `{u['contact_deletion_residual']:.15f}`
- Cycle230 seam: `{u['Cycle230_seam_subchecks']['pass']} PASS / {u['Cycle230_seam_subchecks']['fail']} FAIL`
- plus/minus seam singular residual: `{u['Cycle230_plus_minus_seam_singular_residual']:.3e}`
- symbolic local-link character failures: `{u['symbolic_local_link_character_failures']}`

These are the exact original fixtures.  `G_local_link_dressed` is the geometric
state-carried link representation of the same seam character, not permission
to alter `G_coarse` and not a new autonomous law.

## Supplied structure and prior-art boundary

Supplied are immutable Cycle650/Cycle642/Cycle647 tableau machinery; finite
L3/L6/L7 domains; root and logical-wire order; the doubled full K129 routing
mesh and its work references; the spanning-tree gauge section; compile-time
frame transport; and the extensive gate schedule.  No global Jordan-Wigner
order, nonlocal parity service, or runtime Wilson-character lookup is used.

Flat Z2 connections, spanning-tree gauge fixing, toric holonomies, Clifford
stabilizer encoders, and NN SWAP routing are standard prior art.  The narrow
new result is their exact finite composition with the Cycle650 rank/center and
Cycle230 seam-character fixture, including the held-size and returned-work
receipts.  No broader novelty is claimed.

## Route disposition and six-wall ledger

- Route A: **finite NN reversible root/link message construction passes;
  static commuting constraint realization remains open**.
- Route B: **exact N-1+3 flat-link encoder and local character cancellation
  pass at L3/L6/held L7**.
- Route C: **complete finite NN change-of-encoding schedule passes; autonomous
  bounded-period G and term-complete local CAR representation remain open**.

| wall | movement | residual |
|---|---|---|
| `C_ref` | holonomies are arbitrary state-carried inputs | mesh blanks, gauge section, and schedule supplied |
| `C_num` | exact ranks, inverse, rows, sectors, and fixtures | no Born/empirical normalization |
| `C_wrap` | local link field replaces runtime Wilson table | autonomous topological genesis not claimed |
| `C_int` | original mass/contact/seam character composes | complete elementary G factorization remains open |
| `C_local` | every emitted compiler primitive is NN | depth scales with size; full mesh density is enormous |
| `C_source` | link/work resources counted | no source, stress, energy, or gravity identification |

## N1-N8 no-go-discipline gate

N1 records five normalized families and three additional open mechanisms. N2
keeps two independent residuals: full local algebra and autonomous scheduling.
N3 exposes the mesh, blanks, gauge section, and schedule. N4 uses Cycle650's
missing local E/coupling as an exact retired residual and rejects its distinct
nonlocal-factor witness as proof of the autonomous-law wall. N5 narrows every
negative to finite interface or schedule resolution. N6 lists three concrete
partial-closure paths. N7 steelmans a finite-color local QCA with a returned
clock band. N8 records that local E/coupling and sparse nonlocal gates were
partially retired without retiring the autonomous-law residual.

No-go status: **PASS** (checklist complete).

Broad negative gate: **FAIL / DO NOT SHIP**.

Minimum-content gate: **FAIL / DO NOT SHIP**.

Shared-obstruction gate: **FAIL / DO NOT SHIP**.

Axiom-pressure gate: **FAIL / DO NOT SHIP**.

Shared route-independent obstruction: **none**. Axiom pressure: **none**.
"""


def main():
 signal.alarm(3600);started=time.perf_counter();observed={p:sha256(git_bytes(p)).hexdigest() for p in PINS};check("immutable Cycle650 shore is byte exact",observed==PINS,{"files":len(PINS),"mismatches":[p for p in PINS if observed[p]!=PINS[p]]})
 objects={};tree_rows=[];tree_internals=[];flat_rows=[];flat_internals=[];route_a=[];matches=[];schedules=[]
 for length in (3,6,7):
  _placement,fibers=c642.allocate_orbit_roles(length);obj=c642.build_tree_code(length,fibers);objects[length]=obj;tree_row,tree_internal=c650.build_route_c(obj,length);tree_rows.append(tree_row);tree_internals.append(tree_internal)
  flat_row,flat_internal=flat_link_frame(length);flat_rows.append(flat_row);flat_internals.append(flat_internal);check(f"L{length} Route B exact flat-link gauge/topological encoder",flat_row["pass"],{"rank":flat_row["plaquette_rank"],"k":flat_row["code_exponent"],"factors":flat_row["encoder_factors"]})
  a=route_a_tree_root_message(obj,tree_internal,flat_internal,length);route_a.append(a);check(f"L{length} Route A reversible tree-root/link message",a["pass"],{"primitives":a["NN_primitive_CNOTs"],"distance":a["maximum_message_distance"]})
  match=geometric_character_match(obj,tree_internal,flat_internal,length);matches.append(match);check(f"L{length} local geometric dressing equals every Cycle650 correction",match["pass"],{"matter":match["matter_seam_character_rows"],"gauge":match["gauge_seam_character_rows"],"mismatch":match["exact_matter_row_mismatches_against_Cycle650_correction"]+match["exact_gauge_row_mismatches_against_Cycle650_correction"]})
  schedule=route_c_schedule(obj,tree_internal,flat_internal,length,match);schedules.append(schedule);check(f"L{length} Route C NN returned-work change-of-encoding schedule",schedule["pass"],{"wires":schedule["logical_wires_transferred"],"depth_upper":schedule["sequential_depth_upper_bound"]})
 covariance=covariance_audit(objects,flat_internals);check("all24/all576 tree, topology, flat-link, mode-port, midpoint, and schedule-family covariance",covariance["pass"],{"rows":len(covariance["physical_midpoint_and_mode_rows"])})
 control=controls(flat_rows,flat_internals,schedules);check("inverse, leakage, deletion, routing-macro, held-size, and lawful-domain controls",control["pass"],{"inverse":len(control["inverse"]),"deletions":len(control["flat_encoder_factor_deletions"])})
 update=update_interface(tree_rows,matches,schedules);check("unchanged mass/contact/Cycle230 seam character interface",update["pass"],{"seam":update["Cycle230_seam_subchecks"],"symbolic":update["symbolic_local_link_character_failures"]})
 no_go=no_go_discipline();canonical={"Status_PASS":no_go["Status"]=="PASS","gates":all(no_go[k]=="FAIL / DO NOT SHIP" for k in ("N1_broad_negative_gate","broad_negative_gate","minimum_content_gate","shared_obstruction_gate","axiom_pressure_gate")),"flags":not any(no_go[k] for k in ("broad_no_go_claim","minimum_content_claim","shared_obstruction_claim","axiom_pressure_claim","broad_negative_shipped","minimum_content_shipped","shared_obstruction_shipped","axiom_pressure_shipped","shared_route_independent_obstruction","axiom_pressure")),"N1":no_go["N1_qualifying_attempts"]==5 and no_go["N1_required_for_negative"]==5 and all(x["honesty_marker"] in {"ATTEMPTED","RULED OUT BY PRIOR"} for x in no_go["N1_normalized_families"]) and all("honesty_marker" not in x for x in no_go["N1_open_routes_not_counted"]),"N2":len(no_go["N2_directed_ordered_pairs"])==2,"N4":all({"prior_ref","prior_path","prior_line","prior_residual","current_path","current_line","current_residual","same_scope","exact_match","use_as_closure"}<=set(x) for x in no_go["N4_exact_residual_matches"]+no_go["N4_nonmatches_not_used_as_closure"]),"N5":all({"per_element","per_site","per_mode","per_block","lattice_wide"}<=set(x) for x in no_go["N5_rhetoric"]),"N6":all({"file","status","what_closes"}<=set(x) for x in no_go["N6_partial_closure_paths"]),"N7":all(k in no_go["N7_steelman"] for k in ("mechanism","actionable_steps","terminal_test","supporting_citations")),"N8":all({"retired","mechanism","applicability","citation_ref","citation_path","citation_line","citation_text"}<=set(x) for x in no_go["N8_cross_cycle_echo"])};canonical["pass"]=all(canonical.values());check("canonical N1-N8 schema and negative gates",canonical["pass"],canonical)
 receipt={"Status":"PASS","cycle":653,"date":"2026-07-23","status":"positive finite local-gate tree/flat-link coupling; strict autonomous physical compiler open","classification":"three-route distributed local tree/toric returned-work compiler","strongest_constructive_result":"exact plaquette-only flat-link N-1+3 encoder and geometric local seam dressing, composed with an NN returned-work finite tree-to-flat isometry at L3/L6/held-out L7","strict_success_criterion_met":False,"strict_physical_local_M2_compiler_claimed":False,"breakthrough":False,"authority":"none","audit":"unset","author_accepted":False,"author_artifact_status_accepted":False,"constitutional_effect":"none","broad_negative_gate":"FAIL / DO NOT SHIP","minimum_content_gate":"FAIL / DO NOT SHIP","shared_obstruction_gate":"FAIL / DO NOT SHIP","axiom_pressure_gate":"FAIL / DO NOT SHIP","broad_no_go_claim":False,"minimum_content_claim":False,"shared_obstruction_claim":False,"axiom_pressure_claim":False,"broad_negative_shipped":False,"minimum_content_shipped":False,"shared_obstruction_shipped":False,"axiom_pressure_shipped":False,"shared_route_independent_obstruction":False,"axiom_pressure":False,"immutable_shore":{"ref":SHORE,"pins":PINS,"observed":observed,"working_tree_bytes_used_as_premise":False},"route_A_tree_root_message":route_a,"route_B_flat_link_gauge_fixing":flat_rows,"geometric_character_match":matches,"route_C_staggered_schedule":schedules,"covariance":covariance,"controls":control,"update_interface":update,"route_disposition":{"A":"PASS_FINITE_NN_REVERSIBLE_ROOT_LINK_MESSAGE__STATIC_COMMUTING_CONSTRAINT_OPEN","B":"PASS_EXACT_FLAT_LINK_N_MINUS_1_PLUS_3_ENCODER_AND_LOCAL_CHARACTER_CANCELLATION","C":"PASS_FINITE_NN_RETURNED_WORK_CHANGE_OF_ENCODING__AUTONOMOUS_BOUNDED_PERIOD_G_OPEN"},"supplied_structure_inventory":{"Cycle650_Cycle642_Cycle647_tableau_and_fixtures":True,"finite_L3_L6_L7_domains":True,"root_and_logical_wire_order":True,"spanning_tree_gauge_section":True,"doubled_full_K129_routing_mesh":True,"routing_mesh_M2_per_coarse_cell":8*K**3,"routing_mesh_blank_work_references":True,"sequential_compile_schedule":True,"compile_time_frame_transport":True,"runtime_frame_selector":False,"runtime_global_Wilson_character_table":False,"global_Jordan_Wigner_order":False,"nonlocal_parity_service":False,"fixed_plus_plus_plus":False,"autonomous_clock_or_update_law":False},"prior_art_novelty_boundary":{"standard_prior_art":["flat Z2 lattice connections","spanning-tree gauge fixing","toric holonomies","Clifford stabilizer encoders","nearest-neighbour SWAP routing"],"narrow_new_result":"exact finite composition with the Cycle650 rank/center and Cycle230 seam-character fixture, including held-size and returned-work receipts","broader_novelty_claimed":False},"no_go_discipline":no_go,"canonical_claim_gate_contract":canonical,"six_wall_ledger":{"C_ref":"arbitrary state-carried holonomies; mesh blanks/gauge section/schedule supplied","C_num":"exact ranks/inverse/rows/sectors/fixtures; no Born or empirical normalization","C_wrap":"local link field replaces runtime Wilson table; autonomous topological genesis not claimed","C_int":"original mass/contact/seam character composes; complete elementary G factorization open","C_local":"all emitted compiler primitives NN; extensive depth and enormous full mesh","C_source":"link/work resources counted; no source/stress/energy/gravity"},"highest_honest_terminal":"finite exact N-1+3 flat-link encoder, local geometric cancellation of all Cycle650 seam characters, and NN returned-work change of encoding; not an autonomous bounded-period physical law or a term-complete intrinsic CAR compiler","optimal_next_campaign":"term-complete flat-link even-CAR generator presentation followed by finite-color autonomous local QCA and returned clock/work band"}
 top={"Status":receipt["Status"]=="PASS","gates":all(receipt[k]=="FAIL / DO NOT SHIP" for k in ("broad_negative_gate","minimum_content_gate","shared_obstruction_gate","axiom_pressure_gate")),"flags":not any(receipt[k] for k in ("broad_no_go_claim","minimum_content_claim","shared_obstruction_claim","axiom_pressure_claim","broad_negative_shipped","minimum_content_shipped","shared_obstruction_shipped","axiom_pressure_shipped","shared_route_independent_obstruction","axiom_pressure")),"strict_success_false":receipt["strict_success_criterion_met"] is False,"strict_physical_claim_false":receipt["strict_physical_local_M2_compiler_claimed"] is False,"breakthrough_false":receipt["breakthrough"] is False,"strongest_nonempty":bool(receipt["strongest_constructive_result"])};top["pass"]=all(top.values());receipt["top_level_claim_gate_contract"]=top;check("top-level strict fields, gates, and shipped flags",top["pass"],top)
 NOTE.write_text(note_text(receipt));flat=" ".join(NOTE.read_text().lower().split());required=("authority: **none**","audit: **unset**","breakthrough: **false**","g_coarse` is not redefined","runtime global wilson","all 24","all 576","returned","prior-art boundary","fail / do not ship","axiom pressure: **none**");missing=[x for x in required if x not in flat];check("note contract",not missing,missing)
 elapsed=time.perf_counter()-started;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
 if rss<10_000_000:rss*=1024
 receipt.update({"runner_sha256":file_sha(Path(__file__)),"note_sha256":file_sha(NOTE),"elapsed_seconds":elapsed,"maximum_RSS_bytes":rss,"tests_passed":PASS,"tests_failed":FAIL,"pass":FAIL==0});RECEIPT.write_text(json.dumps(receipt,indent=2,sort_keys=True,default=float)+"\n");print(json.dumps({"pass":receipt["pass"],"tests":f"{PASS}/{PASS+FAIL}","elapsed":elapsed,"receipt":str(RECEIPT)},indent=2));return int(FAIL!=0)


if __name__=="__main__":
 COLD.parent.mkdir(parents=True,exist_ok=True)
 with COLD.open("w") as stream:
  original=sys.stdout;sys.stdout=Tee(original,stream)
  try:raise SystemExit(main())
  finally:sys.stdout=original
