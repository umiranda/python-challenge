

#import dependencies
import csv
import os

#retrieving data from file
filepath = os.path.join("Resources", "Unit 3 - Python_Homework_Instructions_PyPoll_Resources_election_data.csv")

#reading file
with open(filepath, 'r') as input_file:
    csvreader = csv.reader(input_file,delimiter=",")

#declaring variables
    header = next(csvreader)
    Voter_ID = []
    County = []
    Candidate = []
    Candidates = {}
    #looping through to extract results
    for row in csvreader:
        Voter_ID.append(row[0])
        Candidate.append(row[2])
        Num_vot = len(Voter_ID)
        #condition to check if the row matches the Candidates
        if (row[2] in Candidates):
            Candidates[row[2]] +=1
        else:
            Candidates[row[2]] = 1
    #write and create an output txt
    with open("pp_output.txt", "w") as datafile:

        election_responses = (
            f"\nElection Results\n"
            f"---------------------------\n"
            f"Total Votes: {Num_vot}\n"
            f"---------------------------\n"
        )

        print(election_responses)
        datafile.write(election_responses)
        #looping to find out and write information for each candidate
        for candidate_name in Candidates:

            vote_amount = Candidates.get(candidate_name)
            voter_percentage = float(vote_amount) / float(Num_vot) * 100
            voter_output = f"{candidate_name} : {voter_percentage:.3f}% ({vote_amount})\n"
            datafile.write(voter_output)
            print(voter_output)
        #getting and writting the election winner
        winning_name = max(Candidates,key=Candidates.get)

        winning_output = (
            f"---------------------------\n"
            f"Winner: {winning_name}\n"
            f"---------------------------\n"
        )
        print(winning_output)
        datafile.write(winning_output)