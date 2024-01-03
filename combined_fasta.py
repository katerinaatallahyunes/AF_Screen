#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 10:53:07 2023

@author: atallahyuneska
"""
import os

def read_fasta_file(file_path):
    sequences = {}
    current_header = ""
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                current_header = line
                sequences[current_header] = ""
            else:
                sequences[current_header] += line
    return sequences

def write_fasta_file(file_path, sequences):
    with open(file_path, "w") as file:
        for header, sequence in sequences.items():
            file.write(header + "\n")
            file.write(sequence + "\n")

def main():
    fasta_folder_path = '/fasta/path' #Replace with folder path that has all the raw fastas 
    appended_fasta_path = '/fasta/path' #Replace with the fasta file path of the protein of interest for the screen
    output_fasta_path = '/fasta/path' #Replace with the folder path where you want all the new fastas to be saved 
    
    for filename in os.listdir(fasta_folder_path):
        input_file = os.path.join(fasta_folder_path, filename)  # Join folder path with filename
        appended_fasta = appended_fasta_path

        # Read the existing sequences
        existing_sequence = read_fasta_file(input_file)
    
        # Read the new sequence file and add it to the existing sequences
        new_sequence = read_fasta_file(appended_fasta)
        existing_sequence.update(new_sequence)
    
        # Construct the output file name based on input file and new sequence name
        output_file = os.path.join(output_fasta_path, filename.replace(".fasta", "_name.fasta"))
        
        # Append the new sequences to the input file and write to the output file
        write_fasta_file(output_file, existing_sequence)

if __name__ == "__main__":
    main()

