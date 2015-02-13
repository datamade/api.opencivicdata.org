"""
Configuration describing the shapefiles to be loaded.
"""
from django.contrib.gis.gdal.error import OGRIndexError
from datetime import date
import boundaries


state_fips = {
    '01': 'al', '02': 'ak', '04': 'az', '05': 'ar', '06': 'ca', '08': 'co',
    '09': 'ct', '10': 'de', '11': 'dc', '12': 'fl', '13': 'ga', '15': 'hi',
    '16': 'id', '17': 'il', '18': 'in', '19': 'ia', '20': 'ks', '21': 'ky',
    '22': 'la', '23': 'me', '24': 'md', '25': 'ma', '26': 'mi', '27': 'mn',
    '28': 'ms', '29': 'mo', '30': 'mt', '31': 'ne', '32': 'nv', '33': 'nh',
    '34': 'nj', '35': 'nm', '36': 'ny', '37': 'nc', '38': 'nd', '39': 'oh',
    '40': 'ok', '41': 'or', '42': 'pa', '44': 'ri', '45': 'sc', '46': 'sd',
    '47': 'tn', '48': 'tx', '49': 'ut', '50': 'vt', '51': 'va', '53': 'wa',
    '54': 'wv', '55': 'wi', '56': 'wy', '60': 'as', '66': 'gu', '69': 'mp',
    '72': 'pr', '78': 'vi'
}


def tiger_namer(feature):
    global OGRIndexError
    global state_fips

    try:
        fips_code = feature.get('STATEFP')
    except OGRIndexError:
        fips_code = feature.get('STATEFP10')

    try:
        name = feature.get('NAMELSAD')
    except OGRIndexError:
        name = feature.get('NAMELSAD10')

    try:
        geoid = feature.get('GEOID')
    except OGRIndexError:
        geoid = feature.get('GEOID10')

    state_abbrev = state_fips[fips_code].upper()
    name = name.encode('utf8').decode('latin-1')
    resp = u"{0} {1} {2}".format(state_abbrev, name, geoid)
    return resp


def geoid_tiger_namer(feature):
    try:
        geoid = feature.get('GEOID')
    except OGRIndexError:
        geoid = feature.get('GEOID10')
    return geoid


class index_namer(object):
    def __init__(self, prefix):
        self.prefix = prefix
        self.count = 0

    def __call__(self, feature):
        self.count += 1
        return '{0}{1}'.format(self.prefix, self.count)


CENSUS_URL = 'http://www.census.gov/geo/maps-data/data/tiger.html'
LAST_UPDATE = date(2015, 1, 28)
defaults = dict(last_updated=LAST_UPDATE,
                domain='United States',
                authority='US Census Bureau',
                source_url=CENSUS_URL,
                license_URL=CENSUS_URL,
                data_url=CENSUS_URL,
                notes='',
                extra='{}',
               )


# congressional districts
boundaries.register('cd-114',
                    singular='cd-114',
                    file='cd-114/',
                    name_func=tiger_namer,
                    id_func=geoid_tiger_namer,
                    **defaults
                   )

boundaries.register('cd-113',
                    singular='cd-113',
                    file='cd-113/',
                    name_func=tiger_namer,
                    id_func=geoid_tiger_namer,
                    **defaults
                   )

boundaries.register('cd-111',
                    singular='cd-111',
                    file='cd-111/',
                    name_func=tiger_namer,
                    id_func=geoid_tiger_namer,
                    **defaults
                   )

# Zip Code Tabulation Areas
boundaries.register('zcta-14',
                    singular='zcta-14',
                    file='zcta-14/',
                    name_func=boundaries.attr('ZCTA5CE10'),
                    id_func=geoid_tiger_namer,
                    start_date=date(2015, 1, 1),
                    **defaults
                   )

boundaries.register('zcta-13',
                    singular='zcta-13',
                    file='zcta-13/',
                    name_func=boundaries.attr('ZCTA5CE10'),
                    id_func=geoid_tiger_namer,
                    start_date=date(2012, 1, 1),
                    end_date=date(2015, 1, 1),
                    **defaults
                   )

boundaries.register('sldl-14',
                    singular='sldl-14',
                    file='sldl-14/',
                    name_func=tiger_namer,
                    id_func=geoid_tiger_namer,
                    start_date=date(2015, 1, 1),
                    **defaults
                   )

boundaries.register('sldl-13',
                    singular='sldl-13',
                    file='sldl-13/',
                    name_func=tiger_namer,
                    id_func=geoid_tiger_namer,
                    start_date=date(2012, 1, 1),
                    end_date=date(2015, 1, 1),
                    **defaults
                   )

boundaries.register('sldu-14',
                    singular='sldu-14',
                    file='sldu-14/',
                    name_func=tiger_namer,
                    id_func=geoid_tiger_namer,
                    start_date=date(2015, 1, 1),
                    **defaults
                   )

boundaries.register('sldu-13',
                    singular='sldu-13',
                    file='sldu-13/',
                    name_func=tiger_namer,
                    id_func=geoid_tiger_namer,
                    start_date=date(2012, 1, 1),
                    end_date=date(2015, 1, 1),
                    **defaults
                   )

boundaries.register('county-14',
                    singular='county-14',
                    file='county-14/',
                    encoding='latin-1',
                    name_func=tiger_namer,
                    id_func=geoid_tiger_namer,
                    start_date=date(2015, 1, 1),
                    **defaults
                   )

boundaries.register('county-13',
                    singular='county-13',
                    file='county-13/',
                    encoding='latin-1',
                    name_func=tiger_namer,
                    id_func=geoid_tiger_namer,
                    start_date=date(2012, 1, 1),
                    end_date=date(2015, 1, 1),
                    **defaults
                   )

boundaries.register('place-14',
                    singular='place-14',
                    file='place-14/',
                    name_func=tiger_namer,
                    id_func=geoid_tiger_namer,
                    start_date=date(2015, 1, 1),
                    encoding='latin-1',
                    **defaults
                   )

boundaries.register('place-13',
                    singular='place-13',
                    file='place-13/',
                    name_func=tiger_namer,
                    id_func=geoid_tiger_namer,
                    start_date=date(2012, 1, 1),
                    end_date=date(2015, 1, 1),
                    encoding='latin-1',
                    **defaults
                   )
