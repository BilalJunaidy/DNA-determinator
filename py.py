from sys import argv
import csv



def main():



    #The following dictionary is going to be storing the key value pairs for each of the STR counts
    STR_count = {}

    #Helps make sure that user has provided adequate number of command-line arguments
    if len(argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)
    #Following code executes if the user has provided an adequate number of command-line arguments
    else:
        with open(f"{argv[1]}", 'r') as file:
            dna_file = csv.reader(file)
            STR = next(dna_file)
            #The first element 'name' has now been removed from the list STR ~ STR is now the list of all of the STRs in the database
            STR.remove(STR[0])

            #Helps iterate through each str in the list STR
            for str in STR:

                with open(f"{argv[2]}", 'r') as file:
                    seq_file = file.read()

                    #Base case condition (i.e. the str is not in the given sequence, and hence, has an STR count of 0. This will be appended to the dictionary)
                    if seq_file.count(str) == 0:
                        STR_count[str] = 0

                    #Condition where an STR has been found and then we need to determine the longest run of consecutive repeats in the DNA sequence of the str
                    else:
                        #The following list is going to be used to store the various numbers of STR counts for each position (i.e. character) in the dna sequence
                        list = []
                        l = len(str)

                        for index, c in enumerate(seq_file):
                            if seq_file[index: (index + l)] == str:
                                list.append(count(index, l, str))

                            else:
                                continue

                        #The following code essentially sets the value of the str key to the highest number in the list
                        STR_count[str] = max(list)

        print(STR_count)


    with open(argv[1]) as file:
        dna_file_dict = csv.DictReader(file)


        for row in dna_file_dict:
            y = 0
            for str in STR:

                if (STR_count[str] == int(row[str])):
                    y += 1
                    continue
                else:
                    break

            if(y == len(STR)):
                print(row['name']

            #     if y == len(STR):
            #         print(row['name'])

            # if(y != len(STR)):
            #     print("No match")



def count(i, length, str):
    with open(f"{argv[2]}", 'r') as sfile:
                    seq_file_2 = sfile.read()
    #consec_repeats is the number to be added to the list
    consec_repeats = 1
    i +=length
    while True:
        if seq_file_2[i:(i + length)] == str:
            consec_repeats +=1
            i +=length
        else:
            break
    return consec_repeats

main()


