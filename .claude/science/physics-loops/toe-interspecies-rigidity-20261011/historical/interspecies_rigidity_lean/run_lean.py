from pathlib import Path
import os, sys, subprocess, time, json, hashlib

D = Path(__file__).resolve().parent
OLD = D.parent / 'lean_audit'
runtime = OLD / 'lean-4.35.0-rc4-darwin_aarch64'
source = (D / sys.argv[1]).resolve()
label = sys.argv[2]
assert source.is_relative_to(D)
logs = D / 'logs'
logs.mkdir(exist_ok=True)
for name in ('tmp', 'cache', 'cache/xdg', 'lake_home'):
    (D / name).mkdir(parents=True, exist_ok=True)
snapshot = logs / (label + '.lean')
assert not snapshot.exists(), 'Preserve previous attempts: choose a fresh label'
snapshot.write_bytes(source.read_bytes())
env = dict(os.environ, PATH=str(runtime/'bin')+os.pathsep+os.environ['PATH'],
           MATHLIB_CACHE_DIR=str(D/'cache'), XDG_CACHE_HOME=str(D/'cache/xdg'),
           LAKE_HOME=str(D/'lake_home'), TMPDIR=str(D/'tmp'),
           LEAN_PATH=str(D))
cmd = [str(runtime/'bin/lake'), 'env', 'lean', '-R', str(D), str(source),
       '-o', str(D / (source.stem + '.olean'))]
t = time.monotonic()
try:
    p = subprocess.run(cmd, cwd=OLD/'mathlib', env=env, text=True,
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=120)
    code, output = p.returncode, p.stdout
except subprocess.TimeoutExpired as ex:
    code, output = 124, ex.stdout or ''
    if isinstance(output, bytes): output = output.decode()
    output += '\nPROCESS TIMEOUT after 120 seconds\n'
(logs/(label+'.log')).write_text(output)
(logs/(label+'.json')).write_text(json.dumps({'command':cmd,'cwd':str(OLD/'mathlib'),
    'exit':code,'elapsed_seconds':time.monotonic()-t,'timeout_seconds':120,
    'source_snapshot':str(snapshot),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
    'environment_overrides':{k:env[k] for k in ('MATHLIB_CACHE_DIR','XDG_CACHE_HOME','LAKE_HOME','TMPDIR','LEAN_PATH')},
    'path_prepend':str(runtime/'bin')},indent=2)+'\n')
print(output)
print('COMPILER_EXIT', code)
sys.exit(code)
