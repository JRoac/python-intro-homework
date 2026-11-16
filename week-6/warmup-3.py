#Example of NameError
#def wnba_score(a,b):
#    final_score = a + b

#wnba_score()

#print(final_score)
#Traceback (most recent call last):
#  File "c:\Users\jlevi\documents\Code The Dream Intro to Python 26.1\python-intro-homework\week-6\warmup-3.py", line 6, in <module>
#    print(final_score)
#          ^^^^^^^^^^^
#NameError: name 'final_score' is not defined. Did you mean: 'wnba_score'?

def wnba_score(a,b):
    final_score = a + b
    return(final_score)

score = wnba_score(70,50)

print(score)
