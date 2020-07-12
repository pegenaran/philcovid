import requests
from bs4 import BeautifulSoup
import lxml
from IPython.core.display import display, HTML

# need the following to tell it we are a firefox browser in order to prevent getting blocked as a bot
headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

# r = requests.get(hlist[0], headers=headers)
# soup = BeautifulSoup(r.text, 'html.parser')

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
    "https://news.abs-cbn.com/"]

covid_taglist	=	["covid-19",	
			"coronavirus",
			"quarantine",
			"pandemic",
			"vacine",
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
			"investments"]
			
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
			"navy"]
			
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


taglist =  covid_taglist+ auth_taglist+ chinathreat_taglist+ chrgroup_taglist+ econ_taglist+ insurgency_taglist+ moro_taglist+ ncr_taglist+ province_taglist+ pulitika_taglist
taglist = list(set(taglist))
taglist.sort()


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
            print('Percent complete retired analyst list: ' + "{:.1%}".format(pctval2))
            # usually there is no title in the retired analyst links, so have to go get those
            url = elem.contents[1].get('href')
            try:
                r2 = requests.get(url, headers=headers)
                soup2 = BeautifulSoup(r2.text, 'html.parser')
                titletext = soup2.title.text
                for checker in taglist:
                    if checker.lower() in titletext.lower():
#                         print(checker, titletext)
                        if checker.lower() in covid_taglist:
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
                            
            except:
                errors += 1
    else:
        myelems = soup.findAll('a')
        pctcount3 = 0
        for elem in myelems:
            pctcount3 +=1
            pctval3 = pctcount3 / len(myelems)
            print('Percent complete ' + paper + ' list: ' + "{:.1%}".format(pctval3))
            titletext = str(elem.get('title'))
            url = elem.get('href')
            for checker in taglist:
                if checker.lower() in titletext.lower():
                    if "maguindanao blast" in titletext.lower() or "solon claims network" in titletext.lower():
                        print
                    if checker.lower() in covid_taglist:
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
#     xlist = [elem[0] for elem in hitlist]
#     [print(x) for x in xlist]
    for ilink in hlist:
        try:
            r = requests.get(ilink, headers=headers)
            soup = BeautifulSoup(r.text, 'html.parser')
            titletext = soup.title.text
            reflink = "<a href='" + ilink + "'> " + titletext + "</a>"
            html = HTML(reflink)
            display(html)
        except:
            errors += 1

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