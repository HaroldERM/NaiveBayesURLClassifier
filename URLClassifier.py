from bs4 import BeautifulSoup
import requests
import csv
import random
import concurrent.futures
import matplotlib.pyplot as plt
from tkinter import *

# -----------------------------------------------
# -----------------------------------------------
# --- Words list ---


def webScrappingSport(url):
    sport_list = []
    r = requests.get(url)
    s = BeautifulSoup(r.text, "html.parser")
    for i in s.find_all("span"):
        for x in i.find_all("a"):
            sport_list.append(x.text)
    return (sport_list)


def webScrappingScience(url):
    science_list = []
    r = requests.get(url)
    s = BeautifulSoup(r.text, "html.parser")
    for i in s.find_all("span"):
        for x in i.find_all("a"):
            science_list.append(x.text)
    return (science_list)


with concurrent.futures.ThreadPoolExecutor() as executor:
    sport_list = executor.submit(
        webScrappingSport, "https://relatedwords.io/sports")
    science_list = executor.submit(
        webScrappingScience, "https://relatedwords.io/science")

# --- END Words list ---
# -----------------------------------------------
# -----------------------------------------------


# -----------------------------------------------
# -----------------------------------------------
# --- Get Links ---


def getLinksFromCSV():
    file = open('Links.csv')
    type(file)

    csvreader = csv.reader(file)

    links = []
    for row in csvreader:
        links.append(row[1])

    file.close()

    return random.choices(links, k=10000)


link_list = getLinksFromCSV()
list1 = link_list[0:1000]
list2 = link_list[1000:2000]
list3 = link_list[2000:3000]
list4 = link_list[3000:4000]
list5 = link_list[4000:5000]
list6 = link_list[5000:6000]
list7 = link_list[6000:7000]
list8 = link_list[7000:8000]
list9 = link_list[8000:9000]
list10 = link_list[9000:10000]


# --- END Get Links ---
# -----------------------------------------------
# -----------------------------------------------


# -----------------------------------------------
# -----------------------------------------------
# --- Web Scrapping Links ---
def webScrappingLink(links):
    cont_error = 0
    complete_list = []
    for link in links:
        word_list = []
        word_list.append(link)
        try:
            r = requests.get(link)
            r.raise_for_status()
        except Exception as err:
            cont_error += 1
        else:
            s = BeautifulSoup(r.text, "html.parser")
            for x in s.find_all("div"):
                word_list.append(x.text)
            for x in s.find_all("a"):
                word_list.append(x.text)
            for x in s.find_all("p"):
                word_list.append(x.text)
            for x in s.find_all("h1"):
                word_list.append(x.text)
            for x in s.find_all("h2"):
                word_list.append(x.text)
            for x in s.find_all("h3"):
                word_list.append(x.text)
            for x in s.find_all("h4"):
                word_list.append(x.text)
            for x in s.find_all("h5"):
                word_list.append(x.text)
            for x in s.find_all("h6"):
                word_list.append(x.text)
            complete_list.append(word_list)
    complete_list.append(cont_error)
    return (complete_list)


with concurrent.futures.ThreadPoolExecutor() as executor:
    block_list1 = executor.submit(webScrappingLink, list1)
    block_list2 = executor.submit(webScrappingLink, list2)
    block_list3 = executor.submit(webScrappingLink, list3)
    block_list4 = executor.submit(webScrappingLink, list4)
    block_list5 = executor.submit(webScrappingLink, list5)
    block_list6 = executor.submit(webScrappingLink, list6)
    block_list7 = executor.submit(webScrappingLink, list7)
    block_list8 = executor.submit(webScrappingLink, list8)
    block_list9 = executor.submit(webScrappingLink, list9)
    block_list10 = executor.submit(webScrappingLink, list10)

# --- END Web Scrapping Links ---
# -----------------------------------------------
# -----------------------------------------------


