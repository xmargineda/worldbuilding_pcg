#Prompt to generate the entities in the text
raw_input_character_txt = '''Categorize the all entities in the text that fit into one of the categories. If an entity doesn\'t fit into any of the categories, DO NOT categorize it. The categories are the following:
*Character, which represents a person within the story.
*Settlement, which represents a location that is populated.
*Place, which represents a place within the story that seems relevant.
*Group, which represents a group of people who are working together.
Text: The great mage Lyra, leader of the Arcane Conglomerate, helped the kingdom of Wasben win the Thunder War against the kingdom of Golia and the mercenaries of the Iron Fist. To show his gratefulness, the king Loan and the queen Sea built the Academy, a magical school; and a wizard tower for Lyra, where she spent the rest of her days.
Catergorization:
*Lyra->Character
*Arcane Conglomerate->Faction
*Kingdom of Wasben->Settlement
*Kingdom of Golia->Settlement\n*Iron Fist->Faction
*King Loan->Character
*Queen Sea->Character
*Academy->Place
*Lyra\'s tower->Place

Text: {txt}
Catergorization:
'''''

#Prompt to generate the story actions so far
raw_input_story_txt = '''Context: A chapter is a division of a narrative composed by a number of story actions (at least one) that has a similar mood througout the chapter. A story action is a relevant event within the narrative provoked by an entity that moves the plot forward in a way.
Analyze the text to write it as a list of chapters, and, for each chapter, all its story actions ordered.

Text: After leaving his home town in search of a remedy for his father, Ari ended up at the city of Vinyas. Ari met with Heila, a famous bottanist, at Vinurl Academy and explained the situation with his father. She deduced that the sickness that his father is suffering is Olisgareosis, a rare degenerative disease. Heila agreed to help Ari, in exchange for a favour in the future after his father has healed. Desperate to help his father, Ari agreed. After making the pact, Helia explained that to attempt to make a cure for his father she would need a rare material that couldn\'t be found inside her workshop: the Purunima Aldima, a flower that grows in hot climates.
Entities:
- Ari
- Ari\'s father
- Heila
- Ari\'s home town
- Vinyas
- Vinurl Academy
- Olisgareosis
- Purunima Aldima
Story:
Chapter "Ari\'s Departure": Ari leaves his hometown to try to help his sick father
1. Ari left his home town in search for a remedy for his father
Chapter "Meeting Heila": Ari meets Heila, who agrees to help Ari in exchange for a favor
1. Ari went to Vinyas
2. Ari and Heila had a meeting
3. Ari explained to Heila that his father was sick
4. Heila deduced that the sickness that Ari\'s father is suffering is Olisgareosis
5. Heila agreed to help Ari in exchange for a favour after his father was healed
6. Heila explained to Ari that to attempt to make a cure for his father she would need the Purunima Aldima

Text: {txt}
Entities:
{entities}
Story:
'''

gen_words_data_prop_table = {'appearance':'a list of independent short sentences',
                    'climate':'a list of independent short sentences',
                    'description':'a list of independent short sentences',
                    'dislikes':'a list of independent words',
                    'economy':'a list of independent short sentences',
                    'fauna':'a list of independent short sentences',
                    'flora':'a list of independent short sentences',
                    'geography':'a list of independent short sentences',
                    'likes':'a list of independent words',
                    'material':'a list of materials independent from one another',
                    'objective':'a list of independent short sentences',
                    'organization':'a list of independent short sentences',
                    'population':'a list of independent short sencences',
                    'profession':'a list of independent words',
                    'use':'a list of independent short sentences',
                    'value':'a list of independent short sentences',
                    'citizens':'a number'}


data_property_generator_text = '''Context: A story in a medieval fantasy world is being written and you have to help by coming up with plausible information about a given topic.
Generate {gen_words} about the topic. Assure the generated content doesn't contradict the given information about the topic.
Topic: {topic} -> {topic_definition}
Information related to the topic: {info_topic}
Generated content:
-'''

