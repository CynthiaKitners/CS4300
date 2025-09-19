# Create a file named task6_read_msoure.txt and add the information.  Then count
# the number of words in the file
import pytest

file = open("/home/student/CS4300/homework1/task6_read_me.txt")

content = file.read()
# print(content)

with open ("/home/student/CS4300/homework1/task6_read_me.txt", "w",encoding='utf-8') as file:
    file.write("Lorem ipsum dolor sit amet , consectetur adipiscing elit . Duis vitae feugiat"
    "tortor , quis tempus lacus . Maecenas sollicitudin rhoncus ultricies ."
    "Mauris neque metus , blandit sed sagittis aliquam , fringilla eget massa ."
    "Donec at luctus leo . Curabitur suscipit nulla aliquam sapien maximus ,"
    "sit amet fermentum sem malesuada . Nulla suscipit , felis non consequat"
    "eleifend , sem quam pharetra turpis , vel efficitur tellus est placerat"
    "est . Nam metus orci , facilisis et ante sed , ultricies pulvinar lorem ."
    "Phasellus eu ipsum sit amet ex auctor volutpat . Suspendisse ac turpis et"
    "felis tristique facilisis vitae in diam . Donec maximus ex in lorem"
    "auctor vulputate . Nulla finibus sodales ante , convallis gravida metus"
    "iaculis id ."
    )
print()
count_words = 0

# Opening our text file in read only mode
with open(r'/home/student/CS4300/homework1/task6_read_me.txt','r') as file:
    data = file.read()
    lines = data.split()

    # Iterating over every word in lines
    for word in lines:
        # checking if the word is numeric or not
        if not word.isnumeric():          
            count_words += 1

print("The number of words in this file is: ",count_words)

def word_count():
    print(file.read())

#==============================================================================

def test_word_count():
    assert count_words  == 117
   
