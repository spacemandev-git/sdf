[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/K3K11VCDK)


SDF Version: 0.5

# Deck Structure

### For decks with card images 
deckfolder/
- deck.yaml
- cards.yaml
- images/
- (optional) templates/
- (optional) assets/

## SDFv05

Card Objects may specifify a imgPath: OR a templatePath:
These things are mutually exclusive. 

If imgPath is provided then the card will be built by images. 

If templatePath is provided, then svg template will be treated as a handlebars template and rendered with assets/ and data. 

If both are provided then the card will NOT be rendered. 

### Deck.yaml
- deck_name: namespace for the deck, usually written deckname.gamename.creatorname
- game: name of the game this deck is for
- sdf_version: version of sdf this complies with

### Cards.yaml
Split with `---' to denote different file for each card

For every card:
- namespace: written cardname.deckname.gamename.creatorname
- data: key:value pairs used to store data for the card
- (optional) cardBack: images/name_of_file.png 
- (optional) qty: # of copies of this card that exist in the deck 
IF card image is predfined:
- (optional) imgPath: images/name_of_image_file.jpg

IF card image is a template:
- (optional) templatePath
