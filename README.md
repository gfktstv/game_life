#### Game "Life" is a task in CS class
**There is requirements for the game in English (in Russian listed below)**
It is required to write a program that simulates the life of animals:

All "life" occurs on an infinite area divided into cells, where each object occupies from one to three cells depending on its mass.
Animals are divided into predators, herbivores, and omnivores. Predators eat other animals, herbivores eat plants, omnivores eat both animals and plants.
Plants are divided into nutritious and poisonous. Nutritious plants give their nutritional value to whoever eats them, poisonous plants kill with a probability of 1/2.
All changes in "life" occur discretely, within one unit of time.
When a new unit of time begins, animals either stay in place or move with a probability of 1/2. The direction of movement is chosen from all available directions with equal probability (diagonal movement is allowed). Each "day," hunger increases, and health decreases. The speed of an animal is from 1 to 5 cells, proportional to its health.
When two predators land on the same cell, they engage in combat if they are both hungry or if the aggressiveness level of at least one of them is higher than a certain level. The winner is the one who is larger/hungrier/more aggressive/healthier (the formula is at the discretion of the developer). The loser dies, and the winner eats it.
When a predator lands on a cell with an herbivore, it attacks only if hungry. The probability of winning should depend on the level of hunger. The predator eats the defeated herbivore. The losing predator retreats with a loss of health.
Omnivores engage in combat only if hungry or if attacked by a predator. The rules of victory are the same as for predators.
Herbivores and omnivores eat plants only if hungry.
Hunger cannot be satisfied above a certain level; uneaten food disappears and is inaccessible to other animals. When an object is eaten, its nutritional value equals its mass.
If a plant is not eaten, it increases its mass by a certain amount in one unit of time.
Animals and plants die when they reach a certain age, defined individually for each object.
Additionally:
13. Animals can reproduce. For reproduction to occur, two animals of the same species, different sexes, and older than a certain age must be in the same cell. As a result, a new animal with age 0 and a certain mass appears on one of the randomly available neighboring cells.

Plants reproduce by shoots - with a probability of 1/10, instead of increasing mass, a plant creates another plant on one of the randomly available neighboring cells.
Among the animals, there may be scavengers.
Herbivores can form herds to increase survival.
General conditions:

At the beginning of the emulation, all animals and plants already have some age, mass, etc.
At the beginning of the emulation, all objects are randomly placed within a 100x100 cell territory.
The emulation ends when there is nothing left on the territory.
The result should be provided as a script (set of scripts) along with accompanying files (if required) in a folder named after the author's last name, written in Russian. The code should contain comments and comply with PEP8 requirements.

**There is requirements for the game in Russian**
Требуется написать программу эмулирующую жизнь животных:
1. Вся "жизнь" поисходит на бесконечной площади, расчерченной на клетки, где каждый объект занимает от одной до трех клеток в зависимости от массы
2. Животные делятся на хищников, травоядных и всеядных. Хищники едят других животных, травоядные - растения, всеядные - и животных, и растения.
3. Растения делятся на питательные и ядовитые. Питательные отдают свою питательную ценность тому, кто их съел, ядовитые убивают с вероятностью 1/2
4. Все изменения в "жизни" происходят дискретно, за одну единицу времени.
5. Животные при наступлении новой единицы времени остаются на месте или перемещаются с вероятностью 1/2. Направление перемещения выбирается из всех доступных с равной вероятностью (по диагонали ходить можно). "Ежедневно" возрастает голод и уменьшается здоровье. Скорость животного - от 1 до 5 клеток, пропорциональна здоровью. 
6. При попадании на одну клетку хищники вступают в бой если они оба голодны или если уровень агрессивности хотя бы одного из них выше определенного уровня. Побеждает тот, кто массивнее/голоднее/агрессивнее/здоровее (формула на усмотрение разработчика). Проигравший погибает, его съедает победитель.
7. При попадании на клетку с травоядным хищник нападает только если голоден. Вероятность победы должна зависеть от уровня голода. Проигравшего травоядного съедает хищник. Проигравший хищник ретируется с потерей здоровья
8. Всеядные вступают в бой только если голодны или на них напал хищник. Правила победы такие же, как у хищников. 
9. Травоядные и всеядные едят растения только если голодны.
10. Нельзя утолить голод выше заданного уровня, несъеденное исчезает и недоступно другим животным. При съедении объекта его питательность равна его массе.
11. Если растение не съедено, оно за единицу времени увеличивает свою массу на определенную величину.
12. Животные и растения умирают при достижении определенного возраста, задаваемого для каждого объекта отдельно. 

Дополнительно:
13. Животные могут размножаться. Для размножения необходимо, чтобы в одной клетке оказались два животных одного вида, разного пола, старше определенного возраста. В результате на одной из случайных свободных соседних клеток появляется новое животное с возрастом 0 и определенной массой.
14. Растения размножаются побегами - с вероятностью 1/10 растение вместо увеличения массы создает другое растение на одной из случайных свободных соседних клеток.
15. Среди животных могут быть падальщики
16. Травоядные могут объединятьв с стаи для повышения выживаемости


Общие условия:
1. В начале эмуляции все животные и растения уже имеют какой-то возраст, массу и т.д.
2. В начале эмуляции все объекты размещаются случайным образом в пределах территории 100х100 клеток
3. Эмуляция завершается, когда на территории не остается ничего

Результат должен быть выложен в виде скрипта (набора скриптов) вместе с сопутствующими файлами (если они требуются) в папку с фамилией автора, написанной на русском языке.
Код должен содержать комментарии и соответствовать требованиям PEP8
