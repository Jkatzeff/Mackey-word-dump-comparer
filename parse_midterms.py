import urllib.request
import re
import sys

#USAGE: python3 parse_midterms.py WORDDUMP OUTPUT ACCURACY [104a or 112]
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
BASE_DIR = ""
TESTS = []
if sys.argv[4] == "112":
	BASE_DIR = "https://www2.ucsc.edu/courses/cmps112-wm/:/Old-Exams/"
	TESTS = ["cmps112-2015q4-final.tt", "cmps112-2015q4-test1.tt", "cmps112-2015q4-test2.tt", 
		 "cmps112-2016q4-final.tt", "cmps112-2016q4-midterm.tt", "cmps112-2017q2-final.tt",
		 "cmps112-2017q2-midterm.tt","cmps112-2017q4-final.tt","cmps112-2017q4-midterm.tt",
		 "cmps112-2018q1-final.tt","cmps112-2018q1-midterm.tt"]
elif sys.argv[4] == "104a":
	BASE_DIR = "https://www2.ucsc.edu/courses/cmps104a-wm/:/Old-Exams/"
	TESTS = ["cmps104a-2015q4-final.tt",
	"cmps104a-2015q4-test1.tt",
	"cmps104a-2015q4-test2.tt",
	"cmps104a-2016q2-final.tt",
	"cmps104a-2016q2-test1.tt",
	"cmps104a-2016q2-test2.tt",
	"cmps104a-2016q4-final.tt",
	"cmps104a-2016q4-midterm.tt",
	"cmps104a-2017q2-final.tt",
	"cmps104a-2017q2-midterm.tt",
	"cmps104a-2017q4-final.tt",
	"cmps104a-2017q4-midterm.tt",
	"cmps104a-2018q2-midterm.tt"]
else:
	sys.exit("104a or 112 only")
for TEST in TESTS:
	URL = BASE_DIR + TEST

	txt = urllib.request.urlopen(URL).read()
	txt = txt.decode("ISO-8859-1")

	free_response = txt.split("Multiple choice")[0]
	multiple_choice = txt.split("Multiple choice")[1:]

	fr = re.compile(r"\n *[0-9]+\.").split("".join(free_response))[1:]
	mc = []
	for val in multiple_choice:
		mc.append(re.compile(r"\n *[0-9]+\.").split("".join(val))[1:])
	index=1
	for elem in fr:
		num_matched = 0
		num_tot = 0
		temp = str(elem).strip().split()
		for t in temp:
			tmp = t.strip().strip(".").strip('\\').strip("\'").strip("\\").strip(";").strip(".").strip(",").strip("(").strip(")").split('\\n')[0].strip(";").strip(".").strip(":").strip('\'')
			if tmp.isalpha() or tmp.isdigit():
				if tmp in wordlist:
					num_matched+=1
					num_tot+=1
				else:
					num_tot+=1
			else:
				pass
				# print(tmp)

		# print(num_matched, num_tot) if num_matched/num_tot > 0.8
		if num_tot==0:
			index+=1
			continue	
		if(num_matched/num_tot > accuracy):
			# print(num_matched, num_tot)
			output.write("Question " +str(index) + " on Free Response on " + TEST +" with accuracy " + str(num_matched/num_tot) + ": " + '\n' + (len(str(index)) + 1) * " " + elem +'\n\n\n')
		index+=1
	for part, each in enumerate(mc):
		index=1
		for elem in each:
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
			if(num_matched/num_tot > accuracy):
				output.write("Question " +str(index) + " on Multiple Choice part " + str(part + 1) + " on " + TEST + " with accuracy " + str(num_matched/num_tot) +": " +'\n' + (len(str(len(each))) + 1) * " " + elem +'\n\n\n')
			index+=1
output.close()
