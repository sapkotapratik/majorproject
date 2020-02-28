\include{KECReportFormat} %includes the file KecReportFormat.tex that include all necessary formattings
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%Define Macros for Details of your Project
\newcommand{\project}{Major Project} %Specify "Major Project" or "Minor Project"
\newcommand{\projectTitle}{Nepali News Classifier} %specify "Title" of Your Project
\newcommand{\doc}{Mid-Term Report} % specify the document you are preparing eg. "Proposal", "Mid-Term Report" or "Final Report" 
% Note that You have to sibmit "Final Report" for Pre-final defense as well.
\newcommand{\subCode}{CT707} %specify Subject of Your Project
\newcommand{\degree}{Bachelor in Computer Engineering} %specify your degree
\newcommand{\submittedBy}%Specify Names and Roll/Symbol Numbers of the Project Group Members
{
%Edit Member Names and Roll/Symbol No. and adjust width (\makebox[width]) if necessary 
\makebox[9cm]{Alisha Dahal \hfill [03/BCT/2073]}\\
\makebox[9cm]{Dikshya Tamling Limbu \hfill [16/BCT/2073]}\\
\makebox[9cm]{Pratik Sapkota \hfill [29/BCT/2073]}\\
\makebox[9cm]{Nayan Deep Rijal \hfill [113/BCT/2073]}
%\makebox[9cm]{Member Name \hfill [Roll/Symbol No.]}\\
} % Note that You must write your "Symbol Numbers"(Exam Roll Numbers) for Final Defenses

\newcommand{\submittedTo}{Department of Computer and Electronics Engineering} %specify your department
\newcommand{\hod}{Er. Rabindra Khati} %specify Head ot the department
\newcommand{\defYear}{2020} %Defense Year
\newcommand{\defMonth}{Feb} %Defense Month- January, February, ...
\newcommand{\defDay}{24} %specify Defense Day- 1, 2, ...

\newif\ifhassupervisor
\hassupervisorfalse % to display supervisor name use command- \hassupervisortrue
 
