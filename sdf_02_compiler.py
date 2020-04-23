# Deck Namespace -> Assumes 
# Assumes the Deck Namespace Folder is setup:
  ## deckname.zip #compiler output
  ## deckname_images/ #interpreter output
  ## deckname.csv
  ## deckname/
  ##   assets/
  ##   cards/
  ##   templates/
  ##   deck.yaml

import sys, csv
import yaml
from os import listdir
from os.path import isfile, join
import shutil

def buildDeck(namespace):
  """Takes in a Deck namespace file and finds the csv file associated with it"""
  # Locate & Load the CSV file
  try:
    path = './%s/%s/%s.csv' % (namespace.split('.')[2], namespace.split('.')[1], namespace.split('.')[0])
    return list(csv.DictReader(open(path, 'r')))
  except:
    raise Exception("Could not find CSV file for the specified namespace")

def writedecktofile(namespace, deck):
  #Build cardlist and write the card.yaml files
  cardList = []
  for card in deck:
    cardName = card['name'].lower().replace(" ", "_")
    cardPath = './%s/%s/%s/cards/%s.yaml' % (namespace.split('.')[2], namespace.split('.')[1], namespace.split('.')[0], cardName)
    try:
      finalCard = {
        "namespace": cardName + "." + namespace,
        "data": {},
        "assets": {}, #should have their .jpg/.png/etc
        "cardType": card['_cardtype'], #do not need to have .html
        "cardBack": card['_cardback']  #do not need to have .html
      }
    except:
      raise Exception("Could not find _cardtype or _cardback in the CSV file")

    for attr in card.keys():
      if attr == "_cardtype" or attr == "_cardback":
        pass
      elif(attr[0] == "*"):
        finalCard['assets'][attr[1:]] = card[attr] #ignore the * when dumping
      else:
        finalCard['data'][attr] = card[attr]      

    with open(cardPath, 'w+') as file:
      yaml.dump(finalCard, file)
    cardList.append(cardName)

  
  #Append to deck meta
  try:
    deckPath = './%s/%s/%s/deck.yaml' % (namespace.split('.')[2], namespace.split('.')[1], namespace.split('.')[0])
    with open(deckPath, 'r') as file:
      meta = (yaml.load(file, Loader=yaml.FullLoader))['meta']
    with open(deckPath, 'w') as file:
      yaml.dump({"meta":meta, "cardlist":cardList}, file)
  except:
    raise Exception("Could not load deck.yaml")  

#Outputs a ZIP file for each deck
if __name__ == "__main__":
  #print(sys.argv[1])
  #build deck
  namespace = sys.argv[1]
  try: 
    deck = buildDeck(namespace)
  except Exception as e:
    print(str(e))
  #write deck to file
  try:
    writedecktofile(namespace, deck)
  except Exception as e:
    print(str(e))
  #create zip
  dirpath =  './%s/%s/%s/' % (namespace.split('.')[2], namespace.split('.')[1], namespace.split('.')[0])
  shutil.make_archive(dirpath, 'zip', dirpath)