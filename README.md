[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/K3K11VCDK)


SDF Version: 0.6

#Deck Structure
deckfolder.zip/
  deck.yaml
  images/

### deck.Yaml
- (required) name: name of the card, does not need the full path as previous versions required
- (optional) version: sdf version to be used by the interpreter. If left out, will use interpreter default
- (optional) img: path to file inside images. If the file is images/img.jpg then the path should just be img.jpg
- (optional) back: image path for the back of the card 
- (optional) data: object with data values for the card 
- (optional) qty: How many copies of the card exist in the deck
Split with `---' to denote different file for each card
