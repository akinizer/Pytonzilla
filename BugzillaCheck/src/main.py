import requests, bugzilla, datetime

# !!you need to do "pip install bugzilla"!!

# apikey generated from user account in bugzilla
# which is necessary for authorization of thr query access in Bugzilla Mozilla
apikey = "YOUR_BUGZILLA_API_KEY_GOES_HERE"


def printBug(bugid):
    url = "https://bugzilla.mozilla.org/rest/bug"
    r = requests.get(url, params={'id': bugid, 'api_key': apikey})
    return r.json()['bugs'][0]


def searchBugs(keyword, time1, time2):
    url = "https://bugzilla.mozilla.org/rest/"
    b = bugzilla.Bugzilla(url=url,api_key=apikey)

    # keyword: "eclipse"
    # get list of "bug arrays" from search
    # check creation_time attribute of bugs in the list

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

print("\nA list of bugs between dates of ",t1.date()," and ",t2.date(),":\n")

# print a list of bugs between two times t1 and t2 for a query search with a keyword

printBugs(keyword,t1,t2)

# print a bug with bugid

bugid = "INSERT_BUG_ID_HERE"

print("\n\nBug with id ",bugid,":\n",printBug(bugid))

# the labels i.e 'is_confirmed' keep values of attributes, to reach them:

# bugzilla.Bugzilla(url=url,api_key=apikey)['bugs']['INSERT_LABELNAME'] OR
# requests.get(url, params={'id': bugid, 'api_key': apikey})['bugs']['INSERT_LABELNAME']
