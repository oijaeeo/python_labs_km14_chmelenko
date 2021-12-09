import re
import csv

with open('platina.csv', 'w', newline='') as csvfile:
    writer = csv.writer( csvfile )
    writer.writerow(['Abu Dhabi Ba6y',2021])
    writer.writerow(['This is not love',2018])
    writer.writerow(['Brothel',2018])
    writer.writerow(['Bandana',2018])
    writer.writerow(['Forever',2019])
    writer.writerow(['Salam',2020])
    
list=[ ]
with open( 'platina.csv', 'r' ) as songs:
    strings = songs.readlines()
    print( 'File name:' , songs.name )
    print( '-' * 15)
    for string in strings:
        restring = string.replace( '\n' , ' Year' )
        tear = re.split( ',' , restring )
        list.append( tear )
        print( ','.join( tear ) )
        print( '-' * 15)