"""""
Title: Assignment 2.1-3 Word Importance
Author: Simone Lewis
Date 10-31-2022

Assignment discussion follows the script. 

This script contains the solutions for problems 1-3 from assignment 2. 

"""""


import operator
from numpy import dot
from numpy.linalg import norm
import pandas as pd # import pandas module 

df = pd.read_csv('horoscopes.csv')
texts = df['horoscope-clean'].values

def stopwords():
    """ Stopword list for American English
    """
    return ["","a","about","above","after","again","against","ain","all","am","an","and","any","are","aren","aren't","as","at","be","because","been","before","being","below","between","both","but","by","can","couldn","couldn't","d","did","didn","didn't","do","does","doesn","doesn't","doing","don","don't","down","during","each","few","for","from","further","had","hadn","hadn't","has","hasn","hasn't","have","haven","haven't","having","he","her","here","hers","herself","him","himself","his","how","i","if","in","into","is","isn","isn't","it","it's","its","itself","just","ll","m","ma","me","mightn","mightn't","more","most","mustn","mustn't","my","myself","needn","needn't","no","nor","not","now","o","of","off","on","once","only","or","other","our","ours","ourselves","out","over","own","re","s","same","shan","shan't","she","she's","should","should've","shouldn","shouldn't","so","some","such","t","than","that","that'll","the","their","theirs","them","themselves","then","there","these","they","this","those","through","to","too","under","until","up","ve","very","was","wasn","wasn't","we","were","weren","weren't","what","when","where","which","while","who","whom","why","will","with","won","won't","wouldn","wouldn't","y","you","you'd","you'll","you're","you've","your","yours","yourself","yourselves","could","he'd","he'll","he's","here's","how's","i'd","i'll","i'm","i've","let's","ought","she'd","she'll","that's","there's","they'd","they'll","they're","they've","we'd","we'll","we're","we've","what's","when's","where's","who's","why's","would","able","abst","accordance","according","accordingly","across","act","actually","added","adj","affected","affecting","affects","afterwards","ah","almost","alone","along","already","also","although","always","among","amongst","announce","another","anybody","anyhow","anymore","anyone","anything","anyway","anyways","anywhere","apparently","approximately","arent","arise","around","aside","ask","asking","auth","available","away","awfully","b","back","became","become","becomes","becoming","beforehand","begin","beginning","beginnings","begins","behind","believe","beside","besides","beyond","biol","brief","briefly","c","ca","came","cannot","can't","cause","causes","certain","certainly","co","com","come","comes","contain","containing","contains","couldnt","date","different","done","downwards","due","e","ed","edu","effect","eg","eight","eighty","either","else","elsewhere","end","ending","enough","especially","et","etc","even","ever","every","everybody","everyone","everything","everywhere","ex","except","f","far","ff","fifth","first","five","fix","followed","following","follows","former","formerly","forth","found","four","furthermore","g","gave","get","gets","getting","give","given","gives","giving","go","goes","gone","got","gotten","h","happens","hardly","hed","hence","hereafter","hereby","herein","heres","hereupon","hes","hi","hid","hither","home","howbeit","however","hundred","id","ie","im","immediate","immediately","importance","important","inc","indeed","index","information","instead","invention","inward","itd","it'll","j","k","keep","keeps","kept","kg","km","know","known","knows","l","largely","last","lately","later","latter","latterly","least","less","lest","let","lets","like","liked","likely","line","little","'ll","look","looking","looks","ltd","made","mainly","make","makes","many","may","maybe","mean","means","meantime","meanwhile","merely","mg","might","million","miss","ml","moreover","mostly","mr","mrs","much","mug","must","n","na","name","namely","nay","nd","near","nearly","necessarily","necessary","need","needs","neither","never","nevertheless","new","next","nine","ninety","nobody","non","none","nonetheless","noone","normally","nos","noted","nothing","nowhere","obtain","obtained","obviously","often","oh","ok","okay","old","omitted","one","ones","onto","ord","others","otherwise","outside","overall","owing","p","page","pages","part","particular","particularly","past","per","perhaps","placed","please","plus","poorly","possible","possibly","potentially","pp","predominantly","present","previously","primarily","probably","promptly","proud","provides","put","q","que","quickly","quite","qv","r","ran","rather","rd","readily","really","recent","recently","ref","refs","regarding","regardless","regards","related","relatively","research","respectively","resulted","resulting","results","right","run","said","saw","say","saying","says","sec","section","see","seeing","seem","seemed","seeming","seems","seen","self","selves","sent","seven","several","shall","shed","shes","show","showed","shown","showns","shows","significant","significantly","similar","similarly","since","six","slightly","somebody","somehow","someone","somethan","something","sometime","sometimes","somewhat","somewhere","soon","sorry","specifically","specified","specify","specifying","still","stop","strongly","sub","substantially","successfully","sufficiently","suggest","sup","sure","take","taken","taking","tell","tends","th","thank","thanks","thanx","thats","that've","thence","thereafter","thereby","thered","therefore","therein","there'll","thereof","therere","theres","thereto","thereupon","there've","theyd","theyre","think","thou","though","thoughh","thousand","throug","throughout","thru","thus","til","tip","together","took","toward","towards","tried","tries","truly","try","trying","ts","twice","two","u","un","unfortunately","unless","unlike","unlikely","unto","upon","ups","us","use","used","useful","usefully","usefulness","uses","using","usually","v","value","various","'ve","via","viz","vol","vols","vs","w","want","wants","wasnt","way","wed","welcome","went","werent","whatever","what'll","whats","whence","whenever","whereafter","whereas","whereby","wherein","wheres","whereupon","wherever","whether","whim","whither","whod","whoever","whole","who'll","whomever","whos","whose","widely","willing","wish","within","without","wont","words","world","wouldnt","www","x","yes","yet","youd","youre","z","zero","a's","ain't","allow","allows","apart","appear","appreciate","appropriate","associated","best","better","c'mon","c's","cant","changes","clearly","concerning","consequently","consider","considering","corresponding","course","currently","definitely","described","despite","entirely","exactly","example","going","greetings","hello","help","hopefully","ignored","inasmuch","indicate","indicated","indicates","inner","insofar","it'd","keep","keeps","novel","presumably","reasonably","second","secondly","sensible","serious","seriously","sure","t's","third","thorough","thoroughly","three","well","wonder"]

