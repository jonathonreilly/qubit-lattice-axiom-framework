#!/usr/bin/env python3
"""Assemble the self-contained runner from personal, separately checked prototypes."""
from pathlib import Path
import re

PACK=Path(__file__).resolve().parent.parent
DELIVERY=Path('/Users/jonreilly/Documents/Codex/toe-periodic-gaussian-codec-20260914')


def definitions(name):
    text=(PACK/name).read_text()
    text=text.split('\ndef main():')[0]
    return re.sub(r'^from block4_[^\n]+\n','',text,flags=re.M)


def body(name,function):
    text=(PACK/name).read_text().split('\ndef main():',1)[1].split("\n\nif __name__",1)[0]
    text=re.sub(r'^    Path\(__file__\).*\n','',text,flags=re.M)
    text=text.replace('    print(json.dumps(result,indent=2))','    return result')
    return '\ndef '+function+'():'+text+'\n'


def main():
    sections=['''#!/usr/bin/env python3
"""Finite checks of a supplied periodic Gaussian compiler and equivariant codecs.

All scientific definitions used by this primary runner are below. It reads
no repository scientific inputs. Finite checks challenge the accompanying
all-volume derivations; they are not independent audit or native law selection.
"""
AUDIT_TIMEOUT_SEC = 180
''']
    sections.append(definitions('block4_codec_relay_check.py'))
    sections.append(definitions('block4_closed_codec_check.py').replace('EPS','CLOSED_EPS'))
    sections.append(body('block4_closed_codec_check.py','closed_codec_checks').replace('EPS','CLOSED_EPS'))
    sections.append(definitions('block4_periodic_routing_check.py'))
    sections.append(body('block4_periodic_routing_check.py','periodic_cases'))
    sections.append(definitions('block4_routing_stress_check.py'))
    sections.append(body('block4_routing_stress_check.py','routing_stress_cases'))
    sections.append(definitions('block4_record_cluster_check.py'))
    record=body('block4_record_cluster_check.py','record_cluster_cases')
    record=re.sub(r'^    source=json.loads.*\n','',record,flags=re.M)
    record=re.sub(r'^    assert list\(source.*\n','',record,flags=re.M)
    record=record.replace("source_revision=source['source_sha256'],ports=[8,1,1]",
                          "template='supplied finite Record cluster',ports=[8,1,1]")
    record=record.replace('actual finite-fixture cluster port/geometry match; periodic DK source still not matched',
                          'supplied protected cluster geometry; no periodic DK source-family claim')
    sections.append(record)
    sections.append(definitions('block4_spectral_check.py'))
    sections.append('''
def main():
    result = dict(codec=codec_checks(),
                  measure=measure_checks(),
                  closed_support_codec=closed_codec_checks(),
                  exact_relay=relay_checks(),
                  periodic_map=periodic_cases(),
                  routing_stress=routing_stress_cases(),
                  protected_cluster=record_cluster_cases(),
                  massive_spectral_bounds=spectral_checks(),
                  status='author_checked_finite_witnesses; independent_review_pending',
                  open='source/action/measure selection, periodic DK family and autonomous formation')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
''')
    text='\n\n'.join(sections)
    # Only the first shebang/module string is the execution header.
    text=text.replace('\n#!/usr/bin/env python3\n','\n')
    destination=DELIVERY/'scripts/periodic_gaussian_full_payload_matrix_codec_2026_09_14.py'
    destination.write_text(text)
    print(destination)


if __name__=='__main__':
    main()
