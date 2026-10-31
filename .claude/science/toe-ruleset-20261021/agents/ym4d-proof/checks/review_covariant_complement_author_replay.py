from pathlib import Path
import hashlib
source_path=Path(__file__).with_name('covariant_complement_01.py')
source=source_path.read_text()
assert source.count('covariant_complement_01_results.json')==1
# Output-basename routing only; all mathematics, predicates and exit handling retained.
source=source.replace('covariant_complement_01_results.json','review_covariant_complement_author_results.json')
exec(compile(source,str(source_path),"exec"),{"__name__":"__main__","__file__":str(source_path)})
