---
title: "Recursive probabilistic analysis: A robust and practical method to study research articles in computer science"
journal: "English for Special Purposes"
author:
- name: Jingxuan Zhang\corref{cor1}
  email: jingxuan.zhang@tongji.edu.cn
  group: cs
  address: "Department of Computer Science, Tongji University"
- name: Yang Qian
  email: anneqiantj@126.com
  group: en
  address: "Department of College English, Tongji University"
biblio-files: references
options: "review, 3p, authoryear"
abstract:
  "This article proposes a novel method to perform the genre-based analysis in an efficient way. This method addresses two key challenges in the genre-based analysis of the research articles: (1) The incorrect genre labels conduct the inaccurate analysis result; and (2) the subjective analysis leads the unconfirmed conclusion. The key insight of this method is to perform a recursive probabilistic analysis based on traditional Markov model and association rules learning. In this new method, the ESP researchers can recheck the data collection and get accurate objective result efficiently. This article designs several experiments to verify the effectiveness of the proposed method. The result of the evaluation shows this method is robust and practical."
keywords: "ESP, genre analysis, probabilistic model."
---

<!-- TODO: Find a better title for this article. -->

# Introduction

The researchers would like to understand "how to write a good research article" so that their valuable work can be accepted by the society. Actually, the more general problem, which is well known as English for Specific Purposes (ESP), have been well studied in the past decades.
To solve such a general problem, the previous researchers \citep[e.g.][]{swales1990genre, hyland2004genre} proposed the concept "genre" to formulate the writing structure of the articles in ESP. Genre-based approach, which is also called genre analysis, has been the fundamental approach in ESP since 1990.

Since there are an increasing number of computer science researchers writing in a second language, it is an essential topic to answer the above question to them. Although there are a considerable number of related studies in many different domains (e.g. management, laws, medical science, etc.), computer science research articles has not gotten enough attention yet. \citet{Anthony1999} played a role of pioneer in software engineering, which is a specific domain of computer science. The more comprehensive study in computer science, however, is still a blank.

Another crucial problem is how to improve the current research method in ESP. CARS (create a research space) model which was proposed by \citet{swales1990genre} has become the de facto standard theoretical model and been applied by recent studies in ESP. The key idea of CARS model is "move and step analysis", which is a technique to organize the continuous text of the article into several groups by the communicative purposes. The group with the same communicative purpose is labeled as a move (for the bigger context) or a step (for the smaller one). CARS model and its move-step analysis are widely accepted in the research of ESP. A bunch of studies have practised the methods based on the move-step analysis in different research domains: \citet{Anthony1999} studied the accuracy of the CARS model for software engineering articles; \citet{Lim2006} performed a qualitative study for method sections of management research articles; \citet{Li2009} did a comprehensive genre analysis for amount of medical research articles published from 1985 to 2004; \citet{Loi2010} compared the research article introductions in Chinese and English by performing a genre-based study.

<!-- \info{CARS model and move-step theory is widely accepted. Literature review here.} -->

<!-- Literature review: \citep[e.g.][]{swales1990genre, Anthony1999, Lim2006, Loi2010} -->

However, these CARS model based studies are still very primary. The conclusions of these studies are always derived from the subjective findings of the raw data collection and some simple statistics on it. It is hard to avoid conducting wrong results because of the inaccurate data collection. Since the effectiveness of data mining technique has been verified in widespread areas, an intuited idea is to apply the data mining tools to model and analyze the research articles in computer science robustly.

<!-- \info{The limitation of the previous studies.} -->

To address these limitations and get better understanding of how to write a qualified computer science research article, we have to face two major challenges:

- The CARS model based study requires to manually analyze the moves and steps of the related sections for each research article. A reliable study result is built on the foundation of the accurate labeling of moves and steps, which is a subjective process and easy to make some mistakes.

- The reviewers of the research articles often focus on the contents of them rather than their writing. It does hardly occur that a reviewer indicates a writing issue or give a mark of the writing grade level.

<!-- TODO: Need to explain solutions to crossing the challenges above briefly. -->

