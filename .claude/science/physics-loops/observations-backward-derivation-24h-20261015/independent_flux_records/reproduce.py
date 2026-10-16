from pathlib import Path
import runpy
p=Path(__file__).resolve().parent
src=p.parent/'probe_flux_records_v1.py'
original=Path.write_text
def redirect(self,data,*a,**k):
    if self==src.parent/'FLUX_RECORD_CONTROLS_v1.json':
        return original(p/'reproduced_controls.json',data,*a,**k)
    raise RuntimeError('Unexpected write '+str(self))
Path.write_text=redirect
runpy.run_path(str(src),run_name='__main__')
