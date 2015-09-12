SHAKESPEARE_TOPARSE = 'shakespeare_dictionary.txt'

def parseText(toParse):
	# Discard csv header
	toParse.readline()

	nouns = []
	verbs = []
	adjs = []
	
	for line in toParse:
		line = line.strip()
		
		if not line:
		  continue
			
		nonum = ''.join([i for i in line if not i.isdigit()])
                if "(n.)" in nonum:
                    #nouns.append(nonum.split(" (n.) "))
                    noun = nonum.split("(n.)")
                    oldword = noun[0].strip()
                    if " " in oldword or oldword == "":
                        continue
                    newword = noun[1].strip()
                    newwordlist = newword.split(",")
                    word = newwordlist[0] #just take first word because too long
                    word = word.strip()
                    if " " in word or word == "":
                        continue
                    else:
                        replaceString = "currentVal.nodeValue = currentVal.nodeValue.replace(/"+word+"/gi, \""+oldword+"\");"
                        print replaceString
                elif "(v.)" in nonum:
                    #verbs.append(nonum.split(" (v.) "))
                    verb = nonum.split("(v.)")
                    oldword = verb[0].strip()
                    if " " in oldword or oldword == "":
                        continue
                    newword = verb[1].strip()
                    newwordlist = newword.split(",")
                    word = newwordlist[0] #just take first word because too long
                    word = word.strip()
                    if " " in word or word == "":
                        continue
                    else:
                        replaceString = "currentVal.nodeValue = currentVal.nodeValue.replace(/"+word+"/gi, \""+oldword+"\");"
                        print replaceString
                elif "(adj.)" in nonum:
                    #adjs.append(nonum.split(" (adj.) "))
                    adj = nonum.split("(adj.)")
                    oldword = adj[0].strip()
                    if " " in oldword or oldword == "":
                        continue
                    newword = adj[1].strip()
                    newwordlist = newword.split(",")
                    word = newwordlist[0] #just take first word because too long
                    word = word.strip()
                    if " " in word or word == "":
                        continue
                    else:
                        replaceString = "currentVal.nodeValue = currentVal.nodeValue.replace(/"+word+"/gi, \""+oldword+"\");"
                        print replaceString
                    
                
                #print replaceString


	return nouns, verbs, adjs

if __name__ == '__main__':
	with open(SHAKESPEARE_TOPARSE) as toParse:
		nouns, verbs, adjs = parseText(toParse)
		
	#for noun in nouns:
	    #print(noun)
	#for verb in verbs:
	    #print(verb)
	#for adj in adjs:
	    #print(adj)
