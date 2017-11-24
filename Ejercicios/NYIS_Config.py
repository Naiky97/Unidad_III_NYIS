#Naiky Yunetsy Isidro Suarez
#GITI9072-e

from configparser import ConfigParser

def config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    #read config file
    parser.read(filename)

    #get section default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in {1} file'.format(section, filename))
    return db