This paper targets a more practical approach to analyze and understand the research articles in computer science. Our main contributions are: (1) Apply n-grams probability transition model and association rule model to the analysis of research articles; (2) Perform a genre-based study of research article introductions in computer science to understand the usage of the sentence tense of voice well; and (3) Provide a practical method and the toolkits to build your own research articles analysis database and validate the move-step labels automatically.

To demonstrate the effectiveness of this approach, firstly, we run our analysis toolkit to proceed the probability transition and association rule analysis in a proved correct move-step dataset, which has been checked by multiple experts. Then we perform the validation toolkit in the homework of students and show the estimated error rate of each move-step label. Finally, we double check the move-step labels with the higher error rate and report the percentage of false-positive error and true-negative error. When the threshold is set to 0.1, the frequency of false-positive error is in an accepted range.

# Research Design

This paper develops a robust and practical method with both qualitative and quantitative analysis. To verify the effectiveness of our method and better understand the writing of research article introductions in computer science, we design the following experiment. As expected, the result of the experiment should explain the following features of our method:

Robustness.

: The statistical analysis of the experiment result should still be valuable and accepted although mistakes appear in the moves and steps labeled by volunteers. In other words, the analysis can tolerate the incorrect genre labels in a given threshold.

Practicality.

: The evaluation of the analysis should be able to indicate the potential error of the genre labels. Volunteers can hence double check labels purposefully and reduce their mistakes.

## Data collection

Computer science, which is very different from the traditional experiment-based natural science (e.g. biotechnology, medicine, physics, etc.) in the academic culture, prefers the practical implementation and the social communication. So there are two characters of research articles in computer science:

- The computer science research articles with the high quality are usually published in some popular conferences rather than the academic journals.

- The purposes of research articles in computer science are usually not to report findings in some experiments, but to explain the practice of some theories or engineering systems. So the structure of these research articles usually do not follow the IMRD framework.

Based on the insight above, considering the specific research objective, a total of 25 articles were selected from 10 Class A conference proceedings. These conference proceedings are selected from CCF recommended conferences list, which is reviewed and provided by well-known experts in all fields of computer science.

## Analysis Coding

### Genre coding

\citet{swales1990genre} proposed the original CARS model (see table \ref{tbl:swales-model}) for the standard IMRD research articles. However, most of research articles in computer science do not follow the standard IMRD framework.

------------------------------------------------------------------------------
Rhetorical move                  Constituent step
-------------------------------- ---------------------------------------------
Move 1: Establishing a Territory Step 1: Claiming centrality (and/or)\
                                 Step 2: Making topic generalizations (and/or)\
                                 Step 3: Reviewing items of previous research

Move 2: Establishing a Niche     Step 1:\
                                 (a) Counter-claiming (or)\
                                 (b) Indicating a gap (or)\
                                 (c) Question-raising (or)\
                                 (d) Continuing a tradition

Move 3: Occupying the Niche      Step 1:\
                                 (a) Outlining purposes (or)\
                                 (b) Announcing present research\
                                 Step 2: Announcing principle findings\
                                 Step 3: Indicating article structure
------------------------------------------------------------------------------

: Swales' CARS model. \label{tbl:swales-model}

We modified CARS model (see table \ref{tbl:modified-model}) to satisfy the genre analysis of science research article introductions in computer science:

-----------------------------------------------------------------------------------------
Rhetorical move                  Constituent step
-------------------------------- --------------------------------------------------------
Move 1: Establishing a Territory Step 1: General knowledge in the field\
                                 Step 2: Establish importance of the field\
                                 Step 3: Topic generalizations of increasing specificity\
                                 Step 4: Review of previous studies (contributions)

Move 2: Create a Space           Step 1:\
                                 (a) Indicating gaps (or)\
                                 (b) Counter-claims (or)\
                                 (c) Adding to what is known (or)\
                                 (d) Raising questions (or)\
                                 (e) Suggest value of the issue\
                                 Step 2: Present positive justification

