# define punctuation

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = "He#@llo!!%#!, World ---."

no_punct = ""
for char in my_str:
    if char not in punctuations:
        no_punct = no_punct + char

# display the unpunctuated string
print(no_punct)
