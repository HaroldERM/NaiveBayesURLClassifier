## Instituto Tecnológico de Costa Rica      
Principios De Sistemas Operativos.
### Project II                                             Group 51.
### Armando Lorenzo Villalta Pérez - Harold Enrique Ramirez Mora - Daniel Vargas Castro.
#### armandovp2408@estudiantec.cr - enrique5129876@estudiantec.cr - 86097312.dv@estudiantec.cr.
# URL classifier using Naive Bayes Theorem
This project corresponds to the second semester 2022 in the Computer Engineering career. 
According to Chauhan, > “Naïve Bayes is a probabilistic machine learning algorithm based 
on the Bayes Theorem, used in a wide variety of classification tasks.”(N.S.Chauhan, 2022). 	
It also says that Bayes' theorem can be defined as a way of finding a probability when 
we know certain other probabilities.

In this project we are going to classify 10000 urls in different categories using the 
naive bayes algorithm. The programming language selected to make this program is Python.
Being a project which implies classifying url, this means that we will have to inspect 
each url, for this it is necessary to carry out the Web Scraping process, so we have to 
import the `from bs4 import BeautifulSoup` library, this library allows us to be able to 
inspect each url and extract the information we need.

Knowing this, when carrying out this process sequentially we realize that the execution 
time is long, for this problem the proposed solution is to implement parallelism, we 
add the following line to the code: `import concurrent.futures`, which gives us the 
ability to execute the different processes in parallel and in this way the execution 
time is reduced.

#### 1. Imports necessary for the correct functionality of the project
~~~
from bs4 import BeautifulSoup
import requests
import csv
import random
import concurrent.futures
import matplotlib.pyplot as plt
from tkinter import *
~~~
The `BeautifulSoup` library is used to access the urls and the `requests` library is used to extract the data we need.The `CSV` library is used to read documents with a csv extension. The `random` library is used to generate the random list of 10,000 urls to be ranked. `import concurrent.futures` is used to perform parallelism in the functions,in addition, the `matplotlib.pyplot as plt` library is used to create graphs, finally the `tkinter` library is imported to create the interface that will contain the results.

#### 2. Creation of word banks with web scraping
For our project it was decided to create 2 word banks, one with the category of Science and the other with the category of Sports.

~~~
def webScrappingSport(url):
    sport_list = []
    r = requests.get(url)
    s = BeautifulSoup(r.text, "html.parser")
    for i in s.find_all("span"):
        for x in i.find_all("a"):
            sport_list.append(x.text)
    return (sport_list)
~~~
In this function, a url is received which is where the words will be extracted to fill the list of words for the Sports category.

~~~
def webScrappingScience(url):
    science_list = []
    r = requests.get(url)
    s = BeautifulSoup(r.text, "html.parser")
    for i in s.find_all("span"):
        for x in i.find_all("a"):
            science_list.append(x.text)
    return (science_list)
~~~
In the same way, we perform the same function this time to fill the word bank for the Science category.

To execute these functions, we call them in the parallelism method to make it faster.
~~~
with concurrent.futures.ThreadPoolExecutor() as executor:
    sport_list = executor.submit(
        webScrappingSport, "https://relatedwords.io/sports")
    science_list = executor.submit(
        webScrappingScience, "https://relatedwords.io/science")
~~~

#### 3. Obtaining the 10,000 urls to classify.
To obtain this data, a .csv file with the url was downloaded, the download link is: https://www.kaggle.com/datasets/shawon10/url-classification-dataset-dmoz

Once downloaded, a function is created that accesses the document and the 10,000 urls are extracted randomly.
Then the list of 10,000 urls is divided into 10 lists with 1,000 urls each.
~~~
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
~~~

#### 4. Extraction of information from each URL.
The webScrapingLink() function is defined, it receives the list of links and through a for cycle proceeds to access each link in the list to extract the information.

##### Note: To see the full code, access the class called URLClassifier.py
~~~
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
~~~

### 5. Garbage removal through filters.
In this stage, what is done is to perform 2 functions that will help us to clean the recovered information, in this one it is contemplated to eliminate the special characters, in the second the words are separated one by one and all the words are converted to lowercase.

##### Note: To see the full code, access the class called URLClassifier.py

###### funcion 1
~~~
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
~~~

###### funcion 1
~~~
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
~~~

### 6. Match count of words found in the url with respect to the word banks.
In this function, its main characteristic is that it generates the number of matches that each url has with respect to the word banks.
~~~
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
~~~

### 7. Naïve Bayes Classifier
This is the function on which the project could be said to be based, it will proceed to classify the url. For this classification, the prior probability is taken and multiplied by the number of incidences divided by the number of total words in the bank.
~~~
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
~~~

### 8. Main results.
The countResults() function is created to count the results obtained, both the number of urls that belong to each category as well as the urls that could not be visited.
~~~
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
~~~

After obtaining these results, we proceed to use the tkinter library to display the graphics obtained as results on the screen.

For the full implementation check out the URLClassifier.py class.