# -----------------------------------------------
# -----------------------------------------------
# --- Filter Words (replace) ---
def filterWords(list):
    for i in list:
        if type(i) != int:
            for x in range(1, len(i)):
                i[x] = i[x].replace('\n', ' ')
                i[x] = i[x].replace('\r', ' ')
                i[x] = i[x].replace('\t', ' ')
                i[x] = i[x].replace('\\', ' ')
                i[x] = i[x].replace('\'', ' ')
                i[x] = i[x].replace('\"', ' ')
                i[x] = i[x].replace('/', ' ')
                i[x] = i[x].replace('.', ' ')
                i[x] = i[x].replace(',', ' ')
                i[x] = i[x].replace('@', ' ')
                i[x] = i[x].replace('0', ' ')
                i[x] = i[x].replace('1', ' ')
                i[x] = i[x].replace('2', ' ')
                i[x] = i[x].replace('3', ' ')
                i[x] = i[x].replace('4', ' ')
                i[x] = i[x].replace('5', ' ')
                i[x] = i[x].replace('6', ' ')
                i[x] = i[x].replace('7', ' ')
                i[x] = i[x].replace('8', ' ')
                i[x] = i[x].replace('9', ' ')
                i[x] = i[x].replace(':', ' ')
                i[x] = i[x].replace('"', ' ')
                i[x] = i[x].replace('(', ' ')
                i[x] = i[x].replace('“', ' ')
                i[x] = i[x].replace(')', ' ')
                i[x] = i[x].replace('#', ' ')
                i[x] = i[x].replace('-', ' ')
                i[x] = i[x].replace(';', ' ')
                i[x] = i[x].replace('&', ' ')
                i[x] = i[x].replace('*', ' ')
                i[x] = i[x].replace('+', ' ')
                i[x] = i[x].replace('_', ' ')
                i[x] = i[x].replace('—', ' ')
                i[x] = i[x].replace('$', ' ')
                i[x] = i[x].replace('!', ' ')
                i[x] = i[x].replace('?', ' ')
                i[x] = i[x].replace('’', ' ')
                i[x] = i[x].replace('|', ' ')
                i[x] = i[x].replace('©', ' ')
                i[x] = i[x].replace('Â', ' ')
                i[x] = i[x].replace('[', ' ')
                i[x] = i[x].replace(']', ' ')
                i[x] = i[x].replace('{', ' ')
                i[x] = i[x].replace('}', ' ')
                i[x] = i[x].replace('=', ' ')
                i[x] = i[x].replace('^', ' ')
                i[x] = i[x].replace('%', ' ')
                i[x] = i[x].replace('<', ' ')
                i[x] = i[x].replace('>', ' ')
                i[x] = i[x].replace('→', ' ')
                i[x] = i[x].replace('…', ' ')
                i[x] = i[x].replace('~', ' ')
                i[x] = i[x].replace('×', ' ')
                i[x] = i[x].replace('`', ' ')
                i[x] = i[x].replace('°', ' ')
                i[x] = i[x].replace('\xa0', ' ')
    return list


with concurrent.futures.ThreadPoolExecutor() as executor:
    filter_list1 = executor.submit(filterWords, block_list1.result())
    filter_list2 = executor.submit(filterWords, block_list2.result())
    filter_list3 = executor.submit(filterWords, block_list3.result())
    filter_list4 = executor.submit(filterWords, block_list4.result())
    filter_list5 = executor.submit(filterWords, block_list5.result())
    filter_list6 = executor.submit(filterWords, block_list6.result())
    filter_list7 = executor.submit(filterWords, block_list7.result())
    filter_list8 = executor.submit(filterWords, block_list8.result())
    filter_list9 = executor.submit(filterWords, block_list9.result())
    filter_list10 = executor.submit(filterWords, block_list10.result())

# --- END Filter Words (replace) ---
# -----------------------------------------------
# -----------------------------------------------


# -----------------------------------------------
# -----------------------------------------------
# --- Filter Words (split) ---
def splitWords(list):
    complete_list = []
    for i in list:
        if type(i) != int:
            split_list = []
            split_list.append(i[0])
            for x in range(1, len(i)):
                if ' ' in i[x]:
                    i[x] = i[x].split()
                    if type(i[x]) == type(list):
                        for e in i[x]:
                            if len(e) > 1:
                                aux = e.lower()
                                if aux not in split_list:
                                    split_list.append(aux)
                    else:
                        if len(i[x]) > 1:
                            aux = i[x].lower()
                            if aux not in split_list:
                                split_list.append(aux)
            complete_list.append(split_list)
    return complete_list


with concurrent.futures.ThreadPoolExecutor() as executor:
    perfect_list1 = executor.submit(splitWords, filter_list1.result())
    perfect_list2 = executor.submit(splitWords, filter_list2.result())
    perfect_list3 = executor.submit(splitWords, filter_list3.result())
    perfect_list4 = executor.submit(splitWords, filter_list4.result())
    perfect_list5 = executor.submit(splitWords, filter_list5.result())
    perfect_list6 = executor.submit(splitWords, filter_list6.result())
    perfect_list7 = executor.submit(splitWords, filter_list7.result())
    perfect_list8 = executor.submit(splitWords, filter_list8.result())
    perfect_list9 = executor.submit(splitWords, filter_list9.result())
    perfect_list10 = executor.submit(splitWords, filter_list10.result())

# --- END Filter Words (split) ---
# -----------------------------------------------
# -----------------------------------------------