Move 3: Occupying the Space      Step 1:\
                                 (a) directly announce research purpose (or)\
                                 (b) Describe briefly research (or)\
                                 (c) Present research questions (or)\
                                 (d) Present research hypothesis\
                                 Step 2: Summarize methods\
                                 Step 3:\
                                 (a): Clarify terms\
                                 (b): State frameworks / theoretical positions\
                                 Step 4: Announce principle results\
                                 Step 5: Claim research value\
                                 Step 6: Suggest further research\
                                 Step 7: Indicate RA structure
-----------------------------------------------------------------------------------------

: The modified CARS model used in this article. \label{tbl:modified-model}

### Article coding

Each article in the present study is coded by its research objective (e.g. experimental article, theoretical article, literature review, etc.) and the native writing language (L1/L2 writing). Since the first author is usually the responding author of the research article, it should be reasonable that we assume the first author wrote the most part of the article and the nationality of the first author determines the native writing language of this article.

To simplify the description, the present article uses the symbols in table \ref{tbl:article-coding} to encode the type of each article.

-------------------------------------------------
 Code   Description
------  -----------------------------------------
 E1     Experimental article written by L1 writer

 E2     Experimental article written by L2 writer

 T1     Theoretical article written by L1 writer

 T2     Theoretical article written by L2 writer

 R1     Literature review written by L1 writer

 R2     Literature review written by L2 writer
-------------------------------------------------

: The encode of article types used in this article. \label{tbl:article-coding}

## Analysis models

### Qualitative analysis: CARS model

This article performs the fundamental analysis from the statistics of sentences tense and voice based on the modified CARS model (explained in table \ref{tbl:modified-model}). For simplicity, we analyze introductions of research articles in the data collection claimed in section \ref{data-collection} sentence by sentence with three variables: tense, voice, genre coding (moves/steps) and article coding. The basic research objective is to study and understand the relationship among these variables.

### Quantitative analysis: Markov model and association rules

The basic analysis model described above can only give writers an intuition of understanding the relationship among different variables. This article indicates there are two limitations at lease in this analysis model:

Qualitative and subjective conclusions.

: Follow the basic analysis model, researchers can only get some qualitative and subjective conclusions (i.e. the active voice is used more in experimental articles than in literature reviews), which many previous studies did but we do not want.

Lack of chronological relationship.

: The basic analysis model counts the variables sentence by sentence. The statistics is missing the chronological relation of sentences. It will loss many useful information.

This paper introduces two probabilistic analysis model to mine the deeper knowledge of the CARS model.

First, this paper use Markov model to show the transition probability between the previous and next move/step. Considering each academic writer is a *Turing Machine*, the writer should write research papers by following a state transfer function intuitively. The result of Markov model analysis is a probability transition matrix, whose rows and columns stand by different moves/steps. The value of each element in this matrix estimates the probability when the move/step of current sentence is the row label of the element and next sentence moves to the column label of the element.

Secondly, we introduce association rules model to mine more general relationship among the variables. Association rules model is well-known because of association rule learning, which is proposed by \citet{Agrawal1993} to achieve data mining in large databases. We apply association rule learning into the genre analysis. The association rules in our result can infer the appearance of moves/steps from the existing moves/steps.
<!-- TODO: Take an example. -->

# Method

Based on the coding and model design of analysis explained in section \ref{research-design}, the present article performs a recursive experiment to evaluate the new analysis method. Figure \ref{fig:workflow} shows the simplified workflow of our method.

\begin{figure}[!htp]
\centering
\begin{tikzpicture}[node distance = 2cm, auto]
    % Place nodes
    \node [process] (init) {initialize analysis};
    \node [process, below of=init] (analysis) {probabilistic analysis};
    \node [process, below of=analysis] (evaluate) {evaluate \\ potential error};
    \node [process, left of=evaluate, node distance=4cm] (update) {review and validate};
    \node [condition, below of=evaluate] (decide) {is there the potential error?};
    \node [process, below of=decide, node distance=2.5cm] (stop) {report and stop};
    % Draw edges
    \path [line] (init) -- (analysis);
    \path [line] (analysis) -- (evaluate);
    \path [line] (evaluate) -- (decide);
    \path [line] (decide) -| node [near start] {yes} (update);
    \path [line] (update) |- (analysis);
    \path [line] (decide) -- node {no}(stop);
