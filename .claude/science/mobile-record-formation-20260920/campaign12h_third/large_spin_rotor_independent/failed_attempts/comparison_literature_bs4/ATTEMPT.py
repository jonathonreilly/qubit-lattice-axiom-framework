from pathlib import Path
from bs4 import BeautifulSoup
p=Path('/Users/jonreilly/Documents/Codex/mobile-record-formation-20260920/.claude/science/mobile-record-formation-20260920/campaign12h_third/large_spin_rotor_independent/comparison_literature/Zohar_Cirac_Reznik_1303_5040v3.html')
s=BeautifulSoup(p.read_text(),'html.parser')
for e in s.find_all('section'):
 h=e.find(['h2','h3','h4'],recursive=False)
 if h and ('finite number of bosons' in h.get_text()):
  print(e.get('id'));print(e.get_text(' ',strip=True))
