import requests, bugzilla, datetime, pandas as pd, numpy as np

# !!you need to do "pip install bugzilla"!!

# apikey generated from user account in bugzilla
# which is necessary for authorization of thr query access in Bugzilla Mozilla
apikey = "INSERT_BUGZILLA_APIKEY"

# --GET DATE--
def time2date(year, month, day):
    return datetime.datetime(year,month,day)


# --FIND BUGS--
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

    for i in searchBugs(keyword, time1,time2):
        print(i)

def printBugsWithNoPriority(keyword,time1,time2):
    # searchBugs gets a keyword to search in query of bugzilla, a start time t1 and a finish time t2,
    # returns a list of bugs with attributes(labels)
    # check whether priority is set, print bugs with no priority

    for i in searchBugs(keyword, time1,time2):
        if i['priority']=="--":
            print(i)

def printBugsWithKeySummary(keyword, time1, time2, bottomLimit, topLimit):
    # searchBugs gets a keyword to search in query of bugzilla, a start time t1 and a finish time t2,
    # returns a list of bugs with attributes(labels)
    # check whether summary is in a specified interval, print bugs with no priority

    for i in searchBugs(keyword, time1,time2):
        if bottomLimit<=len(i['summary'])<=topLimit:
            print(i)


# --END LABELS--


# --FIND LABELS--

# get a list of labels
def printLabels(labelList):
    print("\nLabels:")
    for i in labelList:
        print(i)

# show the list of labels
def getLabels(bugid):
    url = "https://bugzilla.mozilla.org/rest/bug"
    r = requests.get(url, params={'id': bugid, 'api_key': apikey})
    dataframe = pd.DataFrame(data=r.json()['bugs'])

    return dataframe.head()

# --END LABELS--


# --INPUTS--

def bugsBetweenDatesSample():
    # show bugs between two dates t1, t2
    year1=2010
    month1=10
    day1=10

    t1 = time2date(year1,month1,day1)

    year2=2019
    month2=12
    day2=12

    t2 = time2date(year2,month2,day2)

    keyword = "bugs"

    print("\nA list of bugs between dates of ",t1.date()," and ",t2.date(),":\n")

    # print a list of bugs between two times t1 and t2 for a query search with a keyword

    printBugs(keyword,t1,t2)

def prioritySample():
    # show bugs between two dates t1, t2 as (year, month, day)

    keyword = "bugzilla"
    t1 = time2date(2010,10,10)
    t2 = time2date(2019,12,12)

    printBugsWithNoPriority(keyword, t1,t2)


def bugWithIdSample():
    # print a bug with bugid

    bugid = "1600646"

    print("\n\nBug with id ",bugid,":\n",printBug(bugid))

    # the labels i.e 'is_confirmed' keep values of attributes, to reach them:

    # bugzilla.Bugzilla(url=url,api_key=apikey)['bugs']['LABELNAME'] OR
    # requests.get(url, params={'id': bugid, 'api_key': apikey})['bugs']['LABELNAME']

# samples that check no priority and summary length

def labelListSample():
    bugid = "1600646"

    # print labels
    labels = getLabels(bugid)
    printLabels(labels)

def summarySample():
    keyword = "eclipse"
    t1 = time2date(2016,11,15)
    t2 = time2date(2020,1,1)

    minCharacters = 10
    maxCharacters = np.inf  # no limit

    printBugsWithKeySummary(keyword,t1,t2,minCharacters,maxCharacters)


# --END INPUTS--