\end{tikzpicture}
\caption{Basic workflow of the analysis method proposed by this article.} \label{fig:workflow}
\end{figure}

## Initial analysis

At the beginning of the analysis, we prepare a small-scale initial dataset of research article introductions with the complete move/step labels, which are assumed somehow correct. Considering the number of research articles in this initial dataset can be very small, we can fully review the move/step labels of each article in accepted time. Hence we can somehow guarantee the correctness of the labels.

Since the initial dataset can be guaranteed, we run the initial analysis in this dataset and get the initial result of the probability transition matrix and association rules. Although the labels should be correct, we still cannot ensure the statistical analysis result is accepted because of the small scale of the dataset. However, we can consider this initial result as an iterative origin to add more labeled articles into the dataset.

## Probabilistic analysis for correctness

The next step of our method is to enlarge the accepted dataset. First, we select a labeled article from the unaccepted dataset to decide whether it can be added into the accepted dataset. Secondly, we check the move/step labels of this article sentence by sentence to estimate the Bayesian probability of the move/step transition. If the estimated Bayesian probability is lower than a given threshold, we should suspect the correctness of the label and recheck the corresponding sentences.

## Review and validation

From the process above, each move/step transition in the selected article will be validated by the probability transition matrix. In this way, we can immediately find which transition conducts a potential error. So we can locate the possible incorrect move/step label more accurately. In principle, we only need to review the label of the current sentence reported by the transition matrix and its following sentence. So the workload of the review should be reduced essentially from fully reviewing.

The reported potential error only indicates it is possible to make a mistake in the current move/step label. The result of the recheck can also show there is no mistake. Once the manual recheck has been done, the new move/step label in the current position should be thought accepted.

## Update the result

After all sentence labels of the selected article has been validated, this labeled article should be accepted. We add this article into the accepted database, and then perform the probabilistic analysis again. As the result, we will get an updated probability transition matrix and a larger accepted dataset.

# Results

For simplicity, we only show the result of experimental articles to demonstrate the effectiveness of our method in this section. The complete result and the analysis can be found in section \ref{appendix-a}.

## Initial probabilistic analysis

We select the 5 E1 articles and 6 E2 articles (see the definition in section \ref{article-coding}) as the initial accepted dataset to analyze the genre of their introductions.

Table \ref{tbl:init-matrix-e1} shows the probability transition matrix of moves/steps in the initial E1 introductions set. There are two different "\$" symbols, which stand by different things in this table. The "\$" symbol in the row label means the beginning move. i.e. The value of the element in "\$" row and "1.1" column is 0.5, which means there are half of beginning sentences labeled as "Step 1.1". The "\$" symbol in the column label stands by the end move. i.e. The value of the element in "3.7" row and "\$" column is 1, which means all the sentences with the label "Step 3.7" do not accept any other move/step as the following sentence label.

Because the scale of the initial dataset is too small, it is very possible that findings based on the statistics of this result matrix are inaccurate. So we can only perform some rough analysis.

