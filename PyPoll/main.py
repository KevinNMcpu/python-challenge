#importing os and csv for reading the CSV and navigating the file system
import os
import csv

#moving to resources folder to find the election_data file
os.chdir("Resources")

#setting up lists for holding election data
voter_id = []
vote_cast = []

#adding election data to our lists
with open("election_data.csv") as csv_file:
    #election_data.csv is assigned work, election_data2.csv is my smaller testing data
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            #skipping the headers
               line_count = line_count + 1
        else:
            voter_id.append(row[0])
            vote_cast.append(row[2])
            line_count = line_count + 1

#creating lists for counting votes
candidates = []
candidates_votes_received = []

#loops through election data lists
for x in range((len(voter_id))):
    #if the candidate list is empty, adds the first candidate to the list
    if (len(candidates) == 0):
        candidates.append(vote_cast[x])
        candidates_votes_received.append(1)
    #if the candidate list has candidates already, loop through the list to see if the candidate being voted for is already on the list
    else:
        found = 0
        count = 0
        count_target = len(candidates)-1
        while found==0:
            #if the candidate is on the list, add one vote to their total
            if (candidates[(count)] == vote_cast[x]):
                candidates_votes_received[count] = candidates_votes_received[count] + 1
                found=1
            #if we reach the end of the list and the candidate wasn't found, add them to the list
            elif (count == count_target):
                candidates.append(vote_cast[x])
                candidates_votes_received.append(1)
                found=1
            else:
                count = count+1

total_votes = 0
candidates_to_count = len(candidates_votes_received)

y = 0

#quickly loop through to find the total votes
while y < candidates_to_count:
    total_votes = total_votes + candidates_votes_received[y]
    y = y + 1

#prepare to write to .txt, from this point on I am printing to terminal and printing to .txt at the same time
os.chdir("..")
os.chdir("Analysis")
file1 = open("output.txt", "w")

print("Election Results")
file1.write("Election Results")
file1.write("\n")
print("-------------------------")
file1.write("-------------------------")
file1.write("\n")
print(f"Total Votes: {total_votes}")
file1.write(f"Total Votes: {total_votes}")
file1.write("\n")
print("-------------------------")
file1.write("-------------------------")
file1.write("\n")

candidate_list_empty = 0

winning_candidate = None
current_candidate = None
current_candidate_votes = 0

winner_found = 0
z = 0

#loop through the list of candidates to find who has the most, this will sort the list automatically so whatever candidate gets the most votes is first, etc
while z < len(candidates):
    #when looping through the list, if the one currently being checked has the most votes, save it so we can print them in order
    if (candidates_votes_received[z] > current_candidate_votes):
        current_candidate = candidates[z]
        current_candidate_votes = candidates_votes_received[z]
    #if we've reached the end of the list, print them, then remove them from the list
    if (z == (len(candidates)-1)):
        print(f"{current_candidate}: {round(((current_candidate_votes / total_votes)*100),3)}% ({current_candidate_votes})")
        file1.write(f"{current_candidate}: {round(((current_candidate_votes / total_votes)*100),3)}% ({current_candidate_votes})")
        file1.write("\n")
        candidates.remove(current_candidate)
        candidates_votes_received.remove(current_candidate_votes)
        if (winner_found == 0):
        #save the name of the winning candidate for printing at the end of the results
            winning_candidate = current_candidate
            winner_found = 1
        current_candidate = None
        current_candidate_votes = 0
        z = -1
    #if the lists are empty, then we are done!
    if (len(candidates) == 0):
        candidate_list_empty = 1
    z = z + 1

print("-------------------------")
file1.write("-------------------------")
file1.write("\n")
print(f"Winner: {winning_candidate}")
file1.write(f"Winner: {winning_candidate}")
file1.write("\n")
file1.close()