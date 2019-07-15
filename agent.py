from gensim.models import KeyedVectors
from gensim.models import Word2Vec
import train
import preprocess

try:
    Word2Vec.load('word2vec.model')
except:
    print("Model file unavailable, training agent")
    exec(open("train.py").read());

questions = {
}

questions[1]=preprocess.string_to_analogy("land:excavate::shoal:_,sound salvage dredge survey sidle,dredge")
#questions[2]=preprocess.string_to_analogy("sword:brandish::_:_,")
questions[3]=preprocess.string_to_analogy("volcano:quiescent::talent:_,imperious hyperbolical oblique latent pliant,latent")
questions[4]=preprocess.string_to_analogy("style:flamboyant::behavior:_,brazen lofty volatile insolent sassy,brazen")
questions[5]=preprocess.string_to_analogy("direct:confront::oblique:_,unsettle incite sidle stymie flourish,sidle")
questions[6]=preprocess.string_to_analogy("beforehand:trepidation::afterwards:_,bravado decadence hyperbole foolhardy rue,rue")
questions[7]=preprocess.string_to_analogy("person:odious::action:_,unsettling imperious heinous lofty haughty,heinous")
questions[8]=preprocess.string_to_analogy("naughtiness:permit::misbehavior:_,dredge confront pique countenance stymie,countenance")
questions[9]=preprocess.string_to_analogy("speech:hyperbole::behavior:_,trepidation quiescence bravado pique parsimony,bravado")
questions[10]=preprocess.string_to_analogy("emotional:resistance::physical:_,cadaver survey conflagration decadence friction,friction")
questions[11]=preprocess.string_to_analogy("interest:rouse::curiosity:_,assuage nettle dredge rue pique,pique")
questions[12]=preprocess.string_to_analogy("mien:haughty::countenance:_, flamboyant imperious befuddled canny brazen,imperious")
questions[13]=preprocess.string_to_analogy("threateningly:brandish::flamboyantly:_,confront flaunt fan incite garner,flaunt")
#questions[14]=preprocess.string_to_analogy
questions[15]=preprocess.string_to_analogy("latent:possibility::hidden:_,cache ire hovel visage urchin,cache")
#questions[16]=preprocess.string_to_analogy
questions[17]=preprocess.string_to_analogy("travel:blocked::attempt:_,rued incited salvage stymied unsettled,stymied")
questions[18]=preprocess.string_to_analogy("salesman:canny::businesswoman:_,entrepreneurial prolific shrewd haughty frugal,shrewd")
questions[19]=preprocess.string_to_analogy("brave:reckless::frugal:_,prolific audacious foolhardy poor parsimonious,parsimonious")
questions[20]=preprocess.string_to_analogy("personality:pliant::behavior:_,lofty insolent cooperative volatile popular,cooperative")


#questions[4]=preprocess.string_to_analogy("after:regrets::before:_,thresholds prologues misgivings memories pitfalls,misgivings")

print("-----------------------------\n")

correct = []
incorrect = []

for question_number in questions:
    data = questions[question_number] 
    print(f"{question_number}. {data[0]}:{data[1]}::{data[2]}:_____?")
    for answer in data[3]:
        print(f"\t{answer}")

    ref = model.most_similar_cosmul(positive=[data[1],data[2]], negative=[data[0]], topn=5)
    print(f"Predictions are {ref}")

    for word in data[3]:
        if word not in model.vocab:
            data[3].remove(word)

    submission = model.most_similar_to_given(ref[0][0], data[3])
    print()
    print(f"Answer: {submission}")
    print(f"{data[0]}:{data[1]}::{data[2]}:{submission}")
    if submission ==  data[4]:
        print("Answer is correct.")
        correct.append(question_number)
    else:
        print(f"Answer is incorrect, intended answer was {data[4]}.")
        incorrect.append(question_number)

    print("\n\n\n")

print(f"Model scored {len(correct)} out of {len(correct)+len(incorrect)}!")    