|       |   1.1  |   1.2  |   1.3  |   1.4  |   2.1  |   2.2  |   3.1  |   3.2  |   3.3  |   3.4  |   3.5  |   3.6  |   3.7  |     $ |
| ----- | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ----- |
|    $  |   0.50 |   0.33 |   0.17 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |    0.0 |   0.00 |  0.00 |
|  1.1  |   0.00 |   0.25 |   0.00 |   0.12 |   0.50 |   0.00 |   0.12 |   0.00 |   0.00 |   0.00 |   0.00 |    0.0 |   0.00 |  0.00 |
|  1.2  |   0.33 |   0.00 |   0.17 |   0.17 |   0.17 |   0.17 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |    0.0 |   0.00 |  0.00 |
|  1.3  |   0.33 |   0.33 |   0.00 |   0.00 |   0.33 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |    0.0 |   0.00 |  0.00 |
|  1.4  |   0.50 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   0.50 |   0.00 |   0.00 |   0.00 |   0.00 |    0.0 |   0.00 |  0.00 |
|  2.1  |   0.12 |   0.12 |   0.12 |   0.00 |   0.00 |   0.00 |   0.25 |   0.00 |   0.12 |   0.00 |   0.25 |    0.0 |   0.00 |  0.00 |
|  2.2  |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   1.00 |   0.00 |   0.00 |   0.00 |   0.00 |    0.0 |   0.00 |  0.00 |
|  3.1  |   0.00 |   0.00 |   0.00 |   0.00 |   0.12 |   0.00 |   0.00 |   0.38 |   0.00 |   0.12 |   0.12 |    0.0 |   0.12 |  0.12 |
|  3.2  |   0.00 |   0.00 |   0.00 |   0.00 |   0.33 |   0.00 |   0.67 |   0.00 |   0.00 |   0.00 |   0.00 |    0.0 |   0.00 |  0.00 |
|  3.3  |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   1.00 |    0.0 |   0.00 |  0.00 |
|  3.4  |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   1.00 |    0.0 |   0.00 |  0.00 |
|  3.5  |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   0.40 |   0.00 |   0.00 |   0.00 |   0.00 |    0.2 |   0.40 |  0.00 |
|  3.6  |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |    0.0 |   0.00 |  1.00 |
|  3.7  |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |    0.0 |   0.00 |  1.00 |

: Probability transition matrix of E1 article introductions. \label{tbl:init-matrix-e1}

Table \ref{tbl:init-matrix-e2} shows the similar result but for the initial E2 dataset. We can, of course, also perform the similar analysis as we did for table \ref{tbl:init-matrix-e1}. However, the more valuable result can be extracted by comparing the data of these two tables.

Intuitively, table \ref{tbl:init-matrix-e1} shows the writing style of authors writing in their native language. Similarly, table \ref{tbl:init-matrix-e2} shows the writing style of those authors whose native language is not English. A first rough impression on the two transition matrices is that the popular beginning steps are different for L1 writers and L2 writers. According to these small samples, all the beginning transitions point to "Move 1" in introductions written by L1 writers, but the introductions written by L2 writers can begin with "Move 2". L1 writers seem to strictly follow the writing style that "Move 1" should always be the beginning of an introduction. However, L2 writers sometimes do not follow such a writing style.

|       |   1.1  |   1.2  |   1.3  |   1.4  |   2.1  |   2.2  |   3.1  |   3.2  |   3.3  |   3.4  |   3.5  |   3.6  |   3.7  |     $ |
| ----- | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ----- |
|    $  |   0.29 |   0.57 |   0.00 |   0.00 |   0.14 |      0 |   0.00 |   0.00 |   0.00 |   0.00 |    0.0 |      0 |   0.00 |   0.0 |
|  1.1  |   0.00 |   0.00 |   0.80 |   0.00 |   0.20 |      0 |   0.00 |   0.00 |   0.00 |   0.00 |    0.0 |      0 |   0.00 |   0.0 |
|  1.2  |   0.25 |   0.00 |   0.25 |   0.00 |   0.50 |      0 |   0.00 |   0.00 |   0.00 |   0.00 |    0.0 |      0 |   0.00 |   0.0 |
|  1.3  |   0.33 |   0.00 |   0.00 |   0.33 |   0.33 |      0 |   0.00 |   0.00 |   0.00 |   0.00 |    0.0 |      0 |   0.00 |   0.0 |
|  1.4  |   0.00 |   0.00 |   0.00 |   0.00 |   0.60 |      0 |   0.40 |   0.00 |   0.00 |   0.00 |    0.0 |      0 |   0.00 |   0.0 |
|  2.1  |   0.00 |   0.00 |   0.10 |   0.30 |   0.00 |      0 |   0.30 |   0.00 |   0.10 |   0.00 |    0.1 |      0 |   0.00 |   0.1 |
|  2.2  |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |      0 |   0.00 |   0.00 |   0.00 |   0.00 |    0.0 |      0 |   0.00 |   0.0 |
|  3.1  |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |      0 |   0.00 |   0.38 |   0.12 |   0.12 |    0.0 |      0 |   0.38 |   0.0 |
|  3.2  |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |      0 |   0.25 |   0.00 |   0.00 |   0.75 |    0.0 |      0 |   0.00 |   0.0 |
|  3.3  |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |      0 |   0.50 |   0.00 |   0.00 |   0.50 |    0.0 |      0 |   0.00 |   0.0 |
|  3.4  |   0.00 |   0.00 |   0.00 |   0.00 |   0.20 |      0 |   0.20 |   0.20 |   0.00 |   0.00 |    0.4 |      0 |   0.00 |   0.0 |
|  3.5  |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |      0 |   0.00 |   0.00 |   0.00 |   0.00 |    0.0 |      0 |   0.00 |   1.0 |
|  3.6  |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |      0 |   0.00 |   0.00 |   0.00 |   0.00 |    0.0 |      0 |   0.00 |   0.0 |
|  3.7  |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |      0 |   0.00 |   0.00 |   0.00 |   0.00 |    0.0 |      0 |   0.00 |   1.0 |

