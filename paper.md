%%%%%%%% ICML 2019 EXAMPLE LATEX SUBMISSION FILE %%%%%%%%%%%%%%%%%

\documentclass{article}

% Recommended, but optional, packages for figures and better typesetting:
\usepackage{microtype}
\usepackage{graphicx}
\usepackage{subfigure}
\usepackage{booktabs} % for professional tables

% hyperref makes hyperlinks in the resulting PDF.
% If your build breaks (sometimes temporarily if a hyperlink spans a page)
% please comment out the following usepackage line and replace
% \usepackage{icml2019} with \usepackage[nohyperref]{icml2019} above.
\usepackage{hyperref}

% Attempt to make hyperref and algorithmic work together better:
\newcommand{\theHalgorithm}{\arabic{algorithm}}

% Use the following line for the initial blind version submitted for review:
%\usepackage{icml2019}

% If accepted, instead use the following line for the camera-ready submission:
\usepackage[accepted]{icml2019}

% The \icmltitle you define below is probably too long as a header.
% Therefore, a short form for the running title is supplied here:
\icmltitlerunning{Submission and Formatting Instructions for ICML 2019}

\begin{document}

\twocolumn[
\icmltitle{Analyzing bacterial markers for a non-intrusive Colorectal Cancer diagnosis}

% It is OKAY to include author information, even for blind
% submissions: the style file will automatically remove it for you
% unless you've provided the [accepted] option to the icml2019
% package.

% List of affiliations: The first argument should be a (short)
% identifier you will use later to specify author affiliations
% Academic affiliations should list Department, University, City, Region, Country
% Industry affiliations should list Company, City, Region, Country

% You can specify symbols, otherwise they are numbered in order.
% Ideally, you should not use this facility. Affiliations will be numbered
% in order of appearance and this is the preferred way.
\icmlsetsymbol{equal}{*}

\begin{icmlauthorlist}
\icmlauthor{Julian Kocher}{equal,to}
\icmlauthor{Ragavendra Kumar Ranjith Kumar}{equal,to}
\end{icmlauthorlist}

\icmlaffiliation{to}{Department of Computer Science, Courant Institute of Mathematical Sciences, New York University}

\icmlcorrespondingauthor{}{c.vvvvv@googol.com}
\icmlcorrespondingauthor{Eee Pppp}{ep@eden.co.uk}

% You may provide any keywords that you
% find helpful for describing your paper; these are used to populate
% the "keywords" metadata in the PDF but will not be shown in the document
\icmlkeywords{Machine Learning, colorectal cancer, ICML}

\vskip 0.3in 
]

