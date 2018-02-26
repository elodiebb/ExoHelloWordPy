#print ('Hello Word')

def LectureStringHelloWord():
    File = open('StringHelloWord.txt','r')
    ReadText = File.read()
    return (ReadText)

def AffichageHelloWord(Text):
    ''' 
    Affiche Hello Word
    '''
    print ('%s'%Text)
    return()
    
HelloWord = LectureStringHelloWord()
AffichageHelloWord(HelloWord)    