: Probability transition matrix of E2 article introductions. \label{tbl:init-matrix-e2}

## Final probabilistic analysis

After initiating the accepted dataset, we start to enlarge it and update its probability transition matrix. In this section, we only demonstrate the process of enlarging and updating in the E2 dataset.

--------------------------------------
 Paragraph-Sentence Range   Move/Step
-------------------------- -----------
 1-1 to 1-3                 Step 1.1
 
 1-4                        Step 1.3
 
 2-1 to 2-2                 Step 1.2
 
 2-3 to 2-5                 Step 1.1
 
 2-6                        Step 1.3
 
 3-1 to 3-2                 Step 1.1
 
 3-3                        Step 2.1
 
 3-4 to 3.6                 Step 1.4
 
 3-7 to 3-8                 Step 2.1
 
 4-1 to 4-2                 Step 3.2
 
 4-3 to 4-4                 Step 2.1
 
 5-1 to 5-8                 Step 3.2
 
 6-1                        Step 3.4
 
 7-1                        Step 3.7
--------------------------------------

: Move/step labels of \citet{yu2016salve} introduction. \label{tbl:sample-moves}

As a demonstration, we firstly select the article "SALVE: server authentication with location verification" \citep{yu2016salve} to be added into the initial E2 dataset. This article has been labeled with the moves/steps as table \ref{tbl:sample-moves}. We validate each transition of labels in this article. We find the first potential error appears in the transition from the last sentence of the first paragraph to the first sentence of the second paragraph, because the probability of the transition $Step 1.3 \to Step 1.2$ shown in the table \ref{tbl:init-matrix-e2} is zero. It is reasonable that we need to recheck labels of these two sentences.

The two sentences in this article are written as follows:

"... When estimated using secure localization methods, location further becomes a unique characteristic of the mobile device.

Location information obtained from mobile networks can be used in critical security applications. ..." \citep[p1]{yu2016salve}

The previous sentence specifies the topic from general localization service to the secure localization problem. So it should be labeled as "Step 1.3". The following sentence emphasizes the usage of the localization service. So "Step 1.2" is its move. After rechecking these two sentences, we decide to accept this transition.

In this way, we can find another three potential errors in the last sentence of the third paragraph, the last sentence of the forth paragraph and the sixth paragraph. We recheck them one by one and correct the mistake or accept the original label directly. Then we add this article introduction into the accepted dataset and update the transition matrix.

We directly show the final probability transition matrix of E2 after adding three another articles into the initial dataset in table \ref{tbl:final-matrix-e2}.

