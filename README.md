# Identification of Viral Polymerase Program
This is the repository created for the first project of the subject Programming fundamentals for biological sciences.
National University of Colombia (UNAL).

The following program was made for comparing a template or target sequence, 
from a section of the genome of a polymerase from a strain of Influenza type A virus (H1N1),
with the genome of the polymerase from any strain of Influenza, or any virus from the same family, Orthomyxoviridae.

The steps for downloading the target sequence from NCBI are:
#### 1) Head to NCBI through the link https://www.ncbi.nlm.nih.gov/
#### 2) Type on the search bar "<ins>_influenza virus polymerase complete genome_</ins>" or something similar
#### 3) Select the one you prefer the most, click on <ins>FASTA</ins> and "<ins>Change region shown</ins>"
![image](https://github.com/user-attachments/assets/278c5098-ace4-445f-826d-732fff8d18b0)
#### 4) Then, "<ins>Selected region</ins>" and input the range from which you desire to extract the template
![image](https://github.com/user-attachments/assets/ebff3b41-40f9-4139-ac56-6080eecfd4e4)
#### 5) Go ahead and download the FASTA file like such:
![image](https://github.com/user-attachments/assets/dc0ebe4a-886a-4db2-8a15-206333cbefbf)
#### 6) Done! Now, repeat the steps excluding the range selecting part, and download every sequence that you'd like to compare the template with.
#### 7) The final step would be opening the code and modify the routes and file names as you have them. (The code is commented as well, so it's more intuitive)

## Example of the execution of the program and its outputs as a .txt file:

#### Using the same file where the target sequence was taken from, but without the range configuration:
![image](https://github.com/user-attachments/assets/3f833014-e6a4-478d-9a64-ee182a6a702e)


#### Using another file:
![image](https://github.com/user-attachments/assets/569f6c15-24e9-421c-a390-f80bfce544f3)


### I also uploaded several fasta files usefull for running the code:
#### *confirmation_h1n1.fasta* is the same file where the target sequence was taken from, but without the range configuration, this is the proof that the code works.
#### *target_seq_2.fasta* the target sequence used, with range 600-700


## DISCLAIMER: for this program to work correctly, there needs to be a 100% identity between the sequences to compare.
