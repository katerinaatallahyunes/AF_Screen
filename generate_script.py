#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 11:18:42 2023

@author: atallahyuneska
"""

import os

# Specify the path to the folder containing the FASTA files
fasta_folder = "/Users/atallahyuneska/Library/CloudStorage/OneDrive-NationalInstitutesofHealth/OReilly_group/Users/Katerina/Projects/CycD/FASTA/combined_fasta/Homeobox"

# Specify the directory where you want to save the Slurm scripts
output_directory = "/Users/atallahyuneska/Library/CloudStorage/OneDrive-NationalInstitutesofHealth/OReilly_group/Users/Katerina/Projects/CycD/Scripts/"

# Template for the Slurm batch script (split into two parts)
template_part1 = """#!/bin/bash
#SBATCH --job-name={job_name}
#SBATCH --cpus-per-task=8
#SBATCH --partition=gpu
#SBATCH --time=10-00:00:00
#SBATCH --gres=gpu:2
#SBATCH --mem=100g
#SBATCH --mail-user=
#SBATCH --mail-type=ALL

module load alphafold/2.3.2_conda
"""

template_part2 = """run \\
--model_preset=multimer \\
--fasta_paths={fasta_path} \\
--max_template_date=2020-05-14 \\
--output_dir= \\
--use_gpu_relax=false \\
--num_multimer_predictions_per_model=1
"""

# Iterate through FASTA files in the folder
for filename in os.listdir(fasta_folder):
    if filename.endswith(".fasta"):
        # Extract the job name from the filename (without the .fasta extension)
        job_name = os.path.splitext(os.path.basename(filename))[0]
        
        # Combine the two template parts with a line break between them
        slurm_script = template_part1.format(job_name=job_name) + "\n" + template_part2.format(job_name=job_name, fasta_path=os.path.join("../../../FASTA/",filename))
        
        # Define the output script filename (e.g., job_script.sh) with the desired output directory
        output_script_filename = os.path.join(output_directory, f"{job_name}_script.sh")
        
        # Write the Slurm script to the output file
        with open(output_script_filename, "w") as output_file:
            output_file.write(slurm_script)

        print(f"Generated Slurm script for {filename}: {output_script_filename}")



