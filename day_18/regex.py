import re
import string
from collections import Counter
from pprint import pprint

paragraph = "I love teaching. If you do not love teaching what else can you love. I love Python if you do not love " \
            "something which can give you all the capabilities to develop an application what else can you love. "


def most_common_words(text):
    split_it = text.split()
    Cnter = Counter(split_it).most_common()
    # Cnter.sort(reverse=True)
    return Cnter


pprint(most_common_words(paragraph))
para = """The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 
0 at origin, 4 and 8 in the positive direction. """

num_list = list(map(int, re.findall(r"[-+]?[.]?[\d]+", para)))
num_list.sort()
pprint(num_list)
dist = num_list[-1] - num_list[0]
pprint(dist)


def is_valid_variable(potential_variable):
    if re.search(r"^[a-zA-Z_]\w*$", potential_variable):
        return True
    else:
        return False


pprint(is_valid_variable("first_name"))
pprint(is_valid_variable("first-name"))

sentence = """%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as 
educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s 
mo@tivate yo@u to be a tea@cher!? """


# noinspection DuplicatedCode
def clean_text(text):
    text = text.lower()
    text = re.sub("\[.*?]", "", text)
    text = re.sub("https?://\S+|www\.\S+", "", text)
    text = re.sub("<.*?>+", "", text)
    text = re.sub("[%s]" % re.escape(string.punctuation), "", text)
    text = re.sub("\n", "", text)
    text = re.sub("\w*\d\w*", "", text)
    return text


pprint(clean_text(sentence))
pprint(most_common_words(clean_text(sentence))[:3])
