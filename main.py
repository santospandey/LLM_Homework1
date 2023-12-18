import os

# function to check whether the string is terminal,preterminals, or non terminals
# - we need to stop the recursion if we reach to terminal words
# - terminal words have each first letter of word lowercase Eg. chief of staff
def check_terminals(str):
  word_list = str.split(' ')
  # logic to check if first letter of words is lowercase or not
  # if all not upper => it is terminal words
  return not all(word[0].isupper() for word in word_list)


def read_grammer(filepath):
    dictionary = {}
    file = open(filepath, 'r')
    for line in file:
        list = line.strip().split('\t')
        if(len(list) == 3):
            first = list[0]
            second = list[1]
            third = list[2]

            if(second != 'ROOT'):
                productions = third if check_terminals(third) else third.split(" ")
                # store result in list even for string
                productions = productions if len(productions) == 1 else [productions]
                # condition check if symbol is already in dictionary or not
                if second in dictionary:
                    dictionary[second] += productions 
                else:
                    dictionary[second] = productions
    return dictionary

# function to write the generated sentence into file.
def append_to_file(filename, content):
    file = open(filename, 'a')
    file.write(content + '\n')


if __name__ == '__main__':
    # filename for parsing grammer file
    filename = 'grammar.gr'
    filepath = os.path.join(os.getcwd(),filename)
    grammar = read_grammer(filepath)
    outputfile = 'generate_words.txt'


    
    # for i in range(10000):
    #     append_to_file(outputfile, generateSentence(grammar))