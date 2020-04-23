# Standard Deck Format 

SDF a specification for represeting any type of card as an YAML file. This allows easy prototyping with new card types 

## SDF Compiler
SDF compiler takes in an decknamespace and looks for the right folder structure and an excel file. Then it reads the file turning all the entires into yaml files and then zipping up the whole shebang along into a zip file ready to be distributed. 

## SDF Interpreter
The interpreter reads a Zip file of an SDF deck and outputs an deckname_images/ folder with pictures of each card


