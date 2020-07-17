#Script used to practice how to slice off a value out of a string

str='X-DSPAM-Confidence: 0.8475'
print(str)
ini=str.find(':')
print(ini)
slice=str[ini+1:]
num=float(slice)
print(num)
print(type(num))
