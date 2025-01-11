from model.Presenter import Presenter
from model.Tvprogramme import Tvprogramme
from model.Tvchannel import Tvchannel


presenter1 = Presenter("Laura", "Tesoro")
presenter2 = Presenter("Nathalie", "Meskens")


programme1 = Tvprogramme("Belgium got talent", presenter1)
programme2 = Tvprogramme("The traitors", presenter2)
programme2.is_active = False

# Shorter way
programma3 = Tvprogramme("The Late Late Show", Presenter("James", "Corden"))

tvchannel1 = Tvchannel("VTM", "NL")
tvchannel2 = Tvchannel("FOX", "ENG")
tvchannel3 = Tvchannel("TV China", "Chinees")   #error

tvchannel1.add_tvprogramme(programme1)
tvchannel1.add_tvprogramme(programme2)
tvchannel2.add_tvprogramme(programma3)
tvchannel2.add_tvprogramme("not very succesfull")

print("\n*** info channels ***")
print(tvchannel1)
print(tvchannel2)
print(tvchannel3)

print(f"\n**** The following programmes are no longer on air: {tvchannel1.name}  ***")
print(tvchannel1.search_inactive_tvprogrammes())

print(f"\n**** This programme is randomly selected from {tvchannel1.name} ***")
print(tvchannel1.select_random_tvprogramme())

