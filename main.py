import json
import image_functions as img
import pdf_functions as pdf



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
    pdf.create_pdf("pdf1.pdf")