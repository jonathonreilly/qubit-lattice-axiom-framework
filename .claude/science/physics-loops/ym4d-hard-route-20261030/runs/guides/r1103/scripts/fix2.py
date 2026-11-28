import sys
p=sys.argv[1]; t=open(p,encoding='utf-8').read()
def rep(a,b):
    global t
    assert t.count(a)==1, (t.count(a), a[:70])
    t=t.replace(a,b)
rep("""$2.64\\,c_{1/2}^4\\le0.19$ in the window.""", """$2.64\\,c_{1/2}^4\\le0.20$ in the window.""")
rep("""**What this run did not cover** (kept current):
- (filled in as the run goes; see the end of each step)
""", """**What this run did not cover** (kept current; final state):
- **The nine check files were read in part, not in full** (RESULT lines of
  all nine; three passages of two of them). The row asked for full reading.
  Their verdicts were taken from `parts/gap.md` L156-168, read in full.
- Of `parts/gap.md` only L156-168 and L221-275 were read. The other 380
  `gap` files of `library/`, the other rows of `FINISH.md`, `checks/` and
  `library/open-registry.md` were searched by `grep` only. Rows 859, 962,
  998, 1053 and 1063 enter through the grepped lines quoted in step 5.
- Open PR branches and `main` were not searched. So no item is called new;
  the strongest mark is "not found in the lane folder".
- Literature: Durhuus-Fröhlich 1980, Osterwalder-Seiler 1978, Borgs-Seiler
  1983, Fröhlich 1979, Bhanot-Creutz 1981, Fu-Nielsen 1984 and Koma 2010
  were not read (recalled or abstract-level). Fingberg-Heller-Karsch: Table 5
  only, through a fetch tool. The two OpenAI preprints and the Hexagon
  preprint were not read by this run (row 1104's reading is used).
  Cao-Nissim-Sheffield arXiv:2509.04688v2: pages 1-4 read.
- No literature search was made for the mixed-only corner of route F4. Its
  prior art is unknown to this run.
- No blind check of the plain version. No check by another model. The
  passes of step 7 are by one writer and are not independent.
- (F4-KP) is not proved; the entropy bound is not written. The corner
  "$K_4$ minus an edge" was not analysed. Rates of forests other than the
  star were not written out. C2' with one short side was not analysed.
- Two exact enumeration runs (guides). No Monte Carlo. No Lean.
""")
open(p,'w',encoding='utf-8').write(t)
print('ok')
