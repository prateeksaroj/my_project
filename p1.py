#read a paragraph in python and print each line separately?

para="""Mahatma Gandhi came to be known as Mahatma (great soul) for the courageous, selfless,and nonviolent methodologies 
 that characterized the way he lived as well as his attempts at instilling reform for the betterment of his fellow citizens
 and the world. In this chapter we look at the wisdom that can be gleaned from an individual who was neither simple to 
 understand, nor a stranger to error or to defeat, but who continues to inspire many and interest many more. We attempt to 
 describe the path to learning proposed by this man who was also an exceedingly shrewd tactician and strategist. In particular, 
 we attempt to explain Gandhi’s creative vision of swadeshi, swaraj, satyagraha, and sarvodaya, all of which were constructs 
 that he adapted for the building of living economies and living democracies. He taught us that an individual can train 
 himself or herself to become transparentand open and also create synergy and cooperation between education, training, 
 employment, and the community, strivingalways for continuous improvement. Gandhi was a performance manager for the country 
 and a supremely practical leader for change. He believed that truth, tolerance, sacrifice, joy, and the nonviolent rejection 
 of tyranny were the very substance of a successful life. Gandhi’s ways of organizing people, of examining and producing ideas 
 for bringing people together, are important lessons for reducing the present tensions created by global trade, commerce, 
 and information technologies. Gandhi measured all decisions against truth. Truth can be translated as transparency in thought, 
 word,and action and the courage to see limitations and possibilities against the raw material of aptitude and skill available in a person."""
#print(para)
#lines = para.readlines()
'''
for line in para.split():
    print(line)
    '''

'''
txt=open("gandhi.txt")
print(type(txt))
lines=txt.readlines()
print(lines)
print(type(lines))
for line in lines:
    print(lin
    print(type(line))
'''
#print(para.splitlines())
for line in para.splitlines():
    pass
        #print(line)
data=para.splitlines()
print(data[5])


