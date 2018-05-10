import re
import fasta

reader = fasta.FastaReader('orf_coding_all.fa')
with open('List_Yeast_ORFs_RestSites.txt', 'w') as f:
    count = 0
    for title, seq in reader.data.items():
        f.write('>{}'.format(title))
        dsai_matches = re.findall(r'CCGCGG|CCGTGG|CCACGG|CCATGG', seq)
        seci_matches = re.findall(r'CC[ATGC]{2}GG', seq)
        cjul_matches = re.findall(r'CA[CT][ATGC]{5}[AG]TG', seq)
        if len(dsai_matches) + len(seci_matches) + len(cjul_matches) > 0:
            count += 1
        if len(dsai_matches):
            f.write('There are {} DsaI sites:\n'.format(len(dsai_matches)))
            for m in dsai_matches:
                f.write('DsaI site: {}\n'.format(m))
        if len(seci_matches):
            f.write('There are {} SecI sites:\n'.format(len(seci_matches)))
            for m in seci_matches:
                f.write('SecI site: {}\n'.format(m))
        if len(cjul_matches):
            f.write('There are {} Cjul sites:\n'.format(len(cjul_matches)))
            for m in cjul_matches:
                f.write('Cjul site: {}\n'.format(m))
    f.write('Number of protein with any kind of site: {}'.format(count))
print('done')
