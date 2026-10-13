"""R19-16: run an UNMODIFIED R19-9 (or referee) script from orig/ against the REPAIRED kernel.
Usage: python3 r1916_run.py <script in orig/> [args...]
lib1916 is imported first; it patches the lib199 module object, which the script then receives from `import lib199`."""
import os, sys, runpy
import lib1916                                           # noqa: F401  (patches lib199 in place)
HERE = os.path.dirname(os.path.abspath(__file__))
script = os.path.join(HERE, 'orig', sys.argv[1])
sys.argv = [script] + sys.argv[2:]
print(f'[r1916_run] {os.path.basename(script)} {" ".join(sys.argv[1:])} with the REPAIRED kernel (lib1916 patch active: '
      f'sig/cfun analytic, divdiff uniform, piece_A Neumann both sides)', flush=True)
runpy.run_path(script, run_name='__main__')
