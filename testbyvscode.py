import requests
from bs4 import BeautifulSoup
import lxml
from IPython.core.display import display, HTML
import pandas as pd

hlist = ['https://newsinfo.inquirer.net/1304791/who-indoor-airborne-spread-of-coronavirus-possible',
    'https://www.theguardian.com/world/live/2020/jul/10/coronavirus-live-news-global-update-cases-bolivia-president-covid-19-positive-south-africa-brazil-president-jair-bolsonaro-latest-updatescoronavirus-live-news-bolivia-president-tests-positive-as-south-africa-sees-record-case-rise',
    'https://www.wsj.com/articles/oil-went-below-0-some-think-it-will-rebound-to-150-one-day-11594287002',
    'https://www.cnbc.com/2020/07/09/disney-reopening-this-week-even-as-coronavirus-cases-spike-in-florida.html',
    'https://www.cnbc.com/2020/07/09/who-warns-the-coronavirus-is-getting-worse-continues-to-accelerate.html',
    'http://feeds.foxbusiness.com/~r/foxbusiness/latest/~3/y4ny8VF4PX0/us-stocks-july-9-2020',
    'http://www.marketwatch.com/news/story.asp?guid=%7BAED11BCA-C218-11EA-B5C1-1D55841A4EF0%7D&siteid=rss&rss=1',
    'http://www.marketwatch.com/news/story.asp?guid=%7B0A9972CF-FF2C-4035-AA5B-3D557A0B7869%7D&siteid=rss&rss=1',
    'https://www.wsj.com/articles/vaccine-stock-soars-rewarding-investors-big-bet-11594294901',
    'https://www.bbc.co.uk/news/uk-england-kent-53349929',
    'http://feeds.foxnews.com/~r/foxnews/national/~3/45WkRCxllyI/health-official-trump-rally-likely-source-virus-surge',
    'https://www.nytimes.com/2020/07/09/us/politics/trump-supreme-court-appointees.html']




# need the following to tell it we are a firefox browser in order to prevent getting blocked as a bot
headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

