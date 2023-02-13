with open("books/frankenstein.txt", "r") as f:
    file_contents = f.read()
    # print(file_contents)

# Counts words
def countwords(storytext):
    words = storytext.split()
    storycount = len(words)
    # print('this is the count', storycount)
    return storycount

# Counts letters
# Add a new function to your script that takes the text from the book as a string, 
# and returns the number of times each character appears in the string. 

def letterCounter(storytext):
    # returns dictionary of each character and number of times it appears
    # convert all to lowercase
    lowercase_text = storytext.lower()

    story_dictionary = {}
    for element in lowercase_text:
        if element in story_dictionary:
            story_dictionary[element] = story_dictionary[element] + 1
        else:
            story_dictionary[element] = 1
    return story_dictionary

# Print a Report
def print_report(totalStoryCount, letterCountdata):
    count = totalStoryCount(file_contents)
    data = letterCountdata(file_contents)
    print('THE COUNT', count)
    print(f'{count} words found in the document')

    for element in data:
        print('element', element)
        print(f'The {element} character was found {data[element]} times')

print_report(countwords, letterCounter)