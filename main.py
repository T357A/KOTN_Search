"""
A multi-webpage search for KOTN auction items that I commonly look for that opens a browser page/ tab
with each search and yields upto 400 results per page.
The list.txt file is able to be added and subtracted from as search requirements become needed.
"""

import webbrowser

# You will neeed to adjust the path to the file that the list.txt is in
search_list = open("/Users/a357a/Python Stuff/KOTN_Search/list.txt", "r")
terms = search_list.read().split("\n")
# Test to check list
# print(terms)  # Works up to this point- all WORDS print- no need to index through- only letters would print then

for word in terms:
    url = "https://kotnauction.com/auctions/all?find="
    size = "&per_page=200"
    page = "{}{}{}".format(url, word, size)
    webbrowser.open(page)