entity_property_generator_text = '''Context: A story in a medieval fantasy world is being written and you have to help by coming up with the desired entity that is related to another.
Generate an a name and a description (two or three simple sencences) for a {entity_type} that is related to {topic_entity}. Assure the generated content doesn't contradict the given information about the topic.
Relation type: {topic} -> {topic_definition}
Information related to the topic:  {info_topic}
Generated content:
-Name: '''


debug_txt = '''Context: A chapter is a division of a narrative composed by a number of story actions (at least one) that has a similar mood througout the chapter. A story action is a relevant event within the narrative provoked by an entity that moves the plot forward in a way.
Analyze the text to write it as a list of chapters, and, for each chapter, all its story actions ordered.

Text: After leaving his home town in search of a remedy for his father, Ari ended up at the city of Vinyas. Ari met with Heila, a famous bottanist, at Vinurl Academy and explained the situation with his father. She deduced that the sickness that his father is suffering is Olisgareosis, a rare degenerative disease. Heila agreed to help Ari, in exchange for a favour in the future after his father has healed. Desperate to help his father, Ari agreed. After making the pact, Helia explained that to attempt to make a cure for his father she would need a rare material that couldn't be found inside her workshop: the Purunima Aldima, a flower that grows in hot climates.
Entities:
- Ari
- Ari's father
- Heila
- Ari's home town
- Vinyas
- Vinurl Academy
- Olisgareosis
- Purunima Aldima
Story:
Chapter "Ari's Departure": Ari leaves his hometown to try to help his sick father
1. Ari left his home town in search for a remedy for his father
Chapter "Meeting Heila": Ari meets Heila, who agrees to help Ari in exchange for a favor
1. Ari went to Vinyas
2. Ari and Heila had a meeting
3. Ari explained to Heila that his father was sick
4. Heila deduced that the sickness that Ari's father is suffering is Olisgareosis
5. Heila agreed to help Ari in exchange for a favour after his father was healed
6. Heila explained to Ari that to attempt to make a cure for his father she would need the Purunima Aldima

Text: Nott was born a halfling, Revvetha "Veth" Smyt'hh, in the town of Felderwin. Growing up, she was often ridiculed for her peculiarities, which made it difficult for her to fit in, and she had abusive older siblings that used to chase her through the woods, lock her up or dunk her head in the water as "jokes". One day Veth met a halfling man named Yeza Brenatto through a game of truth or dare, and eventually they fell in love. They were later married and had a son, Luc. About three and a half years after Luc's birth, the family was kidnapped by a local goblin clan led by a couple, Drekkit and Khaaz. After being held there for weeks, Veth helped her family to escape, letting her son and husband run ahead while luring their captors away. She was cornered by the goblins and threw a vial of acid in their leader's face, killing him. The goblins recaptured Veth, and Drekkit's widow, Khaaz, took her to an old spellcaster, Isharnai, with instructions to "make her suffer".
Entities:
- Veth (Revvetha)
- Felderwin
- Yeza Brenatto
- Luc
- Drekkit
- Khaaz
- Goblin Clan
- Acid
- Spellcaster Isharnai

Story:
Chapter "Childhood Abuse": Veth experiences abuse from her older siblings growing up
1. Veth was born a halfling
2. Veth experienced difficulty fitting in due to her peculiarities
3. Veth was frequently ridiculed and bullied by her older siblings
4. Her older siblings locked her up or dunked her head in water as jokes

Chapter "Escape and Revenge": Veth escapes and kills the leader of the goblin clan that kidnapped her family
1. Veth met Yeza Brenatto through a game of truth or dare
2. Veth and Yeza fell in love and got married
3. Veth and Yeza had a son, Luc
4. Three and a half years after Luc's birth, the family was kidnapped by a local goblin clan
5. While trying to escape, Veth killed the leader of the goblin clan with acid'''