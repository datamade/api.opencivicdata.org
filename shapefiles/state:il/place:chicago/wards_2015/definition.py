from datetime import date

import boundaries

def ocd_id_func(feature):
    return 'ocd-division/country:us/state:il/place:chicago/ward:{0}'.format(feature.get('WARD'))

def ward_namer(feature):
    return 'chicago-ward-{0}'.format(feature.get('WARD'))

boundaries.register('chicago-wards-2015',  
    file='',
    last_updated=date(2015, 9, 15),
    name='Chicago Wards 2015',
    singular='Chicago Ward 2015',
    domain='Chicago',
    authority='City of Chicago',
    source_url='https://data.cityofchicago.org/api/geospatial/sp34-6z76?method=export&format=Original',
    licence_url='',
    start_date=date(2015,5,1),
    end_date=None,
    notes='',
    name_func=ward_namer,
    id_func=ocd_id_func,
    is_valid_func=lambda feature: True,
    label_point_func=lambda feature: None,
)

