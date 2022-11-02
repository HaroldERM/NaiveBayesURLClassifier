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
