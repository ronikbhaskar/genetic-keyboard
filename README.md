# genetic-keyboard
Building a genetic algorithm from scratch to optimize the layout of a swipe keyboard.

## Overview

I did this as a speedrun to build a genetic algorithm as fast as possible while also having little idea how to build one. I finished in 2 hours and 40 minutes. 

Question: What is the optimal keyboard for single-finger swiping on a phone?

Background: Swipe keyboards don't require the user to input capitalization, and most users don't really care about punctuation, since they're used in the context of instant messages. As such, the main issue slowing experienced users down is the distance their finger has to travel.

Method: Build a fitness function that evaluates keyboards based on the distances between letters for commonly spoken words. The more common a word is, the higher it is weighted in the fitness function. Let the layout of the keyboard be the genetic material. Generate a random population of keyboards. Calculate the fitnesses. Create new keyboards by combining the layouts of the original keyboards, selecting keyboards more frequently if they are fitter. Repeat for *n* generations.

Results: The fitness has improved, but I have yet to properly evaluate my fitness function to absolutely confirm it is a useful metric.

## Datasets

 - frequency list of 1000 most common words in TV scripts in 2006: https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/TV/2006/1-1000 
 - more frequency lists: https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists

