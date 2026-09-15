AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=('docs/NATIVE_L6_NONLINEAR_STAR_VERTEX_NOTE_2026-09-09.md', 'docs/NATIVE_THIRD_ORDER_STAR_VERTEX_NOTE_2026-09-08.md', 'docs/work_history/repo/review_feedback/pr8061-proof-sources/kept/pr8061-proof-adapted_frame-4eb81c02792f3306.md', 'docs/work_history/repo/review_feedback/pr8061-proof-sources/kept/pr8061-proof-four_solve-eff578cafd7f48f7.md', 'docs/work_history/repo/review_feedback/pr8061-proof-sources/kept/pr8061-proof-projection-e801411de605cecc.md', 'docs/work_history/repo/review_feedback/pr8061-proof-sources/kept/pr8061-proof-real_error-57d49d5cf78c0e3e.md', 'docs/work_history/repo/review_feedback/pr8061-proof-sources/kept/pr8061-proof-real_sign-c2692f5746303191.md', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/ADAPTED.json', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/BLOCKS.json', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/COEFFICIENTS.json', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/LEDGER.json', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/TRANSPORTS.json', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/VECTOR_MANIFEST.json', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/accepted/INDEPENDENT_REVIEW.json', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/accepted/RESULT.json', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/accepted/ROOT_ACCEPTANCE.json', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/accepted/WORKER_COMPLETE.json', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/accepted/firstO_candidate.json', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/accepted/firstP_candidate.json', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/accepted/secondO_candidate.json', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/accepted/secondP_candidate.json', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/vectors/chi_real.bin.gz', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/vectors/chi_real.npy.gz', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/vectors/firstO.bin.gz', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/vectors/firstO.npy.gz', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/vectors/firstP.bin.gz', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/vectors/firstP.npy.gz', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/vectors/secondO.bin.gz', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/vectors/secondO.npy.gz', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/vectors/secondP.bin.gz', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/vectors/secondP.npy.gz', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/vectors/sourceO.bin.gz', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/vectors/sourceO.npy.gz', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/vectors/sourceP.bin.gz', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/vectors/sourceP.npy.gz')
"""Same-process candidate certificate prerequisite; never changes FP environment."""
import ctypes,sys,platform,struct,hashlib

def check():
 import numpy as np
 # FE_TONEAREST is0 on the explicitly supported Darwin/Linux ABIs.
 if sys.platform not in ('darwin','linux'):raise RuntimeError('unreviewed fenv ABI')
 libc=ctypes.CDLL(None);get=getattr(libc,'fegetround',None)
 if get is None:raise RuntimeError('fegetround unavailable')
 get.argtypes=[];get.restype=ctypes.c_int
 if get()!=0:raise RuntimeError('rounding mode is not FE_TONEAREST')
 def array(bits):return np.array(bits,dtype=np.uint64).view(np.float64)
 def bitlist(a):return [int(v) for v in a.view(np.uint64)]
 rows=[]
 # Expectations are literal IEEE binary64 bit patterns, not host arithmetic.
 cases=[
 ('multiply_normal_ties','multiply',[0x3ff0000000000001,0x3ff0000000000003],[0x3ff8000000000000]*2,[0x3ff8000000000002,0x3ff8000000000004]),
 ('add_ties_even','add',[0x3ff0000000000000,0x3ff0000000000001,0xbff0000000000000,0xbff0000000000001],[0x3ca0000000000000,0x3ca0000000000000,0xbca0000000000000,0xbca0000000000000],[0x3ff0000000000000,0x3ff0000000000002,0xbff0000000000000,0xbff0000000000002]),
 ('multiply_subnormal_ties','multiply',[1,3,0x8000000000000001,0x8000000000000003],[0x3fe0000000000000]*4,[0,2,0x8000000000000000,0x8000000000000002]),
 ('gradual_result','multiply',[0x0010000000000000,0x8010000000000000],[0x3fe0000000000000]*2,[0x0008000000000000,0x8008000000000000]),
 ('subnormal_input_no_daz','multiply',[1,0x000fffffffffffff,0x8000000000000001],[0x3ff0000000000000]*3,[1,0x000fffffffffffff,0x8000000000000001]),
 ('boundary_add','add',[0x000fffffffffffff,1,0x0010000000000000,0x8010000000000000],[1,1,0x800fffffffffffff,0x000fffffffffffff],[0x0010000000000000,2,1,0x8000000000000001]),
 ('signed_zero_add','add',[0,0x8000000000000000,0,0x3ff0000000000000],[0x8000000000000000,0x8000000000000000,0,0xbff0000000000000],[0,0x8000000000000000,0,0]),
 ('signed_zero_product','multiply',[0,0x8000000000000000,0,0x8000000000000000],[0xbff0000000000000,0xbff0000000000000,0x3ff0000000000000,0x3ff0000000000000],[0x8000000000000000,0,0,0x8000000000000000])]
 # Replication exercises array-loop paths, including full SIMD blocks/tails.
 for name,op,left,right,expected in cases:
  for repeat in (1,17):
   x=array(left*repeat);y=array(right*repeat)
   # Suppress only diagnostic warnings locally; no rounding/FTZ mutation.
   with np.errstate(under='ignore'):z=getattr(np,op)(x,y)
   actual=bitlist(z)
   if actual!=expected*repeat:raise RuntimeError('FP bit-pattern mismatch '+name)
   if not np.isfinite(z).all():raise RuntimeError('unexpected nonfinite')
   rows.append(dict(name=name,repeat=repeat,outputs=[hex(v) for v in actual]))
 if get()!=0:raise RuntimeError('rounding mode changed during check')
 return dict(status='PASS',rounding_mode=0,platform=sys.platform,machine=platform.machine(),numpy_version=np.__version__,numpy_origin=np.__file__,cases=rows,scope='same-process fenv and exercised NumPy ufunc bit patterns only; not universal IEEE proof')
if __name__=='__main__':
 if len(sys.argv)!=1:raise SystemExit('no arguments')
 import json
 print(json.dumps(check(),indent=2))
