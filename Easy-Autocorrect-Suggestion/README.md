## Problem Statement Difficulty: EASY

Problem Statement: Autocorrect Suggestions

Problem Statement Description: Problem Description: Your task is to develop an AI system capable of providing autocorrect suggestions for English words. The system should be able to recognize misspelled words and suggest the correct spelling. It should have the capability to handle a wide range of words and common spelling mistakes.
Input: An English word provided by the user. The word could be spelled correctly or incorrectly.

Output: If the word is spelled incorrectly, the system should provide a list of possible correct spellings. If the word is spelled correctly, the system could confirm its correctness or provide synonyms or similar words as suggestions.

Rules: Participants can use existing autocorrect algorithms to develop the system. However, they should justify their choice of algorithms and explain how these contribute to the effectiveness of the system. They should demonstrate the system's ability to accurately correct a wide variety of common spelling errors.

Reference: The reference is a GeeksforGeeks tutorial that demonstrates how to implement an autocorrect feature using Natural Language Processing in Python. Participants can use this tutorial to understand the mechanism of an autocorrect system, learn about the implementation of NLP for autocorrect suggestions, and use the provided code as a basis for their solution.
https://www.geeksforgeeks.org/autocorrector-feature-using-nlp-in-python/

1. Edit distance: Is the number of letters that is required to change a word to another word.
2. Jaccard distance: is the measure of similarity between the sets.

## Solution Visualization

<table width="100%"> 
<tr>
<td width="50%">      
&nbsp; 
<br>
<p align="center">
  Word : Collection
</p>
<img src="https://github.com/Mohammedvaraliya/AI-Amplify-Hackathon/assets/95087498/726a3778-ab08-435e-b93f-ad56b1d4728f">
</td> 
<td width="50%">
<br>
<p align="center">
  Word : Section
</p>
<img src="https://github.com/Mohammedvaraliya/AI-Amplify-Hackathon/assets/95087498/9d8769dd-1822-404f-b3e5-3524ee6b31cf">
</td>
</tr>
<tr>
<td width="50%">
<br>
<p align="center">
  Word : Human
</p>
<img src="https://github.com/Mohammedvaraliya/AI-Amplify-Hackathon/assets/95087498/4d6863f6-0c8e-4256-aea4-0f13788a509f">
</td>
<td width="50%">
<br>
<p align="center">
  Word : Distribution
</p>
<img src="https://github.com/Mohammedvaraliya/AI-Amplify-Hackathon/assets/95087498/345d27f1-dbf7-4f6a-abec-bcc625e200d8">
</td>
</tr>
</table>
