import urllib.request
import re
import sys
from collections import Counter

#USAGE: python3 parse_midterms.py WORDDUMP OUTPUT ACCURACY
#Accuracy matches what percentage match of past test questions
#IE: 0.8 would match test questions that 80% of the words are on this word dump

inp = open(sys.argv[1],"r")

wordlist = inp.readlines()
inp.close()

output = open(sys.argv[2],"w+")

accuracy = float(sys.argv[3])

output.write("Matching questions with at least " + str(accuracy) +" in common." + '\n\n')

for i in range(len(wordlist)):
	wordlist[i] = wordlist[i].strip()
BASE_DIR = "https://www2.ucsc.edu/courses/cmps112-wm/:/Old-Exams/"
TESTS = ["cmps112-2015q4-final.tt", "cmps112-2015q4-test1.tt", "cmps112-2015q4-test2.tt", 
		 "cmps112-2016q4-final.tt", "cmps112-2016q4-midterm.tt", "cmps112-2017q2-final.tt",
		 "cmps112-2017q2-midterm.tt","cmps112-2017q4-final.tt","cmps112-2017q4-midterm.tt",
		 "cmps112-2018q1-final.tt","cmps112-2018q1-midterm.tt"]
for TEST in TESTS:
	URL = BASE_DIR + TEST

	txt = urllib.request.urlopen(URL).read()
	txt = str(txt)

	free_response = txt.split("Multiple choice")[0]
	multiple_choice = txt.split("Multiple choice")[1:]

	# print(re.findall(r'[0-9]+\.',"".join(multiple_choice)))

	fr = re.compile(r"[0-9]+\.").split("".join(free_response))[3:]
	mc = re.compile(r"[0-9]+\.").split("".join(multiple_choice))[1:]
	# print(fr[1])
	index=1
	for elem in fr:
		num_matched = 0
		num_tot = 0
		temp = str(elem).strip().split()
		for tmp in temp:
			tmp = tmp.strip()
			if tmp.isalpha() or tmp.isdigit():
				if tmp in wordlist:
					num_matched+=1
				num_tot+=1
		if num_tot==0:
			index+=1
			continue	
		if(num_matched/num_tot > 0.8):
			output.write("Question " +str(index) + " on Free Response on " + TEST +": " + '\n' + " ".join(temp)+'\n\n\n')
		index+=1
	index=1
	for elem in mc:
		num_matched = 0
		num_tot = 0
		temp = str(elem).strip().split()
		for tmp in temp:
			tmp = tmp.strip()
			if tmp.isalpha() or tmp.isdigit():
				if tmp in wordlist:
					num_matched+=1
				num_tot+=1
		if num_tot==0:
			index+=1
			continue
		if(num_matched/num_tot > 0.8):
			output.write("Question " +str(index) + " on Multiple Choice on " + TEST	 +": " +'\n' + " ".join(temp)+'\n\n\n')
		index+=1
output.close()