# -----------------------------------------------
# -----------------------------------------------
# --- Naive Bayes ---
def naiveBayes(list):
    complete_list = []
    for i in list:
        cont_sport = 0
        cont_science = 0
        cont_other = 0
        cont_list = []
        cont_list.append(i[0])
        for x in range(1, len(i)):
            if i[x] in sport_list.result():
                cont_sport += 1
            if i[x] in science_list.result():
                cont_science += 1
            else:
                cont_other += 1
        cont_list.append(cont_sport)
        cont_list.append(cont_science)
        cont_list.append(cont_other)
        complete_list.append(cont_list)
    return complete_list


with concurrent.futures.ThreadPoolExecutor() as executor:
    bayes_list1 = executor.submit(naiveBayes, perfect_list1.result())
    bayes_list2 = executor.submit(naiveBayes, perfect_list2.result())
    bayes_list3 = executor.submit(naiveBayes, perfect_list3.result())
    bayes_list4 = executor.submit(naiveBayes, perfect_list4.result())
    bayes_list5 = executor.submit(naiveBayes, perfect_list5.result())
    bayes_list6 = executor.submit(naiveBayes, perfect_list6.result())
    bayes_list7 = executor.submit(naiveBayes, perfect_list7.result())
    bayes_list8 = executor.submit(naiveBayes, perfect_list8.result())
    bayes_list9 = executor.submit(naiveBayes, perfect_list9.result())
    bayes_list10 = executor.submit(naiveBayes, perfect_list10.result())

# --- END Naive Bayes ---
# -----------------------------------------------
# -----------------------------------------------


# -----------------------------------------------
# -----------------------------------------------
# --- Naive Bayes Link ---
def naiveBayesLink(list):
    complete_list = []
    for i in list:
        aux_list = []
        aux_list.append(i[0])
        aux_list.append((600/1200) * (i[1]/600))
        aux_list.append((600/1200) * (i[2]/600))
        aux_list.append((600/1200) * (i[3]/600))
        if (aux_list[1] > aux_list[2] and aux_list[1] > aux_list[3]) or (aux_list[1] > 0.02 and aux_list[1] > aux_list[2]):
            aux_list.append(1)
        elif (aux_list[2] > aux_list[1] and aux_list[2] > aux_list[3]) or (aux_list[2] > 0.02 and aux_list[2] > aux_list[1]):
            aux_list.append(2)
        else:
            aux_list.append(3)
        complete_list.append(aux_list)
    return complete_list


with concurrent.futures.ThreadPoolExecutor() as executor:
    perfect_bayes1 = executor.submit(naiveBayesLink, bayes_list1.result())
    perfect_bayes2 = executor.submit(naiveBayesLink, bayes_list2.result())
    perfect_bayes3 = executor.submit(naiveBayesLink, bayes_list3.result())
    perfect_bayes4 = executor.submit(naiveBayesLink, bayes_list4.result())
    perfect_bayes5 = executor.submit(naiveBayesLink, bayes_list5.result())
    perfect_bayes6 = executor.submit(naiveBayesLink, bayes_list6.result())
    perfect_bayes7 = executor.submit(naiveBayesLink, bayes_list7.result())
    perfect_bayes8 = executor.submit(naiveBayesLink, bayes_list8.result())
    perfect_bayes9 = executor.submit(naiveBayesLink, bayes_list9.result())
    perfect_bayes10 = executor.submit(naiveBayesLink, bayes_list10.result())
# --- END Naive Bayes Link ---
# -----------------------------------------------
# -----------------------------------------------


# -----------------------------------------------
# -----------------------------------------------
# --- Count Results ---

def countResults(list):
    cont1 = 0
    cont2 = 0
    cont3 = 0
    list_sport = []
    list_science = []
    list_other = []
    for i in list:
        if i[4] == 1:
            cont1 += 1
            list_sport.append(i[0])
        elif i[4] == 2:
            cont2 += 1
            list_science.append(i[0])
        else:
            cont3 += 1
            list_other.append(i[0])

    return [cont1, cont2, cont3, list_sport, list_science, list_other]


with concurrent.futures.ThreadPoolExecutor() as executor:
    final_results1 = executor.submit(countResults, perfect_bayes1.result())
    final_results2 = executor.submit(countResults, perfect_bayes2.result())
    final_results3 = executor.submit(countResults, perfect_bayes3.result())
    final_results4 = executor.submit(countResults, perfect_bayes4.result())
    final_results5 = executor.submit(countResults, perfect_bayes5.result())
    final_results6 = executor.submit(countResults, perfect_bayes6.result())
    final_results7 = executor.submit(countResults, perfect_bayes7.result())
    final_results8 = executor.submit(countResults, perfect_bayes8.result())
    final_results9 = executor.submit(countResults, perfect_bayes9.result())
    final_results10 = executor.submit(countResults, perfect_bayes10.result())

