
def upload_image(instance, filename):
    format = filename[filename.rindex("."):]
    return f"media/images/{instance.abr}_{instance.id}{format}"
