## Typo-Corrector
Typo corrector is an engine that references a database of stored words to predict the word that you probably meant to type.

### Part 1 - Segmentation
The system first splits up the user input string into a list of words, which can be pulled.

### Part 2 - Weightage
The system then weights all the words in the English language based on how many of their letters are the same and in the same spot as the user's last typed word.

### Part 3 - Correction
Finally, the system allows the user to change the wrong word to the corrected version using a simple GUI click element.

All in all, this system allows the user to type text, and runs in the background to actively correct the user's typographical errors as they are made.
