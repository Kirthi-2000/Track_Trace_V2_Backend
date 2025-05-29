from django.views.generic import TemplateView

class JigCompositionView(TemplateView):
    template_name = "JigLoading/Jig_Composition.html"

class JigView(TemplateView):
    template_name = "JigLoading/Jig_Picktable.html"

class JigCompletedTable(TemplateView):
    template_name = "JigLoading/Jig_Completedtable.html"