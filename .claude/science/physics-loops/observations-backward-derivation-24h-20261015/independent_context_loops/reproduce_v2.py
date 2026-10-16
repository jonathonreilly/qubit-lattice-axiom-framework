from pathlib import Path
import runpy
p=Path(__file__).resolve().parent
src=p.parent/'probe_context_loops_v2.py'
original=Path.write_text
def redirect(self,data,*a,**k):
    if self==src.parent/'CONTEXT_LOOP_CONTROLS_v2.json':
        return original(p/'reproduced_controls_v2.json',data,*a,**k)
    raise RuntimeError('Unexpected write '+str(self))
Path.write_text=redirect
runpy.run_path(str(src),run_name='__main__')
