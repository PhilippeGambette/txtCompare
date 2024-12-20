# txtCompare

Tools for text comparison

## intertextFinder

### `intertextFinder.py`
How to use (with texts provided in the `.txt` format, UTF-8 encoding):
* put the corpus into a folder named `TXT` in the same folder as this script;
* put the texts to analyze into a folder named `todo` in the same folder as this script;
* run the script by executing in the console the following command: `python intertextFinder.py`;
* for each text file in the todo folder, a new file with the same name and the extra extension `.html` is added into the same folder, open it in a web browser to see the results.

Demo of the result at [https://philippegambette.github.io/txtCompare/intertextFinder](https://philippegambette.github.io/txtCompare/intertextFinder) to check which poems by Marceline Desbordes-Valmore are present in her 1849 book *Les Anges de la famille*

### `intratextFinder.py`
How to use (with texts provided in the `.txt` format, UTF-8 encoding):
* put the corpus into a folder named `TXT` in the same folder as this script;
* run the script by executing in the console the following command: `python intratextFinder.py`;
* for each text file in the `TXT` folder, a new file with the same name and the extra extension `.html` is added into the same folder;
* a file named `intratextFinder.html` is created in the folder containing the script: open it in a web browser to see the results.

Demo of the result at [https://philippegambette.github.io/txtCompare/intertextFinder/intratextFinder.html](https://philippegambette.github.io/txtCompare/intertextFinder/intratextFinder.html) to find intratextuality between three poetry books by Victor Hugo, *Feuilles d'automne*, *Odes et balades* and *Orientales*.


## pairwiseMedite

Automatically call MEDITE at [http://obvil.lip6.fr/medite/](http://obvil.lip6.fr/medite/):
* to start pairwise comparisons of all UTF-8 encoded text files in a `files` folder in the same folder and simply execute the script with python: `python pairwiseMedite.py`
* to start comparing two long text files which were previously split in smaller parts (`file1-1.txt` compared with `file2-1.txt`, `file1-2.txt` with `file2-2.txt`, etc., if `file1` and `file2` are given as input file names): `python pairwiseMedite.py L_education_sentimentale_1870.txt L_education_sentimentale_1880.txt`

Requires Python 3 and selenium with Firefox browser ([https://selenium-python.readthedocs.io/installation.html](https://selenium-python.readthedocs.io/installation.html)).

Demo of the result at [https://philippegambette.github.io/txtCompare/pairwiseMedite](https://philippegambette.github.io/txtCompare/pairwiseMedite).

In order to split long files into smaller parts, insert the character `?` each time you want to split the file and then use the script decoupeOuvrage.py with the filename as input: `python decoupeOuvrage L_education_sentimentale_1870.txt`

## sankeyCompare

Visualize the differences of order of texts in two collections of texts (for example, two editions of a collection of poems, or short stories) with a Sankey Diagram, built in Javascript/jQuery from a spreadsheet file.

Demo of the result at [https://philippegambette.github.io/txtCompare/sankeyCompare](https://philippegambette.github.io/txtCompare/sankeyCompare).

## visuLexique

Visualisation of the evolution of the frequencies, along a text, of words taken from two input word lists.

Tool available online, with a demo on the *Memoirs* of Marguerite de Valois, at [https://philippegambette.github.io/txtCompare/visuLexique](https://philippegambette.github.io/txtCompare/visuLexique).

## CollaTeX

Tutorial for multiple alignment of texts using tools from bioinformatics, at [https://philippegambette.github.io/txtCompare/CollateX/](https://philippegambette.github.io/txtCompare/CollateX/).
