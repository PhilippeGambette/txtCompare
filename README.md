# txtCompare

Tools for text comparison

## pairwiseMedite

Automatically call MEDITE at http://obvil.lip6.fr/medite/:
* to start pairwise comparisons of all UTF-8 encoded text files in a `files` folder in the same folder and simply execute the script with python: `python pairwiseMedite.py`
* to start comparing two long text files which were previously split in smaller parts (`file1-1.txt` compared with `file2-1.txt`, `file1-2.txt` with `file2-2.txt`, etc., if `file1` and `file2` are given as input file names): `python pairwiseMedite.py L_education_sentimentale_1870.txt L_education_sentimentale_1880.txt`

Requires Python 3 and selenium with Firefox browser (https://selenium-python.readthedocs.io/installation.html).

Demo of the result at https://philippegambette.github.io/txtCompare/pairwiseMedite

In order to split long files into smaller parts, insert the character `?` each time you want to split the file and then use the script decoupeOuvrage.py with the filename as input: `python decoupeOuvrage L_education_sentimentale_1870.txt`

## sankeyCompare

Visualize the differences of order of texts in two collections of texts (for example, two editions of a collection of poems, or short stories) with a Sankey Diagram, built in Javascript/jQuery from a spreadsheet file.

Demo of the result at https://philippegambette.github.io/txtCompare/sankeyCompare