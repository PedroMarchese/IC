import numpy as np
import pandas as pd
from Bio import SeqIO
import os
import sys

base_path = 'micro_proteins\\data'

reference_proteome = []
pep_results: pd.Series = None


def read_files():
    global reference_proteome
    global pep_results
    
    pep_results = pd.read_csv(f'{base_path}\\all_pep_results_final.txt', sep='\t')
    pep_results = pep_results['proteinIds']
    
    with open(f'{base_path}\\mtb_proteome_cat.fasta', 'r') as handle:
        for record in SeqIO.parse(handle, 'fasta'):
            reference_proteome.append(record.id)
            
        reference_proteome = pd.Series(reference_proteome)
        reference_proteome.name = 'proteinIds'
        

def main():
    read_files()
    print('Reading files...')
    
    separated_peps = pep_results.str.split(';').explode()
    separated_peps = separated_peps.reset_index(drop=True)
    separated_peps.name = 'proteinIds'
    print(f'Length: {separated_peps.size}')
    print('All proteins splitted!')
    
    intersection_peps = separated_peps[separated_peps.isin(reference_proteome)].unique()
    print(intersection_peps.size)
    
    pd.DataFrame(intersection_peps, columns=['proteinIds']).to_csv(f'{base_path}\\intersection_peps.csv', index=False, sep='\t')
    
    
main()    