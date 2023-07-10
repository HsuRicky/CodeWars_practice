# https://www.codewars.com/kata/554e4a2f232cdd87d9000038
def DNA_strand(dna):
    comp = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G',}
    return ''.join([comp[i] for i in dna])