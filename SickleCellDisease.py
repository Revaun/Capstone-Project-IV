dna_ = input("Enter the DNA sequence to translate: ")   #
def translate():                                                    #translation define for loop
  translate()
for i in range(0,len(dna_),3):      # for loop if statement - DNA seq input matches Amino Acid table. 
    dna = dna_[i:i+3]
    if dna == "ATA" or dna == "ATC" or dna == "ATT":
      print ("I")
    elif dna == "CTA" or dna == "CTC" or dna == "CTG" or dna == "CTT" or dna == "TAA" or dna =="TTG":
      print ("L")
    elif dna == "GTA" or dna == "GTC" or dna == "GTG" or dna == "GTT":
      print ("V")
    elif dna == "TTC" or dna == "TTT":
      print ("F")
    elif dna == "ATG":
      print ("M")
    else:
      print ("X")

def translate(sq, table):               #translation define for loop
    result=''
    for i in range(0,len(sq),3):
        codon = sq[i:i+3].upper()
        if codon in table:
            result += table[codon]
        else:
            result += 'X'
    return result
                                                                        #DNA ref 
SLC = 'ACATTTGCTTCTGACACAACTGTGTTCACTAGCAACCTCAAACAGACACCATGGTGCATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAGGCTGCTGGTGGTCTACCCTTGGACCCAGAGGTTCTTTGAGTCCTTTGGGGATCTGTCCACTCCTGATGCTGTTATGGGCAACCCTAAGGTGAAGGCTCATGGCAAGAAAGTGCTCGGTGCCTTTAGTGATGGCCTGGC'
table = {"ATA":"I", "ATC":"I", "ATT":"I", "CTA":"I",                    #translation table
         "CTC":"L", "CTG":"L", "CTT":"L", "TAA":"L", "TTG":"L",
         "GTA":"V", "GTC":"V", "GTG":"V", "GTT":"V",
         "TTC":"F", "TTT":"F",
         "ATG":"M"}

print(translate(SLC,table))                             # print translation


dna_list = [] # store codes

f = open("DNA.txt", "r")
for code in f:
    code = [code[i:i+3] for i in range(0, len(code), 3)]
    dna_list.append(code)# append the dna codes to the dna list



store_every_dna = []# store every items that is stored in dna_list and then loop over the dna list
for code in dna_list: 
   
    for dna in code:
        store_every_dna.append(dna)# update each dna item to stored each dna list
        
f.close()

print(store_every_dna)





def translate(dna_input):

    amino_acid = ''#This will be equal to the dna inputed from the user
    check_dna = ''
    
    for code in store_every_dna:# loop over the stored dna to get the dna names
        
        if code in dna_input:
            check_dna = code

    
    if check_dna == 'ATT' or check_dna == 'ATC' or check_dna == 'ATA':    # check if the input value is equal to these 5 dna codons
        amino_acid = 'Isoleucine'
        # assign amino acid
    elif check_dna == 'CTT' or check_dna == 'CTC' or check_dna == 'CTA' or check_dna == 'CTG' or check_dna == 'TTA' or check_dna == 'TTG':
        amino_acid = 'Leucine'
    elif check_dna == 'GTT' or check_dna == 'GTC' or check_dna == 'GTA' or check_dna == 'GTG':
        amino_acid = 'Valine'
    elif check_dna == 'TTT' or check_dna == 'TTC':
        amino_acid = 'Phenylalanine '
    elif check_dna == 'ATG':
        amino_acid == 'Methionine'
    else:
        amino_acid = 'X'
        

    print('Amino Acid : ' + amino_acid) # print result




def mutate(file_name):        
    in_file = open("DNA.txt", "r")  #read DNA.txt file
    for in_line in in_file:
        in_line = in_line.rstrip('\n')# split each letter 
        in_line = list(in_line)
        
        
        write_to_normal_file = open('normalDNA.txt', 'w')# write to the normalDna file and loop over each letter
        for lower_case in in_line:       

            if lower_case == lower_case.lower():     # if the current letter is lower case change it to upper case
               
                index_of_lower = in_line.index(lower_case)
                in_line[index_of_lower] = lower_case.upper()    # update the list index to the upper case version
                
                                                        # write to the file the updated A value
        write_to_normal_file.write(str(in_line))
                                                    
        write_to_normal_file.close()

 
    in_file = open("DNA.txt", "r")#read DNA.txt file
    for line in in_file:
        line = line.rstrip('\n')# split each letter 
        line = list(line)


        write_to_muatated_file = open('mutatedDNA.txt', 'w')        # write to mutatedDNA
        for lower_case in line:                                      # loop over each letter
               
            if lower_case == lower_case.lower():      # if the letter is lower case change to upper case
                
                index_of_lower = line.index(lower_case) # update the list index to T
                line[index_of_lower] = 'T'

         
        write_to_muatated_file.write(str(line)) # write to the file the updated A value and wrie to mutated file

        write_to_muatated_file.close
    in_file.close()

  




def txtTranslate():
    user_dna_input = input('Enter DNA Code: ') #User input
    translate(user_dna_input)
    mutate('DNA.txt')


txtTranslate()      #call all functions

