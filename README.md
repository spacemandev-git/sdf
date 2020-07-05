# Standard Deck Format 
[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/K3K11VCDK)
SDF a specification for represeting any type of card as an YAML file. 

Motivations:
- Provide a template for decks that shared data not just the image of the card
- Allow for easy rendering of the card as an image
- Maintain low file size
- Be game agnostic
- Allow for easy remixing of decks

## SDF Folder Structure
We namespace deck folders much like code namespacing. For user Spacemandev, who wants to make the deck "Sinbad" for the game "Unmatched", the namespace might look like:
sinbad.unmatched.spacemandev
and would resolve to the folder
spacemandev/unmatched/sinbad

In a given deck folder are the following items:

cards/
templates/
assets/
deck.yaml

### Cards
Cards/ is a folder with each individual card file as a yaml file that holds the data about the cards. A card file looks like:

namespace: the namespace for the card (cardname.deckname.gamename.username)
cardtype: the cardtype that this card is. when rendering, the interpreter looks for templates/cardtype.html 
cardback: the back of the card. when rendering, the interpreter looks for templates/cardback.html
data:
  - list of attributes for the card ("attack":5)
asset:
  - list of assets for the card ("centerimg":"monster.jpg")

### Templates
It is recommended to use MUSTACHE templates with built in style tags for each template
A simple template might look like
```
<style></style>
<div><h1>{{data.name}}</h1></div>
```
If all it did was pull the name attribute from the data of the card when rendering.

### Assets
Assets folder holds all the image files used by the card. 


## Requirements
CairoSVG Pystache YAML

## SDF Compiler
SDF compiler takes in an decknamespace and looks for the right folder structure and an CSV file. Then it reads the file turning all the entires into yaml files and then zipping up the whole shebang along into a zip file ready to be distributed. 

### CSV Structure
_cardtype and _cardback MUST be present as column headings in the csv file and list the name (without .html) of the template used to render the card
_quantity is used to determine how many copies of the card you want in the deck
_attributes WILL NOT be added to the card, and are reserved for future meta attributes

&ast; is used to prefix any column headings that denote assets 

all other column headings are treated as data attributes for the card


## SDF Interpreter
The interpreter reads a Zip file of an SDF deck and outputs an deckname_images/ folder with pictures of each card


