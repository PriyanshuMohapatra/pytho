
import random

first  = ['Once upon a time', 'In the era of celestials', 'A long time back']
  
protagonist = [' there lived a Supreme being',' there was a Swordsman',
             ' there lived a young boy']
  
duration = [' many moons ago', ' in the night of darkness''in the absensce of light']
  
plot = [' he was passing by', ' he was going to slaughter']
  
the_place = ['the valley of death',' his clan']
  
protagonist_the_two = [' he saw an ancient being ', ' he saw a young lady']
  
nature = [' who seemed to radiate youthfulness ', ' who seemed to have killing intent']
  
work = [' and was standing with a sword in the hand', 'and was looking at him who was  standing infront the sea']

# it will select each element from the variables associated and add them
print(random.choice(first)+random.choice(protagonist
                                         )+
      random.choice(duration)+random.choice(plot)+random.choice(the_place)+random.choice(protagonist_the_two)+random.choice
      (nature)+random.choice(work))