\newcommand{\supervisor}{Supervisor's Name} % Specify Name of Supervisor for Major Project
\newcommand{\degSup}{Supervisor's Designation\\Second Line of Designation (if required)} %Specify Designation of Supervisor for Major Project, use multiple lines (\\) if necessary
\newcommand{\external}{External's Name} %Specify Name of External for Major Project (Required for Black Book)
\newcommand{\degExternal}{External's Designation\\Second Line of Designation (if required)} %Specify Name of External for Major Project (Required for Black Book) , use multiple lines (\\) if necessary


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%The Document
\begin{document}

\KECcoverpage % command defined in KECReportFormat
\KECtitlepage % command defined in KECReportFormat

\pagenumbering{roman} % starts pagenumberins in Roman numerals i, ii, ...

%Copyright Page is required for FINAL REPORT only. Comment this section for other Reports.
%\KECcopyright % defined in KECReportFormat.tex

%Approval Page is required for FINAL(Black Book Binded) REPORT of MAJOR PROJECT only. Comment this section for other Reports. 
%\KECapproval % defined in KECReportFormat.tex

\chapter*{Abstract} % The summary of your report
\addcontentsline{toc}{chapter}{Abstract}%to include this chapter in TOC 
Nepali News classification is the task of categorizing news into some predefined categories based on their content with the confidence learned from the training news dataset. This project will make comparison on some of the most widely used machine learning techniques, mainly Naive Bayes, and SVM  for Nepali news classification problem. For the experimentation and building the classifier we will be crawling different national news portal for our dataset. This can be seen as text classification problem. Text classification  is one of the most widely used natural language processing(NLP) applications in different business problems.
\par
\textbf{\textit{Keywords$-$}} Machine Learning, Natural Language Processing, SVM , Nepali News Classification


%to adjust spacings for TOC, LOF, LOT
{
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%TOC, LOF and LOT
\KECadjusttocspacings % defined in KECReportFormat.tex to adjust spacings
\makeatletter
% to add vskip of 18 point which is reduced when parskip is set to 0 in \LECadjustspacings
\def\@makeschapterhead#1{%
  %\vspace*{50\p@}% Remove the vertical space
  {\newpage \parindent \z@ \raggedright
    \normalfont
    \interlinepenalty\@M
    \center \fontsize{16pt}{1} \bfseries \MakeUppercase{#1}\par\nobreak
    \vskip 18\p@ % adjust space after heading 18pt
  }}
\makeatother 

\tableofcontents % prints table of contents
\listoffigures % prints list of figures
%\listoftables % prints list of table
}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%comment this chapter if you don't have List of Abbreviations
\KECloa % defined in KECReportFormat

%comment this chapter if you don't have List of Symbols
\KEClos % defined in KECReportFormat

\newpage
\pagenumbering{arabic} % starts pagenumbering in arabic numerals

\chapter{Introduction}
\section{Background}\label{sec:bkgrnd}%label your section if you require to refer them somewhere else in your document.
This project is intended to be a walk through on the development of a machine learning project  used to create an application that can be used to obtain some benefit to a set of users.This is achieved with a supervised machine learning classification model that is able to predict the category of a given news article, a web scraping method that gets  the  latest  news  from  the  newspapers,  and  an interactive  web  application that shows the obtained results to the user.This can be seen as a text classification problem. Text classification is one of the widely  used  natural  language  processing  (NLP)applications  in  different business problems.
.\cite{shahi2018nepali}


\section{Problem Statement}\label{sec:probstm}
This project mainly focuses on classifying the unstructured Nepali news data into the different categories.This project will be very useful in scenario of Nepali News since there are not many good classifier present.

\section{Objective}\label{sec:obj}
To provide the best user experience in reading the Nepali news.

\section{Application}\label{sec:app}
Our project will be mainly the system to classify the unstructured the Nepali news text into the respective class of news category.

\section{Features}\label{sec:feat}
\begin{enumerate}[label=\Roman*.]
\item Classify the Nepali news articles into respective category.
\item Providing  the users the good experience of reading news.
\end{enumerate}

\section{Feasibility}\label{sec:fblty}
\subsection{Economic Feasibility}
In order to build this system we will crawl the many News portal which might lead to big size of data. We might need heavy computing resource to train the model and the expenses of computing resources. Other  than that the project is economically feasible.

\subsection{Technical Feasibility}
This system is the web application where the technology is used widely and internet facilities are spread all over the world so it is technically possible.

\subsection{Operational Feasibility}
While using this system, there should be smart devices with internet access. Smart devices and internet access are common these days. This project can be easily operated by the users, no any special operators required.

\section{System Requirements}\label{sec:sysreq}
\subsection{Software}
\begin{enumerate}
\item Windows OS

\end{enumerate}

\subsection{Hardware}
\begin{enumerate}
\item Pentium IV or higher processor
\item Internet connection
\end{enumerate}

\chapter{Literature Review}
Online news portal and other media on the internet now produced the large amount of text, which is mostly unstructured in nature. When an individual wants to access or share particular news, it should be organized or classified in the proper class. Automatic classification of text is to assign a label or class to given text using a computer program. It is more important when a large number of texts come from the different source and needs to be reported into specific labels for further processing as it happens mostly in case of news. At present, as like in all other parts of the world, the most of the news now flashed out from the online media in Nepal. The news in print media becomes almost outdated or already known before it reached the hand of reader next day. The online news portals classify their news into different categories such as "Political News", "Sports News", "Entertainment News" and so on. This task of manually labeling the news class becomes tedious when a large amount of news comes together from different sources. It is almost impossible to make this classification manually if some application tries to feed the trending news to the reader in real time. Hence it is necessary to develop an automatic tool that will be able to classify the Nepali news into relevant class. The technique developed to classify News text will be equally applicable to classify the other kind of Nepali text documents.


\chapter{Methodology}
\section{Fundamentals of Machine Learning}
Predictive modeling is a general concept where a model is built to make predictions. Machine learning algorithms are also predictive models that learn from a training data set to make predictions. Predictive models can be built for classification or regression problems. Regression models explore relationships between variables and make predictions about continuous variables. Classification involves predicting discrete class labels for data points. For example, predicting whether an android application is a malware or goodware during a malware detection process is a classification task, whereas estimating the threat level of a system is a regression task.\cite{pereira2019machine}.

\section{Creation of the initial dataset}
A collection of Nepali news will be  collected from various online Nepali News portals using web crawler.The news portal namely ratopati.com, setopati.com, onlinekhabar.com, and E-kantipur.com were used to gather text related to different news types.The category of News class that are found widely are namely Entertainment,health, literature, opinion, politics,and sports.
\section{Data Preprocessing}
The text preprocessing cleans the text data to make it ready to use in training and testing of the machine learning model.
Preprocessing is done to reduce the noise in the text that helps to improve the performance of the classifier and speed up the classification process, thus aiding in real time news classification. The main preprocessing techniques used are
given below.\\
\textbf{1.Tokenization:} Breakdowns the text into sentences and then words. Vertical bar, question mark, and fullstop are used to break down the sentences and while space and comma are used to break down the words.\cite{shahi2018nepali}\\
\textbf{2.​Stop word removal}: ​Stop words are high-frequency
words that has not much influence in the text are
removed to increase the performance of the
classification. The list of 255 stop-words were collected and removed
from the text.\\
\textbf{3.Word Stemming:} Stemming is used to reduce the
given word into its stem. Since the word stem reflects
the meaning of a particular word, we have segmented
the inflected word and derivational word into a stem
word so that the dimension of vocabulary reduced in
the significant manner.\cite{shahi2018nepali}

\section{Feature Vector Construction}
Feature Vector construction is the process of representing
the news into a vector form. To represent Nepali news in
vector form, the TF-IDF weighting value for each word in the
text is taken as a dimensional value in a vector.\cite{shahi2018nepali}

\section{Predictive Machine Learning Algorithm:}
Since this is multi class classification of problem here are two mainly algorithms related:

Multinomial Naïve Bayes
Naive Bayes is based on applying Bayes theorem (with the strong assumption that
every  feature  is  independent  of  the  others)  in  order  to  predict  the  category  of  a
given  sample.  It  is  a  probabilistic  classifier,  meaning  that  itwill  calculate  the
probability  of  each  category  using  Bayes  theorem,  and  the  category  with  the
highest probability will be output.

Support Vector Machine
Support Vector Machine is a supervised machine learning algorithm which is mostly used in classification problems. The classification is performed by finding the hyperplane that best differentiates the classes. When we have non-linear relationships in our data, we can modify the coordinate space with some kernel  transformations to capture the relationships





\section{Use Case Diagram}
\begin{figure}[tbh]
\centering
\includegraphics[scale=0.6]{usecase_news}
\caption{Use-case Diagram for Nepali News Classifier}
\label{UseCaseDiagram}
\end{figure}

\pagebreak




\pagebreak
\section{Software Development Model}
\begin{figure}[tbh]
\centering
\includegraphics[scale=0.8]{SwDevModel}
\caption{Software Development Life Cycle for Nepali News Classifier}
\label{SwDevModel}
\end{figure}
For the development of the project we are selecting iterative software development life Cycle model. In the Iterative model, iterative process starts with a simple implementation of a small set of the software requirements and iteratively enhances the evolving versions until the complete system is implemented and ready to be deployed. An iterative life cycle model does not attempt to start with a full specification of requirements. Instead, development begins by specifying and implementing just part of the software, which is then reviewed to identify further requirements. This process is then repeated, producing a new version of the software at the end of each iteration of the model.
Incremental development is done in steps from analysis design, implementation, testing/ verification. We are expecting to have 5-6 builds


\chapter{Epilogue}
\section{Work Schedule}
We have planned our project according to the requirements. Gantt chart of our project on the basis of which we intend to proceed our project and complete it accordingly.
\section{Gantt Chart}
\begin{figure}[tbh]
\centering
\includegraphics[scale=0.97]{GanttChart}
\caption{Gantt Chart of Project}
\label{GanttChart}
\end{figure}
\section{Work Completed}
We have completed building News scrapper.We also researched on Nepali text processing tool for NLP like stopwords,tokenizer,stemmer.
\section{Work Remaining}
The remaining works are designing user interface for the system, building database of the system and building overall machine learning classifier model of the system.
%Reference
\renewcommand\bibname{References} % Change heading to References
\bibliographystyle{IEEEtran} % to use IEEE Format for referencing
\addcontentsline{toc}{chapter}{References} % to add references in TOC
\bibliography{library} % specify the .bib file containing reference information 

\end{document}
