root_word=input("Enter a root word: ")
prefix=input("Enter a valid prefix: ")
suffix=input("Enter a valid suffix: ")

new_word=prefix.lower()+root_word.lower()+suffix.lower()

print("The new word is {}".format(new_word))