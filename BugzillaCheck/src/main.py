import requests, bugzilla

# pip install bugzilla

un = "ege.acican@ug.bilkent.edu.tr"
pw = "wVM5V6F_vEtxA65"

url = "https://bugzilla.mozilla.org/rest/login?login=gokcessefa@gmail.com&password=Gok123456ce.Gss"
url2 = "https://bugzilla.mozilla.org/rest/bug"
apikey = "tYf554cf8XujDMyt3bmzypjSjUNCavDD5quBKQsh"
bugid = "1600646"
page = requests.get(url2,params={'id': bugid, 'api_key': apikey})
# page = requests.get(url=url, params={'id':'123456','api_key':'tYf554cf8XujDMyt3bmzypjSjUNCavDD5quBKQsh'})

def retrieveReport():
    url2 = "https://bugzilla.mozilla.org/rest/bug"
    apikey = "tYf554cf8XujDMyt3bmzypjSjUNCavDD5quBKQsh"
    bugid = "1600646"
    page = requests.get(url2,params={'id': bugid, 'api_key': apikey})
    print("\nBugstring:",page.text)

def retrieveInfo():
    url2 = "https://bugzilla.mozilla.org/rest/bug"
    apikey = "tYf554cf8XujDMyt3bmzypjSjUNCavDD5quBKQsh"
    bugid = "1600646"
    page = requests.get(url2,params={'id': bugid, 'api_key': apikey})

    print("retrieve html repsonse:\n")
    print(page,"\n")

    print("retrieve full message:\n")
    print(page.text,"\n")

    print("retrieve messages as bytes:\n")
    for i in page:
        print(i)
    print()

    print("url:\n")
    print(page.url,"\n")

    print("bugs:\n")
    print(page.json()['bugs'],"\n")

# retrieveReport()
# retrieveInfo()

def printReportsHTML():
    url2 = "https://bugzilla.mozilla.org/buglist.cgi?quicksearch=bug&list_id=15239429"
    apikey = "tYf554cf8XujDMyt3bmzypjSjUNCavDD5quBKQsh"
    bugid = "1600646"
    type = "defect"
    updated = "2020-03-09"
    status = "UNCO"
    page = requests.get(url2,params={'type': type, 'status': status, 'updated': updated, 'api_key': apikey})
    print("\nBugstring:",page.text)

def printReportsDate():
    apikey = "tYf554cf8XujDMyt3bmzypjSjUNCavDD5quBKQsh"
    url = "https://bugzilla.mozilla.org/rest/bug/35?include_fields=updated,summary,status,resolution"
    r = requests.get(url, params={'api_key':apikey})

    print(r.text)


def search(keyword):
    url = "https://bugzilla.mozilla.org/rest/"
    b = bugzilla.Bugzilla(url=url,api_key=apikey)

    print()
    # keyword: "eclipse"
    # get list of "bug arrays" from serach
    # check creation_time attribute of bugs in the list
        # if year of creation_time > 210
            # print the bug array
    for i in b.quick_search(keyword)['bugs']:
        creationTime = i['creation_time']
        year = int(creationTime[0:4])
        if year>2010:
            print(i)

search("eclipse")