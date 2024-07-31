# SpellChecking-
This process verify that a particular word is spelled properly according to some dictionary. Spell checkers are used in many applications, including word processors (such as Microsoft Word), electronic dictionaries…
Spell checking itself is trivial, requiring only a simple lookup in a dictionary. However, most applications of spell checking also require that the spell checker provide a list of potentially 
correct spellings (“near matches”) when the word was spelled improperly. For instance, if I type 
“speling” into an online dictionary, it will provide suggestions of similar words that I may have 
meant to type, including “spelling”, “spoiling”, “sapling”, and “splendid”.

 Method
First thing have to do in a spell checking model is create the required dependencies
1. Dictionary
  Cause this project is based on probability of word apprear in dictionary so, the word will be extract from some standard passage Eng, novel: romeo and juliet, sherlock holmes
  
2. Candidate correction from the word
  4 regular method are delete, swap, replace, insert
  
  

We can identify four main components in the final expression:

1- Selection mechanism — We select a candidate correction with the highest probability.

2- Candidate model: A list of all candidates that will be considered. It is common to generate candidates that are valid words within certain edit distance. Petr Norvig in his work (above) uses the Damerau–Levenshtein distance, wherein the set of allowed operations is character insertion, deletion, substitution and transposition of two adjacent letters.

The choice of this metric because these four operations cover more than 80 percent of all human misspellings.

3- Error model P(w|c): A probabilistic model that estimates a noisy channel transmission posterior probability for all possible values of w and c is usually denoted as an error model. These probabilities should be estimated from data, however, for simplicity, Petr Norvig uses edit distance to approximate them. In this way, the fewer operations is required to transform the received word w to candidate word c, the higher the probability P(w|c).

4-Language model P(c): A probabilistic model that estimates a priori probability of input word c is called language model.
