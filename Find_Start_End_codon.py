import re
import fasta

reader = fasta.FastaReader('orf_coding_all.fa')
count = {'ALL': 0}
for head, seq in reader.data.items():
    match = re.search(r'^(ATG)[ATGC]*(TAA|TGA|TAG)$', seq)
    if match is not None:
        codon = match.group(2)
        count[codon] = count.get(codon, 0) + 1
        count['ALL'] += 1
print('Number of yeast coding sequences with start and end codons: {}'.format(count['ALL']))
print('Number of ORFs with TAA end codon: {}, {:.2%} of all ORFs'.format(count['TAA'], count['TAA'] / count['ALL']))
print('Number of ORFs with TGA end codon: {}, {:.2%} of all ORFs'.format(count['TGA'], count['TGA'] / count['ALL']))
print('Number of ORFs with TAG end codon: {}, {:.2%} of all ORFs'.format(count['TAG'], count['TAG'] / count['ALL']))
print('done')
