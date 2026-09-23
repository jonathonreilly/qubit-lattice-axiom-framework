import pathlib,json,hashlib,difflib,ast
R=pathlib.Path('/private/tmp/review-drain-20260915');W=R/'review-draft-slot';sha=lambda b:hashlib.sha256(b).hexdigest()
v=json.loads((R/'drain8031-author-prepared-v1.json').read_text());assert all(sha((W/x['path']).read_bytes())==x['sha256'] for x in v['source'])
n=next(x['path'] for x in v['source'] if x['path'].startswith('docs/GAUGE_'));p='scripts/gauge_wilson_finite_transporter_pw_defect_check_2026_09_07.py'
before=(W/n).read_text();rb=(W/p).read_text()
for name,data in [('drain8031-canonical-note-snapshot-v1.md',before),('drain8031-canonical-runner-snapshot-v1.py',rb)]:
 assert not (R/name).exists();(R/name).write_text(data)
a=before.index('## 1. Conditional Cartan trace-square identities');b=before.index('## 2. Actual Haar link')
section='''## 1. Tensor trace-square identity

Let H be a nonzero finite-dimensional Hilbert space, Q any Hermitian operator on H, and T any traceless Hermitian 3-by-3 matrix. Write Qbar=Q tensor I3 and Tbar=I_H tensor T. Direct expansion and factorization of the tensor trace give

 Tr(Qbar+Tbar)²=Tr Qbar²+dim(H) Tr T²,

because the cross term is2Tr_H(Q)Tr_3(T)=0. Replacing Tbar by −Tbar gives the same square contribution. This is a tensor trace identity; no transporter covariance or unitary-similarity hypothesis is imposed in this live statement. The original negative proof, including its conditional similarity and character arguments and one-sided-isometry corollary, is preserved completely in the exact recovery archive. Its formal negative certification is deferred, not mathematically refuted.

'''
after=before[:a]+section+before[b:]
a=after.index('The original root proof also records');b=after.index('For inverse link orientation',a)
after=after[:a]+'''The historical root proof's conditional character argument and group-convention discussion remain complete in the exact archive. They are not conclusions of this live bounded row. The following supplied-compression and state-comparison details remain affirmative parts of the result.

'''+after[b:]
after=after.replace('Conditional trace algebra and the exact supplied-compression norm identity are preserved; universal negative conclusions remain deferred.','The tensor trace identity and exact supplied-compression norm identity are retained; the universal negative proof is archived and its certification deferred.')
(W/n).write_text(after);ra=rb.replace(sha(before.encode()),sha(after.encode()));assert ra!=rb;(W/p).write_text(ra);ast.parse(ra)
assert rb.replace(sha(before.encode()),'PIN')==ra.replace(sha(after.encode()),'PIN')
assert before[before.index('## 2. Actual Haar link'):before.index('## Appendix A.')]==after[after.index('## 2. Actual Haar link'):after.index('## Appendix A.')]
patch=''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile=n+'@v1',tofile=n+'@v2'))+''.join(difflib.unified_diff(rb.splitlines(True),ra.splitlines(True),fromfile=p+'@v1',tofile=p+'@v2'))
(R/'drain8031-author-corrections-v2.patch').write_text(patch)
v['stage']='untracked author preparation v2; affected independent confirmation pending';v['source']=[{'path':x['path'],'sha256':sha((W/x['path']).read_bytes())} for x in v['source']];v['runtime_inputs'][n]=sha(after.encode());v['proof_mapping']['native']='Complete positive PW/energy/path sections retained; negative conditional similarity proof preserved exact in archive, live section1 only arbitrary tensor trace identity';v['proof_mapping']['root']='Positive orientation/interior/state-distance details retained in Appendix A; complete negative character/convention proof exact in archive';v['historical_v1_snapshots']=[{'path':str(R/f),'sha256':sha((R/f).read_bytes()),'status':'historical author proposal, not live accepted claim'} for f in ['drain8031-canonical-note-snapshot-v1.md','drain8031-canonical-runner-snapshot-v1.py']];v['verification']['positive_sections_2_to_5_byte_identical_to_v1']=True;v['evidence_references']+=['drain8031-author-prepared-v1.json','drain8031-author-corrections-v2.patch'];v['verification']['full_v2_diff_read']='pending author read'
(R/'drain8031-author-prepared-v2.json').write_text(json.dumps(v,indent=2)+'\n');print(patch)
