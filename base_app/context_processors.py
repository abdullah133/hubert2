from contact_app.models import KontaktInfo


def global_footer_info(request):
    kontaktinfo = KontaktInfo.objects.all().first()
    return {'kontaktinfo':kontaktinfo,}
