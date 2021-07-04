import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Site, Category, State, Region, Iso


def run():
    fhand = open('unesco/many_load.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Site.objects.all().delete()
    Category.objects.all().delete()
    State.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()

    #name,description,justification,year,longitude,latitude,area_hectares,category,state,region,iso

    #Cultural Landscape and Archaeological Remains of the Bamiyan Valley,
    #"<p>The cultural landscape and archaeological remains of the Bamiyan Valley represent the artistic and religious developments which from the 1st to the 13th centuries characterized ancient Bakhtria, integrating various cultural influences into the Gandhara school of Buddhist art. The area contains numerous Buddhist monastic ensembles and sanctuaries, as well as fortified edifices from the Islamic period. The site is also testimony to the tragic destruction by the Taliban of the two standing Buddha statues, which shook the world in March 2001.</p>",
    #"<p><em>Criterion (i):</em> The Buddha statues and the cave art in Bamiyan Valley are an outstanding representation of the Gandharan school in Buddhist art in the Central Asian region.</p> <p><em>Criterion (ii)</em> : The artistic and architectural remains of Bamiyan Valley, and an important Buddhist centre on the Silk Road, are an exceptional testimony to the interchange of Indian, Hellenistic, Roman, Sasanian influences as the basis for the development of a particular artistic expression in the Gandharan school. To this can be added the Islamic influence in a later period.</p> <p><em>Criterion (iii):</em> The Bamiyan Valley bears an exceptional testimony to a cultural tradition in the Central Asian region, which has disappeared.</p> <p><em>Criterion (iv):</em> The Bamiyan Valley is an outstanding example of a cultural landscape which illustrates a significant period in Buddhism.</p> <p><em>Criterion (vi):</em> The Bamiyan Valley is the most monumental expression of the western Buddhism. It was an important centre of pilgrimage over many centuries. Due to their symbolic values, the monuments have suffered at different times of their existence, including the deliberate destruction in 2001, which shook the whole world.</p>",
    #2003,
    #67.82525,
    #34.84694,
    #158.9265,
    #Cultural,
    #Afghanistan,
    #Asia and the Pacific,
    #af

    for row in reader:
        print(row)

        re, is_re_created = Region.objects.get_or_create(name=row[9])
        iso, is_iso_created = Iso.objects.get_or_create(name=row[10])
        st, is_st_created = State.objects.get_or_create(name=row[8])
        ca, is_ca_created = Category.objects.get_or_create(name=row[7])

        try:
            si_year = int(row[3])
        except:
            si_year = None

        try:
            si_longtitude = float(row[4])
        except:
            si_longtitude = None

        try:
            si_latitude = float(row[5])
        except:
            si_latitude = None

        try:
            si_area_hectares = float(row[6])
        except:
            si_area_hectares = None

        si, is_si_created = Site.objects.get_or_create( name=row[0],
                                                        description=row[1],
                                                        justification=row[2],
                                                        year=si_year,
                                                        longtitude=si_longtitude,
                                                        latitude=si_latitude,
                                                        area_hectares=si_area_hectares,
                                                        state=st,
                                                        category=ca,
                                                        iso=iso,
                                                        region=re)