# --- END Count Results ---
# -----------------------------------------------
# -----------------------------------------------


# -----------------------------------------------
# -----------------------------------------------
# --- Final Results ---


def finalResults():
    result_sport = final_results1.result()[0]+final_results2.result()[0]+final_results3.result()[0]+final_results4.result()[0]+final_results5.result(
    )[0]+final_results6.result()[0]+final_results7.result()[0]+final_results8.result()[0]+final_results9.result()[0]+final_results10.result()[0]

    result_science = final_results1.result()[1]+final_results2.result()[1]+final_results3.result()[1]+final_results4.result()[1]+final_results5.result(
    )[1]+final_results6.result()[1]+final_results7.result()[1]+final_results8.result()[1]+final_results9.result()[1]+final_results10.result()[1]

    result_other = final_results1.result()[2]+final_results2.result()[2]+final_results3.result()[2]+final_results4.result()[2]+final_results5.result(
    )[2]+final_results6.result()[2]+final_results7.result()[2]+final_results8.result()[2]+final_results9.result()[2]+final_results10.result()[2]

    result_errors = block_list1.result()[-1]+block_list2.result()[-1]+block_list3.result()[-1]+block_list4.result()[-1]+block_list5.result(
    )[-1]+block_list6.result()[-1]+block_list7.result()[-1]+block_list8.result()[-1]+block_list9.result()[-1]+block_list10.result()[-1]

    links_sport = final_results1.result()[3]+final_results2.result()[3]+final_results3.result()[3]+final_results4.result()[3]+final_results5.result(
    )[3]+final_results6.result()[3]+final_results7.result()[3]+final_results8.result()[3]+final_results9.result()[3]+final_results10.result()[3]

    links_science = final_results1.result()[4]+final_results2.result()[4]+final_results3.result()[4]+final_results4.result()[4]+final_results5.result(
    )[4]+final_results6.result()[4]+final_results7.result()[4]+final_results8.result()[4]+final_results9.result()[4]+final_results10.result()[4]

    links_other = final_results1.result()[5]+final_results2.result()[5]+final_results3.result()[5]+final_results4.result()[5]+final_results5.result(
    )[5]+final_results6.result()[5]+final_results7.result()[5]+final_results8.result()[5]+final_results9.result()[5]+final_results10.result()[5]

    root = Tk()
    root.geometry("300x300")

    def graph():
        fig, ax = plt.subplots()
        ax.bar(['Sport', 'Science', 'Others', 'Invalid Links'], [
               result_sport, result_science, result_other, result_errors])
        plt.show()

    def sportLinks():
        top = Toplevel(root)
        top.geometry("500x500")
        scrollbar = Scrollbar(top)
        scrollbar.pack(side=RIGHT, fill=Y)

        mylist = Listbox(top, yscrollcommand=scrollbar.set, width="500")
        for i in links_sport:
            mylist.insert(END, i)

        mylist.pack(side=LEFT, fill=BOTH)
        scrollbar.config(command=mylist.yview)

    def scienceLinks():
        top = Toplevel(root)
        top.geometry("500x500")
        scrollbar = Scrollbar(top)
        scrollbar.pack(side=RIGHT, fill=Y)

        mylist = Listbox(top, yscrollcommand=scrollbar.set, width="500")
        for i in links_science:
            mylist.insert(END, i)

        mylist.pack(side=LEFT, fill=BOTH)
        scrollbar.config(command=mylist.yview)

    def otherLinks():
        top = Toplevel(root)
        top.geometry("500x500")
        scrollbar = Scrollbar(top)
        scrollbar.pack(side=RIGHT, fill=Y)

        mylist = Listbox(top, yscrollcommand=scrollbar.set, width="500")
        for i in links_other:
            mylist.insert(END, i)

        mylist.pack(side=LEFT, fill=BOTH)
        scrollbar.config(command=mylist.yview)

    Button(root, text="Graph", command=graph,
           padx=5, pady=10).pack(padx=5, pady=10)

    Button(root, text="Sport links", command=sportLinks,
           padx=5, pady=10).pack(padx=5, pady=10)

    Button(root, text="Science links", command=scienceLinks,
           padx=5, pady=10).pack(padx=5, pady=10)

    Button(root, text="Other links", command=otherLinks,
           padx=5, pady=10).pack(padx=5, pady=10)

    root.mainloop()


finalResults()
# --- END Final Results ---
# -----------------------------------------------
# -----------------------------------------------
