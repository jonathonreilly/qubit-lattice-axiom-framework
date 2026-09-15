from pathlib import Path
import sys,json,difflib,subprocess,hashlib
w=Path('/private/tmp/review-drain-20260915/author-pool/author-backlog');o=Path('/private/tmp/review-drain-20260915');orig=o/'unit8058';sys.path[:0]=[str(w/'docs/audit/scripts'),str(w/'scripts')]
import build_citation_graph as g,audit_packet_script_deps as p,runner_cache as c
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();git=lambda *a:subprocess.check_output(['git','-C',str(w),*a],text=True).strip();paths=git('diff','--cached','--name-only').splitlines();primaries=['scripts/native_zero_penalty_l4_delayed_splitting_2026_09_08.py','scripts/native_weak_electric_spectator_gap_2026_09_08.py','scripts/native_third_order_star_vertex_2026_09_08.py'];outputs=['outputs/native_zero_penalty_l4_delayed_splitting_2026_09_08.json','outputs/native_weak_electric_spectator_gap_2026_09_08.json','scripts/native_third_order_star_vertex_2026_09_08.json'];inputs={};discovery={}
for n in primaries:
 helper=g.resolve_helper_runner_paths(n);discovery[n]={'graph':helper,'packet':sorted(p.transitive_helpers(Path(n).stem))}
 for x in [n]+helper:
  for k in c.declared_input_paths(x) or ():inputs[k]=sha(w/k)
r={'role':'author preexecution source freeze, not independent verdict','base':git('rev-parse','HEAD'),'source_tree':git('write-tree'),'worktree':str(w),'source_sha256':{x:sha(w/x) for x in paths if x not in outputs},'input_sha256':inputs,'original_output_sha256':{x:sha(w/x) for x in outputs},'primaries':primaries,'helper_discovery':discovery,'timeout_sec':180,'rss_cap_mib':384};(o/'8058-author-preexecution.json').write_text(json.dumps(r,indent=2)+'\n')
s=''
for n in subprocess.check_output(['git','-C',str(orig),'diff','--cached','--name-only'],text=True).splitlines():
 if n.endswith(('.py','.md')):s+=''.join(difflib.unified_diff((orig/n).read_text().splitlines(True),(w/n).read_text().splitlines(True),fromfile='original/'+n,tofile='author/'+n))
(o/'8058-author-correction.diff').write_text(s);print(r['source_tree'],len(paths),len(inputs))
# Original immutable science input bytes must not change.
for n in paths:
 if '/native_weak_electric_spectator_gap_2026_09_08_inputs/' in n and not n.endswith('INPUT_HASHES.json'):assert (w/n).read_bytes()==(orig/n).read_bytes(),n