def tokenizer(text, lower=True, stopword=True):
    """ String tokenization with optional and casefolding and stopword filetering
    
    
    """
    if stopword:
        stopwordlist = stopwords()
        tokens = [token for token in text.lower().split(' ') if token not in stopwordlist]

    elif lower:
        tokens = text.lower().split()
    
    else:
        tokens = text.split()
    
    return tokens

def word_count(text, sort = True, stopword=True):
    """ count words
    """
    counter = {}
    for word in tokenizer(text, stopword=stopword):
        counter.setdefault(word, 0)
        counter[word] = counter[word] + 1
    
    if sort:
        counter = dict(sorted(counter.items(), key=operator.itemgetter(1), reverse=True))

    return counter

def list_to_dtm(corpus, stopword=True):
    wc = word_count(' '.join(corpus), stopword=stopword)
    lexicon = list(wc.keys())
    
    dtm = []
    for content in corpus:
        document = [0 for _ in lexicon]
        wc = word_count(content, stopword=stopword)
        for (i, word) in enumerate(lexicon):
            if word in wc:
                document[i] = wc[word]
        
        dtm.append(document)
    
    return dtm, lexicon


def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

def difference(lst1, lst2):
    return list(set(lst1).difference(set(lst2)))

def cosine_similarity(a, b):
    return dot(a, b) / (norm(a) * norm(b))


def main():
    print('[INFO] text data set:\n')
    data = texts
    for text in data:
        print(text)

    print('[INFO] all tokens:\n')
    for token in ' '.join(data).split():
        print(token)    
    
    wc = word_count(' '.join(data))
    print('[INFO] word counts with stopword filtering:')
    print(wc)
    
    print('[INFO] building vector space model:')
    (dtm,  lexicon) = list_to_dtm(data, stopword=True)
    print(lexicon)
    print(dtm)


    print('[INFO] document 1:')
    print(data[0])
    print(lexicon)
    print(dtm[0])
    for (i, val) in enumerate(dtm[0]):
        if val > 0:
            print(lexicon[i])
    
    # measure document overlap
    v1 = dtm[0]
    v2 = dtm[1]
    print(cosine_similarity(v1, v2))
    
    
if __name__=="__main__":
    main()

"""""

For question 2, the code is changed in line 10 for the different signs. 
For question 1, the indexing portion of the code is removed, and all the stopword 
values are changed to false in order to compare. 

Most of the frequent words with stopword filtering occur at 
the beginning of the horoscope, with the highest value being 1 in both documents. 
This produced a value of 0.0, meaning that the documents are not similar at all. 

Without stopword filtering, most of the frequent words also occur at the start 
of the horoscopes, however the value doesn’t go over 3. Without stopwords, it produced 
a value of 0.4393747751637468, meaning it is slightly similar, but not identical. 

All the horoscopes are different for each of the signs. Pisces is concerned with their
job, and possibly changing directions in life, they may be scared of failure. 
Virgo is more concerned with those close to them, and possibly annoying someone, 
while Scorpio is concerned with money, and the wealthy side of life, which is somewhat similar 
to Pisces being worried about their career. 

"""""
