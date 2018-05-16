Fietsa_spheres = {

    "Fashion": {
        "classic": {
          "Shop" : {"Faina" : "yerevan mall", "Arevik" : "yerevan mall"},
          "Designer" : {"Faina" : "yerevan mall", "Arevik" : "yerevan mall"}},
        "sport": {
          "Shop" : {"Light Affect": "metronom", "KIvetat": "Tashirarmbrands"},
          "Designer": {"Aram": "metronom", "Tatev": "Tashirarmbrands"}},
      },

    "Interests": {
        "Art": {
          "Painter": {"Ivan Aivazovsky": "National Gallery of Armenia", "Minas": "National Gallery of Armenia"},
          "Sculptor": {"Ara Shiraz": "Cascade", "Ara Haroutunyan": "National Gallery of Armenia"}},
        "Music": {
          "singer": {"Aram mp3": "Mezzo", "Sevak": "The Voice"},
          "Band": {"The Band": "Mezzo", "Colorsofmusicband": "Lennon pub"}},
      },

    "Event": {
      "Exhibition": {
        "Vine": {"Ijevan": "Petur", "Ararat": "Saryan"},
        "Book": {"Armenian ": "Beurokrat", "Armenian": "Bookinist"}},

      "Party": {"DJ": "EL-Sky-Bar", "The Band": "Malkhas Juzz Club"}
      },

    "Sport": {
      "gym": {"Gold's gym": "Komitas", "Flex Fitness": "Tumanyan str"},
      "football": {"Pyunik": "Tsicernakaberdi st", "Real Madrid": "Spain"},
      "swimming pool": {"Davit Hambardzumyan": "Davit - Anhaxt", "DDD": "Komitas"}
      },

    "Travel": {
      "health": {"Armenia Wellness & Spa Hotel Jermuk": "Jermuk", "Gorni Armenia": "Dilijan"},
      "sport": {"GENERAL SPORT COMPLEX": "TSAGHKADZOR", "Dilijan resort": "Dilijan"},
      "history": {"Monastery ": "Noravank", "Monastery": "Garni Geghard"}
    }
  }

raw_input("Enter Your name: ")

# for key, value in
print(list(Fietsa_spheres.keys()))

ask_sphere = raw_input("Enter sphere from above: ")

if ask_sphere == "Fashion":
    print(list(Fietsa_spheres["Fashion"].keys()))
    style = raw_input("Enter Styel from above: ")
    if style == "classic" or style == "sport":
      Shop_or_design = raw_input("Enter Shop or Designer: ")
      if Shop_or_design == "Shop":
        print(list(Fietsa_spheres["Fashion"][style]["Shop"].keys()))
        answer = raw_input("Enter name of Shop: ")
        print(Fietsa_spheres["Fashion"][style]["Shop"][answer])
      elif Shop_or_design == "Designer":
        print(list(Fietsa_spheres["Fashion"][style]["Designer"].keys()))
        answer = raw_input("Enter name of Shop: ")
        print(Fietsa_spheres["Fashion"][style]["Designer"][answer])
      else:
        exit()
    else:
      exit()

elif ask_sphere == "Interests":
    print(list(Fietsa_spheres["Interests"].keys()))
    Art_or_Music = raw_input("Enter Art_or_Music from above: ")
    if Art_or_Music == "Art":
      print(list(Fietsa_spheres["Interests"]["Art"].keys()))
      answer = raw_input("Enter Painter or Sculptor: ")
      if answer == "Painter":
        print(list(Fietsa_spheres["Interests"]["Art"]["Painter"].keys()))
        answer = raw_input("Enter Name of Painter: ")
        print(Fietsa_spheres["Interests"]["Art"]["Painter"][answer])
      if answer == "Sculptor":
        print(list(Fietsa_spheres["Interests"]["Art"]["Sculptor"].keys()))
        answer = raw_input("Enter Name of Sculptor: ")
        print(Fietsa_spheres["Interests"]["Art"]["Sculptor"][answer])
    if Art_or_Music == "Music":
      print(list(Fietsa_spheres["Interests"]["Music"].keys()))
      answer = raw_input("Enter singer or Band: ")
      if answer == "singer":
        print(list(Fietsa_spheres["Interests"]["Music"]["singer"].keys()))
        answer = raw_input("Enter Name of singer: ")
        print(Fietsa_spheres["Interests"]["Music"]["singer"][answer])
      if answer == "Band":
        print(list(Fietsa_spheres["Interests"]["Music"]["Band"].keys()))
        answer = raw_input("Enter Name of Band: ")
        print(Fietsa_spheres["Interests"]["Music"]["Band"][answer])

elif ask_sphere == "Event":
    print(list(Fietsa_spheres["Event"].keys()))
    ex_or_party = raw_input("Enter Exhibition or party from above: ")
    if ex_or_party == "Exhibition":
      print(list(Fietsa_spheres["Event"]["Exhibition"].keys()))
      answer = raw_input("Enter Vine  or picture: ")
      if answer == "Vine":
        print(list(Fietsa_spheres["Event"]["Exhibition"]["Vine"].keys()))
        answer = raw_input("Enter Name of Vine: ")
        print(Fietsa_spheres["Event"]["Exhibition"]["Vine"][answer])
      if answer == "Book":
        print(list(Fietsa_spheres["Event"]["Exhibition"]["Book"].keys()))
        answer = raw_input("Enter Name of Book: ")
        print(Fietsa_spheres["Event"]["Exhibition"]["Book"][answer])
    if ex_or_party == "Party":
      print(list(Fietsa_spheres["Event"]["Party"].keys()))
      answer = raw_input("Enter party name: ")
      print(Fietsa_spheres["Event"]["Party"][answer])

elif ask_sphere == "Sport":
    print(list(Fietsa_spheres["Sport"].keys()))
    type = raw_input("Enter sport type from above: ")
    if type == "gym":
      print(list(Fietsa_spheres["Sport"]["gym"].keys()))
      answer = raw_input("Enter name: ")
      print(Fietsa_spheres["Sport"]["gym"][answer])
    if type == "football":
      print(list(Fietsa_spheres["Sport"]["football"].keys()))
      answer = raw_input("Enter name: ")
      print(Fietsa_spheres["Sport"]["football"][answer])
    if type == "swimming pool":
      print(list(Fietsa_spheres["Sport"]["swimming pool"].keys()))
      answer = raw_input("Enter name: ")
      print(Fietsa_spheres["Sport"]["swimming pool"][answer])

elif ask_sphere == "Travel":
    print(list(Fietsa_spheres["Travel"].keys()))
    type = raw_input("Enter Travel type from above: ")
    if type == "health":
      print(list(Fietsa_spheres["Travel"]["health"].keys()))
      answer = raw_input("Enter name: ")
      print(Fietsa_spheres["Travel"]["health"][answer])
    if type == "sport":
      print(list(Fietsa_spheres["Travel"]["sport"].keys()))
      answer = raw_input("Enter name: ")
      print(Fietsa_spheres["Travel"]["sport"][answer])
    if type == "history":
      print(list(Fietsa_spheres["Travel"]["history"].keys()))
      answer = raw_input("Enter name: ")
      print(Fietsa_spheres["Travel"]["history"][answer])