% this must go after the closing bracket ] following \twocolumn[ ...

% This command actually creates the footnote in the first column
% listing the affiliations and the copyright notice.
% The command takes one argument, which is text to display at the start of the footnote.
% The \icmlEqualContribution command is standard text for equal contribution.
% Remove it (just {}) if you do not need this facility.

%\printAffiliationsAndNotice{}  % leave blank if no need to mention equal contribution
\printAffiliationsAndNotice{\icmlEqualContribution} % otherwise use the standard text.

\begin{abstract}
Current best techniques of detecting colorectal cancer require invasive methods, such as colonoscopy. However, analysis of gut bacteria across multi-national cohorts shows there are universal markers that could predict the presence of colorectal cancer.  Using this analysis, we apply various machine learning techniques to highlight significant bacterial interactions and better predict the probability of an individual having colorectal cancer given a sample of their gut microbiome.
\end{abstract}

\section{Introduction}
\label{introduction}

Colorectal cancer (CRC) is the second-leading cause of cancer-related deaths in the United States for both men and women combined. The cancer begins by forming a benign polyp and, if not removed, becomes life-threatening. Typically, a colonoscopy is performed to find and remove these protrusions from the intestinal wall. However, roughly one in ten polyps are unique in that they are highly cancerous and difficult to detect unless using additional techniques.  
The primary methods of detecting CRC are:
\begin{itemize}
\item fecal occult blood testing - a chemical test to detect the presence of blood in stool
\item flexible sigmoidoscopy - a visual inspection of the lower colon and rectum
\item a double contrast barium enema - an x-ray using radioactive liquid in the colon
\item colonoscopy - a visual inspection of the entire colon
\end{itemize}
Of these four major methods, three require some aspect of invasive techniques. Our goal is to explore various machine learning models to determine the best predictor of the presence of CRC using significant features we identify within the data set. We believe that the ability to predict the presence of CRC with a reasonable degree of accuracy is useful in determining the necessity of invasive CRC detection methods. It is also effective in detecting 'hidden' polyps mentioned above. It also has some application as an additional test performed while concurrent tests are preformed on an individual's gut microbia sample.

\subsection{Related Work}

The inspiration for our study stems from an analysis over data of a collection of gut microbiota across multi-national cohorts. The focus of this analysis was to determine if universal bacterial markers that allude to CRC exist. The analysis was unique in that most other work in the past have analyzed population samples differentiated by geographical region and thus produced results according to these specific regions and gut biomes. The related analysis determined the possibility and analysis of universal markers that exist across many populations to obtain a widespread collection of markers that could signify the possibility of CRC with some degree of accuracy. We, in attempting to verify and further this work, modelled some of our practices after their own.

Using simulation analysis, the related analysis identified bacterial species that showed differential abundance in CRC compared to the control samples. Of these 994 species, the analysis found 7 enriched species and 62 depleted species using the rank sum test. These were their features of interest regarding further machine learning application.

\textbf{MOVE THIS TO THE RESULTS SECTION}


This study employed the use of a Support Vector Machine (SVM) with several different basis functions, using the seven species correlated with enrichment associated with CRC as features. Predictions using a radial basis kernel resulted in an area under the curve (AUC) of 0.83 for the USA, 0.87 for Austria, 0.84 for China, and 0.82 for France/Germany. The model was also trained using 10-fold cross validation, resulting in an average AUC of 0.75 for separate cohorts, and 0.80 for the combined population. As we can see, their predictions from cohort to cohort is quite high (using the radial kernel), but average prediction across all populations is not as reliable. This is an area we hope to improve.


\subsection{Data}

The data set we used is publicly available on GitHub \textbf{reference}. It consists of 526 records with 1992 features across four cohorts. The cohorts represent samples taken from the USA, China, Austria, France and Germany.

The bacterial genomic records of our data set were collected through shotgun metagenomic sequencing of 9 separate data sets of 16S rRNA gene sequences (from prior studies)\textbf{reference}. 

\subsubsection{Preprocessing}

The data set consisted of 4 separate CSV files, with fields \texttt{SampleId, GroupedDiagnosis, age, BMI, gender, obese}, 1,986 fields for identified taxonomies and 1 field for unidentified taxonomies. As part of the preparation of the data set, we had to change alphabetic values to numeric values (such as obesity and the presence of CRC). We calculated the effect of missing values to ensure that our missing features were missing not at random (MNAR). To determine the potential importance of the missing data, we calculated the mean and standard deviation of the missing values across their respective cohorts and supplied a Gaussian distribution of values to determine their level of importance. We found that these features, roughly 50 in number, did not have any significant importance or correlation in regards to CRC and so we removed them. Among the remaining records, we applied a general scaling as the number of samples from cohort to cohort was not balanced due to slight differences in how sampling was performed. To further reduce the number of  unimportant features we determined which features exhibited zero or near zero variance and removed them as well. 

\begin{equation}
PUT \otimes ELASTIC \otimes NET \otimes HERE
\end{equation}

\subsection{Exploratory Data Analysis}

\subsubsection{Dimensional Reduction}

We applied dimensionality reduction to our data set. This is an essential step, especially concerning genetic data,  as high dimensionality may have data that is redundant or may decrease the accuracy of our models. We performed our reduction through elastic net regularization, which linearly combines the penalties of L1 and L2 regularization, due to that we know there is correlation between features. 

After dimensionality reduction, we found six species that had a positive correlation, and 11 with a negative correlation. Our machine learning models explored below used the six CRC enriched species found through this reduction.

\subsubsection{High Dimensionality Inference}

An important aspect of finding and using significant features is verifying their p-value in relation to CRC prediction. Via dimensionality reduction we found 6 enriched species, but we would also like to ensure that these species are indeed significant. To determine this, we used a method known as high dimensionality inference (HDI) \textbr{reference}. This method allows us to obtain p-values and confidence intervals from data sets where the number of records is much smaller than the number of features. Generally, estimators in high dimensions with some fixed design have an unidentifiable regression parameter. However, the design can be restricted in such a way to ensure the vector is identifiable. This is called the 'compatibility condition' of the design and guarantees identifiability and near optimal results with the Lasso estimator. Through these restrictions, we are able to obtain p-values over our high dimension data set.

\section{Methods}

\subsection{Logistic Regression}

We used the standard binomial generalized linear model (GLM) with a loss function in the form of \textbf{negative binomial log-likelihood}.
\begin{equation}
    equation2
\end{equation}

To prevent over-fitting, we used L1 Lasso regularization.


\subsection{Decision Trees}
Decision trees are simple machine learning models commonly used for regression or classification. In our case, we will be using trees for classification (predicting CRC). Essentially, each feature in our data set is a branch in a series of decisions. Branch splits within the tree are iterations of classification according to the feature considered. By doing so for a number (or all) features constructs a tree that arrives at some binomial decision.

\subsubsection{Gradient Boosted Trees}
Gradient boosted trees are prediction models formed of an ensemble of simple decision trees. This method allows us to reduce the bias of our model at the expense of variance. This approach generates new models that predict the error of prior models, and then combines them together. Models are generalized through optimization using a differentiable loss function until the overall model cannot be improved any further. This results in increased accuracy over a simple decision tree, but is subject to over-fitting. We used the XGBoost implementation of gradient boosted trees for its high speed, low memory use and high accuracy.

\subsubsection{Random Forest}
A random decision forest is a prediction model that can be used for regression and classification. Their most powerful feature over standard decision trees is their ability to prevent over-fitting due to their random construction. A key element of random forests is the addition of bootstrap aggregating (bagging), where each tree construction uses a training data that is a subset of the full training set. These randomly constructed trees are combined to create the random forest. This method of bagging allows us to decrease the variance compared to a standard decision tree without increasing bias by using different training sets to de-correlate one tree from another.

\subsection{Artificial Neural Network}
Artificial neural networks is a popular and powerful machine learning algorithm that is a collection of nodes which model the behavior of organic neurons. Given a number of input nodes, a series of layers (of variable number) are formed where each preceding node connects to each node in the following layer. Each connection has an associated weight that is adjusted during the learning process. The final layer is the output layer.
We implemented a standard neural network model with two hidden layers and a binary sigmoid activation function.

\textbf{reference}

\section{Results and Discussion}

In relevant scenarios, we are interested in our results both from the data set of all features as well as the data set consisting of our six CRC enriched species.

\subsection{High Dimensionality Inference}

We performed High Dimensionality Inference (HDI) to obtain p-values for our 1991 features. With HDI, we used a desparsified Lasso method with a weighted squared error \textbf{reference}.
We chose this method to obtain our p-values because the desparsified Lasso method does not make any assumption, other than sparsity on the regression coefficient. The inverse covariance matrix of our data indicates that our data set is indeed sparse, which is ideal for this method. Additionally, this method provides uniform convergence over all sparse regression vectors. Using this method allowed us to obtain both p-values and an honest confidence interval. However, it is quite computationally demanding.

\textbr{PUT HDI RESULTS HERE}

\subsection{Logistic Regression}

Through 5-fold cross-validation, in fig. 3 we see that the
optimal C value for both feature-sets occurs around 0.01.The
SAG algorithm automatically calculates the learning rate
value, so one was not needed to be selected prior [10].
With a chosen C value of 0.01, the limited feature-set model
performed with an 63.9% accuracy on the test set and the full
feature-set model performed with a 81.5% accuracy, both of
which are very similar to the validation sets. From the confusion matrix (which is not posted due to space constraints),
the main sources of error for the both feature-set models are
activities like vacuum cleaning and ironing, Nordic walking
and walking, or lying and sitting. As expected, these activities
have similar body movements, so from the point of view of a
sensor reading, these may be hard to distinguish for a linear
classifier.


The paper title should be set in 14~point bold type and centered
between two horizontal rules that are 1~point thick, with 1.0~inch
between the top rule and the top edge of the page. Capitalize the
first letter of content words and put the rest of the title in lower
case.

\subsection{Author Information for Submission}
\label{author info}

ICML uses double-blind review, so author information must not appear. If
you are using \LaTeX\/ and the \texttt{icml2019.sty} file, use
\verb+\icmlauthor{...}+ to specify authors and \verb+\icmlaffiliation{...}+ to specify affiliations. (Read the TeX code used to produce this document for an example usage.) The author information
will not be printed unless \texttt{accepted} is passed as an argument to the
style file.
Submissions that include the author information will not
be reviewed.

\subsubsection{Self-Citations}

If you are citing published papers for which you are an author, refer
to yourself in the third person. In particular, do not use phrases
that reveal your identity (e.g., ``in previous work \cite{langley00}, we
have shown \ldots'').

Do not anonymize citations in the reference section. The only exception are manuscripts that are
not yet published (e.g., under submission). If you choose to refer to
such unpublished manuscripts \cite{anonymous}, anonymized copies have
to be submitted
as Supplementary Material via CMT\@. However, keep in mind that an ICML
paper should be self contained and should contain sufficient detail
for the reviewers to evaluate the work. In particular, reviewers are
not required to look at the Supplementary Material when writing their
review.

\subsubsection{Camera-Ready Author Information}
\label{final author}

If a paper is accepted, a final camera-ready copy must be prepared.
%
For camera-ready papers, author information should start 0.3~inches below the
bottom rule surrounding the title. The authors' names should appear in 10~point
bold type, in a row, separated by white space, and centered. Author names should
not be broken across lines. Unbolded superscripted numbers, starting 1, should
be used to refer to affiliations.

Affiliations should be numbered in the order of appearance. A single footnote
block of text should be used to list all the affiliations. (Academic
affiliations should list Department, University, City, State/Region, Country.
Similarly for industrial affiliations.)

Each distinct affiliations should be listed once. If an author has multiple
affiliations, multiple superscripts should be placed after the name, separated
by thin spaces. If the authors would like to highlight equal contribution by
multiple first authors, those authors should have an asterisk placed after their
name in superscript, and the term ``\textsuperscript{*}Equal contribution"
should be placed in the footnote block ahead of the list of affiliations. A
list of corresponding authors and their emails (in the format Full Name
\textless{}email@domain.com\textgreater{}) can follow the list of affiliations.
Ideally only one or two names should be listed.

A sample file with author names is included in the ICML2019 style file
package. Turn on the \texttt{[accepted]} option to the stylefile to
see the names rendered. All of the guidelines above are implemented
by the \LaTeX\ style file.

\subsection{Abstract}

The paper abstract should begin in the left column, 0.4~inches below the final
address. The heading `Abstract' should be centered, bold, and in 11~point type.
The abstract body should use 10~point type, with a vertical spacing of
11~points, and should be indented 0.25~inches more than normal on left-hand and
right-hand margins. Insert 0.4~inches of blank space after the body. Keep your
abstract brief and self-contained, limiting it to one paragraph and roughly 4--6
sentences. Gross violations will require correction at the camera-ready phase.

\subsection{Partitioning the Text}

You should organize your paper into sections and paragraphs to help
readers place a structure on the material and understand its
contributions.

\subsubsection{Sections and Subsections}

Section headings should be numbered, flush left, and set in 11~pt bold
type with the content words capitalized. Leave 0.25~inches of space
before the heading and 0.15~inches after the heading.

Similarly, subsection headings should be numbered, flush left, and set
in 10~pt bold type with the content words capitalized. Leave
0.2~inches of space before the heading and 0.13~inches afterward.

Finally, subsubsection headings should be numbered, flush left, and
set in 10~pt small caps with the content words capitalized. Leave
0.18~inches of space before the heading and 0.1~inches after the
heading.

Please use no more than three levels of headings.

\subsubsection{Paragraphs and Footnotes}

Within each section or subsection, you should further partition the
paper into paragraphs. Do not indent the first line of a given
paragraph, but insert a blank line between succeeding ones.

You can use footnotes\footnote{Footnotes
should be complete sentences.} to provide readers with additional
information about a topic without interrupting the flow of the paper.
Indicate footnotes with a number in the text where the point is most
relevant. Place the footnote in 9~point type at the bottom of the
column in which it appears. Precede the first footnote in a column
with a horizontal rule of 0.8~inches.\footnote{Multiple footnotes can
appear in each column, in the same order as they appear in the text,
but spread them across columns and pages if possible.}

\begin{figure}[ht]
\vskip 0.2in
\begin{center}
\centerline{\includegraphics[width=\columnwidth]{icml_numpapers}}
\caption{Historical locations and number of accepted papers for International
Machine Learning Conferences (ICML 1993 -- ICML 2008) and International
Workshops on Machine Learning (ML 1988 -- ML 1992). At the time this figure was
produced, the number of accepted papers for ICML 2008 was unknown and instead
estimated.}
\label{icml-historical}
\end{center}
\vskip -0.2in
\end{figure}

\subsection{Figures}

You may want to include figures in the paper to illustrate
your approach and results. Such artwork should be centered,
legible, and separated from the text. Lines should be dark and at
least 0.5~points thick for purposes of reproduction, and text should
not appear on a gray background.

Label all distinct components of each figure. If the figure takes the
form of a graph, then give a name for each axis and include a legend
that briefly describes each curve. Do not include a title inside the
figure; instead, the caption should serve this function.

Number figures sequentially, placing the figure number and caption
\emph{after} the graphics, with at least 0.1~inches of space before
the caption and 0.1~inches after it, as in
Figure~\ref{icml-historical}. The figure caption should be set in
9~point type and centered unless it runs two or more lines, in which
case it should be flush left. You may float figures to the top or
bottom of a column, and you may set wide figures across both columns
(use the environment \texttt{figure*} in \LaTeX). Always place
two-column figures at the top or bottom of the page.

\subsection{Algorithms}

If you are using \LaTeX, please use the ``algorithm'' and ``algorithmic''
environments to format pseudocode. These require
the corresponding stylefiles, algorithm.sty and
algorithmic.sty, which are supplied with this package.
Algorithm~\ref{alg:example} shows an example.

\begin{algorithm}[tb]
   \caption{Bubble Sort}
   \label{alg:example}
\begin{algorithmic}
   \STATE {\bfseries Input:} data $x_i$, size $m$
   \REPEAT
   \STATE Initialize $noChange = true$.
   \FOR{$i=1$ {\bfseries to} $m-1$}
   \IF{$x_i > x_{i+1}$}
   \STATE Swap $x_i$ and $x_{i+1}$
   \STATE $noChange = false$
   \ENDIF
   \ENDFOR
   \UNTIL{$noChange$ is $true$}
\end{algorithmic}
\end{algorithm}

\subsection{Tables}

You may also want to include tables that summarize material. Like
figures, these should be centered, legible, and numbered consecutively.
However, place the title \emph{above} the table with at least
0.1~inches of space before the title and the same after it, as in
Table~\ref{sample-table}. The table title should be set in 9~point
type and centered unless it runs two or more lines, in which case it
should be flush left.

% Note use of \abovespace and \belowspace to get reasonable spacing
% above and below tabular lines.

\begin{table}[t]
\caption{Classification accuracies for naive Bayes and flexible
Bayes on various data sets.}
\label{sample-table}
\vskip 0.15in
\begin{center}
\begin{small}
\begin{sc}
\begin{tabular}{lcccr}
\toprule
Data set & Naive & Flexible & Better? \\
\midrule
Breast    & 95.9$\pm$ 0.2& 96.7$\pm$ 0.2& $\surd$ \\
Cleveland & 83.3$\pm$ 0.6& 80.0$\pm$ 0.6& $\times$\\
Glass2    & 61.9$\pm$ 1.4& 83.8$\pm$ 0.7& $\surd$ \\
Credit    & 74.8$\pm$ 0.5& 78.3$\pm$ 0.6&         \\
Horse     & 73.3$\pm$ 0.9& 69.7$\pm$ 1.0& $\times$\\
Meta      & 67.1$\pm$ 0.6& 76.5$\pm$ 0.5& $\surd$ \\
Pima      & 75.1$\pm$ 0.6& 73.9$\pm$ 0.5&         \\
Vehicle   & 44.9$\pm$ 0.6& 61.5$\pm$ 0.4& $\surd$ \\
\bottomrule
\end{tabular}
\end{sc}
\end{small}
\end{center}
\vskip -0.1in
\end{table}

Tables contain textual material, whereas figures contain graphical material.
Specify the contents of each row and column in the table's topmost
row. Again, you may float tables to a column's top or bottom, and set
wide tables across both columns. Place two-column tables at the
top or bottom of the page.

\subsection{Citations and References}

Please use APA reference format regardless of your formatter
or word processor. If you rely on the \LaTeX\/ bibliographic
facility, use \texttt{natbib.sty} and \texttt{icml2019.bst}
included in the style-file package to obtain this format.

Citations within the text should include the authors' last names and
year. If the authors' names are included in the sentence, place only
the year in parentheses, for example when referencing Arthur Samuel's
pioneering work \yrcite{Samuel59}. Otherwise place the entire
reference in parentheses with the authors and year separated by a
comma \cite{Samuel59}. List multiple references separated by
semicolons \cite{kearns89,Samuel59,mitchell80}. Use the `et~al.'
construct only for citations with three or more authors or after
listing all authors to a publication in an earlier reference \cite{MachineLearningI}.

Authors should cite their own work in the third person
in the initial version of their paper submitted for blind review.
Please refer to Section~\ref{author info} for detailed instructions on how to
cite your own papers.

Use an unnumbered first-level section heading for the references, and use a
hanging indent style, with the first line of the reference flush against the
left margin and subsequent lines indented by 10 points. The references at the
end of this document give examples for journal articles \cite{Samuel59},
conference publications \cite{langley00}, book chapters \cite{Newell81}, books
\cite{DudaHart2nd}, edited volumes \cite{MachineLearningI}, technical reports
\cite{mitchell80}, and dissertations \cite{kearns89}.

Alphabetize references by the surnames of the first authors, with
single author entries preceding multiple author entries. Order
references for the same authors by year of publication, with the
earliest first. Make sure that each reference includes all relevant
information (e.g., page numbers).

Please put some effort into making references complete, presentable, and
consistent. If using bibtex, please protect capital letters of names and
abbreviations in titles, for example, use \{B\}ayesian or \{L\}ipschitz
in your .bib file.

\subsection{Software and Data}

We strongly encourage the publication of software and data with the
camera-ready version of the paper whenever appropriate. This can be
done by including a URL in the camera-ready copy. However, do not
include URLs that reveal your institution or identity in your
submission for review. Instead, provide an anonymous URL or upload
the material as ``Supplementary Material'' into the CMT reviewing
system. Note that reviewers are not required to look at this material
when writing their review.

% Acknowledgements should only appear in the accepted version.
\section*{Acknowledgements}

\textbf{Do not} include acknowledgements in the initial version of
the paper submitted for blind review.

If a paper is accepted, the final camera-ready version can (and
probably should) include acknowledgements. In this case, please
place such acknowledgements in an unnumbered section at the
end of the paper. Typically, this will include thanks to reviewers
who gave useful comments, to colleagues who contributed to the ideas,
and to funding agencies and corporate sponsors that provided financial
support.


% In the unusual situation where you want a paper to appear in the
% references without citing it in the main text, use \nocite
\nocite{langley00}

\bibliography{example_paper}
\bibliographystyle{icml2019}

\end{document}
