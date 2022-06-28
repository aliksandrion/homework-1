from re import findall


def domain_name(url):  # use regex for searching domain
    item = findall(r"(?<=[sp]://|w{3}.)[^w{3}].+?(?=\.\w)", url)
    return item[0]


# test
assert domain_name("http://github.com/carbonfive/raygun") == "github"
assert domain_name("http://www.zombie-bites.com") == "zombie-bites"
assert domain_name("https://www.cnet.com") == "cnet"

assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"
