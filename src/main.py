import requests, bugzilla, datetime

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


def searchBugs(keyword, time1, time2):
    url = "https://bugzilla.mozilla.org/rest/"
    b = bugzilla.Bugzilla(url=url,api_key=apikey)

    # keyword: "eclipse"
    # get list of "bug arrays" from serach
    # check creation_time attribute of bugs in the list
        # if year of creation_time > 210
            # print the bug array

    bugarray = []
    for i in b.quick_search(keyword)['bugs']:
        creationTime = i['creation_time']

        year = int(creationTime[0:4])
        month = int(creationTime[5:7])
        day = int(creationTime[8:10])

        date = datetime.datetime(year,month,day)
        if (date-time1).total_seconds()>0 and (time2-date).total_seconds()>0:
            bugarray.append(i)
    return bugarray

def printBugs(keyword,time1,time2):
    # searchBugs gets a keyword to search in query of bugzilla, a start time t1 and a finish time t2,
    # returns a list of bugs with attributes(labels)

    for i in searchBugs(keyword, t1,t2):
        print(i)

# show bugs between two dates t1, t2

year1=2010
month1=10
day1=10

t1 = datetime.datetime(year1,month1,day1)

year2=2019
month2=12
day2=12

t2 = datetime.datetime(year2,month2,day2)

keyword = "bugs"

# print a list of bugs between two times t1 and t2 for a query search with a keyword

printBugs(keyword,t1,t2)