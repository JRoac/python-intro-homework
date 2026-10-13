#Error message:
#$ python warmup4.py
#Traceback (most recent call last):
#  File "C:\Users\jlevi\documents\Code The Dream Intro to Python 26.1\python-intro-homework\week-2\assignment-2\warmup4.py", line 3, in <module>
#    print(name + rebounds)
#          ~~~~~^~~~~~~~~~
#TypeError: can only concatenate str (not "float") to str

#Error caused by type error, two different data types cannot concatenate
#I added a f-string to print a sentence with both data types.

name = "Olivia"
rebounds = 6.7
print(f"{name} had {rebounds} rebounds last game!")