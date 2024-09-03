from django.shortcuts import render, get_object_or_404
from .models import Image

def image(request):
    caracteristiques = ["4pattes", "2pattes", "ailes", "poils", "plumes", 
                        "cornes", "bec", "écailles", "reptile", "queue",
                        "félin", "sabots", "rayures"]
    images = Image.objects.all()
    liste = []
    caracterisqtique_list = []
    get_carac_lenght = 0

    def check(liste1, liste2):
        compt = 0
        for el in liste1:
            if el in liste2:
                compt += 1
            print(">>>>>>>> Compteur: ", compt)
            if compt == len(liste1):
                return True
        return False

    if 'search' in request.GET:
        get_carac = request.GET.getlist('caracteristiques')
        get_carac_lenght = len(get_carac)
        print(">>>>>>>> Get_carac_lenght: ", get_carac_lenght)

        for img in images:
            caracterisqtique_list = img.caracteristique.split('_')
            check_liste = check(get_carac, caracterisqtique_list)
            print(">>>>>>>> Check: ", check_liste)

            if check_liste:
                selected_image = get_object_or_404(Image, id_image=img.id_image)
                print(">>>>>>>> Image: ", selected_image.id_image)
                if selected_image not in liste:
                    liste.append(selected_image)

    context = {
        'liste': liste,
        'caracteristiques': caracteristiques,
        'images': images,
    }
    return render(request, 'index.html', context)