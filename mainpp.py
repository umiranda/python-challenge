
import csv
import os

filepath = os.path.join("Resources", "Unit 3 - Python_Homework_Instructions_PyPoll_Resources_election_data.csv")

with open(filepath, 'r') as input_file:
    csvreader = csv.reader(input_file,delimiter=",")

    header = next(csvreader)
    Voter_ID = []
    County = []
    Candidate = []
    Candidates = {}
    
    for row in csvreader:
        Voter_ID.append(row[0])
        Candidate.append(row[2])
        Num_vot = len(Voter_ID)
        if (row[2] in Candidates):
            Candidates[row[2]] +=1
        else:
            Candidates[row[2]] = 1

    with open("pp_output.txt", "w") as datafile:

        election_responses = (
            f"\nElection Results\n"
            f"---------------------------\n"
            f"Total Votes: {Num_vot}\n"
            f"---------------------------\n"
        )

        print(election_responses)
        datafile.write(election_responses)

        for candidate_name in Candidates:

            vote_amount = Candidates.get(candidate_name)
            voter_percentage = float(vote_amount) / float(Num_vot) * 100
            voter_output = f"{candidate_name} : {voter_percentage:.3f}% ({vote_amount})\n"
            datafile.write(voter_output)
            print(voter_output)

        winning_name = max(Candidates,key=Candidates.get)

        winning_output = (
            f"---------------------------\n"
            f"Winner: {winning_name}\n"
            f"---------------------------\n"
        )
        print(winning_output)
        datafile.write(winning_output)