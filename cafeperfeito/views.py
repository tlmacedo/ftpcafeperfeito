import datetime

from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from cafeperfeito.forms import LoginForm
from ftpcafeperfeito.models import Usuario

now = datetime.datetime.now()


class LoginTemplateView(FormView):
    form_class = LoginForm
    template_name = 'cafeperfeito/login.html'
    model = Usuario
    context_object_name = 'usuario'
    extra_context = {'now': now, }
    success_url = reverse_lazy('cafeperfeito:home')
    error_message = 'Deu zebra meu filho'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            usuario = form.valida_usuario()
            user = authenticate(username=usuario.id.apelido, password=form.cleaned_data['senha'])
            login(request, user)
            if user is None:
                messages.error(request, 'usuario não existe')
            else:
                if usuario is False:
                    messages.error(request, 'usuário ou senha invalido')
                else:
                    return self.form_valid(form)
            return self.form_invalid(**{'form': form})
        return render(request, 'cafeperfeito/login.html', {'form': form})


class HomeTemplateView(LoginRequiredMixin, TemplateView):
    login_url = '/'
    permission_denied_message = 'não está conectado'
    raise_exception = True
    redirect_field_name = 'next'

    extra_context = {'now': now}
    template_name = 'cafeperfeito/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeTemplateView, self).get_context_data(**kwargs)
        # home = []
        # nivel_1 = []
        # for nv_1 in Menuprincipal.objects.all():
        #     while nv_1.menupai_id ==1:
        #         nivel_1.append()

        menus = [
            {'text': " MenuPrincipal",
             'href': "#home",
             'icon': "glyphicon glyphicon-home",
             'nodes': [
                 {'text': " Cadastros",
                  'icon': "cafeico",  # "glyphicon glyphicon-home",
                  'nodes': [
                      {'text': " Cadastro de empresa",
                       'href': "#empresa",
                       'icon': "glyphicon glyphicon-home",
                       'selectable': 'true',
                       },

                      {'text': " Cadastro de produto",
                       'href': "#produto",
                       'icon': "glyphicon glyphicon-home",
                       'selectable': 'true',
                       },

                      {'text': " MenuPrincipal",
                       'href': "#home",
                       'icon': "glyphicon glyphicon-home",
                       'selectable': 'true',
                       },
                  ]
                  },

             ]
             },
            {'text': "Parent 2"},
            {'text': "Parent 3"},
            {'text': "Parent 4"},
            {'text': "Parent 5"}]

        # home_item = Menuprincipal.objects.get(id=1)
        # home = {'id': home_item.id, 'menu':home_item.menu, 'menulabel':home_item.menulabel, 'menupai_id':home_item.menupai_id}
        # menus['home']=home
        # for parent1 in Menuprincipal.objects.get(menupai_id=1):
        # for parent2 in Menuprincipal.objects.get(menupai_id=parent1.menupai_id):
        #         for parent3 in Menuprincipal.objects.get(menupai_id=parent2.menupai_id):

        print("menus:", menus)

        # tree = Tree()
        # tree.create_node("Home", "home")
        # for itemMenu in Menuprincipal.objects.all():
        #     if itemMenu.menupai_id != 0:
        #         # print("menulabel:", itemMenu.menulabel)
        #         print("menu:", itemMenu.menu)
        #         # print("menupai_id:", itemMenu.menupai_id)
        #         # print("pesquisa:", Menuprincipal.objects.get(id=itemMenu.menupai_id).menu)
        #         tree.create_node(itemMenu.menulabel, itemMenu.menu,
        #                          parent=Menuprincipal.objects.get(id=itemMenu.menupai_id).menu)
        #     print(tree.get_node(itemMenu.menu))
        # #tree.create_node("Sair", "sair")
        context['logUser'] = Usuario.objects.get(id=self.request.user.id)
        context['menus'] = menus
        return context
    # def get(self, request, *args, **kwargs):
    #     context = super(HomeTemplateView, self).get_context_data(**kwargs)
    #     context['usuario'] = Usuario.objects.get(id=request.user.id)
    #     return context


class EmpresaTemplateView(TemplateView):
    template_name = 'cafeperfeito/empresa.html'

# class MenuView(TemplateView):
#     template_name = 'cafeperfeito/home.html'
#     title = "genre poxa view"
#
#     def get_context_data(self, **kwargs):
#         context = super(MenuView, self).get_context_data(**kwargs)
#
#         menus = [{'text': "Parent 1",
#                   'nodes': [{'text': "Child 1", 'nodes': [{'text': "Grandchild 1"}, {'text': "Grandchild 2"}]},
#                             {'text': "Child 2"}]}, {'text': "Parent 2"}, {'text': "Parent 3"}, {'text': "Parent 4"},
#                  {'text': "Parent 5"}]
#
#         # for x in Menuprincipal.objects.all():
#         #     if x.menupai_id == 0:
#         #         Menutree.objects.create(menu_id=x)
#         #     else:
#         #         Menutree.objects.create(menu_id=x, parent=Menuprincipal.objects.get(id=x.id))
#
#         for x in Menutree.objects.all():
#             print(x.menu_id.menulabel)
#         # rock = Genre.objects.create(name="Rock")
#         # blues = Genre.objects.create(name="Blues")
#         # Genre.objects.create(name="Hard Rock", parent=rock)
#         # Genre.objects.create(name="Pop Rock", parent=rock)
#
#         context['menus'] = menus
#         return context
