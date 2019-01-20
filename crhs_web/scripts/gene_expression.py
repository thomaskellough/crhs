from random import choice

nucleotide_list = ['A', 'T', 'G', 'C']
stop_codon_dna = ['ATT', 'ATC', 'ACT']
start_codon = 'AUG'
stop_codon = ['UAA', 'UAG', 'UGA']

mRNA_dict = {'A': 'U',
             'T': 'A',
             'G': 'C',
             'C': 'G'}

tRNA_dict = {'A': 'U',
             'U': 'A',
             'C': 'G',
             'G': 'C'}

codon_dict = {'Phe': ['UUU', 'UUC'],
              'Leu': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
              'Ile': ['AUU', 'AUC', 'AUA'],
              'Met': ['AUG'],
              'Val': ['GUU', 'GUC', 'GUA', 'GUG'],
              'Ser': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
              'Pro': ['CCU', 'CCC', 'CCA', 'CCG'],
              'Thr': ['ACU', 'ACC', 'ACA', 'ACG'],
              'Ala': ['GCU', 'GCC', 'GCA', 'GCG'],
              'Tyr': ['UAU', 'UAC'],
              'His': ['CAU', 'CAC'],
              'Gln': ['CAA', 'CAG'],
              'Asn': ['AAU', 'AAC'],
              'Lys': ['AAA', 'AAG'],
              'Asp': ['GAU', 'GAC'],
              'Glu': ['GAA', 'GAG'],
              'Cys': ['UGU', 'UGC'],
              'Trp': ['UGG'],
              'Arg': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
              'Gly': ['GGU', 'GGC', 'GGA', 'GGG'],
              'STOP': ['UAA', 'UAG', 'UGA']}


def dict_to_list(dict_of_codons):
    return [[k, v] for k, v in dict_of_codons.items()]


def create_random_sequence(number):
    sequence = 'TAC' + ''.join(choice(nucleotide_list) for _ in range(number)) + choice(stop_codon_dna)
    return sequence


def transcribe(sequence):
    return ''.join(mRNA_dict[nucleotide] for nucleotide in sequence)


def mRNA_to_tRNA(sequence):
    return ''.join(tRNA_dict[nucleotide] for nucleotide in sequence)


def translate(sequence):
    try:
        # Find start codon
        start_index = sequence.index(start_codon)
        start_peptide_chain = sequence[start_index:]

        # Find stop codon
        peptide_chain = []
        for nucleotide in range(0, len(start_peptide_chain), 3):
            codon = start_peptide_chain[nucleotide] \
                    + start_peptide_chain[nucleotide + 1] \
                    + start_peptide_chain[nucleotide + 2]
            peptide_chain.append(codon)
            if codon in stop_codon:
                break

        # Determine amino acid
        amino_acids = {n: k for k, v in codon_dict.items() for n in v}
        amino_acids_list = [amino_acids[codon] for codon in peptide_chain]
        # Return a string of amino acids
        aa_string = '-'.join(amino_acids_list)
        return aa_string
    except (IndexError, ValueError):
        return 'No protein found'