r = requests.get(hlist[0], headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')

print(r.text[0:500])

paperlist = ["http://davaotoday.com/main/",
    "https://www.eaglenews.ph/",
    "https://www.gmanetwork.com/news/",
    "https://www.inquirer.net/",
    "https://www.interaksyon.com/",
    "https://pia.gov.ph/news",
    "https://edgedavao.net/",
    "http://www.senate.gov.ph/",
    "https://politics.com.ph/",
    "https://www.mindanews.com/",
    "https://palawan-news.com/",
    "https://philnews.ph/",
    "https://www.philstar.com/",
    "https://www.manilatimes.net/",
    "https://mb.com.ph/",
    "https://www.rappler.com/",
    "http://retiredanalyst.blogspot.com/",
    "http://tempo.com.ph/",
    "https://news.abs-cbn.com/",
    "https://asia.nikkei.com/",
    "https://www.benarnews.org/english/",
    "https://www.theborneopost.com/",
    "https://www.straitstimes.com/global",
    "https://www.thejakartapost.com/",
    "http://www.straitstimes.com/asia/",
    "http://www.straitstimes.com/asia/east-asia/",
    "https://www.scmp.com/",
    "https://www.globaltimes.cn/",
    "https://www.nytimes.com/",
    "https://www.foxnews.com/",
    "https://cnnphilippines.com/"]

covid_taglist	=	["covid-19",	
			"coronavirus",
			"quarantine",
			"pandemic",
			"vaccine",
			"injections",
			"ecq",
			"mecq",
			"gcq",
			"mgcq",
			"lsi",
			"locally stranded individuals",
			"death rate",
			"new cases",
			"total cases"]

econ_taglist	=	["economy",	
			"inflation",
			"angkas",
			"backriding",
			"bitcoin",
			"crypto",
			"cryptocurrencies",
			"crypto-currencies",
			"asia development bank",
			"psei",
			"buses",
			"employment",
			"build-build-build",
			"investments"
            "chinese banks"]
			
chinathreat_taglist	=	["south china sea",	
			"west philippine sea",
			"liu jianchao",
			"chinese ambassador",
			"xi xingping",
			"spratly islands",
			"freedom of navigation",
			"pla navy",
			"vfa",
			"scarborough shoal",
			"mischief reef",
			"pla militia",
			"air defense identification zone",
			"adiz",
			"visiting forces agreement",
			"philippine navy",
			"brp",
			"us navy",
			"navy",
            "us troops",
            "guard against china",
            "beidaihe",
            "lorenzana"]
			
insurgency_taglist	=	["anti-terror",	
			"anti-terror law",
			"abu sayyaf",
			"biff",
			"bangsamoro islamic freedom fighters",
			"npa",
			"new people's army",
			"milf",
			"moro islamic liberation front",
			"mnlf",
			"moro national liberation front",
			"islamic state",
			"sison",
			"marawi",
			"mamasapano"]

			
			
pulitika_taglist	=	["lopez",	
			"supreme court",
			"serreno",
			"duterte",
			"abs-cbn",
			"house votes",
			"senate votes",
			"opposition"]
			
			
province_taglist	=	["palawan",	
			"manobo",
			"tuguegarao",
			"cagayan valley",
			"igorot",
			"lumad",
			"ipra",
			"indigenous",
			"kankanaey",
			"palawano",
			"agutaya",
			"malaybalay",
			"bukidnon",
			"higaunon",
			"davao"]
			
			
ncr_taglist	=	["rizal province",	
			"antipolo",
			"mandaluyong",
			"cainta",
			"edsa",
			"taguig",
			"quezon city"]
			
			
chrgroup_taglist	=	["catholic",	
			"catholic bishop’s conference of the philippines",
			"catholic bishops conference of the philippines",
			"cbcp",
			"iglesia ni cristo",
			"quiboloy",
			"quibuloy"]
			
			
moro_taglist	=	["moro",	
			"bangsamoro",
			"barmm",
			"sultan kudarat",
			"sulu",
			"basilan",
			"jolo",
			"maranao",
			"tausug",
			"maguindanao",
			"cotobato",
			"cotabato",
			"sabah",
			"sultan of sulu",
			"sultanate of sulu"]
			
			
auth_taglist	=	["duterte",	
			"red-tagging",
			"anti-terror",
			"jose calida",
			"solicitor general",
			"medialdea",
			"bong go",
			"bato dela rosa",
			"ronald dela rosa",
			"dela rosa",
			"de la rosa"]

exclude_list = ["leave a comment on",
    "california",
    "watch",
    "permalink",
    "inmate",
    "stores closed",
    "overseas filipinos",
    "alibaba",
    "artistry",
    "flu pandemic",
    "korean trash",
    "walmart",
    "us stores",
    "tournament",
    "filipino workers stranded",
    "donald trump",
    "rhine river",
    "european union",
    "fertilizer scam",
    "olympics",
    "coronavirus affects",
    "kids in malaysia",
    "liquor ban",
    "piolo pascual",
    "profile of a killer",
    "croatia",
    "nba",
    "sexual abuse",
    "festival queen",
    "tips for parents",
    "arcadia fitness gym"]

taglist =  covid_taglist+ auth_taglist+ chinathreat_taglist+ chrgroup_taglist+ econ_taglist+ insurgency_taglist+ moro_taglist+ ncr_taglist+ province_taglist+ pulitika_taglist
taglist = list(set(taglist))
taglist.sort()

# FORMAT FOR THE TAG DICTIONARIES
# IF A TAG IS TO BE SCREENED INTO THE LIST WITHOUT A CORRESPONDING OTHER TAG
# THE TERM 'solotag' MUST BE ONE OF THE ANDTAGS IN THE DICTIONARY

covid_tagdict=[{"maintag":"covid","andtag01":"hunt","andtag02":"lockdown","andtag03":"infected with",
        "andtag04":"hahawa","angtag05":"cases","andtag06":"house-to-house","andtag07":"test positive",
        "andtag08":"statistics","andtag09":""},
	{"maintag":"covid","andtag01":"infection","andtag02":"","andtag03":"",
        "andtag04":"","angtag05":"","andtag06":"","andtag07":"",
        "andtag08":"","andtag09":""},
    {"maintag":"coronavirus","andtag01":"vaccine","andtag02":"","andtag03":"",
        "andtag04":"","angtag05":"","andtag06":"","andtag07":"",
        "andtag08":"","andtag09":""},
	{"maintag":"quarantine","andtag01":"classification","andtag02":"home","andtag03":"facility",
        "andtag04":"facilities","angtag05":"","andtag06":"","andtag07":"",
        "andtag08":"","andtag09":""},
	{"maintag":"pandemic","andtag01":"flying back","andtag02":"barter","andtag03":"",
        "andtag04":"","angtag05":"","andtag06":"","andtag07":"",
        "andtag08":"","andtag09":""},
	{"maintag":"injections","andtag01":"solotag","andtag02":"","andtag03":"",
        "andtag04":"","angtag05":"","andtag06":"","andtag07":"",
        "andtag08":"","andtag09":""},
	{"maintag":"ecq","andtag01":"list","andtag02":"gcq","andtag03":"mgcq",
        "andtag04":"mecq","angtag05":"city","andtag06":"province","andtag07":"provinces",
        "andtag08":"metro","andtag09":""},
    {"maintag":"mecq","andtag01":"list","andtag02":"gcq","andtag03":"mgcq",
        "andtag04":"ecq","angtag05":"city","andtag06":"province","andtag07":"provinces",
        "andtag08":"metro","andtag09":""},
	{"maintag":"gcq","andtag01":"list","andtag02":"ecq","andtag03":"mgcq",
        "andtag04":"mecq","angtag05":"city","andtag06":"province","andtag07":"provinces",
        "andtag08":"metro","andtag09":""},
	{"maintag":"mgcq","andtag01":"list","andtag02":"gcq","andtag03":"ecq",
        "andtag04":"mecq","angtag05":"city","andtag06":"province","andtag07":"provinces",
        "andtag08":"metro","andtag09":""},
	{"maintag":"lsi","andtag01":"","andtag02":"","andtag03":"",
        "andtag04":"","angtag05":"","andtag06":"","andtag07":"",
        "andtag08":"","andtag09":""},
	{"maintag":"locally","andtag01":"stranded","andtag02":"individuals","andtag03":"",
        "andtag04":"","angtag05":"","andtag06":"","andtag07":"covid-19",
        "andtag08":"","andtag09":""},  
	{"maintag":"death rate","andtag01":"solotag","andtag02":"","andtag03":"",
        "andtag04":"","angtag05":"","andtag06":"","andtag07":"",
        "andtag08":"","andtag09":""},
	{"maintag":"cases","andtag01":"new","andtag02":"total","andtag03":"recoveries",
        "andtag04":"infection","angtag05":"","andtag06":"","andtag07":"",
        "andtag08":"","andtag09":""}]

covid_tagdf = pd.DataFrame(covid_tagdict)
covid_tagdf.set_index('maintag', inplace=True)

auth_tagdict=[{"maintag": "duterte", "andtag01":"priority", "andtag02":"war", "andtag03":"martial", "andtag04":"arrest", "andtag05":"deny", "andtag06":"denies", "andtag07":"abs-cbn", "andtag08":"charter", "andtag09":"cha-cha"},
    {"maintag": "duterte", "andtag01":"onerous", "andtag02":"probe", "andtag03":"fascist", "andtag04":"suffering", "andtag05":"sona", "andtag06":"political", "andtag07":"oligarch", "andtag08":"failing", "andtag09":""},
    {"maintag": "anti-terror", "andtag01":"defends", "andtag02":"autonomous region", "andtag03":"bangsamoro", "andtag04":"", "andtag05":"", "andtag06":"", "andtag07":"", "andtag08":"", "andtag09":""},
    {"maintag": "jolo shooting", "andtag01":"solotag", "andtag02":"", "andtag03":"", "andtag04":"", "andtag05":"", "andtag06":"", "andtag07":"", "andtag08":"", "andtag09":""},
    {"maintag": "red-tagging", "andtag01":"solotag", "andtag02":"", "andtag03":"", "andtag04":"", "andtag05":"", "andtag06":"", "andtag07":"", "andtag08":"", "andtag09":""},
    {"maintag": "trillanes", "andtag01":"solotag", "andtag02":"", "andtag03":"", "andtag04":"", "andtag05":"", "andtag06":"", "andtag07":"", "andtag08":"", "andtag09":""},
    {"maintag": "jose calida", "andtag01":"solotag", "andtag02":"", "andtag03":"", "andtag04":"", "andtag05":"", "andtag06":"", "andtag07":"", "andtag08":"", "andtag09":""},
    {"maintag": "solicitor general", "andtag01":"solotag", "andtag02":"", "andtag03":"", "andtag04":"", "andtag05":"", "andtag06":"", "andtag07":"", "andtag08":"", "andtag09":""},
    {"maintag": "medialdea", "andtag01":"solotag", "andtag02":"", "andtag03":"", "andtag04":"", "andtag05":"", "andtag06":"", "andtag07":"", "andtag08":"", "andtag09":""},
    {"maintag": "bong go", "andtag01":"solotag", "andtag02":"", "andtag03":"", "andtag04":"", "andtag05":"", "andtag06":"", "andtag07":"", "andtag08":"", "andtag09":""},
    {"maintag": "bato dela rosa", "andtag01":"solotag", "andtag02":"", "andtag03":"", "andtag04":"", "andtag05":"", "andtag06":"", "andtag07":"", "andtag08":"", "andtag09":""},
    {"maintag": "ronald dela rosa", "andtag01":"solotag", "andtag02":"", "andtag03":"", "andtag04":"", "andtag05":"", "andtag06":"", "andtag07":"", "andtag08":"", "andtag09":""},
    {"maintag": "dela rosa", "andtag01":"solotag", "andtag02":"", "andtag03":"", "andtag04":"", "andtag05":"", "andtag06":"", "andtag07":"", "andtag08":"", "andtag09":""},
    {"maintag": "de la rosa", "andtag01":"solotag", "andtag02":"", "andtag03":"", "andtag04":"", "andtag05":"", "andtag06":"", "andtag07":"", "andtag08":"", "andtag09":""},
    {"maintag": "de lima", "andtag01":"solotag", "andtag02":"", "andtag03":"", "andtag04":"", "andtag05":"", "andtag06":"", "andtag07":"", "andtag08":"", "andtag09":""}]

auth_tagdf = pd.DataFrame(auth_tagdict)
auth_tagdf.set_index('maintag', inplace=True)

# if there are duplicates, the dictionary returned will be formatted
# with {value duplicated: [list of index values where it is duplicated]}
def find_idxnum_dup(list1):
    from collections import Counter, defaultdict
    duplist = [k for k,v in Counter(list1).items() if v>1]
    D = defaultdict(list)
    for i,item in enumerate(list1):
        D[item].append(i)
    dupdict = {k:v for k,v in D.items() if len(v)>1}
    return duplist, dupdict

def tags_in_str(scanstr, tagdf):
    found_tag = False
    colslist = tagdf.columns.tolist()
    maintaglist = tagdf.index.tolist()
    # find if any main tags are duplicated
    duplist, dupdict = find_idxnum_dup(maintaglist)
    scanned_dups = []
#     print(maintaglist)
#     print(colslist)
#     print(tagdf.loc['duterte'])
#     print("scanstr: ", scanstr)
    for maintag in maintaglist:
#         print('maintag: ', maintag)
#         print(duplist)
#         print(scanned_dups)
#         print(dupdict)
        if maintag in duplist:
            if maintag not in scanned_dups:
#                 print(maintag, duplist, dupdict)
                for idxval in dupdict[maintag]:
                    for andcol in list(range(0,9)):
#                         print(idxval, andcol)
                        andtag = tagdf.iloc[idxval, andcol]
#                         print(andtag)
                        if (maintag in scanstr and andtag in scanstr and andtag != "") or (maintag in scanstr and andtag == "solotag"):
                            found_tag=True
                            break
            scanned_dups.append(maintag)
            
        else:    
            for andcol in colslist:
                andtag = tagdf.loc[maintag, andcol]
                if (maintag in scanstr and andtag in scanstr and andtag != "") or (maintag in scanstr and andtag == "solotag"):
                    found_tag=True
#                     print(maintag, andtag)
                    break
    return found_tag

scanstr = "President Rodrigo Duterte addresses the public May 25, 2020"

if tags_in_str(scanstr.lower(), auth_tagdf):
    print(scanstr)
else:
    print("not found")
auth_tagdf

# if tags_in_str(scanstr.lower(), covid_tagdf):
#     print(scanstr)
# else:
#     print("not found")
# covid_tagdf


def excluder(mystr, exclude_list):
    excludeit = False
    for excl in exclude_list:
        if excl in mystr:
            excludeit = True
            break
    return excludeit

covid_list = []
auth_list = []
chinathreat_list = []
chrgroup_list = []
econ_list = []
insurgency_list = []
moro_list = []
ncr_list = []
province_list = []
pulitika_list = []
errors = 0
pctcount1 = 0
for paper in paperlist:
    pctcount1 +=1
    pctval1 = pctcount1 / len(paperlist)
    print('Percent complete all sources list: ' + "{:.1%}".format(pctval1))
    r = requests.get(paper, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    if (paper == "http://retiredanalyst.blogspot.com/"):
        myelems = soup.findAll('h3')
#         print(len(myelems))
        pctcount2 = 0
        for elem in myelems:
            pctcount2 +=1
            pctval2 = pctcount2 / len(myelems)
#             print('Percent complete retired analyst list: ' + "{:.1%}".format(pctval2))
            # usually there is no title in the retired analyst links, so have to go get those
            url = elem.contents[1].get('href')
            try:
                r2 = requests.get(url, headers=headers)
                soup2 = BeautifulSoup(r2.text, 'html.parser')
                titletext = soup2.title.text

                if scanstr.lower() == titletext.lower():
                    pause = input('type here ')
				
                if not excluder(titletext.lower(), exclude_list):
                    for checker in taglist:
                        if checker.lower() in titletext.lower():
    #                         print(checker, titletext)
                            if tags_in_str(titletext.lower(), covid_tagdf):
                                covid_list.append((titletext, url))
#                             if checker.lower() in auth_taglist:
                            if tags_in_str(titletext.lower(), auth_tagdf):
                                auth_list.append((titletext, url))
                            if checker.lower() in chinathreat_taglist:
                                chinathreat_list.append((titletext, url))
                            if checker.lower() in chrgroup_taglist:
                                chrgroup_list.append((titletext, url))
                            if checker.lower() in econ_taglist:
                                econ_list.append((titletext, url))
                            if checker.lower() in insurgency_taglist:
                                insurgency_list.append((titletext, url))
                            if checker.lower() in moro_taglist:
                                moro_list.append((titletext, url))
                            if checker.lower() in ncr_taglist:
                                ncr_list.append((titletext, url))
                            if checker.lower() in province_taglist:
                                province_list.append((titletext, url))
                            if checker.lower() in pulitika_taglist:
                                    pulitika_list.append((titletext, url))
                            
            except:
                errors += 1
    else:
        myelems = soup.findAll('a')
        pctcount3 = 0
        for elem in myelems:
            pctcount3 +=1
            pctval3 = pctcount3 / len(myelems)
#             print('Percent complete ' + paper + ' list: ' + "{:.1%}".format(pctval3))
            titletext = str(elem.get('title'))
            if not excluder(titletext.lower(), exclude_list):
                url = elem.get('href')
                for checker in taglist:
                    if checker.lower() in titletext.lower():
    #                     print(checker, titletext)
                        if tags_in_str(titletext.lower(), covid_tagdf):
                            covid_list.append((titletext, url))
                        if checker.lower() in auth_taglist:
                            auth_list.append((titletext, url))
                        if checker.lower() in chinathreat_taglist:
                            chinathreat_list.append((titletext, url))
                        if checker.lower() in chrgroup_taglist:
                            chrgroup_list.append((titletext, url))
                        if checker.lower() in econ_taglist:
                            econ_list.append((titletext, url))
                        if checker.lower() in insurgency_taglist:
                            insurgency_list.append((titletext, url))
                        if checker.lower() in moro_taglist:
                            moro_list.append((titletext, url))
                        if checker.lower() in ncr_taglist:
                            ncr_list.append((titletext, url))
                        if checker.lower() in province_taglist:
                            province_list.append((titletext, url))
                        if checker.lower() in pulitika_taglist:
                            pulitika_list.append((titletext, url))
                        
covid_list = list(set(covid_list))
covid_list.sort()
auth_list = list(set(auth_list))
auth_list.sort()
chinathreat_list = list(set(chinathreat_list))
chinathreat_list.sort()
chrgroup_list = list(set(chrgroup_list))
chrgroup_list.sort()
econ_list = list(set(econ_list))
econ_list.sort()
insurgency_list = list(set(insurgency_list))
insurgency_list.sort()
moro_list = list(set(moro_list))
moro_list.sort()
ncr_list = list(set(ncr_list))
ncr_list.sort()
province_list = list(set(province_list))
province_list.sort()
pulitika_list = list(set(pulitika_list))
pulitika_list.sort()

               
hitlist = covid_list+ auth_list+ chinathreat_list+ chrgroup_list+ econ_list+ insurgency_list+ moro_list+ ncr_list+ province_list+ pulitika_list
hitlist = list(set(hitlist))
hitlist.sort()
# sort_disp_list = [covid_list, auth_list, chinathreat_list, chrgroup_list, econ_list, insurgency_list, moro_list, ncr_list, province_list, pulitika_list]
# for elem in hitlist:
#     print(elem[0])
#     print(elem[1])

def display_links(header, newslist, errors):
    print('\n' + header)
    hlist = [elem[1] for elem in newslist]

    for newselem in newslist:
        if newselem[0] == 'None':
            try:
                r = requests.get(newselem[1], headers=headers)
                soup = BeautifulSoup(r.text, 'html.parser')
                titletext = soup.title.text
                reflink = "<a href='" + ilink + "'> " + titletext + "</a>"
                html = HTML(reflink)
                display(html)
            except:
                errors += 1
        else:
            reflink = "<a href='" + newselem[1] + "'> " + newselem[0] + "</a>"
            html = HTML(reflink)
            display(html)
            
    return errors


errors = display_links("COVID-19 NEWS ITEMS: ", covid_list, errors)
errors = display_links("AUTHORITARIANISM/ DEMOCRACY THREAT NEWS ITEMS: ", auth_list, errors)
errors = display_links("CHINA THREAT TO THE PHILIPPINES NEWS ITEMS: ", chinathreat_list, errors)
errors = display_links("CHRISTIAN AND RELIGIOUS GROUPS NEWS ITEMS: ", chrgroup_list, errors)
errors = display_links("ECONOMY NEWS ITEMS: ", econ_list, errors)
errors = display_links("INSURGENCY RELATED NEWS ITEMS: ", insurgency_list, errors)
errors = display_links("MORO ISSUES RELATED NEWS ITEMS: ", moro_list, errors)
errors = display_links("NATIONAL CAPITAL REGION RELATED NEWS ITEMS: ", ncr_list, errors)
errors = display_links("PROVINCIAL NEWS ITEMS: ", covid_list, errors)
errors = display_links("POLITICAL NEWS ITEMS: ", province_list, errors)
print("Errors: ", errors)