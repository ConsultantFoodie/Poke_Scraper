import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

num_pokemon=890

pokedex={'Names':[], 'Primary Typing':[], 'Secondary Typing':[], 'HP':[], 'Attack':[], 'Defense':[], 'Sp. Atk':[], 'Sp. Def':[], 'Speed':[], 'Total':[]}

for i in range(1,num_pokemon+1):
	res=requests.get('https://pokemondb.net/pokedex/' + str(i))
	soup=bs(res.text, 'html.parser')

	name=soup.find('h1').get_text()
	table=soup.find('table', attrs={'class':'vitals-table'}).findAll('a', href=True, attrs={'class':'type-icon'})
	stats=soup.find('div', attrs={'class':'resp-scroll'}).findAll('td', attrs={'class':['cell-num', 'cell-total']})[::3]
	
	primary=table[0].get_text()
	secondary='None'
	if len(table)>1:
		secondary=table[1].get_text()

	hp=stats[0].get_text()
	atk=stats[1].get_text()
	dfn=stats[2].get_text()
	sp_atk=stats[3].get_text()
	sp_dfn=stats[4].get_text()
	spd=stats[5].get_text()
	tot=stats[6].get_text()

	pokedex['Names'].append(name)
	pokedex['Primary Typing'].append(primary)
	pokedex['Secondary Typing'].append(secondary)
	pokedex['HP'].append(hp)
	pokedex['Attack'].append(atk)
	pokedex['Defense'].append(dfn)
	pokedex['Sp. Atk'].append(sp_atk)
	pokedex['Sp. Def'].append(sp_dfn)
	pokedex['Speed'].append(spd)
	pokedex['Total'].append(tot)


pokeframe = pd.DataFrame.from_dict(pokedex)
print(pokeframe)