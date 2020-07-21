# Complete the function/method so that it returns the url with anything after the anchor (#) removed.

# Examples
# # returns 'www.codewars.com'
# remove_url_anchor('www.codewars.com#about')

# # returns 'www.codewars.com?page=1' 
# remove_url_anchor('www.codewars.com?page=1') 

def remove_url_anchor(url):
    first = url.find('#') #The find method returns the index of the first occurence of the argument. Returns -1 if arg not found
    return url[:first] if first != -1 else url

print(remove_url_anchor("www.codewars.com#about"))
print(remove_url_anchor("www.codewars.com/katas/?page=1#about"))
print(remove_url_anchor("www.codewars.com/katas/"))