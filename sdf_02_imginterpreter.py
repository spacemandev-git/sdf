## Unzip SDF.zip into temp
## Load Cards into memory
## Replace the asset values with path for the unzipped files
## Run through with Mustache
## 
import os
import sys
from zipfile import ZipFile
import pystache
import yaml
import imgkit
import tempfile

def loadDeck(fileUrl):
  deckfile = ZipFile(fileUrl)
  path = os.getcwd().replace('\\','/') + "/temp_dir/"
  #path = tempfile.TemporaryDirectory().name + "/"
  print(path)
  #Create a temp dir to 
  deckfile.extractall(path)
  deckyaml = yaml.load(open(path+'deck.yaml','r'), Loader=yaml.FullLoader)
  #print(deckyaml)
  for c in deckyaml['cardlist']:
    card = yaml.load(open(path+"cards/"+c+".yaml", 'r'), Loader=yaml.FullLoader)

    #Replace asset urls with path
    assetspath = 'file:///' + path + "assets/"
    #assetspath = "assets/"
    print(assetspath)
    for asset in card['assets']:
      card['assets'][asset] = assetspath + card['assets'][asset]
    
    #sub the data and assets into the card
    
    templatepath = path+'templates/'+card['cardType']+'.svg'
    frontSVG = open(templatepath, 'r').read()
    cardSVG = pystache.render(frontSVG, card)
    
    os.mkdir('deckimgs')
    outputPath = "deckimgs/"+c+'.png'
    imgkit.from_string(cardSVG, outputPath)


if __name__ == "__main__":
  fileUrl = sys.argv[1]
  loadDeck(fileUrl)