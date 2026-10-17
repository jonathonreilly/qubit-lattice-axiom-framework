import sys, pickle, subprocess, time
sys.path.insert(0, '/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/c2')
from module_tool import singular_script
ACTION = sys.argv[1]; orbs = [int(v) for v in sys.argv[2].split(',')]
d = pickle.load(open(f'orb3q_{ACTION}.pkl', 'rb')); elems = d['elems']
STAR = [(0,0,0),(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
def dec(a): return [((int(a) >> (6*i)) & 63) for i in range(7)]
gens = []
for k in orbs:
    for e in elems[k]:
        l = dec(e); gens.append({STAR[i]: tuple((l[i] >> (2*a)) & 3 for a in range(3)) for i in range(7) if l[i]})
fn = f'ext_{ACTION}_{"_".join(map(str, orbs))[:60]}.sing'
open(fn, 'w').write(singular_script(gens, 3, 'c'))
t0 = time.time()
out = subprocess.run(['/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/indep_check/runsing.sh', fn], stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=int(sys.argv[3]) if len(sys.argv) > 3 else 1800).stdout
mob = out.split('3D-mobile charge exists)?')[1].split()[0] if '3D-mobile' in out else '?'
ann = out.split('Ann(Ext^3) saturated:')[1].split('minimal primes')[0].strip().replace('\n', ' ') if 'saturated:' in out else ''
print(orbs[:6], len(gens), 'gens: mobile3D =', mob, '| Ann(Ext3):', ann[:120], f'| {time.time()-t0:.0f}s', flush=True)
