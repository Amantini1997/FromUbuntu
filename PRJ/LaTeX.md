textbf{} -> bold
    it is the same as {\bf text}
textit -> italic
texttt -> monospace (programming like) e.g. \texttt{mdpAgent.py}

\chapter -> requires \documentclass{book}
\section
    \section*{} will not be numerated
\subsection{}

\tableofcontents -> [TOC]


\includegraphics[scale=0.5]{filename} -> requires \usepackage{graphicx}
> 0.5 = 50%, you could even say width=10cm or using the height

\begin{figure}[htb]
> put the image h = here if you can, else t = top, else b = bottom
\centering
\includegraphics[]{}
\caption{image}
\end{figure}

> this will count the figure eg. figure 1.1

To mention a figure use labels in the figure and reference it:
\begin{figure}
...
\label{neilArmostrong}
\end{figure}

Please see figure \ref{neilArmostrong}

labels can refer to sections as well

\\ or \newline breaks the line
double \n creates a new paragraph and the new line start with \t which is called \quads

to leave space between letters (or words) in a line use \hline{5cm}

\mbox{} prevents to break the content at any point

you can also replace blankspaces with ~ which means space that cannot be broken by going to a new line

use it with
> please see figure~\ref{}

use `listings` package to create loops
\begin{listings}[language=Python]
...code here
\end{listings}

spaces and tabs are displayed as rough text

you can even color commands

Also check \lstinputlisting[]language=Python]{file}
> used to import the code

% is reserved to comments, escape it to use it \%

To add bibliographies create a .bib file of the form @book{}

and include
\bibliographystyle{plain} 
\bibliography{references} at the end of the LaTeX file

sort bibliographies alphabetically


