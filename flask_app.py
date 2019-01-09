from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    # found in ../templates/
    return render_template("main_page.html")

def choose_race(trait):
    if trait == "Loyalty":
        return "dwarf"
    if trait == "Beauty":
        return "elf"
    if trait == "Adaptability":
        return "human"
    if trait == "Cunning":
        return "gnome"
    if trait == "Strength":
        return "half-orc"
    return "dragonborn"

def choose_class(weapon):
    if not weapon:
        return "cleric"
    elif "Shield" in weapon:
        if len(weapon) == 1:
            return "coward (seriously, hiding behind a shield while the orcs are attacking?!)"
        else:
            return "paladin"
    elif "A sick guitar" in weapon:
        return "bard"
    elif "Sword" in weapon:
        return "fighter"
    elif "Axe" in weapon:
        return "barbarian"
    elif "Dagger" in weapon or "Bow and arrows" in weapon:
        return "ranger"
    elif "Magic wand" in weapon:
        return "wizard"
    elif "Fists" in weapon:
        return "monk"

def get_first_name(name):
    # Make the name all lowercase and reverse it
    newname = name.lower()[::-1]
    # Replace all vowels with numbers for now
    newname = newname.replace('a', '1')
    newname = newname.replace('e', '2')
    newname = newname.replace('i', '3')
    newname = newname.replace('o', '4')
    newname = newname.replace('u', '5')
    # Now shift all the vowels 2 over by replacing the numbers with a new vowel
    # So, we start with the order a,e,i,o,u
    # a -> 1 -> i
    # e -> 2 -> o, etc.
    newname = newname.replace('1', 'i')
    newname = newname.replace('2', 'o')
    newname = newname.replace('3', 'u')
    newname = newname.replace('4', 'a')
    newname = newname.replace('5', 'e')
    # Now capitalize the first letter.
    return newname.capitalize()

def get_last_name(lastname, petname):
    lastname = lastname.lower()
    petname = petname.lower()
    l = len(lastname) + len(petname)
    index1 = 0
    index2 = 0
    newname = ''
    for i in range(l):
        if index1 < len(lastname) and index2 < len(petname):
            if i % 2 == 0:
                newname = newname + lastname[index1]
                index1+=1
            else:
                newname = newname + petname[index2]
                index2+=1
        else:
            if index1 < len(lastname):
                newname = newname + lastname[index1]
                index1+=1
            else:
                newname = newname + petname[index2]
                index2+=1
    return newname.capitalize()

@app.route('/process_inputs', methods=['POST'])
def process_inputs():
    firstname = request.form.get('input_firstname', '')
    lastname = request.form.get('input_lastname', '')
    petname = request.form.get('input_petname', '')
    trait = request.form.get('input_trait', '')
    weapon = request.form.getlist('input_weapon')

    race = choose_race(trait)
    clazz = choose_class(weapon)
    newfirstname = get_first_name(firstname)
    newlastname = get_last_name(lastname, petname)

    return render_template("main_page.html",
            output="You're a %s %s named %s %s." %
            (race, clazz, newfirstname, newlastname))


if __name__ == "__main__":
    print("test")
    print(get_first_name("Haley"))
    print(get_last_name("Flintstone", "Dino"))


