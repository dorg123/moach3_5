import re
import fasta

reader = fasta.FastaReader('orf_trans_all.fa')
count = 0
for head, seq in reader.data.items():
    match = re.findall(r'C[A-Z]H[A-Z][LIVMFY]C[A-Z]{2}C[LIVMYA]', seq)
    if len(match) > 0:
        count += 1
        print('>{}\n{}'.format(head, '\n'.join(match)))
print('Number of proteins contain Zinc Finger Motif: {}'.format(count))
print('done')
