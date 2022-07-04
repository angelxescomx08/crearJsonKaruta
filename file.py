autores = open('autor.txt','r', encoding='utf8')
poemas = open('poema.txt','r', encoding='utf8')
json = open('cartas.ts','w',encoding='utf8')

json.write('export const cartas = [ \n')
id = 1
for autor in autores:
    poema = poemas.readline().rstrip()
    autor = autor.rstrip()

    json.write('\t{\n')
    
    json.write('\t\tid: "{id}",\n'.format(id=id))
    json.write('\t\tautor: "{autor}",\n'.format(autor=autor))
    json.write('\t\tpoema: "{poema}"\n'.format(poema=poema))

    json.write('\t},\n')

    id+=1

json.write('];')

autores.close()
poemas.close()
json.close()