import json
import image_functions as img
import pdf_functions as pdf


# Continuati aplicatia cu caini asa cum am mentionat la curs.
# Creati un meniu care ii da voie utilizatorului sa genereze o noua imagine,
# sa vada toate imaginile,
# sa vada numai o imagine (aleasa dintr o lista.)
#
# Modificati codul astfel incat sa nu se mai salveze image_timestamp
# ci sa se salveze image_ceva_specific_din_url_cum_ar_fi_rasa_timestamp
#
# O alta optiune e sa creati un pdf cu o anumita imagine incadrata corect.
# Schimbati size ul imaginii sa fie la fel in pdf indiferent de imagine.



def initialise_config(path: str) ->dict:
    try:
        with open(path, "r") as f:
            config = json.loads(f.read())
    except Exception as e:
        print(f"Unable to initialise project {e}")
        exit(1)
    return config


if __name__ == '__main__':

    config = initialise_config("config.json")
    #
    # image_url = img.get_dog_image_url(config['rest_api_url'])
    #
    # img.save_image(image_url)
    # img.show_images()
    #
    # print(image_url)

    menu = """ 
    1. Genereaza o noua imagine
    2. Afiseaza toate imaginile
    3. Alege rasa de caine pe care ti-o doresti sa o gasesti    
    4. Exit
    """

    while True:
        user_pick = input(menu + " ")

        match user_pick:

            case "1":
                image_url = img.get_dog_image_url(config['rest_api_url'])
                img.save_image(image_url)
            case "2":
                img.save_image(image_url)
            case "3":
                pass
            #
            case "4":
                exit()

    print("\n\n\n\n")
    user_pick = input(menu + " ")

    # pdf.create_pdf("pdf1.pdf")