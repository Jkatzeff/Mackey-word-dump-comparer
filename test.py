from collections import Counter

x = "0 0140x125 03 05 07 1 10 100 11 112 12 12pt 13 132 150 1pt 2 2018 2018q2\
23 25 2pt 3 4 41421356237309515 42 5 5pt 6 7 8 9 a accomplished ad add\
addc alan allows alonzo also an analog and answer answers antikythera\
any applicative apply are argument arguments as associated at automatic\
b backus bar base baz bce be ber bjarne books bool bound box break built\
by c calculator calculus call called calls can canonical carry cdar\
cddr choice church circa class classes cmps cmps112 cobol code column\
complex computer cond consistent continue conversion correct d declared\
deducted deeper define defined defines delim dennis derivation derived\
different dijkstra directly do does don down each edsger elsewhere email\
en enter eq error evaluation examboxes example examples excep exception\
exp expression expressions f failure failwith figure fill final find\
first float fold foldl following foo for fortran found free from fun func\
function functions generate generic gers give given gosling goto grace\
greek haskell here higher hoc hopper http id if in incorrect indentation\
indicates inner instructions int inte interactions internet into is its\
james java john join jpgs key kinds known label lambda language languages\
left length let letter levels lisp list lists local map match max mccarthy\
mechanism message messy midterm missing mm multiple multiprecise name\
names negative no non none normal not notes num num1 num2 number ocaml\
of oldest one only operational option order org out output overloading\
page parameter parameterization past pe phone pl points polymorphism\
presumed procedure programming project proper provided ps question raise\
refers representation respect result return returning returns reverse\
risk ritchie same sample scheme scientific scratch several show shown\
signature signatures similar single some something sometimes spaces\
specified spring sqrt stack statement string stroustrup structure sum\
sure swer t table takes term test that the this throw thus tion to top\
total turing two tye type universal unreadable use uses using v val\
value want was what when which wiki wikipedia will with without work\
worker worth write written wrong x y you your z zipwith"

print(Counter(x.split()))