|       |   1.1  |   1.2  |   1.3  |   1.4  |   2.1  |   2.2  |   3.1  |   3.2  |   3.3  |   3.4  |   3.5  |   3.6  |   3.7  |     $ |
| ----- | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ----- |
|    $  |   0.40 |   0.50 |   0.00 |   0.00 |   0.10 |      0 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |  0.00 |
|  1.1  |   0.00 |   0.23 |   0.46 |   0.00 |   0.23 |      0 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   0.08 |   0.00 |  0.00 |
|  1.2  |   0.20 |   0.00 |   0.30 |   0.00 |   0.50 |      0 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |  0.00 |
|  1.3  |   0.36 |   0.18 |   0.00 |   0.18 |   0.27 |      0 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |  0.00 |
|  1.4  |   0.10 |   0.00 |   0.00 |   0.00 |   0.70 |      0 |   0.20 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |  0.00 |
|  2.1  |   0.05 |   0.00 |   0.10 |   0.33 |   0.00 |      0 |   0.14 |   0.10 |   0.05 |   0.10 |   0.05 |   0.05 |   0.00 |  0.05 |
|  2.2  |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |      0 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |  0.00 |
|  3.1  |   0.00 |   0.00 |   0.00 |   0.10 |   0.00 |      0 |   0.00 |   0.40 |   0.10 |   0.10 |   0.00 |   0.00 |   0.30 |  0.00 |
|  3.2  |   0.00 |   0.00 |   0.00 |   0.00 |   0.11 |      0 |   0.11 |   0.00 |   0.00 |   0.56 |   0.00 |   0.00 |   0.11 |  0.11 |
|  3.3  |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |      0 |   0.50 |   0.00 |   0.00 |   0.50 |   0.00 |   0.00 |   0.00 |  0.00 |
|  3.4  |   0.00 |   0.00 |   0.00 |   0.00 |   0.11 |      0 |   0.22 |   0.22 |   0.00 |   0.00 |   0.33 |   0.00 |   0.11 |  0.00 |
|  3.5  |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |      0 |   0.00 |   0.25 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |  0.75 |
|  3.6  |   0.50 |   0.00 |   0.00 |   0.00 |   0.00 |      0 |   0.50 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |  0.00 |
|  3.7  |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |      0 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |   0.00 |  1.00 |

: The final probability transition matrix of E2 article introductions. \label{tbl:final-matrix-e2}

# Discussion

This study is performed on top of the genre-based analysis. The main objective is to improve the accuracy of the traditional genre-based analysis. According to the result in section \ref{results}, the method proposed by the present article can indeed reduce the false-positive error by doing a few rechecks. The methodology has been proved robust and practical. However, this method still cannot find and correct the true-negative error efficiently. It may be a major challenge in the future.

A preferred benefit from this study is the automatic analysis. We provide a series of toolkits \citep{fno2010} to assist some statistical analysis automatically. Although there have been a few software systems \citep[e.g.][]{Anthony2003, cotos2014genre} developed to perform the genre-based analysis automatically, they are not able to guarantee the result is accurate or check the potential error in an efficient way. Our method can allow the analyzer to fix the potential error efficiently, which should be very helpful in the large-scale analysis.

Some general studies \citep[e.g.][]{zobel2015writing, gastel2016write} about writing research articles summarize the practical methods, which may give some useful recommendations or valuable insights on how to reduce the potential error more efficiently.

# Conclusion

In this article, we proposed a robust and practical method to perform the genre-based analysis with the modified CARS model. This method can allow the analyzer to reduce the false-positive error and fix the potential error by only reviewing the necessary part of the original article. A series of useful toolkits are also developed to assist and finish parts of the analysis automatically. The effectiveness of this method and the simplified workflow has been shown in this article. Some known limitations of this method are also explained and discussed. To fix these limitations, some major challenges can not be avoided. The next step of this work should be to address these key challenges and improve the performance of this method.

\section*{Acknowledgements}\label{acknowledgements}

We would like to express our gratitude to Ya Xiao, Shenshen Chen, Leifeng He, Chenxi Huang, Lei Zhou and Yuxiang Zhao for their volunteering to provide and review the move/step labels of the research articles. We are also very grateful to Sujin Xu and Hongping Tao for their contributing the useful data sources. Our thanks also go to our classmates of the academic English writing course for their helpful and insightful comments.

\section*{Appendix A. Supplementary material}\label{appendix-a}

Supplementary data associated with this article can be found at [https://github.com/fno2010/writing-\
analyzer](https://github.com/fno2010/writing-analyzer).
