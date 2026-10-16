from pathlib import Path
import runpy
p=Path(__file__).resolve().parent
src=p.parent/'probe_network_history_v2.py'
original=Path.write_text
def redirected(self,data,*a,**k):
    if self==src.parent/'NETWORK_HISTORY_CONTROLS_v2.json':
        return original(p/'reproduced_controls_v2.json',data,*a,**k)
    raise RuntimeError('Unapproved write '+str(self))
Path.write_text=redirected
runpy.run_path(str(src),run_name='__main__')
