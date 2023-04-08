import wayback
from datetime import datetime

client = wayback.WaybackClient()

for record in client.search('http://nasa.gov', to_date=datetime(1999, 1, 1)):

    memento = client.get_memento(record)

    fileName=memento.memento_url.replace("/","-")+".html"

    memento_file = open(fileName, "a")

    memento_file.write(memento.text)

    memento_file.close()

    print (fileName)
