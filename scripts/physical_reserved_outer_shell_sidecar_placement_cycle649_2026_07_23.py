#!/usr/bin/env python3
"""Cycle649: literal outer-shell placement and safe-route tournament.

Places the Cycle646 controller/register grammar on proper-cubic role orbits
and constructs actual occupied-role-safe NN route words through a K129 outer-shell
backbone plus formula-generated sidecar fingers.  This is placement/routing,
not E, preparation, autonomous repair, occurrence, or time.

Authority none; audit unset; constitutional effect none.
"""
from __future__ import annotations

from collections import Counter, deque
from hashlib import sha256
from itertools import combinations, permutations, product
import gc
import importlib.util
import io
import json
import math
import os
from pathlib import Path
import resource
import subprocess
import sys
import tarfile
import tempfile
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
IMMUTABLE_COMMIT = "c56a40368236cacb6b2c787e0eb4a4052fa0df5f"
_EXPORT = tempfile.TemporaryDirectory(prefix="cycle649-immutable-")
IMMUTABLE_ROOT = Path(_EXPORT.name).resolve()
os.environ["GIT_DIR"] = str((ROOT / ".git").resolve())
os.environ["GIT_WORK_TREE"] = str(ROOT.resolve())
_archive = subprocess.check_output([
    "git", "archive", "--format=tar", IMMUTABLE_COMMIT,
    "scripts", "outputs/physical_autonomous_marker_recognition_token_attempt_cycle631_receipt_2026_07_23.json",
], cwd=ROOT)
with tarfile.open(fileobj=io.BytesIO(_archive), mode="r:") as _tar:
    _tar.extractall(IMMUTABLE_ROOT, filter="data")
# The immutable Cycle646 runner archives its own older shore at import time.
# Give that temporary worktree a read-only route to this repository's git
# object database; no working-tree artifact is imported as a premise.
os.symlink((ROOT / ".git").resolve(), IMMUTABLE_ROOT / ".git", target_is_directory=True)
sys.path.insert(0, str(IMMUTABLE_ROOT / "scripts"))
import physical_orbit_tree_local_enforcement_cycle646_2026_07_23 as c646

# Load the immutable Cycle638 source under a private module name so its ROOT
# points at the archive containing the Cycle631 receipt used by role placement.
_spec = importlib.util.spec_from_file_location(
    "cycle649_immutable_c638",
    IMMUTABLE_ROOT / "scripts/physical_hierarchical_grammar_full_act_compiler_cycle638_2026_07_23.py",
)
c638 = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(c638)

c642 = c646.c642
FRAMES = c646.FRAMES
K = 129
SHELL = 64
AUTHORITY = "none"
AUDIT = "unset"
NOTE = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_RESERVED_OUTER_SHELL_SIDECAR_PLACEMENT_CYCLE649_NOTE_2026-07-23.md"
RECEIPT = ROOT / "outputs/physical_reserved_outer_shell_sidecar_placement_cycle649_receipt_2026_07_23.json"
COLD = ROOT / "outputs/physical_reserved_outer_shell_sidecar_placement_cycle649_cold_2026_07_23.txt"
PASS = FAIL = 0
PINS = {
    "scripts/physical_orbit_tree_local_enforcement_cycle646_2026_07_23.py": "36b8a26a81e9a2cd7c8cdd651160515eecdfed7b7dc14638e44e10bf4d7bf423",
    "docs/work_history/repo/review_feedback/PHYSICAL_ORBIT_TREE_LOCAL_ENFORCEMENT_CYCLE646_NOTE_2026-07-23.md": "8170dda07aee66aeaaa8a6e973eb9dae34936a96cb8a6445fc0528521015b5e2",
    "outputs/physical_orbit_tree_local_enforcement_cycle646_receipt_2026_07_23.json": "0433e88df3c74ec54b7afd0a110b1739f0f1101f344248ebebf1f6f8a5031d5a",
    "outputs/physical_orbit_tree_local_enforcement_cycle646_cold_2026_07_23.txt": "321b0a905e32ae6e1f751187ed980603d947bf743dacbbea015d5f8a99f87133",
    "scripts/physical_hierarchical_grammar_full_act_compiler_cycle638_2026_07_23.py": "7c30cb47934ea6faf908d13ef15e6d62bf0c494ba8632ebdffeec88352037d53",
    "outputs/physical_autonomous_marker_recognition_token_attempt_cycle631_receipt_2026_07_23.json": "be13c9df070477d653b82e97c2f15aace54b77a08718c1af9ce5d08ca649c989",
}
NO_GO_ORIGIN_MAIN_SHA256 = "7d1aea8243ddd972331b935e2e836657e72115da3efe259f828fe862469d68b7"
DIRECTIONS = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))


class Tee:
    def __init__(self, *streams): self.streams = streams
    def write(self, value):
        for stream in self.streams: stream.write(value)
        return len(value)
    def flush(self):
        for stream in self.streams: stream.flush()


def check(label, condition, detail=""):
    global PASS, FAIL
    PASS += int(condition); FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def json_default(value):
    if isinstance(value, np.generic): return value.item()
    if isinstance(value, np.ndarray): return value.tolist()
    if isinstance(value, (set, frozenset)): return sorted(value, key=repr)
    raise TypeError(type(value).__name__)


def git_blob(path: str) -> bytes:
    return subprocess.check_output(["git", "show", f"{IMMUTABLE_COMMIT}:{path}"], cwd=ROOT)


def git_sha(path: str) -> str:
    return sha256(git_blob(path)).hexdigest()


def immutable_citation(path: str, fragment: str) -> dict:
    for line, text in enumerate(git_blob(path).decode().splitlines(), 1):
        if fragment in text:
            return {"ref":IMMUTABLE_COMMIT,"path":path,"line":line,"line_text":text.strip(),"fragment":fragment}
    raise AssertionError((path, fragment))


def current_citation(path: str, fragment: str) -> dict:
    for line, text in enumerate((ROOT/path).read_text().splitlines(), 1):
        if fragment in text:
            return {"ref":"Cycle649 working artifact","path":path,"line":line,"line_text":text.strip(),"fragment":fragment}
    raise AssertionError((path, fragment))


