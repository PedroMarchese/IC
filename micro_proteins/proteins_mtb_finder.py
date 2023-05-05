import numpy as np
import pandas as pd
from Bio import SeqIO
import os
import sys

reference_proteome = []
pep_results: pd.Series = None


def read_files():
    # return print(os.getcwd())
    base_path = 'micro_proteins\\data'
    
    global reference_proteome
    global pep_results
    
    pep_results = pd.read_csv(f'{base_path}\\all_pep_results_final.txt', sep='\t')
    pep_results = pep_results['proteinIds']
    
    with open(f'{base_path}\\mtb_proteome_cat.fasta', 'r') as handle:
        for record in SeqIO.parse(handle, 'fasta'):
            reference_proteome.append(record.id)
            
        reference_proteome = pd.Series(reference_proteome)
        

def main():
    read_files()
    print('Read files')
    
    separated_peps = pep_results.str.split(';').explode()
    print(separated_peps)
    
main()    