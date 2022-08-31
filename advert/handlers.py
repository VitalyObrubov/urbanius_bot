from django.conf import settings
from django.core.mail import send_mail
import datetime
from telegram import ParseMode,  Update
from telegram.ext import (
    Dispatcher, MessageHandler, Filters,
    CallbackQueryHandler, CommandHandler,
    CallbackContext, ConversationHandler
)
from tgbot.handlers.filters import FilterPrivateNoCommand
from tgbot.models import User, Status
from .models import *
from .messages import *
from .answers import *
from tgbot.handlers.utils import send_message
from tgbot.handlers.keyboard import make_keyboard
from tgbot.handlers.main.answers import get_start_menu
from tgbot.handlers.main.messages import get_start_mess

def use_partner_spec_offer (update: Update, context: CallbackContext):
    """
     Вызывается когда нажимается кнопка "Вроспользоваться предложенем"
     в спец предложении партнера
    """
    query = update.callback_query
    query.answer()
    user_id = query.from_user.id
    user = User.get_user_by_username_or_user_id(user_id)
    query_data = query.data.split("-")
    offer_pk = int(query_data[-1])
    offer = SpecialOffers.objects.get(pk = offer_pk)
    so_discount = offer.specialoffersdiscounts_set.filter(for_status = user.status).first()
    if not so_discount:
        text = f"Для вашего статуса '{user.status}' данное предложение не действует"
        send_message(user_id=user_id, text = text)
        return       
    so_user_reqwest = SOUserRequests.objects.filter(offer = offer,user = user).first()
    if so_user_reqwest:
        send_message(user_id=user_id, text = REQWEST_EXIST)
        return
    so_user_reqwest = SOUserRequests()
    so_user_reqwest.offer = offer
    so_user_reqwest.user = user
    so_user_reqwest.for_status = user.status
    so_user_reqwest.discount = so_discount.discount
    so_user_reqwest.sended_to_partner = True
    so_user_reqwest.save()
    subject = 'URBANIUS BOT: заявка на специальное предложение'
    message = f"Участник URBANIUS CLUB {user.last_name} {user.first_name} {user.sur_name} запросил у Вас скидку "
    message += f"по Вашему специальному предложению: '{offer}' \n"
    message += f"Номер запроса: {so_user_reqwest.pk} \n"
    message += f"Статус участника: {user.status} \n"
    message += f"Размер скидки: {so_user_reqwest.discount}% \n"
    message += f"Телефон: {user.telefon} \n"
    message += f"E-mail: {user.email} \n"
    message += "\n"
    message += "С уважением, URBANIUS BOT"
    send_mail(subject, message, settings.EMAIL_HOST_USER, [offer.partner.email])

    text = f"Вы получили скидку {so_discount.discount}% у партнера '{offer.partner.full_name}' " \
           f"на предложение '{offer}'. Для получения скидки сообщите партнеру ее номер '{so_user_reqwest.pk}'"
    send_message(user_id=user_id, text = text)
 

# Возврат к главному меню
def stop_conversation(update: Update, context: CallbackContext):
    # Заканчиваем разговор.
    if update.message:
        user_id = update.message.from_user.id
    else:
        query = update.callback_query
        query.answer()
        user_id = query.from_user.id
        query.edit_message_reply_markup(make_keyboard(EMPTY,"inline",1))

    user = User.get_user_by_username_or_user_id(user_id)

    send_message(user_id=user_id, text=REQW_FINISH, reply_markup=make_keyboard(EMPTY,"usual",1))
    send_message(user_id=user_id, text=get_start_mess(user), reply_markup=get_start_menu(user))
    return ConversationHandler.END

# Временная заглушка
def blank(update: Update, context: CallbackContext):
    pass

def bad_callback_enter(update: Update, context: CallbackContext):
    update.message.reply_text(ASK_REENTER)
    return "working"

# Начало разговора
def start_conversation(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=HELLO_MESS, reply_markup=make_keyboard(REQW_MNU,"inline",1,None,BACK))

    return "working"


def show_so_reqwests_list(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    user_id = query.from_user.id
    user = User.get_user_by_username_or_user_id(user_id)
    so_reqw_set = user.souserrequests_set.filter(offer__valid_until__gte = datetime.date.today())
    btn_reqw = {}
    for so_reqw in so_reqw_set:
        btn_reqw[f"show_so_reqwest-{so_reqw.pk}"] = str(so_reqw)
    if len(btn_reqw) > 0:
        text = "Выберите вашу заявку для просмотра подробностей"
    else:
        text = "У Вас отсутствуют заявки"    
    reply_markup = make_keyboard(btn_reqw,"inline",1,None,BACK)
    query.edit_message_text(text=text, reply_markup = reply_markup)   
    return "show_so_reqwests_list"

def show_so_reqwest(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    user_id = query.from_user.id
    user = User.get_user_by_username_or_user_id(user_id)
    query_data = query.data.split("-")
    request = SOUserRequests.objects.get(pk = int(query_data[-1]))
    text = f"Вы получили скидку {request.discount}% у партнера '{request.offer.partner.full_name}' " \
           f"на предложение '{request.offer}'. Для получения скидки сообщите партнеру ее номер '{request.pk}'"
    reply_markup = make_keyboard(REQW_LST,"inline",1,None,BACK)
    query.edit_message_text(text = text, reply_markup = reply_markup)
    return "show_so_reqwest"


def setup_dispatcher_conv(dp: Dispatcher):
    dp.add_handler(CallbackQueryHandler(use_partner_spec_offer, pattern="^use_offer-"))

    conv_handler = ConversationHandler( 
        # точка входа в разговор      
        entry_points=[CallbackQueryHandler(start_conversation, pattern="^my_requests$")],      
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            "working":[             
                       CallbackQueryHandler(stop_conversation, pattern="^back$"),
                       CallbackQueryHandler(show_so_reqwests_list, pattern="^so_reqwests$"),
                       MessageHandler(Filters.text & FilterPrivateNoCommand, blank)
                      ],
            "show_so_reqwests_list":[
                          CallbackQueryHandler(stop_conversation, pattern="^back$"),
                          CallbackQueryHandler(show_so_reqwest, pattern="^show_so_reqwest-"),
                          MessageHandler(Filters.text([BACK["back"]]) & FilterPrivateNoCommand, stop_conversation),
                         ],
            "show_so_reqwest":[
                          CallbackQueryHandler(stop_conversation, pattern="^back$"),
                          CallbackQueryHandler(show_so_reqwests_list, pattern="^reqw_lst$"),
                          MessageHandler(Filters.text([BACK["back"]]) & FilterPrivateNoCommand, stop_conversation),
                         ],
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', stop_conversation, Filters.chat_type.private),
                   CommandHandler('start', stop_conversation, Filters.chat_type.private)]        
    )
    dp.add_handler(conv_handler) 