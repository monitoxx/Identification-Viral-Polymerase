"""
Please, read the README.md and LICENSE files beforehand in my GitHub repository:
https://github.com/monitoxx/Identification-Viral-Polymerase

The following code was made by me (https://github.com/monitoxx) , with some help from Gemini Assistant for finding errors.
The comments provide a really self-explanatory experience from now on.
Reach me at my email for any doubts: ljimenezbe@unal.edu.co
"""
def find_polymerase_sequence_in_fasta(fasta_file, target_sequence):
    """
    Finds a target nucleotide sequence within the FASTA file.
    fasta_file (str): Path to the FASTA file.
    target_seq (str): The target nucleotide sequence to search for.
    The Gen Bank reference is: DQ508888.1, it was filtered from the 600 to the 700th position and downloaded.
    """

    with open(target_sequence, 'r') as file: #Converts to the right format the target sequence so it can be used.
        sequence = ''
        for line in file:
            if line.startswith('>'):
                temp = line.strip('>').split(' ')
                _temp = (str(temp[0])).split(':') #Temporary variable for extracting FASTA code and range
                target_code = _temp[0] #Extracts the FASTA code
                target_range = _temp[1] #Extracts the range used
            else:
                sequence += line.strip()
                #print(sequence) #Just a test

    clean_target_sequence = sequence #The resulting clean sequence
    target_seq_genbank_code = target_code
    target_seq_genbank_range = target_range

    with open(fasta_file, 'r') as file: #The same as before but with the complete polymerase file
        sequence = ""
        for line in file:
            if line.startswith('>'):
                temp = line.strip('>').split(' ') #Temporary variable for extracting the FASTA code
                fasta_code = temp[0] #Extracts the FASTA code
            else:
                sequence += line.strip()
                #print(sequence) #Just a test

    clean_fasta_file = sequence #The resulting clean sequence
    fasta_file_genbank_code = fasta_code

    finder = clean_fasta_file.find(clean_target_sequence) #Finder compares the sequences, if it is not found, (.find) returns -1

    #Getting the codes, range and results off the function:
    results_of_function = [fasta_file_genbank_code, target_seq_genbank_code, target_seq_genbank_range]
    if finder == -1:
        results_of_function.append(0)
        return results_of_function
    else:
        results_of_function.append(1)
        return results_of_function


#------MODIFY ONLY THIS------
fasta_file = ('sequences_folder/confirmation_h1n1.fasta')
target_sequence = 'sequences_folder/target_seq_2.fasta'
#------MODIFY ONLY THIS------

file_route = fasta_file.split('.')[0] #Gives the route to the file
file_name = file_route.split('/')[1]  #Gives the name of the file


##------Results of the analysis------##
output_file = open('analysis_results.txt', 'w') #Creates the file containing the analysis result


result = find_polymerase_sequence_in_fasta(fasta_file, target_sequence) #Executes the function


#Writes the output file:
output_file.write(f'The analysis results for the file "{file_name}" are the following:\n\n')
if result[-1] == 1:
    output_file.write(f'\tTARGET SEQUENCE FOUND!!!\n\n\tThis program found similarities between the target polymerase with code: {result[1]} and range {result[2]},\n\tand the polymerase with code {result[0]} both from GenBank.\n\t')
    output_file.write(f'\n\t-->Hence, there seems to be a taxonomic relationship within both species.\n\t\n\t')
else:
    output_file.write(f'\tTarget sequence not found\n\n\tThis program did not find similarities between the target polymerase with code: {result[1]} and range {result[2]},\n\tand the polymerase with code {result[0]} both from GenBank.\n\t')
    output_file.write(f'\n\t-->The reasons for this, could be:\n\t')
    output_file.write(f'1)They have no taxonomic relationship whatsoever, or they do, but do not share specific mutations.\n\t')
    output_file.write(f'2)There is not a 100% similarity between the sequences because of the margin of error in the sequencing method\n\t')
    output_file.write(f'3)Parts of the polymerase sequence, like those of the beginning or end are missing\n\t\n\t')
output_file.write(f'DISCLOSURE: for this program to work correctly, there needs to be a 100% identity between the sequences to compare.\n\n')

output_file.close()
