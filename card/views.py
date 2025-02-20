from django.core.management import call_command
from django.utils import timezone
from django.views.generic import DeleteView, CreateView

from card.models import WhyLook, WhyStop, WhyEat, MyHistory, ZoneRelax, Proiz, Question, Contact


class HistoryDetailView(DeleteView):
    model = MyHistory
    template_name = "front/item_info.html"


from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import WhyLook, WhyStop, WhyEat, MyHistory, ZoneRelax

def main(request):
    # Получение всех необходимых объектов
    whylook = WhyLook.objects.all()
    whystop = WhyStop.objects.all()
    whyeat = WhyEat.objects.all()
    history = MyHistory.objects.all()
    zone = ZoneRelax.objects.all()
    proiz = Proiz.objects.all()
    question = Question.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            current_time = timezone.now().timestamp()
            last_sent_time = request.session.get('last_message_time', 0)

            if current_time - last_sent_time >= ContactCreateView.MESSAGE_COOLDOWN:
                contact = form.save()  # Теперь это работает, так как это ModelForm

                # Отправка уведомления
                call_command('bot', contact.id)
                request.session['last_message_time'] = current_time  # Обновляем время

                return redirect('main:main')  # Используйте правильное имя с namespace
            else:
                # Сообщение о неудаче из-за слишком частых отправок
                request.session['form_submitted'] = False  # Отметка только в случае успеха

                return redirect('main:main')  # Используйте правильное имя с namespace
    else:
        form = ContactForm()

    context = {
        "whylook": whylook,
        "whystop": whystop,
        "whyeat": whyeat,
        "history": history,
        "zone": zone,
        "form": form,
        "proiz": proiz,
        "question": question,
    }

    return render(request, 'main_list.html', context)

class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    MESSAGE_COOLDOWN = 120  # Время ожидания в секундах

    def form_valid(self, form):
        # Получаем текущее время
        current_time = timezone.now().timestamp()
        last_sent_time = self.request.session.get('last_message_time', 0)

        # Проверяем время ожидания
        if current_time - last_sent_time >= self.MESSAGE_COOLDOWN:
            contact = form.save(commit=False)  # Сохраняем форму, но не записываем в БД пока

            # Отправляем уведомление
            call_command('bot', contact.id)
            self.request.session['last_message_time'] = current_time  # Обновляем время последней отправки

            # Теперь сохраняем контакт в БД
            contact.save()

            return super().form_valid(form)
        else:
            # Сообщение о неудаче из-за слишком частых отправок
            self.request.session['form_submitted'] = False  # Отметка только в случае успеха

            # Перенаправляем на страницу main или возвращаем сообщение об ошибке
