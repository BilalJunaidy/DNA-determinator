from sys import argv
import csv


def main():

        #Helps make sure that user has provided adequate number of command-line arguments
    if len(argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)

    #Opens up and define all of the different files that are going to be used throughout this program
    #1 - Dna file as a csv.reader
    with open(f"{argv[1]}", 'r') as file:
            dna_file = csv.reader(file)
            STR = next(dna_file)
            #The first element 'name' has now been removed from the list STR ~ STR is now the list of all of the STRs in the database
            STR.remove(STR[0])

    #2 - Sequence file using file.read
    with open(f"{argv[2]}", 'r') as file:
            seq_file = file.read()



    #Following code executes if the user has provided an adequate number of command-line arguments

    #The following dictionary is going to be storing the key value pairs for each of the STR counts
    STR_count = {}

    #Helps iterate through each str in the list STR
    for str in STR:
        STR_count[str] = counter(seq_file, str)

    #TO REVIVE
    #     #Base case condition (i.e. the str is not in the given sequence, and hence, has an STR count of 0. This will be appended to the dictionary)
    #     if seq_file.count(str) == 0:
    #         STR_count[str] = 0

    #     #Condition where an STR has been found and then we need to determine the longest run of consecutive repeats in the DNA sequence of the str
    #     else:
    #         #The following list is going to be used to store the various numbers of STR counts for each position (i.e. character) in the dna sequence
    #         list = []
    #         l = len(str)

    #         for index, c in enumerate(seq_file):
    #             if seq_file[index: (index + l)] == str:
    #                 list.append(counter(index, l, str, seq_file))

    #             else:
    #                 break

    #         #The following code essentially sets the value of the str key to the highest number in the list
    #         STR_count[str] = max(list)
    # print(STR_count)

        #TO REVIVE

    # 3 - Dna file as csv.DictReader
    with open(argv[1]) as file:
        dna_file_dict = csv.DictReader(file)

        #Last step of the program whereby the name of the individual is printed (if there is a match), or No match is printed if there is no match
        for row in dna_file_dict:
            y = 0
            for str in STR:
                if (STR_count[str] != int(row[str])):
                    break
                else:
                    y+=1

            if y == len(STR):
                print(row['name'])
                break

        if y != len(STR):
            print("No match")






            #y = 0
            # for str in STR:
            #     if (STR_count[str] == int(row[str])):
            #         y += 1
            #         continue
            #     else:
            #         break

            # if(y == len(STR)):
            #     print(row['name']


#TO REVIVE
# def counter(i, length, str, seq_file):
#     # with open(f"{argv[2]}", 'r') as sfile:
#     #                 seq_file_2 = sfile.read()
#     #consec_repeats is the number to be added to the list
#     consec_repeats = 1
#     i +=length
#     while True:
#         if seq_file[i:(i + length)] == str:
#             consec_repeats +=1
#             i +=length
#         else:
#             break
#     return consec_repeats


def counter(seq_file, str):
    min_count = 0
    l = len(str)
    for i in range(len(seq_file)):
        count = 0
        while True:
            start = i + (count * l)
            end = start + l
            # print('this is start', start)
            # print('this is end', end)
            if seq_file[start:end] == str:
                count +=1
            else:
                break
        min_count = max(min_count, count)
    # print(count)

    return min_count


main()