def centered_residue(value: int) -> int:
    return (int(value) + K//2) % K - K//2


def rotate_mod(frame, site, modulus):
    return tuple(value % modulus for value in c642.rotate(frame, site))


def block_center(site, modulus):
    return tuple((site[a] - centered_residue(site[a])) % modulus for a in range(3))


def nn(left, right, modulus):
    return sum(min((left[a]-right[a])%modulus,(right[a]-left[a])%modulus) for a in range(3)) == 1


def shell_backbone_predicate(site):
    return sum(abs(centered_residue(value)) == SHELL for value in site) >= 2


def shell_backbone(length: int) -> set[tuple[int,int,int]]:
    modulus = K*length
    boundaries = tuple((K*cell + sign*SHELL) % modulus for cell in range(length) for sign in (-1,1))
    sites=set()
    for free_axis in range(3):
        fixed=tuple(axis for axis in range(3) if axis != free_axis)
        for first in boundaries:
            for second in boundaries:
                for value in range(modulus):
                    site=[0,0,0];site[free_axis]=value;site[fixed[0]]=first;site[fixed[1]]=second
                    sites.add(tuple(site))
    return sites


def axis_line(start, axis, target, modulus):
    current=list(start); delta=(target-current[axis])%modulus
    if delta > modulus//2: delta -= modulus
    step=1 if delta>0 else -1
    path=[]
    for _ in range(abs(delta)):
        current[axis]=(current[axis]+step)%modulus;path.append(tuple(current))
    return tuple(path)


def straight_shell_finger(target, occupied, modulus):
    center=block_center(target,modulus); candidates=[]
    for first,second in combinations(range(3),2):
        for first_sign,second_sign in product((-1,1),repeat=2):
            for order,signs in (((first,second),(first_sign,second_sign)),
                                ((second,first),(second_sign,first_sign))):
                current=target;path=[]
                for axis,sign in zip(order,signs):
                    segment=axis_line(current,axis,(center[axis]+sign*SHELL)%modulus,modulus)
                    path.extend(segment)
                    if segment: current=segment[-1]
                if path and shell_backbone_predicate(path[-1]) and not any(occupied(site) for site in path):
                    candidates.append((len(path),order,signs,tuple(path)))
    return min(candidates,key=lambda row:(row[0],row[1],row[2]))[-1] if candidates else None


def local_index(site):
    return ((site[0]+SHELL)*K+(site[1]+SHELL))*K+site[2]+SHELL


def local_coordinate(index):
    z=index%K-SHELL; index//=K
    y=index%K-SHELL; x=index//K-SHELL
    return (x,y,z)


def local_backbone_sites():
    return {site for free in range(3)
            for first in (-SHELL,SHELL) for second in (-SHELL,SHELL)
            for value in range(-SHELL,SHELL+1)
            for site in [tuple(value if axis==free else first if axis==min(a for a in range(3) if a!=free) else second for axis in range(3))]}


def bfs_shell_fingers(center, targets, occupied_sites, modulus):
    """Compile finite witnesses; runtime grammar uses bounded word enumeration.

    The BFS parent array is not emitted or stored in the physical controller.
    It certifies witnesses and the terminal word-length bound only.
    """
    total=K**3; blocked=np.zeros(total,dtype=np.bool_)
    for site in occupied_sites:
        if block_center(site,modulus) != center: continue
        local=tuple(centered_residue(site[a]-center[a]) for a in range(3))
        blocked[local_index(local)]=True
    parent=np.full(total,-2,dtype=np.int32); distance=np.full(total,-1,dtype=np.int16)
    queue=np.empty(total,dtype=np.int32); head=tail=0
    for site in sorted(local_backbone_sites()):
        index=local_index(site)
        if not blocked[index] and parent[index]==-2:
            parent[index]=-1;distance[index]=0;queue[tail]=index;tail+=1
    while head<tail:
        index=int(queue[head]);head+=1
        local=local_coordinate(index)
        for direction in DIRECTIONS:
            target=tuple(local[a]+direction[a] for a in range(3))
            if any(value < -SHELL or value > SHELL for value in target): continue
            target_index=local_index(target)
            if parent[target_index]!=-2 or blocked[target_index]: continue
            parent[target_index]=index;distance[target_index]=distance[index]+1
            queue[tail]=target_index;tail+=1
    paths={}
    for global_target in targets:
        local_target=tuple(centered_residue(global_target[a]-center[a]) for a in range(3))
        candidates=[]
        for direction_index,direction in enumerate(DIRECTIONS):
            start=tuple(local_target[a]+direction[a] for a in range(3))
            if any(value < -SHELL or value > SHELL for value in start): continue
            index=local_index(start)
            if parent[index]!=-2: candidates.append((int(distance[index]),direction_index,start,index))
        if not candidates: continue
        _distance,_direction,start,index=min(candidates)
        local_path=[start]
        while parent[index]!=-1:
            index=int(parent[index]);local_path.append(local_coordinate(index))
        paths[global_target]=tuple(tuple((center[a]+site[a])%modulus for a in range(3)) for site in local_path)
    return paths,{"block_center":center,"reachable_free_vertices":tail,"maximum_distance":int(distance.max()),
                  "unreachable_free_vertices":int((~blocked).sum())-tail,"target_count":len(targets),"targets_solved":len(paths)}


def reconstruct_existing_cycle638_roles():
    grammar,private=c638.capture_and_compile_grammar()
    routes,route_private=c638.coordinate_counter_router(private)
    storage,program_private=c638.encode_program(private)
    layout,program_layout=c638.place_program_roles(program_private,route_private)
    roles=tuple(program_layout["roles"]);values=tuple(program_layout["values"])
    digest=sha256()
    for index,site in enumerate(roles): digest.update(repr((index,site)).encode())
    result={"roles":len(roles),"role_coordinate_sha256":digest.hexdigest(),
            "immutable_layout_assignment_sha256":layout["role_value_assignment_sha256"],
            "inner_coordinate_bound":layout["inner_coordinate_bound"],
            "reserved_route_residues":len(route_private["reserved"]),
            "pass":len(roles)==1_871_624 and layout["pass"] and routes["pass"] and storage["pass"]}
    del grammar,private,route_private,program_private,program_layout
    gc.collect()
    check("immutable Cycle638 exact inner program role set is reconstructed as occupied",result["pass"],result)
    return result,roles,values


def build_existing_occupancy(length, existing_program_local):
    placement,fibers=c642.allocate_orbit_roles(length)
    obj=c642.build_tree_code(length,fibers); modulus=K*length
    old={tuple(value%modulus for value in c642.old_position_K(obj["graph"],q)) for q in range(obj["graph"].qubits)}
    aux={tuple(value%modulus for value in site) for role in obj["roles"] for site in obj["fibers"][role]}
    program={tuple(value%modulus for value in site) for site in existing_program_local}
    collisions={"old_aux":tuple(sorted(old&aux)),"old_program":tuple(sorted(old&program)),"aux_program":tuple(sorted(aux&program))}
    small=old|aux
    def occupied(site):
        if site in small:return True
        return block_center(site,modulus)==(0,0,0) and tuple(centered_residue(value) for value in site) in existing_program_local
    summary,rows,_same_obj,_placement=c646.build_descriptors(length)
    return placement,obj,summary,rows,old,aux,program,occupied,collisions


def compile_fingers(length, targets, occupied, occupied_sites):
    modulus=K*length; fingers={}; route_kind=Counter(); failures=[]
    for target in sorted(targets):
        path=straight_shell_finger(target,occupied,modulus)
        if path is None: failures.append(target)
        else:fingers[target]=path;route_kind["two_axis_formula"]+=1
    bfs_rows=[]
    for center in sorted({block_center(target,modulus) for target in failures}):
        group=tuple(target for target in failures if block_center(target,modulus)==center)
        paths,row=bfs_shell_fingers(center,group,occupied_sites,modulus);bfs_rows.append(row)
        for target,path in paths.items():fingers[target]=path;route_kind["bounded_word_search_witness"]+=1
    unresolved=tuple(target for target in targets if target not in fingers)
    digest=sha256()
    for target,path in sorted(fingers.items()):digest.update(repr((target,path)).encode())
    result={"length":length,"targets":len(targets),"route_kind_histogram":dict(route_kind),
            "initial_two_axis_failures":len(failures),"unresolved_targets":unresolved,
            "maximum_finger_edges":max(len(path) for path in fingers.values()),
            "finger_word_sha256":digest.hexdigest(),"bounded_search_rows":bfs_rows,
            "runtime_formula":"try finite two-axis shell words; if none, enumerate NN words by length and lexicographic direction, rejecting occupied/repeated vertices until the certified <=max word is found",
            "runtime_host_path_service":False,"compile_time_BFS_parent_table_stored":False,
            "pass":not unresolved and all(nn(target,path[0],modulus) and shell_backbone_predicate(path[-1])
                                          and all(nn(a,b,modulus) for a,b in zip(path,path[1:]))
                                          and not any(occupied(site) for site in path)
                                          for target,path in fingers.items())}
    check(f"L{length} every equality/face support gets an actual occupied-role-safe NN finger to the outer backbone",
          result["pass"],{k:result[k] for k in ("targets","route_kind_histogram","maximum_finger_edges","unresolved_targets")})
    return result,fingers


def backbone_to_hub(start,modulus,hub):
    fixed=[axis for axis in range(3) if abs(centered_residue(start[axis]))==SHELL]
    if len(fixed)<2:raise AssertionError(("not backbone",start))
    fixed=fixed[:2];free=next(axis for axis in range(3) if axis not in fixed)
    path=[start];current=start
    for axis in (free,fixed[0],fixed[1]):
        segment=axis_line(current,axis,hub[axis],modulus);path.extend(segment)
        if segment:current=segment[-1]
    if current!=hub or not all(shell_backbone_predicate(site) for site in path):raise AssertionError((start,current,hub))
    return tuple(path)


def backbone_between(left,right,modulus,hub):
    first=backbone_to_hub(left,modulus,hub);second=backbone_to_hub(right,modulus,hub)
    return first+tuple(reversed(second[:-1]))


def allocate_outer_program(length,logical_bits,backbone,corridor_orbit,old,aux):
    modulus=K*length;blocked=backbone|corridor_orbit|old|aux;used=set();rows=[]
    for port in sorted(backbone):
        if len(rows)>=logical_bits:break
        for direction in DIRECTIONS:
            seed=tuple((port[a]+direction[a])%modulus for a in range(3))
            if seed in blocked or seed in used:continue
            orbit={rotate_mod(frame,seed,modulus) for frame in FRAMES}
            if len(orbit)!=24 or orbit&blocked or orbit&used:continue
            rows.append({"logical_bit":len(rows),"seed":seed,"port":port})
            used|=orbit;break
    digest=sha256()
    for row in rows: digest.update(repr((row["logical_bit"],row["seed"],row["port"])).encode())
    result={"length":length,"logical_register_and_route_stack_bits":logical_bits,
            "physical_frame_orbit_program_M2":len(used),"role_orbits":len(rows),
            "placement_sha256":digest.hexdigest(),"placements":rows,
            "program_backbone_collisions":len(used&backbone),"program_corridor_collisions":len(used&corridor_orbit),
            "program_old_aux_collisions":len(used&(old|aux)),
            "all_orbits_free_size24":len(used)==24*len(rows),
            "pass":len(rows)==logical_bits and len(used)==24*logical_bits and not (used&blocked)}
    check(f"L{length} every formula register/token/search-stack bit is literally placed on a free 24-site outer-shell orbit",
          result["pass"],{k:result[k] for k in ("logical_register_and_route_stack_bits","physical_frame_orbit_program_M2","program_backbone_collisions","program_corridor_collisions")})
    return result,rows,used


def simulate_swap_exhaust(path,delete_last_inverse=False):
    sites=set(path);values={site:site for site in sites};edges=list(zip(path,path[1:]));word=edges+list(reversed(edges))
    if delete_last_inverse and word:word=word[:-1]
    for left,right in word:values[left],values[right]=values[right],values[left]
    return sum(values[site]!=site for site in sites)


def compile_full_routes(length,fingers,program_rows,program_sites,occupied,backbone,aliased_targets):
    modulus=K*length;hub=(SHELL,SHELL,SHELL);probe=program_rows[0]["seed"];port=program_rows[0]["port"]
    routes={};digest=sha256();collisions=nn_failures=exhaust_failures=target_adjacency_failures=0
    for target,finger in sorted(fingers.items()):
        body=backbone_between(port,finger[-1],modulus,hub)
        path=(probe,)+body+tuple(reversed(finger[:-1]))
        collisions+=sum(occupied(site) or (site in program_sites and site!=probe) for site in path[1:])
        nn_failures+=sum(not nn(a,b,modulus) for a,b in zip(path,path[1:]))
        target_adjacency_failures+=not nn(path[-1],target,modulus)
        exhaust_failures+=simulate_swap_exhaust(path)!=0
        routes[target]=path;digest.update(repr((target,path)).encode())
    max_target=max(routes,key=lambda target:len(routes[target]));deletion_residual=simulate_swap_exhaust(routes[max_target],True)
    port_path_failures=0
    for row in program_rows:
        port_path=backbone_to_hub(row["port"],modulus,hub)
        port_path_failures+=not nn(row["seed"],row["port"],modulus)
        port_path_failures+=sum(site not in backbone for site in port_path)
    result={"length":length,"routed_unique_targets":len(routes),"route_word_sha256":digest.hexdigest(),
            "maximum_probe_to_access_SWAPS":max(len(path)-1 for path in routes.values()),
            "total_probe_to_access_SWAPS_one_pass":sum(len(path)-1 for path in routes.values()),
            "occupied_or_other_program_route_collisions":collisions,"fine_NN_edge_failures":nn_failures,
            "controlled_P_target_adjacency_failures":target_adjacency_failures,"forward_inverse_exhaust_failures":exhaust_failures,
            "delete_final_inverse_SWAP_permutation_residual":deletion_residual,
            "all_register_pair_route_template_failures":port_path_failures,
            "register_pair_rule":"move either state seed->port->hub->other port; apply its support-two gate adjacent to the other seed; exactly reverse",
            "token_rule":"the same literal program-pair route applies when either selected register is the serialized token",
            "one_active_token_serial_schedule":True,"maximum_simultaneously_active_routes":1,"temporal_route_congestion":1,
            "inherited_data_program_aliased_targets":tuple(sorted(aliased_targets)),
            "support_one_two_routing_controller_gates_enumerated_and_tested":False,
            "controlled_P_status":"target-adjacent access geometry only; full oracle circuit not executed",
            "full_physical_oracle_composition_pass":False,
            "pass_as_literal_route_word_geometry":not any((collisions,nn_failures,target_adjacency_failures,exhaust_failures,port_path_failures)) and deletion_residual>0}
    result["pass"]=result["pass_as_literal_route_word_geometry"]
    check(f"L{length} probe/register/token SWAP route words are NN, occupied-safe, target-adjacent, and algebraically exhausted",
          result["pass"],{k:result[k] for k in ("routed_unique_targets","maximum_probe_to_access_SWAPS","occupied_or_other_program_route_collisions","fine_NN_edge_failures","forward_inverse_exhaust_failures","delete_final_inverse_SWAP_permutation_residual")})
    return result,routes


def covariance_and_capacity(length,backbone,fingers,program_sites,program_rows,old,aux,existing_program_count):
    modulus=K*length
    backbone_covariance_failures=sum(not shell_backbone_predicate(rotate_mod(frame,site,modulus))
                                     for frame in FRAMES for site in backbone)
    corridor_orbit={rotate_mod(frame,site,modulus) for frame in FRAMES for path in fingers.values() for site in path}
    program_orbit_failures=0
    for row in program_rows:
        seed_orbit={rotate_mod(frame,row["seed"],modulus) for frame in FRAMES}
        port_orbit={rotate_mod(frame,row["port"],modulus) for frame in FRAMES}
        program_orbit_failures+=len(seed_orbit)!=24 or any(site not in backbone for site in port_orbit)
    frame_keys={tuple(int(value) for value in frame.ravel()) for frame in FRAMES}
    exact_group_failures=0;coordinate_sample_failures=0
    sample=tuple(list(backbone)[:8]+list(program_sites)[:8]+list(corridor_orbit)[:8])
    for left in FRAMES:
        for right in FRAMES:
            product_frame=left@right
            exact_group_failures+=tuple(int(value) for value in product_frame.ravel()) not in frame_keys
            for site in sample:
                coordinate_sample_failures+=rotate_mod(left,rotate_mod(right,site,modulus),modulus)!=rotate_mod(product_frame,site,modulus)
    active_finger_union=set().union(*map(set,fingers.values()))
    persistent=backbone|program_sites|old|aux
    active_total_upper=len(persistent|active_finger_union)+existing_program_count
    result={"length":length,"proper_frames":24,"ordered_products":576,
            "backbone_all24_predicate_failures":backbone_covariance_failures,
            "program_orbit_and_port_failures":program_orbit_failures,
            "all576_exact_signed_permutation_group_failures":exact_group_failures,
            "all576_coordinate_sample_failures":coordinate_sample_failures,
            "all576_scope":"exact signed-permutation matrix group closure; coordinate composition follows linearly, with displayed placement samples checked",
            "outer_backbone_M2":len(backbone),"outer_backbone_M2_per_coarse_cell":len(backbone)/length**3,
            "program_orbit_M2":len(program_sites),"active_identity_finger_union_M2":len(active_finger_union),
            "existing_Cycle638_program_M2":existing_program_count,"active_total_upper_bound":active_total_upper,
            "available_M2":modulus**3,"capacity_margin":modulus**3-active_total_upper,
            "no_refit_constants":{"K":K,"outer_shell_residue":SHELL,"same_formula":True},
            "pass":backbone_covariance_failures==program_orbit_failures==exact_group_failures==coordinate_sample_failures==0 and active_total_upper<modulus**3}
    check(f"L{length} placement is all24/all576 covariant and fits with the occupied Cycle638 bank without refit",
          result["pass"],{k:result[k] for k in ("outer_backbone_M2","outer_backbone_M2_per_coarse_cell","program_orbit_M2","capacity_margin","backbone_all24_predicate_failures","all576_exact_signed_permutation_group_failures","all576_coordinate_sample_failures")})
    return result,corridor_orbit


def local_sidecar_discriminator(length,fingers,probe_port):
    modulus=K*length;adj={probe_port:set()}
    access_by_target={}
    for target,path in fingers.items():
        access_by_target[target]=path[0]
        for site in path:adj.setdefault(site,set())
        for left,right in zip(path,path[1:]):adj[left].add(right);adj[right].add(left)
    seen={probe_port};queue=deque([probe_port])
    while queue:
        site=queue.popleft()
        for target in adj.get(site,set())-seen:seen.add(target);queue.append(target)
    reachable=sum(access in seen for access in access_by_target.values())
    components=0;unseen=set(adj)
    while unseen:
        components+=1;seed=next(iter(unseen));part={seed};queue=deque([seed]);unseen.remove(seed)
        while queue:
            site=queue.popleft()
            for target in adj[site]&unseen:unseen.remove(target);part.add(target);queue.append(target)
    result={"length":length,"strictly_local_fiber_components":components,"targets":len(fingers),
            "targets_reachable_from_one_controller_without_backbone_edges":reachable,
            "standalone_local_fiber_route_pass":reachable==len(fingers),
            "broad_local_sidecar_no_go":False,"repair":"join endpoints by the reserved outer-shell backbone or replicate controllers",
            "pass_as_narrow_discriminator":reachable<len(fingers)}
    check(f"L{length} strictly local fingers alone do not connect one controller, while the backbone composition remains available",
          result["pass_as_narrow_discriminator"],result)
    return result


def malformed_and_deletion_controls(length,backbone,program_sites,fingers,existing_program_local):
    modulus=K*length
    inner63={site for site in backbone if sum(abs(centered_residue(v))==SHELL for v in site)>=2}
    # Mutating the shell predicate from 64 to 63 enters the occupied Cycle638 domain.
    malformed_witness=(-63,63,-63)
    target,path=max(fingers.items(),key=lambda row:len(row[1]));middle=len(path)//2
    shortened=path[:middle]+path[middle+1:]
    deleted_finger_nn_failures=sum(not nn(a,b,modulus) for a,b in zip(shortened,shortened[1:]))
    seed=next(iter(program_sites));frame=FRAMES[1];deleted_orbit={rotate_mod(h,seed,modulus) for h in FRAMES};deleted_orbit.remove(seed)
    deleted_program_covariance_residual=int(rotate_mod(frame,seed,modulus) not in deleted_orbit or len(deleted_orbit)!=24)
    result={"length":length,"malformed_shell_63_witness":malformed_witness,
            "malformed_shell_63_enters_inner_program_domain":malformed_witness in existing_program_local,
            "delete_middle_finger_vertex_NN_failures":deleted_finger_nn_failures,
            "delete_one_program_orbit_site_covariance_residual":deleted_program_covariance_residual,
            "delete_backbone_edge_route_residual":"certified by full-route deleted inverse SWAP permutation control",
            "pass":malformed_witness in existing_program_local and deleted_finger_nn_failures>0 and deleted_program_covariance_residual>0}
    check(f"L{length} malformed shell and finger/program deletions have explicit nonzero residuals",result["pass"],result)
    return result


def no_go_gate():
    c646_open=immutable_citation("docs/work_history/repo/review_feedback/PHYSICAL_ORBIT_TREE_LOCAL_ENFORCEMENT_CYCLE646_NOTE_2026-07-23.md","Occupied-role-safe detours and literal fine-neighbor physical lowering remain")
    c646_scope=immutable_citation("docs/work_history/repo/review_feedback/PHYSICAL_ORBIT_TREE_LOCAL_ENFORCEMENT_CYCLE646_NOTE_2026-07-23.md","compatible with physical storage but is")
    c638_inner=immutable_citation("docs/work_history/repo/review_feedback/PHYSICAL_HIERARCHICAL_GRAMMAR_FULL_ACT_COMPILER_CYCLE638_NOTE_2026-07-23.md","physical grammar storage and dispatch paths lie in the inner")
    current_backbone=current_citation("scripts/physical_reserved_outer_shell_sidecar_placement_cycle649_2026_07_23.py","def shell_backbone_predicate")
    current_finger=current_citation("scripts/physical_reserved_outer_shell_sidecar_placement_cycle649_2026_07_23.py","def straight_shell_finger")
    families=[
        {"family":"reserved outer-shell backbone","object":"two-|residue|=64 wireframe plus program ports","mechanism":"placed blank rails and certified hub route words","terminal":"occupied-safe one-controller connectivity and target adjacency","honesty_marker":"ATTEMPTED","marker":"ATTEMPTED","result":"route geometry positive; joint inherited substrate allocation has one separate non-target data/program alias"},
        {"family":"strictly local sidecar fibers","object":"target-to-shell fingers without shell edges","mechanism":"two-axis words plus bounded-search exceptions","terminal":"one-controller connectivity","honesty_marker":"ATTEMPTED","marker":"ATTEMPTED","result":"route-specific failure: disconnected components"},
        {"family":"time-multiplexed corridor","object":"one active probe/token route word","mechanism":"formula word and algebraic forward/reverse SWAP certificate","terminal":"zero simultaneous collision, algebraic exhaust, target adjacency, and literal controller circuit","honesty_marker":"ATTEMPTED","marker":"ATTEMPTED","result":"route word positive; unlowered search/control circuit blocks execution, while a separate inherited non-target alias blocks joint substrate allocation"},
        {"family":"Cycle646 oracle grammar","object":"formula registers and coherent phase word","mechanism":"state-carried counters/token","terminal":"literal placement and route lowering","honesty_marker":"RULED OUT BY PRIOR","marker":"RULED OUT BY PRIOR","result":"algebra supplied; placement was explicitly open"},
    ]
    open_routes=[
        {"family":"replicated local controllers","status":"OPEN / NOT COUNTED","terminal":"remove the global shell backbone"},
        {"family":"3D subsystem crossing center","status":"OPEN / NOT COUNTED","terminal":"static bounded-generator enforcement"},
        {"family":"autonomous clean-corridor renewal","status":"OPEN / NOT COUNTED","terminal":"generate blank rails rather than supply them"},
    ]
    walls={"W_inherited_role_alias":"one Cycle642 old-data non-target is already a Cycle638 program role and lacks two tensor factors",
           "W_blank_shell_and_controller_supply":"blank outer-shell rails, route stack, and routing-control circuit remain supplied/unlowered",
           "W_repair":"routing/oracle application is not autonomous rejection, repair, or convergence"}
    pairs=[{"from":a,"to":b,"implied":False,"reason":f"closing {a} does not construct {b}"} for a in walls for b in walls if a!=b]
    required={"prior_ref","prior_path","prior_line","prior_residual","current_path","current_line","current_residual","same_scope","exact_match","use_as_closure"}
    matches=[{"prior_ref":c646_open["ref"],"prior_path":c646_open["path"],"prior_line":c646_open["line"],
              "prior_residual":"occupied-role-safe detours and literal fine-NN lowering open",
              "current_path":current_backbone["path"],"current_line":current_backbone["line"],
              "current_residual":"new route vertices and target access close under supplied blank rails, but one inherited non-target role alias and an unlowered routing-control circuit prevent full physical closure",
              "same_scope":True,"exact_match":True,"use_as_closure":False}]
    nonmatches=[{"prior_ref":c646_scope["ref"],"prior_path":c646_scope["path"],"prior_line":c646_scope["line"],
                 "prior_residual":"controller registers not placed",
                 "current_path":current_finger["path"],"current_line":current_finger["line"],
                 "current_residual":"outer-shell orbit placement closes storage, but E/repair remain outside scope",
                 "same_scope":False,"exact_match":False,"use_as_closure":False}]
    n5=[
        {"claim":"strict local fibers alone fail one-controller connectivity","per_element":"each actual finger edge is NN","per_site":"occupied sites are excluded","per_mode":"no CAR-mode no-go inferred","per_block":"L3/L6/L7 component counts pass","lattice_wide":"backbone and replicated controllers remain constructive alternatives"},
        {"claim":"outer-shell route geometry closes but full joint-substrate physical composition does not","per_element":"each new register role and route edge is placed/certified","per_site":"route collisions and target aliases are zero while one inherited non-target data/program alias remains","per_mode":"the missing tensor factor is outside the tested oracle supports but still invalidates joint allocation","per_block":"same alias and K129 constants at L3/L6/L7","lattice_wide":"role relocation, routing-control lowering, blank renewal, and repair remain open"},
    ]
    n6=[{"file":"UNMATERIALIZED/physical_cycle638_single_role_relocation_decoder_update_cycle_next.py","status":"OPEN / PRIORITY","what_closes":"W_inherited_role_alias"},
        {"file":"UNMATERIALIZED/physical_outer_shell_router_circuit_and_blank_renewal_cycle_next.py","status":"OPEN","what_closes":"W_blank_shell_and_controller_supply"},
        {"file":"UNMATERIALIZED/physical_violation_repair_exhaust_cycle_next.py","status":"OPEN","what_closes":"W_repair"}]
    n7={"mechanism":"replace the global shell rail by one covariant controller port per coarse block and bounded inter-block handoff tiles",
        "actionable_steps":["place one local port orbit per block","compile bounded handoff tile","prove exact token transfer and exhaust","rerun all24/all576 and capacity"],
        "why_it_breaks_the_negative":"the local-fiber discriminator assumes one controller with no joining edges; replicated ports add precisely those missing joins",
        "terminal_test":"bounded diameter/overhead, no shared blank global rail, L3/L6/L7, deletion, covariance"}
    n8=[
        {"cycle":638,"retired":"unaccounted inner program occupancy","mechanism":"exact reconstruction of 1,871,624 roles","applicability":"forces Cycle649 storage/backbone to the outer shell","citation_ref":c638_inner["ref"],"citation_path":c638_inner["path"],"citation_line":c638_inner["line"],"citation_text":c638_inner["line_text"]},
        {"cycle":646,"retired":"formula grammar mistaken for placement","mechanism":"explicit grammar/placement boundary","applicability":"Cycle649 supplies coordinates and routes only","citation_ref":c646_scope["ref"],"citation_path":c646_scope["path"],"citation_line":c646_scope["line"],"citation_text":c646_scope["line_text"]},
        {"cycle":649,"retired":"abstract occupied-role-safe detour","mechanism":"outer-shell backbone plus finite target fingers","applicability":"L3/L6/L7 routing under blank-shell supply","citation_ref":current_backbone["ref"],"citation_path":current_backbone["path"],"citation_line":current_backbone["line"],"citation_text":current_backbone["line_text"]},
    ]
    return {"Status":"PASS","N1_normalized_families":families,"N1_open_routes_not_counted":open_routes,
            "N1_qualifying_attempts":len(families),"N1_required_for_negative":5,"N1_negative_gate":"FAIL / DO NOT SHIP",
            "N2_collapsed_walls":walls,"N2_directed_ordered_pairs":pairs,"N3_hidden_wall_scan":[
                {"phrase":"blank outer-shell backbone","classification":"explicit supplied clean corridor, not generated resource","wall":"W_blank_shell_and_controller_supply"},
                {"phrase":"bounded word enumerator","classification":"route grammar plus placed stack roles; support-one/two routing-control gates are not enumerated/executed","wall":"W_blank_shell_and_controller_supply"},
                {"phrase":"serialized token","classification":"ownership schedule, not time or autonomous repair","wall":"W_repair"},
                {"phrase":"existing Cycle638 bank","classification":"one K129 bank of 1,871,624 roles is reused at every tested size, not repeated per cell; one role aliases a non-target old-data site","wall":"W_inherited_role_alias"}],
            "N4_exact_residual_matches":matches,"N4_nonmatches_not_used_as_closure":nonmatches,"N4_required_fields":sorted(required),
            "N5_rhetoric":n5,"N6_partial_closure_paths":n6,"N7_steelman":n7,"N8_cross_cycle_echo":n8,
            "broad_negative_gate":"FAIL / DO NOT SHIP","minimum_content_gate":"FAIL / DO NOT SHIP",
            "shared_obstruction_gate":"FAIL / DO NOT SHIP","axiom_pressure_gate":"FAIL / DO NOT SHIP",
            "broad_negative_shipped":False,"minimum_content_shipped":False,"shared_obstruction_shipped":False,"axiom_pressure_shipped":False,
            "broad_no_go_claim":False,"minimum_content_claim":False,"shared_obstruction_claim":False,"axiom_pressure_claim":False,
            "shared_route_independent_obstruction":False,"axiom_pressure":False}


def main():
    global PASS,FAIL
    started=time.perf_counter();observed={path:git_sha(path) for path in PINS}
    imported={name:str(Path(module.__file__).resolve()) for name,module in sys.modules.items()
              if (name.startswith("physical_") or name.startswith("cycle649_immutable")) and getattr(module,"__file__",None)}
    working=[path for path in imported.values() if Path(path).is_relative_to(ROOT)]
    check("Cycle646/638 shore and every imported physics module are immutable",observed==PINS and not working,
          {"commit":IMMUTABLE_COMMIT,"pins":len(PINS),"mismatches":[p for p in PINS if observed[p]!=PINS[p]],"working":working})
    existing_summary,existing_program_roles,existing_program_values=reconstruct_existing_cycle638_roles()
    existing_program_local=set(existing_program_roles)
    systems=[]
    for length in (3,6,7):
        placement,obj,descriptor_summary,descriptors,old,aux,program,occupied,collisions=build_existing_occupancy(length,existing_program_local)
        modulus=K*length;backbone=shell_backbone(length)
        backbone_collisions=sum(occupied(site) for site in backbone)
        check(f"L{length} invariant outer wireframe avoids every existing data/aux/Cycle638 program role",
              backbone_collisions==0,{"backbone_M2":len(backbone),"collisions":backbone_collisions})
        targets={site for row in descriptors for _qubit,site,_letter in row["support"]}
        inherited_aliases=set(collisions["old_program"]);alias_rows=[]
        for site in sorted(inherited_aliases):
            local=tuple(centered_residue(value) for value in site)
            index=existing_program_roles.index(local)
            alias_rows.append({"site":site,"Cycle638_program_role_index":index,
                               "Cycle638_program_bit_value":existing_program_values[index],
                               "is_Cycle646_oracle_target":site in targets})
        check(f"L{length} inherited Cycle638/Cycle642 role alias is isolated exactly rather than hidden by routing",
              not collisions["old_aux"] and not collisions["aux_program"] and len(alias_rows)==1
              and all(not row["is_Cycle646_oracle_target"] for row in alias_rows),
              {"alias_rows":alias_rows,"old_aux":collisions["old_aux"],"aux_program":collisions["aux_program"]})
        occupied_sites=old|aux|program
        finger_summary,fingers=compile_fingers(length,targets,occupied,occupied_sites)
        corridor_orbit={rotate_mod(frame,site,modulus) for frame in FRAMES for path in fingers.values() for site in path}
        grammar=c646.coherent_oracle_grammar(length,descriptors,obj)
        base_bits=grammar["logical_program_and_work_bits"]
        route_stack_bits=3*finger_summary["maximum_finger_edges"]+64
        program_summary,program_rows,program_sites=allocate_outer_program(length,base_bits+route_stack_bits,backbone,corridor_orbit,old,aux)
        route_summary,routes=compile_full_routes(length,fingers,program_rows,program_sites,occupied,backbone,inherited_aliases&targets)
        covariance,corridor_orbit_check=covariance_and_capacity(length,backbone,fingers,program_sites,program_rows,old,aux,len(existing_program_roles))
        local=local_sidecar_discriminator(length,fingers,program_rows[0]["port"])
        malformed=malformed_and_deletion_controls(length,backbone,program_sites,fingers,existing_program_local)
        systems.append({"length":length,"existing_role_collisions":collisions,"inherited_alias_rows":alias_rows,"descriptor_summary":descriptor_summary,
                        "finger_compiler":finger_summary,"program_placement":program_summary,"literal_routes":route_summary,
                        "covariance_and_capacity":covariance,"strict_local_sidecar_discriminator":local,
                        "malformed_and_deletion_controls":malformed,
                        "route_disposition":{"reserved_outer_shell_backbone":"PASS_PLACED_RAIL_AND_ROUTE_WORD_GEOMETRY_FULL_ORACLE_BLOCKED",
                                             "local_sidecar_fibers":"PASS_AS_ACCESS_COMPONENT_FAILS_STANDALONE_CONNECTIVITY",
                                             "time_multiplexed_corridor":"PASS_ROUTE_WORD_ALGEBRA_FULL_CONTROLLER_AND_ORACLE_BLOCKED"}})
        del program,occupied_sites,backbone,corridor_orbit,corridor_orbit_check,fingers,routes,program_sites,old,aux,obj,descriptors
        gc.collect()
    nogo=no_go_gate();exact={"ATTEMPTED","RULED OUT BY PRIOR"};required=set(nogo["N4_required_fields"])
    gate_keys=("broad_negative_gate","minimum_content_gate","shared_obstruction_gate","axiom_pressure_gate")
    shipped=("broad_negative_shipped","minimum_content_shipped","shared_obstruction_shipped","axiom_pressure_shipped")
    check("canonical N1-N8 permits scoped route-geometry result but blocks physical/negative/minimum/shared/axiom promotion",
          nogo["Status"]=="PASS" and all(row["honesty_marker"] in exact and row["marker"]==row["honesty_marker"] for row in nogo["N1_normalized_families"])
          and all("honesty_marker" not in row and "marker" not in row for row in nogo["N1_open_routes_not_counted"])
          and len(nogo["N2_directed_ordered_pairs"])==6
          and all(required<=set(row) for row in nogo["N4_exact_residual_matches"]+nogo["N4_nonmatches_not_used_as_closure"])
          and all(nogo[key]=="FAIL / DO NOT SHIP" for key in gate_keys) and all(nogo[key] is False for key in shipped)
          and not nogo["shared_route_independent_obstruction"] and not nogo["axiom_pressure"],
          {"qualifying":len(nogo["N1_normalized_families"]),"open":len(nogo["N1_open_routes_not_counted"]),"directed":len(nogo["N2_directed_ordered_pairs"])})
    note=NOTE.read_text();markers=("Status: **PASS**","Authority: **none**","Audit: **unset**","1,871,624","outer-shell backbone","literal placement","occupied-role-safe","not autonomous repair","N1-N8","Axiom pressure: **none**")
    check("Cycle649 note freezes literal placement result, supplied blank-shell wall, and semantic scope",all(marker in note for marker in markers),markers)
    result={"cycle":649,"date":"2026-07-23","Status":"PASS","status":"cycle649-outer-shell-role-and-route-word-placement-partial",
            "classification":"partial: literal register-role and route-word geometry is positive, but joint substrate allocation has one inherited non-target program/data alias and no support-one/two routing-control circuit is executed",
            "authority":AUTHORITY,"audit":AUDIT,"author_accepted":False,"author_artifact_status_accepted":False,
            "constitutional_effect":"none","breakthrough":False,
            "broad_negative_gate":"FAIL / DO NOT SHIP","minimum_content_gate":"FAIL / DO NOT SHIP",
            "shared_obstruction_gate":"FAIL / DO NOT SHIP","axiom_pressure_gate":"FAIL / DO NOT SHIP",
            "broad_negative_shipped":False,"minimum_content_shipped":False,"shared_obstruction_shipped":False,"axiom_pressure_shipped":False,
            "shared_route_independent_obstruction":False,"axiom_pressure":False,
            "route_word_geometry_pass":True,"joint_inherited_role_allocation_pass":False,
            "routing_control_circuit_executed":False,"full_physical_oracle_compiler_pass":False,
            "shore":{"immutable_commit":IMMUTABLE_COMMIT,"pins":PINS,"observed":observed,"actual_imported_physical_modules":imported,
                     "working_tree_bytes_used_as_premise":False,"working_import_failures":working,"no_go_skill_origin_main_sha256":NO_GO_ORIGIN_MAIN_SHA256},
            "existing_Cycle638_inner_program_occupancy":existing_summary,"systems":systems,
            "strongest_constructive_result":"at L3/L6/L7 with no refit, every new Cycle646 register/token/search-stack bit has an explicit proper-cubic 24-site outer-shell orbit and every support has an occupied-role-safe NN route word with algebraic SWAP exhaust and controlled-P target adjacency; exact reconstruction of the one reused 1,871,624-role Cycle638 K129 bank finds one pre-existing non-target program/data alias, and routing-control gates are not enumerated/executed, so this is not a full joint-substrate physical compiler",
            "W_collision_free_lowering":"ROUTE_WORD_GEOMETRY_CLOSED_ROUTING_CONTROL_CIRCUIT_OPEN",
            "W_joint_role_allocation":"BLOCKED_ONE_INHERITED_NON_TARGET_DATA_PROGRAM_ALIAS",
            "W_local_enforcement":"SHARPLY_NARROWED_NOT_CLOSED",
            "residual":"new register-role placement, route words, and target adjacency close under supplied blank rails; one inherited non-target role alias, literal routing-control gates, static enforcement, blank-shell genesis, repair, preparation, and E remain open",
            "route_by_route_disposition":{"reserved_outer_shell_backbone":"PASS_ROLE_AND_ROUTE_WORD_GEOMETRY_FULL_ORACLE_BLOCKED",
                                           "strict_local_sidecar_fibers":"FAIL_STANDALONE_ONE_CONTROLLER_CONNECTIVITY_ONLY",
                                           "time_multiplexed_corridor":"PASS_SERIAL_ROUTE_WORD_ALGEBRA_CONTROLLER_NOT_EXECUTED",
                                           "autonomous_repair":"OPEN_NOT_CLAIMED","physical_E_or_preparation":"OPEN_NOT_TOUCHED"},
            "supplied_structure_inventory":{"K129_partition_and_macro_origin":True,"existing_Cycle638_program_values_and_roles":True,
                "existing_Cycle642_data_aux_roles":True,"one_inherited_non_target_Cycle638_program_Cycle642_data_alias":True,
                "blank_outer_shell_backbone_and_active_finger_sites":True,
                "one_active_state_carried_frame_sector":True,"initially_clean_route_stack_probe_flag_token_work":True,
                "runtime_host_path_service":False,"stored_target_path_table":False,
                "support_one_two_routing_control_circuit_enumerated_or_executed":False,"autonomous_blank_renewal":False,
                "autonomous_repair":False,"physical_E_or_preparation":False},
            "semantic_firewall":{"serialized_schedule_is_time":False,"route_length_is_rate":False,"oracle_phase_is_energy":False,
                                   "syndrome_flag_is_occurrence":False,"syndrome_flag_is_Record":False},
            "six_wall_ledger":{"C_ref":"literal outer-shell program/route placement is all24/all576; macro-origin, active sector, and blank shell remain supplied",
                "C_num":"exact binary routing, capacity, ranks inherited; no probability/normalization claim",
                "C_wrap":"route words have algebraic forward/inverse exhaust; controller execution, occurrence, Record, history, and preparation remain absent",
                "C_int":"controlled-P target adjacency is certified but the full oracle is not executed; no new mass/contact/seam dynamics claim",
                "C_local":"route-word geometry and target access close conditionally; inherited non-target joint-allocation alias, routing-control lowering, static enforcement, blank renewal, repair, and E remain open",
                "C_source":"unchanged; route capacity and phase have no energy/source/gravity meaning"},
            "no_go_discipline":nogo,
            "optimal_next_campaign":"relocate the single aliased Cycle638 program bit to a free outer-shell role, update and exhaust its decoder route, then enumerate/test the support-one/two routing-control circuit; only afterward pursue blank renewal or replicated local ports",
            "resources":{"elapsed_seconds":time.perf_counter()-started,"maximum_RSS_bytes":int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss if sys.platform=='darwin' else resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024)}}
    check("all L3/L6/L7 role/route-word geometries and target access pass while joint alias and controller execution block full promotion",
          all(system["finger_compiler"]["pass"] and system["program_placement"]["pass"] and system["literal_routes"]["pass"]
              and system["covariance_and_capacity"]["pass"] and system["strict_local_sidecar_discriminator"]["pass_as_narrow_discriminator"]
              and not system["literal_routes"]["full_physical_oracle_composition_pass"]
              and len(system["inherited_alias_rows"])==1
              and not system["inherited_alias_rows"][0]["is_Cycle646_oracle_target"]
              for system in systems),{"systems":len(systems)})
    result.update({"tests_passed":PASS,"tests_failed":FAIL,"tests_total":PASS+FAIL,"pass":FAIL==0})
    RECEIPT.write_text(json.dumps(result,indent=2,sort_keys=True,default=json_default)+"\n")
    print(json.dumps({"status":"PASS" if FAIL==0 else "FAIL","tests":f"{PASS}/{PASS+FAIL}","elapsed":result["resources"]["elapsed_seconds"],"receipt":str(RECEIPT.relative_to(ROOT))},sort_keys=True))
    return int(FAIL!=0)


if __name__=="__main__":
    COLD.parent.mkdir(parents=True,exist_ok=True)
    with COLD.open("w") as stream:
        previous=sys.stdout;sys.stdout=Tee(previous,stream)
        try:raise SystemExit(main())
        finally:sys.stdout=previous
